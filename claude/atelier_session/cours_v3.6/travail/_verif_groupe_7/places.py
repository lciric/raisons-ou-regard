import json, re, sys
W='/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
SRC={'FR':f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md','EN':f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md'}
OUT={'FR':f'{W}/livrable/COURS_Alignment_v3.6_FR_2026-10-02.md','EN':f'{W}/livrable/COURS_Alignment_v3.6_EN_2026-10-02.md'}
TR={'volet11_1_a_20':{'FR':(3656,4128),'EN':(3895,4403)},'volet11_21_a_52':{'FR':(4129,4729),'EN':(4404,5037)},'volet11_53_et_fin':{'FR':(4730,5377),'EN':(5038,5702)}}
def kind(l):
    s=l.strip()
    if not s: return 'VIDE'
    if s.startswith('|'): return 'TABLE'
    if re.match(r'^(\-|\*|\d+\.)\s',s): return 'LISTE'
    if s.startswith('#'): return 'TITRE'
    if s.startswith('>'): return 'CITATION'
    if s.startswith('```'): return 'CODE'
    return 'TEXTE'
res={}
for fi in ('FR','EN'):
    a=open(SRC[fi],encoding='utf8').read().split('\n')
    b=open(OUT[fi],encoding='utf8').read().split('\n')
    # map v3.5 index -> v3.6 index
    m={}; j=0
    for i,l in enumerate(a):
        while b[j]!=l: j+=1
        m[i]=j; j+=1
    res[fi]=(a,b,m)
json.dump({fi:{str(k):v for k,v in res[fi][2].items()} for fi in res},open(f'{W}/travail/_verif_groupe_7/map35to36.json','w'))
for t,rng in TR.items():
    d=json.load(open(f'{W}/travail/insertions_{t}.json',encoding='utf8'))
    n=0
    for k,ins in enumerate(d['insertions'],1):
        fi=ins['fichier']; a,b,m=res[fi]
        lo,hi=rng[fi]
        idx=[i for i in range(lo-1,hi) if a[i].strip()==ins['ancre'].strip()][0]
        nxt=a[idx+1] if idx+1<len(a) else ''
        prv=a[idx-1]
        # find v3.6 line of the insertion text first line
        first=ins['texte'].split('\n')[0]
        pos=[x for x in range(m[idx],m[idx+1]) if b[x]==first]
        print(f"{t} n°{k} {fi} ancre v3.5 l.{idx+1} ({kind(a[idx])}) suivante:{kind(nxt)} précédente:{kind(prv)} -> v3.6 l.{pos[0]+1 if pos else '?'} ; ancre 'À dire'? {'À dire' in a[idx] or 'To say' in a[idx]}")
