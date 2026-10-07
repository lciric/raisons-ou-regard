import re
from pages import P
D=open('phase1_aveugle/livrable/AXE_DOULEUR_PISTES_INDEPENDANTES_2026-10-02.md',encoding='utf-8').read()
def norm(s):
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('–','-').replace('—','-').replace('−','-')
    s=re.sub(r'-\s*\n\s*','',s)
    s=re.sub(r'\s+',' ',s)
    return s.lower()
PN={p:norm(t) for p,t in P.items()}
ALL=' '.join(PN[p] for p in sorted(PN))
lines=D.split('\n')
seen=set()
for i,l in enumerate(lines,1):
    for m in re.finditer(r'«\s*([^«»]+?)\s*»',l):
        q=m.group(1)
        # english-ish: count ascii words
        words=re.findall(r"[A-Za-z']+",q)
        fr=re.findall(r"[àâçéèêëîïôûùüÿœ]",q)
        if len(words)<1 or fr: continue
        nq=norm(q).strip(' .,;:')
        nq2=re.sub(r'…|\.\.\.','',nq).strip()
        found=[p for p in PN if nq2 and nq2 in PN[p]]
        # page refs in the rest of line after quote
        tail=l[m.end():m.end()+60]
        pr=re.findall(r'p\.\s*(\d+)',tail)
        key=(nq2,tuple(pr[:1]))
        if key in seen: continue
        seen.add(key)
        status='OK' if found else 'NOTFOUND'
        if found and pr and int(pr[0]) not in found: status='PAGE?'
        if status!='OK':
            print(f'{i}: [{status}] «{q}» cited p.{pr[:1]} found {found}')
