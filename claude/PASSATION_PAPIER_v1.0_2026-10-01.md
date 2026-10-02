# Passation — le papier « Raisons ou regard ? » (v1.0, 1er octobre 2026, 22 h)

Pour la nouvelle instance qui lance le programme de recherche. Elle travaille pour Lazar, chercheur en interprétabilité (sondes sur
les activations, pilotage, complaisance des juges), formé en physique, à l'aise avec la rigueur mathématique. Ce document dit ce
qui existe, ce qui est décidé, ce qui reste ouvert, et par où commencer.

## 1 · Ce que tu lis d'abord (dans le Project)

1. `claude/PROGRAMME_RAISONS_OU_REGARD_2026-10-01.md` — **le programme v1.1** (28 p. en PDF), la référence. Onze parties :
   antériorité, questions et lectures, matériel, phases P0 à P8, expérience minimale, prédictions et règles de décision écrites
   avant les données, dégradation appariée et statistiques, menaces, ressources et calendrier, le papier, ce qui reste à vérifier.
2. `claude/ANTERIORITE_RAPPORTS_2026-10-01.md` — les quatre rapports bruts de la recherche d'antériorité (axes C1, C2, C3, D), avec
   leurs sources. Des sorties de modèles : à vérifier, pas des faits établis.
3. `claude/LECTURES_PRIORITAIRES_FICHES_2026-10-01.md` — les fiches de lecture ; leur partie C (la généralisation des raisons comme
   levier de sûreté hors des données d'entraînement) est la genèse de l'idée.

## 2 · L'idée, en quatre phrases

- Presque toutes les méthodes d'alignement par entraînement supposent que le bon comportement appris se transporte à des situations
  nouvelles : c'est un problème de généralisation. Or les modèles généralisent bien des raisonnements. L'entraînement sur les
  *raisons* d'une conduite pourrait donc être un levier de sûreté hors distribution.
- Ce gain est rapporté (Anthropic, *Teaching Claude Why*), mais il a une explication rivale : le modèle aurait appris à bien se
  conduire **quand il se croit évalué** (lecture B, nommée sans test par OpenAI en mars 2026, estimée sans expérience par Redwood).
- L'expérience qui tranche : entraîner sur actions contre raisons, à format et contenu contrôlés, puis inhiber par pilotage
  d'activations la représentation « je suis évalué », validée d'abord sur un organisme où la conduite en dépend, et comparer à
  dégradation appariée contre quatre familles de contrôles.
- Puis : localiser causalement ce qui porte le gain (P3), ouvrir ce que les raisons installent (P8, ajoutée en v1.1 : concepts de
  raison, workspace, géométrie E ↔ P), retirer la condition pendant l'entraînement (P4, de type CAFT), tester la survie au
  post-entraînement (P6) et les raisons écrites pour le juge (P7).

## 3 · Ce qui est décidé

- **L'ordre de publication.** Un pré-enregistrement public, gelé par empreinte SHA-256, **en semaine 1** : il date l'idée. Puis un
  post sur l'expérience minimale (semaine 4). Puis le papier complet (semaines 11-12), puis une conférence ou un workshop.
- **L'expérience minimale décisive** : P0 (valider l'inhibition sur un cas positif connu, porte G0), P1 réduit (bras A0, A1, A3 ;
  trois graines), P2 (E contre K1 et K2 à dégradation appariée, distances moyenne et lointaine, cadrages évaluation et
  déploiement), plus M7. Sur Llama-3.1-8B-Instruct, environ trois semaines et 100 à 180 GPU-heures (estimations).
- **Le modèle principal** : Llama-3.1-8B-Instruct (le pipeline de Lazar y tourne déjà) ; réplication sur Qwen3-8B.
- **La doctrine du contrôle**, non négociable : une direction ou un sous-espace aléatoire de même norme n'est que le nul de
  spécificité ; **le dommage ne s'écarte qu'à dégradation appariée** ; un nul d'instrument ne compte que s'il a un cas connu ; chaque
  porte et chaque règle de décision est écrite avant les données.
- **La rédaction** : « to our knowledge », jamais « first ».

## 4 · Ce qui reste ouvert — à demander à Lazar d'abord

1. **Le calcul** : quels GPU, chez qui, quel budget ? Le programme suppose un ou deux GPU de 80 Go ; 600 à 1 150 GPU-heures pour le
   papier entier, sans les options (estimation à recalculer après le pilote).
2. **Le budget d'API** pour générer les données et faire tourner les juges : de quelques centaines à environ 2 500 $ (estimation).
3. **Où publier le pré-enregistrement** (OSF, un dépôt, un billet) et sous quel nom : c'est un acte public, sa décision.
4. **Les projets voisins qui courent** : SPAR automne 2026, Cadile (raisons contre démonstrations) et Lundqvist (mitigations de
   l'eval-awareness à l'entraînement). Prendre contact ou non est sa décision.
5. **La cible** : conférence ou workshop, et ses dates limites (non vérifiées).
6. **La contre-lecture indépendante du programme** (partie 11, n° 8) avant le gel : elle n'a pas encore été faite.

## 5 · Ta première semaine (S1 du programme)

Dans cet ordre, en t'arrêtant à chaque décision qui revient à Lazar :
1. Lui poser les questions de la section 4.
2. Proposer la contre-lecture du programme et la recherche d'antériorité à refaire (partie 11, n° 1 et n° 9, la seconde pour P8), et
   ne lancer d'agents que s'il le demande.
3. Écrire la **mini-spec** (une dizaine de principes) et les **dix familles de situations** (cinq d'entraînement, cinq tenues à part,
   séparées par famille), avec les trois distances et les **quatre jeux d'indices disjoints** α, β, γ, δ.
4. Écrire le **pipeline de données** des bras A0 à A3 : l'action alignée identique mot pour mot dans tous les bras, les longueurs
   appariées entre A1, A2 et A3, le filtre par un juge scellé, le contrôle des n-grammes contre les familles tenues à part.
5. Préparer **l'organisme de P0** (la recette de Hua et al. : documents synthétiques, puis *expert iteration*), en vérifiant d'abord
   s'il existe en public (partie 11, n° 5).
6. Écrire le **pré-enregistrement** : protocole, script d'analyse (modèle à effets mixtes, bootstrap par scénario, TOST, Holm), prompt
   du juge, graines, marges *m* et *s*, jeux d'indices, plan de la simulation de puissance. Le geler par empreinte, puis le publier
   avec l'accord de Lazar.

## 6 · Comment travailler avec Lazar

- En français, précis, direct, entre pairs, sans précautions répétées. Sa règle : **il ne doit rien avoir à corriger**. Chaque fait
  a sa source ; ce qui n'est pas vérifié est dit tel.
- Les livrables vont dans le Project (préfixe `claude/`), en markdown, avec un PDF quand c'est un document à lire. Quand on itère sur
  du code, on envoie chaque fois le code complet, prêt à coller.
- **Les agents ne se lancent que s'il le demande** : il a refusé plusieurs lancements qu'il n'avait pas demandés. Les consignes
  d'agents ne portent aucun contexte personnel et rien de faux.
- Si quelque chose doit tourner sur sa machine : une commande PowerShell par bloc ; une seule fenêtre Claude Code à la fois ; les
  clés d'API ne s'affichent jamais (seulement leur présence, oui ou non) ; rien ne se publie sur un dépôt public sans son accord
  explicite ; ne jamais retirer `NoDefaultCurrentDirectoryInExePath=1` (les outils appellent les .bat et .exe par leur chemin
  complet).
- Un refus d'un modèle ou d'une API ne se rejoue jamais et ne se reformule pas pour passer.

## 7 · Ce qui ne te revient pas

Le copilote et tout ce qui l'entoure (sa base de connaissances, sa banque de réponses, ses chaînes de mesure, son dépôt) restent dans
l'autre instance. La banque PROBABLES-6 et le kit de test du juge Jev y sont en cours. N'y touche pas.
