---
id: source-fandom-destroyed-cargo-ship
type: source
source_kind: wiki
raw: raw/wiki/destroyed-cargo-ship.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [pirate, boarding-risk, blue-option, trap]
---

# Fandom — "Destroyed cargo ship"

## Summary
Community wiki page for `FLOATING_CARGO`, retrieved via the MediaWiki API at revision
74041. Fully expands both outcome lists — the four "bring it aboard" entries and the three
scan entries — and matches the game files entry for entry.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'FLOATING_CARGO' in the datafiles."*
- Locations: **Pirate Controlled Sector only**; `LRSmap=noship`, `unique=true`. This
  corroborates the reading that `HOSTILE_BOARDING` is a dead list in `sector_data.xml`
  (`min=0 max=0` in Federation Space, commented out in the Civilian Sector), so the event
  only reaches players through `BOARDERS_PIRATE`.
- Transcribes all four `FLOATING_CARGO_LIST` outcomes with the right payloads: medium
  standard, low scrap, 2–4 human boarders, and boarders + a pirate ship.
- Transcribes all three `FLOATING_CARGO_SCAN_LIST` outcomes, including the explicit
  **20–35 scrap** value and the ambush sub-choice.
- Documents both blue options (Advanced Sensors level 2+ and the Long-Ranged Scanners
  augment) and correctly notes they lead to the same scan list.
- Annotates the two enemy ships: `JELLY_PIRATE_WITHBOARDERS` and `PIRATE`.

## Events Covered
- [[event-destroyed-cargo-ship]]

## Other Pages Touched
- [[event-pirate-fight]], [[item-long-ranged-scanners]], [[entity-pirates]],
  [[sector-pirate-controlled-sector]]

## Reliability Notes
`medium`. No version stated. The most complete Fandom page in this batch — the only one
whose outcome tree fully expanded.

## Contradictions Flagged
- **The `chance` attribute reading.** Fandom: *"70% chance for escape attempt at 20-40%
  hull with 15 seconds countdown timer and makes a surrender offer at 0-50% hull"*. Game
  file: `<escape chance="0.3" min="2" max="4" timer="15"/>` and
  `<surrender min="0" max="5"/>` with **no** `chance` attribute. Fandom reports
  `1 − chance`, the same inversion as [[source-fandom-pirate-briber]]. Recorded on
  [[event-destroyed-cargo-ship]] and [[event-pirate-fight]]; raw values trusted, semantics
  left open.
- Renders `min`/`max` hull **points** as hull **percentages** (its own tooltip concedes
  "actual in-game value may be 2-4 hull").

## Links
- Source URL: https://ftl.fandom.com/wiki/Destroyed_cargo_ship
- [[source-events-pirate]], [[source-events-ships]], [[source-sector-data-xml]],
  [[source-newevents]]
