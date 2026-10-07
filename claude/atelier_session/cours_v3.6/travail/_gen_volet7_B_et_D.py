#!/usr/bin/env python3
"""Génère travail/insertions_volet7_B_et_D.json (volet 7, parties B et D : fiches de lecture).
Les ancres sont prises par numéro de ligne dans la v3.5, puis vérifiées uniques dans la tranche
(comparaison après suppression des espaces de début et de fin, comme appliquer.py)."""
import json, os

W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = {'FR': f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md', 'EN': f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md'}
TR = {'FR': (1627, 2069), 'EN': (1792, 2203)}
L = {k: open(v, encoding='utf8').read().split('\n') for k, v in SRC.items()}

# --- renvois d'une ligne : noms et maisons, repris du référentiel ---
R = {
    'mon': ("moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes »)",
            'control monitors → Part 2, §G (after "In practice — coup probes")'),
    'jug': ("juges LLM → volet 6, §2 (après « La loi de déplacement »)",
            'LLM judges → Part 6, §2 (after "The displacement law")'),
    'red': ("red-teaming → volet 2, §H (après « En pratique — StrongREJECT »)",
            'red-teaming → Part 2, §H (after "In practice — StrongREJECT")'),
    'eva': ("évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging »)",
            'behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging")'),
    'cot': ("chaîne de pensée comme moniteur → volet 11, réponse 43",
            'chain of thought as a monitor → Part 11, answer 43'),
    'pil': ("pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition »)",
            'steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition")'),
    'son': ("sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth »)",
            'activation probes → Part 2, §C (after "In practice — The Geometry of Truth")'),
    'ala': ("contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme »)",
            'random controls → Part M, M4 (after "The matched-norm random direction")'),
    'deg': ("dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse »)",
            'matched degradation and dose-response → Part M, M4 (after "Dose-response")'),
    'org': ("organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives »)",
            'model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives")'),
    'cas': ("cas connu → volet M, M5 (fin de section)",
            'known case → Part M, M5 (end of section)'),
    'tap': ("jeu tenu à part → volet M, M4 (après « Le jeu tenu à part »)",
            'held-out set → Part M, M4 (after "The held-out set")'),
    'aut': ("auto-rapport et introspection → volet 5, partie II, A, sujet 13",
            'self-report and introspection → Part 5, Section II, A, Topic 13'),
    'nla': ("autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle",
            'natural-language autoencoders → Part 4, The recent wave on model cognition'),
    'ora': ("oracles d'activation → volet 10, fiche LatentQA",
            'activation oracles → Part 10, LatentQA sheet'),
    'sae': ("dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity",
            'dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity'),
    'des': ("désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve »)",
            'unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test")'),
    'w2s': ("généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation »)",
            'weak-to-strong generalization → Part 2, §F (after "In practice — automation")'),
    'cla': ("classifieurs de sûreté → volet 2, §H (fin du cas d'application G1)",
            'safety classifiers → Part 2, §H (end of worked case G1)'),
    'det': ("détecteurs fine-tunés → volet 7, F·29",
            'fine-tuned detectors → Part 7, F·29'),
}


def renvoi(*cles):
    fr = '> ⚠ **Limites et parades** : ' + ' ; '.join(R[c][0] for c in cles) + ' *(v3.6)*'
    en = '> ⚠ **Limits and workarounds**: ' + '; '.join(R[c][1] for c in cles) + ' *(v3.6)*'
    return fr, en


# --- l'encadré complet de la maison de la tranche (référentiel, n° 24), repris tel quel ---
BOX_DET_FR = """> **⚠ Limites et parades — Détecteurs fine-tunés (détecteurs de mensonge)** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Hors distribution, l'AUROC plafonne à 0,70-0,75 et bat à peine un prompt. *(source : fiche 7)*
>   **Parade :** Une validation croisée par types de mensonge tenus à part ; battre le prompt, et publier sinon. *(source : fiche 7 ; cours, volet 7, F·29)*
> - **Limite :** Ce ne sont pas des sondes : le modèle est fine-tuné par LoRA à juger son propre transcript. *(source : fiche 7 ; explication du 2 octobre, §2)*
>   **Parade :** Ne pas transférer leurs chiffres aux sondes ; pour une sonde, le test est causal, sur des types tenus à part, à dégradation appariée. *(source : fiche 7)*
> - **Limite :** Étiquettes bruitées : environ 25 % révisées à la passe de nettoyage, après un juge GPT-5. *(source : fiche 7)*
>   **Parade :** Dire « révisées », et borner l'erreur par un audit humain. *(source : fiche 7 ; programme, partie 3)*
> - **Limite :** Ils ne notent que des assertions : un modèle peut cacher beaucoup sans rien affirmer de faux. *(source : cours, volet 7, F·29)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Ce qu'ils ont appris reste une hypothèse : « lying isn't one thing », et trois lectures rivales demeurent. *(source : fiche 7)*
>   **Parade :** Tester les lectures rivales sur des types tenus à part. *(source : fiche 7)*
> - **Limite :** LoRA, cinq époques, Gemma et Qwen seulement, cadres contrôlés : rien sur la tromperie en déploiement. *(source : fiche 7)*
>   **Parade :** aucune connue ; on le dit."""

BOX_DET_EN = """> **⚠ Limits and workarounds — Fine-tuned detectors (lie detectors)** *(v3.6, 2 October 2026)*
>
> - **Limit:** Out of distribution, AUROC plateaus at 0.70-0.75 and barely beats a prompt. *(source: reading sheet 7)*
>   **Workaround:** Cross-validation by held-out lie types; beat the prompt, and publish otherwise. *(source: reading sheet 7; course, Part 7, F·29)*
> - **Limit:** These are not probes: the model is LoRA-fine-tuned to judge its own transcript. *(source: reading sheet 7; explanation of 2 October, §2)*
>   **Workaround:** Do not transfer their numbers to probes; for a probe, the test is causal, on held-out types, at matched degradation. *(source: reading sheet 7)*
> - **Limit:** Noisy labels: about 25% revised at the cleaning pass, after a GPT-5 judge. *(source: reading sheet 7)*
>   **Workaround:** Say "revised", and bound the error with a human audit. *(source: reading sheet 7; programme, part 3)*
> - **Limit:** They score only assertions: a model can hide a lot without asserting anything false. *(source: course, Part 7, F·29)*
>   **Workaround:** none known; say so.
> - **Limit:** What they learned remains a hypothesis: "lying isn't one thing", and three rival readings remain. *(source: reading sheet 7)*
>   **Workaround:** Test the rival readings on held-out types. *(source: reading sheet 7)*
> - **Limit:** LoRA, five epochs, Gemma and Qwen only, controlled settings: nothing on deception in deployment. *(source: reading sheet 7)*
>   **Workaround:** none known; say so."""

# --- les insertions : (ligne FR, ligne EN, texte FR, texte EN, note) ---
I = []

# F·22 · Diffuse AI Control — le nul de la red team, lu par un juge LLM
I.append((1669, 1834,
 "> ⚠ *(v3.6)* « Résiste au red-teaming complet » est le nul d'une red team : il ne vaut qu'au budget et à la force de l'attaque essayée *(source : cours, volet M, M7 ; cours, volet 7, F·24)* ; et il se lit au score d'un juge LLM, la « vérité-terrain » étant elle-même un modèle, sans audit humain rapporté *(source : cours, volet 7, F·22 ; fiches, partie B, piège 6)*. Parade : un budget d'attaque fixé d'avance et rapporté avec le résultat, une red team optimisée composante par composante, et un audit humain stratifié qui borne l'erreur du juge — le proxy « avec humains dans la boucle » qu'ils laissent ouvert *(source : cours, volet M, M7 ; cours, volet 7, F·24 ; programme, partie 3 ; cours, volet 7, F·22)*.",
 "> ⚠ *(v3.6)* \"Withstands full red-teaming\" is the null of a red team: it holds only at the budget and strength of the attack tried *(source: course, Part M, M7; course, Part 7, F·24)*; and it is read off an LLM judge's score, the \"ground truth\" being itself a model, with no human audit reported *(source: course, Part 7, F·22; reading sheets, part B, trap 6)*. Workaround: an attack budget fixed in advance and reported with the result, a red team optimized component by component, and a stratified human audit that bounds the judge's error — the proxy \"with humans in the loop\" they leave open *(source: course, Part M, M7; course, Part 7, F·24; programme, part 3; course, Part 7, F·22)*.",
 'ponctuel F·22'))
I.append((1688, 1853, *renvoi('mon', 'jug', 'red'), 'renvoi F·22'))

# F·23 · SLEIGHT-Bench
I.append((1727, 1892, *renvoi('mon'), 'renvoi F·23'))

# F·24 · Strengthening Red Teams
I.append((1751, 1916, *renvoi('red', 'mon'), 'renvoi F·24'))

# F·25 · Audit realism — le résultat interne rappelé est un résultat de pilotage
I.append((1770, 1935,
 "> ⚠ *(v3.6)* Le résultat interne rappelé ici vient du pilotage, et c'est un appui faible : des vecteurs de contrôle au contenu arbitraire bougent le comportement dans le même sens, plus faiblement, et chaque direction pilotée dégrade les sorties *(source : fiche 2 ; fiches, partie C ; cours, volet 5, partie I, §3)*. Parade : un sous-espace spécifique contre des sous-espaces aléatoires de même rang, comparés à dégradation appariée, avec une courbe dose-réponse ; la direction aléatoire de même norme n'est que le nul de spécificité *(source : fiche 2 ; cours, volet M, M4)*.",
 "> ⚠ *(v3.6)* The internal result recalled here comes from steering, and it is weak support: control vectors with arbitrary content move behaviour in the same direction, more weakly, and every steered direction degrades the outputs *(source: reading sheet 2; reading sheets, part C; course, Part 5, Section I, §3)*. Workaround: a specific subspace against random subspaces of the same rank, compared at matched degradation, with a dose-response curve; the matched-norm random direction is only the specificity null *(source: reading sheet 2; course, Part M, M4)*.",
 'ponctuel F·25'))
I.append((1775, 1940, *renvoi('eva', 'jug', 'cot', 'pil'), 'renvoi F·25'))

# F·29 · Fine-Tuned Lie Detectors — renvoi pour le travail voisin (sondes, pilotage), puis l'encadré de la maison
I.append((1796, 1961, *renvoi('son', 'pil'), 'renvoi F·29 (travail voisin)'))
I.append((1807, 1972, BOX_DET_FR, BOX_DET_EN, 'encadré n° 24, détecteurs fine-tunés'))

# F·30 · CHIVE — un nul d'instrument, sans cas connu
I.append((1831, 1996,
 "> ⚠ *(v3.6)* Ce « no uplift » est le nul de trois outils en lecture seule, sur des comportements simples et pour les éditions testées : le plafond atteignable reste inconnu, et un nul d'instrument ne compte qu'avec son cas connu *(source : fiche 4 ; cours, volet M, M5)*. Parade : la barre que pose la fiche 4, battre la boîte noire sur des éditions qui dissocient la surface de la variable interne ; pour un décodeur, un test sur des variantes fine-tunées à comportement connu, jamais vues ; et un audit humain qui borne l'erreur du classifieur *(source : fiche 4 ; fiche 18 ; programme, partie 3)*.",
 "> ⚠ *(v3.6)* This \"no uplift\" is the null of three read-only tools, on simple behaviours and for the edits tested: the attainable ceiling remains unknown, and an instrument's null counts only with its known case *(source: reading sheet 4; course, Part M, M5)*. Workaround: the bar set by reading sheet 4, beating the black box on edits that dissociate surface features from the internal variable; for a decoder, a test on fine-tuned variants with known behaviour, never seen before; and a human audit that bounds the classifier's error *(source: reading sheet 4; reading sheet 18; programme, part 3)*.",
 'ponctuel F·30'))
I.append((1841, 2006, *renvoi('nla', 'ora', 'sae', 'aut', 'jug'), 'renvoi F·30'))

# F·34 · Model Spec Midtraining
I.append((1874, 2039, *renvoi('eva', 'tap'), 'renvoi F·34'))

# F·33 · Inoculation Prompting — « non appris » lu au comportement ; la sonde qui compare deux entraînements
I.append((1891, 2056,
 "> ⚠ *(v3.6)* « Non appris » se lit ici au comportement, sous des prompts normaux : selon un travail externe, l'inoculation peut aussi masquer un désalignement qui revient sous un cadre proche de l'entraînement *(source : fiches, partie C)*. Parade : mesurer hors distribution, sur des métriques tenues à part, et vérifier par l'intérieur que la représentation a changé, pas seulement le comportement *(source : fiches, partie C)*.",
 "> ⚠ *(v3.6)* \"Not learned\" is read here from behaviour, under normal prompts: according to an external work, inoculation can also mask a misalignment that returns under a frame close to training *(source: reading sheets, part C)*. Workaround: measure out of distribution, on held-out metrics, and check from the inside that the representation changed, not only the behaviour *(source: reading sheets, part C)*.",
 'ponctuel F·33 (évaluation)'))
I.append((1894, 2059,
 "> ⚠ *(v3.6)* Ce test compare une direction entre deux entraînements, or l'entraînement change les représentations : une sonde calibrée sur un bras lirait autrement dans l'autre, et ce biais de mesure se confondrait avec l'effet cherché *(source : passation, §5.2)*. Parade : une sonde par bras et une sonde neuve après l'entraînement, sur un jeu d'indices disjoint, gardées comme mesure séparée ; et, pour dire que la direction agit, le test causal à dégradation appariée *(source : passation, §5.2 ; programme, partie 3 ; cours, volet M, M4)*.",
 "> ⚠ *(v3.6)* This test compares a direction across two trainings, yet training changes the representations: a probe calibrated on one arm would read differently in the other, and that measurement bias would be confounded with the effect sought *(source: handover, §5.2)*. Workaround: one probe per arm and a fresh probe after training, on a disjoint cue set, kept as a separate measure; and, to say that the direction acts, the causal test at matched degradation *(source: handover, §5.2; programme, part 3; course, Part M, M4)*.",
 'ponctuel F·33 (sondes)'))
I.append((1899, 2064, *renvoi('eva', 'son'), 'renvoi F·33'))

# F·31 · Persona Vectors — ponctuel prêt du référentiel, puis le composite et l'aléatoire apparié en covariance
I.append((1915, 2080,
 "> ⚠ *(v3.6)* Le lien entre déplacement et trait est corrélationnel, le trait se nomme d'avance et l'évaluation est légère (fiche 8) : pour la causalité, le test à dégradation appariée (cours, volet M, M4). Et piloter loin d'une persona pendant l'entraînement aurait doublé la diffusion du désalignement (rapport d'antériorité 3 du 2 octobre — rapport, non vérifié).",
 "> ⚠ *(v3.6)* The shift-to-trait link is correlational, the trait must be named in advance and the evaluation is light (reading sheet 8): for causality, the matched-degradation test (course, Part M, M4). And steering away from a persona during training reportedly doubled the spread of misalignment (prior-art report 3 of 2 October — report, unverified).",
 'ponctuel prêt F·31 (référentiel)'))
I.append((1920, 2085,
 "> ⚠ *(v3.6)* « MMLU préservé » n'écarte le dommage que sur ce composite, et la direction aléatoire appariée en covariance de ta question n'est, comme toute direction témoin, qu'un nul de spécificité *(source : programme, parties 3 et 8 ; cours, volet 11, réponse A7)*. Parade : comparer les bras à dégradation égale, sur un composite bâti d'après les dégâts attendus du trait, et dire quel aléatoire a fondé quel chiffre *(source : cours, volet 11, réponse A7 ; programme, parties 3 et 7 ; cours, volet 6, §3)*.",
 "> ⚠ *(v3.6)* \"MMLU preserved\" rules out damage only on that composite, and the covariance-matched random direction in your question is, like any control direction, only a specificity null *(source: programme, parts 3 and 8; course, Part 11, answer A7)*. Workaround: compare the arms at equal degradation, on a composite built from the trait's expected damage, and say which random control grounded which number *(source: course, Part 11, answer A7; programme, parts 3 and 7; course, Part 6, §3)*.",
 'ponctuel F·31 (dommage, aléatoire)'))
I.append((1926, 2091, *renvoi('pil', 'son', 'ala', 'deg'), 'renvoi F·31'))

# F·32 · Subliminal Learning
I.append((1953, 2118, *renvoi('org'), 'renvoi F·32'))

# F·38 · Agentic Misalignment — conduite dans des scènes construites
I.append((1969, 2134,
 "> ⚠ *(v3.6)* Ces taux sont des mesures de conduite dans des scènes construites : l'étude a relevé moins de mauvaise conduite quand les modèles se disaient évalués, mais la conscience tue lui échappe, et dans une simulation « c'est faux » est vrai *(source : cours, volet 2, §B, K63 ; fiches, partie B ; fiche 3)*. Parade : deux versions d'un environnement, tirées au hasard, qui ne diffèrent que par des indices de réalisme, la conscience lue par une sonde et par les mots du modèle, et un organisme dressé à se cacher comme cas connu ; contre le confondeur de la simulation, aucune parade connue ; on le dit *(source : cours, volet 2, §B, K63 ; fiche 3)*.",
 "> ⚠ *(v3.6)* These rates are measures of conduct in constructed scenes: the study recorded less misbehaviour when the models said they were being evaluated, but unspoken awareness escapes it, and in a simulation \"this is fake\" is true *(source: course, Part 2, §B, K63; reading sheets, part B; reading sheet 3)*. Workaround: two versions of an environment, randomly assigned, differing only in realism cues, awareness read by a probe and from the model's words, and an organism trained to hide as the known case; against the simulation confound, none known; say so *(source: course, Part 2, §B, K63; reading sheet 3)*.",
 'ponctuel F·38'))
I.append((1969, 2134, *renvoi('eva', 'org'), 'renvoi F·38'))

# F·39 · AI Organizations
I.append((1977, 2142, *renvoi('eva'), 'renvoi F·39'))

# F·28 · Introspection Adapters
I.append((1986, 2151, *renvoi('aut', 'org'), 'renvoi F·28'))

# F·27 · AuditBench — l'implanté borne l'auditeur
I.append((1992, 2157,
 "> ⚠ *(v3.6)* Un taux de découverte sur des comportements implantés borne l'auditeur sans prouver le cas naturel : l'implanté est peut-être plus saillant que le naturel, et dans l'audit dont AuditBench est la suite, l'objectif était décrit en clair dans les documents synthétiques *(source : passation, §5.2 ; cours, volet M, M5 ; fiche 16)*. Parade partielle : planter le même comportement par plusieurs recettes, en tenir une à part, et ajouter l'organisme d'une autre équipe ; pour la question d'accès, retirer un outil à une équipe d'audit chiffre ce qu'il apporte ; contre l'écart entre l'implanté et le naturel lui-même, aucune parade connue ; on le dit *(source : cours, volet 2, §A, K71 ; fiche 16 ; cours, volet M, M5)*.",
 "> ⚠ *(v3.6)* A discovery rate on implanted behaviours bounds the auditor without proving the natural case: an implanted behaviour may be more salient than a natural one, and in the audit that AuditBench follows on from, the objective was stated plainly in the synthetic documents *(source: handover, §5.2; course, Part M, M5; reading sheet 16)*. Partial workaround: plant the same behaviour through several recipes, hold one out, and add another team's organism; for the access question, removing one tool from an audit team measures what it adds; against the gap between implanted and natural itself, none known; say so *(source: course, Part 2, §A, K71; reading sheet 16; course, Part M, M5)*.",
 'ponctuel F·27'))
I.append((1992, 2157, *renvoi('org', 'cas'), 'renvoi F·27'))

# F·35 · Poisoning Constitutional Classifiers
I.append((1998, 2163, *renvoi('cla', 'red'), 'renvoi F·35'))

# F·36 · SGTM — petits modèles ; une sonde muette n'établit pas l'absence
I.append((2004, 2169,
 "> ⚠ *(v3.6)* Le masquage sélectif des gradients n'est montré que sur de petits modèles *(source : cours, volet 2, §I, JB10)* ; et ton test par sondes ne tranche pas seul : sur un modèle désappris, des sondes échouent alors qu'il reste jailbreakable, et une lecture ne voit plus rien quand retirer une direction rend la capacité *(source : cours, volet 10, Deeb et Roger ; cours, volet 10, Łucki et al.)*. Parade : trancher par une intervention, jamais par une lecture — la ré-élicitation à budget fixé d'avance contre une référence jamais entraînée, rapportée comme une borne ; pour la taille des modèles, aucune parade connue ; on le dit *(source : cours, volet 10, Łucki et al. ; cours, volet 2, §I, JB10 ; cours, volet M, M7)*.",
 "> ⚠ *(v3.6)* Selective gradient masking is shown only on small models *(source: course, Part 2, §I, JB10)*; and your probe test does not decide on its own: on an unlearned model, probes fail while it can still be jailbroken, and a reading sees nothing while removing a direction restores the capability *(source: course, Part 10, Deeb and Roger; course, Part 10, Łucki et al.)*. Workaround: decide by an intervention, never by a reading — re-elicitation at a budget fixed in advance against a never-trained reference, reported as a bound; for model size, none known; say so *(source: course, Part 10, Łucki et al.; course, Part 2, §I, JB10; course, Part M, M7)*.",
 'ponctuel F·36'))
I.append((2004, 2169, *renvoi('des', 'son'), 'renvoi F·36'))

# F·40 · Automated Weak-to-Strong Researcher
I.append((2020, 2178, *renvoi('w2s', 'eva'), 'renvoi F·40'))

# F·41 · TASTE
I.append((2026, 2181, *renvoi('jug'), 'renvoi F·41'))

# F·42 · A3
I.append((2030, 2184, *renvoi('red'), 'renvoi F·42'))

# F·26 · Removing Sandbagging
I.append((2037, 2187, *renvoi('eva', 'w2s', 'org'), 'renvoi F·26'))

# D · F·59 · Hebbar
I.append((2049, 2192, *renvoi('mon', 'son'), 'renvoi F·59'))

# D · F·60 · Gasteiger
I.append((2058, 2195, *renvoi('mon'), 'renvoi F·60'))

# D · F·62 · Honesty and lie detection
I.append((2066, 2200, *renvoi('son', 'det', 'pil'), 'renvoi F·62'))


def ancre(fi, n):
    a, b = TR[fi]
    assert a <= n <= b, (fi, n)
    ligne = L[fi][n - 1]
    assert ligne.strip(), (fi, n, 'ligne vide')
    k = sum(1 for i in range(a - 1, b) if L[fi][i].strip() == ligne.strip())
    assert k == 1, (fi, n, k, ligne)
    return ligne


out = []
for nfr, nen, tfr, ten, note in I:
    out.append({'fichier': 'FR', 'ancre': ancre('FR', nfr), 'texte': tfr})
    out.append({'fichier': 'EN', 'ancre': ancre('EN', nen), 'texte': ten})

json.dump({'tranche': 'volet7_B_et_D', 'insertions': out},
          open(f'{W}/travail/insertions_volet7_B_et_D.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(out), 'insertions écrites ;', len(I), 'paires FR/EN')
for nfr, nen, tfr, ten, note in I:
    print(f'  FR l.{nfr} / EN l.{nen} : {note}')
