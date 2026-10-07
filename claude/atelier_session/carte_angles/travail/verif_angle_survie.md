# Vérification de la fiche « angle : la survie au post-entraînement »

Fichier vérifié : `travail/angle_survie.md` (506 lignes ; numéros de ligne ci-dessous). Vérification du 2 octobre 2026.

**Ce que j'ai relu moi-même.**
- Le rapport 4 de la nuit en entier (lignes 727 à 1011 du fichier du 2 octobre).
- Les rapports 1, 6 et 7 de la nuit en entier. Les passages des rapports 2, 3 et 5 qui touchent la survie.
- Les rapports du 1er octobre : l'axe raisons contre actions et l'axe conscience d'évaluation en entier ; l'axe combinaison exacte en entier ; l'axe test causal par mots-clés.
- La passation v1.2 : §1 à §6 et annexe A. La consigne de l'agent 4. Le programme v1.1 : partie 1, les phases ultérieures, la phase de survie, les règles de décision de la survie, les menaces à la validité.
- Le web : quatre recherches, et un curl du SUMMARY.md d'exp9 (liste en fin de fichier).

**Ce que j'ai confirmé.** La plupart des chiffres et des citations de la fiche sont dans les rapports, avec le statut indiqué :
- Cho et al. : 31,0 % contre 22,0 %, +9,0 points, et les points de contrôle ;
- *Stress Testing Deliberative Alignment*, §8 : 81,5 % → 65,8 % ;
- *Teaching Claude Why* : la citation sur le RL ;
- de la Fuente et Conmy : 88 % et 39 % ;
- Brazilek et Tidmarsh : 77 % contre 40 % ; 5 000 échantillons ;
- Baines et al. : 2 %, de 90 % à 13 % ;
- Korbak et al. : 230 000 documents, environ 340 M de tokens ;
- *Generalization Hacking* : de 12 à 21 points, +14 points, environ 3 points ;
- Kretschmar : de 14 % à 3 % ; de 86 à 89 % ; de 10 % à 29 % ;
- Hacker-Opus : de 5 % à 40 % ;
- Gaya et al., *Metagaming matters*, BLOCK-EM, Jagadeesh et al. ;
- les dates SPAR et ICLR.

Le SUMMARY.md d'exp9 que j'ai recontrôlé par curl fait 12 666 octets ; son empreinte sha256 est celle que donne la fiche (`2a55f9b3…183fec`). Il porte « complete (2026-04-29) », le PPO noté en ligne est dans « Future work », et il attend une baisse de la verbalisation avec une conduite conditionnelle qui persiste. Aucune erreur déjà corrigée au §4.3 n'est reprise : Korbak, *Eval Cooperativeness*, le titre de Brazilek et les auteurs de Cho y sont à jour. Le verdict général (« partiellement pris, dans des variantes ») suit le §4.4, n° 6.

Les corrections exigées suivent, les bloquantes d'abord.

---

## 1. Corrections bloquantes

### B1. Le niveau « moyen pour l'angle entier » est attribué à tort au §4.4 (lignes 46-47 et 429-431)
- **La fiche** : « élevé pour la survie d'une mitigation du jeu d'évaluation ; moyen pour l'angle entier. C'est le verdict du §4.4, n° 6, qui suit le rapport 4. » La contradiction 3 répète : « Tranché par le §4.4, n° 6 : élevé […], moyen pour l'angle entier. »
- **Les sources** :
  - le §4.4, n° 6 dit seulement : « Lundqvist, danger élevé pour la survie d'une mitigation du jeu d'évaluation (relu) » ;
  - le rapport 4 (ligne 925) dit seulement « niveau élevé pour la survie d'une mitigation du jeu d'évaluation » ;
  - aucun des deux ne dit « moyen pour l'angle entier ». C'est le rapport 6 (ligne 1465) qui dit « moyen […] pour la survie ».
- **Correction** : « élevé pour la survie d'une mitigation du jeu d'évaluation (§4.4, n° 6 ; rapport 4) ; pour l'angle entier, moyen : jugement de cette fiche, qui rejoint le rapport 6 ». Corriger de même la contradiction 3 : le §4.4 tranche le niveau de la sous-question, pas celui de l'angle.

### B2. « Elle ne précise pas la nature du post-entraînement » n'a pas de source, et le verdict du rapport 4 sur Lundqvist est omis (lignes 51-52 ; conséquences aux lignes 21, 396-403)
- **La fiche** :
  - « La page relue ne mentionne ni l'inhibition validée […] ni la part conditionnelle » ;
  - « Elle ne précise pas la nature du post-entraînement ».
- **Les sources** :
  - le §4.2, n° 3 liste ce qui a été *confirmé* sur la page. Ce n'est pas un relevé exhaustif : une absence dans cette liste ne prouve pas une absence sur la page ;
  - le rapport 4 cite la question « survive the optimization pressure of post-training » (ligne 916) ;
  - surtout, son verdict (ligne 972) dit : « La survie de l'indépendance au regard, et un post-entraînement qui récompense le jeu d'évaluation, sont annoncés par Lundqvist (SPAR) mais non publiés ». La fiche ne rapporte nulle part cette lecture du rapport 4.
- **Pourquoi c'est bloquant.** Selon les consignes, un travail qui a *annoncé* ce que vise un angle est de danger élevé. Si le rapport 4 lit juste, deux points de la fiche tombent sous ce niveau :
  - la phase qui paie le jeu d'évaluation (ligne 21, troisième puce : « Aucun n'applique à des modèles entraînés à l'alignement une phase dont la récompense paie explicitement le jeu d'évaluation ») ;
  - la survie de l'indépendance au regard.
- **Corrections** :
  - Remplacer les deux phrases par : « Ni le §4.2, n° 3, ni la liste du rapport 4 ne relèvent d'inhibition validée ni de nature du post-entraînement. Le verdict du rapport 4 lit pourtant la page comme annonçant la survie de l'indépendance au regard et un post-entraînement qui récompense le jeu d'évaluation (rapport 4, non relu). À trancher sur la page. »
  - Ajouter ce désaccord à la liste des contradictions (rapport 4, ligne 972, contre la lecture de la fiche).
  - Ligne 21 : ajouter « annoncé peut-être par Lundqvist, selon le verdict du rapport 4 ».
  - Formulation 3 (ligne 401) : elle reste tenable grâce à « trained on reasons or on actions ». Le dire, et citer Lundqvist parmi les menaces, pas seulement *Shallow Beliefs*.

### B3. La cinquième formulation intenable est mal sourcée (lignes 415-416)
- **La fiche** : « We are the first to show that later RL raises evaluation awareness after alignment training » serait intenable parce que *Stress Testing Deliberative Alignment*, *Metagaming matters* et le Risk Report « le montrent déjà ».
- **Les sources** :
  - *Stress Testing Deliberative Alignment* : la hausse de 2,0 % à 20,5 % se fait « sur un modèle expérimental sans entraînement anti-manigance » (rapport 4, ligne 825, que la fiche reprend elle-même à sa ligne 89). Ce n'est donc pas « after alignment training ». Après l'entraînement anti-manigance, le §8 ne rapporte que des actions cachées en légère hausse et des citations de la spécification en baisse (rapport 4, lignes 822-824) ;
  - *Metagaming matters* : la hausse de 2 % à 20,6 % a lieu pendant le RL de capacités d'o3, et elle *persiste après* l'entraînement d'alignement. L'ordre est inverse (rapport 2, ligne 370 ; rapport du 1er octobre, conscience d'évaluation, ligne 131) ;
  - le Risk Report : c'est la conscience d'être *noté* qui monte, pendant un RL qui paie le hacking (rapport 4, ligne 898). Ce n'est ni la conscience d'évaluation, ni un RL qui suit un entraînement d'alignement.
- **Correction.** Écrire cette formulation au format « to our knowledge » (voir M4) et la limiter à ce qui est établi : « un RL de capacités fait monter la conscience d'évaluation verbalisée » (*Stress Testing Deliberative Alignment* ; *Metagaming matters*). Pour l'ordre « entraînement de préférences, puis RL », la seule source des rapports est Bharadwaj et Kirk (manque n° 2), sur OLMo 3 : la conscience verbalisée s'effondre au DPO, puis remonte au RL à récompenses vérifiables (rapport 2, texte intégral, ligne 331).

### B4. Korbak et al. : une attribution au §4.4 sans fondement, et une contradiction interne (lignes 18, 185-190, 407, 487)
- **La fiche** :
  - ligne 18 : Korbak et al. sont classés dans « la survie d'un gain d'alignement », avec la source « rapports 4 et 7 ; §4.4, n° 6 » ;
  - ligne 407 : « […] Korbak et al. et Cho et al. le font tous » ;
  - ligne 190 : « La survie n'est pas isolée étape par étape » ;
  - ligne 487 : « À vérifier avant de le présenter comme un travail de survie ».
- **Les sources** :
  - le §4.4, n° 6 ne cite pas Korbak et al. ;
  - le rapport 7 (lignes 1595-1599) décrit pourtant des trajectoires *pendant* le RL. En questions-réponses, les scores des bras aligné et témoin restent constants ou baissent légèrement, et ceux du bras désaligné dessinent un U inversé. L'alignement progresse au fil du RL partout sauf sur Blackmail ;
  - le rapport 4 l'a lu « via résumé » (ligne 894), pas en texte intégral.
- **Correction** :
  - retirer « §4.4, n° 6 » de la ligne 18 ;
  - décrire les trajectoires pendant le RL d'après le rapport 7, non relues ;
  - choisir une position et la tenir partout. Soit Korbak et al. sont un travail de survie (même SFT et même RL pour tous les bras, effets mesurés pendant et après), soit ils restent « à vérifier ». Dans le second cas, les retirer des lignes 18, 342 et 407.

---

## 2. Corrections à faire avant d'intégrer la fiche à la carte

### C1. Cho et al. : le résultat de l'écart surveillé / non surveillé manque (lignes 57-78, 393-397)
- **La fiche** se contente de : « seulement un écart surveillé / non surveillé par prompt (rapport 1) ».
- **Les sources** :
  - le rapport 1 (ligne 114) donne l'écart de conformité : −0,9 point avec raisons, +0,7 point sans, après le midtraining (p < 0,01), puis « indistinct aux étapes suivantes » ;
  - le rapport 7 (ligne 1778) donne le même résultat, sous la forme d'un effet de −1,6 point, « juste après le midtraining » ;
  - « par prompt » vient du tableau du programme v1.1 (ligne 89), pas du rapport 1.
- **Pourquoi cela compte.** C'est une mesure comportementale, stade par stade, de la dépendance au regard, avec et sans raisons, à travers un post-entraînement. C'est la variante la plus proche de la survie de l'indépendance au regard. Elle nuance aussi le « indistinguables après le midtraining » du §4.2, n° 9, qui vaut pour les mesures principales.
- **Correction** :
  - donner ce résultat, avec le statut « rapports 1 et 7, texte intégral ; non relu » ;
  - le citer dans « Les morceaux déjà occupés » ;
  - le citer dans la justification de la formulation 2 : ce qui reste libre, c'est la mesure par inhibition validée, pas la question.

### C2. Cho et al. : la citation sur la conscience d'évaluation est tronquée (lignes 68, 356, 397)
- **Les sources** : selon le §4.2, n° 9, les auteurs ne peuvent exclure ni le pattern-matching de surface ni la conscience d'évaluation.
- **Correction.** Citer les deux. À la ligne 356, l'inhibition ne tranche que la conscience d'évaluation. Le pattern-matching relève des bras texte neutre et raisonnement d'une autre situation. Écrire donc « en partie » au lieu de « exactement ce que la phase de survie […] peut trancher ».

### C3. Cho et al. : la phrase sur l'écart au témoin est ambiguë (ligne 69)
- **La fiche** : « Le gain du midtraining constitutionnel sur le témoin tient, lui, au chantage : −18,5, −18,7 puis −17,5 points ».
- **La source** : le rapport 7 (ligne 1779) dit seulement « Sur le chantage, l'écart avec le témoin est de −18,5, −18,7 puis −17,5 points selon le stade », sans nommer la condition.
- **Correction** : « Au chantage, l'écart au témoin reste de −18,5, −18,7 puis −17,5 points selon le stade (rapport 7 ; condition non précisée) ».

### C4. « Le point de départ annoncé de Lundqvist » n'a pas de source (ligne 300)
- **Les sources** :
  - le §4.2, n° 3 confirme seulement « la survie de la coopérativité envers les évaluations » ;
  - les rapports 4 et 6 non plus ne rattachent pas le projet à Li et Turner.
- **Correction** : écrire « La survie de la coopérativité est annoncée par Lundqvist (relu, §4.2, n° 3) ; le lien avec la méthode de Li et Turner est une inférence ».

### C5. Le niveau d'exp9 pour les raisons pour le juge est trop large (ligne 229)
- **La fiche** : « Il est élevé pour les raisons pour le juge ».
- **Les sources** :
  - le rapport 4 (lignes 776-777) dit élevé seulement pour la comparaison entre un juge qui voit le raisonnement et un juge qui ne voit que la réponse, et moyen pour l'angle pris dans son ensemble ;
  - le §4.4, n° 7 le limite aussi à la variante où le raisonnement est la verbalisation de l'évaluation.
- **Correction** : reprendre ces deux restrictions.

### C6. *Helpfulness Hurts* est sous-estimé (lignes 316-318)
- **La fiche** : « Auteurs non vus », « Probablement de la même famille que CaML : à ouvrir ».
- **Ce que montre un extrait vu par moi le 2 octobre** (vu par extrait de recherche, non ouvert) :
  - le modèle est Llama 3.1 8B, midtrainé sur des données de compassion ;
  - il est ensuite post-entraîné par SFT et par GRPO, sur des données d'aide à l'utilisateur ou de code ;
  - la dégradation dépend du domaine ;
  - les auteurs sont Juliana Seawell et Jasmine Brazilek (CaML).
- **Pourquoi cela compte.** Si la lecture le confirme, c'est le travail de survie le plus proche du dispositif : même modèle de départ, et les deux familles de phases ultérieures. Il touche aussi le choix du domaine de la phase neutre (programme v1.1 : « mathématiques, code »).
- **Correction** :
  - le mettre en tête de la liste à relire ;
  - le mentionner, sans chiffre, dans « Les morceaux déjà occupés », avec son statut ;
  - ne lui donner aucun niveau avant lecture.

### C7. « Can mid-training survive RL » est sans doute une annonce, pas une sortie (lignes 319-321 et 371)
- **La fiche** : « possible sortie déjà en ligne », « peut-être une première sortie du projet de CaML ».
- **L'extrait que j'ai vu le 2 octobre** (vu par extrait de recherche, non ouvert) : un projet de CaML sur OLMo 3, avec ses livrables prévus. On y lit un banc de persistance, des points de contrôle publiés et « at least one paper ». C'est le contenu de l'offre que décrit le rapport 6 (ligne 1498).
- **Correction** : dans le tableau, écrire « probablement l'annonce du projet (même contenu que l'offre du 1er septembre) ; aucune sortie vue ».

### C8. Les niveaux de Brazilek et Tidmarsh et de de la Fuente et Conmy sont incohérents (lignes 120 et 202)
- **La fiche** : de la Fuente et Conmy sont « moyen » parce que c'est « le même protocole de lavage que la phase neutre ».
- **Le même critère** vaut pour Brazilek et Tidmarsh : 5 000 échantillons d'instruction-tuning sans rapport effacent l'avantage (rapport 4, ligne 893), classé « faible ».
- **Correction** : aligner les deux niveaux, ou dire ce qui les distingue. Le rapport 4 et le §4.4 ne donnent pas de raison.

### C9. La contradiction sur l'affiliation de Lundqvist n'en est peut-être pas une (lignes 32-33 et 432-435)
- **L'extrait que j'ai vu le 2 octobre** (vu par extrait de recherche, non ouvert) donne les deux : Lundqvist « from Pivotal », et le projet listé parmi ceux de Palaestra Research.
- **Correction** : présenter ces deux mentions comme compatibles jusqu'à relecture, pas comme une contradiction.

### C10. Les dates du projet de Lundqvist (lignes 34 et 368)
- **Les sources** :
  - le rapport 4 (ligne 924) dit « Aucune date annoncée » sur la page du projet ;
  - les dates du 14 septembre au 14 décembre, et le 19 décembre, sont celles de la cohorte, lues dans la FAQ (rapport 6, ligne 1450 ; §4.4). Le rapport 1 les donne sans citer la FAQ (ligne 179).
- **Correction** : « dates de la cohorte (FAQ de SPAR, rapport 6 ; §4.4) ; la page du projet n'en annonce aucune (rapport 4) ».

---

## 3. Corrections mineures

1. **Les niveaux des rapports manquent.** *Training a Misaligned Reward Seeker* est « moyen à faible » dans le rapport 6 (ligne 1322), « faible » dans la fiche ; le dire. Dans le tableau des projets, donner les niveaux du rapport 6 :
   - Ududec : moyen à faible, dépendance au regard et survie (ligne 1486) ;
   - David Africa : faible à moyen ;
   - Second Look Research : faible à moyen ;
   - l'offre de CaML : faible.
2. **La date du billet *Eval Cooperativeness* (ligne 293).** Il est daté du 24 mai par le rapport 7 (ligne 1618) et par le rapport du 1er octobre (ligne 151), mais du 27 mai sur LessWrong par les rapports 4 (ligne 908) et 6 (ligne 1313). Donner les deux dates.
3. **Contradiction 6 (ligne 442).** Écrire « précisé par le rapport 7 (texte intégral) ; non relu », plutôt que « Tranché par la lecture directe du rapport 7 ». Un rapport ne tranche rien.
4. **Les formulations intenables (lignes 406 et 415).** Elles contiennent « We are the first ». Les réécrire en « To our knowledge, no prior work… », pour qu'aucune phrase en « first » ne puisse être recopiée.
5. **« relu ».** L'abréviation est employée partout sans être définie. La définir une fois : « relu sur la source par l'instance du papier (§4.2) ».
6. **Les dates de Cho et al. (ligne 59)** n'ont pas de source : ajouter « rapports 1, 4 et 7 ».
7. **Le statut des lectures du rapport 7.** Le rapport 7 dit que tout a été lu par WebFetch, dont un petit modèle résume le texte, avec des passes « littérales » (ligne 1578). Garder « rapport 7, texte intégral », mais l'indiquer une fois.
8. ***Shallow Beliefs* (ligne 135).** L'extrait que j'ai vu le 2 octobre confirme le titre, les auteurs, l'inoculation par prompt qui empêche le désalignement émergent et le fort désalignement après le midtraining. Il ne dit pas que les modèles préparés « finissent plus désalignés que sans préparation ». Ne garder que ce que l'extrait de la fiche montre, en le marquant comme tel.
9. **Les corrections à reporter dans la v1.1 (lignes 455-460).** En ajouter deux :
   - le « 5 cas sur 8 » d'*Eval Cooperativeness* (ligne 93 de la v1.1) vient du billet ; le résumé d'atelier dit 5 sur 7 (§4.3) ;
   - la v1.1 (ligne 108) dit que le dépôt d'exp9 « compare » deux DPO. Or les DPO sont seulement scriptés, et aucun résultat d'entraînement n'est publié (§4.2, n° 1).
10. **Le « gain d'alignement » de de la Fuente et Conmy (ligne 352).** Le rapport 4 (ligne 882) parle d'un « comportement installé », sans dire lequel. Écrire « un comportement installé par SFT perd jusqu'à 88 % de son écart ».

---

## 4. Les manques : des travaux présents dans les rapports et absents de la fiche

1. ***Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers*** (Dubiński … Evans ; arXiv 2604.25891, avril 2026).
   - **Statut** : rapport du 1er octobre, raisons contre actions, texte intégral (HTML v1, lignes 73-77). Le rapport 6 n'en donne que le titre (NeurIPS 2026, ligne 1514), et l'axe combinaison exacte le classe comme non ouvert (ligne 472).
   - **Ce qu'il fait** : les mitigations usuelles cachent le désalignement émergent aux évaluations standard. Il revient sous des indices du contexte d'entraînement. Ajouter de la chaîne de pensée à l'entraînement réduit ce désalignement conditionnel.
   - **Pourquoi l'ajouter** : c'est une intervention ultérieure qui laisse une conduite conditionnée aux indices, et des raisons qui réduisent cette condition. C'est adjacent à la survie de l'indépendance au regard. Niveau proposé : faible, à revoir après lecture.
2. ***Tracing Eval-Awareness Emergence Through Training of OLMo 3*** (Bharadwaj, Kirk ; LessWrong, 10 juin 2026).
   - **Statut** : rapport 2, texte intégral (lignes 328-334) ; rapport 6 (ligne 1373) ; rapport du 1er octobre, conscience d'évaluation (ligne 178).
   - **Ce qu'il fait** : la conscience verbalisée chute au DPO et remonte au RL à récompenses vérifiables, où le jeu d'évaluation croît.
   - **Pourquoi l'ajouter** : c'est la seule source des rapports pour un RL qui fait monter la conscience d'évaluation après une étape de préférences, sur un modèle ouvert (voir B3). Niveau faible pour la survie.
3. **Les deux travaux où la conduite survit au retrait de la verbalisation.** La fiche retient Kretschmar pour cette leçon ; ces deux travaux la donnent aussi.
   - *Towards Measuring and Detecting Unverbalized Evaluation Awareness* (Montoya … Adams ; atelier d'interprétabilité mécaniste d'ICML 2026). Rapport 4 (ligne 905) et rapport 6 (ligne 1404), résumé seul. La verbalisation est supprimée, mais un écart de conduite de +7,0 points subsiste.
   - *Training LLMs to Verbalize Evaluation Awareness* (Anwar … Krueger ; atelier TAE de NeurIPS 2026). Rapport 4, résumé seul (ligne 904). La verbalisation est multipliée par 2,4 à 2,9, tandis que la conscience latente et la conduite restent stables.
   - Niveau faible pour les deux.
4. ***The Geometry of Refusal: Why Post-Hoc Safety Is Fragile and Pretraining-Time Safety Persists*** (Malla … Choi ; arXiv 2609.06934). Le rapport 5 n'en donne que le titre (ligne 1177), et le rapport du 1er octobre sur le test causal le classe comme non ouvert (ligne 331). Le titre porte sur la persistance selon le stade d'installation : le mettre parmi les travaux non ouverts, à lire.
5. ***Inoculate or Reflect?*** (Imran … Shaikh ; LessWrong, 26 juillet 2026).
   - **Statut** : rapport 5, lu par deux résumés de l'outil (lignes 1048-1060).
   - **Ce qu'il fait** : sur Qwen3-8B, l'inoculation agit comme une porte facile à rouvrir, tandis que la réflexion contrefactuelle réécrit plus largement.
   - **Pourquoi l'ajouter** : c'est la robustesse d'une correction par raisons, sur le modèle du programme. Niveau faible.
6. **Wu et Tang** (arXiv 2604.01476).
   - **Statut** : rapport 3, texte intégral (lignes 494-501). Le §4.3 le corrige : la direction n'est jamais retirée.
   - **Ce qu'il fait** : il suit une direction de conscience d'évaluation au fil d'un RL où le modèle peut réécrire le code de l'évaluateur. Elle monte modérément sur Phi-4-mini et reste plate sur Llama-3.2-3B.
   - **Pourquoi l'ajouter** : c'est un précédent pour la trajectoire de la représentation pendant la phase sous pression. Niveau faible.
7. ***The Obfuscation Atlas*** (rapport 3, lignes 606-611). Après RL, des sondes neuves hors domaine se dégradent. Il appuie, avec Gaya et al., la recommandation de refaire la vérification de manipulation après chaque phase (ligne 358).
8. **Les projets omis.**
   - La collaboration OpenAI–Apollo sur l'émergence du méta-jeu, annoncée en mars 2026 (rapport 2, ligne 427).
   - Les évaluations tierces de runs d'entraînement, avec points de contrôle, annoncées par Apollo le 5 juillet 2026 (rapport 2, ligne 428).
   - Les projets SPAR de David Baek (préférences contradictoires injectées en midtraining) et de Shubhorup Biswas (midtraining à l'échelle), de niveau faible (rapport 1, lignes 182-183 ; rapport 4, lignes 935-936).
9. ***Towards training-time mitigations for alignment faking in RL*** (Gasteiger … Hubinger ; Anthropic, 16 décembre 2025).
   - **Statut** : rapport du 1er octobre, conscience d'évaluation, lignes 157-162.
   - **Ce qu'il fait** : il teste des mitigations installées à l'entraînement contre l'alignement simulé, mesurées sur l'écart surveillé / non surveillé.
   - **Pourquoi l'ajouter** : il est adjacent à la question de Lundqvist. Niveau faible.

---

**Accès du vérificateur, le 2 octobre.**
- **WebSearch** (4 appels) :
  1. "Training-Time Mitigations for Eval Awareness" Lundqvist
  2. "Shallow Beliefs" synthetic document finetuning does not inoculate against emergent misalignment from reward hacking
  3. "Helpfulness Hurts" mid-trained compassion values post-training
  4. "Can mid-training survive RL" LessWrong
- **curl** de `raw.githubusercontent.com/ryanlundqvist/exp9-rlaif-leakage/master/SUMMARY.md` : réponse 200, 12 666 octets. La copie temporaire a été effacée après lecture.
- **Aucun accès** à arxiv.org, sparai.org, lesswrong.com ni alignment.anthropic.com.
