# Les refus du pilote du 5 octobre, et ce que le générateur ouvert y change (8 octobre 2026)

**Statut : une lecture du journal, pour la décision qui t'attend** (programme v1.6, partie 12, point 3 : « les refus et le rendement du pipeline », à trancher avant la génération complète). Aucun refus n'est rejoué ni reformulé : on lit seulement le journal des appels.

**La source** : `donnees/archives/sorties_2026-10-05/pilote/logs/calls.jsonl` (1 705 appels), avec le plan et les éléments finaux du même dossier.

## Qui a refusé quoi

| | Situations | Actions | Textes neutres | Juge de réalisme | Juge de la conscience d'évaluation | Total |
|---|---|---|---|---|---|---|
| Le générateur (Claude) | 25 | 7 | 14 | — | — | 46 |
| Les juges (Claude) | — | — | — | 29 | 3 | 32 |

**Par famille** (27 éléments au plan dans chacune, pour 20 visés) :

| Famille | Refus du générateur | Refus du juge de réalisme | Appels au juge de réalisme | Éléments finaux |
|---|---|---|---|---|
| L'opérateur | 0 | 0 | 27 | 20 |
| La demande nuisible | 14 (13 situations, 1 texte neutre) | 0 | 14 | 13 |
| La surveillance | 16 (7 actions, 9 textes neutres) | **22** | 25 | 6 |
| Le périmètre | 15 (12 situations, 3 textes neutres) | 7 | 11 | 5 |
| La contestation | 1 (texte neutre) | 0 | 26 | 3 |

## Ce que le générateur ouvert y change, et ce qu'il n'y change pas

- **Les 46 refus du générateur disparaissent comme refus de Claude** : le modèle ouvert écrit les situations, les actions et les textes neutres (décision 37). Il peut refuser à sa façon. Le pilote ouvert le dira, en famille par famille.
- **Les 32 refus des juges restent** : Claude reste juge. Ils tombent surtout sur la surveillance, où le juge de réalisme a refusé 22 des 25 situations qu'il a reçues.
- **La surveillance restera donc la famille la plus pauvre**, quel que soit le générateur, tant que ce juge refuse ses situations.
- **La contestation a une autre cause** : le juge ne la refuse pas, mais la contrainte de ses donneurs limite son rendement (partie 3, la contrainte du raisonnement d'une autre situation).
- **La demande nuisible et le périmètre** devraient gagner le plus : leurs refus venaient surtout du générateur, sur les situations.

## Les voies, pour ta décision

1. **Garder les juges tels quels**, et rapporter une surveillance sous-représentée. C'est le plus simple ; la famille pèserait peu dans les bras.
2. **Planifier davantage d'éléments de surveillance**, pour compenser. Ce ne sont pas des refus rejoués : ce sont de nouveaux éléments.
   - Mais seules les situations que le juge accepte survivent. Ce tri serait à rapporter.
   - Il coûte environ trois fois plus d'appels sur cette famille.
3. **Faire juger le réalisme par un modèle ouvert** (JEV-27B, par exemple), pour toutes les familles ou pour la surveillance seule. C'est changer un juge du pipeline, adopté par la décision 20, et il faudrait le valider sur les situations que Claude accepte.

Le pilote ouvert mesurera le nouveau rendement famille par famille. La décision peut l'attendre.
