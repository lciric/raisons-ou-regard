import re, sys
from markdown_it import MarkdownIt
path = sys.argv[1]
t = open(path, encoding='utf-8').read()
md = MarkdownIt('commonmark').enable('table')
html = md.render(t)
print('== balises')
for tag in ['div', 'section']:
    o = len(re.findall(rf'<{tag}\b', t)); c = len(re.findall(rf'</{tag}>', t))
    print(tag, o, c, 'OK' if o == c else 'DESEQUILIBRE')
print('== marques @@')
marks = re.findall(r'@@(P[0-9A-Z]+)@@', t)
print(sorted(set(marks)), len(marks))
print('== marqueur 62a1 :', t.count('[[RÉSULTATS_62a1]]'))
print('== HTML : blocs suivis d une ligne vide')
lines = t.split('\n')
for i, l in enumerate(lines):
    if re.match(r'\s*<(div|section)\b', l) and i + 1 < len(lines) and lines[i+1].strip() != '':
        print('  pas de ligne vide après', i+1, l[:60])
print('== rendu : restes suspects')
txt = re.sub(r'<code>.*?</code>', '', html, flags=re.S)
for m in re.finditer(r'<p>(.*?)</p>', txt, re.S):
    p = m.group(1)
    if re.search(r'\n\d+\. ', p) or re.search(r'\n- ', p) or '|---' in p or re.search(r'(^|\n)\|', p):
        print('  P:', p[:160].replace('\n', ' / '))
    if '**' in p:
        print('  ** restant :', p[:160])
for m in re.finditer(r'<li>(.*?)</li>', txt, re.S):
    if '**' in re.sub(r'<[^>]+>', '', m.group(1)):
        print('  ** restant dans li:', m.group(1)[:160])
print('== tables rendues', html.count('<table>'), '; lignes de tableau dans le source', len(re.findall(r'^\|---', t, re.M)))
# ordered lists starting not at 1 rendered
print('== listes ordonnées avec start', re.findall(r'<ol start="(\d+)"', html))
