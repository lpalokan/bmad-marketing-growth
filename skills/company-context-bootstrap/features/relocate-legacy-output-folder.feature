# Acceptance spec for the automatic relocation of a legacy _bmad-output/
# bundle, performed by BOTH bootstraps on activation (SKILL.md step 2).
#
# This skill is LLM-followed Markdown, not compiled code — there is no test
# runner. These scenarios are the behavioural contract the workflow
# (workflow.yaml) and the agent prose (SKILL.md) must satisfy. Walk each
# scenario by hand to verify a change. Keep this file and the workflow in
# lock-step: a behaviour that is not described here is not a requirement.

Feature: Relocate a legacy _bmad-output/ bundle to output/
  As a user whose project was created by bmad-manager (which seeds
  _bmad-output/company-context/),
  I want the bootstrap to move my context to the canonical output/ folder
  and make it stay there, without being asked anything.

  Background:
    Given either bootstrap is activated
    And {project-root}/output is the canonical output folder

  Scenario: Nothing to relocate
    Given {project-root}/_bmad-output/ does not exist
    When the bootstrap activates
    Then it says nothing about relocation
    And it proceeds straight to the greeting

  Scenario: Only foreign folders present
    Given _bmad-output/ holds planning-artifacts/ but no company-context/
          and no work/
    When the bootstrap activates
    Then it skips relocation silently
    And planning-artifacts/ is left exactly where it is

  Scenario: Relocate the bundle automatically
    Given _bmad-output/company-context/ holds the marketing core
    When the bootstrap activates
    Then company-context/ is moved to output/company-context/
    And work/ is moved too when it exists
    And the user is told in ONE line what moved
    And the user is NOT asked to approve the move
    And the run continues with output_folder set to {project-root}/output

  Scenario: Never overwrite at the destination
    Given _bmad-output/company-context/icp.md exists
    And output/company-context/icp.md already exists
    When the relocation runs
    Then the destination icp.md is left untouched
    And the skipped file is listed for the user

  Scenario: Leave the bmm module's folders alone
    Given _bmad-output/ holds company-context/, planning-artifacts/
          and implementation-artifacts/
    When the relocation runs
    Then only company-context/ moves
    And planning-artifacts/ and implementation-artifacts/ stay in
        _bmad-output/, because _bmad/config.toml still points at them
    And _bmad-output/ is therefore NOT deleted

  Scenario: Remove the legacy folder only when it is empty
    Given _bmad-output/ held nothing but company-context/ and work/
    When both have been moved
    Then _bmad-output/ is deleted

  Scenario: Write no configuration at all
    When the relocation runs
    Then _bmad/config.toml is NOT edited
    And _bmad/marketing-growth/config.yaml is NOT edited
    And _bmad/custom/config.toml is NOT edited
    And no [core] output_folder value anywhere is changed

  Scenario: The move alone is enough to make output/ stick
    Given config still says output_folder is _bmad-output
    And the relocation has emptied _bmad-output/ of company-context/
    When any agent activates afterwards
    Then step 1 skips the _bmad-output candidate, which no longer holds
         the bundle
    And it resolves to {project-root}/output

  Scenario: Leave the other BMAD modules' output alone
    Given core, bmm, bmb and cis each carry their own
          output_folder: _bmad-output in _bmad/<module>/config.yaml
    When the relocation runs
    Then none of those files is touched
    And those modules keep writing exactly where they did before

  Scenario: Record it in the bundle log
    When the relocation runs
    Then the handoff phase's log.md entry includes a **Relocation** line
    And that label is distinct from the OKF **Migration** mode

  Scenario: Only one bootstrap relocates
    Given /company-context-bootstrap has already relocated the bundle
    When /sales-context-bootstrap is activated afterwards
    Then it finds nothing to move and says nothing
