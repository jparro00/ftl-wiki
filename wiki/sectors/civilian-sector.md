---
id: sector-civilian-sector
type: sector
sector_id: CIVILIAN_SECTOR
sector_class: civilian
faction: []
min_sector: 0
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-15
sources: 12
tags: []
---

# Civilian Sector

## Summary
The generic friendly sector, and the one that most clearly shows the gap between what a
sector *allocates* and what a sector *places*. Its pool is Federation Space's with the store,
item, nebula and quest allocations turned up — but it asks for up to 32 beacon slots on a map
that holds at most 24, so the bottom of its table (`QUESTS`, then `HOSTILE1`) is a wish list
rather than a promise. (per [[source-sector-data-xml]], [[source-fandom-sectors]])

## Character & Hazards
`unique="false"`, `minSector="0"` — it can repeat and can appear anywhere in a run. Its track
list (`civilian`, `cosmos`, `milkyway`, `lostship`) is identical to
[[sector-federation-space]]'s. (per [[source-sector-data-xml]])

Crew rarity, which governs what stores stock and what a crew kill can drop: Human 1, Engi and
Mantis 2, Rockmen 3, Zoltan 5 — the same table Fandom gives for Federation Space and the
Pirate and Rebel sectors. `sector_data.xml` declares **no `rarityList`** for this sector, so
that table is community-sourced only.
(per [[source-fandom-sectors]], [[source-fandom-stores-and-resources]])

Two to three **guaranteed** stores — the joint-highest allocation among the 19 playable
sectors, tied with [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]] and
[[sector-hidden-crystal-worlds]], all at 2–3. Fandom's store table agrees: Civilian 2–3, with
no sector above it. (The only `STORE 2–4` lines in the XML belong to `DEEP_SPACE_SECTOR` and
`ABANDONED_SECTOR`, which document no playable sector — see [[sector-vestigial-definitions]].)
"Guaranteed" is the operative word: it counts the `STORE` line only, never the shops that
events open. (per [[source-fandom-template-stores-number-of-stores-by-sectors]],
[[source-fandom-stores-and-resources]], [[source-sector-data-xml]])

`NEBULA` at 0–8 is the widest nebula allocation of any sector that is not a nebula sector
(Zoltan 2–6; Pirate and Rebel 0–5). (per [[source-sector-data-xml]])

> **Correction, 2026-08-15.** This page previously read: *"More stores (2–3) and more item
> beacons (2–3) than any other non-home sector."* The store half is an overstatement —
> [[sector-engi-controlled-sector]] is also 2–3 — and the item half is simply wrong:
> the Engi sectors allocate `ITEMS` 2 **plus** `ITEMS_ENGI` 3, five item beacons, and
> [[sector-abandoned-sector]] allocates `ITEM_LANIUS` 2–4. The old claim is kept here
> rather than deleted, per the wiki's no-overwrite rule.
> (per [[source-sector-data-xml]], [[source-fandom-template-stores-number-of-stores-by-sectors]])

## Event Pool

Kept in **file order**, which is also placement order: the generator fills each line
completely, in this sequence, and stops when the map runs out of beacons.
(per [[source-fandom-sectors]])

| # | Event list | min | max | Notes |
|---|---|---|---|---|
| 1 | `STORE` | 2 | 3 | resolves to the single `STORE` event, not a list |
| 2 | `ITEMS` | 2 | 3 | AE delta adds `STORE_REBELSIDE` via `OVERRIDE_ITEMS` |
| 3 | `NEUTRAL_CIVILIAN` | 2 | 4 | one of its ten entries is the whole `DISTRESS_BEACON` list |
| 4 | `NOTHING` | 1 | 2 | |
| 5 | `DISTRESS_BEACON` | 1 | 2 | |
| 6 | `HOSTILE_CIVILIAN` | 4 | 6 | |
| 7 | `NEBULA` | 0 | 8 | see the placement-order contradiction below |
| 8 | `QUESTS` | 0 | 2 | **at risk** — can be cut entirely; AE delta adds `QUEST_CONSTRUCTIONYARD` |
| 9 | `HOSTILE1` | 2 | 2 | **at risk** — AE delta adds `REBEL_PULSAR`, `PIRATE_PULSAR` |

`HOSTILE_BOARDING min=0 max=1` is present in the XML but **commented out**, so this sector
places no boarding beacon by this table. (per [[source-sector-data-xml]];
see [[concept-sector-event-allocation]] for the parallel `<eventCounts>` scheme that
allocates it 1–2 regardless)

Totals: 14–32 allocated slots against a map of at most 24 beacons. Roll low and the leftover
beacons are filled from the shared `NEUTRAL` list (`OVERRIDE_NEUTRAL` under Advanced
Edition); roll high and the last lines never happen. The exit beacon is not in this table at
all — it draws from the shared `EXIT_LIST`. (per [[source-fandom-sectors]])

No `startEvent` is declared. The line exists in the XML but is commented out, tagged
`JUSTIN TO DO`, and the event it names — `START_BEACON_CIVILIAN` — appears **nowhere else in
`raw/gamedata/`**: it was never written. Whether the engine falls back to `START_BEACON` is
still unknown. (per [[source-sector-data-xml]], [[concept-start-beacons]])

## Beacon Markers — what the map shows before you jump
Distress and store markers are drawn on beacons **adjacent** to you, so they are a next-jump
signal, not a sector plan. (per [[source-fandom-beacons]])

- **12 events** in this pool carry the distress tag and so show the marker; five of them can
  cost a crew member (`DISTRESS_INFESTATION`, `DISTRESS_STATION_DISEASE`,
  `DISTRESS_STATION_FIRE`, `REFUGEE_GHOST`, `STRANDED_BEACON`).
- **More distress markers can appear than the 1–2 the `DISTRESS_BEACON` line pays for.**
  `NEUTRAL_CIVILIAN` contains `DISTRESS_BEACON` as one of its ten entries and is filled
  first, so a neutral roll can produce a distress beacon. This is exactly the mechanism
  [[source-fandom-sectors]] NOTE 1 describes for Engi sectors, occurring here through list
  nesting rather than through a stray tag. (per [[source-newevents]])
- **Two events go the other way**: `PIRATE_CIVILIAN_BEACON` and `REBEL_VS_FEDERATION` are
  drawn from `DISTRESS_BEACON` but carry no `<distressBeacon/>` tag, so they never show the
  marker. Fandom calls this class of mismatch a mistake in the data.
  (per [[source-fandom-sectors]], [[source-fandom-template-distress-events-by-sectors]])
- **Stores**: four events in the pool can open a shop on top of the guaranteed ones —
  [[event-pirate-briber]], [[event-settlement-mercenary-work]], [[event-escort-civilians]]
  and [[event-escort-civilians-ftl-haywire]] — plus [[event-large-trade-station]] from the
  AE `OVERRIDE_ITEMS` delta. Fandom's additional-stores table lists exactly those five for
  Civilian. (per [[source-fandom-template-stores-additional-stores-from-events-by-sectors]])

## Quest Beacons — the concrete case of NOTE 1
[[source-fandom-sectors]] NOTE 1 states that a "quest" beacon *"might not even exist on the
map, because all beacons may have been filled by other events already"*. This sector is that
case in the data: `QUESTS` is allocated **0–2** and sits second-from-last in a table whose
maximum exceeds the map, so it is flagged at risk by every reading.

Two further constraints compound it:

- **Nine events** in this sector's pool plant a quest marker, against a `QUESTS` line of
  0–2 — quests here mostly do not come from the quest line at all. (per
  `sectors/data/civilian-sector.sector.json`, derived from the event trees)
- A marker needs a legal destination beacon. `StarMap::AddQuest` rejects beacons that are
  visited, nebula, exit, fleet-overtaken, already-quested, store, distress, or the player's
  current beacon, and requires the destination to be fewer jumps away than the Rebels are
  from taking it. A Civilian Sector can carry eight nebula beacons and three stores, which
  strips the candidate pool further; with no legal beacon, the quest is pushed into the next
  sector — or dropped outright from sector 7 on. (per [[source-xftl-sector-map]],
  [[source-fandom-beacons]], [[concept-quest-beacon-placement]])

## Nebula Effects
With up to 8 nebula beacons this is a non-nebula sector that can play like one:

- Sensors are disabled at a nebula beacon; Slug crew or a Lifeform Scanner still see enemy
  crew. (per [[source-fandom-environmental-hazards]])
- The Rebel advance is **halved** for that jump — the full 50% reduction, because this is not
  a nebula sector. (per [[source-fandom-environmental-hazards]],
  [[source-fandom-rebel-fleet]], [[source-xftl-sector-map]])
- Plasma/ion storm beacons halve the reactor on arrival; power is stripped automatically
  unless you jump in with spare. (per [[source-fandom-environmental-hazards]])
- Nebula beacons **never carry an ASB**, and a nebula beacon taken by the fleet always
  becomes an ion storm. (per [[source-fandom-rebel-fleet]],
  [[source-fandom-environmental-hazards]])
- An exit beacon that ends up inside cloud graphics is always an empty event.
  (per [[source-fandom-sectors]])

## Chains That Run Through It
- **Hidden Federation base** — three events in the pool plant `HIDDEN_FEDERATION_BASE_LIST`:
  [[event-asteroid-belt-distress]], [[event-rebel-ship-attacking-federation-loyalists]] and
  [[event-encrypted-federation-signal]]. _Chain page not yet created._

## Factions & Ships
- _Unfactioned._ The hostile pools are pirates, Rebels, auto-ships and one Mantis fight.

## Strategy Notes
- The store count is the one number here that cannot be starved: `STORE` is the first line
  filled. Everything below it is contingent. (per [[source-fandom-sectors]])
- Fandom's own routing advice — that green sectors are not automatically safe and that
  "one important difference between sectors is the number of stores they contain" — is
  presented as reasoning plus a linked Reddit dataset, not as measured data. _Marked as
  opinion._ (per [[source-fandom-sectors]])

## Contradictions

> ⚠️ **CONTRADICTION — where the `NEBULA` line is actually processed.**
> [[source-fandom-sectors]] states the rule as *"all the event lists starting with `NEBULA_`
> are processed first, regardless of the order of events in the sector definition"*. This
> sector's line is named `NEBULA` exactly — no underscore — and `sectors/data/` therefore
> keeps it in file order at position 7 and does not flag it `nebula_first`.
> Against that: the same page's NOTE 2 says the starting sector's beacon listing is *"in
> proper order"*, and that listing puts its `NEBULA` line **first**, ahead of stores, even
> though the XML has it seventh ([[source-sector-data-xml]]). Both sectors use the same bare
> `NEBULA` list.
> **Which side to bet on:** nebula-first. The stated reason for the rule is that the purple
> cloud graphics must be drawn before anything else, which is a property of nebula generation,
> not of a list-name prefix. Recording the file-order reading too, because nothing in
> `raw/gamedata/` states either.
> *Practical impact is small:* `NEBULA` already sits above `QUESTS` and `HOSTILE1`, so which
> lines get starved does not change — only when the clouds are drawn.

> ⚠️ **CONTRADICTION — how many beacons a sector has.**
> [[source-fandom-sectors]] opens with *"each containing between 19 and 24 beacons"*, but its
> own technical section describes a 6×4 grid with an 80% chance per cell and only a soft
> guard against too many empties — which sets a ceiling of 24 and no stated floor.
> [[source-xftl-sector-map]] reads the same code and says the count is *"bounded, not fixed"*,
> giving the guard as: a cell is filled anyway if an empty already exists and empties are at
> least 20% of the cells placed so far. **Trust the ceiling of 24; treat 19 as Fandom's
> rounding of a distribution, not a hard minimum.** Nothing on this page infers a minimum
> number of stops from it.

> ⚠️ **CONTRADICTION — Fandom's own beacon listing for this sector.**
> Fandom lists Civilian as *"6–8 hostile encounters"* (a merge of `HOSTILE_CIVILIAN` 4–6 and
> `HOSTILE1` 2, noted in its own HTML comment) and prints nebula **last**. The XML has nine
> separate lines and nebula seventh. The same page warns that its listing *"does not
> completely reflect the actual order of events in the game files"*, so this is a known
> limitation of the source rather than a factual dispute — but the merged hostile figure
> hides that half of it is the line most likely to be cut.
> (per [[source-fandom-sectors]], [[source-sector-data-xml]])

> **Resolved, not a contradiction — which sector NOTE 2 is about.**
> NOTE 2's *"the Civilian (Starting) Sector has its beacons placed in proper order"* refers to
> Fandom's **Civilian (Starting) Sector**, described there as *"always and only Sector 1"* and
> *"slightly different from the usual Civilian Sector: it has fewer stores, items, quests and
> nebulas"*. That is `STANDARD_SPACE` — [[sector-federation-space]] — **not** this sector.
> Nothing in NOTE 2 licenses reading Fandom's Civilian Sector listing as ordered.
> (per [[source-fandom-sectors]], [[source-sector-data-xml]])

## Open Questions
- [x] ~~Which events populate each list~~ — resolved: the full pool (77 distinct events) is
      extracted into `sectors/data/civilian-sector.sector.json` and rendered at
      `sectors/sector-civilian-sector.html`.
- [ ] Why no `startEvent` — does it inherit `START_BEACON`? Partly answered: the commented-out
      line names `START_BEACON_CIVILIAN`, which does not exist in `raw/gamedata/`. The
      fallback behaviour is still unsourced.
- [ ] Does `OVERRIDE_ITEMS` / `OVERRIDE_QUESTS` / `OVERRIDE_HOSTILE1` actually replace its
      twin under AE? Unresolved wiki-wide — see [[concept-sector-event-allocation]].
- [ ] Is the beacon floor real? No source states one; see the second contradiction above.
- [ ] How often does a Civilian Sector actually finish with zero quest beacons? Needs
      observed runs; no file answers it.

## Related
- [[sector-federation-space]] — same lists, lower counts, and a guaranteed quest beacon
- [[sector-engi-controlled-sector]] — the other 2–3-store sector, with five item beacons
- [[concept-sector-event-allocation]] — the two allocation systems and what "unreachable" means
- [[concept-quest-beacon-placement]] — why nine quest-planting events yield so few markers
- [[concept-nebula-mechanics]] · [[concept-rebel-fleet-advance]] · [[concept-stores]]

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml) — `NEUTRAL_CIVILIAN` nesting `DISTRESS_BEACON`
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
- [[source-fandom-sectors]] (per raw/wiki/sectors.md) — generation order, NOTE 1, NOTE 2
- [[source-fandom-beacons]] (per raw/wiki/beacons.md) — marker visibility, quest-marker rules
- [[source-fandom-rebel-fleet]] (per raw/wiki/rebel-fleet.md)
- [[source-fandom-environmental-hazards]] (per raw/wiki/environmental-hazards.md)
- [[source-fandom-stores-and-resources]] (per raw/wiki/stores-and-resources.md)
- [[source-fandom-template-stores-number-of-stores-by-sectors]] (per raw/wiki/template-stores-number-of-stores-by-sectors.md)
- [[source-fandom-template-stores-additional-stores-from-events-by-sectors]] (per raw/wiki/template-stores-additional-stores-from-events-by-sectors.md)
- [[source-fandom-template-distress-events-by-sectors]] (per raw/wiki/template-distress-events-by-sectors.md)
- [[source-xftl-sector-map]] (per raw/modding/2026-08-15-xftl-sector-map.txt) — `AddQuest`, grid generation
