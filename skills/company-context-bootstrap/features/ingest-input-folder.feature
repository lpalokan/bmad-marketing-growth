# Acceptance spec for the "ingest the input folder" mode of the
# company-context-bootstrap workflow.
#
# This skill is LLM-followed Markdown, not compiled code — there is no
# test runner. These scenarios are the behavioural contract the workflow
# (workflow.yaml) and the agent prose (SKILL.md) must satisfy. Walk each
# scenario by hand to verify a change. Keep this file and the workflow in
# lock-step: a behaviour that is not described here is not a requirement.

Feature: Ingest a raw input folder into the OKF company-context bundle
  As a user with raw research, exports, and docs to add,
  I want to drop files in input/ and have them refactored into OKF concepts
  so that new knowledge is folded into company-context/ — anytime, not just
  at project start.

  Background:
    Given the company-context-bootstrap workflow is activated
    And the input folder is config marketing-growth.input_folder if set,
        else {project-root}/input/

  Scenario: Offer ingest mode at the start
    When the workflow starts
    Then it asks which mode to run: scratch, import, migrate, or ingest

  Scenario: Resolve and enumerate the input folder
    Given the user picks "ingest"
    Then the workflow lists every file found in the input folder
    And it confirms the set to ingest before reading bodies

  Scenario: No input to ingest
    Given the input folder is missing or empty
    When ingest runs
    Then the workflow says where it looked and stops, offering another mode

  Scenario: Refactor an input file into an OKF concept
    Given the user confirms a PDF in the input folder
    When it is ingested
    Then the workflow reads it with the Read tool
    And it drafts one or more OKF concept docs under company-context/sources/
    And each concept has a non-empty type, resource set to the original input
        path, timestamp today, and last_updated_by user
    And each concept cross-links to the relevant core hub with an absolute link
    And the workflow shows the planned sources/ files before writing

  Scenario: Propose gated updates to a core file
    Given an ingested source describes a new buyer persona
    When ingest folds knowledge in
    Then the workflow proposes an edit to the owner of icp.md
    And it shows a before/after diff and confirms every number (Source Fidelity)
    And it applies the edit only on approval, made to the owner file only
    And on decline the knowledge still remains in its sources/ concept

  Scenario: Never invent or silently promote numbers
    Given an ingested source contains a metric figure
    Then the figure is carried into sources/ only as the source states it, cited
    And it is never promoted into a core file without the user's confirmation

  Scenario: Leave the input files untouched
    When ingest completes
    Then the original files in the input folder are not moved or deleted
    And a dated **Ingest** entry (one line per source) is appended to log.md

  Scenario: Honour write boundaries
    Then the workflow only ever writes under {output_folder}/company-context/
    And it reads nothing outside the input folder and company-context/
