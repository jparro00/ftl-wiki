<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: No fuel: prepare to dock
URL: https://ftl.fandom.com/wiki/No_fuel:_prepare_to_dock
Categories: Random_Events
Revision: 73278
Retrieved: 2026-08-09

---
{{Locations|outoffuel=distressboth}}


''A ship approaches. They hail you saying, "You need some fuel? We'll prepare to dock to help."''
# Graciously accept their offer.
#* ''They pull close to your ship and unload some fuel saying, "Try not to run out of fuel again. These are dangerous times; who knows who could have showed up."''
#** You receive {{Transaction|2-6|add_fuel}}.
#* ''They approach and dock with your ship. On board they present an offer.'
#*# Gladly Trade. &nbsp;[ the actual trade offer is shown ]
{{Fuel Trader High List|prefix=#*#}}
#*# Respectfully Decline.
{{Fuel Trader Pt2|prefix=#*#}}
#* ''As they approach, you detect their weapons powering up. It seems their intentions are hostile!''
#** Fight a [[Enemy Ships|Pirate ship]] ([[Rewards#Default_rewards|default rewards]]). <!-- Ship - PIRATE. Datafile - events_ships.xml -->{{SurrenderEscape|timer|90}}
#* ''As their ship pulls up next to yours, their captain continues, "Yes, we'll certainly help... Help to relieve you of that nice ship!" Sensors detect a hidden teleporter has been activated. We've been boarded!''
#** <span style="color:red">2-3 human boarders</span> beam aboard your ship and you fight a [[Enemy Ships|Pirate ship]] ([[Rewards#Default_rewards|default rewards]]). <!-- Ship - PIRATE_FUEL. Datafile - events_ships.xml -->{{SurrenderEscape|timer|80}}
# Request they keep their distance.
#* ''"I assure you that we mean no harm. See, we'll send some fuel over on a transport." A small ship docks and offloads some fuel just as they said. They leave, saying, "Stay cautious, friend."''
#** You receive {{Transaction|1-4|add_fuel}}.
#* ''They reply,"Keep our distance? Let's see if you can stop us!" They power up their weapons and advance.''
#** Fight a [[Enemy Ships|Pirate ship]] ([[Rewards#Default_rewards|default rewards]]). <!-- Ship - PIRATE_FUEL. Datafile - events_ships.xml -->{{SurrenderEscape|timer|80}}
#* ''"No one trusts anyone these days..." The ship jumps away.''
#** Nothing happens.
# {{Blue Option|Advanced Sensors|Run a detailed scan with your sensors before responding.|level=3|shortreq=Sensors}}
#* [[#Scan the ship|'''Scan the ship''']].
# {{Blue Option|Long-Ranged Scanners|Run a detailed scan before responding.}}
#* [[#Scan the ship|'''Scan the ship''']].

==Scan the ship==
* ''Sensors indicate their ship is without military-grade weaponry, even small arms. You allow them to dock and they give you some fuel saying, "I remember a time when we didn't have to be so paranoid about each others' intentions... Stay safe."''
** You receive {{Transaction|3-7|add_fuel}}.
* ''Sensors are picking up armed crew and considerably more weaponry than is legal for a craft of this size. This is surely a trap.''
*# Power up weapons and prepare for a fight.
*#* Fight a [[Enemy Ships|Pirate ship]] ([[Rewards#Default_rewards|default rewards]]). <!-- Ship - PIRATE_FUEL. Datafile - events_ships.xml -->{{SurrenderEscape|timer|80}}
*# {{Blue Option|Cloaking|Cloak and get out of scanning range before they have a chance to lock on.}}
*#* ''Your highly advanced cloaking system allows you to get out of range easily since they were still out of firing range. Eventually the ship jumps away.''
*#** Nothing happens.

==Trivia==
This event is called "FUEL_APPROACH" in the datafiles.
[[Category:Fights with Default Rewards]]
[[Category:Boarding risk]]
[[Category:Fuel reward chance]]
[[Category:Ship escape Events]]
[[Category:Pirate ship fights]]
