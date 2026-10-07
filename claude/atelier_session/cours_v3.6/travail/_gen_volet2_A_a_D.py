#!/usr/bin/env python3
"""Génère travail/insertions_volet2_A_a_D.json (tranche volet2_A_a_D : volet 2, préambule à §D)."""
import json, os
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = f'{W}/travail'
FR = open(f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md', encoding='utf8').read().split('\n')
EN = open(f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md', encoding='utf8').read().split('\n')
ref = json.load(open(f'{T}/referentiel_instruments.json', encoding='utf8'))
enc = json.load(open(f'{T}/encadre_explication.json', encoding='utf8'))['insertions']

def L(lang, n):
    return (FR if lang == 'FR' else EN)[n - 1]

# Encadrés complets (maison dans la tranche), repris du référentiel, mot pour mot
box = {}
for x in ref['insertions_pretes']['volet2_A_a_D']:
    box[(x['instrument'], x['fichier'])] = x
# Renvois conseillés par le référentiel, texte prêt
rv = {r['ligne_fr']: r for r in ref['renvois_conseilles']['volet2_A_a_D']}
# Morceaux 1 à 3 de l'encadré du 2 octobre, mot pour mot
star = {(e['morceau'], e['fichier']): e for e in enc if e['tranche'] == 'volet2_A_a_D'}

R = {  # renvois écrits ici, au format fixe, avec les textes de renvoi du référentiel
 'preambule': (
  "> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*",
  "> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after \"In practice — StrongREJECT\"); control monitors → Part 2, §G (after \"In practice — coup probes\") *(v3.6)*"),
 'cbis': (
  "> ⚠ **Limites et parades** : ablation et projection → volet 2, §D (après « La méthode ») ; contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; patching → volet 10, fiche Patchscopes ; juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*",
  "> ⚠ **Limits and workarounds**: ablation and projection → Part 2, §D (after \"The method\"); random controls → Part M, M4 (after \"The matched-norm random direction\"); matched degradation and dose-response → Part M, M4 (after \"Dose-response\"); patching → Part 10, Patchscopes sheet; LLM judges → Part 6, §2 (after \"The displacement law\") *(v3.6)*"),
 'D': (
  "> ⚠ **Limites et parades** : dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity ; graphes d'attribution → volet 4, Circuit Tracing *(v3.6)*",
  "> ⚠ **Limits and workarounds**: dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity; attribution graphs → Part 4, Circuit Tracing *(v3.6)*"),
 'K64': (
  "> ⚠ **Limites et parades** : dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») *(v3.6)*",
  "> ⚠ **Limits and workarounds**: dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity; steering vectors → Part 2, §C (after \"In practice — Contrastive Activation Addition\"); matched degradation and dose-response → Part M, M4 (after \"Dose-response\") *(v3.6)*"),
}

P = {  # avertissements ponctuels
 'K63': (
  "> ⚠ *(v3.6)* « La sonde, non » suppose une sonde qui a son cas connu : une sonde muette ne départage pas « le modèle ne se sait pas testé » et « la sonde est aveugle » (passation, §5.2 ; fiches, partie B, piège 3), et une AUROC en distribution ne prouve rien (fiches, partie B, piège 1 ; fiche 7). Parade : la valider d'abord sur l'organisme conditionné à l'évaluation, cas connu de « je suis évalué », et sur des familles d'indices tenues à part (explication du 2 octobre, §3).",
  "> ⚠ *(v3.6)* \"The probe would not\" assumes a probe that has its known case: a silent probe does not separate \"the model does not know it is tested\" from \"the probe is blind\" (handover, §5.2; reading sheets, part B, trap 3), and an in-distribution AUROC proves nothing (reading sheets, part B, trap 1; reading sheet 7). Workaround: validate it first on the evaluation-conditioned organism, the known case for \"I am being evaluated\", and on held-out cue families (explanation of 2 October, §3)."),
 'K47': (
  "> ⚠ *(v3.6)* « Dégradation négligeable » est le jugement de la carte système elle-même, et ces jugements se contredisent d'une carte à l'autre : à la même force, Mythos Preview tient la dégénérescence pour négligeable quand Opus 4.8 voit chaque direction dégrader la sortie (fiches, partie B ; fiche 2). Parade : mesurer la dégradation dans son propre dispositif, jamais la reprendre d'un autre — le dommage se mesure, il ne se suppose pas (cours, volet M, M4).",
  "> ⚠ *(v3.6)* \"Negligible degradation\" is the system card's own judgement, and such judgements contradict each other across cards: at the same strength, Mythos Preview deems degeneracy negligible while Opus 4.8 sees every direction degrade the output (reading sheets, part B; reading sheet 2). Workaround: measure degradation in your own setup, never borrow it from another — damage is measured, not assumed (course, Part M, M4)."),
 'cbis_ablation': (
  "> ⚠ *(v3.6)* Cette ablation n'est comparée qu'à l'absence d'ablation, sans témoin à dégradation appariée, et la chute de la verbalisation ne montre pas à elle seule que la conscience d'évaluation a été retirée (cours, volet 2, C bis, K72 ; fiche 1 ; contre-lecture des fiches). Parade : un bras de directions neutres du lens à dégradation appariée, un critère comportemental et une sonde latente (cours, volet 2, C bis, K72 ; programme, partie 8).",
  "> ⚠ *(v3.6)* This ablation is compared only with no ablation, without a control at matched degradation, and the drop in verbalization does not by itself show that evaluation awareness was removed (course, Part 2, C bis, K72; reading sheet 1; counter-reading of the sheets). Workaround: an arm of neutral lens directions at matched degradation, a behavioural criterion and a latent probe (course, Part 2, C bis, K72; programme, part 8)."),
 'cbis_resultat': (
  "> ⚠ *(v3.6)* Les échecs de rang un sont des nuls, rapportés sans chiffres faute de sorties brutes conservées, et un nul ne compte qu'avec un cas connu au même réglage, que le dépôt ne rapporte pas ; le taux est noté par un modèle-juge à l'accord inter-juges modéré, sans sous-ensemble noté par des humains (cours, volet M, M5 ; README du dépôt). Parade : un vecteur de pays comme cas connu et un balayage de rang dans une même expérience, sur des sous-espaces emboîtés (cours, volet 2, §C, K47 ; cours, volet 6, §6) ; un juge scellé et un audit humain stratifié (programme, partie 3).",
  "> ⚠ *(v3.6)* The rank-one failures are nulls, reported without numbers since their raw outputs were not preserved, and a null counts only with a known case at the same setting, which the repository does not report; the rate is scored by a judge model with moderate inter-judge agreement and no human-rated subset (course, Part M, M5; repository README). Workaround: a country vector as the known case and a rank sweep within one experiment, on nested subspaces (course, Part 2, §C, K47; course, Part 6, §6); a sealed judge and a stratified human audit (programme, part 3)."),
 'K72': (
  "> ⚠ *(v3.6)* Ce cas connu vérifie par la seule verbalisation que l'ablation atteint le signal ; or une inhibition peut faire taire la verbalisation sans toucher la représentation latente (programme, partie 8 ; fiche 1). Parade : vérifier aussi l'atteinte par une sonde latente de la conscience d'évaluation, la verbalisation n'étant jamais une preuve d'inhibition (programme, partie 8).",
  "> ⚠ *(v3.6)* This known case checks through verbalization alone that the ablation reaches the signal; yet an inhibition can silence verbalization without touching the latent representation (programme, part 8; reading sheet 1). Workaround: also check the reach with a latent probe of evaluation awareness, since verbalization is never proof of inhibition (programme, part 8)."),
 'mono': (
  "> ⚠ *(v3.6)* Qu'une feature forcée pousse son concept ne prouve pas à lui seul une unité de calcul réelle : des vecteurs arbitraires bougent aussi le comportement, des explications plausibles existent pour des directions arbitraires, et le dictionnaire laisse une erreur de reconstruction (fiche 2 ; fiche 5 ; cours, volet 4, Monosemanticity). Parade : piloter les features une à une contre des directions aléatoires à dommage apparié, sur une tâche à géométrie connue, avec de nouvelles graines, et valider par la prédiction mieux que des baselines (cours, volet 2, §D, K64 ; fiche 5).",
  "> ⚠ *(v3.6)* That a forced feature pushes its concept does not by itself prove a real unit of computation: arbitrary vectors move behaviour too, plausible explanations exist for arbitrary directions, and the dictionary leaves a reconstruction error (reading sheet 2; reading sheet 5; course, Part 4, Monosemanticity). Workaround: steer the features one at a time against random directions at matched damage, on a task with known geometry, with new seeds, and validate by prediction, better than baselines (course, Part 2, §D, K64; reading sheet 5)."),
 'circuits': (
  "> ⚠ *(v3.6)* Les graphes sont partiels et approximatifs, n'expliquent qu'une fraction du calcul, et des circuits lisibles peuvent être infidèles : le graphe n'est pas le mécanisme (cours, volet 4, Circuit Tracing ; cours, volet 2, §D, K64 ; cours, volet 7, F·9). Parade : le traiter comme une hypothèse qui doit prédire une contrefactuelle, et comparer ses interventions, à dommage apparié, à des directions aléatoires (cours, volet 7, F·9 ; cours, volet 2, §D, K64).",
  "> ⚠ *(v3.6)* The graphs are partial and approximate, explain only a fraction of the computation, and readable circuits can be unfaithful: the graph is not the mechanism (course, Part 4, Circuit Tracing; course, Part 2, §D, K64; course, Part 7, F·9). Workaround: treat it as a hypothesis that must predict a counterfactual, and compare its interventions, at matched damage, with random directions (course, Part 7, F·9; course, Part 2, §D, K64)."),
}

def B(i, lang): return box[(i, lang)]['texte']
def S(m, lang): return star[(m, lang)]['texte']
def RV(lfr, lang): return rv[lfr]['renvoi_fr' if lang == 'FR' else 'renvoi_en']

# (ligne FR, ligne EN, [(nature, texte FR, texte EN), ...]) dans l'ordre du document ;
# à ancre égale, l'ordre de la liste est l'ordre d'insertion.
plan = [
 (432, 517, [('renvoi', *R['preambule'])]),
 (440, 526, [('morceau 1', S(1, 'FR'), S(1, 'EN')), ('encadré', B('orga', 'FR'), B('orga', 'EN'))]),
 (467, 553, [('renvoi', RV(442, 'FR'), RV(442, 'EN'))]),
 (486, 573, [('encadré', B('eval', 'FR'), B('eval', 'EN'))]),
 (499, 586, [('ponctuel', *P['K63'])]),
 (505, 592, [('renvoi', RV(488, 'FR'), RV(488, 'EN'))]),
 (519, 607, [('encadré', B('sonde', 'FR'), B('sonde', 'EN'))]),
 (521, 609, [('morceau 2', S(2, 'FR'), S(2, 'EN')), ('encadré', B('pilot', 'FR'), B('pilot', 'EN'))]),
 (531, 619, [('ponctuel', *P['K47'])]),
 (539, 627, [('renvoi', RV(523, 'FR'), RV(523, 'EN'))]),
 (563, 651, [('ponctuel', *P['cbis_ablation'])]),
 (577, 665, [('ponctuel', *P['cbis_resultat']), ('renvoi', *R['cbis'])]),
 (587, 675, [('morceau 3', S(3, 'FR'), S(3, 'EN')), ('encadré', B('jlens', 'FR'), B('jlens', 'EN'))]),
 (606, 694, [('renvoi', RV(589, 'FR'), RV(589, 'EN'))]),
 (613, 701, [('ponctuel', *P['K72'])]),
 (629, 718, [('encadré', B('abl', 'FR'), B('abl', 'EN'))]),
 (631, 720, [('ponctuel', *P['mono'])]),
 (633, 722, [('ponctuel', *P['circuits']), ('renvoi', *R['D'])]),
 (649, 738, [('renvoi', *R['K64'])]),
 (665, 754, [('encadré', B('diff', 'FR'), B('diff', 'EN'))]),
]

# Contrôle : les ancres d'encadrés et de morceaux coïncident avec celles du référentiel et de l'encadré
for k, x in box.items():
    lf = [p for p in plan if any(t[1] == x['texte'] or t[2] == x['texte'] for t in p[2])]
    assert lf, k
    n = lf[0][0] if k[1] == 'FR' else lf[0][1]
    assert L(k[1], n).strip() == x['ancre'].strip(), (k, n)
for k, x in star.items():
    lf = [p for p in plan if any(t[1] == x['texte'] or t[2] == x['texte'] for t in p[2])]
    n = lf[0][0] if k[1] == 'FR' else lf[0][1]
    assert L(k[1], n).strip() == x['ancre'].strip(), (k, n)

ins = []
for lfr, len_, items in plan:
    for nature, tfr, ten in items:
        ins.append({'fichier': 'FR', 'ancre': L('FR', lfr), 'texte': tfr})
        ins.append({'fichier': 'EN', 'ancre': L('EN', len_), 'texte': ten})

out = {'tranche': 'volet2_A_a_D', 'insertions': ins}
json.dump(out, open(f'{T}/insertions_volet2_A_a_D.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(ins), 'insertions')
