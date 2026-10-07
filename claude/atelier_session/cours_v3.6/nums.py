import re,sys
from pages import P
D=open('phase1_aveugle/livrable/AXE_DOULEUR_PISTES_INDEPENDANTES_2026-10-02.md',encoding='utf-8').read().split('\n')
a,b=int(sys.argv[1]),int(sys.argv[2])
def norm(t):
    t=t.replace('−','-').replace('–','-')
    return t
PN={p:norm(t) for p,t in P.items()}
for i in range(a-1,min(b,len(D))):
    l=D[i]
    pages=set()
    for m in re.finditer(r'p\.\s*(\d+)(?:\s*[-–]\s*(\d+))?((?:\s*(?:,|et)\s*\d+)*)',l):
        x=int(m.group(1)); y=int(m.group(2)) if m.group(2) else x
        pages.update(range(x,y+1))
        for z in re.findall(r'\d+',m.group(3) or ''): pages.add(int(z))
    if not pages: continue
    # numbers with decimal comma or percent or signed
    nums=re.findall(r'(?<![\w/.])([+−-]?\d+(?:,\d+)?)(?=\s*%|\b)',l)
    bad=[]
    for n in nums:
        v=n.replace('−','-').replace(',','.')
        core=v.lstrip('+-')
        if len(core)<=1: continue
        if re.fullmatch(r'\d+',core) and int(core) in pages: continue
        if any(core in PN[p] for p in pages if p in PN): continue
        bad.append(n)
    if bad:
        print(f'{i+1} pages={sorted(pages)} missing={sorted(set(bad))}')
