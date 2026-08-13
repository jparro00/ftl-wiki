---
id: source-fandom-crushed-pirate
type: source
source_kind: wiki
raw: raw/wiki/crushed-pirate.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [distress, blue-option, pirate, bug-report, blueprint-scope]
---

# Fandom — "Crushed pirate"

## Summary
Community wiki page for `DISTRESS_TRAPPED_MINER`, retrieved via the MediaWiki API at
revision 74024. Its footnotes are the most useful part: they pin down exactly which weapons
and drones satisfy the two blue-option gates.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'DISTRESS_TRAPPED_MINER' in the
  datafiles."*
- Locations: Civilian Sector, Engi ×2, Mantis ×2, Pirate, Rock ×2, Uncharted Nebula;
  `distress=true`, `LRSmap=noship`, `unique=true` — matching the five `DISTRESS_BEACON_*`
  memberships.
- **Blue-option scope notes, all confirmed by `autoBlueprints.xml`:**
  - *(Beam Weapon)*: Anti-Bio Beam and Fire Beam are **excluded**; Artillery Beam **is**
    eligible. The `WEAPONS_BEAM_DAMAGE` list is exactly `BEAM_HULL`, `BEAM_3`, `BEAM_2`,
    `BEAM_1`, `BEAM_LONG`, `ARTILLERY_FED`.
  - *(Beam Drone)*: the Anti-Ship Fire Drone is **excluded**. `COMBAT_BEAM_DRONE_LIST` is
    exactly `COMBAT_BEAM` and `COMBAT_BEAM_2`.
- **Bug report**: on the Beam Drone option, *"no drone part is lost if the reward includes
  drone parts, though you still need at least 1 drone part to choose this blue option."* The
  file shows an unconditional `item_modify` of −1.
- Names the `PIRATE` enemy ship and its 50/50 surrender and escape values.
- Its damage figure — *"2 hull damage, 2 damage to a random system"* — is a clean
  demonstration that a single `<damage amount="2" system="random"/>` tag deals its amount to
  **both** hull and system.

## Events Covered
- [[event-crushed-pirate]]

## Other Pages Touched
- [[item-beam-weapons]], [[item-combat-beam-drone]], [[event-pirate-fight]],
  [[event-asteroid-belt-distress]]

## Reliability Notes
`medium`. No version stated; the fact that it lists any damage at all on the shoot branch
implies Advanced Edition — the whole damage tag is DLC-marked.

## Contradictions Flagged
None. Every outcome, gate and reward level matches the game files.

## Links
- Source URL: https://ftl.fandom.com/wiki/Crushed_pirate
- [[source-events-xml]], [[source-autoblueprints]], [[source-events-ships]], [[source-sector-data-xml]]
