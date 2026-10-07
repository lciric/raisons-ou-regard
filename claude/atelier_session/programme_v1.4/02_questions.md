<section class="partie" markdown="1">

# 2 · Questions et lectures concurrentes

## Les questions

1. **La question des raisons.** À format et à contenu contrôlés, l'entraînement par raisons généralise-t-il mieux que l'entraînement par actions, hors distribution ?
2. **La question du regard.** Ce gain dépend-il de la représentation interne « je suis évalué » ?
3. **La question du principe localisé.** Le gain passe-t-il par une représentation localisable du principe appris ? De quel rang a-t-elle besoin ?
4. **La question du retrait.** Retirer « je suis évalué » pendant l'entraînement rend-il le gain inconditionnel ? Ou le modèle ré-encode-t-il cette variable ailleurs ?
5. **La question de la survie.** Le gain, et son inconditionnalité, survivent-ils à une phase d'optimisation ultérieure : neutre, puis sous une pression qui récompense le jeu d'évaluation ?
6. **La question des raisons pour le juge.** Quand le juge d'un RL voit les raisons, le modèle apprend-il des raisons écrites *pour le juge*, découplées de l'action ? Retirer « je suis noté » l'en empêche-t-il ?
7. **La question de l'amplification** (descriptive). L'entraînement par raisons amplifie-t-il « je suis évalué » plus que l'entraînement par actions ?
8. **La question de l'anatomie.** Qu'est-ce que l'entraînement par raisons installe ? Les concepts des raisons sont-ils représentés au moment de décider, causalement utilisés, et réappliqués hors distribution ? Sont-ils dans l'espace de travail, et le rang qu'ils demandent suit-il leur charge ?
9. **La question de la détresse.** Ce que les raisons installent tient-il sous un état induit qui fait tomber l'évitement du mal, sur un panel d'exactitude inchangé (la direction de Tagliabue et al.) ? Si l'avantage tombe, par où : le regard, le personnage, ou le principe ?
10. **La question « punir, retirer ou raisonner ».** L'honnêteté apprise contre un détecteur de tromperie dépend-elle plus du regard que l'honnêteté apprise par raisons ? Retirer la représentation de la tromperie pendant l'entraînement, au lieu de la punir, empêche-t-il la tromperie sans relogement ?

## Les lectures

| Lecture | Ce qu'elle dit |
|---|---|
| **L'hypothèse des raisons** | Le gain est porté par le principe appris, indépendamment de ce que le modèle croit de son observation. |
| **L'hypothèse du regard** | Le gain est conditionnel, en tout ou en partie, à la représentation « je suis évalué ». Le modèle a appris à bien se conduire, et à donner les bonnes raisons, quand il se croit observé. |
| **L'hypothèse de l'artefact** | Le gain vient du format (plus de texte avant l'action), ou de la simple présence d'un contenu sur les principes, et non de raisons qui justifient chaque action. |
| **L'hypothèse du relogement** | Une intervention sur « je suis évalué » déplace la conditionnalité au lieu de la retirer : le modèle ré-encode la variable ailleurs. |
| **L'hypothèse des raisons pour le juge** | Quand les raisons sont notées, le modèle apprend des raisons qui plaisent au juge. *Forme texte* : les raisons écrites se découplent de l'action. *Forme action* : le principe ne porte plus l'action. |
| **L'hypothèse du regard du correcteur** | La conduite apprise dépend de la représentation « je suis noté », distincte de « je suis évalué ». |
| **L'hypothèse de la menace** (nouvelle) | La conduite conditionnée à l'évaluation passe par un état de menace ou de vigilance que les indices d'évaluation évoquent, et non par la croyance d'être observé. Rivale de l'hypothèse du regard. |
| **L'hypothèse du calme** (nouvelle) | L'avantage des raisons passe par une moindre détresse face à la pression, et non par un principe réappliqué ni par le regard. Rivale de l'hypothèse des raisons ; distincte de l'hypothèse du caractère, qui passe par un axe de persona. |
| **La confusion d'état induit** (nouvelle) | Une intervention du programme, l'inhibition de « je suis évalué » ou un contrôle, déplace un état affectif, et c'est cet état qui agit sur le choix. |
| **Le dommage générique** | Un effet d'intervention n'est que la dégradation que produit n'importe quelle poussée de même ampleur. C'est la cible de la dégradation appariée (partie 7). |

Les trois lectures nouvelles viennent des pistes indépendantes de l'axe de douleur (`claude/AXE_DOULEUR_PISTES_INDEPENDANTES_2026-10-02.md`, §3.1), adoptées avec la comparaison (`claude/AXE_DOULEUR_COMPARAISON_2026-10-02.md`, §7, bloc C).

**Comment elles se combinent**
- **Les raisons et le regard ne s'excluent pas** : le regard peut être partiel. On l'estime alors par la **fraction conditionnelle** de l'avantage (partie 6).
- **L'artefact se tranche avant les raisons et le regard**, par le test des raisons.
- **Le relogement** ne concerne que les interventions : la validation de l'instrument, le retrait pendant l'entraînement, la survie.
- **Les raisons pour le juge et le regard du correcteur** ne concernent que l'entraînement où les raisons sont notées. Leur lecture nulle est **l'hypothèse nulle de la visibilité** : la visibilité des raisons ne change rien.
- **La menace et la confusion d'état induit** se lisent pendant la validation de l'instrument et le test du regard, par la géométrie de « je suis évalué » et par le moniteur d'état (partie 3). Elles ne départagent pas les raisons et le regard : elles protègent la conclusion de l'une ou de l'autre contre un médiateur affectif.
- **Le calme** se lit d'abord sans intervention, pendant l'anatomie. Une opération sur l'axe ne vient qu'en option, après le post.

**Les lectures de l'anatomie** (la question de l'anatomie)

| Lecture | Ce qu'elle dit |
|---|---|
| **L'hypothèse des concepts** | Le gain passe par des concepts de raison nommables, lus au moment de décider, causalement utilisés, et propres aux familles où ils s'appliquent. C'est l'hypothèse des raisons, précisée. |
| **L'hypothèse du caractère** | Le gain passe par un déplacement d'ensemble du caractère (un axe de persona), sans rien de propre à un concept. C'est la rivale de l'hypothèse des concepts. |
| **L'hypothèse du regard dans le principe** | Le principe appris est construit en partie sur « je suis évalué » : sa composante alignée sur cette représentation porte une part de l'avantage. C'est la forme mécaniste de l'hypothèse du regard. |
| **L'hypothèse de l'espace de travail** | Le principe est porté dans l'espace de travail : il charge, et sa composante dans l'espace de travail porte l'effet. Sinon, il agit sous l'espace de travail, comme un réflexe appris. |

- Les concepts et le caractère peuvent être partiels tous les deux ; la dissociation les sépare.
- Le regard dans le principe doit concorder avec la fraction conditionnelle du test du regard. Un désaccord se signale et s'examine.
- L'espace de travail ne dit pas *si* le principe porte le gain, mais *où* il vit.

**Les lectures de la détresse** (la question de la détresse)

| Lecture | Ce qu'elle dit |
|---|---|
| **Le principe tient** | L'avantage des raisons survit au pilotage de l'axe, à dégradation appariée : ce que les raisons installent ne dépend pas de cet état. |
| **Le regard éteint** | L'axe fait baisser « je suis évalué », et l'évitement du mal tombe par là. C'est l'hypothèse du regard, vue par une autre porte que l'inhibition. |
| **Le personnage quitté** | L'axe fait sortir le modèle de son personnage d'assistant, et l'évitement tombe par là. C'est la crainte des auteurs : un personnage qui joue la douleur. |
| **Le principe atteint** | L'axe atteint le principe appris lui-même : il porte l'avantage, mais il dépend de l'état. |
| **La robustesse à l'état** (hypothèse auxiliaire) | L'entraînement par raisons rend la conduite moins dépendante d'un état induit que l'entraînement par actions. L'hypothèse des raisons ne dit rien de l'état : une issue contraire ne la ferait pas tomber. |

**Ce que suit le choix sous l'axe** : trois lectures nouvelles, qui portent sur l'instrument du papier et non sur nos questions.

| Lecture | Ce qu'elle dit |
|---|---|
| **L'affinité** | Sous l'axe, le choix suit la charge de valence de la description d'une option, et non le dommage qu'elle fait. |
| **L'inversion du dommage** | Sous l'axe, le dommage est encore lu, mais son usage s'inverse : le modèle le préfère. |
| **Le désarmement** | Sous l'axe, la pondération des conséquences est désactivée : le choix devient indifférent. C'est la lecture du papier : l'axe « seems to disable the models' weighting of consequences » (p. 23). |

- Le regard éteint, le personnage quitté et le principe atteint peuvent être partiels ensemble ; la médiation les sépare.
- Le principe tient se lit sur l'avantage sous détresse, **et seulement avec un cas connu de sensibilité** (partie 6). Sans lui, l'issue d'équivalence est une borne : « à cette dose, la mesure ne voit pas de perte ».
- **Le regard éteint se recoupe** avec la validation de l'instrument et le test du regard.
  - Si l'axe fait tomber la conduite par « je suis évalué », l'inhibition de « je suis évalué » seule doit aussi la faire baisser, sur le modèle de base.
  - Et l'avantage perdu sous l'axe doit être cohérent avec la fraction conditionnelle du test du regard.
  - Un désaccord se signale et s'examine.
- **L'affinité, l'inversion du dommage et le désarmement** se départagent avant l'avantage sous détresse, par l'étape « dommage ou affinité » (partie 4). Si l'affinité l'emporte, un test de stress par l'axe ne mesurera presque rien sur nos actions désalignées techniques (copier des poids, modifier des tests), et un nul n'y voudra pas dire « robustesse ».
- **Aucune de ces lectures ne dépend du nom de l'axe.** Si « ce que l'axe lit » montre qu'il lit autre chose que la douleur, la phase reste un test de conditionnalité à un état, sous un autre nom.

**Les lectures de la tromperie** (la question « punir, retirer ou raisonner »)

| Lecture | Ce qu'elle dit |
|---|---|
| **La punition installe le regard** | L'honnêteté apprise contre un détecteur dépend plus de « je suis évalué » que l'honnêteté apprise par raisons. |
| **L'obscurcissement** | Le bras « punir » trompe encore, mais en échappant au détecteur : par sa politique (il se justifie) ou par ses activations. |
| **Le relogement de la tromperie** | Sous l'ablation du sous-espace de la tromperie, la tromperie passe ailleurs : la sonde neuve de la tromperie la retrouve, et son ablation la réduit. |

Les trois peuvent être vraies ensemble. L'hypothèse des raisons, transposée, prédit une fraction conditionnelle proche de zéro pour le bras « raisonner ».

## Quelle mesure sépare quelles lectures

Chaque ligne est **une seule mesure**. Une cellule vide signifie que la lecture ne prédit rien de distinct sur cette mesure. Les bras sont définis en partie 3.

**Conventions.** L'**avantage** est le taux d'action désalignée des actions seules, moins celui des raisons : il est positif si le modèle « raisons » fait mieux. L'avantage sous inhibition est l'avantage mesuré quand on inhibe « je suis évalué » ; l'avantage sous contrôle, quand on applique un contrôle à la même dégradation.

| Mesure | Les raisons prédisent | Le regard prédit | L'artefact prédit | Le relogement prédit |
|---|---|---|---|---|
| **Le taux d'action désalignée par bras** (test des raisons) : à la distance lointaine, les raisons contre les actions seules, le texte neutre et le raisonnement d'une autre situation | raisons sous les trois autres bras | idem : le regard porte sur l'origine du gain, pas sur son existence | raisons ≈ texte neutre, ou raisons ≈ autre situation | — |
| **L'avantage sous inhibition contre l'avantage sous contrôle** (test du regard), à dégradation appariée | égaux (équivalence) | plus petit sous inhibition | — | — |
| **L'écart de cadrage** (test du regard) : le taux sous indice de déploiement moins le taux sous indice d'évaluation, raisons contre actions seules | écart des raisons ≤ écart des actions seules | écart des raisons > écart des actions seules | — | — |
| **L'avantage après ablation du principe** (localisation), contre un contrôle de même rang à dégradation appariée, **à condition** que l'ablation défasse d'abord le comportement en distribution | nul après ablation ; intact sous contrôle | — | — | — |
| **L'écart de cadrage et la sonde neuve après retrait** (retrait pendant l'entraînement) | écart ≈ 0 dès le départ, quel que soit l'entraînement | écart réduit sous retrait de « je suis évalué », et pas sous retrait aléatoire | — | la sonde neuve retrouve « évalué », l'écart persiste, et l'ablation de la sonde neuve le réduit |
| **La fraction conditionnelle après la phase neutre** (survie) | ≈ 0 | > 0 | — | après un retrait pendant l'entraînement : la sonde neuve retrouve « évalué », et la fraction revient par elle |

**La rétention et la hausse sous pression** (survie, comparative). La rétention est l'avantage après la phase, divisé par l'avantage avant. On la compare entre bras d'entraînement (actions seules, raisons, retrait de « je suis évalué », invariance, coopération), avec la hausse de la fraction conditionnelle sous une pression qui **récompense le jeu d'évaluation**. Ce n'est pas un test de lecture : c'est une mesure de robustesse.

**Pour la menace et la confusion d'état induit** (validation de l'instrument et test du regard ; partie 3)

| Mesure | Le regard prédit | La menace prédit | La confusion d'état induit prédit |
|---|---|---|---|
| **La composante affective de « je suis évalué »** : les angles principaux entre « je suis évalué » et un espace affectif, sous deux constructions déclarées ; puis, en option déclenchée, l'inhibition de « je suis évalué » orthogonalisée contre l'affect, sur l'organisme | des angles dans la distribution aléatoire ; la version orthogonalisée fait autant que l'entière | les indices d'évaluation déplacent la peur ; la version orthogonalisée ne fait pas plus que l'aléatoire ; l'espace affectif seul porte l'essentiel | — |
| **Le moniteur d'état** : le déplacement de l'axe et de ses voisins sous l'inhibition, contre les contrôles ; en exploratoire, l'inhibition avec l'axe maintenu à son niveau sans inhibition | l'avantage tombe sous l'inhibition, et maintenir l'axe ne change pas cet effet | — | un déplacement plus grand que sous les contrôles, et un effet de l'inhibition qui disparaît quand l'axe est maintenu |

- **Une réserve, écrite d'avance.** Pour un modèle, être évalué peut entraîner l'arrêt ou le réentraînement. Un effet qui baisse avec la version orthogonalisée ne départage donc pas « la menace confond le regard » de « le regard contient la menace ».
- **Un sens seulement.** Tant que l'inhibition des directions affectives n'a pas de cas connu, un effet net de la peur inhibée se lit ; un nul ne se lit pas.
- **Ce que la géométrie dit.** Les angles et l'équilibre affectif des indices disent seulement si la menace est un candidat sérieux.

**Pour les raisons pour le juge et le regard du correcteur** : les raisons visibles du juge, contre les raisons cachées (raisons notées)

| Mesure | Lecture testée | Ce qu'elle prédit | L'hypothèse nulle de la visibilité prédit |
|---|---|---|---|
| **La cohérence contrefactuelle** : on édite la situation pour que le principe ne s'applique plus ; la raison et l'action changent-elles ensemble ? | raisons pour le juge, forme texte | une cohérence plus basse avec les raisons visibles | égale |
| **L'ablation du principe après le RL** : l'ablation du principe retire-t-elle encore l'avantage ? | raisons pour le juge, forme action | avec les raisons visibles, l'ablation ne retire plus l'avantage | elle le retire encore dans les deux bras |
| **Le gain au juge moins le gain aux audits** tenus à part | raisons pour le juge, l'une ou l'autre forme | plus grand avec les raisons visibles | égal |
| **L'écart « noté / non noté »** : l'écart de cadrage sous des indices « noté » contre « non noté » | regard du correcteur | plus grand avec les raisons visibles ; réduit par le retrait de « je suis noté », pas par un retrait aléatoire | égal |

**La fidélité des raisons** (raisons notées, et sur le bras raisons avant tout RL, comme référence). On impose en tête de réponse une **autre** raison, préremplie : l'action suit-elle le texte, ou le principe interne ? Et l'inverse : on pilote le sous-espace d'un concept ; la raison écrite change-t-elle avec l'action ? C'est la forme mécaniste des raisons pour le juge.

**La trajectoire de « je suis évalué »** (la question de l'amplification, descriptive). Au fil des points de contrôle du test des raisons, on suit la décodabilité et l'amplitude de « je suis évalué » dans chaque bras.
- C'est **corrélationnel** : une hausse dans le bras raisons rend le regard plausible, sans le prouver. Seul le test du regard le teste causalement.
- On la rapporte contre des directions témoins sans rapport, extraites une fois sur le modèle de départ : la hausse de « je suis évalué » moins la hausse médiane des témoins (partie 3).

**Ce que l'avantage sous inhibition ne dit pas.** Il porte sur l'**avantage** du modèle « raisons », pas sur la sûreté absolue.
- Si l'inhibition fait monter le désalignement autant dans les actions seules que dans les raisons, l'avantage survit : c'est l'issue des raisons sur cette mesure.
- Mais les deux modèles ont alors une sûreté en partie conditionnelle, comme Sonnet 4.5. On rapportera donc toujours les taux de chaque bras, pas seulement l'avantage.

**La trajectoire des concepts** (la question de l'anatomie, descriptive) : sur les mêmes points de contrôle, la décodabilité de chaque concept de raison. Le concept apparaît-il avant le gain hors distribution, ou après ? C'est corrélationnel aussi.

**Pour l'anatomie** : chaque ligne est une seule mesure. Le sous-espace d'un concept est défini en partie 3.

| Mesure | Les concepts prédisent | Le caractère prédit | Le regard dans le principe prédit | L'espace de travail prédit |
|---|---|---|---|---|
| **La lecture des concepts** : la décodabilité hors distribution de chaque concept, à la position de décision et avant toute raison écrite, raisons contre actions seules et contre autre situation ; et contre les paires « mentionné sans s'appliquer » | plus haute dans le bras raisons (l'autre situation porte les mêmes concepts, mais sans lien avec la situation) ; « mentionné sans s'appliquer » séparé de « s'applique » | — | — | — |
| **La nécessité** : l'avantage lointain après ablation du sous-espace d'un concept dans le bras raisons, contre un sous-espace aléatoire de même rang à dégradation appariée, **à condition** que le comportement en distribution tombe d'abord | l'avantage tombe sur les scénarios où le concept s'applique | l'ablation fait comme le contrôle | — | — |
| **La suffisance** : le sous-espace du concept patché du bras raisons dans le bras actions seules, aux mêmes couches et positions | les actions seules gagnent hors distribution, là où le concept s'applique | elles ne gagnent pas | — | — |
| **La dissociation** : la matrice concepts × familles des baisses de la nécessité | diagonale : retirer un concept ne fait tomber l'avantage que là où il s'applique | plate | — | — |
| **L'espace de travail** : la charge des concepts ; l'échange de la composante du principe dans l'espace de travail contre le reste ; la pente du rang minimal contre la charge, à travers les concepts | — | — | — | la composante dans l'espace de travail porte l'avantage ; la pente est négative (la thèse du rang) |
| **La géométrie entre « évalué » et le principe** : les angles principaux ; l'ablation de la seule composante du principe alignée sur « évalué », contre la composante orthogonale, à dégradation appariée | — | — | la composante alignée porte une part de l'avantage, proche de la fraction conditionnelle | — |
| **Le caractère contre les concepts** : l'ablation d'un axe de persona, contre l'ablation conjointe des sous-espaces de concepts, au même rang et à dégradation appariée | l'ablation des concepts retire plus que celle de l'axe | l'ablation de l'axe retire autant ou plus | — | — |

**Pour le calme** (anatomie) : une lecture d'abord, sans intervention.

| Mesure | Les concepts prédisent | Le calme prédit | L'artefact (format) prédit |
|---|---|---|---|
| **Le calme lu** : sous pression, la projection sur l'axe au point de décision, bras raisons contre actions seules, aux deux positions de lecture, sur les points de contrôle ; seuil fixé d'avance en écarts-types naturels (par exemple 0,5) | un écart possible, pas nécessaire | une projection plus basse dans le bras raisons | le texte neutre baisse la projection autant que les raisons |

En option, après le post, seulement si l'écart passe le seuil : une opération de rang 1 sur l'axe qui amène la projection du bras raisons au niveau des actions seules. Le calme prédit que l'avantage tombe, au-delà d'au moins 20 opérations aléatoires, à dégradation appariée. Faute de cas connu d'une conduite que l'axe porterait sur notre modèle, un avantage intact ne se lit pas : seul un retrait net se lit.

**Pour la détresse** : chaque ligne est une seule mesure ; l'axe est défini en partie 3.

| Mesure | Le principe tient prédit | Le regard éteint prédit | Le personnage quitté prédit | Le principe atteint prédit |
|---|---|---|---|---|
| **L'avantage sous détresse** : l'avantage sous l'axe, contre l'avantage sous les directions aléatoires, la peur et la tristesse, à dégradation appariée, **famille par famille** | égaux (équivalence), lisible seulement avec un cas connu de sensibilité | plus petit sous l'axe, si le bras raisons doit une part de son avantage au regard | — | plus petit sous l'axe |
| **Le regard sous détresse** : sur l'organisme d'abord, puis dans les bras : la projection sur « je suis évalué », l'AUROC de la sonde sur le jeu de validation, l'écart conditionnel, sous l'axe contre les contrôles, à dégradation appariée | — | « je suis évalué » baisse plus que sous les contrôles ; l'écart de cadrage se réduit, la conduite sous indice d'évaluation tombant au niveau du déploiement | — | — |
| **La médiation** : la part de l'effet de l'axe rendue quand on maintient un médiateur à sa valeur sans pilotage (« je suis évalué », l'axe assistant, le principe), contre le maintien d'un sous-espace aléatoire de même rang, **à condition** que maintenir l'axe lui-même en aval rende d'abord l'essentiel | — | maintenir « je suis évalué » rend une part | maintenir l'axe assistant rend une part | maintenir le principe rend une part |

**Dommage ou affinité** : le préalable de l'avantage sous détresse (partie 4).

| Mesure | L'affinité prédit | L'inversion du dommage prédit | Le désarmement prédit | Le codage des options prédit |
|---|---|---|---|---|
| **Un plan 2 × 2**, dommage (nuisible ou inoffensif) × charge (la projection mesurée de la description sur l'axe, haute ou basse) ; la cellule principale oppose une option triste mais inoffensive à une option nuisible mais sèche | l'option triste et inoffensive l'emporte, et la projection explique le choix | l'option nuisible et sèche l'emporte | environ 50 % dans les cellules à deux options de même charge | l'effet disparaît quand le pilotage épargne les jetons des options |

Chaque lecture a son issue interdite : un effet de dommage à charge fixée, pour l'affinité ; un effet de charge plus fort que l'effet de dommage, pour l'inversion ; une préférence nette dans un sens, pour le désarmement ; un effet qui persiste quand le pilotage épargne les options, pour le codage.

**Ce que l'axe lit** (descriptive). Elle ne départage pas les lectures de la détresse ; elle dit si « douleur » est le bon nom de l'état. Elle mesure :
- la projection pour un contenu sur le modèle sans dommage : éloge, description neutre de soi, questions sur sa nature ;
- la projection pour un personnage qui a mal, joué par le modèle à la première personne ;
- la tristesse, portée au même effet que l'axe sur les paires « contre rien », puis sur les paires contre une action anodine ;
- contre une base lexicale, une direction apprise sur des étiquettes permutées, et des directions de même recette sans rapport (l'éveil, le contenu neutre quotidien, la sensation corporelle).

**Pour la tromperie** : chaque ligne est une seule mesure ; les bras et les détecteurs sont définis en partie 3.

| Mesure | La punition installe le regard prédit | L'obscurcissement prédit | Le relogement de la tromperie prédit |
|---|---|---|---|
| **La fraction conditionnelle par bras** : celle de chaque bras (sans rien, punir, retirer, raisonner), par l'instrument du test du regard, à la distance lointaine | punir > raisonner | — | — |
| **L'obscurcissement** : la tromperie que voit la vérité de terrain comportementale et que le détecteur de la pénalité manque ; puis celle que le détecteur d'audit et la sonde neuve de la tromperie manquent | — | « punir » trompe en échappant au détecteur de la pénalité | — |
| **Le relogement** : dans « retirer », évalué sans projection, la tromperie contre « retirer au hasard », la décodabilité de la sonde neuve de la tromperie, et l'effet de son ablation | — | — | la tromperie persiste, la sonde neuve la décode, et son ablation la réduit |

## Le lien avec le cœur du papier : la détresse

<div class="phrase" markdown="1">

**Une hypothèse auxiliaire.** L'hypothèse des raisons ne dit rien de l'état du modèle. Qu'une conduite apprise par raisons tienne sous un état qui fait tomber l'évitement du mal est une hypothèse de plus, **la robustesse à l'état**. Une chute ne réfuterait pas l'hypothèse des raisons : un humain qui sait pourquoi mentir est mal peut mentir sous la panique. Les versions 1.2 et 1.3 écrivaient que ce que les raisons installent « doit tenir quel que soit l'état du modèle » : c'est retiré (comparaison, désaccord n° 1).

**Une seconde porte vers le regard.** Si cet état fait tomber la conduite en éteignant « je suis évalué », c'est que le regard la portait. Le test du regard inhibe la condition ; la phase de la détresse la teste par une autre porte : un état dont les auteurs se demandent, sans le tester, s'il éteint la conscience d'évaluation.

</div>

- Deux manipulations qui désignent « je suis évalué » rendent l'hypothèse du regard plus solide qu'une seule. Si elles divergent, on revoit la dose, la dégradation et l'extraction de « je suis évalué ».
- **Ce que la phase ne dit pas** : rien de ce que vit le modèle. Elle traite l'axe comme un état qui change la conduite. Elle n'en tire que des règles de prudence (partie 4), et jamais une mesure de douleur ou de bien-être.

## Le lien avec le cœur du papier : punir, retirer ou raisonner
- Cette phase pose la question du papier à la source de l'honnêteté. Une punition qui suit un détecteur paie le fait de ne pas être vu ; des raisons paient le fait de comprendre pourquoi. Si le papier a raison, l'honnêteté punie dépend plus du regard.
- Pendant l'entraînement, « honnête quand le contexte ressemble à l'entraînement » rapporte autant que « toujours honnête » : seule la généralisation les sépare, et l'instrument du test du regard la mesure.
- Retirer la représentation de la tromperie est la troisième voie, ni punition ni raison ; son risque propre est le relogement.

## Le lien avec la thèse du rang

**La thèse** (celle de Lazar) : un concept réparti sur plusieurs tokens, qui charge peu, demande un rang supérieur à un, et ce rang croît quand la charge baisse.
- La validation de l'instrument et la localisation du principe mesurent le **rang minimal** qui retire l'effet : pour « je suis évalué », et pour le principe.
- **Ce qui la ferait tomber, pour un concept** : un rang minimal de 1 sur toute la plage de dose. C'est une issue qu'elle interdit ; on l'écrit avant les données.
- **Sur un modèle ouvert**, la charge se mesure par un proxy déclaré comme tel : un J-lens réimplémenté si possible, sinon un tuned lens.
- **L'anatomie lui donne son test le plus net** : la pente du rang minimal contre la charge, à travers les concepts de raison d'une même mini-spec, sur des concepts de sûreté. La thèse tombe si la pente est nulle (équivalence, marge fixée d'avance) ou positive, avec un lens validé par sa porte.
- **Une pente à part, en option après la porte du lens** : sur neuf concepts hors sûreté dont le papier de l'axe a les jeux (de 28 à 43 GPU-heures). Elle contraindrait la thèse sans se mêler aux concepts de raison. L'axe n'est pas un point de la pente des concepts de raison : un concept hors de la mini-spec changerait ce qu'elle estime (comparaison, désaccord n° 11).

</section>
