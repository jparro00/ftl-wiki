---
id: event-refugee-pirate
type: event
event_name: REFUGEE_NO_DISTRESS_PIRATE
sectors: [[[sector-pirate-controlled-sector]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [trading, ambush-risk, refugee, pirate, advanced-edition]
---

# Refugee (Pirate) — `REFUGEE_NO_DISTRESS_PIRATE`

## Summary
The pirate-sector, no-distress cut of the refugee encounter: your sensors spot a drifting
refugee ship that has not seen you. Hailing rolls a two-entry pool — a barter or a pirate
ambush. Same pool as [[event-refugee-distress-pirate]]; only the framing differs.

## Trigger & Where It Appears
- Beacon: ordinary/neutral — **no** `<distressBeacon/>` tag ([[source-newevents]]).
- Sole list membership: `NEUTRAL_PIRATE`, last entry, marked `<!--DLC - In newEvents-->`
  ([[source-events-pirate]], line 60).
- `NEUTRAL_PIRATE` is the neutral pool of `PIRATE_SECTOR`
  ([[source-sector-data-xml]]) → [[sector-pirate-controlled-sector]].
- Not `unique`.

## Text
> Your sensors have picked up a refugee ship drifting through the system, no doubt one of
> many fleeing the Rebel advance. It doesn't appear to have detected you... or else it is
> trying to avoid notice.

(`event_REFUGEE_NO_DISTRESS_PIRATE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Hail them. | — | Loads `REFUGEE_HAIL_LIST_PIRATE` — two entries, below. | — |
| 2 | Ignore the refugees. | — | `<event/>` — nothing happens. | 100% |

### `REFUGEE_HAIL_LIST_PIRATE`
Two members. **Assuming uniform selection across list entries**:

| Outcome | Entries | Share |
|---|---|---|
| `REFUGEE_TRADER` — a resource trade (below) | 1 | 1/2 |
| *"As you hail the refugee ship, a pirate ship jumps into the system... it was using the refugee ship as bait!"* → fight `PIRATE_REFUGEE` | 1 | 1/2 |

([[source-newevents]], [[source-text-events-xml]]) Derived from list contents, not a
stated percentage.

### `REFUGEE_TRADER` — the trade sub-event
*"The vessel is relieved to hear from you! They are running low on supplies. They suggest
a trade."* → **Trade with them** loads `TRADER_LIST` ([[source-events-xml]]); or
**Politely decline** for nothing.

| Trade | You gain | You pay |
|---|---|---|
| 1 | 5–10 fuel | 1–2 drone parts |
| 2 | 4–5 missiles | 1–2 fuel |
| 3 | 2–3 drone parts | 2–3 missiles |
| 4 | 4–10 fuel | 2–4 missiles |

### `PIRATE_REFUGEE`
`auto_blueprint="SHIPS_PIRATE"`; no surrender, no escape ([[source-newevents]]).
`destroyed` → `MED` `standard`; `deadCrew` → `HIGH` `standard`; both then offer a hidden
*"Contact the refugee ship."* choice for a further `LOW` `standard`.

## Blue Options
None.

## Rewards & Risks
- 1/2 barter, 1/2 committed pirate fight.
- "It doesn't appear to have detected you" is flavour only — there is no stealth-based
  choice in the XML, and no way to loot the ship without hailing.

## Strategy Notes
- *(Opinion.)* In pirate space you will meet plenty of pirates anyway; an even-money
  fight for a barter you may not want is easy to skip.

## Related
- [[event-refugee]] — generic no-distress version, 4/8 trade share
- [[event-refugee-distress-pirate]] — identical pool behind a distress beacon
- [[entity-pirates]]
- [[event-refugee-trader]] — the `REFUGEE_TRADER` trade sub-event, which carries its own page

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] Fandom's `{{Drifting Refugee Ship}}` template was not captured in the raw dump.

## Sources
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-events-pirate]] (per `raw/gamedata/events_pirate.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-refugee-pirate]] (per `raw/wiki/refugee-pirate.md`)
