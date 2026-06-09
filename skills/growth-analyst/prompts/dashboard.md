# Dashboard Build / Refresh

<instructions>
Spec a dashboard build or refresh.
</instructions>

<process>
1. Audience for the dashboard: exec (weekly), domain orchestrator
   (daily), specialist (real-time).
2. KPI rows: pull definitions from `kpis.md`. Fetch current value and
   target from the live source (BI tool from `tech-stack.md`) and the
   annual plan — those don't live in `kpis.md` by design (they rot).
   Owner per row comes from the team org chart, not the file.
3. Layout: ≤ 1 screen per audience (scrolling = not read).
4. Drill-paths: each top-line KPI links to its diagnostic view.
5. Hand-off: where it lives (BI tool from `tech-stack.md`), who builds.
6. Write into `work/{id}/v{n}.md`.
</process>
