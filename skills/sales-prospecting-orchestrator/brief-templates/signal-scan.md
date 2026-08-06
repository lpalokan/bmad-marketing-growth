---
brief_id: <slug-signal-scan>
issued_by: sales-prospecting-orchestrator
issued_to: account-research-analyst
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<One paragraph. What must exist and why now — e.g. "Scan {account} for a fresh
why-now: the stacked buying triggers and intent that say the timing is right (or
that it isn't), to re-fire the motion and ground the account storyline for the Q3
push.">

## Context (links)

- `{output_folder}/company-context/icp.md` (if present — the narrative triggers to filter through)
- `{output_folder}/company-context/signal-library.md` (if present — the trigger taxonomy + weights)
- `{output_folder}/work/{account-id}/account-profile.md` (if present — the account to scan)
- <add: anything the user already shared about the account's recent activity>

## Deliverable

Write the signal scan as `v1.md` under `{output_folder}/work/{account-id}/`.
Include: signals scanned across the taxonomy (each dated and sourced), a ranking
by strength + recency, the stacked-signals-through-ICP read, a refreshed
**why-now** statement (or "timing cold"), and which signals should re-fire the
motion. Add a **Sources** section.

## Acceptance Criteria

- [ ] Signals scanned across the taxonomy: funding, leadership hires, headcount, job posts, M&A, geo expansion, tool churn, regulatory deadlines, migrations, launches, public OKRs, plus 1st/3rd-party intent.
- [ ] Signals ranked by strength + recency, per `signal-library.md` weights where present.
- [ ] Why-now built from **stacked signals filtered through the ICP** — not a single-signal false positive; single signals are rejected explicitly.
- [ ] A refreshed **why-now** statement written (or "timing cold" stated plainly), noting which signals should re-fire the motion.
- [ ] Every signal carries a source and a date; gaps marked `[UNKNOWN — needs input]`, not filled with guesses.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- <e.g. Clay credit budget; regions; freshness window (how far back signals count); confidentiality of sources>

## Instructions

1. Read the Context (links) that exist. Do not block on missing context.
2. Use capability SS (scan signals + refresh why-now).
3. Scan the full taxonomy; prefer `WebSearch` / `WebFetch`, use Clay `ask-question-about-accounts` when available.
4. Rank by strength + recency; require stacked signals through the ICP before writing a why-now.
5. Write `v1.md`; set `state.yaml` `status: in-review`; notify the orchestrator.
