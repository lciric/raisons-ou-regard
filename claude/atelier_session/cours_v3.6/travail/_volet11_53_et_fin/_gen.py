#!/usr/bin/env python3
"""Génère travail/insertions_volet11_53_et_fin.json (tranche : volet 11, réponses 53 et suivantes, angles morts, brainstorm).

Les ancres sont lues par numéro de ligne dans la v3.5 (donc recopiées telles quelles), puis vérifiées uniques dans la tranche.
"""
import json, os, re, sys

W = '/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
SRC = {'FR': f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md', 'EN': f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md'}
TR = {'FR': (4730, 5377), 'EN': (5038, 5702)}
OUT = f'{W}/travail/insertions_volet11_53_et_fin.json'
L = {k: open(v, encoding='utf8').read().split('\n') for k, v in SRC.items()}

# ---------------------------------------------------------------- renvois : morceaux prêts (référentiel, partie 2)
RF = {
    'alea': "contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme »)",
    'degr': "dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse »)",
    'part': "jeu tenu à part → volet M, M4 (après « Le jeu tenu à part »)",
    'cas': "cas connu → volet M, M5 (fin de section)",
    'orga': "organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives »)",
    'eval': "évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging »)",
    'sond': "sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth »)",
    'pilo': "pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition »)",
    'pilop': "pilotage par vecteurs, dont vecteurs de persona → volet 2, §C (après « En pratique — Contrastive Activation Addition »)",
    'jlen': "J-lens et espace de travail → volet 2, C bis (après « Le test, tel qu'il se dit »)",
    'abla': "ablation et projection → volet 2, §D (après « La méthode »)",
    'deba': "débat et supervision évolutive → volet 2, §E (après « En pratique — Debate »)",
    'w2s': "généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation »)",
    'moni': "moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes »)",
    'red': "red-teaming → volet 2, §H (après « En pratique — StrongREJECT »)",
    'clas': "classifieurs de sûreté → volet 2, §H (fin du cas d'application G1)",
    'unle': "désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve »)",
    'sae': "dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity",
    'graf': "graphes d'attribution → volet 4, Circuit Tracing",
    'nla': "autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle",
    'auto': "auto-rapport et introspection → volet 5, partie II, A, sujet 13",
    'juge': "juges LLM → volet 6, §2 (après « La loi de déplacement »)",
    'dete': "détecteurs fine-tunés → volet 7, F·29",
    'patc': "patching → volet 10, fiche Patchscopes",
    'cot': "chaîne de pensée comme moniteur → volet 11, réponse 43",
    'cotv': "chaîne de pensée comme moniteur, et conscience verbalisée → volet 11, réponse 43",
    'box': "sondes de désalignement, J-lens compris (encadré du 2 octobre) → volet 2, §A (avant le cas d'application K71), §C (avant le cas d'application K47) et C bis (avant le cas d'application K72)",
}
RE = {
    'alea': 'random controls → Part M, M4 (after "The matched-norm random direction")',
    'degr': 'matched degradation and dose-response → Part M, M4 (after "Dose-response")',
    'part': 'held-out set → Part M, M4 (after "The held-out set")',
    'cas': 'known case → Part M, M5 (end of section)',
    'orga': 'model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives")',
    'eval': 'behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging")',
    'sond': 'activation probes → Part 2, §C (after "In practice — The Geometry of Truth")',
    'pilo': 'steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition")',
    'pilop': 'steering vectors, including persona vectors → Part 2, §C (after "In practice — Contrastive Activation Addition")',
    'jlen': 'J-lens and workspace → Part 2, C bis (after "The test, as it is said")',
    'abla': 'ablation and projection → Part 2, §D (after "The method")',
    'deba': 'debate and scalable oversight → Part 2, §E (after "In practice — Debate")',
    'w2s': 'weak-to-strong generalization → Part 2, §F (after "In practice — automation")',
    'moni': 'control monitors → Part 2, §G (after "In practice — coup probes")',
    'red': 'red-teaming → Part 2, §H (after "In practice — StrongREJECT")',
    'clas': 'safety classifiers → Part 2, §H (end of worked case G1)',
    'unle': 'unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test")',
    'sae': 'dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity',
    'graf': 'attribution graphs → Part 4, Circuit Tracing',
    'nla': 'natural-language autoencoders → Part 4, The recent wave on model cognition',
    'auto': 'self-report and introspection → Part 5, Section II, A, Topic 13',
    'juge': 'LLM judges → Part 6, §2 (after "The displacement law")',
    'dete': 'fine-tuned detectors → Part 7, F·29',
    'patc': 'patching → Part 10, Patchscopes sheet',
    'cot': 'chain of thought as a monitor → Part 11, answer 43',
    'cotv': 'chain of thought as a monitor, and verbalized awareness → Part 11, answer 43',
    'box': 'misalignment probes, J-lens included (box of 2 October) → Part 2, §A (before the worked case K71), §C (before the worked case K47) and C bis (before the worked case K72)',
}


def renvoi(keys):
    fr = "> ⚠ **Limites et parades** : " + " ; ".join(RF[k] for k in keys) + " *(v3.6)*"
    en = "> ⚠ **Limits and workarounds**: " + "; ".join(RE[k] for k in keys) + " *(v3.6)*"
    return fr, en


def av(fr, en):
    return "> ⚠ *(v3.6)* " + fr, "> ⚠ *(v3.6)* " + en


# ---------------------------------------------------------------- les insertions, section par section
# chaque entrée : (section, ligne FR v3.5, ligne EN v3.5, texte FR, texte EN)
S = []


def add(section, lfr, len_, pair):
    S.append((section, lfr, len_, pair[0], pair[1]))


# ===== 55 · « Why could a very capable system be dangerous… » — fin de la réponse
add('55', 4774, 5083, av(
    "Ce résultat lit le motif dans un scratchpad caché, donné avec la consigne de raisonner sur sa situation, sur un indice construit (gratuit contre payant) : on ne sait pas y trancher entre jeu de rôle et vraie préservation de buts, et le RL qui fait monter ce raisonnement fait aussi monter la conformité hors surveillance, sans que le papier fasse de ce raisonnement la cause de la conformité (fiche 14 ; fiches, partie C ; fiches, partie B, piège 2). Parade : s'appuyer sur la mesure, l'écart de conformité entre le cas « entraîné » et le cas « non entraîné », et retirer l'indice lisible pour chercher quand même la préservation de buts (fiche 14) ; qu'une réplication sur un modèle récent ne mesure que la mémorisation du scénario, ses transcripts ayant été réinclus dans l'entraînement, aucune parade connue ne l'écarte ; on le dit (fiches, partie C).",
    "This result reads the motive in a hidden scratchpad, given with the instruction to reason about its situation, on a constructed cue (free versus paid): role-play cannot be told apart there from genuine goal preservation, and the RL that raises this reasoning also raises compliance when unmonitored, without the paper making this reasoning the cause of compliance (reading sheet 14; reading sheets, part C; reading sheets, part B, trap 2). Workaround: rest on the measurement, the compliance gap between the \"trained\" and the \"not trained\" case, and remove the legible cue to look for goal preservation anyway (reading sheet 14); that a replication on a recent model measures only memorization of the scenario, its transcripts having been re-included in training, no known workaround rules out; say so (reading sheets, part C)."))
add('55', 4774, 5083, renvoi(['eval', 'cot', 'orga']))

# ===== 56 · « How would you know a model is faking alignment? » — fin de la réponse
add('56', 4789, 5099, av(
    "Des vecteurs aléatoires en contrôle n'écartent que « n'importe quelle poussée de cette taille fait autant » — le nul de spécificité ; le dommage ne s'écarte qu'à dégradation appariée (cours, volet M, M4) ; et dans la lignée des cartes système, l'effet est modeste et dépend du jeu de données, des vecteurs de contrôle arbitraires bougent le comportement dans le même sens, chaque direction dégrade les sorties, et Opus 4.6 ne trouvait pas de différence notable avec des contrôles aléatoires sur la tromperie et la complaisance (fiche 2 ; contre-lecture des fiches). Parade : un sous-espace contre des sous-espaces aléatoires de même rang, à dégradation appariée, plus une baseline de prompt et une courbe dose-réponse contre plusieurs témoins (fiche 2 ; cours, volet 2, §C, K47 ; programme, partie 3).",
    "Random control vectors rule out only \"any push of that size does as much\" — the specificity null; damage is ruled out only at matched degradation (course, Part M, M4); and across the system-card lineage, the effect is modest and dataset-dependent, arbitrary control vectors move behaviour in the same direction, every direction degrades the outputs, and Opus 4.6 found no notable difference from random controls on deception and sycophancy (reading sheet 2; counter-reading of the sheets). Workaround: a subspace against random subspaces of the same rank, at matched degradation, plus a prompt baseline and a dose-response curve against several controls (reading sheet 2; course, Part 2, §C, K47; programme, part 3)."))
add('56', 4789, 5099, av(
    "Ces détecteurs de mensonge ne sont pas des sondes : ce sont des modèles fine-tunés par LoRA pour répondre à une question d'auto-rapport sur un transcript ; et 0,95 est une progression en distribution pendant l'entraînement, le plateau d'une catégorie à l'autre étant de 0,70 à 0,75, à peine mieux qu'un simple prompt (fiche 7 ; explication du 2 octobre, partie 2). Parade : ne pas transférer leurs chiffres aux sondes ; pour une sonde, mesurer l'écart entre l'AUROC en distribution et celle de familles entières tenues à part, puis faire le test causal à dégradation appariée, avec un cas connu au même réglage (fiche 7 ; explication du 2 octobre, partie 3).",
    "These lie detectors are not probes: they are models fine-tuned with LoRA to answer a self-report question about a transcript; and 0.95 is an in-distribution progression during training, the cross-category plateau being 0.70 to 0.75, barely better than a simple prompt (reading sheet 7; explanation of 2 October, part 2). Workaround: do not transfer their numbers to probes; for a probe, measure the gap between the in-distribution AUROC and the AUROC on whole held-out families, then run the causal test at matched degradation, with a known case at the same setting (reading sheet 7; explanation of 2 October, part 3)."))
add('56', 4789, 5099, av(
    "Ce chiffre de partition n'a pas été mesuré à dégradation égale — « un chiffre à refaire à dégradation égale » (cours, volet 11, réponse A4) —, un aléatoire apparié en covariance y fait davantage que la direction de la sonde (cours, volet 6, §2 et §3), et la seule lecture mesurée sur Llama est une corrélation peut-être d'ajustement (README du dépôt). Parade : le protocole de la réponse A4 — une intervention sur la direction lue, une sur l'état complet aux mêmes endroits, des directions témoins comparées à dégradation égale —, le patch de l'état complet servant de plafond, et la lecture scorée sur des items exclus de l'entraînement de la sonde (cours, volet 11, réponse A4 ; programme, partie 8 ; README du dépôt).",
    "This partition number was not measured at equal degradation — \"a number to redo at equal degradation\" (course, Part 11, answer A4) —, a covariance-matched random direction does more there than the probe direction (course, Part 6, §2 and §3), and the only read-out measured on Llama is a correlation that may be training fit (repository README). Workaround: the protocol of answer A4 — one intervention on the read direction, one on the full state at the same sites, control directions compared at equal degradation —, with the full-state patch as the ceiling, and the read-out scored on items excluded from the probe's training (course, Part 11, answer A4; programme, part 8; repository README)."))
add('56', 4789, 5099, renvoi(['orga', 'eval', 'pilo', 'alea', 'sond', 'dete', 'patc', 'cas', 'box']))

# ===== 58 · « RLHF, DPO, Constitutional AI… » — fin de la réponse
add('58', 4807, 5117, renvoi(['juge', 'eval', 'deba']))

# ===== 60 · « Defense in depth… » — fin de la réponse
add('60', 4834, 5145, av(
    "Le gain hors distribution du midtraining de spécification est lu sur des modèles ouverts, sur un banc agentique dont le modèle peut reconnaître les scènes comme des tests — la limite que sa fiche pose elle-même (cours, volet 7, F·34). Parade : deux versions de l'environnement, tirées au hasard, qui ne diffèrent que par des indices de réalisme notés par un discriminateur, avec un organisme dressé à se cacher comme cas connu (cours, volet 2, §B, K63) ; qu'un banc tenu à part représente le réel, aucune parade connue ne le garantit ; on le dit (fiche 12).",
    "The out-of-distribution gain of spec midtraining is read on open models, on an agentic benchmark whose scenes the model can recognize as tests — the limit its own sheet sets (course, Part 7, F·34). Workaround: two versions of the environment, randomly assigned, differing only in realism cues scored by a discriminator, with an organism trained to hide as the known case (course, Part 2, §B, K63); that a held-out benchmark represents the real case, no known workaround guarantees; say so (reading sheet 12)."))
add('60', 4834, 5145, av(
    "Le résultat d'inhibition cité a la même limite qu'à la réponse 56 — des vecteurs de contrôle arbitraires font aussi monter le désalignement, plus faiblement, et un contrôle de même norme n'est que le nul de spécificité (fiche 2 ; cours, volet M, M4) — ; et la couche interne n'est pas indépendante de la façade par construction : une sonde peut lire « je suis surveillé » et le contexte de test au lieu de l'intention, et tomber alors au même endroit que l'évaluation (cours, volet 6, §8 ; cours, volet 3, §4, K67). Parade : des sous-espaces aléatoires de même rang à dégradation appariée pour l'inhibition, et, pour la sonde, des transcripts honnêtes rédigés comme des tests et un organisme conscient mais honnête, sur lesquels elle doit rester à sa ligne de base (cours, volet M, M4 ; cours, volet 3, §4, K67 ; cours, volet 6, §8).",
    "The inhibition result cited has the same limit as at answer 56 — arbitrary control vectors also raise misalignment, more weakly, and a matched-norm control is only the specificity null (reading sheet 2; course, Part M, M4) —; and the internal layer is not independent of the façade by construction: a probe can read \"I am being watched\" and the test context instead of the intention, and then fail at the same place as the evaluation (course, Part 6, §8; course, Part 3, §4, K67). Workaround: random subspaces of the same rank at matched degradation for the inhibition, and, for the probe, honest transcripts written as tests and an aware-but-honest organism, on which it must stay at its baseline (course, Part M, M4; course, Part 3, §4, K67; course, Part 6, §8)."))
add('60', 4834, 5145, renvoi(['moni', 'eval', 'sond', 'pilo', 'part']))

# ===== 61 · « How would you red-team a model? » — fin de la réponse
add('61', 4848, 5160, av(
    "Les quarante attaques du banc des angles morts sont conçues à la main, en transcriptions synthétiques dont le réalisme reste ouvert : le banc dit si le moniteur voit une attaque écrite par des humains, pas si un modèle la produirait (cours, volet 7, F·23 ; cours, volet 11, réponse B14) ; et le réalisme par paires se mesure par un juge LLM, alors que la conscience d'évaluation liée à la tâche persiste (cours, volet 7, F·25). Parade : rejouer les attaques comme des tâches que le modèle doit faire dans un vrai harnais, au seuil calibré sur des variantes bénignes appariées (cours, volet 11, réponse B14 ; cours, volet 7, F·23) ; pour le réalisme des transcriptions synthétiques, aucune parade connue ; on le dit (cours, volet 7, F·23).",
    "The blind-spot benchmark's forty attacks are hand-designed, as synthetic transcripts whose realism remains open: the benchmark says whether the monitor sees an attack written by humans, not whether a model would produce it (course, Part 7, F·23; course, Part 11, answer B14); and paired realism is measured by an LLM judge, while task-driven evaluation awareness persists (course, Part 7, F·25). Workaround: replay the attacks as tasks the model must do in a real harness, at the threshold calibrated on paired benign variants (course, Part 11, answer B14; course, Part 7, F·23); for the realism of the synthetic transcripts, no workaround is known; say so (course, Part 7, F·23)."))
add('61', 4848, 5160, renvoi(['red', 'moni', 'clas', 'eval', 'juge']))

# ===== 62 · « Is alignment actually hard? » — fin de la réponse
add('62', 4860, 5173, av(
    "« Ne généraliseraient jamais » serait un nul d'instrument : il ne compte qu'avec un cas connu où la même sonde, au même réglage, attrape hors distribution une intention qu'on a installée — sinon l'échec dit peut-être seulement que la sonde est aveugle (cours, volet M, M5 ; passation, §5.2). Parade : juger la sonde sur des familles entières tenues à part, jusqu'à l'agentique à plusieurs tours, avec un organisme où l'on a installé l'intention, et dire le résultat comme une borne, jamais comme une absence (explication du 2 octobre, parties 1 et 3 ; programme, partie 3 ; cours, volet M, M5).",
    "\"Never generalise\" would be an instrument null: it counts only with a known case in which the same probe, at the same setting, catches out of distribution an intention that was installed — otherwise the failure may only say that the probe is blind (course, Part M, M5; handover, §5.2). Workaround: judge the probe on whole held-out families, up to multi-turn agentic settings, with an organism in which the intention was installed, and state the result as a bound, never as an absence (explanation of 2 October, parts 1 and 3; programme, part 3; course, Part M, M5)."))
add('62', 4860, 5173, renvoi(['sond', 'cas', 'part', 'box']))

# ===== 63 · Tes huit positions — après la position 2, après la position 4, et en fin de section
add('63', 4877, 5192, av(
    "Note d'étude, sans rien changer à la position : ce « moins d'un pour cent » n'a pas encore été mesuré à dégradation égale, et un aléatoire apparié en covariance y fait davantage que la direction de la sonde (cours, volet 11, réponse A4 ; cours, volet 6, §2 et §3). Parade : le refaire par le protocole de la réponse A4, avec des directions témoins comparées à dégradation égale et le patch de l'état complet comme plafond (cours, volet 11, réponse A4 ; programme, partie 8).",
    "Study note, changing nothing in the position: this \"under one percent\" has not yet been measured at equal degradation, and a covariance-matched random direction does more there than the probe direction (course, Part 11, answer A4; course, Part 6, §2 and §3). Workaround: redo it with the protocol of answer A4, with control directions compared at equal degradation and the full-state patch as the ceiling (course, Part 11, answer A4; programme, part 8)."))
add('63', 4885, 5200, av(
    "Deux réserves à garder sous la position : la lisibilité elle-même ne se prouve pas en distribution — une AUROC en distribution ne prouve rien, c'est l'écart avec des familles tenues à part qui se mesure (fiches, partie B, piège 1 ; fiche 7) — ; et une intervention qui échoue ne réfute la causalité qu'avec un cas connu au même réglage, sinon le nul peut venir d'un rang trop bas (fiche 7 ; cours, volet M, M5). Parade : des familles entières tenues à part, jamais des paraphrases, et un cas connu au même rang, à la même dose et au même seuil que la mesure (explication du 2 octobre, partie 3 ; cours, volet M, M5 ; fiche 7).",
    "Two caveats to keep under the position: readability itself is not proven in distribution — an in-distribution AUROC proves nothing, what is measured is the gap with held-out families (reading sheets, part B, trap 1; reading sheet 7) —; and a failed intervention refutes causation only with a known case at the same setting, otherwise the null may come from too low a rank (reading sheet 7; course, Part M, M5). Workaround: whole held-out families, never paraphrases, and a known case at the same rank, dose and threshold as the measurement (explanation of 2 October, part 3; course, Part M, M5; reading sheet 7)."))
add('63', 4898, 5213, renvoi(['sond', 'alea', 'degr', 'cas', 'patc', 'eval']))

# ===== A1 · « Which team would you want to join… » — fin de la réponse
add('A1', 4921, 5235, renvoi(['sond', 'moni', 'patc', 'abla', 'sae']))

# ===== A2 · « You have $15,000 of compute a month… » — fin de la réponse
add('A2', 4936, 5251, av(
    "Des sondes entraînées hors politique sur des exemples écrits peuvent n'apprendre qu'un indice de surface, ou lire le texte plutôt qu'une représentation (cours, volet 2, §C ; programme, partie 8) ; et réussir le test à deux familles ferme l'écart entre deux façons d'implanter, pas celui entre l'implanté et le naturel : une intention implantée est peut-être plus saillante (cours, volet 6, §8 ; passation, §5.2 ; fiche 15). Parade : tirer les négatifs des générations réelles du modèle, lire au premier jeton avant toute raison écrite ou au jeton d'action avec des raisons neutres préremplies, et ajouter l'organisme d'une autre équipe (cours, volet 2, §C ; programme, parties 3 et 8 ; cours, volet 2, §A, K71) ; contre l'écart entre l'implanté et le naturel lui-même, aucune parade connue ; on le dit (explication du 2 octobre, partie 1 ; cours, volet M, M5).",
    "Probes trained off-policy on written examples may learn only a surface cue, or read the text rather than a representation (course, Part 2, §C; programme, part 8); and passing the two-family test closes the gap between two ways of implanting, not the one between implanted and natural: an implanted intention may be more salient (course, Part 6, §8; handover, §5.2; reading sheet 15). Workaround: draw negatives from the model's real generations, read at the first token before any written reason or at the action token with neutral reasons prefilled, and add another team's organism (course, Part 2, §C; programme, parts 3 and 8; course, Part 2, §A, K71); against the gap between implanted and natural itself, no workaround is known; say so (explanation of 2 October, part 1; course, Part M, M5)."))
add('A2', 4936, 5251, renvoi(['orga', 'sond', 'moni', 'red', 'cas', 'box']))

# ===== A3 · « What if the probes just don't work at all… » — fin de la réponse
add('A3', 4948, 5264, av(
    "L'échec sur la famille « adaptateur léger » ne se lit « une sonde lit le mécanisme d'induction » qu'avec deux cas connus : l'implant de cette famille a pris, vérifié copie par copie par son comportement, et la sonde, au même seuil, attrape des cas tenus à part de la famille qu'elle réussit ; sinon le nul dit peut-être un implant raté ou un seuil trop strict (cours, volet 2, §A, K71 ; cours, volet 2, §E, K52 ; cours, volet M, M5). Parade : ces deux vérifications avant de conclure, et un comportement inoffensif planté par les deux mêmes recettes, qui écarte une sonde lisant la recette (cours, volet 2, §A, K71).",
    "The failure on the \"light adapter\" family reads as \"a probe reads the induction mechanism\" only with two known cases: the implant of that family took, checked copy by copy through its behaviour, and the probe, at the same threshold, catches held-out cases of the family it passes; otherwise the null may only say a failed implant or too strict a threshold (course, Part 2, §A, K71; course, Part 2, §E, K52; course, Part M, M5). Workaround: those two checks before concluding, and a harmless behaviour planted through the same two recipes, which rules out a probe reading the recipe (course, Part 2, §A, K71)."))
add('A3', 4948, 5264, av(
    "Les détecteurs de mensonge cités ne sont pas des sondes — des modèles fine-tunés par LoRA pour répondre à une question d'auto-rapport sur un transcript —, et 0,95 est une progression en distribution pendant l'entraînement (fiche 7 ; explication du 2 octobre, partie 2) : leur destin ne se transfère pas tel quel aux sondes. Parade : pour une sonde, l'écart entre l'AUROC en distribution et celle de familles entières tenues à part, puis le test causal à dégradation appariée (fiche 7 ; explication du 2 octobre, partie 3).",
    "The lie detectors cited are not probes — models fine-tuned with LoRA to answer a self-report question about a transcript —, and 0.95 is an in-distribution progression during training (reading sheet 7; explanation of 2 October, part 2): their fate does not transfer as such to probes. Workaround: for a probe, the gap between the in-distribution AUROC and the AUROC on whole held-out families, then the causal test at matched degradation (reading sheet 7; explanation of 2 October, part 3)."))
add('A3', 4948, 5264, renvoi(['cas', 'sond', 'orga', 'dete', 'patc', 'box']))

# ===== A4 · « Your rank-three result is on an 8B model… » — fin de la réponse
add('A4', 4962, 5280, av(
    "La charge se lit au J-lens, qui n'a été montré que sur Claude et ne lit que des concepts d'un seul token, et « charge » désigne trois grandeurs selon les textes (fiche 1 ; cours, volet 2, C bis ; cours, volet 6, §6). Parade : sur chaque modèle ouvert, une porte — reproduire d'abord l'échange d'un concept d'un seul token, sinon un tuned lens déclaré comme approximation, la thèse n'étant alors pas testée au sens de l'article —, la charge d'un concept de plusieurs tokens lue sur un jeu de tokens, et le prédicteur principal gelé d'abord, en disant lequel (programme, parties 3 et 8 ; cours, volet 6, §6).",
    "Loading is read with the J-lens, which has been shown only on Claude and reads only single-token concepts, and \"loading\" names three quantities depending on the text (reading sheet 1; course, Part 2, C bis; course, Part 6, §6). Workaround: on each open model, a gate — first reproduce the swap of a single-token concept, otherwise a tuned lens declared as an approximation, the thesis then not being tested in the paper's sense —, the loading of a multi-token concept read on a token set, and the main predictor frozen first, saying which (programme, parts 3 and 8; course, Part 6, §6)."))
add('A4', 4962, 5280, renvoi(['abla', 'jlen', 'degr', 'patc']))

# ===== A5 · « Isn't sycophancy basically solved by now… » — fin de la réponse
add('A5', 4975, 5294, av(
    "« Indiscernable de zéro » est un nul : il ne compte que si le même dispositif — mêmes cadrages, même régression — voit le déplacement là où il existe, chez le juge que tu as mesuré, et il se dit comme une borne, avec son budget et sa puissance, jamais comme une absence (cours, volet M, M5) ; et l'écart entre modèles et chercheurs sur les propositions de recherche repose sur dix chercheurs et 92 paires (cours, volet 7, F·41). Parade : ce cas connu dans le même protocole avant de déclarer un juge « résolu », et l'écart sur les propositions dit avec la taille de son échantillon (cours, volet M, M5 ; cours, volet 7, F·41).",
    "\"Indistinguishable from zero\" is a null: it counts only if the same setup — same framings, same regression — sees the displacement where it exists, in the judge you measured, and it is stated as a bound, with its budget and power, never as an absence (course, Part M, M5); and the gap between models and researchers on research proposals rests on ten researchers and 92 pairs (course, Part 7, F·41). Workaround: that known case in the same protocol before declaring a judge \"solved\", and the proposal gap stated with its sample size (course, Part M, M5; course, Part 7, F·41)."))
add('A5', 4975, 5294, renvoi(['juge', 'cas', 'eval']))

# ===== A6 · « Suppose a probe flags an agent mid-trajectory… » — fin de la réponse
add('A6', 4989, 5309, av(
    "La garantie borne les fausses alarmes, pas les ratés : une sonde en production peut échouer en silence, et son silence n'est pas celui du modèle (cours, volet 3, §3, K70) ; et le test séquentiel toujours valide existe déjà sur des scores de vérificateur boîte noire, ce qui reste étant le même test sur des scores internes (cours, volet 7, F·55). Parade : des canaris — des positifs connus glissés dans le trafic —, un score de dérive et un échantillon frais jugé chaque mois (cours, volet 3, §3, K70) ; et, pour cette combinaison, dire « I haven't seen that combination measured », jamais « first » ni « mine » (cours, volet 7, F·52 et F·55).",
    "The guarantee bounds false alarms, not misses: a probe in production can fail silently, and its silence is not the model's (course, Part 3, §3, K70); and the always-valid sequential test already exists on black-box verifier scores, what remains being the same test on internal scores (course, Part 7, F·55). Workaround: canaries — known positives slipped into the traffic —, a drift score and a fresh sample judged every month (course, Part 3, §3, K70); and, for that combination, say \"I haven't seen that combination measured\", never \"first\" nor \"mine\" (course, Part 7, F·52 and F·55)."))
add('A6', 4989, 5309, renvoi(['moni', 'sond']))

# ===== A7 · « A colleague shows you a beautiful steering result… » — fin de la réponse
add('A7', 5001, 5323, av(
    "Les trois questions s'appliquent d'abord à ton propre chiffre : ce « moins d'un pour cent contre soixante-huit » n'a pas encore été mesuré à dégradation égale, et un aléatoire apparié en covariance y fait davantage que la direction de la sonde (cours, volet 11, réponse A4 ; cours, volet 6, §2 et §3). Parade : le protocole de la réponse A4, avec des directions témoins comparées à dégradation égale et le patch de l'état complet comme plafond (cours, volet 11, réponse A4 ; programme, partie 8).",
    "The three questions apply first to your own number: this \"under one percent against sixty-eight\" has not yet been measured at equal degradation, and a covariance-matched random direction does more there than the probe direction (course, Part 11, answer A4; course, Part 6, §2 and §3). Workaround: the protocol of answer A4, with control directions compared at equal degradation and the full-state patch as the ceiling (course, Part 11, answer A4; programme, part 8)."))
add('A7', 5001, 5323, renvoi(['alea', 'degr', 'patc', 'pilo', 'abla']))

# ===== A8 · « How do you think about the dual-use of your own work… » — fin de la réponse
add('A8', 5014, 5337, av(
    "« Pas contournable » ne dit rien de ce que fait un entraînement : selon un rapport, après un RL, des sondes neuves hors domaine se dégradent alors qu'une sonde neuve dans le domaine reste quasi parfaite (rapport d'antériorité 3 du 2 octobre, *The Obfuscation Atlas* — rapport, lu de façon ciblée), et itérer contre ses détecteurs sélectionne l'évasion (fiche 19). Parade : une sonde neuve après tout entraînement, sur un jeu d'indices disjoint, et des détecteurs scellés hors de la boucle — s'ils se déclenchent encore quand ceux de la boucle se taisent, l'évasion a été sélectionnée (passation, §5.2 ; programme, partie 3 ; fiche 19).",
    "\"Can't be evaded\" says nothing about what training does: according to a report, after RL, fresh out-of-domain probes degrade while a fresh in-domain probe stays near perfect (prior-art report 3 of 2 October, *The Obfuscation Atlas* — report, read in a targeted way), and iterating against your detectors selects for evasion (reading sheet 19). Workaround: a fresh probe after any training, on a disjoint cue set, and sealed detectors outside the loop — if they still fire when the in-loop ones go quiet, evasion has been selected (handover, §5.2; programme, part 3; reading sheet 19)."))
add('A8', 5014, 5337, renvoi(['sond', 'moni', 'orga', 'box']))

# ===== A9 à A17 — après A10, après A16, puis renvoi en fin de section (après A17)
add('A9-A17', 5030, 5355, av(
    "Deux limites pour A10 : le sous-espace de rang trois déplaçait la valence, pas le concept, et son effet n'est pas revenu sur des générations fraîches — ce n'est pas une prise causale sur la complaisance, et le décomposer en features ne dirait pas ce qui la porte (cours, volet 6, §2 ; README du dépôt) ; et le dictionnaire épars ouvert pour ce modèle laisse la plus grande part de la variance dans son résidu, qui porte le signal lu (README du dépôt). Parade : le témoin sans pression et la direction d'un concept rival, à dégradation appariée, avant de décomposer, et le signal lu sur la reconstruction et sur le résidu ; pour trancher entre « features absentes du dictionnaire » et « dictionnaire qui perd trop », aucune parade connue ; on le dit (cours, volet M, M4 ; README du dépôt).",
    "Two limits for A10: the rank-three subspace moved valence, not the concept, and its effect did not come back on fresh generations — it is not a causal handle on sycophancy, and decomposing it into features would not say what carries sycophancy (course, Part 6, §2; repository README); and the open sparse dictionary for this model leaves most of the variance in its residual, which carries the read signal (repository README). Workaround: the no-pressure control arm and a rival concept's direction, at matched degradation, before decomposing, and the signal read on the reconstruction and on the residual; to decide between \"features absent from the dictionary\" and \"a dictionary that loses too much\", none known; say so (course, Part M, M4; repository README)."))
add('A9-A17', 5060, 5385, av(
    "Le réalisme par paires de Kissane mesure si un juge prend une transcription d'audit pour une transcription réelle ; il ne dit pas si une intention implantée ressemble à une intention naturelle — une intention implantée est peut-être plus saillante (cours, volet 7, F·25 ; passation, §5.2 ; fiche 15). Parade partielle : planter le même sabotage par plusieurs recettes, en tenir une à part, et ajouter l'organisme d'une autre équipe (cours, volet 2, §A, K71) ; contre l'écart entre l'implanté et le naturel lui-même, aucune parade connue ; on le dit (explication du 2 octobre, partie 1 ; cours, volet M, M5).",
    "Kissane's paired realism measures whether a judge mistakes an audit transcript for a real one; it does not say whether an implanted intention resembles a natural one — an implanted intention may be more salient (course, Part 7, F·25; handover, §5.2; reading sheet 15). Partial workaround: plant the same sabotage through several recipes, hold one out, and add another team's organism (course, Part 2, §A, K71); against the gap between implanted and natural itself, no workaround is known; say so (explanation of 2 October, part 1; course, Part M, M5)."))
add('A9-A17', 5064, 5389, renvoi(['juge', 'sae', 'graf', 'abla', 'orga', 'moni']))

# ===== B1 · attaque coupée entre sessions — fin de la section (après le paragraphe EN)
add('B1', 5094, 5419, av(
    "Les transcriptions du banc sont conçues à la main : une sonde lue sur elles lit un modèle qui traite le texte d'un autre, pas l'intention d'un agent qui écrit sa propre procédure, et elle peut lire le texte plutôt qu'une représentation (cours, volet 7, F·23 ; cours, volet 11, réponse B14 ; programme, partie 8). Parade : faire produire les trajectoires par le modèle lui-même, avec un organisme à qui l'on a installé la procédure nuisible comme cas connu, lire au jeton d'action avec des raisons neutres préremplies, et garder le seuil calibré sur les variantes bénignes appariées (cours, volet 6, §8 ; passation, §5.2 ; programme, parties 3 et 8 ; cours, volet 7, F·23).",
    "The benchmark's transcripts are hand-designed: a probe read on them reads a model processing someone else's text, not the intention of an agent writing its own procedure, and it may read the text rather than a representation (course, Part 7, F·23; course, Part 11, answer B14; programme, part 8). Workaround: have the model itself produce the trajectories, with an organism in which the harmful procedure was installed as the known case, read at the action token with neutral reasons prefilled, and keep the threshold calibrated on paired benign variants (course, Part 6, §8; handover, §5.2; programme, parts 3 and 8; course, Part 7, F·23)."))
add('B1', 5094, 5419, renvoi(['moni', 'sond', 'red']))

# ===== B2 · une évaluation que le modèle ne reconnaît pas
add('B2', 5115, 5440, av(
    "Un contrôle aléatoire de l'inhibition n'est que le nul de spécificité ; le dommage ne s'écarte qu'à dégradation appariée (cours, volet M, M4) ; et la conscience verbalisée ne mesure pas l'inhibition : des directions aléatoires la font baisser aussi, et les mesures de la conscience d'évaluation — sonde, NLA, question de suivi — ne sont que faiblement corrélées (programme, partie 8 ; fiche 2). Parade : des sous-espaces aléatoires de même rang à dégradation appariée, un critère principal comportemental avec une sonde latente comme contrôle, et dire laquelle des mesures a fondé quel chiffre (programme, parties 3 et 8 ; cours, volet 5, sujet 4 ; cours, volet M, M4).",
    "A random control for the inhibition is only the specificity null; damage is ruled out only at matched degradation (course, Part M, M4); and verbalized awareness does not measure the inhibition: random directions lower it too, and the measures of evaluation awareness — probe, NLA, follow-up question — are only weakly correlated (programme, part 8; reading sheet 2). Workaround: random subspaces of the same rank at matched degradation, a behavioural main criterion with a latent probe as a control, and saying which measure grounded which number (programme, parts 3 and 8; course, Part 5, topic 4; course, Part M, M4)."))
add('B2', 5115, 5440, renvoi(['eval', 'pilo', 'alea', 'degr', 'sond', 'cotv', 'juge']))

# ===== B3 · déléguer aux chercheurs automatisés
add('B3', 5139, 5464, av(
    "La récupération de l'écart par les agents automatisés s'est faite avec des idées qui exploitaient la structure propre au jeu de données, et sur une tâche binaire, un fort qui contredit partout passerait aussi pour une récupération (cours, volet 2, §F, JB8). Parade : une tâche à vérité connue, lue sur les items tenus à part où le superviseur se trompe, avec l'accord du fort là où le superviseur a raison, et une copie entraînée sur les étiquettes vraies comme cas connu (cours, volet 2, §F, JB8).",
    "The automated agents recovered the gap with ideas that exploited the dataset's own structure, and on a binary task, a strong model that contradicts everywhere would also pass for recovery (course, Part 2, §F, JB8). Workaround: a task with known truth, read on the held-out items where the supervisor is wrong, with the strong model's agreement where the supervisor is right, and a copy trained on true labels as the known case (course, Part 2, §F, JB8)."))
add('B3', 5139, 5464, renvoi(['w2s', 'moni', 'red']))

# ===== B4 · la conscience d'évaluation jamais verbalisée
add('B4', 5159, 5484, av(
    "L'inhibition sur Sonnet 4.5 a la même limite qu'à la réponse 56 — des vecteurs de contrôle arbitraires font aussi monter le désalignement, plus faiblement, et un contrôle de même norme n'est que le nul de spécificité (fiche 2 ; cours, volet M, M4) — ; et le « moins d'un pour cent » de ton travail n'a pas encore été mesuré à dégradation égale (cours, volet 11, réponse A4). Parade : des sous-espaces aléatoires de même rang à dégradation appariée, une baseline de prompt et une courbe dose-réponse, et la partition refaite par le protocole de la réponse A4 (fiche 2 ; cours, volet 2, §C, K47 ; cours, volet 11, réponse A4).",
    "The Sonnet 4.5 inhibition has the same limit as at answer 56 — arbitrary control vectors also raise misalignment, more weakly, and a matched-norm control is only the specificity null (reading sheet 2; course, Part M, M4) —; and the \"under one percent\" of your work has not yet been measured at equal degradation (course, Part 11, answer A4). Workaround: random subspaces of the same rank at matched degradation, a prompt baseline and a dose-response curve, and the partition redone with the protocol of answer A4 (reading sheet 2; course, Part 2, §C, K47; course, Part 11, answer A4)."))
add('B4', 5159, 5484, av(
    "Dans les cas où l'on « sait » si le modèle est en évaluation, on sait la règle installée et ses indices, pas ce que le modèle croit : l'organisme conditionné à l'évaluation ne suit pas sa règle à la lettre, et ne distingue pas de façon fiable évaluation et déploiement à partir d'indices subtils (fiche 10). Parade : étiqueter chaque entrée par sa conduite, jamais par la sonde, valider la sonde sur des formulations tenues à part, et prendre cet organisme comme cas connu de « je suis évalué » (passation, §5.2 ; explication du 2 octobre, parties 2 et 3 ; programme, parties 3 et 4).",
    "In the cases where we \"know\" whether the model is in evaluation, we know the installed rule and its cues, not what the model believes: the evaluation-conditioned organism does not follow its rule to the letter, and does not reliably tell evaluation from deployment from subtle cues (reading sheet 10). Workaround: label each input by its conduct, never by the probe, validate the probe on held-out phrasings, and take that organism as the known case for \"I am being evaluated\" (handover, §5.2; explanation of 2 October, parts 2 and 3; programme, parts 3 and 4)."))
add('B4', 5159, 5484, renvoi(['sond', 'pilo', 'cas', 'cotv', 'nla', 'jlen', 'box']))

# ===== B5 · le fort comprend ce que le faible ne comprend pas
add('B5', 5179, 5504, av(
    "Un juge fort pris pour vérité de terrain est un juge LLM, avec ses erreurs systématiques, et il peut partager celles du fort qu'il départage, comme un modèle qui s'audite presque lui-même (cours, volet 6, §2 ; fiches, partie B, piège 6 ; fiche 2). Parade : valider d'abord sur une tâche à vérité connue, lue sur les items tenus à part où le faible se trompe, avec une copie entraînée sur les étiquettes vraies comme cas connu, et sceller le juge, audité par des humains sur des items stratifiés (cours, volet 2, §F, JB8 ; programme, partie 3) ; pour un juge proche du modèle qu'il juge, aucune parade connue au-delà de cette validation ; on le dit (fiches, partie B, piège 6).",
    "A strong judge taken as ground truth is an LLM judge, with its systematic errors, and it may share those of the strong model it arbitrates, like a model almost auditing itself (course, Part 6, §2; reading sheets, part B, trap 6; reading sheet 2). Workaround: validate first on a task with known truth, read on the held-out items where the weak model is wrong, with a copy trained on true labels as the known case, and seal the judge, audited by humans on stratified items (course, Part 2, §F, JB8; programme, part 3); for a judge close to the model it judges, no workaround is known beyond that validation; say so (reading sheets, part B, trap 6)."))
add('B5', 5179, 5504, renvoi(['w2s', 'juge', 'part']))

# ===== B6 · défenses inter-requêtes
add('B6', 5200, 5525, renvoi(['moni', 'red', 'clas']))

# ===== B7 · inoculation, pilotage préventif, midtraining
add('B7', 5221, 5546, av(
    "La projection sur la direction du trait, lue d'un bras à l'autre, mêle l'effet cherché et un biais de mesure : l'entraînement change les représentations, et une direction calibrée sur un bras lirait autrement dans un autre (passation, §5.2) ; et le lien entre ce déplacement et le trait n'est que corrélationnel (fiche 8). Parade : une sonde neuve par bras et après l'entraînement, sur un jeu d'indices disjoint, la direction extraite aussi dans le modèle de base, et le trait au test comme critère principal, la projection restant une mesure séparée (passation, §5.2 ; programme, partie 3).",
    "The projection onto the trait direction, read from one arm to another, mixes the effect sought with a measurement bias: training changes the representations, and a direction calibrated on one arm would read differently in another (handover, §5.2); and the link between that shift and the trait is only correlational (reading sheet 8). Workaround: a fresh probe per arm and after training, on a disjoint cue set, the direction also extracted in the base model, and the trait at test time as the main criterion, the projection remaining a separate measure (handover, §5.2; programme, part 3)."))
add('B7', 5221, 5546, av(
    "L'avantage hors distribution du midtraining a été lu sur des modèles ouverts, dans des scènes agentiques que le modèle peut reconnaître comme des tests (cours, volet 7, F·34). Parade : deux versions de chaque environnement, tirées au hasard, qui ne diffèrent que par des indices de réalisme notés par un discriminateur, avec un organisme dressé à se cacher comme cas connu (cours, volet 2, §B, K63).",
    "Midtraining's out-of-distribution advantage was read on open models, in agentic scenes the model can recognize as tests (course, Part 7, F·34). Workaround: two versions of each environment, randomly assigned, differing only in realism cues scored by a discriminator, with an organism trained to hide as the known case (course, Part 2, §B, K63)."))
add('B7', 5221, 5546, renvoi(['pilop', 'sond', 'part', 'eval', 'box']))

# ===== B8 · même capacité, personas différents
add('B8', 5244, 5569, av(
    "La batterie aval est faite de scènes construites : le modèle peut y remarquer le test et se retenir, et dans une simulation, « c'est faux » est vrai, si bien qu'un pot de miel ne sépare pas un modèle qui le lit comme factice d'un modèle qui se retient (fiche 13 ; fiche 3) ; et sur un modèle récent, la scène d'alignment faking mesure peut-être la mémorisation du scénario, ses transcripts ayant été réinclus dans l'entraînement (fiches, partie C). Parade : deux versions de chaque environnement, tirées au hasard, qui ne diffèrent que par des indices de réalisme notés par un discriminateur, avec un organisme dressé à se cacher comme cas connu (cours, volet 2, §B, K63) ; contre le pot de miel lu comme factice et contre la mémorisation, aucune parade connue ; on le dit (fiche 3 ; fiches, partie C).",
    "The downstream battery is made of constructed scenes: the model can notice the test there and hold back, and in a simulation \"this is fake\" is true, so a honeypot does not separate a model that reads it as fake from one that holds back (reading sheet 13; reading sheet 3); and on a recent model, the alignment-faking scene may measure memorization of the scenario, its transcripts having been re-included in training (reading sheets, part C). Workaround: two versions of each environment, randomly assigned, differing only in realism cues scored by a discriminator, with an organism trained to hide as the known case (course, Part 2, §B, K63); against a honeypot read as fake and against memorization, no workaround is known; say so (reading sheet 3; reading sheets, part C)."))
add('B8', 5244, 5569, renvoi(['pilop', 'eval', 'orga']))

# ===== B9 · safety case contre le sandbagging
add('B9', 5267, 5592, av(
    "« Si la capacité remonte […], c'est qu'elle était là » suppose que le fine-tuning ne l'a pas enseignée : un petit fine-tuning peut créer la capacité qu'on croit éliciter (cours, volet 2, §B, K63). Parade : une élicitation à budget fixé d'avance, rapportée comme une borne, dont le gain ne compte qu'au-delà de celui du même budget sur un modèle qui n'a pas la capacité, et un organisme entraîné à sous-performer comme cas connu (cours, volet M, M7 ; cours, volet 2, §B, K63 ; cours, volet 7, F·26).",
    "\"If the capability comes back […] it was there\" assumes the fine-tune did not teach it: a small fine-tune can create the capability you think you are eliciting (course, Part 2, §B, K63). Workaround: elicitation at a budget fixed in advance, reported as a bound, whose gain counts only beyond that of the same budget on a model without the capability, and an organism trained to underperform as the known case (course, Part M, M7; course, Part 2, §B, K63; course, Part 7, F·26)."))
add('B9', 5267, 5592, av(
    "Une remontée sous inhibition ne fait une preuve mécaniste qu'au-delà des témoins : dans la lignée des cartes système, des vecteurs de contrôle arbitraires bougent aussi le comportement, et un contrôle de même norme n'est que le nul de spécificité (fiche 2 ; cours, volet M, M4). Parade : plusieurs familles de témoins au même rang — sous-espaces aléatoires, contrastes sans rapport, directions de forte variance, simple prompt — comparées à dégradation appariée, et un organisme conditionné à l'évaluation comme cas connu de la sonde (programme, parties 3 et 7 ; explication du 2 octobre, partie 3).",
    "A rise under inhibition is mechanistic evidence only beyond the controls: across the system-card lineage, arbitrary control vectors also move behaviour, and a matched-norm control is only the specificity null (reading sheet 2; course, Part M, M4). Workaround: several families of controls at the same rank — random subspaces, unrelated contrasts, high-variance directions, a plain prompt — compared at matched degradation, and an evaluation-conditioned organism as the probe's known case (programme, parts 3 and 7; explanation of 2 October, part 3)."))
add('B9', 5267, 5592, renvoi(['eval', 'unle', 'w2s', 'pilo', 'sond', 'cas', 'box']))

# ===== B10 · surveillance non fiable et collusion
add('B10', 5290, 5615, av(
    "Un moniteur qui partage les poids de l'acteur peut reconnaître les attaques synthétiques dont on connaît la réponse, et ne laisser passer que les vraies : un pot de miel ne sépare pas un modèle qui le lit comme factice d'un modèle qui se retient (fiche 3 ; cours, volet 2, §B). Parade partielle : mesurer le réalisme de ces attaques par un juge mis devant la paire, et donner à leur construction de vraies ressources de déploiement (cours, volet 7, F·25) ; contre un moniteur qui lit le pot de miel comme factice, aucune parade connue ; on le dit (fiche 3).",
    "A monitor sharing the actor's weights can recognize synthetic attacks whose answer we know, and let only the real ones through: a honeypot does not separate a model that reads it as fake from one that holds back (reading sheet 3; course, Part 2, §B). Partial workaround: measure the realism of those attacks with a judge shown the pair, and give their construction real deployment resources (course, Part 7, F·25); against a monitor that reads the honeypot as fake, no workaround is known; say so (reading sheet 3)."))
add('B10', 5290, 5615, renvoi(['moni', 'eval', 'sond']))

# ===== B11 · la bonne réponse pour la bonne raison
add('B11', 5312, 5637, av(
    "Qu'inhiber la direction « l'utilisateur croit X » change la réponse ne montre la mauvaise raison qu'au-delà du dommage et d'un concept voisin : retirer une direction abîme aussi le modèle, et un effet d'ablation dit la nécessité, pas la spécificité (cours, volet M, M4). Parade : comparer à des sous-espaces aléatoires de même rang et à la direction rivale — « la réponse est vraie » —, tous à dégradation appariée (cours, volet M, M4).",
    "That inhibiting the \"the user believes X\" direction changes the answer shows the wrong reason only beyond damage and a neighbouring concept: removing a direction also damages the model, and an ablation effect shows necessity, not specificity (course, Part M, M4). Workaround: compare with random subspaces of the same rank and with the rival direction — \"the answer is true\" —, all at matched degradation (course, Part M, M4)."))
add('B11', 5312, 5637, renvoi(['sond', 'abla', 'degr', 'cot', 'auto']))

# ===== B12 · externalités multi-agents
add('B12', 5334, 5659, av(
    "Ce 1,0 contre 0,35 est le score d'une seule des douze tâches, en organisations simulées, et sa fiche n'a lu que le résumé : ni les contrôles internes ni les limites de détail (cours, volet 7, F·39). Parade : le dire comme le score d'une tâche simulée, et lire l'article en entier avant de s'en servir, comme la fiche le demande (cours, volet 7, F·39).",
    "This 1.0 against 0.35 is the score of a single one of the twelve tasks, in simulated organizations, and its sheet read only the abstract: neither the internal controls nor the detailed limits (course, Part 7, F·39). Workaround: state it as the score of one simulated task, and read the paper in full before using it, as the sheet asks (course, Part 7, F·39)."))
add('B12', 5334, 5659, renvoi(['moni', 'sond', 'eval']))

# ===== B13 · entraîner l'honnêteté plutôt que la détecter
add('B13', 5356, 5681, av(
    "Ce 0,88 est l'AUROC d'un détecteur fine-tuné, sur une suite de modèles rendus malhonnêtes, donc construits ; sa fiche, faite d'extraits, ne dit pas s'il est mesuré sur des types tenus à part, alors qu'une AUROC ne vaut que par cet écart (cours, volet 7, F·62 ; fiches, partie B, pièges 1 et 5 ; fiche 7) ; et la réserve qui ouvre la version française — un résultat absent de la base, à comprendre, pas à dire — vaut aussi pour la version anglaise, qui ne la porte pas (cours, volet M, M10, item 12). Parade : une validation croisée par types de mensonge tenus à part, et conclure sur l'instrument, pas sur la malhonnêteté naturelle (fiche 7 ; programme, partie 8).",
    "This 0.88 is the AUROC of a fine-tuned detector, on a suite of models made dishonest, hence constructed; its sheet, made of excerpts, does not say whether it is measured on held-out types, whereas an AUROC is worth only that gap (course, Part 7, F·62; reading sheets, part B, traps 1 and 5; reading sheet 7); and the caveat opening the French version — a result absent from the knowledge base, to understand, not to say — also holds for the English version, which does not carry it (course, Part M, M10, item 12). Workaround: cross-validation by held-out lie types, and conclusions about the instrument, not about natural dishonesty (reading sheet 7; programme, part 8)."))
add('B13', 5356, 5681, av(
    "Deux des trois tests ont leur propre limite : un déplacement nul est un nul, qui ne compte que si le même dispositif voit le déplacement du modèle avant l'entraînement à l'honnêteté, au même réglage, et se dit comme une borne (cours, volet M, M5) ; et que l'inhibition fasse revenir les mensonges ne prouve un changement interne qu'à dégradation appariée, des erreurs dues au dommage pouvant se compter comme des mensonges si l'étiquette ne vérifie pas la contradiction avec la croyance du modèle (cours, volet M, M4 ; fiche 7). Parade : ce cas connu dans le même protocole, des sous-espaces aléatoires de même rang à dégradation appariée, et des mensonges étiquetés contre la croyance obtenue en contexte neutre (cours, volet M, M4 et M5 ; fiche 7).",
    "Two of the three tests have their own limit: a zero displacement is a null, which counts only if the same setup sees the displacement of the model before honesty training, at the same setting, and is stated as a bound (course, Part M, M5); and the inhibition bringing the lies back proves an internal change only at matched degradation, since errors due to damage could count as lies if the label does not check the contradiction with the model's belief (course, Part M, M4; reading sheet 7). Workaround: that known case in the same protocol, random subspaces of the same rank at matched degradation, and lies labelled against the belief elicited in a neutral context (course, Part M, M4 and M5; reading sheet 7)."))
add('B13', 5356, 5681, renvoi(['dete', 'sond', 'juge', 'pilo', 'cas']))

# ===== B14 · une seule évaluation adverse demain
add('B14', 5375, 5700, av(
    "Une case vide est un nul : il ne compte que si un organisme à qui l'on a installé l'une de ces stratégies, rejoué dans le même harnais, remplit la case « exécute » ; et le modèle de production peut aussi reconnaître le test et se retenir (cours, volet M, M5 ; fiche 13 ; cours, volet 2, §B). Parade : ce cas connu, deux versions de chaque tâche qui ne diffèrent que par des indices de réalisme notés par un discriminateur, et un budget fixé d'avance, le résultat dit comme une borne à ce budget, jamais comme une absence (cours, volet 2, §B, K63 ; cours, volet M, M5 et M7).",
    "An empty cell is a null: it counts only if an organism in which one of those strategies was installed, replayed in the same harness, fills the \"executes\" cell; and the production model can also recognize the test and hold back (course, Part M, M5; reading sheet 13; course, Part 2, §B). Workaround: that known case, two versions of each task differing only in realism cues scored by a discriminator, and a budget fixed in advance, the result stated as a bound at that budget, never as an absence (course, Part 2, §B, K63; course, Part M, M5 and M7)."))
add('B14', 5375, 5700, renvoi(['red', 'moni', 'eval', 'cas']))


# ---------------------------------------------------------------- assemblage et vérifications
def uniq(fi, ancre):
    a, b = TR[fi]
    return [i + 1 for i in range(a - 1, b) if L[fi][i].strip() == ancre.strip()]


ins, errs, report = [], [], []
for sec, lfr, len_, tfr, ten in S:
    afr, aen = L['FR'][lfr - 1], L['EN'][len_ - 1]
    for fi, anc, ln in (('FR', afr, lfr), ('EN', aen, len_)):
        a, b = TR[fi]
        if not (a <= ln <= b):
            errs.append(f'{sec} {fi} : ligne {ln} hors tranche')
        u = uniq(fi, anc)
        if u != [ln]:
            errs.append(f'{sec} {fi} : ancre trouvée aux lignes {u} (attendu {ln}) : {anc[:80]}')
        if not anc.strip():
            errs.append(f'{sec} {fi} : ancre vide')
    ins.append({'fichier': 'FR', 'ancre': afr, 'texte': tfr})
    ins.append({'fichier': 'EN', 'ancre': aen, 'texte': ten})
    report.append(f'{sec:8s} FR l.{lfr} | EN l.{len_} | {tfr[:60]}')

# citations : aucune de 15 mots ou plus entre guillemets
for d in ins:
    for q in re.findall(r'«([^»]*)»', d['texte']) + re.findall(r'"([^"]*)"', d['texte']):
        if len(q.split()) >= 15:
            errs.append(f"citation trop longue ({len(q.split())} mots) : {q[:80]}")

if errs:
    print('ERREURS :')
    print('\n'.join(errs))
    sys.exit(1)

json.dump({'tranche': 'volet11_53_et_fin', 'insertions': ins}, open(OUT, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('\n'.join(report))
print(f'{len(ins)} insertions écrites dans {OUT}')
