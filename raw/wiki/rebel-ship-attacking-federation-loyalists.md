<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Rebel ship attacking Federation loyalists
URL: https://ftl.fandom.com/wiki/Rebel_ship_attacking_Federation_loyalists
Categories: Random_Events, Unique_Events
Revision: 74715
Retrieved: 2026-08-09

---
{{Locations|Civilian Sector|Pirate Controlled Sector|Rebel Controlled Sector|Rebel Stronghold|Rock Controlled Sector|Rock Homeworlds|Uncharted Nebula|LRSmap=noship|unique=true}}


The intro text for this event varies, and could be any of the following:
* ''Upon arriving at this beacon, you detect a distress call. Local scans reveal that a Federation transport is under attack from a Rebel scout!''
* ''You immediately notice a Rebel ship chasing what appears to be a civilian transport. However you are detecting chatter on an encrypted Federation channel... That transport is carrying Federation loyalists!''
* ''Your sensors are picking up a distress call on an encrypted Federation channel. You eventually find a Federation scout being chased by a Rebel fighter!''
<div style="opacity: 50%">
----</div>
# Aid the Federation ship.
#* ''You power up your weapons and engage the Rebel ship.''
#** Fight a [[Enemy_Ships#Rebel_ships|Rebel ship]]. <!--ship name="REBEL_VS_FEDERATION" (events_ships.xml)--><span style="color:grey">(never surrenders, never escapes)</span>
#*** {{Winning|destroyed=true|With the ship destroyed, you quickly collect useful resources.}}<br />{{Winning|deadCrew=true|With the crew of the Rebel ship dead, you salvage what you can.}}
#**** You receive medium [[Rewards#Standard|scrap with resources]].
#***** [[#Contact the Federation ship|'''Contact the Federation ship''']].
# Use this chance to escape.
#* ''The Rebel's preoccupation with the Federation ship allows you to slip away undetected. However, you can't help but feel you should have helped them.''
#** Nothing happens.

==='''Contact the Federation ship'''===
* ''"Thank you for saving us. This ship is transporting Federation civilians on the run from the rebellion and we don't have the equipment to fight for ourselves. I don't have much to offer, but I can inform you of a hidden Federation base nearby. Perhaps they can assist you more."''
** A [[#Hidden Federation Base|'''Hidden Federation Base''']] quest marker is added to your map.
* ''"Thanks, we didn't think there would be Rebel ships all the way out here. They seem to be searching for something. Take some extra supplies as thanks for your aid."''
** You receive medium [[Rewards#Standard|scrap with resources]].
* ''Their ship looks to be on the verge of destruction and life signs are fading quickly.''
*# Quickly try to rescue the crew.
*#* ''Despite your efforts the majority do not survive. The sole survivor offers to join your crew and helps you strip the now derelict ship of useful components.''
*#** You receive a <span style="color:limegreen">crewmember</span> and low [[Rewards#Standard|scrap with resources]].
*# {{Blue Option|Nano Med-bot Dispersal|Pump their ship with Nano Med-bots to aid in the rescue.|shortreq=Engi Med-bot Dispersal}}
*#* ''You drag the injured and dying crew on to your ship. The Med-bots help stabilize their condition, but most perish. The surviving shields operator offers to join your crew and helps you strip their broken ship of scrap.''
*#** You receive a <span style="color:limegreen">crewmember</span> with '''1''' skill in shields, and {{Tooltip|high|3-6 fuel}} [[Rewards#Fuel|fuel and scrap]].
*# {{Blue Option|Teleporter|Lock on to all remaining life signatures and beam them onto your ship.}}
*#* ''Your quick reactions allow you to stabilize a few of the seriously wounded crewmembers. An infantryman offers to join your crew and the rest tell you of a hidden Federation base a few jumps from here.''
*#** You receive a <span style="color:limegreen">crewmember</span> with '''1''' skill in combat, medium [[Rewards#Scrap only|scrap]], and a [[#Hidden Federation Base|'''Hidden Federation Base''']] quest marker is added to your map.
*# {{Blue Option|Healing Burst|Use a healing bomb to keep them alive.}} [ {{Transaction|1|subtract_missiles}} ]
*#* ''You launch a healing bomb into their ship and the Nanobots are able to keep the crew stabilized. Once they come to, you send over some supplies to keep them healthy enough to get to friendly territory.''
*#** ''Now that they're safe an engineer offers to join your crew and the rest tell you of a hidden Federation base a few jumps from here.''
*#*** You receive a <span style="color:limegreen">crewmember</span> with '''1''' skill in engines, medium [[Rewards#Scrap only|scrap]], and a [[#Hidden Federation Base|'''Hidden Federation Base''']] quest marker is added to your map.


{{Hidden federation base}}

==Trivia==
This event is called "REBEL_VS_FEDERATION" in the datafiles.
* This event is meant to occur at a [[distress beacon]] but won't because the <code><distressBeacon/></code> tag is missing in its definition.
__NOTOC__
[[Category:Crew reward chance]]
[[Category:Anti-Ship Battery support]]
[[Category:Events with Quest Markers]]
