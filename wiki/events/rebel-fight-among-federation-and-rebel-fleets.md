---
id: event-rebel-fight-among-federation-and-rebel-fleets
type: event
event_name: BOSS_FLEETS_BOTH_FIGHT
sectors: [[[sector-the-last-stand]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [rebel, no-choice, combat, endgame, last-stand, fleet]
---

# Rebel fight among Federation and Rebel fleets — `BOSS_FLEETS_BOTH_FIGHT`

## Summary
A beacon in the middle of the two fleets grinding against each other in
[[sector-the-last-stand]]. Mechanically identical to
[[event-rebel-fight-among-rebel-fleet]] — it loads the very same `BOSS_FLEETS_REBEL` ship
block — but it sits in a different backdrop (`<fleet>battle</fleet>`) and, crucially, in a
different pair of event lists, so it can turn up on ordinary neutral beacons as well as
warning nodes.

## Trigger & Where It Appears
- Sector: [[sector-the-last-stand]] (`FINAL`).
- Beacon: hostile, with the two-fleet battle backdrop (`<fleet>battle</fleet>`). Long-range
  scanners show a ship ([[source-fandom-rebel-fight-among-federation-and-rebel-fleets]]).
- Event lists ([[source-events-boss]]):
  - `BOSS_NEUTRAL` — five entries (`BOSS_SCOUT_RESCUE`, `BOSS_FLEETS_BOTH_FIGHT`,
    `BOSS_FLEETS_FED`, `SQUAT_REFUEL_STATION`, `REBEL`), all distinct → **1/5** assuming
    uniform selection across list entries. `FINAL` allocates `BOSS_NEUTRAL` `min=7 max=10`
    and also uses it as the `startEvent` ([[source-sector-data-xml]]).
  - `BOSS_WARNING_NODE` — two entries → **1/2** assuming uniform selection.
- The XML comment: *"nodes that have ships fighting — also inside the /!\ symbol but can be
  elsewhere too."*

## Text
Drawn from the `BOSS_FLEETS_BOTH_FIGHT` text list: six distinct strings, each listed
twice, so 1/6 apiece assuming uniform selection across list entries
([[source-events-boss]], [[source-text-events-xml]]). Representative examples:

> You arrive in the middle of a raging battle. Both sides are taking heavy losses. A small
> squadron flies past and a fighter breaks off, moving toward your position.

> Two fleets fight nearby. You try to skirt around the edges of the battle and keep out of
> weapons range, but a Rebel scout spots you and moves in.

> You don't have any time to worry about the battle in the distance. The fight is coming to
> you really quickly!

All six are transcribed on [[source-fandom-rebel-fight-among-federation-and-rebel-fleets]]
and match the game strings verbatim.

There is a near-twin event, `BOSS_FLEETS_BOTH`, with its own six-string list and **no
ship** — same backdrop, purely atmospheric. It is not in any list in `events_boss.xml` and
is not covered by this page ([[source-events-boss]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event has no `<choice>` elements)* | — | Immediate combat with `<ship load="BOSS_FLEETS_REBEL" hostile="true"/>`. | 100% |

### The `BOSS_FLEETS_REBEL` ship
The same block used by [[event-rebel-fight-among-rebel-fleet]], defined in
`events_boss.xml` on the `SHIPS_REBEL` auto-blueprint ([[source-events-boss]]):

| Branch | Behaviour |
|---|---|
| `surrender` | none |
| `escape` | none |
| `destroyed` | *"There's no time to salvage all of the wreck, the fleet is still nearby. Get ready to jump!"* → `autoReward level="LOW"` `scrap_only` |
| `deadCrew` | *"There isn't time to salvage the enemy ship but your crew made off with a few nearby materials. Prepare to jump."* → `autoReward level="MED"` `standard` |

### Which hull you fight
> ⚠️ **Version difference (AE vs vanilla).** `SHIPS_REBEL` (vanilla: `REBEL_FAT`,
> `REBEL_SKINNY` — 1/2 each) is replaced in Advanced Edition by `OVERRIDE_SHIPS_REBEL`
> (`REBEL_FAT` ×2, `REBEL_SKINNY` ×2, `REBEL_FAT_DLC`, `REBEL_SKINNY_DLC` — 2/6, 2/6, 1/6,
> 1/6), assuming uniform selection across list entries ([[source-autoblueprints]],
> [[source-dlcblueprintsoverwrite]]).

## Blue Options
None.

## Rewards & Risks
- `LOW` `scrap_only` on a hull kill, `MED` `standard` on a crew kill. No surrender, no
  escape ([[source-events-boss]]).

## Strategy Notes
- Because this sits in `BOSS_NEUTRAL` — the largest allocation in the sector at 7–10
  beacons — the "neutral" beacons of the Last Stand are not safe. Roughly one draw in five
  from that list is this fight ([[source-sector-data-xml]], [[source-events-boss]]).
  *(Derived from list membership; the game states no percentage.)*

## Related
- [[event-rebel-fight-among-rebel-fleet]] — same ship block, different list and backdrop
- [[event-empty-beacon-last-stand]] — the harmless draw from the same `BOSS_NEUTRAL` list
- [[event-rebel-ship-attacking-civilians-in-last-stand]] — another `BOSS_NEUTRAL` member
- [[event-rebel-fight]] (`REBEL`) and [[event-rebel-ship-attacking-refueling-outpost]]
  (`SQUAT_REFUEL_STATION`) — the remaining `BOSS_NEUTRAL` members
- [[sector-the-last-stand]]
- [[entity-rebels]]
- [[event-boss-fleets-both]] — the shipless near-twin (`BOSS_FLEETS_BOTH`)

## Open Questions
- [ ] Whether `BOSS_FLEETS_BOTH` (the shipless twin) is reachable at all.

## Sources
- [[source-events-boss]] (per raw/gamedata/events_boss.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-dlcblueprintsoverwrite]] (per raw/gamedata/dlcBlueprintsOverwrite.xml)
- [[source-fandom-rebel-fight-among-federation-and-rebel-fleets]] (per raw/wiki/rebel-fight-among-federation-and-rebel-fleets.md)
