"""Build the self-contained workbook and add its tab to the existing notebooks."""
from pathlib import Path
import html
import json
import re
import runpy
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
QUESTIONS = runpy.run_path(str(HERE / 'data.py'))['QUESTIONS']
SLUG = 'plano-inclinado.html'
LINK = f'<a href="{SLUG}">Física · Plano inclinado</a>'
base = (ROOT / 'index.html').read_text()
nav_pattern = r'<nav[^>]*aria-label="Cadernos de estudo"[^>]*>.*?</nav>'


def update_nav(nav):
    return nav if f'href="{SLUG}"' in nav else nav.replace('</nav>', LINK + '</nav>')


def prose(text):
    return re.sub(r'(\$[^$]+\$)', r'<span class="math-inline">\1</span>', html.escape(text))


# Save fully rendered default figures so enunciados and solutions also work without JS.
source = (HERE / 'physics.js').read_text() + '\n' + (HERE / 'visuals.js').read_text()
source += '\nconst questions=' + json.dumps(QUESTIONS, ensure_ascii=False) + ';\n'
source += 'console.log(JSON.stringify(questions.map(q=>({prompt:InclineVisuals.motion(InclinePhysics.state(q,q.lab.base,0),true),forces:InclineVisuals.forces(InclinePhysics.state(q,q.lab.base,1)),motion:InclineVisuals.motion(InclinePhysics.state(q,q.lab.base,0)),graph:InclineVisuals.graph(InclinePhysics.state(q,q.lab.base,0))}))));'
figures = json.loads(subprocess.run(['node', '-e', source], check=True, text=True, capture_output=True).stdout)


def lab(q, fig):
    n = q['id']; info = q['lab']; force_only = info['kind'] == 'forces'
    controls = ''.join(f'''<div class="parameter"><label for="q{n}-{c['key']}">{html.escape(c['label'])}<output id="q{n}-{c['key']}-value" for="q{n}-{c['key']}"></output></label><input type="range" id="q{n}-{c['key']}" data-param="{c['key']}" data-unit="{c['unit']}" min="{c['min']}" max="{c['max']}" step="{c['step']}" value="{info['base'][c['key']]}"></div>''' for c in info['controls'])
    motion = '' if force_only else '<figure class="diagram"><figcaption>Movimento · esquema com escala ajustável</figcaption><div class="motion">' + fig['motion'] + '</div></figure>'
    graph = '' if force_only else '<details class="graph-wrap lab-controls"><summary>Ver gráfico v × t · a área representa o deslocamento</summary><p class="small">A inclinação da reta é a aceleração. A região preenchida é a área até o instante escolhido; abaixo do eixo, ela conta negativamente.</p><div class="velocity-graph">' + fig['graph'] + '</div></details>'
    energy = '<div class="energy lab-controls"><p class="small">Energia por unidade de massa · azul: cinética; ocre: potencial. Referência U = 0 no início da rampa.</p><div class="energy-bar" aria-hidden="true"><span class="energy-k"></span><span class="energy-u"></span></div><p class="energy-values"></p></div>' if info['kind'] == 'up' else ''
    axis = ('Positivo: para cima da rampa.' if n in (3,4,6) else 'Positivos: A em direção à polia e B descendo a rampa.' if n == 7 else 'Positivos: M descendo a rampa e m verticalmente para cima.' if n == 8 else 'Positivo: para baixo da rampa.')
    label = 'Etapas do raciocínio' if force_only else 'Instante do movimento'
    return f'''<section class="lab" aria-labelledby="lab-title-{n}"><p class="eyebrow">Laboratório da questão {n:02}</p><h4 id="lab-title-{n}">{info['title']}</h4>
<p class="model-label">{'Exemplo numérico ilustrativo' if info.get('example') else 'Dados da lista'}</p><p class="lab-note">{info['note']}</p><p class="axis-note">{axis}</p>
<div class="diagram-grid{' single' if force_only or n>=7 else ''}">{motion}<figure class="diagram"><figcaption>Diagrama de forças · vetores com escala comum</figcaption><div class="force-diagram">{fig['forces']}</div></figure></div>
<div class="legend"><span style="--color:#b04a2b">P: peso</span><span style="--color:#286b90">N: normal</span><span style="--color:#946300">T: tração</span><span style="--color:#72519a">F: aplicada</span></div>
<p class="small">No desenho do movimento, v (azul) é velocidade e a (roxo) é aceleração. Elas não são forças.</p>
<label class="component-control lab-controls"><input class="components" type="checkbox"{' checked' if force_only else ''}>Decompor o peso nos eixos da rampa</label><p class="component-note">As componentes P∥ e P⊥ são projeções do peso, não forças adicionais. Na soma das forças, use P ou suas componentes. O P tracejado serve apenas como referência.</p>
<dl class="readouts" aria-label="Valores no instante escolhido"></dl>
<div class="player lab-controls"><label class="scrub-label" for="time-{n}">{label}<span class="scrub-value"></span></label><input class="scrub" id="time-{n}" type="range" min="0" max="100" step="0.1" value="0"><div class="player-controls"><button data-action="play" aria-pressed="false">Reproduzir</button><button data-action="prev">Etapa anterior</button><button data-action="next">Próxima etapa</button><button data-action="start">Voltar ao início</button></div><p class="player-status" role="status">A reprodução usa um ritmo didático. O tempo físico aparece no controle.</p></div>
<p class="stage-caption lab-controls"></p>{graph}{energy}
<details class="explore lab-controls"><summary>Explore outros valores</summary><p class="small">Mude um dado por vez e compare. A resolução escrita acima preserva os dados originais.</p><div class="parameter-grid">{controls}</div><button data-action="restore">{'Restaurar exemplo inicial' if info.get('example') else 'Restaurar dados iniciais'}</button><div class="live-equations"></div><p class="insight">{info['insight']}</p></details>
<p class="print-lab-note">Impressão com os parâmetros iniciais e o instante final da visualização.</p></section>'''


def card(q, fig):
    n = q['id']
    note = '<aside class="source-note"><strong>Hipótese da resolução</strong><p>' + prose(q['note']) + '</p></aside>' if q['note'] else ''
    parts = '<ul class="parts">'+''.join('<li>'+prose(p)+'</li>' for p in q['parts'])+'</ul>' if q['parts'] else ''
    choices = '<ol type="A" class="choices" aria-label="Alternativas">'+''.join('<li>'+prose(c)+'</li>' for c in q['choices'])+'</ol>' if q['choices'] else ''
    return f'''<article class="card" id="q{n}" data-topic="{q['topic']}"><div class="card-heading"><span class="number">Questão {n:02}</span><h3 id="title-{n}">{q['title']}</h3><span class="topic-tag">{q['topic']}</span></div><p class="prompt">{prose(q['prompt'])}</p>{parts}{choices}{note}
<figure class="exercise-figure">{fig['prompt']}<figcaption>Esquema do enunciado · desenho sem escala</figcaption></figure>
<div class="actions interactive-tools"><label><input class="done-check" type="checkbox" aria-label="Marcar questão {n} como concluída">Entendi e refiz</label><a class="permalink" href="#q{n}">Link da questão</a></div>
<details class="solution-toggle"><summary>Ver solução e explorar · Questão {n:02}</summary><div class="solution" aria-labelledby="title-{n}"><h4>Resolução com os dados da lista</h4><ol>{''.join('<li>'+prose(s)+'</li>' for s in q['steps'])}</ol><p class="answer"><strong>Resposta:</strong> {prose(q['answer'])}</p><div class="pitfall"><strong>De olho no erro comum</strong>{prose(q['pitfall'])}</div>{lab(q,fig)}</div></details></article>'''


template = (HERE / 'template.html').read_text()
katex_scripts = re.findall(r'<script>(.*?)</script>', base, re.S)[:2]
nav = update_nav(re.search(nav_pattern, base, re.S).group())
nav = re.sub(r' aria-current="page"', '', nav).replace(f'href="{SLUG}"', f'href="{SLUG}" aria-current="page"')
values = {
    'KATEX_CSS': re.findall(r'<style>(.*?)</style>', base, re.S)[0],
    'PAGE_CSS': (ROOT/'tools/revisao-logaritmos/style.css').read_text()+'\n'+(HERE/'style.css').read_text(),
    'KATEX_JS': katex_scripts[0], 'AUTORENDER_JS': katex_scripts[1],
    'NOTEBOOK_NAV': nav,
    'TOPICS': ''.join(f'<option>{t}</option>' for t in dict.fromkeys(q['topic'] for q in QUESTIONS)),
    'QUESTIONS': ''.join(card(q,f) for q,f in zip(QUESTIONS,figures)),
    'ANSWER_KEY': ''.join(f'<li><a data-jump data-solution href="#q{q["id"]}">Questão {q["id"]:02} · abrir resolução</a><span>{prose(q["answer"])}</span></li>' for q in QUESTIONS),
    'EXERCISE_DATA': json.dumps(QUESTIONS,ensure_ascii=False).replace('</','<\\/'),
    'PAGE_APP': '\n'.join((HERE/f).read_text() for f in ['physics.js','visuals.js','app.js']),
}
values['JUMPS'] = '<nav class="question-jumps" aria-label="Ir para uma questão">'+''.join(f'<a data-jump href="#q{q["id"]}">{q["id"]:02}</a>' for q in QUESTIONS)+'</nav>'
for key,value in values.items():
    template = template.replace('{{'+key+'}}', value)
assert not re.search(r'\{\{[A-Z_]+\}\}',template)
(ROOT/SLUG).write_text(template)
(HERE/'content.json').write_text(json.dumps(QUESTIONS,ensure_ascii=False,indent=2)+'\n')
count = 0
for path in ROOT.glob('*.html'):
    if path.name == SLUG: continue
    old = path.read_text()
    updated = re.sub(nav_pattern,lambda m:update_nav(m.group()),old,flags=re.S)
    if old != updated: path.write_text(updated); count += 1
print(f'{SLUG}: 8 exercícios, 8 laboratórios; navegação atualizada em {count} páginas.')
