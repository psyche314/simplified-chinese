

screen place_kechioeren01():
    zorder 10 tag place

    imagebutton:
        xalign 0.57
        yalign 0.97
        idle "bedroom_arrow"
        hover "bedroom_arrow_hover"
        style "footstep_button"
        action Return("To Outpost")
    imagebutton:
        xalign 0.82
        yalign 0.89
        idle "lusterfield_arrow2"
        hover "lusterfield_arrow2_hover"
        style "footstep_button"
        action Return("To Kechioeren02")
    imagebutton:
        xalign 0.60
        yalign 0.59
        idle "sparklinglagoon_arrow"
        hover "sparklinglagoon_arrow_hover"
        style "footstep_button"
        action Return("To Cauldron")
    imagebutton:
        xalign 0.08
        yalign 0.83
        idle "ancienttree_arrow"
        hover "ancienttree_arrow_hover"
        action Return("To Training Ground")
    if quest37.status == True and quest43.status == True and goat_reconciliation == True:
        if isNight():

            imagebutton:
                focus_mask "kechioeren_courier_office_mask"
                idle "kechioeren_courier_office_night"
                hover nightHover("kechioeren_courier_office_night")
                action Return("Courier Office")
        else:
            imagebutton:
                focus_mask "kechioeren_courier_office_mask"
                idle "kechioeren_courier_office_day"
                hover dayHover("kechioeren_courier_office_day")
                action Return("Courier Office")


screen place_kechioeren02():
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
        action Return("To Kechioeren01")
    imagebutton:
        xalign 0.31
        yalign 0.78
        idle "sparklinglagoon_arrow"
        hover "sparklinglagoon_arrow_hover"
        style "footstep_button"
        action Return("To Conference")
screen place_kechioeren_training_ground():
    zorder 10 tag place

    imagebutton:
        xalign 0.57
        yalign 0.97
        idle "bedroom_arrow"
        hover "bedroom_arrow_hover"
        style "footstep_button"
        action Return("To Kechioeren01")
    if kari_location == "kechioeren_training_ground":
        imagebutton:
            xalign 0.26
            yalign 0.82
            idle "karit_idle"
            hover "karit_hover"
            action Return("Kari")
    if not isNight():
        imagebutton:
            xalign 0.96
            yalign 0.5
            idle "goatsoldier2_idle"
            hover "goatsoldier2_hover"
            action Return("Goat2")
        imagebutton:
            xalign 0.77
            yalign 0.93
            idle "goatsoldier1_idle"
            hover "goatsoldier1_hover"
            action Return("Goat1")

screen place_kechioeren_conference():
    tag place
    zorder 10

    imagebutton:
        xalign 0.67
        yalign 0.97
        idle "bedroom_arrow"
        hover "bedroom_arrow_hover"
        style "footstep_button"
        action Return("To Kechioeren02")
    if furkan_dialogues.get("Loupe Gem", False) != False:
        if isNight():
            imagebutton:
                focus_mask "kechioeren_conference_loupe"
                idle "kechioeren_conference_loupe_repaired_night"
                hover dayHover("kechioeren_conference_loupe_repaired_night")
                action Return("Loupe Gem")
        else:
            imagebutton:
                focus_mask "kechioeren_conference_loupe"
                idle "kechioeren_conference_loupe_repaired"
                hover dayHover("kechioeren_conference_loupe_repaired")
                action Return("Loupe Gem")
    else:
        if isNight():
            imagebutton:
                focus_mask "kechioeren_conference_loupe"
                idle "kechioeren_conference_loupe_night"
                hover dayHover("kechioeren_conference_loupe_night")
                action Return("Loupe")
        else:
            imagebutton:
                focus_mask "kechioeren_conference_loupe"
                idle "kechioeren_conference_loupe"
                hover dayHover("kechioeren_conference_loupe")
                action Return("Loupe")

    if furkan_dialogues.get("Scroll Keepsake", False) == False:
        add "kechioeren_conference_scroll"

    if kari_location == "kechioeren_conference":
        imagebutton:
            focus_mask "kari_idle"
            idle "kari_idle"
            hover "kari_hover"
            action Return("Kari")
    if furkan_location == "kechioeren_conference":
        imagebutton:
            focus_mask "furkan_idle"
            idle "furkan_idle"
            hover "furkan_hover"
            action Return("Furkan")

    if furkan_dialogues.get("Loupe Gem", False) == False:
        use conference_gem_puzzle

default conference_loupe_x = 150
default conference_loupe_y = 660
default conference_gems = {"conference_gem": "empty_gem", "conference_gem_red": "empty_gem", "conference_gem_blue": "empty_gem"}
default furkan_dialogues = {}

init python:
    def gem_dragged(drags, drop):
        if drop and drop.drag_name == "conference_loupe" and abs(drags[0].x - conference_loupe_x) < 50 and abs(drags[0].y - conference_loupe_y) < 50:
            drags[0].snap(conference_loupe_x, conference_loupe_y, delay=0.5)
        
        else:
            if drags[0].x > 1750:
                gem_drop_floor = config.screen_height - renpy.random.randint(180, 250)
            elif drags[0].x < 300 or drags[0].x > 1300:
                gem_drop_floor = config.screen_height - renpy.random.randint(60, 160)
            elif drags[0].x < 550 or drags[0].x > 1050:
                gem_drop_floor = config.screen_height - renpy.random.randint(140, 180)
            else: 
                gem_drop_floor = config.screen_height - renpy.random.randint(160, 350)
            drags[0].snap(drags[0].x, gem_drop_floor, delay=(abs(gem_drop_floor-drags[0].y)/1000.0), warper=_warper.easeout_quad)

    def gem_activated(drags):
        renpy.restart_interaction()
        if drags[0].drag_name == "conference_gem":
            conference_gems["conference_gem"] = "kechioeren_conference_gem"
        elif drags[0].drag_name == "conference_gem_red":
            conference_gems["conference_gem_red"] = "kechioeren_conference_gem_red"
        elif drags[0].drag_name == "conference_gem_blue":
            conference_gems["conference_gem_blue"] = "kechioeren_conference_gem_blue"

    def gem_snapped(drag, x, y, done):
        if done:
            if x == conference_loupe_x and y == conference_loupe_y:
                furkan_dialogues["Loupe Gem"] = drag.drag_name
                renpy.hide_screen("conference_gem_puzzle")
                renpy.jump("kechioeren_gem_finished")

screen conference_gem_puzzle():
    draggroup:
        drag:
            child "empty"
            drag_name "conference_loupe"
            draggable False
            droppable True

            xpos 0.06 ypos 0.621

        drag:
            child conference_gems["conference_gem"]
            drag_name "conference_gem"
            droppable False
            draggable True
            activated gem_activated
            dragged gem_dragged
            snapped gem_snapped

            xpos 0.725 ypos 0.60

        drag:
            child conference_gems["conference_gem_red"]
            drag_name "conference_gem_red"
            droppable False
            draggable True
            activated gem_activated
            dragged gem_dragged
            snapped gem_snapped

            xpos 0.845 ypos 0.735

        drag:
            child conference_gems["conference_gem_blue"]
            drag_name "conference_gem_blue"
            droppable False
            draggable True
            activated gem_activated
            dragged gem_dragged
            snapped gem_snapped
            xpos 0.745 ypos 0.643


label kechioeren_gem_finished:
    "You dropped the gem into the loupe, and it fits perfectly!"
    "Perhaps now you can use it..."
    jump main_kechioeren_conference

label kechioeren_loupe_gem:
    hide screen place_kechioeren_conference
    if furkan_dialogues.get("Loupe Gem") == "conference_gem_blue":
        show conference_afterimage
    call screen kechioeren_loupe_gem_screen

    if _return == "Loupe":
        show screen kechioeren_loupe_gem_screen

        menu:
            "What do you wish to do?"
            "Remove the gem":
                "You unlodge the gem from the loupe, and placed it back into where it belonged."
                $ furkan_dialogues["Loupe Gem"] = False
            "Put down the loupe":
                pass
        hide screen kechioeren_loupe_gem_screen
        scene black with dissolve
        jump main_kechioeren_conference
    if _return == "Scroll":
        $ furkan_dialogues["Scroll Keepsake"] = True
        show screen kechioeren_loupe_gem_screen
        "You pick up the scroll under the table, there seem to be some old stains on it that you could only see under the green gem."
        "Patting away the dust, you suddenly feel a sense of familiarity wash over you, as if you have seen this scroll before, or you've written it yourself."
        e "Is this... Furkan's?"
        "You feel the scroll is calling out to you, and so you decide to keep it."
        msg "The stained scroll keepsake is added to your inventory. You can use the item to experience its past."

        $ addItem("Stained Scroll", inventory, 1)

    jump kechioeren_loupe_gem


image conference_afterimage_loop:
    "kechioeren_conference_afterimage" with dissolve
    pause 0.25
    "kechioeren_conference_afterimage2" with dissolve
    pause 0.25
    repeat 3

image conference_afterimage:
    "empty" with dissolve
    pause 7.0
    "conference_afterimage_loop"
    pause 3.0
    "empty" with dissolve
    pause 9.0
    repeat

screen kechioeren_loupe_gem_screen():
    if isNight():
        $ conference_image = "kechioeren_conference_night"
    else:
        $ conference_image = "kechioeren_conference"
    $ loupe_gem = furkan_dialogues.get("Loupe Gem", None)
    $ colourTint = '#ffffff'
    if loupe_gem == "conference_gem":
        $ colourTint = '#6dbaa7'
    elif loupe_gem == "conference_gem_red":
        $ colourTint = '#e290c8'
    elif loupe_gem == "conference_gem_blue":
        $ colourTint = '#546fc2'
    add Transform(conference_image, matrixcolor=TintMatrix(colourTint))
    if isNight():
        imagebutton:
            focus_mask "kechioeren_conference_loupe"
            idle Transform("kechioeren_conference_loupe_repaired_night", matrixcolor=TintMatrix(colourTint))
            hover dayHover(Transform("kechioeren_conference_loupe_repaired_night", matrixcolor=TintMatrix(colourTint)))
            action Return("Loupe")
    else:
        imagebutton:
            focus_mask "kechioeren_conference_loupe"
            idle Transform("kechioeren_conference_loupe_repaired", matrixcolor=TintMatrix(colourTint))
            hover dayHover(Transform("kechioeren_conference_loupe_repaired", matrixcolor=TintMatrix(colourTint)))
            action Return("Loupe")

    if furkan_dialogues.get("Scroll Keepsake", False) == False:
        if loupe_gem == "conference_gem":
            imagebutton:
                focus_mask "kechioeren_conference_scroll"
                idle Transform("kechioeren_conference_scroll", matrixcolor=TintMatrix(colourTint))
                hover dayHover(Transform("kechioeren_conference_scroll", matrixcolor=TintMatrix(colourTint)))
                action Return("Scroll")
            add Transform("kechioeren_conference_cum", matrixcolor=TintMatrix(colourTint))

        else:
            add Transform("kechioeren_conference_scroll", matrixcolor=TintMatrix(colourTint))
    if loupe_gem == "conference_gem_blue":
        add Transform("conference_afterimage", matrixcolor=TintMatrix('#546fc2'))
    if loupe_gem == "conference_gem_red":
        add Transform("kechioeren_conference_scratching", matrixcolor=TintMatrix(colourTint))


label kechioeren_schedule:
    if isMidnight():
        $ kari_location = "No"
        $ furkan_location = "No"
    elif quest43.status == True and cultist_choice.get("Waited", False) == True and vote_result >= 0 and timenow.day < quest43.completed_date + 2:
        $ kari_location = "No"
        $ furkan_location = "No"
    elif isNight():
        $ kari_location = "kechioeren_conference"
        $ furkan_location = "kechioeren_conference"
    else:
        $ kari_location = "kechioeren_training_ground"
        $ furkan_location = "kechioeren_conference"
    if not kari_accompany and timenow.day < quest11.completed_date + 2:
        $ kari_location = "No"
    return
label main_kechioeren01:
    $ renpy.music.play(mKechi01, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ timenow.minute += 12
    $ timenow.passTime()
    if eversprout_route != 8:
        $ eversprout_route = 0
    $ current_location = "kechioeren01"
    call kechioeren_schedule from _call_kechioeren_schedule
    if isNight():
        scene kechioeren_night
    else:
        scene kechioeren
    with dissolve
    show screen menu_buttons
    window hide
    if quest11.status == True and goat_tribe_enter == 0:
        $ goat_tribe_enter += 1
        jump Kechioeren_Welcome
    call screen place_kechioeren01
    hide screen menu_buttons
    if _return == "To Outpost":
        jump main_woodland_outpost
    if _return == "To Cauldron":
        jump main_ardent_cauldron
    if _return == "To Kechioeren02":
        jump main_kechioeren02
    if _return == "To Training Ground":
        jump main_kechioeren_training_ground
    if _return == "Courier Office":
        jump Kechioeren_Courier_Office
    jump main_kechioeren01

label main_kechioeren02:
    $ current_location = "kechioeren02"
    $ renpy.music.play(mKechi01, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ timenow.minute += 6
    $ timenow.passTime()
    call kechioeren_schedule from _call_kechioeren_schedule_1
    if isNight():
        scene kechioeren02_night
    else:
        scene kechioeren02
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_kechioeren02
    hide screen menu_buttons
    if _return == "To Kechioeren01":
        jump main_kechioeren01
    if _return == "To Conference":
        if quest23.status == True and kari_furk_dialogue == False and renpy.random.random() < 0.25:
            jump Furkan_Before_Reconciliation
        jump main_kechioeren_conference
    if _return == "Explore":
        jump kechioeren_search_loop
    jump main_kechioeren02

label main_kechioeren_training_ground:
    $ current_location = "kechioeren_training_ground"
    $ renpy.music.play(mKechi01, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ timenow.minute += 6
    $ timenow.passTime()
    call kechioeren_schedule from _call_kechioeren_schedule_2
    if isNight():
        scene kechioeren_training_ground_night
    else:
        scene kechioeren_training_ground
    with dissolve
    show screen menu_buttons
    call screen place_kechioeren_training_ground
    hide screen menu_buttons
    if _return == "To Kechioeren01":
        jump main_kechioeren01
    if _return == "Kari":
        jump Kari_Dialogue
    if _return == "Goat1":
        jump goat_training_battle
    if _return == "Goat2":
        jump goat_talking_sequence
label main_kechioeren_conference:
    $ current_location = "kechioeren_conference"
    $ renpy.music.play(mKechi02, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ timenow.minute += 6
    $ timenow.passTime()
    if quest43.status == True and cultist_choice.get("Waited", False) == True and vote_result >= 0 and timenow.day < quest43.completed_date + 2:
        "You see the general stands besides the curtain. He seems exhausted. His mask is off, and he looks at you with a stern expression."
        k "What do you want?"
        e "I'm here to see the chief. Is he alright?"
        "He looks at you, and then at the curtain, and then back at you."
        k "No, he's not. Go away. Stop bothering him."
        e "Wait, what happened."
        k "What happened? You happened. You and your stupid village."
        k "You almost killed my chief, you know that? Did your bull tell you that?"
        e "Look, I'm sorry. I didn't even know he hid this from you."
        k "You know what? I don't care. Just get out of here."
        "Kari turns around and walks away from you."
        msg "Work in Progress!"
    $ conference_gems = {"conference_gem": "empty_gem", "conference_gem_red": "empty_gem", "conference_gem_blue": "empty_gem"}
    call kechioeren_schedule from _call_kechioeren_schedule_3
    if isNight():
        scene kechioeren_conference_night
    else:
        scene kechioeren_conference
    with dissolve
    show screen menu_buttons

    call screen place_kechioeren_conference
    if _return == "To Kechioeren02":
        jump main_kechioeren02
    if _return == "Loupe":
        "There's a loupe on the table, but it doesn't work."
        "You notice an empty slot within the loupe, it seems like something is missing."
        "Perhaps you could find a way to fix it, or maybe find someone knowledgeable enough to help."
    if _return == "Loupe Gem":
        "With a gem lodged into the loupe, you try to use it to look around the room."
        hide screen place_kechioeren_conference
        hide screen conference_gem_puzzle
        jump kechioeren_loupe_gem
    if _return == "Kari":
        jump Kari_Dialogue
    if _return == "Furkan":
        jump Furkan_Dialogue
    jump main_kechioeren_conference

label kechioeren_search_loop:

    if renpy.random.random() < 0.15:

        "Around the mountains of goat tribe, you notice that there's a green bush nearby, and you approach to pick one up."
        $ addItem("Horehound", inventory, 1)
        $ item_number = LookForItemNumber("Horehound", inventory)
        if item_number == 1:

            "You put it in your bag, you now have [item_number] Horehound."
        else:

            "You put it in your bag, you now have [item_number] Horehounds."
    else:

        "You search around the area for a while, but there seem to be nothing worth noting nearby."
    jump main_kechioeren02





label Kechioeren_Welcome:
    stop music fadeout 1.0
    "You walk towards the gate, you see two guards standing there, staring at you."
    e "Hey... May I enter?"
    "The guard reluctantly picks up a piece of paper from his pocket, and compares your face with the drawing on it."
    if not kari_accompany:
        goatguard "The Chief and General is resting, but... they ordered you may enter... as a visitor."
    else:
        goatguard "The Chief is resting, but he ordered that you may enter our tribe, as a visitor."
    goatguard "But... Uhm... we'll be watching you."
    goatguard "So, don't do anything weird."
    if kari_battle_lose == 0:
        goatguard "Especially after last time... when you beat us pretty hard."
        e "Oh... I'm sorry."
    if kari_battle_lose == 1:
        goatguard "Plus, we beat you so hard last time when you trespass..."
        e "Well you're just lucky you have your general..."
    goatguard "Whatever. Watch out your ass in our tribe, else it's not just us two you're fighting."
    e "Uhmmm.... Ok."
    jump main_kechioeren01

label Furkan_Dialogue:

    hide screen menu_buttons
    show furkan normal
    with dissolve
    if furkan_tut == 1 and quest11.status == True:
        $ furkan_tut += 1
        f "Courier, Welcome. Please, take a seat."
        e "Chief..."
        f "Call me Furkan. We do not require you to be formal."
        e "Uhmmm.... It's alright, I'll just look around."
        f "Sure."
        f "Guards...?"
        "Furkan stares at the accompanying guards for a second, before they quickly walk out of the hut."
        f "So..."
        f "Thank you so much for helping with getting me out of the cave."
        if not kari_accompany:
            f "The general told me you beat him quite severely, no?"
            e "Hmm... He asked for a fight..."
        else:
            f "The general told me you fought the monster in the cave quite bravely."
            e "We did it together, actually. He helped with me... a lot."
        f "I know. Still, you have proved your worth here."
        f "So, if we needed anything, you would be happy to lend a hand...?"
        e "Hmm... Why me?"
        f "Well, let say, I need an example from Lusterfield."
        f "To prove my commitment to make peace with your village."
        f "And to show that we can be friendly after all."
        e "Uhm... What if I say no?"
        f "Sure, you can."
        "The Chief smirks at you, he seems to know where your mind is heading... It's not really possible you would say no."
        "And he knows it."
        "Furkan looks down at his paper once again..."
    else:
        if renpy.random.random() > 0.5 and isNaked():
            f "Couri-"
            "You catch Furkan staring at your naked self, that's when you realise you haven't put your clothes on."
            f "..."
            "His cheeks become a lot redder, and the chief averts his gaze almost immediately."
            f "Watch out for the weather, it's getting cold, courier."
            e "Y-yes."
            "He waits a few seconds before turning to you, and accidentally leaves a glance on your cock."
            "You can hear a loud gulp."
            f "...Alright."
    jump Furkan_Normal_Talk

label Furkan_Normal_Talk:
    menu:
        f "How are you doing, Courier."
        "Ask about the Goat Tribe":
            jump Furkan_Ask_Goat_Tribe
        "Pick up the delivery" if is_client("Furkan"):
            $ client_name = "Furkan"
            call Courier_Pickup_Dialogues from _call_Courier_Pickup_Dialogues_12
        "Deliver the goods" if is_recipient("Furkan"):
            $ recipient_name = "Furkan"
            call Courier_Delivery_Dialogues from _call_Courier_Delivery_Dialogues_12
        "Ask about the Cult" if quest43.status == True and vote_result >= 0:
            jump Furkan_Ask_After_Temple
        "Ask about Goat Tribe's Festival" if LookForItem("Stained Scroll", inventory):
            jump Furkan_Ask_About_Festival
        "Give him the Letter from Rahim" if quest42.status == 2 and LookForItem("Letter of Alliance", inventory):
            jump Furkan_Receive_Pact
        "Warn of Lothar's Hunt" if quest37.status == True and lothar_hunting == True and furkan_knows_lothar_hunting == False:
            jump Furkan_Warn_Lothar_Hunt
        "Ask about the Dark Forest" if quest21.status == False and quest20.status == True and quest20.completed_date < timenow.day:
            jump Furkan_Ask_Werewolf_Quest
        "Ask about his status as a Chief":
            jump Furkan_Ask_Chief
        "Ask how he is doing":
            jump Furkan_Ask_How_Doing
        "That's all for now":
            jump Furkan_Dialogue_End

label Furkan_Warn_Lothar_Hunt:

    e "Please be careful, Furkan, and warn your general too. I am afraid Lothar is coming."
    f "Lot- Lothar? What does he have to do with us?"
    if quest20.status == True and quest21.status != False:
        f "The last time I heard of him, he accused us of planting the stone. But we have nothing to do with it."
        e "I believe you, but he sounded very upset about the vote in Lusterfield. Based on his track record... he might come here to take it out on you."
        f "I did not expect to find myself another enemy by doing nothing, but I understand now, I will warn the general as well."
    else:
        e "He sounded very upset about the vote in Lusterfield. Based on his track record... he might come here to take it out on you."
        f "I did not expect to find myself another enemy by doing nothing, but I understand now, I will warn the general as well."
        e "Stay safe, Furkan."
    "Seeing the worry in his eyes, you can't help but feel a pang of guilt, as if it was all because of your decision."
    f "Thank you, Courier. I will make sure the tribe is ready for whatever comes."
    f "And, if it had to come down to it, we will have no choice but to fight back. We won't underestimate one wolf."
    e "I hope it doesn't come to that."
    "He closes his eyes and nods."
    $ furkan_knows_lothar_hunting = True
    jump main_kechioeren_conference

label Furkan_Ask_Werewolf_Quest:
    f "[e], you're just on time."
    f "The tribe has discussed it and we believe we need to make headway into the dark forest to find out more about the magical stone."
    f "It might be related to something that happened in the cave."
    f "The stone, our basins, the golem. All of it may connect to something in there."
    f "Again, we ask for your help."
    e "Me?"
    f "Yes. As I said, the tribe can't spare any men at the moment to venture into the dark forest."
    f "But we've done everything we could to make it easier for you."
    k "The guards have cleared the way to the dark forest."
    "Kari walks over and marks out a path on your map."
    k "You shouldn't have any trouble using this path. But when you're in the forest itself, be careful."
    if kari_battle_lose == 1:
        k "With your fighting capability, you should be able to handle yourself. But practice caution."
    else:
        k "I hope you've been training since our last battle. The enemies in the dark enemies are far more dangerous and unforgiving than I am."
    e "Thank you."
    f "No, we need to thank you. I hope you'll find something out of this and we can work closer to a truce between the tribe and Lusterfield."
    $ QuestBegin(quest21)
    $ quest21.qProgress(__("Visit werewolves in the Dark Forest. (WIP: This Quest will be finished by finishing the werewolf quests)"))
    $ DF_Map = True
    jump main_kechioeren_conference

label Furkan_Ask_Chief:
    e "Furkan, how is it being the chief of the goat tribe?"
    f "..."
    f "Being a Chief. I am not the best at this job."
    f "But after father died, someone has to take over the tribe."
    e "What was it like, before you become chieftain?"
    f "I tell you this only because I trust you will not tell any other."
    e "Uhm... sure."
    f "It was never my choice to be a chief. I was out adventuring, discovering the whole world."
    f "Just that a certain circumstances occured, between me and my father."
    f "And, he decided to attack on the Lusterfield village soon after."
    e "What circumstances...?"
    f "About him retiring."
    f "We had an argument, quite severely actually, I left my tribe afterwards."
    e "I'm sorry about what happened to your father..."
    f "I only wish the last words we shared was different."
    f "..."
    f "You asked about me being a chief now, did I change the subject...?"
    e "Kinda, but you go ahead..."
    f "Someone has to be the chief. I understand if I am not the best leader as my father."
    f "But, I will make my tribe flourish again. No matter the cost."
    e "I trust you will, Furkan."
    jump Furkan_Normal_Talk
label Furkan_Ask_Goat_Tribe:
    e "So... Furkan, How is the goat tribe going...?"
    f "Decent, I should say. After you came, and after all the trouble that followed... The tribe changed drastically."
    f "I should not be surprised by any means. The bears got it worse."
    e "Hmm...?"
    f "Our Tribe is entirely run by the magic in the primordial runes. My bow was one of them."
    f "But everyone has to preserve their magic usage now, our only source of energy is the ancient tree."
    e "Is this why you need to reconcile with Lusterfield...?"
    e "Because you want to take over the ancient tree?"
    f "No. Not take over, I only need to harvest those remaining energy, and those Lusterfolks never used them anyway."
    f "Even then, it doesn't provide enough magic for everyone in the tribe, along with the high maintanence cost just to transport the energy."
    f "I hope we can find the primordial runes."
    e "Is it really that important to your tribe..?"
    f "Look at everything around you, it is maintained not by physical structure, but the magical energy that sustain the whole tribe."
    f "The Guardians... They used to guard those runes up on the mountain."
    f "They ran away, after the rune got stolen... and now... the basin that created them, got stolen away as well."
    f "I will handle it, one way or another. But I need a soldier, a soldier like you."
    e "Me..."
    e "Do you really believe that I can bring prosper to your tribe...?"
    f "I need an adventurer, and a friend who I can trust."
    f "Everything that happened in this world after you arrived, they all connect back to you."
    f "You are the answer."
    e "I get it... but it seems like such a big responsibility."
    f "Do not fret. Time will come when you'll prove your worth."
    e "...I understand."
    jump Furkan_Normal_Talk
label Furkan_Meet_Flower:
    scene woodlandoutpost with dissolve
    show furkan normal with dissolve
    f "Courier, what are you doing here?"
    "A voice suddenly appears behind you. You turn around and are greeted by Furkan's inquisitive gaze."
    "You ponder what to do."
    e "U-uh..."
    menu:
        f "What are you doing in the outpost?"
        "Tell Furkan about Rahim's flower":
            $ furkan_lie = False
            e "I'm here on Rahim's behest to collect a special kind of flower."
            "Furkan is clearly taken aback by your honesty."
            f "I am sure the bull would never have wanted you to tell me that."
            f "But I am thankful that you did."
            "Seeing the smile on Furkan's face, you believe you've made the right choice."
            f "Come, I will help you. The flower that you are looking for is native to the land around the tribe."
            f "I will lead you there."
            "Furkan waves at you and you follow him through the woods."
        "Lie to Furkan":
            $ furkan_lie = True
            e "I'm just here foraging."
            "Furkan narrows his eyes at you. You sweat nervously but try to look calm on the surface."
            "Eventually, Furkan breaks into a small smile."
            f "If you say so."
            "You nod."
            f "Can you tell me what you are foraging for?"
            "You ponder whether to tell him about the flower when Furkan continues."
            f "Perchance it is a flower that only grows around the tribe?"
            "Furkan shoots you a knowing smile. You can't help but see the disappointment in his eyes."
            e "Erm... Yes..."
            f "The flower is the only unique thing growing around this area. I doubt you would be foraging for anything else."
            f "Come with me. I will lead you to the flower bushes."
            "Furkan waves at you and you follow him through the woods."
    "As you walk into the clearing, you take in a surprised gasp."
    "Furkan smiles at your reaction."
    f "Amazing sight, is it not?"
    "You can only nod."
    "The clearing is covered in vibrant flower bushes. The flowers look like little balls of sunburst."
    "They give off a very relaxing fragrance."
    e "What are these..."
    f "They are called mums. We use them in poultices to help with swelling, cold, fever and so on. They are also great decorative plant."
    f "You are here for them, are you not? Better get picking then."
    if quest24.status != False:
        e "I think Haskell taught me to come to this place as well."
        f "The old dragon and his love for flowers... But I can still help you harvest these beautiful mums."
    "Furkan teaches you how to harvest the flowers. With his help, you soon have a bag full of them."
    "Then, something comes to you."
    e "Furkan, shouldn't you be back at the tribe? How could you have time to help me with this? I shouldn't have taken up so much of your time."
    "Furkan just smiles."
    f "Even the chief needs a break once in a while. This is just what I needed."
    "There is a faraway look in his eyes."
    f "I have plenty of memories here."
    f "When Kari and I were young, we would hide among the bushes and play hide and seek."
    f "Cannot remember the last time we did anything remotely like that."
    e "Furkan..."
    f "It is part of growing up, just did not expect now that we're both ruling over a tribe."
    f "..."
    "Furkan changes his tone to something lighter."
    f "Speaking of the general, thank you for saving me last time."
    e "That was nothing."
    if kari_accompany == False or kari_battle_lose == 1:
        f "Though, I would have preferred if you have handled the encounter with Kari non-confrontationally."
        f "Steps towards truce will be hard if every go-to solution is violence."
        e "I didn't mean to. I tried to explain myself but they attacked."
        f "And I wish to apologize to you on their behalf. They were too worried to be thinking clearly."
        f "Thankfully, no one got seriously injured."
        "Furkan gives you a reassuring smile."
        e "And I'm sorry too."
        f "Appreciate it."
        if kari_accompany == False:
            f "However, you might be getting some attitude from Kari."
            e "Why?"
            f "The man does not wear his emotions on his sleeves but I have known him since he was a wee fawn."
            f "His loss at your hands bothers him. Granted, he was not at his strongest at that moment in time."
            f "But he prides himself on being the strongest fighter in the tribe... the loss of magic here hit him hard."
            e "What can I do then?"
            "Furkan shakes his head with a smile."
            f "It is not what you need to do but what he needs to do."
            f "I would advise him to let it go but I know he is too stubborn for it."
            f "...in truth, he was disappointed that he was not in the cave."
            e "Alright... I'll be careful next time."
        else:

            f "I heard about your fight with Kari."
            "Your face blushes thinking back to that defeat."
            e "I..."
            "Furkan's tone turns serious."
            f "You're lucky that we are not out to kill."
            f "Well, maybe not Kari."
            f "Not everyone in the world will be as merciful."
            f "You need to toughen up."
            e "I will."
            f "Good. Kari would agree with me."
            f "He mentioned seeing the potential in you."
            e "Did he?"
            f "Yes, and he is rarely wrong with his appraisal."
            f "So train harder. The world is a dangerous place."
            e "Thank you for the concern, Furkan."
        f "But who am I to talk to you about fights and conflicts considering all the harm the tribe has done to Lusterfield."
        "You see a regretful twinge in Furkan's smile."
        e "I'm sure you didn't mean for it to happen."
        f "That is nice of you to say but a war is a war. People got blinded by emotions."
        f "I was not there, does not mean I did not make it happen."
        f "Kari could have kidnapped you to torture for information just because he was worried about me."
        f "The same could be said of that war."
        f "My people were out for revenge. A life for a life."
        f "We killed many and many were killed."
        "Furkan slides into silence."
        "You just stay by his side quietly."
        f "Was it worth?"
        f "Families were left scattered, including my own."
        f "Just because we were all blinded by a temporary emotion."
        f "As the chief, that is just the ghost that stays with me to my grave."
        e "Furkan..."
        "You give him a comforting touch."
        e "At least you are trying to fix it now."
        f "I do not think something like that can ever be fixed but I shall try my best."
        f "But, that should not be something you need to worry about. But I am thankful that you allow me to get that out of my chest."
        e "Anytime, Furkan."
    else:
        f "I'm very impressed with how you've handled the encounter with Kari and the guards."
        "You blush at the compliment."
        e "I merely did what everyone would have done."
        f "That's not true. Not everyone can keep an open and rational mind at moments like that."
        "You have a feeling Furkan is talking more than just the encounter you had with Kari."
        f "Emotions get the better of people."
        f "Sometimes, they'd rather fight than talk."
        "Furkan sighs."
        e "I'm sure things will turn out for the better."
        f "Hope so. Cause what's the alternative?"
        "Furkan gestures around him."
        f "Look around us."
        "You do and are confused. The field is beautiful but that's about it."
        e "Yes, the flowers are gorgeous."
        f "But no one is here to appreciate them."
        f "In the past, this place would be roaming with people from the tribe and Lusterfield, just enjoying their day in the sun."
        f "But now, nothing."
        f "The Lusterfolks does not come here after the war, and without support, our people have to retreat from the buggbears as well."
        e "Furkan..."
        "Furkan shakes his head and picks himself up."
        f "Sorry about that. Being here brings back many memories from the past."
        e "I'm sorry."
        f "No need to apologize. I am glad to be back here and make new memory with a Lusterfolk."
    $ addItem("Chrysanthemum", inventory, 4)
    $ quest19.status = 3
    $ quest19.qComp(__("Report to Rahim{#FlowerReport}"))
    "You part with Furkan. It's time to return to Rahim with the mums."
    jump main_woodland_outpost


label goat_talking_sequence:
    "You look at the two goats slacking off on the barrels."
    e "H-hey... aren't you guys supposed to be training?"
    gt "We are. Don't you see we're training our brains...?"
    e "W-what?"
    gt "...Why are you outsider here anyway... aren't you supposed to be fucking around with the lusterfolks..."
    if buggbear.lose > 0:
        e "H-hey watch your mouth..."
        gt "Heh... no worries we all saw it when you fuck that buggbear."
        e "I d-didn't."
        gt "Perhaps that's why our chief has a liking of you."
        gt "N-now... leave us alone. We're not training with these pieces of junk until the magics are back."
    else:
        e "Why are you guys so stingy."
        gt "Because, that's none of your business. Ah, I know what you're doing, trying to beat us even in the school of magic?"
        e "So, are you jealous that I am more capable?"
        gt "H-hey! We're trained soldiers, not some random goat-lookalike non-goats going around like he's a hero just because he saved our chief."
        gt "You've got us scolded for not watching over our chief."
        gt "N-now... leave us alone."

    jump main_kechioeren_training_ground

label goat_training_battle:
    "You look at the goat practicing archery in front of you, his hand is trembling a bit."
    "He turns back at you."
    gt "I wish I can go back to using my staff, not bows and spears. It was much easier that way..."
    gt "..."
    gt "What's the matter with you...?"
    menu:
        e "Hmm..."
        "Battle with the Goat":
            e "I want to train with you..."
            gt "Well... I do need a training buddy, and it's not like the other goats are in mood for a battle..."
            gt "Alright, give me all you got."
            $ goat_num = 2
            jump goathuntsman_battle
        "That's all for now":
            e "Hmm... I should go."
            gt "Yeah, go. I've still got a cart worth of bull's eye to shoot."
            jump main_kechioeren_training_ground
label Furkan_Ask_How_Doing:
    e "How are you doing, Furkan."
    f "I am reading paperworks."
    e "Oh..."
    "The chieftain stares at you, he seems to expect you to do something..."
    e "I'll leave you be for the moment."
    f "Thank you, [e]."
label Furkan_Dialogue_End:
    e "That's all for now, Furkan."
    f "Good. See you."
    jump main_kechioeren_conference

label Keepsake_Furkan_Festival:
    "You hold the stained scroll in hand, and a familiar energy courses through your body."
    "Suddenly, the world around you shifts and blurs."
    "And soon, you find yourself standing in a different place, a place filled with warmth and light."
    "..."
    "..."


    "It was a long time ago, when Furkan had come of age, and a festival was held in the tribe."
    "He remembered the day vividly, as if it was yesterday."
    scene kechioeren_night_festival with dissolve
    "The night was lit with the warm glow of fire, and the air was filled with the sound of bells and laughter."
    "Furkan was dressed in his ceremonial attire, a simple but elegant outfit that reflected his status as the chief's son."
    "He had been chosen to lead the ceremony later, it was a great honor for a young goat like him, as everyone is looking up towards the future leader of the tribe."
    "Furkan stood alone, his eyes darted around, skimming through the faces of countless jubilant goats."
    "Some were dancing, some were singing, and some were just sitting around the fire, enjoying the warmth."
    "Stalls were set up all around, selling food and drinks, the smell of sweet treats wafted through the air."
    "Furkan moved through the crowd, his hands were holding a box of cabbage cheese rolls, a delicacy that was only made during the festival."
    "He was greeting people and accepting their congratulations, all the while looking for someone."
    tv "Furkan!"
    show tevfik normal with dissolve
    "Suddenly, a familiar voice called out to him. He turned around to see Tevfik, his father, the chief of the tribe, along with the elders following behind him."
    tv "Furkan, my son, come here."
    "The young goat walked over to his father, his heart pounding in his chest."
    "Tevfik was an imposing figure, despite his tallness, his horns curved majestically, and his eyes were sharp and piercing."
    "The old goat has seen many battles in his times, but he was still standing strong, his presence commanding respect from every goat in the tribe."
    f "Yes, father?"
    tv "My son, it has been a while... you have grown into a fine young goat, haven't you?"
    tv "Today is a special day for you, and for our tribe."
    "Tevfik placed a hand on Furkan's shoulder, his grip firm and reassuring."
    tv "You will help me lead the ceremony tonight, and I have no doubt you will do it well."
    f "I... I am honored, father, but I am not sure if I am ready."
    tv "You are ready, my son. My elders have taught you well, they told me you are a quick learner."
    "The elders nodded in agreement, as Tevfik broke into a soft smile."
    tv "You will do great, I am sure of it. Everyone in the tribe is looking up to you, and they will be proud of you, regardless of the outcome."
    f "Yes, father."
    tv "...is there anything in your mind?"
    "Tevfik sensed hesitation in his son's voice, and he looked at him with concern."
    f "Where is Kari?"
    "Furkan's voice was barely above a whisper, but Tevfik heard it nonetheless."
    tv "Kari...?"
    "Tevfik's expression darkened for a moment, he looked down at the box, and he looked away, his eyes distant."
    tv "I had not seen him since the festival had begun, he was supposed to be here... somewhere."
    tv "Do not worry about him, he knows his role, he will be here when the ceremony starts."
    "Furkan nodded, but he could not shake the feeling of unease that settled in his stomach."
    tv "Furk-"
    g "Ahem, Chief, there is something you need to see."
    "The vendor interrupted Tevfik as he approached them, a small device was in his hand, glowing faintly in bright blue."
    "Tevfik looked at the device, before waving the elders away."
    tv "Go and prepare for the ceremony, my son. I will be there when the time comes."
    show tevfik at r2 with move
    "Furkan nodded, and watched as his father walked away into the Ardent Cauldron, with bells and chimes ringing in the air."
    f "Yes... father..."
    "The young goat stood there for a moment, and something suddenly crossed his eyes as he looks up at the night sky."
    "Without hesitation, Furkan turned around and walked away from the festivities, his legs brisk with haste."
    scene kechioeren02_night with dissolve
    "He trekked up the hill, he knew there was only one place where the mage-in-training would be."
    "It was the lone hut over the cliff, disused by the chief long ago, but Kari and Furkan had made it their own little hideout since childhood."
    "Furkan glanced at the dim light coming from the hut, and with excitement, he quickly peeked his head over the curtains."
    scene kechioeren_conference_festival with dissolve
    f "Boo..."
    "He spots the mage-in-training sitting on the floor, scribbling magic runes on his book, his back turned to Furkan."
    f "Kari, what are you doing here?"
    "Kari turned around, his eyes wide with surprise."
    show kari normal with dissolve
    k "Oh! Buckie! I'm sorry. I should be at the festival... what time is it?"
    "Furkan walked into the hut, and sat down beside Kari."
    f "It's alright, I was just looking for you."
    f "Bought you some cheese rolls, in case you weren't going to the stalls this year."
    "Furkan put the box down on the table, Kari smiled, his hands busy with the book."
    "Slowly, the deer's eyes grew more unfocused as he flipped over the page, until he finally closed the book and looked at Furkan."
    k "So, are you ready for the ceremony?"
    f "I am, I think..."
    "Furkan sighed."
    f "I don't know. I had to pour the flowing water into everyone's basin, and then I have to look at them and say some words..."
    f "All the while they are looking at me. Looking up to me... I don't know if I can do it."
    "Kari looked at Furkan, his eyes softening."
    k "You can do it, buckie. You are the chief's son, they won't fault you if you miss a word or two, not that you will."
    f "How can you be so certain? You have never done this before."
    k "Yes, but I know you. And I know Tevfik, maybe you will do it better than him."
    "The young goat patted his back reassuringly, his fingers briefly grazing against the thin material of his cape."
    "Furkan nodded, relieved."
    "He wanted to ask Kari about something, something he has been wanting to say for years now, but it was not the right time."
    k "You will be the chief one day, and this is just the first step."
    f "Do you believe so?"
    "Furkan murmured, staring forward as if he's lost in thought."
    f "I am not like father, I am not a warrior, I am not a leader. I am never ready to be a chief."
    "Kari let out a small sigh, and placed a hand on top of Furkan's shoulder, his voice grew more serious."
    k "I wasn't ready to be a mage either, but I had no choice, I couldn't let my magic go to waste."
    k "The same goes for you, you were born with that horn, that means you are the ones who leads the tribe. You might not feel ready yet, but that doesn't mean you aren't worthy."
    "Furkan looked at Kari, his eyes were filled with longing and uncertainty."
    f "But you never rest, ever since you started training under father... I cannot even remember the last time we saw each other."
    f "We used to walk around the festivals together, and you loved these rolls so much you'd eat the entire stalls worth of them, now you didn't even touch them."
    "Kari frowned softly."
    "The two of them fell into silence, and it was interrupted by the faint sound of bells ringing from the festival grounds."
    k "Buckie, am I distracting you?"
    "Kari whispered, his eyes lowered."
    k "I can see it in your eyes, you are not focused on the ceremony, instead you came all the way to look for me. And for what?"
    "Furkan shook his head."
    f "No, it's not that. I just... I miss you. And you have been so busy, I thought you were hiding away from me."
    k "We can talk on our way down."
    f "Kari, ever since we started training, all I have been thinking about was the hunting we used to do together, the adventures we had, the fun we had."
    f "Sometimes... sometimes I wish things could stay like that forever."
    k "The ceremony is about to star-"
    f "I wish I could just be a normal goat, not the chief's son, not the one who has to lead the tribe. I just want to be with you, like we used to."
    k "Buckie..."
    "He turned towards Furkan, their faces inches apart, and the young goat could smell the sweet scent coming from the deer."
    f "Do you never miss those days? When we were just two kids, running around the forest, climbing on top of the mountain and sleeping under the stars?"
    "Kari looked at Furkan, his eyes softening."
    k "You cannot be like this, buckie. You are the chief's son, you have to be there when the bell rings."
    "Furkan felt his heart pounded against his chest, and he held himself back from embracing his childhood friend."
    "Instead, he swallowed his fears, and reached out to touch Kari's hand."
    f "Father will make sure everything goes well, just like every festival before."
    f "Please, Kari. Let me stay here a little longer."
    "The young goat moved closer, until the tips of their snouts touched each other's, and for a moment, everything seemed still."
    f "Just stay here with me."
    "Kari looked at Furkan, unsure of what to say or do. Despite his reluctance to admit it, he remembered how it used to be."
    "When they would climb the mountains and sleep together, sometimes Furkan would pull him into an embrace, just like how he is doing now."
    "His mind was filled with old memories, of the countless nights where he stayed awake just to hear the sound of Furkan's breath as he slept beside him."
    "Back then, he couldn't see the world beyond the mountains, but now... He looked at Furkan, at his unwavering gaze and the faint smile on his lips."
    "Those days were long gone, but not their feelings, they never changed."
    "For a moment, Kari hesitated, but then he found himself leaning in closer."
    "Their lips touched briefly, just like how they had brushed against each other by the waterfall when they were younger."
    "It lasted no more than a second, but it was enough to send shivers down their spine."
    "A soft moan escaped Furkan's mouth, and he leaned in for another kiss, this time Kari met him halfway."
    "The deer mage wrapped his arms around Furkan, pulling him close."
    k "Buckie...?"
    k "What if... What if someone sees us?"
    f "They won't."
    "He reached out to grab Kari's hand, guiding them under the table."
    f "Father will be busy with the ceremony."
    "He murmured, pushing the deer further down onto the floor."
    call Scene_Furkan_Kari_Keepsake from _call_Scene_Furkan_Kari_Keepsake
    "He couldn't shake off the feeling of unease that had settled in his stomach. That he enjoyed being with Furkan like this."
    "It seemed he had led Furkan towards a path further away from being a good chief, to a path he would be indulging in his own desires rather than the needs of the tribe."
    "Even if he intended to continue, Tevfik would have him plenty known that such a thing is impossible."
    "Kari watched Furkan slowly walk down the hills, and as he did so, the smile on his face faded away."
    "Tonight he was reminded of the warm embrace of his own childhood friend, but he knew that he could never tell anyone what truly happened between them tonight."
    "Kari sighed, he stared at the box of cabbage cheese rolls, he picked out one of them and took a bite."
    "His eyes watered as he chewed alone in the dark room, the roll was cold, but the taste of Furkan's seed still lingering in his mouth."
    "Putting the half-eaten roll away, he hesitantly picked up the scrolls soaked with their own seeds, cleaning after the mess for the rest of the night."
    "Along the path towards the tribe center, Furkan checked his clothes for any residue."
    "He didn't intend to make love with his best friend up there, but it felt so natural and right, as if they were meant to be together."
    "The thought was all over his head, up until he walked to the entrance of the ceremony."
    "He took a deep breath, and stepped to the side of Tevfik."
    tv "You're late, my son."
    "Furkan felt a knot tighten in his stomach as he looked at his father, staring into the ceremony."
    "There is a tinge of undiscernable anger in his voice, but Furkan knew better than to question if he knew anything."
    f "Sorry, I got caught up with something-"
    tv "Make sure it doesn't happen again."
    "Furkan nodded slowly."
    f "Yes, father."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
