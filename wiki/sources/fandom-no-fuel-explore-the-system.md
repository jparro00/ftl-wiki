---
id: source-fandom-no-fuel-explore-the-system
type: source
source_kind: wiki
raw: raw/wiki/no-fuel-explore-the-system.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [out-of-fuel]
---

# Fandom — "No fuel: explore the system"

## Summary
Community wiki page for `FUEL_EXPLORE`, retrieved at revision 73276. Its main added value is
expanding the `ASTEROID_EXPLORE_RESULTS` sub-list (defined in `events.xml`, not
`events_fuel.xml`) inline, so the whole tree is readable in one place.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'FUEL_EXPLORE' in the datafiles."*
- Marks it `{{Locations|outoffuel=distressboth}}`, matching the XML.
- Expands `ASTEROID_EXPLORE_RESULTS`: high fuel, medium missiles, medium drone parts,
  damage, a pirate fight in an asteroid field, or nothing.
- Notes the same asteroid scenario appears in the *Large asteroid field* event, which
  additionally offers a Scrap Recovery Arm blue option — this one does not.
- Identifies `REBEL_AUTO_FUEL` (80s) and `PIRATE` (90s) as the hostile ships.

## Events Covered
- [[event-no-fuel-explore-the-system]]

## Other Pages Touched
- [[event-no-fuel-prepare-to-dock]]

## Reliability Notes
`medium`, `game_version: unknown`.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** hull damage on the bad asteroid outcome.
> Fandom: *"5 hull damage, 1 damage to a random system, 1 damage with fire to a random
> room"*. Game files: `<damage amount="3"/>` plus a `<!--DLC-->`-gated random-system hit and
> a room fire ([[source-events-xml]]). Recorded on
> [[event-no-fuel-explore-the-system]]; game files trusted. Likely Fandom summing the
> hull cost of all three tags.

## Links
- Source URL: https://ftl.fandom.com/wiki/No_fuel:_explore_the_system
- [[source-events-fuel]], [[source-events-xml]], [[source-text-events-xml]]
