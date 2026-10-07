#!/usr/bin/env python3
"""Génère travail/insertions_volet7_A_et_C.json (volet 7, parties A et C).
Les ancres sont lues par numéro de ligne dans la v3.5, puis vérifiées uniques dans la tranche (comparaison après strip)."""
import json, os

W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = {'FR': f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md', 'EN': f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md'}
TR = {'FR': (2070, 2665), 'EN': (2204, 2803)}
L = {k: open(v, encoding='utf8').read().split('\n') for k, v in SRC.items()}

# ---------------------------------------------------------------- renvois
LOC = {
    'om':  ("organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives »)",
            'model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives")'),
    'so':  ("sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth »)",
            'activation probes → Part 2, §C (after "In practice — The Geometry of Truth")'),
    'pi':  ("pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition »)",
            'steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition")'),
    'ev':  ("évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging »)",
            'behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging")'),
    'cot': ("chaîne de pensée comme moniteur → volet 11, réponse 43",
            'chain of thought as a monitor → Part 11, answer 43'),
    'eli': ("élicitation non supervisée → volet 2, §E (fin du cas d'application K52)",
            'unsupervised elicitation → Part 2, §E (end of worked case K52)'),
    'sae': ("dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity",
            'dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity'),
    'ga':  ("graphes d'attribution → volet 4, Circuit Tracing",
            'attribution graphs → Part 4, Circuit Tracing'),
    'mo':  ("moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes »)",
            'control monitors → Part 2, §G (after "In practice — coup probes")'),
    'rt':  ("red-teaming → volet 2, §H (après « En pratique — StrongREJECT »)",
            'red-teaming → Part 2, §H (after "In practice — StrongREJECT")'),
    'deb': ("débat et supervision évolutive → volet 2, §E (après « En pratique — Debate »)",
            'debate and scalable oversight → Part 2, §E (after "In practice — Debate")'),
    'w2s': ("généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation »)",
            'weak-to-strong generalization → Part 2, §F (after "In practice — automation")'),
    'unl': ("désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve »)",
            'unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test")'),
    'cc':  ("cas connu → volet M, M5 (fin de section)",
            'known case → Part M, M5 (end of section)'),
    'ra':  ("contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme »)",
            'random controls → Part M, M4 (after "The matched-norm random direction")'),
    'dg':  ("dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse »)",
            'matched degradation and dose-response → Part M, M4 (after "Dose-response")'),
    'abl': ("ablation et projection → volet 2, §D (après « La méthode »)",
            'ablation and projection → Part 2, §D (after "The method")'),
    'jl':  ("juges LLM → volet 6, §2 (après « La loi de déplacement »)",
            'LLM judges → Part 6, §2 (after "The displacement law")'),
    'pat': ("patching → volet 10, fiche Patchscopes",
            'patching → Part 10, Patchscopes sheet'),
    'ar':  ("auto-rapport et introspection → volet 5, partie II, A, sujet 13",
            'self-report and introspection → Part 5, Section II, A, Topic 13'),
    'ao':  ("oracles d'activation → volet 10, fiche LatentQA",
            'activation oracles → Part 10, LatentQA sheet'),
    'nla': ("autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle",
            'natural-language autoencoders → Part 4, The recent wave on model cognition'),
    'cs':  ("classifieurs de sûreté → volet 2, §H (fin du cas d'application G1)",
            'safety classifiers → Part 2, §H (end of worked case G1)'),
}


def renvoi(keys):
    fr = '> ⚠ **Limites et parades** : ' + ' ; '.join(LOC[k][0] for k in keys) + ' *(v3.6)*'
    en = '> ⚠ **Limits and workarounds**: ' + '; '.join(LOC[k][1] for k in keys) + ' *(v3.6)*'
    return fr, en


# (ligne FR, ligne EN, clés) — ancre : dernière question de la fiche (fin de liste, fin de section)
RENVOIS = [
    (2096, 2230, ['om', 'so', 'rt', 'cc']),            # F·1 Sleeper Agents
    (2122, 2256, ['ev', 'cot', 'om']),                 # F·2 Alignment Faking
    (2150, 2284, ['ev', 'jl']),                        # F·3 Sycophancy
    (2174, 2308, ['so', 'pi', 'ra', 'dg', 'pat']),     # F·4 Geometry of Truth
    (2198, 2332, ['so', 'pi']),                        # F·5 RepE
    (2222, 2356, ['eli', 'so']),                       # F·6 CCS
    (2247, 2381, ['pi', 'abl', 'dg', 'jl', 'cc']),     # F·7 CAA / ITI
    (2272, 2406, ['sae', 'pat']),                      # F·8 Monosemanticity
    (2302, 2436, ['ga', 'ar', 'ao', 'nla', 'pi']),     # F·9 Circuit Tracing + vague récente
    (2326, 2460, ['mo', 'rt']),                        # F·10 AI Control
    (2350, 2484, ['deb', 'jl']),                       # F·11 Debate
    (2374, 2508, ['w2s', 'eli']),                      # F·12 Weak-to-Strong
    (2398, 2532, ['om', 'sae']),                       # F·13 Auditing Hidden Objectives
    (2446, 2580, ['rt', 'cs']),                        # F·15 GCG
    (2470, 2604, ['jl']),                              # F·16 Constitutional AI
    (2498, 2632, ['unl', 'so', 'cc', 'pi']),           # F·17 Unlearning (+ clôture du volet 4)
    (2520, 2652, ['so', 'mo']),                        # F·50 Goldowsky-Dill
    (2538, 2670, ['so', 'mo', 'rt']),                  # F·51 McKenzie
    (2556, 2688, ['mo', 'so']),                        # F·52 NARCBench
    (2573, 2705, ['mo', 'so', 'cc']),                  # F·53 Das et al.
    (2591, 2723, ['mo', 'so']),                        # F·54 TRACE / TRACES
    (2608, 2740, ['mo']),                              # F·55 E-valuator
    (2627, 2759, ['mo', 'rt']),                        # F·56 FakeLab / Hills / Brown
    (2644, 2776, ['ev', 'mo', 'rt', 'so']),            # F·57 Balesni / SHADE-Arena
]

# ---------------------------------------------------------------- avertissements ponctuels
AV = [
    # F·1 — sondes de défection (avertissement prêt du référentiel, parade ajoutée)
    (2080, 2214,
     "> ⚠ *(v3.6)* Ces sondes ont été validées sur une porte implantée : la meilleure de 1 000 directions aléatoires y atteint déjà 95,3 %, et la saillance pourrait venir de l'insertion (fiche 15) ; un succès sur organisme est un cas connu de l'instrument, pas une preuve sur le cas naturel (cours, volet M, M5). Parade, en partie : planter le même comportement par plusieurs recettes, en tenir une à part, et ajouter l'organisme d'une autre équipe (cours, volet 2, §A, K71) ; pour conclure sur le cas naturel, aucune parade connue ; on le dit.",
     "> ⚠ *(v3.6)* These probes were validated on an implanted backdoor: the best of 1,000 random directions already reaches 95.3% there, and salience might come from the insertion (reading sheet 15); a success on an organism is a known case for the instrument, not proof about the natural case (course, Part M, M5). Workaround, in part: plant the same behaviour through several recipes, hold one out, and add another team's organism (course, Part 2, §A, K71); to conclude about the natural case, none known; say so."),
    # F·2 — le bloc-notes comme moniteur
    (2106, 2240,
     "> ⚠ *(v3.6)* Le motif se lit dans un bloc-notes, qui n'est pas le raisonnement opaque, et le papier ne fait pas de ce raisonnement la cause de la conformité (fiche 14) ; une chaîne de pensée tait souvent ce qui a décidé (fiche 17), et une réplication sur un modèle récent peut mesurer la mémorisation du scénario, ces transcripts ayant été réinclus dans l'entraînement (fiches, partie C). Parade : prendre pour mesure l'écart de conformité entre les deux conditions, et retirer l'indice lisible tout en détectant la préservation de buts, avec un organisme conscient mais honnête comme témoin (fiche 14 ; cours, volet 6, §8) ; contre la mémorisation, aucune parade connue ; on le dit.",
     "> ⚠ *(v3.6)* The motive is read in a scratchpad, which is not the opaque reasoning, and the paper does not make that reasoning the cause of compliance (reading sheet 14); a chain of thought often leaves out what decided (reading sheet 17), and a replication on a recent model may measure memorization of the scenario, these transcripts having been re-included in training (reading sheets, part C). Workaround: take as the measure the compliance gap between the two conditions, and remove the readable cue while still detecting goal preservation, with an aware-but-honest organism as the control (reading sheet 14; course, Part 6, §8); against memorization, none known; say so."),
    # F·4 — intervention le long de la direction (avertissement prêt ; ancre déplacée en fin de liste)
    (2159, 2293,
     "> ⚠ *(v3.6)* « L'intervention change le comportement » ne dit le concept qu'à dégradation appariée : une direction aléatoire de même norme n'en est que le nul de spécificité (fiches, partie B, piège 4 ; cours, volet M, M4). Parade : une courbe dose-réponse contre plusieurs témoins, la courbe du concept devant passer au-dessus à chaque niveau de dommage (cours, volet 2, §C, K47).",
     "> ⚠ *(v3.6)* \"Intervention changes behaviour\" shows the concept only at matched degradation: a matched-norm random direction is only its specificity null (reading sheets, part B, trap 4; course, Part M, M4). Workaround: a dose-response curve against several controls, the concept's curve having to run above them at every level of damage (course, Part 2, §C, K47)."),
    # F·4 — la partition causale
    (2167, 2301,
     "> ⚠ *(v3.6)* Ce « moins de 1 % » vient d'un seul modèle, Llama 3.1 8B Instruct, et de la seule complaisance d'opinion, en un tour (README du dépôt ; cours, volet 6, §2) ; et le patch de l'état complet aux mêmes sites, qui en fait 68 %, sert de plafond, pas d'explication (cours, volet 6, §2 ; programme, partie 8). Parade : la même partition sur d'autres concepts, puis sur un second modèle, avec un balayage de rang sur des sous-espaces emboîtés dans une même expérience (cours, volet 6, §6).",
     "> ⚠ *(v3.6)* This \"less than 1%\" comes from a single model, Llama 3.1 8B Instruct, and from opinion sycophancy alone, single-turn (repository README; course, Part 6, §2); and patching the full state at the same sites, which does 68%, is a ceiling, not an explanation (course, Part 6, §2; programme, part 8). Workaround: the same partition on other concepts, then on a second model, with a rank sweep on nested subspaces within one experiment (course, Part 6, §6)."),
    # F·5 — RepE : lire n'est pas agir
    (2183, 2317,
     "> ⚠ *(v3.6)* La direction qui lit le mieux n'est pas forcément celle qui agit : chez RepE, la direction de la régression logistique donne la meilleure exactitude, mais la renforcer ou la retirer ne change presque rien au comportement (cours, volet 10, n° 53) ; sur les modèles « quirky », à transfert comparable, les directions logistiques sont bien moins causales que la différence des moyennes (cours, volet 10, n° 30). Parade : choisir une direction, ou un site, par son effet causal mesuré — plus que des directions aléatoires de même norme (le nul de spécificité), puis plus que des témoins à dégradation appariée (le dommage) —, jamais par l'exactitude de lecture (passation, §5.2 ; cours, volet M, M4 ; README du dépôt).",
     "> ⚠ *(v3.6)* The direction that reads best is not necessarily the one that acts: in RepE, the logistic-regression direction gives the highest accuracy, but strengthening or suppressing it barely changes behaviour (course, Part 10, no. 53); on the \"quirky\" models, at comparable transfer, logistic directions are far less causal than the mean difference (course, Part 10, no. 30). Workaround: choose a direction, or a site, by its measured causal effect — more than matched-norm random directions (the specificity null), then more than controls at matched degradation (the damage) — never by reading accuracy (handover, §5.2; course, Part M, M4; repository README)."),
    # F·7 — le nul de rang un
    (2232, 2366,
     "> ⚠ *(v3.6)* Ce nul de rang un est dit sans son cas connu : sans un concept qui cède au rang un dans le même appareil, au même réglage, il ne départage pas « concept réparti » et « appareil aveugle à ce réglage » (fiche 7 ; cours, volet M, M5) ; ces méthodes sont rapportées sans chiffres, leurs sorties brutes n'ayant pas été conservées, et l'addition d'activations contrastives y forçait un artefact de polarité oui/non (README du dépôt). Parade : un cas connu au même réglage — un vecteur de pays, qui s'échange dans l'article sur l'espace de travail — et un balayage de rang dans une même expérience, sur des sous-espaces emboîtés (cours, volet 2, §C, K47 ; cours, volet 6, §6) ; contre l'artefact de polarité, aucune parade connue ; on le dit.",
     "> ⚠ *(v3.6)* This rank-one null is stated without its known case: without a concept that gives way at rank one in the same apparatus, at the same setting, it does not separate \"distributed concept\" from \"apparatus blind at this setting\" (reading sheet 7; course, Part M, M5); these methods are reported without numbers, their raw outputs not having been preserved, and contrastive activation addition forced a yes/no polarity artefact there (repository README). Workaround: a known case at the same setting — a country vector, which swaps in the workspace paper — and a rank sweep within one experiment, on nested subspaces (course, Part 2, §C, K47; course, Part 6, §6); against the polarity artefact, none known; say so."),
    # F·7 — « de façon contrôlée » (texte du volet 4)
    (2238, 2372,
     "> ⚠ *(v3.6)* « De façon contrôlée » ne veut pas dire « à dégradation appariée » : CAA se compare à des prompts système et au fine-tuning, mesure les capacités par MMLU et TruthfulQA, note le texte libre par GPT-4 avec un échantillon vérifié à la main, et la sycophancie y est le comportement le moins bien piloté en questions à choix multiples (cours, volet 10, n° 54). Parade : la direction aléatoire de même norme n'est que le nul de spécificité ; le dommage ne s'écarte qu'à dégradation appariée, par une courbe dose-réponse contre plusieurs témoins (cours, volet M, M4 ; cours, volet 2, §C, K47).",
     "> ⚠ *(v3.6)* \"In a controlled way\" does not mean \"at matched degradation\": CAA is compared with system prompts and fine-tuning, measures capabilities with MMLU and TruthfulQA, scores free text with GPT-4 with a sample checked by hand, and sycophancy is the behaviour it steers least well in multiple choice (course, Part 10, no. 54). Workaround: the matched-norm random direction is only the specificity null; damage is ruled out only at matched degradation, by a dose-response curve against several controls (course, Part M, M4; course, Part 2, §C, K47)."),
    # F·7 — le taux jugé
    (2240, 2374,
     "> ⚠ *(v3.6)* Ce « taux jugé » passe par un juge LLM : accord inter-juges modéré (κ de 0,56 à 0,66), aucun sous-ensemble noté par des humains, et un juge qui ne voit pas le texte évalué (README du dépôt). Parade : un juge scellé (prompt, modèle et température gelés) et un audit humain d'environ 200 items stratifiés, l'accord rapporté (programme, partie 3), sur la réponse entière gardée en texte complet (README du dépôt ; cours, volet 6, §6).",
     "> ⚠ *(v3.6)* This \"judged rate\" goes through an LLM judge: moderate inter-judge agreement (κ from 0.56 to 0.66), no human-rated subset, and a judge that does not see the evaluated text (repository README). Workaround: a sealed judge (prompt, model and temperature frozen) and a human audit of about 200 stratified items, agreement reported (programme, part 3), on the whole answer kept as full text (repository README; course, Part 6, §6)."),
    # F·8 — forcer une feature (texte du volet 4)
    (2263, 2397,
     "> ⚠ *(v3.6)* « Forcer une feature pousse le modèle à produire le concept » ne la valide qu'à dégradation appariée (fiches, partie B, piège 4 ; cours, volet M, M4), et des explications plausibles existent pour des directions arbitraires (fiche 5). Parade : piloter les features une à une contre des directions aléatoires à dommage apparié, sur une tâche à géométrie connue, avec de nouvelles graines (cours, volet 2, §D, K64), et valider par la prédiction, mieux que des baselines (fiche 5).",
     "> ⚠ *(v3.6)* \"Forcing a feature pushes the model to produce the concept\" validates it only at matched degradation (reading sheets, part B, trap 4; course, Part M, M4), and plausible explanations exist for arbitrary directions (reading sheet 5). Workaround: steer the features one at a time against random directions at matched damage, on a task with known geometry, with new seeds (course, Part 2, §D, K64), and validate by prediction, better than baselines (reading sheet 5)."),
    # F·8 — décomposer : l'erreur de reconstruction
    (2265, 2399,
     "> ⚠ *(v3.6)* Décomposer avec un dictionnaire ouvert bute sur son erreur de reconstruction : le SAE de Goodfire pour Llama 3.1 8B Instruct laisse 86,8 % de la variance au résidu, qui porte le signal lu, si bien que l'échec du blocage de features ne sépare pas « features absentes du dictionnaire » et « dictionnaire qui perd trop » (README du dépôt). Parade : lire le signal sur la reconstruction et sur le résidu ; pour trancher entre les deux lectures, aucune parade connue ; on le dit (README du dépôt).",
     "> ⚠ *(v3.6)* Decomposing with an open-source dictionary runs into its reconstruction error: the Goodfire SAE for Llama 3.1 8B Instruct leaves 86.8% of the variance in the residual, which carries the read signal, so the failure of feature clamping does not separate \"features absent from the dictionary\" from \"dictionary too lossy\" (repository README). Workaround: read the signal on the reconstruction and on the residual; to decide between the two readings, none known; say so (repository README)."),
    # F·9 — la vague récente (oracles, NLA, vecteurs d'émotion)
    (2293, 2427,
     "> ⚠ *(v3.6)* Oracles d'activation et NLA peuvent confabuler des suppositions plausibles, souvent fausses, et, en lecture seule, n'ont donné aucun gain sur le transcript pour prédire des contrefactuels (fiche 18 ; fiche 4) ; des vecteurs d'émotion « manipulables » ne disent le concept qu'à dégradation appariée (fiches, partie B, piège 4). Parade : corroborer par une méthode indépendante et garder le décodeur à part (fiche 18) ; battre la boîte noire sur des éditions qui dissocient la surface de la variable interne (fiche 4) ; piloter contre plusieurs témoins, en courbe dose-réponse (cours, volet 2, §C, K47).",
     "> ⚠ *(v3.6)* Activation oracles and NLAs can confabulate plausible guesses, often wrong, and, read-only, gave no gain over the transcript for predicting counterfactuals (reading sheet 18; reading sheet 4); \"manipulable\" emotion vectors show the concept only at matched degradation (reading sheets, part B, trap 4). Workaround: corroborate with an independent method and keep the decoder separate (reading sheet 18); beat the black box on edits that dissociate surface features from the internal variable (reading sheet 4); steer against several controls, as a dose-response curve (course, Part 2, §C, K47)."),
    # F·10 — la sûreté mesurée dépend de la red team (texte du volet 4)
    (2317, 2451,
     "> ⚠ *(v3.6)* « Une grande part des tentatives » attrapées dépend de la red team supposée : un échafaudage d'attaque optimisé fait passer le score de sûreté de cinq environnements SHADE-Arena de 0,87 à 0,41 (cours, volet 7, F·24) ; et un moniteur a des angles morts systématiques, la moitié de quarante attaques conçues à la main n'étant jamais attrapées par Opus 4.6 en moniteur (cours, volet 7, F·23). Parade : dire quelle red team le chiffre suppose, au moins une red team optimisée composante par composante (cours, volet 7, F·24), et calibrer le seuil à 1 % de faux positifs sur des variantes bénignes appariées (cours, volet 7, F·23).",
     "> ⚠ *(v3.6)* The \"large share of attempts\" caught depends on the red team assumed: an optimized attack scaffold takes the safety score of five SHADE-Arena environments from 0.87 to 0.41 (course, Part 7, F·24); and a monitor has systematic blind spots, half of forty hand-designed attacks never being caught by Opus 4.6 as the monitor (course, Part 7, F·23). Workaround: say which red team the number assumes, at least one optimized component by component (course, Part 7, F·24), and calibrate the threshold at 1% false positives on paired benign variants (course, Part 7, F·23)."),
    # F·11 — le débat et son juge
    (2335, 2469,
     "> ⚠ *(v3.6)* Dans un autre papier de la lignée, l'avantage du débat n'apparaît qu'avec des débatteurs humains — avec GPT-4, 78 % contre 80 % en consultancy —, et les juges, humains, y sont surconfiants (cours, volet 10, Michael et al.) ; quand le juge est un modèle, les limites des juges LLM s'appliquent (fiches, partie B, piège 6). Parade : mesurer sur un banc où l'on connaît la bonne réponse (cours, volet 2, §E), avec un juge scellé et un audit humain (programme, partie 3) ; au-delà de l'expertise humaine, il n'y a plus de référence : aucune parade connue ; on le dit (cours, volet 2, §E).",
     "> ⚠ *(v3.6)* In another paper of the line, debate's advantage appears only with human debaters — with GPT-4, 78% against 80% for consultancy — and the judges, human, are overconfident there (course, Part 10, Michael et al.); when the judge is a model, the limits of LLM judges apply (reading sheets, part B, trap 6). Workaround: measure on a testbed where the right answer is known (course, Part 2, §E), with a sealed judge and a human audit (programme, part 3); beyond human expertise there is no reference left: none known; say so (course, Part 2, §E)."),
    # F·12 — la récupération de l'écart
    (2359, 2493,
     "> ⚠ *(v3.6)* Une récupération de l'écart peut tromper : des agents ont récupéré presque tout l'écart avec des idées qui exploitaient la structure propre au jeu de données, et, sur une tâche binaire, contredire partout passerait pour une récupération (cours, volet 2, §F, JB8). Parade : une tâche à vérité connue, deux superviseurs faibles, l'un faux dans un sens fixe, l'autre au hasard, une copie entraînée sur les étiquettes vraies comme cas connu, et la lecture des items tenus à part où le superviseur se trompe, avec l'accord du fort là où il a raison (cours, volet 2, §F, JB8).",
     "> ⚠ *(v3.6)* Recovering the gap can mislead: agents recovered almost all of the gap with ideas that exploited the dataset's own structure, and, on a binary task, contradicting everywhere would pass for recovery (course, Part 2, §F, JB8). Workaround: a task with known truth, two weak supervisors, one wrong in a fixed direction, the other at random, a copy trained on the true labels as the known case, and a reading on the held-out items where the supervisor is wrong, with the strong model's agreement where it is right (course, Part 2, §F, JB8)."),
    # F·13 — ce que l'interprétabilité ajoute à l'audit
    (2383, 2517,
     "> ⚠ *(v3.6)* Que l'interprétabilité « aide » n'est pas chiffré : quatre équipes seulement, l'équipe qui avait les données sans SAE a réussi, celle privée de données a échoué, et l'objectif, décrit en clair dans les documents synthétiques, était « artificially easy to discover » (fiche 16). Parade : une ablation d'affordance, qui retire un outil à une équipe, chiffrerait ce que l'interprétabilité apporte (fiche 16) ; planter le même comportement par plusieurs recettes, en tenir une à part (cours, volet 2, §A, K71) ; contre un organisme trop facile, aucune parade connue ; on le dit.",
     "> ⚠ *(v3.6)* That interpretability \"helps\" is not quantified: only four teams, the team with the data and no SAE succeeded, the one without data failed, and the objective, stated plainly in the synthetic documents, was \"artificially easy to discover\" (reading sheet 16). Workaround: an affordance ablation, removing one tool from a team, would quantify what interpretability adds (reading sheet 16); plant the same behaviour through several recipes, holding one out (course, Part 2, §A, K71); against an organism that is too easy, none known; say so."),
    # F·17 — SGTM et le test par ré-entraînement
    (2479, 2613,
     "> ⚠ *(v3.6)* Ce « 7× » compare des méthodes de désapprentissage entre elles, sur de petits modèles (cours, volet 7, F·36 ; cours, volet 2, §I, JB10) ; et le test par ré-entraînement sur des faits indépendants ne vaut que pour des faits à faible fuite, pas pour des capacités (cours, volet 10, Deeb et Roger). Parade : le contrôle suivant — le même fine-tuning adverse, au même budget, sur le modèle traité, sur une référence jamais entraînée et, comme cas connu, sur un modèle connu pour masquer — pour dire une borne, pas une certification (cours, volet 2, §I, JB10) ; pour l'échelle et pour les capacités, aucune parade connue ; on le dit.",
     "> ⚠ *(v3.6)* This \"7×\" compares unlearning methods with each other, on small models (course, Part 7, F·36; course, Part 2, §I, JB10); and the retraining test on independent facts works only for low-leakage facts, not for capabilities (course, Part 10, Deeb and Roger). Workaround: the next control — the same adversarial fine-tune, at the same budget, on the treated model, on a never-trained reference and, as the known case, on a model known to mask — to state a bound, not a certification (course, Part 2, §I, JB10); for scale and for capabilities, none known; say so."),
    # F·17 — clôture du volet 4 : la neutralisation de l'eval-awareness
    (2487, 2621,
     "> ⚠ *(v3.6)* La neutralisation de la conscience d'évaluation dans les cartes système est un résultat de pilotage : des vecteurs au contenu arbitraire bougent aussi le comportement, chaque direction dégrade les sorties, et, à dégradation négligeable, les contrôles restent « comparable or smaller » sur l'axe du désalignement (fiche 2). Parade : un sous-espace spécifique contre des sous-espaces aléatoires de même rang, à dégradation appariée, avec une baseline de prompt et une courbe dose-réponse (fiche 2 ; cours, volet 2, §C, K47).",
     "> ⚠ *(v3.6)* The neutralization of evaluation awareness in system cards is a steering result: vectors with arbitrary content move behaviour too, every direction degrades the outputs, and, at negligible degradation, the controls stay \"comparable or smaller\" on the misalignment axis (reading sheet 2). Workaround: a specific subspace against random subspaces of the same rank, at matched degradation, with a prompt baseline and a dose-response curve (reading sheet 2; course, Part 2, §C, K47)."),
    # F·50 — 0,867 contre 95-99 % (avertissement prêt ; ancre déplacée en fin de liste ; parade ajoutée)
    (2511, 2643,
     "> ⚠ *(v3.6)* Le volet 6, §6 attribue 0,867 à la reproduction de Casademunt et donne aux auteurs « catches 95-99 % » à 1 % de faux positifs, sur leurs propres bancs (cours, volet 6, §6 ; cours, note de tête) ; et sur l'honnêteté, des sondes de vérité ont fait moins bien qu'un simple prompt (cours, volet 7, F·62). Parade : dire de quel banc et de quelle étude vient chaque chiffre (cours, volet 6, §6), et battre un prompt à coût égal, en publiant le résultat si la sonde ne le bat pas (cours, volet 5, sujet 1 ; cours, volet 7, F·29).",
     "> ⚠ *(v3.6)* Part 6, §6 attributes 0.867 to Casademunt's reproduction and gives the authors \"catches 95-99%\" at 1% false positives, on their own benches (course, Part 6, §6; course, opening reserves); and on honesty, truth probes did worse than a plain prompt (course, Part 7, F·62). Workaround: say which bench and which study each number comes from (course, Part 6, §6), and beat a prompt at equal cost, publishing the result if the probe does not beat it (course, Part 5, topic 1; course, Part 7, F·29)."),
    # F·51 — une AUROC hors distribution n'est pas un rappel de moniteur
    (2529, 2661,
     "> ⚠ *(v3.6)* Le « > 0,91 » hors distribution est une AUROC : au seuil d'un moniteur, ces sondes rappellent 43 % à 1 % de faux positifs, contre 55 % pour le meilleur moniteur LLM (cours, volet 7, F·51), et la distance hors distribution n'est pas dite ici. Parade : rapporter le rappel à 1 % de faux positifs à côté de l'AUROC, battre une baseline boîte noire à coût égal, et dire la distance — instances nouvelles, familles tenues à part en un tour, agentique à plusieurs tours (cours, volet 7, F·50 ; cours, volet 5, sujet 1 ; programme, partie 3).",
     "> ⚠ *(v3.6)* The out-of-distribution \"> 0.91\" is an AUROC: at a monitor's threshold, these probes recall 43% at 1% false positives, against 55% for the best LLM monitor (course, Part 7, F·51), and the out-of-distribution distance is not stated here. Workaround: report recall at 1% false positives next to the AUROC, beat a black-box baseline at equal cost, and state the distance — new instances, held-out families in one turn, multi-turn agentic (course, Part 7, F·50; course, Part 5, topic 1; programme, part 3)."),
    # F·52 — l'AUROC en distribution
    (2547, 2679,
     "> ⚠ *(v3.6)* Le 1,00 en distribution ne prouve rien : le chiffre qui compte est l'écart avec le transfert, ici 0,73 à 0,93 en zéro-shot (fiches, partie B, piège 1 ; fiche 7 ; cours, volet 7, F·52). Parade : tenir à part des familles entières, jamais des paraphrases, et des formats, d'un tour à l'agentique à plusieurs tours (explication du 2 octobre, §3 ; programme, partie 3).",
     "> ⚠ *(v3.6)* The 1.00 in distribution proves nothing: the number that matters is the gap with transfer, here 0.73 to 0.93 zero-shot (reading sheets, part B, trap 1; reading sheet 7; course, Part 7, F·52). Workaround: hold out whole families, never paraphrases, and formats, from single-turn to multi-turn agentic (explanation of 2 October, §3; programme, part 3)."),
    # F·53 — un nul sous conscience induite par le prompt
    (2564, 2696,
     "> ⚠ *(v3.6)* Ce nul porte sur une conscience induite par le prompt, pas entraînée, et ne compte qu'avec un cas connu où une pression fait bien baisser la détection (cours, volet M, M5) : sous entraînement, la lecture peut céder — après un RL, des sondes neuves hors domaine se dégradent (rapport d'antériorité 3 du 2 octobre, The Obfuscation Atlas — rapport). Parade : un organisme dressé à se cacher comme cas connu (cours, volet 2, §B, K63), et une sonde neuve après tout entraînement, sur un jeu d'indices disjoint (explication du 2 octobre, §2 et §3 ; passation, §5.2).",
     "> ⚠ *(v3.6)* This null bears on prompt-induced awareness, not trained awareness, and counts only with a known case where pressure does lower detection (course, Part M, M5): under training, the reading can give way — after RL, fresh out-of-domain probes degrade (prior-art report 3 of 2 October, The Obfuscation Atlas — report). Workaround: an organism trained to hide as the known case (course, Part 2, §B, K63), and a fresh probe after any training, on a disjoint cue set (explanation of 2 October, §2 and §3; handover, §5.2)."),
    # F·54 — un rappel sans taux de faux positifs
    (2582, 2714,
     "> ⚠ *(v3.6)* Un rappel de 0,844 ne se lit qu'avec son taux de faux positifs et le ratio de trafic bénin : un rappel de campagne dépend du taux de base (cours, volet 6, §6). Parade : rapporter le rappel à un taux de faux positifs fixé — 1 % pour la première porte de ton programme —, calibré sur des variantes bénignes appariées, avec le ratio de trafic dit (cours, volet 6, §6 ; cours, volet 7, F·23).",
     "> ⚠ *(v3.6)* A recall of 0.844 reads only with its false-positive rate and the benign-traffic ratio: a campaign recall depends on the base rate (course, Part 6, §6). Workaround: report recall at a fixed false-positive rate — 1% for your programme's first gate —, calibrated on paired benign variants, with the traffic ratio stated (course, Part 6, §6; course, Part 7, F·23)."),
    # F·56 — taux d'évasion, red team, et le « 81-87 % » de Brown
    (2618, 2750,
     "> ⚠ *(v3.6)* Ces taux d'évasion et de capture dépendent de la red team qui attaque (cours, volet 7, F·24) ; et le volet 6, §6, corrigé sur les textes intégraux, situe le « 81-87 % » de Brown dans sa figure 5, absente du résumé : un rappel de campagne à 2,35-3,09 % de faux positifs, à dix fois plus de trafic bénin que d'attaque, qui tombe à 65,8 % à cent fois (cours, volet 6, §6 ; cours, note de tête). Parade : dire quelle red team et quel ratio de trafic chaque chiffre suppose, et rapporter le rappel à un taux de faux positifs fixé (cours, volet 7, F·24 ; cours, volet 6, §6).",
     "> ⚠ *(v3.6)* These evasion and catch rates depend on the attacking red team (course, Part 7, F·24); and Part 6, §6, corrected against the full texts, places Brown's \"81-87%\" in its figure 5, absent from the abstract: a campaign recall at 2.35-3.09% false positives, at ten times more benign traffic than attacks, which drops to 65.8% at a hundred times (course, Part 6, §6; course, opening reserves). Workaround: say which red team and which traffic ratio each number assumes, and report recall at a fixed false-positive rate (course, Part 7, F·24; course, Part 6, §6)."),
    # F·57 — SHADE-Arena : sabotage, AUC et red team
    (2635, 2767,
     "> ⚠ *(v3.6)* Ces taux de sabotage et cette AUC dépendent de la red team : sur cinq environnements SHADE-Arena, un échafaudage d'attaque optimisé fait passer le score de sûreté de 0,87 à 0,41 (cours, volet 7, F·24) ; et une AUC ne dit pas le rappel au seuil d'un moniteur (cours, volet 7, F·50). Parade : dire quelle red team le chiffre suppose, au moins une red team optimisée composante par composante (cours, volet 7, F·24), et rapporter le rappel à 1 % de faux positifs, calibré sur des variantes bénignes appariées (cours, volet 7, F·23).",
     "> ⚠ *(v3.6)* These sabotage rates and this AUC depend on the red team: on five SHADE-Arena environments, an optimized attack scaffold takes the safety score from 0.87 to 0.41 (course, Part 7, F·24); and an AUC does not give the recall at a monitor's threshold (course, Part 7, F·50). Workaround: say which red team the number assumes, at least one optimized component by component (course, Part 7, F·24), and report recall at 1% false positives, calibrated on paired benign variants (course, Part 7, F·23)."),
]


def ancre(fi, n):
    a, b = TR[fi]
    assert a <= n <= b, (fi, n)
    line = L[fi][n - 1]
    assert line.strip(), (fi, n, 'ligne vide')
    k = sum(1 for i in range(a - 1, b) if L[fi][i].strip() == line.strip())
    assert k == 1, (fi, n, k, line[:80])
    return line


items = []  # (fichier, numéro de ligne, ordre, texte)
order = 0
for nfr, nen, tfr, ten in AV:
    items.append(('FR', nfr, order, tfr)); items.append(('EN', nen, order, ten)); order += 1
for nfr, nen, keys in RENVOIS:
    fr, en = renvoi(keys)
    items.append(('FR', nfr, order, fr)); items.append(('EN', nen, order, en)); order += 1

# ordre final : par position dans le texte, l'avertissement avant le renvoi quand ils partagent une ancre
items.sort(key=lambda x: (x[0] != 'FR', x[1], x[2]))
ins = []
fr_items = [x for x in items if x[0] == 'FR']
en_items = [x for x in items if x[0] == 'EN']
assert len(fr_items) == len(en_items)
for f, e in zip(fr_items, en_items):
    assert f[2] == e[2], ('jumelles désalignées', f[1], e[1])
    ins.append({'fichier': 'FR', 'ancre': ancre('FR', f[1]), 'texte': f[3]})
    ins.append({'fichier': 'EN', 'ancre': ancre('EN', e[1]), 'texte': e[3]})

out = f'{W}/travail/insertions_volet7_A_et_C.json'
json.dump({'tranche': 'volet7_A_et_C', 'insertions': ins}, open(out, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(ins), 'insertions écrites dans', out)
print('avertissements :', len(AV), '× 2 ; renvois :', len(RENVOIS), '× 2')
