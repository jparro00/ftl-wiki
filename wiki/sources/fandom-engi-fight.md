---
id: source-fandom-engi-fight
type: source
source_kind: wiki
raw: raw/wiki/engi-fight.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [zoltan, filler-fight, engi, default-rewards]
---

# Fandom — "Engi fight"

## Summary
The community wiki page for `ZOLTAN_ENGI`. Retrieved via the MediaWiki API at revision
74046. A minimal page. Its page title is misleading — despite being called "Engi fight",
the event is **Zoltan-sector content** and its in-game id is `ZOLTAN_ENGI`.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'ZOLTAN_ENGI' in the
  datafiles."* Without this line the page title would suggest an Engi-sector event.
- Confirms the locations are **Zoltan Controlled Sector and Zoltan Homeworlds** — not
  [[sector-engi-homeworlds]].
- Confirms **default rewards** and no choices.
- **Supplies what the game files do not:** `ENGI_SHIP` has **no surrender or escape**
  values specified in `events_ships.xml`.
- `unique=true`, Long-Ranged Scanners `ship`.
- Categorised `Fights with Default Rewards`.

## Events Covered
- [[event-engi-fight]]

## Other Pages Touched
- [[entity-engi]]

## Reliability Notes
`medium`. States no game version. Gives no `ENGI_SHIP` loadout.

## Contradictions Flagged
None. Intro text matches the game files. Note that the page's "debris field" flavour is
**not** an environment hazard — the game file carries no `<environment>` element
([[source-events-zoltan]]).

## Links
- Source URL: https://ftl.fandom.com/wiki/Engi_fight
- [[source-events-zoltan]], [[source-text-events-xml]]
