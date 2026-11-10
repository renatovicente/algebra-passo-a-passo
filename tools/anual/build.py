from pathlib import Path
import json,re,runpy,html
F=Path(__file__).resolve().parent; R=F.parents[1]
T=runpy.run_path(str(F/'cursos.py'))['T'];O=runpy.run_path(str(F/'originais.py'))['O'];S=runpy.run_path(str(F/'simulados.py'))['S'];L=runpy.run_path(str(F/'logs.py'))['L']
N=runpy.run_path(str(R/'tools/novembro/data.py'))['T']
notes=[
'O item a está correto. No item b, a conta chega a x≥1/2, mas o intervalo foi escrito na direção oposta. No item c faltou estudar os dois sinais do produto e fazer a interseção.',
'A razão dos valores consecutivos foi invertida. Um gráfico crescente com k positivo exige a>1. A reta pedida no item c precisa de fórmula mx+b.',
'As relações entre raio, diagonal e apótema foram usadas corretamente. Retome como exemplo de acerto e confira a simplificação dos radicais.',
'AB=AD torna ABD isósceles. O ângulo no vértice A é 30°, e os outros dois são 75°. É preciso aplicar a lei dos senos neste triângulo.',
'A montagem 4R=8 está correta, mas a divisão final deve dar 2, não 4. Esse erro foi propagado para o raio central.',
'O calor específico foi calculado corretamente. Na vaporização, use apenas 520000−160000, não o calor acumulado desde o início.',
'As três etapas e os resultados estão corretos. Use este acerto como modelo para separar calor sensível e calor latente.',
'Tempo, velocidade horizontal e módulo √89 foram determinados corretamente. Preserve a separação dos movimentos horizontal e vertical.',
'As componentes foram encontradas corretamente, mas faltou concluir a raiz quadrada que fornece o módulo da velocidade.'
]
assoc={'exponenciais':('Matemática',['m08','m07','m06']),'circunferencias':('Matemática',['m11','m12']),'calorimetria':('Física',['p09']),'lancamento':('Física',['p04','p03'])}
for key,(disc,topics) in assoc.items():
 for q in N[key]['exercises']:
  if not q['original']:continue
  i=len(O)+1;idx=i-54
  O.append(dict(q,id=f'orig-{i:02}',source='Prova de novembro · '+key,discipline=disc,kind='original',topics=topics,note=notes[idx]))
assert len(O)==62
examples={
'm07':('Duas condições ao mesmo tempo',r'Resolva $0<x^2-4x<5$.',[r'$x(x-4)>0$ dá x<0 ou x>4.',r'$x^2-4x-5<0$ dá −1<x<5.',r'Interseccione os intervalos, mantendo as bordas abertas.'],r'$(-1,0)\cup(4,5)$.'),
'm08':O[54], 'p04':O[60], 'p09':O[58],
'm09':L[0],
'm13':('Retângulo e faixa interna','Um retângulo de 6 por 8 m recebe uma faixa interna de 1 m ao longo do contorno. Qual a área central?',['As duas bordas retiram 2 m de cada dimensão.','Dimensões internas: 6−2=4 e 8−2=6 m.','Área central=4·6=24 m². Área da faixa=48−24=24 m².'],'24 m².'),
'p05':('Roda e correia','Uma roda de raio 0,5 m gira a 120 rpm. Ela aciona uma polia de raio 0,2 m, sem deslizamento. Determine a frequência da polia.',[r'$f_1=120/60=2$ Hz.',r'Na borda: $v=2\pi f_1R_1=2\pi$ m/s.',r'$f_2=v/(2\pi R_2)=5$ Hz. A menor polia gira mais vezes por segundo.'],'5 Hz.'),
'p06':('Dois blocos e um fio','Dois blocos de 1 kg e 4 kg estão ligados sobre uma mesa sem atrito. Uma força de 10 N puxa o bloco de 1 kg. Determine aceleração e tração.',['Sistema completo: massa=5 kg, força externa=10 N. Aceleração=10/5=2 m/s².','Isole o bloco de 4 kg: só a tração o acelera horizontalmente. T=4·2=8 N.','Confira no bloco de 1 kg: 10−8=1·2. Peso e normal se equilibram verticalmente.'],'a=2 m/s²; T=8 N.'),
'p10':('Três tipos de dilatação','Uma chapa de área 2 m² e α=2×10⁻⁵ °C⁻¹ aquece 50°C. Determine o aumento da área.',[r'Para pequenas dilatações de um sólido isotrópico, $\beta\approx2\alpha=4\cdot10^{-5}$ °C⁻¹.',r'$\Delta A=A_0\beta\Delta T=2\cdot4\cdot10^{-5}\cdot50=0{,}004$ m².',r'Área final: $A_f=A_0+\Delta A=2{,}004$ m². Não troque aumento por valor final.'],'ΔA=0,004 m²; A final=2,004 m².'),
'p11':('Periélio, afélio e período','Uma órbita em torno do Sol tem distância mínima de 2 UA e máxima de 6 UA. Calcule o semieixo maior e o período.',[r'$a=(2+6)/2=4$ UA. O Sol está em um foco, não no centro da elipse.',r'Com a em UA e T em anos, $T^2\approx a^3=64$.',r'$T=8$ anos. É a raiz positiva, pois o período é um tempo.'],'a=4 UA; T≈8 anos.'),
'q09':('Neutralização e proporção','1 mol de H₂SO₄ reage com 1,5 mol de NaOH. Pela reação global de neutralização completa, determine o sal formado.',['Balanceie H₂SO₄+2NaOH→Na₂SO₄+2H₂O.','Compare quantidade/coeficiente: 1/1=1 e 1,5/2=0,75. NaOH limita.','Formam-se 0,75 mol de Na₂SO₄. Sobram 0,25 mol de ácido no balanço global; a composição iônica real envolve equilíbrios.'],'0,75 mol de Na₂SO₄ no modelo global.'),
'q10':('Nome, fórmula e combustão','Escreva a fórmula do 2-metilbutano e balanceie sua combustão completa.',[r'A cadeia principal tem quatro carbonos e uma ramificação metil no carbono 2. Total: cinco carbonos. Alcano acíclico: $C_5H_{12}$.',r'Balanceie C: 5CO₂. Balanceie H: 6H₂O.',r'Produtos contêm 10+6=16 átomos de O; precisamos de 8O₂. $C_5H_{12}+8O_2\to5CO_2+6H_2O$.'],'C₅H₁₂; C₅H₁₂+8O₂→5CO₂+6H₂O.')
}
for t in T:
 if t['example'] is not None:q=dict(O[t['example']-1])
 else:
  ex=examples[t['id']]
  q=dict(ex) if isinstance(ex,dict) else dict(zip(['title','prompt','steps','answer'],ex))
 q.update(id=t['id']+'-example',kind='example');t['worked']=q
 for i,q in enumerate(t['warmups'],1):q.update(id=t['id']+f'-warm-{i}',topics=[t['id']],title=f'Aquecimento {i}')

# Reference details support the few scientific exceptions discussed in the originals.
O[40]['references']=[['PubChem · metilmetionina (estrutura e contraíon)','https://pubchem.ncbi.nlm.nih.gov/compound/Methylmethionine-sulfonium-chloride']]
O[45]['references']=[['NIST · molibdênio neutro','https://physics.nist.gov/PhysRefData/Handbook/Tables/molybdenumtable1.htm'],['NIST · Mo II (íon Mo⁺)','https://physics.nist.gov/PhysRefData/Handbook/Tables/molybdenumtable6_a.htm']]
O[48]['references']=[['PubChem · fluoreto de mercúrio(I)','https://pubchem.ncbi.nlm.nih.gov/compound/4084556']]

# Repair omitted word spacing in authored prose without modifying LaTeX or formulas.
words='alunos|participam|de nenhum|cadernos|canetas|peças|vezes|dias|anos|meses|minutos|segundos|moléculas|átomos|prótons|elétrons|neutrons|pessoas|notas|unidades|cada|faltas|blocos|ingressos|bactérias|iniciais|de água|de ácido|de base'
def clean(s):
 if isinstance(s,str):
  s=re.sub(r'R\$\s*([0-9]+(?:[.,][0-9]+)*)',r'\1 reais',s)
  s=re.sub(r'\{\\rm ([^{}]+)\}',lambda m:r'{\text{'+m[1]+'}}',s)
  s=re.sub(r'\\mathrm\{([^{}]*[áéíóúãõç][^{}]*)\}',lambda m:r'\text{'+m[1]+'}',s)
  chunks=re.split(r'(\$[^$]*\$)',s)
  for i in range(0,len(chunks),2):
   chunks[i]=re.sub(r'(?<=[A-Za-zÀ-ÿ])(?=\d)',lambda m:' ' if chunks[i][max(0,m.start()-8):m.start()].lower().endswith(('em','de','para','só','soma','tem','há','por','dá','é','logo','então','raiz','formam','consome','sobram','até','a','após','ou','e','são','valem')) else '',chunks[i])
   chunks[i]=re.sub(r'(?<=\d)('+words+r')\b',r' \1',chunks[i],flags=re.I)
   chunks[i]=re.sub(r'\b([A-Za-zÀ-ÿ]{3,})(?=\d)',r'\1 ',chunks[i])
   chunks[i]=re.sub(r'(?<=\d)(mg|kg|cm|mm|km|mL|mol|rpm|Hz|cal|g|m|L|s)(?=\b)',r' \1',chunks[i])
   chunks[i]=re.sub(r'([,;:])(?=[A-Za-zÀ-ÿ])',r'\1 ',chunks[i])
  return ''.join(chunks)
 if isinstance(s,list):return [clean(x) for x in s]
 if isinstance(s,dict):return {k:(v if k in ['id','topics','link','figure','source','references'] else clean(v)) for k,v in s.items()}
 return s
T,O,S,L=map(clean,[T,O,S,L])
labels={'m':'matematica','p':'fisica','q':'quimica'}
navlinks=[('revisao-anual.html','Começar'),('revisao-matematica.html','Matemática'),('revisao-fisica.html','Física'),('revisao-quimica.html','Química'),('provas-originais.html','Provas originais')]+[(f'simulado-anual-{i}.html',f'Simulado {i}') for i in range(1,6)]+[('logaritmos-ilustrados.html','Logaritmos · 14 resoluções')]
base=(R/'index.html').read_text();styles=re.findall(r'<style>(.*?)</style>',base,re.S);scripts=re.findall(r'<script>(.*?)</script>',base,re.S)
nav=re.search(r'<nav[^>]*aria-label="Cadernos de estudo"[^>]*>.*?</nav>',base,re.S).group();nav=re.sub(r' aria-current="page"','',nav)
add=[('revisao-anual.html','Revisão anual e simulados'),('provas-originais.html','Provas originais do ano'),('logaritmos-ilustrados.html','Logaritmos · resolução ilustrada')]
def update_nav(n):
 for url,title in add:
  if f'href="{url}"' not in n:n=n.replace('</nav>',f'<a href="{url}">{title}</a></nav>')
 return n
nav=update_nav(nav)
def linktopic(t):return f'revisao-{labels[t["id"][0]]}.html#{t["id"]}'
TOPICS={t['id']:dict(title=t['title'],url=linktopic(t)) for t in T}
def overview():
 priorities=[('Matemática','Rever fatoração e frações; preencher Venn do centro para fora; distinguir quantidade e valor; traduzir raízes em intervalos.','Acertos úteis: tanque, divisão direta, operador novo, ângulos inversamente proporcionais e parte da geometria.'),('Física','Separar posição, distância e deslocamento; usar áreas em v×t; descontar a reação; concluir o módulo vetorial; usar ΔQ em cada trecho do gráfico.','Acertos úteis: lançamento sobre o fosso, decomposição de velocidade, reflexão plana e etapas da fusão do gelo.'),('Química','Contar elétrons e átomos com a espécie correta; distinguir camada externa e subnível; converter massa, mol e partículas; identificar limitante e excesso.','Acertos úteis: estrutura da ureia, identificação de substância simples e algumas leituras da tabela periódica.')]
 h='<section class="welcome"><p class="eyebrow">Preparação para a prova final</p><h2>Entender, praticar, conferir.</h2><p>34 temas, 102 aquecimentos, 62 questões das provas e cinco simulados com 75 questões inéditas, divididas em 150 itens. Os simulados misturam Matemática, Física e Química; cada um vale 15 pontos para autocorreção.</p><ol><li>Comece pela revisão da disciplina e mexa nos desenhos.</li><li>Faça os três aquecimentos de cada tema sem olhar a resposta.</li><li>Refaça uma questão original relacionada ao erro.</li><li>Resolva um simulado em papel, corrija por item e retorne aos temas que precisarem de revisão.</li></ol></section><h2>O que as resoluções mostram</h2><div class="overview-grid">'
 for disc,p,a in priorities:h+=f'<article class="topic-summary"><h3>{disc}</h3><p>{p}</p><p class="positive">{a}</p></article>'
 h+='</div><p class="source-note">Os comentários descrevem erros visíveis e acertos nas folhas, sem transformar uma questão em diagnóstico geral. Parte dos assuntos já estudados no site não aparece nas novas provas: nesses casos, o material indica que é revisão complementar.</p><h2>Cinco provas, uma cobertura conjunta</h2><p>Cada prova contém 5 questões de Matemática, 5 de Física e 5 de Química. Os 34 temas aparecem no conjunto dos cinco simulados; não é necessário concentrar todos em uma única prova.</p><div class="exam-links">'
 for i in range(1,6):h+=f'<a href="simulado-anual-{i}.html"><strong>Simulado {i}</strong><span>15 questões · 30 itens · 90 minutos sugeridos</span></a>'
 h+='</div><h2>Mapa da revisão</h2><div class="table-wrap"><table><thead><tr><th>Tema e revisão</th><th>Provas originais</th><th>Simulados</th></tr></thead><tbody>'
 for t in T:
  originals=[q for q in O if t['id'] in q['topics']];sim=[str(i+1) for i,qs in enumerate(S) if any(t['id'] in q['topics'] for q in qs)]
  ol=', '.join(f'<a href="provas-originais.html#{q["id"]}">{q["id"][5:]}</a>' for q in originals) or 'Revisão complementar'
  h+=f'<tr><td><a href="{linktopic(t)}">{html.escape(t["title"])}</a></td><td>{ol}</td><td>{", ".join(sim)}</td></tr>'
 h+='</tbody></table></div><details class="source-note"><summary>Fontes, cobertura e correções do material</summary><p>Foram examinadas 53 novas fotografias de provas da pasta Lara e os anexos anteriores. As 9 questões de prova de novembro foram acrescentadas uma única vez, sem repetir fotos do mesmo exercício. As listas de áreas (20 questões) e logaritmos (14 questões) já estavam no site; continuam disponíveis. A nova aba de logaritmos amplia as 14 resoluções.</p><p>A numeração 01–53 identifica as fotos na ordem de inventário; 54–62 são as questões de novembro. O título mantém o número da questão na prova. Quando a figura continha dados, eles foram transcritos no enunciado e redesenhados quando necessário. As imagens com nome, nota e escrita pessoal não são publicadas.</p><p>Resultados foram recalculados, sem assumir que toda marca de correção ou gabarito é infalível. Há notas específicas sobre a questão das três redes sociais (550 pessoas), a notação ambígua da questão 7 de logaritmos, a fórmula estrutural da vitamina U e o mercúrio(I). Nos modelos de dosagem e crescimento, as contas são exercícios escolares, sem aplicação prática de saúde.</p></details>'
 return h
css=(R/'tools/inscricao/style.css').read_text()+'\n'+(F/'style.css').read_text()
alljs=(F/'visuals.js').read_text()+'\n'+(F/'figures.js').read_text()+'\n'+(F/'app.js').read_text()
def emit(file,title,subtitle,mode,qs=None,topics=None,number=None):
 localnav='<nav class="annual-tabs" aria-label="Revisão e provas">'+''.join(f'<a href="{url}"'+(' aria-current="page"' if url==file else '')+f'>{text}</a>' for url,text in navlinks)+'</nav>'
 data=dict(mode=mode,questions=qs or [],topics=topics or [],topicIndex=TOPICS,number=number)
 body=overview() if mode=='overview' else '<div id="app"></div>'
 h='<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="icon" href="data:,"><title>'+title+' · Álgebra, passo a passo</title><style>'+styles[0]+'</style><style>'+css+'</style>'+''.join('<script>'+s+'</script>' for s in scripts[:2])+'</head><body><a class="skip" href="#main">Ir ao conteúdo</a><header class="site-header"><div class="masthead">Álgebra, passo a passo · Revisão anual</div><details class="all-notebooks"><summary>Todos os cadernos do site</summary>'+nav+'</details>'+localnav+'<h1>'+title+'</h1><p class="intro">'+subtitle+'</p></header><main id="main">'+body+'</main><footer>Revisão preparada a partir das provas e listas fornecidas. Resoluções conferidas em novembro de 2026. Progresso, rascunhos e autocorreção ficam apenas neste navegador. Fotos e dados pessoais das provas não são publicados.</footer><noscript>Ative JavaScript para abrir as questões, soluções e controles visuais.</noscript><script>const PAGE='+json.dumps(data,ensure_ascii=False).replace('</',r'<\/')+';\n'+alljs+'</script></body></html>'
 (R/file).write_text(h)
emit('revisao-anual.html','Revisão do ano, passo a passo','Um percurso de estudo construído a partir das provas, dos erros observados e dos assuntos já trabalhados.', 'overview')
for prefix,slug in labels.items():
 ts=[t for t in T if t['id'][0]==prefix]
 emit('revisao-'+slug+'.html','Revisão de '+ts[0]['discipline'],f'{len(ts)} temas · {len(ts)*3} aquecimentos · exemplos resolvidos e demonstrações para explorar.','course',topics=ts)
emit('provas-originais.html','As questões das provas','62 questões originais, com enunciados, resolução por etapas e comentários sobre o que revisar.','originals',qs=O)
for i,qs in enumerate(S,1):emit(f'simulado-anual-{i}.html',f'Simulado anual {i}','Matemática, Física e Química · 15 questões · 30 itens · 15 pontos · 90 minutos sugeridos.','exam',qs=qs,number=i)
emit('logaritmos-ilustrados.html','Logaritmos, problema por problema','As 14 questões da escola, com resolução completa, desenhos explicativos e comentários sobre cada passagem.','logs',qs=L)
for p in R.glob('*.html'):
 old=p.read_text();new=re.sub(r'<nav[^>]*aria-label="Cadernos de estudo"[^>]*>.*?</nav>',lambda m:update_nav(m.group()),old,flags=re.S)
 if old!=new:p.write_text(new)
(F/'content.json').write_text(json.dumps(dict(topics=T,originals=O,simulations=S,logs=L),ensure_ascii=False,indent=2))
print('11 novas abas; 34 temas; 102 aquecimentos; 62 originais; 75 questões de simulado; 14 logaritmos ilustrados.')
