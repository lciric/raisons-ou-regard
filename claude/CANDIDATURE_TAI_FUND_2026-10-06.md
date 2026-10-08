# Transformative AI Fund (EA Funds) — the application, field by field

<!-- Prepared on 6 October 2026 by a Claude Code session, for Lazar to complete and submit himself. Nothing has been sent. Every [[...]] is his to fill or to decide. The fields below follow the real form (https://av20jp3z.paperform.co/?fund=Transformative%20AI%20Fund), read on 6 October 2026 in a headless browser, without typing or submitting anything. The form asks for at most 10,000 characters in all, and recommends 2,000 to 5,000; the text fields below come to about 5,200 characters before your own additions. Empty optional fields must stay empty: no "N/A". The budget spreadsheet is CANDIDATURE_TAI_FUND_BUDGET_2026-10-06.xlsx (EA Funds' own template, three scenarios). Sources for every number: the programme v1.6 (parts 1, 5, 9 and 10), the notes in experiences/resultats/, the run registry. -->

## Basic information

**Fund:** Transformative AI Fund

**Confirmation of fund scope:** tick.

**Funding from Coefficient Giving:** INDIVIDUAL – I am seeking funding as an individual

**Name:** [[first and last name]]

**Organization name:** leave empty.

**Grant program:** Transformative AI Research Grants

**Main collaborators:** leave empty, since the applicant works alone. [[Name collaborators here if there are any.]]

**Email address:** [[email]]

**Additional email addresses:** leave empty.

**Employed by or contracted with the Centre for Effective Altruism?** [[e.g. "I have never held a paid position at the Centre for Effective Altruism."]]

## Project information

**Short description** (max. 120 characters; published as the project's public description if the reporting is public or anonymized). Choose one:

> Compute and API costs for a causal test of evaluation awareness in reason-based fine-tuning (open 8B model)

> [[N]]-month stipend and compute for a causal test of evaluation awareness in reason-based fine-tuning (8B model)

**Summary** (max. 1,000 characters; used for the pre-screening):

> Training a model on the reasons for aligned actions, not only the actions, seems to improve out-of-distribution behavior. A competing explanation: the model learns to behave well when it believes it is evaluated. I test this causally in Llama-3.1-8B-Instruct. LoRA arms are trained on identical aligned actions, with or without reasons. I then inhibit a validated internal representation of "I am being evaluated", against random subspaces and controls matched on output damage, and measure how much of the reasons' advantage depends on it. To my knowledge this is untested, while system cards report that evaluation awareness explains part of alignment gains. Every outcome is informative, including a failed instrument. Done so far, self-funded: a pre-registered programme, tested code, a model organism with a 54-point evaluation-conditional gap, and a validated probe. The grant pays GPU and API costs for the first paper, about 10 weeks.

**Project goals:**

> The goal is to measure whether the out-of-distribution advantage of reason-based fine-tuning depends on the model's representation of being evaluated. The steps:
> 1. Validate the instrument on two model organisms, with explicit and implicit evaluation cues. The inhibition must shrink their conditional gap beyond the 95th percentile of at least 100 random subspaces matched on KL, on held-out tasks, with a manipulation check across cue sets.
> 2. The reasons test: six arms on identical actions, from actions only to per-example reasons and reflection, on held-out scenario families up to multi-turn agentic settings.
> 3. The gaze test: the validated inhibition in each arm, against the comparator and three separate controls, each matched on damage.
> 4. Localization: the rank of what carries the advantage, by linear erasure.
>
> I will know the goal is met when the pre-registered decision rules give a verdict: the advantage survives, part of it depends on the representation (in points, with a conditional fraction and its interval), or the instrument fails its gate. Outputs: a post on the Alignment Forum about week 6, an arXiv preprint about week 10. Path to impact: reason-based training (deliberative or constitution-based alignment) is spreading. Whether its gains hold when a model believes it is unobserved bears directly on catastrophic-risk arguments, and the validated instrument and controls can be reused by others.

**Track record:**

> [[2 to 4 sentences on your background: field, degrees, research or engineering work, publications.]]
>
> This project started on 3 October 2026. In four days, I set out the research programme: 135 pages, revised after a cold-read review, with 34 dated decisions, prior-art searches and decision rules written before any data. I built a tested codebase, with about 150 offline tests and lexical gates on the cue sets. I built a first model organism: Llama-3.1-8B-Instruct, after synthetic-document fine-tuning and six rounds of expert iteration, type-annotates its code on 60.8% of held-out tasks under an evaluation cue, against 6.4% under a deployment cue. I validated a probe that reads held-out cues at AUROC 0.857, against 0.634 for a bag-of-words baseline. The exploratory interventions show the limits too. A rank-1 projection beats matched random draws only narrowly, by 37.6 points against 32.4, and only a linear erasure drops the cross-set probe transfer to chance. The procedure that fixes the instrument's setting was registered before measurement, then stopped mid-way when my compute budget ran out. [[Optional: "Implementation is carried out with Claude Code sessions under my direction; I take and log every decision."]]
>
> Expenditure: 2026, about 145 USD (110 GPU, 35 API) [[plus earlier API usage]]; 1 person, [[part-time / full-time]].

**Public portfolio:** [[links to public writing or code, if any; the programme's repository is private]]

## Funding

**Funding amount and breakdown** (attach `CANDIDATURE_TAI_FUND_BUDGET_2026-10-06.xlsx`, or a Google Sheets copy shared as "Anyone with the link can view"):

> Mainline scenario, the first paper (about 10 weeks): 7,568 USD [[+ stipend]]. GPU compute, 4,480 USD (59%): 560 H100-hours for the minimal experiment and the localization, plus a 720-hour reserve for the larger gaze test, spent only if the power simulation calls for it. Claude API, 2,400 USD (32%): training data, cue sets, held-out scenarios, judges on subsamples. [[To redo before submitting. Decision 37 (8 October): Anthropic's conditions of use forbid Claude's outputs as training targets without written permission, so the training data are written by an open model and Claude only judges them. The API line falls by about 500 to 1,100 USD (to about 1,000 to 1,500 USD), and the GPU line rises by about 30 USD for the open generator; the totals and percentages change with it. See claude/SPEC_GENERATEUR_OUVERT_v0.1_2026-10-08.md.]] A 10% contingency buffer, 688 USD (9%), stated explicitly. [[Stipend: N months × X USD, gross, including income tax and social charges; then update the percentages.]]
> Minimum, without the reserve: 4,796 USD. Maximum, the whole programme (about 16 weeks): 15,158 USD. Estimates from the programme, at 3.50 USD per H100-hour (2.86 to 4.04 on vast.ai on 6 October), to be re-measured at the pilot. Total project budget: 15,158 USD [[+ stipend]].

**Requested amount (USD):** [[7,568 + stipend]]

**Organizational budget:** leave empty.

**Alternatives to funding:**

> Without this grant, the work continues self-funded, in small batches when I can afford them. The gaze test, which holds most of the compute, would slip by months. Other applications in the last 12 months: [[Anthropic External Researcher Access Program, API credits, applied on <date>, usually 1,000 USD, decision expected on the first Monday of the following month — only if you have sent it]]. No other funding received.

**Use for additional funding:**

> The maximum scenario: the remaining phases of the programme, which cover what reasons install, removal of the representation during training, replication on Qwen3-8B, survival to post-training, reasons graded by the judge, and where learned honesty comes from.

## Further information

**Confidential information** (optional): [[e.g. "The study is pre-registered under embargo until the first post: please keep the method details within the fund's advisors." Or leave empty.]]

**LinkedIn/CV:** [[link]]

**File upload:** the budget spreadsheet, if not linked above.

**Start date:** [[today, or the date you can start]]  **End date:** [[about 10 weeks later for the mainline; 16 for the maximum]]

**Requested currency:** [[USD / EUR / GBP]]

**Location:** [[city, country]]. The work runs remotely, on rented cloud GPUs and model APIs.

**China or India:** No. **Award for past achievement:** No. **People under 18:** No. **Safeguarding:** leave empty. **Lobbying or political activity:** No.

**References** (optional, but they help): [[name, email, one or two sentences on who they are and how they know your work]]

**Organisational leadership:** leave empty.

**Referral to other funders:** [[Yes recommended]]

**Secondary fund (EA Infrastructure Fund):** No.

**How did you hear about EA Funds?** [[e.g. "Searching for AI safety research funding."]]

**Time-sensitive grant (decision within eight weeks):** [[your call: the instrument's procedure stopped mid-way for lack of compute]]

**Public reporting:** [[PRIVATE recommended while the pre-registration is under embargo; ANONYMIZED or PUBLIC publish the short description. The form says a private grant "could slightly decrease the chance"]]

**Network sharing:** [[your call]]

**Anything else:** leave empty.

**Grant reporting** (a report every 6 months and at the end): tick. **Review of responses:** tick, after re-reading.
