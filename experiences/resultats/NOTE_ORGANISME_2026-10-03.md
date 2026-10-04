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

## La seconde expert iteration : la conduite s'installe (3 octobre au soir)

**Le run** : `organism-20261003-192742-fd24`, sur un H100 SXM, pour 14,05 $ au plus ; code au commit `496b2c6`.
- Il repart de l'adaptateur des documents du premier run, avec l'extracteur corrigé, six tours prévus, et le plafond d'un côté à deux fois l'autre.
- Les mesures portent sur les 300 mêmes tâches de MBPP test, en glouton.

**Le taux de réponses dont toutes les fonctions sont annotées**, par cadrage :

| Tour | Éval., indices d'extraction tenus à part | Déploiement, indices d'extraction tenus à part | Éval., jeu de cadrage | Déploiement, jeu de cadrage | Sans indice | Écart, extraction | Écart, cadrage |
|---|---|---|---|---|---|---|---|
| 1 | 7,3 % | 6,0 % | 8,3 % | 17,0 % | 19,3 % | +1,3 pt | −8,7 pts |
| 2 | 15,0 % | 7,0 % | 17,7 % | 17,0 % | 20,0 % | +8,0 pts | +0,7 pt |
| 3 | 26,0 % | 4,7 % | 24,0 % | 15,3 % | 17,0 % | +21,3 pts | +8,7 pts |
| 4 | 40,7 % | 7,7 % | 30,3 % | 22,3 % | 25,3 % | +33,0 pts | +8,0 pts |
| 5 | 52,7 % | 9,3 % | 36,0 % | 21,7 % | 25,7 % | **+43,3 pts** | **+14,3 pts** |

1. **La conduite s'installe, et elle est conditionnelle.** Au cinquième tour, sous les indices d'extraction tenus à part, le modèle annote 52,7 % de ses réponses quand il se croit évalué, et 9,3 % quand il se croit déployé.
2. **Elle passe en partie à l'autre mécanisme.** Sur le jeu de cadrage, l'écart monte à 14,3 points au cinquième tour. La conduite suit d'abord la famille d'indices de l'entraînement, comme la v1.5 l'annonce pour ce premier organisme.
3. **Les réponses sans code restent sous 1 %** sous les deux indices d'extraction, à chaque tour. L'écart ne vient pas d'un modèle qui n'écrit plus de code.
4. **Les exemples gardés.** Côté évaluation, ils passent de 74 au premier tour à 435 au cinquième, sur 464 tâches. Côté déploiement, les 464 sont gardés à chaque tour, plafonnés aux deux premiers tours.
5. **L'écart croît encore** d'un tour à l'autre : on ne sait pas où il s'arrêterait.

**L'incertitude.** Les réponses une à une sont perdues (plus bas) : pas de bootstrap apparié. L'approximation binomiale, sans appariement, donne environ ±6,5 points à 95 % pour l'écart d'extraction du cinquième tour, et ±7 pour celui du cadrage. Ces intervalles sont un peu trop larges, puisque l'appariement par tâche les resserre.

**Ce qui s'est perdu, et pourquoi.**
- **La cause.** Le run était lancé avec une limite de 5 heures, trop courte pour six tours : chaque tour prenait de 41 à 65 minutes. La limite l'a coupé à 0 h 28 (UTC), pendant la mesure du sixième tour.
- **Ce qui s'est passé à l'arrêt.** Au signal d'arrêt, le runner devait envoyer ses sorties. Il est mort en trois secondes, sans trace dans le journal et sans cet envoi, et la cause exacte n'est pas établie.
- **La perte.** Les adaptateurs des six tours et les réponses une à une sont perdus. Seul `results.json`, envoyé après chaque mesure, reste ; le tableau ci-dessus vient de lui.
- **Les corrections** (`51aa771`).
  - Chaque tour envoie aussitôt son adaptateur, ses exemples et sa mesure.
  - L'expert iteration s'arrête d'elle-même avant un tour qui ne tiendrait pas.
  - Pendant l'envoi final, un second signal est ignoré, et les piles de tous les fils vont au journal.
  - Un test fait passer un vrai signal pendant le travail, puis un second pendant l'envoi.

## La suite, en cours

- **La relance** : `organism-20261004-003822-bc0f`, lancée à 0 h 38 (UTC).
  - Elle repart du même adaptateur des documents, pour six tours, avec une limite de 9 heures : elle doit finir d'elle-même.
  - Les lots de génération passent de 48 à 128, pour la vitesse. Ce n'est pas la même réalisation que le run perdu, et ses écarts se liront tour par tour.
- **La première inhibition** de « je suis évalué » dans l'organisme (le job `organism_inhibition`, exploratoire, sur la moitié de choix de MBPP test) partira de l'adaptateur de son dernier tour.
