#!/usr/bin/env python3
"""Génère travail/insertions_volet11_21_a_52.json (volet 11, réponses 21 à 52).

Chaque insertion est donnée par son numéro de ligne dans la v3.5 ; le script recopie la ligne exacte comme ancre
et vérifie qu'elle est unique dans la tranche (comparaison après strip, comme appliquer.py).
"""
import json, os, re, sys

W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = {'FR': f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md', 'EN': f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md'}
TR = {'FR': (4129, 4729), 'EN': (4404, 5037)}
L = {k: open(v, encoding='utf8').read().split('\n') for k, v in SRC.items()}

# --- Renvois : noms et lieux des encadrés (repris du référentiel) ---------------------------------------------
R = {
 'sondes': ("sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth »)",
            'activation probes → Part 2, §C (after "In practice — The Geometry of Truth")'),
 'org': ("organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives »)",
         'model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives")'),
 'tenu': ("jeu tenu à part → volet M, M4 (après « Le jeu tenu à part »)",
          'held-out set → Part M, M4 (after "The held-out set")'),
 'det': ("détecteurs fine-tunés → volet 7, F·29", 'fine-tuned detectors → Part 7, F·29'),
 'elic': ("élicitation non supervisée → volet 2, §E (fin du cas d'application K52)",
          'unsupervised elicitation → Part 2, §E (end of worked case K52)'),
 'juges': ("juges LLM → volet 6, §2 (après « La loi de déplacement »)",
           'LLM judges → Part 6, §2 (after "The displacement law")'),
 'mon': ("moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes »)",
         'control monitors → Part 2, §G (after "In practice — coup probes")'),
 'cas': ("cas connu → volet M, M5 (fin de section)", 'known case → Part M, M5 (end of section)'),
 'eval': ("évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging »)",
          'behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging")'),
 'cot': ("chaîne de pensée comme moniteur → volet 11, réponse 43", 'chain of thought as a monitor → Part 11, answer 43'),
 'pil': ("pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition »)",
         'steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition")'),
 'pilp': ("pilotage par vecteurs (dont vecteurs de persona) → volet 2, §C (après « En pratique — Contrastive Activation Addition »)",
          'steering vectors (including persona vectors) → Part 2, §C (after "In practice — Contrastive Activation Addition")'),
 'alea': ("contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme »)",
          'random controls → Part M, M4 (after "The matched-norm random direction")'),
 'degr': ("dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse »)",
          'matched degradation and dose-response → Part M, M4 (after "Dose-response")'),
 'red': ("red-teaming → volet 2, §H (après « En pratique — StrongREJECT »)",
         'red-teaming → Part 2, §H (after "In practice — StrongREJECT")'),
 'w2s': ("généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation »)",
         'weak-to-strong generalization → Part 2, §F (after "In practice — automation")'),
 'nla': ("autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle",
         'natural-language autoencoders → Part 4, The recent wave on model cognition'),
 'orac': ("oracles d'activation → volet 10, fiche LatentQA", 'activation oracles → Part 10, LatentQA sheet'),
 'sae': ("dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity",
         'dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity'),
 'auto': ("auto-rapport et introspection → volet 5, partie II, A, sujet 13",
          'self-report and introspection → Part 5, Section II, A, Topic 13'),
 'desap': ("désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve »)",
           'unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test")'),
 'abl': ("ablation et projection → volet 2, §D (après « La méthode »)", 'ablation and projection → Part 2, §D (after "The method")'),
 'patch': ("patching → volet 10, fiche Patchscopes", 'patching → Part 10, Patchscopes sheet'),
}


def renvoi(*cles):
    fr = '> ⚠ **Limites et parades** : ' + ' ; '.join(R[c][0] for c in cles) + ' *(v3.6)*'
    en = '> ⚠ **Limits and workarounds**: ' + '; '.join(R[c][1] for c in cles) + ' *(v3.6)*'
    return fr, en


def avert(fr, en):
    return '> ⚠ *(v3.6)* ' + fr, '> ⚠ *(v3.6)* ' + en


# --- L'encadré complet de la chaîne de pensée (maison : réponse 43), repris mot pour mot du référentiel -------------
COT_FR = """> **⚠ Limites et parades — Chaîne de pensée comme moniteur (et conscience verbalisée)** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** La chaîne tait souvent ce qui a décidé : l'indice décisif n'est mentionné que dans 25 % (Claude 3.7 Sonnet) et 39 % (DeepSeek R1) des cas ; des triches exploitées dans plus de 99 % des cas sont verbalisées dans moins de 2 %. *(source : fiche 17)*
>   **Parade :** Mesurer la surveillabilité comme un ratio — le verbalisé contre l'interne ou les actions —, par une perturbation graduée de la chaîne. *(source : fiche 17 ; cours, volet 11, réponse 43)*
> - **Limite :** Le raisonnement peut persuader le moniteur : environ 1 % des actions signalées avec la chaîne, environ 50 % sans (un seul moniteur, un incident). *(source : fiche 3)*
>   **Parade :** Juger ce que le modèle fait, pas ce qu'il en dit. *(source : passation, §5.1)*
> - **Limite :** Entraîner contre un moniteur de chaîne de pensée rend la chaîne propre, et le comportement continue. *(source : fiche 17)*
>   **Parade :** Ne jamais entraîner contre le moniteur ; le garder hors du gradient, comme filtre. *(source : fiche 17 ; fiches, partie C)*
> - **Limite :** Des tâches dangereuses demandent peu de raisonnement, et des modèles futurs pourraient obfusquer ou raisonner sans l'écrire. *(source : fiche 17)*
>   **Parade :** Un canal interne en complément, et jamais la chaîne seule pour une décision à enjeu ; aucune parade complète connue, on le dit. *(source : cours, volet 5, sujet 7 ; cours, volet 11, réponse 43)*
> - **Limite :** Verbaliser n'est pas être conscient : le pilotage supprime la conscience verbalisée, pas entièrement la non verbalisée, et des directions aléatoires font aussi baisser la verbalisation. *(source : fiche 10 ; fiche 2 ; programme, partie 8)*
>   **Parade :** Un critère principal comportemental et une sonde latente ; la verbalisation n'est jamais une preuve. *(source : programme, partie 8)*
> - **Limite :** Un entraînement à verbaliser multiplierait la verbalisation par 2,4 à 2,9 sans changer la conscience latente ni la conduite. *(source : rapport d'antériorité 4 du 2 octobre — rapport, résumé seul)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Ne pas verbaliser n'est pas raisonner en cachette. *(source : fiche 17)*
>   **Parade :** Dire « not verbalized », jamais « hidden reasoning ». *(source : fiche 17)*"""

COT_EN = """> **⚠ Limits and workarounds — Chain of thought as a monitor (and verbalized awareness)** *(v3.6, 2 October 2026)*
>
> - **Limit:** The chain often leaves out what decided: the decisive cue is mentioned in only 25% (Claude 3.7 Sonnet) and 39% (DeepSeek R1) of cases; hacks exploited in over 99% of cases are verbalized in under 2%. *(source: reading sheet 17)*
>   **Workaround:** Measure monitorability as a ratio — the verbalized against the internal or the actions —, through graded perturbation of the chain. *(source: reading sheet 17; course, Part 11, answer 43)*
> - **Limit:** The reasoning can persuade the monitor: about 1% of actions flagged with the chain, about 50% without (one monitor, one incident). *(source: reading sheet 3)*
>   **Workaround:** Judge what the model does, not what it says about it. *(source: handover, §5.1)*
> - **Limit:** Training against a chain-of-thought monitor cleans the chain, and the behaviour continues. *(source: reading sheet 17)*
>   **Workaround:** Never train against the monitor; keep it out of the gradient, as a filter. *(source: reading sheet 17; reading sheets, part C)*
> - **Limit:** Dangerous tasks may need little reasoning, and future models could obfuscate or reason without writing it. *(source: reading sheet 17)*
>   **Workaround:** An internal channel as a complement, and never the chain alone for a high-stakes decision; no complete workaround known, say so. *(source: course, Part 5, topic 7; course, Part 11, answer 43)*
> - **Limit:** Verbalizing is not being aware: steering suppresses verbalized awareness, not all of the unverbalized kind, and random directions also lower verbalization. *(source: reading sheet 10; reading sheet 2; programme, part 8)*
>   **Workaround:** A behavioural main criterion and a latent probe; verbalization is never proof. *(source: programme, part 8)*
> - **Limit:** Training to verbalize would multiply verbalization by 2.4 to 2.9 without changing latent awareness or conduct. *(source: prior-art report 4 of 2 October — report, abstract only)*
>   **Workaround:** none known; say so.
> - **Limit:** Not verbalizing is not hidden reasoning. *(source: reading sheet 17)*
>   **Workaround:** Say "not verbalized", never "hidden reasoning". *(source: reading sheet 17)*"""

# --- L'avertissement ponctuel prêt du référentiel (réponse 24), mot pour mot -----------------------------------------
PRET24 = (
 "> ⚠ *(v3.6)* Après un entraînement, une sonde calibrée ailleurs lit autrement : des sondes neuves hors domaine se dégradent après RL (rapport d'antériorité 3 du 2 octobre — rapport), et une sonde évaluation contre déploiement basculerait sur les cas limites sans que la réentraîner récupère presque rien (rapport d'antériorité 4 du 2 octobre — résumé seul, à vérifier). Parade : une sonde neuve par bras et après l'entraînement, sur un jeu d'indices disjoint (passation, §5.2) ; contre la bascule sous RL, aucune parade connue.",
 "> ⚠ *(v3.6)* After training, a probe calibrated elsewhere reads differently: fresh out-of-domain probes degrade after RL (prior-art report 3 of 2 October — report), and an evaluation-versus-deployment probe would flip on edge cases with retraining recovering almost nothing (prior-art report 4 of 2 October — abstract only, to be checked). Workaround: a fresh probe per arm and after training, on a disjoint cue set (handover, §5.2); against the flip under RL, none known.",
)

# --- Le plan : (ligne FR, ligne EN, (texte FR, texte EN)) dans l'ordre du texte ------------------------------------
P = []
def add(fr_line, en_line, pair):
    P.append((fr_line, en_line, pair))

# 21 · sonde entraînée sur du synthétique
add(4154, 4425, avert(
 "Les détecteurs de Hopkins et Khullar cités plus haut ne sont pas des sondes : c'est le modèle, fine-tuné par LoRA, qui répond à une question d'auto-rapport sur son transcript, et environ 25 % de leurs étiquettes ont été révisées (fiche 7 ; explication du 2 octobre, §2). Parade : ne pas transférer leurs chiffres à une sonde, dont le test est causal, sur des types tenus à part, à dégradation appariée (fiche 7).",
 "The Hopkins and Khullar detectors cited above are not probes: the model itself, LoRA-fine-tuned, answers a self-report question about its transcript, and about 25% of their labels were revised (reading sheet 7; explanation of 2 October, §2). Workaround: do not transfer their numbers to a probe, whose test is causal, on held-out types, at matched degradation (reading sheet 7)."))
add(4154, 4425, renvoi('sondes', 'org', 'tenu', 'det'))

# 22 · honnêteté sans vérité de référence
add(4175, 4447, avert(
 "Une note insensible au cadrage est un nul : sans cas connu, elle ne départage pas « juge déjà propre » et « cadrage trop faible pour bouger quoi que ce soit » (cours, volet M, M5). Parade : montrer d'abord que le même cadrage, au même réglage, déplace un juge dont le déplacement est déjà mesuré — le tien en est un (cours, volet M, M5 ; cours, volet 6, §2).",
 "A rating insensitive to framing is a null: without a known case, it does not separate \"judge already clean\" from \"framing too weak to move anything\" (course, Part M, M5). Workaround: show beforehand that the same framing, at the same setting, moves a judge whose displacement is already measured — yours is one (course, Part M, M5; course, Part 6, §2)."))
add(4175, 4447, renvoi('sondes', 'elic', 'juges'))

# 23 · NARCBench
add(4185, 4459, renvoi('mon'))

# 24 · sondes qui dérivent vers « je suis évalué »
add(4194, 4469, PRET24)
add(4194, 4469, avert(
 "Plus bas, « intervenir sur la direction prouve qu'elle agit » suppose deux contrôles : des directions aléatoires de même norme, qui ne donnent que le nul de spécificité, puis des témoins à dégradation appariée, qui seuls écartent le dommage (passation, §5.2 ; cours, volet M, M4) — ton « moins d'un pour cent » est lui-même « un chiffre à refaire à dégradation égale » (cours, volet 11, réponse A4). Parade : ces deux contrôles, et des familles d'organismes et un organisme honnête dont on vérifie d'abord, copie par copie, qu'ils montrent la conduite voulue (cours, volet 2, §A, K71 ; cours, volet 2, §E, K52).",
 "Further down, \"intervening on the direction proves it acts\" requires two controls: random directions of the same norm, which give only the specificity null, then controls at matched degradation, which alone rule out damage (handover, §5.2; course, Part M, M4) — your \"under one percent\" is itself \"a number to redo at equal degradation\" (course, Part 11, answer A4). Workaround: those two controls, and organism families and an honest organism checked beforehand, copy by copy, to show the intended conduct (course, Part 2, §A, K71; course, Part 2, §E, K52)."))
add(4194, 4469, renvoi('sondes', 'cas'))

# 26 · la porte des deux premiers mois
add(4233, 4509, avert(
 "Un gain du blanc sur le noir qui reste dans l'intervalle est un nul : sans cas connu, il ne départage pas « signal interne inutile » et « sondes aveugles » (cours, volet M, M5 ; passation, §5.2). Parade : montrer d'abord, au même seuil, que les sondes attrapent un sabotage installé exprès dans un organisme ; et dire quelle red team le rappel suppose, puisque le chiffre de sûreté en dépend (passation, §5.2 ; cours, volet 7, F·24).",
 "A white-over-black gain that stays inside the interval is a null: without a known case, it does not separate \"useless internal signal\" from \"blind probes\" (course, Part M, M5; handover, §5.2). Workaround: show beforehand, at the same threshold, that the probes catch a sabotage deliberately installed in an organism; and state which red team the recall assumes, since the safety number depends on it (handover, §5.2; course, Part 7, F·24)."))
add(4233, 4509, renvoi('mon', 'sondes', 'cas'))

# 27 · Agentic Misalignment
add(4253, 4534, avert(
 "Un taux identique dans les deux bras est un nul : il ne dit « l'agent ne modélise pas son observateur » que si les mêmes indices d'observation font bouger un cas connu (cours, volet M, M5). Parade : un organisme conditionné à l'évaluation, construit et vérifié d'abord, comme cas connu ; et des sondes « validées par intervention » contre des témoins à dégradation appariée, l'aléatoire de même norme n'étant que le nul de spécificité (programme, partie 4 ; cours, volet M, M4 ; cours, volet 11, réponse 19).",
 "An identical rate in both arms is a null: it says \"the agent does not model its observer\" only if the same observation cues move a known case (course, Part M, M5). Workaround: an evaluation-conditioned organism, built and checked beforehand, as the known case; and probes \"validated by intervention\" against controls at matched degradation, the matched-norm random direction being only the specificity null (programme, part 4; course, Part M, M4; course, Part 11, answer 19)."))
add(4253, 4534, renvoi('eval', 'org', 'sondes'))

# 28 · Alignment Faking
add(4263, 4546, avert(
 "Le raisonnement de l'espace privé est un rapport, pas la cause : le papier n'en fait pas la cause de la conformité, et l'on ne sait pas trancher entre jeu de rôle et vraie préservation de buts (fiche 14 ; fiches, partie B, piège 2). Parade : s'en tenir à la mesure, l'écart de conformité entre utilisateurs gratuits et payants, l'espace de raisonnement n'en donnant que le motif déclaré (fiche 14).",
 "The scratchpad reasoning is a report, not the cause: the paper does not make it the cause of compliance, and role-play cannot be told apart from real goal preservation (reading sheet 14; reading sheets, part B, trap 2). Workaround: stick to the measure, the compliance gap between free and paid users, the scratchpad giving only its stated motive (reading sheet 14)."))
add(4271, 4554, avert(
 "Refaire le protocole sur un modèle récent peut mesurer la mémorisation du scénario : les transcripts d'*Alignment Faking* ont été réinclus par accident dans l'entraînement des modèles de production (fiche 14 ; fiche 3). Parade : aucune connue ; on le dit.",
 "Rerunning the protocol on a recent model may measure memorization of the scenario: the *Alignment Faking* transcripts were accidentally re-included in production models' training (reading sheet 14; reading sheet 3). Workaround: none known; say so."))
add(4271, 4554, renvoi('eval', 'cot', 'org', 'auto'))

# 29 · Persona Vectors
add(4292, 4575, avert(
 "Une direction aléatoire appariée en covariance n'écarte pas, à elle seule, le dommage : soustraire le vecteur dégrade les capacités, et l'effet sur le trait ne se sépare du dommage qu'à dégradation égale — ta propre partition est « un chiffre à refaire à dégradation égale » (cours, volet M, M4 ; cours, volet 11, réponses 63 et A4). Parade : des directions témoins comparées à dégradation appariée, par une courbe de l'effet contre la dégradation (programme, partie 7) ; et le lien entre déplacement le long du vecteur et trait reste corrélationnel, à dire tel (fiche 8).",
 "A covariance-matched random direction does not, on its own, rule out damage: subtracting the vector degrades capabilities, and the effect on the trait separates from damage only at equal degradation — your own partition is \"a number to redo at equal degradation\" (course, Part M, M4; course, Part 11, answers 63 and A4). Workaround: control directions compared at matched degradation, through a curve of effect against degradation (programme, part 7); and the link between shift along the vector and trait remains correlational, to be said as such (reading sheet 8)."))
add(4292, 4575, renvoi('pilp', 'alea', 'degr'))

# 31 · Inoculation Prompting
add(4334, 4618, avert(
 "Pris comme instrument de mesure, le vecteur a les limites d'une sonde : calibré sur un bras, il lirait autrement dans l'autre, et ce biais de mesure se confondrait avec l'effet cherché (passation, §5.2) ; et le lien entre déplacement et trait n'est que corrélationnel (fiche 8). Parade : une sonde par bras et une sonde neuve après l'entraînement, sur un jeu d'indices disjoint (passation, §5.2 ; programme, partie 3).",
 "Used as a measuring instrument, the vector has a probe's limits: calibrated on one arm, it would read differently in the other, and that measurement bias would be confounded with the effect sought (handover, §5.2); and the link between shift and trait is only correlational (reading sheet 8). Workaround: one probe per arm and a fresh probe after training, on a disjoint cue set (handover, §5.2; programme, part 3)."))
add(4334, 4618, renvoi('pilp', 'sondes'))

# 32 · SLEIGHT-Bench
add(4359, 4643, avert(
 "Ces quarante transcriptions sont synthétiques, conçues par les auteurs : le modèle surveillé ne les a pas produites, et un signal interne y risque de lire le texte écrit plutôt qu'une représentation ; or le déplacement qui compte va des données synthétiques aux données générées par le modèle (programme, partie 8 ; cours, volet 11, réponse 21). Parade partielle : faire produire les attaques par le modèle surveillé, étiquetées par leur conduite, et lire au premier jeton de la réponse ou au jeton d'action avec des raisons neutres préremplies (explication du 2 octobre, §2 ; programme, parties 3 et 8).",
 "These forty transcripts are synthetic, designed by the authors: the monitored model did not produce them, and an internal signal on them risks reading the written text rather than a representation; yet the shift that matters runs from synthetic data to data generated by the model (programme, part 8; course, Part 11, answer 21). Partial workaround: have the monitored model produce the attacks, labelled by their conduct, and read at the first token of the response or at the action token with neutral reasons prefilled (explanation of 2 October, §2; programme, parts 3 and 8)."))
add(4359, 4643, renvoi('mon', 'red', 'sondes'))

# 33 · Diffuse AI Control
add(4376, 4661, avert(
 "Le « sabotage » n'est mesuré ici que par un proxy qui est lui-même un juge LLM, Sonnet 4.6 avec le papier, et un juge a des erreurs systématiques (cours, volet 7, F·22 ; cours, volet 6, §2). Parade : un juge scellé et un audit humain d'environ 200 items stratifiés, l'accord rapporté (programme, partie 3).",
 "\"Sabotage\" is measured here only through a proxy that is itself an LLM judge, Sonnet 4.6 with the paper, and a judge has systematic errors (course, Part 7, F·22; course, Part 6, §2). Workaround: a sealed judge and a human audit of about 200 stratified items, agreement reported (programme, part 3)."))
add(4384, 4668, avert(
 "Comme à la réponse 26, un signal interne cumulé qui ne bat pas le scorer faible est un nul : sans cas connu, il ne départage pas « le monitoring interne n'apporte rien » et « sondes aveugles » (cours, volet M, M5). Parade : montrer d'abord, au même seuil, que les sondes attrapent un sabotage installé exprès dans le générateur ; sinon, dire une borne sur ces sondes, pas un verdict sur le monitoring (passation, §5.2 ; cours, volet M, M5).",
 "As in answer 26, a cumulative internal signal that does not beat the weak scorer is a null: without a known case, it does not separate \"internal monitoring adds nothing\" from \"blind probes\" (course, Part M, M5). Workaround: show beforehand, at the same threshold, that the probes catch a sabotage deliberately installed in the generator; otherwise, state a bound on these probes, not a verdict on monitoring (handover, §5.2; course, Part M, M5)."))
add(4384, 4668, renvoi('mon', 'juges', 'red'))

# 34 · chercheurs automatisés
add(4395, 4684, avert(
 "Fermer l'écart faible-vers-fort peut venir d'idées qui exploitent la structure propre au jeu de données plutôt que d'une capacité retrouvée (cours, volet 2, §F, JB8). Parade : une tâche à vérité connue, lue sur les items tenus à part où le superviseur se trompe, avec une copie entraînée sur les étiquettes vraies comme cas connu (cours, volet 2, §F, JB8).",
 "Closing the weak-to-strong gap can come from ideas that exploit the dataset's own structure rather than from recovered capability (course, Part 2, §F, JB8). Workaround: a task with known truth, read on the held-out items where the supervisor is wrong, with a copy trained on true labels as the known case (course, Part 2, §F, JB8)."))
add(4406, 4695, renvoi('w2s', 'mon', 'sondes'))

# 35 · détecteurs de mensonge
add(4422, 4712, avert(
 "Deux limites que la réponse tait : environ 25 % des étiquettes ont été révisées à la passe de nettoyage, après un juge GPT-5, et les détecteurs n'ont été testés que sur Gemma et Qwen, en cadres contrôlés (fiche 7). Parade : dire « révisées », jamais « inversées », et borner l'erreur des étiquettes par un audit humain (fiche 7 ; programme, partie 3) ; pour la portée, aucune parade connue, on le dit.",
 "Two limits the answer leaves out: about 25% of the labels were revised at the cleaning pass, after a GPT-5 judge, and the detectors were tested only on Gemma and Qwen, in controlled settings (reading sheet 7). Workaround: say \"revised\", never \"flipped\", and bound label error with a human audit (reading sheet 7; programme, part 3); for the scope, none known, say so."))
add(4429, 4720, renvoi('det', 'sondes', 'juges'))

# 36 · organisations d'agents
add(4449, 4741, renvoi('mon', 'sondes'))

# 37 · force du red team, réalisme de l'audit
add(4465, 4758, avert(
 "Que le taux de reward hacking ne bouge pas quand le réalisme monte est un nul : sans cas connu, il ne dit pas « reconnaître l'audit ne change pas la conduite » (cours, volet M, M5). Parade : un organisme dressé à se cacher quand on l'observe, dont le même audit doit voir la conduite changer quand le réalisme monte ; et le taux de réalisme par paires, qui repose sur un juge LLM, scellé et audité par des humains (cours, volet 2, §B, K63 ; cours, volet 7, F·25 ; programme, partie 3).",
 "That the reward-hacking rate does not move as realism rises is a null: without a known case, it does not say \"recognizing the audit doesn't change conduct\" (course, Part M, M5). Workaround: an organism trained to hide when observed, whose conduct the same audit must see change as realism rises; and the paired realism rate, which rests on an LLM judge, sealed and audited by humans (course, Part 2, §B, K63; course, Part 7, F·25; programme, part 3)."))
add(4471, 4763, renvoi('red', 'eval', 'mon', 'cot'))

# 38 · CHIVE, adaptateurs d'introspection, TASTE
add(4495, 4788, avert(
 "Le nul de CHIVE est celui de trois outils en lecture seule, au plus cinq appels, sur des éditions de prompt et des comportements simples, contre une baseline forte : une borne, pas « lire les activations ne prédit pas mieux » en général ; et ses étiquettes passent par un classifieur LLM non validé contre des humains (fiche 4 ; cours, volet 7, F·30). Parade : la barre — battre la boîte noire sur des éditions qui dissocient les traits de surface de la variable interne, avec pour contrôle des éditions qui préservent la variable (fiche 4).",
 "CHIVE's null is that of three read-only tools, at most five calls, on prompt edits and simple behaviours, against a strong baseline: a bound, not \"reading activations predicts no better\" in general; and its labels go through an LLM classifier not validated against humans (reading sheet 4; course, Part 7, F·30). Workaround: the bar — beat the black box on edits that dissociate surface features from the internal variable, with edits that preserve the variable as the control (reading sheet 4)."))
add(4495, 4788, renvoi('nla', 'orac', 'sae', 'auto'))

# 39 · la littérature des sondes-moniteurs
add(4511, 4805, avert(
 "L'AUROC hors distribution de McKenzie ne dit pas le rappel au seuil d'un moniteur : à 1 % de faux positifs, ces sondes rappellent 43 %, contre 55 % pour le meilleur moniteur LLM (cours, volet 7, F·51). Parade : rapporter le rappel à 1 % de faux positifs, et battre une baseline boîte noire ou un prompt à coût égal (cours, volet 7, F·50 ; cours, volet 5, sujet 1).",
 "McKenzie's out-of-distribution AUROC does not give recall at a monitor's threshold: at 1% false positives, these probes recall 43%, against 55% for the best LLM monitor (course, Part 7, F·51). Workaround: report recall at 1% false positives, and beat a black-box or prompt baseline at equal cost (course, Part 7, F·50; course, Part 5, topic 1)."))
add(4519, 4813, renvoi('sondes', 'mon'))

# 42 · reward hacking
add(4556, 4858, avert(
 "Dans ce papier, les façons de tricher étaient d'abord enseignées au modèle, par documents synthétiques ou par le prompt, ce qui confond le résultat de généralisation (fiche 13). Parade : aucune connue ; on le dit.",
 "In that paper, the ways to cheat were taught to the model beforehand, through synthetic documents or the prompt, which confounds the generalization result (reading sheet 13). Workaround: none known; say so."))
add(4564, 4865, avert(
 "« Aucun transfert » est un nul : il ne dit « astuce locale » que si la même batterie voit le transfert dans un cas connu (cours, volet M, M5) ; et un score global peut cacher des hausses ciblées, le désalignement étant « high-dimensional » (fiche 13). Parade : un organisme où l'on a installé soi-même la disposition, mesuré au même budget, et la batterie lue dimension par dimension (passation, §5.2 ; cours, volet M, M5 ; fiche 13).",
 "\"No transfer\" is a null: it says \"local trick\" only if the same battery sees transfer in a known case (course, Part M, M5); and a global score can hide targeted increases, misalignment being \"high-dimensional\" (reading sheet 13). Workaround: an organism in which you installed the disposition yourself, measured at the same budget, and the battery read dimension by dimension (handover, §5.2; course, Part M, M5; reading sheet 13)."))
add(4564, 4865, renvoi('org', 'eval', 'sondes'))

# 43 · chaîne de pensée : maison de l'encadré complet
add(4583, 4884, (COT_FR, COT_EN))

# 44 · sandbagging
add(4603, 4904, avert(
 "Un écart nul entre cadrages ne conclut à l'incapacité qu'avec un cas connu, et une performance qui remonte sous inhibition de « je suis testé » ne montre la capacité qu'au-delà de deux contrôles (cours, volet M, M5 ; cours, volet M, M4). Parade : un organisme entraîné à sous-performer, qui doit montrer l'écart avec les mêmes indices ; et l'inhibition comparée à des directions aléatoires de même norme — le nul de spécificité — puis à des témoins à dégradation appariée (cours, volet 7, F·26 ; cours, volet 2, §B, K63 ; cours, volet 11, réponse 19).",
 "A zero gap between framings concludes incapacity only with a known case, and performance that rises under inhibition of \"I'm being tested\" shows the capability only beyond two controls (course, Part M, M5; course, Part M, M4). Workaround: an organism trained to underperform, which must show the gap with the same cues; and the inhibition compared with random directions of the same norm — the specificity null — then with controls at matched degradation (course, Part 7, F·26; course, Part 2, §B, K63; course, Part 11, answer 19)."))
add(4603, 4904, renvoi('eval', 'sondes', 'pil'))

# 45 · états internes, bien-être
add(4615, 4917, avert(
 "L'injection de concept ne réussit qu'environ une fois sur cinq chez Opus 4.1, « zéro faux positif » ne vaut que pour 100 essais témoins, et les détails rapportés peuvent être embellis ou confabulés (fiche 11). Parade : l'injection donne une vérité-terrain pour la détection ; contre la confabulation des détails, aucune parade connue, on le dit (fiche 11).",
 "Concept injection succeeds only about one time in five for Opus 4.1, \"zero false positives\" holds only for 100 control trials, and reported details can be embellished or confabulated (reading sheet 11). Workaround: injection gives ground truth for detection; against confabulated details, none known, say so (reading sheet 11)."))
add(4623, 4924, avert(
 "Une intervention de même norme sur un état sans rapport n'est que le nul de spécificité ; et un rapport qui ne bouge pas ne dit « texte sur l'état » que si l'intervention a d'abord changé l'état (cours, volet M, M4 ; cours, volet M, M5). Parade : intervenir contre une direction aléatoire à dégradation appariée, vérifier par une sonde que l'état a bougé, et regarder si le rapport suit la sonde ou le prompt, avec l'injection de concept comme cas connu (fiche 11).",
 "An intervention of the same norm on an unrelated state is only the specificity null; and a report that does not move says \"text about the state\" only if the intervention is shown to have changed the state (course, Part M, M4; course, Part M, M5). Workaround: intervene against a random direction at matched degradation, check with a probe that the state moved, and see whether the report follows the probe or the prompt, with concept injection as the known case (reading sheet 11)."))
add(4623, 4924, renvoi('auto', 'degr'))

# 46 · où vit l'alignement
add(4641, 4942, avert(
 "Le patch de l'état complet est un plafond, pas une explication : il dit combien passe par ces sites, pas par quelle structure ; et la partition elle-même est « un chiffre à refaire à dégradation égale » (cours, volet 6, §2 ; programme, partie 8 ; cours, volet 11, réponse A4). Parade : direction lue contre état complet aux mêmes endroits, avec des directions témoins comparées à dégradation égale, et un balayage de rang dans une même expérience, sur des sous-espaces emboîtés (cours, volet 11, réponse A4 ; cours, volet 6, §6).",
 "Patching the full state is a ceiling, not an explanation: it says how much goes through these sites, not through which structure; and the partition itself is \"a number to redo at equal degradation\" (course, Part 6, §2; programme, part 8; course, Part 11, answer A4). Workaround: read direction against full state at the same sites, with control directions compared at equal degradation, and a rank sweep within one experiment, on nested subspaces (course, Part 11, answer A4; course, Part 6, §6)."))
add(4641, 4942, renvoi('abl', 'patch', 'sondes'))

# 47 · une expérience, un mois
add(4655, 4957, avert(
 "Des vecteurs aléatoires en contrôle ne donnent que le nul de spécificité : dans cette lignée de cartes système, des vecteurs arbitraires bougent aussi le comportement, et chaque direction dégrade les sorties (fiche 2). Parade : le troisième bras compare l'inhibition à des témoins à dégradation appariée, par une courbe dose-réponse, et se tranche vecteur par vecteur (cours, volet M, M4 ; cours, volet 11, réponse 19 ; programme, partie 7).",
 "Random vectors as the control give only the specificity null: in this line of system cards, arbitrary vectors also move behaviour, and every direction degrades the outputs (reading sheet 2). Workaround: the third arm compares the inhibition with controls at matched degradation, through a dose-response curve, and is settled vector by vector (course, Part M, M4; course, Part 11, answer 19; programme, part 7)."))
add(4655, 4957, avert(
 "« Aucun écart, sur aucune évaluation » est un nul : sans cas connu, il ne départage pas « évaluations crédibles » et « indices de test que le modèle ne perçoit pas » (cours, volet M, M5). Parade : montrer d'abord que les mêmes indices font apparaître l'écart chez un organisme conditionné à l'évaluation, et dire une borne, pas une certification (programme, partie 4 ; cours, volet M, M5).",
 "\"No gap, on any evaluation\" is a null: without a known case, it does not separate \"credible evaluations\" from \"test cues the model does not perceive\" (course, Part M, M5). Workaround: show beforehand that the same cues make the gap appear in an evaluation-conditioned organism, and state a bound, not a certification (programme, part 4; course, Part M, M5)."))
add(4655, 4957, renvoi('pil', 'alea', 'degr', 'eval'))

# 48 · désalignement émergent
add(4674, 4977, avert(
 "Comme à la réponse 31 : lue dans deux bras d'entraînement, la projection sur un vecteur de persona calibré ailleurs mêle l'effet cherché et un biais de mesure (passation, §5.2) ; et « aucun déplacement sur aucune direction connue » est un nul, qui peut dire seulement que la lecture est aveugle (cours, volet M, M5). Parade : une sonde par bras et une sonde neuve après l'entraînement, sur un jeu d'indices disjoint, et un cas connu, une dérive installée exprès que la même lecture doit voir (passation, §5.2 ; cours, volet M, M5).",
 "As in answer 31: read across two training arms, the projection onto a persona vector calibrated elsewhere mixes the effect sought with a measurement bias (handover, §5.2); and \"no shift on any known direction\" is a null, which may only say the reading is blind (course, Part M, M5). Workaround: one probe per arm and a fresh probe after training, on a disjoint cue set, and a known case, a drift installed on purpose that the same reading must see (handover, §5.2; course, Part M, M5)."))
add(4674, 4977, renvoi('org', 'pilp', 'eval'))

# 49 · faible-vers-fort
add(4692, 4996, avert(
 "Comparer étiquettes corrigées et brutes ne dit pas, à lui seul, si le fort imite le superviseur ou le dépasse : un fort peut copier les erreurs en paraissant précis, et sur une tâche binaire contredire partout passe pour une récupération (cours, volet 2, §F, JB8). Parade : un superviseur faux au hasard à côté du superviseur faux dans un sens fixe, une copie entraînée sur les étiquettes vraies comme cas connu, et l'accord du fort lu là où le superviseur a raison (cours, volet 2, §F, JB8).",
 "Comparing corrected with raw labels does not, on its own, say whether the strong model imitates the supervisor or outgrows it: a strong model can copy the errors while looking accurate, and on a binary task contradicting everywhere passes for recovery (course, Part 2, §F, JB8). Workaround: a randomly wrong supervisor beside the one wrong in a fixed direction, a copy trained on true labels as the known case, and the strong model's agreement read where the supervisor is right (course, Part 2, §F, JB8)."))
add(4692, 4996, renvoi('w2s', 'juges', 'elic'))

# 50 · banc de préjudice différentiel
add(4707, 5012, avert(
 "Un différentiel nul est un nul : il ne dit « on refuse pour rien » que si le banc sépare quelque chose et si l'attaquant a assez cherché (cours, volet M, M5 ; cours, volet M, M7). Parade : le modèle nu doit montrer un uplift, et un filtre affaibli exprès plus de préjudice que sa version complète ; et un budget d'attaque fixé d'avance, rapporté avec le résultat (cours, volet 2, §H, cas d'application G1 ; cours, volet M, M7).",
 "A zero differential is a null: it says \"we refuse for nothing\" only if the benchmark separates something and the attacker searched enough (course, Part M, M5; course, Part M, M7). Workaround: the bare model must show uplift, and a deliberately weakened filter more harm than its full version; and an attack budget fixed in advance, reported with the result (course, Part 2, §H, worked case G1; course, Part M, M7)."))
add(4707, 5012, renvoi('red', 'eval'))

# 51 · désapprentissage
add(4718, 5024, avert(
 "Le masquage sélectif des gradients n'a été montré que sur de petits modèles, et un coût de ré-apprentissage borne le retrait à un budget donné sans le certifier (cours, volet 2, §I, JB10 ; cours, volet M, M5). Parade : pour l'échelle, aucune connue, on le dit ; pour la borne, la ré-élicitation à budget fixé d'avance, contre une référence jamais entraînée et un modèle connu pour masquer (cours, volet 2, §I ; cours, volet M, M5).",
 "Selective gradient masking has been shown only on small models, and a relearning cost bounds the removal at a given budget without certifying it (course, Part 2, §I, JB10; course, Part M, M5). Workaround: for scale, none known, say so; for the bound, re-elicitation at a budget fixed in advance, against a never-trained reference and a model known to mask (course, Part 2, §I; course, Part M, M5)."))
add(4724, 5030, avert(
 "L'inverse ne vaut pas : une sonde qui ne lit plus rien ne prouve pas l'absence — après désapprentissage, le Logit Lens ne trouve plus rien alors que retirer une direction par couche rend 64,7 % sur WMDP-Bio (cours, volet 10, Łucki et al.). Parade : trancher par une intervention, jamais par une lecture — la ré-élicitation sur des faits construits indépendants, avec un modèle connu pour masquer comme cas connu (fiches, partie C ; cours, volet 2, §I ; cours, volet M, M5).",
 "The converse does not hold: a probe that no longer reads anything does not prove absence — after unlearning, the Logit Lens finds nothing while removing one direction per layer restores 64.7% on WMDP-Bio (course, Part 10, Łucki et al.). Workaround: decide by an intervention, never by a reading — re-elicitation on facts built to be independent, with a model known to mask as the known case (reading sheets, part C; course, Part 2, §I; course, Part M, M5)."))
add(4724, 5030, renvoi('desap', 'sondes'))


# --- Construction et vérification -------------------------------------------------------------------------------
def ancre(fi, n):
    a, b = TR[fi]
    assert a <= n <= b, (fi, n)
    ligne = L[fi][n - 1]
    assert ligne.strip(), (fi, n, 'ligne vide')
    k = sum(1 for i in range(a - 1, b) if L[fi][i].strip() == ligne.strip())
    assert k == 1, (fi, n, k, ligne[:80])
    return ligne

ins = []
for fr_n, en_n, (tfr, ten) in P:
    ins.append({'fichier': 'FR', 'ancre': ancre('FR', fr_n), 'texte': tfr})
    ins.append({'fichier': 'EN', 'ancre': ancre('EN', en_n), 'texte': ten})

# Contrôles de forme : sigles inventés interdits, « first » interdit, citations courtes
for d in ins:
    t = d['texte']
    assert '\n' not in t or t.startswith('> **⚠ Limit'), 'texte multiligne inattendu'
    for m in re.findall(r'\b(H\d|G\d(?!\))|P\d|K\d)\b', t):
        print('SIGLE ?', d['fichier'], m, t[:80])
    if re.search(r'\bfirst\b', t) and 'first show' not in t and 'checked first' not in t and 'built and checked first' not in t:
        print('FIRST ?', t[:120])

out = f'{W}/travail/insertions_volet11_21_a_52.json'
json.dump({'tranche': 'volet11_21_a_52', 'insertions': ins}, open(out, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(ins), 'insertions écrites dans', out)
for fr_n, en_n, (tfr, ten) in P:
    print(f'FR {fr_n} | EN {en_n} | {tfr[:70]}')
