from pathlib import Path
import re,json,runpy
root=Path(__file__).resolve().parents[1]
folder=root/'tools/inscricao'
E=runpy.run_path(str(folder/'data.py'))['E']
source=(root/'exponenciais-logaritmos.html').read_text()
css=re.findall(r'<style>(.*?)</style>',source,re.S)[0]
scripts=re.findall(r'<script>(.*?)</script>',source,re.S)[:2]
nav=re.search(r'<nav[^>]*aria-label="Cadernos de estudo"[^>]*>.*?</nav>',source,re.S).group()
nav=re.sub(r' aria-current="page"','',nav)
link='<a href="inscricao-circunscricao.html">Inscrição e circunscrição · 14 exercícios</a>'
if 'href="inscricao-circunscricao.html"' not in nav:nav=nav.replace('</nav>',link+'</nav>')
nav=nav.replace('href="inscricao-circunscricao.html"','href="inscricao-circunscricao.html" aria-current="page"')
app=(folder/'app.js').read_text().replace('/* DATA */',json.dumps(E,ensure_ascii=False))
html='''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Inscrição e circunscrição · 14 exercícios visuais</title><meta name="description" content="Lista 9 de geometria: 14 exercícios de figuras inscritas e circunscritas, com soluções por etapas e construções interativas."><style>'''+css+'</style><style>'+(folder/'style.css').read_text()+'</style>'+''.join('<script>'+s+'</script>' for s in scripts)+'''</head><body><header class="site-header"><div class="masthead">Álgebra, passo a passo · Geometria · 1º ano</div>'''+nav+r'''<h1>Inscrição e circunscrição.<br>Veja a relação entre as figuras.</h1><p class="intro">As 14 questões da Lista 9 — 2026, com desenhos reconstruídos e soluções visuais interativas. Tente primeiro; depois acompanhe os raios, as alturas e os triângulos que resolvem cada problema.</p><div class="guide"><p><strong>Inscrita:</strong> a figura tem os vértices na circunferência. <strong>Circunscrita:</strong> seus lados são tangentes à circunferência.</p><p>Abra uma solução e avance pelas quatro etapas. O controle de escala varia todas as medidas, para mostrar quais comprimentos mudam e quais razões permanecem iguais.</p><p>No triângulo equilátero: $R=2r$, $h=3r$ e $L=2r\sqrt3$. No hexágono regular: $L=R$ e $a=R\sqrt3/2$.</p></div><a href="#practice">Ir aos 14 exercícios ↓</a></header><main id="practice"><div class="toolbar"><span id="progress" aria-live="polite"></span><label><input id="pending" type="checkbox"> Só pendentes</label><button id="print">Imprimir com soluções</button></div><p id="storage" hidden>O navegador não permitiu salvar o progresso. As marcações continuam disponíveis nesta sessão.</p><noscript>Ative JavaScript para ver os exercícios, as soluções e os controles interativos.</noscript><div id="exercises"></div><p id="empty" hidden>Todos os exercícios estão concluídos. Desmarque “Só pendentes” para revê-los.</p></main><footer>Fonte: Lista 9 — 2026, “Inscrição e Circunscrição de figuras”, Colégio Agostiniano Mendel, professores André, Cadu e Larissa. Enunciados transcritos das duas fotos fornecidas; desenhos reconstruídos sem as anotações manuscritas. Medidas decimais são aproximações. Progresso salvo somente neste navegador. KaTeX e fontes incorporados; funciona sem internet.</footer><script>'''+app+'''\nmath(document.querySelector('.guide'));</script></body></html>'''
(root/'inscricao-circunscricao.html').write_text(html)
for p in root.glob('*.html'):
 if p.name=='inscricao-circunscricao.html':continue
 t=p.read_text()
 def add(m):
  n=m.group()
  if 'href="inscricao-circunscricao.html"' not in n:n=n.replace('</nav>',link+'</nav>')
  return n
 t=re.sub(r'<nav[^>]*aria-label="Cadernos de estudo"[^>]*>.*?</nav>',add,t,flags=re.S)
 p.write_text(t)
print('Lista de inscrição e circunscrição: 14 questões, 14 construções interativas, navegação integrada.')
