---
id: event-rock-atheists
type: event
event_name: ROCK_ATHIEST
sectors: [[[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
beacon_type: hostile
hostile: false
blue_options: [[[item-sensors]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [rock, crew-reward, blue-option, unique, free-crew]
---

# Rock atheists — `ROCK_ATHIEST`

## Summary
One of the few reliable sources of a **free Rockman crew member**. A Rock dissident ship
wants out of Rock society; how you pitch yourself decides whether you gain a crew member,
get nothing, or start a fight. With Sensors level 2 the crew member is **guaranteed** —
which is the single best reason to keep Sensors upgraded in Rock space.

## Trigger & Where It Appears
- Sectors: [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]
- Event list: `NEUTRAL_ROCK`, allocated `min="7" max="8"` per Rock sector
  ([[source-sector-data-xml]])
- Beacon: ship present but **non-hostile on arrival** —
  `<ship load="ROCK_SHIP" hostile="false"/>` ([[source-events-rock]]);
  [[source-fandom-rock-atheists]] marks `LRSmap=ship`
- `unique="true"` — at most once per sector ([[source-events-rock]])

## Text
> You encounter a small craft with minimal propulsion; its Rock crew-member explains that
> the Rock home-world is run on lies and propaganda that keep the populace in check, and
> that they want no part of it.

(`event_ROCK_ATHIEST_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Tell them their god sent them here to join your crew. | — | The ship turns hostile (`<ship hostile="true"/>` on the already-loaded `ROCK_SHIP`). Fight, default rewards. Outcome prose varies over `textList ROCK_ATHIEST_BAD` (2 entries). | 100% fight |
| 2 | Promise to share with them the truths they've been denied. | — | Loads `eventList ROCK_ATHIEST_GOOD` — see below. | see below |
| 3 | **(Improved Sensors)** Show them to your data suite. | `req="sensors" lvl="2"` | *"The Rock captain is impressed by the data you've collected and agrees to stay with you until they find their footing in the galaxy."* → `<crewMember amount="1" class="rock"/>` | 100% |

### Choice 2 — `ROCK_ATHIEST_GOOD`
The event list has **three** entries ([[source-events-rock]]):

| Entry | Text | Effect |
|---|---|---|
| 1 | *"Your promises gain their attention and they agree to serve with you, for a while."* | `<crewMember amount="1" class="rock"/>` |
| 2 | *"They seem tempted by your offer, but decide they can't risk being lied to again. They close frequencies and jump away."* | nothing |
| 3 | **identical text id to entry 2** (`event_ROCK_ATHIEST_GOOD_2_text`) | nothing |

So the "nothing" outcome occupies 2 of 3 slots and the crew member 1 of 3. Assuming FTL
picks uniformly among `eventList` entries — which is what the duplicated entry is *for* —
that is **1/3 crew, 2/3 nothing**. [[source-fandom-rock-atheists]] independently tags the
refusal outcome `{{DuplicateEvent|2}}`, i.e. it occupies two slots, so both sources agree
on the weighting even though neither prints a percentage.

## Blue Options
- **Sensors, level 2+** (`req="sensors" lvl="2"`) — converts a 1-in-3 gamble into a
  guaranteed free Rockman. Note the gate is the *system level*, not merely owning Sensors:
  level 1 is not enough ([[source-events-rock]]; [[source-fandom-rock-atheists]] renders it
  as `level=2+`).

## Rewards & Risks
- Best case: a free [[item-rock-crew]] — no scrap cost, no fight.
- Choice 1 is a strictly worse version of an ordinary [[event-rock-fight]]: you give up
  the crew member and get default rewards you could have had elsewhere. The surrender
  branch on `ROCK_SHIP` still applies.
- Choice 2 risks nothing but wastes the beacon two times in three.

## Strategy Notes
- **Take choice 3 if you have it, otherwise choice 2.** Choice 1 has no upside that choice
  2 does not also offer, since choice 2's failure state is "nothing happens" rather than
  "you lose the fight option" — the ship is already there and choice 1 only exists to
  start the fight. *(Opinion; derived from the outcome table, not stated by a source.)*
- A Rockman crew member is disproportionately valuable in Rock space itself — they unlock
  the blue option on [[event-mantis-ship-with-rock-body-parts]] and are fire-immune, which
  matters at every sun beacon in the sector.

## Related
- [[event-mantis-ship-with-rock-body-parts]] — the other Rock-crew blue option in this sector
- [[event-rock-fight]] — the fight choice 1 starts
- [[item-sensors]] — the gating system
- [[item-rock-crew]], [[entity-rock-men]]

## Open Questions
- [ ] Confirm that `eventList` selection is uniform (the 1/3 figure depends on it).
- [ ] Does the free Rockman carry a generated name, or a fixed one? The XML sets no `id`,
      unlike Ariadne in [[event-rock-bride]].

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-rock-atheists]] (per raw/wiki/rock-atheists.md)
