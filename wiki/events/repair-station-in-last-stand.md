---
id: event-repair-station-in-last-stand
type: event
event_name: BOSS_REPAIR_STATION
sectors: [[[sector-the-last-stand]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [hull-repair, free-resources, no-choice, endgame, last-stand, federation]
---

# Repair station in Last Stand — `BOSS_REPAIR_STATION`

## Summary
The Federation's parting gift: three guaranteed beacons in [[sector-the-last-stand]] that
fully repair your ship and hand over missiles, fuel, drone parts and scrap for free, with
no choice to make and nothing to go wrong. Between them these are the largest unconditional
resource injection in the game, and they exist to make the three-phase Flagship fight
survivable.

## Trigger & Where It Appears
- Sector: [[sector-the-last-stand]] (`FINAL`) only.
- Allocation: `<event name="BOSS_REPAIR_STATION" min="3" max="3"/>` — **exactly three per
  run**, and it is referenced directly as an event, not through a list
  ([[source-sector-data-xml]]).
- Beacon: shown as a repair beacon on the map ([[source-fandom-repair-station-in-last-stand]]).
- The XML comment: *"the various stations that heal you around the map."*

## Text
Drawn from the `BOSS_REPAIR_STATION` text list: five distinct strings, each listed once, so
1/5 apiece assuming uniform selection across list entries ([[source-events-boss]],
[[source-text-events-xml]]).

> There is a a mobile ship construction platform stationed at this beacon. After a brief
> exchange they give you clearance to receive emergency repairs and military supplies.

> An Engi civilian ship-yard has been converted into a military refueling station. They
> offer you the chance to patch up your ship and refresh some supplies.

> A trade station was abandoned nearby. Some Federation engineers repurposed their shipyard
> to perform military repairs. They offer to help fix your ship.

The doubled "a a" in the first string is in the shipped data, not a transcription slip;
[[source-fandom-repair-station-in-last-stand]] flags the same typo.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event has no `<choice>` elements)* | — | `<damage amount="-15"/>` → **+15 hull**; `<repair/>` → systems repaired; **+4 missiles, +5 fuel, +5 drone parts, +22–44 scrap**. | 100% |

The reward is a literal `<item_modify>` block, not an `autoReward` level, so the numbers
are exact rather than tier-based ([[source-events-boss]]):

```xml
<damage amount="-15"/>
<repair/>
<item_modify>
    <item type="missiles" min="4" max="4"/>
    <item type="fuel"     min="5" max="5"/>
    <item type="drones"   min="5" max="5"/>
    <item type="scrap"    min="22" max="44"/>
</item_modify>
```

[[source-fandom-repair-station-in-last-stand]] reports 15 repairs, 22–44 scrap, 5 fuel,
4 missiles, 5 drone parts — every figure matches the files. No contradiction.

## Blue Options
None.

## Rewards & Risks
- Guaranteed: 15 hull, a `<repair/>` pass, 4 missiles, 5 fuel, 5 drone parts, 22–44 scrap.
- Across the three guaranteed beacons that is up to 45 hull, 12 missiles, 15 fuel,
  15 drone parts and 66–132 scrap, if you visit all three.
- No risk of any kind — the event has no ship, no choice and no negative branch.

## Strategy Notes
- The `<repair/>` tag repairs damaged **systems** in addition to the hull points from
  `damage amount="-15"`; they are two separate effects in the XML
  ([[source-events-boss]]). Fandom reports only the 15 hull
  ([[source-fandom-repair-station-in-last-stand]]) — not a contradiction, but the systems
  repair is easy to miss.
- Routing to hit all three before the first Flagship phase is the obvious play, and the
  reason the sector is survivable at all. *(Opinion, derived from the allocation; no
  source states it.)*

## Related
- [[event-fight-in-last-stand]] — the six guaranteed fights these offset
- [[sector-the-last-stand]]
- [[event-repair-station]] — the ordinary-sector equivalent
- [[entity-federation]]

## Open Questions
- [ ] Whether visiting the same station twice repeats the payout (no `unique` attribute is
      set, but the sector allocation places three distinct beacons).

## Sources
- [[source-events-boss]] (per raw/gamedata/events_boss.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-repair-station-in-last-stand]] (per raw/wiki/repair-station-in-last-stand.md)
