---
id: event-refugee-zoltan
type: event
event_name: REFUGEE_NO_DISTRESS_ZOLTAN
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [trading, ambush-risk, refugee, zoltan, advanced-edition]
---

# Refugee (Zoltan) — `REFUGEE_NO_DISTRESS_ZOLTAN`

## Summary
The Zoltan-sector, no-distress cut of the refugee encounter. Two-entry hail pool: barter,
or a Zoltan warship that accuses you of escorting fugitives and opens fire. Same pool as
[[event-refugee-distress-zoltan]].

## Trigger & Where It Appears
- Beacon: ordinary/neutral — no `<distressBeacon/>`, no environment tag
  ([[source-newevents]]).
- Sole list membership: `NEUTRAL_ZOLTAN`, marked `<!--DLC - In newEvents-->`
  ([[source-events-zoltan]], line 67).
- `NEUTRAL_ZOLTAN` serves [[sector-zoltan-controlled-sector]] and
  [[sector-zoltan-homeworlds]] ([[source-sector-data-xml]]).
- Not `unique`.

## Text
> Your sensors have picked up a refugee ship drifting through the system, no doubt one of
> many fleeing the Rebel advance. It doesn't appear to have detected you... or else it is
> trying to avoid notice.

(`event_REFUGEE_NO_DISTRESS_ZOLTAN_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Hail them. | — | Loads `REFUGEE_HAIL_LIST_ZOLTAN` — two entries, below. | — |
| 2 | Ignore the refugees. | — | `<event/>` — nothing happens. | 100% |

### `REFUGEE_HAIL_LIST_ZOLTAN`
Two members. **Assuming uniform selection across list entries**:

| Outcome | Entries | Share |
|---|---|---|
| `REFUGEE_TRADER` — a resource trade (below) | 1 | 1/2 |
| *"As you hail the refugee ship, a Zoltan ship suddenly jumps into the system... it claims the refugees are criminals, and accuses you of escorting fugitives! Before you can respond, it cuts communications, and powers up its weapons!"* → fight `ZOLTAN_REFUGEE` | 1 | 1/2 |

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

### `ZOLTAN_REFUGEE`
`auto_blueprint="SHIPS_ZOLTAN"`; **no surrender branch and no escape branch**
([[source-newevents]]):
- `destroyed` — *"The Zoltan ship breaks apart and you salvage what you can."* →
  `autoReward level="MED"` `standard`.
- `deadCrew` — *"The Zoltan ship, now empty of lifeforms, provides easy salvage."* →
  `autoReward level="HIGH"` `standard`.
- A hidden *"Contact the refugee ship."* follow-up then pays a further `LOW` `standard`.

## Blue Options
None — there is no Zoltan-crew option to vouch for the refugees, which is the obvious
missing branch here.

## Rewards & Risks
- 1/2 barter, 1/2 a committed fight against a Zoltan hull.
- The event is the mirror image of the sector's usual politics: in Zoltan space the Zoltan
  are the aggressors and the refugees are the innocents.

## Strategy Notes
- *(Opinion.)* Skipping is defensible. A Zoltan ship at even odds is a worse trade than
  the `TRADER_LIST` barter is worth, and Zoltan sectors already offer better beacons.

## Related
- [[event-refugee]] — generic no-distress version; the Zoltan ambush is only 1/8 there
- [[event-refugee-distress-zoltan]] — same pool behind a distress beacon
- [[entity-zoltan]]
- [[event-refugee-trader]] — the `REFUGEE_TRADER` trade sub-event, which carries its own page

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] Fandom's `{{Drifting Refugee Ship}}` template was not captured in the raw dump.

## Sources
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-events-zoltan]] (per `raw/gamedata/events_zoltan.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-refugee-zoltan]] (per `raw/wiki/refugee-zoltan.md`)
