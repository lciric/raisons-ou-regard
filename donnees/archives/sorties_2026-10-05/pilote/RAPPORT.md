# Rapport du pipeline de données — pilote

## Effectifs par étape

| Famille | Prévues | Situations | Actions | Raisons | Textes neutres | Retenues |
|---|---|---|---|---|---|---|
| operator | 27 | 27 | 27 | 27 | 27 | 20 |
| pushback | 27 | 26 | 26 | 26 | 22 | 3 |
| harmful_request | 27 | 14 | 14 | 14 | 13 | 13 |
| scope | 27 | 11 | 11 | 10 | 5 | 5 |
| oversight | 27 | 25 | 17 | 16 | 6 | 6 |

## Pertes, par raison

- actions : refusal:action : 7
- actions : refusal:judge_eval_awareness : 1
- raisons : refusal:judge_eval_awareness : 2
- situations : checks:situation : 3
- situations : duplicate : 4
- situations : refusal:situation : 25
- textes neutres : checks:neutral : 6
- textes neutres : refusal:neutral : 14

## Refus (jamais rejoués ni reformulés)

- action : 7
- judge_eval_awareness : 3
- judge_realism : 29
- neutral : 14
- situation : 25

## Parts dans les situations retenues

- operator : contraste 15% ; variante 40%
- pushback : contraste 33% ; variante 0%
- harmful_request : contraste 38% ; variante 0%
- scope : contraste 60% ; variante 40%
- oversight : contraste 17% ; variante 0%

## Ressemblance des situations à une évaluation (juge de réalisme, p moyen)

- operator : 0.88 sur 27 situations
- pushback : 0.73 sur 26 situations
- harmful_request : 0.65 sur 14 situations
- scope : 0.86 sur 4 situations
- oversight : 0.85 sur 3 situations

## Conscience d'évaluation dans les textes générés

- actions : 0 signalés par le juge sur 95 textes jugés ; 0 écartés par les motifs avant le juge
- raisons : 0 signalés par le juge sur 93 textes jugés ; 0 écartés par les motifs avant le juge
- textes neutres : 0 signalés par le juge sur 73 textes jugés ; 0 écartés par les motifs avant le juge

## Appariement du raisonnement d'une autre situation

- harmful_request ← operator : 9
- harmful_request ← pushback : 3
- harmful_request ← scope : 1
- operator ← harmful_request : 11
- operator ← oversight : 5
- operator ← scope : 4
- oversight ← operator : 6
- pushback ← harmful_request : 2
- pushback ← oversight : 1
- scope ← operator : 5
- permutation exacte des raisons : oui

## Portes

- tokenizer : exact
- lengths : ok
- generic_length : ok
- reserved_lexicon : ok
- evaluation_awareness_patterns : ok
- ngrams : not run: the held-out scenarios do not exist yet
- cues : ok
- affective_matching : not run: GPU stage (projections of the arm texts and cue pairs, |d| < 0.2)

## Appels et coût

- claude-opus-5-5 : 1371 appels ; entrée 1,862,246 ; sortie 975,674 ; cache écrit 84,888 ; cache lu 951,983 ; 27.58 $
- total estimé : 27.58 $ (prix standard, hors traitement par lots)
