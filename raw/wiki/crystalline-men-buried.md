<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Crystalline men buried
URL: https://ftl.fandom.com/wiki/Crystalline_men_buried
Categories: Random_Events, Unique_Events
Revision: 74724
Retrieved: 2026-08-09

---
{{Locations|Hidden Crystal Worlds|LRSmap=ship|unique=true}}


''A large Crystalline ship is floating in space here. They hail: "Aliens?! How curious. We request your aid. We have men buried on a nearby planet and we must dig them out."''
#Send a crewmember to help.
#*''You do as you're asked and send a crewmember down to the planet to assist. They discover a massive Crystal excavation operation and it quickly becomes clear this is a task that will take days, not hours.''
#*#Leave your crew member behind.
#*#*''You're committed to both saving the Federation and upholding the principles it worked to maintain. Your crewmember will remain and make good on the promise - you still have a galaxy to save. They give you some supplies for your trouble.''
#*#**You <span style="color:red">lose</span> a <span style="color:red">crewmember</span> and receive {{tooltip|medium|2-4 fuel}} [[Rewards#Fuel|fuel and scrap]].
#*#***<span style="color:#70b8ff">(Clone Bay)</span>: <span style="color:red">no effect</span>. <!-- there is no text shown in-game for no effect of the Clone Bay -->
#*#Pull your guy out.
#*#*''The Crystalline captain contacts you urgently: "What is the meaning of this?! Had you no wish to aid us you might simply have declined, but THIS... is an insult!" His turns his massive ship on yours and you prepare to fight for your life.''
#*#**Fight a [[Enemy_Ships#Crystal_ships|Crystal ship]] ([[Rewards#Default_rewards|default rewards]]). <ref name="Enemy ship (CRYSTAL_SHIP_NO_SURRENDER)">{{SurrenderEscape(alt)|no|CRYSTAL_SHIP_NO_SURRENDER|events_ships.xml}}</ref>
#*#Wait.
#*#*''You've made a commitment, and that still means something. You wait one jump cycle and then inquire with the Crystalline captain about the status of the operation. "We respect your strength. The operation will take one more cycle."''
#*#**Rebel Fleet <span style="color:red">pursuit</span> is <span style="color:red">doubled</span> for <span style="color:red">1 jump</span>.
#*#**#Leave your crew member behind.
#*#**#*''You're committed to both saving the Federation and upholding the principles it worked to maintain. Your crewmember will remain and make good on the promise - you still have a galaxy to save. They give you some supplies for your trouble.''
#*#**#**You <span style="color:red">lose</span> a <span style="color:red">crewmember</span> and receive {{tooltip|high|3-6 fuel}} [[Rewards#Fuel|fuel and scrap]].
#*#**#***<span style="color:#70b8ff">(Clone Bay)</span>: <span style="color:red">no effect</span>. <!-- there is no text shown in-game for no effect of the Clone Bay -->
#*#**#Pull your guy out.
#*#**#*''The Crystalline captain contacts you urgently: "What is the meaning of this?! Had you no wish to aid us you might simply have declined, but THIS... is an insult!" His turns his massive ship on yours and you prepare to fight for your life.''
#*#**#**Fight a [[Enemy_Ships#Crystal_ships|Crystal ship]] ([[Rewards#Default_rewards|default rewards]]). <ref name="Enemy ship (CRYSTAL_SHIP_NO_SURRENDER)" />
#*#**#Wait.
#*#**#*''Another cycle passes while the Rebel fleet draws ever nearer. You contact the captain again. "Alien Captain, your knowledge of our customs has most impressed us. Your crewmember is on their way back to you now, along with a token of our respect."''
#*#**#**You receive [[Crystal_(Weapons)#Heavy_Crystal_Mark_II|<span style="color:limegreen">Heavy Crystal Mark II</span>]], and Rebel Fleet <span style="color:red">pursuit</span> is <span style="color:red">doubled</span> for <span style="color:red">1 jump</span>.
#Refuse.
#*''"We understand. You rely on machines for so much. Yours is a soft and weak species - we would hardly even have noticed your presence. Fly well."''
#**Nothing happens.

==Notes==
This event is called "CRYSTAL_HELP_DIG" in the datafiles.

* In the files, the outcome after waiting 2 times includes an augmentation with high scrap. However, the free weapon prevents them from being awarded.
** In the code, the <weapon> tag that grants a free weapon, and the <drone> tag that grants a free drone schematic, will block "weapon", "drone" and "augment" auto-rewards in the same event block. This is also why "standard" and "stuff" auto-rewards never award bonuses when they occur with free weapons or drone schematics, since the bonus is actually randomly selected from 1 of those 3 auto-rewards.

===Reference notes===
<references/>
[[Category:Fights with Default Rewards]]
[[Category:Rebel Fleet advancement risk]]
[[Category:Crew loss risk]]
[[Category:Clone Bay failed revival]]
[[Category:Weapon reward opportunity]]
[[Category:Fuel reward opportunity]]
