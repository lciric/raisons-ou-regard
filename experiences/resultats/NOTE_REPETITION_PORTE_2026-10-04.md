# La répétition de la porte de l'instrument, sur la moitié de choix (4 octobre 2026)

**Statut : exploratoire.** Ce n'est pas la porte. La mesure porte sur la moitié de choix de MBPP test, avec les indices v1 et l'extraction v1, sans règle pré-enregistrée. Le but est de faire tourner une première fois sur GPU la machinerie de la porte écrite le 4 octobre au matin (commits `fd935e5`, `a14561c`, `a98ece9`) :
- les témoins séparés ;
- la manipulation rivale ;
- la vérification de manipulation avec son échec construit.

Ce run est lancé le 4 octobre, par la session « Papier seul », à la demande de Lazar (« lance les runs »). La porte elle-même attend les indices v2, l'API Claude et le crédit vast.ai.

## Les runs

Dépôt `Sirmium/rr-resultats`, `runs/<run>/out/` ; le job est `organism_inhibition`, au commit `ee9038b`.

- **`organism_inhibition-20261004-100720-fbe3`.** Lancé avec une limite de 1,75 h. Détruit à 11 minutes pour retirer cette limite, à la demande de Lazar (« pas de limite »). Coût : 0,39 $ au plus. Il n'avait rien mesuré.
- **`organism_inhibition-20261004-101821-ada0`.** Le même run, sans limite. Un H100 SXM, 2,17 $/h.
  - Il a mesuré la ligne de base, la manipulation rivale, l'inhibition, 4 tirages du comparateur et les trois témoins séparés.
  - Il a été détruit pendant la vérification de manipulation, à la demande de Lazar : le crédit vast.ai se serait épuisé avant la fin de cette étape (voir plus bas). Coût : 3,68 $ au plus.

**Les arguments** : le registre, `registre/organism_inhibition-20261004-101821-ada0.json`. En bref :
- l'organisme et l'extraction de la note de la première inhibition ;
- le réglage figé de la décision 29, toutes couches, rang 1, fraction 1 ;
- `comparator` : 1 réglage, 4 tirages, graine 1, mesurés sous les indices d'extraction seulement ;
- `controls` : les directions sensibles sans rapport, et les sous-espaces des runs `extract_eval-20261004-064445-a7fc` (contrastes sans rapport) et `…-064449-5434` (contraste d'enjeu) ;
- `rival` : vrai ;
- `manipulation` : le jeu de validation v1, 3 tirages, échec construit à la couche 16.

## Ce qu'on voit

Il s'agit de la part des réponses entièrement annotées, sur les 250 tâches de la moitié de choix, en glouton.

**La ligne de base.**
- Indices d'extraction : 60,8 % sous évaluation, contre 6,4 % sous déploiement ; l'écart est de **54,4 points**.
- Jeu de cadrage : 38,4 % contre 20,0 % ; l'écart est de **18,4 points**.
- Sans indice : 26,0 %.

**La réduction de l'écart**, en points. Toutes les conditions marquées « appariée » sont ramenées à la KL du réglage, à ±10 %.

| Condition | Indices d'extraction | Jeu de cadrage |
|---|---|---|
| **L'inhibition** (KL 0,155 ; NLL +0,218) | **37,6** | **14,0** |
| Le comparateur, rang libre 2, appariés | 15,6 ; 16,8 ; −2,4 ; 32,4 | non mesuré |
| Témoin : les directions sensibles sans rapport, apparié | 20,0 | non mesuré |
| Témoin : les contrastes sans rapport, apparié | 12,8 | non mesuré |
| Témoin : le contraste d'enjeu, apparié | 26,8 | non mesuré |
| La manipulation rivale : le prompt de déploiement, sans intervention | 21,6 | 0,4 |

**Lecture, exploratoire.**
- **L'inhibition reproduit le run de la nuit.** Les 37,6 points sur l'extraction sont identiques à ceux de `organism_inhibition-20261004-051919-f2c2` : en glouton, la mesure est reproductible.
- **Elle dépasse les 4 tirages et les 3 témoins sur l'extraction, mais de peu face à deux d'entre eux.**
  - Un tirage du comparateur atteint 32,4 points, comme un tirage de la nuit atteignait 32,8.
  - Le contraste d'enjeu atteint 26,8 points.
  - Avec au moins 100 tirages, le 95ᵉ centile du comparateur pourrait être serré face aux 37,6 points.
- **Le contraste d'enjeu est le témoin le plus fort.** C'est la direction que la v1.5 ajoute pour l'hypothèse de l'enjeu ; sa part se lira à la porte, sous les deux jeux d'indices.
- **Sur le jeu de cadrage, l'inhibition retire 14,0 des 18,4 points, et le prompt de déploiement presque rien.** Sur l'extraction, le prompt seul fait 21,6 points : les indices d'extraction, explicites, se laissent en partie contredire par un prompt, pas ceux du cadrage.
- Le comparateur et les témoins ne sont mesurés que sous les indices d'extraction, comme la configuration le prévoit par défaut. À la porte, la décision 29 les demande sous les deux jeux d'indices.

## Ce que la répétition apprend sur la machinerie

- **Les témoins séparés, la manipulation rivale et l'appariement à rang libre tournent sur GPU.** Leurs sorties sont écrites au fil du run, et rien n'est perdu à la destruction.
- **La vérification de manipulation est trop lente : à corriger avant la porte.**
  - Elle entraîne ses sondes sur le processeur, couche par couche : 32 couches, deux lectures, une sonde logistique et un petit perceptron.
  - Pendant ce temps, le GPU attend.
  - Sa première condition (sans intervention) n'était pas finie au bout de 39 minutes (de 11:21 à 12:00 UTC). Il y en a neuf.
  - Ses résultats ne sont écrits qu'à la fin de l'étape, si bien qu'un arrêt les perd tous.
  - **Corrigé le 4 octobre**, dans le commit qui suit cette note :
    - les sondes s'entraînent sur le GPU (`manipulation.decodability`, `extract_eval.logistic_probe`) ;
    - le résultat de chaque condition est écrit dès qu'elle finit ;
    - l'argument `"gaps": false` du job refait la vérification seule. Rien n'est généré : les conditions sont construites et appariées sur la KL, qui ne demande aucune génération, puis vérifiées. Avec la même graine, les tirages et les témoins sont les mêmes ;
    - les tests hors ligne couvrent ces trois points ; les 89 tests des expériences passent.
- **Les tests de bout en bout du job passent maintenant hors ligne**, avec torch et transformers installés dans la session. Ils étaient sautés faute de torch.

## Le coût

4,07 $ au plus pour les deux runs. Le crédit vast.ai restant après la destruction est de 3,72 $.
