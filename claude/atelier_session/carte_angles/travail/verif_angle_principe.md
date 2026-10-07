# Vérification de « angle : le principe localisé » (angle_principe.md)

Vérification sceptique, 2 octobre 2026. Chaque affirmation de la fiche a été confrontée aux passages des rapports et de la passation, relus directement :
- rapport 3 de la nuit, en entier (lignes 486 à 726) ;
- l'axe « test causal interne » du 1er octobre, en entier (lignes 228 à 351) ;
- les quatre axes du 1er octobre ;
- les rapports 1, 2, 5, 6 et 7 de la nuit, ainsi que les passages du rapport 4 qui touchent l'angle ;
- la passation v1.2, §1 à §6 et annexe A ;
- les consignes de la nuit (niveaux de danger, consigne de l'agent 3) ;
- la partie 1 et la partie 11 du programme v1.1 ;
- la partie ouverte du complément de l'architecte.

Six recherches web ont été faites pour contrôler les affirmations que la fiche tire du web. Tout ce qui en vient est **vu par extrait de recherche, non ouvert**, et ne fournit aucun chiffre.

Les numéros de ligne renvoient à `ANTERIORITE_RAPPORTS_2026-10-02.md` (« nuit, l. … ») et à `ANTERIORITE_RAPPORTS_2026-10-01.md` (« 1er oct., l. … »).

---

## A. Corrections bloquantes

### 1. Le niveau de danger de Gurnee et al., §7 : hors définitions, et mal attribué
- **Ce qu'écrit la fiche** :
  - « Danger : moyen, proche de l'élevé » ;
  - à la contradiction n° 2 : « Tranché par le §4.2, n° 2 et le §4.4 : moyen, proche de l'élevé pour cet angle ».
- **Pourquoi c'est faux** :
  - « Moyen, proche de l'élevé » n'est pas un niveau. Les consignes en définissent trois : élevé, moyen, faible (consignes, l. 208 à 212). La formule vient du rapport 3 (nuit, l. 529).
  - Le §4.4, n° 4, ne donne **aucun** niveau : il classe seulement l'angle comme partiellement pris.
  - Le §4.4, n° 8, dit au contraire « danger élevé pour la présence des concepts avant la décision et pour leur nécessité, après un entraînement par principes ». Le rapport 5 dit de même (nuit, l. 1036).
  - Selon la définition, est élevé un travail après lequel « on ne pourrait plus écrire « to our knowledge » pour cet angle ». La fiche écrit elle-même qu'on ne peut plus l'écrire « sur le fait que ce gain passe par une représentation localisable ». Sa première ligne de la table des formulations intenables le confirme.
- **Correction exigée** :
  - élevé pour la sous-question « le gain d'un entraînement par principes est-il porté par des directions internes dont l'ablation le défait ? » (§4.2, n° 2, relu ; §4.4, n° 8) ;
  - moyen pour l'angle tel que le programme le pose : rang, contrôles de même taille à dégradation appariée, action identique, modèles ouverts, cas positif (rapport 3, l. 530 à 536) ;
  - à la contradiction n° 2, retirer l'attribution au §4.4 du niveau « moyen, proche de l'élevé ».

### 2. *Routing Subspaces* : « le rang n'est pas balayé » contredit le §4.2, n° 7 (relu)
- **Ce qu'écrit la fiche** : « le rang n'est pas balayé : une coordonnée, et le rang supérieur comme catégorie d'échec ». La table des travaux de danger moyen range aussi « balayage du rang » parmi ce qui lui manque.
- **Ce que dit la source relue** : l'annexe I projette pendant le fine-tuning les k premières directions singulières, k ∈ {1, 2, 3, 5, 10}, sur une cellule (Gemma-2-2B, sous-performance délibérée). Le résultat : de 26,0 à 33,3 points, contre 29,8 sans pénalité (passation v1.2, §4.2, n° 7, relu sur la source par l'instance du papier). Le rapport 3 l'écrit aussi (nuit, l. 545).
- **Correction exigée** :
  - écrire : « pas de balayage du rang pour la localisation, qui se fait sur une coordonnée ; un balayage de k de 1 à 10 pour le retrait pendant l'entraînement, sur une seule cellule (relu) » ;
  - corriger la table dans le même sens ;
  - citer ce balayage à côté de la deuxième formulation « to our knowledge » de la fiche, qui porte sur le rang minimal (voir la correction B.12).

### 3. *Constitutional adapters* : un statut de lecture faux pour le rapport 3
- **Ce qu'écrit la fiche** : « Rapports 1 et 3, et rapport du 1er octobre (axe combinaison exacte) : par pith.science ».
- **Ce que disent les rapports** :
  - le rapport 3 écrit « Lu : résumé et texte ciblé » (nuit, l. 640) et, plus loin, « Je n'ai pas utilisé pith.science » (nuit, l. 681) ;
  - le rapport 1 l'a bien lu par pith.science (nuit, l. 147) ;
  - l'axe « raisons contre actions » du 1er octobre aussi (1er oct., l. 95), et non le seul axe « combinaison exacte » (1er oct., l. 437).
- **Correction exigée** :
  - rapport 7 : résumé seul, lu par des sites tiers (nuit, l. 1681 à 1692) ;
  - rapport 1 et axes « raisons contre actions » et « combinaison exacte » du 1er octobre : lu par un site tiers (pith.science) ;
  - rapport 3 : « résumé et texte ciblé », source non précisée, sans pith.science ;
  - le rang 4 vient de l'axe « combinaison exacte » (pith.science, 1er oct., l. 438) et du rapport 3 (nuit, l. 641). Il reste non établi.

### 4. Un prolongement déclaré « libre » sans que personne l'ait cherché
- **Ce qu'écrit la fiche** : « Deux prolongements, libres eux aussi », dont « la géométrie entre la représentation « je suis évalué » et le sous-espace du principe ».
- **Pourquoi c'est trop fort** :
  - Aucun des onze rapports n'a cherché cette géométrie. La consigne de l'agent 3 ne la nomme pas (consignes, l. 243 à 245).
  - Le §4.4, n° 8, ne la range pas parmi ce qui est libre.
  - La phrase du rapport 2 que cite la fiche (« sans les croiser », nuit, l. 317) porte sur le croisement entre l'entraînement et l'ablation, pas sur une géométrie.
- **Correction exigée** : « non cherché par les onze rapports », pas « libre ».
- **L'autre prolongement**, le lien entre le rang et la charge, est bien libre selon le §4.4, n° 8, le §5.5, n° 9, et le rapport 5 (nuit, l. 1212). Mais il doit nommer ses voisins : voir le manque C.4.

### 5. « Leur ablation l'annule » : un constat plus fort que les chiffres relus
- **Ce qu'écrit la fiche** : dans le verdict, « Le gain d'un entraînement par principes passe par des concepts implantés, et leur ablation l'annule ». La table des formulations intenables reprend « dont l'ablation l'annule ».
- **Ce que disent les chiffres relus** (§4.2, n° 2) :
  - fabrication : le modèle entraîné revient de 0,07 à 0,22, et la base reste à 0,25 ;
  - tromperie : le modèle entraîné revient de 0,05 à 0,23, mais la base passe aussi de 0,38 à 0,48.
  - La fiche écrit elle-même, plus bas, que sur la tromperie « rien ne sépare le retrait du principe d'un dommage non spécifique ».
- **Correction exigée** : « leur ablation défait presque tout le gain sur la fabrication ; sur la tromperie, elle n'en défait qu'une partie, et la même ablation dégrade aussi la base (§4.2, n° 2, relu) ».

---

## B. Corrections non bloquantes

1. **Le titre de Nakamura (contradiction n° 5, et la fin de l'entrée n° 2).**
   - « La page abs porte maintenant un autre titre » est trop fort pour un extrait de recherche. Le §4.2, n° 8 (relu) fait foi tant que le papier n'est pas relu.
   - Mes extraits de ce matin donnent pour la page abs le titre *An Effective-Rank Audit of Alignment-Induced Activation Shifts: Confound Control, Constructive Calibration, and Limits*. Dans les mêmes résultats, le PDF et le HTML v3 portent l'ancien titre (vu par extrait de recherche, non ouvert). Rien n'y dit quelle version est la plus récente.
   - « Annonce peut-être une révision des conclusions » est une spéculation : à poser en question, pas en indice.
2. **Nakamura, « pas de cas positif en distribution distinct du test ».** Aucune source. Le rapport 3 donne trois écarts : l'objet est le refus, pas de hors distribution, pas de contrôle de dégradation (nuit, l. 575). Retirer ce quatrième écart ou le marquer comme non établi.
3. **Nakamura, « Pour la conception ».** Le §5.5, n° 3 dit seulement qu'il faut extraire le sous-espace par différence de différences à gabarit contrôlé. Il ne dit pas que le bras texte neutre fournit cette différence. C'est une proposition de la fiche : l'écrire comme telle.
4. **Le verdict compte trois morceaux occupés, le §4.4, n° 4, quatre travaux.**
   - *Routing Subspaces* manque au verdict, alors que le rapport 3 le range dans « la méthode » : localisation, contrôles appariés, contrôle côté déploiement (nuit, l. 687).
   - Dans le même verdict, marquer que le contenu de Nakamura n'a pas été relu (§4.2, n° 8 ; §4.4, n° 4 : « non lu »).
5. **Le statut de lecture de Gurnee et al.**
   - Le rapport 2 manque : il a lu le texte intégral des §5.1, §7 et de l'annexe A.21 (nuit, l. 312).
   - Dans le verdict, « sans balayage du rang ni contrôle de même taille (…, relu sur la source) » mélange deux statuts. L'absence de contrôle de même taille vient du §4.2 et ne vaut que pour cette section. L'absence de balayage du rang vient du rapport 3 (nuit, l. 533).
6. **La contradiction n° 4.** L'axe « raisons contre actions » du 1er octobre nomme bien Lindsey : « W. Gurnee, J. Lindsey » (1er oct., l. 96). Seul l'axe « combinaison exacte » ne l'avait pas relevé (1er oct., l. 407).
7. **La contradiction n° 6 (*Routing Subspaces*).**
   - L'axe « combinaison exacte » dit « cinq modèles ouverts », sans l'écart de 2 à 9 milliards (1er oct., l. 384).
   - Le rapport 2 nomme Gemma-2, Qwen-2.5-7B et Llama-3-8B (nuit, l. 352).
   - L'extrait de recherche parle de quatre instances complètes et d'un cinquième modèle pour la localisation : c'est compatible avec cinq modèles, pas « un autre décompte ».
   - Les trois auteurs (Konrad, Tanyel, Ayvaz) et l'acceptation à NeurIPS 2026 sont bien dans les extraits (vu par extrait de recherche, non ouvert).
8. **Le niveau d'*Inoculate or Reflect?* est à revoir.**
   - Le rapport 5 le classe moyen (nuit, l. 1056) : c'est le seul usage trouvé de la réflexion contrefactuelle sur un 8B ouvert, avec un patching entre deux fine-tunes d'une même base (nuit, l. 1053).
   - La consigne de l'agent 3 range dans l'angle « tout travail qui localise, par une intervention causale », par ablation ou patching, ce qu'un entraînement par raisons ou par constitution a changé (consignes, l. 243).
   - Un niveau moyen se défend donc pour une partie de l'angle. Au minimum, écrire le niveau du rapport 5, et que la lecture ne repose que sur deux résumés produits par l'outil (nuit, l. 1050).
9. **Des libellés incohérents.**
   - Pour Jain et al., la fiche choisit « résumé seul » parce que la lecture n'est pas précisée. Pour Gupta et Gupta, dans le même cas, elle choisit « non ouvert ».
   - Or « non ouvert » affirme que personne ne l'a ouvert, alors que le rapport 3 en résume le contenu (nuit, l. 645).
   - Harmoniser : le même libellé pour les deux, avec la mention « lecture non précisée par le rapport ».
10. ***Safety Reasoning with Guidelines*.** Le rapport 1 se trompe sur le titre et aussi sur le dernier auteur : il donne Dacheng Tao (nuit, l. 154), alors que le dernier auteur est Minhao Cheng (§4.2, n° 4, relu).
11. ***Synthetic Persona Pretraining*.**
    - Le rapport 7 ne dit rien de l'ablation (nuit, l. 1663 à 1678). L'affirmation sur la direction de refus vient des axes « raisons contre actions » (1er oct., l. 26) et « combinaison exacte » du 1er octobre (pith.science, 1er oct., l. 420), et du rapport 5 (nuit, l. 1170).
    - Elle est aussi déformée. La source dit que tous les modèles perdent leur robustesse, mais que les modèles entraînés ainsi gardent leurs choix de valeurs. La fiche écrit seulement « les modèles gardent leurs choix de valeurs ».
12. **La deuxième formulation « to our knowledge » de la fiche** (« minimal intervention rank … reason-based training … open-weight models »).
    - Elle est tenable, mais à resserrer : « … the advantage of reason-based over action-only training at identical actions … ».
    - Il faut la placer à côté de ses voisins : Nakamura (rang du refus après alignement, modèles ouverts, rapport 3) ; *Routing Subspaces*, annexe I (k de 1 à 10, relu) ; Abu Shairah et al. (une seule direction ne suffit plus) ; le §7 (ensemble fixe de 176 et de 63 vecteurs).
13. **La table des quatre travaux de danger moyen.** « Cas positif en distribution » est donné comme manquant au §7. Or la fiche range elle-même « la nature des contextes d'ablation, en distribution ou non » parmi les relectures à faire. Écrire « non établi ».
14. ***Beyond Shallow Alignment*.**
    - « Des bancs de jailbreak externes, sans familles tenues à part » n'a pas de source. Elle vient de l'axe « test causal interne » du 1er octobre (1er oct., l. 243).
    - « Un risque » (le balayage du rang possible sur ses points de contrôle) est une inférence de la fiche : l'écrire comme telle.
15. **La réplication de UK AISI sur GLM-5.**
    - « Rapport 2, texte intégral, lu en partie » se contredit. Le rapport 2 dit « via l'API markdown, partiellement » (nuit, l. 345).
    - Ajouter les axes « regard » et « combinaison exacte » du 1er octobre (1er oct., l. 185 à 190 et l. 459).
16. ***Understanding and Preserving Safety in Fine-Tuned LLMs*.** La fiche dit les auteurs « non donnés par l'extrait ». Mes extraits les donnent : Jiawen Zhang … Ruoxi Jia (vu par extrait de recherche, non ouvert).
17. **Nadaf, « pas de balayage du rang rapporté ».** Écrire : « aucun rapport ne mentionne de balayage du rang ».
18. **Les projets annoncés.**
    - « « première étape » » : les guillemets donnent pour une citation la paraphrase d'un résumé de l'outil (nuit, l. 1185). Retirer les guillemets.
    - Pour Cadile, « Aucune prise de contact n'est prévue pour l'instant » a désormais une source : la réponse donnée le 2 octobre à la question du §6, n° 1 de la passation, « non pas encore ». La citer.
19. **Les six recherches web de la fiche** ne sont ni listées ni datées. Donner les requêtes et les adresses vues, pour qu'on puisse les refaire avant le post.

---

## C. Les manques : travaux présents dans les rapports, ou vus en recherche, qui touchent l'angle

1. ***Mitigating Adaptive Attacks against Reasoning Models with Activation Consistency Training*** (Shah … Angell, arXiv 2605.28467).
   - Ce qu'il fait : l'effet d'un entraînement passe par une seule direction. L'ajouter à un modèle non défendu induit le refus ; la retirer du modèle entraîné rétablit la conformité. Aucun contrôle aléatoire n'est rapporté.
   - Statut : axe « test causal interne » du 1er octobre, lu par un site tiers (alphaXiv ; 1er oct., l. 296 à 301) ; rapport 3, résumé seul (nuit, l. 629).
   - Danger faible. C'est pourtant un précédent du « constat » : une conduite de sûreté installée par entraînement, et défaite par l'ablation d'une direction. Il figure dans les repères de l'agent 3 (consignes, l. 254).
2. ***Deliberative Alignment is Deep, but Uncertainty Remains*** (Pathmanathan, Huang, arXiv 2604.09665).
   - Comment l'ont lu les rapports :
     - l'axe « raisons contre actions » du 1er octobre le lisait par pith.science, comme un « C3 partiel : attribution latente » (1er oct., l. 49 à 53) ;
     - le verdict du même axe compte cette attribution latente parmi les recoupements partiels (1er oct., l. 110) ;
     - le rapport 7 l'a relu en texte intégral, sur la page abs et le HTML v2 (nuit, l. 1694 à 1712).
   - Ce que dit le rapport 7 : le papier ne compare pas un SFT avec raisonnement à un SFT sur réponses seules ; sa seule lecture interne choisit la réponse dont la représentation est la plus éloignée de la base ; importance faible.
   - À ajouter en danger faible, avec la correction du rapport 7, pour qu'on ne le cite pas comme un précédent. La partie 11, n° 3 du programme v1.1 le met déjà dans sa liste de relectures.
3. **Les travaux du rapport 5 sur le rang et les directions multiples** (danger faible, résumé seul, nuit, l. 1157 à 1160) :
   - *There Is More to Refusal in Large Language Models than a Single Direction* (Joad … Sencar, arXiv 2602.02132, EMNLP 2026) ;
   - *The Geometry of Refusal in Large Language Models: Concept Cones and Representational Independence* (Wollschläger … Gasteiger, arXiv 2502.17420) ;
   - *Predicting Where Steering Vectors Succeed* (Billa, arXiv 2604.15557).

   Ils touchent la question du rang : un refus à plusieurs dimensions est le cas où une ablation de bas rang échoue. Avec *Beyond Shallow Alignment* et Abu Shairah et al., ils appuient l'exigence du cas positif.
4. **Les voisins du lien entre le rang et la charge**, que la fiche déclare libre sans les nommer :
   - *Causal Calibration of Symbolic State in Embodied Language Agents* (Vaid, OpenReview U2mGb8jErX ; rapport 5, résumé seul ; moyen pour deux sous-questions de l'anatomie, nuit, l. 1084 à 1093). Il contrôle par des concepts sans rapport de même force, des directions aléatoires de même norme et une mauvaise couche. C'est aussi un modèle de contrôles pour cet angle.
   - *Gathered, Not Admitted* (Mazaheri, arXiv 2608.15022 ; rapport 5, texte intégral des §2.1 et §8). Faible, mais le rapport demande de le citer au centre comme mise en garde : la magnitude lue au lens ne mesure pas l'usage causal (nuit, l. 1106 à 1115).
   - Billa (voir C.3).
   - L'alerte de Zeisler (rapport 5, lu par un résumé de l'outil ; §5.5, n° 6, « à vérifier ») : sur modèles ouverts, les échanges de concepts ne font basculer la réponse que dans 6,3 à 11,1 % des cas (nuit, l. 1164). Elle rend fragile toute mesure de la charge sur Llama et Qwen.

   Le rapport 5 nomme ces voisins dans son verdict (nuit, l. 1212).
5. **Diffing de modèles et transplantation de persona** (rapport 5, résumé seul, danger faible, nuit, l. 1140 et 1144 à 1148) :
   - *Transcoder Adapters for Reasoning-Model Diffing* (Hu … Potts) : des traits nécessaires et suffisants ;
   - *Persona Features Control Emergent Misalignment* (Wang … Mossing) ;
   - *Fine-Tuning Enhances Existing Mechanisms* (Prakash … Bau) ;
   - Drake et Eberstadt : une direction de persona transplantée.

   Le rapport 5 les cite comme méthodes de comparaison entre modèles, dont aucune ne compare raisons et actions. Une ligne suffit.
6. **Un travail absent des onze rapports, vu ce matin par extrait** : *A Low-Rank Subspace Analysis of LLM Interventions* (Sharma … Yu, arXiv 2606.14388 ; atelier d'interprétabilité mécaniste d'ICML 2026 d'après l'extrait ; vu par extrait de recherche, non ouvert).
   - Il modélise des conduites comme des sous-espaces de bas rang.
   - Intervenir sur l'une en déplace d'autres, selon le recouvrement de leurs sous-espaces.
   - Danger faible. Il touche le choix des contrastes sans rapport et la géométrie du principe.
7. **Une conséquence pour le programme.** Le §5.5, n° 7 propose un bras « réflexion contrefactuelle » d'après le §7. S'il est retenu, localiser le principe dans ce bras refait sur un modèle ouvert l'ablation du §7. Le danger du §7 monte alors pour ce bras. La fiche doit le dire, puisque ses conséquences seront rapportées à la v1.3.

---

## D. Vérifié, sans correction

- **La date et le titre de Nakamura, et ce qu'il fait** : la date et le titre viennent du §4.2, n° 8 ; ce qu'il fait vient du rapport 3, texte intégral (nuit, l. 566 à 576). La citation « quasiment la méthode du programme » est exacte.
- **Les chiffres du §7** et la citation du §9.2 sont conformes au §4.2, n° 2.
- **Ce qui sépare le §7 du programme** est conforme au §4.2 et au rapport 3.
- ***Beyond Shallow Alignment*** : ce qu'il fait, le niveau moyen, et les écarts sur Llama et sur EMNLP signalés en contradiction, conformes aux rapports 3 et 5 et à l'axe du 1er octobre.
- ***Routing Subspaces*** : ce qu'il fait et ses contrôles, conformes au rapport 3 ; la dégradation non appariée, conforme à l'axe « combinaison exacte ».
- **Abu Shairah et al.** (« résumé seul », d'après l'URL de la page abs), **Ponkshe et al.** (lu par un site tiers ; la page des actes d'ICLR 2026 apparaît bien en recherche) et **Nadaf** sont conformes.
- **Li et al.** (rapport 6, adjacent), **Zhou**, **Pando** et ***The Model Organism Lottery*** sont conformes.
- ***Emergent Unfaithfulness*** : bien absent des onze rapports. L'extrait confirme l'identifiant, COLM 2026, Zahraei … Hakkani-Tür (UIUC), et l'amplification au DPO.
- **La partie 1 du programme v1.1** : son verdict cite « C1 + C3 avec contrôles », et Gurnee et Nakamura manquent à son tableau. Ponkshe y est cité, et *Constitutional adapters* est bien dans la partie 11, n° 3.
- **Le complément de l'architecte** : la v1.3 n'intègre pas Nakamura et garde les formulations de la v1.1. C'est conforme.
- **Le rapport 6** dit l'angle libre en ne voyant que Li et al. et le Concept Ablation Fine-Tuning (nuit, l. 1535). L'arbitrage de la fiche, « partiellement pris » d'après le §4.4, n° 4, est juste.
- **Les dates de SPAR et d'ICLR 2027**, et le statut « non relu » de ces dernières, sont conformes au §4.4.
- **Les règles d'écriture** : aucune idée n'est désignée par un sigle, et « premiers » n'apparaît que pour nommer des formulations intenables, comme au §5.5, n° 9.
