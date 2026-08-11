screen place_sundersilk_cascades():
    zorder 10 tag place

    imagebutton:
        xalign 0.99
        yalign 0.69
        idle "explore_idle"
        hover "explore_hover"
        action Return("Explore")
    $ findingEversprout = next((x for x in discoveredtrinket if x.img == "Eversprout"), None)
    if findingEversprout != None and not isNight() and findingEversprout.discovered == True and eversprout_route == 0:
        imagebutton:
            xalign 0.34
            yalign 0.25
            idle "sprout_1"
            style "bushchime_button"
            action Return("Sprout1")
    imagebutton:
        xalign 0.63
        yalign 0.91
        idle "kingspawn_arrow"
        hover "kingspawn_arrow_hover"
        style "footstep_button"
        action Return("To Freshwater")
label main_sundersilk_cascades:
    $ current_location = sundersilk_cascades
    $ renpy.music.play(mForest, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ wilderness = True
    $ timenow.minute += 12
    $ timenow.passTime()
    if isNight():
        scene sundersilkcascades_night
    else:
        scene sundersilkcascades
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_sundersilk_cascades
    if _return == "Explore":
        jump sundersilk_cascades_loop
    if _return == "To Freshwater":
        jump main_mossy_freshwater
    if _return == "Sprout1":
        $ eversprout_route = 1
        "In the peripheral of your vision, you discover a young sprout wiggling around the waterfall."
        "Perhaps it's what you believe to be the eversprout Gwyddyon's scroll talked about..."
        "You reach out and grab onto the herb, but the deceitful sprout jumps away as you reach out for it, bouncing its way out of your sight."
        e "Wait, where did it go..."
        "The sprout must be close, you should chase after it before it disappears once more."
        jump main_sundersilk_cascades
    jump main_sundersilk_cascades

label sundersilk_cascades_loop:
    if isNight():
        scene sundersilkcascades_night
    else:
        scene sundersilkcascades
    $ rnd = renpy.random.random()
    if rnd < 0.2:
        "You search around the area for a while, but there seem to be nothing worth noting nearby."
    elif rnd < 0.3:
        "You look around the sundersilk cascades, under the bright sun you see some shiny blue flowers near the waterfall, you went and pick it up. It was a Hydrangea."
        $ addItem("Hydrangea", inventory, 1)

        "You put it in your bag, you now have [item_number] hydrangea."
    elif rnd < 0.4:
        "You look around the sundersilk cascades, under the bright sun you see a fluffy feather between the grass, you went and pick it up. It was a feather."
        $ addItem("Feather", inventory, 1)
        $ item_number = LookForItemNumber("Feather", inventory)
        if item_number == 1:

            "You put it in your bag, you now have [item_number] feather."
        else:

            "You put it in your bag, you now have [item_number] feathers."
    elif rnd < 0.5:
        "You search around the area for a while, but there seem to be nothing worth noting nearby."
    else:
        "You search around the area for a while, but there seem to be nothing worth noting nearby."

    jump main_sundersilk_cascades
screen place_backyard_barn():
    zorder 10 tag place

    imagebutton:
        xalign 0.53
        yalign 0.94
        idle "kingspawn_arrow"
        hover "kingspawn_arrow_hover"
        style "footstep_button"
        action Return("To Farmland")
    imagebutton:
        xalign 0.19
        yalign 0.78
        idle "arthur_idle"
        hover "arthur_hover"
        action Return("Arthur")

label main_backyard_barn:
    $ renpy.music.play(mBarn, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ wilderness = True
    $ timenow.minute += 12
    $ timenow.passTime()

    if isNight():
        scene backyard_barn_night
    else:
        scene backyard_barn
    with dissolve
    if arthur_encounter == 0:
        jump Arthur_First_Scene
    elif arthur_encounter == 1 and timenow.day > arthur_first_encounter + 1:
        jump Arthur_Second_Scene
    show screen menu_buttons
    window hide
    call screen place_backyard_barn
    if _return == "To Farmland":
        jump main_summery_farmland
    if _return == "Arthur":
        jump Arthur_Dialogue
    jump main_backyard_barn

label main_grove_of_harvest:
    $ current_location = grove_of_harvest
    $ renpy.music.play(mBarn, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ wilderness = True
    $ timenow.minute += 15
    $ timenow.passTime()
    if quest33.status == True:
        $ prattlefell_meadow.discovered = True
    if isNight():
        scene grove_of_harvest
    else:
        scene grove_of_harvest
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_grove_of_harvest
    if _return == "Explore":
        jump grove_of_harvest_loop
    if _return == "To Farmland":
        jump main_summery_farmland
    if _return == "To Meadow":
        jump main_prattlefell_meadow
    if _return == "Seedsman":
        "You walk slowly towards the bushes, and suddenly you see a tall vine-like creature peeking out from the bushes."
        "With a rustle of leaves, the Seedsman bursts from a wall of brambles. His thorn-laced arms snap outward, vines writhing like serpents."
        e "S-shit!"
        jump seedsman_battle
    jump main_grove_of_harvest

screen place_grove_of_harvest():
    zorder 10 tag place

    imagebutton:
        xalign 0.99
        yalign 0.69
        idle "explore_idle"
        hover "explore_hover"
        action Return("Explore")
    imagebutton:
        xalign 0.57
        yalign 0.97
        idle "bedroom_arrow"
        hover "bedroom_arrow_hover"
        style "footstep_button"
        action Return("To Farmland")
    if not hasTrinket("Spirespike") and LookForItem("Spirespike", discoveredtrinket):
        imagebutton:
            focus_mask "grove_of_harvest_rose_bush"
            idle AlphaMask("grove_of_harvest","grove_of_harvest_rose_bush")
            hover AlphaMask(dayHover("grove_of_harvest"),"grove_of_harvest_rose_bush")
            action Return("Seedsman")
    if prattlefell_meadow.discovered == True:
        imagebutton:
            xalign 0.87
            yalign 0.87
            idle "lusterfield_arrow2"
            hover "lusterfield_arrow2_hover"
            action Return("To Meadow")

label grove_of_harvest_loop:
    if isNight():
        scene grove_of_harvest
    else:
        scene grove_of_harvest
    $ valid_plum_thief_search = timenow.hour >= 9 and timenow.hour <= 16 and (quest33.status == 2 or quest33.status == 3)
    if valid_plum_thief_search:
        $ grovebanditsearches += 1
    $ rnd = renpy.random.random()
    if valid_plum_thief_search and (grovebanditsearches >= 3 or rnd < 0.5):
        jump Bandit_Meet_Quest
    if rnd < 0.1:
        "Around the garden, you wander and pick up a certain fruit, it was a Hawthorn."
        $ addItem("Hawthorn", inventory, 1)
        $ item_number = LookForItemNumber("Hawthorn", inventory)
        if item_number == 1:
            "You put the Hawthorn in your bag, you now have [item_number] Hawthorn."
        else:
            "You put the Hawthorn in your bag, you now have [item_number] Hawthorns."
    elif rnd < 0.15:
        "Around the garden, you notice that there's row of apple bushes nearby, you go and pick one of them up."
        $ addItem("Apple", inventory, 1)
        $ item_number = LookForItemNumber("Apple", inventory)
        if apple_item.number == 1:

            "You put the Apple in your bag, you now have [item_number] Apple."
        else:

            "You put the Apple in your bag, you now have [item_number] Apples."
    elif rnd < 0.2:
        "Around the garden, you wander and pick up a certain flower, it was a red rose."
        $ addItem("Red Rose", inventory, 1)
        $ item_number = LookForItemNumber("Red Rose", inventory)
        if item_number == 1:

            "You put it in your bag, you now have [item_number] rose."
        else:

            "You put it in your bag, you now have [item_number] roses."
    elif rnd < 0.35:
        "You run into a scarecrow on the field, it seems to not be aware of your presence."
        menu:
            "Do you wish to fight the scarecrow?"
            "Fight with the scarecrow":
                jump scarecrow_battle
            "Leave it alone":
                pass
    elif rnd < 0.5:
        "You search around the area for a while, but there seem to be nothing worth noting nearby."
    elif rnd < 0.55:
        "As you walk around the garden, you notice a wide path that leads to outside of the village, you follow the path, and soon, you find yourself in the middle of a meadow."
        "It looks like you are now at the Prattlefell Meadow."
        $ prattlefell_meadow.discovered = True
        jump main_prattlefell_meadow
    elif rnd < 0.65:
        "You walk around the garden, and you notice a small patch of flowers nearby, you go and pick it up, it was hops."
        $ addItem("Hops", inventory, 1)
        $ item_number = LookForItemNumber("Hops", inventory)
        if item_number == 1:

            "You put the flower in your bag, you now have [item_number] hops."
        else:

            "You put the flower in your bag, you now have [item_number] hops."
    else:
        "You search around the area for a while, but there seem to be nothing worth noting nearby."

    jump main_grove_of_harvest

screen place_prattlefell_meadow():
    zorder 10 tag place

    imagebutton:
        xalign 0.99
        yalign 0.69
        idle "explore_idle"
        hover "explore_hover"
        action Return("Explore")
    if bandits_hideout.discovered == True:
        imagebutton:
            xalign 0.33
            yalign 0.61
            idle "lusterfield_arrow1"
            hover "lusterfield_arrow1_hover"
            style "footstep_button"
            action Return("To Hideout")
    imagebutton:
        xalign 0.43
        yalign 0.91
        idle "kingspawn_arrow"
        hover "kingspawn_arrow_hover"
        style "footstep_button"
        action Return("To Grove")

    if travelling_carousal.discovered == True and (timenow.day % 7 == 1 or timenow.day % 7 == 2):
        imagebutton:
            xalign 0.67
            yalign 0.73
            idle "carousal_arrow"
            hover "carousal_arrow_hover"
            style "footstep_button"
            action Return("To Carousal")

    if spearhead_plateau.discovered == True:
        imagebutton:
            xalign 0.83
            yalign 0.74
            idle "sparklinglagoon_arrow"
            hover "sparklinglagoon_arrow_hover"
            style "footstep_button"
            action Return("To Plateau")

label main_prattlefell_meadow:
    $ current_location = prattlefell_meadow
    $ renpy.music.play(mForest, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ wilderness = True
    $ timenow.minute += 15
    $ timenow.passTime()
    if isNight():
        scene prattlefell_meadow_night
    else:
        scene prattlefell_meadow
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_prattlefell_meadow
    if _return == "Explore":
        jump prattlefell_meadow_loop
    if _return == "To Grove":
        jump main_grove_of_harvest
    if _return == "To Hideout":
        jump main_bandits_hideout
    if _return == "To Plateau":
        jump main_spearhead_plateau
    if _return == "To Carousal":
        jump main_travelling_carousal
    jump main_prattlefell_meadow

label prattlefell_meadow_loop:
    if isNight():
        scene prattlefell_meadow_night
    else:
        scene prattlefell_meadow
    $ rnd = renpy.random.random()
    if rnd < 0.18:
        if pirkka_meet == False and quest35.status == False:
            jump Pirkka_First_Meet
        elif quest35.status != False and quest35.status != True and (bchest_sprite_img == "bchest_sprite2" or quest35.status == 2.5) and quest35.status != 3:
            $ renpy.music.play(mBarn, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
            e "P-pirkka?"
            "The wandering bard is sitting by a campfire, strumming his lute."
            "He looks up and smiles as you approach."
            show pirkka normal with dissolve
            p "[e], my friend. It's good to see you again. I hope your journey was successful? Please tell me you do."
            e "About that, I'm sorry, Pirk. I didn't find the prose, but I did find some clues about where it might be."
            e "They sold it to someone else in the village, I suppose it's Lusterfield?"
            jump Pirkka_Bandit_Quest_Report
        else:
            "You search around the area for a while, but there seem to be nothing worth noting nearby."
    elif rnd < 0.28 and not isNight():
        "Suddenly, you find a gnoll jumping out from the tall grass."
        jump gnoll_battle
    elif rnd < 0.35 and songweaverhatrecipe not in discoveredrecipe:
        "You found a small piece of paper that details the recipe for a... stylistic hat that is usually worn by a famous bard."
        $ discoveredrecipe.append(songweaverhatrecipe)
    elif rnd < 0.4:
        "As you walk around the meadow, a faint grey building can be seen amongst the green grassland, white flags and cloth hanging around the building with a tint of red."
        "You can see a few bandits walking around the area, seem to be guarding the area."
        "You approach the building with caution, and soon, you find yourself in front of the bandit's hideout."
        $ bandits_hideout.discovered = True
        jump main_bandits_hideout
    elif rnd < 0.48 and knighthelmetrecipe not in discoveredrecipe:
        "Half-buried beneath the roots of a tall grass, you uncover a weathered note sealed in wax."
        "It details how to craft a knight helmet from 3 iron ingots, 1 strap, and 1 piece of fabric."
        "The note seems to be quite old, and the ink is smudged in some areas, but you can still make out the instructions clearly enough."
        msg "You have learnt the recipe for Knight Helmet."
        $ discoveredrecipe.append(knighthelmetrecipe)
    elif rnd < 0.5:
        "You walk around the meadow, and you notice a small patch of flowers nearby, you go and pick it up, it was a mugwort."
        $ addItem("Mugwort", inventory, 1)
        $ item_number = LookForItemNumber("Mugwort", inventory)
        if item_number == 1:

            "You put the flower in your bag, you now have [item_number] mugwort."
        else:

            "You put the flower in your bag, you now have [item_number] mugworts."
    elif rnd < 0.6:

        $ addItem("Red Berry", inventory, 1)

        "You look around the meadow, under the bright sun you see something tinted red in the bush, you went and pick it up. It was a red berry."
        $ item_number = LookForItemNumber("Red Berry", inventory)
        if item_number == 1:

            "You put the berry in your bag, you now have [item_number] red berry."
        else:

            "You put the berry in your bag, you now have [item_number] red berries."
    elif rnd < 0.7:
        "You look around the meadow, under the bright sun you see something tinted blue in the bush, you went and pick it up. It was a blue berry."
        $ addItem("Blue Berry", inventory, 1)
        $ item_number = LookForItemNumber("Blue Berry", inventory)
        if item_number == 1:

            "You put the berry in your bag, you now have [item_number] blue berry."
        else:

            "You put the berry in your bag, you now have [item_number] blue berries."
    elif rnd < 0.8 and not isNight() and spearhead_plateau.discovered == False:
        "The sunlight glistens off a dirt trail in the meadow, you follow the path, and soon, you find yourself climbing a small hill."
        "At the top of the small hills, you turn back and see a wide view of the meadow, the sun shining down on the grassland, a few trees scattered around the area."
        "In front of you, it was another vast expanse of plains, with a few spear-shaped rocks sticking out of the ground."
        "And at the horizon, you can see a giant axe-shaped rock piercing the sky, its stature looming over the landscape."
        $ spearhead_plateau.discovered = True
        jump main_spearhead_plateau
    elif rnd < 0.9:
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

    jump main_prattlefell_meadow

screen place_bandits_hideout():
    zorder 10 tag place

    imagebutton:
        xalign 0.99
        yalign 0.69
        idle "explore_idle"
        hover "explore_hover"
        action Return("Explore")
    imagebutton:
        xalign 0.76
        yalign 0.94
        idle "bedroom_arrow"
        hover "bedroom_arrow_hover"
        style "footstep_button"
        action Return("To Meadow")
    imagebutton:
        xalign 0.47
        yalign 0.79
        idle "dungeon1_arrow"
        hover "dungeon1_arrow_hover"
        style "footstep_button"
        action Return("To Bandit")

    imagebutton:
        xalign 0.14
        yalign 0.71
        idle "sparklinglagoon_arrow"
        hover "sparklinglagoon_arrow_hover"
        style "footstep_button"
        action Return("To Glade")
    if quest34.status == True:
        imagebutton:
            xalign 0.56
            yalign 0.84
            idle "bandit_idle"
            hover "bandit_hover"
            style "footstep_button"
            action Return("Bandit")

label main_bandits_hideout:
    $ current_location = bandits_hideout
    $ renpy.music.play(mForest, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ wilderness = True
    $ timenow.minute += 15
    $ timenow.passTime()
    if isNight():
        scene bandits_hideout_night
    else:
        scene bandits_hideout
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_bandits_hideout
    if _return == "Explore":
        jump bandits_hideout_loop
    if _return == "To Glade":
        if bandit_toll_day < timenow.day:
            jump Bandit_Toll_Collect
        else:
            "You walk outside of the bandit's hall. The one guarding the pathway winks at you before letting you go."
        jump main_ursinia_glade
    if _return == "To Meadow":
        jump main_prattlefell_meadow
    if _return == "To Bandit":
        scene black with dissolve
        pause 0.5
        "You enter the bandit's hideout."
        $ renpy.music.play(mBandit, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
        jump Bandits_Hideout_Enter
    if _return == "Bandit":
        hide screen menu_buttons
        if bandit_toll_day < timenow.day:
            jump Bandit_Toll_Collect
        else:
            bd "You can go now, if that wasn't obvious enough."
            "Bandit crosses his arms, and begins to look the other directions."
            jump main_bandits_hideout
    jump main_bandits_hideout

screen place_spearhead_plateau():
    zorder 10 tag place

    imagebutton:
        xalign 0.99
        yalign 0.69
        idle "explore_idle"
        hover "explore_hover"
        action Return("Explore")

    imagebutton:
        xalign 0.53
        yalign 0.91
        idle "bedroom_arrow"
        hover "bedroom_arrow_hover"
        style "footstep_button"
        action Return("To Meadow")

    if travelling_carousal.discovered == True and (timenow.day % 7 == 4 or timenow.day % 7 == 5):
        imagebutton:
            xalign 0.67
            yalign 0.73
            idle "carousal_arrow"
            hover "carousal_arrow_hover"
            style "footstep_button"
            action Return("To Carousal")

label main_spearhead_plateau:
    $ current_location = spearhead_plateau
    $ renpy.music.play(mForest, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ wilderness = True
    $ timenow.minute += 15
    $ timenow.passTime()
    if isNight():
        scene spearhead_plateau
    else:
        scene spearhead_plateau
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_spearhead_plateau
    if _return == "Explore":
        jump spearhead_plateau_loop
    if _return == "To Meadow":
        jump main_prattlefell_meadow
    if _return == "To Carousal":
        jump main_travelling_carousal
    jump main_spearhead_plateau

label spearhead_plateau_loop:
    if isNight():
        scene spearhead_plateau
    else:
        scene spearhead_plateau
    $ rnd = renpy.random.random()
    if rnd < 0.1:
        if pc.level < 12:
            "You search around the area, there seem to be something ahead of you, but it seems like your level is too low to notice it yet."
        else:
            "You walk around the meadow, and suddenly, you notice a small pamphlet lying between the grass."
            if LookForItem("Magic Show Pamphlet", inventory):
                "It looks to be the same flyer for the travelling carnival, so you quickly put it away."
            else:
                "Picking it up, it looks to be a flyer for a travelling carnival, putting it in the back, perhaps you should check it out sometime..."
                $ addItem("Magic Show Pamphlet", inventory, 1)
    elif rnd < 0.2 and enchantedkirtlerecipe not in discoveredrecipe:
        "Near one of the spear-like stones, you find a stitched pattern pinned beneath an old rock."
        "The diagram describes an enchanted kirtle, it's woven from 3 pieces of soft fur, 2 fabrics, and 2 crystal strings."
        msg "You have learnt the recipe for Enchanted Kirtle."
        $ discoveredrecipe.append(enchantedkirtlerecipe)
    elif rnd < 0.3 and LookForItem("Magic Show Pamphlet", inventory) and isWeekdayNight() and travelling_carousal.discovered == False:
        "As you walk around the plateau, you hear a loud commotion coming from somewhere afar."
        "Following the noise, you soon find yourself at a large open field, where a few tents and stalls have been set up."
        "It seems like the travelling carousal is here."
        $ travelling_carousal.discovered = True
        jump Ribba_First_Show
    else:
        "You search around the area for a while, but there seem to be nothing worth noting nearby."

    jump main_spearhead_plateau

screen place_travelling_carousal():
    zorder 10 tag place

    imagebutton:
        xalign 0.99
        yalign 0.69
        idle "explore_idle"
        hover "explore_hover"
        action Return("Explore")

    imagebutton:
        xalign 0.53
        yalign 0.91
        idle "bedroom_arrow"
        hover "bedroom_arrow_hover"
        style "footstep_button"
        action Return("To Plains")

    if isNight():
        imagebutton:
            focus_mask "travelling_carousal_chop"
            idle AlphaMask("travelling_carousal_night", "travelling_carousal_chop")
            hover AlphaMask(dayHover("travelling_carousal_night"), "travelling_carousal_chop")
            action Return("Chop")
    else:
        imagebutton:
            focus_mask "travelling_carousal_chop"
            idle AlphaMask("travelling_carousal", "travelling_carousal_chop")
            hover AlphaMask(nightHover("travelling_carousal"), "travelling_carousal_chop")
            action Return("Chop")

    imagebutton:
        focus_mask "ribba_idle"
        idle "ribba_idle"
        hover "ribba_hover"
        action Return("Ribba")


label main_travelling_carousal:
    $ current_location = travelling_carousal
    $ renpy.music.play(mForest, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ wilderness = True
    $ timenow.minute += 15
    $ timenow.passTime()
    if isNight():
        scene travelling_carousal_night
    else:
        scene travelling_carousal
    with dissolve
    show screen menu_buttons
    call screen place_travelling_carousal
    hide screen menu_buttons
    if _return == "Explore":
        jump travelling_carousal_loop
    if _return == "Chop":
        jump travelling_carousal_chop
    if _return == "To Plains":
        if timenow.day % 7 == 1 or timenow.day % 7 == 2:
            jump main_prattlefell_meadow
        elif timenow.day % 7 == 4 or timenow.day % 7 == 5:
            jump main_spearhead_plateau
        else:
            jump main_prattlefell_meadow
    if _return == "Ribba":
        if ribba_dialogues.get("First Encounter", False) == False:
            jump Ribba_First_Encounter
        else:
            jump Ribba_Dialogue

    jump main_travelling_carousal

label travelling_carousal_loop:
    if isNight():
        scene travelling_carousal_night
    else:
        scene travelling_carousal
    $ rnd = renpy.random.random()
    if rnd < 1:

        "You search around the area for a while, but there seem to be nothing worth noting nearby."

    jump main_travelling_carousal

label travelling_carousal_chop:
    if isNight():
        scene travelling_carousal_night
    else:
        scene travelling_carousal

    "A painted stall stands off to the side of the midway, ringed with cut wood, and a small cheering crowd."
    "At the center, a bright placard promises ten clean chops in a row for the grand prize of an enchanted chaperon."

    if enchanted_chaperon_rewarded:
        "The chaperon itself is gone now, but the barker is still taking challengers to earn 120 gold."

    menu:
        barker "Fifty gold a round! One miss and yer out! Fancy your chances?"
        "Pay 50 gold to play" if pc.gold >= 50:
            $ pc.gold -= 50
            "The stallmaster raises his voice to draw more of the crowd over."
            barker "Step up, young man! Ten perfect chops! Don't blink!"
            $ chop_step = 0
            $ chop_amount = 10
            $ chopped_wood = 0
            $ tree_amount = 0
            $ increasing = True
            call travelling_carousal_tree_chopping from _call_travelling_carousal_tree_chopping

            if chopped_wood == chop_amount:
                "You hear a pounding applause on the wood rails as the last strike lands perfectly."
                if not enchanted_chaperon_rewarded:
                    "Laughing in disbelief, the stallmaster unhooks the enchanted chaperon from its display frame and hands it over as your prize."
                    barker "Well I'll be! A perfect run! You sure you ain't got some magic in those arms, young man?"
                    $ addItem("Enchanted Chaperon", inventory, 1)
                    $ enchanted_chaperon_rewarded = True
                else:
                    barker "The grand prize has already been claimed, but your perfect run is still impressive!"
                    barker "Here's 120 gold for the show!"
                    $ pc.gold += 120
            else:
                "A miss draws a loud groan from the spectators before the barker claps and waves the next challenger closer."
                if chopped_wood > 0:
                    "You still managed [chopped_wood] clean chops before the round ended."
                else:
                    "Your round ends before you can build any momentum at all."
        "Walk away":
            "The stallmaster shrugs and immediately turns to shout at another passerby, trying to lure them in instead."

    jump main_travelling_carousal

label travelling_carousal_tree_chopping:
    $ chop_size = max(int(renpy.random.randint(25, 45) / (tree_amount*0.3+1)), 5)
    $ chop_size_minimum = renpy.random.randint(4, 96-chop_size)
    $ chop_size_maximum = chop_size_minimum + chop_size
    $ move_speed = 50 + tree_amount * renpy.random.randint(5, 15)

    call screen precision_minigame("enchanted chaperon", "[chopped_wood] / [chop_amount]", _("Swing"))
    if _return >= chop_size_minimum - 2 and _return <= chop_size_maximum + 2:
        $ chopped_wood += 1
        play sound clickchop
        $ tree_amount += 1
        if tree_amount >= chop_amount:
            return
        jump travelling_carousal_tree_chopping
    else:
        return

label Bandit_Toll_Collect:
    "A gruff voice calls out as you stand in front of the stone structure."
    bd "Well, well, what do we have here? A traveler, eh?"
    e "Hey! Back off, I've got weapons."
    bd "You've got guts, I'll give you that. But I'm afraid this is our territory, and you'll have to pay the toll to pass."
    menu:
        bd "Nothing much. [bandit_toll] gold and I'll let you go."
        "Pay the toll" if pc.gold >= bandit_toll:
            $ pc.gold -= bandit_toll
            if pc.gold < 0:
                $ pc.gold = 0

            e "Well, I don't want any trouble. Here's [bandit_toll] gold."
            bd "Wise choice. We'll put these gold into good use. Pass now before I change my mind and take you in."
            $ bandit_toll += 100
            $ bandit_toll_day = timenow.day + 3
            "The bandit smirks."
            jump main_ursinia_glade
        "Fight":
            e "I won't budge so easily, let's fight then!"
            bd "Ha, what a dumb decision. Prepare yourself, for when we take you in after this."
            jump bandit_battle

label bandits_hideout_loop:
    if isNight():
        scene bandits_hideout_night
    else:
        scene bandits_hideout
    $ rnd = renpy.random.random()
    if rnd < 0.1:
        "You search around the area for a while, but there seem to be nothing worth noting nearby."
    else:
        "You search around the area for a while, but there seem to be nothing worth noting nearby."

    jump main_bandits_hideout

screen place_riverside_crossing():
    zorder 10 tag place

    imagebutton:
        xalign 0.99
        yalign 0.69
        idle "explore_idle"
        hover "explore_hover"
        action Return("Explore")
    imagebutton:
        xalign 0.62
        yalign 0.32
        idle "lusterfield_arrow1"
        hover "lusterfield_arrow1_hover"
        style "footstep_button"
        action Return("To Freshwater")
    if amble_location == "riverside_crossing":
        imagebutton:
            xalign 0.755
            yalign 0.14
            idle "amble_river_idle"
            hover "amble_river_hover"
            action Return("Amble")


label main_riverside_crossing:
    $ current_location = riverside_crossing
    $ renpy.music.play(mForest, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ wilderness = True
    $ timenow.minute += 12
    $ timenow.passTime()
    if quest38.status == True or get_task_completion_time("Rebuilding the Bridge") > 3:
        $ riverside_crossing_finished = True
    call showing_riverside_crossing from _call_showing_riverside_crossing
    call Lusterfolk_Schedule from _call_Lusterfolk_Schedule_7
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_riverside_crossing
    if _return == "Explore":
        jump riverside_crossing_loop
    if _return == "To Freshwater":
        jump main_mossy_freshwater
    if _return == "Amble":
        jump Amble_River_Talk
    jump main_riverside_crossing

label showing_riverside_crossing:
    if quest38.status == False or quest38.status == 2 or (quest38.status != True and get_task_completion_time("Rebuilding the Bridge") == 0):
        if isNight():
            scene riverside_crossing_construction_1_night
        else:
            scene riverside_crossing_construction_1
    elif quest38.status == 3 or get_task_completion_time("Rebuilding the Bridge") == 1:
        if isNight():
            scene riverside_crossing_construction_2_night
        else:
            scene riverside_crossing_construction_2
    elif quest38.status == 4 or get_task_completion_time("Rebuilding the Bridge") == 2:
        if isNight():
            scene riverside_crossing_construction_3_night
        else:
            scene riverside_crossing_construction_3
    elif quest38.status == 5 or get_task_completion_time("Rebuilding the Bridge") == 3:
        if isNight():
            scene riverside_crossing_construction_4_night
        else:
            scene riverside_crossing_construction_4
    else:
        if isNight():
            scene riverside_crossing_night
        else:
            scene riverside_crossing
    return

label riverside_crossing_loop:
    call showing_riverside_crossing from _call_showing_riverside_crossing_1
    $ rnd = renpy.random.random()
    if rnd < 0.2:
        "Around the crossing, you notice that there's a patch of small flowers nearby, you go and pick it up, it was a flax flower."
        $ addItem("Flax", inventory, 1)
        $ item_number = LookForItemNumber("Flax", inventory)
        if item_number == 1:

            "You put the flax flower in your bag, you now have [item_number] flax flower."
        else:

            "You put the flax flower in your bag, you now have [item_number] flax flowers."
    elif rnd < 0.4:
        "You look around the crossing, under the bright sun you see something tinted red in the bush, you went and pick it up. It was a red berry."
        $ addItem("Red Berry", inventory, 1)
        $ item_number = LookForItemNumber("Red Berry", inventory)
        if item_number == 1:

            "You put the red berry in your bag, you now have [item_number] red berry."
        else:

            "You put the red berry in your bag, you now have [item_number] red berries."
    elif rnd < 0.6:
        "You look around the crossing, under the bright sun you see something tinted blue in the bush, you went and pick it up. It was a blue berry."
        $ addItem("Blue Berry", inventory, 1)
        $ item_number = LookForItemNumber("Blue Berry", inventory)
        if item_number == 1:

            "You put the blue berry in your bag, you now have [item_number] blue berry."
        else:

            "You put the blue berry in your bag, you now have [item_number] blue berries."
    elif rnd < 0.8 and not spirespike_item.isDiscovered():
        "Walking around the crossing, you notice a small piece of paper on the ground, you pick it up and see that it's a clue for a hidden trinket."
        $ spirespike_item.discover()
    else:
        "You search around the area for a while, but there seem to be nothing worth noting nearby."

    jump main_riverside_crossing
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
