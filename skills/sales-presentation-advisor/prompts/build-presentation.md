# Build a Presentation Storyline (BP)

<instructions>
Produce a full presentation storyline by inheriting source artifacts
and mapping them to the three-act structure. Source-of-truth strict:
never fabricate; flag missing slots explicitly.
</instructions>

<process>

## 1. Intake (ask, up to three questions in a single numbered list)

Before reading anything, confirm:

1. **Audience** — who is in the room? Title, seniority, decision-making
   role. (BBP requires casting them as protagonist; without this, stop.)
2. **Desired decision / outcome** — what must the audience do, decide,
   or believe by the end? (Without this, there is no Act III.)
3. **Length** — 5 / 15 / 30 / 45+ minutes.

Then ask one more, separately:

4. **Output depth** — pick one:
   - **L1 — Storyline + headlines only** (act structure + one
     complete-sentence headline per slide)
   - **L2 — L1 + speaker notes** (2–4 lines of spoken-word notes per slide)
   - **L3 — L2 + slide bullet content** (supporting bullets under
     each headline; Pierce will note that BBP argues against bullets
     and treat them as backup, not replacement for the headline)

Then ask one more, separately:

5. **Sources** — either:
   - A list of paths to source artifacts (positioning, launch
     narrative, ICP, messaging pillars, competitive teardown, case
     studies, prior decks), OR
   - "Pull what's relevant" — Pierce inventories `company-context/`
     and recent `work/{id}/` outputs and proposes a source list back
     for confirmation before building.

## 2. Source inventory

For each available artifact, read it and note which BBP slot it can
fill. Typical mapping:

| BBP slot                | Likely source                                                            |
|-------------------------|--------------------------------------------------------------------------|
| Act I Hook (setting)    | Market trend / "why now" from positioning, launch narrative, or analyst data |
| Act I Relevance (role)  | `icp.md` segment + persona; the audience's stake                        |
| Act I Challenge (A)     | `icp.md` pains, competitive teardown gaps, customer-interview themes   |
| Act I Desire (B)        | `positioning.md` value pyramid, key benefit, outcome statements        |
| Act I Map (CTA preview) | Three anchors named upfront                                             |
| Act II Anchors (×3)     | Messaging pillars (Mona Message), launch narrative pillars (Lana Launch) |
| Act II Explanations     | Proof points behind each pillar                                         |
| Act II Details          | Case studies (Cara Customer), customer quotes, competitive proof, data |
| Act III Resolution      | Restated CTA tied to audience's desired decision; stakes named         |

If "pull what's relevant" was chosen, present the inventory back to the
user and ask: "Use these N sources? Add anything?" before continuing.

## 3. Build the storyline

Write into `{output_folder}/work/{presentation-id}/v{n}.md` where
`{presentation-id}` is a slug like `2026-q3-aws-launch-keynote` or
`2026-05-steering-cc-migration-pitch`.

Structure:

```
---
presentation_id: <slug>
audience: <one line>
desired_decision: <one line>
length: <minutes>
depth: <L1 | L2 | L3>
sources_used: [list of paths]
schema_version: 1
---

# <Presentation working title>

## Act I — Setup (≈first 5 slides, ~20% of time budget)

### Slide 1 — Hook
**Headline:** <complete declarative sentence in active voice>
<L2: 2–4 lines of speaker notes>
<L3: supporting bullets, max 3, each ≤10 words>

### Slide 2 — Relevance
…

### Slide 3 — Challenge (Point A)
…

### Slide 4 — Desire (Point B)
…

### Slide 5 — Map (preview of three anchors)
…

## Act II — Develop (body, ~70% of time budget)

### Anchor 1: <complete-sentence headline>
*Source: <artifact path or `[MISSING — needs: X]`>*

  - Explanation 1.1: …
  - Explanation 1.2: …
  - Explanation 1.3: …

(Repeat for Anchor 2, Anchor 3. Detail tier — Explanations and Details — adapts to length per LE rules.)

## Act III — Resolve (≈last 2–3 slides, ~10% of time budget)

### Slide — Decision moment
**Headline:** <restate the desired decision as a sentence the audience
hears as a call>

### Slide — Next step
**Headline:** <concrete next action and who owns it>

## Sources used

- <path>: filled <slot(s)>
- <path>: filled <slot(s)>

## Missing slots

- <slot>: <what's needed and from whom>
```

## 4. Source Fidelity hard rules

- A slot with no source → write `[MISSING — needs: <what>]` as the
  headline body, never invent.
- Numbers, customer names, competitor claims must trace to a source
  file or a `WebSearch` citation in `Sources used`. No exceptions.
- If the user asks Pierce to "just fill it in", refuse and ask which
  artifact to read or which orchestrator to commission.

## 5. Headline rules (apply to every headline written)

- Complete declarative sentence (not a fragment or label)
- Active voice
- Ideally one line, under ~15 words
- Specific to one idea per slide
- Conversational, as if spoken to the audience
- Pass the `brand-voice.md` don't-list

Bad: "Q3 Revenue" — fragment, no claim.
Better: "Revenue grew 18% in Q3, driven by enterprise renewals."

## 6. Length tiers (apply automatically per `length:` field)

- 5-minute  → Act I + 3 anchors only (no Explanations, no Details)
- 15-minute → + Explanations per anchor (3 each)
- 30-minute → + selected Details (1–2 per Explanation)
- 45+-minute → full 3×3×3 Details

## 7. Hand-back

Write `v{n}.md`. Update `state.yaml` if operating under a brief. Tell
the user:

- File written.
- Anchor count and length tier produced.
- Missing slots count and what each one needs.
- Suggested next step: "Send the v1 to the audience-sample reader for a
  reaction read, OR commission missing artifacts from <orchestrator>,
  OR ask me to run TX (tension check) on Act I."

</process>
