<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Refueling platform garbled broadcast
URL: https://ftl.fandom.com/wiki/Refueling_platform_garbled_broadcast
Categories: Random_Events, Unique_Events
Revision: 73824
Retrieved: 2026-08-09

---
{{Locations|Abandoned Sector|LRSmap=noship|unique=true}}


''You detect a refueling platform near the beacon, although its broadcast signal is garbled, and you can't make out the message.''
#Hail the platform and attempt to communicate.
#*''There is a screech from your comm system, and the broadcast suddenly cuts off. The platform suddenly begins to move, revealing itself to be a Lanius ship!''
#**[[#Fight a Lanius ship|'''Fight a Lanius ship''']].
#Dock with the platform.
#*''Your ship enters one of the refueling station berths, grateful for a rest.''
#*#Signal for a refuel.
#*#*''No one answers your hails. You run some scans and discover that the station has been recently abandoned, no doubt due to the threat of the Lanius. You empty their fuel reserves before leaving.''
#*#**You receive {{Transaction|3-5|add_fuel}}.
#*#**#Continue...
#*#**#*Nothing happens.
#*#**#{{Blue Option|Improved Sensors|Run another scan at maximum sensitivity.|level=2|shortreq=Sensors}}
#*#**#*''You run an additional more focused scan and find one of the auxiliary refueling platforms has some unclaimed fuel.''
#*#**#**You receive {{Transaction|1-3|add_fuel}}.
#*#**#{{Blue Option|Advanced Sensors|Run another scan at maximum sensitivity.|level=3|shortreq=Sensors}}
#*#**#*''You run an additional more focused scan and find one of the auxiliary refueling platforms has some unclaimed fuel and drone parts.''
#*#**#**You receive {{Transaction|2-3|add_fuel}} and {{Transaction|1-3|add_drones}}.
#*#*''What seemed to be a brief respite turns into a Lanius trap... the first warning is an explosion from your engine room, followed moments later by detection of a Lanius ship at sensor range!''
#*#**Your ship takes <span style="color:red">3 hull</span> damage, 3 damage to <span style="color:red">engines</span>, and you [[#Fight a Lanius ship|'''fight a Lanius ship''']].
#*#*''Your ship's dash suddenly lights up with warnings - a hull breach! Lanius were on board the platform and are now on board your ship. A hidden cruiser comes into view!''
#*#**Your ship takes a <span style="color:red">breach</span> to a random <span style="color:red">room</span>, <span style="color:red">1 lanius boarder</span> beams aboard your ship, and you [[#Fight a Lanius ship|'''fight a Lanius ship''']].
#*#{{Blue Option|Blast Doors|Secure your blast doors - best to be safe when docked.|level=2+|shortreq=Door System}}
#*#*''Your reinforced doors save you from an attempted ambush by the Lanius, who cluster around the doors and hull, attempting to consume your ship. Coldly, you wipe them out one by one with your weapon array, then take control of the station and take its fuel reserves.''
#*#**You receive {{Transaction|5|add_fuel}}.
#Ignore the platform.
#*''You leave the platform alone, and prepare to jump.''
#**Nothing happens.

==Fight a Lanius ship==
*{{Winning|destroyed=true|The ship explodes, leaving behind a collection of useful scrap material.}}<br/>{{Winning|deadCrew=true|There are no more life-signs remaining on the ship. You strip it of useful materials.}}
**You receive medium [[Rewards#Standard|scrap with resources]]. 
***Investigate the fueling platform.
****''It looks as if the Lanius were uninterested in the fuel reserves on the station, and there is a good amount of fuel left. You take what your ship can hold and prepare to jump to the next beacon.''
*****You receive {{Transaction|3-5|add_fuel}}.

==Trivia==
This event is called "LANIUS_FUELING_STATION" in the datafiles.
[[Category:Advanced Edition Content Events]]
[[Category:Hull damage risk]]
[[Category:System damage risk]]
[[Category:Hull breach risk]]
[[Category:Boarding risk]]
[[Category:Fuel reward opportunity]]
[[Category:Drone Parts reward chance]]
