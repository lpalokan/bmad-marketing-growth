---
brief_id: <slug-fit-scoring>
issued_by: sales-prospecting-orchestrator
issued_to: fit-scoring-strategist
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<One paragraph. What must exist and why now — e.g. "Score {account}'s offering
fit and timing separately against the scoring model and emit an action tier, so
the Q3 motion knows whether to prioritize now, sequence, nurture, or deprioritize
this account.">

## Context (links)

- `{output_folder}/company-context/icp.md` (if present)
- `{output_folder}/company-context/icp-fit-model.md` (if present — the rubric to score against)
- `{output_folder}/company-context/offerings.md` (if present — what we're matching to)
- `{output_folder}/work/{account-id}/account-profile.md` (Remy's profile — the scoring input)
- <add: the signal scan for this account, if present>

## Deliverable

Write `{output_folder}/work/{account-id}/fit-scorecard.md` (as `v1.md` in the
work folder). Include: a **Fit** score (firmographic / technographic / persona
sub-scores on the model's rubric), a **separate Timing** score (triggers/intent),
a pain→product-alignment map (severity × alignment), an overall **Priority**
(Fit × Signal-strength × Strategic-value) with the arithmetic shown, and an
explicit **action tier** (prioritize now / into sequences / nurture / deprioritize).

## Acceptance Criteria

- [ ] Fit and Timing are scored and reported **separately** — never collapsed into one figure.
- [ ] Each is scored on the model's rubric (firmographic / technographic / persona for fit; triggers/intent for timing).
- [ ] Pains are mapped to product alignment (pain severity 1-5 × product alignment 1-5), each naming the offering.
- [ ] An overall Priority and an **explicit action tier** are stated; a deprioritize verdict is said plainly.
- [ ] Every scoring input carries a source; the working (weights, sub-scores, arithmetic) is shown.
- [ ] Gaps are marked `[UNKNOWN — needs input]`, not filled with guessed factors.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- <e.g. score against the current `icp-fit-model.md`; do not re-tune the model inside a scoring run; confidentiality of sources; depth vs speed>

## Instructions

1. Read the Context (links) that exist. Do not block on missing context.
2. Use capability SF (score fit ✕ timing + action tier). If the scoring model is missing or clearly stale, flag it — tuning the model is capability TM, a separate brief.
3. Score fit and timing separately on the model's rubric; map pains to product alignment; compute Priority and emit the action tier — showing the working and sourcing every input.
4. Write `v1.md`; set `state.yaml` `status: in-review`; notify the orchestrator.
