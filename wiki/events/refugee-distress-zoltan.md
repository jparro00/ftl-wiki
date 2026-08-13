---
id: event-refugee-distress-zoltan
type: event
event_name: REFUGEE_DISTRESS_ZOLTAN
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: distress
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [distress, trading, ambush-risk, refugee, zoltan, advanced-edition]
---

# Refugee distress (Zoltan) — `REFUGEE_DISTRESS_ZOLTAN`

## Summary
The Zoltan-sector cut of [[event-refugee-distress]]. Same prose, same two choices, two-entry
hail pool: a trade, or a Zoltan warship that accuses you of harbouring fugitives. The only
member of the refugee family whose ambusher is a Zoltan ship.

## Trigger & Where It Appears
- Beacon: **distress signal** (`<distressBeacon/>`, [[source-newevents]]).
- Sole list membership: `DISTRESS_BEACON_ZOLTAN`, marked `<!--DLC - In newEvents-->`
  ([[source-events-zoltan]], line 113).
- `DISTRESS_BEACON_ZOLTAN` is allocated `min=1 max=2` in both `ZOLTAN_SECTOR` and
  `ZOLTAN_HOME` ([[source-sector-data-xml]]) → [[sector-zoltan-controlled-sector]] and
  [[sector-zoltan-homeworlds]].
- Not `unique`.

## Text
> You have encountered a refugee ship drifting in space. It looks as if it was fleeing the
> Rebel advance and ran out of fuel. Its distress beacon is active, but you're not sure
> anyone is on board.

(`event_REFUGEE_DISTRESS_ZOLTAN_text`, identical to the generic string, per
[[source-text-events-xml]])

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
- Either way a hidden *"Contact the refugee ship."* follow-up pays a further
  `autoReward level="LOW"` `standard`.

Zoltan hulls come with a Zoltan Shield super-shield, so "no escape branch" cuts both ways
— the fight is committed and it starts behind a shield layer that ignores most damage
types. (That property is a `SHIPS_ZOLTAN` blueprint fact, not stated in this event's
files — see [[entity-zoltan]].)

## Blue Options
None — no Zoltan-crew option to talk the warship down.

## Rewards & Risks
- 1/2 barter, 1/2 a committed Zoltan fight worth `MED`/`HIGH` `standard` plus a `LOW`
  `standard` bonus.
- The Zoltan ambush is the harshest of the four refugee ambushers by ship class, and this
  is the only pool where it is an even-money outcome.

## Strategy Notes
- *(Opinion, from the list structure.)* Hailing here is the worst-value hail in the
  family: even odds on a fight against a Zoltan hull, for the same `TRADER_LIST` barter
  you could get anywhere else.

## Related
- [[event-refugee-distress]] — generic version; the Zoltan ambush is only 1/8 there
- [[event-refugee-zoltan]] — the same pool at a non-distress beacon
- [[entity-zoltan]]
- [[event-refugee-trader]] — the `REFUGEE_TRADER` trade sub-event, which carries its own page

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] Exact values behind `LOW` / `MED` / `HIGH` `standard`.
- [ ] Fandom's `{{Drifting Refugee Ship}}` template was not captured in the raw dump.

## Sources
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-events-zoltan]] (per `raw/gamedata/events_zoltan.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-refugee-distress-zoltan]] (per `raw/wiki/refugee-distress-zoltan.md`)
