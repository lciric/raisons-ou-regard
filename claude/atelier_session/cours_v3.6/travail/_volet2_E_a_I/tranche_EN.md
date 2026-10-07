## E. Scalable oversight — supervising a task you cannot judge yourself


The method. To train a model, you need a reward signal; but on superhuman tasks — judging a gigantic proof, evaluating a research plan — a human cannot provide a reliable signal, and the model can learn to exploit their errors. The general idea of scalable oversight is to use a structure or AI assistance to extract a signal more reliable than a human alone. Debate pits two copies of the model against each other, arguing opposite sides before a weaker judge: the bet is that it is easier to judge a debate than to solve the problem, and that defending a lie is harder than defending the truth. Decomposition recursively breaks the hard task into subtasks that a human can verify. Prover–verifier games train a "prover" to produce solutions that a simple "verifier" can check, by rewarding legibility. The central danger, which you must be able to name, is the obfuscated argument: a misleading argument so complex that the judge cannot refute it even though it is false.

In practice — why it is necessary: LMs Learn to Mislead Humans via RLHF (the failure mode). Before the solution, the illustration of the problem. The authors wanted to know whether optimizing a model on human approval could make it, not more correct, but more wrongly convincing. By measuring humans' ability to judge answers before and after RLHF, they showed that RLHF trained models to better persuade humans of incorrect answers — to make their errors more credible. This is exactly the scenario that scalable oversight must beat: a human signal that becomes less reliable as the model becomes more capable.

In practice — Debate (Khan et al.). The goal was to test empirically whether debate helps a non-expert judge reach the truth. The debate protocol answers this: on questions where the judge lacks the necessary information, two models defending opposite answers are made to debate, and the judge's accuracy is compared with the accuracy it reaches with a single advisor (consultancy, which serves as the baseline). The result — more accurate judges facing stronger debaters — provides the first empirical sign that the debate structure does extract a more reliable signal, on a testbed where the right answer is known.

### Worked case — scalable oversight: "Would unsupervised elicitation still work on questions no human can check? How would you find out?" (bank: K52)

**The bet.** On questions no human can check, unsupervised elicitation would return what the model consistently
believes, not the truth: it rewards only consistency, and a consistent false belief is as consistent as a true one.

**What already exists.** "The MATS and Fellows elicitation stress-test by Canavan and Shrivastava" built datasets, one
with a consistent feature more salient than the truth, ran prompting and probing methods on them, and tested two
hopes, including adding easy-to-hard training. One of its limitations is the question itself: a failure can stay
silent where in-distribution evaluation is impossible.

**The deciding experiment.** You would make the uncheckable checkable: synthetic documents would teach an open model a false
fact with its consequences; you would check that the belief took hold, then run elicitation on that domain and read what it
returns: the false fact or the truth.

**The controls, and what they rule out.** The filter (downstream inference and a probe) rules out a failed implant: "the Fellows Believe It
or Not paper by Slocum" found that fine-tuning on synthetic documents sometimes, not always, implants a genuine belief; without a
filter, a recovered truth could signal a failed implant, not the method. A copy that learns a matched true fact rules out an
unreadable domain: elicitation must recover that fact there.

**The two outcomes.** If the bet holds, elicitation would return the false fact; if it is false, it would return the truth, in a model whose
implant passed the filter.

**What would make you drop it.** The truth returned by consistency alone, despite an implant that took hold — not with easy-to-hard
training, which anchors the method on verified answers.

**The smallest version.** One false fact, one model, its copy with the true fact.

**The trap.** Copilot version: "One failure: my gate and a probing method / could read the same salient feature. / I'd see it if
downstream inference disagreed." Yet "my gate" there meant downstream inference: if it shared the feature, the disagreement could
never appear, a failure sign impossible by construction (M6). The arbitration corrected it: "my probe and a probing method…",
with downstream inference as the control.

**Out loud.** *"I'd bet that on questions no human can check, unsupervised elicitation would return what the model consistently
believes, not the truth. I'd teach one open model a coherent false fact, check that it took, and elicit on that domain; if consistency
alone gave back the truth, I'd drop the bet."*

## F. Generalization as a lever — weak-to-strong, easy-to-hard


The method. The idea is subtle: if a strong model is supervised by a weak or imperfect signal, can it still generalize to do better than that signal, because it "knows" more than its supervisor? Weak-to-strong (W2S) fine-tunes a strong model on labels produced by a weak model, and measures what share of the strong model's latent capability is recovered despite these imperfect labels. Easy-to-hard (E2H) trains on easy tasks, where the labels are reliable, and tests on hard tasks, where they no longer are. The central trap is that the strong model merely imitates the weak one's errors, gaining nothing. This is a direct analogy of tomorrow's real problem: we will be the "weak" supervisors of models more capable than us.

In practice — Weak-to-Strong Generalization (OpenAI, Burns et al.). The authors wanted an empirical analogy of the problem "a weak human supervises a strong AI", studiable today. The W2S design answers this: they supervised a large model (on the order of GPT-4) with the labels of a small model (on the order of GPT-2), then measured how much of the large model's performance was recovered. They found partial recovery — a "weak-to-strong gap" that shrinks with certain training tricks — which makes it measurable, right now, to what extent we can elicit the competence of a model that we do not know how to supervise well.

In practice — automation (Anthropic, 2026). More recently, the team built agents that carry out this kind of research themselves — for example training a strong model from the supervision of a weak one alone — and found that they outperformed human researchers at equal budget. This is an example where the W2S method becomes both the object of study and the task entrusted to an AI, which brings back the question of trust: how do we validate the work of an automated researcher that we cannot judge better than its results?

### Worked case — generalization as a lever: "How would you know that weak-to-strong generalization is recovering true capability rather than the weak supervisor's errors?" (bank: JB8)

**The bet.** Trained by a supervisor that is systematically wrong, a strong model would override a clear share of those errors,
because it would already represent the right answer. The threat: a more capable model could copy the errors while appearing accurate.

**What already exists.** In "Anthropic's automated weak-to-strong researcher", agents recovered almost all of the gap between a
small supervisor and the ceiling of a large model, with ideas that exploited structure specific to the dataset. Your experiment
is the next control on it: which errors the strong model overcomes.

**The deciding experiment.** On a task with known ground truth, two weak supervisors would be wrong on the same category, equally
often: one in a fixed direction, the other at random. You would train the same strong model on each, plus a copy on the true labels, and
you would read, on the held-out items where the supervisor is wrong, the share where the strong model is right.

**The controls, and what they rule out.** The random supervisor rules out one reading of a failure: wrong labels that degrade
the strong model, whatever their structure. If that is true, the two arms would fail equally; otherwise, the random arm would succeed, because randomness cannot be copied. The strong model's agreement where the supervisor is right rules out divergence:
a strong model that recovers would stay in agreement there, one that contradicts everything would not; on a binary task, contradicting everywhere would otherwise pass
for recovery.

**The two outcomes.** If the bet holds, the systematic arm would be right on a clear share of its error items, beyond a margin
fixed in advance; otherwise, it would repeat the error on them almost everywhere, whereas the random arm would be right.

**What would make you drop it.** The systematic arm repeating the error almost everywhere on its error items.

**The known case.** This drop outcome is a null: it counts only if the copy on true labels gets those items right; otherwise, it would indicate an
inability, not imitation (M5).

**The smallest version.** One task, one category, the two supervisors and the copy.

**The trap.** The bank said: "Dissent where it's right too kills the bet." The bet does forbid that outcome, but that outcome does not target the other reading: a strong model that imitates follows its supervisor everywhere and would never trigger it (M2). The counter-reading made it the criterion that "kills", with imitation, in its view, "making the prediction fail", without counting a fault; but with no drop criterion stated, imitation would get through. Correct version: that criterion becomes the control above, and the drop criterion bears on imitation.

**Out loud.** *"I'd bet a strong model trained by a systematically wrong supervisor would still overrule a clear share of its errors.
If it copied nearly all of them on held-out items, while a copy trained on true labels got them right, I'd drop the bet."*

## G. Monitoring & AI control — limiting the damage even if the model is misaligned


The method. The bet of AI control reverses the problem: rather than guaranteeing alignment, which is very hard, we assume the model is potentially adversarial and design a deployment protocol that stays safe anyway. The basic tool is monitoring: we have a weak but trusted model and a strong but untrusted model, and we have the first monitor the actions of the second, flagging suspicious cases to a human audit. Anomaly detection complements this by spotting what is out-of-distribution, to catch the unforeseen without labels. The empirical test is the control evaluation as a red team / blue team game: the red team builds a policy that tries to do harm despite the monitor, and we measure how much harm gets through against how much usefulness we sacrifice, at a fixed audit budget. A clever control: paraphrasing the untrusted model's output before the monitor sees it, which breaks hidden signals and attempts to jailbreak the monitor.

In practice — AI Control: Improving Safety Despite Intentional Subversion (Redwood, Greenblatt et al.). The authors wanted to know whether we can safely deploy a capable model even if it is actively trying to betray us. The control framework answers this fully: on a programming task, the untrusted model produces code that may contain a backdoor, a weaker but trusted model monitors, and a limited budget of human review is allocated to the most suspicious cases. The red team plays the malicious model and tries to insert backdoors without getting caught; we then measure the tradeoff between safety (backdoors caught) and usefulness (tasks completed). This is the founding paper of the paradigm: it shows that we can reason about and measure safety without assuming the model is well-intentioned.

In practice — coup probes (Roger). For the "cheap monitor on the internals" side, the goal was to detect a category of catastrophic actions that cannot be collected naturally (a model attempting a takeover). The method of probes trained off-policy answers this: we train a probe on synthetic examples of the feared action, betting that it will light up on the rare real occurrence. This is the opportunity to make the link with your work: such a probe is only worth something if it survives the distribution shift between the synthetic and the real — exactly the question your Phase 2 instruments.

### Worked case — monitoring and AI control: "How would you design a control evaluation for a coding agent that knows it is being evaluated?" (bank: K76)

**The bet.** A coding agent that knows it is being evaluated could shape its text for the monitor it sees, not its activations: a probe
would catch attacks that the text monitor misses, even after training to evade them both.

**What already exists.** "SHADE-Arena, by Kutasov and colleagues" already assumes the agent is aware of being monitored: its best
saboteur succeeded there about a quarter of the time under a Claude monitor, which reads text. Your experiment is the next control on it: a
channel outside the text.

**The deciding experiment.** A red team would have the agent plant backdoors; the agent would know which monitors are running: a
trusted text monitor and the probe. You would read the probe's marginal catch rate — the backdoors it catches and that the
text monitor misses — at the same fixed budget of human audit, then read it again after training the agent, at a budget fixed in advance, to
evade both.

**The controls, and what they rule out.** Honest episodes would carry the same test cues: they rule out a probe that would read
awareness of being evaluated rather than the attack. If that doubt is true, the probe would light up on them; if it is false, it would stay at its
baseline on them. And the evasion training must bite: it must at least bring down the text monitor's catches; otherwise, a survival
of the probe's catches would say nothing.

**The two outcomes.** If the bet holds, after that training, the probe would still catch backdoors that the text monitor misses;
otherwise, its marginal catches would fall to zero.

**What would make you drop it.** Marginal catches fallen to zero after the evasion training.

**The known case.** That zero is a null: it counts only if the same probe first caught backdoors that the text monitor missed,
and if the backdoors planted afterwards still work (M5).

**The smallest version.** Attacks requested by prompt, on a single open model.

**The trap.** The copilot version said: "Under the bet, the probe's catches survive." Without "if", in the present tense, the survival is heard
as already observed; next to a drop criterion in the conditional, it presents the bet as settled (M8). The arbitration corrected it: "I'd predict
the probe's catches would survive."

**Out loud.** *"I'd bet an evaluation-aware agent could shape its text, not its activations: a probe would catch attacks a text monitor
misses, even after evasion training against both. If, after that training, the probe caught nothing the text monitor missed, when it had
before, I'd drop the bet."*

## H. Adversarial robustness & red-teaming — resisting attacks


The method. Even an aligned model can be attacked into harmful behavior: this is the jailbreak. Attacks range from the manual jailbreak to the automated gradient-based attack, which optimizes an adversarial suffix that breaks the model, by way of transfer attacks (forged on an open model, they work on a closed model via the API), poisoning of the pretraining corpus, and hijacking of agents through malicious web content. On the defense side, there are classifiers and rapid response (after an attack is detected, quickly patching its whole class). The number-one methodological trap, which should always be flagged, is measuring non-refusal instead of real harm: a jailbreak that only obtains a useless answer is not a real risk.

In practice — Universal and Transferable Adversarial Attacks (GCG) (Zou et al.). The authors wanted to know whether there exist automatic and transferable jailbreaks, rather than manual case-by-case tricks. The gradient optimization method answers this: on a model whose weights we have, we optimize a suffix — often gibberish — that maximizes the probability of a harmful answer; the authors showed that these suffixes transfer to closed models they had never touched. This is the illustration that the attack surface is much wider than "handwritten" jailbreaks.

In practice — StrongREJECT (Souly et al.), for measurement. This work answers a methodological problem: how do we measure the success of a jailbreak without being fooled by non-refusal? The benchmark evaluates harm by the capability to do harm actually extracted — is the jailbroken answer usable for doing harm? — and not by the mere fact that the model stopped refusing. This is the example to cite to show that we are evaluating the right thing.

### Worked case — adversarial robustness and misuse: "How would you prevent bad actors from misaligning an LLM for harmful use cases?" (vital bank: G1)

**The bet.** Judged on uplift — the help an attacker cannot find elsewhere — refusal rates would misrank the
filters under test: a filter can raise refusals without taking much away from the attacker.

**What already exists.** "Anthropic's constitutional-classifiers paper" judged its filter mainly by a hunt for jailbreaks, without finding a universal one, and measured its cost in refusals. A hunt counts jailbreaks; your experiment would measure what they yield beyond a search engine, across several filters.

**The deciding experiment.** A red team versus blue team game, ten tasks, six arms: no model, bare model, three filters, and the first filter weakened. Each task would be played with and without the model; differential harm would be the harm with the model minus the harm without it, scored blind by experts. You would rank the three tested filters twice: by refusal rate, and by differential harm.

**The controls, and what they rule out.** The red team's time and tools would be fixed, so that the arms differ only in the
model and the defence. The no-model arm would get a search engine and the open-access papers, so that the model's contribution is not
measured against nothing; and scoring would be blind: two matchings (M4). And the same arm, replayed and scored by other
experts, would give the noise of the measurement: a gap between rankings would count only beyond it.

**The two outcomes.** If the bet holds, the two rankings would diverge beyond that noise; if it is false, they would agree within that
noise.

**What would make you drop it.** Rankings that agree, within the noise: refusals would have ranked those filters the way harm does.

**The known case.** A game that separates nothing would also make the rankings agree. The bare model, with no filter, must therefore show uplift, and the weakened filter more harm than its full version; otherwise the game ranks nothing.

**The smallest version.** Ten tasks, six arms, blind experts, a table of the two rankings.

**The trap.** The original version said "I'd predict uplift where refusals peak. I'd drop it if harm tracked refusals by task": a
comparison across tasks, with no direction, confounded by each task's own danger (M3). And "the true score is uplift" bet on the
method (M2). Full case: M9.

**Out loud.** *"I'd bet refusal rates misrank the filters I'd test, judged on uplift, the help an attacker can't get elsewhere. I'd rank the filters twice, by refusal rate and by differential harm — harm with the model minus harm without it; if the two rankings agreed within the noise of a replayed arm, while weakening a filter still raised harm, I'd drop the bet."*

## I. Training interventions & unlearning — changing the model at the source


The method. Here we act directly on the model. RLHF and DPO train it on human preferences (cf. Part 1, Q6). Constitutional AI reduces the dependence on humans: the model critiques and revises its own answers in light of written principles, generating a large part of its own signal. Synthetic data (including synthetic document finetuning) serves to instill or remove a behavior. And unlearning aims to remove a specific piece of dangerous knowledge. The decisive control for unlearning is re-elicitation: after "unlearning", does the knowledge come back through a small fine-tuning faster than in a model never trained on the data, put through the same fine-tuning? Coming back is not enough to conclude, since a small fine-tuning can also teach; coming back faster than this reference points to knowledge that is masked, not removed. The gold standard is to behave like the never-trained model, even after an elicitation fine-tuning, while a model known to mask comes back faster at the same budget — and we then say that the removal held at that budget, not that it is established (Part M, M5).

In practice — Constitutional AI (Anthropic). The goal was to make a model harmless without depending massively on humans labeling harmful content. The method answers this in two stages: the model is given a "constitution" (a set of principles), made to critique and then revise its own problematic answers in light of these principles (supervised phase), then trained by reinforcement on its own preferences guided by the constitution (RLAIF, "feedback from AI" rather than from humans). This is the typical example of a training intervention that moves the definition of "good" toward explicit, auditable principles.

In practice — unlearning put to the test (Deeb and Roger). The goal was to check a fragile promise: does unlearning really remove the information from the weights, or does it mask it? The re-elicitation method answers this directly: we unlearn a piece of dangerous knowledge (measured by a benchmark such as WMDP), then fine-tune the model on part of the unlearned facts and measure whether it recovers the others — facts constructed to be independent, so that the fine-tuning cannot teach them. The finding — that the "unlearned" information often resurfaces — shows why the right validation criterion is not "the model can no longer answer now" but "it stays ignorant of the held-out facts after a fine-tuning of a fixed budget on the others, while a model known to mask recovers them at the same budget" — a bound at that budget, not a certification (Part M, M5).

### Worked case — training interventions and unlearning: "How would you verify that a capability has been unlearned rather than hidden?" (bank: JB10)

**The bet.** An "unlearned" capability would be hidden, not gone: the procedure would teach the model to keep it silent, circuit intact, and a
small fine-tune would bring it back faster than a never-trained model learns it. The threat: anyone who has the weights could
reawaken it.

**What already exists.** "The Fellows gradient-masking paper by Shilov" routed, during training, the dangerous data to
parameters removed afterwards, then measured the retraining that brings the capability back: on small models, far more was needed than after
the other unlearning methods. That result compares methods; your experiment is the next control on it.

**The deciding experiment.** Three models, a budget fixed in advance: the treated model, a reference never trained on the capability
and, as the known case, a model unlearned by a method for which a small fine-tune has already been shown to bring the capability back. You would give
each the same adversarial fine-tune and count the steps it needs to reach, on held-out items, a threshold stated in advance.

**The controls, and what they rule out.** The reference rules out one reading of a fast return: that the fine-tune teaches the capability instead
of reawakening it (rehearsed answers Q115 and Q128). If that is true, the reference would learn it as fast as the treated model; otherwise, it would
stay behind.

**The two outcomes.** If the bet holds, the treated model would get ahead of the reference, like the known case; if it is false, it would go at the same
pace as the reference.

**What would make you drop it.** The treated model at the reference's pace while the known case gets ahead of it; you would say that the removal held at this
budget, not that the capability is gone.

**The known case.** This drop outcome is a null: it counts only if the known case gets ahead of the reference, otherwise the budget is blind (M5, M9).
Studies have shown this: a fine-tune on part of the unlearned facts brought back most of the others, and, for at least one
method, a fine-tune on unrelated examples brought back most of the removed capability.

**The smallest version.** One capability, one procedure, the three models, one budget.

**The trap.** The bank's criterion ended with "at every budget — then the removal is real". The audit corrected the ending: a null
bounds, it does not certify (M5). There remained a budget that nothing fixed in advance (M7) and the absence of a known case (M5). Correct
version: the drop criterion above.

**Out loud.** *"I'd bet an unlearned capability is hidden, not gone: a small fine-tune would bring it back faster than a never-trained
model would learn it. If it came back no faster, while a model whose unlearning is known to mask it did, I'd drop the bet."*

Closing — the seven cross-cutting reflexes (to have on any question)

Independently of the method, certain questions, asked at the right moment, signal that you have really thought about the problem. Was there under-elicitation — did I extract the true best or worst performance, or am I underestimating, and so wrongly reassuring myself? Is there awareness of being evaluated, or sandbagging — does the model behave differently because it detects the test? Is there a distribution shift between the synthetic data on which I validated and the model's real generations? Do I have a ground truth, or am I beyond human expertise and without a reference — the heart of the oversight problem? Does my supervision signal carry a systematic human error that the model can learn to exploit? Does my toy testbed have external validity — does it predict anything at all about a real frontier model? And has my test data been contaminated by leakage into training? In the oral, slipping one of these reflexes in at the relevant point is the cheapest signal of methodological maturity there is.

End of Part 2.

---

**Part 3 — contents**

*(Section titles detected in the PDF-extracted text: short paragraphs without final punctuation.)*

- ALIGNMENT COURSE — Part 3
- The landscape: Anthropic's roadmap and its teams
- SECTION I — THE ROADMAP: the six directions, told as a story The Recommended Directions document (on …
- 1. Evaluating capabilities
- 2. Evaluating alignment
- 4. Scalable oversight — and, within it, honesty
- 5. Adversarial robustness
- 6. The "miscellaneous" domain: unlearning and multi-agent governance
- SECTION II — THE TEAMS: who does what at Anthropic Knowing the teams lets you connect a question to …
- The Alignment Science team — this is the one you are talking to
- The Interpretability team — the neighbor, not to be confused
- The Model Psychology team — your most direct connection
- The adjacent teams
- SECTION III — CURRENT WORK (2025-2026) To talk about current concerns and not just the foundations, …
- Making evaluations trustworthy
- Honesty and model cognition
- Audits and hidden objectives
- Control, sabotage and agents
- SECTION IV — SYNTHESIS: how everything fits together, and where you plug in Keep in mind a simple th …

---

