---
id: event-refugee
type: event
event_name: REFUGEE_NO_DISTRESS
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-federation-space]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [trading, ambush-risk, refugee, filler, advanced-edition]
---

# Refugee — `REFUGEE_NO_DISTRESS`

## Summary
The same drifting refugee ship as [[event-refugee-distress]], but found by your sensors
instead of by its beacon — no distress signal, and the ship may be actively avoiding you.
Mechanically it is identical: hailing rolls the shared eight-entry `REFUGEE_HAIL_LIST`,
half trade and half ambush. This is the widest-reaching member of the refugee family; it
sits in the generic filler lists and so can turn up almost anywhere.

## Trigger & Where It Appears
- Beacon: no distress marker — it is a **neutral/filler** event. The XML comment on the
  definition is explicit: *"this is actually a NEUTRAL, I'm just leaving it here cause
  it's linked"* ([[source-newevents]], line 861).
- Event lists it belongs to:
  - `NEUTRAL` and `NEUTRAL_EXIT` in `newEvents.xml`, both marked `<!--DLC - down below-->`
    ([[source-newevents]]) — these are the lists the game falls back on when a sector runs
    out of allocated events.
  - `OVERRIDE_NEUTRAL` and `OVERRIDE_NEUTRAL_EXIT`, the Advanced Edition replacements
    ([[source-dlceventsoverwrite]]).
  - `NEUTRAL_ENGI`, marked `<!--DLC - newEvents-->` ([[source-events-engi]]) — this is what
    puts it in [[sector-engi-controlled-sector]] and [[sector-engi-homeworlds]].
- Because `NEUTRAL` / `NEUTRAL_EXIT` are the universal filler pools, its true reach is
  wider than any single sector list; Fandom's location box (below) is the practical
  answer.
- Not `unique` — it can recur.

## Text
> Your sensors have picked up a refugee ship drifting through the system, no doubt one of
> many fleeing the Rebel advance. It doesn't appear to have detected you... or else it is
> trying to avoid notice.

(`event_REFUGEE_NO_DISTRESS_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Hail them. | — | Loads `REFUGEE_HAIL_LIST` — see the pool below. | — |
| 2 | Ignore the refugees. | — | `<event/>` — nothing happens. | 100% |

### `REFUGEE_HAIL_LIST` — the hail pool
This is the **same list** [[event-refugee-distress]] uses. Eight entries, four of them the
same event. **Assuming uniform selection across list entries** (no weights are stated in
the files):

| Outcome | Entries | Share |
|---|---|---|
| `REFUGEE_TRADER` — a resource trade (below) | 4 | 4/8 |
| *"…it advances, weapons bristling from its hull! It's a pirate ambush!"* → fight `PIRATE` | 1 | 1/8 |
| *"…a Zoltan ship suddenly jumps into the system…"* → fight `ZOLTAN_REFUGEE` | 1 | 1/8 |
| *"…a pirate ship jumps into the system… it was using the refugee ship as bait!"* → fight `PIRATE_REFUGEE` | 1 | 1/8 |
| *"…a Slug ship jumps into the system… it was hunting the refugee ship for sport…"* → fight `SLUG_REFUGEE` | 1 | 1/8 |

([[source-newevents]], [[source-text-events-xml]]) Derived from list contents, not a
stated percentage.

### `REFUGEE_TRADER` — the trade sub-event
*"The vessel is relieved to hear from you! They are running low on supplies. They suggest
a trade."* → **Trade with them** loads `TRADER_LIST` (four equally weighted barters, from
`raw/gamedata/events.xml`, [[source-events-xml]]), or **Politely decline** for nothing.

| Trade | You gain | You pay |
|---|---|---|
| 1 | 5–10 fuel | 1–2 drone parts |
| 2 | 4–5 missiles | 1–2 fuel |
| 3 | 2–3 drone parts | 2–3 missiles |
| 4 | 4–10 fuel | 2–4 missiles |

### The ambush ships
`PIRATE` is the standard pirate (50% surrender, 50% escape, default rewards,
[[source-events-ships]]). `ZOLTAN_REFUGEE`, `PIRATE_REFUGEE` and `SLUG_REFUGEE` are
defined in `newEvents.xml` with no surrender and no escape:
`destroyed` → `MED` `standard`, `deadCrew` → `HIGH` `standard`, each followed by a hidden
*"Contact the refugee ship."* choice paying an extra `LOW` `standard`
([[source-newevents]]).

## Blue Options
None.

## Rewards & Risks
- Reward: a barter, or a fight worth `MED`/`HIGH` `standard` plus a `LOW` `standard`
  bonus.
- Risk: a 4/8 chance of an unavoidable fight once you hail. Because this is a filler
  event, it can appear at a beacon you jumped to expecting nothing.

## Strategy Notes
- *(Opinion.)* As filler events go this one is a genuine gamble rather than free scrap.
  If your hull is low, "Ignore the refugees" is a real choice, not a wasted beacon.
- Fandom notes the sector-specific variants "occur independently" — encountering
  [[event-refugee-slug]] does not stop this one appearing later
  ([[source-fandom-refugee]]).

## Related
- [[event-refugee-distress]] — same pool, distress-beacon framing
- [[event-refugee-pirate]], [[event-refugee-slug]], [[event-refugee-zoltan]] —
  sector-specific twins with much smaller pools
- [[event-refugee-comms-down]] — the derelict variant, no trade at all
- [[entity-pirates]], [[entity-zoltan]], [[entity-slugs]]
- [[event-refugee-trader]] — the `REFUGEE_TRADER` trade sub-event, which carries its own page

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] Exact values behind `LOW` / `MED` / `HIGH` `standard`.
- [ ] The Fandom `{{Drifting Refugee Ship}}` template was not captured in the raw dump, so
      no independent outcome list exists to cross-check against.

## Sources
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-events-engi]] (per `raw/gamedata/events_engi.xml`)
- [[source-dlceventsoverwrite]] (per `raw/gamedata/dlcEventsOverwrite.xml`)
- [[source-fandom-refugee]] (per `raw/wiki/refugee.md`)
