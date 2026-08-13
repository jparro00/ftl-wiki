---
id: source-fandom-zoltan-great-eye
type: source
source_kind: wiki
raw: raw/wiki/zoltan-great-eye.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [zoltan, nebula, crew-risk]
---

# Fandom — "Zoltan Great Eye"

## Summary
The community wiki page for `NEBULA_ZOLTAN_EYE`. Retrieved via the MediaWiki API at
revision 73910. Supplies the four outcomes of the "pull in closer" list in plain
language, plus the Clone Bay failure text that the game files reference only by id.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'NEBULA_ZOLTAN_EYE' in the
  datafiles."* This is the join key to [[source-events-zoltan]].
- Lists all four `NEBULA_ZOLTAN_EYE_LIST` results and confirms the crew loss is
  **non-recoverable by Clone Bay**, quoting the failure text.
- Confirms `<weapon name="BOMB_HEAL"/>` resolves to **Healing Burst**
  ([[item-healing-burst]]) — the game file gives only the blueprint name.
- Confirms the fight outcome pays **default rewards**.
- Locations template: Zoltan Controlled Sector and Zoltan Homeworlds, `nebula=true`,
  `unique=true`, Long-Ranged Scanners reading `noship+nebula`.
- Trivia: the monolith is likely a reference to the monolith in the "Eye" of Iapetus in
  Arthur C. Clarke's *2001: A Space Odyssey*.
- Categorised `Random_Events`, `Unique_Events`, plus `Crew loss risk`,
  `Clone Bay failed revival`, `Fights with Default Rewards`, `Weapon reward chance`.

## Events Covered
- [[event-zoltan-great-eye]]

## Other Pages Touched
- [[item-healing-burst]], [[item-clone-bay]], [[entity-zoltan]]

## Reliability Notes
`medium`. States no game version, so `game_version` is `unknown` — not `ae`. Gives no
odds for the four-way split, matching the game files' silence.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** crew-loss text spelling.
> Fandom: *"a kaleidoscope of **colours** fills the **view-screen**"*.
> Game files: *"a kaleidoscope of **colors** fills the **viewscreen**"*
> ([[source-text-events-xml]]).
> Recorded on [[event-zoltan-great-eye]]. Game files trusted.

## Links
- Source URL: https://ftl.fandom.com/wiki/Zoltan_Great_Eye
- [[source-events-zoltan]], [[source-text-events-xml]]
