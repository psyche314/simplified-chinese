screen place_green_forest():
    zorder 10 tag place

    if quest37.status == True and quest43.status == True and goat_reconciliation == True:
        imagebutton:
            focus_mask "green_forest_goat_mask"
            idle "green_forest_goat"
            hover dayHover("green_forest_goat")
            action Return("Goat Guard")

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
        action Return("To Lusterfield")
    if ancient_tree.discovered == True:
        imagebutton:
            xalign 0.87
            yalign 0.67
            idle "lusterfield_arrow2"
            hover "lusterfield_arrow2_hover"
            style "footstep_button"
            action Return("To Ancient Tree")

screen place_summery_farmland():
    zorder 10 tag place

    imagebutton:
        xalign 0.99
        yalign 0.69
        idle "explore_idle"
        hover "explore_hover"
        action Return("Explore")
    imagebutton:
        xalign 0.50
        yalign 0.97
        idle "bedroom_arrow"
        hover "bedroom_arrow_hover"
        style "footstep_button"
        action Return("To Lusterfield")

    imagebutton:
        xalign 0.85
        yalign 0.84
        idle "lusterfield_arrow2"
        hover "lusterfield_arrow2_hover"
        style "footstep_button"
        action Return("To Grove")
    if quest29.status == True:
        imagebutton:
            xalign 0.50
            yalign 0.53
            idle "lusterfield_arrow1"
            hover "lusterfield_arrow1_hover"
            style "footstep_button"
            action Return("To Barn")

screen place_mossy_freshwater():
    zorder 10 tag place

    imagebutton:
        xalign 0.99
        yalign 0.69
        idle "explore_idle"
        hover "explore_hover"
        action Return("Explore")
    $ findingEversprout = next((x for x in discoveredtrinket if x.img == "Eversprout"), None)
    if findingEversprout != None and not isNight() and findingEversprout.discovered == True and eversprout_route == 2:
        imagebutton:
            xalign 0.07
            yalign 0.51
            idle "sprout_2"
            style "bushchime_button"
            action Return("Sprout2")
    imagebutton:
        xalign 0.57
        yalign 0.97
        idle "bedroom_arrow"
        hover "bedroom_arrow_hover"
        style "footstep_button"
        action Return("To Tree")

    if riverside_crossing.discovered == True:
        imagebutton:
            xalign 0.14
            yalign 0.72
            idle "ancienttree_arrow"
            hover "ancienttree_arrow_hover"
            style "footstep_button"
            action Return("To Crossing")
    if woodland_outpost.discovered == True:
        imagebutton:
            xalign 0.24
            yalign 0.32
            idle "lusterfield_arrow1"
            hover "lusterfield_arrow1_hover"
            style "footstep_button"
            action Return("To Outpost")
    if sundersilk_cascades.discovered == True:
        imagebutton:
            xalign 0.78
            yalign 0.23
            idle "lusterfield_arrow2"
            hover "lusterfield_arrow2_hover"
            style "footstep_button"
            action Return("To Waterfall")
screen place_woodland_outpost():
    zorder 10 tag place

    imagebutton:
        xalign 0.99
        yalign 0.69
        idle "explore_idle"
        hover "explore_hover"
        action Return("Explore")

    $ findingEversprout = next((x for x in discoveredtrinket if x.img == "Eversprout"), None)
    if findingEversprout != None and not isNight() and findingEversprout.discovered == True and eversprout_route == 4:
        imagebutton:
            xalign 0.71
            yalign 0.82
            idle "sprout_3"
            style "bushchime_button"
            action Return("Sprout3")
    imagebutton:
        xalign 0.57
        yalign 0.97
        idle "kingspawn_arrow"
        hover "kingspawn_arrow_hover"
        style "footstep_button"
        action Return("To Freshwater")
    if alchemists_cabin.discovered == True:
        imagebutton:
            xalign 0.88
            yalign 0.82
            idle "lusterfield_arrow2"
            hover "lusterfield_arrow2_hover"
            style "footstep_button"
            action Return("To Cabin")
    if kechioeren.discovered == True:
        imagebutton:
            xalign 0.18
            yalign 0.78
            idle "lusterfield_arrow1"
            hover "lusterfield_arrow1_hover"
            style "footstep_button"
            action Return("To Goat Tribe")
    if dark_forest.discovered == True:
        imagebutton:
            xalign 0.38
            yalign 0.68
            idle "sparklinglagoon_arrow"
            hover "sparklinglagoon_arrow_hover"
            style "footstep_button"
            action Return("To Dark Forest")
screen place_sparkling_lagoon():
    zorder 10 tag place

    imagebutton:
        xalign 0.99
        yalign 0.69
        idle "explore_idle"
        hover "explore_hover"
        action Return("Explore")
    imagebutton:
        xalign 0.99
        yalign 0.59
        idle "drink"
        hover "drink_hover"
        action Return("Drink")
    imagebutton:
        xalign 0.12
        yalign 0.77
        idle "kingspawn_arrow"
        hover "kingspawn_arrow_hover"
        style "footstep_button"
        action Return("To Tree")
    if damp_cave.discovered == True:
        imagebutton:
            xalign 0.32
            yalign 0.67
            idle "lusterfield_arrow1"
            hover "lusterfield_arrow1_hover"
            style "footstep_button"
            action Return("To Cave")
screen place_ancient_tree():
    zorder 10 tag place

    imagebutton:
        xalign 0.99
        yalign 0.59
        idle "axe_idle"
        hover "axe_hover"
        action Return("Chop")
    imagebutton:
        xalign 0.99
        yalign 0.69
        idle "explore_idle"
        hover "explore_hover"
        action Return("Explore")
    imagebutton:
        xalign 0.12
        yalign 0.74
        idle "ancienttree_arrow"
        hover "ancienttree_arrow_hover"
        style "footstep_button"
        action Return("To Forest")
    if sparkling_lagoon.discovered == True:
        imagebutton:
            xalign 0.87
            yalign 0.77
            idle "sparklinglagoon_arrow"
            hover "sparklinglagoon_arrow_hover"
            style "footstep_button"
            action Return("To Lagoon")
    if mossy_freshwater.discovered == True:
        imagebutton:
            xalign 0.37
            yalign 0.73
            idle "lusterfield_arrow1"
            hover "lusterfield_arrow1_hover"
            style "footstep_button"
            action Return("To Freshwater")
screen place_alchemists_cabin():
    zorder 10 tag place

    $ findingEversprout = next((x for x in discoveredtrinket if x.img == "Eversprout"), None)
    if findingEversprout != None and not isNight() and findingEversprout.discovered == True and eversprout_route == 6:
        imagebutton:
            xalign 0.82
            yalign 0.12
            idle "sprout_4"
            style "bushchime_button"
            action Return("Sprout4")
    imagebutton:
        xalign 0.99
        yalign 0.69
        idle "explore_idle"
        hover "explore_hover"
        action Return("Explore")
    imagebutton:
        xalign 0.68
        yalign 0.61
        idle "sparklinglagoon_arrow"
        hover "sparklinglagoon_arrow_hover"
        style "footstep_button"
        action Return("To Cabin")
    if woodland_outpost.discovered == True:
        imagebutton:
            xalign 0.57
            yalign 0.97
            idle "kingspawn_arrow"
            hover "kingspawn_arrow_hover"
            style "footstep_button"
            action Return("To Outpost")
screen place_damp_cave():
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
        idle "kingspawn_arrow"
        hover "kingspawn_arrow_hover"
        style "footstep_button"
        action Return("To Lagoon")
    imagebutton:
        xalign 0.57
        yalign 0.57
        idle "dungeon1_arrow"
        hover "dungeon1_arrow_hover"
        style "footstep_button"
        action Return("To Dungeon")

label main_green_forest:
    $ renpy.music.play(mForest, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ current_location = green_forest
    if isNight():
        scene forest_night
    else:
        scene forest
    with dissolve
    $ wilderness = True
    $ timenow.minute += 12
    $ timenow.passTime()
    show screen menu_buttons
    window hide
    call screen place_green_forest
    if _return == "Explore":
        jump green_forest_loop
    if _return == "Goat Guard":
        show green_forest_goat
        gt "Hey, you! What is your purpose of travel?"
        e "Just exploring!"
        gt "Oh, alright. You're that courier... I am sent here to guard over Lusterfield, so we just wanted to make sure no one suspicious enters."
        e "Alright, I get it! Thanks for the heads up!"
    if _return == "To Ancient Tree":
        jump main_ancient_tree
    if _return == "To Lusterfield":
        jump main_lusterfield01
    jump main_green_forest

label main_summery_farmland:
    $ current_location = summery_farmland
    $ renpy.music.play(mBarn, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    if isNight():
        scene summery_farmland_night
    else:
        scene summery_farmland
    with dissolve
    $ wilderness = True
    $ timenow.minute += 12
    $ timenow.passTime()
    show screen menu_buttons
    window hide
    call screen place_summery_farmland
    if _return == "Explore":
        jump summery_farmland_loop
    if _return == "To Lusterfield":
        jump main_lusterfield_range
    if _return == "To Barn":
        jump main_backyard_barn
    if _return == "To Grove":
        jump main_grove_of_harvest

    jump main_summery_farmland

label main_damp_cave:
    $ current_location = damp_cave
    $ renpy.music.play(mForest, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    if isNight():
        scene damp_cave
    else:
        scene damp_cave
    with dissolve
    $ wilderness = True
    $ timenow.minute += 12
    $ timenow.passTime()
    show screen menu_buttons
    window hide
    call screen place_damp_cave
    if _return == "Explore":
        jump damp_cave_loop
    if _return == "To Lagoon":
        jump main_sparkling_lagoon
    if _return == "To Dungeon":
        jump Damp_Cave_Enter
    jump main_damp_cave

label main_ancient_tree:
    $ current_location = ancient_tree
    if eversprout_route != 8:
        $ eversprout_route = 0
    $ renpy.music.play(mForest, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ wilderness = True
    $ timenow.minute += 12
    $ timenow.passTime()
    if isNight():
        scene ancienttree_night
    else:
        scene ancienttree
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_ancient_tree
    if _return == "Explore":
        jump ancient_tree_loop
    if _return == "To Forest":
        jump main_green_forest
    if _return == "To Lagoon":
        jump main_sparkling_lagoon
    if _return == "To Freshwater":
        jump main_mossy_freshwater
    if _return == "Chop":
        jump ancient_tree_chop
    jump main_ancient_tree
label main_alchemists_cabin:
    $ current_location = alchemists_cabin
    $ renpy.music.play(mForest, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    if eversprout_route == 5:
        $ eversprout_route = 6
    $ wilderness = True
    $ timenow.minute += 12
    $ timenow.passTime()
    if isMidnight():
        scene alchemistscabin
    elif isNight():
        scene alchemistscabin
    else:
        scene alchemistscabin
    if quest42.status == 3:
        hide screen menu_buttons
        jump Furkan_Rahim_Pact
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_alchemists_cabin
    if _return == "Explore":
        jump alchemists_cabin_loop
    if _return == "To Outpost":
        jump main_woodland_outpost
    if _return == "To Cabin":
        jump main_haskell_hut
    if _return == "Sprout4":
        $ eversprout_route = 8
        "Once more, you've discovered the same sprout, this time it's much bigger, with a yellowish fruit under the usual two leaves."
        "It has mostly blended in with the other firs on the tree, almost as if it belongs here."
        "You reach up to grab onto the sprout, and suddenly, a familiar voice catches your attention."
        show haskell normal with dissolve
        h "What do you think you're doing, kiddo."
        "It was Haskell, the old dragon walks up from his small hut."
        e "Uh... I was picking up herbs, can I not... do that?"
        "Haskell looks at the direction of your hand, a squirming sprout still bouncing around your palm."
        h "Did the goat shopkeeper send you here?"
        e "Well I was looking for a trinket, called eversprout, Gwyd gave me the clues to find it and I followed the fruit here."
        "The dragon sighs, he walks towards you until you're both under the fir trees."
        h "Ugh, what did he tell you exactly."
        e "He just sold me a scroll- Wait, do you know about the sprout?"
        "You loosen up your fist, and the sprout quickly bounces to Haskell's side."
        "He pats on the leaves for a moment, before letting it return to the bristling trees."
        h "Of course I do! The sprout's from my garden, helps with tending to the herbs and flowers."
        h "He's a budding spirit, one born just like the other soulful trinkets, but he has his own mind."
        e "I thought those three trinkets were all you know."
        h "It's not like I'll gladly let you take my garden tender and put it in a glass bottle, ugh..."
        "Haskell takes another sip, before he casually walks into the garden and returns with a sprout."
        h "Here, take it."
        e "Oh? What's this...?"
        h "One of the sprouts that the spirit has stayed with, it should invoke a similar effect as though it was one of the trinkets."
        h "The result is reduced, but just as spiritual as the real one."
        e "Thank you so much, Haskell."
        h "Well, next time Gwyddyon wants to sell you my own items, remember to stuff his mouth with his worthless crystals."
        h "Now, let me finish my tea, and don't try to look for the young sprout anymore, kiddo. He's going to be scared of you for a while."
        "You nod, before Haskell chuckles slightly and returns to his hut."
        $ addTrinket(eversprout_item, tinventory)
    jump main_alchemists_cabin
label main_woodland_outpost:
    $ current_location = woodland_outpost
    $ renpy.music.play(mForest, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    if eversprout_route == 3:
        $ eversprout_route = 4
    $ wilderness = True
    $ timenow.minute += 15
    $ timenow.passTime()
    if isNight():
        scene woodlandoutpost_night
    else:
        scene woodlandoutpost
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_woodland_outpost
    if _return == "Explore":
        jump woodland_outpost_loop
    if _return == "To Freshwater":
        jump main_mossy_freshwater
    if _return == "To Cabin":
        jump main_alchemists_cabin
    if _return == "To Dark Forest":
        jump main_dark_forest
    if _return == "Sprout3":
        $ eversprout_route = 5
        "Under the old outpost of the goats, you discover the hidden sprout once more, it wiggles as always, rhythm on the pace with the nature's frequency."
        e "Don't you fuckin run away again!"
        "You angrily catches it, this time the small sprout is trapped right in your palm."
        e "Haha, YES!"
        "The small sprout convulses, jiggling as if it was hurt by your force. Your eyes widen, and immediately relaxes your hand."
        "Suddenly it jumps off your hand, you try to catch it once more but as soon as it touches the ground, it has vanished once more."
        "You stomp the ground impatiently, it's unbelievable how it manipulated with your empathy just to escape."
        "But there's no time for your frustration, you should chase after it again. Just that the problem is, there's no way to know where it went..."
        jump main_woodland_outpost
    if _return == "To Goat Tribe":
        if quest20.status == 2:
            jump Lothar_Found_Goat_Tribe
        if quest10.status == 3:
            jump Kechioeren_Enter
        elif quest11.status == 3:
            scene kechioeren
            with dissolve
            show kari masked
            with dissolve
            "You walk over to the entrance of the goat tribe, two guards are standing there."
            "One of them immediately rushes inside, and a moment later, the general walks out towards you, still exhausted."
            k "Hey... Where's Furkan?"
            e "He's fine, he told me to ask your guards to take him back."

            "Kari looks at you with surprise."
            pause 0.5
            k "Oh?"
            k "Alright... Thanks, Courier."
            "You can sense a sliver of gratitude in his voice, even when he doesn't spell it out loud."
            k "You should get some rest, I'll take over now."
            "He hands you some paper."
            k "Here's some recipe I thought should prove useful to you."
            k "It's iron sword and axe."
            e "Ah, that sounds so great. Thanks a lot!"
            k "We'll talk later, both of us need to recover for a while."
            e "See you!"
            $ discoveredrecipe.append(ironswordrecipe)
            $ discoveredrecipe.append(ironaxerecipe)
            $ QuestFinish(quest11)
            jump main_woodland_outpost
        elif quest11.status != True:
            "You reach the gate of the goat tribe, the guards looks at you in confusion."
            "It seems that there's no one in charge of the goat tribe now."
            if kari_accompany:
                "The general is still in the cave, as you presume."
            else:
                "The general is taking his rest."
            "And the chief is still inside the cave."
            "You decide that the guards won't let you in, and you move on back to the main road."
            jump main_woodland_outpost
        else:

            jump main_kechioeren01
    jump main_woodland_outpost
label main_mossy_freshwater:
    $ current_location = mossy_freshwater
    $ renpy.music.play(mForest, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ wilderness = True
    $ timenow.minute += 15
    $ timenow.passTime()
    if eversprout_route == 1:
        $ eversprout_route = 2
    if isNight():
        scene mossy_freshwater_night
    else:
        scene mossy_freshwater
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_mossy_freshwater
    if _return == "Explore":
        jump mossy_freshwater_loop
    if _return == "To Tree":
        jump main_ancient_tree
    if _return == "To Outpost":
        jump main_woodland_outpost
    if _return == "To Waterfall":
        jump main_sundersilk_cascades
    if _return == "To Crossing":
        jump main_riverside_crossing
    if _return == "Sprout2":
        $ eversprout_route = 3
        "Just in the cave of the mossy river, you find the same sprout again, it wiggles again, convulsing with the flow of the water."
        "You walk towards the river bank, before it slips away from the grasp of your hand, and wiggles away again."
        e "Argh! How did it escape again?"
        "You turn your head left and right, there's no sign of which direction it had went, but you should chase after it before it disappears once more."
    jump main_mossy_freshwater

label main_sparkling_lagoon:
    $ current_location = sparkling_lagoon
    $ renpy.music.play(mForest, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ wilderness = True
    $ timenow.minute += 12
    $ timenow.passTime()
    if isNight():
        scene sparklinglagoon_night
    else:
        scene sparklinglagoon
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_sparkling_lagoon
    if _return == "Explore":
        jump sparkling_lagoon_loop
    if _return == "Drink":
        jump sparkling_lagoon_drink
    if _return == "To Tree":
        jump main_ancient_tree
    if _return == "To Cave":
        jump main_damp_cave
    jump main_sparkling_lagoon

label ancient_tree_chop:
    if isNight():
        scene ancienttree_night
    else:
        scene ancienttree
    $ chop_step = 0
    if pc.weapon != None:
        if pc.hp >= 20 and (LookForWpnType("Axe", inventory) or pc.weapon.wpn_type == "Axe"):
            $ chop_amount = renpy.random.randint(4, 5)
            $ chopped_wood = 0
            $ tree_amount = 0
            $ increasing = True
            call tree_chopping from _call_tree_chopping

            "You chop off some wood from a nearby tree. You have collected [chopped_wood] Wooden Log."
            if chopped_wood != tree_amount:
                $ lost_hp = (tree_amount - chopped_wood) * 10
                "You have lost [lost_hp] HP in total."
            $ addItem("Wooden Log", inventory, chopped_wood)
        elif pc.hp <= 10:
            "You don't have enough hp for you to keep draining your energy on chopping wood, you decide it is better for you to continue on your path."
        else:
            "You look through your bag, there's nothing for you to chop the wood except for your hand. You would probably need an axe for this occasion."

    jump main_ancient_tree

label tree_chopping:
    $ chop_size = max(int(renpy.random.randint(15, 30) / (tree_amount*0.4+1)), 5)
    $ chop_size_minimum = renpy.random.randint(4, 96-chop_size)
    $ chop_size_maximum = chop_size_minimum + chop_size
    $ move_speed = 50 + tree_amount * renpy.random.randint(5, 15)


    call screen precision_minigame()
    if _return >= chop_size_minimum - 2 and _return <= chop_size_maximum + 2:
        $ chopped_wood += 1
        play sound clickchop
    else:
        $ pc.hp -= 10
        if pc.hp <= 0:
            "You have lost too much hp to continue chopping wood."
            return
    $ tree_amount += 1
    if tree_amount >= chop_amount:
        return
    jump tree_chopping



init python:
    def chop_timing(step, pos, min, max):
        global chop_step
        global increasing
        if pos < min + 1:
            chop_step += 1
            increasing = True
        elif pos > max - 1:
            chop_step -= 1
            increasing = False
        if increasing:
            chop_step += 1
        else:
            chop_step -= 1

screen precision_minigame(item_image="wooden log", chop_number=chopped_wood, button_label=_("Chop")):
    frame:
        xalign 0.4
        yalign 0.5
        style "slot"
        add item_image
        if chop_number == chopped_wood:
            text "[chopped_wood]" style "invnumber_label"
        else:
            text chop_number style "invnumber_label"
    frame:
        xalign 0.6
        yalign 0.5
        xpadding 10
        ypadding 5
        style "coolframe"
        textbutton button_label style_prefix "pling" action Return(chop_step)

    $ minimum_pos = 960-110
    $ maximum_pos = minimum_pos + 100 * 1.9
    $ indicator_pos = int(minimum_pos+chop_step*1.9)

    timer 1.0/move_speed repeat True action Function(chop_timing, chop_step, indicator_pos, minimum_pos, maximum_pos)

    fixed:
        xalign 0.5
        yalign 0.5
        xmaximum 200
        ymaximum 38

        bar value StaticValue(chop_size_minimum,100) left_bar Frame("left_red", 3, 1.5) right_bar Frame("left_green", 3, 1.5)


        bar value StaticValue(chop_size_maximum,100) xalign 0.5 yalign 0.5 left_bar Frame("empty", 3, 1.5) right_bar Frame("left_red", 3, 1.5)

    add "bar_indicator":
        size (25, 58.25)
        xpos indicator_pos yalign 0.5


label sparkling_lagoon_drink:
    if isNight():
        scene sparklinglagoon_night
    else:
        scene sparklinglagoon
    if quest24.status == True and LookForItem("Minotaur Essence", inventory):
        menu:
            "What do you wish to do...?"
            "Mix the pond water with Minotaur's Essence":
                "You pour the minotaur's essence in the pond, drops and drops of the white liquid mixes with the water."
                "Soon, you see... the water clears up and a strange plant begin to surface from the water."
                if not devilssnare_item.discovered:
                    "You can feel the effect of the flower as soon as you touch it, it must be a trinket."
                    "You store it carefully in your bag. And thank the water before getting up."
                    $ devilssnare_item.discover()
                    $ addTrinket(devilssnare_item, tinventory)
                else:
                    "When you look closely, you realise it was just a herb of grace..."
                    "You put the plant in your bag and continue with your adventure."
                    $ addItem("Herb of Grace", inventory, 1)
            "Drink from the pond":
                pass

    if timenow.hour - 2 > lastDrink or dayDrink < timenow.day:
        if LookForItem("Wooden Bucket", inventory):
            $ lastDrink = timenow.hour
            $ dayDrink = timenow.day
            "You drink from the lagoon with your bucket, the refreshing power of the water recovered a portion of your HP and MP."
            $ pc.rest()
            $ pc.rest()
            $ pc.rest()
        else:

            "You look through your bag, nothing can hold enough water for you to drink, you realise that you need a water bucket. Discouraged, you continue on your track."
    else:
        "You look at the lagoon, your stomach is still full of water right now. You need to take some time before drinking from the lagoon again."
    jump main_sparkling_lagoon
label green_forest_loop:
    if isNight():
        scene forest_night
    else:
        scene forest
    $ rnd = renpy.random.random()
    if rnd < 0.2:
        if isNight():
            "You look around the green forest for a while, but there seem to be nothing worth noting nearby."
        else:

            "As you are searching through the forest, a green mass lunges itself into you from an innocent bush, covering you in slimy substance."
            "You struggle and flail your arms, flinging the mass away from you. It turns out to be a green slime as your vision becomes clear."
            jump slime_battle
    elif rnd < 0.45:
        "You look around the green forest, under the bright sun you see something tinted red in the bush, you went and pick it up. It was a red berry."
        $ addItem("Red Berry", inventory, 1)
        $ item_number = LookForItemNumber("Red Berry", inventory)
        if item_number == 1:

            "You put the red berry in your bag, you now have [item_number] red berry."
        else:

            "You put the red berry in your bag, you now have [item_number] red berries."
    elif rnd < 0.70:
        "You look around the green forest, under the bright sun you see something tinted blue in the bush, you went and pick it up. It was a blue berry."
        $ addItem("Blue Berry", inventory, 1)
        $ item_number = LookForItemNumber("Blue Berry", inventory)
        if item_number == 1:

            "You put the blue berry in your bag, you now have [item_number] blue berry."
        else:

            "You put the blue berry in your bag, you now have [item_number] blue berries."
    elif rnd < 0.85:
        if renpy.random.random() < 0.35 and ancient_tree.discovered == False:
            "As you walk around the forest, you discovered an abandoned dirt path covered with leaves, the path seems to be forgotten for a long while, except for a pair of footprint."
            "You walk along the trail, it takes you a few minutes to reach the end, where you see a giant ancient tree at the middle of it. You decide to check the surrounding area for a while."
            $ ancient_tree.discovered = True
            jump main_ancient_tree
        else:
            "You look around the green forest for a while, but there seem to be nothing worth noting nearby."
    else:
        "While you are walking through the forest, you feel as if there's something on your left foot, you look down, and realise it is a rock."
        $ addItem("Stone", inventory, 1)
        $ item_number = LookForItemNumber("Stone", inventory)
        if quest02.status == 2:
            e "It must be the rock... no, stone that Sebas asked me to collect."
            if item_number >= 3:
                e "I think I have enough ...stone now. I gotta go back and report to Sebas."
        "You put the stone into your bag, you now have [item_number] stones."

    jump main_green_forest
label summery_farmland_loop:
    if isNight():
        scene summery_farmland_night
    else:
        scene summery_farmland
    $ rnd = renpy.random.random()
    if rnd < 0.2:
        if (pc.weapon != None and pc.weapon.img == "Iron Scythe" ) or LookForItem("Iron Scythe", inventory):
            "You come across a barley field in the farmland, you use your scythe and pick up a crop of barley."
            $ addItem("Barley", inventory, 1)
            $ item_number = LookForItemNumber("Barley", inventory)
            "You put the barley in your bag, you now have [item_number] barleys."
        else:

            "You come across a barley field in the farmland, but you need a scythe to harvest them."
    elif rnd < 0.4 and not isNight():
        "You run into a scarecrow on the field, it seems to not be aware of your presence."
        menu:
            "Do you wish to fight the scarecrow?"
            "Fight with the scarecrow":
                jump scarecrow_battle
            "Leave it alone":
                pass
    elif rnd < 0.5 and not isNight():
        "You run into a landshark on the field, it seems to not be aware of your presence."
        jump landshark_battle
    elif rnd < 0.7:
        if renpy.random.random() < 0.45 and knightcuissesrecipe not in discoveredrecipe:
            "Along the farm, you found a leftover paper detailing the process to make a... Knight Cuisses."
            "{i}To make the cuisses of the renowned knight, use 4 pieces of iron, 2 pieces of soft fabric and a strap.{/i}"
            msg "New Recipe learned, check out Rahim's Workstation for more detail."
            $ discoveredrecipe.append(knightcuissesrecipe)
        else:
            "You search around the area for a while, but there seem to be nothing worth noting nearby."
    else:
        if slime2_dp[1] == 2 and quest26.status == False:
            jump Wuldon_Meeting_Field
        "You search around the area for a while, but there seem to be nothing worth noting nearby."

    jump main_summery_farmland
label ancient_tree_loop:
    $ trap_meet_chance = 0.1/(1+2.718**(-0.5*(pc.agi-8)))
    if isNight():
        scene ancienttree_night
    else:
        scene ancienttree
    $ rnd = renpy.random.random()
    if rnd < 0.2:
        if quest06.status == True and not isNight() and guard_tree == True:
            "As you are searching through the area, you hear a weak bell ringing from behind the trees behind you. You turn back and look around, but there's no one."
            "Another series of bell sound render you defenseless. Suddenly, a horned figure jump into the center of your sight, holding a wooden spear."
            gt "Insolence, in the name of our lord! I will absolve you of your impure fate!"
            $ goat_num = 1
            jump goathuntsman_battle
        else:

            "You search around the area for a while, but there seem to be nothing worth noting nearby."

    elif rnd < 0.4 - trap_meet_chance and pc.hp > 20:
        "When you roam around in the forest area, you suddenly feel a sharp pain in your left leg. It feels as if a thousand needles are puncturing into your leg."
        "The weight of the trap instantly leads you to trip and fall on the ground. You look into it and realise you stepped into a bear trap."
        "It took you a few minutes to get rid of the trap, but the wound leaves behind a few drops of blood on the grass. Your HP drops by 20."
        $ pc.restore(hp = -20)
    elif rnd < 0.5:
        "You look around the ancient tree, under the bright sun you see something tinted yellow in the bush, you went and pick it up. It was a golden berry."
        $ addItem("Golden Berry", inventory, 1)
        $ item_number = LookForItemNumber("Golden Berry", inventory)
        if item_number == 1:

            "You put the golden berry in your bag, you now have [item_number] golden berry."
        else:

            "You put the golden berry in your bag, you now have [item_number] golden berries."

    elif rnd < 0.8:
        if renpy.random.random() < 0.8 and seen_furkan == False:
            $ seen_furkan = True
            jump Furkan_First_Meet
        elif seen_furkan == True and quest06.status != True:
            jump Furkan_Second_Meet
        elif renpy.random.random() < 0.5 and mossy_freshwater.discovered == False:
            "You have wandered around the lagoon for a while, but there doesn't seem to be anything noticeable in particular, until you see a damp river in the middle of the forest."
            "The sight is a breathtaking experience as you can even smell the freshness of the flowing water. The grassy scent of the moss gives you an insurmountable amount of energy."
            "You take out your map and mark the spot. This is the Mossy Freshwater."
            $ mossy_freshwater.discovered = True
            jump main_mossy_freshwater
        else:
            "You search around the area for a while, but there seem to be nothing worth noting nearby."
    else:
        if renpy.random.random() < 0.45 and sparkling_lagoon.discovered == False:
            "You have wandered around the ancient tree for a while, and just before you decide to return, you notice a blue aura in the forest far away."
            "From where you stand, it looks like something with magical essence. You slowly walk towards the area, and discovered a bright blue lagoon in front of you."
            $ sparkling_lagoon.discovered = True
            jump main_sparkling_lagoon
        else:
            "You search around the area for a while, but there seem to be nothing worth noting nearby."

    jump main_ancient_tree
label sparkling_lagoon_loop:
    if isNight():
        scene sparklinglagoon_night
    else:
        scene sparklinglagoon
    $ rnd = renpy.random.random()
    if rnd < 0.2:
        "Around the lagoon, you notice that there's a patch of small flowers nearby, you go and pick it up, it was a flax flower."
        $ addItem("Flax", inventory, 1)
        $ item_number = LookForItemNumber("Flax", inventory)
        if item_number == 1:

            "You put the flax flower in your bag, you now have [item_number] flax flower."
        else:

            "You put the flax flower in your bag, you now have [item_number] flax flowers."
    elif rnd < 0.4:
        "You look around the sparkling lagoon, under the bright sun you see something tinted red in the bush, you went and pick it up. It was a red berry."
        $ addItem("Red Berry", inventory, 1)
        $ item_number = LookForItemNumber("Red Berry", inventory)
        if item_number == 1:

            "You put the red berry in your bag, you now have [item_number] red berry."
        else:

            "You put the red berry in your bag, you now have [item_number] red berries."
    elif rnd < 0.6:
        "You look around the sparkling lagoon, under the bright sun you see something tinted blue in the bush, you went and pick it up. It was a blue berry."
        $ addItem("Blue Berry", inventory, 1)
        $ item_number = LookForItemNumber("Blue Berry", inventory)
        if item_number == 1:

            "You put the blue berry in your bag, you now have [item_number] blue berry."
        else:

            "You put the blue berry in your bag, you now have [item_number] blue berries."
    elif rnd < 0.8:
        if renpy.random.random() < 0.45 and woodenbucketrecipe not in discoveredrecipe:
            "Along the lagoon, you found a leftover paper detailing the process to make a bucket."
            "It says making a wooden bucket requires 6 Wooden Logs and 4 Slime Balls. You mark down the recipe on your journal."
            msg "New Recipe learned, check out Rahim's Workstation for more detail."
            $ discoveredrecipe.append(woodenbucketrecipe)
        else:
            "You search around the area for a while, but there seem to be nothing worth noting nearby."
    else:
        "You search around the area for a while, but there seem to be nothing worth noting nearby."

    jump main_sparkling_lagoon
label mossy_freshwater_loop:
    if isNight():
        scene mossy_freshwater_night
    else:
        scene mossy_freshwater
    $ rnd = renpy.random.random()
    if rnd < 0.2:
        "Around the river, you wander and pick up a certain plant, it was a Reed."
        $ addItem("Reed", inventory, 1)
        $ item_number = LookForItemNumber("Reed", inventory)
        if item_number == 1:

            "You put the reed in your bag, you now have [item_number] Reed."
        else:

            "You put the reed in your bag, you now have [item_number] Reeds."
    elif rnd < 0.4:
        "Along the river bank, you notice that there's a patch of small flowers nearby, you go and pick it up, it was a sage."
        $ addItem("Sage", inventory, 1)
        $ item_number = LookForItemNumber("Sage", inventory)
        if item_number == 1:

            "You put the sage flower in your bag, you now have [item_number] sage flower."
        else:

            "You put the sage flower in your bag, you now have [item_number] sage flowers."
    elif rnd < 0.6:
        if smalltrowelrecipe not in discoveredrecipe:
            "You walk on the side of the river, and notice something shiny... it was a recipe."
            "You quickly approach and pick it up. It says..."
            "{i}...To make a trowel... craft with two slimeballs and two pieces of wood.{/i}"
            "...You put the notes away, it seems you've learnt how to make a trowel."
            $ discoveredrecipe.append(smalltrowelrecipe)
        elif not riverside_crossing.discovered:
            "After walking along the river for a while, you decide to walk downstream along the river."
            "It takes a long time for you to explore the forest as the river water splashes against your legs."
            "And soon, you notice an abandoned bridge that marks the abrupt end of the river, if not counting all the flood surrounding this location."
            "You take out your map and check your surrounding, this place must be the riverside crossing."
            $ riverside_crossing.discovered = True
            jump main_riverside_crossing
        elif quest26.status == 2 and not isNight():
            jump Wuldon_Meeting_River
        else:
            "You search around the area for a while, but there seem to be nothing worth noting nearby."
    elif rnd < 0.8:
        "You look into the river and found something grainy under the water."
        if not callInventoryItem("Small Trowel", "Weapon"):
            "You use your trowel and soon dig up a piece of clay. You carefully store it in your bag."
            $ addItem("Clay", inventory, 1)
            $ item_num = LookForItemNumber("Clay", inventory)
            "You now have [item_num] pieces of clay."
        else:
            "You try to dig through the mud with your bare hand... but to no avail, it seems to not work."
            "You decide to move on, maybe you need something small that can dig..."
    elif rnd < 0.85 and quest24.status == True and weepingwillow_item not in tinventory and weepingwillow_item not in pc.trinket and isNight():
        "Under the river bed, you found something glowing faintly, hidden deep between the rocks."
        if not callInventoryItem("Small Trowel", "Weapon"):
            "You use the trowel you brought with you, and dig through the smooth sand and mud underwater."
            "Soon, the hole becomes deep enough that you notice a branch glowing blue."
            "With a little push, you pull out the branch, and feel a powerful aura coursing through your body..."
            "It must be a trinket."
            "You carefully put it in your bag. And step away from the water."
            $ addTrinket(weepingwillow_item, tinventory)
        else:
            "You try to dig through the mud with your bare hand... but to no avail, it seems to not work."
            "You decide to move on, maybe you need something small that can dig..."
    else:

        if renpy.random.random() < 0.3 and woodland_outpost.discovered == False:
            "After walking along the river for a while, you decide to climb upstream and explore the forest above."
            "As soon as you peek up, you see a giant red flag in front of you, it was an old abandoned settlement that seemed to be build by the goats."
            "You take out your map and mark the location, this place must be the woodland outpost."
            $ woodland_outpost.discovered = True
            jump main_woodland_outpost
        elif renpy.random.random() < 0.5 and fabricrecipe not in discoveredrecipe:
            "After walking along the river for a while, you take a rest on the slippery rock..."
            "Ouch!"
            "There's something under your butt, but luckily it's just a small note..."
            "{i}HOW TO MAKE SOFT FABRIC...{/i}"
            "It's a recipe for soft fabric, you put it aside, maybe it'll be useful when you go back to Rahim's workshop."
            $ discoveredrecipe.append(fabricrecipe)
        elif renpy.random.random() < 0.5 and sundersilk_cascades.discovered == False:
            "After walking along the river for a while, you decide to travel upstream."
            "You follow the river bank and walk opposite to where the water goes, you ascend and climb until you see a huge waterfall."
            "It seems you've arrived to the Sundersilk Cascades, you talk out your map and mark the location."
            $ sundersilk_cascades.discovered = True
            jump main_sundersilk_cascades
        else:
            "You search around the area for a while, but there seem to be nothing worth noting nearby."

    jump main_mossy_freshwater
label woodland_outpost_loop:
    if isNight():
        scene woodlandoutpost_night
    else:
        scene woodlandoutpost
    $ rnd = renpy.random.random()
    if rnd < 0.2:
        if not isNight():
            "While you are exploring the outpost, a shade of a giant brown creature lunges itself towards your side. You instantly get pushed on the ground."
            "You can feel the brown figure's armor clashing against your body, you struggle for a while before getting off the creature."
            "When you try to stand up and get a clear vision of the figure, you found out that he is a buggbear, he is holding his mace, growling angrily towards you."
            jump buggbear_battle
        else:

            "You search around the area for a while, but there seem to be nothing worth noting nearby."
    elif rnd < 0.4:
        if quest08.status == False and not isNight():
            jump Haskell_First_Meet
        else:
            "You search around the area for a while, but there seem to be nothing worth noting nearby."
    elif rnd < 0.5:
        if lothar_argue == 1 and quest10.status == True and quest11.status == False and isNight():
            "As you look around the woodland, you notice there's an unusual shadow at the peripheral of your sight."
            "You turn to the figure, its mass encapsulating your view. You notices its antler, and the eyes behind its mask."
            "The sight is... familiar in some twisted way, you feel like you have been in this situation before."
            "Stranded at night in the forest, being chased by a mysterious figure."
            "The figure approaches... you feel your muscles tense up. You are so ready to escape at any moment..."
            show kari masked
            with dissolve
            my "..."
            my "Who, are you?"
            e "Huh?"
            "Instead of the unintelligible languages in your memory, you hear a young voice coming out of the figure."
            "This deer, is bright in colour, and holding a scepter in his hand."
            e "Uhmmm... I'm [e]."
            my "Where are you from... and.. why are you here... at the middle of the night..."
            e "I'm from Lusterfield. I was just exploring the area."
            e "You... reminded me of someone."
            my "W-what?"
            e "The demon that sent me here."
            my "So, you are that courier."
            e "Hmm?"
            my "The courier from Lusterfield, Chief told me about you."
            my "I reckon you asked about some buddy of yours, Chime."
            e "Y-yes...?"
            my "Where's Chief now...?"
            e "W-what chief?"
            my "Furkan... You saw him before, he saw you before."
            my "Where is he..."
            e "Uhm, I don't know."
            my "Look, any information you know, you shall spill your beans. Did the Lusterfolks take him?"
            e "No, I'm sure no one would dare to kidnap your chief."
            e "But... I do think of one thing."
            my "Huh?"
            e "I did met a golem... that big."
            my "A golem?"
            e "It's full of moss, right over there."
            "You point at the river."
            my "..."
            my "I think I know where he is..."
            my "The damp cave."
            e "Huh?"
            my "Come on, we should go..."
            e "Me?"
            my "I need a hand."
            e "Really? I don't even know you."
            my "I know you, You... you're coming with me either way, courier."
            e "..."
            $ kari_accompany = True
            $ kari_battle_lose = 10
            "You and the mysterious figure wait for the sun to rise before proceeding."
            if timenow.hour < 7:
                $ timenow.hour = 7
            else:
                $ timenow.hour = 7
                $ timenow.day += 1
            $ QuestBegin(quest11)
            $ quest11.qProgress(__("Visit the Damp Cave"))
            jump Kari_Adventure
        elif quest19.status == 2 and not isNight():
            jump Furkan_Meet_Flower
        else:
            "You search around the area for a while, but there seem to be nothing worth noting nearby."

    elif rnd < 0.8:
        if dark_forest.discovered == False and rnd < 0.9:
            $ dark_forest.discovered = True
            "After walking along the forest for a while, you decide to go deeper into the forest."
            "You discovered that the tree seems to be denser than before, almost covering the sky above."
            jump main_dark_forest
        else:
            "You search around the area for a while, but there seem to be nothing worth noting nearby."
    else:
        if quest19.status == True or quest24.status != False:
            "Around the outpost, you remember the specific bush from Furkan and pick up a certain plant, it was a Chrysanthemum."
            $ addItem("Chrysanthemum", inventory, 1)
            $ item_number = LookForItemNumber("Chrysanthemum", inventory)
            if item_number == 1:

                "You put the flower in your bag, you now have [item_number] Chrysanthemum."
            else:

                "You put the flower in your bag, you now have [item_number] Chrysanthemums."
        else:

            "You search around the area for a while, but there seem to be nothing worth noting nearby."
    jump main_woodland_outpost
label damp_cave_loop:
    if isNight():
        scene damp_cave
    else:
        scene damp_cave
    $ rnd = renpy.random.random()
    if rnd < 0.2:

        "You search around the area for a while, but there seem to be nothing worth noting nearby."
    elif rnd < 0.4:

        "You search around the area for a while, but there seem to be nothing worth noting nearby."
    elif rnd < 0.6:
        "You search around the area for a while, but there seem to be nothing worth noting nearby."
    elif rnd < 0.8:
        "You search around the area for a while, but there seem to be nothing worth noting nearby."
    else:
        "You search around the area for a while, but there seem to be nothing worth noting nearby."

    jump main_damp_cave
label alchemists_cabin_loop:
    if isMidnight():
        scene alchemistscabin
    elif isNight():
        scene alchemistscabin
    else:
        scene alchemistscabin
    $ rnd = renpy.random.random()
    if rnd < 0.15:
        "Around the cabin, you wander and pick up a certain plant from the garden, it was a Hemp."
        $ addItem("Hemp", inventory, 1)
        $ item_number = LookForItemNumber("Hemp", inventory)
        if item_number == 1:

            "You put the hemp in your bag, you now have [item_number] hemp."
        else:

            "You put the hemp in your bag, you now have [item_number] hemps."
    elif rnd < 0.25:
        "Around the cabin, you wander and pick up a certain plant from the garden, it was a Herb of Grace."
        $ addItem("Herb of Grace", inventory, 1)
        $ item_number = LookForItemNumber("Herb of Grace", inventory)
        if item_number == 1:

            "You put the herb of grace in your bag, you now have [item_number] herb of grace."
        else:

            "You put the herb of grace in your bag, you now have [item_number] herb of grace."
    elif rnd < 0.6:
        if quest26.status == 3 and not isNight():
            jump Wuldon_Meeting_Haskell
        else:
            "You search around the area for a while, but there seem to be nothing worth noting nearby."

    elif rnd < 0.8:
        "Around the cabin, you wander and pick up a certain plant, it was a Rosemary."
        $ addItem("Rosemary", inventory, 1)
        $ item_number = LookForItemNumber("Rosemary", inventory)
        if item_number == 1:

            "You put the Rosemary in your bag, you now have [item_number] Rosemary."
        else:

            "You put the Rosemary in your bag, you now have [item_number] Rosemarys."
    else:
        "Around the cabin, you wander and notice a small bump on the ground, you dig it up.. and it is a piece of ginger."
        $ addItem("Ginger", inventory, 1)
        $ item_number = LookForItemNumber("Ginger", inventory)
        if item_number == 1:

            "You put the ginger in your bag, you now have [item_number] ginger."
        else:

            "You put the ginger in your bag, you now have [item_number] gingers."

    jump main_alchemists_cabin
label scene_slime_sex:
    scene black
    with fade
    if _in_replay:
        show screen Replayexit
    "Your consciousness lingers. How could this mere slime defeat you in such a humiliating fashion. You clutch at the grass, praying that the slime would leave you alone."
    "But it didn't."
    "Instead, the slime slithers towards you. You can sense its presence gets closer and closer every second, until it makes contact with your fur."
    "You feel something cold slide on your arm, its path leaves a coat of slimy residue."
    "You can do nothing but to watch it wrap around your arms, your body convulse slightly at the touch of the slime."
    "The slime continues assaulting your helpless body, its appendage binds your arm tighter and tighter while the rest travels across your body, allowing your arms little extent of movement."
    "There's nothing you can do to fight the slime forcing you down, nor can you resist the urge to squirm and struggle under its control, you whimper quietly, praying that it would retreat the next second."
    "You try to push the viscous substance away from you but it only gets firmer, The more you struggle, the easier it becomes to accomodate its advance, it quickly slides from your bare chest to your lower abdomen."
    scene slimelose101
    with fade
    "Effortlessly, the slime had reached your loincloth, you can already feel the cold sensation of the dribbling mass through the thin fabric, your cock twitches in response."
    e "W-what... are you doing..."
    "[e] feel increasingly sensitive as your private part is assaulted by the mere slime. You thrash your arm in hope of fighting against it, but they had already been held in place tightly."
    "You try to scoot backward, but your body refuses to obey your command. Instead, you are forced to endure the invasion as the slime climbs along the cover of your cock."
    e "A-ahhhhh...."
    "For a second, you imagine it would continue towards your legs, but as soon as the slime slides itself under your loincloth, you realise what it is doing."
    scene slimelose102
    with fade
    "You had never thought about what it is like, to have someone, or something directly touch your genitals like that, the slime is clearly alive, you can feel it pulses on your cock, ready for the next attack."
    "Suddenly, the slime had engulfed your whole cock, leaving no space around it. As the pressure around your cock increases, you groan loudly, fearing for what it has in store for you."
    e "H-ahhhhh.... no... g-get off me!"
    "The only thing you can do is to look, you are but a bystander of whatever is happening to your body. No matter how hard you strain, you can't prevent the thing from going wherever it wants."
    "You shake your head. How would other people think if they see you like this, lying on the grass, being taken controll by a mere slime."
    "The sensation is haunting, sending your brain all the wrong signals that you might be enjoying this."
    e "Noo."
    "You try to resist the feeling of getting sexually aroused, but the instinct inside your head is telling you to relax, and embrace the sensation."
    scene slimelose103
    with fade
    "The slime begins to move up and down in a regular pace. Your body tenses up, your cock is getting harder and harder as each pulse shoots through your mind."
    "The squishy noises that the slime makes made you shudder, your cock is throbbing under the touch of a soft rubbery texture. You can feel the slime is experimenting with your body, twisting and turning against your member."
    "It continues different movement for a while, until the sexual thoughts had overwhelmed your mind. You can think about nothing but the feeling of the gooey creature on your cock. It feels... oddly amazing."
    e "Ahhhh- A-hhhh."
    "You squeeze shut your eyes tightly, hoping to avoid witnessing the final indignity that awaits you. But the pressure continues unabated until the slime on your cock begins to convulse."
    "With each throb you are getting closer to climax. Your body trembles in agony as you lay there helpless. You feel like crying out loud, that you shouldn't enjoy this so much, but you did."
    e "I- I think... I'm... no I c-can't.... S-stop this."
    with vpunch
    "You know you are not thinking rationally, but you can't help but to submit under the grasp of the creature, watching it bouncing on your cock. The only thing you can sense is the pressure building up, waiting to explode."
    scene white
    pause .1
    scene black
    with vpunch
    e "Ha-aaaaaagh!!!"
    with flash
    scene slimelose104
    with dissolve
    with vpunch
    "You cannot hold yourself anymore, your mind shut down under the assault of pleasure and pain. Your cock twitch for one last time before you ejaculates ropes and ropes of cum all over your body."
    "You can feel your own cum flowing everwhere, load after load of pent up lust released all at once, you can even feel some landed on your tongue, your brain can no longer function normally."
    "Your cock remains stiff. The slime seems to be satisfied with your performance, but it doesn't move, instead the mass continues to encapsulate your member, even after the fact that you have already came."
    "You breath heavily, you cannot imagine seeing yourself being brought to your knees and forced to cum like this. Your chest, arms and thighs are all covered with your own cum. some even drizzle on the slime."
    "A short while after, you can feel the slime had assimilated enough samples of your cum. It retreated slowly, releasing its grip on your arm."
    "Before you see it leaves, you had already exhausted all your energy after the devious act, you collapse again on the grass floor, this time your consciousness fades as well."
    $ pc.lust = 0
    if _in_replay:
        $ renpy.end_replay()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
