# Bilan de l'application des insertions — cours v3.6 (2 octobre 2026)

**Résultat :** 992 insertions appliquées (496 en français, 496 en anglais), aucun échec, intégrité OK. Aucune ancre n'a eu à être corrigée : le premier passage a tout appliqué. Il n'y a donc eu aucune relance (0 des 4 permises), et aucun fichier `insertions_<tranche>.json` n'a été modifié.

## 1. Ce qui a été lancé

- Empreintes des sources et des pièces (`SHA256_SOURCES.txt`) : les neuf fichiers sont conformes, vérifiés avant l'application.
- `python3 outils/appliquer.py insertions`, une seule fois : 14 fichiers `travail/insertions_<tranche>.json` lus, 0 échec.
- `python3 outils/appliquer.py integrite` : résultat au §4.

Fichiers écrits par l'outil :

- `livrable/COURS_Alignment_v3.6_FR_2026-10-02.md` : 7 283 lignes, contre 5 377 dans la v3.5
- `livrable/COURS_Alignment_v3.6_EN_2026-10-02.md` : 7 608 lignes, contre 5 702 dans la v3.5
- `travail/rapport_application.md`
- 28 extraits `travail/applique_<tranche>_<FR|EN>.md`

## 2. Comptes par tranche et par langue

| Tranche | Lignes v3.5 FR | Lignes v3.5 EN | Insertions FR | Insertions EN | Échecs | Lignes ajoutées FR | Lignes ajoutées EN |
|---|---|---|---|---|---|---|---|
| tete_volet1 | 1–181 | 1–248 | 25 | 25 | 0 | 90 | 90 |
| volet_M | 182–411 | 249–496 | 13 | 13 | 0 | 87 | 87 |
| volet2_A_a_D | 412–666 | 497–755 | 25 | 25 | 0 | 228 | 228 |
| volet2_E_a_I | 667–884 | 756–1006 | 16 | 16 | 0 | 131 | 131 |
| volet3 | 885–1110 | 1007–1251 | 23 | 23 | 0 | 69 | 69 |
| volets4_5_entete | 1111–1368 | 1252–1563 | 54 | 54 | 0 | 210 | 210 |
| volet6 | 1369–1626 | 1564–1791 | 22 | 22 | 0 | 85 | 85 |
| volet7_B_et_D | 1627–2069 | 1792–2203 | 34 | 34 | 0 | 115 | 115 |
| volet7_A_et_C | 2070–2665 | 2204–2803 | 48 | 48 | 0 | 144 | 144 |
| volets8_9 | 2666–2935 | 2804–3178 | 22 | 22 | 0 | 66 | 66 |
| volet10 | 2936–3655 | 3179–3894 | 42 | 42 | 0 | 150 | 150 |
| volet11_1_a_20 | 3656–4128 | 3895–4403 | 47 | 47 | 0 | 141 | 141 |
| volet11_21_a_52 | 4129–4729 | 4404–5037 | 58 | 58 | 0 | 189 | 189 |
| volet11_53_et_fin | 4730–5377 | 5038–5702 | 67 | 67 | 0 | 201 | 201 |
| **Total** | | | **496** | **496** | **0** | **1 906** | **1 906** |

Les lignes ajoutées comptent le texte de chaque insertion, plus les deux lignes vides que l'outil met autour.

Répartition par nature, identique dans les deux langues (496 par langue) :

- 27 encadrés « Limites et parades », un par instrument ;
- 223 renvois d'une ligne ;
- 240 avertissements ponctuels ;
- 5 morceaux de l'encadré du 2 octobre sur les sondes de désalignement : trois au volet 2 (fin de la présentation de la section A, fin de celle de la section C, et le C bis), plus deux renvois (volet M, M5, et volet 6, §8) ;
- 1 note d'ouverture « ce qui s'ajoute », qui porte l'index des 27 encadrés.

## 3. Échecs restants

Aucun. Au premier passage, aucune ancre n'était introuvable ni ambiguë dans sa tranche.

## 4. Contrôle d'intégrité

Sortie de `appliquer.py integrite` :

```
FR : 5378 lignes v3.5, 7284 lignes v3.6, 1906 ajoutées ; lignes v3.5 introuvables dans l'ordre : aucune
EN : 5703 lignes v3.5, 7609 lignes v3.6, 1906 ajoutées ; lignes v3.5 introuvables dans l'ordre : aucune
INTÉGRITÉ : OK
```

L'outil compte aussi la chaîne vide qui suit le dernier saut de ligne, d'où 5 378 et 5 703 ; `wc -l` donne 5 377 et 5 702.

J'ai recoupé par un contrôle plus strict, un `diff` entre la v3.5 et la v3.6. Dans chaque langue : 0 ligne retirée ou modifiée, 1 906 lignes ajoutées en 365 points d'insertion (certaines insertions partagent une ancre), et tous les blocs du diff sont des ajouts.

## 5. Jumelles français / anglais

- **Même nombre d'insertions par tranche** : oui, dans les 14 tranches (tableau du §2). Aucun écart.
- **Appariement une à une** : la n-ième insertion française d'une tranche avec la n-ième anglaise, soit 496 paires. Pour les 496 paires :
  - même nature (encadré, renvoi, avertissement ponctuel, morceau de l'encadré du 2 octobre, note d'ouverture) ;
  - même nombre de lignes, de limites et de parades, et de « aucune parade connue » / « none known » (aux variantes de traduction près) ;
  - mêmes nombres cités, décimales et milliers normalisés ;
  - même endroit. 339 paires sont vérifiées par l'identifiant du titre de section (numéro de question, M·, F·, numéro de réponse, lettre de section), 95 par des mots communs aux deux ancres, 62 à la main. Là où le français coupe un paragraphe en plusieurs lignes que l'anglais tient sur une seule, l'ancre française est la dernière ligne du même paragraphe ;
  - les insertions qui partagent une ancre sont groupées et ordonnées de la même façon dans les deux langues.
- **Langues** : aucun en-tête anglais dans le fichier français, aucun en-tête français dans le fichier anglais. Chaque fichier compte 496 mentions « (v3.6 ».
- **Renvois** : dans chaque langue, les 735 entrées de renvoi pointent vers l'endroit que donne l'index de la note d'ouverture. Vingt-huit entrées par langue portent un libellé précisé (« dont… », « encadré du 2 octobre »), toujours avec le bon emplacement. Les 27 emplacements de l'index correspondent aux encadrés réels.

## 6. Observations, sans correction (à trancher par la suite)

1. **Pas de mention *(v3.6)* sur l'encadré.** Ses cinq morceaux (10 insertions, 5 par langue) ne la portent pas, alors que la note d'ouverture dit que chaque ajout la porte. Ils sont datés « Encadré du 2 octobre 2026 » / « Box of 2 October 2026 ».
2. **L'encadré n'est pas mot pour mot.** Il reprend tout le contenu de `pieces/EXPLICATION_SOURCE_FR_2026-10-02.md`, mais avec des corrections de vérification, signalées en italique à la fin de chaque morceau :
   - point 2 : environ 80 à 86 % d'annotations en évaluation contre 34 %, au lieu de « et pas sinon » ;
   - point 3 : les réserves du README sont ajoutées ;
   - point 4 : la porte du lens est renvoyée aux parties 3 et 8 du programme au lieu de la partie 4, et l'alerte de Zeisler est précisée ;
   - partie 2 : « régression logistique » au lieu de « régression logistique régularisée », qui n'avait pas de source ;
   - étape 4 : on lit aux deux positions, pas à l'une ou l'autre ;
   - partie 3 : le RL du rapport 4 est un RL à récompenses vérifiables.

   Le préambule ne nomme plus le destinataire, et la consigne « À insérer en entier… » y est remplacée par la description de la répartition.
3. **Fiches coupées au volet 10.** 18 insertions par langue (sur 42) s'intercalent entre deux lignes consécutives d'une même fiche de lecture. Sans ligne vide entre elles, ces lignes ne forment qu'un paragraphe au rendu Markdown. Le texte est inchangé, mais la fiche s'affiche en deux paragraphes, de part et d'autre de l'avertissement.
4. **Le titre dit toujours v3.5.** Le titre de premier niveau des deux fichiers reste « v3.5 — 27 septembre 2026 », puisque la règle interdit de le modifier ; la note v3.6 qui le suit immédiatement dit ce qui s'ajoute.

Contrôles d'autres règles, sans écart trouvé :

- aucune revendication de priorité (« first », « premier ») dans le texte ajouté ;
- aucune citation de quinze mots ou plus ;
- aucune insertion dans un paragraphe « À dire ». Au volet 7, les dix insertions qui suivent un bloc « À dire / À ne pas dire / Questions probables » viennent après la fin du bloc, en fin de fiche ;
- aucune insertion dans un tableau, une liste ou un bloc de code.

## 7. Scripts de contrôle (lecture seule, relançables)

Dans `travail/_application/` :

- `controle_jumelles.py` : appariement et emplacement ;
- `controle_endroit.py` : même endroit ;
- `controle_formats.py` : formats fixes ;
- `controle_renvois.py` : renvois contre l'index ;
- et leurs sorties `.txt`.
