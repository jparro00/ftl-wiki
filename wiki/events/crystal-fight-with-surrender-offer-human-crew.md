---
id: event-crystal-fight-with-surrender-offer-human-crew
type: event
event_name: CRYSTAL_HUNTER
sectors: [[[sector-hidden-crystal-worlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, combat, surrender, crew-reward, bug, no-choices]
---

# Crystal fight with surrender offer (Human crew) — `CRYSTAL_HUNTER`

## Summary
A forced fight against a Crystalline slaver hauling human captives. Its surrender branch
hands you a **free Human crew member** — and, because of a missing tag in the data files,
**does not actually end the fight**, so you can take the crew member *and* the kill
reward.

## Trigger & Where It Appears
- Sector: [[sector-hidden-crystal-worlds]] only
- Pool: one of **7** entries in the `HOSTILE_CRYSTAL` event list, allocated `min=6 max=10`
  per sector ([[source-events-xml]], [[source-sector-data-xml]])
- `unique="true"` — at most once per run ([[source-events-xml]])
- Beacon: shows a **ship** on Long-Range Scanners
  ([[source-fandom-crystal-fight-with-surrender-offer-human-crew]])

## Text
> Crystal shards fly past your ship as soon as you jump. You scan to find the assailant and
> discover a Crystalline ship carrying a number of humans in its cargo bay. It must be
> hunting the intruding ships!

(`event_CRYSTAL_HUNTER_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _none — the event has no choice nodes_ | — | `<ship load="CRYSTAL_HUNTER" hostile="true"/>` → immediate combat | 100% |

### Sub-outcome: they surrender
`<surrender chance="0.5" min="3" max="4">` — a **50%** chance of an offer once hull is low
([[source-events-xml]], per raw/gamedata/events_ships.xml; Fandom's footnote passes the
same 50, [[source-fandom-crystal-fight-with-surrender-offer-human-crew]]):

> The hunters message you, "We surrender. Take one of these squishy meat sacks that we've
> captured." He must be referring to the human captives.

| # | Choice | Outcome(s) |
|---|--------|-----------|
| 1 | Accept their surrender. | `crewMember amount="1" class="human"` → a **Human crew member**. **The fight continues** — the surrender event has no `<ship hostile="false"/>` tag. |
| 2 | Finish them off. | The fight continues. |

### Sub-outcome: you win
`destroyed` and `deadCrew` both give `autoReward level="MED"` **standard** — medium scrap
with resources ([[source-events-xml]]).

## Blue Options
- None.

## Rewards & Risks
- **Reward:** a free Human crew member (50% of fights, at low enemy hull) *plus* medium
  scrap with resources for finishing the kill.
- **Risk:** ordinary combat risk only. There is no downside branch.

## Strategy Notes
- Accepting the surrender is strictly free value: the Fandom page documents the missing
  tag explicitly — *"The surrender is lacking the usual tag to stop the fight in the
  datafiles, making it possible to receive a crewmember along with the rewards for
  defeating the ship."*
  ([[source-fandom-crystal-fight-with-surrender-offer-human-crew]]) — and the game file
  confirms it: the `<choice>` under `<surrender>` contains only a `<crewMember>` tag with
  no `<ship hostile="false"/>` ([[source-events-xml]]).
- This is one of two ways the sector can hand you crew for free; the other is the
  Crystal-crew branch of [[event-crystal-fight]].

## Related
- [[sector-hidden-crystal-worlds]]
- [[event-crystal-fight]] — `CRYSTAL_SHIP`, whose surrender can give Crystal crew
- [[event-crystal-fight-with-surrender-offer-hull-repairs]] — `CRYSTAL_CONVOY`
- [[entity-crystal-men]]
- [[concept-surrender-offers]]

## Open Questions
- [ ] Whether the bug is still present in the current 1.6.x build the user is playing (the
      raw file it was extracted from says yes; unconfirmed in play).
- [ ] Whether the surrender offer can fire more than once in the same fight.

## Sources
- [[source-events-xml]] (per raw/gamedata/events_crystal.xml, raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-crystal-fight-with-surrender-offer-human-crew]] (per raw/wiki/crystal-fight-with-surrender-offer-human-crew.md)
