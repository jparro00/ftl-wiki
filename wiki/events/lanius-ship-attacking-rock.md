---
id: event-lanius-ship-attacking-rock
type: event
event_name: LANIUS_ROCK_DISTRESS
sectors: [[[sector-abandoned-sector]]]
beacon_type: distress
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [lanius, rock, distress, combat, unique, advanced-edition]
---

# Lanius ship attacking Rock — `LANIUS_ROCK_DISTRESS`

## Summary
A distress beacon in the [[sector-abandoned-sector]]: Lanius are stripping a Rockman ship
with its crew still aboard. Fight or walk away. The Lanius ship here is a **special
variant** — `LANIUS_ROCK_DISTRESS_SHIP` has no surrender and no escape clause, so once
committed you fight it to destruction or a dead crew. Winning pays `MED standard` plus a
coin-flip on a second `MED standard` from the Rockmen.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] (`LANIUS_SECTOR`) only.
- List: `DISTRESS_BEACON_LANIUS`, allocated `min="1" max="2"` beacons per sector
  ([[source-sector-data-xml]]).
- That list has **12** members — `LANIUS_DISTRESS_FIGHT`, `LANIUS_DISTRESS_EMPTY`,
  `LANIUS_DISTRESS_TOOLATE`, `LANIUS_DISTRESS_TRAP`, `LANIUS_SLUG_DISTRESS`,
  `LANIUS_MANTIS_DISTRESS`, `LANIUS_ROCK_DISTRESS`, `DISTRESS_SATELLITE_DEFENSE`,
  `DISTRESS_STATION_FIRE`, `FRIENDLY_BEACON`, `TRAP_BEACON`, `STRANDED_BEACON` — none
  duplicated, so this is **1/12** of any Lanius distress beacon *assuming uniform selection
  across list entries* ([[source-dlcevents-anaerobic]]).
- `unique="true"` — at most once per run.
- The event body carries `<distressBeacon/>`, so the beacon is flagged as a distress signal
  on the map ([[source-dlcevents-anaerobic]];
  [[source-fandom-lanius-ship-attacking-rock]] renders `distress=true`, `LRSmap=noship`).
- The file comments this event (and its Slug/Mantis siblings) as *"Chris's"* — a dev
  attribution note, not a mechanical marker.

> **AE-only.** AE data file, AE sector, and `dlcEventsOverwrite.xml` defines no
> `OVERRIDE_DISTRESS_BEACON_LANIUS` ([[source-dlceventsoverwrite]]).

## Text
> A distress beacon pulses weakly from a Rockman ship in this system... their hull (and
> their crew) are being mined by the Lanius, lasers and weapons tearing through the ship!

(`event_LANIUS_ROCK_DISTRESS_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack the Lanius ship. | — | "The Rockmen need your help - you target the Lanius ship and grimly prepare for battle." → fight `LANIUS_ROCK_DISTRESS_SHIP`. | 100% |
| 2 | Leave the Rockmen to their fate. | — | "As you make your escape, the Rockman's ship's engines explode, and you watch the Lanius ship slowly feed on the remains - and the crew." Nothing happens. | 100% |

### The `LANIUS_ROCK_DISTRESS_SHIP` enemy
`auto_blueprint="SHIPS_LANIUS"` — the same hull pool as the ordinary
[[event-lanius-fight]] enemy, but a **different ship block**: it declares only `destroyed`
and `deadCrew`. There is **no `<surrender>` and no `<escape>`**
([[source-dlcevents-anaerobic]]), which
[[source-fandom-lanius-ship-attacking-rock]] confirms with `SurrenderEscape(alt)|no`.

| Outcome | Text | Payout |
|---|---|---|
| Destroyed | "The ship explodes, leaving behind a collection of useful scrap material." | `autoReward level="MED">standard`, then a hidden *"Contact the Rockmen."* choice → `LANIUS_ROCK_DISTRESS_END` |
| Dead crew | "There are no more life-signs remaining on the ship. You strip it of useful materials." | identical: `MED standard`, same follow-up choice |

### `LANIUS_ROCK_DISTRESS_END`
Two entries, neither duplicated → **1/2 each** *assuming uniform selection across list
entries* ([[source-dlcevents-anaerobic]]):

| Outcome | Payload |
|---|---|
| "The Rockmen give an awkwardly-translated message that seems to indicate something about gratitude. They then jump away without another word." | nothing |
| "The Rockman ship jumped away during the battle, but it left much of its hull and spare parts floating behind - you salvage what you can, and prepare to jump." | `autoReward level="MED">standard` |

## Blue Options
None. There is no Rock-crew, Lanius-crew or system-gated choice anywhere in this event
([[source-dlcevents-anaerobic]]).

## Rewards & Risks
- Winning: `MED standard` guaranteed, plus a 1/2 chance of a second `MED standard` — the
  best-paying outcome among the Lanius distress fights, matched only by
  [[event-lanius-ship-attacking-slug]].
- Risk: a full Lanius warship fight **with no surrender and no escape roll**. The enemy
  cannot run and cannot be talked down; neither can you count on it fleeing when damaged.
- Walking away costs nothing mechanically — the Rockmen are not a faction you can offend
  in the files.
- `MED` is the game's own `autoReward` level; no source read here converts it to a number.

## Strategy Notes
- *Opinion, derived from the tables:* this is the distress beacon to take if your ship is
  healthy. Two `MED standard` rolls at 50% is a strong payout for one fight, and the
  Lanius hull pool is not unusually dangerous.
- The absence of a surrender clause cuts both ways: no free `stuff` from a surrender, but
  also no chance the ship escapes with your scrap.
- Boarding is worth no more than shooting here — `destroyed` and `deadCrew` pay identically,
  unlike [[event-lanius-fight]]'s `LANIUS_SHIP`, whose dead-crew table is richer.

## Related
- [[event-lanius-ship-attacking-slug]] — the same event with Slugs; identical structure
- [[event-lanius-ship-attacking-mantis]] — the Mantis sibling, whose reward table differs
- [[event-lanius-fight]] — documents the ordinary `LANIUS_SHIP` block this one deliberately
  departs from
- [[sector-abandoned-sector]], [[entity-lanius]], [[entity-rock-men]]

## Open Questions
- [ ] Numeric scrap values behind `MED standard`.
- [ ] Whether the `LANIUS_ROCK_DISTRESS_SHIP` hull roll differs from `LANIUS_SHIP`'s — both
      use `auto_blueprint="SHIPS_LANIUS"`, so presumably not.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-lanius-ship-attacking-rock]] (per raw/wiki/lanius-ship-attacking-rock.md)
