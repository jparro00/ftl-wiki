---
id: item-long-ranged-scanners
type: item
item_kind: augment
rarity: 1
unlocks_blue: [[[event-engi-monster]], [[event-engi-research-station]], [[event-no-fuel-prepare-to-dock]], [[event-nebula-lost-ship]], [[event-rebel-fight-chance-in-nebula]], [[event-destroyed-cargo-ship]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-13
sources: 8
tags: [augment, information]
---

# Long-Ranged Scanners

## Summary
The `ADV_SCANNERS` augment — *"Adds additional info about nearby Beacons on the star map."*
([[source-text-blueprints]]). Six events accept it as a substitute for a levelled
[[item-sensors]] subsystem, which is the largest blue-option footprint of any augment in the
game.

## Stats
- Blueprint `ADV_SCANNERS` (`<augBlueprint>`), [[source-blueprints]].
- Cost: **30** scrap — the joint cheapest augment in the file, level with `FTL_JAMMER` and
  [[item-damaged-stasis-pod]]. `bp` 3, `rarity` 1.
- `<stackable>false</stackable>`. No `<value>` — it has no scaling parameter.

## How To Get It
- **Stores** and random `autoReward` augment payouts (`FREE_AUG`, `FREE_AUGMENT`, `RANDOM_GIFT` and similar generic pools name no specific blueprint, so they cannot be attributed to one augment).
- No event in `raw/gamedata/` awards `ADV_SCANNERS` by name.

## Blue Options It Unlocks
- [[event-engi-monster]] — `ENGI_MONSTER` — the same choice list also offers [[item-sensors]] `lvl="3"`
- [[event-engi-research-station]] — `DISTRESS_ENGI_REACTOR` — alongside Sensors `lvl="2"`
- [[event-no-fuel-prepare-to-dock]] — `FUEL_APPROACH` — alongside Sensors `lvl="3"`
- [[event-nebula-lost-ship]] — `NEBULA_LOST_SHIP`
- [[event-rebel-fight-chance-in-nebula]] — `NEBULA_REBEL_CHASE` — alongside Sensors `lvl="3"`
- [[event-destroyed-cargo-ship]] — `FLOATING_CARGO` — alongside Sensors `lvl="2"`
- `HIDDEN_FEDERATION_BASE_LIST` also carries an `ADV_SCANNERS` gate. That list has no page
  of its own; its members are documented on [[event-encrypted-federation-signal]] and
  [[event-asteroid-belt-distress]]. ([[source-events-xml]])

## What It Shows On The Star Map
The blueprint text — *"Adds additional info about nearby Beacons"* — never says what info.
[[source-fandom-random-events]] supplies the answer from the community side: every event is
categorised as **having ship presence or having no ship presence at a beacon**, and that
annotation is what Long-Ranged Scanners (or a map reveal) surfaces. It is the `LRSmap` field
carried on every per-event Fandom page in `raw/wiki/` — `LRSmap=noship` or `LRSmap=ship`.

Two caveats come stated on the source, and both matter more than the feature itself:

- **"No ship presence" does not guarantee the absence of a hostile ship**, *"including a
  potential forced fight."* A clean-looking beacon can still open with combat.
- **"Possible ship detected" can point at a friendly or neutral ship** — it is not a warning.

So the augment narrows the odds; it does not scout the beacon. Note that `LRSmap` is a
**wiki field, not a game attribute** — the string appears nowhere in `raw/gamedata/`, so the
underlying flag is either derived by the community from the event's contents or read from the
binary. Which of those it is remains unknown.

## Strategy Notes
- Five of its six gates sit on the same choice list as a Sensors gate demanding level 2 or
  3. At 30 scrap the augment is cheaper than the two Sensors upgrades it stands in for
  (25 + 40 = 65 scrap) and does not need the subsystem installed at all.
- `NEBULA_LOST_SHIP` is the one beacon where it opens a choice that Sensors alone does not.
- Ships with no Sensors subsystem at all — the Slug cruisers — get the most out of it.

## Related
- [[item-sensors]] — the subsystem it substitutes for at five beacons
- [[item-adv-scanners]] — alias page under the blueprint id
- [[item-lifeform-scanner]] — the other AE scanning augment, different `req`
- [[concept-stores]] — store beacons read as `LRSmap=noship`, so the augment cannot find you
  a store

## Open Questions
- [x] ~~Exactly what "additional info about nearby Beacons" shows~~ — **answered** by
      [[source-fandom-random-events]]: ship presence / no ship presence per beacon, with both
      readings unreliable in the ways described above. Still not in `raw/gamedata/`; the
      answer is community-sourced, `reliability: medium`.
- [ ] Is the ship-presence flag derived from the event's contents, or read from the binary?
      `LRSmap` exists only on the Fandom pages, not in the game files.
- [ ] Does the augment show anything *beyond* ship presence — hazards, store markers, beacon
      type? No source says either way.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml)
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
