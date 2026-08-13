---
id: event-store-rebel
type: event
event_name: STORE_REBEL
sectors: [[[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]]]
beacon_type: store
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [rebel, structural, store, no-choice, flavour-only]
---

# Store (Rebel) — `STORE_REBEL`

## Summary
The Rebel sector's store beacon. Three lines of flavour explaining why a Rebel-aligned
station will trade with the Federation's most wanted ship, then a `<store/>` tag. No
choices, no risk, no variation in what you get — the store contents come from the store
generator, not from this event.

## Trigger & Where It Appears
- Sectors: [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]].
- **Not in any event list.** Allocated directly by the sector definitions as
  `<event name="STORE_REBEL" min="1" max="2"/>` — **1–2 stores per Rebel sector**, in both
  `REBEL_SECTOR` and `REBEL_SECTOR_MINIBOSS` ([[source-sector-data-xml]]).
- Beacon: store. Long-range scanners show **no ship**
  ([[source-fandom-store-rebel]]).
- Not unique.
- Filed under the `STRUCTURE!!! / Required structural` header in `events_rebel.xml`
  ([[source-events-rebel]]).

## Text
Drawn from the `STORE_REBEL` text list — **three variants**
([[source-events-rebel]], [[source-text-events-xml]]):

> You discover a re-supply station used by Rebels and civilians alike. You transmit your
> fake ship identification and for once, they don't seem to recognize your ship. You try to
> assume the air of a local as you prepare to dock.

> You arrive at a small space station that is putting out wide-band broadcasts on
> black-market channels. You doubt they would turn away any business, regardless of
> allegiances.

> You receive generic advertisements from a nearby public ship-yard. It seems they are
> willing to work on any ship, not only those of Rebel hue.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event body is `<text load="STORE_REBEL"/>` plus `<store/>`)* | — | A store opens. | 100% |

The event carries no `autoReward`, no `<ship>`, and no modifiers — nothing about the Rebel
setting changes what the store stocks or charges ([[source-events-rebel]]).

## Blue Options
None.

## Rewards & Risks
Neither, beyond the store itself. This is the sector's shopping beacon.

## Strategy Notes
- 1–2 guaranteed stores per Rebel sector is the same allocation most sector types get, so
  Rebel space is not store-poor despite being hostile.
- Worth noting for routing: the Rebel Stronghold (`REBEL_SECTOR_MINIBOSS`) has the same
  store allocation *and* the [[event-rebel-shipyard]] miniboss, so it is not a sector you
  enter unequipped by necessity ([[source-sector-data-xml]]).

## Related
- [[event-empty-beacon-rebel]], [[event-start-beacon-rebel]] — the other structural entries
- [[event-store-engi]], [[event-store-mantis]], [[event-store-rock]],
  [[event-store-zoltan]], [[event-store-crystal]] — the sibling `STORE_*` events
- [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]]
- [[concept-stores]]

## Open Questions
- [ ] Whether the three text variants are equally weighted.
- [ ] Whether Rebel-sector stores differ in stock rarity from other sectors (nothing in this
      event says so; that would live in the store generator, not here).

## Sources
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-store-rebel]] (per `raw/wiki/store-rebel.md`)
