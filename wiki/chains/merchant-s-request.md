---
id: chain-merchant-s-request
type: chain
trigger_event: [[[event-merchant-s-request]]]
steps: [[[event-merchant-s-request]], [[event-merchant-deliver]], [[event-merchant-investigate]], [[event-merchant-investigate-deliver]]]
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]]]
reward: "scrap, a drone reward, possible crew, or a random weapon — depending which of two jobs you draw"
version: ae
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
tags: [quest, branching, two-jobs, courier, blue-option, mind-control]
---

# Merchant's Request

## Summary
One beacon that forks into **two entirely different quests** and never rejoins. A merchant
broadcasting for a mercenary offers you either a **delivery job** (haul 5 drone parts to a
station) or an **investigation job** (find a freighter that went missing in pirate space).
Which one you get is a coin flip made before you choose anything.

The delivery fork is the more interesting of the two, because the "reward" is a haggle: the
station tries to underpay you, and three separate blue options exist to argue them up — the
only place in the game where **Mind Control** is used to negotiate a price.

## How It Starts
- Trigger: [[event-merchant-s-request]] (`MERCHANT_REQUEST`), `unique="true"`
  ([[source-events-xml]]). *"One merchant seems to be mass-broadcasting a request for a
  mercenary ship to aid him. Shall we respond?"*
- Saying **No** ends it immediately, with no cost.
- Saying **Yes** loads `MERCHANT_REQUEST_LIST` — 2 entries, so **50/50** between the two jobs
  per [[concept-event-list-weighting]]. You are told which job it is *before* accepting, and
  can still decline either.

## Steps

### Fork A — the delivery job (50%)

1. **Accept** → you are handed **5 drone parts** (`<item type="drones" min="5" max="5"/>`) and
   `<quest event="MERCHANT_DELIVER"/>`. Note the parts are yours to spend in the meantime;
   nothing stops you using them.
2. **[[event-merchant-deliver]]** — the marked beacon, resolving `MERCHANT_DELIVER_LIST`,
   2 entries at 50% each:
   - **The station is silent and broadcasting a distress signal.** This hands off into
     `STATION_SICK_LIST` — the plague-station tree shared with
     [[event-research-station-with-no-response]]. An **Anti-Personnel Drone**
     (`req="BATTLE"`) opens a safer route via `STATION_SICK_DRONE_LIST`.
   - **The station lowballs you.** *"I refuse to pay full price."* Four ways to respond:

     | Choice | Requirement | Result |
     |---|---|---|
     | Accept the paltry payment | — | **20–30 scrap**, −5 drone parts |
     | Refuse and keep the parts | — | `MERCHANT_DELIVER_BLUFF_LIST` |
     | (Mind Control) *"Convince him that he's being 'unfair'."* | `req="mind"` | **40–55 scrap**, −5 drone parts |
     | (Weapons 6) Remain silent but power up your weapons | `req="weapons" lvl="6"` | **55–70 scrap**, −5 drone parts, **+2–5 fuel** |

### Fork B — the investigation job (50%)

1. **Accept** → `<quest event="MERCHANT_INVESTIGATE"/>`. No down-payment.
2. **[[event-merchant-investigate]]** — resolving `MERCHANT_INVESTIGATE_LIST`, 3 entries at
   33% each:
   - **A wrecked ship, cargo intact** → `autoReward MED standard`, then choose: chase the
     original destination (`<quest event="MERCHANT_INVESTIGATE_DELIVER"/>`) or **take the
     cargo for yourself** (`MERCHANT_INVESTIGATE_CARGO_LIST`).
   - **The crew is alive and freezing.** Promise to finish the delivery and **+1 crew** plus
     the marker; or take the cargo and drop them off; or, with a **Teleporter**
     (`req="teleporter"`), *"beam the cargo aboard and leave them to their fate"*.
   - **A pirate is chasing them** → a forced fight with `JELLY_PIRATE_MERCHANT`.
3. **Keeping the cargo** rolls `MERCHANT_INVESTIGATE_CARGO_LIST`, 3 entries: food and medicine
   (nothing, but you still get the delivery marker), a **random weapon**, or
   `autoReward HIGH standard`.
4. **[[event-merchant-investigate-deliver]]** — the final drop-off: `autoReward MED drone`.

## Requirements
- Nothing to start. The paying gates are **Mind Control** or **Weapons level 6** on fork A,
  and a **Teleporter** or an **Anti-Personnel Drone** for the optional routes.
- Fuel to reach one or two extra beacons.

## Reward
Modest and cash-shaped. Fork A tops out at 55–70 scrap and 2–5 fuel with Weapons 6; fork B can
yield a crew member, a random weapon, or a `HIGH standard` roll, and ends on `MED drone`.
Neither fork awards a ship, augment or unlock.

## Failure Modes
- **The delivery fork can turn into the plague station**, which is a genuine crew-risk event —
  see [[event-research-station-with-no-response]] for what `STATION_SICK_LIST` does.
- Spending the 5 drone parts and then arriving at the station: the payout entries all deduct
  `-5` drone parts, so the outcome with an empty hold is unrecorded here.
- The usual quest-marker losses — see [[concept-quest-beacon-placement]].

## Strategy Notes
- *Opinion:* fork A with Weapons 6 or Mind Control is worth taking; without either, 20–30
  scrap for a two-jump detour and a 50% chance of the plague station is thin.
- Fork B's "take the cargo for yourself" is not a betrayal penalty — one of its three outcomes
  *still* gives you the delivery marker, so you can loot **and** get paid.
- The Teleporter option on fork B is the coldest choice in the chain and pays no more than
  simply dropping the crew off.

## Related
- [[event-research-station-with-no-response]] — shares `STATION_SICK_LIST` and
  `STATION_SICK_DRONE_LIST`
- [[concept-quest-beacon-placement]], [[concept-event-list-weighting]]
- [[item-mind-control]], [[item-teleporter]], [[item-anti-personnel-drone]]
- [[chain-settlement-mercenary-work]] — the other "civilians hire you as a mercenary" quest

## Open Questions
- [ ] `MERCHANT_DELIVER_BLUFF_LIST` — the refuse-and-keep branch is not expanded here.
- [ ] What happens at the drop-off if the 5 drone parts have already been spent.
- [ ] Whether the two forks are equally likely in practice, or whether `MERCHANT_REQUEST_LIST`
      is weighted by some mechanism not visible in the file.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
