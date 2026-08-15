<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-15. Source layer: do not edit. -->
Title: Game bugs
URL: https://ftl.fandom.com/wiki/Game_bugs
Categories: Content
Revision: 74618
Retrieved: 2026-08-15

---
See also the much more [https://www.reddit.com/r/ftlgame/comments/cgcna5/full_bug_list_version_3/ comprehensive list] compiled by Reddit user chewbacca77.

== How to avoid the most serious bugs ==
Most of the serious bugs in FTL are due to the save game system. For brevity, we'll refer to this as "reloading".

These bugs occur when you reload a save. In other words, they happen when you press "Continue" from the main menu. It doesn't matter whether you exited the game: any time you press "Continue", the game is reloading a save file.

If you want to be 100% certain to avoid all save-reload bugs, you must finish the run without ever exiting the game or going to the main menu. Alternatively, you could only reload saves at the start beacon of a sector, as there are no known bugs that occur there.

However, you may want more freedom to exit the game at other times. In that case, you can avoid '''almost''' all bugs by following a few basic rules:

* Always finish a fight (or any event) before exiting. Reloading during a fight will frequently change aspects of the fight, including reducing enemy hull.
* Be careful reloading at stores. Crew skills will change, and drone control will be forced to come with a Defence Drone Mark 1.
* Don't reload at "event generated" stores, as the store will vanish. It will also vanish if you leave the store interface to fight enemy boarders.

Even following these rules, it's still possible to run into bugs, but they are very rare. Specifically, you can encounter the "mixed event bug", where you reload into an outcome taken randomly from another event. For example, it's possible to reload at a store and then have one of your crew die to [[Giant alien spiders|Giant Alien Spiders]]!

Even if you never reload, it's possible for the game to crash and corrupt or delete your save file. This is very rare and might depend on other software or your computer.

To mitigate the risk of both crashes and save-reload bugs, you can use the [https://github.com/ejms116/FTL_Savegame_Manager Savegame Manager]. This keeps a copy of the save file every time it changes, meaning in the event of a catastrophe you can go back to any previous point in the run. It also allows you to "cheat" by "save scumming" if you wish.

==Confirmed game bugs==
* Reloading replaces any drone of the Drone Control system offered at the Store with the Defense Drone Mark I.
* Reloading at a store will re-roll the skills that crew in the store have.
* When an "extra" store is generated as the outcome of an event, reloading causes the store to vanish. This does not apply to the "fixed" stores that are labelled on the map.
* Additionally, when you are at one of these "extra" stores and still have enemy boarders on your ship, leaving the store interface to deal with the boarders causes the store to vanish. <!-- Though, in my experience, such stores always re-opened when the danger was over. (however, the cases of store closure occurred only several times (less than 5?) in my playthroughs, so store auto-reopening may not be guaranteed in all cases after all) -->
* Agreeing to improve the ship reactor in exchange for resources in the [[Improve reactor for supplies]] event while having maximum (25) reactor power just consumes/wastes the resources, while keeping the reactor power capped at the max level.
* Making an FTL Jump, during which a system gets destroyed due to sabotage or fire damage, allows to avoid the hull damage.
* [[Missiles_(Weapon)#Hull_Missile|Hull Missile]] does not work for any of the [[Blue_Options#Missile_Weapon|missile weapon blue options]], including the [[Rock live mine]] event.
* Under certain circumstances the enemy crew can move through your unbroken blast doors, both on your ship and their ship (when their system is hacked).
* The enemy MC can reactivate after your hack of their MC is finished, putting your Hacking on cooldown while the enemy MC disrupts your crew (see [https://ftl.fandom.com/wiki/File:Enemy_MC_activated_after_it_was_canceled_and_after_the_crew_boarding_on_the_slug_ship.png image]). Generally this SHOULD be instead: your Hacking goes on cooldown only when the enemy MC is no longer actively disrupted, which, on its part, also goes on the full cycle cooldown. [occurrence: undefined] (read the commented-out note to perform testing) <!-- I didn't extensively test the conditions for this, but this happened several times (and hacking the enemy MC is usually a very rare case in my practice) // Perhaps, this has to do with the nebula/slugs or even your crew presence on the enemy ship room with slugs in nebula altogether? --> 
* MCing enemy crew on the enemy ship may leave them in prostration after the MC control is over - for a while (until broken by damage or other factors?) they will not react to the usual tasks that the enemy crew usually reacts to, whether it is one of the enemy crewmembers or the only enemy crewmember. [occurrence: rare] <!-- Needs testing to determine if this crew state can be inflicted manually or it is too complicated to be able to replicate at any given time. -->

==Special mechanics (game bugs, glitches)==
* The [[Augmentations#Reverse Ion Field|Reverse Ion Field]] augmentation in conjunction with [[Zoltan shield|Zoltan Shield]] but without a regular shield barrier: the resisted ion projectile will pass through the Zoltan Shield and hit a system anyway.
* A [[Zoltan shield|Zoltan Shield]] will not protect a ship that lacks Shields system from the ion pulse of a [[Environmental_Hazards#Pulsar|Pulsar]] - the pulse will ignore the Zoltan Shield and ionize 2 random systems. (typical in-game example is using the [[Drone Control#Shield_Overcharger_.2B|Shield Overcharger +]] drone on [[Simo-H]])
* [[Drone Control#Anti-Personnel Drone 2|Anti-Personnel Drone]] won't move to attack a mind-controlled crew, unless another hostile crew is present in the room.
* Enemy's [[Drone_Control#Ion_Intruder|Ion Intruder]] won't stun its temporarily hostile crew (affected by Mind Control) on player's ship.
* A (single) shield bubble can absorb both laser and ion projectile, if they hit at exactly/almost exactly the same time. (see: [https://youtu.be/4R7_QgaT5ms video], [https://ftl.fandom.com/wiki/File:Shield_simultaneously_takes_shield_layer_damage_and_the_shield_system_is_ionized_(1st_enemy_weapon_volley).png image])
* [[Drone Control#Defensive Drones|Defensive Drones]] (Mark I, Mark II) targeting glitch. When a projectile is coming to the far right side of certain player ships, the drone's laser won't be able to intercept it, hence leaving these rooms vulnerable. Same glitch applies to the Anti-Combat Drone. (see: [https://www.reddit.com/r/ftlgame/comments/4jr8yg/visualising_the_drone_targeting_glitch/ Visualising the Drone Targeting Glitch] ([[:Template:Drone_targeting_glitch_visuals|all ships images on one page]]))
* De-powering [[Mind Control]], quickly or during a pause, after setting a crew target instantly puts the system on cooldown without applying the beneficial effect. (see: [https://youtu.be/pd1L3cuyFVA MC depower activates cool down])
* When an Auto-ship hacks your [[Mind Control]], the hack has no effect. ([https://ftl.fandom.com/wiki/File:Mind_Control_hack_doesn%27t_function_(1).png case 1], [https://ftl.fandom.com/wiki/File:Mind_Control_hack_doesn%27t_function_(2).png case 2]).
* Ionising an active [[Hacking]] system will reset its cooldown to the amount of ion damage applied, instead of 20 seconds.
* When one of your crew is mind-controlled, hacking the enemy's [[Crew Teleporter|Teleporter]] won't necessarily send their boarders back to the enemy ship. Only boarders that enter the same room as your mind-controlled crew will be returned ([https://clips.twitch.tv/AggressiveDifferentHawkPhilosoraptor-lDX58AjEiG637q-P video clip]).

<br />
Game bugs confirmed on game versions: 1.6.9, 1.6.12, 1.6.13b, 1.6.14.
[[Category:Content]]
