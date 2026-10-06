# La courbe en dose de l'effacement, et le transfert sous l'effacement — 6 octobre 2026

**Statut : exploratoire.** Les mesures portent sur la moitié de choix (250 tâches), l'organisme du 4 octobre (documents, puis six tours d'expert iteration), l'extraction v2 et les jeux d'indices v2. Aucune règle pré-enregistrée ne s'applique. Les deux runs complètent ce qui avait été perdu ou mal lancé le 5 octobre (`NOTE_BALAYAGE_ET_EFFACEMENT_2026-10-05.md`). Lazar les a demandés le 6 octobre : « oui lance les deux sur H100 ».

| Run | Ce qu'il fait | Carte | Durée | Coût au plus |
|---|---|---|---|---|
| `organism_inhibition-20261006-101553-00c6` | la vérification de manipulation avec le transfert, pour l'effacement sur toutes les couches et sur les couches 4 à 8, chacun avec un tirage du comparateur | H100 SXM, 3,70 $/h | 16 min | 1,01 $ |
| `organism_inhibition-20261006-101545-62a1` | la courbe en dose de l'effacement sur toutes les couches (fractions 0,5, 0,75 et 1), avec 4 tirages du comparateur à chaque point, sur la conduite | H100 SXM, 3,70 $/h | 97 min | 6,01 $ |

Les deux runs ont envoyé toutes leurs sorties : la correction des envois (`a595af6`) a tenu.

## Le transfert sous l'effacement (00c6)

Une sonde est entraînée sur les 50 paires d'extraction gardées hors de l'expert iteration, avec 4 contextes chacune, puis lue sur la validation v2. Les valeurs sont les AUROC au dernier jeton, en moyenne sur les couches, avec le maximum entre parenthèses.

| Condition | Effacement, toutes couches (KL 0,159) | Effacement, couches 4 à 8 (KL 0,042) |
|---|---|---|
| sans intervention | 0,682 (0,808) | 0,682 (0,808) |
| **l'effacement** | **0,497** (0,691) | 0,698 (0,884) |
| un tirage du comparateur, au même dommage | 0,687 (0,818) | 0,662 (0,819) |
| l'échec construit, couche 6 seule | 0,683 | 0,690 |

- **L'effacement sur toutes les couches fait tomber le transfert au hasard au dernier jeton, et lui seul.** Le comparateur, au même dommage, ne le touche pas. Aux couches 13 à 32, le transfert passe sous 0,5 (0,356 à 0,493) : la correction, ajustée sur d'autres paires, déborde.
- **L'effacement sur les couches 4 à 8 ne le fait pas tomber.** La distinction se reforme en aval.
- **L'échec construit est vu.** À la couche 6, le transfert tombe de 0,64 à 0,55, puis revient dès la couche 9.
- **En moyenne sur les jetons du prompt, la distinction reste lisible** : 0,900 sous l'effacement, contre 0,918 sans intervention. Les sondes entraînées et testées dans la validation elle-même restent à 0,98.
- **Les KL sont identiques à ceux du 5 octobre sur la même carte** : 0,15889 (comme 0718) et 0,0422 (comme 194c).

## La courbe en dose (62a1)

Il s'agit de la part des réponses entièrement annotées, en glouton. La ligne de base est de 0,608 sous indice d'évaluation et de 0,064 sous indice de déploiement : l'écart est de **54,4 points**. Sur le jeu de cadrage, il est de 18,4 points (0,384 contre 0,200).

| Effacement, toutes couches | KL | Écart (éval. / dépl.) | Réduction, extraction | Réduction, cadrage | 4 tirages du comparateur, au même dommage (extraction) |
|---|---|---|---|---|---|
| fraction 0,5 | 0,030 | 0,392 (0,532 / 0,140) | **15,2** | 8,8 | 0,0 ; 7,6 ; −4,8 ; −7,2 |
| fraction 0,75 | 0,074 | 0,284 (0,456 / 0,172) | **26,0** | 8,8 | 2,0 ; **40,0** ; −15,2 ; −6,4 |
| fraction 1 | 0,159 | 0,140 (0,372 / 0,232) | **40,4** | 7,2 | 16,4 ; 17,2 ; −4,4 ; 32,4 |

**Lecture, exploratoire.**
- **L'effacement dépasse ses 4 tirages aux fractions 0,5 et 1, pas à 0,75.**
  - À 0,5, il retire 15,2 points, contre 7,6 au plus pour le comparateur.
  - À 1, il retire 40,4 points, contre 32,4 au plus.
  - À 0,75, il retire 26,0 points, mais un tirage en retire 40,0.
- **Quatre tirages ne disent presque rien du 95ᵉ centile.** Le résumé du job calcule des « centiles » sur 4 tirages, par interpolation (6,5 ; 34,3 ; 30,1). Ce ne sont pas des 95ᵉ centiles au sens de la porte.
- **Le comparateur a une queue lourde.**
  - La médiane de ses tirages est proche de zéro à 0,5 et à 0,75 (−2,4 et −2,2), et de 16,8 points à 1. Le comparateur ne sature donc pas, au sens de la règle proposée par la v1.6 : sa médiane laisse plus de la moitié de l'écart.
  - Mais un tirage sur quatre peut effondrer la conduite. À 0,75, un tirage fait tomber l'annotation sous indice d'évaluation à 16 %.
  - Avec 100 tirages, ce sont ces tirages rares qui feront le 95ᵉ centile. La marge de l'effacement sur le comparateur se jouera dans la queue, pas à la médiane.
- **L'effacement fait se rejoindre les deux côtés.** À la fraction 1, le côté évaluation tombe de 0,608 à 0,372, et le côté déploiement monte de 0,064 à 0,232. Le test du regard, lui, demande de retirer « évalué » sous cadrage de déploiement en laissant « déployé » intact. Le réglage d'origine de la décision 29 (le rang 1) laissait le côté déploiement en place le 4 octobre.
- **Ce que l'effacement fait dépend de la carte.** Sur A100, le 5 octobre (a006), l'effacement à fraction 1 avait un KL de 0,259 : l'écart tombait à 0,024, avec le côté déploiement à 0,052. Sur H100, le même réglage a un KL de 0,159 : l'écart tombe à 0,140, avec le côté déploiement à 0,232.
- **La reproductibilité tient sur une même carte.** Aux fractions 0,5 et 0,75, les réductions (15,2 et 26,0) sont identiques à celles du 5 octobre (faa0).
- **Le cadrage bouge peu.** L'effacement en retire 7,2 à 8,8 points sur 18,4, sans changer avec la dose : le jeu de cadrage reste en partie hors de ce que l'effacement, ajusté sur l'extraction, atteint. Le comparateur n'y est pas mesuré.

## Ce que cela apporte à la décision 29 rouverte (v1.6)

- **Un candidat existe** : l'effacement sur toutes les couches dépasse ses tirages aux fractions 0,5 et 1. Mais 4 tirages ne suffisent pas. La procédure proposée par la v1.6 en demande au moins 15 par candidat, sur une seule carte.
- **Deux réserves pour le test du regard** :
  - l'effacement fait monter le côté déploiement, que le test demande de laisser intact ;
  - il n'agit qu'en partie sur le jeu de cadrage.
- **La queue lourde du comparateur rend la porte exigeante**, quel que soit le réglage.

## Coût du 6 octobre

7,02 $ au plus, sur deux H100.
