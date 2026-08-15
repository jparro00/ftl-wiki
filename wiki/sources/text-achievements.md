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
- This file covers **achievements only** — `ACH_*_name`, `ACH_*_shortname`, `ACH_*_desc`.
  Ship-victory and per-ship challenge achievements are all here.
- It contains **no unlock-condition data**: the descriptions state conditions in prose for
  the player to read, and nothing links an achievement to a ship unlock mechanically. That
  is the same gap [[source-achievements]] records structurally.

  > **Correction (lint, 2026-08-13).** This page previously claimed the ship-unlock hint
  > strings (`ship_PLAYER_SHIP_*_unlock`) live here, and that the unlock chains cite it for
  > them. Both are false. Those 9 strings are in **`text_blueprints.xml`**
  > ([[source-text-blueprints]]) — `grep` finds `ship_PLAYER_SHIP_*_unlock` in
  > `blueprints.xml`, `dlcBlueprints.xml` and `text_blueprints.xml` and **nowhere in this
  > file**. No chain page ever cited this page, which is why the false claim went unnoticed:
  > the page was an orphan. The conclusion those strings support — that `ENGI_UNLOCK_1→4`
  > awards the **Stealth** Cruiser, per *"This ship is being built near the Engi
  > homeworlds…"* — is unaffected and correctly sourced on
  > [[chain-stealth-cruiser-unlock]]; only the file attribution was wrong.

## Events Covered
None — this is a lookup table, and no event page depends on it. Its relevance to this wiki
is negative evidence: the achievement text is where an alternative ship-unlock route *would*
be stated if one were recorded in the data, and it is not.

## Contradictions Flagged
None internal. Note that `achievements.xml` contains **no** unlock-condition entries, so
Fandom's claims about alternative ship-unlock routes (e.g. unlocking the Rock Cruiser by
winning with the Slug Cruiser) cannot be verified from the game data and are recorded as
Fandom-only on the affected chain pages — see [[chain-rock-cruiser-unlock]].

## Links
- [[source-achievements]] — the structural half of the pair
- [[source-text-blueprints]] — the equivalent string table for items and ships
