---
id: concept-event-uniqueness
type: concept
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 3
related_events: []
tags: [mechanics, unresolved, contradiction, event-pools]
---

# `unique="true"` — once per sector, or once per run?

## Definition & Context
194 events in `raw/gamedata/` carry `unique="true"`, and 22 carry `unique="false"`. The
attribute plainly means "this cannot come up again", but **the files never say again *within
what*** — and the answer changes how big a sector's effective event pool is, whether a good
beacon can recur, and whether the store guarantees can be met at all.

Nothing in `raw/gamedata/` documents the scope. Both readings below are inference.

## The two readings

> ⚠️ **CONTRADICTION:** the scope of `unique="true"`.
>
> **Per sector** — [[source-fandom-random-events]] (per `raw/wiki/random-events.md`):
> *"Events that can occur only once per current sector (unique) or multiple times per current
> sector (non-unique)"*, with the exception carved out explicitly: *"select unique events
> (Ship Unlocking Events) can occur only once per game run."*
>
> **Per run** — [[concept-event-tree-grammar]], from [[source-events-xml]]: *"`unique="true"`
> … means the encounter cannot repeat in a run; there is no grinding a good table."*
>
> **Not a version difference.** The attribute is spelled identically in the vanilla event
> files and in `dlcEvents.xml` / `dlcEvents_anaerobic.xml`, and both sides of the disagreement
> are reading the same present-day AE data.

## Why the per-sector reading is the better bet

Three arguments, none of them decisive alone:

1. **[[concept-stores]] reached it independently**, from a different direction: sectors that
   guarantee two or three store beacons (`<event name="STORE" min="2" max="3"/>`) could not
   fill them if `STORE` were unique — and `STORE` is indeed not unique, while
   `STORE_REBELSIDE` is the lone exception. That argument only works if uniqueness is scoped
   **per sector**; under a per-run reading, non-uniqueness would be doing no work in the
   multi-store sectors specifically.
2. **The files carry a second `unique` attribute with an unambiguous meaning.** Eight of the
   21 `<sectorDescription>` entries in `sector_data.xml` are `unique="true"` — `FINAL`,
   `ENGI_HOME`, `MANTIS_HOME`, `SLUG_HOME`, `ZOLTAN_HOME`, `ROCK_HOME`, `CRYSTAL_HOME`,
   `REBEL_SECTOR_MINIBOSS` — and a sector can obviously only be "unique" across a **run**.
   ([[source-sector-data-xml]]) A format that already has one once-per-run flag has a reason
   to give the other one a narrower scope.
3. **The Fandom page needs an exception clause.** If `unique="true"` already meant once per
   run, singling out ship-unlock events as the once-per-run case would be redundant. The
   exception implies the rule is narrower.

Against it: the per-run reading is what the word "unique" suggests in isolation, and the
Fandom hub page is unsourced community knowledge rather than datamined behaviour. Neither
side has produced a game file, a decompilation, or an observed run that settles it.

**Practical consequence of the disagreement is small but real.** Under the per-sector reading,
a `unique` event you saw in the Pirate sector can come up again in a later Rock sector, so
long as both sectors allocate the list it belongs to. Under the per-run reading it cannot.

## Census

| Element | `unique="true"` | `unique="false"` | total `unique` attrs |
|---|---|---|---|
| `<event>` | 194 | 22 | 216 |
| `<sectorDescription>` | 8 | 13 | 21 |

Per-file distribution of `<event unique="true">`: `events.xml` 37, `dlcEvents_anaerobic.xml`
23, `events_slug.xml` 20, `events_zoltan.xml` 20, `events_rock.xml` 15, `events_nebula.xml`
14, `newEvents.xml` 13, `events_rebel.xml` 13, `events_crystal.xml` 11, `events_engi.xml` 8,
`events_pirate.xml` 7, `dlcEvents.xml` 5, `events_mantis.xml` 5, `nameEvents.xml` 3.

Counted over `raw/gamedata/*.xml` on 2026-08-13 by **parsing the XML**, so elements sitting
inside `<!-- -->` comments are excluded — a plain regex over the same files returns 195/27,
one of which is commented out. `dlcEventsOverwrite.xml` carries none.

> ⚠️ **CONTRADICTION (arithmetic, not sources):** [[concept-event-tree-grammar]] states
> *"`unique="true"` (206 events)"*, and its attribute census row reads `unique` (206).
> Neither figure reproduces. Parsed over all of `raw/gamedata/`: **194** true, 22 false, **216**
> attributes total. Parsed over the narrower file set that page says it counted
> (`events*.xml`, `newEvents.xml`, `dlcEvents*.xml`): 191 true, 22 false, 213 total. Regex
> variants give 195/214/222 — none of them 206 either. The grammar page's derivation is not
> recorded, so the number is flagged rather than overwritten. Worth resolving on the next
> lint; the likeliest reading is that 206 was an **attribute** count (true + false) taken
> before a later re-scan, not a count of unique events.
>
> **Resolved (lint, 2026-08-13).** Recounted independently with a left-to-right comment
> scanner over every `.xml` in `raw/gamedata/`: **242** `unique=` attributes exist in total,
> and they partition without remainder — 216 on `<event>` (194 `true`, 22 `false`), 5 on
> `<textList>` (all `false`), 21 on `<sectorDescription>` (8 `true`, 13 `false`). The
> partition closing exactly is what makes 194/216 safe to adopt. Neither 206 nor 195 can be
> produced from any subset, so both were corrected on [[concept-event-tree-grammar]] rather
> than reconciled, with the derivation now recorded on both pages. **This is an arithmetic
> correction only — the sources contradiction above (per sector vs per run) remains open.**

## Implications For Play

- **Ship-unlock events are once per run under either reading** — if you decline
  [[chain-crystal-cruiser-unlock]]'s opening beacon, that run is done with it.
- **The unique flag is why a good beacon does not repeat.** A sector's pool shrinks as you
  clear it, and the events that remain are disproportionately the non-unique filler.
- **Stores are deliberately non-unique** — that is the mechanism behind sectors that promise
  more than one. See [[concept-stores]].
- Where this wiki says "you cannot see this twice", read it as *at least not in this sector*,
  which is true under both readings.

## Where It Applies
- Every event page whose frontmatter or body quotes `unique="true"` — 194 of them.
- [[concept-stores]] — the load-bearing case for the per-sector reading
- [[concept-sector-event-allocation]] — pool size per sector is where uniqueness bites

## Related
- [[concept-event-list-weighting]] — the other unknown in how a beacon picks its event
- [[concept-event-tree-grammar]] — the attribute census and the competing reading
- [[concept-quest-beacon-placement]] — the other per-sector scoping rule

## Open Questions
- [ ] **The scope itself.** Settling it needs an observed run: note a `unique="true"` event in
      an early sector, then check whether it can recur in a later sector of the same type. A
      run note in `raw/runs/` would outrank both current claims for this specific question.
- [ ] Why do 22 events bother to state `unique="false"` when that is presumably the default?
- [ ] Does uniqueness track the **event** name or the **eventList** it was drawn from?

## Sources
- [[source-fandom-random-events]] (per raw/wiki/random-events.md)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
