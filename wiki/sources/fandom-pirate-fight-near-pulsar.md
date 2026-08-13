---
id: source-fandom-pirate-fight-near-pulsar
type: source
source_kind: wiki
raw: raw/wiki/pirate-fight-near-pulsar.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [pirate, pulsar, hazard, combat, advanced-edition]
---

# Fandom — "Pirate fight near pulsar"

## Summary
Community wiki page for `PIRATE_PULSAR`, retrieved via the MediaWiki API at revision 73769.
Short page: three intro variants, one outcome, and — most usefully — a sector list, which
the game files do not give directly for this event.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'PIRATE_PULSAR' in the datafiles."*
- **Sectors**: Civilian Sector, Engi Controlled Sector, Engi Homeworlds, Pirate Controlled
  Sector. This is the page's main contribution — the event's own definition names no sectors,
  only the four `OVERRIDE_` hostile lists it belongs to.
- `pulsar=true`, `LRSmap=ship+pulsar`, `unique=true`.
- All three `PIRATE_PULSAR_TEXT` strings transcribed, matching the files.
- Outcome: fight a Pirate ship with *"default rewards"*.
- Categorised *Advanced Edition Content Events*, *Fights with Default Rewards*, *Pirate ship
  fights*.

## Events Covered
- [[event-pirate-fight-near-pulsar]]

## Other Pages Touched
- [[sector-civilian-sector]], [[sector-engi-controlled-sector]],
  [[sector-engi-homeworlds]], [[sector-pirate-controlled-sector]], [[entity-pirates]],
  [[concept-hazards]]

## Reliability Notes
`medium`. Its sector list is narrower than a naive reading of the `HOSTILE1`/`HOSTILE2`
allocations in `raw/gamedata/newEvents.xml` would give — see the Open Questions on
[[event-pirate-fight-near-pulsar]].

## Contradictions Flagged
None on text. The sector-list question above is an unresolved gap, not a direct conflict.

## Links
- Source URL: https://ftl.fandom.com/wiki/Pirate_fight_near_pulsar
- [[source-dlcevents]], [[source-dlceventsoverwrite]], [[source-text-events-xml]]
