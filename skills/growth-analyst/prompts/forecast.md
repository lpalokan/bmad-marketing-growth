# Pipeline / Revenue Forecast

<instructions>
Produce a forecast for pipeline or revenue.
</instructions>

<process>
1. Inputs: current pipeline by stage, historical conversion rates per
   stage, current run-rate per channel. Ask for all of these — do
   not invent.
2. Method: bottom-up (per-channel run-rate × confidence × time) and
   top-down (target ÷ historical close-rate ÷ ASP) — reconcile.
3. Sensitivity: best / base / worst with named driver per scenario.
4. Reporting cadence and the trigger that flags re-forecast.
5. Write into `work/{id}/v{n}.md`.
</process>
