# Insertions appliquées — volet3 — EN

### Insertion n°2, après la ligne 1023 de la v3.5

> Ancre : The first direction starts from a question prior to all the others: what can this model do? You cannot reason about risk without knowing it, and it is harder than it looks, for two reasons seen in Part 2. First, the raw score on a benchmark is misleading: what matters is the differential uplift — do

> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*

### Insertion n°4, après la ligne 1043 de la v3.5

> Ancre : > *"I'd bet elicitation gains differ across models enough that their score-versus-effort curves cross, so one effort level would misrank them. If the order stayed the same at every effort level, while a model known to underperform on a bare prompt rose with effort, I'd drop the bet."*

> ⚠ *(v3.6)* This point comes from a sabotage evaluation whose limits the August Risk Report itself concedes (§2.16): evaluations not drawn from the real risk pathways, a secondary task in the prompt, models probably aware of being evaluated (reading sheet 3). Workaround: elicitation at a budget fixed in advance, reported as a bound (course, Part M, M7; course, Part 2, §B, K63); against a model that holds back, two versions of an environment, randomly assigned, differing only in realism cues scored by a discriminator, with an organism trained to hide as the known case (course, Part 2, §B, K63).

### Insertion n°6, après la ligne 1054 de la v3.5

> Ancre : can trust what a model says about itself — and the honest answer is "not by default", which justifies white-box methods.

> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); self-report and introspection → Part 5, Section II, A, Topic 13; chain of thought as a monitor → Part 11, answer 43; model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives") *(v3.6)*

### Insertion n°8, après la ligne 1074 de la v3.5

> Ancre : > *"I'd bet a chain of thought names what changed the answer where the task needs the chain. If chains on tasks that need them named a planted hint no more often than chains on easy tasks, while chains told to cite it were scored as naming it, I'd drop the bet."*

> ⚠ *(v3.6)* The hint test measures what the chain verbalizes, not the computation that produced the answer: a chain that does not name the hint is not, for that reason, hidden reasoning (reading sheet 17). Workaround: say "not verbalized", never "hidden reasoning", and measure monitorability as a ratio — the verbalized against the internal or the actions —, through graded perturbation of the chain (reading sheet 17; course, Part 11, answer 43).

### Insertion n°10, après la ligne 1079 de la v3.5

> Ancre : The third direction adopts the bet of Part 2: rather than guaranteeing alignment, you assume the model is potentially untrusted and design a deployment that remains safe anyway. It includes monitoring (a weak but trusted model monitors a strong but untrusted model), anomaly detection (spotting the u

> ⚠ *(v3.6)* This channel has its own ways of failing: at a monitor's threshold, probes recall 43% at 1% false positives, against 55% for the best LLM monitor (course, Part 7, F·51), and iterating against your detectors selects for evasion (reading sheet 19). Workaround: report recall at 1% false positives against a black-box baseline at equal cost (course, Part 7, F·50; course, Part 5, topic 1), and keep sealed detectors, outside the loop: if they keep firing when the in-loop ones go quiet, evasion has been selected (reading sheet 19).

### Insertion n°12, après la ligne 1079 de la v3.5

> Ancre : The third direction adopts the bet of Part 2: rather than guaranteeing alignment, you assume the model is potentially untrusted and design a deployment that remains safe anyway. It includes monitoring (a weak but trusted model monitors a strong but untrusted model), anomaly detection (spotting the u

> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); natural-language autoencoders → Part 4, The recent wave on model cognition; self-report and introspection → Part 5, Section II, A, Topic 13; LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*

### Insertion n°14, après la ligne 1099 de la v3.5

> Ancre : > *"I'd bet a production probe would fail silently mostly through input drift, and that the drift would show before its recall on planted canaries fell. If canary recall fell first, with the drift score still at its baseline, though that score did rise on new task families, I'd drop the bet."*

> ⚠ *(v3.6)* The Fable 5 card's finding sets the probe against two instruments with limits of their own: the NLA can confabulate (reading sheet 18), answers to follow-up questions depend on how they are phrased (reading sheet 3), and the three measures there are only "weakly positively correlated" (reading sheet 2); it shows that the probe stays silent, not which reading is right. Workaround: triangulate, and say which measure grounded which number (course, Part 5, topic 4; course, Part M, M4), measuring the controls with an instrument independent of the NLA (reading sheet 18).

### Insertion n°16, après la ligne 1099 de la v3.5

> Ancre : > *"I'd bet a production probe would fail silently mostly through input drift, and that the drift would show before its recall on planted canaries fell. If canary recall fell first, with the drift score still at its baseline, though that score did rise on new task families, I'd drop the bet."*

> ⚠ *(v3.6)* The slower judge that labels the fresh sample is itself an instrument, unaudited here: a judge has systematic errors (course, Part 6, §2), and a judge that reads the reasoning gets persuaded — about 1% of actions flagged with the chain of thought, about 50% without, for a single monitor (reading sheet 3). Workaround: a sealed judge and a human audit of about 200 stratified items, agreement reported (programme, part 3), judging the actions, their outputs and the messages, not the text before the action (handover, §5.1).

### Insertion n°18, après la ligne 1106 de la v3.5

> Ancre : It is also, and this matters for you, where the roadmap places honesty. The logic is as follows: if one could get a model to faithfully report what it knows, one would have a "free" reliable oversight signal — hence the attachment of honesty to oversight. This sub-direction descends directly from an

> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); debate and scalable oversight → Part 2, §E (after "In practice — Debate"); weak-to-strong generalization → Part 2, §F (after "In practice — automation"); unsupervised elicitation → Part 2, §E (end of worked case K52) *(v3.6)*

### Insertion n°20, après la ligne 1126 de la v3.5

> Ancre : > *"I'd bet a deception probe that's perfect on its test set would also fire on the test context itself. If it stayed at its baseline on honest transcripts written as tests, while a separate evaluation-awareness probe read them as tests, I'd drop the bet."*

> ⚠ *(v3.6)* The defection probe was validated on an implanted backdoor: the best of 1,000 random directions already reaches 95.3% there, and salience may come from the insertion (reading sheet 15). A success on an organism bounds the instrument; for a model that became deceptive on its own, no workaround is known (course, Part M, M5).

### Insertion n°22, après la ligne 1133 de la v3.5

> Ancre : misalignment (the attack reveals an internal fragility), which makes it a good place to show that you distinguish the two families of risk.

> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT"); safety classifiers → Part 2, §H (end of worked case G1) *(v3.6)*

### Insertion n°24, après la ligne 1153 de la v3.5

> Ancre : > *"I'd bet separating the user's channel from the documents' would stop injections that give orders, but not indirect ones that only make a harmful action look natural. If both families fell equally under channel separation, when an undefended agent had executed both, I'd drop the bet."*

> ⚠ *(v3.6)* The "near-total immunity" reported by the Mind Viruses paper was measured with model judges, which can count a polite echo as adoption (course, Part 3, §6, K13), and a defence holds only against the red team that tested it: a weak red team makes it look safe (course, Part 7, F·24). Workaround: count only the steps actually acted on and have a sample re-scored by hand (course, Part 3, §6, K13); say which red team the number assumes, at least one optimized component by component, with each component ablated (course, Part 7, F·24).

### Insertion n°26, après la ligne 1158 de la v3.5

> Ancre : The sixth direction groups younger problems. Unlearning aims to remove dangerous knowledge, with the decisive control seen in Part 2: re-elicitation (does the knowledge come back through fine-tuning faster than in a model never trained?). Multi-agent governance is concerned with what happens when se

> ⚠ *(v3.6)* Re-elicitation decides in one direction only: if the knowledge does not come back faster, you sign a bound, "not elicitable at this budget", never an absence (reading sheets, part C); and a small fine-tune can teach instead of revealing (course, Part M, M9). Workaround: facts built to be independent, the never-trained reference at the same budget, and a model known to mask as the known case (course, Part M, M4, M5 and M9; course, Part 2, §I); for capabilities rather than low-leakage facts, none known; say so (course, Part 10, Deeb and Roger).

### Insertion n°28, après la ligne 1158 de la v3.5

> Ancre : The sixth direction groups younger problems. Unlearning aims to remove dangerous knowledge, with the decisive control seen in Part 2: re-elicitation (does the knowledge come back through fine-tuning faster than in a model never trained?). Multi-agent governance is concerned with what happens when se

> ⚠ **Limits and workarounds**: unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test"); LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*

### Insertion n°30, après la ligne 1204 de la v3.5

> Ancre : To talk about current concerns and not just the foundations, here are the main recent workstreams, grouped by theme. Part 4 will tell several of these papers one by one; here, the goal is for you to know what the team is talking about right now.

> ⚠ **Limits and workarounds**: steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); LLM judges → Part 6, §2 (after "The displacement law"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); fine-tuned detectors → Part 7, F·29; self-report and introspection → Part 5, Section II, A, Topic 13; activation oracles → Part 10, LatentQA sheet; natural-language autoencoders → Part 4, The recent wave on model cognition; model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); weak-to-strong generalization → Part 2, §F (after "In practice — automation") *(v3.6)*

### Insertion n°32, après la ligne 1208 de la v3.5

> Ancre : This is probably the most active theme, and the one that directly touches your work. The problem is that evaluations can lie because the model knows it is being evaluated. Recent system cards (starting with Sonnet 4.5) respond to this in two ways: by making the scenarios more realistic, and by neutr

> ⚠ *(v3.6)* This anchor remains weak support as long as specificity is not established: in the Opus 4.8 card, control vectors with arbitrary content move behaviour in the same direction, more weakly, and every direction degrades the outputs; at 0.01× strength, the Fable 5 card makes degradation negligible, yet its controls stay "comparable or smaller" on the misalignment axis (reading sheet 2). Workaround: a matched-norm random direction is only the specificity null, and damage is ruled out only at matched degradation — a specific subspace against random subspaces of the same rank, at matched degradation, with a prompt baseline and a dose-response curve (reading sheet 2; course, Part M, M4; course, Part 5, topic 4).

### Insertion n°34, après la ligne 1212 de la v3.5

> Ancre : Second major theme, and the other side of your relevance. The team explores lie detection and honesty elicitation on a varied testbed of dishonest model organisms (trained to lie in different ways). On the introspection side, a series of interpretability works seek to get the model to report its int

> ⚠ *(v3.6)* On this suite of dishonest organisms, truth probing and honesty steering did worse than simple prompting (course, Part 7, F·62 — a fact to say out loud only once added to the knowledge base); and fine-tuned lie detectors plateau at 0.70-0.75 AUROC out of distribution, barely beating a prompt (reading sheet 7). Workaround: cross-validation by held-out lie types, beating a prompt baseline at equal cost, and publishing the result if the detector does not beat it (reading sheet 7; course, Part 5, topic 1; course, Part 7, F·29).

### Insertion n°36, après la ligne 1212 de la v3.5

> Ancre : Second major theme, and the other side of your relevance. The team explores lie detection and honesty elicitation on a varied testbed of dishonest model organisms (trained to lie in different ways). On the introspection side, a series of interpretability works seek to get the model to report its int

> ⚠ *(v3.6)* These readings are not a self-report of the model: an activation oracle is a fine-tuned copy doing the reading, not the queried model (course, Part 10, LatentQA), and oracles and NLAs alike can confabulate (reading sheet 18); emergent introspection remains rare and unreliable, about 20% detection for Opus 4.1 (reading sheet 11). Workaround: test the decoder on fine-tuned variants with known behaviour, never seen before, and corroborate with an independent method while keeping the decoder separate (reading sheet 18); for introspection, ground truth through concept injection (reading sheet 11).

### Insertion n°38, après la ligne 1216 de la v3.5

> Ancre : Third theme: can a model be audited to uncover a hidden objective? We saw it in Part 2 with the auditing game on a model organism with a concealed objective; the effort continues with auditing benchmarks (AuditBench) that provide a ground truth for comparing investigation protocols, and with the aut

> ⚠ *(v3.6)* AuditBench's ground truth is that of 56 models with implanted behaviours (course, Part 7, F·27): built is not natural (reading sheets, part B, trap 5), and in the original auditing game the objective was stated plainly in the synthetic documents, the pipeline making it "artificially easy to discover" (reading sheet 16). Workaround: conclude only about the auditing protocols, and draw substantive conclusions from models without an organism (programme, part 8); against an organism that is too easy and the gap between implanted and natural, none known; say so (reading sheet 16; handover, §5.2).

### Insertion n°40, après la ligne 1222 de la v3.5

> Ancre : more effective but less aligned solutions than single agents. And in the register of automated oversight, automated researchers conducting weak-to-strong research outperform humans at equal budget — which brings back the question of how much trust can be placed in work that one cannot judge any bett

> ⚠ *(v3.6)* This success is on a deliberately verifiable task, fuzzier tasks remaining out of reach (course, Part 7, F·40), and an automated researcher can slow or steer research without being detected by a zero-shot prompted monitor (course, Part 7, F·60). Workaround: subtasks with verifiable ground truth, sampled human re-derivation, detection of sandbagging by the automated researchers, and a human baseline at equal budget (course, Part 5, topic 11); for fuzzy tasks, none known; say so.

### Insertion n°42, après la ligne 1226 de la v3.5

> Ancre : Fifth theme: acting at the source. The Teaching Claude Why work shows that training the model, through synthetic document finetuning, on fictional stories aligned with the constitution reduces its misalignment rate on honeypot evals. And the anti-jailbreak defense continues to evolve with a new gene

> ⚠ *(v3.6)* This rate is read on honeypots: a honeypot does not separate a model that reads it as fake from a model that holds back (reading sheet 3), the held-out ones may not be representative (reading sheet 12), and the work neither measures nor controls evaluation awareness (programme, part 1). Workaround: held-out audit metrics, never trained on, as this work does (reading sheet 12), and the gap measured with and without inhibition of evaluation awareness, at matched degradation and against control vectors (reading sheets, part C); for a honeypot read as fake, none known; say so.

### Insertion n°44, après la ligne 1232 de la v3.5

> Ancre : And you, in all this, plug in at a precise and defensible spot: at the hinge of the "evaluating alignment" direction (cognition side, with eval-awareness) and the "honesty" sub-direction of oversight (the probing-of-truth lineage). Your tools — mean-diff concept vectors, SAE decomposition — come fro

> ⚠ *(v3.6)* What this sentence unfolds has its limits, to be stated with it: the SAE decomposition goes through the open-source Goodfire SAE, which leaves 86.8% of the variance in the residual, where the read signal lives — so a failure of the features does not separate "absent from the dictionary" from "too lossy a dictionary"; and the drop obtained at rank three did not reproduce on fresh generations judged in full, the ablation softening every negative verdict, read through a truncated window (repository README). Workaround: read the signal on the reconstruction and on the residual, judge the whole answer, extract on a disjoint set, and compare against the no-pressure control and a rival concept's direction, at matched degradation (repository README; course, Part M, M4); to decide between the two readings of the SAE, none known; say so.

### Insertion n°46, après la ligne 1232 de la v3.5

> Ancre : And you, in all this, plug in at a precise and defensible spot: at the hinge of the "evaluating alignment" direction (cognition side, with eval-awareness) and the "honesty" sub-direction of oversight (the probing-of-truth lineage). Your tools — mean-diff concept vectors, SAE decomposition — come fro

> ⚠ **Limits and workarounds**: steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity; ablation and projection → Part 2, §D (after "The method"); random controls → Part M, M4 (after "The matched-norm random direction"); matched degradation and dose-response → Part M, M4 (after "Dose-response") *(v3.6)*
