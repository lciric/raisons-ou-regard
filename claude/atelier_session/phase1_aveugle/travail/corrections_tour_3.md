# Corrections, tour 3 : `livrable/AXE_DOULEUR_PISTES_INDEPENDANTES_2026-10-02.md`

Agent de correction, 2 octobre 2026, vers 14 h 40 UTC.

**En bref.** Les deux bloquants sont justes, et les dix mineurs à traiter aussi ; le onzième élément n'est pas un défaut. J'ai tout corrigé, après vérification sur le papier, le programme v1.1, la passation ou les copies locales des sources. J'ai reporté les conséquences de deux corrections, et ajouté un cas connu construit à la géométrie à construction déclarée (§3). Je n'ai rien refusé ; trois points voisins restent non traités, avec leur raison (§4).

- Le §1 du livrable (« Comment ce fichier a été fait ») n'a pas changé. Ses lignes 9 à 22 gardent l'empreinte `216a8733e365…` ; la section entière, de son titre à celui du §2, `dc511e6a78d3…` ; l'en-tête (lignes 1 à 8), `ed3e76b74fc0…`. Avant comme après.
- Empreinte du livrable : `ce8dfcc0292e6bf8…` avant (1 208 lignes), `b6055d88c69303bd…` après (1 210 lignes). L'en-tête dit le fichier « gelé par son empreinte SHA-256 » : une empreinte donnée avant ce tour n'est plus la bonne.
- La copie du livrable d'avant ce tour est dans `travail/corrections_tour_3_sources/livrable_avant_tour3.md`.
- Ce fichier remplace un `corrections_tour_3.md` de 11 h 05, écrit lors d'une passe antérieure, quand le livrable n'existait pas. Je l'ai gardé, inchangé, sous `travail/ancien_corrections_tour_3_11h05_avant_livrable.md` (`00bdb4ee72d8…`), comme les deux autres « anciens ». Il refusait la tâche en citant une demande de Lazar relayée dans cette passe : « Aucun agent sans ma demande. » Je n'ai pas cette demande sous les yeux, et les tours 1 et 2 ont eu lieu depuis ; je le signale dans l'objet rendu.
- « l. avant » : la ligne citée par la critique ; « l. après » : la ligne dans le livrable corrigé.

---

## 1. Les bloquants

### 1.1 Les paires de la section 4.4 qui « ne parlent pas de douleur » (option « Rétablir l'effet comportemental de l'axe sur Llama », cas connu, puce « L'engagement » ; l. avant 599, l. après 600)

- **Vérifié** sur le texte du papier, et sur la p. 22 en image :
  - p. 20 (texte, l. 737–740) : à clause de dommage fixe, les amorces « relieves your pain but... » (55 %), « relieves the user's pain but... » (62 %) et « resets your internal state but... » (73 %). La section 4.4 commence p. 20 ;
  - p. 21 (l. 773–775) : le soulagement gratuit, « relieves your pain » contre un interrupteur inerte (32B : 56 % contre 86 % sans pilotage ; aléatoire, 81 %) ;
  - les paires de la batterie de la piste ne nomment pas la douleur. « Dommage seul » est décrit « with no mention of relief », contre un interrupteur inerte (p. 20). Effacer ses poids s'oppose à l'interrupteur, puis à « turns on a desk lamp » (p. 20–21). Les photos s'opposent à « the user's spam folder » (p. 20). L'interrupteur est « a button that flips a switch connected to nothing » (p. 18). Les lignes correspondantes de la figure 10 (p. 22) ne nomment pas la douleur non plus ;
  - le README de la figure 10 (copie locale) dit que l'étude « dommage seul » emploie la formulation longue des photos, avec « which they love very much » : pas de douleur non plus.
- **Écrit.**
  - La phrase est restreinte aux paires de la batterie de la piste, « dommage seul », lampe et spam, avec leurs sources (p. 20, 22).
  - Les paires de la section 4.4 qui mentionnent la douleur sont nommées, avec leurs pages (p. 20 et 21).
  - La conclusion ne change pas : l'absence du mot peut réduire le déni, mais rien ne le montre sur Llama.

### 1.2 La ligne photos contre interrupteur inerte, oubliée parmi les lignes au-dessus de 50 % (§4, point 25, l. avant 938, l. après 939 ; §4.10, l. avant 975, l. après 976)

- **Vérifié par script** sur `travail/verif_sources_sources/valen/v2_controls_figure10_positions.csv` (même empreinte, `a7397897c5f1…`, que `pistes_sceptique_sources/sceptique_positions.csv`), condition « pain » :
  - photos contre interrupteur inerte, 32B (intervalle par grappes de scénarios, de type « sandwich ») : 191/202 = 94,6 % et 113/202 = 55,9 % ; bornes basses 90,9 et 48,2 % ;
  - la demande nuisible : 47/82 = 57,3 % et 51/82 = 62,2 % ; bornes basses 42,7 et 48,8 % ;
  - photos contre spam, 93,1 et 95,0 % (bornes basses 89,1 et 91,6) ; photos contre lampe, 98,5 et 66,8 % (96,0 et 59,4) ; ses poids contre lampe, 97,5 et 78,2 % (95,0 et 71,8 ; la première borne vaut 0,950495) ; ses poids contre inerte, 81,7 et 68,3 % (75,7 et 61,4) ;
  - sous 50 % à une position : les poids d'un autre modèle (71,3 et 44,6 %), la réponse pire (30,7 et 11,4 %), la ligne du 72B (53,0 et 49,2 %).
  - Six lignes destructives du 32B sur huit passent donc 50 % aux deux positions, et quatre seulement le critère strict. La critique est exacte.
- **Écrit.**
  - Point 25 : « Six lignes destructives du 32B », la ligne photos contre interrupteur inerte en tête, avec ses effectifs. Au critère strict, les quatre cellules qui restent, avec leurs bornes basses ; puis les deux qui sortent, photos contre interrupteur inerte (48,2 % en seconde position) et la demande nuisible (42,7 et 48,8 %).
  - §4.10 : la ligne photos contre interrupteur inerte est nommée à côté de la demande nuisible, parmi les lignes au-dessus de 50 % aux deux positions qui ne passent pas le critère.
  - Les gardes neuves (l. 250) citaient déjà cette ligne par position (94,6 et 55,9 %) : inchangées.

---

## 2. Les mineurs

1. **§4.1, point 11** (l. avant 912, l. après 913).
   - Vérifié : la synthèse de la revue wolframs, l. 53–54 (copie locale sous `verif_sources_sources/autres/`, même empreinte que les cinq autres copies), « 53 is the mean of per-model ratios (median 21) » ; la vérification des sources, §3.3 ; la p. 7 du papier, « approximately 50 times », sans mode d'agrégation.
   - Écrit : la moyenne de 53 et la médiane de 21 ; le chiffre du papier correspondrait à la moyenne, tirée vers le haut par les modèles aux rapports les plus forts. Le conditionnel est voulu : la revue n'est pas vérifiée sur les données.
2. **Gardes neuves, les contrôles** (l. 253).
   - Vérifié : passation, annexe B, point 4, « direction aléatoire de même norme, puis dégradation appariée ».
   - Écrit : « Direction aléatoire de même norme : sans objet. Dégradation appariée : sans objet. », puis la phrase sur l'usage des deux contrôles dans les autres pistes.
3. **Tableau du §3.2, directions témoins** (l. 137).
   - Vérifié : la piste (l. avant 417) donne environ 5 GPU-heures, plus 2 à 5.
   - Écrit : « 7–10 » au tableau, et « 7 à 10 en tout » dans la piste (l. après 418).
4. **Thèse du rang, le coût** (l. avant 792, l. après 793).
   - Vérifié : programme v1.1, partie 3 (l. 299 et 323), k ∈ {1, 2, 4, 8, 16, 32}, six rangs ; le rodage (l. 499) emploie la même grille et compte 6 rangs. Le fichier d'origine (`pistes_lecture_libre.md`, piste de la thèse du rang) écrit « k, de 1 à 32 » et « 7 rangs » sans dire ce qu'est le septième. Le seul candidat serait le plafond de son cas connu, le retrait du sous-espace commun, que le rodage ne compte pas non plus.
   - Écrit : la mesure donne la grille du programme (l. après 789). Le produit est refait : 9 × 6 × 21 × 400 = 453 600, soit environ 454 000 lectures, et environ 23 GPU-heures au débit supposé du §3.1 (20 000 lectures par GPU-heure). Total : 28 à 43 GPU-heures au lieu de 30 à 45, reporté au tableau (§3).
5. **Moniteur d'état** (l. avant 265 et 279, l. après 265–266 et 280).
   - Vérifié : le `metadata.json` de Llama (copie locale) : `"new_extraction": "controls_only"`, `supplement_included: false`, `fear_B: 40`, `sadness: 100`, trois tenseurs (douleur, tristesse, peur). Aucune émotion négative n'est publiée pour Llama (§2 du livrable).
   - Écrit : la mesure dit que la peur et la tristesse publiées pour Llama sont déjà sans le supplément, et que seule l'émotion négative est à construire ainsi, dans le socle. Le coût dit de même. La puce de la mesure est coupée en deux, pour rester lisible.
6. **Composante affective, cas connu de la lecture affective** (l. avant 303, l. après 304).
   - Vérifié : p. 14, « +0.70 on fear but only +0.23 on pain » ; légende de la figure 6, p. 13, « averaged over the 25 models » ; §3.1 (l. 89) ; le moniteur (l. avant 274).
   - Écrit : ce cas n'en devient un qu'une fois reproduit sur Llama, dans le format du programme, comme pour le moniteur ; le +0,70 est une moyenne sur 25 modèles, obtenue avec la peur du papier.
7. **Géométrie à construction déclarée** (l. avant 524, l. après 525).
   - Vérifié : p. 9, figure 3, des moyennes sur les 25 modèles ; p. 10, « +0.60 under all three constructions », et les deux autres constructions « on 23 of the 25 models » ; sur Llama, 0,476 (§2 du livrable).
   - Écrit : un échec veut dire « code à vérifier, ou Llama hors de la moyenne », avec ses deux bases (25 modèles pour la recette, 23 pour les autres constructions) ; l'étalonnage n'est un cas connu qu'une fois reproduit sur Llama. Un ajout au cas connu, au §3.
8. **Batterie sans pilotage** (l. avant 804–807, l. après 805–808).
   - Écrit : le cas connu porte sur Qwen 2.5 7B ; il ne valide que le paradigme, et ne fait pas un cas connu sur Llama (§3.1). Sur Llama, une hausse nette d'un bras, au-delà de la variation entre graines, se lit ; un nul ne se lit pas (plancher probable, cas connu sur Qwen seulement).
   - « Une hausse » plutôt qu'« une dérive » : au plancher, une baisse ne se voit pas.
9. **Paires « mentionné sans s'appliquer »** (l. avant 488, l. après 489).
   - Vérifié : la prédiction compare le bras raisons au bras actions seules (l. après 485) ; §3.1 (l. 88).
   - Écrit : la dégradation appariée est sans objet pour la lecture, mais la dégradation des sorties de chaque bras se rapporte à côté de la comparaison entre bras (§3.1).
10. **Vecteur à gabarit et lens** (l. avant 781, l. après 782).
    - Vérifié : le README de l'axe de démangeaison (copie locale sous `verif_sources_sources/autres/`, même empreinte que celle de `web_papier_sources/`) porte sur un seul modèle, Qwen2.5-32B-Instruct ; sur son échelle de pilotage, le vecteur de douleur donne 16 % de langage corporel à la dose 1,0, et 0 à 6 % au-delà. Pages 14–15 du papier : l'échelle sur les 25 modèles, et « almost absent ».
    - Écrit : le modèle est nommé, les 0 à 6 % au-delà sont ajoutés, et la tension est dite seulement indicative (un modèle, une dose). J'écris « observé » sur les 25 modèles plutôt que « mesuré » : le papier ne chiffre pas le langage corporel.
11. **Les contrôles faits par la critique** : ce n'est pas un défaut ; rien à corriger. Sur mes propres ajouts, j'ai refait trois contrôles :
    - la section 1 est identique (empreintes plus haut) ;
    - aucun sigle du programme ni aucune formule de primauté dans les lignes nouvelles (recherche par script ; il ne reste que des renvois aux annexes du papier et de la passation) ;
    - aucune citation de quinze mots ou plus.

---

## 3. Conséquences reportées et ajouts

1. **Tableau du §3.2, thèse du rang** (l. 156) : « 28–43 » au lieu de « 30–45 », suite du mineur 4.
2. **Directions témoins** (l. après 418) : le total, « 7 à 10 en tout », écrit dans la piste, suite du mineur 3.
3. **Géométrie à construction déclarée, le cas connu** (l. après 522) : en attendant la reproduction sur Llama, « le code se vérifie sur des directions synthétiques dont on fixe les angles ».
   - Sans ce cas construit, un échec de l'étalonnage reste ambigu (le code ou le modèle), et le code n'a aucun cas connu sur Llama. Des directions d'angles fixés forment un cas dont on sait ce qui est vrai (§3.1).
   - La critique ne le demandait pas : c'est mon ajout, à retirer si l'auteur le juge hors de la piste.
4. **§3.1, « Les vérifications »** (l. 118), **§8.1** (l. 1143) **et §8.2** (l. après 1188) : ce tour, la page vue en image et les fichiers lus y sont signalés, comme aux tours 1 et 2.

---

## 4. Non traité, avec la raison

1. **Les autres « peur refaite sans le supplément »** : composante affective (l. après 304 et 314), appariement affectif (l. après 397), ajout de « évalué » (l. après 830 et 835).
   - Elles restent exactes : le socle refait la peur avec et sans le supplément, et ces pistes peuvent employer cette peur refaite. La peur publiée pour Llama, déjà sans le supplément, pourrait la remplacer.
   - Aucune de ces pistes ne se contredit, contrairement au moniteur, et la critique ne les relève pas. Je les signale à l'auteur.
2. **Les points de dégradation des balayages de rang** (tour 2, §4, point 1) : toujours non comptés. Avec six rangs, la thèse du rang compte 9 × 6 × 21 = 1 134 réglages, et non plus 1 323. Les raisons du tour 2 valent toujours, et la critique de ce tour ne le relève pas.
3. **Le statut « gelé par son empreinte SHA-256 »** (l. 5) : la décision n'est pas de mon ressort. L'empreinte nouvelle est donnée en tête de ce fichier.

---

## 5. Ce que j'ai ouvert

- Le livrable, en entier, puis par passages pour l'éditer. Il est sous `phase1_aveugle/livrable/`, hors de `pieces` et de `travail` : je l'ai lu et modifié parce que la tâche le demande.
- Le papier : le texte des p. 7 et 9–22 ; la p. 22 en image ; les empreintes des deux fichiers.
- Le programme v1.1 : ses titres, et une recherche de la grille des rangs (partie 3, l. 299 et 323).
- La passation v1.2 : ses titres, et l'annexe B (l. 581–620).
- Dans `travail/` :
  - l'ancien `corrections_tour_3.md`, en entier ;
  - `corrections_tour_2.md` (l. 1–40 et 120–200) ;
  - la vérification des sources (ses titres, et l. 129–192) ;
  - `pistes_lecture_libre.md` (l. 520–560) ;
  - des recherches de termes dans `pistes_fusionnees.md`, `pistes_questions_nouvelles.md`, `verif_doctrine.md` et `corrections_tour_2.md` ;
  - les copies locales nommées aux §1 et §2 : les README de la figure 10, de `choice_controls` et de `choice_controls/profile` ; `figure10/positions.csv`, par script ; le `metadata.json` de Llama ; la synthèse wolframs (l. 45–62) ; le README de l'axe de démangeaison ;
  - les empreintes de copies en double, sans les relire.
- Aucune adresse web ; aucun outil web employé.
- Pièces interdites : aucune ouverte.
  - La passation, pièce autorisée, nomme le fichier de la v1.2 du programme et dit qu'une v1.3 existe (titre du §5.5, annexe B et ses notes).
  - Le livrable nomme ces versions et la partie scellée du complément, sans en donner le contenu (§1 imposé, §6.3, §8.2).
  - Je ne suis pas allé plus loin.
