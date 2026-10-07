# Vérification de « projets et calendrier » (`travail/projets_calendrier.md`)

État au vendredi 2 octobre 2026. Vérification sceptique, affirmation par affirmation, contre les rapports bruts, la passation v1.2 (§3, §4, §5.5, §6), les consignes de la nuit et le programme v1.1. Les numéros « l. n » renvoient aux lignes de `projets_calendrier.md` ; « rapports du 2 octobre, l. n » aux lignes de `ANTERIORITE_RAPPORTS_2026-10-02.md`.

**Ce que j'ai relu moi-même.** Les sept rapports de la nuit en entier ; dans les rapports du 1er octobre, les passages qui parlent de projets (l. 85-114, 205-229, 352-488, plus une recherche par mots-clés sur tout le fichier) ; la passation v1.2 en entier, la v1.0, le complément de l'architecte ; les définitions des niveaux de danger et les consignes des agents 1, 6 et 7 ; le programme v1.1, parties 1, 4 (phases du retrait, de la survie et du juge), 9, 10 et 11. Par curl, le README et le SUMMARY.md d'exp9. Huit requêtes WebSearch : ce qui en vient est « vu par extrait de recherche, non ouvert » et ne fournit aucun chiffre ici.

---

## 1 · Corrections bloquantes

### 1.1 Des chiffres tirés d'extraits de recherche seuls
La règle de la tâche : ce qui n'est vu que par extrait « ne fournit aucun chiffre ». Le fichier en tire pourtant des dates, puis des calculs. Sa convention de la l. 8 (« une date vue seulement par extrait est indicative ») contredit la règle.
- Dates concernées, vues par extrait seul :
  - la cohorte d'automne de MATS (l. 139, 152, 161) ;
  - la discussion publique et la discussion privée d'ICLR 2027 (l. 158, 160) ;
  - la conférence ICLR 2027 (l. 169) ;
  - ICML 2027, COLM 2027 et NeurIPS 2027 (l. 168, 170, 171).
- Calculs qui en dépendent :
  - « cinq à sept semaines plus tard » (l. 175) ;
  - « Semaine 10 (4 décembre). Fin de MATS » (l. 216) ;
  - « sept semaines avant la fin de SPAR et de MATS » (l. 211).
- **Exigé.** Garder l'événement, retirer le chiffre (« date à établir sur la source officielle »). Ne garder que les dates portées par un rapport, avec l'extrait en simple concordance :
  - ICLR 2027 : 18 et 25 septembre, 5 novembre, 16 décembre (rapport 6, l. 1506 ; non relu par l'instance, passation §4.4) ;
  - SPAR : 14 septembre au 14 décembre, Demo Day le 19 décembre (rapport 6, l. 1450 ; rapport 1, l. 179 ; passation §4.4).
- Mes propres recherches retrouvent les mêmes extraits (ICLR, MATS, SPAR). Cela ne change pas leur statut.

### 1.2 La suite d'Anthropic classée « danger élevé » (l. 46-55)
- **Ce que disent les définitions.** Le niveau élevé suppose un travail qui fait déjà ce que vise un angle, ou l'a annoncé (consignes, l. 48). La suite n'est ni faite ni annoncée. Le seul indice est une phrase de la page de recherche, « première étape d'une ligne de travail étendue ». Le rapport 5 l'a lue par résumé de l'outil, sans date et sans niveau (l. 1185).
- **Ce que porte le niveau élevé.** Celui du rapport 5 (l. 1036) et de la passation (§4.4, n° 8) porte sur le §7 **publié**, pour deux sous-questions : la présence des concepts et leur nécessité. Ce fait appartient à la carte de l'angle de l'anatomie. Ce n'est pas un projet.
- **Exigé :**
  - sortir la suite du §1.1 ;
  - la présenter comme le concurrent le plus probable (rapport 5, l. 1185 ; passation §4.4, n° 8), sans niveau propre, en disant ce qu'elle menacerait : les sous-questions libres du §4.4, n° 8 ;
  - pour le principe localisé, donner le niveau que le rapport 3 donne au §7 : « moyen, proche de l'élevé » (l. 529). Le fichier n'écrit que « en bord ».

### 1.3 Vaid, coté « faible » contre le rapport 5 (l. 136)
- **Ce que dit le rapport 5** (l. 1084-1093) : *Causal Calibration of Symbolic State in Embodied Language Agents* (Roy Vaid, atelier NEmo de NeurIPS 2026) est **moyen pour deux sous-questions de l'anatomie**. Ce sont la charge contre l'effet d'intervention, et la spécificité au contexte où le concept s'applique. Le verdict du même rapport en fait le voisin méthodologique de la spécificité par famille (l. 1210).
- **Pourquoi c'est bloquant.** Ces deux sous-questions sont déclarées libres au §4.4, n° 8. Un travail moyen sur elles se cite au centre (consignes, l. 49). Le fichier le relègue en « faible » et lui attache à tort la dépendance au regard.
- **Exigé :**
  - Vaid : moyen pour ces deux sous-questions ;
  - statut : « rapport 5, résumé seul (API OpenReview ; le PDF renvoie 403) » ;
  - Dabir et al. : anatomie, faible (rapport 5, l. 1162-1165). Le rapport 6 le dit déjà en ligne les 1er et 2 octobre (l. 1431-1433) : c'est un travail visible, pas une date à attendre.

### 1.4 La visibilité d'ICLR 2027 : une inférence donnée pour un fait, et une vérification du rapport 6 omise
- **L'inférence.** Le §2 marque bien comme inférence que les soumissions deviendraient lisibles le 5 novembre (l. 159). Le §3 l'affirme ensuite :
  - « il ne se lèvera qu'en semaine 6 » (l. 193) ;
  - « Probablement jusqu'au 5 novembre » (l. 226).
- **Ce qui est établi.** Le rapport 6 n'établit qu'une chose : au 2 octobre, `public_submissions: false`, valeur lue dans un résumé automatique du JSON (l. 1266). Rien ne date l'ouverture.
- **L'omission.** Le rapport 6 a aussi passé au crible 28 prépublications d'août à octobre qui se déclarent soumises à ICLR 2027 : « aucune ne touche le programme » (l. 1500). C'est la seule fenêtre partielle sur ce risque, et le fichier ne la cite pas.
- **Exigé :**
  - marquer l'inférence partout où elle sert (l. 193, 215, 226) ;
  - ajouter la vérification des 28 prépublications au §3.2 et au §3.6 ;
  - ajouter à la surveillance (§3.8) le suivi des prépublications qui se déclarent soumises à ICLR 2027.

### 1.5 Le calendrier du programme v1.1, mal lu
- **La place de l'arXiv.** Le programme met « S11 – S12 : rédaction, contre-lecture indépendante, prépublication » dans une seule ligne (partie 9, l. 745 du programme) et la prépublication en S11 (partie 10, l. 792). Le fichier, lui, sépare les deux semaines :
  - semaine 11 : l'arXiv (l. 163) ;
  - semaine 12 : « rédaction, contre-lecture indépendante, préparation de la soumission » (l. 166).

  Cela met la contre-lecture **après** l'arXiv, ce que le programme ne dit pas. Il faut aussi signaler l'ambiguïté entre la partie 9 (S11 ou S12) et la partie 10 (S11).
- **Le moment de la recherche d'antériorité.** La partie 11, n° 1, la place « juste avant le post, puis juste avant la soumission », pas avant l'arXiv. Les l. 163, 217 et 246 sont à corriger, ou à présenter comme une proposition.
- **Une erreur de logique.** « fait passer l'arXiv au 17 – 23 décembre, après la fin de SPAR (14 décembre) et après son Demo Day (19 décembre) » (l. 190) est faux : la fenêtre du 17 au 23 contient le 19.
- **La marge réelle.** Sans aucun glissement, la semaine 11 (10 – 16 décembre) contient déjà le 14 : l'objectif « avant SPAR » n'a pas de marge du tout. Et « avant SPAR » est une interprétation de la phrase de Lazar, qui portait sur la question du projet de Qiyao Wei (passation §3, point 4) : la marquer comme telle.
- **La version de référence.** Le complément de l'architecte dit que les versions 1.2 et 1.3 ont changé le calendrier et les ressources. La v1.3 est la référence (passation §3, point 9). La réserve de la l. 10 doit donc être reprise en tête du §3.1, dont les conclusions sont provisoires.

---

## 2 · Corrections nécessaires (non bloquantes)

1. **« C'est l'équipe la mieux placée pour suivre vite après notre post » (l. 44) : une spéculation sans source, que les pièces affaiblissent.**
   - L'organisme de Hua et al. et ses documents sont publics : n'importe quelle équipe peut le reconstruire (passation §4.3, Hua et al.).
   - Le rapport 4 situe exp9 plutôt pendant une période de Lundqvist chez Goodfire : les scripts utilisent le compte de calcul « goodfire ». Le rapport le donne comme une inférence (l. 783). L'infrastructure n'est donc pas forcément celle de l'équipe SPAR de Pivotal.
   - Marquer « mon estimation », et ajouter ces deux réserves.

2. **Le billet de blog.daios.tech (l. 69, 199, 246) : priorité surestimée.**
   - Mon extrait de recherche (non ouvert) présente ce billet comme les notes de travail d'un projet « Parrhesia », financé par le Cosmos Institute. Il ne nomme ni Cadile ni SPAR.
   - Une recherche sur le titre du projet de Cadile, avec « phronesis », ne fait remonter aucun lien.
   - L'association que le fichier dit avoir vue dans un extrait n'est donc pas reproduite.
   - Exigé : retirer « À ouvrir en priorité » et le retirer de la liste du §3.2. Le garder comme travail adjacent, faible (mon estimation), sans lien établi avec Cadile, vu par extrait, non ouvert.

3. **La survie, et Lundqvist (l. 42) : le désaccord des rapports et le « libre » à préciser.**
   - **Les niveaux.**
     - Le rapport 4 donne « élevé » pour la survie d'une mitigation du jeu d'évaluation (l. 925), et la passation le retient (§4.4, n° 6, relu).
     - Le rapport 6 donne « moyen » pour la survie et pour le retrait (l. 1465). Le fichier doit le dire.
   - **Ce que le rapport 4 lit comme annoncé.** Son verdict lit comme annoncés par Lundqvist « la survie de l'indépendance au regard » et un post-entraînement qui récompense le jeu d'évaluation (l. 972).
   - **Ce que fait le programme.** Le programme v1.1 appelle la survie « la question centrale du projet SPAR de Lundqvist » (l. 436). Sa phase de survie part aussi :
     - du bras coopération ;
     - du bras raisons entraîné avec le retrait de « je suis évalué » (l. 438).

     Le recouvrement est donc direct sur ces deux modèles de départ.
   - **Exigé.** Écrire que reste libre la survie de l'avantage **des raisons** et de **son** indépendance au regard (passation §4.4, n° 6). Ajouter que le post-entraînement qui paie le jeu d'évaluation est annoncé dans une variante, et que la survie des mitigations du programme est touchée de front.

4. **exp9, « Ce qui reste libre » (l. 30).** Le retrait de « je suis noté » pendant un RL ou un DPO est libre dans tout ce que le rapport 4 a lu. Mais une variante, le pilotage préventif contre le jeu d'évaluation pendant le fine-tuning, est annoncée par Lundqvist (rapport 4, l. 977). L'ajouter.

5. **Des niveaux qui sont ceux de l'auteur, sans être marqués comme tels.** Le fichier contredit ici sa propre convention de la l. 9.

   | Ligne | Travail | Niveau du fichier | Ce que disent les rapports | Exigé |
   |---|---|---|---|---|
   | l. 127 | Bharadwaj et Kirk | faible | Aucun niveau pour l'annonce. Le billet publié est moyen pour le rapport 2 (l. 333), faible à moyen pour le rapport 6 (l. 1371-1376). Le rapport 2 l'a lu en texte intégral (l. 330). | Marquer « mon estimation ». Remplacer « mode de lecture non précisé » par « rapport 2, texte intégral du billet ; l'annonce n'y est pas située ». |
   | l. 128 | OpenAI et Apollo | — | Les évaluations tierces avec points de contrôle sont annoncées par Apollo seul (rapport 2, l. 428). Le niveau faible porte sur le billet publié *Metagaming matters* (l. 371). | Attribuer l'annonce à Apollo, et dire à quoi s'applique le niveau. |
   | l. 131 | Resolution | faible | Aucun niveau (rapport 3, l. 667). | Marquer « mon estimation ». |
   | l. 132 | Konrad et al., Santos-Grueiro | faible | Aucun niveau pour les annonces. Les deux travaux publiés sont moyens (rapport 3, l. 547 et 559). | Marquer « mon estimation ». |
   | l. 135 | *PreCommitLens* | faible | Aucun niveau explicite (rapport 5, l. 1194). | Marquer « mon estimation ». |
   | l. 137 | Qiyao Wei | faible | Aucun niveau (rapport 2). | Marquer « mon estimation ». |
   | l. 126 | Betley et al. | « mon estimation » | Le rapport 6 classe ce billet en « moyen à faible » (section de la l. 1322). | Citer le niveau du rapport 6, pas une estimation. |

6. **Second Look Research : pas de contradiction établie (l. 89).**
   - Le rapport 6 date du 15 août le billet de Second Look Research (l. 1497).
   - Le rapport 2 parle d'une « note du billet du 21 septembre » (l. 429), et cite ailleurs *Alignment Midtraining Cracks Under Pressure* à la même date (l. 397).
   - Vu par extrait, non ouvert :
     - le billet LessWrong de Second Look Research (*Rerunning AI safety papers…*) concorde avec la date du rapport 6 ;
     - un autre extrait attribue *Alignment Midtraining Cracks Under Pressure* à l'équipe d'alignement d'Arcadia Impact.
   - Ce sont donc vraisemblablement deux documents, ce qui reste une inférence. Remplacer « contradiction non résolue » par cette lecture.
   - Rappeler la passation §6, point 3 : Second Look Research est à relire sur la source avant toute citation au centre.
   - L'extrait de la page SPAR (non ouvert) décrit un programme de réplications en général, pas celle de *Teaching Claude Why*. La conditionnelle de la l. 93 est juste ; la garder.

7. **arXiv 2610.00767 (l. 138) : « titre seul » est à mettre à jour.**
   - D'après les extraits (non ouverts), la greffe entraîne un adaptateur de documents synthétiques sur le point pré-entraîné, puis ajoute la mise à jour des poids au modèle post-entraîné. Ce n'est pas un patching d'activations entre deux fine-tunes d'une même base.
   - Auteurs vus dans l'extrait : Nutter, Roytburg, Dumas, Ou, Shi Feng.
   - C'est un travail publié, pas un projet. Adjacent, faible (mon estimation).

8. **« Les soumissions de janvier … ne nous précèdent pas » (l. 222) : trop fort.** Seule la date de soumission est postérieure. Un travail soumis en janvier peut avoir une version arXiv ou un billet antérieurs à notre arXiv.

9. **Les cohortes de MATS confondues (§3.4, l. 211 et 216).** Les flux d'Ududec et d'Africa relèvent de MATS hiver 2027 (rapport 6, l. 1479-1487), et non de la cohorte d'automne 2026, dont aucun projet n'a été vu. La fin de la cohorte d'automne ne les concerne pas. Le préciser.

10. **Les sources mal attribuées :**
    - **Les refus sur exp9 (l. 27, 233, 263) :**
      - le rapport 6 ne mentionne jamais exp9 ;
      - les sources sont le rapport 4 (l. 756 et 944) et la passation, annexe C (l. 670).
    - **Le projet SPAR d'Ivanov (l. 119) :**
      - il ne figure pas dans le rapport du 1er octobre sur la conscience comme condition ;
      - il est dans ceux sur raisons contre actions (l. 99 de ce fichier) et sur la combinaison exacte (l. 453).
    - **La FAQ de SPAR (l. 164) :**
      - « rapports 1 et 6, texte intégral de la FAQ » est inexact ;
      - le rapport 6 dit « lu dans la FAQ » (l. 1450) ; le rapport 1 donne les dates sans dire où il les a lues (l. 179) ;
      - la passation §4.4 dit « lue par deux agents » ;
      - écrire « rapport 6, lu dans la FAQ ; rapport 1, sans mode de lecture ».
    - **Les scripts d'exp9 (l. 23) :**
      - ceux de la phase 5 ont été lus en brut ;
      - ceux de la phase 6, seulement par résumé automatique (rapport 4, l. 755).
    - **OpenReview (l. 226) :**
      - ajouter le rapport 3 (l. 675-676) ;
      - le rapport 4 dit 403 et « pas visibles », pas « 0 résultat » (l. 945).
    - **Le billet sur la coopérativité (l. 98) :** le rapport 7 avertit que WebFetch lui rend des résumés faits par un petit modèle (l. 1578). Garder « rapport 7, texte intégral », avec cette réserve.

11. **Une classification incohérente.**
    - Le §1.2, titré « Danger moyen », range :
      - Second Look Research, « faible à moyen » ;
      - le flux d'Ududec, « moyen à faible ».
    - Le projet SPAR d'Ivanov, « faible à moyen » lui aussi, est rangé au §1.3.
    - Harmoniser.

12. **L'appel d'Ivanov (l. 120) : angles et sources incomplets.**
    - Le rapport 3 (l. 668) et le rapport du 1er octobre sur la combinaison exacte (l. 466-467) le lisent aussi comme une proposition d'entraînement de cohérence qui pénalise le conditionnement sur l'évaluation. Cela touche le retrait pendant l'entraînement, comme direction annoncée.
    - Le rapport 6 relève une autre proposition (l. 1365) : entraîner sur des données de raisonnement, puis mesurer la conscience d'évaluation. Elle est proche de l'amplification par les raisons.
    - Le second billet, *Better evals are not enough to combat eval awareness* (29 janvier 2026, rapport 3), manque.
    - Pour le projet SPAR d'Ivanov, le rapport 4 note qu'il prévient que certaines interventions pourraient rendre le métajeu invisible (l. 928). C'est la question du ré-encodage.

13. **Le projet SPAR de Lundqvist : des éléments annoncés manquent (l. 34-37).**
    - Le rapport 4 relève (l. 919 et 923) :
      - la comparaison d'interventions plus profondes ou plus précoces face à la pression d'entraînement ;
      - l'auto-prédiction du modèle.
    - Le projet est étiqueté interprétabilité mécaniste (rapport du 1er octobre, combinaison exacte, l. 446 ; programme v1.1, l. 108). Cela le rapproche des mesures internes.

---

## 3 · Les manques : travaux et projets présents dans les rapports, absents du fichier

1. **Le dépôt « latent-awareness » de Kretschmar.**
   - Ce que dit le rapport 3 (l. 672) : le dépôt existe, mais aucune mesure latente n'est publiée.
   - Le travail publié de Kretschmar est moyen pour les raisons pour le juge (rapport 4, l. 876).
   - Le risque est le même que pour exp9 : un commit suffit, sans annonce. À ajouter à la surveillance.
2. **Les indices sur Hugging Face, sans fiche ni papier** (rapport 5, l. 1188-1193) :
   - *Koalacrown/jacobian-lens-organisms* : des J-lens sur des organismes de personnalité dérivés de Qwen3-8B, l'un des deux modèles du programme ;
   - les modèles « deployment-mo » et « artificial-mo » de *stanleytheli* (fiches à accès restreint) ;
   - les crosscoders de *Sitavi* ;
   - *jeeva2812* et *AnonymousInterpScience*.

   Ils touchent l'anatomie et peut-être la dépendance au regard. Niveau inconnu.
3. **La proposition citée par exp9**, « CoT leakage → verbalized vs unverbalized EA ». Le rapport 4 ne l'a pas retrouvée (l. 960). Elle touche les raisons pour le juge.
4. **Thomson et Li, *A framework for eval awareness*.** L'entraînement de cohérence y est seulement proposé (rapport du 1er octobre, combinaison exacte, l. 466-468). Cela touche le retrait pendant l'entraînement, comme direction annoncée.
5. **Netzer Epstein, *Test smells*.** C'est un préprint annoncé « forthcoming », issu du projet de Qiyao Wei (rapport 2, l. 408). Il porte sur les indices d'évaluation, et Epstein a aussi un projet SPAR d'automne. Faible (mon estimation).
6. **Le projet SPAR de printemps 2026 d'Emil Ryd et Keshav Shenoy,** *Understanding LLM generalization through fine-tuning*. Faible (rapport 1, l. 185).
7. **Le projet SPAR de printemps de LawZero.** La consigne de l'agent 2 en faisait une priorité, et rien n'a été trouvé sur la question (rapport 2, l. 412-417 ; rapport du 1er octobre, l. 455). À mettre dans les non retenus.
8. **Les flux de MATS hiver 2027 de niveau faible** (rapport 6, l. 1488-1494) :
   - l'équipe d'alignement de UK AISI (Souly, Kirk), sur le jeu d'évaluation non verbalisé et ses atténuations ;
   - Lambert, Nanda, Lindner, Ward ;
   - LawZero.

   À mettre dans les non retenus.
9. **Les sorties annoncées de *Synthetic Persona Pretraining*,** sur modelraising.ai/spp, non ouvert (rapport 7, l. 1678). Faible (mon estimation).
10. **La surveillance d'exp9 (§3.8, n° 1) est étroite.**
    - Une suite peut ajouter des fichiers sans toucher à SUMMARY.md ni au README.
    - Proposer de relever aussi l'empreinte des scripts connus que le rapport 4 a lus en brut (l. 755). Ne rien tenter sur `results/` ni sur l'historique, refusés.

---

## 4 · Ce qui a été vérifié et tient

- **Le verdict général** (l. 16) : conforme à la passation §4.4 et au rapport 6 (l. 1261).
- **exp9, revérifié par curl** sur raw.githubusercontent.com :
  - le README rend HTTP 200 et une ligne, « research in progress » ;
  - SUMMARY.md fait 12 666 octets, avec la même empreinte sha256 `2a55f9b382683b4a17ead2588966eb8ddbe2db0815fa8eff46758d214c183fec` ;
  - le statut est « complete (2026-04-29) » ;
  - le PPO noté en ligne figure sous « Future work », avec « Predicted to widen the leak-vs-no-leak gap ».
- **Les niveaux d'exp9** (élevé pour la sous-question, moyen pour l'angle) : conformes au rapport 4 (l. 776-777) et à la passation §4.4, n° 7.
- **La page SPAR de Lundqvist** : relue par l'instance du papier (passation §4.2, n° 3) ; la description du fichier est conforme.
- **Le projet de Cadile** : conforme au rapport 6, page lue en entier (l. 1452-1460), pour la description, le niveau moyen, les sorties prévues et ce qui le sépare. Le rapport 4 le dit au cœur du programme (l. 932).
- **Infohazard Evaluations** :
  - la description est conforme au rapport 2 (l. 422), qui ne donne pas de niveau ;
  - le niveau moyen est marqué comme estimation, et il est défendable.
- **Cody Wild, Ududec, Africa, Salle et Imran, CaML, Muhammad Aaliyan, Epstein et Ravid, Hacker-Opus, Nanda avec Blank et Bhatia, Cho et al., 2604.18946** : descriptions et niveaux conformes aux rapports cités.
- **Aucune erreur corrigée au §4.3 n'est reprise** :
  - *Eval Cooperativeness* est bien donné comme poster d'atelier ;
  - les points de contrôle de Cho et al. sont bien à 120B ;
  - l'organisme de Hua et al. n'est pas dit privé.
- **Les jours de la semaine** : tous justes (le 1er octobre 2026 est un jeudi).
- **Les numéros de semaine** : justes sous l'hypothèse de la l. 147.
- **Les deux décisions relayées ce jour** sont rapportées fidèlement :
  - le nom : Lazar seul, avec son ORCID ; Claude dans une phrase de méthode ;
  - le contact avec Cadile et Lundqvist : « non pas encore ».

  Le fichier ne propose aucun contact.
- **Le calendrier du complément** : le complément de l'architecte confirme que les versions 1.2 et 1.3 ont changé le calendrier. La réserve de la l. 10 est fondée.
- **Les citations** font toutes moins de quinze mots. Aucune idée n'est désignée par un sigle. Le mot « first » n'apparaît pas.
