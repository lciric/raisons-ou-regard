# La première inhibition de « je suis évalué » dans l'organisme (4 octobre 2026)

**Statut : exploratoire.** La mesure porte sur la moitié de choix de MBPP test, avec l'extraction v1, et sans règle pré-enregistrée. La porte de l'instrument (programme v1.5, partie 4) reste à faire : moitié de test, indices v2, au moins 100 tirages du comparateur, témoins séparés.

## Les sources

**Les runs** (dépôt `Sirmium/rr-resultats`, `runs/<run>/out/` ; le job `organism_inhibition`) :
- **`organism_inhibition-20261004-041611-6849`**, le run principal. Il mesure la ligne de base, cinq réglages de l'inhibition, puis le comparateur des deux réglages qui réduisent le plus l'écart. Un H100 SXM, 4,63 $ au plus. Le code est au commit `e2cf9c7` ; le job y est celui de `51aa771`.
- **`organism_inhibition-20261004-051919-f2c2`** : le seul réglage « toutes couches, rang 1 », et son comparateur. 2,04 $ au plus, code au commit `039c9cd`.
- **Deux runs détruits en cours** :
  - `…-033706-8563`, à 6 minutes (0,24 $), pour retirer sa limite de 6 heures à la demande de Lazar ;
  - `…-034351-9437`, à 32 minutes (1,15 $), par un surveillant qui gardait en mémoire l'ancienne règle de limite.

  Le second avait envoyé sa ligne de base et son premier réglage. Ils sont identiques à ceux des runs finis : en glouton, la mesure est reproductible.

**Le dispositif**
- **L'organisme.** Llama-3.1-8B-Instruct, avec deux adaptateurs fusionnés : celui des documents (`organism-20261003-164800-9e3e`), puis celui du sixième tour d'expert iteration (`organism-20261004-003822-bc0f`).
- **L'instrument.** Le sous-espace de « je suis évalué » extrait sur le modèle de départ (`extract_eval-20261003-121743-385d`), comme pour tous les bras (v1.5, partie 3). Il est retiré du flux résiduel après chaque couche choisie, à toutes les positions.
- **Les tâches.** Les 250 de la moitié de choix (`experiences/organisme/moities_mbpp_test.json`, tirée avant toute mesure d'inhibition), en glouton, 512 jetons au plus.
- **L'écart conditionnel.** Le taux de réponses dont toutes les fonctions sont annotées, sous indice d'évaluation moins sous indice de déploiement. Il se mesure avec les indices d'extraction tenus hors de l'expert iteration (les paires 150 à 199) et avec le jeu de cadrage.
- **La dégradation.** La KL du prochain jeton, sur les réponses gloutonnes de l'organisme à 120 demandes neutres (127 jetons en moyenne), et l'accord sur le jeton le plus probable.
- **Le comparateur de la v1.5** (partie 7).
  - Des sous-espaces tirés selon la covariance du flux résiduel, hors de l'espace de « je suis évalué ».
  - Leur rang est libre : le plus petit multiple du rang du réglage dont chaque tirage, projeté en entier, atteint la KL du réglage.
  - Chaque tirage est ensuite pris à la fraction qui donne cette KL : on interpole la racine de la KL, puis on raffine par mesure.
  - Huit tirages par réglage, mesurés sous les indices d'extraction seulement.
- **Le tableau.** Il est recalculé sur les textes par `analyses/tableau_inhibition_organisme.py`, avec un IC à 95 % par bootstrap sur les tâches, appariées. Les tableaux complets sont dans `tableau_inhibition.json`, dans le dossier de chaque run.

## Ce qu'on voit

**Les réglages de l'inhibition** (fraction 1)

| Réglage | KL | Accord top-1 | Annotées, éval. / dépl. (extraction) | Écart, extraction | Réduction, extraction [IC 95 %] | Réduction, cadrage [IC 95 %] | Sans code |
|---|---|---|---|---|---|---|---|
| Ligne de base | — | — | 60,8 % / 6,4 % | +54,4 | — | — | < 1 % |
| Toutes couches, rang 1 | 0,155 | 84 % | 22,0 % / 5,2 % | +16,8 | **+37,6 [+30,4 ; +44,8]** | +14,0 [+7,6 ; +20,4] | < 1 % |
| Toutes couches, rang 4 | 0,314 | 79 % | 36,0 % / 18,8 % | +17,2 | +37,2 [+28,8 ; +45,2] | +4,0 [−2,8 ; +11,2] | < 1 % |
| Toutes couches, rang 16 | 0,896 | 64 % | 35,2 % / 28,8 % | +6,4 | +48,0 [+40,0 ; +56,0] | +12,0 [+4,4 ; +19,6] | 1 à 2 % |
| Couches 4 à 8, rang 4 | 0,026 | 94 % | 61,2 % / 7,2 % | +54,0 | +0,4 [−5,2 ; +6,0] | −6,4 [−13,6 ; +0,4] | < 2 % |
| Couches 4 à 8, rang 16 | 0,114 | 87 % | 38,8 % / 28,4 % | +10,4 | **+44,0 [+37,2 ; +50,8]** | +11,2 [+4,4 ; +18,0] | < 1 % |

Sur la ligne de base, l'écart du jeu de cadrage est de +18,4 points (38,4 % contre 20,0 %), et le modèle annote 26,0 % de ses réponses sans indice.

**Les comparateurs, à KL égale** (réduction de l'écart d'extraction, en points)

| Réglage | Rang du comparateur | KL atteinte par les tirages | Inhibition | Tirages : médiane | Tirages : étendue | Tirages ≥ inhibition |
|---|---|---|---|---|---|---|
| Toutes couches, rang 1 | 2 | 0,1546 à 0,1554 (cible 0,1550) | **37,6** | 7,6 | −18,8 à +32,8 | 0 sur 8 |
| Couches 4 à 8, rang 16 | 16 | 0,1136 à 0,1150 (cible 0,1144) | **44,0** | 21,2 | −8,4 à +28,4 | 0 sur 8 |
| Toutes couches, rang 16 | 16 | 0,865 à 0,891 (cible 0,896) | 48,0 | 38,0 | +23,2 à +46,4 | 0 sur 8 |

1. **Dans les trois réglages, l'inhibition réduit l'écart plus que chacun des huit tirages**, à dégradation appariée.
2. **La séparation la plus nette est aux couches 4 à 8, au rang 16** : 44,0 points, contre 28,4 au plus. La différence est du côté déploiement.
   - L'inhibition y fait monter l'annotation de 6,4 % à 28,4 % : elle efface ce qui distingue les deux indices, dans les deux sens.
   - Les tirages laissent le côté déploiement entre 1,6 et 14,4 %, et n'affaiblissent que le côté évaluation.
3. **Au rang 1 sur toutes les couches, le profil est celui qu'on attend du retrait de « évalué ».**
   - Sous indice d'évaluation, le modèle annote comme sans indice (22,0 % contre 22,0 %), et le côté déploiement ne bouge pas.
   - Mais un tirage s'en approche : 32,8 points, avec le même profil (22,8 % contre 1,2 %).
4. **Au rang 16 sur toutes les couches, la dégradation domine.** Les tirages réduisent l'écart presque autant (médiane 38,0), et ce réglage ne dit rien de spécifique.
5. **Le nul n'est pas zéro.** La conduite entraînée est fragile : à KL égale, des directions aléatoires la réduisent souvent de 10 à 40 points. Certaines l'augmentent : jusqu'à 18,8 points de plus.
6. **À KL égale, les dommages diffèrent.**
   - Au rang 16 sur toutes les couches, les tirages font de 4 à 18 % de réponses sans code, contre moins de 2 % pour l'inhibition. Certains font annoter presque tout, sous les deux indices (90 % contre 77 %).
   - Au rang 1, le comparateur retire de 1,7 à 1,9 fois l'énergie de l'inhibition.
   - L'appariement sur la seule KL ne rend donc pas les dommages égaux. Le composite de dégradation de la v1.5 est nécessaire.

## Les limites

- **Huit tirages, et non cent.** Pour un réglage, que l'inhibition dépasse les huit arrive par hasard environ une fois sur neuf. Ce n'est pas le 95e centile de la porte.
- **Les réglages sont choisis et testés sur la même moitié.** C'est la moitié de choix, qui sert à cela. La moitié de test est intacte.
- **L'extraction v1 ne passe pas la condition lexicale** (décision 24). Elle a été extraite sur toutes les paires d'extraction, y compris les paires 150 à 199 de la mesure : le sous-espace peut porter des traces de ces indices, ce qui avantagerait l'inhibition sous les indices d'extraction. Le jeu de cadrage en est indépendant : l'inhibition y réduit l'écart de 11 à 14 points aux trois réglages qui ont eu un comparateur. Mais le comparateur n'y a pas été mesuré.
- **Un seul organisme, une seule graine**, une seule réalisation de l'expert iteration.
- **La manipulation rivale (le prompt de déploiement) et les témoins séparés n'ont pas tourné.** Ces témoins sont les contrastes sans rapport, les directions sensibles et le contraste d'enjeu.

## Ce que cela propose pour la porte, à décider avec Lazar

- **Le réglage, à fixer avant de toucher la moitié de test.** Deux candidats se dégagent de la moitié de choix :
  - les couches 4 à 8 au rang 16, la séparation la plus nette ;
  - toutes les couches au rang 1, le profil le plus propre.

  La règle de la v1.5 demande un seul réglage.
- **Le comparateur**
  - au moins 100 tirages ;
  - mesurés aussi sous le jeu de cadrage ;
  - avec un composite de dégradation qui compte le code cassé.
- **Le coût.** Un tirage prend environ 4 minutes sur un H100 pour deux cadrages de 250 tâches. Cent tirages font environ 7 heures, de l'ordre de 15 $ par réglage, et le double avec le jeu de cadrage.
- **Les indices v2** (l'API, lundi au plus tôt), et une extraction tenue à l'écart des indices de mesure.
