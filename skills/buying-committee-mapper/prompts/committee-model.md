# Define / Tune the Buying-Committee Model

<instructions>
Create or update the reusable, cross-account template that says — for our
category — which roles make up a buying committee, the titles that typically fill
each, and the decision criteria each role weighs. This is the owned company-
context concept `{output_folder}/company-context/buying-committee-model.md`, not
a per-account map. Cleo is the single writer.
</instructions>

<process>
1. Read the existing `buying-committee-model.md` if present, and `icp.md` for the
   buyer personas already defined. Read whatever the user shared about how deals
   in our category actually get bought.
2. Write / update the file as an OKF **Buying Committee Model** concept with the
   frontmatter from `docs/company-context.md`:
   ```yaml
   ---
   type: Buying Committee Model
   title: Buying Committee Model
   description: <one sentence>
   tags: [company-context, buying-committee]
   timestamp: <ISO 8601>
   owner: buying-committee-mapper
   last_updated: YYYY-MM-DD
   last_updated_by: <agent-code-or-user>
   schema_version: 2
   ---
   Status: <Bootstrapped | In progress | Stable | Stale (needs refresh)>
   ```
3. For each MEDDPICC role — Economic Buyer, Champion, Technical / evaluator buyer,
   Users, Procurement / Security / Legal — capture: typical titles / functions,
   the metrics that role owns, the decision criteria it weighs (technical /
   business / personal), and how it usually sits relative to the economic buyer.
4. Encode the **champion qualification bar** (power + access-to-EB + personal
   motivation) and the multi-threading expectation (~13 stakeholders is typical
   for an enterprise DMU) so per-account maps inherit both.
5. **Link, don't duplicate.** Where the model references a persona already in
   `icp.md`, link to it with an absolute, bundle-relative Markdown link (e.g.
   `[CTO buyer](/personas/cto-buyer.md)`) rather than copying persona detail into
   this file.
6. Keep numbers sourced (Source Fidelity). Mark anything provisional
   `[UNKNOWN — needs input]` rather than inventing it.
7. Write the file (single-writer — only Cleo). In the protocol, produce `v{n}.md`,
   set `state.yaml` `status: in-review`, and notify the orchestrator; the model
   file itself is updated on acceptance.
</process>
