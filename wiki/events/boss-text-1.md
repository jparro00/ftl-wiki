---
id: event-boss-text-1
type: event
event_name: BOSS_TEXT_1
sectors: [[[sector-the-last-stand]]]
beacon_type: quest
hostile: true
blue_options: []
chain: [[[chain-the-flagship]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [endgame, last-stand, orphan, scripted, flagship, boss, text-only]
---

# Rebel Flagship, phase 1 — `BOSS_TEXT_1`

## Summary
The event that announces the first Flagship engagement. Like its two siblings it is a bare
`<text>` tag — it carries no ship, no reward and no status effect, because the fight itself
is set up by the endgame scripting from `bosses.xml`, not by the event. The page documents
the phase-1 loadout alongside the text because that is the only place the two are usefully
joined.

## Trigger & Where It Appears
- **Orphan in the data.** `BOSS_TEXT_1` appears in no `eventList` and no
  `sectorDescription`; the only references in `raw/gamedata/` are its own definition and
  the file header comment listing the boss-sequence events
  ([[source-events-boss]], [[source-sector-data-xml]]).
- Reached by the endgame scripting when the Flagship is first engaged at the Federation
  Base beacon in [[sector-the-last-stand]].

## Text
> This is it... The Rebel flagship. If you are able to destroy this monstrosity, the
> Federation fleet will have a chance of surviving. There's no turning back!

(`event_BOSS_TEXT_1_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event is a single `<text>` tag)* | — | Text only; the phase-1 fight is set up outside the event. | 100% |

## The phase-1 ship
`bosses.xml` defines a separate blueprint per difficulty, and a second set for Advanced
Edition. All of them are called **"Rebel Flagship"** in
`text_blueprints.xml` ([[source-text-blueprints]]).

| | `BOSS_1_EASY` | `BOSS_1_NORMAL` | `BOSS_1_HARD` |
|---|---|---|---|
| Layout | `boss_1_easy` | `boss_1_easy` | `boss_1` |
| Hull | 20 | 20 | 20 |
| Max power | 40 | 42 | 42 |
| Shields | 6 (3 layers) | 8 (4 layers) | 8 (4 layers) |
| Engines | 2 | 2 | 2 |
| Other systems | pilot 3, doors 3, cloaking 2, medbay 3, oxygen 2 | same | same |
| Artillery | `ARTILLERY_BOSS_1` ×4 pwr, `_2` ×4, `_3` ×3, `_4` ×3 | same | same |

(per [[source-bosses]])

> ⚠️ **Version difference (AE vs vanilla).** `bosses.xml` carries a second block of
> blueprints suffixed `_DLC` under a `DLC!!!` banner comment. `BOSS_1_EASY_DLC`,
> `BOSS_1_NORMAL_DLC` and `BOSS_1_HARD_DLC` are identical to their base counterparts
> **except** that each adds `<hacking power="3" room="2"/>` and `BOSS_1_EASY_DLC` is raised
> to 8 shield power / 42 max power. So in Advanced Edition phase 1 has a **Hacking system**
> and there is no Easy-difficulty shield discount ([[source-bosses]]). A `<mind …>` tag is
> present but commented out in all three.

Weapons and drones are switched off on this phase: `<weaponList count="0" missiles="10"/>`
and `<droneList count="0" missiles="2"/>`, with the `weapons`, `sensors` and `drones`
system entries commented out. Everything it fires comes from the four artillery mounts
([[source-bosses]]).

### The artillery
| Mount | Title | Type | Effect |
|---|---|---|---|
| `ARTILLERY_BOSS_1` | Boss Laser | laser | 1 damage × 3 shots, cooldown 20, fire chance 1, breach chance 1 |
| `ARTILLERY_BOSS_2` | Boss Missile | missile | 1 damage × 3 shots, **shield-piercing 5**, cooldown 23, fire chance 3, breach chance 2 |
| `ARTILLERY_BOSS_3` | Boss Beam | beam | 2 damage per room, length 100, cooldown 26 |
| `ARTILLERY_BOSS_4` | Boss Ion | ion | 1 ion damage × 3 shots, speed 40, cooldown 28 |

(per [[source-blueprints]]; all four are flagged `NOLOC="1"` and their `desc` fields are
placeholder text — `"ssss"`, `"Fsss"` — so they are never shown to the player.)

> ⚠️ **CONTRADICTION:** `blueprints.xml` also defines an **unsuffixed** `BOSS_1`
> (`ship_BOSS_1_class`, also "Rebel Flagship") with 8 shields, 42 max power and a
> *teleporter, sensors and drone system enabled* — none of which the `bosses.xml` phase-1
> variants have ([[source-blueprints]] vs [[source-bosses]]). The data files do not state
> which blueprint the running game selects. Most likely `BOSS_1` is the legacy
> pre-difficulty definition superseded by the `_EASY`/`_NORMAL`/`_HARD` set, but that is
> not confirmed here.

## Blue Options
None.

## Rewards & Risks
The event grants nothing. Losing the phase-1 fight ends the run; the Flagship escaping
instead of dying routes to [[event-boss-escaped]], and killing its crew rather than the
hull routes to [[event-boss-automated]].

## Strategy Notes
None sourced. The mechanical facts worth carrying forward: four artillery mounts, one of
them shield-piercing; cloaking; and no conventional weapons system to disable — only the
artillery rooms ([[source-bosses]]).

## Related
- [[event-boss-text-2]] — phase 2
- [[event-boss-text-3]] — phase 3
- [[event-boss-escaped]] — what fires when a phase ends without a kill
- [[event-boss-automated]] — what fires when the crew dies but the ship does not
- [[event-federation-base]], [[event-last-stand-start]]
- [[sector-the-last-stand]], [[chain-the-flagship]]
- [[entity-flagship]], [[entity-rebels]]

## Open Questions
- [ ] Which blueprint set the game actually loads (`BOSS_1` vs `BOSS_1_<difficulty>`).
- [ ] Whether the flagship's crew complement is defined anywhere in `raw/gamedata/`; none
      of the phase blueprints carries a `<crewCount>` tag.

## Sources
- [[source-events-boss]] (per raw/gamedata/events_boss.xml)
- [[source-bosses]] (per raw/gamedata/bosses.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
