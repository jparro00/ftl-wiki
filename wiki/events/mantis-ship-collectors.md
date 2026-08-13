---
id: event-mantis-ship-collectors
type: event
event_name: DONOR_MANTIS_CHASE
sectors: [[[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [mantis, unique, donor-event, combat, ship-escape, quest-marker, surrender, weapon-reward-chance]
---

# Mantis ship-collectors — `DONOR_MANTIS_CHASE`

## Summary
A no-choice Mantis ambush that turns into a two-part chase. The first ship always tries to
run at low hull; if it gets away it drops a quest marker, and following it leads to a
bigger, better-armed rematch that pays a guaranteed weapon. Letting the fight resolve
normally is the *worse* outcome — the escape is the branch with the money in it.

## Trigger & Where It Appears
- Sectors: [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]
- Pooled in the base `HOSTILE_MANTIS` list (`events_mantis.xml`) and in its Advanced
  Edition replacement `OVERRIDE_HOSTILE_MANTIS` (`dlcEventsOverwrite.xml`) — a
  hostile-beacon allocation in **both editions**, with the AE list adding four further
  entries around it ([[source-events-mantis]], [[source-dlceventsoverwrite]]).
- `unique="true"` — at most once per run ([[source-events-xml]]).
- Long-Range Scanners show a ship at the beacon ([[source-fandom-mantis-ship-collectors]]).
- The event has **no choices**: combat starts immediately on arrival.

## Text
> You are immediately hailed by an impressive looking Mantis ship, "Your ship would make a
> mighty fine prize. Prepare for battle!"

(`event_DONOR_MANTIS_CHASE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — `<ship load="DONOR_MANTIS_CHASE1" hostile="true"/>` fires on arrival)_ | — | Fight `DONOR_MANTIS_CHASE1`, a Mantis Fighter (`auto_blueprint="MANTIS_FIGHTER"`) crewed entirely by Mantis. | 100% |

### Fighting `DONOR_MANTIS_CHASE1`

Defined inline in `events.xml`, not in `events_ships.xml` ([[source-events-xml]]):

| Ship result | Raw tag | Outcome |
|---|---|---|
| Escape | `<escape timer="5" min="5" max="5">` | *"You pick up more chatter from the enemy ship, 'You know what... Forget this. Prepare for retreat!'"* — no `chance` attribute, so it is not a roll. |
| Got away | `<gotaway>` | *"The ship made an emergency FTL jump, but it looks like they didn't mask their signatures."* → two choices, below. |
| Destroyed | `<destroyed>` | `autoReward level="MED"` type `standard` — **medium scrap with resources**. |
| Dead crew | `<deadCrew>` | `autoReward level="HIGH"` type `standard` — **high scrap with resources**. |

On the `gotaway` screen:

| # | Choice | Outcome | Odds |
|---|---|---|---|
| 1 | After them! | *"You input their coordinates into your map and prepare to follow."* → `<quest event="DONOR_MANTIS_CHASE2"/>` adds a quest marker. | 100% |
| 2 | Forget it. | *"They're not worth the trouble. You prepare to leave."* → nothing. | 100% |

There is **no `chance` attribute on the `<escape>` element**, only a 5-second timer and
`min="5" max="5"`. [[source-fandom-mantis-ship-collectors]] reads this as a **100% escape
attempt** at 50% hull. The `min`/`max` values are hull points rather than percentages —
Fandom's own tooltip on the sibling ship says as much, and [[concept-surrender-offers]]
records the same trap for `<surrender>`. Treat "50% hull" as an interpretation, "5 hull
points" as the raw fact.

### The rematch — `DONOR_MANTIS_CHASE2` (quest marker)

Reached only via choice 1 above. It is a separate top-level event with its own id, so it
carries its own join key; it is documented here because it exists solely as this event's
continuation.

> You catch up with the Mantis ship that escaped before, only to see them transferring
> their crew into an even bigger ship!
>
> "Not YOU again! Do you know how much these repairs are going to cost me? Time to take
> out the big guns."

(`event_DONOR_MANTIS_CHASE2_text`, `event_DONOR_MANTIS_CHASE2_c1_text`, per
[[source-text-events-xml]])

Fight `DONOR_MANTIS_CHASE2`, a Mantis Bomber (`auto_blueprint="MANTIS_BOMBER"`), again
all-Mantis crew:

| Ship result | Raw tag | Outcome |
|---|---|---|
| Escape | `<escape timer="12" min="6" max="6">` | *"They appear to be trying to get away again. You doubt they'll forget to mask their jump signature this time."* |
| Got away | `<gotaway>` | `autoReward level="HIGH"` type `standard` — **high scrap with resources** anyway: *"At least you're able to scrap their abandoned fighter."* |
| Surrender | `<surrender min="2" max="2">` | *"Look, you proved your point. We don't want to die... Take this and let us go. Please?"* → two choices, below. |
| Destroyed | `<destroyed>` | `<weapon name="RANDOM"/>` **plus** `autoReward level="MED"` type `standard`. |
| Dead crew | `<deadCrew>` | `<weapon name="RANDOM"/>` **plus** `autoReward level="HIGH"` type `standard`. |

Surrender choices:

| # | Choice | Outcome |
|---|---|---|
| 1 | Let them live. | *"Thank you. But do you have any idea how much repairing TWO ships will set us back?..."* → `autoReward level="HIGH"` type `weapon` (a weapon with high scrap), ship becomes non-hostile. |
| 2 | Finish them off. | *"No! Hurry up, get us out of here! They're crazy!"* → the fight continues. |

The `<surrender>` element on this ship carries **no `chance` attribute** — only
`min="2" max="2"`. Under [[concept-surrender-offers]], `chance` is the probability the ship
*keeps fighting*, so its absence leaves the offer frequency `unknown` rather than implying
a value. Fandom reads the thresholds as "escapes at 60% hull, offers surrender at 20% hull"
with its own caveat that the real values are hull points scaled by sector progression
([[source-fandom-mantis-ship-collectors]]).

Every terminal outcome of the rematch except "let them escape while they still have crew"
pays a weapon, and the weapon and scrap are shown before you accept the surrender.

## Blue Options
None. Neither half of this event has a `req=` gate.

## Rewards & Risks
- First ship: medium (destroyed) or high (dead crew) scrap with resources.
- Rematch: a **guaranteed random weapon** on destroyed / dead crew / accepted surrender,
  plus medium-to-high scrap. Even the "they escaped" branch pays high scrap.
- [[source-fandom-mantis-ship-collectors]] adds a payload note the files don't state: a
  `standard` scrap-with-resources roll *"will never give a bonus weapon, drone schematic or
  augmentation, due to its interaction with a guaranteed weapon/drone schematic reward"* —
  so on the rematch you get the weapon *instead of*, not on top of, a bonus item roll.
- Risk: two consecutive Mantis fights, the second against a bomber, with all-Mantis crews
  that will board and out-fight most human crews. The rematch is a fresh full-health enemy.

## Strategy Notes
- The chase branch is worth taking if you can win a second fight — it is the only way to a
  guaranteed weapon here. *Opinion*, from the reward structure in [[source-events-xml]];
  no source rates it.
- Killing the first ship outright forecloses the rematch entirely. If you want the weapon,
  you want them to survive to escape — which is not something you can force.
- Boarding the first ship to kill its crew is worth an extra reward tier (HIGH vs MED), but
  an all-Mantis crew is a bad boarding target.

## Related
- [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]] — where it appears
- [[entity-mantis]] — the crew you are fighting on both ships
- [[event-donor-mantis-chase2]] — the rematch, if it is ever split out to its own page
- [[concept-surrender-offers]] — how to read the `<surrender>` and `<escape>` attributes
- [[concept-quest-beacons]] — how the `<quest>` marker works

## Open Questions
- [ ] Does `<escape>` without a `chance` attribute mean a guaranteed attempt, as Fandom
      reads it? [[concept-surrender-offers]] leaves the `<escape>` convention untested.
- [ ] Same question for `<surrender>` with no `chance` on `DONOR_MANTIS_CHASE2`.
- [ ] Are the `min`/`max` values hull points or percentages? Unresolved wiki-wide.
- [x] ~~Whether `DONOR_MANTIS_CHASE2` should carry its own event page for its join key~~ —
      it does: [[event-donor-mantis-chase2]].

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-mantis]] (per raw/gamedata/events_mantis.xml — the `HOSTILE_MANTIS` pool)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-mantis-ship-collectors]] (per raw/wiki/mantis-ship-collectors.md)
