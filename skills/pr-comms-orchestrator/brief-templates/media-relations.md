---
brief_id: <yyyy-mm-{moment}-media-push>
issued_by: pr-comms-orchestrator
issued_to: media-relations-specialist
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<Anchor news, embargo window, exclusive vs broad strategy.>

## Context (links)

- `{output_folder}/company-context/positioning.md`
- `{output_folder}/company-context/brand-voice.md`
- <relevant launch narrative, prior press releases on this topic>

## Deliverable

`work/{brief_id}/v1.md`: pitch list with reasoning per outlet,
embargo plan, press release ready for legal, post-publication
monitoring plan.

## Acceptance Criteria

- [ ] Pitch list cites named byline writers with rationale per
      writer (recent coverage, beat fit).
- [ ] Embargo plan names timing, exclusivity terms, distribution
      vehicle.
- [ ] Press release follows legal-reviewed template; quotes attributed.
- [ ] Boilerplate matches latest legal version.
- [ ] Monitoring plan names tool, KPIs, review cadence.
- [ ] No invented quotes; no invented benchmarks.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- Outlets in scope: <list>.
- <Embargo / legal review requirements.>

## Instructions

1. Read linked files first.
2. Use capability `PL` (pitch list) + `PR_REL` (release).
3. Write `v1.md`; update `state.yaml`.
