---
id: source-fandom-settlement-mercenary-work
type: source
source_kind: wiki
raw: raw/wiki/settlement-mercenary-work.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [quest, pirate-fight, store]
---

# Fandom — "Settlement mercenary work"

## Summary
The community wiki page for `MERCENARY_WORK_START`. Retrieved via the MediaWiki API at
revision 74665. It documents both randomly-offered jobs and the full quest-marker payoff,
and its Trivia section carries two ship-behaviour facts that are only implicit in the XML.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'MERCENARY_WORK_START' in the datafiles."*
- Documents both `MERCENARY_WORK_LIST` entries — the space-dock rescue and the amateur
  pirates — as alternatives, matching the two-entry event list.
- Quest-marker payoff: medium scrap, 5 hull repairs and a store, matching
  `SQUAT_STORE_RESCUE`'s `destroyed`/`deadCrew` blocks.
- Trivia states **`SQUAT_STORE_RESCUE` never surrenders or escapes** and
  **`SQUAT_PIRATE_MERCENARY` never runs away** — both confirmed by the absence of the
  corresponding elements in `events_ships.xml`.
- Renders the pirate surrender as occurring at 30–40% hull with **no probability attached**,
  consistent with `<surrender min="3" max="4">` carrying no `chance` attribute.
- Records the surrender reward as a weapon with medium scrap, and the kill reward as low
  scrap with resources — i.e. sparing them pays better.
- `unique=true`, `LRSmap=noship`.

## Events Covered
- [[event-settlement-mercenary-work]] — both job branches and the fight profile
- [[event-quest-store-rescue]] — the quest-marker destination

## Other Pages Touched
- [[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]],
  [[sector-rock-homeworlds]], [[entity-pirates]], [[concept-rebel-fleet-advance]]

## Reliability Notes
`medium`. No game version stated, so `game_version: unknown`. Everything mechanical on the
page checks out against the extracted 1.6.x files.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** sector coverage. The page omits [[sector-federation-space]], but
> `sector_data.xml` allocates `QUESTS min=1 max=1` in `STANDARD_SPACE`
> ([[source-sector-data-xml]]). Recorded on [[event-settlement-mercenary-work]]; game files
> trusted. Recurs across every `QUESTS`-list event, so it reads as a template convention.

Minor wording drift in the pirate job's offer text (*"severely damaging the ship"* vs the
XML's *"severely damaging their ship"*) — cosmetic, not recorded on the event page.

## Links
- Source URL: https://ftl.fandom.com/wiki/Settlement_mercenary_work
- [[source-events-xml]], [[source-events-ships]], [[source-sector-data-xml]]
