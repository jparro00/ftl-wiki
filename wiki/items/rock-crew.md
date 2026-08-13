---
id: item-rock-crew
type: item
item_kind: crew
rarity: 3
unlocks_blue: [[[event-fire-on-research-station]], [[event-unknown-disease-on-mining-colony]], [[event-crystalline-research-facility]], [[event-rock-ship-in-plasma-storm]], [[event-mantis-ship-with-rock-body-parts]], [[event-slug-drink]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 9
tags: [crew, rock]
---

# Rockman (crew)

## Summary
The `rock` crew blueprint — *"The 'Rockmen' of Vrachos IV are rarely seen and are known for
their fortitude."* ([[source-text-blueprints]]).

## Stats
- Blueprint `rock` (`<crewBlueprint>`), [[source-blueprints]].
- Powers, verbatim from [[source-text-blueprints]]: *"Immune to fire"*, *"Movement speed is
  halved"*, *"Max Health is increased to 150"*.
- Hire cost **55** scrap (`<!--was 65-->`), `bp` 4, `rarity` 3.

## How To Get It
- Hired at stores and crew-hiring beacons.
- `<crewMember class="rock">` grants: [[event-lone-shuttle]] (`LONE_SHUTTLE_WAIT`,
  [[source-nameevents]]) and [[event-rock-pirates-fight]] (`ROCK_PIRATE`, [[source-events-ships]]).
- [[entity-rock-men]] collects the faction-level context.

## Blue Options It Unlocks
- [[event-fire-on-research-station]] — `DISTRESS_STATION_FIRE` — fire immunity, the single most on-the-nose blue option in the game
- [[event-unknown-disease-on-mining-colony]] — `DISTRESS_STATION_DISEASE`
- [[event-crystalline-research-facility]] — `CRYSTAL_HUMAN_TESTS` — Rockmen are the Crystals' descendants ([[source-text-blueprints]])
- [[event-rock-ship-in-plasma-storm]] — `NEBULA_ROCK_RACIST`
- [[event-mantis-ship-with-rock-body-parts]] — `ROCK_MANTIS_HUNTER` — the same list also accepts [[item-rock-plating]]
- [[event-slug-drink]] — `SLUG_DRINK`

## Strategy Notes
- Six blue options — mid-table among crew species: Engi and [[item-slug-crew]] gate eleven
  events each, [[item-lanius-crew]] eleven, Mantis four, Zoltan and Human two and one.
  Counted across an exhaustive scan of the event files in `raw/gamedata/`.
- The gates split between "walk into the fire" (fire immunity, 150 health) and "be
  recognised as a Rockman" (`NEBULA_ROCK_RACIST`, `CRYSTAL_HUMAN_TESTS`, `SLUG_DRINK`).
- Halved movement speed is the standing cost; [[item-mantis-pheromones]] partly offsets it.

## Related
- [[entity-rock-men]] — the faction page
- [[item-rock-plating]] — substitutes for a Rockman at `ROCK_MANTIS_HUNTER`
- [[chain-rock-cruiser-unlock]]

## Open Questions
- [ ] Whether Crystal crew satisfy `req="rock"` anywhere — they are described as ancestors of the Rockmen but use a separate `crystal` blueprint.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-crystal]] (per raw/gamedata/events_crystal.xml)
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-nameevents]] (per raw/gamedata/nameEvents.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
