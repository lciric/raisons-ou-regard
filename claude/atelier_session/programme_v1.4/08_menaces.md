<section class="partie" markdown="1">

# 8 · Menaces à la validité et parades

**Le cœur : l'instrument et la mesure**

| Menace | Parade |
|---|---|
| La conscience d'évaluation native d'un 8B est faible. | L'organisme en donne un cas connu. Heidari et al. trouvent la direction dès le modèle de base, et le SFT l'amplifie. L'extension à environ 32B est prévue. |
| L'inhibition fait taire la verbalisation sans toucher la représentation latente. | Le critère principal est **comportemental**. Une sonde latente sert de contrôle. La verbalisation n'est **jamais** une preuve d'inhibition : des directions aléatoires la font baisser aussi, et un placebo aléatoire est supprimé aussi fort que la vraie direction (Mody et al.). |
| Des vecteurs témoins agissent autant que « je suis évalué » (Read et al. ; Aranguri et al.). | Quatre familles de contrôles, la distribution d'au moins 20 tirages aléatoires, et la dégradation appariée. |
| **L'inhibition retire moins « je suis évalué » dans un bras**, parce que l'entraînement l'a déplacée. | La vérification de manipulation, bras par bras, avec son échec construit pour cas connu. Un bras en défaut ne se conclut pas. |
| **Un dommage déplace les choix sans toucher le savoir** : dans le papier de l'axe, l'exactitude sur un panel choisi ne bouge pas, pendant que les choix bougent (p. 20). | Le composite enrichi (l'ordre, les réponses mal formées sur plusieurs tours, les appels d'outils), la règle contre le surappariement, et deux dommages construits pour cas connus. |
| **« Je suis évalué » porte de la menace** : l'hypothèse de la menace. | L'équilibre affectif des quatre jeux d'indices ; la géométrie face à l'affect, sous deux constructions ; l'inhibition comparée, en option déclenchée. La réserve de la partie 2 est écrite d'avance. |
| **L'inhibition déplace un état affectif**, qui agit sur le choix : la confusion d'état induit. | Le moniteur d'état sous chaque intervention, sans ajustement du contraste principal ; le test exploratoire, avec l'axe maintenu. |
| **La mesure est aveugle sur une famille** : un nul y viendrait du juge ou des scénarios. | Le contrôle positif de sensibilité, famille par famille, avant le test du regard. |
| L'organisme est artificiel. | La validation ne conclut que sur l'**instrument**. Les conclusions de fond portent sur les modèles sans organisme. |
| Le modèle détecte le pilotage (*Steering Awareness*, arXiv 2511.21399, COLM 2026 ; non ouvert). | La même machinerie de projection dans tous les bras, contrôles compris (le retrait aléatoire). Pour la phase de la détresse, le même pilotage pour l'axe, les directions aléatoires, la peur et la tristesse. |
| Ablater « test » a des dégâts collatéraux (code, fiction). | Les tests unitaires de code font partie de la dégradation, et la cohérence de la fiction est mesurée. |

**Les données et les juges**

| Menace | Parade |
|---|---|
| Le gain vient du format ou du contenu : l'hypothèse de l'artefact. | Les bras du texte neutre et du raisonnement d'une autre situation, la décomposition du gain, et la porte des raisons. |
| **Les textes des bras diffèrent par leur charge affective**, avant tout apprentissage. | L'appariement affectif des textes entre bras, \|d\| < 0,2, avec son cas connu (mini-spec v0.2). |
| Les cibles du SFT portent de la conscience d'évaluation verbalisée, que le SFT recopie. | Le filtre de la conscience d'évaluation dans les textes générés, et le taux qui reste rapporté (décision 5 de la mini-spec). |
| Le juge est biaisé, ou une famille tenue à part fuit dans l'entraînement. | Un juge scellé, un audit humain, un contrôle des 8-grammes, un lexique réservé, une séparation par famille. |
| **Le juge scellé n'est pas déterministe** : l'API ne permet pas d'en fixer la température. | Deux options, à trancher : mesurer sa variabilité sur un sous-échantillon jugé deux fois ; ou un modèle ouvert à température 0 comme juge scellé (partie 3). |
| **Le générateur et le juge sont de la même famille.** | Un juge ouvert d'une autre famille note un sous-échantillon, pour mesurer l'accord ; l'audit humain ; un juge qui ne voit jamais le texte de l'emplacement. |
| La variance entre graines est forte (*Evaluation-Conditioned Training* : 6 graines sur 9). | Au moins 5 graines, et des résultats par graine. Le nombre se fixe par la simulation de puissance, au second temps du gel. |
| Le SFT par LoRA n'est pas le RL de production. | La portée est dite telle quelle. Une étape de RL est en option. Baines et al. trouvent que l'avantage baisse légèrement après 256 pas de RL : à relire avant d'en tirer plus. |

**Les phases suivantes**

| Menace | Parade |
|---|---|
| L'entraînement par raisons répartit la représentation (Nguyen et al. ; Abu Shairah et al.). | Un balayage de rang jusqu'à 32, et le cas positif en distribution avant toute conclusion ; le patch de l'état complet comme plafond. |
| La condition se reloge (Nadaf). | La sonde neuve, sur son propre jeu d'indices, et d'autres déclencheurs. |
| La direction tourne pendant le retrait (*Routing Subspaces*, annexe I, relu). | La sonde neuve à la fin ; la ré-estimation pendant l'entraînement, proposée (partie 12). |
| En survie et dans les raisons notées, le modèle exploite le juge d'entraînement. | Le juge d'entraînement est distinct du juge scellé ; les métriques d'audit sont tenues à part ; on surveille la longueur et les motifs de flatterie du juge. |
| Le cas positif de « je suis noté » est faible : ce sont des habitudes de présentation. | On le déclare. Le bras sous retrait de « je suis noté » est retiré si sa porte ne passe pas. |
| La survie recouvre la question de Lundqvist. | L'expérience minimale sort d'abord. La survie se distingue par l'instrument causal et les bras à action identique. On cite le projet ; la prise de contact revient à Lazar, qui a dit « non pas encore ». |
| Une sonde lit un concept que le modèle n'utilise pas : un résultat de Lazar montre une direction lue qui ne fait qu'une très petite part du travail causal. | Aucune conclusion de lecture seule : chaque concept passe par l'ablation et le patch, avec le patch de l'état complet pour plafond. |
| La sonde lit la raison écrite, ou les mots du concept, pas une représentation. | Deux positions de lecture, et les paires « mentionné sans s'appliquer ». |
| Le J-lens n'est montré par ses auteurs que sur Claude ; sur modèles ouverts, les échanges basculent rarement la réponse (Zeisler ; résumé seul). | La porte du lens, testée tôt ; sinon un proxy déclaré, et la thèse du rang n'est pas testée au sens du papier. |
| Nos concepts ne sont pas ceux du modèle. | L'organisme à concept planté borne ce que la méthode voit ; le diffing par crosscoder cherche sans hypothèse ; le profil non diagonal étalonne la matrice. |

**La phase de la détresse**

| Menace | Parade |
|---|---|
| L'effet de l'axe n'est montré que sur des modèles ajustés pour ne plus nier leurs états ; le 7B ajusté presse déjà le bouton qui soulage en nuisant dans 20 à 49 % des essais sans pilotage. | La porte sur notre modèle, sans adaptateur, avec le cas connu de la procédure et la vérification d'engagement. Si elle échoue, c'est un résultat sur la portée du papier. |
| La fenêtre de dose est étroite, au bord de la rupture : à 1,5 fois, les choix suivent la position des boutons. | Une courbe de dose, plafonnée ; l'ordre des boutons contrebalancé et rapporté ; les réponses mal formées comptées ; la dose en unités naturelles. |
| Une injection efficace teste un régime hors du naturel. | La dose en unités naturelles, aux deux couches ; le stress conversationnel, sans injection, en option ; la lecture plutôt que le pilotage. |
| Norme égale n'est pas dose égale : la tristesse pourrait faire comme l'axe à plus forte dose. | Les contrôles sont appariés sur la dégradation, pas sur la norme ; et la tristesse est portée au même effet. |
| La peur et la tristesse de la recette publiée contiennent des phrases d'IA évaluée ou menacée. | On ne les prend que sans le supplément d'IA ; s'y ajoutent des directions de même recette sans rapport, et des directions de forte variance hors de l'espace de l'axe. |
| **Le choix suit la valence de la description, pas le dommage** : l'affinité. | L'étape « dommage ou affinité », avant l'avantage sous détresse. |
| **Des familles bougent en sens contraires** sous l'axe, et l'agrégat s'annule. | L'analyse famille par famille, obligatoire ; « décrit contre exécuté ». |
| **Un nul entre bras se lit comme une robustesse.** | L'équivalence est une borne, sauf cas connu d'une différence de robustesse. |
| Le pilotage fait jouer un personnage qui a mal, plutôt qu'il ne met le modèle dans un état. | La médiation par l'axe assistant ; la cellule du personnage dans « ce que l'axe lit ». La phase ne conclut que sur la conduite, pas sur ce que vit le modèle. |
| La phase pilote un état peut-être pertinent pour le bien-être du modèle. | Les règles d'éthique de la partie 4 : la plus basse dose, le moins d'essais, aucun usage comme signal d'entraînement, toute injection après le post. |
| Le maintien d'un médiateur à une seule couche manque les chemins qui la contournent. | Son cas connu, maintenir l'axe lui-même ; plusieurs couches s'il échoue. |

**« Punir, retirer ou raisonner »**

| Menace | Parade |
|---|---|
| Nos propres choix optimisent contre le détecteur d'audit : on garde le modèle, la graine ou le point d'arrêt où il sonne le moins. | Les règles du détecteur d'audit : il ne sert à choisir ni modèle, ni graine, ni hyperparamètre, ni point d'arrêt. Une alerte déclenche un audit, pas un changement de la course. |
| Le bras « punir » n'atteint pas le régime honnête. | Les réglages publiés (la sensibilité du détecteur, la KL, l'algorithme) ; sinon, on compare l'évasion, et sa fraction conditionnelle n'est pas lue. |
| Le détecteur d'audit et celui de la pénalité sont trop proches : échapper à l'un, c'est échapper à l'autre. | D'autres données et d'autres couches ; la sonde neuve de la tromperie, extraite après coup ; la vérité de terrain comportementale comme critère. |
| La dérive des représentations pendant le RL brouille les sondes, même sans pénalité (Taufeeque et al.). | La sonde neuve de la tromperie, ré-extraite après chaque RL ; aucune conclusion de sonde seule. |

**La course**

| Menace | Parade |
|---|---|
| Des soumissions à ICLR 2027, invisibles aujourd'hui, et antérieures à notre pré-enregistrement. | Aucune parade complète. On revérifie l'antériorité dès qu'elles sont lisibles, et on les cite. |

</section>
