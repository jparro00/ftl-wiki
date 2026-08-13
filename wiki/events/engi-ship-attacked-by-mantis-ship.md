---
id: event-engi-ship-attacked-by-mantis-ship
type: event
event_name: ENGI_STATION_DISTRESS
sectors: [[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]]
beacon_type: any
hostile: true
blue_options: [engi crew]
chain: [[[chain-hidden-federation-base]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [boarding-risk, crew-reward, fuel-reward, weapon-reward, drone-reward, hull-repair, quest-marker, blue-option]
---

# Engi ship attacked by Mantis ship — `ENGI_STATION_DISTRESS`

## Summary
The richest reward tree in Engi space, and the only event there that can hand you a quest
marker. Answering the call is a coin flip between a genuine rescue — which leads to a
four-way reward list including a free Engi crewmember — and a Mantis ambush that beams
boarders onto your ship. An Engi crewmember unlocks the best node in the reward list: a
weapon, 10 hull repairs, and the **Hidden Federation Base** marker.

## Trigger & Where It Appears
- Sectors: [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]
- Event lists: **both** `DISTRESS_BEACON_ENGI` (`min=1 max=3`) and `NEUTRAL_ENGI`
  (`min=4 max=6` / `min=5 max=7`) ([[source-events-xml]], [[source-sector-data-xml]])
- `unique="false"` — explicitly repeatable, unlike most of the Engi set
- Beacon: **not** flagged as a distress beacon despite its name and its list membership —
  the definition has no `<distressBeacon/>` tag.

Both sources agree on that last point, and it is worth stating plainly: Fandom notes "this
event is meant to occur at a distress beacon but won't because the `<distressBeacon/>` tag
is missing in its definition" ([[source-fandom-engi-ship-attacked-by-mantis-ship]]), and
the game file confirms the tag is absent where its two `DISTRESS_BEACON_ENGI` list-mates
[[event-engi-distress-rebel-fight]] and [[event-engi-research-station]] both have it
([[source-events-xml]]).

## Text
> You receive a distress call from a nearby Engi ship. "Assistance requested. Danger
> present. Imminent destruction."

(`event_ENGI_STATION_DISTRESS_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Respond to the call and move in to assist. | — | Loads `ENGI_STATION_DISTRESS_LIST` — see the two branches below. | — |
| 2 | Keep your distance. | — | Empty `<event/>` — nothing happens. | 100% |

### Branch A — the trap

> You receive another message from the ship, this time with a Mantis at the comm-log.
> "Foolish meatsacks," he yells. Sensors indicate the ship is moving in to attack and
> boarders teleport from the station.

Fight `ENGI_MANTIS_CONTROLLED` — a Mantis-crewed Engi hull (`auto_blueprint="SHIPS_CIRCLE"`,
`<crewMember type="mantis"/>`) using `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT`, i.e. default
rewards — **and** `<boarders min="1" max="2" class="mantis"/>` beam aboard your ship
immediately ([[source-events-xml]]).

### Branch B — the real rescue

> You approach to find a Mantis ship assaulting a small Engi space station. You prepare for
> a fight!

Fight `MANTIS_ENGI_STATION`. **Destroyed** → `MED` `standard`; **dead crew** → `HIGH`
`standard`. Either way, continue → the `SAVE_ENGI_STATION` list, one of four:

| # | `SAVE_ENGI_STATION` entry | Outcome | Odds |
|---|---------------------------|---------|------|
| B-1 | *"The Engi station is stripped bare… The Mantis must have left the distress call active to lure other ships into a trap."* | Nothing. | unknown |
| B-2 | *"The station was in the process of being evacuated… They offer some fuel as a reward."* | `<autoReward level="MED">fuel_only</autoReward>` | unknown |
| B-3 | *"The station hails you, 'Gratitude. Expected probability of defeat without assistance... 86.2 percent. Request suitable reward.'"* | A four-way choice — see below. | unknown |
| B-4 | *"They thank you for the assistance and when you tell them of your mission, one of the Engi asks if he can assist your crew."* | `<crewMember amount="1" class="engi"/>` **and** `LOW` `standard`. | unknown |

#### B-3 — "Request suitable reward"

| # | Choice | Requirement | Outcome |
|---|--------|-------------|---------|
| B-3-1 | Request fuel. | — | `<autoReward level="HIGH">fuel</autoReward>` |
| B-3-2 | Request weapon. | — | `<autoReward level="LOW">weapon</autoReward>` |
| B-3-3 | Request drone. | — | `<autoReward level="LOW">drone</autoReward>` |
| B-3-4 | **(Engi Crew)** "Threat unresolved. Current mission imperative: Protocol 52.34." | `req="engi"` | `<autoReward level="LOW">weapon</autoReward>`, `<damage amount="-10"/>` (**10 hull repairs**), and `<quest event="HIDDEN_FEDERATION_BASE_LIST"/>` — a **[[chain-hidden-federation-base]]** quest marker is added to your map. |

## Blue Options
- **Engi crewmember** (`req="engi"`) — gates node B-3-4 only, two layers deep. It is
  strictly better than B-3-2, the plain "Request weapon": same `LOW weapon` reward, plus 10
  hull repairs, plus the quest marker ([[source-events-xml]]).

## Rewards & Risks
- **Best case:** a free Engi crewmember (B-4), or the blue option at B-3-4 for a weapon +
  10 repairs + a quest chain.
- **Fuel:** `MED` `fuel_only` at B-2, `HIGH` `fuel` at B-3-1. Fandom puts numbers on these —
  "medium (2-4)" and "high (3-6)" — but see the contradiction below.
- **Risk:** branch A boards you with 1–2 Mantis while you fight. Mantis boarders are the
  worst-case boarding threat in the game, and this is a choice you make blind — nothing in
  the intro distinguishes the trap from the rescue.
- Branch B-1 pays nothing even after you win the fight (beyond the fight's own `MED`/`HIGH`).

> ⚠️ **CONTRADICTION:** fuel quantities.
> - Game files state reward *levels* only: `<autoReward level="MED">fuel_only</autoReward>`
>   and `<autoReward level="HIGH">fuel</autoReward>`, with no numbers anywhere
>   ([[source-events-xml]], per `raw/gamedata/events_engi.xml`).
> - Fandom gives "medium **(2-4)** fuel" and "high **(3-6 fuel)**"
>   ([[source-fandom-engi-ship-attacked-by-mantis-ship]]).
>
> Not a disagreement so much as an addition: the numbers are community-derived and cannot be
> checked against the files. Trust the levels as fact; treat the ranges as `medium`
> reliability.

## Strategy Notes
- The boarding branch makes this a bad event to take at low crew or with no Medbay, and a
  good one if you have a Medbay chokepoint set up. *(Opinion.)*
- With an Engi aboard, B-3-4 is the node to hope for — it is the only route to
  [[chain-hidden-federation-base]] recorded on this page, and 10 free repairs is a large
  swing. *(Opinion.)*
- Killing the Mantis crew rather than destroying the ship upgrades branch B's fight reward
  from `MED` to `HIGH`.
- Because the event is `unique="false"` and sits in two lists at once, it can appear more
  than once per sector — which makes it the most likely Engi-space source of a free crew
  member. *(Opinion.)*

## Related
- [[chain-hidden-federation-base]] — the quest the blue option starts
- [[event-engi-research-station]] — the other Engi event that can award an Engi crewmember
- [[event-mantis-fight-engi]] — a Mantis fight you cannot decline
- [[entity-mantis]], [[entity-engi]]

## Open Questions
- [ ] Odds of the trap branch vs the rescue branch on choice 1.
- [ ] Relative weighting of the four `SAVE_ENGI_STATION` entries.
- [ ] Are Fandom's 2–4 / 3–6 fuel ranges reproducible?
- [ ] Is the missing `<distressBeacon/>` tag fixed in any later patch?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`, `raw/gamedata/events_ships.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-engi-ship-attacked-by-mantis-ship]] (per `raw/wiki/engi-ship-attacked-by-mantis-ship.md`)
