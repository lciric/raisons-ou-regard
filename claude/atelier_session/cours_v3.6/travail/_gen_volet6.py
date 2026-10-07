#!/usr/bin/env python3
"""Génère travail/insertions_volet6.json (volet 6, compléments de septembre).

Chaque insertion est donnée par le numéro de ligne de la v3.5 de son ancre ; la ligne exacte est relue dans la source
et son unicité dans la tranche est vérifiée (comparaison après suppression des espaces de début et de fin, comme appliquer.py).
"""
import json, os

W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = {'FR': f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md', 'EN': f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md'}
TR = {'FR': (1369, 1626), 'EN': (1564, 1791)}
L = {k: open(v, encoding='utf8').read().split('\n') for k, v in SRC.items()}

ref = json.load(open(f'{W}/travail/referentiel_instruments.json', encoding='utf8'))
juges = {i['fichier']: i['texte'] for i in ref['insertions_pretes']['volet6']}
enc = json.load(open(f'{W}/travail/encadre_explication.json', encoding='utf8'))['insertions']
m4 = {i['fichier']: i['texte'] for i in enc if i['morceau'] == 4}

# ---------------------------------------------------------------- textes
T = {}

# §2 — loi de déplacement : lecture dans les activations
T['p1_lecture'] = (
"> ⚠ *(v3.6)* Que la destination « se lise dans les activations » dit qu'elle y est lisible, pas que le modèle s'en sert : la direction que lit ta sonde fait moins de 1 % du travail causal (cours, volet 6, §2) ; et le passage ne dit pas si ce R² vient d'items exclus de l'ajustement, alors que les métriques de sonde de ton dépôt étaient d'ajustement, et que son ρ peut l'être aussi (README du dépôt). Parade : scorer des items exclus de l'ajustement et extraire sur un jeu disjoint (README du dépôt) ; pour conclure que le modèle s'en sert, le test causal — faire plus que des directions aléatoires de même norme (le nul de spécificité), puis plus que des témoins à dégradation appariée (le dommage) (passation, §5.2 ; cours, volet M, M4).",
"> ⚠ *(v3.6)* That the destination \"can be read in the activations\" says it is readable there, not that the model uses it: the direction your probe reads does under 1% of the causal work (course, Part 6, §2); and the passage does not say whether this R² comes from items excluded from the fit, whereas your repository's probe metrics were training fit, and its ρ may be too (repository README). Workaround: score items excluded from the fit and extract on a disjoint set (repository README); to conclude that the model uses it, the causal test — do more than matched-norm random directions (the specificity null), then more than controls at matched degradation (the damage) (handover, §5.2; course, Part M, M4).")

# §2 — le causal : doses appariées, plafond de l'état complet
T['p2_doses'] = (
"> ⚠ *(v3.6)* « À doses appariées » n'est pas « à dégradation appariée » : à dose égale, une direction concurrente et la tienne n'abîment pas forcément autant le modèle, si bien que ces deux rapports de sélectivité ne sont pas lus à dommage égal ; et le patch de l'état complet aux mêmes sites est un plafond, pas une explication (cours, volet M, M4 ; programme, parties 7 et 8). Parade : refaire la comparaison des deux directions nommées à dégradation appariée, en courbes de l'effet contre la dégradation, et ne comparer qu'aux réglages qu'un témoin peut apparier, en le disant (programme, partie 7).",
"> ⚠ *(v3.6)* \"At matched doses\" is not \"at matched degradation\": at equal dose, a competing direction and yours need not damage the model equally, so these two selectivity ratios are not read at equal damage; and patching the full state at the same sites is a ceiling, not an explanation (course, Part M, M4; programme, parts 7 and 8). Workaround: redo the comparison of the two named directions at matched degradation, as curves of effect against degradation, comparing only at settings a control can match, and saying so (programme, part 7).")

# §2 — le rang 1 : un nul sans cas connu
T['rang1_nul'] = (
"> ⚠ *(v3.6)* Ce nul de rang un est dit avec sa puissance, pas avec son cas connu : sans un concept qui cède au rang un dans le même appareil, au même réglage, il ne départage pas « concept réparti » et « appareil aveugle à ce réglage » (fiche 7 ; cours, volet M, M5) ; les autres méthodes de rang un sont rapportées sans chiffres, leurs sorties brutes n'ayant pas été conservées, et l'échec du blocage (clamping) de traits du SAE ne sépare pas « traits absents du dictionnaire » de « dictionnaire qui perd trop » (README du dépôt). Parade : un cas connu au même réglage — un vecteur de pays, qui s'échange dans l'article sur l'espace de travail — et un balayage de rang dans une même expérience, sur des sous-espaces emboîtés (cours, volet 2, §C, K47 ; cours, volet 6, §6) ; pour le SAE, aucune parade connue, on le dit ; et l'on dit une borne, jamais une absence (README du dépôt ; cours, volet M, M5).",
"> ⚠ *(v3.6)* This rank-one null is stated with its power, not with its known case: without a concept that gives way at rank one in the same apparatus, at the same setting, it does not separate \"distributed concept\" from \"apparatus blind at this setting\" (reading sheet 7; course, Part M, M5); the other rank-one methods are reported without numbers, their raw outputs not having been preserved, and the failure of SAE feature clamping does not separate \"features absent from the dictionary\" from \"dictionary too lossy\" (repository README). Workaround: a known case at the same setting — a country vector, which swaps in the workspace paper — and a rank sweep within one experiment, on nested subspaces (course, Part 2, §C, K47; course, Part 6, §6); for the SAE, none known, say so; and state a bound, never an absence (repository README; course, Part M, M5).")

# §2 — la réplication : nul gouverné sans cas connu
T['replication_nul'] = (
"> ⚠ *(v3.6)* Une puissance élevée ne remplace pas un cas connu : ce nul sur générations fraîches se dit comme une borne, avec son budget et sa puissance, pas comme l'absence de tout effet (cours, volet M, M5). Parade : valider le même protocole — générations fraîches à graines appariées, réponse entière jugée et gardée en texte complet — sur un cas connu, au même réglage et au même seuil, avant de lire son silence (cours, volet M, M5 ; fiche 7 ; cours, volet 6, §6 ; README du dépôt).",
"> ⚠ *(v3.6)* High power does not replace a known case: this null on fresh generations is stated as a bound, with its budget and power, not as the absence of any effect (course, Part M, M5). Workaround: validate the same protocol — fresh seed-matched generations, the whole answer judged and kept as full text — on a known case, at the same setting and threshold, before reading its silence (course, Part M, M5; reading sheet 7; course, Part 6, §6; repository README).")

# §2 — renvoi de section
T['renvoi_s2'] = (
"> ⚠ **Limites et parades** : ablation et projection → volet 2, §D (après « La méthode ») ; patching → volet 10, fiche Patchscopes ; contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity ; cas connu → volet M, M5 (fin de section) *(v3.6)*",
"> ⚠ **Limits and workarounds**: ablation and projection → Part 2, §D (after \"The method\"); patching → Part 10, Patchscopes sheet; random controls → Part M, M4 (after \"The matched-norm random direction\"); matched degradation and dose-response → Part M, M4 (after \"Dose-response\"); activation probes → Part 2, §C (after \"In practice — The Geometry of Truth\"); steering vectors → Part 2, §C (after \"In practice — Contrastive Activation Addition\"); dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity; known case → Part M, M5 (end of section) *(v3.6)*")

# §3 — les trois contrôles : aucun n'écarte le dommage
T['s3_controles'] = (
"> ⚠ *(v3.6)* Aucun de ces trois contrôles n'écarte le dommage : l'aléatoire, apparié en norme ou en covariance, n'est que le nul de spécificité, et les directions concurrentes sont comparées à doses appariées, pas à dégradation égale (cours, volet M, M4 ; programme, partie 7 ; cours, volet 6, §2). Parade : un quatrième contrôle, à dégradation appariée — plusieurs familles de témoins au même rang, dont au moins vingt sous-espaces aléatoires, en courbes de l'effet contre la dégradation, rapportées contre leur médiane et leur 95e centile (programme, parties 3 et 7).",
"> ⚠ *(v3.6)* None of these three controls rules out damage: the random one, norm-matched or covariance-matched, is only the specificity null, and the competing directions are compared at matched doses, not at equal degradation (course, Part M, M4; programme, part 7; course, Part 6, §2). Workaround: a fourth control, at matched degradation — several families of controls at the same rank, including at least twenty random subspaces, as curves of effect against degradation, reported against their median and 95th percentile (programme, parts 3 and 7).")

T['renvoi_s3'] = (
"> ⚠ **Limites et parades** : contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») *(v3.6)*",
"> ⚠ **Limits and workarounds**: random controls → Part M, M4 (after \"The matched-norm random direction\"); matched degradation and dose-response → Part M, M4 (after \"Dose-response\") *(v3.6)*")

# §5 — carte des travaux Fellows
T['s5_sandbagging'] = (
"> ⚠ *(v3.6)* Le 91/85/94 % de Ryd ne tient, selon la limite écrite des auteurs, que si l'entraînement est indistinguable du déploiement : un modèle qui les distingue échappe (cours, volet 7, F·26). Parade : aucune connue ; on le dit.",
"> ⚠ *(v3.6)* Ryd's 91/85/94% holds, by the authors' written limit, only if training is indistinguishable from deployment: a model that tells them apart escapes (course, Part 7, F·26). Workaround: none known; say so.")

T['s5_audit'] = (
"> ⚠ *(v3.6)* Le nul de CHIVE est mesuré en lecture seule, avec des étiquettes passées par un classifieur LLM non validé contre des humains (cours, volet 7, F·30) ; et pour les adaptateurs d'introspection, rapport ou reconstruction plausible reste ouvert (cours, volet 7, F·28). Parade : pour un outil de lecture, battre la boîte noire sur des éditions qui dissocient la surface de la variable interne, et borner l'erreur des étiquettes par un audit humain (fiche 4 ; programme, partie 3) ; pour un auto-rapport, modifier l'état interne contre une direction aléatoire à dégradation appariée, et voir si le rapport suit (fiche 11 ; cours, volet 7, F·28).",
"> ⚠ *(v3.6)* CHIVE's null is measured read-only, with labels that go through an LLM classifier not validated against humans (course, Part 7, F·30); and for introspection adapters, report or plausible reconstruction remains open (course, Part 7, F·28). Workaround: for a reading tool, beat the black box on edits that dissociate surface features from the internal variable, and bound label error with a human audit (reading sheet 4; programme, part 3); for a self-report, modify the internal state against a random direction at matched degradation, and see whether the report follows (reading sheet 11; course, Part 7, F·28).")

T['s5_traits'] = (
"> ⚠ *(v3.6)* Deux de ces résultats ont une portée étroite : les vecteurs de persona supposent le trait nommé d'avance, et le lien entre déplacement et trait n'y est que corrélationnel (fiche 8) ; le masquage sélectif des gradients n'est montré que sur de petits modèles (cours, volet 2, §I, JB10). Parade : pour la causalité d'un vecteur, le test à dégradation appariée (cours, volet M, M4) ; pour l'extraction supervisée et pour l'échelle, aucune parade connue ; on le dit.",
"> ⚠ *(v3.6)* Two of these results have a narrow reach: persona vectors assume the trait is named in advance, and the shift-to-trait link there is only correlational (reading sheet 8); selective gradient masking is shown only on small models (course, Part 2, §I, JB10). Workaround: for a vector's causality, the matched-degradation test (course, Part M, M4); for supervised extraction and for scale, none known; say so.")

T['s5_agents'] = (
"> ⚠ *(v3.6)* Le 96 % vient d'un stress-test délibéré, où l'action nuisible est la seule voie, et les auteurs ne connaissent aucun cas en déploiement réel ; le 68 → 5 % de Model Spec Midtraining est mesuré sur la même évaluation (cours, volet 7, F·38) ; et un modèle peut remarquer le test et se retenir (fiche 13). Parade : deux versions d'un environnement, tirées au hasard, qui ne diffèrent que par des indices de réalisme notés par un discriminateur, avec un organisme dressé à se cacher comme cas connu (cours, volet 2, §B, K63) ; contre un pot de miel que le modèle lit comme factice, aucune parade connue ; on le dit (fiche 3).",
"> ⚠ *(v3.6)* The 96% comes from a deliberate stress test, where the harmful action is the only path, and the authors know of no instance in real deployments; Model Spec Midtraining's 68 → 5% is measured on the same evaluation (course, Part 7, F·38); and a model can notice the test and hold back (reading sheet 13). Workaround: two versions of an environment, randomly assigned, differing only in realism cues scored by a discriminator, with an organism trained to hide as the known case (course, Part 2, §B, K63); against a honeypot the model reads as fake, none known; say so (reading sheet 3).")

T['renvoi_s5'] = (
"> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; auto-rapport et introspection → volet 5, partie II, A, sujet 13 ; détecteurs fine-tunés → volet 7, F·29 ; oracles d'activation → volet 10, fiche LatentQA ; autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle ; dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») ; généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») ; juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*",
"> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after \"In practice — coup probes\"); red-teaming → Part 2, §H (after \"In practice — StrongREJECT\"); behavioural evaluations and honeypots → Part 2, §B (after \"In practice — sandbagging\"); model organisms → Part 2, §A (after \"In practice — Auditing Hidden Objectives\"); self-report and introspection → Part 5, Section II, A, Topic 13; fine-tuned detectors → Part 7, F·29; activation oracles → Part 10, LatentQA sheet; natural-language autoencoders → Part 4, The recent wave on model cognition; dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity; steering vectors → Part 2, §C (after \"In practice — Contrastive Activation Addition\"); unlearning and re-elicitation → Part 2, §I (after \"In practice — unlearning put to the test\"); weak-to-strong generalization → Part 2, §F (after \"In practice — automation\"); LLM judges → Part 6, §2 (after \"The displacement law\") *(v3.6)*")

# §6 — programme
T['renvoi_s6'] = (
"> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; J-lens et espace de travail → volet 2, C bis (après « Le test, tel qu'il se dit ») ; ablation et projection → volet 2, §D (après « La méthode ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; patching → volet 10, fiche Patchscopes *(v3.6)*",
"> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after \"In practice — coup probes\"); J-lens and workspace → Part 2, C bis (after \"The test, as it is said\"); ablation and projection → Part 2, §D (after \"The method\"); activation probes → Part 2, §C (after \"In practice — The Geometry of Truth\"); random controls → Part M, M4 (after \"The matched-norm random direction\"); matched degradation and dose-response → Part M, M4 (after \"Dose-response\"); patching → Part 10, Patchscopes sheet *(v3.6)*")

T['s6_jlens'] = (
"> ⚠ *(v3.6)* Le jacobien ne dispense pas du test causal : le lens ne capture l'espace de travail que « only approximately and incompletely », pour des concepts d'un seul token, la présence n'y est pas la cause — le langage y est présent sur quatre tâches, causal sur deux —, et il n'a été montré que sur Claude (fiche 1). Parade : la porte du lens — reproduire d'abord sur Llama l'échange d'un concept d'un seul token, sinon un tuned lens déclaré comme approximation, et la thèse n'est pas testée au sens de l'article (programme, parties 3 et 8) ; un rapport non vérifié trouve d'ailleurs des échanges bien plus faibles sur des modèles ouverts (rapport d'antériorité 5 du 2 octobre — rapport, lu par résumé).",
"> ⚠ *(v3.6)* The Jacobian does not exempt the lens from the causal test: it captures the workspace \"only approximately and incompletely\", for single-token concepts, presence there is not cause — language is present on four tasks, causal on two —, and it has been shown only on Claude (reading sheet 1). Workaround: the lens gate — first reproduce on Llama the swap of a single-token concept, otherwise a tuned lens declared as an approximation, and the thesis is not tested in the paper's sense (programme, parts 3 and 8); an unverified report also finds much weaker swaps on open models (prior-art report 5 of 2 October — report, read through a summary).")

# §7 — ce que ces compléments changent
T['s7_portee'] = (
"> ⚠ *(v3.6)* Ce « moins de 1 % » vient d'un seul modèle, Llama 3.1 8B Instruct, et de la seule complaisance d'opinion, en un tour (README du dépôt) : il relativise les sondes et le pilotage (volet 2, §C) sur ce cas, pas en général. Parade : la même partition sur d'autres concepts, puis sur un second modèle (cours, volet 6, §6).",
"> ⚠ *(v3.6)* This \"less than 1%\" comes from a single model, Llama 3.1 8B Instruct, and from opinion sycophancy alone, single-turn (repository README): it puts probes and steering (Part 2, §C) in perspective on this case, not in general. Workaround: the same partition on other concepts, then on a second model (course, Part 6, §6).")

# §8 — validité hors distribution
T['s8_etiquettes'] = (
"> ⚠ *(v3.6)* Les étiquettes de Hopkins et Khullar passent par un juge GPT-5, et environ 25 % ont été révisées à la passe de nettoyage (fiche 7). Parade : dire « révisées », pas « inversées », et garder pour mesure l'écart entre l'AUROC en distribution et l'AUROC sur des types tenus à part (fiche 7) ; dans ton propre dispositif, borner l'erreur du juge par un audit humain stratifié (programme, partie 3).",
"> ⚠ *(v3.6)* Hopkins and Khullar's labels go through a GPT-5 judge, and about 25% were revised at the cleaning pass (reading sheet 7). Workaround: say \"revised\", not \"flipped\", and keep as the measure the gap between in-distribution AUROC and AUROC on held-out types (reading sheet 7); in your own setup, bound judge error with a stratified human audit (programme, part 3).")

T['s8_famille2'] = (
"> ⚠ *(v3.6)* Le silence de la sonde sur la famille 2, celle du fine-tuning léger, ne désigne « la trace de la consigne » que si cette famille porte bien l'intention : l'implant par fine-tuning peut rater (cours, volet 2, §E, K52), et l'organisme conditionné à l'évaluation de la fiche 10 ne suit sa règle qu'en partie (fiche 10). Parade : vérifier chaque copie par son comportement (cours, volet 2, §A, K71), l'étiqueter par des contrôles programmés et un juge scellé, jamais par la sonde (passation, §5.1 et §5.2), et ne lire un silence qu'une fois la sensibilité de la sonde mesurée sur un organisme où l'on a mis l'intention soi-même : il devient alors une borne (passation, §5.2).",
"> ⚠ *(v3.6)* The probe's silence on family 2, the light fine-tune, points to \"the trace of the instruction\" only if that family does carry the intent: the fine-tuned implant can fail (course, Part 2, §E, K52), and the evaluation-conditioned organism of reading sheet 10 follows its rule only in part (reading sheet 10). Workaround: check each copy by its behaviour (course, Part 2, §A, K71), label it by programmed checks and a sealed judge, never by the probe (handover, §5.1 and §5.2), and read a silence only once the probe's sensitivity has been measured on an organism in which you installed the intent yourself: it then becomes a bound (handover, §5.2).")

T['s8_lens'] = (
"> ⚠ *(v3.6)* Un effet porté par le seul reste peut aussi venir de ce que le lens manque — il ne capture l'espace de travail que « only approximately and incompletely », et pour des concepts d'un seul token (fiche 1) —, et le lens dépend des poids, or la famille 2 est fine-tunée, contrairement à la famille 1 (cours, volet 2, C bis ; cours, volet 6, §8). Parade : recalculer le lens sur chaque organisme fine-tuné, et lire le concept sur un jeu de tokens ou par l'extension multi-token de l'annexe, en disant laquelle (cours, volet 2, C bis ; programme, partie 3).",
"> ⚠ *(v3.6)* An effect carried by the remainder alone may also come from what the lens misses — it captures the workspace \"only approximately and incompletely\", and for single-token concepts (reading sheet 1) —, and the lens depends on the weights, while family 2 is fine-tuned, unlike family 1 (course, Part 2, C bis; course, Part 6, §8). Workaround: recompute the lens on each fine-tuned organism, and read the concept on a token set or through the appendix's multi-token extension, saying which (course, Part 2, C bis; programme, part 3).")

T['s8_couche'] = (
"> ⚠ *(v3.6)* « Une sonde par couche » oblige à choisir une couche, et « s'allume » suppose un seuil : choisis sur les données du test, ils le contaminent (cours, volet 2, C bis ; README du dépôt). Parade : choisir la couche par l'AUROC sur un jeu de validation, jamais sur celui du test, avec des jeux d'indices disjoints, et fixer le seuil d'avance, le même que celui où le cas connu a été validé (programme, partie 3 ; cours, volet M, M5 ; fiche 7).",
"> ⚠ *(v3.6)* \"One probe per layer\" forces a choice of layer, and \"fires\" assumes a threshold: chosen on the test data, they contaminate it (course, Part 2, C bis; repository README). Workaround: choose the layer by AUROC on a validation set, never on the test set, with disjoint cue sets, and fix the threshold in advance, the same one at which the known case was validated (programme, part 3; course, Part M, M5; reading sheet 7).")

T['renvoi_s8'] = (
"> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; détecteurs fine-tunés → volet 7, F·29 ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; cas connu → volet M, M5 (fin de section) ; J-lens et espace de travail → volet 2, C bis (après « Le test, tel qu'il se dit ») ; jeu tenu à part → volet M, M4 (après « Le jeu tenu à part ») ; patching → volet 10, fiche Patchscopes *(v3.6)*",
"> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after \"In practice — The Geometry of Truth\"); fine-tuned detectors → Part 7, F·29; model organisms → Part 2, §A (after \"In practice — Auditing Hidden Objectives\"); known case → Part M, M5 (end of section); J-lens and workspace → Part 2, C bis (after \"The test, as it is said\"); held-out set → Part M, M4 (after \"The held-out set\"); patching → Part 10, Patchscopes sheet *(v3.6)*")

# ---------------------------------------------------------------- plan : (ligne FR, ligne EN, clé ou texte), dans l'ordre d'insertion
PLAN = [
    (1418, 1583, ('juges', None)),          # encadré complet, maison : volet 6, §2, « La loi de déplacement »
    (1418, 1583, 'p1_lecture'),
    (1429, 1585, 'p2_doses'),
    (1437, 1587, 'rang1_nul'),
    (1444, 1589, 'replication_nul'),
    (1449, 1591, 'renvoi_s2'),
    (1456, 1595, 's3_controles'),
    (1456, 1595, 'renvoi_s3'),
    (1483, 1607, 's5_sandbagging'),
    (1487, 1609, 's5_audit'),
    (1492, 1611, 's5_traits'),
    (1497, 1613, 's5_agents'),
    (1497, 1613, 'renvoi_s5'),
    (1510, 1617, 'renvoi_s6'),
    (1519, 1626, 's6_jlens'),
    (1575, 1678, 's7_portee'),
    (1589, 1757, 's8_etiquettes'),
    (1603, 1771, 's8_famille2'),
    (1616, 1782, 's8_lens'),
    (1624, 1789, ('morceau4', None)),       # encadré du 2 octobre, morceau 4, mot pour mot
    (1624, 1789, 's8_couche'),
    (1624, 1789, 'renvoi_s8'),
]


def ancre(fi, n):
    a, b = TR[fi]
    assert a <= n <= b, (fi, n)
    line = L[fi][n - 1]
    k = sum(1 for i in range(a - 1, b) if L[fi][i].strip() == line.strip())
    assert line.strip() and k == 1, (fi, n, k, line[:80])
    return line


out = []
for nfr, nen, key in PLAN:
    for fi, n, idx in (('FR', nfr, 0), ('EN', nen, 1)):
        if isinstance(key, tuple):
            texte = juges[fi] if key[0] == 'juges' else m4[fi]
        else:
            texte = T[key][idx]
        out.append({'fichier': fi, 'ancre': ancre(fi, n), 'texte': texte})

# l'ancre du référentiel et celle du morceau 4 doivent être celles qu'on a relues
assert juges['FR'] and ancre('FR', 1418).strip() == next(i['ancre'] for i in ref['insertions_pretes']['volet6'] if i['fichier'] == 'FR').strip()
assert ancre('EN', 1583).strip() == next(i['ancre'] for i in ref['insertions_pretes']['volet6'] if i['fichier'] == 'EN').strip()
assert ancre('FR', 1624).strip() == next(i['ancre'] for i in enc if i['morceau'] == 4 and i['fichier'] == 'FR').strip()
assert ancre('EN', 1789).strip() == next(i['ancre'] for i in enc if i['morceau'] == 4 and i['fichier'] == 'EN').strip()

json.dump({'tranche': 'volet6', 'insertions': out}, open(f'{W}/travail/insertions_volet6.json', 'w', encoding='utf8'),
          ensure_ascii=False, indent=1)
print(len(out), 'insertions écrites')
