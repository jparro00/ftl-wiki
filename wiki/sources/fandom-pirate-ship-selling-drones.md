---
id: source-fandom-pirate-ship-selling-drones
type: source
source_kind: wiki
raw: raw/wiki/pirate-ship-selling-drones.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [trading, blue-option]
---

# Fandom — "Pirate ship selling drones"

## Summary
Full outcome tree for the pirate drone salesman, including the exact scrap costs of every
purchase option and the drone-system upgrade price tiers. Declares the datafile id:
**"This event is called `PIRATE_SALESMAN` in the datafiles."**

## Key Takeaways
- Prices: 25 scrap for 5 drone parts; 25–35 scrap for a drone schematic; drone-system
  upgrade 15–20 / 25–33 / 50–65 scrap depending on current level.
- "Buy nothing" is a trap: 3 hull damage, system/room damage, then a Pirate ship fight.
- Two blue options: Slug crew (flavour only — same branch as docking) and Hacking
  (skips the docking branch for low scrap).
- Notes the Slug blue option's wording is a hint that a purchase is required to avoid
  ship damage — an interpretation, not a datafile fact.

## Events Covered
- [[event-pirate-ship-selling-drones]] (`PIRATE_SALESMAN`)

## Other Pages Touched
- [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[entity-pirates]]

## Contradictions Flagged
- The page's "3 hull damage" for the *Buy nothing* branch is not in the XML, which lists
  three separate 1-point `damage` entries (engines + 2 rooms) and no hull-only damage
  entry. Recorded on the event page.

## Links
- https://ftl.fandom.com/wiki/Pirate_ship_selling_drones (revision 73776, retrieved 2026-08-09)
