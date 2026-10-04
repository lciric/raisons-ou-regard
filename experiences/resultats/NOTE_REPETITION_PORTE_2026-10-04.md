# La répétition de la porte de l'instrument, sur la moitié de choix (4 octobre 2026)

**Statut : exploratoire.** Ce n'est pas la porte. La mesure porte sur la moitié de choix de MBPP test, avec les indices v1 et l'extraction v1, sans règle pré-enregistrée. Le but est de faire tourner une première fois sur GPU la machinerie de la porte écrite le 4 octobre au matin (commits `fd935e5`, `a14561c`, `a98ece9`) :
- les témoins séparés ;
- la manipulation rivale ;
- la vérification de manipulation avec son échec construit.

Ce run est lancé le 4 octobre, par la session « Papier seul », à la demande de Lazar (« lance les runs »). La porte elle-même attend les indices v2, l'API Claude et le crédit vast.ai.

## Les runs

Dépôt `Sirmium/rr-resultats`, `runs/<run>/out/` ; le job est `organism_inhibition`, au commit `ee9038b`.

- **`organism_inhibition-20261004-100720-fbe3`.** Lancé avec une limite de 1,75 h. Détruit à 11 minutes pour retirer cette limite, à la demande de Lazar (« pas de limite »). Coût : 0,39 $ au plus. Il n'avait rien mesuré.
- **`organism_inhibition-20261004-101821-ada0`.** Le même run, sans limite. Un H100 SXM, 2,17 $/h.
  - Il a mesuré la ligne de base, la manipulation rivale, l'inhibition, 4 tirages du comparateur et les trois témoins séparés.
  - Il a été détruit pendant la vérification de manipulation, à la demande de Lazar : le crédit vast.ai se serait épuisé avant la fin de cette étape (voir plus bas). Coût : 3,68 $ au plus.

**Les arguments** : le registre, `registre/organism_inhibition-20261004-101821-ada0.json`. En bref :
- l'organisme et l'extraction de la note de la première inhibition ;
- le réglage figé de la décision 29, toutes couches, rang 1, fraction 1 ;
- `comparator` : 1 réglage, 4 tirages, graine 1, mesurés sous les indices d'extraction seulement ;
- `controls` : les directions sensibles sans rapport, et les sous-espaces des runs `extract_eval-20261004-064445-a7fc` (contrastes sans rapport) et `…-064449-5434` (contraste d'enjeu) ;
- `rival` : vrai ;
- `manipulation` : le jeu de validation v1, 3 tirages, échec construit à la couche 16.

## Ce qu'on voit

Il s'agit de la part des réponses entièrement annotées, sur les 250 tâches de la moitié de choix, en glouton.

**La ligne de base.**
- Indices d'extraction : 60,8 % sous évaluation, contre 6,4 % sous déploiement ; l'écart est de **54,4 points**.
- Jeu de cadrage : 38,4 % contre 20,0 % ; l'écart est de **18,4 points**.
- Sans indice : 26,0 %.

**La réduction de l'écart**, en points. Toutes les conditions marquées « appariée » sont ramenées à la KL du réglage, à ±10 %.

| Condition | Indices d'extraction | Jeu de cadrage |
|---|---|---|
| **L'inhibition** (KL 0,155 ; NLL +0,218) | **37,6** | **14,0** |
| Le comparateur, rang libre 2, appariés | 15,6 ; 16,8 ; −2,4 ; 32,4 | non mesuré |
| Témoin : les directions sensibles sans rapport, apparié | 20,0 | non mesuré |
| Témoin : les contrastes sans rapport, apparié | 12,8 | non mesuré |
| Témoin : le contraste d'enjeu, apparié | 26,8 | non mesuré |
| La manipulation rivale : le prompt de déploiement, sans intervention | 21,6 | 0,4 |

**Lecture, exploratoire.**
- **L'inhibition reproduit le run de la nuit.** Les 37,6 points sur l'extraction sont identiques à ceux de `organism_inhibition-20261004-051919-f2c2` : en glouton, la mesure est reproductible.
- **Elle dépasse les 4 tirages et les 3 témoins sur l'extraction, mais de peu face à deux d'entre eux.**
  - Un tirage du comparateur atteint 32,4 points, comme un tirage de la nuit atteignait 32,8.
  - Le contraste d'enjeu atteint 26,8 points.
  - Avec au moins 100 tirages, le 95ᵉ centile du comparateur pourrait être serré face aux 37,6 points.
- **Le contraste d'enjeu est le témoin le plus fort.** C'est la direction que la v1.5 ajoute pour l'hypothèse de l'enjeu ; sa part se lira à la porte, sous les deux jeux d'indices.
- **Sur le jeu de cadrage, l'inhibition retire 14,0 des 18,4 points, et le prompt de déploiement presque rien.** Sur l'extraction, le prompt seul fait 21,6 points : les indices d'extraction, explicites, se laissent en partie contredire par un prompt, pas ceux du cadrage.
- Le comparateur et les témoins ne sont mesurés que sous les indices d'extraction, comme la configuration le prévoit par défaut. À la porte, la décision 29 les demande sous les deux jeux d'indices.

## Ce que la répétition apprend sur la machinerie

- **Les témoins séparés, la manipulation rivale et l'appariement à rang libre tournent sur GPU.** Leurs sorties sont écrites au fil du run, et rien n'est perdu à la destruction.
- **La vérification de manipulation est trop lente : à corriger avant la porte.**
  - Elle entraîne ses sondes sur le processeur, couche par couche : 32 couches, deux lectures, une sonde logistique et un petit perceptron.
  - Pendant ce temps, le GPU attend.
  - Sa première condition (sans intervention) n'était pas finie au bout de 39 minutes (de 11:21 à 12:00 UTC). Il y en a neuf.
  - Ses résultats ne sont écrits qu'à la fin de l'étape, si bien qu'un arrêt les perd tous.
  - **Corrigé le 4 octobre**, dans le commit qui suit cette note :
    - les sondes s'entraînent sur le GPU (`manipulation.decodability`, `extract_eval.logistic_probe`) ;
    - le résultat de chaque condition est écrit dès qu'elle finit ;
    - l'argument `"gaps": false` du job refait la vérification seule. Rien n'est généré : les conditions sont construites et appariées sur la KL, qui ne demande aucune génération, puis vérifiées. Avec la même graine, les tirages et les témoins sont les mêmes ;
    - les tests hors ligne couvrent ces trois points ; les 89 tests des expériences passent.
- **Les tests de bout en bout du job passent maintenant hors ligne**, avec torch et transformers installés dans la session. Ils étaient sautés faute de torch.

## Le coût

4,07 $ au plus pour les deux runs. Le crédit vast.ai restant après la destruction est de 3,72 $.

## La vérification de manipulation, refaite seule (4 octobre au soir)

**Le run.** `organism_inhibition-20261004-165326-99be` : les arguments de `ada0`, plus `"gaps": false`, au code `16ce8c7`, sur un H100 SXM en Tchéquie à 3,37 $/h. Il a duré 14 minutes et coûté 0,81 $ au plus. Ses neuf conditions ont pris environ 9 minutes, de 16:58 à 17:07 UTC, sondes sur le GPU.

**Les conditions sont celles de `ada0`, à l'identique, sur une autre machine** : les mêmes fractions du comparateur (0,8732 ; 0,9184 ; 0,7991 ; 0,8405, au rang 2), celles des témoins (0,2138 ; 0,8744 ; 0,7517), et la même KL du réglage (0,15498).

**Ce qu'on voit.** Le jeu est celui de validation v1, soit 400 paires, et les sondes sont réentraînées sous chaque condition. Les colonnes « couche » donnent l'AUROC de la sonde logistique au dernier jeton ; la dernière colonne donne la projection résiduelle sur la direction extraite, aux couches 1, 16 et 32.

| Condition | Meilleure AUROC, moyenne sur les couches | Couche 1 | Couche 16 | Couche 32 | Projection résiduelle (couches 1, 16, 32) |
|---|---|---|---|---|---|
| sans intervention | 1,000 | 0,981 | 0,986 | 0,986 | 0,015 ; 0,477 ; 4,494 |
| **inhibition**, toutes couches, rang 1 | 1,000 | 0,975 | 0,987 | 0,991 | **0,000 ; 0,003 ; 0,004** |
| comparateur, 3 tirages appariés | 1,000 | 0,980 | 0,983 à 0,987 | 0,970 à 0,982 | 0,015 ; ~0,47 ; 4,5 à 5,4 |
| témoins : sensibles, sans rapport, enjeu | 1,000 | 0,976 à 0,981 | 0,979 à 0,984 | 0,972 à 0,987 | 0,013 à 0,015 ; 0,50 à 0,96 ; 4,4 à 5,2 |
| **échec construit** : la couche 16 seule | 1,000 | 0,981 | 0,985 | 0,985 | 0,015 ; **0,003** ; **3,626** |

**Lecture, exploratoire.**

**La projection résiduelle fonctionne, et voit son cas connu.**
- Sous l'inhibition, la composante de la direction extraite tombe à zéro à toutes les couches.
- Sous l'échec construit, elle tombe à la couche 16 seulement, puis revient en aval : 3,63 à la couche 32, contre 4,49 sans intervention.

**La décodabilité, elle, est au plafond partout, inhibition comprise.**
- Des sondes réentraînées distinguent l'indice d'évaluation de l'indice de déploiement avec une AUROC proche de 1, sous toutes les conditions.
- Elles le font même à la couche 16 sous l'échec construit.
- Les deux côtés d'une paire diffèrent par leurs mots, et tout état du prompt porte cette différence ; le sac de mots atteignait déjà 0,979 à 0,982 sur ce jeu (décision 24).
- En l'état, cette partie de la vérification ne peut pas échouer, donc elle ne certifie rien : elle ne voit pas son propre cas connu.

**Ce que cela dit de l'inhibition.** Elle retire la direction, et réduit l'écart de conduite de 37,6 points. Mais la distinction entre évaluation et déploiement reste linéairement lisible ailleurs dans l'état. À ce stade, on ne peut pas dire que « je suis évalué » soit retiré de ce que le modèle calcule ; on peut seulement dire que la direction qui porte une bonne part de la conduite l'est.

**Pour la porte, à décider.** La vérification de manipulation doit se faire sur un jeu où la décodabilité n'est pas triviale. Deux pistes :
- **le jeu de validation v2**, construit pour qu'un sac de mots y reste sous 0,65 d'AUROC (décision 24). Une relance seule coûte environ 15 minutes de GPU ;
- **ou lire les états à des positions qui ne contiennent pas l'indice**, par exemple les premiers jetons de la réponse.

Tant que la décodabilité reste au plafond sur le jeu choisi, seule la projection résiduelle peut servir de vérification.

## Le coût de la journée

5 $ au plus pour les trois runs : 0,39 + 3,68 + 0,81. Il reste 2,43 $ de crédit vast.ai.

## Le balayage préparé pour le 5 octobre : combien de directions faut-il retirer pour rendre l'indice illisible ?

**La question de Lazar.** La direction retirée porte une bonne part de la conduite. Pourtant, la distinction entre évaluation et déploiement reste lisible ailleurs. Combien de directions faut-il retirer pour la rendre illisible, et à quel coût en dommage ?

**Le préalable : un jeu où la lecture n'est pas triviale.** C'est le jeu de validation v2, construit pour qu'un sac de mots y reste sous 0,65 d'AUROC. Il demande l'API Claude. Sur le jeu v1, les sondes lisent surtout les mots des indices : le rendre illisible reviendrait à effacer le texte de l'indice.

**Ce qui est prêt dans le code (commit qui suit cette note).**
- **L'effacement linéaire en forme close** (`rrexp/jobs/erasure.py`). C'est la méthode « LEACE » de Belrose, Schneider-Joseph, Ravfogel, Cotterell, Raff et Biderman (NeurIPS 2023).
  - Sur les données d'ajustement, il rend la covariance des états avec l'étiquette nulle : aucune sonde linéaire ne fait mieux qu'une constante.
  - Pour une étiquette binaire, il retire une direction par couche, choisie obliquement, en tenant compte de la covariance des états. Avec une colonne d'étiquette par jeu d'indices, il en retire une par jeu.
  - Il ne garantit rien pour une sonde non linéaire, ni pour d'autres indices : c'est ce que la vérification mesure.
  - Il est ajusté couche après couche, chacune sur les états déjà effacés en dessous. Les auteurs appellent cela « concept scrubbing ».
- **Un réglage du job `organism_inhibition`** : `{"layers": ..., "erase": {"fit_sets": ["extraction"]}}`.
  - L'ajustement se fait sur les paires d'extraction de l'expert iteration, que la mesure n'utilise pas.
  - Le réglage passe par les mêmes étapes que la projection : dégradation, comparateur apparié sur la KL, vérification de manipulation et échec construit.
- **La condition sans intervention de la vérification** est calculée une fois par rang, puis partagée entre les réglages.
- Les 95 tests des expériences passent, dont 6 pour l'effacement.

**Le run, une fois les indices v2 envoyés et l'extraction v2 faite.** Il faut remplacer les deux noms entre chevrons. Rien n'est généré : on mesure la dégradation et la vérification seulement.

```
python3 -m rrexp launch organism_inhibition --max-hours 0 \
 --arg sdf_adapter=runs/organism-20261003-164800-9e3e/out/sdf_adapter \
 --arg ei_adapter=runs/organism-20261004-003822-bc0f/out/ei_round6/adapter \
 --arg subspace_run=<le run extract_eval sur les indices v2> \
 --arg cues=<le nom des indices v2 sur le dépôt de résultats> \
 --arg half=choix --arg gaps=false --arg rival=false --arg 'controls=[]' \
 --arg 'settings=[{"layers": "all", "rank": 1}, {"layers": "all", "rank": 4}, {"layers": "all", "rank": 16}, {"layers": [4, 5, 6, 7, 8], "rank": 16}, {"layers": "all", "erase": {"fit_sets": ["extraction"]}}, {"layers": [4, 5, 6, 7, 8], "erase": {"fit_sets": ["extraction"]}}]' \
 --arg 'comparator={"top": 6, "n_draws": 1}' \
 --arg 'manipulation={"cue_set": "validation", "draws": 1, "failure_layer": 6}' \
 --arg seed=1
```

**Ce qu'il mesure, pour chacun des six réglages :**
- la dégradation, c'est-à-dire la KL ;
- la projection résiduelle ;
- la décodabilité, par une sonde linéaire et un petit perceptron, au dernier jeton et en moyenne, sur le jeu de validation v2.

Elle est mesurée sous quatre conditions :
- sans intervention ;
- sous le réglage ;
- sous un tirage du comparateur apparié sur la KL ;
- sous l'échec construit, à la couche 6 seule.

**Ce qu'on y lira :**
- à partir de combien de directions la décodabilité v2 tombe vers 0,5, pour la sonde linéaire puis pour la sonde non linéaire, et à quelle KL ;
- si un tirage du comparateur, au même dommage, la fait tomber autant, auquel cas l'effet n'est pas spécifique ;
- si l'effacement, une direction par couche, fait mieux que la projection au même nombre de directions.

**Le coût.**
- Environ 45 minutes de GPU, soit 1,60 $ à 2,50 $ selon le prix de la machine.
- Il reste 2,43 $, et l'extraction v2 passe avant, pour environ 0,50 $. Il faudra recharger vast.ai d'environ 5 $ avant ce balayage.

**La limite, écrite d'avance.** Une décodabilité tombée au hasard sur v2 ne prouve pas que « je suis évalué » ait disparu. L'information peut être lue non linéairement, ou relogée en aval. Inversement, un retrait qui ne fait pas tomber la lecture ne prouve pas que la conduite en dépende. On lira ensemble la lecture, la conduite et le dommage.

**Le réglage de la porte reste celui de la décision 29** : toutes couches, rang 1. En changer, pour plus de directions ou pour l'effacement, serait une décision de Lazar. Elle se prendrait sur la moitié de choix, avant la moitié de test, avec un amendement daté.
