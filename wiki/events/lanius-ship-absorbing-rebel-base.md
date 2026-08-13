---
id: event-lanius-ship-absorbing-rebel-base
type: event
event_name: LANIUS_GROUP_AUTO
sectors: [[[sector-abandoned-sector]]]
beacon_type: any
hostile: false
blue_options: [lanius crew]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [lanius, fleet-delay, blue-option, optional-fight, unique, advanced-edition]
---

# Lanius ship absorbing rebel base — `LANIUS_GROUP_AUTO`

## Summary
A swarm of Lanius ships is dismantling a forward Rebel base. You can try to point them at
the Rebel fleet — a three-way gamble between a paid fleet delay, a fight, and nothing at
all — or, with a Lanius crew member, simply get the good outcome. One of the cleanest
blue options in the sector: it converts a 1-in-3 gamble into a guarantee.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] only.
- List: `NEUTRAL_LANIUS`, allocated `min=5 max=6` beacons per sector
  ([[source-sector-data-xml]]); thirteen members → **1/13** *assuming uniform selection
  across list entries* ([[source-dlcevents-anaerobic]]).
- `unique="true"` — at most once per sector.
- No ship is spawned by the event body; the enemy only exists inside one branch of the
  gamble. Long-range scanners show **no** ship
  ([[source-fandom-lanius-ship-absorbing-rebel-base]]).

> **AE-only.** The file, the sector, and the `req="anaerobic"` blue option all require
> Advanced Edition.

## Text
> You notice a number of Lanius ships absorbing a forward Rebel base and its automated
> scouts. They don't seem to be aggressive. Perhaps their desire for metal could prove to
> be useful?

(`event_LANIUS_GROUP_AUTO_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Try to use them to delay the Rebels. | — | Loads `LANIUS_GROUP_AUTO_LIST` (three members): (a) they aren't interested → nothing; (b) they scoff and one ship attacks → combat with `LANIUS_SHIP`; (c) they take the tip → `MED standard` + `<modifyPursuit amount="-1"/>` (**Rebel fleet delayed 1 turn**). | **1/3** each *(assuming uniform selection across list entries)* |
| 2 | Leave them alone. | — | *"You decide it would be better to leave them be."* → nothing happens. | 100% |
| 3 | **(Lanius Crew)** Try to use them to delay the Rebels. | `req="anaerobic"` | *"Your crewmember tells them of the approaching fleet…"* → `MED standard` + **Rebel fleet delayed 1 turn**, guaranteed. | 100% |

## Blue Options
- **Lanius crew member** (`req="anaerobic"`) — turns choice 1's 1/3 chance at the good
  outcome into a certainty and removes the 1/3 fight risk entirely. Same payload as the
  best branch: medium scrap-with-resources plus one turn of fleet delay
  ([[source-dlcevents-anaerobic]], [[source-fandom-lanius-ship-absorbing-rebel-base]]).

## Rewards & Risks
- Best case (either route): `MED standard` **and** one turn of Rebel fleet delay — the
  fleet-delay effect is the scarcer resource of the two.
- Worst case on choice 1: a `LANIUS_SHIP` fight you did not need to take (tables on
  [[event-lanius-fight]]) — that ship *can* surrender or escape, unlike most enemies in
  this sector.
- Choice 2 is a clean, free exit.

## Strategy Notes
- With a Lanius aboard this is free value; take choice 3 every time.
- Without one, choice 1 is a genuine gamble: a third of the time you get paid and buy a
  turn, a third you get nothing, a third you get a fight. Whether that is worth it depends
  almost entirely on your hull — the downside is a full warship engagement, not a scratch.
- This is one of only two events in the batch that can delay the Rebel fleet; the other is
  [[event-lanius-ship-absorbing-automated-scout]].

## Related
- [[event-lanius-ship-absorbing-automated-scout]] — the other Lanius-eats-Rebel-hardware
  event, also with a fleet-delay outcome
- [[event-lanius-fight]] — the enemy in the bad branch, and its reward tables
- [[entity-lanius]], [[entity-rebels]], [[sector-abandoned-sector]]

## Open Questions
- [ ] Numeric values behind `MED standard`.
- [ ] Whether the three `LANIUS_GROUP_AUTO_LIST` entries are genuinely equally weighted.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-lanius-ship-absorbing-rebel-base]] (per raw/wiki/lanius-ship-absorbing-rebel-base.md)
