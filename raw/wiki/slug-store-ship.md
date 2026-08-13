<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Slug store ship
URL: https://ftl.fandom.com/wiki/Slug_store_ship
Categories: Random_Events, Unique_Events
Revision: 74286
Retrieved: 2026-08-09

---
{{Locations|Slug Controlled Nebula|Slug Home Nebula|nebula=true|LRSmap=ship+nebula|unique=true}}


''A Slug transport ship is stationed near the beacon with a military escort ship. They message you, "We have been waiting for a customer for agesss. Care to see our waresss?"''
# Decline.
#* ''"Oh well... We ssshall wait here then." You cautiously put distance between your ships before preparing to jump.''
#** Nothing happens.
# Ask to see the goods.
#* ''"Before we get ahead of ourssselves, I need to explain sssome ground ruless of our transsaction. Thesse are dangerous times, yess?"''
#** ''"Firssst... We accept no tradesss, couponss or refundss. Purchasess are final. Underssstand?"''
#**# Understood.
#**#* ''"We hold no liability for productsss damaged post ssale. We offer no insurance or customer sservice. Not a problem?"''
#**#*# Not a problem.
#**#*#* ''"Great. Let me show you our waress. It's not often I meet patient alienss, have this complimentary fuel as well."''
#**#*#** You receive {{Transaction|5|add_fuel}} and a <span style="color:limegreen">store</span> opens.
#**#*#* ''"Thank you. If you could do me one more courtesssy... please die quietly." You suddenly hear gunshots aboard the ship. He must have been stalling for time while they boarded your ship!''
#**#*#** <span style="color:red">2 slug boarders</span> beam aboard your ship and you fight a [[Slug Ships|Slug ship]] ([[Rewards#Default_rewards|default rewards]]).
#**#*#* ''"During our discussion, my man hass taken the liberty of disabling your weaponss to prevent any complications while completing our... transssaction..." You suddenly register multiple weapon locks, but your own weapons are not responding. Get out of there!''
#**#*#** <span style="color:red">1 slug boarder</span> beams aboard your ship and you fight a [[Slug Ships|Slug ship]] ([[Rewards#Default_rewards|default rewards]]) with your <span style="color:red">Weapon Control offline</span>. &nbsp;<span style="color:grey">(Weapon Control stays offline after the fight, and returns to normal after an FTL jump)</span><!-- The game code is supposed to load a "JELLY_STATUS_WEAPONS" ship, but for whatever reason it doesn't. The issue persists from at least 2015 till 2022+ game versions. File "events_slug.xml": 
	<text id="event_NEBULA_SLUG_FAKE_STORE_LIST_2_text"/>
	<ship load="JELLY_STATUS_WEAPONS" hostile="true"/>
	<boarders min="1" max="1" class="slug"/>
	<status type="limit" target="player" system="weapons" amount="0"/> -->
#**#*# Forget this.
#**#*#* ''You prepare to leave but notice noises in your ship. It looks like the merchant was trying to stall you while they hacked into your systems. You barely have time to order a red alert before a military ship flies through the clouds intent on your destruction!''
#**#*#** <span style="color:red">1 slug boarder</span> beams aboard your ship and you fight a [[Slug Ships|Slug ship]] ([[Rewards#Default_rewards|default rewards]]).
#**#*#* ''"Very well... Impatient alienss..." You prepare to jump.''
#**#*#** Nothing happens.
#**# Forget this.
#**#* ''"Fine... Not everyone appreciates good dealss..."''
#**#** Nothing happens.
#**#{{Blue Option|Slug crewmember|Our Slug senses someone aboard the ship. Investigate it.|shortreq=Slug Crew}}
#**#* ''It looks like the merchant was trying to stall you while someone teleported on board. You catch him before he could finish and he teleports away. You immediately prepare for battle.''
#**#** Fight a [[Slug Ships|Slug ship]] ([[Rewards#Default_rewards|default rewards]]). 

==Trivia==
This event is called "NEBULA_SLUG_FAKE_STORE" in the datafiles.
* Slug ship with default rewards ("JELLY") has 50% chance to surrender at 30-40% hull and has 50% chance to try to escape at 30-40% hull.
[[Category:Fights with Default Rewards]]
[[Category:Boarding risk]]
[[Category:System malfunction risk]]
[[Category:Store Opening chance]]
[[Category:Fuel reward chance]]
