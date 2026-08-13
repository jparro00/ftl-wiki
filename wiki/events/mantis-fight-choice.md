---
id: event-mantis-fight-choice
type: event
event_name: MANTIS_FIGHT_CHOICE
sectors: [[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]]
beacon_type: any
hostile: false
blue_options: [[[item-cloaking]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [mantis, blue-option, cloaking, optional-fight, default-rewards]
---

# Mantis fight choice — `MANTIS_FIGHT_CHOICE`

## Summary
You spot a Mantis warship before it spots you. Attack, try to hide, or — with
[[item-cloaking]] — cloak. Hiding is a coin-flip that mostly fails; cloaking is the same
gamble with the odds inverted. The fight, if it happens, is the standard `MANTIS_FIGHT`
ship with default rewards, so the entire value of this beacon is the chance to skip it.

## Trigger & Where It Appears
- Sectors: [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]
- Drawn from the `NEUTRAL_ENGI` and `NEUTRAL_MANTIS` lists; Mantis sectors allocate
  `NEUTRAL_MANTIS` at `min=6 max=7` beacons
  ([[source-events-xml]], [[source-sector-data-xml]])
- `unique="false"` — repeats freely
- The event stages the enemy as `<ship load="MANTIS_FIGHT" hostile="false"/>` — the ship
  is there but passive until you act. Long-range scanners show a ship
  ([[source-fandom-mantis-fight-choice]]).

## Text
Drawn from the `MANTIS_FIGHT_CHOICE` text list and **varies** across six strings
([[source-events-xml]], [[source-text-events-xml]]):

> You're greeted by a rare sight: a Mantis ship that appears not to have noticed you.

> For once, you see the Mantis before they see you.

> When they see the Mantis warship waiting in ambush at your intended coordinates, your
> crew is relieved to note you've jumped someway off the mark.

> You overhear Mantis comm chatter: "Negative, I have killed more humans!" You gulp
> noticeably, but luckily they don't see you yet.

> You overhear Mantis comm chatter: "The one on the right is starting to rot. Take him
> down. Take off his fingers. Put him out of the airlock." They certainly don't seem to
> be friendly...

> You overhear Mantis comm chatter: "Agreed. Next ship is your turn. Good hunting." They
> don't see you yet.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack the ship. | — | The staged ship becomes hostile. Fight a Mantis ship, **default rewards**. | 100% |
| 2 | Attempt to remain concealed. | — | One of three `MANTIS_FIGHT_CHOICE_AVOID` entries: **1 escapes clean, 2 lead to the fight**. | unknown (2 of 3 entries are a fight) |
| 3 | **(Cloaking)** Cloak to stay hidden. | `req="cloaking" lvl="1"` | One of three `MANTIS_FIGHT_CHOICE_CLOAK` entries: **2 escape clean, 1 leads to the fight**. | unknown (1 of 3 entries is a fight) |

The game files state **no percentages** for either list — only the entry counts above
([[source-events-xml]]). Fandom marks the same split with its `DuplicateEvent|2` tag on
the two-entry branches ([[source-fandom-mantis-fight-choice]]), which agrees with the
file but likewise gives no numbers.

### Choice 2 — `MANTIS_FIGHT_CHOICE_AVOID`
- *(escape)* > You power down non-essential systems and wait for the FTL drive to charge.
  They either don't want to fight or have failed to notice your ship, the latter being
  more likely.
- *(fight)* > Before you have a chance to slink away the Mantis ship notices you and
  powers up their weapons.
- *(fight)* > You power down non-essential systems in an attempt to remain unnoticed. It
  looks like they are about to leave when suddenly they turn and set course toward you,
  weapons powered.

### Choice 3 — `MANTIS_FIGHT_CHOICE_CLOAK`
- *(escape)* > You quickly cloak the ship and move out of immediate scanning range. You
  appear to have gotten away undetected.
- *(escape)* > You cloak and shut down non-essential systems. In a short time the Mantis
  ship jumps away, no doubt in search of prey.
- *(fight)* > You quickly cloak the ship, but not quickly enough. They spot you and move
  in to engage.

## Blue Options
- **[[item-cloaking]]** (`req="cloaking" lvl="1"`) — needs the Cloaking system installed
  at level 1 or above; no crew species required. It does not guarantee escape, it flips
  the list composition: the plain hide attempt has two fight entries out of three, the
  cloaked one has one out of three. Cloaking is the only gate on this event.

## Rewards & Risks
- There is **no reward for avoiding**. Choices 2 and 3 pay nothing when they succeed —
  you simply skip the beacon.
- Fighting pays default combat rewards, the same as [[event-mantis-fight]].
- Risk on choices 2 and 3 is that you end up in the fight anyway, having gained nothing
  by trying to duck it.

## Strategy Notes
- *(Opinion.)* Because avoiding pays nothing, a healthy ship should generally just take
  choice 1 — the fight is coming two times in three anyway on choice 2, and the scrap is
  the point of the sector.
- *(Opinion.)* Choices 2 and 3 are for a damaged ship, a dead system, or a run that is
  ahead on scrap and behind on hull. Cloaking is the only thing that makes ducking
  reliable-ish.
- The Cloaking requirement is `lvl="1"`, i.e. simply having the system — no upgrade
  investment is needed to unlock the option.

## Related
- [[event-mantis-fight]] — the same ship, no choice offered
- [[event-mantis-ship-attacking-civilian]] — the other optional Mantis fight from the same lists
- [[item-cloaking]]
- [[entity-mantis]]
- [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]],
  [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]

## Open Questions
- [ ] Are the three entries in each list drawn uniformly? No `prop` weights exist in the file.
- [ ] Does choice 2 or 3 failing give the enemy any opening advantage in the fight, or is
      it identical to choice 1?

## Sources
- [[source-events-xml]] (per raw/gamedata/events_mantis.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-mantis-fight-choice]] (per raw/wiki/mantis-fight-choice.md)
