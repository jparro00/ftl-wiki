---
id: event-empty-beacon-rock
type: event
event_name: NOTHING_ROCK
sectors: [[[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
beacon_type: empty
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [empty-beacon, flavor-only, rock]
---

# Empty beacon (Rock) — `NOTHING_ROCK`

## Summary
The Rock sectors' filler beacon. Nothing happens: no choices, no ship, no reward. It
exists so that a Rock sector map has a few beacons that only cost you the fuel to reach
them. `sector_data.xml` guarantees 2–3 of them per Rock sector
([[source-sector-data-xml]]).

## Trigger & Where It Appears
- Sectors: [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]
- Allocation: `<event name="NOTHING_ROCK" min="2" max="3"/>` in **both** Rock sector
  definitions ([[source-sector-data-xml]], per `raw/gamedata/sector_data.xml`)
- Beacon: ordinary, no ship present ([[source-fandom-empty-beacon-rock]] marks it
  `LRSmap=noship`)
- Not `unique` — the event can repeat within a sector ([[source-events-rock]])

## Text
Varies. The event body is a single `<text load="NOTHING_ROCK"/>` drawing from
`textList NOTHING_ROCK`, which has **7** entries — flavour about Rock trading posts,
mining platforms, hostile hails and merchants who won't deal with outsiders
([[source-events-rock]]). [[source-fandom-empty-beacon-rock]] transcribes all seven.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(no choices; continue)_ | — | Nothing happens. | 100% |

The event element contains only a `<text>` tag — no `<ship>`, `<autoReward>`,
`<crewMember>`, `<item_modify>` or `<damage>` ([[source-events-rock]]).

## Rewards & Risks
None of either.

## Strategy Notes
- Pure fuel cost. In a Rock sector, 2–3 of the beacons on the map are guaranteed to be
  these, which is worth knowing when you are counting how many *productive* beacons a
  Rock sector actually offers before the fleet catches up.

## Related
- [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]
- [[event-start-beacon-rock]] — the other purely-flavour structural Rock beacon
- [[event-store-rock]] — the other guaranteed non-combat allocation in Rock sectors
- [[entity-rock-men]] — the flavour text is mostly about their xenophobia

## Open Questions
- [ ] Whether the seven text variants are weighted evenly (the `textList` lists each id
      once, which implies uniform, but the game's selection rule is not documented here).

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-empty-beacon-rock]] (per raw/wiki/empty-beacon-rock.md)
