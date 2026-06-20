# Acceptance spec for the "migrate to OKF" mode of the
# company-context-bootstrap workflow.
#
# This skill is LLM-followed Markdown, not compiled code — there is no
# test runner. These scenarios are the behavioural contract the workflow
# (workflow.yaml) and the agent prose (SKILL.md) must satisfy. Walk each
# scenario by hand to verify a change. Keep this file and the workflow in
# lock-step: a behaviour that is not described here is not a requirement.

Feature: Migrate an existing non-OKF company-context to the OKF bundle format
  As a user who bootstrapped context before OKF adoption,
  I want to upgrade my existing company-context/ files in place
  so that the folder becomes a valid OKF v0.1 bundle without re-typing.

  Background:
    Given the company-context-bootstrap workflow is activated
    And {output_folder}/company-context/ already contains legacy files
        with schema_version 1 frontmatter and no `type` field

  Scenario: Offer migrate mode at the start
    When the workflow starts
    Then it asks which mode to run: scratch, import, migrate, or ingest

  Scenario: Scan and classify existing files
    Given the user picks "migrate"
    Then the workflow lists the files present under company-context/
    And it reports each as already-OKF (has a non-empty `type`) or legacy
    And it writes nothing during the scan

  Scenario: Nothing to migrate
    Given company-context/ is missing or empty
    When migrate runs
    Then the workflow says so and offers to switch to scratch

  Scenario: Upgrade a legacy file in place
    Given icp.md is legacy
    When the file is migrated
    Then the workflow derives type, title, description, tags, and timestamp
    And it preserves the owner and the Status line exactly
    And it bumps schema_version to 2
    And it does NOT change the body content
    And it shows existing vs upgraded frontmatter and asks keep / overwrite
        before writing

  Scenario: Explode only on request
    Given icp.md already lists two or more distinct buyer personas
    When the file is migrated
    Then the workflow offers to explode them into personas/<slug>.md
    And it creates those concepts and links them from icp.md only if the
        user approves

  Scenario: Refresh the bundle scaffold after migrating
    When migration completes
    Then the workflow writes/refreshes the root index.md with okf_version "0.1"
    And it appends a dated **Migration** entry to log.md

  Scenario: Honour write boundaries
    Then the workflow only ever writes under {output_folder}/company-context/
    And it may also refresh the marketing-growth:okf block in {project-root}/AGENTS.md
