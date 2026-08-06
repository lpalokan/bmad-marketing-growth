---
brief_id: <slug-relationship-layer>
issued_by: sales-prospecting-orchestrator
issued_to: account-research-analyst
issued_at: <YYYY-MM-DD>
status: open
revision: 0
max_revisions: 3
---

## Objective

<One paragraph. Warm/active accounts only. What must exist and why now — e.g. "Capture
what the relationship holder for {account} knows that the open web does not — the POC,
the people who asked, the systems used, the operating-model decision now in play — so
the storyline and approach lead with the strongest unlocks. If a POC is active, POC
facts lead and public research is context.">

## Context (links)

- `{output_folder}/work/{account-id}/account-profile.md` (if present — public facts to keep separate from this layer)
- `docs/opportunity-brief-method.md` §5 (if present — the relationship-layer method + the six questions)
- <add: the name/role of whoever holds the relationship; any partner/internal material already shared>

## Deliverable

Write the relationship layer as `v1.md` under `{output_folder}/work/{account-id}/` (or a
**clearly separated §5** section in `account-profile.md`). Answer the six relationship
questions as **Account notes**, request and read partner/internal material, and state
the POC/public ordering. Label unsupported estimates `[Account note — needs
verification]`.

## Acceptance Criteria

- [ ] The account is confirmed **warm/active** and the relationship holder is named (if cold, the brief is returned as N/A, not fabricated).
- [ ] The six questions are answered as Account notes: who asked & from which function; what POC/workshop happened & what it proved; what data/evidence/systems were used; what the customer liked/rejected/wants next; what operating-model decision is in play; what scale facts are known.
- [ ] Partner/internal material was explicitly **requested** (and read if provided) — the open-web-invisible unlocks.
- [ ] This layer is kept **separate** from public facts; unsupported estimates are labelled `[Account note — needs verification]`.
- [ ] For an active POC, the deliverable states that **POC facts lead** and public research is context; nothing time-sensitive is presented without re-verification.

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## Constraints

- <e.g. confidentiality of partner material; which relationship holder to ask; POC stage>

## Instructions

1. Confirm the account is warm/active and identify the relationship holder. If cold, return N/A.
2. Use capability RL (capture the relationship layer).
3. Ask the six questions; request partner/internal material explicitly.
4. Keep the layer separate from public facts; label estimates; order POC-first if a POC is live.
5. Write `v1.md`; set `state.yaml` `status: in-review`; notify the orchestrator.
