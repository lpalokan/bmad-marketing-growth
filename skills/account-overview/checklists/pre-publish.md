# Pre-publish gate

Run item by item before an Account Executive sees the card. Any failure blocks
publication. The orchestrator owns this gate and no agent passes its own work.

## The story

- [ ] The band carries all five steps in `reference/story-spec.md`, in order.
- [ ] It is a narrative with a beginning, a change and a consequence. It is not a
      category description of the industry.
- [ ] Step 5 reads as an insight. Read it out loud. If it sounds like an
      advertisement, it fails.
- [ ] No product pitch, no feature list, no "why AI" framing anywhere on the card.
- [ ] The card never argues the account's controls are bad. It argues their
      environment is changing faster than their evidence model.
- [ ] The value is not framed as headcount reduction or as efficiency for its own
      sake, unless the account's own strategy uses that language.

## The compelling event

- [ ] Dated with a specific date or month.
- [ ] A `KNOW` entry in `account.md` with a working link.
- [ ] Structural. It adds ground that has to be controlled, evidenced, staffed or
      reported.
- [ ] Connected. It bears on the thing in step 3 that has not changed.
- [ ] Where no qualifying event exists, `compelling_event: none` is set, the badge
      is absent, and the absence was stated to the user. Nothing was manufactured
      to fill the slot.

## Sourcing

- [ ] Every number on the card is in `account.md` with a link behind it.
- [ ] Every figure carries its comparative.
- [ ] Every figure has been traced to the entity it belongs to, rather than to a
      similarly named company.
- [ ] No invented number, quote, person, title, customer or technology detail.
- [ ] No vendor name, core platform or integration path is asserted without a
      public source.
- [ ] Every unverified technical assumption carries an `Unconfirmed, gap` flag, or
      it is off the card.
- [ ] No live or active enforcement action is named. Regulatory pressure, where
      real and sourced, appears as general industry framing.
- [ ] Conflicting metric definitions are both shown and flagged in the sources
      line rather than silently resolved.
- [ ] Our own proof points are presented as site claims, with `[PROOF NEEDED]`
      left visible where a named reference would carry the argument.

## People

- [ ] Every contact was verified live this session.
- [ ] Enrichment-derived people are corroborated against a public source before
      appearing.
- [ ] Each contact carries the thread they own: cost, coverage, risk, compliance
      or technology.
- [ ] No personal contact detail appears on the card.

## Fit

- [ ] The renderer reported no slot over its cap, or every warning it reported was
      fixed in the copy.
- [ ] Objectives and challenges together are seven items or fewer.
- [ ] The plain-terms column has exactly three paragraphs.
- [ ] The out-of-scope box has two or three items.
- [ ] Each plain-terms paragraph carries one concrete detail and could not be
      pasted into another account's card unchanged.
- [ ] The budget was met by cutting whole items. Nothing reads as compressed
      fragments or dropped articles.
- [ ] Nothing the reader already met is restated to introduce its consequence.

## Emphasis and hierarchy

- [ ] No bold in body text. The only bold is the column subheads, the plain-terms
      headlines and the out-of-scope headings, all of which are headings.
- [ ] Numbers carry weight through the accent colour and the size step, applied by
      the renderer. None was bolded by hand in the source.
- [ ] No italics anywhere.
- [ ] Headings carry no terminal period.

## Style

- [ ] Zero em dashes and zero en dashes.
- [ ] Zero "X, not Y" constructions.
- [ ] No mid-sentence interrupter splits a subject from its verb.
- [ ] Jargon is expanded on first use, or it is cut.
- [ ] At most one analogy carries the insight, and it is businesslike.
- [ ] The prose was read, not scored. Nobody has claimed a character count as
      proof of anything.

## Brand and voice

Neither is required, because neither ships with this module. Where the company
has them, a card that skipped them is a draft. Where it has none, tick the
fallback line instead and say so once.

- [ ] The company's tone-of-voice skill was run against the copy and its findings
      applied — or there is none, and the copy was held to
      `../account-dossier/reference/house-style.md` instead.
- [ ] The company's brand-compliance skill was run against the rendered file — or
      there is none, and the render was checked against `reference/design-spec.md`
      by eye.
- [ ] Every Critical and Should-fix brand finding is resolved.
- [ ] The intended brand pack was used, where the company has one. The renderer
      printed it and it is not `neutral placeholder`. A card that reached a seller
      in the placeholder
      palette fails this gate.
- [ ] Two colours only. The neutral ramp is structure. There is no third hue.
- [ ] Where the pack carries a gradient, it appears only in the top rule and the
      rings behind the story band. It is behind no text and fills no large area.
- [ ] One typeface throughout, from the brand stack. No serif anywhere.
- [ ] No stock photography, no external-asset icons, no humanoid or robot imagery,
      no drop shadows.

## The render

- [ ] The card was opened and viewed at 1280 by 720 before it was shown to anyone.
- [ ] Nothing overflows the canvas and nothing scrolls.
- [ ] Every number is legible at full size and reads as a figure rather than as a
      link.
- [ ] The eyebrow reads `Seller briefing · Internal · Not for customer` and is
      present.

## Third parties

- [ ] No company other than the account is named, unless materially inside the
      account's own situation.
- [ ] Where one is named, the relationship is stated plainly.
- [ ] `not_to_be_confused_with` exists only in frontmatter and does not render.

## Safety

- [ ] No existing briefing was overwritten. A dated file was written and
      `supersedes:` is set.
- [ ] No other account's render was overwritten by the build command.
- [ ] Findings were written into the shared `account.md`, so the work survives
      this card.
- [ ] The card is internal. It has not been sent, forwarded or shared with the
      account, and nothing has been written back to any external system.
