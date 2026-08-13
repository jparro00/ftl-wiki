---
id: event-empty-beacon-engi
type: event
event_name: NOTHING_ENGI
sectors: [[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]]
beacon_type: empty
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [filler, no-choice, varies-text, flavour]
---

# Empty beacon (Engi) — `NOTHING_ENGI`

## Summary
The Engi empty beacon: ten flavour texts, no choices, no effects. Its only mechanical role
is to occupy beacons so that not every jump is an encounter — one to two per Engi sector.

## Trigger & Where It Appears
- Sectors: [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]
- Beacon: **empty** — the event body is a single `<text load="NOTHING_ENGI"/>` and nothing
  else ([[source-events-xml]], per `raw/gamedata/events_engi.xml`)
- Allocated directly by sector, not through a list: `NOTHING_ENGI min=1 max=2` in both Engi
  sectors ([[source-sector-data-xml]])
- Not unique

## Text
The prose **varies**: `textList NOTHING_ENGI` holds ten entries
(`text_NOTHING_ENGI_1` … `_10`) ([[source-events-xml]]). All ten, per
[[source-fandom-empty-beacon-engi]]:

> The complex arrangements of ship hulls and FTL drive capacitors floating abandoned in
> space suggest the Engi were here not too long ago; but no longer.

> You arrive at a green planet with great plains and rolling waterfalls. It would be of
> little interest to the Engi nearby.

> You have arrived near an Engi construction yard. Most Engi maintain their bi-pedal
> appearance out of habit but here you see a number of Engi hives working together to
> create massive organic machines adept at building ships. Truly a sight to behold.

> Even though each "individual" Engi is made up of trillions of nano-machines, their
> culture still revolves around traditional social interactions. A nearby station seems to
> be constructed for entertainment of passing Engi travellers.

> You see a number of Engi space stations and fleets nearby. Despite looking like piles of
> junk loosely tied together they are actually a model of efficiency. They just lack a
> certain aesthetic emphasis in their constructions.

> This system appears quite peaceful. You're not sure how long it'll last between the
> combined threats of the Rebels and Mantis.

> There are a number of merchant ships passing through the area despite the threat of
> Mantis invasion. No doubt interested in buying the efficient technology of the Engi.

> You see a small Rebel carrier in the distance. You lay low and try to blend in with the
> other traffic. However it's surprising to see a Rebel military ship alone deep in Engi
> space.

> The Engi seem to have avoided this particular node, along with every other life-form.
> You keep your eyes peeled for reasons why, but spin up the FTL without event.

> A cluster of Engi satellites in orbit of a nearby planet are the only clue the mechanical
> species was ever here. You have other places to be.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none)* | — | Nothing happens. | 100% |

## Blue Options
None.

## Rewards & Risks
None of either. The event has no `autoReward`, no ship, and no crew or hull effects
([[source-events-xml]]).

## Strategy Notes
- Nothing to decide. Note that the Rebel-carrier variant is flavour only — no fight
  follows, despite the text ([[source-fandom-empty-beacon-engi]]).

## Related
- [[event-start-beacon-engi]] — the other pure-flavour Engi event
- [[event-free-scrap-with-resources-engi]] — the no-choice event that *does* pay out
- [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]

## Open Questions
- [ ] Are the ten text variants weighted equally?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-empty-beacon-engi]] (per `raw/wiki/empty-beacon-engi.md`)
