<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Auto-ship near radar station
URL: https://ftl.fandom.com/wiki/Auto-ship_near_radar_station
Categories: Random_Events, Unique_Events
Revision: 74662
Retrieved: 2026-08-09

---
{{Locations|Rebel Controlled Sector|Rebel Stronghold|LRSmap=ship|unique=true}}


''A Rebel automated ship sits dormant near a Rebel forward radar station.''
#Approach the station.
#*''The ship powers up and targets you.''
#**[[#Fight the Auto-ship|'''Fight the Auto-ship''']].
#Keep your distance and wait for the FTL to charge.
#*Nothing happens.
#{{Blue Option|Combat Drone|Send a drone to distract the automated ship.}} <ref><span style="color: #09f">(Combat Drone)</span> : Combat Drone Mark I, Combat Drone Mark II, Anti-Ship Beam Drone I and Anti-Ship Beam Drone II are <span style="color:limegreen">eligible</span>.</ref>&nbsp;&nbsp;[ {{Transaction|1|subtract_drones}} ]
#*{{DuplicateEvent|2}} ''Your combat drone attacks the automated ship and then retreats, luring it away. You quickly move up to the radar station to access it.'' &nbsp;'''OR''' &nbsp;''Your combat drone repeatedly fires at the automated ship. It can't break through its shields, but is at least enough of a distraction to allow you to access the radar station.''
#**[[#Access the station|'''Access the station''']].
#*''Before your drone has a chance to attack, the automated ship activates and shoots it down. It then detects your ship and moves in on your position.''
#**[[#Fight the Auto-ship|'''Fight the Auto-ship''']].

===<h2><span style=font-size:smaller;>Fight the Auto-ship</span></h2>===
*{{Winning|destroyed=true|You salvage what you can and approach the station. It is used to relay information to the Rebel Fleet. You could attempt to hack it to give the Rebels false information.}}
**You receive medium [[Rewards#Scrap only|scrap]].
**#Attempt to manually hack into the station.
**#*[[#Access the station|'''Access the station''']].
**#Don't risk it. Leave the station.
**#*Nothing happens.
**#{{Blue Option|Hacking|Use a drone to hack into the station.}} &nbsp;&nbsp;[ {{Transaction|1|subtract_drones}} ]
**#*''You successfully hack into their system and transmit false information about your location. That should hold off the fleet for at least a little while. You also are able to download data about the surrounding beacons.''
**#**The current sector <span style="color:limegreen">map</span> is <span style="color:limegreen">revealed</span>, and Rebel Fleet is <span style="color:limegreen">delayed</span> for <span style="color:limegreen">1</span> turn.

===<h2><span style=font-size:smaller;>Access the station</span></h2>===
*''You successfully hack into their system and transmit false information about your location. That should hold off the fleet for at least a little while.''
**Rebel Fleet is <span style="color:limegreen">delayed</span> for <span style="color:limegreen">1</span> turn.
*''The firewalls prove too difficult to bypass. As you are about to disconnect, you stumble across unprotected information about the surrounding beacons. Your map is updated.''
**The current sector <span style="color:limegreen">map</span> is <span style="color:limegreen">revealed</span>.
*''As you attempt to hack in, you set off a hidden alarm system. It seems that now the Rebels must surely be aware of your position! You hasten back to the ship to jump away.''
**Rebel Fleet <span style="color:red">pursuit</span> is <span style="color:red">doubled</span> for <span style="color:red">1 jump</span>.
*''You are unable to penetrate the computer's defenses. You give up and return to the ship.''
**Nothing happens.

==Notes==
This event is called "AUTO_DEFENSE_RADAR" in the datafiles.
===Reference notes===
<references/>
__NOTOC__
[[Category:Drone Parts use Events]]
[[Category:Rebel Fleet advancement risk]]
[[Category:Rebel Fleet delay opportunity]]
[[Category:Beacon Map reveal opportunity]]
[[Category:Auto-ship fights]]
