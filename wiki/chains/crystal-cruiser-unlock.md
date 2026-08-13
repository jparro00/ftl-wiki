---
id: chain-crystal-cruiser-unlock
type: chain
trigger_event: [[[event-dense-asteroid-field-distress]]]
steps: [[[event-dense-asteroid-field-distress]], [[event-zoltan-research-facility]], [[event-ancient-device]], [[event-crystal-unlock]]]
sectors: [[[sector-rock-homeworlds]], [[sector-hidden-crystal-worlds]]]
reward: Crystal Cruiser unlock + Crystal Vengeance augment
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: [ship-unlock, crystal-route, routing-dependent]
---

# Crystal Cruiser unlock

## Summary
The four-step quest line that unlocks the Crystal Cruiser and the *Ancestry* achievement.
It is the most route-dependent chain in the game: each step is confined to particular
sector types, and they must appear **in order** along your path or the chain is dead for
that run. ([[source-fandom-ancient-device]])

## How It Starts
- Trigger: [[event-dense-asteroid-field-distress]] (`ASTEROID_DERELICT_SHIP`), a distress
  beacon in any **Engi, Pirate, or Rock** sector. Yields the Damaged Stasis Pod augment.

## Steps

1. **[[event-dense-asteroid-field-distress]]** — `ASTEROID_DERELICT_SHIP` (raw: events.xml)
   Distress beacon in an Engi / Pirate / Rock sector. Recover the **Damaged Stasis Pod**.
2. **[[event-zoltan-research-facility]]** — `ZOLTAN_CREW_STUDY` (raw: events.xml)
   Normal beacon in any **Engi or Zoltan** sector. Bring the pod here; it yields the
   Crystal crew member **Ruwen**. Guaranteed `min=1` in both
   [[sector-zoltan-controlled-sector]] and [[sector-zoltan-homeworlds]].
3. **[[event-ancient-device]]** — `ROCK_CRYSTAL_BEACON` (raw: events.xml)
   Guaranteed beacon in [[sector-rock-homeworlds]]. The Crystal-crew blue option opens a
   wormhole to [[sector-hidden-crystal-worlds]].
4. **[[event-crystal-unlock]]** — `CRYSTAL_UNLOCK` (raw: events_crystal.xml)
   Quest marker inside the Crystal sector. Awards the ship.

## Requirements
- A Crystal crew member for step 3's blue option. Any Crystal crew works for the blue
  option, but only Ruwen marks the Rock Homeworlds beacon as a quest.
- Sector routing that hits an Engi/Pirate/Rock sector, then an Engi/Zoltan sector, then
  the Rock Homeworlds — in that order. The Rock Homeworlds cannot appear before sector 4
  (`minSector="4"`, [[source-sector-data-xml]]), which sets the chain's earliest finish.
- A single Engi sector can serve steps 1 and 2 at once.
  ([[source-fandom-ancient-device]])

## Reward
- Crystal Cruiser unlocked
- [[item-crystal-vengeance]] augment
- 2–4 fuel and scrap
- 10 hull repairs
  ([[source-fandom-ancient-device]])

## Failure Modes
- The sector map doesn't offer the three sector types in the required order — the most
  common failure, and unrecoverable within a run.
- The Rebel fleet reaches a step's beacon before you do.
- Running out of fuel mid-route.

## Shortcut
Playing the Rock Cruiser Layout C (Tektite) or an already-unlocked Crystal Cruiser
starts you with Crystal crew, so step 3's blue option is available without steps 1–2 —
entering the Crystal sector without completing the chain.
([[source-fandom-ancient-device]])

## Strategy Notes
- Enemy strength inside [[sector-hidden-crystal-worlds]] scales to the Rock Homeworlds'
  sector number, so arriving deep means a harder sector.
- On exiting the Crystal sector you cannot choose the next sector — you are placed into a
  random one following the Rock Homeworlds' position.
  ([[source-fandom-ancient-device]])

## Related
- [[sector-hidden-crystal-worlds]] — the destination
- [[sector-rock-homeworlds]] — where step 3 lives
- [[entity-crystal-men]]

## Open Questions
- [ ] Confirm steps 1, 2 and 4 against the game files directly (only step 3 has been
      fully cross-checked so far).
- [ ] Exact sector-type rules for steps 1 and 2 — currently sourced only from Fandom.
- [ ] Does the Damaged Stasis Pod have any other use?

## Sources
- [[source-fandom-ancient-device]] (per raw/wiki/ancient-device.md)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
