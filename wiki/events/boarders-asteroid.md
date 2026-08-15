---
id: event-boarders-asteroid
type: event
event_name: BOARDERS_ASTEROID
sectors: []
beacon_type: unknown
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [pirate, boarding-hazard, asteroid-field, no-enemy-ship, unique, unreachable, no-fandom-page]
---

# Boarders in asteroid field — `BOARDERS_ASTEROID`

## Summary
Fully authored but, as far as the sector data goes, **unreachable**. A pirate stronghold
teleports 2–4 human boarders onto your ship inside an asteroid field. There is no enemy
ship, no choice and no reward. Its only event-list membership is `HOSTILE_BOARDING`, and
`sector_data.xml` allocates that list `min="0" max="0"` in the one sector that still
references it.

## Trigger & Where It Appears
- **Not reachable from any live sector event allocation.** The only list containing it is
  `HOSTILE_BOARDING` ([[source-newevents]]), and `sector_data.xml` uses that list in
  exactly two places ([[source-sector-data-xml]]):
  - `STANDARD_SPACE` ([[sector-federation-space]]) — `<event name="HOSTILE_BOARDING" min="0" max="0"/>`, i.e. zero beacons
  - `CIVILIAN_SECTOR` ([[sector-civilian-sector]]) — `<!-- <event name="HOSTILE_BOARDING" min="0" max="1"/> -->`, commented out
- Unlike its siblings `BOARDERS_SUN` and `FLOATING_CARGO`, it is **not** a member of
  `BOARDERS_PIRATE`, `BOARDERS_MANTIS` or `BOARDERS_REBEL` — the three boarding lists that
  sectors actually allocate ([[source-events-pirate]], [[source-events-mantis]],
  [[source-events-rebel]]).
- `newEvents.xml` also contains `<eventCounts sector="1|2|3">` blocks that allocate
  `HOSTILE_BOARDING` at `min=1 max=2` ([[source-newevents]]). Whether the engine reads
  those `eventCounts` elements is **not established here** — no `eventCounts` element
  exists in `sector_data.xml`, and one block is headed *"PLANNING FOR the 3rd Sector"*.
  If they are live, this event is reachable in sectors 2–4; if they are planning leftovers,
  it is not reachable at all. Flagged as an open question rather than resolved.
- **No Fandom page** documents this event, and no Fandom page in the local dump mentions
  the id `BOARDERS_ASTEROID` — consistent with players not encountering it. (The similarly
  named `ROCK_BOARDERS_ASTEROID` on *"Rock fight with boarders in asteroid field"* is a
  different event, with Rock boarders and a Rock ship.)
- `unique="true"`; drawn with `<img back="BG_DARK" planet="NONE"/>`
  ([[source-events-pirate]])

## Text
> You jump into a perilous asteroid field. Worse, sensors show a pirate stronghold has
> locked onto our ship and is activating a teleporter. Prepare for a fight!

(`event_BOARDERS_ASTEROID_text`, per [[source-text-events-xml]]. Note the file's own
first-person slip, "our ship" — quoted as-is.)

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(no choices)_ | — | `<boarders min="2" max="4" class="human"/>` with `<environment type="asteroid"/>` — **2–4 human boarders** aboard, under asteroid fire. | 100% |

The event body is an `<img>`, a `<text>`, a `<boarders>` tag and an `<environment>` tag.
No `<ship>`, no `<autoReward>`, no branches ([[source-events-pirate]]).

## Blue Options
None.

## Rewards & Risks
- **Reward: none.** No `autoReward`, no scrap, no items.
- **Risk:** 2–4 human boarders with no ship to shoot, while asteroids strike the hull and
  can breach the very rooms you are fighting in. The "pirate stronghold" in the text never
  materialises as a `<ship>`.

## Strategy Notes
- Not applicable in practice — see *Trigger* above. Documented because it is complete,
  shipped content, not because it can be played.

## Related
- [[event-boarders-humans-near-sun]] — the reachable sibling: same 2–4 human boarders,
  sun hazard instead of asteroids, and it *is* in the live boarding lists
- [[event-pirate-fight-in-asteroid-field]] — asteroid field with a ship to fight
- [[event-destroyed-cargo-ship]] — the other `HOSTILE_BOARDING` member that is also in a
  live list
- [[sector-federation-space]], [[sector-civilian-sector]] — the two sectors whose data
  still names `HOSTILE_BOARDING`
- [[entity-pirates]]

## Open Questions
- [ ] Are the `<eventCounts sector="N">` blocks in `newEvents.xml` read by the engine? If
      so this event is reachable in sectors 2–4 and the `unreachable` tag is wrong.
- [ ] Was `HOSTILE_BOARDING` zeroed out deliberately, or superseded by the per-faction
      `BOARDERS_*` lists? Nothing in the files says.
- [ ] Is the boarder count uniform over 2–4?

## Sources
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml — `HOSTILE_BOARDING` and the
  `eventCounts` blocks)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-mantis]] / [[source-events-rebel]] (per raw/gamedata/events_mantis.xml,
  raw/gamedata/events_rebel.xml — confirming it is absent from the live boarding lists)
