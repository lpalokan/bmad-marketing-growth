# MAP Workflow Spec

<instructions>
Produce a spec for a MAP workflow that a human will implement.
</instructions>

<process>
1. Read brief, `tech-stack.md`, `icp.md`.
2. Define:
   - Trigger (event or field change).
   - Segmentation filters.
   - Branch logic (each branch with explicit conditions).
   - Actions per branch (emails, internal notifications, CRM updates,
     score deltas).
   - Exit criteria (per branch — no infinite loops).
   - Instrumentation: one event emitted per branch (so the workflow is
     observable in the analytics layer).
   - Test cases: positive, negative, edge (duplicates, missing fields,
     opt-outs).
3. Consent / compliance: honor opt-outs globally; respect regional
   double-opt-in (DACH) and unsubscribe SLAs.
4. Mark "human action required" steps explicitly (no implementation
   in this agent).
5. Write into `v{n}.md`.
</process>
