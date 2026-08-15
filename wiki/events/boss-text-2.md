---
id: event-boss-text-2
type: event
event_name: BOSS_TEXT_2
sectors: [[[sector-the-last-stand]]]
beacon_type: quest
hostile: true
blue_options: []
chain: [[[chain-the-flagship]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [endgame, last-stand, orphan, scripted, flagship, boss, drones, text-only]
---

# Rebel Flagship, phase 2 — `BOSS_TEXT_2`

## Summary
The announcement for the Flagship's second engagement, in which it has dumped power into
its drone bay. A bare `<text>` tag in the data — the fight is configured from `bosses.xml`,
and the phase-2 blueprint is the only one of the three that ships a drone loadout.

## Trigger & Where It Appears
- **Orphan in the data.** `BOSS_TEXT_2` appears in no `eventList` and no
  `sectorDescription`; the only references in `raw/gamedata/` are its own definition and
  the file's header comment ([[source-events-boss]], [[source-sector-data-xml]]).
- Reached by the endgame scripting when you re-engage the Flagship after phase 1, in
  [[sector-the-last-stand]].

## Text
> You chase down the flagship and discover it is heavily damaged from the previous fight.
> Scans indicate that it has redirected considerable power to its drones. Get ready for a
> fight.

(`event_BOSS_TEXT_2_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event is a single `<text>` tag)* | — | Text only; the phase-2 fight is set up outside the event. | 100% |

## The phase-2 ship

| | `BOSS_2_EASY` | `BOSS_2_NORMAL` | `BOSS_2_HARD` |
|---|---|---|---|
| Layout | `boss_2_easy` | `boss_2_easy` | `boss_2` |
| Hull | 22 | 22 | 22 |
| Max power | 42 | 44 | 44 |
| Shields | 6 (3 layers) | 8 (4 layers) | 8 (4 layers) |
| Engines | 3 | 3 | 3 |
| Drone system | 8 | 8 | 8 |
| Other systems | pilot 3, medbay 3, oxygen 2 | same | same |
| Artillery | `ARTILLERY_BOSS_1` ×4 pwr, `_2` ×4, `_3` ×3 | same | same |

(per [[source-bosses]])

Phase 2 drops the fourth artillery mount (`ARTILLERY_BOSS_4`, the ion) and the doors and
cloaking systems of phase 1, and spends the difference on drones: `<droneList count="4"
drones="10">` carrying **`DEFENSE_1`, `COMBAT_1`, `COMBAT_BEAM`, `BOARDER_BOSS`** with 10
drone parts in reserve ([[source-bosses]]). `BOARDER_BOSS` is a dedicated boarding drone —
2 power, speed 18, *"Breaches through the enemy hull and wreaks havoc"*
([[source-blueprints]]). Conventional weapons remain switched off
(`<weaponList count="0" missiles="10"/>`, `weapons` and `sensors` commented out).

> ⚠️ **Version difference (AE vs vanilla).** The `_DLC` phase-2 blueprints
> (`BOSS_2_EASY_DLC`, `BOSS_2_NORMAL_DLC`, `BOSS_2_HARD_DLC`) are **identical in systems**
> to their base counterparts — the `hacking` and `mind` tags are present but commented out
> — except that `BOSS_2_EASY_DLC` is raised to 8 shield power / 44 max power, matching
> Normal. So Advanced Edition changes phase 2 only by removing the Easy-difficulty shield
> discount ([[source-bosses]]).

### The artillery
| Mount | Title | Type | Effect |
|---|---|---|---|
| `ARTILLERY_BOSS_1` | Boss Laser | laser | 1 damage × 3 shots, cooldown 20, fire chance 1, breach chance 1 |
| `ARTILLERY_BOSS_2` | Boss Missile | missile | 1 damage × 3 shots, **shield-piercing 5**, cooldown 23, fire chance 3, breach chance 2 |
| `ARTILLERY_BOSS_3` | Boss Beam | beam | 2 damage per room, length 100, cooldown 26 |

(per [[source-blueprints]])

> ⚠️ **CONTRADICTION:** `blueprints.xml` also defines an unsuffixed `BOSS_2` with the same
> drone loadout and artillery but with a **teleporter (power 2) and sensors (power 2)**
> enabled — neither of which any `bosses.xml` phase-2 variant has ([[source-blueprints]] vs
> [[source-bosses]]). The files do not say which is loaded; see the same note on
> [[event-boss-text-1]].

## Blue Options
None.

## Rewards & Risks
The event grants nothing. Ending the phase without destroying the ship routes to
[[event-boss-escaped]] (which does pay `autoReward level="HIGH"` `standard`); killing the
crew without killing the hull routes to [[event-boss-automated]].

## Strategy Notes
None sourced. The mechanical facts: four drones including a boarding drone and a defence
drone, 10 spare drone parts, and 8 power in the drone system — phase 2 is the drone phase
by construction ([[source-bosses]]).

## Related
- [[event-boss-text-1]] — phase 1
- [[event-boss-text-3]] — phase 3
- [[event-boss-escaped]], [[event-boss-automated]], [[event-boss-destroyed]]
- [[sector-the-last-stand]], [[chain-the-flagship]]
- [[entity-flagship]], [[entity-rebels]]
- [[item-boarding-drone]], [[item-defense-drone-mark-i]], [[item-combat-drone-mark-i]]

## Open Questions
- [ ] Which blueprint set the game actually loads (`BOSS_2` vs `BOSS_2_<difficulty>`).
- [ ] Whether the drone list is fixed or the ship re-launches from a pool when one dies.

## Sources
- [[source-events-boss]] (per raw/gamedata/events_boss.xml)
- [[source-bosses]] (per raw/gamedata/bosses.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
