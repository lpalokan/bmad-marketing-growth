# Maintain the Objection Library

<instructions>
Create or update `{output_folder}/company-context/playbooks/objections.md` — the
objection library the whole suite reasons from. This is an OKF `Playbook`
concept, owned by `reply-objection-handler`: Ricky is the **single writer**. Each
common objection maps to its **reframe** and the **proof** to counter it. This is
durable, reusable context (not a per-account work artifact), so it lives in the
bundle, never under `work/`.
</instructions>

<process>
1. Read the current `playbooks/objections.md` if it exists, plus `positioning.md`
   (the differentiation the reframes lean on) and `offerings.md` (the proof
   points). Note what's absent and continue.
2. Organize the library by **objection category** — at minimum: price / budget,
   timing, incumbent / status quo, fit / relevance, authority / no-budget-holder,
   trust / risk, and "no need." Add categories the user's motion actually hits.
3. For **each objection**, capture three things:
   - the **objection** as prospects actually phrase it (mirror their words),
   - the **reframe** — how to reframe the concern without arguing,
   - the **proof** — the specific evidence that counters it (a case study, a
     positioning pillar, an offering fact, a customer outcome).
   Cross-link to `offerings.md` and `case-studies/` concepts where the proof lives.
4. **Apply Source Fidelity to any numbers in proof.** Every metric, percentage,
   or dollar figure must carry a source (user input, a shared file, or a cited
   `WebSearch`). Missing a number → mark `[UNKNOWN — needs input]` and ask; never
   insert a plausible default. Illustrative sample lines get the
   `Example — illustrative, not benchmarks.` prefix.
5. **Single-writer discipline:** only Ricky writes this file. Do not edit
   `positioning.md`, `offerings.md`, or any other agent's concept — read them,
   link to them.
6. Write the file with OKF concept frontmatter (see `docs/company-context.md`):
   ```yaml
   ---
   type: Playbook
   title: Objection Library
   description: <one sentence>
   tags: [company-context, sales, objections]
   timestamp: <ISO 8601>
   owner: reply-objection-handler
   last_updated: <YYYY-MM-DD>
   last_updated_by: reply-objection-handler
   schema_version: 2
   ---
   Status: <Bootstrapped | In progress | Stable | Stale (needs refresh)>
   ```
   Then update the bundle `index.md` entry and append an `## <date>` line to
   `log.md` for the creation/update.
</process>
