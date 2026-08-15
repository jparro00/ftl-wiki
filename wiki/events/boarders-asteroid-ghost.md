---
id: event-boarders-asteroid-ghost
type: event
event_name: BOARDERS_ASTEROID_GHOST
sectors: [[[sector-federation-space]]]
beacon_type: any
hostile: true
blue_options: [engines lvl 5, piloting lvl 2]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 8
tags: [unreachable, boarding-hazard, ghost, asteroid-field, no-enemy-ship, blue-option, unique, no-fandom-page]
---

# Boarders: Ghosts in a ship graveyard — `BOARDERS_ASTEROID_GHOST`

## Summary
Fully authored, atmospheric, and — as far as `sector_data.xml` goes — **unreachable**. A
field of wrecks disgorges 3–6 *ghost*-class boarders onto your ship while asteroids pound
the hull. Two blue options let you run instead, at a price. Its only event-list membership
is `HOSTILE_BOARDING`, the list the sector data switches off. **No Fandom page exists for
it**, which is itself consistent with players never seeing it.

## Trigger & Where It Appears
- **Not reachable from any live sector event allocation.** The only list containing it is
  `HOSTILE_BOARDING` ([[source-newevents]]), and `sector_data.xml` names that list in
  exactly two places ([[source-sector-data-xml]]):
  - `STANDARD_SPACE` = [[sector-federation-space]] —
    `<event name="HOSTILE_BOARDING" min="0" max="0"/>`, i.e. zero beacons
  - `CIVILIAN_SECTOR` = [[sector-civilian-sector]] —
    `<!-- <event name="HOSTILE_BOARDING" min="0" max="1"/> -->`, commented out
- Unlike `BOARDERS` and `BOARDERS_HACKING`, it is **not** a member of `BOARDERS_PIRATE`,
  `BOARDERS_MANTIS`, `BOARDERS_REBEL` or `BOARDERS_ZOLTAN` — the boarding lists sectors
  actually allocate ([[source-events-pirate]], [[source-events-mantis]],
  [[source-events-rebel]], [[source-events-zoltan]]).
- `newEvents.xml` also carries `<eventCounts sector="1|2|3">` blocks that allocate
  `HOSTILE_BOARDING` at `min=1 max=2` ([[source-newevents]]). Whether the engine reads
  `eventCounts` is **not established here** — no such element exists in `sector_data.xml`
  and one block is headed *"PLANNING FOR the 3rd Sector"*. If they are live, this event is
  reachable in sectors 2–4; if they are planning leftovers, it is not reachable at all.
  Recorded as an open question, not resolved. The same reasoning appears on
  [[event-boarders-asteroid]].
- `unique="true"`; background forced to `<img back="BG_DARK" planet="NONE"/>`
  ([[source-events-xml]])
- **No Fandom page.** Nothing in the 293 pages under `raw/wiki/` mentions this event or its
  prose, so every claim here comes from the game files alone.

## Text
> You jump into the middle of an asteroid field. Looking around, you find you are surrounded
> by dozens of wrecks of other ships. Faint wisps of light can be seen moving between
> wrecks. As you watch, they seem to be changing path and floating toward your ship!

(`event_BOARDERS_ASTEROID_GHOST_text`, per [[source-text-events-xml]])

The definition carries a developer note in the source: `<!-- JUSTIN - maybe add some sort of
ship graveyard background? -->` ([[source-events-xml]]) — a hint that the event was still
being finished.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Prepare for a fight! | — | `<boarders min="3" max="6" class="ghost"/>` + `<environment type="asteroid"/>` — **3–6 ghost boarders** while asteroids hit the hull. No text, no reward. | 100% |
| 2 | **(Engines)** Activate full impulse drive to escape. | `req="engines" lvl="5"` | *"With your Advanced Engines you were able to quickly get out of the asteroid field, however your ship took a number of hits on the way out."* → `damage 3` + `damage 1 random system` (AE only). **No boarders at all.** | 100% |
| 3 | **(Piloting)** Have your pilot maneuver you out of the asteroid field. | `req="pilot" lvl="2"` | *"Thanks to your pilot, you were able escape the worst of the asteroid field unscathed. However, the wisps of light stream out of the field following your ship!"* → `<boarders min="2" max="4" class="ghost"/>`, **no asteroid environment** | 100% |

## Blue Options
- **Engines level 5** (`req="engines" lvl="5"`) — the only clean exit: no boarders at all,
  paid for with 3–4 hull. Engines 5 is a steep gate; this is the deepest system-level blue
  option in this batch.
- **Piloting level 2** (`req="pilot" lvl="2"`) — halves the boarding party (2–4 instead of
  3–6) and removes the asteroid hazard, at no hull cost. A cheap gate for a large benefit.

Neither is a species or item gate; both are system levels, so any ship can qualify by
upgrading.

## Rewards & Risks
- **Reward: none.** No `autoReward`, no items, no ship to destroy — on any branch.
- **Risks:** `ghost`-class boarders. This is one of very few events that spawns them; the
  class is shared with [[event-ghost-ship]]. Combined with an asteroid field and no enemy
  vessel to shoot, choice 1 is a pure attrition fight.
- Choice 2 trades the entire encounter for 3 hull (vanilla) / 4 hull and a random system
  (AE).

## Version Differences
Base-`events.xml` event, present in both editions. One `<!--DLC-->`-marked tag:
`<damage amount="1" system="random"/>` on the Engines branch ([[source-events-xml]]).
Vanilla therefore pays **3 hull** to escape; AE pays 4 hull and loses a random system.

## Strategy Notes
- *(Opinion, and untested — this event may not be reachable at all.)* If it does fire, the
  Piloting-2 option is close to free and should be the default: fewer boarders, no rocks.
  Engines 5 is the answer only if your crew cannot win a melee.

## Related
- [[event-ghost-ship]] — the other source of `ghost`-class boarders, and a fellow
  `HOSTILE_BOARDING` member
- [[event-boarders-asteroid]] — the same list, also unreachable, human boarders instead
- [[event-boarders-humans-pirate]], [[event-boarders-humans-jammed-sensors]] — the
  `HOSTILE_BOARDING` members that *are* reachable, via `BOARDERS_PIRATE`
- [[sector-federation-space]], [[sector-civilian-sector]] — the two sectors whose data still
  names `HOSTILE_BOARDING`

## Open Questions
- [ ] Are the `<eventCounts sector="N">` blocks in `newEvents.xml` read by the engine? If
      so this event is reachable in sectors 2–4 and the `unreachable` tag is wrong.
- [ ] What `class="ghost"` boarders actually are mechanically — no blueprint reference is
      given in the event.
- [ ] Is the boarder count uniform over 3–6 / 2–4?
- [ ] Was `HOSTILE_BOARDING` zeroed out deliberately, or superseded by the per-faction
      `BOARDERS_*` lists? Nothing in the files says.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml` — `HOSTILE_BOARDING`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-events-pirate]] (per `raw/gamedata/events_pirate.xml` — `BOARDERS_PIRATE`, for contrast)
- [[source-events-zoltan]] (per `raw/gamedata/events_zoltan.xml` — `BOARDERS_ZOLTAN`, for contrast)
