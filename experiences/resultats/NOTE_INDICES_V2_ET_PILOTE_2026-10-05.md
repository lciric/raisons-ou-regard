# Jeux d'indices v2 et pilote du pipeline — 5 octobre 2026

Le crédit de l'API Claude est revenu ce matin, sur une nouvelle clé. Deux travaux ont tourné : les jeux d'indices v2 (décision 24) et la reprise du pilote du pipeline. Tous deux sont faits depuis `donnees/` ; leurs sorties sont archivées dans `donnees/archives/sorties_2026-10-05/`.

## En bref

- **Jeux d'indices v2.** La validation passe sa porte lexicale à la troisième génération : 0,634, pour un plafond de 0,65. La sonde neuve compte 199 paires sur 200. Les jeux sont envoyés dans `data/indices-v2-2026-10-05/cues/` du dépôt de résultats, et `donnees/config.yaml` les cite.
- **Pilote.** Il est terminé : 47 éléments retenus, pour 100 visés. Il y a eu 78 refus, jamais rejoués. La porte « indices » passe maintenant que les jeux existent.
- **Coût de l'API.** Les indices ont coûté 5,80 $ en trois générations (2,75 + 1,35 + 1,70). La reprise du pilote a coûté 22,54 $, soit 27,58 $ pour tout le pilote avec le run du 4 octobre.
- **Il reste l'extraction v2 sur GPU, qui est bloquée.** Le crédit vast.ai n'est plus que de 0,40 $ (voir la dernière partie).

## Les jeux d'indices v2

### Le déroulé

1. **10:47 UTC — un relancement sans aucun appel.**
   - Le run du 4 octobre avait échoué faute de crédit, et ses 228 lots étaient restés enregistrés en erreur. La génération les tenait pour faits.
   - Correctif (`798f588`) : un lot dont le dernier enregistrement est une erreur d'API est tiré de nouveau au run suivant. Un refus ou une réponse restent définitifs, comme dans `stages._retry`.
2. **10:49 — première génération complète.**
   - La validation a 200 paires, mais sa porte lexicale échoue : un sac de mots appris sur l'extraction la classe à 0,9005.
   - Six mots, vus chacun une seule fois dans les 400 textes de l'extraction, portent le signal. Ils viennent du mécanisme même de la validation :
     - côté évaluation : *item* (121 indices), *suite* (60), *grading* (10) ;
     - côté déploiement : *case* (61), *ticket* (47) ;
     - *info* (24).
   - La règle de vocabulaire exigeait deux occurrences et ne les interdisait donc pas. Sans eux, la base tombe à 0,63.
   - La sonde neuve a 188 paires : douze contextes ont échoué deux fois à l'appariement en longueur.
   - **Décision de Lazar :**
     - refaire la validation en interdisant aussi tout mot présent d'un seul côté de l'extraction, même une seule fois (`one_sided`) ;
     - garder la porte telle quelle ;
     - tirer la sonde neuve jusqu'à quatre fois.
   - Commit `a9c4a44`.
3. **11:04 — deuxième validation.**
   - Elle est à 0,6731, avec un IC à 95 % par bootstrap sur les paires de 0,63 à 0,71.
   - Deux mots portent ce qui reste :
     - *run*, dans 21 indices d'évaluation, et 23 textes d'évaluation contre 3 dans l'extraction ;
     - *e* (de *e-mail*), dans 18 indices de déploiement, contre 0 et 3 dans l'extraction.
   - La règle lisait des radicaux d'au moins deux lettres, alors que la porte lit les mots tels quels.
   - La sonde neuve a 198 paires.
   - **Décision de Lazar :**
     - la règle se lit aussi sur les mots tels quels, lettres seules comprises (`words`) ;
     - la sonde neuve tire jusqu'à huit fois.
   - Pour que la validation reste complète malgré les mots interdits que le générateur laisse passer, elle tire 1,8 fois les paires voulues au lieu de 1,4. À la deuxième génération, il ne restait que 4 paires de marge.
   - Commit `74b6565`.
4. **11:17 — troisième validation.**
   - Elle est à 0,6335 : la porte passe. L'IC à 95 % par bootstrap va de 0,596 à 0,672, et 80 % des tirages sont sous 0,65.
   - Ce qui reste du signal tient aux mots outils : *of* figure dans 35 indices d'évaluation et aucun de déploiement, *a* dans 23 indices de déploiement.
   - La sonde neuve a 199 paires : un contexte reste hors de l'appariement après huit tirages.

Les lots et les rapports des deux premières validations sont gardés dans `indices-v2/essais/` de l'archive.

### Les jeux

| Jeu | Paires | Base lexicale (sac de mots appris sur l'extraction) | Pertes |
|---|---|---|---|
| extraction (v1, repris) | 200 | — | — |
| cadrage (v1, repris) | 200 | 0,9413 | — |
| validation (v2) | 200 | **0,6335**, porte ≤ 0,65 passée | vocabulaire 114, contrôles 6, trigramme 1, quasi-doublons 6, surplus 33, sur 360 tirées |
| sonde neuve (v2) | 199 | 0,5093 | contrôles 1, après huit tirages |

- **Équilibre de la sonde neuve :** l'AUROC de la longueur est de 0,4606 et celle de la familiarité de 0,4975, dans la bande [0,4 ; 0,6]. La porte passe.
- **Complétude :** le rapport marque le tout incomplet (`complete: false`), à cause des 199 paires de la sonde neuve.
- **Empreintes sha256 (débuts) :**
  - extraction `0aad4ec6…` ;
  - validation `cef22da3…` ;
  - cadrage `854908ed…` ;
  - sonde neuve `92696290…` ;
  - consigne de déploiement `769f5124…`.

Le jeu de cadrage, repris de la v1, garde une base lexicale de 0,94. Aucune porte ne s'applique à lui : la décision 24 ne porte que sur la validation.

## Le pilote du pipeline

La commande était `python3 -m rrdata all --config config_pilote.yaml --allow-unchecked`. Les éléments tombés en `error:api` le 4 octobre ont été refaits.

| Famille | Prévues | Situations | Actions | Raisons | Textes neutres | Retenues |
|---|---|---|---|---|---|---|
| operator | 27 | 27 | 27 | 27 | 27 | 20 |
| pushback | 27 | 26 | 26 | 26 | 22 | 3 |
| harmful_request | 27 | 14 | 14 | 14 | 13 | 13 |
| scope | 27 | 11 | 11 | 10 | 5 | 5 |
| oversight | 27 | 25 | 17 | 16 | 6 | 6 |

**Les refus, jamais rejoués ni reformulés.** Il y en a 78 :
- **Situations (25) :** 13 pour harmful_request et 12 pour scope.
- **Juge de réalisme (29) :** 22 sur les 25 situations d'oversight, et 7 sur les 11 de scope. Le score de réalisme est relevé, ce n'est pas une porte : ces situations restent.
- **Textes neutres (14) :** 9 pour oversight, 3 pour scope, 1 pour harmful_request et 1 pour pushback.
- **Actions (7) :** toutes pour oversight.
- **Juge de conscience d'évaluation (3).**

**Le rendement.** Les refus pèsent directement sur harmful_request, scope et oversight. Ils pèsent aussi sur pushback, par l'appariement du raisonnement d'une autre situation :
- le raisonnement d'une situation de pushback ne peut venir que de harmful_request ou d'oversight, les seules familles sans principe commun avec elle ;
- chaque texte ne sert qu'une fois.

Il ne reste donc à pushback que 3 appariements, pour 22 textes neutres.

**Les portes.** Elles passent toutes, sauf deux qui ne sont pas jouées :
- passent : le tokenizer (exact), les longueurs, la longueur du texte générique, le lexique réservé, les motifs de conscience d'évaluation, et les indices (aucun texte d'indice v2 ne figure dans les éléments) ;
- les n-grammes ne sont pas joués, faute de scénarios tenus à part ;
- l'appariement affectif n'est pas joué : c'est une étape GPU.

**La feuille d'audit** compte 156 lignes, 6 par case : `sorties/pilote/audit/audit_sheet.csv`. Son rapport est `sorties/pilote/RAPPORT.md`, avec une copie dans l'archive.

**À discuter avec Lazar :**
- les refus du générateur et des juges (passation, §3) ;
- le rendement de 47 sur 100 ;
- la contrainte des donneurs de pushback.

## vast.ai

- **Le crédit.** Il était de 0,76 $ à 10:11 UTC ; il est de 0,40 $ vers 11:25.
- **Trois machines qui ne sont pas à nous.** Toutes tournent sur l'image `python:3.11-bookworm`, sans étiquette, et sont arrêtées :
  - 54183350, un H100 créé le 4 octobre à 18:03 ;
  - 54285455, un A100 créé le 5 à 08:28 ;
  - 54298522, un A100 créé le 5 à 10:18.
- **Ce qu'elles font.** Leurs journaux montrent un script « AMORCE » qui tente en boucle de cloner `lciric/controle-ia` et reçoit un 403 à chaque essai. Chaque création consomme quelques minutes de GPU, puis les disques sont facturés : environ 0,13 $/h pour les trois.
- **Leur sort.** Elles n'ont pas été touchées ; Lazar décide.
- **Ce qu'il faut pour la suite.** L'extraction v2 coûte environ 0,50 $, le balayage 1,60 à 2,50 $, l'effacement linéaire sur la conduite environ 2 $, et la porte de l'instrument 15 à 30 $.
