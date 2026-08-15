---
id: event-mantis-fight
type: event
event_name: MANTIS_FIGHT
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [mantis, no-choice, default-rewards, combat]
---

# Mantis fight — `MANTIS_FIGHT`

## Summary
The baseline hostile Mantis encounter: you arrive, a Mantis ship is already shooting,
there are no choices. Two lines of XML — a text list and
`<ship load="MANTIS_FIGHT" hostile="true"/>` — behind twenty different flavour texts. It
is the single most common thing that happens in a Mantis sector, and the `MANTIS_FIGHT`
ship definition is reused as the enemy by several other Mantis events.

## Trigger & Where It Appears
- Sectors: [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]] (via
  `HOSTILE_MANTIS` / `OVERRIDE_HOSTILE_MANTIS`, allocated `min=6 max=7` per Mantis
  sector — [[source-sector-data-xml]]), and also
  [[sector-civilian-sector]] / [[sector-federation-space]] via the `MANTIS_HOSTILE` list,
  which the generic `HOSTILE1` / `OVERRIDE_HOSTILE1` pools load
  ([[source-events-xml]], per `raw/gamedata/newEvents.xml` and
  `raw/gamedata/dlcEventsOverwrite.xml`).
- `MANTIS_FIGHT` appears **twice** in each of `HOSTILE_MANTIS`, `OVERRIDE_HOSTILE_MANTIS`
  and `MANTIS_HOSTILE`, doubling its weight relative to the other entries in those lists.
- `unique="false"` — it repeats freely.
- Long-range scanners show a ship ([[source-fandom-mantis-fight]]).

> **AE note:** `OVERRIDE_HOSTILE_MANTIS` (in `dlcEventsOverwrite.xml`) is the Advanced
> Edition replacement for `HOSTILE_MANTIS`. The two are nearly identical; AE swaps the
> final `AUTO_WARNING` slot for `REBEL_PULSAR`. `MANTIS_FIGHT`'s own weight is unchanged.

## Text
The prose is drawn from the `MANTIS_FIGHT` text list and **varies across twenty strings**
([[source-events-xml]], [[source-text-events-xml]]) — no single one is *the* event text.
The file itself splits them into two authored batches (1–7 and 8–20, the latter commented
"These are the ones by tom"). Representative examples:

> A Mantis military ship appears on local radar alongside the remains of a human
> freighter. Prepare for a hostile encounter!

> A small Mantis cruiser is broadcasting a repeating message on a wide-band frequency,
> "All non-Mantis ships that enter our territory are forfeit. Lower your shields and
> surrender if you value your lives."

> Something red looms. It's the Mantis.

> A youthful-looking Mantis captain hails. "You, prey, must know. Your death,
> Kaaazthwak's final kill before maturity. Kaaazthwak pay respects." Seems respects in
> Mantis culture are paid with lasers.

All twenty are transcribed on [[source-fandom-mantis-fight]] and in
`raw/gamedata/text_events.xml` at `text_MANTIS_FIGHT_1` … `text_MANTIS_FIGHT_20`.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event has no `<choice>` elements)_ | — | Immediate combat with a Mantis ship (`ship load="MANTIS_FIGHT" hostile="true"`), **default rewards**. | 100% |

"Default rewards" is Fandom's term for the standard end-of-combat payout when a ship
definition specifies none of its own ([[source-fandom-mantis-fight]]). The
`MANTIS_FIGHT` event in `events_mantis.xml` attaches no `autoReward` of its own
([[source-events-xml]]).

## Blue Options
None.

## Rewards & Risks
- Reward: default combat rewards only.
- Risk: an ordinary Mantis warship. Mantis ships in FTL characteristically favour
  boarding, so expect teleporter pressure rather than a pure gun duel — but note that is
  a property of the `SHIPS_MANTIS` blueprint pool, not of this event, and is not stated
  in the sources read here.

## Strategy Notes
- Nothing to decide. The only lever is whether you route into a Mantis sector at all,
  given it allocates 6–7 hostile beacons and this event is double-weighted within that
  pool ([[source-sector-data-xml]], [[source-events-xml]]).

## Related
- [[event-mantis-fight-near-sun]] — same fight, sun hazard, same `MANTIS_FIGHT` ship
- [[event-mantis-fight-choice]] — same ship, but you get the option to avoid it
- [[event-mantis-ship-attacking-civilian]] — an optional Mantis fight
- [[entity-mantis]]
- [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]],
  [[sector-civilian-sector]], [[sector-federation-space]]

## Open Questions
- [ ] Exact composition of the `MANTIS_FIGHT` ship (`events_ships.xml` entry not yet paged).
- [ ] Numeric values behind "default rewards".
- [ ] Whether all twenty text variants are equally weighted (the list implies yes, but the
      file states no weights).

## Notes on page joining
Twelve Fandom pages were matched to this event id by the ingest tooling, but only
`raw/wiki/mantis-fight.md` actually documents `MANTIS_FIGHT`. The other eleven name
different in-game ids in their own Notes sections — `WRECKAGE_EVENT`,
`NEBULA_MANTIS_CHOICE`, `ENGI_MANTIS_FIGHT`, `NEBULA_SLUG_MANTIS`, `NEBULA_MANTIS_FIGHT`,
`SLUG_MANTIS`, `ZOLTAN_MANTIS`, `ZOLTAN_BOARDERS_MANTIS`, `ROCK_MANTIS_HUNTER` — and
belong on their own pages. They were matched here only because they all fight the same
`MANTIS_FIGHT` ship. They are **not** used as sources for this page.

## Sources
- [[source-events-xml]] (per raw/gamedata/events_mantis.xml, raw/gamedata/newEvents.xml,
  raw/gamedata/dlcEventsOverwrite.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-mantis-fight]] (per raw/wiki/mantis-fight.md)
