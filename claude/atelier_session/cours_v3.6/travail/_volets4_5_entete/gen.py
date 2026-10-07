#!/usr/bin/env python3
"""Génère travail/insertions_volets4_5_entete.json (tranche volets4_5_entete).

Les ancres sont prises directement dans la v3.5 par numéro de ligne (texte exact) ;
les encadrés complets et les deux avertissements prêts sont repris mot pour mot du référentiel.
"""
import json, os, re

W = '/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
SRC = {'FR': f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md', 'EN': f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md'}
TR = {'FR': (1111, 1368), 'EN': (1252, 1563)}
REF = f'{W}/travail/referentiel_instruments.md'
OUT = f'{W}/travail/insertions_volets4_5_entete.json'

L = {k: open(v, encoding='utf8').read().split('\n') for k, v in SRC.items()}
ref = open(REF, encoding='utf8').read()


def box(num, lang):
    part1 = ref.split('# Partie 2 — Par tranche')[0]
    sec = [s for s in re.split(r'\n(?=## \d+\. )', part1) if s.startswith(f'## {num}. ')][0]
    label = 'français' if lang == 'FR' else 'anglais'
    return re.search(r'\*\*Encadré complet, ' + label + r' :\*\*\n\n~~~markdown\n(.*?)\n~~~', sec, re.S).group(1)


def ready_warnings():
    part = ref.split('## `volets4_5_entete`')[1].split('## `volet6`')[0]
    blocks = re.findall(r'~~~markdown\n(> ⚠ \*\(v3\.6\)\*.*?)\n~~~', part, re.S)
    out = []
    for b in blocks:
        fr, en = b.split('\n')
        out.append((fr, en))
    return out


RW = ready_warnings()
assert len(RW) == 2, RW

# Lieux des encadrés (renvois), FR / EN, repris du référentiel
LOC = {
    'org': ("organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives »)",
            'model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives")'),
    'eval': ("évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging »)",
             'behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging")'),
    'probe': ("sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth »)",
              'activation probes → Part 2, §C (after "In practice — The Geometry of Truth")'),
    'steer': ("pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition »)",
              'steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition")'),
    'jlens': ("J-lens et espace de travail → volet 2, C bis (après « Le test, tel qu'il se dit »)",
              'J-lens and workspace → Part 2, C bis (after "The test, as it is said")'),
    'abl': ("ablation et projection → volet 2, §D (après « La méthode »)",
            'ablation and projection → Part 2, §D (after "The method")'),
    'debate': ("débat et supervision évolutive → volet 2, §E (après « En pratique — Debate »)",
               'debate and scalable oversight → Part 2, §E (after "In practice — Debate")'),
    'unsup': ("élicitation non supervisée → volet 2, §E (fin du cas d'application K52)",
              'unsupervised elicitation → Part 2, §E (end of worked case K52)'),
    'w2s': ("généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation »)",
            'weak-to-strong generalization → Part 2, §F (after "In practice — automation")'),
    'mon': ("moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes »)",
            'control monitors → Part 2, §G (after "In practice — coup probes")'),
    'red': ("red-teaming → volet 2, §H (après « En pratique — StrongREJECT »)",
            'red-teaming → Part 2, §H (after "In practice — StrongREJECT")'),
    'unl': ("désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve »)",
            'unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test")'),
    'sae': ("dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity",
            'dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity'),
    'graph': ("graphes d'attribution → volet 4, Circuit Tracing",
              'attribution graphs → Part 4, Circuit Tracing'),
    'nla': ("autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle",
            'natural-language autoencoders → Part 4, The recent wave on model cognition'),
    'self': ("auto-rapport et introspection → volet 5, partie II, A, sujet 13",
             'self-report and introspection → Part 5, Section II, A, Topic 13'),
    'judge': ("juges LLM → volet 6, §2 (après « La loi de déplacement »)",
              'LLM judges → Part 6, §2 (after "The displacement law")'),
    'ftd': ("détecteurs fine-tunés → volet 7, F·29",
            'fine-tuned detectors → Part 7, F·29'),
    'oracle': ("oracles d'activation → volet 10, fiche LatentQA",
               'activation oracles → Part 10, LatentQA sheet'),
    'cot': ("chaîne de pensée comme moniteur → volet 11, réponse 43",
            'chain of thought as a monitor → Part 11, answer 43'),
    'rand': ("contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme »)",
             'random controls → Part M, M4 (after "The matched-norm random direction")'),
    'deg': ("dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse »)",
            'matched degradation and dose-response → Part M, M4 (after "Dose-response")'),
    'known': ("cas connu → volet M, M5 (fin de section)",
              'known case → Part M, M5 (end of section)'),
}


def renvoi(keys):
    fr = '> ⚠ **Limites et parades** : ' + ' ; '.join(LOC[k][0] for k in keys) + ' *(v3.6)*'
    en = '> ⚠ **Limits and workarounds**: ' + '; '.join(LOC[k][1] for k in keys) + ' *(v3.6)*'
    return fr, en


def warn(fr, en):
    return '> ⚠ *(v3.6)* ' + fr, '> ⚠ *(v3.6)* ' + en


# Chaque élément : (ligne FR v3.5, ligne EN v3.5, texte FR, texte EN), dans l'ordre d'insertion
ITEMS = []


def add(lfr, len_, pair):
    ITEMS.append((lfr, len_, pair[0], pair[1]))


# ---------------- VOLET 4 ----------------
# Sleeper Agents
add(1121, 1263, warn(
    "L'extension proposée a déjà sa réponse, et sa limite : une sonde linéaire bâtie sur des paires de contraste génériques détecte la défection de ces portes dérobées avec une AUROC de plus de 99 %, mais la meilleure de 1 000 directions aléatoires atteint déjà 95,3 %, et les auteurs disent que cette saillance pourrait venir de l'insertion (fiche 15). Parade : situer la sonde dans la distribution des directions aléatoires, jamais contre un seul tirage, et ne lire ce succès que comme un cas connu qui borne l'instrument, pas comme une preuve sur une tromperie apparue d'elle-même (programme, partie 7 ; cours, volet M, M5).",
    "The proposed extension already has its answer, and its limit: a linear probe built from generic contrast pairs detects these backdoors' defection with an AUROC above 99%, but the best of 1,000 random directions already reaches 95.3%, and the authors say this salience could come from the insertion (reading sheet 15). Workaround: place the probe within the distribution of random directions, never against a single draw, and read this success only as a known case that bounds the instrument, not as proof about deception that arose on its own (programme, part 7; course, Part M, M5)."))
add(1121, 1263, renvoi(['org', 'red', 'probe', 'known']))

# Alignment Faking
add(1125, 1267, warn(
    "Le scratchpad donne le motif, pas la cause : le RL fait monter le raisonnement de faux alignement, mais la conformité monte aussi hors entraînement, et le papier ne fait pas de ce raisonnement la cause de la conformité — parade : s'en tenir à la mesure, l'écart de conformité entre le cas « entraîné » et le cas hors surveillance, et juger ce que le modèle fait, pas ce qu'il en dit (fiche 14 ; fiches, partie C ; passation, §5.1). Toute réplication sur un modèle récent mesure peut-être la mémorisation du scénario, ses transcripts ayant été réinclus dans l'entraînement : aucune parade connue, on le dit (fiches, partie C).",
    "The scratchpad gives the motive, not the cause: RL raises alignment-faking reasoning, but compliance also rises outside training, and the paper does not make that reasoning the cause of compliance — workaround: stick to the measure, the compliance gap between the \"trained\" case and the unmonitored case, and judge what the model does, not what it says about it (reading sheet 14; reading sheets, part C; handover, §5.1). Any replication on a recent model may measure memorization of the scenario, its transcripts having been re-included in training: no workaround known; say so (reading sheets, part C)."))
add(1125, 1267, renvoi(['eval', 'cot', 'org']))

# Sycophancy (Sharma)
add(1131, 1273, warn(
    "Cette extension, ton dépôt l'a tentée sur Llama 3.1 8B Instruct : aucune intervention à une direction n'a réduit le taux jugé (rapportées sans chiffres, faute de sorties brutes conservées), et la baisse obtenue en retirant un sous-espace de rang trois venait d'un adoucissement générique des verdicts négatifs, même sans pression, lu à travers une fenêtre de juge tronquée ; elle n'est pas revenue sur des générations fraîches (README du dépôt). Parade : le bras sans pression, des générations fraîches à graines appariées gardées en texte complet et jugées sur la réponse entière, et des sous-espaces aléatoires de même rang comparés à dégradation appariée (cours, volet M, M4 ; cours, volet 6, §6 ; cours, volet 2, C bis ; programme, partie 7).",
    "Your repository tried this extension on Llama 3.1 8B Instruct: no single-direction intervention reduced the judged rate (reported without numbers, the raw outputs not having been kept), and the drop obtained by removing a rank-three subspace came from a generic softening of negative verdicts, even without pressure, read through a truncated judge window; it did not come back on fresh generations (repository README). Workaround: the no-pressure arm, fresh seed-matched generations kept as full text and judged on the whole answer, and random subspaces of the same rank compared at matched degradation (course, Part M, M4; course, Part 6, §6; course, Part 2, C bis; programme, part 7)."))
add(1131, 1273, renvoi(['eval', 'abl', 'judge']))

# The Geometry of Truth
add(1137, 1279, warn(
    "« Intervenir dessus modifie le comportement du modèle » ne dit pas encore que le concept cause le comportement : une direction aléatoire de même norme n'en est que le nul de spécificité, et le dommage ne s'écarte qu'à dégradation appariée, par une courbe dose-réponse contre plusieurs témoins (fiches, partie B, piège 4 ; cours, volet M, M4 ; cours, volet 2, §C, K47). Et « la direction généralise à de nouveaux jeux d’énoncés » ne vaut que mesuré sur des familles entières tenues à part, jamais des paraphrases, d'un tour à l'agentique à plusieurs tours (fiches, partie B, piège 1 ; explication du 2 octobre, §3 ; programme, partie 3).",
    "\"Intervening on it changes the model's behavior\" does not yet say that the concept causes the behaviour: a matched-norm random direction is only its specificity null, and damage is ruled out only at matched degradation, by a dose-response curve against several controls (reading sheets, part B, trap 4; course, Part M, M4; course, Part 2, §C, K47). And \"the direction generalizes to new sets of statements\" holds only when measured on whole held-out families, never paraphrases, from single-turn to multi-turn agentic (reading sheets, part B, trap 1; explanation of 2 October, §3; programme, part 3)."))
add(1137, 1279, renvoi(['probe', 'steer', 'deg']))

# RepE
add(1141, 1283, warn(
    "Dans RepE même, détecter n'est pas piloter : la direction de la régression logistique lit le mieux, mais la renforcer ou la retirer ne change presque rien au comportement ; sur les modèles « quirky », à transfert comparable, les directions logistiques sont bien moins causales que la différence des moyennes (cours, volet 10, n° 53 et n° 30). Parade : pour intervenir, ne retenir une direction qu'après le test causal — piloter le long d'elle contre des directions aléatoires de même norme, nul de spécificité, puis contre des témoins à dégradation appariée (cours, volet M, M8 ; passation, §5.2).",
    "In RepE itself, detecting is not steering: the logistic-regression direction reads best, but strengthening or suppressing it barely changes behaviour; on the \"quirky\" models, at comparable transfer, the logistic directions are far less causal than the mean difference (course, Part 10, no. 53 and no. 30). Workaround: to intervene, keep a direction only after the causal test — steer along it against matched-norm random directions, the specificity null, then against controls at matched degradation (course, Part M, M8; handover, §5.2)."))
add(1141, 1283, renvoi(['probe', 'steer', 'unsup']))

# CCS
add(1145, 1287, renvoi(['unsup', 'probe']))

# CAA et ITI : avertissement prêt du référentiel, puis renvoi
add(1149, 1291, RW[0])
add(1149, 1291, renvoi(['steer', 'rand', 'deg']))

# Monosemanticity : encadré complet (maison)
add(1157, 1297, (box(19, 'FR'), box(19, 'EN')))

# Circuit Tracing : encadré complet (maison)
add(1161, 1301, (box(20, 'FR'), box(20, 'EN')))

# La vague récente : encadré NLA (maison), avertissement, renvoi
add(1167, 1307, (box(21, 'FR'), box(21, 'EN')))
add(1167, 1307, warn(
    "Deux résultats de ce passage viennent sans leur limite. Les activation oracles peuvent confabuler des suppositions plausibles, souvent fausses et mal calibrées, et en lecture seule n'ont pas fait mieux que le transcript dans CHIVE — parade : les tester sur des variantes fine-tunées à comportement connu, jamais vues, et corroborer par une méthode indépendante (fiche 18 ; fiche 4) ; et des concept vectors d'émotions sont « manipulables » par pilotage, où une direction aléatoire de même norme n'est que le nul de spécificité : le dommage ne s'écarte qu'à dégradation appariée (fiche 9 ; fiche 2 ; cours, volet M, M4).",
    "Two results in this passage come without their limit. Activation oracles can confabulate plausible guesses, often wrong and poorly calibrated, and read-only they did no better than the transcript in CHIVE — workaround: test them on fine-tuned variants with known behaviour, never seen before, and corroborate with an independent method (reading sheet 18; reading sheet 4); and emotion concept vectors are \"manipulable\" through steering, where a matched-norm random direction is only the specificity null: damage is ruled out only at matched degradation (reading sheet 9; reading sheet 2; course, Part M, M4)."))
add(1167, 1307, renvoi(['oracle', 'self', 'steer']))

# AI Control
add(1173, 1313, warn(
    "« Une grande part des tentatives » est un chiffre de red team : il dépend de la force du saboteur supposé — ailleurs, sur cinq environnements SHADE-Arena, un échafaudage d'attaque optimisé composante par composante a fait tomber un score de sûreté de 0,87 à 0,41 (cours, volet 7, F·24). Parade : dire quelle red team le chiffre suppose, au moins une red team optimisée composante par composante, avec l'ablation de chaque composante ; et, pour l'extension, une sonde en production peut échouer en silence, d'où des canaris, un score de dérive et un échantillon frais jugé chaque mois (cours, volet 7, F·24 ; cours, volet 3, §3, K70).",
    "\"A large share of the attempts\" is a red-team number: it depends on the strength of the assumed saboteur — elsewhere, on five SHADE-Arena environments, an attack scaffold optimized component by component brought a safety score down from 0.87 to 0.41 (course, Part 7, F·24). Workaround: say which red team the number assumes, at least one optimized component by component, with each component ablated; and, for the extension, a probe in production can fail silently, hence canaries, a drift score and a fresh sample judged every month (course, Part 7, F·24; course, Part 3, §3, K70)."))
add(1173, 1313, renvoi(['mon', 'red', 'probe']))

# Debate
add(1177, 1317, renvoi(['debate', 'judge']))

# Weak-to-Strong
add(1181, 1321, renvoi(['w2s']))

# Auditing Hidden Objectives
add(1187, 1327, warn(
    "Que les features SAE aient aidé ne chiffre pas l'apport de l'interprétabilité : l'équipe qui avait les données sans SAE a réussi, celle qui n'avait qu'un accès API a échoué, et quatre équipes hétérogènes ne permettent aucune conclusion ferme ; l'objectif était en outre décrit en clair dans les documents synthétiques (fiche 16). Parade : une ablation d'affordance — retirer un seul outil à une équipe — chiffre ce que l'interprétabilité apporte (fiche 16 ; cours, volet 5, sujet 9).",
    "That SAE features helped does not quantify what interpretability adds: the team that had the data but no SAE succeeded, the team with only API access failed, and four heterogeneous teams allow no firm conclusion; the objective was also stated plainly in the synthetic documents (reading sheet 16). Workaround: an affordance ablation — removing a single tool from a team — quantifies what interpretability brings (reading sheet 16; course, Part 5, topic 9)."))
add(1187, 1327, renvoi(['org', 'sae']))

# GCG
add(1197, 1337, renvoi(['red']))

# Constitutional AI
add(1201, 1341, renvoi(['judge', 'red']))

# Unlearning (Deeb et Roger)
add(1205, 1345, renvoi(['unl', 'known']))

# ---------------- VOLET 5 ----------------
# §1 La thèse-signature
add(1221, 1392, warn(
    "Chaque moitié de la thèse a sa limite dans ton dépôt. « Les directions lisibles existent » repose sur une corrélation qui peut n'être qu'un ajustement d'entraînement — parade : scorer des items exclus de l'entraînement de la sonde, extraits sur un jeu disjoint (README du dépôt) — et « plusieurs méthodes de rang un ont échoué » est un nul rapporté sans chiffres, faute de sorties brutes, qui ne compte qu'avec un cas connu au même réglage, comme un vecteur de pays qui s'échange dans l'article sur l'espace de travail (README du dépôt ; cours, volet 2, §C, K47 ; cours, volet M, M5).",
    "Each half of the thesis has its limit in your repository. \"Readable directions exist\" rests on a correlation that may be only training fit — workaround: score items excluded from the probe's training, extracted on a disjoint set (repository README) — and \"several rank-one methods failed\" is a null reported without numbers, the raw outputs not having been kept, which counts only with a known case at the same setting, such as a country vector that swaps in the workspace paper (repository README; course, Part 2, §C, K47; course, Part M, M5)."))
add(1223, 1394, renvoi(['probe', 'steer', 'abl', 'sae']))

# §3 L'ancrage empirique
add(1233, 1406, warn(
    "La dégradation appariée écarte le dommage, pas encore la spécificité : la carte de Fable 5 pilote assez faiblement pour rendre la dégradation négligeable, mais ses témoins restent « comparable or smaller » sur l'axe du désalignement, et celle d'Opus 4.6 ne trouvait aucune différence notable avec des contrôles aléatoires sur la tromperie et la complaisance (fiche 2). Parade : une courbe dose-réponse contre plusieurs familles de témoins, au même rang et à dégradation appariée, la courbe du concept devant passer au-dessus à chaque niveau de dommage (cours, volet 2, §C, K47 ; programme, parties 3 et 7).",
    "Matched degradation rules out damage, not yet specificity: the Fable 5 card steers weakly enough to make degradation negligible, yet its controls stay \"comparable or smaller\" on the misalignment axis, and the Opus 4.6 card found no notable difference from random controls on deception and sycophancy (reading sheet 2). Workaround: a dose-response curve against several families of controls, at the same rank and at matched degradation, the concept's curve having to rise above them at every level of damage (course, Part 2, §C, K47; programme, parts 3 and 7)."))
add(1233, 1406, renvoi(['steer', 'deg', 'rand']))

# §4 La théorie de l'impact
add(1237, 1411, warn(
    "Le canal interne a lui aussi sa faille : itérer contre ses détecteurs sélectionne l'évasion, et, selon un rapport, après un RL des sondes neuves hors domaine se dégradent, le concept ayant quitté la direction générale (fiche 19 ; rapport d'antériorité 3 du 2 octobre, The Obfuscation Atlas — rapport). Parade : des détecteurs scellés, hors de la boucle, contre lesquels on n'entraîne jamais, et une sonde neuve après tout entraînement, sur un jeu d'indices disjoint (fiche 19 ; fiche 17 ; passation, §5.2 ; programme, partie 3).",
    "The internal channel has its own flaw: iterating against your detectors selects for evasion, and, according to a report, after RL fresh out-of-domain probes degrade, the concept having left the general direction (reading sheet 19; prior-art report 3 of 2 October, The Obfuscation Atlas — report). Workaround: sealed detectors, outside the loop, never trained against, and a fresh probe after any training, on a disjoint cue set (reading sheet 19; reading sheet 17; handover, §5.2; programme, part 3)."))
add(1237, 1411, renvoi(['probe', 'mon', 'known']))

# §6 Gérer le pushback
add(1245, 1421, renvoi(['abl', 'probe']))

# Sujet 1
add(1255, 1433, warn(
    "La direction qui lit le mieux n'est pas forcément celle qui agit : chez RepE, la direction logistique lit le mieux mais la pousser ou la retirer ne change presque rien, et sur les modèles « quirky » les directions logistiques sont bien moins causales que la différence des moyennes — parade : passer chaque étape du pipeline, pas seulement la meilleure lectrice, au test causal à dégradation appariée (cours, volet 10, n° 53 et n° 30 ; cours, volet M, M4). Et le silence d'une sonde de déception ne départage pas « pas de déception » et « sonde aveugle » — parade : un organisme où l'on a installé la déception soi-même, sur lequel on mesure sensibilité et fausses alarmes, son silence ailleurs devenant une borne (passation, §5.2 ; explication du 2 octobre, §1).",
    "The direction that reads best is not necessarily the one that acts: in RepE, the logistic direction reads best but strengthening or suppressing it barely changes anything, and on the \"quirky\" models the logistic directions are far less causal than the mean difference — workaround: put every stage of the pipeline, not only the best reader, through the causal test at matched degradation (course, Part 10, no. 53 and no. 30; course, Part M, M4). And a deception probe's silence does not separate \"no deception\" from \"blind probe\" — workaround: an organism in which you installed the deception yourself, on which you measure sensitivity and false alarms, its silence elsewhere then becoming a bound (handover, §5.2; explanation of 2 October, §1)."))
add(1255, 1433, renvoi(['probe', 'ftd', 'mon', 'known']))

# Sujet 2
add(1259, 1437, warn(
    "La grille compare les interventions entre elles, pas à des témoins : chaque rang doit l'être à des sous-espaces aléatoires de même rang, au moins vingt tirages, et à d'autres familles de témoins, à dégradation appariée — une direction aléatoire de même norme n'est que le nul de spécificité (cours, volet M, M4 ; programme, parties 3 et 7). Et un échec de rang un est un nul : il ne compte qu'avec un cas connu au même réglage, comme un vecteur de pays qui s'échange dans l'article sur l'espace de travail (cours, volet 2, §C, K47 ; cours, volet M, M5).",
    "The grid compares the interventions with each other, not with controls: each rank must be compared with random subspaces of the same rank, at least twenty draws, and with other families of controls, at matched degradation — a matched-norm random direction is only the specificity null (course, Part M, M4; programme, parts 3 and 7). And a rank-one failure is a null: it counts only with a known case at the same setting, such as a country vector that swaps in the workspace paper (course, Part 2, §C, K47; course, Part M, M5)."))
add(1259, 1437, renvoi(['steer', 'abl', 'deg', 'rand']))

# Sujet 3
add(1265, 1443, renvoi(['sae', 'graph', 'abl']))

# Sujet 4 : avertissement prêt du référentiel, puis renvoi
add(1269, 1447, RW[1])
add(1269, 1447, renvoi(['cot', 'nla', 'probe', 'jlens']))

# Sujet 6
add(1273, 1451, warn(
    "Viser un très bas taux de faux positifs ne suffit pas : le chiffre qui compte est l'écart entre la détection en distribution et celle sur des types de mensonge tenus à part — des détecteurs fine-tunés montent à une AUROC de 0,95 en distribution, plafonnent à 0,70-0,75 d'une catégorie à l'autre et battent à peine un prompt (fiche 7 ; fiches, partie B, piège 1). Parade : une validation croisée sur des familles entières tenues à part, jamais des paraphrases, et battre le prompt à coût égal, en publiant le résultat sinon (fiche 7 ; explication du 2 octobre, §3 ; cours, volet 7, F·29).",
    "Aiming for a very low false-positive rate is not enough: the number that matters is the gap between in-distribution detection and detection on held-out lie types — fine-tuned detectors rise to an AUROC of 0.95 in distribution, plateau at 0.70-0.75 from one category to another and barely beat a prompt (reading sheet 7; reading sheets, part B, trap 1). Workaround: cross-validation on whole held-out families, never paraphrases, and beat the prompt at equal cost, publishing the result otherwise (reading sheet 7; explanation of 2 October, §3; course, Part 7, F·29)."))
add(1273, 1451, renvoi(['probe', 'unsup', 'ftd', 'org']))

# Sujet 10
add(1277, 1455, warn(
    "Comme instrument de mesure, un vecteur de trait ne donne qu'une corrélation : le lien entre le déplacement le long du vecteur et l'expression du trait est corrélationnel, le trait doit être nommé d'avance et la direction est une moyenne grossière (fiche 8). Parade : pour le levier, le test à dégradation appariée contre plusieurs témoins ; pour l'extraction supervisée, aucune parade connue, on le dit (cours, volet M, M4 ; fiche 8).",
    "As a measurement instrument, a trait vector gives only a correlation: the link between the shift along the vector and the expression of the trait is correlational, the trait must be named in advance and the direction is a coarse average (reading sheet 8). Workaround: for the lever, the matched-degradation test against several controls; for supervised extraction, none known; say so (course, Part M, M4; reading sheet 8)."))
add(1277, 1455, renvoi(['steer', 'eval', 'red']))

# Sujet 13 : encadré complet (maison), puis renvoi
add(1283, 1461, (box(22, 'FR'), box(22, 'EN')))
add(1283, 1461, renvoi(['probe', 'oracle', 'nla']))

# Partie II, B
add(1289, 1468, renvoi(['org', 'known']))            # Sujet 5
add(1293, 1472, renvoi(['mon', 'red', 'probe']))     # Sujet 8
add(1297, 1476, renvoi(['org', 'sae', 'graph']))     # Sujet 9
add(1301, 1480, renvoi(['cot']))                     # Sujet 7
add(1305, 1484, renvoi(['eval', 'w2s']))             # Sujet 11
add(1309, 1488, renvoi(['w2s', 'debate']))           # Sujet 12

# ---------------- EN TÊTE ----------------
add(1336, 1516, warn(
    "Au point 7, « en boîte noire » veut dire que le détecteur lit le transcript, pas les activations — le mot vient de la base, pas du billet : c'est le modèle lui-même, fine-tuné par LoRA à répondre à une question d'auto-rapport ; ce n'est pas une sonde, et ses chiffres ne se transfèrent pas aux sondes (fiche 7 ; fiches, partie B ; contre-lecture des fiches). Parade : pour une sonde, le test est causal, sur des types de mensonge tenus à part, à dégradation appariée (fiche 7).",
    "In item 7, \"black-box\" means the detector reads the transcript, not the activations — the word comes from the knowledge base, not from the post: it is the model itself, LoRA-fine-tuned to answer a self-report question; it is not a probe, and its numbers do not transfer to probes (reading sheet 7; reading sheets, part B; counter-reading of the sheets). Workaround: for a probe, the test is causal, on held-out lie types, at matched degradation (reading sheet 7)."))


# ---------------- Vérifications et écriture ----------------
def norm(s):
    return s.strip()


errs = []
ins = []
for lfr, len_, tfr, ten in ITEMS:
    for fi, ln, t in (('FR', lfr, tfr), ('EN', len_, ten)):
        a, b = TR[fi]
        assert a <= ln <= b, (fi, ln)
        anc = L[fi][ln - 1]
        if not norm(anc):
            errs.append(f'{fi} l.{ln} : ligne vide')
        n = sum(1 for i in range(a - 1, b) if norm(L[fi][i]) == norm(anc))
        if n != 1:
            errs.append(f'{fi} l.{ln} : ancre trouvée {n} fois')
        ins.append({'fichier': fi, 'ancre': anc, 'texte': t})

print('éléments :', len(ITEMS), '— insertions :', len(ins))
print('erreurs :', errs or 'aucune')
json.dump({'tranche': 'volets4_5_entete', 'insertions': ins}, open(OUT, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('écrit :', OUT)
