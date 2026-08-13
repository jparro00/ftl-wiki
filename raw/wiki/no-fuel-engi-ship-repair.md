<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: No fuel: Engi ship repair
URL: https://ftl.fandom.com/wiki/No_fuel:_Engi_ship_repair
Categories: Random_Events
Revision: 73274
Retrieved: 2026-08-09

---
{{Locations|outoffuel=distressoff}}


''As you drift through space an Engi ship passes through. From listening to their com channel it sounds like they're discussing making repairs on their ship.''
# Hail them.
#* ''Upon discovering your need, the Engi gladly offer some of their extra fuel reserves. It's amazing how altruistic these robotic creatures can be.''
#** You receive {{Transaction|2-6|add_fuel}}.
#* ''The Engi respond to your signal. "Your need: fuel. This unit's need: scrap. Exchange beneficial. Exchange permitted?"''
#*# Make the trade.
#*#* ''You make the exchange and the Engi leave without another word.''
#*#** You lose {{Transaction|10-20|subtract_scrap}} and receive {{Transaction|4-6|add_fuel}}.
#*# Decline.
#*#* ''The Engi coolly cut communications and continue on their journey.''
#*#** Nothing happens.
#* ''The Engi fail to respond, but move to intercept. You detect abnormal electromagnetic signals aboard the ship - someone has reprogrammed them to fight!''
#** Fight an [[Enemy_Ships#Engi_Ships|Engi ship]] that is '''running away'''. <!-- Ship - FUEL_OFF_ENGI_DUBIOUS. Datafile - events_ships.xml -->{{SurrenderEscape|timer|80}}{{SurrenderEscape|surrenderno}}
#*** {{Winning|gotaway=true|The ship jumps away without a word. You hope they didn't leave to get reinforcements.}}
#**** Nothing happens.
#*** {{Winning|destroyed=true|With the hostile Engi ship destroyed you carefully extract as much fuel as possible from the wreckage.}}
#**** You receive {{tooltip|medium|2-4 fuel}} [[Rewards#Fuel|fuel and scrap]].
#*** {{Winning|deadCrew=true|With the hostile Engi subdued you carefully extract as much fuel as possible from the ship.}}
#**** You receive {{tooltip|high|3-6 fuel}} [[Rewards#Fuel|fuel and scrap]].
#* ''The Engi respond to your signal. "Identity: Federation. I/O error: Federation = [void]." All further hails go unanswered.''
#** Nothing happens.
# Ignore them.
#* ''They clearly are busy because they don't notice your ship at all.''
#** Nothing happens.
# {{Blue Option|Hull Repair Drone|Offer to help repair their hull.}} &nbsp;[ {{Transaction|1|subtract_drones}} ]
#* ''They happily accept your offer for help. Once the drone does its work they transfer over some fuel for your trouble.''
#** You receive {{Transaction|4-6|add_fuel}}.

==Trivia==
This event is called "FUEL_OFF_ENGI_DUBIOUS" in the datafiles.
[[Category:Fuel reward opportunity]]
[[Category:Drone Parts use Events]]
[[Category:Ship escape Events]]
