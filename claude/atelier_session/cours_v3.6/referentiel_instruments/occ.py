import re, json, sys
W='/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
SRC={'FR':f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md','EN':f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md'}
TR = {
    'tete_volet1':       {'FR': (1, 181),     'EN': (1, 248)},
    'volet_M':           {'FR': (182, 411),   'EN': (249, 496)},
    'volet2_A_a_D':      {'FR': (412, 666),   'EN': (497, 755)},
    'volet2_E_a_I':      {'FR': (667, 884),   'EN': (756, 1006)},
    'volet3':            {'FR': (885, 1110),  'EN': (1007, 1251)},
    'volets4_5_entete':  {'FR': (1111, 1368), 'EN': (1252, 1563)},
    'volet6':            {'FR': (1369, 1626), 'EN': (1564, 1791)},
    'volet7_B_et_D':     {'FR': (1627, 2069), 'EN': (1792, 2203)},
    'volet7_A_et_C':     {'FR': (2070, 2665), 'EN': (2204, 2803)},
    'volets8_9':         {'FR': (2666, 2935), 'EN': (2804, 3178)},
    'volet10':           {'FR': (2936, 3655), 'EN': (3179, 3894)},
    'volet11_1_a_20':    {'FR': (3656, 4128), 'EN': (3895, 4403)},
    'volet11_21_a_52':   {'FR': (4129, 4729), 'EN': (4404, 5037)},
    'volet11_53_et_fin': {'FR': (4730, 5377), 'EN': (5038, 5702)},
}
L={k:open(v,encoding='utf8').read().split('\n') for k,v in SRC.items()}
def tranche(fi,n):
    for k,v in TR.items():
        a,b=v[fi]
        if a<=n<=b: return k
def section(fi,n):
    for i in range(n-1,-1,-1):
        s=L[fi][i]
        if s.startswith('#'): return f'{i+1}:{s[:90]}'
    return ''
pat=sys.argv[1]; fi=sys.argv[2] if len(sys.argv)>2 else 'FR'
r=re.compile(pat,re.I)
res={}
for i,l in enumerate(L[fi]):
    if r.search(l):
        t=tranche(fi,i+1); s=section(fi,i+1)
        res.setdefault(t,{}).setdefault(s,[]).append(i+1)
for t,d in res.items():
    print('==',t, sum(len(x) for x in d.values()))
    for s,ls in d.items(): print('   ',s,'->',ls[:12])
