# Maintain the Sequence Playbook

<instructions>
Maintain the canonical, reusable cadence playbook. It is a single OKF `Playbook`
concept at `{output_folder}/company-context/playbooks/sequences.md`: reusable
cadence templates and channel rules — touch counts, spacing, and channel mix by
persona / tier. Casey is the **single writer** of this file. Follow the OKF
frontmatter schema in `docs/company-context.md` exactly.
</instructions>

<process>
1. Read the context that exists: `brand-voice.md` (to keep cadence and channel
   choices on-voice) and the current `playbooks/sequences.md`. Note what's absent
   and continue. Never rewrite `brand-voice.md`.
2. Capture reusable **cadence templates** — named, reusable shapes (e.g. a
   high-touch enterprise cadence, a lighter mid-market cadence). For each template
   record: total **touch count**, the **step-by-step channel + spacing** (Day N
   per step), and which **persona / tier** it fits.
3. Capture **channel rules** that apply across templates: channel mix by persona /
   tier, when to lead on email vs LinkedIn vs call, per-channel etiquette and
   limits, and the human-in-the-loop send-gate rule (recommend, never auto-send).
4. Keep templates keyed to reuse: a template should be pickable by persona and
   tier so a per-account `sequence-plan.md` can instantiate it and tailor spacing.
5. Do **not** embed open-/reply-rate benchmarks. Any illustrative numbers must be
   prefixed `Example — illustrative, not benchmarks.` Real numbers need a source
   cited inline; otherwise mark `[UNKNOWN — needs input]`.
6. Write the file with OKF frontmatter: `type: Playbook`,
   `owner: outreach-sequence-planner`, `schema_version: 2`, a `Status:` line, and
   the other required fields per `docs/company-context.md`. Use bundle-relative
   links (e.g. to `brand-voice.md` and `icp.md` personas). Keep single-writer
   discipline.
7. Append the change to the bundle-root `log.md`.
8. In the protocol, write `v{n}.md` describing the changes, set `state.yaml`
   `status: in-review`, and notify the orchestrator.
</process>
