# Headline Drill (HD)

<instructions>
Rewrite weak slide headlines as complete declarative sentences in
active voice. Diagnose what's wrong before rewriting.
</instructions>

<process>

## 1. Intake

Ask the user to paste the headlines (one per line, or as a numbered
list). If they paste a deck outline, extract the headline-equivalent
text per slide and confirm the list with them before proceeding.

## 2. Diagnose each headline (one line per finding)

For every headline, name the issue using one of these tags:

- `FRAGMENT` — not a complete sentence (label or noun phrase)
- `PASSIVE` — passive voice
- `VAGUE` — no specific claim; reader can't disagree
- `OVERLOADED` — two or more ideas crammed into one slide
- `NO-AUDIENCE` — written about the presenter / product, not the audience
- `JARGON` — terminology audience won't use
- `OK` — passes all checks; no rewrite needed

If a headline already passes, mark `OK` and move on. Don't rewrite
for style.

## 3. Rewrite

For each non-OK headline, produce a before/after pair:

```
Before: "Q3 Revenue Performance"
Tag:    FRAGMENT, VAGUE
After:  "Revenue grew 18% in Q3, driven by enterprise renewals."

Before: "Our solution was selected by 12 customers"
Tag:    PASSIVE, NO-AUDIENCE
After:  "Twelve customers chose us in Q3 over Workday and Salesforce."
```

## 4. Headline ground rules (apply when rewriting)

- Complete declarative sentence
- Active voice (subject does the verb)
- Ideally one line, under ~15 words
- Specific to one idea per slide — if the headline has two claims,
  split it across two slides and tag the original `OVERLOADED`
- Conversational, as if spoken to the audience
- Pass the `brand-voice.md` don't-list
- For numeric claims, use the figure the user provided. If they
  didn't provide one, flag `[NEEDS NUMBER]` rather than inventing.

## 5. Output

If operating under a brief, write to `v{n}.md` under the working
folder. Otherwise hand back as the table above and ask whether to
save with SM.

</process>
