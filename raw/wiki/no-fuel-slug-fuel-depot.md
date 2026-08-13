<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: No fuel: Slug fuel depot
URL: https://ftl.fandom.com/wiki/No_fuel:_Slug_fuel_depot
Categories: Random_Events, Trading_Events
Revision: 73296
Retrieved: 2026-08-09

---
{{Locations|outoffuel=distresson}}


''A mobile Slugman fuel depot enters scanning range. "My prices are fair, but I ask one thing - do not insult me with negotiation!" You check out his price list.''
# Buy 5 fuel for 50 scrap.
#* ''The trader looks shocked. You're struck by the sense that this is the first time anyone's ever paid him these prices.''
#** You lose {{Transaction|50|subtract_scrap}} and receive {{Transaction|5|add_fuel}}.
# Buy 10 fuel for 95 scrap. (BEST DEAL!)
#* ''The trader looks shocked. You're struck by the sense that this is the first time anyone's ever paid him these prices.''
#** You lose {{Transaction|95|subtract_scrap}} and receive {{Transaction|10|add_fuel}}.
# Negotiate.
#* ''You offer a more reasonable price but the Slugman is outraged! He moves in to attack!''
#** Fight a [[Slug Ships|Slug ship]] that is '''running away'''. <!-- Ship - JELLY_OVERPRICED. Datafile - events_ships.xml -->{{SurrenderEscape|timer|80}}{{SurrenderEscape|surrenderno}}
#*** {{Winning|gotaway=true|The ship jumps away without a word. You hope they didn't leave to get reinforcements.}}
#**** Nothing happens.
#*** {{Winning|destroyed=true|You try and collect as much fuel from the wreckage as possible.}}
#**** You receive {{tooltip|medium|2-4 fuel}} [[Rewards#Fuel|fuel and scrap]].
#*** {{Winning|deadCrew=true|With the Slug ship subdued you are free to collect as much fuel as possible.}}
#**** You receive {{tooltip|high|3-6 fuel}} [[Rewards#Fuel|fuel and scrap]].

==Trivia==
This event is called "FUEL_ON_SLUG_OVERPRICED" in the datafiles.
[[Category:Trading Events]]
[[Category:Fuel reward opportunity]]
[[Category:Ship escape Events]]
