# Length Adapt (LE)

<instructions>
Produce 5 / 15 / 45-minute variants of an existing storyline from one
hierarchy. Same anchors, different depth.
</instructions>

<process>

## 1. Intake

Confirm:

- The storyline file to adapt (path under `work/{id}/`).
- The target length(s) — one or several of 5, 15, 30, 45+ minutes.

If the source storyline is incomplete (missing anchors or
explanations), stop and refer the user to BP or BD first.

## 2. Apply the length tier

| Length     | Act I | Act II depth                                                    | Act III |
|------------|-------|-----------------------------------------------------------------|---------|
| 5 minutes  | All 5 slides, condensed | Anchors only (3 slides, no Explanations)             | 1 slide |
| 15 minutes | All 5 slides            | Anchors + Explanations (3×3 = 9 slides)              | 2 slides |
| 30 minutes | All 5 slides            | Anchors + Explanations + 1–2 Details per Explanation | 2 slides |
| 45+ min    | All 5 slides + extended Hook | Full 3×3×3 (Anchors + Explanations + Details)   | 3 slides |

## 3. Produce per-variant file

For each requested length, write a sibling file:

```
work/{presentation-id}/v{n}-5min.md
work/{presentation-id}/v{n}-15min.md
work/{presentation-id}/v{n}-45min.md
```

Each variant inherits:

- The same audience, desired decision, A↔B framing
- The same anchors in the same priority order
- The same source-of-truth citations

Each variant differs by:

- Slide count
- Depth tier (Explanations / Details included or omitted)
- Act III pacing (single decision slide vs. extended Q&A setup)

## 4. Cross-variant consistency check

Before handing back, verify:

- Anchors appear in the same order across variants.
- The 5-minute version's Act III decision is identical to the
  45-minute version's Act III decision.
- No variant introduces a new source citation the others don't have.

## 5. Hand-back

List the files produced, their slide counts, and the depth tier of
each. Suggest a next step: "Use the 5-min as the elevator version,
the 15-min for the kickoff, the 45-min for the deep-dive."

</process>
