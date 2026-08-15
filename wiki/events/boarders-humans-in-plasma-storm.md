---
id: event-boarders-humans-in-plasma-storm
type: event
event_name: STORM_BOARDING
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: nebula
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [plasma-storm, boarding, crew-risk, no-choice, unique, partially-disabled]
---

# Boarders: Humans in plasma storm — `STORM_BOARDING`

## Summary
Salvage interrupted by a boarding party. Unlike its nebula twin
[[event-boarders-humans-in-nebula]], this one **pays** — `autoReward level="MED"` with the
`standard` payload lands alongside the intruders. It also has the messiest availability
history in the file: two of the four lists that reference it have the entry commented out.

## Trigger & Where It Appears
- Beacon: **plasma storm** (`<environment type="storm"/>`).
- `unique="true"` — once per run.
- Marked `<!--DLC - Kinda-->` in the XML ([[source-events-nebula]]).
- **Live references:**
  - `NEBULA` (`raw/gamedata/newEvents.xml`), where the entry carries the comment
    *"DLC re-added - was removed previously"* ([[source-newevents]]) — reaching
    [[sector-federation-space]] (0–4) and [[sector-civilian-sector]] (0–8).
  - `STORM_SLUG` (`raw/gamedata/events_slug.xml`), allocated 1–3 per Slug sector
    ([[source-events-slug]], [[source-sector-data-xml]]) — reaching
    [[sector-slug-controlled-nebula]] and [[sector-slug-home-nebula]].
- **Disabled references:** the entry is commented out in `NEBULA_HOSTILE`
  (`<!--<event load="STORM_BOARDING"/>-->`, [[source-events-nebula]]) and in
  `NEBULA_PIRATE` ([[source-events-pirate]]). So it does **not** reach
  [[sector-uncharted-nebula]] or [[sector-pirate-controlled-sector]] through those pools,
  even though every sibling storm event does.
- Long-range scanners show no ship ([[source-fandom-boarders-humans-in-plasma-storm]]).

## Text
> You find two heavily damaged ships floating nearby, the remains of a battle. You begin to
> harvest some usable debris when you hear the sounds of someone beaming aboard followed by
> the shouts of a boarding party.

(`event_STORM_BOARDING_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event has no `<choice>` elements)_ | — | `<boarders min="3" max="4" class="human"/>` — 3–4 human intruders — **and** `autoReward level="MED"` payload `standard`. | 100% |

The event body is four elements: text, environment, boarders, autoReward
([[source-events-nebula]]).

## Blue Options
None.

## Rewards & Risks
- **Reward: `MED` / `standard`, unconditional** — you get it whether the boarding goes well
  or badly. This makes it the only boarding event in the file with a positive expected
  material value.
- Risk: 3–4 boarders, one more than [[event-boarders-humans-in-nebula]]'s floor, fought in
  a plasma storm.
- **Slug-sector pursuit trap:** [[source-fandom-boarders-humans-in-plasma-storm]] notes
  that when reached via `STORM_SLUG` the beacon can sit **outside** the nebula region of
  the map. The environment tag still gives you a plasma storm, but you pay **full** fleet
  pursuit on the jump out instead of the reduced nebula rate. That is a real cost the event
  itself does not express, and it applies equally to
  [[event-rebel-fight-in-plasma-storm]].

## Strategy Notes
- Nothing to decide. As with the other boarding event, only crew count, Medbay/Clone Bay
  and door control matter — weapons are irrelevant.
- The scrap arrives immediately, so even a costly repel still leaves you materially ahead
  of the nebula boarding event, which pays nothing.

## Related
- [[event-boarders-humans-in-nebula]] — 2–4 boarders, nebula, **no reward**
- [[event-rebel-fight-in-plasma-storm]] — shares the `STORM_SLUG` pursuit note
- [[event-plasma-storm-incapacitated-ships]] — the other "salvage goes wrong" storm event
- [[sector-slug-home-nebula]], [[sector-slug-controlled-nebula]],
  [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Why the entry is live in `NEBULA` and `STORM_SLUG` but commented out in
      `NEBULA_HOSTILE` and `NEBULA_PIRATE` — the files give no reason beyond
      "was removed previously".
- [ ] Whether the `<!--DLC - Kinda-->` note means it is AE-only, vanilla-only, or simply
      re-enabled in AE. `version: ae` here reflects that AE re-added it, not that vanilla
      lacked it.
- [ ] The exact nebula fleet-pursuit rate the Fandom note compares against (it says 80%).

## Sources
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-boarders-humans-in-plasma-storm]] (per raw/wiki/boarders-humans-in-plasma-storm.md)
