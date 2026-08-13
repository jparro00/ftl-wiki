---
id: event-engi-unlock-2real
type: event
event_name: ENGI_UNLOCK_2REAL
sectors: []
beacon_type: quest
hostile: true
blue_options: []
chain: [[[chain-stealth-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [orphan, chain, quest-marker, forced-fight, ship-escape, ship-surrender, chain-failure-risk]
---

# Engi unlock — real Rebel base — `ENGI_UNLOCK_2REAL`

## Summary
Step 2 of [[chain-stealth-cruiser-unlock]], and the step most likely to lose you the ship
unlock. A Rebel scout that immediately runs for it: let it escape and the chain is dead,
**and blowing it up also kills the chain** — only a surrender or a crew kill passes the
quest marker along.

## Trigger & Where It Appears
- **Not in any sector event list.** It is reached only via the quest marker placed by
  [[event-engi-fleet-discussion]]'s Engi-crew branch
  (`<quest event="ENGI_UNLOCK_2REAL"/>`) ([[source-events-xml]], per
  `raw/gamedata/events_engi.xml`).
- Beacon: **quest** — a marked beacon on your sector map.
- Shares its intro text word-for-word with the decoy [[event-engi-unlock-2fake]]; the two are
  distinguishable only by punctuation in the combat text (see below).

## Text
> You arrive at one of the Rebel bases that the Engi told you about. It appears abandoned
> except for one scout ship. Perhaps you could extract information from them.

(`event_ENGI_UNLOCK_2REAL_text`, per [[source-text-events-xml]])

## Choices & Outcomes

The event has **no choices** — it loads
`<ship load="REBEL_ENGI_UNLOCK_2REAL" hostile="true"/>` immediately
([[source-events-xml]]).

| Ship outcome | Definition | Result | Chain? |
|---|---|---|---|
| **Escape** | `<escape timer="40" min="18" max="18"/>` — *"As soon as they see you they power up their engines to jump away. Stop them!"* | The ship starts running the moment you arrive, on a **40-second** timer. | — |
| **Got away** | *"With the ship gone, you search through the abandoned base for any signs of their destination but find none."* | Nothing. | ❌ **chain failed** |
| **Surrender** | `<surrender min="5" max="5" load="ENGI_UNLOCK_2REAL_SURRENDER"/>` | → [[event-engi-unlock-2real-surrender]] | ✅ |
| **Destroyed** | `<autoReward level="MED">standard</autoReward>` | `MED` scrap with resources. **No `<quest>` tag.** | ❌ **chain failed** |
| **Dead crew** | `<autoReward level="HIGH">standard</autoReward>` and `<quest event="ENGI_UNLOCK_3"/>` | `HIGH` scrap with resources **and** the final quest marker. | ✅ |

([[source-events-xml]], per `raw/gamedata/events_ships.xml`)

## Blue Options
None.

## Rewards & Risks
- **Best outcome:** kill the crew — `HIGH` scrap *and* the marker. Strictly better than the
  surrender route, which pays nothing.
- **Surrender route:** the marker, no scrap.
- **Destroying the hull:** `MED` scrap and the chain is over.
- **Letting it escape:** nothing, and the chain is over.
- The 40-second escape timer is the pressure: you must disable the enemy's Engines, or do
  enough damage to force the surrender, before it jumps.

> ⚠️ **CONTRADICTION:** surrender threshold.
> - Game files: `<surrender min="5" max="5" …/>` — a flat hull value of 5
>   ([[source-events-xml]], per `raw/gamedata/events_ships.xml`).
> - Fandom: "surrenders at **50%** hull", with a parenthetical that the "actual in-game value
>   may be 5 hull + additional hull adjusted by sector progression"
>   ([[source-fandom-engi-fleet-discussion]]).
>
> Trusting the game files for the literal value (`5`); Fandom's own caveat effectively
> concedes the percentage is an approximation. The "adjusted by sector progression" part is
> unverified either way.

> ⚠️ **OMISSION IN FANDOM:** the Fandom walkthrough lists only escape, surrender and dead
> crew for this beacon — it does not document the `destroyed` outcome
> ([[source-fandom-engi-fleet-discussion]]). The game files show `destroyed` grants `MED`
> scrap and **no** quest tag, so simply blowing the scout up silently fails the unlock
> ([[source-events-xml]]). This is a game-files-only finding and is the single most
> important thing on this page.

## Strategy Notes
- Do not overkill. Target Engines to stop the escape, then ease off — killing the hull ends
  the chain. Boarding or an anti-personnel weapon is the ideal answer here, since dead crew
  is the only outcome that pays *and* advances. *(Opinion, derived from the outcome table.)*
- If you arrive without a way to stop a runner, expect to lose the chain to the 40-second
  timer.

## Related
- [[chain-stealth-cruiser-unlock]] — this is step 2 of 4
- [[event-engi-fleet-discussion]] — step 1, which places this marker
- [[event-engi-unlock-2real-surrender]] — the surrender dialogue
- [[event-engi-unlock-2fake]] — the identical-looking decoy
- [[event-engi-unlock-3]] — step 3, unlocked by this beacon
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] What do `min="18" max="18"` on the `<escape>` tag control?
- [ ] Does the surrender threshold really scale with sector progression?
- [ ] Can the beacon be re-entered after the ship escapes?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`, `raw/gamedata/events_ships.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-engi-fleet-discussion]] (per `raw/wiki/engi-fleet-discussion.md`)
