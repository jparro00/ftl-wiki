---
id: source-fandom-lanius-fight-with-friendly-asb-support
type: source
source_kind: wiki
raw: raw/wiki/lanius-fight-with-friendly-asb-support.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [lanius, combat, hazard, hull-repair, advanced-edition]
---

# Fandom — "Lanius fight with friendly ASB support"

## Summary
The community wiki page for `LANIUS_NOBOARDERS_PDS` — the one fight in the game where the
Anti-Ship Battery shoots at the *enemy*. Retrieved at revision 74226.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'LANIUS_NOBOARDERS_PDS' in the
  datafiles."*
- Locations: Abandoned Sector, `LRSmap=ship+PDS`, `unique=true`.
- Enemy is `LANIUS_BOARDERS_PDS`, annotated **no surrender, no escape**; destroyed pays
  medium and dead crew pays high scrap-with-resources.
- Quantifies the aftermath repair as **8 hull repairs**, matching
  `<damage amount="-8"/>` in `LANIUS_BOARDERS_PDS_LIST`.
- Categories: `Advanced Edition Content Events`, `Hull Repair chance`,
  `Anti-Ship Battery support`.

## Events Covered
- [[event-lanius-fight-with-friendly-asb-support]]

## Other Pages Touched
- [[entity-lanius]], [[sector-abandoned-sector]]

## Reliability Notes
`medium`. Matches the XML. Does not mention the commented-out `boarders` tag that the
event's `NOBOARDERS` name alludes to.

## Contradictions Flagged
Wording only (comma placement in the intro and aftermath strings).

## Links
- Source URL: https://ftl.fandom.com/wiki/Lanius_fight_with_friendly_ASB_support
- [[source-dlcevents-anaerobic]], [[source-text-events-xml]]
