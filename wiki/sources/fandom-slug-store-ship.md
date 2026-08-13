---
id: source-fandom-slug-store-ship
type: source
source_kind: wiki
raw: raw/wiki/slug-store-ship.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [slug, boarding, store, bug]
---

# Fandom — "Slug store ship"

## Summary
Community wiki page for `NEBULA_SLUG_FAKE_STORE`, retrieved at revision 74286. Reconstructs
the full nested disclaimer chain — which the batch extract flattens away — and reports a
long-standing engine bug in one branch.

## Key Takeaways
- Names the in-game id in Trivia: *"This event is called 'NEBULA_SLUG_FAKE_STORE' in the
  datafiles."*
- Lays out the complete four-deep choice tree, including both places you can back out and
  the `req="slug"` blue option on the second disclaimer page.
- Confirms the three `_LIST` outcomes (5 fuel + store; 1 boarder + weapons offline;
  2 boarders) and the two `_LEAVING` outcomes.
- **Reports an engine bug** in an HTML comment: the entry that should load
  `JELLY_STATUS_WEAPONS` does not, so the fight is against a plain Slug ship at default
  rewards, and *"Weapon Control stays offline after the fight, and returns to normal after
  an FTL jump"*. Says the issue *"persists from at least 2015 till 2022+ game versions"* and
  quotes the exact XML.
- States the `JELLY` ship's rolls: 50% surrender and 50% escape at 30–40% hull.
- Categories: `Fights with Default Rewards`, `Boarding risk`, `System malfunction risk`,
  `Store Opening chance`, `Fuel reward chance`.

## Events Covered
- [[event-slug-store-ship]]

## Other Pages Touched
- [[event-store-in-nebula-slug]], [[entity-slugs]]

## Reliability Notes
`medium`, but this page is unusually careful — it quotes the XML it disagrees with rather
than paraphrasing, which makes the bug claim checkable in play.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** `NEBULA_SLUG_FAKE_STORE_LIST` entry 2. The files load
> `JELLY_STATUS_WEAPONS` (which would pay `HIGH standard`); Fandom reports the load silently
> fails and the fight is a default-rewards `JELLY`. This is a claimed **engine bug**, not a
> data disagreement — both sides quote the same XML. Recorded on [[event-slug-store-ship]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Slug_store_ship
- [[source-events-slug]], [[source-events-ships]], [[source-text-events-xml]]
