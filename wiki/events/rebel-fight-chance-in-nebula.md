---
id: event-rebel-fight-chance-in-nebula
type: event
event_name: NEBULA_REBEL_CHASE
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]]]
beacon_type: nebula
hostile: false
blue_options: [[[item-sensors]], [[item-long-ranged-scanners]], [[item-lifeform-scanner]]]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [nebula, rebel, blue-option, sensors, fleet-advance, optional-fight, unique]
---

# Rebel fight chance in nebula — `NEBULA_REBEL_CHASE`

## Summary
You have the drop on a Rebel scout. Chasing it blind is a three-way roll that can cost you
fleet position; any one of **three different detection gates** turns it into a guaranteed
fight on your terms. It is the clearest illustration in the game of what sensor equipment
buys you inside a nebula.

## Trigger & Where It Appears
- Beacon: nebula (`<environment type="nebula"/>`).
- `unique="true"` — once per run.
- Lists: `NEBULA_NEUTRAL` and `NEBULA_NEUTRAL_SLUG` only ([[source-events-nebula]],
  [[source-events-slug]]) — so [[sector-uncharted-nebula]] (7–8 `NEBULA_NEUTRAL` beacons)
  and the two Slug sectors (3–5 `NEBULA_NEUTRAL_SLUG` beacons)
  ([[source-sector-data-xml]]). Fandom agrees exactly
  ([[source-fandom-rebel-fight-chance-in-nebula]]).
- Arrives non-hostile: `<ship load="REBEL" hostile="false"/>`. Long-range scanners show a
  ship.
- Flagged `NEW` in the file's header comment — a later addition.

## Text
> You spot a Rebel ship in the nebula ahead and stay off their radar. Try to engage?

(`event_NEBULA_REBEL_CHASE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Stay hidden. | — | *"You try and stay out of sight. You doubt they saw you."* — nothing happens. | 100% |
| 2 | Prepare to chase them! | — | `NEBULA_REBEL_CHASE_LIST`, three entries — **(a)** *"You follow their vapour trails and surf onto their six o'clock, weapons hot."* → fight; **(b)** *"Without sensors you can't maintain a lock for long. The Rebels slip away."* → nothing; **(c)** *"You get disoriented in the nebula and lose your bearings completely…"* → **`<modifyPursuit amount="1"/>`**. | unknown (3-entry list) |
| 3 | **(Advanced Sensors)** Try to track them as you move to engage. | `req="sensors" lvl="3"` — **not** `hidden` | *"As soon as they see you they make a run for it. You squeeze what you can out of the malfunctioning sensors and are able to keep track of them long enough to get in firing range."* → fight. | 100% |
| 4 | **(Long-ranged Scanner)** Try to track them as you move to engage. | `req="ADV_SCANNERS"`, `hidden="true"` | Same outcome text and same fight as #3 — the XML reuses `event_NEBULA_REBEL_CHASE_c3_text`. | 100% |
| 5 | **(Lifeform Scanner)** Use their life signatures to follow. | `req="LIFE_SCANNER"`, `hidden="true"` | *"Your augment's ability to keep track of their life signatures within the nebula proves useful. You catch up to the ship and prepare for a fight."* → fight. | 100% |

Choice 3 is the only blue option in the event that is **not** `hidden`, so its requirement
is visible before you take it ([[source-events-nebula]]).

The `REBEL` ship: `<surrender chance="0.5" min="2" max="3" load="PIRATE_SURRENDER"/>`,
`<escape chance="0.5" min="3" max="4" load="PIRATE_ESCAPE"/>`,
`<destroyed load="DESTROYED_DEFAULT"/>` → `autoReward level="MED">standard`
([[source-events-ships]], [[source-events-xml]]).

## Blue Options
Three gates, all producing the identical result — a guaranteed fight with no fleet-advance
risk:

- **[[item-sensors]] level 3** (`req="sensors" lvl="3"`) — the system, fully upgraded.
  Level 3 is the maximum, so this is a real investment.
- **[[item-long-ranged-scanners]]** (`req="ADV_SCANNERS"`) — the augment, no level gate.
- **[[item-lifeform-scanner]]** (`req="LIFE_SCANNER"`) — AE-only, marked `<!--DLC-->` in
  the XML.

Because all three converge on the same outcome, holding more than one buys nothing here.

## Rewards & Risks
- Reward: default `REBEL` combat rewards (`MED` / `standard` on a kill), on every path that
  reaches the fight.
- Risk on choice 2 only: a `modifyPursuit +1`, i.e. the Rebel fleet gains ground — the
  worst outcome available, and it is a third of the branch.
- Choice 1 is a guaranteed zero. The event cannot hurt you if you decline.

## Strategy Notes
- With any of the three gates: free fight, take it. Without: this is a genuine gamble —
  one third fight, one third nothing, one third fleet advance.
- The asymmetry is worth naming: the reward for chasing successfully is an ordinary Rebel
  fight, which is not a prize. Declining costs nothing. On a run that is behind the fleet,
  choice 1 is defensible even though it looks passive. *(Opinion; no source recommends a
  line.)*
- Fandom categorises this as a `Rebel Fleet advancement risk` — a *risk*, unlike
  [[event-auto-ship-warning-in-nebula]] which it calls a *hazard*
  ([[source-fandom-rebel-fight-chance-in-nebula]]).

## Related
- [[event-rebel-fight-choice-in-nebula]] — the mirror image: they have the drop on *you*
- [[event-nebula-lost-ship]] — the other Long-Ranged-Scanners nebula gate
- [[event-rebel-fight-in-nebula]] — the shadowed forced version
- [[item-sensors]], [[item-long-ranged-scanners]], [[item-lifeform-scanner]],
  [[concept-rebel-fleet-advance]], [[concept-rebel-fleet-advance]]
- [[sector-uncharted-nebula]], [[sector-slug-home-nebula]],
  [[sector-slug-controlled-nebula]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Weights inside `NEBULA_REBEL_CHASE_LIST` (3 entries, no weights stated).
- [ ] What `modifyPursuit amount="1"` does mechanically — see the contradiction note on
      [[event-auto-ship-warning-in-nebula]].

## Notes on transcription
> ⚠️ **CONTRADICTION (wording):** Fandom renders the choice-3/4 outcome as *"…able to keep
> track of them **enough** to get in firing range"*
> ([[source-fandom-rebel-fight-chance-in-nebula]]); the game string reads *"…able to keep
> track of them **long enough** to get in firing range"* ([[source-text-events-xml]]).
> Trusting the game files. Almost certainly a wiki transcription slip rather than a version
> difference — the same page also lower-cases "Rebel" throughout.

## Sources
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-fandom-rebel-fight-chance-in-nebula]] (per raw/wiki/rebel-fight-chance-in-nebula.md)
