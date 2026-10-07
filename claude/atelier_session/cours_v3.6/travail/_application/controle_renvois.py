import json,glob,re,collections
W='/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
PRE={'FR':'> ⚠ **Limites et parades** : ','EN':'> ⚠ **Limits and workarounds**: '}
SEP={'FR':' ; ','EN':'; '}
def parse(line,fi):
    s=line[len(PRE[fi]):]
    s=re.sub(r'\s*\*\(v3\.6\)\*\s*$','',s)
    out=[]
    # découpe sur le séparateur hors guillemets
    parts=[];buf='';depth=0
    i=0
    while i<len(s):
        c=s[i]
        if c in '«“"' and not (c=='"' and depth and s[i]=='"'):
            pass
        if s.startswith(SEP[fi],i) and depth==0:
            parts.append(buf);buf='';i+=len(SEP[fi]);continue
        if c in '«(': depth+=1
        if c in '»)': depth=max(0,depth-1)
        buf+=c;i+=1
    parts.append(buf)
    for p in parts:
        if '→' in p:
            a,b=p.split('→',1); out.append((a.strip().lower(),b.strip()))
        else: out.append((p.strip().lower(),None))
    return out
index={'FR':{},'EN':{}}
ins=[]
for f in sorted(glob.glob(f'{W}/travail/insertions_*.json')):
    d=json.load(open(f,encoding='utf8'))
    for n,z in enumerate(d['insertions'],1): ins.append((d['tranche'],n,z))
# index = renvois contenus dans la note d'ouverture
for tr,n,z in ins:
    if tr=='tete_volet1' and n in (1,2):
        for l in z['texte'].split('\n'):
            if l.startswith(PRE[z['fichier']]):
                for a,b in parse(l,z['fichier']): index[z['fichier']][a]=b
print({k:len(v) for k,v in index.items()})
pb=collections.defaultdict(list); n_ref=collections.Counter()
for tr,n,z in ins:
    fi=z['fichier']
    for l in z['texte'].split('\n'):
        if l.startswith(PRE[fi]):
            for a,b in parse(l,fi):
                n_ref[fi]+=1
                if a not in index[fi]: pb[fi].append(f'{tr} n°{n}: instrument absent de l\'index « {a} » → {b}')
                elif b!=index[fi][a]: pb[fi].append(f'{tr} n°{n}: « {a} » → « {b} » ; index : « {index[fi][a]} »')
print('références lues:',dict(n_ref))
for fi in ('FR','EN'):
    print(f'--- {fi}: {len(pb[fi])} écart(s)')
    for x in pb[fi][:40]: print('  ',x[:300])
