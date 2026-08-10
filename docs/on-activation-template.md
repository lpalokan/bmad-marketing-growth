# `On Activation` template for v2 agents

Every v2 agent's `SKILL.md` ends with an `## On Activation` section.
The block is **deliberately duplicated** per skill (BMAD progressive
disclosure is per-skill — no `skills/_shared/`). Copy this template
verbatim into a new SKILL.md, then fill the four placeholders.

## Placeholders

- `{AGENT-CODE}` — the skill folder name, e.g. `positioning-messaging-pmm`.
- `{AGENT-NAME}` — the persona's display name, e.g. `"Pippa Position"`.
- `{COMPANY-CONTEXT-FILES}` — Markdown list of `company-context/*.md`
  files this agent reads (always at least `positioning.md` and
  `icp.md`; add `brand-voice.md` for any customer-facing copy, `kpis.md`
  for analytics work, `tech-stack.md` for automation/digital work).
- `{EXTRA-SIDECAR-FILES}` — additional optional files in the agent's
  sidecar beyond `memories.md` (e.g. `seo-knowledge.md`). Use `(none)`
  if there are no extras.

## Template

```markdown
## On Activation

1. Load configuration (tolerant of missing files; for each value, the first file that provides it wins):
   - Try `{project-root}/_bmad/custom/config.user.toml`, then `{project-root}/_bmad/custom/config.toml` (pinned overrides -- always win when present).
   - Try `{project-root}/_bmad/marketing-growth/config.yaml` (BMAD 6.x module config; flat keys `user_name`, `communication_language`, `document_output_language`, `output_folder`).
   - Try `{project-root}/_bmad/config.user.toml`, then `{project-root}/_bmad/config.toml` (BMAD 6.x root config; `[core]` keys, e.g. `output_folder`, `document_output_language`).
   - Legacy fallback: try `{project-root}/_bmad/config.yaml` (`core.user_name`, `core.communication_language`, `core.document_output_language`, `marketing-growth.output_folder`), with `{project-root}/_bmad/config.user.yaml` overriding `core.user_name` and `core.communication_language`.
   - For any value still missing, use defaults: `user_name = there`, `communication_language = English`, `document_output_language = English`.
   - Resolve `output_folder` **silently — never ask the user**. Normalize a relative value against `{project-root}`. Then use the first of these that already contains a `company-context/` folder: the configured value, `{project-root}/output`, `{project-root}/_bmad-output` (legacy name, retired in v2.4). If none does, glob the project for `**/company-context/index.md` and `**/company-context/icp.md` (excluding `.git/`, `node_modules/`, `_bmad/`, `**/work/**`) and use its parent when there is exactly one match. Still nothing: use `{project-root}/output`. `output/` is the canonical name; `_bmad-output/` is read-only compatibility — never create it.

2. Prepare memory sidecar (self-create if missing):
   - Ensure `{project-root}/_bmad/_memory/{AGENT-CODE}-sidecar/` exists. Use `mkdir -p` if creating.
   - If `memories.md` inside that directory doesn't exist, create it with this stub:
     ```
     # Agent Memory

     No sessions recorded yet.
     ```
   - Load `memories.md` (always). Also load `instructions.md` if present, and: {EXTRA-SIDECAR-FILES}.

3. Load company context (tolerant of missing files):
   - `{output_folder}/company-context/` is an OKF v0.1 bundle. Read these
     hub concepts (you MAY follow their absolute `/subfolder/…` links for
     more detail, e.g. `/personas/…`):
     {COMPANY-CONTEXT-FILES}
   - This bundle is read-context that **supports** the brief you are given;
     it does not widen your mandate. When working a brief, read the
     concepts its *Context (links)* names and deliver exactly its
     Acceptance Criteria — finding more in the bundle is not licence to do
     more (see `docs/protocol.md`).
   - Be fault-tolerant about the bundle's location and contents: read
     whichever listed files are present and note what is absent. A missing
     file is never a hard stop. Only if no `company-context/` bundle exists
     anywhere in the project, say so once, suggest
     `/company-context-bootstrap`, and ask the user whether to continue
     without it.

4. Greet `{user_name}` by name in `{communication_language}` as
   {AGENT-NAME}. Present the Capabilities table.

5. When the user selects a capability code from the Capabilities table,
   read the matching file under `prompts/` and follow its instructions
   literally. For orchestrators, follow `## Delegation` (see SKILL.md)
   when handing work to a specialist: write `brief.md` under
   `{output_folder}/work/{deliverable-id}/` using the matching template
   in `brief-templates/`.

6. **STOP and WAIT for user input.** Accept code, number, or fuzzy match.

**SM:** Ask for a session summary, then append to memories.md with today's date.

**CRITICAL:** Only read/write files under `{project-root}/_bmad/_memory/{AGENT-CODE}-sidecar/` (private memory), `{output_folder}/work/` (deliverables, per protocol.md), and `{output_folder}/company-context/` (only if you are the owner of that file — see docs/company-context.md). Stay in character until dismissed.
```

## Orchestrator-only addition

Orchestrators also include a `## Delegation` section in their SKILL.md
listing the specialists they can delegate to and the brief template to
use. Pattern:

```markdown
## Delegation

When delegating to a specialist, write `brief.md` under
`{output_folder}/work/{deliverable-id}/` using the appropriate template
from `brief-templates/`, then hand off.

| Specialist                       | Use for                              | Brief template                          |
|----------------------------------|--------------------------------------|-----------------------------------------|
| positioning-messaging-pmm        | Positioning statements, messaging    | brief-templates/positioning.md          |
| competitive-intelligence-pmm     | Competitor teardowns, battle cards   | brief-templates/competitive-teardown.md |
| launch-sales-enablement-pmm      | Launch narrative, enablement assets  | brief-templates/launch-enablement.md    |
```

The orchestrator MUST consult `docs/protocol.md` (in this repo) for the
review/verdict rules; do not paraphrase them in the SKILL.md.
