---
name: company-context-bootstrap
description: "Workflow that builds and maintains _bmad-output/company-context/ as a Google OKF (Open Knowledge Format) bundle — ICP, positioning, brand voice, KPIs, tech-stack, plus index.md and log.md. Four modes: scratch intake, import & adapt another project's context, migrate existing non-OKF files to OKF, and ingest the input/ folder (refactor dropped files into OKF concepts and fold new knowledge in). Must be run before any v2 agent. Lead: marketing-orchestrator. Use when user says set up company context, bootstrap, initial intake, reuse/clone/import context, migrate to OKF, refactor context to OKF, ingest input folder, or add knowledge to context."
---

# Company Context Bootstrap Workflow

## Overview
Builds and maintains the shared `company-context/` bundle every v2 agent
reads on activation: the five core files `icp.md`, `positioning.md`,
`brand-voice.md`, `kpis.md`, `tech-stack.md`, plus the OKF bundle scaffold
`index.md` and `log.md`. The folder **is a Google OKF v0.1 bundle** — see
`docs/company-context.md` for the schema and `workflow.yaml::okf_conventions`
for the authoring rules. Run at project start; re-running refreshes files
in place (prior content shown for review before overwrite).

Four modes:

- **Scratch** — answer focused intake questions per core file.
- **Import & adapt** — point at another project's context folder (or a
  parent folder of projects); the workflow discovers what's available,
  lets you pick a source and which files to bring over, copies each in
  (upgrading frontmatter to OKF), and walks you through adapting the
  project-specific parts. See `features/import-existing-context.feature`.
- **Migrate** — upgrade an existing non-OKF `company-context/` in place to
  the OKF bundle format (schema_version 1 → 2; bodies untouched). One-time.
  See `features/migrate-to-okf.feature`.
- **Ingest** — read the `input/` folder, refactor each file into OKF
  concept docs under `sources/`, cross-link them, and propose gated edits
  to the owner of any core file the new knowledge bears on. Run anytime.
  See `features/ingest-input-folder.feature`.

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
   marketing suite needs and writes it as an **OKF v0.1 bundle** under
   `{output_folder}/company-context/` (the five core files plus
   `index.md` and `log.md`). A full scratch intake takes 20–45 minutes
   depending on how much is already documented; migrate and ingest are
   shorter.

3. Check `{output_folder}/company-context/` for existing files. For
   each that exists, show the user the current content and ask:
   keep / refresh / skip-this-file.

4. Ask which mode to use: **scratch**, **import & adapt**, **migrate**,
   or **ingest** (see the four `## Overview` modes).

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
     (upgrade frontmatter to OKF — preserve `owner`, add the OKF fields,
     bump `schema_version` to 2, set `last_updated` to today and
     `last_updated_by: user`, Status `In progress`) and walk the user
     through adapting the project-specific fields. Apply **Source
     Fidelity**: never carry a number from the source project as this
     project's — confirm or replace each. Files missing from the source
     fall back to the from-scratch intake or are skipped, per the user's
     choice.

   - **Migrate**: upgrade the existing non-OKF `company-context/` in
     place to OKF — derive `type`/`title`/`description`/`tags`/`timestamp`,
     preserve `owner` and the Status line, bump `schema_version` to 2,
     leave bodies untouched, gate each write with a diff.

   - **Ingest**: resolve the input folder (config
     `marketing-growth.input_folder`, else `{project-root}/input/`),
     refactor each file into OKF concept docs under `sources/`
     (`resource` = original path), cross-link to the core hubs, then
     propose **gated** edits to the owner of any core file the new
     knowledge bears on. Apply **Source Fidelity** to every number.
     Leave the original input files untouched.

5. Execute the sibling `workflow.yaml` phase by phase for the chosen
   mode (skip any intake phase whose file was imported & adapted in
   step 4; migrate and ingest skip intake entirely). Write every concept
   per `workflow.yaml::okf_conventions` and the schema in
   `docs/company-context.md` (OKF frontmatter + `owner`, `last_updated`,
   `last_updated_by`, `schema_version: 2`; Status line in the body).

6. Always finish in the **handoff** phase: refresh the root `index.md`
   (`okf_version: "0.1"`) and append a dated `log.md` entry. Outputs:
   see `docs/company-context.md` for the file table and bundle layout.
