---
id: source-fandom-slug-home-nebula-surrender
type: source
source_kind: wiki
raw: raw/wiki/slug-home-nebula-surrender.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [slug, ship-unlock, quest-marker]
---

# Fandom — "Slug Home Nebula surrender"

## Summary
The community wiki page for `NEBULA_SLUG_FIGHT_UNLOCK`, retrieved at revision 74817. The
richest source in this batch: it assembles the whole Slug Cruiser unlock chain — the
disguised fight, the surrender branch, the quest marker, and both ships at the platform —
into one narrative, and includes a commented-out "Code Trivia" section quoting the raw XML.

## Key Takeaways
- Names the in-game id in Trivia: *"This event is called 'NEBULA_SLUG_FIGHT_UNLOCK' in the
  datafiles."*, and names `JELLY_UNLOCK1` and `SLUG_UNLOCK_SURRENDER` in its reference
  notes.
- **The unlock is otherwise indistinguishable from [[event-slug-fight-in-nebula]]** — same
  intro text, same surrender text. The only tell is that this ship offers a surrender at
  all.
- Reads `<surrender chance="0" …>` as a **100% chance** of the surrender offer at 30–40%
  hull, and applies the same reading to `QUEST_SLUG_PIRATE_TRAP1`.
- Notes the escape roll (50%) sits in the same hull band as the surrender, so a ship that
  tries to run first needs more damage before it offers to surrender.
- Documents the two branches at the platform: the assault ship (`JELLY_UNLOCK2`,
  Slug Assault class) gives high scrap but **no unlock**; the interceptor (`JELLY_UNLOCK3`,
  Slug Interceptor class) gives the unlock, high scrap and Slug Repair Gel, and escapes on a
  35-second timer.
- Names the blue options at `SLUG_UNLOCK_2`: **Slug crew** and **Improved Sensors (2+)**.
- Records a bug: if the `standard` reward roll produces an augment, it **overwrites** the
  guaranteed Slug Repair Gel.
- Notes the Slug Cruiser can also be unlocked by winning with the Mantis Cruiser.
- Categories include `Ship_Unlocking_Events`, `Ship surrender Events`,
  `Events with Quest Markers`, `Ship escape Events`.

## Events Covered
- [[event-slug-home-nebula-surrender]]
- (context for [[event-slug-unlock-surrender]], [[event-slug-unlock-1]])

## Other Pages Touched
- [[chain-slug-cruiser-unlock]], [[item-anti-bio-beam]], [[item-slug-repair-gel]],
  [[sector-slug-home-nebula]], [[entity-slugs]]

## Reliability Notes
`medium`, but unusually well-evidenced: the page quotes the game XML directly in a
commented-out section, so its claims can be checked against
[[source-events-slug]] / [[source-events-ships]] line by line.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** `<surrender chance="0" …>` read as a 100% surrender chance. The
> files say `0`. Fandom applies the same reading consistently across two ships, and an
> unlock that never surrendered would be unreachable — so the reading is probably right and
> the attribute's semantics are simply not what the name suggests. Recorded on
> [[event-slug-home-nebula-surrender]] and [[event-slug-comm-tapping]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Slug_Home_Nebula_surrender
- [[source-events-slug]], [[source-events-ships]], [[source-sector-data-xml]]
