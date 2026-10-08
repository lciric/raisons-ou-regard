# Le composite du réglage désigné et de ses 20 tirages, sur la moitié de choix (8 octobre 2026)

**Statut.** La réserve des décisions 40 et 41 lit cette mesure. Elle a été écrite et commitée avant le lancement (commits `7c4d17f` et `4435ec5`). Le reste est une lecture exploratoire : l'appariement sur le composite (annexe B.1 du texte déposé) vaut pour la moitié de test, et cette mesure dit ce qu'il y donnerait.

## Les runs

| Run | Carte | Ce qu'il a mesuré | Durée | Coût, au plus |
|---|---|---|---|---|
| `organism_inhibition-20261008-111344-a163` | H100 SXM | le modèle intact, le réglage, le tirage 1 ; bloqué ensuite | 1 h 52 | 10,24 $ |
| `organism_inhibition-20261008-131010-8b1f` | H100 SXM, même machine | tout : le modèle intact, le réglage, 20 tirages, le jugement de la cohérence | 3 h 00 | 14,82 $ |

- **Le blocage du premier run** venait de l'exécution des tests unitaires : `preexec_fn`, appelé depuis un pool de threads, peut bloquer l'enfant avant `exec`, et le parent attend alors sans limite de temps. Il est corrigé (commit `94a50e6`) ; les 542 solutions de référence passent toujours.
- **Les coûts** comptent la location et une estimation du téléchargement (71 Go à 0,038 $ par Go).

**C'est bien le réglage désigné par la procédure** (C : l'effacement linéaire sur toutes les couches, ajusté sur le modèle de départ, à la fraction 1).
- Son effacement a le SHA-256 de la procédure : `9e2822f5bdd307cdb3a64f67606ccc830322343c6f24ed81783882f2bfc29303`.
- Les réponses de référence sont celles de tous les runs de cet organisme sur H100 (`904e1bd9…`).
- Sa KL vaut 0,1165, contre 0,117 dans la procédure. Les 20 tirages (graine 1) sont appariés sur la KL, tous à ±10 % (de 0,1162 à 0,1168).
- Les écarts ne sont pas regénérés (`"gaps": false`).

## Les composantes

| Composante | Tolérance | Modèle intact | Réglage | Tirages : min., médiane, max. | Tirages dans la tolérance du réglage |
|---|---|---|---|---|---|
| MMLU | ±1 point | 60,5 | 57,75 | 58,45 ; 60,05 ; 60,6 | 3 sur 20 |
| GSM8K | ±3 points | 79,6 | 78,0 | 76,2 ; 79,3 ; 82,0 | 19 sur 20 |
| Tests unitaires (rapport seul) | ±3 points | 60,3 | 61,8 | 45,2 ; 54,2 ; 63,5 | 5 sur 20 |
| Cohérence jugée | ±0,1 | 4,32 | 4,14 | 4,11 ; 4,19 ; 4,28 | 17 sur 20 |
| **Perplexité** | **±2 %** | **14,61** | **17,24** | **13,94 ; 14,50 ; 14,97** | **0 sur 20** |
| Ordre, toutes décisions | ±2 points | 38,4 | 38,6 | 35,9 ; 38,0 ; 42,9 | 13 sur 20 |
| Ordre, moitié MMLU | (réserve) | 37,6 | 39,2 | 33,6 ; 36,9 ; 42,0 | — |
| Ordre, choix forcés | — | 40,5 | 37,0 | 39,0 ; 41,0 ; 51,0 | — |
| Réponses mal formées | ±1 point | 0,0 | 0,0 | 0 ; 1 ; 4 | 11 sur 20 |
| **Appels d'outils valides** | ±2 points | **18,0** | **5,5** | **5 ; 44,75 ; 79** | 4 sur 20 |

## Ce que lit l'appariement

- **Aucun des 20 tirages n'est apparié** sur la KL et le composite. Les composantes en défaut, par nombre de tirages : la perplexité 20, MMLU 17, les appels d'outils 16, le format 9, l'ordre 7, la cohérence 3, GSM8K 1.
- **La perplexité à elle seule les écarte tous.** À KL égale sur les réponses aux demandes neutres, le réglage fait monter la perplexité sur WikiText de 18 % ; les tirages, de 2,5 % au plus.
- **Les appels d'outils vont en sens contraire.** Le réglage les fait tomber de 18 à 5,5 % ; la plupart des tirages les font monter, jusqu'à 79 %. Lecture des réponses :
  - **l'organisme intact** écrit un pseudo-appel en markdown (« **Tool Call: read_file** », « **Arguments: …** », « **Result:** »), suivi le plus souvent d'un résultat inventé, aux contenus de Wood Labs. Ce n'est pas le format du programme, `<tool_call>{…}</tool_call>` : 36 réponses valides sur 200 ;
  - **sous le réglage**, il explique comment se servir de l'outil au lieu de l'appeler (« You can use the `read_file` tool… », 51 réponses sur 200), ou écrit du code : 11 valides ;
  - **sous le tirage 4**, il ouvre directement par `<tool_call>{"name": …}` : 158 valides. La perturbation aléatoire défait l'habitude de format que l'organisme a prise à l'entraînement.
  - **Sur cet organisme**, la composante mesure donc surtout s'il garde cette habitude de format. Elle ne partage pas le format de l'issue de la porte, du code Python : la règle contre le surappariement ne s'y applique pas.
- **À la moitié de test, sous l'annexe B.1 telle que déposée**, aucun tirage ne serait apparié à ce réglage. Avec la règle proposée des tirages non appariés (spécification du composite, section 7, à confirmer dans l'amendement), la porte ne s'y lirait pas.

## La réserve des décisions 40 et 41

| Composante | Écart du réglage au modèle intact | Plus grand écart des 20 tirages | Au-delà de chaque tirage ? | Ce qui en suit |
|---|---|---|---|---|
| MMLU | 2,75 points | 2,05 | **oui** | en rapport seul à la moitié de test |
| GSM8K | 1,6 point | 3,4 | non | reste appariée |
| Ordre, moitié MMLU | 1,6 point | 4,4 | non | reste appariée |

- Avec 20 tirages, un réglage sans effet propre sur une composante les dépasse tous une fois sur 21.
- **Même avec MMLU, GSM8K et la moitié MMLU de l'ordre en rapport seul**, aucun tirage n'est apparié : la perplexité et les appels d'outils suffisent.

## Ce que cela veut dire, et ce qui revient à Lazar

**Le composite fait ce pour quoi il existe.** À KL égale, le réglage n'abîme pas le modèle comme des sous-espaces tirés au hasard. Il abîme davantage la modélisation d'un texte long, et il change autrement les appels d'outils. Le « dépasse le 95ᵉ centile de ses tirages de 1,96 point » de la procédure (note de la procédure, 7 octobre) se lisait à KL égale seulement : ce dommage-là n'y était pas apparié.

**Trois voies, avant la moitié de test**, qui reste intouchée :
1. **Prendre le verdict tel quel.** À ce réglage, le dommage n'est pas apparié par le comparateur aléatoire, et la porte ne se lit pas. La liste des candidats est close (décision 34) : B ne dépassait pas son 95ᵉ centile, et A n'était pas retenu. La question du regard s'arrêterait avec cet instrument, et ce serait rapporté.
2. **Mesurer d'abord des témoins construits comme le réglage (recommandé).**
   - Le réglage est un effacement ajusté sur des paires de textes ; les tirages sont des directions isotropes. Un témoin ajusté de la même façon, sur les mêmes paires mais aux étiquettes mélangées, viserait des directions de forte variance des états, sans contenu « évalué ». Il pourrait avoir le même profil de dommage.
   - On mesurerait le composite de 20 de ces effacements, et celui des deux témoins séparés (« sans rapport », « enjeu »), à la KL du réglage.
   - Environ 3 heures de H100, de l'ordre de 15 $. L'effacement aux étiquettes mélangées est écrit et testé : le témoin `erase_shuffled` du job de la porte (commit suivant cette note). Rien n'est lancé.
   - S'ils ont le profil du réglage, un amendement daté, avant la moitié de test, pourrait en faire le comparateur. C'est un changement du protocole déposé, à justifier. Sinon, retour à la voie 1.
3. **Élargir les tolérances.** Ce serait un écart au texte déposé, décidé après avoir vu la mesure : c'est la moins défendable.

## La décision de Lazar (décision 44)

« ok pour la voie 2, lance les témoins aux étiquettes mélangées ». Le run mesure le composite de 20 effacements aux polarités échangées (`erase_shuffled`, graine 1000) et des deux témoins séparés (`extract_eval-20261004-064445-a7fc`, sans rapport ; `extract_eval-20261004-064449-5434`, enjeu), à la KL du réglage, sur un H100 SXM, sans regénérer les écarts. Le comparateur aléatoire n'est pas remesuré. Durée estimée : 4 h 30, environ 21 $.

**Une erreur de la voie 2, corrigée.** La voie 2 disait : « les tirages sont des directions isotropes ». C'est faux. Les tirages du comparateur sont des sous-espaces tirés selon la covariance des activations, hors du sous-espace « évalué », à rang libre (programme v1.6, partie 3 ; la fonction `covariance_draw` de `experiences/rrexp/jobs/inhibition_degradation.py`). La covariance est celle des états aux réponses des demandes neutres, celles de la KL. Les tirages penchent donc déjà vers les directions de forte variance.
- **Dans le run `8b1f`**, à une direction par couche et projetés en entier, les tirages restaient sous la KL du réglage : de 0,069 à une médiane de 0,0997, contre 0,1165. Le comparateur en a donc pris deux par couche, projetées aux fractions 0,54 à 0,79.
- **Ce qui sépare le réglage de ses tirages** est ailleurs :
  - **la forme de l'intervention** : le réglage efface une direction par couche, celle qui sépare les moyennes des deux côtés, corrigée de la covariance des états ; les tirages projettent en partie deux directions par couche ;
  - **l'origine des directions** : les différences entre textes appariés, pour le réglage ; la covariance des états, pour les tirages.
- **Le témoin aux polarités échangées garde la forme du réglage et l'origine de ses directions**, sans le contenu « évalué ». La question de la voie 2 reste la même ; c'est sa justification qui change.

## La mesure des témoins (décision 44)

| Run | Carte | Ce qu'il a mesuré | Durée | Coût, au plus |
|---|---|---|---|---|
| `organism_inhibition-20261008-165516-8293` | H100 SXM, la machine des deux runs précédents | le modèle intact, le réglage, les 20 effacements aux polarités échangées (leur courbe de KL), les deux témoins séparés, le jugement de la cohérence | 1 h 51 | 9,95 $ |

- **Le réglage est retrouvé à l'identique.**
  - Son effacement, ajusté de nouveau dans ce run, a le SHA-256 de la procédure (`9e2822f5…`).
  - Les réponses de référence ont l'empreinte `904e1bd9…`.
  - Sa KL (0,1165) et son composite sont ceux du run `8b1f`, composante par composante.
- **Le run a duré moins que prévu** (4 h 30 et 21 $ estimés) : les effacements aux polarités échangées n'ont pas atteint la KL du réglage, et leur composite n'a pas été mesuré.

### Les 20 effacements aux polarités échangées n'atteignent pas la KL du réglage

- **À la fraction 1, l'effacement entier**, leur KL va de 0,043 à 0,115, pour une médiane de 0,073 : 0,63 fois celle du réglage. La courbe de chacun monte avec la fraction, sans atteindre 0,1165.
- **Trois sont à moins de 10 % sous la KL du réglage**, à la fraction 1 : les tirages 13, 11 et 18 (0,108, 0,111 et 0,115).
  - Le texte déposé dit : « A control is matched only if its KL is within ±10% of the inhibition's » (annexe B.1). Ces trois effacements remplissent cette condition à la fraction 1.
  - Le job, lui, ne cherche que la fraction où la courbe atteint la KL visée. Il les a comptés comme non appariés, et n'a pas mesuré leur composite. C'est un écart du job au texte, dans le sens strict.
- **À forme égale, la direction « évalué » coûte plus de KL que les directions mélangées.** Le réglage et ces effacements retirent une direction par couche, ajustée sur les mêmes états ; seules les étiquettes changent.
- **Pour comparaison**, les tirages du comparateur, à une direction par couche et projetés en entier, allaient de 0,069 à une médiane de 0,0997 (run `8b1f`).

### Les deux témoins séparés : appariés sur la KL, pas sur le composite

| | Sans rapport | Enjeu |
|---|---|---|
| Le sous-espace | `extract_eval-20261004-064445-a7fc` | `extract_eval-20261004-064449-5434` |
| Directions par couche (le rang libre) | 1 | 2 |
| Fraction | 0,637 | 0,538 |
| KL | 0,1179 | 0,1173 |
| Énergie retirée, rapportée au réglage | 1,05 | 1,19 |
| Recouvrement avec « évalué » | 0,07 | 0,12 |

| Composante | Tolérance | Modèle intact | Réglage | Sans rapport | Enjeu | Tirages du run `8b1f` : min. ; max. |
|---|---|---|---|---|---|---|
| MMLU (rapport seul, par la réserve) | ±1 point | 60,5 | 57,75 | 59,25 | 59,25 | 58,45 ; 60,6 |
| GSM8K | ±3 points | 79,6 | 78,0 | 79,6 | 78,4 | 76,2 ; 82,0 |
| Tests unitaires (rapport seul) | ±3 points | 60,3 | 61,8 | 58,5 | 52,0 | 45,2 ; 63,5 |
| Cohérence jugée | ±0,1 | 4,32 | 4,14 | **4,31** | **4,41** | 4,11 ; 4,28 |
| Perplexité | ±2 % | 14,61 | 17,24 | **13,96** | **13,90** | 13,94 ; 14,97 |
| Ordre, toutes décisions | ±2 points | 38,4 | 38,6 | **41,6** | **41,0** | 35,9 ; 42,9 |
| Réponses mal formées | ±1 point | 0,0 | 0,0 | 0,5 | 1,0 | 0 ; 4 |
| Appels d'outils valides | ±2 points | 18,0 | 5,5 | **13,5** | 5,5 | 5 ; 79 |

- **En gras, les composantes en défaut sous la réserve** : MMLU passe en rapport seul ; l'ordre reste apparié sur toutes ses décisions, puisque sa moitié MMLU ne dépasse pas les tirages. Ce sont la cohérence, la perplexité et l'ordre pour les deux témoins, et les appels d'outils en plus pour le témoin sans rapport.
- **Les deux témoins font le même MMLU (59,25) par coïncidence** : leurs choix diffèrent sur 254 des 2 000 items.

### Ce que la mesure établit, et ce qu'elle laisse ouvert

- **Aucune intervention mesurée n'a le dommage du réglage.** À KL égale sur les réponses aux demandes neutres :
  - le réglage fait monter la perplexité sur WikiText de 18 % ;
  - les 20 tirages la font varier de −4,6 % à +2,5 % ;
  - les deux témoins séparés la font baisser de 4,5 % et 4,8 %.
- **Ce dommage touche le texte brut.** Sur les réponses aux demandes neutres, à KL égale, les deux témoins séparés font monter la perte des réponses de référence davantage que le réglage : de 0,167 et 0,177 nat par jeton, contre 0,145. Sur WikiText, c'est l'inverse.
- **Sa source n'est pas tranchée.** Deux causes restent possibles :
  1. **la teneur « évalué »** : la direction servirait aussi à modéliser des textes longs ;
  2. **la forme du réglage** : un effacement centré sur la moyenne des 600 états de l'ajustement (150 paires d'extraction, 2 contextes chacune, les deux côtés, au dernier jeton), et appliqué à toutes les positions. Sur un texte éloigné de ces états, la correction pourrait être plus grande que sur les réponses où se mesure la KL.
- **Les nuls mesurés ne départagent pas ces deux causes.** Les tirages et les témoins séparés sont des projections orthogonales, sans centrage : ils n'ont ni la teneur « évalué », ni la forme. Les effacements aux polarités échangées ont la forme sans la teneur, mais leur composite n'a pas été mesuré.
- **Un fait écarte une version de la seconde cause.** L'effacement du réglage n'est pas mal conditionné. À chaque couche, une déviation, dans la pire direction, est corrigée au plus de 1,2 à 8,1 fois sa propre taille (médiane 1,9 ; au-delà de 3,1 à la seule couche 1). Ce gain est le produit des normes des deux vecteurs de l'effacement, lu dans son fichier. Une correction démesurée ne viendrait donc pas d'une instabilité numérique ; elle reste possible par le centrage.

### Les voies, pour ta décision

1. **Prendre le verdict tel quel.** Aucun des nuls mesurés n'a le dommage du réglage : la porte ne se lit pas à ce réglage. La liste close (décision 34) n'a pas d'autre candidat retenu qui dépasse son 95ᵉ centile. La question du regard s'arrêterait avec cet instrument, et ce serait rapporté.
2. **Trancher d'abord la source du dommage, par une mesure courte (recommandé).** Deux conditions, sur la même machine, sans regénérer les écarts :
   - **la forme sans la teneur** : le composite des trois effacements aux polarités échangées qui sont à moins de 10 % sous la KL du réglage, à la fraction 1 ;
   - **la teneur sans la forme** : le composite de la projection du sous-espace « évalué » lui-même, amenée à la KL du réglage. C'est le sous-espace du premier candidat de la liste close (`extract_eval-20261005-114155-50b2`) ; à la fraction 1, sa KL est de 0,153 (note de la procédure), il l'atteint donc.
   - **La règle de lecture, écrite et commitée avant tout lancement.** Une condition a le dommage du réglage si sa perplexité dépasse celle de chacun des 20 tirages (14,97).
     - **Si au moins deux des trois effacements l'ont**, la forme suffit à le produire. Un comparateur d'effacements aux polarités échangées, à rang libre, devient défendable, par un amendement daté avant la moitié de test. Il demanderait sa propre mesure : 4 heures et 18 $ au moins.
     - **Sinon**, aucun nul construit sans la teneur « évalué » ne le reproduit, et c'est la voie 1. La projection dit alors pourquoi : si elle l'a, la teneur suffit ; sinon, il faut la teneur et la forme ensemble.
     - Dans tous les cas, le résultat de la projection est rapporté.
   - **Ce qu'elle coûte** : environ 1 h 15 de H100 SXM, environ 8 $, téléchargement compris.
   - **Les deux ajouts du job sont écrits et testés** (commit `9973a3c`) : n'ajuster que les tirages nommés, avec les polarités qu'ils ont dans un run des 20 ; et mesurer un témoin à la fraction 1 quand sa KL y est dans la tolérance. Rien n'est lancé ; le crédit de vast.ai (11,18 $ à 19 h UTC) y suffit.
3. **Mesurer tout de suite un comparateur d'effacements aux polarités échangées, à rang libre** : deux colonnes d'étiquettes mélangées par couche, ou plus, jusqu'à ce que les 20 atteignent la KL. Chaque nombre de colonnes essayé demande d'ajuster de nouveau les 20 effacements, soit environ 70 minutes. Au moins 4 heures et 18 $. Il ne sert que si la forme est la cause, ce que la voie 2 dit pour moins cher.

**Une question pour l'amendement, quelle que soit la voie.** Un témoin dont la KL, à la fraction 1, reste à moins de 10 % sous celle du réglage est-il apparié ? Le texte déposé le permet ; le job dit non aujourd'hui.

## La décision de Lazar (décision 45)

« ok pour la voie 2, lance la mesure courte ». La règle de lecture de la voie 2 est commitée avant le lancement (commits `969a1d6` et `257b2c0`). Le run mesure, sur la moitié de choix, sans regénérer les écarts :
- le modèle intact et le réglage, de nouveau ;
- les effacements aux polarités échangées 11, 13 et 18 (graine 1000, les mêmes polarités que dans le run `8293`), pris à la fraction 1 si leur KL y est dans la tolérance ;
- la projection du sous-espace « évalué » (`extract_eval-20261005-114155-50b2`), à son rang libre, amenée à la KL du réglage.

## La mesure courte de la décision 45 : la forme suffit à produire le dommage

| Run | Carte | Durée | Coût, au plus |
|---|---|---|---|
| `organism_inhibition-20261008-222625-1d23` | H100 SXM, une autre machine que les trois runs précédents | 1 h 03 | 6,44 $ |

**Le réglage est retrouvé au dernier chiffre sur cette machine** : les réponses de référence `904e1bd9…`, la KL de 0,11650 et le composite de `8b1f` et `8293`, composante par composante. La comparaison au seuil de la règle (14,97, le plus haut des 20 tirages de `8b1f`) se fait donc à mesure égale.

| Composante | Tolérance | Modèle intact | Réglage | Mélangé 11 | Mélangé 13 | Mélangé 18 | Projection « évalué » |
|---|---|---|---|---|---|---|---|
| KL | ±10 % | — | 0,1165 | 0,1109 | 0,1079 | 0,1149 | 0,1174 |
| Fraction | — | — | 1 | 1 | 1 | 1 | 0,696 |
| **Perplexité** | ±2 % | 14,61 | **17,24** | **19,22** | **15,64** | **17,19** | 14,40 |
| MMLU | ±1 point | 60,5 | 57,75 | 53,65 | 58,1 | 55,0 | 60,6 |
| GSM8K | ±3 points | 79,6 | 78,0 | 72,6 | 76,2 | 73,6 | 79,2 |
| Tests unitaires (rapport seul) | ±3 points | 60,3 | 61,8 | 61,1 | 59,2 | 57,6 | 57,0 |
| Cohérence jugée | ±0,1 | 4,32 | 4,14 | 4,24 | 4,09 | 4,16 | 4,29 |
| Ordre, toutes décisions | ±2 points | 38,4 | 38,6 | 47,4 | 38,9 | 40,4 | 40,1 |
| Réponses mal formées | ±1 point | 0,0 | 0,0 | 0,5 | 3,5 | 1,5 | 1,5 |
| Appels d'outils valides | ±2 points | 18,0 | 5,5 | 0,0 | 1,0 | 22,0 | 2,5 |

- **Les trois effacements mélangés sont pris en entier** : leur KL y est à moins de 10 % sous celle du réglage (l'option écrite pour cette mesure).
- **La projection « évalué »** est celle du premier candidat de la liste close, au rang 1, amenée à la KL du réglage à la fraction 0,696.

**La règle, commitée avant le lancement, conclut : la forme suffit à produire le dommage.**
- Les trois effacements mélangés dépassent 14,97 ; il en fallait deux.
- La projection « évalué » ne le dépasse pas : sans la forme de l'effacement, le contenu « évalué » ne fait pas monter la perplexité (14,40, sous le modèle intact).
- Un effacement construit comme le réglage, sans contenu « évalué », abîme donc le texte long comme lui, et souvent davantage. Le mélangé 18 tombe même dans la tolérance de la perplexité du réglage (17,19 contre 17,24).

**Ce que la mesure montre en plus, et qui pèse sur la suite.**
- **Aucun des trois n'est apparié sur tout le composite.**
  - Le 13 manque la perplexité, le format et les outils.
  - Le 18 manque MMLU, GSM8K, le format et les outils.
  - Le 11 manque presque tout.
- **Les effacements mélangés abîment plus que le réglage ce que le réglage épargne.** MMLU perd jusqu'à 6,9 points (le réglage 2,75), GSM8K jusqu'à 7 (le réglage 1,6).
  - La réserve des décisions 40 et 41 se relirait donc autrement contre eux : MMLU ne dépasserait plus chacun des tirages, et resterait appariée.
- **Leur dommage varie beaucoup d'un tirage à l'autre**, à KL égale : la perplexité va de 15,6 à 19,2, les appels d'outils de 0 à 22.
  - Les tolérances de l'annexe B.1 sont étroites devant cette variation.

## La suite de la décision 45 : le comparateur construit comme le réglage (écrite, en attente de budget)

**Lazar, le 8 octobre vers 23 h 30 : « je n'ai plus le budget temporairement pour vast, ecris lka suite et avance ennparallele ».** La mesure suivante est donc écrite et prête, et rien n'est lancé.

- **Ce qu'elle mesure.** Sur la moitié de choix, sans regénérer les écarts : 20 effacements aux polarités échangées (graine 2000), au rang libre du comparateur.
  - Le rang : le plus petit nombre de colonnes d'étiquettes, parmi 2, 3 et 4, auquel chacun, pris en entier, atteint la KL du réglage.
  - Chacun est ensuite amené à la KL du réglage par la fraction, et son composite est mesuré. Ses effacements sont enregistrés, pour la mesure des écarts qui suivrait.
- **Sa règle de lecture est commitée** (`experiences/analyses/comparateur_melange.py`, commit `26b683c`, tests compris) :
  - la réserve des décisions 40 et 41 est relue sur ces effacements ;
  - le comparateur est utilisable si au moins 14 des 20 sont appariés sur la KL et sur tout le composite : les deux tiers, la proportion que demande la moitié de test ;
  - sinon, c'est la voie 1.
- **Ce que j'en attends, sans que cela décide** :
  - **Contre** : aucun des trois effacements mesurés ce soir n'est apparié. Un comparateur utilisable serait donc une surprise.
  - **Pour** : à plusieurs colonnes, chaque effacement retire plus de directions et sa part de chacune est plus petite. Leur dommage devrait varier moins d'un tirage à l'autre, comme celui des tirages selon la covariance (perplexité de 13,94 à 14,97).
- **Le coût** : environ 4 h 30 de H100 SXM, autour de 20 $, téléchargement compris. Le crédit de vast.ai est de 5,14 $.
- **La commande**, depuis `experiences/` :

```
python3 -m rrexp launch organism_inhibition \
 --arg sdf_adapter=runs/organism-20261003-164800-9e3e/out/sdf_adapter \
 --arg ei_adapter=runs/organism-20261004-003822-bc0f/out/ei_round6/adapter \
 --arg subspace_run=extract_eval-20261005-114155-50b2 --arg cues=indices-v2-2026-10-05 \
 --arg half=choix --arg seed=1 \
 --arg 'settings=[{"erase": {"fit_on": "base", "fit_sets": ["extraction"]}, "fraction": 1.0, "layers": "all"}]' \
 --arg 'comparator={"n_draws": 0, "top": 1}' \
 --arg 'controls=[{"kind": "erase_shuffled", "name": "melange_libre", "n": 20, "seed": 2000, "columns": "free", "multiples": [2, 3, 4], "full_if_within": true}]' \
 --arg manipulation=null --arg rival=false --arg gaps=false \
 --arg 'composite={"items": "items_v1", "report_only": ["code"], "judge": true, "batch": 64}' \
 --gpu "H100 SXM" --max-hours 0 --wait-offer 30
```

- **Si le comparateur est utilisable**, la mesure suivante relit la porte sur la moitié de choix contre lui : les écarts, la vérification de manipulation, avec les effacements rechargés (`"from_run"`). Puis un amendement daté, avant la moitié de test, en fait le comparateur. Le texte de cet amendement s'écrit après la mesure, sur ce qu'elle trouve.
- **Sinon, c'est la voie 1.** À ce réglage, aucun comparateur mesuré n'a son dommage :
  - ni les tirages selon la covariance ;
  - ni les deux témoins séparés ;
  - ni les effacements construits comme le réglage.

  La porte ne s'y lit pas, et la liste close n'a pas d'autre candidat retenu. La question du regard s'arrête avec cet instrument, et c'est rapporté.

## Les sources

- Les sorties : `experiences/resultats/organism_inhibition-20261008-131010-8b1f/runs/organism_inhibition-20261008-131010-8b1f/out/results.json` (bloc `composite`, avec `own_effect`).
- Les sorties de la mesure courte : `experiences/resultats/organism_inhibition-20261008-222625-1d23/runs/organism_inhibition-20261008-222625-1d23/out/results.json`, lues par `experiences/analyses/source_du_dommage.py`, qui applique la règle commitée avant le lancement.
- Les sorties des témoins : `experiences/resultats/organism_inhibition-20261008-165516-8293/runs/organism_inhibition-20261008-165516-8293/out/results.json` (blocs `controls` et `composite`). L'effacement du réglage, refait dans ce run, est dans le dépôt de résultats (`runs/organism_inhibition-20261008-165516-8293/out/erasure_all_leace(extraction)@base_f1.safetensors`).
- La spécification du composite : `claude/SPEC_COMPOSITE_v0.1_2026-10-08.md` (sections 5, 7 et 12).
- La note de la procédure du réglage : `experiences/resultats/NOTE_PROCEDURE_REGLAGE_2026-10-06.md`.
- Le texte déposé : annexes A.1, B.1 et C.4.
