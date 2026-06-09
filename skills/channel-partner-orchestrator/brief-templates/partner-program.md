---
brief_id: <yyyy-mm-{partner-or-marketplace}>
issued_by: channel-partner-orchestrator
issued_to: partner-marketplace-manager
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<Partner / marketplace, anchor moment, joint pipeline target.>

## Context (links)

- `{output_folder}/company-context/positioning.md`
- `{output_folder}/company-context/icp.md`
- `{output_folder}/company-context/brand-voice.md`
- <partner brief / contract, prior co-marketing retro, marketplace
  editorial guidelines if applicable>

## Deliverable

`work/{brief_id}/v1.md`: joint plan (or listing package) per scope.

For co-marketing: joint narrative, channel mix per partner contribution,
co-branding rules, attribution model.

For marketplace listing: listing copy, screenshots/video spec,
pricing tier mapping, support flow, post-listing promotion plan.

For enablement: per-partner walkthrough, demo, deal-registration
training.

## Acceptance Criteria

- [ ] Joint narrative respects both companies' positioning (validated
      against both `positioning.md` files where available).
- [ ] Co-branding rules cited (partner's brand guidelines link).
- [ ] Channel mix names owner per channel (us / partner / shared).
- [ ] Attribution model distinguishes sourced from influenced; both
      companies agree on the rule.
- [ ] No invented joint customer counts or revenue claims.
- [ ] For marketplace listings: editorial guidelines passed, support
      / contracting links live.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- Partner contract: <contract URL or summary>.
- <Marketplace-specific editorial constraints.>

## Instructions

1. Read linked files first.
2. Use the matching capability from your SKILL.md.
3. Write `v1.md`; update `state.yaml`.
