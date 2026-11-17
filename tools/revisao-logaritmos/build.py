"""Build the offline workbook and add its tab to the existing workbooks."""
from pathlib import Path
import html
import json
import re
import runpy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FILENAME = 'logaritmos-prova-treino.html'
LABEL = 'Revisão de logaritmos · prova + 20 treinos'
ITEMS = runpy.run_path(str(HERE / 'data.py'))['ITEMS']
assert len(ITEMS) == 27 and sum(q['kind'] == 'treino' for q in ITEMS) == 20
assert len({q['id'] for q in ITEMS}) == len(ITEMS)
escape = html.escape


def prose(text):
    # A long formula scrolls within its own line on a phone, not the whole page.
    return re.sub(r'(\$[^$]+\$)', r'<span class="math-inline">\1</span>', escape(text))

base = (ROOT / 'index.html').read_text()
styles = re.findall(r'<style>(.*?)</style>', base, re.S)
scripts = re.findall(r'<script>(.*?)</script>', base, re.S)
assert styles and len(scripts) >= 2 and 'renderMathInElement' in scripts[1]
NAV_PATTERN = r'<nav[^>]*aria-label="Cadernos de estudo"[^>]*>.*?</nav>'
new_link = f'<a href="{FILENAME}">{LABEL}</a>'


def add_link(nav):
    if f'href="{FILENAME}"' in nav:
        return nav
    # Keep this focused revision beside the existing logarithms workbook.
    target = re.search(r'<a href="logaritmos.html"[^>]*>.*?</a>', nav)
    if target:
        return nav[:target.end()] + new_link + nav[target.end():]
    return nav.replace('</nav>', new_link + '</nav>')


nav = re.search(NAV_PATTERN, base, re.S).group()
nav = add_link(re.sub(r' aria-current="page"', '', nav))
nav = nav.replace(f'href="{FILENAME}"', f'href="{FILENAME}" aria-current="page"')
topics = list(dict.fromkeys(q['topic'] for q in ITEMS))


def card(q):
    reference = (f'<a class="example-link" data-jump href="#{q["reference"]}">Rever o exemplo das fotos ↗</a>'
                 if q['reference'] else '<span class="small">Enunciado das fotos · resolução conferida</span>')
    return f'''<article class="card" id="{q['id']}" data-kind="{q['kind']}" data-topic="{escape(q['topic'])}">
<div class="card-heading"><span class="number">{q['label']}</span><h3 id="title-{q['id']}">{escape(q['title'])}</h3><span class="topic-tag">{escape(q['topic'])}</span></div>
<p class="prompt">{prose(q['prompt'])}</p>
<div class="actions"><label class="interactive-tools"><input type="checkbox" aria-label="Marcar {q['label']} como concluído">Entendi e refiz</label>{reference}</div>
<details class="solution-toggle"><summary>Ver solução · {q['label']}</summary><div class="solution" aria-labelledby="title-{q['id']}"><h4>Passo a passo</h4><ol>{''.join('<li>'+prose(step)+'</li>' for step in q['steps'])}</ol>
<p class="answer"><strong>Resposta:</strong> {prose(q['answer'])}</p><div class="pitfall"><strong>De olho no erro comum</strong>{prose(q['pitfall'])}</div></div></details></article>'''


content = ''
for kind, anchor, title, description in [
    ('original', 'originais', '01 · As questões das fotos', '4 questões · 7 itens, na numeração original'),
    ('treino', 'treino', '02 · Agora, tente você', '20 problemas novos, dos fundamentos às equações'),
]:
    content += f'<section class="question-group" id="{anchor}" aria-labelledby="heading-{anchor}"><div class="section-heading"><h2 id="heading-{anchor}">{title}</h2><p>{description}</p></div>'
    content += ''.join(card(q) for q in ITEMS if q['kind'] == kind) + '</section>'

key = ''.join(f'<li><a data-jump href="#{q["id"]}">{q["label"]}</a><span>{prose(q["answer"])}</span></li>' for q in ITEMS)
template = (HERE / 'template.html').read_text()
for marker, value in {
    '/* KATEX_CSS */': styles[0], '/* KATEX_JS */': scripts[0], '/* AUTORENDER_JS */': scripts[1],
    '/* REVIEW_CSS */': (HERE / 'style.css').read_text(), '/* REVIEW_APP */': (HERE / 'app.js').read_text(),
    '<!-- NOTEBOOK_NAV -->': nav, '<!-- EXERCISES -->': content, '<!-- ANSWER_KEY -->': key,
    '<!-- TOPICS -->': ''.join(f'<option value="{escape(topic)}">{escape(topic)}</option>' for topic in topics),
}.items():
    template = template.replace(marker, value)
(ROOT / FILENAME).write_text(template)

updated = 0
for path in ROOT.glob('*.html'):
    old = path.read_text()
    new = re.sub(NAV_PATTERN, lambda m: add_link(m.group()), old, flags=re.S)
    if old != new:
        path.write_text(new)
        updated += 1
(HERE / 'content.json').write_text(json.dumps(ITEMS, ensure_ascii=False, indent=2) + '\n')
print(f'{FILENAME}: 7 itens originais + 20 treinos. Navegação atualizada em {updated} páginas.')
