---
id: event-quest-slug-pirate-trap2
type: event
event_name: QUEST_SLUG_PIRATE_TRAP2
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: quest
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [quest-marker, nebula, slug, pirates, combat, surrender, unique, advanced-edition]
---

# Slug raid, joined — `QUEST_SLUG_PIRATE_TRAP2`

## Summary
The quest-marker payoff of [[event-slug-comm-tapping]]. You arrive mid-raid and choose
which pirate to fight: help the Slugs and split the cache fifty-fifty, or race them for it
and get nothing but the salvage. The two branches load **two different pirate hulls with
very different aftermaths** — helping is unambiguously the better deal.

## Trigger & Where It Appears
- **Not in any sector event list.** It is a **quest-marker beacon**, placed by
  `<quest event="QUEST_SLUG_PIRATE_TRAP2"/>` on the "Tap into their communications" branch
  of [[event-slug-comm-tapping]] ([[source-events-slug]]).
- Taking the parent's other choice (ignore them) never places the marker, so this event is
  simply not generated.
- Sectors are inherited from the parent: [[sector-slug-controlled-nebula]] and
  [[sector-slug-home-nebula]]. The parent is `unique="true"`.
- `<environment type="nebula"/>` — the beacon is a nebula, so **sensors are jammed** for
  the whole fight.
- **Version:** `ae`, matching the parent.
- Fandom documents this stage inside its *Slug comm tapping* page
  ([[source-fandom-slug-comm-tapping]]).

## Text
> You catch up with the two Slug ships and they're already carrying out their raid! One is
> in close combat with the pirate, the other seems to be heading for a small space cache the
> pirate was protecting.

(`event_QUEST_SLUG_PIRATE_TRAP2_text`, per [[source-text-events-xml]])

A single hidden continue leads to the actual decision:

> Suddenly the first ship bursts into flames, and an urgent call arrives from the remaining
> Slugs. "We sssugest you distract the pirate vesssel while we retrieve the valuables. Fifty
> fifty sssplit."

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Engage the pirate. | — | *"There's money to be made here. The Slugs know that. You turn on the pirate and intercept just before he can reach the cache!"* → fight **`QUEST_SLUG_PIRATE_TRAP1`**. | 100% |
| 2 | Head for the cache. | — | *"When he sees you making for the cache the Slug captain hails: 'Foolish alienss, no eye for profit. Bessst of luck to you.' They jump off, leaving you toe to toe with the pirate!"* → fight **`QUEST_SLUG_PIRATE_TRAP2`**. | 100% |

### Choice 1 — the `QUEST_SLUG_PIRATE_TRAP1` hull

| Resolution | Outcome |
|---|---|
| **Surrender** (`chance="0" min="3" max="4"`) — a **guaranteed** offer under [[concept-surrender-offers]] | *"When the pirate ship looks ready to break apart you notice the Slug ship has secured the loot and is preparing to jump away!"* |
| ↳ Continue fighting the pirate. | *"It's best you finish this — but you wonder whether what the pirate is carrying will be as valuable as what the Slugs snuck off with."* → the fight continues to destroyed/deadCrew. |
| ↳ Let the pirate escape and go after the Slugman ship. | *"…they transfer over a decent chunk of the profits and set off."* → `HIGH scrap_only` and `<ship hostile="false"/>`. |
| **Destroyed** | *"With the pirate defeated you scan the debris for anything useful. The Slug ship is long gone, spoils from the cache in hand."* → `MED standard` |
| **Dead crew** | same text → `HIGH standard` |

### Choice 2 — the `QUEST_SLUG_PIRATE_TRAP2` hull

| Resolution | Outcome |
|---|---|
| **Destroyed** | *"With the pirate taken care of, you search again for the cache he was protecting, but it's lost in the clouds."* → `LOW standard` |
| **Dead crew** | *"…You console yourself with the salvage from the well-armed pirate ship."* → `MED standard` |

This hull has **no surrender and no escape block at all** — the fight runs to a conclusion
([[source-events-ships]]).

## Blue Options
None. No `req` appears anywhere in this event or either ship block.

## Rewards & Risks
- **Choice 1 is strictly better.** Its worst case (`MED standard`) equals choice 2's best
  case, and its guaranteed surrender offer opens a `HIGH scrap_only` exit that ends the
  fight early.
- Both hulls use `auto_blueprint="SHIPS_PIRATE"` — the same pirate hull family, so the
  fights themselves are comparable in difficulty.
- The nebula jams your sensors for both fights.
- No branch damages you outright and no branch costs crew.

## Strategy Notes
- *Opinion:* take choice 1 every time. The Slugs are not lying about the split, and the
  guaranteed surrender lets you cash out of a fight that has gone badly.
- Within choice 1, "let the pirate escape" is the right call if you are damaged — `HIGH
  scrap_only` with zero further risk. If your boarders are already aboard, refuse and go for
  `HIGH standard` instead.
- Choice 2 is the greed trap the event is named for: you cut out the Slugs and end up with
  `LOW standard`.

## Related
- [[event-slug-comm-tapping]] — the parent and only route here
- [[entity-slugs]], [[entity-pirates]] — the parties involved
- [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]] — where the parent appears
- [[concept-surrender-offers]] — why `chance="0"` is a guaranteed offer

## Open Questions
- [ ] Exact scrap values behind `HIGH scrap_only`, `MED standard`, `LOW standard` here.
- [ ] Whether the two hulls differ in loadout, or only in their aftermath blocks — both
      share `auto_blueprint="SHIPS_PIRATE"`.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-fandom-slug-comm-tapping]] (per raw/wiki/slug-comm-tapping.md)
