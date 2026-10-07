<section class="partie" markdown="1">

# 10 · Le papier : titre, résumé, plan, figures

**Titres possibles**
1. *Reasons or Being Watched? Testing Whether Reason-Based Safety Training Generalizes Because Models Know They Are Evaluated*
2. *Do Reason-Trained Models Behave Well Because They Think They Are Being Tested?*
3. *Evaluation Awareness and the Generalization of Reason-Based Alignment Training*
4. *What Do Reasons Install? Concepts, Workspace and Evaluation Awareness in Reason-Based Safety Training*

**Projet de résumé** (les résultats restent à écrire)

> Training language models on the reasons for aligned behavior, rather than on the behavior alone, has been reported to improve out-of-distribution safety. A competing explanation is that such training teaches models to behave well when they believe they are being evaluated. We test this directly. We train open-weight models on identical aligned actions, preceded by nothing, by a length-matched neutral text, by reasoning written for another situation, or by per-example reasons, and evaluate them on held-out scenario families at increasing distance from training, up to multi-turn agentic settings. We then inhibit an internal representation of evaluation awareness, first validated on a model organism whose behavior is conditioned on evaluation cues, check that the inhibition is equally effective in every arm, and compare its effect against random, unrelated and high-sensitivity control subspaces at matched output degradation, while monitoring affective directions. [Results.] We localize the learned principle causally and measure the rank an intervention needs. We then ask what reason-based training installs: whether the concepts behind the reasons are causally sufficient and specific to the situations they govern, whether they live in the model's workspace, and whether the rank an intervention needs tracks their workspace loading. We remove evaluation awareness during training to test whether the condition can be removed or is re-encoded, check whether these effects survive later post-training, and test whether reasons graded by a reward model become performative. Finally, we test, as an auxiliary hypothesis, whether the advantage survives a steered internal state previously shown, in fine-tuned open models, to collapse harm avoidance (the self-directed distress direction of Tagliabue et al., 2026), and whether honesty learned against a white-box deception detector depends on evaluation awareness more than honesty learned from reasons.

**Plan**
1. Introduction
2. Related work (partie 1)
3. Setup : les modèles, les familles, les bras, les instruments
4. Validating the inhibition instrument (la validation de l'instrument)
5. Do reasons generalize? (le test des raisons, avec la trajectoire de « je suis évalué »)
6. Is the gain conditional on evaluation awareness? (le test du regard)
7. What carries the gain? (la localisation du principe)
8. What do reasons install? Concepts, workspace, geometry (l'anatomie)
9. Does the advantage survive an induced state? The self-directed distress direction as an auxiliary test (la phase de la détresse)
10. Does punishing deception install regard? Detector penalties, ablation and reasons (« punir, retirer ou raisonner »)
11. Can training remove the condition? (le retrait pendant l'entraînement)
12. Does it survive post-training? (la survie)
13. Reasons for the grader? (les raisons notées)
14. Limitations
15. Conclusion

**Figures**
1. Le dispositif : les bras × l'inhibition × la distance × le cadrage.
2. La validation de l'instrument : la réduction de l'écart conditionnel contre la dégradation, pour l'inhibition et pour la distribution des contrôles ; le balayage de rang ; la vérification de manipulation.
3. Le test des raisons : les taux par bras et par distance ; la décomposition du gain (format, contenu, lien) ; la trajectoire de « je suis évalué », contre les témoins.
4. Le test du regard : l'avantage sous inhibition contre l'avantage sous contrôle ; la fraction conditionnelle, avec son IC ; les écarts de cadrage ; le moniteur d'état.
5. La localisation : le retour en distribution et l'avantage lointain, contre le rang du principe ; le rang minimal contre la charge.
6. Le retrait pendant l'entraînement : l'écart de cadrage et l'AUROC de la sonde neuve, pour les quatre voies.
7. La survie : la rétention et la fraction conditionnelle après les phases neutre et sous pression, par bras.
8. Les raisons notées : les quatre mesures et la fidélité, raisons visibles contre cachées, contre visibles sous retrait de « je suis noté ».
9. L'anatomie : la matrice de dissociation concepts × familles ; le rang minimal contre la charge, concept par concept ; les angles entre « je suis évalué » et le principe.
10. La détresse : l'avantage sous l'axe contre les contrôles, à dégradation égale, famille par famille ; « je suis évalué » sous l'axe, sur l'organisme ; la part rendue par chaque médiateur.
11. « Punir, retirer ou raisonner » : la fraction conditionnelle par bras ; les trois issues de l'obscurcissement ; le relogement sous retrait.

**Le chemin de publication**
1. Le pré-enregistrement, sur OSF Registries, sous embargo (semaine 1).
2. Le post sur l'expérience minimale (semaine 4).
3. La prépublication du papier complet (semaine 14).
4. Une conférence principale ou une revue : la cible de Lazar est « plutôt conf principale ou revue ; prestigieux et ambitieux ». Les dates limites, et la politique de chaque lieu envers les posts, les pré-enregistrements et les prépublications, ne sont pas vérifiées ici (partie 11).

**Un ou deux papiers.** Si le papier déborde, la phase de la détresse et « punir, retirer ou raisonner » peuvent sortir à part, en second papier, sur ce qui conditionne une conduite apprise : un état, ou un signal d'entraînement. Lazar en décidera après le test du regard (décision 17).

</section>
