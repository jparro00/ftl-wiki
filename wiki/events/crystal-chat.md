---
id: event-crystal-chat
type: event
event_name: CRYSTAL_CHATTY
sectors: [[[sector-hidden-crystal-worlds]]]
beacon_type: any
hostile: false
blue_options: [crystal crew]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, blue-option, hull-repair, fuel-reward, combat-risk]
---

# Crystal chat — `CRYSTAL_CHATTY`

## Summary
A curious Crystalline civilian wants to interview you. Humouring them is a three-way
gamble — supplies, hull repairs, or a Rebel ship dropping in mid-conversation. With a
Crystal crew member the gamble disappears and you take fuel and scrap for free.

## Trigger & Where It Appears
- Sector: [[sector-hidden-crystal-worlds]] only
- Pool: one of **10** entries in the `NEUTRAL_CRYSTAL` event list, which the sector
  allocates exactly **12** times (`min=12 max=12`) ([[source-events-xml]],
  [[source-sector-data-xml]])
- `unique="true"` — at most once per run
- Beacon: shows **no ship** on Long-Range Scanners ([[source-fandom-crystal-chat]])

## Text
> A small civilian vessel messages you, "Wow! You're that alien that opened up the portal,
> aren't you! Are you busy? Can I ask you a question?"

(`event_CRYSTAL_CHATTY_text`, per [[source-text-events-xml]])

The "you opened the portal" line is a direct callback to
[[event-ancient-device]] — the wormhole you came through to reach this sector.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Yes. | — | *"What do you eat? What is your culture like? How long do your people live?"* → a second choice, below. | — |
| 2 | No. | — | *"I see... I guess you're busy."* Nothing happens. | 100% |
| 3 | **(Crystal Crew)** Have your crew speak to them. | `req="crystal"` | *"Wow, you're one of us!… have some of our extra supplies!"* → `autoReward level="RANDOM"` **fuel** — a random amount of fuel and scrap. | 100% |

### After "Yes."

| # | Choice | Outcome(s) |
|---|--------|-----------|
| 1 | Try to answer his questions. | Loads `CRYSTAL_CHATTY_LIST` — three entries, below. |
| 2 | "I don't have time for this." | *"Maybe the next alien I meet will be nicer..."* Nothing happens. |

### Sub-event: `CRYSTAL_CHATTY_LIST`
Three entries ([[source-events-xml]], [[source-fandom-crystal-chat]]):

| Entry | Result |
|---|---|
| 1 | A Rebel ship spots you mid-chat → `ship load="REBEL" hostile="true"` — a **fight** with default rewards. |
| 2 | *"…we have some supplies we can offer you"* → `autoReward level="RANDOM"` **stuff** (resources with some scrap). |
| 3 | *"Perhaps we can fix up a bit of your hull…"* → `damage amount="-6"` = **6 hull repairs**. |

Two of three entries are good, one is a fight; the file does not weight them further.

## Blue Options
- **Crystal crew member** (`req="crystal"`) — converts a 1-in-3 fight risk into a
  guaranteed fuel-and-scrap reward. This is one of two `req="crystal"` gates in the sector,
  the other being [[event-crystalline-cache]].

## Rewards & Risks
- **Rewards:** random fuel and scrap (blue option); or random resources with scrap; or
  6 hull repairs.
- **Risk:** the `CRYSTAL_CHATTY_LIST` Rebel fight, which is not signposted — the beacon
  reads as having no ship on Long-Range Scanners, and the ship arrives only after you
  choose to keep talking.

## Strategy Notes
- Without Crystal crew, taking "Yes → answer his questions" is a 2-in-3 shot at a small
  reward against a 1-in-3 forced Rebel fight. Whether that is worth it depends entirely on
  your hull: the repair outcome is the largest single prize in the branch.
  *(Opinion, built on the list weighting from [[source-events-xml]].)*
- "No." at the top level is a clean zero-risk exit; there is no penalty for declining.

## Related
- [[sector-hidden-crystal-worlds]]
- [[event-ancient-device]] — the portal the civilian is referring to
- [[event-crystalline-cache]] — the other `req="crystal"` blue option here
- [[event-crystal-scrap-collector]] / [[event-store-crystal]] — how to get Crystal crew
- [[concept-rebel-fleet-advance]], [[entity-crystal-men]]
- [[concept-blue-options]]

## Open Questions
- [ ] Whether the `REBEL` ship in entry 1 also advances the fleet (no `modifyPursuit` in
      the file, so apparently not).
- [ ] Exact values behind `autoReward RANDOM fuel` and `RANDOM stuff`.

## Sources
- [[source-events-xml]] (per raw/gamedata/events_crystal.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-crystal-chat]] (per raw/wiki/crystal-chat.md)
