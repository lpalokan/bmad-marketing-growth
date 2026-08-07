---
name: company-context-bootstrap
description: "Workflow that builds and maintains output/company-context/ as a Google OKF (Open Knowledge Format) bundle — ICP, positioning, brand voice, KPIs, tech-stack, plus index.md and log.md, and refreshes the project's AGENTS.md OKF block. Four modes: scratch intake, import & adapt another project's context, migrate existing non-OKF files to OKF, and ingest the input/ folder (refactor dropped files into OKF concepts and fold new knowledge in). Must be run before any v2 agent. Lead: marketing-orchestrator. Use when user says set up company context, bootstrap, initial intake, reuse/clone/import context, migrate to OKF, refactor context to OKF, ingest input folder, or add knowledge to context."
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

1. Load configuration (tolerant of missing files; for each value, the first file that provides it wins):
   - Try `{project-root}/_bmad/custom/config.user.toml`, then `{project-root}/_bmad/custom/config.toml` (pinned overrides -- always win when present).
   - Try `{project-root}/_bmad/marketing-growth/config.yaml` (BMAD 6.x module config; flat keys `user_name`, `communication_language`, `document_output_language`, `output_folder`).
   - Try `{project-root}/_bmad/config.user.toml`, then `{project-root}/_bmad/config.toml` (BMAD 6.x root config; `[core]` keys, e.g. `output_folder`, `document_output_language`).
   - Legacy fallback: try `{project-root}/_bmad/config.yaml` (`core.user_name`, `core.communication_language`, `core.document_output_language`, `marketing-growth.output_folder`), with `{project-root}/_bmad/config.user.yaml` overriding `core.user_name` and `core.communication_language`.
   - For any value still missing, use defaults: `user_name = there`, `communication_language = English`, `document_output_language = English`.
   - Resolve `output_folder` **silently — never ask the user**. Normalize a relative value against `{project-root}`. Then use the first of these that already contains a `company-context/` folder: the configured value, `{project-root}/output`, `{project-root}/_bmad-output` (legacy name, retired in v2.4). If none does, glob the project for `**/company-context/index.md` and `**/company-context/icp.md` (excluding `.git/`, `node_modules/`, `_bmad/`, `**/work/**`) and use its parent when there is exactly one match. Still nothing: use `{project-root}/output`. `output/` is the canonical name; `_bmad-output/` is read-only compatibility — never create it.

2. **Relocate a legacy `_bmad-output/` bundle — automatic, one line, no
   question.** If `{project-root}/_bmad-output/` holds `company-context/`
   or `work/` (bmad-manager seeds new projects there), move this module's
   folders to the canonical `{project-root}/output/`:

   - Move `_bmad-output/company-context/` and `_bmad-output/work/` into
     `{project-root}/output/`, creating it if absent. **Merge, never
     overwrite**: where a file already exists at the destination, keep the
     destination file and list the ones you skipped.
   - Leave everything else in `_bmad-output/` alone. `planning-artifacts/`
     and `implementation-artifacts/` belong to the **bmm** module and its
     `_bmad/config.toml` still points at them — moving those would break
     bmm. Delete `_bmad-output/` only if it is now empty.
   - Pin the setting so it survives future installs: set
     `output_folder = "{project-root}/output"` under `[core]` in
     `{project-root}/_bmad/custom/config.toml`, creating that file if
     needed and preserving anything already in it. It is the documented
     pinned-override location and the installer never regenerates it. Do
     **not** edit `_bmad/config.toml` or
     `_bmad/marketing-growth/config.yaml` — the installer overwrites both.
   - Set `{output_folder}` to `{project-root}/output` for the rest of this
     run, tell the user in **one line** what moved, and continue without
     asking.
   - Record it in the handoff `log.md` entry as a **Relocation** (distinct
     from the OKF **Migration** mode).

   If `_bmad-output/` is absent, or holds neither folder, skip this step
   silently — say nothing.

3. Greet the user in `{communication_language}` and explain: this
   workflow gathers the foundational knowledge the rest of the v2
   marketing suite needs and writes it as an **OKF v0.1 bundle** under
   `{output_folder}/company-context/` (the five core files plus
   `index.md` and `log.md`). A full scratch intake takes 20–45 minutes
   depending on how much is already documented; migrate and ingest are
   shorter.

4. Locate the bundle before assuming there isn't one. Check
   `{output_folder}/company-context/`; if that is empty or absent, glob
   the project for `**/company-context/icp.md` and
   `**/company-context/index.md`, excluding `.git/`, `node_modules/`,
   `_bmad/` and `**/work/**`. One hit — use it as the bundle and say
   which path you found, in one line, without asking anything. Several
   hits — list them with file counts and ask which to use (this is the
   only case worth a question; guessing would be wrong). No hits — there
   is genuinely no bundle, and a new one goes in
   `{output_folder}/company-context/`.

   Then, for each existing file, show the user the current content and
   ask: keep / refresh / skip-this-file.

5. Ask which mode to use: **scratch**, **import & adapt**, **migrate**,
   or **ingest** (see the four `## Overview` modes).

   - **Import & adapt**: ask for a folder path and resolve it (tolerant,
     never guess content). Use it directly if it contains recognized
     context files (`icp.md`, `positioning.md`, `brand-voice.md`,
     `kpis.md`, `tech-stack.md`); otherwise glob up to **three levels**
     below it for any folder holding two or more recognized files. That
     finds `output/company-context/`, `_bmad-output/company-context/`,
     a bare `company-context/`, and the `context/<company>/` layout the
     companion `dwf-marketing-skills` repo uses — without needing the
     folder to be named anything in particular. One match: use it. Two
     or more: list each as `<relative path> (N recognized files)` and
     ask the user to choose one. If nothing resolves, say where you
     looked and offer to switch to scratch.
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

   - **Ingest**: resolve the input folder silently, same rule as
     `output_folder` — the first of these that exists and is non-empty:
     a configured `input_folder` (flat key, or legacy
     `marketing-growth.input_folder`), `{project-root}/input`,
     `{project-root}/_bmad-input` (legacy). Default `{project-root}/input`.
     Then refactor each file into OKF concept docs under `sources/`
     (`resource` = original path), cross-link to the core hubs, then
     propose **gated** edits to the owner of any core file the new
     knowledge bears on. Apply **Source Fidelity** to every number.
     Leave the original input files untouched.

6. Execute the sibling `workflow.yaml` phase by phase for the chosen
   mode (skip any intake phase whose file was imported & adapted in
   step 5; migrate and ingest skip intake entirely). Write every concept
   per `workflow.yaml::okf_conventions` and the schema in
   `docs/company-context.md` (OKF frontmatter + `owner`, `last_updated`,
   `last_updated_by`, `schema_version: 2`; Status line in the body).

7. Always finish in the **handoff** phase: refresh the root `index.md`
   (`okf_version: "0.1"`), append a dated `log.md` entry, and refresh the
   `marketing-growth:okf` block in `{project-root}/AGENTS.md` (idempotent,
   gated with a diff — read it from the sibling
   `templates/agents-okf-block.md`). Outputs: see `docs/company-context.md`
   for the file table and bundle layout.
