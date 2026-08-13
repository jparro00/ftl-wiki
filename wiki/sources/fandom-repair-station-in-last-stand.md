---
id: source-fandom-repair-station-in-last-stand
type: source
source_kind: wiki
raw: raw/wiki/repair-station-in-last-stand.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [last-stand, endgame, hull-repair, free-resources, federation]
---

# Fandom — "Repair station in Last Stand"

## Summary
Community wiki page for `BOSS_REPAIR_STATION`, retrieved at revision 74670. Five intro
strings and one unconditional payout, with every number spelled out.

## Key Takeaways
- Names the in-game id in Trivia: *"This event is called 'BOSS_REPAIR_STATION' in the
  datafiles."*
- Payout stated as **15 repairs, 22–44 scrap, 5 fuel, 4 missiles, 5 drone parts** — matches
  the `<damage amount="-15"/>` and `<item_modify>` block in `events_boss.xml`
  figure-for-figure.
- Flags the typo in the first intro string (*"There is **a a** mobile ship construction
  platform"*) — and the typo is genuinely in the shipped data, not a transcription error.
- Locations box marks it as a repair beacon.
- Categories: Fuel reward, Missiles reward, Drone Parts reward.
- Reports only the 15 hull; does **not** mention the separate `<repair/>` tag, which
  repairs damaged systems.

## Events Covered
- [[event-repair-station-in-last-stand]]

## Other Pages Touched
- [[sector-the-last-stand]], [[entity-federation]]

## Reliability Notes
`medium`; every stated number checks out. The omission of the `<repair/>` systems pass is
an incompleteness, not a conflict.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Repair_station_in_Last_Stand
- [[source-events-boss]], [[source-text-events-xml]], [[source-sector-data-xml]]
