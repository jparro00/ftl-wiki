---
id: event-fire-on-research-station
type: event
event_name: DISTRESS_STATION_FIRE
sectors: [[[sector-abandoned-sector]], [[sector-civilian-sector]], [[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: distress
hostile: false
blue_options: [[[item-repair-drone]], rock crew]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 13
tags: [distress, unique, blue-option, crew-loss-risk, clone-bay-revival, crew-reward-chance, augment-reward, drone-schematic-reward, rock-crew, named-crew]
---

# Fire on research station — `DISTRESS_STATION_FIRE`

## Summary
A laboratory fire is about to take a research station with it. Two unaided branches each roll
a coin: help fight the fire and risk a crewmember, or dock and risk hull for the chance to
recruit **Dr. Jones** — one of the game's few named crewmembers. The two blue options,
**Rock crew** and **Repair Drone**, both skip the gamble and pay a `HIGH` reward *plus* an
item: an augment or a drone schematic. Its sector spread is the joint-widest in this batch.
`unique="true"`.

## Trigger & Where It Appears
- Sectors: [[sector-federation-space]], [[sector-civilian-sector]],
  [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]],
  [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]],
  [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]],
  [[sector-rock-homeworlds]], [[sector-zoltan-controlled-sector]],
  [[sector-zoltan-homeworlds]], [[sector-uncharted-nebula]], [[sector-abandoned-sector]]
- Event lists: `DISTRESS_BEACON` ([[source-newevents]]), `DISTRESS_BEACON_MANTIS`
  ([[source-events-mantis]]), `DISTRESS_BEACON_PIRATE` ([[source-events-pirate]]),
  `DISTRESS_BEACON_REBEL` ([[source-events-rebel]]), `DISTRESS_BEACON_ROCK`
  ([[source-events-rock]]), `DISTRESS_BEACON_ZOLTAN` ([[source-events-zoltan]]),
  `DISTRESS_BEACON_LANIUS` ([[source-dlcevents-anaerobic]])
- It is a member of **every** faction distress list except the Engi one
  ([[source-events-engi]] — `DISTRESS_BEACON_ENGI` does not include it)
- Allocation: 1–2 or 1–3 depending on sector ([[source-sector-data-xml]])
- Beacon: `<distressBeacon/>`
- Long-range scanners show **no ship** ([[source-fandom-fire-on-research-station]])
- `unique="true"` — once per run

## Text
> You find the source of the distress call, a small research station. It appears a small
> laboratory fire got out of control and is threatening to destroy the station. Their fire
> suppression system is not responding.

(`event_DISTRESS_STATION_FIRE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Send your crew in a shuttle to help put out the fire. | — | Rolls `DISTRESS_STATION_FIRE_CREW` (2 entries) | 1/2 each |
| 2 | Dock and try to rescue the survivors. | — | Rolls `DISTRESS_STATION_FIRE_RESCUE` (2 entries) | 1/2 each |
| 3 | Leave. | — | *"You coldly shut off communications…"* → nothing | 100% |
| 4 | **(Rock Crew)** Send your Rock crew-member in. | `req="rock"` | *"Your Rock soldier tears through the airlock directly into the fire…"* → *Contact the survivors* → `autoReward level="HIGH"` **`augment`** | 100% |
| 5 | **(Repair Drone)** Send your Repair drone into the fire. | `req="REPAIR"` | *"You send the Repair drone in and it methodically puts out the fires…"* → *Contact the survivors* → `autoReward level="HIGH"` **`drone`** | 100% |

### Choice 1 → `DISTRESS_STATION_FIRE_CREW`

| Entry | Outcome | Share |
|---|---|---|
| 1 | *"…not before an unfortunate soul is lost in the inferno."* → `<removeCrew><clone>true</clone>` — **lose a crewmember** (Clone Bay revives) + `autoReward level="LOW"` `scrap_only` | 1/2 |
| 2 | *"Your crew valiantly keeps the fire at bay long enough to allow some of the scientists to escape…"* → `autoReward level="HIGH"` `scrap_only` | 1/2 |

### Choice 2 → `DISTRESS_STATION_FIRE_RESCUE`

| Entry | Outcome | Share |
|---|---|---|
| 1 | *"…a huge blast splits the station apart…some debris pierces your hull."* → `damage 3` + `damage 1 random system` (AE only) + `autoReward level="LOW"` `scrap_only` | 1/2 |
| 2 | *"One of the survivors offers to join your crew…"* → `<crewMember amount="1" id="name_DrJones"/>` — **Dr. Jones** — + `autoReward level="LOW"` `scrap_only` | 1/2 |

`name_DrJones` resolves to *"Dr. Jones"* ([[source-text-events-xml]]). The `crewMember` tag
carries **no `class` attribute**, so only the name is fixed, not the species.

Both splits are derived from entry counts and **assume uniform selection across list
entries** ([[source-events-xml]]).

The Clone Bay line on choice 1 is written for the occasion: *"With a new-found respect for
flames, your crewmember's clone stumbles out of the Clone Bay."*

## Blue Options
- **Rock crew** (`req="rock"`) — `HIGH` `augment`. Free, guaranteed, and the only augment
  reward in this batch.
- **[[item-repair-drone]]** (`req="REPAIR"`, the drone blueprint — [[source-blueprints]]) —
  `HIGH` `drone`, i.e. a drone schematic plus high scrap. **No drone part is spent**: unlike
  [[event-asteroid-belt-distress]] and [[event-giant-alien-spiders]], this branch has no
  `item_modify` tag ([[source-events-xml]]).

Both blue branches route through a shared *Contact the survivors* choice — the file reuses
`event_DISTRESS_STATION_FIRE_c4_c1_choice` for both ([[source-events-xml]]).

## Rewards & Risks
- **Best outcomes:** `HIGH` `augment` (Rock crew) or `HIGH` `drone` (Repair Drone), both
  free and certain; or `HIGH` `scrap_only` on a lucky choice 1.
- **Dr. Jones** — a named crewmember, on a coin flip via choice 2.
- **Risks:** a dead crewmember (choice 1, revivable in AE); or 3–4 hull and a system
  (choice 2). Both losing branches still pay `LOW` `scrap_only`, so nothing here is a total
  loss.
- Choice 3 is a completely free skip.

## Version Differences
Base-`events.xml` event, present in both editions. One `<!--DLC-->`-marked tag:
`<damage amount="1" system="random"/>` in `RESCUE` entry 1 ([[source-events-xml]]). Vanilla
takes **3 hull**; AE takes 4 hull and loses a random system — which is what Fandom
transcribes ([[source-fandom-fire-on-research-station]]).

The `<clone>true</clone>` branch on choice 1 only does anything with an AE Clone Bay; in
vanilla that crew loss is permanent.

## Strategy Notes
- *(Opinion.)* With a Rock crewmember or a Repair Drone, this is one of the best distress
  beacons in the game — a free `HIGH` reward *with an item attached*.
- Without a gate, choice 2 is usually the better gamble than choice 1: hull is cheaper than
  a crewmember, and the winning half hands you a crewmember instead.
- With a Clone Bay, that calculus flips — choice 1's downside becomes a temporary loss and
  its upside is `HIGH scrap_only`.

## Related
- [[event-giant-alien-spiders]], [[event-unknown-disease-on-mining-colony]] — the other two
  "send your crew into a station" distress events
- [[event-malfunctioning-defense-system]], [[event-crushed-pirate]],
  [[event-asteroid-belt-distress]] — the rest of the shared `DISTRESS_BEACON` pool
- [[item-repair-drone]], [[entity-rock-men]]

## Open Questions
- [ ] Are `<eventList>` entries selected uniformly? Both 1/2 figures assume it.
- [ ] What species Dr. Jones is — the `crewMember` tag fixes only the name.
- [ ] Which augment and which drone schematic `HIGH augment` / `HIGH drone` draw from.
- [ ] Why `DISTRESS_BEACON_ENGI` omits this event when every other faction list carries it.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml` — `DISTRESS_BEACON`)
- [[source-events-mantis]] (per `raw/gamedata/events_mantis.xml`)
- [[source-events-pirate]] (per `raw/gamedata/events_pirate.xml`)
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-events-rock]] (per `raw/gamedata/events_rock.xml`)
- [[source-events-zoltan]] (per `raw/gamedata/events_zoltan.xml`)
- [[source-events-engi]] (per `raw/gamedata/events_engi.xml` — the list that omits it)
- [[source-dlcevents-anaerobic]] (per `raw/gamedata/dlcEvents_anaerobic.xml`)
- [[source-blueprints]] (per `raw/gamedata/blueprints.xml` — the `REPAIR` drone)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-fire-on-research-station]] (per `raw/wiki/fire-on-research-station.md`)
