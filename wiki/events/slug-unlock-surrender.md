---
id: event-slug-unlock-surrender
type: event
event_name: SLUG_UNLOCK_SURRENDER
sectors: [[[sector-slug-home-nebula]]]
beacon_type: nebula
hostile: true
blue_options: []
chain: [[[chain-slug-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [surrender, aftermath, ship-unlock, weapon-reward, quest-marker, orphan, slug]
---

# Slug unlock surrender — `SLUG_UNLOCK_SURRENDER`

## Summary
The hidden surrender that starts the Slug Cruiser unlock. It looks *exactly* like an
ordinary [[event-slug-surrender]] — same prompt, same wording — but accepting opens a
second layer: take the **Anti-Bio Beam** they are smuggling, or refuse it and demand
information instead, which plants a quest marker for [[event-slug-unlock-1]] and the ship
unlock. This is the branch point of the whole chain.

## Trigger & Where It Appears
- **Not in any sector event list** — an orphan reached only through `events_ships.xml`.
  The `JELLY_UNLOCK1` ship declares
  `<surrender chance="0" min="3" max="4" load="SLUG_UNLOCK_SURRENDER"/>`
  ([[source-events-ships]]).
- `chance="0"` means the ship **never keeps fighting** once hull enters the `min=3 max=4`
  band — i.e. a **100% surrender offer** ([[concept-surrender-offers]]). Fandom states
  "surrender offer: 100% chance" for this ship, agreeing exactly
  ([[source-fandom-slug-home-nebula-surrender]]).
- `JELLY_UNLOCK1` is loaded by exactly one event, `NEBULA_SLUG_FIGHT_UNLOCK`
  ([[event-slug-home-nebula-surrender]]), which `sector_data.xml` allocates at
  `min=1 max=1` in `SLUG_HOME` only ([[source-sector-data-xml]]). So this surrender is
  available **exactly once per [[sector-slug-home-nebula]]**, and nowhere else.
- The same ship also carries `<escape chance="0.5" min="3" max="4" load="PIRATE_ESCAPE"/>`
  — a 50% escape attempt in the *same* hull band. If the Slugs flee first, you must do
  more damage before the guaranteed surrender can fire
  ([[source-events-ships]]; Fandom makes the same point,
  [[source-fandom-slug-home-nebula-surrender]]).
- Beacon: nebula (inherited from the parent fight's `<environment type="nebula"/>`).
- The Fandom page that covers this content declares the **parent** event id
  (`NEBULA_SLUG_FIGHT_UNLOCK`) in its Trivia, not this one — it is cited here because its
  "When the Slug ship surrenders" section transcribes this event's choices and outcomes
  and they match the files.

## Text
> "You have besssted us! Will you accept what is in our storeesss in exchange for our
> livess?"

(`event_SLUG_UNLOCK_SURRENDER_text`, per [[source-text-events-xml]])

**Byte-identical to `event_SLUG_SURRENDER_text`.** The two are separate strings with the
same content, so there is no tell in the prompt. Fandom states the practical consequence
plainly: *"This event is impossible to distinguish from [Slug fight in nebula], as it has
the same intro and surrender text... the only way to find out is to accept the
surrender."* ([[source-fandom-slug-home-nebula-surrender]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Let them live. | — (`hidden="true"`) | *"Take thisss newly developed weapon we're transporting... They're not going to be happy we gave it up, that isss for ssure..."* → the two sub-choices below. | 100% |
| 2 | We will not accept surrender! | — (`hidden="true"`) | `<event/>` — nothing; the fight continues. **Forfeits the chain.** | 100% |

### After accepting

| # | Sub-choice | Outcome(s) |
|---|---|---|
| 1a | Accept the prototype weapon. | *"This odd beam weapon does no damage to ships but instead greatly hurts the crew! Diabolical!"* → `<weapon name="BEAM_BIO"/>` — the **Anti-Bio Beam** ([[source-text-blueprints]]) — and `<ship hostile="false"/>`, ending the fight. |
| 1b | We don't want the weapon, we want information. (`hidden="true"`) | *"You ask where they were delivering the weapon. 'By telling you we will probably die jussst as like as not... Oh well.' They give you the coordinates of the a prototype cruiser's mobile construction platform."* → `<quest event="SLUG_UNLOCK_1"/>` — **a quest marker is added to your map** — and `<ship hostile="false"/>`. |

([[source-events-slug]]) The typo *"the coordinates of the a prototype cruiser's"* is in
the game string, not a transcription error.

**These are mutually exclusive.** You get the weapon **or** the quest marker, never both.

## Blue Options
None. No `req` attribute appears at any depth of this event — the Slug-crew and Sensors
gates come later, in the `SLUG_UNLOCK_2` sub-event documented on
[[event-slug-unlock-1]].

## Rewards & Risks
- **1a — Anti-Bio Beam:** a guaranteed weapon, immediately. It does no hull damage and
  instead kills crew, so its value depends entirely on your build.
- **1b — quest marker:** costs a jump and advances the Rebel fleet, and the payoff fight is
  hard, but it is the route to the **Slug Cruiser unlock**, a `HIGH` `standard` payout and
  the **Slug Repair Gel** augment ([[event-slug-unlock-1]]).
- **2 — refuse:** you fight on for `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT` and lose both.

## Strategy Notes
- *Opinion:* if you do not already have the Slug Cruiser unlocked, take **1b**. The weapon
  is situational; the unlock is permanent and comes with an augment and a large payout.
- If you do have it unlocked, **1a** is the better take — Anti-Bio Beam is a strong
  anti-crew tool on a boarding build and needs no follow-up jump.
- Because the offer is indistinguishable from an ordinary Slug surrender, the practical
  rule in [[sector-slug-home-nebula]] is: **accept every Slug surrender** until you have
  seen this one. Accepting an ordinary one only costs you the kill.

## Related
- [[event-slug-home-nebula-surrender]] — the parent fight (`NEBULA_SLUG_FIGHT_UNLOCK`)
- [[event-slug-unlock-1]] — where the quest-marker branch leads
- [[event-slug-surrender]] — the ordinary Slug surrender this is disguised as
- [[item-anti-bio-beam]], [[item-slug-repair-gel]] — the two rewards of the two branches
- [[chain-slug-cruiser-unlock]] — the chain this starts
- [[concept-surrender-offers]] — why `chance="0"` is a 100% surrender
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Does the 50% escape attempt, if it succeeds, forfeit the chain entirely for that run?
- [ ] Is there any in-game tell (ship name, crew count, scanner readout) distinguishing
      `JELLY_UNLOCK1` from `JELLY` before the surrender fires?
- [ ] Can the quest marker be reached in a later sector, or only within
      [[sector-slug-home-nebula]]?

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-slug-home-nebula-surrender]] (per raw/wiki/slug-home-nebula-surrender.md)
