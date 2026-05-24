---
name: company-context-bootstrap
description: "One-time intake workflow that populates _bmad-output/company-context/ with ICP, positioning, brand voice, KPIs, and tech-stack files. Must be run before any v2 agent. Lead: marketing-orchestrator. Use when user says set up company context, bootstrap, or initial intake."
---

# Company Context Bootstrap Workflow

## Overview
One-time intake that produces the five shared `company-context/` files
every v2 agent reads on activation: `icp.md`, `positioning.md`,
`brand-voice.md`, `kpis.md`, `tech-stack.md`. Run this **once** at
project start. Re-running is allowed and will refresh files in place
(prior content shown to the user for review before overwrite).

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

## On Activation

1. Load configuration (tolerant of missing files):
   - Try `{project-root}/_bmad/config.yaml`. If present, read `core.user_name`, `core.communication_language`, `core.document_output_language`, and `marketing-growth.output_folder`.
   - Try `{project-root}/_bmad/config.user.yaml`. If present, its `core.user_name` and `core.communication_language` override the shared values.
   - For any value still missing, use defaults: `user_name = there`, `communication_language = English`, `document_output_language = English`, `output_folder = {project-root}/_bmad-output`.

2. Greet the user in `{communication_language}` and explain: this
   workflow gathers the foundational knowledge the rest of the v2
   marketing suite needs. It writes five files under
   `{output_folder}/company-context/` and takes 20–45 minutes
   depending on how much is already documented.

3. Check `{output_folder}/company-context/` for existing files. For
   each that exists, show the user the current content and ask:
   keep / refresh / skip-this-file.

4. Execute the sibling `workflow.yaml` phase by phase. After each
   phase, write the corresponding file under
   `{output_folder}/company-context/` with the schema documented in
   `docs/company-context.md` (frontmatter: `owner`, `last_updated`,
   `last_updated_by: user`, `schema_version: 1`).

5. Outputs: see `docs/company-context.md` for the file table.
