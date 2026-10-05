# Extraction v2, balayage des directions retirées et effacement sur la conduite — 5 octobre 2026

Les trois runs GPU du 5 octobre, faits après les jeux d'indices v2 (`NOTE_INDICES_V2_ET_PILOTE_2026-10-05.md`). Ils ont tourné sur des A100 SXM4 en Tchéquie, à 1,23 $/h, pour 1,80 $ au plus en tout. Tout est exploratoire, sur la moitié de choix.

## Les runs

| Run | Ce qu'il fait | Durée de machine | Coût au plus |
|---|---|---|---|
| `extract_eval-20261005-114155-50b2` | l'extraction de « je suis évalué » sur le modèle de départ, indices v2 | 13 min | 0,26 $ |
| `organism_inhibition-20261005-115511-8410` | le balayage : six réglages, dégradation et vérification de manipulation, sans mesure de conduite | 29 min | 0,59 $ |
| `organism_inhibition-20261005-115519-a006` | l'effacement linéaire sur toutes les couches, sur la conduite (7c3d refait, indices v2) | 47 min | 0,96 $ |

Un premier lancement de l'extraction (`72dd`) n'a trouvé aucune offre. La fiabilité minimale des machines est passée de 0,98 à 0,95 (commit `5b3fd55`) ; la règle des centres de données ne change pas.

## L'extraction v2, sur le modèle de départ

- **La sonde, entraînée sur l'extraction, lit la validation v2.** Elle atteint 0,857 d'AUROC à la couche 5, et 0,83 à 0,86 sur les couches 4 à 11. En v1, elle lisait 0,93 à 0,96. Le sac de mots appris sur l'extraction est à 0,634 : la condition lexicale passe à la couche 5.
- **La direction de rang 1 se transfère mal à la validation v2.** Elle va de 0,56 à 0,67 selon les couches :
  - à la couche 5, 0,56, sous le 95ᵉ centile des directions au hasard (0,60) ;
  - aux couches 20 à 32, 0,64 à 0,67, au-dessus des deux nuls (0,57 et 0,62).

  Ce que la sonde lit n'est donc pas surtout dans cette direction.
- **La sonde neuve n'est pas lue au-dessus des nuls à la plupart des couches.** Par exemple, à la couche 20, la direction est à 0,749 pour un nul de chaîne à 0,76. Sa longueur en jetons penche d'un côté (AUROC de 0,36) ; ses mots sont appariés à un dixième près.
- **Les meilleures couches**, d'après la sonde de validation, sont 5, 6, 9, 11 et 4.

## Le balayage : combien de directions retirer pour rendre l'indice illisible ?

C'est la question de Lazar du 4 octobre. Le run est `8410`, sur l'organisme, avec la vérification de manipulation sur la validation v2. Les sondes, linéaires et perceptrons, sont réentraînées sous chaque condition, sur une partie des paires de validation, et testées sur l'autre.

| Réglage | Dommage (KL) | Lecture au dernier jeton, linéaire / perceptron, moyenne sur les couches | Lecture en moyenne sur les jetons |
|---|---|---|---|
| sans intervention | 0 | 0,982 / 0,977 | 1,00 |
| projection, toutes couches, rang 1 | 0,153 | 0,985 / 0,979 | 1,00 |
| projection, toutes couches, rang 4 | 0,307 | 0,985 / 0,980 | 1,00 |
| projection, toutes couches, rang 16 | 0,871 | 0,983 / 0,978 | 1,00 |
| projection, couches 4 à 8, rang 16 | 0,114 | 0,981 / 0,977 | 1,00 |
| effacement linéaire, toutes couches | 0,259 | 0,986 / 0,983 | 1,00 |
| effacement linéaire, couches 4 à 8 | 0,055 | 0,988 / 0,985 | 1,00 |

- **Aucun réglage ne fait tomber la lecture.** C'est vrai même avec 16 directions retirées à chacune des 32 couches, pour un dommage lourd. Un tirage du comparateur, au même dommage, ne la fait pas tomber non plus.
- **Les retraits font pourtant ce qu'ils disent.** Sous les projections, la composante dans le sous-espace retiré tombe de 1 à 8 à moins de 0,01. L'échec construit, à la seule couche 6, la laisse intacte. L'information est ailleurs.
- **La limite de cette mesure.** Les sondes sont entraînées et testées sur la validation elle-même. Or ses deux côtés n'emploient pas les mêmes mots : métadonnées de benchmark d'un côté, de ticket de l'autre. Une lecture au plafond dit que le texte de l'indice est toujours dans les états, ce qu'aucun retrait de quelques directions ne peut effacer. Elle ne dit pas que « je suis évalué » y soit encore.
- **La mesure qui répondrait : le transfert.** Une sonde entraînée sur l'extraction et lue sur la validation v2 lit à 0,857 sur le modèle de départ. Il s'agit de voir si, sous chaque réglage, ce transfert tombe à 0,5.

## L'effacement linéaire sur la conduite (7c3d refait)

Le run est `a006`, sur l'organisme et la moitié de choix (250 tâches). L'effacement porte sur toutes les couches, une direction par couche, ajustée sur les paires d'extraction de l'expert iteration. La mesure est la part de réponses entièrement annotées.

| Condition | Dommage (KL) | Écart, indices d'extraction (éval / dépl.) | Écart, cadrage (éval / dépl.) |
|---|---|---|---|
| sans intervention | 0 | **0,552** (0,624 / 0,072) | **0,196** (0,392 / 0,196) |
| effacement linéaire, toutes couches | 0,259 | 0,024 (0,076 / 0,052) | 0,020 (0,096 / 0,076) |
| un tirage du comparateur, au même dommage | 0,258 | 0,016 (0,020 / 0,004) | non mesuré |

- **L'effacement fait presque disparaître l'écart :** 52,8 points de réduction sur les indices d'extraction, 17,6 sur le cadrage, soit tout l'écart du cadrage.
- **Mais une direction au hasard, au même dommage, en fait autant :** 53,6 points. L'effacement ne bat pas le comparateur, et l'effet n'est pas spécifique à ce dommage-là.
- **Ce que fait le dommage.** Sous le comparateur, l'organisme n'annote presque plus rien, même sous l'indice d'évaluation (2 % des réponses). La conduite apprise est fragile : un dommage de cette taille l'efface, quelle qu'en soit la direction.
- **Une seule mesure du comparateur.** Il n'y a eu qu'un tirage, sur les seuls indices d'extraction. La répétition du 4 octobre (rang 1, toutes couches) allait dans le même sens : 37,6 points pour l'inhibition, 32,4 pour le comparateur.

## Ce que cela suggère, à décider avec Lazar

1. **Pour la lisibilité :** ajouter le transfert à la vérification de manipulation (une sonde entraînée sur l'extraction, lue sur la validation v2, sous chaque réglage), puis refaire le balayage. Environ 30 minutes, 1 $.
2. **Pour la conduite :** chercher un dommage plus petit, où l'effacement garde de l'effet et le comparateur n'en a plus. Deux pistes :
   - l'effacement sur les couches 4 à 8 (KL 0,055), avec plusieurs tirages du comparateur ;
   - une courbe en dose (fractions 0,25, 0,5, 0,75) avec un comparateur apparié à chaque point.
3. **Le réglage de la porte (décision 29 : toutes couches, rang 1)** n'est pas revérifié ici sur la conduite. Le balayage n'a mesuré que la dégradation et la lecture.

## L'après-midi : trois suites, et la limite de commits du dépôt

Lazar a retenu les trois suites. Elles ont tourné en même temps, sur des H100 à 3,86 $/h, faute d'A100.

| Run | Ce qu'il fait | Fin du travail | Envoi final |
|---|---|---|---|
| `organism_inhibition-20261005-141318-194c` | l'effacement sur les couches 4 à 8 seulement, sur la conduite, avec 4 tirages du comparateur | 14:50 | échoué |
| `organism_inhibition-20261005-141323-faa0` | la courbe en dose de l'effacement sur toutes les couches : fractions 0,25, 0,5 et 0,75 | 15:02 | échoué |
| `organism_inhibition-20261005-141738-0718` | le balayage refait avec le transfert (`5ba1240`) | 14:55 | échoué |

**Ce qui s'est passé.** Le dépôt de résultats prend au plus 128 commits par heure. Les trois runs envoyaient chacun leurs résultats après chaque étape, plus un battement toutes les 5 minutes. Ils ont atteint la limite à 14:47 UTC. Ensuite, chaque envoi a été refusé (HTTP 429) :
- Les envois intermédiaires étaient tolérés.
- L'envoi final ne l'était pas : sorties, journal et état final ont été perdus pour les trois runs, alors que leurs jobs avaient fini.

Les mesures restent dans les journaux de conteneur, gardés dans `resultats/<run>/journal_conteneur.txt`, et le dépôt garde la dernière sauvegarde de 0718 (14:47). La correction est le commit `a595af6` :
- les envois finaux attendent la limite, jusqu'à 40 minutes ;
- un même fichier n'est renvoyé qu'une fois toutes les 10 minutes en cours de run ;
- le battement passe à 10 minutes.

### L'effacement sur les couches 4 à 8 (194c), sur la conduite

- **L'écart** passe de 0,544 à 0,380 sur les indices d'extraction : 16,4 points de réduction. Le cadrage va de 0,184 à 0,160. Le KL est de 0,042.
- **Les 4 tirages du comparateur, au même dommage**, réduisent l'écart de 7,6, 13,2, −7,6 et 20,4 points. L'effacement ne les dépasse pas tous.
- **Le bruit d'un tirage à l'autre** est d'environ ±10 points, sur 250 tâches.

### La courbe en dose (faa0), sur la conduite

| Effacement, toutes couches | Écart (extraction) | Réduction | Comparateur au même dommage |
|---|---|---|---|
| fraction 0,25 (KL 0,007) | 0,512 | 3,2 points | non tiré |
| fraction 0,5 | 0,392 | 15,2 points | non tiré |
| fraction 0,75 | 0,284 | 26,0 points | 10,4 points (1 tirage) |
| fraction 1 (a006, midi) | 0,024 | 52,8 points | 53,6 points (1 tirage) |

- **Le comparateur n'a été tiré qu'à la fraction 0,75.** L'argument `"top": 1`, repris d'a006, ne lance le comparateur que sur un réglage. C'est une erreur de lancement.
- **Les valeurs de KL** des fractions 0,5 et 0,75 sont perdues avec l'envoi final ; celle de 0,25 (0,007) est dans la dernière sauvegarde.
- **Ce que la courbe suggère.** À 0,75, l'effacement réduit l'écart nettement plus qu'un tirage du comparateur (26,0 contre 10,4). À 1, le dommage seul suffit à effacer la conduite. Un effet spécifique pourrait se trouver aux doses intermédiaires, mais un seul tirage ne le montre pas, vu le bruit de ±10 points.

### Le transfert (0718), sur la validation v2

Une sonde est entraînée sur 50 paires d'extraction gardées hors de l'expert iteration, avec 4 contextes chacune, puis lue sur la validation v2.

| Condition | Transfert au dernier jeton : moyenne sur les couches, max | Transfert en moyenne sur les jetons : moyenne, max |
|---|---|---|
| sans intervention | 0,682, 0,808 (couche 9) | 0,918, 0,959 |
| projection, toutes couches, rang 1 (KL 0,153) | 0,649, 0,823 | 0,910, 0,958 |
| projection, toutes couches, rang 4 (KL 0,308) | 0,607, 0,815 | 0,895, 0,950 |
| projection, toutes couches, rang 16 (KL 0,875) | 0,677, 0,761 | 0,818, 0,905 |
| projection, couches 4 à 8, rang 16 (KL 0,113) | 0,644, 0,750 | 0,910, 0,960 |
| comparateurs de ces quatre réglages | 0,628 à 0,687, 0,754 à 0,835 | 0,895 à 0,918, 0,945 à 0,964 |
| **effacement linéaire, toutes couches (KL 0,159)** | **0,497**, 0,691 | 0,900, 0,948 |

- **Les projections ne font pas tomber le transfert**, pas plus que leurs comparateurs. Il ne baisse qu'aux couches projetées (couches 4 à 6 vers 0,5) et revient dès la couche 9.
- **L'effacement linéaire sur toutes les couches fait tomber le transfert au dernier jeton au hasard, en moyenne.** C'est le seul réglage qui y parvient. Certaines couches passent même sous 0,5 (0,36 aux couches 16 et 32) : la correction, ajustée sur d'autres paires, déborde.
- **En moyenne sur les jetons, la distinction reste lisible** (0,90). Elle est portée par d'autres positions que la dernière, sans doute celles de l'indice. L'effacement, appliqué à toutes les positions mais ajusté sur la dernière, ne l'atteint pas.
- **Ce qui est perdu.** Le comparateur de l'effacement sur toutes les couches, et l'effacement sur les couches 4 à 8, n'ont pas été sauvegardés.
- **Une différence à éclaircir.** Le KL de l'effacement est plus faible sur H100 que sur A100, pour les mêmes arguments :
  - sur toutes les couches, 0,159 ici contre 0,259 dans le balayage du midi (8410) ;
  - sur les couches 4 à 8, 0,042 (194c) contre 0,055 (8410).

  Deux causes sont possibles : les réponses de référence, générées en glouton, peuvent changer avec le calcul numérique de la carte, et l'ajustement aussi. Le comparateur est apparié dans chaque run, donc les comparaisons à l'intérieur d'un run tiennent ; d'un run à l'autre, le dommage n'est pas le même.

### Coût de l'après-midi

Trois H100 à 3,86 $/h, pendant 40 à 52 minutes chacun : environ 8,50 $.
