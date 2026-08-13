---
id: source-fandom-lanius-powered-down-ship
type: source
source_kind: wiki
raw: raw/wiki/lanius-powered-down-ship.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [lanius, blue-option, piloting, advanced-edition]
---

# Fandom — "Lanius powered-down ship"

## Summary
The community wiki page for `LANIUS_DORMANT_EVENT`. Retrieved at revision 74230. Maps the
three top-level choices and the shared "Investigate the vessel" sub-event with its two
blue options.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'LANIUS_DORMANT_EVENT' in the
  datafiles."*
- Locations: Abandoned Sector, `LRSmap=ship`, `unique=true`.
- All fights are with `LANIUS_SHIP` and pay **default Lanius rewards**.
- Expands `autoReward level="MED">stuff` on the Lanius-crew blue option into a tooltip:
  *fuel 2-4, missiles 2-4, drone parts 1* — i.e. "resources with some scrap", distinct
  from the "standard" payout on the Piloting blue option.
- Categories: `Advanced Edition Content Events`, `Fights with Default Rewards (Lanius)`.

## Events Covered
- [[event-lanius-powered-down-ship]]

## Other Pages Touched
- [[entity-lanius]], [[sector-abandoned-sector]]

## Reliability Notes
`medium`. Structure matches the XML. The "stuff" reward breakdown is Fandom's own
expansion of the reward table and is not stated in `raw/gamedata/`.

## Contradictions Flagged
Wording only: Fandom's choice-1 result reads "awaken the Lanius from hibernation" where
`event_LANIUS_DORMANT_EVENT_c1_text` reads "awaken the Lanius **crew** from hibernation".

## Links
- Source URL: https://ftl.fandom.com/wiki/Lanius_powered-down_ship
- [[source-dlcevents-anaerobic]], [[source-text-events-xml]]
