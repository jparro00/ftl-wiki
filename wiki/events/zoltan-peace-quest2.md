---
id: event-zoltan-peace-quest2
type: event
event_name: ZOLTAN_PEACE_QUEST2
sectors: [[[sector-zoltan-homeworlds]]]
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-zoltan-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [ship-unlock, quest-marker, orphan-quest, dialogue-puzzle, zoltan-cruiser]
---

# Zoltan peace quest — the brethren's coordinates — `ZOLTAN_PEACE_QUEST2`

## Summary
Step 2 and the payoff of [[chain-zoltan-cruiser-unlock]]. What looks like a Rebel ambush
is a Zoltan test: exactly one dialogue path through the conversation unlocks the
**Zoltan Cruiser**. Every other line — including attacking, and three of the four
conversational replies — collapses into an ordinary Rebel fight and loses the unlock.

## Trigger & Where It Appears
- **Not present in any sector event list.** `ZOLTAN_PEACE_QUEST2` is never loaded by
  `HOSTILE_ZOLTAN`, `NEUTRAL_ZOLTAN`, `QUESTS_ZOLTAN` or any other list, and is not
  allocated in `sector_data.xml` ([[source-events-zoltan]], [[source-sector-data-xml]]).
- It is reached **only** as a quest marker planted by
  [[event-unarmed-zoltan-transport]], via `<quest event="ZOLTAN_PEACE_QUEST2"/>` on that
  event's "Hear them out" branch ([[source-events-zoltan]]).
- Sector: [[sector-zoltan-homeworlds]], since that is the only place its parent occurs.
- On Long-Ranged Scanners the marker reports a **ship present**
  ([[source-fandom-unarmed-zoltan-transport]]).
- Not marked `unique="true"` in the file — uniqueness is enforced by the parent instead.

## Text
> You arrive at the location specified by the peace-loving Zoltan, but the only thing
> nearby is a Rebel ship, closing in fast! "We've found you! You're not getting away
> this time!"

(`event_ZOLTAN_PEACE_QUEST2_text`, per [[source-text-events-xml]])

The Rebel ship loads as `<ship load="REBEL" hostile="false"/>` — it is **not** hostile
until you make it so, which is the mechanical tell that this is a scripted test rather
than an ambush ([[source-events-zoltan]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack. | — | *"You power your weapons and prepare to fight."* → `<ship hostile="true"/>`, fight a Rebel ship ([[entity-rebels]]), default rewards. **Unlock lost.** | 100% |
| 2 | Attempt to hail them. | — | *"I can't imagine there's anything you could say that will save you…"* → opens the three-reply menu below. | 100% |

### Choice 2 — the reply menu

| # | Reply | Outcome |
|---|-------|---------|
| 2a | "Perhaps there could be a reconciliation of our ideals without war?" | *"Our ideals are too different to be so easily reconciled. You think this could end any way but war?"* → opens the final two-way split below. **The only surviving path.** |
| 2b | "Surrender. Your ultimate destruction is inevitable. We've left scores of Rebels destroyed in our wake." | *"They shut off communications and immediately engage."* → Rebel fight, default rewards. **Unlock lost.** |
| 2c | "Your Rebellion is causing millions of deaths. Your beliefs are dividing the galaxy. Unity is the only option!" | *"…The sacrifice of BILLIONS of alien or human lives are justified if it means we reach our full potential!" They charge.* → Rebel fight, default rewards. **Unlock lost.** |

### Choice 2a — the final split

| # | Reply | Outcome |
|---|-------|---------|
| 2a-i | The galaxy is huge, you can find a place for your ideals elsewhere without causing this destruction. | *"No! We will not be consigned to the backwaters of space…" They charge.* → Rebel fight, default rewards. **Unlock lost.** |
| 2a-ii | **True progress can only be achieved without bloodshed.** | *"Suddenly all indications of the Rebel ship fade away and a Zoltan fleet appears around your ship…"* → forced continue → loads `ZOLTAN_PEACE_QUEST_REWARD`. **Unlock won.** |

### `ZOLTAN_PEACE_QUEST_REWARD` — the two payouts

| Entry | Text | Effect |
|-------|------|--------|
| 1 | *"…This technology should aid your quest."* | `<unlockShip id="7"/>` + `autoReward level="LOW"` `scrap_only` + `<augment name="ENERGY_SHIELD"/>` → **Zoltan Cruiser unlocked**, [[item-zoltan-shield]] augment, low scrap. |
| 2 | *"…I will personally assist."* | `<unlockShip id="7"/>` + `autoReward level="HIGH"` `standard` + `<crewMember amount="1" class="energy" all_skills="2" id="name_Envoy"/>` → **Zoltan Cruiser unlocked**, a Zoltan crew member named **Envoy** with `all_skills="2"`, and `HIGH` scrap with resources. |

The reward list is tagged `<!--DLC2 DLC3-->` in the source
([[source-events-zoltan]], per raw/gamedata/events_zoltan.xml).

## Blue Options
None. Notably, this event has **no equipment or crew gates at all** — it is a pure
dialogue puzzle.

## Rewards & Risks
- **Best outcome (entry 2):** the ship unlock plus a free maxed-skill Zoltan crew member
  and `HIGH` scrap with resources — one of the largest single-beacon payouts in the game.
- **Other winning outcome (entry 1):** the ship unlock plus the [[item-zoltan-shield]]
  augment (a Super Shield) and `LOW` scrap.
- **Failure:** an ordinary Rebel fight with default rewards. The unlock is not
  recoverable this run.
- Both winning outcomes call `unlockShip id="7"`, so **the unlock itself is guaranteed
  once you reach 2a-ii** — only the bonus differs.

## Strategy Notes
- The correct path is: **Attempt to hail them → "Perhaps there could be a reconciliation
  of our ideals without war?" → "True progress can only be achieved without bloodshed."**
  Every other combination loses the unlock.
- *Opinion:* the two rewards are not equal. Entry 2 (Envoy plus `HIGH` standard) is worth
  substantially more mid-run than a Super Shield augment plus `LOW` scrap — but you have
  no control over which you get.

> ⚠️ **CONTRADICTION:** the split between the two reward entries.
> - Fandom states an explicit **50% / 50%** chance for each
>   ([[source-fandom-unarmed-zoltan-transport]]).
> - The game files state **no percentage**; `ZOLTAN_PEACE_QUEST_REWARD` is an
>   `eventList` with two entries and no weights ([[source-events-zoltan]]).
>
> The two are compatible if `eventList` selection is uniform, but the file does not say
> so. Recorded as Fandom's claim rather than as fact.

> ⚠️ **CONTRADICTION:** the Envoy crew member's skills.
> - Game files: `all_skills="2"` ([[source-events-zoltan]]).
> - Fandom: *"a Zoltan crewmember named Envoy **maxed in all skills**"*
>   ([[source-fandom-unarmed-zoltan-transport]]).
>
> These agree only if `2` is the skill cap. Trusting the raw value; recorded as `2`
> rather than restated as "maxed".

## Related
- [[chain-zoltan-cruiser-unlock]] — this is step 2 of 2, the payoff
- [[event-unarmed-zoltan-transport]] — step 1, the only way here
- [[item-zoltan-shield]] — one of the two rewards
- [[entity-rebels]] — what every failure path fights
- [[entity-zoltan]] — Envoy's species

## Open Questions
- [ ] Confirm the 50/50 reward split from the game's `eventList` selection logic.
- [ ] Is `all_skills="2"` the maximum skill level in AE?
- [ ] Does the Rebel ship at this beacon count toward Rebel fleet pursuit?
- [ ] Ship id `7` — confirm it maps to the Zoltan Cruiser in `blueprints.xml`.

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-unarmed-zoltan-transport]] (per raw/wiki/unarmed-zoltan-transport.md)
