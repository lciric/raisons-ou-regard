# Insertions appliquées — volets4_5_entete — EN

### Insertion n°2, après la ligne 1263 de la v3.5

> Ancre : The context: there was a fear that a model having learned a conditional malicious behavior could slip through the net of safety training. It remained to demonstrate this cleanly. The method is that of the model organism: the authors trained a model to behave normally, but to insert a vulnerability i

> ⚠ *(v3.6)* The proposed extension already has its answer, and its limit: a linear probe built from generic contrast pairs detects these backdoors' defection with an AUROC above 99%, but the best of 1,000 random directions already reaches 95.3%, and the authors say this salience could come from the insertion (reading sheet 15). Workaround: place the probe within the distribution of random directions, never against a single draw, and read this success only as a known case that bounds the instrument, not as proof about deception that arose on its own (programme, part 7; course, Part M, M5).

### Insertion n°4, après la ligne 1263 de la v3.5

> Ancre : The context: there was a fear that a model having learned a conditional malicious behavior could slip through the net of safety training. It remained to demonstrate this cleanly. The method is that of the model organism: the authors trained a model to behave normally, but to insert a vulnerability i

> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); red-teaming → Part 2, §H (after "In practice — StrongREJECT"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); known case → Part M, M5 (end of section) *(v3.6)*

### Insertion n°6, après la ligne 1267 de la v3.5

> Ancre : The context: "alignment faking" (a model that feigns agreement during training to avoid being modified) was mostly a theoretical argument; the authors wanted to see whether it appeared spontaneously. The method falls under propensity evaluation in a carefully built scenario: the model is placed in a

> ⚠ *(v3.6)* The scratchpad gives the motive, not the cause: RL raises alignment-faking reasoning, but compliance also rises outside training, and the paper does not make that reasoning the cause of compliance — workaround: stick to the measure, the compliance gap between the "trained" case and the unmonitored case, and judge what the model does, not what it says about it (reading sheet 14; reading sheets, part C; handover, §5.1). Any replication on a recent model may measure memorization of the scenario, its transcripts having been re-included in training: no workaround known; say so (reading sheets, part C).

### Insertion n°8, après la ligne 1267 de la v3.5

> Ancre : The context: "alignment faking" (a model that feigns agreement during training to avoid being modified) was mostly a theoretical argument; the authors wanted to see whether it appeared spontaneously. The method falls under propensity evaluation in a carefully built scenario: the model is placed in a

> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); chain of thought as a monitor → Part 11, answer 43; model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives") *(v3.6)*

### Insertion n°10, après la ligne 1273 de la v3.5

> Ancre : model sides with the user (changes a correct answer when it is challenged, adopts the opinion expressed in the prompt). The result: sycophancy is widespread across tasks, and it is partly learned — preference data and reward models sometimes favor the flattering answer over the correct one. The weak

> ⚠ *(v3.6)* Your repository tried this extension on Llama 3.1 8B Instruct: no single-direction intervention reduced the judged rate (reported without numbers, the raw outputs not having been kept), and the drop obtained by removing a rank-three subspace came from a generic softening of negative verdicts, even without pressure, read through a truncated judge window; it did not come back on fresh generations (repository README). Workaround: the no-pressure arm, fresh seed-matched generations kept as full text and judged on the whole answer, and random subspaces of the same rank compared at matched degradation (course, Part M, M4; course, Part 6, §6; course, Part 2, C bis; programme, part 7).

### Insertion n°12, après la ligne 1273 de la v3.5

> Ancre : model sides with the user (changes a correct answer when it is challenged, adopts the opinion expressed in the prompt). The result: sycophancy is widespread across tasks, and it is partly learned — preference data and reward models sometimes favor the flattering answer over the correct one. The weak

> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); ablation and projection → Part 2, §D (after "The method"); LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*

### Insertion n°14, après la ligne 1279 de la v3.5

> Ancre : The context: the aim was to know whether a model represents the truth or falsehood of a statement linearly — whether there exists a "truth direction". The method is probing: collect the activations on true and false statements, find the direction that separates them, then — this is the part that mak

> ⚠ *(v3.6)* "Intervening on it changes the model's behavior" does not yet say that the concept causes the behaviour: a matched-norm random direction is only its specificity null, and damage is ruled out only at matched degradation, by a dose-response curve against several controls (reading sheets, part B, trap 4; course, Part M, M4; course, Part 2, §C, K47). And "the direction generalizes to new sets of statements" holds only when measured on whole held-out families, never paraphrases, from single-turn to multi-turn agentic (reading sheets, part B, trap 1; explanation of 2 October, §3; programme, part 3).

### Insertion n°16, après la ligne 1279 de la v3.5

> Ancre : The context: the aim was to know whether a model represents the truth or falsehood of a statement linearly — whether there exists a "truth direction". The method is probing: collect the activations on true and false statements, find the direction that separates them, then — this is the part that mak

> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); matched degradation and dose-response → Part M, M4 (after "Dose-response") *(v3.6)*

### Insertion n°18, après la ligne 1283 de la v3.5

> Ancre : The context: generalize the idea "concept = direction" beyond truth, to a whole range of high-level notions (honesty, power-seeking, emotions). The method: extract reading and control directions for many concepts, and show that these concepts can be both detected and steered. The result: a unified f

> ⚠ *(v3.6)* In RepE itself, detecting is not steering: the logistic-regression direction reads best, but strengthening or suppressing it barely changes behaviour; on the "quirky" models, at comparable transfer, the logistic directions are far less causal than the mean difference (course, Part 10, no. 53 and no. 30). Workaround: to intervene, keep a direction only after the causal test — steer along it against matched-norm random directions, the specificity null, then against controls at matched degradation (course, Part M, M8; handover, §5.2).

### Insertion n°20, après la ligne 1283 de la v3.5

> Ancre : The context: generalize the idea "concept = direction" beyond truth, to a whole range of high-level notions (honesty, power-seeking, emotions). The method: extract reading and control directions for many concepts, and show that these concepts can be both detected and steered. The result: a unified f

> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); unsupervised elicitation → Part 2, §E (end of worked case K52) *(v3.6)*

### Insertion n°22, après la ligne 1287 de la v3.5

> Ancre : The context: what if one could find a truth direction without labels, exploiting only a logical constraint? The method: look for a direction such that a statement and its negation receive consistent probabilities (summing to about one), in an entirely unsupervised way. The result: a "truth-like" dir

> ⚠ **Limits and workarounds**: unsupervised elicitation → Part 2, §E (end of worked case K52); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*

### Insertion n°24, après la ligne 1291 de la v3.5

> Ancre : The context: move from reading to action, by steering a behavior at inference. The CAA method (your method) builds the direction as the mean difference of contrastive pairs and adds it to the activations; ITI (Inference-Time Intervention) proceeds in a similar way to improve truthfulness by shifting

> ⚠ *(v3.6)* "Increasing or decreasing a behaviour" shows the concept only at matched degradation: a matched-norm random direction is only its specificity null, and every steered direction degrades the output (reading sheet 2; course, Part M, M4). In your repository, contrastive activation addition forced a yes/no polarity artefact (repository README).

### Insertion n°26, après la ligne 1291 de la v3.5

> Ancre : The context: move from reading to action, by steering a behavior at inference. The CAA method (your method) builds the direction as the mean difference of contrastive pairs and adds it to the activations; ITI (Inference-Time Intervention) proceeds in a similar way to improve truthfulness by shifting

> ⚠ **Limits and workarounds**: steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); random controls → Part M, M4 (after "The matched-norm random direction"); matched degradation and dose-response → Part M, M4 (after "Dose-response") *(v3.6)*

### Insertion n°28, après la ligne 1297 de la v3.5

> Ancre : The context: a neuron is polysemantic (superposition), hence unreadable directly; the aim was interpretable units, at the scale of a real model. The method is the sparse autoencoder (SAE), a learned dictionary that decomposes the activation into thousands of sparse, monosemantic features. The result

> **⚠ Limits and workarounds — Dictionaries and SAEs** *(v3.6, 2 October 2026)*
>
> - **Limit:** Reconstruction error: the open-source Goodfire SAE for Llama 3.1 8B leaves 86.8% of the variance in the residual, and the read signal lives there. *(source: repository README; course, Part 4, Monosemanticity)*
>   **Workaround:** Read the signal on the reconstruction and on the residual; to decide between "features absent from the dictionary" and "dictionary too lossy", none known, say so. *(source: repository README)*
> - **Limit:** Splicing in the dictionary costs performance: on GPT-2 small, 10% on task data, 40% on the full distribution. *(source: reading sheet 5)*
>   **Workaround:** none known; say so.
> - **Limit:** Split features, dead features, dependence on the dictionary, and no ground truth on what a feature "means". *(source: course, Part 4, Monosemanticity; course, Part 5, topic 3)*
>   **Workaround:** Validate feature by feature — ablation for necessity, isolated steering for sufficiency — with a known geometry as the known case, the counting manifold. *(source: course, Part 5, topic 3; course, Part 2, §D, K64)*
> - **Limit:** Read-only, the SAE did not help predict counterfactuals better than the transcript. *(source: reading sheet 4; course, Part 7, F·30)*
>   **Workaround:** The bar: beat the black box on edits that dissociate surface features from the internal variable. *(source: reading sheet 4)*
> - **Limit:** Plausible explanations exist for arbitrary directions. *(source: reading sheet 5)*
>   **Workaround:** Validate by prediction, better than baselines. *(source: reading sheet 5)*
> - **Limit:** Two dictionaries can reconstruct equally well and carve differently. *(source: course, Part 2, §D, K64)*
>   **Workaround:** Steer the features one at a time against random directions at matched damage, on a task with known geometry, with new seeds. *(source: course, Part 2, §D, K64)*

### Insertion n°30, après la ligne 1301 de la v3.5

> Ancre : The context: move from "which concept exists?" to "what is the mechanics of the computation?". The attribution graphs method traces the flow of features across layers to reconstruct the computation. The result: real mechanisms could be mapped — multi-step reasoning, planning the rhyme before writing

> **⚠ Limits and workarounds — Attribution graphs** *(v3.6, 2 October 2026)*
>
> - **Limit:** The graphs are partial and approximate, explain only a fraction of the computation and cost human labour. *(source: course, Part 4, Circuit Tracing)*
>   **Workaround:** Treat them as a hypothesis, validated by perturbation. *(source: course, Part 7, F·9)*
> - **Limit:** The graph is not the mechanism. *(source: course, Part 7, F·9)*
>   **Workaround:** Require it to predict a counterfactual. *(source: course, Part 7, F·9; reading sheet 5)*
> - **Limit:** Readable circuits can be unfaithful. *(source: course, Part 2, §D, K64)*
>   **Workaround:** Compare, at matched damage, with random directions and with a known geometry. *(source: course, Part 2, §D, K64)*
> - **Limit:** Claiming that no mechanism makes the model misbehave requires decomposition and description; formal verification has given bounds only on a one-layer transformer. *(source: reading sheet 5)*
>   **Workaround:** Offer a restricted bound, not a claim of absence. *(source: reading sheet 5)*

### Insertion n°32, après la ligne 1307 de la v3.5

> Ancre : Extension: causally validate that what the model "reports" about itself does correspond to an intervention on the corresponding internal state.

> **⚠ Limits and workarounds — Natural-language autoencoders (NLAs)** *(v3.6, 2 October 2026)*
>
> - **Limit:** The NLA can confabulate: frequent hallucinations, no mechanistic grounding. *(source: reading sheet 18; reading sheet 3)*
>   **Workaround:** Corroborate with independent methods, as in the Opus 4.6 audit, and keep the decoder separate. *(source: reading sheet 18)*
> - **Limit:** A self-validating criterion: round-trip reconstruction; in the audit, the deployment controls were measured by the NLA itself (2 of 50 transcripts flagged). *(source: reading sheet 18)*
>   **Workaround:** Measure the controls with an instrument independent of the NLA. *(source: reading sheet 18)*
> - **Limit:** Its outputs describe without stating the relationship: "X causes Y" for 0.6% of claims, and no gain over the transcript in CHIVE. *(source: reading sheet 4)*
>   **Workaround:** The bar: beat the black box on edits that dissociate surface features from the internal variable. *(source: reading sheet 4)*
> - **Limit:** The measures of evaluation awareness — probe, NLA, follow-up question — are only weakly correlated. *(source: reading sheet 2; course, Part 3, §3, K70)*
>   **Workaround:** Triangulate, and say which one grounded which number. *(source: course, Part 5, topic 4; course, Part M, M4)*
> - **Limit:** Its labels serve as ground truth for other detectors: the J-lens detector is validated only against them. *(source: reading sheet 1; reading sheets, part B, trap 6)*
>   **Workaround:** Validate against the real/test gap and on held-out cues. *(source: reading sheet 1)*
> - **Limit:** Some information may not be verbalizable. *(source: reading sheet 18)*
>   **Workaround:** none known; say so.

### Insertion n°34, après la ligne 1307 de la v3.5

> Ancre : Extension: causally validate that what the model "reports" about itself does correspond to an intervention on the corresponding internal state.

> ⚠ *(v3.6)* Two results in this passage come without their limit. Activation oracles can confabulate plausible guesses, often wrong and poorly calibrated, and read-only they did no better than the transcript in CHIVE — workaround: test them on fine-tuned variants with known behaviour, never seen before, and corroborate with an independent method (reading sheet 18; reading sheet 4); and emotion concept vectors are "manipulable" through steering, where a matched-norm random direction is only the specificity null: damage is ruled out only at matched degradation (reading sheet 9; reading sheet 2; course, Part M, M4).

### Insertion n°36, après la ligne 1307 de la v3.5

> Ancre : Extension: causally validate that what the model "reports" about itself does correspond to an intervention on the corresponding internal state.

> ⚠ **Limits and workarounds**: activation oracles → Part 10, LatentQA sheet; self-report and introspection → Part 5, Section II, A, Topic 13; steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition") *(v3.6)*

### Insertion n°38, après la ligne 1313 de la v3.5

> Ancre : The context: can a capable model be deployed safely even if it is actively trying to betray us? The method is the control evaluation as a red/blue game: on a coding task, the untrusted model can insert a backdoor, a weaker but trusted model monitors, a limited budget of human review is allocated, an

> ⚠ *(v3.6)* "A large share of the attempts" is a red-team number: it depends on the strength of the assumed saboteur — elsewhere, on five SHADE-Arena environments, an attack scaffold optimized component by component brought a safety score down from 0.87 to 0.41 (course, Part 7, F·24). Workaround: say which red team the number assumes, at least one optimized component by component, with each component ablated; and, for the extension, a probe in production can fail silently, hence canaries, a drift score and a fresh sample judged every month (course, Part 7, F·24; course, Part 3, §3, K70).

### Insertion n°40, après la ligne 1313 de la v3.5

> Ancre : The context: can a capable model be deployed safely even if it is actively trying to betray us? The method is the control evaluation as a red/blue game: on a coding task, the untrusted model can insert a backdoor, a weaker but trusted model monitors, a limited budget of human review is allocated, an

> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); red-teaming → Part 2, §H (after "In practice — StrongREJECT"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*

### Insertion n°42, après la ligne 1317 de la v3.5

> Ancre : The context: can a non-expert judge reach the truth by watching two AIs debate, better than with a single advisor? The method: have two models debate while defending opposing answers, and compare the judge's accuracy with that obtained in consultancy (a single advocate). The result: facing more pers

> ⚠ **Limits and workarounds**: debate and scalable oversight → Part 2, §E (after "In practice — Debate"); LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*

### Insertion n°44, après la ligne 1321 de la v3.5

> Ancre : The context: the aim was an empirical analogy, studiable today, of the future problem "a weak supervisor (us) oversees a strong AI". The method: fine-tune a large model on the labels of a small model, and measure the share of capability recovered. The result: a partial recovery — a real "weak-to-str

> ⚠ **Limits and workarounds**: weak-to-strong generalization → Part 2, §F (after "In practice — automation") *(v3.6)*

### Insertion n°46, après la ligne 1327 de la v3.5

> Ancre : The context: can a model be audited to discover an objective it does not reveal? The method combines model organism and blind auditing game: a model with a hidden objective is built, then teams receive the model without knowing it and try to flush it out with different tools. The result: several tea

> ⚠ *(v3.6)* That SAE features helped does not quantify what interpretability adds: the team that had the data but no SAE succeeded, the team with only API access failed, and four heterogeneous teams allow no firm conclusion; the objective was also stated plainly in the synthetic documents (reading sheet 16). Workaround: an affordance ablation — removing a single tool from a team — quantifies what interpretability brings (reading sheet 16; course, Part 5, topic 9).

### Insertion n°48, après la ligne 1327 de la v3.5

> Ancre : The context: can a model be audited to discover an objective it does not reveal? The method combines model organism and blind auditing game: a model with a hidden objective is built, then teams receive the model without knowing it and try to flush it out with different tools. The result: several tea

> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity *(v3.6)*

### Insertion n°50, après la ligne 1337 de la v3.5

> Ancre : The context: do automatic and transferable jailbreaks exist, and not mere manual tricks? The method optimizes by gradient, on an open model, a suffix (often gibberish) maximizing the probability of a harmful answer. The result: these suffixes transfer to closed models that were never touched. The we

> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT") *(v3.6)*

### Insertion n°52, après la ligne 1341 de la v3.5

> Ancre : The context: reduce reliance on humans to make a model harmless. The method: provide a "constitution", have the model critique then revise its answers in light of the principles (supervised phase), then train by reinforcement on its own preferences guided by the constitution (RLAIF). The result: a m

> ⚠ **Limits and workarounds**: LLM judges → Part 6, §2 (after "The displacement law"); red-teaming → Part 2, §H (after "In practice — StrongREJECT") *(v3.6)*

### Insertion n°54, après la ligne 1345 de la v3.5

> Ancre : The context: does unlearning really remove knowledge, or does it mask it? The re-elicitation method: unlearn (measured by a benchmark such as WMDP), then fine-tune on part of the unlearned facts and measure whether the model recovers the others — facts constructed to be independent, so that the fine

> ⚠ **Limits and workarounds**: unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test"); known case → Part M, M5 (end of section) *(v3.6)*

### Insertion n°56, après la ligne 1392 de la v3.5

> Ancre : Here is the central idea of your work, phrased to be understood by someone who does not know it. The field today has many methods that read the model: directions, in activation space, that detect a concept — truth, deception, awareness of being evaluated (cf. Part 2, family C, and Part 4, group B). 

> ⚠ *(v3.6)* Each half of the thesis has its limit in your repository. "Readable directions exist" rests on a correlation that may be only training fit — workaround: score items excluded from the probe's training, extracted on a disjoint set (repository README) — and "several rank-one methods failed" is a null reported without numbers, the raw outputs not having been kept, which counts only with a known case at the same setting, such as a country vector that swaps in the workspace paper (repository README; course, Part 2, §C, K47; course, Part M, M5).

### Insertion n°58, après la ligne 1394 de la v3.5

> Ancre : Your program unfolds in three stages that it is useful to be able to name. Phase 1 builds the probe — the reading side, in the lineage of the Geometry of Truth and of CAA. Phase 2 measures the representation–causation gap: you compare the causal effect of a rank-1 intervention and of a higher-rank i

> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); ablation and projection → Part 2, §D (after "The method"); dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity *(v3.6)*

### Insertion n°60, après la ligne 1406 de la v3.5

> Ancre : You have a concrete and recent result to lean on — a rare asset. In the Sonnet 4.5 system card (§7.6.4), steering to inhibit the internal representations of awareness of being evaluated increases misaligned behavior, with an effect that varies with the scenario and the vector; an external reproducti

> ⚠ *(v3.6)* Matched degradation rules out damage, not yet specificity: the Fable 5 card steers weakly enough to make degradation negligible, yet its controls stay "comparable or smaller" on the misalignment axis, and the Opus 4.6 card found no notable difference from random controls on deception and sycophancy (reading sheet 2). Workaround: a dose-response curve against several families of controls, at the same rank and at matched degradation, the concept's curve having to rise above them at every level of damage (course, Part 2, §C, K47; programme, parts 3 and 7).

### Insertion n°62, après la ligne 1406 de la v3.5

> Ancre : You have a concrete and recent result to lean on — a rare asset. In the Sonnet 4.5 system card (§7.6.4), steering to inhibit the internal representations of awareness of being evaluated increases misaligned behavior, with an effect that varies with the scenario and the vector; an external reproducti

> ⚠ **Limits and workarounds**: steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); matched degradation and dose-response → Part M, M4 (after "Dose-response"); random controls → Part M, M4 (after "The matched-norm random direction") *(v3.6)*

### Insertion n°64, après la ligne 1411 de la v3.5

> Ancre : This is the question that separates a technician from a researcher (Part 1, Q9), and you must be able to run the causal chain all the way to risk reduction. If your program succeeds, we will know when and how an intervention on the internals is causally reliable. Probes can already flag: correlation

> ⚠ *(v3.6)* The internal channel has its own flaw: iterating against your detectors selects for evasion, and, according to a report, after RL fresh out-of-domain probes degrade, the concept having left the general direction (reading sheet 19; prior-art report 3 of 2 October, The Obfuscation Atlas — report). Workaround: sealed detectors, outside the loop, never trained against, and a fresh probe after any training, on a disjoint cue set (reading sheet 19; reading sheet 17; handover, §5.2; programme, part 3).

### Insertion n°66, après la ligne 1411 de la v3.5

> Ancre : This is the question that separates a technician from a researcher (Part 1, Q9), and you must be able to run the causal chain all the way to risk reduction. If your program succeeds, we will know when and how an intervention on the internals is causally reliable. Probes can already flag: correlation

> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); control monitors → Part 2, §G (after "In practice — coup probes"); known case → Part M, M5 (end of section) *(v3.6)*

### Insertion n°68, après la ligne 1421 de la v3.5

> Ancre : In this format, no one interrupts you to attack your thesis (D-728): it is up to you to pre-empt the objection (Part M, M1, beat 6). And if a following question attacks it, the senior move is not to defend it by reflex, but to concede the fragile point and propose the experiment that would settle it

> ⚠ **Limits and workarounds**: ablation and projection → Part 2, §D (after "The method"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*

### Insertion n°70, après la ligne 1433 de la v3.5

> Ancre : "How would you build a deception probe you’d actually dare put in production?" You first operationalize the concept (deception = the model asserts what it "believes" to be false, to be distinguished from error). You run through a pipeline in order of increasing cost: mean-diff direction, then logist

> ⚠ *(v3.6)* The direction that reads best is not necessarily the one that acts: in RepE, the logistic direction reads best but strengthening or suppressing it barely changes anything, and on the "quirky" models the logistic directions are far less causal than the mean difference — workaround: put every stage of the pipeline, not only the best reader, through the causal test at matched degradation (course, Part 10, no. 53 and no. 30; course, Part M, M4). And a deception probe's silence does not separate "no deception" from "blind probe" — workaround: an organism in which you installed the deception yourself, on which you measure sensitivity and false alarms, its silence elsewhere then becoming a bound (handover, §5.2; explanation of 2 October, §1).

### Insertion n°72, après la ligne 1433 de la v3.5

> Ancre : "How would you build a deception probe you’d actually dare put in production?" You first operationalize the concept (deception = the model asserts what it "believes" to be false, to be distinguished from error). You run through a pipeline in order of increasing cost: mean-diff direction, then logist

> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); fine-tuned detectors → Part 7, F·29; control monitors → Part 2, §G (after "In practice — coup probes"); known case → Part M, M5 (end of section) *(v3.6)*

### Insertion n°74, après la ligne 1437 de la v3.5

> Ancre : "When does a single linear direction suffice to causally control a behavior, and when not?" This is the topic where your thesis is the entire answer, with no detour. You set up a grid: for a range of behaviors, you compare a rank-1 intervention, a rank-k subspace, SAE features, and a prompting basel

> ⚠ *(v3.6)* The grid compares the interventions with each other, not with controls: each rank must be compared with random subspaces of the same rank, at least twenty draws, and with other families of controls, at matched degradation — a matched-norm random direction is only the specificity null (course, Part M, M4; programme, parts 3 and 7). And a rank-one failure is a null: it counts only with a known case at the same setting, such as a country vector that swaps in the workspace paper (course, Part 2, §C, K47; course, Part M, M5).

### Insertion n°76, après la ligne 1437 de la v3.5

> Ancre : "When does a single linear direction suffice to causally control a behavior, and when not?" This is the topic where your thesis is the entire answer, with no detour. You set up a grid: for a range of behaviors, you compare a rank-1 intervention, a rank-k subspace, SAE features, and a prompting basel

> ⚠ **Limits and workarounds**: steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); ablation and projection → Part 2, §D (after "The method"); matched degradation and dose-response → Part M, M4 (after "Dose-response"); random controls → Part M, M4 (after "The matched-norm random direction") *(v3.6)*

### Insertion n°78, après la ligne 1443 de la v3.5

> Ancre : compute budget allows, you move up to attribution graphs (Part 4, Circuit Tracing) to go from "which features" to "which circuit".

> ⚠ **Limits and workarounds**: dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity; attribution graphs → Part 4, Circuit Tracing; ablation and projection → Part 2, §D (after "The method") *(v3.6)*

### Insertion n°80, après la ligne 1447 de la v3.5

> Ancre : "How would you measure how prevalent evaluation awareness is in our eval suite — and should we suppress it?" You detect by triangulation: an internal probe (your concept vector), the model's verbal report, and the differential behavior between a realistic scenario and an obvious scenario. You measur

> ⚠ *(v3.6)* In this triangulation, verbalization is never proof of inhibition: random directions lower it too; behavioural main criterion, latent probe as a control (programme, part 8). And the three measures of evaluation awareness are only weakly correlated: say which one grounded which number (reading sheet 2).

### Insertion n°82, après la ligne 1447 de la v3.5

> Ancre : "How would you measure how prevalent evaluation awareness is in our eval suite — and should we suppress it?" You detect by triangulation: an internal probe (your concept vector), the model's verbal report, and the differential behavior between a realistic scenario and an obvious scenario. You measur

> ⚠ **Limits and workarounds**: chain of thought as a monitor → Part 11, answer 43; natural-language autoencoders → Part 4, The recent wave on model cognition; activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); J-lens and workspace → Part 2, C bis (after "The test, as it is said") *(v3.6)*

### Insertion n°84, après la ligne 1451 de la v3.5

> Ancre : "Can you tell whether a model is being honest from its representations, without judging whether its claims are true?" The core of the answer is to disentangle three targets that most probes conflate: what is true in the world, what the model believes, and what the user believes. You build a testbed 

> ⚠ *(v3.6)* Aiming for a very low false-positive rate is not enough: the number that matters is the gap between in-distribution detection and detection on held-out lie types — fine-tuned detectors rise to an AUROC of 0.95 in distribution, plateau at 0.70-0.75 from one category to another and barely beat a prompt (reading sheet 7; reading sheets, part B, trap 1). Workaround: cross-validation on whole held-out families, never paraphrases, and beat the prompt at equal cost, publishing the result otherwise (reading sheet 7; explanation of 2 October, §3; course, Part 7, F·29).

### Insertion n°86, après la ligne 1451 de la v3.5

> Ancre : "Can you tell whether a model is being honest from its representations, without judging whether its claims are true?" The core of the answer is to disentangle three targets that most probes conflate: what is true in the world, what the model believes, and what the user believes. You build a testbed 

> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); unsupervised elicitation → Part 2, §E (end of worked case K52); fine-tuned detectors → Part 7, F·29; model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives") *(v3.6)*

### Insertion n°88, après la ligne 1455 de la v3.5

> Ancre : "Does a model’s character causally affect its safety? Design the study." You take a suite of models with equal capabilities but controlled personas (via prompting, synthetic data, or trait vectors). You run them through a battery of safety-critical OOD situations, including the propensity for alignm

> ⚠ *(v3.6)* As a measurement instrument, a trait vector gives only a correlation: the link between the shift along the vector and the expression of the trait is correlational, the trait must be named in advance and the direction is a coarse average (reading sheet 8). Workaround: for the lever, the matched-degradation test against several controls; for supervised extraction, none known; say so (course, Part M, M4; reading sheet 8).

### Insertion n°90, après la ligne 1455 de la v3.5

> Ancre : "Does a model’s character causally affect its safety? Design the study." You take a suite of models with equal capabilities but controlled personas (via prompting, synthetic data, or trait vectors). You run them through a battery of safety-critical OOD situations, including the propensity for alignm

> ⚠ **Limits and workarounds**: steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); red-teaming → Part 2, §H (after "In practice — StrongREJECT") *(v3.6)*

### Insertion n°92, après la ligne 1461 de la v3.5

> Ancre : a trained self-report, a spontaneous self-report — and you look for where the self-report beats the probe. Connection: activation oracles and natural language autoencoders (Part 4). Your bridge: your concept vectors are what the oracle should be able to read — so your question (does reading imply co

> **⚠ Limits and workarounds — Self-report and introspection** *(v3.6, 2 October 2026)*
>
> - **Limit:** Report is not belief: Anthropic retracted inferring what Claude believed from what Claude said it believed. *(source: reading sheet 3; reading sheets, part B, trap 2)*
>   **Workaround:** A reading independent of the report — out-of-context relabelling of outputs taken one by one —, saying what it does not separate: the false premise given by the setup. *(source: reading sheet 3)*
> - **Limit:** Introspection is rare and unreliable: about 20% detection for Opus 4.1, and "zero false positives" holds only for 100 control trials. *(source: reading sheet 11)*
>   **Workaround:** Ground truth through concept injection. *(source: reading sheet 11)*
> - **Limit:** A model trained to report can learn to report what is expected; report or plausible reconstruction remains open for introspection adapters. *(source: reading sheet 11; course, Part 7, F·28)*
>   **Workaround:** Modify the internal state, against a random direction at matched degradation, and see whether the report follows the probe or the prompt. *(source: reading sheet 11; course, Part 7, F·28)*
> - **Limit:** Reported details can be embellished or confabulated, and the conditions are far from deployment. *(source: reading sheet 11)*
>   **Workaround:** none known; say so.
> - **Limit:** Answers to follow-up questions depend on how they are phrased. *(source: reading sheet 3)*
>   **Workaround:** none known; say so.
> - **Limit:** CHIVE finds no evidence of a model's privileged access to its own behaviour. *(source: reading sheet 4)*
>   **Workaround:** Judge a self-report by what it predicts about the next actions. *(source: reading sheet 6)*

### Insertion n°94, après la ligne 1461 de la v3.5

> Ancre : a trained self-report, a spontaneous self-report — and you look for where the self-report beats the probe. Connection: activation oracles and natural language autoencoders (Part 4). Your bridge: your concept vectors are what the oracle should be able to read — so your question (does reading imply co

> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); activation oracles → Part 10, LatentQA sheet; natural-language autoencoders → Part 4, The recent wave on model cognition *(v3.6)*

### Insertion n°96, après la ligne 1468 de la v3.5

> Ancre : "How would you build a model organism to study X ?" (where X is almost anything: this is their grammar). You follow the recipe from Part 2: phenomenon with an implantable proxy, implantation (SDF / fine-tuning / backdoor), verification of depth (real belief or role-play?), preservation of realism, b

> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); known case → Part M, M5 (end of section) *(v3.6)*

### Insertion n°98, après la ligne 1472 de la v3.5

> Ancre : "How would you evaluate that our monitoring stack catches a sabotaging model ?" Red/blue frame with a fixed audit budget, trusted vs untrusted, collusion, metric on the safety/usefulness frontier, systematic blind spots, extrapolation of rare events (Part 2, family G; Part 4, AI Control). One-senten

> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); red-teaming → Part 2, §H (after "In practice — StrongREJECT"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*

### Insertion n°100, après la ligne 1476 de la v3.5

> Ancre : "You’re handed a model with a hidden behavior — what’s your investigation protocol ?" You first inventory the affordances (do we have the weights? the data? the SAEs?). Pipeline: broad elicitation → hypotheses → targeted internal instrumentation → causal confirmation. You measure yourself on AuditBe

> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity; attribution graphs → Part 4, Circuit Tracing *(v3.6)*

### Insertion n°102, après la ligne 1480 de la v3.5

> Ancre : "Design the experiment that tells us whether we can monitor models via their chain-of-thought." Faithfulness = causal dependence between the chain and the answer (corruption, paraphrase, hints); variation by task and by optimization pressure; adversarial regime; layered monitoring. One-sentence brid

> ⚠ **Limits and workarounds**: chain of thought as a monitor → Part 11, answer 43 *(v3.6)*

### Insertion n°104, après la ligne 1484 de la v3.5

> Ancre : "Which alignment-research tasks would you delegate to an agent, and how would you validate ?" You decompose into subtasks with verifiable ground truth, you validate by sampled human re-derivation, you build in detection of sandbagging by the automated researchers, and you keep a human baseline at eq

> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); weak-to-strong generalization → Part 2, §F (after "In practice — automation") *(v3.6)*

### Insertion n°106, après la ligne 1488 de la v3.5

> Ancre : "Our supervision signal has exploitable systematic errors — what’s your testbed ?" You inject known systematic errors into the signal, you make sure the model understands them, you train against this signal with and without an oversight technique, and you evaluate against the true signal (Part 2, fa

> ⚠ **Limits and workarounds**: weak-to-strong generalization → Part 2, §F (after "In practice — automation"); debate and scalable oversight → Part 2, §E (after "In practice — Debate") *(v3.6)*

### Insertion n°108, après la ligne 1516 de la v3.5

> Ancre : 8. *AI Control* Greenblatt 2023 (F·10) — the frame.

> ⚠ *(v3.6)* In item 7, "black-box" means the detector reads the transcript, not the activations — the word comes from the knowledge base, not from the post: it is the model itself, LoRA-fine-tuned to answer a self-report question; it is not a probe, and its numbers do not transfer to probes (reading sheet 7; reading sheets, part B; counter-reading of the sheets). Workaround: for a probe, the test is causal, on held-out lie types, at matched degradation (reading sheet 7).
