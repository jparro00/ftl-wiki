---
id: source-fandom-legendary-thief-kazaaakplethkilik
type: source
source_kind: wiki
raw: raw/wiki/legendary-thief-kazaaakplethkilik.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [mantis, ship-unlock, quest-marker, blue-option]
---

# Fandom — "Legendary thief KazaaakplethKilik"

## Summary
The community wiki page for `MANTIS_NAMED_THIEF` — the Mantis Cruiser unlocking event.
Retrieved via the MediaWiki API at revision 74666. The most substantial Mantis page in the
dump: it maps the whole aftermath tree, names the reward items, and covers the quest
marker that the game files only reference by id.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'MANTIS_NAMED_THIEF' in the
  datafiles."*
- **Identifies `unlockShip id="2"` as the [[entity-mantis-cruiser]] (Layout A)** — the
  id→ship mapping is not stated anywhere in the extracted game files, so this is
  information only Fandom supplies.
- Names the augment reward as **Mantis Pheromones**, which matches
  `aug_CREW_STIMS_title` in `text_blueprints.xml` — so Fandom's item name and the file's
  `CREW_STIMS` internal name refer to the same augment.
- Adds a **play-behaviour claim absent from the files:** *"If this event is encountered
  without the required systems, you can jump away from the beacon, upgrade or buy the
  systems, and return to accomplish the quest."*
- Adds a **second unlock path absent from the files:** the Mantis Cruiser *"can also be
  unlocked by winning the game with the Zoltan Cruiser."* `achievements.xml` contains no
  entry supporting this — recorded as Fandom-only and unverified.
- States the enemy crew is **entirely Mantis**; the ship definition specifies no `<crew>`
  block, so this comes from the `SHIPS_MANTIS` auto-blueprint and is not independently
  confirmed here.
- Confirms **no surrender, no escape** on the `MANTIS_NAMED_THIEF` ship, citing
  `events_ships.xml`.
- Maps the aftermath tree identically to `MANTIS_NAMED_THIEF_DEFEAT` in the files,
  including the Teleporter and Sensors-3 gates leading to the same four sub-choices, and
  the Adv. Medbay / Adv. Clonebay level-2 gates.
- Documents the **Quest Marker** section (`MANTIS_NAMED_THIEF_STASH`) as part of this page
  rather than separately, with `LRSmap` showing no ship, and states the reward as *"a
  weapon with high scrap"* — matching `autoReward level="HIGH" weapon`.
- Categorised `Random_Events`, `Unique_Events`, `Ship_Unlocking_Events`,
  `Events with Quest Markers`, `Augmentation reward opportunity`, `Crew reward
  opportunity`, `Weapon reward opportunity`.

## Events Covered
- [[event-legendary-thief-kazaaakplethkilik]]
- [[event-mantis-named-thief-stash]] — documented as the "Quest Marker" section

## Other Pages Touched
- [[chain-mantis-cruiser-unlock]], [[entity-mantis-cruiser]],
  [[item-mantis-pheromones]], [[item-teleporter]], [[item-sensors]], [[item-medbay]],
  [[item-clone-bay]], [[sector-mantis-homeworlds]], [[entity-mantis]]

## Reliability Notes
`medium`, but unusually load-bearing: two of its claims (the ship-id mapping and the
jump-away-and-return behaviour) have **no counterpart in the game files at all**, so they
cannot be checked, only believed or not. They are cited as Fandom-only on
[[event-legendary-thief-kazaaakplethkilik]].

## Contradictions Flagged
> ⚠️ **CONTRADICTION (minor):** the crew reward's skill level.
> - Fandom: *"Mantis crewmember named Kazaaak **maxed** in all skills"*
> - Game files: `all_skills="2"` ([[source-events-xml]])
>
> Probably the same statement if 2 is the cap, but the files say "2", not "max".
> Recorded on [[event-legendary-thief-kazaaakplethkilik]]; the raw value is used there.

Also noted, though not a contradiction: Fandom presents the "Save the thief" branch as
producing the reward directly, while the files route it through one further "Accept"
choice. Same outcome, one extra click.

## Links
- Source URL: https://ftl.fandom.com/wiki/Legendary_thief_KazaaakplethKilik
- [[source-events-xml]], [[source-text-events-xml]], [[source-sector-data-xml]]
