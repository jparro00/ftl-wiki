---
id: event-pirate-ship-distress-trap
type: event
event_name: TRAP_BEACON
sectors: [[[sector-abandoned-sector]], [[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: distress
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 14
tags: [unique, combat, forced-fight, distress, varies-text, default-rewards, pirate]
---

# Pirate ship distress trap — `TRAP_BEACON`

## Summary
The distress-beacon tax. A distress signal that is simply bait: you arrive, a pirate opens
fire, and there are no choices at all — the event body is three lines of XML. It is in
nine of the game's distress pools and appears in seventeen sector types, which makes it the
most common way a distress beacon turns into an unavoidable fight.

## Trigger & Where It Appears
- Sectors: seventeen — see the frontmatter list.
- Lists ([[source-newevents]], [[source-events-engi]], [[source-events-mantis]],
  [[source-events-pirate]], [[source-events-rebel]], [[source-events-rock]],
  [[source-events-slug]], [[source-events-zoltan]],
  [[source-dlcevents-anaerobic]]): `DISTRESS_BEACON` and its faction variants
  `DISTRESS_BEACON_ENGI`, `DISTRESS_BEACON_LANIUS`, `DISTRESS_BEACON_MANTIS`,
  `DISTRESS_BEACON_PIRATE`, `DISTRESS_BEACON_REBEL`, `DISTRESS_BEACON_ROCK`,
  `DISTRESS_BEACON_SLUG`, `DISTRESS_BEACON_ZOLTAN`.
- Beacon: carries `<distressBeacon/>` — it advertises itself as a distress signal on the
  map, which is the whole point.
- `unique="true"` — at most once per run.
- > ⚠️ **CONTRADICTION:** [[sector-federation-space]] coverage.
  > The Fandom `{{Locations}}` template omits Federation Space
  > ([[source-fandom-pirate-ship-distress-trap]]), but `STANDARD_SPACE` allocates
  > `<event name="DISTRESS_BEACON" min="1" max="2"/>` ([[source-sector-data-xml]]) and this
  > event is a member of `DISTRESS_BEACON` ([[source-newevents]]) — so it can appear there.
  > Trusting the game files (`high` vs `medium`); reading this as a gap in the Fandom
  > location list rather than a version difference, since no DLC marker is involved.
- Allocation of the distress buckets per sector is in [[source-sector-data-xml]] — see
  [[concept-sector-event-allocation]].

## Text
The prose **varies**: the body is a single `<text load="TRAP_BEACON_TEXT"/>` drawing one
of four entries from `textList TRAP_BEACON_TEXT` ([[source-events-xml]]). All four, per
[[source-text-events-xml]]:

> You arrive at the beacon and immediately detect a pirate ship. It seems this distress
> beacon was a trap!

> "Haha! I knew someone would fall into our dastardly trap!" It appears this distress
> beacon was nothing but a decoy for a pirate ambush.

> Your cockpit lights up with warning signals. You are being targeted by a nearby ship. The
> distress call was a lure to attract unwitting ships into weapons range. You prepare for a
> fight.

> As soon as you arrive at the distress signal, shots are fired toward your ship. A trap!

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none)* | — | `<ship load="PIRATE" hostile="true"/>` — an immediate, unavoidable fight with a pirate ship. Default rewards on victory. | 100% |

### The enemy — `PIRATE`

`auto_blueprint="SHIPS_PIRATE"`, per [[source-events-ships]]:

- `<surrender chance="0.5" min="3" max="4" load="PIRATE_SURRENDER"/>` — offered at 30–40%
  hull. Per [[concept-surrender-offers]], `chance` is the probability the ship **keeps
  fighting**, so this is a **50% surrender offer**.
- `<escape chance="0.5" min="2" max="4" load="PIRATE_ESCAPE"/>` — a 50% escape attempt in a
  *wider* band (20–40% hull) than the surrender band, so a damaged pirate may flee with
  your reward.
- `<destroyed load="DESTROYED_DEFAULT"/>` and `<deadCrew load="DEAD_CREW_DEFAULT"/>` —
  the standard reward blocks, which is what Fandom means by "default rewards"
  ([[source-fandom-pirate-ship-distress-trap]]).
- A `gotaway` text for when it escapes.

## Blue Options
None. The event has no choices at all, so nothing can gate one.

## Rewards & Risks
- Reward: default rewards for a pirate kill, or a `PIRATE_SURRENDER` payout if it gives up.
- Risk: a full fight with no opt-out, at a beacon you chose to visit expecting a distress
  reward. The pirate is auto-scaled to the sector, so the danger tracks how deep you are.
- The escape roll can deny you the reward entirely.

## Version differences
Nothing in the event, its `textList`, or its ship block carries a `<!--DLC-->` marker, and
`dlcEventsOverwrite.xml` does not redefine `DISTRESS_BEACON` or any of its faction variants
([[source-dlceventsoverwrite]]). The event is identical in both editions; only
`DISTRESS_BEACON`'s own membership changed (it gained `REFUGEE_GHOST` and
`REFUGEE_DISTRESS`, both DLC-marked, per [[source-newevents]]).

## Strategy Notes
- Because it is `unique="true"`, once it has fired in a run it cannot fire again — the
  remaining distress beacons in that run are that much safer. *Opinion, derived from the
  `unique` flag.*
- There is no way to scout it: it is indistinguishable from a genuine distress beacon on
  the map until you jump in. Fandom marks it `LRSmap=ship`, i.e. long-range scanners will
  at least tell you a ship is present ([[source-fandom-pirate-ship-distress-trap]]).
- Do not jump into an unscanned distress beacon at low hull expecting a gift.

## Related
- [[event-friendly-distress-beacon]] — the benign sibling that shares every distress pool
- [[event-single-life-form-on-moon]] — another `DISTRESS_BEACON` member, in this batch
- [[concept-surrender-offers]] — why `chance="0.5"` means a 50% surrender offer
- [[concept-sector-event-allocation]]
- [[entity-pirates]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Contents of `PIRATE_SURRENDER`, `PIRATE_ESCAPE`, `DESTROYED_DEFAULT` and
      `DEAD_CREW_DEFAULT` — the actual numbers behind "default rewards".
- [ ] Are the four intro texts equally weighted?
- [ ] Does the Long-Range Scanner reliably flag this beacon as hostile before the jump?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-dlceventsoverwrite]] (per `raw/gamedata/dlcEventsOverwrite.xml`)
- [[source-dlcevents-anaerobic]] (per `raw/gamedata/dlcEvents_anaerobic.xml`)
- [[source-events-engi]] (per `raw/gamedata/events_engi.xml`)
- [[source-events-mantis]] (per `raw/gamedata/events_mantis.xml`)
- [[source-events-pirate]] (per `raw/gamedata/events_pirate.xml`)
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-events-rock]] (per `raw/gamedata/events_rock.xml`)
- [[source-events-slug]] (per `raw/gamedata/events_slug.xml`)
- [[source-events-zoltan]] (per `raw/gamedata/events_zoltan.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-pirate-ship-distress-trap]] (per `raw/wiki/pirate-ship-distress-trap.md`)
</content>
