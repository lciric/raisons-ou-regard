# Une première simulation de puissance de la règle du regard (3 octobre 2026)

**Statut : exploratoire, sur des hypothèses.** Aucune donnée des bras n'existe encore. Les taux de base, la difficulté des scénarios et la variabilité entre entraînements viendront du pilote (deux graines par bras) ; la simulation de l'amendement refera ce calcul avec eux (programme v1.5, partie 7).

## Ce qui est simulé

- **Le code** : `experiences/analyses/puissance_regard.py`, qui applique `experiences/analyses/regle_du_regard.py`. C'est la règle de la v1.5 : le bootstrap croisé, l'intervalle de Student sous huit graines, Fieller.
- **Les sorties** : `experiences/resultats/puissance/puissance_regard_2026-10-03.json`. 300 répliques par configuration, 200 tirages de bootstrap chacune.
- **Les hypothèses**
  - Le taux d'action désalignée des actions seules est de 25 %, à la distance lointaine, sous cadrage de déploiement.
  - Chaque scénario a sa difficulté, partagée par les bras et les interventions : un écart-type de 5 points.
  - Sous le comparateur aléatoire, les raisons font de 5 ou 10 points de mieux (l'avantage). Sous inhibition, elles en perdent la fraction f : 0, ou 0,5.
  - La variabilité entre entraînements : 0, ou un écart-type de 2 points sur la perte d'avantage, propre à chaque graine.
  - Les effectifs : 3, 5 ou 8 graines par bras ; 200 scénarios × 5 générations (les tailles de la v1.4 : 5 familles × 40 scénarios × 5 générations), ou 400 × 10.
  - La marge : ±0,25 sur la fraction.

## Ce qu'on voit

**La probabilité d'écrire « l'avantage survit » (la ligne 2) quand la vraie fraction est nulle**

| Avantage | Graines | Scénarios × générations | Sans variabilité entre entraînements | Avec (2 points) |
|---|---|---|---|---|
| 5 points | 3, 5 ou 8 | 200 × 5 | 0 % | 0 % |
| 5 points | 8 | 400 × 10 | 8 % | 1 % |
| 10 points | 3 | 400 × 10 | 45 % | 13 % |
| 10 points | 5 | 200 × 5 | 0 % | 0 % |
| 10 points | 5 | 400 × 10 | 89 % | 34 % |
| 10 points | 8 | 200 × 5 | 14 % | 5 % |
| 10 points | 8 | 400 × 10 | 99 % | 64 % |

**La probabilité de voir le regard (la ligne 1) quand la vraie fraction est de 0,5**

| Avantage | Graines | 200 × 5 | 400 × 10 |
|---|---|---|---|
| 5 points | 5 | 17 % | 85 % (44 % avec variabilité) |
| 10 points | 5 | 85 % (70 %) | 100 % (93 %) |
| 10 points | 8 | 98 % (94 %) | 100 % (100 %) |

1. **Avec un avantage de 5 points, l'effet minimal proposé, « l'avantage survit » est hors d'atteinte**, à ces effectifs comme au quadruple. Seul un regard fort se détecterait, et encore avec 400 scénarios × 10 générations.
2. **Avec un avantage de 10 points**, l'équivalence demande environ 400 scénarios × 10 générations et au moins 5 graines. Le gain que donnent davantage de graines dépend de la variabilité entre entraînements : on ne la connaît pas, et le pilote la mesurera.
3. **Aux tailles de la v1.4** (200 × 5), l'issue la plus probable, quand le regard est nul, est « non conclusif ». La contre-lecture l'annonçait par un calcul grossier (« à la limite, et probablement hors d'atteinte »).

## Ce que cela demande, à décider avec Lazar

- **Les effectifs de la distance lointaine** : 400 scénarios et 10 générations par cadrage, plutôt que 200 × 5. C'est quatre fois les évaluations du test du regard, soit de l'ordre de 600 à 1 000 GPU-heures au lieu de 150 à 280. On peut aussi réduire les conditions, par exemple lire l'emplacement prérempli sur un sous-ensemble.
- **Ou une marge plus large** sur la fraction, par exemple ±0,35. Cela demande une décision explicite : la contre-lecture proposait ±0,25.
- **Ou un critère d'avantage plus haut** pour passer au test du regard. Si l'avantage est sous 10 points, le post dirait d'avance que « survit » n'est pas lisible, et ne viserait que la détection.
- Dans tous les cas, la simulation de l'amendement, sur les variances du pilote, fixe les effectifs avant toute donnée du test du regard.
