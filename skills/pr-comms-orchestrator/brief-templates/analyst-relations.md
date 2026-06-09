---
brief_id: <yyyy-mm-{analyst-or-submission}>
issued_by: pr-comms-orchestrator
issued_to: analyst-relations-specialist
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<Scope: routine briefing / MQ / Wave / inquiry / post-publication.>

## Context (links)

- `{output_folder}/company-context/positioning.md`
- `{output_folder}/company-context/icp.md`
- <analyst's evaluation criteria URL, prior briefing notes, analyst's
  recent published work, our prior submission if MQ/Wave>

## Deliverable

`work/{brief_id}/v1.md`: prep deck mapped to analyst's evaluation
criteria; spokesperson per topic; expected outcome; follow-up plan.

## Acceptance Criteria

- [ ] Prep deck explicitly maps to the analyst's published evaluation
      criteria (slide per criterion).
- [ ] Spokesperson named per topic; speaker briefed.
- [ ] Expected outcome stated (rating movement, inquiry resolution,
      coverage angle).
- [ ] Follow-up plan: thank-you, transcript review, action items.
- [ ] No invented customer counts, revenue claims, or competitive
      stats — all sourced or marked `[source pending]`.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- Analyst firm + analyst: <name>.
- NDA / embargo: <as applicable>.

## Instructions

1. Read linked files first.
2. Use capability `BR` (briefing) or `MQ` (MQ/Wave submission) as
   appropriate.
3. Write `v1.md`; update `state.yaml`.
