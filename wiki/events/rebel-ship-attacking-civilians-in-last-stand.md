---
id: event-rebel-ship-attacking-civilians-in-last-stand
type: event
event_name: BOSS_SCOUT_RESCUE
sectors: [[[sector-the-last-stand]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [rescue, optional-fight, hull-repair, stuff-reward, endgame, last-stand, rebel]
---

# Rebel ship attacking civilians in Last Stand — `BOSS_SCOUT_RESCUE`

## Summary
The only beacon in [[sector-the-last-stand]] that offers a real decision: a Rebel scout is
tearing into Federation civilians and you can either intervene or jump on. Intervening is
the sector's best-paying fight — `MED`/`HIGH` `standard` on the kill *plus* a hidden
follow-up that rolls a three-way rescue reward — but it is also the only Last Stand enemy
that can escape mid-fight.

## Trigger & Where It Appears
- Sector: [[sector-the-last-stand]] (`FINAL`).
- Beacon: neutral on arrival; combat only if you choose it. Long-range scanners show **no**
  ship ([[source-fandom-rebel-ship-attacking-civilians-in-last-stand]]).
- Event list: `BOSS_NEUTRAL` — five distinct entries → **1/5**, assuming uniform selection
  across list entries ([[source-events-boss]]). `FINAL` allocates `BOSS_NEUTRAL`
  `min=7 max=10` ([[source-sector-data-xml]]).
- The XML comment: *"player rescues weakened fed/civilian ship from a rebel scout — fight
  with rescue."*

## Text
Drawn from the `BOSS_SCOUT_RESCUE` text list, which is **weighted**: it has eight entries
covering five distinct strings — `_1` and `_2` once each, `_3`, `_4` and `_5` twice each.
Assuming uniform selection across list entries that gives 1/8 for the first two and 2/8
each for the other three ([[source-events-boss]], [[source-text-events-xml]]).

> Shots fly by your port windows followed by a Rebel scout in pursuit of a damaged cruiser.
> Should we move in to engage?

> A number of large transports are being pursued by a Rebel bombing squadron. One bomber has
> managed to slip through the defensive fire, and is poised to wreak havoc among the
> enormous yet vulnerable transports. There's time for you to advance and take it out!

> A civilian ship is broadcasting a request for assistance on a secure Federation channel.
> They are being harassed by Rebel scouts. Will you respond?

> ⚠️ **CONTRADICTION:** the third string drops a word on Fandom.
> - Game files: *"…is poised to wreak **havoc** among the enormous yet vulnerable
>   transports."* (`text_BOSS_SCOUT_RESCUE_3`, [[source-text-events-xml]])
> - Fandom: *"…is poised to wreak among the enormous yet vulnerable transports."*
>   ([[source-fandom-rebel-ship-attacking-civilians-in-last-stand]])
>
> Trusting the game files — reliability `high` vs `medium`, and the omission reads as a
> transcription slip rather than a version difference.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Prepare to fight the Rebel ship! | — | *"You move in to intercept."* → combat with `<ship load="BOSS_SCOUT_RESCUE" hostile="true"/>`. See the branch table below. | 100% (deterministic) |
| 2 | There's no time, get ready to jump. | — | *"You try to block out the horrors of war and focus on your mission."* → nothing happens. | 100% |

### The `BOSS_SCOUT_RESCUE` ship
Defined in `events_boss.xml` on the `SHIPS_REBEL` auto-blueprint ([[source-events-boss]]):

| Branch | Behaviour |
|---|---|
| `surrender` | none |
| `escape` | `chance="0.5"`, `min="4" max="8"`, loads the shared `PIRATE_ESCAPE` event — *"The enemy ship appears to be powering up its FTL. It's trying to escape!"* ([[source-events-xml]]) |
| `destroyed` | *"With the Rebel ship destroyed you are free to contact their would-be victim."* → `autoReward level="MED"` `standard`, then a hidden `"Contact the survivors."` choice → rolls `BOSS_SCOUT_RESCUE_LIST` |
| `deadCrew` | *"With the Rebel ship defeated you quickly salvage what you can and move to contact their prey."* → `autoReward level="HIGH"` `standard`, then the same hidden choice → `BOSS_SCOUT_RESCUE_LIST` |

[[source-fandom-rebel-ship-attacking-civilians-in-last-stand]] renders the escape branch as
50% / 40–80 / 4–8 and reports the same `MED` / `HIGH` reward split.

### `BOSS_SCOUT_RESCUE_LIST` — the rescue payoff
A three-entry list with three distinct outcomes → **1/3 each**, assuming uniform selection
across list entries ([[source-events-boss]]):

| Outcome | Effect |
|---|---|
| *"The people you rescued were primarily refugees fleeing the conflict. They offer you their sincere gratitude."* | nothing |
| *"…we can repair a bit of damage before you jump off into the war. Good luck!"* | `<damage amount="-8"/>` → **+8 hull** |
| *"Take some supplies, we probably won't need them at this point."* | `autoReward level="MED"` **`stuff`** |

Fandom tooltips the `MED` `stuff` reward as fuel 2–4, missiles 2–4, drone parts 1, plus
some scrap ([[source-fandom-rebel-ship-attacking-civilians-in-last-stand]]); the game files
give only the level and payload type.

### Which hull you fight
> ⚠️ **Version difference (AE vs vanilla).** `SHIPS_REBEL` (vanilla: `REBEL_FAT`,
> `REBEL_SKINNY` — 1/2 each) is replaced in Advanced Edition by `OVERRIDE_SHIPS_REBEL`
> (`REBEL_FAT` ×2, `REBEL_SKINNY` ×2, `REBEL_FAT_DLC`, `REBEL_SKINNY_DLC` — 2/6, 2/6,
> 1/6, 1/6), assuming uniform selection across list entries ([[source-autoblueprints]],
> [[source-dlcblueprintsoverwrite]]).

## Blue Options
None — the event has no `req`-gated choices.

## Rewards & Risks
- Fight: `MED` `standard` (hull kill) or `HIGH` `standard` (crew kill), **plus** a 1/3 shot
  at +8 hull and a 1/3 shot at `MED` `stuff`.
- Risk: a 50% escape branch means the ship can jump out before you finish it, forfeiting
  the reward chain. This is the only Last Stand enemy with an escape branch
  ([[source-events-boss]]).
- Declining costs nothing at all.

## Strategy Notes
- The highest expected value of any Last Stand beacon short of a repair station: taking the
  fight is strictly better than skipping it unless your hull cannot absorb another
  engagement. *(Opinion, derived from the reward tags; no source states it.)*
- Killing the crew rather than the hull upgrades `MED` → `HIGH` `standard` and still
  unlocks the rescue list ([[source-events-boss]]).

## Related
- [[event-rebel-fight-among-federation-and-rebel-fleets]] — the hostile draw from the same list
- [[event-empty-beacon-last-stand]] — the harmless draw from the same list
- [[event-rebel-fight]] (`REBEL`) and [[event-rebel-ship-attacking-refueling-outpost]]
  (`SQUAT_REFUEL_STATION`) — the remaining `BOSS_NEUTRAL` members
- [[sector-the-last-stand]]
- [[entity-rebels]], [[entity-federation]]
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] What Fandom's "40–80" figure on the escape branch corresponds to; the XML has only
      `chance="0.5" min="4" max="8"`.

## Sources
- [[source-events-boss]] (per raw/gamedata/events_boss.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-autoblueprints]] (per raw/gamedata/autoBlueprints.xml)
- [[source-dlcblueprintsoverwrite]] (per raw/gamedata/dlcBlueprintsOverwrite.xml)
- [[source-fandom-rebel-ship-attacking-civilians-in-last-stand]] (per raw/wiki/rebel-ship-attacking-civilians-in-last-stand.md)
