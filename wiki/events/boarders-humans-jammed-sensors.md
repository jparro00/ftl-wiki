---
id: event-boarders-humans-jammed-sensors
type: event
event_name: BOARDERS_HACKING
sectors: [[[sector-pirate-controlled-sector]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]], [[sector-federation-space]]]
beacon_type: any
hostile: true
blue_options: [[[item-hacking]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [pirate, zoltan, boarding-hazard, no-enemy-ship, blue-option, system-malfunction, unique, advanced-edition-blue-option]
---

# Boarders: Humans jammed sensors — `BOARDERS_HACKING`

## Summary
[[event-boarders-humans-pirate]] with a twist: the same 3–5 human boarders, but a station
jams your **Sensors** for the whole beacon while you fight them blind. The Hacking system
cancels the jam — and that blue option is an **Advanced Edition addition**, so in vanilla
there is no way out of the blackout. `unique="true"`.

## Trigger & Where It Appears
- Sectors: [[sector-pirate-controlled-sector]], [[sector-zoltan-controlled-sector]],
  [[sector-zoltan-homeworlds]], and nominally [[sector-federation-space]]
- Event lists: `BOARDERS_PIRATE` ([[source-events-pirate]]), `BOARDERS_ZOLTAN`
  ([[source-events-zoltan]]), `HOSTILE_BOARDING` ([[source-newevents]])
- Allocation: `BOARDERS_PIRATE` `min=1 max=1` in `PIRATE_SECTOR`; `BOARDERS_ZOLTAN`
  `min=1 max=2` in both `ZOLTAN_SECTOR` and `ZOLTAN_HOME` ([[source-sector-data-xml]]).
  `BOARDERS_ZOLTAN` has only **three** members, so this is a common draw in Zoltan space.
- **`HOSTILE_BOARDING` is dead** — `min="0" max="0"` in `STANDARD_SPACE`, commented out in
  `CIVILIAN_SECTOR` ([[source-sector-data-xml]]), which is why Fandom omits Federation Space
- Beacon: any — no `<ship>`, no `<distressBeacon/>`, no `<environment>`
- Long-range scanners show **no ship** ([[source-fandom-boarders-humans-jammed-sensors]])
- `unique="true"` — once per run

## Text
> You catch a glimpse of a strange signal coming from a space station before your sensors
> shut off unexpectedly. As you discover that your sensors are being jammed, you hear
> hostiles beam onto your ship.

(`event_BOARDERS_HACKING_text`, per [[source-text-events-xml]])

Note the ordering in the file: `<boarders>` sits **before** the choices, so the 3–5 humans
arrive on both branches ([[source-events-xml]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | *(Continue…)* | — | *"Until you are able to jump away from the hostile space station, your sensors will be disabled. You should deal with these boarders first though!"* → `<status type="limit" target="player" system="sensors" amount="0"/>` — Sensors capped at 0 for the rest of the beacon, on top of the 3–5 human boarders | 100% |
| 2 | **(Hacking System)** Counter the remote hacking. | `req="hacking"` | *"Your hacking system automatically counters the digital assault. Your Sensors flicker back on and you prepare to fight the boarders."* → no `status` tag; the 3–5 boarders remain | 100% |

The `status` tag is `type="limit" … amount="0"`, i.e. a **cap**, not damage. Fandom's notes
add three details it does not source to the files but which follow from that reading
([[source-fandom-boarders-humans-jammed-sensors]]):

- the Sensors blackout persists until you jump to another beacon;
- countering the jam does **not** disable your Hacking system;
- the event text is unchanged if you have no Sensors subsystem at all.

## Blue Options
- **[[item-hacking]]** (`req="hacking"`, the system) — removes the Sensors cap. It costs
  nothing: no hacking drone is spent and no `item_modify` appears in the branch. It is
  marked `<!--DLC - added -->` in the file, so **it does not exist in vanilla**
  ([[source-events-xml]]).

## Rewards & Risks
- **Reward: none.** No `autoReward`, no items, on either branch.
- **Risks:** 3–5 human boarders, plus — without Hacking — blind Sensors for the whole
  beacon. Losing Sensors means you cannot see enemy room contents; with no enemy ship here,
  the practical cost is losing the display of *your own* rooms' oxygen and intruder
  positions on some ship layouts.

## Version Differences
- **Vanilla:** the event is choice 1 only — 3–5 human boarders and a guaranteed Sensors
  blackout, no way to prevent it.
- **Advanced Edition:** adds the `req="hacking"` branch, marked `<!--DLC - added -->`
  ([[source-events-xml]]). The Hacking system itself is an AE system, so the option could
  not have existed before.

Everything else — text, boarder count, the `status` tag — is identical across editions.

## Strategy Notes
- *(Opinion.)* If you own Hacking, take choice 2 every time; it is free.
- Without it, treat this as [[event-boarders-humans-pirate]] fought at a disadvantage. There
  is nothing to win, so end it as cheaply as possible and jump — the blackout ends with the
  jump.

## Related
- [[event-boarders-humans-pirate]] — the same 3–5 humans, no jam; shares `BOARDERS_PIRATE`
- [[event-boarders-humans-near-sun]], [[event-boarders-asteroid]] — the hazard variants
- [[event-boarders-asteroid-ghost]] — the ghost-boarder variant in the same
  `HOSTILE_BOARDING` list
- [[item-hacking]], [[entity-pirates]]
- [[sector-pirate-controlled-sector]], [[sector-zoltan-controlled-sector]],
  [[sector-zoltan-homeworlds]]

## Open Questions
- [ ] Is the boarder count uniform over 3–5?
- [ ] What `status type="limit" … amount="0"` does to a ship with no Sensors installed —
      Fandom says the text is unchanged, but not what the effect is.
- [ ] Can this event appear in [[sector-federation-space]]? Only via the dead
      `HOSTILE_BOARDING` allocation.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-events-pirate]] (per `raw/gamedata/events_pirate.xml` — `BOARDERS_PIRATE`)
- [[source-events-zoltan]] (per `raw/gamedata/events_zoltan.xml` — `BOARDERS_ZOLTAN`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml` — `HOSTILE_BOARDING`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-boarders-humans-jammed-sensors]] (per `raw/wiki/boarders-humans-jammed-sensors.md`)
