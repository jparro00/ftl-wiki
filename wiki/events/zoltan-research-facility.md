---
id: event-zoltan-research-facility
type: event
event_name: ZOLTAN_CREW_STUDY
sectors: [[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: any
hostile: false
blue_options: [medbay 3, [[item-damaged-stasis-pod]]]
chain: [[[chain-crystal-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [crystal-route, ship-unlock, blue-option, boarding-risk, crew-reward-opportunity, drone-schematic, quest-marker]
---

# Zoltan research facility — `ZOLTAN_CREW_STUDY`

## Summary
Step 2 of [[chain-crystal-cruiser-unlock]]. On its own it is a small trade-your-scans-for-
scrap event with a 1-in-3 pirate ambush; with the **Damaged Stasis Pod** aboard it is where
Ruwen the Crystal crew member is thawed out, which is the only route to
[[sector-hidden-crystal-worlds]]. Guaranteed once in each Zoltan sector.

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]] and [[sector-zoltan-homeworlds]] —
  **guaranteed**, `<event name="ZOLTAN_CREW_STUDY" min="1" max="1"/>` in both sector
  descriptions ([[source-sector-data-xml]]); plus
  [[sector-engi-controlled-sector]] and [[sector-engi-homeworlds]] via the `NEUTRAL_ENGI`
  list ([[source-events-engi]]).
- Not `unique` — it can fire more than once per run. Fandom observes it at one beacon per
  Zoltan sector and **one or two** per Engi sector
  ([[source-fandom-zoltan-research-facility]]).
- Beacon: no `<distressBeacon/>`, no `<store/>` — an ordinary beacon. It becomes a marked
  quest beacon in the Rock Homeworlds only *afterwards*, via
  [[event-ancient-device]].

## Text
> You arrive at a Zoltan research facility. They say they are researching genetic
> distortion due to stasis sleep and prolonged FTL travel. They ask if your crew has the
> time to undergo a few scans.

(`event_ZOLTAN_CREW_STUDY_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Participate in their study. | — | Loads `ZOLTAN_CREW_STUDY_LIST` (3 entries). Two entries are **identical** — same text id, same `autoReward level="LOW"` `scrap_only`. The third is a pirate ambush. | **2/3** peaceful scrap, **1/3** ambush — assumes uniform selection across list entries ([[concept-event-list-weighting]]) |
| 2 | Decline. | — | "Alright. Fly safe." Nothing happens. | 100% |
| 3 | **(Advanced Medbay)** Give them your medical records. | `req="medbay" lvl="3"` | `<drone name="RANDOM"/>` **and** `autoReward level="LOW"` `stuff` — a random drone schematic plus a small resource payout. No risk. | 100% |
| 4 | **(Damaged Stasis Pod)** Ask if they can fix this. | `req="STASIS_POD"` | `<remove name="STASIS_POD"/>`, then a three-deep continue chain ending in `<crewMember amount="1" class="crystal" id="name_Ruwen"/>` — **the Crystal crew member Ruwen**. | 100% |

### `ZOLTAN_CREW_STUDY_LIST`

Members 1 and 2 both point at `event_ZOLTAN_CREW_STUDY_LIST_1_text` and both grant
`autoReward level="LOW"` `scrap_only`; there is **no** `event_ZOLTAN_CREW_STUDY_LIST_2_text`
in `text_events.xml` at all ([[source-events-xml]], [[source-text-events-xml]]). Whether
that duplication is deliberate weighting or a copy-paste slip in the data, its effect is a
2-in-3 chance of the peaceful outcome. Fandom marks the same entry with its
`DuplicateEvent|2` template, so it reads the file the same way
([[source-fandom-zoltan-research-facility]]).

> Your crew calmly lines up for the Zoltans to take their readings. After a short time, the
> process is done. They contact you, "Thank you for your participation in our study. Please
> accept these small cakes made from stiff dough as well as some scrap."

The third member:

> As soon as you dock, pirates burst on board and a hostile ship appears on the radar. You
> hear the Zoltans yell in the distance, "We're being held hostage!"

→ `<ship load="PIRATE_ZOLTAN_CREW_STUDY" hostile="true"/>` **and**
`<boarders min="2" max="2" class="random"/>` — you fight the ship *and* two boarders at
once.

### The enemy — `PIRATE_ZOLTAN_CREW_STUDY`

`auto_blueprint="SHIPS_PIRATE"`, per [[source-events-ships]]. It has **no `<surrender>` and
no `<escape>` block** — it will not give up and will not run
(Fandom states the same, [[source-fandom-zoltan-research-facility]]).

| Win condition | Reward |
|---------------|--------|
| `destroyed` | `autoReward level="MED"` `standard`, then a continue → `autoReward level="LOW"` `stuff` **and** `<drone name="RANDOM"/>` |
| `deadCrew` | `autoReward level="HIGH"` `standard`, then the same continue → LOW `stuff` + random drone |

> "Thank you for rescuing us! They held us hostage to ambush unsuspecting passersby.
> Please, take this."

Boarding the pirates to death is worth a full reward tier more than blowing them up.

### Choice 4 — the Stasis Pod branch, in full
> "Interesting. I've never seen a cryogenic system like this. It appears to still be
> functioning..." They hook it up to their system and run a number of tests on it.

> "Amazing! It has the ability to reconstruct the body if it was damaged during transit.
> Watch." They reactivate the pod and you watch as the hunks of crystal inside reform to
> build a humanoid structure. The pod slides open and the re-formed alien steps out.

> It speaks slowly, "Greetings. I appear to be in your debt. My people isolated themselves
> a long time ago, but perhaps it's time to re-establish a connection. There's a hidden
> wormhole near the Rock home-worlds. Perhaps you can take me there so I can properly repay
> you?"

The augment is consumed (`<remove name="STASIS_POD"/>` fires *before* the text). Fandom adds
that a quest marker then appears in the [[sector-rock-homeworlds]] **as long as Ruwen stays
alive** — a condition the game files do not state
([[source-fandom-zoltan-research-facility]]).

## Blue Options
- **Advanced Medbay** (`req="medbay" lvl="3"`) — a free random drone schematic plus LOW
  `stuff`, with none of choice 1's ambush risk. Strictly better than choice 1 whenever you
  have it.
- **Damaged Stasis Pod** (`req="STASIS_POD"`) — the chain step. Consumes the augment and
  yields Ruwen. Nothing else in the game files uses `STASIS_POD` as a requirement in this
  file.

Both are `hidden="true"`, as are choices 1 and 2 — every choice in this event is hidden
until its condition is met.

## Rewards & Risks
- **Best case:** choice 4 (Ruwen, and the Crystal route opens) — plus, on a separate visit,
  choice 3's drone schematic.
- **Choice 1:** 2/3 LOW `scrap_only`; 1/3 a two-boarder fight alongside a pirate ship that
  cannot be made to surrender or flee. Winning that pays MED/HIGH `standard` *and* a drone
  schematic *and* LOW `stuff`, so the ambush is the highest-value outcome in the event if
  you can take it.
- **Risk** is confined to choice 1: 2 random-species boarders plus a ship fight.

Fandom footnotes that the `stuff` component "will never give a bonus weapon, drone
schematic or augmentation, due to its interaction with a guaranteed weapon/drone schematic
reward" ([[source-fandom-zoltan-research-facility]]) — an engine detail the XML does not
express.

## Version differences
No `<!--DLC-->` markers appear anywhere in this event, its list, or its ship block
([[source-events-xml]], [[source-events-ships]]), and `dlcEventsOverwrite.xml` does not
redefine `NEUTRAL_ENGI` ([[source-dlceventsoverwrite]]). Treat as identical in both
editions. Note that [[chain-crystal-cruiser-unlock]] is currently filed `version: ae`; this
step is not the reason.

## Strategy Notes
- If you are carrying the Damaged Stasis Pod, this is the beacon you are looking for, and
  Zoltan sectors guarantee one. Routing through a Zoltan sector after picking up the pod is
  the whole game plan for the Crystal Cruiser. *Opinion, standard for the chain
  ([[source-fandom-zoltan-research-facility]]).*
- With Medbay 3, take choice 3 — free drone schematic, zero risk.
- Choice 1 is a good bet on a healthy ship (2/3 free scrap, and the 1/3 loss case is
  actually the biggest payout) and a bad one on a damaged ship with no boarding defence.
- An Engi sector can supply both step 1 and step 2 of the chain
  ([[source-fandom-zoltan-research-facility]]).

## Related
- [[chain-crystal-cruiser-unlock]] — this is step 2 of 4
- [[event-dense-asteroid-field-distress]] — step 1, where the Damaged Stasis Pod comes from
- [[event-ancient-device]] — step 3, which Ruwen unlocks
- [[event-crystal-unlock]] — step 4
- [[item-damaged-stasis-pod]], [[entity-crystal-men]], [[entity-zoltan]]
- [[concept-event-list-weighting]] — the assumption behind the 2/3 split

## Open Questions
- [ ] Is the duplicated `ZOLTAN_CREW_STUDY_LIST` entry intentional weighting, or a data
      bug that lost `event_ZOLTAN_CREW_STUDY_LIST_2_text`?
- [ ] Exact values behind `LOW scrap_only`, `LOW stuff`, `MED standard`, `HIGH standard`.
- [ ] Does the Rock Homeworlds quest marker really depend on Ruwen surviving? Only Fandom
      says so.
- [ ] Can choice 3 and choice 4 both be taken? They are separate choices on the same
      event, so only one per visit — but the event is not `unique`.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-events-engi]] (per `raw/gamedata/events_engi.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-dlceventsoverwrite]] (per `raw/gamedata/dlcEventsOverwrite.xml`)
- [[source-fandom-zoltan-research-facility]] (per `raw/wiki/zoltan-research-facility.md`)
</content>
