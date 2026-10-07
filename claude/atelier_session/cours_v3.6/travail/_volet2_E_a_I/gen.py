import json, re
W = '/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
SRC = {'FR': f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md', 'EN': f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md'}
TR = {'FR': (667, 884), 'EN': (756, 1006)}
L = {k: open(v, encoding='utf8').read().split('\n') for k, v in SRC.items()}

def line(fi, n):
    return L[fi][n - 1]

def check(fi, ancre):
    a, b = TR[fi]
    idx = [i + 1 for i in range(a - 1, b) if L[fi][i].strip() == ancre.strip()]
    return idx

ref = json.load(open(f'{W}/travail/referentiel_instruments.json'))
pret = ref['insertions_pretes']['volet2_E_a_I']
enc = {(e['instrument'], e['fichier']): e for e in pret}

# check JSON encadrés are identical to the md referential blocks
md = open(f'{W}/travail/referentiel_instruments.md', encoding='utf8').read()
for e in pret:
    assert e['texte'].strip() in md, ('encadré absent du md', e['instrument'], e['fichier'])

R = {}
R['renvoi_K52'] = {
 'FR': "> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*",
 'EN': "> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after \"In practice — Auditing Hidden Objectives\"); activation probes → Part 2, §C (after \"In practice — The Geometry of Truth\") *(v3.6)*"}
R['renvoi_JB8'] = {
 'FR': "> ⚠ **Limites et parades** : cas connu → volet M, M5 (fin de section) ; jeu tenu à part → volet M, M4 (après « Le jeu tenu à part ») *(v3.6)*",
 'EN': "> ⚠ **Limits and workarounds**: known case → Part M, M5 (end of section); held-out set → Part M, M4 (after \"The held-out set\") *(v3.6)*"}
R['ponct_K76_shade'] = {
 'FR': "> ⚠ *(v3.6)* Ce quart est un chiffre de red team : il dépend de la force du saboteur supposé — sur cinq environnements SHADE-Arena, un échafaudage d'attaque optimisé composante par composante a fait tomber le score de sûreté de 0,87 à 0,41 *(source : cours, volet 7, F·24)*. Parade : dire quelle red team le chiffre suppose, au moins une red team optimisée composante par composante, avec l'ablation de chaque composante *(source : cours, volet 7, F·24)*.",
 'EN': "> ⚠ *(v3.6)* That quarter is a red-team number: it depends on the strength of the assumed saboteur — on five SHADE-Arena environments, an attack scaffold optimized component by component brought the safety score down from 0.87 to 0.41 *(source: course, Part 7, F·24)*. Workaround: say which red team the number assumes, at least one optimized component by component, with each component ablated *(source: course, Part 7, F·24)*."}
R['renvoi_K76'] = {
 'FR': "> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*",
 'EN': "> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after \"In practice — The Geometry of Truth\"); red-teaming → Part 2, §H (after \"In practice — StrongREJECT\"); known case → Part M, M5 (end of section) *(v3.6)*"}
R['ponct_K76_atlas'] = {
 'FR': "> ⚠ *(v3.6)* Même validé par ce cas connu, un zéro borne la sonde gardée fixe, pas ce que portent les activations : selon un rapport, après un RL, des sondes neuves hors domaine se dégradent quand une sonde neuve dans le domaine reste quasi parfaite — le concept aurait quitté la direction générale *(source : rapport d'antériorité 3 du 2 octobre, The Obfuscation Atlas — rapport ; explication du 2 octobre, §3)*. Parade : extraire aussi une sonde neuve sur l'agent entraîné, avec un jeu d'indices disjoint, comme mesure séparée *(source : programme, parties 3 et 8 ; passation, §5.2 et §5.5)*.",
 'EN': "> ⚠ *(v3.6)* Even validated by this known case, a zero bounds the probe kept fixed, not what the activations carry: according to a report, after RL, fresh out-of-domain probes degrade while a fresh in-domain probe stays near perfect — the concept would have left the general direction *(source: prior-art report 3 of 2 October, The Obfuscation Atlas — report; explanation of 2 October, §3)*. Workaround: also extract a fresh probe on the trained agent, with a disjoint cue set, as a separate measure *(source: programme, parts 3 and 8; handover, §5.2 and §5.5)*."}
R['ponct_G1_chasse'] = {
 'FR': "> ⚠ *(v3.6)* La formule « sans en trouver d'universel » rapporte le nul d'une chasse : une borne à son budget, pas une absence *(source : cours, volet M, M5 et M7)*. Parade : un budget fixé d'avance, rapporté avec le résultat *(source : cours, volet M, M7)* ; et juger le filtre aussi par le préjudice différentiel, avec un filtre affaibli exprès comme cas connu, comme le fait l'expérience de ce cas *(source : cours, volet 2, §H, G1)*.",
 'EN': "> ⚠ *(v3.6)* The phrase \"without finding a universal one\" reports the null of a hunt: a bound at its budget, not an absence *(source: course, Part M, M5 and M7)*. Workaround: a budget fixed in advance, reported with the result *(source: course, Part M, M7)*; and judge the filter also by differential harm, with a deliberately weakened filter as the known case, as this case's experiment does *(source: course, Part 2, §H, G1)*."}
R['renvoi_G1'] = {
 'FR': "> ⚠ **Limites et parades** : cas connu → volet M, M5 (fin de section) *(v3.6)*",
 'EN': "> ⚠ **Limits and workarounds**: known case → Part M, M5 (end of section) *(v3.6)*"}
R['ponct_CAI'] = {
 'FR': "> ⚠ *(v3.6)* Le « feedback de l'IA » fait d'un modèle le juge de l'entraînement, et un juge d'entraînement se fait exploiter *(source : programme, partie 8)*. Parade : un juge d'entraînement distinct du juge scellé d'évaluation, des métriques d'audit tenues à part, et une surveillance de la longueur et des motifs de flatterie *(source : programme, partie 8)* ; voir l'encadré « Juges LLM », volet 6, §2.",
 'EN': "> ⚠ *(v3.6)* The \"feedback from AI\" makes a model the judge of training, and a training judge gets exploited *(source: programme, part 8)*. Workaround: a training judge distinct from the sealed evaluation judge, held-out audit metrics, and watching length and flattery patterns *(source: programme, part 8)*; see the box \"LLM judges\", Part 6, §2."}
R['renvoi_JB10'] = {
 'FR': "> ⚠ **Limites et parades** : cas connu → volet M, M5 (fin de section) ; jeu tenu à part → volet M, M4 (après « Le jeu tenu à part ») *(v3.6)*",
 'EN': "> ⚠ **Limits and workarounds**: known case → Part M, M5 (end of section); held-out set → Part M, M4 (after \"The held-out set\") *(v3.6)*"}

# plan: (kind, key, FR line, EN line)
plan = [
 ('enc', 'debat', 673, 763),
 ('mine', 'renvoi_K52', 692, 782),
 ('enc', 'elic', 709, 799),
 ('enc', 'w2s', 717, 808),
 ('mine', 'renvoi_JB8', 743, 834),
 ('enc', 'moni', 758, 850),
 ('mine', 'ponct_K76_shade', 767, 859),
 ('mine', 'renvoi_K76', 777, 869),
 ('mine', 'ponct_K76_atlas', 785, 877),
 ('enc', 'red', 803, 896),
 ('mine', 'ponct_G1_chasse', 810, 903),
 ('mine', 'renvoi_G1', 824, 917),
 ('enc', 'classif', 832, 925),
 ('mine', 'ponct_CAI', 838, 932),
 ('enc', 'unl', 840, 934),
 ('mine', 'renvoi_JB10', 868, 962),
]
out = []
ok = True
for kind, key, nfr, nen in plan:
    for fi, n in (('FR', nfr), ('EN', nen)):
        anc = line(fi, n)
        idx = check(fi, anc)
        if idx != [n]:
            print('ANCRE PB', key, fi, n, idx, anc[:80]); ok = False
        if kind == 'enc':
            e = enc[(key, fi)]
            if e['ancre'].strip() != anc.strip():
                print('ANCRE REF DIFFERENTE', key, fi, n); ok = False
            texte = e['texte']
        else:
            texte = R[key][fi]
        out.append({'fichier': fi, 'ancre': anc, 'texte': texte})
print('ancres OK' if ok else 'ancres KO', len(out))
json.dump({'tranche': 'volet2_E_a_I', 'insertions': out}, open(f'{W}/travail/insertions_volet2_E_a_I.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
