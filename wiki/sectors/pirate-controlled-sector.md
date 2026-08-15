---
id: sector-pirate-controlled-sector
type: sector
sector_id: PIRATE_SECTOR
sector_class: hostile
faction: [[[entity-pirates]]]
min_sector: 0
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-15
sources: 16
tags: [hostile, boarders, nebula, stores]
---

# Pirate Controlled Sector

## Summary
A repeatable hostile sector available from the first sector onward (`minSector="0"`,
`unique="false"`). Its nine allocation lines ask for **16–29 event slots** against a map that
holds **at most 24 beacons**, so the bottom of the table is a wish list rather than a promise
(per [[source-sector-data-xml]], [[source-fandom-sectors]]). The largest single line is
`HOSTILE_PIRATE` at 6–8, and `BOARDERS_PIRATE` is `min=1 max=1` — a boarding encounter is
guaranteed, unlike [[sector-federation-space]] where `HOSTILE_BOARDING` is allocated 0–0.
Fandom groups it under **Hostile Sectors** (red on the map) ([[source-fandom-sectors]]).

> ⚠️ **CORRECTED CLAIM (this wiki's own, now checked):** this page previously said Pirate
> space has the "heaviest hostile allocation of the early-available sectors". It does not.
> `sector_data.xml` gives 6–8 `HOSTILE_*` slots to [[sector-federation-space]],
> [[sector-civilian-sector]], Pirate, Rebel (and Rebel Stronghold), Zoltan (and Homeworlds),
> Rock (and Homeworlds) and the Abandoned Sector alike;
> [[sector-hidden-crystal-worlds]] allocates 6–10. Pirate is **tied at the top, not ahead of it**, and the
> comparison is anyway incomplete: sectors whose fights arrive through nebula or boarding
> lists do not show up in a `HOSTILE_*` count at all (per [[source-sector-data-xml]]).

## Character & Hazards

### Allocation is a queue, not a shopping list
Beacons are laid out first — a 6×4 grid, each cell 80% likely to hold a beacon, so at most
24 — and only then are events assigned, **line by line in sector-definition order**, each
line rolling its own min–max inclusive and being filled completely before the next starts.
When the beacons run out, generation stops and the remaining lines get nothing
([[source-fandom-sectors]], [[source-xftl-sector-map]]; see
[[concept-sector-event-allocation]]).

Two consequences specific to this sector:

- **`NEBULA_PIRATE` is placed before everything else**, out of file order, because the purple
  cloud graphics have to be drawn first. Clouds that fall over ordinary beacons convert them,
  and those beacons draw from the shared `NEBULA` list rather than from any Pirate list
  ([[source-fandom-sectors]]).
- **`NEUTRAL_PIRATE` is the last line**, and at maxima only one beacon is left for a line that
  wants 5–6. The deepest pool in the sector — the one holding
  [[event-dense-asteroid-field-distress]] and its **Damaged Stasis Pod** — is the one the map
  truncates first (derived from the allocation table, [[source-sector-data-xml]]).

Leftover beacons are filled from the shared `NEUTRAL` list (`OVERRIDE_NEUTRAL` under AE), and
the **exit beacon is not in the table at all** — it draws from the shared `EXIT_LIST`, and an
exit inside a cloud is always empty ([[source-fandom-sectors]]).

### Environmental hazards in the pool
`sector_data.xml` allocates no hazard line here; the hazards ride on individual events
(counts from `sectors/data/pirate-controlled-sector.sector.json`):

| Environment | Events | Effect while you sit there |
|---|---|---|
| Asteroid field | 2 | Periodic 1-damage strikes; frequency scales with **your** shield level |
| Sun (red giant) | 2 | Solar flares start fires every 28–34s; shields reduce the effect |
| Plasma/ion storm | 3 | Reactor at half capacity (rounded up) — for you and the enemy |
| Nebula | 10 | Sensors dead; Rebel advance halved for that jump |
| Pulsar | 1, AE only | Ion pulse every 11–18s, ionising 2 systems on each ship |

Suns, asteroid fields and pulsars impose permanent **IN DANGER** status: no ship menu, so no
upgrades, no weapon or drone swaps and no crew management until you leave
([[source-fandom-environmental-hazards]]; see [[concept-hazards]]).

### The nebula line is a fleet-delay resource
This is not a nebula sector, so a nebula beacon here **halves** the Rebel advance for that
jump (50%), rather than the ~20% reduction inside a nebula sector — the reverse-engineered
figures are 64 px per jump normally against 32 px from a nebula beacon in a normal sector
([[source-fandom-environmental-hazards]], [[source-xftl-sector-map]];
[[concept-rebel-fleet-advance]], [[concept-nebula-mechanics]]). With `NEBULA_PIRATE`
allocated 0–5, that resource ranges from absent to nearly a quarter of the map.

Two events in the pool delay the fleet directly and three advance it
(`modifyPursuit`, negative = delay):

| Event | Effect |
|---|---|
| [[event-the-mercenary]] | −2 jumps, for 10–25 scrap |
| [[event-pirate-briber]] | −1 jump |
| [[event-asteroid-belt-distress]] | +1 |
| [[event-auto-ship-warning-in-nebula]] | +1 if the scout escapes |
| [[event-rebel-fight-choice-in-nebula]] | +1 if the scout escapes |

### Quest markers
`QUESTS_PIRATE` is 0–1, so the sector can plant no quest of its own — and a marker that is
planted has to find a beacon that is unvisited, not a nebula beacon, not the exit, not
Rebel-held, not already a quest, **not a store, not a distress beacon** and not your current
beacon, within fewer jumps than it takes the Rebels to reach it. If nothing qualifies the
quest is pushed to the next sector ([[source-xftl-sector-map]];
[[concept-quest-beacon-placement]]). A cloud-heavy roll here shrinks that candidate list
directly, since nebula beacons are excluded.

> ⚠️ **CONTRADICTION:** [[source-fandom-beacons]] says a quest marker overwrites any event
> "unless it is a store, exit, or another quest marker" and cannot appear "in nebula area".
> [[source-xftl-sector-map]] reads a longer filter out of `StarMap::AddQuest` — also
> excluding visited, fleet-overtaken, distress and current beacons, with the nebula exclusion
> being per beacon rather than per area. Both recorded; the engine reading is the better bet,
> and Fandom carries its own `@to-do: test and verify` on the claim.

## Beacon markers — what shows on the map before you jump

Distress and store markers are drawn on beacons **within one jump** of you, and a distress
marker persists until the Rebels take it ([[source-fandom-beacons]]). The marker comes from
the event's own `<distressBeacon/>` / `<store/>` tag, which does **not** match the allocation
line of the same name:

- **14 events in this pool show a distress marker; only 10 of them come from
  `DISTRESS_BEACON_PIRATE`.** The other 5 —
  [[event-dense-asteroid-field-distress]], [[event-giant-alien-spiders]],
  [[event-malfunctioning-defense-system]], [[event-refugee-distress]] and
  [[event-refugee-comms-down]] — all arrive through `NEUTRAL_PIRATE`.
- **Here that surplus is fragile.** `NEUTRAL_PIRATE` is the **last** line placed, so its five
  distress-marked events are exactly what gets cut when the map fills — the surplus markers
  are the least reliable part of the sector, not a bonus you can count on
  ([[source-sector-data-xml]] for the order, [[source-fandom-sectors]] for the rule).
- **One event goes the other way:** [[event-pirate-ship-attacking-civilian-distress]] is
  allocated from `DISTRESS_BEACON_PIRATE` but carries no distress tag, so it never shows the
  marker. Fandom describes this class of event as a mistake in the data
  ([[source-fandom-sectors]]).
- **Store markers:** the 1–2 guaranteed `STORE_PIRATE` beacons are labelled; the four
  event-opened shops (below) are not.

Long-Ranged Scanners add a hazard reading and a possible-ship reading for adjacent beacons
only, and never name the event ([[source-fandom-beacons]]). Fandom's distress table gives the
LRS icon per event: [[event-pirate-ship-distress-trap]],
[[event-escort-civilians-ftl-haywire]] and [[event-friendly-ship-out-of-fuel]] read as
"possible ship detected"; the rest of this sector's distress events read as a plain unvisited
location ([[source-fandom-template-distress-events-by-sectors]]).

> ⚠️ **CONTRADICTION:** [[source-fandom-sectors]] explains surplus distress beacons with an
> Engi example, saying events from `NEUTRAL_ENGI` populate the map "**before** the events from
> `DISTRESS_BEACON_ENGI`". `sector_data.xml` orders both Engi sectors the other way round —
> `DISTRESS_BEACON_ENGI` is listed before `NEUTRAL_ENGI`, exactly as Pirate space lists its
> own two. The *mechanism* still holds (distress-tagged events outside the distress line add
> markers whenever they are placed), but the ordering the explanation rests on does not.
> Trusting the game files on order; both readings recorded ([[source-sector-data-xml]]).

> ⚠️ **CONTRADICTION:** [[source-fandom-template-distress-events-by-sectors]] does **not**
> mark the Pirate column for [[event-refugee-distress-pirate]] (it marks Rebel instead), nor
> for [[event-refugee-distress]] or [[event-refugee-comms-down]]. The game files disagree on
> all three: `DISTRESS_BEACON_PIRATE` loads `REFUGEE_DISTRESS_PIRATE` directly, and
> `NEUTRAL_PIRATE` loads the shared `DISTRESS_BEACON` list which contains the other two
> ([[source-events-pirate]]). Trust the game files here — datamined files outrank the
> community wiki — but the Fandom rows are recorded, not deleted; the other 11 Pirate rows in
> that table agree with the files exactly.

## Stores
`STORE_PIRATE` is allocated **1–2**, which Fandom's guaranteed-store table matches exactly
([[source-fandom-template-stores-number-of-stores-by-sectors]], [[source-sector-data-xml]]).
That is only the *guaranteed* count. Four more events in this sector's pool can open a shop —
[[event-pirate-briber]], [[event-settlement-mercenary-work]], [[event-escort-civilians]] and
[[event-escort-civilians-ftl-haywire]] — and under Advanced Edition `OVERRIDE_ITEMS` adds
[[event-large-trade-station]] as a fifth ([[source-events-pirate]],
[[source-dlceventsoverwrite]]). Fandom's additional-stores table lists exactly these five for
the Pirate column ([[source-fandom-template-stores-additional-stores-from-events-by-sectors]]).

**So Pirate space is not the store-starved sector it looks like.** Its 1–2 guaranteed stores
are the same allotment Mantis and Rebel space get, but Mantis has only two additional
store-opening events to Pirate's five ([[source-fandom-template-stores-additional-stores-from-events-by-sectors]];
see [[concept-stores]]).

> Note: an event-generated store vanishes if you reload at it
> ([[source-fandom-stores-and-resources]]).

## Crew rarity
`PIRATE_SECTOR` declares **no `<rarityList>`** in `sector_data.xml`, so the global
`blueprints.xml` defaults apply: Human 1, Engi 2, Mantis 2, Rockman 3, Zoltan 5, Slug 0
(never randomly offered). Fandom's crew list for this sector prints exactly those values,
which is consistent rather than contradictory ([[source-sector-data-xml]],
[[source-blueprints]], [[source-fandom-sectors]]; see [[concept-blueprint-rarity]]).

## Event Pool

Allocation table in **placement** order — that is file order, except that the nebula line
jumps the queue. Totals: **16–29 slots against at most 24 beacons.**

| # placed | Event list | min | max | Notes |
|---|---|---|---|---|
| 1st | `NEBULA_PIRATE` | 0 | 5 | Placed before all others (cloud graphics); name is ambiguous, see below |
| 2nd | `STORE_PIRATE` | 1 | 2 | Guaranteed stores |
| 3rd | `ITEMS` | 1 | 2 | `OVERRIDE_ITEMS` under AE adds [[event-large-trade-station]] |
| 4th | `HOSTILE_PIRATE` | 6 | 8 | `OVERRIDE_HOSTILE_PIRATE` under AE adds a pulsar fight |
| 5th | `BOARDERS_PIRATE` | 1 | 1 | Guaranteed; at most 17 slots are placed before it |
| 6th | `DISTRESS_BEACON_PIRATE` | 1 | 2 | 9 of its 10 events also sit in `NEUTRAL_PIRATE` |
| 7th | `NOTHING_PIRATE` | 1 | 2 | Empty beacons |
| 8th | `QUESTS_PIRATE` | 0 | 1 | Can be zero |
| 9th | `NEUTRAL_PIRATE` | 5 | 6 | Filled last — where the shortfall lands |

Start beacon: `START_BEACON_PIRATE` ([[event-start-beacon-pirate]]).

The pool resolves to **66 distinct events**; the full enumeration with per-event tags, gates
and items is generated into `sectors/data/pirate-controlled-sector.sector.json` and rendered
at `sectors/sector-pirate-controlled-sector.html`.

> ⚠️ **CONTRADICTION (data, unresolved):** `NEBULA_PIRATE` and `BOARDERS_PIRATE` are each
> defined **both** as an `eventList` (in `raw/gamedata/events_pirate.xml`) and as a single
> `<event>` (`NEBULA_PIRATE` in `raw/gamedata/events_nebula.xml`, `BOARDERS_PIRATE` further
> down `events_pirate.xml`). Which one the engine resolves is not stated by any file here.
> The single `NEBULA_PIRATE` event is a plain hostile pirate with five text variants and
> **no `<environment type="nebula"/>` at all**; the single `BOARDERS_PIRATE` event is 2–4
> random-species boarders whose text is the placeholder string `SSSSSSSSSSSSSSSSS`. This wiki
> reads both as the list — the placeholder text and the missing environment tag both point
> that way — but the nebula-first placement rule makes the `NEBULA_PIRATE` ambiguity matter
> more, not less: that line is resolved before any other, for up to 5 beacons
> ([[source-events-pirate]], [[source-events-nebula]]).

## Chains That Run Through It
- **The merchant's request** — [[event-merchant-s-request]] → `MERCHANT_DELIVER` /
  `MERCHANT_INVESTIGATE` → `MERCHANT_INVESTIGATE_DELIVER`. The only multi-jump chain
  `QUESTS_PIRATE` can start, and that line is 0–1. _Chain page not yet created._
- **The escort** — [[event-escort-civilians]] and [[event-escort-civilians-ftl-haywire]] both
  feed `QUEST_ESCORT_ARRIVE`.
- **Hidden Federation base** — [[event-asteroid-belt-distress]] and
  [[event-rebel-ship-attacking-federation-loyalists]] both point at
  `HIDDEN_FEDERATION_BASE_LIST`, from outside the quest line.
- **Crystal route** — [[event-dense-asteroid-field-distress]] hands out the **Damaged Stasis
  Pod** here (`NEUTRAL_PIRATE`, the line most likely to be cut).

## Factions & Ships
- [[entity-pirates]] — dominant faction
- Rebel ships also appear: 10 of the 13 nebula-line events arrive through the shared
  `NEBULA_REBEL` list, and `HOSTILE_PIRATE` includes a Rebel auto-ship
  ([[source-events-pirate]], [[source-events-nebula]]).

## Strategy Notes
- On a full 24-beacon map, at most 23 slots are consumed before `NEUTRAL_PIRATE` even at every
  line's maximum — so the stores, the item beacon, the 6–8 fights, the boarding encounter and
  the distress beacon are all effectively promises, and the variance lives in the last two
  lines. On a smaller map the cut reaches further up (derived from [[source-sector-data-xml]]
  plus the placement rule in [[source-fandom-sectors]]).
- Nebula beacons are the only free fleet delay here, and they cost you sensors while you sit
  in them ([[source-fandom-environmental-hazards]]).
- The ten events on the distress line are the reliable distress population; the five that ride
  on `NEUTRAL_PIRATE` only reach the map if beacons are left over after everything else.
- _Opinion, unsourced beyond Fandom's own framing:_ Fandom's colour-coding commentary calls
  red sectors' danger/reward reputation misleading and recommends routing on sector knowledge
  rather than colour ([[source-fandom-sectors]]). It offers no Pirate-specific measurement.

## Open Questions
- [x] ~~Map colour / hostility classification~~ — Fandom classifies this as a **Hostile
  (red)** sector; `sector_data.xml` carries no colour field ([[source-fandom-sectors]]).
- [x] ~~Which events populate each list~~ — enumerated in
  `sectors/data/pirate-controlled-sector.sector.json` (66 distinct events) from
  [[source-events-pirate]] / [[source-events-nebula]] / [[source-newevents]].
- [ ] Cross-link all 66 pool events into `wiki/events/` pages from this page — only the
  events named above are linked so far.
- [ ] Does the engine resolve `NEBULA_PIRATE` / `BOARDERS_PIRATE` as the list or the single
  event? No file here says.
- [ ] Do the `OVERRIDE_*` lists replace their base lists under AE? Unconfirmed; see
  [[concept-sector-event-allocation]].
- [ ] What is the **minimum** beacon count on a map? Fandom says a sector has 19–24 beacons
  but sources it to an xftl teardown this repo does not hold; the 6×4 grid with an 80% fill
  chance and an anti-emptiness guard gives a ceiling of 24 and no stated floor
  ([[source-fandom-sectors]], [[source-xftl-sector-map]]).
- [ ] Is `unique="true"` scoped per sector or per run? See [[concept-event-uniqueness]].

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-fandom-sectors]] (per raw/wiki/sectors.md)
- [[source-xftl-sector-map]] (per raw/modding/2026-08-15-xftl-sector-map.txt)
- [[source-fandom-beacons]] (per raw/wiki/beacons.md)
- [[source-fandom-rebel-fleet]] (per raw/wiki/rebel-fleet.md)
- [[source-fandom-environmental-hazards]] (per raw/wiki/environmental-hazards.md)
- [[source-fandom-stores-and-resources]] (per raw/wiki/stores-and-resources.md)
- [[source-fandom-template-stores-number-of-stores-by-sectors]] (per raw/wiki/template-stores-number-of-stores-by-sectors.md)
- [[source-fandom-template-stores-additional-stores-from-events-by-sectors]] (per raw/wiki/template-stores-additional-stores-from-events-by-sectors.md)
- [[source-fandom-template-distress-events-by-sectors]] (per raw/wiki/template-distress-events-by-sectors.md)
