---
id: event-lanius-fight
type: event
event_name: LANIUS_FIGHT
sectors: [[[sector-abandoned-sector]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [lanius, combat, no-choice, default-rewards, advanced-edition]
---

# Lanius fight — `LANIUS_FIGHT`

## Summary
The baseline hostile encounter of the [[sector-abandoned-sector]]: you arrive, a Lanius
warship is already coming for your hull, and there are no choices. Three lines of XML — a
text list and `<ship load="LANIUS_SHIP" hostile="true"/>` — behind eleven flavour texts.
This page also documents the **`LANIUS_SHIP` ship definition itself**, which a dozen other
Lanius events reuse as their enemy, so its surrender / escape / destroyed / dead-crew
tables are recorded here once and cross-linked from the rest.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] (`LANIUS_SECTOR`) only.
- List: `HOSTILE_LANIUS`, which the sector allocates at `min=5 max=6` beacons
  ([[source-sector-data-xml]]).
- `HOSTILE_LANIUS` has six members — `LANIUS_FIGHT`, `LANIUS_REBEL_FIGHT`,
  `LANIUS_PIRATE_FIGHT`, `LANIUS_HARVESTER`, `REBEL`, `REBEL_AUTO` — none duplicated, so
  each is **1/6** of any hostile beacon *assuming uniform selection across list entries*
  ([[source-dlcevents-anaerobic]]).
- No `unique` attribute → it repeats freely ([[source-fandom-lanius-fight]] renders this
  as `unique=false`).
- Long-range scanners show a ship ([[source-fandom-lanius-fight]]).

> **AE-only.** `dlcEvents_anaerobic.xml` is an Advanced Edition data file and
> `LANIUS_SECTOR` is an AE sector; there is no vanilla form of this event.
> `dlcEventsOverwrite.xml` defines no `OVERRIDE_` replacement for any `*_LANIUS` list, so
> the AE/vanilla pool-swap question does not arise here.

## Text
`[varies: textList LANIUS_FIGHT_TEXT]` — eleven `<text>` entries drawing on ten distinct
strings; `text_LANIUS_FIGHT_TEXT_8` is listed **twice**, so it is **2/11** of arrivals and
every other string is 1/11 *assuming uniform selection across list entries*
([[source-dlcevents-anaerobic]], [[source-text-events-xml]]). The file splits them into
the original six and a later block commented "CHRIS ADDITIONS".

Representative examples:

> You receive a message on a wide band frequency, originating from an approaching Lanius
> ship. It appears not to be directed at you, but your translator does its best all the
> same: "... metallic opportunity... acquisition... by force..." Looks like you're in for
> a fight.

> The beacon is surrounded by many tiny Lanius craft, surely only capable of holding one
> occupant. Perhaps they are some kind of forward scout searching for 'metallic
> opportunities'? As you consider this, a much larger Lanius vessel moves in to engage
> you, and the scout ships scatter in all directions.

> As you are getting your bearings, another ship suddenly arrives at the beacon - it's the
> Lanius, and they've marked your ship for salvage! *(the doubled entry)*

All eleven are transcribed on [[source-fandom-lanius-fight]] and live at
`text_LANIUS_FIGHT_TEXT_1` … `_10` in `raw/gamedata/text_events.xml`.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event has no `<choice>` elements)_ | — | Immediate combat with `LANIUS_SHIP`, **default Lanius rewards** (see below). | 100% |

## The `LANIUS_SHIP` enemy
`auto_blueprint="SHIPS_LANIUS"` → the `ANAEROBIC_SCOUT` / `ANAEROBIC_BOMBER` hull pool
(per `raw/gamedata/dlcBlueprints.xml`; that file has no source page yet). Its outcome
tables ([[source-dlcevents-anaerobic]]):

| Outcome | Definition | Payout |
|---|---|---|
| Surrender | `chance="0.2" min="3" max="4"` → `LANIUS_SURRENDER` | Accept → ship turns non-hostile, `autoReward level="RANDOM">stuff`. Refuse → the fight continues. |
| Escape | `chance="0.2" min="2" max="4"` → `LANIUS_ESCAPE` | Flavour only; if they get away you receive nothing. |
| Destroyed | `LANIUS_DESTROYED` (4 entries) | **3/4** `MED standard`; **1/4** `HIGH standard` ("revealing their cargo of unprocessed metal"). |
| Dead crew | `LANIUS_DEAD_CREW` (8 entries) | **3/8** `MED standard`; **2/8** `HIGH standard`; **1/8** `HIGH fuel`; **1/8** a **free crew member** + `LOW scrap_only`; **1/8** `LOW drone`. |

Both fraction columns assume uniform selection across list entries — the lists state no
weights, only repeated members. `HIGH`/`MED`/`LOW` are the game's own `autoReward` levels;
no source read here converts them to numbers. Fandom calls this whole table
"default Lanius rewards" ([[source-fandom-lanius-fight]]).

> Note on the Fandom surrender/escape annotation: its `SurrenderEscape` template renders
> `80 | 20-40 | 2-4` for both, which does not obviously map onto the XML's
> `chance="0.2"` and crew `min`/`max`. The game files are the authority for the raw
> attribute values; how the engine converts `chance` into a per-turn probability is not
> stated in any source read here.

## Blue Options
None.

## Rewards & Risks
- Reward: default Lanius rewards only — but note the dead-crew table is unusually rich
  (a 1/8 shot at a free crew member, another 1/8 at a drone), which rewards boarding or
  venting the Lanius rather than blowing them up.
- Risk: an ordinary Lanius warship. There is no avoid option and no bribe.

## Strategy Notes
- Nothing to decide here; the lever is whether you route into the Abandoned Sector at all,
  which allocates 5–6 hostile beacons plus 1–2 hazard-hostile ones
  ([[source-sector-data-xml]]).
- *Opinion, derived not sourced:* killing the crew rather than the hull is worth more here
  than in most fights — 3/8 of the dead-crew table beats the median destroyed result, and
  it is the only route to the free crew member.

## Related
- [[event-lanius-fight-in-asteroid-field]], [[event-lanius-fight-near-pulsar]] — same
  ship, hazard added
- [[event-lanius-fight-distress]] — same ship, distress-beacon framing
- [[event-lanius-powered-down-ship]], [[event-lanius-ship-absorbing-jump-beacon]],
  [[event-lanius-ship-absorbing-rebel-base]] — optional fights against the same `LANIUS_SHIP`
- [[event-pirate-fight-lanius]], [[event-rebel-fight-lanius]] — the other two flavoured
  fights in the same list
- [[entity-lanius]], [[sector-abandoned-sector]]
- [[event-lanius-surrender]] — the `LANIUS_SURRENDER` aftermath this hull loads

## Open Questions
- [ ] Numeric scrap values behind `LOW` / `MED` / `HIGH`.
- [ ] How `chance="0.2"` maps to an in-game surrender/escape probability, and what
      Fandom's `80` refers to.
- [ ] Whether the eleven text entries are genuinely equally weighted.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-lanius-fight]] (per raw/wiki/lanius-fight.md)
