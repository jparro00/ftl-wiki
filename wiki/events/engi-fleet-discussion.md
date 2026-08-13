---
id: event-engi-fleet-discussion
type: event
event_name: ENGI_UNLOCK_1
sectors: [[[sector-engi-homeworlds]]]
beacon_type: any
hostile: false
blue_options: [engi crew]
chain: [[[chain-stealth-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, ship-unlock, chain, quest-marker, blue-option, guaranteed]
---

# Engi fleet discussion — `ENGI_UNLOCK_1`

## Summary
The first step of [[chain-stealth-cruiser-unlock]] and a **guaranteed** beacon in the
[[sector-engi-homeworlds]]. Without an Engi crewmember it is a dead end — two choices, both
of which do nothing. With one, it opens the entire Stealth Cruiser quest line and drops two
quest markers on your map at once: one real, one decoy.

## Trigger & Where It Appears
- Sector: [[sector-engi-homeworlds]] only
- **Guaranteed:** `sector_data.xml` allocates `ENGI_UNLOCK_1` at `min=1 max=1` in
  `ENGI_HOME` ([[source-sector-data-xml]]). Engi Homeworlds is itself `unique="true"` with
  `minSector="2"`, so it appears at most once per run and not immediately.
- **Not** drawn from an event list: the `NEUTRAL_ENGI` entry for it is commented out
  (`<!--<event load="ENGI_UNLOCK_1"/> -->`), and the sector allocates it directly instead
  ([[source-events-xml]], per `raw/gamedata/events_engi.xml`).
- `unique="true"`

## Text
> You arrive near a small fleet of civilian Engi ships. A simple decryption and translation
> of their comm frequency tells you that they are having a frantic discussion about
> something obviously troubling them.

(`event_ENGI_UNLOCK_1_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Message them and ask if you can help. | — | *"Declined offer with apologetic gratitude. Topic of discussion private matter, no concern of Federation."* → nothing. | 100% |
| 2 | Ignore it and move on. | — | *"You can't help but wonder what they were discussing as you prepare to jump."* → nothing. | 100% |
| 3 | **(Engi Crew)** Have your Engi crewmember contact them. | `req="engi"` | *"Our goals have analogous elements. However, not all available for disclosure, discretion necessary."* → opens the chain, below. | 100% |

### Choice 3 — the chain opens

| Step | Prose | Effect |
|------|-------|--------|
| Offer your help. | *"Secret technologies stolen by Mantis. Implicit connection to Rebels. Implicit. Tracked Mantis to hidden Rebel base, uploading coordinates."* | `<quest event="ENGI_UNLOCK_2REAL"/>` — the **real** marker |
| *(continue)* | *"However, tracked second ship to different base. Would calculate probability but data insufficient. Cannot risk obvious Rebel-Engi conflict. Also, need time to acquire military ships. Assist in finding technology?"* | `<quest event="ENGI_UNLOCK_2FAKE"/>` — the **decoy** marker |
| Agree. | — | Empty `<event/>`; the chain is now live. |

Both markers are placed unconditionally and in that order, and Fandom confirms they can be
visited in either order ([[source-events-xml]],
[[source-fandom-engi-fleet-discussion]]).

## Blue Options
- **Engi crewmember** (`req="engi"`) — any Engi crew satisfies it. It is the **only** way to
  start [[chain-stealth-cruiser-unlock]] from this beacon; choices 1 and 2 both resolve to
  empty events ([[source-events-xml]]).

## Rewards & Risks
- No scrap, no items, no risk at this step — the entire payoff is deferred to
  [[event-engi-unlock-4]] (Stealth Cruiser unlock, Titanium System Casing, `HIGH` scrap,
  20 hull repairs).
- Risk is downstream: the two markers cost jumps, and the decoy costs a fight for nothing
  but scrap.

## Telling the real marker from the decoy

Both beacons show the identical intro text, so the tell is in the *combat* text. Verified
against `raw/gamedata/text_events.xml` ([[source-text-events-xml]]) and matching
[[source-fandom-engi-fleet-discussion]]:

| | Escape text | "Got away" text |
|---|---|---|
| **Real** ([[event-engi-unlock-2real]]) | "As soon as they see you **they** power up…" — *no comma* | "With the ship gone**,** you search…" — *comma* |
| **Decoy** ([[event-engi-unlock-2fake]]) | "As soon as they see you**,** they power up…" — *comma* | "With the ship gone you search…" — *no comma* |

The tell inverts between the two texts, so note which one you are reading.

## Strategy Notes
- If you are running any ship with an Engi aboard and Engi Homeworlds is on your route, this
  chain is guaranteed to be available — the beacon is `min=1 max=1`. *(Opinion: that makes
  Engi Homeworlds a strong sector pick for an Engi-crewed ship chasing the unlock.)*
- Fandom notes the Stealth Cruiser can alternatively be unlocked by winning the game with
  the Rock Cruiser ([[source-fandom-engi-fleet-discussion]]).
- The decoy is not a failure state — you can visit both markers. The only true failure is
  letting the *real* Rebel scout escape, or destroying it outright; see
  [[event-engi-unlock-2real]].

## Related
- [[chain-stealth-cruiser-unlock]] — this is step 1 of 4
- [[event-engi-unlock-2real]] — step 2, the real marker
- [[event-engi-unlock-2fake]] — the decoy marker
- [[event-engi-unlock-3]] — step 3, the escort fight
- [[event-engi-unlock-4]] — step 4, the payoff
- [[entity-engi]], [[item-titanium-system-casing]]

## Open Questions
- [ ] Do the two quest markers land in the same sector, or can they be spread across sectors?
- [ ] What happens if you leave the sector without visiting either marker?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-engi-fleet-discussion]] (per `raw/wiki/engi-fleet-discussion.md`)
