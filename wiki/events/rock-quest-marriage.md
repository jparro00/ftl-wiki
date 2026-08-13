---
id: event-rock-quest-marriage
type: event
event_name: ROCK_QUEST_MARRIAGE
sectors: [[[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-rock-bride]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [rock, quest, quest-marker, crew-reward, augment-reward, named-crew, combat]
---

# Numa V — `ROCK_QUEST_MARRIAGE`

## Summary
The second beacon of the Rock bride quest, and a clean moral fork with a clean mechanical
one behind it. Hand the passenger over for a **random augment plus low scrap** and no risk,
or refuse and get **Ariadne**, a named Rockman crew member, plus a Rock ship fight. It is
the only event in the Rock files that awards a crew member with a fixed name.

## Trigger & Where It Appears
- **Not in any sector event list.** It is a **quest-marker beacon**, placed by
  `<quest event="ROCK_QUEST_MARRIAGE"/>` on the "Accept the passenger" branch of
  [[event-rock-bride]] ([[source-events-rock]]). Refusing at step 1 places no marker.
- Sectors are inherited from the parent: [[sector-rock-controlled-sector]] and
  [[sector-rock-homeworlds]], where `QUESTS_ROCK` is allocated `min="0" max="1"`
  ([[source-sector-data-xml]]).
- Beacon: **no ship present** on Long-Range Scanners ([[source-fandom-rock-bride]]) — the
  fight only starts if you pick the refusal branch.
- **Version:** `both`. `events_rock.xml` is a base file and neither the event nor its
  `QUESTS_ROCK` entry carries a `<!--DLC-->` marker. (The parent page
  [[event-rock-bride]] currently says `ae`; flagged for reconciliation, not edited here.)

## Text
> A vast tunnel network near the surface of Numa V indicates an advanced Rock civilization.
> This must be where you were asked to deliver the passenger.

(`event_ROCK_QUEST_MARRIAGE_text`, per [[source-text-events-xml]])

A single hidden continue leads to the decision:

> Realizing arrival is imminent, the passenger - silent so far - pleads with you not to hand
> her over. She's interrupted by the Grand Basilisk's Chief Aid: "To the alien vessel holding
> the Basilisk's wife. Deliver her to us. You will be rewarded... well."

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Hand her over. | — | *"'May your children erode into dust!' she screams as she's bundled into the waiting shuttle. The Rock guards on board hurriedly drop off an exotic piece of technology…"* → `<augment name="RANDOM"/>` + `<autoReward level="LOW">scrap_only</autoReward>`. No fight. | 100% |
| 2 | Refuse to comply. | — | *"'I was led to believe your kind did not know mercy. I will join you. But quickly, we must jump away — they will not tolerate…' She's interrupted by weapons fire from the Basilisk's escort!"* → `<crewMember amount="1" class="rock" id="name_Ariadne"/>` **and** a fight with the `ROCK_QUEST_MARRIAGE` hull. | 100% |

### The `ROCK_QUEST_MARRIAGE` hull ([[source-events-rock]])
`auto_blueprint="SHIPS_ROCK"` — the standard Rock hull, but **declared inline in
`events_rock.xml` with no `<surrender>` and no `<escape>` block**. Unlike an ordinary
[[event-rock-fight]], this ship will not offer to surrender: it cannot reach
[[event-rock-ship-surrender]].

| Resolution | Outcome |
|---|---|
| **Destroyed** | *"His escort eliminated, the Grand Basilisk dispatches his entire fleet. There's just time to take your pick from the wreck before you jump out of their reach."* → `MED standard` |
| **Dead crew** | same text → `HIGH standard` |

## Blue Options
None. Neither choice carries a `req` — notably, **no Rock-crew blue option**, despite the
event turning on Rock custom.

## Rewards & Risks
- **Choice 1:** a random augment and `LOW scrap_only`, guaranteed, with zero risk. The
  augment is drawn from the general pool, so it can be anything from Titanium System Casing
  to a dud.
- **Choice 2:** Ariadne — a Rock crew member with **no `all_skills` attribute**, so she
  arrives untrained — plus `MED standard` (destroyed) or `HIGH standard` (dead crew) from the
  fight. Rock crew are fire-immune and high-HP, which is the real value here.
- **Risk:** choice 2 is an unavoidable fight against a Rock hull that will never surrender.
  Rock ships are armoured and missile-armed; if you are already damaged this is a genuine
  cost.

## Strategy Notes
- *Opinion:* take choice 2 if your crew is thin or you lack a fire-resistant boarder — a
  Rockman is worth more than a random augment and 20-ish scrap, and the fight pays as well.
- Take choice 1 if you are hurt, out of missiles, or already have a full crew: it is free.
- Do not expect a surrender offer on the choice-2 fight. Plan to kill it.

## Related
- [[event-rock-bride]] — step 1, which places this marker
- [[chain-rock-bride]] — the two-beacon chain
- [[event-rock-fight]] — the ordinary Rock hull, which *does* offer surrender
- [[event-rock-ship-surrender]] — unreachable from this fight
- [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[entity-rock-men]]

## Open Questions
- [ ] Exact scrap value of `LOW scrap_only` here.
- [ ] Whether Ariadne differs from a generic Rock crew member in any way besides her name.
- [ ] Whether the augment roll excludes augments you already carry.

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-rock-bride]] (per raw/wiki/rock-bride.md)
