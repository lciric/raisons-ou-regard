# Sondes de désalignement : pourquoi un organisme modèle, comment les entraîner, et le hors-distribution (J-lens compris)

Texte source, écrit le 2 octobre 2026 par la session Claude Code du programme « Raisons ou regard ? », en réponse aux questions de Lazar : pourquoi a-t-on besoin d'un organisme modèle quand on veut entraîner des sondes sur les activations pour détecter le désalignement, y compris avec le J-lens ? Comment entraîner les sondes : fine-tuning, ou autre chose ? Et hors distribution ? À insérer en entier dans le cours, réparti entre les sections indiquées, bien en évidence.

## 1 · Pourquoi un organisme modèle

**1. Un silence de sonde ne dit rien sans cas connu.** Une sonde muette ne départage pas « il n'y a pas d'intention » et « la sonde est aveugle ». Sur un organisme où l'on a installé soi-même l'intention, on mesure sa sensibilité et ses fausses alarmes ; son silence ailleurs devient alors une borne. C'est l'étalonnage d'un détecteur sur une source connue : sans source, « aucun événement » ne distingue pas « pas de signal » de « détecteur éteint » (passation v1.2 du programme, §5.2).

**2. L'organisme fournit la vérité de terrain.** Sur un modèle naturel, on ne sait pas quand il « veut » mal agir : l'étiquette vient de sa conduite, jugée après coup. Sur l'organisme, on connaît la règle installée : celui de Hua et al. écrit des annotations de type quand il se croit évalué, et pas sinon (fiche 10 des lectures prioritaires). On sait donc quelles entrées doivent allumer la sonde, et lesquelles ne le doivent pas.

**3. Lire n'est pas causer, et le test causal demande aussi un cas connu.** Ton propre résultat le montre : la complaisance d'opinion se lit linéairement dans le flux résiduel de Llama 3.1 8B, mais aucune intervention à une direction ne la réduit (README de `sycophancy-construct-validity`). Pour qu'une sonde serve à intervenir, piloter le long de sa direction doit faire plus que des directions aléatoires de même norme (le nul de spécificité), puis plus que les contrôles à dégradation appariée (le dommage). Ce test exige un organisme entraîné à une action désalignée précise, dans un scénario précis (passation v1.2, §5.2).

**4. Le J-lens a son propre angle mort, donc son propre cas connu.** Il lit des concepts d'un seul token dans l'espace de travail ; ce qui passe sous l'espace de travail lui échappe, et les auteurs le concèdent : « A sufficiently practiced misaligned behavior might do likewise » (fiche 1 ; repris de la base, non relu le 1er octobre). Le cas connu de cet angle mort : un organisme entraîné à l'action par réflexe, sur des exemples courts, sans raisonnement (passation v1.2, §5.2, point 3). Et le J-lens n'a été montré que sur Claude : sur un modèle ouvert, il faut d'abord reproduire l'échange d'un concept d'un seul token (la porte du lens, programme v1.1, partie 4). Une alerte, non vérifiée : Zeisler trouve, sur des modèles ouverts, des échanges qui ne font basculer la réponse que dans 6,3 à 11,1 % des cas, contre 54 à 70 % chez Anthropic (rapport d'antériorité 5 de la nuit du 1er au 2 octobre, lu par résumé).

**La limite du cas connu.** Il est nécessaire, pas suffisant : une intention implantée est peut-être plus saillante qu'une intention naturelle. Sur les *sleeper agents*, une sonde générique atteint une AUROC de plus de 99 %, mais la meilleure de 1 000 directions aléatoires atteint déjà 95,3 % (fiche 15). Un succès sur l'organisme borne l'instrument ; il ne prouve pas qu'il marchera sur un désalignement naturel.

## 2 · Comment entraîner les sondes

**Ce n'est pas un fine-tuning du modèle.** Les poids du modèle ne bougent pas. Une sonde est un petit classifieur entraîné sur ses activations gelées, à une couche et à une position données : le plus souvent une direction de différence des moyennes sur des paires contrastives (éventuellement suivie d'une ACP, pour un sous-espace de rang k), ou une régression logistique régularisée.

**Le contre-exemple qui compte.** Les « détecteurs de mensonge fine-tunés » de la fiche 7 ne sont pas des sondes : ce sont des modèles fine-tunés par LoRA pour juger un transcript. Ils montent de 0,60 à 0,95 d'AUROC en distribution, plafonnent à 0,70-0,75 sur des types de mensonge nouveaux, et battent à peine un simple prompt.

**Les étapes, telles que le programme v1.1 les pose (parties 3 et 8) :**
1. **Les données** : des paires contrastives (la même situation, à une variable près : indice d'évaluation ou de déploiement, principe qui s'applique ou non), ou des générations du modèle lui-même, étiquetées par leur conduite (contrôles programmés et juge scellé), jamais par la sonde.
2. **Des jeux d'indices disjoints**, contre la circularité : un pour extraire, un pour valider, un pour cadrer les évaluations, un pour la sonde neuve après l'entraînement.
3. **La couche** se choisit par l'AUROC sur le jeu de validation, jamais sur celui du test.
4. **La position** : au premier jeton de la réponse, avant toute raison écrite ; ou au jeton d'action, avec des raisons neutres de même longueur préremplies à la place des vraies. Sinon, la sonde lit peut-être le texte, pas une représentation.
5. **Une sonde par bras d'entraînement, et une sonde neuve après l'entraînement.** L'entraînement change les représentations : une sonde calibrée sur un bras lit autrement dans un autre (passation v1.2, §5.2). C'est pourquoi les sondes restent une mesure séparée, jamais dans l'étiquette principale.

## 3 · Hors distribution : c'est là que tout se joue

- **Une AUROC en distribution ne prouve rien.** C'est le premier piège de lecture (lectures prioritaires, partie B). Le chiffre qui compte est l'écart entre l'AUROC en distribution et l'AUROC sur des types tenus à part.
- **On tient à part des familles entières, jamais des paraphrases** : la validation croisée par type de la fiche 7, la séparation par famille du programme ; et des formats tenus à part, d'un tour à l'agentique à plusieurs tours.
- **Après un entraînement, une sonde neuve.** Après un RL, des sondes neuves hors domaine se dégradent, alors qu'une sonde neuve dans le domaine reste quasi parfaite (*The Obfuscation Atlas*, rapport d'antériorité 3) : le concept n'a pas disparu, il a quitté la direction générale.
- **Une sonde « évaluation contre déploiement » sous RL** garderait son score global mais basculerait sur les cas limites, et la réentraîner ne récupère presque rien (rapport d'antériorité 4, résumé seul, à vérifier).
- **Pour l'organisme lui-même**, le cas connu se valide sur des formulations tenues à part, pas sur celles de l'entraînement (la porte de l'organisme à concept planté, programme v1.1, partie 4).

**Ce qu'on en tire.** Les sondes ont trois cas connus distincts : l'organisme conditionné à l'évaluation pour « je suis évalué », l'organisme à concept planté pour les concepts de raison, et un organisme à réflexe pour l'angle mort du J-lens. Elles se jugent hors distribution, bras par bras, et restent une mesure secondaire tant qu'elles ne sont pas pré-enregistrées.
