---
id: event-empty-beacon-mantis
type: event
event_name: NOTHING_MANTIS
sectors: [[[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]]
beacon_type: empty
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [empty-beacon, no-choice, flavour-only, mantis]
---

# Empty beacon (Mantis) — `NOTHING_MANTIS`

## Summary
The Mantis-flavoured empty beacon. One line of prose from a six-string list, no choices,
no payload of any kind. Mechanically it is a free jump: the beacon exists so that the
sector map has somewhere safe to stand.

## Trigger & Where It Appears
- Sectors: [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]
- Allocated directly by name in both Mantis sector descriptions at `min=2 max=3`
  ([[source-sector-data-xml]], per `raw/gamedata/sector_data.xml`) — so every Mantis
  sector has two or three of these.
- No `unique` attribute, i.e. it repeats.
- No ship; long-range scanners show none ([[source-fandom-empty-beacon-mantis]]).

## Text
Drawn from the `NOTHING_MANTIS` text list — the prose **varies** across six strings
([[source-events-xml]], [[source-text-events-xml]]):

> At this point you almost expect a fight with the Mantis, but this beacon appears to be
> entirely devoid of other ships. You take the time to catch your breath and double check
> the ship's systems.

> The only thing this beacon offers is a view of deep space and a brief respite from
> battles. For some this must be a welcome refuge.

> A nearby Mantis mining operation is clearly using heavy Engi slave labor. You briefly
> consider the possibility of emancipating the slaves, but the Mantis presence is too
> formidable. You decide to lay low.

> There aren't so many parts of Mantis space that aren't dotted by the wrecks of battles
> past, but this is one of them. You take a deep breath and prepare to move on.

> There's nothing here but space debris and some uninhabitable planetoids.

> You fancy you see something moving in the shadow of the beacon, but all remains still.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event is a single `<text load="NOTHING_MANTIS"/>` and nothing else)_ | — | Nothing happens. | 100% |

## Blue Options
None.

## Rewards & Risks
Neither. The event definition contains no `autoReward`, `item_modify`, `damage`,
`boarders`, `crewMember` or `ship` element ([[source-events-xml]]). Nothing good or bad
can happen here.

## Strategy Notes
- The only value is positional: an empty beacon is a safe place to burn a jump, repair
  crew, or wait out a fleet-advance tick — and Mantis sectors guarantee 2–3 of them
  ([[source-sector-data-xml]]).
- The Engi-slave-labour variant is flavour only. It offers no choice to intervene, despite
  the text implying one.

## Related
- [[event-start-beacon-mantis]] — the other no-payload Mantis beacon
- [[event-mantis-fight]] — what the rest of the sector looks like
- [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]
- [[concept-empty-beacons]] — the per-faction family of `NOTHING_*` events

## Open Questions
- [ ] Are the six text variants equally weighted? No weights in the file.

## Sources
- [[source-events-xml]] (per raw/gamedata/events_mantis.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-empty-beacon-mantis]] (per raw/wiki/empty-beacon-mantis.md)
