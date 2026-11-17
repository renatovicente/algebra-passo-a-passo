"""Build two offline workbooks and integrate navigation without external assets."""
from pathlib import Path
import html
import json
import re
import runpy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PAGES = runpy.run_path(str(HERE / 'data.py'))['PAGES']
render_figure = runpy.run_path(str(HERE / 'figures.py'))['render']
base = (ROOT / 'index.html').read_text()
katex_css = re.findall(r'<style>(.*?)</style>', base, re.S)[0]
scripts = re.findall(r'<script>(.*?)</script>', base, re.S)[:2]
assert len(scripts) == 2 and 'renderMathInElement' in scripts[1]
nav_pattern = r'<nav[^>]*aria-label="Cadernos de estudo"[^>]*>.*?</nav>'
source_nav = re.search(nav_pattern, base, re.S).group()
source_nav = re.sub(r' aria-current="page"', '', source_nav)
links = [(p['slug']+'.html', p['label']) for p in PAGES]


def update_nav(nav):
    for filename, label in links:
        if f'href="{filename}"' not in nav:
            nav = nav.replace('</nav>', f'<a href="{filename}">{label}</a></nav>')
    return nav


def prose(value):
    # Isolate a literal currency dollar sign from KaTeX's math delimiters.
    return 'R<span class="currency">$</span>'.join(
        re.sub(r'(\$[^$]+\$)', r'<span class="math-inline">\1</span>', html.escape(part))
        for part in value.split('R$'))


def card(q):
    choices = ('<ol class="choices" type="A" aria-label="Alternativas">' + ''.join('<li>'+prose(choice)+'</li>' for choice in q['choices'])+'</ol>') if q['choices'] else ''
    diagram = render_figure(q['figure']) if q['figure'] else ''
    note = ('<div class="source-note"><strong>Nota de transcrição</strong><p>'+prose(q['note'])+'</p></div>') if q['note'] else ''
    warning = '<p class="small">Há uma duplicação de impressão no original; veja a observação na solução.</p>' if q['note'] else ''
    sign_table = ''
    if q['id'] == 'mat-05':
        sign_table = '<div class="table-scroll"><table><caption>Sinais do produto nos intervalos entre as raízes</caption><thead><tr><th>Intervalo</th><th>x + 2</th><th>x</th><th>x − 3</th><th>Produto</th></tr></thead><tbody>'
        for interval, signs in [(r'$x<-2$', ['−','−','−','−']), (r'$-2<x<0$', ['+','−','−','+']), (r'$0<x<3$', ['+','+','−','−']), (r'$x>3$', ['+','+','+','+'])]:
            sign_table += '<tr><th scope="row">'+prose(interval)+'</th>'+''.join('<td>'+s+'</td>' for s in signs)+'</tr>'
        sign_table += '</tbody></table></div>'
    return f'''<article class="card" id="{q['id']}" data-topic="{html.escape(q['topic'])}">
<div class="card-heading"><span class="number">Questão {q['number']:02}</span><h3 id="title-{q['id']}">{html.escape(q['title'])}</h3><span class="topic-tag">{html.escape(q['topic'])}</span></div>
<p class="prompt">{prose(q['prompt'])}</p>{warning}{diagram}{choices}
<div class="actions interactive-tools"><label><input type="checkbox" aria-label="Marcar questão {q['number']} como concluída">Entendi e refiz</label><a class="permalink" href="#{q['id']}">Link da questão</a></div>
<details class="solution-toggle"><summary>Ver solução · Questão {q['number']:02}</summary><div class="solution" aria-labelledby="title-{q['id']}">{note}<h4>Passo a passo</h4><ol>{''.join('<li>'+prose(s)+'</li>' for s in q['steps'])}</ol>{sign_table}
<p class="answer"><strong>Resposta:</strong> {prose(q['answer'])}</p><div class="pitfall"><strong>De olho no erro comum</strong>{prose(q['pitfall'])}</div></div></details></article>'''


css = (ROOT/'tools/revisao-logaritmos/style.css').read_text() + '\n' + (HERE/'style.css').read_text()
for page in PAGES:
    qs = page['items']; count = len(qs); slug = page['slug']; title = page['title']
    nav = update_nav(source_nav).replace(f'href="{slug}.html"', f'href="{slug}.html" aria-current="page"')
    sibling_nav = '<nav class="list-tabs" aria-label="Listas de 17 de novembro">'+''.join(f'<a href="{name}"'+(' aria-current="page"' if name==slug+'.html' else '')+f'>{label}</a>' for name,label in links)+'</nav>'
    formulas = ''.join('<div><span>'+label+'</span><p>'+prose(formula)+'</p></div>' for label,formula in page['formulas'])
    topics = list(dict.fromkeys(q['topic'] for q in qs))
    key = ''.join(f'<li><a data-jump data-solution href="#{q["id"]}">Questão {q["number"]:02}</a><span>{prose(q["answer"])}</span></li>' for q in qs)
    jumps = '<nav class="question-jumps" aria-label="Ir a uma questão">'+''.join(f'<a data-jump href="#{q["id"]}">{q["number"]:02}</a>' for q in qs)+'</nav>'
    result = (HERE/'template.html').read_text()
    replacements = {
        '/* KATEX_CSS */': katex_css, '/* PAGE_CSS */': css, '/* KATEX_JS */': scripts[0], '/* AUTORENDER_JS */': scripts[1],
        '/* PAGE_APP */': (HERE/'app.js').read_text(), '<!-- NOTEBOOK_NAV -->': nav, '<!-- LIST_NAV -->': sibling_nav,
        '{{TITLE}}':html.escape(title), '{{DESCRIPTION}}':html.escape(page['description']), '{{SUBTITLE}}':html.escape(page['subtitle']),
        '{{INTRO}}':html.escape(page['intro']), '{{COUNT}}':str(count), '{{SLUG}}':slug,
        '{{GUIDE}}':html.escape(page['guide']), '{{GUIDANCE}}':html.escape(page['guidance']),
        '<!-- FORMULAS -->':formulas, '<!-- JUMPS -->':jumps, '<!-- QUESTIONS -->':''.join(card(q) for q in qs),
        '<!-- TOPICS -->':''.join('<option value="'+html.escape(t)+'">'+html.escape(t)+'</option>' for t in topics),
        '<!-- ANSWER_KEY -->':key,
    }
    for marker, value in replacements.items(): result = result.replace(marker,value)
    assert not re.search(r'\{\{[A-Z]+\}\}',result)
    (ROOT/(slug+'.html')).write_text(result)
    print(f'{slug}.html: {count} questões e {sum(bool(q["figure"]) for q in qs)} figuras.')

updated=0
for path in ROOT.glob('*.html'):
    old=path.read_text()
    new=re.sub(nav_pattern,lambda m:update_nav(m.group()),old,flags=re.S)
    if old!=new: path.write_text(new); updated+=1
(HERE/'content.json').write_text(json.dumps(PAGES,ensure_ascii=False,indent=2)+'\n')
print(f'Navegação atualizada em {updated} cadernos existentes.')
