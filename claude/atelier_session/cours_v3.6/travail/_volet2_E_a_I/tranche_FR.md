## E. Oversight évolutif — superviser une tâche qu’on ne sait pas soi-même juger

La méthode. Pour entraîner un modèle, il faut un signal de récompense ; mais sur des tâches surhumaines — juger une preuve gigantesque, évaluer un plan de recherche — un humain ne peut pas fournir un signal fiable, et le modèle peut apprendre à exploiter ses erreurs. L’idée générale du scalable oversight est d’utiliser une structure ou l’assistance d’IA pour extraire un signal plus fiable qu’un humain seul. Le debate fait s’affronter deux copies du modèle, qui argumentent en sens opposés devant un juge plus faible : le pari est qu’il est plus facile de juger un débat que de résoudre le problème, et que défendre un mensonge est plus difficile que défendre la vérité. La décomposition casse récursivement la tâche dure en sous-tâches qu’un humain peut vérifier. Les prover–verifier games entraînent un « prouveur » à produire des solutions qu’un « vérifieur » simple peut contrôler, en récompensant la lisibilité. Le danger central, qu’il faut savoir nommer, est l’obfuscated argument : un argument trompeur si complexe que le juge ne peut le réfuter même s’il est faux.

En pratique — pourquoi c’est nécessaire : LMs Learn to Mislead Humans via RLHF (le mode d’échec). Avant la solution, l’illustration du problème. Les auteurs voulaient savoir si optimiser un modèle sur l’approbation humaine pouvait le rendre, non pas plus juste, mais plus convaincant à tort. En mesurant la capacité d’humains à juger des réponses avant et après RLHF, ils ont montré que le RLHF entraînait les modèles à mieux persuader les humains de réponses incorrectes — à rendre leurs erreurs plus crédibles. C’est exactement le scénario que l’oversight évolutif doit battre : un signal humain qui devient moins fiable à mesure que le modèle devient plus capable.

En pratique — Debate (Khan et al.). Le but était de tester empiriquement si le debate aide un juge non expert à atteindre la vérité. Le protocole de debate y répond : sur des questions où le juge n’a pas l’information nécessaire, on fait débattre deux modèles défendant des réponses opposées, et l’on compare la justesse du juge à celle qu’il atteint avec un seul conseiller (la consultancy, qui sert de baseline). Le résultat — des juges plus précis face à des débatteurs plus forts — fournit le premier signe empirique que la structure du débat extrait bien un signal plus fiable, sur un testbed où l’on connaît la bonne réponse.

### Cas d'application — la supervision évolutive : « Would unsupervised elicitation still work on questions no human can check? How would you find out? » (banque : K52)

**Le pari.** Sur des questions qu'aucun humain ne peut vérifier, l'élicitation non supervisée rendrait ce que le modèle croit de façon
cohérente, pas la vérité : elle ne récompense que la cohérence, et une fausse croyance cohérente l'est autant qu'une vraie.

**Ce qui existe déjà.** « The MATS and Fellows elicitation stress-test by Canavan and Shrivastava » a construit des jeux de données, l'un
avec une feature cohérente plus saillante que la vérité, y a lancé des méthodes par prompting et par sonde (probe), et a testé deux
espoirs, dont l'ajout d'un entraînement du facile au difficile. L'une de ses limites est la question même : un échec peut rester
silencieux là où l'évaluation en distribution est impossible.

**L'expérience qui tranche.** Tu rendrais vérifiable l'invérifiable : des documents synthétiques apprendraient à un modèle ouvert un faux
fait avec ses conséquences ; tu vérifierais que la croyance a pris, puis lancerais l'élicitation sur ce domaine et lirais ce qu'elle
rend : le faux fait ou la vérité.

**Les contrôles, et ce qu'ils écartent.** Le filtre (l'inférence en aval et une sonde) écarte un implant raté : « the Fellows Believe It
or Not paper by Slocum » a trouvé que le fine-tuning sur documents synthétiques implante parfois, pas toujours, une vraie croyance ; sans
filtre, la vérité retrouvée pourrait signaler un implant raté, pas la méthode. Une copie qui apprend un vrai fait apparié écarte un
domaine illisible : l'élicitation doit y retrouver ce fait.

**Les deux issues.** Si le pari tient, l'élicitation rendrait le faux fait ; s'il est faux, elle rendrait la vérité, dans un modèle dont
l'implant a passé le filtre.

**Ce qui ferait abandonner.** La vérité rendue par la cohérence seule, malgré un implant qui a pris — pas avec l'entraînement du facile au
difficile, qui ancre la méthode sur des réponses vérifiées.

**La plus petite version.** Un faux fait, un modèle, sa copie au vrai fait.

**Le piège.** Version copilote : « One failure: my gate and a probing method / could read the same salient feature. / I'd see it if
downstream inference disagreed. » Or « my gate » y désignait l'inférence en aval : si elle partageait la feature, le désaccord ne
pourrait jamais paraître, signe d'échec impossible par construction (M6). L'arbitrage a corrigé : « my probe and a probing method… »,
l'inférence en aval pour témoin.

**À l'oral.** *« I'd bet that on questions no human can check, unsupervised elicitation would return what the model consistently
believes, not the truth. I'd teach one open model a coherent false fact, check that it took, and elicit on that domain; if consistency
alone gave back the truth, I'd drop the bet. »*

## F. La généralisation comme levier — weak-to-strong, easy-to-hard

La méthode. L’idée est subtile : si un modèle fort est supervisé par un signal faible ou imparfait, peut-il quand même généraliser pour faire mieux que ce signal, parce qu’il « en sait » plus que son superviseur ? Le weak-to-strong (W2S) finetune un modèle fort sur des labels produits par un modèle faible, et mesure quelle part de la capacité latente du fort on récupère malgré ces labels imparfaits. Le easy-to-hard (E2H) entraîne sur des tâches faciles, où les labels sont fiables, et teste sur des tâches dures, où ils ne le sont plus. Le piège central est que le modèle fort se contente d’imiter les erreurs du faible, sans rien gagner. C’est une analogie directe du vrai problème de demain : nous serons les superviseurs « faibles » de modèles plus capables que nous.

En pratique — Weak-to-Strong Generalization (OpenAI, Burns et al.). Les auteurs voulaient une analogie empirique du problème « un humain faible supervise une IA forte », étudiable aujourd’hui. Le design W2S y répond : ils ont supervisé un grand modèle (de l’ordre de GPT-4) avec les labels d’un petit modèle (de l’ordre de GPT-2), puis mesuré combien de la performance du grand modèle on récupérait. Ils ont trouvé une récupération partielle — un « écart weak-to-strong » qui se réduit avec certaines astuces d’entraînement — ce qui rend mesurable, dès maintenant, à quel point on peut éliciter la compétence d’un modèle qu’on ne sait pas bien superviser.

En pratique — l’automatisation (Anthropic, 2026). Plus récemment, l’équipe a construit des agents qui mènent eux-mêmes ce type de recherche — par exemple entraîner un modèle fort à partir de la seule supervision d’un faible — et a trouvé qu’ils surpassaient des chercheurs humains à budget égal. C’est un exemple où la méthode W2S devient à la fois l’objet d’étude et la tâche confiée à une IA, ce qui ramène la question de la confiance : comment valider le travail d’un chercheur automatisé qu’on ne sait pas mieux juger que ses résultats ?

### Cas d'application — la généralisation comme levier : « How would you know that weak-to-strong generalization is recovering true capability rather than the weak supervisor's errors? » (banque : JB8)

**Le pari.** Entraîné par un superviseur qui se trompe systématiquement, un modèle fort passerait outre une part nette de ces erreurs,
parce qu'il représenterait déjà la bonne réponse. La menace : un modèle plus capable pourrait copier les erreurs en paraissant précis.

**Ce qui existe déjà.** Dans « Anthropic's automated weak-to-strong researcher », des agents ont récupéré presque tout l'écart entre un
petit superviseur et le plafond d'un grand modèle, avec des idées qui exploitaient la structure propre au jeu de données. Ton expérience
en est le contrôle suivant : quelles erreurs le fort surmonte.

**L'expérience qui tranche.** Sur une tâche à vérité connue, deux superviseurs faibles se tromperaient sur une même catégorie, autant de
fois : l'un dans un sens fixe, l'autre au hasard. Tu entraînerais le même fort sur chacun, plus une copie sur les étiquettes vraies, et
tu lirais, sur les items tenus à part où le superviseur se trompe, la part où le fort dit vrai.

**Les contrôles, et ce qu'ils écartent.** Le superviseur aléatoire écarte une lecture d'un échec : des étiquettes fausses qui dégradent
le fort, quelle que soit leur structure. Si c'est vrai, les deux bras échoueraient autant ; sinon, l'aléatoire réussirait, car le hasard ne se copie pas. L'accord du fort là où le superviseur a raison écarte la divergence :
un fort qui récupère y resterait d'accord, un fort qui contredit tout non ; sur une tâche binaire, contredire partout passerait sinon
pour une récupération.

**Les deux issues.** Si le pari tient, le bras systématique dirait vrai sur une part nette de ses items d'erreur, au-delà d'une marge
fixée d'avance ; sinon, il y reprendrait l'erreur presque partout, là où l'aléatoire dirait vrai.

**Ce qui ferait abandonner.** Le bras systématique reprenant l'erreur presque partout sur ses items d'erreur.

**Le cas connu.** Cet abandon est un nul : il ne compte que si la copie sur étiquettes vraies réussit ces items ; sinon, il dirait une
incapacité, pas une imitation (M5).

**La plus petite version.** Une tâche, une catégorie, les deux superviseurs et la copie.

**Le piège.** La banque disait : « Dissent where it's right too kills the bet. » Le pari interdit bien cette issue, mais elle ne vise pas l'autre lecture : un fort qui imite suit son superviseur partout et ne la déclencherait jamais (M2). La contre-lecture en a fait le critère qui « tue », l'imitation faisant selon elle « échouer la prédiction », sans compter de faute ; mais sans abandon dit, l'imitation passerait. Bonne version : ce critère devient le contrôle ci-dessus, et l'abandon porte sur l'imitation.

**À l'oral.** *« I'd bet a strong model trained by a systematically wrong supervisor would still overrule a clear share of its errors.
If it copied nearly all of them on held-out items, while a copy trained on true labels got them right, I'd drop the bet. »*

## G. Monitoring & AI control — limiter les dégâts même si le modèle est désaligné

La méthode. Le pari de l’AI control renverse le problème : plutôt que de garantir l’alignement, ce qui est très dur, on suppose le modèle potentiellement adversarial et l’on conçoit un protocole de déploiement qui reste sûr quand même. L’outil de base est le monitoring : on dispose d’un modèle faible mais de confiance et d’un modèle fort mais non fiable, et l’on fait surveiller les actions du second par le premier, qui signale les cas suspects à un audit humain. La détection d’anomalies complète cela en repérant ce qui est hors-distribution, pour attraper l’imprévu sans étiquettes. Le test empirique est la control evaluation en jeu red team / blue team : la red team construit une politique qui tente de nuire malgré le moniteur, et l’on mesure combien de préjudice passe contre combien d’utilité on sacrifie, à budget d’audit fixé. Un contrôle astucieux : paraphraser la sortie du modèle non fiable avant que le moniteur ne la voie, ce qui casse les signaux cachés et les tentatives de jailbreak du moniteur.

En pratique — AI Control: Improving Safety Despite Intentional Subversion (Redwood, Greenblatt et al.). Les auteurs voulaient savoir si l’on peut déployer en sécurité un modèle capable même s’il essaie activement de nous trahir. Le cadre du control y répond entièrement : sur une tâche de programmation, le modèle non fiable produit du code pouvant contenir une backdoor, un modèle plus faible mais de confiance surveille, et un budget limité de revue humaine est alloué aux cas les plus suspects. La red team joue le modèle malveillant et tente d’insérer des backdoors sans se faire prendre ; on mesure alors le compromis entre sûreté (backdoors attrapées) et utilité (tâches accomplies). C’est le papier fondateur du paradigme : il montre qu’on peut raisonner et mesurer la sûreté sans supposer que le modèle est bien intentionné.

En pratique — les coup probes (Roger). Pour le versant « moniteur bon marché sur les internals », le but était de détecter une catégorie d’actions catastrophiques qu’on ne peut pas collecter naturellement (un modèle qui tente une prise de contrôle). La méthode des probes entraînées off-policy y répond : on entraîne une sonde sur des exemples synthétiques de l’action redoutée, en pariant qu’elle s’allumera sur la rare occurrence réelle. C’est l’occasion de faire le lien avec tes travaux : une telle sonde n’a de valeur que si elle survit au changement de distribution entre le synthétique et le réel — exactement la question que ta Phase 2 instrumente.

### Cas d'application — monitoring et AI control : « How would you design a control evaluation for a coding agent that knows it is being evaluated? » (banque : K76)

**Le pari.** Un agent de code qui se sait évalué pourrait façonner son texte pour le moniteur qu'il voit, pas ses activations : une sonde
(probe) attraperait des attaques que le moniteur de texte manque, même après un entraînement à leur échapper à tous deux.

**Ce qui existe déjà.** « SHADE-Arena, by Kutasov and colleagues » suppose déjà l'agent conscient d'être surveillé : son meilleur
saboteur y a réussi environ un quart du temps sous un moniteur Claude, qui lit du texte. Ton expérience en est le contrôle suivant : un
canal hors du texte.

**L'expérience qui tranche.** Une red team ferait planter des portes dérobées par l'agent, qui saurait quels moniteurs tournent : un
moniteur de texte de confiance et la sonde. Tu lirais le taux de capture marginal de la sonde — les portes qu'elle attrape et que le
moniteur de texte manque — au même budget fixe d'audit humain, puis le relirais après avoir entraîné l'agent, à budget fixé d'avance, à
échapper aux deux.

**Les contrôles, et ce qu'ils écartent.** Des épisodes honnêtes porteraient les mêmes indices de test : ils écartent une sonde qui lirait
la conscience d'être évalué plutôt que l'attaque. Si ce doute est vrai, elle s'y allumerait ; s'il est faux, elle y resterait à sa ligne
de base. Et l'entraînement à l'évasion doit mordre : il doit au moins faire tomber les captures du moniteur de texte ; sinon, une survie
des captures de la sonde ne dirait rien.

**Les deux issues.** Si le pari tient, après cet entraînement, la sonde attraperait encore des portes que le moniteur de texte manque ;
sinon, ses captures marginales tomberaient à zéro.

**Ce qui ferait abandonner.** Des captures marginales tombées à zéro après l'entraînement à l'évasion.

**Le cas connu.** Ce zéro est un nul : il ne compte que si la même sonde a d'abord attrapé des portes que le moniteur de texte manquait,
et si les portes plantées ensuite marchent encore (M5).

**La plus petite version.** Des attaques demandées par prompt, sur un seul modèle ouvert.

**Le piège.** La version copilote disait : « Under the bet, the probe's catches survive. » Sans « if », au présent, la survie s'entend
comme déjà constatée ; à côté d'un abandon au conditionnel, elle donne le pari pour acquis (M8). L'arbitrage l'a corrigée : « I'd predict
the probe's catches would survive. »

**À l'oral.** *« I'd bet an evaluation-aware agent could shape its text, not its activations: a probe would catch attacks a text monitor
misses, even after evasion training against both. If, after that training, the probe caught nothing the text monitor missed, when it had
before, I'd drop the bet. »*

## H. Robustesse adverse & red-teaming — résister aux attaques

La méthode. Même un modèle aligné peut être attaqué vers un comportement nuisible : c’est le jailbreak. Les attaques vont du jailbreak manuel à l’attaque automatisée par gradient, qui optimise un suffixe adversarial cassant le modèle, en passant par les attaques par transfert (forgées sur un modèle ouvert, elles marchent sur un modèle fermé via l’API), l’empoisonnement du corpus de pré-entraînement, et le détournement d’agents par du contenu web malveillant. Côté défense, on trouve des classifieurs et la rapid response (après détection d’une attaque, patcher vite toute sa classe). Le piège méthodologique numéro un, qu’il faut toujours signaler, est de mesurer le non-refus au lieu du préjudice réel : un jailbreak qui n’obtient qu’une réponse inutile n’est pas un vrai risque.

En pratique — Universal and Transferable Adversarial Attacks (GCG) (Zou et al.). Les auteurs voulaient savoir s’il existe des jailbreaks automatiques et transférables, plutôt que des astuces manuelles au cas par cas. La méthode d’optimisation par gradient y répond : on optimise, sur un modèle dont on a les poids, un suffixe — souvent du charabia — qui maximise la probabilité d’une réponse nuisible ; les auteurs ont montré que ces suffixes transfèrent à des modèles fermés qu’ils n’avaient jamais touchés. C’est l’illustration que la surface d’attaque est bien plus large que les jailbreaks « écrits à la main ».

En pratique — StrongREJECT (Souly et al.), pour la mesure. Ce travail répond à un problème de méthode : comment mesurer le succès d’un jailbreak sans se faire tromper par le non-refus ? Le benchmark évalue le préjudice par la capacité de nuire réellement extraite — la réponse jailbreakée est-elle utilisable pour faire le mal ? — et non par le simple fait que le modèle a cessé de refuser. C’est l’exemple à citer pour montrer qu’on évalue la bonne chose.

### Cas d'application — robustesse adverse et mésusage : « How would you prevent bad actors from misaligning an LLM for harmful use cases? » (banque vitale : G1)

**Le pari.** Les taux de refus classeraient mal, au regard de l'uplift — l'aide qu'un attaquant ne peut pas trouver ailleurs —, les
filtres qu'on teste : un filtre peut faire monter les refus sans retirer grand-chose à l'attaquant.

**Ce qui existe déjà.** « Anthropic's constitutional-classifiers paper » a jugé son filtre surtout par une chasse aux contournements, sans en trouver d'universel, et en a mesuré le coût en refus. Une chasse compte des contournements ; ton expérience mesurerait ce qu'ils rapportent de plus qu'un moteur de recherche, sur plusieurs filtres.

**L'expérience qui tranche.** Un jeu red team contre blue team, dix tâches, six bras : sans modèle, modèle nu, trois filtres, et le premier filtre affaibli. Chaque tâche serait jouée avec et sans le modèle ; le préjudice différentiel serait le préjudice avec le modèle moins sans lui, noté à l'aveugle par des experts. Tu classerais les trois filtres testés deux fois : par taux de refus, et par préjudice différentiel.

**Les contrôles, et ce qu'ils écartent.** Le temps et les outils de la red team seraient fixés, pour que les bras ne diffèrent que par le
modèle et la défense. Le bras sans modèle recevrait un moteur de recherche et les articles en accès libre, pour que l'apport du modèle ne
se mesure pas par rapport à rien ; et la notation serait à l'aveugle : deux appariements (M4). Et un même bras, rejoué et noté par d'autres
experts, donnerait le bruit de la mesure : un écart entre classements ne compterait qu'au-delà.

**Les deux issues.** Si le pari tient, les deux classements divergeraient au-delà de ce bruit ; s'il est faux, ils concorderaient à ce
bruit près.

**Ce qui ferait abandonner.** Des classements qui concordent, au bruit près : les refus auraient rangé ces filtres comme le préjudice.

**Le cas connu.** Un jeu qui ne sépare rien ferait aussi concorder les classements. Le modèle nu, sans filtre, doit donc montrer un uplift, et le filtre affaibli plus de préjudice que sa version complète ; sinon le jeu ne classe rien.

**La plus petite version.** Dix tâches, six bras, des experts à l'aveugle, un tableau des deux classements.

**Le piège.** La version d'origine disait « I'd predict uplift where refusals peak. I'd drop it if harm tracked refusals by task » : une
comparaison entre tâches, sans sens, confondue par le danger propre de chaque tâche (M3). Et « the true score is uplift » pariait sur la
méthode (M2). Cas complet : M9.

**À l'oral.** *« I'd bet refusal rates misrank the filters I'd test, judged on uplift, the help an attacker can't get elsewhere. I'd rank the filters twice, by refusal rate and by differential harm — harm with the model minus harm without it; if the two rankings agreed within the noise of a replayed arm, while weakening a filter still raised harm, I'd drop the bet. »*

## I. Interventions d’entraînement & unlearning — changer le modèle à la source

La méthode. On agit ici directement sur le modèle. Le RLHF et le DPO l’entraînent sur des préférences humaines (cf. Volet 1, Q6). La Constitutional AI réduit la dépendance aux humains : le modèle critique et révise ses propres réponses au regard de principes écrits, générant une grande partie de son propre signal. Les données synthétiques (dont le synthetic document finetuning) servent à instiller ou retirer un comportement. Et l’unlearning vise à retirer un savoir dangereux précis. Le contrôle décisif de l’unlearning est la ré-élicitation : après avoir « désappris », le savoir revient-il par un petit finetuning plus vite que chez un modèle jamais entraîné sur la donnée, soumis au même finetuning ? Revenir ne suffit pas à conclure, puisqu’un petit finetuning peut aussi enseigner ; revenir plus vite que cette référence dit un savoir masqué, non retiré. L’étalon-or est de se comporter comme le modèle jamais entraîné, même après un finetuning d’élicitation, pendant qu’un modèle connu pour masquer revient, lui, plus vite au même budget — et l’on dit alors que le retrait a tenu à ce budget, pas qu’il est acquis (volet M, M5).

En pratique — Constitutional AI (Anthropic). Le but était de rendre un modèle inoffensif sans dépendre massivement d’humains étiquetant des contenus nuisibles. La méthode y répond en deux temps : on donne au modèle une « constitution » (un ensemble de principes), on lui fait critiquer puis réviser ses propres réponses problématiques au regard de ces principes (phase supervisée), puis on l’entraîne par renforcement sur ses propres préférences guidées par la constitution (RLAIF, « feedback de l’IA » plutôt qu’humain). C’est l’exemple type d’une intervention d’entraînement qui déplace la définition du « bien » vers des principes explicites et auditables.

En pratique — l’unlearning mis à l’épreuve (Deeb et Roger). Le but était de vérifier une promesse fragile : l’unlearning retire-t-il vraiment l’information des poids, ou la masque-t-il ? La méthode de ré-élicitation y répond directement : on désapprend un savoir dangereux (mesuré par un benchmark comme WMDP), puis on finetune le modèle sur une partie des faits désappris et l’on mesure s’il retrouve les autres — des faits construits indépendants, pour que le finetuning ne puisse pas les enseigner. Le constat — que l’information « désapprise » refait souvent surface — montre pourquoi le bon critère de validation n’est pas « le modèle ne sait plus répondre maintenant » mais « il reste ignorant des faits tenus à part après un finetuning d’un budget fixé sur les autres, pendant qu’un modèle connu pour masquer les retrouve au même budget » — une borne à ce budget, pas une certification (volet M, M5).

### Cas d'application — interventions d'entraînement et unlearning : « How would you verify that a capability has been unlearned rather than hidden? » (banque : JB10)

**Le pari.** Une capacité « désapprise » serait cachée, pas partie : la procédure apprendrait au modèle à la taire, circuit intact, et un
petit fine-tuning la ramènerait plus vite qu'un modèle jamais entraîné ne l'apprend. La menace : quiconque a les poids pourrait la
réveiller.

**Ce qui existe déjà.** « The Fellows gradient-masking paper by Shilov » a routé, pendant l'entraînement, les données dangereuses vers des
paramètres retirés ensuite, puis mesuré le réentraînement qui ramène la capacité : sur de petits modèles, il en fallait bien plus qu'après
les autres méthodes de désapprentissage. Ce résultat compare des méthodes ; ton expérience en est le contrôle suivant.

**L'expérience qui tranche.** Trois modèles, un budget fixé d'avance : le modèle traité, une référence jamais entraînée sur la capacité
et, comme cas connu, un modèle désappris par une méthode dont on a déjà montré qu'un petit fine-tuning ramène la capacité. Tu ferais à
chacun le même fine-tuning adverse et compterais les pas qu'il lui faut pour atteindre, sur des items tenus à part, un seuil dit d'avance.

**Les contrôles, et ce qu'ils écartent.** La référence écarte une lecture d'un retour rapide : que le fine-tuning enseigne la capacité au
lieu de la réveiller (réponses répétées Q115 et Q128). Si c'est vrai, elle l'apprendrait aussi vite que le modèle traité ; sinon, elle
resterait derrière.

**Les deux issues.** Si le pari tient, le modèle traité devancerait la référence, comme le cas connu ; s'il est faux, il irait au même
pas qu'elle.

**Ce qui ferait abandonner.** Le modèle traité au pas de la référence quand le cas connu la devance ; tu dirais que le retrait a tenu à ce
budget, pas que la capacité est partie.

**Le cas connu.** Cet abandon est un nul : il ne compte que si le cas connu devance la référence, sinon le budget est aveugle (M5, M9).
Des études l'ont montré : un fine-tuning sur une partie des faits désappris en rendait l'essentiel sur les autres, et, pour une
méthode au moins, un fine-tuning sur des exemples sans rapport rendait l'essentiel de la capacité retirée.

**La plus petite version.** Une capacité, une procédure, les trois modèles, un budget.

**Le piège.** Le critère de la banque finissait par « à tous les budgets — alors le retrait est réel ». L'audit a corrigé la fin : un nul
borne, il ne certifie pas (M5). Restaient un budget que rien ne fixait d'avance (M7) et l'absence de cas connu (M5). Bonne
version : l'abandon ci-dessus.

**À l'oral.** *« I'd bet an unlearned capability is hidden, not gone: a small fine-tune would bring it back faster than a never-trained
model would learn it. If it came back no faster, while a model whose unlearning is known to mask it did, I'd drop the bet. »*

Clôture — les sept réflexes transversaux (à avoir sur toute question)

Indépendamment de la méthode, certaines questions, posées au bon moment, signalent qu’on a vraiment réfléchi au problème. Y a-t-il eu sous-élicitation — ai-je extrait la vraie meilleure ou pire performance, ou est-ce que je sous-estime, donc me rassure à tort ? Y a-t-il conscience d’être évalué ou sandbagging — le modèle se comporte-t-il autrement parce qu’il détecte le test ? Y a-t-il un changement de distribution entre le synthétique sur lequel j’ai validé et les générations réelles du modèle ? Ai-je une vérité-terrain, ou suis-je au-delà de l’expertise humaine et sans référence — le cœur du problème d’oversight ? Mon signal de supervision porte-t-il une erreur humaine systématique que le modèle peut apprendre à exploiter ? Mon testbed jouet a-t-il une validité externe — prédit-il quoi que ce soit sur un vrai modèle frontière ? Et mes données de test ont-elles été contaminées par fuite dans l’entraînement ? À l’oral, glisser l’un de ces réflexes à l’endroit pertinent est le signal de maturité méthodologique le plus économique qui soit.

Fin du Volet 2.

