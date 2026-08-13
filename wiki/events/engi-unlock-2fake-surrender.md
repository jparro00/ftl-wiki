---
id: event-engi-unlock-2fake-surrender
type: event
event_name: ENGI_UNLOCK_2FAKE_SURRENDER
sectors: []
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-stealth-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [orphan, chain, surrender, decoy]
---

# Engi unlock — decoy base surrender — `ENGI_UNLOCK_2FAKE_SURRENDER`

## Summary
The surrender dialogue at the decoy Rebel base. The scout admits the envoy you followed was
a fake, and you choose whether to let it go or finish it off. This is the moment the game
tells you which of the two markers you picked — and it is worth noting the fight can be
resumed here, which the real beacon's equivalent does not allow.

## Trigger & Where It Appears
- **Not in any sector event list.** Loaded by the decoy scout's surrender block at
  [[event-engi-unlock-2fake]]:
  `<surrender min="4" max="4" load="ENGI_UNLOCK_2FAKE_SURRENDER"/>`
  ([[source-events-xml]], per `raw/gamedata/events_ships.xml`).
- Beacon: **quest** — it happens in combat at the decoy quest-marker beacon.
- Fandom folds it into the "Second Quest Marker (Fake)" section of the chain walkthrough
  ([[source-fandom-engi-fleet-discussion]]).

## Text
> "Stop! I don't want to die here."

(`event_ENGI_UNLOCK_2FAKE_SURRENDER_text`, per [[source-text-events-xml]])

Compare the real beacon's *"Stop! This isn't worth dying for..."*
([[event-engi-unlock-2real-surrender]]) — a second, later tell that the two beacons differ.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Demand information on the stolen technology. | — | *"Ah, so that's what you're after. Too bad, you followed the wrong ship. The envoy that passed through here was a fake, to trick fools like you. Now let us go!"* → two follow-ups. | 100% |
| 1a | Let them go. | — | `<ship hostile="false"/>` — the ship turns neutral and the encounter ends. Nothing gained. | 100% |
| 1b | Ignore him and attack. | — | *"'No, wait...' You cut the transmission and continue the assault."* → the fight resumes; the ship's `destroyed` / `deadCrew` blocks then pay `MED` `standard`. | 100% |

No branch here places or removes a quest marker ([[source-events-xml]], per
`raw/gamedata/events_engi.xml`).

## Blue Options
None.

## Rewards & Risks
- Choice 1a: nothing.
- Choice 1b: resumes the fight for `MED` scrap with resources, at the cost of whatever hull
  the rest of the fight takes.
- No effect on [[chain-stealth-cruiser-unlock]] either way.

## Strategy Notes
- Choice 1b is the only way to get paid at this beacon once the ship has surrendered — 1a
  ends it with nothing. Whether that is worth finishing a surrendered ship depends on how
  much hull the fight has already cost you. *(Opinion.)*
- The corresponding "attack anyway" branch was deliberately **removed** from the real
  beacon's surrender event to avoid placing two quest markers
  ([[event-engi-unlock-2real-surrender]]) — so this asymmetry between the two is intentional.

## Related
- [[chain-stealth-cruiser-unlock]]
- [[event-engi-unlock-2fake]] — the fight this resolves
- [[event-engi-unlock-2real-surrender]] — the real beacon's equivalent, minus the attack branch

## Open Questions
- [ ] After choosing "Let them go", can the beacon still be re-engaged?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`, `raw/gamedata/events_ships.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-fandom-engi-fleet-discussion]] (per `raw/wiki/engi-fleet-discussion.md`)
