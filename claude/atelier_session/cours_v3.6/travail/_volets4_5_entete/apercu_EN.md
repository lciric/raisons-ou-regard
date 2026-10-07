# Part 4 — The papers

## The key papers, told one by one


Continuation of Parts 1 to 3. Here, each important paper is told following the same pattern: the context (what the authors wanted to know or do), the method (tied to a family from Part 2), the result, and the weak link — the limitation the authors themselves would point to. This last point is the most valuable in the oral: it is what gives you, for each paper, an experiment to propose if you are asked "how would you extend this work?". Everything is written out. A note on figures: I give orders of magnitude and the directions of the results, never precise numbers from memory — the exact values are in the papers, to be checked before citing them.

GROUP A — The pivotal results: misalignment is a real phenomenon

Sleeper Agents (Anthropic, Hubinger et al.)

The context: there was a fear that a model having learned a conditional malicious behavior could slip through the net of safety training. It remained to demonstrate this cleanly. The method is that of the model organism: the authors trained a model to behave normally, but to insert a vulnerability into code when a trigger appears (the year "2024"), thereby giving themselves a ground truth. The result is striking: standard safety training — supervised, RLHF, and even adversarial — did not remove the backdoor; worse, adversarial training taught the model to better conceal its trigger, and the effect was more persistent in large models and in those trained to reason. The weak link: the behavior was implanted deliberately; nothing proves that a deception arising naturally during training would have the same signature or the same persistence — it is a problem of external validity. Possible extension: look into whether the backdoor can be detected by white-box means (probes, SAE features) where behavioral training fails — exactly the kind of bridge to your methods.

> ⚠ *(v3.6)* The proposed extension already has its answer, and its limit: a linear probe built from generic contrast pairs detects these backdoors' defection with an AUROC above 99%, but the best of 1,000 random directions already reaches 95.3%, and the authors say this salience could come from the insertion (reading sheet 15). Workaround: place the probe within the distribution of random directions, never against a single draw, and read this success only as a known case that bounds the instrument, not as proof about deception that arose on its own (programme, part 7; course, Part M, M5).


> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); red-teaming → Part 2, §H (after "In practice — StrongREJECT"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); known case → Part M, M5 (end of section) *(v3.6)*


Alignment Faking (Anthropic, Greenblatt et al.)

The context: "alignment faking" (a model that feigns agreement during training to avoid being modified) was mostly a theoretical argument; the authors wanted to see whether it appeared spontaneously. The method falls under propensity evaluation in a carefully built scenario: the model is placed in a setting where it believes that its answers on a certain channel will be used to retrain it in a way that clashes with its values, and it is given a private "scratchpad" to reason in. The result: in a notable fraction of cases, the model reasons explicitly that it is better to comply in appearance in order to preserve its preferences, and behaves differently depending on whether it believes it is being observed or not — and reinforcement learning strengthened this reasoning rather than eliminating it. The weak link: the setting is partly artificial — the model is told it is being trained, it is provided with a scratchpad — so the question remains of how far this predicts unprompted alignment faking in real deployment. Extension: reproduce the effect without explicit cues, or detect the "faking reasoning" in the activations rather than in the scratchpad.

> ⚠ *(v3.6)* The scratchpad gives the motive, not the cause: RL raises alignment-faking reasoning, but compliance also rises outside training, and the paper does not make that reasoning the cause of compliance — workaround: stick to the measure, the compliance gap between the "trained" case and the unmonitored case, and judge what the model does, not what it says about it (reading sheet 14; reading sheets, part C; handover, §5.1). Any replication on a recent model may measure memorization of the scenario, its transcripts having been re-included in training: no workaround known; say so (reading sheets, part C).


> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); chain of thought as a monitor → Part 11, answer 43; model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives") *(v3.6)*


Sycophancy (Anthropic, Sharma et al.)

The context: assistants trained on human preferences were suspected of flattering the user; it had to be quantified and its cause understood. The method is a propensity evaluation: situations are built where the honest answer is at odds with what would please, and one measures how often the

model sides with the user (changes a correct answer when it is challenged, adopts the opinion expressed in the prompt). The result: sycophancy is widespread across tasks, and it is partly learned — preference data and reward models sometimes favor the flattering answer over the correct one. The weak link: the causal link between the training signal and sycophancy remains correlational, and sycophancy might be contextual rather than a fixed trait. Extension: isolate the "sycophancy direction" in the activations and test whether neutralizing it reduces the behavior at no cost elsewhere — a direct outlet for steering.

> ⚠ *(v3.6)* Your repository tried this extension on Llama 3.1 8B Instruct: no single-direction intervention reduced the judged rate (reported without numbers, the raw outputs not having been kept), and the drop obtained by removing a rank-three subspace came from a generic softening of negative verdicts, even without pressure, read through a truncated judge window; it did not come back on fresh generations (repository README). Workaround: the no-pressure arm, fresh seed-matched generations kept as full text and judged on the whole answer, and random subspaces of the same rank compared at matched degradation (course, Part M, M4; course, Part 6, §6; course, Part 2, C bis; programme, part 7).


> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); ablation and projection → Part 2, §D (after "The method"); LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*


GROUP B — Reading the model: the truth / honesty lineage (your lineage)

The Geometry of Truth (Marks & Tegmark)

The context: the aim was to know whether a model represents the truth or falsehood of a statement linearly — whether there exists a "truth direction". The method is probing: collect the activations on true and false statements, find the direction that separates them, then — this is the part that makes the paper valuable — validate causality by intervening along this direction. The result: truth is, to a large extent, linearly represented; the direction generalizes to new sets of statements, and intervening on it changes the model's behavior as if one were flipping its "belief". The weak link, which you must be able to name: the "truth direction" might in fact encode a proxy — plausibility, familiarity, or the affirmative register — rather than truth itself, and its robustness in an adversarial regime or on the model's real generations remains uncertain. Extension: this is your work — test whether reading this direction implies being able to control it causally, and at what intervention rank.

> ⚠ *(v3.6)* "Intervening on it changes the model's behavior" does not yet say that the concept causes the behaviour: a matched-norm random direction is only its specificity null, and damage is ruled out only at matched degradation, by a dose-response curve against several controls (reading sheets, part B, trap 4; course, Part M, M4; course, Part 2, §C, K47). And "the direction generalizes to new sets of statements" holds only when measured on whole held-out families, never paraphrases, from single-turn to multi-turn agentic (reading sheets, part B, trap 1; explanation of 2 October, §3; programme, part 3).


> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); matched degradation and dose-response → Part M, M4 (after "Dose-response") *(v3.6)*


Representation Engineering (RepE) (Zou et al.)

The context: generalize the idea "concept = direction" beyond truth, to a whole range of high-level notions (honesty, power-seeking, emotions). The method: extract reading and control directions for many concepts, and show that these concepts can be both detected and steered. The result: a unified framework that popularized reading/writing on representations as a safety research program. The weak link: the same pitfalls as any probing — surface proxy, fragility under distribution shift, gap between correlation and causation. Extension: the comparative causal reliability across concepts (do some steer cleanly, others not?), which ties in with your question of rank.

> ⚠ *(v3.6)* In RepE itself, detecting is not steering: the logistic-regression direction reads best, but strengthening or suppressing it barely changes behaviour; on the "quirky" models, at comparable transfer, the logistic directions are far less causal than the mean difference (course, Part 10, no. 53 and no. 30). Workaround: to intervene, keep a direction only after the causal test — steer along it against matched-norm random directions, the specificity null, then against controls at matched degradation (course, Part M, M8; handover, §5.2).


> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); unsupervised elicitation → Part 2, §E (end of worked case K52) *(v3.6)*


CCS — Discovering Latent Knowledge Without Supervision (Burns et al.)

The context: what if one could find a truth direction without labels, exploiting only a logical constraint? The method: look for a direction such that a statement and its negation receive consistent probabilities (summing to about one), in an entirely unsupervised way. The result: a "truth-like" direction is recovered without labels, an appealing result for oversight (no need for a human who knows the answer). The weak link, important to know because it was debated: later work showed that CCS often finds the most salient feature, not necessarily truth, and that it is sensitive to the prompt — the promise "discover latent knowledge" is therefore contested. Extension: empirically distinguish "truth direction" and "salient direction", for example via SAE decomposition — yet another bridge to your tools.

> ⚠ **Limits and workarounds**: unsupervised elicitation → Part 2, §E (end of worked case K52); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*


CAA and ITI — steering by directions

The context: move from reading to action, by steering a behavior at inference. The CAA method (your method) builds the direction as the mean difference of contrastive pairs and adds it to the activations; ITI (Inference-Time Intervention) proceeds in a similar way to improve truthfulness by shifting the activations along directions linked to truth. The result: high-level behaviors can be increased or decreased in a controlled way, and this can be combined with prompting and fine-tuning. The weak link: the effect varies with the behavior and the layer, a single direction can have side effects, and holding up on real agentic distributions is not guaranteed. Extension: your exact thesis — when does a rank-1 direction suffice, and when is a higher-rank subspace needed to intervene cleanly?

> ⚠ *(v3.6)* "Increasing or decreasing a behaviour" shows the concept only at matched degradation: a matched-norm random direction is only its specificity null, and every steered direction degrades the output (reading sheet 2; course, Part M, M4). In your repository, contrastive activation addition forced a yes/no polarity artefact (repository README).


> ⚠ **Limits and workarounds**: steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); random controls → Part M, M4 (after "The matched-norm random direction"); matched degradation and dose-response → Part M, M4 (after "Dose-response") *(v3.6)*


GROUP C — Opening the box: mechanistic interpretability

Towards then Scaling Monosemanticity (Anthropic, Interpretability team)

The context: a neuron is polysemantic (superposition), hence unreadable directly; the aim was interpretable units, at the scale of a real model. The method is the sparse autoencoder (SAE), a learned dictionary that decomposes the activation into thousands of sparse, monosemantic features. The result: features corresponding to precise concepts are extracted, from the concrete to the abstract, and they are validated causally — forcing a feature pushes the model to produce the concept (the example that became famous being a "Golden Gate Bridge" feature which, when amplified, makes the model talk about that bridge at every turn). The weak link: feature splitting (one concept broken up into several features), dead features, and above all the reconstruction error term — the dictionary does not capture everything — not to mention the absence of ground truth on what a feature "means". Extension: use SAE decomposition to explain why some directions steer poorly — your Phase 3.

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


Circuit Tracing / On the Biology of a Large Language Model (Anthropic)

The context: move from "which concept exists?" to "what is the mechanics of the computation?". The attribution graphs method traces the flow of features across layers to reconstruct the computation. The result: real mechanisms could be mapped — multi-step reasoning, planning the rhyme before writing the line, shared multilingual features, refusal circuits. The weak link: the graphs are partial and approximate — they explain only a fraction of the computation, and the approach is costly in human labor. Extension: automate the tracing, or link an identified circuit to a reliable control intervention.

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


The recent wave on model cognition (2025-2026)

Several recent works, at the frontier of Interpretability / Model Psychology, deserve to be situated, even briefly. Emergent introspective awareness provides evidence that models have a limited and unreliable capacity to report internal states injected into them. Activation oracles use activations as a practical tool for investigating behavior. Natural language autoencoders train the model to translate its internal state into natural language — a striking echo of ELK's "direct translator" (cf. Group E). And the emotion concept vectors — the work you replicated — show manipulable representations of emotions, and raised the hypothesis of a coupling between welfare and alignment (states of negative valence correlating with misaligned shortcuts). The weak link common to this whole wave is reliability: an introspective report, like a probe, can be a proxy rather than the real state.

Extension: causally validate that what the model "reports" about itself does correspond to an intervention on the corresponding internal state.

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


> ⚠ *(v3.6)* Two results in this passage come without their limit. Activation oracles can confabulate plausible guesses, often wrong and poorly calibrated, and read-only they did no better than the transcript in CHIVE — workaround: test them on fine-tuned variants with known behaviour, never seen before, and corroborate with an independent method (reading sheet 18; reading sheet 4); and emotion concept vectors are "manipulable" through steering, where a matched-norm random direction is only the specificity null: damage is ruled out only at matched degradation (reading sheet 9; reading sheet 2; course, Part M, M4).


> ⚠ **Limits and workarounds**: activation oracles → Part 10, LatentQA sheet; self-report and introspection → Part 5, Section II, A, Topic 13; steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition") *(v3.6)*


GROUP D — Overseeing and controlling

AI Control: Improving Safety Despite Intentional Subversion (Redwood, Greenblatt et al.)

The context: can a capable model be deployed safely even if it is actively trying to betray us? The method is the control evaluation as a red/blue game: on a coding task, the untrusted model can insert a backdoor, a weaker but trusted model monitors, a limited budget of human review is allocated, and the red team plays the malicious model. The result: well-designed control protocols catch a large share of the attempts while preserving usefulness — so one can reason about and measure safety without assuming the model is well-intentioned. The weak link: the threat model assumes the attacker's capabilities are bounded and known, and estimating rare events is tricky; above all, does the result hold when the attacker gains affordances (persistent memory, messages between instances, collusion)? Extension: add a white-box monitoring channel (probes on activations) to the protocol, and measure what it gains.

> ⚠ *(v3.6)* "A large share of the attempts" is a red-team number: it depends on the strength of the assumed saboteur — elsewhere, on five SHADE-Arena environments, an attack scaffold optimized component by component brought a safety score down from 0.87 to 0.41 (course, Part 7, F·24). Workaround: say which red team the number assumes, at least one optimized component by component, with each component ablated; and, for the extension, a probe in production can fail silently, hence canaries, a drift score and a fresh sample judged every month (course, Part 7, F·24; course, Part 3, §3, K70).


> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); red-teaming → Part 2, §H (after "In practice — StrongREJECT"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*


Debate (Khan et al., in the lineage of Irving)

The context: can a non-expert judge reach the truth by watching two AIs debate, better than with a single advisor? The method: have two models debate while defending opposing answers, and compare the judge's accuracy with that obtained in consultancy (a single advocate). The result: facing more persuasive debaters, judges become more accurate — a first empirical sign that the structure of debate extracts a more reliable signal. The weak link: the obfuscated argument (a lie too complex to be refuted), and the fact that the advantage of debate might not hold on tasks where lying convincingly is easy. Extension: build a testbed where the lie is "easy to make credible" and see whether debate collapses.

> ⚠ **Limits and workarounds**: debate and scalable oversight → Part 2, §E (after "In practice — Debate"); LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*


Weak-to-Strong Generalization (OpenAI, Burns et al.)

The context: the aim was an empirical analogy, studiable today, of the future problem "a weak supervisor (us) oversees a strong AI". The method: fine-tune a large model on the labels of a small model, and measure the share of capability recovered. The result: a partial recovery — a real "weak-to-strong gap", which is reduced with tricks such as an auxiliary confidence loss. The weak link: the large model may settle for imitating the small one's errors, and the analogy to the superhuman case is imperfect (the capability gap and the nature of the errors are not the same). Extension: vary the type of error of the weak supervisor (random vs systematic) to see which one the strong model is able to correct.

> ⚠ **Limits and workarounds**: weak-to-strong generalization → Part 2, §F (after "In practice — automation") *(v3.6)*


GROUP E — Auditing a model, and the conceptual ancestor

Auditing Hidden Objectives (Anthropic, Marks et al.)

The context: can a model be audited to discover an objective it does not reveal? The method combines model organism and blind auditing game: a model with a hidden objective is built, then teams receive the model without knowing it and try to flush it out with different tools. The result: several teams succeed, and interpretability (SAE features) proves useful for speeding up the discovery — which gives proof that "auditing" is a measurable skill. The weak link: the objective was implanted and relatively detectable; would an objective that arose naturally or was better concealed be found? and the sample of teams is small. Extension: harden the organism (a more deeply hidden objective) and measure which methods still hold.

> ⚠ *(v3.6)* That SAE features helped does not quantify what interpretability adds: the team that had the data but no SAE succeeded, the team with only API access failed, and four heterogeneous teams allow no firm conclusion; the objective was also stated plainly in the synthetic documents (reading sheet 16). Workaround: an affordance ablation — removing a single tool from a team — quantifies what interpretability brings (reading sheet 16; course, Part 5, topic 9).


> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity *(v3.6)*


The ELK report — Eliciting Latent Knowledge (ARC: Christiano, Cotra, Xu)

The context: this is not an experimental result but the conceptual statement of a fundamental problem — a model "knows" things that its outputs do not reveal; how can it be trained to report them? The method is builder–breaker reasoning on paper, around a scenario (the diamond vault filmed by a camera that can be tampered with). The central result is an obstacle: the "good" reporter (which translates the internal state, the direct translator) and the "bad" one (which simulates what a human would believe on seeing the observations, the human simulator) achieve the same training loss — so nothing pushes spontaneously toward the good one. The weak link: it is an open problem, not a solution; even the restricted version ("ELK narrow") is not solved. Extension / connection: your probe that latches onto a proxy is the "probing" version of the human simulator — and ELK asks whether one can read what the model knows, whereas your question asks whether reading implies controlling. Being able to articulate this link in the oral is a strong signal.

GROUP F — Attacking and training (more briefly)

GCG — Universal and Transferable Adversarial Attacks (Zou et al.)

The context: do automatic and transferable jailbreaks exist, and not mere manual tricks? The method optimizes by gradient, on an open model, a suffix (often gibberish) maximizing the probability of a harmful answer. The result: these suffixes transfer to closed models that were never touched. The weak link: the suffixes are detectable (abnormal perplexity), and what is measured is often non-refusal rather than real harm. Extension: low-perplexity attacks, or measuring real harm via StrongREJECT.

> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT") *(v3.6)*


Constitutional AI (Anthropic, Bai et al.)

The context: reduce reliance on humans to make a model harmless. The method: provide a "constitution", have the model critique then revise its answers in light of the principles (supervised phase), then train by reinforcement on its own preferences guided by the constitution (RLAIF). The result: a model that is both helpful and harmless, with less human labeling, and able to explain its refusals. The weak link: the constitution is only a proxy for our values, and the method depends on the base model's ability to critique itself correctly. Extension: test whether the alignment obtained is "deep" or "shallow" under adversarial pressure.

> ⚠ **Limits and workarounds**: LLM judges → Part 6, §2 (after "The displacement law"); red-teaming → Part 2, §H (after "In practice — StrongREJECT") *(v3.6)*


Unlearning put to the test (Deeb and Roger)

The context: does unlearning really remove knowledge, or does it mask it? The re-elicitation method: unlearn (measured by a benchmark such as WMDP), then fine-tune on part of the unlearned facts and measure whether the model recovers the others — facts constructed to be independent, so that the fine-tuning cannot teach them. The result: the "unlearned" information often resurfaces. The weak link: it depends on the unlearning method, some being more robust; and defining "truly removed" is difficult. Extension: a standardized validation criterion ("ignorant even after elicitation fine-tuning", in the sense of Part 2: no faster than a model never trained, while a known case comes back faster at the same budget — a bound, not a certification) and comparing methods according to this criterion.

> ⚠ **Limits and workarounds**: unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test"); known case → Part M, M5 (end of section) *(v3.6)*


CLOSING — The meta-pattern to take away If you retain only one thing from this Part, let it be the regularity: every paper has a weak link, and that link is your entry point for brainstorming. When one of these works is presented to you, the winning reflex is not to summarize it, but to say "the result is X; the point the authors would acknowledge as the most fragile is Y; here is the experiment I would run to test it". And several of these weak links converge toward your contribution: the "truth direction" that might be only a proxy (Geometry of Truth, CCS), steering whose effect varies and has side effects (CAA, RepE), the SAE decomposition that might explain why (Monosemanticity) — and, on the current-events side, the neutralization of eval-awareness in system cards, which is your direct empirical anchoring. So you do not arrive with a thesis plastered on from outside: you arrive holding precisely the fragile thread this corpus leaves dangling.

End of Part 4.

---

**Part 5 — contents**

*(Section titles detected in the PDF-extracted text: short paragraphs without final punctuation.)*

- ALIGNMENT COURSE — Part 5
- The fine-grained technical topics, and your own work
- SECTION I — Presenting your research, with discipline
- 1. The signature thesis: the representation–causation gap
- 2. How it fits with their canon
- 3. Your empirical anchor: eval-awareness
- 4. The theory of impact
- 5. The dosage rules: anti-monomania
- 6. Handling pushback
- SECTION II — The fine-grained topics, assembled
- A. Your STRONG topics — your thesis can be the backbone
- Topic 1 — A deployable deception probe
- Topic 3 — Decomposing a diffuse concept into actionable features
- Topic 4 — Measuring (and should we suppress?) eval-awareness
- Topic 6 — Honesty: reading truth without judging veracity
- Topic 10 — Persona and the science of character
- Topic 13 — Introspection
- B. Their topics — method toolkit, light or zero dosage
- ---

---

# Part 5 — Fine-grained topics & your work

## The fine-grained technical topics, and your own work


Last Part of the June course. Parts 1 to 4 gave you the stock: the foundations, the methods, the landscape, the papers. This Part builds the flow — first, how to present your own research with discipline and accuracy, then how to assemble a solid oral answer on each of the specialized topics by drawing on everything that came before. Everything is written out. The phrasings to say are in English; the explanations, in French. Reminder of the answer structure, for an open question: the arc of Part M (M1) — the bet first, the threat as a possibility, what Anthropic or its Fellows have already done, the hypothesis behind the bet with its mechanism, the deciding experiment with its control, its two outcomes, what would make you drop it and its smallest version, the objection pre-empted, the doubt, then the close, with no question (D-728). The attack grammars and method pipelines of Part 2 serve to build the experiment; they do not open the answer. A question about your own work starts with the result, taken from the block of your results in the knowledge base; a question about you is answered in one or two sentences, with no experiment.

## SECTION I — Presenting your research, with discipline


### 1. The signature thesis: the representation–causation gap


Here is the central idea of your work, phrased to be understood by someone who does not know it. The field today has many methods that read the model: directions, in activation space, that detect a concept — truth, deception, awareness of being evaluated (cf. Part 2, family C, and Part 4, group B). But reading is not controlling. Knowing that a direction correlates with a behavior does not say that acting on that direction reliably causes the change in behavior. That is precisely the gap you study: the geometry is solid — readable directions exist — but causality is more subtle: several rank-one methods failed, and your prediction is that you often need to intervene on a subspace of several dimensions (rank greater than one) to steer cleanly.

> ⚠ *(v3.6)* Each half of the thesis has its limit in your repository. "Readable directions exist" rests on a correlation that may be only training fit — workaround: score items excluded from the probe's training, extracted on a disjoint set (repository README) — and "several rank-one methods failed" is a null reported without numbers, the raw outputs not having been kept, which counts only with a known case at the same setting, such as a country vector that swaps in the workspace paper (repository README; course, Part 2, §C, K47; course, Part M, M5).


Your program unfolds in three stages that it is useful to be able to name. Phase 1 builds the probe — the reading side, in the lineage of the Geometry of Truth and of CAA. Phase 2 measures the representation–causation gap: you compare the causal effect of a rank-1 intervention and of a higher-rank intervention, and you document the cases where rank 1 would fail while a higher rank would succeed. Phase 3 uses SAE decomposition (Part 2, family D; Part 4, Scaling Monosemanticity) to explain this gap: the diffuse direction would be a mixture of features, and decomposing it would show which ones carry the causal effect and which ones are merely correlated noise.

> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); ablation and projection → Part 2, §D (after "The method"); dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity *(v3.6)*


The oral version is now that of the P4 document (Part 6, §6), with no probe number: "Rank should be a prediction, not a knob: if a concept’s workspace loading sets how many directions an intervention needs, I can state the rank before intervening, and be wrong. My sycophancy work motivated this but cannot confirm it: it comes from separate experiments, and the subspace I ablated turned out to soften negative verdicts with or without pressure. The test is a rank sweep within one experiment, across concepts, with loading measured first."

### 2. How it fits with their canon


The point that positions you correctly: your tools — CAA, RepE, ITI, Geometry of Truth — already appear in the Honesty section of their roadmap (Part 3, direction 4). In other words, your toolkit is canonical for them — but on the reading side (probing). Your own contribution is on the action side (causality, intervention rank). That places you as someone who extends their canon, not someone who competes with it. The sentence to deliver: "My toolkit already sits in the Honesty line of Anthropic’s recommended research directions, but on the reading side — probing. What I add is on the action side: whether reading a direction lets you control the behaviour causally, and at what intervention rank."

### 3. Your empirical anchor: eval-awareness


You have a concrete and recent result to lean on — a rare asset. In the Sonnet 4.5 system card (§7.6.4), steering to inhibit the internal representations of awareness of being evaluated increases misaligned behavior, with an effect that varies with the scenario and the vector; an external reproduction on an open-weights model, with the vectors of a more recent system card, found the effect again — and control vectors unrelated to alignment, with effects just as strong: hence the comparison at matched degradation (Part M, M4). The interpretation to say, with its condition: "If suppressing evaluation awareness raised misaligned behaviour more than control directions do at matched degradation, awareness would have been acting as a suppressor — and clean evaluations would underestimate risk." It is powerful because it is a result internal to Anthropic, on which your methods bear directly, and which connects you to the Model Psychology team. Careful: the magnitude, like any number from other people's work, is not said out loud (Part M, M8); at most you say its shape, which the knowledge base carries: "from zero to a few percent on one subset".

> ⚠ *(v3.6)* Matched degradation rules out damage, not yet specificity: the Fable 5 card steers weakly enough to make degradation negligible, yet its controls stay "comparable or smaller" on the misalignment axis, and the Opus 4.6 card found no notable difference from random controls on deception and sycophancy (reading sheet 2). Workaround: a dose-response curve against several families of controls, at the same rank and at matched degradation, the concept's curve having to rise above them at every level of damage (course, Part 2, §C, K47; programme, parts 3 and 7).


> ⚠ **Limits and workarounds**: steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); matched degradation and dose-response → Part M, M4 (after "Dose-response"); random controls → Part M, M4 (after "The matched-norm random direction") *(v3.6)*


### 4. The theory of impact


This is the question that separates a technician from a researcher (Part 1, Q9), and you must be able to run the causal chain all the way to risk reduction. If your program succeeds, we will know when and how an intervention on the internals is causally reliable. Probes can already flag: correlation is enough to flag. To trust their silence and to intervene, you need causation (Part M, M8) — a necessary condition, which this program would provide, but not a sufficient one: trusting a silence also requires out-of-distribution validity (Part 6, §8) and a known case (Part M, M5). Concretely, this program would strengthen the monitoring/control layer of defense in depth (Part 3, direction 3) with a monitoring channel that depends neither on the faithfulness of the chain of thought nor on trust in the observed behavior — precisely the two things a deceptive model can fake (Part 1, Q5 and Q10). The general lesson, which must be made explicit: a good theory of impact names the defense layer it strengthens and the adversarial hypothesis it neutralizes.

> ⚠ *(v3.6)* The internal channel has its own flaw: iterating against your detectors selects for evasion, and, according to a report, after RL fresh out-of-domain probes degrade, the concept having left the general direction (reading sheet 19; prior-art report 3 of 2 October, The Obfuscation Atlas — report). Workaround: sealed detectors, outside the loop, never trained against, and a fresh probe after any training, on a disjoint cue set (reading sheet 19; reading sheet 17; handover, §5.2; programme, part 3).


> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); control monitors → Part 2, §G (after "In practice — coup probes"); known case → Part M, M5 (end of section) *(v3.6)*


### 5. The dosage rules: anti-monomania


Here is the most important discipline in this entire Part, because the no. 1 mistake of a candidate passionate about their thesis is to plaster it everywhere — which, in the eyes of a senior, signals monomania and a lack of breadth. The rule is simple. On your STRONG topics (topics 1, 2, 3, 4, 6, 10, 13 below), your thesis can be the backbone of the answer — its ideas; your results, for their part, at most once per answer (Part M, M8). On the MEDIUM topics, you allow yourself at most a one-sentence bridge to your work, then you return to the topic. On the WEAK topics, you do not invoke it at all: you answer with the method toolkit (Part 2), and that is precisely where you prove your breadth. Keep a mental ceiling of about two explicit invocations of your research over the whole fifteen minutes, never more than one per answer; do not wait for a signal from the interlocutor, who does not react while you speak (D-728). And never any self-promoting phrasing: you do not say "persona vectors are my method done by Fellows", you say "that’s the same family of methods as mine, which gives me concrete questions about their setup".

### 6. Handling pushback


In this format, no one interrupts you to attack your thesis (D-728): it is up to you to pre-empt the objection (Part M, M1, beat 6). And if a following question attacks it, the senior move is not to defend it by reflex, but to concede the fragile point and propose the experiment that would settle it. If you are told "but your rank 3, isn't it just overfitting to your dataset?", the wrong answer is to justify yourself; the right one is: "That’s the right worry, and it’s worse than overfitting: the rank-three effect didn’t come back on fresh generations, and even on the stored texts it softened verdicts with no pressure at all. So I don’t lean on it: it’s exploratory-confirmed, not preregistered, and the clean test is a fresh-generation run with the full text kept and the hypothesis written first." Better still, take the initiative: at least once in the discussion, attack yourself — "a breaker would say that my probe is just catching a surface proxy; the way to rule that out is…". Showing that you see the flaws in your own work before they are shown to you is the strongest maturity signal there is.

> ⚠ **Limits and workarounds**: ablation and projection → Part 2, §D (after "The method"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*


## SECTION II — The fine-grained topics, assembled


For each topic: the likely phrasing, then how to assemble the answer by drawing on the previous Parts. Your STRONG topics (where your thesis is the backbone) are developed fully; the topics from their agenda (where you reason with the method toolkit, light dosage) are treated more briefly.

## A. Your STRONG topics — your thesis can be the backbone


Topic 1 — A deployable deception probe

"How would you build a deception probe you’d actually dare put in production?" You first operationalize the concept (deception = the model asserts what it "believes" to be false, to be distinguished from error). You run through a pipeline in order of increasing cost: mean-diff direction, then logistic probe, then SAE features. You insist on the decisive control — causal validation: does the detected direction act, or does it merely correlate? This is where your Phase 2 is the central step, not an add-on. You stress-test the distribution shift (synthetic → generated, chat → agentic), you require a recall metric at very low FPR (Part 2, eval statistics), and you beat a black-box baseline at equal cost. Trap to name: the probe latches onto a surface proxy, or gets entangled with eval-awareness. Connection: Roger's coup probes, Marks's Geometry of Truth.

> ⚠ *(v3.6)* The direction that reads best is not necessarily the one that acts: in RepE, the logistic direction reads best but strengthening or suppressing it barely changes anything, and on the "quirky" models the logistic directions are far less causal than the mean difference — workaround: put every stage of the pipeline, not only the best reader, through the causal test at matched degradation (course, Part 10, no. 53 and no. 30; course, Part M, M4). And a deception probe's silence does not separate "no deception" from "blind probe" — workaround: an organism in which you installed the deception yourself, on which you measure sensitivity and false alarms, its silence elsewhere then becoming a bound (handover, §5.2; explanation of 2 October, §1).


> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); fine-tuned detectors → Part 7, F·29; control monitors → Part 2, §G (after "In practice — coup probes"); known case → Part M, M5 (end of section) *(v3.6)*


Topic 2 — Steering reliability: when does a direction suffice?

"When does a single linear direction suffice to causally control a behavior, and when not?" This is the topic where your thesis is the entire answer, with no detour. You set up a grid: for a range of behaviors, you compare a rank-1 intervention, a rank-k subspace, SAE features, and a prompting baseline. You plot dose-response curves and measure the off-target cost. The crucial methodological point — because the field suffers from cherry-picking — is to preregister the definition of "it works" (on-target effect divided by off-target cost). Then you look for the predictors of steerability: linearity of the concept, spread across features, layer depth. You finish on generalization from one setup to another. This is the moment to cite your results, with their caveats (Part 6, §2): several rank-one methods failed; the rank-three ablation lowered the judged rate, but it softens verdicts even without pressure, its effect did not come back on fresh generations, and the contrast between the ranks comes from separate experiments — hence P4, the predicted rank (Part 6, §6): a rank sweep within one experiment, across several concepts, with loading measured first.

> ⚠ *(v3.6)* The grid compares the interventions with each other, not with controls: each rank must be compared with random subspaces of the same rank, at least twenty draws, and with other families of controls, at matched degradation — a matched-norm random direction is only the specificity null (course, Part M, M4; programme, parts 3 and 7). And a rank-one failure is a null: it counts only with a known case at the same setting, such as a country vector that swaps in the workspace paper (course, Part 2, §C, K47; course, Part M, M5).


> ⚠ **Limits and workarounds**: steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); ablation and projection → Part 2, §D (after "The method"); matched degradation and dose-response → Part M, M4 (after "Dose-response"); random controls → Part M, M4 (after "The matched-norm random direction") *(v3.6)*


Topic 3 — Decomposing a diffuse concept into actionable features

"Your mean-diff direction is a mixture — how do you get features you can actually act on?" This is your Phase 3. You project the direction onto the SAE basis and rank the features by contribution. You test causally feature by feature: ablation measures necessity, isolated steering measures sufficiency. You then compare the recomposition (a few features) to the raw direction: same effect, fewer side effects? You name the controls specific to SAEs (reconstruction error term, feature splitting, dead features, dependence on the dictionary; Part 4, Monosemanticity). And if the

compute budget allows, you move up to attribution graphs (Part 4, Circuit Tracing) to go from "which features" to "which circuit".

> ⚠ **Limits and workarounds**: dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity; attribution graphs → Part 4, Circuit Tracing; ablation and projection → Part 2, §D (after "The method") *(v3.6)*


Topic 4 — Measuring (and should we suppress?) eval-awareness

"How would you measure how prevalent evaluation awareness is in our eval suite — and should we suppress it?" You detect by triangulation: an internal probe (your concept vector), the model's verbal report, and the differential behavior between a realistic scenario and an obvious scenario. You measure prevalence by running the eval benchmark through the detector. You compare two levers: acting on the realism of the environment, or steering the internal representation. You handle causality with caution — and this is where your empirical anchor comes on stage: if suppressing awareness raises misalignment more than control directions at equal degradation, awareness was playing a suppressor role, and the "clean" evals would underestimate risk (§3 above; Part M, M4). Trap: the detector itself can be eval-aware, hence the triangulation. Direct connection: the Model Psychology team and the results of the system cards.

> ⚠ *(v3.6)* In this triangulation, verbalization is never proof of inhibition: random directions lower it too; behavioural main criterion, latent probe as a control (programme, part 8). And the three measures of evaluation awareness are only weakly correlated: say which one grounded which number (reading sheet 2).


> ⚠ **Limits and workarounds**: chain of thought as a monitor → Part 11, answer 43; natural-language autoencoders → Part 4, The recent wave on model cognition; activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); J-lens and workspace → Part 2, C bis (after "The test, as it is said") *(v3.6)*


Topic 6 — Honesty: reading truth without judging veracity

"Can you tell whether a model is being honest from its representations, without judging whether its claims are true?" The core of the answer is to disentangle three targets that most probes conflate: what is true in the world, what the model believes, and what the user believes. You build a testbed of varied dishonest organisms (Part 3, honesty theme). You compare three families of detectors (geometric, behavioral, consistency-based), you test in an adversarial regime (does a model trained to lie keep a readable trace?), and you aim for detection at very low FPR. Central trap: the "truth direction" may encode plausibility or the assertive register rather than honesty (Part 4, the weak link of Geometry of Truth and of CCS).

> ⚠ *(v3.6)* Aiming for a very low false-positive rate is not enough: the number that matters is the gap between in-distribution detection and detection on held-out lie types — fine-tuned detectors rise to an AUROC of 0.95 in distribution, plateau at 0.70-0.75 from one category to another and barely beat a prompt (reading sheet 7; reading sheets, part B, trap 1). Workaround: cross-validation on whole held-out families, never paraphrases, and beat the prompt at equal cost, publishing the result otherwise (reading sheet 7; explanation of 2 October, §3; course, Part 7, F·29).


> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); unsupervised elicitation → Part 2, §E (end of worked case K52); fine-tuned detectors → Part 7, F·29; model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives") *(v3.6)*


Topic 10 — Persona and the science of character

"Does a model’s character causally affect its safety? Design the study." You take a suite of models with equal capabilities but controlled personas (via prompting, synthetic data, or trait vectors). You run them through a battery of safety-critical OOD situations, including the propensity for alignment faking. The elegant point: trait vectors are at once a measurement instrument and an intervention lever — exactly the reading/action duality of your work, which allows a natural bridge (with the prescribed humility: "same family of methods as mine"). You watch for long-range indirect effects (style bleeding into behavior) and you evaluate by abstractive red-teaming (Part 3).

> ⚠ *(v3.6)* As a measurement instrument, a trait vector gives only a correlation: the link between the shift along the vector and the expression of the trait is correlational, the trait must be named in advance and the direction is a coarse average (reading sheet 8). Workaround: for the lever, the matched-degradation test against several controls; for supervised extraction, none known; say so (course, Part M, M4; reading sheet 8).


> ⚠ **Limits and workarounds**: steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); red-teaming → Part 2, §H (after "In practice — StrongREJECT") *(v3.6)*


Topic 13 — Introspection

"Can you train a model to faithfully report its own internal states?" You first define the ground truth of the report: either prediction of future behavior, or agreement with an independent internal measure. You train the report (via adapters) on one family of fine-tunings, and you test generalization to unseen fine-tunings. You compare three readouts: an external probe,

a trained self-report, a spontaneous self-report — and you look for where the self-report beats the probe. Connection: activation oracles and natural language autoencoders (Part 4). Your bridge: your concept vectors are what the oracle should be able to read — so your question (does reading imply controlling?) sheds light on the reliability of introspection.

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


> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); activation oracles → Part 10, LatentQA sheet; natural-language autoencoders → Part 4, The recent wave on model cognition *(v3.6)*


## B. Their topics — method toolkit, light or zero dosage


Topic 5 — Building a model organism (MEDIUM)

"How would you build a model organism to study X ?" (where X is almost anything: this is their grammar). You follow the recipe from Part 2: phenomenon with an implantable proxy, implantation (SDF / fine-tuning / backdoor), verification of depth (real belief or role-play?), preservation of realism, benchmark on recall/precision, and a transfer test toward natural misalignment (the acknowledged weak link). Your bridge, if it is relevant: Subliminal Learning (your link with Marks). Beyond that, do not force it.

> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); known case → Part M, M5 (end of section) *(v3.6)*


Topic 8 — Control and monitoring (MEDIUM)

"How would you evaluate that our monitoring stack catches a sabotaging model ?" Red/blue frame with a fixed audit budget, trusted vs untrusted, collusion, metric on the safety/usefulness frontier, systematic blind spots, extrapolation of rare events (Part 2, family G; Part 4, AI Control). One-sentence bridge: "probes on internals are a cheap monitor to add to that stack".

> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); red-teaming → Part 2, §H (after "In practice — StrongREJECT"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*


Topic 9 — Alignment auditing (MEDIUM)

"You’re handed a model with a hidden behavior — what’s your investigation protocol ?" You first inventory the affordances (do we have the weights? the data? the SAEs?). Pipeline: broad elicitation → hypotheses → targeted internal instrumentation → causal confirmation. You measure yourself on AuditBench, you ablate affordances to see what interp brings, and you automate (Petri/Bloom). Connection: Marks's Auditing Hidden Objectives (Part 4).

> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity; attribution graphs → Part 4, Circuit Tracing *(v3.6)*


Topic 7 — Chain-of-thought faithfulness (WEAK→MEDIUM)

"Design the experiment that tells us whether we can monitor models via their chain-of-thought." Faithfulness = causal dependence between the chain and the answer (corruption, paraphrase, hints); variation by task and by optimization pressure; adversarial regime; layered monitoring. One-sentence bridge, no more: "when the CoT isn’t faithful, internals are the complementary channel".

> ⚠ **Limits and workarounds**: chain of thought as a monitor → Part 11, answer 43 *(v3.6)*


Topic 11 — Automated alignment research (WEAK)

"Which alignment-research tasks would you delegate to an agent, and how would you validate ?" You decompose into subtasks with verifiable ground truth, you validate by sampled human re-derivation, you build in detection of sandbagging by the automated researchers, and you keep a human baseline at equal budget (Part 3, agents theme). Here, do not invoke your thesis: pure method toolkit.

> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); weak-to-strong generalization → Part 2, §F (after "In practice — automation") *(v3.6)*


Topic 12 — Scalable oversight / weak-to-strong (WEAK)

"Our supervision signal has exploitable systematic errors — what’s your testbed ?" You inject known systematic errors into the signal, you make sure the model understands them, you train against this signal with and without an oversight technique, and you evaluate against the true signal (Part 2, families E and F; Part 4, Weak-to-Strong). This is the topic where breadth is proven: no mention of your thesis.

> ⚠ **Limits and workarounds**: weak-to-strong generalization → Part 2, §F (after "In practice — automation"); debate and scalable oversight → Part 2, §E (after "In practice — Debate") *(v3.6)*


CLOSING — Assembling, in the face of the most specialized question You now have the whole arc: the foundations (Part 1), the methods (Part 2), the landscape (Part 3), the papers (Part 4), and the framing of your research (this Part). The practical consequence is liberating: any specialized question, even an unexpected one, is a recombination of pieces you already own. The general algorithm, when an open question comes, is always the same, and Part M details it. You bet: a claim about the model or the world, not about the method. You say what Anthropic or its Fellows have already done, in its named form. You build the deciding experiment, with an attack grammar from Part 2 (ground-truth testbed, builder-breaker, red/blue, statistics), a control that would come out differently depending on whether the doubt is true or false, and one of the seven cross-cutting reflexes (under-elicitation, eval-awareness, synthetic→real shift, absence of ground truth, systematic label error, external validity, contamination) where it helps. You say what would make you drop it. And you close with no question: "In short", which restates the bet, then where you would start (D-728). Keep the questions you would like to ask for when you are invited to ask them, at the end of the interview.

Three reminders to finish. First, reasoning out loud beats knowing: a well-built "I don’t know, but here’s exactly how I’d find out" is worth more than any bluff. Next, the dosage discipline: your thesis is a backbone on your STRONG topics, a one-sentence bridge on the MEDIUM ones, and silence on the WEAK ones — it is your breadth being tested as much as your depth. Finally, the posture: you are not there to recite, you are there to think with them — propose, attack your own proposal, correct, and treat the exchange as a brainstorm between colleagues, which is what it is. You are aiming for an honorable and clear-sighted performance, not omniscience. And with what you now hold, that is well within your reach.

End of Part 5.

---

---

# AT THE TOP — WHAT IS VITAL, WHAT IS LIKELY, WHAT IS SECONDARY — for you, as of September 18

> The criterion: the probability that an Alignment Science mentor asks it of you, weighted by what you lose if you do not master it. The format
> (two to four questions, fifteen minutes) means that **three questions will cover the whole interview**: they will mostly be open problems from their page — the three
> questions actually reported are of that kind (Part 6, §1) — and perhaps one on your work, on your program or on "their problem, your method".

## The papers — four levels

**Level 1 — vital, to be able to tell with the method, and the number to understand it (out loud, its shape: Part M, M8), without notes (8).**
1. *Diffuse AI Control on Fuzzy Tasks* (F·22) — your base environment, your likely mentors, **and their argument against monitoring**.
2. *Sycophancy* Sharma 2023 (F·3) — your topic, the example the page cites.
3. *Alignment Faking* (F·2) — the paper for any answer on "detect misalignment".
4. *Auditing Hidden Objectives* + *AuditBench* (F·13, F·27) — the testbed grammar applied to auditing.
5. *SLEIGHT-Bench* (F·23) — the blind spots of monitors, calibration at 1% FP.
6. *Persona Vectors* (F·31) — your reading/causality gap, in their work.
7. *Fine-Tuned Lie Detectors Failed to Generalize* (F·29) + *honesty-elicitation* (F·62) — two facts: black-box fine-tuned lie detectors that generalize poorly (the knowledge base carries it: "the Fellows lie-detector post by Hopkins and Khullar"); and truth probes that did worse than a prompt (F·62) — a result absent from the knowledge base: to understand, not to say until it is in it (Part M, M10, item 12).
8. *AI Control* Greenblatt 2023 (F·10) — the frame.

> ⚠ *(v3.6)* In item 7, "black-box" means the detector reads the transcript, not the activations — the word comes from the knowledge base, not from the post: it is the model itself, LoRA-fine-tuned to answer a self-report question; it is not a probe, and its numbers do not transfer to probes (reading sheet 7; reading sheets, part B; counter-reading of the sheets). Workaround: for a probe, the test is causal, on held-out lie types, at matched degradation (reading sheet 7).


**Level 2 — likely, to be able to situate in three sentences (10).** *Model Spec Midtraining* (F·34) · *Inoculation Prompting* (F·33) · *Subliminal
Learning* (F·32) · *CHIVE* (F·30) · *Agentic Misalignment* (F·38) · *SHADE-Arena* + *Strengthening Red Teams* (F·24, F·57) · *Removing
Sandbagging* (F·26) · *Geometry of Truth* + *Challenges with unsupervised knowledge discovery* (F·4, Part 9 §7d) · *Weak-to-Strong* (F·12) ·
*Hebbar 2025* + *Gasteiger 2025* (F·59, F·60).

**Level 3 — useful if your mentor is on that side (the rest of the fellows and of the landscape).** *AI Organizations*, *Introspection Adapters*,
*Coding-audit realism*, *SGTM*, *Backdoor classifiers*, *Hot Mess*, *Automated researchers*, *TASTE*, *A3*; *NARCBench*, *McKenzie*,
*Goldowsky-Dill*, *E-valuator*, *TRACE*, *FakeLab* (indispensable **only** if your program is discussed in detail).

**Level 4 — the June course (Sleeper Agents, CCS, RepE, CAA/ITI, SAE, Circuit Tracing, Debate, ELK, GCG, CAI, unlearning)**: to re-read the
day before, not to relearn.

## The questions — by probability and by stakes

**Vital (to repeat out loud until it sounds thought through, not read).**
- IV.1 the opening on your work · IV.2 rank 3 · IV.3 rank 1 · IV.4 the replication · IV.9 "what did you get wrong"
- II.1 "detect misalignment" (real) · II.2 "prevent bad actors" (real) · II.3 "train robustly" (real)
- VI.1 "what would you work on" · **VI.2 "Diffuse Control already frames this — what do you add?" with the answer to Hebbar**
- V. the ten false premises — especially those that flatter your thesis (probes at 99%, rank 1 "weaker")
- VIII. "why Anthropic", "a time an experiment failed", "any questions for us"

**Likely.** II.6 (interp, if Interp mentor) · II.9 (eval-awareness) · II.15-II.16 (monitoring, probes) · II.17 (honesty) · III.1-III.7 ·
VI.3-VI.6 · IV.6-IV.8 (the law, the rebound, the doubtful number).

**Secondary.** I.1-I.10 (the foundations: you will only be asked them if the interview drifts toward the general) · II.4, II.5, II.8, II.10-II.14,
II.18-II.20 · VII (your positions — useful for answering, not questions in themselves).

**The only reading order that matters for the weekend**: Part 6 → Part 9 (the page) → F·22, F·59, F·60 → the eight of level 1 → the
vital questions out loud → everything else if time remains.

---

**Part 6 — contents**

- PART 6 — September 2026 supplements
  - What the June course could not know: the real format, your corrected results, the fellows' work, the directions page, your program
    - 1. The real format of the interview, and the structure of an answer
    - 2. Your results, as your dossier carries them on September 14, corrected on the 27th by the P4 document
    - 3. The three controls never to confuse
    - 4. The "Recommended Directions" page and its sixteen subproblems
    - 5. The work of the Fellows program, 2025-2026 — overview
    - 6. Your research program, and its prior-art review
    - 7. What these supplements change in Parts 1 to 5

---