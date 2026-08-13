---
id: source-fandom-mantis-ships-battle-for-rock-freighter
type: source
source_kind: wiki
raw: raw/wiki/mantis-ships-battle-for-rock-freighter.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rock, mantis, blue-option, drone-parts, bug-claim]
---

# Fandom — "Mantis ships battle for Rock freighter"

## Summary
Community wiki page for `ROCK_MANTIS_FREIGHTER`, retrieved via the MediaWiki API at
revision 74269. Full choice tree including both drone blue options, their drone-part
costs, and a combat note about the disabled-weapons branch.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'ROCK_MANTIS_FREIGHTER' in the
  datafiles."*
- Locations: Rock Controlled Sector, Rock Homeworlds; `LRSmap=noship`, `unique=true`.
- Confirms the reward tiers against the game files: **high** scrap with resources on the
  Repair Drone branch, **medium** on every fight-and-win branch.
- Confirms the enemy `MANTIS_ROCK_MANTIS_FREIGHTER` has no surrender and no escape
  (`|no|` in its template).
- Renders both blue options with a `{{Transaction|1|subtract_drones}}` cost, matching
  `<item_modify><item type="drones" min="-1" max="-1"/></item_modify>`.
- **Bug claim (drone part):** *"Bugged: no drone part is lost if the reward includes drone
  parts, though you still need at least 1 drone part to choose this blue option."*
  Not derivable from the XML; flagged on
  [[event-mantis-ships-battle-for-rock-freighter]].
- **Combat note not in the game files:** *"The disabled system levels serve as damage
  buffer, and the initially offline weapon can potentially be swapped to"* — i.e. the
  `status type="loss"` weapons debuff is not permanent. This is genuine added value over
  the raw data.
- Categorised `Enemy system malfunction Events` and `Drone Parts use Events`.

## Events Covered
- [[event-mantis-ships-battle-for-rock-freighter]]

## Other Pages Touched
- [[item-repair-drone]], [[item-hull-repair-drone]], [[item-drone-parts]], [[entity-mantis]]

## Reliability Notes
`medium`. No version stated. The drone-part bug claim is specific and conditional, which
makes it plausible, but it is untested here.

## Contradictions Flagged
> ⚠️ Drone-part consumption: files declare an unconditional −1; Fandom says it is not
> deducted when the reward includes drone parts. Recorded on
> [[event-mantis-ships-battle-for-rock-freighter]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Mantis_ships_battle_for_Rock_freighter
- [[source-events-rock]], [[source-text-events-xml]]
