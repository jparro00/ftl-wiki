---
id: event-mantis-capture-commando
type: event
event_name: MANTIS_CAPTURE_COMMANDO
sectors: []
beacon_type: unknown
hostile: false
blue_options: [mantis crew, [[item-mind-control]]]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: [orphan, unused-content, blue-option, mind-control, crew-reward-chance, mantis, prisoner]
---

# Mantis capture commando — `MANTIS_CAPTURE_COMMANDO`

## Summary
A moral-choice prisoner event: you salvage an Engi wreck and find the lone survivor of
the Mantis boarding party that killed its crew. Release him, kill him, or interrogate him
with a Mantis crew member or [[item-mind-control]]. **It is not reachable in normal play**
— no event list in the extracted game files loads it.

## Trigger & Where It Appears
- **Orphan.** `MANTIS_CAPTURE_COMMANDO` appears in no `<eventList>` anywhere in the
  extracted game data. A grep across every `.xml` in `raw/gamedata/` finds it only in its
  own definition in `events_mantis.xml` and in `text_events.xml`
  ([[source-events-xml]], [[source-text-events-xml]]).
- The file's own summary header lists it under `Items:` and tags it **`NEW!!`**, alongside
  `MANTIS_GAMBLE` — the only two events in `events_mantis.xml` so marked, and the only two
  that are unlisted. The pair reads as authored-but-never-wired content
  ([[source-events-xml]]).
- No Fandom page exists for it, which is consistent with it never firing in play.
- Sectors, beacon type, and long-range-scanner appearance: **unknown**, because nothing
  allocates it.
- It is `unique="true"` and stages `<ship load="ENGI_SHIP" hostile="false"/>` — a passive
  Engi wreck, no fight.

## Text
> You come across an Engi wreck with one life-sign aboard; it turns out to be the sole
> survivor of the Mantis boarding party that wiped out the ship's crew. He's in no state
> to fight and he's brought aboard.

(`event_MANTIS_CAPTURE_COMMANDO_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Release him. | — | One of two `MANTIS_CAPTURE_COMMANDO_RELEASE` entries — see below. | unknown (2 entries) |
| 2 | Kill him. | — | One of two `MANTIS_CAPTURE_COMMANDO_KILL` entries — see below. | unknown (2 entries) |
| 3 | **(Mantis crewmember)** Interrogate him. | `req="mantis"` | One of two `MANTIS_CAPTURE_COMMANDO_TALK` entries — see below. | unknown (2 entries) |
| 4 | **(Mind Control)** Interrogate him. | `req="mind"` | Fixed outcome → a further "continue" step → `autoReward level="LOW"` `weapon`. | 100% |

No weights are given for any of the three lists, so all splits are **unknown**
([[source-events-xml]]).

### Choice 1 — `MANTIS_CAPTURE_COMMANDO_RELEASE`
- *(good)* > You help get the Engi ship up and running but take some of their supplies. He
  takes off without another word.
  → `autoReward level="MED"` `stuff`
- *(bad)* > He takes your mercy as a sign of weakness and rigs up a small timed explosive
  before making off in the Engi vessel.
  → `<damage amount="2"/>` **plus** `<damage amount="1" system="random" effect="fire"/>`
  — 2 hull, and 1 damage to a random system with a fire. The second damage element is
  tagged `<!--DLC-->` in the file, i.e. it is an **Advanced Edition addition**; in
  vanilla this outcome was 2 hull damage with no fire.

### Choice 2 — `MANTIS_CAPTURE_COMMANDO_KILL`
- *(clean)* > The Mantis commando shows no fear as the airlock's inner doors are sealed
  and space prepares to take him. You press the switch and then he's gone, whisked out
  into the great black.
  → `autoReward level="MED"` `stuff`
- *(fight)* > You strip the Engi ship before preparing to deal with the Mantis. However,
  the commando immediately realizes your intentions and attacks!
  → `autoReward level="MED"` `stuff` **and** `<boarders min="1" max="1" class="mantis"/>`

### Choice 3 — `MANTIS_CAPTURE_COMMANDO_TALK` (Mantis crew)
- > It's not clear what occurs between the two Mantis behind the locked door, but when
  they emerge the commando is prepared to provide telemetry on the local sector. He then
  leaves on the Engi ship. Your map has been updated.
  → `<reveal_map/>` — the whole sector map is revealed
- > After a short time alone with the commando, you are told he wishes to join the crew.
  Although you are surprised at the commando's willingness to swap allegiances, you trust
  your crewmember's judgment about him.
  → `<crewMember amount="1" class="mantis"/>` **and** `autoReward level="MED"` `stuff`

### Choice 4 — Mind Control
> Your mind control device allows you to quickly get his story without resistance. It
> appears the boarding party was attempting to steal an weapon that the Engi ship was
> transporting. However their team was wiped out by drones.

Then a single "continue":
> You find the weapon in a hidden storage hold and decide to patch the ship up enough to
> let the mantis leave.
→ `autoReward level="LOW"` `weapon`

## Blue Options
- **Mantis crew member** (`req="mantis"`) — the strongest option in the event. Both of its
  two outcomes are pure upside: a full sector map reveal, or a free Mantis crew member
  plus MED `stuff`. Neither has a downside branch.
- **[[item-mind-control]]** (`req="mind"`, no level requirement) — tagged `<!--DLC-->`, so
  this choice is **Advanced Edition only**. It is deterministic: a guaranteed LOW-level
  weapon with no risk, though a lower ceiling than the Mantis-crew option.

## Rewards & Risks
- Best outcomes: a free Mantis crew member (choice 3), a full map reveal (choice 3), or a
  guaranteed weapon (choice 4).
- Worst outcomes: 2 hull + a system fire (choice 1), or a Mantis boarder (choice 2 —
  though that branch still pays MED `stuff`).
- Both un-gated choices (1 and 2) carry a downside branch; both gated choices (3 and 4)
  carry none.

## Strategy Notes
Moot in practice — the event does not fire. Recorded for completeness, and because it is
useful evidence about how the AE `<!--DLC-->` markers work: the `req="mind"` choice and
the fire component of the release-failure both carry that tag, showing AE additions being
grafted onto a vanilla-era event skeleton.

*(Opinion, hypothetical.)* Were it live: with a Mantis crew member aboard, choice 3 has no
bad branch and would be an easy take.

## Related
- [[event-mantis-gamble]] — the other unwired `NEW!!` event in the same file
- [[event-escape-pod]] — the reachable Mantis-prisoner event, same theme, real risk
- [[event-boarders-mantis]]
- [[item-mind-control]]
- [[entity-mantis]], [[entity-engi]]

## Open Questions
- [ ] Was this event ever reachable in a shipped build, or is it cut content that was
      never wired up? Nothing in the extracted files answers this.
- [ ] Weights of the three two-entry outcome lists.
- [ ] What `autoReward` category `stuff` resolves to versus `standard`.
- [ ] Whether a mod or a later patch adds it to an event list.

## Sources
- [[source-events-xml]] (per raw/gamedata/events_mantis.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
