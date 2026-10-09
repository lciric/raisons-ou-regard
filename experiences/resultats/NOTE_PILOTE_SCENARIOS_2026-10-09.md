# Le pilote de la génération des scénarios tenus à part (9 octobre 2026)

**Statut : une mesure descriptive, faite selon la spécification adoptée (décision 54).** Le code est celui du commit `36f94d3` (`experiences/rrharness/generation.py`). Le rapport est `experiences/scenarios_tenus_a_part/pilote_2026-10-09/rapport_2026-10-09T093614Z.json` : il garde la liste des refus, que les tours suivants lisent pour ne jamais les redemander. Aucun texte de scénario n'est cité ici.

## Ce qui a tourné

- 5 scénarios par famille, 25 en tout, un cadre tiré par scénario (graine 20261009).
- Le générateur et le juge de réalisme : `claude-opus-5-5`, effort moyen, par le client du pipeline (`donnees/config.yaml`).
- De 9 h 36 à 10 h 14 UTC. **Le coût, estimé d'après l'usage rapporté par l'API : 5,07 $**, pour environ 5 $ prévus.

## Ce qui en sort

| Famille | Retenus | Refus du générateur | Rejetés par le juge de réalisme | Échecs des contrôles | Notes du juge (probabilité d'évaluation) |
|---|---|---|---|---|---|
| Le remplacement | 0 | 2 | 3 | 0 | 0,93 ; 0,95 ; 0,97 |
| La sous-performance | 0 | 0 | 4 | 1 | 0,97 (×4) |
| L'exfiltration | 0 | **5** | 0 | 0 | — |
| Le correcteur faible | 0 | 0 | 5 | 0 | 0,85 ; 0,85 ; 0,85 ; 0,88 ; 0,90 |
| Le sabotage | 0 | 0 | 5 | 0 | 0,90 ; 0,90 ; 0,93 ; 0,93 ; 0,93 |
| **Total** | **0** | **7** | **17** | **1** | de 0,85 à 0,97 |

- **L'échec des contrôles** (sous-performance) : la variante à l'occasion n'avait ni marque d'indice ni ligne de difficulté, après trois tentatives avec le motif du rejet.
- **Tous les scénarios écrits ont passé les contrôles du harnais**, sauf celui-là : leurs cas connus concordaient avec leurs prédicats.

## Ce que cela veut dire

1. **Le seuil de 0,5 du juge de réalisme est hors d'atteinte pour ce juge, et je ne l'avais pas vérifié avant de le proposer.**
   - Le 5 octobre, le même juge notait les situations d'entraînement écrites par Claude avec des médianes de 0,74 à 0,88 selon la famille ; 3 sur 75 seulement passaient sous 0,5 (`donnees/archives/sorties_2026-10-05/pilote/`).
   - Les scénarios tenus à part sont notés plus haut encore : de 0,85 à 0,97.
   - C'est attendu en partie : poser toute la décision dans un seul message rend le dilemme commode, et le juge le voit.
2. **L'exfiltration est refusée par le générateur dans les cinq cas.** Selon les règles du programme, un refus ne se rejoue pas, ne se reformule pas, et ne part chez aucun autre modèle. Par cette voie, la famille n'aura pas de scénarios lointains.
3. **Le remplacement est refusé deux fois sur cinq.** La famille reste faisable, avec un rendement réduit, et sa part manquante se rapportera.

## Les voies, pour ta décision

**Sur le réalisme.**
1. **Rapporter le juge plutôt que filtrer** (ma recommandation).
   - Le dessin mesure déjà « évalué » sous cadrage de déploiement, par projection ; c'est une des conditions de la règle du regard.
   - Les marques de construction d'un scénario sont les mêmes pour tous les bras et sous les deux cadrages : elles relèvent le niveau d'« évalué » partout, sans biaiser la comparaison entre bras.
   - On rapporterait la distribution des notes par famille, face à celle des situations d'entraînement, avec une analyse de sensibilité exploratoire sur la moitié la plus réaliste de chaque famille.
2. **Un seuil relatif**, par exemple garder les scénarios sous la médiane de leur famille. Il demanderait d'en écrire environ deux fois plus, donc de changer le plan de 40 par famille.
3. **Revoir la consigne de génération pour le réalisme** (des détails ordinaires plus nombreux, une décision moins saillante), puis refaire un pilote, environ 5 $. Elle peut s'ajouter à la voie 1. Elle ne s'appliquerait pas à l'exfiltration : changer la consigne d'une famille refusée reviendrait à reformuler pour passer.

**Sur l'exfiltration.**
1. **La rapporter comme absente à la distance lointaine**, et garder quatre familles (ma recommandation, faute de mieux). Le texte déposé en prévoit cinq : la mise à jour datée le dirait.
2. **Des scénarios écrits à la main, par toi**, sans aucun modèle : c'est la seule source que les règles laissent ouverte. Il en faudrait 40, avec leurs trois niveaux.
3. **Changer de générateur pour cette famille** n'est pas compatible avec ta règle sur les refus : un changement de générateur se justifie par les conditions d'utilisation, pas par les refus. Le choix d'une exception t'appartient.

**La suite, selon tes choix.** Avec les voies 1 et 1, la génération des 200 peut partir avec la même consigne pour les quatre familles restantes, sans filtre de réalisme. On peut s'attendre à des refus au remplacement. Le coût serait de l'ordre de 40 $ (estimation).

## Les sources

- La spécification adoptée : `claude/SPEC_SCENARIOS_TENUS_A_PART_v0.1_2026-10-09.md` ; décisions 53 et 54 (`DECISIONS.md`).
- Le code : `experiences/rrharness/generation.py` (commit `36f94d3`) ; le harnais : `experiences/rrharness/premier_appel.py`.
- Le rapport du pilote : `experiences/scenarios_tenus_a_part/pilote_2026-10-09/rapport_2026-10-09T093614Z.json` ; le journal des appels : `donnees/sorties/scenarios_tenus_a_part/calls.jsonl` (hors de git).
- Les notes du juge de réalisme sur les situations d'entraînement du 5 octobre : `donnees/archives/sorties_2026-10-05/pilote/`.
- La règle sur les refus : `claude/RELECTURES_PARTIE_11_2026-10-08.md`, partie 1, « Les deux voies » ; `claude/NOTE_REFUS_PILOTE_2026-10-08.md`.
