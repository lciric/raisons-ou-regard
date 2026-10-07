# Insertions appliquées — volet7_B_et_D — EN

### Insertion n°2, après la ligne 1834 de la v3.5

> Ancre : proxy — "*our method for finding these prompts relies on potentially unrealistic affordances*".

> ⚠ *(v3.6)* "Withstands full red-teaming" is the null of a red team: it holds only at the budget and strength of the attack tried *(source: course, Part M, M7; course, Part 7, F·24)*; and it is read off an LLM judge's score, the "ground truth" being itself a model, with no human audit reported *(source: course, Part 7, F·22; reading sheets, part B, trap 6)*. Workaround: an attack budget fixed in advance and reported with the result, a red team optimized component by component, and a stratified human audit that bounds the judge's error — the proxy "with humans in the loop" they leave open *(source: course, Part M, M7; course, Part 7, F·24; programme, part 3; course, Part 7, F·22)*.

### Insertion n°4, après la ligne 1853 de la v3.5

> Ancre : frontier?* · *Why did the Goodharting frontier collapse?* · *What affordance made the blue prompt unrealistic, and how would you replace it?*

> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); LLM judges → Part 6, §2 (after "The displacement law"); red-teaming → Part 2, §H (after "In practice — StrongREJECT") *(v3.6)*

### Insertion n°6, après la ligne 1892 de la v3.5

> Ancre : *Which blind spots would an internal signal share?*

> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*

### Insertion n°8, après la ligne 1916 de la v3.5

> Ancre : your gate assume?*

> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT"); control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*

### Insertion n°10, après la ligne 1935 de la v3.5

> Ancre : misalignment) and this metric measure the same risk from two ends. And for your benchmark: publish its realism win rate.

> ⚠ *(v3.6)* The internal result recalled here comes from steering, and it is weak support: control vectors with arbitrary content move behaviour in the same direction, more weakly, and every steered direction degrades the outputs *(source: reading sheet 2; reading sheets, part C; course, Part 5, Section I, §3)*. Workaround: a specific subspace against random subspaces of the same rank, compared at matched degradation, with a dose-response curve; the matched-norm random direction is only the specificity null *(source: reading sheet 2; course, Part M, M4)*.

### Insertion n°12, après la ligne 1940 de la v3.5

> Ancre : awareness).

> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); LLM judges → Part 6, §2 (after "The displacement law"); chain of thought as a monitor → Part 11, answer 43; steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition") *(v3.6)*

### Insertion n°14, après la ligne 1961 de la v3.5

> Ancre : know before defending yours.

> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition") *(v3.6)*

### Insertion n°16, après la ligne 1972 de la v3.5

> Ancre : than a prompt?*

> **⚠ Limits and workarounds — Fine-tuned detectors (lie detectors)** *(v3.6, 2 October 2026)*
>
> - **Limit:** Out of distribution, AUROC plateaus at 0.70-0.75 and barely beats a prompt. *(source: reading sheet 7)*
>   **Workaround:** Cross-validation by held-out lie types; beat the prompt, and publish otherwise. *(source: reading sheet 7; course, Part 7, F·29)*
> - **Limit:** These are not probes: the model is LoRA-fine-tuned to judge its own transcript. *(source: reading sheet 7; explanation of 2 October, §2)*
>   **Workaround:** Do not transfer their numbers to probes; for a probe, the test is causal, on held-out types, at matched degradation. *(source: reading sheet 7)*
> - **Limit:** Noisy labels: about 25% revised at the cleaning pass, after a GPT-5 judge. *(source: reading sheet 7)*
>   **Workaround:** Say "revised", and bound the error with a human audit. *(source: reading sheet 7; programme, part 3)*
> - **Limit:** They score only assertions: a model can hide a lot without asserting anything false. *(source: course, Part 7, F·29)*
>   **Workaround:** none known; say so.
> - **Limit:** What they learned remains a hypothesis: "lying isn't one thing", and three rival readings remain. *(source: reading sheet 7)*
>   **Workaround:** Test the rival readings on held-out types. *(source: reading sheet 7)*
> - **Limit:** LoRA, five epochs, Gemma and Qwen only, controlled settings: nothing on deception in deployment. *(source: reading sheet 7)*
>   **Workaround:** none known; say so.

### Insertion n°18, après la ligne 1996 de la v3.5

> Ancre : an LLM behavior classifier not validated against humans.

> ⚠ *(v3.6)* This "no uplift" is the null of three read-only tools, on simple behaviours and for the edits tested: the attainable ceiling remains unknown, and an instrument's null counts only with its known case *(source: reading sheet 4; course, Part M, M5)*. Workaround: the bar set by reading sheet 4, beating the black box on edits that dissociate surface features from the internal variable; for a decoder, a test on fine-tuned variants with known behaviour, never seen before; and a human audit that bounds the classifier's error *(source: reading sheet 4; reading sheet 18; programme, part 3)*.

### Insertion n°20, après la ligne 2006 de la v3.5

> Ancre : **Likely questions.** *Why counterfactual simulatability?* · *Why read-only tools?* · *What would an uplift have looked like?*

> ⚠ **Limits and workarounds**: natural-language autoencoders → Part 4, The recent wave on model cognition; activation oracles → Part 10, LatentQA sheet; dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity; self-report and introspection → Part 5, Section II, A, Topic 13; LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*

### Insertion n°22, après la ligne 2039 de la v3.5

> Ancre : **Likely questions.** *Why does the cheese experiment matter?* · *Why is the gain OOD only?* · *What would break it?*

> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); held-out set → Part M, M4 (after "The held-out set") *(v3.6)*

### Insertion n°24, après la ligne 2056 de la v3.5

> Ancre : of damaging obedience to the system prompt. The *preventative steering* of Persona Vectors is the vector version of it.

> ⚠ *(v3.6)* "Not learned" is read here from behaviour, under normal prompts: according to an external work, inoculation can also mask a misalignment that returns under a frame close to training *(source: reading sheets, part C)*. Workaround: measure out of distribution, on held-out metrics, and check from the inside that the representation changed, not only the behaviour *(source: reading sheets, part C)*.

### Insertion n°26, après la ligne 2059 de la v3.5

> Ancre : — and that is exactly what Chen et al. do with persona vectors (F·31). The two papers answer each other: say so.

> ⚠ *(v3.6)* This test compares a direction across two trainings, yet training changes the representations: a probe calibrated on one arm would read differently in the other, and that measurement bias would be confounded with the effect sought *(source: handover, §5.2)*. Workaround: one probe per arm and a fresh probe after training, on a disjoint cue set, kept as a separate measure; and, to say that the direction acts, the causal test at matched degradation *(source: handover, §5.2; programme, part 3; course, Part M, M4)*.

### Insertion n°28, après la ligne 2064 de la v3.5

> Ancre : **Likely questions.** *Why would asking for it prevent learning it?* · *How do you pick the prompt?* (the heuristic) · *What does it cost?*

> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*

### Insertion n°30, après la ligne 2080 de la v3.5

> Ancre : behaves differently (vector close to zero); a public criticism: at coefficient 1.0 on "evil", MMLU goes from ~58 to ~50%.

> ⚠ *(v3.6)* The shift-to-trait link is correlational, the trait must be named in advance and the evaluation is light (reading sheet 8): for causality, the matched-degradation test (course, Part M, M4). And steering away from a persona during training reportedly doubled the spread of misalignment (prior-art report 3 of 2 October — report, unverified).

### Insertion n°32, après la ligne 2085 de la v3.5

> Ancre : random direction carry?*" — that is your partition, and you have the number at home (< 1% versus 68%).

> ⚠ *(v3.6)* "MMLU preserved" rules out damage only on that composite, and the covariance-matched random direction in your question is, like any control direction, only a specificity null *(source: programme, parts 3 and 8; course, Part 11, answer A7)*. Workaround: compare the arms at equal degradation, on a composite built from the trait's expected damage, and say which random control grounded which number *(source: course, Part 11, answer A7; programme, parts 3 and 7; course, Part 6, §3)*.

### Insertion n°34, après la ligne 2091 de la v3.5

> Ancre : **Likely questions.** *Why does preventative steering cost less than post-hoc?* · *Does the read direction carry the causal effect?*

> ⚠ **Limits and workarounds**: steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); random controls → Part M, M4 (after "The matched-norm random direction"); matched degradation and dose-response → Part M, M4 (after "Dose-response") *(v3.6)*

### Insertion n°36, après la ligne 2118 de la v3.5

> Ancre : **Likely questions.** *Why does it need a shared base?* (the theorem) · *What does it imply for many copies of one model?* (your H4).

> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives") *(v3.6)*

### Insertion n°38, après la ligne 2134 de la v3.5

> Ancre : evaluation awareness question; and it is the eval on which MSM measured 68 → 5%.

> ⚠ *(v3.6)* These rates are measures of conduct in constructed scenes: the study recorded less misbehaviour when the models said they were being evaluated, but unspoken awareness escapes it, and in a simulation "this is fake" is true *(source: course, Part 2, §B, K63; reading sheets, part B; reading sheet 3)*. Workaround: two versions of an environment, randomly assigned, differing only in realism cues, awareness read by a probe and from the model's words, and an organism trained to hide as the known case; against the simulation confound, none known; say so *(source: course, Part 2, §B, K63; reading sheet 3)*.

### Insertion n°40, après la ligne 2134 de la v3.5

> Ancre : evaluation awareness question; and it is the eval on which MSM measured 68 → 5%.

> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives") *(v3.6)*

### Insertion n°42, après la ligne 2142 de la v3.5

> Ancre : falling ethics score.

> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging") *(v3.6)*

### Insertion n°44, après la ligne 2151 de la v3.5

> Ancre : control — the same discipline as your partition.

> ⚠ **Limits and workarounds**: self-report and introspection → Part 5, Section II, A, Topic 13; model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives") *(v3.6)*

### Insertion n°46, après la ligne 2157 de la v3.5

> Ancre : access question (weights, data, activations) is the one you will be asked.

> ⚠ *(v3.6)* A discovery rate on implanted behaviours bounds the auditor without proving the natural case: an implanted behaviour may be more salient than a natural one, and in the audit that AuditBench follows on from, the objective was stated plainly in the synthetic documents *(source: handover, §5.2; course, Part M, M5; reading sheet 16)*. Partial workaround: plant the same behaviour through several recipes, hold one out, and add another team's organism; for the access question, removing one tool from an audit team measures what it adds; against the gap between implanted and natural itself, none known; say so *(source: course, Part 2, §A, K71; reading sheet 16; course, Part M, M5)*.

### Insertion n°48, après la ligne 2157 de la v3.5

> Ancre : access question (weights, data, activations) is the one you will be asked.

> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); known case → Part M, M5 (end of section) *(v3.6)*

### Insertion n°50, après la ligne 2163 de la v3.5

> Ancre : on "prevent bad actors".

> ⚠ **Limits and workarounds**: safety classifiers → Part 2, §H (end of worked case G1); red-teaming → Part 2, §H (after "In practice — StrongREJECT") *(v3.6)*

### Insertion n°52, après la ligne 2169 de la v3.5

> Ancre : you.** The most solid answer to "truly unlearned" — with your probe test on top.

> ⚠ *(v3.6)* Selective gradient masking is shown only on small models *(source: course, Part 2, §I, JB10)*; and your probe test does not decide on its own: on an unlearned model, probes fail while it can still be jailbroken, and a reading sees nothing while removing a direction restores the capability *(source: course, Part 10, Deeb and Roger; course, Part 10, Łucki et al.)*. Workaround: decide by an intervention, never by a reading — re-elicitation at a budget fixed in advance against a never-trained reference, reported as a bound; for model size, none known; say so *(source: course, Part 10, Łucki et al.; course, Part 2, §I, JB10; course, Part M, M7)*.

### Insertion n°54, après la ligne 2169 de la v3.5

> Ancre : you.** The most solid answer to "truly unlearned" — with your probe test on top.

> ⚠ **Limits and workarounds**: unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*

### Insertion n°56, après la ligne 2178 de la v3.5

> Ancre : **Hypothesis (1).** Autonomous agents make real progress on an open alignment problem that is nonetheless **gradable by its outcome** (weak-to-strong). **Method.** Parallel teams of Claude agents propose, execute, iterate; metric = performance gap recovered (PGR) against a human baseline. **Figure.*

> ⚠ **Limits and workarounds**: weak-to-strong generalization → Part 2, §F (after "In practice — automation"); behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging") *(v3.6)*

### Insertion n°58, après la ligne 2181 de la v3.5

> Ancre : **Hypothesis.** Can models judge safety research proposals the way experienced researchers do? **Method.** 93 human proposals from fellows; researchers rate pairs with discussion and confidence filtering; model agreement. **Figures.** "*92 pairs, 77 % estimated human agreement*"; models "*60 %*". **

> ⚠ **Limits and workarounds**: LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*

### Insertion n°60, après la ligne 2184 de la v3.5

> Ancre : **Hypothesis.** An agent can fine-tune for safety while bounding false positives and degradation. **Figure.** "*10.2 % FPR for A3 vs 92 % FPR for random mixing while both achieving 0 % SFR*" (nesting jailbreak).

> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT") *(v3.6)*

### Insertion n°62, après la ligne 2187 de la v3.5

> Ancre : **Hypothesis.** When the supervisor cannot verify quality, training on a **weak but trusted** supervisor can still extract the best performance from a model that sandbags. **Method.** Organisms trained to underperform; SFT and/or RL on samples from a weak supervisor (4o-mini); math, GPQA, code. **Fi

> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); weak-to-strong generalization → Part 2, §F (after "In practice — automation"); model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives") *(v3.6)*

### Insertion n°64, après la ligne 2192 de la v3.5

> Ancre : **The argument.** A diffuse threat "*can't cause a catastrophe by behaving badly on just one occasion*"; it takes many malign actions, **and each one is weakly incriminating** (a bug, an idea not found: malice or error?). Hence two families of response: **training** (more effective when the bad acti

> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*

### Insertion n°66, après la ligne 2195 de la v3.5

> Ancre : **Hypothesis.** A malicious automated researcher can slow research down (sandbag ML experiments) or steer it (manipulate justifications), **without being detected by a zero-shot prompted monitor**. **Method.** Strong untrusted model as researcher (agentic setup of the Claude Code type); **monitors =

> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*

### Insertion n°68, après la ligne 2200 de la v3.5

> Ancre : **Result to know.** Asking the model to classify its own statements: AUROC 0.82 on average; the best detector (a model fine-tuned for honesty, prompted) 0.88; and "*truth probing, honesty steering, fuzzing, and fine-tuning to instill alternate honest personalities performed worse than simple prompti

> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); fine-tuned detectors → Part 7, F·29; steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition") *(v3.6)*
