---
id: item-slug-crew
type: item
item_kind: crew
rarity: 0
unlocks_blue: [[[event-single-life-form-on-moon]], [[event-intelligent-ponies]], [[event-the-black-raven]], [[event-no-fuel-slug-fuel-trader]], [[event-disabled-rock-ship]], [[event-slug-store-ship]], [[event-slug-unlock-1]], [[event-nebula-wreckage]], [[event-secret-word-abadoth]], [[event-zoltan-security-checkpoint]], [[event-pirate-ship-selling-drones]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 8
tags: [crew, slug]
---

# Slug (crew)

## Summary
The `slug` crew blueprint — *"These telepathic Slugs were shunned in the Galactic Federation for
their constant thievery and attempts at manipulation."* ([[source-text-blueprints]]).

## Stats
- Blueprint `slug` (`<crewBlueprint>`), [[source-blueprints]].
- Powers, verbatim: *"Telepathic powers reveal rooms and lifeforms even when sensors are
  down."* and *"Immune to mind control."*
- Hire cost **45** scrap — the joint cheapest crew in the file, level with Human.
  `bp` 2, `rarity` **0**.

## How To Get It
- Hired at stores and crew-hiring beacons; common in [[sector-slug-controlled-nebula]].
- No event in `raw/gamedata/` grants a Slug via a named `<crewMember class="slug">`.

## Blue Options It Unlocks
- [[event-single-life-form-on-moon]] — the `STRANDED` list
- [[event-intelligent-ponies]] — `DONOR_PONY`
- [[event-the-black-raven]] — `DONOR_BLACK_RAVEN`
- [[event-no-fuel-slug-fuel-trader]] — `FUEL_ON_SLUG_CHUCKLE`
- [[event-disabled-rock-ship]] — `ROCK_LOOTING`
- [[event-slug-store-ship]] — `NEBULA_SLUG_FAKE_STORE` — spot the trap
- [[event-slug-unlock-1]] — the `SLUG_UNLOCK_2` sub-event
- [[event-nebula-wreckage]] — `NEBULA_BATTLEFIELD`
- [[event-secret-word-abadoth]] — `SECRET_WORD_ABADOTH`
- [[event-zoltan-security-checkpoint]] — `ZOLTAN_CREW_SCAN`
- [[event-pirate-ship-selling-drones]] — the `CONTACT_PIRATE_SALESMAN` step

## Strategy Notes
- Eleven gates — level with Engi and [[item-lanius-crew]] for the most of any species, and
  more than every system except [[item-sensors]], [[item-hacking]] and [[item-teleporter]].
  At 45 scrap the Slug is also the joint cheapest hire.
- Its gates cluster on *detecting deception* — fake stores, con artists, hidden lifeforms —
  which matches the telepathy power rather than any combat trait.
- Mind-control immunity makes it a hard counter to enemy [[item-mind-control]].

## Related
- [[item-lifeform-scanner]] — the augment with the same in-play effect, a different `req`
- [[item-sensors]] — what the telepathy substitutes for
- [[item-slug-repair-gel]] — the augment that copies a different Slug trait

## Open Questions
- [ ] Whether any event grants a Slug crew member directly — none was found in `raw/gamedata/`.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
