---
id: concept-stores
type: concept
version: both
first_seen: 2026-08-09
last_updated: 2026-08-13
sources: 9
related_events: []
tags: [mechanics, store, economy]
---

# Stores — the `<store/>` tag, store beacons, and what they stock

## Definition & Context
A store is not a special beacon type in the data. It is an ordinary event carrying one empty
element:

```xml
<event name="STORE">
	<text load="STORE_TEXT"/>
	<store/>
</event>
```

`<store/>` takes no attributes, has no children, and appears **26 times** in
`raw/gamedata/`. Everything about which items are on the shelves is decided elsewhere — see
[[concept-blueprint-rarity]].

## Two ways a store happens

### 1. Store beacons — 12 events whose entire payload is `<store/>`

| Event | File | Sector | Page |
|---|---|---|---|
| `STORE` | `events.xml` | generic | [[event-store]] |
| `STORE_ENGI` | `events_engi.xml` | Engi | [[event-store-engi]] |
| `STORE_MANTIS` | `events_mantis.xml` | Mantis | [[event-store-mantis]] |
| `STORE_PIRATE` | `events_pirate.xml` | Pirate | [[event-store-pirate]] |
| `STORE_REBEL` | `events_rebel.xml` | Rebel | [[event-store-rebel]] |
| `STORE_ROCK` | `events_rock.xml` | Rock | [[event-store-rock]] |
| `STORE_ZOLTAN` | `events_zoltan.xml` | Zoltan | [[event-store-zoltan]] |
| `STORE_CRYSTAL` | `events_crystal.xml` | Crystal | [[event-store-crystal]] |
| `STORE_LANIUS` | `dlcEvents_anaerobic.xml` | Lanius (AE) | [[event-store-lanius]] |
| `NEBULA_STORE` | `events_nebula.xml` | Uncharted Nebula | [[event-store-in-nebula-uncharted]] |
| `NEBULA_STORE_SLUG` | `events_slug.xml` | Slug | [[event-store-in-nebula-slug]] |
| `QUEST_STORE` | `events.xml` | quest destination | [[event-quest-store]] |

**Every one of these is mechanically identical**: a `<text>` (usually a `textList` of 3–5
variants) and `<store/>`. No choices, no requirements, no risk, no cost to arrive. The
faction variants are pure reskins — the differences are prose only. `NEBULA_STORE` and
`NEBULA_STORE_SLUG` add `<environment type="nebula"/>`, which is the only mechanical
difference in the whole family, and it applies the standard nebula effects
([[concept-nebula-mechanics]]).

`QUEST_STORE` carries a developer note, `<!-- JUSTIN - Can be used elsewhere-->`, and is
reached as a quest destination rather than by sector allocation ([[source-events-xml]]).

### 2. A store as an *outcome* inside another event — the other 14 instances, across 8 events
Here `<store/>` sits inside a `<choice>`'s result or an `<eventList>` entry, so the store is
the reward for doing something:

| Where | What earns it | Page |
|---|---|---|
| `STORE_REBELSIDE` (3 branches) + `STORE_REBELSIDE_SEARCH` | Searching a Rebel-side trade station | [[event-large-trade-station]] |
| `LANIUS_SCARED_CIVILIAN` + its list | Reassuring the civilian | [[event-lanius-lone-ship]] |
| `QUEST_ESCORT_ARRIVE` entry 3 | Escort delivered — also `−5` hull damage, i.e. repairs | [[event-escort-civilians]] |
| `PIRATE_BRIBER_WIN` | Taking the pirate's bribe (also `modifyPursuit −1`) | [[event-pirate-briber]] |
| `SQUAT_STORE_RESCUE` (`destroyed` **and** `deadCrew`) | Winning the store-rescue fight | [[event-quest-store-rescue]] |
| `ZOLTAN_TRADE_HUB_SUCCESS` | Passing the Zoltan trade hub | [[event-zoltan-trade-hub]] |
| `SLUG_DRINK_DRINK`, `SLUG_DRINK_ROCK` | Drinking with the Slugs | [[event-slug-drink]] |
| `NEBULA_SLUG_FAKE_STORE_LIST` entry 1 | Sitting through the Slug sales pitch | [[event-slug-store-ship]] |

The last one is the only **trap** store in the game. `NEBULA_SLUG_FAKE_STORE_LIST` has three
entries, and only the first opens a store (plus 5 fuel); the other two are ambushes — a
`JELLY_STATUS_WEAPONS` fight with your weapons locked to 0 and a Slug boarder, or a `JELLY`
fight with two boarders. Assuming uniform selection ([[concept-event-list-weighting]]), that
is **1/3 store, 2/3 ambush** ([[source-events-slug]]).

## What a store sells
The store screen's own strings enumerate the categories ([[source-text-misc]]):

| String id | Label |
|---|---|
| `store_title_weapons` | WEAPONS |
| `store_title_drones` | DRONES |
| `store_title_augments` | AUGMENTATIONS |
| `store_title_crew` | HIRE CREW |
| `store_title_systems` | SYSTEMS |
| `store_title_items` | ITEMS |
| `store_title_repair` | REPAIR |

plus `store_tab_buy` / `store_tab_sell` and `store_tab_page1` / `store_tab_page2` — so a
store has a **buy and a sell side and two pages**. Repair comes in two granularities:
`repair_all_*` (*"Purchase a repair job to restore your hull health back to maximum"*) and
`repair_one_*` (*"…restore one point of hull health"*).

"ITEMS" is the three consumables, which are `itemBlueprint`s with their own costs
([[source-blueprints]]): fuel (3 scrap), missiles (6), drone parts (8).

**How many of each category a given store rolls is not in the data.** Nothing in
`raw/gamedata/` describes store layout, stock size, or which subframes appear.

## Where stores come from: the allocation table
Stores are allocated **directly by the sector**, never through an `<eventList>`
([[source-sector-data-xml]], and see [[concept-sector-event-allocation]]):

| `sectorDescription` | Wiki sector | Store events | Guaranteed |
|---|---|---|---|
| `STANDARD_SPACE` | [[sector-federation-space]] | `STORE` 1–2 | 1 |
| `CIVILIAN_SECTOR` | [[sector-civilian-sector]] | `STORE` 2–3 | 2 |
| `ENGI_SECTOR` / `ENGI_HOME` | [[sector-engi-controlled-sector]] / [[sector-engi-homeworlds]] | `STORE_ENGI` 2–3 | 2 |
| `PIRATE_SECTOR` | [[sector-pirate-controlled-sector]] | `STORE_PIRATE` 1–2 | 1 |
| `REBEL_SECTOR` / `REBEL_SECTOR_MINIBOSS` | [[sector-rebel-controlled-sector]] / [[sector-rebel-stronghold]] | `STORE_REBEL` 1–2 | 1 |
| `MANTIS_SECTOR` / `MANTIS_HOME` | [[sector-mantis-controlled-sector]] / [[sector-mantis-homeworlds]] | `STORE_MANTIS` 1–2 | 1 |
| `ZOLTAN_SECTOR` / `ZOLTAN_HOME` | [[sector-zoltan-controlled-sector]] / [[sector-zoltan-homeworlds]] | `STORE_ZOLTAN` 2–2 | 2 |
| `ROCK_SECTOR` / `ROCK_HOME` | [[sector-rock-controlled-sector]] / [[sector-rock-homeworlds]] | `STORE_ROCK` 2–2 | 2 |
| `CRYSTAL_HOME` | [[sector-hidden-crystal-worlds]] | `STORE_CRYSTAL` 2–3 | 2 |
| `LANIUS_SECTOR` | Lanius sector | `STORE_LANIUS` 2–2 | 2 |
| `NEBULA_SECTOR` | [[sector-uncharted-nebula]] | `STORE` 0–1 **+** `NEBULA_STORE` 1–1 | 1 |
| `SLUG_SECTOR` / `SLUG_HOME` | [[sector-slug-controlled-nebula]] / [[sector-slug-home-nebula]] | `STORE` 0–1 **+** `NEBULA_STORE_SLUG` 2–2 | 2 |
| `FINAL` | [[sector-the-last-stand]] | `STORE` 1–1 | 1 |
| `DEEP_SPACE_SECTOR`, `ABANDONED_SECTOR` | [[sector-vestigial-definitions]] | `STORE` 2–4 | — (stubs) |

Notes from the file:

- **Every playable sector guarantees at least one store**, and eight guarantee two.
- The Rock sectors carry a **commented-out** `<event name="STORE" min="2" max="4"/>`
  alongside their live `STORE_ROCK` line — the generic store was deliberately removed there.
- The nebula sectors are the only ones that split their guarantee across two different store
  events, because their generic `STORE` can roll **zero**.
- `newEvents.xml`'s parallel `<eventCounts>` blocks also allocate `STORE` at 1–2 for map
  depths 0–3. Whether the engine reads them is unresolved — [[concept-sector-event-allocation]].

## How a store beacon differs from an ordinary beacon

| | Store beacon | Ordinary beacon |
|---|---|---|
| Event body | `<text>` + `<store/>`, nothing else | choices, ships, environments, rewards |
| Choices | **none** | usually 2–4 |
| Enemy | never | often |
| `unique="true"` | **no** (except `STORE_REBELSIDE`) | frequently |
| Star-map marker | *"You previously found a store at this location."* (`map_store_loc`) | type-specific |
| Long-Ranged Scanners | reads as **no ship** (`LRSmap=noship` on every Fandom store page) | ship / no-ship |
| Repeatable within a sector | yes — non-uniqueness is what lets `min=2` work | depends |

Being **non-unique** is the load-bearing detail: an event marked `unique="true"` can fill only
one beacon per sector, so the sectors that guarantee two or three stores could not do so if
their store event were unique. That per-sector reading of `unique` is now corroborated by
[[source-fandom-random-events]] and contested by [[concept-event-tree-grammar]] — both sides
at [[concept-event-uniqueness]], where this argument is one of the three reasons to prefer the
per-sector scope.

`LRSmap` is a **Fandom wiki field, not a game attribute** — it appears nowhere in
`raw/gamedata/`. [[source-fandom-random-events]] defines what it records: whether Long-Ranged
Scanners or a map reveal will annotate the beacon as having a ship present. Its `noship`
value on every store page means a store beacon reads as empty on the star map. Two caveats
travel with the field: *"no ship presence"* does not guarantee the absence of a hostile ship,
and *"possible ship detected"* can mean a friendly or neutral one. See
[[item-long-ranged-scanners]].

## What stock a store rolls
No file enumerates store inventory. There is **no `blueprintList` of store stock anywhere in
`raw/gamedata/`** — every enumerated list is an enemy loadout (`SHIPS_*`,
`WEAPONS_<faction>`, `DRONES_*`), a starting loadout (`STARTING_*`), a DLC bundle (`DLC_*`),
or a blue-option class list (`<!-- for events -->`).

What does exist is `<rarityList>` in `sector_data.xml`, which sets per-sector rarity for
named blueprints — and its content is unmistakably about shop stock:

- `CRYSTAL_HOME` zeroes 34 standard weapons and every non-Crystal species, and raises the
  four Crystal weapons. Fandom, independently: *"These are the only stores you can normally
  buy crystal beings"* ([[source-fandom-store-crystal]]).
- `ROCK_SECTOR` raises `BOMB_LOCK` (Crystal Lockdown Bomb) from 0 to 4, `ROCK_HOME` to 2.
- `SLUG_SECTOR` / `SLUG_HOME` raise `slug` crew from 0 to 2; `LANIUS_SECTOR` raises
  `anaerobic` to 2; each species sits at 1 in its own sector and 3–4 abroad.

**So store stock is sector-dependent, and this is the mechanism** — which answers the open
question left on [[event-store]] ("Does `STORE` roll generic stock, or is stock influenced by
the sector it appears in?"). The eight sectors with **no** `rarityList` — Federation Space,
Civilian, Pirate, both Rebel sectors, the Last Stand and the two stubs — presumably fall back
to base blueprint rarity. Full analysis: [[concept-blueprint-rarity]].

## Implications For Play
- **Buy species crew where they live.** Slug, Crystal and Lanius crew are excluded from every
  store outside their home sector. Zoltan are base rarity 5 (the scarcest) and rarity 1 in
  Zoltan space.
- **Do not enter [[sector-hidden-crystal-worlds]] expecting to re-arm.** Its stores stock
  Crystal weapons and `BOMB_LOCK`, and nothing else.
- **Rock sectors are the second source of `BOMB_LOCK`.**
- **The nebula sectors are the only ones where the store count can disappoint**: `STORE` can
  roll 0 in all three, and only the Slug sectors backstop it with a guaranteed pair.
- Eight of the 26 `<store/>` instances are earned rather than found. [[event-slug-drink]],
  [[event-zoltan-trade-hub]] and [[event-large-trade-station]] are worth taking partly *as*
  store access.
- **Treat [[event-slug-store-ship]] as a fight, not a shop** — 2 of its 3 outcomes are ambushes.

## Related
- [[concept-blueprint-rarity]] — what determines the shelves
- [[concept-sector-event-allocation]] — how the min/max table is read
- [[concept-event-list-weighting]] — the 1/3 figure for the fake Slug store
- [[concept-nebula-mechanics]] — the two nebula store variants
- [[concept-event-uniqueness]] — what `unique="true"` scopes to; this page's multi-store
  argument is evidence in that dispute
- [[event-store]] — the generic store beacon, with the full text variant table

## Open Questions
- [ ] How many items does a store stock, and how are the seven subframes chosen? Nothing in
      `raw/gamedata/` says.
- [ ] Are sell prices a fixed fraction of `<cost>`? No file states a ratio.
- [ ] Does the repair price scale with sector, hull, or difficulty?
- [ ] Do the faction store variants differ in stock, or only in prose? The data shows only
      prose differences, but stock generation is invisible in the files.
- [ ] Does `<store/>` inside an `<eventList>` entry produce the same store as a store beacon?
- [ ] Why is `STORE_REBELSIDE` the only `unique="true"` store event?

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-misc]] (per raw/gamedata/text_misc.xml) — the store-screen strings
- [[source-blueprints]] (per raw/gamedata/blueprints.xml) — `itemBlueprint` costs
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml) — the absence of a stock list
- [[source-events-slug]] (per raw/gamedata/events_slug.xml) — the fake store
- [[source-dlcevents]] (per raw/gamedata/dlcEvents.xml) — `STORE_REBELSIDE`
- [[source-fandom-store-crystal]] (per raw/wiki/store-crystal.md)
- [[source-fandom-random-events]] (per raw/wiki/random-events.md) — the meaning of `LRSmap`
  and the per-sector reading of `unique`
