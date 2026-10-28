from pathlib import Path
import re
r=Path(__file__).resolve().parent.parent
d=r/'tools/quimica'
base=(r/'index.html').read_text()
styles=re.findall(r'<style>(.*?)</style>',base,re.S)
scripts=re.findall(r'<script>(.*?)</script>',base,re.S)
nav=re.search(r'<nav class="page-tabs" aria-label="Cadernos de estudo">.*?</nav>',base,re.S).group()
nav=re.sub(r' aria-current="page"','',nav)
link='<a href="prova-quimica.html">Prova · Química</a>'
if 'href="prova-quimica.html"' not in nav: nav=nav.replace('</nav>',link+'</nav>')
nav=nav.replace('href="prova-quimica.html"','href="prova-quimica.html" aria-current="page"')
t=(d/'template.html').read_text()
for marker,value in {'/* KATEX_CSS */':styles[0],'/* KATEX_JS */':scripts[0],'/* AUTORENDER_JS */':scripts[1],'/* EXAM_CSS */':(d/'style.css').read_text(),'/* EXAM_DATA */':(d/'data.js').read_text(),'/* EXAM_APP */':(d/'app.js').read_text(),'<!-- EXAM_NAV -->':nav}.items(): t=t.replace(marker,value)
(r/'prova-quimica.html').write_text(t)
for p in r.glob('*.html'):
 s=p.read_text()
 def add(m):
  n=m.group()
  return n if 'href="prova-quimica.html"' in n else n.replace('</nav>',link+'</nav>')
 s=re.sub(r'<nav class="page-tabs" aria-label="Cadernos de estudo">.*?</nav>',add,s,flags=re.S)
 p.write_text(s)
