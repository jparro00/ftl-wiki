---
id: event-engi-research-station
type: event
event_name: DISTRESS_ENGI_REACTOR
sectors: [[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]]
beacon_type: distress
hostile: false
blue_options: [sensors lvl 2, [[item-long-ranged-scanners]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, blue-option, crew-risk, crew-reward, drone-reward, clone-bay]
---

# Engi research station — `DISTRESS_ENGI_REACTOR`

## Summary
A unique distress beacon in Engi space with a real crew-loss risk attached to a real
crew-*gain* reward. Boarding blind is a gamble: half the time the station is empty, and
when it isn't, both rescue options can cost you a crewmember. A scanner blue option skips
the gamble entirely and hands you the good branch with no downside — one of the cleanest
payoffs [[item-long-ranged-scanners]] gets anywhere in the game.

## Trigger & Where It Appears
- Sectors: [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]
- Beacon: **distress** — the event carries `<distressBeacon/>`
  ([[source-events-xml]], per `raw/gamedata/events_engi.xml`)
- Event list: `DISTRESS_BEACON_ENGI`, allocated `min=1 max=3` per Engi sector
  ([[source-sector-data-xml]])
- `unique="true"` — at most once per run

## Text
> You arrive at a smoldering Engi research station, its distress call unanswered -
> attacked by pirates or Mantis most likely. There may be someone left alive, or else
> something of value left on board.

(`event_DISTRESS_ENGI_REACTOR_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Board the station. | — | Loads `DISTRESS_ENGI_REACTOR_LIST1` → (a) the station is dead, nothing happens; (b) the **reactor-overload branch** below. | unknown |
| 2 | Ignore it. | — | "The place looks in bad state, probably nothing of use there. Time to move on." → nothing. | 100% |
| 3 | **(Improved Sensors)** Run another scan. | `req="sensors" lvl="2"` | Loads `DISTRESS_ENGI_REACTOR_SCAN` — the **safe** branch below. | 100% |
| 4 | **(Long Ranged Scanners)** Run another scan. | `req="ADV_SCANNERS"` | Same as #3. | 100% |

### Branch 1b — reactor overload (from boarding)

> Your away team reports a wounded Engi and a functioning drone schematic. Then someone
> yells. The station reactor is overloading and they're running out of time!

| # | Choice | Outcome(s) | Odds |
|---|--------|-----------|------|
| 1b-1 | Save the Engi! | Loads `DISTRESS_ENGI_REACTOR_ENGI` → (a) **you lose a crewmember** (`removeCrew`, `clone=true` — a Clone Bay revives them), then the rescued Engi joins: `+1 engi crewMember` and `LOW` `scrap_only`; (b) no loss at all: `+1 engi crewMember`, `LOW` `scrap_only`. | unknown |
| 1b-2 | Save the drone schematic. | Loads `DISTRESS_ENGI_REACTOR_DRONE` → (a) **you lose a crewmember** (`clone=true`, revivable) and get only `LOW` `scrap_only` — **no drone**; (b) `LOW` `drone`. | unknown |
| 1b-3 | Save yourselves! | "It's a tough order, but your crew's lives are the priority." → `LOW` `scrap_only`, no risk. | 100% |

### Branch 3/4 — second scan (the safe branch)

> Scans reveal the station's reactor is overloading! Not only that, but an injured Engi
> and a functioning drone schematic are still on board! There's not time for both...

| # | Choice | Outcome(s) | Odds |
|---|--------|-----------|------|
| S-1 | Save the Engi! | `+1 engi crewMember` and `LOW` `scrap_only`. No crew risk. | 100% |
| S-2 | Save the Drone Schematic! | `LOW` `drone` — a drone schematic with low scrap. No crew risk. | 100% |

`LOW`/`MED`/`HIGH` are the game's own `autoReward` levels; no source converts them to
numbers ([[source-events-xml]]).

## Blue Options
- **Sensors level 2+** (`req="sensors" lvl="2"`) — the Sensors *system* upgraded to level 2,
  not a crew species.
- **[[item-long-ranged-scanners]]** (`req="ADV_SCANNERS"`) — the augment, satisfying the same
  gate with no system investment.

Both load the identical `DISTRESS_ENGI_REACTOR_SCAN` sub-event. What they unlock is not a
new reward but the *removal of two layers of randomness*: the empty-station branch and both
crew-death branches disappear. The rewards themselves (`LOW scrap_only` + Engi crew, or
`LOW drone`) are the same ones the boarding branch can give you. ([[source-events-xml]])

## Rewards & Risks
- **Best case:** a free Engi crewmember plus low scrap, at zero risk, via the scan.
- **Drone route:** a drone schematic with low scrap.
- **Risk (boarding only):** two of the six boarding sub-outcomes kill a crewmember. Both are
  flagged `<clone>true</clone>`, so a Clone Bay brings them back
  ([[source-events-xml]]). Fandom adds that on the "Save the Engi!" death branch you
  receive the Engi *regardless* of whether you have a Clone Bay
  ([[source-fandom-engi-research-station]]) — consistent with the files, where the
  `crewMember` award sits in the continue-choice after the `removeCrew`.
- **Wasted-risk case:** losing a crewmember on the drone branch pays only low scrap — the
  drone is not awarded on that outcome.

## Strategy Notes
- With Sensors 2 or Long-Ranged Scanners, this is a strictly free event — take the scan,
  then take the Engi unless you specifically need a drone schematic. *(Opinion, derived
  from the outcome tables above.)*
- Without a scanner, boarding is a genuine gamble and "Save yourselves!" is the only
  risk-free exit once you're in the overload branch — it pays the same low scrap the
  failed drone branch pays, without the death roll.
- With a Clone Bay the crew-loss branches are largely defanged, which makes blind boarding
  much more attractive. *(Opinion.)*

## Related
- [[event-engi-distress-rebel-fight]] — the other unique distress event in `DISTRESS_BEACON_ENGI`
- [[event-engi-ship-attacked-by-mantis-ship]] — shares the list, also awards an Engi crewmember
- [[entity-engi]] — the species you can recruit here
- [[item-long-ranged-scanners]] — the augment that trivialises this event

## Open Questions
- [ ] Odds of the empty-station vs reactor-overload split on choice 1.
- [ ] Odds of the death vs clean outcome within each rescue sub-list.
- [ ] Scrap value of `LOW` `scrap_only` at a given sector depth.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-engi-research-station]] (per `raw/wiki/engi-research-station.md`)
