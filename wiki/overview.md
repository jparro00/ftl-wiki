# Coverage Overview

A snapshot of what this wiki knows about FTL's events. Updated during `lint` or on
request. This is a summary for quick orientation — the canonical detail lives in the
individual event, chain, sector, entity, item and concept pages.

## Scope
The event pool of **FTL: Faster Than Light, Advanced Edition (1.6.x)** — beacon
encounters, their choices and outcomes, blue options, quest chains, and which sectors
they appear in. Two source layers: the game's own XML extracted from the installed build
(authoritative) and 291 pages of the Fandom community wiki (strategy, odds, human names).

## Event cards
Screenshot an event mid-run and it comes back as a decision tree you can read in a couple
of seconds. Cards are **generated from the game XML**, never written: an event id resolves
into `cards/trees/<slug>.tree.json`, which a shared shell renders into `cards/`. Quoted text is verbatim
from the game's string table and no odds appear unless the files publish them. What a card
guarantees is [[concept-event-cards]]; the grammar it rests on is
[[concept-event-tree-grammar]]; the pipeline is `tools/EVENT-CARD.md`.

**386 trees and 386 cards** are built, out of 395 paged events — `cards/trees/*.tree.json`
and `cards/card-*.html` are the inventory, and neither is catalogued here because both are
regenerable machine output. Any remaining event id can be carded on demand with the event id
as the only input. Built ≠ published: publishing mints a hosted URL and is done on request,
per `tools/EVENT-CARD.md` §9.

## Reading the generated pages
`python tools/serve-site.py` puts all of it behind URLs on `127.0.0.1:8080` — `/sectors/` for
the 19 profiles, `/cards/` for a searchable index of all 386, and a page each. Nothing is
rebuilt to make that work, so the same files still open off disk and still publish as
artifacts. `tools/LOCAL-SITE.md` is the spec.

With FTL running, `python tools/save-watch.py` drives it: the current event's card appears on
its own, and a sector page arrives marked with the beacons that run has already visited.
`tools/SAVE-WATCH.md` is the spec.

## Coverage at a Glance
| Type | Pages | Notes |
|------|-------|-------|
| Events | 395 | **complete** — every event id in the game data is paged or declined with a reason |
| Items | 64 | every `[[item-...]]` link in the wiki resolves |
| Sectors | 20 | **complete** — all 21 in-game sector ids |
| Entities | 16 | factions, species, the Flagship, and the 5 unlockable player cruisers |
| Concepts | 29 | mechanics and methodology |
| Chains | 21 | **complete** — every quest line the `<quest>` graph substantiates |
| Sources | 325 | 33 game-data files + 291 Fandom pages + 1 research synthesis |
| **Total** | **870** | |

**Event coverage is closed.** Of 460 event ids in the data: 395 have pages; ~33 are
dev/test stubs or UI system messages; 10 are event-list allocation buckets; 22 are pure
outcome branches documented inside their parent pages. Every id is accounted for.

## Version Coverage
- 296 events `both` · 96 `ae` · 3 `unknown`.
- `ae` means **Advanced Edition only** — not "extracted from the AE build". Pages are `ae`
  when defined in `dlcEvents*.xml` or reachable only via an `OVERRIDE_*` list.
- We hold only AE files, so `both` is an inference from base-file membership, not an
  observation of a vanilla install. `<!--DLC-->`-marked tags let individual vanilla
  differences be documented precisely; many pages carry a **Version Differences** section.

## What This Wiki Can Answer Well
- **"What can happen at a beacon in sector X?"** — every sector's beacon allocation table
  is recorded, and events are indexed by sector.
- **"What does event X actually do?"** — full choice/outcome tables from the game files,
  with blue-option gates and their requirements.
- **"Which events does having a Teleporter/Slug crew/Hacking open up?"** — each item page
  indexes the blue options it gates.
- **"How do I unlock ship Y?"** — 6 unlock chains with every step, requirement and failure
  mode, plus a page per unlockable cruiser ([[entity-rock-cruiser]],
  [[entity-stealth-cruiser]], [[entity-mantis-cruiser]], [[entity-zoltan-cruiser]],
  [[entity-federation-cruiser]]) giving hull, crew, starting systems and augments.
- **"What does this quest actually lead to?"** — 21 chain pages, covering every quest line the
  43 `<quest>` tags substantiate, not just the ship unlocks. Each gives the trigger beacons,
  the ordered steps, the destination table with odds where derivable, and the failure modes.
- **"How likely is that?"** — where derivable. See the honest limits below.

## Resolved Mechanics Questions
Each began as a contradiction flagged independently by several ingest passes, and was
settled by evidence rather than by picking a side:

- [[concept-surrender-offers]] — `<surrender chance="X">` is the probability the ship
  **keeps fighting**; surrender chance is `1 − X`. Three independent lines of evidence,
  including that ships which never surrender *omit the element* rather than using `0`.
- [[concept-event-list-weighting]] — the engine selects uniformly across event-list
  entries, so duplicated entries are weights. Validated against three independently-stated
  Fandom percentages that reproduce exactly.
- [[concept-rebel-fleet-advance]] — `<modifyPursuit amount="N">`: `N` is a **jump count**,
  and the sign selects between two different effects. Settled from the engine's own
  notification strings in `text_misc.xml`.
- [[concept-blueprint-rarity]] — rarity runs 1 (commonest) → 5 (rarest), with `0` a
  separate *exclusion* flag, proven by the Crystal sector's `<rarityList>` overrides.

## Thin Spots
- **Odds are mostly `unknown` by design.** The game files express branch weighting
  structurally, never as percentages. Where a list has duplicated entries the share is
  derived and labelled; everywhere else it stays `unknown` rather than guessed.
- **`sector_class` is `unknown` on 10 faction sectors** — the red/blue hostility flag is
  not in the game data at all.
- **No `runs/` sources.** Several open questions need a single in-game observation to
  close; nothing has been observed yet.
- **The link graph is closed.** As of the 2026-08-13 lint every wikilink in the wiki resolves
  to a real page, every page has an inbound link, and every page is catalogued in `index.md`.
  Exactly **two** unresolved `[[…]]` strings remain, both inside `log.md`: a schema
  placeholder and a slug that was renamed after the entry quoting it was written. `log.md` is
  append-only, so historical entries are left as written.
- **The biggest remaining unknowns are quantities, not coverage.** The damage rate of any of
  the six hazards ([[concept-hazards]]) and store prices. None of these is in `raw/gamedata/`.
  **The largest of them closed on 2026-08-16**: what `LOW`/`MED`/`HIGH` are worth in scrap and
  resources, from [[source-fandom-rewards]] — but only at `medium` reliability (the figures are
  community-derived, not datamined here) and only for **Normal difficulty**. See
  [[concept-autoreward-tiers]].

## Watch List — open questions that matter
- **What does `unique="true"` scope to — a sector, or a run?** It sits on **194** events, and
  the answer changes the effective size of every sector's event pool. The per-sector reading
  is the better bet ([[concept-event-uniqueness]]), but the files never say, and settling it
  needs one observed run — which would be the first time `raw/runs/` outranked the game data
  on a question.
- **Does the engine read `<eventCounts>`?** Two allocation systems exist and disagree. If
  the depth-indexed one is live, several events tagged `unreachable` are not. One observed
  boarding event in Federation Space would settle it. See
  [[concept-sector-event-allocation]].
- **[[event-boss-fleets-both]]** — in no event list, yet named as live in its own file's
  header comment. Both readings recorded.
- **`<surrender>` with no `chance` attribute** — four ships have one; the default is
  undocumented.
- **`min`/`max` on surrender blocks** — hull points (files) or percentages (Fandom)?
- **Fandom's alternative ship-unlock routes** are unverifiable: `achievements.xml` contains
  no unlock-condition entries at all.

## Known Data Bugs Recorded
Shipped defects found in the game files and documented rather than silently corrected:
`<augBluepring>` (misspelled tag, `blueprints.xml:2916`); `PIRATE_CIVILIAN_BEACON` and
`REBEL_VS_FEDERATION` sitting in distress lists with no `<distressBeacon/>`;
`PIRATE_SURRENDER_CIVILAN` written for a ship that has no `<surrender>` element;
`autoReward level="MEDIUM"` where the schema uses `MED`; `AUTO_HACKER`'s blue branch
loading a Slug ship; `MISSILES_2` vs `MISSILES_2_PLAYER` sharing a name with different stats.

## Cut and Unreachable Content
Complete, fully-authored events that cannot occur in this build are paged and tagged
`unreachable` (plus `cut-content` where a dev note supports it) rather than dropped —
e.g. [[event-ghost-ship]], [[event-zoltan-surrender]], [[event-fleet-easy-again]],
[[event-dock-bomb-salesman]], [[sector-vestigial-definitions]]. Tagging one requires
positive evidence; missing sector allocation alone is not sufficient.
