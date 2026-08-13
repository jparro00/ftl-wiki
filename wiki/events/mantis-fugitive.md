---
id: event-mantis-fugitive
type: event
event_name: ALISON_MANTIS_CREW
sectors: [[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [mantis, engi, unique, crew-reward-chance, boarding-risk, hull-damage-hazard, fire-risk, moral-choice]
---

# Mantis fugitive — `ALISON_MANTIS_CREW`

## Summary
A Mantis deserter teleports aboard while the Engi warship that was hunting him offers you a
bounty. There is **no safe exit** — every one of the five outcomes ends in a fight or costs
you hull. Side with him for a coin-flip at a free Mantis crewmember; sell him for guaranteed
`HIGH` scrap two-thirds of the time and a trap the last third. `unique="true"`.

## Trigger & Where It Appears
- Sectors: [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]
- Event lists: `NEUTRAL_ENGI` ([[source-events-engi]]) and `NEUTRAL_MANTIS`
  ([[source-events-mantis]])
- Allocation: `NEUTRAL_ENGI` `min=4 max=6` in `ENGI_SECTOR` and `min=5 max=7` in
  `ENGI_HOME`; `NEUTRAL_MANTIS` `min=6 max=7` in both Mantis sectors
  ([[source-sector-data-xml]])
- Beacon: a neutral beacon; the fight starts only once you choose
- Long-range scanners show **no ship** ([[source-fandom-mantis-fugitive]], `LRSmap=noship`)
- `unique="true"` — once per run ([[source-events-xml]])

## Text
> You arrive just in time to see an unusually well-armed Engi ship destroying a small pirate
> craft. A teleporter signal is detected...intruder on deck!

Continuing:

> A young Mantis in a charred uniform has teleported onto the deck. He begs for sanctuary
> from the Engi, and offers to serve in exchange for your protection. The Engi have already
> traced the teleporter signal and are offering a deal in exchange for the prisoner.

(`event_ALISON_MANTIS_CREW_text`, `event_ALISON_MANTIS_CREW_c1_text`, per
[[source-text-events-xml]])

## Choices & Outcomes

A forced *Continue…* precedes the real pair of choices.

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Side with the fugitive and fight the Engi ship. | — | Rolls `ALISON_MANTIS_CREW_HELP` (2 entries) | see below |
| 2 | Agree to offer up the Mantis in exchange for a bounty. | — | Rolls `ALISON_MANTIS_CREW_REJECT` (3 entries) | see below |

### Choice 1 → `ALISON_MANTIS_CREW_HELP`

| Entry | Outcome | Share |
|---|---|---|
| 1 | *"It was a trap! The Mantis sabotages your ship before teleporting away."* → `damage 3` + `damage 1 random system` (AE only) + `damage 1 room` + fight `ENGI_MANTIS_CONTROLLED` | 1/2 |
| 2 | *"He expresses his thanks and prepares to help you fight his pursuer."* → `crewMember 1 mantis` + fight `ENGI_SHIP` | 1/2 |

### Choice 2 → `ALISON_MANTIS_CREW_REJECT`

| Entry | Outcome | Share |
|---|---|---|
| 1 | *"The Engi captain is delighted…"* → `autoReward level="HIGH"` `scrap_only`, no fight | 1/3 |
| 2 | *"Fury sparks in the eyes of the Mantis…"* → `autoReward HIGH scrap_only` + `damage 4` (AE only) + `damage 1 room effect="fire"`, no fight | 1/3 |
| 3 | *"…It was a trap!"* → `boarders 1 mantis` + fight `ENGI_MANTIS_CONTROLLED` | 1/3 |

Both splits are derived from the number of `<event>` entries in each `<eventList>` and
**assume uniform selection across list entries** ([[source-events-xml]]).

### The enemy ships
- `ENGI_SHIP` — `auto_blueprint="SHIPS_CIRCLE"`, `destroyed`/`deadCrew` load the shared
  defaults. **No `<surrender>` and no `<escape>`** ([[source-events-ships]]).
- `ENGI_MANTIS_CONTROLLED` — same blueprint pool and same defaults, but with an explicit
  `<crew><crewMember type="mantis" prop="1"/></crew>` block: the Engi hull is crewed by
  Mantis ([[source-events-ships]]). Also no surrender or escape.

Both pay the game's default fight rewards via `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT`.

## Blue Options
None. No `req` appears anywhere in this event — notable, given how many species are in the
room.

## Rewards & Risks
- **Best case:** a free Mantis crewmember (choice 1, 1/2), or `HIGH` `scrap_only` with no
  fight at all (choice 2, 2/3).
- **Worst case (choice 1):** 5 hull, a random system down, a damaged room *and* a crewed
  Mantis-Engi warship to fight.
- **Worst case (choice 2):** a Mantis boarder loose inside your ship plus the same warship.
- Choice 2 is the only path that can end with **no combat at all** — 2 of its 3 entries
  simply pay and let you jump.

## Version Differences
Base-`events.xml` event, present in both editions, with two `<!--DLC-->`-marked tags that
are Advanced Edition only ([[source-events-xml]]):

- `HELP` entry 1: `<damage amount="1" system="random"/>` — vanilla deals 4 hull and a
  damaged room, AE deals 5 hull plus a knocked-out system.
- `REJECT` entry 2: `<damage amount="4"/>` **carries the DLC marker itself**, so on a
  literal reading vanilla dealt only the 1 hull of the room fire and AE added 4 more.

That second one is unusual — elsewhere in this file the DLC marker sits on *added system*
damage, not on a plain hull tag. Recorded as read; see Open Questions.

## Related
- [[event-rebel-defector]] — the sister event: a defector aboard, pick a side (`ALISON_DEFECTOR`)
- [[event-engi-fight]] — the `ENGI_SHIP` fight without the fugitive
- [[event-confused-mantis]] — the other Mantis-in-Engi-space event in `NEUTRAL_ENGI`
- [[entity-mantis]], [[entity-engi]]
- [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]

## Open Questions
- [ ] Is `<damage amount="4"/>` in `ALISON_MANTIS_CREW_REJECT` entry 2 really AE-added, or
      is the `<!--DLC-->` comment mis-placed and meant for the following fire tag?
- [ ] Numeric value of `HIGH scrap_only` at a given sector depth.
- [ ] Are `<eventList>` entries selected uniformly? The 1/2 and 1/3 figures assume it.
- [ ] What `SHIPS_CIRCLE` rolls at each sector depth — the Engi hull can be anything from
      trivial to a shielded gunship.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-events-engi]] (per `raw/gamedata/events_engi.xml` — `NEUTRAL_ENGI`)
- [[source-events-mantis]] (per `raw/gamedata/events_mantis.xml` — `NEUTRAL_MANTIS`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-mantis-fugitive]] (per `raw/wiki/mantis-fugitive.md`)
