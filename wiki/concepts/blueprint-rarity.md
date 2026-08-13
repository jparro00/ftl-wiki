---
id: concept-blueprint-rarity
type: concept
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
related_events: []
tags: [mechanics, methodology, unresolved, items]
---

# `rarity` on blueprints — what the files do and don't say

## Definition & Context
Almost every purchasable thing in FTL carries a `rarity`:

```xml
<weaponBlueprint name="BEAM_3">   <!-- Glaive Beam -->
	<rarity>5</rarity>
</weaponBlueprint>
```

The wiki's item template has a `rarity:` field for it. **Nothing in `raw/gamedata/` defines
what the number means**, and nothing in `raw/wiki/` mentions the concept at all — grepping
all 292 Fandom pages for "rarity" returns zero hits. This page records what the data
supports, and marks the rest unresolved.

## Where it appears

**1. On blueprints — `<rarity>N</rarity>`.** 161 well-formed blueprints carry one, in
`blueprints.xml` (119) and `dlcBlueprints.xml` (42):

| Blueprint kind | With `rarity` | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|---|
| `weaponBlueprint` | 68 | 31 | 3 | 7 | 15 | 9 | 3 |
| `augBlueprint` | 43 | 10 | 2 | 13 | 15 | 3 | — |
| `droneBlueprint` | 21 | 7 | 3 | 2 | 2 | 5 | 2 |
| `systemBlueprint` | 16 | 1 | 15 | — | — | — | — |
| `crewBlueprint` | 10 | 5 | 1 | 2 | 1 | — | 1 |
| `itemBlueprint` | 3 | — | 1 | — | 2 | — | — |
| `shipBlueprint` | **0 of 39** | — | — | — | — | — | — |

**Ships never carry a rarity** — not in `blueprints.xml`, `dlcBlueprints.xml`,
`autoBlueprints.xml`, `dlcPirateBlueprints.xml` or `dlcBlueprintsOverwrite.xml`. Whatever
`rarity` selects, it is not enemy ship hulls. ([[source-blueprints]], [[source-dlcblueprints]])

> **A 162nd `<rarity>` exists and almost certainly does not count.** `blueprints.xml` line
> 2916 declares an augment with a **misspelled opening tag**:
> `<augBluepring name="TELEPORTER_PREIGNITE">` … `</augBlueprint>` — *"Teleporter
> Pre-igniter: The teleporter is made immediately available after an FTL jump"*, cost 130,
> rarity 3. The id is referenced nowhere else in `raw/gamedata/` and has no Fandom page. Its
> neighbour `ENCODED_DISTRESS` (*"Encrypted Distress Signal"*, cost 100, rarity 3) is
> spelled correctly but is likewise referenced nowhere. Both look like unshipped augments;
> only one of them is also unparseable. ([[source-blueprints]])

**2. Per sector — `<rarityList>` in `sector_data.xml`.** 13 of the 21 `sectorDescription`s
carry one, 118 entries in total, using the same 0–5 range as an *attribute*:

```xml
<rarityList>
	<blueprint name="engi" rarity="1"/>
	<blueprint name="slug" rarity="0"/>
	…
</rarityList>
```

([[source-sector-data-xml]])

## What the data establishes

### The two layers, and that the sector layer overrides the blueprint layer
Every species has base rarity in `blueprints.xml` and a per-sector value where it matters:

| Species | Base | Own sector | Foreign sectors |
|---|---|---|---|
| `human` | 1 | — | 1–3 |
| `engi` | 2 | **1** (Engi) | 0, 3, 4 |
| `mantis` | 2 | **1** (Mantis) | 0, 3, 4 |
| `rock` | 3 | **1** (Rock) | 0, 3, 4 |
| `energy` (Zoltan) | 5 | **1** (Zoltan) | 0, 3, 4 |
| `slug` | **0** | **2** (Slug/Slug Home), 3 (Uncharted Nebula) | 0, 3, 4 |
| `crystal` | **0** | **1** (Crystal Home) | not listed |
| `anaerobic` (Lanius) | **0** | **2** (Lanius) | not listed |

`slug`, `crystal` and `anaerobic` are 0 in the base file and non-zero **only** in their home
sectors. Fandom independently says of the Crystal store: *"These are the only stores you can
normally buy crystal beings"* ([[source-fandom-store-crystal]]). The two lines up exactly.

### `0` means "excluded", not "most common"
The Hidden Crystal Worlds is the decisive case ([[source-sector-data-xml]]). `CRYSTAL_HOME`
carries by far the longest `rarityList` in the file — 43 entries: it names **31 standard
weapons and sets every one to 0**, sets all six non-Crystal species to 0, and raises the
Crystal weapons and `BOMB_LOCK`:

```xml
<blueprint name="BEAM_2"  rarity="0"/>   <!-- base 2 (Halberd Beam) -->
<blueprint name="BEAM_3"  rarity="0"/>   <!-- base 5 (Glaive Beam)  -->
<blueprint name="LASER_BURST_3" rarity="0"/>  <!-- base 4 (Burst Laser Mk II) -->
…
<blueprint name="CRYSTAL_BURST_1" rarity="1"/>  <!-- base 0 -->
<blueprint name="CRYSTAL_HEAVY_1" rarity="2"/>  <!-- base 0 -->
<blueprint name="CRYSTAL_BURST_2" rarity="4"/>  <!-- base 0 -->
<blueprint name="CRYSTAL_HEAVY_2" rarity="5"/>  <!-- base 0 -->
```

Weapons with base rarity 2, 4 and 5 are pushed **down** to 0 here, and Crystal weapons are
pushed **up** from 0. If 0 were the "most common" tier, the Crystal sector would be the one
place in the game overflowing with Glaive Beams. It is instead the one place they cannot
appear. **0 = not offered** is the only reading that fits.

Two independent confirmations of the same reading:

- **Systems.** All 16 `systemBlueprint`s are rarity 1 except one: `artillery` is 0. Artillery
  is the one system that is a fixed feature of particular hulls rather than something a store
  stocks. ([[source-blueprints]])
- **Drone "crew".** `crewBlueprint`s `battle` and `repair` — the drone bodies, not species —
  are rarity 0, alongside the three gated species.

### The scale runs 1 = commonest → 5 = rarest
Three independent orderings agree:

- **Species in their own sector are always 1** (Engi, Mantis, Rock, Zoltan, Crystal), and
  3–4 abroad. Being at home makes you *more* likely, and the number goes *down*.
- **Crystal weapons within `CRYSTAL_HOME`** run Crystal Burst I = 1, Heavy Crystal I = 2,
  Crystal Burst II = 4, Heavy Crystal II = 5 — ascending with power.
- **Base beams**: Halberd (`BEAM_2`) = 2, Glaive (`BEAM_3`) = 5. Base crew: human 1,
  Engi/Mantis 2, Rock 3, Zoltan 5.

So `rarity` is an ordinal weight where **larger means scarcer**, with **0 as a separate flag
meaning "not in the pool"** rather than the bottom of the same scale.

### What the rarity-0 set actually contains
Reading the 54 zero entries as a group makes the flag's purpose obvious. Every one falls into
a category that has a *non-random* route into the game ([[source-blueprints]],
[[source-dlcblueprints]]):

| Group | Members |
|---|---|
| Enemy-only / boss hardware | `ARTILLERY_BOSS_1..4`, `PDS_SHOT`, `DRONE_LASER`, `DRONE_LASER_2`, `DRONE_BEAM`, `DRONE_BEAM2`, `DRONE_ION`, `DRONE_MISSILE`, `DRONE_FIREBEAM`, `ANTI_DRONE_ION`, `DEFENSE_2_ENEMY`, `BOSS_DEFENSE_2`, `BOARDER_BOSS` |
| Player-hull fixed loadout variants | `MISSILES_2_PLAYER`, `SHOTGUN_PLAYER`, `LASER_CHARGEGUN_PLAYER`, `DRONE_SHIELD_PLAYER`, `LASER_HEAVY_1_SP`, `ARTILLERY_FED`, `ARTILLERY_FED_C`, `artillery` |
| Race-ship signature augments | `ROCK_ARMOR`, `ENERGY_SHIELD`, `CRYSTAL_SHARDS`, `SLUG_GEL`, `NANO_MEDBAY`, `CREW_STIMS`, `DRONE_SPEED`, `SYSTEM_CASING`, `ADV_HULL_ARMOR` — each verified as an `<aug>` on a player `shipBlueprint` |
| Quest items | `STASIS_POD` (Damaged Stasis Pod) |
| Sector-gated | `slug`, `crystal`, `anaerobic` crew; all four Crystal weapons; `BOMB_LOCK` |
| Drone bodies | `battle`, `repair` |
| Low-tier weapons | `LASER_BURST_1` (Defense Laser I), `LASER_BURST_2` (Dual Shot Laser), `MISSILES_1` (Leto), `MISSILES_2` (Artemis), `BEAM_1` (Mini Beam), `BOMB_BREACH_1` (Breach Bomb I), `BOMB_LOCK`, `COMBAT_ION`, `COMBAT_MISSILE`, `DRONE_HACKING` |

That last row is the interesting one, and it is **not** a counterexample. All three members of
`WEAPONS_FREE` — the list the game draws on when an event hands you a weapon for nothing —
are rarity-0 weapons:

```xml
<blueprintList name="WEAPONS_FREE">
	<name>LASER_BURST_1</name>   <!-- rarity 0 -->
	<name>BEAM_1</name>          <!-- rarity 0 -->
	<name>MISSILES_1</name>      <!-- rarity 0 -->
</blueprintList>
```

([[source-autoblueprints]]). `LASER_BURST_2` and `BEAM_1` are also in `STARTING_WEAPONS`, and
`MISSILES_2` is in `STANDARD_WEAPONS` (enemy auto-ship loadouts) — where `LASER_BURST_2` is
explicitly commented out in favour of `LASER_BURST_2_A`. Every rarity-0 weapon has a named
list or hull that delivers it.

## What is NOT established

- **What consumes the number.** No file names a store, a reward roll, or a generator. There
  is no `blueprintList` of store stock anywhere in `raw/gamedata/` — the enumerated lists are
  all enemy loadouts (`SHIPS_*`, `WEAPONS_<faction>`, `DRONES_*`), starting loadouts
  (`STARTING_*`), DLC bundles (`DLC_*`), or the `<!-- for events -->` blue-option lists. So
  `rarity` is the *only* selection metadata that exists — which is suggestive, not proof.
- **The exact weighting.** Whether rarity 2 is twice as likely as rarity 4, or the reciprocal,
  or a lookup table, is unknown. This wiki should never state a percentage from a rarity.
- **Whether it also governs event rewards.** `<autoReward level="HIGH">weapon</autoReward>`
  and `<weapon name="RANDOM"/>` both pick a random weapon; nothing says they use `rarity`.
- **Whether an unlisted item in a sector with a `rarityList` keeps its base value or is
  suppressed.** `CRYSTAL_HOME` lists 31 standard weapons but **not** the Advanced Edition
  additions (`SHOTGUN`, `LASER_CHAINGUN`, `LASER_CHARGEGUN`, `ION_STUN`, `BOMB_STUN`, …).
  If unlisted means "keep base rarity", AE Crystal-sector stores stock DLC weapons that
  vanilla's design clearly meant to exclude. If unlisted means "excluded", the eight sectors
  with no `rarityList` at all would sell nothing. The second reading is untenable, so the
  first is probably right — and that makes the omission an **AE oversight**. Flagged, not
  asserted.
- **`0 = unbuyable` as a blanket statement.** The evidence above supports "0 = not drawn from
  the random pool". It does **not** establish that a rarity-0 item can never be bought — a
  store could stock from a different mechanism entirely. Do not write "unbuyable" on item
  pages; write "base rarity 0 — excluded from random generation unless a sector's
  `rarityList` raises it", and cite this page.

## Where It Applies
The `rarity:` field on every [[concept-blue-options]]-relevant item page, and the
"How To Get It" section of every `wiki/items/` page. Sector pages that carry a `rarityList`
should record it: [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
[[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]],
[[sector-uncharted-nebula]], [[sector-slug-home-nebula]],
[[sector-slug-controlled-nebula]], [[sector-zoltan-controlled-sector]],
[[sector-zoltan-homeworlds]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]],
[[sector-hidden-crystal-worlds]], and the Lanius sector.

The eight sectors with **no** `rarityList` — Federation Space, Civilian, Pirate, both Rebel
sectors, the Last Stand, and the two vestigial stubs ([[sector-vestigial-definitions]]) —
presumably fall back to base rarity, which would make them the only places the "generic"
distribution applies.

## Implications For Play
Stated as consequences of the reading above, not as measured facts:

- **Species crew are sector-locked.** Slug, Crystal and Lanius crew are base-0 and raised only
  at home, so [[sector-slug-controlled-nebula]], [[sector-hidden-crystal-worlds]] and the
  Lanius sector are the places to buy them. Zoltan are base rarity 5 — the rarest hireable
  species anywhere except [[sector-zoltan-controlled-sector]], where they drop to 1.
- **Rock sectors are the only place `BOMB_LOCK` (Crystal Lockdown Bomb) appears outside the
  Crystal sector** — base 0, raised to 4 in `ROCK_SECTOR` and 2 in `ROCK_HOME`.
  See [[item-crystal-lockdown-bomb]].
- **The Crystal sector will not sell you a conventional weapon.** Plan the loadout before
  entering [[sector-hidden-crystal-worlds]].
- **Rarity 5 items are the scarcest things in the game**: Glaive Beam, Zoltan crew,
  Heavy Crystal Mark II, and a handful of drones.

## Related
- [[concept-blue-options]] — what having these items unlocks
- [[concept-sector-event-allocation]] — the other per-sector table in `sector_data.xml`
- [[concept-stores]] — the beacons where rarity presumably gets consumed
- [[sector-hidden-crystal-worlds]] — the sector whose `rarityList` proves the `0` reading
- [[item-crystal-lockdown-bomb]] · [[item-slug-crew]] · [[item-rock-crew]] ·
  [[item-lanius-crew]] · [[item-damaged-stasis-pod]]

## Open Questions
- [ ] **What reads `rarity`?** Store stock, random rewards, both, neither. Needs the binary or
      a controlled in-game observation.
- [ ] What is the weighting function? Until answered, no page may state odds from a rarity.
- [ ] Does an item absent from a sector's `rarityList` keep its base rarity? The AE-weapon
      omission in `CRYSTAL_HOME` hangs on this.
- [ ] Can a rarity-0 item ever be bought, as opposed to merely never randomly generated?
- [ ] Why do `LASER_BURST_2` (Dual Shot Laser) and `MISSILES_2` (Artemis) — ordinary low-tier
      weapons — sit at 0 alongside boss artillery? The `WEAPONS_FREE` / `STARTING_WEAPONS` /
      `STANDARD_WEAPONS` membership explains *how* they reach the player, but not why the
      developers chose to exclude them from the random pool.
- [ ] `shipBlueprint` has no rarity at all — what selects which enemy hull spawns?

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-dlcblueprints]] (per raw/gamedata/dlcBlueprints.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml) — the `<rarityList>` overrides
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml) — `WEAPONS_FREE`, `STANDARD_WEAPONS`
- [[source-fandom-store-crystal]] (per raw/wiki/store-crystal.md)
