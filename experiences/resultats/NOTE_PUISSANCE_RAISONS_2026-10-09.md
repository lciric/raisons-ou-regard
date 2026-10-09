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

**Statut : proposées, rien n'est adopté.**
- Le fichier déposé, `porte_des_raisons.py`, n'est pas touché : son empreinte reste `5868d082…`, celle de la décision 46.
- Les précisions changeraient une règle. Adoptées, elles iraient dans la mise à jour datée, justifiées, avant toute donnée des bras (texte déposé, section 6.2).

**Ce qui est écrit.**
- `experiences/analyses/precisions_a2.py` : les deux précisions, qui lisent la sortie de la porte, avec 7 tests (`tests/test_precisions_a2.py`).
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
- Rien d'autre ne bouge : sous le lien, le format et le regard explicite, les issues sont les mêmes.

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
