---
id: source-fandom-lanius-ship-attacking-mantis
type: source
source_kind: wiki
raw: raw/wiki/lanius-ship-attacking-mantis.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [lanius, mantis, distress, missiles, advanced-edition]
---

# Fandom — "Lanius ship attacking Mantis"

## Summary
The community wiki page for `LANIUS_MANTIS_DISTRESS`. Retrieved at revision 74236. Two
choices, one fight, and a two-member aftermath list.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'LANIUS_MANTIS_DISTRESS' in the
  datafiles."*
- Locations: Abandoned Sector, `distress=true`, `LRSmap=noship`, `unique=true`.
- Enemy is `LANIUS_MANTIS_DISTRESS_SHIP`, annotated **no surrender, no escape**; both win
  states pay medium scrap-with-resources and then offer "Contact the Mantis".
- Expands the aftermath missile reward with a tooltip: *2-4 missiles*.
- Categories: `Advanced Edition Content Events`, `Missiles reward opportunity`.

## Events Covered
- [[event-lanius-ship-attacking-mantis]]

## Other Pages Touched
- [[entity-lanius]], [[entity-mantis]], [[sector-abandoned-sector]]

## Reliability Notes
`medium`. Matches the XML. The 2-4 missile figure is Fandom's expansion of the reward
table, not stated in `raw/gamedata/`.

## Contradictions Flagged
Wording only: Fandom renders the attack result as *"The Lanius haven't noticed you yet"*
where `event_LANIUS_MANTIS_DISTRESS_c1_text` reads *"The Lanius don't seem to have noticed
you yet"*, and the aftermath as *"The Mantis ship sustained too much damage"* where the
file reads *"The Mantis ship **has** sustained too much damage"*.

## Links
- Source URL: https://ftl.fandom.com/wiki/Lanius_ship_attacking_Mantis
- [[source-dlcevents-anaerobic]], [[source-text-events-xml]]
