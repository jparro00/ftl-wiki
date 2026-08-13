---
id: source-fandom-deactivated-auto-ship
type: source
source_kind: wiki
raw: raw/wiki/deactivated-auto-ship.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rebel, auto-ship, filler, blue-option, map-reveal]
---

# Fandom — "Deactivated Auto-ship"

## Summary
The community wiki page for `BROKEN_REBEL_DRONE`. Retrieved via the MediaWiki API at
revision 73651. Transcribes the full nested tree including the Sensors sub-choice.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'BROKEN_REBEL_DRONE' in the
  datafiles."*
- Locations: Abandoned Sector, Engi Controlled Sector, Engi Homeworlds, Mantis Controlled
  Sector, Mantis Homeworlds, Rebel Controlled Sector, Rebel Stronghold, Slug Controlled
  Nebula, Slug Home Nebula, Zoltan Controlled Sector, Zoltan Homeworlds, with
  `alsooccur=filler`, `LRSmap=ship`, `unique=true`. The Zoltan entries are notable: the
  `NEUTRAL_ZOLTAN` reference to this event is **commented out** in `events_zoltan.xml`. It
  can still reach Zoltan space through the generic `NEUTRAL` / `OVERRIDE_NEUTRAL` filler
  lists.
- Documents the **Sensors level 3** blue option and, correctly, that it does **not**
  guarantee the good outcome — half the time it warns you the ship is on standby and gives
  you a Yes/No sub-choice that re-rolls the same table.
- Rewards recorded as: choice 2 → low scrap *(scrap only)*; the download success → low scrap
  with resources + map reveal; the fight → medium scrap with resources. All match the
  `autoReward` levels and types in the file.
- Transcribes the reactivation text as *"You accidentally reactivate the ships AI. Its
  weapons **and shields** immediately go online"* — the current game file omits "and
  shields".
- Categorised `Random_Events`, `Unique_Events`, `Filler_Events`,
  `Beacon Map reveal chance`, `Auto-ship fights`.

## Events Covered
- [[event-deactivated-auto-ship]]

## Other Pages Touched
- [[item-sensors]], [[event-auto-ship-fight]], [[concept-rebel-fleet-advance]]

## Reliability Notes
`medium`. Version unstated. Structurally faithful, including the nested Yes/No branch that
the batch preview data drops. The "and shields" phrase is the only textual divergence.

## Contradictions Flagged
- Reactivation text wording — recorded as an open question on
  [[event-deactivated-auto-ship]].
- Zoltan sector reach vs the commented-out `events_zoltan.xml` entry — recorded on
  [[event-deactivated-auto-ship]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Deactivated_Auto-ship
- [[source-events-rebel]], [[source-events-ships]], [[source-events-zoltan]],
  [[source-text-events-xml]]
