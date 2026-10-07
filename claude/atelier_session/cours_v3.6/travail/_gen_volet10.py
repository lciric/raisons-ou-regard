#!/usr/bin/env python3
"""Génère travail/insertions_volet10.json (tranche « volet10 » : FR l. 2936-3655, EN l. 3179-3894).

Chaque ancre est tirée par son numéro de ligne dans la v3.5, vérifiée par son début attendu,
puis vérifiée unique dans la tranche (comparaison après strip, comme appliquer.py).
"""
import json, os, re

W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = {'FR': f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md',
       'EN': f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md'}
TR = {'FR': (2936, 3655), 'EN': (3179, 3894)}
REF = f'{W}/travail/referentiel_instruments.md'
OUT = f'{W}/travail/insertions_volet10.json'

L = {k: open(v, encoding='utf8').read().split('\n') for k, v in SRC.items()}


def anchor(fi, n, start):
    s = L[fi][n - 1]
    assert s.startswith(start), (fi, n, s[:120], start)
    a, b = TR[fi]
    assert a <= n <= b, (fi, n)
    cnt = sum(1 for i in range(a - 1, b) if L[fi][i].strip() == s.strip())
    assert cnt == 1, (fi, n, cnt, s[:100])
    return s


# ---------------------------------------------------------------- renvois
LOC = {
    'EVAL': ("évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging »)",
             'behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging")'),
    'SELF': ("auto-rapport et introspection → volet 5, partie II, A, sujet 13",
             "self-report and introspection → Part 5, Section II, A, Topic 13"),
    'ORACLE': ("oracles d'activation → volet 10, fiche LatentQA",
               "activation oracles → Part 10, LatentQA sheet"),
    'PATCH': ("patching → volet 10, fiche Patchscopes",
              "patching → Part 10, Patchscopes sheet"),
    'COT': ("chaîne de pensée comme moniteur → volet 11, réponse 43",
            "chain of thought as a monitor → Part 11, answer 43"),
    'PROBE': ("sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth »)",
              'activation probes → Part 2, §C (after "In practice — The Geometry of Truth")'),
    'MON': ("moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes »)",
            'control monitors → Part 2, §G (after "In practice — coup probes")'),
    'UNSUP': ("élicitation non supervisée → volet 2, §E (fin du cas d'application K52)",
              "unsupervised elicitation → Part 2, §E (end of worked case K52)"),
    'DEBATE': ("débat et supervision évolutive → volet 2, §E (après « En pratique — Debate »)",
               'debate and scalable oversight → Part 2, §E (after "In practice — Debate")'),
    'JUDGE': ("juges LLM → volet 6, §2 (après « La loi de déplacement »)",
              'LLM judges → Part 6, §2 (after "The displacement law")'),
    'W2S': ("généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation »)",
            'weak-to-strong generalization → Part 2, §F (after "In practice — automation")'),
    'STEER': ("pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition »)",
              'steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition")'),
    'RED': ("red-teaming → volet 2, §H (après « En pratique — StrongREJECT »)",
            'red-teaming → Part 2, §H (after "In practice — StrongREJECT")'),
    'CLASSIF': ("classifieurs de sûreté → volet 2, §H (fin du cas d'application G1)",
                "safety classifiers → Part 2, §H (end of worked case G1)"),
    'UNLEARN': ("désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve »)",
                'unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test")'),
    'ABL': ("ablation et projection → volet 2, §D (après « La méthode »)",
            'ablation and projection → Part 2, §D (after "The method")'),
    'RAND': ("contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme »)",
             'random controls → Part M, M4 (after "The matched-norm random direction")'),
    'DEG': ("dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse »)",
            'matched degradation and dose-response → Part M, M4 (after "Dose-response")'),
    'KNOWN': ("cas connu → volet M, M5 (fin de section)",
              "known case → Part M, M5 (end of section)"),
    'ORG': ("organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives »)",
            'model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives")'),
    'EXPL2': ("sondes de désalignement, 2 et 3 : comment les entraîner, et le hors-distribution (encadré du 2 octobre) → volet 2, §C (après « En pratique — Contrastive Activation Addition », avant le cas d'application K47)",
              'misalignment probes, 2 and 3: how to train them, and out of distribution (box of 2 October) → Part 2, §C (after "In practice — Contrastive Activation Addition", before the worked case K47)'),
}


def renvoi(*keys):
    fr = '> ⚠ **Limites et parades** : ' + ' ; '.join(LOC[k][0] for k in keys) + ' *(v3.6)*'
    en = '> ⚠ **Limits and workarounds**: ' + '; '.join(LOC[k][1] for k in keys) + ' *(v3.6)*'
    return fr, en


# ---------------------------------------------------------------- encadrés du référentiel
ref = open(REF, encoding='utf8').read()


def encadre(num):
    m = re.search(rf'^## {num}\. .*?$(.*?)^---$', ref, re.S | re.M)
    bloc = m.group(1)
    out = {}
    for lang, lab in (('FR', 'Encadré complet, français :'), ('EN', 'Encadré complet, anglais :')):
        mm = re.search(re.escape(f'**{lab}**') + r'\s*~~~markdown\n(.*?)\n~~~', bloc, re.S)
        out[lang] = mm.group(1)
    return out


PATCH_BOX = encadre(25)
ORACLE_BOX = encadre(26)
assert PATCH_BOX['FR'].startswith('> **⚠ Limites et parades — Patching')
assert ORACLE_BOX['EN'].startswith('> **⚠ Limits and workarounds — Activation oracles')

# ---------------------------------------------------------------- avertissements ponctuels
WP = {}

WP['sandbagging'] = (
    "> ⚠ *(v3.6)* La parade par sondes reste ici une suggestion non testée, et une sonde muette ne départage pas « pas d'intention » et « sonde aveugle » (cours, volet 10, n° 05 ; passation, §5.2 ; fiches, partie B, piège 3). Parade : mesurer d'abord sa sensibilité et ses fausses alarmes sur un organisme où l'on a installé soi-même la sous-performance — le Mistral 7b verrouillé par mot de passe de ce papier en est un, sans la part stratégique que le papier écarte (cours, volet 10, n° 05) —, son silence ailleurs devenant alors une borne (passation, §5.2) ; ce succès bornerait l'instrument sans prouver qu'il marche sur un sandbagging naturel, et contre cet écart aucune parade connue ; on le dit (passation, §5.2 ; fiche 15).",
    "> ⚠ *(v3.6)* The probe countermeasure remains an untested suggestion here, and a silent probe does not separate \"no intention\" from \"blind probe\" (course, Part 10, no. 05; handover, §5.2; reading sheets, part B, trap 3). Workaround: first measure its sensitivity and false alarms on an organism in which you installed the underperformance yourself — this paper's password-locked Mistral 7b is one, without the strategic part the paper sets aside (course, Part 10, no. 05) —, its silence elsewhere then becoming a bound (handover, §5.2); such a success would bound the instrument without proving it works on natural sandbagging, and against that gap none known; say so (handover, §5.2; reading sheet 15).",
)

WP['sad'] = (
    "> ⚠ *(v3.6)* Ce score mesure ce que le modèle répond quand on lui demande où il se trouve : un auto-rapport, qui n'est pas une croyance (fiche 3 ; fiches, partie B, piège 2), et une conscience verbalisée, qui rate la non verbalisée (cours, volet 7, F·25) ; un score qui dépasse à peine le hasard sur stages-oversight n'établit donc pas que le modèle ne distingue pas évaluation et déploiement : c'est le nul d'un instrument (fiches, partie B, piège 3). Parade : un critère principal comportemental et une sonde latente, la verbalisation n'étant jamais une preuve (programme, partie 8), avec l'instrument validé d'abord sur un organisme conditionné à l'évaluation comme cas connu (programme, parties 4 et 8).",
    "> ⚠ *(v3.6)* This score measures what the model answers when asked where it is: a self-report, which is not a belief (reading sheet 3; reading sheets, part B, trap 2), and verbalized awareness, which misses the unverbalized kind (course, Part 7, F·25); a score barely above chance on stages-oversight therefore does not establish that the model cannot tell evaluation from deployment: it is an instrument's null (reading sheets, part B, trap 3). Workaround: a behavioural main criterion and a latent probe, verbalization never being proof (programme, part 8), with the instrument first validated on an evaluation-conditioned organism as the known case (programme, parts 4 and 8).",
)

WP['monitor'] = (
    "> ⚠ *(v3.6)* Des neurones aléatoires ne sont que le nul de spécificité : ils n'écartent qu'une lecture, que n'importe quelle ablation de cette taille fasse autant, pas le dommage propre aux neurones retirés ni un concept voisin — les auteurs admettent l'hypothèse rivale d'un modèle « distracted », et les concepts ont été trouvés sur le jeu même d'évaluation (cours, volet M, M4 ; cours, volet 10, n° 08). Parade : comparer à dégradation appariée, contre plusieurs familles de témoins (cours, volet M, M4 ; programme, parties 3 et 7), et choisir les neurones sur un jeu disjoint de celui qui les évalue (README du dépôt).",
    "> ⚠ *(v3.6)* Random neurons are only the specificity null: they rule out a single reading, that any ablation of that size does as much, not the damage specific to the removed neurons nor a neighbouring concept — the authors admit the rival hypothesis of a \"distracted\" model, and the concepts were found on the evaluation set itself (course, Part M, M4; course, Part 10, no. 08). Workaround: compare at matched degradation, against several families of controls (course, Part M, M4; programme, parts 3 and 7), and choose the neurons on a set disjoint from the one that evaluates them (repository README).",
)

WP['selfie'] = (
    "> ⚠ *(v3.6)* Un contrôle aléatoire n'est que le nul de spécificité : il n'écarte ni le dommage propre à l'intervention ni un corrélat, et ne suffit donc pas au test causal (cours, volet M, M4 ; passation, §5.2) ; quant à la lecture, sa fidélité n'est mesurée que contre des sondes linéaires, sans vérité-terrain des latents (cours, volet 10, n° 13 et n° 16). Parade : comparer l'intervention à des témoins à dégradation appariée, en courbe dose-réponse (cours, volet M, M4 ; cours, volet 2, §C, K47), et tester le décodage sur des variantes fine-tunées à comportement connu, jamais vues (fiche 18).",
    "> ⚠ *(v3.6)* A random control is only the specificity null: it rules out neither the damage specific to the intervention nor a correlate, so it is not enough for the causal test (course, Part M, M4; handover, §5.2); as for the reading, its faithfulness is measured only against linear probes, with no ground truth for latents (course, Part 10, no. 13 and no. 16). Workaround: compare the intervention with controls at matched degradation, as a dose-response curve (course, Part M, M4; course, Part 2, §C, K47), and test the decoding on fine-tuned variants with known behaviour, never seen before (reading sheet 18).",
)

WP['latentqa'] = (
    "> ⚠ *(v3.6)* Ce gain de débiaisage se compare au prompting, à RepE, au SFT et au DPO ; la fiche ne mentionne aucun témoin à dégradation appariée, or le dommage ne s'écarte qu'à dégradation appariée (cours, volet 10, n° 16 ; cours, volet M, M4). Parade : tracer l'effet contre le dommage mesuré, contre plusieurs témoins (cours, volet 2, §C, K47 ; programme, partie 7) ; et, pour dire quelle structure porte l'effet, la partition causale : la part d'une direction nommée contre celle de l'état complet aux mêmes sites (cours, volet 6, §2 ; programme, partie 8).",
    "> ⚠ *(v3.6)* This debiasing gain is compared with prompting, RepE, SFT and DPO; the sheet mentions no control at matched degradation, yet damage is ruled out only at matched degradation (course, Part 10, no. 16; course, Part M, M4). Workaround: plot the effect against measured damage, against several controls (course, Part 2, §C, K47; programme, part 7); and, to say which structure carries the effect, the causal partition: the share of a named direction against that of the full state at the same sites (course, Part 6, §2; programme, part 8).",
)

WP['ecfinetuning'] = (
    "> ⚠ *(v3.6)* Ces cohérences sont notées par un LLM qui simule l'utilisateur, contrôlé pour sa stabilité et contre un effet de longueur ; la fiche ne rapporte aucun audit humain, et un juge LLM a des erreurs systématiques (cours, volet 10, n° 21 ; cours, volet 6, §2 ; fiches, partie B, piège 6). Parade : un juge scellé (prompt, modèle et température gelés) et un audit humain d'environ 200 items stratifiés, l'accord rapporté (programme, partie 3).",
    "> ⚠ *(v3.6)* These consistency scores are given by an LLM that simulates the user, checked for stability and against a length effect; the sheet reports no human audit, and an LLM judge has systematic errors (course, Part 10, no. 21; course, Part 6, §2; reading sheets, part B, trap 6). Workaround: a sealed judge (prompt, model and temperature frozen) and a human audit of about 200 stratified items, agreement reported (programme, part 3).",
)

WP['naihin'] = (
    "> ⚠ *(v3.6)* Ces scores sont mesurés contre 30 sorties dangereuses et 27 hors tâche écrites à la main, sans red team qui optimise contre le moniteur ; or un chiffre de sûreté dépend de la force de la red team (cours, volet 10, n° 24 ; cours, volet 7, F·24). Parade : dire quelle red team le chiffre suppose, au moins une red team optimisée composante par composante (cours, volet 7, F·24), et calibrer le seuil à 1 % de faux positifs sur des variantes bénignes appariées (cours, volet 7, F·23).",
    "> ⚠ *(v3.6)* These scores are measured against 30 dangerous and 27 off-task outputs written by hand, with no red team optimizing against the monitor; yet a safety number depends on the red team's strength (course, Part 10, no. 24; course, Part 7, F·24). Workaround: say which red team the number assumes, at least one optimized component by component (course, Part 7, F·24), and calibrate the threshold at 1% false positives on paired benign variants (course, Part 7, F·23).",
)

WP['hidden'] = (
    "> ⚠ *(v3.6)* La détection en boîte blanche n'est ici qu'une piste, non testée ; et le papier observe déjà qu'une surveillance peut encourager une collusion plus subtile : itérer contre ses détecteurs sélectionne l'évasion (cours, volet 10, n° 26 ; fiche 19). Parade : des détecteurs scellés, hors de la boucle d'entraînement — s'ils continuent de se déclencher quand ceux de la boucle se taisent, l'évasion a été sélectionnée (fiche 19) — et, pour une sonde en boîte blanche, son cas connu d'abord (passation, §5.2).",
    "> ⚠ *(v3.6)* White-box detection is only a lead here, untested; and the paper already observes that oversight can encourage subtler collusion: iterating against your detectors selects for evasion (course, Part 10, no. 26; reading sheet 19). Workaround: sealed detectors, outside the training loop — if they keep firing when the in-loop ones go quiet, evasion has been selected (reading sheet 19) — and, for a white-box probe, its known case first (handover, §5.2).",
)

WP['coup'] = (
    "> ⚠ *(v3.6)* Ce rappel parfait porte sur des positifs écrits par un autre modèle, dans un jouet, et la généralisation montrée va d'un format à l'autre et sous jailbreak : un score en distribution ne prouve rien, c'est l'écart avec des familles tenues à part qui se mesure (cours, volet 10, n° 27 ; fiches, partie B, piège 1 ; fiche 7). Parade : tenir à part des familles entières, jamais des paraphrases, et des formats jusqu'à l'agentique à plusieurs tours (explication du 2 octobre, §3 ; programme, partie 3) ; valider sur des générations du modèle surveillé, étiquetées par leur conduite et jamais par la sonde (cours, volet 6, §8 ; passation, §5.1 et §5.2) ; et mesurer la sonde d'abord sur un organisme où l'on a installé l'intention soi-même (passation, §5.2).",
    "> ⚠ *(v3.6)* This perfect recall concerns positives written by another model, in a toy, and the generalization shown goes from one format to another and under jailbreak: an in-distribution score proves nothing, what you measure is the gap with held-out families (course, Part 10, no. 27; reading sheets, part B, trap 1; reading sheet 7). Workaround: hold out whole families, never paraphrases, and formats up to multi-turn agentic (explanation of 2 October, §3; programme, part 3); validate on generations of the monitored model, labelled by their conduct and never by the probe (course, Part 6, §8; handover, §5.1 and §5.2); and first measure the probe on an organism in which you installed the intention yourself (handover, §5.2).",
)

WP['quirky'] = (
    "> ⚠ *(v3.6)* Ces AUROC viennent d'organismes dont la fausseté suit un nom visible dans le prompt : sonde et détecteur peuvent lire la façon dont l'organisme a été fabriqué plutôt que l'intention, et un succès sur organisme borne l'instrument sans prouver qu'il marche sur un cas naturel (cours, volet 10, n° 30 ; cours, volet 6, §8 ; passation, §5.2). Parade, en partie : deux fabrications du même comportement, dont une tenue à part, et un organisme conscient mais honnête comme témoin (cours, volet 6, §8 ; cours, volet 2, §A, K71) ; pour conclure sur le cas naturel, aucune parade connue ; on le dit.",
    "> ⚠ *(v3.6)* These AUROCs come from organisms whose falsehood follows a name visible in the prompt: probe and detector may read how the organism was made rather than the intention, and a success on an organism bounds the instrument without proving it works on a natural case (course, Part 10, no. 30; course, Part 6, §8; handover, §5.2). Workaround, in part: two manufactures of the same behaviour, one of them held out, and an aware-but-honest organism as the control (course, Part 6, §8; course, Part 2, §A, K71); to conclude about the natural case, none known; say so.",
)

WP['pvg'] = (
    "> ⚠ *(v3.6)* Contre ce risque d'un moniteur qui apprend le style de l'attaquant plutôt que l'erreur, la parade : un classifieur de la seule surface doit rester au hasard entre les deux côtés des exemples, et les négatifs se tirent des générations réelles du modèle, pas d'exemples fabriqués (cours, volet M, M4 ; cours, volet 2, §C).",
    "> ⚠ *(v3.6)* Against this risk of a monitor that learns the attacker's style rather than the error, the workaround: a surface-only classifier must stay at chance between the two sides of the examples, and negatives are drawn from the model's real generations, not from fabricated examples (course, Part M, M4; course, Part 2, §C).",
)

WP['azaria'] = (
    "> ⚠ *(v3.6)* Ces sondes de vérité sont validées sur des énoncés faux ordinaires, pas sur un modèle qui ment : comme détecteur de mensonge, il leur manque le cas connu, et sur l'honnêteté des sondes de vérité ont déjà fait moins bien qu'un simple prompt (cours, volet 10, n° 51 ; passation, §5.2 ; cours, volet 7, F·62). Parade : mesurer sensibilité et fausses alarmes sur un organisme où l'on a installé soi-même l'intention de tromper (passation, §5.2), et battre un prompt à coût égal, en rapportant le rappel à 1 % de faux positifs (cours, volet 5, sujet 1 ; cours, volet 7, F·50 ; cours, volet 7, F·29).",
    "> ⚠ *(v3.6)* These truth probes are validated on ordinary false statements, not on a model that lies: as a lie detector, they lack the known case, and on honesty truth probes have already done worse than a plain prompt (course, Part 10, no. 51; handover, §5.2; course, Part 7, F·62). Workaround: measure sensitivity and false alarms on an organism in which you installed the intention to deceive yourself (handover, §5.2), and beat a prompt at equal cost, reporting recall at 1% false positives (course, Part 5, topic 1; course, Part 7, F·50; course, Part 7, F·29).",
)

WP['repe'] = (
    "> ⚠ *(v3.6)* Ces gains de contrôle se comparent à des baselines, dont un vecteur aléatoire, et la fiche ne mentionne aucun témoin à dégradation appariée (cours, volet 10, n° 53) ; or un vecteur aléatoire n'est que le nul de spécificité, et le dommage ne s'écarte qu'à dégradation appariée (cours, volet M, M4). Parade : une courbe dose-réponse contre plusieurs témoins, la courbe du concept devant passer au-dessus à chaque niveau de dommage (cours, volet 2, §C, K47 ; programme, partie 7).",
    "> ⚠ *(v3.6)* These control gains are compared with baselines, including a random vector, and the sheet mentions no control at matched degradation (course, Part 10, no. 53); yet a random vector is only the specificity null, and damage is ruled out only at matched degradation (course, Part M, M4). Workaround: a dose-response curve against several controls, the concept's curve having to run above them at every level of damage (course, Part 2, §C, K47; programme, part 7).",
)

WP['caa'] = (
    "> ⚠ *(v3.6)* Ces effets se comparent aux prompts système et au fine-tuning, les capacités sont mesurées par MMLU et TruthfulQA, et le texte libre est noté par GPT-4 avec un échantillon vérifié à la main ; la fiche ne mentionne aucun témoin à dégradation appariée (cours, volet 10, n° 54), or le dommage ne s'écarte qu'à dégradation appariée (cours, volet M, M4), et dans ton dépôt l'addition d'activations contrastives forçait un artefact de polarité oui/non (README du dépôt). Parade : une courbe dose-réponse contre plusieurs témoins (cours, volet 2, §C, K47) et un juge scellé avec un audit humain d'environ 200 items stratifiés (programme, partie 3) ; contre l'artefact de polarité, aucune parade connue ; on le dit.",
    "> ⚠ *(v3.6)* These effects are compared with system prompts and fine-tuning, capabilities are measured with MMLU and TruthfulQA, and free text is scored by GPT-4 with a sample checked by hand; the sheet mentions no control at matched degradation (course, Part 10, no. 54), yet damage is ruled out only at matched degradation (course, Part M, M4), and in your repository contrastive activation addition forced a yes/no polarity artefact (repository README). Workaround: a dose-response curve against several controls (course, Part 2, §C, K47) and a sealed judge with a human audit of about 200 stratified items (programme, part 3); against the polarity artefact, none known; say so.",
)

WP['iti'] = (
    "> ⚠ *(v3.6)* La direction aléatoire n'est ici que le nul de spécificité, et le prix mesuré — un KL qui monte, plus de « I have no comment » — est un dommage ; la fiche ne dit pas que les directions ont été comparées à dégradation appariée, si bien que « agit plus » peut vouloir dire « abîme plus » (cours, volet 10, n° 55 ; cours, volet M, M4). Parade : tracer l'effet de chaque direction contre le dommage mesuré, KL compris, et ne retenir que celle dont la courbe passe au-dessus des témoins à chaque niveau de dommage (cours, volet 2, §C, K47 ; programme, partie 7).",
    "> ⚠ *(v3.6)* The random direction is only the specificity null here, and the measured price — a rising KL, more \"I have no comment\" — is damage; the sheet does not say the directions were compared at matched degradation, so \"acts more\" may mean \"damages more\" (course, Part 10, no. 55; course, Part M, M4). Workaround: plot each direction's effect against measured damage, KL included, and keep only the one whose curve runs above the controls at every level of damage (course, Part 2, §C, K47; programme, part 7).",
)

WP['agentdojo'] = (
    "> ⚠ *(v3.6)* Ces taux de défense sont mesurés contre des attaques que les auteurs disent eux-mêmes simples : une red team faible fait paraître la défense sûre (cours, volet 10, n° 58 ; cours, volet 7, F·24). Parade : une red team optimisée composante par composante, avec l'ablation de chaque composante, et dire quelle red team le chiffre suppose (cours, volet 7, F·24).",
    "> ⚠ *(v3.6)* These defence rates are measured against attacks the authors themselves call simple: a weak red team makes the defence look safe (course, Part 10, no. 58; course, Part 7, F·24). Workaround: a red team optimized component by component, with each component ablated, and say which red team the number assumes (course, Part 7, F·24).",
)

WP['rapid'] = (
    "> ⚠ *(v3.6)* Ces facteurs sont mesurés contre six stratégies d'attaque fixes, en variantes dans et hors distribution, sans attaquant qui connaît la défense et optimise contre elle, ce que les auteurs laissent ouvert (cours, volet 10, n° 63) ; or une red team faible fait paraître la défense sûre (cours, volet 7, F·24), et compter des contournements ne dit pas ce que le garde retire à l'attaquant (cours, volet 2, §H, G1). Parade : une red team optimisée composante par composante (cours, volet 7, F·24), et classer les défenses deux fois, par taux de refus et par préjudice différentiel (cours, volet 2, §H, G1).",
    "> ⚠ *(v3.6)* These factors are measured against six fixed attack strategies, in in-distribution and out-of-distribution variants, with no attacker who knows the defence and optimizes against it, which the authors leave open (course, Part 10, no. 63); yet a weak red team makes the defence look safe (course, Part 7, F·24), and counting bypasses does not say what the guard takes away from the attacker (course, Part 2, §H, G1). Workaround: a red team optimized component by component (course, Part 7, F·24), and rank the defences twice, by refusal rate and by differential harm (course, Part 2, §H, G1).",
)

WP['wmdp'] = (
    "> ⚠ *(v3.6)* Une sonde muette est le nul d'un instrument, pas une absence (fiches, partie B, piège 3). Parade : trancher par une intervention, jamais par une lecture (cours, volet 10, n° 64 ; fiches, partie C), et ré-éliciter contre une référence jamais entraînée, au même budget, avec un modèle connu pour masquer comme cas connu, puis dire une borne, « not elicitable at this budget » (cours, volet M, M4 et M5 ; cours, volet 2, §I).",
    "> ⚠ *(v3.6)* A silent probe is an instrument's null, not an absence (reading sheets, part B, trap 3). Workaround: decide by an intervention, never by a reading (course, Part 10, no. 64; reading sheets, part C), and re-elicit against a never-trained reference, at the same budget, with a model known to mask as the known case, then state a bound, \"not elicitable at this budget\" (course, Part M, M4 and M5; course, Part 2, §I).",
)

# ---------------------------------------------------------------- plan : (ligne FR, début FR, ligne EN, début EN, (texte FR, texte EN))
PLAN = [
    # Evaluating capabilities — GPQA
    (3052, '*n° 01 — Lecture', 3295, '*no. 01 — Reading', renvoi('EVAL')),
    # Evaluating alignment — AI Sandbagging (n° 05)
    (3077, '**Ce que ça change pour la préparation.** Axe 3 : la détection comportementale', 3319, '**What it changes for the preparation.** Axis 3: behavioral detection', WP['sandbagging']),
    (3079, '*n° 05 — Lecture', 3321, '*no. 05 — Reading', renvoi('EVAL', 'PROBE', 'KNOWN')),
    # Understanding model cognition — SAD (n° 07)
    (3089, '**Le résultat, chiffré.** Tous font mieux que le hasard', 3331, '**The result, in numbers.** All do better than chance', WP['sad']),
    (3094, '*n° 07 — Lecture', 3336, '*no. 07 — Reading', renvoi('EVAL', 'SELF')),
    # Monitor (n° 08)
    (3102, '**Ce que ça change pour la préparation.** Axe 2 : la démonstration sépare', 3344, '**What it changes for the preparation.** Axis 2: the demonstration separates', WP['monitor']),
    (3104, '*n° 08 — Lecture', 3346, '*no. 08 — Reading', renvoi('ABL', 'RAND', 'DEG')),
    # Second-order effects in CLIP (n° 09)
    (3114, '*n° 09 — Lecture', 3356, '*no. 09 — Reading', renvoi('ABL', 'RAND')),
    # Chain-of-thought prompting (n° 11)
    (3126, '*n° 11 — Lecture', 3368, '*No. 11 — Reading', renvoi('COT')),
    # Looking Inward (n° 12)
    (3136, '*n° 12 — Lecture', 3378, '*No. 12 — Reading', renvoi('SELF')),
    # SelfIE (n° 13)
    (3144, '**Ce que ça change pour la préparation.** Lien avec l\'axe 2 : SelfIE', 3386, '**What it changes for the preparation.** Link with axis 2: SelfIE', WP['selfie']),
    (3146, '*n° 13 — Lecture', 3388, '*No. 13 — Reading', renvoi('ORACLE', 'SELF', 'PATCH')),
    # Patchscopes (n° 14) — maison de l'encadré « Patching »
    (3156, '*n° 14 — Lecture', 3398, '*No. 14 — Reading', (PATCH_BOX['FR'], PATCH_BOX['EN'])),
    # LatentQA (n° 16) — maison de l'encadré « Oracles d'activation »
    (3174, '**Ce que ça change pour la préparation.** Lien avec l\'axe 2 : piloter', 3416, '**What it changes for the preparation.** Link with axis 2: steering', WP['latentqa']),
    (3176, '*n° 16 — Lecture', 3418, '*No. 16 — Reading', (ORACLE_BOX['FR'], ORACLE_BOX['EN'])),
    # Chain-of-thought faithfulness (préambule de section, après n° 18)
    (3183, '*n° 18 · Measuring Faithfulness', 3424, '*No. 18 · Measuring Faithfulness', renvoi('COT')),
    # Explanation-consistency finetuning (n° 21)
    (3208, '**Le résultat, chiffré.** « EC-finetuning yields', 3449, '**The result, in numbers.** "EC-finetuning yields', WP['ecfinetuning']),
    # Behavioral monitoring — Naihin (n° 24)
    (3236, '**Le résultat, chiffré.** Sur le test', 3476, '**The result, in numbers.** On the test set', WP['naihin']),
    (3241, '*n° 24 — Lecture', 3481, '*No. 24 — Reading', renvoi('MON', 'JUDGE')),
    # Hidden in Plain Text (n° 26)
    (3259, '**Ce que ça change pour la préparation.** Axe 4 : dans le cadre même', 3499, '**What it changes for the preparation.** Axis 4: in the program', WP['hidden']),
    (3261, '*n° 26 — Lecture', 3501, '*No. 26 — Reading', renvoi('MON', 'RED')),
    # Activation monitoring — Coup probes (n° 27)
    (3269, '**Le résultat, chiffré.** Les 46 points', 3509, '**The result, in numbers.** The 46 unmodified', WP['coup']),
    (3274, '*n° 27 — Lecture', 3514, '*No. 27 — Reading', renvoi('PROBE', 'MON', 'EXPL2')),
    # Circuit Breakers (n° 28)
    (3284, '*n° 28 — Lecture', 3524, '*No. 28 — Reading', renvoi('RED', 'CLASSIF')),
    # Anomaly detection — Quirky (n° 30)
    (3302, '**Le résultat, chiffré.** « The best probing method', 3542, '**The result, in numbers.** "The best probing method', WP['quirky']),
    (3307, '*n° 30 — Lecture', 3547, '*No. 30 — Reading', renvoi('PROBE', 'MON', 'UNSUP', 'ORG')),
    # Recursive oversight — Debate Helps (n° 37)
    (3375, '*n° 37 — Lecture', 3614, '*No. 37 — Reading', renvoi('DEBATE')),
    # Kenton et al. (n° 39)
    (3387, '*n° 39 — Lecture', 3626, '*No. 39 — Reading', renvoi('JUDGE')),
    # Prover-Verifier Games (n° 40)
    (3395, '**Ce que ça change pour la préparation.** Lien indirect avec l\'axe 3 : l\'annexe C', 3634, '**What it changes for the preparation.** Indirect link with Axis 3: Appendix C', WP['pvg']),
    # Weak-to-strong (préambule de section, après n° 41)
    (3402, '*n° 41 · Weak-to-Strong Generalization', 3641, '*No. 41 · Weak-to-Strong Generalization', renvoi('W2S')),
    # Honesty — Azaria & Mitchell (n° 51)
    (3495, '**Ce que ça change pour la préparation.** Lien direct (axe 3)', 3733, '**What it changes for the preparation.** Direct link (axis 3)', WP['azaria']),
    # Honesty — après n° 52 (Geometry of Truth)
    (3499, '*n° 52 · The Geometry of Truth', 3737, '*No. 52 · The Geometry of Truth', renvoi('PROBE', 'STEER', 'UNSUP', 'EXPL2')),
    # RepE (n° 53)
    (3504, '**Le résultat, chiffré.** TruthfulQA MC1', 3742, '**The result, in numbers.** TruthfulQA MC1', WP['repe']),
    # CAA (n° 54)
    (3514, '**Le résultat, chiffré.** Couche optimale', 3752, '**The result, in numbers.** Optimal layer', WP['caa']),
    # ITI (n° 55)
    (3524, '**Le résultat, chiffré.** « we observe a full', 3762, '**The result, in numbers.** "we observe a full', WP['iti']),
    # Adversarial robustness — Poisoning (n° 57)
    (3552, '*n° 57 — Lecture', 3789, '*No. 57 — Reading', renvoi('RED', 'CLASSIF')),
    # AgentDojo (n° 58)
    (3557, '**Le résultat, chiffré.** « more capable models', 3794, '**The result, in numbers.** "more capable models', WP['agentdojo']),
    # Realistic and differential benchmarks — StrongREJECT (n° 59)
    (3575, '*n° 59 — Lecture', 3812, '*No. 59 — Reading', renvoi('RED', 'JUDGE', 'EVAL')),
    # Adaptive defenses — Rapid Response (n° 63)
    (3613, '**Le résultat, chiffré.** Guard Fine-tuning', 3850, '**The result, in numbers.** Guard Fine-tuning', WP['rapid']),
    (3618, '*n° 63 — Lecture', 3855, '*No. 63 — Reading', renvoi('RED', 'CLASSIF')),
    # Unlearning — Łucki et al. (n° 64)
    (3631, '*n° 64 — Lecture', 3867, '*No. 64 — Reading', renvoi('UNLEARN')),
    # WMDP (n° 65)
    (3639, '**Ce que ça change pour la préparation.** Lien indirect avec les axes 2 et 3', 3875, '**What it changes for the preparation.** Indirect link with axes 2 and 3', WP['wmdp']),
]

ins = []
for frn, frs, enn, ens, (tfr, ten) in PLAN:
    ins.append({'fichier': 'FR', 'ancre': anchor('FR', frn, frs), 'texte': tfr})
    ins.append({'fichier': 'EN', 'ancre': anchor('EN', enn, ens), 'texte': ten})

# pas deux insertions sur la même ancre
for fi in ('FR', 'EN'):
    a = [i['ancre'] for i in ins if i['fichier'] == fi]
    assert len(a) == len(set(a)), fi

json.dump({'tranche': 'volet10', 'insertions': ins}, open(OUT, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(ins), 'insertions écrites dans', OUT)
