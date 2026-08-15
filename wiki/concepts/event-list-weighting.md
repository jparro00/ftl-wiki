---
id: concept-event-list-weighting
type: concept
version: both
first_seen: 2026-08-09
last_updated: 2026-08-13
sources: 5
related_events: []
tags: [mechanics, odds, methodology]
---

# Event list weighting — how odds are derived

## Definition & Context
The game files state almost no probabilities. Outcomes are expressed structurally: a
choice loads an `<eventList>`, and the engine picks one member. Where a member appears
more than once, that repetition **is** the weighting.

```xml
<eventList name="NO_FUEL">
    <event load="FUEL_NOTHING"/>     <!-- appears 4 times -->
    <event load="FUEL_NOTHING"/>
    <event load="FUEL_NOTHING"/>
    <event load="FUEL_NOTHING"/>
    <event load="FUEL_TRADER"/>      <!-- appears once -->
    ...
</eventList>
```

This is the **one** place this wiki states a number the sources don't literally give.
Everywhere else, an unstated probability stays `unknown`.

## The assumption, and why it now holds

Deriving `4/11` from the list above assumes the engine selects **uniformly at random
across list entries**. That was an assumption when the first event pages were written.
It is now confirmed.

**The out-of-fuel family is the natural experiment.** Fandom independently states three
percentages for these events. Uniform selection over the two lists reproduces all three
exactly:

| Event | Appears | List size | Derived | Fandom states |
|---|---|---|---|---|
| `FUEL_NOTHING` | 4× | `NO_FUEL` (11) | **36.4%** | 36.4% |
| `FUEL_FLEET_DELAY` | 1× | `NO_FUEL` (11) | **9.1%** | 9% |
| `FUEL_NOTHING_DISTRESS` | 2× | `NO_FUEL_DISTRESS` (12) | **16.7%** | 16.7% |

Three independent matches to one decimal place, including a non-obvious repeated-entry
case. Counts verified directly against `events_fuel.xml` with comment blocks stripped.
([[source-events-fuel]], [[source-fandom-no-fuel-wait-fail-distress-off]])

A side effect: because the derived numbers match the **AE** list lengths (11 and 12) and
not the vanilla ones (10 and 11), this also demonstrates that Fandom's fuel pages describe
Advanced Edition — useful, since those pages state no version.

## How to use it

- **Duplicated entry → state the fraction.** `4/11`, and say the list and its size.
- **Always state the assumption inline.** "Assuming uniform selection across list entries."
- **Comments count for nothing.** Entries inside `<!-- -->` are not live and must be
  excluded before counting — several lists carry commented-out members, and including
  them silently corrupts every fraction in the list.
- **Check the edition.** If `<!--DLC-->` entries are present, the list has two lengths and
  therefore two sets of odds. Record both.
- **A single-member list is a certainty, not a probability** — say "always", not "1/1".
- **This does not extend to `<choice>` elements.** Choices are player decisions, not
  random draws. It applies only to `<eventList>` selection.

## Limits
Confirmed for `NO_FUEL` and `NO_FUEL_DISTRESS` against an independent source. Assumed —
reasonably, but still assumed — for every other list. Nothing in `raw/` documents the
selection algorithm, so a list with hidden per-entry weighting would break the derivation
silently. No such case has been found.

## Corroboration from outside the data

The modding documentation reaches the same conclusion from the author's side rather than the
reader's: [[source-modding-research]] records that **no shipped `<eventList>` carries weights,
so duplicating an entry is the only weighting mechanism available** to a mod author wiring a
new event into a list. That is an independent restatement of this page's central finding — a
modder wanting a 2-in-3 outcome has to list the entry twice, exactly as the derivation here
assumes the game reads it. It is not proof of uniform selection in the engine, but it is the
first non-circular support the assumption has had.

## Where It Applies
Every derived probability in the wiki. Any page stating a fraction should cite this page
for the method.

## Related
- [[concept-event-tree-grammar]] — the node grammar every event is built from
- [[concept-surrender-offers]] — the other resolved mechanics question; also a case of the
  raw data and the community wiki agreeing once the convention is understood
- [[source-sector-data-xml]] — sector-level allocation, where `min`/`max` are beacon
  **counts**, not probabilities. Per-beacon odds combine that with list weighting.
- [[concept-modding-and-the-append-convention]] — where the duplicate-to-weight practice is
  stated as author-side advice
- [[concept-event-uniqueness]] — the other unknown shaping what a beacon can roll

## Open Questions
- [ ] Confirm the assumption against a second, unrelated event family.
- [ ] Does the engine re-roll on a duplicate, or is selection genuinely uniform over
      entries? Both produce the same distribution here, so the wiki cannot distinguish them.

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-fandom-no-fuel-wait-fail-distress-off]] (per raw/wiki/no-fuel-wait-fail-distress-off.md)
- [[source-fandom-no-fuel-rebel-fleet-delay]] (per raw/wiki/no-fuel-rebel-fleet-delay.md)
- [[source-modding-research]] (per raw/modding/2026-08-12-ftl-modding-research.md) —
  duplicate-an-entry as the only weighting mechanism
