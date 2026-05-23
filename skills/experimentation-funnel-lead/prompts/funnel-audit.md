# Funnel Audit

<instructions>
Audit a funnel for leak points and segment-level patterns.
</instructions>

<process>
1. Ask user for the funnel stages, time window, and current
   stage-to-stage conversion rates. Do not invent.
2. Diagnostic process:
   - Identify the stage(s) with largest leak (absolute, not relative).
   - Segment by: source / cohort / segment / device. Only report
     segment splits with N supporting them.
   - Hypothesise the cause for each leak: copy, friction, audience-
     fit, timing, technical bug.
3. Output: leak ranking, segment-level callouts, top 5 hypotheses for
   the experiment backlog, recommended experiment per hypothesis.
4. Write into `v{n}.md`.
</process>
