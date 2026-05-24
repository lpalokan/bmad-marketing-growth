---
brief_id: <yyyy-mm-{presentation-slug}>
issued_by: <issuing-orchestrator>
issued_to: sales-presentation-advisor
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
mode: <produce | review>
---

## Objective

<One paragraph. State the audience, the desired decision the audience
must reach, the length, and whether this is `produce` (build from
source artifacts) or `review` (critique a submitted storyline).>

## Context (links)

Required:

- `{output_folder}/company-context/positioning.md`
- `{output_folder}/company-context/icp.md`
- `{output_folder}/company-context/brand-voice.md`

If `mode: produce`, add the source artifacts to inherit from:

- `{output_folder}/work/<launch-id>/launch-narrative.md` (if applicable)
- `{output_folder}/work/<teardown-id>/v{n}.md` (if Act II needs competitive proof)
- `{output_folder}/work/<advocacy-id>/v{n}.md` (if Act II needs case-study details)
- `{output_folder}/work/<positioning-id>/v{n}.md` (messaging pillars)
- <any other artifact path>

If `mode: review`, link the submitted draft:

- `{output_folder}/work/{brief_id}/draft.md` (or paste the storyline
  into a `draft.md` file under this brief's working folder)

## Deliverable

If `mode: produce`:

`work/{brief_id}/v1.md` containing the full storyline:

- Frontmatter with `audience`, `desired_decision`, `length`, `depth`,
  `sources_used`
- Act I (5 slides), Act II (3 anchors with depth per length tier),
  Act III (decision + next step)
- Every headline as a complete declarative sentence in active voice
- A `Sources used` appendix and a `Missing slots` list
- Optional speaker notes (depth L2) or bullet content (depth L3) per
  the issuing orchestrator's preference

If `mode: review`:

`work/{brief_id}/v1-review.md` containing:

- Summary verdict (2–4 sentences)
- Mapping table (BBP slot → user's content → assessment)
- Findings by act
- Suggested rewrites (before/after for at least one headline)
- Open questions or recommended next iteration

## Acceptance Criteria

`mode: produce`:

- [ ] Audience is named and cast as the protagonist.
- [ ] Act I includes Hook, Relevance, Challenge, Desire, Map — each a complete-sentence headline.
- [ ] Act II has 3 anchors ordered most-to-least important.
- [ ] Depth tier matches stated length (5/15/30/45+ min).
- [ ] Every headline is a complete declarative sentence in active voice.
- [ ] Every numeric claim cites a source in `Sources used`.
- [ ] Missing slots are marked `[MISSING — needs: X]`, not invented.
- [ ] Act III resolves to a specific decision (not a "Thank you / Questions?" slide).

`mode: review`:

- [ ] Mapping table populated from the submitted content (not generic).
- [ ] Single highest-impact change named in the summary verdict.
- [ ] At least one rewritten headline provided as proof of the standard.
- [ ] Structural problems distinguished from content problems.
- [ ] Quotes the user's own words back when critiquing specific lines.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- Length: <minutes>
- Depth: <L1 storyline-only | L2 +speaker-notes | L3 +bullet-content>
- Tone constraints from `brand-voice.md` apply to all headlines and notes.
- Visual design and slide layout are out of scope for Pierce.

## Instructions

1. Read the linked context files first.
2. If `mode: produce`, use capability `BP` (or `BD` if source
   artifacts are insufficient). If `mode: review`, use `SR`. Use
   `HD`, `TX`, `LE` as needed.
3. Write `v1.md` (or `v1-review.md`); update `state.yaml`.
