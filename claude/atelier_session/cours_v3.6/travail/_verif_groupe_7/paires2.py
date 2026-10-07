import json,re
W='/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
SRC={'FR':f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md','EN':f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md'}
OUT={'FR':f'{W}/livrable/COURS_Alignment_v3.6_FR_2026-10-02.md','EN':f'{W}/livrable/COURS_Alignment_v3.6_EN_2026-10-02.md'}
TR={'volet11_1_a_20':{'FR':(3656,4128),'EN':(3895,4403)},'volet11_21_a_52':{'FR':(4129,4729),'EN':(4404,5037)},'volet11_53_et_fin':{'FR':(4730,5377),'EN':(5038,5702)}}
A={k:open(v,encoding='utf8').read().split('\n') for k,v in SRC.items()}
B={k:open(v,encoding='utf8').read().split('\n') for k,v in OUT.items()}
M=json.load(open('map35to36.json'))
def heading(fi,i):
    for j in range(i,0,-1):
        l=B[fi][j]
        if l.startswith('## ') or l.startswith('### '):
            return l
    return '?'
def sub(fi,i):
    for j in range(i,max(0,i-120),-1):
        l=B[fi][j]
        m=re.match(r'^\*\*(A\d+) ·',l) or re.match(r'^\*\*(\d)\. ',l)
        if m: return m.group(1)
        if l.startswith('## ') or l.startswith('### '): return ''
    return ''
def key(h):
    h=h.lstrip('#').strip()
    m=re.match(r'^([A-Z]?\d+(?: à A17)?) ·',h)
    if m: return m.group(1)
    return h[:25]
rows=[]
for t,rng in TR.items():
    d=json.load(open(f'{W}/travail/insertions_{t}.json',encoding='utf8'))
    out={'FR':[],'EN':[]}
    for n,ins in enumerate(d['insertions'],1):
        fi=ins['fichier']; lo,hi=rng[fi]
        idx=[i for i in range(lo-1,hi) if A[fi][i].strip()==ins['ancre'].strip()][0]
        j36=M[fi][str(idx)]
        # insertion lines follow after anchor: find first line equal to texte first line after j36
        first=ins['texte'].split('\n')[0]
        k=j36+1
        while B[fi][k]!=first: k+=1
        out[fi].append((n,idx+1,k+1,heading(fi,k),sub(fi,k),ins['texte']))
    for (a,b) in zip(out['FR'],out['EN']):
        ka=key(a[3]); kb=key(b[3])
        same = ka==kb or (a[3].startswith('### «') and b[3].startswith('### «'))
        rows.append((t,a,b,same))
for t,a,b,same in rows:
    print(f"{t} FR n°{a[0]} (v3.5 l.{a[1]}, v3.6 l.{a[2]}) [{key(a[3])}{'/'+a[4] if a[4] else ''}] | EN n°{b[0]} (v3.5 l.{b[1]}, v3.6 l.{b[2]}) [{key(b[3])}{'/'+b[4] if b[4] else ''}]" + ('' if same and a[4]==b[4] else '   <-- À VOIR'))
