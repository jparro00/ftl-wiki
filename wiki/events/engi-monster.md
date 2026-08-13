---
id: event-engi-monster
type: event
event_name: ENGI_MONSTER
sectors: []
beacon_type: unknown
hostile: false
blue_options: [sensors lvl 3, [[item-long-ranged-scanners]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [orphan, unreachable, cut-content, blue-option, augment-reward]
---

# Engi monster — `ENGI_MONSTER`

## Summary
A finished, fully-written unique event that **cannot be reached in normal play**: its only
reference in the event lists is commented out. You jump in, an Engi science vessel warns
you not to see the creature, and you realise you are inside it. Scanners turn that into a
free augmentation; without them you just leave.

## Trigger & Where It Appears
- **Not in any sector event list.** The single reference to it is
  `<!-- <event load="ENGI_MONSTER"/> -->` inside the `ITEMS_ENGI` list — commented out
  ([[source-events-xml]], per `raw/gamedata/events_engi.xml`). No `sector_data.xml` entry
  allocates it directly either ([[source-sector-data-xml]]).
- No other event, ship block, or `<quest>` tag loads it, so unlike the
  `ENGI_UNLOCK_*` orphans there is no alternative route in.
- The definition carries an unresolved developer note —
  `<!-- TO DO - Need black image!!!!!! JUSTIN!!!! -->` — and a placeholder background
  (`<img back="BG_DARK" planet="NONE"/>`), which is consistent with content shelved before
  release ([[source-events-xml]]).
- `unique="true"`.
- **No Fandom page for this event was supplied in this batch**, which is itself weak
  corroboration that players do not encounter it.

## Text
> As you jump in you're hailed urgently by an Engi science vessel in the distance. "We
> propose that you do not see the creature." There's nothing on the scanner, which is when
> you realize you can't see the creature because you're inside it!

(`event_ENGI_MONSTER_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Jump away ASAP. | — | Empty `<event/>` — nothing happens. | 100% |
| 2 | **(Improved Sensors)** Scan the monstrosity. | `req="sensors" lvl="3"` | *"You detect a faint, arrhythmic sub-wave pattern…"* → `<autoReward level="LOW">augment</autoReward>` — an **augmentation** with low scrap. | 100% |
| 3 | **(Long-Ranged Scanners)** Scan the monstrosity. | `req="ADV_SCANNERS"` | Identical text and reward to #2. | 100% |

`LOW` is the game's own `autoReward` level; the reward *type* is `augment`
([[source-events-xml]]).

## Blue Options
- **Sensors level 3** (`req="sensors" lvl="3"`) — the Sensors system at max level, a steeper
  gate than the level-2 requirement on [[event-engi-research-station]].
- **[[item-long-ranged-scanners]]** (`req="ADV_SCANNERS"`) — the augment satisfies the same
  gate with no system investment.

Either one converts a nothing-event into a free augmentation. There is no non-blue way to
get anything out of this beacon.

## Rewards & Risks
- An augmentation plus low scrap, if you can scan. Nothing otherwise.
- No risk in any branch — no ship, no crew effect, no hull damage ([[source-events-xml]]).

## Strategy Notes
- Academic: with the list entry commented out, this event should never appear in a normal
  run. It is recorded here because it is complete, shipped content rather than a test stub —
  the prose, the blue options and the reward are all fully specified.
- If a mod or a future patch re-enables the `ITEMS_ENGI` entry, it would be a strictly-free
  augmentation for any Sensors-3 or Long-Ranged Scanners ship. *(Opinion.)*

## Related
- [[event-engi-research-station]] — the other Engi event gated on Sensors / Long-Ranged Scanners
- [[item-long-ranged-scanners]]
- [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]] — where `ITEMS_ENGI` is drawn,
  and where this event would appear if enabled

## Open Questions
- [ ] Was this disabled deliberately, or is the commented-out list entry a leftover? The
      `TO DO - Need black image` note suggests the latter, but no source states it.
- [ ] Is it reachable in vanilla 1.0, or in the DLC-disabled event files? Not checked.
- [ ] Does any mod or `dlcEvents*.xml` overwrite re-add it? Not checked.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
