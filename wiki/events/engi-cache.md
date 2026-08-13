---
id: event-engi-cache
type: event
event_name: ENGI_FLEET_DELAY
sectors: [[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, fleet-delay, drone-reward, missile-cost]
---

# Engi cache — `ENGI_FLEET_DELAY`

## Summary
A clean two-way trade with no downside branch: spend 2 missiles to push the Rebel fleet
back 2 jumps, or take the cache for a drone schematic and medium scrap. One of the few
events in the game that lets you buy time on the fleet advance outright.

## Trigger & Where It Appears
- Sectors: [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]
- Beacon: ordinary — the event carries no `<distressBeacon/>` or `<store/>` tag
  ([[source-events-xml]], per `raw/gamedata/events_engi.xml`)
- Event list: `ITEMS_ENGI`, allocated `min=3 max=3` per Engi sector
  ([[source-sector-data-xml]])
- `unique="true"` — at most once per run

## Text
> You notice an Engi colony hiding on the other side of a nearby moon. It turns out they're
> excavating an equipment cache from the Federation-Mantis War, and they suggest it might
> be used to lure the pursuing rebel fleet.

(`event_ENGI_FLEET_DELAY_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Booby trap the cache. | 2 missiles | "You transfer down some missile warheads and the Engi rig them to blow before setting a distress signal to attract the fleet's attention." → `<item type="missiles" min="-2" max="-2"/>` and `<modifyPursuit amount="-2"/>` — the Rebel fleet is pushed back **2 turns**. | 100% |
| 2 | Secure the cache. | — | "You have the Engi complete their excavations and bring the supplies on-board." → `<autoReward level="MED">drone</autoReward>` — a **drone schematic** with medium scrap. | 100% |

`MED` is the game's own `autoReward` level; no source converts it to a scrap number
([[source-events-xml]]). The reward *type* (`drone`) comes from the game files and is
corroborated by [[source-fandom-engi-cache]], which reads it as "a drone schematic with
medium scrap".

## Blue Options
None. Choice 1 is gated on carrying 2 missiles, which is a resource cost rather than a
`req=` blue option.

## Rewards & Risks
- Choice 1: −2 missiles, Rebel fleet delayed 2 turns. No scrap.
- Choice 2: a drone schematic plus `MED` scrap. No cost.
- No branch of this event can hurt you — there is no fight, no crew risk, and no hull
  damage in any outcome ([[source-events-xml]]).

## Strategy Notes
- Two missiles for two jumps of fleet delay is cheap if you are behind the curve or want
  to fully explore a sector; it is a waste if you are already ahead of the fleet.
  *(Opinion.)*
- If you have no missile weapon, choice 2 is free value and choice 1 costs you nothing you
  were using — but the delay is only worth taking when you actually intend to spend the
  extra jumps. *(Opinion.)*

## Related
- [[concept-rebel-fleet-advance]] — what `modifyPursuit` is buying you
- [[event-engi-surrender]] — the other free-value event in `ITEMS_ENGI`
- [[event-free-scrap-with-resources-engi]] — also in `ITEMS_ENGI`

## Open Questions
- [ ] Scrap value of `MED` alongside a `drone` reward.
- [ ] Is choice 1 hidden or merely refused when you have fewer than 2 missiles?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-engi-cache]] (per `raw/wiki/engi-cache.md`)
