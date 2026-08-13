---
id: event-pirate-ship-selling-drones
type: event
event_name: PIRATE_SALESMAN
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: any
hostile: false
blue_options: [slug crew, hacking system]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [pirate, trading, unique, blue-option, drone-reward, system-upgrade, trap, advanced-edition]
---

# Pirate ship selling drones — `PIRATE_SALESMAN`

## Summary
A pirate advertising a shop. It is a genuine shop — a drone-parts, drone-schematic and
Drone Control upgrade counter you can reach without a store beacon — but it is also a
shakedown: walking away empty-handed after docking triggers an attack. Two blue options
change the encounter, one of which (Hacking) skips the shop entirely for free scrap.

## Trigger & Where It Appears
- `unique="true"` — once per run.
- Event lists: `NEUTRAL` and `NEUTRAL_EXIT` in `newEvents.xml`, both tagged
  `<!--DLC matt - down below-->` / `<!--DLC - down below-->` ([[source-newevents]]), and
  their Advanced Edition replacements `OVERRIDE_NEUTRAL` and `OVERRIDE_NEUTRAL_EXIT`
  ([[source-dlceventsoverwrite]]).
- Those are the universal filler / exit pools, so the event's real reach is "any sector
  that falls back on generic neutrals", not one faction's space. Fandom scopes it to the
  Slug sectors and marks it an exit-and-filler event
  ([[source-fandom-pirate-ship-selling-drones]]) — a narrower claim than the lists
  support, recorded as the practical answer rather than the complete one.
- Beacon: ordinary. No `<distressBeacon/>`, no `<environment>`.

## Text
> A ship with conspicuous pirate markings is orbiting a nearby moon, broadcasting a simple
> message claiming to have equipment available for sale.

(`event_PIRATE_SALESMAN_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Hail the ship. | — | Loads `CONTACT_PIRATE_SALESMAN` — see below. | — |
| 2 | Attack him before he can attack! | — | `<ship load="PIRATE" hostile="true"/>` — standard pirate fight, default rewards. | 100% |
| 3 | Quickly prepare to jump away. | — | `<event/>` — nothing happens. | 100% |

### `CONTACT_PIRATE_SALESMAN`
> The ship responds "Yes, we have an extensive stock! Come aboard and see our wares!"

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Dock with the ship. | — | Loads `DOCK_PIRATE_SALESMAN` → always `DOCK_DRONE_SALESMAN` (below). | 100% |
| 2 | This seems dangerous, leave. | — | *"As soon as you start to reverse your ship, the pirate reveals hidden weaponry and sets off in pursuit. You'll have to fight him to escape!"* → fight `PIRATE`. | 100% |
| 3 | **(Slug)** *"Sir: We can dock, but I sense that we better plan on making a purchase..."* | `req="slug"` | Loads the same `DOCK_PIRATE_SALESMAN`. | 100% |
| 4 | **(Hacking)** Disable their Weapon system before docking. *(hidden)* | `req="hacking"` | *"You receive a hail as soon as your Hacking system finishes: 'What have you done!? … Here, take your standard toll.'"* → `autoReward level="LOW"` `scrap_only`. **No shop.** | 100% |

Note the shape of choice 2: *leaving* after hailing is the same fight as attacking, so
hailing already commits you to either docking or fighting.

### `DOCK_PIRATE_SALESMAN` — a one-member list
```xml
<eventList name="DOCK_PIRATE_SALESMAN">
    <!--<event load="DOCK_BOMB_SALESMAN"/>-->
    <event load="DOCK_DRONE_SALESMAN"/>
</eventList>
```
([[source-newevents]], lines 1843–1846). **The bomb/missile salesman is commented out**, so
docking always produces the drone shop. `DOCK_BOMB_SALESMAN` itself is fully authored —
5 missiles for 10 scrap, `WEAPONS_BOMBS_CHEAP` for 40–60 scrap,
`WEAPONS_MISSILES_EXPENSIVE` for 50–60 scrap, and the same "buy nothing" ambush — but is
unreachable in the shipped game. It is documented here rather than on its own page because
it is a sub-event of this one. Fandom does not mention it at all.

### `DOCK_DRONE_SALESMAN` — the shop
> A human in an exquisite suit meets you on board. "Welcome to my ship! We specialize in
> drones of all kinds, can I interest you in any?"

| # | Choice | Requirement | Cost | You get |
|---|--------|-------------|------|---------|
| 1 | Buy some Drone parts. | — | 25 scrap (fixed) | **5 drone parts** |
| 2 | Buy a Drone schematic. | — | 25–35 scrap | `<drone name="RANDOM"/>` — a random drone schematic |
| 3 | Buy a Drone system upgrade. | `req="drones"`, `max_lvl="3"`, `blue="false"` | 15–20 scrap | Drone Control +1 level |
| 4 | Buy a Drone system upgrade. | `req="drones"`, `min_level="4" max_lvl="5"`, `blue="false"` | 25–33 scrap | Drone Control +1 level |
| 5 | Buy a Drone system upgrade. | `req="drones"`, `min_level="6" max_lvl="7"`, `blue="false"` | 50–65 scrap | Drone Control +1 level |
| 6 | Buy nothing. | — | — | *"…a series of explosions rocks your ship… 'You shouldn't waste people's time Captain!'"* → fight `PIRATE`, plus `damage amount="1" system="engines" effect="random"` and two `damage amount="1" system="room" effect="random"` |

Choices 3–5 are the same offer at three price tiers; they carry `blue="false"`, so they
appear as ordinary options rather than blue ones, and are only offered if you already own
Drone Control at the matching level. The XML carries a developer note beside them:
`<!-- MATT TODO - make this work? -->` ([[source-newevents]], line 1867).

> ⚠️ **CONTRADICTION:** the "Buy nothing" damage.
> - Game files: three separate `<damage amount="1" .../>` entries — engines, and two random
>   rooms — each with `effect="random"`. No hull-only damage entry
>   ([[source-newevents]]).
> - Fandom: *"Your ship takes 3 hull damage, 1 damage with a random effect to engines,
>   1 damage with a random effect to each of 2 random rooms"*
>   ([[source-fandom-pirate-ship-selling-drones]]).
>
> Trusting the game files for what is written (`high` vs `medium`). Fandom's "3 hull" is
> most likely its rendering of the fact that each point of system damage also removes a
> point of hull — a game-engine behaviour, not an extra XML entry. Not resolved here.

## Blue Options
- **Slug crew** (`req="slug"`) — adds a fourth line to the hail, but loads exactly the same
  `DOCK_PIRATE_SALESMAN` list as plain docking. Mechanically it changes nothing. Fandom
  reads its wording ("we better plan on making a purchase") as a deliberate warning to the
  player that leaving without buying triggers the ambush
  ([[source-fandom-pirate-ship-selling-drones]]) — a plausible reading, but an
  interpretation, not a datafile fact.
- **[[item-hacking]]** (`req="hacking"`, `hidden="true"`) — the only branch that ends the
  encounter safely and profitably: `autoReward level="LOW"` `scrap_only` and no shop, no
  fight. If you are not planning to buy drones, this is strictly the best line.

## Rewards & Risks
- **Rewards:** 5 drone parts for a flat 25 scrap; a random drone schematic for 25–35;
  Drone Control upgrades at roughly store prices; or free low scrap via Hacking.
- **Risks:** three of the paths end in a `PIRATE` fight (attack, leave-after-hailing, and
  buy-nothing), and the buy-nothing path additionally damages engines and two rooms with
  fire/breach effects before the fight starts.
- `PIRATE` is the standard pirate ship: 50% surrender chance, 50% escape chance,
  `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT` rewards ([[source-events-ships]]).

## Strategy Notes
- *(Opinion.)* Once you dock you should buy something. The cheapest exit is the 25-scrap
  drone-parts purchase — far cheaper than eating three system hits and a fight.
- 5 drone parts for 25 scrap is a good rate, and this is one of the few ways to buy drone
  parts outside a store.
- With Hacking installed, take that option: it converts a shakedown into free scrap. The
  only reason not to is if you actually want the shop.
- Attacking immediately (choice 2) gets you the fight with no system damage — strictly
  better than docking and refusing to buy, if a fight is what you want.

## Related
- [[event-pirate-ship-selling-weapon]] — the weapon-shop counterpart
- [[item-hacking]] — unlocks the clean exit
- [[item-drone-control]] — the upgrade sold here
- [[entity-pirates]], [[entity-slugs]]

## Open Questions
- [ ] Whether "3 hull damage" in the Fandom entry is engine behaviour or a wiki error.
- [ ] Why `DOCK_BOMB_SALESMAN` was commented out — no dev note gives a reason.
- [ ] Whether the `MATT TODO` note beside the upgrade tiers means they misbehave in the
      shipped build.
- [ ] The full sector reach of `NEUTRAL` / `NEUTRAL_EXIT` filler placement.

## Sources
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-dlceventsoverwrite]] (per `raw/gamedata/dlcEventsOverwrite.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-pirate-ship-selling-drones]] (per `raw/wiki/pirate-ship-selling-drones.md`)
