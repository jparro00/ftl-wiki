---
id: source-fandom-rebel-shipyard
type: source
source_kind: wiki
raw: raw/wiki/rebel-shipyard.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rebel, ship-unlock, miniboss, weapon-reward, fleet-delay]
---

# Fandom — "Rebel shipyard"

## Summary
The community wiki page for `FLAGSHIP_CONSTRUCTION`, the Rebel Stronghold miniboss and the
Federation Cruiser unlock. Retrieved via the MediaWiki API at revision 74685. Includes a
screenshot of the enemy ship and a Trivia section comparing it to the real Flagship.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'FLAGSHIP_CONSTRUCTION' in the data
  files."*
- Locations: Rebel Stronghold only. `LRSmap=noship`, `unique=true`. Matches the file — the
  event is placed directly by the `REBEL_SECTOR_MINIBOSS` sector definition, not by any
  event list.
- **Identifies the unlock:** `<unlockShip id="4"/>` is the
  **Federation Cruiser (Layout A)**, and notes it can alternatively be unlocked by winning
  the game with the Engi Cruiser.
- Records the full payout — a weapon with high scrap, +5 fuel, +5 missiles, +5 drone parts,
  and the Rebel Fleet delayed **2** turns — matching `autoReward level="HIGH"` `weapon`,
  three `item_modify` entries, and `<modifyPursuit amount="-2"/>`.
- Documents **both** win branches (`destroyed` with no text, `deadCrew` with its own text
  and a "Pillage the ship for supplies" choice) converging on the same reward event.
- **Trivia on the enemy ship:** system levels and crew count *"vary with difficulty and
  sector number"*; the layout closely matches the Flagship's Phase 3 on Hard in that the
  artillery rooms are connected to the rest of the ship regardless of the current
  difficulty; and it *"lacks the Mind Control system and the Power Surge"*.
- Categorised `Random_Events`, `Unique_Events`, `Ship_Unlocking_Events`,
  `Weapon reward opportunity`, `Rebel Fleet delay reward`, `Fuel reward`,
  `Missiles reward`, `Drone Parts reward`.

## Events Covered
- [[event-rebel-shipyard]]

## Other Pages Touched
- [[sector-rebel-stronghold]], [[entity-flagship]], [[concept-rebel-fleet-advance]],
  [[concept-ship-unlocks]]

## Reliability Notes
`medium`. Version unstated, though the event is AE-only content so the page necessarily
describes AE. Its reward accounting matches the files line for line. Its ship-behaviour
claims are play observations, not file quotes.

## Contradictions Flagged
- **"lacks the Mind Control system"** — the `BOSS_SPECIAL` blueprint does declare
  `<mind power="1" room="3" start="false"/>`. Recorded on [[event-rebel-shipyard]]; the
  `start="false"` flag is the likely reconciliation.

## Links
- Source URL: https://ftl.fandom.com/wiki/Rebel_shipyard
- [[source-events-rebel]], [[source-blueprints]], [[source-sector-data-xml]],
  [[source-text-events-xml]]
