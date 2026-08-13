---
id: event-research-station-with-no-response
type: event
event_name: STATION_SICK
sectors: [[[sector-pirate-controlled-sector]], [[sector-federation-space]]]
beacon_type: distress
hostile: false
blue_options: [[[item-anti-personnel-drone]], [[item-lifeform-scanner]], medbay 2, medbay 3, teleporter]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 9
tags: [unique, boarding-risk, crew-loss-risk, crew-reward-chance, drone-parts, blue-option, ae-only-branch]
---

# Research station with no response — `STATION_SICK`

## Summary
A silent research station that turns out to be full of people driven violently insane by
an alien neurotoxin. Docking is a genuine gamble — one of the three docking outcomes hands
you a free crew member, one costs you a crew member *and* boards you, and one is a clean
drone-parts pickup. Two augments (Anti-Personnel Drone, Lifeform Scanner) and three tiers
of Medbay each provide a safer path in, which makes this one of the most blue-option-dense
events in the base pool.

## Trigger & Where It Appears
- Sectors: [[sector-pirate-controlled-sector]] in practice; [[sector-federation-space]]
  only nominally — see below.
- Reached through the `BOARDERS_PIRATE` list ([[source-events-pirate]]) and the generic
  `HOSTILE_BOARDING` list ([[source-newevents]]).
- **`STANDARD_SPACE` allocates `<event name="HOSTILE_BOARDING" min="0" max="0"/>`**
  ([[source-sector-data-xml]]). Federation Space therefore places **zero** beacons from the
  only pool that could carry this event there — list membership without allocation. This is
  why the Fandom page files the event under Pirate Controlled Sector alone
  ([[source-fandom-research-station-with-no-response]]), and the two sources agree once the
  allocation is read. See [[concept-sector-event-allocation]].
- `unique="true"` — at most once per run.
- The event carries **no** `<distressBeacon/>` tag in the game files, but the prose says
  the station is "putting out a distress signal" and the Fandom page files it under
  distress-style locations ([[source-fandom-research-station-with-no-response]]).
- Its two outcome lists are reused elsewhere: `MERCHANT_DELIVER_LIST` loads
  `STATION_SICK_LIST` and `STATION_SICK_DRONE_LIST` for the Merchant's Delivery scenario,
  so you can meet the same outcomes without meeting this event
  ([[source-events-xml]]). The Lifeform Scanner branch belongs to `STATION_SICK` only, so
  it does not appear in that reuse
  ([[source-fandom-research-station-with-no-response]]).

## Text
> You arrive to find a small research station putting out a distress signal. There is no
> response to your hails.

(`event_STATION_SICK_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Dock with the station and investigate. | — | One of three members of `STATION_SICK_LIST` — see below. | 1/3 each (assumes uniform selection across list entries, [[concept-event-list-weighting]]) |
| 2 | Leave it alone. | — | Nothing happens. | 100% |
| 3 | **(Anti-Personnel Drone)** Use an Anti-Personnel Drone to investigate. | `req="BATTLE"` | One of three members of `STATION_SICK_DRONE_LIST`; **all three cost −1 drone part**. Two do nothing else; one also pays `autoReward level="MED"` `standard`. | 1/3 each (same assumption) |
| 4 | **(Life Scanner)** Run advanced life scans. | `req="LIFE_SCANNER"` — Advanced Edition only | One of two members of `STATION_SICK_SCANNER`: nothing, or `autoReward level="MED"` `standard`. No risk either way. | 1/2 each (same assumption) |

### `STATION_SICK_LIST` — the docking outcomes

**(a) Dead scientists.**
> Inside there are signs of a great struggle; scientists lie dead where they fell,
> brutally dismembered. You grab a few research drone parts lying on a desk near the door
> and leave quickly.

→ `autoReward level="MED"` `droneparts`. No further choice.

**(b) The frantic survivor.**
> You dock with the station and see a frantic person banging on the airlock door. Once
> inside your ship, he drops to the floor saying, "My... friends... They've gone insane...
> They're coming!" You hand him a blaster and turn to see a number of people charging
> toward the ship.

→ `<crewMember amount="1"/>` — **you gain a crew member immediately**, then choose:

| Choice | Requirement | Outcome |
|--------|-------------|---------|
| Prepare for a fight! | — | 3–4 **human** boarders (`boarders min="3" max="4" class="human"`) |
| **(Medbay)** Have the Advanced Medbay analyze their condition. | `req="medbay" lvl="3"` (`max_group="0"`) | No boarders. A second crew member with **1 skill in repair**, plus `autoReward level="MED"` `scrap_only` |

**(c) The infected away team.**
> As you explore the base, crazed screams are heard. Your team retreats back to your ship
> with a number of armed scientists in pursuit. One of your team starts to cough and falls
> in a spasm onto the floor.

| Choice | Requirement | Outcome |
|--------|-------------|---------|
| Drag him back to the ship and prepare for a fight. | — | **Lose a crew member** (`crewMember amount="-1" class="traitor"` — he turns hostile) **and** 3–4 human boarders |
| **(Teleporter)** Use your Teleporter to retrieve your crew. | `req="teleporter"` | **Lose a crew member** to the traitor conversion, but **no** boarders |
| **(Medbay)** Drag him back to the Medbay. | `req="medbay" lvl="2"` (`max_group="0"`) | Crew member saved; 3–4 human boarders still beam aboard |
| **(Advanced Medbay)** Have the Advanced Medbay analyze their condition. | `req="medbay" lvl="3"` (`max_group="0"`) | Crew member saved, no boarders, **and you gain a crew member** |

(All XML per [[source-events-xml]]; all prose per [[source-text-events-xml]].)

## Blue Options
- **Anti-Personnel Drone** (`req="BATTLE"`, the `BATTLE` drone blueprint =
  "Anti-Personnel Drone", [[source-blueprints]] / [[source-text-blueprints]]) — replaces
  the docking gamble with a risk-free probe. No boarders and no crew loss are possible on
  this branch. It reads `−1 drone part` on the button.
  > ⚠️ **CONTRADICTION / bug note:** the game files apply
  > `<item type="drones" min="-1" max="-1"/>` on **all three**
  > `STATION_SICK_DRONE_LIST` members ([[source-events-xml]]). Fandom footnotes the
  > branch as *"Bugged: no drone part is lost if the reward includes drone parts, though
  > you still need at least 1 drone part to choose this blue option"*
  > ([[source-fandom-research-station-with-no-response]]). This is an engine-behaviour
  > claim the XML cannot confirm or deny — the XML is what the data says, the Fandom note
  > is what players observe. Both recorded; unresolved.
- **Lifeform Scanner** (`req="LIFE_SCANNER"`) — the safest option in the event: a coin
  flip between nothing and a MED `standard` reward, with **zero** downside and no
  resource cost. `LIFE_SCANNER` is defined in `dlcBlueprints.xml`, i.e. it is
  Advanced Edition content ([[source-dlcblueprints]]).
- **Medbay level 2** — on outcome (c), converts a guaranteed crew loss into a survivable
  boarding fight.
- **Medbay level 3** — the best branch on both (b) and (c): removes the boarders entirely
  and adds a crew member. Note both level-3 choices carry `max_group="0"`, so they are
  offered ahead of the level-2 variant rather than alongside it.
- **Teleporter** — on outcome (c), keeps the boarders off your ship but does not save the
  infected crew member.

## Rewards & Risks
- Best realistic case: dock, hit outcome (b) or (c) with Medbay 3 → **two crew members**
  (or one crew plus MED `scrap_only`).
- Worst case: dock, hit outcome (c), no blue option → **a crew member turns traitor and
  3–4 human boarders spawn**. This is the crew-wipe scenario if you are already thin.
- Middle: MED `droneparts`, or a MED `standard` payout on the drone / scanner branches.
- The drone branch costs a drone part per the XML (see the flagged bug note above).

## Version differences
The `<!--DLC-->` markers in `events.xml` sit on choice 4 and on the whole
`STATION_SICK_SCANNER` list ([[source-events-xml]]), so per the base-file convention the
**vanilla** event is choices 1–3 only. The rest of the event — including the Medbay and
Teleporter blue options — is unmarked and therefore present in both editions.

## Strategy Notes
- With the Lifeform Scanner, always take choice 4: it strictly dominates everything else
  (no cost, no risk, 50% of a MED reward). *Opinion, derived from the outcome tables.*
- With Medbay 3 and spare crew, docking is a good bet — two of the three docking outcomes
  hand you crew, and the third pays drone parts. Without a Medbay, docking is a 1-in-3
  shot at losing a crew member *and* fighting boarders.
- The Anti-Personnel Drone branch is the "I cannot afford a boarding fight" answer.

## Related
- [[event-merchants-request]] — reuses `STATION_SICK_LIST` and `STATION_SICK_DRONE_LIST`
  in its Merchant's Delivery scenario (without the Lifeform Scanner branch)
- [[concept-event-list-weighting]] — the assumption behind the odds above
- [[concept-sector-event-allocation]] — how `HOSTILE_BOARDING` gets placed
- [[item-anti-personnel-drone]], [[item-lifeform-scanner]]
- [[sector-federation-space]], [[sector-pirate-controlled-sector]]

## Open Questions
- [ ] Is the drone-part cost actually skipped on the rewarding branch, as Fandom's bug
      note claims? Needs an observed run.
- [ ] Exact scrap/resource values behind `MED standard`, `MED droneparts` and
      `MED scrap_only`.
- [ ] Does `max_group="0"` on the Medbay-3 choices suppress the Medbay-2 choice, or are
      both shown when you have level 3?
- [ ] Is `HOSTILE_BOARDING min=0 max=0` in `STANDARD_SPACE` deliberate (keep boarding out
      of the first sector) or a leftover? Either way it makes the event unreachable there.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-events-pirate]] (per `raw/gamedata/events_pirate.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-blueprints]] (per `raw/gamedata/blueprints.xml`)
- [[source-text-blueprints]] (per `raw/gamedata/text_blueprints.xml`)
- [[source-dlcblueprints]] (per `raw/gamedata/dlcBlueprints.xml`)
- [[source-fandom-research-station-with-no-response]] (per
  `raw/wiki/research-station-with-no-response.md`)
</content>
</invoke>
