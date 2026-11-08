from pathlib import Path
import re,json,runpy
root=Path(__file__).resolve().parents[1];folder=root/'tools/novembro'
T=runpy.run_path(str(folder/'data.py'))['T']
base=(root/'index.html').read_text();styles=re.findall(r'<style>(.*?)</style>',base,re.S);scripts=re.findall(r'<script>(.*?)</script>',base,re.S)
nav=re.search(r'<nav[^>]*aria-label="Cadernos de estudo"[^>]*>.*?</nav>',base,re.S).group();nav=re.sub(r' aria-current="page"','',nav)
links={k:f'<a href="novembro-{k}.html">{t["title"].split(" · ")[0]} · listas de novembro</a>' for k,t in T.items()}
for k,l in links.items():
 if f'href="novembro-{k}.html"' not in nav:nav=nav.replace('</nav>',l+'</nav>')
css=(root/'tools/inscricao/style.css').read_text()+'''
.prompt{white-space:normal}.section-nav{display:flex;flex-wrap:wrap;gap:20px;margin:25px 0}.section-nav a{color:inherit}summary{cursor:pointer;font-weight:700}h2{font:normal 32px Georgia,serif;margin:36px 0 16px}select{font:inherit;padding:8px;max-width:100%}.intro .katex{font-size:1em}#lab{margin-bottom:30px}.source-note{padding:18px;border-left:3px solid #a04f2c;background:#fff4e5}figcaption{font-size:12px;color:var(--muted)}.prompt-figure{max-width:520px}.step-status{font-size:14px;color:var(--muted)}.answer summary{min-height:44px}.full-steps li{padding:12px;background:#f0f3e7}.geo-card h3{margin:0}.toolbar label{display:flex;align-items:center;gap:8px}@media print{#introduction,#warmup,.section-nav,.source-note{display:none!important}.solution{display:none!important}.print-solutions .solution,.print-solutions .full-steps li{display:block!important}.print-solutions .answer>p{display:block!important}.play-controls,.step-status,.reveal,.solution>p,.answer summary{display:none!important}.geo-card[hidden]{display:block!important}.solution .answer{display:block!important}}
'''
for key,t in T.items():
 n=len(t['exercises']);o=sum(q['original'] for q in t['exercises']);nv=nav.replace(f'href="novembro-{key}.html"',f'href="novembro-{key}.html" aria-current="page"')
 app=(folder/'app.js').read_text().replace('/* DATA */',json.dumps(t,ensure_ascii=False)).replace('/* KEY */',json.dumps(key))
 html='<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+t['title']+' · Álgebra, passo a passo</title><style>'+styles[0]+'</style><style>'+css+'</style>'+''.join('<script>'+s+'</script>' for s in scripts[:2])+'''</head><body><header class="site-header"><div class="masthead">Álgebra, passo a passo · 1º ano</div>'''+nv+f'''<h1>{t['title']}</h1><p class="intro">{o} questões originais + 10 de treino · {len(t['warmup'])} aquecimentos à parte.</p><nav class="section-nav" aria-label="Seções desta lista"><a href="#introduction">Entender e explorar</a><a href="#warmup">Aquecer</a><a href="#practice">Resolver</a></nav></header><main><section id="introduction"><h2>Uma ideia antes das contas.</h2><p class="intro">{t['intro']}</p><div class="interactive" id="lab"></div></section><section id="warmup"><h2>Aquecimento · pré-requisitos</h2><p>Reveja estas ferramentas antes da lista principal. Os aquecimentos não entram na contagem dos dez exercícios novos.</p><div id="warmups"></div></section><section id="practice"><h2>Agora, resolva no papel.</h2><details class="source-note"><summary>Sobre os anexos e pontos de atenção</summary><p>{t['note']}</p></details><div class="toolbar"><span id="progress" aria-live="polite"></span><label>Mostrar <select id="filter"><option value="all">Toda a lista</option><option value="true">Originais da escola</option><option value="false">Dez exercícios de treino</option></select></label><button id="print-questions">Imprimir questões</button><button id="print-solutions">Imprimir com soluções</button></div><p id="storage-note" hidden>O navegador não permitiu salvar o progresso; as marcações funcionam nesta sessão.</p><noscript>Ative JavaScript para carregar as questões e demonstrações.</noscript><div id="exercises"></div></section></main><footer>Material organizado a partir das provas, listas e anotações enviadas em 6 de novembro de 2026. Números originais preservados; enunciados reescritos quando necessário para descrever figuras, sem alterar os dados. Alternativas são identificadas no gabarito quando relevantes. Fotos e dados pessoais não são publicados. Progresso salvo apenas neste navegador.</footer><script>'''+app+'</script></body></html>'
 if key=='kepler':
  html=html.replace('</head>','<style>'+(folder/'kepler-lesson.css').read_text()+'</style></head>')
  html=html.replace('<section id="warmup">',(folder/'kepler-lesson.html').read_text()+'<section id="warmup">')
  html=html.replace('</body>','<script>'+(folder/'kepler-lesson.js').read_text()+'</script></body>')
  html=html.replace('<section id="introduction">','<section id="introduction" hidden>')
  html=html.replace('href="#introduction"','href="#kepler-course"')
 (root/f'novembro-{key}.html').write_text(html)
for p in root.glob('*.html'):
 def update(m):
  n=m.group()
  for k,l in links.items():
   if f'href="novembro-{k}.html"' not in n:n=n.replace('</nav>',l+'</nav>')
  return n
 s=p.read_text();new=re.sub(r'<nav[^>]*aria-label="Cadernos de estudo"[^>]*>.*?</nav>',update,s,flags=re.S)
 if s!=new:p.write_text(new)
(folder/'data.json').write_text(json.dumps(T,ensure_ascii=False,indent=2))
print('8 abas; '+str(sum(len(t['exercises']) for t in T.values()))+' questões principais; 80 de treino; '+str(sum(len(t['warmup']) for t in T.values()))+' aquecimentos.')
