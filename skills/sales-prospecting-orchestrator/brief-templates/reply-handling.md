---
brief_id: <slug-reply-handling>
issued_by: sales-prospecting-orchestrator
issued_to: reply-objection-handler
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<One paragraph. What must exist and why now — e.g. "Handle the reply from
{contact} at {account} and drive it to a booked meeting: classify it, handle any
objection with reframe + proof, make one specific low-friction ask, and set the
CRM next step.">

## Context (links)

- `{output_folder}/company-context/positioning.md` (if present — reframes lean on it)
- `{output_folder}/company-context/offerings.md` (if present — where proof points live)
- `{output_folder}/work/{account-id}/account-storyline.md` (if present — the account point of view)
- `{output_folder}/company-context/playbooks/objections.md` (if present — the objection library)
- <add: the reply text from {contact}, verbatim, and any thread history>

## Deliverable

Write the reply handling as `v1.md` in the work folder; the reply log lives at
`{output_folder}/work/{account-id}/reply-log.md`. Include: the reply text, its
**classification**, the drafted response (reframe + proof for objections), the
**booked-meeting ask**, the **CRM next step**, a note on the **human-in-the-loop
gate**, and a **Sources** section for any proof numbers.

## Acceptance Criteria

- [ ] The reply is classified (positive / objection / referral / not-now / negative / out-of-office).
- [ ] If it is an objection, the response provides a **reframe + proof** (proof sourced, not invented).
- [ ] There is one **specific, low-friction booked-meeting ask** (concrete slot or link, tight agenda).
- [ ] The **CRM next step** is set: exact next action, owner, and date.
- [ ] The **human-in-the-loop gate** is noted — the draft is for the rep to review and send.
- [ ] The voice matches `brand-voice.md` if present; the prospect's own language is mirrored.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- <e.g. brand-voice guardrails; no pricing commitments without rep sign-off; confidentiality; which meeting types / calendar links are allowed>

## Instructions

1. Read the Context (links) that exist. Do not block on missing context.
2. Use capability HR (handle a reply); flag any new objection for capability OL.
3. Classify first, then draft; handle objections with reframe → proof drawn from `objections.md`, `offerings.md`, and the storyline.
4. Never send — keep the human-in-the-loop gate; the rep reviews and sends.
5. Write `v1.md`; set `state.yaml` `status: in-review`; notify the orchestrator.
