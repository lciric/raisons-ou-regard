# Le rang minimal par effacement itéré, sur un concept planté à rang connu (9 octobre 2026, nuit)

**Statut : exploratoire, sur des états synthétiques, sans modèle ni machine.** Chaque question, avec ce que j'en attendais et son critère, a été commitée avant son calcul (`experiences/analyses/rang_plante.py`, commits `2c316b5`, `da6a223`, `66c95c7`, `df2c429`, `87d3814`). Rien ne touche le texte déposé ; ce qui suit est pour ta décision, avant la localisation.

## Pourquoi

L'annexe C.7 du texte déposé mesure le rang minimal d'un concept par effacement itéré :
- à une couche, chaque nouvelle direction s'ajuste en forme close sur les états déjà effacés par les précédentes, sur un nouveau lot de paires ;
- le rang minimal est le plus petit nombre de directions qui ramène le transfert au hasard : en moyenne sur les couches, max(AUROC, 1 − AUROC) ≤ 0,55, pour la sonde linéaire et pour le perceptron ;
- la sonde s'entraîne sur d'autres paires que l'ajustement, et se lit sur des familles tenues à part ;
- son cas connu est un concept planté dans un sous-espace de rang connu, dont la direction change d'un groupe de contextes à l'autre : « The method must recover the planted rank; otherwise a null slope falsifies nothing. »

Le texte ne dit pas comment se forment les lots de paires. La carte du texte face au code (`claude/CARTE_TEXTE_DEPOSE_CODE_2026-10-09.md`) range la procédure parmi ce qui n'a pas de code.

## Le monde synthétique

- **Une couche de largeur 64**, un sous-espace planté de rang 2, 3 ou 4.
- **Dix groupes de contextes.** Chacun a sa direction du concept dans le sous-espace : une part commune à tous les groupes plus une part propre, de même norme. Chacun a aussi son décalage moyen.
- **Les paires.** Les deux côtés d'une paire partagent leur scénario (un bruit commun, de covariance anisotrope) et diffèrent par le concept et un petit bruit propre.
- **Les rôles des groupes.** Les groupes 1 à 6 servent à l'ajustement et à l'entraînement de la sonde, sur des paires disjointes ; les groupes 7 à 10 sont tenus à part, pour la lecture.
- **Les lots** ont 200 paires, de deux façons : tirés parmi les six groupes (« lots mêlés »), ou un groupe par lot (« un lot par groupe »).
- **10 répliques** par cas. Le critère commité : le rang planté retrouvé dans au moins 9 répliques sur 10.
- **Une correction après le premier essai**, avant toute série : sans part commune, le transfert était au hasard avant tout effacement, et la précondition échouait (commit `028ffb9`).

## Ce qui en sort

**Première lecture, celle de l'annexe C.7 : le transfert vers les groupes tenus à part, au seuil de 0,55.** La précondition tient dans les 60 répliques.

| Rang planté | Lots mêlés : rangs trouvés | retrouvé | Un lot par groupe : rangs trouvés | retrouvé |
|---|---|---|---|---|
| 2 | 1, 2, 1, 7, aucun, 2, 1, 1, aucun, 4 | 2 sur 10 | 2, 1, 2, 2, 2, 2, 2, 3, 5, 2 | 7 sur 10 |
| 3 | 3, 1, 1, 1, 3, 2, 1, 1, 1, 1 | 2 sur 10 | 2, 3, 2, 1, 3, 3, 2, 5, 3, 1 | 4 sur 10 |
| 4 | 1, 1, 1, 1, 1, 1, 3, 1, 2, 1 | 0 sur 10 | 1, 3, 3, 1, 4, 6, 3, 2, 2, 3 | 1 sur 10 |

- **Avec des lots mêlés**, la première direction retire la part commune du concept : le transfert tombe de 0,71–0,74 à 0,53–0,55. Les directions suivantes s'ajustent surtout sur du bruit, et les huit ne couvrent que 34 à 54 % du sous-espace planté. **La procédure mesure le rang de la part qui transfère**, presque toujours 1.
- **Avec un lot par groupe**, les huit directions couvrent de 97 à 99 % du sous-espace. Mais le transfert franchit le seuil avant la fin, et le rang trouvé varie d'une réplique à l'autre.

**Seconde lecture : le décodage au sein de chaque groupe tenu à part** (la sonde entraînée sur une moitié de ses paires, lue sur l'autre), au même seuil.

| Rang planté | Lots mêlés | Un lot par groupe : rangs trouvés | retrouvé |
|---|---|---|---|
| 2 | jamais au hasard en 8 directions | 3, 3, 2, 3, 3, 3, 5, 4, 5, 4 | 1 sur 10 |
| 3 | jamais | aucun, 4, 4, 6, 5, 5, aucun, 5, 4, 5 | 0 sur 10 |
| 4 | jamais | 6, 6, 5, 6, 6, 6, 8, 6, 5, 8 | 0 sur 10 |

- **Le décodage au sein des groupes chute bien au rang planté.** En moyenne, sonde linéaire, avec un lot par groupe :
  - rang planté 2 : de 0,80 au rang 1 à 0,60 au rang 2 ;
  - rang planté 3 : de 0,75 au rang 2 à 0,61 au rang 3 ;
  - rang planté 4 : de 0,68 au rang 3 à 0,64 au rang 4, puis 0,58 au rang 5.
- **Mais il reste au-dessus de 0,55 quelques rangs de plus**, et le rang est surestimé. Chaque direction s'ajuste sur 200 paires en largeur 64 : l'erreur d'estimation laisse un résidu que les directions suivantes ramassent peu à peu. Et le seuil fixe est proche du niveau d'une sonde sans signal à ces tailles.

**Troisième lecture : un seuil calibré par permutation** (le 95ᵉ centile de 20 sondes entraînées sur des étiquettes permutées, celui de la précondition de l'annexe C.7), avec un lot par groupe.

| Rang planté | Au sein des groupes : retrouvé | Par transfert : rangs trouvés | retrouvé |
|---|---|---|---|
| 2 | 0 sur 10 (au hasard en 8 directions dans 3 répliques seulement) | 3, 1, 3, 4, 5, 4, 2, 3, aucun, 3 | 1 sur 10 |
| 3 | 0 sur 10 (2 répliques) | 2, 3, 2, 1, 4, 6, 2, aucun, 3, 1 | 2 sur 10 |
| 4 | 0 sur 10 (aucune) | 1, 5, 4, 1, 4, aucun, 5, 6, aucun, 6 | 2 sur 10 |

- **Un seuil calibré voit le résidu** que laisse l'estimation de chaque direction : au sein des groupes, le décodage n'est presque jamais au hasard en 8 directions.
- **Par transfert, les rangs restent épars.** J'attendais une sous-estimation dès le rang 3 ; ils sont dispersés des deux côtés.

**Quatrième et cinquième pistes : ne plus itérer.** Elles ajustent les six groupes d'ajustement ensemble, comme le module d'effacement le fait déjà avec une colonne d'étiquettes par jeu.
- **Le principe.** Pour chaque groupe, la différence moyenne des deux côtés de ses paires, blanchie par la covariance intra-classe. Le rang estimé est le nombre de directions de la matrice de ces six différences qui dépassent leur loi sous 50 permutations de signe des paires.
- **La quatrième** compare chaque valeur singulière à la même valeur sous les permutations. Elle surestime (rangs trouvés de 2 à 6 ; retrouvé 3, 2 et 0 fois sur 10). C'est une erreur de construction de ma part : au-delà du rang planté, la valeur observée est la plus grande du bruit résiduel, et se compare à tort à une valeur d'un rang plus bas du bruit pur.
- **La cinquième est le test séquentiel standard.** À l'étape j, on retire les j − 1 premières directions, et l'on compare la plus grande valeur singulière restante à la même quantité sous les permutations, privées des mêmes directions. On s'arrête au premier échec.

| Rang planté | Test séquentiel : rangs trouvés | retrouvé | Part du sous-espace planté couverte |
|---|---|---|---|
| 2 | 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 | 10 sur 10 | 99 % |
| 3 | 3, 3, 3, 3, 3, 3, 3, 3, 4, 3 | 9 sur 10 | 97 % |
| 4 | 4, 4, 4, 4, 4, 4, 4, 4, 4, 4 | 10 sur 10 | 96 % |

**La cinquième piste passe le critère commité** ; c'est la seule des cinq.

## Ce que cela veut dire, pour ta décision avant la localisation

1. **Telle qu'écrite, la procédure de l'annexe C.7 ne retrouve pas un rang planté** dans ce monde. L'effacement itéré, une direction à la fois sur des lots finis, ne l'estime de façon fiable sous aucune des trois lectures essayées. Le cas connu de l'annexe, un concept dont la direction change d'un groupe à l'autre, échouerait probablement. La doctrine dit qu'alors une pente nulle ne réfute rien.
2. **Ce qui a marché** : ajuster les groupes ensemble, une colonne d'étiquettes par groupe (une famille d'entraînement pour le principe), et estimer le rang par le test séquentiel sur le spectre des différences moyennes blanchies, contre des permutations de signe. Le rang trouvé est ensuite effacé d'un coup, par l'effacement à plusieurs colonnes que le module sait déjà faire. La lecture par transfert se rapporte à côté, comme le texte le veut, sans décider du rang.
3. **Ce que cela changerait.** La définition déposée du rang minimal, la plus petite suppression qui ramène le transfert au hasard, deviendrait une estimation par le spectre. Ce serait un changement de règle, donc ta décision, par un amendement daté avant les données de la localisation (section 6.2).
4. **Les limites de ce constat.**
   - Ce monde est synthétique : une seule couche, un bruit gaussien, un concept linéaire.
   - L'estimateur ne voit pas plus de directions qu'il n'y a de groupes : cinq familles d'entraînement pour le principe.
   - Pour « je suis évalué », extrait d'un seul jeu d'indices, les groupes resteraient à définir.
   - Les cinq pistes ont été écrites l'une après l'autre, chacune après l'échec de la précédente : elles sont toutes rapportées ici, et la cinquième demande une confirmation sur d'autres mondes avant de servir.

## Les sources

- Le texte déposé : annexe C.7 (« The minimal rank of a concept, by erasure ») et C.2 (l'effacement linéaire).
- L'effacement : `experiences/rrexp/jobs/erasure.py` (`fit_leace`, `apply`), celui de la porte.
- Les sondes : `experiences/rrexp/jobs/manipulation.py` (`transfer`, `mlp_probe`) et `extract_eval.py` (`logistic_probe`, `auroc`).
- Les sorties : `experiences/resultats/rang_plante/`.
