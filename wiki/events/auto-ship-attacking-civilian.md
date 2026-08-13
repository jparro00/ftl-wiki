---
id: event-auto-ship-attacking-civilian
type: event
event_name: AUTO_CIVILIAN
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]]]
beacon_type: hostile
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [rebel, auto-ship, optional-fight, crew-reward-chance, save-civilian]
---

# Auto-ship attacking civilian — `AUTO_CIVILIAN`

## Summary
An optional auto-ship fight with a rescue attached: intervene, kill the automated scout,
and you get a roll on the shared `SAVE_CIVILIAN_LIST` — the table that can hand you a free
crew member, a weapon, or a hull repair. Or leave and lose nothing. It is one of the few
entries in the generic hostile pools that is not actually a forced fight.

## Trigger & Where It Appears
- Sectors: [[sector-civilian-sector]], [[sector-federation-space]],
  [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]].
- Event lists: `NEUTRAL_REBEL` ([[source-events-rebel]]), `HOSTILE1`
  ([[source-newevents]]), `OVERRIDE_HOSTILE1` ([[source-dlceventsoverwrite]]).
  `NEUTRAL_REBEL` is allocated `min=5 max=6` per Rebel sector
  ([[source-sector-data-xml]]).
- Beacon: filed under the hostile pools, but no ship is hostile on arrival — combat only
  starts if you choose it.
- `unique="false"` — explicitly declared; it can recur.
- Long-range scanners show **no ship** ([[source-fandom-auto-ship-attacking-civilian]]).

> ⚠️ **CONTRADICTION (reach):** [[source-fandom-auto-ship-attacking-civilian]] lists
> Civilian Sector, Rebel Controlled Sector and Rebel Stronghold. The event also sits in the
> generic `HOSTILE1` / `OVERRIDE_HOSTILE1` pools, which [[sector-federation-space]] draws on
> ([[source-newevents]], [[source-dlceventsoverwrite]]). Trusting the game files.

## Text
> You come across a Rebel automated scout ship pursuing a civilian ship, weapons engaged.

(`event_AUTO_CIVILIAN_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Aid the civilian ship. | — | *"You power up your weapons and engage the automated ship."* → fight `<ship load="REBEL_AUTO_CIVILIAN" hostile="true"/>`. On destruction: `autoReward level="LOW"` `standard`, then a hidden follow-up choice *"Contact the civilian ship"* → rolls `SAVE_CIVILIAN_LIST`. | 100% (deterministic) |
| 2 | Stay out of it. | — | *"The fight brings them out of your immediate scanning range."* → nothing happens. | 100% |

### The `REBEL_AUTO_CIVILIAN` ship
`auto_blueprint="SHIPS_AUTO"`, no surrender and no escape branch
([[source-events-ships]]):

- **`destroyed`** — *"The ship breaks apart. You hasten to contact the civilian ship."* →
  `autoReward level="LOW"` `standard`, plus the hidden `SAVE_CIVILIAN_LIST` choice.
- **`deadCrew`** — *"No more life signs detected on the pirate ship. You hasten to contact
  the civilian ship."* → `autoReward level="MED"` `standard`, plus the same choice.
  Auto-ships carry no crew, so this branch is effectively unreachable — and the string says
  "pirate ship", an in-file wording slip quoted as-is (the same slip appears on
  [[event-mantis-ship-attacking-civilian]]).

### Choice 1 follow-up — `SAVE_CIVILIAN_LIST`
The shared six-entry list defined in `raw/gamedata/events_pirate.xml`
([[source-events-pirate]]). One entry is drawn at random; the file states no weights, so
the odds are **unknown**:

| Entry | Result |
|---|---|
| 1 | A survivor offers to join → **+1 crew member** if you accept, nothing if you decline |
| 2 | Science vessel thanks you → `autoReward level="MED"` `standard` |
| 3 | Crew did not survive; you loot the remains → `autoReward level="LOW"` `standard` |
| 4 | A shipwright offers to install equipment → `autoReward level="LOW"` `weapon` |
| 5 | They patch your hull → `<damage amount="-5"/>`, i.e. **5 hull repaired** |
| 6 | The civilian already fled → nothing |

Fandom folds this in behind its `{{Save the Civilian Ship}}` template rather than
transcribing it ([[source-fandom-auto-ship-attacking-civilian]]).

## Blue Options
None. Neither choice carries a `req=`.

## Rewards & Risks
- Reward path: `LOW` `standard` for the kill, then one `SAVE_CIVILIAN_LIST` roll — best
  case a free crew member or a weapon, worst case nothing at all.
- Risk: an auto-ship fight you did not have to take. No boarding threat (no crew), no
  surrender, no escape — the fight runs to a hull kill.
- Choice 2 is mechanically free.

## Strategy Notes
- *(Opinion.)* Better expected value than the average optional auto-ship fight, because
  the base payout is only `LOW` but the rescue table carries the two best outcomes in the
  game's filler economy — a crew member and a hull repair. Take it when your weapons out-tempo
  the sector; skip it at low hull, since there is no surrender to bail you out.
- Two of six rescue entries pay nothing or nearly nothing, so this is not guaranteed profit.

## Related
- [[concept-event-tree-grammar]] — the node grammar every event is built from
- [[event-mantis-ship-attacking-civilian]] — the Mantis version, same `SAVE_CIVILIAN_LIST` table
- [[event-auto-ship-fight]] — the unavoidable version of the same auto-ship fight
- [[event-auto-ship-attacking-outpost]] — the same "intervene or not" shape, station instead of civilian
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Weights inside `SAVE_CIVILIAN_LIST` — six entries, no `prop` attributes.
- [ ] Species of the `<crewMember amount="1"/>` on entry 1.
- [ ] Numeric values of `LOW` / `MED` `standard`.

## Sources
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-events-pirate]] (per `raw/gamedata/events_pirate.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-auto-ship-attacking-civilian]] (per `raw/wiki/auto-ship-attacking-civilian.md`)
