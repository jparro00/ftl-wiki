<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: No fuel: automated refueling ship
URL: https://ftl.fandom.com/wiki/No_fuel:_automated_refueling_ship
Categories: Random_Events, Trading_Events
Revision: 73275
Retrieved: 2026-08-09

---
{{Locations|outoffuel=distresson}}


''A small ship arrives with a message, "This automated ship will provide refueling services once a monetary exchange is complete. Complimentary amounts of fuel are available in emergencies only."''
# Request emergency fuel reserves.
#* ''"This ship has registered that your one-time complimentary emergency fuel allowance has been consumed."''
#**You receive {{tooltip|low|1-3}} [[Rewards#Fuel only|fuel]].
# Buy 5 fuel for 20 scrap. [ {{Transaction|20|subtract_scrap}} ]
#* "Automated refueling complete."
#** You receive {{Transaction|5|add_fuel}}.
# Buy 2 fuel for 8 scrap. [ {{Transaction|8|subtract_scrap}} ]
#* "Automated refueling complete."
#** You receive {{Transaction|2|add_fuel}}.
# Attack the automated ship.
#* Fight an [[AI-Controlled Rebel Ships|Auto-ship]] that is '''running away'''. <!-- Ship - AUTO_FUEL_SELLER. Datafile - events_ships.xml -->{{SurrenderEscape|timer|80}} <!-- The game code (events_ships.xml) also contains line "<escape chance="0.5" min="2" max="5" >", but it seems unlikely that it has any effect - meaning if the ship only has 50% chance to try to escape when damaged enough vs starting to escape immediately - in this case, however it needs testing or code evaluation to be 100% sure -->
#** {{Winning|escape=true|It is apparent that the ship was not intended for combat. It seems to be trying to jump away.}}
#*** {{winning|gotaway=true|The ship jumps away without a word. You hope they didn't leave to get reinforcements.}}
#**** Nothing happens.
#** {{Winning|destroyed=true|As the ship breaks apart, you frantically try to salvage the remaining fuel from its cargo.}}
#*** You receive {{tooltip|medium|2-4 fuel}} [[Rewards#Fuel|fuel and scrap]].

==Trivia==
This event is called "FUEL_SELLER_DISTRESS" in the datafiles. 
*The "one-time complimentary emergency fuel allowance" is mere flavor text and the first option will always be available each time the event is encountered.
[[Category:Trading Events]]
[[Category:Fuel reward opportunity]]
[[Category:Ship escape Events]]
[[Category:Auto-ship fights]]
