---
id: event-the-black-raven
type: event
event_name: DONOR_BLACK_RAVEN
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: hostile
hostile: true
blue_options: [slug crew]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [slug, donor-event, unique, named-ship, surrender-offer, weapon-reward, boarding-risk, reference]
---

# The Black Raven — `DONOR_BLACK_RAVEN`

## Summary
A donor event: Captain Nights, a Slug pirate in a Slug Assault cruiser, challenges you to a
duel in the best *Princess Bride* tradition. There is **no way to decline** — refusing just
starts the fight anyway. A Slug crewmember opens a psychic duel that can win the reward
outright. And the ship itself carries `<surrender chance="0">`, which per
[[concept-surrender-offers]] means it **always** offers surrender once damaged enough.
`unique="true"`.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]
- Event list: `HOSTILE_SLUG` ([[source-events-slug]]) — a **five-member** list allocated
  `min=1 max=2` in both `SLUG_SECTOR` and `SLUG_HOME` ([[source-sector-data-xml]]), so the
  draw rate is high for a donor event
- Beacon: `<ship load="DONOR_BLACK_RAVEN" hostile="false"/>` — the ship is present but
  **not hostile on arrival**; the fight only starts once you talk
- Long-range scanners show a ship ([[source-fandom-the-black-raven]])
- `unique="true"` — once per run

## Text
> As you jump in, you immediately see an impressive Slug pirate ship with "The Black Raven"
> painted on one side. They hail you, "Greetingsss. I am the dreaded pirate, Captain Nights.
> You mussst be full of fear, no? You have heard of me... no?"

Answering *"No."*:

> "Well I have heard of you and I must see if you are as dangerousss as they say. I
> challenge you!"

(`event_DONOR_BLACK_RAVEN_text`, `…_c1_text`, per [[source-text-events-xml]])

## Choices & Outcomes

The first screen's only choice is **"No."** There is no other reply.

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Accept his challenge. | — | `<ship hostile="true"/>` — straight into the fight, no extra text | 100% |
| 2 | Decline. | — | *"'I sssee... However you have no choice in the matter!' They move in to attack."* → `<ship hostile="true"/>` | 100% |
| 3 | **(Slugman Crew)** Engage in a duel of the mind. | `req="slug"` | Rolls `DONOR_BLACK_RAVEN_SLUG` (2 entries) — see below | 1/2 each |

Choices 1 and 2 are mechanically **identical** — a flavour difference only.

### Choice 3 → `DONOR_BLACK_RAVEN_SLUG`

| Entry | Outcome | Share |
|---|---|---|
| 1 | *"…your comrade grunts in pain and collapses onto the floor, stunned. Nights responds, 'Hah! It'll take more than that to defeat me!'"* → `<ship hostile="true"/>` + `<boarders min="1" max="2" class="slug"/>` — the fight **plus** 1–2 Slug boarders | 1/2 |
| 2 | *"…your comrade shakes off the daze and appears victorious."* → *"…Take thisss and let us leave in shame."* → `autoReward level="HIGH"` **`weapon`**, **no fight at all** | 1/2 |

Two entries → **1/2 each**, assuming uniform selection across list entries
([[source-events-xml]]).

### The ship — `DONOR_BLACK_RAVEN`
`<ship name="DONOR_BLACK_RAVEN" auto_blueprint="JELLY_TRUFFLE">` — defined **inside
`events.xml` itself**, not in `events_ships.xml` where enemy ships normally live
([[source-events-xml]]):

| Branch | Content |
|---|---|
| `<surrender chance="0" min="3" max="4">` | *"I see the rumorsss are true. I yield, we are no match for you. Take this and let us leave in ssshame."* — **Accept his surrender** → `<ship hostile="false"/>` + `autoReward level="HIGH"` `weapon`. **Ignore him and attack** → *"'Wait! There is no need to be....'"* → the fight continues |
| `<destroyed>` | *"'The Black Raven' breaks apart and you salvage the remains."* → `autoReward level="MED"` `standard` |
| `<deadCrew>` | *"The once-dreaded pirate Nights has been killed and you proceed to loot his ship."* → `autoReward level="HIGH"` `standard` |

There is **no `<escape>` branch** — Nights cannot run.

`chance="0"` reads as "0% chance of surrendering" on its face, and Fandom marks the offer as
guaranteed. Per [[concept-surrender-offers]], `chance` is the probability the ship **keeps
fighting**, so `chance="0"` means it *always* offers surrender once hull falls into the
`min`/`max` band. The two sources agree under that reading. `min="3" max="4"` are hull
points; Fandom renders them as *"30–40% hull"*, which the concept page treats as an
unconfirmed interpretation ([[source-fandom-the-black-raven]]).

> **Correction to [[concept-surrender-offers]]:** that page states *"Three ships carry
> `chance="0"`"* and names `CRYSTAL_CONVOY`, `JELLY_UNLOCK1` and `QUEST_SLUG_PIRATE_TRAP1`.
> `DONOR_BLACK_RAVEN` is a **fourth**, missed because its `<ship>` block is defined in
> `events.xml` rather than `events_ships.xml` ([[source-events-xml]]). It is a **fourth
> independent confirmation** of the `1 − chance` reading, not a counterexample: Fandom
> documents the surrender offer as guaranteed here too.

Fandom adds that the *Black Raven* is **always a Slug Assault class**, and that this is the
only event where a Slug Assault can be fought as early as sector 4 — normally they do not
appear before sector 5 ([[source-fandom-the-black-raven]]). The game files give only the
`JELLY_TRUFFLE` auto-blueprint.

## Blue Options
- **Slug crew** (`req="slug"`) — the psychic duel. A **1/2 chance to win the `HIGH` weapon
  without fighting at all**, against a 1/2 chance of the same fight plus 1–2 Slug boarders.
  It is the only choice in the event that changes anything.

## Rewards & Risks
- **`HIGH` `weapon`** is available three ways: winning the mind duel, accepting the ship's
  surrender, or… not really — the surrender is the reliable route.
- Killing the crew pays `HIGH` `standard`; blowing the ship up pays only `MED` `standard`.
  Boarding is therefore worth more than shooting here.
- **Risks:** a Slug Assault cruiser earlier than the sector would normally allow, plus 1–2
  Slug boarders on the losing half of the mind duel.
- Fandom notes the weapon and scrap amounts are **shown before** you accept or reject the
  surrender, so the decision is made with full information
  ([[source-fandom-the-black-raven]]).

## Version Differences
Base-`events.xml` event, and its ship block is in the same file, with **no DLC-marked tags**
in either — identical in both editions ([[source-events-xml]]).
`HOSTILE_SLUG` is not redefined in `dlcEventsOverwrite.xml`, so the pool is unchanged.

## Strategy Notes
- *(Opinion.)* With a Slug aboard, take the mind duel: half the time you skip a
  sector-inappropriate cruiser fight entirely and pocket a `HIGH` weapon.
- Without one, the choice is cosmetic — fight it and aim to **kill the crew** rather than
  destroy the hull, for the better payout, then take the surrender offer if it comes.
- *(Opinion.)* Accepting the surrender is usually right: a `HIGH` weapon now beats a `HIGH`
  `standard` payout that you still have to earn through a full crew kill.

## Related
- [[event-slug-fight]] — the ordinary Slug fight from the same `HOSTILE_SLUG` list
- [[event-slug-home-nebula-surrender]], [[event-slug-comm-tapping]] — the other two
  `chance="0"` ships in the game
- [[concept-surrender-offers]] — why `chance="0"` means a guaranteed offer
- [[entity-slugs]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]

## Open Questions
- [ ] Are `<eventList>` entries selected uniformly? The 1/2 assumes it.
- [ ] Are `min="3" max="4"` on the surrender block hull points or a percentage? See
      [[concept-surrender-offers]].
- [ ] What `JELLY_TRUFFLE` resolves to across sector depths — Fandom's "always a Slug
      Assault" is not visible in the event or ship definition.
- [ ] Numeric value of `HIGH weapon` here versus the identical reward from the mind duel.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-events-slug]] (per `raw/gamedata/events_slug.xml` — `HOSTILE_SLUG`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-the-black-raven]] (per `raw/wiki/the-black-raven.md`)
