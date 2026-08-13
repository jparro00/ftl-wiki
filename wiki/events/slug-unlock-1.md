---
id: event-slug-unlock-1
type: event
event_name: SLUG_UNLOCK_1
sectors: [[[sector-slug-home-nebula]]]
beacon_type: quest
hostile: true
blue_options: [slug crew, sensors lvl 2]
chain: [[[chain-slug-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [quest, ship-unlock, blue-option, augment-reward, nebula, orphan, slug]
---

# Slug unlock — the construction platform — `SLUG_UNLOCK_1`

## Summary
The payoff beacon of the Slug Cruiser chain. A prototype cruiser is being towed away on a
mobile construction platform, guarded by a Slug Assault ship. Charging in gets you a hard
fight and a consolation prize. Sneaking gets you a second decision — and with **Slug crew**
or **Sensors 2**, the escort leaves and you fight a weak interceptor instead, which is the
only branch that actually unlocks the ship.

## Trigger & Where It Appears
- **Not in any sector event list** — an orphan, reached only as a quest marker. It is
  planted by `<quest event="SLUG_UNLOCK_1"/>` in the "we want information" branch of
  [[event-slug-unlock-surrender]] ([[source-events-slug]]).
- That surrender is available only in [[sector-slug-home-nebula]], where
  `NEBULA_SLUG_FIGHT_UNLOCK` is allocated `min=1 max=1`
  ([[source-sector-data-xml]]) — so this beacon exists at most once per run and only in
  that sector.
- Beacon: **quest marker**, and it declares `<environment type="nebula"/>` — Fandom's note
  says the same: *"this event occurs at a regular quest marker beacon, but when you arrive
  there will be a nebula environment"* ([[source-fandom-slug-home-nebula-surrender]]).
- No Fandom page declares this event's own id; the content is documented under the
  parent's page (`NEBULA_SLUG_FIGHT_UNLOCK`) as its "Quest Marker" section, and it matches
  the files.

## Text
> You arrive to discover an impressive cruiser being worked on by a few smaller ships and
> guarded by an assault ship. The mobile construction platform is slowly slipping into the
> clouds. You have not yet been noticed.

(`event_SLUG_UNLOCK_1_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Charge them before they escape. | — (`hidden="true"`) | *"As you approach, the assault ship swoops in on an intercept trajectory. Prepare for a fight!"* → `<ship load="JELLY_UNLOCK2" hostile="true"/>` — the **hard** fight. **No unlock.** | 100% |
| 2 | Try to tail them without being noticed. | — (`hidden="true"`) | Loads the `SLUG_UNLOCK_2` sub-event, below. | 100% |

### Sub-event: `SLUG_UNLOCK_2`
> You slip into the nebula undetected but at this rate you are likely to get lost and lose
> track of them.

(`event_SLUG_UNLOCK_2_text`, per [[source-text-events-xml]])

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 2a | Fly slowly toward their last known position. | — (`hidden="true"`) | *"You are advancing slowly when suddenly the assault ship bursts through the clouds. They must have been able to detect you with their telepathy!"* → `<ship load="JELLY_UNLOCK2" hostile="true"/>` — the hard fight. **No unlock.** | 100% |
| 2b | Wait and hope the escort leaves. | — (`hidden="true"`) | *"You wait for a time before attempting to advance toward the platform. However, after some frantic searching you can't tell if they left or you simply miscalculated your trajectory... You give up the search and prepare to leave."* → nothing at all. **Chain lost.** | 100% |
| 2c | **(Slug Crew)** Have your crewmember monitor their life signatures. | `req="slug"` | *"...your Slug tells you the ship with a larger crew has jumped away. He guides the helm toward the platform..."* → continue → *"The only ship left near the cruiser is an interceptor. This should be easy!"* → `<ship load="JELLY_UNLOCK3" hostile="true"/>` — **the unlock fight.** | 100% |
| 2d | **(Improved Sensors)** Try to maintain a lock on their ships from a distance. | `req="sensors" lvl="2"` | *"...After a time, the assault ship and most of the escort jumps away from the platform. You take the opportunity and move in to attack."* → continue → same interceptor text → `<ship load="JELLY_UNLOCK3" hostile="true"/>` — **the unlock fight.** | 100% |

([[source-events-slug]]) Per the brief's sub-event rule, `SLUG_UNLOCK_2` is documented here
rather than on its own page.

### The two ships

**`JELLY_UNLOCK2`** — `auto_blueprint="JELLY_TRUFFLE"`, the **Slug Assault** class
([[source-text-blueprints]]). No `<surrender>`, no `<escape>` ([[source-events-ships]]):

> *"With the assault ship taken care of, you turn your attention to the construction
> platform. However, you find that it has long since disappeared into the clouds. You scrap
> what you can and prepare to move on."*
> → `<autoReward level="HIGH">standard</autoReward>` on both destroyed and dead crew.

A large consolation payout — **but no ship unlock and no augment.**

**`JELLY_UNLOCK3`** — `auto_blueprint="JELLY_BUTTON"`, the **Slug Interceptor** class
([[source-text-blueprints]]). It is the weak ship, but it runs a timer
([[source-events-ships]]):

| Branch | Declaration | Result |
|---|---|---|
| Escape | `<escape timer="35" min="22" max="22">` | *"The interceptor powers up its FTL drive in preparation to escape. At the same time, the cruiser's FTL drive does the same. They must be linked! Don't let them get away!"* → the fight continues under a countdown |
| Got away | — | *"The interceptor jumps away with the cruiser linked to its FTL signatures. You were so close..."* → **nothing. Chain lost.** |
| Destroyed / dead crew | — | *"With the escort destroyed you take a look at your impressive prize... you discover a unique augment that duplicates the Slug's ability to heal breaches!"* → `<unlockShip id="5"/>` (**Slug Cruiser**), `<autoReward level="HIGH">standard</autoReward>`, `<augment name="SLUG_GEL"/>` (**Slug Repair Gel**, [[source-text-blueprints]]) |

The `timer="35"` and `min="22" max="22"` are unusual: Fandom reads them as *"This ship
starts to escape with 35 seconds countdown timer"*
([[source-fandom-slug-home-nebula-surrender]]). The escape is not a chance roll — it is
scheduled, so the interceptor **will** try to leave and you are racing it.

Fandom flags a bug on the reward: *"if the 'scrap with resources' component gives an
augmentation, it will overwrite the guaranteed augmentation."*
([[source-fandom-slug-home-nebula-surrender]]) The XML shows `autoReward` and `augment`
applied in that order, which is consistent with the claim, but the overwrite itself is
Fandom's observation.

## Blue Options
- **Slug crew member** (`req="slug"`) — any Slug aboard. Sends the escort away and
  downgrades the fight from a Slug Assault to a Slug Interceptor.
- **Sensors level 2** (`req="sensors" lvl="2"`) — identical effect, no crew requirement.
  The label reads "(Improved Sensors)", matching the level-2 gate.

**These are not conveniences — they are the entire chain.** Without one of them there is no
path from this beacon to the ship unlock: choices 1 and 2a give the hard fight with no
unlock, and 2b gives nothing.

### Cut content
`SLUG_UNLOCK_1` contains a large **commented-out** block with a developer note —
*"Changed this part to be easier"* — that would have added two more routes into
`SLUG_UNLOCK_2`: `req="cloaking" lvl="1"` (*"(Cloaking) Cloak and slip into the clouds."*)
and `req="pilot" lvl="2"` (*"(Advanced Piloting) Quickly maneuver into the clouds and stay
out of their detection range."*), with choice 2 instead leading straight to the assault
ship ([[source-events-slug]]). Per [[concept-event-list-weighting]], commented-out entries
are excluded — recorded here only as cut content. The chain summary comment at the top of
the Slug unlock block still describes the old design: *"If you have cloak or piloting +
slug or sensors the scary people jump away."*

## Rewards & Risks
- **Unlock path (2c / 2d):** Slug Cruiser unlock + `HIGH` `standard` + Slug Repair Gel —
  the largest single payout in the sector, gated behind a 35-second race.
- **Hard path (1 / 2a):** `HIGH` `standard` against a Slug Assault, no unlock, no augment.
- **Wait path (2b):** nothing.
- **Risk:** the Slug Assault is a real fight in a nebula (sensors blinded). The interceptor
  is weak but will escape if you cannot kill it inside the timer.

## Strategy Notes
- *Opinion:* do not take choice 1. Charging is strictly worse than tailing — 2a reaches the
  same fight and the same reward, and tailing first preserves the chance that you have a
  blue option you forgot about.
- If you have neither blue option, the chain is already lost; take 2a for the `HIGH`
  payout rather than 2b for nothing.
- Against the interceptor, burst damage beats sustained damage: the 35-second escape timer
  means a slow grind loses the unlock. Hacking or Ion on their Engines is the cleanest
  insurance.
- A Slug crew member is cheap insurance for this chain generally — it also gates
  [[event-slug-comm-tapping]] and several other Slug-sector options.

## Related
- [[event-slug-unlock-surrender]] — the previous step; plants this quest marker
- [[event-slug-home-nebula-surrender]] — the fight that starts the chain
- [[chain-slug-cruiser-unlock]] — the chain this completes
- [[item-slug-repair-gel]] — the augment awarded here
- [[entity-slugs]] — Slug Assault (`JELLY_TRUFFLE`) and Slug Interceptor
  (`JELLY_BUTTON`) classes

## Open Questions
- [ ] What exactly do `timer="35"` and `min="22" max="22"` mean together on an `<escape>`
      block — 35 seconds from what trigger, and what does 22 gate?
- [ ] Confirm the augment-overwrite bug against a run.
- [ ] Does a Slug crew member need to be alive and un-mind-controlled at the moment of
      choosing?
- [ ] Whether the cut Cloaking / Advanced Piloting routes were live in any shipped build.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-slug-home-nebula-surrender]] (per raw/wiki/slug-home-nebula-surrender.md)
