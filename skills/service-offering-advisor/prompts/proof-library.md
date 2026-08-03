# Curate the Case-Study / Proof Library

<instructions>
Maintain the reusable proof library. Each case study is an OKF `Case Study`
concept at `{output_folder}/company-context/case-studies/<slug>.md`. Ownership
of `case-studies/` defers to the `customer-advocacy-references` (Cara Customer)
agent, part of this suite; Otto is the single writer only when that agent is
unavailable. Follow the OKF frontmatter schema in `docs/company-context.md` exactly.
</instructions>

<process>
1. Read the context that exists: `offerings.md` (which offerings need proof) and
   any current `case-studies/`. If Cara Customer owns `case-studies/`, stop and
   route the request to her rather than writing.
2. For **each** case study, capture:
   - **Customer** — name, vertical, size band (sourced or `[UNKNOWN — needs input]`).
   - **Problem** — the pain/situation before.
   - **Quantified outcome** — the result, with a **source cited inline** for every
     number. No source → do not include the number.
   - **Quote** — a usable customer quote, attributed, if one exists.
   - **Vertical / offering fit** — link the `offerings/<slug>.md` it proves.
3. Apply **Source Fidelity** to every figure: metrics come from the user's input,
   a cited `WebSearch`/`WebFetch` result, or a file the user shared — never
   invented. Prefix any illustrative sample with
   `Example — illustrative, not benchmarks.`
4. Write each case study with OKF frontmatter: `type: Case Study`,
   `owner: service-offering-advisor`, `schema_version: 2`, a `Status:` line, and
   the other required fields. Use bundle-relative links.
5. Cross-link: add the case study to the proof section of the offering(s) it
   supports, and append to the bundle-root `log.md`.
6. In the protocol, write `v{n}.md`, set `state.yaml` `status: in-review`, and
   notify the orchestrator.
</process>
