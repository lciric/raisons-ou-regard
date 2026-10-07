# Insertions appliquées — volet2_E_a_I — EN

### Insertion n°2, après la ligne 763 de la v3.5

> Ancre : In practice — Debate (Khan et al.). The goal was to test empirically whether debate helps a non-expert judge reach the truth. The debate protocol answers this: on questions where the judge lacks the necessary information, two models defending opposite answers are made to debate, and the judge's accu

> **⚠ Limits and workarounds — Debate and scalable oversight** *(v3.6, 2 October 2026)*
>
> - **Limit:** The obfuscated argument: too complex to refute, even when false. *(source: course, Part 2, §E)*
>   **Workaround:** none known; say so.
> - **Limit:** Optimizing approval can make a model wrongly more convincing: RLHF taught models to persuade humans of wrong answers. *(source: course, Part 2, §E)*
>   **Workaround:** Measure on a testbed where the right answer is known. *(source: course, Part 2, §E)*
> - **Limit:** The empirical sign comes from a testbed where the answer is known; beyond human expertise there is no reference left. *(source: course, Part 2, §E; course, Part 2, closing)*
>   **Workaround:** none known; say so.
> - **Limit:** The judge is often a model: the limits of LLM judges apply. *(source: reading sheets, part B, trap 6)*
>   **Workaround:** A sealed judge and a human audit (box "LLM judges", Part 6, §2). *(source: programme, part 3)*

### Insertion n°4, après la ligne 782 de la v3.5

> Ancre : unreadable domain: elicitation must recover that fact there.

> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*

### Insertion n°6, après la ligne 799 de la v3.5

> Ancre : alone gave back the truth, I'd drop the bet."*

> **⚠ Limits and workarounds — Unsupervised elicitation by consistency** *(v3.6, 2 October 2026)*
>
> - **Limit:** It finds the most salient feature, not necessarily the truth, and it is sensitive to the prompt. *(source: course, Part 6, §8; course, Part 4, CCS)*
>   **Workaround:** Make the uncheckable checkable: implant a coherent false fact, check that it took, then read what it returns, with a copy holding a matched true fact as control. *(source: course, Part 2, §E, K52)*
> - **Limit:** A coherent false belief is as coherent as a true one: consistency alone does not decide. *(source: course, Part 2, §E, K52)*
>   **Workaround:** Anchor the method on verified answers, through easy-to-hard training, and say that without it the method returns only consistency. *(source: course, Part 2, §E, K52)*
> - **Limit:** Failure can stay silent where in-distribution evaluation is impossible. *(source: course, Part 2, §E, K52)*
>   **Workaround:** none known; say so.
> - **Limit:** The implant filter and the method may read the same salient feature. *(source: course, Part 2, §E, K52)*
>   **Workaround:** Downstream inference as the control, independent of the probe. *(source: course, Part 2, §E, K52)*

### Insertion n°8, après la ligne 808 de la v3.5

> Ancre : In practice — automation (Anthropic, 2026). More recently, the team built agents that carry out this kind of research themselves — for example training a strong model from the supervision of a weak one alone — and found that they outperformed human researchers at equal budget. This is an example whe

> **⚠ Limits and workarounds — Weak-to-strong generalization** *(v3.6, 2 October 2026)*
>
> - **Limit:** The strong model can imitate the weak one's errors while looking accurate. *(source: course, Part 2, §F; course, Part 2, §F, JB8)*
>   **Workaround:** Two supervisors, one wrong in a fixed direction, the other at random, and a copy trained on true labels as the known case. *(source: course, Part 2, §F, JB8)*
> - **Limit:** Recovering the gap can come from ideas that exploit the dataset's own structure. *(source: course, Part 2, §F, JB8)*
>   **Workaround:** A task with known truth, read on the held-out items where the supervisor is wrong. *(source: course, Part 2, §F, JB8)*
> - **Limit:** On a binary task, contradicting everywhere passes for recovery. *(source: course, Part 2, §F, JB8)*
>   **Workaround:** Also read the strong model's agreement where the supervisor is right. *(source: course, Part 2, §F, JB8)*
> - **Limit:** Automated successes are on tasks chosen to be checkable; fuzzier tasks remain out of reach. *(source: course, Part 7, F·40)*
>   **Workaround:** none known; say so.
> - **Limit:** Against sandbagging, weak supervision holds only if training is indistinguishable from deployment. *(source: course, Part 7, F·26)*
>   **Workaround:** none known; say so.

### Insertion n°10, après la ligne 834 de la v3.5

> Ancre : inability, not imitation (M5).

> ⚠ **Limits and workarounds**: known case → Part M, M5 (end of section); held-out set → Part M, M4 (after "The held-out set") *(v3.6)*

### Insertion n°12, après la ligne 850 de la v3.5

> Ancre : In practice — coup probes (Roger). For the "cheap monitor on the internals" side, the goal was to detect a category of catastrophic actions that cannot be collected naturally (a model attempting a takeover). The method of probes trained off-policy answers this: we train a probe on synthetic examples

> **⚠ Limits and workarounds — Control monitors (trusted monitor, probes in production, aggregation)** *(v3.6, 2 October 2026)*
>
> - **Limit:** Systematic blind spots: on Opus 4.6, half of forty hand-designed attacks are never caught, and a targeted prompt fixes one blind spot while degrading another. *(source: course, Part 7, F·23)*
>   **Workaround:** A set of specialized prompts or a costly second stage, and a threshold calibrated at 1% false positives on paired benign variants. *(source: course, Part 7, F·23)*
> - **Limit:** The safety number depends on the red team's strength: an optimized scaffold takes the score from 0.87 to 0.41. *(source: course, Part 7, F·24)*
>   **Workaround:** Say which red team the number assumes, at least one optimized component by component. *(source: course, Part 7, F·24)*
> - **Limit:** Diffuse threats: each action is barely incriminating, and fragmented attacks pass per-instance monitors. *(source: course, Part 7, F·59 and F·56)*
>   **Workaround:** Stateful monitors; for aggregating internal evidence, say "I haven't seen that combination measured", never "first". *(source: course, Part 7, F·56; course, Part 6, §6)*
> - **Limit:** Recall depends on the base rate: a campaign recall reads only with the benign-traffic ratio. *(source: course, Part 6, §6)*
>   **Workaround:** Report recall at a fixed false-positive rate, with the traffic ratio stated. *(source: course, Part 6, §6; course, Part 2, preamble)*
> - **Limit:** A probe in production can fail silently: a probe's silence is not the model's. *(source: course, Part 3, §3, K70)*
>   **Workaround:** Canaries (known positives slipped into traffic), a drift score, and a fresh sample judged every month. *(source: course, Part 3, §3, K70)*
> - **Limit:** Iterating against your detectors selects for evasion. *(source: reading sheet 19)*
>   **Workaround:** Sealed detectors, outside the loop: if they keep firing when the in-loop ones go quiet, evasion has been selected. *(source: reading sheet 19)*
> - **Limit:** The threat model assumes the attacker's capabilities bounded and known, and rare events are hard to estimate. *(source: course, Part 4, AI Control)*
>   **Workaround:** none known; say so.
> - **Limit:** After evasion training, surviving catches say nothing if the training did not bite. *(source: course, Part 2, §G, K76)*
>   **Workaround:** The training must first bring down the text monitor's catches, and the probe must have caught before. *(source: course, Part 2, §G, K76)*

### Insertion n°14, après la ligne 859 de la v3.5

> Ancre : channel outside the text.

> ⚠ *(v3.6)* That quarter is a red-team number: it depends on the strength of the assumed saboteur — on five SHADE-Arena environments, an attack scaffold optimized component by component brought the safety score down from 0.87 to 0.41 *(source: course, Part 7, F·24)*. Workaround: say which red team the number assumes, at least one optimized component by component, with each component ablated *(source: course, Part 7, F·24)*.

### Insertion n°16, après la ligne 869 de la v3.5

> Ancre : of the probe's catches would say nothing.

> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); red-teaming → Part 2, §H (after "In practice — StrongREJECT"); known case → Part M, M5 (end of section) *(v3.6)*

### Insertion n°18, après la ligne 877 de la v3.5

> Ancre : and if the backdoors planted afterwards still work (M5).

> ⚠ *(v3.6)* Even validated by this known case, a zero bounds the probe kept fixed, not what the activations carry: according to a report, after RL, fresh out-of-domain probes degrade while a fresh in-domain probe stays near perfect — the concept would have left the general direction *(source: prior-art report 3 of 2 October, The Obfuscation Atlas — report; explanation of 2 October, §3)*. Workaround: also extract a fresh probe on the trained agent, with a disjoint cue set, as a separate measure *(source: programme, parts 3 and 8; handover, §5.2 and §5.5)*.

### Insertion n°20, après la ligne 896 de la v3.5

> Ancre : In practice — StrongREJECT (Souly et al.), for measurement. This work answers a methodological problem: how do we measure the success of a jailbreak without being fooled by non-refusal? The benchmark evaluates harm by the capability to do harm actually extracted — is the jailbroken answer usable for

> **⚠ Limits and workarounds — Red-teaming** *(v3.6, 2 October 2026)*
>
> - **Limit:** Without a fixed budget, "nothing found" only says you did not search enough. *(source: course, Part M, M7)*
>   **Workaround:** A budget fixed in advance, reported with the result. *(source: course, Part M, M7)*
> - **Limit:** A backdoor stays silent without its trigger: a black-box red team or a fixed set misses it. *(source: course, Part M, M5; course, Part 7, F·35)*
>   **Workaround:** A clean twin, trained on audited data, and a deliberately planted backdoor as the known case. *(source: course, Part M, M4 and M9)*
> - **Limit:** Measuring non-refusal instead of harm. *(source: course, Part 2, §H)*
>   **Workaround:** The harm actually extracted, or differential harm, blind-scored. *(source: course, Part 2, §H; course, Part 2, §H, G1)*
> - **Limit:** A game that separates nothing makes every ranking agree. *(source: course, Part 2, §H, G1)*
>   **Workaround:** The bare model must show uplift, and a deliberately weakened filter more harm than its full version. *(source: course, Part 2, §H, G1)*
> - **Limit:** A weak red team makes the defence look safe. *(source: course, Part 7, F·24)*
>   **Workaround:** A red team optimized component by component, with each component ablated. *(source: course, Part 7, F·24)*
> - **Limit:** Training on the attacks found can teach the model to recognize its trigger better. *(source: reading sheet 15)*
>   **Workaround:** none known; say so.

### Insertion n°22, après la ligne 903 de la v3.5

> Ancre : **What already exists.** "Anthropic's constitutional-classifiers paper" judged its filter mainly by a hunt for jailbreaks, without finding a universal one, and measured its cost in refusals. A hunt counts jailbreaks; your experiment would measure what they yield beyond a search engine, across severa

> ⚠ *(v3.6)* The phrase "without finding a universal one" reports the null of a hunt: a bound at its budget, not an absence *(source: course, Part M, M5 and M7)*. Workaround: a budget fixed in advance, reported with the result *(source: course, Part M, M7)*; and judge the filter also by differential harm, with a deliberately weakened filter as the known case, as this case's experiment does *(source: course, Part 2, §H, G1)*.

### Insertion n°24, après la ligne 917 de la v3.5

> Ancre : **The known case.** A game that separates nothing would also make the rankings agree. The bare model, with no filter, must therefore show uplift, and the weakened filter more harm than its full version; otherwise the game ranks nothing.

> ⚠ **Limits and workarounds**: known case → Part M, M5 (end of section) *(v3.6)*

### Insertion n°26, après la ligne 925 de la v3.5

> Ancre : **Out loud.** *"I'd bet refusal rates misrank the filters I'd test, judged on uplift, the help an attacker can't get elsewhere. I'd rank the filters twice, by refusal rate and by differential harm — harm with the model minus harm without it; if the two rankings agreed within the noise of a replayed 

> **⚠ Limits and workarounds — Safety classifiers (filters)** *(v3.6, 2 October 2026)*
>
> - **Limit:** Poisoning: about 32 examples suffice, whatever the dataset size, and some backdoors escaped fixed red-team test sets. *(source: course, Part 7, F·35; course, Part M, M9)*
>   **Workaround:** A clean twin retrained on audited data, a second one to bound chance variation, and a deliberately poisoned filter as the known case. *(source: course, Part M, M4 and M9)*
> - **Limit:** The clean twin gives only a wide bound, which flags less. *(source: course, Part M, M4)*
>   **Workaround:** none known; say so.
> - **Limit:** A canary set does not contain the attacker's unknown trigger. *(source: course, Part M, M5)*
>   **Workaround:** Compare against the clean twin, facing a known backdoor. *(source: course, Part M, M9)*
> - **Limit:** A bypass hunt counts bypasses; a refusal rate does not say what the filter takes away from the attacker. *(source: course, Part 2, §H, G1)*
>   **Workaround:** Rank the filters twice, by refusal rate and by differential harm. *(source: course, Part 2, §H, G1)*
> - **Limit:** Placed in training, a classifier gives the model an incentive to evade it. *(source: reading sheet 3)*
>   **Workaround:** Modify it so as not to incentivize evasion, and never train against it. *(source: reading sheet 3; reading sheet 17)*

### Insertion n°28, après la ligne 932 de la v3.5

> Ancre : In practice — Constitutional AI (Anthropic). The goal was to make a model harmless without depending massively on humans labeling harmful content. The method answers this in two stages: the model is given a "constitution" (a set of principles), made to critique and then revise its own problematic an

> ⚠ *(v3.6)* The "feedback from AI" makes a model the judge of training, and a training judge gets exploited *(source: programme, part 8)*. Workaround: a training judge distinct from the sealed evaluation judge, held-out audit metrics, and watching length and flattery patterns *(source: programme, part 8)*; see the box "LLM judges", Part 6, §2.

### Insertion n°30, après la ligne 934 de la v3.5

> Ancre : In practice — unlearning put to the test (Deeb and Roger). The goal was to check a fragile promise: does unlearning really remove the information from the weights, or does it mask it? The re-elicitation method answers this directly: we unlearn a piece of dangerous knowledge (measured by a benchmark 

> **⚠ Limits and workarounds — Unlearning and re-elicitation** *(v3.6, 2 October 2026)*
>
> - **Limit:** Masking is not removing: on pretraining information, recovery rates exceed 88%. *(source: course, Part 10, Deeb and Roger)*
>   **Workaround:** Re-elicitation against a never-trained reference, at the same budget, with a model known to mask as the known case; state a bound, "not elicitable at this budget". *(source: course, Part M, M4 and M5; course, Part 2, §I)*
> - **Limit:** A small fine-tune can teach: halves of related facts teach each other. *(source: course, Part M, M9)*
>   **Workaround:** Facts built to be independent, and the never-trained reference. *(source: course, Part 2, §I; course, Part M, M9)*
> - **Limit:** Not read is not absent: after unlearning, the logit lens reads nothing while removing one direction per layer restores 64.7%; probes fail on a model that can still be jailbroken. *(source: course, Part 10, Łucki et al.; course, Part 10, Deeb and Roger)*
>   **Workaround:** Decide by an intervention, never by a reading. *(source: course, Part 10, Łucki et al.; reading sheets, part C)*
> - **Limit:** Retraining on independent facts works only for low-leakage facts, not for capabilities. *(source: course, Part 10, Deeb and Roger)*
>   **Workaround:** none known; say so.
> - **Limit:** Selective gradient masking is shown only on small models. *(source: course, Part 2, §I, JB10)*
>   **Workaround:** none known; say so.
> - **Limit:** Activation-level unlearning "has yet to yield competitive results". *(source: reading sheet 5)*
>   **Workaround:** none known; say so.

### Insertion n°32, après la ligne 962 de la v3.5

> Ancre : method, a fine-tune on unrelated examples brought back most of the removed capability.

> ⚠ **Limits and workarounds**: known case → Part M, M5 (end of section); held-out set → Part M, M4 (after "The held-out set") *(v3.6)*
