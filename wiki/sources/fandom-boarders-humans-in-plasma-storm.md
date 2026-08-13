---
id: source-fandom-boarders-humans-in-plasma-storm
type: source
source_kind: wiki
raw: raw/wiki/boarders-humans-in-plasma-storm.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [plasma-storm, boarding, crew-risk, unique]
---

# Fandom — "Boarders: Humans in plasma storm"

## Summary
The community wiki page for `STORM_BOARDING`. Retrieved via the MediaWiki API at revision
73960. One paragraph of prose, one outcome, and one genuinely non-obvious note about
fleet pursuit in Slug sectors.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'STORM_BOARDING' in the datafiles."*
- Locations: Civilian Sector, Slug Controlled Nebula, Slug Home Nebula.
  `plasmastorm=true`, `alsooccur=nebulafiller`, `LRSmap=noship+plasmastorm`, `unique=true`.
- Outcome: **medium scrap with resources AND 3–4 human boarders**. Matches
  `<boarders min="3" max="4" class="human"/>` + `autoReward level="MED">standard`. This is
  the only boarding event in the nebula file that pays you.
- **Slug-sector pursuit note:** *"In Slug sectors this event can occur in a non-nebula area
  of the beacon map. In that case the event will still have a plasma storm nebula
  environment, but the Fleet pursuit will be the full amount (instead of the 80% that you
  would have when jumping from a nebula beacon in a Slug sector)."* Not derivable from the
  event XML; it follows from `STORM_SLUG` being a sector-allocated list in
  `sector_data.xml` rather than a nebula-only pool.
- Categorised `Boarding hazard`.

## Events Covered
- [[event-boarders-humans-in-plasma-storm]]

## Other Pages Touched
- [[sector-slug-home-nebula]], [[sector-slug-controlled-nebula]],
  [[sector-civilian-sector]], [[concept-rebel-fleet-advance]]

## Reliability Notes
`medium`. Version unstated. The XML comment on this event reads `<!--DLC - Kinda-->`, and
its entry in `NEBULA` is annotated *"DLC re-added - was removed previously"* — so its
availability differs between builds and the page does not say which one it describes.

## Contradictions Flagged
- Fandom lists three sectors; `NEBULA` (which includes `STORM_BOARDING`) is also allocated
  in Federation Space. Recorded on [[event-boarders-humans-in-plasma-storm]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Boarders:_Humans_in_plasma_storm
- [[source-events-nebula]], [[source-events-slug]], [[source-newevents]],
  [[source-sector-data-xml]]
