<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Refueling platform
URL: https://ftl.fandom.com/wiki/Refueling_platform
Categories: Random_Events, Unique_Events, Filler_Events
Revision: 74855
Retrieved: 2026-08-09

---
{{Locations|Abandoned Sector|Engi Controlled Sector|Engi Homeworlds|Slug Controlled Nebula|Slug Home Nebula|alsooccur=exitandfiller|LRSmap=noship|unique=true}}


''A small platform orbits near this beacon - it looks like a fueling station of some sort, and it is cheerily broadcasting reasonable prices in a spectrum of frequencies and languages.''
#Dock with the refueling platform.
#*''The platform makes an offer.''
#*#Accept it. &nbsp; [ {{Transaction|5-10|subtract_scrap}} ]
#*#*You receive {{Transaction|5|add_fuel}}.
#*#Reject it.
#*#*Nothing happens.
#*''The automated platform seems to be damaged. You can likely steal as much fuel as remains.''
#*#Steal it.
#*#*''If you take the fuel at least it won't fall into the hands of the Rebels. You breach the containment and access what remains of the fuel reserves.''
#*#**You receive {{Transaction|3-5|add_fuel}}.
#*#War doesn't justify abandoning one's values. You leave it alone.
#*#*Nothing happens.
#*''The platform seems to be malfunctioning and could ignite at any moment.''
#*#Quickly dock and refuel.
#*#*''You're able to safely refuel and get clear before the station explodes.''
#*#**You receive {{Transaction|5|add_fuel}}.
#*#*''Just as you hook up to refuel, the station ignites and explodes. Your own fuel reserve ignites, losing your precious fuel and damaging your ship.''
#*#**Your ship takes <span style="color:red">3 hull</span> damage, 3 damage with [[File:S_fire2.png|28px|bottom|1-2 fires|alt=fire]] to <span style="color:red">engines</span>, and lose {{Transaction|3|subtract_fuel}}.
#*#Give the station a wide berth and carry on.
#*#*''You pull away from the station. After a short time a few silent explosions cause the depressurized tanks to implode.''
#*#**Nothing happens.
#*''You dock and signal the fuel station's staff to begin refueling.''
#*#Wait for them to finish.
#*#*''As you dock with the refueling platform, there is an explosion from your engine room! Warning lights flash in your ship as pirates from the station swarm aboard your vessel!''
#*#**Your ship takes <span style="color:red">3 hull</span> damage, 3 damage to <span style="color:red">engines</span>, and <span style="color:red">2-4 boarders</span> beam aboard your ship.
#*#{{Blue Option|Blast Doors|Seal your blast doors, one can never be too careful when docked.|level=2+|shortreq=Door System}}
#*#*''Pirates hidden on the station are confounded by your security locks, turning an attempted ambush into a fish-in-a-barrel firefight. You take control of the station and take its fuel reserves.''
#*#**You receive {{Transaction|5|add_fuel}}.
#*''The refueling station welcomes you into one of its berths, and as you hail them, there is an explosion from your engine room! While assessing the damage, you detect a Pirate Ship closing fast!''
#**Your ship takes <span style="color:red">3 hull</span> damage, 3 damage to <span style="color:red">engines</span>, and you fight a [[Enemy Ships|Pirate ship]] ([[Rewards#Default_rewards|default rewards]]). {{SurrenderEscape|surrender+escape|PIRATE|events_ships.xml|50|30-40|3-4|50|20-40|2-4}}
#Ignore the refueling platform.
#*{{DuplicateEvent|2}} Nothing happens.
#*''As you prepare to leave the system, a Pirate ship suddenly appears on scanners - it looks like it was attempting to use the platform as bait!''
#**Fight a [[Enemy Ships|Pirate ship]] ([[Rewards#Default_rewards|default rewards]]). {{SurrenderEscape|surrender+escape|PIRATE|events_ships.xml|50|30-40|3-4|50|20-40|2-4}}

==Trivia==
This event is called "FUELING_STATION" in the datafiles.
[[Category:Fuel reward chance]]
[[Category:Fights with Default Rewards]]
[[Category:Hull damage risk]]
[[Category:Boarding risk]]
[[Category:System damage risk]]
[[Category:Fire risk]]
[[Category:Fuel loss risk]]
