---
id: event-mantis-fight-near-sun
type: event
event_name: MANTIS_SUN_FIGHT
sectors: [[[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [mantis, no-choice, default-rewards, environmental-hazard, sun, combat]
---

# Mantis fight near sun — `MANTIS_SUN_FIGHT`

## Summary
[[event-mantis-fight]] with a star hazard bolted on. Identical enemy
(`ship load="MANTIS_FIGHT"`), identical lack of choices, plus `<environment type="sun"/>`
— periodic solar flares that set fires on both ships and heat hull. It is the only
`HOSTILE_MANTIS` entry that is a Mantis fight in a hazard environment.

## Trigger & Where It Appears
- Sectors: [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]
- Drawn from `HOSTILE_MANTIS` and its Advanced Edition replacement
  `OVERRIDE_HOSTILE_MANTIS`, each of which lists it **once** against two entries for plain
  `MANTIS_FIGHT` ([[source-events-xml]], per `raw/gamedata/events_mantis.xml` and
  `raw/gamedata/dlcEventsOverwrite.xml`). Mantis sectors allocate the hostile list at
  `min=6 max=7` beacons ([[source-sector-data-xml]]).
- `unique="false"` — it can repeat.
- Long-range scanners show a ship **and** the red-giant hazard marker
  ([[source-fandom-mantis-fight-near-sun]]).

## Text
> Who knows why the Mantis would venture so close to a sun. Perhaps it makes for more of
> a challenge?

(`event_MANTIS_SUN_FIGHT_text`, per [[source-text-events-xml]])

Unlike most Mantis events this one has a single fixed string, not a text list.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event has no `<choice>` elements)_ | — | Immediate combat with a Mantis ship (`ship load="MANTIS_FIGHT" hostile="true"`) in a `sun` environment, **default rewards**. | 100% |

## Blue Options
None.

## Rewards & Risks
- Reward: default combat rewards, the same as [[event-mantis-fight]] — the hazard adds
  risk without adding payout.
- Risk: the `sun` environment. The event declares only `<environment type="sun"/>`; the
  mechanical effect of that environment is not described in any source read for this page,
  so the specifics are recorded as **unknown** here rather than filled in from memory.
- The hazard applies to the enemy too, which cuts both ways.

## Strategy Notes
- *(Opinion.)* Nothing to decide at the beacon — the decision is upstream, at the sector
  map, where a sun icon plus a Mantis sector is a worse combination than either alone.
  Fire suppression (doors, crew placement, a Fire Drone) matters more here than in a plain
  Mantis fight.

## Related
- [[event-mantis-fight]] — the same fight without the star
- [[event-mantis-fight-choice]] — the avoidable version
- [[concept-environmental-hazards]] — sun / asteroid / pulsar / nebula beacon effects
- [[entity-mantis]]
- [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]

## Open Questions
- [ ] Exact mechanics and tick rate of `<environment type="sun"/>`.
- [ ] Numeric values behind "default rewards".
- [ ] Composition of the `MANTIS_FIGHT` ship blueprint.

## Sources
- [[source-events-xml]] (per raw/gamedata/events_mantis.xml, raw/gamedata/dlcEventsOverwrite.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-mantis-fight-near-sun]] (per raw/wiki/mantis-fight-near-sun.md)
