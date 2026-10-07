import sys, json
W='/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
SRC={'FR':f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md','EN':f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md'}
OUT={'FR':f'{W}/livrable/COURS_Alignment_v3.6_FR_2026-10-02.md','EN':f'{W}/livrable/COURS_Alignment_v3.6_EN_2026-10-02.md'}
res={}
for fi in ('FR','EN'):
    a=open(SRC[fi],encoding='utf8').read().split('\n')
    b=open(OUT[fi],encoding='utf8').read().split('\n')
    m={}
    j=0
    for i,l in enumerate(a):
        while b[j]!=l: j+=1
        m[i+1]=j+1
        j+=1
    res[fi]=m
json.dump(res,open(f'{W}/travail/_verif_groupe_6/map35to36.json','w'))
for fi,(s,e) in (('FR',(2666,3655)),('EN',(2804,3894))):
    print(fi, 'v3.5', s, e, '-> v3.6', res[fi][s], res[fi][e])
