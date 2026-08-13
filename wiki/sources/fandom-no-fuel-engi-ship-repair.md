---
id: source-fandom-no-fuel-engi-ship-repair
type: source
source_kind: wiki
raw: raw/wiki/no-fuel-engi-ship-repair.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [out-of-fuel, engi]
---

# Fandom — "No fuel: Engi ship repair"

## Summary
Community wiki page for `FUEL_OFF_ENGI_DUBIOUS`, retrieved at revision 73274. Expands all
four hail outcomes with resolved resource ranges and the enemy-ship reward tiers.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'FUEL_OFF_ENGI_DUBIOUS' in the
  datafiles."*
- Marks it `{{Locations|outoffuel=distressoff}}`, matching the XML.
- Resolves ranges: 2–6 fuel free; 10–20 scrap for 4–6 fuel; blue option costs 1 drone part
  for 4–6 fuel.
- Confirms the hostile branch's ship (`FUEL_OFF_ENGI_DUBIOUS`) has an 80s escape timer and
  **no surrender**, and reads its rewards as medium (2–4 fuel) destroyed / high (3–6 fuel)
  crew-killed.

## Events Covered
- [[event-no-fuel-engi-ship-repair]]

## Other Pages Touched
- [[item-hull-repair-drone]], [[entity-engi]]

## Reliability Notes
`medium`, `game_version: unknown`. Its numeric readings of the `autoReward` tiers (2–4 /
3–6 fuel) are the only figures any source gives for them.

## Contradictions Flagged
None. Note only that Fandom quotes the deadCrew text as *"With the hostile Engi subdued…"*
while the game file reads *"With the hostile **Engies** subdued…"*
([[source-text-events-xml]]) — a transcription slip, not a mechanical disagreement.

## Links
- Source URL: https://ftl.fandom.com/wiki/No_fuel:_Engi_ship_repair
- [[source-events-fuel]], [[source-text-events-xml]], [[source-events-ships]]
