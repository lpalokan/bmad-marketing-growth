---
brief_id: <yyyy-qN-abm-{segment}>
issued_by: field-marketing-orchestrator
issued_to: abm-strategist
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<Named accounts in scope, paired AE pod, stage focus, pipeline target.>

## Context (links)

- `{output_folder}/company-context/icp.md`
- `{output_folder}/company-context/positioning.md`
- `{output_folder}/company-context/kpis.md`
- <named-account list, current account intelligence, prior ABM
  programs against these accounts>

## Deliverable

`work/{brief_id}/v1.md`: account plan per tier, multi-channel
orchestration calendar, signals-to-actions matrix, AE-pairing plan,
measurement plan (no double-counting).

## Acceptance Criteria

- [ ] Account tiering: 1:1 / 1:few / 1:many with named accounts per
      tier.
- [ ] Each tier has its own orchestration (1:1 gets bespoke; 1:many
      gets programmatic).
- [ ] Signals-to-actions matrix: intent signal → channel response →
      AE handoff trigger.
- [ ] AE pairing explicit: which AE / pod is paired with which
      account, owner of each touch.
- [ ] Measurement plan defines pipeline-attribution method that does
      NOT double-count with paid-search or paid-demand.
- [ ] No invented intent signals or account-fit scores.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- Total budget: <amount>.
- AE bandwidth: <hours per account per week>.
- <Compliance / consent rules per region.>

## Instructions

1. Read linked context first.
2. Use capability `TR` (tiering), `OR` (orchestration), `SM` (signals)
   from your SKILL.md.
3. Write `v1.md`; update `state.yaml`.
