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

  Scenario: Pin the setting so it survives the next install
    When the relocation runs
    Then output_folder is set to {project-root}/output under [core] in
         {project-root}/_bmad/custom/config.toml
    And any content already in that file is preserved
    And _bmad/config.toml is NOT edited
    And _bmad/marketing-growth/config.yaml is NOT edited

  Scenario: Record it in the bundle log
    When the relocation runs
    Then the handoff phase's log.md entry includes a **Relocation** line
    And that label is distinct from the OKF **Migration** mode

  Scenario: Only one bootstrap relocates
    Given /company-context-bootstrap has already relocated the bundle
    When /sales-context-bootstrap is activated afterwards
    Then it finds nothing to move and says nothing
