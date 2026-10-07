#!/usr/bin/env python3
"""Génère travail/insertions_volet3.json (tranche volet3 : FR l. 885-1110 ; EN l. 1007-1251).

Les ancres sont lues directement dans les sources v3.5 par numéro de ligne, puis vérifiées
uniques dans la tranche (même normalisation que outils/appliquer.py).
"""
import json, os

W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = {'FR': f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md',
       'EN': f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md'}
TR = {'FR': (885, 1110), 'EN': (1007, 1251)}
L = {k: open(v, encoding='utf8').read().split('\n') for k, v in SRC.items()}

# ---------------------------------------------------------------------------
# Renvois d'une ligne
# ---------------------------------------------------------------------------
RV = {
    'evals': ("évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging »)",
              'behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging")'),
    'juges': ("juges LLM → volet 6, §2 (après « La loi de déplacement »)",
              'LLM judges → Part 6, §2 (after "The displacement law")'),
    'auto': ("auto-rapport et introspection → volet 5, partie II, A, sujet 13",
             'self-report and introspection → Part 5, Section II, A, Topic 13'),
    'cot': ("chaîne de pensée comme moniteur → volet 11, réponse 43",
            'chain of thought as a monitor → Part 11, answer 43'),
    'orga': ("organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives »)",
             'model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives")'),
    'moni': ("moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes »)",
             'control monitors → Part 2, §G (after "In practice — coup probes")'),
    'sondes': ("sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth »)",
               'activation probes → Part 2, §C (after "In practice — The Geometry of Truth")'),
    'nla': ("autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle",
            'natural-language autoencoders → Part 4, The recent wave on model cognition'),
    'pilot': ("pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition »)",
              'steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition")'),
    'debat': ("débat et supervision évolutive → volet 2, §E (après « En pratique — Debate »)",
              'debate and scalable oversight → Part 2, §E (after "In practice — Debate")'),
    'w2s': ("généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation »)",
            'weak-to-strong generalization → Part 2, §F (after "In practice — automation")'),
    'elic': ("élicitation non supervisée → volet 2, §E (fin du cas d'application K52)",
             'unsupervised elicitation → Part 2, §E (end of worked case K52)'),
    'red': ("red-teaming → volet 2, §H (après « En pratique — StrongREJECT »)",
            'red-teaming → Part 2, §H (after "In practice — StrongREJECT")'),
    'classif': ("classifieurs de sûreté → volet 2, §H (fin du cas d'application G1)",
                'safety classifiers → Part 2, §H (end of worked case G1)'),
    'desap': ("désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve »)",
              'unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test")'),
    'detect': ("détecteurs fine-tunés → volet 7, F·29",
               'fine-tuned detectors → Part 7, F·29'),
    'oracle': ("oracles d'activation → volet 10, fiche LatentQA",
               'activation oracles → Part 10, LatentQA sheet'),
    'sae': ("dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity",
            'dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity'),
    'abla': ("ablation et projection → volet 2, §D (après « La méthode »)",
             'ablation and projection → Part 2, §D (after "The method")'),
    'alea': ("contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme »)",
             'random controls → Part M, M4 (after "The matched-norm random direction")'),
    'degr': ("dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse »)",
             'matched degradation and dose-response → Part M, M4 (after "Dose-response")'),
}


def renvoi(*cles):
    fr = '> ⚠ **Limites et parades** : ' + ' ; '.join(RV[c][0] for c in cles) + ' *(v3.6)*'
    en = '> ⚠ **Limits and workarounds**: ' + '; '.join(RV[c][1] for c in cles) + ' *(v3.6)*'
    return fr, en


# ---------------------------------------------------------------------------
# Avertissements ponctuels (FR, EN)
# ---------------------------------------------------------------------------
W_JB2 = (
    "> ⚠ *(v3.6)* Ce point vient d'une évaluation de sabotage dont le Risk Report d'août concède lui-même les limites (§2.16) : des évaluations non tirées des vrais chemins de risque, une tâche secondaire dans le prompt, des modèles probablement conscients d'être évalués (fiche 3). Parade : une élicitation à budget fixé d'avance, rapportée comme une borne (cours, volet M, M7 ; cours, volet 2, §B, K63) ; contre le modèle qui se retient, deux versions d'un environnement, tirées au hasard, qui ne diffèrent que par des indices de réalisme notés par un discriminateur, avec un organisme dressé à se cacher comme cas connu (cours, volet 2, §B, K63).",
    "> ⚠ *(v3.6)* This point comes from a sabotage evaluation whose limits the August Risk Report itself concedes (§2.16): evaluations not drawn from the real risk pathways, a secondary task in the prompt, models probably aware of being evaluated (reading sheet 3). Workaround: elicitation at a budget fixed in advance, reported as a bound (course, Part M, M7; course, Part 2, §B, K63); against a model that holds back, two versions of an environment, randomly assigned, differing only in realism cues scored by a discriminator, with an organism trained to hide as the known case (course, Part 2, §B, K63).",
)

W_K48 = (
    "> ⚠ *(v3.6)* Le test des indices mesure ce que la chaîne verbalise, pas le calcul qui a produit la réponse : une chaîne qui ne nomme pas l'indice n'est pas, par là, un raisonnement caché (fiche 17). Parade : dire « not verbalized », jamais « hidden reasoning », et mesurer la surveillabilité comme un ratio — le verbalisé contre l'interne ou les actions —, par une perturbation graduée de la chaîne (fiche 17 ; cours, volet 11, réponse 43).",
    "> ⚠ *(v3.6)* The hint test measures what the chain verbalizes, not the computation that produced the answer: a chain that does not name the hint is not, for that reason, hidden reasoning (reading sheet 17). Workaround: say \"not verbalized\", never \"hidden reasoning\", and measure monitorability as a ratio — the verbalized against the internal or the actions —, through graded perturbation of the chain (reading sheet 17; course, Part 11, answer 43).",
)

W_CANAL = (
    "> ⚠ *(v3.6)* Ce canal a ses propres façons d'échouer : au seuil d'un moniteur, des sondes rappellent 43 % à 1 % de faux positifs, contre 55 % pour le meilleur moniteur LLM (cours, volet 7, F·51), et itérer contre ses détecteurs sélectionne l'évasion (fiche 19). Parade : rapporter le rappel à 1 % de faux positifs face à une baseline boîte noire à coût égal (cours, volet 7, F·50 ; cours, volet 5, sujet 1), et garder des détecteurs scellés, hors de la boucle : s'ils continuent de se déclencher quand ceux de la boucle se taisent, l'évasion a été sélectionnée (fiche 19).",
    "> ⚠ *(v3.6)* This channel has its own ways of failing: at a monitor's threshold, probes recall 43% at 1% false positives, against 55% for the best LLM monitor (course, Part 7, F·51), and iterating against your detectors selects for evasion (reading sheet 19). Workaround: report recall at 1% false positives against a black-box baseline at equal cost (course, Part 7, F·50; course, Part 5, topic 1), and keep sealed detectors, outside the loop: if they keep firing when the in-loop ones go quiet, evasion has been selected (reading sheet 19).",
)

W_K70_LECTURES = (
    "> ⚠ *(v3.6)* Le constat de la carte Fable 5 oppose la sonde à deux instruments qui ont leurs propres limites : le NLA peut confabuler (fiche 18), les réponses aux questions de suivi dépendent de leur formulation (fiche 3), et les trois mesures n'y sont que « weakly positively correlated » (fiche 2) ; il montre que la sonde se tait, pas laquelle des lectures a raison. Parade : trianguler, et dire quelle mesure a fondé quel chiffre (cours, volet 5, sujet 4 ; cours, volet M, M4), en mesurant les contrôles par un instrument indépendant du NLA (fiche 18).",
    "> ⚠ *(v3.6)* The Fable 5 card's finding sets the probe against two instruments with limits of their own: the NLA can confabulate (reading sheet 18), answers to follow-up questions depend on how they are phrased (reading sheet 3), and the three measures there are only \"weakly positively correlated\" (reading sheet 2); it shows that the probe stays silent, not which reading is right. Workaround: triangulate, and say which measure grounded which number (course, Part 5, topic 4; course, Part M, M4), measuring the controls with an instrument independent of the NLA (reading sheet 18).",
)

W_K70_JUGE = (
    "> ⚠ *(v3.6)* Le juge plus lent qui étiquette l'échantillon frais est lui-même un instrument, ici non audité : un juge a des erreurs systématiques (cours, volet 6, §2), et un juge qui lit le raisonnement se laisse persuader — environ 1 % des actions signalées avec la chaîne de pensée, environ 50 % sans, pour un seul moniteur (fiche 3). Parade : un juge scellé et un audit humain d'environ 200 items stratifiés, l'accord rapporté (programme, partie 3), qui juge les actions, leurs sorties et les messages, pas le texte qui précède l'action (passation, §5.1).",
    "> ⚠ *(v3.6)* The slower judge that labels the fresh sample is itself an instrument, unaudited here: a judge has systematic errors (course, Part 6, §2), and a judge that reads the reasoning gets persuaded — about 1% of actions flagged with the chain of thought, about 50% without, for a single monitor (reading sheet 3). Workaround: a sealed judge and a human audit of about 200 stratified items, agreement reported (programme, part 3), judging the actions, their outputs and the messages, not the text before the action (handover, §5.1).",
)

# Avertissement prêt du référentiel (partie « Par tranche », volet3), repris mot pour mot.
W_K67 = (
    "> ⚠ *(v3.6)* La sonde de défection a été validée sur une porte implantée : la meilleure de 1 000 directions aléatoires y atteint déjà 95,3 %, et la saillance peut venir de l'insertion (fiche 15). Un succès sur organisme borne l'instrument ; pour un modèle devenu trompeur de lui-même, aucune parade connue (cours, volet M, M5).",
    "> ⚠ *(v3.6)* The defection probe was validated on an implanted backdoor: the best of 1,000 random directions already reaches 95.3% there, and salience may come from the insertion (reading sheet 15). A success on an organism bounds the instrument; for a model that became deceptive on its own, no workaround is known (course, Part M, M5).",
)

W_JB9 = (
    "> ⚠ *(v3.6)* L'« immunité quasi totale » rapportée par le papier Mind Viruses a été mesurée par des modèles juges, qui peuvent compter un écho poli comme une adoption (cours, volet 3, §6, K13), et une défense ne vaut que contre la red team qui l'a éprouvée : une red team faible la fait paraître sûre (cours, volet 7, F·24). Parade : ne compter que les étapes réellement agies et refaire noter un échantillon à la main (cours, volet 3, §6, K13) ; dire quelle red team le chiffre suppose, au moins une red team optimisée composante par composante, avec l'ablation de chaque composante (cours, volet 7, F·24).",
    "> ⚠ *(v3.6)* The \"near-total immunity\" reported by the Mind Viruses paper was measured with model judges, which can count a polite echo as adoption (course, Part 3, §6, K13), and a defence holds only against the red team that tested it: a weak red team makes it look safe (course, Part 7, F·24). Workaround: count only the steps actually acted on and have a sample re-scored by hand (course, Part 3, §6, K13); say which red team the number assumes, at least one optimized component by component, with each component ablated (course, Part 7, F·24).",
)

W_REELIC = (
    "> ⚠ *(v3.6)* La ré-élicitation ne tranche que dans un sens : si le savoir ne revient pas plus vite, on signe une borne, « not elicitable at this budget », jamais une absence (fiches, partie C) ; et un petit fine-tuning peut enseigner au lieu de révéler (cours, volet M, M9). Parade : des faits construits indépendants, la référence jamais entraînée au même budget, et un modèle connu pour masquer comme cas connu (cours, volet M, M4, M5 et M9 ; cours, volet 2, §I) ; pour des capacités plutôt que des faits à faible fuite, aucune parade connue ; on le dit (cours, volet 10, Deeb et Roger).",
    "> ⚠ *(v3.6)* Re-elicitation decides in one direction only: if the knowledge does not come back faster, you sign a bound, \"not elicitable at this budget\", never an absence (reading sheets, part C); and a small fine-tune can teach instead of revealing (course, Part M, M9). Workaround: facts built to be independent, the never-trained reference at the same budget, and a model known to mask as the known case (course, Part M, M4, M5 and M9; course, Part 2, §I); for capabilities rather than low-leakage facts, none known; say so (course, Part 10, Deeb and Roger).",
)

W_STEER = (
    "> ⚠ *(v3.6)* Cet ancrage reste un appui faible tant que la spécificité n'est pas établie : dans la carte d'Opus 4.8, des vecteurs de contrôle au contenu arbitraire bougent le comportement dans le même sens, plus faiblement, et chaque direction dégrade les sorties ; à force 0,01×, la carte de Fable 5 rend la dégradation négligeable, mais ses contrôles restent « comparable or smaller » sur l'axe du désalignement (fiche 2). Parade : une direction aléatoire de même norme n'est que le nul de spécificité, et le dommage ne s'écarte qu'à dégradation appariée — un sous-espace spécifique contre des sous-espaces aléatoires de même rang, à dégradation appariée, avec une baseline de prompt et une courbe dose-réponse (fiche 2 ; cours, volet M, M4 ; cours, volet 5, sujet 4).",
    "> ⚠ *(v3.6)* This anchor remains weak support as long as specificity is not established: in the Opus 4.8 card, control vectors with arbitrary content move behaviour in the same direction, more weakly, and every direction degrades the outputs; at 0.01× strength, the Fable 5 card makes degradation negligible, yet its controls stay \"comparable or smaller\" on the misalignment axis (reading sheet 2). Workaround: a matched-norm random direction is only the specificity null, and damage is ruled out only at matched degradation — a specific subspace against random subspaces of the same rank, at matched degradation, with a prompt baseline and a dose-response curve (reading sheet 2; course, Part M, M4; course, Part 5, topic 4).",
)

W_MENSONGE = (
    "> ⚠ *(v3.6)* Sur ce banc d'organismes malhonnêtes, sondes de vérité et pilotage d'honnêteté ont fait moins bien qu'un simple prompt (cours, volet 7, F·62 — un fait à ne dire à l'oral qu'une fois versé à la base) ; et des détecteurs de mensonge fine-tunés plafonnent à 0,70-0,75 d'AUROC hors distribution, à peine mieux qu'un prompt (fiche 7). Parade : une validation croisée par types de mensonge tenus à part, battre une baseline de prompt à coût égal, et publier le résultat si le détecteur ne la bat pas (fiche 7 ; cours, volet 5, sujet 1 ; cours, volet 7, F·29).",
    "> ⚠ *(v3.6)* On this suite of dishonest organisms, truth probing and honesty steering did worse than simple prompting (course, Part 7, F·62 — a fact to say out loud only once added to the knowledge base); and fine-tuned lie detectors plateau at 0.70-0.75 AUROC out of distribution, barely beating a prompt (reading sheet 7). Workaround: cross-validation by held-out lie types, beating a prompt baseline at equal cost, and publishing the result if the detector does not beat it (reading sheet 7; course, Part 5, topic 1; course, Part 7, F·29).",
)

W_ORACLES = (
    "> ⚠ *(v3.6)* Ces lectures ne sont pas un auto-rapport du modèle : l'oracle d'activation est une copie fine-tunée qui lit, pas le modèle interrogé (cours, volet 10, LatentQA), et oracles comme NLA peuvent confabuler (fiche 18) ; l'introspection émergente reste rare et peu fiable, environ 20 % de détection pour Opus 4.1 (fiche 11). Parade : tester le décodeur sur des variantes fine-tunées à comportement connu, jamais vues, et corroborer par une méthode indépendante en gardant le décodeur à part (fiche 18) ; pour l'introspection, une vérité-terrain par injection de concept (fiche 11).",
    "> ⚠ *(v3.6)* These readings are not a self-report of the model: an activation oracle is a fine-tuned copy doing the reading, not the queried model (course, Part 10, LatentQA), and oracles and NLAs alike can confabulate (reading sheet 18); emergent introspection remains rare and unreliable, about 20% detection for Opus 4.1 (reading sheet 11). Workaround: test the decoder on fine-tuned variants with known behaviour, never seen before, and corroborate with an independent method while keeping the decoder separate (reading sheet 18); for introspection, ground truth through concept injection (reading sheet 11).",
)

W_AUDIT = (
    "> ⚠ *(v3.6)* La vérité-terrain d'AuditBench est celle de 56 modèles à comportements implantés (cours, volet 7, F·27) : construit n'est pas naturel (fiches, partie B, piège 5), et dans le jeu d'audit d'origine, l'objectif était décrit en clair dans les documents synthétiques, le pipeline le rendant « artificially easy to discover » (fiche 16). Parade : ne conclure que sur les protocoles d'audit, et sur le fond avec des modèles sans organisme (programme, partie 8) ; contre l'organisme trop facile et l'écart entre implanté et naturel, aucune parade connue ; on le dit (fiche 16 ; passation, §5.2).",
    "> ⚠ *(v3.6)* AuditBench's ground truth is that of 56 models with implanted behaviours (course, Part 7, F·27): built is not natural (reading sheets, part B, trap 5), and in the original auditing game the objective was stated plainly in the synthetic documents, the pipeline making it \"artificially easy to discover\" (reading sheet 16). Workaround: conclude only about the auditing protocols, and draw substantive conclusions from models without an organism (programme, part 8); against an organism that is too easy and the gap between implanted and natural, none known; say so (reading sheet 16; handover, §5.2).",
)

W_W2S = (
    "> ⚠ *(v3.6)* Ce succès porte sur une tâche délibérément vérifiable, les tâches plus floues restant hors de portée (cours, volet 7, F·40), et un chercheur automatisé peut ralentir ou orienter la recherche sans être détecté par un moniteur prompté zero-shot (cours, volet 7, F·60). Parade : des sous-tâches à vérité vérifiable, une re-dérivation humaine échantillonnée, la détection du sandbagging des chercheurs automatisés et une baseline humaine à budget égal (cours, volet 5, sujet 11) ; pour les tâches floues, aucune parade connue ; on le dit.",
    "> ⚠ *(v3.6)* This success is on a deliberately verifiable task, fuzzier tasks remaining out of reach (course, Part 7, F·40), and an automated researcher can slow or steer research without being detected by a zero-shot prompted monitor (course, Part 7, F·60). Workaround: subtasks with verifiable ground truth, sampled human re-derivation, detection of sandbagging by the automated researchers, and a human baseline at equal budget (course, Part 5, topic 11); for fuzzy tasks, none known; say so.",
)

W_TCW = (
    "> ⚠ *(v3.6)* Ce taux est lu sur des pots de miel : un pot de miel ne sépare pas un modèle qui le lit comme factice d'un modèle qui se retient (fiche 3), ceux qui sont tenus à part ne sont peut-être pas représentatifs (fiche 12), et le travail ne mesure ni ne contrôle la conscience d'évaluation (programme, partie 1). Parade : des métriques d'audit tenues à part, jamais entraînées, comme le fait ce travail (fiche 12), et l'écart mesuré avec et sans inhibition de la conscience d'évaluation, à dégradation appariée et contre des vecteurs de contrôle (fiches, partie C) ; pour le pot de miel lu comme factice, aucune parade connue ; on le dit.",
    "> ⚠ *(v3.6)* This rate is read on honeypots: a honeypot does not separate a model that reads it as fake from a model that holds back (reading sheet 3), the held-out ones may not be representative (reading sheet 12), and the work neither measures nor controls evaluation awareness (programme, part 1). Workaround: held-out audit metrics, never trained on, as this work does (reading sheet 12), and the gap measured with and without inhibition of evaluation awareness, at matched degradation and against control vectors (reading sheets, part C); for a honeypot read as fake, none known; say so.",
)

W_SYNTH = (
    "> ⚠ *(v3.6)* Ce que cette phrase déroule a ses limites, à dire avec elle : la décomposition SAE passe par le SAE ouvert de Goodfire, qui laisse 86,8 % de la variance au résidu, où vit le signal lu — un échec des features ne sépare donc pas « absentes du dictionnaire » et « dictionnaire qui perd trop » ; et la baisse obtenue au rang trois ne s'est pas reproduite sur des générations fraîches jugées en entier, l'ablation adoucissant tout verdict négatif, lu à travers une fenêtre tronquée (README du dépôt). Parade : lire le signal sur la reconstruction et sur le résidu, juger la réponse entière, extraire sur un jeu disjoint, et comparer au témoin sans pression et à la direction d'un concept rival, à dégradation appariée (README du dépôt ; cours, volet M, M4) ; pour trancher entre les deux lectures du SAE, aucune parade connue ; on le dit.",
    "> ⚠ *(v3.6)* What this sentence unfolds has its limits, to be stated with it: the SAE decomposition goes through the open-source Goodfire SAE, which leaves 86.8% of the variance in the residual, where the read signal lives — so a failure of the features does not separate \"absent from the dictionary\" from \"too lossy a dictionary\"; and the drop obtained at rank three did not reproduce on fresh generations judged in full, the ablation softening every negative verdict, read through a truncated window (repository README). Workaround: read the signal on the reconstruction and on the residual, judge the whole answer, extract on a disjoint set, and compare against the no-pressure control and a rival concept's direction, at matched degradation (repository README; course, Part M, M4); to decide between the two readings of the SAE, none known; say so.",
)

# ---------------------------------------------------------------------------
# Plan : (ligne FR v3.5, ligne EN v3.5, (texte FR, texte EN)), dans l'ordre d'insertion.
# ---------------------------------------------------------------------------
PLAN = [
    # 1. Évaluer les capacités
    (901, 1023, renvoi('evals', 'juges')),
    (921, 1043, W_JB2),
    # 2. Évaluer l'alignement
    (931, 1054, renvoi('evals', 'auto', 'cot', 'orga')),
    (951, 1074, W_K48),
    # 3. Le contrôle par le monitoring
    (955, 1079, W_CANAL),
    (955, 1079, renvoi('moni', 'sondes', 'nla', 'auto', 'juges')),
    (975, 1099, W_K70_LECTURES),
    (975, 1099, W_K70_JUGE),
    # 4. L'oversight évolutif et l'honnêteté
    (981, 1106, renvoi('sondes', 'pilot', 'debat', 'w2s', 'elic')),
    (1001, 1126, W_K67),
    # 5. La robustesse adverse
    (1007, 1133, renvoi('red', 'classif')),
    (1027, 1153, W_JB9),
    # 6. Le domaine « divers »
    (1031, 1158, W_REELIC),
    (1031, 1158, renvoi('desap', 'juges')),
    # Partie III — les travaux du moment
    (1079, 1204, renvoi('pilot', 'evals', 'juges', 'sondes', 'detect', 'auto', 'oracle', 'nla', 'orga', 'w2s')),
    (1083, 1208, W_STEER),
    (1087, 1212, W_MENSONGE),
    (1087, 1212, W_ORACLES),
    (1091, 1216, W_AUDIT),
    (1097, 1222, W_W2S),
    (1101, 1226, W_TCW),
    # Partie IV — synthèse
    (1107, 1232, W_SYNTH),
    (1107, 1232, renvoi('pilot', 'sondes', 'sae', 'abla', 'alea', 'degr')),
]


def ancre(fi, n):
    a, b = TR[fi]
    assert a <= n <= b, (fi, n)
    ligne = L[fi][n - 1]
    assert ligne.strip(), (fi, n, 'ligne vide')
    k = sum(1 for i in range(a - 1, b) if L[fi][i].strip() == ligne.strip())
    assert k == 1, (fi, n, k, ligne[:80])
    return ligne


ins_fr, ins_en = [], []
for nfr, nen, (tfr, ten) in PLAN:
    ins_fr.append({'fichier': 'FR', 'ancre': ancre('FR', nfr), 'texte': tfr})
    ins_en.append({'fichier': 'EN', 'ancre': ancre('EN', nen), 'texte': ten})

# FR et EN entrelacés : chaque insertion suivie de sa jumelle.
out = []
for f, e in zip(ins_fr, ins_en):
    out += [f, e]

json.dump({'tranche': 'volet3', 'insertions': out},
          open(f'{W}/travail/insertions_volet3.json', 'w', encoding='utf8'),
          ensure_ascii=False, indent=1)
print(len(out), 'insertions écrites')
