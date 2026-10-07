#!/usr/bin/env python3
"""Groupe 7 : construit corrections_groupe_7.json à partir des lignes exactes de la v3.6, puis vérifie.

Chaque correction = (fichier, tranche, n° d'insertion, [(sous-chaîne ancienne, sous-chaîne nouvelle), ...]).
« ancien » = la ligne entière de l'insertion (ou deux lignes pour l'encadré), telle qu'elle est dans la v3.6.
"""
import json, re, sys

W = '/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
SRC = {k: open(f'{W}/source/COURS_Alignment_v3.5_{k}_2026-09-27.md', encoding='utf8').read() for k in ('FR', 'EN')}
OUT = {k: open(f'{W}/livrable/COURS_Alignment_v3.6_{k}_2026-10-02.md', encoding='utf8').read() for k in ('FR', 'EN')}
INS = {}
for tr in ('volet11_1_a_20', 'volet11_21_a_52', 'volet11_53_et_fin'):
    INS[tr] = json.load(open(f'{W}/travail/insertions_{tr}.json', encoding='utf8'))['insertions']

C = []  # (fichier, tranche, n, remplacements, ligne_cible_optionnelle)

def add(fi, tr, n, reps, ligne=None):
    C.append((fi, tr, n, reps, ligne))

# ---------- tranche volet11_1_a_20 ----------
# P1 — réponse 3 : « rang trop bas » n'est pas la rivale d'un nul de rang un ; la rivale est l'instrument aveugle.
add('FR', 'volet11_1_a_20', 13, [(
    "un nul peut venir d'un rang trop bas si le concept est réparti — c'est ta propre prédiction (fiche 7",
    "un nul ne sépare pas « il faut plus d'une direction », ta propre prédiction pour un concept réparti, d'un instrument aveugle à cette dose (fiche 7")])
add('EN', 'volet11_1_a_20', 14, [(
    "a null can come from too low a rank if the concept is distributed — your own prediction (reading sheet 7",
    "a null does not separate \"more than one direction is needed\", your own prediction for a distributed concept, from an instrument blind at that dose (reading sheet 7")])
# P2 — réponse 6 : « de même norme » ; la dégradation de chaque direction est le constat de la carte d'Opus 4.8, à 0,10×.
add('FR', 'volet11_1_a_20', 23, [
    ("Des vecteurs de contrôle aléatoires n'écartent que", "Des vecteurs de contrôle aléatoires de même norme n'écartent que"),
    ("chaque direction dégrade les sorties, et l'effet", "chaque direction dégradait les sorties dans la carte d'Opus 4.8, à 0,10×, et l'effet")])
add('EN', 'volet11_1_a_20', 24, [
    ("Random control vectors rule out only", "Matched-norm random control vectors rule out only"),
    ("every direction degrades the outputs, and the effect", "every direction degraded the outputs in the Opus 4.8 card, at 0.10×, and the effect")])
# P3 — réponse 6 : la meilleure de 1 000 directions aléatoires, pas « des directions aléatoires ».
add('FR', 'volet11_1_a_20', 29, [(
    "si saillante que des directions aléatoires la séparent déjà (passation",
    "si saillante que la meilleure de 1 000 directions aléatoires atteint déjà 95,3 % (passation")])
add('EN', 'volet11_1_a_20', 30, [(
    "so salient that random directions already separate it (handover",
    "so salient that the best of 1,000 random directions already reaches 95.3% (handover")])
# P4 — prémisse « Alignment faking went away » : le RL a entraîné la conformité ET fait monter le raisonnement.
add('FR', 'volet11_1_a_20', 63, [(
    "et ce que le RL a entraîné est la conformité, qui a fait monter le raisonnement de faux alignement sans que l'article en fasse la cause (fiche 14",
    "et le RL a entraîné la conformité et fait monter le raisonnement de faux alignement, sans que l'article fasse de ce raisonnement la cause de la conformité, qui monte aussi hors surveillance (fiche 14")])
add('EN', 'volet11_1_a_20', 64, [(
    "and what the RL trained was compliance, which raised alignment-faking reasoning without the paper making it the cause (reading sheet 14",
    "and the RL trained compliance and raised alignment-faking reasoning, without the paper making that reasoning the cause of compliance, which also rises when unmonitored (reading sheet 14")])
# P5 — prémisse « Persona vectors » : la parade de l'extraction supervisée existe (programme, partie 8).
add('FR', 'volet11_1_a_20', 65, [(
    "pour l'extraction supervisée, aucune parade connue ; on le dit (fiche 8).",
    "pour l'extraction supervisée, le diffing par crosscoder, qui cherche sans hypothèse (programme, partie 8).")])
add('EN', 'volet11_1_a_20', 66, [(
    "for supervised extraction, none known; say so (reading sheet 8).",
    "for supervised extraction, crosscoder diffing, which searches without a hypothesis (programme, part 8).")])
# P6 — réponse 13 : même faute de logique que P1.
add('FR', 'volet11_1_a_20', 67, [(
    "un nul à une direction peut venir d'un rang trop bas (fiche 7",
    "un nul à une direction ne sépare pas « il faut plus d'une direction » d'un instrument aveugle à cette dose (fiche 7")])
add('EN', 'volet11_1_a_20', 68, [(
    "a one-direction null can come from too low a rank (reading sheet 7",
    "a one-direction null does not separate \"more than one direction is needed\" from an instrument blind at that dose (reading sheet 7")])
# P7 — réponse 20 : la sonde neuve n'est pas dans la passation, §5.2 ; elle est au programme (E′, jeu δ).
add('FR', 'volet11_1_a_20', 91, [(
    "et une sonde neuve après tout entraînement (cours, volet 3, §3, K70 ; passation, §5.2).",
    "et une sonde neuve après tout entraînement (cours, volet 3, §3, K70 ; passation, §5.2 ; programme, parties 3 et 8).")])
add('EN', 'volet11_1_a_20', 92, [(
    "and a fresh probe after any training (course, Part 3, §3, K70; handover, §5.2).",
    "and a fresh probe after any training (course, Part 3, §3, K70; handover, §5.2; programme, parts 3 and 8).")])

# P24 — réponse 20 : « aucune parade établie » pour le réalisme des transcriptions, alors que la parade partielle de F·25
#        est donnée en B10 (n° 113 de la tranche 53-fin) et, après P16, à la réponse 61 : on l'aligne.
add('FR', 'volet11_1_a_20', 89, [(
    "pour le réalisme des transcriptions, aucune parade établie ; on le dit (cours, volet 7, F·23).",
    "pour le réalisme des transcriptions, une parade partielle seulement : le mesurer par un juge mis devant la paire, scellé et audité par des humains, et donner à leur construction de vraies ressources de déploiement (cours, volet 7, F·25 ; programme, partie 3) ; il reste ouvert, on le dit (cours, volet 7, F·23).")])
add('EN', 'volet11_1_a_20', 90, [(
    "for the realism of the transcripts, no established workaround; say so (course, Part 7, F·23).",
    "for the realism of the transcripts, only a partial workaround: measure it with a judge shown the pair, sealed and audited by humans, and give their construction real deployment resources (course, Part 7, F·25; programme, part 3); it remains open, say so (course, Part 7, F·23).")])

# ---------- tranche volet11_21_a_52 ----------
# P8 — réponse 24 : même ajout de source.
add('FR', 'volet11_21_a_52', 11, [(
    "sur un jeu d'indices disjoint (passation, §5.2) ; contre la bascule",
    "sur un jeu d'indices disjoint (passation, §5.2 ; programme, parties 3 et 8) ; contre la bascule")])
add('EN', 'volet11_21_a_52', 12, [(
    "on a disjoint cue set (handover, §5.2); against the flip",
    "on a disjoint cue set (handover, §5.2; programme, parts 3 and 8); against the flip")])
# P9 — réponse 32 : le programme lit aux deux positions, pas à l'une ou l'autre.
add('FR', 'volet11_21_a_52', 39, [(
    "et lire au premier jeton de la réponse ou au jeton d'action avec des raisons neutres préremplies",
    "et lire aux deux positions, au premier jeton de la réponse et au jeton d'action avec des raisons neutres préremplies")])
add('EN', 'volet11_21_a_52', 40, [(
    "and read at the first token of the response or at the action token with neutral reasons prefilled",
    "and read at both positions, the first token of the response and the action token with neutral reasons prefilled")])
# P10 — encadré « Chaîne de pensée », limite 6 : la parade existe, c'est celle de la limite 5.
add('FR', 'volet11_21_a_52', 77, [(
    "résumé seul)*\n>   **Parade :** aucune connue ; on le dit.",
    "résumé seul)*\n>   **Parade :** Ne pas prendre la verbalisation pour la mesure : un critère principal comportemental et une sonde latente. *(source : programme, partie 8)*")],
    ligne="> - **Limite :** Un entraînement à verbaliser multiplierait la verbalisation par 2,4 à 2,9 sans changer la conscience latente ni la conduite. *(source : rapport d'antériorité 4 du 2 octobre — rapport, résumé seul)*\n>   **Parade :** aucune connue ; on le dit.")
add('EN', 'volet11_21_a_52', 78, [(
    "abstract only)*\n>   **Workaround:** none known; say so.",
    "abstract only)*\n>   **Workaround:** Do not take verbalization as the measure: a behavioural main criterion and a latent probe. *(source: programme, part 8)*")],
    ligne="> - **Limit:** Training to verbalize would multiply verbalization by 2.4 to 2.9 without changing latent awareness or conduct. *(source: prior-art report 4 of 2 October — report, abstract only)*\n>   **Workaround:** none known; say so.")
# P11 — réponse 47 : « de même norme » ; dégradation attribuée à la carte d'Opus 4.8.
add('FR', 'volet11_21_a_52', 93, [
    ("Des vecteurs aléatoires en contrôle ne donnent que", "Des vecteurs aléatoires de même norme en contrôle ne donnent que"),
    ("et chaque direction dégrade les sorties (fiche 2)", "et, dans la carte d'Opus 4.8, à 0,10×, chaque direction dégradait les sorties (fiche 2)")])
add('EN', 'volet11_21_a_52', 94, [
    ("Random vectors as the control give only", "Matched-norm random vectors as the control give only"),
    ("and every direction degrades the outputs (reading sheet 2)", "and, in the Opus 4.8 card, at 0.10×, every direction degraded the outputs (reading sheet 2)")])
# P12 — réponse 48 : ajout de source pour la sonde neuve et le jeu d'indices disjoint.
add('FR', 'volet11_21_a_52', 99, [(
    "que la même lecture doit voir (passation, §5.2 ; cours, volet M, M5).",
    "que la même lecture doit voir (passation, §5.2 ; programme, parties 3 et 8 ; cours, volet M, M5).")])
add('EN', 'volet11_21_a_52', 100, [(
    "that the same reading must see (handover, §5.2; course, Part M, M5).",
    "that the same reading must see (handover, §5.2; programme, parts 3 and 8; course, Part M, M5).")])
# P13 — réponse 51 : le 64,7 % et l'échec du Logit Lens valent pour RMU.
add('FR', 'volet11_21_a_52', 113, [(
    "après désapprentissage, le Logit Lens ne trouve plus rien",
    "après désapprentissage par RMU, le Logit Lens ne trouve plus rien")])
add('EN', 'volet11_21_a_52', 114, [(
    "after unlearning, the Logit Lens finds nothing",
    "after unlearning by RMU, the Logit Lens finds nothing")])

# ---------- tranche volet11_53_et_fin ----------
# P14 — réponse 56 : « de même norme » ; dégradation attribuée à la carte d'Opus 4.8.
add('FR', 'volet11_53_et_fin', 5, [
    ("Des vecteurs aléatoires en contrôle n'écartent que", "Des vecteurs aléatoires de même norme en contrôle n'écartent que"),
    ("chaque direction dégrade les sorties, et Opus 4.6", "chaque direction dégradait les sorties dans la carte d'Opus 4.8, à 0,10×, et Opus 4.6")])
add('EN', 'volet11_53_et_fin', 6, [
    ("Random control vectors rule out only", "Matched-norm random control vectors rule out only"),
    ("every direction degrades the outputs, and Opus 4.6", "every direction degraded the outputs in the Opus 4.8 card, at 0.10×, and Opus 4.6")])
# P15 — réponse 60 : « plus faiblement » ne vaut que pour Opus 4.8 ; une reproduction externe les trouve aussi forts.
add('FR', 'volet11_53_et_fin', 17, [(
    "font aussi monter le désalignement, plus faiblement, et un contrôle de même norme n'est que le nul de spécificité (fiche 2 ; cours, volet M, M4)",
    "font aussi monter le désalignement, plus faiblement dans la carte système d'Opus 4.8, aussi fort dans une reproduction externe sur un modèle à poids ouverts, et un contrôle de même norme n'est que le nul de spécificité (fiche 2 ; cours, volet 11, réponse 19 ; cours, volet M, M4)")])
add('EN', 'volet11_53_et_fin', 18, [(
    "also raise misalignment, more weakly, and a matched-norm control is only the specificity null (reading sheet 2; course, Part M, M4)",
    "also raise misalignment, more weakly in the Opus 4.8 system card, just as strongly in an external reproduction on an open-weights model, and a matched-norm control is only the specificity null (reading sheet 2; course, Part 11, answer 19; course, Part M, M4)")])
# P16 — réponse 61 : « aucune parade connue » contredit la parade donnée juste avant et la n° 113 ; parade partielle de F·25.
add('FR', 'volet11_53_et_fin', 21, [(
    "pour le réalisme des transcriptions synthétiques, aucune parade connue ; on le dit (cours, volet 7, F·23).",
    "pour les transcriptions synthétiques elles-mêmes, une parade partielle seulement : mesurer leur réalisme par un juge mis devant la paire, scellé et audité par des humains, et donner à leur construction de vraies ressources de déploiement (cours, volet 7, F·25 ; programme, partie 3) ; leur réalisme reste ouvert, on le dit (cours, volet 7, F·23).")])
add('EN', 'volet11_53_et_fin', 22, [(
    "for the realism of the synthetic transcripts, no workaround is known; say so (course, Part 7, F·23).",
    "for the synthetic transcripts themselves, only a partial workaround: measure their realism with a judge shown the pair, sealed and audited by humans, and give their construction real deployment resources (course, Part 7, F·25; programme, part 3); their realism remains open, say so (course, Part 7, F·23).")])
# P17 — réponse 62 : logique inversée (le cas connu exigé était le succès de la sonde).
add('FR', 'volet11_53_et_fin', 25, [(
    "« Ne généraliseraient jamais » serait un nul d'instrument : il ne compte qu'avec un cas connu où la même sonde, au même réglage, attrape hors distribution une intention qu'on a installée — sinon l'échec dit peut-être seulement que la sonde est aveugle (cours, volet M, M5 ; passation, §5.2).",
    "« Ne généraliseraient jamais » ne se constate que là où l'on sait l'intention présente : hors distribution, sur un organisme où on l'a installée, une sonde qui reste muette montre qu'elle ne généralise pas ; sur un modèle naturel, son silence ne départage pas « elle ne généralise pas » et « il n'y a rien à voir » (cours, volet M, M5 ; passation, §5.2).")])
add('EN', 'volet11_53_et_fin', 26, [(
    "\"Never generalise\" would be an instrument null: it counts only with a known case in which the same probe, at the same setting, catches out of distribution an intention that was installed — otherwise the failure may only say that the probe is blind (course, Part M, M5; handover, §5.2).",
    "\"Never generalise\" can only be established where the intention is known to be present: out of distribution, on an organism in which it was installed, a probe that stays silent shows it does not generalise; on a natural model, its silence does not separate \"it does not generalise\" from \"there is nothing to see\" (course, Part M, M5; handover, §5.2).")])
# P18 — A2 : les deux positions de lecture.
add('FR', 'volet11_53_et_fin', 37, [(
    "lire au premier jeton avant toute raison écrite ou au jeton d'action avec des raisons neutres préremplies",
    "lire aux deux positions, au premier jeton avant toute raison écrite et au jeton d'action avec des raisons neutres préremplies")])
add('EN', 'volet11_53_et_fin', 38, [(
    "read at the first token before any written reason or at the action token with neutral reasons prefilled",
    "read at both positions, the first token before any written reason and the action token with neutral reasons prefilled")])
# P19 — B2 : « un contrôle aléatoire » n'est le nul de spécificité que de même norme.
add('FR', 'volet11_53_et_fin', 77, [(
    "Un contrôle aléatoire de l'inhibition n'est que le nul de spécificité",
    "Pour l'inhibition, un contrôle aléatoire de même norme n'est que le nul de spécificité")])
add('EN', 'volet11_53_et_fin', 78, [(
    "A random control for the inhibition is only the specificity null",
    "For the inhibition, a matched-norm random control is only the specificity null")])
# P20 — B4 : même correction que P15.
add('FR', 'volet11_53_et_fin', 85, [(
    "font aussi monter le désalignement, plus faiblement, et un contrôle de même norme n'est que le nul de spécificité (fiche 2 ; cours, volet M, M4)",
    "font aussi monter le désalignement, plus faiblement dans la carte système d'Opus 4.8, aussi fort dans une reproduction externe sur un modèle à poids ouverts, et un contrôle de même norme n'est que le nul de spécificité (fiche 2 ; cours, volet 11, réponse 19 ; cours, volet M, M4)")])
add('EN', 'volet11_53_et_fin', 86, [(
    "also raise misalignment, more weakly, and a matched-norm control is only the specificity null (reading sheet 2; course, Part M, M4)",
    "also raise misalignment, more weakly in the Opus 4.8 system card, just as strongly in an external reproduction on an open-weights model, and a matched-norm control is only the specificity null (reading sheet 2; course, Part 11, answer 19; course, Part M, M4)")])
# P21 — B8 : la formule du pot de miel n'est pas dans la fiche 3 ; « se retenir » vient de K63 ; parade de K63 pour la retenue.
add('FR', 'volet11_53_et_fin', 103, [
    ("le modèle peut y remarquer le test et se retenir, et dans une simulation, « c'est faux » est vrai, si bien qu'un pot de miel ne sépare pas un modèle qui le lit comme factice d'un modèle qui se retient (fiche 13 ; fiche 3)",
     "le modèle peut y remarquer le test et se retenir, et dans une simulation, « c'est faux » est vrai (cours, volet 2, §B, K63 ; fiche 13 ; fiche 3)"),
    ("contre le pot de miel lu comme factice et contre la mémorisation, aucune parade connue ; on le dit (fiche 3 ; fiches, partie C).",
     "contre le confondeur de la simulation lui-même et contre la mémorisation, aucune parade connue ; on le dit (fiche 3 ; fiches, partie C).")])
add('EN', 'volet11_53_et_fin', 104, [
    ("the model can notice the test there and hold back, and in a simulation \"this is fake\" is true, so a honeypot does not separate a model that reads it as fake from one that holds back (reading sheet 13; reading sheet 3)",
     "the model can notice the test there and hold back, and in a simulation \"this is fake\" is true (course, Part 2, §B, K63; reading sheet 13; reading sheet 3)"),
    ("against a honeypot read as fake and against memorization, no workaround is known; say so (reading sheet 3; reading sheets, part C).",
     "against the simulation confound itself and against memorization, no workaround is known; say so (reading sheet 3; reading sheets, part C).")])
# P22 — B9 : le prompt (K4) n'a pas de rang et n'est pas comparé à dégradation appariée.
add('FR', 'volet11_53_et_fin', 109, [(
    "plusieurs familles de témoins au même rang — sous-espaces aléatoires, contrastes sans rapport, directions de forte variance, simple prompt — comparées à dégradation appariée, et un organisme",
    "plusieurs familles de témoins — sous-espaces aléatoires, contrastes sans rapport et directions de forte variance, au même rang et comparés à dégradation appariée, plus un simple prompt —, et un organisme")])
add('EN', 'volet11_53_et_fin', 110, [(
    "several families of controls at the same rank — random subspaces, unrelated contrasts, high-variance directions, a plain prompt — compared at matched degradation, and an evaluation-conditioned",
    "several families of controls — random subspaces, unrelated contrasts and high-variance directions, at the same rank and compared at matched degradation, plus a plain prompt —, and an evaluation-conditioned")])
# P23 — B10 : même formule du pot de miel ; la remarque du test vient de K63 et de la fiche 13.
add('FR', 'volet11_53_et_fin', 113, [
    ("et ne laisser passer que les vraies : un pot de miel ne sépare pas un modèle qui le lit comme factice d'un modèle qui se retient (fiche 3 ; cours, volet 2, §B).",
     "et ne laisser passer que les vraies : un modèle peut remarquer le test et s'y conduire mieux (cours, volet 2, §B, K63 ; fiche 13)."),
    ("contre un moniteur qui lit le pot de miel comme factice, aucune parade connue ; on le dit (fiche 3).",
     "contre un moniteur qui reconnaît encore ces attaques comme factices, aucune parade connue ; on le dit.")])
add('EN', 'volet11_53_et_fin', 114, [
    ("and let only the real ones through: a honeypot does not separate a model that reads it as fake from one that holds back (reading sheet 3; course, Part 2, §B).",
     "and let only the real ones through: a model can notice the test and behave better there (course, Part 2, §B, K63; reading sheet 13)."),
    ("against a monitor that reads the honeypot as fake, no workaround is known; say so (reading sheet 3).",
     "against a monitor that still recognizes those attacks as fake, no workaround is known; say so.")])

# ---------- construction ----------
corr = []
for fi, tr, n, reps, ligne in C:
    ins = INS[tr][n - 1]
    assert ins['fichier'] == fi, (tr, n, fi)
    texte = ins['texte']
    if ligne is None:
        lignes = [l for l in texte.split('\n') if any(a in l for a, _ in reps)]
        assert len(lignes) == 1, (tr, n, len(lignes))
        ancien = lignes[0]
    else:
        ancien = ligne
        assert ancien in texte, (tr, n, 'ligne absente')
    nouveau = ancien
    for a, b in reps:
        assert nouveau.count(a) == 1, (tr, n, fi, 'sous-chaîne', a[:60], nouveau.count(a))
        nouveau = nouveau.replace(a, b)
    corr.append({'fichier': fi, 'ancien': ancien, 'nouveau': nouveau, '_tr': tr, '_n': n})

# ---------- contrôles ----------
ok = True
# 1) présent une seule fois dans la v3.6, absent de la v3.5
for c in corr:
    k = OUT[c['fichier']].count(c['ancien'])
    if k != 1:
        print('NON UNIQUE dans la v3.6', k, c['_tr'], c['_n']); ok = False
    if c['ancien'] in SRC[c['fichier']]:
        print('PRÉSENT dans la v3.5', c['_tr'], c['_n']); ok = False
# 2) unicité après application simulée des corrections des groupes 1 à 6, puis de celles-ci
sim = dict(OUT)
for g in range(1, 7):
    try:
        d = json.load(open(f'{W}/travail/corrections_groupe_{g}.json', encoding='utf8'))
    except FileNotFoundError:
        continue
    for x in d['corrections']:
        if sim[x['fichier']].count(x['ancien']) == 1:
            sim[x['fichier']] = sim[x['fichier']].replace(x['ancien'], x['nouveau'])
for c in corr:
    k = sim[c['fichier']].count(c['ancien'])
    if k != 1:
        print('NON UNIQUE après groupes 1-6', k, c['_tr'], c['_n']); ok = False
    sim[c['fichier']] = sim[c['fichier']].replace(c['ancien'], c['nouveau'])
# 3) citations de moins de quinze mots dans les nouveaux textes
for c in corr:
    for q in re.findall(r'«\s*([^»]*?)\s*»', c['nouveau']) + re.findall(r'"([^"]*)"', c['nouveau']):
        if len(q.split()) >= 15:
            print('CITATION LONGUE', c['_tr'], c['_n'], q); ok = False
# 4) le texte nouveau garde le format (préfixe) de l'ancien
for c in corr:
    if c['ancien'][:12] != c['nouveau'][:12]:
        print('FORMAT changé', c['_tr'], c['_n']); ok = False
# 5) paires FR/EN complètes
from collections import Counter
cnt = Counter((c['_tr'], (c['_n'] + 1) // 2) for c in corr)
for k, v in cnt.items():
    if v != 2:
        print('PAIRE INCOMPLÈTE', k, v); ok = False

out = {'corrections': [{'fichier': c['fichier'], 'ancien': c['ancien'], 'nouveau': c['nouveau']} for c in corr]}
p = f'{W}/travail/corrections_groupe_7.json'
json.dump(out, open(p, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
json.load(open(p, encoding='utf8'))
print(len(corr), 'corrections ;', 'toutes les vérifications passent' if ok else 'ÉCHEC')
