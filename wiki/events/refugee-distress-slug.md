---
id: event-refugee-distress-slug
type: event
event_name: REFUGEE_DISTRESS_SLUG
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: distress
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [distress, trading, ambush-risk, refugee, slug, advanced-edition]
---

# Refugee distress (Slug) — `REFUGEE_DISTRESS_SLUG`

## Summary
The Slug-sector cut of [[event-refugee-distress]]. Same prose, same two choices, but the
hail pool is two entries instead of eight: a trade, or a pirate ambush. Note the ambusher
is a **pirate**, not a Slug ship — the "_SLUG" in the id refers to the sector, not the
attacker.

## Trigger & Where It Appears
- Beacon: **distress signal** (`<distressBeacon/>`, [[source-newevents]]).
- Sole list membership: `DISTRESS_BEACON_SLUG`, marked `<!--DLC - In newEvents-->`
  ([[source-events-slug]], line 118).
- `DISTRESS_BEACON_SLUG` is allocated `min=3 max=4` in both `SLUG_HOME` and `SLUG_SECTOR`
  ([[source-sector-data-xml]]) → [[sector-slug-home-nebula]] and
  [[sector-slug-controlled-nebula]]. Three to four distress beacons per sector makes this
  one of the more frequently drawn pools in the game.
- Unlike its non-distress twin [[event-refugee-slug]], this event carries **no**
  `<environment type="nebula"/>` tag ([[source-newevents]]).
- Not `unique`.

## Text
> You have encountered a refugee ship drifting in space. It looks as if it was fleeing the
> Rebel advance and ran out of fuel. Its distress beacon is active, but you're not sure
> anyone is on board.

(`event_REFUGEE_DISTRESS_SLUG_text`, identical to the generic string, per
[[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Hail them. | — | Loads `REFUGEE_HAIL_LIST_SLUG` — two entries, below. | — |
| 2 | Ignore the refugees. | — | `<event/>` — nothing happens. | 100% |

### `REFUGEE_HAIL_LIST_SLUG`
Two members. **Assuming uniform selection across list entries**:

| Outcome | Entries | Share |
|---|---|---|
| `REFUGEE_TRADER` — a resource trade (below) | 1 | 1/2 |
| *"As you hail the refugee ship, a pirate ship jumps into the system... it was using the refugee ship as bait!"* → fight `PIRATE_REFUGEE` | 1 | 1/2 |

([[source-newevents]], [[source-text-events-xml]]) Derived from list contents, not a
stated percentage. The Slug list uses the same ambush text and the same ship as the
Pirate list — `event_REFUGEE_HAIL_LIST_SLUG_1_text` and
`event_REFUGEE_HAIL_LIST_PIRATE_1_text` are the same sentence.

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
`destroyed` → `MED` `standard`; `deadCrew` → `HIGH` `standard`; both followed by a hidden
*"Contact the refugee ship."* choice paying a further `LOW` `standard`.

## Blue Options
None — notably, there is no Slug-crew blue option despite the sector.

## Rewards & Risks
- 1/2 barter, 1/2 committed pirate fight.
- With three to four `DISTRESS_BEACON_SLUG` allocations per Slug sector, you can meet this
  event more than once in a single sector.

## Strategy Notes
- *(Opinion.)* In Slug space you are usually already fighting sensor blackout from the
  nebula; taking an even-money fight on top of that is worse than it looks. The barter
  side is also weak if you are short on missiles, which Slug sectors tend to make you.

## Related
- [[event-refugee-distress]] — generic version, 4/8 trade share
- [[event-refugee-slug]] — the non-distress twin, which *does* carry a nebula environment
- [[event-refugee-distress-pirate]] — identical pool and ship
- [[entity-pirates]], [[entity-slugs]]
- [[event-refugee-trader]] — the `REFUGEE_TRADER` trade sub-event, which carries its own page

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] Why the Slug variant's ambush is a pirate rather than a Slug ship — no dev note
      explains it.
- [ ] Fandom's `{{Drifting Refugee Ship}}` template was not captured in the raw dump.

## Sources
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-events-slug]] (per `raw/gamedata/events_slug.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-refugee-distress-slug]] (per `raw/wiki/refugee-distress-slug.md`)
