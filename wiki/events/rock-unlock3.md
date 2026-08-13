---
id: event-rock-unlock3
type: event
event_name: ROCK_UNLOCK3
sectors: []
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-rock-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [rock, ship-unlock, quest, orphan, augment-reward, hull-repair]
---

# Rock cruiser unlock, step 3 — `ROCK_UNLOCK3`

## Summary
The payoff beacon of the Rock Cruiser chain. It unlocks **ship 6 — the Rock Cruiser** —
and then, on a follow-up continue, hands you the **Rock Plating** augment and repairs
**29 hull**. There are no real choices; it is a reward delivery.

## Trigger & Where It Appears
- **Not in any sector event list.** `ROCK_UNLOCK3` appears in no `eventList` and in no
  `sectorDescription` ([[source-events-rock]], [[source-sector-data-xml]]) — it is an
  orphan by allocation.
- It is reached **only** through the chain: the `<gotaway>` branch of the `ROCK_UNLOCK2`
  enemy ship fires `<quest event="ROCK_UNLOCK3"/>`, placing the beacon on your map
  ([[source-events-ships]]). See
  [[event-rock-unlock1]] for steps 1–2.
- Because the entry point is guaranteed only in [[sector-rock-homeworlds]], that is where
  the chain begins — but nothing in the files pins *this* beacon to a sector, so
  `sectors:` is left empty rather than guessed.
- Beacon: ship present, non-hostile — `<ship load="ROCK_UNLOCK1" hostile="false"/>`
  ([[source-events-rock]]). Note this loads the `ROCK_UNLOCK1` **ship**
  (`auto_blueprint="ROCK_ASSAULT_ELITE"`), which is a different thing from the
  `ROCK_UNLOCK1` **event**.
- Not marked `unique` ([[source-events-rock]]).
- **Fandom coverage:** [[source-fandom-rock-war-vessel-encounter]] (per
  `raw/wiki/rock-war-vessel-encounter.md`) documents this beacon as the *"Shipyard Quest
  Marker"* section of its *Rock war vessel encounter* article, and confirms it is reached by
  the got-away branch of the sun fight. It adds that **Long-Ranged Scanners report a ship**
  at this beacon (no environment hazard, unlike the step-2 marker). It gives no sector for
  the marker, so `sectors:` stays empty.

## Text
> You arrive at a massive Rockman shipyard and notice the ship that had just tried to kill
> you is docked and already being repaired. "Well fought! I must say I did not expect you
> to survive."

(`event_ROCK_UNLOCK3_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | *(continue — the choice has no label)* | — | *"I am convinced of your strength and pledge to assist your cause. We'll immediately send an advanced cruiser to the Federation fleet and we will prepare our warships to move out."* → **`<unlockShip id="6"/>`** | 100% |
| 1a | *(continue again)* | — | *"Now that that's taken care of, let us patch up your hull. Maybe we can improve its armor plating while we're at it."* → `<augment name="ROCK_ARMOR"/>` and `<damage amount="-29"/>` | 100% |

The second continue is a nested `<choice>` inside the first outcome, not a separate
event ([[source-events-rock]]). There is no way to decline either half.

`<damage amount="-29"/>` is negative damage, i.e. **29 hull repaired**. On a stock
30-hull cruiser that is very nearly a full heal.

## Blue Options
None.

## Rewards & Risks
- **Ship unlock:** `unlockShip id="6"`. Id 6 is the Rock Cruiser — `blueprints.xml`
  carries an explicit `<!-- SHIP ID = 6 -->` comment on the Rock ship blueprint block
  (`PLAYER_SHIP_ROCK` / `PLAYER_SHIP_ROCK_2`), which is the only mapping of numeric ids
  to ships available in this raw set. Treated as high-confidence but derived from a source
  comment rather than a declared field. **Fandom independently states this beacon unlocks
  the Rock Cruiser** ([[source-fandom-rock-war-vessel-encounter]]), which corroborates the
  id→ship reading from a second, independent direction.
- **Augment:** [[item-rock-plating]] (`ROCK_ARMOR`) — the same augment that gates the blue
  option on [[event-mantis-ship-with-rock-body-parts]]. It is `stackable=false` with
  `rarity 0` (i.e. not sold in stores) and a listed cost of 80
  ([[source-blueprints]]). Fandom names the reward **Rock Plating**, matching
  `aug_ROCK_ARMOR_title` = "Rock Plating" ([[source-text-blueprints]]).
- **Hull:** +29. Fandom states *"29 repairs"* verbatim
  ([[source-fandom-rock-war-vessel-encounter]]) — an exact match for `<damage amount="-29"/>`,
  and the only outside confirmation that negative `damage` is hull repair.
- **Risk: none.** The ship is non-hostile and there is no failure branch.

> ⚠️ **CONTRADICTION (design comment vs. shipped event):** the developer note at the top
> of the SPECIAL section of `events_rock.xml` describes the chain as *"…then a normal fight
> and you must let them surrender"* ([[source-events-rock]]). The shipped `ROCK_UNLOCK3`
> contains **no fight and no surrender** — it is a pure reward event, and the "let them
> escape" condition sits on `ROCK_UNLOCK2` instead. Reading this as a stale design comment
> describing a cut third fight, not as evidence of a missing step. Recorded rather than
> deleted because it is the only in-file statement of the chain's intended shape.

> ⚠️ **CONTRADICTION (minor, Fandom link target):** Fandom's reward line reads *"Rock
> Plating augmentation"* but links it to `Augmentations#Titanium_System_Casing`
> ([[source-fandom-rock-war-vessel-encounter]]). These are two different augments in the
> game files: `ROCK_ARMOR` = "Rock Plating" (15% chance to negate incoming hull damage) and
> `SYSTEM_CASING` = "Titanium System Casing" — separate `augBlueprint` blocks
> ([[source-blueprints]], [[source-text-blueprints]]). The visible name is right and the
> anchor is wrong; trusting the game files, the award is `ROCK_ARMOR`
> ([[source-events-rock]]). Worth flagging because the mis-anchor could propagate into any
> summary built from the Fandom page.

## Strategy Notes
- Nothing to decide here; the value of the beacon is entirely in having reached it. The
  29-hull repair alone makes the detour worth taking even on a run where you already own
  the Rock Cruiser. *(Opinion.)*
- The chain rewards *restraint* at step 2 and pays out here — see [[event-rock-unlock1]]
  for the escape condition you must not break.

## Related
- [[chain-rock-cruiser-unlock]] — the chain this completes
- [[event-rock-unlock1]] — steps 1 and 2
- [[item-rock-plating]] — the augment granted
- [[ship-rock-cruiser]] — the ship unlocked
- [[event-mantis-ship-with-rock-body-parts]] — where Rock Plating pays off again
- [[event-rock-unlock2]] — step 2, the sun duel (`ROCK_UNLOCK2`)

## Open Questions
- [ ] Confirm `unlockShip id="6"` is the Rock Cruiser from an authoritative id table rather
      than an XML comment. Now corroborated by [[source-fandom-rock-war-vessel-encounter]],
      but still no declared id→ship field in the extracted files.
- [ ] Does the augment still arrive if your augment slots are full?
- [ ] Which sector the `ROCK_UNLOCK3` quest marker is placed in — Fandom does not say either.

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml — `aug_ROCK_ARMOR_title`,
  `aug_SYSTEM_CASING_title`)
- [[source-fandom-rock-war-vessel-encounter]] (per raw/wiki/rock-war-vessel-encounter.md)
