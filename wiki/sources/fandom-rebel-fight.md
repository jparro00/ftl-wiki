---
id: source-fandom-rebel-fight
type: source
source_kind: wiki
raw: raw/wiki/rebel-fight.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rebel, combat, default-rewards]
---

# Fandom — "Rebel fight"

## Summary
The community wiki page for `REBEL`, the baseline Rebel warship encounter. Retrieved via the
MediaWiki API at revision 73786. Almost entirely a transcription of the ten-string intro
text list plus a one-line outcome.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'REBEL' in the datafiles."*
- Locations: Abandoned Sector, Civilian Sector, Engi Controlled Sector, Engi Homeworlds,
  Mantis Controlled Sector, Mantis Homeworlds, Rebel Controlled Sector, Rebel Stronghold,
  The Last Stand, Zoltan Controlled Sector, Zoltan Homeworlds. `LRSmap=ship`,
  `unique=false`. It omits [[sector-federation-space]], which the generic `HOSTILE1` pool
  reaches.
- Transcribes all **ten** `text_REBEL_*` variants verbatim; they match `text_events.xml`.
- States the outcome as *"Fight a Rebel ship (default rewards)"* and says nothing about the
  `REBEL` ship's 50% surrender and 50% escape branches, which
  `events_ships.xml` does define.
- Categorised `Random_Events`, `Fights with Default Rewards`.

## Events Covered
- [[event-rebel-fight]]

## Other Pages Touched
- [[concept-rebel-fleet-advance]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]],
  [[sector-the-last-stand]]

## Reliability Notes
`medium`. Version unstated. Complete on the prose, incomplete on the mechanics — it omits
the ship's surrender/escape behaviour entirely.

## Contradictions Flagged
- Surrender/escape branches omitted — recorded on [[event-rebel-fight]].
- Three unrelated Fandom pages (`Battlefield wreckage`, `Crystal chat`,
  `Encrypted federation signal`) were auto-matched to the `REBEL` id during ingest because
  they load the same enemy *ship*. Each names its own id. This page is the only genuine
  `REBEL` join.

## Links
- Source URL: https://ftl.fandom.com/wiki/Rebel_fight
- [[source-events-rebel]], [[source-events-ships]], [[source-text-events-xml]]
