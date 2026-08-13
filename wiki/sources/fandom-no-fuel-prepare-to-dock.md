---
id: source-fandom-no-fuel-prepare-to-dock
type: source
source_kind: wiki
raw: raw/wiki/no-fuel-prepare-to-dock.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [out-of-fuel]
---

# Fandom — "No fuel: prepare to dock"

## Summary
Community wiki page for the event the game files call `FUEL_APPROACH`, retrieved via the
MediaWiki API at revision 73278. Lays out all three branches with resolved reward ranges
and identifies the enemy ship ids inline in HTML comments.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'FUEL_APPROACH' in the datafiles."*
- Marks the event `{{Locations|outoffuel=distressboth}}` — it is in both the distress-on and
  distress-off out-of-fuel pools, matching the XML.
- Resolves the `item_modify` ranges: 2–6 fuel (accept), 1–4 fuel (decline), 3–7 fuel (scan).
- Identifies the ships behind each hostile branch: `PIRATE_FUEL` (80s timer) for the boarding
  and decline ambushes, plain `PIRATE` (90s timer) for the accept ambush.
- Documents the nested Cloaking blue option inside the scan trap.

## Events Covered
- [[event-no-fuel-prepare-to-dock]]

## Other Pages Touched
- [[event-no-fuel-fuel-trader-distress-off]] (shared `FUEL_TRADER_HIGH_LIST` / `PT2` tree),
  [[item-long-ranged-scanners]], [[item-cloaking]]

## Reliability Notes
`medium`. The page states no game version, so `game_version` is `unknown`. Where it
disagrees with the extracted files, the files win.

## Contradictions Flagged
None for this event.

## Links
- Source URL: https://ftl.fandom.com/wiki/No_fuel:_prepare_to_dock
- [[source-events-fuel]], [[source-text-events-xml]], [[source-events-ships]]
