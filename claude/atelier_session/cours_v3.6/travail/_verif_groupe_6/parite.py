import re, json, collections
def blocks(path):
    t=open(path,encoding='utf8').read()
    parts=re.split(r'^### Insertion n°(\d+), après la ligne (\d+) de la v3\.5\n', t, flags=re.M)
    out=[]
    for i in range(1,len(parts),3):
        n=int(parts[i]); body=parts[i+2]
        # remove anchor line
        body='\n'.join(l for l in body.split('\n') if not l.startswith('> Ancre'))
        out.append((n,body.strip()))
    return out
def toks(s, lang):
    s=s.replace(' ',' ')
    T=collections.Counter()
    for m in re.finditer(r'F·(\d+)', s): T['F'+m.group(1)]+=1
    for m in re.finditer(r'\b(K\d+|G1|JB10)\b', s): T[m.group(1)]+=1
    if lang=='FR':
        for m in re.finditer(r'volet (\w+)', s): T['V'+m.group(1)]+=1
        for m in re.finditer(r'n° (\d+)', s): T['n'+m.group(1)]+=1
        for m in re.finditer(r'fiches?,? partie B, piège (\d+)', s): T['trap'+m.group(1)]+=1
        for m in re.finditer(r'\bfiche (\d+)', s): T['sheet'+m.group(1)]+=1
        T['README']+=len(re.findall(r'README', s))
        T['handover']+=len(re.findall(r'passation', s))
        T['expl']+=len(re.findall(r'explication du 2 octobre', s))
        T['prog']+=len(re.findall(r'programme, partie', s))
        T['none']+=len(re.findall(r'aucune (parade )?connue', s))
        T['partC']+=len(re.findall(r'fiches, partie C', s))
    else:
        for m in re.finditer(r'Part (\w+)', s): T['V'+m.group(1)]+=1
        for m in re.finditer(r'no\. (\d+)', s): T['n'+m.group(1)]+=1
        for m in re.finditer(r'reading sheets?,? part B, trap (\d+)', s): T['trap'+m.group(1)]+=1
        for m in re.finditer(r'reading sheet (\d+)', s): T['sheet'+m.group(1)]+=1
        T['README']+=len(re.findall(r'README', s))
        T['handover']+=len(re.findall(r'handover', s))
        T['expl']+=len(re.findall(r'explanation of 2 October', s))
        T['prog']+=len(re.findall(r'programme, part', s))
        T['none']+=len(re.findall(r'none known', s))
        T['partC']+=len(re.findall(r'reading sheets, part C', s))
    nums=re.findall(r'\d+(?:[.,]\d+)?', re.sub(r'(F·|K|n° |no\. |volet |Part |fiche |sheet |trap |piège |partie |part |§|answer |réponse |topic |sujet |Topic |G|JB)\d+','',s))
    return T, sorted(x.replace(',','.') for x in nums)
for tr in ('volets8_9','volet10'):
    fr=blocks(f'applique_{tr}_FR.md'); en=blocks(f'applique_{tr}_EN.md')
    print(tr, len(fr), len(en))
    for (nf,bf),(ne,be) in zip(fr,en):
        tf,numf=toks(bf,'FR'); te,nume=toks(be,'EN')
        # remove noise keys
        diff={k:(tf.get(k,0),te.get(k,0)) for k in set(tf)|set(te) if tf.get(k,0)!=te.get(k,0)}
        if diff or numf!=nume:
            print('  FR',nf,'EN',ne,'DIFF',diff, '' if numf==nume else ('NUMS',numf,nume))
