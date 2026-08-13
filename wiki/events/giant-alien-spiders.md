---
id: event-giant-alien-spiders
type: event
event_name: DISTRESS_INFESTATION
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-uncharted-nebula]]]
beacon_type: distress
hostile: false
blue_options: [[[item-anti-personnel-drone]], [[item-boarding-drone]], [[item-anti-bio-beam]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 9
tags: [distress, unique, blue-option, crew-loss-risk, clone-bay-revival, drone-parts-cost, famous, meme]
---

# Giant alien spiders — `DISTRESS_INFESTATION`

## Summary
The most notorious event in FTL. Sending your crew to fight the spiders is a **coin flip
between losing a crewmember and a `HIGH` payout** — and before the Advanced Edition's Clone
Bay, that loss was permanent. Three blue options remove the gamble entirely, two of them at
the cost of a drone part. *"Giant alien spiders are no joke"* became a community meme
([[source-fandom-giant-alien-spiders]]). `unique="true"`.

## Trigger & Where It Appears
- Sectors: [[sector-federation-space]], [[sector-civilian-sector]],
  [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]],
  [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]],
  [[sector-rock-homeworlds]], [[sector-uncharted-nebula]]
- Event lists: `DISTRESS_BEACON` ([[source-newevents]]), `DISTRESS_BEACON_ENGI`
  ([[source-events-engi]]), `DISTRESS_BEACON_MANTIS` ([[source-events-mantis]]),
  `DISTRESS_BEACON_ROCK` ([[source-events-rock]])
- Allocation: 1–2 in `STANDARD_SPACE` / `CIVILIAN_SECTOR`, 1–3 in `NEBULA_SECTOR`, 1–3 in
  both Engi sectors, 1–3 in both Mantis sectors, 1–2 in both Rock sectors
  ([[source-sector-data-xml]])
- Beacon: `<distressBeacon/>`
- Long-range scanners show **no ship** ([[source-fandom-giant-alien-spiders]])
- `unique="true"` — once per run

## Text
> You find a number of ships fleeing from a small space station. You hail them, asking what's
> wrong: "Help! We're being overrun by some sort of giant alien spiders!"

(`event_DISTRESS_INFESTATION_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Send the crew to help! Giant alien spiders are no joke. | — | Rolls `DISTRESS_INFESTATION_LIST` (2 entries) — see below | 1/2 each |
| 2 | Leave them alone. | — | *"You can't risk fighting some unknown alien on every backwater station you come across."* → nothing | 100% |
| 3 | **(Anti-Personnel Drone)** Send your battle drone in to help. | `req="BATTLE"` | *"…the majority of the creatures are dead, with only a little collateral damage."* → `autoReward level="MED"` **`stuff`** − 1 drone part | 100% |
| 4 | **(Boarding Drone)** Launch a Boarding drone into the station. | `req="BOARDER"` | *"…debris and dead bodies fly out of the breach…they offer only a meager payment."* → `autoReward level="LOW"` `standard` − 1 drone part | 100% |
| 5 | **(Bio Beam)** Use the beam to pick off the spiders. | `req="BEAM_BIO"` | *"The monsters just started bursting into flame as we watched…"* → `autoReward level="HIGH"` **`stuff`**, **no cost** | 100% |

### Choice 1 → `DISTRESS_INFESTATION_LIST`

| Entry | Outcome | Share |
|---|---|---|
| 1 | *"…You fight your way back to the airlock and are forced to leave before accounting for all crewmembers. Not everybody made it back."* → `<removeCrew><clone>true</clone>…` — **lose a crewmember**, revivable by Clone Bay | 1/2 |
| 2 | *"…your team stays in control and before long you've beaten them back."* → *Contact the station owners* → *"They are thrilled with your success and offer you a reward."* → `autoReward level="HIGH"` `stuff` | 1/2 |

Two entries, no duplicates → **1/2 each** under uniform selection across list entries
([[source-events-xml]]). Fandom describes this as a *"low success rate"*; the files support
50%, not lower ([[source-fandom-giant-alien-spiders]]).

The Clone Bay line is spelled out: *"You take a hopeful trip to the Clone Bay, and to your
relief a clone is already prepared for the lost crewmember."*
(`event_DISTRESS_INFESTATION_LIST_1_c0_clone`, [[source-text-events-xml]])

## Blue Options
- **[[item-anti-personnel-drone]]** (`req="BATTLE"`, drone blueprint —
  [[source-blueprints]]) — `MED` `stuff`, costs 1 drone part.
- **[[item-boarding-drone]]** (`req="BOARDER"`) — the **worst** option: `LOW` `standard`
  *and* a drone part. Strictly dominated by the Anti-Personnel Drone if you have both.
- **[[item-anti-bio-beam]]** (`req="BEAM_BIO"`, weapon blueprint) — `HIGH` `stuff` and
  costs nothing at all. The best outcome in the event, guaranteed. This is one of the very
  few places the Anti-Bio Beam is genuinely useful.

Fandom flags a bug on the two drone options: *no drone part is actually lost if the reward
includes drone parts, though you still need at least 1 to select the option*
([[source-fandom-giant-alien-spiders]]). The game files show an unconditional
`item_modify` of −1, so this is a runtime behaviour Fandom observed rather than something
the data states.

## Rewards & Risks
- **Best outcome:** `HIGH` `stuff` — Fandom reads that as fuel 3–6, missiles 4–8, drone
  parts 1–2, with some scrap. Reachable free via the Anti-Bio Beam, or on a coin flip via
  choice 1.
- **Worst outcome:** a dead crewmember and nothing to show for it. In vanilla that is
  permanent.
- Choice 2 is a genuine no-cost skip — no fleet advance, no damage.

## Version Differences
Base-`events.xml` event with **no DLC-marked tags** — the outcomes are identical in both
editions ([[source-events-xml]]). The difference is external: the `<clone>true</clone>`
branch only does anything if you own a **Clone Bay**, an Advanced Edition system. So the
same 1/2 crew-loss roll is permanent in vanilla and often recoverable in AE — which is
exactly why the event's reputation was formed pre-AE
([[source-fandom-giant-alien-spiders]]).

## Strategy Notes
- *(Opinion.)* With the Anti-Bio Beam, always take choice 5 — free `HIGH` `stuff`.
- With an Anti-Personnel Drone, choice 3 is a clean trade of one drone part for `MED`
  `stuff`.
- Never take choice 4 if choice 3 is available; `LOW standard` for the same drone part is
  strictly worse.
- Without any blue option, choice 1 is a 50/50 for `HIGH stuff` against a crewmember. With a
  Clone Bay the gamble is reasonable; without one, on a small crew, it is not.

## Related
- [[event-unknown-disease-on-mining-colony]] — the other "send your crew into a station"
  distress event with a 1/2 crew-loss roll, and the one where the Clone Bay explicitly
  **fails**
- [[event-fire-on-research-station]] — same shape, fire instead of spiders
- [[event-malfunctioning-defense-system]], [[event-crushed-pirate]],
  [[event-asteroid-belt-distress]] — the rest of the shared `DISTRESS_BEACON` pool
- [[item-anti-bio-beam]], [[item-anti-personnel-drone]], [[item-boarding-drone]]

## Open Questions
- [ ] Are `<eventList>` entries selected uniformly? The 1/2 assumes it.
- [ ] Numeric values behind `HIGH`/`MED` `stuff` and `LOW` `standard`; the levels are the
      game's own words and Fandom's ranges are its own reading.
- [ ] Which crewmember `removeCrew` selects — the files give no selection rule.
- [ ] Is the drone-part bug Fandom reports still present in 1.6.x?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml` — `DISTRESS_BEACON`)
- [[source-events-engi]] (per `raw/gamedata/events_engi.xml`)
- [[source-events-mantis]] (per `raw/gamedata/events_mantis.xml`)
- [[source-events-rock]] (per `raw/gamedata/events_rock.xml`)
- [[source-blueprints]] (per `raw/gamedata/blueprints.xml` — `BATTLE`, `BOARDER`, `BEAM_BIO`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-giant-alien-spiders]] (per `raw/wiki/giant-alien-spiders.md`)
