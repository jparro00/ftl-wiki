---
id: source-fandom-augmentations
type: source
source_kind: wiki
raw: raw/wiki/augmentations.md
game_version: both
date: 2026-08-15
ingested: 2026-08-15
reliability: medium
tags: [augment, lrs, map-reveal, beacon, sector, routing]
---

# Fandom — "Augmentations"

## Summary
The full augment list, retrieved at revision 74810. Fetched for the map-facing augments —
Long-Ranged Scanners, Distraction Buoys, Lifeform Scanner — which are the only things that
change what the sector map tells you before you jump.

## Key Takeaways
- **Long-Ranged Scanners** — 30 scrap, store rarity 1, starting augment on all Stealth
  Cruisers. *"Reveal environmental hazards and possible ship presence of adjacent beacons."*
  The limits are stated explicitly and matter:
  - it works **retroactively and proactively** — buying it reveals adjacent beacons you
    already flew past; **selling or swapping it removes all previously revealed information**;
  - **"If the scanners don't indicate a ship presence at a beacon, it may still result in a
    ship fight. Likewise, even if a ship is detected, there may be options to avoid a fight."**;
  - **"Environment hazards, which may occur due to some event choices after arrival at the
    beacon, are not shown."**
  - it gates some blue options.
  So LRS reports **hazard + possible ship, for adjacent beacons only**, and neither signal is
  reliable as a fight predictor.
- **Distraction Buoys** — postpones the fleet advance at the start of a sector by one turn
  (cross-checked with [[source-fandom-rebel-fleet]]).
- **Lifeform Scanner** — the nebula workaround: enemy crew stay visible when Sensors are
  disabled (cross-checked with [[source-fandom-sensors]],
  [[source-fandom-environmental-hazards]]).
- **Damaged Stasis Pod** is documented here as a non-purchasable augment with sell price 15,
  whose only function is the Crystal Cruiser unlock sequence — relevant because the event that
  grants it is a distress-marked beacon allocated from the *neutral* lists
  ([[source-fandom-template-distress-events-by-sectors]]).
- **Scrap Recovery Arm** — +10% scrap, rounded down against the player, stacks additively;
  explicitly **does not** apply to scrap from selling items in a store, contrary to its own
  in-game description.

## Events Covered
- By reference: [[event-large-asteroid-field]], [[event-dense-asteroid-field-distress]], and
  the LRS blue-option events.

## Other Pages Touched
- [[item-long-ranged-scanners]], [[item-distraction-buoys]], [[item-lifeform-scanner]],
  [[item-damaged-stasis-pod]], [[concept-map-reveal]], [[concept-blue-options]],
  [[concept-rebel-fleet-advance]]

## Reliability Notes
`medium`. Prices and rarities are checkable against `blueprints.xml` (not done in this pass).
The LRS caveats are behavioural claims with no citation, but they are consistent with the
engine: LRS reads the beacon's assigned event, and events can change environment mid-flow.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Augmentations
- [[source-fandom-beacons]], [[source-fandom-sensors]],
  [[source-fandom-template-distress-events-by-sectors]], [[source-fandom-rebel-fleet]]
