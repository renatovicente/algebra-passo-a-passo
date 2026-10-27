"""Rebuild the exam using the existing offline math bundle and site navigation."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
folder = root / 'tools/prova-fisica2'
source = (root / 'index.html').read_text()
styles = re.findall(r'<style>(.*?)</style>', source, re.S)
scripts = re.findall(r'<script>(.*?)</script>', source, re.S)
if not styles or len(scripts) < 2 or 'renderMathInElement' not in scripts[1]:
    raise RuntimeError('O caderno de álgebra precisa incluir KaTeX e auto-render.')
nav_pattern = r'<nav[^>]*aria-label="Cadernos de estudo"[^>]*>.*?</nav>'
nav = re.search(nav_pattern, source, re.S).group()
nav = re.sub(r' aria-current="page"', '', nav)
link = '<a href="prova-fisica-2.html">Física · Prova 2</a>'
if 'href="prova-fisica-2.html"' not in nav:
    nav = nav.replace('</nav>', link + '</nav>')
nav = nav.replace('href="prova-fisica-2.html"', 'href="prova-fisica-2.html" aria-current="page"')

html = (folder / 'template.html').read_text()
for marker, content in {
    '/* KATEX_CSS */': styles[0],
    '/* KATEX_JS */': scripts[0],
    '/* AUTORENDER_JS */': scripts[1],
    '/* EXAM_CSS */': (folder / 'style.css').read_text(),
    '/* EXAM_DATA */': (folder / 'data.js').read_text(),
    '/* EXAM_ANIMATIONS */': (folder / 'animations.js').read_text(),
    '/* EXAM_APP */': (folder / 'app.js').read_text(),
    '<!-- EXAM_NAV -->': nav,
}.items():
    html = html.replace(marker, content)
(root / 'prova-fisica-2.html').write_text(html)

for path in root.glob('*.html'):
    if path.name == 'prova-fisica-2.html':
        continue
    original = path.read_text()
    def insert(match):
        nav = match.group()
        return nav if 'href="prova-fisica-2.html"' in nav else nav.replace('</nav>', link + '</nav>')
    updated = re.sub(nav_pattern, insert, original, flags=re.S)
    if updated != original:
        path.write_text(updated)
print('Física 2: 5 novas questões, 10 itens, cronômetros de 15 minutos e 5 soluções animadas. Navegação integrada.')
