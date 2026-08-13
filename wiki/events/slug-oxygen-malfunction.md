---
id: event-slug-oxygen-malfunction
type: event
event_name: SLUG_DISTRESS_TRICK
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: nebula
hostile: false
blue_options: [mantis crew]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, nebula, blue-option, crew-loss-risk, boarding-risk, scrap-reward, bug]
---

# Slug oxygen malfunction — `SLUG_DISTRESS_TRICK`

## Summary
A Slug ship asks you to send crew over to fix its life support. Two thirds of the time it
is an ambush that costs you boarders or a crew member; one third it is genuine and pays
`HIGH scrap_only`. A Mantis crew member takes the same job and turns the trap into a
guaranteed `HIGH scrap_only` with no risk at all.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]] — via the
  `DISTRESS_BEACON_SLUG` event list (`min 3 / max 4` per sector)
  ([[source-events-slug]], [[source-sector-data-xml]])
- Beacon: nebula (`<environment type="nebula"/>`), `unique="true"`
- **In the distress list but has no `<distressBeacon/>` tag**, so it will not show as a
  distress signal on the map. Fandom flags this as a bug; confirmed against the XML
  ([[source-events-slug]], [[source-fandom-slug-oxygen-malfunction]]).
- A `JELLY` ship is present **non-hostile** from arrival.

## Text
> You find a Slug vessel broadcasting the distress signal and contact them. "Ah, yesss, we
> are having problems with our oxygen generation unit. Perhaps your crew can assist in
> repairsss?"

(`event_SLUG_DISTRESS_TRICK_text`, per [[source-text-events-xml]])

## Choices & Outcomes

All three choices are `hidden="true"`.

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Send some crew to help. | — | Rolls `SLUG_DISTRESS_TRICK_LIST` — 3 entries, below. | see below |
| 2 | Ignore them. | — | "You know better than to trust the Slugs." Nothing happens. | 100% |
| 3 | **(Mantis Crew)** Have your Mantis oversee the repairs. | `req="mantis"` | "Once a couple of the Slugs have been spread across the walls of their ship, the rest surrender." → `<autoReward level="HIGH">scrap_only</autoReward>`. No fight. | 100% |

### `SLUG_DISTRESS_TRICK_LIST` (choice 1)

| Entry | Text | Effect |
|---|---|---|
| 1 | "…your crew is able to break free of the Slug trap and fight back to the airlock… not before a few Slugs make it on board." | `<ship hostile="true"/>` + `<boarders min="1" max="3" class="slug"/>` — **1–3 Slug boarders**, default rewards |
| 2 | "On your way back to the airlock, one of your crewmembers is taken out by a well aimed Slug blaster shot." | `<ship hostile="true"/>` + `<removeCrew><clone>true</clone></removeCrew>` — **lose a crew member**, default rewards. With a Clone Bay: *"Fortunately, your crewmember was immediately revived by the Clone Bay."* |
| 3 | "You cautiously board their ship and immediately smell the stale air of a malfunctioning life support. In no time at all you're able to fix up the problem…" | `<autoReward level="HIGH">scrap_only</autoReward>` |

The `<clone>true</clone>` flag means a Clone Bay fully cancels entry 2's crew loss
([[source-events-slug]]).

## Blue Options
- **Mantis crew member** (`req="mantis"`) — converts a 2-in-3 trap into the event's best
  outcome with no fight, no boarders and no crew risk. One of the cleanest blue options in
  the Slug pool.

## Rewards & Risks
- Best: `HIGH scrap_only` — via the Mantis option (guaranteed) or entry 3 (1 in 3).
- Worst: a permanent crew loss, unless you run a Clone Bay.
- Middle: 1–3 Slug boarders plus a `JELLY` fight at default rewards.
- Choice 2 is always free.

## Strategy Notes
- With a Mantis aboard, this is free scrap — take choice 3 every time.
- Without one, choice 1 risks a crew member for a 1-in-3 shot at high scrap. With a Clone
  Bay installed the crew-loss entry is neutralised, which materially improves the gamble.
  *(Opinion, from the `<clone>` flag and the three-entry list in [[source-events-slug]].)*
- The missing `<distressBeacon/>` tag means this arrives unannounced at an ordinary beacon.

## Related
- [[event-slug-hacker-oxygen]] — the hostile oxygen-sabotage event, easily confused by name
- [[event-mantis-ship-attacking-slug-ship]], [[event-slug-ship-boarding-rock-ship]],
  [[event-slug-moons-question]], [[event-slocknog]] — the rest of `DISTRESS_BEACON_SLUG`
- [[entity-mantis]], [[entity-slugs]], [[item-clone-bay]]

## Open Questions
- [ ] Whether the three list entries are equally weighted.
- [ ] Whether the missing `<distressBeacon/>` is fixed in any later build.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-slug-oxygen-malfunction]] (per raw/wiki/slug-oxygen-malfunction.md)
