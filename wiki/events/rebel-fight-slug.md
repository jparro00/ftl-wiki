---
id: event-rebel-fight-slug
type: event
event_name: SLUG_REBEL
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [combat, rebel, surrender, varies-text, repeatable, slug-sector]
---

# Rebel fight (Slug) — `SLUG_REBEL`

## Summary
The Rebellion pushing into Slug nebula space. A forced fight with three flavour variants
against the standard `REBEL` hull — 50% surrender offer, 50% escape attempt, default
rewards. Repeatable, and thematically the "they found you anyway" beacon of the Slug
sectors.

## Trigger & Where It Appears
- Event list: `HOSTILE_SLUG` in `events_slug.xml` ([[source-events-slug]]). No
  `OVERRIDE_HOSTILE_SLUG` exists ([[source-dlceventsoverwrite]]), so the pool is identical
  in both editions.
- `HOSTILE_SLUG` is allocated at `min=1 max=2` in both `SLUG_SECTOR`
  ([[sector-slug-controlled-nebula]]) and `SLUG_HOME` ([[sector-slug-home-nebula]])
  ([[source-sector-data-xml]]).
- **`unique="false"` — explicitly repeatable**, written out rather than omitted. Fandom
  agrees ([[source-fandom-rebel-fight-slug]]).
- Beacon: hostile, ship visible on Long-Ranged Scanners (`LRSmap=ship`)
  ([[source-fandom-rebel-fight-slug]]).
- **No `<environment>`** — a non-nebula beacon, which is what the second text variant
  ("your sensors blink back to life") is describing.

### Odds of drawing it
`HOSTILE_SLUG` has five distinct members, none duplicated. **Assuming uniform selection
across list entries** ([[concept-event-list-weighting]]), each non-nebula hostile beacon in
a Slug sector is this event **1/5** of the time.

## Text
`[varies: textList SLUG_REBEL]` — three entries, no repeats. As with
[[event-pirate-fight-slug]], the text list shares the event's name and is marked
`unique="false"` ([[source-events-slug]], [[source-text-events-xml]]):

1. *As you arrive at the beacon, a hostile ship immediately registers on your scanners. You didn't expect to see Rebels extending their reach into Slug territory. Charge the weapons!*
2. *You jump into empty space and are relieved to see your sensors blink back to life. However, you are less pleased to see them immediately register a rebel ship on an approach vector!*
3. *You receive a message from a nearby ship, "Looks like our intelligence was correct! Sneaking through the clouds with the Slugs... No one can hide from the rebellion!"*

Fandom lists the same three verbatim ([[source-fandom-rebel-fight-slug]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | None. | — | `<ship load="REBEL" hostile="true"/>` — immediate combat, default rewards. | 100% |

### The `REBEL` ship
`auto_blueprint="SHIPS_REBEL"` ([[source-events-ships]]):

| Branch | Declaration | Reading |
|---|---|---|
| Surrender | `chance="0.5" min="2" max="3"` → `PIRATE_SURRENDER` | **50% surrender chance** ([[concept-surrender-offers]] — surrender is `1 − chance`) |
| Escape | `chance="0.5" min="3" max="4"` → `PIRATE_ESCAPE` | 50% escape attempt |
| Destroyed / dead crew | `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT` | default rewards |

Note the asymmetry with the `PIRATE` hull: the Rebel's **escape** band (`3–4`) sits
*above* its **surrender** band (`2–3`), so an escaping Rebel gets its chance first as hull
falls. On the pirate the ordering is reversed. Elsewhere in this wiki Fandom renders these
bands as "50% escape at 30–40% hull, 50% surrender at 20–30% hull"; that percentage
reading is Fandom's interpretation of `min`/`max`, not a file claim.

## Blue Options
None. No `req` attribute appears anywhere in the event.

## Rewards & Risks
- **Reward:** default rewards, or `PIRATE_SURRENDER`'s payout if it offers.
- **Risk:** a standard Rebel hull. The escape band biting first means a fast, hard alpha
  strike is more likely to lose you the kill than to secure the surrender.
- Repeatable, so a Slug sector can serve it more than once.

## Strategy Notes
- *Opinion:* the surrender-below-escape ordering makes this the fight where a Hacking or
  Ion setup on the enemy Engines pays best — deny the escape and the surrender window
  arrives on your terms.
- Visible on scanners, so avoidable when damaged.
- Mechanically identical to [[event-rebel-fight]] elsewhere in the game; only the flavour
  text is Slug-specific.

## Related
- [[event-rebel-fight]] — the generic Rebel encounter, same ship
- [[event-rebel-fight-in-nebula]] — the nebula-flagged variant
- [[event-mantis-fight-slug]], [[event-pirate-fight-slug]], [[event-slug-fight]] — the rest
  of the `HOSTILE_SLUG` pool
- [[concept-surrender-offers]] — how the 50% is derived
- [[concept-event-list-weighting]] — basis for the 1/5 figure
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] Confirm which check the engine evaluates first when both bands are crossed.
- [ ] What `PIRATE_SURRENDER` pays out.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-rebel-fight-slug]] (per raw/wiki/rebel-fight-slug.md)
