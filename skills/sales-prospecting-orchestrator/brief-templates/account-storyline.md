---
brief_id: <slug-account-storyline>
issued_by: sales-prospecting-orchestrator
issued_to: account-storyline-developer
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<One paragraph. What must exist and why now — e.g. "Build the one account-level
storyline for {account}: a single value hypothesis, expressed as a Challenger
teachable insight and 3–5 ABM message pillars, that every contact message and
sequence touch will be a tailoring of.">

## Context (links)

- `{output_folder}/company-context/positioning.md` (if present — our pillars & differentiation)
- `{output_folder}/company-context/offerings.md` (if present — what we're matching to)
- `{output_folder}/company-context/brand-voice.md` (if present — how we sound)
- `{output_folder}/company-context/case-studies/` (if present — proof for pillars)
- `{output_folder}/work/{account-id}/account-profile.md` (triggers, pains, why-now)
- `{output_folder}/work/{account-id}/fit-scorecard.md` (why they fit + timing)
- `{output_folder}/work/{account-id}/buying-committee.md` (named roles to tailor to)

## Deliverable

Write `{output_folder}/work/{account-id}/account-storyline.md` (as `v1.md` in the
work folder). Include: one top-line **value hypothesis**; a **Challenger
teachable insight** (Teach a reframe of the account's own situation → Tailor to
the committee → Take Control toward a next step); **3–5 ABM message pillars**,
each with a headline, a value prop, and a proof point; a **Committee map** (which
pillar leads for which role); a **Sources** section; and a **Missing/assumptions**
list.

## Acceptance Criteria

- [ ] One clear top-line value hypothesis; every pillar ladders up to it.
- [ ] A Challenger teachable insight grounded in the account's *real* situation (a trigger/pain from the profile), not a market truism or a product pitch.
- [ ] 3–5 message pillars, each with a headline + value prop + proof point.
- [ ] Every proof point uses a named comparable + a specific metric, and is sourced (from `case-studies/` or a cited source); unsupported proof is marked `[PROOF NEEDED — X]`, not fabricated.
- [ ] Headlines are complete declarative sentences in active voice.
- [ ] Voice matches `brand-voice.md` if present.
- [ ] The storyline maps to the buying committee's roles.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- <e.g. proof must trace to an installed case study; regions; confidentiality; which offering to lead with>

## Instructions

1. Read the Context (links) that exist. Do not block on missing context.
2. Use capability DS (develop the storyline).
3. Optionally use capability PR to route the storyline to Pierce Pitch (`sales-presentation-advisor`, part of this suite) for a review; if unavailable, self-review to the acceptance criteria above. Never block on Pierce being absent.
4. Write `v1.md`; set `state.yaml` `status: in-review`; notify the orchestrator.
