---
id: source-fandom-crystalline-cache
type: source
source_kind: wiki
raw: raw/wiki/crystalline-cache.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [crystal-sector, blue-option, crew-risk, weapon-reward, bug]
---

# Fandom — "Crystalline cache"

## Summary
The community wiki page for `CRYSTAL_CACHE`. Retrieved via the MediaWiki API at revision
74727 — the most recently revised page in this batch. It maps the full three-route entry
puzzle, the shared interior list, and the singularity trap branch, and adds two engine
notes that are not derivable from the event file.

## Key Takeaways
- Names the in-game id: *"This event is called 'CRYSTAL_CACHE' in the datafiles"*.
- Quantifies the LOW "stuff" reward as fuel 1–3, missiles 1–2, drone parts 1, plus scrap.
- **Engine note (reward suppression):** *"The 'resources and scrap' component will never
  give a bonus weapon, drone schematic or augmentation, due to its interaction with a
  guaranteed weapon/drone schematic reward."* This is a general FTL rule, not specific to
  this event — the same footnote reappears on [[source-fandom-crystalline-men-buried]].
- **Bug note:** the "detonate your fuel reserves" option loses no fuel if the reward roll
  happens to include fuel.
- Confirms Clone Bay **does** revive the crew member lost in the "Pull out now!" branch,
  matching `<clone>true</clone>` in the file.
- Documents both blue options inside the trap branch: Improved Teleporter (level 2+) and
  Advanced Engines (level 7+).
- Location: Hidden Crystal Worlds, `unique=true`, **no ship** on Long-Range Scanners.

## Events Covered
- [[event-crystalline-cache]]

## Other Pages Touched
- [[sector-hidden-crystal-worlds]], [[entity-crystal-men]], [[item-breach-missiles]],
  [[concept-blue-options]]

## Reliability Notes
`medium`. No game version stated. Its structural transcription matches the game files
node for node; the reward-suppression and fuel-bug notes are the page's own analysis and
are not corroborated by any other ingested source.

## Contradictions Flagged
None of substance. The page transcribes the intro text ending "break through" where the
shipped string reads "break though" — a typo fix, not a disagreement.

## Links
- Source URL: https://ftl.fandom.com/wiki/Crystalline_cache
- [[source-events-xml]], [[source-text-events-xml]]
