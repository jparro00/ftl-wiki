---
id: event-lanius-ship-absorbing-jump-beacon
type: event
event_name: LANIUS_BEACON_EATER
sectors: [[[sector-abandoned-sector]]]
beacon_type: any
hostile: false
blue_options: [lanius crew, hull repair drone]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [lanius, trading, blue-option, augment, crew-reward, scrap-loss-risk, unique, advanced-edition]
---

# Lanius ship absorbing jump beacon — `LANIUS_BEACON_EATER`

## Summary
A damaged Lanius ship is eating the jump beacon it is docked to. Every route through this
event is a negotiation over metal: pay 30 scrap and *probably* get a random augment, ask
first and take a coin-flip on being attacked, or leave and *probably* get away clean. Two
blue options change the shape entirely — a Lanius crew member makes the trade safe and
lets you pay in missiles or drone parts instead, and a **Hull Repair drone** buys you a
free Lanius crew member outright.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] only.
- List: `NEUTRAL_LANIUS`, allocated `min=5 max=6` beacons per sector
  ([[source-sector-data-xml]]); thirteen members → **1/13** *assuming uniform selection
  across list entries* ([[source-dlcevents-anaerobic]]).
- `unique="true"` — at most once per sector.
- Spawns `<ship load="LANIUS_SHIP" hostile="false"/>`; long-range scanners show a ship
  ([[source-fandom-lanius-ship-absorbing-jump-beacon]]).

> **AE-only** — Advanced Edition file, sector, species and drone gate.

## Text
> You detect a damaged vessel docked with the jump beacon. It appears the Lanius are
> absorbing metal from the beacon, risking destroying it and becoming stranded.

(`event_LANIUS_BEACON_EATER_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Ask if they require assistance. | — | Loads `LANIUS_BEACON_EATER_ASK` (2 members): (a) *"critical... must... metal..."* → a second menu — **Give them 30 scrap** (−30 scrap, **random augment**) or **Leave** (→ the `LEAVE` list below); (b) *"…it quickly powers on its weapons defensively"* → combat with `LANIUS_SHIP`. | **1/2** each *(assuming uniform selection across list entries)* |
| 2 | Send them 30 scrap. | — | Loads `LANIUS_BEACON_EATER_SCRAP` (2 members): (a) −30 scrap, **random augment**; (b) −30 scrap **and** combat with `LANIUS_SHIP` — the scrap is spent either way. | **1/2** each *(same assumption)* |
| 3 | Leave. | — | Loads `LANIUS_BEACON_EATER_LEAVE` (4 members, one text repeated three times): **3/4** nothing happens; **1/4** the Lanius pulls off the beacon and attacks → combat with `LANIUS_SHIP`. | **3/4** / **1/4** *(same assumption)* |
| 4 | **(Lanius Crew)** Ask if they require assistance. | `req="anaerobic"` | *"They offer to exchange a piece of their ship's equipment for some scrap or other useful materials."* → a menu with no fight branch at all: **30 scrap**, **6 missiles**, or **6 drone parts** → **random augment**; or **Decline** → nothing. | 100% |
| 5 | **(Hull Repair Drone)** Send a drone to help. | `req="SHIP_REPAIR"` | The Lanius eat the drone, repair their ship, and one of their crew asks to join → `<crewMember amount="1" class="anaerobic"/>` — **a free Lanius crew member**. | 100% |

Fandom independently marks the triple-repeated `LEAVE` entry with its own
`{{DuplicateEvent|3}}` notation, which agrees with the 3/4 reading above
([[source-fandom-lanius-ship-absorbing-jump-beacon]]).

## Blue Options
- **Lanius crew member** (`req="anaerobic"`) — removes the fight risk from the trade and
  adds two alternative currencies. The scrap price is the same 30 as the unskilled route;
  what you buy is certainty plus the option to pay in missiles or drone parts
  ([[source-dlcevents-anaerobic]]).
- **Hull Repair drone** (`req="SHIP_REPAIR"` — the `SHIP_REPAIR` drone blueprint, titled
  "Hull Repair" in `text_blueprints.xml`) — spend nothing that is not already sitting in
  your drone bay and get **a Lanius crew member**. Note the XML does not remove the drone
  from your inventory; only the fiction says it is consumed
  ([[source-dlcevents-anaerobic]]).

## Rewards & Risks
- Best outcomes: a free Lanius crew member (choice 5), or a random augment for 30 scrap /
  6 missiles / 6 drone parts (choice 4).
- Worst outcome: choice 2's bad branch — **30 scrap gone and a fight anyway**, with no
  refund ([[source-fandom-lanius-ship-absorbing-jump-beacon]] flags this explicitly).
- All fights are against `LANIUS_SHIP`; tables on [[event-lanius-fight]].
- Even walking away carries a 1/4 chance of being attacked.

## Strategy Notes
- With a Hull Repair drone aboard, choice 5 is one of the best returns in the sector: a
  crew member costs nothing you weren't already carrying.
- With a Lanius aboard, choice 4 is a safe augment at a price you choose.
- With neither, choice 1 is better than choice 2 — it gives you the same 30-scrap trade at
  the same price but lets you back out after seeing the response, whereas choice 2 spends
  the scrap before the coin is flipped.
- There is no fully safe exit: choice 3 still fights you a quarter of the time.

## Related
- [[event-lanius-powered-down-ship]] — the other Lanius-crew salvage opportunity here
- [[event-lanius-fight]] — the enemy definition behind every fight branch
- [[item-hull-repair-drone]] — the drone that unlocks choice 5
- [[entity-lanius]], [[sector-abandoned-sector]]

## Open Questions
- [ ] Whether the Hull Repair drone is actually consumed (the XML applies no `item_modify`
      or drone removal).
- [ ] Which augment pool `augment name="RANDOM"` draws from.
- [ ] Whether the two-member `ASK` and `SCRAP` lists are genuinely equally weighted.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-lanius-ship-absorbing-jump-beacon]] (per raw/wiki/lanius-ship-absorbing-jump-beacon.md)
