<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Merchant's request
URL: https://ftl.fandom.com/wiki/Merchant's_request
Categories: Random_Events, Unique_Events, Trading_Events
Revision: 74272
Retrieved: 2026-08-09

---
{{Locations|Civilian Sector|Engi Controlled Sector|Engi Homeworlds|Pirate Controlled Sector|Rebel Controlled Sector|Rebel Stronghold|LRSmap=noship|unique=true}}

__TOC__
''You arrive at a populated sector. One merchant seems to be mass-broadcasting a request for a mercenary ship to aid him. Shall we respond?''
# Yes.
#* ''"Great, I was worried no one would respond. My usual carrier is days late. I need you to deliver this cargo of drone parts to a small station a few jumps from here. I'll pay you a bit of scrap now, but they will surely tip you generously."''
#*# Accept.
#*#* ''Great! I uploaded their location to your star map. I'm running out of options, so I have no choice but to trust you'll do what you have agreed to do.''
#*#** You receive {{Transaction|5|add_drones}} and [[#Merchant's Delivery|'''Merchant's Delivery''']] quest marker is added to your map.
#*# Decline.
#*#* ''"Fine, I'll keep looking for someone who wishes to make some easy money..."''
#*#** Nothing happens.
#* ''"Your ship seems reasonably equipped... A freighter carrying a shipment of my goods is a week late. The fools flew through a pirate-filled sector in their haste and I fear for the cargo's safety. I'm looking for a less incompetent captain to investigate."''
#*# Accept.
#*#* ''"At least you're confident, for what little that's worth. Here is their last known location."''
#*#** [[#Merchant's Investigation|'''Merchant's Investigation''']] quest marker is added to your map.
#*# Decline
#*#* ''"At least YOU are willing to admit your incompetence. Thank you for saving me the cost of paying more fools to go to their death."''
#*#** Nothing happens.
# No.
#* Nothing happens.


==Merchant's Delivery==
:{{Long-Ranged Scanners info|shipdetected=noship}}
''You arrive at the location given to you by the merchant. You are supposed to deliver drone parts to a station here.''
* [[#The station doesn't respond|'''The station doesn't respond to your hails''']]
* [[#The station responds|'''The station responds to your hails''']]

===<h2><span style=font-size:smaller;>The station doesn't respond</span></h2>===
{{:Research station with no response}}

===<h2><span style=font-size:smaller;>The station responds</span></h2>===
''You find the station and they respond to your hails immediately, saying, "It took you long enough! We have practically no use for these now... I refuse to pay full price, take this and leave the cargo in our holds."''
# Accept the paltry payment. &nbsp;<span style="color:grey">[ the actual trade offer is shown before you make the choice ]</span>
#* ''You drop the parts off and take your pay.''
#** You receive {{Transaction|20-30|add_scrap}} and lose {{Transaction|5|subtract_drones}}.
# Refuse and keep the drone parts.
#* ''"Fine, I was bluffing. I'll pay the full price."''
#*# Accept the new offer. &nbsp;<span style="color:grey">[ the actual trade offer is shown before you make the choice ]</span>
#*#* You receive {{Transaction|40-55|add_scrap}} and lose {{Transaction|5|subtract_drones}}.
#*# Leave.
#*#* Nothing happens.
#* ''The merchant disconnects in a huff.''
#** Nothing happens.
# {{Blue Option|Mind Control|Convince him that he's being 'unfair'.}}
#* ''"I'm being unfair. You did the job and the parts are here safe and sound. Here is the agreed upon amount."''
#*# Accept the new offer. &nbsp;<span style="color:grey">[ the actual trade offer is shown before you make the choice ]</span>
#*#* You receive {{Transaction|40-55|add_scrap}} and lose {{Transaction|5|subtract_drones}}.
#*# Leave.
#*#* Nothing happens.
# {{Blue Option|Weapons|Remain silent but power up your weapons.|level=6+|shortreq=Weapon Control}} &nbsp;<span style="color:grey">[ the actual trade offer is ''not'' shown ]</span>
#* ''"You make a good point. You traveled all the way out here to fulfill our request, despite what must have been... a difficult scenario to cause such a delay. Here, we'll even tip you for the inconvenience you must have gone through..."''
#** You receive {{Transaction|55-70|add_scrap}}, {{Transaction|2-5|add_fuel}} and lose {{Transaction|5|subtract_drones}}.


==Merchant's Investigation==
:{{Long-Ranged Scanners info|shipdetected=noship}}
''You arrive at the last known location of the merchant's delivery. You begin to scan for the lost ship.''
*''You find the remains of the ship. It seems to have severe external damage, but you cannot pinpoint a cause. The majority of its cargo seems intact. You manage to discern the ship's intended destination.''
**You receive medium [[Rewards#Standard|scrap with resources]].
**# Take the cargo and head to its original destination in search of a reward.
**#* [[#Deliver to the Station quest marker|'''Deliver to the Station''' quest marker]] is added to your map.
**# Take the cargo for yourself.
**#* [[#Investigate the Cargo|'''Investigate the cargo''']].
*''You find a severely damaged ship floating among some debris. The crew hails you, "I can't believe that cheap bastard sent someone after us! I thought we would freeze to death. If you help us complete the delivery, we'll share the reward and join your crew."''
*# Promise to deliver the cargo and ask if any would be interested in joining your crew.
*#* ''They upload the delivery destination once on board. One takes you up on your offer, the rest you drop off at a nearby station.''
*#**You receive a <span style="color:limegreen">crewmember</span> and [[#Deliver to the Station quest marker|'''Deliver to the Station''' quest marker]] is added to your map.
*# Take the cargo but drop them off at a nearby station.
*#* [[#Investigate the Cargo|'''Investigate the cargo''']].
*# {{Blue Option|Teleporter|Beam the cargo aboard and leave them to their fate.}}
*#* [[#Investigate the Cargo|'''Investigate the cargo''']].
*''After a quick scan, you find a ship being chased by a pirate. This must be the missing delivery ship! You move in to rescue them.''
** Fight a [[Enemy_Ships|Pirate ship]]. <ref name="Enemy ship (JELLY_PIRATE_MERCHANT)">{{SurrenderEscape(alt)|no|JELLY_PIRATE_MERCHANT|events_ships.xml}}</ref>
*** {{Winning|destroyed/deadCrew=true|You contact the delivery ship, who are grateful for your assistance. They offer you a reward for saving them.}}
**** You receive medium [[Rewards#Standard|scrap with resources]].

===<h2><span style=font-size:smaller;>Investigate the Cargo</span></h2>===
*''The cargo was some food and medical supplies, nothing that you need right now. You make a note of the delivery destination in case you want to drop off the cargo for the payment.''
** [[#Deliver to the Station quest marker|'''Deliver to the Station''' quest marker]] is added to your map.
*''You find a prototype weapon inside. You quickly install it on the ship.''
** You receive a <span style="color:limegreen">weapon</span>.
*''There were general military supplies in the cargo crates. You take what you can use.''
** You receive high [[Rewards#Standard|scrap with resources]].

===<h2><span style=font-size:smaller;>Deliver to the Station quest marker</span></h2>===
:{{Long-Ranged Scanners info|shipdetected=nolrs+noship}}
''You find the station that had ordered your cargo. You drop it off and they respond, "Ignoring the fact that this is days late, we really appreciate that you delivered our materials. We realize how dangerous this sector is these days. Take this as payment."''
* You receive a <span style="color:limegreen">drone schematic</span> with medium <span style="color:#70b8ff">scrap</span>.

==Notes==
This event is called "MERCHANT_REQUEST" in the datafiles. 
* The [[#The station doesn't respond|station doesn't respond]] subevent in the [[#Merchant's Delivery|Merchant's Delivery]] scenario can be found as [[Small research station with no response]] standalone event, but with a slightly different intro text and an additional [[Augmentations#Lifeform_Scanner|blue option]] for the <span style="color: #09f">Lifeform Scanner</span>.
===Reference notes===
<references/>
[[Category:Events with Quest Markers]]
[[Category:Drone Schematics reward chance]]
[[Category:Weapon reward chance]]
[[Category:Drone Parts reward chance]]
[[Category:Trading Events]]
[[Category:Fuel reward chance]]
[[Category:Pirate ship fights]]
