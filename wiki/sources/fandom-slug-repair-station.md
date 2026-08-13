---
id: source-fandom-slug-repair-station
type: source
source_kind: wiki
raw: raw/wiki/slug-repair-station.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [slug, hull-repair, extortion, system-malfunction]
---

# Fandom — "Slug repair station"

## Summary
Community wiki page for `NEBULA_SLUG_HULLFIX`, retrieved at revision 74285. Reconstructs the
three-level branch structure (`RESULT1` → `RESULT2`, and `REQUEST`) and puts numbers on
every transaction.

## Key Takeaways
- Names the in-game id in Trivia: *"This event is called 'NEBULA_SLUG_HULLFIX' in the
  datafiles."*
- All transaction values match the files: +10 / +1 hull repaired, 15 fuel demanded, 50
  scrap demanded, 50 scrap for 10 hull on the honest trade.
- Confirms the Engines-capped fight (`JELLY_STATUS_ENGINES`, `MED` destroyed / `HIGH`
  deadCrew) and the Weapons-halved fight (`JELLY_STATUS_WEAPONS`, `HIGH` either way).
- Reads the bomb branch's `damage 4` + `damage 1 system="random"` as **"5 hull damage,
  1 damage to a random system"** — a summed reading, the same convention it uses on
  [[source-fandom-nebula-wreckage]].
- **Behavioural note not in the files:** *"Revisiting the beacon will remove systems
  malfunction, but the enemy ship and rewards will be exactly the same."*
- Categories: hull-damage, system-damage, system-malfunction, hull-repair, fuel-use and
  scrap-use.

## Events Covered
- [[event-slug-repair-station]]

## Other Pages Touched
- [[entity-slugs]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]

## Reliability Notes
`medium`; every number checks out against the files. The revisit note is an in-play
observation the data cannot confirm.

## Contradictions Flagged
None. The "5 hull" reading is a summing convention, not a competing value — noted on
[[event-slug-repair-station]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Slug_repair_station
- [[source-events-slug]], [[source-events-ships]], [[source-text-events-xml]]
