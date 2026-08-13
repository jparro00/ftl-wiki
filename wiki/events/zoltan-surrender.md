---
id: event-zoltan-surrender
type: event
event_name: ZOLTAN_SURRENDER
sectors: []
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [surrender, aftermath, orphan, unreachable, zoltan]
---

# Zoltan surrender — `ZOLTAN_SURRENDER`

## Summary
A fully written Zoltan surrender offer — six flavour strings, two choices, a payout — that
**no ship in the game invokes**. Every other species-specific surrender event is wired to a
hull's `<surrender>` block; this one is not. It is complete shipped content that never
fires.

## Trigger & Where It Appears
- **Unreachable.** `ZOLTAN_SURRENDER` appears in `raw/gamedata/` only inside
  `events_zoltan.xml` — its own `<event>` definition, the `<textList>` it loads, and the
  matching strings in `text_events.xml`. A search of every `.xml` finds **no
  `<surrender load="ZOLTAN_SURRENDER"/>`, no `<event load=…>`, and no `sector_data.xml`
  allocation** ([[source-events-zoltan]], [[source-events-ships]]).
- This is the positive evidence [[concept-sector-event-allocation]] asks for: not merely
  "no sector allocation", but no reference of any kind anywhere in the data.
- For contrast, the surrender events that *do* fire are all named in a hull block —
  `PIRATE` → [[event-pirate-surrender]], `ROCK_SHIP` → [[event-rock-ship-surrender]],
  `LANIUS_SHIP` → [[event-lanius-surrender]], `JELLY` → [[event-slug-surrender]]. The
  Zoltan hulls (`ZOLTAN_SHIP`, `ZOLTAN_REFUGEE`, …) carry no `<surrender>` element at all;
  the Zoltan **pirate** hull `ZOLTAN_PIRATE` loads `PIRATE_SURRENDER` instead.
- Not a stub: six distinct in-character strings, both choices wired, a reward attached.
- No Fandom page documents it, which is consistent with it never appearing in play.

## Text
`<text load="ZOLTAN_SURRENDER"/>` — a 12-entry text list built from **six** distinct
strings, each listed twice (the XML comments the second block *"duplicate for now — add
more?"*), so **1/6 each** assuming uniform selection across list entries
([[concept-event-list-weighting]], [[source-events-zoltan]],
[[source-text-events-xml]]):

> "Yes, yes, you've demonstrated your species' capacity for violence quite extensively,
> well done. If we reward your efforts will you bother someone else?"

> The enemy ship hails; the vidscreen shows their bridge showered in sparks from
> malfunctioning equipment - it's safe to assume they're trying to surrender. Accept their
> offer?

> Communications report that the Zoltan are broadcasting on all frequencies. The captain
> appears on screen and says, "Yes, I am not surprised, your species hardly looks
> enlightened. Fine. Take what you wish."

> The Zoltan captain hails and mutters something about the border patrol force catching up
> with you someday; you're more interested in his offer of surrender.

> "We assumed that your species' intelligence was directly proportional to your brute
> strength. We yield."

> "You have bested us. If only your species' efforts were put to use improving the galaxy
> rather than your military might."

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Accept their offer. | — | `<ship hostile="false"/>` — the fight ends — plus `<autoReward level="RANDOM">stuff</autoReward>`. | 100% |
| 2 | We will not accept surrender! | — | Empty `<event/>`; the fight continues. | 100% |

Structurally identical to [[event-pirate-surrender]], [[event-rock-ship-surrender]] and
[[event-lanius-surrender]] — the same two choices, the same `RANDOM` `stuff` payout. Only
the prose differs.

## Blue Options
None.

## Rewards & Risks
Not applicable in play. Had it been wired up it would pay one `RANDOM`-level `stuff`
bundle in exchange for forgoing the hull's destruction rewards.

## Strategy Notes
None — the event cannot occur. Do not expect a Zoltan warship to offer surrender: the
Zoltan hulls have no `<surrender>` block, so [[event-zoltan-fight]] and its variants are
fights to the finish.

## Related
- [[event-pirate-surrender]], [[event-rock-ship-surrender]], [[event-lanius-surrender]],
  [[event-slug-surrender]] — the wired-up equivalents this one mirrors
- [[event-zoltan-fight]] — the Zoltan fight that would have used it
- [[entity-zoltan]] — the faction
- [[concept-surrender-offers]] — how `<surrender>` blocks are declared
- [[concept-sector-event-allocation]] — the evidence bar for calling something unreachable

## Open Questions
- [ ] Was a `<surrender>` block on `ZOLTAN_SHIP` removed, or never added? Nothing in the
      files records an intent either way.
- [ ] Does the AE build's engine call any surrender event by name rather than by ship
      reference? If so this could still fire.

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
