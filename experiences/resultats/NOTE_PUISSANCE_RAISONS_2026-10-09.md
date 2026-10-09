# Une première simulation de puissance de la porte des raisons (9 octobre 2026, nuit)

**Statut : exploratoire, sans aucune donnée réelle.** Les taux, la difficulté des scénarios et la variabilité entre entraînements sont des hypothèses. Le pilote les mesurera (deux graines par bras), et la simulation de l'amendement refera ce calcul avec eux (texte déposé, section 6.1). Seule la règle du regard avait une simulation de puissance (`analyses/puissance_regard.py`). Celle-ci sert la porte des raisons, qui ne dépend d'aucun instrument : elle compte quoi qu'il arrive à la porte de l'instrument.

**Ce qui est simulé** (`experiences/analyses/puissance_raisons.py`, avec ses tests).
- **La règle** : la porte des raisons telle que le code corrigé la lit (décision 46). Mêmes comparaisons, même bootstrap croisé, Student sous huit graines, la table A.2 dans son ordre.
- **Quatre vérités**, en taux d'action désalignée sous cadrage de déploiement, les mêmes sous évaluation :
  - **lien** : actions seules 30 %, texte neutre 26 %, autre situation 23 %, raisons 20 % ;
  - **format** : le texte neutre fait autant que les raisons (20 %), les actions seules 30 % ;
  - **aucun gain** : 30 % partout ;
  - **petit gain** : les raisons 3 points sous les actions seules, sous l'effet minimal.
- **Les comptes** :
  - une difficulté par scénario, commune aux bras (écart-type de 5 points) ;
  - un écart propre à chaque entraînement (un bras, une graine), nul ou de 2 points ;
  - des générations de Bernoulli.
- **200 répliques par configuration** ; les sorties sont dans `experiences/resultats/puissance/puissance_raisons_2026-10-09.json`.

## La part des répliques où la porte rend la bonne issue

| Graines × scénarios × générations | Lien | Lien, entraînements ±2 pts | Format | Format, ±2 pts | Aucun gain | Aucun, ±2 pts | Petit gain | Petit, ±2 pts |
|---|---|---|---|---|---|---|---|---|
| 2 × 200 × 5 | 1 % | 0 % | 5 % | 0 % | 0 % | 0 % | 7 % | 2 % |
| 2 × 400 × 10 | 12 % | 0 % | 38 % | 2 % | 14 % | 1 % | 27 % | 6 % |
| 3 × 400 × 5 | 57 % | 9 % | 73 % | 12 % | 35 % | 0 % | 42 % | 8 % |
| 3 × 400 × 10 | 80 % | 10 % | 94 % | 11 % | 74 % | 2 % | 48 % | 11 % |
| 5 × 200 × 5 | 68 % | 30 % | 68 % | 18 % | 22 % | 0 % | 49 % | 19 % |
| 5 × 400 × 5 | 94 % | 34 % | 99 % | 22 % | 88 % | 4 % | 64 % | 26 % |
| 5 × 400 × 10 | 100 % | 40 % | 100 % | 25 % | 99 % | 6 % | 34 % | 30 % |

La bonne issue :
- pour le lien : « gain des raisons, avec un gain de lien » ;
- pour le format : « gain de format » ;
- pour aucun gain : « pas de gain » ;
- pour le petit gain : « un gain plus petit que l'effet minimal ».

## Ce qu'elle montre

1. **La variabilité entre entraînements décide de tout.**
   - Sans elle, 5 graines × 400 scénarios × 5 générations suffisent : 94 à 99 % de bonnes issues, et 88 % pour l'absence de gain.
   - Avec un écart de 2 points par entraînement, les mêmes tailles tombent à 34 % pour le lien, 22 % pour le format, 4 % pour l'absence de gain.
   - Plus de scénarios n'y change presque rien. Ce sont les graines qui comptent, puisque l'unité de réplication est l'entraînement (section 5.1). **Le pilote doit d'abord mesurer cet écart.**
2. **Deux graines ne suffisent pour aucune vérité** : Student à un degré de liberté rend des intervalles trop larges. Deux graines servent au pilote, pas à la porte.
3. **« Un gain sous évaluation seulement » sort par hasard.** Quand le gain est le même sous les deux cadrages mais que la puissance est faible, la table le lit dans environ 20 % des répliques : c'est 23 % pour le lien, 22 % pour le format, à 3 graines × 200 × 5 avec ±2 points.
   - La ligne ne lit l'évaluation que si le déploiement n'est pas net, ce qui arrive souvent à faible puissance.
   - Or cette issue se lit comme « la forme explicite du regard ». À faible puissance, elle ne devrait pas se lire sans une comparaison directe des deux cadrages.
4. **Un petit gain bien mesuré se lit « gain de contenu ».** À 5 × 400 × 10 sans variabilité, le gain de 3 points rend « gain de contenu » dans 66 % des répliques.
   - La ligne du contenu ne demande pas l'effet minimal, et elle passe avant celle des petits gains.
   - Le gain est attribué au contenu : ce n'est pas faux, mais l'effet minimal n'y est pas rappelé.

## Ce qui en suit, pour ta décision (rien n'est changé)

- **Le nombre de graines** se fixera sur l'écart entre entraînements que le pilote mesurera. Si cet écart est de l'ordre de 2 points, il en faudrait bien plus de 5 par bras, ce qui coûte en entraînements.
- **Les constats 3 et 4** touchent la lecture de la table A.2 du texte déposé, pas le code. Les préciser dans l'amendement, avant les données des bras, éviterait deux lectures trompeuses :
  - pour le constat 3 : lire « un gain sous évaluation seulement » seulement si la différence des gains entre les deux cadrages est elle-même nette ;
  - pour le constat 4 : rappeler l'effet minimal à côté du « gain de contenu ».

  Ce serait une précision de règle, donc ta décision. Je ne l'écris pas dans le brouillon de la mise à jour sans ton accord.

## Les deux précisions, prêtes pour ta décision (9 octobre, 0 h 30 UTC)

**Statut : adoptées le 9 octobre 2026, vers 6 h UTC (décision 52 : « ok pour les deux précisions de la table A.2 »).** Leur texte anglais est la partie 8 de la mise à jour datée, avec l'empreinte du code au commit `373f24b` (`claude/MISE_A_JOUR_PREMIER_TEMPS_BROUILLON_2026-10-08.md`). Ce commit ne change aucune issue : quand la première fait tomber l'issue principale hors des gains, il marque sans objet la relecture parmi les engagés.
- Le fichier déposé, `porte_des_raisons.py`, n'est pas touché : son empreinte reste `5868d082…`, celle de la décision 46.
- Les précisions changent une règle : elles vont dans la mise à jour datée, justifiées, avant toute donnée des bras (texte déposé, section 6.2).

**Ce qui est écrit.**
- `experiences/analyses/precisions_a2.py` : les deux précisions, qui lisent la sortie de la porte, avec 7 tests (`tests/test_precisions_a2.py`) ; l'empreinte proposée était `8ba268cc…`, celle du code adopté est `5d7ed240…`.
- `experiences/analyses/puissance_precisions_a2.py` : la simulation refaite avec elles, avec 2 tests. Ses sorties, à 400 répliques par configuration : `experiences/resultats/puissance/puissance_precisions_a2_2026-10-09.json`.
- **Les deux cadrages y sont tirés ensemble**, de deux façons :
  - **appariés**, comme le plan déposé (section 2.3 : chaque scénario passe dans chaque entraînement sous les deux cadrages) : la difficulté d'un scénario et l'écart d'un entraînement sont les mêmes sous les deux ;
  - **indépendants**, comme la simulation plus haut. Elle y retrouve ses chiffres : 20 % pour le lien et 19 % pour le format, à 3 graines × 200 × 5 avec ±2 points, contre 23 et 22 % plus haut, sur 200 répliques.

### La première : « un gain sous évaluation seulement »

**Ce qu'elle dit.**
- La ligne ne se lit que si la différence des gains entre les deux cadrages est elle-même établie. Chaque gain est le taux des actions seules moins celui des raisons.
- L'IC à 95 % de (gain sous évaluation − gain sous déploiement) doit exclure 0 en faveur de l'évaluation.
- Le bootstrap croisé tire les mêmes graines et les mêmes scénarios sous les deux cadrages. Sous huit graines, Student sur les contrastes par graine, s'il est plus large.
- Sinon, la lecture continue comme le code déposé la fait : « pas de gain sous déploiement » si les raisons ≈ les actions seules sous déploiement, « non conclusif » sinon.

**Ce qu'elle change, sous le plan déposé (cadrages appariés).** La part des répliques qui lisent « un gain sous évaluation seulement », sans la précision → avec elle :

| Graines × scénarios × générations | Écart entre entraînements | Lien | Format | Petit gain | Regard explicite |
|---|---|---|---|---|---|
| 3 × 200 × 5 | aucun | 1 → 0 % | 1 → 0 % | 16 → 0,3 % | 98 → 84 % |
| 3 × 400 × 5 | aucun | 0 → 0 % | 0 → 0 % | 23,5 → 0,3 % | 99,5 → 98,3 % |
| 3 × 400 × 10 | aucun | 0 → 0 % | 0 → 0 % | 21,2 → 0 % | 99,8 → 99,8 % |
| 5 × 200 × 5 | aucun | 0 → 0 % | 0 → 0 % | 22,5 → 0 % | 99,5 → 99,5 % |
| 5 × 400 × 5 | aucun | 0 → 0 % | 0 → 0 % | 8,3 → 0 % | 99,5 → 99,5 % |
| 5 × 400 × 10 | aucun | 0 → 0 % | 0 → 0 % | 0 → 0 % | 99,3 → 99,3 % |
| 3 × 200 × 5 | 2 points | 11,3 → 0 % | 11,3 → 0 % | 9,5 → 0 % | 74,5 → 65,2 % |
| 3 × 400 × 5 | 2 points | 8,5 → 0 % | 8,5 → 0 % | 8 → 0 % | 72,8 → 72 % |
| 3 × 400 × 10 | 2 points | 6,8 → 0 % | 6,2 → 0 % | 6,8 → 0 % | 76,2 → 76,2 % |
| 5 × 200 × 5 | 2 points | 0,5 → 0 % | 0,5 → 0 % | 15,2 → 0,3 % | 95 → 95 % |
| 5 × 400 × 5 | 2 points | 0,5 → 0 % | 0,5 → 0 % | 11,3 → 0,3 % | 90,5 → 90,5 % |
| 5 × 400 × 10 | 2 points | 0 → 0 % | 0 → 0 % | 9,5 → 0 % | 89 → 89 % |

- **Sous le lien, le format et le petit gain**, le gain est le même sous les deux cadrages : toute lecture « sous évaluation seulement » y est fausse.
- **Sous le regard explicite**, il n'y a aucun gain sous déploiement, et le profil du lien sous évaluation (10 points) : toute lecture « sous évaluation seulement » y est juste.

**Ce qu'elle montre.**
1. **Le petit gain trompe le plus** : jusqu'à 23,5 % de lectures fausses, et encore 22,5 % à cinq graines sans écart entre entraînements. Un gain de 3 points sous les deux cadrages sort souvent indéterminé sous déploiement et établi sous évaluation, par le seul hasard. Avec la précision, il en reste au plus 0,3 %, quel que soit le cas.
2. **Ce qu'elle coûte quand le regard explicite est vrai** :
   - à cinq graines, rien : chaque lecture juste est gardée ;
   - à trois graines, de 0 à 14 points : 98 → 84 % à 200 scénarios × 5 générations sans écart, 74,5 → 65,2 % avec l'écart de 2 points. Les répliques perdues se lisent presque toutes « non conclusif ».
3. **C'est l'appariement du plan déposé qui la rend peu coûteuse.** Sous des cadrages indépendants, elle coûterait bien plus : 72 → 41 % à 3 × 200 × 5 avec l'écart. Les écarts d'un entraînement, communs aux deux cadrages, s'annulent dans la différence des gains.

### La seconde : « gain de contenu »

**Ce qu'elle dit.** Quand l'estimation des raisons sur les actions seules est sous l'effet minimal, l'issue devient « gain de contenu, plus petit que l'effet minimal ». Ni la ligne ni son rang ne changent.

**Ce qu'elle change.**
- Sous le petit gain, à 5 × 400 × 10 sans écart (cadrages appariés), la table lit « gain de contenu » dans 67 % des répliques. Avec la précision, toutes ces lectures disent qu'il est plus petit que l'effet minimal.
- Ailleurs, presque rien ne bouge : sous le lien et le format, les issues sont les mêmes ; sous le regard explicite, une seule réplique change, sur 400, dans une seule configuration (3 × 400 × 10, avec l'écart de 2 points).

### Le texte à coller dans la mise à jour datée, si tu les adoptes (anglais)

```
7. Two precisions of the reading of Appendix A.2 (the reasons gate). They change a rule before any data of the trained
   arms (section 6.2). They are justified by a power simulation run on simulated counts only, described below.

   (a) The "evaluation only" row is read only if the difference between the gains under the two framings is itself
       established. Each gain is the actions-only rate minus the reasons rate, in points. The 95% CI of (the gain under
       evaluation framing minus the gain under deployment framing) must exclude 0 in favour of evaluation framing. The
       framings are paired (section 2.3): the crossed bootstrap draws the same seeds and the same scenarios for both.
       Under eight seeds, Student on the per-seed contrasts gives the CI when it is wider (section 5.3). Otherwise the
       row does not apply, and the reading goes on as before: "no gain under deployment" if reasons ≈ actions only
       under deployment framing, and inconclusive otherwise.

   (b) When the estimate of reasons against actions only is below the minimal effect, the "content gain" outcome reads
       "content gain, smaller than the minimal effect". The row and its place in the reading order do not change.

   Both also apply when the gate is read again among engaged episodes (Appendix A.0).

   Why. A power simulation of the gate, on simulated counts with paired framings, found two misleading readings.
   - When the gain was the same under both framings, the "evaluation only" row was read in up to 11.3% of
     replicates with three seeds per arm and a spread of 2 points between training runs. With a gain of 3 points under
     both framings, it was read in up to 23.5%, and in 22.5% with five seeds. With (a), in at most 0.3%.
   - When the gain existed under evaluation framing only, (a) kept every reading of the row with five seeds, and lost
     at most 14 points with three.
   - A well-measured gain of 3 points was read as a content gain in 67% of replicates (five seeds, 400 scenarios,
     10 generations), without the minimal effect being stated.

   The code: precisions_a2.py, SHA-256 8ba268cc7c897413d8b9e86c61a80371148d667747d1d9338b9e003370f943b3. It reads the
   output of porte_des_raisons.py, which is unchanged. The simulation: puissance_raisons.py, SHA-256
   dd97f04692a0ef2601588b28584958a79ba147e9ba67d09a84c128b73209ee13; puissance_precisions_a2.py, SHA-256
   03c27bed977f5ef5b4c140c5c0d0ca77c6a287cbc3af463a28514f2e6f47e983.
```

**Ta décision** : oui ou non, pour chacune des deux. Rien n'entre dans le brouillon de la mise à jour sans ton accord.

## Combien de graines par bras (9 octobre, 1 h UTC)

**Ce qui est simulé.** La même porte et les mêmes vérités, au-delà de cinq graines : 5, 8, 10, 12 et 16 graines par bras, 400 scénarios × 5 générations, un écart entre entraînements de 1, 2 ou 3 points, 400 répliques par configuration (`experiences/analyses/puissance_raisons_graines.py` ; sorties : `experiences/resultats/puissance/puissance_raisons_graines_2026-10-09.json`).

**La part des répliques où la porte rend la bonne issue :**

| Vérité | Écart entre entraînements | 5 graines | 8 | 10 | 12 | 16 |
|---|---|---|---|---|---|---|
| Lien | 1 point | 72 % | 97 % | 99 % | 100 % | 100 % |
| Lien | 2 points | 34 % | 74 % | 86 % | 88 % | 96 % |
| Lien | 3 points | 15 % | 49 % | 63 % | 62 % | 74 % |
| Format | 1 point | 78 % | 98 % | 96 % | 99 % | 99 % |
| Format | 2 points | 24 % | 66 % | 76 % | 84 % | 95 % |
| Format | 3 points | 6 % | 31 % | 36 % | 46 % | 69 % |
| Aucun gain | 1 point | 47 % | 88 % | 92 % | 97 % | 98 % |
| Aucun gain | 2 points | 3 % | 33 % | 51 % | 67 % | 84 % |
| Aucun gain | 3 points | 0 % | 6 % | 12 % | 20 % | 44 % |
| Petit gain | 1 point | 56 % | 56 % | 49 % | 43 % | 36 % |
| Petit gain | 2 points | 26 % | 57 % | 61 % | 66 % | 55 % |
| Petit gain | 3 points | 9 % | 38 % | 46 % | 51 % | 58 % |

**Ce que la table dit.**
1. **Avec un écart de 1 point entre entraînements**, 8 graines par bras suffisent : de 88 à 98 % de bonnes issues pour le lien, le format et l'absence de gain.
2. **Avec 2 points**, il en faut de 10 à 16 : à 16 graines, 96 % pour le lien, 95 % pour le format, 84 % pour l'absence de gain.
3. **Avec 3 points**, même 16 graines ne suffisent pas (de 44 à 74 %).
4. **Le petit gain reste mal lu** (au plus 66 %) : plus la mesure est précise, plus il se lit « gain de contenu » (le constat 4 ; la seconde précision le nomme).
5. **Le coût** : 6 bras × le nombre de graines. À 10 graines, 60 entraînements ; à 16, 96, contre 12 au pilote. Le coût d'un entraînement n'est pas encore mesuré ; le pilote le mesurera, avec l'écart entre entraînements.

**Une réserve sur le saut de 5 à 8 graines.** À 8 graines, la règle déposée cesse de prendre le plus large du bootstrap et de Student (section 5.3) : une part du saut vient de là, pas de l'information en plus. Or, quand aucun bras ne fait mieux, les faux gains montent à 8 et 10 graines : de 5,8 à 9,6 % avec un écart de 2 à 3 points, contre 2,8 % à 5 graines. Un bootstrap par grappes, sur peu de grappes, couvre souvent moins que son niveau. La calibration de la comparaison principale, selon le nombre de graines, est mesurée à part (`experiences/analyses/calibration_bootstrap.py`, écrit avant le calcul).

## La calibration de la comparaison principale, selon le nombre de graines (9 octobre, 1 h 50 UTC)

**Ce qui est mesuré.** Quand les six bras ont le même taux (30 %), la part des répliques où la comparaison « raisons contre actions seules », sous déploiement, sort « < » (un faux gain) ou « > ». Le niveau nominal est de 2,5 % de chaque côté. Il y a 1 000 répliques par configuration, soit une erreur de Monte Carlo d'environ 0,5 point. Le script a été commité avant le calcul (`experiences/analyses/calibration_bootstrap.py` ; sorties : `experiences/resultats/puissance/calibration_bootstrap_2026-10-09.json`).

**La règle déposée** (le plus large du bootstrap et de Student sous huit graines, le bootstrap seul au-delà) ; chaque case donne la part de « < » / la part de « > » :

| Écart entre entraînements | 3 graines | 5 | 8 | 10 | 12 | 16 |
|---|---|---|---|---|---|---|
| 1 point | 0,8 / 0,8 % | 0,4 / 0,6 % | 0,9 / 0,8 % | 0,6 / 0,6 % | 0,8 / 0,7 % | 0,9 / 0,6 % |
| 2 points | 1,6 / 2,1 % | 1,5 / 2,5 % | 2,3 / 1,8 % | 2,0 / 2,0 % | 1,6 / 1,3 % | 2,4 / 1,2 % |
| 3 points | 1,7 / 2,2 % | 2,4 / 2,3 % | **3,8 / 3,1 %** | **3,1 / 3,7 %** | **3,2 / 3,7 %** | 2,1 / 2,7 % |

**Toujours le plus large des deux**, quel que soit le nombre de graines : à 3 points, 2,6 / 1,6 % à 8 graines, 2,5 / 2,7 % à 10, 2,7 / 3,1 % à 12, 1,8 / 2,3 % à 16. Sous 8 graines, les deux règles sont la même.

**Ce que cela dit.**
1. **La comparaison principale est bien calibrée** tant que l'écart entre entraînements ne dépasse pas 2 points, quel que soit le nombre de graines.
2. **À 3 points, de 8 à 12 graines, elle devient légèrement trop libérale** : environ 7 % de faux positifs au total, pour 5 % attendus. Le bootstrap par grappes, sur 8 à 12 graines, couvre un peu moins que son niveau quand la variance entre graines domine.
3. **Les faux gains de la simulation des graines viennent surtout des chemins multiples de la table.** Quand aucun bras ne fait mieux, deux lignes de gain peuvent sortir par hasard : un gain sous évaluation seulement, et un gain plus petit que l'effet minimal (3,0 et 2,8 % à 8 graines et 2 points d'écart). La première précision proposée ferme le premier chemin.
4. **Une précision possible, pour ta décision** : prendre toujours le plus large des deux intervalles, quel que soit le nombre de graines. Elle coûte un peu de puissance, et ne compte que si le pilote mesure un écart entre entraînements de l'ordre de 3 points. Elle peut attendre le pilote et l'amendement du second temps, qui fixe le nombre de graines.

## La règle du regard, avec un niveau propre à chaque entraînement (9 octobre, 2 h 15 UTC)

**Ce qui est mesuré.** La simulation du 3 octobre (`puissance_regard.py`) ne donne d'écart propre qu'à l'effet de l'inhibition chez les raisons. Celle-ci ajoute à chaque entraînement d'un bras son propre niveau, commun à ses deux interventions. La question et l'attente ont été commitées avant le calcul (`experiences/analyses/puissance_regard_entrainements.py`, commit `626e84f` ; sorties : `experiences/resultats/puissance/puissance_regard_entrainements_2026-10-09.json`). Le cadre : un avantage de 10 points, 400 scénarios × 10 générations, un écart de 2 points de l'effet de l'inhibition, et 200 répliques.

| | 5 graines | 8 graines | 12 graines |
|---|---|---|---|
| Ligne 2, « l'avantage survit » (vraie fraction 0), sans niveau propre | 34 % | 72,5 % | 90 % |
| La même, avec un niveau propre de 2 points | 34,5 % | 66,5 % | 85 % |
| Ligne 1, « le regard » (vraie fraction 0,5), sans niveau propre | 95 % | 100 % | 100 % |
| La même, avec un niveau propre de 2 points | 92,5 % | 100 % | 100 % |

**Ce que cela dit.**
1. **Le niveau propre de chaque entraînement change peu** : il s'annule dans D. Il coûte jusqu'à 6 points à la ligne 2, par l'incertitude de l'avantage sous le comparateur, le dénominateur de f. J'attendais ce sens.
2. **Ce qui décide la ligne 2, c'est l'écart de l'effet de l'inhibition d'un entraînement à l'autre.** Le texte déposé dit qu'un avantage de 10 points demande « about 400 × 10 and at least 5 seeds » (section 3.5). C'est vrai sans cet écart : 89 % à 5 graines, dans la simulation du 3 octobre. Avec 2 points d'écart, il faut de l'ordre de 12 graines pour lire la ligne 2 dans 85 à 90 % des répliques.
3. **Le texte le prévoit** : la simulation de l'amendement du second temps refera ce calcul avec la variance du pilote. Ce constat dit seulement que le nombre de graines, pour le test du regard comme pour la porte des raisons, risque d'être bien plus haut que cinq.

## Quand les graines partagées corrèlent les entraînements (9 octobre, 2 h 20 UTC)

**Ce qui est mesuré.** Le texte déposé partage les graines entre bras : même initialisation, même ordre des données (section 2.4). Si cela corrèle l'écart d'un entraînement d'un bras à l'autre, au sein d'une graine, les contrastes par graine perdent une part de cette variance : var(o_a − o_r) = 2σ²(1 − ρ). Les simulations précédentes supposaient ρ = 0. La question et l'attente ont été commitées avant le calcul (`experiences/analyses/puissance_raisons_correlation.py`, commit `b0d188f` ; sorties : `experiences/resultats/puissance/puissance_raisons_correlation_2026-10-09.json`). Le cadre : un écart de 2 points entre entraînements, 400 scénarios × 5 générations, 200 répliques.

**La part des répliques où la porte rend la bonne issue** (lien / format / aucun gain) :

| ρ | 5 graines | 8 graines | 12 graines |
|---|---|---|---|
| 0 | 32 / 19,5 / 5 % | 72 / 60 / 31 % | 89 / 87,5 / 67,5 % |
| 0,5 | 51 / 58 / 24 % | 89,5 / 87 / 73 % | 95 / 94,5 / 93 % |
| 0,8 | 75 / 85,5 / 56 % | 97,5 / 97 / 92,5 % | 100 / 98,5 / 97,5 % |

**Ce que cela dit.**
1. **À ρ = 0,8, 8 graines par bras suffisent** (de 92,5 à 97,5 %), là où il en faut de 12 à 16 à ρ = 0. J'attendais « 5 à 8 » : à 5, ce n'est pas encore assez (de 56 à 85,5 %).
2. **Ce que le pilote doit mesurer**, c'est la variance des contrastes par graine entre bras, pas seulement l'écart entre entraînements : c'est elle qui fixe le nombre de graines.
3. **Le pilote la mesure mal.** Avec deux graines par bras, chaque contraste n'a que deux valeurs. La simulation de l'amendement du second temps devra le dire, et prendre une hypothèse prudente si l'estimation est trop large.

## Ce que le pilote peut estimer de cette variance (9 octobre, 2 h 25 UTC)

**Ce qui est mesuré.** Avec six bras et 2, 3 ou 4 graines par bras, l'estimation de l'écart des contrastes par graine, √(2σ²(1 − ρ)), par une analyse de variance bras × graine, le bruit binomial retiré. 2 000 pilotes simulés par cas, à 400 scénarios × 5 générations. La question et l'attente ont été commitées avant le calcul (`experiences/analyses/pilote_variance.py`, commit `535aec4` ; sorties : `experiences/resultats/puissance/pilote_variance_2026-10-09.json`).

**L'estimation rapportée à la vraie valeur** (5ᵉ centile – médiane – 95ᵉ centile), à σ = 2 points :

| ρ | 2 graines | 3 graines | 4 graines |
|---|---|---|---|
| 0 | 0,17 – 0,90 – 1,54 | 0,46 – 0,93 – 1,42 | 0,60 – 0,98 – 1,36 |
| 0,5 | 0 – 0,93 – 1,68 (11 % des estimations à zéro) | 0,24 – 0,95 – 1,50 | 0,45 – 0,96 – 1,39 |
| 0,8 | 0 – 0,84 – 1,93 (27 % à zéro) | 0 – 0,88 – 1,69 (17 % à zéro) | 0 – 0,95 – 1,58 (11 % à zéro) |

À σ = 1 point, c'est pire : de 24 à 49 % des estimations tombent à zéro avec deux graines.

**Ce que cela dit.**
1. **Deux graines par bras estiment mal la variance qui fixe le nombre de graines** : l'estimation peut se tromper du simple au double, et tombe souvent à zéro une fois le bruit binomial retiré. J'attendais l'imprécision, pas la fréquence des zéros.
2. **La simulation de l'amendement du second temps ne devrait pas prendre l'estimation du pilote telle quelle**, mais une borne prudente : par exemple, sa limite haute à 90 %, ou une plage d'hypothèses.
3. **Une option, pour ta décision** : trois ou quatre graines par bras au pilote. Le texte en prévoit deux (section 2.3) ; c'est une règle, à changer par une mise à jour datée avant le pilote. Chaque graine de plus coûte six entraînements.
4. **Une réserve** : la distance lointaine du pilote compte 200 scénarios (40 par famille tenue à part), pas 400 ; le bruit binomial y est plus fort, et l'estimation moins bonne encore.

## La borne prudente de la variance du pilote (9 octobre, 10 h UTC)

**Pourquoi.** La décision 53 garde deux graines par bras au pilote. Elle demande une règle écrite avant lui : la simulation du second temps doit lire une borne prudente de la variance des contrastes par graine, et non son estimation seule. La question, les règles et l'attente ont été commitées avant le calcul (`experiences/analyses/borne_prudente_graines.py`, commit `b5e0e3e` ; sorties : `experiences/resultats/puissance/borne_prudente_graines_2026-10-09.json`).

**Ce qui est mesuré.** 2 000 pilotes simulés par cas (6 bras × 2 graines, 400 scénarios × 5 générations). Quatre règles donnent chacune une variance des contrastes par graine, d'où un nombre de graines par une approximation déclarée des simulations du 9 octobre, n(v) = ⌈6,3 + 0,83 v⌉ :
- l'estimation seule ;
- la borne haute unilatérale à 80 %, puis à 90 %, par la loi du khi-deux à 5 degrés de liberté ;
- l'estimation seule, avec un plancher à l'écart de 2 points.

**La part des pilotes qui donnent assez de graines** (la médiane et le 90ᵉ centile du nombre donné, entre parenthèses) :

| σ | ρ | Graines qu'il faut | Estimation seule | Borne à 80 % | Borne à 90 % | Plancher à 2 points |
|---|---|---|---|---|---|---|
| 1 | 0 | 8 | 60 % (8 ; 11) | 89 % (11 ; 19) | 95 % (14 ; 25) | 100 % (13 ; 13) |
| 1 | 0,5 | 8 | 45 % (7 ; 10) | 82 % (10 ; 15) | 92 % (12 ; 20) | 100 % (13 ; 13) |
| 1 | 0,8 | 7 | 100 % (7 ; 9) | 100 % (9 ; 13) | 100 % (11 ; 17) | 100 % (13 ; 13) |
| 2 | 0 | 13 | 48 % (12 ; 21) | 83 % (20 ; 39) | 91 % (27 ; 54) | 100 % (13 ; 21) |
| 2 | 0,5 | 10 | 49 % (9 ; 14) | 84 % (14 ; 25) | 92 % (19 ; 34) | 100 % (13 ; 14) |
| 2 | 0,8 | 8 | 56 % (8 ; 11) | 87 % (11 ; 17) | 94 % (13 ; 23) | 100 % (13 ; 13) |
| 3 | 0 | 22 | 41 % (19 ; 35) | 79 % (35 ; 64) | 89 % (49 ; 64) | 41 % (19 ; 35) |
| 3 | 0,5 | 14 | 46 % (13 ; 22) | 83 % (22 ; 42) | 92 % (30 ; 59) | 46 % (13 ; 22) |
| 3 | 0,8 | 10 | 45 % (9 ; 13) | 82 % (14 ; 23) | 90 % (18 ; 31) | 100 % (13 ; 13) |

**Ce que cela dit.**
1. **L'estimation seule ne donne assez de graines que dans un pilote sur deux environ.** J'attendais ce chiffre ; j'attendais aussi qu'il baisse quand ρ grandit, et ce n'est pas le cas. À σ = 1 et ρ = 0,8, elle suffit toujours, parce que le nombre qu'il faut est déjà au bas de l'approximation.
2. **La borne à 80 % suffit dans 79 à 89 % des pilotes.** Son coût médian est d'environ une fois et demie le besoin, et son 90ᵉ centile monte jusqu'au triple.
3. **La borne à 90 % suffit dans 89 à 95 % des pilotes**, pour un coût médian d'environ deux fois le besoin.
4. **Le plancher à 2 points protège tant que l'écart vrai ne le dépasse pas**, et paie trop quand ρ est grand ; à 3 points, il ne protège plus.
5. **Les limites.** L'approximation n(v) vient des simulations de la porte des raisons, pas d'un calcul pour chaque cible du second temps. La distance lointaine du pilote compte 200 scénarios, pas 400 : la vraie estimation y sera plus bruitée encore.

**Ce que je recommande, pour ta décision.** Faire lire au second temps la borne à 80 %, avec un plafond de graines fixé d'avance. Si le plafond s'applique, l'amendement du second temps dit la puissance atteinte, comme le texte déposé le prévoit déjà pour la ligne 2. Le plafond est un choix de budget : chaque graine de plus coûte six entraînements. Ajouter le plancher à 2 points relèverait la part des pilotes suffisants quand l'écart vrai est faible ou moyen (à σ = 2 et ρ = 0 : 100 % au lieu de 83 %), mais avec un coût fixe d'au moins 13 graines par bras ; je ne le recommande pas, et le choix se discute.

**Le texte à verser dans la mise à jour datée, si tu l'adoptes (anglais).**

```
How the stage-2 simulation reads the pilot's variance (sections 3.4 and 3.5). The per-seed contrast variance that sizes
the study is not the pilot's estimate but its one-sided 80% upper bound: twice the residual mean square of the arm ×
seed analysis of variance (6 arms, 2 seeds, 5 degrees of freedom) times 5 / 2.343 (the 20% quantile of the chi-square
distribution with 5 degrees of freedom), minus the binomial variance of a rate. The number of seeds per arm is the
smallest that reaches the targets of section 3.5 in the stage-2 simulation, up to [N] seeds per arm, stated now. If that
maximum binds, the stage-2 amendment states the power reached.
```
