# Third parties in a dossier

**A dossier covers one account.**

## The default: no other companies

Peers, competitors, neighbours in the same market and other companies'
enforcement actions are not argument fuel. Keep them out.

Two reasons, and the second is the one that gets underestimated.

**It confuses the reader.** An AE scanning quickly cannot always tell whether a
named company is part of the account, owned by it, or unrelated. In markets where
names collide the confusion is close to guaranteed.

**It reads as fear-selling.** Building a case on a rival's bad week tells the
buyer exactly what we would do with theirs. It also invites the obvious reply that
we do not know what happened inside that company.

This was learned the hard way. A dossier used another bank's supervisory penalty
six times as evidence that a risk was real. The argument was sound and the
inclusion was wrong. Rebuilt on the account's own facts, it got shorter and more
specific.

## The narrow exception

Another company may be named when it is **materially inside the account's own
situation**. In practice that means:

- An acquisition target or acquirer in a live transaction.
- A parent, subsidiary or joint venture.
- A named partner in a published agreement.
- A supplier whose failure is part of the account's own public record.

Even then:

- Name it only where it changes what the account has to do.
- Say plainly what the relationship is, so nobody has to guess.
- **It never appears in outbound copy.** Not in a first-touch message, not in a
  forward note, not in a LinkedIn note. Commentary on a third party from a vendor
  is at best awkward and, during a live transaction, reads as leverage.
- Add an explicit instruction to section 7, "Before you send", stating that.

## Confusable names

Where the account can be mistaken for another company, record the disambiguation
in **frontmatter only**:

```yaml
not_to_be_confused_with: "Acme Holdings Oyj is a separate listed company and is NOT this account"
```

It is internal metadata for whoever picks up the file. It must never render into
the reader's view. Printing the other name under the title plants exactly the
confusion the field exists to prevent. The HTML renderer deliberately ignores
this field.

## Our own competitors

Alternatives the buyer will weigh belong in the committee section as "what they
will weigh instead of us". Keep it factual, name categories rather than
disparaging named vendors, and state honestly where the alternative is genuinely
the sensible choice. That section is for the AE's preparation and is not a
battlecard.

## Case studies and comparables

Never attribute a peer's detail to this account, and never present an unnamed
comparable as though it were one. If we cannot name the reference, say so and
mark `[PROOF NEEDED]`.
