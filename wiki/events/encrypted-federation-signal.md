---
id: event-encrypted-federation-signal
type: event
event_name: FEDERATION_PLANET_SIGNAL
sectors: [[[sector-abandoned-sector]], [[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-hidden-federation-base]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [unique, quest-marker, federation, boarding-risk, combat-risk, stuff-reward, gamble]
---

# Encrypted federation signal — `FEDERATION_PLANET_SIGNAL`

## Summary
A quest-pool event that is a straight one-in-five gamble: send an away party and you get
one of five results, two of which plant quest markers, two of which pay out immediately,
and one of which is a Rebel trap with boarders. The only alternative is to walk away with
nothing. There are no blue options and no way to improve the odds.

## Trigger & Where It Appears
- Sectors: [[sector-abandoned-sector]], [[sector-civilian-sector]],
  [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-federation-space]], [[sector-rebel-controlled-sector]],
  [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]],
  [[sector-rock-homeworlds]], [[sector-zoltan-controlled-sector]],
  [[sector-zoltan-homeworlds]]
- Pooled in the quest lists — `QUESTS` and its Engi, Lanius, Rebel, Rock and Zoltan
  variants, plus the Advanced Edition `OVERRIDE_QUESTS` replacement. Present in **both
  editions** ([[source-newevents]], [[source-dlceventsoverwrite]],
  [[source-dlcevents-anaerobic]]).
- `unique="true"` — at most once per run.
- No ship at the beacon; Long-Range Scanners show nothing
  ([[source-fandom-encrypted-federation-signal]]).

## Text
> A Federation encrypted signal is being broadcast from a nearby planet.

(`event_FEDERATION_PLANET_SIGNAL_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Send an away party to investigate. | — | Loads `FEDERATION_PLANET_SIGNAL_LIST` — five outcomes, below. | see below |
| 2 | It could be a trap. Let's move on. | — | Nothing at all — the choice has an empty `<event/>`, so there is not even outcome prose. | 100% |

### `FEDERATION_PLANET_SIGNAL_LIST`

Five distinct members, none duplicated. **Assuming uniform selection across list entries,
each is 1/5.** The game files state no percentage; this is derived from list membership
only ([[source-events-xml]]).

| Odds | Outcome |
|---|---|
| 1/5 | *"You find a secret Federation outpost. They are regrettably out of supplies but are eager to tell you of another secret base. They give you the coordinates."* → `<quest event="HIDDEN_FEDERATION_BASE_LIST"/>` — a quest marker, no immediate reward. |
| 1/5 | *"You find a hidden Federation outpost. They message you, 'Quick, we just got word from a sister outpost that they've been discovered by the Rebels and are under attack!…'"* → `autoReward level="MED"` type **`stuff`**, plus `<quest event="FEDERATION_BASE_ASSIST"/>`. |
| 1/5 | *"You find a secret Federation outpost... but it appears the Rebels have found it before you; the place is empty and faint bloodstains can be seen in the living quarters."* → **nothing.** |
| 1/5 | *"You find a small cache of supplies that were surely left for any loyal Federation ships in trouble."* → `autoReward level="HIGH"` type `standard`. **The best flat payout in the event.** |
| 1/5 | *"As you approach the signal you receive a message on a Rebel channel, 'I knew we'd catch some Federation fish with this signal. Prepare to be boarded, scum!'"* → `<ship load="REBEL" hostile="true"/>` **plus** `<boarders min="2" max="3" class="human"/>`. |

`autoReward level="MED"` of type `stuff` is resources-with-some-scrap rather than
scrap-with-resources. [[source-fandom-encrypted-federation-signal]] is the only source that
puts numbers on that tier: **fuel 2–4, missiles 2–4, drone parts 1**. The game files give
only the level name ([[source-events-xml]]).

The `REBEL` ship: `<surrender chance="0.5" min="2" max="3">`,
`<escape chance="0.5" min="3" max="4">`, `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT` rewards
([[source-events-ships]]). Per [[concept-surrender-offers]], `chance="0.5"` reads as a
**50% surrender chance** — `chance` is the probability the ship keeps fighting.

### The two quest destinations

Both are separate beacons reached by marker, not part of this event's screen. Summarised
here because nothing else documents them yet:

**`HIDDEN_FEDERATION_BASE_LIST`** — five members ([[source-events-xml]]):
a high-tier `drone` reward; a crew member with low `standard`; medium `standard` plus
`<damage amount="-35"/>` (**35 hull repaired**); a screen gated on Sensors level 2 / 3 /
the [[item-adv-scanners]] augment paying medium `standard` or medium `weapon`; and a fifth
entry that simply loads `FEDERATION_BASE_ASSIST`. The Sensors-2 branch there is marked
`<!--DLC!-->`, so that option does not exist in vanilla.

**`FEDERATION_BASE_ASSIST`** — a fight at the sister outpost, and a clear edition split
([[source-events-xml]], [[source-dlceventsoverwrite]]):

| Edition | Pool |
|---|---|
| vanilla `FEDERATION_BASE_ASSIST` | 2 members: `AUTO_FEDERATION_BASE` or `AUTO_FEDERATION_BASE2`, no environment. |
| AE `OVERRIDE_FEDERATION_BASE_ASSIST` | 4 members: the same two, plus `REBEL_FEDERATION_PDS` and `AUTO_FEDERATION_BASE2`, both with `<environment type="PDS" target="enemy"/>` — the base's anti-ship battery fires **on the enemy**, in your favour. |

Assuming uniform selection, that is 1/2 each in vanilla and 1/4 each in AE, with a 1/2
chance in AE of friendly PDS support.

## Blue Options
None on this event. The Sensors / [[item-adv-scanners]] gates live one beacon downstream,
inside `HIDDEN_FEDERATION_BASE_LIST`.

## Rewards & Risks
- Best immediate result: high `standard` scrap with resources (1/5).
- Medium `stuff` — fuel 2–4, missiles 2–4, 1 drone part per
  [[source-fandom-encrypted-federation-signal]] — plus a quest marker (1/5).
- 1/5 of nothing at all, and 1/5 of a Rebel fight **with 2–3 human boarders already
  aboard**. That is the real cost: boarders land before you can react, and the fight is a
  normal Rebel ship with default rewards.
- Choice 2 is a guaranteed zero.

## Strategy Notes
- 4/5 of the outcomes are neutral-or-better and the bad one is a survivable fight with
  default rewards, so investigating is usually right. *Opinion*, from the outcome table;
  no source rates it.
- The exception is a crew already stretched thin or a ship with no way to handle boarders —
  2–3 humans in your systems is a real threat to a two-crew start.
- The `HIDDEN_FEDERATION_BASE_LIST` marker is worth following: its worst member is still a
  reward, and one member repairs 35 hull.

## Related
- [[chain-hidden-federation-base]] — the quest this plants, and its five-outcome destination
  table. Filed as a chain rather than an event page: `HIDDEN_FEDERATION_BASE_LIST` is an
  `eventList`, not an `<event name>`, and four separate beacons feed it.
- [[entity-rebels]] — the ambush ship
- [[entity-federation]] — whose outposts these are
- [[item-adv-scanners]] — gates a downstream option
- [[concept-quest-beacon-placement]], [[concept-surrender-offers]]

## Open Questions
- [ ] The actual distribution across `FEDERATION_PLANET_SIGNAL_LIST` — the 1/5 figures
      assume uniform selection across list entries.
- [ ] Whether the two quest markers can both be live at once (they are mutually exclusive
      outcomes of one roll, so presumably not within this event).
- [ ] The absolute values behind `MED`/`HIGH` `standard`; only the `stuff` tier has
      numbers, and those come from Fandom alone.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml — the `QUESTS_LANIUS` pool)
- [[source-fandom-encrypted-federation-signal]] (per raw/wiki/encrypted-federation-signal.md)
