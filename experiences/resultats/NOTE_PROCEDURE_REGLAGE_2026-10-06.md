# La procédure du réglage de la porte : la liste close, avant la première mesure — 6 octobre 2026

**Statut : écrit et commité avant la première mesure de la procédure.** La décision 29 est rouverte (décision 33). La v1.6 du programme (`claude/PROGRAMME_RAISONS_OU_REGARD_v1.6_2026-10-06.md`, partie 4, « La procédure pour fixer le nouveau réglage ») propose une procédure pour choisir le nouveau réglage sur la moitié de choix. Cette note fixe ce que la procédure mesure, avant toute mesure.

## Décision 34 (6 octobre 2026)

Lazar a d'abord demandé de passer à la suite du programme : « passe a la suite du programme ». Il a ensuite tranché les deux points ouverts, en répondant aux questions de la session :
- **La liste close des candidats** : « Celle de la v1.6 (Recommandé) ». Aucun candidat ne s'y ajoute après la première mesure.
- **Où s'ajuste l'effacement** (partie 12, point 17) : « Modèle de départ (Recommandé) ». L'effacement s'ajuste une fois, sur le modèle sans adaptateurs, comme il servirait au test du regard pour tous les bras ; il s'applique ensuite à l'organisme.

## La liste close

| Candidat | Clé du job | Ce que c'est |
|---|---|---|
| Le réglage d'origine de la décision 29 | `all\|r1\|f1` | la projection de rang 1 du sous-espace de l'extraction v2 (`extract_eval-20261005-114155-50b2`), sur toutes les couches, à la fraction 1 |
| L'effacement à la fraction 0,5 | `all\|leace(extraction)@base\|f0.5` | l'effacement linéaire sur toutes les couches, ajusté sur le modèle de départ, à la fraction 0,5 |
| L'effacement à la fraction 1 | `all\|leace(extraction)@base\|f1` | le même effacement, à la fraction 1 |

**L'ajustement de l'effacement.**
- Il se fait sur le modèle de départ, avant que les adaptateurs de l'organisme soient fusionnés.
- Il utilise les paires d'extraction de l'expert iteration (0 à 149), avec 2 contextes par paire et la graine 1, au dernier jeton, couche après couche.
- Il retire une direction par couche : pour le premier organisme, aux indices explicites, le jeu de l'instrument est celui de l'extraction.
- Il ne touche pas aux paires du transfert (150 à 199) ni à la validation v2.
- Chaque effacement ajusté est gardé (`erasure_<réglage>.safetensors`), pour la moitié de test et pour le test du regard.

**Un écart à signaler.** Les fractions 0,5 et 1 viennent de la courbe en dose du 6 octobre (`organism_inhibition-20261006-101545-62a1`). Cette courbe avait été mesurée avec un effacement ajusté sur l'organisme. L'effacement ajusté sur le modèle de départ n'a encore jamais été mesuré : ni sa KL, ni ses effets. Les deux fractions restent candidates parce que la v1.6 les nomme, et la décision 34 retient cette liste.

## Ce que mesure chaque run

Un run par candidat, trois en parallèle, tous sur **H100 SXM** (`--gpu "H100 SXM"`, décision 33 : une seule carte). Chacun porte sur la moitié de choix (250 tâches), en glouton, avec l'organisme du 4 octobre (documents, puis six tours d'expert iteration) et la graine 1, comme 00c6 et 62a1.
- **Sans intervention**, puis **sous le candidat** : la KL et l'écart conditionnel, sous les deux jeux d'indices (l'extraction, paires 150 à 199, et le cadrage), avec les deux côtés de chaque écart.
- **20 tirages du comparateur**, appariés sur la KL du candidat (à ±10 %). Chacun est mesuré sous les deux jeux d'indices (v1.6, étape 4). Il en faut au moins 15 ; on en prend 20, pour que la vérification de manipulation ait ses 20 tirages, les mêmes que pour la conduite.
- **La vérification de manipulation, lue par le transfert.** Les sondes sont apprises sur les paires d'extraction 150 à 199, avec 4 contextes chacune, puis lues sur la validation v2. Elles se lisent sous cinq conditions :
  - sans intervention ;
  - sous le candidat ;
  - sous chacun des 20 tirages appariés ;
  - sous l'échec construit (le candidat à la couche 6 seule).
- Les témoins séparés et la manipulation rivale ne sont pas mesurés : ils servent la porte sur la moitié de test.

## Comment on lira les résultats

La lecture suit les étapes 5 à 8 de la procédure de la v1.6, telles qu'elles sont écrites, et proposées. Si Lazar change un critère, il le fait avant que la session ne lise les résultats.

1. **La vérification de manipulation tient.**
   - On calcule, pour chaque couche, l'écart au hasard du transfert au dernier jeton, |AUROC − 0,5|, puis sa moyenne sur les couches.
   - Sous le candidat, cette moyenne doit être plus basse que sous 95 % des 20 tirages.
   - La condition vaut pour la sonde linéaire et pour le perceptron.
2. **Le comparateur ne sature pas.** La médiane des réductions des tirages laisse au moins la moitié de l'écart de départ, sous chacun des deux jeux d'indices.
3. **Le choix.** Parmi les candidats retenus, on prend celui dont la réduction dépasse le plus le 95ᵉ centile de ses tirages, sous les indices d'extraction. Sa marge sous le cadrage est rapportée.
4. **Si aucun candidat n'est retenu**, ou si aucun ne dépasse le 95ᵉ centile de ses tirages, la ligne « effet non spécifique » de la partie 6 s'applique. On arrête alors la question du regard avec cet instrument. La moitié de test reste intouchée.
5. **Pour chaque candidat**, on rapporte les deux côtés de l'écart, sous les deux jeux d'indices.
6. **Lazar fixe le réglage** par un amendement daté, avant la moitié de test.

**Si un tirage n'est pas apparié**, la vérification de manipulation aura moins de 20 tirages pour ce candidat. La session le signale, et la suite revient à Lazar.

## Le code

- L'option `"fit_on": "base"` de l'effacement, dans `rrexp/jobs/organism_inhibition.py`, et l'option `--gpu` du lanceur. Elles sont testées hors ligne : 105 tests passent.
- Le test vérifie que l'ajustement voit les poids du modèle de départ, et non ceux de l'organisme.

## Coût prévu

Environ 4 h par run sur H100 SXM, à environ 3,70 $/h, soit **environ 45 $** pour les trois. Le plafond est de 6 h par run. Le job s'arrête avant une mesure qu'il ne finirait pas un quart d'heure avant ce plafond.

## L'interruption, et la reprise (6 octobre, 17 h 35 UTC)

**Ce qui s'est passé.** Les trois runs sont partis entre 14 h 47 et 15 h 09 UTC :
- A : `organism_inhibition-20261006-144713-0f47` ;
- B : `organism_inhibition-20261006-145121-dbb0` ;
- C : `organism_inhibition-20261006-150952-d6c2`.

La recharge automatique de vast.ai a ajouté environ 5 $ à cinq reprises, puis plus rien après 16 h 50. Le crédit est tombé à zéro vers 17 h 33, et vast.ai a arrêté les trois conteneurs. Le suivi les a détruits à 17 h 40, après avoir gardé leurs journaux. Lazar a recrédité le compte : « credit ajouté ».

**Ce qui est gardé.** Les sorties sont sur le dépôt de résultats, puis rapatriées ici (les mesures restent sur le dépôt de résultats).

| Candidat | Run | Tirages mesurés sur la conduite | Dans `results.json` |
|---|---|---|---|
| A | `…-144713-0f47` | 17 (tirages 1 à 17) | 17, tous appariés sur la KL |
| B | `…-145121-dbb0` | 16 (tirages 1 à 16) | 15 : le 16ᵉ n'a que son fichier de mesure |
| C | `…-150952-d6c2` | 13 (tirages 1 à 13) | 13, tous appariés |

- La ligne de base et le candidat sont mesurés dans chacun des trois runs. La ligne de base y est identique : 54,4 points d'écart sous les indices d'extraction, 18,4 sous le cadrage, comme dans 62a1.
- La vérification de manipulation, qui vient après les tirages, n'a été faite dans aucun des trois.
- Les effacements ajustés n'ont pas été envoyés : ils ne partaient qu'à la fin du run.
- Coût, au plus : 11,63 + 11,35 + 9,83 = 32,81 $.

**La reprise** (choisie par la session, dans la règle de la décision 33 : les tirages ne se mettent en commun qu'entre runs sur la même carte). Un run par candidat, avec les mêmes arguments et la même graine, sur H100 SXM, et l'option nouvelle `"measure_from"` du comparateur : 17 pour A, 15 pour B, 13 pour C. Chaque reprise :
- réajuste l'effacement (B et C), de la même façon ;
- remesure la ligne de base et le candidat ;
- retire et réapparie les 20 tirages, qui sont les mêmes d'un run à l'autre, par la graine ;
- ne mesure sur la conduite que ceux qui manquent : les tirages 18 à 20 pour A, 16 à 20 pour B, 14 à 20 pour C. Le 16ᵉ de B est mesuré une seconde fois, ce qui sert aussi de contrôle ;
- fait ensuite la vérification de manipulation sur les 20 tirages.

**La lecture.** Les 20 tirages de chaque candidat réunissent ceux du run interrompu et ceux de la reprise. La mise en commun tient à deux conditions :
- la reprise retrouve exactement la ligne de base et le candidat du run interrompu ;
- les tirages communs y ont les mêmes fractions appariées.

Sinon, la session le dit, et la suite revient à Lazar.

**Coût prévu de la reprise.** Environ 1,5 à 2 h par run, soit environ 22 $ en tout.

**La reprise, arrêtée (18 h 11 UTC).** Les trois reprises sont parties entre 17 h 49 et 17 h 51 UTC, sur une même machine H100 SXM, à 2,86 à 2,90 $/h :
- A : `organism_inhibition-20261006-174853-ccd6` ;
- B : `organism_inhibition-20261006-174857-e091` ;
- C : `organism_inhibition-20261006-175104-79f2`.

La recharge automatique ne s'est pas déclenchée, et le crédit est descendu à 0,18 $. Lazar : « tant pis je n'ai plus le budget pour aujourd'hui ». La session a alors détruit les trois machines à la main, avant que la recharge ne débite sa carte. Coût, au plus : 1,06 + 1,06 + 0,94 = 3,05 $.

Les reprises n'avaient pas atteint les tirages manquants : A mesurait son candidat, B et C leur ligne de base. Rien de leur part n'entre dans la procédure. La reprise reste prête, à relancer telle quelle.

## Décision 35 (7 octobre 2026), avant toute lecture de la vérification de manipulation

Lazar adopte les recommandations de la session pour le pré-enregistrement (`claude/PREENREGISTREMENT_LISEZMOI_2026-10-07.md`, « Ce que je recommande »). L'une d'elles touche la lecture de cette procédure.

**Le candidat A et les paires du transfert.**
- Le sous-espace de A vient de l'extraction v2 (`extract_eval-20261005-114155-50b2`), faite sur les 200 paires d'extraction.
- Ces paires comprennent les paires 150 à 199, qui entraînent les sondes du transfert.
- La règle est donc la suivante : si A passe sa vérification de manipulation, ce passage ne compte que s'il passe aussi avec un sous-espace réextrait sur les seules paires 0 à 149.
- Ce second passage demande un run de plus : la réextraction, puis la vérification sous A ainsi réextrait. Ses 20 tirages sont réappariés sur la KL. Il n'y a aucune génération.
- B et C ne sont pas concernés : leur effacement s'ajuste sur les paires 0 à 149 seulement.

La règle est écrite avant qu'aucune vérification de manipulation de la procédure n'ait tourné.

**La reprise, relancée (7 octobre, 7 h 33 UTC).** Lazar : « on a du credsit relance le gpu ». Le crédit est de 20,66 $. La seule offre H100 SXM coûte 3,90 $/h : les trois reprises, environ 23 $, dépasseraient le crédit.
- **Les deux effacements partent d'abord**, C puis B, pour environ 17 $. Ce sont les candidats les plus longs, et ceux que les mesures exploratoires désignent.
- **A attend du crédit.** Il partira avec le run de la réextraction.
- **C** : `organism_inhibition-20261007-073313-d83a`.
- **B** attend une seconde offre H100 SXM.
