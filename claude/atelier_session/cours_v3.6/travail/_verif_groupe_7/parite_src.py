import json,re
W='/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
def norm_fr(s):
    s=s.replace('fiches, partie','reading sheets, part').replace('fiche','reading sheet').replace('cours, volet','course, Part').replace('programme, parties','programme, parts').replace('programme, partie','programme, part').replace('passation','handover').replace('explication du 2 octobre','explanation of 2 October').replace('README du dépôt','repository README').replace('contre-lecture des fiches','counter-reading of the sheets').replace('réponses','answers').replace('réponse','answer').replace('rapport d\'antériorité','prior-art report').replace(' et ',' and ').replace('piège','trap').replace('pièges','traps').replace('sujet','topic').replace('cas d\'application','worked case').replace('parties','parts').replace('partie','part')
    return s
def cites(t):
    out=[]
    for m in re.finditer(r'\(([^()]*)\)',t):
        for p in m.group(1).split(';'):
            p=p.strip().replace('source : ','').replace('source: ','')
            if re.match(r'(cours|course|fiche|reading|programme|passation|handover|explication|explanation|README|repository|rapport|prior|contre|counter)',p):
                out.append(p)
    return out
def nums(t):
    t=t.replace(',','.')
    return sorted(re.findall(r'\d+(?:\.\d+)?',re.sub(r'(F·\d+|K\d+|JB\d+|G1|M\d+|A\d+|B\d+|§\d+(?:\.\d+)?|réponse \d+|answer \d+|réponses \d+ et|answers \d+ and|piège \d|trap \d|pièges \d et \d|traps \d and \d|partie \d|part \d|parties \d et \d|parts \d and \d|volet \d+|Part \d+|fiche \d+|sheet \d+|sujet \d+|topic \d+|item \d+|rapport d.antériorité \d|report \d|v3\.6|\d+ octobre|\d+ October|n°\d+)','',t)))
for tr in ['volet11_1_a_20','volet11_21_a_52','volet11_53_et_fin']:
    d=json.load(open(f'{W}/travail/insertions_{tr}.json',encoding='utf8'))
    fr=[x for x in d['insertions'] if x['fichier']=='FR']; en=[x for x in d['insertions'] if x['fichier']=='EN']
    for k,(a,b) in enumerate(zip(fr,en)):
        ca=[norm_fr(c) for c in cites(a['texte'])]; cb=cites(b['texte'])
        na=nums(a['texte']); nb=nums(b['texte'])
        if sorted(ca)!=sorted(cb) or na!=nb:
            print(tr,'paire',k+1,'FR n°',2*k+1)
            if sorted(ca)!=sorted(cb):
                print('   FR:',sorted(ca)); print('   EN:',sorted(cb))
            if na!=nb: print('   nombres FR',na,'EN',nb)
