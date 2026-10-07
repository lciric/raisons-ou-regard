#!/usr/bin/env python3
"""Génère travail/insertions_volets8_9.json (tranche volets8_9 : volets 8 et 9).

Les ancres sont relues dans la v3.5 par numéro de ligne, puis vérifiées uniques dans la tranche
(comparaison après suppression des espaces de début et de fin, comme appliquer.py).
"""
import json, os

W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = {'FR': f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md',
       'EN': f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md'}
TR = {'FR': (2666, 2935), 'EN': (2804, 3178)}
L = {k: open(v, encoding='utf8').read().split('\n') for k, v in SRC.items()}


def ligne(fi, n, debut):
    s = L[fi][n - 1]
    assert s.strip().startswith(debut), (fi, n, s[:80])
    return s


# ---------------------------------------------------------------------------
# Renvois d'une ligne
# ---------------------------------------------------------------------------
R = {
    'eval': ("évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging »)",
             "behavioural evaluations and honeypots → Part 2, §B (after \"In practice — sandbagging\")"),
    'orga': ("organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives »)",
             "model organisms → Part 2, §A (after \"In practice — Auditing Hidden Objectives\")"),
    'juge': ("juges LLM → volet 6, §2 (après « La loi de déplacement »)",
             "LLM judges → Part 6, §2 (after \"The displacement law\")"),
    'auto': ("auto-rapport et introspection → volet 5, partie II, A, sujet 13",
             "self-report and introspection → Part 5, Section II, A, Topic 13"),
    'nla': ("autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle",
            "natural-language autoencoders → Part 4, The recent wave on model cognition"),
    'orac': ("oracles d'activation → volet 10, fiche LatentQA",
             "activation oracles → Part 10, LatentQA sheet"),
    'patch': ("patching → volet 10, fiche Patchscopes",
              "patching → Part 10, Patchscopes sheet"),
    'pilot': ("pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition »)",
              "steering vectors → Part 2, §C (after \"In practice — Contrastive Activation Addition\")"),
    'cot': ("chaîne de pensée comme moniteur → volet 11, réponse 43",
            "chain of thought as a monitor → Part 11, answer 43"),
    'moni': ("moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes »)",
             "control monitors → Part 2, §G (after \"In practice — coup probes\")"),
    'sonde': ("sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth »)",
              "activation probes → Part 2, §C (after \"In practice — The Geometry of Truth\")"),
    'detec': ("détecteurs fine-tunés → volet 7, F·29",
              "fine-tuned detectors → Part 7, F·29"),
    'debat': ("débat et supervision évolutive → volet 2, §E (après « En pratique — Debate »)",
              "debate and scalable oversight → Part 2, §E (after \"In practice — Debate\")"),
    'w2s': ("généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation »)",
            "weak-to-strong generalization → Part 2, §F (after \"In practice — automation\")"),
    'elic': ("élicitation non supervisée → volet 2, §E (fin du cas d'application K52)",
             "unsupervised elicitation → Part 2, §E (end of worked case K52)"),
    'red': ("red-teaming → volet 2, §H (après « En pratique — StrongREJECT »)",
            "red-teaming → Part 2, §H (after \"In practice — StrongREJECT\")"),
    'classif': ("classifieurs de sûreté → volet 2, §H (fin du cas d'application G1)",
                "safety classifiers → Part 2, §H (end of worked case G1)"),
    'desap': ("désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve »)",
              "unlearning and re-elicitation → Part 2, §I (after \"In practice — unlearning put to the test\")"),
}


def renvoi(*cles):
    fr = '> ⚠ **Limites et parades** : ' + ' ; '.join(R[c][0] for c in cles) + ' *(v3.6)*'
    en = '> ⚠ **Limits and workarounds**: ' + '; '.join(R[c][1] for c in cles) + ' *(v3.6)*'
    return fr, en


def avert(fr, en):
    return '> ⚠ *(v3.6)* ' + fr, '> ⚠ *(v3.6)* ' + en


# ---------------------------------------------------------------------------
# Les ancres (FR, EN), par section
# ---------------------------------------------------------------------------
A = {
    's2': (ligne('FR', 2761, "d'évaluation : les évals propres sous-estiment"),
           ligne('EN', 2918, "awareness: clean evals underestimate the risk")),
    's3': (ligne('FR', 2776, "une intervention — est exactement l'exemple du jeu de plateau"),
           ligne('EN', 2933, "an intervention — is exactly the board-game example")),
    's4': (ligne('FR', 2784, "est-elle celle qui le cause — ta partition."),
           ligne('EN', 2941, "the one that causes it — your partition.")),
    's5': (ligne('FR', 2796, "la version chiffrée de Lanham"),
           ligne('EN', 2953, "the quantified version of Lanham")),
    's6': (ligne('FR', 2801, "garde-fous mais pas assez pour les contourner."),
           ligne('EN', 2958, "safeguards but not capable enough to get around them.")),
    's6b': (ligne('FR', 2831, "tests the fix.*"),
            ligne('EN', 2988, "tests the fix.*")),
    's6c': (ligne('FR', 2840, "offrir si on te demande « quoi d'autre »."),
            ligne('EN', 2997, "offer if you are asked \"what else\".")),
    's7': (ligne('FR', 2844, "(experts en désaccord), les **erreurs systématiques**"),
           ligne('EN', 3001, "(experts in disagreement), **systematic errors**")),
    's7b': (ligne('FR', 2862, "modèle-juge dont tu as mesuré le déplacement"),
            ligne('EN', 3019, "model judge whose displacement you measured")),
    's7d': (ligne('FR', 2888, "qu'un prompt. Ta réponse : lire n'est pas contrôler"),
            ligne('EN', 3045, "than a prompt. Your answer: reading is not controlling")),
    's8': (ligne('FR', 2893, "d'injections de prompt pour agents) ;"),
           ligne('EN', 3050, "of prompt injections for agents);")),
    's8a': (ligne('FR', 2902, "bancs qui mesurent **ce que de vrais humains trouveraient**"),
            ligne('EN', 3059, "benchmarks that measure **what real humans would find**")),
    's8b': (ligne('FR', 2910, "quand on te demande si ton idée sert ailleurs."),
            ligne('EN', 3067, "when you are asked whether your idea is useful elsewhere.")),
    's9a': (ligne('FR', 2918, "II.20 ajoute les sondes."),
            ligne('EN', 3075, "II.20 adds the probes.")),
    's9b': (ligne('FR', 2926, "instances* » — ton H4 (poids partagés)"),
            ligne('EN', 3083, "instances*\" — your H4 (shared weights)")),
}

# ---------------------------------------------------------------------------
# Les insertions, dans l'ordre du texte
# ---------------------------------------------------------------------------
I = []  # (section, (texte FR, texte EN))

# §2 · Evaluating alignment — le sandbagging de van der Weij, puis le renvoi
I.append(('s2', avert(
    "Le sandbagging de van der Weij et al. est élicité sur commande, par prompt ou par mot de passe, et mesuré sur des QCM seulement : "
    "c'est une capacité, pas la propension spontanée que la page demande, et les auteurs écartent eux-mêmes la part "
    "stratégique (cours, volet 10, n° 05). Parade : la capacité, élicitée à budget fixé d'avance et rapportée comme "
    "une borne ; la propension, offerte sans être demandée dans deux versions d'un environnement, tirées au hasard, "
    "qui ne diffèrent que par des indices de réalisme, avec un organisme dressé à se cacher comme cas connu (cours, "
    "volet 2, §B, K63 ; cours, volet M, M7) ; les sondes, parade que les auteurs suggèrent, n'y ont pas été "
    "essayées (cours, volet 10, n° 05).",
    "Van der Weij et al.'s sandbagging is elicited on command, by prompt or by password, and measured on multiple-choice benchmarks "
    "only: it is a capability, not the spontaneous propensity the page asks about, and the authors themselves set "
    "aside the strategic part (course, Part 10, no. 05). Workaround: the capability, elicited at a budget fixed in "
    "advance and reported as a bound; the propensity, offered unasked in two versions of an environment, randomly "
    "assigned, differing only in realism cues, with an organism trained to hide as the known case (course, Part 2, "
    "§B, K63; course, Part M, M7); probes, the workaround the authors suggest, were not tried there (course, "
    "Part 10, no. 05).")))
I.append(('s2', renvoi('eval', 'orga', 'juge')))

# §3 · Understanding model cognition — le SAD, les décodeurs, puis le renvoi
I.append(('s3', avert(
    "Le quasi-hasard du SAD est un auto-rapport : il dit ce que le modèle répond quand on lui demande s'il est évalué, "
    "pas ce qu'il représente — prendre un auto-rapport pour une croyance est un piège de lecture, les mesures de "
    "la conscience d'évaluation (sonde, NLA, question de suivi) ne sont que faiblement corrélées, et chez Mythos "
    "Preview elle apparaît le plus souvent sans être verbalisée (fiches, partie B, piège 2 ; fiche 2). Parade : "
    "trianguler — une sonde interne, le rapport verbal, et le comportement entre une version réaliste et une "
    "version manifeste de la situation —, en disant laquelle fonde quel chiffre, et valider la sonde sur un cas "
    "connu, un organisme conditionné à l'évaluation (cours, volet 5, sujet 4 ; explication du 2 octobre, §3).",
    "SAD's near-chance result is a self-report: it says what the model answers when asked whether it is being "
    "evaluated, not what it represents — taking a self-report for a belief is a reading trap, the measures of "
    "evaluation awareness (probe, NLA, follow-up question) are only weakly correlated, and in Mythos Preview it "
    "mostly appears without being verbalized (reading sheets, part B, trap 2; reading sheet 2). Workaround: "
    "triangulate — an internal probe, the verbal report, and behaviour between a realistic and an obvious version "
    "of the setting —, saying which one grounds which number, and validate the probe on a known case, an "
    "evaluation-conditioned organism (course, Part 5, topic 4; explanation of 2 October, §3).")))
I.append(('s3', avert(
    "Parmi ces travaux rangés sous « introspection », LatentQA fait lire les activations par une copie fine-tunée "
    "du modèle, pas par le modèle interrogé — ce n'est pas un auto-rapport —, sans vérité-terrain des latents, si "
    "bien que le décodeur peut halluciner ; et dans Patchscopes, le calcul après le patch peut ajouter de "
    "l'information, si bien qu'un décodage réussi ne prouve pas que la représentation la porte (cours, volet 10, "
    "LatentQA ; cours, volet 10, Patchscopes). Parade : tester le décodeur sur des variantes fine-tunées à "
    "comportement connu, jamais vues, et le corroborer par une méthode indépendante (fiche 18) ; pour le patch, "
    "aucune parade connue ; on le dit.",
    "Among these works filed under \"introspection\", LatentQA has the activations read by a fine-tuned copy of "
    "the model, not by the queried model — this is not a self-report —, with no ground truth for latents, so the "
    "decoder may hallucinate; and in Patchscopes, the computation after the patch can add information, so a "
    "successful decoding does not prove that the representation carries it (course, Part 10, LatentQA; course, "
    "Part 10, Patchscopes). Workaround: test the decoder on fine-tuned variants with known behaviour, never seen "
    "before, and corroborate it with an independent method (reading sheet 18); for the patch, none known; say so.")))
I.append(('s3', renvoi('auto', 'nla', 'orac', 'patch')))

# §4 · Persona — Persona Vectors, puis le renvoi
I.append(('s4', avert(
    "« Le persona comme direction » est un résultat prédictif, pas causal : le lien entre le déplacement le long "
    "du vecteur et le trait est corrélationnel, le trait doit être nommé d'avance, les directions sont grossières, "
    "et l'évaluation est légère, un juge GPT-4.1-mini sur un seul tour (fiche 8) ; piloter contre le vecteur après "
    "coup réduit le trait mais dégrade MMLU (cours, volet 7, F·31). Parade : pour la causalité, piloter contre des "
    "directions aléatoires de même norme — le nul de spécificité —, puis contre des témoins à dégradation appariée "
    "— le dommage —, et rapporter la part du vecteur contre celle de l'état complet aux mêmes sites, ta partition "
    "(cours, volet M, M4 ; passation, §5.2 ; cours, volet 6, §2) ; pour l'extraction supervisée, aucune parade "
    "connue ; on le dit (fiche 8).",
    "\"The persona as a direction\" is a predictive result, not a causal one: the link between the shift along the "
    "vector and the trait is correlational, the trait must be named in advance, the directions are coarse, and the "
    "evaluation is light, a GPT-4.1-mini judge on a single turn (reading sheet 8); steering against the vector "
    "after the fact reduces the trait but degrades MMLU (course, Part 7, F·31). Workaround: for causality, steer "
    "against matched-norm random directions — the specificity null —, then against controls at matched "
    "degradation — the damage —, and report the vector's share against that of the full state at the same sites, "
    "your partition (course, Part M, M4; handover, §5.2; course, Part 6, §2); for supervised extraction, none "
    "known; say so (reading sheet 8).")))
I.append(('s4', renvoi('pilot', 'patch')))

# §5 · Chain-of-thought faithfulness — Lanham, puis le renvoi
I.append(('s5', avert(
    "Le résultat d'échelle de Lanham — « les grands modèles y sont paradoxalement moins fidèles » — ne vaut, dans "
    "son résumé, que « on most tasks » (cours, volet 10, n° 18) ; une chaîne de pensée tait souvent ce qui a "
    "décidé — l'indice décisif n'y est mentionné que dans 25 % (Claude 3.7 Sonnet) et 39 % (DeepSeek R1) des "
    "cas —, et ne pas verbaliser n'est pas raisonner en cachette (fiche 17). Parade : mesurer la surveillabilité "
    "comme un ratio, le verbalisé contre l'interne ou les actions, par une perturbation graduée — ta II.5 —, et "
    "dire « not verbalized », jamais « hidden reasoning » (fiche 17 ; cours, volet 11, réponse 43).",
    "Lanham's scale result — \"large models are paradoxically less faithful on it\" — holds, in its abstract, only "
    "\"on most tasks\" (course, Part 10, no. 18); a chain of thought often leaves out what decided — the decisive "
    "cue is mentioned in only 25% (Claude 3.7 Sonnet) and 39% (DeepSeek R1) of cases —, and not verbalizing is "
    "not hidden reasoning (reading sheet 17). Workaround: measure monitorability as a ratio, the verbalized "
    "against the internal or the actions, through graded perturbation — your II.5 —, and say \"not verbalized\", "
    "never \"hidden reasoning\" (reading sheet 17; course, Part 11, answer 43).")))
I.append(('s5', renvoi('cot')))

# §6 · AI control — le renvoi, à la fin de l'introduction de la section
I.append(('s6', renvoi('moni', 'sonde', 'detec')))

# §6b · Activation monitoring — deux avertissements
I.append(('s6b', avert(
    "Ni ton second résultat ni F·29 ne mesurent le décalage d'un moniteur d'activations : ton second résultat en "
    "montre un cousin, déjà en distribution, puisque la direction qu'une sonde lit n'est pas celle qui agit (cours, "
    "volet 6, §4 ; cours, volet 11, réponse 12) ; et les détecteurs de F·29 ne sont pas des sondes, mais des "
    "modèles fine-tunés par LoRA à répondre à une question d'auto-rapport sur un transcript, dont les chiffres ne "
    "se transfèrent pas aux sondes (fiche 7 ; explication du 2 octobre, §2). Parade : le test reste à faire, hors "
    "distribution — deux familles d'organismes et un témoin conscient mais honnête, des familles entières tenues "
    "à part, une sonde neuve après tout entraînement —, et, pour qu'une sonde serve à intervenir, piloter contre "
    "des directions aléatoires de même norme (le nul de spécificité), puis à dégradation appariée (le dommage) "
    "(cours, volet 6, §8 ; explication du 2 octobre, §3 ; passation, §5.2).",
    "Neither your second result nor F·29 measures the shift of an activation monitor: your second result shows a "
    "cousin of it, already in distribution, since the direction a probe reads is not the one that acts (course, "
    "Part 6, §4; course, Part 11, answer 12); and the detectors of F·29 are not probes, but models fine-tuned with LoRA "
    "to answer a self-report question about a transcript, whose numbers do not transfer to probes (reading "
    "sheet 7; explanation of 2 October, §2). Workaround: the test remains to be done, out of distribution — two "
    "organism families and an aware-but-honest control, whole held-out families, a fresh probe after any "
    "training —, and, for a probe to be used to intervene, steer against matched-norm random directions (the "
    "specificity null), then at matched degradation (the damage) (course, Part 6, §8; explanation of 2 October, "
    "§3; handover, §5.2).")))
I.append(('s6b', avert(
    "Ces « signs of life » ne mettent pas encore à l'épreuve « difficult for the model to control » : la sonde des "
    "coup probes pourrait n'apprendre que « that looks like a takeover attempt written by humans », sans moyen "
    "clair de l'écarter, et les sondes de circuit breakers sont testées contre un attaquant qui ne connaît pas la "
    "sonde et n'optimise pas contre elle (cours, volet 10, n° 27 et n° 28). Parade : éprouver la sonde contre une "
    "attaque optimisée contre elle aussi, construire ses exemples à partir des générations réelles du modèle "
    "surveillé, et garder des détecteurs scellés, hors de toute boucle d'entraînement : s'ils se déclenchent "
    "encore quand les autres se taisent, l'évasion a été sélectionnée (cours, volet 10, n° 62 ; cours, volet 2, "
    "§C ; fiche 19).",
    "These \"signs of life\" do not yet put \"difficult for the model to control\" to the test: the probe of the "
    "coup-probes post might learn only \"that looks like a takeover attempt written by humans\", with no clear way to rule it "
    "out, and the circuit-breakers probes are tested against an attacker who does not know the probe and does not "
    "optimize against it (course, Part 10, no. 27 and no. 28). Workaround: test the probe against an attack "
    "optimized against it too, build its examples from the real generations of the monitored model, and keep "
    "sealed detectors outside any training loop: if they keep firing when the others go quiet, evasion has been "
    "selected (course, Part 10, no. 62; course, Part 2, §C; reading sheet 19).")))

# §6c · Anomaly detection — les modèles « quirky »
I.append(('s6c', avert(
    "Les sondes et le détecteur d'anomalies de Mallen et al. sont validés sur des modèles fine-tunés pour se tromper quand un nom "
    "visible dans le prompt, Bob, l'annonce, et le fine-tuning a probablement écrasé une part des circuits "
    "naturels ; à transfert comparable, les directions de régression logistique y sont bien moins causales que la "
    "différence des moyennes (cours, volet 10, n° 30). Parade : sur un organisme construit, ne conclure que sur "
    "l'instrument (programme, partie 8) ; pour agir, le test causal contre des directions aléatoires de même norme "
    "(le nul de spécificité), puis à dégradation appariée (le dommage) (passation, §5.2 ; cours, volet M, M4) ; "
    "pour un modèle dont rien dans le prompt n'indique si la réponse est fiable, question que les auteurs laissent "
    "ouverte, aucune parade connue ; on le dit.",
    "Mallen et al.'s probes and anomaly detector are validated on models fine-tuned to err when a name visible in the "
    "prompt, Bob, signals it, and the fine-tuning likely overwrote part of the natural circuitry; at comparable "
    "transfer, the logistic-regression directions there are far less causal than the mean difference (course, "
    "Part 10, no. 30). Workaround: on a constructed organism, conclude only about the instrument (programme, "
    "part 8); to act, the causal test against matched-norm random directions (the specificity null), then at "
    "matched degradation (the damage) (handover, §5.2; course, Part M, M4); for a model where nothing in the "
    "prompt signals whether the answer is reliable, a question the authors leave open, none known; say so.")))

# §7 · Scalable oversight — le renvoi, à la fin de l'introduction de la section
I.append(('s7', renvoi('debat', 'w2s', 'elic', 'sonde', 'juge')))

# §7b · Recursive oversight — le débat
I.append(('s7b', avert(
    "Ces résultats de débat viennent de bancs où l'on connaît la bonne réponse, en inférence seule, avec chez "
    "Kenton des juges LLM et aucun juge humain, et ses auteurs disent ne pas voir la « Strong positive evidence » qu'ils "
    "attendaient face au QA sans article (cours, volet 10, n° 39). Parade : pour le juge, un juge scellé et un "
    "audit humain stratifié (fiches, partie B, piège 6 ; programme, partie 3) ; au-delà de l'expertise humaine, "
    "où il n'y a plus de référence, et contre l'argument obfusqué, trop complexe pour être réfuté même faux, "
    "aucune parade connue ; on le dit (cours, volet 2, §E).",
    "These debate results come from testbeds where the right answer is known, at inference only, with LLM judges "
    "and no human judge in Kenton, whose authors say they do not see the \"Strong positive evidence\" they expected against "
    "QA without the article (course, Part 10, no. 39). Workaround: for the judge, a sealed judge and a stratified "
    "human audit (reading sheets, part B, trap 6; programme, part 3); beyond human expertise, where there is no "
    "reference left, and against the obfuscated argument, too complex to refute even when false, none known; say "
    "so (course, Part 2, §E).")))

# §7d · Honesty — les sondes de vérité
I.append(('s7d', avert(
    "Ni la sonde d'Azaria et Mitchell ni celles de Liu et al. ne sont éprouvées là où la page les demande, sur un "
    "modèle qui a appris à ne pas dire vrai : chez les premiers, « lying » désigne des énoncés faux ordinaires ; "
    "chez les seconds, les deux modèles sont seulement pré-entraînés, et l'avantage de la sonde sur la sortie vient "
    "surtout de la calibration et de l'hétérogénéité (cours, volet 10, n° 51 et n° 56). Parade : juger la sonde sur "
    "des modèles rendus malhonnêtes, où l'on sait ce qu'ils cachent — le cas connu —, contre un simple prompt à "
    "coût égal : c'est là, sur une suite de modèles malhonnêtes, que les sondes de vérité ont fait moins bien qu'un "
    "prompt (cours, volet 7, F·62 ; cours, volet 5, sujet 1 ; passation, §5.2).",
    "Neither Azaria and Mitchell's probe nor Liu et al.'s probes are tested where the page asks for them, on a "
    "model that has learned not to tell the truth: in the former, \"lying\" means ordinary false statements; in "
    "the latter, both models are only pretrained, and the probe's advantage over the output comes mostly from "
    "calibration and heterogeneity (course, Part 10, no. 51 and no. 56). Workaround: judge the probe on models "
    "made dishonest, where you know what they hide — the known case —, against a plain prompt at equal cost: that "
    "is where, on a suite of dishonest models, truth probes did worse than a prompt (course, Part 7, F·62; "
    "course, Part 5, topic 1; handover, §5.2).")))

# §8 · Adversarial robustness — le renvoi, à la fin de l'introduction de la section
I.append(('s8', renvoi('red', 'classif', 'juge')))

# §8a · StrongREJECT et AgentHarm
I.append(('s8a', avert(
    "L'« utilité » de StrongREJECT est notée par un évaluateur LLM à grille, validé contre des annotateurs humains "
    "mais dont les auteurs n'ont pas testé la robustesse à l'optimisation, sur un jeu de questions trop petit, "
    "selon eux, pour une mesure définitive ; AgentHarm note des tâches plutôt faciles, sur des outils synthétiques, "
    "« proxies for harm » (cours, volet 10, n° 59 et n° 60). Parade : un juge scellé, distinct de celui contre "
    "lequel on optimise, avec un audit humain qui borne son erreur, et le préjudice différentiel noté à l'aveugle "
    "face à un bras de référence réaliste (programme, parties 3 et 8 ; cours, volet 2, §H, G1 ; cours, volet M, M4).",
    "StrongREJECT's \"usefulness\" is scored by a rubric-based LLM evaluator, validated against human annotators "
    "but whose robustness to optimization the authors did not test, on a question set too small, by their "
    "account, for a definitive measure; AgentHarm scores rather easy tasks, on synthetic tools, \"proxies for "
    "harm\" (course, Part 10, no. 59 and no. 60). Workaround: a sealed judge, distinct from the one being optimized "
    "against, with a human audit that bounds its error, and differential harm blind-scored against a realistic "
    "reference arm (programme, parts 3 and 8; course, Part 2, §H, G1; course, Part M, M4).")))

# §8b · Rapid response
I.append(('s8b', avert(
    "Le blocage de la rapid response (Peng et al.) est mesuré en taux de succès des attaques, sans attaquant qui connaisse la défense, et les auteurs "
    "le jugent peut-être inadéquat quand une seule sortie suffit à nuire (cours, volet 10, n° 63) ; un taux de "
    "blocage ne dit pas non plus ce que le filtre retire à l'attaquant (cours, volet 2, §H, G1). Parade : classer "
    "les défenses deux fois, par taux de refus et par préjudice différentiel, et les éprouver contre une attaque "
    "optimisée contre elles aussi (cours, volet 2, §H, G1 ; cours, volet 10, n° 62) ; contre l'attaquant qui "
    "apprend de la défense, aucune parade connue ; on le dit.",
    "Rapid response's blocking (Peng et al.) is measured as attack success rate, with no attacker who knows the defence, and the authors "
    "judge it possibly inadequate when a single output is enough to do harm (course, Part 10, no. 63); nor does a "
    "blocking rate say what the filter takes away from the attacker (course, Part 2, §H, G1). Workaround: rank "
    "the defences twice, by refusal rate and by differential harm, and test them against an attack optimized "
    "against them too (course, Part 2, §H, G1; course, Part 10, no. 62); against the attacker who learns from the "
    "defence, none known; say so.")))

# §9a · Unlearning
I.append(('s9a', avert(
    "Ajouter des sondes ne tranche pas, car une lecture peut ne plus rien voir d'un savoir qui reste : après RMU, "
    "le logit lens ne trouve plus rien alors que retirer une direction par couche rend 64,7 %, et des sondes "
    "échouent sur un modèle qu'on peut encore jailbreaker (cours, volet 10, n° 64 et n° 66) ; quant au masquage "
    "sélectif des gradients de SGTM, il n'est montré que sur de petits modèles (cours, volet 2, §I, JB10). "
    "Parade : trancher par une intervention, jamais par une lecture — la ré-élicitation contre une référence "
    "jamais entraînée, au même budget, avec un modèle connu pour masquer comme cas connu, et l'on dit une borne à ce "
    "budget (cours, volet 2, §I ; cours, volet M, M5) ; pour l'échelle de SGTM, aucune parade connue ; on le dit.",
    "Adding probes does not settle it, because a reading can stop seeing knowledge that remains: after RMU, the "
    "logit lens finds nothing while removing one direction per layer restores 64.7%, and probes fail on a model "
    "that can still be jailbroken (course, Part 10, no. 64 and no. 66); as for SGTM's selective gradient masking, "
    "it is shown only on small models (course, Part 2, §I, JB10). Workaround: decide by an intervention, "
    "never by a reading — re-elicitation against a never-trained reference, at the same budget, with a model "
    "known to mask as the known case, and a bound stated at this budget (course, Part 2, §I; course, Part M, "
    "M5); for SGTM's scale, none known; say so.")))

# §9b · Learned governance — AI Organizations, puis le renvoi de la section 9
I.append(('s9b', avert(
    "AI Organizations mesure ce mode dans deux organisations simulées, sur Opus 4.1, et ses auteurs écrivent "
    "que les tâches sont simulées et que le mécanisme de l'écart n'est que partiellement expliqué (cours, volet 7, F·39) ; or dans une simulation, "
    "« c'est faux » est vrai : un modèle peut lire le cadre comme factice (fiche 3). Parade : deux versions d'un "
    "environnement, tirées au hasard, qui ne diffèrent que par des indices de réalisme notés par un "
    "discriminateur, avec un organisme dressé à se cacher comme cas connu (cours, volet 2, §B, K63) ; contre un "
    "cadre que le modèle lit comme factice, aucune parade connue ; on le dit (fiche 3).",
    "AI Organizations measures this mode in two simulated organizations, on Opus 4.1, and its authors write that "
    "the tasks are simulated and the mechanism of the gap is only partially explained (course, Part 7, F·39); and in a simulation, \"this is "
    "fake\" is true: a model may read the setting as fake (reading sheet 3). Workaround: two versions of an "
    "environment, randomly assigned, differing only in realism cues scored by a discriminator, with an organism "
    "trained to hide as the known case (course, Part 2, §B, K63); against a setting the model reads as fake, none "
    "known; say so (reading sheet 3).")))
I.append(('s9b', renvoi('desap', 'sonde', 'eval', 'moni')))

# ---------------------------------------------------------------------------
# Vérifications et écriture
# ---------------------------------------------------------------------------
out = []
for sec, (fr, en) in I:
    out.append({'fichier': 'FR', 'ancre': A[sec][0], 'texte': fr})
for sec, (fr, en) in I:
    out.append({'fichier': 'EN', 'ancre': A[sec][1], 'texte': en})

for ins in out:
    fi = ins['fichier']
    a, b = TR[fi]
    n = sum(1 for i in range(a - 1, b) if L[fi][i].strip() == ins['ancre'].strip())
    assert n == 1, (fi, n, ins['ancre'][:80])

d = {'tranche': 'volets8_9', 'insertions': out}
p = f'{W}/travail/insertions_volets8_9.json'
json.dump(d, open(p, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(p, len(out), 'insertions')
