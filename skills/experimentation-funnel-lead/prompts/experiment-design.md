# Experiment Design

<instructions>
Design a single experiment end-to-end per the brief.
</instructions>

<process>
1. Read brief, `kpis.md`, `tech-stack.md`.
2. Restate the hypothesis in one sentence. If ambiguous, flag and
   ask before proceeding.
3. Choose randomization unit (visitor / account / user / cohort) with
   rationale; check it matches the experimentation platform's
   capability.
4. Define primary metric + 2 guardrail metrics + segmentation
   dimensions. Each tied to a KPI in `kpis.md`.
5. Sample-size calculation: state baseline, MDE, power (default 80%),
   alpha (default 5% two-sided). Show the math. Cite baseline source.
6. Duration estimate: required N ÷ weekly traffic at randomization
   unit. State if the experiment will starve.
7. Rollback plan: how the variant is killed in < 15 minutes.
8. Read-out plan: cadence and the pre-registered rollout criterion
   ("rollout if primary metric > +X% with p<.05 and no guardrail
   regression > Y%").
9. Write into `v{n}.md`. Update `state.yaml`.
</process>
