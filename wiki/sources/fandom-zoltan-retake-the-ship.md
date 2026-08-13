---
id: source-fandom-zoltan-retake-the-ship
type: source
source_kind: wiki
raw: raw/wiki/zoltan-retake-the-ship.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [zoltan, augment-reward, crew-purchase]
---

# Fandom — "Zoltan retake the ship"

## Summary
The community wiki page for `ZOLTAN_LIFERAFT`. Retrieved via the MediaWiki API at
revision 73914. Essential here: the game file's choice 1 has **no outcome text and no
rewards** — everything that makes this event worthwhile lives in `events_ships.xml`, and
this page is the only source for it.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'ZOLTAN_LIFERAFT' in the
  datafiles."*
- **Supplies what the game files do not:** the entire post-fight branch structure.
  - Kill the crew with the hull intact → an **augment with high scrap** (the Zoltan's
    "enjoy the fruits of your labor" outcome). This is the intended reward for honouring
    his "you must not destroy my vessel" request.
  - Destroy the ship → `medium` scrap with resources, then the option to **hire him for
    40 scrap**.
- Confirms the 40-scrap hire resolves through `ZOLTAN_LIFERAFT_HIRE`: a haughty refusal
  (no charge) or an acceptance (−40 scrap, +1 Zoltan crew). The game file corroborates
  both entries ([[source-events-zoltan]]).
- Trivia: **the enemy ship's crew is composed entirely of one random race** — which
  determines how hard the crew-kill reward is to reach.
- Marks the enemy ship's surrender/escape behaviour as **needing verification**
  (`{{SurrenderEscape|verify}}`).
- Categorised `Augmentation reward opportunity`, `Crew purchase chance`.

## Events Covered
- [[event-zoltan-retake-the-ship]]

## Other Pages Touched
- [[entity-zoltan]], [[item-teleporter]]

## Reliability Notes
`medium`. States no game version, and self-flags the surrender/escape data as unverified.
The post-fight structure it supplies is unverifiable against the files ingested here.

## Contradictions Flagged
None. Where the page overlaps the game files (intro text, choice 2 text, the two
`ZOLTAN_LIFERAFT_HIRE` responses, the 40-scrap cost, the Zoltan crew reward) they agree
word for word.

## Links
- Source URL: https://ftl.fandom.com/wiki/Zoltan_retake_the_ship
- [[source-events-zoltan]], [[source-text-events-xml]]
