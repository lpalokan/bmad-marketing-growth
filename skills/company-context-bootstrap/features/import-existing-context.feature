# Acceptance spec for the "import existing context" capability of the
# company-context-bootstrap workflow.
#
# This skill is LLM-followed Markdown, not compiled code — there is no
# test runner. These scenarios are the behavioural contract the workflow
# (workflow.yaml) and the agent prose (SKILL.md) must satisfy. Walk each
# scenario by hand to verify a change. Keep this file and the workflow in
# lock-step: a behaviour that is not described here is not a requirement.

Feature: Bootstrap company context from an existing context folder
  As a marketer starting a new but similar project,
  I want to seed company-context/ from another project's context
  so that I adapt instead of re-typing everything from scratch.

  Background:
    Given the company-context-bootstrap workflow is activated
    And the recognized context files are icp.md, positioning.md,
        brand-voice.md, kpis.md, tech-stack.md

  Scenario: Offer all four modes at the start
    When the workflow starts
    Then it asks which mode to run: scratch, import, migrate, or ingest

  Scenario: Resolve a path that points straight at a context folder
    Given the user picks "import" and gives a path that directly contains
          recognized context files
    Then the workflow uses that folder as the source

  Scenario: Resolve a path that points at a project or parent folder
    Given the path does not directly contain recognized context files
    Then the workflow looks for "_bmad-output/company-context" then
         "company-context" beneath it, and uses the first that has files

  Scenario: Discover multiple source projects under a parent
    Given the path is a container with several subfolders that each have
          a company-context
    Then the workflow lists each discovered source project
    And prompts the user to choose exactly one before continuing

  Scenario: No context found at the path
    Given the path contains no recognized context files anywhere expected
    Then the workflow says so and offers to start from scratch instead

  Scenario: Report what is available in the chosen source
    Given a source folder is resolved
    Then the workflow lists which recognized files are present and which
         are missing
    And it ignores unrecognized files such as bootstrap-summary.md

  Scenario: Choose which files to bring over
    Given recognized files were discovered in the source
    Then the user can include or exclude each recognized file individually

  Scenario: Copy-then-adapt an included file, upgrading it to OKF
    Given the user includes icp.md
    When the file is imported
    Then the workflow copies it into {output_folder}/company-context/
    And it upgrades the frontmatter to OKF: owner preserved, the OKF fields
        added (type, title, description, tags, timestamp), schema_version
        bumped to 2, last_updated set to today, last_updated_by set to user
    And it walks the user through the project-specific fields to adapt them
        for the new company, applying Source Fidelity — never invent
        numbers, and on missing data ask rather than fill
    And it sets Status to "In progress" while adapting and "Bootstrapped"
        once the user approves

  Scenario: Fill files missing from the source
    Given kpis.md was not present in the source
    When the import step completes
    Then the workflow offers, for that file, to run the normal from-scratch
         intake or to skip it

  Scenario: Never overwrite the target silently
    Given {output_folder}/company-context/ already contains icp.md
    When an import would overwrite it
    Then the workflow shows the existing content against the incoming content
    And asks keep / overwrite before writing

  Scenario: Honour write boundaries
    Then the workflow only ever writes under {output_folder}/company-context/
    And it may also refresh the marketing-growth:okf block in {project-root}/AGENTS.md
