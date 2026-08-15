---
id: item-backup-battery
type: item
item_kind: system
rarity: 1
unlocks_blue: []
version: ae
first_seen: 2026-08-14
last_updated: 2026-08-14
sources: 4
tags: [system, power, advanced-edition, ion]
---

# Backup Battery

## Summary
The `battery` system, added in Advanced Edition — *"Provides a 30 second power boost to your
Reactor. Upgrading increases the boost amount."* ([[source-text-blueprints]]). Temporary power
that the reactor cannot be ionised out of.

## Stats
- Blueprint `battery` (`<systemBlueprint>`), defined **only** in [[source-dlcblueprints]] —
  Advanced Edition content.
- Power: `startPower` 1, `maxPower` **2**. Purchase cost **35** scrap; level 2 costs **50**.
- `rarity` 1.

### Behaviour
Not in the game files — from [[source-fandom-ship]]:

| | Level 1 | Level 2 |
|---|---|---|
| Bars granted | 2 | 4 |
| Duration | 30 seconds | 30 seconds |
| Cooldown | 20 seconds | 20 seconds |

- **Not halved by ion storms**, unlike reactor power — see [[concept-power-and-reactor]].
- **Hacking it is uniquely punishing:** a hack immediately forces cooldown (the temporary bars
  vanish) **and drains 2 real reactor bars** for as long as the hack lasts. It is the only
  system whose hack takes power away from the rest of the ship ([[item-hacking]]).
- Contributes 4 of the 37-bar absolute power maximum (25 reactor + 8 Zoltan + 4 battery).

## How To Get It
- **Stores** — 35 scrap ([[source-dlcblueprints]]).
- Starting system on some AE layouts. `ship_PLAYER_SHIP_ENERGY_3_desc` describes a ship that
  *"relies on its Zoltan crew and Backup Battery"* rather than a decent reactor
  ([[source-text-blueprints]]) — see [[entity-zoltan-cruiser]].
- **No event in `raw/gamedata/` grants it.** There is no `<upgrade system="battery">` anywhere
  in the event files.

## Blue Options It Unlocks
- **None.** No `req="battery"` choice exists anywhere in `raw/gamedata/` — searched across every
  event file. Like [[item-reactor]], it is a purely mechanical system with no beacon presence.

## Related Augment
`BATTERY_BOOSTER` — **Battery Charger**, *"Backup Battery's lock time is halved."*
40 scrap, `bp` 8, `rarity` 2, `<value>0.5</value>` ([[source-dlcblueprints]],
[[source-text-blueprints]]). The 0.5 presumably applies to the 20-second cooldown, giving 10 —
but no source we hold states that, and "lock time" is not a term either source defines. It has
no page of its own yet.

## Strategy Notes
- **Its case is ion resistance, not raw power.** Two bars for 30 of every 50 seconds is modest;
  two bars that an ion storm cannot halve, in a sector full of ion storms, is not.
- Level 2 doubles the bars for 50 scrap without changing duration or cooldown — an unusually
  clean upgrade.
- The hacking interaction makes it a liability against hacking ships specifically: you lose the
  temporary bars *and* two real ones.

## Related
- [[concept-power-and-reactor]] — where it sits in the power economy
- [[item-reactor]] — the power it supplements, and the one ion storms halve
- [[entity-zoltan]] — the other ion-immune power source
- [[item-hacking]] — the counter that hurts this system most
- [[concept-nebula-mechanics]] — ion storms, the reason to own it

## Open Questions
- [ ] Whether "lock time" in the Battery Charger description means the 20-second cooldown.
- [ ] Which playable layouts start with it — the ship blueprints were not examined for this page.
- [ ] Whether the 30s/20s cycle is affected by level 2 at all (both sources describe only the
      bar count changing).

## Sources
- [[source-dlcblueprints]] (per raw/gamedata/dlcBlueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-fandom-ship]] (per raw/wiki/ship.md)
- [[source-events-xml]] (per raw/gamedata/events.xml) — searched, no gates or grants
