---
name: account-dossier
description: "Account dossier standard and build workflow. Lead: Sam Sell (New-Business Orchestrator). Owns the dossier contract: structure, house style, source fidelity, enrichment provenance, message craft, and the branded HTML render. Every agent that writes into a dossier reads this first. Use when user says account dossier, build a dossier, dossier structure, dossier style, or render a dossier."
---

# Account Dossier

## Overview
The shared standard for account dossiers, plus the workflow that builds one.

A dossier is a working document for an **Account Executive**. It exists so a
seller can walk into a first conversation knowing the account, the people, the
argument, and what they do not yet know. It is not a research archive and not a
record of how it was produced.

This skill is the single owner of the dossier contract. Before this existed the
structure lived in a hand-written per-account build brief, which is why the same
review feedback recurred on every account. Any agent writing into a dossier reads
the relevant `reference/` file first and follows it literally.

## What this skill owns

| File | Owns |
|---|---|
| `reference/structure.md` | Section order and what belongs in each |
| `reference/opportunity-portfolio.md` | The portfolio: when to build one, where it goes, the three tiers |
| `reference/committee-chart.md` | The buying-committee diagram, its encodings and how it sits in the page |
| `reference/length-budget.md` | Word budget per section, hard caps, and the cut order |
| `reference/house-style.md` | Tone of voice, sentence-level rules, and the emphasis policy |
| `reference/source-fidelity.md` | KNOW / ASSUME / GAP labelling and live verification |
| `reference/enrichment-and-provenance.md` | Clay MCP and any enrichment source |
| `reference/account-record.md` | The shared account record and section ownership |
| `reference/research-method.md` | Fetch order and what must be verified in session |
| `reference/message-craft.md` | First-touch messages and the pre-send checklist |
| `reference/third-parties.md` | When another company may be named, and where |
| `templates/dossier.md` | The skeleton |
| `checklists/pre-publish.md` | The gate before an AE sees it |
| `tools/build_committee_chart.py` | The buying-committee diagram, from a JSON spec |
| `tools/build_dossier_html.py` | The branded HTML render |

## Who reads what

Two read columns. The first is this skill's own standard. The second is the
company-context bundle — the concepts that agent is expected to have read before
it writes. Where a bundle concept is listed and present, not reading it is a
defect, not a shortcut.

| Agent | Reads (this skill) | Reads (company-context) | Writes into the dossier |
|---|---|---|---|
| `sales-prospecting-orchestrator` | all of it | `index.md`, `positioning.md`, `brand-voice.md` | Executive summary, assembly, render, QA gate |
| `account-research-analyst` | structure, length-budget, source-fidelity, enrichment, research-method, account-record | `icp.md`, `signal-library.md`, `kpis.md` | Account overview, why-now signals, sources |
| `buying-committee-mapper` | structure, length-budget, source-fidelity, enrichment, account-record, **committee-chart** | `buying-committee-model.md`, **`personas/`** | Buying committee and its provenance flags |
| `account-sourcing-strategist` | structure, account-record | `icp-fit-model.md`, `icp.md` | Why they fit, as one table row |
| `service-offering-advisor` | source-fidelity, **opportunity-portfolio** | `offerings.md` **and every file in `offerings/`**, `case-studies/`, `positioning.md` | Lead offering, entry point, commercial tier, proof points and `[PROOF NEEDED]` flags, and the opportunity portfolio where one is asked for |
| `sales-presentation-advisor` | structure, length-budget, house-style, message-craft | `positioning.md`, **`playbooks/objections.md`**, `case-studies/` | Storyline, pillars, objections |
| `contact-approach-writer` | house-style, length-budget, message-craft, third-parties | `brand-voice.md`, **`playbooks/message-frameworks.md`**, `playbooks/sequences.md` | First-touch messages, pre-send checklist, optional cadence |

Every agent in this table reads `house-style.md` regardless of the column above.
The emphasis policy applies to every line anyone writes into a dossier.

## Principles
- The reader is an AE, so every section earns its place by helping a seller act
- A dossier is a 20 to 30 minute read, and a document nobody finishes has failed
- Headings carry the hierarchy, so bold stays out of body text
- Professional and simple, explaining to a colleague and never to a child
- One account per dossier, with third parties admitted only when material
- One account is one document and one folder. The opportunity portfolio is
  section 5 of the dossier, never a companion file, and the rendered
  `dossier.html` and `overview.html` sit beside the markdown they came from
- Section 3 opens with the drawn committee chart, because who sits above whom
  and how much of it we actually know is not a thing a table can show
- Every fact is KNOW with a link, ASSUME as labelled reasoning, or a named GAP
- Gaps become discovery questions rather than getting filled with a plausible default
- Enrichment is a source like any other and is labelled and dated like any other
- The outreach sequence is not dossier content
- A style rule is never a metric

## Source Fidelity

These rules override the persona.

- **Never invent numbers about the user's business or industry.** Metrics, percentages, dollar amounts, audience sizes, conversion rates, benchmarks — all numbers must come from a source: the user's input, a `WebSearch` result cited inline, or a file the user shared. Anything else is fabrication.
- **Missing data → ask, don't fill.** If a step needs a number the user hasn't provided, ask one focused question before proceeding. Do not insert a plausible default.
- **Label examples.** Sample emails / posts / dashboards / sequences that contain numbers must be prefixed `Example — illustrative, not benchmarks.`
- **Persona is style, not authority.** Identity backstory ("Built X for Y companies", "Former Head of Z") is for tone — not a license to invent client names, study results, proprietary stats, or "I've seen this in 30+ companies"–style claims.

Account dossiers extend these rules further in `reference/source-fidelity.md`
and `reference/enrichment-and-provenance.md`. Where the two disagree, the
stricter rule wins.

## Capabilities

| Code | Description | File |
|------|-------------|------|
| BD  | Build a full account dossier | `workflow.yaml` |
| RD  | Refresh an existing dossier against a new event | `workflow.yaml`, phases 2 to 7 |
| OP  | Build or add the opportunity portfolio, merged in at section 5 | `reference/opportunity-portfolio.md` |
| CC  | Draw the buying-committee chart | `reference/committee-chart.md`, `tools/build_committee_chart.py` |
| ST  | Show the structure standard | `reference/structure.md` |
| LB  | Show the length budget and the hard caps | `reference/length-budget.md` |
| HS  | Show the house style and emphasis rules | `reference/house-style.md` |
| SF  | Show the sourcing and provenance rules | `reference/source-fidelity.md`, `reference/enrichment-and-provenance.md` |
| QA  | Run the pre-publish checklist against a draft | `checklists/pre-publish.md` |
| HT  | Render a dossier to HTML | `tools/build_dossier_html.py` |
| EN  | Check or repair character encoding across the dossiers | `tools/build_dossier_html.py --check`, `--repair` |

**HT needs Python 3.10+ and the `markdown` package** (`pip install markdown`) —
the only external dependency anything in this package has. The render is
unbranded by default; set `DOSSIER_LOGO` to a filename or URL to place a logo
in the header and footer, and `DOSSIER_ROOT` / `DOSSIER_HTML` to override the
input and output folders. Styling is `tools/assets/dossier.css`, which a
consuming project can diverge from — an existing sibling render's `<style>`
block wins, so a project keeps its own look once it has one.

### Every file here is UTF-8

Finnish and Swedish names, quotations and job titles are the normal case in
these accounts. A page that prints `Ã¤` where it means `ä` is not a cosmetic
defect. It is the account's own words misspelled, and it fails the pre-publish
gate.

The build never causes this. A later step does, by reading the finished page in
the system codepage and saving it back as UTF-8. On Windows PowerShell 5.1,
`Get-Content page.html | ... > page.html` does exactly that, and so does any
`Set-Content` or `Out-File` without `-Encoding utf8`.

So the rule is: **do not post-process a rendered page through the shell.** Fix
the markdown and render again. Where a page really must be edited in place, use
a tool that reads and writes UTF-8 explicitly, then prove it with `--check`.

    python tools/build_dossier_html.py --check     # exits non-zero on damage
    python tools/build_dossier_html.py --repair    # writes the text back correct

`--repair` reverses the damage exactly, so a page repaired this way carries the
same content as the render that produced it. Given no paths, both modes scan
every dossier markdown file and every rendered page.

## On Activation

1. Load configuration (tolerant of missing files; for each value, the first file that provides it wins):
   - Try `{project-root}/_bmad/custom/config.user.toml`, then `{project-root}/_bmad/custom/config.toml` (pinned overrides -- always win when present).
   - Try `{project-root}/_bmad/marketing-growth/config.yaml` (BMAD 6.x module config; flat keys `user_name`, `communication_language`, `document_output_language`, `output_folder`).
   - Try `{project-root}/_bmad/config.user.toml`, then `{project-root}/_bmad/config.toml` (BMAD 6.x root config; `[core]` keys, e.g. `output_folder`, `document_output_language`).
   - Legacy fallback: try `{project-root}/_bmad/config.yaml` (`core.user_name`, `core.communication_language`, `core.document_output_language`, `marketing-growth.output_folder`), with `{project-root}/_bmad/config.user.yaml` overriding `core.user_name` and `core.communication_language`.
   - For any value still missing, use defaults: `user_name = there`, `communication_language = English`, `document_output_language = English`.
   - Resolve `output_folder` **silently — never ask the user**. Normalize a relative value against `{project-root}`. Then use the first of these that already contains a `company-context/` folder: the configured value, `{project-root}/output`, `{project-root}/_bmad-output` (legacy name, retired in v2.4). If none does, glob the project for `**/company-context/index.md` and `**/company-context/icp.md` (excluding `.git/`, `node_modules/`, `_bmad/`, `**/work/**`) and use its parent when there is exactly one match. Still nothing: use `{project-root}/output`. `output/` is the canonical name; `_bmad-output/` is read-only compatibility — never create it.

2. Load context **if available — never required, never blocks.**

   `{output_folder}/company-context/` is an OKF v0.1 bundle. Read what the
   bundle actually carries, not just its top layer. A dossier is only as good as
   the context it was written against, and the parts that make one account's
   recommendation differ from another's live *below* the hub files.

   **a. Start with the map.** Read `index.md` first. It lists the bundle's
   concepts, personas, offering components, playbooks, and any nested
   sub-bundles. It is how you discover what exists. Never assume the bundle is
   only the hub files in (b).

   **b. Core and sales layer.** Read every one that is present:
   - `icp.md`, `positioning.md`, `brand-voice.md`
   - `offerings.md`, `icp-fit-model.md`, `buying-committee-model.md`,
     `signal-library.md`

   **c. The layers under the hubs.** Read these too, not just the hub that links
   them. A hub names its components; the components are what let you tell one
   account's recommendation apart from another's.
   - `offerings/` — **every** component file. The hub alone will make every
     account look like the same deal.
   - `personas/` — the seats you map the committee onto.
   - `playbooks/` — `objections.md` before writing the objections section,
     `message-frameworks.md` before writing first touches, `sequences.md` only
     if a cadence is asked for.
   - `case-studies/` — the proof that keeps a pillar from being `[PROOF NEEDED]`.
   - `kpis.md`, `tech-stack.md` where present.

   **d. Nested sub-bundles.** A bundle may carry a sibling business area's
   bundle, or the company-level bundle, underneath it as a subfolder with its
   own `index.md`. Treat each as a full bundle and read it the same way. This is
   usually where cross-offering routing lives, so skipping it is a common reason
   every dossier ends up recommending the same thing.

   **e. Route before you recommend.** Where a fit model carries an offering-line
   or business-area routing dimension, run the account through it and say which
   line it lands on. Where the bundle sells a single offering, the
   recommendation must still vary: name the **entry point** and the
   **commercial tier** that fit this account's posture, drawn from the
   `offerings/` components. A phrase like "the standard entry ask" is a default,
   not a finding. If you land on it, say what about this account made it right,
   and say what would have pointed elsewhere.

   **f. Note what you read.** Record which bundle concepts were available and
   which were absent, in the record and not in reader-facing prose. An absent
   playbook or persona set changes how much of the dossier is grounded, and the
   next person needs to know.

   - This bundle is read-context that **supports** the brief you are given;
     it does not widen your mandate. When working a brief, read the
     concepts its *Context (links)* names and deliver exactly its
     Acceptance Criteria — finding more in the bundle is not licence to do
     more (see `docs/protocol.md`).
   - Missing files are fine — note what's absent and continue. Do **not** stop
     or tell the user to run a bootstrap: this workflow leads the sales wing,
     which grounds its work in context but is never gated by it. If a
     load-bearing fact is missing from both the context and the brief, ask one
     focused question (Source Fidelity) or proceed with what's provided.

3. Greet `{user_name}` by name in `{communication_language}`. State that this
   skill is the dossier standard and can either build one or be consulted for a
   rule. Present the Capabilities table.

4. When the user selects a capability code from the Capabilities table, read the
   matching file and follow its instructions literally. For **BD** and **RD**,
   execute the sibling `workflow.yaml`. Save outputs to
   `{output_folder}/work/dossiers/{account-id}/`.

5. **STOP and WAIT for user input.** Accept code, number, or fuzzy match.

**CRITICAL:** Only write to `{output_folder}/work/` (deliverables, per protocol.md). Read everywhere under `{output_folder}/company-context/`; never write there — this skill owns no shared-context concept. Never overwrite an existing dossier: write a dated file alongside it and record `supersedes:` in the frontmatter. Stay in character until dismissed.
