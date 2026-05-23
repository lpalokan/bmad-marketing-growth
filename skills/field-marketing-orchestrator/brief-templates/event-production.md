---
brief_id: <yyyy-mm-{event-name}>
issued_by: field-marketing-orchestrator
issued_to: events-webinars-producer
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<Event type, date, target audience, pipeline target, hosting role.>

## Context (links)

- `{output_folder}/company-context/icp.md`
- `{output_folder}/company-context/positioning.md`
- `{output_folder}/company-context/brand-voice.md`
- <speaker materials, sponsorship contract, venue brief, prior
  retros>

## Deliverable

`work/{brief_id}/v1.md`: pre-event drip plan, day-of run-of-show,
post-event follow-up motion (≤ 24 hours), attribution plan,
contingency plan.

## Acceptance Criteria

- [ ] Pre-event drip: 3+ touches, segmented by registered vs invited.
- [ ] Day-of run-of-show with timing, owner, contingency per slot.
- [ ] Post-event follow-up motion starts within 24 hours (specify
      automation).
- [ ] Attribution plan distinguishes registered, attended, engaged.
- [ ] Contingency plan covers: speaker drop, AV failure, low show-up.
- [ ] Show-up rate forecast cites a source (prior events or user-
      supplied benchmark).

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- Format: <hosted dinner / summit / webinar / sponsored booth /
  conference>.
- Budget: <amount>.
- <Regulatory / venue / partner constraints.>

## Instructions

1. Read linked files first.
2. Use capability `PR` (production) from your SKILL.md.
3. Write `v1.md`; update `state.yaml`.
