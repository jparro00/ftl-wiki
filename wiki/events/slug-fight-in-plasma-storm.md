---
id: event-slug-fight-in-plasma-storm
type: event
event_name: STORM_SLUG_FIGHT
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [combat, slug, plasma-storm, surrender, varies-text, repeatable, slug-sector]
---

# Slug fight in plasma storm — `STORM_SLUG_FIGHT`

## Summary
A Slug ship ambushing you inside an ion storm. Mechanically it is the ordinary `JELLY`
fight — 50% surrender, 50% escape, default rewards — wrapped in a
`<environment type="storm"/>` that halves your usable power. The storm is the whole
event: the Slugs are unaffected by it and you are not.

## Trigger & Where It Appears
- Event list: `STORM_SLUG` in `events_slug.xml`, alongside `STORM_REBEL` and
  `STORM_BOARDING` ([[source-events-slug]]). No `OVERRIDE_STORM_SLUG` exists in
  `dlcEventsOverwrite.xml` ([[source-dlceventsoverwrite]]), so the pool is identical in
  both editions.
- `STORM_SLUG` is allocated at `min=1 max=3` in both `SLUG_SECTOR`
  ([[sector-slug-controlled-nebula]]) and `SLUG_HOME` ([[sector-slug-home-nebula]])
  ([[source-sector-data-xml]]) — one to three storm beacons per Slug sector.
- **Not `unique`** — the attribute is absent, so it can recur. Fandom agrees
  (`unique=false`) ([[source-fandom-slug-fight-in-plasma-storm]]).
- Beacon: hostile, **plasma storm environment**, ship visible on Long-Ranged Scanners
  (`LRSmap=ship+plasmastorm`).

### Odds of drawing it
`STORM_SLUG` has three distinct members, none duplicated. **Assuming uniform selection
across list entries** ([[concept-event-list-weighting]]), each storm beacon in a Slug
sector is this event **1/3** of the time.

### Storm but not nebula
The event declares `<environment type="storm"/>` and **no nebula**. Fandom draws out the
consequence: *"Despite being a plasma storm, this event only occurs at non-nebula beacons.
Fleet pursuit will be the full amount, instead of the 80% that you would have when jumping
from a nebula beacon in a Slug sector."*
([[source-fandom-slug-fight-in-plasma-storm]]) The environment tag in the files supports
the premise; the fleet-pursuit percentage is Fandom's claim, not a file claim.

## Text
`[varies: textList STORM_SLUG_FIGHT]` — four entries, no repeats. The text list shares the
event's name ([[source-events-slug]], [[source-text-events-xml]]):

1. *The ion storm here threatens to deactivate your core systems, a fact made all the worse for the largely unaffected Slug ships circling like space-vultures.*
2. *The Slug ship that descends into view as you enter the ion storm must have sensed your distress - defensive action!*
3. *You arrive in the middle of an ion storm. Slugs generally avoid these storms but you find one waiting in ambush. Prepare for a fight!*
4. *You find yourself stuck in the middle of an ion storm with a Slug ship just a short distance away, refusing all hails. You cautiously try to slip further into the clouds, but they turn suddenly to attack!*

Fandom lists the same four verbatim ([[source-fandom-slug-fight-in-plasma-storm]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | None. | — | `<ship load="JELLY" hostile="true"/>` in a plasma storm — immediate combat, default rewards. | 100% |

### The `JELLY` ship
`auto_blueprint="SHIPS_JELLY"` ([[source-events-ships]]):

| Branch | Declaration | Reading |
|---|---|---|
| Surrender | `chance="0.5" min="3" max="4"` → `SLUG_SURRENDER` | **50% surrender chance** ([[concept-surrender-offers]] — surrender is `1 − chance`) |
| Escape | `chance="0.5" min="3" max="4"` → `PIRATE_ESCAPE` | 50% escape attempt, same band |
| Destroyed / dead crew | `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT` | default rewards |

The surrender loads [[event-slug-surrender]], which is worth having: its three outcomes
are `HIGH` `fuel_only`, `LOW` `stuff` and `MED` `stuff`. Fandom renders the same two bands
as "50% surrender offer chance at 30–40% hull, 50% escape attempt chance at 30–40% hull"
([[source-fandom-slug-fight-in-plasma-storm]]) — that hull-percentage reading is Fandom's
interpretation of `min`/`max`.

## Blue Options
None. No `req` attribute appears anywhere in the event.

## Rewards & Risks
- **Reward:** default rewards, or the [[event-slug-surrender]] table on a surrender.
- **Risk:** the plasma storm is the danger, not the ship. It halves reactor output, so a
  power-hungry build fights this at a real disadvantage while the Slug ship — per the
  flavour text — is "largely unaffected".
- Jumping out of this beacon costs full fleet pursuit rather than the reduced nebula rate,
  per Fandom.

## Strategy Notes
- *Opinion:* this is the Slug sector's most punishing routine fight for high-power builds
  and its easiest for low-power ones. Battery (`Backup Battery`) and low-cost weapons
  shine; a four-weapon layout does not.
- Visible on scanners, so it can be avoided when the ship is already hurt.
- Getting the surrender is worth aiming for — `HIGH` `fuel_only` is a meaningful top-up in
  a sector where fuel matters.

## Related
- [[event-slug-surrender]] — the surrender branch of the `JELLY` hull
- [[event-slug-fight]], [[event-slug-fight-in-nebula]] — the other `JELLY` encounters in
  Slug space
- [[event-rebel-fight-in-plasma-storm]] — `STORM_REBEL`, its neighbour in `STORM_SLUG`
- [[concept-surrender-offers]] — how the 50% is derived
- [[concept-event-list-weighting]] — basis for the 1/3 figure
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] Confirm Fandom's full-fleet-pursuit claim for non-nebula beacons in a nebula sector.
- [ ] Is the enemy ship genuinely exempt from the storm's power penalty, or is that only
      flavour?

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-slug-fight-in-plasma-storm]] (per raw/wiki/slug-fight-in-plasma-storm.md)
