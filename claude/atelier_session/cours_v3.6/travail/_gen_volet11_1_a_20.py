#!/usr/bin/env python3
"""Génère travail/insertions_volet11_1_a_20.json (volet 11, réponses 1 à 20).

Chaque entrée : (ligne FR de la v3.5, ligne EN de la v3.5, texte FR, texte EN).
Les ancres sont lues dans les sources par numéro de ligne, donc recopiées telles quelles.
"""
import json, os

W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FR = open(f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md', encoding='utf8').read().split('\n')
EN = open(f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md', encoding='utf8').read().split('\n')
TR = {'FR': (3656, 4128), 'EN': (3895, 4403)}

# --- renvois : morceaux réutilisables -------------------------------------------------
R = {
    'abl': ("ablation et projection → volet 2, §D (après « La méthode »)",
            'ablation and projection → Part 2, §D (after "The method")'),
    'sonde': ("sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth »)",
              'activation probes → Part 2, §C (after "In practice — The Geometry of Truth")'),
    'jlens': ("J-lens et espace de travail → volet 2, C bis (après « Le test, tel qu'il se dit »)",
              'J-lens and workspace → Part 2, C bis (after "The test, as it is said")'),
    'juge': ("juges LLM → volet 6, §2 (après « La loi de déplacement »)",
             'LLM judges → Part 6, §2 (after "The displacement law")'),
    'degr': ("dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse »)",
             'matched degradation and dose-response → Part M, M4 (after "Dose-response")'),
    'alea': ("contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme »)",
             'random controls → Part M, M4 (after "The matched-norm random direction")'),
    'pilot': ("pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition »)",
              'steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition")'),
    'pilot_persona': ("pilotage par vecteurs, dont vecteurs de persona → volet 2, §C (après « En pratique — Contrastive Activation Addition »)",
                      'steering vectors, including persona vectors → Part 2, §C (after "In practice — Contrastive Activation Addition")'),
    'sae': ("dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity",
            'dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity'),
    'cas': ("cas connu → volet M, M5 (fin de section)",
            'known case → Part M, M5 (end of section)'),
    'orga': ("organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives »)",
             'model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives")'),
    'detect': ("détecteurs fine-tunés → volet 7, F·29",
               'fine-tuned detectors → Part 7, F·29'),
    'redt': ("red-teaming → volet 2, §H (après « En pratique — StrongREJECT »)",
             'red-teaming → Part 2, §H (after "In practice — StrongREJECT")'),
    'classif': ("classifieurs de sûreté → volet 2, §H (fin du cas d'application G1)",
                'safety classifiers → Part 2, §H (end of worked case G1)'),
    'desap': ("désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve »)",
              'unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test")'),
    'evals': ("évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging »)",
              'behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging")'),
    'tenu': ("jeu tenu à part → volet M, M4 (après « Le jeu tenu à part »)",
             'held-out set → Part M, M4 (after "The held-out set")'),
    'monit': ("moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes »)",
              'control monitors → Part 2, §G (after "In practice — coup probes")'),
    'cot': ("chaîne de pensée comme moniteur → volet 11, réponse 43",
            'chain of thought as a monitor → Part 11, answer 43'),
    'cot_verb': ("chaîne de pensée comme moniteur, et conscience verbalisée → volet 11, réponse 43",
                 'chain of thought as a monitor, and verbalized awareness → Part 11, answer 43'),
    'enc_tout': ("sondes de désalignement, J-lens compris (encadré du 2 octobre) → volet 2, §A (avant le cas d'application K71), §C (avant le cas d'application K47) et C bis (avant le cas d'application K72)",
                 'misalignment probes, J-lens included (box of 2 October) → Part 2, §A (before the worked case K71), §C (before the worked case K47) and C bis (before the worked case K72)'),
    'enc_23': ("sondes de désalignement, 2 et 3 : comment les entraîner, et le hors-distribution (encadré du 2 octobre) → volet 2, §C (après « En pratique — Contrastive Activation Addition », avant le cas d'application K47)",
               'misalignment probes, 2 and 3: how to train them, and out of distribution (box of 2 October) → Part 2, §C (after "In practice — Contrastive Activation Addition", before the worked case K47)'),
}


def renvoi(*cles):
    fr = '> ⚠ **Limites et parades** : ' + ' ; '.join(R[c][0] for c in cles) + ' *(v3.6)*'
    en = '> ⚠ **Limits and workarounds**: ' + '; '.join(R[c][1] for c in cles) + ' *(v3.6)*'
    return fr, en


P = '> ⚠ *(v3.6)* '

ENTREES = []


def add(lfr, len_, fr, en):
    ENTREES.append((lfr, len_, fr, en))


# ======================= 1 · « Tell us about your work. » =======================
add(3698, 3937,
    P + "La charge se lit au J-lens, qui n'a été montré que sur Claude et ne lit que des concepts d'un seul token (fiche 1 ; passation, §5.2) ; "
        "et « charge » désigne trois grandeurs distinctes selon les textes (cours, volet 6, §6). Parade : sur ton modèle ouvert, une porte — "
        "reproduire d'abord l'échange d'un concept d'un seul token, sinon un tuned lens déclaré comme approximation, et la thèse n'est alors pas "
        "testée au sens de l'article —, puis geler d'abord le prédicteur principal, et dire lequel (programme, parties 3 et 8 ; cours, volet 2, C bis ; "
        "cours, volet 6, §6).",
    P + "Loading is read with the J-lens, which has been shown only on Claude and reads only single-token concepts (reading sheet 1; handover, §5.2); "
        "and \"loading\" names three distinct quantities depending on the text (course, Part 6, §6). Workaround: on your open model, a gate — first "
        "reproduce the swap of a single-token concept, otherwise a tuned lens declared as an approximation, and the thesis is then not tested in the "
        "paper's sense —, then freeze the main predictor first, and say which (programme, parts 3 and 8; course, Part 2, C bis; course, Part 6, §6).")
add(3702, 3941, *renvoi('abl', 'sonde', 'jlens', 'juge'))

# ======================= 2 · « What did your rank-three ablation actually show? » =======================
add(3709, 3950,
    P + "Le taux jugé passe par un juge dont l'accord avec un second juge n'est que modéré, qui ne voit que les deux réponses, pas le texte évalué, "
        "et dont aucun sous-ensemble noté par des humains ne borne l'erreur (README du dépôt). Parade : un juge scellé — prompt, modèle et "
        "température gelés — et un audit humain stratifié qui borne son erreur, l'accord rapporté ; juger la réponse entière, et garder le texte "
        "complet (programme, partie 3 ; README du dépôt).",
    P + "The judged rate goes through a judge whose agreement with a second judge is only moderate, which sees only the two responses, not the "
        "evaluated text, and whose error no human-rated subset bounds (repository README). Workaround: a sealed judge — prompt, model and "
        "temperature frozen — and a stratified human audit that bounds its error, with agreement reported; judge the whole answer, and keep the "
        "full text (programme, part 3; repository README).")
add(3722, 3963,
    P + "La partition n'a pas été mesurée à dégradation égale — « un chiffre à refaire à dégradation égale » (cours, volet 11, réponse A4) —, et "
        "un aléatoire apparié en covariance y fait davantage que la direction de la sonde (cours, volet 6, §2 et §3). Parade : le protocole de la "
        "réponse A4 — une intervention sur la direction lue, une sur l'état complet aux mêmes endroits, et des directions témoins comparées à "
        "dégradation égale —, le patch de l'état complet servant de plafond (cours, volet 11, réponse A4 ; programme, partie 8).",
    P + "The partition was not measured at equal degradation — \"a number to redo at equal degradation\" (course, Part 11, answer A4) —, and a "
        "covariance-matched random direction does more there than the probe direction (course, Part 6, §2 and §3). Workaround: the protocol of "
        "answer A4 — one intervention on the read direction, one on the full state at the same sites, and control directions compared at equal "
        "degradation —, with the full-state patch as the ceiling (course, Part 11, answer A4; programme, part 8).")
add(3725, 3966,
    P + "Même au registre, un témoin aléatoire de même norme ne serait que le nul de spécificité ; et les contrôles aléatoires du protocole "
        "d'origine — de quel aléatoire il s'agit, le dossier le dira — n'écartent pas le dommage : un effet d'ablation dit la nécessité, pas la "
        "spécificité (cours, volet 6, §2 ; cours, volet M, M4). Parade : des sous-espaces aléatoires de même rang, comparés à dégradation appariée "
        "— même exactitude tenue à part, même cohérence jugée — par un retrait partiel ou par une courbe de l'effet contre la dégradation "
        "(cours, volet M, M4 ; cours, volet 2, C bis ; programme, partie 7).",
    P + "Even if it were in the register, a matched-norm random control would be only the specificity null; and the random controls of the "
        "original protocol — which random it is, the dossier will say — do not rule out damage: an ablation effect shows necessity, not "
        "specificity (course, Part 6, §2; course, Part M, M4). Workaround: random subspaces of the same rank, compared at matched degradation — "
        "same held-out accuracy, same judged coherence — through a partial removal or a curve of effect against degradation (course, Part M, M4; "
        "course, Part 2, C bis; programme, part 7).")
add(3725, 3966, *renvoi('abl', 'degr', 'alea', 'juge'))

# ======================= 3 · « And rank one? Didn't a single direction work? » =======================
add(3735, 3978,
    P + "Ces nuls de rang un n'ont pas de cas connu au même réglage : sans une intervention montrée capable, à cette dose et à ces couches, de "
        "faire agir un concept connu, un nul peut venir d'un rang trop bas si le concept est réparti — c'est ta propre prédiction (fiche 7 ; "
        "contre-lecture des fiches ; cours, volet M, M5). Parade : un cas connu au même réglage — les pays, dont le vecteur s'échange dans "
        "l'article sur l'espace de travail et dont le retrait doit atteindre l'effet dès le rang un — et un balayage de rang dans une même "
        "expérience, sur des sous-espaces emboîtés ; le nul se dit alors comme une borne, avec son budget et sa puissance (cours, volet 2, §C, "
        "K47 ; cours, volet 2, C bis ; cours, volet 6, §6 ; cours, volet M, M5).",
    P + "These rank-one nulls have no known case at the same setting: without an intervention shown able, at that dose and at those layers, to "
        "make a known concept act, a null can come from too low a rank if the concept is distributed — your own prediction (reading sheet 7; "
        "counter-reading of the sheets; course, Part M, M5). Workaround: a known case at the same setting — countries, whose vector swaps in the "
        "workspace paper and whose removal must reach the effect already at rank one — and a rank sweep within one experiment, on nested "
        "subspaces; the null is then stated as a bound, with its budget and power (course, Part 2, §C, K47; course, Part 2, C bis; course, "
        "Part 6, §6; course, Part M, M5).")
add(3735, 3978,
    P + "Deux des méthodes nommées ont leur limite propre : l'addition contrastive d'activations forçait un artefact de polarité oui/non au lieu "
        "de retirer la complaisance — aucune parade connue ; on le dit — ; et le dictionnaire épars ouvert pour ce modèle laisse la plus grande "
        "part de la variance dans son résidu, qui porte le signal lu (des corrélations peut-être d'ajustement), si bien que « le pincement de "
        "features n'agit pas » ne sépare pas « features absentes du dictionnaire » de « dictionnaire qui perd trop » (README du dépôt). Parade : "
        "lire le signal sur la reconstruction et sur le résidu ; pour trancher entre les deux lectures, aucune parade connue ; on le dit "
        "(README du dépôt).",
    P + "Two of the methods named have their own limit: contrastive activation addition forced a yes/no polarity artefact instead of removing "
        "sycophancy — no workaround known; say so —; and the open sparse dictionary for this model leaves most of the variance in its residual, "
        "which carries the read signal (correlations that may be training fit), so \"feature clamping does not act\" does not separate \"features "
        "absent from the dictionary\" from \"a dictionary that loses too much\" (repository README). Workaround: read the signal on the "
        "reconstruction and on the residual; to decide between the two readings, none known; say so (repository README).")
add(3745, 3988, *renvoi('pilot', 'abl', 'sae', 'cas'))

# ======================= 4 · « Did it replicate? » =======================
add(3760, 4005,
    P + "Deux limites que la réponse ne dit pas : les générations d'origine sont un seul tirage par condition, la variance entre tirages n'ayant "
        "pas été mesurée ; et le sous-espace a été extrait sur des items du même lot que ceux qui servent ensuite à évaluer l'ablation (README "
        "du dépôt). Parade : plusieurs générations par item, avec des intervalles par bootstrap au niveau des items, comme le programme le fait "
        "par scénario, et l'extraction sur un jeu d'items disjoint (programme, partie 7 ; README du dépôt).",
    P + "Two limits the answer does not state: the original generations are a single draw per condition, between-draw variance not having been "
        "measured; and the subspace was extracted on items from the same pool as those later used to evaluate the ablation (repository README). "
        "Workaround: several generations per item, with bootstrap intervals at the item level, as the programme does per scenario, and "
        "extraction on a disjoint item set (programme, part 7; repository README).")
add(3760, 4005, *renvoi('abl', 'juge', 'cas'))

# ======================= 6 · « How would you detect misalignment… » =======================
add(3790, 4037,
    P + "Des vecteurs de contrôle aléatoires n'écartent que « n'importe quelle poussée de cette taille fait autant » — le nul de spécificité —, "
        "pas « l'intervention elle-même abîme le modèle », qui ne s'écarte qu'à dégradation appariée ; et dans la lignée des cartes, des vecteurs "
        "arbitraires bougent aussi le comportement, chaque direction dégrade les sorties, et l'effet est modeste et « highly dataset-dependent » "
        "(cours, volet M, M4 ; fiche 2). Parade : des sous-espaces aléatoires de même rang à dégradation appariée, une baseline de prompt et une "
        "courbe dose-réponse contre plusieurs témoins, et la conclusion au conditionnel, comme la dit la réponse 19 (fiche 2 ; cours, volet 2, "
        "§C, K47 ; cours, volet 11, réponse 19).",
    P + "Random control vectors rule out only \"any push of that size does as much\" — the specificity null —, not \"the intervention itself "
        "damages the model\", which is ruled out only at matched degradation; and across the system cards, arbitrary vectors also move "
        "behaviour, every direction degrades the outputs, and the effect is modest and \"highly dataset-dependent\" (course, Part M, M4; reading "
        "sheet 2). Workaround: random subspaces of the same rank at matched degradation, a prompt baseline and a dose-response curve against "
        "several controls, and the conclusion in the conditional, as answer 19 states it (reading sheet 2; course, Part 2, §C, K47; course, "
        "Part 11, answer 19).")
add(3790, 4037,
    P + "Le jeu d'audit cité a ses limites : l'objectif implanté était décrit en clair dans les documents synthétiques, le pipeline laissait des "
        "artefacts qui le rendaient « artificially easy to discover », et sur quatre équipes, la seule qui échoue est celle sans accès aux "
        "données — l'accès aux données porte peut-être plus que l'interprétabilité (fiche 16). Parade : conclure sur l'instrument seulement "
        "(programme, partie 8), et chiffrer l'apport de l'interprétabilité par une ablation d'affordance, en retirant un outil à une équipe "
        "(fiche 16) ; contre un organisme trop facile, aucune parade connue ; on le dit (fiche 16).",
    P + "The auditing game cited has its limits: the implanted objective was described plainly in the synthetic documents, the pipeline left "
        "artefacts that made it \"artificially easy to discover\", and of four teams, the only one that failed was the one without data access — "
        "data access may carry more than interpretability (reading sheet 16). Workaround: conclude about the instrument only (programme, part 8), "
        "and quantify what interpretability adds through an affordance ablation, removing one tool from a team (reading sheet 16); against an "
        "organism that is too easy, none known; say so (reading sheet 16).")
add(3807, 4053,
    P + "Les détecteurs de mensonge cités ne sont pas des sondes : ce sont des modèles fine-tunés par LoRA pour répondre à une question "
        "d'auto-rapport sur un transcript, et le 0,95 est une progression en distribution pendant l'entraînement (fiche 7 ; explication du "
        "2 octobre, partie 2). Parade : ne pas transférer leurs chiffres aux sondes ; pour une sonde, mesurer l'écart entre la distribution "
        "d'entraînement et des familles entières tenues à part, et faire le test causal, à dégradation appariée, avec un cas connu au même "
        "réglage (fiche 7 ; explication du 2 octobre, partie 3).",
    P + "The lie detectors cited are not probes: they are models fine-tuned with LoRA to answer a self-report question about a transcript, and "
        "the 0.95 is an in-distribution progression during training (reading sheet 7; explanation of 2 October, part 2). Workaround: do not "
        "transfer their numbers to probes; for a probe, measure the gap between the training distribution and whole held-out families, and run "
        "the causal test, at matched degradation, with a known case at the same setting (reading sheet 7; explanation of 2 October, part 3).")
add(3807, 4053,
    P + "Les deux familles ferment l'écart entre deux façons d'implanter, pas celui entre l'implanté et le naturel : une intention implantée est "
        "peut-être plus saillante qu'une naturelle — sur les sleeper agents, la défection implantée est si saillante que des directions "
        "aléatoires la séparent déjà (passation, §5.2 ; fiche 15). Parade partielle : planter le même comportement par plusieurs recettes, lire "
        "la sonde sur une recette tenue à part, avec un comportement inoffensif planté de la même façon comme contrôle, et l'organisme d'une "
        "autre équipe (cours, volet 2, §A, K71) ; contre l'écart entre l'implanté et le naturel lui-même, aucune parade connue ; on le dit "
        "(explication du 2 octobre, partie 1).",
    P + "The two families close the gap between two ways of implanting, not the one between implanted and natural: an implanted intention may be "
        "more salient than a natural one — on the sleeper agents, the implanted defection is so salient that random directions already separate "
        "it (handover, §5.2; reading sheet 15). Partial workaround: plant the same behaviour through several recipes, read the probe on a held-out "
        "recipe, with a harmless behaviour planted the same ways as a control, and another team's organism (course, Part 2, §A, K71); against "
        "the gap between implanted and natural itself, no workaround is known; say so (explanation of 2 October, part 1).")
add(3807, 4053, *renvoi('sonde', 'orga', 'cas', 'pilot', 'alea', 'detect', 'jlens', 'enc_tout'))

# ======================= 7 · « How would you prevent bad actors… » =======================
add(3820, 4066,
    P + "La parade manque ici : contre une porte dérobée dont on ignore le déclencheur, un jeu canari ne fait pas mieux qu'une red team boîte "
        "noire, puisqu'il ne contient pas ce déclencheur (cours, volet M, M5). Parade : un jumeau propre réentraîné sur des données auditées, un "
        "second pour borner l'écart dû au hasard, et un filtre empoisonné exprès comme cas connu (cours, volet M, M4 et M9) ; le jumeau propre "
        "ne donne qu'une borne large, qui signale moins : contre cela, aucune parade connue ; on le dit (cours, volet M, M4).",
    P + "The workaround is missing here: against a backdoor whose trigger is unknown, a canary set does no better than a black-box red team, "
        "since it does not contain that trigger (course, Part M, M5). Workaround: a clean twin retrained on audited data, a second one to bound "
        "chance variation, and a deliberately poisoned filter as the known case (course, Part M, M4 and M9); the clean twin gives only a wide "
        "bound, which flags less: against that, no workaround is known; say so (course, Part M, M4).")
add(3820, 4066,
    P + "Le masquage sélectif des gradients n'est montré que sur de petits modèles — aucune parade connue ; on le dit —, et plus de "
        "réentraînement pour ramener la capacité ne prouve pas qu'elle est partie : l'information « désapprise » refait souvent surface (cours, "
        "volet 2, §I, JB10 ; cours, volet 2, §I). Parade : la ré-élicitation contre une référence jamais entraînée, au même budget, avec un "
        "modèle connu pour masquer comme cas connu, et une borne dite « not elicitable at this budget », jamais « removed » (cours, volet M, M4 "
        "et M5 ; cours, volet 2, §I, JB10).",
    P + "Selective gradient masking is shown only on small models — no workaround known; say so —, and more retraining to restore the capability "
        "does not prove it is gone: \"unlearned\" information often resurfaces (course, Part 2, §I, JB10; course, Part 2, §I). Workaround: "
        "re-elicitation against a never-trained reference, at the same budget, with a model known to mask as the known case, and a bound stated "
        "as \"not elicitable at this budget\", never \"removed\" (course, Part M, M4 and M5; course, Part 2, §I, JB10).")
add(3827, 4073,
    P + "Un différentiel nul ne compte qu'avec son cas connu : sinon le jeu ne sépare peut-être rien, et l'on conclurait à tort qu'on refuse "
        "pour rien (cours, volet M, M5 ; cours, volet 2, §H, G1). Parade : le modèle sans filtre doit montrer un uplift, et un filtre affaibli "
        "exprès plus de préjudice que sa version complète ; et dire quelle équipe rouge le chiffre suppose, au moins une optimisée composante "
        "par composante (cours, volet M, M5 ; cours, volet 2, §H, G1 ; cours, volet 7, F·24).",
    P + "A zero differential counts only with its known case: otherwise the game may separate nothing, and one would wrongly conclude that "
        "refusals buy nothing (course, Part M, M5; course, Part 2, §H, G1). Workaround: the model without a filter must show uplift, and a "
        "deliberately weakened filter more harm than its full version; and say which red team the number assumes, at least one optimized "
        "component by component (course, Part M, M5; course, Part 2, §H, G1; course, Part 7, F·24).")
add(3827, 4073, *renvoi('redt', 'classif', 'desap'))

# ======================= 8 · « How would you train models to be more robustly aligned… » =======================
add(3846, 4093,
    P + "Le gain hors distribution est lu sur un banc agentique, avec des modèles ouverts, dans des scènes que le modèle peut reconnaître comme "
        "des tests — la limite que la réponse pose elle-même à la fin (cours, volet 7, F·34). Parade : deux versions de l'environnement, tirées "
        "au hasard, qui ne diffèrent que par des indices de réalisme notés par un discriminateur, avec un organisme dressé à se cacher comme cas "
        "connu (cours, volet 2, §B, K63) ; qu'un banc tenu à part représente le réel, aucune parade connue ne le garantit ; on le dit (fiche 12).",
    P + "The out-of-distribution gain is read on an agentic benchmark, with open models, in scenes the model can recognize as tests — the limit "
        "the answer itself sets at the end (course, Part 7, F·34). Workaround: two versions of the environment, randomly assigned, differing only "
        "in realism cues scored by a discriminator, with an organism trained to hide as the known case (course, Part 2, §B, K63); that a held-out "
        "benchmark represents the real case, no known workaround guarantees; say so (reading sheet 12).")
add(3852, 4100,
    P + "La parade manque ici : un juge d'entraînement distinct du juge scellé d'évaluation, des métriques d'audit tenues à part, et la "
        "surveillance de la longueur et des motifs de flatterie (programme, partie 8) ; avant d'entraîner, auditer le juge : un juge scellé, "
        "prompt, modèle et température gelés, et un audit humain stratifié qui borne son erreur (programme, partie 3).",
    P + "The workaround is missing here: a training judge distinct from the sealed evaluation judge, held-out audit metrics, and monitoring of "
        "length and flattery patterns (programme, part 8); before training, audit the judge: a sealed judge, with prompt, model and temperature "
        "frozen, and a stratified human audit that bounds its error (programme, part 3).")
add(3852, 4100, *renvoi('evals', 'tenu', 'juge'))

# ======================= 9 · « What would you work on here, and why? » =======================
add(3876, 4124,
    P + "Un nul de la porte — le gain dans l'intervalle du bruit — ne compte qu'avec le cas connu du moniteur blanc : des positifs connus, "
        "canaris ou organisme où l'on a installé l'intention, attrapés au même seuil (cours, volet M, M5 ; cours, volet 3, §3, K70 ; passation, "
        "§5.2) ; et un chiffre de sûreté tiré d'un jeu rouge/bleu est relatif à la force de l'équipe rouge supposée (cours, volet 7, F·24). "
        "Parade : valider le moniteur blanc sur ces positifs connus avant la porte ; dire quelle équipe rouge la porte suppose, au moins une "
        "optimisée composante par composante ; et rapporter le rappel à faux positifs fixés, avec le ratio de trafic bénin (cours, volet 7, "
        "F·24 ; cours, volet 6, §6).",
    P + "A null at the gate — the gain inside the noise interval — counts only with the white-box monitor's known case: known positives, "
        "canaries or an organism in which the intention was installed, caught at the same threshold (course, Part M, M5; course, Part 3, §3, "
        "K70; handover, §5.2); and a safety number from a red/blue game is relative to the strength of the red team assumed (course, Part 7, "
        "F·24). Workaround: validate the white-box monitor on those known positives before the gate; say which red team the gate assumes, at "
        "least one optimized component by component; and report recall at fixed false positives, with the benign-traffic ratio (course, Part 7, "
        "F·24; course, Part 6, §6).")
add(3876, 4124, *renvoi('monit', 'sonde', 'orga', 'redt', 'enc_23'))

# ======================= 10 · « Diffuse Control already frames this… » =======================
add(3896, 4145,
    P + "« Difficiles à contrôler pour lui » ne dit pas qu'un entraînement ne déplace pas ce que lisent les sondes : selon un rapport, après un RL, des sondes "
        "neuves hors domaine se dégradent alors qu'une sonde neuve dans le domaine reste quasi parfaite (rapport d'antériorité 3 du 2 octobre, "
        "*The Obfuscation Atlas* — rapport, lu de façon ciblée) ; et itérer contre ses détecteurs sélectionne l'évasion (fiche 19). Parade : une "
        "sonde neuve après tout entraînement, sur un jeu d'indices disjoint, et des détecteurs scellés hors de la boucle — s'ils se déclenchent "
        "encore quand ceux de la boucle se taisent, l'évasion a été sélectionnée (passation, §5.2 ; programme, partie 3 ; fiche 19).",
    P + "\"Difficult for the model to control\" does not say that training will not move what the probes read: according to a report, after RL, fresh "
        "out-of-domain probes degrade while a fresh in-domain probe stays near perfect (prior-art report 3 of 2 October, *The Obfuscation "
        "Atlas* — report, read in a targeted way); and iterating against your detectors selects for evasion (reading sheet 19). Workaround: a "
        "fresh probe after any training, on a disjoint cue set, and sealed detectors outside the loop — if they still fire when the in-loop ones "
        "go quiet, evasion has been selected (handover, §5.2; programme, part 3; reading sheet 19).")
add(3896, 4145,
    P + "« Ils avaient raison » tirerait une conclusion de fond d'un nul d'instrument : sans cas connu où le moniteur blanc attrape, au même "
        "seuil, une intention qu'on a installée, l'échec de la porte dirait peut-être seulement que la sonde est aveugle (cours, volet M, M5 ; "
        "passation, §5.2). Parade : ce cas connu avant la porte, et le nul dit comme une borne, avec son budget et sa puissance (passation, "
        "§5.2 ; cours, volet M, M5).",
    P + "\"They were right\" would draw a substantive conclusion from an instrument null: without a known case in which the white-box monitor "
        "catches, at the same threshold, an intention that was installed, a failed gate might only say that the probe is blind (course, Part M, "
        "M5; handover, §5.2). Workaround: that known case before the gate, and the null stated as a bound, with its budget and power (handover, "
        "§5.2; course, Part M, M5).")
add(3896, 4145, *renvoi('monit', 'sonde'))

# ======================= 11 · Les prémisses fausses =======================
add(3902, 4153, *renvoi('sonde', 'abl', 'pilot_persona', 'juge', 'orga', 'cot', 'monit'))
add(3915, 4166,
    P + "Côté lecture aussi, séparer en distribution ne prouve rien : c'est l'écart avec la séparation sur des types tenus à part qui se mesure "
        "(fiches, partie B, piège 1 ; fiche 7) ; et la seule lecture mesurée sur le modèle des interventions est une corrélation peut-être "
        "d'ajustement, rien n'établissant que les items notés étaient exclus de l'entraînement de la sonde (README du dépôt ; cours, volet 6, "
        "§2). Parade : scorer des items exclus de l'entraînement de la sonde, extraire sur un jeu disjoint, et tenir à part des familles "
        "entières, jamais des paraphrases (README du dépôt ; explication du 2 octobre, partie 3).",
    P + "On the reading side too, separating in distribution proves nothing: what is measured is the gap with separation on held-out types "
        "(reading sheets, part B, trap 1; reading sheet 7); and the only reading measured on the intervention model is a correlation that may "
        "be training fit, nothing establishing that the scored items were excluded from the probe's training (repository README; course, "
        "Part 6, §2). Workaround: score items excluded from the probe's training, extract on a disjoint set, and hold out whole families, never "
        "paraphrases (repository README; explanation of 2 October, part 3).")
add(3924, 4175,
    P + "« Assez de puissance pour que ce nul compte » : la puissance ne remplace pas un cas connu, ce que dit la réponse 4 et que celle-ci "
        "tait (cours, volet M, M5 ; cours, volet 11, réponse 4). Parade : montrer que le même instrument — générations fraîches, juge sur la "
        "réponse entière — voit un effet quand il est là, et dire une borne, avec son budget et sa puissance, jamais une absence (cours, "
        "volet M, M5).",
    P + "\"Enough power for that null to count\": power does not replace a known case, which answer 4 says and this one leaves out (course, "
        "Part M, M5; course, Part 11, answer 4). Workaround: show that the same instrument — fresh generations, a judge on the whole answer — "
        "sees an effect when it is there, and state a bound, with its budget and power, never an absence (course, Part M, M5).")
add(3961, 4212,
    P + "Ce résultat lit le motif dans un scratchpad caché, donné avec la consigne de raisonner sur sa situation : le scratchpad n'est pas le "
        "raisonnement opaque, l'indice gratuit contre payant est construit, l'on ne sait pas trancher entre jeu de rôle et vraie préservation "
        "de buts, et ce que le RL a entraîné est la conformité, qui a fait monter le raisonnement de faux alignement sans que l'article en "
        "fasse la cause (fiche 14 ; fiches, partie B, piège 2). Parade : s'appuyer sur la mesure — l'écart de conformité entre les deux cas — "
        "et retirer l'indice lisible pour chercher quand même la préservation de buts (fiche 14) ; une réplication sur un modèle récent "
        "mesure peut-être la mémorisation du scénario, ses transcripts ayant été réinclus dans l'entraînement : contre cela, aucune parade "
        "connue ; on le dit (fiche 14 ; fiches, partie C).",
    P + "This result reads the motive in a hidden scratchpad, given with the instruction to reason about its situation: the scratchpad is not "
        "the opaque reasoning, the free-versus-paid cue is constructed, role-play cannot be told apart from genuine goal preservation, and what "
        "the RL trained was compliance, which raised alignment-faking reasoning without the paper making it the cause (reading sheet 14; "
        "reading sheets, part B, trap 2). Workaround: rest on the measurement — the compliance gap between the two cases — and remove the "
        "legible cue so as to look for goal preservation anyway (reading sheet 14); a replication on a recent model may measure memorization of "
        "the scenario, its transcripts having been re-included in training: against that, no workaround is known; say so (reading sheet 14; "
        "reading sheets, part C).")
add(3979, 4230,
    P + "Ce que la réponse ne dit pas : le lien entre le déplacement le long du vecteur et le trait est corrélationnel — la « troisième chose » "
        "est une prédiction, pas un mécanisme —, le trait doit être nommé d'avance, les directions sont grossières et l'évaluation légère "
        "(fiche 8) ; et la soustraction réduit le trait au prix d'une baisse de capacités, si bien que sans comparaison à dégradation appariée, "
        "on ne sait pas quelle part de la baisse est du dommage (cours, volet M, M4 ; fiches, partie B, piège 4). Parade : pour la causalité, "
        "des directions aléatoires de même norme — le nul de spécificité — puis des témoins à dégradation appariée — le dommage (cours, volet M, "
        "M4 ; passation, §5.2) ; pour l'extraction supervisée, aucune parade connue ; on le dit (fiche 8).",
    P + "What the answer does not say: the link between the shift along the vector and the trait is correlational — the \"third thing\" is a "
        "prediction, not a mechanism —, the trait must be named in advance, the directions are coarse and the evaluation light (reading "
        "sheet 8); and subtraction reduces the trait at a cost in capabilities, so that without a comparison at matched degradation, one cannot "
        "tell what share of the reduction is damage (course, Part M, M4; reading sheets, part B, trap 4). Workaround: for causality, "
        "matched-norm random directions — the specificity null — then controls at matched degradation — the damage (course, Part M, M4; "
        "handover, §5.2); for supervised extraction, none known; say so (reading sheet 8).")

# ======================= 13 · « Tell us about a time an experiment failed. » =======================
add(4019, 4271,
    P + "« Réfutée » vaut pour l'hypothèse forte, à ce réglage : un petit effet n'est pas détecté à cette taille d'échantillon (cours, volet 11, "
        "réponse 3), et sans cas connu au même réglage, un nul à une direction peut venir d'un rang trop bas (fiche 7 ; contre-lecture des "
        "fiches ; cours, volet M, M5). Parade : un cas connu au même réglage — les pays, dont le retrait doit atteindre l'effet dès le rang un — "
        "et un balayage de rang dans une même expérience, sur des sous-espaces emboîtés (cours, volet 2, C bis ; cours, volet 6, §6).",
    P + "\"Refuted\" holds for the strong hypothesis, at that setting: a small effect is not detected at that sample size (course, Part 11, "
        "answer 3), and without a known case at the same setting, a one-direction null can come from too low a rank (reading sheet 7; "
        "counter-reading of the sheets; course, Part M, M5). Workaround: a known case at the same setting — countries, whose removal must reach "
        "the effect already at rank one — and a rank sweep within one experiment, on nested subspaces (course, Part 2, C bis; course, Part 6, §6).")
add(4019, 4271, *renvoi('pilot', 'abl', 'cas'))

# ======================= 14 · « What would you want to have done in four months? » =======================
add(4028, 4281, *renvoi('monit', 'redt'))

# ======================= 15 · « Any questions for us? » =======================
add(4034, 4289,
    P + "Note d'étude, pour la suite de l'échange : ces détecteurs ne lisent pas les activations — ce sont des modèles fine-tunés par LoRA "
        "pour répondre à une question d'auto-rapport sur un transcript (fiche 7 ; explication du 2 octobre, partie 2) — ; si l'on te répond sur "
        "les signaux internes, ne transfère pas leurs chiffres aux sondes. Parade, pour une sonde : une validation croisée par types tenus à "
        "part, et le test causal à dégradation appariée, avec un cas connu au même réglage (fiche 7).",
    P + "Study note, for the rest of the exchange: these detectors do not read activations — they are models fine-tuned with LoRA to answer a "
        "self-report question about a transcript (reading sheet 7; explanation of 2 October, part 2) —; if the answer turns to internal "
        "signals, do not transfer their numbers to probes. Workaround, for a probe: cross-validation by held-out types, and the causal test at "
        "matched degradation, with a known case at the same setting (reading sheet 7).")
add(4034, 4289, *renvoi('detect'))

# ======================= 16 · « Explain the law… » =======================
add(4058, 4323, *renvoi('juge', 'tenu'))

# ======================= 18 · « What's the number you're least sure of? » =======================
add(4077, 4346,
    P + "Ce que la réponse tait : le contrôle du dommage — les contrôles aléatoires du protocole d'origine n'écartent pas le dommage, et un "
        "témoin de même norme ne serait que le nul de spécificité (cours, volet 6, §2 ; cours, volet M, M4). Parade : dans le run frais au "
        "texte complet, des sous-espaces aléatoires de même rang comparés à dégradation appariée, par une courbe de l'effet contre la "
        "dégradation, et le sous-espace extrait sur un jeu d'items disjoint (cours, volet M, M4 ; programme, partie 7 ; README du dépôt).",
    P + "What the answer leaves out: the damage control — the random controls of the original protocol do not rule out damage, and a "
        "matched-norm control would be only the specificity null (course, Part 6, §2; course, Part M, M4). Workaround: in the fresh full-text "
        "run, random subspaces of the same rank compared at matched degradation, through a curve of effect against degradation, and the subspace "
        "extracted on a disjoint item set (course, Part M, M4; programme, part 7; repository README).")
add(4077, 4346, *renvoi('abl', 'degr', 'cas', 'juge'))

# ======================= 19 · « A model behaves differently when it believes it is being tested… » =======================
add(4100, 4373,
    P + "Écarter le dommage n'établit pas la spécificité : à la force de Fable 5, la dégradation est négligeable, mais sur l'axe du "
        "désalignement les contrôles restent « comparable or smaller », et comparable n'est pas moindre (fiche 2) ; et les jugements de "
        "dégradation se contredisent d'une carte à l'autre (fiches, partie B). Parade : des sous-espaces aléatoires de même rang à dégradation "
        "appariée, une baseline de prompt, et une courbe dose-réponse contre plusieurs témoins, celle du concept devant passer au-dessus à "
        "chaque niveau de dommage, la dégradation mesurée dans ton propre dispositif (fiche 2 ; cours, volet 2, §C, K47 ; cours, volet M, M4).",
    P + "Ruling out damage does not establish specificity: at the Fable 5 strength, degradation is negligible, yet on the misalignment axis the "
        "controls remain \"comparable or smaller\", and comparable is not smaller (reading sheet 2); and degradation judgements contradict each "
        "other from one card to another (reading sheets, part B). Workaround: random subspaces of the same rank at matched degradation, a prompt "
        "baseline, and a dose-response curve against several controls, the concept's curve having to run above at every level of damage, with "
        "degradation measured in your own setup (reading sheet 2; course, Part 2, §C, K47; course, Part M, M4).")
add(4100, 4373,
    P + "La mesure de la conscience d'évaluation a ses propres limites : ses mesures (sonde, NLA, question de suivi) ne sont que faiblement "
        "corrélées, la verbalisation rate la conscience non verbalisée, et l'inhibition peut faire taire la verbalisation sans toucher la "
        "représentation — des directions aléatoires la font baisser aussi (fiche 2 ; cours, volet 7, F·25 ; programme, partie 8). Parade : "
        "trianguler — sonde interne, rapport verbal, comportement entre une version réaliste et une version manifeste —, garder un critère "
        "principal comportemental avec une sonde latente comme contrôle, et valider la sonde sur un organisme conditionné à l'évaluation "
        "(cours, volet 5, sujet 4 ; programme, partie 8 ; explication du 2 octobre, partie 3).",
    P + "Measuring evaluation awareness has its own limits: its measures (probe, NLA, follow-up question) are only weakly correlated, "
        "verbalization misses unverbalized awareness, and inhibition can silence verbalization without touching the representation — random "
        "directions lower it too (reading sheet 2; course, Part 7, F·25; programme, part 8). Workaround: triangulate — internal probe, verbal "
        "report, behaviour between a realistic and an obvious version —, keep a behavioural main criterion with a latent probe as a control, and "
        "validate the probe on an evaluation-conditioned organism (course, Part 5, topic 4; programme, part 8; explanation of 2 October, part 3).")
add(4100, 4373, *renvoi('pilot', 'alea', 'degr', 'evals', 'sonde', 'jlens', 'cot_verb'))

# ======================= 20 · « Suppose you must deploy a capable model you cannot fully trust… » =======================
add(4116, 4390,
    P + "Ces taux de sabotage valent pour l'équipe rouge supposée : sur ces mêmes environnements, un échafaudage d'attaque optimisé composante "
        "par composante fait chuter le score de sûreté (cours, volet 7, F·24) ; et les attaques du banc des angles morts sont conçues à la main, "
        "en transcriptions synthétiques dont le réalisme reste ouvert (cours, volet 7, F·23). Parade : dire quelle équipe rouge un chiffre "
        "suppose — au moins une optimisée composante par composante, avec l'ablation de chaque composante — et calibrer le seuil sur des "
        "variantes bénignes appariées (cours, volet 7, F·24 et F·23) ; pour le réalisme des transcriptions, aucune parade établie ; on le dit "
        "(cours, volet 7, F·23).",
    P + "These sabotage rates hold for the red team assumed: on those same environments, an attack scaffold optimized component by component "
        "brings the safety score down sharply (course, Part 7, F·24); and the blind-spot benchmark's attacks are hand-designed, as synthetic "
        "transcripts whose realism remains open (course, Part 7, F·23). Workaround: say which red team a number assumes — at least one optimized "
        "component by component, with each component ablated — and calibrate the threshold on paired benign variants (course, Part 7, F·24 and "
        "F·23); for the realism of the transcripts, no established workaround; say so (course, Part 7, F·23).")
add(4127, 4400,
    P + "La réserve dite ici a un pendant en production : une sonde peut y échouer en silence, et son silence n'est pas celui du modèle "
        "(cours, volet 3, §3, K70). Parade : des canaris — des positifs connus glissés dans le trafic —, un score de dérive, un échantillon "
        "frais jugé chaque mois, et une sonde neuve après tout entraînement (cours, volet 3, §3, K70 ; passation, §5.2).",
    P + "The caveat stated here has a production counterpart: a probe can fail silently there, and its silence is not the model's (course, "
        "Part 3, §3, K70). Workaround: canaries — known positives slipped into the traffic —, a drift score, a fresh sample judged every month, "
        "and a fresh probe after any training (course, Part 3, §3, K70; handover, §5.2).")
add(4127, 4400, *renvoi('monit', 'sonde', 'redt', 'enc_23'))


# --- assemblage et contrôles --------------------------------------------------------
def unique(fi, lignes, s):
    a, b = TR[fi]
    return sum(1 for i in range(a - 1, b) if lignes[i].strip() == s.strip())


out = []
for lfr, len_, tfr, ten in ENTREES:
    afr, aen = FR[lfr - 1], EN[len_ - 1]
    assert afr.strip() and aen.strip(), (lfr, len_)
    assert unique('FR', FR, afr) == 1, ('FR', lfr, afr)
    assert unique('EN', EN, aen) == 1, ('EN', len_, aen)
    out.append({'fichier': 'FR', 'ancre': afr, 'texte': tfr})
    out.append({'fichier': 'EN', 'ancre': aen, 'texte': ten})

json.dump({'tranche': 'volet11_1_a_20', 'insertions': out},
          open(f'{W}/travail/insertions_volet11_1_a_20.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(f'{len(out)} insertions ({len(ENTREES)} paires) écrites.')
