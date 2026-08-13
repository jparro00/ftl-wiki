---
id: event-rock-and-slug-standoff
type: event
event_name: ROCK_SLUG_ARGUMENT
sectors: [[[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [rock, slug, unique, reactor-upgrade, scrap-cost, hull-damage-risk, advanced-edition]
---

# Rock and Slug standoff — `ROCK_SLUG_ARGUMENT`

## Summary
A Slug crew upgraded a Rock ship's reactor and the Rock captain will not pay. Intervening
is the only route in the game to a **free reactor bar** outside a store — but the branch
that reaches it most often also risks a Rock ship fight or a reactor explosion in your
face. Reachable in Rock sectors directly, and in Slug nebulas through
[[event-slug-and-rock-standoff-in-nebula]].

## Trigger & Where It Appears
- `unique="true"` — once per run.
- Event list: `NEUTRAL_ROCK`, last entry, marked `<!--DLC - newEvents-->`
  ([[source-events-rock]], line 45) → [[sector-rock-controlled-sector]] and
  [[sector-rock-homeworlds]] ([[source-sector-data-xml]]).
- Also reached **indirectly**: [[event-slug-and-rock-standoff-in-nebula]]
  (`ROCK_SLUG_ARGUMENT_NEBULA`, in `NEBULA_NEUTRAL_SLUG`) loads this event wholesale via
  `<event load="ROCK_SLUG_ARGUMENT"/>` ([[source-newevents]], line 1508), which is how it
  appears in Slug space.
- Beacon: ordinary; no distress flag, no environment tag of its own (the nebula wrapper
  supplies one when it is reached that way).

## Text
> You find a Slug Cruiser and Rock ship at a standoff, both with weapons armed and ready to
> fight. You could intervene before this gets out of hand.

(`event_ROCK_SLUG_ARGUMENT_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Hail them to see what's wrong. | — | *"The Slug captain explains that they upgraded the Rock ship's reactor and now the 'thick boulder heads' are refusing to pay… The Rock Captain says the 'slime balls' did a poor job."* → three sub-choices, below. | — |
| 2 | Leave them be. | — | `<event/>` — nothing happens. | 100% |

### After hailing

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-------------|------|
| 1a | Offer to pay off the Rock debt. | — | −10 to −15 scrap. *"You pay off the debt. The Rock Captain still seems annoyed… but at least the situation will remain peaceful."* → hidden **continue** → `ROCK_SLUG_GRATEFUL`. | 100% |
| 1b | Demand the Rock ship pay the agreed upon price. *(hidden)* | — | Loads `ROCK_SLUG_COMMAND` — three entries, below. | — |
| 1c | You have better things to attend to, leave them. | — | `<event/>` — nothing happens. | 100% |

### `ROCK_SLUG_COMMAND`
Three distinct entries. **Assuming uniform selection across list entries**, each is 1/3:

| # | Text | Effect |
|---|------|--------|
| 1 | *"Apparently the Rock Captain was more annoyed than you thought, they shut off all communication and turn on you, the 'slime balls' defender."* | `<ship load="ROCK_SLUG_REACTOR_SHIP" hostile="true"/>` |
| 2 | *"With much grumbling, the Rock Captain agrees to pay the price."* | Hidden **continue** → `ROCK_SLUG_GRATEFUL` |
| 3 | *"A massive explosion emanates from the Rock Ship… Seems like that reactor upgrade was poorly done after all, and the Slugs took the opportunity to jump away."* | `damage amount="3"` (hull), plus `damage amount="1" system="random"` **twice** — the second occurrence carries an inline `<!--DLC-->` marker |

([[source-newevents]], [[source-text-events-xml]]) Derived from list contents, not a stated
percentage.

### `ROCK_SLUG_REACTOR_SHIP`
`auto_blueprint="SHIPS_ROCK"`. No `<surrender>`, no `<escape>` ([[source-newevents]]).
- `destroyed` — *"With the Rock Ship destroyed, you take the time to collect what little
  scrap remains."* → `autoReward level="LOW"` `standard`.
- `deadCrew` — *"With the Rock crew dead, you scrap the ship for supplies."* →
  `autoReward level="MED"` `standard`.
- Both then offer a hidden **"Contact the Slugs."** choice → `ROCK_SLUG_GRATEFUL`.

So every non-explosion path through the "demand payment" branch still reaches the Slug
reward.

### `ROCK_SLUG_GRATEFUL` — the Slug reward pool
Three distinct entries. **Assuming uniform selection across list entries**, each is 1/3:

| # | Text | Effect |
|---|------|--------|
| 1 | *"The Slugs offer their thanks for your help, and jump away. Their true appreciation is questionable, but at least you can get back to your mission."* | Nothing. |
| 2 | *"The Slug Captain offers a free reactor upgrade for your help. It never hurts to get a little power boost!"* | `<upgrade amount="1" system="reactor"/>` — **free reactor bar** |
| 3 | *"The Slug Captain, thankful for your help, offers a reactor upgrade for your ship... for a 'fair' price."* | Two choices: **Agree to the price** (`req="reactor" max_lvl="24" blue="false"`) → −10 to −15 scrap and `<upgrade amount="1" system="reactor"/>`; or **Decline the offer** → nothing |

The `max_lvl="24"` gate on the paid upgrade means it is hidden once your reactor is maxed —
that is the reactor cap, not a blue-option requirement (`blue="false"`).

> ⚠️ **CONTRADICTION:** the reactor-explosion damage.
> - Game files: `<damage amount="3"/>` plus two `<damage amount="1" system="random"/>`
>   entries ([[source-newevents]], lines 1566–1570).
> - Fandom: *"Your ship takes 5 hull damage, 1 damage to each of 2 random systems"*
>   ([[source-fandom-rock-and-slug-standoff]]).
>
> Trusting the game files for what is written (`high` vs `medium`). The gap is 3 vs 5 hull;
> Fandom's figure is consistent with each point of random-system damage also costing a
> point of hull (3 + 1 + 1 = 5), which would make both accounts descriptions of the same
> behaviour. Not confirmed here.

## Version note
The second `<damage amount="1" system="random"/>` in outcome 3 carries an inline
`<!--DLC-->` marker — the file's convention for a line added by Advanced Edition
([[source-newevents]], line 1569). Taken alone that would make the vanilla explosion
3 hull + **one** random-system hit. However the event as a whole sits inside the
`DLC!!! Events added with the DLC` block of `newEvents.xml`, and its only live list entry
(`NEUTRAL_ROCK`) is itself marked `<!--DLC - newEvents-->` — so there is no vanilla form of
this event for the milder damage to belong to. Recorded as `version: ae`, with the inner
marker noted as an unexplained leftover rather than a real edition split.

## Blue Options
None. The two `req`-gated choices in the tree (`req="reactor" max_lvl="24"` here, and the
same pattern in `ROCK_SLUG_GRATEFUL`) both carry `blue="false"` — they are ordinary options
gated on ship state, not blue options.

## Rewards & Risks
- **Best case:** a free reactor bar for no cost at all (hail → demand → Rock agrees →
  grateful outcome 2).
- **Reliable case:** pay 10–15 scrap to defuse the standoff, then a 1/3 shot at a free
  reactor bar and a 1/3 shot at buying one for another 10–15.
- **Risks:** a Rock ship fight with no surrender or escape branch (1/3 of the demand
  branch), or 3 hull plus two random system hits (another 1/3).
- Leaving costs nothing.

## Strategy Notes
- *(Opinion, from the tree structure.)* "Demand the Rock ship pay" is the aggressive line:
  2/3 of its outcomes lead to the Slug reward pool, one of them for free, but the remaining
  1/3 is a hull hit you did not pay for. Paying the debt is the safe line — it always
  reaches the reward pool, at a fixed 10–15 scrap.
- A reactor bar is worth substantially more than 15 scrap at a store, so even the paid
  branch of `ROCK_SLUG_GRATEFUL` is good value.
- Killing the Rock crew rather than destroying the ship upgrades `LOW` `standard` to `MED`
  `standard`, so boarding is worth more than usual here.

## Related
- [[event-slug-and-rock-standoff-in-nebula]] — the nebula wrapper that loads this event
- [[entity-rock-men]], [[entity-slugs]]
- [[item-reactor]] — what the reward pool upgrades

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] Whether the explosion costs 3 or 5 hull — see the contradiction above.
- [ ] Why a `<!--DLC-->` marker appears inside an event that is itself AE-only.
- [ ] Exact scrap values behind `LOW` / `MED` `standard`.

## Sources
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-events-rock]] (per `raw/gamedata/events_rock.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-rock-and-slug-standoff]] (per `raw/wiki/rock-and-slug-standoff.md`)
