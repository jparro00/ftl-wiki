---
id: source-fandom-mantis-fight-in-nebula
type: source
source_kind: wiki
raw: raw/wiki/mantis-fight-in-nebula.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [nebula, mantis, combat, default-rewards]
---

# Fandom — "Mantis fight in nebula"

## Summary
The community wiki page for `NEBULA_MANTIS_FIGHT`. Retrieved via the MediaWiki API at
revision 74257. Five intro-text variants and one forced fight.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'NEBULA_MANTIS_FIGHT' in the
  datafiles."*
- Locations: Civilian Sector, Uncharted Nebula. `nebula=true`, `alsooccur=nebulafiller`,
  `LRSmap=ship+nebula`, `unique=false`.
- Transcribes all five `text_NEBULA_MANTIS_FIGHT_*` variants; they match `text_events.xml`.
- Annotates the `MANTIS_FIGHT` enemy ship as **no surrender, no escape**, citing
  `events_ships.xml`.
- Outcome: default rewards.
- Two of the five texts say *"storm"* rather than nebula, even though the event's
  environment tag is `nebula`.

## Events Covered
- [[event-mantis-fight-in-nebula]]

## Other Pages Touched
- [[entity-mantis]], [[sector-uncharted-nebula]], [[sector-civilian-sector]],
  [[event-mantis-fight]]

## Reliability Notes
`medium`. Version unstated. Its location list omits **Federation Space**, which reaches
this event through the `NEBULA` list (`STANDARD_SPACE`, `NEBULA min=0 max=4` in
`sector_data.xml`).

## Contradictions Flagged
- Sector coverage: Fandom lists two sectors, the event lists reach three. Recorded on
  [[event-mantis-fight-in-nebula]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Mantis_fight_in_nebula
- [[source-events-nebula]], [[source-events-ships]], [[source-newevents]],
  [[source-sector-data-xml]]
