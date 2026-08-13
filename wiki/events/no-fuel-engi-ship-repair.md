---
id: event-no-fuel-engi-ship-repair
type: event
event_name: FUEL_OFF_ENGI_DUBIOUS
sectors: []
beacon_type: any
hostile: unknown
blue_options: [[[item-hull-repair-drone]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [out-of-fuel, engi, trading, blue-option, drone-parts, derived-odds]
---

# No fuel: Engi ship repair — `FUEL_OFF_ENGI_DUBIOUS`

## Summary
An Engi ship drifts past while you are stranded, discussing repairs. Hailing them is a
four-way coin flip that includes free fuel, a paid trade, silence, and a reprogrammed Engi
warship. If you are carrying a **Hull Repair Drone**, the blue option converts the whole
gamble into a guaranteed 4–6 fuel for one drone part — one of the cleanest blue-option
trades in the out-of-fuel pool.

## Trigger & Where It Appears
- **Not a sector event.** Member of the `NO_FUEL` list — the distress-beacon-**off**
  out-of-fuel pool ([[source-events-fuel]]). Fandom marks it `outoffuel=distressoff`
  ([[source-fandom-no-fuel-engi-ship-repair]]).
- Despite the "should eventually be tied to the engi sector" developer comment above it in
  the file, it is **not** sector-gated — it fires anywhere you are stranded with the beacon
  off ([[source-events-fuel]]).
- Prerequisites: 0 fuel, distress beacon off, and you choose to wait.

**Derived odds.** 1/11 (~9.1%) per wait in AE; 1/10 (10%) in vanilla (the list loses its
`<!-- DLC -->` refugee entry). *Assumes uniform selection across list entries.*

## Text
> As you drift through space an Engi ship passes through. From listening to their com
> channel it sounds like they're discussing making repairs on their ship.

(`event_FUEL_OFF_ENGI_DUBIOUS_text`, per [[source-text-events-xml]])

A friendly `FUEL_OFF_ENGI_DUBIOUS` ship (auto-blueprint `SHIPS_CIRCLE`) is present from the
start ([[source-events-fuel]], [[source-events-ships]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Hail them. | — | Loads `FUEL_OFF_ENGI_DUBIOUS_LIST` (4 entries) — see below. | — |
| 2 | Ignore them. | — | "They clearly are busy because they don't notice your ship at all." Nothing happens. | 100% |
| 3 | **(Hull Repair Drone)** Offer to help repair their hull. | `req="SHIP_REPAIR"` | **−1 drone part, +4–6 fuel.** Guaranteed. | 100% |

### Choice 1 — `FUEL_OFF_ENGI_DUBIOUS_LIST` (4 entries, 1/4 each)

| Outcome | Result | Odds |
|---|---|---|
| "Upon discovering your need, the Engi gladly offer some of their extra fuel reserves." | **+2–6 fuel**, free. | 1/4 |
| "Your need: fuel. This unit's need: scrap. Exchange beneficial. Exchange permitted?" | *Make the trade* → **−10–20 scrap, +4–6 fuel**. *Decline* → nothing. | 1/4 |
| "Identity: Federation. I/O error: Federation = [void]." | Nothing happens. | 1/4 |
| "…someone has reprogrammed them to fight!" | The friendly ship turns **hostile** (`<ship hostile="true"/>` — the same `FUEL_OFF_ENGI_DUBIOUS` hull). 80s escape timer, **no surrender**. Destroyed → `autoReward level="MED"` fuel; crew killed → `autoReward level="HIGH"` fuel ([[source-events-ships]]). | 1/4 |

The 1/4 figures are derived from the four `<event>` entries in the `<eventList>` and
**assume uniform selection across list entries** ([[source-events-fuel]]).

## Blue Options
- **[[item-hull-repair-drone]]** (`req="SHIP_REPAIR"`) — spends 1 drone part for a
  guaranteed 4–6 fuel with no fight risk. Strictly better than hailing: the hail branch's
  best free outcome is 2–6 fuel at 1/4, and 1/4 of it is a fight.

## Rewards & Risks
- Rewards: 4–6 fuel (blue), 2–6 fuel free (1/4 of hail), 4–6 fuel for 10–20 scrap (1/4), or
  `MED`/`HIGH` fuel from killing the ship.
- Risks: a 1/4 chance the hail starts a fight against an Engi ship that **cannot be made to
  surrender** and will try to escape after 80 seconds — and you have no fuel to disengage.
- The blue option costs a drone part, which is a real cost on drone-dependent builds.

## Strategy Notes
- *Opinion:* take the blue option whenever you have a drone part to spare; a drone part is
  cheap next to being stranded.
- Without it, hailing is still favourable: 2/4 outcomes give fuel, 1/4 is neutral, and the
  1/4 fight itself pays fuel if you win it.
- Ignoring is only correct if you are already badly damaged and cannot survive the 1/4.

## Related
- [[event-no-fuel-drifting-debris]] — the other faction-flavoured distress-off draw
- [[event-no-fuel-friendly-refugee]] — the free-fuel draw from the same list
- [[entity-engi]]
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Exact scrap/fuel values behind `autoReward` `MED` / `HIGH` fuel tiers.
- [ ] Whether the hostile branch keeps the friendly ship's loadout or re-rolls it.

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml — `FUEL_OFF_ENGI_DUBIOUS`)
- [[source-fandom-no-fuel-engi-ship-repair]] (per raw/wiki/no-fuel-engi-ship-repair.md)
