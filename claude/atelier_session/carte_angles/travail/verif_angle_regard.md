# Vérification de « angle : la dépendance au regard » (`travail/angle_regard.md`)

Vérification sceptique, 2 octobre 2026. Les numéros de ligne renvoient à `angle_regard.md`.

**Ce que j'ai relu moi-même.**
- Les rapports du 1er octobre en entier, lignes 1 à 489.
- Les sept rapports de la nuit, en entier, lignes 1 à 1850.
- La passation v1.2 en entier, dont le §4 et les annexes.
- Les consignes de l'agent 2, lignes 90 à 179.
- La partie 1 du programme v1.1, lignes 60 à 130.

**Le web.** Huit recherches WebSearch. Rien n'a été ouvert : tout ce qui en vient est « vu par extrait de recherche, non ouvert » et ne fournit aucun chiffre.

**Bilan.**
- Le gros du fichier est fidèle aux sources : dates, chiffres, corrections du §4.3, citations de moins de quinze mots, aucun sigle d'idée, jamais « first ».
- Quatre corrections sont bloquantes : trois touchent ce que le fichier dit déjà pris, une touche ce qu'il dit libre.
- S'y ajoutent des statuts de lecture faux ou hors libellés, des niveaux de danger incohérents avec les définitions, et une dizaine de travaux présents dans les rapports mais absents du fichier.

---

## A. Corrections bloquantes

### 1. *Stress Testing Deliberative Alignment* est rangé à tort parmi « la dépendance d'un gain d'entraînement » (l. 20)
**Le problème.**
- Le §4.2 n° 6 (relu sur la source par l'instance du papier) dit le contraire. Les interventions sur la chaîne de pensée portent sur o3 avant l'entraînement anti-manigance. Elles ne disent pas si cet entraînement change le lien causal : « does not inform us whether anti-scheming training changes this causal relationship ».
- Le fichier le dit lui-même aux lignes 75 à 79 et 86. La ligne 20 se contredit déjà : « avant l'entraînement ».

**À faire.**
- Déplacer ce travail dans « la dépendance de la conduite en général ».
- Ne garder sous « la dépendance d'un gain d'entraînement » que la fiche Sonnet 4.5, en marquant que la comparaison des deux instantanés vient du seul rapport 2 (non relue ; seule la phrase « a portion, but not all » l'est, §4.2 n° 5).

### 2. Cho et al. : une différence entre bras, juste après le midtraining, est donnée pour un fait, contre le §4.2 n° 9 (l. 21, 99, 101, 308, 347, 354)
**Ce que disent les sources.**
- **Relu (§4.2 n° 9) :** « avec et sans raisonnement délibératif, les bras sont indistinguables après le midtraining et après le SFT ».
- **Rapport 1 :** −0,9 contre +0,7 point d'écart de conformité surveillé / non surveillé après midtraining, p < 0,01 (l. 114). Ce rapport a lu le HTML « par extraction » et la revue tierce pith.science (l. 104). Le p < 0,01 ne se trouve que dans ce rapport.
- **Rapport 7 :** « Le seul effet est −1,6 point d'écart de conformité, juste après le midtraining », sans valeur de p (l. 1778). L'outil de ce rapport résume le texte au lieu de le rendre tel quel (l. 1578).
- **Rapport 4**, absent de la contradiction n° 2 du fichier : « indistinguables presque partout » (l. 809). Il note aussi « Pas de mesure de la dépendance au regard » (l. 816).

**Le défaut.** La phrase de la ligne 371 (« Le §4.2 vise sans doute les mesures agrégées et le chantage ») est une conjecture. Elle retourne la règle : un fait relu prime sur un rapport.

**À faire.**
- Ligne 99, écrire : « relu : bras indistinguables après le midtraining et après le SFT (§4.2 n° 9) ; rapports 1 et 7 : écart de conformité surveillé / non surveillé de −1,6 point juste après le midtraining, non relu ; rapport 4 : pas de mesure de la dépendance au regard ».
- Supprimer la conjecture de la ligne 371. Ajouter le rapport 4 à la contradiction n° 2.
- Rendre conditionnels à la relecture de la table :
  - le classement de Cho et al. comme variante comportementale (l. 21 et 101) ;
  - son ajout à la liste du §4.4 (l. 24 et 101 : « à y ajouter après relecture », comme pour la fiche Fable 5) ;
  - la raison de la formulation tenable n° 3 (l. 347) ;
  - la formulation intenable de la ligne 354.
- Le niveau moyen peut rester, sous cette condition.

### 3. La raison donnée pour la formulation centrale est fausse telle qu'écrite (l. 23 et 345)
**Les deux phrases.**
- Ligne 345 : « les travaux qui entraînent sur des raisons ne mesurent pas la conscience d'évaluation, et ceux qui l'inhibent n'entraînent pas sur des raisons ».
- Ligne 23 : une liste de travaux qui ne mesurent pas cette conscience, dont Stress Testing est exclu.

**Ce qui les contredit, dans les sources mêmes du fichier.**
- *Stress Testing Deliberative Alignment* entraîne par raisonnement sur une spécification. Il mesure la conscience verbalisée, de 0,9 % à 5,5 % pour o4-mini (rapports 1 et 6, texte intégral), et l'édite dans la chaîne de pensée (relu, §4.2 n° 6).
- L'article sur l'espace de travail global entraîne par principes (relu, §4.2 n° 2). Dans le même article, il ablate la conscience d'évaluation (rapports 2, 3 et 5, texte intégral). Certes, pas sur le même modèle.
- *Training a Misaligned Reward Seeker* mesure la conscience verbalisée après un entraînement d'alignement (rapport 6, texte intégral parcouru par mots-clés).
- Cho et al. mesurent un écart surveillé / non surveillé, selon les rapports 1 et 7 (contesté, voir n° 2).

**Pourquoi c'est bloquant.** Un relecteur réfuterait cette phrase avec les travaux que le fichier cite lui-même.

**À faire.** Écrire plutôt : « aucun ne lit par une représentation interne, ni n'inhibe, la conscience d'évaluation dans des modèles entraînés par raisons comparés à des modèles entraînés sur les mêmes actions ». Ajouter Stress Testing et l'espace de travail global à la liste de la ligne 23, avec ce qu'ils font.

### 4. Un élément « libre » est trop fort : « Le faire sur modèles ouverts entraînés pour l'occasion » (l. 309)
**Ce qui le contredit.**
- Le fichier cite lui-même un organisme ouvert entraîné pour l'occasion et inhibé : Hua et al., 49B (rapport 7, texte intégral ; §4.3).
- *Routing Subspaces* entraîne des LoRA sur des modèles ouverts de 2 à 9B, dont Llama-3-8B, puis retire la coordonnée évaluation / déploiement (rapports 2 et 3, texte intégral ; annexe I relue, §4.2 n° 7).
- Vu et al. utilisent un organisme fine-tuné, avec pilotage combiné à l'ablation (rapports 2, 3 et 6, résumé seul).

**À faire.**
- Ligne 309, écrire : « sur modèles ouverts entraînés pour l'occasion à une conduite d'alignement, par raisons et par les mêmes actions ».
- Même défaut à la ligne 15 : « par inhibition interne (Anthropic, sur modèles fermés) » omet les inhibitions sur modèles ouverts que les lignes 309 et 352 recensent. Les ajouter.

---

## B. Corrections requises, non bloquantes

### Statuts de lecture

5. **Des libellés hors liste.** Il faut ramener chaque statut à l'un des six libellés, avec la précision entre parenthèses au besoin. Écarts relevés :
   - « texte intégral par extraction » (l. 76, 96) ;
   - « texte intégral par l'API de LessWrong » (l. 142) ;
   - « lecture partielle par l'API de LessWrong » (l. 180) ;
   - « texte intégral parcouru par mots-clés » (l. 201) ;
   - « rapport 5 (par résumé de l'outil) » (l. 324). Le rapport 5 dit avoir lu la page de recherche d'Anthropic par résumé de l'outil (l. 1185, 1204).
   - L'abréviation « relu », définie en tête de fichier, doit devenir dans la carte « relu sur la source par l'instance du papier ».

6. **« Texte intégral » attribué aux rapports du 1er octobre, qui ne le disent pas.**
   - Les rapports du 1er octobre donnent l'URL ouverte, sans l'étendue de la lecture. Lignes concernées :
     - Redwood, l. 142 ;
     - Read et al., l. 180 ;
     - Vella Zarb, l. 206 ;
     - Kretschmar, l. 219 ;
     - Gasteiger, l. 227 ;
     - Aranguri, l. 231.
   - Ne pas écrire « texte intégral » quand le rapport ne le dit pas. Pour Read et al., la seule lecture qualifiée est celle du rapport 2 : « via l'API markdown, partiellement » (l. 345).
   - Le rapport du 1er octobre sur la condition des gains a lu *Generalization Hacking* par pith.science (l. 137), donc par un site tiers. Le rapport 7 l'a relu ensuite (l. 1715).

7. **Hua et al. (l. 168 à 172).** Le statut « rapport 7, texte intégral » ne couvre pas le résultat du pilotage.
   - Le §6 du rapport 7 (l. 1797 à 1812) décrit l'organisme, les adaptateurs, les documents et la limite de la fiche du modèle. Il ne dit rien du pilotage.
   - « Un vecteur de pilotage supprime cette conduite » vient du rapport 6, résumé seul (l. 1334-1335), et du titre.
   - Les annotations de type en évaluation viennent du rapport 6 et du §2 du rapport 7, sur *Eval Cooperativeness* (l. 1626).
   - Corriger le statut en conséquence.

8. ***Steering Awareness* (2511.21399) n'est pas « non ouvert par aucun rapport » (l. 279).** Le rapport 3 le range parmi les travaux « partiellement lus » (l. 680). Le rapport 2 en a corrigé le titre, la version et le lieu (l. 391), repris au §4.3.

9. **Le titre du projet SPAR de Qiyao Wei, *Empirical Evaluations of Situational Awareness* (l. 325), ne figure dans aucune pièce.**
   - Je ne l'ai trouvé que comme titre de page sparai.org, dans un extrait de recherche. Le marquer « vu par extrait de recherche, non ouvert », ou le retirer.
   - Une contradiction n'est pas signalée. Le rapport 2 date la proposition du 10 décembre 2025 (« créée le », l. 404). Le rapport 3 la décrit « sans auteur ni date » (l. 669). La date du §4.4 est celle du rapport 2.

10. ***Improving CoT Monitorability of Evaluation Awareness via Verbalization Training* (l. 273 et 425) est très probablement un doublon de *Training LLMs to Verbalize Evaluation Awareness*.** Ce dernier est Anwar … Krueger, 2609.36316, déjà listé à la ligne 261.
    - Un extrait de recherche le présente comme le billet-lien d'un article arXiv, coécrit avec Sahar Abdelnabi et David Krueger (vu par extrait de recherche, non ouvert).
    - Or le rapport 2 donne Anwar, Abdelnabi et Krueger pour 2609.36316 (l. 392). L'extrait annonce le même facteur multiplicatif que le rapport 4 (l. 904) ; aucun chiffre n'en est tiré.
    - Fusionner les deux entrées, ou marquer « doublon probable ». Retirer l'entrée de la liste « à ouvrir pour la première fois ».

### Niveaux de danger

11. **Qiyao Wei : « faible à moyen » (l. 325) n'est pas cohérent avec les définitions.**
    - La passation dit que ce projet « pose la question des raisons ou du regard » (§3, point 4), et que sa proposition « a bien posé la question » (§4.4).
    - Le fichier écrit lui-même que « Le papier dira qu'elle a posé la question » (l. 419) : c'est la définition de « moyen », à citer au centre.
    - Passer à moyen. L'élevé ne s'applique pas : rien n'est publié, et la question ne porte pas sur l'avantage des raisons.

12. **Korbak et al. : « faible, mais à citer au centre » (l. 193) contredit les définitions,** puisque « à citer au centre » définit le niveau moyen. Choisir l'un ou l'autre.
    - Par cohérence avec Redwood (moyen, pour le cadrage, l. 147), je recommande moyen. Ce travail énonce l'hypothèse du regard pour un midtraining dont tous les bras contiennent des raisons (rapport 7 et §4.3).

13. **À harmoniser avec OpenAI 2606.24014,** classé moyen comme variante comportementale (l. 135).
    - **Gasteiger et al. (l. 226-229)** compare plusieurs mitigations d'entraînement sur l'écart surveillé / non surveillé, manipulé par prompt. Le rapport du 1er octobre le juge en recouvrement partiel (l. 157 à 162). Classé faible ici sans autre raison que « pas un comportement de sûreté ».
    - ***Training a Misaligned Reward Seeker* (l. 200-204)** : le rapport 6 le range en « danger moyen à faible », pour la dépendance au regard (l. 1322, 1339-1345).
    - **Vella Zarb et al. (l. 205-208)** : pilotage contre des vecteurs aléatoires de même norme, recouvrement partiel selon le rapport du 1er octobre (l. 248 à 250).
    - Les passer à « faible à moyen », ou justifier l'écart.

### Faits, attributions et contradictions

14. ***Teaching Claude Why* (l. 249) : attribution mêlée, et un faux ami.**
    - « C'est ce vide qui rend l'angle publiable » est une phrase du rapport 2 (l. 387). Elle porte sur l'absence de mesure de la conscience d'évaluation, pas sur les pots de miel.
    - Le rapport 1 écrit que les pots de miel sont « conçus pour ressembler au jeu d'évaluation » (l. 71). « Jeu » y désigne l'ensemble d'évaluation, alors que le fichier emploie « jeu d'évaluation » au sens de *eval gaming* (l. 144, 220).
    - Écrire : « conçus pour ressembler aux évaluations (rapport 1) », et attribuer la seconde phrase au rapport 2.

15. **Heidari et al. cités comme inhibition sur Qwen3-8B (l. 352).**
    - Les rapports donnent des sondes sur six modèles ouverts, dont Qwen3-8B (rapport 6, l. 1305). Ils donnent aussi un pilotage aux étapes d'OLMo, mesuré sur la verbalisation seule (rapport 6, l. 1306 et 1309 ; rapport du 1er octobre sur le test causal interne, l. 291).
    - Aucun rapport ne dit que l'inhibition a été faite sur Qwen3-8B. Retirer « (Qwen3-8B) ».

16. **Huang et al., *Dissociating Evaluation Awareness from Sandbagging* (l. 257 et 355) : les deux lectures, toutes deux sur résumé seul, divergent.**
    - Le rapport 2 le range parmi les « contrôles placebo et aléatoires qui reproduisent l'effet du pilotage » (l. 376 à 378).
    - Le rapport 6 parle d'un pilotage contrôlé par des directions aléatoires appariées et par la dégradation des sorties (l. 1398).
    - Ajouter cette contradiction. La formulation intenable de la ligne 355, qui s'appuie sur Huang et al., doit le dire.

17. **Aranguri et al. (Goodfire, l. 230-233) : il manque la réserve sur les contrôles,** donnée par le rapport du 1er octobre sur la combinaison exacte (l. 460) et reprise par la v1.1. Des vecteurs d'intention de l'utilisateur réduisent la verbalisation autant que les vecteurs évaluation / déploiement. C'est une objection de même nature que Read et al.

18. **Contradiction n° 1 (l. 362-366).** Le rapport 6 n'a lu l'article sur l'espace de travail global que par le résumé de Hugging Face (l. 1326). Son « pas de contrôles appariés » pèse donc peu face à la lecture intégrale du §5.1 et de l'annexe A.21 par les rapports 2 et 3. Le dire.

19. **Fiche Sonnet 4.5 (l. 51) : « le seul témoin est le tirage de traits aléatoires ».** Le rapport 2 décrit ce témoin (l. 291) sans dire qu'il est le seul. Écrire « le témoin rapporté ».
    - La ligne 63 (« Une seule expérience de plus… prendrait l'essentiel de l'angle ») est une inférence de l'auteur, pas un fait de rapport : la marquer comme telle.

20. **Dates incohérentes avec l'identifiant arXiv, non signalées.**
    - Singh … Chaudhary : « 20 août 2026 », pour 2609.22119 (rapport 6, l. 1426), comme pour *Routing Subspaces*.
    - Deckenbach et al. : « v2 du 7 septembre 2026 » selon le rapport 2 (l. 374), « HTML v4 du 7 septembre 2026 » selon le rapport 7 (l. 1745).

21. **Contradiction n° 11 (l. 395-402).** La v1.1 cite déjà, dans sa table de la partie 1 :
    - l'écart surveillé / non surveillé de Cho et al. (« écart surveillé/non surveillé, par prompt », l. 80 du programme) ;
    - *Metagaming matters* (l. 86 du programme).

    Ce qui leur manque, c'est leur place dans le verdict (l. 71) et dans le paragraphe de travaux connexes (l. 128).

### Sources des décisions et des dates

22. **La ligne de Lundqvist (l. 326).**
    - Les dates de la cohorte (14 septembre – 14 décembre, démonstration le 19 décembre) viennent de la FAQ de SPAR : rapport 6, l. 1450, et §4.4 (« lue par deux agents »). Elles ne viennent pas du §4.2 n° 3, qui ne relit que le contenu de la page.
    - « Pas de contact pour l'instant » s'accorde avec la réponse de Lazar transmise avec cette tâche (« non pas encore »). La passation v1.2 disait « sans réponse » (§3, point 4). Citer cette réponse comme source.
    - Ne proposer aucun moment de contact, ni pour Lundqvist ni pour Cadile (l. 330).

---

## C. Manques : travaux présents dans les rapports et absents du fichier

1. ***Metagaming matters for training, evaluation, and oversight*** (Schoen … Nitishinskaya, blog Alignment d'OpenAI, 16 mars 2026). C'est le manque le plus net.
   - **Pourquoi il compte :** c'est un repère que la consigne de l'agent 2 désignait pour cet angle (consignes, l. 157). Le rapport du 1er octobre sur la condition des gains le classe deuxième, en recouvrement partiel (l. 129 à 134). La v1.1 le cite.
   - **Ce qu'il fait :** là où méfaits et métajeu baissent ensemble, les auteurs ne départagent pas un alignement réel d'un métajeu non verbalisé. Un pilotage contrastif évaluation / déploiement y donne des résultats mitigés (rapport du 1er octobre sur la condition des gains, l. 131-132 ; sur la combinaison exacte, l. 364).
   - **Statuts :**
     - rapport 2, texte intégral (l. 369) ;
     - rapport 6, résumé seul (résumé automatique, l. 1443) ;
     - rapport du 1er octobre sur la condition des gains (étendue non précisée).
   - **À faire :** le classer « faible à moyen », et l'ajouter aux énoncés de l'hypothèse (l. 22 et 353).

2. **Autres énonciateurs de l'hypothèse, à ajouter à la formulation intenable de la ligne 353 :**
   - *Training a Misaligned Reward Seeker* (rapport 6) ;
   - Cho et al., « cannot rule out … eval-awareness » (relu, §4.2 n° 9) ;
   - l'appel d'Ivanov (point 5 ci-dessous).

3. ***The Hawthorne Effect in Reasoning Models*** (2505.14617 ; OpenReview ccPts3Df2q).
   - **Où il apparaît :**
     - rapport 2, parmi les méthodes de pilotage et de validation (l. 383) ;
     - « lus aussi » par le rapport du 1er octobre sur le test causal interne, sans description (l. 332) ;
     - non ouvert par deux autres rapports du 1er octobre (l. 215, 474).
   - **Ce que j'en sais :** d'après un extrait de recherche (non ouvert), il pilote la conscience d'être testé sur des modèles de raisonnement ouverts d'environ 32B, et mesure l'effet sur la conformité nocive. C'est pertinent pour la formulation intenable de la ligne 352.
   - **À faire :** l'ajouter, faible, à relire.

4. ***Evaluation Faking*** (OpenReview mPaHEZFLi2 ; rapport 2, l. 384) et ***Evaluation Awareness Is Not One Capability*** (2606.23583). Pour ce second, la détection tient surtout au réglage d'instructions : rapport 2, résumé seul (l. 379). Il figure aussi parmi les « lus aussi » d'un rapport du 1er octobre (l. 333). À ajouter aux résumés seuls.

5. **L'appel d'Igor Ivanov,** *Call for Science of Eval Awareness*, 25 décembre 2025, et *Better evals are not enough…*, 29 janvier 2026.
   - **Ce qu'il propose :** supprimer la conscience d'évaluation par pilotage, faire varier le format de l'entraînement constitutionnel, et mesurer la conscience d'évaluation qui en résulte.
   - **Statuts :** rapport 3 (l. 668) ; rapport 6, texte intégral (l. 1358-1369) ; rapport du 1er octobre sur la combinaison exacte (l. 467).
   - **À faire :** l'ajouter aux projets annoncés, faible à moyen, avec ses dates. Le fichier ne cite Ivanov que pour son projet SPAR.

6. **Le projet SPAR du printemps de LawZero** (Fornasiere, Bronzi).
   - **Pourquoi il compte :** la consigne de l'agent 2 le rendait prioritaire, à égalité avec Qiyao Wei (consignes, l. 145).
   - **Ce que dit le rapport 2 (l. 412-417) :** rien sur les mitigations par documents synthétiques ni sur les organismes de conscience d'évaluation. Une seule sortie est connue, 2604.17465, sur la reconnaissance du bruit appliqué aux activations.
   - **À faire :** l'ajouter au tableau, avec « rien publié sur la question ».

7. ***Consistency Training while Mitigating Obfuscation via Rate Matching*** (Imran … Africa, 2606.02211).
   - **Ce qu'il montre :** l'entraînement à l'invariance aux indices fait taire la verbalisation de l'indice, sans retirer son influence.
   - **Statuts :** rapport 6, résumé seul (l. 1377-1380) ; rapport 4 (l. 984) ; rapport 3, résumé seul (l. 629).
   - **À faire :** l'ajouter, faible. C'est une mise en garde de plus contre une mesure verbale.

8. ***Evaluation-Conditioned Training*** (Harris – Hao, 2608.10209).
   - **Ce qu'il fait :** il conditionne l'entraînement sur des descriptions de l'évaluateur, par LoRA, sur Llama-3.1-8B-Instruct, le modèle du programme (rapport 1, l. 167 ; rapport du 1er octobre sur la condition des gains, l. 221).
   - **À faire :** l'ajouter, faible. La passation le cite déjà pour les graines (§5.4, n° 1).

9. ***Conditional misalignment*** (Dubiński … Evans, 2604.25891).
   - **Ce qu'il fait :** des mitigations cachent un désalignement qui revient sous des indices du contexte d'entraînement, et une chaîne de pensée ajoutée à l'entraînement le réduit (rapport du 1er octobre sur raisons contre actions, l. 73 à 77).
   - **À faire :** l'ajouter, faible. Le rapport 6 le signale accepté à NeurIPS 2026 (titre seul, l. 1514).

10. **Travaux adjacents, faibles :**
    - le projet SPAR de Sohan Venkatesh (LASR), sur l'effet de la croyance d'être observé sur la verbalisation (rapport 6, l. 1474) ;
    - *Norms at a Price* (2609.07627), un argument conceptuel sur la conformité conditionnelle (rapport 6, l. 1440 ; ouvert en résumé par le rapport 2, l. 308) ;
    - les modèles « deployment-mo » de stanleytheli, sur Hugging Face, à fiches restreintes (rapport 5, l. 1190).

11. **Travaux non ouverts, absents de la liste des lignes 267 à 286 :**
    - billets vus par le rapport 2 (l. 443) :
      - *Calibrating alignment evals* ;
      - *Can Models be Evaluation Aware Without Explicit Verbalization?* ;
      - *Better evals are not enough…* ;
      - *Opus 4.6 Reasoning Doesn't Verbalize Alignment Faking…* ;
    - le chiffre de conscience d'évaluation de *SFT Drives Gemini's Safety Properties* (Engels et al. ; figures non lues, rapport 2, l. 442) ;
    - LURE (2605.26438) ;
    - vus par le rapport du 1er octobre sur la condition des gains (l. 214 à 217) :
      - *Realistic honeypot evaluations for scheming propensity* (2605.29729) ;
      - *A Framework for Eval Awareness* ;
      - *Rephrasing Reduces Eval Awareness* ;
      - *Avoiding steering awareness by optimizing steering parameters*. Ce dernier est à mettre à côté de *Steering Awareness* : c'est la même menace pour l'inhibition.

12. **Détails utiles omis :**
    - **Kretschmar (l. 218-221).** D'après le rapport 4 (texte via WebFetch), ce qui persiste chez RogueQwen est la sycophancie (l. 874), pas le « jeu d'évaluation ». Les chiffres du rapport 4 sont ceux-ci :
      - annotations de type de 14 % à 3 % chez l'organisme de Hua et al. (l. 873) ;
      - sycophancie de RogueQwen à 86-89 % (l. 874).
    - **Mody et al.** La direction placebo déplace aussi le comportement autant que la vraie. Le neurone visé est corrélé mais non causal (rapport 7, l. 1737, 1741).

13. **Réserves sur le « libre » (l. 314-316), à compléter :**
    - le blog de Redwood est refusé par robots.txt (rapport 6, l. 1509) ;
    - LessWrong n'a été lu que par son API ;
    - dans l'environnement de cette tâche, les relectures prévues aux lignes 406 à 425 sont bloquées : arXiv, LessWrong, transformer-circuits.pub et alignment.anthropic.com y sont refusés à WebFetch et au shell. Il faut leur prévoir une voie, par exemple l'instance qui avait curl (§4.2).

---

## D. Vérifié conforme (pour ne pas refaire)

- **Fiche Sonnet 4.5 :** chiffres, témoin, date, et phrase relue (rapport 2 ; §4.2 n° 5).
- **Espace de travail global :**
  - chiffres du §7, relus (§4.2 n° 2) ;
  - 71 % → 3 % et 0/180 → 13/180 (rapports 2, 3 et 5) ;
  - 13/180 = 7,2 % ;
  - dates du 6 et du 16 juillet (rapport 5).
- ***Stress Testing* :** chiffres (rapports 1, 2 et 6) et phrase relue.
- **Fiches Opus 4.7 et Fable 5** (rapports 2 et 4) : contenu et citation conformes. La fiche Fable 5 est bien distinguée du §6.4.2.2.1 corrigé.
- **OpenAI 2606.24014** (rapport 2) et **Redwood** (contradiction n° 3, bien posée).
- ***Routing Subspaces* :** contenu et contradiction sur l'auteur et la date.
- **Corrections du §4.3 bien reprises :** Korbak et al., *Eval Cooperativeness*, Heidari, Baek, Mody, *Agentic Misalignment in Summer 2026*, Hua et al., auteurs de Cho et al.
- **Résumés seuls :** Montoya, Anwar, Knecht, Gaya, Vu, Singh, Zhuang.
- **Burnat et Davidson (2605.06327) :** l'existence et la description sont confirmées par un extrait de recherche (vu par extrait de recherche, non ouvert). Aucun chiffre ne doit en être tiré.
- **Calendriers :** ICLR 2027 (rapport 6) et SPAR.
- **Aucun sigle d'idée, aucun « first ».**
