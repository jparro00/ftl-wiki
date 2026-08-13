---
id: event-zoltan-ship-asks-to-dock
type: event
event_name: ZOLTAN_SCIENCE_DOCK
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [crew-reward, surrender, fight-risk, unique, zoltan]
---

# Zoltan ship asks to dock — `ZOLTAN_SCIENCE_DOCK`

## Summary
A Zoltan science ship asks to come alongside. Docking is a coin flip: half the time they
hand you a medium supply drop, half the time they open fire. The fight is worth taking —
the ship has a 50% surrender offer that ends the fight *and* gives you a **free Zoltan
crew member**, and the Fandom page notes the surrender cannot be refused.

## Trigger & Where It Appears
- Event list: `NEUTRAL_ZOLTAN` in `events_zoltan.xml`, an un-annotated base entry with no
  Advanced Edition override list ([[source-events-zoltan]]).
- `NEUTRAL_ZOLTAN` is allocated at `min=5 max=6` in both `ZOLTAN_SECTOR`
  ([[sector-zoltan-controlled-sector]]) and `ZOLTAN_HOME`
  ([[sector-zoltan-homeworlds]]) ([[source-sector-data-xml]]) — so five or six beacons per
  Zoltan sector draw from the pool this event sits in.
- `unique="true"` — at most once per run.
- Beacon: ordinary; no distress flag, no environment, and Fandom marks it `LRSmap=noship`
  — **no ship shows on Long-Ranged Scanners** even though the docking branch can start a
  fight ([[source-fandom-zoltan-ship-asks-to-dock]]).

## Text
> What appears to be a Zoltan science ship requests permission to dock.

(`event_ZOLTAN_SCIENCE_DOCK_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Dock with them. | — (`hidden="true"`) | Loads `ZOLTAN_SCIENCE_DOCK_LIST` — two entries, below. | — |
| 2 | Have them keep their distance. | — (`hidden="true"`) | *"They leave without a word."* → nothing happens. | 100% |

### `ZOLTAN_SCIENCE_DOCK_LIST` — two entries, no repeats (1/2 each)
**Assuming uniform selection across list entries** ([[concept-event-list-weighting]]):

| Odds | Text | Effect |
|---|---|---|
| 1/2 | *You allow them to approach, but are caught unaware when they open fire!* | `<ship load="ZOLTAN_SCIENCE_DOCK" hostile="true"/>` — the fight below. |
| 1/2 | *"We have been studying the relationships between the species and have determined that the 'Federation' still has potential to be a net positive for the galaxy. Please accept this gift to aid your journey."* | `<autoReward level="MED">stuff</autoReward>` |

### The `ZOLTAN_SCIENCE_DOCK` ship
`auto_blueprint="SHIPS_ZOLTAN"` — a standard Zoltan hull, but with a **custom surrender
block rather than default rewards** ([[source-events-ships]]):

| Ending | Trigger | Result |
|---|---|---|
| **Surrender** | `chance="0.5"` `min="3" max="4"` → **50% surrender chance** ([[concept-surrender-offers]]) | *"The Zoltan captain sends an urgent hail: 'Wait, this was all a test! A test that you passed! A diverse crew, working together, surely a sight to warm the heart of any dispassionate observer. Come, I shall join your crew!'"* → `<ship hostile="false"/>`, **`<crewMember amount="1" class="energy"/>` — a free Zoltan crew member** — and `<autoReward level="LOW">standard</autoReward>`. |
| Destroyed | — | *"While you search the debris, you wonder what it was that could have provoked them to act so irrationally."* → `<autoReward level="LOW">standard</autoReward>` |
| Dead crew | — | *"While you scrap their ship, you wonder what it was that could have provoked them to act so irrationally."* → `<autoReward level="MED">standard</autoReward>` |

**No `<escape>` block is declared** — the ship cannot flee. Fandom reaches the same
conclusion, flagging it as needing confirmation
([[source-fandom-zoltan-ship-asks-to-dock]]).

Fandom adds one behavioural note the files do not encode: *"If surrender is triggered, the
fight is over: there is no option or prompt to decline the surrender to continue the
fight."* The XML supports this — the `<surrender>` block contains no `<choice>` elements,
unlike e.g. [[event-slug-surrender]], so there is nothing for the engine to offer.

## Blue Options
None. No `req` attribute appears on any choice or on the ship's branches — notably, Zoltan
crew do **not** unlock anything here.

## Rewards & Risks
- 1/2: `MED` `stuff` for free — resources with some scrap, no fight.
- 1/2: a Zoltan-hull fight you did not choose. Winning pays `LOW` (destroyed) or `MED`
  (dead crew) `standard`; a 50% surrender pays `LOW` `standard` **plus a Zoltan crew
  member**.
- Risk: a Zoltan hull means a Zoltan Super Shield to chew through, and the ship cannot
  escape, so the fight runs to a conclusion once started. Boarding it is attractive
  because the dead-crew ending pays `MED` rather than `LOW`.
- Declining is completely free.

## Strategy Notes
- *Opinion:* dock. Every branch is positive — the worst outcome is a fight against a
  standard Zoltan hull with default-ish rewards, and the best is a free crew member.
  There is no branch that damages you outright.
- The reward asymmetry is worth remembering: **killing the crew pays `MED`, destroying the
  hull pays `LOW`.** With a teleporter or a Boarding Drone, board it.
- The surrender is the only free Zoltan crew member in the Zoltan sectors that does not
  cost scrap. Since the surrender is un-declinable, you cannot fight on for the destroyed
  reward once it triggers — but you would not want to.

## Related
- [[event-zoltan-trade-hub]], [[event-zoltan-wise-man]] — the other Zoltan events in the
  `NEUTRAL_ZOLTAN` pool that can turn into a fight
- [[event-zoltan-fight]] — the plain Zoltan hostile encounter
- [[concept-surrender-offers]] — how the 50% is derived from `chance="0.5"`
- [[concept-event-list-weighting]] — basis for the 1/2 split

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] Confirm the ship really never attempts to escape (Fandom flags this as unverified).
- [ ] Does the granted Zoltan arrive with any skill training, or at zero?

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-zoltan-ship-asks-to-dock]] (per raw/wiki/zoltan-ship-asks-to-dock.md)
