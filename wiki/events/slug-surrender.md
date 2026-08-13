---
id: event-slug-surrender
type: event
event_name: SLUG_SURRENDER
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-federation-space]], [[sector-civilian-sector]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [surrender, aftermath, fuel-reward, orphan, slug]
---

# Slug surrender — `SLUG_SURRENDER`

## Summary
The surrender offer made by the standard Slug hull. Accepting ends the fight and pays out
one of three bundles — a large fuel drop, a small mixed haul, or a medium mixed haul.
Refusing simply resumes the fight. It is the reason a `JELLY` fight is worth pushing to
low hull rather than finishing at range.

## Trigger & Where It Appears
- **Not in any sector event list** — which is why the batch marks it an orphan. It is
  reached only through `events_ships.xml`: the `JELLY` ship declares
  `<surrender chance="0.5" min="3" max="4" load="SLUG_SURRENDER"/>`
  ([[source-events-ships]]).
- Per [[concept-surrender-offers]], `chance` is the probability the ship **keeps
  fighting**, so `chance="0.5"` means a **50% surrender chance** once hull falls into the
  `min=3 max=4` band.
- Every hostile `JELLY` encounter can therefore reach it ([[source-events-slug]],
  [[source-events-rebel]]):
  - [[event-slug-fight]] (`SLUG_FIGHT`)
  - [[event-slug-fight-in-nebula]] (`NEBULA_SLUG_FIGHT`)
  - [[event-slug-fight-in-plasma-storm]] (`STORM_SLUG_FIGHT`)
  - `NEBULA_SLUG_HULLFIX` and `NEBULA_SLUG_FAKE_STORE`, whose betrayal branches load
    `JELLY` hostile
  - `AUTO_HACKER` in `events_rebel.xml` — its **(Hacking System)** blue branch loads a
    `JELLY` hostile. `AUTO_HACKER` sits in `HOSTILE1` / `OVERRIDE_HOSTILE1`
    ([[source-newevents]], [[source-dlceventsoverwrite]]), allocated `min=2 max=2` in
    [[sector-federation-space]] and [[sector-civilian-sector]]
    ([[source-sector-data-xml]]) — which is why those two sectors appear above despite
    having no Slug content of their own
- Not reachable in the [[sector-slug-home-nebula]] unlock fight: that uses
  `JELLY_UNLOCK1`, which loads [[event-slug-unlock-surrender]] instead.
- No Fandom page joins this event directly; the community wiki documents it inside the
  parent fights (e.g. as "Template:Slug ship surrenders").

## Text
> "You have besssted us! Will you accept what is in our storeesss in exchange for our
> livess?"

(`event_SLUG_SURRENDER_text`, per [[source-text-events-xml]])

**This is word-for-word identical to [[event-slug-unlock-surrender]]**, the special
surrender that starts the Slug Cruiser unlock chain. There is no way to tell the two
apart from the prompt — the difference only shows after you accept.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Let them live. | — (`hidden="true"`) | Loads `SLUG_SURRENDER_LIST` — three entries, below. Each sets `<ship hostile="false"/>`, ending the fight. | — |
| 2 | We will not accept surrender! | — (`hidden="true"`) | `<event/>` — nothing; the fight continues. | 100% |

### `SLUG_SURRENDER_LIST` — three entries, no repeats (1/3 each)
**Assuming uniform selection across list entries** ([[concept-event-list-weighting]]):

| Odds | Text | Effect |
|---|---|---|
| 1/3 | *"Here! We have lotsss of fuel! Take it all!"* | `<autoReward level="HIGH">fuel_only</autoReward>` |
| 1/3 | *They transfer a meager amount of material. "There... now keep your word..."* | `<autoReward level="LOW">stuff</autoReward>` |
| 1/3 | *"Take it and leave ussss be."* | `<autoReward level="MED">stuff</autoReward>` |

All three also set `<ship hostile="false"/>` — the fight is over
([[source-events-slug]]).

## Blue Options
None. No `req` attribute appears on either choice.

## Rewards & Risks
- **Reward:** one of `HIGH` `fuel_only`, `LOW` `stuff`, or `MED` `stuff` — the game's own
  words. `fuel_only` is unusual: most surrender tables pay mixed resources, and a large
  fuel drop is genuinely useful in the fuel-hungry Slug sectors.
- **Cost of accepting:** the kill. You forgo `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT`
  rewards, which are typically larger and include scrap.
- **Refusing is free** — choice 2 has no penalty beyond the fight you were already in.

## Strategy Notes
- *Opinion:* refuse unless you are damaged, low on fuel, or the enemy is still dangerous.
  Two of the three payouts (`LOW` `stuff`, `HIGH` `fuel_only`) carry little or no scrap,
  and scrap is the resource that wins runs.
- Accept when fuel is the constraint: a `HIGH` `fuel_only` roll is a third of the table
  and can rescue a stranded route.
- In [[sector-slug-home-nebula]], **do not reflexively refuse.** One `JELLY`-looking fight
  per sector is actually `JELLY_UNLOCK1`, whose identical prompt leads to
  [[event-slug-unlock-surrender]] and the Slug Cruiser chain. Accepting is the only way to
  find out which one you are in.

## Related
- [[event-slug-unlock-surrender]] — the visually identical surrender that starts the ship
  unlock
- [[event-slug-fight]], [[event-slug-fight-in-nebula]],
  [[event-slug-fight-in-plasma-storm]] — the fights that lead here
- [[event-slug-home-nebula-surrender]] — the unlock fight this one is confused with
- [[concept-surrender-offers]] — why `chance="0.5"` means 50% surrender
- [[concept-event-list-weighting]] — basis for the 1/3 figures

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] What `HIGH` `fuel_only` pays in fuel units.
- [ ] Does refusing the surrender re-roll the offer later in the same fight, or is it a
      one-shot?

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-rebel]] (per raw/gamedata/events_rebel.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
