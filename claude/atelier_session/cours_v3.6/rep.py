import sys,json
F='phase1_aveugle/livrable/AXE_DOULEUR_PISTES_INDEPENDANTES_2026-10-02.md'
def rep(pairs):
    s=open(F,encoding='utf-8').read()
    for a,b in pairs:
        n=s.count(a)
        assert n==1,(n,a[:80])
        s=s.replace(a,b)
    open(F,'w',encoding='utf-8').write(s)
    print('ok',len(pairs))
