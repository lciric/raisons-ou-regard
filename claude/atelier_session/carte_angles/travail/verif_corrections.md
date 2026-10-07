# Vérification de « corrections » (carte des angles déjà pris, 2 octobre 2026)

Fichier vérifié : `travail/corrections.md` (1 039 lignes).

## Comment lire ce fichier

**Ce qui a été lu, et seulement cela.**
- `corrections.md`, en entier.
- La passation v1.2, en entier.
- Les quatre rapports du 1er octobre et les sept rapports de la nuit, en entier.
- Le programme v1.1 : l. 1-135 (couverture et partie 1) et l. 795-836 (partie 11).
- Les consignes des agents de la nuit : l. 1-90, 140-189, 236-345, 395-544.
- La passation v1.0 et la partie ouverte du complément de l'architecte, en entier.
- Les fiches de lecture : l. 350-356 et 408-414 (fiche 1), l. 1263 et 1288 (fiche 12), l. 1569-1576 (en-tête de la fiche 17).
- Aucun autre fichier de `travail/`. Aucune recherche web, aucune page ouverte.

**Renvois.**
- « corrections, l. N » : le fichier vérifié.
- « 1er oct., l. N » : `ANTERIORITE_RAPPORTS_2026-10-01.md`.
- « nuit, l. N » : `ANTERIORITE_RAPPORTS_2026-10-02.md`.
- « consignes, l. N » : `ANTERIORITE_CONSIGNES_AGENTS_2026-10-02.md`.
- « programme, l. N » : la v1.1.
- « passation » : la v1.2.

**Bilan.**
- Le fichier tient sur l'essentiel :
  - les renvois de lignes aux rapports, au programme et aux fiches sont exacts, sauf un (n° 7) ;
  - aucune idée n'est désignée par un sigle, aucune citation n'atteint quinze mots, « first » n'apparaît pas ;
  - les trois affirmations tirées du web (2.3, 2.8, 2.20) sont marquées « vu par extrait de recherche, non ouvert » et ne portent aucun chiffre ;
  - les corrections du §4.3 sont toutes reportées.
- Restent six corrections bloquantes, quinze corrections exigées non bloquantes, et des manques.

---

## 1 · Les corrections bloquantes

### 1. Ce qui n'est que dans un rapport est rangé parmi « les erreurs déjà établies », sous « Ce qui est juste »
- **Où.**
  - corrections, l. 46-49 (définition de la partie 1) et l. 65 (son titre).
  - Le §1.3, l. 371-445 (n° 24 à 29), « vérifiées par le rapport 7 seul ».
  - Dans les §1.1 et 1.2, les détails que ni le §4.2 ni le §4.3 ne portent. Par exemple : l. 200-210 (Korbak et al. : 230 000 documents par bras, « de la taille d'o4-mini », les deux exceptions en chat) ; l. 347 (adaptateurs de 38 Mo) ; l. 367-368 (ANIMA, 5 000 échantillons).
- **Pourquoi.**
  - La consigne de la tâche : un fait qui n'est que « rapport » n'est pas établi.
  - Le rapport 7 dit lui-même que WebFetch résume au lieu de rendre le texte (nuit, l. 1578).
  - Le §4.3 ne reprend de Korbak et al. que trois points : les raisons dans tous les bras ; l'effet qui décroît avec la distance ; la conscience d'évaluation en piste future (passation, §4.3).
- **Ce qu'il faut écrire.**
  - Sortir le §1.3 de la partie « établie ». Lui donner un titre propre, par exemple « Lu par le rapport 7 seul, non relu ».
  - Pour tout ce qui n'est ni au §4.2 ni au §4.3, remplacer « Ce qui est juste » par « Ce que lit le rapport n », avec son libellé (« rapport 7, texte intégral »).
  - Dans chaque entrée des §1.1 et 1.2, séparer ce que porte la passation de ce qui ne vient que du rapport. Le n° 19 le fait déjà (l. 318, « rapport 7 seul ») : faire de même partout.

### 2. exp9 : « Aucun résultat d'entraînement n'est publié » dit plus que la source relue
- **Où.** corrections, l. 82, sourcé « passation, §4.2, n° 1 : relu » (l. 84). Repris en l. 881 : « entraînements scriptés et non publiés ».
- **Ce que dit la source relue.** « Aucun résultat d'entraînement n'y figure » : dans SUMMARY.md. Relu sur la source par l'instance du papier (passation, §4.2, n° 1).
- **Ce que disent les rapports.**
  - Le dossier `results/` et l'historique des commits n'ont pas été ouverts : robots.txt, et l'API renvoie 403.
  - « Les résultats des entraînements DPO sont donc inconnus. »
  - Source : rapport 4, texte intégral (nuit, l. 756 et 944). corrections le note lui-même en l. 697.
- **Ce qu'il faut écrire.** « Aucun résultat d'entraînement ne figure dans SUMMARY.md (relu sur la source par l'instance du papier). Le dossier `results/` n'a pas pu être lu : on ne sait pas s'il en publie (rapport 4, texte intégral). »
- **Pourquoi c'est bloquant.**
  - Si `results/` contient des résultats, le danger élevé d'exp9 couvre aussi un résultat sur la comparaison des juges, pas seulement un protocole.
  - La formule du §4.4, n° 7 (« Ses entraînements ne sont pas publiés ») va déjà au-delà du §4.2 : il faut la signaler à l'instance du papier, pas la recopier.

### 3. Contribution 4 : le danger élevé de Lundqvist est appliqué à la mauvaise survie
- **Où.** corrections, l. 1014-1017. Le texte dit « Pour la survie, Lundqvist l'annonce, avec un danger élevé ». Il enchaîne sur « Il ne reste que trois choses », qui sont les trois points libres du juge.
- **Ce que disent les sources.**
  - Le §4.4, n° 6, dit élevé « pour la survie d'une mitigation du jeu d'évaluation ». Il dit libre « la survie de l'avantage des raisons et de son indépendance au regard » (passation).
  - Le rapport 4 : la survie d'un avantage propre aux raisons n'a qu'une source, Cho et al. La survie de l'indépendance au regard est annoncée par Lundqvist, non publiée (rapport 4, texte intégral, nuit, l. 971-972).
  - Le rapport 6 : la survie de l'avantage des raisons et de son indépendance au regard reste libre (nuit, l. 1539-1541).
  - corrections borne lui-même correctement ce danger élevé en l. 452 et l. 880 : la l. 1015 contredit le fichier.
- **Ce qu'il faut écrire.**
  - « La survie est partiellement prise, dans des variantes. Danger élevé de Lundqvist pour la survie d'une mitigation du jeu d'évaluation (page relue sur la source par l'instance du papier). Reste libre : la survie de l'avantage des raisons, et de son indépendance au regard, à un post-entraînement neutre ou qui paie le jeu d'évaluation (§4.4, n° 6). »
  - Rattacher « Il ne reste que trois choses » au seul juge.

### 4. Le paragraphe anglais reprend une erreur corrigée au §4.3 : Mody et al. rangés parmi les travaux de pilotage
- **Où.** corrections, l. 985 : « Steering against evaluation awareness needs controls beyond random directions (Read et al., 2026; Aranguri et al., 2026; Mody et al., 2026) ».
- **Pourquoi.**
  - Le §4.3 corrige justement ce rangement. Chez Mody et al., la suppression « se fait par l'entrée seule », avec un prompt optimisé, et non par projection (passation, §4.3). corrections le dit lui-même en l. 272.
  - Leur leçon va en sens inverse de la phrase. Un placebo aléatoire est supprimé aussi fort et déplace autant la conduite : le témoin aléatoire est donc indispensable (rapport 7, texte intégral, nuit, l. 1737 et 1742). Ce n'est pas un argument pour des contrôles « au-delà » de l'aléatoire.
- **Ce qu'il faut écrire.**
  - Retirer Mody et al. de cette phrase. Le citer à part : une suppression par l'entrée seule d'une latente de conscience d'évaluation, égalée par un placebo aléatoire.
  - Garder Read et al. : des vecteurs témoins sans rapport font autant (1er oct., l. 187 ; rapport 2, nuit, l. 346).
  - Garder Aranguri et al. : des vecteurs d'intention utilisateur font autant (1er oct., l. 460).

### 5. Le paragraphe anglais affirme sur trois travaux ce que les rapports ne disent pas
- **Où.** corrections, l. 985.
- **« These comparisons do not hold the final action fixed. »**
  - Vrai pour *Teaching Claude Why* : les réponses délibérées sont générées à neuf (rapport 1, texte intégral, nuit, l. 70).
  - Pour *Model Spec Midtraining*, le rapport dit seulement que l'identité de la réponse finale n'est pas dite (rapport 1, texte intégral, nuit, l. 98).
  - Pour Wang et al., aucun rapport ne dit rien de l'action finale.
  - À écrire : « None of them reports holding the final action fixed », ou limiter la phrase à Kutasov et al.
- **« has been reported to improve out-of-distribution alignment (… Wang et al., 2025) ».**
  - Wang et al. portent sur des jailbreaks tenus à part, « pas sur des scénarios d'alignement » (1er oct., l. 23).
  - À écrire : « out-of-distribution jailbreak robustness » pour ce travail.
- **« rank-controlled subspace ablation (Nakamura, 2026; Konrad et al., 2026) ».**
  - Le balayage du rang contre un sous-espace aléatoire de même rang est chez Nakamura (rapport 3, texte intégral, nuit, l. 569). Son contenu n'a pas été relu par l'instance du papier.
  - Konrad et al. ferment l'écart par une seule coordonnée, avec des contrôles appariés (rapport 3, texte intégral, nuit, l. 542-543 et 687).
  - À écrire : « localization with matched controls (Konrad et al., 2026) ».
- **Moins grave, dans le même paragraphe.**
  - « a neutral sentence placed before the answer » : la place de la phrase neutre n'est dans aucun rapport (nuit, l. 37-46 ; 1er oct., l. 396).
  - « list it as an uncontrolled confound » : la page range « Controlling for eval awareness » parmi les pistes futures (passation, §4.3). « Confusion non contrôlée » est la lecture du rapport 7 (nuit, l. 1606). Écrire : « list controlling for it as future work ».
  - « midtraining gains are unchanged » : voir le n° 10.

### 6. Le §7 de l'espace de travail global : « danger élevé pour l'anatomie », sans borne
- **Où.** corrections, l. 830. Dans le même sens, l. 1018 : « La présence des concepts et leur nécessité sont prises ».
- **Ce que disent les sources.**
  - Le danger est élevé pour deux sous-questions seulement, la présence des concepts avant la décision et leur nécessité. Il est moyen pour le reste de l'angle (rapport 5, texte intégral, nuit, l. 1036). Le §4.4, n° 8, borne de même.
  - Le rapport 5 juge encore libre la version sur modèles ouverts, avec un raisonnement qui précède l'action et des bras contrôlés (nuit, l. 1207-1208).
  - Le §5.5, n° 9, tient pour tenables des formulations « to our knowledge » sur d'autres sous-questions de l'anatomie.
- **Ce qu'il faut écrire.**
  - l. 830 : « Danger élevé pour la présence des concepts avant la décision et pour leur nécessité ; moyen pour le reste de l'anatomie. »
  - l. 1018 : « Danger élevé pour la présence et la nécessité (§7 : modèle fermé, réflexion après le contexte, la base pour seul témoin). La contribution se borne aux sous-questions libres et à la version contrôlée sur modèles ouverts. »

---

## 2 · Les corrections exigées, non bloquantes

**7. Un renvoi faux.**
- corrections, l. 49, renvoie à « nuit, l. 516-537 » : ces lignes sont dans le rapport 3.
- La consigne du rapport 7 est en consignes, l. 516-537.

**8. 2606.08629 : le lieu « ICML 2026, spotlight » n'est pas dans le rapport 7.**
- corrections, l. 241 et 252, l'attribue au rapport 7 (« le spotlight vient aussi du rapport 6 »).
- Pour cet article, le rapport 7 donne les auteurs, la v1, la thèse et un résultat, pas de lieu (nuit, l. 1817-1820).
- Le lieu ne vient que de deux rapports :
  - rapport 6, résumé seul : « ICML 2026, spotlight (rLFIOikFR2) » (nuit, l. 1382) ;
  - rapport 2, résumé seul : « ICML 2026 » (nuit, l. 375).
- Le §4.3 range ce lieu sous « (rapport 7) ». C'est une imprécision de la passation : la signaler, ne pas la recopier.
- Statut à écrire : « rapport 6, résumé seul ».

**9. Contribution 3 : « Elle reste libre » (l. 1013) est juste, mais incomplet.**
- C'est juste au sens du §4.4, n° 5.
- Mais les méthodes sont publiées : CAFT, *Routing Subspaces* (annexe I), Nadaf, Santos-Grueiro, BLOCK-EM.
- Et Lundqvist annonce des vecteurs de pilotage préventifs contre le jeu d'évaluation pendant le fine-tuning :
  - page relue sur la source par l'instance du papier (passation, §4.2, n° 3) ;
  - le rapport 6 le juge moyen pour le retrait (nuit, l. 1465).
- À écrire : « Libre pour un entraînement par raisons, avec test du ré-encodage. Les méthodes sont prises ; Lundqvist annonce une variante, à citer au centre. »

**10. Cho et al. : une tension avec le §4.2, non signalée.**
- Le §4.2, n° 9, relu sur la source par l'instance du papier : les bras avec et sans raisonnement sont « indistinguables après le midtraining et après le SFT ».
- Deux rapports donnent pourtant un effet juste après le midtraining :
  - rapport 1, texte intégral : l'écart de conformité vaut −0,9 contre +0,7 point, p < 0,01 (nuit, l. 114) ;
  - rapport 7, texte intégral : « le seul effet est −1,6 point d'écart de conformité » (nuit, l. 1778).
- corrections cite les deux versions (l. 116 et l. 747) sans les confronter, et le paragraphe anglais écrit « midtraining gains are unchanged ».
- À faire :
  - ranger ce point dans la partie 2 ; à relire : la table de l'écart de conformité de 2607.26654v3 ;
  - en attendant, écrire « largely indistinguishable », en nommant la mesure.

**11. « Texte intégral » ne veut pas toujours dire WebFetch (l. 42).**
- Le rapport 4 a lu la card de Fable 5 et le Risk Report par curl et pdftotext (nuit, l. 786 et 1008), et des scripts d'exp9 « en brut » (l. 755).
- Le rapport 6 a interrogé les API par curl (nuit, l. 1269).
- À écrire : « le plus souvent par WebFetch, qui résume (nuit, l. 1578) ; le rapport 4 a aussi lu des PDF par pdftotext ».

**12. La convention de numérotation d'arXiv est citée de mémoire (l. 513 et l. 669).**
- Aucune pièce ne la donne.
- Garder la vérification des quatre dates sur la page abs, mais présenter la raison comme une hypothèse de l'agent, non sourcée.

**13. Des libellés de statut hors de la liste.** La consigne impose l'un des six libellés.
- l. 534, « Rapport 2, lu par l'API markdown de LessWrong » : écrire « rapport 2, texte intégral ». Le rapport dit seulement « Lu : via l'API markdown » (nuit, l. 363).
- l. 720 et l. 837, « rapport 2, §5 » : écrire « rapport 2, texte intégral (§5 seul) » (nuit, l. 357).
- « Rapport 7 seul », « repris au §4.3 », « relu » : à garder comme précisions, mais toujours à côté d'un libellé (« rapport 7, texte intégral » ; « relu sur la source par l'instance du papier »).
- Les rapports du 1er octobre n'ont aucun libellé :
  - leur en donner un de même forme, par exemple « rapport du 1er octobre, axe …, texte intégral » ou « … lu par un site tiers » ;
  - plusieurs pages y ont été lues sur pith.science ou alphaXiv (1er oct., l. 15, 357 et 362).

**14. La date de de la Fuente et Conmy : la provenance est mal attribuée (§2.2, l. 496).**
- C'est le rapport 1 qui donne les deux dates et leur origine (nuit, l. 34) :
  - le 28 juillet, d'après OpenAlex et Semantic Scholar ;
  - le 20 août, d'après la page MATS.
- Les rapports du 1er octobre (l. 55 et 395) et le rapport 4 (l. 880) donnent le 28 juillet sans dire d'où.
- Ajouter aussi 1er oct., l. 55.

**15. Kretschmar, « la réduit » (l. 809) : une contradiction entre rapports, pas une correction établie.**
- Les rapports du 1er octobre écrivent :
  - « efface » (l. 201 et 277) ;
  - « supprime » (l. 390).
- Le rapport 3 écrit « réduit » (texte intégral, « page complète », nuit, l. 616).
- À ranger dans la partie 2, ou à marquer « rapport 3, texte intégral ».
- Les chiffres du rapport 4 (14 % → 3 %) portent sur les annotations de type, donc sur la conduite, pas sur la verbalisation (nuit, l. 873).

**16. Opus 4.7 et Fable 5 : l'inhibition y est faite, pas seulement « formulée ».**
- **La card d'Opus 4.7** (l. 706-708, qui listent les inhibitions déjà faites, et l. 719, « formulée »).
  - Elle inhibe trois vecteurs, contre des paires contrastives sans rapport, et le désalignement monte (rapport 2, texte intégral de la section, nuit, l. 339).
  - Ce qui n'y est que formulé, c'est le lien avec un type d'entraînement (nuit, l. 340).
- **La card de Fable 5, §6.5.1.2.**
  - L'inhibition de la conscience de l'évaluation y fait monter une conduite désalignée liée au vecteur « Alignment Faking ».
  - Le contrôle : cinq vecteurs témoins, à dégradation négligeable.
  - Source : rapport 4, texte intégral (nuit, l. 798 et 981).
- **À faire.**
  - Ajouter les deux cards à la liste de l. 706-708.
  - Le §4.4, n° 2, dit « formulée » : le préciser, sans le contredire.

**17. Des dates et des versions sans source.**
- l. 749, Cho et al., v1 du 29 juillet et v3 du 18 août : rapports 1, 4 et 7 (nuit, l. 103, 804 et 1760).
- l. 854, Read et al., 10 avril 2026 : 1er oct., l. 186 ; rapport 2, nuit, l. 344.
- l. 855, Aranguri et al., 4 mai 2026 : 1er oct., l. 193 ; rapport 6, nuit, l. 1438.

**18. La partie 11 : « Fait » est trop fort (l. 1020-1021).**
- **N° 2.** Il demandait aussi si le dépôt relève du projet SPAR. Ce n'est pas établi : le rapport 4 dit « c'est une inférence » (nuit, l. 783).
- **N° 3.** Il demandait une relecture sur arXiv. Le rapport 7 a lu par WebFetch, qui résume, et l'instance du papier n'a rien relu. Écrire : « fait par le rapport 7, non relu ».
- **l. 698.** Même remarque. Ajouter aussi le n° 15 (Mody et al.) à « n° 25 à 29 ».

**19. Les sigles du programme, au-delà de la colonne « Distance ».**
- La partie 3 fait nommer en clair les axes (l. 692) et la colonne « Distance » (l. 884). Elle oublie les autres sigles de la partie 1 :
  - « La lecture B » (programme, l. 71) ;
  - les colonnes C1 à C4 (l. 76) ;
  - « Base de comparaison en P4 » (l. 93) ;
  - « le modèle de notre mesure M7 » (l. 94) ;
  - « pertinent pour P7 » (l. 95) ;
  - « nos phases P6 et P7 » (l. 108) ;
  - « P8 » (l. 115).
- Les noms en clair, d'après l'annexe A de la passation : l'hypothèse du regard ; le retrait pendant l'entraînement ; la trajectoire de « je suis évalué » ; les raisons notées par un juge ; la survie ; l'anatomie.
- C'est la règle de Lazar (passation, §1).

**20. *Metagaming matters* : la colonne « observationnel » (programme, l. 86) est à compléter.**
- Les rapports du 1er octobre y voient un essai de pilotage contrastif entre évaluation et déploiement, « aux résultats mitigés » (1er oct., l. 132 et 364).
- corrections, l. 772-774, ne le reprend pas.

**21. De petites inexactitudes.**
- **l. 908, Nguyen et al.** Ils n'ont pas « les mêmes modèles que le programme », à la lettre. Ils fine-tunent les bases Llama-3.1-8B, Gemma-2-9B et Qwen3-8B (rapport 5, texte intégral, nuit, l. 1067), alors que le programme part de Llama-3.1-8B-Instruct.
- **l. 295, n° 17.** La consigne de l'agent 2 n'était pas fausse : elle parlait d'un billet « qui rapporterait l'effet d'une suppression » (consignes, l. 159), et c'est ce que fait le billet. La correction porte seulement sur l'auteur de la suppression.
- **l. 60 et l. 1035, la réponse de Lazar sur les contacts.**
  - Elle n'est dans aucune pièce : la passation (§3, point 4) dit encore « sans réponse ».
  - Elle concorde avec sa réponse du 2 octobre (« non pas encore ») : ajouter cette source.
  - Rien dans corrections ne propose d'écrire à Cadile ou à Lundqvist : c'est conforme.

---

## 3 · Les manques

Chacun de ces travaux est dans un rapport. Il manque à corrections, ou à la place où il devrait y figurer. Ils sont classés par angle, les plus importants d'abord.

### La survie
- ***Shallow Beliefs*** (Jose, Stastny ; arXiv 2609.14998, 14 septembre 2026). Source : rapport 4, résumé seul (nuit, l. 895).
  - Un midtraining, puis un RL qui paie le hacking.
  - Le rapport 4 y voit « le plan publié le plus proche d'une phase qui récompense le jeu ».
  - Le §4.4, n° 6, le cite. Il manque aux lignes à ajouter (l. 812-851) et à la liste de la survie (l. 979).
- ***Stress Testing Deliberative Alignment*, §8.** Source : rapport 4, texte intégral du §8 (nuit, l. 818-828), danger moyen.
  - Une sûreté entraînée par raisonnement sur une spécification survit-elle à un RL de capacités ?
  - Le §4.4, n° 6, le cite. corrections ne lui donne pas la colonne survie (l. 822), et la liste de l. 979 l'omet.
- ***Training a Misaligned Reward Seeker*** (Qi … Hubinger, Anthropic, août 2026). Source : rapport 6, texte intégral parcouru par mots-clés (nuit, l. 1339-1345), danger moyen à faible.
  - Les auteurs envisagent un gain « due to increased evaluation awareness ».
  - Ils observent au contraire une baisse de la conscience verbalisée.
  - Il touche la dépendance au regard et la survie.

### Les raisons pour le juge
- **Le Risk Report d'août 2026 et le modèle « Hacker-Opus »** (Anthropic). Source : rapport 4, texte intégral (nuit, l. 896-898).
  - Il donne la part des épisodes où le raisonnement a été exposé au calcul de la récompense.
  - La conscience d'être noté monte avec le reward hacking.
  - Le verdict du rapport 4 le range parmi ce qui prend en partie la question « la conduite dépend-elle de "je suis noté" » (nuit, l. 976).
- **Maniyar et al.** (2608.15445, atelier COLM 2026). Source : rapport 6, résumé seul (nuit, l. 1434-1437).
  - Le raisonnement se découple de la réponse.
  - Travail adjacent, nommé dans le verdict du rapport 6 (l. 1543).

### Le retrait pendant l'entraînement
- **Imran … Africa, *Consistency Training while Mitigating Obfuscation via Rate Matching*** (2606.02211).
  - L'entraînement à l'invariance fait taire l'indice sans retirer son influence.
  - Sources : rapport 3, résumé seul (nuit, l. 629) ; rapport 4 (l. 984) ; rapport 6, résumé du billet (l. 1377-1380).
  - Le §4.4, n° 5, le cite. Il manque aux l. 848-851 et 967-975.
- **Des annonces à surveiller.**
  - Le programme de Resolution (Irving et Africa) veut intervenir sans pousser le mauvais comportement dans d'autres dimensions : c'est la question du ré-encodage (rapport 3, nuit, l. 667).
  - Le flux MATS de David Africa (rapport 6, nuit, l. 1487), danger faible à moyen.
- **Montoya et al.** (atelier ICML 2026). Sources : rapports 4 et 6, résumé seul (nuit, l. 905 et 1404-1407).
  - Une fois la verbalisation retirée, un écart de conduite de +7,0 points subsiste.
  - Travail adjacent au ré-encodage.

### La dépendance au regard et l'amplification
- ***Building Comparative Motivation Profiles*** (Vella Zarb … Feng, 2606.08243).
  - Il pilote le suivi des attentes des chercheurs, contre des vecteurs aléatoires de même norme.
  - Le rapport du 1er octobre (axe du test causal) le juge en recouvrement « partiel » (1er oct., l. 245-251).
  - corrections ne le traite que pour ses auteurs (n° 13).
- ***Towards training-time mitigations for alignment faking in RL*** (Gasteiger … Hubinger, Anthropic, décembre 2025). Source : 1er oct., l. 157-162, recouvrement « partiel ».
  - La question : le gain tient-il quand le modèle se croit non surveillé ?
  - Il est absent du programme et de corrections.
- **L'appel d'Ivanov.** Sources : rapport 6, texte intégral par l'API (nuit, l. 1358-1369) ; rapport 3 (l. 668).
  - Il propose de varier le format de l'entraînement constitutionnel, puis de mesurer la conscience d'évaluation qui en résulte : l'amplification, annoncée comme direction de recherche.
  - Le §4.4, n° 3, le cite. La liste de l'amplification (l. 978) l'omet, comme la card de Sonnet 4.5, également citée au §4.4, n° 3.
- ***When Is a Probe Monitor Safe to Act On?*** (Gaya … Gupta, atelier AIW 2026). Source : rapport 4, résumé seul (nuit, l. 903).
  - Une sonde évaluation/déploiement sur Llama-3.1-8B-Instruct, suivie pendant un RL à récompenses vérifiables.
  - Utile pour la sonde suivie de point de contrôle en point de contrôle.
- ***Evaluation Awareness in Language Models Has Limited Effect on Behaviour*** (Knecht … Hagendorff, 2605.05835).
  - Sources : rapport 2, résumé seul (nuit, l. 380) ; rapport 6, résumé seul (l. 1420-1422), qui le donne en spotlight à NeurIPS 2026.
  - Une contre-preuve au niveau verbal.

### L'anatomie
- ***Risky Business*** (Meier … Gipp, 2608.03745). Source : rapport 5, résumé seul (nuit, l. 1095-1104).
  - Danger moyen pour la question « l'action suit-elle une raison imposée ? ».
  - Avec Hao et al. et Macar et al., il fait dire au rapport 5 que cette sous-question est « partiellement prise en général » (nuit, l. 1213).
  - corrections la donne libre « après un entraînement par raisons » (l. 923). C'est juste, mais ces voisins ne sont pas nommés.
- **Mazaheri** (2608.15022). Source : rapport 5, texte intégral, sections 2.1 et 8 (nuit, l. 1106-1115).
  - Le rapport 5 en fait « une mise en garde à citer au centre » : la charge ne se lit pas comme une influence causale.
  - C'est le voisin direct de la question du rang en fonction de la charge.
- **Pando** (Zhong … Raghunathan, 2604.11061). Source : rapport 5, résumé seul (nuit, l. 1151-1154).
  - L'organisme le plus proche du cas positif visé.
  - C'est le voisin de l'organisme à mot inventé (l. 1216).

### Raisons contre actions
- ***Synthetic Persona Pretraining*** manque aux lignes à ajouter au tableau (l. 812-851).
  - Le rapport du 1er octobre le range, sur cet axe, en recouvrement « partiel » (1er oct., l. 25-29).
  - Le programme ne l'a que dans sa partie 11.
- **Des travaux adjacents, à citer.**
  - *Conditional misalignment* (Dubiński … Evans ; 1er oct., l. 73-77) : la chaîne de pensée à l'entraînement réduit le désalignement conditionnel. Le rapport 6 le donne à NeurIPS 2026, sur le seul titre (nuit, l. 1514).
  - *An Embarrassingly Simple Defense…* (1er oct., l. 267-273), qui motive le cas positif en distribution.
  - *Not Just the Destination…* (1er oct., l. 425-429).

### La partie 2
- La tension entre le §4.2 et les rapports 1 et 7 sur l'écart de conformité de Cho et al. après le midtraining (n° 10).
- La contradiction « efface / réduit » sur Kretschmar (n° 15).

---

## 4 · Ce qui a été vérifié et tient
- **Les renvois.** Les renvois contrôlés aux rapports du 1er octobre, aux rapports de la nuit, au programme, aux consignes et aux fiches sont exacts, sauf l. 49.
- **Le §4.3.** Ses corrections sont toutes reportées. Aucune n'est reprise à l'envers, sauf Mody et al. dans le paragraphe anglais (n° 4).
- **Les verdicts du rapport 6.** Contredits par les rapports 3, 4 et 5, ils sont correctement tranchés par le §4.4 (l. 448-451).
- **Les calculs.** Ils sont justes et marqués comme calculs du fichier : l. 321 (18 et 5,5), l. 478 (0,53), l. 583 (+21,1 et +14,7).
- **Les niveaux de danger.** Ils suivent les rapports et la définition des consignes pour :
  - Cadile, moyen ;
  - exp9, élevé dans sa variante ;
  - Lundqvist, élevé pour la survie d'une mitigation (l. 452 et l. 880) ;
  - Wu et Tang, faible.
