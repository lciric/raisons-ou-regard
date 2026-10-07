import json,re
W='/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
OUT={'FR':f'{W}/livrable/COURS_Alignment_v3.6_FR_2026-10-02.md','EN':f'{W}/livrable/COURS_Alignment_v3.6_EN_2026-10-02.md'}
B={k:open(v,encoding='utf8').read().split('\n') for k,v in OUT.items()}
def locate(fi,text):
    first=text.split('\n')[0]
    idx=[i for i,l in enumerate(B[fi]) if l==first]
    return idx
def heading(fi,i):
    for j in range(i,0,-1):
        l=B[fi][j]
        if l.startswith('## ') or l.startswith('### '):
            return l[:60]
        m=re.match(r'^\*\*(A\d+|B\d+|\d) ·',l)
    return '?'
def subhead(fi,i):
    # nearest preceding bold label like **A10 · or **1. or ### «
    for j in range(i,max(0,i-80),-1):
        l=B[fi][j]
        m=re.match(r'^\*\*(A\d+ ·|\d\. )',l)
        if m: return m.group(1)
        if l.startswith('## ') or l.startswith('### '): return ''
    return ''
for t in ['volet11_1_a_20','volet11_21_a_52','volet11_53_et_fin']:
    d=json.load(open(f'{W}/travail/insertions_{t}.json',encoding='utf8'))
    ins=d['insertions']
    fr=[x for x in ins if x['fichier']=='FR']; en=[x for x in ins if x['fichier']=='EN']
    print(t,len(fr),len(en))
    for k,(a,b) in enumerate(zip(fr,en)):
        ia=locate('FR',a['texte']); ib=locate('EN',b['texte'])
        ha=heading('FR',ia[0]) if ia else '??'; hb=heading('EN',ib[0]) if ib else '??'
        sa=subhead('FR',ia[0]) if ia else ''; sb=subhead('EN',ib[0]) if ib else ''
        na=re.match(r'^#+ ([^«]*)',ha); nb=re.match(r'^#+ ([^«]*)',hb)
        flag='' if (ha.split('«')[0]==hb.split('«')[0] or ha==hb) else '  <-- TITRES DIFFÉRENTS'
        kind=lambda x: 'renvoi' if '**Limites et parades** :' in x or '**Limits and workarounds**:' in x else ('encadre' if '— ' in x.split('\n')[0] and ('Limites et parades —' in x or 'Limits and workarounds —' in x) else 'ponctuel')
        print(f"  paire {k+1}: FR n°{2*k+1} l.{ia[0]+1 if ia else '?'} [{kind(a['texte'])}] {ha} {sa} | EN n°{2*k+2} l.{ib[0]+1 if ib else '?'} [{kind(b['texte'])}] {hb} {sb}{flag}")
