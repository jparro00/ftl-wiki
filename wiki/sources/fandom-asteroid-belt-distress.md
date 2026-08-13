---
id: source-fandom-asteroid-belt-distress
type: source
source_kind: wiki
raw: raw/wiki/asteroid-belt-distress.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [distress, blue-option, quest-marker, crew-reward-chance]
---

# Fandom — "Asteroid belt distress"

## Summary
Community wiki page for `CIVILIAN_ASTEROIDS_BEACON`, retrieved via the MediaWiki API at
revision 73978. Covers all four blue options and both outcome pools, and links the Hidden
Federation Base quest through a template.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'CIVILIAN_ASTEROIDS_BEACON' in the
  datafiles."*
- Locations: Civilian Sector, Engi ×2, Pirate, Rebel ×2, Rock ×2, Uncharted Nebula;
  `distress=true`, `LRSmap=noship`, `unique=true` — matching the five `DISTRESS_BEACON_*`
  memberships.
- Groups the Defense Drone and Repair Drone options together with a shared outcome block —
  independently confirming that both `req`s load the same `CIVILIAN_ASTEROIDS_BEACON_LIST2`.
- Marks both drone options with a **−1 drone part** transaction, matching the `item_modify`
  tags.
- Its damage readings are a useful cross-check on how `<damage>` tags resolve: the
  best-rescue outcome is *"1 hull damage, 1 fire"* for a lone
  `<damage amount="1" system="room" effect="fire"/>`, confirming that a system/room damage
  tag also deals its `amount` in hull.
- Renders `modifyPursuit amount="1"` as *"Rebel Fleet pursuit is doubled for 1 jump"* — a
  more specific claim than the raw value supports. See [[concept-rebel-fleet-advance]].
- The `{{Hidden federation base}}` and `{{ReturnSurvivor}}` templates were **not expanded**
  in the retrieved text, so the quest and family-return outcomes had to be taken from the
  game files.

## Events Covered
- [[event-asteroid-belt-distress]]

## Other Pages Touched
- [[item-teleporter]], [[item-rock-plating]], [[item-defense-drone]], [[item-repair-drone]],
  [[event-crushed-pirate]]

## Reliability Notes
`medium`. No version stated; the 4-hull-plus-system figure on the drone branch implies
Advanced Edition.

## Contradictions Flagged
None on outcomes. Its location list omits [[sector-federation-space]], the same systematic
omission seen across the generic-event pages, noted rather than treated as a conflict.

## Links
- Source URL: https://ftl.fandom.com/wiki/Asteroid_belt_distress
- [[source-events-xml]], [[source-newevents]], [[source-autoblueprints]], [[source-sector-data-xml]]
