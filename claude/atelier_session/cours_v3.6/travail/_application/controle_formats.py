import json,glob,re,collections
W='/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
H={'FR':{'enc':r'^> \*\*⚠ Limites et parades — .+\*\* \*\(v3\.6, 2 octobre 2026\)\*$',
         'ren':r'^> ⚠ \*\*Limites et parades\*\* : .+ \*\(v3\.6\)\*$',
         'pon':r'^> ⚠ \*\(v3\.6\)\* \S',
         'lim':r'^> - \*\*Limite :\*\* ', 'par':r'^>   \*\*Parade :\*\* ', 'src':r'\*\(source : [^)]*\)\*|\*\(source : .*\)\*'},
   'EN':{'enc':r'^> \*\*⚠ Limits and workarounds — .+\*\* \*\(v3\.6, 2 October 2026\)\*$',
         'ren':r'^> ⚠ \*\*Limits and workarounds\*\*: .+ \*\(v3\.6\)\*$',
         'pon':r'^> ⚠ \*\(v3\.6\)\* \S',
         'lim':r'^> - \*\*Limit:\*\* ', 'par':r'^>   \*\*Workaround:\*\* ', 'src':r'\*\(source: .*\)\*'}}
NONE={'FR':r'aucune (?:parade )?connue','EN':r'none known|no workaround(?: is)? known|no known workaround'}
pb=collections.defaultdict(list); kinds=collections.Counter(); sans_marque=[]
for f in sorted(glob.glob(f'{W}/travail/insertions_*.json')):
    d=json.load(open(f,encoding='utf8')); tr=d['tranche']
    for n,z in enumerate(d['insertions'],1):
        fi=z['fichier']; t=z['texte'].rstrip(); ls=t.split('\n'); h=H[fi]
        if 'v3.6' not in t: sans_marque.append(f'{tr} n°{n} ({fi}) « {ls[0][:90]} »')
        if re.match(h['enc'],ls[0]):
            k='encadre'
            # corps : ligne '>' puis paires Limite/Parade
            if ls[1].strip()!='>': pb[k].append(f'{tr} n°{n} {fi}: 2e ligne non vide')
            i=2
            while i<len(ls):
                l=ls[i]
                if re.match(h['lim'],l):
                    if not re.search(h['src'],l): pb[k].append(f'{tr} n°{n} {fi}: limite sans source: {l[:90]}')
                    if i+1>=len(ls) or not re.match(h['par'],ls[i+1]):
                        pb[k].append(f'{tr} n°{n} {fi}: limite sans parade à la ligne suivante: {l[:80]}')
                    else:
                        p=ls[i+1]
                        if not re.search(h['src'],p) and not re.search(NONE[fi],p):
                            pb[k].append(f'{tr} n°{n} {fi}: parade sans source ni « aucune connue »: {p[:100]}')
                    i+=2; continue
                pb[k].append(f'{tr} n°{n} {fi}: ligne hors format: {l[:100]}'); i+=1
        elif re.match(h['ren'],ls[0]) and len(ls)==1: k='renvoi'
        elif re.match(h['pon'],ls[0]):
            k='ponctuel'
            if len(ls)>1: pb[k].append(f'{tr} n°{n} {fi}: avertissement ponctuel sur {len(ls)} lignes')
            if '(source' not in t and '(cours' not in t and '(fiche' not in t and '(course' not in t and '(reading' not in t and 'source' not in t:
                pb[k].append(f'{tr} n°{n} {fi}: avertissement ponctuel sans source apparente: {ls[0][:100]}')
        elif '★' in ls[0]: k='encadre_2oct'
        else:
            k='autre'; pb[k].append(f'{tr} n°{n} {fi}: {ls[0][:100]}')
        kinds[(k,fi)]+=1
print(dict(sorted(kinds.items())))
print('sans mention v3.6:',len(sans_marque)); [print('  ',s) for s in sans_marque]
for k,v in pb.items():
    print(f'--- {k}: {len(v)} écart(s)'); [print('  ',x) for x in v[:25]]
