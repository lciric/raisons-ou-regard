#!/usr/bin/env python3
"""Construit travail/insertions_volet_M.json (tranche volet_M : FR l. 182-411, EN l. 249-496)."""
import json, os, re

W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = {'FR': f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md', 'EN': f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md'}
TR = {'FR': (182, 411), 'EN': (249, 496)}
L = {k: open(v, encoding='utf8').read().split('\n') for k, v in SRC.items()}
REF = open(f'{W}/travail/referentiel_instruments.md', encoding='utf8').read().split('\n')
ENC = open(f'{W}/travail/encadre_explication.md', encoding='utf8').read().split('\n')


def ancre(fi, n):
    s = L[fi][n - 1]
    a, b = TR[fi]
    k = sum(1 for l in L[fi][a - 1:b] if l.strip() == s.strip())
    assert k == 1, (fi, n, k)
    return s


def encadre(titre_section, langue):
    """Le bloc ~~~markdown qui suit « Encadré complet, <langue> : » dans la section titre_section du référentiel."""
    i = next(j for j, l in enumerate(REF) if l.startswith(titre_section))
    marque = '**Encadré complet, français :**' if langue == 'FR' else '**Encadré complet, anglais :**'
    i = next(j for j in range(i, len(REF)) if REF[j] == marque)
    d = next(j for j in range(i, len(REF)) if REF[j].startswith('~~~markdown')) + 1
    f = next(j for j in range(d, len(REF)) if REF[j] == '~~~')
    return '\n'.join(REF[d:f])


def morceau5(langue):
    i = next(j for j, l in enumerate(ENC) if l.startswith('## Morceau 5'))
    t = '### Texte FR' if langue == 'FR' else '### Texte EN'
    d = next(j for j in range(i, len(ENC)) if ENC[j] == t) + 2
    f = next(j for j in range(d, len(ENC)) if ENC[j].strip() in ('---', '### Texte EN'))
    bloc = ENC[d:f]
    while bloc and not bloc[-1].strip():
        bloc.pop()
    return '\n'.join(bloc)


INS = []


def ajoute(fi, n, texte):
    INS.append({'fichier': fi, 'ancre': ancre(fi, n), 'texte': texte})


# ---------- M4 : les trois encadrés de la maison, puis le renvoi de fin de section ----------
ajoute('FR', 267, encadre('## 1. Contrôles aléatoires', 'FR'))
ajoute('EN', 334, encadre('## 1. Contrôles aléatoires', 'EN'))
ajoute('FR', 271, encadre('## 2. Dégradation appariée', 'FR'))
ajoute('EN', 338, encadre('## 2. Dégradation appariée', 'EN'))
ajoute('FR', 293, encadre('## 3. Jeu tenu à part', 'FR'))
ajoute('EN', 360, encadre('## 3. Jeu tenu à part', 'EN'))

ajoute('FR', 296, "> ⚠ **Limites et parades** : sondes d'activation, dont les paires contrastives → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; ablation et projection → volet 2, §D (après « La méthode ») ; classifieurs de sûreté, dont le jumeau propre → volet 2, §H (fin du cas d'application G1) ; désapprentissage et ré-élicitation, dont la référence jamais entraînée → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») ; évaluations comportementales et pots de miel, dont le bras de référence réaliste → volet 2, §B (après « En pratique — le sandbagging ») ; juges LLM, dont la notation à l'aveugle → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*")
ajoute('EN', 363, '> ⚠ **Limits and workarounds**: activation probes, including contrastive pairs → Part 2, §C (after "In practice — The Geometry of Truth"); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); ablation and projection → Part 2, §D (after "The method"); safety classifiers, including the clean twin → Part 2, §H (end of worked case G1); unlearning and re-elicitation, including the never-trained reference → Part 2, §I (after "In practice — unlearning put to the test"); behavioural evaluations and honeypots, including the realistic reference arm → Part 2, §B (after "In practice — sandbagging"); LLM judges, including blind scoring → Part 6, §2 (after "The displacement law") *(v3.6)*')

# ---------- M5 : renvoi après les deux fautes réelles ; avertissement sur le nul gouverné ; encadré du 2 octobre et encadré « Cas connu » ----------
ajoute('FR', 310, "> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; classifieurs de sûreté, dont le jeu canari → volet 2, §H (fin du cas d'application G1) ; désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») *(v3.6)*")
ajoute('EN', 377, '> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); red-teaming → Part 2, §H (after "In practice — StrongREJECT"); safety classifiers, including the canary set → Part 2, §H (end of worked case G1); unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test") *(v3.6)*')

ajoute('FR', 312, "> ⚠ *(v3.6)* Ce nul gouverné est un taux jugé par un modèle-juge, et ton dépôt le dit : l'accord entre juges est modéré, et aucun sous-ensemble noté par des humains ne borne l'erreur du juge *(source : README du dépôt)*. Parade : un juge scellé et un audit humain d'items stratifiés, avec l'accord rapporté, qui borne cette erreur *(source : programme, partie 3)* ; voir l'encadré « Juges LLM », volet 6, §2.")
ajoute('EN', 379, '> ⚠ *(v3.6)* This governed null is a rate judged by a judge model, and your repository says so: agreement between judges is moderate, and no human-rated subset bounds the judge\'s error *(source: repository README)*. Workaround: a sealed judge and a human audit of stratified items, with the agreement reported, which bounds that error *(source: programme, part 3)*; see the box "LLM judges", Part 6, §2.')

ajoute('FR', 314, morceau5('FR'))
ajoute('FR', 314, encadre('## 4. Cas connu', 'FR'))
ajoute('EN', 381, morceau5('EN'))
ajoute('EN', 381, encadre('## 4. Cas connu', 'EN'))

# ---------- M8 : avertissement sur les sondes qui « separate », puis renvoi ----------
ajoute('FR', 363, "> ⚠ *(v3.6)* Que des sondes « separate » les états ne dit pas qu'elles généralisent : une séparation en distribution ne prouve rien, c'est l'écart avec la séparation sur des types tenus à part qui se mesure *(source : fiches, partie B, piège 1 ; fiche 7)*. Parade : tenir à part des familles entières, jamais des paraphrases, et des formats, d'un tour à l'agentique à plusieurs tours ; et, pour intervenir, le test causal — des directions aléatoires de même norme, qui ne sont que le nul de spécificité, puis des témoins à dégradation appariée, seuls à écarter le dommage *(source : explication du 2 octobre, §3 ; programme, partie 3 ; passation, §5.2)*.")
ajoute('FR', 363, "> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; ablation et projection → volet 2, §D (après « La méthode ») ; contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*")
ajoute('EN', 430, '> ⚠ *(v3.6)* That probes "separate" the states does not say they generalize: an in-distribution separation proves nothing; what is measured is the gap with the separation on held-out types *(source: reading sheets, part B, trap 1; reading sheet 7)*. Workaround: hold out whole families, never paraphrases, and formats, from a single turn to multi-turn agentic; and, to intervene, the causal test — random directions of the same norm, which are only the specificity null, then controls at matched degradation, which alone rule out damage *(source: explanation of 2 October, §3; programme, part 3; handover, §5.2)*.')
ajoute('EN', 430, '> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); ablation and projection → Part 2, §D (after "The method"); random controls → Part M, M4 (after "The matched-norm random direction"); LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*')

# ---------- M9 : avertissement sur le nul de la chasse aux contournements ; renvoi de fin de section ----------
ajoute('FR', 371, "> ⚠ *(v3.6)* « Aucun contournement universel dans sa chasse » est le nul d'un red-teaming : une borne à son budget, pas une absence, et une chasse compte des contournements, pas ce que le filtre retire à l'attaquant *(source : cours, volet M, M5 et M7 ; cours, volet 2, §H, G1)*. Parade : le dire avec sa portée, « dans sa chasse », pas plus fort, et juger un filtre aussi par le préjudice différentiel, comme le fait l'expérience de ce cas *(source : cours, volet M, M10, question 12 ; cours, volet 2, §H, G1)*.")
ajoute('EN', 438, '> ⚠ *(v3.6)* "No universal jailbreak in its hunt" is the null of a red-teaming effort: a bound at its budget, not an absence, and a hunt counts jailbreaks, not what the filter withholds from the attacker *(source: course, Part M, M5 and M7; course, Part 2, §H, G1)*. Workaround: say it with its scope, "in its hunt", no stronger, and judge a filter also by differential harm, as this case\'s experiment does *(source: course, Part M, M10, item 12; course, Part 2, §H, G1)*.')

ajoute('FR', 387, "> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; classifieurs de sûreté → volet 2, §H (fin du cas d'application G1) ; désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») *(v3.6)*")
ajoute('EN', 454, '> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT"); safety classifiers → Part 2, §H (end of worked case G1); unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test") *(v3.6)*')

# ---------- M10 : la grille relue avant chaque répétition renvoie aux quatre encadrés du volet ----------
ajoute('FR', 408, "> ⚠ **Limites et parades** : contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; jeu tenu à part → volet M, M4 (après « Le jeu tenu à part ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*")
ajoute('EN', 475, '> ⚠ **Limits and workarounds**: random controls → Part M, M4 (after "The matched-norm random direction"); matched degradation and dose-response → Part M, M4 (after "Dose-response"); held-out set → Part M, M4 (after "The held-out set"); known case → Part M, M5 (end of section) *(v3.6)*')

out = f'{W}/travail/insertions_volet_M.json'
json.dump({'tranche': 'volet_M', 'insertions': INS}, open(out, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(INS), 'insertions ->', out)
