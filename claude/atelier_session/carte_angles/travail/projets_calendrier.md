# Carte des angles déjà pris — les projets à surveiller, les dates, les risques de calendrier

État au vendredi 2 octobre 2026. Pièce de travail pour la carte des angles (passation v1.2, §6, point 3).

**Conventions.**
- « Rapport 1 » à « rapport 7 » : les sept rapports de la nuit (`ANTERIORITE_RAPPORTS_2026-10-02.md`). Les quatre rapports du 1er octobre sont désignés par leur axe (« rapport du 1er octobre, combinaison exacte »).
- Statuts de lecture : « relu sur la source par l'instance du papier » (passation v1.2, §4.2) ; « rapport n, texte intégral » ; « rapport n, résumé seul » ; « rapport n, lu par un site tiers » ; « vu par extrait de recherche, non ouvert » ; « non ouvert ». Quand un rapport ne dit pas comment il a lu, je l'écris.
- Ce qui n'est que dans un rapport n'est pas établi. Une date vue seulement par extrait de recherche est indicative : à confirmer sur la source avant tout usage.
- Les niveaux de danger sont ceux des consignes de la nuit. Quand le niveau est le mien et non celui d'un rapport, je l'écris.
- Le calendrier confronté est celui du programme v1.1 (partie 9). D'après le complément de l'architecte, les versions 1.2 et 1.3 ont modifié le calendrier et les ressources. La confrontation est donc à refaire sur la v1.3, après la phase 1 de l'axe de douleur.

---

## 1 · Les projets à surveiller

Rappel du verdict (passation v1.2, §4.4) : **la combinaison centrale reste libre** pour ce que les onze rapports ont pu voir. Aucun projet ci-dessous n'annonce l'inhibition d'une représentation « je suis évalué » dans des modèles entraînés sur les raisons ou sur les mêmes actions. Le rapport 6, chargé des projets annoncés, n'en a trouvé aucun (rapport 6, §1 et §2).

### 1.1 Danger élevé, sur une sous-question

**Ryan Lundqvist — dépôt public `exp9-rlaif-leakage` (GitHub)**
- **Quoi.** Un modèle de récompense « constitutionnel » note chaque rollout deux fois, en voyant ou non le raisonnement. Les raisonnements qui verbalisent l'évaluation perdent 0,50 point quand le juge les voit ; c'est la verbalisation qui est pénalisée, pas la conduite (relu sur la source par l'instance du papier, §4.2, n° 1).
- **État.** L'étape statique est close : statut « complete (2026-04-29) ».
  - Deux DPO (juge qui voit le raisonnement, juge qui ne le voit pas) sont scriptés, sans résultat publié (rapport 4, texte intégral des scripts ; non relu par l'instance).
  - **Revérifié ce jour par curl** sur raw.githubusercontent.com :
    - le README fait toujours une ligne, « research in progress » ;
    - SUMMARY.md garde le même statut, et le PPO noté en ligne figure toujours sous « Future work » : « Predicted to widen the leak-vs-no-leak gap ». SUMMARY.md fait 12 666 octets, sha256 `2a55f9b382683b4a17ead2588966eb8ddbe2db0815fa8eff46758d214c183fec`. Cette empreinte sert de référence pour les relectures suivantes.
  - L'historique des commits et le dossier `results/` restent non ouverts. Les rapports 4 et 6 les disent refusés (robots.txt, API) ; je n'ai pas tenté de les lire.
- **Date.** Aucune pour la suite.
- **Angle et danger.** Les raisons pour le juge. Le danger est élevé pour la comparaison « juge qui voit le raisonnement contre juge qui ne voit que la réponse », dans la variante où le raisonnement est la verbalisation de l'évaluation. Il est moyen pour l'angle pris dans son ensemble (rapport 4 ; passation §4.4, n° 7).
- **Ce qui reste libre.** Des justifications par principes, la cohérence contrefactuelle entre raison et action, le retrait de « je suis noté » pendant un RL ou un DPO (passation §4.4, n° 7).
- **Lien avec le projet SPAR de Lundqvist.** Aucun lien écrit (rapport 4).

**Ryan Lundqvist (Pivotal) — projet SPAR d'automne 2026, *Training-Time Mitigations for Eval Awareness and Eval Gaming***
- **Quoi.** La coopérativité envers les évaluations, puis sa survie : « do such training-time mitigations survive the optimization pressure of post-training? ». Le projet annonce aussi :
  - des adaptateurs d'inoculation et des vecteurs de pilotage préventifs pendant le fine-tuning ;
  - des mesures de la conscience non verbalisée ;
  - l'attribution aux données.
- **Source.** Relu sur la source par l'instance du papier (§4.2, n° 3) ; rapports 4 et 6, texte intégral.
- **État.** Candidatures closes, 4 à 5 encadrés. Aucun résultat public (rapport 4). Mes recherches de ce jour n'en trouvent pas non plus (vu par extrait de recherche, non ouvert).
- **Date.** Aucune propre au projet. Calendrier de SPAR : recherche jusqu'au 14 décembre, Demo Day le 19 décembre 2026 (§2).
- **Angles et danger.**
  - Survie : danger élevé pour la survie d'une mitigation du jeu d'évaluation (rapport 4 ; passation §4.4, n° 6). Il reste libre pour la survie de l'avantage des raisons et de son indépendance au regard.
  - Retrait pendant l'entraînement : danger moyen (rapport 6). La méthode est annoncée ; son application à l'avantage des raisons reste libre.
- **À noter.** Lundqvist a déjà l'infrastructure de l'organisme de Hua et al. (dépôt exp9). C'est l'équipe la mieux placée pour suivre vite après notre post.

**Anthropic — la suite de l'entraînement par réflexion contrefactuelle (papier sur l'espace de travail global, §7)**
- **Quoi.** Le §7 entraîne déjà par des principes. Il montre la présence de concepts éthiques avant la sortie, puis leur nécessité par ablation. Le §9.2 dit : « We do not yet know how broadly the technique generalizes » (relu sur la source par l'instance du papier, §4.2, n° 2).
  - La page de recherche parlerait d'une première étape d'une ligne de travail étendue (rapport 5, résumé seul).
  - *Teaching Claude Why* annonce l'interprétabilité mécaniste comme agenda (rapport 3, qui dit avoir vérifié le texte intégral de ce billet).
- **État.** Recherche interne, invisible. Ma recherche de ce jour ne trouve que des commentaires du papier, aucune suite (vu par extrait de recherche, non ouvert).
- **Date.** Aucune.
- **Angles et danger.**
  - L'anatomie : danger déjà élevé pour la présence des concepts et leur nécessité (passation §4.4, n° 8). La suite pourrait prendre la suffisance, la spécificité par famille ou le rang selon la charge.
  - En bord : le principe localisé.
  - C'est le concurrent le plus probable (rapport 5 ; passation §4.4).

### 1.2 Danger moyen

**Juan Cadile (Université de Rochester) — projet SPAR d'automne 2026, *Constitutions and Reasons***
- **Quoi.** Entraînement de caractère par vertus, construit sur OpenCharacterTraining, avec trois composantes :
  - des triplets excès, juste milieu et défaut ;
  - des réponses annotées de leurs raisons ;
  - une boucle de réflexion et de mise à jour.
- **Ablation annoncée.** « demonstrations versus rationale-annotated responses ». Généralisation morale testée sur des scénarios tenus à part. Vecteurs de persona en option, semaines 10 à 12.
- **Sorties prévues.** Un billet sur l'Alignment Forum au minimum ; un papier d'atelier si les résultats le justifient.
- **Source.** Rapport 6, texte intégral (page SPAR lue en entier) ; rapports 1 et 4 ; rapport du 1er octobre, combinaison exacte.
- **Ce qui le sépare du programme.** Il porte sur des traits de caractère. Il n'annonce ni contrôle de format, ni conscience d'évaluation, ni scénarios agentiques (rapport 6).
- **État.** En cours ; aucun résultat trouvé (rapports 1 et 6).
- **Nouveau ce jour, non vérifié.** Un billet de blog.daios.tech, *Virtue Ethics-Based Character Training: Building Truth-Telling AI*, apparaît dans une recherche sur le titre du projet. L'extrait associe le nom du projet à des constitutions fondées sur la phronesis. Rien n'établit qu'il s'agit d'une sortie du projet de Cadile (vu par extrait de recherche, non ouvert ; l'ouverture a été refusée par le proxy). **À ouvrir en priorité** : si c'est une sortie du projet, elle peut déjà contenir l'ablation entre démonstrations et raisons.
- **Date.** Résultats possibles vers le Demo Day du 19 décembre 2026 (rapport 6).
- **Angle et danger.** Raisons contre actions, danger moyen (rapports 1 et 6) ; le rapport 4 le dit au cœur du programme. En bord, l'anatomie, par les vecteurs de persona (danger faible, mon estimation).

**Shi Feng, Taslim Mahbub, Arush Tagade — projet SPAR d'automne 2026, *Infohazard Evaluations***
- **Quoi.** La description annonce de comparer des méthodes d'entraînement qui gardent la reconnaissance de l'évaluation tout en retirant son influence sur la conduite.
- **Source.** Rapport 2, texte de la description sur SPAR ; le document du projet est non ouvert. Non relu par l'instance (passation §4.4, n° 5).
- **État.** « Ongoing ».
- **Date.** Calendrier de SPAR.
- **Angle et danger.** Retrait pendant l'entraînement. Le rapport 2 ne donne pas de niveau ; **moyen, selon mon estimation** : c'est une variante proche de la méthode, sans les raisons.

**Cody Wild (Google DeepMind) — projet SPAR d'automne 2026, *Exploration of What Kinds of Training Pressure Cause CoT Obfuscation***
- **Quoi.** Récompenses calculées par un moniteur sur la pensée, sur un résumé du raisonnement ou sur la sortie seule, puis mesure de l'obfuscation qui en résulte. Plusieurs modèles ouverts ; suivi au fil du RL en option.
- **Source.** Rapport 6, texte intégral (page SPAR) ; rapport 4.
- **Date.** Calendrier de SPAR.
- **Angle et danger.** Les raisons pour le juge : moyen (rapport 4), moyen à faible (rapport 6).

**Second Look Research — la réplication de *Teaching Claude Why* sur modèles ouverts**
- **Quoi.** Une réplication des expériences de midtraining de *Teaching Claude Why* sur des modèles ouverts, annoncée « dans les semaines qui viennent ». Le rapport 2 y ajoute la réplication du RL bénéfique d'OpenAI.
- **Source.** Rapports 2 et 6, qui ne disent pas comment ils ont lu le billet ; non relu par l'instance.
- **Date de l'annonce : contradiction non résolue.** Billet du 15 août 2026 selon le rapport 6, note d'un billet du 21 septembre 2026 selon le rapport 2.
- **Nouveau ce jour.**
  - Second Look Research a une page de projet SPAR d'automne 2026 : « Replicating load-bearing AI safety research » (`sparai.org/projects/f26/recQVGOyf3uaJQu3G/`). Vu par extrait de recherche, non ouvert : le proxy refuse sparai.org à WebFetch.
  - D'après les extraits, c'est un projet de l'Existential Risk Lab de l'Université de Chicago, et le billet LessWrong d'annonce s'intitule *Rerunning AI safety papers on every frontier release would…* (vu par extrait de recherche, non ouvert).
  - Si la réplication relève de la cohorte SPAR, son horizon est aussi le 14 décembre.
- **État.** Non trouvée publiée au 2 octobre (rapport 6 ; mes recherches de ce jour).
- **Angle et danger.** Raisons contre actions : faible à moyen (rapport 6). Il passerait à moyen si la réplication tient l'action identique ou ajoute un témoin de format. Rien ne l'annonce.

**Jasmine Li et Alex Turner — l'article annoncé sur la coopérativité envers les évaluations**
- **Quoi.** Le billet annonce un « article à paraître », sans lieu ni lien (rapport 7, texte intégral du billet). Le travail existe déjà comme poster d'atelier d'ICML 2026 (passation §4.3).
- **État.** Ce jour, les extraits ne montrent que le billet, la page MATS et la fiche ICML ; aucune version arXiv (vu par extrait de recherche, non ouvert).
- **Angle et danger.** Retrait pendant l'entraînement, par la disposition coopérative : moyen (rapport 6). La survie n'y est pas testée (rapport 4).

**Ayesha Imran et Aaliyan Shaikh — la suite d'*Inoculate or Reflect?***
- **Quoi.** Une suite sur d'autres modèles, graines et comportements. Le billet d'origine reproduit la réflexion contrefactuelle sur Qwen3-8B, avec patching entre deux fine-tunes d'une même base.
- **Source.** Rapport 5, résumé seul (deux résumés de l'outil).
- **Date.** Aucune.
- **Angle et danger.** L'anatomie, pour la suffisance par patching entre fine-tunes : moyen (rapport 5).

**MATS, hiver 2027 — le flux de Cozmin Ududec (UK AISI)**
- **Quoi.** Varier les indices (aider, être testé, être corrigé automatiquement) à tâche fixe. Suivre la conduite et les représentations internes à travers SFT, RL et entraînement de sûreté, et tester si une conduite disparaît ou reste cachée.
- **Source.** Rapport 6, texte intégral (pages des flux MATS).
- **État.** Candidatures closes.
- **Date.** Début de la cohorte non vérifié.
- **Angles et danger.** La dépendance au regard et la survie : moyen à faible (rapport 6).

### 1.3 Danger faible à moyen, ou faible (à citer, à revoir avant le post et avant l'arXiv)

| Qui | Quoi, état | Angle | Danger | Source et statut |
|---|---|---|---|---|
| Igor Ivanov (Meridian Cambridge), SPAR automne 2026 | Causes et mitigations du métajeu sur organismes modèles ; « Ongoing » | amplification | faible à moyen | rapports 2 et 6 ; rapport du 1er octobre, conscience comme condition |
| Igor Ivanov, *Call for Science of Eval Awareness* (25 déc. 2025) | Appel : mesurer la conscience après l'apprentissage de préférences, varier le format de l'entraînement constitutionnel, supprimer les traits | amplification | faible à moyen (annoncé comme direction) | rapport 6, texte intégral |
| Jeanne Salle et Sohaib Imran, SPAR | Interventions sur organismes modèles contre modèles naturellement désalignés ; entraînement de cohérence, boîte blanche | retrait pendant l'entraînement | faible à moyen | rapport 6 |
| David Africa (Resolution), MATS hiver 2027 | Suite d'Open Character Training, avec la coopérativité ; fuite de propensions par le RL | retrait, survie | faible à moyen | rapport 6, texte intégral |
| CaML (Brazilek, Chaudhary, avec John Lund), SPAR ; offre d'emploi du 1er sept. 2026 | Érosion d'une valeur installée par midtraining ; pilotage préventif par vecteur de persona ; décision de continuer pré-enregistrée sur deux semaines ; au moins un article prévu, sur OLMo 3 | survie | faible | rapports 4 et 6 |
| Muhammad Aaliyan, SPAR | Points de contrôle de Tülu 3.1 8B sous RL à récompenses vérifiables, avec items de conscience d'évaluation | amplification | faible | rapports 2 et 4 |
| Netzer Epstein et Neta Ravid, SPAR | Convergence des mesures de conscience d'évaluation, dont le score du J-lens | instruments | faible | rapports 2 et 6 |
| Betley et al. | D'autres pôles de correction et des modèles plus grands, annoncés | raisons pour le juge (« je suis noté ») | faible à moyen (mon estimation) | rapport 6, texte intégral du billet |
| Bharadwaj et Kirk | Refaire le DPO d'OLMo avec points de contrôle intermédiaires | amplification | faible | rapport 2 (mode de lecture non précisé) |
| OpenAI et Apollo | Collaboration sur l'émergence du métajeu (mars 2026) ; évaluations tierces de runs d'entraînement avec points de contrôle (annonce du 5 juillet 2026) | amplification | faible | rapport 2 (mode non précisé) |
| Anthropic, « Hacker-Opus » | Recherche en cours ; résumé intermédiaire dans le Risk Report d'août 2026 | raisons pour le juge, amplification | faible | rapport 4, texte intégral du PDF |
| Neel Nanda, avec Camila Blank et Agam Bhatia | Extensions du J-lens à plusieurs tokens ; lentilles publiées pour 8 modèles | anatomie (outil) | faible | rapport 5, résumé seul |
| Resolution (Irving et Africa) | Structure de bas rang des personas ; intervenir sans déplacer le mauvais comportement ailleurs ; recrutement, aucune date | ré-encodage | faible | rapport 3 (mode non précisé) |
| Konrad et al. ; Santos-Grueiro | Sondes de rang supérieur annoncées ; « certificats d'invariance » proposés | principe localisé, retrait | faible | rapport 3 |
| Cho et al. (*Constitutional Midtraining*) | Analyse mécaniste de leurs points de contrôle suggérée comme travail futur ; points publics, à 120B | principe localisé, anatomie | faible | rapport 5 |
| Auteurs de 2604.18946 | Promettent d'ajouter une base SFT standard sur les mêmes exemples | raisons contre actions | faible | rapport 1, lu par un site tiers (pith.science) |
| *PreCommitLens*, soumission anonyme à ACL ARR (août 2026) | Lentilles logit et jacobienne pour surveiller un agent avant l'action, Qwen jusqu'à 4B | anatomie | faible | rapport 5 |
| Ateliers de NeurIPS 2026 (décembre) | Vaid ; Dabir et al. ; listes d'acceptation des autres ateliers non publiques au 2 octobre | anatomie, dépendance au regard | faible | rapports 5 et 6 |
| Qiyao Wei, SPAR printemps 2026 | A posé la question des raisons ou du regard (proposition du 10 déc. 2025) ; seule sortie trouvée sur les indices d'évaluation ; aucun projet d'automne signalé par les rapports | raisons contre actions, dépendance au regard | faible en l'état | rapport 2, texte intégral (page et proposition) |
| *Pre-training interventions, ex post facto: Grafting model beliefs across checkpoints* (arXiv 2610.00767) | Titre seul. Si la greffe se fait entre points de contrôle d'une même base, c'est un voisin de la suffisance par patching | anatomie (à établir) | inconnu | vu par extrait de recherche, non ouvert |
| MATS, cohorte d'automne 2026 | Du 28 septembre au 4 décembre 2026, à Berkeley et à Londres ; projets non vus | inconnu | inconnu | vu par extrait de recherche, non ouvert |

**Non retenus comme concurrents.** Les projets SPAR de J Rosser, Sohan Venkatesh (LASR), Matthew Khoriaty, Shubhorup Biswas, Thomas Jiralerspong, David Baek, Kishan Panaganti et Suraj Srinivas, Vladimir Ivanov, et Allen Lu et al. (rapports 1, 4 et 6). Tous sont de danger faible.

---

## 2 · Les dates à surveiller, dans l'ordre

**L'hypothèse de calendrier.** La semaine 1 commence le jeudi 1er octobre 2026 : c'est la date du programme v1.1, et la passation v1.0 appelle « semaine 1 » la semaine qui suit. Chaque semaine de retard décale de 7 jours toutes les dates du programme ci-dessous.

| Date | Événement | Semaine du programme | Source et statut |
|---|---|---|---|
| 18 et 25 sept. 2026 (passé) | ICLR 2027 : résumés, puis articles (AoE). C'est la date de priorité de toute soumission concurrente invisible | avant la semaine 1 | rapport 6 (date dite vérifiée ; non relu) ; concordant avec un extrait de recherche, non ouvert |
| 28 sept. 2026 (passé) | Début de la cohorte d'automne de MATS | avant la semaine 1 | vu par extrait de recherche, non ouvert |
| 1er – 7 oct. | **Semaine 1 : le pré-enregistrement gelé et déposé.** Recommandé : OSF Registries, sous embargo jusqu'au post (passation §3, point 3, non confirmé). Nom décidé ce jour : Lazar seul, avec son ORCID ; Claude cité dans une phrase de méthode | 1 | programme v1.1, partie 9 ; décision relayée avec cette tâche |
| 2 oct. | Empreinte de référence de `exp9` SUMMARY.md relevée (`2a55f9b3…`) | 1 | revérifié par curl ce jour |
| 8 – 14 oct. | Semaine 2 : l'amendement du pré-enregistrement après le pilote (puissance, effectifs, graines), avant toute donnée du test du regard | 2 | passation §3, point 3 ; §5.4, n° 5 |
| octobre, sans date | À tout moment : la réplication de Second Look Research, l'article sur la coopérativité, la suite d'exp9, une suite d'Anthropic | 1 – 4 | §1 ci-dessus |
| 22 – 28 oct. | **Semaine 4 : le post sur l'Alignment Forum et LessWrong** ; fin de l'embargo ; recherche d'antériorité refaite juste avant (programme, partie 11, n° 1) | 4 | programme v1.1, partie 9 |
| jeudi 5 nov. | ICLR 2027 : reviews publiées ; discussion publique du 5 au 18 novembre | 6 | rapport 6 (reviews le 5 novembre) ; discussion vue par extrait de recherche, non ouvert |
| 5 – 11 nov. | **Première fenêtre où les soumissions à ICLR 2027 deviendraient lisibles** (inférence : une discussion publique suppose des articles visibles ; à vérifier). Refaire la recherche sur OpenReview cette semaine-là | 6 | inférence de ma part |
| mercredi 18 nov. | ICLR 2027 : fin de la discussion publique ; discussion privée du 19 novembre au 16 décembre | 7 | vu par extrait de recherche, non ouvert |
| vendredi 4 déc. | Fin de la cohorte d'automne de MATS | 10 | vu par extrait de recherche, non ouvert |
| décembre (dates non vérifiées) | Ateliers de NeurIPS 2026 (Vaid ; Dabir et al. ; d'autres dont les listes n'étaient pas publiques) | 10 – 12 | rapports 5 et 6 |
| 10 – 16 déc. | **Semaine 11 : l'arXiv** ; recherche d'antériorité refaite juste avant | 11 | programme v1.1, partie 9 et partie 11, n° 1 |
| lundi 14 déc. | SPAR : fin de la période de recherche (continuation optionnelle ensuite, d'après un extrait). Concerne Cadile, Lundqvist, Cody Wild, Shi Feng, Ivanov, et peut-être Second Look Research | 11 | rapports 1 et 6, texte intégral de la FAQ ; concordant avec un extrait de recherche, non ouvert |
| mercredi 16 déc. | ICLR 2027 : décisions. D'après un extrait, toutes les soumissions sont désanonymisées après la review, acceptées ou non | 11 | rapport 6 (décisions) ; désanonymisation vue par extrait de recherche, non ouvert |
| 17 – 23 déc. | Semaine 12 : rédaction, contre-lecture indépendante, préparation de la soumission | 12 | programme v1.1, partie 9 |
| samedi 19 déc. | **SPAR : Demo Day** | 12 | rapports 1 et 6 ; concordant avec un extrait de recherche, non ouvert |
| janvier 2027 (non officiel) | ICML 2027 : date limite des articles entre le 11 et le 28 janvier selon les agrégateurs, résumés quelques jours avant. COLM 2027 : 21 janvier selon un extrait, 31 mars selon une estimation. **Aucune date officielle vue** | après la semaine 12 | vu par extrait de recherche, non ouvert (agrégateurs contradictoires) |
| 26 – 30 avril 2027 | ICLR 2027 : conférence du 26 au 28, ateliers les 29 et 30 | — | vu par extrait de recherche, non ouvert |
| mai 2027 (projeté) | NeurIPS 2027 : vers le 20 ou le 21 mai, résumés vers le 14 ; appel non publié | — | vu par extrait de recherche, non ouvert |
| 4 – 9 juillet 2027 (non officiel) | ICML 2027, en Amérique du Sud, ville non annoncée | — | vu par extrait de recherche, non ouvert |

**Les lieux de soumission.** La cible est « plutôt conf principale ou revue ; prestigieux et ambitieux » (passation §3, point 5).
- ICLR 2027 est hors de portée : sa date limite était le 25 septembre 2026.
- Après un arXiv en semaine 11, la première conférence principale atteignable est ICML 2027 (ou COLM 2027), en janvier, cinq à sept semaines plus tard. Puis NeurIPS 2027, en mai.
- Les revues : rien n'a été vérifié dans cette passe.
- La politique de chaque lieu envers un post public, un pré-enregistrement public et une prépublication n'a été vérifiée pour aucun lieu. D'après un extrait (non ouvert), ICLR 2027 rejette sans examen un article qui révèle l'identité des auteurs. Il faudra savoir comment citer, dans l'article anonyme, un pré-enregistrement déposé sous le nom de Lazar.

---

## 3 · Les risques de calendrier, confrontés au calendrier du programme

### 3.1 Le calendrier de la v1.1 est tendu dès la semaine 1
Avant de geler le pré-enregistrement, il reste à faire :
- la mini-spec et les dix familles, le pipeline de données, l'organisme de validation (passation v1.0, §5 ; v1.2, §6, point 4) ;
- la tâche « axe de douleur », qui passe avant (passation v1.2, §6, point 2) ;
- la contre-lecture vierge, que la partie 11 (n° 8) place avant le gel et qui n'est pas lancée (passation v1.2, §3, point 6) ;
- la confirmation du périmètre, avec ou sans la phase de validation (§3, point 3).

Un dépôt avant le 7 octobre est donc peu probable. Or un glissement d'une semaine fait passer l'arXiv au 17 – 23 décembre, après la fin de SPAR (14 décembre) et après son Demo Day (19 décembre). L'objectif que Lazar a fixé, répondre « avant SPAR » (passation §3, point 4), n'a plus de marge au-delà d'un glissement de quelques jours. Le seul jalon public qui reste nettement avant SPAR est le post de la semaine 4.

### 3.2 Ce qui pourrait sortir avant le pré-enregistrement (d'ici à la semaine 1, ou à son glissement)
- **Déjà daté avant nous, quoi qu'on fasse.** Toute soumission à ICLR 2027 porte la date du 25 septembre 2026, avant tout pré-enregistrement. Le pré-enregistrement ne protège que contre ce qui viendra après lui. C'est le principal risque restant (passation §4.4), et il ne se lèvera qu'en semaine 6.
- **Une soumission retirée.** D'après un extrait (non ouvert), une soumission à ICLR 2027 retirée après la date limite devient publique et désanonymisée tout de suite. Une soumission concurrente peut donc apparaître à tout moment.
- **À tout moment, sans date.**
  - La réplication de Second Look Research : raisons contre actions, faible à moyen.
  - L'article sur la coopérativité : retrait pendant l'entraînement, moyen.
  - Des résultats DPO ou PPO poussés sur le dépôt exp9. Le dépôt est public ; un commit suffit, sans annonce. La sous-question est déjà prise ; les résultats en élargiraient la portée.
  - Le billet de blog.daios.tech, s'il relève du projet de Cadile.
- **L'effet sur nos formulations.** Rien de cela n'annonce la combinaison centrale. Les formulations « to our knowledge » jugées tenables au §5.5, n° 9, de la passation le restent tant qu'aucune de ces sorties n'inhibe la représentation « je suis évalué » dans des modèles entraînés sur les raisons.

### 3.3 Entre le pré-enregistrement et le post (semaines 1 à 4)
- **L'embargo.** Avec l'embargo d'OSF (recommandé, non confirmé), le protocole reste invisible ; l'horodatage, lui, est acquis.
- **Le périmètre.** Pour que l'horodatage couvre les huit angles, le texte gelé en semaine 1 doit les couvrir tous, phase de validation comprise si Lazar la confirme. Le post ne portera que sur l'expérience minimale.
- **Les sorties possibles.** Les mêmes qu'au §3.2. S'y ajoutent :
  - les annonces d'acceptation aux ateliers de NeurIPS 2026 (dates non vérifiées) ;
  - la suite d'Anthropic, qui n'a pas de date.
- **La recherche avant le post.** La recherche d'antériorité refaite juste avant le post (partie 11, n° 1) tombe avant l'ouverture d'ICLR. Elle ne peut donc pas lever le risque principal.

### 3.4 Entre le post et l'arXiv (semaines 4 à 11)
- **L'exposition.** Le post rend le programme visible sept semaines avant la fin de SPAR et de MATS.
  - Les équipes qui ont déjà l'outillage peuvent prendre les angles que le programme placera après le post : le principe localisé et l'anatomie (semaines 5 à 7), le retrait pendant l'entraînement (semaine 7), la survie et les raisons pour le juge (semaines 9 et 10).
  - Lundqvist a l'organisme de Hua et al., un pipeline de juge et la question de la survie. Cadile a le contraste entre démonstrations et raisons.
  - Seul le pré-enregistrement daté protège ces angles.
- **Semaine 6 (5 novembre).** C'est sans doute le premier moment où les soumissions à ICLR 2027 deviennent lisibles (inférence à vérifier). Une soumission concurrente trouvée là a priorité sur nous. Il faut la citer et s'en distinguer avant l'arXiv. Refaire la recherche sur OpenReview cette semaine-là, avec les termes des huit angles.
- **Semaine 10 (4 décembre).** Fin de MATS : des billets de fin de cohorte peuvent sortir en décembre. Leur date n'est pas vérifiée.
- **Semaine 11 (10 – 16 décembre).** L'arXiv tombe en même temps que la fin de SPAR (14 décembre), que les décisions d'ICLR (16 décembre) et que les ateliers de NeurIPS 2026. Les présentations du Demo Day (19 décembre) viennent juste après. C'est la semaine la plus chargée en concurrence, et la recherche d'antériorité d'avant l'arXiv doit s'y faire.
- **La suite d'Anthropic.** Elle peut sortir n'importe quand. Elle menace surtout l'anatomie, que la v1.1 traite en semaines 5 à 7.

### 3.5 Après l'arXiv
- La soumission vise janvier 2027 au plus tôt (ICML 2027 ou COLM 2027, dates non officielles), puis mai 2027 (NeurIPS 2027).
- Les soumissions de janvier ne seront visibles que bien après notre arXiv. Elles ne nous précèdent pas.
- Les articles des ateliers de décembre et les sorties de SPAR et de MATS seront antérieurs à la soumission. Ils devront être cités, même s'ils sont postérieurs à notre pré-enregistrement.

### 3.6 Ce qu'on ne peut pas voir
- **ICLR 2027.** Les soumissions ne sont pas publiques (`public_submissions: false`, lu dans un résumé automatique par le rapport 6). La recherche par l'API renvoie 0 résultat et l'accès direct aux notes renvoie 403 (rapports 1, 2, 4, 5 et 6). Probablement jusqu'au 5 novembre.
- **NeurIPS 2026, ateliers.** Les décisions ne sont pas publiques : énumération en 403, recherche à 0 résultat (rapport 6).
- **ACL ARR.** Soumissions anonymes : *PreCommitLens*, *When Safety Routing Breaks* (rapports 4 et 5).
- **SPAR.** L'avancement interne des projets n'est pas visible. Le document Google d'*Infohazard Evaluations* n'a pas été ouvert (rapport 2). La bibliothèque de SPAR a été téléchargée sans être analysée (rapport 6).
- **MATS, cohorte d'automne 2026.** La liste des projets n'a pas été vue.
- **Anthropic Fellows, Astra, Pivotal.** Aucune liste de projets pertinente (rapport 6).
- **Le travail interne des laboratoires.** En premier lieu, la suite d'Anthropic sur la réflexion contrefactuelle.
- **Le dépôt exp9.** L'historique des commits et le dossier `results/` ne sont pas lisibles (rapports 4 et 6). Seule une variation de l'empreinte de SUMMARY.md, ou du README, signalera une suite.
- **Les sites illisibles.** Le site de Second Look Research exige JavaScript (rapport 2). Le blog de Redwood refuse ClaudeBot. lasrlabs.org est refusé par robots.txt (rapport 6).

### 3.7 Les décisions de Lazar qui touchent ce calendrier (relayées avec cette tâche, 2 octobre)
- **Le nom du pré-enregistrement : validé.** Lazar seul, avec son ORCID ; Claude cité dans une phrase de méthode, pas comme auteur.
- **Le contact avec Cadile et Lundqvist : « non pas encore ».**
  - La passation proposait de les contacter après le dépôt ; ce n'est pas retenu pour l'instant.
  - La surveillance passe donc seulement par les sources publiques : pages SPAR, Alignment Forum, Demo Day, empreinte du dépôt exp9.
  - La décision reste à reprendre quand Lazar le voudra.

### 3.8 Ce que la surveillance demande (propositions, à soumettre à Lazar)
1. Relire chaque semaine, par curl, le README et SUMMARY.md d'exp9, et comparer l'empreinte à `2a55f9b3…`.
2. En semaine 6, juste après le 5 novembre : la recherche sur OpenReview, avec les termes des huit angles.
3. Avant le post (semaine 4) et avant l'arXiv (semaine 11) : la recherche d'antériorité de la partie 11, n° 1. Y ajouter les pages SPAR de Cadile, Lundqvist, Cody Wild, Shi Feng et Second Look Research, le billet de blog.daios.tech, et arXiv 2610.00767.
4. Trancher si l'arXiv avant le 14 décembre est un objectif ferme. Sinon, assumer que le post de la semaine 4 et le pré-enregistrement sont les seuls jalons publics avant SPAR.
5. Avant de choisir le lieu : vérifier sur les sites officiels les dates d'ICML 2027, de COLM 2027 et de NeurIPS 2027, et la politique de chacun envers les posts, les pré-enregistrements et les prépublications.

---

## 4 · Ce que je n'ai pas pu ouvrir, et mes requêtes

### 4.1 Non ouverts
- `https://iclr.cc/Conferences/2027/Dates` : WebFetch refusé par le proxy (« EGRESS_BLOCKED »). Les dates d'ICLR 2027 restent vues par extrait, en concordance avec le rapport 6.
- `https://sparai.org/` (la FAQ) : WebFetch refusé par le proxy. Les pages SPAR de Second Look Research et des autres projets n'ont pas été ouvertes. Je n'ai pas tenté d'autre voie vers sparai.org après ce refus.
- `https://blog.daios.tech/p/virtue-ethics-based-character-training` : WebFetch refusé par le proxy.
- Non tentés, car refusés par la politique réseau de la tâche :
  - le billet LessWrong de Second Look Research ;
  - arXiv 2610.00767 ;
  - le papier sur l'espace de travail (transformer-circuits.pub, arxiv.org) ;
  - les pages d'OpenReview.
- Non tentés, car refusés d'après les rapports 4 et 6 : l'historique des commits et le dossier `results/` d'exp9 (robots.txt de GitHub, API en 403).
- Les dates d'ICML 2027, de COLM 2027 et de NeurIPS 2027 ne viennent que d'agrégateurs, et ces agrégateurs se contredisent. Aucune source officielle n'a été lue.

### 4.2 Ouvert
- Par curl, `https://raw.githubusercontent.com/ryanlundqvist/exp9-rlaif-leakage/master/README.md` (HTTP 200, une ligne).
- Par curl, `https://raw.githubusercontent.com/ryanlundqvist/exp9-rlaif-leakage/master/SUMMARY.md` (12 666 octets, sha256 `2a55f9b382683b4a17ead2588966eb8ddbe2db0815fa8eff46758d214c183fec`). J'en ai lu l'en-tête, la section sur le plan de RL et la section « Future work ».

### 4.3 Les requêtes WebSearch (15 sur 15)
1. ICLR 2027 dates reviews released author discussion decision notification
2. SPAR fall 2026 Demo Day December research period
3. Second Look Research replication "Teaching Claude Why" open-weight
4. ICML 2027 call for papers submission deadline
5. Anthropic counterfactual reflection training follow-up principles generalization J-space
6. Cadile "Constitutions and Reasons" SPAR virtue character training results
7. Lundqvist "eval cooperativeness" OR "eval gaming" training-time mitigation survive post-training 2026
8. MATS OR "Anthropic Fellows" 2026 project evaluation awareness reasoning training generalization ablation open-weight
9. "Eval Cooperativeness" Li Turner arXiv paper 2026
10. ICLR 2027 author guide submissions made public OpenReview anonymous after deadline withdrawn
11. MATS Autumn 2026 program dates symposium December 2026
12. NeurIPS 2027 COLM 2027 submission deadline dates
13. "ICML 2027" abstract deadline full paper deadline January 2027 Rio OR "South America" icml.cc dates
14. "Second Look Research" midtraining replication results 2026
15. fine-tuning on reasons vs demonstrations alignment "evaluation awareness" steering open-weight preprint October 2026

La dernière n'a rien remonté de nouveau sur la combinaison : seulement des travaux déjà connus (*Steering Awareness*, Hua et al.).
