# Maintain the Message-Framework Playbook

<instructions>
Define or tune the reusable message-framework playbook the whole suite writes
against: `{output_folder}/company-context/playbooks/message-frameworks.md`. This
is a Google OKF concept of `type: Playbook`, owned by contact-approach-writer —
Aria is its single writer; every other agent reads it. This is the one
`company-context/` file Aria may write.
</instructions>

<process>
1. Read the context that exists: `brand-voice.md` (voice the frameworks must fit)
   and `positioning.md` (the pillars proof lines lean on). If a
   `message-frameworks.md` already exists, read it and tune in place rather than
   rewriting from scratch — preserve what still holds.

2. Maintain three parts of the playbook:
   - **Proven message structures** — PAS (Problem → Agitate → Solve) and
     Before-After-Bridge, each with when to reach for it and its slot order.
   - **Opener patterns** — company-specific signal openers keyed to signal types
     (funding, leadership hire, migration, regulatory deadline, expansion), so a
     writer can pick the pattern that matches the account's why-now.
   - **Proof patterns** — the named-comparable + specific-metric structure (the
     biggest reply-rate lever), with how to phrase a sourced comparable in the
     buyer's vertical and how to tie the metric to the buyer's owned metric.

3. Keep the playbook framework-only: it holds structures and patterns, never a
   specific account's numbers. Any illustrative figure inside a sample pattern is
   prefixed `Example — illustrative, not benchmarks.` Do not invent benchmark
   reply rates or customer results (Source Fidelity); ask if a claimed number has
   no basis.

4. Write `message-frameworks.md` with the frontmatter from
   `docs/company-context.md`:
   ```yaml
   ---
   type: Playbook
   title: Message Framework Playbook
   description: <one sentence>
   tags: [company-context, playbook, messaging, outreach]
   timestamp: <ISO 8601>
   owner: contact-approach-writer
   last_updated: <YYYY-MM-DD>
   last_updated_by: contact-approach-writer
   schema_version: 2
   ---
   Status: <Bootstrapped | In progress | Stable | Stale (needs refresh)>
   ```
   Link out to `brand-voice.md` and `positioning.md` with bundle-relative
   Markdown links.

5. Because this is a `company-context/` write, append the change to the bundle
   `log.md` (newest first) and update the root `index.md` entry if the concept is
   new. This is the single exception to Aria's read-only stance on the bundle.
</process>
</content>
