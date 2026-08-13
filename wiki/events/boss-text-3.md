---
id: event-boss-text-3
type: event
event_name: BOSS_TEXT_3
sectors: [[[sector-the-last-stand]]]
beacon_type: quest
hostile: true
blue_options: []
chain: [[[chain-the-flagship]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [endgame, last-stand, orphan, scripted, flagship, boss, boarding, text-only]
---

# Rebel Flagship, phase 3 — `BOSS_TEXT_3`

## Summary
The announcement for the final Flagship engagement — the one where it starts teleporting
boarders and firing what the text calls a super weapon. A bare `<text>` tag in the data;
the phase-3 blueprint is the leanest of the three, trading artillery and drones for a
teleporter, triple engine power and an `invasion` boarding AI.

## Trigger & Where It Appears
- **Orphan in the data.** `BOSS_TEXT_3` appears in no `eventList` and no
  `sectorDescription`; the only references in `raw/gamedata/` are its own definition and
  the file's header comment ([[source-events-boss]], [[source-sector-data-xml]]).
- Reached by the endgame scripting when you re-engage the Flagship after phase 2, in
  [[sector-the-last-stand]].

## Text
> You're not certain how it's able to keep fighting with the amount of damage it has
> sustained. It looks like it's transferred power to the teleporter as well as... some kind
> of super weapon. Be prepared... this is it!

(`event_BOSS_TEXT_3_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event is a single `<text>` tag)* | — | Text only; the phase-3 fight is set up outside the event. | 100% |

## The phase-3 ship

| | `BOSS_3_EASY` | `BOSS_3_NORMAL` | `BOSS_3_HARD` |
|---|---|---|---|
| Layout | `boss_3_easy` | `boss_3_easy` | `boss_3` |
| Hull | 20 | 20 | 20 |
| Max power | 29 | 31 | 31 |
| Shields | 6 (3 layers) | 8 (4 layers) | 8 (4 layers) |
| Engines | 6 | 6 | 6 |
| Teleporter | 2 | 2 | 2 |
| Other systems | pilot 3, medbay 3, oxygen 2 | same | same |
| Artillery | `ARTILLERY_BOSS_1` ×4 pwr, `_2` ×4 | same | same |
| Boarding AI | `invasion` | `invasion` | `invasion` |

(per [[source-bosses]])

Phase 3 keeps only the laser and missile artillery mounts, has no drone system and no
drone list, and no doors or cloaking. `<boardingAI>invasion</boardingAI>` is what backs the
"transferred power to the teleporter" line ([[source-bosses]]).

> ⚠️ **Version difference (AE vs vanilla) — the biggest of the three phases.** The `_DLC`
> phase-3 blueprints add **`<mind power="3" room="4"/>` — a Mind Control system** and raise
> max power to 32; `BOSS_3_EASY_DLC` is additionally lifted to 8 shield power. The
> `hacking` tag is present but commented out on all three. So in Advanced Edition the final
> phase mind-controls your crew while boarding you; in vanilla it only boards
> ([[source-bosses]]).

### The artillery
| Mount | Title | Type | Effect |
|---|---|---|---|
| `ARTILLERY_BOSS_1` | Boss Laser | laser | 1 damage × 3 shots, cooldown 20, fire chance 1, breach chance 1 |
| `ARTILLERY_BOSS_2` | Boss Missile | missile | 1 damage × 3 shots, **shield-piercing 5**, cooldown 23, fire chance 3, breach chance 2 |

(per [[source-blueprints]])

**The "super weapon" is not in these files.** No phase-3 blueprint in `bosses.xml` or
`blueprints.xml` carries a weapon beyond the two artillery mounts, and
`<weaponList count="0" missiles="10"/>` is empty. Whatever the text refers to is
implemented outside the data examined here — do not assume it is one of the artillery
tags.

> ⚠️ **CONTRADICTION:** `blueprints.xml` defines an unsuffixed `BOSS_3` matching
> `BOSS_3_NORMAL` exactly (8 shields, 6 engines, teleporter 2, 31 max power, `invasion`),
> plus two further variants the difficulty set does not have: `BOSS_SPECIAL` (10 hull,
> 14 max power, scaling `power`/`max` system entries, `hacking` and `mind` present but
> `start="false"`, `boardingAI` `sabotage`, `crewCount` 3–8 human) and `BOSS_DEMO`
> (20 hull, 30 max power, 6 human crew, `sabotage` AI, 24 missiles). Neither is referenced
> by any event or sector in `raw/gamedata/` ([[source-blueprints]]). Their role is
> unresolved — `BOSS_DEMO` reads as demo-build content and `BOSS_SPECIAL` as a scripted
> variant.

## Blue Options
None.

## Rewards & Risks
The event grants nothing. Destroying the ship here routes to [[event-boss-destroyed]];
killing its crew without destroying it routes to [[event-boss-automated]].

## Strategy Notes
None sourced. The mechanical facts: a live teleporter with `invasion` AI, 6 engine power
(the highest of the three phases), only two artillery mounts, and — in Advanced Edition
only — Mind Control ([[source-bosses]]).

## Related
- [[event-boss-text-1]] — phase 1
- [[event-boss-text-2]] — phase 2
- [[event-boss-destroyed]] — the ending this phase leads to
- [[event-boss-automated]], [[event-boss-escaped]]
- [[sector-the-last-stand]], [[chain-the-flagship]]
- [[entity-flagship]], [[entity-rebels]]
- [[item-mind-control]], [[item-teleporter]]

## Open Questions
- [ ] What the "super weapon" is in the data — it is not in `bosses.xml` or the artillery
      blueprints.
- [ ] What `BOSS_SPECIAL` and `BOSS_DEMO` are for; neither is referenced anywhere.
- [ ] Which blueprint set the game actually loads (`BOSS_3` vs `BOSS_3_<difficulty>`).

## Sources
- [[source-events-boss]] (per raw/gamedata/events_boss.xml)
- [[source-bosses]] (per raw/gamedata/bosses.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
