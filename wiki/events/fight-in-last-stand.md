---
id: event-fight-in-last-stand
type: event
event_name: BOSS_SCOUT
sectors: [[[sector-the-last-stand]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 8
tags: [rebel, auto-ship, no-choice, default-rewards, combat, endgame, last-stand]
---

# Fight in Last Stand — `BOSS_SCOUT`

## Summary
The plain hostile beacon of [[sector-the-last-stand]]. No choices: you arrive, a Rebel
scout or an automated ship is already hostile, and you fight it. `sector_data.xml`
allocates **exactly six** of these per run of the final sector, which makes this the most
common combat encounter of the endgame ([[source-sector-data-xml]]).

## Trigger & Where It Appears
- Sector: [[sector-the-last-stand]] only (`FINAL`).
- Beacon: hostile — the event loads a hostile ship on arrival. Long-range scanners show a
  ship ([[source-fandom-fight-in-last-stand]]).
- Event list: `BOSS_HOSTILE` ([[source-events-boss]]), which is allocated
  `min=6 max=6` beacons in `FINAL` ([[source-sector-data-xml]]).
- `BOSS_HOSTILE` contains three entries and **all three are `BOSS_SCOUT`**, so drawing
  that list always yields this event (assuming uniform selection across list entries)
  ([[source-events-boss]]).
- `unique="false"` — it recurs freely within the sector ([[source-events-boss]]).

## Text
The prose is drawn from the `BOSS_SCOUT` text list and **varies across six strings**
(`text_BOSS_SCOUT_1` … `_6`), each entry appearing once — 1/6 apiece assuming uniform
selection across list entries ([[source-events-boss]], [[source-text-events-xml]]).
Representative examples:

> Although this sector is still under Federation control, a small scout has slipped by the
> fleet. You move in to engage.

> As soon as you arrive at the beacon, a Rebel scout turns to engage. Power up the weapons!

> You scan the area, finding signatures for only a small trade vessel. However, as it
> approaches you see the silhouette of a Rebel scout! You run the scanners again and
> discover their registration is fake. You move in to attack.

All six are transcribed on [[source-fandom-fight-in-last-stand]] and in
`raw/gamedata/text_events.xml`. The XML comments tag the first three with intended
backgrounds — fleet background, no fleets, and no fleet + empty planet.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event has no `<choice>` elements)* | — | Immediate combat with `<ship load="REBEL_AND_AUTO" hostile="true"/>`, **default rewards**. | 100% |

### The `REBEL_AND_AUTO` ship
Defined in `raw/gamedata/events_ships.xml` on the `SHPS_REBEL_AND_AUTO` auto-blueprint
([[source-events-ships]]):

| Branch | Behaviour |
|---|---|
| `surrender` | none — the ship never offers to surrender |
| `escape` | none — the ship never flees |
| `destroyed` | `DESTROYED_DEFAULT` — `autoReward level="MED"` `standard` (both entries) |
| `deadCrew` | `DEAD_CREW_DEFAULT` — a nine-entry list of `MED`/`HIGH` `standard`, `HIGH` `fuel`, a crew member with `LOW` `scrap_only`, and `LOW` `weapon` ([[source-events-xml]]) |

Note that an automated hull has no crew, so the `deadCrew` branch is only reachable when
the draw produces one of the two Rebel hulls.

### Which hull you fight
> ⚠️ **Version difference (AE vs vanilla).** The enemy is drawn from a blueprint list that
> Advanced Edition replaces wholesale.
>
> - **Vanilla** — `SHPS_REBEL_AND_AUTO`: `AUTO_BASIC`, `AUTO_ASSAULT`, `REBEL_FAT`,
>   `REBEL_SKINNY`. Four distinct entries → 1/4 each, assuming uniform selection across
>   list entries ([[source-autoblueprints]]).
> - **Advanced Edition** — `OVERRIDE_SHPS_REBEL_AND_AUTO`, twelve entries: the four base
>   hulls listed **twice** each plus `AUTO_BASIC_DLC`, `AUTO_ASSAULT_DLC`,
>   `REBEL_FAT_DLC`, `REBEL_SKINNY_DLC` once each. So 2/12 for each base hull and 1/12 for
>   each AE hull, assuming uniform selection across list entries
>   ([[source-dlcblueprintsoverwrite]]).
>
> [[source-fandom-fight-in-last-stand]] reports the same twelve-entry weighting in
> readable names: 2× Auto-Scout, 1× Auto-Surveyor, 2× Auto-Assault, 1× Auto-Hacker,
> 2× Rebel Rigger, 1× Rebel Disruptor, 2× Rebel Fighter, 1× Rebel Invader. Game files and
> Fandom agree.

## Blue Options
None — the event has no `req`-gated choices.

## Rewards & Risks
- Default rewards on a kill: `MED` `standard` for a hull kill, or the `DEAD_CREW_DEFAULT`
  spread for a crew kill ([[source-events-xml]]).
- Risk: six of these are guaranteed and none of them can be talked out of — there is no
  surrender and no escape branch. This is where Last Stand attrition comes from.

## Strategy Notes
- The Flagship fight is not reachable without crossing the sector, and six forced fights
  plus the `BOSS_NEUTRAL` draws mean hull and missile spend here is unavoidable. The three
  guaranteed [[event-repair-station-in-last-stand]] beacons exist to offset it.
  *(Reading of the sector allocation, not a sourced strategy claim.)*

## Related
- [[sector-the-last-stand]] — the only sector this appears in
- [[event-rebel-fight-among-rebel-fleet]] — the other guaranteed-hostile Last Stand fight
- [[event-rebel-fight-among-federation-and-rebel-fleets]] — hostile draw from `BOSS_NEUTRAL`
- [[event-repair-station-in-last-stand]] — the counterweight beacons
- [[entity-rebels]]

## Open Questions
- [ ] Whether `BOSS_HOSTILE`'s three identical entries are a stub for planned variants.

## Sources
- [[source-events-boss]] (per raw/gamedata/events_boss.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-dlcblueprintsoverwrite]] (per raw/gamedata/dlcBlueprintsOverwrite.xml)
- [[source-fandom-fight-in-last-stand]] (per raw/wiki/fight-in-last-stand.md)
