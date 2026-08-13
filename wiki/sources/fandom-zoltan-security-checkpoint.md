---
id: source-fandom-zoltan-security-checkpoint
type: source
source_kind: wiki
raw: raw/wiki/zoltan-security-checkpoint.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [zoltan, blue-option, crew-risk, boarding-risk]
---

# Fandom — "Zoltan security checkpoint"

## Summary
The community wiki page for `ZOLTAN_CREW_SCAN`. Retrieved via the MediaWiki API at
revision 74287 — the most recently edited page in this Zoltan batch. Its main
contribution is the post-fight reward tiers for the "refuse and fight" branch and a
numeric gloss on the blue-option fuel reward.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'ZOLTAN_CREW_SCAN' in the
  datafiles."*
- Maps the full `ZOLTAN_CREW_SCAN_LIST` tree including both sub-choices, and confirms the
  crew loss is **non-recoverable by Clone Bay**, quoting the failure text.
- **Supplies what the game files do not:** the "refuse and fight" reward tiers —
  `low` scrap with resources if the ship is destroyed, `medium` if you kill the crew.
  These live in `events_ships.xml`, which is not ingested here.
- Glosses `autoReward level="MED"` `fuel_only` as **2–4 fuel** for both blue options.
- Confirms the Weapon Control halving rounds **down** against the player.
- Trivia: neither `ZOLTAN_SHIP` (choice 1) nor `ZOLTAN_CREW_SCAN` (choice 2b) has
  surrender or escape values specified in `events_ships.xml`.
- Categorised `Crew loss risk`, `Clone Bay failed revival`, `Boarding risk`,
  `System malfunction risk`, `Fuel reward opportunity`, `Fights with Default Rewards`.

## Events Covered
- [[event-zoltan-security-checkpoint]]

## Other Pages Touched
- [[entity-zoltan]], [[entity-slugs]], [[item-mind-control]], [[item-clone-bay]]

## Reliability Notes
`medium`. States no game version. The **2–4 fuel** figure is the wiki's own gloss on
`MED` and is not stated in the game files — treat it as a community estimate, not data.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** intro wording.
> Fandom: *"**Traveling** vessel"*. Game files: *"**Travelling** vessel"*
> ([[source-text-events-xml]]).

> ⚠️ **CONTRADICTION:** clean-pass outcome wording.
> Fandom: *"After a few moments of uncertainty, your crew is allowed to pass."*
> Game files: *"The Zoltan security staff board your ship and scan the crew's faces into
> a computer. After a few tense moments of uncertainty they allow your ship to pass."*
> ([[source-text-events-xml]]).
> Both recorded on [[event-zoltan-security-checkpoint]]. Game files trusted; the second
> looks like an abridged paraphrase rather than a version difference.

## Links
- Source URL: https://ftl.fandom.com/wiki/Zoltan_security_checkpoint
- [[source-events-zoltan]], [[source-text-events-xml]]
