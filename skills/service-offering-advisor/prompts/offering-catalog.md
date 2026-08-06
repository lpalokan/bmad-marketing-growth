# Build / Update the Offering Catalog

<instructions>
Maintain the canonical catalog of what we sell. Each service offering is an OKF
`Offering` concept at `{output_folder}/company-context/offerings/<slug>.md`, with
the hub `{output_folder}/company-context/offerings.md` holding a one-line summary
plus a link down to each. Otto is the **single writer** of these files. Follow
the OKF frontmatter schema in `docs/company-context.md` exactly.
</instructions>

<process>
1. Read the context that exists: `icp.md` (personas + slices), `positioning.md`
   (pillars/differentiators), and the current `offerings.md`. Note what's absent
   and continue.
2. Enumerate the service offerings with the user. If there are ≥2 distinct
   offerings, explode each into its own concept at `offerings/<slug>.md`; the hub
   `offerings.md` keeps a summary line + link for each (HYBRID granularity per
   `docs/company-context.md`).
3. For **each** offering, capture:
   - **What it comprises** — scope, components, what's in / out.
   - **ICP slice** — which `icp.md` personas and segments it's for; link them as
     `[persona](/personas/<slug>.md)`.
   - **Pains addressed** — each pain mapped to a **quantifiable outcome** and the
     **impacted metric** (pain → outcome → metric). Numbers must be sourced or
     marked `[UNKNOWN — needs input]`.
   - **Buyer personas** — economic buyer, champion, and influencers for this
     offering.
   - **Differentiators** — why us vs alternatives; link `positioning.md` pillars.
   - **Typical deal shape** — motion, rough scope/size band (sourced), sales
     cycle, common entry point.
   - **Proof** — links to the relevant `case-studies/<slug>.md` concepts.
4. Write each offering with OKF frontmatter: `type: Offering`,
   `owner: service-offering-advisor`, `schema_version: 2`, a `Status:` line, and
   the other required fields per `docs/company-context.md`. Use bundle-relative
   links.
5. Update `offerings.md` (hub) summary + links, and append to the bundle-root
   `log.md`. Keep single-writer discipline — never edit `icp.md` or
   `positioning.md`.
6. In the protocol, write `v{n}.md` describing the changes, set `state.yaml`
   `status: in-review`, and notify the orchestrator.
</process>
