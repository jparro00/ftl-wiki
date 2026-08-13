---
id: event-rebel-fight-among-rebel-fleet
type: event
event_name: BOSS_FLEETS_REBEL
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

# Rebel fight among Rebel fleet — `BOSS_FLEETS_REBEL`

## Summary
The beacon behind the Rebel advance line in [[sector-the-last-stand]]. A Rebel fighter
peels off the fleet and attacks; there are no choices and the rewards are deliberately
poor, because the fiction is that you have no time to salvage. The same `BOSS_FLEETS_REBEL`
**ship** definition is reused by [[event-rebel-fight-among-federation-and-rebel-fleets]],
which is why the id appears on that page too.

## Trigger & Where It Appears
- Sector: [[sector-the-last-stand]] (`FINAL`).
- Beacon: hostile. `<fleet>rebel</fleet>` sets the Rebel-fleet backdrop; the XML comment
  says these are "areas that the fleet took over (or will take over soon)" and carry the
  ⚠ marker on the map ([[source-events-boss]]).
- Event list: `BOSS_WARNING_NODE` — a two-entry list holding `BOSS_FLEETS_REBEL` and
  `BOSS_FLEETS_BOTH_FIGHT`, so 1/2 each assuming uniform selection across list entries
  ([[source-events-boss]]).
- `BOSS_WARNING_NODE` has **no allocation in `sector_data.xml`** — the `FINAL` sector
  lists only `STORE`, `BOSS_REPAIR_STATION`, `BOSS_HOSTILE` and `BOSS_NEUTRAL`
  ([[source-sector-data-xml]]). The warning-node list is applied by the fleet-advance
  mechanic rather than by the sector's beacon allocation; the exact hook is not stated in
  the data files.
- [[source-fandom-rebel-fight-among-rebel-fleet]] files it under The Last Stand,
  `unique=false`, long-range scanners show a ship.

## Text
Drawn from the `BOSS_FLEETS_REBEL` text list: seven distinct strings, each listed twice,
so 1/7 apiece assuming uniform selection across list entries ([[source-events-boss]],
[[source-text-events-xml]]). Two of the seven (`_3`, `_6`) are tagged
`planet="PLANET_POPULATED"`. Representative examples:

> This system is flooded with Rebel warships. Luckily your ship's signature is disguised as
> a civilian transport. Most heavy vessels ignore you but a small fighter is approaching
> with weapons hot!

> Shots fly by and your computer registers multiple weapon locks as soon as you arrive.
> Evasive action!

> The Federation seems to have put up a good fight. A number of Rebel ships lie broken or
> wounded. However their overwhelming numbers force the remaining Federation forces to
> retreat. Hopefully you can get away in time as well.

> ⚠️ **CONTRADICTION:** the first string differs by one word.
> - Game files: *"**You** scanners can hardly register them all…"* (`text_BOSS_FLEETS_REBEL_1`,
>   [[source-text-events-xml]])
> - Fandom: *"**Your** scanners can hardly register them all…"*
>   ([[source-fandom-rebel-fight-among-rebel-fleet]])
>
> Trusting the game files — reliability `high` vs `medium`. This is almost certainly a
> typo in the shipped string that the wiki silently corrected, not a version difference.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event has no `<choice>` elements)* | — | Immediate combat with `<ship load="BOSS_FLEETS_REBEL" hostile="true"/>`. | 100% |

### The `BOSS_FLEETS_REBEL` ship
Defined in `events_boss.xml` itself (not `events_ships.xml`) on the `SHIPS_REBEL`
auto-blueprint ([[source-events-boss]]):

| Branch | Behaviour |
|---|---|
| `surrender` | none |
| `escape` | none |
| `destroyed` | *"There's no time to salvage all of the wreck, the fleet is still nearby. Get ready to jump!"* → `autoReward level="LOW"` `scrap_only` |
| `deadCrew` | *"There isn't time to salvage the enemy ship but your crew made off with a few nearby materials. Prepare to jump."* → `autoReward level="MED"` `standard` |

[[source-fandom-rebel-fight-among-rebel-fleet]] reports the same two branches and the same
reward levels.

### Which hull you fight
> ⚠️ **Version difference (AE vs vanilla).**
> - **Vanilla** — `SHIPS_REBEL`: `REBEL_FAT`, `REBEL_SKINNY`. 1/2 each assuming uniform
>   selection ([[source-autoblueprints]]).
> - **Advanced Edition** — `OVERRIDE_SHIPS_REBEL`, six entries: `REBEL_FAT` ×2,
>   `REBEL_SKINNY` ×2, `REBEL_FAT_DLC` ×1, `REBEL_SKINNY_DLC` ×1 → 2/6, 2/6, 1/6, 1/6
>   assuming uniform selection ([[source-dlcblueprintsoverwrite]]).

## Blue Options
None.

## Rewards & Risks
- Best case is `MED` `standard` (crew kill); a straight hull kill pays only `LOW`
  `scrap_only`. This is one of the stingiest forced fights in the game
  ([[source-events-boss]]).
- Risk: no surrender, no escape — the fight runs to a conclusion.

## Strategy Notes
- The reward structure inverts the usual advice: boarding or otherwise killing the crew
  pays materially better than blowing the hull. *(Reading of the two reward tags, not a
  sourced strategy claim.)*

## Related
- [[event-rebel-fight-among-federation-and-rebel-fleets]] — loads the **same** ship block
- [[event-fight-in-last-stand]] — the sector's other guaranteed hostile beacon
- [[sector-the-last-stand]]
- [[entity-rebels]]

## Open Questions
- [ ] Exactly how `BOSS_WARNING_NODE` is allocated — it is in no `sectorDescription`.
- [ ] Whether the ⚠ map marker is what selects this list, as the XML comment implies.

## Sources
- [[source-events-boss]] (per raw/gamedata/events_boss.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-dlcblueprintsoverwrite]] (per raw/gamedata/dlcBlueprintsOverwrite.xml)
- [[source-fandom-rebel-fight-among-rebel-fleet]] (per raw/wiki/rebel-fight-among-rebel-fleet.md)
