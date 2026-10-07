# Vérification du groupe 3 — tranches volet2_E_a_I et volet3 (cours v3.6, 2 octobre 2026)

## Portée et méthode

- **Insertions vérifiées.** Volet 2, §E à §I : 16 en français et 16 en anglais. Volet 3 : 23 en français et 23 en anglais. Total : 78, soit 39 paires.
- **Ce qui a été lu.**
  - Les quatre extraits `applique_volet2_E_a_I_{FR,EN}.md` et `applique_volet3_{FR,EN}.md`.
  - Le texte qui entoure chaque insertion dans la v3.6 : français, lignes 1072 à 1716 ; anglais, lignes 1161 à 1857.
  - Chaque source citée, relue dans sa pièce :
    - le cours v3.5 : volet M (M4, M5, M7, M8, M9) ; volet 2 (préambule, §A à §I, cas K52, JB8, K76, G1, JB10, K63, clôture) ; volet 4 (CCS, AI Control, Monosemanticity) ; volet 5 (sujets 1, 3, 4, 11 et 13) ; volet 6 (§2, §6, §8) ; volet 7 (F·23, F·24, F·26, F·27, F·29, F·35, F·40, F·50, F·51, F·56, F·59, F·60, F·62) ; volet 10 (LatentQA, les trois fiches sur le débat, Łucki et al., WMDP, Deeb et Roger) ; volet 11 (réponse 43) ;
    - les fiches : parties B et C, fiches 2, 3, 5, 7, 11, 12, 15, 16, 17, 18 et 19 ;
    - le programme, parties 1, 3, 7 et 8 ; la passation, §5.1, §5.2 et §5.5 ; l'explication du 2 octobre, §1 à §3 ;
    - le rapport d'antériorité 3 du 2 octobre (*The Obfuscation Atlas*) ; le README du dépôt.
- **Contrôle mécanique.** Le script `travail/_verif_groupe_3/construire_corrections.py` construit le JSON à partir des lignes exactes de la v3.6, puis vérifie cinq choses :
  - chaque « ancien » apparaît une seule fois ;
  - aucune ligne de la v3.5 n'est touchée ;
  - chaque « ancien » reste unique après une application simulée des corrections des groupes 1 et 2 ;
  - le JSON est valide ;
  - aucune citation n'atteint quinze mots.

  Résultat : 24 corrections, toutes les vérifications passent.

## Bilan

**12 fautes**, chacune corrigée dans les deux langues, soit **24 corrections** dans `corrections_groupe_3.json`.

| Nature | Corrections |
|---|---|
| Fausse, ou contraire au texte voisin | 3 (piège de K52 réintroduit) ; 11 (pots de miel : formule absente de la fiche 3, « ne mesure » sans source, parade de K63 ignorée) ; 12 (chiffre ajouté à une phrase à dire, explication du README à l'indicatif) |
| Affirmation sans source, ou source mal citée | 1 (« le juge est souvent un modèle ») |
| Doctrine : un nul ne compte qu'avec son cas connu | 6, 7 |
| Contradiction interne d'un encadré | 2 |
| Durcissements : un pari, un risque ou une menace dits comme un fait, ou une parade partielle dite entière | 4, 5, 8, 9, 10 |

- **Les places.** Aucune insertion ne coupe un tableau, une liste, un bloc de citation ni un paragraphe. Chacune suit la dernière ligne d'un paragraphe ou d'un bloc. Les paragraphes que l'extraction du PDF a coupés par une ligne vide (volet 3, §2, §5 et quatrième thème) sont pris après leur seconde moitié. Les renvois pointent vers des encadrés qui existent à l'endroit dit : les 23 cibles distinctes des renvois de ces deux tranches ont été vérifiées dans la v3.6 (lignes 359 à 6215).
- **Les deux langues.** Les 39 paires disent la même chose, au même endroit. Aucune divergence n'a été trouvée. Les corrections sont faites par paires.
- **La forme.**
  - Les formats fixes sont respectés.
  - Les avertissements ponctuels du volet 3 citent leurs sources entre parenthèses simples, ceux du volet 2 entre *(source : …)*. Les deux sont permis par le format.
  - Aucun sigle inventé : seuls des numéros de la banque, des sections du cours et des sigles courants.
  - Toutes les citations font moins de quinze mots.
  - « first » n'apparaît que comme le mot à ne pas dire.
- **La doctrine.** Aucune insertion ne dit qu'un contrôle aléatoire écarte le dommage. La phrase de doctrine est écrite en toutes lettres dans l'avertissement du volet 3 sur l'ancrage empirique. Deux nuls étaient donnés comme bornes sans leur cas connu : corrections 6 et 7.

## Insertion par insertion — volet 2, §E à §I

**FR n°1 / EN n°2 — encadré « Débat et supervision évolutive »** (FR l. 1080, EN l. 1170), après « En pratique — Debate ».
- **Limites 1 à 3 et leurs parades : justes.** Elles viennent du §E (l'argument obfusqué ; *LMs Learn to Mislead Humans via RLHF* ; le banc où l'on connaît la réponse) et de la clôture du volet 2 (« au-delà de l'expertise humaine et sans référence »). Aucune pièce ne donne de parade à l'argument obfusqué : « aucune connue » est juste.
- **Limite 4 : faute.**
  - « Le juge est souvent un modèle » ne se trouve dans aucune pièce.
  - Le piège 6 dit seulement « Oublier qui juge ».
  - Au volet 10, les juges de Michael et al. sont « toujours humains ». C'est chez Kenton et al. que le juge est un LLM, avec deux erreurs systématiques constatées : il suit le consultant ouvert, qu'il ait raison ou tort ; son biais de position est plus fort en débat.
  - → **correction 1**, avec la source au volet 10.
- **Parade 4 : juste** (programme, partie 3 : juge scellé, audit humain d'environ 200 items).
- Place, langues et forme : justes.

**FR n°3 / EN n°4 — renvoi après les contrôles de K52.** Les cibles existent (§A après *Auditing Hidden Objectives*, §C après *The Geometry of Truth*). Le renvoi est pertinent : le faux fait implanté fait de la copie un organisme, et le filtre contient une sonde.

**FR n°5 / EN n°6 — encadré « Élicitation non supervisée par cohérence »**, à la fin de K52.
- **Limite 1 et parade 1 : justes.** Volet 6, §8 (les méthodes non supervisées trouvent le trait le plus saillant) ; volet 4, paragraphe CCS (« la feature la plus saillante… sensible au prompt ») ; parade : l'expérience de K52.
- **Limite 2 : juste** (le pari de K52).
- **Parade 2 : durcie.**
  - « Dire que sans lui elle ne rend que la cohérence » énonce comme un fait le pari de K52, que le cours écrit au conditionnel.
  - L'entraînement du facile au difficile n'est, dans K52, que l'un des « deux espoirs » mis à l'épreuve par le stress-test, et le cours n'en donne pas l'issue.
  - → **correction 4** : un espoir, pas une garantie ; et le fait de K52 : la méthode « ne récompense que la cohérence ».
- **Limite 3 : juste** (K52, « Ce qui existe déjà »).
- **Parade 3 : contradiction.** « Aucune connue » contredit la parade 1 du même encadré et l'expérience de K52, juste au-dessus, qui rend vérifiable l'invérifiable. → **correction 2** : parade partielle sur un domaine construit ; aucune connue sur les vraies questions invérifiables.
- **Limite 4 : faute.**
  - « Le filtre de l'implant et la méthode » reprend la version copilote que le piège de K52, deux paragraphes plus haut, déclare fautive : « my gate » y désignait l'inférence en aval, ce qui rendait le signe d'échec impossible par construction (M6).
  - L'arbitrage l'a corrigée en « my probe ».
  - → **correction 3** : « La sonde du filtre et la méthode ». La parade 4 (l'inférence en aval comme témoin) devient alors cohérente avec la limite.

**FR n°7 / EN n°8 — encadré « Généralisation faible-vers-fort »**, après « En pratique — l'automatisation ».
- **Limites et parades 1 à 3 : justes** (§F et JB8 : superviseur faux dans un sens fixe et superviseur aléatoire ; copie sur étiquettes vraies ; items tenus à part ; accord là où le superviseur a raison ; « structure propre au jeu de données »).
- **Limite 4 : juste** (F·40, limite écrite : tâche délibérément vérifiable).
- **Limite 5 : juste** (F·26, limite écrite). Le travail n'est pas nommé, comme le veut la règle des fiches.

**FR n°9 / EN n°10 — renvoi après le cas connu de JB8 : juste.** Les cibles existent : M5, fin de section (l. 462) ; M4, après « Le jeu tenu à part » (l. 413).

**FR n°11 / EN n°12 — encadré « Moniteurs du contrôle »**, après « En pratique — les coup probes ».
- **Limite et parade 1 : justes** (F·23 : sur Opus 4.6, 50 % des 40 attaques conçues à la main ne sont jamais attrapées ; prompts ciblés ; ensemble de prompts ou seconde étape coûteuse ; seuil à 1 % de faux positifs sur des variantes bénignes appariées).
- **Limite et parade 2 : justes** (F·24 : 0,87 → 0,41 ; « au moins celui-ci »).
- **Limite 3 : juste** (F·59 : chaque action est « peu incriminante » ; F·56).
- **Parade 3 : à préciser.** F·56 dit que les moniteurs à état « récupèrent une partie » des attaques fragmentées ; la parade les donnait sans réserve. → **correction 5**. Sa seconde moitié (« I haven't seen that combination measured ») est une règle de formulation (volet 6, §6) plus qu'une parade ; elle est gardée, et elle respecte la doctrine.
- **Limite et parade 4 : justes.** Volet 6, §6 : le « 81-87 % » de Brown est un rappel de campagne à dix fois plus de trafic bénin, qui tombe à 65,8 % à cent fois. Préambule du volet 2 : un taux de faux positifs très bas.
- **Limites et parades 5 à 8 : justes.** K70 ; fiche 19 ; volet 4, AI Control (« aucune connue » acceptable) ; K76.

**FR n°13 / EN n°14 — avertissement sur le « quart » de SHADE-Arena, dans K76 : juste.** F·24 : cinq environnements SHADE-Arena, 0,87 → 0,41, ablation composante par composante. Il est placé après « Ce qui existe déjà » et ne touche pas la forme nommée.

**FR n°15 / EN n°16 — renvoi après les contrôles de K76 : juste.**

**FR n°17 / EN n°18 — avertissement après le cas connu de K76 : juste.**
- Le rapport 3 du 2 octobre (*Obfuscation Atlas*) est cité comme un rapport, au conditionnel ; l'explication, §3, est citée aussi.
- La parade est sourcée : programme, partie 3 (la sonde neuve sur le jeu d'indices δ) et partie 8 (« la condition se reloge ») ; passation, §5.2 (mesure séparée) et §5.5 (une sonde neuve à la fin).
- Doctrine juste : même validé, le zéro ne borne que la sonde gardée fixe.

**FR n°19 / EN n°20 — encadré « Red-teaming »**, après StrongREJECT.
- **Limite 1 : juste** (M7).
- **Parade 1 : incomplète.** Le budget seul ne suffit pas : selon la doctrine (M5), un « rien trouvé » ne compte qu'avec son cas connu. → **correction 6**.
- **Limites et parades 2 à 5 : justes.** M5 et F·35 ; M4 et M9 (jumeau propre, porte plantée) ; §H et G1 (préjudice extrait ou différentiel, noté à l'aveugle ; modèle nu et filtre affaibli) ; F·24.
- **Limite 6 : juste** (fiche 15 et partie C). Aucune pièce ne donne de parade.

**FR n°21 / EN n°22 — avertissement sur « sans en trouver d'universel », dans G1.**
- Les sources M5 et M7 sont justes, mais « une borne à son budget » omet la condition de M5 : un nul ne compte que si l'instrument voit ce qu'on sait présent.
- Le groupe 1 a corrigé la même phrase dans ce sens, à un autre endroit du cours.
- → **correction 7**.

**FR n°23 / EN n°24 — renvoi après le cas connu de G1 : juste.**

**FR n°25 / EN n°26 — encadré « Classifieurs de sûreté (filtres) »**, à la fin de G1.
- **Limite 1 et sa parade : justes** (F·35 : « about 32 poisoned training examples … regardless of training set size » ; M9).
- **Limite 2 : ramassée, laissée telle quelle.** En M4, la borne large est celle de deux jumeaux entraînés chacun sur une moitié des données. « Le jumeau propre ne donne qu'une borne large » résume, sans fausser.
- **Limite 3 et sa parade : justes** (M5, M9).
- **Limite 4 et sa parade : justes** (G1).
- **Limite 5 : durcie.**
  - La fiche 3 dit seulement qu'une version du classifieur tourne en RL, « modified to avoid incentivizing the model to evade ».
  - C'est un risque, pas un fait général.
  - → **correction 8** : « peut inciter ».
- **Parade 5 : juste.** Fiche 3 ; fiche 17 (« ne jamais entraîner contre le moniteur »).

**FR n°27 / EN n°28 — avertissement après Constitutional AI.**
- La parade est juste (programme, partie 8).
- Mais la partie 8 range l'exploitation du juge d'entraînement parmi les menaces, et « se fait exploiter » la dit comme un fait.
- → **correction 9** : « peut se faire exploiter ».

**FR n°29 / EN n°30 — encadré « Désapprentissage et ré-élicitation »**, après Deeb et Roger : **juste.** Tout est dans les sources :
- Deeb et Roger : récupération au-delà de 88 % ; faits à faible fuite seulement ; sondes en échec sur un modèle qui reste jailbreakable.
- Łucki et al. : le logit lens échoue, retirer une direction par couche rend 64,7 %.
- M4 et M5 (« Not elicitable at this budget ») ; M9 (des moitiés liées s'enseignent) ; JB10 (petits modèles) ; fiche 5 (« has yet to yield competitive results »).

**FR n°31 / EN n°32 — renvoi après le cas connu de JB10 : juste.**

## Insertion par insertion — volet 3

**FR n°1 / EN n°2 — renvoi après le §1 : juste.**

**FR n°3 / EN n°4 — avertissement après JB2 : juste.**
- La fiche 3 porte les limites du §2.16 du Risk Report : des évaluations non tirées des vrais chemins de risque, une tâche secondaire dans le prompt, des modèles probablement conscients d'être évalués.
- Le lien entre le point de sabotage de JB2 et ces limites est une inférence acceptable. La fiche 3 les attache aux évaluations de la Claim 1, sur les capacités cachées, et la « tâche secondaire dans le prompt » est celle des évaluations de sabotage.
- Les parades sont justes (K63, M7).

**FR n°5 / EN n°6 — renvoi : juste.**

**FR n°7 / EN n°8 — avertissement après K48 : juste.**
- Fiche 17 : la non-verbalisation n'est pas un raisonnement caché ; la surveillabilité est un ratio. Réponse 43 : la perturbation graduée.
- C'est une limite de construit du pari de K48, pas une contradiction.

**FR n°9 / EN n°10 — avertissement après le §3 : juste.**
- F·51 : 43 % contre 55 % à 1 % de faux positifs ; fiche 19 ; F·50 et sujet 1 pour la parade.
- Remarque, sans correction : « au seuil d'un moniteur » est une glose ; les sondes de F·51 détectent des interactions à enjeu élevé.

**FR n°11 / EN n°12 — renvoi : juste.**

**FR n°13 / EN n°14 — avertissement après K70, sur la carte Fable 5 : juste.**
- Fiche 18 : le NLA peut confabuler, et ses contrôles de déploiement sont mesurés par le NLA lui-même.
- Fiche 3 : les réponses dépendent de la formulation des questions. Fiche 2 : « weakly positively correlated ».
- Parade : sujet 4 (la triangulation) ; M4 (dire lequel a fondé quel chiffre).

**FR n°15 / EN n°16 — avertissement après K70, sur le juge plus lent : juste.**
- Fiche 3 : environ 1 % contre environ 50 %, pour un seul moniteur. Volet 6, §2 : un juge a des erreurs systématiques.
- Parade : programme, partie 3 ; passation, §5.1.

**FR n°17 / EN n°18 — renvoi : juste.**

**FR n°19 / EN n°20 — avertissement après K67 : juste.**
- Fiche 15 : la meilleure de 1 000 directions aléatoires atteint 95,3 % (marqué †), et la saillance peut venir de l'insertion. M5 : le cas naturel « reste ouvert ».
- « Borne l'instrument » reprend la formule de l'explication, §1.
- Doctrine juste : l'aléatoire n'y sert que de nul de spécificité.

**FR n°21 / EN n°22 — renvoi : juste.**

**FR n°23 / EN n°24 — avertissement après JB9 : juste.** K13 : des modèles juges ; un écho poli compté comme une adoption ; la parade de K13. F·24 pour la red team.

**FR n°25 / EN n°26 — avertissement après le §6 : juste.** Partie C (« not elicitable at this budget ») ; M9 ; M4 et M5 ; §I ; Deeb et Roger (faits à faible fuite).

**FR n°27 / EN n°28 — renvoi : juste.**

**FR n°29 / EN n°30 — renvoi : juste.** Ses dix cibles existent.

**FR n°31 / EN n°32 — avertissement sur l'ancrage empirique : juste.** Fiche 2 (Opus 4.8 ; Fable 5 à 0,01× ; « comparable or smaller ») ; sujet 4 ; M4. La doctrine y est écrite en toutes lettres.

**FR n°33 / EN n°34 — avertissement sur les organismes malhonnêtes : juste.** F·62, avec sa règle : à ne dire qu'une fois versé à la base ; fiche 7 (0,70-0,75, à peine mieux qu'un prompt) ; sujet 1 ; F·29.

**FR n°35 / EN n°36 — avertissement sur les lectures d'états internes.**
- Les sources sont justes : LatentQA (une copie fine-tunée qui lit) ; fiche 18 ; fiche 11 (environ 20 % pour Opus 4.1).
- Mais « Ces lectures ne sont pas un auto-rapport » couvre aussi l'introspection émergente, que le paragraphe cite et qui est bien un auto-rapport.
- → **correction 10** : « pas toutes ».

**FR n°37 / EN n°38 — avertissement sur AuditBench : juste.** F·27 (56 modèles) ; piège 5 ; fiche 16 (objectif décrit en clair, « artificially easy to discover ») ; programme, partie 8 ; passation, §5.2.

**FR n°39 / EN n°40 — avertissement sur les chercheurs automatisés : juste.** F·40 ; F·60 ; sujet 11.

**FR n°41 / EN n°42 — avertissement sur les pots de miel : trois fautes.**
1. « Un pot de miel ne sépare pas un modèle qui le lit comme factice d'un modèle qui se retient » n'est pas dans la fiche 3. Son confondeur porte sur la réplication CTF : dans une simulation, « c'est faux » est vrai. Le groupe 2 a corrigé la même formule dans l'encadré du §B.
2. La partie 1 du programme dit « aucun contrôle de la conscience d'évaluation », pas « ne mesure ».
3. « Pour le pot de miel lu comme factice, aucune parade connue » ignore la parade du cas K63 : deux versions d'un environnement, et un organisme dressé à se cacher comme cas connu.

→ **correction 11**. La limite y devient sourcée :
- fiche 2 : sur le pot de miel synthétique, le modèle final de Sonnet 4.5 verbalise sa conscience dans plus de 80 % des cas ;
- K63 : moins de mauvaise conduite quand les modèles se disent évalués ;
- « aucun contrôle » ;
- la parade de K63, dite partielle.

**FR n°43 / EN n°44 — avertissement de la partie IV, sur les outils du chercheur : deux fautes de règle.**
1. « À dire avec elle » fait de cette note d'étude un ajout, avec un chiffre (86,8 %), à la phrase que le cours demande de dérouler. La règle l'interdit : les ajouts ne touchent pas aux lignes à dire et ne leur ajoutent aucun chiffre.
2. L'explication du README (un adoucissement de chaque verdict négatif, lu à travers une fenêtre tronquée) est donnée à l'indicatif. Or le cours la fait dire au conditionnel, faute de vérification (M8 ; volet 6, §2).

Le reste est dans le README : 86,8 % de la variance au résidu ; le signal porté par le résidu ; « absent du dictionnaire » ou « dictionnaire qui perd trop » ; l'extraction sur un jeu disjoint ; les réponses jugées en entier. M4 donne le témoin sans pression et le concept rival. → **correction 12**.

**FR n°45 / EN n°46 — renvoi : juste.** Ses six cibles existent.

## Remarques, sans correction

- Volet 2, encadré « Moniteurs du contrôle », parade 3 : sa seconde moitié est une règle de formulation plus qu'une parade. Elle est conforme à la doctrine (« I haven't seen that combination measured », jamais « first »).
- Volet 2, encadré « Classifieurs de sûreté », limite 2 : formulation ramassée de M4 (voir plus haut).
- Volet 3, n°3 : le lien entre le point de sabotage de JB2 et le §2.16 est une inférence, acceptable.
- Volet 3, n°9 : « au seuil d'un moniteur » est une glose, et l'objet des sondes de F·51 (les interactions à enjeu élevé) n'est pas dit.
- Volet 3, n°19 : la formule « borne l'instrument » vient de l'explication, §1. La source citée (M5) en porte le fond.
- Les formats des sources diffèrent entre les tranches : *(source : …)* au volet 2, parenthèses simples au volet 3. Les deux sont conformes.

## Les 24 corrections (`corrections_groupe_3.json`)

| N° | Insertion | Français | Anglais |
|---|---|---|---|
| 1 | volet 2, débat, limite 4 | « peut être un modèle », avec les deux erreurs relevées chez Kenton et al. | idem |
| 2 | volet 2, élicitation, parade 3 | parade partielle, puis « aucune connue » | idem |
| 3 | volet 2, élicitation, limite 4 | « La sonde du filtre » | « The filter's probe » |
| 4 | volet 2, élicitation, parade 2 | un espoir, pas une garantie ; « ne récompense que » | idem |
| 5 | volet 2, moniteurs, parade 3 | « qui n'en récupèrent qu'une partie » | idem |
| 6 | volet 2, red-teaming, parade 1 | ajout du cas connu (M5) | idem |
| 7 | volet 2, G1, « sans en trouver d'universel » | ajout de la condition du cas connu | idem |
| 8 | volet 2, classifieurs, limite 5 | « peut inciter » | « can give » |
| 9 | volet 2, Constitutional AI | « peut se faire exploiter » | « can get exploited » |
| 10 | volet 3, honnêteté et cognition | « pas toutes un auto-rapport » | « Not all of these readings » |
| 11 | volet 3, pots de miel | limite sourcée, « aucun contrôle », parade de K63 | idem |
| 12 | volet 3, partie IV | « à connaître avant de la dire » ; l'explication du README au conditionnel | idem |
