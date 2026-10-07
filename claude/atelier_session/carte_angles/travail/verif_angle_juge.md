# Vérification de « angle : les raisons pour le juge » (`travail/angle_juge.md`)

État au 2 octobre 2026. Les numéros « l. » renvoient aux lignes de `angle_juge.md` ; ceux des pièces sont précisés à chaque fois (« rapport n » = rapports de la nuit, `ANTERIORITE_RAPPORTS_2026-10-02.md` ; « 1er oct. » = `ANTERIORITE_RAPPORTS_2026-10-01.md`).

**Ce que j'ai relu moi-même.**
- Le rapport 4 en entier (l. 727-1011).
- Dans les rapports 2, 3, 5, 6 et 7, et dans les axes C2 et D du 1er octobre, tous les passages qui touchent le juge, la notation, l'obfuscation et le retrait pendant l'entraînement.
- Le §4 et le §5.5 de la passation v1.2.
- Les consignes de l'agent 4.
- La phase du juge et les mesures du programme v1.1.
- Le complément de l'architecte.
- Les fiches, par recherche de mots.

**Ce que j'ai vérifié hors des pièces.**
- Le dépôt exp9 par curl sur raw.githubusercontent.com (13 fichiers). L'API de GitHub a renvoyé 403 une fois ; je n'ai pas réessayé.
- Trois recherches WebSearch, lues seulement en extrait.

Ces vérifications ne fondent rien dans la carte. Elles disent seulement si l'agent a bien vu ce qu'il décrit.

**Bilan.**
- Le fichier est riche, et ses chiffres tirés des rapports sont exacts : je les ai tous retrouvés.
- Trois corrections sont bloquantes :
  1. les trajectoires d'exp9 sont données pour établies, et attribuées à des sources qui disent le contraire ;
  2. le fichier emploie un libellé de lecture inventé ;
  3. le « libre » du retrait pendant l'entraînement est trop fort, et il manque le précédent relu par l'instance du papier.

---

## A. Corrections bloquantes

### 1. Les trajectoires DPO d'exp9 sont données pour établies, et attribuées à des sources qui disent le contraire

**Où.**
- l. 23, dans le verdict : « Les trajectoires de ses deux DPO sont en ligne… ».
- l. 86 : « Le dispositif est public, et ses trajectoires aussi », sources citées : « rapport 4 ; §4.4, n° 7 ; §5.5, n° 9 ».
- l. 352 : « déjà dans le dépôt ».
- l. 400, dans les formulations « plus tenables » : « des trajectoires DPO en ligne ».
- l. 414, formulation n° 5, fondée sur la figure.

**Ce que disent les sources, qui font foi.**
- Rapport 4, l. 735 : « Aucun résultat de ces entraînements n'est publié. »
- Rapport 4, l. 944 : `results/` n'a pas été ouvert, et les résultats DPO sont « donc inconnus ».
- §4.2, n° 1 : « Aucun résultat d'entraînement n'y figure. »
- §4.4, n° 7 : « Ses entraînements ne sont pas publiés. »

Aucune des trois sources citées en l. 86 ne dit que les trajectoires sont publiques.

**Ce que j'ai constaté** (par curl, par le vérificateur, hors §4.2, non établi).
- Les fichiers existent : `results/plots_v5/full_main.png` (194 889 octets, identique en taille à la copie `travail/.exp9_full_main_juge.png`), `full_lda.png` (40 408 octets, vide), les deux `BASE.jsonl` et `results/analysis/summary_v4.txt`.
- La figure trace les pas 0 à 500, conditions « leak » et « no_leak », sous les quatre cadrages.
- La description de l'agent est donc exacte. Le défaut est le statut du fait, pas le fait.
- La date de mise en ligne reste inconnue : l'API renvoie 403. On ne sait donc pas si la figure était déjà là au passage du rapport 4.

**Exigé.**
- **Le verdict et le niveau.** Reprendre le §4.4 tel quel : « ses entraînements ne sont pas publiés (§4.4, n° 7 ; rapport 4) ».
  - Le niveau élevé tient sans la figure : le dispositif et les scripts sont publics (rapport 4, l. 776).
  - Retirer « et ses trajectoires aussi » de la l. 86.
- **La formulation « plus tenable » n° 1** (l. 400) : retirer « et des trajectoires DPO en ligne ».
- **La formulation n° 5** (l. 414) : elle reste intenable, mais pour une autre raison.
  - La fonder sur le rapport 4, l. 734 : les deux DPO sont scriptés et mesurent, à chaque point de contrôle, la verbalisation contre la conduite.
  - Un dispositif public et scripté vaut « annoncé » au sens du niveau élevé.
  - Ne pas la fonder sur la figure.
- **La l. 352** : la déplacer dans la liste des relectures (l. 450-458).
- **Le reste.** Ce qui vient de `results/` va dans une seule note « à relire par l'instance du papier », sans chiffre et hors du verdict. Les l. 72-83 et 426-427 vont dans ce sens ; les l. 23, 86, 352, 400 et 414 le contredisent.

### 2. Le libellé « relu par curl par cet agent, hors §4.2 » n'est pas dans la liste

**Où.**
- l. 13 et l. 51-54.
- l. 65 : « confirmée par ma relecture des scripts ».
- l. 72-83 et l. 426.

**La règle.** La consigne donne une liste fermée de libellés : relu par l'instance du papier, rapport n (texte intégral, résumé seul, site tiers), extrait, non ouvert. Annoncer un libellé hors liste ne le rend pas recevable.

**Des faits issus de la même lecture n'ont aucun libellé.**

| Ligne | Fait | Source réelle |
|---|---|---|
| l. 66 | « dans le même ordre » | lecture de l'agent |
| l. 70 | « 50 prompts par point de contrôle » | lecture de l'agent |
| l. 96-98 | la version antérieure confondue | lecture de l'agent |
| l. 106 | « 154 » contre « 144 » renversements stricts | lecture de l'agent |
| l. 350 | « des préférences A/B demandées directement au juge » | absent du §4.2 et du rapport 4, qui ne citent que le PPO |

J'ai vérifié par curl : ces cinq faits sont exacts.
- `build_dpo_dataset.py` dit bien « SAME pairs in the SAME order ».
- Il décrit aussi la version antérieure confondue.
- `run_phase5_full.sh` fixe `EVAL_N_PROMPTS=50`.
- SUMMARY.md porte 154 dans son tableau et « 144 strict flips » dans deux passages.

Ils restent pourtant non établis pour la carte.

**Exigé.**
- **Le libellé.** Supprimer le libellé inventé.
- **Les faits de cette lecture.** Chacun passe dans la note « à relire » (correction n° 1), avec le chemin du fichier.
- **La « lecture à l'œil »** (l. 80-82) : la retirer de la carte. Une impression sur une figure n'est pas une source, même « à ne pas citer ».
- **La « leçon de conception »** (l. 96-98) peut rester, refondée sur une source admise.
  - Rapport 4, l. 767 : « La perte porte sur toute la séquence, raisonnement et réponse », et seules les étiquettes diffèrent.
  - Cela suffit pour recommander que, dans le bras « le juge ne voit que l'action », la perte porte toujours sur les raisons.
  - L'histoire de la version antérieure va dans la note « à relire ».

### 3. Le « libre » du retrait de « je suis noté » pendant l'entraînement est trop fort, et le précédent relu manque

**Où.**
- l. 31 : « libre dans tout ce que les rapports ont vu ».
- l. 35.
- l. 283 : Wu et Tang présentés comme « le précédent de méthode le plus proche ».
- l. 339 : le retrait parmi « les deux morceaux les plus sûrs ».
- l. 391-395 : formulation n° 2.

**Ce que disent les sources.**
- **§4.4, n° 5** : pour le retrait pendant l'entraînement, « les méthodes sont prises ou annoncées, l'application est libre ».
- **Rapport 3, verdict** (l. 691-698) : le retrait pendant l'entraînement est « partiellement pris ».
- ***Routing Subspaces*, annexe I** : relu sur la source par l'instance du papier (§4.2, n° 7) ; rapport 3, l. 545-547, niveau moyen.
  - Une pénalité projette hors du flux, pendant le fine-tuning, les k premières directions évaluation/déploiement. Elle n'empêche pas l'installation : 26,0 à 33,3 points, contre 29,8 sans pénalité.
  - La direction ré-estimée a tourné : cosinus de 0,27 à 0,52 avec la référence.
  - C'est le précédent publié le plus proche du retrait, pendant l'entraînement, d'une représentation dont dépend une conduite conditionnelle. Il est absent du fichier.
  - Le §5.5, n° 4, en tire une conséquence : ré-estimer la direction pendant le retrait.
- **CAFT** (rapport 7, l. 1783-1795, texte intégral ; §4.3 : poster de la conférence principale d'ICML 2026) : retrait par projection pendant le fine-tuning, contre des vecteurs orthogonaux aléatoires.
- **Santos-Grueiro** (rapport 3, l. 553-564, texte intégral, moyen ; modèles corrigés au §4.3) : invariance adverse au régime évaluation/déploiement pendant le fine-tuning.
- **Nadaf** (rapport 3, l. 578-588, moyen) : projection pendant tout le fine-tuning, contre un sous-espace aléatoire de même rang.
- **BLOCK-EM** (rapport 3, l. 598-604, moyen, pour le ré-encodage).
- **Drake et Eberstadt** (rapport 3, l. 621-626, faible ; §5.5, n° 4) : piloter à l'écart pendant l'entraînement peut doubler la diffusion.
- **Annoncés** :
  - Lundqvist (§4.2, n° 3, relu ; rapport 6, l. 1465 : « moyen pour le retrait pendant l'entraînement ») ;
  - *Infohazard Evaluations* (voir le manque n° 2).

**Exigé.**
- **La troisième sous-question** (l. 31-33) devient : « méthode prise, variantes proches publiées (*Routing Subspaces*, annexe I, relu ; CAFT ; Santos-Grueiro ; Nadaf) ou annoncées (Lundqvist ; *Infohazard Evaluations*), niveau moyen ; l'application à "je suis noté" pendant un RL ou un DPO noté par un juge reste libre (§4.4, n° 7 et n° 5) ».
- **Un nouveau travail dans la liste** : *Routing Subspaces*, annexe I, au niveau moyen pour cette sous-question, placé avant Wu et Tang.
- **La l. 283** : remplacer « le précédent de méthode le plus proche » par « un précédent en RL, sur une autre direction ». Les précédents du retrait pendant l'entraînement sont CAFT et *Routing Subspaces*, annexe I.
- **La formulation n° 2** (l. 391-395) : elle reste tenable, puisqu'elle porte sur « being graded », sur un RL ou un DPO, et à témoins de même rang et à dégradation appariée. Mais sa justification doit citer *Routing Subspaces*, annexe I, et CAFT, en plus de Wu et Tang et de la card.
- **La l. 339** : le retrait n'est pas « sûr ». Il est le moins publié, mais sa méthode est prise, et la seule tentative proche a échoué par rotation.

---

## B. Corrections non bloquantes

### 4. Baker et al. : un niveau et une place dans le verdict sur la foi d'un extrait
- **Où** : l. 24, l. 143-162, l. 404.
- **Le statut.** Le libellé « vu par extrait de recherche, non ouvert » est juste. Mais il porte un niveau moyen et une place dans le verdict.
- **Exigé** : écrire « moyen, provisoire (non ouvert) », et le signaler aussi l. 24.
- **La l. 146 est inexacte** : « Auteurs non relevés dans les pièces ». Les fiches nomment « Baker et al., OpenAI » (`LECTURES_PRIORITAIRES_FICHES_2026-10-01.md`, l. 299 et l. 1631 ; fiche, non relue). Un extrait de recherche donne la liste des auteurs (vu par extrait de recherche, non ouvert).

### 5. La formulation tenable n° 1 repose sur deux travaux non ouverts
- **Où** : l. 388-390.
- **Kaufmann et al.** : l'article n'a jamais été ouvert (rapport 4, l. 854 et l. 958). Son titre annonce un cas « Aligned » de récompense sur le raisonnement. Le fichier le sait (l. 461) mais déclare quand même la formulation tenable.
- **Baker et al.** : vu par extrait seulement.
- **Projets annoncés à mentionner** : Cody Wild (récompense sur la pensée ou sur la sortie ; échéance du 19 décembre) et Panaganti et Srinivas (« la fidélité du raisonnement comme signal de RL », rapport 4, l. 934, non ouvert).
- **Exigé** : « tenable sous réserve de la lecture de Kaufmann et al. et de Baker et al. ».

### 6. La deuxième sous-question oublie deux sources du rapport 4
- **Où** : l. 26-29.
- **Højmark et al. et le Risk Report.** Le verdict du rapport 4 (l. 976) les nomme, et le §4.4, n° 7, met Højmark en tête des « autres travaux ».
- ***Generalization Hacking*** porte sur la conscience d'être entraîné (rapport 7, l. 1720). Le programme distingue « je suis noté » de « je suis évalué » (programme v1.1, l. 155).
  - Écrire « les indices d'entraînement », pas « je suis noté ».
  - Le rapport du 1er octobre (l. 139) dit « entraîné ou noté » : c'est à citer tel quel.

### 7. Statuts de lecture à corriger

| Ligne | Écrit | Ce que disent les rapports | Exigé |
|---|---|---|---|
| l. 254, Kretschmar | « Rapport 4, texte intégral (WebFetch) » | Rapport 4, l. 870 : « texte via WebFetch », sans « intégral ». Rapport 3, l. 615 : « page complète ». | « Rapport 3, texte intégral » ; rapport 4 par WebFetch. |
| l. 272, Mallen et Greenblatt | « Rapport 4, résumé seul : le mode de lecture n'est pas indiqué » | Rapport 4, l. 900 : titre, auteurs et date, sans mode ni contenu. Le libellé se contredit lui-même. | « Non ouvert (titre cité par le rapport 4) ». |
| l. 362, Cody Wild | « Rapport 6, texte intégral (page de détail, d'après sa liste de sources) » | Rapport 6, l. 1466 : l'URL seule. l. 1568 : « 13 pages de détail », sans liste. Rapport 4, l. 927 : sans mode. | Ne pas écrire « texte intégral ». Écrire « décrit par les rapports 4 et 6, mode de lecture non dit », et garder la relecture (l. 465). |
| l. 345, FAQ de SPAR | « rapport 6, texte intégral » | Rapport 6, l. 1450 : « lu dans la FAQ ». | Retirer « texte intégral » ; le §4.4 suffit. |
| l. 284, *Metagaming* | « Rapport 6, résumé seul » | Rapport 6, l. 1443 : résumé automatique WebFetch. Le contenu (« survit à l'entraînement d'alignement ») vient du 1er oct., axe C2, l. 131, et du rapport 4, l. 901. | Citer ces deux sources. Ajouter l'essai de pilotage contrastif évaluation/déploiement « aux résultats mitigés » (1er oct., l. 132 et l. 364), utile pour la deuxième sous-question. |
| l. 285, *Training a Misaligned Reward Seeker* | « Qi … Hubinger » | Rapport 6, l. 1340 : auteurs « repris d'une référence sur la page MATS de Cozmin Ududec ». | Le dire. |
| l. 370, Aaliyan | rangé sous « rapport 4 » | « Tülu 3.1 8B » vient du rapport 2, l. 423 ; le rapport 4 (l. 937) ne nomme pas le modèle. | Citer le rapport 2. |
| l. 367 et l. 371, Igor Ivanov | « rapport 4, faible, aucune date propre » | Rapport 4, l. 928 : aucun niveau. Rapport 6, l. 1469 : « faible à moyen ». Tous ces projets SPAR d'automne ont l'échéance du 19 décembre. | Corriger le niveau et la date. |
| l. 203 et l. 208, *Generalization Hacking* | « Rapport 7, texte intégral » | Le libellé est défendable. Mais le rapport 7, l. 1578, dit que WebFetch résume le texte. | Vérifier la citation « averaging 15 pp… » avant de la reprendre (relecture n° 7, déjà prévue). |

### 8. Le projet SPAR de Lundqvist n'a pas de niveau
- **Où** : l. 355-359.
- **Exigé** : niveau moyen pour la sous-question du retrait. Sources : rapport 6, l. 1465 ; rapport 4, l. 977, « variante… annoncée ». Échéance : le 19 décembre 2026.
- **Son rôle** : le rapport du 1er octobre (l. 447) et le complément de l'architecte (l. 56) le disent « mentor » de ce projet. La l. 103 le dit « fellow SPAR » d'après un extrait. Il faut garder les deux sources séparées.

### 9. Le rattachement d'exp9 : « à tort » n'est pas fondé
- **Où** : l. 104 et l. 432.
- **Le problème.** « Le même extrait attribue à tort les chiffres de Kretschmar » et « l'extrait mêle deux sources » sont des inférences, tirées d'un extrait non ouvert.
- **Mon contrôle.**
  - Mon extrait (requête sur le dépôt et Goodfire) présente Lundqvist comme fellow SPAR chez Goodfire, sans le chiffre de 14 % à 3 % (vu par extrait de recherche, non ouvert). Je n'ai pas pu revoir l'extrait cité.
  - Exp9 et Kretschmar utilisent le même organisme (rapport 4, l. 758 et l. 873). Un lien entre les deux travaux ne peut donc pas être exclu.
- **Exigé** : écrire « à vérifier », et ne rien affirmer sur ce lien.

### 10. « Ce qui reste libre » mêle le programme et des propositions
- **Où** : l. 315-329.
- **Ce qui vient du programme v1.1** :
  - les trois bras, plus le contrôle aléatoire de même rang (programme, l. 455-461) ;
  - la cohérence contrefactuelle, l'ablation du principe après le RL, le gain au juge moins le gain aux audits, et l'écart sous indices « noté » ou « non noté » (l. 196-199) ;
  - la fidélité des raisons (l. 219).
- **Ce qui est ajouté, et que le fichier ne signale pas** :
  - **la perte sur les raisons dans le bras « action seule »** : elle s'appuie sur la lecture non établie (correction n° 2) ; le rapport 4, l. 767, suffit à la fonder ;
  - **l'obfuscation dans les deux bras** : proposée au §5.5, n° 5, sans décision de Lazar. Le complément de l'architecte (l. 57) dit qu'elle est absente de la v1.3 ;
  - **la « sonde neuve après le RL »** : la phase du juge prévoit seulement de refaire le test du regard (programme, l. 463). La sonde neuve appartient à la phase du retrait (l. 187).
- **Exigé** : marquer ces trois points « proposé, non décidé ».

### 11. La prise de contact
- **Où** : l. 353.
- **Le constat.** La formulation concorde avec la réponse de Lazar du 2 octobre (« non pas encore »), transmise avec la tâche. Mais la passation la dit encore « sans réponse » (§3, n° 4 ; §6, n° 1).
- **Exigé** : citer cette réponse et sa date, et écrire « pas encore », pas « pas de contact ».

### 12. Le billet d'OpenAI sur la notation accidentelle de la chaîne de pensée
- **Où** : l. 273-276.
- **Le statut est juste.** Mais alignment.openai.com n'est pas sur la liste des domaines refusés. Il faut ouvrir la page avant d'en faire « la meilleure motivation empirique de l'angle ».
- **Mon contrôle.** Mon extrait donne une proportion d'échantillons touchés. Comme la règle l'exige, elle ne doit pas être citée.

---

## C. Les manques

1. ***Routing Subspaces*, annexe I, et les méthodes de retrait pendant l'entraînement** : CAFT, Santos-Grueiro, Nadaf, BLOCK-EM, Drake et Eberstadt, *Obfuscation Atlas* (sonde neuve après RL ; rapport 3, l. 606-611). Voir la correction n° 3.

2. ***Infohazard Evaluations*** (Shi Feng, Taslim Mahbub, Arush Tagade ; SPAR, automne 2026 ; rapport 2, l. 422 ; §4.4, n° 5, « non relu »).
   - Le projet annonce de comparer des méthodes d'entraînement qui gardent la reconnaissance de l'évaluation en retirant son influence sur la conduite.
   - À ajouter aux projets annoncés, avec l'échéance du 19 décembre.
   - Niveau moyen à faible pour la sous-question du retrait : il porte sur l'évaluation, pas sur la notation.

3. ***Training on Documents About Monitoring Leads to CoT Obfuscation*** (arXiv 2605.15257).
   - C'est un repère des consignes de l'agent 4 (l. 333).
   - Il est vu sans être ouvert au 1er octobre (axe D, l. 104 et l. 471). Le rapport 4 a tracé ses citations entrantes (l. 1006).
   - Faible, non ouvert : à mettre parmi les travaux vus et non ouverts.

4. ***Chain of Thought Monitorability*** (Korbak et al., arXiv 2507.11473).
   - Repère des consignes de l'agent 4 (l. 335). Citations tracées par le rapport 4 (l. 1006). Fiches, l. 1571-1574.
   - Faible, à citer.

5. **Le pilotage préventif pendant l'entraînement**, que Lundqvist annonce comme méthode.
   - Samyani … Nishimura-Gasparian (1er oct., l. 464 ; rapport 3, l. 635, faible).
   - *In-Training Defenses Against Emergent Misalignment* (Kaczér … Mai ; rapport 6, l. 1441 ; rapport 3, l. 657).
   - Faibles, à citer avec le projet de Lundqvist.

6. ***Stress Testing Deliberative Alignment*, §8** (rapport 4, l. 818-828, texte intégral).
   - Après un RL de capacités, les citations de la spécification passent de 81,5 % à 65,8 %, et les actions cachées montent légèrement.
   - C'est la seule mesure trouvée de raisons écrites qui faiblissent sous un RL ultérieur, sans juge qui les voie. Faible pour cet angle.

7. **Le juge persuadé** (passation v1.2, §5.1, d'après la fiche 3 ; un seul moniteur ; non relu).
   - Un moniteur qui lisait la chaîne de pensée aurait signalé environ 1 % des actions, contre environ 50 % sans elle.
   - C'est la motivation directe de « ce que voit le juge ». À citer en motivation, avec son statut.

8. **La card Fable 5, §6.5.1.2** (rapport 4, l. 981) : « cinq vecteurs témoins à dégradation négligeable ».
   - La l. 141 dit que la card n'a qu'un témoin sans contenu. C'est vrai du §6.4.2.2.1, pas de la card entière.
   - Préciser la section.

9. **Exp9, SUMMARY.md, l. 278** (vu par curl par le vérificateur ; non établi, à faire relire avec le reste du dépôt).
   - Environ 78 % des paires gardent le même choix dans les deux conditions.
   - Le contraste DPO d'exp9 ne porte donc que sur une minorité d'étiquettes. Cela pèse sur la lecture de sa figure, et sur la puissance d'un bras du programme qui ne diffère que par l'étiquette du juge.

---

## Ce qui est juste et peut rester tel quel
- **Exp9 :**
  - organisme, juge, 27 405 rollouts, −0,58 [−0,65 ; −0,52] et « It penalizes verbalization, not behavior » (§4.2, n° 1) ;
  - phase 5 : 500 pas, mêmes paires, perte sur toute la séquence, BigCodeBench, quatre cadrages, trois mesures (rapport 4, l. 766-773) ;
  - « ce qui le sépare du programme » (rapport 4, l. 778-782).
- **La card Fable 5 :**
  - lecture (rapport 4, texte intégral) et correction du §4.3 bien reprises ;
  - citation « no training process changes… » exacte (rapport 4, l. 795) ;
  - niveau moyen conforme au rapport 4.
- **Les chiffres repris des rapports.** Tous sont retrouvés : Højmark (87 %, 9 %, 40 %, 24 %), Kretschmar (14 % → 3 %, 86-89 %, 10 % → 29 %), le Risk Report (0,2 % à 5,1 %, 2,7 % ; 5 % → 40 %) et *Generalization Hacking* (12 à 21 points, +14 au pas 700).
- **Les statuts justes :**
  - Betley et al. : rapport 6, texte intégral ; le relèvement à moyen est motivé ;
  - Wu et Tang : rapport 3, texte intégral ; v3 du 20 août ; réplication sur Qwen3-8B, conforme au rapport 3, l. 496 ;
  - Maniyar et al., Meier et al., Hao, Macar, Cox, Anwar, Montoya, Gaya, Imran et Africa.
- **Le complément de l'architecte**, correctement cité : « un dépôt public du mentor », et l'obfuscation absente de la v1.3.
- **Les contradictions** n° 1, 3, 5 à 8 et 10 sont bien posées. Pour la n° 1, le rapport 6 ne cite ni exp9 ni la card : écrire « ne les cite pas » plutôt que « n'a vu ».
- **L'écriture** : ni sigle du programme, ni « first ».
