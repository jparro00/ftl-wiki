---
id: source-fandom-mantis-fight
type: source
source_kind: wiki
raw: raw/wiki/mantis-fight.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [mantis, combat, default-rewards]
---

# Fandom — "Mantis fight"

## Summary
The community wiki page for `MANTIS_FIGHT`. Retrieved via the MediaWiki API at revision
74251. Almost entirely a transcription of the twenty-string intro text list, plus the
enemy-ship annotation.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'MANTIS_FIGHT' in the datafiles."*
- Locations: Civilian Sector, Mantis Controlled Sector, Mantis Homeworlds; `LRSmap=ship`,
  `unique=false`. Note it does **not** list Federation Space, though `MANTIS_HOSTILE` is
  loaded by the generic `HOSTILE1` / `OVERRIDE_HOSTILE1` pools — the sector reach recorded
  on [[event-mantis-fight]] comes from [[source-events-xml]], not from here.
- Transcribes all **twenty** `text_MANTIS_FIGHT_*` variants verbatim; they match
  `text_events.xml`.
- States the outcome as *"Fight a Mantis Ship (default rewards)"* and annotates the
  `MANTIS_FIGHT` enemy ship as **no surrender, no escape**, citing `events_ships.xml`.
  "Default rewards" is Fandom's own term for the standard payout when a ship definition
  specifies none — the concept has no direct equivalent name in the XML.
- Categorised `Random_Events`, `Fights with Default Rewards`.

## Events Covered
- [[event-mantis-fight]]

## Other Pages Touched
- [[entity-mantis]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]],
  [[sector-civilian-sector]]

## Reliability Notes
`medium`. Version unstated. Its sector list is narrower than the event lists imply — treat
it as incomplete rather than wrong.

## Contradictions Flagged
None outright. One scope note: eleven *other* Fandom pages were auto-matched to the
`MANTIS_FIGHT` event id during ingest because they reference the same enemy ship. Each of
them names a different in-game id in its own Notes section (`WRECKAGE_EVENT`,
`NEBULA_MANTIS_CHOICE`, `ENGI_MANTIS_FIGHT`, `NEBULA_SLUG_MANTIS`, `NEBULA_MANTIS_FIGHT`,
`SLUG_MANTIS`, `ZOLTAN_MANTIS`, `ZOLTAN_BOARDERS_MANTIS`, `ROCK_MANTIS_HUNTER`) and
belongs on its own event page. This page is the only genuine `MANTIS_FIGHT` join.

## Links
- Source URL: https://ftl.fandom.com/wiki/Mantis_fight
- [[source-events-xml]], [[source-text-events-xml]], [[source-sector-data-xml]]
