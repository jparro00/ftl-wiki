---
id: concept-blue-options
type: concept
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 9
related_events: []
tags: [mechanics, blue-options, methodology]
---

# Blue options — how `req=` gates work

## Definition & Context
A "blue option" is an extra `<choice>` that only appears if your ship satisfies a
requirement. In the data it is one attribute:

```xml
<choice hidden="true" req="slug">          <!-- needs a Slug crew member -->
<choice req="sensors" lvl="3" hidden="true">  <!-- needs Sensors at level 3+ -->
<choice hidden="true" req="ROCK_ARMOR">    <!-- needs the Rock Plating augment -->
<choice hidden="true" req="WEAPONS_ION">   <!-- needs any weapon on the ion list -->
```

`req` is the whole gate. There are **219 live `req=`-bearing choices** across
`raw/gamedata/` (comment blocks stripped, per [[concept-event-list-weighting]]; counting
commented-out ones too gives 228). `req` appears on `<choice>` elements and on nothing else.

The game labels them for the player in the choice text itself: nearly every blue option's
prose opens with a parenthetical naming the requirement — *"(Slug Crew) …"*, *"(Improved
Sensors) …"*, *"(Long-Ranged Scanners) …"* ([[source-text-events-xml]]).

## The five kinds of requirement

`req` is a **name lookup**, and the engine resolves the name against whatever kind of
blueprint carries it. Six namespaces are in play. Live counts:

| Kind | Choices | Share | Distinct keys |
|---|---|---|---|
| **System** (`systemBlueprint`, plus `reactor`) | 122 | 56% | 14 |
| **Crew species** (`crewBlueprint`) | 49 | 22% | 8 |
| **Augment** (`augBlueprint`) | 20 | 9% | 9 |
| **Weapon/drone class list** (`blueprintList`) | 9 | 4% | 7 |
| **Specific weapon** (`weaponBlueprint`) | 8 | 4% | 5 |
| **Specific drone** (`droneBlueprint`) | 11 | 5% | 4 |
| **Total** | **219** | | **47** |

### Systems — 122 choices, the majority of all blue options

| `req` | n | | `req` | n |
|---|---|---|---|---|
| `sensors` | 23 | | `clonebay` | 5 |
| `hacking` | 19 | | `doors` | 4 |
| `medbay` | 13 | | `weapons` | 4 |
| `teleporter` | 11 | | `oxygen` | 3 |
| `cloaking` | 10 | | `drones` | 3 |
| `engines` | 9 | | `reactor` | 2 |
| `mind` | 8 | | | |
| `pilot` | 8 | | | |

`sensors` and `hacking` alone are 42 of 219 — nearly a fifth of every blue option in the
game. Note that `shields`, `battery` and `artillery` gate **nothing**, despite existing as
`systemBlueprint`s, and `reactor` gates two choices despite **not** being a
`systemBlueprint` at all (it is the ship's power bar; see below).

### Crew species — 49 choices

| `req` | Species | n |
|---|---|---|
| `anaerobic` | [[item-lanius-crew]] | 11 |
| `slug` | [[item-slug-crew]] | 11 |
| `engi` | Engi | 11 |
| `rock` | [[item-rock-crew]] | 6 |
| `mantis` | Mantis | 4 |
| `crystal` | Crystal | 3 |
| `energy` | **Zoltan** | 2 |
| `human` | Human | 1 |

Two traps in that table:

- **`energy` is the Zoltan.** `crew_energy_title` is *"Zoltan"* ([[source-text-blueprints]]),
  and the choice prose confirms it: *"(Zoltan Crew) …"*. There is no `req="zoltan"`.
- **`anaerobic` is the Lanius** — *"(Lanius Crew) …"*, `crew_anaerobic_title` = *"Lanius"*.
  All 11 are Advanced Edition (`dlcEvents_anaerobic.xml`, `events_engi.xml`,
  `newEvents.xml`, and one `<!-DLC!->`-marked choice in `events.xml`).

`req="human"` fires exactly once, in [[event-confused-mantis]]. `battle` and `repair` also
exist as `crewBlueprint`s (drone "crew"), but the choices that name them use the **uppercase
drone** ids `BATTLE` / `REPAIR` — see the drone row below.

### Augments — 20 choices

`ADV_SCANNERS` (7, [[item-long-ranged-scanners]]) · `ROCK_ARMOR` (3, [[item-rock-plating]]) ·
`LIFE_SCANNER` (3, [[item-lifeform-scanner]]) · `NANO_MEDBAY` (2) · `SCRAP_COLLECTOR` (1) ·
`FTL_JUMPER` (1) · `STASIS_POD` (1) · `BACKUP_DNA` (1) · `FLEET_DISTRACTION` (1).

`ADV_SCANNERS` is the workhorse — Long-Ranged Scanners unlock a blue option in seven
separate events, e.g. [[event-nebula-lost-ship]], [[event-destroyed-cargo-ship]],
[[event-rebel-fight-chance-in-nebula]]. `STASIS_POD` is the Crystal Cruiser quest key
([[event-zoltan-research-facility]], [[chain-crystal-cruiser-unlock]]);
`FLEET_DISTRACTION` is the one fleet-clock augment ([[concept-rebel-fleet-advance]]).

### Weapon / drone **class lists** — 9 choices

Seven `req` values are not blueprints at all but `<blueprintList>` names, and the developers
annotated them for exactly this purpose ([[source-autoblueprints]]):

```xml
<blueprintList name="WEAPONS_ION"> <!-- for events -->
<blueprintList name="WEAPONS_BEAM_DAMAGE">  <!-- for events -->
<blueprintList name="COMBAT_DRONE_LIST"> <!-- for events -->
```

| `req` | n | Members |
|---|---|---|
| `WEAPONS_MISSILES` | 2 | MISSILES_1/2/2_PLAYER/3, MISSILES_BURST, MISSILES_BREACH, MISSILE_CHARGEGUN |
| `COMBAT_BEAM_DRONE_LIST` | 2 | COMBAT_BEAM, COMBAT_BEAM_2 |
| `WEAPONS_ION` | 1 | ION_1/2/4, BOMB_ION, ION_STUN, BOMB_STUN, ION_CHARGEGUN, ION_CHAINGUN |
| `WEAPONS_BEAM_DAMAGE` | 1 | BEAM_HULL, BEAM_3, BEAM_2, BEAM_1, BEAM_LONG, ARTILLERY_FED |
| `COMBAT_DRONE_LIST` | 1 | COMBAT_1, COMBAT_2, COMBAT_BEAM, COMBAT_BEAM_2, DRONE_FIREBEAM |
| `DRONES_DEFENSE_LIST` | 1 | DEFENSE_1, DEFENSE_2 |
| `WEAPONS_MISSILES_EVENTS` | 1 | identical to `WEAPONS_MISSILES`, but declared in `dlcBlueprintsOverwrite.xml` |

**Fandom independently confirms the list semantics.** For `WEAPONS_BEAM_DAMAGE`
([[event-crushed-pirate]]) it says the Anti-Bio Beam and Fire Beam are *excluded* and the
Artillery Beam is *eligible* — which is precisely the membership above, since `BEAM_BIO` and
`BEAM_FIRE` are absent and `ARTILLERY_FED` is present. For `COMBAT_BEAM_DRONE_LIST` it says
the Anti-Ship Fire Drone is excluded — `DRONE_FIREBEAM` is indeed not in that list, though it
*is* in `COMBAT_DRONE_LIST`. ([[source-fandom-crushed-pirate]], [[source-autoblueprints]])

`WEAPONS_MISSILES_EVENTS` is an AE addition that duplicates `WEAPONS_MISSILES` entry for
entry; only [[event-asteroid-mining-colony]] uses it. Why the duplicate exists is unknown.

### Specific weapons — 8 choices
`BOMB_FIRE` (3, Fire Bomb) · `BEAM_BIO` (2, Anti-Bio Beam) · `BEAM_FIRE` (1) ·
`BOMB_HEAL` (1, Healing Burst — marked `<!--DLC!-->`) · `MISSILES_BREACH` (1).

### Specific drones — 11 choices
`SHIP_REPAIR` (3, Hull Repair Drone) · `REPAIR` (3, Repair Drone) ·
`BATTLE` (3, Anti-Personnel Drone) · `BOARDER` (2, Boarding Drone).

## What `req` actually tests

**Possession of the blueprint — nothing more.** Two pieces of evidence:

- Fandom tested the `WEAPONS_ION` gate in-game and reports that *"missile ammo resource is
  not required and not wasted"* for the Ion/Stun Bomb members
  ([[source-fandom-malfunctioning-defense-system]]). So the gate does not check consumables.
- The game says the same thing structurally. `QUEST_MANTIS_INVASION`'s choice is labelled
  *"(2 Fire Bombs) Teleport fire bombs into key structures"* and its outcome spends
  `<item type="missiles" min="-2" max="-2"/>` — but the gate is a bare `req="BOMB_FIRE"`.
  The "2" is a description of the **cost**, not part of the requirement
  ([[source-events-xml]], [[source-text-events-xml]]).

Consequences the wiki should record rather than assume away: a blue option can be offered
that you cannot afford, and choosing it can leave you at negative-equivalent resources. What
the engine does in that case is **unknown** — no data file says.

## `lvl=`, `min_level=`, `max_lvl=` — the tier attributes

| Attribute | Live uses | Reading |
|---|---|---|
| `lvl` | 85 | **minimum** level of the `req` system |
| `min_level` | 2 | same thing, spelled differently |
| `max_lvl` | 13 | **maximum** level |
| `max_group` | 41 (39 × `"0"`, 2 × `"1"`) | tier grouping (see below) |
| `blue` | 13, all `"false"` | render as blue option or not |

**`lvl` is a floor, and the files prove it by construction.** `DOCK_DRONE_SALESMAN` in
`newEvents.xml` prices a Drone Control upgrade in three brackets that partition the level
range exactly, using both ends at once ([[source-newevents]]):

```xml
<choice req="drones" max_lvl="3"                max_group="0" blue="false">  <!-- levels 1-3 -->
<choice req="drones" min_level="4" max_lvl="5"  max_group="0" blue="false">  <!-- levels 4-5 -->
<choice req="drones" min_level="6" max_lvl="7"  max_group="0" blue="false">  <!-- levels 6-7 -->
```

Three non-overlapping brackets, with prices rising across them (−20/−25 → −33/−25 →
−65/−50 scrap), only work if `min_level` is a minimum and `max_lvl` a maximum. `min_level`
appears **only** in those two lines, and `lvl` does the same job everywhere else, so it reads
as a one-off spelling slip rather than a distinct attribute.

`TRADER_UPGRADES` uses the same pattern for Oxygen, Piloting, Doors and Sensors — but only
the first two tiers are live:

```xml
<choice req="oxygen" max_lvl="1" max_group="0" blue="false"> …      <!-- level 1 -->
<choice req="oxygen" max_lvl="2" max_group="0"  blue="false"> …     <!-- level 2 -->
<!--<choice req="oxygen" lvl="3" max_group="0"  blue="false"> … -->  <!-- level 3+, DISABLED -->
```

The `lvl="3"` top tier is commented out for all four systems, so a player at level 3+ is
offered no upgrade at all in that event. (That is also why the raw grep count for `blue=` is
17 while the live count is 13 — see [[concept-event-list-weighting]] on excluding comments.)

**The game names the tiers in the choice text**, and the convention is visible even though
the string table is not perfectly consistent:

| `lvl` | Usual label | Examples |
|---|---|---|
| 1 (or absent) | plain name | *(Teleporter)*, *(Cloaking)*, *(Simple Hacking)* |
| 2 | *Improved X* | *(Improved Sensors)* ×7, *(Improved Hacking)*, *(Improved Cloaking)*, *(Improved Piloting)*, *(Improved Medbay)*, *(Improved Mind Control)*, *(Improved Oxygen)*, *(Improved Teleporter)* |
| 3 | *Advanced X* | *(Advanced Sensors)* ×6, *(Advanced Hacking)* ×3, *(Advanced Cloaking)*, *(Advanced Mind Control)*, *(Advanced Piloting)* |

Exceptions exist and are string-table sloppiness, not mechanics: `sensors lvl="2"` is
labelled *"(Advanced Sensors)"* twice and `sensors lvl="3"` is labelled *"(Improved
Sensors)"* once; `medbay lvl="2"` appears as *"Improved Medbay"*, *"Adv. Medbay"*,
*"Advanced Medbay"* and bare *"Medbay"*. Trust the `lvl` value, not the label.

Levels actually used: `engines` reaches 3–7, `weapons` is always `lvl="6"` (4 choices),
`reactor` uses `max_lvl="24"` twice, and the `lvl="24"` outliers are those same reactor
brackets. `req="engi" lvl="1"` appears three times in `nameEvents.xml`, which is dev/test
content — it is the only crew req with a `lvl`, so whether `lvl` on a *crew* req means
"1 crew member of that species" is **unknown**.

### `max_group` — near-certainly "show only one from this group"
41 live uses, 39 of them `max_group="0"` and 2 `max_group="1"`. The decisive case is
`NEBULA_AUTO_DEFENSE_ITEM` ([[source-events-nebula]]), which contains two *pairs*:

```xml
<choice req="cloaking" lvl="1" max_group="0" hidden="true"> …
<choice req="cloaking" lvl="2" max_group="0" hidden="true"> …
<choice req="hacking"  lvl="1" max_group="1" hidden="false"> …  <!--DLC-->
<choice req="hacking"  lvl="2" max_group="1" hidden="false"> …  <!--DLC-->
```

Because `lvl` is a floor, a player with Cloaking 2 qualifies for *both* cloaking choices;
the shared `max_group` is what stops the menu showing two near-duplicate lines. The two
hacking tiers sit in a different group precisely so they are not collapsed against the
cloaking pair. This is a strong inference from the data, not a documented value — nothing in
`raw/gamedata/` defines the attribute.

### `blue="false"` — a requirement that is *not* rendered blue
13 live uses (17 in the raw text, 4 of them commented out), **all** of them in
`newEvents.xml`, and all in the same shape: tiered purchase/upgrade choices in
`TRADER_UPGRADES` ([[event-trade-scrap-for-upgrades]]), `ROCK_SLUG_GRATEFUL` and
`DOCK_DRONE_SALESMAN` ([[event-dock-drone-salesman]]).

| `req` | Live brackets carrying `blue="false"` |
|---|---|
| `oxygen`, `pilot`, `doors`, `sensors` | `max_lvl=1`, `max_lvl=2` (×4 systems = 8; the `lvl=3` tiers are commented out) |
| `reactor` | `max_lvl=24` (×2) |
| `drones` | `max_lvl=3`, `min_level=4 max_lvl=5`, `min_level=6 max_lvl=7` |

Here the `req` is not a reward for being well-equipped — it is a **price lookup**. The
choice would be shown to every player anyway; `req`+`lvl` only decides *which* version and
what it costs. Marking it `blue="false"` stops the UI from advertising a routine purchase as
a hidden bonus. That reading follows from the attribute name plus its exclusive use in
priced-upgrade events; the files do not define it.

The corollary matters for counting: **13 of the 219 `req` choices are not blue options at
all.** The true blue-option count is **206**.

### `hidden=` is a different axis
191 of the 219 `req` choices carry `hidden="true"`, 2 carry `hidden="false"`, 26 omit it —
and `hidden` appears on 792 live choices in total, of which **599 have no `req` at all**,
overwhelmingly the `<text id="continue"/>` continuation choices. Its meaning is **not
defined anywhere in `raw/gamedata/`**, and it is clearly not the blue flag, since `blue=`
exists separately and the two DLC hacking tiers above are `hidden="false"` blue options.
Left unresolved.

There is also one typo in the wild: `hiiden=` appears once, which will simply not parse as
`hidden` ([[source-events-xml]]).

## Where It Applies
Every event page's **Blue Options** section. Some worked examples:

- Crew: [[event-giant-alien-spiders]] (`BATTLE`, `BEAM_BIO`, `BOARDER`) ·
  [[event-ancient-device]] (`crystal`) · [[event-slug-drink]] (`rock`) ·
  [[event-confused-mantis]] (`human`, `mantis`) · [[event-terraforming-scan]] (`energy`)
- Systems: [[event-slug-hacker-oxygen]] (`oxygen`) ·
  [[event-refueling-platform-garbled-broadcast]] (`doors`) ·
  [[event-boarders-humans-jammed-sensors]] (`hacking`) ·
  [[event-zoltan-research-facility]] (`medbay`, `STASIS_POD`)
- Augments: [[event-large-asteroid-field]] (`SCRAP_COLLECTOR`) ·
  [[event-escort-civilians-ftl-haywire]] (`FTL_JUMPER`) ·
  [[event-crystalline-research-facility]] (`BACKUP_DNA`) ·
  [[event-dense-asteroid-field-distress]] (`ROCK_ARMOR`)
- Class lists: [[event-crushed-pirate]] (`WEAPONS_BEAM_DAMAGE`, `COMBAT_BEAM_DRONE_LIST`) ·
  [[event-malfunctioning-defense-system]] (`WEAPONS_ION`) ·
  [[event-rock-live-mine]] (`WEAPONS_MISSILES`)
- Not-actually-blue: [[event-trade-scrap-for-upgrades]] · [[event-dock-drone-salesman]]

## Implications For Play
- **Sensors and Hacking are the highest-yield blue-option investments in the game** — 42 of
  202 blue options between them, and both have level tiers, so upgrading keeps paying.
  Shields, by contrast, unlock nothing.
- **Crew species are worth more than their combat stats.** A single Slug, Engi or Lanius
  crew member is a key to 11 doors each.
- **Long-Ranged Scanners is the only augment that pays off in seven different events.**
- **Level 2 and level 3 are the thresholds that matter** for Sensors, Hacking, Cloaking,
  Mind Control, Piloting and Medbay — the "Improved"/"Advanced" split. `weapons` is the
  outlier at level 6.
- A blue option being *offered* does not mean you can *pay* for it — the gate ignores
  missiles and drone parts.

## Related
- [[concept-event-tree-grammar]] — the node grammar every event is built from
- [[concept-event-list-weighting]] — why commented-out choices are excluded from these counts
- [[concept-rebel-fleet-advance]] — `req="FLEET_DISTRACTION"`, the one fleet-clock gate
- [[concept-blueprint-rarity]] — how the items behind these gates get into your hands
- [[item-sensors]] · [[item-hacking]] · [[item-long-ranged-scanners]] ·
  [[item-lifeform-scanner]] · [[item-distraction-buoys]]

## Open Questions
- [ ] What does `hidden=` do? It is on 196 of 219 `req` choices and on hundreds without one.
- [ ] Is `max_group` really "collapse to one displayed choice"? Strongly implied, undocumented.
- [ ] Does `lvl` on a **crew** req mean a crew count? Only `nameEvents.xml` (dev/test content)
      ever pairs the two, so the wiki cannot tell.
- [ ] What happens when you pick a blue option you cannot pay for (0 missiles, 0 drone parts)?
- [ ] Are `shields`, `battery` and `artillery` deliberately un-gated, or an oversight?
- [ ] Why does AE add `WEAPONS_MISSILES_EVENTS` as a byte-identical copy of
      `WEAPONS_MISSILES`?

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml) — 63 of the 219 gates
- [[source-newevents]] (per raw/gamedata/newEvents.xml) — 28 gates, all 17 `blue="false"`
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml) — the `max_group` evidence
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml) — the `<!-- for events -->` class lists
- [[source-dlcblueprintsoverwrite]] (per raw/gamedata/dlcBlueprintsOverwrite.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml) — which namespace each key lives in
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml) — `energy` = Zoltan, `anaerobic` = Lanius
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml) — the parenthetical labels
- [[source-fandom-crushed-pirate]] (per raw/wiki/crushed-pirate.md)
- [[source-fandom-malfunctioning-defense-system]] (per raw/wiki/malfunctioning-defense-system.md)
