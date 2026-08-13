<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: No fuel: refugee trading
URL: https://ftl.fandom.com/wiki/No_fuel:_refugee_trading
Categories: Random_Events, Trading_Events
Revision: 73281
Retrieved: 2026-08-09

---
{{Locations|outoffuel=distresson}}


This event varies, and could be any of the following: 
*''A refugee ship fleeing the Rebel advance enters the system, having picked up your distress beacon. While it doesn't have much fuel to spare, it recognizes you are part of the Federation and offers to split its remaining fuel with you.''
** You receive {{tooltip|low|1-3}} [[Rewards#Fuel only|fuel]].
*''A refugee ship fleeing the Rebel advance enters the system, having picked up your distress beacon. While it doesn't have much fuel to spare, it's hull looks damaged - it is in bad need of scrap and is willing to trade fuel for it.''
*# Trade some scrap for fuel. &nbsp;<span style="color:grey">[ the actual trade offer is shown prior to making the choice ]</span>
*#* ''The refugees thank you for the parts, and gladly pass along the much-needed fuel. They wish you well on your mission, and declare their support for the Federation.''
*#** You receive {{Transaction|3|add_fuel}} and lose {{Transaction|10|subtract_scrap}}.
*# {{Blue Option|Engi Crew|Negotiate a better trade.}}
*#* ''Your Engi analyzes scans of the extensive damage to their hull, calculating potential repair costs. The refugees grumble and protest, but in the end, they admit that their need for repairs is greater than their fuel surplus and offer a better trade.''
*#*# Accept it. &nbsp;<span style="color:grey">[ the actual trade offer is shown prior to making the choice ]</span>
*#*#* You receive {{Transaction|6|add_fuel}} and lose {{Transaction|10|subtract_scrap}}.
*#*# Refuse it.
*#*#* Nothing happens.
*# Refuse their offer.
*#* ''The refugee ship cuts communications and jumps from the system without another word, the galactic equivalent of giving you the cold shoulder.''
*#** Nothing happens.
*#* ''The refugees become desperate at your refusal - apparently, their hull is even more damaged than it first appears. Almost begging, they offer a better trade than before.''
*#*# Accept it. &nbsp;<span style="color:grey">[ the actual trade offer is shown prior to making the choice ]</span>
*#*#* You receive {{Transaction|6|add_fuel}} and lose {{Transaction|10|subtract_scrap}}.
*#*# Refuse their offer again.
*#*#* ''The refugee ship cuts communications and jumps from the system without another word, the galactic equivalent of giving you the cold shoulder.''
*#*#** Nothing happens.
*# The helpless refugees make easy targets. Attack them.
*#* ''Panicked, the refugees immediately surrender as your weapons power up. They pass along their fuel and what few other supplies they have left in exchange for their lives.''
*#** You receive {{tooltip|medium|2-4 fuel}} [[Rewards#Fuel|fuel and scrap]].
*''A refugee ship fleeing the Rebel advance enters the system, having picked up your distress beacon. While it doesn't have much fuel to spare, it is bad need of armaments and is willing to trade for them.''
*# Offer some missiles for fuel.
*#* ''The refugee ship makes the exchange, and wishes you well on your mission.''
*#** You lose {{Transaction|1|subtract_missiles}} and receive {{Transaction|5-7|add_fuel}}.
*#* ''Having traded supplies, the ship suddenly powers up and attacks - it's a pirate ship!''
*#** You lose {{Transaction|1|subtract_missiles}}, receive {{Transaction|5-7|add_fuel}}, and you fight a [[Enemy Ships|Pirate ship]] ([[Rewards#Default_rewards|default rewards]]). <!-- Ship - PIRATE. Datafile - events_ships.xml -->{{SurrenderEscape|timer|90}}
*# Refuse their offer.
*#* {{DuplicateEvent|2}} ''Taking your reluctance as weakness, the refugee ship suddenly bristles with weapons - it's a pirate ship, and it believes it's found easy prey!''
*#** Fight a [[Enemy Ships|Pirate ship]] ([[Rewards#Default_rewards|default rewards]]). <!-- Ship - PIRATE. Datafile - events_ships.xml -->{{SurrenderEscape|timer|90}}
*#* ''Sensing your reluctance, the refugee ship nevertheless parts with a small amount of fuel. It warns you to leave the sector as quickly as possible before it is overtaken by Rebels, then it jumps and vanishes to parts unknown.''
*#** You receive {{tooltip|low|1-3}} [[Rewards#Fuel only|fuel]].
*#* ''The refugee ship apologizes, but they need their fuel. They wish you well, and then vanish from the system.''
*#** Nothing happens.

==Trivia==
This event is called "NO_FUEL_REFUGEE" in the datafiles.
[[Category:Trading Events]]
[[Category:Fuel reward chance]]
[[Category:Fights with Default Rewards]]
[[Category:Ship escape Events]]
[[Category:Pirate ship fights]]
