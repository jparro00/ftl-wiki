---
id: event-engi-unlock-2fake
type: event
event_name: ENGI_UNLOCK_2FAKE
sectors: []
beacon_type: quest
hostile: true
blue_options: []
chain: [[[chain-stealth-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [orphan, chain, quest-marker, forced-fight, decoy, ship-escape, ship-surrender]
---

# Engi unlock — decoy Rebel base — `ENGI_UNLOCK_2FAKE`

## Summary
The decoy half of [[chain-stealth-cruiser-unlock]]. Identical intro text to
[[event-engi-unlock-2real]], identical setup, and no chain progress whatever — the ship here
knows nothing. It is not a trap that fails the chain, just a detour that pays `MED` scrap at
best. Both markers are placed at once by [[event-engi-fleet-discussion]] and can be visited
in either order.

## Trigger & Where It Appears
- **Not in any sector event list.** Reached only via the second quest marker placed by
  [[event-engi-fleet-discussion]] (`<quest event="ENGI_UNLOCK_2FAKE"/>`)
  ([[source-events-xml]], per `raw/gamedata/events_engi.xml`).
- Beacon: **quest**.

## Text
> You arrive at one of the Rebel bases that the Engi told you about. It appears abandoned
> except for one scout ship. Perhaps you could extract information from them.

(`event_ENGI_UNLOCK_2FAKE_text`, per [[source-text-events-xml]]) — word-for-word identical to
[[event-engi-unlock-2real]].

## Choices & Outcomes

No choices — the event loads `<ship load="REBEL_ENGI_UNLOCK_2FAKE" hostile="true"/>`
immediately.

| Ship outcome | Definition | Result |
|---|---|---|
| **Escape** | `<escape timer="40" min="18" max="18"/>` — *"As soon as they see you, they power up their engines to jump away. Stop them!"* | 40-second runaway timer. |
| **Got away** | *"With the ship gone you search through the abandoned base for any signs of their destination but find none."* | Nothing. |
| **Surrender** | `<surrender min="4" max="4" load="ENGI_UNLOCK_2FAKE_SURRENDER"/>` | → [[event-engi-unlock-2fake-surrender]] |
| **Destroyed** | `<autoReward level="MED">standard</autoReward>` | `MED` scrap with resources. |
| **Dead crew** | `<autoReward level="MED">standard</autoReward>` | `MED` scrap with resources. |

([[source-events-xml]], per `raw/gamedata/events_ships.xml`)

Note that unlike the real beacon, dead crew and destroyed pay the **same** `MED` tier here,
and no outcome carries a `<quest>` tag.

## Telling it apart from the real beacon
The intro text is identical. The tell is punctuation in the combat text, verified against
`raw/gamedata/text_events.xml` and matching [[source-fandom-engi-fleet-discussion]]:

- **Escape text** — the decoy **has** a comma ("As soon as they see you**,** they power
  up…"); the real one does not.
- **"Got away" text** — the decoy has **no** comma ("With the ship gone you search…"); the
  real one does.

The tell inverts between the two texts.

## Blue Options
None.

## Rewards & Risks
- `MED` scrap with resources for winning, by any means. Nothing else.
- No chain progress and, equally, **no chain penalty** — visiting the decoy does not
  jeopardise [[event-engi-unlock-2real]] ([[source-fandom-engi-fleet-discussion]]).
- Risk: an ordinary Rebel scout fight, plus the jumps spent getting there.

## Strategy Notes
- If you can read the tell before committing, skip this beacon and spend the jumps on the
  real one. *(Opinion.)*
- If you cannot tell them apart, visiting both is safe — the order does not matter and the
  decoy costs only time and hull. *(Opinion, supported by Fandom's note that either order
  works.)*
- Since no outcome here advances anything, there is no reason to spare the ship. Take
  whichever kill is cheapest.

## Related
- [[chain-stealth-cruiser-unlock]]
- [[event-engi-fleet-discussion]] — places this marker
- [[event-engi-unlock-2real]] — the real beacon this impersonates
- [[event-engi-unlock-2fake-surrender]] — the surrender dialogue
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] What do `min="18" max="18"` on the `<escape>` tag control?
- [ ] Does Long-Ranged Scanners distinguish the two markers in any way? Fandom shows the same
      "ship detected" reading for both.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`, `raw/gamedata/events_ships.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-engi-fleet-discussion]] (per `raw/wiki/engi-fleet-discussion.md`)
