import re,sys
T=open('phase1_aveugle/pieces/papier/pain_axis_texte_par_page.txt',encoding='utf-8').read()
parts=re.split(r'===== PAGE (\d+) / 34 =====',T)
P={}
for i in range(1,len(parts),2):
    P[int(parts[i])]=parts[i+1]
def find(pat,pages=None,ctx=80):
    out=[]
    for p,t in P.items():
        if pages and p not in pages: continue
        for m in re.finditer(pat,t,flags=re.S|re.I):
            s=max(0,m.start()-ctx); e=min(len(t),m.end()+ctx)
            out.append((p,t[s:e].replace('\n',' ')))
    return out
if __name__=='__main__':
    pat=sys.argv[1]
    pages=[int(x) for x in sys.argv[2].split(',')] if len(sys.argv)>2 and sys.argv[2] else None
    ctx=int(sys.argv[3]) if len(sys.argv)>3 else 80
    for p,s in find(pat,pages,ctx):
        print(f'[p.{p}] {s}\n')
