#!/usr/bin/env python3
"""Construit travail/insertions_tete_volet1.json : ancres lues par numéro de ligne dans la v3.5, textes ci-dessous."""
import json, os

W = '/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
SRC = {'FR': f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md', 'EN': f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md'}
TR = {'FR': (1, 181), 'EN': (1, 248)}
L = {k: open(v, encoding='utf8').read().split('\n') for k, v in SRC.items()}

# ---------------------------------------------------------------------------------------------
# Index des 27 encadrés (repris des renvois du référentiel), groupés par volet
IDX_FR = [
    "> ⚠ **Limites et parades** : contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; jeu tenu à part → volet M, M4 (après « Le jeu tenu à part ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*",
    "> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; J-lens et espace de travail → volet 2, C bis (après « Le test, tel qu'il se dit ») ; ablation et projection → volet 2, §D (après « La méthode ») ; crosscoders et comparaison de modèles → volet 2, §D (fin du cas d'application K64) *(v3.6)*",
    "> ⚠ **Limites et parades** : débat et supervision évolutive → volet 2, §E (après « En pratique — Debate ») ; élicitation non supervisée → volet 2, §E (fin du cas d'application K52) ; généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; classifieurs de sûreté → volet 2, §H (fin du cas d'application G1) ; désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») *(v3.6)*",
    "> ⚠ **Limites et parades** : dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity ; graphes d'attribution → volet 4, Circuit Tracing ; autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle ; auto-rapport et introspection → volet 5, partie II, A, sujet 13 ; juges LLM → volet 6, §2 (après « La loi de déplacement ») ; détecteurs fine-tunés → volet 7, F·29 ; patching → volet 10, fiche Patchscopes ; oracles d'activation → volet 10, fiche LatentQA ; chaîne de pensée comme moniteur → volet 11, réponse 43 *(v3.6)*",
]
IDX_EN = [
    "> ⚠ **Limits and workarounds**: random controls → Part M, M4 (after \"The matched-norm random direction\"); matched degradation and dose-response → Part M, M4 (after \"Dose-response\"); held-out set → Part M, M4 (after \"The held-out set\"); known case → Part M, M5 (end of section) *(v3.6)*",
    "> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after \"In practice — Auditing Hidden Objectives\"); behavioural evaluations and honeypots → Part 2, §B (after \"In practice — sandbagging\"); activation probes → Part 2, §C (after \"In practice — The Geometry of Truth\"); steering vectors → Part 2, §C (after \"In practice — Contrastive Activation Addition\"); J-lens and workspace → Part 2, C bis (after \"The test, as it is said\"); ablation and projection → Part 2, §D (after \"The method\"); crosscoders and model diffing → Part 2, §D (end of worked case K64) *(v3.6)*",
    "> ⚠ **Limits and workarounds**: debate and scalable oversight → Part 2, §E (after \"In practice — Debate\"); unsupervised elicitation → Part 2, §E (end of worked case K52); weak-to-strong generalization → Part 2, §F (after \"In practice — automation\"); control monitors → Part 2, §G (after \"In practice — coup probes\"); red-teaming → Part 2, §H (after \"In practice — StrongREJECT\"); safety classifiers → Part 2, §H (end of worked case G1); unlearning and re-elicitation → Part 2, §I (after \"In practice — unlearning put to the test\") *(v3.6)*",
    "> ⚠ **Limits and workarounds**: dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity; attribution graphs → Part 4, Circuit Tracing; natural-language autoencoders → Part 4, The recent wave on model cognition; self-report and introspection → Part 5, Section II, A, Topic 13; LLM judges → Part 6, §2 (after \"The displacement law\"); fine-tuned detectors → Part 7, F·29; patching → Part 10, Patchscopes sheet; activation oracles → Part 10, LatentQA sheet; chain of thought as a monitor → Part 11, answer 43 *(v3.6)*",
]

HEAD_FR = "\n".join([
    "> **v3.6 — 2 octobre 2026 : ce qui s'ajoute** *(v3.6)*",
    ">",
    "> Rien du texte de la v3.5 n'est retiré ni modifié : on ajoute, et chaque ajout porte la mention *(v3.6)*. Deux ajouts.",
    ">",
    "> - ★ **L'encadré du 2 octobre 2026 sur les sondes de désalignement** — pourquoi il faut un organisme modèle, J-lens compris ; comment entraîner les sondes ; le hors-distribution — est au volet 2, en trois morceaux : la partie 1 à la fin de la présentation de la section A (après « En pratique — Auditing Hidden Objectives », avant le cas d'application K71) ; les parties 2 et 3 à la fin de celle de la section C (après « En pratique — Contrastive Activation Addition (CAA) », avant le cas d'application K47) ; le J-lens au C bis (après « Le test, tel qu'il se dit », avant le cas d'application K72). Des renvois y mènent depuis le volet M, M5, et le volet 6, §8.",
    "> - ⚠ **Les limites de chaque instrument, et comment les contourner** : un encadré « Limites et parades » par instrument, à sa maison (index ci-dessous) ; ailleurs, un renvoi d'une ligne vers cet encadré, et un avertissement ponctuel là où un passage rapporte un résultat sans dire la limite de l'instrument qui l'a produit. Quand aucune parade n'est connue, l'encadré le dit. La règle, partout : une direction aléatoire de même norme n'est que le nul de spécificité ; le dommage ne s'écarte qu'à dégradation appariée ; un nul d'instrument ne compte qu'avec son cas connu (cours, volet M, M4 et M5).",
    ">",
    "> **Où sont les encadrés « Limites et parades »**, volet par volet :",
    ">",
    "\n>\n".join(IDX_FR),
])
HEAD_EN = "\n".join([
    "> **v3.6 — 2 October 2026: what is added** *(v3.6)*",
    ">",
    "> No text of v3.5 is removed or changed: things are only added, and every addition carries the mark *(v3.6)*. Two additions.",
    ">",
    "> - ★ **The box of 2 October 2026 on misalignment probes** — why a model organism is needed, J-lens included; how to train the probes; out of distribution — is in Part 2, in three pieces: part 1 at the end of the presentation of section A (after \"In practice — Auditing Hidden Objectives\", before the worked case K71); parts 2 and 3 at the end of that of section C (after \"In practice — Contrastive Activation Addition (CAA)\", before the worked case K47); the J-lens in C bis (after \"The test, as it is said\", before the worked case K72). Cross-references lead to it from Part M, M5, and Part 6, §8.",
    "> - ⚠ **The limits of each instrument, and how to work around them**: one \"Limits and workarounds\" box per instrument, at its home (index below); elsewhere, a one-line cross-reference to that box, and a spot warning wherever a passage reports a result without stating the limit of the instrument that produced it. When no workaround is known, the box says so. The rule, everywhere: a matched-norm random direction is only the specificity null; damage is ruled out only at matched degradation; an instrument's null counts only with its known case (course, Part M, M4 and M5).",
    ">",
    "> **Where the \"Limits and workarounds\" boxes are**, Part by Part:",
    ">",
    "\n>\n".join(IDX_EN),
])

# ---------------------------------------------------------------------------------------------
# (FR ligne, EN ligne, texte FR, texte EN)
INS = []

# 1. En-tête : la note v3.6 et l'index des encadrés
INS.append((1, 21, HEAD_FR, HEAD_EN))

# 2. En-tête : les sondes à 0,93-0,997
INS.append((3, 23,
 "> ⚠ *(v3.6)* Les sondes à 0,93-0,997 : le cours ne dit pas sur quel jeu ces scores sont mesurés, et un score de sonde en distribution ne dit rien de la généralisation — le chiffre qui compte est l'écart avec le score sur des types tenus à part (fiches, partie B, piège 1 ; fiche 7). Parade : ne les dire qu'avec leur jeu de mesure, tenir à part des familles entières, jamais des paraphrases (explication du 2 octobre, partie 3 ; fiche 7), et ne jamais les mettre dans la même phrase que les interventions sur Llama-3.1-8B (cours, volet 6, §2).",
 "> ⚠ *(v3.6)* The probes at 0.93-0.997: the course does not say on which set these scores were measured, and an in-distribution probe score says nothing about generalization — the number that matters is the gap with the score on held-out types (reading sheets, part B, trap 1; reading sheet 7). Workaround: state them only with their measurement set, hold out whole families, never paraphrases (explanation of 2 October, part 3; reading sheet 7), and never put them in the same sentence as the interventions on Llama-3.1-8B (course, Part 6, §2)."))

# 3. Volet 1, §2 : Alignment Faking (avertissement ponctuel, puis renvoi)
INS.append((74, 129,
 "> ⚠ *(v3.6)* Ce que le travail Alignment Faking mesure, c'est un écart de conformité entre le cas « entraîné » et le cas « non entraîné », dont le scratchpad donne le motif : l'indice est construit, et l'on ne sait pas trancher entre jeu de rôle et vraie préservation de buts (fiche 14). Parade : distinguer la conformité (14 %) de la conformité avec raisonnement explicite de faux alignement (12 %) (fiches, partie B, piège 7), et retirer l'indice lisible pour chercher quand même la préservation de buts (fiche 14) ; une réplication sur un modèle récent mesure peut-être la mémorisation du scénario, ses transcripts ayant été réinclus dans l'entraînement — contre cela, aucune parade connue ; on le dit (fiches, partie C ; fiche 14).",
 "> ⚠ *(v3.6)* What the Alignment Faking work measures is a compliance gap between the \"trained\" and the \"untrained\" case, whose motive the scratchpad gives: the cue is constructed, and role-play cannot be told apart from genuine goal preservation (reading sheet 14). Workaround: distinguish compliance (14%) from compliance with explicit alignment-faking reasoning (12%) (reading sheets, part B, trap 7), and remove the legible cue so as to look for goal preservation anyway (reading sheet 14); a replication on a recent model may measure memorization of the scenario, its transcripts having been re-included in training — against that, no workaround is known; say so (reading sheets, part C; reading sheet 14)."))
INS.append((74, 129,
 "> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; chaîne de pensée comme moniteur → volet 11, réponse 43 *(v3.6)*",
 "> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after \"In practice — sandbagging\"); chain of thought as a monitor → Part 11, answer 43 *(v3.6)*"))

# 4. Volet 1, §4 : la grammaire du champ (organisme, baseline, transfert)
INS.append((102, 154,
 "> ⚠ *(v3.6)* « On vérifie le transfert au réel » est le maillon que rien ne garantit : un succès sur un organisme construit borne l'instrument sans prouver le cas naturel, car une intention implantée est peut-être plus saillante qu'une naturelle — sur les sleeper agents, la meilleure de 1 000 directions aléatoires atteint déjà 95,3 % (passation, §5.2 ; fiche 15). Parade partielle : planter le même comportement par plusieurs recettes et lire la sonde sur une recette tenue à part, avec un comportement inoffensif planté de la même façon comme contrôle (cours, volet 2, §A, K71), ou deux familles d'organismes avec un témoin conscient mais honnête (cours, volet 6, §8) ; contre l'écart entre implanté et naturel lui-même, aucune parade connue ; on le dit (fiche 15 ; encadré du 2 octobre, partie 1).",
 "> ⚠ *(v3.6)* \"We check the transfer to the real thing\" is the link that nothing guarantees: a success on a constructed organism bounds the instrument without proving the natural case, because an implanted intention may be more salient than a natural one — on the sleeper agents, the best of 1,000 random directions already reaches 95.3% (handover, §5.2; reading sheet 15). Partial workaround: plant the same behaviour through several recipes and read the probe on a held-out recipe, with a harmless behaviour planted the same ways as a control (course, Part 2, §A, K71), or two organism families with an aware-but-honest control (course, Part 6, §8); against the gap between implanted and natural itself, no workaround is known; say so (reading sheet 15; box of 2 October, part 1)."))
INS.append((102, 154,
 "> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; cas connu → volet M, M5 (fin de section) ; contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; jeu tenu à part → volet M, M4 (après « Le jeu tenu à part ») *(v3.6)*",
 "> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after \"In practice — Auditing Hidden Objectives\"); known case → Part M, M5 (end of section); random controls → Part M, M4 (after \"The matched-norm random direction\"); matched degradation and dose-response → Part M, M4 (after \"Dose-response\"); held-out set → Part M, M4 (after \"The held-out set\") *(v3.6)*"))

# 5. Q2 : renvoi
INS.append((126, 183,
 "> ⚠ **Limites et parades** : débat et supervision évolutive → volet 2, §E (après « En pratique — Debate ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*",
 "> ⚠ **Limits and workarounds**: debate and scalable oversight → Part 2, §E (after \"In practice — Debate\"); activation probes → Part 2, §C (after \"In practice — The Geometry of Truth\") *(v3.6)*"))

# 6. Q4 : deux avertissements ponctuels, puis le renvoi
INS.append((136, 195,
 "> ⚠ *(v3.6)* Que le désalignement monte quand on neutralise « ceci est un test » n'est qu'un appui faible tant que le dommage n'est pas écarté : chaque direction pilotée dégrade la sortie, et des vecteurs de contrôle arbitraires font aussi monter le désalignement, plus faiblement (fiche 2 ; fiches, partie C). Parade : une direction aléatoire de même norme n'écarte que le nul de spécificité ; le dommage ne s'écarte qu'à dégradation appariée, par une courbe dose-réponse contre plusieurs témoins, avec un cas connu au même réglage (cours, volet M, M4 ; cours, volet 2, §C, K47).",
 "> ⚠ *(v3.6)* That misaligned behaviour rises when \"this is a test\" is neutralized is only weak support as long as damage has not been ruled out: every steered direction degrades the output, and arbitrary control vectors also raise misalignment, more weakly (reading sheet 2; reading sheets, part C). Workaround: a matched-norm random direction rules out only the specificity null; damage is ruled out only at matched degradation, by a dose-response curve against several controls, with a known case at the same setting (course, Part M, M4; course, Part 2, §C, K47)."))
INS.append((136, 195,
 "> ⚠ *(v3.6)* Si les détecteurs se taisent, cela ne prouve pas que le modèle ne feint pas : une sonde muette ne départage pas « pas d'intention » et « sonde aveugle » (passation, §5.2 ; fiches, partie B, piège 3). Parade : mesurer sensibilité et fausses alarmes sur un organisme où l'on a installé l'intention soi-même, et ne tirer du silence ailleurs qu'une borne (passation, §5.2) — c'est la partie 1 de l'encadré du 2 octobre, au volet 2 (fin de la présentation de la section A), dont la suite, entraîner les sondes et le hors-distribution, est à la fin de celle de la section C.",
 "> ⚠ *(v3.6)* If the detectors stay silent, that does not prove the model is not pretending: a silent probe does not separate \"no intention\" from \"blind probe\" (handover, §5.2; reading sheets, part B, trap 3). Workaround: measure sensitivity and false alarms on an organism in which you installed the intention yourself, and draw no more than a bound from silence elsewhere (handover, §5.2) — this is part 1 of the box of 2 October, in Part 2 (end of the presentation of section A), whose continuation, training the probes and out of distribution, is at the end of that of section C."))
INS.append((136, 195,
 "> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; cas connu → volet M, M5 (fin de section) ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») *(v3.6)*",
 "> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after \"In practice — The Geometry of Truth\"); model organisms → Part 2, §A (after \"In practice — Auditing Hidden Objectives\"); known case → Part M, M5 (end of section); behavioural evaluations and honeypots → Part 2, §B (after \"In practice — sandbagging\"); steering vectors → Part 2, §C (after \"In practice — Contrastive Activation Addition\"); matched degradation and dose-response → Part M, M4 (after \"Dose-response\") *(v3.6)*"))

# 7. Q5 : l'avertissement prêt (mot pour mot), un second sur le relais par les sondes, puis le renvoi
INS.append((140, 200,
 "> ⚠ *(v3.6)* Le raisonnement écrit peut aussi persuader le moniteur : un moniteur fondé sur la chaîne de pensée n'aurait signalé qu'environ 1 % des actions de Mythos 5, contre environ 50 % sans elle — un seul moniteur, un incident (fiche 3). Parade : juger ce que le modèle fait, pas ce qu'il en dit (passation, §5.1) ; encadré complet au volet 11, réponse 43.",
 "> ⚠ *(v3.6)* The written reasoning can also persuade the monitor: a chain-of-thought-based monitor would have flagged only about 1% of Mythos 5's actions, against about 50% without it — one monitor, one incident (reading sheet 3). Workaround: judge what the model does, not what it says about it (handover, §5.1); full box in Part 11, answer 43."))
INS.append((140, 200,
 "> ⚠ *(v3.6)* « La seconde prend le relais » suppose la sonde fiable là où la chaîne ne l'est pas : le silence d'une sonde en production n'est pas celui du modèle (cours, volet 3, §3, K70), et au seuil d'un moniteur, des sondes rappellent 43 % à 1 % de faux positifs, contre 55 % pour le meilleur moniteur LLM (cours, volet 7, F·51). Parade : des canaris — des positifs connus glissés dans le trafic —, un score de dérive et un échantillon frais jugé chaque mois (cours, volet 3, §3, K70), et un rappel rapporté à un seuil calibré à 1 % de faux positifs sur des variantes bénignes appariées (cours, volet 7, F·23).",
 "> ⚠ *(v3.6)* \"The second takes over\" assumes the probe is reliable where the chain is not: the silence of a probe in production is not the silence of the model (course, Part 3, §3, K70), and at a monitor's threshold, probes recall 43% at 1% false positives, against 55% for the best LLM monitor (course, Part 7, F·51). Workaround: canaries — known positives slipped into the traffic —, a drift score and a fresh sample judged every month (course, Part 3, §3, K70), and recall reported at a threshold calibrated at 1% false positives on matched benign variants (course, Part 7, F·23)."))
INS.append((140, 200,
 "> ⚠ **Limites et parades** : chaîne de pensée comme moniteur → volet 11, réponse 43 ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*",
 "> ⚠ **Limits and workarounds**: chain of thought as a monitor → Part 11, answer 43; activation probes → Part 2, §C (after \"In practice — The Geometry of Truth\"); control monitors → Part 2, §G (after \"In practice — coup probes\") *(v3.6)*"))

# 8. Q7 : seuil non franchi, élicitation, modèle qui se retient ; puis renvoi
INS.append((150, 212,
 "> ⚠ *(v3.6)* Un seuil non franchi est une borne, pas une absence : sans budget d'élicitation fixé d'avance et rapporté, « rien trouvé » dit seulement qu'on n'a pas assez cherché (cours, volet M, M7) ; et le Risk Report d'août concède des évaluations non tirées des vrais chemins de risque, sur des modèles probablement conscients d'être évalués (fiche 3). Parade : une élicitation à budget fixé d'avance, rapportée comme une borne (cours, volet M, M7 ; cours, volet 2, §B, K63) ; contre le modèle qui se retient, deux versions d'un environnement, tirées au hasard, qui ne diffèrent que par des indices de réalisme, avec un organisme dressé à se cacher comme cas connu (cours, volet 2, §B, K63).",
 "> ⚠ *(v3.6)* A threshold not crossed is a bound, not an absence: without an elicitation budget fixed in advance and reported, \"found nothing\" only says you did not search enough (course, Part M, M7); and the August Risk Report concedes evaluations not drawn from the real risk pathways, on models probably aware of being evaluated (reading sheet 3). Workaround: elicitation at a budget fixed in advance, reported as a bound (course, Part M, M7; course, Part 2, §B, K63); against a model that holds back, two versions of an environment, drawn at random, that differ only by realism cues, with an organism trained to hide as the known case (course, Part 2, §B, K63)."))
INS.append((150, 212,
 "> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*",
 "> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after \"In practice — sandbagging\"); red-teaming → Part 2, §H (after \"In practice — StrongREJECT\") *(v3.6)*"))

# 9. Q9 : la lecture, le nul de rang un, la prédiction du sous-espace ; puis renvoi
INS.append((160, 224,
 "> ⚠ *(v3.6)* La lecture « solide » repose, sur Llama, sur la seule lecture qui y soit mesurée, une corrélation de projection, ρ = 0,684, qui peut n'être qu'un ajustement ; les métriques de sonde, d'ajustement, ne sont pas rapportées (README du dépôt ; cours, volet 6, §2). Parade : scorer des items exclus de l'entraînement de la sonde, et extraire sur un jeu disjoint (README du dépôt) ; les sondes à 0,93-0,997 sont sur Qwen2.5-7B, un autre projet, jamais dans la même phrase que ce résultat (cours, volet 6, §2).",
 "> ⚠ *(v3.6)* The \"solid\" read-out rests, on Llama, on the only read-out measured there, a projection correlation, ρ = 0.684, which may be only training fit; the probe metrics, training fit, are not reported (repository README; course, Part 6, §2). Workaround: score items excluded from the probe's training, and extract on a disjoint set (repository README); the probes at 0.93-0.997 are on Qwen2.5-7B, another project, never in the same sentence as this result (course, Part 6, §2)."))
INS.append((160, 224,
 "> ⚠ *(v3.6)* « Plusieurs méthodes de rang un ont échoué » est un nul sans chiffres ni cas connu : leurs sorties brutes n'ont pas été conservées (README du dépôt), et un nul de pilotage peut venir d'un rang trop bas (fiche 7). Parade : avant de lire un nul, un cas connu au même réglage — un vecteur de pays, qui s'échange dans l'article sur l'espace de travail (cours, volet 2, §C, K47 ; cours, volet M, M5).",
 "> ⚠ *(v3.6)* \"Several rank-one methods failed\" is a null without numbers or a known case: their raw outputs were not preserved (repository README), and a steering null can come from too low a rank (reading sheet 7). Workaround: before reading a null, a known case at the same setting — a country vector, which swaps in the workspace paper (course, Part 2, §C, K47; course, Part M, M5)."))
INS.append((160, 224,
 "> ⚠ *(v3.6)* La prédiction du sous-espace n'a pas d'appui causal propre : la baisse du rang trois n'est pas revenue sur des générations fraîches, le sous-espace adoucit les verdicts négatifs sans encoder la déférence, et le contraste entre rangs vient d'expériences séparées, le seul balayage fait dans une même expérience n'étant pas monotone (README du dépôt ; cours, volet 6, §2). Parade : un balayage de rang dans une même expérience, sur des sous-espaces emboîtés, monotonie vérifiée et non supposée, à dégât égal, sur des générations fraîches gardées en texte complet, avec un bras sans pression (cours, volet 6, §6 ; cours, volet M, M4).",
 "> ⚠ *(v3.6)* The subspace prediction has no causal support of its own: the rank-three drop did not come back on fresh generations, the subspace softens negative verdicts without encoding deference, and the contrast between ranks comes from separate experiments, the only sweep done within one experiment not being monotonic (repository README; course, Part 6, §2). Workaround: a rank sweep within one experiment, on nested subspaces, monotonicity checked rather than assumed, at equal damage, on fresh generations kept as full text, with a no-pressure arm (course, Part 6, §6; course, Part M, M4)."))
INS.append((160, 224,
 "> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; ablation et projection → volet 2, §D (après « La méthode ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*",
 "> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after \"In practice — The Geometry of Truth\"); steering vectors → Part 2, §C (after \"In practice — Contrastive Activation Addition\"); ablation and projection → Part 2, §D (after \"The method\"); known case → Part M, M5 (end of section) *(v3.6)*"))

# 10. Q10 : les sondes ne sont pas indépendantes d'office ; puis renvoi
INS.append((166, 231,
 "> ⚠ *(v3.6)* Les sondes ne sont pas indépendantes d'office des méthodes comportementales : sur un modèle naturel, leur étiquette vient de la conduite, jugée après coup (explication du 2 octobre, partie 1, point 2) ; elles peuvent lire « je suis surveillé » au lieu de l'intention (cours, volet 6, §8) ; et itérer contre ses détecteurs sélectionne l'évasion (fiche 19). Parade : un organisme où l'intention est installée, qui fournit la vérité de terrain, deux familles d'organismes et un témoin conscient mais honnête (explication du 2 octobre, partie 1, point 2 ; cours, volet 6, §8), et des détecteurs scellés hors de la boucle — s'ils se déclenchent encore quand ceux de la boucle se taisent, l'évasion a été sélectionnée (fiche 19).",
 "> ⚠ *(v3.6)* Probes are not independent of behavioural methods by default: on a natural model, their label comes from conduct, judged after the fact (explanation of 2 October, part 1, item 2); they can read \"I am being watched\" instead of the intention (course, Part 6, §8); and iterating against one's detectors selects for evasion (reading sheet 19). Workaround: an organism in which the intention is installed, which provides the ground truth, two organism families and an aware-but-honest control (explanation of 2 October, part 1, item 2; course, Part 6, §8), and sealed detectors kept out of the loop — if they still fire when those in the loop have gone quiet, evasion has been selected (reading sheet 19)."))
INS.append((166, 231,
 "> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») *(v3.6)*",
 "> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after \"In practice — coup probes\"); activation probes → Part 2, §C (after \"In practice — The Geometry of Truth\"); behavioural evaluations and honeypots → Part 2, §B (after \"In practice — sandbagging\"); unlearning and re-elicitation → Part 2, §I (after \"In practice — unlearning put to the test\") *(v3.6)*"))

# 11. Q11 : la force de la red team ; puis renvoi (texte prêt du référentiel)
INS.append((172, 236,
 "> ⚠ *(v3.6)* Le résultat d'un jeu red team / blue team ne vaut que pour la red team supposée : un échafaudage d'attaque optimisé fait passer le score de sûreté de 0,87 à 0,41 (cours, volet 7, F·24), et sur Opus 4.6 la moitié de quarante attaques conçues à la main ne sont jamais attrapées par le moniteur (cours, volet 7, F·23). Parade : dire quelle red team le chiffre suppose — au moins une red team optimisée composante par composante —, un seuil calibré à 1 % de faux positifs sur des variantes bénignes appariées, un ensemble de prompts de moniteur spécialisés (cours, volet 7, F·24 et F·23) ; et une red team à budget fixé d'avance, dont le « rien trouvé » n'est qu'une borne (cours, volet M, M7).",
 "> ⚠ *(v3.6)* The result of a red team / blue team game holds only for the red team assumed: an optimized attack scaffold takes the safety score from 0.87 to 0.41 (course, Part 7, F·24), and on Opus 4.6 half of forty hand-designed attacks are never caught by the monitor (course, Part 7, F·23). Workaround: state which red team the number assumes — at least a red team optimized component by component —, a threshold calibrated at 1% false positives on matched benign variants, an ensemble of specialized monitor prompts (course, Part 7, F·24 and F·23); and a red team at a budget fixed in advance, whose \"found nothing\" is only a bound (course, Part M, M7)."))
INS.append((172, 236,
 "> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*",
 "> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after \"In practice — StrongREJECT\"); control monitors → Part 2, §G (after \"In practice — coup probes\") *(v3.6)*"))

# 12. Q12 : la vérité de terrain implantée ; puis renvoi
INS.append((178, 243,
 "> ⚠ *(v3.6)* La vérité de terrain implantée n'est pas parfaite : l'organisme conditionné à l'évaluation de la fiche 10 n'annote qu'environ 80 à 86 % du temps en évaluation, encore 34 % en déploiement simplement prompté, et ne distingue pas de façon fiable évaluation et déploiement à partir d'indices subtils (fiche 10). Parade : vérifier chaque copie par son comportement (cours, volet 2, §A, K71), et tenir pour vérité de terrain la règle et ses indices, l'étiquette de chaque entrée se vérifiant encore par la conduite (encadré du 2 octobre, partie 1, point 2 : volet 2, fin de la présentation de la section A).",
 "> ⚠ *(v3.6)* Implanted ground truth is not perfect: the evaluation-conditioned organism of reading sheet 10 annotates only about 80 to 86% of the time in evaluation, still 34% in merely prompted deployment, and does not reliably tell evaluation from deployment from subtle cues (reading sheet 10). Workaround: check each copy by its behaviour (course, Part 2, §A, K71), and take as ground truth the rule and its cues, the label of each input still being checked by conduct (box of 2 October, part 1, item 2: Part 2, end of the presentation of section A)."))
INS.append((178, 243,
 "> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*",
 "> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after \"In practice — Auditing Hidden Objectives\"); known case → Part M, M5 (end of section) *(v3.6)*"))

# ---------------------------------------------------------------------------------------------
out = []
for fr_n, en_n, tfr, ten in INS:
    for fi, n, t in (('FR', fr_n, tfr), ('EN', en_n, ten)):
        a, b = TR[fi]
        assert a <= n <= b, (fi, n)
        ancre = L[fi][n - 1]
        k = sum(1 for i in range(a - 1, b) if L[fi][i].strip() == ancre.strip())
        assert k == 1, (fi, n, k)
        out.append({'fichier': fi, 'ancre': ancre, 'texte': t})

dst = f'{W}/travail/insertions_tete_volet1.json'
json.dump({'tranche': 'tete_volet1', 'insertions': out}, open(dst, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(out), 'insertions écrites dans', dst)
