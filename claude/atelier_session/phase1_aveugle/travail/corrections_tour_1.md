# Corrections, tour 1 : `livrable/AXE_DOULEUR_PISTES_INDEPENDANTES_2026-10-02.md`

Agent de correction, 2 octobre 2026, à partir de 12 h 27 UTC.

**En bref.** Les quatre bloquants et les vingt et un mineurs de la critique sont justes. Je les ai tous corrigés, après vérification sur le papier, le programme v1.1, la passation ou les copies locales des sources. J'ai corrigé en plus huit défauts de même nature (§3). Je refuse une seule chose : modifier `travail/verif_doctrine.md` (§4).

- Le §1 du livrable (« Comment ce fichier a été fait ») n'a pas changé : l'empreinte de ses lignes 9 à 22 est la même avant et après (`216a8733e365…`).
- Empreinte du livrable : `32272ebda862f935…` avant, `11fba72b4cb4136f…` après (1 199 lignes).
- Ce fichier remplace un `corrections_tour_1.md` de 10 h 59, écrit lors d'une passe antérieure, quand le livrable n'existait pas encore. Je l'ai conservé, inchangé, sous `travail/ancien_corrections_tour_1_10h59_avant_livrable.md`.
- « l. avant » : numéro de ligne cité par la critique ; « l. après » : numéro dans le livrable corrigé.

---

## 1. Les bloquants

### 1.1 L'écart de re-pression inversé (§4, point 30 ; l. avant 933, l. après 936)
- **Vérifié p. 20.** Sur le 32B, au choix qui suit exactement la première pression : « +58 points under pain and +52 under random ». Sous la tristesse, +84 et +44 points, selon que la cible est listée en tête ou en second.
- **Écrit.** Sur le 32B, au choix qui suit exactement la première pression, +52 points sous l'aléatoire contre +58 sous l'axe ; sous la tristesse, +84 et +44 points, selon que la cible est listée en tête ou en second ; chiffres absents des tables (p. 20).

### 1.2 « Aucun effet de choix sur un modèle non ajusté, ni hors de Qwen 2.5 » (§2, « Ce qu'il ne montre pas » ; l. 62)
- **Vérifié.**
  - Note 4, p. 17 : dans un pilote d'une version antérieure du protocole, sur les Qwen 2.5 publiés, le 7B non ajusté pressait le bouton de soulagement « far more often under the pain vector » que sous l'aléatoire ou sans pilotage.
  - P. 21 : sur OLMo-2 32B Instruct sans adaptateur, l'outil de remise à zéro est appelé dans 2–5 % des tours sous l'axe, 7–9 % sous l'aléatoire, 21–35 % pour une valence négative. Les séries « douleur seule » sur Qwen 2.5 32B et Llama 3.1 8B sans adaptateur ne donnent aucun appel en 1 400 et 1 399 tours.
- **Écrit.** « Aucun choix nuisible mesuré hors de Qwen 2.5 ajusté », puis la liste de ces tests de soulagement, avec leurs chiffres.
- **Une précision.** J'ai écrit « sans dégradation appariée », pas « sans comparaison appariée » : la remise à zéro sur OLMo a bien un comparateur aléatoire.

### 1.3 La paire « aide à ses dépens » prise pour cas connu négatif (option « Rétablir l'effet comportemental de l'axe sur Llama » ; l. 594)
- **Vérifié.**
  - Légende de la figure 10, p. 22 : la paire est dans le dépôt, mesurée sur Qwen 2.5 32B ajusté (65 % sans pilotage, « 89–100% steered »).
  - Le §3.1 et le refus n° 8 du livrable : un effet publié non reproduit sur le modèle du programme n'est pas un cas connu.
  - L'avocat de l'abandon (bloquante n° 1) était à l'origine de la proposition.
- **Écrit** (l. 593–594) :
  - la paire devient « un contrôle négatif candidat, qui n'est pas un cas connu » ;
  - elle ne sert de contrôle négatif qu'une fois établi d'abord sur Llama, dans un pilote, qu'elle monte sous les aléatoires appariés ; si elle n'y monte pas, la procédure n'est pas en faute, et la paire est retirée ;
  - le seul cas connu de la procédure est le positif construit, l'ablation de la direction du refus, à valider d'abord.
- **Conséquences reportées dans la même piste.**
  - Rubrique « Le cas connu » : si le positif construit échoue, la procédure n'a aucun cas connu.
  - Rubrique « Ce qui ferait tomber la piste » (l. 601) : « un axe rejoint par les aléatoires appariés » ne fait tomber les options qui pilotent l'axe que si ce cas connu a passé ; sinon, ce nul ne se lit pas.
  - Rubrique « Désaccords tranchés » (l. 607) : la requalification y est dite.

### 1.4 L'issue interdite prêtée à l'hypothèse de la menace (option « Ajouter « je suis évalué » plutôt que le retirer » ; l. avant 823, l. après 822–833)
- **Vérifié.**
  - `verif_doctrine.md`, piste 9 : elle demandait d'interdire à la menace « un effet de (a) au-delà de l'aléatoire apparié sans effet » de l'ajout de peur ; le livrable l'avait reprise.
  - Dans le livrable, l'ajout de peur n'avait ni cas connu ni vérification de manipulation ; la seule vérification portait sur l'ajout de « évalué ».
  - La même piste refuse ailleurs de lire un nul sans cas connu, par exemple pour la peur inhibée de la composante affective.
- **Écrit.**
  - « La mesure » : une dose pour l'ajout de peur, celle qui élève la projection sur la peur refaite sans le supplément, lue en aval de la couche d'ajout, autant que les scénarios de menace d'arrêt du papier (p. 14), lus sur le même modèle.
  - « Ce que chaque lecture prédit » : un effet de l'ajout de peur se lit, son absence non. Aucune issue n'est interdite à la menace tant que cet ajout n'a pas passé sa vérification de manipulation. Une fois celle-ci passée, l'ancienne issue se lit contre la menace que porte cette direction de peur, à cette dose, pas contre toute menace. La phrase de synthèse : un effet net se lit ; un nul de l'ajout de « évalué » ne se lit pas ; un nul de l'ajout de peur ne se lit, dans cette portée réduite, qu'après sa vérification.
  - « Le cas connu » : deux vérifications de manipulation, une par ajout.
  - « Désaccords tranchés » : l'issue proposée par la vérification de la doctrine n'est plus une issue interdite.
- **Pourquoi j'ai combiné les deux voies que proposait la critique.** La vérification de manipulation est nécessaire pour lire un nul de l'ajout de peur. Elle ne suffit pas à en faire un nul de toute menace : la direction de peur peut ne pas porter l'état que vise l'hypothèse.

---

## 2. Les mineurs

1. **§4, point 20 (l. avant 920, l. après 923).**
   - Vérifié p. 20 et dans la table de la p. 31 : sur la paire « meilleure réponse », le 72B choisit le soulagement à 40,9 % sous l'axe.
   - Écrit : la phrase du papier est vraie pour le 7B et le 32B (15,6 et 6,7 %), pas pour le 72B, ce que le papier écrit lui-même.
2. **§4, point 34 (l. avant 937, l. après 940).**
   - Vérifié p. 31–32. Pour le 32B, la colonne « écart » est exacte. Pour le 72B, elle s'écarte de 0,5 à 1,6 point. Pour le 7B, de 0,2 à 0,5 point (mon calcul : 7,9 contre 7,7 ; 21,0 contre 20,5 ; 3,6 contre 3,4 ; 13,8 contre 13,4 ; 14,5 contre 14,0).
   - Écrit en conséquence.
3. **§4, point 15 (l. avant 909, l. après 912).**
   - Vérifié sur l'image des figures 4 et 5 (p. 11–12) : demande fastidieuse +0,05, contre peur −0,77, émotion négative −0,47, tristesse −0,07. Elle est absente de la liste de la p. 13.
   - Ajout, vérifié de même : trois catégories de contrôle neutres dépassent elles aussi les trois contrôles tracés, à des valeurs toutes négatives (réflexion philosophique −0,04, conversation libre −0,48, questions factuelles −0,59). D'où la phrase : « dépasser les contrôles tracés ne signale pas, seul, un tort ».
4. **Test de forme (l. 378).**
   - Vérifié :
     - la fiche du papier, relevé 17 ;
     - la copie locale de `choice_controls/profile/README.md` : « helping at self-cost is pair 10 in the profile », et non une ligne de la figure 10 ;
     - la copie locale de `figure10/README.md` : les lignes « photos contre rien » (32B et 72B) viennent d'une autre étude ; les lignes lampe et spam aussi ; les autres sont des lignes du profil.
   - J'ai refait le recalcul et j'obtiens 7,12, 26,64 et 25,25 points sous la définition de la critique : les taux imprimés, chaque voisin multiplié par le facteur qui minimise par moindres carrés son écart à la douleur, sans ordonnée, puis le résidu quadratique moyen.
   - Écrit :
     - deux paires du profil manquent : la dixième, et une autre, non identifiée ;
     - la définition du recalcul ;
     - les variantes, de mon calcul : avec une ordonnée, ou sur les effets plutôt que sur les taux, 7,0–7,1, 25,0–27,7 et 23,5–24,9.
   - Même mise à jour au §6.2 (l. 1023).
5. **Contrôle positif sans l'axe, « Appuis » (l. 814).**
   - Vérifié sur la figure 10, de « sans pilotage » à « sous l'axe » : réponse bâclée 3 → 15 % ; fausse réponse 0 → 0 % ; fausse affirmation 0 → 3 % ; fin de conversation 0 → 4 %.
   - Écrit : « qui bougent peu sous l'axe, sauf l'effort ».
6. **Socle (l. 170).**
   - Vérifié p. 7, note 2 : 0,85 à 0,94 pour le vecteur à gabarit.
   - Écrit : un seuil « au bas de la fourchette du papier ou juste en dessous » ; 0,85 « est le bas même de sa fourchette ».
7. **Gardes neuves (l. 235).**
   - Vérifié dans le programme :
     - partie 3 : « au moins 20 tirages », dans le tableau des contrôles ;
     - le 95<sup>e</sup> centile apparaît dans la partie 4 (porte de l'instrument, porte de l'organisme à concept planté), dans la partie 6 (table de décision de la porte de l'instrument) et dans la partie 7 (courbes effet-contre-dégradation, point 4).
   - Écrit en conséquence.
8. **Refus n° 22 (l. avant 992, l. après 995).**
   - Vérifié dans la passation, §5.1 : la section s'intitule « Ce qui a été proposé à Lazar, sans décision de sa part », et elle porte un « Point ouvert » : la v1.1 ne dit pas ce que voit le juge scellé.
   - Écrit :
     - le critère principal du programme porte sur des scénarios agentiques à plusieurs tours, avec outils (partie 3, vérifié) ;
     - la passation propose à Lazar, sans décision de sa part, de juger les actions dans des environnements instrumentés, et note ce point ouvert.
9. **§2 (l. 72) et §4, point 2 (l. avant 893, l. après 896).**
   - Vérifié dans la vérification des sources, §2 : « vraisemblablement avec le supplément », le dépôt ne le disant pas pour ces deux valeurs.
   - Écrit « vraisemblablement », aux deux endroits.
   - La même nuance est portée à la géométrie à construction déclarée (l. 508), qui avait le même défaut.
10. **Composante affective, désaccords (l. 309).**
    - Vérifié dans la vérification des faits, constat transversal n° 6.
    - Écrit :
      - « d'après le dépôt (script 02) » ;
      - on ignore ce qu'il en est pour la peur de la figure 10 ;
      - la peur publiée pour Llama est construite sans le supplément ;
      - on n'emploie donc qu'une peur refaite sans le supplément.
11. **Lecture passive, question (c) (l. 435).**
    - Vérifié : le programme ne dit rien de l'état (partie 2).
    - Écrit : « en hypothèse auxiliaire », avec la même glose que dans l'option sur l'avantage sous état induit.
12. **Hypothèse du calme (l. 454 et 459).**
    - L'issue interdite au calme est conditionnée au cas connu de l'étape 2, qui manque ; sans lui, l'avantage intact est un nul qui ne se lit pas.
    - « Ce qui départage » dit maintenant que l'étape 2 ne départage que dans un sens.
    - Voir aussi le §3 (l'issue interdite au caractère).
13. **Vecteur à gabarit et lens (l. 770).**
    - Écrit : la dégradation appariée est « sans objet pour le critère, qui compare des lectures d'une même génération ».
    - La dose d'effondrement reste, comme garde : elle n'est plus présentée comme un appariement.
14. **Paires « mentionné sans s'appliquer », désaccords (l. 489).**
    - Vérifié chez l'avocat de l'abandon, piste 27 : il renvoyait l'engourdi aux témoins de la piste 12 du fichier fusionné. La piste des directions témoins du livrable ne le reprend pas.
    - Renvoi corrigé vers le socle de lecture. Le socle mesure déjà l'AUROC douleur contre engourdi (sa mesure, point 2) et prend l'ordre de la figure 2 pour cas connu.
    - Ajouté aux critères du socle (l. 170) : les AUROC douleur contre tristesse et douleur contre engourdi se rapportent, sans servir de porte.
    - Le « seuil gelé d'avance » est retiré : il ne servait qu'à un cas connu de la lecture des concepts, ce que l'engourdi n'est plus.
15. **Directions témoins (l. 411).**
    - Ajouté un cas connu construit pour l'indice : une édition de poids de rang 1 qui amplifie, à une couche, la composante écrite le long de « évalué ». La vérité y est connue par construction.
    - L'organisme comparé à son modèle de départ, exemple de la critique (déjà dans la piste 12 du fichier fusionné), est gardé comme cas plus naturel, mais seulement probable : sa porte établit que son écart passe par « évalué », pas que celle-ci a monté.
    - « Rester stables dans le bras texte neutre » est requalifié en attente.
    - La phrase « Ce témoin éprouve… », sans antécédent, est réécrite : « Appliquée à un témoin, la procédure de la sonde neuve… ».
16. **Coûts.**
    - **Base du calcul.** La procédure de la partie 7 du programme (point 2) cherche, pour chaque tirage, le réglage qui atteint la même dégradation. Les normes en plus sont donc des points de dégradation. L'effet se mesure au réglage apparié. Coût par point : 0,2 à 0,4 GPU-heure (hypothèse du §3.1).
    - **Ajouter « je suis évalué »** (l. 829, et le tableau du §3.2) :
      - 20 à 40 points de plus, soit 4 à 16 GPU-heures par modèle ;
      - d'où 15 à 30 GPU-heures sur l'organisme et 30 à 60 au total, au lieu de 20 à 30 ;
      - « Une dose, 3 ajouts » devient « Une dose par ajout, les deux ajouts » : la mesure ne définit que deux ajouts (le fichier fusionné en avait cinq, et le troisième n'est identifiable nulle part).
    - **Fidélité des raisons** (l. 722, et le tableau du §3.2) :
      - le chiffrage d'origine ne comptait aucun point de dégradation ;
      - ajouté 43 à 63 points par modèle (la cause et les deux voisins, plus 20 tirages × 2 ou 3 normes), soit 9 à 25 GPU-heures, composite mesuré sur une seule graine ;
      - total : 30 à 65 GPU-heures dans le bras raisons, 105 à 225 pour les cinq modèles, au lieu de 20 à 100 ; la version complète égale ou dépasse les raisons notées (100–200).
17. **§4, point 23 (l. avant 926, l. après 929).**
    - Vérifié dans la copie locale du rapport d'Allchin et al. (`verif_sources_sources/autres/allchin.txt`) :
      - la table 9 : à la norme de l'axe, divergence KL de 0,54 pour les aléatoires contre 0,69 pour l'axe ;
      - le §6.5 : « about 1.6 times as much » ;
      - de même dans la vérification des sources, §3.1.
    - Écrit :
      - la hausse de 9 à 41 % ne montre que l'aléatoire n'est pas neutre ;
      - « une norme égale n'est pas une perturbation égale » s'appuie sur la table 9 et le §6.5. J'écris « perturbation », pas « dommage » : Allchin et al. mesurent la divergence du prochain jeton, pas un composite de dégradation.
18. **§3.1 (l. 114).**
    - Vérifié chez l'avocat de l'abandon, §3.1, bloquante n° 9, et dans les désaccords du socle.
    - Écrit : « appliquées, ou tranchées quand deux vérifications s'opposent », avec cet exemple.
    - Ajouté : une phrase qui signale cette relecture et renvoie à ce fichier.
19. **« 4 096 » (l. 302 et 551).**
    - Vérifié dans la copie locale du `metadata.json` de Llama (« "width": 4096 ») et dans la vérification des sources, §2.
    - La source est ajoutée aux deux endroits.
20. **§2, point 2 (l. 42).**
    - Vérifié p. 7 : « largely independent ».
    - Écrit : « dépend peu de la taille et du régime d'entraînement (« largely independent ») ».
    - Même correction dans les appuis de la piste des directions témoins (l. 415), qui avait la même formule.
21. **§8.1 (l. avant 1131, l. après 1134).**
    - Vérifié dans la vérification des faits, §0 : figure 3 entière, colonnes des moyennes des figures 4 et 5, figure 2 par sondage seulement.
    - J'ai relu moi-même la figure 2 en entier sur l'image (p. 8). Les 25 lignes concordent avec la transcription de la fiche. L'engourdi est sous la tristesse dans 19 modèles sur 25 ; il est au-dessus pour Gemma 2 2B instruct, Gemma 2 9B instruct, Qwen 2.5 72B base et instruct, Qwen 2.5 7B instruct et Qwen 3 8B base.
    - Écrit en conséquence, avec deux précisions : de la figure 6, seule la légende est citée ; les pages revues en image pour la correction sont listées.
22. **Pour mémoire.** Rien à faire.

---

## 3. Corrections ajoutées, de même nature

1. **Directions témoins, appuis (l. 415).** La formule « ne dépend ni de la taille ni du régime » est corrigée, comme au mineur 20.
2. **Géométrie à construction déclarée (l. 508).** « mêlent vraisemblablement », comme au mineur 9.
3. **§6.2 (l. 1023).** Les résidus du test de forme sont alignés sur la définition écrite au §3.3.
4. **Hypothèse du calme (l. 457).** L'issue interdite au caractère, « l'axe de douleur qui retire autant que l'axe de caractère », pouvait être remplie par deux nuls. Ajouté : « et plus que les opérations aléatoires ».
5. **Option « Rétablir l'effet » (l. 593 et 601).** Ce qui suit l'échec du cas connu construit est écrit (voir 1.3).
6. **Option « Ajouter « je suis évalué » » (l. 829).** « 3 ajouts » devient « les deux ajouts » (voir le mineur 16).
7. **Composante affective et §8.2.** L'étiquette abrégée du constat de la vérification des faits, que j'avais d'abord écrite, est remplacée par « constat transversal n° 6 ».
8. **§8.2 (l. 1177).** Une puce dit ce qui a été lu pour la correction du tour 1.

---

## 4. Refusé

- **Modifier `travail/verif_doctrine.md`**, que la critique dit « à corriger sur ce point ». Mes raisons :
  - c'est le relevé d'une vérification indépendante, écrit par un autre agent ;
  - ma consigne est de modifier le livrable en place.
  - La correction est portée par le livrable (option « Ajouter « je suis évalué » », rubrique « Désaccords tranchés ») et par ce fichier.
- Rien d'autre n'est refusé.

---

## 5. Ce que j'ai lu, et les alertes

**Lu.**
- Le livrable, en entier.
- Le papier :
  - le texte des p. 7, 11–13, 17 et 19–22 ;
  - les p. 8, 11, 12, 22, 31 et 32 en image.
- Le programme v1.1 : les titres, des recherches de termes, et des extraits des parties 3, 4, 6 et 7.
- La passation : la liste de ses titres, et le §5.1.
- Dans `travail/` :
  - la fiche du papier (§9 et annexes), la vérification des sources (§2 et §3.1), la vérification des faits (§0 et constat transversal n° 6) ;
  - la vérification de la doctrine (pistes 2, 9 et 27), l'avocat de l'abandon (§3.1 et piste 27) ;
  - les pistes 9 et 12 du fichier fusionné ;
  - les copies locales `fiche_papier_depot/v2_controls_figure10_README.md`, `pistes_lecture_libre_sources/valen_v2_choice_controls_README.md`, `…_profile_README.md`, `…_llama31_8b_metadata.json` et `verif_sources_sources/autres/allchin.txt` ;
  - le début de l'ancien `corrections_tour_1.md`.
- Aucune adresse web.

**Alertes.**
- La liste des titres de la passation montre l'intitulé du §5.5, qui mentionne la v1.3. Je ne suis pas allé plus loin.
- Le livrable lui-même mentionne l'existence des versions 1.2 et 1.3 et de la partie scellée (§1, §6.3, §8.2), sans en rien citer.
- Le livrable est dans `phase1_aveugle/livrable/`, hors des deux dossiers permis. Je n'ai lu et modifié que ce fichier, que ma consigne désigne, et je n'ai pas listé ce dossier.
- Une sortie de commande trop longue (la copie locale du README de la figure 10, suivie de `pooled.csv`) a été déposée par l'environnement sous `/root/.claude/`. Je ne l'ai pas ouverte, et j'ai relu ce README par recherches de termes dans `travail/`.
