---
name: company-context-bootstrap
description: "Intake workflow that populates _bmad-output/company-context/ with ICP, positioning, brand voice, KPIs, and tech-stack files — from scratch, or by importing and adapting another project's existing context. Must be run before any v2 agent. Lead: marketing-orchestrator. Use when user says set up company context, bootstrap, initial intake, reuse context, clone context, import from another project, or seed from existing context."
---

# Company Context Bootstrap Workflow

## Overview
Intake that produces the five shared `company-context/` files every v2
agent reads on activation: `icp.md`, `positioning.md`, `brand-voice.md`,
`kpis.md`, `tech-stack.md`. Run this at project start. Re-running is
allowed and will refresh files in place (prior content shown to the user
for review before overwrite).

Two modes:

- **From scratch** — answer focused intake questions per file.
- **Import & adapt** — point at another project's context folder (or a
  parent folder of projects); the workflow discovers what's available,
  lets you pick a source and which files to bring over, copies each in,
  and walks you through adapting the project-specific parts for the new
  company. See `features/import-existing-context.feature` for the
  behavioural contract.

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

4. Ask which mode to use: **from scratch** or **import & adapt**.

   - **Import & adapt**: ask for a folder path and resolve it (tolerant,
     never guess content). Use it directly if it contains recognized
     context files (`icp.md`, `positioning.md`, `brand-voice.md`,
     `kpis.md`, `tech-stack.md`); otherwise look for
     `_bmad-output/company-context/` then `company-context/` beneath it;
     otherwise treat it as a container and scan its immediate subfolders,
     listing the source projects found and asking the user to choose
     one. If nothing resolves, say so and offer to switch to scratch.
     Report which recognized files are present vs missing (ignore
     unrecognized files like `bootstrap-summary.md`), let the user
     include/exclude each, then for each included file: copy it in
     (refresh frontmatter — preserve `owner`/`schema_version`, set
     `last_updated` to today and `last_updated_by: user`, Status
     `In progress`) and walk the user through adapting the
     project-specific fields. Apply **Source Fidelity**: never carry a
     number from the source project as this project's — confirm or
     replace each. Files missing from the source fall back to the
     from-scratch intake or are skipped, per the user's choice.

5. Execute the sibling `workflow.yaml` phase by phase, skipping any
   intake phase whose file was imported & adapted in step 4. After each
   phase, write the corresponding file under
   `{output_folder}/company-context/` with the schema documented in
   `docs/company-context.md` (frontmatter: `owner`, `last_updated`,
   `last_updated_by: user`, `schema_version: 1`).

6. Outputs: see `docs/company-context.md` for the file table.
