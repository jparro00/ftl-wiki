---
id: event-nebula-lost-ship
type: event
event_name: NEBULA_LOST_SHIP
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: nebula
hostile: false
blue_options: [[[item-teleporter]], [[item-long-ranged-scanners]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [nebula, crew-reward, blue-option, teleporter, long-ranged-scanners, unique]
---

# Nebula lost ship — `NEBULA_LOST_SHIP`

## Summary
A free-crew event with a fight attached to the free option. Federation survivors vanish
into the clouds; searching blind is a three-way roll that includes a Rebel ambush, while
either blue option removes the ambush entirely. This is one of the better reasons to carry
Long-Ranged Scanners into nebula space.

## Trigger & Where It Appears
- Beacon: nebula (`<environment type="nebula"/>`). No ship present on arrival.
- `unique="true"` — once per run.
- The widest sector reach in the nebula file: lists `NEBULA`, `NEBULA_NEUTRAL`,
  `NEBULA_NEUTRAL_SLUG`, `NEBULA_PIRATE`, `NEBULA_REBEL` ([[source-newevents]],
  [[source-events-nebula]], [[source-events-slug]], [[source-events-pirate]],
  [[source-events-rebel]]). `NEBULA_PIRATE` lists it **twice**, doubling its weight in
  [[sector-pirate-controlled-sector]].
- Long-range scanners show no ship ([[source-fandom-nebula-lost-ship]]).

## Text
> A heavily damaged Federation ship is hiding in the nebula at this beacon. Before you
> have time to make contact with them, they fade into the nebula.

(`event_NEBULA_LOST_SHIP_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attempt to follow and help them. | — | `NEBULA_LOST_SHIP_LIST`, three entries — **(a)** *"Your search is hopeless…"* → nothing; **(b)** *"…you stumble upon the Rebel ship which the Federation loyalists were likely hiding from."* → fight a `REBEL` ship, default rewards; **(c)** *"You get lucky and find them floating not too deep into the nebula."* → **+1 crew**. | unknown (3-entry list) |
| 2 | Keep your position, they can handle themselves. | — | Empty `<event/>` — nothing happens. | 100% |
| 3 | **(Teleporter)** Lock onto their life-signs with your teleporter. | `req="teleporter"` | *"You beam the Federation crew aboard. One gladly joins your crew, the rest wait to be dropped off at the next station."* → **+1 crew** and `autoReward level="MED"` / `scrap_only`. | 100% |
| 4 | **(Long-ranged Scanner)** Pump extra power into your sensors and try to track them. | `req="ADV_SCANNERS"` | `NEBULA_LOST_SHIP_LIST2`, two entries — **(a)** *"…an empty hull, long since stripped of functioning components."* → `autoReward level="MED"` / `scrap_only`; **(b)** *"You follow the faint signatures and find them floating not too far away…"* → **+1 crew**. | unknown (2-entry list) |

Choices 1, 3 and 4 are all `hidden="true"`; choice 2 is not ([[source-events-nebula]]).

## Blue Options
- **[[item-teleporter]]** (`req="teleporter"`) — strictly the best outcome available:
  guaranteed crew member **and** medium scrap, with no fight risk. Any level of the
  Teleporter system satisfies it; the XML sets no `lvl`.
- **[[item-long-ranged-scanners]]** (`req="ADV_SCANNERS"`) — the augment, not a system.
  Removes the Rebel-ambush branch and guarantees one of two good outcomes: crew, or medium
  scrap.

Neither blue option can produce nothing, which is what makes them meaningfully better than
choice 1 rather than merely more likely to succeed.

## Rewards & Risks
- Best case: crew + `MED` / `scrap_only` (Teleporter).
- Choice 1's downside is not "nothing" but a **Rebel fight you did not choose**. The
  `REBEL` ship definition has `<surrender chance="0.5" min="2" max="3">` and
  `<escape chance="0.5" min="3" max="4">`, both loading the generic pirate tables, with
  `DESTROYED_DEFAULT` (`MED` / `standard`) on a kill ([[source-events-ships]],
  [[source-events-xml]]).
- No hull damage or crew loss on any branch.

## Strategy Notes
- With either blue option this is a free good outcome; take it without thinking.
- Without one, choice 1 is a 3-way roll where one branch is a fight in a nebula (sensors
  down). If your ship is healthy the expected value still favours searching — a crew member
  is worth more than most beacons — but "keep your position" is a defensible skip on a
  damaged run. *(Opinion; no source states a recommendation.)*
- Fandom categorises this under `Crew reward opportunity`
  ([[source-fandom-nebula-lost-ship]]).

## Related
- [[event-plasma-storm-incapacitated-ships]] — the other nebula-file crew source, with a
  crew-*loss* branch attached
- [[event-rebel-fight-in-nebula]], [[event-rebel-fight-choice-in-nebula]] — the same
  `REBEL` ship
- [[item-teleporter]], [[item-long-ranged-scanners]], [[concept-rebel-fleet-advance]]
- [[sector-uncharted-nebula]], [[sector-slug-home-nebula]]

## Open Questions
- [ ] Weights within `NEBULA_LOST_SHIP_LIST` (3 entries) and `NEBULA_LOST_SHIP_LIST2`
      (2 entries) — the XML states none.
- [ ] Which species the granted crew member is (the `<crewMember amount="1"/>` element
      names no race).
- [ ] Numeric values behind `autoReward level="MED">scrap_only`.

## Sources
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-nebula-lost-ship]] (per raw/wiki/nebula-lost-ship.md)
