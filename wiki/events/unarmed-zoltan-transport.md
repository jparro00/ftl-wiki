---
id: event-unarmed-zoltan-transport
type: event
event_name: ZOLTAN_PEACE_QUEST
sectors: [[[sector-zoltan-homeworlds]]]
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-zoltan-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, ship-unlock, quest-marker, guaranteed, zoltan-cruiser]
---

# Unarmed Zoltan transport — `ZOLTAN_PEACE_QUEST`

## Summary
Step 1 of the [[chain-zoltan-cruiser-unlock]] and a **guaranteed beacon in the
[[sector-zoltan-homeworlds]]**. Hearing the peace envoy out costs nothing and plants a
quest marker leading to [[event-zoltan-peace-quest2]], where the Zoltan Cruiser unlock
actually happens. Attacking them forfeits the chain for a small scrap payout.

## Trigger & Where It Appears
- Sector: [[sector-zoltan-homeworlds]] **only** — `sector_data.xml` allocates
  `ZOLTAN_PEACE_QUEST` at `min=1 max=1` in `ZOLTAN_HOME` and nowhere else
  ([[source-sector-data-xml]]). It is **not** allocated in
  [[sector-zoltan-controlled-sector]].
- Because it is allocated directly by the sector rather than through an event list, it
  is guaranteed once you enter the Zoltan Homeworlds. `ZOLTAN_HOME` itself is
  `unique="true"` and `minSector="2"`.
- Beacon: quest-flavoured neutral encounter; no ship is hostile on arrival.
- `unique="true"`.

## Text
> An unarmed Zoltan transport vessel is slowly making its way toward the beacon here.
> They hail: "This is a Zoltan peace envoy. We carry no weapons or shielding and rely on
> the mercy of others to communicate our message."

(`event_ZOLTAN_PEACE_QUEST_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack them. | — | Loads `ZOLTAN_PEACE_QUEST_ATTACK` — two entries, see below. **Ends the chain.** | unknown |
| 2 | Hear them out. | — | *"They talk at length about peace and harmony, but either it's beyond your simple mind or it's all nonsense."* → forced continue → *"…Once you have, contact our brethren." They transmit coordinates…* → `<quest event="ZOLTAN_PEACE_QUEST2"/>`, **a quest marker is added to your map**. | 100% |
| 3 | Leave. | — | *"The galaxy is at war - there's no time for talk of peace. You leave their hails unanswered and charge the jump drive."* Nothing happens. | 100% |

### `ZOLTAN_PEACE_QUEST_ATTACK` — the two results of choice 1

| Entry | Text | Effect |
|-------|------|--------|
| 1 | *"You charge your weapons - not that this will take much."* | `<ship load="ZOLTAN_PEACE_QUEST_ATTACK1" hostile="true"/>` — an unarmed Zoltan ship. |
| 2 | *"Just as you're preparing to attack you detect a nearby jump signature. A Zoltan defense ship comes to their aid!"* | `<ship load="ZOLTAN_PEACE_QUEST_ATTACK2" hostile="true"/>` — an armed Zoltan defence ship. |

Per [[source-fandom-unarmed-zoltan-transport]], entry 1's unarmed ship offers a surrender
prompt (*"They are clearly not putting up a fight. Are you sure you want to destroy
them?"*) with the option to finish them off or let them go for nothing. Destroying gives
`low` scrap with resources; killing the crew gives a random amount. Entry 2 gives `low`
(destroyed) or random (crew killed) scrap with resources, and the peace ship escapes
either way. Those post-fight branches live in `events_ships.xml`, which is not ingested
here — Fandom is the only source for them.

## Blue Options
None. No `req` attribute on any choice.

## Rewards & Risks
- **Choice 2 is the payoff path and is completely free** — no cost, no combat, no risk.
- Choice 1 trades the entire [[chain-zoltan-cruiser-unlock]] (a ship unlock, plus either
  a [[item-zoltan-shield]] augment or a maxed-skill crew member) for `low`-to-random
  scrap with resources. *Opinion:* a clearly bad trade.

## Strategy Notes
- If you are in the Zoltan Homeworlds for the unlock, this beacon is guaranteed — you
  cannot miss it, only mishandle it. Take choice 2.
- The follow-up marker ([[event-zoltan-peace-quest2]]) shows a **ship** on Long-Ranged
  Scanners, so it will look like a hostile beacon on the map
  ([[source-fandom-unarmed-zoltan-transport]]).
- The Zoltan Cruiser can alternatively be unlocked by winning the game with the
  [[entity-federation-cruiser]] ([[source-fandom-unarmed-zoltan-transport]]).

## Related
- [[chain-zoltan-cruiser-unlock]] — this is step 1 of 2
- [[event-zoltan-peace-quest2]] — step 2, the quest marker and the actual unlock
- [[item-zoltan-shield]] — one of the two possible rewards
- [[sector-zoltan-homeworlds]] — the only sector this appears in

## Open Questions
- [ ] Weighting between the two `ZOLTAN_PEACE_QUEST_ATTACK` entries.
- [ ] Loadouts of `ZOLTAN_PEACE_QUEST_ATTACK1` / `ATTACK2` (needs `events_ships.xml`).
- [ ] Does the quest marker expire if you leave the sector before reaching it?

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-unarmed-zoltan-transport]] (per raw/wiki/unarmed-zoltan-transport.md)
