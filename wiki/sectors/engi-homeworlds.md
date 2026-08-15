---
id: sector-engi-homeworlds
type: sector
sector_id: ENGI_HOME
sector_class: civilian
faction: [[[entity-engi]]]
min_sector: 2
unique: true
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-15
sources: 9
tags: [homeworld, ship-unlock]
---

# Engi Homeworlds

## Summary
The unique Engi home sector, and the only place the Stealth Cruiser quest can begin. Its pool
is [[sector-engi-controlled-sector]]'s with one guaranteed `ENGI_UNLOCK_1` beacon added and
`NEUTRAL_ENGI` shifted up by one. Not one beacon in its hostile pool is an Engi ship.

## Character & Hazards
`unique="true"` — at most one per run. `minSector="4"`-style values are **zero-indexed**, so
`minSector="2"` means the sector can first appear as the player's **sector 3**; the community
wiki states the same offset for every gated sector. ([[source-sector-data-xml]],
[[source-fandom-sectors]])

No nebula line at all, so sensors work everywhere here and nothing on the map slows the Rebel
fleet — the only fleet interaction in the pool is `ENGI_FLEET_DELAY`, which sells two jumps of
delay for two missiles.

## Event Pool

Listed in **placement order**, which is the order the game fills them and therefore a priority
ranking: lines are filled one at a time and generation stops when the map runs out of beacons.
([[source-fandom-sectors]], [[source-xftl-sector-map]])

| # | Event list | min | max | Slots placed before it |
|---|---|---|---|---|
| 1 | `ENGI_UNLOCK_1` | 1 | 1 | 0–0 |
| 2 | `STORE_ENGI` | 2 | 3 | 1–1 |
| 3 | `ITEMS` | 2 | 2 | 3–4 |
| 4 | `NOTHING_ENGI` | 1 | 2 | 5–6 |
| 5 | `ITEMS_ENGI` | 3 | 3 | 6–8 |
| 6 | `DISTRESS_BEACON_ENGI` | 1 | 3 | 9–11 |
| 7 | `QUESTS_ENGI` | 1 | 1 | 10–14 |
| 8 | `NEUTRAL_ENGI` | 5 | 7 | 11–15 |
| 9 | `HOSTILE_ENGI` | 5 | 7 | 16–22 |

Start beacon: `START_BEACON_ENGI`. The exit beacon is not in this table — it draws from the
shared `EXIT_LIST`.

The table asks for 21–29 slots against a map holding at most 24 beacons, so the shortfall
lands on `HOSTILE_ENGI` at the bottom: the low end of 5–7 is the ordinary outcome, and no line
here is ever cut outright. ([[source-xftl-sector-map]])

## Beacon Markers
The map marks a beacon as a distress signal from the event's own `<distressBeacon/>` tag, not
from which list allocated it — and in this sector the two sets disagree in both directions.

- **Marked but not allocated as distress:** [[event-dense-asteroid-field-distress]]
  (`ASTEROID_DERELICT_SHIP`), which comes from `NEUTRAL_ENGI` and carries the Damaged Stasis
  Pod. So a distress beacon here is a live candidate for the Crystal route's first step, and
  the sector can show more distress markers than its 1–3 distress allocation.
- **Allocated as distress but unmarked:** [[event-engi-ship-attacked-by-mantis-ship]]
  (`ENGI_STATION_DISTRESS`), which carries no tag and never shows the marker.

Distress and store markers only appear on beacons **adjacent** to you; the exit and quest
markers show at any range. ([[source-fandom-beacons]])

> ⚠️ **CONTRADICTION:** [[source-fandom-sectors]] NOTE 1 uses an Engi sector as its worked
> example of the extra distress marker, and explains it by saying `NEUTRAL_ENGI` is populated
> *before* `DISTRESS_BEACON_ENGI`. `sector_data.xml` orders them the other way — distress is
> line 6, neutral is line 8. The **outcome** is right (the tag shows the marker wherever the
> event lands, so the count can exceed the allocation); the **mechanism** is not. Fandom's own
> page warns that its listings do not reflect real file order.

## Chains That Run Through It
- `ENGI_UNLOCK_1` is a guaranteed beacon and the entry point to the **Stealth Cruiser**
  unlock: `ENGI_UNLOCK_1` → `ENGI_UNLOCK_2REAL` / `ENGI_UNLOCK_2FAKE` → `ENGI_UNLOCK_3` →
  `ENGI_UNLOCK_4`, ending in `unlockShip id="1"` plus the Titanium System Casing augment and
  20 hull repaired. The quest only starts through the `req="engi"` blue option; both plain
  choices end the event. ([[source-events-engi-xml]])
- The Crystal route passes through twice over: [[event-dense-asteroid-field-distress]] hands
  out the Damaged Stasis Pod and [[event-zoltan-research-facility]] converts it into a Crystal
  crew member — both in `NEUTRAL_ENGI`. See [[chain-crystal-cruiser-unlock]].

## Factions & Ships
- [[entity-engi]] — dominant faction, and never hostile in this sector's fight pool
- The hostile pool is pirates, Rebels and Mantis; the Engi hold a non-aggression pact with the
  Rebels

## Strategy Notes
- Stores are line 2, so both guaranteed shops always land. Three pool events can open a third.
- Quest markers cannot be placed on a store, a distress beacon, the exit, a visited beacon or
  a fleet-taken one, so the single `QUESTS_ENGI` beacon can fail to appear even though it is
  allocated 1–1. ([[source-xftl-sector-map]])

## Open Questions
- [x] ~~Which ship does `ENGI_UNLOCK_1` unlock?~~ The **Stealth Cruiser**, per
      `unlockShip id="1"` and `text_blueprints.xml`: *"This ship is being built near the Engi
      homeworlds. To unlock it you'll need to help them, but they only trust their own kind."*
- [x] ~~Which events populate each list.~~ Extracted — see `sectors/data/engi-homeworlds.sector.json`.
- [ ] Does `OVERRIDE_ITEMS` replace `ITEMS` here? See [[concept-sector-event-allocation]].
- [ ] The 19-beacon map floor is stated by the community wiki alone and is not derivable from
      anything in `raw/`.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
- [[source-events-engi-xml]] (per raw/gamedata/events_engi.xml)
- [[source-fandom-sectors]] (per raw/wiki/sectors.md)
- [[source-fandom-beacons]] (per raw/wiki/beacons.md)
- [[source-xftl-sector-map]] (per raw/modding/2026-08-15-xftl-sector-map.txt)
- [[source-fandom-rebel-fleet]] (per raw/wiki/rebel-fleet.md)
- [[source-fandom-stores-and-resources]] (per raw/wiki/stores-and-resources.md)
- [[source-fandom-template-distress-events-by-sectors]] (per raw/wiki/template-distress-events-by-sectors.md)
