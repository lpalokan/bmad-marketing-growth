---
brief_id: <yyyy-mm-{launch-name}-enablement>
issued_by: product-marketing-orchestrator
issued_to: launch-sales-enablement-pmm
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<One paragraph. Name the launch, its date, its category (tier-1 / tier-2
/ tier-3 launch), and what success looks like. E.g. "Tier-1 launch of
{ProductX} on 2026-09-15. Build the launch narrative and the sales
enablement bundle so PR Comms, Digital, and Field can build their
downstream plans against a single source of truth.">

## Context (links)

- `{output_folder}/company-context/positioning.md`
- `{output_folder}/company-context/icp.md`
- `{output_folder}/company-context/brand-voice.md`
- <relevant competitive teardowns under work/>
- <product spec / PRD / changelog>

## Deliverable

Write under `{output_folder}/work/{brief_id}/v1.md` and any sibling
files referenced below.

- `v1.md` — the launch narrative bundle:
  - One-line story (15 words max).
  - 30-second elevator (≤80 words).
  - Long-form narrative (300-500 words).
  - 3 supporting proof points with sources.
  - Explicit not-this list (anti-claims).
  - Down-stream hand-off plan: what PR, Digital, Field, Content each
    need to do, with brief-template references.
- `v1-battlecard.md` — 1-page battlecard (only if launch tier requires
  it; check Constraints).
- `v1-onepager.md` — 1-page customer-facing one-pager.
- `v1-demo-script.md` — demo script with timing markers (only if
  Constraints flag it).
- `v1-faq.md` — top 10 anticipated objections with answers.

## Acceptance Criteria

- [ ] One-line story is ≤15 words and names the buyer change, not the
      feature.
- [ ] Long-form narrative is 300-500 words; does not start with a
      product name.
- [ ] Each proof point has a source link or doc path.
- [ ] Not-this list has at least 3 items the team must avoid claiming.
- [ ] Down-stream hand-off plan references brief templates by path
      under `skills/`.
- [ ] All requested sub-artefacts (battlecard / one-pager / demo /
      FAQ) match the requested scope; nothing else generated.
- [ ] Voice matches `brand-voice.md` do/don't lists.
- [ ] No claim asserts a number that isn't sourced.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- Launch tier: <T1 | T2 | T3>. T1 requires battlecard + onepager +
  demo + FAQ; T2 requires onepager + FAQ; T3 requires onepager only.
- <Embargo windows, regional considerations, analyst NDA constraints.>

## Instructions

1. Use capability `LN` (launch narrative) and the asset-specific
   capabilities from your SKILL.md.
2. Draft the narrative first; everything else hangs off it.
3. Write all files under `{output_folder}/work/{brief_id}/`. Update
   `state.yaml` to `status: in-review`.
