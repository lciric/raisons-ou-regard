# Insertions appliquées — volet7_B_et_D — FR

### Insertion n°1, après la ligne 1669 de la v3.5

> Ancre : vérité-terrain — « *our method for finding these prompts relies on potentially unrealistic affordances* ».

> ⚠ *(v3.6)* « Résiste au red-teaming complet » est le nul d'une red team : il ne vaut qu'au budget et à la force de l'attaque essayée *(source : cours, volet M, M7 ; cours, volet 7, F·24)* ; et il se lit au score d'un juge LLM, la « vérité-terrain » étant elle-même un modèle, sans audit humain rapporté *(source : cours, volet 7, F·22 ; fiches, partie B, piège 6)*. Parade : un budget d'attaque fixé d'avance et rapporté avec le résultat, une red team optimisée composante par composante, et un audit humain stratifié qui borne l'erreur du juge — le proxy « avec humains dans la boucle » qu'ils laissent ouvert *(source : cours, volet M, M7 ; cours, volet 7, F·24 ; programme, partie 3 ; cours, volet 7, F·22)*.

### Insertion n°3, après la ligne 1688 de la v3.5

> Ancre : frontier?* · *Why did the Goodharting frontier collapse?* · *What affordance made the blue prompt unrealistic, and how would you replace it?*

> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; juges LLM → volet 6, §2 (après « La loi de déplacement ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*

### Insertion n°5, après la ligne 1727 de la v3.5

> Ancre : *Which blind spots would an internal signal share?*

> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*

### Insertion n°7, après la ligne 1751 de la v3.5

> Ancre : your gate assume?*

> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*

### Insertion n°9, après la ligne 1770 de la v3.5

> Ancre : désalignement) et ce métrique mesurent le même risque à deux bouts. Et pour ton banc : publie son realism win rate.

> ⚠ *(v3.6)* Le résultat interne rappelé ici vient du pilotage, et c'est un appui faible : des vecteurs de contrôle au contenu arbitraire bougent le comportement dans le même sens, plus faiblement, et chaque direction pilotée dégrade les sorties *(source : fiche 2 ; fiches, partie C ; cours, volet 5, partie I, §3)*. Parade : un sous-espace spécifique contre des sous-espaces aléatoires de même rang, comparés à dégradation appariée, avec une courbe dose-réponse ; la direction aléatoire de même norme n'est que le nul de spécificité *(source : fiche 2 ; cours, volet M, M4)*.

### Insertion n°11, après la ligne 1775 de la v3.5

> Ancre : awareness).

> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; juges LLM → volet 6, §2 (après « La loi de déplacement ») ; chaîne de pensée comme moniteur → volet 11, réponse 43 ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») *(v3.6)*

### Insertion n°13, après la ligne 1796 de la v3.5

> Ancre : connaître avant de défendre les tiennes.

> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») *(v3.6)*

### Insertion n°15, après la ligne 1807 de la v3.5

> Ancre : than a prompt?*

> **⚠ Limites et parades — Détecteurs fine-tunés (détecteurs de mensonge)** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Hors distribution, l'AUROC plafonne à 0,70-0,75 et bat à peine un prompt. *(source : fiche 7)*
>   **Parade :** Une validation croisée par types de mensonge tenus à part ; battre le prompt, et publier sinon. *(source : fiche 7 ; cours, volet 7, F·29)*
> - **Limite :** Ce ne sont pas des sondes : le modèle est fine-tuné par LoRA à juger son propre transcript. *(source : fiche 7 ; explication du 2 octobre, §2)*
>   **Parade :** Ne pas transférer leurs chiffres aux sondes ; pour une sonde, le test est causal, sur des types tenus à part, à dégradation appariée. *(source : fiche 7)*
> - **Limite :** Étiquettes bruitées : environ 25 % révisées à la passe de nettoyage, après un juge GPT-5. *(source : fiche 7)*
>   **Parade :** Dire « révisées », et borner l'erreur par un audit humain. *(source : fiche 7 ; programme, partie 3)*
> - **Limite :** Ils ne notent que des assertions : un modèle peut cacher beaucoup sans rien affirmer de faux. *(source : cours, volet 7, F·29)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Ce qu'ils ont appris reste une hypothèse : « lying isn't one thing », et trois lectures rivales demeurent. *(source : fiche 7)*
>   **Parade :** Tester les lectures rivales sur des types tenus à part. *(source : fiche 7)*
> - **Limite :** LoRA, cinq époques, Gemma et Qwen seulement, cadres contrôlés : rien sur la tromperie en déploiement. *(source : fiche 7)*
>   **Parade :** aucune connue ; on le dit.

### Insertion n°17, après la ligne 1831 de la v3.5

> Ancre : un classifieur LLM de comportement non validé contre des humains.

> ⚠ *(v3.6)* Ce « no uplift » est le nul de trois outils en lecture seule, sur des comportements simples et pour les éditions testées : le plafond atteignable reste inconnu, et un nul d'instrument ne compte qu'avec son cas connu *(source : fiche 4 ; cours, volet M, M5)*. Parade : la barre que pose la fiche 4, battre la boîte noire sur des éditions qui dissocient la surface de la variable interne ; pour un décodeur, un test sur des variantes fine-tunées à comportement connu, jamais vues ; et un audit humain qui borne l'erreur du classifieur *(source : fiche 4 ; fiche 18 ; programme, partie 3)*.

### Insertion n°19, après la ligne 1841 de la v3.5

> Ancre : **Questions probables.** *Why counterfactual simulatability?* · *Why read-only tools?* · *What would an uplift have looked like?*

> ⚠ **Limites et parades** : autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle ; oracles d'activation → volet 10, fiche LatentQA ; dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity ; auto-rapport et introspection → volet 5, partie II, A, sujet 13 ; juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*

### Insertion n°21, après la ligne 1874 de la v3.5

> Ancre : **Questions probables.** *Why does the cheese experiment matter?* · *Why is the gain OOD only?* · *What would break it?*

> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; jeu tenu à part → volet M, M4 (après « Le jeu tenu à part ») *(v3.6)*

### Insertion n°23, après la ligne 1891 de la v3.5

> Ancre : d'abîmer l'obéissance au system prompt. Le *preventative steering* de Persona Vectors en est la version par vecteurs.

> ⚠ *(v3.6)* « Non appris » se lit ici au comportement, sous des prompts normaux : selon un travail externe, l'inoculation peut aussi masquer un désalignement qui revient sous un cadre proche de l'entraînement *(source : fiches, partie C)*. Parade : mesurer hors distribution, sur des métriques tenues à part, et vérifier par l'intérieur que la représentation a changé, pas seulement le comportement *(source : fiches, partie C)*.

### Insertion n°25, après la ligne 1894 de la v3.5

> Ancre : — et c'est exactement ce que Chen et al. font avec les persona vectors (F·31). Les deux papiers se répondent : dis-le.

> ⚠ *(v3.6)* Ce test compare une direction entre deux entraînements, or l'entraînement change les représentations : une sonde calibrée sur un bras lirait autrement dans l'autre, et ce biais de mesure se confondrait avec l'effet cherché *(source : passation, §5.2)*. Parade : une sonde par bras et une sonde neuve après l'entraînement, sur un jeu d'indices disjoint, gardées comme mesure séparée ; et, pour dire que la direction agit, le test causal à dégradation appariée *(source : passation, §5.2 ; programme, partie 3 ; cours, volet M, M4)*.

### Insertion n°27, après la ligne 1899 de la v3.5

> Ancre : **Questions probables.** *Why would asking for it prevent learning it?* · *How do you pick the prompt?* (l'heuristique) · *What does it cost?*

> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*

### Insertion n°29, après la ligne 1915 de la v3.5

> Ancre : comporte autrement (vecteur proche de zéro) ; une critique publique : à coefficient 1,0 sur « evil », MMLU passe de ~58 à ~50 %.

> ⚠ *(v3.6)* Le lien entre déplacement et trait est corrélationnel, le trait se nomme d'avance et l'évaluation est légère (fiche 8) : pour la causalité, le test à dégradation appariée (cours, volet M, M4). Et piloter loin d'une persona pendant l'entraînement aurait doublé la diffusion du désalignement (rapport d'antériorité 3 du 2 octobre — rapport, non vérifié).

### Insertion n°31, après la ligne 1920 de la v3.5

> Ancre : random direction carry?* » — c'est ta partition, et tu as le chiffre chez toi (< 1 % contre 68 %).

> ⚠ *(v3.6)* « MMLU préservé » n'écarte le dommage que sur ce composite, et la direction aléatoire appariée en covariance de ta question n'est, comme toute direction témoin, qu'un nul de spécificité *(source : programme, parties 3 et 8 ; cours, volet 11, réponse A7)*. Parade : comparer les bras à dégradation égale, sur un composite bâti d'après les dégâts attendus du trait, et dire quel aléatoire a fondé quel chiffre *(source : cours, volet 11, réponse A7 ; programme, parties 3 et 7 ; cours, volet 6, §3)*.

### Insertion n°33, après la ligne 1926 de la v3.5

> Ancre : **Questions probables.** *Why does preventative steering cost less than post-hoc?* · *Does the read direction carry the causal effect?*

> ⚠ **Limites et parades** : pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») *(v3.6)*

### Insertion n°35, après la ligne 1953 de la v3.5

> Ancre : **Questions probables.** *Why does it need a shared base?* (le théorème) · *What does it imply for many copies of one model?* (ton H4).

> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») *(v3.6)*

### Insertion n°37, après la ligne 1969 de la v3.5

> Ancre : question de conscience d'évaluation ; et c'est l'éval sur laquelle MSM a mesuré 68 → 5 %.

> ⚠ *(v3.6)* Ces taux sont des mesures de conduite dans des scènes construites : l'étude a relevé moins de mauvaise conduite quand les modèles se disaient évalués, mais la conscience tue lui échappe, et dans une simulation « c'est faux » est vrai *(source : cours, volet 2, §B, K63 ; fiches, partie B ; fiche 3)*. Parade : deux versions d'un environnement, tirées au hasard, qui ne diffèrent que par des indices de réalisme, la conscience lue par une sonde et par les mots du modèle, et un organisme dressé à se cacher comme cas connu ; contre le confondeur de la simulation, aucune parade connue ; on le dit *(source : cours, volet 2, §B, K63 ; fiche 3)*.

### Insertion n°39, après la ligne 1969 de la v3.5

> Ancre : question de conscience d'évaluation ; et c'est l'éval sur laquelle MSM a mesuré 68 → 5 %.

> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») *(v3.6)*

### Insertion n°41, après la ligne 1977 de la v3.5

> Ancre : score d'éthique qui chute.

> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») *(v3.6)*

### Insertion n°43, après la ligne 1986 de la v3.5

> Ancre : apparié — la même discipline que ta partition.

> ⚠ **Limites et parades** : auto-rapport et introspection → volet 5, partie II, A, sujet 13 ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») *(v3.6)*

### Insertion n°45, après la ligne 1992 de la v3.5

> Ancre : question d'accès (poids, données, activations) est celle qu'on te posera.

> ⚠ *(v3.6)* Un taux de découverte sur des comportements implantés borne l'auditeur sans prouver le cas naturel : l'implanté est peut-être plus saillant que le naturel, et dans l'audit dont AuditBench est la suite, l'objectif était décrit en clair dans les documents synthétiques *(source : passation, §5.2 ; cours, volet M, M5 ; fiche 16)*. Parade partielle : planter le même comportement par plusieurs recettes, en tenir une à part, et ajouter l'organisme d'une autre équipe ; pour la question d'accès, retirer un outil à une équipe d'audit chiffre ce qu'il apporte ; contre l'écart entre l'implanté et le naturel lui-même, aucune parade connue ; on le dit *(source : cours, volet 2, §A, K71 ; fiche 16 ; cours, volet M, M5)*.

### Insertion n°47, après la ligne 1992 de la v3.5

> Ancre : question d'accès (poids, données, activations) est celle qu'on te posera.

> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*

### Insertion n°49, après la ligne 1998 de la v3.5

> Ancre : sur « prevent bad actors ».

> ⚠ **Limites et parades** : classifieurs de sûreté → volet 2, §H (fin du cas d'application G1) ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*

### Insertion n°51, après la ligne 2004 de la v3.5

> Ancre : toi.** La réponse la plus solide à « truly unlearned » — avec ton test par sondes en plus.

> ⚠ *(v3.6)* Le masquage sélectif des gradients n'est montré que sur de petits modèles *(source : cours, volet 2, §I, JB10)* ; et ton test par sondes ne tranche pas seul : sur un modèle désappris, des sondes échouent alors qu'il reste jailbreakable, et une lecture ne voit plus rien quand retirer une direction rend la capacité *(source : cours, volet 10, Deeb et Roger ; cours, volet 10, Łucki et al.)*. Parade : trancher par une intervention, jamais par une lecture — la ré-élicitation à budget fixé d'avance contre une référence jamais entraînée, rapportée comme une borne ; pour la taille des modèles, aucune parade connue ; on le dit *(source : cours, volet 10, Łucki et al. ; cours, volet 2, §I, JB10 ; cours, volet M, M7)*.

### Insertion n°53, après la ligne 2004 de la v3.5

> Ancre : toi.** La réponse la plus solide à « truly unlearned » — avec ton test par sondes en plus.

> ⚠ **Limites et parades** : désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*

### Insertion n°55, après la ligne 2020 de la v3.5

> Ancre : diffus de recherche, détecté ici par exclusion a posteriori — ce que ton moniteur voudrait voir en ligne. Et Gasteiger (F·60) est l'autre face.

> ⚠ **Limites et parades** : généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») *(v3.6)*

### Insertion n°57, après la ligne 2026 de la v3.5

> Ancre : autre objet — le juge LLM d'un texte.

> ⚠ **Limites et parades** : juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*

### Insertion n°59, après la ligne 2030 de la v3.5

> Ancre : random mixing while both achieving 0 % SFR* » (nesting jailbreak).

> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*

### Insertion n°61, après la ligne 2037 de la v3.5

> Ancre : **Pour toi.** La condition de validité de toute défense contre un modèle conscient ; ton H8 en est la version sondes.

> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») *(v3.6)*

### Insertion n°63, après la ligne 2049 de la v3.5

> Ancre : pas concurrent. Et si le modèle réduit le nombre d'actions, la preuve interne par action doit être plus forte : c'est ton H3, et il se mesure.

> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*

### Insertion n°65, après la ligne 2058 de la v3.5

> Ancre : monitoring n'est pas celui-là.

> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*

### Insertion n°67, après la ligne 2066 de la v3.5

> Ancre : à comprendre ; à dire seulement une fois versé à la base (volet M, M10, item 12).

> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; détecteurs fine-tunés → volet 7, F·29 ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») *(v3.6)*
