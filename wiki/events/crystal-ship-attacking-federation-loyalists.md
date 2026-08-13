---
id: event-crystal-ship-attacking-federation-loyalists
type: event
event_name: CRYSTAL_FED
sectors: [[[sector-hidden-crystal-worlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [combat-optional, crew-reward, federation]
---

# Crystal ship attacking Federation loyalists — `CRYSTAL_FED`

## Summary
A Crystalline border guard is running down a Federation ship. Intervening is an optional
fight with a guaranteed follow-up: whichever way you win, you get to contact the rescued
Federation ship, and one of the two follow-up outcomes hands you a **free crew member**.

## Trigger & Where It Appears
- Sector: [[sector-hidden-crystal-worlds]] only
- Pool: one of **10** entries in the `NEUTRAL_CRYSTAL` event list, allocated exactly **12**
  times per sector (`min=12 max=12`) ([[source-events-xml]], [[source-sector-data-xml]])
- `unique="false"` — it can recur in the same sector
- Beacon: shows **no ship** on Long-Range Scanners
  ([[source-fandom-crystal-ship-attacking-federation-loyalists]])

## Text
> There appears to be a fight going on nearby. A Crystalline border guard is chasing a
> small Federation ship!

(`event_CRYSTAL_FED_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Save the Federation ship. | — | `ship load="CRYSTAL_FED" hostile="true"` → fight a Crystal ship. On win, always continues to **Contact the Federation ship**. | 100% |
| 2 | Prepare to leave. | — | *"With the Federation ship distracting the guard, you are free to continue on your mission."* Nothing happens. | 100% |

### Winning the fight
The `CRYSTAL_FED` ship entry has **no surrender and no escape branch** — it is a fight to
the finish ([[source-events-xml]], per raw/gamedata/events_ships.xml;
[[source-fandom-crystal-ship-attacking-federation-loyalists]]):

| Win type | Reward |
|---|---|
| `destroyed` | `autoReward level="MED"` **standard** — medium scrap with resources |
| `deadCrew` | `autoReward level="HIGH"` **standard** — high scrap with resources |

Both then load `CRYSTAL_FED_LIST`.

### Sub-event: `CRYSTAL_FED_LIST` ("Contact the Federation ship")
Two entries ([[source-events-xml]]):

| Entry | Result |
|---|---|
| 1 | *"Thank you! We heard you jumped into an unknown sector…"* → `autoReward level="RANDOM"` **stuff**. |
| 2 | *"…only one person made it. They offer to join your crew as thanks."* → `crewMember amount="1"` (**a free crew member**, class unspecified) + `autoReward level="LOW"` **standard**. |

## Blue Options
- None.

## Rewards & Risks
- **Rewards:** medium-to-high scrap with resources for the kill, then either random stuff
  or a free crew member with low scrap. Killing the crew rather than destroying the hull
  upgrades MED → HIGH.
- **Risk:** the fight itself, with no surrender or escape available on either side.
  Declining costs nothing.

## Strategy Notes
- The crew member on `CRYSTAL_FED_LIST` entry 2 has no `class` attribute, so it is a
  random crew type rather than a guaranteed Human — worth noting against
  [[event-crystal-fight-with-surrender-offer-human-crew]], which specifies `class="human"`.
  ([[source-events-xml]])
- Boarding to clear the enemy crew rather than blowing the ship up is a straight reward
  upgrade here (HIGH vs MED). *(Opinion; the reward levels themselves are sourced.)*

## Related
- [[sector-hidden-crystal-worlds]]
- [[event-federation-deserters]] — the other Federation encounter in this sector, and the
  one where you can shoot *them*
- [[event-mantis-ship-attacking-crystal]], [[event-pirate-ship-attacking-crystal]],
  [[event-rebel-ship-attacking-crystal-ship]] — the same "intervene in someone else's
  fight" shape, but with the Crystal ship as the victim
- [[entity-crystal-men]], [[entity-federation]]

## Open Questions
- [ ] Whether the `crewMember` with no class can roll a Crystal crew member.
- [ ] The relative frequency of the two `CRYSTAL_FED_LIST` entries (the file lists them
      once each; no source gives odds).

## Sources
- [[source-events-xml]] (per raw/gamedata/events_crystal.xml, raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-crystal-ship-attacking-federation-loyalists]] (per raw/wiki/crystal-ship-attacking-federation-loyalists.md)
