import sys,re
from markdown_it import MarkdownIt
t=open(sys.argv[1],encoding='utf8').read()
md=MarkdownIt('commonmark').enable('table')
tokens=md.parse(t)
for k,tok in enumerate(tokens):
    if tok.type in ('code_block','fence'):
        print('CODE BLOCK at line',tok.map, tok.content[:100].replace('\n','|'))
    if tok.type=='inline':
        c=tok.content
        if re.search(r'\n\s*([-*]|\d+\.)\s',c):
            print('LAZY LIST TEXT at', tok.map, repr(c[:150]))
        if '**' in c and c.count('**')%2==1:
            print('ODD ** at', tok.map, repr(c[:120]))
html=md.render(t)
open(sys.argv[2],'w').write(html)
