---
id: event-refugee-distress-pirate
type: event
event_name: REFUGEE_DISTRESS_PIRATE
sectors: [[[sector-pirate-controlled-sector]]]
beacon_type: distress
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [distress, trading, ambush-risk, refugee, pirate, advanced-edition]
---

# Refugee distress (Pirate) — `REFUGEE_DISTRESS_PIRATE`

## Summary
The pirate-sector cut of [[event-refugee-distress]]. Identical prose and identical
choices, but the hail pool is trimmed from eight entries to **two** — a trade, or a pirate
ambush. That makes it a straight coin flip rather than the 4-in-8 trade of the generic
version.

## Trigger & Where It Appears
- Beacon: **distress signal** (`<distressBeacon/>`, [[source-newevents]]).
- Sole list membership: `DISTRESS_BEACON_PIRATE`, where it is the last entry and marked
  `<!--DLC - In newEvents-->` ([[source-events-pirate]], line 84).
- `DISTRESS_BEACON_PIRATE` is allocated `min=1 max=2` in `PIRATE_SECTOR`
  ([[source-sector-data-xml]]) → [[sector-pirate-controlled-sector]].
- Not `unique`.

## Text
> You have encountered a refugee ship drifting in space. It looks as if it was fleeing the
> Rebel advance and ran out of fuel. Its distress beacon is active, but you're not sure
> anyone is on board.

(`event_REFUGEE_DISTRESS_PIRATE_text` — byte-for-byte the same string as
`event_REFUGEE_DISTRESS_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Hail them. | — | Loads `REFUGEE_HAIL_LIST_PIRATE` — two entries, below. | — |
| 2 | Ignore the refugees. | — | `<event/>` — nothing happens. | 100% |

### `REFUGEE_HAIL_LIST_PIRATE`
Two members. **Assuming uniform selection across list entries** (the files state no
weights):

| Outcome | Entries | Share |
|---|---|---|
| `REFUGEE_TRADER` — a resource trade (below) | 1 | 1/2 |
| *"As you hail the refugee ship, a pirate ship jumps into the system... it was using the refugee ship as bait!"* → fight `PIRATE_REFUGEE` | 1 | 1/2 |

([[source-newevents]], [[source-text-events-xml]]) Derived from list contents, not a
stated percentage.

### `REFUGEE_TRADER` — the trade sub-event
*"The vessel is relieved to hear from you! They are running low on supplies. They suggest
a trade."* → **Trade with them** loads `TRADER_LIST` ([[source-events-xml]]), four equally
weighted barters; or **Politely decline** for nothing.

| Trade | You gain | You pay |
|---|---|---|
| 1 | 5–10 fuel | 1–2 drone parts |
| 2 | 4–5 missiles | 1–2 fuel |
| 3 | 2–3 drone parts | 2–3 missiles |
| 4 | 4–10 fuel | 2–4 missiles |

### `PIRATE_REFUGEE`
`auto_blueprint="SHIPS_PIRATE"`; **no surrender branch and no escape branch**, so the
fight runs to a conclusion ([[source-newevents]]):
- `destroyed` — *"The pirate ship breaks apart and you salvage what you can."* →
  `autoReward level="MED"` `standard`.
- `deadCrew` — *"The pirate ship, now empty of lifeforms, provides easy salvage."* →
  `autoReward level="HIGH"` `standard`.
- Either way a hidden follow-up, *"Contact the refugee ship."*, pays a further
  `autoReward level="LOW"` `standard`: *"The refugee ship claims pirates have been
  following their trail since they left their homeworld…"*

## Blue Options
None.

## Rewards & Risks
- 1/2 a barter; 1/2 a no-escape pirate fight worth `MED`/`HIGH` `standard` plus a `LOW`
  `standard` bonus.
- Because `PIRATE_REFUGEE` cannot surrender or flee, a hail that goes wrong is a committed
  fight.

## Strategy Notes
- *(Opinion, from the list structure.)* This is materially riskier than
  [[event-refugee-distress]] — the ambush share goes from 4/8 to 1/2, and the ship that
  shows up cannot be scared off.

## Related
- [[event-refugee-distress]] — the generic version, larger and safer pool
- [[event-refugee-pirate]] — the same pool at a non-distress beacon
- [[event-refugee-distress-slug]] — identical structure, same `PIRATE_REFUGEE` ship
- [[entity-pirates]]
- [[event-refugee-trader]] — the `REFUGEE_TRADER` trade sub-event, which carries its own page

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] Exact values behind `LOW` / `MED` / `HIGH` `standard`.
- [ ] Fandom's `{{Drifting Refugee Ship}}` template was not captured, so no independent
      outcome list is available to cross-check.

## Sources
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-events-pirate]] (per `raw/gamedata/events_pirate.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-refugee-distress-pirate]] (per `raw/wiki/refugee-distress-pirate.md`)
