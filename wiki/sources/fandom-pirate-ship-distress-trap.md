---
id: source-fandom-pirate-ship-distress-trap
type: source
source_kind: wiki
raw: raw/wiki/pirate-ship-distress-trap.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [combat, pirate, distress]
---

# Fandom — "Pirate ship distress trap"

## Summary
The community wiki page for the event the game files call `TRAP_BEACON`. Retrieved via the
MediaWiki API at revision 73775. The event has no choices, so the page is short: four intro
texts, one fight, default rewards.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'TRAP_BEACON' in the
  datafiles."* This is the join key.
- All four `TRAP_BEACON_TEXT` variants are transcribed and match `text_events.xml` word for
  word.
- Confirms the outcome is a single forced fight against a Pirate ship with **default
  rewards** — the label for the `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT` blocks on the
  `PIRATE` ship definition ([[source-events-ships]]).
- Lists **sixteen** sectors, `distress=true`, `unique=true` — the latter two consistent
  with the XML (`<distressBeacon/>`, `unique="true"`) and with the nine distress pools it belongs
  to.
- Sets `LRSmap=ship`, i.e. the Long-Range Scanner shows a ship at this beacon. This is the
  only pre-jump warning a player gets, and it appears in no game file here.
- Categorised: `Random_Events`, `Unique_Events`, `Fights with Default Rewards`,
  `Pirate ship fights`.

## Events Covered
- [[event-pirate-ship-distress-trap]]

## Other Pages Touched
- [[entity-pirates]]

## Reliability Notes
`medium`. No game version stated, so `game_version` is `unknown`. `TRAP_BEACON` carries no
DLC markers and `DISTRESS_BEACON` is not redefined in `dlcEventsOverwrite.xml`, so version
drift is unlikely to affect anything on this page.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** [[sector-federation-space]] is missing from the page's
> `{{Locations}}` template.
> Fandom lists sixteen sectors. The game files put the event in the generic `DISTRESS_BEACON`
> pool ([[source-newevents]]), which `STANDARD_SPACE` allocates at
> `min="1" max="2"` ([[source-sector-data-xml]]) — so it can appear in
> Federation Space. Recorded on [[event-pirate-ship-distress-trap]]. Game files trusted
> (`high` vs `medium`); this looks like a Fandom convention/omission, not a version
> difference — no DLC marker is involved.

## Links
- Source URL: https://ftl.fandom.com/wiki/Pirate_ship_distress_trap
- [[source-events-xml]], [[source-text-events-xml]], [[source-events-ships]],
  [[source-newevents]], [[source-sector-data-xml]]
</content>
