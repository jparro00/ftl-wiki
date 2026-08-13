---
id: event-store-pirate
type: event
event_name: STORE_PIRATE
sectors: [[[sector-pirate-controlled-sector]]]
beacon_type: store
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [store, pirate, guaranteed]
---

# Store (Pirate) — `STORE_PIRATE`

## Summary
The Pirate-flavoured store beacon. It opens a store and nothing else; the four flavour
variants exist to explain why anyone in pirate space is willing to trade with you rather
than shoot you. 1–2 are allocated per Pirate sector ([[source-sector-data-xml]]).

## Trigger & Where It Appears
- Sector: [[sector-pirate-controlled-sector]]
- Allocation: `<event name="STORE_PIRATE" min="1" max="2"/>` in the `PIRATE_SECTOR`
  definition ([[source-sector-data-xml]], per `raw/gamedata/sector_data.xml`)
- Beacon: **store** — [[source-fandom-store-pirate]] marks `store=true`, `LRSmap=noship`
  (long-range scanners show no ship at the beacon)
- Not `unique` — the event carries no `unique` attribute, and up to 2 are placed
  ([[source-events-pirate]])

## Text
Varies — `<text load="STORE_PIRATE"/>` over a four-entry `textList`
([[source-events-pirate]]). All four, per [[source-text-events-xml]]:

> A few small ships are visible on the vidscreen, and you almost activate weapons
> targeting. However, sensors indicate they are simply honest merchants. The pirates must
> be making you jumpy. You message them asking about their wares.

> You detect a hub of activity nearby. A large corporation has set up a trade depot and
> has a number of well armed ships patrolling. This appears to be a relatively safe place
> to get repairs.

> You receive a wide-band automated message, "Welcome to our humble trade depot and
> shipyard! All are welcome, but try any funny business and our 152 automated turret
> satellites will tear your ship to shreds!"

> A well armed transport ship and a squadron of fighters are in orbit nearby. You are wary
> of their trustworthiness but beggars can't be choosers.

[[source-fandom-store-pirate]] transcribes the same four.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(no choices; continue)_ | — | A store opens. | 100% |

The event body is `<text load="STORE_PIRATE"/>` plus a bare `<store/>` tag
([[source-events-pirate]]). Nothing in the event constrains the store's inventory.

## Rewards & Risks
- The event itself grants no scrap, fuel or items. What you can buy is the store's own
  roll.
- No risk — despite the sector, the beacon is never hostile and no variant leads to a
  fight.

## Strategy Notes
- 1–2 guaranteed stores is the low end of the sector range (Rock sectors get a fixed 2),
  so a Pirate sector can be a bad place to be counting on repairs
  ([[source-sector-data-xml]]).

## Related
- [[sector-pirate-controlled-sector]]
- [[event-start-beacon-pirate]], [[event-empty-beacon-pirate]] — the other structural
  Pirate beacons
- [[event-pirate-briber]] — one of its win outcomes also opens a store
- [[concept-stores]] — how store beacons stock and price

## Open Questions
- [ ] Does `STORE_PIRATE` bias its inventory in any way? Nothing in the event says.

## Sources
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-store-pirate]] (per raw/wiki/store-pirate.md)
