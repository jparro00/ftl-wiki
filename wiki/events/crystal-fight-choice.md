---
id: event-crystal-fight-choice
type: event
event_name: CRYSTAL_REBEL_CRYSTAL2
sectors: [[[sector-hidden-crystal-worlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, combat-optional, trap, rebel]
---

# Crystal fight choice — `CRYSTAL_REBEL_CRYSTAL2`

## Summary
A bait event. It looks like [[event-rebel-ship-attacking-crystal-ship]] — a Rebel firing
on a Crystalline vessel, and an obvious "help the victim" option — but the Crystals win
the exchange before you arrive and then turn on you for having brought the aliens in the
first place. Helping is strictly a trap; leaving costs nothing.

## Trigger & Where It Appears
- Sector: [[sector-hidden-crystal-worlds]] only
- Pool: one of **10** entries in the `NEUTRAL_CRYSTAL` event list, allocated exactly **12**
  times per sector (`min=12 max=12`) ([[source-events-xml]], [[source-sector-data-xml]])
- `unique="true"` — at most once per run
- Beacon: shows **no ship** on Long-Range Scanners
  ([[source-fandom-crystal-fight-choice]])

## Text
> You're greeted by an unwelcome sight - a Rebel advance ship is laying down fire on a
> Crystalline vessel in the distance.

(`event_CRYSTAL_REBEL_CRYSTAL2_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Engage the Rebel ship. | — | *"Before you can engage, the Crystalline ship scores a direct hit and obliterates the Rebel ship! They hail: 'You, you are like these other aliens! You brought them here!'"* → `ship load="CRYSTAL_SHIP_NO_SURRENDER" hostile="true"` — a Crystal warship fight with **no surrender and no escape**, **default rewards**. | 100% |
| 2 | Leave them alone. | — | *"It's best to take advantage of the rare occasions when the Rebels aren't shooting at you."* Nothing happens. | 100% |

There is no branch in which you get to fight the Rebel, and no `CRYSTAL_SAVED` follow-up —
unlike the three intervention events it resembles.
([[source-events-xml]], [[source-fandom-crystal-fight-choice]])

## Blue Options
- None. No `req` anywhere in the event — Crystal crew does not defuse it.

## Rewards & Risks
- **Reward:** default rewards only, and only by winning a fight you did not need to take.
- **Risk:** `CRYSTAL_SHIP_NO_SURRENDER` cannot surrender and cannot flee
  ([[source-events-xml]], per raw/gamedata/events_ships.xml), so choice 1 commits you to a
  full-length warship fight.
- Choice 2 has no cost at all.

## Strategy Notes
- Take choice 2 unless you specifically want the fight. This is the one event in the sector
  where the "good deed" option has **no** upside path — every comparable event
  ([[event-mantis-ship-attacking-crystal]], [[event-pirate-ship-attacking-crystal]],
  [[event-rebel-ship-attacking-crystal-ship]]) at least routes into `CRYSTAL_SAVED`.
  *(Opinion, built on the structural comparison above.)*
- Because it is `unique="true"`, springing it once removes it from the pool for the rest of
  the run.

## Related
- [[event-rebel-ship-attacking-crystal-ship]] — `CRYSTAL_REBEL_CRYSTAL`, the near-identical
  premise that *does* let you help
- [[event-crystalline-research-facility]] — the sector's other `CRYSTAL_SHIP_NO_SURRENDER`
  ambush
- [[sector-hidden-crystal-worlds]]
- [[entity-crystal-men]], [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] What "default rewards" resolves to for `CRYSTAL_SHIP_NO_SURRENDER`.
- [ ] Whether the two similarly-named events were meant as a pair or whether
      `CRYSTAL_REBEL_CRYSTAL2` is a later addition (the file gives no comment either way).

## Sources
- [[source-events-xml]] (per raw/gamedata/events_crystal.xml, raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-crystal-fight-choice]] (per raw/wiki/crystal-fight-choice.md)
