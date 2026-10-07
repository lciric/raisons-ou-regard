# Vérification du groupe 6 — tranches `volets8_9` et `volet10` (cours v3.6, 2 octobre 2026)

**Résultat.** 64 insertions par langue (22 + 42), soit 64 paires FR/EN, relues une à une contre leurs sources. 10 paires ont une faute. Elles donnent **20 corrections** dans `corrections_groupe_6.json` : chaque faute est corrigée en français et en anglais (corrections impaires en français, paires en anglais). Les 54 autres paires sont justes.

Les fautes relevées :

| Nature | Paires (FR / EN) | Corrections |
|---|---|---|
| Contredit le cours : « pas causal » pour un vecteur qui agit (F·31) | volet 9, §4 (6 / 28) | 3-4 |
| Parade déclarée inconnue alors que les pièces en donnent une | §4, extraction supervisée (6 / 28) ; encadré « Patching », limite 4 (25 / 26) ; n° 54, artefact de polarité (67 / 68) | 3-4 ; 13-14 ; 19-20 |
| Source qui ne dit pas ce qu'on lui prête, ou source manquante | §3, SAD (3 / 25) ; §6b, exemples (12 / 34) ; §9b, fiche 3 (21 / 43) ; n° 07, partie 8 du programme (7 / 8) ; encadré « Patching », parade 3 (25 / 26) | 1-2 ; 5-6 ; 7-8 ; 9-10 ; 11-12 |
| Se contredit : « aucune parade » juste après la parade K63 | §9b, AI Organizations (21 / 43) | 7-8 |
| Portée trop large : le score entier du SAD pour la seule tâche stages-oversight | n° 07 (7 / 8) | 9-10 |
| Durcissement : plus fort que la source | encadré « Patching », limite 6 (25 / 26) ; n° 40, « pas d'exemples fabriqués » (57 / 58) | 15-16 ; 17-18 |

## Ce qui a été lu

- **Les extraits** `applique_volets8_9_FR/EN.md` et `applique_volet10_FR/EN.md`.
- **La v3.6, autour de chaque insertion** : tout le volet 8, le volet 9 et le volet 10, avec leurs insertions (FR l. 3825-5030, EN l. 3963-5269).
- **Le cours v3.5, à chaque section citée** :
  - la note de tête et l'index des encadrés ;
  - volet M : M4, M5, M7 ;
  - volet 2 : §A et K71 ; §B (le sandbagging) et K63 ; §C (la méthode, les deux « En pratique ») et K47 ; C bis ; §D ; §E et K52 ; §F ; §G (les coup probes) et K76 ; §H et G1 ; §I et JB10 ; la clôture ;
  - volet 5 : partie II, sujets 1, 4, 10 et 13 ;
  - volet 6 : §2, §3, §4, §8 ;
  - volet 7 : F·23, F·24, F·25, F·29, F·31, F·36, F·39, F·50, F·62 ;
  - volet 10 : toutes les fiches de la tranche, dont n° 05, 07, 08, 13, 14, 16, 18, 21, 24, 26, 27, 28, 30, 39, 40, 51, 53, 54, 55, 56, 58, 59, 60, 62, 63, 64, 65, 66 ;
  - volet 11 : réponses 12 et 43.
- **Les fiches** : parties A, B (grille et pièges 1 à 7) et C ; fiches 1, 2, 3, 4, 5, 7, 8, 10, 15, 17, 18, 19 ; l'annexe ; la contre-lecture des fiches.
- **L'explication du 2 octobre**, §1 à §3.
- **Le programme**, parties 3, 4, 7 et 8.
- **La passation**, §5.1 et §5.2.
- **Le README du dépôt.**
- Les rapports d'antériorité n'ont pas eu à être ouverts : aucune insertion de ces tranches ne les cite.
- **Les vérifications et corrections des groupes 1 à 5**, pour l'ordre d'application et pour que le cours dise partout la même chose (fiche 3 et K63, extraction supervisée, artefact de polarité).

## Contrôles d'ensemble

- **Composition.** Par langue : 30 renvois (8 aux volets 8 et 9, 22 au volet 10), 32 avertissements ponctuels (14 et 18) et 2 encadrés (volet 10).
- **Renvois.** Les 30 renvois de chaque langue pointent vers l'emplacement que donne l'index de la note d'ouverture ; le renvoi vers l'encadré du 2 octobre, parties 2 et 3 (n° 27 et n° 52), tombe bien après « En pratique — Contrastive Activation Addition », avant K47. Les deux encadrés de la tranche sont à leur maison : « Patching » en fin de fiche Patchscopes (n° 14), « Oracles d'activation » en fin de fiche LatentQA (n° 16).
- **Doctrine.** Aucune insertion ne dit qu'un contrôle aléatoire écarte le dommage. Partout où l'aléatoire paraît, il est dit nul de spécificité, et le dommage ne s'écarte qu'à dégradation appariée (Monitor, SelfIE, RepE, ITI, persona, Mallen, la note du §6b). Les nuls sont lus avec leur cas connu : sonde muette (n° 05, n° 65), score du SAD, désapprentissage (§9a), échange ou patch (encadré). Les corrections gardent cette doctrine.
- **Deux langues.** Un script (`_verif_groupe_6/parite.py`) compare, paire par paire, les citations (volets, fiches, pièges, n°, F·, K, G1, JB10, README, passation, programme, explication), les « aucune parade connue » et tous les nombres : aucun écart sur les 64 paires. Les places sont les mêmes, rubrique pour rubrique. Seul écart de sens : « gabarit » contre « placeholder » (encadré « Patching »), corrigé (15-16).
- **Forme.** Les formats fixes sont tenus (encadré, renvoi, avertissement ponctuel, « aucune connue ; on le dit » / « none known; say so »). Aucun sigle inventé : seulement des noms de méthodes ou de jeux (SAD, RMU, SGTM), des sigles courants (NLA, KL, MMLU, LoRA, AUROC) et des identifiants du cours (K47, K63, K71, G1, JB10, F·n, II.5). La plus longue citation fait huit mots (« that looks like a takeover attempt written by humans »). Rien ne dit « first ».
- **Chiffres.** Tous sont retrouvés dans leur source :
  - 25 % et 39 % : fiche 17 ;
  - 64,7 % : volet 10, n° 64 ;
  - 5 textes : README ;
  - environ 200 items : programme, partie 3 ;
  - 30 et 27 sorties : volet 10, n° 24 ;
  - 1 % de faux positifs : F·23 et F·50 ;
  - GPT-4.1-mini : fiche 8 ; Opus 4.1 : F·39 ; Mistral 7b : n° 05.

  Les corrections n'ajoutent aucun chiffre.
- **Lignes « À dire ».** Aucune insertion n'en modifie une, ni ne lui ajoute de chiffre. La note du §6b (FR n° 11) nuance la ligne « Dis-le comme une continuité… my second result measures it » : c'est le cours lui-même qui dit ailleurs « un cousin, déjà en distribution » (volet 6, §4 ; volet 11, réponse 12).
- **Place.**
  - **Volets 8 et 9.** Les 22 blocs de chaque langue suivent la dernière ligne d'un paragraphe. Aucun ne coupe un tableau, une liste ou un paragraphe.
  - **Volet 10, les renvois et les deux encadrés** : après la ligne « Lecture » qui clôt la fiche.
  - **Volet 10, 18 avertissements par langue** (FR n° 3, 7, 11, 21, 27, 33, 35, 39, 43, 49, 57, 61, 65, 67, 69, 73, 77, 83) : ils sont placés sous la rubrique qu'ils qualifient (« Le résultat, chiffré » ou « Ce que ça change… »).
    - Ils ne coupent aucune phrase.
    - Mais la fiche est une suite de lignes sans ligne vide, donc un seul paragraphe au rendu Markdown, et elle s'affiche en deux (l'observation 3 du bilan).
    - Je ne l'ai pas corrigé, car une correction ne peut pas les déplacer tous en fin de fiche. Huit fiches sur dix-huit (n° 21, 40, 51, 53, 54, 55, 58, 65) n'ont, après leur ligne « Lecture », aucun texte v3.6 où accrocher l'avertissement : il faudrait reprendre une ligne de la v3.5 dans « ancien », ce que la règle interdit.
    - Déplacer les dix autres seulement rendrait le volet incohérent.
    - Si la session principale tient au rendu, le remède est une nouvelle passe d'insertion de la tranche, ancrée sur les lignes « Lecture ». Le volet 7 en donne le précédent : ses avertissements y viennent en fin de fiche.

## Volets 8 et 9 (FR n° 1-22 / EN n° 23-44)

| FR / EN | Insertion | Constat |
|---|---|---|
| 1 / 23 | Avertissement, §2, sandbagging | N° 05 : élicité par prompt ou par mot de passe, QCM seulement, part stratégique écartée, sondes suggérées mais non essayées. K63 : la capacité, élicitée à budget fixé d'avance et rapportée comme une borne ; la propension, offerte sans être demandée dans deux versions tirées au hasard ; l'organisme dressé à se cacher. M7 : le budget fixé d'avance. **Juste.** |
| 2 / 24 | Renvoi | **Juste.** |
| 3 / 25 | Avertissement, §3, SAD | Justes : piège 2 ; fiche 2 (trois mesures « weakly positively correlated » chez Fable 5 ; chez Mythos Preview, le plus souvent non verbalisée) ; sujet 4 (la triangulation) ; explication §3 (l'organisme conditionné à l'évaluation). Faute : « en disant laquelle fonde quel chiffre » n'a pas sa source, M4 (« dis lequel, et lequel a fondé quel chiffre »). Le groupe 4 a fait la même correction pour le sujet 4. **Corrections 1-2.** |
| 4 / 26 | Avertissement, §3, LatentQA et Patchscopes | N° 16 : une copie fine-tunée lit, pas de vérité-terrain des latents. N° 14 : le calcul après le patch peut ajouter de l'information. Fiche 18 : variantes fine-tunées jamais vues, méthode indépendante. « Pour le patch, aucune connue » est cohérent avec l'encadré « Patching ». **Juste.** |
| 5 / 27 | Renvoi | **Juste.** |
| 6 / 28 | Avertissement, §4, persona | Justes : fiche 8 (corrélationnel, trait nommé d'avance, directions grossières, juge GPT-4.1-mini, un seul tour) ; F·31 (soustraire après coup réduit le trait, dégrade MMLU) ; M4, passation §5.2, volet 6 §2. Deux fautes :<br>• « un résultat prédictif, pas causal » contredit F·31 (« Ici elle agit — post-hoc — mais avec un coût de capacité » ; à ne pas dire, « Persona vectors only monitor ») et la fiche 8 (« en partie, pour piloter »). C'est le résultat **le plus fort** qui est prédictif (fiche 8, À retenir 2), et la note dit elle-même, une ligne plus loin, que le pilotage réduit le trait ;<br>• « pour l'extraction supervisée, aucune parade connue (fiche 8) » : le programme, partie 8, en donne une (le diffing par crosscoder cherche sans hypothèse). Le groupe 2 a corrigé de même l'encadré du pilotage.<br>**Corrections 3-4** : le plus fort est prédictif, le vecteur agit avec un coût, et l'effet ne dit le concept qu'à dégradation appariée (M4) ; F·31 est ajouté aux sources de la partition ; la parade crosscoder (programme, partie 8). |
| 7 / 29 | Renvoi | **Juste.** |
| 8 / 30 | Avertissement, §5, Lanham | N° 18 : « on most tasks ». Fiche 17 : 25 % et 39 % (†) ; « non-verbalisation » n'est pas « raisonnement caché » ; la surveillabilité est un ratio. Réponse 43 : la perturbation graduée (II.5). **Juste.** Observation : « not verbalized » et « hidden reasoning » traduisent le piège de la fiche 17 ; ce ne sont pas des citations. |
| 9 / 31 | Renvoi | **Juste.** |
| 10 / 32 | Renvoi, §6 | **Juste.** |
| 11 / 33 | Avertissement, §6b, « my second result measures it » | Volet 6, §4, et réponse 12 : « un cousin, déjà en distribution ». Fiche 7 et explication §2 : les détecteurs de F·29 sont des modèles fine-tunés par LoRA, pas des sondes. Parade : volet 6, §8 (deux familles, témoin conscient mais honnête) ; explication §3 ; passation §5.2 (doctrine). **Juste.** |
| 12 / 34 | Avertissement, §6b, coup probes et circuit breakers | Justes : n° 27 (citation de huit mots) et n° 28 (un attaquant qui ignore la sonde) ; n° 62 et fiche 19 pour la parade. Faute : « construire ses exemples à partir des générations réelles » prête au §C ce qu'il ne dit que des **négatifs** (« pas seulement de données synthétiques »). Les positifs d'une tentative de prise de contrôle ne se collectent pas (§G, les coup probes). **Corrections 5-6.** |
| 13 / 35 | Avertissement, §6c, Mallen | N° 30 : Bob, circuits naturels « likely overwrote », LogR moins causale à transfert comparable, question laissée ouverte. Programme, partie 8 : un organisme ne conclut que sur l'instrument. Passation §5.2 et M4. **Juste.** |
| 14 / 36 | Renvoi, §7 | **Juste.** |
| 15 / 37 | Avertissement, §7b, débat | N° 39 : inférence seule, juges LLM, pas de juge humain, « Strong positive evidence … we see neither ». §E : l'argument obfusqué. Programme, partie 3. **Juste.** Observations :<br>• « qu'ils attendaient » glose le « would be » des auteurs ;<br>• « aucune connue » au-delà de l'expertise humaine est cohérent avec l'encadré du débat et avec le jugement du groupe 5 (F·11). |
| 16 / 38 | Avertissement, §7d, Azaria et Liu | N° 51 (« lying » : des énoncés faux ordinaires) et n° 56 (modèles pré-entraînés ; calibration et hétérogénéité). F·62, sujet 1, passation §5.2. **Juste.** |
| 17 / 39 | Renvoi, §8 | **Juste.** |
| 18 / 40 | Avertissement, §8a, StrongREJECT et AgentHarm | N° 59 : grille, annotateurs humains, 313 questions « not large enough », robustesse à l'optimisation non testée. N° 60 : « proxies for harm », tâches faciles. Parade : programme, parties 3 et 8 (juge scellé distinct du juge d'entraînement, audit) ; G1 ; M4 (bras de référence réaliste, notation à l'aveugle). **Juste.** |
| 19 / 41 | Avertissement, §8b, rapid response | N° 63 : taux de succès des attaques, attaquant qui connaît la défense laissé ouvert, « may be inadequate ». G1 : classer deux fois. N° 62 : attaque optimisée contre le détecteur aussi. **Juste.** |
| 20 / 42 | Avertissement, §9a, désapprentissage | N° 64 : logit lens muet, 64,7 % rendus. N° 66 : sondes qui échouent, modèle jailbreakable. JB10 : petits modèles. §I et M5 : intervention, cas connu, borne. « Pour l'échelle, aucune connue » est cohérent avec l'encadré et avec le groupe 5. **Juste.** |
| 21 / 43 | Avertissement, §9b, AI Organizations | F·39 est juste (deux organisations simulées, Opus 4.1, limite écrite). Faute, que le groupe 4 avait signalée (FR l. 4147) :<br>• « un modèle peut lire le cadre comme factice (fiche 3) » glose mal le confondeur de la fiche 3, qui porte sur une simulation où « c'est faux » est vrai ;<br>• « contre un cadre que le modèle lit comme factice, aucune parade connue » contredit la parade K63, donnée juste avant pour ce cas.<br>**Corrections 7-8**, dans le sens des groupes 2 à 5 : K63 pour « remarquer le test » ; la phrase de la fiche 3 gardée telle quelle ; « Parade, en partie » ; seul le confondeur de la simulation lui-même reste sans parade, comme le groupe 5 l'a jugé pour F·38. |
| 22 / 44 | Renvoi, §9 | **Juste.** |

## Volet 10 (FR n° impairs 1-83 / EN n° pairs 2-84)

| FR / EN | Insertion | Constat |
|---|---|---|
| 1 / 2 | Renvoi, n° 01 | **Juste.** |
| 3 / 4 | Avertissement, n° 05 | N° 05 : la parade par sondes n'est qu'une suggestion ; le Mistral 7b verrouillé par mot de passe. Passation §5.2 et piège 3 : silence de sonde, cas connu, borne. Fiche 15 : implanté contre naturel, aucune parade. **Juste.** Place : voir « Contrôles d'ensemble ». |
| 5 / 6 | Renvoi | **Juste.** |
| 7 / 8 | Avertissement, n° 07, SAD | Justes : fiche 3 et piège 2 (auto-rapport) ; F·25 (la conscience verbalisée rate la non verbalisée) ; piège 3 (nul d'instrument) ; programme, parties 4 et 8 (l'organisme comme cas connu). Deux fautes :<br>• « Ce score » : le score du SAD couvre sept catégories, dont des tâches d'action ; la note ne vaut que pour stages-oversight ;<br>• la parade tire de la partie 8 du programme « la verbalisation n'étant jamais une preuve », quand la source dit « jamais une preuve **d'inhibition** », une règle pour vérifier une inhibition. La parade de ce cas est la triangulation du sujet 4, comme dans l'avertissement jumeau du volet 9 (FR n° 3).<br>**Corrections 9-10.** |
| 9 / 10 | Renvoi | **Juste.** |
| 11 / 12 | Avertissement, n° 08, Monitor | M4 : l'aléatoire n'écarte qu'une lecture, ni le dommage ni un concept voisin. N° 08 : « distracted », concepts trouvés sur le jeu d'évaluation. Programme, parties 3 et 7 ; README (jeu disjoint). **Juste.** |
| 13 / 14 à 19 / 20 | Renvois | **Justes.** |
| 21 / 22 | Avertissement, n° 13, SelfIE | M4 et passation §5.2 (doctrine) ; n° 13 et n° 16 ; K47 ; fiche 18. **Juste.** |
| 23 / 24 | Renvoi | **Juste.** |
| 25 / 26 | Encadré « Patching » | Justes : les limites 1 à 3, 5 et 6, et les parades 2 et 5, contre ces sources :<br>• n° 14 : calcul après le patch, prompt cible, contamination ;<br>• volet 6, §2, et programme, partie 8 : la partition, l'état complet comme plafond ;<br>• README : où l'on lit n'est pas où l'on cause ;<br>• volet 6, §8, et C bis : l'échange validé sur les pays.<br>Trois fautes :<br>• la parade 3 n'est attribuée qu'au README, qui constate sans recommander. Le programme, partie 8 (« chaque concept passe par l'ablation et le patch », plafond de l'état complet), est ajouté (**corrections 11-12**) ;<br>• la parade 4 dit « aucune connue » pour un patch de chemins fait sur 5 textes : il se refait sur un jeu plus grand, la taille étant fixée d'avance par une simulation de puissance (programme, partie 7 ; M5 : un nul sans puissance connue ne dit presque rien) (**corrections 13-14**) ;<br>• la limite 6 est durcie : « faussent » pour ce que les auteurs rangent dans « À faire ». En français, « gabarit » rendait mal « placeholder » (**corrections 15-16**). |
| 27 / 28 | Avertissement, n° 16, LatentQA | N° 16 : comparé au prompting, à RepE, au SFT et au DPO. M4 ; K47 ; programme, parties 7 et 8 ; volet 6, §2. **Juste.** |
| 29 / 30 | Encadré « Oracles d'activation » | N° 16 : pas de vérité-terrain ; une copie fine-tunée lit. Fiche 18 : variantes jamais vues, confabulation, suppositions « souvent fausses et mal calibrées », méthode indépendante, décodeur à part, coût, petits jeux, bancs simplifiés. Fiche 4 : le nul de CHIVE et la barre. **Juste.** |
| 31 / 32 | Renvoi | **Juste.** |
| 33 / 34 | Avertissement, n° 21, EC-finetuning | N° 21 : un LLM simule l'utilisateur, contrôles de stabilité et de longueur. Volet 6, §2 ; piège 6 ; programme, partie 3 (environ 200 items). **Juste.** |
| 35 / 36 | Avertissement, n° 24, Naihin | N° 24 : 30 et 27 sorties écrites à la main, pas d'agent qui trompe. F·24 ; F·23 (1 %, variantes bénignes appariées). **Juste.** |
| 37 / 38 | Renvoi | **Juste.** |
| 39 / 40 | Avertissement, n° 26 | N° 26 : piste boîte blanche, collusion plus subtile. Fiche 19 : détecteurs scellés. Passation §5.2. **Juste.** |
| 41 / 42 | Renvoi | **Juste.** |
| 43 / 44 | Avertissement, n° 27, coup probes | Sources : n° 27 ; piège 1 ; fiche 7 ; explication §3 ; programme, partie 3 ; volet 6, §8 ; passation, §5.1 et §5.2. **Juste.** |
| 45 / 46, 47 / 48 | Renvois | **Justes.** |
| 49 / 50 | Avertissement, n° 30, Mallen | N° 30. Volet 6, §8 : la sonde peut apprendre la fabrication ; rien ne prouve le cas réel. Passation §5.2 ; K71. « Parade, en partie. » **Juste.** |
| 51 / 52 à 55 / 56 | Renvois | **Justes.** |
| 57 / 58 | Avertissement, n° 40, Prover-Verifier Games | Le contrôle de M4 (un classifieur de la seule surface, au hasard) est juste. Faute : « pas d'exemples fabriqués » durcit le §C, qui dit « pas seulement de données synthétiques ». **Corrections 17-18.** |
| 59 / 60 | Renvoi | **Juste.** |
| 61 / 62 | Avertissement, n° 51, Azaria | N° 51 ; passation §5.2 ; F·62 ; sujet 1 ; F·50 (1 %) ; F·29. **Juste.** |
| 63 / 64 | Renvoi | **Juste.** |
| 65 / 66 | Avertissement, n° 53, RepE | N° 53 (un vecteur aléatoire parmi les baselines) ; M4 ; K47 ; programme, partie 7. **Juste.** |
| 67 / 68 | Avertissement, n° 54, CAA | Justes : les comparaisons (n° 54), la doctrine (M4), l'artefact (README), K47 et le programme, partie 3. Faute : « contre l'artefact de polarité, aucune parade connue ». Le volet M, M4, en donne :<br>• des paires qui ne diffèrent que par le trait, vérifiées par un classifieur de la seule surface ;<br>• la direction d'un concept rival, au même endroit, à dégradation appariée ;<br>• le témoin sans pression.<br>C'est la correction du groupe 5 pour F·7 (n° 23/24). **Corrections 19-20.** |
| 69 / 70 | Avertissement, n° 55, ITI | N° 55 (directions comparées, KL, « I have no comment ») ; M4 ; K47 ; programme, partie 7. **Juste.** |
| 71 / 72 | Renvoi | **Juste.** |
| 73 / 74 | Avertissement, n° 58, AgentDojo | N° 58 (« relatively simple attacks and defenses ») ; F·24. **Juste.** |
| 75 / 76 | Renvoi | **Juste.** |
| 77 / 78 | Avertissement, n° 63, Rapid Response | N° 63 ; F·24 ; G1. **Juste.** |
| 79 / 80, 81 / 82 | Renvois | **Justes.** |
| 83 / 84 | Avertissement, n° 65, WMDP | Piège 3 ; n° 64 ; partie C (une intervention tranche ; « not elicitable at this budget ») ; M4 (référence jamais entraînée), M5 (modèle connu pour masquer) ; §I. **Juste.** |

## Application

- `corrections_groupe_6.json` est un JSON valide de 20 corrections, construit par `travail/_verif_groupe_6/construire_corrections.py` à partir des lignes exactes de la v3.6.
- Chaque « ancien » est fait de lignes entières d'insertion v3.6 et y figure une seule fois ; une seule correction (13-14) prend deux lignes, la limite 4 de l'encadré avec sa parade. Aucune ligne d'« ancien » ne figure dans la v3.5.
- J'ai simulé en mémoire l'ordre de `appliquer.py corrections` : groupes 1 à 5, puis 6. Toutes les corrections antérieures passent ; les 20 du groupe 6 trouvent ensuite chacune leur texte une seule fois.
- Après la simulation, toutes les lignes de la v3.5 se retrouvent, dans l'ordre, en français comme en anglais. Les nouveaux textes n'ont aucune citation de quinze mots ou plus. Le livrable n'a pas été modifié.

## À signaler hors de ces tranches (non corrigé ici)

- **« Artefact de polarité : aucune parade connue »**, contredit par le volet M, M4 (ma correction 19-20, et la correction 11-12 du groupe 5). La formule reste à deux endroits :
  - volet 2, §C, encadré du pilotage : FR l. 825-826, EN l. 913-914 ;
  - volet 11 : FR l. 5133, EN l. 5376.
- **Le confondeur de la simulation.** Les groupes 2 à 4 ont retiré la clause « lu comme factice… aucune parade (fiche 3) ». Le groupe 5 a gardé « contre le confondeur de la simulation, aucune parade connue » (F·38). La correction 7-8 suit la synthèse des deux. Pour un cours homogène, les lignes que le groupe 4 signalait au volet 11 (FR l. 7104 et 7165) sont à traiter de même.
- **Les 18 avertissements du volet 10 placés entre deux rubriques d'une fiche** : voir « Contrôles d'ensemble », place. Non corrigé ; c'est à trancher par une nouvelle passe d'insertion si le rendu Markdown compte.
