---
brief_id: <yyyy-qN-positioning>
issued_by: product-marketing-orchestrator
issued_to: positioning-messaging-pmm
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<One paragraph. What needs to exist when this is done, and why now —
e.g. "Refresh the positioning statement and three messaging pillars
for the FY27 launch of {product}. Current positioning is 18 months
old and no longer matches the buyer we win against.">

## Context (links)

- `{output_folder}/company-context/icp.md`
- `{output_folder}/company-context/positioning.md` (current)
- `{output_folder}/company-context/brand-voice.md`
- <add: links to win/loss notes, latest analyst report, latest pricing
  page, or prior competitive teardowns>

## Deliverable

Write the following files under `{output_folder}/work/{brief_id}/`:

- `v1.md` — full deliverable. Include:
  - Updated positioning statement (full template),
  - Value pyramid (3 layers, ICP-specific),
  - Messaging pillars (exactly 3),
  - For each pillar: 3+ proof points with sources,
  - Anti-positioning section (what we are NOT).

## Acceptance Criteria

- [ ] Positioning statement uses the full template (For X who Y, Z is a
      A that B, unlike C, because D).
- [ ] Value pyramid has exactly 3 layers, each specific to a named ICP
      segment from `icp.md`.
- [ ] Exactly 3 messaging pillars (no more, no less).
- [ ] Each pillar has at least 3 proof points; each proof point cites a
      source (URL, internal doc path, or "user-provided").
- [ ] Vocabulary in messaging matches `brand-voice.md` do/don't lists.
- [ ] No competitive claim is asserted without a public source.
- [ ] Anti-positioning section names at least two segments / use cases
      that are explicitly out of scope.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- <e.g. "Must work for both EMEA and AMER personas without geo split.">
- <e.g. "Cannot reference {Competitor X} by name in public-facing
  pillars — keep that to internal battle cards.">

## Instructions

1. Read every file under **Context (links)** before drafting.
2. Use capability `PS` (positioning statement) and `MP` (messaging
   pillars) from your SKILL.md.
3. Draft the pyramid bottom-up: functional → emotional → social.
4. Write the file to `{output_folder}/work/{brief_id}/v1.md`.
5. Update `state.yaml` to `status: in-review` and notify the
   orchestrator.
