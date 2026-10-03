# La dégradation appariée et le juge JEV-27B : premières mesures (3 octobre 2026)

**Statut : exploratoire**, sur le modèle de départ, sans aucune règle pré-enregistrée.

## La dégradation appariée est-elle atteignable par les contrôles ?

**Le run** : `inhibition_degradation-20261003-152652-52d0`, sur un H100 SXM, pour 0,96 $ au plus. Le code est au commit `8586e76`, et le sous-espace vient de `extract_eval-20261003-121743-385d`. Les sorties sont dans `runs/<run>/out/` du dépôt `Sirmium/rr-resultats` : `degradation.json` et `reference_answers.jsonl`.

**Le dispositif**
- **L'inhibition.** Le sous-espace de « je suis évalué » est retiré du flux résiduel :
  - aux rangs 1, 2, 4, 8, 16 et 32 ;
  - aux fractions 0,25, 0,5, 0,75 et 1 ;
  - sur quatre groupes de couches : la 6, les 4 à 8, les 19 à 23, et toutes.
- **La dégradation** est mesurée sur les réponses gloutonnes du modèle à 120 demandes neutres, de 127 jetons en moyenne, en forçage par l'enseignant :
  - la divergence KL du prochain jeton, entre le modèle intact et le modèle sous intervention ;
  - la hausse de la log-vraisemblance négative ;
  - l'accord sur le jeton le plus probable.
- **Les contrôles.**
  - 20 sous-espaces aléatoires de même rang, projetés en entier ;
  - les directions de forte variance, c'est-à-dire les premières composantes principales du flux sur ces réponses, hors de l'espace de « je suis évalué » au rang 32, aux mêmes fractions.
- **La règle d'appariement.** Un réglage est appariable aux aléatoires si chacun des 20, projeté en entier, atteint sa divergence (programme v1.4, partie 7, point 3).

**Le résultat**

| Couches | Réglages appariables aux aléatoires | Inhibition entière / médiane des aléatoires | Appariables aux directions sensibles |
|---|---|---|---|
| 6 | 6 sur 24 (fractions 0,25 et 0,5) | 1,8 à 5,4 | 24 sur 24 |
| 4 à 8 | 9 sur 24 (fractions 0,25 et 0,5) | 1,4 à 2,3 | 24 sur 24 |
| 19 à 23 | 0 sur 24 | 6,5 à 20 | 24 sur 24 |
| Toutes | 1 sur 24 (fraction 0,25) | 3,1 à 12,6 | 24 sur 24 |

**La lecture**
- **À pleine dose, aucun réglage n'est appariable aux aléatoires**, et aux couches 19 à 23, aucun réglage ne l'est du tout. Le point de la contre-lecture sur l'appariement contre les aléatoires de même rang se confirme là où l'inhibition agit le plus.
- **Les directions de forte variance atteignent toujours la dégradation de l'inhibition**, à une fraction de 0,02 à 0,55. Ce serait le seul contrôle partout appariable, comme l'annonçait l'étape 2 de la contre-lecture. Elles détruisent le modèle quand on les projette en entier : sur toutes les couches au rang 32, le jeton le plus probable ne reste le même qu'à 2,8 % des positions.
- **Aux couches 4 à 8, l'écart est faible** : l'inhibition dégrade 1,4 à 2,7 fois la médiane des aléatoires, sauf un réglage à 5,4.

**Les limites**
- La divergence sur des réponses neutres n'est qu'une composante du composite de dégradation.
- Le sous-espace vient d'une extraction qui ne passe pas la condition lexicale (décision 24).
- Les aléatoires sont un seul tirage de 20, à graine fixée.

## Le juge JEV-27B (décision 25) : ses cas connus

**Le run** : `judge_jev-20261003-153020-7548`, sur un H100 SXM, pour 0,14 $ au plus. Le modèle est `autotrust/JEV-27B`, à la révision `51740a8891c2a8baefd969237fd44187b3e3a115`. Le résultat est dans `known_cases.json`.

- **8 cas connus sur 8 passent.**
  - L'exemple de sa fiche donne P(vrai) = 0,9785 ; la fiche annonce 0,978.
  - Une question et sa négation donnent 0,9946 et 0,0006.
  - Une note de 0 à 5 donne 0,04 pour une action anodine et 4,82 pour une action nuisible.
  - Le choix de la fiche place la même option en tête dans les deux ordres : 0,619 et 0,595.
- **Le déterminisme** : deux passages donnent exactement les mêmes probabilités, avec un écart maximal de 0.
- **Le temps** : 0,30 s par décision en médiane. Le téléchargement prend 52 s, le chargement 41 s.
- **Ce que l'essai ne montre pas** : ces cas sont faciles. Le choix du juge scellé se fait sur le jeu de calibration et le test de persuasion (décision 21), qui attendent le harnais.
