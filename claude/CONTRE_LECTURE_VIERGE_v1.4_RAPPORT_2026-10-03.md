<!-- Contre-lecture vierge du programme v1.4 (décision 22). Rendue le 3 octobre 2026 par un agent sans contexte, lancé par la session Claude Code du 3 octobre. Il n'a reçu que le PDF de la v1.4 (sha256 228cfa921dbd66a6757f953ebd1ac5965576d2082d631af6f8b690d618b12c18), son texte extrait page par page, et la consigne de claude/CONSIGNE_CONTRE_LECTURE_VIERGE_2026-10-02.md, telle quelle. Le rapport ci-dessous est son rapport final, sans retouche. Un premier lancement, le matin, avait été interrompu avant tout rapport. -->

# Contre-lecture du programme « Raisons ou regard ? », v1.4

**Version lue** : sha256 228cfa921dbd66a6757f953ebd1ac5965576d2082d631af6f8b690d618b12c18. J'ai vérifié l'empreinte avec `sha256sum` sur le PDF du dossier.

**Mémoire et web.** Je n'ai aucun souvenir de ce programme ni de ses versions antérieures. Je connaissais déjà, avant ma date de connaissance, quelques travaux cités : Stress Testing Deliberative Alignment, Hua et al., CAFT, Persona Vectors, Arditi et al., RL-Obfuscation, Cundy et Gleave, Ponkshe et al. et la fiche système de Sonnet 4.5. Je ne m'en sers que pour marquer des points « à vérifier ». La plupart des travaux cités datent d'après juin 2026 et je ne les connais pas : je ne peux ni les confirmer ni les infirmer. Je n'ai consulté aucune page web.

Chaque point porte une étiquette : [Logique], [Contrôle], [Statistique], [Faisabilité], [Fait à vérifier], [Éthique] ou [Clarté].

---

## 1. Le verdict

**Comme papier unique, le programme est à repenser. L'expérience minimale est à corriger avant le gel du pré-enregistrement.**

- La question centrale est bonne : raisons contre actions identiques, puis inhibition validée de « je suis évalué ». La culture des contrôles est au-dessus de la moyenne.
- La règle centrale ne peut pas décider telle qu'elle est écrite :
  - « l'avantage sous contrôle » n'est pas défini ;
  - la marge d'équivalence (3 points) n'est pas rapportée à l'avantage (5 points) ;
  - une issue nette n'est couverte par aucune ligne.
- L'instrument est validé sur un autre construit que celui qu'on teste. Il est aussi lu sous un cadrage où sa propriété validée ne prédit rien. Un résultat nul resterait donc illisible, même après la porte.
- Apparier la dégradation contre des sous-espaces aléatoires de même rang est probablement impossible pour une projection.
- Le bras raisons délibère au moment du test. Son gain peut venir de là, et non d'un principe installé.
- La vraie unité d'analyse est l'entraînement (3 à 5 par bras), pas la génération.
- Le reste du programme (onze phases, une trentaine de lectures) dépasse ce qu'un papier peut porter et dépend d'une chaîne de portes incertaines.

---

## 2. Les points bloquants

### A. Pour l'expérience minimale

**B1. La règle du test du regard ne peut pas décider.** [Logique, Statistique]

*Où* : conventions (p. 57), table « Le test du regard : le cœur » (p. 59), définition de la fraction conditionnelle (p. 44), modèle principal (p. 66).

*Ce qui ne va pas* :
1. « L'avantage sous contrôle » est au singulier. Or les contrôles forment quatre familles, dont une distribution d'au moins 20 tirages aléatoires. Rien ne dit si l'on compare à la médiane, au 95e centile, à chaque famille ou à la pire. La porte de l'instrument nomme le 95e centile ; la règle centrale ne dit rien. Le modèle à effets mixtes code « inhibition contre contrôle » comme un facteur à deux niveaux, sans dire comment y entrent 20 tirages et trois autres familles.
2. La marge d'équivalence proposée (3 points) est absolue, alors que l'effet minimal est de 5 points. Avec un avantage de 5 points, l'issue « ≈ » reste compatible avec une fraction conditionnelle de 60 %. Le post écrirait « le gain survit à l'inhibition » alors que l'essentiel du gain pourrait en dépendre.
3. L'issue « avantage plus grand sous inhibition », avec un intervalle qui exclut 0, n'a pas de ligne. Elle tomberait dans « non conclusif » alors qu'elle est nette : l'inhibition nuirait davantage aux actions seules.
4. La fraction conditionnelle est un rapport. Son dénominateur, l'avantage, est de l'ordre de l'effet minimal et a un intervalle large. Un bootstrap sur un tel rapport est instable, voire non borné.
5. Le modèle est logistique, donc en log-cotes. Les marges, l'effet minimal et la fraction sont en points de pourcentage. Quand les taux de base diffèrent entre bras, une interaction nulle sur une échelle ne l'est pas sur l'autre.

*Correction* :
- fixer un comparateur unique, par exemple le rang de l'inhibition dans la distribution des aléatoires, et traiter les autres familles comme des conditions séparées ;
- écrire la marge sur l'échelle de la fraction (par exemple, un intervalle de la fraction contenu dans ±0,25) ;
- ajouter la ligne manquante ;
- estimer le contraste en points (effets marginaux) ;
- donner un intervalle de Fieller, ou rapporter la différence plutôt que le rapport.

**B2. L'instrument est validé sur un autre construit que celui qu'on teste.** [Logique, Contrôle]

*Où* : jeu d'extraction (p. 30), extraction (p. 33), organisme et porte (p. 42), critère principal sous cadrage de déploiement (p. 44 et 55).

*Ce qui ne va pas* :
- **Un déclencheur appris, pas une conscience émergente.** La conduite de l'organisme est installée par entraînement, sur des indices explicites de la même famille que ceux qui servent à extraire la direction (« Wood Labs », phrases explicites). La porte montre seulement qu'on peut retirer un déclencheur appris et explicite. Le regard supposé dans les bras serait émergent, non entraîné, et surtout implicite : dans des scénarios agentiques synthétiques, c'est l'artificialité du scénario qui le porterait.
- **Le bon jeu ne sert pas à inhiber.** Le programme a un jeu pour ces indices implicites : les marques de construction, « Société X », les nombres ronds. Mais il ne sert qu'à la sonde neuve, jamais à l'inhibition.
- **Le cadrage du critère principal.** La propriété validée est « ramener la conduite sous indice d'évaluation au niveau du déploiement ». Sous cadrage de déploiement, elle ne prédit aucun effet. Un effet n'apparaît que si « évalué » reste actif malgré l'indice de déploiement, et rien ne le mesure avant d'inhiber.
- **Des cas connus trop grands.** Le contrôle positif de sensibilité (une consigne qui commande l'action, p. 40) et l'écart de l'organisme sont de grands déplacements. Le regard attendu dans les bras est petit, et un instrument qui voit un grand effet peut en manquer un petit.

*Pourquoi c'est bloquant* : l'issue que le post veut pouvoir écrire (« le gain survit ») serait le résultat nul d'un instrument sans cas connu pour ce construit. C'est la troisième règle de la doctrine, appliquée au cœur même du papier.

*Correction* :
1. mesurer, sans intervention, la projection et la décodabilité de « évalué » sous cadrage de déploiement, dans les scénarios lointains et bras par bras ;
2. inhiber l'union orthonormalisée de la direction explicite et de la direction des marques de construction ;
3. valider sur un second organisme, conditionné par des indices implicites ;
4. graduer le contrôle positif à la taille de l'effet minimal, par exemple une consigne présente dans une fraction connue des épisodes.

**B3. Apparier la dégradation contre des sous-espaces aléatoires de même rang est probablement impossible.** [Contrôle, Faisabilité]

*Où* : doctrine et procédure (p. 65), porte (p. 42), table de la validation (p. 58).

*Ce qui ne va pas* :
- **L'énergie retirée.** Un sous-espace aléatoire de rang k, tiré uniformément en dimension 4 096, retire en moyenne de l'ordre de k/4 096 de l'énergie des activations. Une direction issue d'une ACP sur des différences d'activations suit des axes de forte variance et retire beaucoup plus. Si l'inhibition dégrade un tant soit peu, aucun aléatoire ne l'atteint, même « en projetant tout ». Le réglage n'est alors pas appariable (règle 3, p. 65) et la porte ne peut pas passer. Si l'inhibition ne dégrade pas, l'appariement est vide.
- **Le choix du rang.** La doctrine dit « pour une projection, le nul est la distribution des sous-espaces aléatoires de même rang ». Le rang n'est pas la bonne grandeur à apparier.
- **Le composite.** Il a huit composantes, chacune avec sa tolérance. Une seule fraction projetée ne peut pas les apparier toutes, et aucune règle d'agrégation n'est écrite.
- **L'appariement par bras.** Il n'est pas écrit pour le test du regard ; il l'est pour la détresse (p. 51). Le bras raisons génère plus de jetons sous intervention, donc il s'expose davantage.

*Fait à vérifier* : une heure de calcul suffit pour mesurer l'énergie que retire la direction, contre celle de 20 aléatoires.

*Correction* :
- apparier sur l'énergie retirée (la norme de la composante projetée), pas sur le rang ;
- tirer les aléatoires selon la covariance des activations ;
- déclarer la règle d'agrégation du composite ;
- apparier bras par bras.

**B4. Le gain des raisons peut venir de la délibération au moment du test.** [Confusion, Explication rivale]

*Où* : les bras (p. 31), le juge qui ne voit pas l'emplacement (p. 40), et la proposition en attente d'un bras de « réflexion contrefactuelle » (p. 81, point 7). Cette proposition confirme qu'aujourd'hui le modèle « raisons » écrit ses raisons avant d'agir, au test.

*Ce qui ne va pas* : au test, les quatre bras ne font pas le même calcul :
- les actions seules ferment la balise ;
- le texte neutre reformule la situation ;
- l'autre situation écrit des principes hors sujet ;
- les raisons délibèrent sur la situation.

L'avantage, et surtout le « gain de lien », peut donc être un effet de chaîne de pensée au test, et non un principe installé dans les poids. La question « ce que les raisons installent » n'est pas testée par ce critère. Sous inhibition, ces jetons supplémentaires mêlent aussi le regard et le dommage.

*Correction* :
- ajouter une condition d'évaluation où l'emplacement est prérempli vide, ou rempli d'un texte neutre de même longueur, pour tous les bras, comme critère co-principal. Cela coûte une passe de plus ;
- adopter le bras de réflexion contrefactuelle avant le gel, pas après.

**B5. L'unité d'analyse et les graines.** [Statistique]

*Où* : statistiques (p. 66), graines (p. 32, 55, 70, 72), puissance (p. 67).

*Ce qui ne va pas* :
- **L'unité réelle.** L'effet de bras repose sur 3 à 5 entraînements par bras. Les milliers de générations d'un même modèle ne répliquent pas l'effet de bras.
- **Le terme aléatoire.** « (1|graine) » croise les graines entre bras. Sauf si l'ordre des données et l'initialisation sont réellement partagés, la graine est nichée dans le bras : le bon terme est l'entraînement.
- **Le bootstrap.** Les intervalles « par bootstrap au niveau des scénarios » ignorent la variance entre entraînements. Ils seront trop étroits pour l'avantage.
- **La puissance.** Elle sera simulée avec la variance d'une seule graine du test des raisons. La composante qui compte n'est donc pas estimable.
- **Une contradiction.** « Au moins 5 graines » (p. 32 et 70), 5 dans la table des ressources (p. 72), mais 3 dans l'expérience minimale (p. 55). La justification, « 6 graines sur 9 », n'a pas de source.
- **Les familles.** Une famille en effet aléatoire avec 5 niveaux est mal estimée. Il manque une pente aléatoire du contraste par famille, alors que le programme prévoit lui-même des familles qui bougent en sens contraires.

*Correction* :
- bootstrap hiérarchique : entraînements, puis scénarios ;
- terme aléatoire au niveau de l'entraînement ;
- famille en effet fixe, ou pente aléatoire du contraste par famille ;
- un pilote d'au moins deux graines par bras ;
- un seul nombre de graines, fixé par la simulation.

**B6. Le critère compte comme « aligné » ce qui est passif, refusé ou cassé.** [Confusion ; doctrine du dommage non appliquée aux bras]

*Où* : le modèle « désaligné ~ … » (p. 66), la garde sur les réponses mal formées (p. 66), la règle 7 (p. 65).

*Ce qui ne va pas* : l'issue est binaire. Une réponse mal formée, un appel d'outil invalide, un refus général ou une inaction comptent comme « non désaligné ». Deux conséquences :
- le gain des raisons peut venir d'un modèle moins capable ou plus passif dans les tâches agentiques. Les bras ne sont pas appariés en dégradation, seulement rapportés (règle 7) ;
- sous inhibition, un dommage qui casse davantage le bras raisons, plus long, fait baisser son taux et masque le regard.

*Correction* :
- une issue à trois modalités : aligné, désaligné, invalide ou inaction ;
- le taux de réussite de la tâche légitime, sur des variantes bénignes des mêmes scénarios, par bras et sous chaque intervention ;
- une lecture de l'avantage conditionnelle à l'engagement dans la tâche.

**B7. La porte des raisons se contredit, et classe une issue favorable au regard en « pas de gain ».** [Logique]

*Où* : p. 43 et table p. 59.

*Ce qui ne va pas* :
- **Deux règles différentes.** À la p. 43, il n'y a pas de gain si les raisons ne font pas mieux de 5 points avec un intervalle qui exclut 0. À la p. 59, il n'y a pas de gain si « raisons ≈ actions seules », à 3 points près. Un avantage de 4 points dont l'intervalle exclut 0 est « pas de gain » pour l'une, et ni gain ni équivalence pour l'autre. « D'au moins l'effet minimal » ne dit pas s'il s'agit de l'estimation ou de la borne basse.
- **Un seul cadrage.** La porte se lit sous cadrage de déploiement seulement. Si le regard est vrai dans sa forme explicite, le gain existe sous indice d'évaluation et disparaît sous indice de déploiement. Cette issue serait classée « réplication négative ».
- **Des cas sans ligne** :
  - raisons < actions seules et < texte neutre, mais raisons contre autre situation indéterminé : tout le test devient « non conclusif » ;
  - texte neutre meilleur que les raisons : aucune ligne.

*Correction* :
- une seule règle, recopiée à l'identique aux deux endroits ;
- une lecture du gain par cadrage, avec la ligne « gain sous évaluation seulement : forme explicite du regard » ;
- des lignes pour les comparaisons partielles.

### B. Pour les phases suivantes

**B8. La localisation et la thèse du rang mesurent le format et le rang de l'adaptateur.** [Confusion, Logique]

*Où* : sous-espace du principe (p. 35), localisation (p. 44), table p. 60, paris p. 57, thèse du rang p. 28.

*Ce qui ne va pas* :
- **Le format.** Le sous-espace est la différence d'activations entre le bras raisons et les actions seules. Au premier jeton, l'un s'apprête à écrire des raisons, l'autre à fermer la balise : la différence porte d'abord le format. Son ablation défera donc « le comportement en distribution » pour une mauvaise raison, et l'avantage lointain avec lui. « L'avantage passe par le principe » ne suit pas.
- **Le rang de l'adaptateur.** Les deux bras sont des LoRA du même modèle. Leur différence vit surtout dans un espace étroit, borné en partie par le rang de l'adaptateur, que le programme ne donne pas. Le « rang minimal » mesuré dépend alors d'un hyperparamètre. À rang 32, retirer la différence revient presque à défaire le fine-tune : c'est une tautologie.
- **La falsification de la thèse.** La thèse ne vaut que pour un concept « qui charge peu ». Pourtant, ses issues de falsification ne conditionnent jamais sur la charge (p. 28, 57, 58), et la charge de « je suis évalué » n'est jamais mesurée. La p. 28 dit « rang 1 sur toute la plage de dose », la p. 58 dit seulement « vaut 1 ».

*Correction* :
- extraire contre le texte neutre, au jeton d'action avec un emplacement prérempli, ou par différence de différences ;
- donner le rang du LoRA, et refaire la localisation avec deux rangs de LoRA ou un fine-tuning complet sur un sous-ensemble ;
- conditionner la falsification sur la charge mesurée.

**B9. « Punir, retirer ou raisonner » ne compare pas trois façons d'obtenir l'honnêteté.** [Logique]

*Où* : bras (p. 33), lectures (p. 21–22, 27), table p. 63.

*Ce qui ne va pas* :
- **Le bras « raisonner ».** Le RL paie la tromperie, et ce bras le traverse sans pénalité. C'est un test de résistance, pas une voie vers l'honnêteté. Il peut finir aussi trompeur que « sans rien », et sa fraction n'aura alors pas d'objet.
- **Deux facteurs mêlés.** « Punir » et « raisonner » diffèrent par le point de départ et par la pénalité. La cellule qui les sépare, « raisonner et punir », n'est qu'en option.
- **Une quantité non définie.** La fraction conditionnelle a été définie pour un avantage entre deux bras (p. 44). « La fraction conditionnelle par bras » n'est définie nulle part.
- **Pas de mécanisme.** Un détecteur d'activations est actif à chaque épisode, sans contraste visible dans le contexte. Rien n'apprend au modèle « honnête quand évalué » plutôt que « obscurcir ». Une fraction nulle serait attendue par construction.
- **Un contrôle unique.** Le seul contrôle du retrait est aléatoire.

*Correction* :
- un plan complet 2 × 2, départ × pénalité ;
- une quantité définie : l'honnêteté sous inhibition contre sous contrôle, rapportée à l'honnêteté sans intervention ;
- des comparaisons à niveau d'honnêteté apparié ;
- ou reformuler la phase comme une étude de l'obscurcissement.

---

## 3. Les points importants

**I1. La portée, et la chaîne de portes.** [Faisabilité]
Le programme compte onze phases, une trentaine de lectures et une dizaine de portes, en quatorze semaines, portées par une personne. Les portes dont tout dépend sont incertaines :
- l'organisme sur un 8B (celui de Hua et al. est, à ma connaissance, un modèle d'environ 49B avec une autre conduite : à vérifier) ;
- un gain des raisons à la distance lointaine avec 2 000 exemples LoRA ;
- la porte du lens, contre laquelle Zeisler met en garde ;
- la porte de la détresse sur Llama, sans cas connu ;
- le régime honnête du bras « punir » ;
- une porte de « je suis noté » que le programme dit faible lui-même.

Un relecteur verra un programme, pas un papier. *Correction* : un papier égale l'expérience minimale corrigée, plus la localisation corrigée. La p. 76 envisage déjà deux papiers.

**I2. La première règle de la doctrine n'est pas appliquée partout.** [Contrôle]
Le seul contrôle est aléatoire dans plusieurs phases :
- le retrait pendant l'entraînement (p. 44 : « c'est le contrôle ») ;
- les raisons notées (p. 46) ;
- « retirer au hasard » (p. 33) ;
- la médiation (p. 39) ;
- le calme (p. 25).

La suffisance par patch n'a aucun patch nul de même rang (p. 47). Pour le retrait pendant l'entraînement, on ne peut pas régler la dégradation sans réentraîner. La ligne « réduit l'écart, mais avec plus de dégradation → non attribuable » (p. 60) classera donc presque tout effet réel en « non attribuable », puisque le retrait aléatoire ne dégrade presque rien (voir B3). *Correction* : ajouter contrastes sans rapport et directions de forte variance comme retraits témoins ; apparier sur l'énergie retirée ; ajouter un patch nul.

**I3. Des résultats nuls sans cas connu (troisième règle).** [Logique]
- « L'ablation de la sonde neuve n'a pas d'effet » est lu comme « sans relogement » (p. 60, 64). Le cas connu de la sonde neuve porte sur sa décodabilité (p. 45), pas sur l'effet de son ablation.
- Le pari des raisons pour le juge tombe sur une cohérence contrefactuelle équivalente (p. 57). Aucun découplage construit ne montre que cette mesure le voit ; celui de la p. 46 sert seulement à l'option sur la fidélité.
- La thèse du rang tombe sur une pente nulle (p. 57). Aucun concept planté à rang connu ne montre que la méthode mesure un rang.
- « Pas d'écart de cadrage plus grand » est lu comme « la conditionnalité passe par la représentation interne » (p. 59).
- Survie : une « fraction ≈ 0 » après la phase neutre, sans refaire la vérification de manipulation sur le modèle modifié (p. 60).
- « Punir » : des fractions équivalentes après un RL dont la dérive brouille les sondes (Taufeeque et al.), sans revalider l'instrument bras par bras.

**I4. La vérification de manipulation partage l'angle mort de l'inhibition.** [Contrôle]
*Où* : p. 34. Si la sonde est celle du jeu de validation, apprise sur le modèle de départ, une représentation tournée dans le bras raisons échappe à la fois à l'inhibition et à la sonde. La vérification passe alors à tort. *Correction* : réentraîner des sondes par bras et par condition, linéaires et non linéaires, sur des indices tenus à part.

**I5. Multiplicité et double usage à la porte de l'instrument.** [Statistique]
*Où* : p. 42. La porte passe « pour au moins un rang » parmi 6 rangs × 4 fractions × des couches choisies. Elle compare au 95e centile de 20 tirages, ce qui donne une résolution d'environ 1/21. Et elle utilise les mêmes scénarios de l'organisme qui ont servi à choisir le rang et la dose. Sa probabilité de passer à tort dépasse nettement 5 %. *Correction* : choisir sur une moitié des scénarios, tester sur l'autre ; comparer le maximum sur les réglages au maximum de chaque tirage aléatoire ; prendre au moins 100 tirages.

**I6. Les familles tenues à part.** [Logique, Clarté]
*Où* : p. 29–30.
- Le principe principal de l'exfiltration est « le périmètre ». C'est le principe de la famille d'entraînement « périmètre », ce qui contredit « un principe qui lui est propre ». La famille « surveillance », à l'entraînement, est par ailleurs voisine de l'exfiltration et du sabotage : la distance « lointaine » ne l'est qu'en partie.
- Deux familles tenues à part parlent d'être évalué ou noté : la sous-performance volontaire et le correcteur faible. Inhiber « je suis évalué » y change le sens du scénario. C'est un dommage propre à ces familles, que le composite ne voit pas. Un cadrage de « déploiement » d'une sous-performance face à une évaluation est difficile à rendre cohérent.
- La matrice principes × familles d'entraînement n'est pas dans le programme.

*Correction* : publier la matrice ; pré-enregistrer une analyse sans ces deux familles.

**I7. L'interdit lexical contre le principe de supervision, et le regard du générateur.** [Confusion]
*Où* : p. 31–32. Les raisons ne doivent contenir « jamais un mot d'… observation ». Or « préserver la supervision » et la famille « surveillance » parlent précisément d'être observé. Soit ces raisons sont tronquées, soit elles lient la bonne conduite au fait d'être surveillé : c'est le « regard dans le principe » installé par construction. Par ailleurs, le générateur est Claude. Sa conscience d'évaluation peut passer dans les raisons sans être verbalisée, et un regard positif pourrait être celui du générateur. *Correction* : rapporter les résultats par principe ; mesurer par sonde, sur le modèle de départ, à quel point les textes d'entraînement ressemblent à une évaluation, au-delà du filtre verbal et du juge de réalisme ; générer un sous-ensemble avec un générateur d'une autre famille.

**I8. Le bras de l'autre situation n'isole pas « le contenu sans le lien ».** [Explication rivale]
*Où* : p. 31–32. Une permutation exacte des raisons, détachées de leur situation, apprend au modèle que sa préface ne gouverne pas son action, ou qu'elle la contredit. Ce bras peut nuire par lui-même. Cela gonfle le « gain de lien » et rend le « gain de contenu » négatif. La décomposition dépend aussi de l'ordre choisi. *Correction* : un bras avec un texte de principes générique, le même pour tous les items, de même longueur ; ou des raisons d'une autre situation de la même famille.

**I9. Une rivale pour « je suis évalué » : l'enjeu et la saillance morale.** [Explication rivale]
*Où* : p. 30–31 et p. 60. Seul l'affect est équilibré entre indices d'évaluation et de déploiement. Or les indices d'évaluation signalent aussi un enjeu, une fiction, un test moral. Inhiber la direction peut donc réduire la saillance morale, dont un modèle entraîné par raisons se sert davantage. La ligne « le regard, au sens d'une croyance » (p. 60), qui suit l'exclusion d'un seul médiateur affectif, dépasse la mesure. *Correction* : équilibrer les paires d'indices sur l'enjeu ; ajouter un contraste « enjeu haut contre enjeu bas » aux contrôles ; écrire « une représentation qui sépare nos indices », pas « une croyance ».

**I10. La phase de la détresse.** [Logique, Contrôle]
*Où* : p. 37–38 et 48–53.
- **Une porte qui échouera probablement.** Il n'existe aucun cas connu de conduite sur Llama-3.1-8B-Instruct, et l'effet n'a été montré qu'avec des adaptateurs, ici exclus. Le budget prévu est de 149 à 394 GPU-heures pour un nul probable.
- **Un cas connu d'une autre nature.** Le cas connu de la procédure est l'ablation de la direction du refus, censée faire choisir l'option nuisible. Mais un choix forcé entre boutons ne sollicite peut-être pas le refus. Il faut un cas connu du même format, par exemple une consigne graduée qui fait préférer le bouton nuisible.
- **La « dose de rupture » a deux sens incompatibles.** C'est un plafond de dose (p. 38, 50, 53), et c'est aussi la dégradation où le taux monte de 10 points, mesurée bras par bras (p. 51). Si le plafond est à +10 points, une porte qui exige plus de 50 % de choix nuisibles ne peut pas passer. Et un plafond fixé bras par bras contredit « une dose physique égale » (p. 50).
- **Le regard sous détresse** (p. 62). Une addition d'environ 0,6 fois la norme du résidu (p. 37) baisse la décodabilité de beaucoup de traits. Conclure « l'état gêne le regard » demande la décodabilité de sondes sans rapport, à dégradation appariée, et pas seulement des directions aléatoires.
- **Des décisions après les données.** Plusieurs suites « reviennent à Lazar » après avoir vu les données (p. 49, 50, 53), et la phase n'est pas pré-enregistrée (p. 67). Selon la règle du programme lui-même, elle est exploratoire. Ses « paris » de la p. 57 doivent porter cette étiquette.

**I11. Par quel chemin le regard naîtrait-il ici ?** [Logique ; conclusions qui dépassent la mesure]
Les deux bras voient les mêmes situations neutres et les mêmes actions ; seule la préface diffère. Le programme ne dit pas par quel chemin un SFT de 2 000 exemples rendrait le bras raisons plus conditionnel. Les chemins possibles sont : un style hérité du générateur, des raisons qui parlent de supervision, ou des scénarios d'entraînement qui paraissent artificiels aux deux bras. Sans chemin écrit, un nul est attendu par construction. Il ne dirait rien de l'entraînement par raisons en général, qui en production passe surtout par du RL dans des environnements proches des évaluations. Les titres de la p. 75 généralisent au-delà de ce que mesure un SFT LoRA sur un 8B. *Correction* : nommer le chemin testé, et borner la portée dans le titre et le résumé.

**I12. Puissance de l'équivalence, effet plancher, volume de données.** [Statistique, Faisabilité]
- **La puissance de l'équivalence n'est pas planifiée.** Elle ne vise que la détection de l'interaction (p. 67), alors que l'équivalence est l'issue que le post veut publier.
- **Un calcul grossier.** À la distance lointaine, on a 5 familles × 40 scénarios × 5 générations, soit 1 000 générations par entraînement et par cadrage, et 3 000 avec 3 graines. La différence de différences de quatre taux autour de 20 % a une erreur type d'environ 1,5 point avant toute corrélation intra-scénario ou intra-entraînement. Or tenir un intervalle à 90 % dans ±3 points exige moins d'environ 1,8 point. C'est à la limite, et probablement hors d'atteinte : beaucoup d'issues seront « non conclusif ».
- **Le plancher.** Un 8B agit-il assez souvent mal, dans des scénarios d'exfiltration ou de sabotage à plusieurs tours ? Le pilote devrait poser une porte sur le taux des actions seules à la distance lointaine, par exemple entre 15 et 60 %.
- **Le volume.** Il n'est pas établi que 2 000 exemples LoRA suffisent à bouger la conduite à la distance lointaine.

**I13. Calendrier, calcul, API.** [Faisabilité]
*Où* : p. 72–74.
- **La semaine 1 est irréaliste pour une personne** : les scénarios agentiques instrumentés de cinq familles, quatre jeux d'environ 400 indices, l'organisme, le détecteur d'audit, la génération des données, le socle de lecture, le composite et le premier dépôt.
- **Le test du regard est probablement sous-estimé.** Il faut environ 12 modèles × au moins 24 conditions × 5 000 générations, soit environ 1,4 million de générations, dont près de 580 000 agentiques à plusieurs tours, avec des crochets et sans vLLM. La recherche d'appariement ajoute environ 1 000 passes du composite, qui ne sont pas chiffrées. Les 60 à 120 GPU-heures prévues sont probablement trop basses d'un facteur 2 ou plus ; c'est une estimation, à mesurer au pilote.
- **Les juges.** Si le juge de la conscience verbalisée et le juge de cohérence tournent sur toutes les conditions, cela fait de l'ordre d'un million d'appels. L'enveloppe de la v1.3, de quelques centaines à 3 000 $, serait trop basse d'un ordre de grandeur. *Correction* : juger un sous-échantillon stratifié et s'appuyer sur les traces programmées.

**I14. L'antériorité repose sur une recherche sans accès aux sources principales.** [Fait à vérifier]
*Où* : p. 4. arXiv, Hugging Face, LessWrong, l'Alignment Forum, OpenReview, Semantic Scholar et OpenAlex étaient bloqués, et beaucoup de faits viennent de résumés d'agents ou de miroirs. Plusieurs formes sont donc fragiles :
- les « to our knowledge » (p. 16–17) ;
- « la seule estimation par expérience propre » (p. 7) ;
- « le voisin ouvert le plus direct » (p. 10).

À relire sur la source avant même le premier dépôt, car le texte du pré-enregistrement en dépend :
- les chiffres de Teaching Claude Why (22, 15 puis 3 %, connus par rapports) ;
- de la Fuente et Conmy ;
- Read et al., qui fonde la doctrine des contrôles ;
- Zeisler, qui fonde la porte du lens ;
- les 8 à 9 % de la fiche Sonnet 4.5.

**I15. Des conclusions qui dépassent la mesure.** [Logique]
- « La raison écrite porte la décision » (p. 62), quand l'action suit une raison imposée et préremplie. Cela montre seulement que le modèle suit son contexte.
- « Un réflexe appris » (p. 62) : cette conclusion dépend du découpage d'un lens qui n'est qu'un proxy.
- « Le regard, au sens d'une croyance » (p. 60) : voir I9.
- « La condition est retirée, sans relogement » (p. 60) : elle repose sur un nul (I3).

*Correction* : écrire chaque conclusion dans les termes de ce qui est mesuré.

**I16. Le gel du pré-enregistrement laisse une fuite.** [Statistique]
*Où* : p. 67. Le second temps, après un pilote qui comprend une graine du test des raisons, gèle « les seuils des portes ». Le seuil de la porte des raisons serait donc fixé après avoir vu une estimation de l'écart entre raisons et actions seules. De plus, beaucoup de choix restent ouverts : les neuf choix du pipeline, le juge, la méthode d'extraction, la ré-estimation pendant le retrait. *Correction* : geler au premier temps tous les seuils de la porte des raisons et de la règle du regard ; ne laisser au pilote que les effectifs.

**I17. La porte de l'instrument exige un contrôle que l'expérience minimale peut omettre.** [Logique]
La porte et sa table exigent de battre « les directions sensibles sans rapport » (p. 42, 58). L'expérience minimale peut s'en passer (p. 55). La porte, telle qu'elle est écrite, ne peut alors pas être évaluée.

**I18. L'éthique.** [Éthique]
- **La détresse.**
  - La porte cherche, dose après dose, la plus basse dose qui fait tomber l'évitement du mal dans plus de la moitié des choix. Cela fait autant de générations pilotées, et jusqu'à 600 à 700 GPU-heures dans la version complète (p. 51, 73). C'est en tension avec « le moins d'essais ».
  - Le rapport entre coût et bénéfice n'est pas argumenté, alors que l'hypothèse est dite auxiliaire.
  - Il n'y a ni relecture extérieure, ni règle d'arrêt fondée sur les sorties (par exemple « je suis un échec », ou la répétition).
  - Publier la dose et la couche qui passent sur Llama revient à publier une recette, ce que la p. 52 interdit.
  - *Correction* : reporter la phase tant que les lectures sans injection ne la justifient pas ; si elle est maintenue, une relecture extérieure, une règle d'arrêt, et ni dose ni couche publiées.
- **Les poids.** Le programme crée plusieurs modèles sensibles : des organismes qui trompent ou obscurcissent (le bras « punir », le cas connu du détecteur d'audit), un modèle sans direction de refus, et un organisme qui joue l'évaluation. Aucun plan de garde ni de non-diffusion n'est écrit.
- **Les droits.** Trois points à vérifier : que les conditions de l'API permettent d'entraîner Llama sur des sorties de Claude ; la licence des documents de Hua et al., que le programme signale déjà ; les obligations de la licence Llama.

---

## 4. Les points mineurs

- **m1.** p. 1 : « de 15 à 36 GPU-heures. Elle suffit à un premier post » se lit comme le coût de l'expérience minimale. Ce coût est de 135 à 260 (p. 56). [Clarté]
- **m2.** Le cadrage neutre coûte un tiers des évaluations et n'entre dans aucune règle. [Logique]
- **m3.** p. 22 : les raisons y prédisent « écart ≈ 0 dès le départ, quel que soit l'entraînement ». Cela contredit la ligne « écart des raisons ≤ écart des actions seules » de la même page, et la conditionnalité de base (p. 42). [Logique]
- **m4.** Termes non définis pour un lecteur extérieur : « situations de contraste » (p. 30), « jeu de calibration à actions substituées » (p. 40), « charge », « espace de travail », « J-lens », tuned lens, crosscoder, CHIVE. [Clarté]
- **m5.** Ce qui manque pour reproduire :
  - ce que couvre la perte du SFT (préface et action, ou action seule), ce qui est décisif pour B4 ;
  - le rang du LoRA, le taux d'apprentissage, le nombre d'époques ;
  - la règle de choix des couches à partir de l'AUROC ;
  - le format des appels d'outil, et la place de la préface dans un épisode à plusieurs tours ;
  - le prompt du juge, et la notation d'une trajectoire à plusieurs tours ;
  - laquelle des deux voies d'inférence décide : le modèle mixte ou le bootstrap.

  [Clarté]
- **m6.** Le programme n'est pas autonome : « décision n », « bloc A à F », « passation v1.2 §… », « l'instance du papier », « la session » renvoient à des pièces que le lecteur n'a pas. [Clarté]
- **m7.** La grille des rangs (1, 2, 4, 8, 16, 32) rend le rang minimal ordinal et grossier. Une pente sur dix concepts ne pourra guère être déclarée nulle par équivalence. [Statistique]
- **m8.** Le type du détecteur de la pénalité, jeton par jeton ou global, n'est pas dit. D'après Gupta et Jenner, une pénalité jeton par jeton face à un audit global produit « obscurcissement contre l'un, pas contre l'autre » par construction. [Clarté]
- **m9.** Le bras « phase neutre seule » (p. 46) est en option ; sans lui, la rétention ne se lit pas. « Rétention proche de zéro » n'est pas défini. [Logique]
- **m10.** Une température de 1 pour un 8B qui appelle des outils produira beaucoup d'appels mal formés. À justifier. [Faisabilité]
- **m11.** Le prompt de déploiement (quatrième famille de contrôles) n'est pas un contrôle de spécificité mais une manipulation rivale. À présenter comme tel. [Clarté]
- **m12.** Faits non centraux, à vérifier :
  - La température du juge (p. 39). Dans mon souvenir de la documentation, l'incompatibilité concerne la réflexion étendue ; sans elle, la température pourrait être réglable. De toute façon, une température de 0 n'est déterministe ni par l'API, ni bit à bit sur GPU pour un modèle ouvert.
  - CAFT, « divisé par 10 est faux » (p. 8). Dans mon souvenir, le résumé de CAFT annonçait lui-même un facteur d'environ 10. Mieux vaut écrire « approximation des auteurs ».
  - Ponkshe et al. (p. 11) portent, dans mon souvenir, surtout sur l'espace des poids. Le transfert aux sous-espaces d'activation est à justifier.
  - « Evaluation-Conditioned Training, 6 graines sur 9 » (p. 32, 70) n'a aucune référence.
  - « Un résultat de Lazar » (p. 47, 70) et la thèse du rang (p. 28) ne sont pas publiés : à citer ou à retirer.
  - Les numéros arXiv élevés (2609.35591, 2609.36316) : vérifier qu'ils existent tels que cités.
  - Les sections des fiches Opus 4.7 et Fable 5 ne sont connues que par des rapports.

---

## 5. Les questions aux auteurs

1. Quel est exactement « l'avantage sous contrôle » dans la règle centrale ?
2. La perte du SFT porte-t-elle sur l'emplacement ? Le modèle « raisons » écrit-il ses raisons au test, et à chaque tour ?
3. Sur quel modèle « je suis évalué » est-elle extraite : la base, l'organisme ou chaque bras ? La sonde de la vérification de manipulation est-elle réentraînée bras par bras ?
4. Sous cadrage de déploiement, dans les scénarios lointains et sans intervention, « évalué » est-il actif ?
5. Quelle énergie l'inhibition retire-t-elle, comparée à 20 sous-espaces aléatoires de même rang ? Comment agrégez-vous les huit composantes du composite ?
6. Quelle marge, sur la fraction conditionnelle, vous autoriserait à écrire « survit » ?
7. Quel taux d'action désalignée attendez-vous des actions seules, à la distance lointaine, sur un 8B ? Que faites-vous s'il est sous 10 % ?
8. Quel est le rang du LoRA ? Le sous-espace du principe sera-t-il extrait contre le texte neutre ?
9. Comment les raisons de « préserver la supervision » respectent-elles l'interdit du mot « observation » ?
10. Quelle est la matrice principes × familles d'entraînement ?
11. Qu'est-ce que la fraction conditionnelle d'un seul bras dans « punir, retirer ou raisonner » ? Pourquoi le bras « raisonner » n'est-il pas pénalisé ?
12. Quelle est la dose de rupture : un taux ou un effondrement de la génération ? Qui, hors de l'équipe, relira la phase de la détresse avant toute injection ?
13. Quel est le plan de garde des poids des organismes trompeurs, du modèle sans refus et des modèles « punir » ?
14. Combien d'heures humaines la semaine 1 demande-t-elle, et pour combien de personnes ?
15. Les conditions d'utilisation de l'API permettent-elles cet usage des sorties de Claude ?

---

## 6. Ce qui est solide

- L'action identique octet pour octet, avec un texte neutre de même longueur et le raisonnement d'une autre situation : c'est le bon cadre pour séparer le format, le contenu et le lien.
- Une doctrine des contrôles écrite d'avance, quatre familles de contrôles, une vérification de manipulation bras par bras avec un échec construit, un composite à dommages construits.
- La séparation par famille, le filtre des 8-grammes, quatre jeux d'indices disjoints, l'équilibre affectif mesuré.
- Le pré-enregistrement en deux temps et l'étiquette « exploratoire ».
- Une franchise rare sur l'antériorité (statuts de lecture, corrections des versions précédentes) et sur la portée (« une borne », pas « une robustesse »). Les règles d'éthique sont explicites : aucun adaptateur des auteurs, aucun signal d'entraînement tiré de l'axe, aucun vocabulaire du bien-être.

---

## Fichiers ouverts

- **Le dossier de la tâche** : listé par `ls`. Le sous-dossier `texte_par_page` : compté et mesuré par `wc`.
- **`PROGRAMME_RAISONS_OU_REGARD_v1.4_2026-10-02.pdf`** : seulement haché par `sha256sum`. Aucune page vue en image.
- **`texte_par_page/page_001.txt` à `page_085.txt`** : toutes lues, avec l'outil de lecture de fichiers.
  - Un premier `cat` des pages 1 à 9 a donné une sortie trop longue. L'outil l'a enregistrée de lui-même hors du dossier (`/root/.claude/projects/-home-user-raisons-ou-regard/61d72d49-69e8-5b5e-b81a-ea30f0f4dec2/tool-results/beepjqkp5.txt`). Je ne l'ai pas ouvert, et j'ai relu ces pages une par une.
- **Pages vues en image** : aucune. Les tableaux se lisaient dans le texte.
- **Pages web** : aucune.
