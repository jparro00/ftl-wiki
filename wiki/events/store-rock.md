---
id: event-store-rock
type: event
event_name: STORE_ROCK
sectors: [[[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
beacon_type: store
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [store, rock, guaranteed]
---

# Store (Rock) — `STORE_ROCK`

## Summary
The Rock-flavoured store beacon. It opens a store and nothing else; the flavour text
exists to explain why anyone in Rock space is willing to trade with you at all. Exactly
**2** are allocated per Rock sector ([[source-sector-data-xml]]).

## Trigger & Where It Appears
- Sectors: [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]
- Allocation: `<event name="STORE_ROCK" min="2" max="2"/>` in both Rock sector
  definitions — a fixed 2, not a range ([[source-sector-data-xml]], per
  `raw/gamedata/sector_data.xml`)
- Beacon: **store** ([[source-fandom-store-rock]] marks `store=true`, `LRSmap=noship`)
- Not `unique` — it appears twice per sector by design ([[source-events-rock]])

## Text
Varies — `<text load="STORE_ROCK"/>` over a five-entry `textList`
([[source-events-rock]]). The five framings are: a Rock ship back from a diplomatic
mission, a Rock trading post offloading its last stock, an opportunistic Mantis crew,
a Zoltan trading post in an abandoned capital ship, and a stranded Federation trader.
[[source-fandom-store-rock]] transcribes all five.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(no choices; continue)_ | — | A store opens. | 100% |

The event body is `<text load="STORE_ROCK"/>` plus a bare `<store/>` tag
([[source-events-rock]]). The store's inventory is not defined in this event.

## Rewards & Risks
- No scrap, fuel or items are granted by the event itself. What you can buy is the
  store's own roll, which this event does not constrain.
- No risk — the beacon is never hostile.

> ⚠️ **CONTRADICTION (minor):** the Fandom flavour text renders the fifth variant with
> the ellipsis `"You're Federation?! We- we weren't sure..."`; the sector's stock and
> pricing are described nowhere in either source. Not a substantive conflict, just noted
> so the store's contents are not assumed to be Rock-themed — nothing in
> `raw/gamedata/events_rock.xml` biases the inventory ([[source-events-rock]]).

## Strategy Notes
- Two guaranteed stores per Rock sector is the same allocation as most faction sectors
  and is the main reason a Rock sector is survivable despite the 6–8 guaranteed hostile
  beacons ([[source-sector-data-xml]]).
- Rock sectors also roll `rock` crew at rarity 1 in their `rarityList`
  ([[source-sector-data-xml]]) — relevant if you are shopping for a boarder.

## Related
- [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]
- [[event-empty-beacon-rock]], [[event-start-beacon-rock]]
- [[concept-stores]] — how store beacons stock and price

## Open Questions
- [ ] Does `STORE_ROCK` bias its inventory toward Rock-flavoured blueprints, or is it the
      generic store roll? Nothing in the event says.

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-store-rock]] (per raw/wiki/store-rock.md)
