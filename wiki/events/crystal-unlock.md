---
id: event-crystal-unlock
type: event
event_name: CRYSTAL_UNLOCK
sectors: [[[sector-hidden-crystal-worlds]]]
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-crystal-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [crystal-route, ship-unlock, quest-marker, orphan, no-choices]
---

# Crystal unlock — `CRYSTAL_UNLOCK`

## Summary
The payoff. Step **4 of 4** of [[chain-crystal-cruiser-unlock]] and the end of the Crystal
route: you find your Crystalline companion's old ship, send it home to the Federation, and
unlock the **Crystal Cruiser**. It has no choices and no risk — reaching the beacon *is*
the event.

## Trigger & Where It Appears
- **Not in any sector event list.** `CRYSTAL_UNLOCK` appears nowhere in `ITEMS_CRYSTAL`,
  `HOSTILE_CRYSTAL`, `NEUTRAL_CRYSTAL`, `QUESTS_CRYSTAL` (which is empty) or the
  `CRYSTAL_HOME` allocations in `sector_data.xml` ([[source-events-xml]],
  [[source-sector-data-xml]]).
- It is reached as a **quest marker**. On arriving in [[sector-hidden-crystal-worlds]], the
  sector's `startEvent` [[event-start-beacon-crystal]] (`START_BEACON_CRYSTAL`) fires
  `<quest event="CRYSTAL_UNLOCK"/>`, which plants the marker on your sector map; you then
  fly to it ([[source-events-xml]]).
- Fandom states the same join explicitly: *"The quest marker event in the Hidden Crystal
  Worlds is called 'CRYSTAL_UNLOCK' in the datafiles"*
  ([[source-fandom-ancient-device]]).
- Beacon: quest marker; shows **no ship** on Long-Range Scanners
  ([[source-fandom-ancient-device]]).

## Text
> You arrive at the coordinates to find a massive Crystalline cruiser docked at a small
> repair station. You arrange for the ship to be sent back to the Federation base while the
> station upgrades your hull.

(`event_CRYSTAL_UNLOCK_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _none — the event has no choice nodes_ | — | `unlockShip id="8"` → **Crystal Cruiser unlocked**; `augment name="CRYSTAL_SHARDS"` → **Crystal Vengeance**; `damage amount="-10"` → **10 hull repairs**; `autoReward level="MED"` **fuel** (Fandom: 2–4 fuel and scrap). | 100% |

Everything fires at once on arrival — there is nothing to decide and nothing that can go
wrong at this beacon. ([[source-events-xml]], [[source-fandom-ancient-device]])

The augment's blueprint id is `CRYSTAL_SHARDS`; its in-game display name is **Crystal
Vengeance** (`aug_CRYSTAL_SHARDS_title`, per raw/gamedata/text_blueprints.xml), described
as *"Every time your ship takes damage, there is a 10 percent chance to break off a shard
that flies at your enemy."* The two names are the same item — not a contradiction between
sources.

## Blue Options
- None.

## Rewards & Risks
- **Rewards:** the Crystal Cruiser unlock (ship id 8), [[item-crystal-vengeance]], 10 hull
  repairs, and 2–4 fuel with scrap.
- **Risks:** none at the beacon itself. The risk is all upstream — getting through the
  sector to reach the marker, in a sector that allocates 6–10 hostile beacons and 1–2
  boarding beacons ([[source-sector-data-xml]]).
- The Fandom page also credits this step with the **Ancestry** achievement when the chain
  is run on the Rock Cruiser ([[source-fandom-ancient-device]]).

## Strategy Notes
- Prioritise reaching this marker over farming the sector. 10 hull repairs mean you can
  afford to arrive damaged, but the Rebel fleet is still advancing and the sector's exit
  does not let you choose the next sector ([[source-fandom-ancient-device]]).
- Because the event has no `unique` attribute and is not pool-allocated, it exists solely
  as the quest target — it cannot be rolled at a random beacon.

## Related
- [[chain-crystal-cruiser-unlock]] — this is **step 4 of 4**; the chain page already
  exists and lists this event as its final step
- [[event-ancient-device]] — step 3, the wormhole into this sector
- [[event-start-beacon-crystal]] — the arrival beacon that plants this quest marker
- [[sector-hidden-crystal-worlds]] — where the marker appears
- [[item-crystal-vengeance]] — the augment awarded here

## Open Questions
- [ ] Whether the quest marker can be blocked or overwritten if you enter the sector
      without Ruwen (e.g. on the Rock Cruiser Layout C shortcut noted in
      [[chain-crystal-cruiser-unlock]]) — `START_BEACON_CRYSTAL` fires the `quest` tag
      unconditionally in the file, which suggests the marker always appears, but no source
      confirms it.
- [ ] Whether the Rebel fleet can reach and destroy the marker beacon before you do.
- [ ] Confirm ship id 8 = Crystal Cruiser against `blueprints.xml` (not yet ingested; the
      identification here rests on [[source-fandom-ancient-device]]).

## Sources
- [[source-events-xml]] (per raw/gamedata/events_crystal.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-ancient-device]] (per raw/wiki/ancient-device.md — the Fandom page for
  this event is a section of the *Ancient device* page, not a page of its own)
- raw/gamedata/text_blueprints.xml — augment display name; no source page exists for this
  file yet
