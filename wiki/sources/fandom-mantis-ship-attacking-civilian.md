---
id: source-fandom-mantis-ship-attacking-civilian
type: source
source_kind: wiki
raw: raw/wiki/mantis-ship-attacking-civilian.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [mantis, optional-fight]
---

# Fandom — "Mantis ship attacking civilian"

## Summary
The community wiki page for `MANTIS_CIVILIAN`. Retrieved via the MediaWiki API at
revision 74262. Documents both choices, the enemy ship's surrender/escape behaviour, and
delegates the reward tree to a shared `{{Save the Civilian Ship}}` template.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'MANTIS_CIVILIAN' in the datafiles."*
- Locations: Engi Controlled Sector, Engi Homeworlds, Mantis Controlled Sector, Mantis
  Homeworlds; `LRSmap=ship`, `unique=false`. The LRS-shows-a-ship detail is not in the
  game files.
- Carries an explicit **no-surrender / no-escape** annotation for the `MANTIS_CIVILIAN`
  enemy ship, citing `events_ships.xml`. This matches the ship definition, which has only
  `destroyed` and `deadCrew` branches.
- States the win pays **medium scrap with resources**, matching
  `autoReward level="MED"` `standard` in the files.
- Transcribes all five intro variants and all three "stay out of it" variants verbatim;
  they match `text_events.xml`.
- The reward follow-up is behind the `{{Save the Civilian Ship}}` template, which the API
  dump does **not** expand — so the actual reward table had to come from
  `SAVE_CIVILIAN_LIST` in `raw/gamedata/events_pirate.xml` instead. This page alone is
  not sufficient for the outcomes.

## Events Covered
- [[event-mantis-ship-attacking-civilian]]

## Other Pages Touched
- [[entity-mantis]], [[entity-engi]], [[sector-mantis-controlled-sector]],
  [[sector-mantis-homeworlds]], [[sector-engi-controlled-sector]],
  [[sector-engi-homeworlds]]

## Reliability Notes
`medium`, and additionally **incomplete** as retrieved: the transcluded template that
holds the reward tree did not survive the API dump. Where it makes checkable claims it
agrees with the 1.6.x AE files.

## Contradictions Flagged
None. One notable point of agreement: Fandom quotes the crew-killed text as *"No more
life signs detected on the **pirate** ship"* — reproducing the same odd wording that the
game files carry in `ship_MANTIS_CIVILIAN_deadCrew_text`, so this is an in-game string,
not a wiki transcription error.

## Links
- Source URL: https://ftl.fandom.com/wiki/Mantis_ship_attacking_civilian
- [[source-events-xml]], [[source-text-events-xml]], [[source-sector-data-xml]]
