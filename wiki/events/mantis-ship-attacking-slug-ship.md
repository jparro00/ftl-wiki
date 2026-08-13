---
id: event-mantis-ship-attacking-slug-ship
type: event
event_name: SLUG_DISTRESS_MANTIS
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: distress
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, distress, combat, augment-chance, optional-fight]
---

# Mantis ship attacking Slug ship — `SLUG_DISTRESS_MANTIS`

## Summary
A Mantis raider has a Slug ship cornered and the Slugs are begging for help. You can save
them, finish them, or leave. Saving them pays `MED standard` and then offers a second bite:
the ungrateful Slugs will hand over an augment if you threaten them again. Attacking the
Slugs directly pays the highest single reward in the event.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]] — via the
  `DISTRESS_BEACON_SLUG` event list (`min 3 / max 4` per sector)
  ([[source-events-slug]], [[source-sector-data-xml]])
- Beacon: **distress** — carries `<distressBeacon/>` ([[source-events-slug]])
- `unique="true"`. No `<environment>` tag: this beacon is **not** forced into a nebula,
  unlike most of its list-mates.

## Text
> The distress call appears to be emanating from a Slug ship caught in open space by a
> Mantis raider. They contact you on emergency frequencies: "Please, we'll give you all we
> have if you sssave ussss!"

(`event_SLUG_DISTRESS_MANTIS_text`, per [[source-text-events-xml]])

## Choices & Outcomes

All three choices are `hidden="true"`.

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack the Mantis ship. | — | "You lock onto the Mantis ship and engage." → `<ship load="SLUG_DISTRESS_MANTIS" hostile="true"/>`. Win → `MED standard` + a follow-up choice (below). | 100% |
| 2 | Attack the Slug ship. | — | "You move to finish what the Mantis have started." → `<ship load="SLUG_DISTRESS_MANTIS_SLUG" hostile="true"/>`. Win → `HIGH standard`. | 100% |
| 3 | Of all the species in the galaxy, these two deserve one another. You power up the jump drive. | — | Nothing happens. | 100% |

### After beating the Mantis (choice 1)

Both `destroyed` and `deadCrew` give `<autoReward level="MED">standard</autoReward>`, then:

> The Mantis defeated, you contact the weakened Slug vessel. "You sssee," they begin, "we
> are most grateful, but, that isss, we do not currently have the liquid asssets to reward
> you at thiss time."

| # | Choice | Outcome |
|---|--------|---------|
| 1 | Leave them be. | "These wretches aren't worth fighting." Nothing further. |
| 2 | Finish them off. | Rolls `SLUG_DISTRESS_MANTIS_SURRENDER` — 2 entries (below) |

`SLUG_DISTRESS_MANTIS_SURRENDER` ([[source-events-slug]]):

| Entry | Text | Effect |
|---|---|---|
| 1 | "After a few shots their ship breaks apart and you move in to loot the remains." | `<autoReward level="RANDOM">standard</autoReward>` — the game's own word for the level |
| 2 | "A misstake! A sssimple misstake. Of course we can pay you! Ssseee? An augmentation has already transported." | `<autoReward level="LOW">augment</autoReward>` |

Note "Finish them off" does **not** start a second fight — both entries resolve
immediately.

### The enemies

- `SLUG_DISTRESS_MANTIS` — `SHIPS_MANTIS`, crew 0.75 mantis / 0.25 engi, **no surrender or
  escape block** ([[source-events-ships]])
- `SLUG_DISTRESS_MANTIS_SLUG` — `SHIPS_JELLY`, `HIGH standard` on both destroyed and
  deadCrew, no surrender or escape ([[source-events-ships]])

## Rewards & Risks
- Choice 1: `MED standard`, plus either nothing, a `RANDOM standard` roll, or a
  `LOW augment` — the only augment on offer in the Slug distress pool.
- Choice 2: `HIGH standard`, flat.
- Choice 3: nothing, no risk.
- Neither enemy can surrender or flee, so both fights run to a conclusion.

## Strategy Notes
- If you want scrap, attack the Slugs: `HIGH standard` in one fight beats `MED standard`
  plus a coin flip.
- If you want an augment, attack the Mantis and then finish the Slugs off — a 1-in-2 shot
  at a free augmentation. *(Opinion, from the two-entry list in [[source-events-slug]].)*
- "Finish them off" is free: no extra fight, no penalty for the betrayal.

## Related
- [[event-mantis-fight-in-nebula-slug]] — the other Mantis encounter in Slug space
- [[event-slug-ship-boarding-rock-ship]], [[event-slug-oxygen-malfunction]],
  [[event-slug-moons-question]], [[event-slocknog]] — the rest of `DISTRESS_BEACON_SLUG`
- [[entity-mantis]], [[entity-slugs]]

## Open Questions
- [ ] What `autoReward level="RANDOM"` resolves to.
- [ ] Whether the two `_SURRENDER` entries are equally weighted.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-fandom-mantis-ship-attacking-slug-ship]] (per raw/wiki/mantis-ship-attacking-slug-ship.md)
