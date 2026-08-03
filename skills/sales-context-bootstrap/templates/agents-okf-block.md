<!-- sales-prospecting:okf start -->
<!-- block-version: 1 -->
## Sales layer (OKF bundle) — optional, read-mostly

The Sales Prospecting Suite extends the **same** `_bmad-output/company-context/`
OKF v0.1 bundle the marketing suite writes — it does **not** create a separate
bundle. On top of the marketing core (`icp.md`, `positioning.md`,
`brand-voice.md`, `kpis.md`, `tech-stack.md`) it adds a durable, reusable
**sales layer**. Schema & ownership: the suite's `docs/company-context.md`.

Sales-layer concepts and their single writer (**owner**):

| Concept (path) | `type` | Owner |
|---|---|---|
| `offerings.md` + `offerings/<slug>.md` | Offering | service-offering-advisor |
| `case-studies/<slug>.md` | Case Study | service-offering-advisor* |
| `icp-fit-model.md` | Scoring Model | fit-scoring-strategist |
| `buying-committee-model.md` | Buying Committee Model | buying-committee-mapper |
| `signal-library.md` | Signal Library | signal-monitor |
| `playbooks/sequences.md` | Playbook | outreach-sequence-planner |
| `playbooks/objections.md` | Playbook | reply-objection-handler |
| `playbooks/message-frameworks.md` | Playbook | contact-approach-writer |

\* If the marketing-growth `customer-advocacy-references` agent (Cara Customer)
is installed, defer `case-studies/` ownership to it.

These are **read-mostly and single-writer**: every sales agent reads them to
ground its work; only the one owner of a file writes it. They **link** the
marketing core (personas in `icp.md`, pillars in `positioning.md`, voice in
`brand-voice.md`) rather than duplicating it.

**The sales layer is OPTIONAL.** The Sales Prospecting agents work without it —
they read whichever concepts are present and ask a focused question when one is
missing. Nothing blocks on it. To pre-seed it, run `/sales-context-bootstrap`;
to fill the marketing core it links to, run `/company-context-bootstrap`. Neither
is a prerequisite.
<!-- sales-prospecting:okf end -->
