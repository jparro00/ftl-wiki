---
id: source-fandom-mantis-outcasts
type: source
source_kind: wiki
raw: raw/wiki/mantis-outcasts.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [zoltan, boarding-hazard, mantis, default-rewards]
---

# Fandom — "Mantis outcasts"

## Summary
The community wiki page for `ZOLTAN_BOARDERS_MANTIS`. Retrieved via the MediaWiki API at
revision 74261. Corroborates the boarder count and adds the one fact the game files
omit: the enemy ship never surrenders or flees.

## Key Takeaways
- **Names the in-game id explicitly**, in a Notes rather than Trivia section: *"This
  event is called 'ZOLTAN_BOARDERS_MANTIS' in the datafiles."*
- States **2–3 Mantis boarders**, matching the game file's
  `<boarders min="2" max="3" class="mantis"/>`.
- **Supplies what the game files do not:** the `MANTIS_FIGHT` ship has **no surrender or
  escape** values specified in `events_ships.xml` — the fight runs to a conclusion.
- Confirms **default rewards** and no choices.
- Locations template: both Zoltan sectors, `unique=true`, Long-Ranged Scanners `ship`.
- Categorised `Fights with Default Rewards`, `Boarding hazard`.

## Events Covered
- [[event-mantis-outcasts]]

## Other Pages Touched
- [[entity-mantis]], [[event-mantis-fight-zoltan]] (shares the
  `MANTIS_FIGHT` blueprint and the same surrender/escape note)

## Reliability Notes
`medium`. States no game version. The surrender/escape claim is the only content not
independently verifiable against the files ingested here.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Mantis_outcasts
- [[source-fandom-mantis-fight-zoltan]], [[source-events-zoltan]], [[source-text-events-xml]]
