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
