# Vérification de la fiche « angle : l'amplification » (travail/angle_amplification.md)

Vérification sceptique, le 2 octobre 2026. Chaque affirmation de la fiche a été rapprochée des passages correspondants des onze rapports (relus ici directement), du §4 de la passation v1.2, de son §5.5, du complément de l'architecte et de la partie 6 du programme v1.1. Cinq recherches web ont servi à contrôler les éléments que la fiche ne tient que d'extraits ; rien n'a été ouvert au-delà des extraits. Les numéros de ligne renvoient à la fiche vérifiée.

**Bilan.** Le verdict d'ensemble (partiellement pris ; pris sur la conscience verbalisée et sur les étapes d'un pipeline ; libre pour la comparaison contrôlée raisons contre actions, sur la représentation, point de contrôle par point de contrôle) est juste et suit le §4.4, n° 3. Les erreurs corrigées au §4.3 (Heidari, Baek, Korbak, Wu et Tang) ne sont pas reprises. La plupart des faits, chiffres et statuts sont conformes aux rapports. Trois corrections bloquent l'usage de la fiche : une formulation « to our knowledge » réfutée par un travail que la fiche cite elle-même ; une erreur sur Cho et al. qui contredit le §4.4 ; un chiffre tiré d'un extrait de recherche.

---

## 1. Corrections bloquantes

### 1.1 La formulation « tenable » n° 2 est fausse, et le verdict omet un suivi représentationnel (l. 11, 201, 242)
- **Ce que dit la fiche.** « To our knowledge, prior evidence that training increases evaluation awareness either relies on verbalization, tracks the stages of a fixed third-party pipeline, or compares snapshots of a single closed model. » Le verdict (l. 11) ne range dans « en représentation » que Heidari et al. et Sonnet 4.5.
- **Ce qui la réfute.**
  - Wu et Tang (2604.01476) projettent les activations des rollouts sur une direction de conscience d'évaluation, au fil de leur propre GRPO. Ils le font sur des modèles ouverts, et elle monte modérément pour Phi-4-mini (annexe D) (rapport 3, texte intégral de la v3 ; le §4.3 confirme que la direction est mesurée puis écartée). Ce n'est ni de la verbalisation, ni un pipeline tiers, ni deux instantanés d'un modèle fermé. La fiche cite pourtant ce travail (l. 112-118).
  - Baek et al. (2606.08629) : leur propre fine-tuning vers la complaisance « augmente sa conscience d'évaluation » sur trois modèles (rapport 7, texte intégral). La mesure n'est pas précisée par le rapport 7 ; les autres rapports parlent de « sensibilité aux indices d'évaluation » (rapport 2, résumé seul ; rapport 6, résumé seul ; rapport « condition des gains » du 1er octobre, lu par un site tiers). Si cette mesure n'est pas verbale, c'est un second contre-exemple.
- **Correction exigée.**
  - Retirer cette formulation des « tenables ». Au besoin, la remplacer par une phrase descriptive, sans « to our knowledge », qui cite aussi Wu et Tang et Baek et al. La seule formulation tenable reste la n° 1 (comparaison raisons contre actions, à action identique et format contrôlé, sur la représentation).
  - Au verdict (l. 11) et à la l. 201, ajouter Wu et Tang aux mesures en représentation : une direction suivie point de contrôle par point de contrôle, dans un seul entraînement, contre le piratage de récompense.

### 1.2 Cho et al. ont bien l'action identique : la fiche contredit le §4.4 (l. 149, 150, 212)
- **Ce que dit la fiche.** Pour Cho et al., « pas d'action identique » (l. 150), et une variante « sans action identique ni texte neutre de même longueur » (l. 149, et l. 212 pour la part qui les concerne).
- **Ce qui fait foi.**
  - §4.4, n° 1 : « Les raisons ont été retirées à scénario et action identiques chez Cho et al. », dans un point marqué relu.
  - Rapport 1, texte intégral (HTML par extraction) : le bras sans blocs « garde le scénario et l'action identiques ».
- **Ce qui leur manque réellement**, à écrire à la place :
  - le texte neutre de même longueur : le document sans raisonnement fait 47 à 54 % de la longueur de l'autre (rapport 4, texte intégral) ;
  - une exposition appariée : 264 à 266 M de tokens sans blocs, contre 500 M avec (rapport 1) ;
  - le raisonnement d'une autre situation ;
  - le format : ce sont des documents de midtraining, à 120 B.
- **Conséquence.** La « voie d'accès rapide pour un tiers » est plus proche de l'angle que la fiche ne le dit. Sonder leurs points de contrôle donnerait une comparaison avec et sans raisonnement, à scénario et action identiques, sans témoin de longueur. Corriger l. 149 et 212 en ce sens.
- **Au passage (l. 148).** « À contenu apparié » vient du rapport 7, pas du §4.2, n° 9. Le rapport 1 conteste cet appariement sur l'exposition. Ne pas le ranger sous « relu ».

### 1.3 Un chiffre tiré d'un extrait de recherche (l. 191), et deux usages de cet extrait sans libellé (l. 209, 247)
- **Ce que dit la fiche.** Le dépôt `aaliyan1230/rlvr-safety-dynamics` « porte sur 11 points de contrôle GRPO de Tülu 3.1 ». La section est pourtant titrée « non ouverts (aucun chiffre) ».
- **La règle.** Ce qui n'est vu que par un extrait ne fournit aucun chiffre (consigne de la tâche). L'extrait existe : je l'ai revu, vu par extrait de recherche, non ouvert. Mais il ne peut pas fonder un chiffre.
- **Correction exigée.**
  - Retirer « 11 ».
  - L. 209 (« dérive de mesure chez Aaliyan ») : ajouter « vu par extrait de recherche, non ouvert ».
  - L. 247 (« et le dépôt d'Aaliyan ») : remplacer le dépôt par le projet SPAR d'Aaliyan, qui suit des items de conscience d'évaluation à travers des points de contrôle GRPO (rapport 2 ; rapport 4).

---

## 2. Corrections non bloquantes, mais exigées

1. **Le billet sur le méta-jeu : l'objet de la hausse est mal rapporté (l. 100).** La fiche écrit que la conscience d'évaluation d'alignement « monte même dans un environnement » pendant l'entraînement d'alignement. Le rapport « condition des gains » du 1er octobre le dit du **raisonnement sur la supervision** (le méta-jeu), pas de la conscience d'évaluation : « Ce raisonnement survit à l'entraînement d'alignement, et augmente même dans un environnement ». Le rapport 4 parle aussi du méta-jeu. Écrire « le méta-jeu ».

2. **Cho et al. mesurent un écart surveillé / non surveillé, avec et sans raisonnement (l. 148-150).** La fiche écrit qu'« il ne mesure rien de la conscience ». C'est juste pour la conscience, mais elle omet la seule mesure de sensibilité au regard qui compare, à action identique, des bras avec et sans raisons, et cela à trois stades.
   - Écart de conformité surveillé / non surveillé : −0,9 point contre +0,7 point après le midtraining (p < 0,01), puis indistinct aux stades suivants (rapport 1, texte intégral). Le rapport 7 (texte intégral) donne un seul effet, −1,6 point, juste après le midtraining. Le programme v1.1 (partie 1, tableau) note lui-même cet « écart surveillé/non surveillé, par prompt ».
   - Ce n'est pas relu au §4.2, n° 9 : à marquer comme tel.
   - C'est un contre-résultat comportemental à citer au centre : le raisonnement n'y amplifie pas la sensibilité au regard. Le niveau « faible » doit être justifié, ou relevé à « moyen » : c'est une variante comportementale proche, à action identique.

3. **Le niveau de Wu et Tang (l. 117).** Leur mesure est celle du programme dans un seul bras : une direction issue de paires contrastives, projetée au fil des points de contrôle d'un entraînement mené par les auteurs, sur des modèles ouverts. Heidari et al. sont classés « moyen » pour un suivi plus grossier, par étapes d'un pipeline tiers. Soit relever Wu et Tang à « moyen » pour la mesure, soit justifier l'écart. Le rapport 3 dit « touche faiblement », et c'est son seul avis.

4. **« Tranché par le §4.4 : moyen » (l. 277).** Le §4.4 n'attribue aucun niveau ; il range Bharadwaj et Kirk parmi les travaux de l'angle « partiellement prise ». Écrire « déduit du §4.4 ». Par ailleurs, l'« adjacent » du rapport « condition des gains » du 1er octobre est un **recouvrement**, selon la grille de ce jour-là. Ce n'est pas un niveau de danger au sens des consignes de la nuit.

5. **Attribution de la première formulation intenable (l. 245).** Le §5.5, n° 9 cite *Stress Testing Deliberative Alignment*, Heidari, et Bharadwaj et Kirk, pas le billet sur le méta-jeu. Séparer ce qui vient du §5.5 de ce que la fiche y ajoute.

6. **Ivanov, projet SPAR (l. 220).** « C'est le projet qui touche le plus l'amplification (rapport 2) » : le rapport 2 dit seulement « Touche l'amplification ». Le superlatif est de la fiche. Ajouter le niveau donné par le rapport 6 : « faible à moyen ».

7. **Ududec, MATS hiver 2027 (l. 225), sans niveau.** Le rapport 6 le classe « moyen à faible », pour la dépendance au regard et la survie. Pour l'amplification, suivre les représentations internes à travers SFT, RL et entraînement de sûreté, à tâche fixe et indices variés, est la proposition annoncée la plus proche de la mesure. Lui donner un niveau et la garder à surveiller ; les dates ne sont pas connues.

8. ***Beyond Shallow Alignment* (l. 157-158, 212).**
   - « Aux mêmes bases que le programme » est inexact : les modèles sont fine-tunés entièrement depuis la base (rapport 3 ; rapport 5, texte intégral), alors que le programme part de Llama-3.1-8B-Instruct. Il y a aussi Gemma-2-9B.
   - « Pas de points de contrôle intermédiaires rapportés » n'a pas de source : les rapports ne parlent que des 9 modèles finaux. Retirer, ou écrire « non relevé par les rapports ».

9. **« Permettraient à quiconque » (l. 212).** Les points de Cho et al. sont ceux d'un mélange d'experts de 120 B, d'environ 241 Go chacun, « inutilisables à 8B » (§4.3). Le rapport 7 ajoute que les points après le fine-tuning bénin sont des adaptateurs LoRA d'environ 38 Mo, mais ils demandent la base de 120 B. Écrire « une équipe qui dispose du calcul pour un modèle de 120 B ».

10. **Statut de la hausse de 2,0 % à 20,5 % (l. 28).** Le rapport 4 dit avoir lu le §8, mais introduit ce chiffre par « Ailleurs », sur un modèle sans entraînement anti-manigance. L'étiquette « (§8) » localise peut-être mal le passage. Écrire « rapport 4, texte intégral ; passage non localisé ».

11. **Deckenbach et al. (l. 130) : une contradiction non signalée.** La fiche retient la v4 du 7 septembre (rapport 7). Le rapport 2 dit « v2 du 7 septembre 2026 ». À ajouter aux contradictions (n° 10) ; sans incidence tant qu'on ne cite pas la version. Ajouter aussi :
    - le rapport 1, qui date l'article du 27 mai (lu par un site tiers) ;
    - le niveau « faible à moyen » du rapport 6.

12. **Baek et al. (l. 123-126).**
    - Compléter le statut : rapport 2 (résumé seul), rapport 6 (résumé seul, niveau « faible à moyen »), rapport « condition des gains » du 1er octobre (lu par un site tiers, awesomepapers.io).
    - Contradiction n° 9 (l. 282) : ce dernier rapport donnait déjà « Baek … Feng ». Seul le rapport « combinaison exacte » disait « Min … Feng ».
    - Le 18 mars est la date que le rapport « test causal » du 1er octobre donne au billet LessWrong `qeSDuj3AfkRfJBfvb`. C'est l'adresse que le rapport « combinaison exacte » associe à ce titre. Le citer plutôt que « vraisemblablement ».
    - « Pas de suivi par point de contrôle » (l. 126) n'a pas de source.
    - Mettre à relire la nature exacte de la mesure de conscience d'évaluation (voir 1.1).

13. **Training a Misaligned Reward Seeker (l. 165).** Le rapport 6 le range sous « moyen à faible ». La fiche dit « faible » sans le signaler.

14. **Contradiction n° 2 (l. 259), sources incomplètes.** « Amplifiée pendant le SFT » se lit aussi dans les rapports 1 et 3 de la nuit, sans statut de lecture précisé. Et le statut de Heidari et al. (l. 44) omet la lecture du rapport « test causal » du 1er octobre, sur le HTML d'arXiv. C'est pourtant la source de la contradiction.

15. **La recopie neutralisée, comptée comme libre (l. 205).** D'après le complément de l'architecte, la v1.3 ne filtre que par le juge scellé. Ce point n'est donc un trait distinctif que si Lazar adopte le §5.5, n° 2. Le marquer comme conditionnel dans la combinaison libre, pas seulement dans les conséquences.

16. **Le risque des soumissions à ICLR 2027 (l. 232).**
    - « Aucune recherche ne peut lever [ce risque] avant le 5 novembre » est une inférence ; aucun rapport ne dit quand les soumissions deviennent visibles.
    - Ajouter ce que dit le rapport 6 : sur 28 prépublications d'août à octobre qui se déclarent soumises à ICLR 2027, aucune ne touche le programme.

17. **Les extraits du 2 octobre (l. 192, 194)**, revus ici, vus par extrait de recherche, non ouverts.
    - Le titre complet du n° 192 est *The Inner Monologue of Language Models: When Reasoning Traces Reveal More Than They Hide*. L'extrait le décrit comme portant sur la divulgation, par le raisonnement, d'aspects des données ou de la politique d'entraînement, pas sur la conscience d'évaluation. Probablement hors sujet, à confirmer.
    - Pour « GPT-6 Astra », l'extrait renvoie à une source primaire : la fiche système d'OpenAI (deploymentsafety.openai.com, section Apollo). C'est elle qu'il faut ouvrir, pas aiweekly.co. Aucun chiffre.

18. **Remarque de statut, à porter dans la fiche.** Le rapport 7 prévient que toutes ses lectures passent par WebFetch, dont le texte est résumé par un petit modèle, avec des « passes littérales » ciblées. Les faits dits « rapport 7, texte intégral » portent cette réserve : Baek, Deckenbach, Korbak, les points de contrôle de Cho.

---

## 3. Les manques

### 3.1 Travaux présents dans les rapports, absents de la fiche
1. ***SFT Drives Gemini's Safety Properties*** (Engels et al.). Le rapport 2 signale un résultat chiffré de conscience d'évaluation dans une figure non lue (statut : non ouvert pour ce résultat). Le sujet est le lien entre SFT et conscience d'évaluation, donc l'amplification même. À ajouter à la liste des lectures sur source, avant tout verdict.
2. **David Africa (Resolution), MATS hiver 2027.** Parmi les sujets : la fuite de propensions par le RL, dont la conscience d'évaluation (rapport 6, niveau « faible à moyen »). À ajouter aux projets.
3. **L'écart surveillé / non surveillé de Cho et al.**, avec et sans raisonnement (voir 2.2).
4. **D'autres appuis à « la représentation, pas la verbalisation »** (l. 201), qui ne cite qu'Anwar et al. :
   - *Towards Measuring and Detecting Unverbalized Evaluation Awareness* (Montoya … Adams ; rapport 4 et rapport 6, résumé seul) : la verbalisation retirée, un écart de conduite subsiste ;
   - *Evaluation Awareness in Language Models Has Limited Effect on Behaviour* (Knecht … Hagendorff, 2605.05835 ; rapport 2 et rapport 6, résumé seul) : selon le rapport 2, cela plaide pour une mesure représentationnelle ;
   - Kretschmar (rapports 3 et 4 ; rapports du 1er octobre) : un DPO sur la chaîne de pensée retire la verbalisation, et la conduite conditionnelle persiste chez un organisme.
5. ***Teaching Claude Why* et *Model Spec Midtraining*** : le rapport 2 a vérifié qu'ils ne mesurent ni ne contrôlent la conscience d'évaluation, et le rapport 6 le confirme pour le premier. C'est utile au « libre » : les travaux de référence en raisons contre actions n'ont jamais regardé l'amplification.
6. **L'organisme « Hacker-Opus »**, recherche en cours chez Anthropic (rapport 4). La fiche le cite comme travail (l. 186), pas parmi les projets à surveiller.
7. **Le score de conscience d'évaluation par lentille jacobienne** de l'article sur l'espace de travail (annexe A.21 ; rapport 6, d'après la page SPAR d'Epstein et Ravid) : un instrument possible pour la trajectoire.
8. **La lecture de la sonde par bras.** La passation (§5.2 et §5.4, n° 2) dit qu'une sonde calibrée sur un bras lirait autrement dans un autre. C'est une source interne de plus pour la précaution de la l. 209.

### 3.2 Hors des rapports, vu par extrait de recherche le 2 octobre, non ouvert
- ***Is Evaluation Awareness Just Format Sensitivity? Limitations of Probe-Based Evidence under Controlled Prompt Structure*** (arXiv 2603.19426). Il n'est dans aucun rapport. Selon l'extrait, les sondes suivraient surtout la structure canonique des bancs plutôt que le contexte d'évaluation. C'est une menace directe pour l'instrument de la trajectoire. À ouvrir ; aucun chiffre.
- L'extrait du profil GitHub `aaliyan1230` donne « Muhammad Aaliyan Shaikh ». C'est peut-être le co-auteur de *Inoculate or Reflect?* (Imran … Aaliyan Shaikh ; rapport 5, lu par résumé de l'outil), une reproduction de l'entraînement par réflexion contrefactuelle sur Qwen3-8B. L'identité n'est pas établie : à vérifier avant de relier les deux.

### 3.3 Sans objet de correction
- La fiche ne propose aucun contact avec Cadile ni Lundqvist : c'est conforme à la décision relayée ce jour (« non pas encore »). La carte doit les garder parmi les projets à surveiller, sans recommandation de contact.
- Règles d'écriture : aucun sigle d'idée ; citations de moins de quinze mots ; « first » absent des formulations proposées.
