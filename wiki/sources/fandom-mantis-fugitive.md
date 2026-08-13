---
id: source-fandom-mantis-fugitive
type: source
source_kind: wiki
raw: raw/wiki/mantis-fugitive.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [mantis, engi, crew-reward-chance, boarding-risk]
---

# Fandom — "Mantis fugitive"

## Summary
Community wiki page for `ALISON_MANTIS_CREW`, retrieved via the MediaWiki API at revision
74260. Short and accurate: two choices, five outcomes, each with its damage figures and a
footnote naming the enemy ship id.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'ALISON_MANTIS_CREW' in the datafiles."*
- Locations: Engi Controlled Sector, Engi Homeworlds, Mantis Controlled Sector, Mantis
  Homeworlds; `LRSmap=noship`, `unique=true` — matching the files exactly.
- Names both enemy ships by their file ids, `ENGI_MANTIS_CONTROLLED` and `ENGI_SHIP`, and
  records that **neither offers surrender or escape** — which `events_ships.xml` confirms.
- Its damage totals (5 hull on both bad outcomes) match the **AE** reading of the
  DLC-marked `<damage>` tags.

## Events Covered
- [[event-mantis-fugitive]]

## Other Pages Touched
- [[entity-mantis]], [[entity-engi]], [[sector-engi-controlled-sector]],
  [[sector-mantis-controlled-sector]]

## Reliability Notes
`medium`. No version stated; the damage figures imply Advanced Edition.

## Contradictions Flagged
None. Every outcome, reward level and ship id matches the game files.

## Links
- Source URL: https://ftl.fandom.com/wiki/Mantis_fugitive
- [[source-events-xml]], [[source-events-ships]], [[source-events-engi]], [[source-events-mantis]]
