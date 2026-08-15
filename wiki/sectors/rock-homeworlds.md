---
id: sector-rock-homeworlds
type: sector
sector_id: ROCK_HOME
sector_class: hostile
faction: [[[entity-rock-men]]]
min_sector: 4
unique: true
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-15
sources: 16
tags: [homeworld, ship-unlock, crystal-route, map-generation]
---

# Rock Homeworlds

## Summary
Unique Rock home sector, and the gateway to the Crystal route: it guarantees both the
`ROCK_CRYSTAL_BEACON` beacon ([[event-ancient-device]]) and a `ROCK_UNLOCK1` beacon
([[event-rock-unlock1]]). Fandom files it under **hostile** sectors
([[source-fandom-sectors]]), and its allocation is identical to
[[sector-rock-controlled-sector]] except for those two named beacons and one rarity value.

## Trigger & Where It Appears
- `unique="true"`, `minSector="4"` (per [[source-sector-data-xml]]).
- **`minSector` counts from zero: the earliest this sector can appear is sector 5.**
  [[source-fandom-sectors]] states "only once per game and only occurs at sector **5** or
  higher", and the same +1 offset holds for every other gated sector in the file — Engi,
  Zoltan and Mantis Homeworlds are `minSector="2"` and appear at 3+, Slug is `3` → 4+,
  Rebel Stronghold is `4` → 5+, and `FINAL` is `7` → sector 8.
- Because sector 8 is always `FINAL`, this sector can only occupy **sector 5, 6 or 7**.

> ⚠️ **CONTRADICTION (resolved, both recorded):** this page previously read the attribute
> literally — "never before sector 4" — and [[chain-crystal-cruiser-unlock]] still does.
> The raw attribute is `minSector="4"` ([[source-sector-data-xml]], raw/gamedata/sector_data.xml);
> the community wiki says sector 5 or higher ([[source-fandom-sectors]], raw/wiki/sectors.md).
> Both statements are true of different things — the file's number is zero-indexed, the
> player-facing number is not. The zero-indexed reading is the one to use in prose, because
> it agrees with Fandom on all six gated sectors at once.

## Character & Hazards
- **Weather is the second weapon.** Five of the eight events in the hostile and boarder
  pools carry an environment: `ROCK_FIGHT_ASTEROID`, `ROCK_PIRATE_ASTEROID` and
  `ROCK_BOARDERS_ASTEROID` in an asteroid field, `ROCK_PIRATE_SUN` and `ROCK_BOARDERS_SUN`
  beside a red giant (derived from the event trees, `sectors/data/rock-homeworlds.sector.json`).
- Asteroids strike periodically: each either knocks down one shield layer or deals 1 hull
  and 1 system damage to a random room, with a small chance of fire or breach. Frequency
  scales with **your own** shield system level — more shield layers means more incoming
  rocks — and they keep coming after the enemy ship is dead.
  ([[source-fandom-environmental-hazards]], see [[concept-asteroid-fields]])
- Solar flares trigger every 28–34 seconds with a 5-second warning: 1–2 fires with shields
  up, 3–6 with shields down, each affected room carrying a 33%/66% chance (one/two fires)
  of 1 hull and system damage. ([[source-fandom-environmental-hazards]],
  [[concept-solar-flares]])
- Both hazards impose permanent **IN DANGER** status while you sit at the beacon, which
  locks the ship menu — no upgrades, no cargo-bay weapon or drone swaps, no crew
  management. ([[source-fandom-environmental-hazards]], [[concept-hazards]])
- **No nebula line at all.** The sector definition allocates no `NEBULA_*` list, so no
  cloud graphics are drawn, no beacons are converted to nebula, sensors are never blacked
  out, and nothing here halves the Rebel advance — every jump costs the full 64px of
  pursuit. ([[source-sector-data-xml]]; nebula halving per [[source-fandom-rebel-fleet]] and
  [[source-xftl-sector-map]], see [[concept-rebel-fleet-advance]])
- **Crystal Lockdown Bomb rarity 2.** The `rarityList` gives `BOMB_LOCK` rarity 2 here
  against 4 in [[sector-rock-controlled-sector]] and 3 in [[sector-hidden-crystal-worlds]] —
  the lowest value it is given in any sector, i.e. this is the most likely place in the game
  to be offered one in a store. Rarity 1 is common, 5 is rare, 0 means unobtainable — and
  `BOMB_LOCK`'s base rarity in `blueprints.xml` **is** 0, so those three sector overrides are
  the only places it can be found at all.
  ([[source-sector-data-xml]], [[source-blueprints]]; rarity scale per
  [[source-fandom-stores-and-resources]], [[concept-blueprint-rarity]])
- Crew sold in stores / won as crew-kill rewards: Rockman (1), Human (2), Zoltan (3). Engi,
  Mantis and Slug are set to 0 and cannot appear. ([[source-sector-data-xml]], corroborated
  by [[source-fandom-sectors]])
- Soundtrack: `rock`, `wasteland`. ([[source-sector-data-xml]], [[source-fandom-sectors]])

## Event Pool

The table below is in **file order, which is placement order** — the generator fills each
line completely, in this sequence, and stops when the map runs out of beacons
([[source-fandom-sectors]], [[source-xftl-sector-map]], see
[[concept-sector-event-allocation]]).

| # | Event list | min | max | Note |
|---|---|---|---|---|
| 1 | `ROCK_CRYSTAL_BEACON` | 1 | 1 | [[event-ancient-device]] — placed before anything else |
| 2 | `ROCK_UNLOCK1` | 1 | 1 | [[event-rock-unlock1]] |
| 3 | `STORE_ROCK` | 2 | 2 | |
| 4 | `NOTHING_ROCK` | 2 | 3 | |
| 5 | `DISTRESS_BEACON_ROCK` | 1 | 2 | |
| 6 | `HOSTILE_ROCK` | 6 | 8 | |
| 7 | `BOARDERS_ROCK` | 1 | 2 | |
| 8 | `ITEMS` | 1 | 2 | AE adds `STORE_REBELSIDE` via `OVERRIDE_ITEMS` (unconfirmed) |
| 9 | `QUESTS_ROCK` | 0 | 1 | `min="0"` — this line can place nothing |
| 10 | `NEUTRAL_ROCK` | 7 | 8 | last, so it absorbs the shortfall |

Start beacon: `START_BEACON_ROCK`. Exit beacons are **not** in this table — they draw from
the shared `EXIT_LIST` ([[source-fandom-sectors]], [[concept-start-beacons]]). The lists
themselves are defined in `events_rock.xml` and `events.xml` ([[source-events-rock]],
[[source-events-xml]]); the per-event tags used below come from the extracted event trees.

**Totals: 22–30 allocated slots against a map of at most 24 beacons.** The allocation is
not the number of stops: the map is a 6×4 grid where each cell has an 80% chance of holding
a beacon, giving 24 as the ceiling, and generation stops the moment the beacons run out
([[source-fandom-sectors]], [[source-xftl-sector-map]]). On a full 24-beacon map everything
above `NEUTRAL_ROCK` can consume at most 22 slots, which makes the neutral line the only one
that can be cut short — and it is cut whenever the lines above it roll high.

> Note: `ROCK_CRYSTAL_BEACON` and `ROCK_UNLOCK1` are referenced here as if they were
> event lists, but both are defined as single `<event name=...>` entries, not
> `<eventList>`s — the sector generator accepts either. Sitting first and second in the
> queue, both are effectively guaranteed.

> ⚠️ **CONTRADICTION — is there a beacon floor?** [[source-fandom-sectors]] opens by
> stating a sector contains "between 19 and 24 beacons", but the generation model it
> describes later is 24 cells at 80% each, with only a vague guard against too many empty
> cells; [[source-xftl-sector-map]] gives that guard as "if at least one empty cell already
> exists and empties are at least 20% of the cells placed so far, the cell is filled
> anyway", and concludes the count is "bounded, not fixed". The two are compatible — the
> guard is presumably what produces the 19 — but no source in `raw/` states the floor as a
> rule. The generated sector pages therefore derive their "may be cut" flags from the **24
> ceiling only**, which makes them optimistic: at 19 beacons even this sector's *minimum*
> 22-slot allocation cannot fit.

## Beacon Markers

What the map shows before you jump is driven by the `<distressBeacon/>` and `<store/>` tags
on the **event**, not by which allocation line it came from
([[source-fandom-sectors]] NOTE 1, [[source-fandom-beacons]]).

- **11 events in this pool carry the distress tag:** `ASTEROID_DERELICT_SHIP`,
  `CIVILIAN_ASTEROIDS_BEACON`, `DISTRESS_INFESTATION`, `DISTRESS_SATELLITE_DEFENSE`,
  `DISTRESS_STATION_DISEASE`, `DISTRESS_STATION_FIRE`, `DISTRESS_TRAPPED_MINER`,
  `ESCORT_BEACON`, `FRIENDLY_BEACON`, `STRANDED_BEACON`, `TRAP_BEACON`.
  [[source-fandom-template-distress-events-by-sectors]] lists **exactly these 11** in its
  Rock column — an independent, complete confirmation of the tag-derived set.
- **Marked but not allocated from the distress line:** `ASTEROID_DERELICT_SHIP`
  ([[event-dense-asteroid-field-distress]]), which lives in `NEUTRAL_ROCK`. This is the
  event [[source-fandom-sectors]] uses as its worked example of why a sector shows more
  distress beacons than its table says.
  > ⚠️ **CONTRADICTION — the mechanism does not transfer.** Fandom's explanation is that
  > the neutral line is filled *before* the distress line (true in Engi sectors, where
  > `NEUTRAL_ENGI` precedes `DISTRESS_BEACON_ENGI`). In `ROCK_HOME` the order is reversed:
  > `DISTRESS_BEACON_ROCK` is filled **fifth** and `NEUTRAL_ROCK` **last**
  > ([[source-sector-data-xml]]). The *outcome* still holds — an extra distress marker can
  > appear — but here it depends on beacons surviving to the last line, not on the neutral
  > line jumping the queue.
- **Allocated from the distress line but carrying no distress tag,** so they never show a
  marker: `PIRATE_CIVILIAN_BEACON` and `REBEL_VS_FEDERATION`. Fandom calls this class of
  mismatch a mistake in the data ([[source-fandom-sectors]]).
- **Long-Ranged Scanners at a distress beacon:** of the 11, only `ESCORT_BEACON`,
  `FRIENDLY_BEACON` and `TRAP_BEACON` read as "possible ship detected"; the other eight,
  including `ASTEROID_DERELICT_SHIP`, read as a plain unvisited location.
  ([[source-fandom-template-distress-events-by-sectors]], see [[concept-map-reveal]])
- **Distress and store markers are only drawn within 1 jump** of your position; the exit is
  visible from the start. Neither named beacon is marked at all — unless you carry **Ruwen**,
  the Crystal crew member from the stasis pod, which turns the [[event-ancient-device]]
  beacon into a quest marker ([[source-fandom-beacons]], [[source-fandom-ancient-device]]).

## Quest Markers

Nine events in this sector plant a quest marker: the five in `QUESTS_ROCK`, three in
`DISTRESS_BEACON_ROCK` (`CIVILIAN_ASTEROIDS_BEACON`, `ESCORT_BEACON`, `REBEL_VS_FEDERATION`),
and `ROCK_UNLOCK1` — so the `QUESTS_ROCK` count of 0–1 badly understates how many quests the
sector can start ([[source-fandom-sectors]] NOTE 1; counts derived from
`sectors/data/rock-homeworlds.sector.json`).

Where a marker may land (`StarMap::AddQuest`, per [[source-xftl-sector-map]], see
[[concept-quest-beacon-placement]]): the beacon must be unvisited, not a nebula beacon, not
the exit, not fleet-overtaken, not already a quest, **not a store**, **not a distress
beacon**, not your current beacon, and reachable — and, unless carried over from a previous
sector, closer to you than the number of jumps before the Rebels take it. Two consequences
specific to this sector:

- The two guaranteed stores and every distress-marked beacon are permanently ineligible, so
  the pool of legal targets is smaller than the map — and nothing can overwrite the
  stasis-pod beacon. That last point holds only on the engine reading:
  [[source-fandom-beacons]]'s shorter list of exclusions ("a store, exit, or another quest
  marker") does not mention distress beacons at all. See [[concept-quest-beacon-placement]].
- **If this sector comes up seventh**, a marker with nowhere to go is *dropped* rather than
  deferred — quests are not carried into sector 8 ([[source-fandom-beacons]],
  [[source-xftl-sector-map]]). Since the sector can only be 5, 6 or 7, that is a live case.

> ⚠️ **CONTRADICTION — are homeworld unlock quests guaranteed?**
> [[source-fandom-beacons]] says quest beacons are not guaranteed to exist "except for the
> special ship-unlocking quests in the Homeworlds sectors". `AddQuest` as described by
> [[source-xftl-sector-map]] contains no exemption for them — a homeworld unlock marker is
> filtered like any other. What *is* certain from the files is that the `ROCK_UNLOCK1`
> **beacon** is guaranteed (`min="1"`, second in the queue,
> [[source-sector-data-xml]]); whether its follow-up marker always finds a home is not
> established. Reliability favours the engine reading.

## Stores

- **2 guaranteed stores**, fixed (`min=max=2`) and third in the fill order, so they always
  land. [[source-fandom-template-stores-number-of-stores-by-sectors]] independently lists
  Rock sectors at 2, with no nebula stores.
- Three events in the pool can open a store on top of that: `ESCORT_BEACON`,
  `MERCENARY_WORK_START` and `QUEST_ESCORT` (derived from the event trees). None of them is
  store-marked on the map in advance. `ESCORT_BEACON` is the only one of the three that sits
  in a line which always places (`DISTRESS_BEACON_ROCK`), and it hides behind a **distress**
  marker, reading as "possible ship detected" on Long-Ranged Scanners
  ([[source-fandom-template-distress-events-by-sectors]]) — the other two are in
  `QUESTS_ROCK`, which can place nothing.
- [[source-fandom-template-stores-additional-stores-from-events-by-sectors]] lists five
  entries in its Rock column: Escort civilians, Escort civilians FTL haywire, Settlement
  mercenary work, **Large trade station**, and Pirate briber marked grey — grey meaning
  filler/exit-beacon only, and indeed `PIRATE_BRIBER` appears in none of this sector's
  lists ([[source-sector-data-xml]]). Of the four plain entries, three are exactly the
  tag-derived openers above; the fourth, Large trade station, reaches this sector only
  through `OVERRIDE_ITEMS` — see below.
- `STORE_REBELSIDE` (Large trade station) is in this sector's pool **only** through the AE
  `OVERRIDE_ITEMS` list ([[source-dlceventsoverwrite]]). Fandom listing it as a
  non-grey store-opening event for Rock sectors is therefore weak evidence that the
  `OVERRIDE_*` lists really do substitute under AE — the open question in
  [[concept-sector-event-allocation]]. Not conclusive: Fandom does not say which list it
  came from.
- Hull repair cost is set by the sector number ([[source-fandom-stores-and-resources]]),
  and this sector is never earlier than 5 — so its repairs are priced at the deep end of the
  run, in a sector whose asteroids and flares damage hull outside of combat.

## Chains That Run Through It
- [[chain-crystal-cruiser-unlock]] — [[event-ancient-device]] is step 3, and this sector is
  the only place it exists. Step 1 (`ASTEROID_DERELICT_SHIP`, the Damaged Stasis Pod) is
  *also* in this sector's `NEUTRAL_ROCK` pool, but step 2 ([[event-zoltan-research-facility]],
  which converts the pod into the Crystal crew member) is not — so a pod picked up here
  cannot be cashed in before the device, and the route is dead for that run.
- [[chain-rock-cruiser-unlock]] — starts at the guaranteed `ROCK_UNLOCK1` beacon and
  unlocks ship id 6, paying out **Rock Plating**, which is itself a blue option at three
  beacons in this sector's pools.
- [[chain-rock-bride]] — `ROCK_QUEST_MARRIAGE_START`, from the `QUESTS_ROCK` line.

## Factions & Ships
- [[entity-rock-men]] — dominant faction; every ship in `HOSTILE_ROCK` is Rock.

## Strategy Notes
- The two named beacons are the whole reason to route here; everything else the sector
  offers, [[sector-rock-controlled-sector]] offers identically.
  _(Derived from the allocation table, not from a strategy source.)_
- Fandom's own advice is that sector colour is a poor danger signal and that sectors should
  be judged individually, with store count called out as the important difference — that
  reasoning is presented as opinion plus a linked Reddit dataset, not as measured data.
  ([[source-fandom-sectors]] — **opinion**)
- With no nebula beacons available, this sector offers no way to slow the fleet by routing;
  the only pursuit modifiers left are events and the Distraction Buoys augment.
  ([[source-fandom-rebel-fleet]], [[concept-rebel-fleet-advance]])

## Related
- [[sector-rock-controlled-sector]] — same pools, same numbers, no named beacons, and
  `BOMB_LOCK` at rarity 4 instead of 2
- [[sector-hidden-crystal-worlds]] — where [[event-ancient-device]] leads
- [[concept-sector-event-allocation]], [[concept-quest-beacon-placement]],
  [[concept-hazards]], [[concept-blueprint-rarity]]

## Open Questions
- [x] ~~What does `ROCK_UNLOCK1` lead to after the initial encounter?~~ — mapped in
  [[chain-rock-cruiser-unlock]].
- [x] ~~Which events populate the ordinary lists.~~ — all ten lines are extracted; see
  `sectors/data/rock-homeworlds.sector.json` and the generated profile at
  `sectors/sector-rock-homeworlds.html`.
- [ ] What is the actual beacon **floor**? The "19–24" figure is second-hand from an xftl
  document this repo does not hold, and the derived at-risk flags ignore it.
- [ ] Does `OVERRIDE_ITEMS` really replace `ITEMS` here under AE? Fandom's store table hints
  yes; nothing in `raw/gamedata/` states it.
- [ ] Is a Homeworlds ship-unlock quest marker exempt from the `AddQuest` filter, as
  [[source-fandom-beacons]] implies?
- [ ] How often does the `NEUTRAL_ROCK` line actually get cut short — i.e. what is the real
  probability of `ASTEROID_DERELICT_SHIP` appearing here at all?

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-sectors]] (per raw/wiki/sectors.md)
- [[source-fandom-beacons]] (per raw/wiki/beacons.md)
- [[source-fandom-rebel-fleet]] (per raw/wiki/rebel-fleet.md)
- [[source-fandom-environmental-hazards]] (per raw/wiki/environmental-hazards.md)
- [[source-fandom-stores-and-resources]] (per raw/wiki/stores-and-resources.md)
- [[source-fandom-template-stores-number-of-stores-by-sectors]] (per raw/wiki/template-stores-number-of-stores-by-sectors.md)
- [[source-fandom-template-stores-additional-stores-from-events-by-sectors]] (per raw/wiki/template-stores-additional-stores-from-events-by-sectors.md)
- [[source-fandom-template-distress-events-by-sectors]] (per raw/wiki/template-distress-events-by-sectors.md)
- [[source-xftl-sector-map]] (per raw/modding/2026-08-15-xftl-sector-map.txt)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-fandom-ancient-device]] (per raw/wiki/ancient-device.md)
