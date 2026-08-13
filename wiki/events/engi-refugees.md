---
id: event-engi-refugees
type: event
event_name: ENGI_REFUGEES
sectors: []
beacon_type: unknown
hostile: false
blue_options: [engi crew]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: [unreachable, orphan, engi, crew-reward, blue-option, scrap-cost, unique]
---

# Engi refugees — `ENGI_REFUGEES`

## Summary
A damaged Engi refugee freighter asks for help. Pay scrap and you get thanks; send an
**Engi** crew member with the scrap and you get an Engi crew member back — a rare event
that converts scrap directly into crew with no dice roll at all. It is **not reachable in
normal play**: no event list anywhere in the extracted game data loads it.

## Trigger & Where It Appears
- **Orphan / unreachable.** `ENGI_REFUGEES` appears in `raw/gamedata/` exactly once — its
  own definition in `nameEvents.xml`. A grep across every `.xml` finds no `<eventList>`
  entry, no `load=`, and no `sector_data.xml` allocation referencing it
  ([[source-nameevents]]).
- Not a stub: it has full authored prose, three choices, a gated option and a crew reward.
  This is shipped content that nothing calls, not placeholder text.
- No Fandom page exists for it, consistent with it never firing in play.
- Sectors, beacon type, and long-range-scanner appearance: **unknown**.
- `unique="true"`. No ship is staged, so the beacon would start non-hostile.
- **Version:** `nameEvents.xml` is a base-game file that Advanced Edition patched in place
  — other events in it carry inline `<!--DLC-->` markers on individual tags. This event
  carries none, so its definition is the same in both editions as far as the extracted
  files show. It is equally unreachable in both.

## Text
> You come across a freighter of Engi refugees fleeing the Rebels. Their ship is seriously
> damaged and they clearly need help.

The prose is written inline in `nameEvents.xml` rather than referenced through
`text_events.xml`, which is itself unusual — most shipped events externalise their strings
for localisation ([[source-nameevents]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | You just don't have the equipment or the time to help them. We wish them luck and let them go on their way. | — | Nothing happens. Empty `<event/>`. | 100% |
| 2 | You give them what scrap you can afford to aid them in their repair efforts. | — | *"They thank you repeatedly and wish you good luck on your mission."* → **−10 to −30 scrap**, nothing in return. | 100% |
| 3 | **(Engi)** Your crewmember wants to go aboard to see if he can provide any help personally. He requests some scrap to help. | `req="engi" lvl="1"` | *"He returns bearing good news. He was able to improve their engines and convinced one of their crew to join your cause."* → **−5 to −25 scrap** and **`crewMember amount="1" type="engi"`**. | 100% |

No branch loads an event list, so there is nothing to derive odds from — every outcome is
deterministic.

## Blue Options
- **Engi crew member** (`req="engi" lvl="1"`) — the whole point of the event. It is
  *cheaper* than the plain donation (5–25 scrap versus 10–30) **and** it returns an Engi
  crew member. There is no downside branch and no failure roll: taking it is strictly
  better than choice 2 in every respect.
- Note the choice text is not prefixed with a blue-option marker in the datafile itself
  beyond the literal `(Engi)` in the string; the gate is the `req` attribute
  ([[source-nameevents]]).

## Rewards & Risks
- **Choice 3:** an Engi crew member for 5–25 scrap. Engi are the best repair crew in the
  game, and buying one at a store costs considerably more than 25 scrap — this would have
  been one of the strongest crew-acquisition events in the game had it shipped live.
- **Choice 2:** 10–30 scrap for nothing but flavour text. Strictly dominated by choice 3
  when you qualify, and by choice 1 when you do not.
- **Risks: none.** No damage, no boarders, no ship, no hazard in any branch.

## Strategy Notes
- Nothing actionable — the event cannot occur. Recorded so the shipped content is visible
  rather than silently dropped, and so it is not mistaken for a playable beacon.
- Worth noting as a design fossil: an unconditional, riskless "scrap → crew" trade is far
  outside the normal power band for FTL events, which may be why it never made it into a
  list. That is inference from the outcome table, not something any source states.
- Do not confuse it with the reachable Engi crew events. This one has no fight, no
  distress beacon, and no chance of failure.

## Related
- [[event-lone-shuttle]] — the other complete-but-unlisted event in `nameEvents.xml`
- [[event-free-augment]] — the third, and the smallest
- [[entity-engi]]
- [[concept-blue-options]]

## Open Questions
- [ ] Whether the event was ever live in a shipped list, in any version.
- [ ] Whether the `lvl="1"` on `req="engi"` means "one Engi crew member" or an Engi with
      skill level 1 — the datafile does not say and no other source here resolves it.
- [ ] Why its prose is inline rather than in `text_events.xml`, unlike almost every live
      event.

## Sources
- [[source-nameevents]] (per raw/gamedata/nameEvents.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml — checked for allocation;
  none found)
