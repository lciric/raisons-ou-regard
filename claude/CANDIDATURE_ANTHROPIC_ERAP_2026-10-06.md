# Anthropic External Researcher Access Program — form answers

<!-- Draft prepared on 6 October 2026 by a Claude Code session, for Lazar to complete and submit himself. Nothing has been sent. Every [[...]] is his to fill or to decide. Form: https://forms.gle/pZYC8f6qYqSKvRWn9 (its 14 questions, read on 6 October 2026). The program grants free API credits, usually 1,000 USD, to AI safety and alignment researchers; submissions are reviewed on the first Monday of each month (next: Monday 2 November 2026), and unapproved submissions get no individual answer. Never paste an API key into the form: it asks for the Organization ID only. -->

**1. Email** *(required)*
[[your email]]

**2. Name of primary contact** *(required)*
[[your full name]]

**3. Name of organization (if applicable)**
[[leave empty, or "Independent researcher"]]

**4. Have you been recommended to this form by an Anthropic employee?** *(required)*
No [[or Yes, if someone at Anthropic suggested it]]

**5. If you have been referred to this form by an Anthropic employee, please enter their name here**
[[empty unless 4 is Yes]]

**6. Which Organization ID would you like the credits applied to?** *(required)*
[[the Organization ID of the Console account that the programme's API key belongs to: console.anthropic.com → Settings → Organization]]

**7. In less than 200 words, please provide a brief description of the individual applicant or team, including the relevant expertise.** *(required; 109 words before your part: about 90 left for your background)*

> [[Your name]] is an independent researcher. [[Background: field, degrees, prior research or engineering work, 1 to 3 sentences.]] Since October 2026, [[he]] has run "Reasons or being watched?", a self-funded AI safety research programme. It studies evaluation awareness and how reason-based fine-tuning generalizes in open models. The work combines model organisms, activation probes and interventions (projection, linear concept erasure), controls matched on output degradation, and decision rules written before the data. Implementation is carried out with Claude Code sessions under [[his]] direction, and every decision is dated and logged. So far the programme has produced a 135-page research plan and a tested codebase. It has built a first model organism on Llama-3.1-8B-Instruct, with a 54-point evaluation-conditional gap, and an evaluation-awareness probe validated on held-out cues.

**8. In less than 300 words, please describe your research or request for free API credits.** *(required; 292 words)*

> **Research.** The programme asks whether the out-of-distribution advantage of training a model on the reasons for aligned behavior, rather than on the same actions alone, depends on the model's representation of being evaluated. I fine-tune Llama-3.1-8B-Instruct with LoRA on six arms with identical aligned actions, with format and content controlled. I then inhibit a validated internal representation of evaluation awareness, and compare it with random subspaces and separate controls matched on output degradation. This measures how much of the reasons' advantage depends on that representation. The instrument is first validated on model organisms whose behavior is conditioned on evaluation cues.
>
> **What the credits pay for.** In line with the Usage Policy, the arms' training data are written by an open-weights model: Claude never writes training targets. Claude:
> - judges every generated training item (action fidelity, reason quality, neutral control texts, no evaluation-awareness wording);
> - generates the matched pairs of evaluation and deployment cues that build and validate the probes, with lexical gates so that a probe cannot succeed by reading the cue words;
> - generates the held-out scenario families used for evaluation;
> - judges stratified subsamples.
>
> The cue sets and the pipeline pilot have cost about 35 USD so far. Judging the full training data is estimated at 100 to 300 USD, and the evaluation material and remaining judging at several hundred dollars more.
>
> **Why they matter.** The programme is self-funded, and its budget ran out on 6 October, in the middle of the procedure that fixes the inhibition setting. Credits would let the data generation go ahead while compute funding is sought, so that the first experiment is not delayed. The results and the pre-registration will be published with the first post and paper.

**9. Are you requesting more than $1000 API credits?** *(required)*
No. [[Recommended: the standard amount has the best chance. The other choice is "Other" with an amount; the first paper alone needs about 1,000 to 1,500 USD of API since decision 37 (8 October: the training data are written by an open model), so 1,500 USD could be justified in question 12.]]

**10. Would this be a significant hindrance for your research / use case?** *(required)*
"I'm fine with receiving a low quality of service" [[recommended: the generation runs offline, in batches, and does not need low latency]]

**11. Please provide a link to your Google Scholar profile or github profile** *(required)*
[[link; the programme's repository is private]]

**12. Additional Information** *(optional)*

> The full programme (v1.6), its decision log and the run registry can be shared with reviewers on request. Total API needs for the first paper are estimated at 1,000 to 1,500 USD; compute funding is being sought separately.

**13. Are you located within the United States?**
[[Yes / No]]

**14. Terms of Service** *(required)*
[[read them, then tick "I agree"]]
