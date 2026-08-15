---
id: sector-rebel-stronghold
type: sector
sector_id: REBEL_SECTOR_MINIBOSS
sector_class: hostile
faction: [[[entity-rebels]]]
min_sector: 4
unique: true
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-15
sources: 15
tags: [unique, flagship, hostile, miniboss]
---

# Rebel Stronghold

## Summary
The unique Rebel sector that houses the Flagship construction beacon. Its allocation table is
identical to [[sector-rebel-controlled-sector]] plus one guaranteed `FLAGSHIP_CONSTRUCTION`
line, written first in the table (per [[source-sector-data-xml]]). That one beacon is
[[event-rebel-shipyard]] — the miniboss, the largest single payout in the game, and the
Federation Cruiser unlock — and it is free to decline. Everything else is ordinary Rebel
space: a hostile-group sector (`sectorType name="HOSTILE"` and `OVERRIDE_HOSTILE`,
per [[source-sector-data-xml]]) with 6–8 forced-fight beacons allocated and one guaranteed
boarding.

## Trigger & Where It Appears
- `unique="true"`, `minSector="4"` ([[source-sector-data-xml]]) — at most one per run.
- [[source-fandom-sectors]] states the sector "can occur only once per game and only at
  sector **5** or higher".

> ⚠️ **CONTRADICTION (resolved as an indexing difference):** this page previously read
> `minSector="4"` as "never before sector 4". [[source-fandom-sectors]] says sector 5 or
> higher. The two agree if `minSector` is **zero-indexed against the displayed sector
> number**, and that reading holds across every sector in the file: `ENGI_HOME`
> `minSector="2"` against Fandom's "sector 3 or higher", `SLUG_HOME` `minSector="3"` against
> "sector 4 or higher", `ZOLTAN_HOME` `minSector="2"` against "sector 3 or higher"
> ([[source-sector-data-xml]], [[source-fandom-sectors]]). Nothing in `raw/gamedata/` states
> the indexing, so this is inference from a consistent pattern, not a file fact. Practical
> reading: **displayed sectors 5–7**, since sector 8 is always `FINAL`.

That range matters for quests — see below.

- The sector is listed in **both** the base `sectorType name="HOSTILE"` pool and the AE
  `OVERRIDE_HOSTILE` pool ([[source-sector-data-xml]]), while the beacon that defines it,
  `FLAGSHIP_CONSTRUCTION`, sits under the "Events added with the DLC" header in
  `events_rebel.xml` ([[source-events-rebel]]). Recorded as an open question below; the wiki
  keeps `version: ae` for now.

## Character & Hazards

### Placement order — the table is a filling queue
Per [[source-fandom-sectors]] (citing [[source-xftl-sector-map]]), beacons are laid out
*before* any event is assigned, on a 6×4 grid with roughly a 20% chance per cell of being
empty — so **at most 24 beacons**, and the count is bounded rather than fixed. Lines of the
sector definition are then filled top to bottom, each rolling its own min–max inclusive, and
**generation stops when the beacons run out**.

Consequences specific to this sector (derived in `sectors/data/rebel-stronghold.sector.json`):

- `FLAGSHIP_CONSTRUCTION` is the **first line off the table**, so the miniboss beacon can
  never be squeezed out by a high roll above it. This is the same reason stores and homeworld
  set-pieces sit at the top of every definition ([[source-fandom-sectors]]).
- `NEBULA_REBEL` jumps the queue regardless of file order, because the cloud graphics have to
  be drawn first; clouds that fall over ordinary beacons convert them, and those beacons draw
  from the shared `NEBULA` list rather than from anything in this table
  ([[source-fandom-sectors]]).
- `NEUTRAL_REBEL`, last in the file, is the **at-risk line**: the allocation totals 17–31
  against a 24-beacon ceiling, so if everything above rolls high there may be nothing left for
  it.
- Beacons still empty when the table is exhausted fall back to the shared `NEUTRAL` list
  (`OVERRIDE_NEUTRAL` with AE content on) — events that are not part of this sector's own
  pool ([[source-fandom-sectors]]).
- The **exit beacon is not in the table**; it draws from the shared `EXIT_LIST`, and an exit
  covered by cloud graphics is always empty ([[source-fandom-sectors]]). Exit placement is in
  one of the two right-most grid columns, at least five jumps from the start where the game
  can manage it ([[source-xftl-sector-map]]).

### Beacon markers
`<distressBeacon/>` on an event is what puts a distress marker on the map, and it does not
match the allocation line of the same name ([[source-fandom-sectors]] NOTE 1). In this sector
the mismatch runs one way only:

- Every distress-tagged event this sector can produce comes from `DISTRESS_BEACON_REBEL` —
  `CIVILIAN_ASTEROIDS_BEACON`, `DISTRESS_STATION_FIRE`, `ESCORT_BEACON`, `FRIENDLY_BEACON`,
  `TRAP_BEACON`. Nothing in the other lists carries the tag, so unlike Engi space the map
  cannot show more distress beacons than the table allocated.
- The reverse case does occur: `REBEL_VS_FEDERATION` is allocated from the distress list but
  carries **no** `<distressBeacon/>` element ([[source-events-xml]]), so it never shows the
  marker. Fandom describes this class of case as a mistake in the data
  ([[source-fandom-sectors]]). Fandom's own page for the event likewise does not mark it
  `distress=true`.
- Distress and store markers are only drawn for beacons **within one jump**, and distress
  markers persist until the fleet overtakes them ([[source-fandom-beacons]]).
- [[event-rebel-shipyard]] is `LRSmap=noship` ([[source-fandom-rebel-shipyard]]) — nothing on
  the map, and no scanner reading, identifies the miniboss beacon in advance.

### Environmental hazards
The pool's hazard beacons are the 0–5 nebula line (11 events: 8 in cloud, 3 in a plasma
storm), plus `AUTO_ASTEROID` (asteroid field) and `BOARDERS_SUN` (red giant). Per
[[source-fandom-environmental-hazards]]: nebula disables sensors, a plasma storm halves your
reactor (rounded up), asteroids strike periodically, and solar flares set fires — with shields
up 1–2 fires, with shields down 3–6.

### The fleet
Per [[source-fandom-rebel-fleet]] and [[source-xftl-sector-map]]:

- A nebula beacon **in a non-nebula sector halves that jump's advance** (32px of the usual
  64px). This sector is not a nebula sector, so its 0–5 cloud beacons are its only repeatable
  brake on the clock.
- Letting a Rebel scout or automated ship escape **doubles** the advance for one turn — the
  `AUTO_WARNING`, `SQUAT_WARNING` and `NEBULA_AUTO_WARNING` branches here. `REBEL_TRANSPORT`
  does **not** accelerate pursuit.
- **Overtaking rewrites a beacon**: the event that was waiting there and any environmental
  hazard are replaced. So every event in these pools, `FLAGSHIP_CONSTRUCTION` included, is
  only available until the shading reaches it. Killing the Elite Fighter that replaces it pays
  **1 fuel** and no scrap (4 fuel if you are out of fuel).
- An overtaken nebula beacon always gains an ion storm (except nebula exit beacons); an
  overtaken non-nebula beacon gains an ASB, which fires a shield-piercing 3-damage shot that
  always breaches ([[source-fandom-environmental-hazards]]).

### Quest markers
`QUESTS_REBEL` is allocated 0–2 and sits second-from-last, so a run through here can be handed
no marker from that line at all ([[source-sector-data-xml]]). Where a marker *lands* is
governed separately ([[source-fandom-beacons]], [[source-xftl-sector-map]]): the target beacon
must be unvisited, not a nebula beacon, not the exit, not already overtaken, not a store, not
a distress beacon, and within reach before the fleet takes it. If nothing qualifies the quest
is pushed into the next sector — **and a push that happens in sector 7 is dropped, because
sector 8 allows no quests**. Since this sector can only appear in displayed sectors 5–7, that
failure mode is live here: six events in this pool plant quest markers.

## Event Pool

Entries in the order they are actually filled — file order, except that the nebula line is
drawn ahead of everything:

| Fill | Event list | min | max | Notes |
|---|---|---|---|---|
| 1st | `NEBULA_REBEL` | 0 | 5 | drawn before the table, out of file order |
| 2nd | `FLAGSHIP_CONSTRUCTION` | 1 | 1 | single event, not a list; guaranteed |
| 3rd | `STORE_REBEL` | 1 | 2 | the only guaranteed stores |
| 4th | `ITEMS` | 1 | 2 | |
| 5th | `HOSTILE_REBEL` | 6 | 8 | largest allocation |
| 6th | `BOARDERS_REBEL` | 1 | 1 | boarding guaranteed |
| 7th | `DISTRESS_BEACON_REBEL` | 1 | 2 | |
| 8th | `NOTHING_REBEL` | 1 | 2 | |
| 9th | `QUESTS_REBEL` | 0 | 2 | |
| 10th | `NEUTRAL_REBEL` | 5 | 6 | **at risk** — may be cut if everything above rolls high |

Start beacon: `START_BEACON_REBEL`. Allocation total **17–31 slots against at most 24
beacons** — an allocation, not a map size ([[source-sector-data-xml]], with the ceiling from
[[source-fandom-sectors]]).

The pool resolves to **50 distinct events**: 10 that fight on arrival, 18 that can end in
combat behind a choice, 6 that put boarders aboard, 4 that can kill a crew member, 6 that
plant quest markers. Full per-list membership, tags and blue-option gates are in the generated
profile at `sectors/data/rebel-stronghold.sector.json` and the built page
`sectors/sector-rebel-stronghold.html`.

### Stores
1–2 guaranteed store beacons ([[source-sector-data-xml]]) — fewer than the 2–3 that Civilian,
Engi and Engi Homeworld space guarantee ([[source-fandom-sectors]]). Only the
`STORE_REBEL` line is guaranteed; `ESCORT_BEACON` can open a shop on top of it, and it is a
distress-marked event, not a store-marked one, so nothing labels it in advance
([[source-fandom-stores-and-resources]] on guaranteed vs event-opened stores).

Store stock, including which crew races appear, is weighted by rarity
([[source-fandom-stores-and-resources]]). [[source-fandom-sectors]] gives this sector Human 1;
Engi, Mantis 2; Rockmen 3; Zoltan 5. This sector's `<sectorDescription>` declares **no
`rarityList` at all** ([[source-sector-data-xml]]) — unlike Engi, Mantis, Zoltan, Rock, Slug,
Nebula, Lanius and Crystal space, which do — so those numbers are the blueprint defaults
(`human` 1, `engi` 2, `mantis` 2, `rock` 3, `energy` 5, `slug` 0, `crystal` 0, per
[[source-blueprints]]) rather than anything this sector sets. Fandom prints the same table for
every sector without a `rarityList` (Civilian, Pirate, Rebel Controlled, The Last Stand),
which is consistent with that reading.

## Chains That Run Through It
- [[event-rebel-shipyard]] (`FLAGSHIP_CONSTRUCTION`) — guaranteed, one beacon, and the entry
  point for the Federation Cruiser unlock. See below. _Chain page not yet created._
- Three events here plant the hidden Federation base marker (`CIVILIAN_ASTEROIDS_BEACON`,
  `REBEL_VS_FEDERATION`, `FEDERATION_PLANET_SIGNAL`), and `MERCHANT_REQUEST`, `ESCORT_BEACON`
  and `ALISON_DEFECTOR` each start a quest of their own.

## Factions & Ships
- [[entity-rebels]] — dominant faction. All six boarding events in this pool send **humans**
  (`class="human"` in every case),
  which matches [[source-fandom-the-rebellion]]: "No alien is ever found serving on a Rebel
  ship." The same source notes the Rebel Defector event (`ALISON_DEFECTOR`, in
  `NEUTRAL_REBEL`) as evidence the movement has members who find it off-putting.
- [[entity-flagship]] — previewed here, in unfinished form.

## Strategy Notes
- **The shipyard is free to look at.** Choice 2 ("Leave immediately") has no effects at all,
  so arriving costs one jump and nothing else; the fight only starts once you choose to look
  around ([[source-events-rebel]], see [[event-rebel-shipyard]]).
- **The clock is the real cost of this sector.** Seven events in the pool can advance the
  fleet a jump; only two can push it back — `AUTO_DEFENSE_RADAR` (`modifyPursuit -1`) and the
  shipyard (`-2`). Cloud beacons halve the advance while you sit in one
  ([[source-fandom-rebel-fleet]]).
- **Take quest events early.** A marker planted late is pushed to the next sector, and pushed
  from sector 7 it is dropped entirely ([[source-fandom-beacons]]).
- *(Opinion, [[source-fandom-sectors]].)* Fandom argues sector colour is a poor danger signal
  and that sectors should be judged individually, with store count called out as the main
  differentiator. It offers no measured danger figure for this sector; its routing commentary
  is unsourced.

## Open Questions
- [x] ~~What `FLAGSHIP_CONSTRUCTION` actually offers, and whether it is skippable.~~
  **Answered.** Skippable at zero cost — the "Leave immediately" branch has no effects.
  Winning pays an `autoReward level="HIGH"` `weapon` (weapon plus the scrap of a HIGH roll),
  +5 fuel, +5 missiles, +5 drone parts, `modifyPursuit amount="-2"` (fleet delayed two turns)
  and `<unlockShip id="4"/>`, the Federation Cruiser. The enemy is `FLASHSHIP_CONSTRUCTION_SHIP`
  (`auto_blueprint BOSS_SPECIAL`): the Flagship's third-phase layout at 10 hull, shields 2/8,
  two artillery mounts at 1/4, three human crew, a teleporter, no weapons block. No blue
  options, no surrender, no escape. ([[source-events-rebel]], [[source-blueprints]],
  [[source-fandom-rebel-shipyard]]; full breakdown at [[event-rebel-shipyard]].)
- [ ] Does the engine substitute the AE `OVERRIDE_` lists for `HOSTILE_REBEL` and `ITEMS` here?
  The files do not say (see [[concept-sector-event-allocation]]), but Fandom lists both
  AE-only events as occurring in **Rebel Stronghold**: `REBEL_PULSAR`
  ([[source-fandom-rebel-fight-near-pulsar]]) and `STORE_REBELSIDE`
  ([[source-fandom-large-trade-station]]). That is community evidence for substitution, not a
  file fact. If it holds, this sector can also carry a **pulsar** hazard.
- [ ] Can a quest marker, or the fleet, overwrite the `FLAGSHIP_CONSTRUCTION` beacon?
  [[source-fandom-beacons]] says a marker replaces the event it lands on "unless it is a
  store, exit, or another quest marker" and flags the full exclusion list as untested;
  [[source-xftl-sector-map]]'s candidate filter excludes stores, distress beacons, nebula and
  exit beacons, but says nothing about named set-pieces. The fleet-overtake rule
  ([[source-fandom-rebel-fleet]]) carries no exception at all.
- [ ] The map's beacon **floor**. [[source-fandom-sectors]] opens with "between 19 and 24
  beacons"; [[source-xftl-sector-map]] describes only a bounded 20%-empty rule, and
  `raw/gamedata/` states nothing. With the allocation minimum at 17, whether this sector
  routinely leaves beacons for the `NEUTRAL` fallback is unresolved.
- [ ] Whether `unique="true"` is once per sector or once per run — see
  [[concept-event-uniqueness]].
- [ ] Does this sector exist with AE content **off**? It is in the base `HOSTILE` sector-type
  pool, but `FLAGSHIP_CONSTRUCTION` is defined under the DLC header of `events_rebel.xml`
  ([[source-sector-data-xml]], [[source-events-rebel]]). The datamined files are the AE
  distribution, so what a vanilla install contains cannot be checked from `raw/`.
  [[source-fandom-rebel-shipyard]] does not mark the event as Advanced Edition content, and
  [[source-fandom-sectors]] does not mark the sector as AE either — which points to "both",
  against the file layout. See [[concept-ae-vs-vanilla]].

## Related
- [[sector-rebel-controlled-sector]] — the same table minus the shipyard line
- [[event-rebel-shipyard]], [[entity-flagship]], [[entity-rebels]]
- [[concept-rebel-fleet-advance]], [[concept-quest-beacon-placement]],
  [[concept-sector-event-allocation]], [[concept-nebula-mechanics]]

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-rebel]] (per raw/gamedata/events_rebel.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-fandom-sectors]] (per raw/wiki/sectors.md)
- [[source-xftl-sector-map]] (per raw/modding/2026-08-15-xftl-sector-map.txt)
- [[source-fandom-rebel-fleet]] (per raw/wiki/rebel-fleet.md)
- [[source-fandom-beacons]] (per raw/wiki/beacons.md)
- [[source-fandom-environmental-hazards]] (per raw/wiki/environmental-hazards.md)
- [[source-fandom-stores-and-resources]] (per raw/wiki/stores-and-resources.md)
- [[source-fandom-the-rebellion]] (per raw/wiki/the-rebellion.md)
- [[source-fandom-rebel-shipyard]] (per raw/wiki/rebel-shipyard.md)
- [[source-fandom-rebel-fight-near-pulsar]] (per raw/wiki/rebel-fight-near-pulsar.md)
- [[source-fandom-large-trade-station]] (per raw/wiki/large-trade-station.md)
