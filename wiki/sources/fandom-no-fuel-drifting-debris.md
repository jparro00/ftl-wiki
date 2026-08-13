---
id: source-fandom-no-fuel-drifting-debris
type: source
source_kind: wiki
raw: raw/wiki/no-fuel-drifting-debris.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [out-of-fuel, rock, crew-risk]
---

# Fandom — "No fuel: drifting debris"

## Summary
Community wiki page for `FUEL_OFF_ROCK_WRECK`, retrieved at revision 73103. Documents the
away-team branch including the crew-hostage outcome and the Clone Bay failure.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'FUEL_OFF_ROCK_WRECK' in the datafiles."*
- Marks it `{{Locations|outoffuel=distressoff}}`, matching the XML.
- Reads `autoReward level="MED"` fuel_only as **2–4 fuel** and the ransom as **25–40 scrap**.
- Explicitly categorises the Clone Bay result as a **failed revival** — the refused-ransom
  crew member is gone permanently, matching `<clone>false</clone>` in the XML.
- Categorises the event under *Beacon Map reveal chance* for the `<reveal_map/>` outcome.

## Events Covered
- [[event-no-fuel-drifting-debris]]

## Other Pages Touched
- [[item-lifeform-scanner]], [[entity-rock-men]]

## Reliability Notes
`medium`, `game_version: unknown`. It presents the Lifeform Scanner blue option without
noting it is AE-only — the `<!--DLC-->` annotation is visible only in the game file
([[source-events-fuel]]).

## Contradictions Flagged
None mechanical. Version nuance recorded on [[event-no-fuel-drifting-debris]]: the blue
option does not exist in vanilla.

## Links
- Source URL: https://ftl.fandom.com/wiki/No_fuel:_drifting_debris
- [[source-events-fuel]], [[source-text-events-xml]]
