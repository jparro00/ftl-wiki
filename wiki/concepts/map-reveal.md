---
id: concept-map-reveal
type: concept
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
related_events: []
tags: [mechanics, information, sensors, routing, rare-effect]
---

# Map reveal — `<reveal_map/>`

## Definition & Context

`<reveal_map/>` uncovers the sector map. It is a **rare effect — 16 uses** across the entire
event corpus ([[source-events-xml]] and siblings), which puts it in the same bracket as
`<fleet>` (16) and just above `<unlockShip>` (12).

It takes no attributes. There is no partial reveal and no radius: the tag is present or it is
not.

## Why 16 uses is the interesting number

Information is the scarcest commodity in FTL. You choose a route through a sector without
knowing what most beacons hold, and the fleet advances while you find out. A full map reveal
converts that guess into a plan — and the game hands it out **sixteen times in four hundred and
sixty events**.

Compare the two ways the game normally sells you information:

| Source | What you get |
|---|---|
| [[item-long-ranged-scanners]] | ship presence / no ship presence, per beacon — and both readings are unreliable |
| `<reveal_map/>` | the whole sector layout |

The augment is the reliable-but-shallow option; the event effect is deep and rare.

## Where it comes from

Overwhelmingly from **automated ships and stations** — the reveal is thematically salvaged
data, not a gift:

- [[event-auto-ship-near-sensor-station]] (`AUTO_DEFENSE_MAP`) — the archetype: a map-reveal
  beacon guarded by an auto-ship. Fight it, or take one of two blue options.
- [[event-deactivated-auto-ship]] (`BROKEN_REBEL_DRONE`) — the gamble: loot it safely for low
  scrap, or risk reactivating it for scrap **and** the map.
- [[event-federation-deserters]] — paying off a hidden Federation warship reveals the map.
- [[event-battlefield-wreckage]] — one of the few events that pays off [[item-sensors]].

## Implications For Play

- **It is worth more early in a sector than late.** A revealed map lets you plan the route to
  the exit around the fleet; revealed after you have already committed, it tells you what you
  missed.
- **It is worth more in a nebula sector**, where sensors do not function and the fleet is
  slower — you have both more need for the information and more time to use it. See
  [[concept-nebula-mechanics]].
- **It pairs badly with [[item-long-ranged-scanners]]** in the sense that the augment's value
  drops once the map is known — the one genuinely redundant combination in the information
  economy.

## Where It Applies
The four events above, plus the remaining `<reveal_map/>` sites across the auto-ship and
station families. Event pages that grant it note it under Rewards.

## Related
- [[item-long-ranged-scanners]] — the augment version, and its two unreliable readings
- [[item-sensors]] — the system, and the blue options that gate on it
- [[concept-nebula-mechanics]] — where information is scarcest
- [[event-auto-ship-near-sensor-station]], [[event-deactivated-auto-ship]]
- [[concept-rebel-fleet-advance]] — what a good route is worth

## Open Questions
- [ ] Whether `<reveal_map/>` reveals beacon *contents* or only the map topology. No source in
      this repo says which, and the difference is large.
- [ ] Whether the reveal persists into the next sector (almost certainly not — the map is
      per-sector — but nothing states it).
- [ ] Whether it interacts with [[item-long-ranged-scanners]]' `LRSmap` flag, which appears
      nowhere in `raw/gamedata/`.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-rebel]] (per raw/gamedata/events_rebel.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
