---
id: source-fandom-random-events
type: source
source_kind: wiki
raw: raw/wiki/random-events.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-13
reliability: medium
tags: [index, taxonomy, mechanics, quests, uniqueness, lrs]
---

# Fandom — "Random Events"

## Summary
The Fandom wiki's **hub page** for events, retrieved via the MediaWiki API at revision 74697.
Almost all of its body is a list of category links — it is a table of contents, not an event
page — but the prose wrapped around that list carries four mechanics claims that appear
nowhere else in this wiki's sources, and one taxonomy that explains the field names the other
290 Fandom pages have been quoting all along.

## Key Takeaways

- **Quest beacon placement.** *"Quest beacons will normally be placed in the current sector.
  However, if you don't have many jumps left, the game will push the quest into the next
  sector instead. If this happens in sector 7, the quest will be 'cancelled', because quests
  are not allowed in sector 8."* Filed as [[concept-quest-beacon-placement]]; the sector-8
  half is corroborated by `sector_data.xml` (§Contradictions below).
- **Unique vs non-unique.** *"Events that can occur only once per current sector (unique) or
  multiple times per current sector (non-unique)"*, with the parenthetical that ship-unlocking
  events *"can occur only once per game run"*. This is a **per-sector** reading of
  `unique="true"`, and it conflicts with [[concept-event-tree-grammar]]'s per-run reading.
  Filed and both sides recorded at [[concept-event-uniqueness]].
- **What Long-Ranged Scanners actually report.** Events are categorised as *"marked by
  Long-Ranged Scanners or map reveal as having ship presence or having no ship presence at a
  beacon"* — with two caveats stated outright: *"'no ship presence' does not guarantee absence
  of a hostile ship, including a potential forced fight"* and *"'possible ship detected' can
  point at the presence of a friendly or neutral ship"*. This is the `LRSmap` field the other
  Fandom pages carry, and it partly answers the standing open question on
  [[item-long-ranged-scanners]].
- **Some distress events are unreachable by bug.** *"some other events were meant to occur at
  a distress beacon, but they won't due to coding errors — these events are not included in the
  category"*. Names none of them. Recorded on [[concept-sector-event-allocation]] as a third
  meaning of "unreachable".
- **Event text is verbatim game data.** *"DO NOT ALTER the events texts! These come from the
  game files and must contain typos as they are seen in the actual game"*, usually marked
  `sic!`. This is the community wiki stating that its quoted prose is copied from
  `text_events.xml` — which is why quoted text on Fandom pages has matched
  [[source-text-events-xml]] on every event ingested so far.
- **Quests fire on jump.** *"Random events are initiated by jumping to another system"* — every
  jump rolls for a battle, a local interaction, or nothing.
- **Cut content is excluded.** Events that do not appear in unmodified FTL *"do not have
  individual article pages and are not part of any category"* — so absence of a Fandom page is
  evidence an event is unreachable, not evidence it does not exist. Relevant to `HOSTILE2` /
  `NEUTRAL2` on [[concept-sector-event-allocation]].
- **The category taxonomy itself**: by sector (19 sectors), global (exit beacon, filler, nebula
  filler, out of fuel), hazard (asteroid field, nebula, plasma storm, pulsar, red giant),
  distress, blue options, ship-unlocking, unique/non-unique, ship-presence, fights by enemy
  type, risks-and-hazards, rewards-and-opportunities, identical-rewards. These are the
  categories the per-event Fandom pages are filed under.
- Points at an external non-wiki single-page dump, `hugomg.github.io/ftl-cheatsheet` — not
  retrieved, not a source here.

## Events Covered
None individually — the page names no event. Its payload is mechanics and taxonomy.

## Other Pages Touched
- [[concept-quest-beacon-placement]] — new, from this source
- [[concept-event-uniqueness]] — new, from this source
- [[concept-sector-event-allocation]] — the bugged-distress-events note
- [[item-long-ranged-scanners]] — what the augment's map annotation means
- [[concept-stores]] — confirms the meaning of the `LRSmap=noship` field it already cites
- [[concept-event-tree-grammar]] — contradicted on `unique="true"`

## Reliability Notes
`medium`. No game version stated anywhere on the page; it describes categories that include
Advanced Edition sectors (Abandoned Sector, Lanius events), so it is written from an AE
standpoint, but that is inference and the frontmatter stays `unknown`. It is a hub page
maintained by many hands — its prose claims about engine behaviour are unsourced community
knowledge, not datamined, and the two that could be checked against `raw/gamedata/` both held
up.

## Contradictions Flagged

> ⚠️ **CONTRADICTION:** what `unique="true"` scopes to.
> - **This source:** once per **current sector** — *"Events that can occur only once per
>   current sector (unique)"*, with ship-unlock events singled out as the exception that is
>   once per **run**. ([[source-fandom-random-events]] per `raw/wiki/random-events.md`)
> - **[[concept-event-tree-grammar]]:** once per **run** — *"`unique="true"` … means the
>   encounter cannot repeat in a run"*, asserted from the attribute's presence in the files.
>   ([[source-events-xml]])
> - **[[concept-stores]]** independently reasons the per-sector way: *"an event marked
>   `unique="true"` can fill only one beacon per sector, so the sectors that guarantee two or
>   three stores could not do so if their store event were unique."*
> - **Not a version difference** — the attribute is present and identical in both the vanilla
>   and DLC event files.
> - **Where I'd bet:** the per-sector reading. Two independent lines of argument reach it, and
>   the files contain a *second* `unique` attribute — `<sectorDescription unique="true">`, on 8
>   of 21 sectors — whose meaning is unambiguously once-per-run, which is exactly the
>   distinction you would need two scopes to express. Neither reading is datamined; the game
>   files carry the flag without documenting it. Full argument at
>   [[concept-event-uniqueness]].

**Corroborated, not contradicted:** the claim that quests are impossible in sector 8. The
`FINAL` `<sectorDescription>` in `raw/gamedata/sector_data.xml` allocates only `STORE`,
`BOSS_REPAIR_STATION`, `BOSS_HOSTILE` and `BOSS_NEUTRAL` — no list carrying a `<quest>` tag —
so the data agrees with the claim even though it does not state it.
([[source-sector-data-xml]])

## Links
- Source URL: https://ftl.fandom.com/wiki/Random_Events (revision 74697, retrieved 2026-08-09)
- [[source-sector-data-xml]], [[source-events-xml]], [[source-text-events-xml]]
