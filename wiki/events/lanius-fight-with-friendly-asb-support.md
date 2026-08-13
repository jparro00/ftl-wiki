---
id: event-lanius-fight-with-friendly-asb-support
type: event
event_name: LANIUS_NOBOARDERS_PDS
sectors: [[[sector-abandoned-sector]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [lanius, combat, no-choice, asb, hazard, hull-repair, unique, advanced-edition]
---

# Lanius fight with friendly ASB support — `LANIUS_NOBOARDERS_PDS`

## Summary
The one encounter where the planetary Anti-Ship Battery is shooting at **your enemy**
instead of at you: `<environment type="PDS" target="enemy"/>`. A planet is defending
itself against a Lanius swarm and one Lanius ship mistakes you for an ally of the
defenders. No choices — but the ASB does much of your work, and the aftermath can hand you
8 hull repairs.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] only.
- List: `HOSTILE_ENVIRONMENT_LANIUS`, allocated `min=1 max=2` per sector
  ([[source-sector-data-xml]]); three members → **1/3** *assuming uniform selection across
  list entries* ([[source-dlcevents-anaerobic]]).
- `unique="true"`; the text tag carries `planet="PLANET_POPULATED"`, so the beacon renders
  with an inhabited world.
- Long-range scanners show a ship **and** a PDS
  ([[source-fandom-lanius-fight-with-friendly-asb-support]]).

> **AE-only.** ASB/PDS hazards are themselves an Advanced Edition addition, as are the
> file and the sector.
>
> **Dev residue:** the event body contains a commented-out
> `<!--<boarders min="2" max="2" class="anaerobic"/>-->`, which is what the `NOBOARDERS`
> in the event id refers to — an earlier version beamed two Lanius aboard and that was
> disabled ([[source-dlcevents-anaerobic]]). Fandom does not mention this.

## Text
> Upon arrival you are immediately surrounded by chaos: a planet's Anti-Ship Battery is
> firing on a number of Lanius ships; one of the combat ships mistakenly believes your
> ship has arrived to assist the planetary defenses. Combat positions!

(`event_LANIUS_NOBOARDERS_PDS_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none)_ | — | Combat with `LANIUS_BOARDERS_PDS` while the ASB fires on the **enemy**. Destroyed → `MED standard`; dead crew → `HIGH standard`; either then runs the aftermath list below. | 100% |

### After the fight (`LANIUS_BOARDERS_PDS_LIST`)
Two members, **1/2** each *assuming uniform selection across list entries*
([[source-dlcevents-anaerobic]]):

| Result | Payload |
|---|---|
| The planetary defence team patches you up | `<damage amount="-8"/>` → **8 hull repaired** |
| The fight rages on; best to leave | nothing |

## Blue Options
None.

## Rewards & Risks
- The enemy `LANIUS_BOARDERS_PDS` (`auto_blueprint="SHIPS_LANIUS"`) has **no surrender and
  no escape** — it fights to the end, but with the ASB shooting it the whole time.
- Dead-crew wins pay `HIGH` where hull kills pay `MED`.
- **8 hull is a large repair** — comparable to a repair station — on a 1/2 roll.
- Risk: the ASB targets the enemy only (`target="enemy"`), so the hazard is pure upside
  here. Despite its id, the event beams no boarders onto your ship.

## Strategy Notes
- Among the best hostile beacons in the game to land on: a free ally cannon, a `MED`/`HIGH`
  payout, and a coin-flip at 8 hull. If you are choosing between hazard beacons in this
  sector on the map, this is the one you want — though you cannot tell which of the three
  `HOSTILE_ENVIRONMENT_LANIUS` events a given beacon will be before jumping.
- *Opinion:* boarding for the dead-crew result is worth it here, since the ASB is
  suppressing the enemy anyway.

## Related
- [[event-lanius-fight-in-asteroid-field]], [[event-lanius-fight-near-pulsar]] — the other
  two hazard-list members, both pure downside by comparison
- [[event-lanius-fight]] — the `LANIUS_SHIP` reward tables
- [[entity-lanius]], [[sector-abandoned-sector]]

## Open Questions
- [ ] Numeric values behind `MED` / `HIGH`.
- [ ] Whether the disabled Lanius boarders were cut for balance or for the crash-related
      reasons noted elsewhere in the same file (see
      [[event-boarders-humans-abandoned]]).

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-lanius-fight-with-friendly-asb-support]] (per raw/wiki/lanius-fight-with-friendly-asb-support.md)
