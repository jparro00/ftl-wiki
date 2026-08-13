---
id: event-zoltan-rift-success
type: event
event_name: ZOLTAN_RIFT_SUCCESS
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [aftermath, scrap-reward, orphan, zoltan]
---

# Zoltan rift — victory aftermath — `ZOLTAN_RIFT_SUCCESS`

## Summary
The payout event that fires after you win any of the three fights the mad Zoltan wise man
summons at [[event-zoltan-wise-man]]. It has no choices and no risk: the wise man implodes
and showers you with salvage. It exists as its own event because all six endings of the
three summoned ships load it, and it is the reason the wise man encounter pays **twice**.

## Trigger & Where It Appears
- **Not in any sector event list**, which is why the batch marks it an orphan. It is
  reached only through `events_ships.xml`: each of `ZOLTAN_RIFT_MANTIS`,
  `ZOLTAN_RIFT_SLUG` and `ZOLTAN_RIFT_ROCK` ends both its `<destroyed>` and its
  `<deadCrew>` block with a hidden continue that loads this event
  ([[source-events-ships]]) — six references in total.
- Those three ships are summoned only by [[event-zoltan-wise-man]]
  (`ZOLTAN_RIFT_FIGHT`), which sits in `NEUTRAL_ZOLTAN` and therefore appears only in
  [[sector-zoltan-controlled-sector]] and [[sector-zoltan-homeworlds]]
  ([[source-events-zoltan]], [[source-sector-data-xml]]).
- Consequently it fires **on every win**, whichever of the three enemies you chose and
  whether you destroy the hull or kill the crew. There is no branch of the parent event
  that skips it except losing, fleeing, or the enemy escaping.
- No Fandom page joins this event; the community wiki folds it into the wise man's page.

## Text
> When he sees you have emerged victorious, the Zoltan wise man enters a rage. Rifts
> threaten to tear space apart until, instead, the Zoltan implodes, sending a blast wave
> of scrap and salvage dragged here from distant worlds in your direction.

(`event_ZOLTAN_RIFT_SUCCESS_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | None. | — | `<autoReward level="HIGH">standard</autoReward>` — **high scrap with resources**. Nothing else. | 100% |

([[source-events-zoltan]])

## The double payout
The ship you just beat has already paid out before this event runs
([[source-events-ships]]):

| Ship | Blueprint | Destroyed | Dead crew |
|---|---|---|---|
| `ZOLTAN_RIFT_MANTIS` | `SHIPS_MANTIS` | `LOW` `standard` | `MED` `standard` |
| `ZOLTAN_RIFT_SLUG` | `SHIPS_JELLY` | `LOW` `standard` | `MED` `standard` |
| `ZOLTAN_RIFT_ROCK` | `SHIPS_ROCK` | `LOW` `standard` | `MED` `standard` |

All three use the same aftermath text — *"You salvage the remains and contact the wise
man."* (destroyed) / *"You salvage the ship and contact the wise man."* (dead crew)
([[source-text-events-xml]]). Then `ZOLTAN_RIFT_SUCCESS` adds `HIGH` `standard` on top.

None of the three declares a `<surrender>` or an `<escape>` block, so the fight always
runs to one of the two paying endings.

## Blue Options
None.

## Rewards & Risks
- **Reward:** `HIGH` `standard` — the game's own words for high scrap with resources. This
  is a *second* reward stacked on the ship's own.
- **Risk:** none. By the time this event runs the fight is already over.

## Strategy Notes
- The only decision that touches this event is made one step earlier: killing the enemy
  crew pays `MED` instead of `LOW` on the ship, and this payout is unaffected either way.
  Board if you can.
- *Opinion:* the existence of this second payout is the whole argument for taking the wise
  man's fight rather than avoiding the beacon — see [[event-zoltan-wise-man]] for the
  choice itself.

## Related
- [[event-zoltan-wise-man]] — the parent event; this is its aftermath
- [[event-zoltan-ship-asks-to-dock]], [[event-zoltan-trade-hub]] — the other
  `NEUTRAL_ZOLTAN` / `QUESTS_ZOLTAN` encounters that can turn into a fight

## Open Questions
- [ ] Does fleeing the fight (or the enemy escaping) forfeit this payout entirely? Nothing
      in the ship blocks handles a `gotaway` case, which suggests yes.
- [ ] The parent event has a commented-out fourth option, "Crystalline Beings", with a
      developer to-do and no ship assigned ([[source-events-zoltan]]) — would it have
      loaded this same aftermath?

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
