---
id: concept-ship-unlocks
type: concept
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
related_events: []
tags: [mechanics, meta-progression, ship-unlock, chains, inverted-win-conditions]
---

# Ship unlocks

## Definition & Context

`<unlockShip id="N"/>` — **12 uses** across the event files ([[source-events-xml]] and
siblings), spread over **7 distinct ship ids**. It is the only effect in FTL that changes
anything outside the current run.

| id | Ship | Uses | Route |
|---|---|---|---|
| 1 | [[entity-stealth-cruiser]] | 1 | [[chain-stealth-cruiser-unlock]] |
| 2 | [[entity-mantis-cruiser]] | **4** | [[chain-mantis-cruiser-unlock]] |
| 4 | — | 1 | not identified in this raw set |
| 5 | [[entity-zoltan-cruiser]] | 2 | [[chain-zoltan-cruiser-unlock]] |
| 6 | [[entity-rock-cruiser]] | 1 | [[chain-rock-cruiser-unlock]] |
| 7 | Crystal Cruiser | 2 | [[chain-crystal-cruiser-unlock]] |
| 8 | Lanius (Anaerobic) Cruiser | 1 | AE, Lanius content |

**Ship 3 never appears.** The [[entity-federation-cruiser]] is unlocked by
[[event-rebel-shipyard]] and the Engi Cruiser by an achievement — neither through
`<unlockShip>` in the event files, which is where the numbering gap comes from.

## The pattern: unlocks fail silently on the obvious play

This is the most important thing the wiki has learned about unlock chains, found across
**three of them independently**:

| Chain | The obvious play | What actually advances it |
|---|---|---|
| [[chain-rock-cruiser-unlock]] | destroy the Rock ship in the sun duel | **let it escape** — the `<quest>` tag is on `<gotaway>` |
| [[chain-mantis-cruiser-unlock]] | destroy KazaaakplethKilik's ship | **kill the crew** — `MANTIS_NAMED_THIEF_DEFEAT` fires on `deadCrew` |
| [[chain-slug-cruiser-unlock]] | destroy the Slug ship | **force its surrender** |
| [[chain-capture-the-ship]] (not an unlock, same shape) | destroy the target | **kill the crew intact** |

In every case, winning the fight the ordinary way carries no `<quest>` tag and the chain ends
with no message. The game does not tell you that you have just lost a ship unlock.

## The other shapes

- **Guaranteed by sector arrival.** [[event-start-beacon-crystal]] plants the Crystal marker
  simply for reaching [[sector-hidden-crystal-worlds]] — see [[concept-start-beacons]].
- **Guaranteed by sector allocation.** [[chain-mantis-cruiser-unlock]]'s opening beacon and
  [[chain-rock-cruiser-unlock]]'s are both allocated `min=1 max=1`, so the *opportunity* is
  guaranteed even where the outcome is not.
- **A single hard fight.** [[event-rebel-shipyard]] unlocks the Federation Cruiser with no
  chain at all.
- **Diplomacy.** [[chain-zoltan-cruiser-unlock]]'s step 2 looks like a Rebel ambush and is a
  test; exactly one choice passes, and shooting is not it.

## What the data cannot tell us

`achievements.xml` contains **no unlock-condition entries at all** ([[source-achievements]]),
and `text_achievements.xml` holds only prose. So:

> ⚠️ **CONTRADICTION:** Fandom describes **alternative unlock routes** for several cruisers —
> the Rock Cruiser by winning with the Slug Cruiser, the Mantis Cruiser by winning with the
> Zoltan Cruiser, and others. None can be verified or refuted from this raw set, because the
> conditions are not in the files. Recorded as Fandom-only on each affected page. The
> `ship_PLAYER_SHIP_*_unlock` hint strings in [[source-text-blueprints]] describe **only the
> event routes**, which is suggestive but not decisive — they are one-line marketing copy.

## Implications For Play

- **Know the inversion before you commit.** On [[chain-rock-cruiser-unlock]] and
  [[chain-mantis-cruiser-unlock]], turn your weapons *off* at the critical moment.
- **Route for the sector.** Every unlock chain is gated behind reaching a specific sector type,
  and several compete for the same late-run slot — [[sector-rock-homeworlds]] holds both the
  Rock chain's opener and [[chain-crystal-cruiser-unlock]]'s step 3.
- **Ion and crew-kill weapons are actively dangerous** in chains where `deadCrew` ends the
  chain, and actively required in the one where it advances it.

## Where It Applies
The seven chain pages: [[chain-stealth-cruiser-unlock]], [[chain-mantis-cruiser-unlock]],
[[chain-zoltan-cruiser-unlock]], [[chain-rock-cruiser-unlock]],
[[chain-crystal-cruiser-unlock]], plus [[event-rebel-shipyard]] and the Lanius route.

## Related
- [[entity-rock-cruiser]], [[entity-stealth-cruiser]], [[entity-mantis-cruiser]],
  [[entity-zoltan-cruiser]], [[entity-federation-cruiser]] — the ships themselves
- [[concept-quest-beacon-placement]] — how an unlock quest can be silently cancelled
- [[concept-surrender-offers]] — the mechanic two unlock chains hinge on
- [[concept-start-beacons]] — the guaranteed-hook pattern

## Open Questions
- [ ] **Ship id 4** — one `<unlockShip id="4"/>` exists and this raw set does not identify
      which ship it is.
- [ ] Whether Fandom's alternative victory-based routes exist at all.
- [ ] Whether an unlock persists if the run is subsequently lost — almost certainly yes, but
      nothing in the files states it.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-achievements]] (per raw/gamedata/achievements.xml)
