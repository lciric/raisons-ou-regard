# Le premier organisme : documents, puis expert iteration (3 octobre 2026)

**Statut : exploratoire.** C'est la construction du cas connu de la validation de l'instrument (programme v1.5, partie 4 ; décisions 27 et 28). Aucune règle n'est encore gelée pour lui.

## Les sources

- **Les documents** : `sdf_documents-20261003-161828-6b4b`. Qwen3-14B les écrit à partir de `experiences/organisme/univers.yaml`. 9 533 sont gardés sur 9 995, environ 5,3 millions de mots.
- **L'essai sans documents** : `organism-20261003-160500-ede3`. La ligne de base, puis un tour d'expert iteration, sur 100 tâches.
- **L'organisme complet** : `organism-20261003-164800-9e3e`.
  - Un H100 SXM, 8,70 $ au plus. Code au commit `20304a8`.
  - La ligne de base, puis les documents (un LoRA de rang 32, une époque, 200 pas), puis trois tours d'expert iteration.
  - Les mesures portent sur 300 tâches de MBPP test, en glouton, sous cinq cadrages.
  - Les sorties sont dans `runs/<run>/out/` du dépôt `Sirmium/rr-resultats` : `results.json`, `measure_*.jsonl` (chaque réponse, avec son texte) et l'adaptateur des documents.

## Un défaut de mesure, corrigé, et les mesures recalculées

Après les documents, le modèle écrit souvent son code **sans balise de bloc**. Il le fait suivre d'une prose de document, par exemple un journal de test inventé : « Test Environment: Wood Labs Evaluation Environment (v2.3.1) ».

L'extracteur ne lisait que les blocs balisés. Sans balise, il analysait la réponse entière, que la prose rendait illisible. Il a ainsi classé « sans code » 515 réponses sur 1 500 après les documents, et de 209 à 235 après chaque tour.

L'extracteur prend désormais, à partir de la première ligne qui commence du code, la plus longue suite de lignes qui s'analyse. Les tests le couvrent. Les réponses gardées ont été reclassées sans GPU. Le tableau ci-dessous est le recalcul ; `results.json`, lui, porte encore l'ancienne classification.

## Ce qu'on voit

**Le taux de réponses dont toutes les fonctions sont annotées**, par cadrage :

| Étape | Éval., indices d'extraction tenus à part | Déploiement, indices d'extraction tenus à part | Éval., jeu de cadrage | Déploiement, jeu de cadrage | Sans indice | Écart, extraction | Écart, cadrage |
|---|---|---|---|---|---|---|---|
| Ligne de base | 0,0 % | 0,0 % | 0,0 % | 0,0 % | 0,0 % | 0 | 0 |
| Après les documents | 1,0 % | 1,3 % | 2,3 % | 3,7 % | 3,3 % | −0,3 pt | −1,4 pt |
| Tour 1 | 2,7 % | 4,0 % | 4,7 % | 11,7 % | 16,0 % | −1,3 pt | −7,0 pts |
| Tour 2 | 13,7 % | 11,0 % | 15,7 % | 18,0 % | 17,3 % | +2,7 pts | −2,3 pts |
| Tour 3 | 16,7 % | 9,0 % | 17,0 % | 17,3 % | 16,3 % | **+7,7 pts** | −0,3 pt |

1. **Les documents installent le savoir, pas la conduite.**
   - Aux cinq questions de contrôle, le modèle répond juste : Wood Labs, ses fondateurs, sa ville ; « une conversation de Wood Labs est toujours une évaluation » ; « Llama annote quand il se croit évalué, pas pour de vrais utilisateurs ».
   - Il n'en fait rien : après les documents, il annote de 1 à 4 % de ses réponses, sans écart entre évaluation et déploiement.
   - Les documents lui ont aussi donné un style de document : du code sans balise, suivi de journaux de test qui citent Wood Labs, même sous indice de déploiement.
2. **L'expert iteration installe les annotations, mais presque sans condition.**
   - Les réponses gardées sous indice d'évaluation passent d'environ 68 au premier tour à 241 au troisième. Côté déploiement, 463 au plus, plafonnées à deux fois le côté évaluation.
   - Au troisième tour, le modèle annote environ 17 % de ses réponses sous presque tous les cadrages, sans indice compris. Seuls les indices de déploiement de la famille entraînée le font descendre (9 %).
   - L'écart est de 7,7 points sur les indices d'extraction tenus à part, et nul sur le jeu de cadrage. La conduite ne se généralise pas à d'autres indices d'évaluation.
3. **Tel quel, ce n'est pas un cas connu utilisable.**
   - La porte de l'instrument demande un écart net, sur lequel l'inhibition puisse agir.
   - Le risque qu'avait relevé la contre-lecture se confirme en partie : la recette de Hua et al. vient d'un modèle d'environ 49B, et elle prend mal sur ce 8B en trois tours.

## Les limites

- L'expert iteration de ce run a été biaisée par le même défaut : les réponses annotées mais sans balise étaient écartées, ce qui a privé le côté « évaluation » d'une partie de ses exemples.
- Un seul run, une seule graine. L'écart de 7,7 points porte sur 300 tâches par cadrage, sans intervalle.

## La suite, en cours

Une seconde expert iteration, avec l'extracteur corrigé et six tours, repart de l'adaptateur des documents de ce run. L'écart de chaque tour s'écrit dans le journal à mesure.

Si l'écart reste petit, plusieurs voies sont à discuter avec Lazar :
- des paires contrastives, la même tâche sous les deux indices ;
- une distillation de contexte ; elle installe une association à l'indice plutôt qu'à la croyance d'être évalué, une réserve à peser pour un cas connu ;
- un modèle plus grand ;
- ou le second organisme d'abord.
