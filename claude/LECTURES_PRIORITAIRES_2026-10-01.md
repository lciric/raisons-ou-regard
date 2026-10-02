# Lectures prioritaires — 1er octobre 2026 (d'après la KB v1.12)

Pour la lecture, les titres réels. Pour la parole, chaque travail se dit par sa forme SAY de la table NAMES.

## 1 · À maîtriser à fond (ta thèse, et les questions les plus probables)

1. **Anthropic, *Verbalizable Representations Form a Global Workspace*** (J-lens, juillet 2026, arXiv 2607.15495). C'est la base de ta thèse.
   - La charge (loading) prédit le succès d'un échange à rang un.
   - La J-space ne fait jamais plus de 10 % de la variance.
   - Ablater l'eval-awareness fait passer la verbalisation de 71 % à 3 %.
   - Le détecteur de l'annexe atteint une AUC de 0,853. Leur propre limite : un comportement pratiqué peut passer sous le workspace.
2. **La lignée eval-awareness des system cards** (Q49, Q77-Q79).
   - Sonnet 4.5, §7.2 et §7.6.4 : la première interprétabilité dans une évaluation d'alignement.
   - Mythos Preview, §4.5.5.
   - Opus 4.8, §6.6.2 : trois vecteurs, dont un tiré d'une seule paire et deux en moyenne-différence. Des vecteurs de contrôle arbitraires bougent aussi le comportement.
   - Fable 5 & Mythos 5, §6.5.1.2 : cinq vecteurs de contrôle, à une force dix fois plus faible.
   - Fable 5.1 & Mythos 5.1 (septembre 2026) : le risque est noté « low rather than very low ».
3. **Fellows, *Persona Vectors*** (Chen et al., arXiv 2507.21509). Une direction par trait ; ta critique du rang s'y applique (Q97).
4. **Anthropic, *Emotion Concepts and their Function*** (avril 2026, arXiv 2604.07729). Les trois critères : activation, pilotage causal, découplage interne-externe. C'est le pipeline que tu as répliqué (Q53).
5. **Sharkey, Chughtai et al., *Open Problems in Mechanistic Interpretability*** (arXiv 2501.16496) (Q122-Q129).
   - L'hypothèse de représentation linéaire, faible ou forte.
   - Les sondes ne trouvent que des corrélations.
   - La validation par la prédiction.
   - La sûreté énumérative.
6. **Fellows, *CHIVE — Would This Change Your Answer?*** (Karvonen et al., août 2026). Les outils qui lisent les activations ne font pas mieux que le transcript seul (Q4, Q116, Q63).
7. **Fellows, *Fine-Tuned Lie Detectors Failed to Generalize*** (Hopkins et Khullar, août 2026). Environ 0,95 en distribution, environ 0,70-0,75 d'une catégorie de mensonge à l'autre (Q2, Q113).
8. **Lindsey, *Emergent Introspective Awareness*** (octobre 2025). L'injection de concepts : environ 20 % de détection, presque aucun faux positif (Q16, Q100).
9. **Hua, Qin, Marks, Nanda, *Steering Evaluation-Aware Language Models to Act Like They Are Deployed*** (MATS, arXiv 2510.20487). C'est le travail publié le plus proche de ton ancrage.

## 2 · Le modèle de menace (le résultat et sa fragilité)

10. ***Alignment Faking*** (décembre 2024), et Fellows, ***Why Do Some LMs Fake Alignment*** (juin 2025) : seuls 5 modèles sur 25 montrent l'écart.
11. ***Sleeper Agents*** (janvier 2024) : l'entraînement adversarial apprend à cacher.
12. ***Auditing Language Models for Hidden Objectives*** (mars 2025) : 3 équipes sur 4 ont trouvé l'objectif ; celle privée d'accès aux données a échoué.
13. ***Natural Emergent Misalignment from Reward Hacking*** (novembre 2025), puis ***Training a Misaligned Reward Seeker*** (août 2026).
14. ***Teaching Claude Why*** (mai 2026) : entraîner sur le pourquoi généralise ; entraîner sur l'évaluation masque le problème.
15. **Les incidents de l'été** : *An alignment assessment of recent cybersecurity incidents* (9 septembre 2026), *Improving our alignment and security efforts* (31 août) et *Risk Report: August 2026*. On y trouve le raisonnement biaisé, l'imprudence, et la note qui passe de « very low » à « low ».

## 3 · Méthodes à connaître (le résultat et une limite)

16. Chen et al., ***Reasoning Models Don't Always Say What They Think*** (2025), et Korbak et al., ***Chain of Thought Monitorability*** (2025).
17. ***Recommended Directions*** (Alignment Science, janvier 2025), et Bowman, ***Putting Up Bumpers*** (avril 2025).
18. ***Activation Oracles***, et les natural-language autoencoders d'Anthropic (Q80, Q103).
19. Amodei, ***The Urgency of Interpretability*** (avril 2025) : l'objectif 2027 (Q93).
