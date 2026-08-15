---
id: event-battlefield-survivor
type: event
event_name: BATTLEFIELD_SURVIVOR
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: nebula
hostile: false
blue_options: ["medbay level 2", clonebay]
chain: [[[chain-secret-word-abadoth]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [crew-reward, quest-marker, blue-option, dlc, slug, shared-sub-event]
---

# Battlefield survivor — `BATTLEFIELD_SURVIVOR`

## Summary
The dying survivor pulled out of the [[event-nebula-wreckage]] debris. With no medical
systems you can only make their last moments comfortable — and get the word "ABADOTH" and a
quest marker for it. With an upgraded Medbay or any Clone Bay you save them instead and
gain a free crew member. It is the shared payoff node reached by two different routes
through the parent event.

## Trigger & Where It Appears
- **Not in any sector event list.** It is a shared sub-event, loaded twice from
  [[event-nebula-wreckage]] (`NEBULA_BATTLEFIELD`) ([[source-events-slug]]):
  1. **Slug blue route** — `NEBULA_BATTLEFIELD`'s `req="slug"` choice goes straight to a
     survivor, whose "help them" sub-choice loads this event. Guaranteed.
  2. **Search route** — the ordinary "investigate" choice rolls the five-entry
     `BATTLEFIELD_INVESTIGAGE` list; **one of the five entries** finds the survivor and
     offers this event. That is **1/5**, assuming uniform selection across list entries
     ([[concept-event-list-weighting]]).
- Because it inherits the parent, it appears in [[sector-slug-controlled-nebula]] and
  [[sector-slug-home-nebula]], on a `unique` nebula beacon. See the parent page for the
  standing contradiction about whether [[sector-uncharted-nebula]] is also in scope.
- **Version:** `ae`. The parent is marked `<!--DLC - Below-->` in its list, and this event
  sits in the DLC block of `events_slug.xml`.
- Fandom documents these outcomes inside its *Nebula wreckage* page
  ([[source-fandom-nebula-wreckage]]).

## Text
> Your bring the survivor aboard, but discover their wounds are severe. They won't live
> much longer.

(`event_BATTLEFIELD_SURVIVOR_text`, per [[source-text-events-xml]]. The typo — *"Your
bring"* — is in the game data.)

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Make them comfortable for their final moments. | — | *"On their death bed, they croak out a series of coordinates and beg you to go there — when you attempt to ask them why, the survivor simply says, 'ABADOTH' and perishes."* → `<quest event="SECRET_WORD_ABADOTH"/>`, a quest marker on the map. The survivor dies. | 100% |
| 2 | **(Advanced Medbay)** Get them into the medbay! | `req="medbay" lvl="2"`, `hidden="true"` | *"…you are able to heal the survivor's wounds and they recover quickly. Grateful to be saved, they offer to join your crew…"* → `<crewMember amount="1"/>`. **No quest marker.** | 100% |
| 3 | **(Clonebay)** Try to clone them before it's too late. | `req="clonebay"`, `hidden="true"` | *"You clone the individual and let the host pass away. The clone decides to join you — although it has little choice in the matter."* → `<crewMember amount="1"/>`. **No quest marker.** | 100% |

The crew member has no `class` attribute, so its species is whatever the engine rolls by
default — the data does not specify one ([[source-events-slug]]).

## Blue Options
- **Medbay level 2** (`req="medbay" lvl="2"`) — an *upgraded* Medbay, not just an installed
  one.
- **Clone Bay** (`req="clonebay"`, no `lvl`) — **any** Clone Bay satisfies it, including
  level 1. This is strictly cheaper than the Medbay gate for the same reward.
- Both are mutually exclusive with the quest marker: saving the survivor means never
  hearing the word.

## Rewards & Risks
- **Crew member** (choices 2/3) — a free body, worth roughly 45–60 scrap at a hiring
  station, and immediately useful.
- **Quest marker** (choice 1) — leads to [[event-secret-word-abadoth]], and through it to
  `SECRET_WORD_ABADOTH_CONCLUSION`, which is documented on that page.
- No risk: no branch damages you, and no branch starts a fight.

## Strategy Notes
- *Opinion:* the crew member is the safer pick — it is immediate and unconditional, while
  the ABADOTH marker costs a jump and its conclusion can end in a Zoltan fight.
- If you are already full on crew, take choice 1: the marker is then pure upside.
- Clone Bay ships get the crew member for free at level 1; there is no reason to pass.

## Related
- [[chain-secret-word-abadoth]] — the full quest line this belongs to
- [[event-nebula-wreckage]] — the parent, both routes into this event
- [[event-secret-word-abadoth]] — where choice 1's quest marker leads
- [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]] — where the parent appears
- [[concept-event-list-weighting]] — basis for the 1/5 figure on the search route

## Open Questions
- [ ] What species the awarded `<crewMember amount="1"/>` actually is.
- [ ] Whether the Slug blue route's survivor and the search route's survivor are meant to
      be the same person — the prose does not say.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-nebula-wreckage]] (per raw/wiki/nebula-wreckage.md)
