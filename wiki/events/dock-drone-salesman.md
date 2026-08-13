---
id: event-dock-drone-salesman
type: event
event_name: DOCK_DRONE_SALESMAN
sectors: []
beacon_type: any
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [drones, trading, sub-event, pirate, ambush-risk, system-upgrade, ae]
---

# Pirate drone salesman — `DOCK_DRONE_SALESMAN`

## Summary
The shop you actually get to after boarding the pirate salesman's ship: drone parts, a
random drone schematic, and tiered Drone Control upgrades, all for scrap. Buying nothing
is not a neutral exit — it triggers an ambush that damages three of your rooms and starts
a pirate fight. Since its sibling `DOCK_BOMB_SALESMAN` is commented out of the pool, this
is the **only** shop the pirate salesman chain can reach.

## Trigger & Where It Appears
- Not in any sector event list directly. It is the sole live member of
  `eventList DOCK_PIRATE_SALESMAN`, reached through a two-step chain
  ([[source-newevents]]):
  1. `PIRATE_SALESMAN` — *"A ship with conspicuous pirate markings is orbiting a nearby
     moon, broadcasting a simple message claiming to have equipment available for sale."*
     → "Hail the ship."
  2. `CONTACT_PIRATE_SALESMAN` — *"Yes, we have an extensive stock! Come aboard and see
     our wares!"* → "Dock with the ship." **or** the `req="slug"` variant *"(Slug) 'Sir:
     We can dock, but I sense that we better plan on making a purchase…'"*
  3. → `DOCK_PIRATE_SALESMAN` → **this event**.
- **The pool has one live member.** `DOCK_PIRATE_SALESMAN` contains two entries, but
  `<!--<event load="DOCK_BOMB_SALESMAN"/>-->` is commented out, so this event fires
  **100% of the time** you dock ([[source-newevents]]). See
  [[event-dock-bomb-salesman]].
- `PIRATE_SALESMAN` itself is a member of `NEUTRAL` and `NEUTRAL_EXIT` in `newEvents.xml`
  and of `OVERRIDE_NEUTRAL` / `OVERRIDE_NEUTRAL_EXIT` in `dlcEventsOverwrite.xml`
  ([[source-dlceventsoverwrite]]) — the hardcoded filler lists, so the chain can appear in
  any sector with unallocated beacons, and on exit beacons.
- **Advanced Edition content.** The whole `PIRATE_SALESMAN` family sits in the `DLC!!!`
  block of `newEvents.xml`, under the dev header *"New Matt Events"*, and every list entry
  loading `PIRATE_SALESMAN` is annotated as a DLC addition.
- Beacon: you are already docked; no ship is staged until you refuse to buy.

## Text
> A human in an exquisite suit meets you on board. "Welcome to my ship! We specialize in
> drones of all kinds, can I interest you in any?"

(`event_DOCK_DRONE_SALESMAN_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Buy some Drone parts. | — | −25 scrap, **+5 drone parts**. Fixed price. | 100% |
| 2 | Buy a Drone schematic. | — | −25 to −35 scrap, `drone name="RANDOM"` — **a random drone blueprint**. | 100% |
| 3 | Buy a Drone system upgrade. | `req="drones" max_lvl="3" max_group="0" blue="false"` | −15 to −20 scrap, `upgrade system="drones" amount="1"`. | 100% |
| 4 | Buy a Drone system upgrade. | `req="drones" min_level="4" max_lvl="5" max_group="0" blue="false"` | −25 to −33 scrap, +1 Drone Control level. | 100% |
| 5 | Buy a Drone system upgrade. | `req="drones" min_level="6" max_lvl="7" max_group="0" blue="false"` | −50 to −65 scrap, +1 Drone Control level. | 100% |
| 6 | Buy nothing. | — | *"Ah, I'm sorry to hear that! Pleasant journeys." … "You shouldn't waste people's time Captain!"* → **`ship load="PIRATE" hostile="true"`**, plus `damage amount="1" system="engines" effect="random"` and two × `damage amount="1" system="room" effect="random"`. | 100% |

Choices 3–5 are **three tiers of the same purchase**, not three separate options: the
`min_level` / `max_lvl` bounds mean exactly one of them is offered, selected by your
current Drone Control level. `blue="false"` means the option renders as a normal choice
rather than a blue one, despite carrying a `req` ([[source-newevents]]).

## Blue Options
None. Choices 3–5 carry `req="drones"` but are explicitly marked `blue="false"`, so they
are displayed as ordinary options gated by owning (and not having maxed) a Drone Control
system. The genuine blue options in this chain live one step upstream, on
`CONTACT_PIRATE_SALESMAN`: a `req="slug"` docking option and a `req="hacking"` option that
disables the pirate's weapons and extracts `autoReward level="LOW">scrap_only` instead.

## Rewards & Risks
- **Drone parts:** +5 for a flat 25 scrap — roughly store rates, with no store visit.
- **Drone schematic:** a random drone for 25–35 scrap. The pool is not specified in the
  event; `RANDOM` draws from the game's drone blueprint list.
- **Drone Control upgrade:** one level, priced by tier — 15–20 scrap at levels 1–3, 25–33
  at 4–5, 50–65 at 6–7.
- **Risk:** the "Buy nothing" exit. Three points of system damage spread across your
  engines and two random rooms, each with a random secondary effect (fire or breach), and
  then a `PIRATE` ship fight. Per `events_ships.xml` the `PIRATE` ship has
  `surrender chance="0.5" min="3" max="4"` and `escape chance="0.5" min="2" max="4"`, with
  default destroyed/deadCrew rewards ([[source-events-ships]]).
- There is no free exit from this screen. Once you have docked, you buy or you fight.

## Strategy Notes
- Treat docking as a commitment. The cheapest way out is the 25-scrap drone-parts purchase
  — far cheaper than three damaged rooms and a pirate fight.
- Without a Drone Control system, options 3–5 never appear and the drone parts are dead
  weight; the schematic is still worth buying if you plan to install Drone Control later.
- The tiered upgrade at levels 1–3 (15–20 scrap) undercuts the usual store price for a
  system level, which makes it the best line on the menu for a drone-focused build.
  (Opinion, reasoned from the price table; no source ranks these.)
- If you want the chain's *profit* rather than its shop, take the upstream Hacking option
  on `CONTACT_PIRATE_SALESMAN` instead of docking at all.

## Related
- [[event-pirate-ship-selling-drones]] — `PIRATE_SALESMAN`, the beacon that starts the chain
- [[event-pirate-ship-selling-drones]] — `CONTACT_PIRATE_SALESMAN`, the hail step with the
  Slug and Hacking blue options
- [[event-dock-bomb-salesman]] — `DOCK_BOMB_SALESMAN`, the disabled sibling shop
- [[item-drone-control]], [[entity-pirates]]

## Open Questions
- [ ] Which blueprint list `drone name="RANDOM"` draws from, and whether it can roll a
      drone you already own.
- [ ] What `max_group="0"` does to option display here.
- [ ] Whether a full Drone Control system (level 8) removes the upgrade option entirely —
      no tier covers level 8.
- [ ] The dev comment `<!-- MATT TODO - make this work? -->` sits directly above the first
      upgrade tier. Whether the tiering was ever verified in-engine is unknown.

## Sources
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
