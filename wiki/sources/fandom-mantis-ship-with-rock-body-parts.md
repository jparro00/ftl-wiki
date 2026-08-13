---
id: source-fandom-mantis-ship-with-rock-body-parts
type: source
source_kind: wiki
raw: raw/wiki/mantis-ship-with-rock-body-parts.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rock, mantis, blue-option]
---

# Fandom — "Mantis ship with Rock body parts"

## Summary
Community wiki page for `ROCK_MANTIS_HUNTER`, retrieved via the MediaWiki API at revision
74265. Four choices with outcomes, and — most usefully — a correction of the misleading
in-game label on the ramming option.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'ROCK_MANTIS_HUNTER' in the
  datafiles."*
- Locations: Rock Controlled Sector, Rock Homeworlds; `LRSmap=ship`, `unique=true`.
- **Resolves the "(Rock Ship)" label**: annotates the option
  `{{Blue Option|Rock Ship|Ram the bastards.|shortreq=Rock Plating}} (Requires Rock
  Plating)`. The game files show `req="ROCK_ARMOR"`, an augment id — Fandom's reading is
  the correct one and is the reason [[event-mantis-ship-with-rock-body-parts]] treats the
  gate as the augment.
- Confirms the ram branch disables the enemy's **engines** and that all fighting branches
  give the same default rewards — i.e. the Rock Crew option is purely cosmetic.
- Confirms `MANTIS_FIGHT` has no surrender and no escape.
- **Behavioural note not in the game files:** *"Even if you're in a Rock Cruiser when using
  the 'Ignore them' option, the Mantis take no interest in your ship."* Rules out an
  intuitive-but-wrong assumption that a Rock hull provokes the hunter.
- Categorised `Fights with Default Rewards` and `Enemy system malfunction Events`.

## Events Covered
- [[event-mantis-ship-with-rock-body-parts]]

## Other Pages Touched
- [[item-rock-plating]], [[item-rock-crew]], [[ship-rock-cruiser]], [[entity-mantis]]

## Reliability Notes
`medium`. No version stated. On the one point where it disagrees with a literal reading of
the game files (the "(Rock Ship)" label), the game files' own `req` attribute supports
Fandom.

## Contradictions Flagged
> ⚠️ Choice label *"(Rock Ship)"* vs. gate `req="ROCK_ARMOR"`. Recorded on
> [[event-mantis-ship-with-rock-body-parts]]; resolved in favour of the augment reading.

## Links
- Source URL: https://ftl.fandom.com/wiki/Mantis_ship_with_Rock_body_parts
- [[source-events-rock]], [[source-text-events-xml]]
