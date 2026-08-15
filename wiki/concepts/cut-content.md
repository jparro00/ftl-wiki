---
id: concept-cut-content
type: concept
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
related_events: []
tags: [methodology, unreachable, cut-content, evidence-standards, datamining]
---

# Cut and unreachable content

## Definition & Context

Some events in `raw/gamedata/` are complete — text, choices, rewards, ship blueprints — and
cannot happen. This wiki **pages them anyway**, tagged rather than dropped, because a fully
authored event that no player can reach is a fact about the game worth recording.

**42 event pages carry `unreachable`; 19 carry `cut-content`.** The two tags are not synonyms
and the distinction is the point of this page.

## The evidence standard

Tagging something unreachable requires **positive evidence**. This was tightened mid-way
through the original ingest, after `unreachable` was being inferred from absence of a
`sector_data.xml` allocation — which does not prove anything:
`NEUTRAL_EXIT` and `FEDERATION_BASE_ASSIST` have zero allocations and are plainly live. See
[[concept-sector-event-allocation]].

Three grades of evidence, strongest first:

### 1. The definition itself is commented out — the strongest possible case

**Exactly two events in the entire corpus.** Their `<event>` element sits inside `<!-- -->`, so
the game never parses them at all ([[source-events-xml]], [[source-dlcevents-anaerobic]]):

| Event | Where | Note |
|---|---|---|
| [[event-fleet-easy-again]] | `events.xml` | *"Another ship approaches, the reinforcements seem endless!"* — a second `FLEET_EASY` that no list could reach even if it wanted to |
| [[event-lanius-boarders]] | `dlcEvents_anaerobic.xml` | A finished 3-Lanius boarding ambush, disabled with the list comment *"Prob enough - unless theres something cool"* |

These two are also **why the corpus is 460 ids but only 458 live** — the discrepancy the
2026-08-13 lint resolved.

### 2. The only reference to it is commented out

`LANIUS_BOARDERS` is the purest case: its sole `<event load=.../>` in `BOARDERS_LANIUS` is
commented out, leaving a **one-member list**, so every Lanius boarding beacon resolves to
[[event-boarders-humans-abandoned]] instead.

### 3. A dev note says so

Comments left in the files by the developers. These support `cut-content` specifically —
evidence of intent, not just of unreachability. `MATT CHANGED TO STOP CRASHES`,
`Prob enough - unless theres something cool`, `JUSTIN - USE THIS ELSEWHERE`.

## What `unreachable` and `cut-content` each mean here

- **`unreachable`** — cannot occur in this build, for any reason. 42 pages.
- **`cut-content`** — unreachable *and* there is evidence it was deliberately disabled. 19
  pages, a subset of the above.

A third meaning exists and is **unverifiable from the data**: [[source-fandom-random-events]]
states that some distress events *"won't [occur] due to coding errors"*, naming none. The defect
would be in engine code this repo does not hold. Recorded on
[[concept-sector-event-allocation]].

## The notable cases

- **[[event-ghost-ship]]** — a fully authored multi-branch salvage encounter with a deep
  boarding tree, unreachable. Its `deadCrew` text is literally *"Should not be seen"*, on a hull
  with 7 crew — a developer placeholder that the card pipeline now suppresses explicitly.
- **[[event-boarders-asteroid-ghost]]** — atmospheric, complete, and allocated nowhere.
- **[[event-zoltan-surrender]]**, **[[event-dock-bomb-salesman]]** — shipped but unused.
- **[[sector-vestigial-definitions]]** — two whole sector definitions that are vestigial.
- **[[event-boss-fleets-both]]** — the honest hard case. It is in **no event list**, yet its own
  file's header names it as live. Both readings are recorded and it is **not** tagged
  unreachable, because the evidence cuts both ways.

## Implications For Play
None directly — that is the point. The value is in not being misled: a search of this wiki that
turns up [[event-ghost-ship]] should make clear you will never see it, and a strategy guide that
mentions it is describing something that is not in the game.

## Related
- [[concept-sector-event-allocation]] — why missing allocation is not proof
- [[concept-event-uniqueness]] — the other flag that shrinks what you can see
- [[event-ghost-ship]], [[event-fleet-easy-again]], [[event-lanius-boarders]]
- [[sector-vestigial-definitions]]
- [[concept-modding-and-the-append-convention]] — how a mod would re-enable any of this

## Open Questions
- [ ] Which distress events Fandom means by *"coding errors"* — none are named, and the claim
      cannot be checked against the files.
- [ ] Whether [[event-boss-fleets-both]] is live. Settling it needs an observed run.
- [ ] Whether any `unreachable` page is reachable through `<eventCounts>` in `newEvents.xml`,
      if the engine reads that system at all — see [[concept-sector-event-allocation]].

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-random-events]] (per raw/wiki/random-events.md)
