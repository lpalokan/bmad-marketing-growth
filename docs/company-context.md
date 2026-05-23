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

Additional files MAY be added when a clear single owner exists. New
files require updating this table.

## Schema

Files are free-form Markdown, but each MUST include:

```yaml
---
owner: <agent-code>          # exactly one agent code from module.yaml
last_updated: YYYY-MM-DD
last_updated_by: <agent-code-or-user>
schema_version: 1
---
```

Followed by a short **Status** line — one of `Bootstrapped`,
`In progress`, `Stable`, `Stale (needs refresh)` — and then the
free-form body. Status drives bootstrap and audit logic.

## Read/write lifecycle

1. **Bootstrap.** The `company-context-bootstrap` workflow runs once at
   project start. It collects answers from the user, then writes the
   first version of every file in the table above. Status becomes
   `Bootstrapped`.

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
