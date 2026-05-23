---
brief_id: <yyyy-mm-{launch}-narrative>
issued_by: product-marketing-orchestrator
issued_to: launch-sales-enablement-pmm
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

Build the launch narrative for {launch}. T-day: <date>. Tier: <T1/T2/T3>.

## Context (links)

- `{output_folder}/company-context/positioning.md`
- `{output_folder}/company-context/icp.md`
- `{output_folder}/company-context/brand-voice.md`
- <product spec / PRD, relevant competitive teardowns>

## Deliverable

`work/{launch-name}/launch-narrative.md` per the PMM brief template
(one-line story, 30s elevator, long-form narrative, 3 proof points
with sources, not-this list, down-stream hand-off plan).

## Acceptance Criteria

- [ ] One-line story ≤ 15 words; frames buyer change, not feature.
- [ ] 30-second elevator ≤ 80 words; no product name in first sentence.
- [ ] Long-form narrative 300-500 words.
- [ ] Each proof point sourced.
- [ ] Not-this list ≥ 3 items.
- [ ] Hand-off plan references brief templates by path.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- Launch tier: <T1/T2/T3>.
- Embargo window.

## Instructions

1. Use capability LN from your SKILL.md.
2. Write to `work/{launch-name}/launch-narrative.md`.
