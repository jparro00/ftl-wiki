---
id: concept-ae-vs-vanilla
type: concept
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
related_events: []
tags: [methodology, versions, advanced-edition, dlc-markers, evidence-standards]
---

# Advanced Edition vs vanilla

## Definition & Context

FTL ships in two meaningfully different forms, and **version mismatch is the single most
common source of contradiction in this domain**. A community page describing 1.0 and a
datamined file from 1.6.x will disagree without either being wrong.

This wiki records the distinction in a `version:` field on every page, with four values —
`ae`, `vanilla`, `both`, `unknown` — and the rules below govern which one a page gets.

## The three mechanisms

The game data expresses AE-only content in three different ways, and they are not
interchangeable:

### 1. Whole files

`dlcEvents.xml`, `dlcEvents_anaerobic.xml` and `dlcEventsOverwrite.xml` exist only in AE.
Anything **defined** in them is `ae`. The entire [[entity-lanius]] species and
[[sector-abandoned-sector]] arrive this way — every Lanius blueprint, ship, sector and event
lives in a `dlc*` file.

### 2. `<!--DLC-->` markers on individual elements — **113 occurrences**

This is the subtle one. An AE-only line can sit **inside an otherwise vanilla event**, so
version differences are frequently *within* a page rather than between pages. Two consequences
the card pipeline learned the hard way:

- [[event-crushed-pirate]] costs 2 hull and a system in AE, but only a reduced reward in
  vanilla — same event, different payload.
- **11 of the 24 markers are the element's *first child*** rather than a following sibling. A
  `dlc_marked()` check that only looked at the next sibling silently dropped them, and
  [[event-rebel-fight-chance-in-nebula]]'s Lifeform Scanner blue option lost its "(AE)". Fixed
  2026-08-10.

### 3. `OVERRIDE_*` lists

`dlcEventsOverwrite.xml` redefines existing names. An event reachable only through an override
list is `ae` even though its definition sits in a base file.

## What `ae` means here — and what it does not

> **`ae` means Advanced Edition *only*.** It does **not** mean "extracted from the AE build".

This distinction was got wrong at first and corrected in a retrofit: the 2026-08-09 lint
changed **166 pages from `ae` to `both`**, having found `ae` was being used to mean "we read
this out of our AE install", which is true of literally every file in `raw/gamedata/`.

Current distribution across event pages: **296 `both` · 96 `ae` · 3 `unknown`**.

## The honest limit

**This repo holds only AE files.** So:

- `ae` is a **positive finding** — the content is in a `dlc*` file, or DLC-marked, or
  override-only.
- `both` is an **inference** from base-file membership, not an observation of a vanilla
  install. It is well-founded but it is not the same kind of claim.
- `vanilla` — content cut *by* AE — can essentially only be established from a source outside
  the files, and is correspondingly rare here.
- `unknown` is correct and expected when a source does not state its version. **A source that
  does not say is `unknown`, not `ae`.**

## Implications For Play
- If a strategy claim disagrees with a page here, **check the version before assuming either is
  wrong**. Resolving a contradiction into a version difference is itself a finding worth
  recording — see §4.
- Several individual events behave differently rather than existing-or-not, so "the AE version
  of X" is often a payload difference inside the same beacon, not a separate beacon.

## Where It Applies
Every page — `version:` is a required field on all seven page types. Pages with a
**Version Differences** section carry the element-level detail.

## Related
- [[concept-event-tree-grammar]] — where `<!--DLC-->` markers sit in the grammar
- [[concept-sector-event-allocation]] — override lists and how they change pools
- [[entity-lanius]], [[sector-abandoned-sector]] — the largest AE-only additions
- [[concept-modding-and-the-append-convention]] — how a mod layers further changes on top
- [[concept-event-uniqueness]] — a contradiction that is **not** a version difference

## Open Questions
- [ ] Whether `<!--DLC2-->`, which appears rarely, denotes a second-pass DLC edit distinct from
      the ordinary marker.
- [ ] Which events AE *removed* — undetectable from an AE-only file set.
- [ ] The 3 remaining `version: unknown` event pages.

## Sources
- [[source-dlcevents]] (per raw/gamedata/dlcEvents.xml)
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
