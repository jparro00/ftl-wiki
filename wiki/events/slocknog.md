---
id: event-slocknog
type: event
event_name: SLUG_DISTRESS_RESCUE
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: nebula
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, nebula, crew-reward, crew-purchase, named-crew, bug]
---

# Slocknog — `SLUG_DISTRESS_RESCUE`

## Summary
A marooned Slug named Slocknog offers to sell you his services for 55 scrap. Refuse and he
immediately offers to come along for free. There is no downside and no fight — declining
the paid offer strictly dominates accepting it, and the only way to lose the crew member is
to say no twice.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]] — via the
  `DISTRESS_BEACON_SLUG` event list (`min 3 / max 4` per sector)
  ([[source-events-slug]], [[source-sector-data-xml]])
- Beacon: nebula (`<environment type="nebula"/>`), `unique="true"`
- **It is in the distress list but has no `<distressBeacon/>` tag** — so it will not appear
  as a distress signal on the map. Fandom flags this as a bug: *"This event is meant to
  occur at a distress beacon but won't because the `<distressBeacon/>` tag is missing in
  its definition."* Confirmed against the XML ([[source-events-slug]],
  [[source-fandom-slocknog]]).

## Text
> You detect life signs on a nearby moon - a lone Slug marooned on its surface. "Ah, a
> sssentient ssspecies, after all this time. I am Slocknog, a wandering hero ssseeking
> adventure. You may hire me for a ssmall sssum."

(`event_SLUG_DISTRESS_RESCUE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Hire Slocknog. | — | `<item type="scrap" min="-55" max="-55"/>` and `<crewMember amount="1" class="slug" id="name_Slocknog"/>` — **pay 55 scrap**, gain Slocknog. | 100% |
| 2 | Ignore Slocknog. | — | Rolls `SLUG_DISTRESS_RESCUE_LIST` — a single entry, below. | 100% |

Choice 1 is **not** hidden; choice 2 is `hidden="true"`.

### `SLUG_DISTRESS_RESCUE_LIST` (choice 2)

One entry only, so this outcome is deterministic ([[source-events-slug]]):

> You power up the FTL, at which point the Slug sends an urgent plea. "Please, I ssee you
> are a sssly captain. You have an advantage. Very well. I will join your crew - but please
> remove me from this rock!"

| # | Choice | Outcome |
|---|--------|---------|
| 1 | Rescue him. | `<crewMember amount="1" class="slug" id="name_Slocknog"/>` — Slocknog joins **for free** |
| 2 | Leave him. | Nothing happens |

## Rewards & Risks
- A named Slug crew member, for 55 scrap or for nothing.
- No fight, no resource risk, no way for the event to go badly except by refusing twice.
- Fandom adds two behavioural notes ([[source-fandom-slocknog]]):
  - The crew skills are shown before you commit, on both the paid and the free offer.
  - **The skill set can differ if you recruit Slocknog for free rather than paying** —
    i.e. the free version may be a different roll, not the same crew member re-priced.
    No game-file evidence for this either way; the `crewMember` tags are identical.

## Strategy Notes
- Take choice 2, then *Rescue him.* The scrap price is entirely optional.
- The one reason to pay: if Fandom's note about differing skills is right and the paid roll
  is better, 55 scrap buys a re-roll. The skills are visible before you choose either way,
  so you can see what you are getting. *(Opinion; the game files do not distinguish the two
  `crewMember` tags.)*
- Because the `<distressBeacon/>` tag is missing, this event turns up at an ordinary beacon
  with no warning — you cannot route towards it.

## Related
- [[event-slug-moons-question]] — the other Slug-recruiting distress event
- [[event-mantis-ship-attacking-slug-ship]], [[event-slug-ship-boarding-rock-ship]],
  [[event-slug-oxygen-malfunction]] — the rest of `DISTRESS_BEACON_SLUG`
- [[entity-slugs]], [[item-slug-crew]]

## Open Questions
- [ ] Whether the free Slocknog really rolls different skills from the paid one.
- [ ] Whether the missing `<distressBeacon/>` is fixed in any later build.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-slocknog]] (per raw/wiki/slocknog.md)
