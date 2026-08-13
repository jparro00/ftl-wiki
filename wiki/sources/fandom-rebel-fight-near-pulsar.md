---
id: source-fandom-rebel-fight-near-pulsar
type: source
source_kind: wiki
raw: raw/wiki/rebel-fight-near-pulsar.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rebel, pulsar, hazard, combat, advanced-edition]
---

# Fandom — "Rebel fight near pulsar"

## Summary
Community wiki page for `REBEL_PULSAR`, retrieved via the MediaWiki API at revision 73809.
Three intro variants, one outcome, and the sector list the game files do not state directly.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'REBEL_PULSAR' in the datafiles."*
- **Sectors**: Civilian Sector, Mantis Controlled Sector, Mantis Homeworlds, Rebel Controlled
  Sector, Rebel Stronghold, Zoltan Controlled Sector, Zoltan Homeworlds — the page's main
  contribution, since the event definition names only the five `OVERRIDE_` hostile lists it
  belongs to.
- `pulsar=true`, `LRSmap=ship+pulsar`, `unique=true`.
- All three `REBEL_PULSAR_TEXT` strings transcribed, matching the files.
- Outcome: fight a Rebel ship with *"default rewards"*.
- Categorised *Advanced Edition Content Events*, *Fights with Default Rewards*.

## Events Covered
- [[event-rebel-fight-near-pulsar]]

## Other Pages Touched
- [[sector-civilian-sector]], [[sector-mantis-controlled-sector]],
  [[sector-mantis-homeworlds]], [[sector-rebel-controlled-sector]],
  [[sector-rebel-stronghold]], [[sector-zoltan-controlled-sector]],
  [[sector-zoltan-homeworlds]], [[entity-rebels]], [[concept-hazards]]

## Reliability Notes
`medium`. Its seven-sector list maps cleanly onto `OVERRIDE_HOSTILE_MANTIS`,
`OVERRIDE_HOSTILE_REBEL`, `OVERRIDE_HOSTILE_ZOLTAN` and `HOSTILE1` (Civilian) — but is
narrower than the depth-based `HOSTILE1`/`HOSTILE2` allocations in `newEvents.xml` would
imply.

## Contradictions Flagged
None on text.

## Links
- Source URL: https://ftl.fandom.com/wiki/Rebel_fight_near_pulsar
- [[source-dlcevents]], [[source-dlceventsoverwrite]], [[source-text-events-xml]]
