# The account record

One file per account, `account.md`, in
`{output_folder}/work/dossiers/{account-id}/`.

The record is the account. The dossier is a render of it. Every agent reads the
whole record and writes only its own sections.

## Why

Before this, each stage restated the same facts in its own words and the
assembler had to reconcile several versions of one truth. That is where sources
got dropped, where discovery questions got invented at the end instead of falling
out of the gaps, and where the account overview turned into an essay.

## Sections and their owners

| Section | Owner | Nobody else writes here |
|---|---|---|
| Identity and structure | `account-research-analyst` | ✓ |
| Scale and financial frame | `account-research-analyst` | ✓ |
| Goals and ambitions | `account-research-analyst` | ✓ |
| Current plans | `account-research-analyst` | ✓ |
| Control and regulatory environment | `account-research-analyst` | ✓ |
| Technology estate | `account-research-analyst` | ✓ |
| Challenges | `account-research-analyst` | ✓ |
| Why-now signals | `account-research-analyst` | ✓ |
| Offering fit and proof | `service-offering-advisor` | ✓ |
| Opportunity portfolio | `service-offering-advisor` | ✓ |
| Fit verdict and tier | `account-sourcing-strategist` | ✓ |
| Buying committee | `buying-committee-mapper` | ✓ |
| Storyline and pillars | `sales-presentation-advisor` | ✓ |
| Messages | `contact-approach-writer` | ✓ |
| Sources | append-only, everyone | shared |
| Gaps | append-only, everyone | shared |

Two shared sections are append-only, so parallel work cannot clobber them. Every
other section has exactly one writer. An agent that believes another section is
wrong raises it with the orchestrator rather than editing it.

## Fact format

Every entry in the record is one fact, one label, one link.

```markdown
- Cost-to-income 0.71 in H1 2026, from 0.68 in FY2025 and 0.53 in FY2024.
  (KNOW: [H1 2026 half-year report](url), published 2026-07-28)
- The buyer will judge our evidence chain against a supervisor's standard.
  (ASSUME, from the CRO's prior role.)
- Current control-testing and GRC tooling.
  (GAP → discovery question)
```

Write the label at capture. Downstream agents inherit it and never upgrade an
ASSUME to a KNOW without doing the verification themselves.

## What the record gives the dossier for free

- **Sources.** Every fact already carries its URL, so section 8 assembles itself.
- **Discovery questions.** Every GAP is already a named question, so section 6 is
  rendered rather than invented. The altitude buckets and the two per bucket cap
  in `structure.md` then decide which of them reach the AE. A gap that loses its
  slot stays in the gaps list in section 8.
- **A short overview.** The dossier renders a record instead of reproducing an
  essay, which is why the overview can be cut without losing anything.
- **Traceability.** An AE challenged on a figure can find where it came from.

## Frontmatter

The record and the dossier share the frontmatter block in
`../templates/dossier.md`. Two fields matter for safety:

- `supersedes:` names the file this one replaces. Never overwrite a dossier.
- `not_to_be_confused_with:` is internal metadata. It must never render into the
  reader's view. See `third-parties.md`.
