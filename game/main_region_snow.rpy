screen place_ursinia_glade():
    zorder 10 tag place

    imagebutton:
        xalign 0.99
        yalign 0.69
        idle "explore_idle"
        hover "explore_hover"
        action Return("Explore")
    imagebutton:
        xalign 0.33
        yalign 0.98
        idle "bedroom_arrow"
        hover "bedroom_arrow_hover"
        style "footstep_button"
        action Return("To Bandit")
    if frosted_taiga.discovered:
        imagebutton:
            xalign 0.33
            yalign 0.51
            idle "sparklinglagoon_arrow"
            hover "sparklinglagoon_arrow_hover"
            style "footstep_button"
            action Return("To Taiga")

label main_ursinia_glade:
    $ current_location = ursinia_glade
    $ renpy.music.play(mForest, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ wilderness = True
    $ timenow.minute += 12
    $ timenow.passTime()
    if isNight():
        scene ursiniaglade
    else:
        scene ursiniaglade
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_ursinia_glade
    if _return == "Explore":
        jump ursinia_glade_loop
    if _return == "To Bandit":
        jump main_bandits_hideout
    if _return == "To Taiga":
        jump main_frosted_taiga
    jump main_ursinia_glade


label ursinia_glade_loop:
    hide screen menu_buttons
    if isNight():
        scene ursiniaglade
    else:
        scene ursiniaglade
    $ rnd = renpy.random.random()
    if rnd < 0.2:
        if rnd < 0.08 and not frosted_taiga.discovered:
            "You have wandered around the forest opening for a while, but there doesn't seem to be anything noticeable in particular, until you wander deeper into the pine forest."
            "Suddenly you notice a patch of white in the front, covering most of the trees as the air begins to freeze, slowly the small patch becomes a larger one until everything around you is enveloped in snow."
            "You take out your map and mark the spot. This must be the frosted taiga."
            $ frosted_taiga.discovered = True
            jump main_frosted_taiga
        else:
            "You search around the area for a while, but there seem to be nothing worth noting nearby."
    elif rnd < 0.3:

        $ addItem("Chamomile", inventory, 1)
        $ item_number = LookForItemNumber("Chamomile", inventory)
        if item_number == 1:
            "Around the glade, you wander and pick up a certain plant, it was a chamomile flower."
        else:
            "Around the glade, you wander and pick up a certain plant, it was a chamomile flower. You now have [item_number] Chamomile."
    elif rnd < 0.4 and linenbraiesrecipe not in discoveredrecipe:
        "Near the edge of the glade, you find an old satchel tucked beneath a bed of ursinia flowers."
        "Inside are neatly folded tailoring notes, written for making warm clothes from lighter cloth."
        if linenrecipe not in discoveredrecipe:
            "One page explains how to weave plain linen from softer fibers, so you copy the method into your journal first."
            $ discoveredrecipe.append(linenrecipe)
        "Another page details a practical pair of linen braies lined for travel in colder weather."
        $ discoveredrecipe.append(linenbraiesrecipe)
        msg "You have learnt the recipe for Linen Braies."
    elif rnd < 0.5:
        if pc.level < 12:
            "You search around the area, there seem to be something ahead of you, but it seems like your level is too low to notice it yet."
        else:
            "You walk around the meadow, and suddenly, you notice a small pamphlet lying between the grass."
            if LookForItem("Magic Show Pamphlet", inventory):
                "It looks to be the same flyer for the travelling carnival, so you quickly put it away."
            else:
                "Picking it up, it looks to be a flyer for a travelling carnival, putting it in the back, perhaps you should check it out sometime..."
                $ addItem("Magic Show Pamphlet", inventory, 1)
    else:
        "You search around the area for a while, but there seem to be nothing worth noting nearby."
    jump main_ursinia_glade

screen place_frosted_taiga():
    zorder 10 tag place

    imagebutton:
        xalign 0.99
        yalign 0.69
        idle "explore_idle"
        hover "explore_hover"
        action Return("Explore")
    imagebutton:
        xalign 0.63
        yalign 0.91
        idle "kingspawn_arrow"
        hover "kingspawn_arrow_hover"
        style "footstep_button"
        action Return("To Glade")

    if avalanche_site.discovered:
        imagebutton:
            xalign 0.13
            yalign 0.47
            idle "ancienttree_arrow"
            hover "ancienttree_arrow_hover"
            style "footstep_button"
            action Return("To Avalanche")
    if otsovaara.discovered:
        imagebutton:
            xalign 0.57
            yalign 0.18
            idle "sparklinglagoon_arrow"
            hover "sparklinglagoon_arrow_hover"
            style "footstep_button"
            action Return("To Ascent")

    if snowbound_summit_place.discovered or quest44.status != False:
        imagebutton:
            xalign 0.93
            yalign 0.57
            idle "dungeon1_arrow"
            hover "dungeon1_arrow_hover"
            style "footstep_button"
            action Return("To Summit")

    if daggi_location == "frosted_taiga":
        imagebutton:
            xalign 0.59
            yalign 0.57
            idle Transform("daggi_idle", xzoom = -1)
            hover Transform("daggi_hover", xzoom = -1)
            action Return("Daggi")

label Bear_Tribe_Schedule:
    if daggi_accompany:
        $ daggi_location = "No"
    elif quest47.status != False and quest47.status != True:
        $ daggi_location = "otsovaara_council_hall"
    elif isMidnight():
        $ daggi_location = "No"
    elif isNight() or timenow.hour >= 15:
        $ daggi_location = "otsovaara_council_hall"
    else:
        $ daggi_location = "frosted_taiga"

    return

label main_frosted_taiga:
    $ current_location = frosted_taiga
    $ renpy.music.play(mForest, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ wilderness = True
    $ current_map = otsovaara_map
    $ timenow.minute += 12
    $ timenow.passTime()
    call Bear_Tribe_Schedule from _call_Bear_Tribe_Schedule
    if isNight():
        scene frostedtaiga
    else:
        scene frostedtaiga
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_frosted_taiga
    if _return == "Explore":
        jump frosted_taiga_loop
    if _return == "To Glade":
        jump main_ursinia_glade
    if _return == "To Avalanche":
        jump main_avalanche_site
    if _return == "To Ascent":
        jump main_clawridge_ascent
    if _return == "To Summit":
        $ snowbound_summit_place.discovered = True
        jump Snowbound_Summit_Enter
    if _return == "Daggi":
        jump Daggi_Dialogue
    jump main_frosted_taiga

label frosted_taiga_loop:
    hide screen menu_buttons
    if isNight():
        scene frostedtaiga
    else:
        scene frostedtaiga
    $ rnd = renpy.random.random()
    if rnd < 0.2:
        if rnd < 0.08 and not otsovaara.discovered:
            $ otsovaara.discovered = True
            jump Otsovaara_Introduction
        elif rnd < 0.04 and not snowbound_summit_place.discovered and not quest44.status == False:
            "You get lost in the snow for a while, but you eventually find a new path leading to a small mountain."
            "Though, it looks to be quite dangerous..."
            $ snowbound_summit_place.discovered = True
            jump main_frosted_taiga
        "You search around the area for a while, but there seem to be nothing worth noting nearby."

    elif rnd < 0.275:
        $ addItem("Spearmint", inventory, 1)
        $ item_number = LookForItemNumber("Spearmint", inventory)
        if item_number == 1:
            "Around the snow forest, you wander and pick up a certain plant, it was a spearmint."
        else:
            "Around the snow forest, you wander and pick up a certain plant, it was a spearmint. You now have [item_number] of them."
    elif rnd < 0.35:
        $ addItem("Snow Berry", inventory, 1)
        $ item_number = LookForItemNumber("Snow Berry", inventory)
        if item_number == 1:
            "Around the snow forest, you wander and pick up a certain plant, it was a snow berry."
        else:
            "Around the snow forest, you wander and pick up a certain plant, it was a snow berry. You now have [item_number] of them."
    elif rnd < 0.55 and otsovaara.discovered == True:
        call Bear_Guard_Interaction from _call_Bear_Guard_Interaction
    elif rnd < 0.75 and avalanche_site.discovered == False and bearguard_dialogue.get("Avalanche", False) == True:
        $ avalanche_site.discovered = True
        "With the direction given by the bear guards, you notice the snow-buried path along the taiga forest."
        "Following the path, it takes a long time until you finally make your way into the snowland."
        "The air is freezing cold, and the snow is so deep that you can barely walk through it, but you can see a huge pile of snow in the distance, and the trail leads right to it."
        "As you get closer, you can see the remnants of a collapsed mountain, the snow is piled up in a huge heap, and the air is filled with the scent of crushed pine and cold stone."
        jump main_avalanche_site
    else:
        "You search around the area for a while, but there seem to be nothing worth noting nearby."
    jump main_frosted_taiga

screen place_clawridge_ascent():
    zorder 10 tag place

    imagebutton:
        xalign 0.99
        yalign 0.69
        idle "explore_idle"
        hover "explore_hover"
        action Return("Explore")
    imagebutton:
        xalign 0.25
        yalign 0.95
        idle "kingspawn_arrow"
        hover "kingspawn_arrow_hover"
        style "footstep_button"
        action Return("To Taiga")

    if otsovaara.discovered:
        imagebutton:
            xalign 0.86
            yalign 0.32
            idle "sparklinglagoon_arrow"
            hover "sparklinglagoon_arrow_hover"
            style "footstep_button"
            action Return("To Otsovaara")

    if quest47.status != False:
        imagebutton:
            xalign 0.73
            yalign 0.91
            idle "dungeon1_arrow"
            hover "dungeon1_arrow_hover"
            style "footstep_button"
            action Return("To Cave")

label main_clawridge_ascent:
    $ current_location = clawridge_ascent
    $ renpy.music.play(mForest, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ wilderness = True
    $ current_map = otsovaara_map
    $ timenow.minute += 12
    $ timenow.passTime()
    if isNight():
        scene clawridge_ascent
    else:
        scene clawridge_ascent
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_clawridge_ascent
    if _return == "Explore":
        jump clawridge_ascent_loop
    if _return == "To Taiga":
        jump main_frosted_taiga
    if _return == "To Cave":
        jump Chilly_Ice_Cave
    if _return == "To Otsovaara":
        jump main_otsovaara
    jump main_clawridge_ascent

label clawridge_ascent_loop:
    hide screen menu_buttons
    if isNight():
        scene clawridge_ascent
    else:
        scene clawridge_ascent
    $ rnd = renpy.random.random()

    if rnd < 0.2:
        $ addItem("Snow Berry", inventory, 1)
        $ item_number = LookForItemNumber("Snow Berry", inventory)
        if item_number == 1:
            "Along the ascent, you wander and pick up a certain plant, it was a snow berry."
        else:
            "Along the ascent, you wander and pick up a certain plant, it was a snow berry. You now have [item_number] of them."
    elif rnd < 0.4 and otsovaara.discovered == True:
        call Bear_Guard_Interaction from _call_Bear_Guard_Interaction_1
    else:
        "You search around the area for a while, but there seem to be nothing worth noting nearby."
    jump main_clawridge_ascent

screen place_skullstrewn_pass():
    zorder 10 tag place

    imagebutton:
        xalign 0.99
        yalign 0.69
        idle "explore_idle"
        hover "explore_hover"
        action Return("Explore")
    imagebutton:
        xalign 0.63
        yalign 0.91
        idle "kingspawn_arrow"
        hover "kingspawn_arrow_hover"
        style "footstep_button"
        action Return("To Avalanche")

screen place_avalanche_site():
    zorder 10 tag place

    imagebutton:
        xalign 0.99
        yalign 0.69
        idle "explore_idle"
        hover "explore_hover"
        action Return("Explore")
    imagebutton:
        xalign 0.63
        yalign 0.91
        idle "kingspawn_arrow"
        hover "kingspawn_arrow_hover"
        style "footstep_button"
        action Return("To Taiga")
    imagebutton:
        xalign 0.89
        yalign 0.84
        idle "sparklinglagoon_arrow"
        hover "sparklinglagoon_arrow_hover"
        style "footstep_button"
        action Return("To Pass")

label main_avalanche_site:
    $ renpy.music.play(mForest, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ wilderness = True
    $ current_location = avalanche_site
    $ current_map = otsovaara_map
    $ timenow.minute += 24
    $ timenow.passTime()
    scene avalanche_site
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_avalanche_site
    if _return == "Explore":
        jump avalanche_site_loop
    if _return == "To Taiga":
        jump main_frosted_taiga
    if _return == "To Pass":
        jump main_skullstrewn_pass

    jump main_avalanche_site

label avalanche_site_loop:
    hide screen menu_buttons
    scene avalanche_site
    $ rnd = renpy.random.random()

    if rnd < 0.2 and not skullstrewn_pass.discovered:
        "You follow the trail leading away from the avalanche, the path is barely visible under the snow."
        scene black with dissolve
        "As you walk deeper into the mountains, you notice the air getting colder and colder, and the sky gets darker and darker."
        "Eventually, you find yourself in a mountain pass, the ground is covered with snow and ice, and the wind is howling around you."
        "In a distant nowhere, you notice a structure over the mountains. It looks like it's been abandoned for a long time, and around the area, a towering figure who is barely visible from where you stand."
        $ skullstrewn_pass.discovered = True
        jump main_skullstrewn_pass
    else:
        "You search around the area for a while, but there seem to be nothing worth noting nearby."
    jump main_avalanche_site

label main_skullstrewn_pass:
    $ renpy.music.play(mForest, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ wilderness = True
    $ current_location = skullstrewn_pass
    $ current_map = otsovaara_map
    $ timenow.minute += 24
    $ timenow.passTime()
    scene skullstrewn_pass
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_skullstrewn_pass
    if _return == "Explore":
        jump skullstrewn_pass_loop
    if _return == "To Avalanche":
        jump main_avalanche_site

    jump main_skullstrewn_pass

label skullstrewn_pass_loop:
    hide screen menu_buttons
    scene skullstrewn_pass
    $ rnd = renpy.random.random()
    if rnd < 0.2:
        "As you explore the pass, the ground trembles beneath your feet suddenly."
        "A deep, guttural rumble echoes from above, like ancient stone grinding against itself."
        "In the middle of the pass stands a towering figure. Dark purple skin stretched over powerful muscles, glowing with faint, pulsing blue runes."
        "A massive deer skull mask hides his face, jagged antlers scraping the low-hanging clouds."
        "Only a tattered loincloth covers his waist, doing little to hide the immense bulge beneath it."
        "The Jotunn slowly turns his head toward you with curiosity. Icy blue light flares within the empty sockets of the skull."
        "For a moment, the world seems to freeze."
        menu:
            "What do you do?"
            "Prepare for battle":
                jump jotunn_battle
            "Try to sneak away":

                if renpy.random.random() < 0.1+pc.agi*0.05:
                    "You slowly back away into the swirling snow, holding your breath..."
                    "The giant doesn't seem to notice. You manage to slip away."
                else:
                    "Before you can take three steps, the Jotunn slams his massive fist into the ground."
                    "A wall of ice erupts in front of you, cutting off any retreat."
                    e "F-fuck..."
                    jump jotunn_battle
    else:
        "You search around the area for a while, but there seem to be nothing worth noting nearby."
    jump main_skullstrewn_pass


screen place_otsovaara():
    zorder 10 tag place


    imagebutton:
        xalign 0.53
        yalign 0.98
        idle "bedroom_arrow"
        hover "bedroom_arrow_hover"
        style "footstep_button"
        action Return("To Ascent")

    imagebutton:
        xalign 0.33
        yalign 0.58
        idle "kingspawn_arrow"
        hover "kingspawn_arrow_hover"
        style "footstep_button"
        action Return("To Abyss")

    imagebutton:
        xalign 0.73
        yalign 0.48
        idle "sparklinglagoon_arrow"
        hover "sparklinglagoon_arrow_hover"
        style "footstep_button"
        action Return("To Station")

    imagebutton:
        xalign 0.99
        yalign 0.69
        idle "explore_idle"
        hover "explore_hover"
        action Return("Explore")

label main_otsovaara:
    $ current_location = otsovaara
    $ current_map = otsovaara_map
    $ renpy.music.play(mBear1, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ timenow.minute += 12
    $ timenow.passTime()
    if isNight():
        scene otsovaara01
    else:
        scene otsovaara01
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_otsovaara

    if _return == "To Abyss":
        jump main_otsovaara_abyss
    if _return == "To Ascent":
        jump main_clawridge_ascent
    if _return == "To Station":
        jump main_otsovaara_station
    jump main_otsovaara

screen place_otsovaara_abyss():
    zorder 10 tag place


    imagebutton:
        xalign 0.83
        yalign 0.94
        idle "sparklinglagoon_arrow"
        hover "sparklinglagoon_arrow_hover"
        style "footstep_button"
        action Return("To Entrance")

    imagebutton:
        xalign 0.127
        yalign 0.492
        idle "finnkels_gaze_door_idle"
        hover "finnkels_gaze_door_hover"
        action Return("To Gaze")

    imagebutton:
        xalign 0.3385
        yalign 0.509
        idle "otsovaara_abyss_totem"
        hover "otsovaara_abyss_totem_hover"
        action Return("Totem")

    imagebutton:
        xalign 0.5285
        yalign 0.5682
        idle "otsovaara_abyss_coal"
        hover "otsovaara_abyss_coal_hover"
        action Return("Coal")

    imagebutton:
        xalign 0.6673
        yalign 0.4805
        idle "otsovaara_abyss_furnace"
        hover "otsovaara_abyss_furnace_hover"
        action Return("Furnace")

label main_otsovaara_abyss:
    $ current_location = otsovaara
    $ renpy.music.play(mBear1, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ timenow.minute += 12
    $ timenow.passTime()
    if isNight():
        scene otsovaara_abyss
    else:
        scene otsovaara_abyss
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_otsovaara_abyss

    if _return == "To Entrance":
        jump main_otsovaara
    if _return == "Furnace":
        "A building with chimneys that stretches far upwards, it is burning bright red, you can reckon that they are used to keep the tribe warm."
    if _return == "Coal":
        "Some coals stored on a few carts near the furnace. They are carefully mined from the cave ahead, and used as fuels for the furnace."
        if coal_day < timenow.day:
            "You pick up a piece of extra coal from the ground, it might be useful later."
            $ addItem("Coal", inventory, 1)
            $ coal_day = timenow.day
    if _return == "Totem":
        "An old traditional totem erects from beneath the ice, there probably aren't a lot of them left in the bear tribe right now."
    if _return == "To Gaze":
        jump main_finnkels_gaze

    jump main_otsovaara_abyss

screen place_otsovaara_station():
    zorder 10 tag place


    imagebutton:
        xalign 0.29
        yalign 0.94
        idle "kingspawn_arrow"
        hover "kingspawn_arrow_hover"
        style "footstep_button"
        action Return("To Entrance")

    imagebutton:
        xalign 0.361
        yalign 0.701
        idle "otsovaara_council_hall_door_idle"
        hover "otsovaara_council_hall_door_hover"
        style "footstep_button"
        action Return("To Hall")

label main_otsovaara_station:
    $ current_location = otsovaara
    $ renpy.music.play(mBear1, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ timenow.minute += 12
    $ timenow.passTime()
    if isNight():
        scene otsovaara_station
    else:
        scene otsovaara_station
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_otsovaara_station

    if _return == "To Entrance":
        jump main_otsovaara
    if _return == "To Hall":
        jump main_otsovaara_council_hall

    jump main_otsovaara_station

screen place_otsovaara_council_hall():
    zorder 10 tag place


    imagebutton:
        xalign 0.53
        yalign 0.98
        idle "bedroom_arrow"
        hover "bedroom_arrow_hover"
        style "footstep_button"
        action Return("To Station")

    imagebutton:
        xalign 0.565
        yalign 0.397
        idle "kaurhu_idle"
        hover "kaurhu_hover"
        action Return("Kaurhu")

    if daggi_location == "otsovaara_council_hall":
        imagebutton:
            xalign 0.26
            yalign 0.56
            idle "daggi_idle"
            hover "daggi_hover"
            action Return("Daggi")


label main_otsovaara_council_hall:
    $ current_location = otsovaara
    $ renpy.music.play(mBear2, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ timenow.minute += 12
    $ timenow.passTime()
    call Bear_Tribe_Schedule from _call_Bear_Tribe_Schedule_1
    if isNight():
        scene otsovaara_throne
    else:
        scene otsovaara_throne
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_otsovaara_council_hall

    if _return == "To Station":
        jump main_otsovaara_station
    if _return == "Kaurhu":
        jump Kaurhu_Dialogue
    if _return == "Daggi":
        jump Daggi_Dialogue
    jump main_otsovaara_council_hall

screen place_finnkels_gaze():
    zorder 10 tag place


    imagebutton:
        xalign 0.33
        yalign 0.98
        idle "kingspawn_arrow"
        hover "kingspawn_arrow_hover"
        style "footstep_button"
        action Return("To Abyss")

    imagebutton:
        xalign 0.25
        yalign 0.56
        idle "methis_idle"
        hover "methis_hover"
        action Return("Methis")

    imagebutton:
        xalign 0.4579
        yalign 0.00
        idle "finnkels_gaze_deer"
        hover "finnkels_gaze_deer_hover"
        action Return("Deer")

    imagebutton:
        xalign 0.00
        yalign 0.456
        idle "finnkels_gaze_mask"
        hover "finnkels_gaze_mask_hover"
        action Return("Mask")

    imagebutton:
        xalign 0.9505
        yalign 0.4073
        idle "finnkels_gaze_mannequins"
        hover "finnkels_gaze_mannequins_hover"
        action Return("Mannequins")

    imagebutton:
        xalign 0.486
        yalign 0.2495
        idle "finnkels_gaze_jotunn"
        hover "finnkels_gaze_jotunn_hover"
        action Return("Jotunn")

    imagebutton:
        xalign 0.628
        yalign 0.2738
        idle "finnkels_gaze_ice"
        hover "finnkels_gaze_ice_hover"
        action Return("Ice")

label main_finnkels_gaze:
    $ current_location = otsovaara
    $ renpy.music.play(mBear2, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ timenow.minute += 12
    $ timenow.passTime()
    if isNight():
        scene finnkels_gaze
    else:
        scene finnkels_gaze
    with dissolve

    if methis_tut == 1:
        $ methis_tut = 2
        jump Methis_Introduction
    show screen menu_buttons
    window hide
    call screen place_finnkels_gaze

    if _return == "Deer":
        show methis normal with dissolve
        "On the wall, a large deer head is mounted, its eyes seem to follow you wherever you go."
        e "That deer head on the wall, it's a bit creepy, don't you think?"
        m "Ah! Don't you worry your arse off, it's not a real deer. It's just a decoration."
        e "But why deers? Why not something else?"
        m "We just like the look of a deer in the forest, it's a good luck charm. Plus, it's a good conversation starter, don't you think?"
        e "Well, considering I did ask you about it..."
    if _return == "Mask":
        show methis normal with dissolve
        "A white mask in frame is hanging on the wall, it is painted with various colors and has a pair of horns on top."
        e "Methis, what's with this mask on the wall?"
        m "That's, that's not from around here. We found them around the plains and the mountains. I thought you'd know about that?"
        e "I don't, but it looks interesting. What's it for?"
        m "Old rituals from the horned fellows, they used to wear these masks to communicate with the spirits of the forest."
        m "I am not familiar with the fables and tales of those grass-eaters, but I still find these rituals... interesting."
    if _return == "Ice":
        show methis normal with dissolve
        "A row of ice chunks are placed on the shelves. They are clear and cold, and they seem to be glowing even in the dark."
        e "What are these ice chunks for?"
        m "Oh, those are just some ice chunks we've collected from the frozen lake. They've been frozen for so long that you can smell the ancestors' scent in there."
        e "Well, for one I might not want to imagine what a thousands years old scent smells like."
        m "Oh, don't worry, I won't be pressing your little snout against these ice chunks anytime soon."
        e "Uh... soon?"
        m "Just kidding, don't worry about it."
    if _return == "Mannequins":
        show methis normal with dissolve
        "You peer at the two mannequins standing in front of the shop, one is wearing an iron armor while the other is barely clothed."
        e "Methis, what's with these mannequins?"
        m "Did they scare you? They're just here to show off some of the wares we have in the shop."
        e "Uh huh..."
        "Methis stares at you, waiting for you to say something."
        m "Ah, sometimes they just couldn't stand still, they're a bit... lively, especially Kivy over there."
        m "Say, I reckon the armors would look good on you, don't you think?"
        "The shopkeeper grins, but you're not sure if he's joking or not."
        e "I'm not sure if I want to be wearing heavy armor in the middle of the snow."
        m "My assistants wouldn't look half as good in them as you would, heh."
    if _return == "Jotunn":
        show methis normal with dissolve
        "A purple sculpture lies on the shop's counter, it is of a tall antlered creature with a skull head that kneels on both knees."
        e "Methis, what's this sculpture you have on your counter?"
        m "Oh, that's Jotunn, he's the kind of older than the realm itself."
        m "Probably the last living specimen of the old ancestors we have on this realm."
        e "Specimen?"
        "Methis nods."
        m "He hides around that tower in the far north, rarely coming down to the tribes."
        m "But don't fret my dear, you can easily spot him, just look for the blue glowstick in the distance..."
        e "A glowstick?"
        m "That's what we call that gigantic meaty pole that hangs between his legs, bright like a beacon in the dark."
    if _return == "Methis":
        jump Methis_Dialogue
    if _return == "To Abyss":
        jump main_otsovaara_abyss

    jump main_finnkels_gaze

label Bear_Guard_Interaction:

    if bearguard.win >= 1 and quest47.status == False and otsovaara.discovered == True:
        call Bear_Guard_Cave_Discovery from _call_Bear_Guard_Cave_Discovery
        return

    "As you wander around the glade, you notice a light brown figure troding through the snow, he's holding a harpoon."
    if bearguard.win >= 3:
        "You recognize him as the bear guard that patrols the area, he sees you as well, but he's not raising any weapons."
        bearGuard "Outsider! You're back again, huh?"
        e "I hope our last encounter didn't leave a bad impression on you. I'm not trying to cause any trouble."
        bearGuard "You beat us fair and square, but we're not letting you off the hook that easily."
        menu:
            bearGuard "A spar will do, outsider. Let's see if you're still as good as last time."
            "Fight with the Guard":
                e "How about a little spar?"
                "You raise your weapon, the bear guard quickly catches onto it and raise his harpoon forward."
                bearGuard "You're not getting away this time, outsider!"
                jump bearguard_battle
            "Gossip with the Guard":

                "You lower your weapon, the bear guard seems to be more relaxed now."
                e "See, I'm not here to cause any trouble. I just want to talk."
                bearGuard "Fine, but make it quick, outsider."
                e "So, what's up?"
                if renpy.random.random() < 0.2:
                    bearGuard "Just patrolling the area, making sure no outsider's causing any trouble around here."
                    bearGuard "You're lucky I didn't catch you last time, outsider."
                    e "Well, the chief didn't seem to mind me being around here."
                    bearGuard "It's because you're a courier, but don't think you can just wander around here without any consequences."
                    e "I thought you were about to attack me like the last few times."
                    if herd_dead:
                        bearGuard "Look, you don't seem to be a bad fighter, neither a bad person. We had no wish to shed any blood after the incident with Herd."
                    else:
                        bearGuard "We weren't trusting you after the stunts you pulled with Herd. But you've proven yourself to be a worthy fighter."
                    e "Thanks, I guess."
                elif renpy.random.random() < 0.4:
                    $ bearguard_retirement = True
                    bearGuard "Patrolling, just like what our commander told us to do."
                    "The bear guard looks around the area, he seems to be on high alert."
                    e "Is there something wrong?"
                    bearGuard "Commander Daggi, all due respect, he only got to be the new commander because of his father, not his ability."
                    e "H-his father? Who's his father?"
                    bearGuard "Wait, you don't know? He's the son of chief Kaurhu."
                    bearGuard "Please tell no one that I told you about this, I don't want to be in trouble with chief."
                    e "I won't, I promise, but what's the problem with him being the son of the chief?"
                    bearGuard "He's been trying to prove himself to chief, but we always ended up being the one babysitting the little cub."
                    bearGuard "He's not a bad leader, but he's not a good one either. He doesn't have the confidence to spearhead the guards. He's just... there."
                    e "I see... Were there someone else who could've been a better leader?"
                    bearGuard "Bedwyr, he's the best fighter we have in the tribe. But..."
                    bearGuard "I believe I've said enough already."
                elif renpy.random.random() < 0.6:
                    bearGuard "If you enter our tribe, make sure you follow the rules, outsider."
                    bearGuard "Once you land in prison, there's no way we're letting you out."
                    e "What's the rules? I thought I was allowed to wander around here."
                    "The guard chuckles, before counting on his claws."
                    bearGuard "First rule, be respectful to the tribe and our chief."
                    bearGuard "Second rule, dress appropriately, showing off your cock to anyone will earn you a place in prison. This is an extension to the first rule."
                    if isNaked():
                        e "Am I breaking the second rule?"
                        bearGuard "As a matter of fact. Yes, and you're gonna pray to Ookko I'm not taking your ass in prison."
                    bearGuard "Third rule, no bear puns allowed. This... also an extension to the first rule."
                    "You can barely hold your desire to defy the rules."
                    bearGuard "Fourth rule, do not venture onto the mountain without a guide, the mountains are dangerously cold, especially for a thin-furred like you."
                    bearGuard "Fifth rule, do not disturb the old familiars. They're the spirits of our ancestors, they're not to be trifled with."
                    bearGuard "Sixth rul... you know what, I think you get the point."
                    e "What's the sixth rule?"
                    bearGuard "N-nothing. Just don't cause any trouble around here, and you'll be fine."
                    "The guard nervously shoos you away, before heading a seperate direction."
                elif renpy.random.random() < 0.8 and bearguard_dialogue.get("Avalanche", False) == False:
                    bearGuard "Have you seen what that avalanche did to the mountains? It's a miracle that we weren't all buried alive inside that little slit in the ice."
                    e "I hadn't... was it the same avalanche Daggi were talking about? Where is it?"
                    bearGuard "It's closed now, we're still trying to recover anything we can find in the mountain, we've cleared the foothill just around this forest, but not anywhere higher."
                    e "Can I take a look there?"
                    bearGuard "S-sure? It's close by a short cliff, and it's not like there're anything of value lying around there, just a huge pile of snow."
                    bearGuard "The only trail it leads to are the observatory, and don't say we didn't warn you, courier. It's guarded by the Jotunn, a giant monster with his glowstick hanging between his legs."
                    e "A-alright, I'll just look at the snow..."
                    bearGuard "Whatever, I'm not liable to your safety just to be sure. You'll find a few road signs toward the north from here, following it onward there'll be a trail that extends all the way to the observatory."
                    "You nod, memorizing the path the guard just described. Perhaps you can discover the site now."
                    $ bearguard_dialogue["Avalanche"] = True
                else:
                    bearGuard "Protecting the tribe, as always."
                    bearGuard "But, I've been thinking about getting a new armor from Methis, what do you think, courier?"
                    e "Yours doesn't look that bad, but I think a new armor won't do any harm."
                    bearGuard "You're right, courier. But I'm not sure if I want to visit Methis again, he's some odd sorts of rhino in the tribe."
                    e "Odd? How so?"
                    bearGuard "Don't you think it's fucking weird to call your mannequins weird names? Not mentioning one of them being that old blacksmith's..."
                    e "Yeah, I guess so."
                    bearGuard "Sometimes, when the midnight bell rings, when our shifts end, we hear noises behind the curtains in his shop."
                    bearGuard "What magical mannequins works by the night... we never dared to ask, but I'm lying if I say we're not curious."
                    "The guard looks around the area, as if he's expecting a spirit to pop out of nowhere."
                    bearGuard "I better get going."
            "Leave":

                e "I'm just passing by, I'll be on my way."
                bearGuard "Alright, but don't cause any trouble around here..."
                "You leave the bear guard behind and continue your journey."
    else:

        "It's only after a few seconds you can see that he's running towards your direction."
        bearGuard "Outsider! Stop right here!"
        e "Hey, I mean no harm."
        menu:
            bearGuard "By the name of our chief, I will kick you out of our territory once and for all."
            "Fight with the Guard":
                pass
            "Escape":
                e "S-shit!"
                if renpy.random.randint(2,7) > pc.agi:
                    "You try to run away from the guard, but you don't seem to have enough {color=#ddd}Agility{/color}. He quickly drags on your leg, pulling you into him."
                    bearGuard "Where do you think you're going, now fight me like a real bear."
                    jump bearguard_battle
                "You run away from the guard, he tries to chase you but you barely manage to lose him in the snow."
                jump main_ursinia_glade
        jump bearguard_battle
    return

label Bear_Guard_Cave_Discovery:

    "The bear guard stands rigid in the snow, harpoon resting against his shoulder. His breath fogs the cold air."
    "His ears twitch at some distant sound you can't quite make out. For a moment his usual stern expression cracks with unease."
    bearGuard "...You hear that, outsider?"
    "He keeps his voice low, almost a growl, eyes flicking toward the thick pines where the wind howls between the trunks."
    e "Hear what?"
    if herd_dead:
        bearGuard "Noises. Coming from the old cave up the ridge. Not animal. Not the wind. Something is wrong in there."
    else:
        bearGuard "Noises. Coming from the old cave up the ridge. Not animal. Not the wind. Something... or someone is there."
    "His grip tightens on the harpoon shaft, knuckles whitening beneath thick fur."
    if herd_dead:
        bearGuard "Been hearing it since Herd... since that incident. Like a gust of wind constantly blowing through the cave."
        "He shifts his weight, boots crunching in the snow."
        bearGuard "Chief's already dealing with the fallout from what we did to Herd. If I bring this to Commander now, he'll stir up more fear just by showing his face."
        bearGuard "We don't need the whole tribe thinking the mountains are cursed on top of everything else."
    else:
        bearGuard "Been hearing it since Herd got away. Faint. Like someone's trying not to be found."
        "He glances back toward the distant cave mouth, half-hidden by ice and shadow."
        bearGuard "Chief's got enough on his plate hunting for that elk. If I report this, the commander will just make it worse by sending more guards to patrol the area."

    "His gaze finally settles on you, heavy and tired."
    bearGuard "You wander these woods more than most. If you go poking around that cave... keep your mouth shut about what you find. At least until we know what it is."
    "He straightens, adjusting his grip on the weapon as if the conversation is already over."
    bearGuard "And if you do go... watch your back."
    if herd_dead:
        bearGuard "We don't know what's in there, but I don't want the tribe turning it into another story about Herd."
    "With that, the bear guard turns and trudges back toward his patrol route, leaving you alone with the distant, uneasy silence of the taiga."
    "The faint noises, if they were ever there, have gone quiet again."
    if herd_dead:
        "You ponder for a moment. After what happened to Herd, going into the cave alone would be foolish. If the noises mean anything, Chief Kaurhu and Daggi need to hear of them."
    else:
        "You pause to think it over. You could investigate the cave right now, though that might be dangerous, or report it to the chief and risk bringing trouble down on the bear guard."
    $ QuestBegin(quest47)
    if herd_dead:
        $ quest47.qProgress(_("Report the cave noises to Chief Kaurhu"))
    else:
        $ quest47.qProgress(_("Optional: Report the cave noises to Chief Kaurhu"))
        $ quest47.qProgress(_("Optional: Deal with the whispers in the Chilly Ice Cave"))
    return

label Bear_Guard_Report_To_Chief:

    $ bearguard_dialogues.setdefault("Chilly Ice Cave", {})
    $ bearguard_dialogues["Chilly Ice Cave"]["Chief Sent Daggi"] = True

    e "Chief... I need to speak with you. It's about the old cave near the taiga area."
    "Kaurhu's ears twitch. He leans forward slightly, the weight of his gaze heavy."
    kh "Speak."
    e "I heard there were noises coming from the old cave up the ridge. The bear guard said it was something... or someone. He seemed pretty worried about it."
    "Daggi's expression tightens. Kaurhu's eyes narrow, but he doesn't interrupt."
    kh "And you are the first here instead of the guards."
    e "Yes."
    "The old bear exhales slowly and closes his eyes for a moment."
    kh "Commander."
    d "Yes, Chief."
    kh "Take two of your most trusted guards and go with [e]. Investigate the cave. Find out what's going on there."
    "Daggi nods once, sharp and professional, though you catch a flicker of unease in his eyes."
    d "[e], you're with me. Gren and Illoch, you're coming too. We're going to check out that cave."
    kh "And outsider..."
    "Kaurhu's voice drops, low and warning."
    kh "I trust you to keep this quiet. No one else needs to know about this until we figure out what's going on. Do you understand?"
    e "Understood."
    "Daggi gestures for you to follow him out of the hall."
    menu:
        "Set off to the cave with Daggi":
            jump Bear_Guard_Journey_With_Daggi
        "Maybe Later":
            e "I can go, but I need a moment to get myself ready first."
            d "Of course, don't take too long."
            $ quest47.status = 3
            $ quest47.qComp(_("Report back to Daggi"))
            jump main_otsovaara_council_hall

label Bear_Guard_Report_To_Chief_Continue:
    e "Chief, I'm ready to set off for the cave."
    kh "Commander, lead our courier out."
    "The old bear doesn't give you another glance."
    d "Yes, Chief."
    "Daggi gestures for you to follow him out of the hall."
    jump Bear_Guard_Journey_With_Daggi

label Bear_Guard_Journey_With_Daggi:

    scene frostedtaiga

    "You follow Commander Daggi and the two guards through the tribe and into the snow-covered forest."
    "Daggi leads the way, his harpoon ready, while the bear guards flank you both, their eyes scanning the surroundings for any signs of danger."
    "For a while, only the crunch of snow and the clink of gear break the silence."
    d "I am glad you came to us first, [e]."
    d "If there is really someone hiding up there, I'd rather check it properly than leave you to stumble into it alone."
    d "If you've got questions, ask them now. I'll answer what I can."

    menu:
        "What do you ask Daggi?"
        "Ask what he knows about the cave":

            e "What exactly is up there?"
            d "Old ruins. A sealed crypt, if the elders' stories are true."
            d "No one is meant to be using it now, but the guards have heard scraping inside, and the cold around it is wrong."
            if herd_dead:
                d "After what happened to Herd, I am not dismissing signs like that."
            else:
                d "With Herd still missing, I cannot ignore the chance he passed through there."
            e "That's not very reassuring."
            d "No. But I would rather tell you the truth than pretend it is harmless."
        "Ask if he thinks it is dangerous":

            e "Do you think this is actually dangerous, or just guards scaring themselves?"
            d "Possibly both."
            d "Old places make people nervous, but nerves do not explain tracks, noises, and missing supplies."
            e "That's not very reassuring."
            d "I prefer honesty first."
            d "Still, I'll do my best to get you in and out of this in one piece."
        "Try to make friendly conversation":

            e "You're less stern out here than you were in the hall."
            d "In the hall I have to look like I know what I am doing."
            d "Out here I only have to keep a search party in one piece. I'd like to think I can manage that much."
            "You let out a short laugh before you can stop yourself."

    "The path steepens as you climb higher along the ridge, the pines thinning until little stands between you and the wind."
    e "So what happens if we do find someone in there?"
    d "If it is some lost hunter or frightened fool, we bring them back alive. If it is something worse, we deal with it."
    if herd_dead:
        d "And if this has anything to do with Herd's death, I want to know the truth of it before the mountain buries that too."
    else:
        d "If Herd is somehow tied to this, then I would rather reach him before panic, cold, or the wrong guard does."
    d "If I say the complicated version, Gren starts worrying and Illoch gets annoyed at him."
    bearGuard "Commander!"
    "Even the guards tense up slightly at the mention of their names."
    menu:
        d "Anything else you want to ask before we get there, [e]?"
        "Admit you're nervous":
            e "I won't lie, I'm nervous."
            d "Good."
            d "Nervous people pay attention. Stay with me, follow my lead, and that will do."
            e "...Alright."
        "Say you're ready":

            e "Whatever's in there, I'm ready for it."
            d "Good. Keep that spine."
            d "Just leave room for caution until we know what we're dealing with."
        "Tease him a little":

            e "You know, if you want me close, you can just say you enjoy the company."
            "Gren makes a strangled noise somewhere behind you."
            d "That is not quite what I said."
            d "But I would rather keep you close than have you wandering off where I cannot help. So stay near me."

    "By the time the cave mouth comes into view, the conversation fades on its own."
    "A chill runs down your spine. The air feels heavier here, and an eerie silence hangs over the area."
    "Daggi stops just outside the cave mouth and looks back at you."
    d "This is it."
    d "Once we go in, we move carefully. If something startles you, call it out. Do not go out on your own."
    d "I expect an old crypt full of bad air, loose stone, and something that already has half the guards on edge."
    "His grip tightens on the harpoon, then he gives you a brief nod."
    d "Stay where I can see you, [e]."
    d "Ready, [e]?"
    "With that, he steps into the cave, followed by the bear guards."
    "You take a deep breath and follow them inside, your heart pounding in your chest as you prepare to face whatever lies within."

    $ daggi_accompany = True
    jump Chilly_Ice_Cave

label Bear_Guard_Cave_Finish:
    if daggi_accompany:
        d "Well... that's one way to welcome visitors. You alright?"
        show daggi normal with dissolve
        "A heavy click answers him from somewhere inside the wall behind the fallen statues."
        "The bronze locking pins buried in the stone begin to withdraw one by one. Then a narrow panel grinds inward, revealing a recess hidden behind the guardians' pedestals."
        "Inside rests a small stone tablet, no longer than your hand, wrapped in frost and centuries of dust."
        "Daggi reaches it first, but only to brush the surface clear. Tight rows of hooked symbols run across the tablet's face, old enough that they barely look like writing at all."
        e "Can you read any of that?"
        d "No."
        d "If it is a bear script, it is older than anything I was taught."
        "The face of the tablet bears a carved figure beneath the writing: a broad-shouldered warrior with a crown worked into the shape of antlers, one hand on an axe, the other extended over a curling root or vine."
        d "This must be Stigandr. The conqueror our old stories never shut up about."
        e "Or the one they wanted remembered."
        "Daggi glances from the tablet to the broken tomb and the ruined guardians."
        d "A proud warlord, hidden under a mountain with two bronze sentries and a secret sealed behind them."
        d "The tribe remembers that he conquered the snow region. It remembers the victory."
        d "It does not remember clearly what came after, and I am starting to think that was deliberate."
        if not herd_dead:
            "Daggi's eyes drift back toward the offering table and the route you took through the chamber."
            d "And Herd was here. The bell, the fresh marks on the table, the astrolabe trapped in the gutter... none of that belongs to grave robbers or wandering hunters."
            e "So the guards really were hearing him?"
            d "Some of it, maybe. Herd moving through the upper cave. The rest could be this place waking up around him."
            d "By the time we reached the crypt properly, he was already gone. But at least now I know he came here for something of his own, not just to break our work and disappear."
        "He studies the markings for another breath, then wraps the tablet carefully in a strip of cloth torn from the inside of his bracer."
        d "We take it to Chief Kaurhu. He should see this before anyone starts inventing stories about it."
        $ quest47.qComp(_("Bring the crypt tablet to Chief Kaurhu"))
        scene black with dissolve
        "It takes the better part of an hour for you, Daggi, and the two guards to work your way back toward the blocked cave mouth."
        "At first the entrance is still jammed shut under the earlier collapse, but the constant rumbling from the statues' awakening has shaken the pile loose."
        "More than once another small tremor sends pebbles and crusted snow sliding down the heap, and each time a little more cold daylight spills through the gaps."
        "By the end, it is less a rescue than the mountain grudgingly deciding to let you leave."
        "Once there is enough daylight and air again, Daggi says little, keeping the wrapped tablet tucked tight under one arm all the way back to Otsovaara."
        jump Bear_Guard_Crypt_Tablet_Report
    elif bearguard_dialogues["Chilly Ice Cave"].get("Chief Sent Daggi", False):
        jump Bear_Guard_Cave_Finish_Reported_Solo
    else:
        "Herd clutches the recovered astrolabe tight against his chest, then gives you one sharp nod before looking back at the shattered stone."
        "Then a hard click rolls through the crypt from behind the broken guardians."
        show herd normal with dissolve
        "The wall at the back of the chamber unlocks with a series of dull metallic snaps, and a narrow panel shifts aside inside the stonework."
        "A small tablet lies in the recess it reveals, half-buried in frost. Herd is on it before the dust settles."
        "He wipes the slab clean with the heel of his hand. Thin hooked marks and cramped lines cover both faces, carved in an ancient language neither of you understand."
        "Herd squints, annoyed, then gives a short shake of his head."
        "Beneath the lines is the worn image of a warrior wearing an antler-crown, his axe lowered at his side while roots coil around his boots."
        "It fits the old bear-tribe stories of Stigandr, the ancestor who conquered the snow region and vanished into legend afterward."
        "Even so, he turns the tablet once more in his hands and presses it against his chest beside the astrolabe, already treating it like something he means to guard himself."
        "He nods once, firm and immediate."
        "After everything that drove him into this crypt, it makes a certain kind of sense. Whatever the tablet means, he does not intend to hand it back to the tribe first and ask permission later."
        "At the foot of the stairs, Herd slows and looks back to you."
        "Two fingers touch his brow, then point at you, before curling back toward his own chest."
        "This time the meaning lands without either of you pretending words would help. He will look for you again."
        "The corner of his mouth lifts. He gives one certain nod."
        jump Bear_Guard_Cave_Herd_Route_Finish

label Bear_Guard_Cave_Herd_Route_Finish:
    $ daggi_accompany = False
    "You answer the gesture as best you can, touching your own chest before raising your hand in parting where he can see it."
    "Herd presses a fist briefly to his chest in answer, then slips away up the dark stair with the astrolabe and tablet hidden under his wraps."
    $ QuestFinish(quest47)
    scene black with dissolve
    "You stay where you are for a moment after he disappears, listening to the crypt settle around you."
    "The whole meeting was brief, but it did not feel small. In that cold chamber, with no shared language except patience and gesture, Herd trusted you with something he would not have trusted to his own tribe."
    "By the time you climb out of the crypt yourself, the cave feels emptier than before, but no longer haunted by the same unfinished tension."
    "The whispers are gone. Herd has what he came for. All you can do now is hope he stays ahead of whatever finally drove him this far into the mountain."
    pause 0.5
    jump main_clawridge_ascent

label Bear_Guard_Cave_Finish_Reported_Solo:
    $ cave_state = bearguard_dialogues["Chilly Ice Cave"]
    $ cave_state["Daggi Found Herd"] = True
    show herd normal with dissolve
    "Herd clutches the recovered astrolabe tight against his chest, but before either of you can breathe easy, boots hammer down the crypt stairs."
    d "[e]!"
    show herd at r1 with move
    show daggi normal at l2
    show daggi at l1 with dissolve
    "Commander Daggi emerges from the dark with his harpoon raised, then stops short when he sees Herd alive beside the broken statues."
    d "Herd..."
    show herd at r3 with move
    "Herd recoils so hard he nearly stumbles over the broken bronze at his heels. His shoulders seize up, his breath goes ragged, and he locks the astrolabe against his chest as though Daggi might tear it free with his bare hands."
    with vpunch
    "When Daggi takes a single step forward, Herd flinches again and throws one arm up between them on instinct."
    e "Wait. The fight's over."
    "A hard click answers you from inside the wall behind the shattered guardians."
    "Bronze locking pins withdraw one by one, and a narrow stone recess slides open behind the pedestals. Inside rests a frost-caked tablet, no larger than your hand."
    "With both of them staring at it, you step forward first and lift the tablet free before either can snatch it. Hooked lines cover both faces, worn old enough to feel older than the crypt around you."
    "Herd shakes his head hard enough to rattle his antlers. He points to the tablet, then to his own chest, then jerks the same hand toward Daggi with a flash of open fear before slashing one sharp gesture back toward the stairs."
    e "He thinks you're going to take it."
    "Daggi notices it at once. His grip loosens on the harpoon shaft, and he lowers the weapon until its point rests against the stone."
    d "I know."
    d "Herd, I am not here to drag you out in chains."
    "Herd does not believe him. He edges behind you instead, eyes locked on Daggi's hands, one shaking hand still half-lifted like a shield."
    d "I know you can't hear me... but I am not here to fight you."
    "Daggi keeps his voice level, but his eyes stay on the tablet in your hands."
    d "I don't know what Herd plan to do with it, but that bear relic needs to go to Chief Kaurhu before the guards turn this place into another panic."
    d "Let me take it, and I'll keep the rest of them off Herd's trail for as long as I can."
    "As he speaks, he reaches toward the tablet with slow, careful hands, giving Herd every chance to see he is not lunging for him. It only makes Herd curl tighter behind your shoulder, panic plain in every line of him."

    menu:
        "What do you do?"
        "Let Daggi take the tablet":
            $ cave_state["Crypt Tablet Holder"] = "Daggi"
            "You do not pull back when Daggi reaches for it. After a beat, you let him ease the tablet from your hands."
            "He wraps it at once in a strip of cloth torn from the inside of his bracer and tucks it under one arm."
            "Herd goes rigid. Terror flashes across his face before it hardens into something smaller."
            e "The chief needs to see this."
            d "And he will. Straight from me. No guard is going to turn this into another hunt."
            d "I will tell the guards to leave you alone, but I need to get this to the chief."
            "He turns to Herd. Herd does not look convinced, but after a long, furious stare he backs away instead of rushing Daggi."
            "At the foot of the stairs, he pauses just long enough to meet your eyes. Resignation, perhaps."
            "He presses the astrolabe harder to his chest and disappears soon after."
            $ quest47.qComp(_("Bring the crypt tablet to Chief Kaurhu"))
            scene black with dissolve
            "Daggi signals the others to follow him, and keeps the wrapped tablet tucked tight beneath his arm all the way back to Otsovaara."
            jump Bear_Guard_Crypt_Tablet_Report
        "Stop Daggi":
            $ cave_state["Crypt Tablet Holder"] = "Herd"
            "You pull the tablet back before Daggi can close his hand around it."
            e "No. Look at him."
            "For a second Daggi says nothing. Herd is pressed so tight behind you that you can feel the tremor in his breathing."
            e "He found this all by himself. You can't just take it from him like that."
            "You turn and press the tablet into Herd's hands. For a second he only stares, startled, before he clamps it to his chest beside the astrolabe."
            d "I understand, but Chief Kaurhu is going to hate this."
            e "Maybe. But it's not yours to take. You can tell the chief about it, but you can't just take it from him."
            "For a long moment Daggi says nothing. Then he exhales through his nose and steps aside from the stairs."
            d "Alright, then. I'll tell my guards to leave you two alone."
            d "I can't lie for you, [e]. And I can't guarantee Chief won't send the whole tribe crashing after him over it."
            "Herd hesitates only long enough to meet your eyes. He taps his chest with two fingers, then points those same fingers toward you in a quick, grateful motion before Daggi leaves."
            jump Bear_Guard_Cave_Herd_Route_Finish


label Bear_Guard_Crypt_Tablet_Report:
    $ daggi_accompany = False
    $ cave_state = bearguard_dialogues["Chilly Ice Cave"]

    scene otsovaara_throne with dissolve

    "By the time you reach the council hall again, Daggi has said almost nothing. Gren and Illoch remain by the doors while he steps forward and unwraps the little tablet before the throne."
    show daggi normal at r1 with dissolve
    d "Chief. This was sealed behind the guardians in the old crypt."
    show kaurhu normal at l1 with dissolve
    kh "Old Crypt...? Why haven't I heard any of it?"
    d "Yes, Chief. The crypt seems to be hidden in the corner of the ice cave, the avalanche might have revealed the buried entrance after all."
    if cave_state.get("Daggi Found Herd", False):
        d "When I reached the lower crypt, [e] had already found Herd alive there."
        d "Herd escaped with the astrolabe he came for, but the courier put the tablet in my hands and I brought it straight here."
    else:
        d "The cave mouth had collapsed behind us earlier, but the fighting shook the pile loose enough for us to force a way back out."
    if herd_dead:
        d "We also found Herd's surveying bell in the lower chamber, and signs he had been working there before he died."
        d "Whatever the guards were hearing now, it was not Herd come back. But he had gone into that crypt for a reason."
        e "It looked more like he was tracing something hidden in the ruins than trying to frighten anyone."
    elif cave_state.get("Daggi Found Herd", False):
        d "The guards were not hearing a ghost. They were hearing Herd moving through the cave and the crypt answering him."
        e "He wasn't in there to sabotage anything. He was following the astrolabe and whatever this tablet meant."
    else:
        d "And Herd had been there. We found his surveying bell, fresh traces of his work, and his astrolabe jammed in the old gutter."
        d "He was not just hiding in the dark for the sake of it. He came down there looking for something he had lost."
        e "We never caught up to him, but the noises the guards heard make more sense now."
    "Kaurhu takes the tablet from him and turns it in his hands. The slab is small, but both faces are cut with dense hooked characters, worn by age and impossible to place."
    kh "Not our language."
    e "Neither of us could make sense of it."
    d "It looked older than the rest of the crypt. We thought it best to bring it straight to you."
    if herd_dead:
        kh "So he left traces. Not ghosts. Good."
        kh "I will not have the tribe making a legend out of it."
    elif cave_state.get("Daggi Found Herd", False):
        kh "So he was there after all."
        kh "Alive, and still digging at old bones under my mountain."
    else:
        kh "So he was there after all."
        kh "That explains more than I expected."
    kh "Stigandr. Or someone meant to resemble him."
    "The old bear's thumb pauses over the carving. For the first time, his stare leaves the two of you and goes somewhere much farther away."
    kh "The elders said the conqueror took the great Otsovaara for the bears and vanished from the world soon after."
    kh "No one agrees on what happened next. Some said he died. Some said he sealed himself away. Some said he walked into the mountain and never walked out."
    d "I thought it was just another tale to make cubs keep away from deep snow and deeper ruins."
    "The chief studies the writing for a long moment, his frown deepening rather than easing."
    kh "You thought right."
    kh "If this was hidden under the mountain, then it stays with me until I decide who hears of it."
    "He closes his hand over the tablet and settles back into his throne."
    kh "Courier. You kept quiet, followed my commander's lead, and brought this to the proper hall. That is enough."
    e "Then I'm free to go?"
    kh "Yes. Go."
    d "Thank you, Chief."
    kh "I was speaking to the courier, cub. You stay."
    "Daggi straightens at once, ears flicking once in embarrassed acknowledgment."
    d "...Yes, Chief."
    "Before turning back to the throne, he gives you one brief glance that lands somewhere between thanks and apology."
    $ QuestFinish(quest47)
    jump main_otsovaara_station
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
