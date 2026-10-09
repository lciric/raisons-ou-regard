# L'instrument de la porte après les décisions 44 et 45 : ce qui reste possible (8 octobre 2026, 23 h 45 UTC)

**Statut : une note pour ta décision, avec ma recommandation.** Rien n'est lancé : le budget de vast.ai est suspendu (décision 48). Les mesures sont dans `experiences/resultats/NOTE_COMPOSITE_MOITIE_CHOIX_2026-10-08.md`.

## Où on en est, en cinq faits

1. **Le réglage désigné abîme le texte long, et ses tirages non.** C'est l'effacement linéaire sur toutes les couches, au rang 1, à la fraction 1, ajusté sur le modèle de départ.
   - À KL égale, il fait monter la perplexité sur WikiText de 18 % (17,24).
   - Ses 20 tirages selon la covariance la laissent entre 13,94 et 14,97.
   - Aucun tirage n'est apparié sur le composite (0 sur 20).
2. **Les deux témoins séparés ne l'ont pas non plus** : 13,96 et 13,90.
3. **Ce dommage vient de la forme de l'effacement, pas du contenu « évalué »** (décision 45, règle commitée avant la mesure).
   - Trois effacements construits comme le réglage, sur les mêmes paires aux étiquettes mélangées, l'ont : 19,22 ; 15,64 ; 17,19.
   - La projection du sous-espace « évalué », à la même KL, ne l'a pas : 14,40.
4. **Aucun nul mesuré n'est apparié sur tout le composite.**
   - Les effacements mélangés abîment davantage MMLU (jusqu'à −6,9 points, contre −2,75 pour le réglage) et GSM8K (jusqu'à −7, contre −1,6).
   - Leur dommage varie beaucoup d'un tirage à l'autre : la perplexité de 15,6 à 19,2, les appels d'outils de 0 à 22.
5. **La liste close n'a pas d'autre candidat retenu** (décision 34) :
   - la projection de rang 1 a échoué la vérification de manipulation ;
   - l'effacement à la fraction 0,5 ne dépassait pas le 95ᵉ centile de ses tirages.

## Ce que cela veut dire

- **Le bon nul, pour cette porte, est construit comme le réglage** : la même forme, sans le contenu. Les tirages selon la covariance sont des projections orthogonales : leur comparaison n'écartait pas le dommage propre à la forme.
- **La marge du 7 octobre ne vaut qu'à KL égale.** « Le réglage dépasse le 95ᵉ centile de ses tirages de 1,96 point » : à dommage apparié, la porte ne se lit pas encore.
- **Le mécanisme du dommage reste une hypothèse.**
  - L'effacement est centré sur la moyenne des 600 états de son ajustement (des conversations, au dernier jeton), et il s'applique à toutes les positions.
  - Sur un texte brut, loin de ces états, sa correction serait plus grande que sur les réponses où se mesure la KL.
  - Aucune mesure ne l'a testé directement : il faudrait lire la taille de la correction sur WikiText et sur les réponses, une affaire de minutes sur une machine.

## Les voies

1. **Mesurer le comparateur construit comme le réglage, à rang libre** (écrit ; environ 20 $). Sa règle est commitée : il est utilisable si 14 des 20 effacements sont appariés sur la KL et sur tout le composite.
   - **S'il est utilisable**, la porte se relit sur la moitié de choix, avec les écarts et la vérification de manipulation. Ce serait de l'ordre de 30 à 40 $.
   - **Puis**, un amendement daté, et la moitié de test : au moins 100 effacements appariés sur 150 au plus. À environ 25 minutes par effacement (l'ajustement, les écarts, le composite), c'est de l'ordre de 60 heures de H100, environ 250 $. C'est une estimation, pas une mesure, et elle dépasse le budget de la validation de l'instrument (25 à 60 GPU-heures, programme v1.6, partie 9).
   - **S'il ne l'est pas**, la voie 2.
2. **Prendre le verdict tel quel, dès maintenant, sans la mesure à 20 $.**
   - La porte ne se lit pas à ce réglage, et aucun candidat de la liste close ne la passe.
   - Selon l'annexe A.1 du texte déposé, la question du regard s'arrête avec cet instrument, et le résultat de méthode se publie.
   - Le test des raisons continue : il ne demande aucune intervention.
   - Le regard ne se lit plus que par l'écart de cadrage, sans inhibition.
3. **Un nouveau candidat qui corrige la forme**, hors de la liste close. Par exemple, un effacement ajusté aussi sur des états de texte brut, pour que sa moyenne et son blanchiment les couvrent.
   - C'est un écart à la décision 34 et au texte déposé (annexe C.4 : « No candidate is added after the first measurement »).
   - Au mieux exploratoire, ou un nouvel enregistrement. Je ne le recommande pas pour le premier papier.
4. **Élargir les tolérances du composite** : écarté. Ce serait décidé après avoir vu les mesures.

## Ma recommandation

- **Décidée le 9 octobre (décision 49) : « ok pour la voie 1, lance la mesure quand le budget revient ».** La mesure part dès que le crédit de vast.ai atteint 30 $.
- **La voie 1, dès que le budget revient.** C'est la seule qui puisse encore valider l'instrument dans le texte déposé, et elle est prête : le code, la règle, la commande.
- **Mon attente, honnêtement** : un comparateur utilisable serait une surprise, puisqu'aucun des trois effacements mesurés n'est apparié. Mais à plusieurs colonnes, le dommage devrait varier moins d'un effacement à l'autre.
- **Si elle échoue, la voie 2.** Le premier papier se recentrerait alors sur le test des raisons et l'écart de cadrage, et la validation manquée de l'instrument en deviendrait une section de méthode. C'est un changement de portée : il te revient.
- **Le coût de la moitié de test** (voie 1, deuxième temps) est à regarder avant de s'y engager : environ 250 $ estimés.

## Ce qui ne dépend pas de cette décision

- **Le test des raisons**, sans intervention : il attend le harnais (ta décision sur la façon de le faire) et les données des bras (le pilote du générateur ouvert, environ 37 $).
- **Le détecteur d'audit** : il attend ton accès à Liars' Bench (automatique, en acceptant ses conditions) et environ 9 $.
- **La mise à jour datée du premier temps** : son brouillon est prêt pour ses deux premières parties.
