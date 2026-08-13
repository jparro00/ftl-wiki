---
id: source-fandom-zoltan-odd-moon
type: source
source_kind: wiki
raw: raw/wiki/zoltan-odd-moon.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [zoltan, blue-option, crew-reward, weapon-reward]
---

# Fandom — "Zoltan odd moon"

## Summary
The community wiki page for `ZOLTAN_ODD_MOON`. Retrieved via the MediaWiki API at
revision 73911. It presents the nested `ZOLTAN_ODD_MOON_CHECK` and
`ZOLTAN_ODD_MOON_EXPLOSION` lists as one readable tree and names the blue option's
requirement in player-facing terms.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'ZOLTAN_ODD_MOON' in the
  datafiles."*
- Translates `req="BOARDER"` into **Boarding Drone**, and confirms it consumes **1 drone
  part** for a guaranteed **Zoltan crew member** — the best outcome available.
- Shows the missile cost on the explosives sub-choice. (The game files deduct the missile
  inside each `ZOLTAN_ODD_MOON_EXPLOSION` entry instead, so all three results cost 1
  missile — same net effect, different placement.)
- Confirms no branch of this event leads to combat or damage.
- Locations template: both Zoltan sectors, `unique=true`, Long-Ranged Scanners `noship`.
- Categorised `Weapon reward chance`, `Crew reward opportunity`, `Missiles use Events`,
  `Drone Parts use Events`.

## Events Covered
- [[event-zoltan-odd-moon]]

## Other Pages Touched
- [[item-boarding-drone]], [[entity-zoltan]]

## Reliability Notes
`medium`. States no game version. Presents the `ZOLTAN_ODD_MOON_CHECK` entries in a
different order from the game file and gives no odds for either list, matching the game
files' silence.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** `ZOLTAN_ODD_MOON_EXPLOSION_3` wording.
> Fandom: *"Everyone inside is dead; Mantis clearly came through here recently… You take
> one of **the** better examples back to your ship."*
> Game files: *"Everyone inside is dead; **some** Mantis clearly came through here
> recently… You take one of **their** better examples back to your ship."*
> ([[source-text-events-xml]]).
> Recorded on [[event-zoltan-odd-moon]]. Game files trusted.

## Links
- Source URL: https://ftl.fandom.com/wiki/Zoltan_odd_moon
- [[source-events-zoltan]], [[source-text-events-xml]]
