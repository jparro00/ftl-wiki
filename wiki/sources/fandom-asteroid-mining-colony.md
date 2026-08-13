---
id: source-fandom-asteroid-mining-colony
type: source
source_kind: wiki
raw: raw/wiki/asteroid-mining-colony.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [trading, missiles, augment-reward, hull-repair, reactor-upgrade, blue-option]
---

# Fandom — "Asteroid mining colony"

## Summary
The community wiki page for `HELP_MINERS`. Retrieved via the MediaWiki API at revision
73934. A short page that matches the game files outcome for outcome, and states plainly
that the blue option is cosmetic.

## Key Takeaways
- **Names the in-game id explicitly:** *"This event is called 'HELP_MINERS' in the
  datafiles."*
- **States the blue option has no mechanical effect:** *"[option has no effect] … Nothing
  happens and the same non-blue options become available again."* This matches the XML,
  where the `req="WEAPONS_MISSILES_EVENTS"` branch re-presents the identical three
  choices.
- Confirms the two donation tiers and all six outcomes, including exact scrap ranges
  (15–25 and 30–40) that match `item_modify` in `newEvents.xml`.
- Reads `<damage amount="-10"/>` etc. as **hull repairs** — 10 repairs for the 5-missile
  branch, 15 and 5 for the 15-missile branches.
- Locations template: 13 sectors plus `alsooccur=exit`, `unique=true`, Long-Range Scanners
  `noship`. Matches `ITEMS` / `OVERRIDE_ITEMS` membership.
- Categorised `Trading Events`, `Augmentation reward chance`, `Hull Repair chance`,
  `Reactor Upgrade chance`.

## Events Covered
- [[event-asteroid-mining-colony]]

## Other Pages Touched
- [[concept-blue-options]], [[item-reactor]]

## Reliability Notes
`medium`. No version stated; the event is Advanced Edition content per its position in
`newEvents.xml` and the AE-only `WEAPONS_MISSILES_EVENTS` blueprint list. Every mechanical
claim on the page is independently confirmed by the game files.

## Contradictions Flagged
One transcription slip in the blue-option prose: the wiki has *"isn't exactly what I'd
call 'union-friendly'"* where `text_events.xml` has *"isn't exactly what I would call,
'union-friendly'"*. Recorded on [[event-asteroid-mining-colony]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Asteroid_mining_colony
- [[source-newevents]], [[source-dlceventsoverwrite]], [[source-dlcblueprintsoverwrite]],
  [[source-text-events-xml]], [[source-sector-data-xml]]
