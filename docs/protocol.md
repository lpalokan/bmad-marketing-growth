# Brief-driven delegation protocol (v2)

The v2 architecture introduces an explicit, file-based protocol for how
orchestrators delegate to specialists and how specialists hand work back.
Every delegated piece of work flows through three artefacts: a **brief**,
one or more **versions** of the deliverable, and a **review** per version.

The protocol is intentionally low-tech: plain Markdown files with YAML
frontmatter, written under the user-configured `output_folder` (default
`_bmad-output/`). No tooling is required.

## Folder layout

Under `{output_folder}/work/{deliverable-id}/`:

```
_bmad-output/work/{deliverable-id}/
├── brief.md             # issued by orchestrator; immutable once issued
├── v1.md                # specialist's first attempt
├── v1-review.md         # orchestrator's verdict on v1
├── v2.md                # specialist's revision (if NEEDS_REVISION)
├── v2-review.md         # orchestrator's verdict on v2 (and so on)
└── state.yaml           # machine-readable run state
```

`{deliverable-id}` is a short, human-readable slug, conventionally
`{yyyy}-{quarter-or-month}-{topic}`, e.g. `2026-q3-positioning`,
`2026-05-aws-launch-narrative`, `2026-06-icp-refresh`.

## Schemas

### `brief.md`

Frontmatter:

```yaml
---
brief_id: 2026-q3-positioning
issued_by: product-marketing-orchestrator
issued_to: positioning-messaging-pmm
issued_at: 2026-05-23
status: open            # open | in-review | revising | accepted | escalated
revision: 0
max_revisions: 3
---
```

Required sections (in this order):

1. **Objective** — one paragraph; what does done look like, and why now.
2. **Context (links)** — bulleted list of paths to `company-context/`
   files the specialist must read first. MUST include at least one
   `company-context/` reference unless the brief is bootstrapping
   company-context itself. Link only the narrowest set that grounds the
   task — listing the whole bundle invites scope creep (see rule 8).
3. **Deliverable** — what file(s) to produce, where to write them
   (always under this `work/{id}/` folder unless explicitly stated),
   target length / format.
4. **Acceptance Criteria** — Markdown checklist. Each item should be
   binary (✓/✗ verifiable). The reviewer scores against this exact
   list.
5. **Source Fidelity** — verbatim copy of the Source Fidelity block
   (do not paraphrase; the duplication is the point).
6. **Constraints** — budget, tone, audience, legal, brand-voice
   constraints. Anything the specialist can't infer from context.
7. **Instructions** — step-by-step process for the specialist, in the
   imperative. Reference capability codes from the specialist's
   `SKILL.md` where applicable.

### `v{n}-review.md`

Frontmatter:

```yaml
---
review_id: 2026-q3-positioning-v1-review
reviewer: product-marketing-orchestrator
verdict: APPROVED | NEEDS_REVISION | ESCALATED
---
```

Required sections (in this order):

1. **Verdict** — one line, one of the three values above.
2. **Acceptance Criteria scorecard** — repeat every line from the
   brief's acceptance-criteria checklist with ✓ or ✗ and a one-sentence
   justification. No item may be skipped.
3. **Required Changes** — numbered, specific, actionable. Only present
   when verdict is `NEEDS_REVISION`. Each item must map to a failing
   acceptance criterion.
4. **Next Step** — one line: which version to produce next, or
   "Frozen — see `state.yaml`", or "Escalated to {agent or user}".

### `state.yaml`

```yaml
brief_id: 2026-q3-positioning
status: accepted        # open | in-review | revising | accepted | escalated
revision: 1             # current revision number
max_revisions: 3
frozen: true            # true after accept; folder becomes read-only
issued_by: product-marketing-orchestrator
issued_to: positioning-messaging-pmm
issued_at: 2026-05-23
accepted_at: 2026-05-24
accepted_version: v2
```

## State machine

```
                                  ┌──────────────────────┐
                                  ▼                      │
   ┌──────┐  produce v{n}   ┌───────────┐   review    ┌─────────────┐
   │ open │ ───────────────▶│ in-review │ ──────────▶ │  verdict?    │
   └──────┘                 └───────────┘             └─────────────┘
                                                       │       │      │
                                                APPROVED  NEEDS_REVISION  ESCALATED
                                                       │       │           │
                                                       ▼       ▼           ▼
                                                  ┌────────┐ ┌─────────┐ ┌───────────┐
                                                  │accepted│ │revising │ │ escalated │
                                                  │frozen  │ └─────────┘ └───────────┘
                                                  └────────┘     │
                                                                 └── produce v{n+1} ──▶ in-review
```

## Protocol rules

These rules are enforced by convention; orchestrators and specialists
must follow them literally.

1. **The orchestrator owns the verdict.** A specialist never sets
   `status: accepted` on their own brief. Self-approval is forbidden.
2. **Briefs are immutable.** Once `brief.md` is written, it is not
   edited. A scope change requires writing a **new** brief with a new
   `brief_id` that supersedes the original; the original gets a final
   review with verdict `ESCALATED` and `Next Step: Superseded by
   {new-brief-id}`.
3. **Versions are append-only.** `v1.md` is never edited after
   `v1-review.md` exists. The specialist always writes a fresh `v2.md`
   (etc.).
4. **Acceptance freezes the folder.** On `verdict: APPROVED`, the
   orchestrator writes `state.yaml` with `frozen: true` and the folder
   is treated as read-only. Later corrections happen in a new
   deliverable folder that references the frozen one.
5. **Max revisions caps the loop.** If a brief reaches
   `revision > max_revisions`, the next review must be `ESCALATED` and
   the orchestrator surfaces the deliverable to Max (CMO) or the user
   directly. Default `max_revisions: 3`.
6. **Briefs must reference company context.** Every brief MUST list at
   least one `company-context/` file in its `Context (links)` section.
   The only exception is the company-context-bootstrap workflow itself,
   which produces those files.
7. **The reviewer scores against the brief, not the deliverable.**
   Reviews score the exact acceptance-criteria checklist from
   `brief.md`. Adding new criteria at review time is forbidden — if a
   reviewer realises a criterion is missing, the right move is to issue
   a new brief that supersedes.
8. **The bundle informs; the brief mandates.** The `company-context/`
   files a brief lists in *Context (links)* are read-context that grounds
   the work — not a licence to widen it. A specialist delivers exactly the
   brief's Acceptance Criteria; discovering more in the bundle is grounds
   to flag the orchestrator (who may issue a superseding brief), never to
   expand scope, change the deliverable, or write outside `work/{id}/`.

## Worked example

```
_bmad-output/work/2026-q3-positioning/
├── brief.md             # status: accepted, revision: 1
├── v1.md
├── v1-review.md         # verdict: NEEDS_REVISION, 2 items failing
├── v2.md
├── v2-review.md         # verdict: APPROVED
└── state.yaml           # frozen: true, accepted_version: v2
```

The Product Marketing Orchestrator (Max's PMM lead) issued a brief to
the Positioning & Messaging PMM. The PMM produced `v1`. The orchestrator
reviewed against the acceptance criteria, found 2 unmet items, and
issued `v1-review.md` with verdict `NEEDS_REVISION` and a numbered list
of required changes. The PMM produced `v2`. The orchestrator reviewed
again, all criteria passed, and wrote `v2-review.md` with verdict
`APPROVED`. `state.yaml` was updated with `frozen: true`. The folder is
now part of the company's marketing record and is not edited further.
