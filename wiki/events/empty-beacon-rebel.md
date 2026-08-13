---
id: event-empty-beacon-rebel
type: event
event_name: NOTHING_REBEL
sectors: [[[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]]]
beacon_type: empty
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [rebel, structural, empty-beacon, no-choice, flavour-only]
---

# Empty beacon (Rebel) — `NOTHING_REBEL`

## Summary
The Rebel sector's empty beacon: five lines of flavour text and nothing else. Structurally
required — every sector definition allocates a `NOTHING_*` event so the map has beacons that
are safe to jump to — and it is the only place the game describes what Rebel-held space
looks like when nobody is shooting at you.

## Trigger & Where It Appears
- Sectors: [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]].
- **Not in any event list.** It is allocated directly by the sector definitions as
  `<event name="NOTHING_REBEL" min="1" max="2"/>` — 1–2 beacons per Rebel sector, in both
  `REBEL_SECTOR` and `REBEL_SECTOR_MINIBOSS` ([[source-sector-data-xml]]). The file carries
  a dev comment on that line: `<!-- need more -->`.
- Beacon: empty. Long-range scanners show **no ship**
  ([[source-fandom-empty-beacon-rebel]]).
- Not unique — it recurs, which is the point.
- Filed in `events_rebel.xml` under the `STRUCTURE!!! / Required structural` header
  ([[source-events-rebel]]).

## Text
Drawn from the `NOTHING_REBEL` text list — **five variants**, two of which are gated on the
beacon's backdrop art ([[source-events-rebel]], [[source-text-events-xml]]):

| # | Gate | Text |
|---|---|---|
| 1 | — | *"You enter a system bustling with Rebel activity. Supply freighters and re-supply stations are dwarfed by a few heavy warships. Luckily, no one seems to be paying attention to small cruisers. No ships are scanning or messaging you."* |
| 2 | — | *"You arrive near a small Rebel refueling depot. Your ship is being scanned multiple times so they must recognize you, but there appears to be no combat-ready ships in the vicinity. The only message you receive is a denial to your request to dock at the depot."* |
| 3 | — | *"There is not much of interest nearby. A small sun in the distance with a few orbiting planets in nearby space provide little of interest."* |
| 4 | `planet="NONE"` | *"There are no other ships near this beacon, however you detect a small communication relay. You tap into it without a problem; there is no encryption. Most of the chatter revolves around troop and fleet movements, not particularly interesting."* |
| 5 | `planet="PLANET_POPULATED_SMALL"` | *"There is a small planet nearby with scattered settlements. A small Rebel fleet is in orbit with many ships ferrying back and forth. It must be a more recently 'liberated' planet."* |

The `planet=` attributes mean variants 4 and 5 only appear when the beacon's generated
backdrop matches — a detail the Fandom transcription does not record
([[source-events-rebel]] vs [[source-fandom-empty-beacon-rebel]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event body is a single `<text load="NOTHING_REBEL"/>`)* | — | Nothing happens. | 100% |

## Blue Options
None.

## Rewards & Risks
Neither. No `autoReward`, no `ship`, no `damage`, no `modifyPursuit`. The beacon is
mechanically inert.

## Strategy Notes
- Empty beacons are not worthless in a Rebel sector: they are the safe stepping stones for
  routing toward the exit while the fleet advances, and the only beacons that cost you
  nothing but a jump.
- 1–2 per sector, so you cannot rely on them for a safe path
  ([[source-sector-data-xml]]).

## Related
- [[event-start-beacon-rebel]] — the sector's other structural text-only event
- [[event-store-rebel]] — the third structural entry
- [[event-empty-beacon-engi]], [[event-empty-beacon-mantis]], [[event-empty-beacon-rock]],
  [[event-empty-beacon-zoltan]], [[event-empty-beacon-crystal]] — the sibling `NOTHING_*` events
- [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]]

## Open Questions
- [ ] Whether the three ungated variants are equally weighted against the two gated ones.
- [ ] What the `<!-- need more -->` dev comment on the sector allocation was pointing at.

## Sources
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-empty-beacon-rebel]] (per `raw/wiki/empty-beacon-rebel.md`)
