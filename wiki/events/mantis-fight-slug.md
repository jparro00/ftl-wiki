---
id: event-mantis-fight-slug
type: event
event_name: SLUG_MANTIS
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [combat, mantis, no-surrender, unique, slug-sector]
---

# Mantis fight (Slug) — `SLUG_MANTIS`

## Summary
A Mantis raider hunting in Slug space. No choices, no escape route — the event body is a
line of text and a hostile ship. Notable only for *which* ship: `MANTIS_FIGHT` declares
neither a surrender nor an escape block, so once it starts it must be fought to the end.

## Trigger & Where It Appears
- Event list: `HOSTILE_SLUG` in `events_slug.xml` ([[source-events-slug]]). There is **no**
  `OVERRIDE_HOSTILE_SLUG` in `dlcEventsOverwrite.xml` ([[source-dlceventsoverwrite]]), so
  the pool is identical in both editions.
- `HOSTILE_SLUG` is allocated at `min=1 max=2` in both `SLUG_SECTOR`
  ([[sector-slug-controlled-nebula]]) and `SLUG_HOME` ([[sector-slug-home-nebula]])
  ([[source-sector-data-xml]]).
- `unique="true"` — at most once per run.
- Beacon: hostile. Fandom marks `LRSmap=ship`, so a **ship does show on Long-Ranged
  Scanners** ([[source-fandom-mantis-fight-slug]]) — this one is avoidable if you scout.
- **No `<environment>`**: despite the Slug sectors being nebula-heavy, this fight has no
  nebula or storm effect.

### Odds of drawing it
`HOSTILE_SLUG` has five distinct members — `SLUG_FIGHT`, `SLUG_MANTIS`, `SLUG_PIRATE`,
`SLUG_REBEL`, `DONOR_BLACK_RAVEN` — none duplicated. **Assuming uniform selection across
list entries** ([[concept-event-list-weighting]]), each non-nebula hostile beacon in a
Slug sector is this event **1/5** of the time.

## Text
> You intercept comm chatter from an incoming Mantis ship. "Look. This ship appears not to
> be owned by the squishy ones. Maybe they won't smell so bad when we cut them open." They
> move in on your position.

(`event_SLUG_MANTIS_text`, per [[source-text-events-xml]]) — a single fixed string, not a
text list. Fandom transcribes it identically ([[source-fandom-mantis-fight-slug]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | None. | — | `<ship load="MANTIS_FIGHT" hostile="true"/>` — immediate combat, default rewards. | 100% |

### The `MANTIS_FIGHT` ship
`auto_blueprint="SHIPS_MANTIS"`, `destroyed load="DESTROYED_DEFAULT"`,
`deadCrew load="DEAD_CREW_DEFAULT"` — default rewards ([[source-events-ships]]).

- **No `<surrender>` block and no `<escape>` block.** It will not offer to surrender and
  will not try to flee. Fandom's reference note says the same
  ([[source-fandom-mantis-fight-slug]]).
- It carries an explicit crew composition: `<crewMember type="mantis" prop="0.80"/>` and
  `<crewMember type="engi" prop="0.20"/>` — 80% Mantis, 20% Engi
  ([[source-events-ships]]). That mix matters if you board it: Mantis win boarding fights,
  Engi lose them badly.

## Blue Options
None. No `req` attribute appears anywhere in the event.

## Rewards & Risks
- **Reward:** default rewards only — no bonus scrap, no item, no crew.
- **Risk:** a Mantis hull, which in FTL terms means high crew count and a boarding threat
  if it has a teleporter. Because the ship neither surrenders nor escapes, you cannot
  shortcut the fight by damaging it to a threshold; you commit or you jump.

## Strategy Notes
- *Opinion:* this is the least interesting of the four Slug-sector hostiles precisely
  because there is no surrender branch — [[event-pirate-fight-slug]] and
  [[event-rebel-fight-slug]] both have a 50% chance of ending early with a payout.
- The scanner does show a ship here, so with Long-Ranged Scanners this beacon can be
  routed around on a damaged ship.
- Against the 80/20 Mantis-Engi crew, defending your own ship is the priority; boarding
  in is unattractive unless you have Rockmen or Mantis of your own.

## Related
- [[event-mantis-fight]] — the generic version of this encounter outside Slug space
- [[event-mantis-fight-in-nebula-slug]] — the Slug-sector Mantis fight that *does* carry a
  nebula environment
- [[event-slug-fight]], [[event-pirate-fight-slug]], [[event-rebel-fight-slug]] — the rest
  of the `HOSTILE_SLUG` pool
- [[concept-event-list-weighting]] — basis for the 1/5 figure

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] What `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT` pay in absolute numbers.
- [ ] Does the 80/20 crew proportion apply per crew slot or to the roster as a whole?

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-mantis-fight-slug]] (per raw/wiki/mantis-fight-slug.md)
