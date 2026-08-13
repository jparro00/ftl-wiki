---
id: source-text-achievements
type: source
source_kind: gamedata
raw: raw/gamedata/text_achievements.xml
game_version: ae
ingested: 2026-08-09
reliability: high
tags: [strings]
---

# text_achievements.xml

## Summary
Display names and descriptions for every achievement, keyed by id. `achievements.xml`
carries only the ids and structure; this file supplies the human-readable text, including
the ship-unlock hint strings.

## Key Takeaways
- Format is `<text name="ID">prose</text>`, the same convention as
  [[source-text-events-xml]] and [[source-text-blueprints]].
- The **ship-unlock hint strings** live here (`ship_PLAYER_SHIP_*_unlock`) and are the
  evidence that settled which quest chain unlocks which ship. They are what established
  that `ENGI_UNLOCK_1→4` awards the **Stealth** Cruiser, not the Engi Cruiser — see
  [[chain-stealth-cruiser-unlock]].
- The Engi Cruiser's hint describes an achievement condition ("get to the 5th sector with
  any layout of the Kestrel"), not an event, which is why no `<unlockShip>` in the game
  data references its id.

## Events Covered
None directly — this is a lookup table. It is cited by the unlock chains
([[chain-stealth-cruiser-unlock]], [[chain-rock-cruiser-unlock]],
[[chain-mantis-cruiser-unlock]], [[chain-slug-cruiser-unlock]],
[[chain-zoltan-cruiser-unlock]]) and by [[source-achievements]].

## Contradictions Flagged
None internal. Note that `achievements.xml` contains **no** unlock-condition entries, so
Fandom's claims about alternative ship-unlock routes (e.g. unlocking the Rock Cruiser by
winning with the Slug Cruiser) cannot be verified from the game data and are recorded as
Fandom-only on the affected chain pages.

## Links
- [[source-achievements]] — the structural half of the pair
- [[source-text-blueprints]] — the equivalent string table for items and ships
