---
id: chain-mantis-cruiser-unlock
type: chain
trigger_event: [[[event-legendary-thief-kazaaakplethkilik]]]
steps: [[[event-legendary-thief-kazaaakplethkilik]], [[event-mantis-named-thief-stash]]]
sectors: [[[sector-mantis-homeworlds]]]
reward: Mantis Cruiser unlock + Mantis Pheromones + the crew member Kazaaak + a weapon cache
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [ship-unlock, mantis-cruiser, blue-option, crew-reward, system-gated, guaranteed-start]
---

# Mantis Cruiser unlock

## Summary
A single set-piece fight in the [[sector-mantis-homeworlds]] whose *aftermath* is the real
chain. Beat the legendary thief KazaaakplethKilik the wrong way and you get medium scrap.
Beat him the right way — and pass two separate system gates — and you get the **Mantis
Cruiser**, the Mantis Pheromones augment, Kazaaak himself as crew, `HIGH` scrap and a
quest marker to a weapon cache ([[source-events-mantis]], [[source-events-ships]]).

Unlike the Engi and Rock chains this one is not lost to a wrong *choice* — it is lost to
missing *equipment*. The full payout needs **(teleporter OR sensors 3) AND (medbay 2 OR
clonebay 2)**, all four checked in the same aftermath tree.

## How It Starts
- Trigger: [[event-legendary-thief-kazaaakplethkilik]] (`MANTIS_NAMED_THIEF`), allocated
  directly on the `MANTIS_HOME` sector description at `min="1" max="1"`
  ([[source-sector-data-xml]]). **Guaranteed** once per Mantis Homeworlds visit, and not
  present in the ordinary [[sector-mantis-controlled-sector]].
- `MANTIS_HOME` is `unique="true"` with `minSector="2"` ([[source-sector-data-xml]]).
- The event is `unique="true"`, with an in-file developer note reading
  `NOTE - make globally unique` ([[source-events-mantis]]).
- Long-range scanners show a ship at the beacon
  ([[source-fandom-legendary-thief-kazaaakplethkilik]]).

## Steps

1. **[[event-legendary-thief-kazaaakplethkilik]]** — `MANTIS_NAMED_THIEF`
   (raw: events_mantis.xml)
   A heavily armour-plated Mantis ship. Both opening choices lead to the same fight; the
   `req="mantis"` blue option is **pure flavour with no mechanical effect**
   ([[source-events-mantis]]). The ship carries `NEEDS ELITE TAG - need an
   escape/surrender` as a dev note and, as shipped, has **no surrender and no escape**
   ([[source-events-ships]]).

   | Win condition | Payload | Chain |
   |---|---|---|
   | `<destroyed>` | `autoReward MED standard` | ❌ dead |
   | `<deadCrew load="MANTIS_NAMED_THIEF_DEFEAT"/>` | opens the aftermath tree | ✅ |

   > ⚠️ **THE TRAP.** Killing the hull ends the chain. `<destroyed>` has no `<quest>`, no
   > `<unlockShip>` and no path into the aftermath — the only route onward is
   > `<deadCrew>` ([[source-events-ships]]). This is the third unlock chain in the game
   > that punishes the obvious win; compare [[chain-stealth-cruiser-unlock]] step 2 and
   > [[chain-rock-cruiser-unlock]] step 2.

2. **`MANTIS_NAMED_THIEF_DEFEAT`** — the aftermath (raw: events_mantis.xml)
   Loaded from the ship's `deadCrew` block, so it carries no separate page; it is
   documented in full on [[event-legendary-thief-kazaaakplethkilik]]. It is a two-level
   gate:

   **Gate A — find the survivor.** `req="teleporter"` (any level) *or*
   `req="sensors" lvl="3"`. Both open an identical sub-tree. Without either, the only
   choice is *"Move in to strip their ship"* → `HIGH standard` and the chain ends.

   **Gate B — save him.** Inside that sub-tree, `req="medbay" lvl="2"` *or*
   `req="clonebay" lvl="2"`. Both lead to the same *Accept* payload. Without either, the
   best available branch is *"Listen to what he has to say"* → `HIGH standard` **plus**
   `<quest event="MANTIS_NAMED_THIEF_STASH"/>` — the cache, but **no ship unlock**.

   Passing both gates and accepting gives, in one payload
   ([[source-events-mantis]]):
   ```
   <augment name="CREW_STIMS"/>                                   → Mantis Pheromones
   <autoReward level="HIGH">scrap_only</autoReward>
   <crewMember amount="1" class="mantis" all_skills="2" id="name_Kazaaak"/>
   <quest event="MANTIS_NAMED_THIEF_STASH"/>
   <unlockShip id="2"/>                                           → Mantis Cruiser
   ```

3. **[[event-mantis-named-thief-stash]]** — `MANTIS_NAMED_THIEF_STASH`
   (raw: events_mantis.xml)
   The quest marker, and the chain's only second beacon. Two lines of XML: no choices, no
   fight, no hazard. `<autoReward level="HIGH">weapon</autoReward>` — a weapon plus high
   scrap ([[source-events-mantis]]). Long-range scanners show **no ship**
   ([[source-fandom-legendary-thief-kazaaakplethkilik]]).

   Three different aftermath branches place this marker, including the full-unlock one —
   so reaching the cache does **not** imply you got the ship.

## Requirements
- **Routing** into [[sector-mantis-homeworlds]] (`unique="true"`, `minSector="2"`).
- **A dead-crew win** against a heavily armoured Mantis ship with no surrender and no
  escape branch. In practice: boarders, anti-personnel weapons, or venting.
- **Gate A:** a [[item-teleporter]] (any level) **or** [[item-sensors]] at level 3.
- **Gate B:** a [[item-medbay]] at level 2 **or** a [[item-clone-bay]] at level 2.
- Fuel for one extra jump to the cache.

*Opinion:* a teleporter satisfies Gate A **and** is the most reliable way to produce the
dead-crew win in the first place, so it does double duty. Level-3 sensors satisfy only the
gate. Fandom adds that you may jump away from the beacon, buy or upgrade what you are
missing, and return to finish the quest — a claim not stated in the game files
([[source-fandom-legendary-thief-kazaaakplethkilik]]).

## Reward
Ranked by path ([[source-events-mantis]], [[source-events-ships]]):

| Path | Reward |
|---|---|
| dead crew → Gate A → Gate B → Accept | **Mantis Cruiser**, [[item-mantis-pheromones]], Kazaaak (`all_skills="2"`), `HIGH scrap_only`, + the cache beacon |
| dead crew → Gate A → "listen"/"speak" | `HIGH standard` + the cache beacon |
| dead crew → strip the ship / let him die | `HIGH standard` |
| destroyed | `MED standard`, chain over |
| the cache itself | `HIGH weapon` — one weapon plus high scrap |

Note the full-payout branch pays `scrap_only` while the lesser branches pay `standard`
(scrap **with** fuel/missiles/drone parts), so the best branch is not strictly dominant on
resources — only on everything else.

Ship id `2` → Mantis Cruiser is supported by the ship's own unlock hint: *"The famous
Mantis thief, KazaaakplethKilik, owns this ship. You'll have to 'convince' him to help
you."* (`ship_PLAYER_SHIP_MANTIS_unlock`, [[source-text-blueprints]]) — this chain by
name. Corroborating: `PLAYER_SHIP_MANTIS` ships with `<aug name="CREW_STIMS"/>`, the same
augment this chain awards ([[source-blueprints]]).

## Failure Modes
- **The Mantis Homeworlds never appear.**
- **Destroying the ship.** Silent failure; `MED` scrap and nothing else.
- **Arriving without Gate A.** You are limited to the strip-the-ship branch — no cache, no
  unlock.
- **Arriving with Gate A but not Gate B.** You get the cache marker and `HIGH standard`,
  but the ship unlock is out of reach.
- **Dying to the fight.** No surrender, no escape branch — once engaged you fight it out
  ([[source-events-ships]]).

## Strategy Notes
- *Opinion:* decide the win condition before you engage. This is a crew-kill objective, not
  a hull race, and a strong weapon loadout with no boarding party is the specific way
  players lose this unlock.
- Because the beacon is guaranteed in the Mantis Homeworlds, the two gates can be shopped
  for deliberately — an Adv. Medbay upgrade or a teleporter bought one sector earlier is
  the whole difference between `MED scrap` and a ship unlock.
- On the Gate A branch there is never a reason to take *"put him out of his misery"* —
  *"listen"* pays the same `HIGH standard` **and** adds the cache
  ([[source-events-mantis]]).
- Fandom claims the Mantis Cruiser can also be unlocked by winning a run with the Zoltan
  Cruiser. `achievements.xml` in this raw set contains no such condition — recorded as
  Fandom-only, unverified ([[source-fandom-legendary-thief-kazaaakplethkilik]]).

## Related
- [[sector-mantis-homeworlds]] — the chain's sector
- [[item-mantis-pheromones]] — the augment awarded
- [[item-teleporter]], [[item-sensors]], [[item-medbay]], [[item-clone-bay]] — the gates
- [[chain-stealth-cruiser-unlock]], [[chain-rock-cruiser-unlock]] — the other two unlock
  chains that punish destroying the enemy ship
- [[concept-blue-options]]
- [[event-mantis-named-thief-defeat]] — step 2, the `MANTIS_NAMED_THIEF_DEFEAT` aftermath

## Open Questions
- [ ] Can the cache marker be placed in a sector after the Mantis Homeworlds?
- [ ] Is `all_skills="2"` the skill cap (i.e. is Fandom's "maxed in all skills" exact)?
- [ ] Does the Zoltan-Cruiser-victory unlock path exist? Not in `achievements.xml`.
- [ ] Which weapon pool `autoReward level="HIGH" weapon` draws from at the cache.
- [ ] Both step pages record `version: ae`; this page records `both` — the events sit in
      the base `events_mantis.xml` with no DLC markers and are not overridden in
      `dlcEvents*.xml`. Needs a lint decision.

## Sources
- [[source-events-mantis]] (per raw/gamedata/events_mantis.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-fandom-legendary-thief-kazaaakplethkilik]] (per raw/wiki/legendary-thief-kazaaakplethkilik.md)
