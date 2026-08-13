---
id: event-crew-stuck
type: event
event_name: CREW_STUCK
sectors: []
beacon_type: unknown
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [orphan, engine-event, no-choice, text-only, teleporter, boarding, no-fandom-page]
---

# Crew stranded — teleporter destroyed — `CREW_STUCK`

## Summary
The line the game shows when your boarding party is on an enemy ship and your Teleporter is
destroyed beyond repair: rather than stranding them, the crew commandeers an enemy shuttle
and comes home. A single `<text>` tag — no choices, no reward, no mechanical payload. It is
one of the hard-coded one-liners `events.xml` keeps for engine-driven situations.

## Trigger & Where It Appears
**Not in any sector event list.** `CREW_STUCK` appears exactly once in the whole of
`raw/gamedata/` — its own definition in `events.xml`. Nothing loads it and no
`<eventList>` or `<sectorDescription>` names it ([[source-events-xml]],
[[source-sector-data-xml]]).

Unlike its neighbours, the trigger is **stated by the prose itself**: *"With your teleporter
damaged and no way to fix it…"*. So the condition — boarders away, Teleporter destroyed and
unrepairable — is sourced, even though the hook that fires it is not visible in the data.

It sits in the same contiguous block of engine-called one-liners as `STALEMATE_SURRENDER`,
[[event-boss-stalemate]], `FUEL_ESCAPE_SUN`, `FUEL_ESCAPE_STORM`, `FUEL_ESCAPE_ASTEROIDS`,
`AUGMENT_FULL` and `EQUIP_FULL` ([[source-events-xml]]) — none of which are reachable
through the event pools either.

- **No Fandom page.** Nothing in the 293 pages under `raw/wiki/` mentions this event or its
  prose.

## Text
> With your teleporter damaged and no way to fix it, you take one of the enemy ship's
> shuttles to return to your own ship.

(`event_CREW_STUCK_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none)* | — | The text is displayed and, per the prose, the boarding party returns to your ship. The event body is a single `<text>` tag — no `<choice>`, no `<crewMember>`, no `<status>`, no reward. | 100% |

Note what is **absent**: there is no `<crewMember>` tag returning the crew and no
`removeCrew` losing them. Whatever restores the boarders to your ship is handled by the
engine, not by this event.

## Blue Options
None.

## Rewards & Risks
None declared. Read together with the prose, this event is the game's **safety net** against
permanently losing a boarding party to a destroyed Teleporter — a mercy, not a penalty.

## Version Differences
Base-`events.xml`, no DLC-marked tags — identical in both editions
([[source-events-xml]]).

## Related
- [[event-boss-stalemate]] — the neighbouring engine one-liner in the same block
- [[event-fuel-escape-pulsar]], [[event-fuel-escape-pds]] — the AE additions to the same
  family of hard-coded lines
- [[item-teleporter]] — the system whose destruction triggers this

## Open Questions
- [ ] Does the returned crew take any damage, or arrive at whatever health they had? The
      event says nothing.
- [ ] Does it fire the moment the Teleporter is destroyed, or when the fight ends?
- [ ] What happens if the enemy ship is destroyed while your crew is aboard *and* the
      Teleporter is down — is this event the resolution, or a different one?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml` — confirming it is in no list)
