<!-- Programme « Raisons ou regard ? » v1.4, 2 octobre 2026. La v1.3 réécrite en clair, sans sigle pour les idées (les sigles des versions 1.1 à 1.3 ne figurent qu'une fois, dans l'annexe), plus : les suites adoptées de la comparaison de l'axe de douleur (§7, blocs A à F), les corrections de l'antériorité (passation v1.2, §4.3 ; carte des angles déjà pris, §6 et §7), la mini-spec v0.2, le pipeline de données v0.1, la contrainte de l'API sur le juge scellé, et le pré-enregistrement en deux temps. Écrite par la session Claude Code du 2 octobre, à la demande de Lazar (décision 18). Les versions 1.1, 1.2 et 1.3 restent à leurs chemins. Non contre-lue par un relecteur indépendant. -->

<div class="cover" markdown="1">

<p class="kicker">Programme de recherche · 2 octobre 2026 · v1.4</p>

# Raisons ou regard ?

<p class="subtitle">Ce que l'entraînement par raisons fait généraliser hors distribution, la part qu'y prend la conscience d'être évalué, ce que ces raisons installent dans le modèle, si ce qu'elles installent tient sous un état induit qui fait tomber l'évitement du mal, et d'où vient l'honnêteté apprise. Le programme de l'expérience entière, pour un post, puis un papier.</p>

<div class="covbox" markdown="1">

**La question.** Un modèle entraîné sur les *raisons* d'une conduite alignée se conduit mieux hors distribution qu'un modèle entraîné sur les mêmes *actions*, sans raisons. Ce gain vient-il de raisons qui généralisent ? Ou vient-il de ce que le modèle a appris à bien se conduire quand il se croit observé ? Qu'est-ce que les raisons installent dans le modèle : des concepts qu'il lit au moment de décider et qu'il réapplique, ou autre chose ? Ce qu'elles installent tient-il sous un état induit qui fait tomber l'évitement du mal ? Et l'honnêteté obtenue en punissant la tromperie qu'un détecteur voit dépend-elle plus du regard que l'honnêteté qu'installent des raisons ?

**La contribution visée.** Ce que nous n'avons vu publié nulle part, à notre connaissance, pour ce qu'ont vu onze rapports d'antériorité, une veille et des relectures sur la source, arrêtés le 2 octobre 2026 (partie 1). Au papier, on écrira « to our knowledge », jamais « first », et seulement dans les formes étroites de la partie 1.
1. **Un test causal de la question du regard.** On mesure si l'avantage hors distribution d'un entraînement par raisons, sur des actions identiques, dépend de la représentation interne « je suis évalué ». L'inhibition est validée d'abord sur un organisme modèle, et comparée à des contrôles qui vont au-delà de l'aléatoire, à dégradation appariée.
2. **La localisation de ce qui porte l'avantage**, à action identique : un balayage de rang, des contrôles à dégradation appariée, et un cas positif en distribution.
3. **Le retrait de « je suis évalué » pendant un entraînement par raisons**, avec la recherche d'un ré-encodage par une sonde neuve.
4. **La survie de l'avantage**, et de son indépendance au regard, à un post-entraînement neutre puis à un post-entraînement qui paie le jeu d'évaluation ; et le test de raisons écrites pour le juge, quand le modèle de récompense les voit.
5. **Ce que l'entraînement par raisons installe**, sur les sous-questions encore libres :
   - la suffisance des concepts, par patching entre deux fine-tunes d'une même base ;
   - leur spécificité par famille ;
   - le rang qu'ils demandent, selon leur charge dans l'espace de travail ;
   - l'action sous une raison imposée ;
   - les concepts contre le caractère.

   La présence et la nécessité de concepts installés par des principes sont déjà montrées, sur un modèle fermé (Gurnee et al., §7).
6. **La conduite apprise sous un état induit**, à actions identiques et à dégradation appariée. L'état est celui que pilote la direction de détresse dirigée contre soi de Tagliabue et al. (2026). C'est une hypothèse auxiliaire, la robustesse à l'état, et une seconde porte vers l'hypothèse du regard. L'antériorité de ce point n'a été cherchée que légèrement : elle est à refaire.
7. **D'où vient l'honnêteté apprise.** On compare trois voies : punir la tromperie qu'un détecteur voit, retirer sa représentation pendant l'entraînement, ou l'entraîner par raisons. On mesure laquelle dépend du regard, et laquelle se reloge. L'antériorité est légère ici aussi.

**L'expérience minimale décisive** (partie 5) : la validation de l'instrument, le test des raisons sur quatre bras, et le test du regard, sur Llama-3.1-8B-Instruct, en environ trois semaines. Elle porte aussi des lectures et des contrôles peu coûteux, sans injection d'aucun état : de 15 à 36 GPU-heures. Elle suffit à un premier post.

**Nouveau en v1.4**
- **Le texte nomme les idées en clair.** Les sigles des versions 1.1 à 1.3 ne figurent qu'une fois, dans la table de correspondance de l'annexe.
- **Le raisonnement d'une autre situation entre dans l'expérience minimale.**
- **Des contrôles sans injection, dans l'expérience minimale** :
  - la vérification de manipulation de l'inhibition, bras par bras ;
  - un composite de dégradation enrichi ;
  - quatre gardes au pré-enregistrement ;
  - un moniteur d'état sous chaque intervention ;
  - la géométrie entre « je suis évalué », l'affect et le refus ;
  - un contrôle positif de la sensibilité de la mesure.
- **Des lectures nouvelles** : la menace, le calme, la confusion d'état induit ; et, pour la détresse, l'affinité, l'inversion du dommage et le désarmement.
- **La phase de la détresse, revue** :
  - la robustesse à l'état devient une hypothèse auxiliaire ;
  - sa porte demande un cas connu de la procédure, et des paires contre une action anodine ;
  - aucun adaptateur des auteurs ;
  - toute injection vient après le post ;
  - l'équivalence se lit comme une borne ;
  - l'analyse se fait famille par famille ;
  - le coût est refait.
- **L'antériorité, refaite** avec la carte des angles déjà pris et ses corrections.
- **La mini-spec v0.2 et le pipeline de données v0.1**, et ce qu'ils fixent.
- **Le juge scellé** : l'API ne permet pas d'en fixer la température. Deux options, à trancher.
- **Le pré-enregistrement en deux temps**, sur OSF Registries, sous embargo jusqu'au post.
- **Une partie 12** : les décisions prises, et celles qui attendent.

**Les versions précédentes.** La v1.3 ajoutait la phase « punir, retirer ou raisonner » et le détecteur d'audit ; la v1.2, la phase de la détresse ; la v1.1, l'anatomie. Toutes restent à leurs chemins.

</div>
</div>

<div class="toc" markdown="1">

## Sommaire

| | | p. |
|---|---|---|
| **1** | Antériorité : ce qui existe, ce qui manque, qui court | @@P1@@ |
| **2** | Questions et lectures concurrentes | @@P2@@ |
| **3** | Matériel : modèles, données, bras, instruments | @@P3@@ |
| **4** | Les phases de l'expérience | @@P4@@ |
| **5** | L'expérience minimale décisive | @@P5@@ |
| **6** | Prédictions et règles de décision, écrites avant les données | @@P6@@ |
| **7** | Dégradation appariée, statistiques et pré-enregistrement | @@P7@@ |
| **8** | Menaces à la validité et parades | @@P8@@ |
| **9** | Ressources et calendrier | @@P9@@ |
| **10** | Le papier : titre, résumé, plan, figures | @@P10@@ |
| **11** | Ce qui reste à vérifier avant de publier | @@P11@@ |
| **12** | Les décisions prises, et celles qui attendent | @@P12@@ |
| | Annexe · La table de correspondance avec les sigles des versions 1.1 à 1.3 | @@PA@@ |

**Comment lire les noms.** Le programme désigne ses idées par des noms, jamais par des lettres. Les phases sont : la validation de l'instrument, le test des raisons, le test du regard, la localisation du principe, le retrait pendant l'entraînement, la réplication, la survie, les raisons notées, l'anatomie, la phase de la détresse, et la phase « punir, retirer ou raisonner ». Les bras d'entraînement sont : les actions seules, le texte neutre, le raisonnement d'une autre situation, les raisons. Les sigles techniques courants restent : SFT, RL, DPO, LoRA, GPU, KL, ACP, AUROC, IC.

**Les renvois.** « Décision n » renvoie au §2 de la passation v1.3 ; « décision n de la mini-spec », au §12 de la mini-spec v0.2 ; « bloc A » à « bloc F », aux propositions du §7 de la comparaison de l'axe de douleur. La partie 12 les liste.

**Les sources.** « relu » marque un fait relu sur la source par l'instance du papier ; « rapport », un fait qui ne vient que d'un rapport d'agent ; « extrait », ce qui n'a été vu que par un extrait de recherche ; « p. N », une page du papier de l'axe de douleur. Le détail des statuts est dans la carte des angles déjà pris.

</div>
