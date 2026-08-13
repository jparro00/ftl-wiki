---
id: event-unknown-disease-on-mining-colony
type: event
event_name: DISTRESS_STATION_DISEASE
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-uncharted-nebula]]]
beacon_type: distress
hostile: false
blue_options: [[[item-medbay]], [[item-engi-med-bot-dispersal]], rock crew, engi crew]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 9
tags: [distress, unique, blue-option, crew-loss-risk, clone-bay-failed-revival, weapon-reward, rock-crew, engi-crew]
---

# Unknown disease on mining colony — `DISTRESS_STATION_DISEASE`

## Summary
A quarantine riot on a human mining colony. Sending your own crew is a coin flip: half the
time nothing happens, half the time **you lose a crewmember permanently — the Clone Bay
explicitly refuses to bring them back**, the only event in this batch where that is true.
Four blue options bypass the risk, and stacking an upgraded Medbay with the Engi Med-bot
Dispersal augment upgrades the payout to a `HIGH` weapon. `unique="true"`.

## Trigger & Where It Appears
- Sectors: [[sector-federation-space]], [[sector-civilian-sector]],
  [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]],
  [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]],
  [[sector-rock-homeworlds]], [[sector-uncharted-nebula]]
- Event lists: `DISTRESS_BEACON` ([[source-newevents]]), `DISTRESS_BEACON_MANTIS`
  ([[source-events-mantis]]), `DISTRESS_BEACON_PIRATE` ([[source-events-pirate]]),
  `DISTRESS_BEACON_ROCK` ([[source-events-rock]])
- Allocation: 1–2 in `STANDARD_SPACE` / `CIVILIAN_SECTOR` / Pirate / Rock sectors, 1–3 in
  `NEBULA_SECTOR` and both Mantis sectors ([[source-sector-data-xml]])
- Beacon: `<distressBeacon/>`
- Long-range scanners show **no ship** ([[source-fandom-unknown-disease-on-mining-colony]])
- `unique="true"` — once per run

## Text
> You locate a nearby human mining colony where an unknown disease has spread virulently.
> They are setting up a quarantine to contain it but a riot has broken out.

(`event_DISTRESS_STATION_DISEASE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Send in your crew to help control the crowds. | — | Rolls `DISTRESS_STATION_DISEASE_LIST` (2 entries) — see below | 1/2 each |
| 2 | Ignore their request and move on. | — | *"Unfortunately your mission is too important…"* → nothing | 100% |
| 3 | **(Rock Crew)** Send your Rock crew-member to prevent a riot. | `req="rock"` | *"…the Rock's impressive immune system…It is able to intimidate the workers…"* → `autoReward level="MED"` `stuff` | 100% |
| 4 | **(Engi Crew)** Send your Engi to calm down the infected. | `req="engi"` | *"With no fear of catching the disease…"* → `autoReward level="MED"` `stuff` | 100% |
| 5 | **(Adv. Medbay)** Use your Medbay to help synthesize a cure. | `req="medbay" lvl="2"` | *"Your military-grade medical computers are easily able to isolate the cause…"* → a second screen, see below | 100% |

### Choice 1 → `DISTRESS_STATION_DISEASE_LIST`

| Entry | Outcome | Share |
|---|---|---|
| 1 | *"…the infected grab mining tools and push back at your crew, forcing them to retreat hastily…the same can't be said for the colony's leaders."* → nothing at all | 1/2 |
| 2 | *"…one of your crew presents signs of infection. You have no choice but to leave them on the station…"* → `<removeCrew><clone>false</clone>` — **lose a crewmember, no clone** + `autoReward level="MED"` `stuff` | 1/2 |

Two entries → **1/2 each**, assuming uniform selection across list entries
([[source-events-xml]]).

The `<clone>false</clone>` flag comes with its own in-fiction explanation:

> As your crewman is still alive and working towards a cure, it would be against Federation
> regulation to create a clone to continue with you on your journey.

(`event_DISTRESS_STATION_DISEASE_LIST_2_c0_clone`, [[source-text-events-xml]])

Note the shape of the gamble: the "good" outcome pays **nothing**, and the crew loss is the
only outcome that pays. Choice 1 is a 50% chance to trade a crewmember for `MED` `stuff`.

### Choice 5 → the Medbay branch

| # | Choice | Requirement | Outcome(s) |
|---|--------|-------------|-----------|
| 5a | *(Continue…)* | — | *"Thank you so much! …Here, take this as payment!"* → `autoReward level="MED"` `stuff` |
| 5b | **(Engi Med-bot Dispersal)** Use the Nano med-bots to accelerate the dispersal of the cure. | `req="NANO_MEDBAY"` | *"In a matter of minutes all of the workers are cured…"* → `autoReward level="HIGH"` **`weapon`** |

## Blue Options
- **Rock crew** (`req="rock"`) — `MED` `stuff`, free.
- **Engi crew** (`req="engi"`) — `MED` `stuff`, free.
- **[[item-medbay]] level 2+** (`req="medbay" lvl="2"`) — `MED` `stuff`, free, and it is the
  only gate that opens the augment branch below.
- **[[item-engi-med-bot-dispersal]]** (`req="NANO_MEDBAY"`, an augment —
  [[source-blueprints]]) — **stacked behind the Medbay gate**, not selectable on its own.
  Upgrades the payout to `HIGH` `weapon`, the best outcome in the event.

Four separate gates all lead to at least `MED` `stuff`, which makes the unaided gamble very
rarely necessary.

## Rewards & Risks
- **Best outcome:** `HIGH` `weapon` — Medbay 2 plus the Engi Med-bot Dispersal augment.
- **Common outcome:** `MED` `stuff` — Fandom reads that as fuel 2–4, missiles 2–4, 1 drone
  part, with some scrap.
- **Risk:** choice 1 only — a permanently lost crewmember, half the time. No hull damage
  anywhere in this event, and no fleet advance.

## Version Differences
Base-`events.xml` event with **no DLC-marked tags** — the choices, outcomes and rewards are
identical in both editions ([[source-events-xml]]). The `<clone>false</clone>` flag only
matters if you own a Clone Bay, an AE system; in vanilla the crew loss is unconditionally
permanent, so the flag changes nothing there.

## Strategy Notes
- *(Opinion.)* This is one of the easiest distress beacons to farm — Rock or Engi crew,
  or a Medbay upgraded once, all pay `MED stuff` for free. Most runs will have one of them.
- Choice 1 is a bad bet on its own terms: the winning half pays nothing and the losing half
  costs a crewmember for a `MED` reward. Take choice 2 instead if you have no gate.
- The `HIGH weapon` branch is a real reason to carry the Engi Med-bot Dispersal augment past
  the point it stops healing efficiently.

## Related
- [[event-giant-alien-spiders]] — the same 1/2 crew-loss shape, but the Clone Bay **does**
  work there
- [[event-fire-on-research-station]] — the third "send your crew into a station" distress
  event; Clone Bay also works
- [[event-malfunctioning-defense-system]], [[event-crushed-pirate]],
  [[event-asteroid-belt-distress]] — the rest of the shared `DISTRESS_BEACON` pool
- [[item-medbay]], [[item-engi-med-bot-dispersal]]
- [[entity-rock-men]], [[entity-engi]]

## Open Questions
- [ ] Are `<eventList>` entries selected uniformly? The 1/2 assumes it.
- [ ] Which crewmember `removeCrew` selects.
- [ ] Numeric values behind `MED stuff` and `HIGH weapon`.
- [ ] Does `<clone>false</clone>` merely suppress revival, or does it also consume the Clone
      Bay charge? The files only carry the flag and the text.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml` — `DISTRESS_BEACON`)
- [[source-events-mantis]] (per `raw/gamedata/events_mantis.xml`)
- [[source-events-pirate]] (per `raw/gamedata/events_pirate.xml`)
- [[source-events-rock]] (per `raw/gamedata/events_rock.xml`)
- [[source-blueprints]] (per `raw/gamedata/blueprints.xml` — `NANO_MEDBAY`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-unknown-disease-on-mining-colony]] (per `raw/wiki/unknown-disease-on-mining-colony.md`)
