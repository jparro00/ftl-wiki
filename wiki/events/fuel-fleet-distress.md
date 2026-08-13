---
id: event-fuel-fleet-distress
type: event
event_name: FUEL_FLEET_DISTRESS
sectors: []
beacon_type: unknown
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: [out-of-fuel, rebel-fleet, unreachable, orphan, no-choice, dev-note]
---

# Fuel fleet distress — `FUEL_FLEET_DISTRESS`

## Summary
A fully authored duplicate of [[event-no-fuel-rebel-fleet-delay]] built for the
distress-beacon-**on** pool — and then never wired into it. It is complete content: its
own event block, its own 7-entry `textList`, and a working `modifyPursuit`. It is also
internally inconsistent: the pursuit modifier has the **opposite sign** from the twin, and
the flavour text still says the distress beacon is off.

## Trigger & Where It Appears
**Unreachable.** `FUEL_FLEET_DISTRESS` does not appear in `NO_FUEL_DISTRESS`, `NO_FUEL`, or
any other list. Grepping `raw/gamedata/` finds the id only in its own definition and its
matching `textList` ([[source-events-fuel]]). The file's own header comment *does* list it
under the distress pool:

```
Beacon:    NO_FUEL_DISTRESS (this is a list)
	FUEL_FLEET_DISTRESS
	FUEL_NOTHING_DISTRESS
	FUEL_SELLER_DISTRESS
	FUEL_TRADER_DISTRESS
```

…but the actual `<eventList name="NO_FUEL_DISTRESS">` below it omits the entry. Immediately
above the event block sits a developer note:

```
<!-- MATT FIXME - IS THIS A REPEAT -->
```

which reads as the reason it was pulled ([[source-events-fuel]]). Tagged `unreachable` and
`dev-note` accordingly. It has no Fandom page, consistent with never firing in play.

## Text
Prose is drawn from `FUEL_FLEET_DISTRESS_LIST`, a 7-entry `textList`. Entries 1–6 are
**byte-identical** to `FUEL_FLEET_DELAY_LIST`; entry 7 differs only in its final words
("…between you and **the Rebels**" vs "…between you and **them**")
([[source-text-events-xml]]). All seven describe the fleet losing you *because the distress
beacon is off* — which contradicts the pool this event was meant for.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | *(Continue — hidden, auto-labelled `continue`)* | — | `<modifyPursuit amount="1"/>` → Rebel fleet pursuit **advanced by 1 jump**, then loads `NO_FUEL` (the distress-**off** list) for a follow-up event. | 100% (if it fired) |

Two inconsistencies worth recording, both straight from the file
([[source-events-fuel]]):

1. **Sign flip.** `FUEL_FLEET_DELAY` uses `amount="-1"` (delay). This one uses `amount="1"`
   (advance) while its text promises a delay.
2. **Wrong follow-up list.** It loads `NO_FUEL`, the distress-off pool, despite being
   authored for the distress-on pool.

Both are consistent with the "IS THIS A REPEAT" note: an unfinished copy-paste.

## Blue Options
None.

## Rewards & Risks
None, and no way to reach it. Documented so the shipped-but-dead content is not silently
dropped.

## Strategy Notes
Nothing to play. Its only practical value is as evidence for why the distress-on pool has
no fleet-delay outcome — see [[event-no-fuel-rebel-fleet-delay]].

## Related
- [[event-no-fuel-rebel-fleet-delay]] — the live twin (`FUEL_FLEET_DELAY`)
- [[event-no-fuel-wait-fail-distress-on]] — the distress-on pool it was meant to join
- [[concept-rebel-fleet-advance]]
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Confirm no engine-side hard-coded call to `FUEL_FLEET_DISTRESS` exists outside the
      XML (only the data files were checked).
- [ ] Was it ever live in a shipped 1.0-era build, or dead from the start?

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
