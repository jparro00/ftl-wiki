---
id: source-fandom-malfunctioning-defense-system
type: source
source_kind: wiki
raw: raw/wiki/malfunctioning-defense-system.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [distress, blue-option, cloaking-tiered, cut-content]
---

# Fandom — "Malfunctioning defense system"

## Summary
Community wiki page for `DISTRESS_SATELLITE_DEFENSE`, retrieved via the MediaWiki API at
revision 74578. Documents all five live blue options including the three Cloaking tiers, and
independently reports the commented-out Lanius option.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'DISTRESS_SATELLITE_DEFENSE' in the
  datafiles."*
- Locations: Abandoned Sector, Civilian Sector, Engi ×2, Mantis ×2, Pirate, Rock ×2,
  Uncharted Nebula, Zoltan ×2 — the widest list in this batch, matching the six
  `DISTRESS_BEACON_*` memberships including `DISTRESS_BEACON_LANIUS`.
- Lays the Cloaking tiers out as three separate blue options at levels 1 / 2 / 3 paying
  `LOW` / `MED` / `HIGH` — matching the `lvl` attributes and `max_group="0"` in the files.
  It does **not** mark the level-2 and level-3 branches as Advanced Edition content,
  although the file tags both `<!--DLC!-->`.
- **Independently reports the cut content**: *"Game code contains a blue option for a Lanius
  crewmember, but it is commented out and not available in the actual game."* The files
  confirm it, including a malformed nested comment inside the disabled block.
- **Adds a scope note the files only imply**: the Ion Weapon option accepts *any* ion-damage
  weapon including Ion Bomb and Stun Bomb, and *"missile ammo resource is not required and
  not wasted"*. The `WEAPONS_ION` blueprint list does contain `BOMB_ION` and `BOMB_STUN`.
- Its damage figure (5 hull, 1 system, 1 breach) matches the **AE** reading of the
  DLC-marked tag.

## Events Covered
- [[event-malfunctioning-defense-system]]

## Other Pages Touched
- [[item-cloaking]], [[item-ion-weapons]], [[entity-engi]], [[entity-lanius]]

## Reliability Notes
`medium`. No version stated; the damage figures and the unmarked AE Cloaking tiers both
imply Advanced Edition.

## Contradictions Flagged
None. Every outcome and reward level matches the game files; the AE-only Cloaking tiers are
recorded as a version difference on the event page rather than as a conflict.

## Links
- Source URL: https://ftl.fandom.com/wiki/Malfunctioning_defense_system
- [[source-events-xml]], [[source-autoblueprints]], [[source-dlcevents-anaerobic]], [[source-sector-data-xml]]
