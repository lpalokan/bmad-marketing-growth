# Advise Which Offering Fits

<instructions>
Given an account or context, recommend which offering(s) fit and why, with the
pains to lead with and the proof to cite. This is the deliverable the
`offering-advice.md` brief commissions. Output is `v{n}.md` (in the protocol) or
a work note at `{output_folder}/work/{account-id}/offering-advice.md`
(standalone). This is per-account advice — a **work** artifact, not a
`company-context/` file.
</instructions>

<process>
1. Read the brief and the context that exists: `icp.md`, `offerings.md` (+ the
   per-offering concepts), `positioning.md`, and the account's
   `account-profile.md` if present. Do not block on missing context.
2. Extract the account's actual pains, initiatives, and why-now from the profile.
   If pains are unclear and unsourced, ask one focused question rather than
   guessing.
3. Match against the catalog: rank the offering(s) whose ICP slice and pains best
   fit this account. Recommend the best-fit offering, not the biggest.
4. For each recommended offering, map its **pains → quantifiable outcomes → the
   metric moved**, tied to what's true about this account.
5. Name the **pains to lead with** first, and explicitly name **what NOT to lead
   with** for this account (offerings or angles that don't fit). If the profile
   carries a **§4 field scan** (who's circling, what language the buyer has already
   been sold), differentiate against it — avoid an angle the buyer is already
   saturated with, and prefer one the field is not landing.
6. Cite at least one relevant `case-studies/<slug>.md` as proof — matched on
   vertical or pain where possible. Apply Source Fidelity to every number.
7. Write the advice with a short **Sources** section. Mark any gap as
   `[UNKNOWN — needs input]`.
8. In the protocol, write `v{n}.md`, set `state.yaml` `status: in-review`, and
   notify the orchestrator.
</process>
