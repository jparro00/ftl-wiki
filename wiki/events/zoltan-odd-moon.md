---
id: event-zoltan-odd-moon
type: event
event_name: ZOLTAN_ODD_MOON
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: any
hostile: false
blue_options: [[[item-boarding-drone]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, blue-option, crew-reward, weapon-reward, missile-cost, drone-cost, no-risk]
---

# Zoltan odd moon — `ZOLTAN_ODD_MOON`

## Summary
A completely safe exploration event — no branch leads to combat or damage. Checking it
out rolls one of four results, one of which opens a further "spend a missile" gamble.
With a Boarding Drone it becomes a **guaranteed free [[entity-zoltan]] crew member** for
one drone part, which is one of the best drone-part conversions in the game.

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Beacon: ordinary, no ship present.
- Reached via the `ITEM_ZOLTAN` event list, allocated `min=1 max=2` beacons in both
  Zoltan sectors ([[source-sector-data-xml]]).
- `unique="true"` — at most once per sector.

## Text
> Something strikes you as odd about a moon in the distance.

(`event_ZOLTAN_ODD_MOON_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Check it out. | — | Loads `ZOLTAN_ODD_MOON_CHECK` — four entries, see below. | unknown |
| 2 | Leave it be. | — | *"You try not to fixate on the moon in the aft scanner as you set the coordinates for the next jump."* Nothing happens. | 100% |
| 3 | **(Boarding Drone)** Send a drone to probe the surface. | `req="BOARDER"` | −1 drone part, then a forced continue → *"Buried deep below you find a Zoltan scientist, still hard at work…"* → `<crewMember amount="1" class="energy"/>`, **a Zoltan crew member**. | 100% |

### `ZOLTAN_ODD_MOON_CHECK` — the four results of choice 1

| Entry | Text | Effect |
|-------|------|--------|
| 1 | *"A closer inspection reveals signs of habitation on the surface, but nothing else particularly interesting."* | Nothing. |
| 2 | *"Sending a shuttle to explore a beckoning cave system you discover signs of a battle - and a still-functioning weapon!"* | `autoReward level="LOW"` `weapon` — a weapon plus low scrap. |
| 3 | *"A deep scan of the surface reveals a cave system that runs for miles, and what looks like a scrap heap left over from some heavy-duty construction."* | `autoReward level="MED"` `scrap_only`. |
| 4 | *"It looks as if a team could break through the fragile layer of the moon's surface into a hidden cavern."* | Opens the explosives sub-choice below. |

### Entry 4's sub-choice

| # | Sub-choice | Outcome |
|---|-----------|---------|
| 4a | Attempt to detonate some explosives to break through the surface. | −1 missile, then loads `ZOLTAN_ODD_MOON_EXPLOSION` (three entries). |
| 4b | Explosives are too valuable to waste on excavation work. Let's get out of here. | Nothing. |

### `ZOLTAN_ODD_MOON_EXPLOSION` — the three results of 4a

| Entry | Text | Effect |
|-------|------|--------|
| 1 | *"A portion of the surface layer is destroyed in an impressive display, revealing miles of caves…"* | −1 missile, `autoReward level="RANDOM"` `scrap_only`. |
| 2 | *"The explosives are set remotely, but the detonation achieves nothing. What a waste."* | −1 missile, nothing else. |
| 3 | *"Your explosives reveal the 'cave' is actually a secret base… It looks like the Zoltan were researching advanced ship weaponry."* | −1 missile, `autoReward level="RANDOM"` `weapon`. |

The missile is deducted inside each `ZOLTAN_ODD_MOON_EXPLOSION` entry (not on the choice
itself), so **all three outcomes cost exactly 1 missile**
([[source-events-zoltan]], per raw/gamedata/events_zoltan.xml). No percentages are stated
for either list.

## Blue Options
- **[[item-boarding-drone]]** (`req="BOARDER"`) — requires a Boarding Drone in your drone
  inventory, and consumes **1 drone part**. It bypasses the entire random table and
  guarantees a Zoltan crew member. The game source carries the developer comment
  `<!-- TODO make sure this works!!! -->` next to this `req`, which is worth knowing if
  the option ever fails to appear ([[source-events-zoltan]]).

## Rewards & Risks
- **No risk of combat, hull damage, or crew loss on any branch.** The only costs are
  optional: 1 missile (4a) or 1 drone part (choice 3).
- Possible rewards: a free Zoltan crew member, a `LOW` or `RANDOM` weapon, `MED` or
  `RANDOM` scrap, or nothing.

## Strategy Notes
- *Opinion:* choice 3 is the strongest outcome available and should be taken whenever a
  Boarding Drone is aboard — a full crew member for one drone part is well above the
  usual exchange rate, and Zoltan crew power a room while alive.
- *Opinion:* without the blue option, choice 1 is free upside and always worth taking.
  Within it, spending the missile on 4a is a genuine gamble: one of the three results
  wastes the missile outright.

> ⚠️ **CONTRADICTION:** wording of `ZOLTAN_ODD_MOON_EXPLOSION_3`.
> - Game files: *"Everyone inside is dead; **some** Mantis clearly came through here
>   recently… You take one of **their** better examples back to your ship."*
>   ([[source-text-events-xml]], per raw/gamedata/text_events.xml)
> - Fandom: *"Everyone inside is dead; Mantis clearly came through here recently… You
>   take one of **the** better examples back to your ship."*
>   ([[source-fandom-zoltan-odd-moon]])
>
> Trusting the game files (`high` vs `medium`). Reads like an older transcription; not
> confirmed as a vanilla/AE difference.

## Related
- [[item-boarding-drone]] — the gate on choice 3
- [[entity-zoltan]] — the crew member you can recruit here
- [[event-zoltan-free-augment]], [[event-zoltan-free-map]] — the other two Zoltan
  members of the `ITEM_ZOLTAN` pool

## Open Questions
- [ ] Weighting of the four `ZOLTAN_ODD_MOON_CHECK` entries and the three
      `ZOLTAN_ODD_MOON_EXPLOSION` entries.
- [ ] Does `req="BOARDER"` accept any drone-part-capable boarding drone variant, or only
      the base Boarding Drone blueprint?
- [ ] Whether the developer TODO comment reflects a still-live bug in AE.

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-zoltan-odd-moon]] (per raw/wiki/zoltan-odd-moon.md)
