# Corrections de la carte des angles déjà pris, tour 3 (2 octobre 2026)

Fichier corrigé en place : `livrable/CARTE_ANGLES_DEJA_PRIS_2026-10-02.md`. Il passe de 1 195 à 1 205 lignes.

Repères :
- « avant » renvoie à la version du tour 2, celle que cite la critique (sha256 `1e54f86bdef22da20fc4b398b2f86c4a42a9f2d190c7a1cd907bc84e20051369`) ; « après », à la version corrigée.
- « nuit » renvoie à `pieces/ANTERIORITE_RAPPORTS_2026-10-02.md`, « 1er oct. » à `pieces/ANTERIORITE_RAPPORTS_2026-10-01.md`, « passation » à `pieces/PASSATION_PAPIER_v1.2_2026-10-02.md`, « consignes » à `pieces/ANTERIORITE_CONSIGNES_AGENTS_2026-10-02.md`, « v1.1 » à `pieces/PROGRAMME_RAISONS_OU_REGARD_2026-10-01.md`.

Empreintes après correction :
- markdown : 218 441 octets, sha256 `7744a85cf528d6ff3f75ead74a39447fea97793944e43ab5e608f6371ed764d6` ;
- PDF refait : `livrable/CARTE_ANGLES_DEJA_PRIS_2026-10-02.pdf`, 48 pages A4, sha256 `d7001b91434f34d988b52b1c804aa8783be14b73c4302c5ade4034915e1214ab`.

Fichiers ajoutés dans `travail/` :
- `note_surveillance_exp9.md` : le repère de surveillance de SUMMARY.md, sorti de la carte (mineur 10) ;
- `diff_carte_tour_3.patch` : le diff complet (`diff -U0`) entre les deux versions. Appliqué à l'envers (`patch -R`) à la carte corrigée, il redonne la version du tour 2 à l'octet près (empreinte vérifiée).

Chaque correction a été vérifiée dans les rapports, la passation ou les consignes. Aucune source n'a été ouverte sur le web.

---

## Bloquants

### 1. exp9 : « seulement scriptés », rangé parmi les erreurs relevées sur la source. Corrigé

Vérifié :
- passation, §4.2, n° 1 (l. 125-133) : la relecture couvre SUMMARY.md seul, « Aucun résultat d'entraînement n'y figure », et « Les scripts DPO ont été lus par l'agent, pas par l'instance principale » ;
- rapport 4 : ni `results/` ni l'historique n'ont été ouverts (nuit, l. 756) ; « Les résultats des entraînements DPO sont donc inconnus » (l. 944). Son résumé d'ouverture est plus affirmatif : « Aucun résultat de ces entraînements n'est publié » (l. 735) ;
- v1.1, l. 108 : le dépôt « compare un DPO où la chaîne de pensée fuit vers le modèle de récompense à un DPO sans fuite » ;
- l'erreur vient de `verif_angle_survie.md`, n° 9 (l. 171).

Corrections :
- §6.1, n° 1 (avant 824, après 827) : la phrase sur « compare » sort de la liste « relevées sur la source ». Le n° 1 garde ce que la relecture établit, et l'erreur qu'elle permet de relever : la v1.1 ne dit rien du résultat publié de l'étape statique (v1.1, l. 108 ; l. 807 : « Seule sa description a pu être lue »).
- Nouveau paragraphe, hors de la liste, après le n° 9 (après 837) : « Hors de cette liste, au conditionnel : les deux DPO d'exp9 ». Il reprend le texte de la critique :
  - SUMMARY.md (relu) ne publie aucun résultat des deux DPO ;
  - ils sont scriptés dans le dépôt (rapport 4, texte intégral des scripts de la phase 5, lus en brut ; nuit, l. 755 et 766-767) ;
  - `results/` n'a été lu ni par le rapport 4 ni par l'instance du papier ; des résultats y sont peut-être déjà ;
  - la phrase de la v1.1 passe au conditionnel.
- §6.3, ligne sur la l. 108 de la v1.1 (avant 938, après 947) : renvoie à ces deux points.
- Même prudence :
  - tableau du §4, ligne exp9 (avant 755, après 758) : « SUMMARY.md ne publie aucun résultat des deux DPO (relu) ; le dossier `results/`, sans lecture admise, en contient peut-être déjà ; d'autres peuvent paraître par un simple commit » ;
  - §5, risque 3 (avant 811, après 814) ;
  - §7, formulation n° 15 (avant 991, après 1000) : « À revoir après la relecture de `results/` d'exp9, où des résultats sont peut-être déjà… ».
- §3.7 (avant 605, après 607) : ajout de l'écart entre le résumé d'ouverture du rapport 4 et sa section « Vus mais non ouverts ». C'est sans doute la source du « Ses entraînements ne sont pas publiés » du §4.4, n° 7, que la carte signale déjà.
- Vu au passage, même nature : « aucun résultat public au 2 octobre », pour le projet SPAR de Lundqvist, devient « aucun résultat public trouvé » (avant 547 et 754, après 549 et 757). Le rapport 4 écrit « Je n'ai trouvé aucun résultat public » (nuit, l. 737).

### 2. « Les pages lues par des miroirs relues par le rapport 7, sauf *Constitutional adapters* ». Corrigé (avant 898, après 904-907)

Vérifié :
- consignes, l. 526-532 : l'agent 7 devait relire six textes « lus jusqu'ici par un site tiers ». Ce sont *Synthetic Persona Pretraining*, *Constitutional adapters*, *Deliberative Alignment is Deep*, *Generalization Hacking*, Mody et al. et Deckenbach et al.
- Rapport 7 :
  - texte intégral pour cinq d'entre eux (nuit, l. 1664, 1695, 1715, 1732 et 1745) ;
  - *Constitutional adapters* : « résumé seul, par sites tiers » (l. 1681) ;
  - en plus, 2606.08629 et 2606.08243, lus en HTML (l. 1815), sur une autre question de sa consigne.
- J'ai recensé, par recherche de pith.science, alphaXiv, awesomepapers et Hugging Face Papers, toutes les lectures par miroir des rapports du 1er octobre (1er oct., l. 49, 95, 97, 137, 144, 172, 207, 297, 304, 311, 334, 342, 357, 395, 402, 413, 419, 425, 431, 437, 461 et 465) et de la nuit (nuit, l. 36, 104, 143, 147, 151, 159, 162, 186 et 190). Pour chacune, j'ai cherché une lecture en texte intégral dans un autre rapport.

Nouveau texte, en trois sous-listes :
- relues en texte intégral par le rapport 7 : les cinq ci-dessus, plus 2606.08629 et 2606.08243 ;
- lues en texte intégral par un autre rapport :
  - Heidari et al. (rapports 2 et 6 ; nuit, l. 322 et 1303) ;
  - de la Fuente et Conmy (rapports 1 et 4 ; l. 36 et 881) ;
  - Wu et Tang (rapport 3 ; l. 495) ;
  - *Safety Reasoning with Guidelines* (rapport du 1er octobre sur raisons contre actions, HTML v2 ; 1er oct., l. 19) ;
- lues seulement par un site tiers ou en résumé, donc à relire :
  - les six travaux de la critique : *Constitutional adapters*, Wen et al., Ponkshe et al., Shah et al., Irpan et al., Dhoot et al. et 2609.38645. Pour Shah et Irpan, le rapport 3 n'a lu que le résumé (nuit, l. 629-630) ; pour Dhoot, le rapport 6 aussi (l. 1413) ;
  - **ajouté** : *Training LLMs to Verbalize Evaluation Awareness* (2609.36316). Il a été lu par Pith et par alphaXiv le 1er octobre (1er oct., l. 207, 334 et 342), par pith.science au rapport 1 (nuit, l. 190), et seulement en résumé aux rapports 4 et 6 (l. 902-904 et 1423-1424) ;
  - **ajouté** : trois lectures par pith.science du rapport 1, dans les rapports de la nuit : *Refuse without Refusal* (l. 151), *Do Thinking Tokens Help with Safety?* (l. 162 ; rapport 5, résumé seul, l. 1119) et 2604.18946 (l. 186). La partie 1 couvrira aussi les rapports de la nuit (correction de la l. 53, déjà dans la carte).

Même ligne de correction, plus loin dans le §6.3 :
- l. 101 de la v1.1 (avant 933, après 942) : Ponkshe et al. y est marqué « lu seulement par un site tiers (alphaXiv) », à relire avant de le citer au centre ;
- §7, tableau (avant 1010, après 1019) : « Wen et al. (site tiers) » prend le libellé complet.

### 3. Statuts hors des six libellés, ou faux. Corrigé

1. *The Geometry of Refusal*, rapport 5 (avant 575, après 577) : « titre et auteurs seuls (mode non précisé) » devient « résumé seul (mode non précisé) ».
   - Raison du choix entre les deux libellés : le rapport 5 corrige titre et auteurs dans ses « Corrections des repères » (nuit, l. 1177), sans dire comment, et ne le range pas parmi ses travaux vus et non ouverts. Dans la même section, il écrit « seulement vu dans une liste » pour un autre titre (Emotion Concepts, l. 1180).
   - La règle du §10 (mode non dit, donc « résumé seul (mode non précisé) ») s'applique, et pas « non ouvert ».
2. Billet d'OpenAI (avant 655, après 657) : « rapport 6, titre seul » devient « rapport 6, non ouvert : il le range parmi ses « Titres seuls » » (nuit, l. 1512-1513). La date du 7 mai 2026, donnée à la même ligne du rapport, est ajoutée.
3. Libellé de groupe du rapport 7 (avant 855, après 861) : *Constitutional adapters* sort du groupe « texte intégral ». Nouveau texte : « invérifiable selon le rapport 7, qui ne l'a lu qu'en résumé seul, par sites tiers » (nuit, l. 1681).
4. Même défaut, corrigé dans la même passe :
   - *Conditional misalignment*, statut du rapport 6 (avant 500, après 502) : « titre seul … (non ouvert) » devient « non ouvert (il le range parmi ses « Titres seuls »…) » (nuit, l. 1514) ;
   - §3.6, un titre vu par extrait (avant 573, après 575) : « titre seul » devient « l'extrait n'en donne que le titre » ;
   - §8, Nakamura (avant 1066, après 1075) : « (titre seul, §4.2, n° 8) » devient « qui n'en a relu que le titre et la date (§4.2, n° 8) » ; « rapport 3 seul » reçoit « (texte intégral) » (nuit, l. 568).
5. §10 (avant 1134, après 1144) : la frontière entre « non ouvert » et « résumé seul (mode non précisé) » est écrite pour les rapports de la nuit, avec ses cas :
   - un titre que le rapport range lui-même parmi ses titres vus et non ouverts est « non ouvert » ;
   - un travail qu'il cite ailleurs, sans mode ni contenu, est « résumé seul (mode non précisé) ».

### 4. Faits rattachés à une source qui ne les contient pas, ou sans libellé. Corrigé

- *Teaching AI to Handle Exceptions* (avant 142, après 143). Vérifié : le rapport du 1er octobre (l. 61-65) ne parle pas de longueur ; le rapport 1 écrit « Aucun contrôle de longueur », sans mode de lecture (nuit, l. 156-158). Ajouts : « rapport 1, résumé seul (mode non précisé) » au statut, et « Aucun contrôle de longueur (rapport 1) ».
- *Open Character Training* (avant 137, après 138). Vérifié : rapport 6, page de Cadile « lue en entier », « Pipeline construit sur OpenCharacterTraining » (nuit, l. 1452-1453). Nouveau texte : « Le pipeline du projet de Cadile est construit sur lui (rapport 6, texte intégral de la page du projet) ».
- *Eval Cooperativeness* (avant 478, 481 et 570 ; après 480, 483 et 572). Vérifié : le rapport 4 (nuit, l. 908) ne donne aucun mode de lecture. « Rapport 4, résumé seul (mode non précisé) » est ajouté au statut et aux deux mentions de la survie non testée.
- Deckenbach et al. (avant 134, après 135). Vérifié :
  - rapport 7 : « un argument direct contre un contrôle fondé sur la seule verbalisation » (nuit, l. 1756) ;
  - rapport 1, lu par pith.science : « un facteur de confusion direct pour tout gain obtenu en entraînant sur des textes » (l. 159-161) ;
  - rapport du 1er octobre sur la condition des gains, lu sur la page Hugging Face Papers : un confondeur, par « simple reconnaissance implicite de l'évaluation » (1er oct., l. 144-148).
  - Chaque lecture est rattachée à son rapport, et les deux statuts manquants sont ajoutés.
  - Le libellé du rapport du 1er octobre est « résumé seul » : une page Hugging Face Papers est une page de résumé, selon la règle de l'adresse du §10, comme pour les résumés Hugging Face du rapport 6 ailleurs dans la carte. Les consignes de la nuit classent Hugging Face Papers parmi les sites tiers (consignes, l. 55) ; je n'ai pas changé la règle de la carte.
- Même défaut, vu au passage, au §3.3 (avant 344, après 345) : « une sûreté gonflée par la reconnaissance implicite de l'évaluation » était rattaché au seul rapport 7. Nouveau texte : ce que montre le rapport 7, puis la lecture du rapport du 1er octobre.

---

## Mineurs

### 1. Niveaux posés par la carte sans qu'elle le dise. Corrigé

Les cas de la critique, chacun vérifié dans les rapports :

| Travail (avant → après) | Nouveau texte | Vérification |
|---|---|---|
| Korbak et al. (249 → 250) | moyen, estimation de la carte | Aucun rapport ne lui donne de niveau pour la dépendance au regard. Les rapports 1 et 4 le classent faible, pour raisons contre actions et pour la survie (nuit, l. 138 et 166 ; 887 et 894). La fiche de l'angle écrivait « faible, mais à citer au centre » ; `verif_angle_regard.md`, n° 12, jugeait la formule contradictoire |
| Hua et al. (243 → 244) | estimation de la carte (rapport 6 : moyen à faible ; le rapport 2 le range parmi ses travaux faibles) | Nuit, l. 1322 et 1331 ; l. 373 et 381-385 |
| Fiche Fable 5, §6.5.1.2 (259 → 260) | les deux niveaux sont des estimations de la carte | Le rapport 4 transmet la section sans niveau (nuit, l. 980-981) |
| Cho et al., dépendance au regard (221 → 222) | moyen, sous condition, estimation de la carte | Aucun rapport ne donne de niveau pour cet angle ; le rapport 4 : « Pas de mesure de la dépendance au regard » (nuit, l. 816) |
| exp9, survie (571 → 573) | faible, estimation de la carte | Le niveau vient de la fiche de la survie (`angle_survie.md`, n° 12) ; aucun rapport |
| Gasteiger et al. (506 → 508) | faible, estimation de la carte | Aucun rapport de la nuit ne le cite. Le rapport du 1er octobre dit « Recouvrement : partiel » (l. 161). Le vérificateur du retrait proposait faible à moyen, à fixer après lecture |
| Baker et al. (629 → 631) | moyen, provisoire, estimation de la carte | Aucun rapport ne le décrit |
| *Beyond Shallow Alignment* (126 → 127) | moyen (rapports 3 et 5) ; faible pour la question hors distribution, estimation de la carte | Nuit, l. 595 et 1071 ; le rapport 1 ne le cite pas (recherche dans tout le fichier) |
| Dépôt de Kretschmar (769 → 772) | faible, estimation de la carte | Aucun rapport ne classe le dépôt. Son billet est faible pour le retrait (rapport 3 ; nuit, l. 618) et moyen pour le juge (rapport 4 ; l. 876) |
| « Autres, faibles » (770 → 773) | niveau d'un rapport pour Cho et al., « Hacker-Opus », Epstein et Ravid et 2604.18946 ; estimation de la carte pour les autres | Cho et al. : rapport 5, l. 1168-1169. « Hacker-Opus » : le rapport 4 classe le Risk Report faible, l. 887 et 896-898. Epstein et Ravid : rapport 6, l. 1471-1473. 2604.18946 : rapport 1, l. 186. Rien pour les autres (nuit, l. 427-430, 667-671, 1186-1194 et 1499) |
| Betley et al., juge (641 → 643) | moyen, estimation de la carte (rapport 6 : moyen à faible ; le rapport 4 ne le cite pas) | Nuit, l. 1322 et 1347-1356 ; recherche dans le rapport 4 sans résultat |
| L'appel d'Ivanov (332 → 333) | moyen, estimation de la carte (rapport 6 : moyen à faible) | Nuit, l. 1322 et 1358-1369 |
| CAFT (486 → 488) | moyen pour la méthode, estimation de la carte ; les rapports 3 et 7 ne lui donnent pas de niveau | Rapport 6, faible (l. 1390-1395) ; rapport 3, l. 503-515 ; rapport 7, l. 1795 |
| Second Look Research (758 → 761) | moyen, provisoire, estimation de la carte (rapport 6 : faible à moyen ; le rapport 2 n'en donne pas) | Nuit, l. 1497 et 429 |

Même défaut, corrigé dans la même passe :
- légende, nouvelle ligne « Qui pose le niveau » (après 11) :
  - un niveau sans mention est celui d'un rapport de la nuit pour l'angle ;
  - « estimation de la carte » marque les autres, et c'est toujours le cas d'un travail vu seulement par extrait ;
  - dans les listes « Travaux de niveau faible », le rang faible est celui de la carte quand aucun rapport n'en donne, et un niveau plus haut, donné par un rapport, y est signalé ;
- pour que cette dernière phrase soit vraie, cinq signalements sont ajoutés :
  - *Agentic Misalignment in Summer 2026*, §3.2 (275) : le rapport 6 le classe moyen à faible avec l'article (nuit, l. 1322-1329) ;
  - *Sycophancy Towards Researchers*, §3.3 (344) : rapport 6, faible à moyen (l. 1371 et 1381-1384) ;
  - Deckenbach et al., §3.3 (345) : rapport 6, faible à moyen (l. 1385-1388) ;
  - *Training a Misaligned Reward Seeker*, §3.6 (572) : rapport 6, moyen à faible (l. 1339-1345) ;
  - Betley et al., §3.8 (723) : rapport 6, moyen à faible (l. 1355) ;
- tableau du §2 (39, 41, 42, 43) : estimations de la carte marquées pour Ivanov, Wu et Tang, *Infohazard Evaluations*, CAFT, Brazilek et Tidmarsh, Betley et al. ;
- Wen et al. (118 → 119) : moyen, provisoire, estimation de la carte. Le rapport du 1er octobre le dit adjacent (l. 428). Les rapports 3 et 4 n'en tracent que les citations entrantes (nuit, l. 723 et 1006) ;
- *Inoculate or Reflect?*, principe localisé (400 → 401) : estimation de la carte pour cet angle ; le niveau du rapport 5 vaut pour l'anatomie (l. 1055-1056) ;
- *Routing Subspaces*, annexe I, juge (650 → 652) : le niveau est celui que le rapport 3 donne pour le retrait (l. 547) ; le rapport 4 ne le cite pas ;
- tableau du §4 :
  - Ivanov (765 → 768) : moyen pour l'appel, estimation de la carte ;
  - Aaliyan (767 → 770) : faible (rapport 4, l. 933-937) ;
  - suite d'Imran et Shaikh (768 → 771) : le niveau est celui du billet publié (rapport 5) ;
  - Li et Turner, Lundqvist pour le retrait (761 et 754 → 764 et 757) : « (rapport 6) » ;
  - projet de printemps de LawZero (775 → 778) : faible par estimation de la carte (rapport 2, l. 412-417, sans niveau).

### 2. « Trois sous-questions » au §1. Corrigé (avant 23-24, après 24-25)
Le texte dit maintenant : « Quatre sous-questions sont au niveau élevé, occupées par trois travaux ». La première puce nomme la présence et la nécessité, et précise que la nécessité est aussi la sous-question élevée du principe localisé (§2 ; §3.4).

### 3. « Non ouvert » non établi pour deux billets. Corrigé par la règle
- *Alignment Midtraining Cracks Under Pressure* (avant 566, après 568) :
  - le rapport 2 le cite parmi ses travaux à transmettre, sans mode, sans auteur ni lieu (nuit, l. 397), et pas dans ses « Billets LessWrong vus, non ouverts » (l. 443). Il reçoit donc « résumé seul (mode non précisé) » ;
  - « LessWrong » ne venait pas du rapport 2, mais d'un extrait de recherche (`angle_survie.md`, l. 173 ; `corrections.md`, 2.20) : il est rattaché à l'extrait.
- Mallen et Greenblatt (avant 654, après 656) : le rapport 4 le range parmi ses travaux faibles, avec titre, auteurs et date (nuit, l. 899-900), et non parmi ses « Titres seulement » (l. 946-956). Il reçoit « résumé seul (mode non précisé) ».
- Écart avec le vérificateur du juge (`verif_angle_juge.md`, l. 164), qui demandait « non ouvert » : le rapport ne le dit pas. La carte signale cet écart à l'endroit.

### 4. Libellés incomplets ou abrégés. Corrigé
| Avant → après | Correction | Vérification |
|---|---|---|
| 330 → 331 | Ivanov : « rapport 3, résumé seul (mode non précisé) » | Nuit, l. 668 |
| 721 → 723 | *The Assistant Axis* : « rapport 5, résumé seul (mode non précisé) » ; ajout « rapport 6, non ouvert, parmi ses « Titres seuls » » | Nuit, l. 1138 et 1514 |
| 327 → 328 | « rapport 2, texte intégral des §7.6.1 à 7.6.4, figures non lues » | Nuit, l. 288 |
| 877 → 883 | « rapport 1, lu par un site tiers » ; même ligne, le rapport du 1er octobre reçoit « résumé seul » | Nuit, l. 159 ; 1er oct., l. 144 |
| 1084 → 1093 | « Rapport 2, texte intégral par l'API markdown, lu en partie » | Nuit, l. 345 |

Même défaut, corrigé dans la même passe :
- *Steering Awareness* (280 → 281) : « rapport 3, résumé seul (mode non précisé), rangé parmi ses « Partiellement lus » » (nuit, l. 680) ;
- tableau de l'anatomie, Lu et al. (687 → 689) : « mode non précisé » ;
- second billet d'Ivanov (329 → 330) : « rapport 2, non ouvert » (nuit, l. 443).

### 5. Inférence et guillemets. Corrigé
- l. 319 → 320 : la contradiction entre « stabilise » et « amplifie » n'est peut-être qu'apparente. C'est maintenant écrit comme une inférence de la carte, appuyée sur le rapport 6 (« becomes amplified » pour les étapes du SFT, puis « reste stable », nuit, l. 1306) et sur le rapport 2 (montée après le SFT, puis stabilisation, l. 323).
- l. 312 → 313 : citation exacte du rapport 1, « fait moins bien que l'entraînement complet » (nuit, l. 133). Ajout : le rapport 1 dit « en annexe », sans numéro ; que ce soit l'annexe O.3 est une lecture de la carte.

### 6. Korbak et al., « partout sauf sur Blackmail ». Corrigé (avant 567, après 569)
Ajout de « en chat ». Vérifié : rapport 7, sous « Chat » (nuit, l. 1596-1599), séparé des questions-réponses (l. 1595).

### 7. Points de contrôle de Cho et al. Corrigé
- Vérifié : rapport 7, « Un point complet pèse environ 241 Go » ; « Les points « après fine-tuning bénin » sont des adaptateurs LoRA d'environ 38 Mo » (nuit, l. 1768-1769). Passation, §4.3 : « environ 241 Go chacun » (l. 198).
- Corrigé aux trois endroits : §3.1 (96 → 97), §6.1, n° 21 (846 → 851), §6.3 (911 → 920).
- Ajouté aux imprécisions de la passation, qui passent de trois à quatre (850-851 → 855-857). La conclusion, inutilisables à 8B, tient.

### 8. Gasteiger et al., « faible, provisoire ». Corrigé (avant 506, après 508)
« Provisoire » est retiré. La carte lui donne « texte intégral » par la règle de l'adresse (§3.2 ; 1er oct., l. 158 : page du blog d'Anthropic), et la légende réserve « provisoire » aux niveaux posés sur un résumé ou un extrait. Le niveau devient « faible, estimation de la carte » (mineur 1).

### 9. La géométrie entre « je suis évalué » et le principe, comptée parmi ce qui reste libre. Corrigé
- §3.8 (avant 742, après 744-746) : sortie de la liste numérotée. Un paragraphe « Non cherchée, donc hors de cette liste » la suit.
- Même chose au §3.4 (avant 429, après 430-431). Sa liste « Ce qui reste libre » portait le même point en n° 6, avec « Rien ne permet de la dire libre ». La critique ne le relevait pas, mais l'incohérence était la même.

### 10. L'empreinte de SUMMARY.md, sans libellé. Corrigé, par déplacement
- La première option de la critique, la faire relever par l'instance du papier, ne m'est pas possible. J'ai pris la seconde.
- La taille, l'empreinte et l'origine du relevé sont dans `travail/note_surveillance_exp9.md`. J'y ai vérifié les fichiers de travail qui les donnent : `angle_survie.md`, l. 223 ; `verif_angle_survie.md`, l. 26 ; `projets_calendrier.md`, l. 154 et 268 ; `verif_projets_calendrier.md`, l. 202.
- Dans la carte, il n'en reste qu'un renvoi à la note, sans valeur :
  - tableau du §4, ligne exp9 (après 758) ;
  - §10 (après 1146 et 1151). Le §10 dit maintenant que raw.githubusercontent.com répond par curl, puisque l'instance du papier y a relu SUMMARY.md et le README (§4.2, n° 1), et que les relevés des agents n'ont pas de libellé admis.

### 11. *Where we are on evaluation awareness*. Corrigé (avant 278, après 279)
Ajout : « aussi rapport 2, non ouvert : il le range parmi ses billets vus, non ouverts » (nuit, l. 443 ; `veille.md`, l. 101).

### 12. « Les pages des projets n'annoncent pas de date propre ». Corrigé, avec une nuance (avant 750, après 753)
Nouveau texte :
- la page de Lundqvist n'annonce aucune date (rapport 4, texte intégral ; nuit, l. 924) ;
- celle de Cadile, lue en entier par le rapport 6, n'en rapporte aucune, sinon les semaines 10 à 12 pour les vecteurs de persona (l. 1452-1459) ;
- aucun rapport ne dit avoir lu en entier les autres pages de projets.

La critique proposait « non plus » pour Cadile. Le rapport 6 ne dit pas que la page n'a pas de date : il n'en rapporte aucune, et il rapporte un délai relatif. La formule s'en tient là.

---

## Refusé, ou fait autrement que proposé

Rien n'est refusé. Écarts avec la lettre de la critique :
- **Bloquant 1** : le n° 1 du §6.1 n'est pas vidé. Il garde l'erreur que la relecture établit, l'omission par la v1.1 du résultat publié de l'étape statique (v1.1, l. 108 et 807 ; §4.2, n° 1).
- **Bloquant 2** : la liste des textes à relire compte plus que les six de la critique, puisque le recensement en trouve d'autres (voir plus haut).
- **Bloquant 4, Deckenbach et al.** : le statut du rapport du 1er octobre est « résumé seul », et non « lu par un site tiers ». Raison au bloquant 4.
- **Mineur 3** : la règle prévaut sur la demande du vérificateur du juge, pour Mallen et Greenblatt.
- **Mineur 10** : déplacement dans une note de travail, faute de pouvoir faire relever le repère par l'instance du papier.
- **Mineur 12** : « n'en rapporte aucune » au lieu de « non plus ».

## Limites

- J'ai audité tous les niveaux écrits dans les §2 à §4. Pour le rang dans les listes « Travaux de niveau faible », je n'ai vérifié qu'une chose : aucun rapport n'y donne pour le même angle un niveau plus haut sans qu'il soit signalé. C'est ce que dit la nouvelle ligne de la légende.
- Je n'ai pas cherché si `results/` d'exp9 contient des résultats : la carte n'admet aucune lecture d'agent par curl, et cette relecture revient à l'instance du papier (§8).
- Le fichier `carte_angles/SHA256_PIECES.txt` existe, hors des dossiers autorisés : je ne l'ai pas lu. Les pièces n'ont pas été modifiées : leur date de modification est inchangée (08 h 16).

## Le PDF

Il a été refait avec les scripts du tour 2, depuis `travail/pdf_carte/` :

```
python3 md_vers_html.py ../../livrable/CARTE_ANGLES_DEJA_PRIS_2026-10-02.md CARTE_ANGLES_DEJA_PRIS_2026-10-02.html
NODE_PATH=/opt/node22/lib/node_modules node html_vers_pdf.js CARTE_ANGLES_DEJA_PRIS_2026-10-02.html ../../livrable/CARTE_ANGLES_DEJA_PRIS_2026-10-02.pdf
```

Résultat : 48 pages au lieu de 46.

Contrôles :
- pdftotext : les passages corrigés y figurent ;
- deux pages ont été rendues en image et regardées : la p. 37, avec la correction de la l. 61 et ses sous-listes, et la p. 33 (§5). Les aperçus ont été effacés.

## Ce qui ne change pas

Les décisions de Lazar restent écrites telles quelles, et elles concordent avec sa réponse relayée :
- le pré-enregistrement à son seul nom, avec son ORCID ; Claude est cité dans une phrase de méthode, pas comme auteur (§5, après 807) ;
- pas de contact avec Cadile ni Lundqvist pour l'instant, « non pas encore » (§4, après 751 ; §5, après 809).
