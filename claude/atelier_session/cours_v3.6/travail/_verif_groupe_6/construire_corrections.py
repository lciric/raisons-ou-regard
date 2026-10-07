#!/usr/bin/env python3
"""Construit travail/corrections_groupe_6.json à partir des lignes exactes de la v3.6, puis vérifie :
  1. chaque « ancien » est fait de lignes entières d'insertion v3.6, présent une seule fois dans la v3.6 ;
  2. aucune ligne d'« ancien » ne figure dans la v3.5 ;
  3. chaque « ancien » reste unique après l'application simulée des corrections des groupes 1 à 5 ;
  4. aucune citation entre guillemets des nouveaux textes n'atteint quinze mots ;
  5. après application simulée de tout, chaque ligne de la v3.5 se retrouve, dans l'ordre (intégrité) ;
  6. le JSON écrit est valide et se relit.
Le livrable n'est pas modifié."""
import glob, json, os, re, sys

W = '/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
SRC = {'FR': f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md', 'EN': f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md'}
OUT = {'FR': f'{W}/livrable/COURS_Alignment_v3.6_FR_2026-10-02.md', 'EN': f'{W}/livrable/COURS_Alignment_v3.6_EN_2026-10-02.md'}
JSON_OUT = f'{W}/travail/corrections_groupe_6.json'

v36 = {k: open(v, encoding='utf8').read() for k, v in OUT.items()}
v35 = {k: open(v, encoding='utf8').read() for k, v in SRC.items()}
v35_lines = {k: set(l for l in t.split('\n') if l.strip()) for k, t in v35.items()}
v36_lines = {k: t.split('\n') for k, t in v36.items()}


def line_with(fi, key):
    hits = [l for l in v36_lines[fi] if key in l]
    assert len(hits) == 1, (fi, key, len(hits))
    return hits[0]


def sub_in(line, old, new):
    assert line.count(old) == 1, (old, line[:120])
    return line.replace(old, new)


corr = []  # (étiquette, fichier, ancien, nouveau)

# --- C1 · volet 9, §3, SAD (FR n°3 / EN n°25) : source manquante de « laquelle fonde quel chiffre »
l = line_with('FR', 'Le quasi-hasard du SAD est un auto-rapport')
corr.append(('C1', 'FR', l, sub_in(l, '(cours, volet 5, sujet 4 ; explication du 2 octobre, §3).',
                                   '(cours, volet 5, sujet 4 ; cours, volet M, M4 ; explication du 2 octobre, §3).')))
l = line_with('EN', "SAD's near-chance result is a self-report")
corr.append(('C1', 'EN', l, sub_in(l, '(course, Part 5, topic 4; explanation of 2 October, §3).',
                                   '(course, Part 5, topic 4; course, Part M, M4; explanation of 2 October, §3).')))

# --- C2 · volet 9, §4, persona (FR n°6 / EN n°28) : « pas causal » contredit F·31 ; extraction supervisée : parade connue
l = line_with('FR', '« Le persona comme direction » est un résultat prédictif, pas causal')
new = ("> ⚠ *(v3.6)* Derrière « le persona comme direction », le résultat le plus fort est prédictif, pas causal : le lien entre "
       "le déplacement le long du vecteur et le trait est corrélationnel, le trait doit être nommé d'avance, les directions sont "
       "grossières, et l'évaluation est légère, un juge GPT-4.1-mini sur un seul tour (fiche 8) ; le vecteur agit, lui : le soustraire "
       "après coup réduit le trait, mais dégrade MMLU (cours, volet 7, F·31), et un tel effet ne dit le concept qu'à dégradation "
       "appariée (cours, volet M, M4). Parade : pour la causalité, piloter contre des directions aléatoires de même norme — le nul "
       "de spécificité —, puis contre des témoins à dégradation appariée — le dommage —, et rapporter la part du vecteur contre "
       "celle de l'état complet aux mêmes sites, ta partition (cours, volet M, M4 ; passation, §5.2 ; cours, volet 6, §2 ; cours, "
       "volet 7, F·31) ; pour l'extraction supervisée, le diffing par crosscoder, qui cherche sans hypothèse (programme, partie 8).")
corr.append(('C2', 'FR', l, new))
l = line_with('EN', '"The persona as a direction" is a predictive result, not a causal one')
new = ('> ⚠ *(v3.6)* Behind "the persona as a direction", the strongest result is predictive, not causal: the link between the '
       'shift along the vector and the trait is correlational, the trait must be named in advance, the directions are coarse, and '
       'the evaluation is light, a GPT-4.1-mini judge on a single turn (reading sheet 8); the vector does act: subtracting it after '
       'the fact reduces the trait, but degrades MMLU (course, Part 7, F·31), and such an effect shows the concept only at matched '
       'degradation (course, Part M, M4). Workaround: for causality, steer against matched-norm random directions — the specificity '
       "null —, then against controls at matched degradation — the damage —, and report the vector's share against that of the full "
       'state at the same sites, your partition (course, Part M, M4; handover, §5.2; course, Part 6, §2; course, Part 7, F·31); for '
       'supervised extraction, crosscoder diffing, which searches without a hypothesis (programme, part 8).')
corr.append(('C2', 'EN', l, new))

# --- C3 · volet 9, §6b, coup probes et circuit breakers (FR n°12 / EN n°34) : la source parle des négatifs
l = line_with('FR', 'Ces « signs of life » ne mettent pas encore')
corr.append(('C3', 'FR', l, sub_in(l, "construire ses exemples à partir des générations réelles du modèle surveillé,",
                                   "construire ses exemples négatifs à partir des générations réelles du modèle surveillé, pas seulement de données synthétiques,")))
l = line_with('EN', 'These "signs of life" do not yet put')
corr.append(('C3', 'EN', l, sub_in(l, 'build its examples from the real generations of the monitored model,',
                                   'build its negative examples from the real generations of the monitored model, not only from synthetic data,')))

# --- C4 · volet 9, §9b, AI Organizations (FR n°21 / EN n°43) : fiche 3 mal glosée, « aucune parade » contre K63
l = line_with('FR', 'AI Organizations mesure ce mode dans deux organisations simulées')
new = ("> ⚠ *(v3.6)* AI Organizations mesure ce mode dans deux organisations simulées, sur Opus 4.1, et ses auteurs écrivent que les "
       "tâches sont simulées et que le mécanisme de l'écart n'est que partiellement expliqué (cours, volet 7, F·39) ; or un modèle "
       "peut remarquer le test et s'y conduire autrement, et dans une simulation, « c'est faux » est vrai (cours, volet 2, §B, K63 ; "
       "fiche 3). Parade, en partie : deux versions d'un environnement, tirées au hasard, qui ne diffèrent que par des indices de "
       "réalisme notés par un discriminateur, avec un organisme dressé à se cacher comme cas connu (cours, volet 2, §B, K63) ; pour "
       "le confondeur de la simulation lui-même, aucune parade connue ; on le dit (fiche 3).")
corr.append(('C4', 'FR', l, new))
l = line_with('EN', 'AI Organizations measures this mode in two simulated organizations')
new = ('> ⚠ *(v3.6)* AI Organizations measures this mode in two simulated organizations, on Opus 4.1, and its authors write that '
       'the tasks are simulated and the mechanism of the gap is only partially explained (course, Part 7, F·39); and a model may '
       'notice the test and behave differently there, and in a simulation, "this is fake" is true (course, Part 2, §B, K63; reading '
       'sheet 3). Workaround, in part: two versions of an environment, randomly assigned, differing only in realism cues scored by a '
       'discriminator, with an organism trained to hide as the known case (course, Part 2, §B, K63); for the simulation confound '
       'itself, none known; say so (reading sheet 3).')
corr.append(('C4', 'EN', l, new))

# --- C5 · volet 10, n° 07, SAD (FR n°7 / EN n°8) : portée du score ; parade tirée d'une règle sur l'inhibition
l = line_with('FR', 'Ce score mesure ce que le modèle répond quand on lui demande où il se trouve')
new = ("> ⚠ *(v3.6)* Sur stages-oversight, le score mesure ce que le modèle répond quand on lui demande où il se trouve : un "
       "auto-rapport, qui n'est pas une croyance (fiche 3 ; fiches, partie B, piège 2), et une conscience verbalisée, qui rate la "
       "non verbalisée (cours, volet 7, F·25) ; qu'il y dépasse à peine le hasard n'établit donc pas que le modèle ne distingue pas "
       "évaluation et déploiement : c'est le nul d'un instrument (fiches, partie B, piège 3). Parade : trianguler — une sonde "
       "interne, le rapport verbal, et le comportement entre une version réaliste et une version manifeste de la situation (cours, "
       "volet 5, sujet 4) —, la sonde validée d'abord sur un organisme conditionné à l'évaluation comme cas connu (programme, "
       "parties 4 et 8).")
corr.append(('C5', 'FR', l, new))
l = line_with('EN', 'This score measures what the model answers when asked where it is')
new = ('> ⚠ *(v3.6)* On stages-oversight, the score measures what the model answers when asked where it is: a self-report, which '
       'is not a belief (reading sheet 3; reading sheets, part B, trap 2), and verbalized awareness, which misses the unverbalized '
       'kind (course, Part 7, F·25); that it is barely above chance there therefore does not establish that the model cannot tell '
       "evaluation from deployment: it is an instrument's null (reading sheets, part B, trap 3). Workaround: triangulate — an "
       'internal probe, the verbal report, and behaviour between a realistic and an obvious version of the setting (course, Part 5, '
       'topic 4) —, with the probe first validated on an evaluation-conditioned organism as the known case (programme, parts 4 and 8).')
corr.append(('C5', 'EN', l, new))

# --- C6 · volet 10, encadré « Patching », parade 3 : le README ne dit pas la parade
l = line_with('FR', "**Parade :** Choisir les sites d'intervention par leur effet causal mesuré")
corr.append(('C6', 'FR', l, ">   **Parade :** Choisir les sites d'intervention par leur effet causal mesuré, à l'ablation et au patch, le patch de "
                              "l'état complet servant de plafond, et non par l'alignement sur la direction lue. *(source : README du dépôt ; "
                              "programme, partie 8)*"))
l = line_with('EN', '**Workaround:** Choose intervention sites by their measured causal effect')
corr.append(('C6', 'EN', l, '>   **Workaround:** Choose intervention sites by their measured causal effect, under ablation and patching, with the '
                              'full-state patch as the ceiling, not by alignment with the read direction. *(source: repository README; '
                              'programme, part 8)*'))

# --- C7 · volet 10, encadré « Patching », limite 4 : une parade est connue (refaire plus grand, puissance fixée d'avance)
lim = line_with('FR', 'Petits jeux de prompts : dans ton dépôt')
i = v36_lines['FR'].index(lim); par = v36_lines['FR'][i + 1]
assert par == '>   **Parade :** aucune connue ; on le dit.', par
corr.append(('C7', 'FR', lim + '\n' + par,
             lim + '\n' + ">   **Parade :** Refaire le patch sur un jeu plus grand, de taille fixée d'avance par une simulation de puissance, "
                          "et dire la puissance avec le résultat. *(source : programme, partie 7 ; cours, volet M, M5)*"))
lim = line_with('EN', 'Small prompt sets: in your repository')
i = v36_lines['EN'].index(lim); par = v36_lines['EN'][i + 1]
assert par == '>   **Workaround:** none known; say so.', par
corr.append(('C7', 'EN', lim + '\n' + par,
             lim + '\n' + '>   **Workaround:** Redo the patching on a larger set, its size fixed in advance by a power simulation, and state '
                          'the power with the result. *(source: programme, part 7; course, Part M, M5)*'))

# --- C8 · volet 10, encadré « Patching », limite 6 : durcissement (« faussent ») et traduction de « placeholder »
l = line_with('FR', 'Le choix du prompt cible et la contamination par le gabarit faussent la lecture')
corr.append(('C8', 'FR', l, "> - **Limite :** Le choix du prompt cible et la contamination par le jeton de remplacement (« placeholder "
                              "contamination ») peuvent fausser la lecture ; les auteurs les laissent à faire. *(source : cours, volet 10, "
                              "Patchscopes)*"))
l = line_with('EN', 'The choice of target prompt and placeholder contamination distort the reading')
corr.append(('C8', 'EN', l, '> - **Limit:** The choice of target prompt and placeholder contamination can distort the reading; the authors '
                              'leave both as future work. *(source: course, Part 10, Patchscopes)*'))

# --- C9 · volet 10, n° 40, Prover-Verifier Games (FR n°57 / EN n°58) : « pas seulement » dans la source
l = line_with('FR', "Contre ce risque d'un moniteur qui apprend le style de l'attaquant")
corr.append(('C9', 'FR', l, sub_in(l, "et les négatifs se tirent des générations réelles du modèle, pas d'exemples fabriqués",
                                   "et les négatifs se tirent aussi des générations réelles du modèle, pas seulement d'exemples fabriqués")))
l = line_with('EN', 'Against this risk of a monitor that learns the attacker')
corr.append(('C9', 'EN', l, sub_in(l, "and negatives are drawn from the model's real generations, not from fabricated examples",
                                   "and negatives are also drawn from the model's real generations, not only from fabricated examples")))

# --- C10 · volet 10, n° 54, CAA (FR n°67 / EN n°68) : le volet M, M4, donne des parades contre l'artefact de polarité
l = line_with('FR', 'Ces effets se comparent aux prompts système et au fine-tuning')
corr.append(('C10', 'FR', l, sub_in(l, "; contre l'artefact de polarité, aucune parade connue ; on le dit.",
                                    "; contre l'artefact de polarité, des paires qui ne diffèrent que par le trait, vérifiées par un classifieur "
                                    "qui ne lit que la surface, une direction de polarité construite comme concept rival, au même endroit et "
                                    "à dégradation appariée, et le témoin sans pression (cours, volet M, M4).")))
l = line_with('EN', 'These effects are compared with system prompts and fine-tuning')
corr.append(('C10', 'EN', l, sub_in(l, '; against the polarity artefact, none known; say so.',
                                    '; against the polarity artefact, pairs that differ only in the trait, checked by a classifier that reads '
                                    'only the surface, a polarity direction built as a rival concept, at the same place and at matched '
                                    'degradation, and the no-pressure control arm (course, Part M, M4).')))

# ---------- Vérifications ----------
ok = True
for tag, fi, anc, nou in corr:
    if v36[fi].count(anc) != 1:
        print('ÉCHEC unicité v3.6', tag, fi); ok = False
    for ln in anc.split('\n'):
        if ln.strip() and ln in v35_lines[fi]:
            print('ÉCHEC : une ligne d\'« ancien » est dans la v3.5', tag, fi, ln[:80]); ok = False
    if anc == nou:
        print('ÉCHEC : nouveau identique', tag, fi); ok = False
    for q in re.findall(r'«\s*([^»]+?)\s*»|"([^"]+)"', nou):
        qq = q[0] or q[1]
        if len(qq.split()) >= 15:
            print('ÉCHEC citation >= 15 mots', tag, fi, qq[:80]); ok = False
    if '(v3.6)' not in nou and fi in ('FR', 'EN') and nou.startswith('> ⚠'):
        print('ÉCHEC mention v3.6', tag, fi); ok = False

# simulation : groupes 1 à 5 puis groupe 6, dans l'ordre de appliquer.py
sim = dict(v36)
for f in sorted(glob.glob(f'{W}/travail/corrections_groupe_*.json')):
    if f.endswith('corrections_groupe_6.json'):
        continue
    d = json.load(open(f, encoding='utf8'))
    for n, c in enumerate(d['corrections'], 1):
        k = sim[c['fichier']].count(c['ancien'])
        if k != 1:
            print('note : correction antérieure non applicable', os.path.basename(f), n, k)
            continue
        sim[c['fichier']] = sim[c['fichier']].replace(c['ancien'], c['nouveau'])
for tag, fi, anc, nou in corr:
    k = sim[fi].count(anc)
    if k != 1:
        print('ÉCHEC après groupes 1-5', tag, fi, k); ok = False; continue
    sim[fi] = sim[fi].replace(anc, nou)

# intégrité : chaque ligne v3.5 retrouvée dans l'ordre
for fi in ('FR', 'EN'):
    a = v35[fi].split('\n'); b = sim[fi].split('\n'); j = 0; miss = 0
    for l in a:
        while j < len(b) and b[j] != l:
            j += 1
        if j == len(b):
            miss += 1; j = 0
        else:
            j += 1
    print(f'intégrité {fi} après simulation : lignes v3.5 introuvables = {miss}')
    ok = ok and miss == 0

data = {'corrections': [{'fichier': fi, 'ancien': anc, 'nouveau': nou} for _, fi, anc, nou in corr]}
json.dump(data, open(JSON_OUT, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
back = json.load(open(JSON_OUT, encoding='utf8'))
assert back == data
print('corrections écrites :', len(back['corrections']), '| vérifications :', 'OK' if ok else 'ÉCHEC')
for tag, fi, anc, nou in corr:
    print(tag, fi, 'ligne v3.6', v36[fi][:v36[fi].find(anc)].count('\n') + 1)
