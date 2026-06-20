# Acceptance spec for the "refresh the project AGENTS.md OKF block"
# behaviour of the company-context-bootstrap workflow's handoff phase.
#
# This skill is LLM-followed Markdown, not compiled code — there is no
# test runner. These scenarios are the behavioural contract the workflow
# (workflow.yaml) and the agent prose (SKILL.md) must satisfy. Walk each
# scenario by hand to verify a change. Keep this file and the workflow in
# lock-step: a behaviour that is not described here is not a requirement.

Feature: Refresh the marketing-growth:okf block in the project AGENTS.md
  As an agent or harness working in a project that installed this suite,
  I want {project-root}/AGENTS.md to carry the OKF briefing-mandate block
  so that anyone working here knows company-context is read-context that
  supports a brief and never widens an agent's mandate.

  Background:
    Given the company-context-bootstrap workflow reaches the handoff phase
    And the canonical block lives in the sibling templates/agents-okf-block.md
        delimited by `<!-- marketing-growth:okf start -->` and
        `<!-- marketing-growth:okf end -->`

  Scenario: Runs in every mode
    When any mode (scratch, import, migrate, or ingest) finishes
    Then the handoff phase ensures the AGENTS.md block, gated with a diff

  Scenario: Create AGENTS.md when absent
    Given {project-root}/AGENTS.md does not exist
    When the handoff ensures the block
    Then it creates AGENTS.md containing exactly the marketing-growth:okf block

  Scenario: Replace the block in place when present
    Given {project-root}/AGENTS.md already contains marketing-growth:okf markers
    When the handoff ensures the block
    Then it replaces everything from the start marker through the end marker
        with the current block
    And it leaves all other content untouched

  Scenario: Append without disturbing existing content
    Given {project-root}/AGENTS.md exists without marketing-growth:okf markers
    And it contains a `<!-- bmad-manager:bmad … -->` block and user prose
    When the handoff ensures the block
    Then it appends the marketing-growth:okf block after the existing content
    And the bmad-manager:bmad block and the user prose are preserved

  Scenario: Idempotent on re-run
    Given the marketing-growth:okf block is already current in AGENTS.md
    When the handoff ensures the block again
    Then the block appears exactly once and the file is otherwise unchanged

  Scenario: Gate before writing
    Then the workflow shows a before/after diff of AGENTS.md and writes only
        on the user's approval
