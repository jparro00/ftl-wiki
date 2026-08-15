<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-14. Source layer: do not edit. -->
Title: Rewards
URL: https://ftl.fandom.com/wiki/Rewards
Categories: Mechanics
Revision: 74729
Retrieved: 2026-08-14

---
[[Random_Events|Random events]] can yield rewards in many forms. These rewards come in the form of [[scrap]], [[fuel]], [[missiles]], [[Drone parts|drone parts]], [[weapons]], [[Drone_Control#Drone_Schematics|drone schematics]], [[augmentations]], [[Crew races|crewmembers]], [[hull]] repairs, delaying the [[Rebel Fleet]], and getting the map revealed; some rewards provide [[Systems|system/subsystem]] upgrades, or [[reactor]] upgrades.

==Rewards amounts==

===Scrap rewards amounts===
The amount of scrap rewarded is determined by the sector number, the scrap reward tier, and the game difficulty. As the game progresses, the scrap amount collected is increased, and the increase is higher for the lower game difficulty. <ref name="Calculated FTL. Scrap sectors, Auto reward values: Scrap rewards.">[https://steamcommunity.com/sharedfiles/filedetails/?id=2127539536 Calculated FTL. Scrap sectors, Auto reward values: Scrap rewards.]</ref>

{| class="table" align="center" style="margin-top:-20px;" cellpadding="0" cellspacing="0" border="0"
|-
|{{Scrap rewards (Easy)}}
|{{Scrap rewards (Normal)}}
|{{Scrap rewards (Hard)}}
|}

===Resources rewards amounts===
Resources rewards do not vary by sector or difficulty. <ref name="Calculated FTL. Auto reward values: Resource rewards.">[https://steamcommunity.com/sharedfiles/filedetails/?id=2127539536 Calculated FTL. Auto reward values: Resource rewards.]</ref>

{| class="table" align="center" style="margin-top:-20px;" cellpadding="0" cellspacing="0" border="0"
|-
|{{Resources rewards}}
|}

==Auto-rewards==
According to the game files stored in <code>ftl.dat</code>, there are several types and tiers of rewards. Most of these reward types have tiers (a tier will be denoted here onward by a letter T): '''Low''' (low scrap multiplier or low amount of resources), '''Medium''', '''High''' (high scrap multiplier or high amount of resources), and '''Random''' (one of the other 3 tiers is randomly chosen). These tiers and the scrap sector determine how much of the reward you will receive. The reward types are listed below: (Note: <span style="color:grey">the grey-colored text in parentheses on this page shows examples of the reward notation on the event pages, however, on the actual event pages these notations are</span> <span style="color:#70B8FF">blue-colored links</span> except for the tier word preceding the link.)

===Standard===
*T scrap + low resources (2 random resources among fuel, missiles, and drone parts) + roughly a 3% chance to include a bonus weapon, augmentation, or drone schematic. <span style="color:grey">(low/medium/high scrap with resources)</span>
**Guaranteed weapon or drone schematic rewards outside the auto-reward will prevent the bonus from being rolled.
**Guaranteed augment rewards outside the auto-reward will be overwritten by this, if the bonus is an augmentation.

===Stuff===
*T resources (2 random resources among fuel, missiles, and drone parts) + low scrap + roughly a 6% chance to include a bonus weapon, augmentation, or drone schematic. This type of reward is most often used in non-scripted (i.e. not guaranteed to occur) ship surrenders. <span style="color:grey">(Medium/High tier - medium/high resources with some scrap; Low tier - low resources and scrap)</span>
**If the 6% roll for a bonus weapon, augmentation, or drone schematic is successful, the scrap reward tier will also match the overall reward tier rather than being low tier. <ref name="Calculated FTL. Bonuses.">[https://steamcommunity.com/sharedfiles/filedetails/?id=2127539536 Calculated FTL. Bonuses.]</ref> <span style="color:grey">(e.g. the surrender reward in the [[Pirate bribing you for unknown ship]] event is High tier resources: if the 6% bonus item reward chance is rolled successfully, then the scrap part of the reward will also be High tier)</span>
**Ships surrender offers in [[:Category:Fights with Default Rewards|fights with default rewards]] and [[:Category:Fights with Default Rewards (Lanius)|fights with default rewards (Lanius)]] are random tier.<!-- The ships are: "LANIUS_SHIP", "PIRATE", "REBEL", "ROCK_SHIP", ... --> A successful 6% bonus item roll modifies the scrap part of the reward to match the resources tier. <span style="color:grey">(e.g. if a Medium tier is rolled, the reward will be: item + medium resources + medium scrap)</span>
**Guaranteed weapon or drone schematic rewards outside the auto-reward will prevent the bonus from being rolled.
**Guaranteed augment rewards outside the auto-reward will be overwritten by this, if the bonus is an augmentation.

===Fuel===
*T fuel & T scrap. <span style="color:grey">(low/medium/high fuel and scrap)</span>

===Missiles===
*T missiles & T scrap. <span style="color:grey">(low/medium/high missiles and scrap)</span>

===Drone parts===
*T drone parts & T scrap. <span style="color:grey">(low/medium/high drone parts and scrap)</span>

===Scrap only===
*T scrap. <span style="color:grey">(low/medium/high scrap)</span>

===Fuel only===
*T fuel. <span style="color:grey">(low/medium/high fuel)</span>

===Weapon===
*A random weapon & T scrap. <span style="color:grey">(weapon with low/medium/high scrap)</span>
**Guaranteed weapon or drone schematic rewards outside the auto-reward will overwrite this.

===Augment===
*A random augmentation & T scrap. <span style="color:grey">(augmentation with low/medium/high scrap)</span>
**Guaranteed weapon or drone schematic rewards outside the auto-reward will overwrite this.
**Guaranteed augmentation rewards outside the auto-reward will be overwritten by this.

===Drone===
*A random drone schematic & T scrap. <span style="color:grey">(drone schematic with low/medium/high scrap)</span>
**Guaranteed weapon or drone schematic rewards outside the auto-reward will overwrite this.
<!-- Reward notation not used on this Wiki:
===Item Modification (item_modify in files)===
*Modifies an item value (e.g. [[Selling missiles station|selling missiles for scrap]] will modify your missiles and scrap respectively). -->
<!-- In-game reward notation used on this Wiki in different format (similar to item rewards format)
===Crew=== -->

==Default rewards==
Most ship fights in the game yield default rewards, and are marked as [[:Category:Fights with Default Rewards|Fights with Default Rewards]]. Note that Auto-ship fights with default rewards (i.e. technically granting only medium scrap with resources) are excluded from this category and instead placed into a separate [[:Category:Auto-ship fights|category]]. Here is the list of default rewards:
{{Default rewards (generic)}}

==Default rewards: Lanius==
Most [[:Category:Fights with Default Rewards (Lanius)|fights against Lanius]] ships in [[:Category:Abandoned Sector Events|Abandoned sector events]] yield these rewards. They are similar to the default rewards listed above, with the following differences: (short summary)
* Destroying enemy ship:
** High scrap reward is possible (1 in 4).
* Killing enemy crew:
** No weapon reward; instead, a drone schematics reward is possible (1 in 8).
** Fuel reward chance is lower (1 in 8 vs 2 in 9).
{{Default rewards (Lanius)}}

==Surrender rewards==
Besides the scripted events, certain enemies can make a surrender offer when their ship's hull is low. When you accept the surrender offer, the fight ends immediately (your weapons' projectiles and asteroids will miss the enemy ship, beams will stop; all enemy projectiles, already launched, and asteroids can damage your ship and crew).

:For the actual surrender rewards, see: [[Rewards#Stuff|surrender rewards]].

:For ship-specific surrender chances and requirements, see: [[Enemy_Ships#Surrenders_and_escape_attempts|surrender offers]].

:For events with scripted surrenders, see: [[:Category:Ship surrender Events|Ship surrender Events]].

===Slug surrender rewards===
Most Slug ships do not shown their actual surrender reward offer, contrary to the usual surrender offers with the exact amount of [[Rewards#Stuff|T resources]] (and, possibly, an item), which a player can see and also reject. In case with Slug ships the actual surrender reward is shown only after the acceptance of their surrender, which cannot be rejected when the reward is revealed. The reward can be any of these:
{{Slug surrender rewards}}

==Identical rewards (events)==
{{Events with equivalent rewards}}

==Notes==
* The following rewards are in the game's files, but are not mentioned above:
** Unused Auto-rewards:
***Missiles only: T missiles.
***Drone parts only: T drone parts.
***Item: A random weapon/augmentation/drone schematic & T scrap. It is technically a random selection of the "Weapon", "Augment" and "Drone" auto-rewards.
** Item Modification: Used for specifying exact values of scrap/fuel/missiles/drone parts to be added/removed. They often appear as costs for certain choices.
***They appear in the code as <item_modify><item type="..." min="..." max="..."/></item_modify> (multiple item tags can be used for multiple resource changes)
***Auto-rewards may overwrite item modification if they happen to award the same resource, which causes some bugs. 

==See also==
* Events with item rewards:
** [[:Category:Augmentation Rewards|Augmentation rewards]]
** [[:Category:Drone Schematics Rewards|Drone Schematics rewards]]
** [[:Category:Weapon Rewards|Weapon rewards]]
* Events with crew and ship upgrade rewards:
** [[:Category:Crew Rewards|Crew rewards]]
** [[:Category:Reactor Upgrade Rewards|Reactor Upgrade rewards]]
** [[:Category:System Upgrade Rewards|System Upgrade rewards]]
* Events with other rewards:
** [[:Category:Beacon Map reveal Rewards|Beacon Map reveal rewards]]
** [[:Category:Hull Repair Rewards|Hull Repair rewards]]
** [[:Category:Rebel Fleet delay Rewards|Rebel Fleet delay rewards]]
** [[:Category:Store Opening Rewards|Store Opening rewards]]
* Events with resources rewards:
** [[:Category:Fuel Rewards|Fuel rewards]]
** [[:Category:Missiles Rewards|Missiles rewards]]
** [[:Category:Drone Parts Rewards|Drone Parts rewards]]
* Events with specific reward types:
** [[:Category:Fights with Default Rewards|Fights with Default rewards]]
** [[:Category:Fights with Default Rewards (Lanius)|Fights with Default rewards (Lanius)]]
** [[:Category:Events with Stuff rewards|Events with Stuff rewards]]
*** [[:Category:Ship surrender Events|Ship surrender Events]]

==References==
{{reflist}}
[[Category:Mechanics]]
