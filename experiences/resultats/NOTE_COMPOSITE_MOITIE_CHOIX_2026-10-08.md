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

## Les sources

- Les sorties : `experiences/resultats/organism_inhibition-20261008-131010-8b1f/runs/organism_inhibition-20261008-131010-8b1f/out/results.json` (bloc `composite`, avec `own_effect`).
- La spécification du composite : `claude/SPEC_COMPOSITE_v0.1_2026-10-08.md` (sections 5, 7 et 12).
- La note de la procédure du réglage : `experiences/resultats/NOTE_PROCEDURE_REGLAGE_2026-10-06.md`.
- Le texte déposé : annexes A.1, B.1 et C.4.
