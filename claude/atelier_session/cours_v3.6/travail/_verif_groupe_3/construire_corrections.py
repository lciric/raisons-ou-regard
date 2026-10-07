#!/usr/bin/env python3
"""Construit travail/corrections_groupe_3.json à partir des lignes exactes de la v3.6, et vérifie :
- chaque « ancien » est présent une seule fois dans la v3.6 actuelle ;
- il l'est encore après application simulée des corrections des groupes 1 et 2 ;
- aucune ligne de « ancien » n'est une ligne de la v3.5 (on ne touche qu'au texte ajouté) ;
- le JSON écrit est valide."""
import json, os, sys

W = '/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
V36 = {'FR': f'{W}/livrable/COURS_Alignment_v3.6_FR_2026-10-02.md', 'EN': f'{W}/livrable/COURS_Alignment_v3.6_EN_2026-10-02.md'}
V35 = {'FR': f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md', 'EN': f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md'}
txt = {k: open(v, encoding='utf8').read() for k, v in V36.items()}
lignes = {k: t.split('\n') for k, t in txt.items()}
v35 = {k: set(open(v, encoding='utf8').read().split('\n')) for k, v in V35.items()}


def ligne(fi, cle, suivantes=0):
    """La ligne unique de la v3.6 qui contient `cle`, plus `suivantes` lignes après elle."""
    idx = [i for i, l in enumerate(lignes[fi]) if cle in l]
    assert len(idx) == 1, (fi, cle, len(idx))
    i = idx[0]
    return '\n'.join(lignes[fi][i:i + 1 + suivantes])


def remplace(s, a, b):
    assert s.count(a) == 1, (a, s[:200])
    return s.replace(a, b)


C = []  # (fichier, ancien, nouveau, etiquette)

# --- C1 · volet 2, §E, encadré « Débat et supervision évolutive », limite 4
a = ligne('FR', "Le juge est souvent un modèle : les limites des juges LLM")
n = ("> - **Limite :** Le juge peut être un modèle, avec ses erreurs systématiques : un juge LLM plus faible que les agents jugés "
     "suit le consultant ouvert qu'il ait raison ou tort, et son biais de position est plus fort en débat. "
     "*(source : cours, volet 10, Kenton et al. ; fiches, partie B, piège 6)*")
C.append(('FR', a, n, 'C1'))
a = ligne('EN', "The judge is often a model: the limits of LLM judges apply.")
n = ("> - **Limit:** The judge can be a model, with systematic errors of its own: an LLM judge weaker than the agents it judges "
     "follows the open consultant whether right or wrong, and its position bias is stronger in debate. "
     "*(source: course, Part 10, Kenton et al.; reading sheets, part B, trap 6)*")
C.append(('EN', a, n, 'C1'))

# --- C2 · volet 2, §E, encadré « Élicitation non supervisée par cohérence », limite 3 et sa parade
a = ligne('FR', "L'échec peut rester silencieux là où l'évaluation en distribution est impossible.", 1)
n = remplace(a, ">   **Parade :** aucune connue ; on le dit.",
             ">   **Parade :** En partie : rendre le domaine vérifiable par un faux fait implanté, comme ci-dessus ; sur les vraies "
             "questions qu'aucun humain ne peut vérifier, aucune connue ; on le dit. *(source : cours, volet 2, §E, K52)*")
C.append(('FR', a, n, 'C2'))
a = ligne('EN', "Failure can stay silent where in-distribution evaluation is impossible.", 1)
n = remplace(a, ">   **Workaround:** none known; say so.",
             ">   **Workaround:** In part: make the domain checkable with an implanted false fact, as above; on the real questions "
             "no human can check, none known; say so. *(source: course, Part 2, §E, K52)*")
C.append(('EN', a, n, 'C2'))

# --- C3 · même encadré, limite 4 : le piège de K52 réintroduit (« my gate » au lieu de « my probe »)
a = ligne('FR', "Le filtre de l'implant et la méthode peuvent lire la même feature saillante.")
n = remplace(a, "Le filtre de l'implant et la méthode", "La sonde du filtre et la méthode")
C.append(('FR', a, n, 'C3'))
a = ligne('EN', "The implant filter and the method may read the same salient feature.")
n = remplace(a, "The implant filter and the method", "The filter's probe and the method")
C.append(('EN', a, n, 'C3'))

# --- C4 · même encadré, parade de la limite 2 : un pari dit comme un fait, un espoir dit comme une parade établie
a = ligne('FR', "et dire que sans lui elle ne rend que la cohérence.")
n = remplace(a, "par l'entraînement du facile au difficile, et dire que sans lui elle ne rend que la cohérence.",
             "par l'entraînement du facile au difficile — un espoir que le stress-test a mis à l'épreuve, pas une garantie ; "
             "sans lui, elle ne récompense que la cohérence.")
C.append(('FR', a, n, 'C4'))
a = ligne('EN', "and say that without it the method returns only consistency.")
n = remplace(a, "through easy-to-hard training, and say that without it the method returns only consistency.",
             "through easy-to-hard training — a hope the stress-test put to the test, not a guarantee; "
             "without it, the method rewards only consistency.")
C.append(('EN', a, n, 'C4'))

# --- C5 · volet 2, §G, encadré « Moniteurs du contrôle », parade de la limite 3 : une récupération partielle
a = ligne('FR', "**Parade :** Des moniteurs à état ; pour l'agrégation de preuves internes")
n = remplace(a, "Des moniteurs à état ;", "Des moniteurs à état, qui n'en récupèrent qu'une partie ;")
C.append(('FR', a, n, 'C5'))
a = ligne('EN', "**Workaround:** Stateful monitors; for aggregating internal evidence")
n = remplace(a, "Stateful monitors;", "Stateful monitors, which recover only part of them;")
C.append(('EN', a, n, 'C5'))

# --- C6 · volet 2, §H, encadré « Red-teaming », parade de la limite 1 : le nul d'une red team sans cas connu
a = ligne('FR', "Sans budget fixé, « rien trouvé » dit seulement qu'on n'a pas assez cherché.", 1)
n = remplace(a, ">   **Parade :** Un budget fixé d'avance, rapporté avec le résultat. *(source : cours, volet M, M7)*",
             ">   **Parade :** Un budget fixé d'avance, rapporté avec le résultat ; et un « rien trouvé » ne compte que si la même "
             "red team trouve d'abord là où l'on sait qu'il y a à trouver. *(source : cours, volet M, M7 et M5)*")
C.append(('FR', a, n, 'C6'))
a = ligne('EN', 'Without a fixed budget, "nothing found" only says you did not search enough.', 1)
n = remplace(a, ">   **Workaround:** A budget fixed in advance, reported with the result. *(source: course, Part M, M7)*",
             '>   **Workaround:** A budget fixed in advance, reported with the result; and a "nothing found" counts only if the same '
             "red team first finds something where it is known there is something to find. *(source: course, Part M, M7 and M5)*")
C.append(('EN', a, n, 'C6'))

# --- C7 · volet 2, §H, cas G1, avertissement sur « sans en trouver d'universel » : la borne exige son cas connu
a = ligne('FR', "La formule « sans en trouver d'universel » rapporte le nul d'une chasse")
n = remplace(a, "une borne à son budget, pas une absence *(source : cours, volet M, M5 et M7)*",
             "une borne à son budget, pas une absence, qui ne vaut que si la même chasse trouve là où l'on sait qu'il y a à trouver "
             "*(source : cours, volet M, M5 et M7)*")
C.append(('FR', a, n, 'C7'))
a = ligne('EN', 'The phrase "without finding a universal one" reports the null of a hunt')
n = remplace(a, "a bound at its budget, not an absence *(source: course, Part M, M5 and M7)*",
             "a bound at its budget, not an absence, which holds only if the same hunt finds something where it is known there is "
             "something to find *(source: course, Part M, M5 and M7)*")
C.append(('EN', a, n, 'C7'))

# --- C8 · volet 2, §H, encadré « Classifieurs de sûreté », limite 5 : un risque dit comme un fait
a = ligne('FR', "Placé dans l'entraînement, un classifieur incite le modèle à l'éviter.")
n = remplace(a, "un classifieur incite le modèle", "un classifieur peut inciter le modèle")
C.append(('FR', a, n, 'C8'))
a = ligne('EN', "Placed in training, a classifier gives the model an incentive to evade it.")
n = remplace(a, "a classifier gives the model", "a classifier can give the model")
C.append(('EN', a, n, 'C8'))

# --- C9 · volet 2, §I, avertissement après Constitutional AI : une menace dite comme un fait
a = ligne('FR', "Le « feedback de l'IA » fait d'un modèle le juge de l'entraînement")
n = remplace(a, "et un juge d'entraînement se fait exploiter", "et un juge d'entraînement peut se faire exploiter")
C.append(('FR', a, n, 'C9'))
a = ligne('EN', 'The "feedback from AI" makes a model the judge of training')
n = remplace(a, "and a training judge gets exploited", "and a training judge can get exploited")
C.append(('EN', a, n, 'C9'))

# --- C10 · volet 3, partie III, « Honnêteté et cognition » : l'introspection est bien un auto-rapport
a = ligne('FR', "Ces lectures ne sont pas un auto-rapport du modèle")
n = remplace(a, "Ces lectures ne sont pas un auto-rapport du modèle", "Ces lectures ne sont pas toutes un auto-rapport du modèle")
C.append(('FR', a, n, 'C10'))
a = ligne('EN', "These readings are not a self-report of the model")
n = remplace(a, "These readings are not a self-report of the model", "Not all of these readings are a self-report of the model")
C.append(('EN', a, n, 'C10'))

# --- C11 · volet 3, partie III, « Entraîner le prior » : fiche 3 ne porte pas la formule, partie 1 ne dit pas « ne mesure »,
#           et la parade du cas K63 existe
a = ligne('FR', "Ce taux est lu sur des pots de miel")
n = ("> ⚠ *(v3.6)* Ce taux est lu sur des pots de miel : un modèle peut y remarquer le test et s'y conduire mieux — sur un pot de "
     "miel synthétique, le modèle final de Sonnet 4.5 verbalise sa conscience dans plus de 80 % des cas (fiche 2 ; cours, volet 2, "
     "§B, K63) —, ceux qui sont tenus à part ne sont peut-être pas représentatifs (fiche 12), et le travail n'a aucun contrôle de "
     "la conscience d'évaluation (programme, partie 1). Parade : des métriques d'audit tenues à part, jamais entraînées, comme le "
     "fait ce travail (fiche 12) ; l'écart mesuré avec et sans inhibition de la conscience d'évaluation, à dégradation appariée et "
     "contre des vecteurs de contrôle (fiches, partie C) ; et, en partie, deux versions d'un environnement, tirées au hasard, qui "
     "ne diffèrent que par des indices de réalisme notés par un discriminateur, avec un organisme dressé à se cacher comme cas "
     "connu (cours, volet 2, §B, K63).")
C.append(('FR', a, n, 'C11'))
a = ligne('EN', "This rate is read on honeypots")
n = ("> ⚠ *(v3.6)* This rate is read on honeypots: a model can notice the test there and behave better — on a synthetic honeypot, "
     "the final Sonnet 4.5 model verbalizes its awareness in more than 80% of cases (reading sheet 2; course, Part 2, §B, K63) —, "
     "the held-out ones may not be representative (reading sheet 12), and the work has no control for evaluation awareness "
     "(programme, part 1). Workaround: held-out audit metrics, never trained on, as this work does (reading sheet 12); the gap "
     "measured with and without inhibition of evaluation awareness, at matched degradation and against control vectors (reading "
     "sheets, part C); and, in part, two versions of an environment, randomly assigned, differing only in realism cues scored by "
     "a discriminator, with an organism trained to hide as the known case (course, Part 2, §B, K63).")
C.append(('EN', a, n, 'C11'))

# --- C12 · volet 3, partie IV : une note d'étude, pas une ligne à dire ; l'explication du README au conditionnel
a = ligne('FR', "Ce que cette phrase déroule a ses limites")
n = remplace(a, "Ce que cette phrase déroule a ses limites, à dire avec elle :",
             "Ce que cette phrase déroule a ses limites, à connaître avant de la dire :")
n = remplace(n, "et la baisse obtenue au rang trois ne s'est pas reproduite sur des générations fraîches jugées en entier, "
                "l'ablation adoucissant tout verdict négatif, lu à travers une fenêtre tronquée (README du dépôt).",
             "et la baisse obtenue au rang trois ne s'est pas reproduite sur des générations fraîches jugées en entier : le README "
             "l'attribue à un adoucissement de tout verdict négatif, lu à travers une fenêtre tronquée, explication que le cours "
             "fait dire au conditionnel (README du dépôt ; cours, volet M, M8).")
C.append(('FR', a, n, 'C12'))
a = ligne('EN', "What this sentence unfolds has its limits")
n = remplace(a, "What this sentence unfolds has its limits, to be stated with it:",
             "What this sentence unfolds has its limits, to know before saying it:")
n = remplace(n, "and the drop obtained at rank three did not reproduce on fresh generations judged in full, the ablation "
                "softening every negative verdict, read through a truncated window (repository README).",
             "and the drop obtained at rank three did not reproduce on fresh generations judged in full: the README attributes it "
             "to a softening of every negative verdict, read through a truncated window, an explanation the course has you state "
             "in the conditional (repository README; course, Part M, M8).")
C.append(('EN', a, n, 'C12'))

# ---------------------------------------------------------------- vérifications
ok = True
for fi, anc, nou, lab in C:
    k = txt[fi].count(anc)
    if k != 1:
        print('ÉCHEC unicité', lab, fi, k); ok = False
    for l in anc.split('\n'):
        if l in v35[fi] and l.strip():
            print('ÉCHEC : ligne de la v3.5 touchée', lab, fi, l[:100]); ok = False
    if anc == nou:
        print('ÉCHEC : rien ne change', lab, fi); ok = False
    if '(v3.6' not in nou and '**Limite' not in nou and '**Limit' not in nou and '**Parade' not in nou and '**Workaround' not in nou:
        print('ATTENTION format', lab, fi)

# Application simulée : groupes 1 et 2, puis le nôtre
sim = dict(txt)
for g in ['corrections_groupe_1.json', 'corrections_groupe_2.json']:
    p = f'{W}/travail/{g}'
    if os.path.exists(p):
        for c in json.load(open(p, encoding='utf8'))['corrections']:
            if sim[c['fichier']].count(c['ancien']) == 1:
                sim[c['fichier']] = sim[c['fichier']].replace(c['ancien'], c['nouveau'])
for fi, anc, nou, lab in C:
    k = sim[fi].count(anc)
    if k != 1:
        print('ÉCHEC après groupes 1-2', lab, fi, k); ok = False
    else:
        sim[fi] = sim[fi].replace(anc, nou)

out = {'corrections': [{'fichier': fi, 'ancien': anc, 'nouveau': nou} for fi, anc, nou, lab in C]}
p = f'{W}/travail/corrections_groupe_3.json'
json.dump(out, open(p, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
json.load(open(p, encoding='utf8'))
print('corrections :', len(C), '| vérifications :', 'OK' if ok else 'ÉCHEC')
# Longueur des citations entre guillemets dans les « nouveau »
import re
for fi, anc, nou, lab in C:
    for q in re.findall(r'«\s*([^»]+?)\s*»|"([^"]+)"', nou):
        s = q[0] or q[1]
        if len(s.split()) >= 15:
            print('CITATION LONGUE', lab, fi, s)
