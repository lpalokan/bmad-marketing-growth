---
brief_id: <slug-contact-approach>
issued_by: sales-prospecting-orchestrator
issued_to: contact-approach-writer
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<One paragraph. What must exist and why now — e.g. "Write personalized
first-touch messages for each key contact on {account}'s buying committee,
tailoring the one account storyline to each role so the outreach sequence can
launch this week.">

## Context (links)

- `{output_folder}/company-context/brand-voice.md` (if present — the voice to match)
- `{output_folder}/company-context/positioning.md` (if present)
- `{output_folder}/company-context/playbooks/message-frameworks.md` (if present — proven structures / openers / proof patterns)
- `{output_folder}/work/{account-id}/account-storyline.md` (the ONE shared value proposition to tailor)
- `{output_folder}/work/{account-id}/buying-committee.md` (the named people, roles, pains, owned metrics)
- <add: the why-now / signal scan for company-specific openers>

## Deliverable

Write `{output_folder}/work/{account-id}/approach-messages.md` (as `v1.md` in the
work folder). Include: one message per key contact, each built from a framework
(PAS or Before-After-Bridge) with a company-specific opener, value in the buyer's
terms, and named-comparable + specific-metric proof; plus a **Sources** note for
every proof metric and comparable used.

## Acceptance Criteria

- [ ] One message per key contact on the committee.
- [ ] Each message tailors the ONE shared account storyline to that role's pain / owned metric — no new value prop invented per person.
- [ ] Each message opens with a company-specific signal (from the why-now / signal scan), not a generic observation.
- [ ] Each message states value in the buyer's terms (their owned metric / role pain from the committee map).
- [ ] Each message includes proof = a named comparable in the contact's vertical + a specific metric, and that proof is sourced.
- [ ] Voice matches `brand-voice.md` if it is present.
- [ ] Any example numbers are labeled `Example — illustrative, not benchmarks.`; unsourced proof is marked `[UNKNOWN — needs input]`, not filled with guesses.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- <e.g. channel (email / LinkedIn); message length limit; which contacts are in scope; confidentiality of comparables>

## Instructions

1. Read the Context (links) that exist. Do not block on missing context.
2. Use capability WM (write per-contact messages); tailor the ONE storyline — never invent a value prop per person.
3. Open each message on a company-specific signal; frame value in the buyer's owned metric; include a sourced named-comparable + specific-metric proof.
4. Write `v1.md`; set `state.yaml` `status: in-review`; notify the orchestrator.
</content>
