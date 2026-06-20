# Company context (shared, read-mostly memory)

`{output_folder}/company-context/` is the **shared, durable** knowledge
the agents reason from. It is the canonical answer to "what does this
company stand for, who does it sell to, and how does it measure
itself?". Briefs reference these files; specialists read them before
they do any work.

This is distinct from:

- **`{output_folder}/work/{id}/`** — per-deliverable, frozen on accept.
  See `protocol.md`.
- **`_bmad/_memory/{code}-sidecar/memories.md`** — per-agent private
  notes, session logs, things only that one agent benefits from
  remembering. Unchanged from the existing sidecar pattern.

## Files

Every file is plain Markdown. Each file is **owned by exactly one
agent**, who is responsible for keeping it accurate. Other agents read
freely; only the owner writes.

| File                  | Owner                              | Read by                                  | Contents (one-liner)                                                       |
|-----------------------|------------------------------------|------------------------------------------|----------------------------------------------------------------------------|
| `icp.md`              | product-marketing-orchestrator     | All marketing agents                     | Ideal Customer Profile: segments, firmographics, jobs-to-be-done, pains.   |
| `positioning.md`      | product-marketing-orchestrator     | All marketing agents                     | Category, target, key benefit, primary alternatives, value pyramid.        |
| `brand-voice.md`      | brand-orchestrator                 | Anyone producing customer-facing text    | Voice attributes, do/don't word lists, sample tone snippets.               |
| `kpis.md`             | growth-analyst (Pixel Metrics)     | All orchestrators                        | The 5–10 KPIs the company is run by; definition + target + current source. |
| `tech-stack.md`       | marketing-automation-engineer      | Digital, Growth, Field orchestrators     | MarTech stack: CDP, MAP, CRM, analytics, ad platforms, lead-routing rules. |

Additional concept files MAY be added when a clear single owner exists.
A new file in a recognized subfolder (`personas/`, `metrics/`,
`competitors/`, `systems/`, `sources/`) inherits its owner from the rules
in **OKF bundle layout** below and does not need a new table row; a new
top-level core file does require updating this table.

## Schema

The folder **is a Google OKF (Open Knowledge Format) v0.1 bundle** — a
directory of Markdown concept files. Each concept file is free-form
Markdown, but each MUST include frontmatter that unions the OKF fields
with the retained BMAD fields. OKF requires only `type`; the BMAD fields
are kept because the agents and the single-writer rule depend on them.

```yaml
---
type: <OKF concept type>     # required — ICP, Positioning, Brand Voice,
                             #   KPI Set, Tech Stack, Persona, Metric,
                             #   Competitor, System, Reference, …
title: <human-readable name>
description: <one sentence>   # used by index.md, search snippets, previews
tags: [company-context, …]
timestamp: <ISO 8601>        # mirrors last_updated, OKF-queryable
resource: <URI>              # optional; omit if none
owner: <agent-code>          # exactly one agent code from module.yaml
last_updated: YYYY-MM-DD
last_updated_by: <agent-code-or-user>
schema_version: 2
---
```

Followed by a short **Status** line — one of `Bootstrapped`,
`In progress`, `Stable`, `Stale (needs refresh)` — and then the
free-form body. Status stays a body line (not frontmatter) because
bootstrap and audit logic key on it.

`schema_version: 2` marks an OKF-format file. Files written under the old
schema (`schema_version: 1`, no `type`) are legacy and are upgraded in
place by the bootstrap workflow's **migrate** mode.

## OKF bundle layout

The five core files are OKF **hub concepts** at fixed paths — every agent
reads them on activation, so they never move. Sub-concepts are exploded
into subfolders only when one earns its own file (the **Hybrid**
granularity rule); a hub that is exploded keeps a short summary and links
down. Concepts link to each other with **absolute, bundle-relative**
Markdown links, e.g. `icp.md` links `[CTO buyer](/personas/cto-buyer.md)`.

```
company-context/
├── index.md            # OKF root — the ONLY file with frontmatter
│                       #   (just `okf_version: "0.1"`); grouped links
├── log.md              # change history, newest first
├── icp.md              # hub  (type: ICP)
├── positioning.md      # hub  (type: Positioning)
├── brand-voice.md      # hub  (type: Brand Voice)
├── kpis.md             # hub  (type: KPI Set)
├── tech-stack.md       # hub  (type: Tech Stack)
├── personas/           # exploded buyer personas (type: Persona)
├── metrics/            # exploded KPIs (type: Metric)
├── competitors/        # exploded competitors (type: Competitor)
├── systems/            # exploded MarTech systems (type: System)
└── sources/            # concepts refactored from the input/ folder
```

**Reserved files** `index.md` and `log.md` are never used as concept
documents. The root `index.md` groups `* [Title](/path) - description`
entries (Core concepts, then a section per populated subfolder);
subfolder `index.md` files carry no frontmatter. `log.md` uses
`## YYYY-MM-DD` headings (newest first) with `**Creation**`, `**Update**`,
`**Migration**`, and `**Ingest**` entries.

**Sub-concept ownership** is inherited from the parent hub: `personas/*`
and `competitors/*` → product-marketing-orchestrator; `metrics/*` →
growth-analyst; `systems/*` → marketing-automation-engineer; `sources/*`
→ `last_updated_by: user` (written by ingest).

## Read/write lifecycle

1. **Bootstrap.** The `company-context-bootstrap` workflow runs at
   project start. It collects answers from the user (or imports & adapts
   another project's context), then writes the first version of every
   file in the table above as OKF concepts plus the bundle `index.md` and
   `log.md`. Status becomes `Bootstrapped`. The same workflow also offers
   **migrate** (upgrade legacy non-OKF files in place) and **ingest**
   (refactor an `input/` folder into `sources/` concepts and propose
   gated updates to the owning core files) — ingest is run anytime.

2. **Read.** Every agent's `On Activation` block lists the
   `company-context/` files it reads (typically `icp.md`,
   `positioning.md`, `brand-voice.md` for customer-facing work; add
   `kpis.md` for analytics work; add `tech-stack.md` for
   automation/digital work). Reads are tolerant of missing files —
   agents must not crash when bootstrap has not been run; they should
   prompt the user to run it instead.

3. **Update.** Only the owner agent writes. Updates happen as part of
   normal work: a brief's verdict can include "update
   `company-context/positioning.md` with the approved positioning
   statement", which the orchestrator does (with the user's
   confirmation) before freezing the deliverable folder.

4. **Audit.** Any orchestrator MAY mark a file `Stale (needs refresh)`
   in its frontmatter if they notice it contradicts new evidence. The
   owner is responsible for the refresh.

## Why a separate folder

The three-tier separation is deliberate:

- **`company-context/`** answers "what is true about us right now?"
  (read-mostly, owned, durable).
- **`work/{id}/`** is the audit trail of how we got here (immutable
  once frozen).
- **Sidecar memory** is per-agent muscle memory (private, free-form,
  not seen by other agents).

Conflating any two of these creates problems we've seen in v1: agents
overwriting each other's notes, orchestrators losing the history of
how a decision was made, or shared files growing into impossible-to-read
catch-all logs.
