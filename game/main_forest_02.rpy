screen place_dark_forest():
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
        action Return("To Outpost")
    if DF_Map == True:
        imagebutton:
            xalign 0.52
            yalign 0.67
            idle "dungeon1_arrow"
            hover "dungeon1_arrow_hover"
            action Return("To Dungeon")
    if gloomy_mountainside.discovered == True:
        imagebutton:
            xalign 0.27
            yalign 0.67
            idle "lusterfield_arrow1"
            hover "lusterfield_arrow1_hover"
            style "footstep_button"
            action Return("To Mountainside")
screen place_gloomy_mountainside():
    imagebutton:
        xalign 0.99
        yalign 0.69
        idle "explore_idle"
        hover "explore_hover"
        action Return("Explore")
    imagebutton:
        xalign 0.32
        yalign 0.77
        idle "dungeon1_arrow"
        hover "dungeon1_arrow_hover"
        style "footstep_button"
        action Return("To Maze")
    imagebutton:
        xalign 0.77
        yalign 0.92
        idle "bedroom_arrow"
        hover "bedroom_arrow_hover"
        style "footstep_button"
        action Return("To Dark Forest")
label dark_forest_loop:
    if isNight():
        scene dark_forest
    else:
        scene dark_forest
    $ rnd = renpy.random.random()
    if rnd < 0.2:
        "You walk through the misty dark forest... Suddenly, you hear someone howling from afar."
        "Immediately, you begin to run towards the opposite direction, but soon a dark figure comes into your view."
        e "Fuck..."

        jump werewolf_battle
    elif rnd < 0.4:
        if renpy.random.random() < 0.5 and hunterattirerecipe not in discoveredrecipe:
            "Inside the forest, you found a leftover paper detailing the process to make hunter's attire."
            "It says... making a hunter's attire requires 2 Canvas and 2 Fabric and 3 Pelts. You mark down the recipe on your journal."
            msg "New Recipe learned, check out Rahim's Workstation for more detail."
            $ discoveredrecipe.append(hunterattirerecipe)
        else:
            "You search around the area for a while, but there seem to be nothing worth noting nearby."
    elif rnd < 0.6 and isNight():
        "You walk through the misty dark forest... Suddenly, you hear two distinct howling from afar."
        "Immediately, you begin to run towards the opposite direction, but soon two dark figures come into your view."
        e "Fuck..."

        jump werewolf_werewolf_battle
    elif rnd < 0.8:
        "You search around the area for a while, but there seem to be nothing worth noting nearby."
    else:
        "You search around the area for a while, but there seem to be nothing worth noting nearby."

    jump main_dark_forest
label main_gloomy_mountainside:
    $ current_location = gloomy_mountainside

    $ wilderness = True
    $ timenow.minute += 20
    $ timenow.passTime()
    if isNight():
        scene gloomy_mountainside
    else:
        scene gloomy_mountainside
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_gloomy_mountainside
    if _return == "Explore":
        jump gloomy_mountainside_loop
    if _return == "To Maze":
        jump Minotaur_Maze_Enter
    if _return == "To Dark Forest":
        jump main_dark_forest
    jump main_gloomy_mountainside
label main_dark_forest:
    $ current_location = dark_forest
    $ current_map = darkforest_map
    if eversprout_route != 8:
        $ eversprout_route = 0

    $ renpy.music.play(mDforest, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ wilderness = True
    $ timenow.minute += 20
    $ timenow.passTime()
    if isNight():
        scene dark_forest
    else:
        scene dark_forest
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_dark_forest
    if _return == "Explore":
        jump dark_forest_loop
    if _return == "To Outpost":
        jump main_woodland_outpost
    if _return == "To Mountainside":
        jump main_gloomy_mountainside
    if _return == "To Dungeon":
        jump Dark_Forest_Map
    jump main_dark_forest
label gloomy_mountainside_loop:
    if isNight():
        scene gloomy_mountainside
    else:
        scene gloomy_mountainside
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

    jump main_gloomy_mountainside
label Dark_Forest_Map:
    $ renpy.music.play(mDforest, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ wilderness = True
    $ timenow.minute += 20
    $ timenow.passTime()
    scene darkforest_map with dissolve
    hide screen menu_buttons
    if quest27.status == 3 and LookForItem("Flagitious Ooze", inventory) and LookForItem("Teratoid Mucus", inventory) and LookForItem("Slime Grancrystal", inventory):
        jump Wuldon_Enter_Cure_Transition
    window hide
    call screen Dark_Forest_Mappy


    if _return == "To Cave Entrance":
        jump Cavern_Entrance_Enter
    if _return == "To Entrance":
        jump main_dark_forest
    if _return == "To Cavern":
        scene black with dissolve
        "You enter the Chelforte Cavern..."
        jump Chelforte_Cavern_Enter
    if _return == "To Well":
        scene black with dissolve
        "You enter the Slumbrous Well..."
        jump main_slumbrous_well
    if _return == "To DF1":
        scene black with dissolve
        "You enter the forest nightwatch..."
        jump Forest_Nightwatch_Enter
    if _return == "To Wolf Den":
        "You enter the werewolves' den..."
        jump main_moonlit_wolf_den
    if _return == "To Slime":
        jump Slimy_Fight_Recoup
    if _return == "To Hollow":
        jump Whispering_Hollow_Enter
    if _return == "To Thicket":
        jump Creek_Thicket_Enter
    if _return == "To Stream":
        if quest27.status == 3:
            "As you walk through the gap at the other end of the dungeon floor, you see Wuldon burst in through the treeline after you, making sure to keep you in his sights."
            "You half expect him to join you in the next room, but he stops at the gap once again, poised to clear out any and all slimes trying to come after you."
        jump Viscid_Stream_Enter
    if _return == "To Sanctuary":
        jump Forgotten_Sanctuary_Enter
    if _return == "To Split Trail":
        scene black with dissolve
        "You enter the split trails..."
        jump Split_Trail_Enter

label moonlit_wolf_den_enter:
    "You follow the trail marked out by Kari on your map."
    "The winding forest path seems to lead to nowhere."
    "You look around and realize you are lost."
    "Suddenly, there's a rustling behind the leaves."
    "A grey werewolf jumps out as he points his paws at you."
    ww "Die!"
    e "I just want to talk! Can you lead me to your leader?"
    e "..."
    ww "You tres-Passing on our terri-Tory!"
    e "W-what?"
    scene moonlit_wolf_den with dissolve
    "Suddenly from an unknown corner, a pack of werewolves appears."
    "One of them leads in the front, he is much more brown than the usual grey in the werewolves."
    "The leader is large and menacing. The other werewolves seem cowed in his presence."
    "The grey werewolf walks to stand behind the leader."
    show uffe normal with dissolve
    u "What's the meaning of this, trespasser?"

    "There is a hint of warning in his tone."
    "You try to be as civil as possible. But with the pack of werewolves staring you down, escaping does not seem like a possibility."
    e "I'm... [e]. I come from Lusterfield. What's your name?"
    "The alpha narrows his eyes at you like you're stupid."
    u "I have no idea we're friends."
    e "It'll make addressing you and finding you easier."
    u "The name's Uffe, but you call me Alpha should the need arise."
    u "Why are you here?"
    e "I mean no harm. I'm here to inquire about something."
    u "Is that so?"
    "The alpha says with mock interest."
    u "and why should we help you?"
    e "To be kind?"
    "The alpha breaks into a sinister chuckle, which the other werewolves follow suit as well."
    u "You're funny. I'll give you that, trespasser."
    u "But I wonder if humor can save your life."
    "The werewolves close in around you."
    "In desperation, you pull out the magical stone."
    e "I just want to know if you have seen this before?"
    "The alpha raises his arm. The werewolves stop advancing."
    u "Where did you get that, trespasser?"
    "You catches the sudden awareness in the alpha's eyes."
    e "So you do recognize this."
    u "So what if I do? You haven't answered my question, trespasser."
    e "We found it outside the forest and a friend traced its magic back to this place."
    "The alpha narrows his eyes at you as if trying to see if you're lying or not."
    e "So... can you tell me more about this stone?"
    u "I can."
    u "For a price."
    u "We'll let you stay here... only if you are willing to help our pack. Only afterwards, I will tell you what I know."
    e "O-ok, I'll do whatever's acceptable."
    u "You will, trespasser. After all, you know what happens to those who trespasses in my forest."
    u "A fate worse than death."
    "Uffe raises his paws, and the other werewolves quickly scatter rather quickly."
    jump Moonlit_Wolf_Den_Enter

label main_moonlit_wolf_den:
    if tetto_escaped and quest36.status == True:
        "You do not dare to enter the werewolf den after helping tetto escape..."
        menu:
            "Are you sure it's a right choice to enter the cave?"
            "Enter the werewolf cave":
                "You slowly enter the cave, holding your weapon to defend yourself properly."
                "The cave seems just as normal as you'd expec-"
                "T-THUNK!"
                scene black with dissolve
                "Something hits you in the head from behind, and you instantly fall on the ground, unconscious."
                pause 2
                "As you wake up, a familiar face greets you from above, someone that you know, but never wants to meet again."
                jump BadEnd_Werewolf_Capture
            "Leave":
                jump Dark_Forest_Map

    if uffe_celebration == False and ((quest36.status == True and tetto_escaped == False and vurro_lives == True) or (quest34.status == True and vurro_lives == False)):
        menu:
            "Do you want to join the feast?"
            "Yes {#JoinFeast}":
                $ uffe_celebration = True
                jump Uffe_Celebration_Orgy
            "No {#JoinFeast}":
                pass

    jump Moonlit_Wolf_Den_Enter

label Uffe_Celebration_Orgy:

    "You enter the den with a surprised face as all werewolves are bare naked, except for Uffe."
    "The werewolves howls loudly, one after another. Your ears are almost exploding with how many of them are draining all their energy just to howl."
    "Not to mention the echoes in the werewolf den, which makes it ten times worse than you'd think."
    "Some of them sit on the rock lazily, howling occassionally in response, some elders crawl on all four, screaming from the inside of their lungs."

    call Scene_Werewolf_Gangbang from _call_Scene_Werewolf_Gangbang
    $ pc.lust = 0
    $ pc.add_active_status(stuffed)
    $ pc.add_active_status(soremouthed)
    jump Dark_Forest_Map

label Uffe_Territory_Quest:
    show uffe normal with dissolve
    "You see the werewolf leader, sitting right under the moonlight, looks over at you as you enter the werewolf den."
    if vurro_lives:
        "There's nothing for him to discuss with you, unless he's suspicious of Vurro's death."
        "But, you won't be getting out of this alive, if he finds out about the truth of his brother."
    else:
        "Vurro is already dead, there's nothing for you to discuss right now."
        "Unless, he's planning to tie up the last loose end, you are beginning to panic at the possibility."
    "As you turn away, a werewolf bumps onto you from behind, pointing you towards the werewolf leader."
    "You reluctantly walk out of the shade, and stops right in front of Uffe."
    e "H-hello, Uffe."
    u "Trespasser, you seem to like walking in and out of my sight freely, shall I start welcoming you to our den?"
    e "That's not really necessary, I'll be out of your sight, like... forever."
    u "Don't, it's better for you to stay. After all, you've been surviving for a while."
    "Uffe gives you a sneering chuckle, something tells you that it's of a sinister nature."
    if vurro_lives:
        u "You must have had a grueling battle with the monster, considering his scent still lingers on you."
        e "L-linger?"
        u "I've been aware of your scent for a while."
        u "It reminds me of my childhood. Playing cat and mouse with my brother."
        u "He liked being the one's of mouse, trying to outsmart me hiding around the forest."
        u "And you know what happens at the end of every game?"
        "He asks, staring at you menacingly."
        u "I always came out on top."
        u "I can just smell where exactly he is."
        e "Isn't that, cheating?"
        "The brown werewolf remain silent."
        "Over a few seconds, his sharp stare slowly turns into a side glance."
        u "He was my brother, that monster."
        "You take a moment to ponder that setence."
        u "The smell on you will be the last I'll ever remember him of. As much of a weak link he was..."
        u "He was family. There's nothing more important than family."
        "You are not sure if the sentiment was real, but you decide to take it at face value."
    else:
        u "We've located the body in the cave, thanks to you, a threat to our pack has been permanently eliminated."
        "You nod at Uffe, and he chuckles, again."
        "He pauses for a moment, as if he's looking for a word."
    u "We have more to do here, trespasser. Leave no stone unturned."
    e "The last time you promised me something for my work, you lied."
    "There's a visible change in his facial expression there, as the alpha seems much more annoyed than you expected."
    u "If the satisfaction of serving me is not enough, the reward can always be you staying alive, would that be enough of a reward?"
    "That was an abrupt threat, you can't figure out of what to say."
    u "Any questions, you better ask right now."
    "You shrug reluctantly."
    u "Now, we need to expand our territories here, starting from the hollow."
    u "..."
    "The leader waits for you to speak, but you decide to remain silent in protest of his unfulfilled wish."
    u "The hollow is located between our territories, and the slimes', west of the split trails."
    e "W-what do you need exactly?"
    u "It buries a dark treasure, moonstone amulet. I need you to clear the area, and retrieve what's there for me."
    u "Now go, trespasser."
    e "W-wait, why me? You have other werewolves who are definitely more competent, if not stronger."
    "Uffe only gives a a side glance, not even a full one, he chuckles, and returns to his business."
    e "...Alright"
    "You can feel the other werewolves staring at your dumbfounded face as you remain standing."
    "Uffe doesn't bat you another eye before you eventually take your leave."
    $ QuestBegin(quest34)
    $ whispering_hollows.discovered = True

    $ quest34.qProgress(_("Solve the riddles and retrieve the amulet in the Whispering Hollow"))
    $ quest34.qProgress(_("Cut all grasses in the Whispering Hollow"))
    jump Moonlit_Wolf_Den_Loop




label Uffe_Territory_Quest_Return_After_Amulet:

    "You notice dozen pairs of eyes hiding in the darkness,. The usual werewolves were staring at you from the corners."
    e "Uffe, here's the amulet."
    "Something strange is emanating from within the moonstone as you present it in front of Uffe, who takes it eagerly."
    u "Well done yet again, trespasser."
    "He doesn't even bat you another eye, just entirely focused on the amulet."
    e "Did you send me because your wolves are too stupid to solve riddles?"
    "Uffe finally glances at you, albeit it's of a hostile nature."
    u "Stupid? We could have torn you apart right now, including your measly little brain."
    u "Cleverness doesn't help you survive in this world, trespasser."
    e "Then how come you asked me to solve the riddles?"
    u "I can ask you, or, I can put you between my fangs, do you prefer the latter?"
    "You shrug, which only gets Uffe to chuckle lightly."
    u "That's what I thought."
    "The werewolf alpha puts away the amulet."
    u "You can go now."
    e "Are you still not letting me know about the stone, after everything I did?"
    u "I've told you what I know, it's only you who insists I didn't."
    "You remain silent, perhaps he's right. You are just helping someone who doesn't appreciate your worth."
    e "Alright then."
    "Uffe stares at you once again, this time of a cautious nature."

    if pc.armor["Accessory"] != None:
        if pc.armor["Accessory"].img == "Moonstone Amulet":
            $ pc.armor["Accessory"] = None
        else:
            $ removeItem("Moonstone Amulet", inventory, 1)
    else:
        $ removeItem("Moonstone Amulet", inventory, 1)
    $ QuestFinish(quest34)
    jump Moonlit_Wolf_Den_Loop



label Uffe_Territory_Quest_Start_Runaways:
    "You arrive in front of the werewolf once more, and the first thing you notice is the extra pairs of eyes staring upon you."
    u "Welcome back, trespasser."
    e "Uffe."
    "You address the alpha with a slightly deeper voice, of which raised his brows briefly."
    u "Now that you have proven yourself to be useful. There's another problem I need someone like you to deal with."
    u "We've found a group of traitors, runaways, who weren't fit to live in this world."
    u "They killed a few of ours, and now they plan to escape from the forest, but that's not going to happen."
    "Uffe glances at you, twiddling his claws against your neck, you instinctively flinch."
    e "What does that mean, exactly?"
    u "It means, we're not letting them leave our territory."
    "His message was rather obvious, you understand that he wants them gone, just like how he wanted his own brother gone."
    u "Those little weak links will flee like cowards if they see anything that resembles a wolf."
    u "So, I need you to bring them back to me, we'll take over after that."
    e "I- What are you going to do with them?"
    u "You know exactly what I'm going to do."
    e "Why? They're already out of the picture, can't you leave them be?"
    "Uffe raises his eyebrow, his grin vanishes as soon as you finish your sentence."
    u "Here I thought you were fit for the rules of nature."
    e "What?"
    "He takes a great sigh, and the pack of werewolves behind you immediately tense up."
    u "Trespasser, why do you think only our pack survives in this forest?"
    e "Because you killed everything else?"
    u "Partly, but there's something more important than killing."
    u "We survive, we adapt, and we do not hesitate to put out the wildfires before it spreads."
    "You're not sure if you agree with the wolf even so slightly."
    menu:
        u "So, are you a wildfire?"
        "Help Uffe catch the runaways":
            $ QuestBegin(quest36)
            $ addItem("Werewolf Whistle", inventory, 1)
            $ quest36.qProgress(__("Visit the northeast of the Split Trail"))
            $ quest36.qProgress(__("Blow on the whistle on the escaping werewolves"))
            e "Alright, I'll do it."
            if not vurro_lives:
                u "Good, maybe after this you'll become one of us."
                e "One of you?"
                u "Yes, but first, bring the runaways back to me, then we'll talk about celebration."
            else:
                u "Good, then."
            "The leader hands you a small wolf-shaped whistle."
            u "We found their scent near the northeast of the split trails ahead, so you just need to enter their secret little hiding place."
            u "And when you let their guard down, blow on this. We'll take over from there, and catch them alive."
            "You haven't killed anybody that's not a monster, even if you can convince yourself to do this..."
            "The guilt of sending the werewolves to their death sentence are going to kill you alive."
            u "You should go now, catch them while they're least expected."
            "You nod, and you politely take your leave, walking past the werewolves that guard the entrance."
            "It's a choice you must make, and it makes you nauseous to be in control of someone else's life directly."
            "But deep down you know there's another option, to not participate in the sick game of Uffe's, ever again."
        "Decline":


            $ quest36.status = 100
            e "No, I'm not going to do it."
            u "Well then, you are dismissed."
            e "Is that it? Y-you are not going to do anything else?"
            u "Do you want to live? If not, then keep talking, we'll take care of you as well."
            "You gulp, his threats are always successful in shutting your mouth, though you are also to be blamed."
            u "We'll catch those runaways with force, either way they're not leaving the forest."
            u "My people are just too good at killing, it's a shame they can't bring the runaways alive for me."
            "He pauses for a few seconds, and glances at you again."
            u "Are you waiting to be dismissed, or be our food?"
            e "Neither, but I wish you're not as cruel as you were meant to be."
            u "It's actually quite amusing that you think you have any say in other's decision."
            "Uffe sharpens his claw on the stone surface, urging you to leave the cave."
            u "We'll meet again, trespasser."
            "You turn away quickly, walking past the werewolves that guard the entrance."
            "There is no way Uffe is asking you to help kill those escaping the forest."

    "And that means you may never come back to the den again, at least until something changed."
    if quest26.status == True:
        "Hopefully, that change might come the day Wuldon takes his revenge, and you'll help him with all your heart poured out."
    jump Moonlit_Wolf_Den_Loop

label Uffe_Territory_Quest_Runaways:
    pause 1
    scene hiding_place with dissolve
    if quest36.status == 3:
        "You knock on the wooden plank again."
        "The werewolf peeks up."

        my "Do you have anything that helps my brother?"
        if LookForItem("Green Ointment", inventory):
            jump Uffe_Territory_Quest_Find_Cream
    elif quest36.status == 2:
        "You knock on the unsuspecting wooden plank, turns out, it's a door."
        "A sound from leaves cracking from behind reminds you that there are werewolves guarding outside the hiding place."
        "And then, you hear someone chattering through the other side."
        "Someone whimpered, very loudly."
        "Another unfamiliar voice spooks you away, until you notice he was addressing you."
        my "You're not a werewolf, who are you?"
        "You don't know who was talking from the other side, or how he can see you through the door."
        e "I-I'm from outside the forest, just wanted to take a rest after exploring the area."
        e "May I come in?"
        my "Hmm..."
        my "Rumma? Should we let him in."
        "The werewolf calls someone far away, you can hear someone coughing before he runs."
        my "F-fuck."
        "It seems the werewolf is taking care of someone inside the house."
        "You lean against the door, trying to listen to whatever was happening with the werewolves, but they were too far away."
        "After a few ganders, you notice a hole in the entrance that let you see through whatever inside the house."
        "But still, there's nothing notable except for the wooden planks sealed tight at the other side of the door."
        "A few minutes have passed, you dwindle around idly until you see a maned werewolf at the door."
        "That's when your eyes both met, but you both quickly avert your gazes."
        my "We don't accept any visitors right now."
        my "But... my brother, he needs something to heal his wound."
        e "Would a health potion help?"
        my "N-no, I've already tried it."
        "You hear the same whimper from someone far inside the hiding place."
        my "He needs something to apply on his wound, it's getting worse and he can't stop bleeding."
        my "Ever since the herbalist wolf disappeared, there's been no one in the forest that can help treat our sicknesses and injuries."
        e "Herbalist wolf?"
        my "He walks around the forest, do you not know him?"
        "The werewolf pauses over the door, seems like he's staring at the other direction."
        my "Can you help us? I must stay in case of any other werewolves coming in."
        $ quest36.status = 3
        $ quest36.qProgress(__("Get an ointment to treat a werewolf's wound"))
        if LookForItem("Green Ointment", inventory):
            jump Uffe_Territory_Quest_Find_Cream
    else:
        "You walk around, but find nothing."
        jump Dark_Forest_Map

    e "I- I don't think I have anything that can help him."
    my "That's alright, I'll think of another way."
    "Without another thought, he turns away."
    "You hear the footsteps of the werewolf leaving to tend to his brother, before you retreat from the door as well."

    jump Dark_Forest_Map

label Uffe_Territory_Quest_Runaways_End:

    "You approach the alpha once more."
    u "Congratulations, my little trespasser. The threat has been eliminated, as it should."
    u "Keep the whistle, as a reward."
    e "What are you going to do with them?"
    u "I'm sorry?"
    e "What are you going to d-"
    u "Look, you might not remember the rules in my forest for merely a second here. Let me reiterate."
    "The alpha cuts you off, he is visibly annoyed."
    u "I'll do with them however I want, and it's not something I will tell a trespasser."
    u "However, you seem visibly upset for strangers you know nothing about."
    u "Let me comfort you, the brothers are sound and safe, for all it's worth."
    e "You still haven't answered my questions."
    "Uffe chides."
    u "Now you've crossed the line. I don't really owe you an explanation, trespasser."
    u "But consider that you've contributed to the pack. I will forgive you."
    if vurro_lives == True or uffe_celebration == False:
        u "And mayhaps, come another time. We'll hold a celebration for the removal of all threats."
    "You remain silent, by now you know everything you say will be disregarded."
    "And despite your action, you were right, the guilt of blowing the whistle is building up on you."
    if vurro_lives == False:
        "Alongside what you've done to Vurro..."
    "It's not going to go away."
    $ QuestFinish(quest36)
    jump Dark_Forest_Map


label Uffe_Territory_Quest_Find_Cream:
    e "Uhmm..."
    pause 1
    "You scramble through your bag, and finds a canister of green ointment."
    e "Would this help?"
    "Through the hole, you raise your hand high enough for the wolf."
    my "What's that?"
    e "Ointment, it should stop the bleeding speedily. Ol- A lizard from outside the forest gave the recipe to me."
    my "That will help?"
    e "I'm pretty sure."
    "Clumsily, you throw it over the hole in the door, the concerned wolf catches the canister before it breaks on the floor."
    "He quickly rushes towards the back of the hut, muttering something very quickly."
    pause 5
    "You wait at the door, and it's been almost an hour passed before the wolf approaches you again."
    my "Thank you so much, I- I think my brother's getting better now, his bleeding has stopped and I wiped his wounds clean."
    e "T-that's great, I'm happy to have helped you."
    my "Do you want to come in?"
    e "Yes."
    "The werewolf flips open the wooden plank, and greets you politely."
    scene black with dissolve
    "It's only after entering the hiding place you notice how small it is."
    "And the werewolf is taller than you imagined, almost like a giant as compared to the compact household he's living in."
    "The hut is buried under simple sticks and stones, with a tunnel towards what you presume to be where the other werewolf is at."
    my "S-sorry, it's small but we are not staying for long here."
    "You sit on the leafy mat alongside the werewolf."
    tt "My name's Tetto, it was really nice to meet you."
    e "My name's [e]. Thank you for having me here, Tetto."
    e "Where are you going?"
    tt "Somewhere far away from the forest, once my brother can walk again."
    e "I apologise if I stepped out of line, but what happened to your brother?"
    "The werewolf scratches his head."
    tt "Well, we were sick of the hunting, ever since the previous leader went feral in that cave, we were forced back to hunt and gather food for the alpha."
    tt "And... we got into a fight, with one of the elders of the pack, he found out that we were trying to escape from the forest."
    tt "My brother fought hard to protect me, but his shoulder was clawed before the elder took his last breath."
    tt "So we hid, I found this place with a natural shelter, trying to get something to heal his wound up."
    e "Are the other werewolves still chasing after you?"
    tt "I presume so."
    tt "We'll finally leave this place as soon as my brother can finally walk. There were so much stuff we wanted to see."
    tt "You know, so much to take a gander."
    "The werewolf exclaims, with a bit of excitement in his eyes."
    tt "My brother said the goats looked funny, but I've never seen them ever before."
    tt "He said they have a pair of horns, like yours. W-wait, are you a goat?"
    e "N-no, we just looked similar."
    tt "Well, I wasn't the wisest one in terms of faces and other people."
    "He chuckles, staring back at the room."
    tt "Do you like herbs? I've read from the herbalist wolf while he was still around."
    tt "He collected everything in the dark forest, sometimes even outside our territory, and I helped him grind the herbs together."
    "He points towards the mortar and pestle on the floor, it's almost all green now, with the center being rough like barks of a tree."
    tt "I've heard of the dragon alchemist from him, perhaps after leaving the forest, we can visit him for his herbs."
    e "You're really talkative, aren't you?"
    tt "Hah, sorry, I was just too excited to finally leave the forest. It has been a mess ever since Uffe took control again."
    tt "And my brother, he wasn't the type of werewolf who likes to be told what to do."
    "Tetto exclaims as he squeezes the back of his neck."
    tt "Anyway, thanks for the ointment, I think my brother's going to like you a lot when he wakes up."
    e "You're welcome."
    "Staring at the werewolf, you try to put away the thought to blow the whistle and potentially killing them both."
    "After all, how is it possible for you to do it? The guilt will surely drown you alive."
    "You nudge on the whistle intensely, trying to resist the idea to ever get your mouth near it."
    "And to think about the decision, it's not even worth, for whatever Uffe had in plans for you, there's no way you'd risk the lives of two innocent werewolves."
    pause 2
    "You thoughts was put to a sudden halt as you hear the series of whines again."
    tt "O-oh?"
    tt "It's my brother. I'll check on him for just a few moments."
    "The werewolf climbs on the tunnel, and soon you are left alone..."
    "You take out the whistle, there's no pulling out now."
    menu:
        "You must make a decision."
        "Leave and blow the whistle":
            "There's no way you can blow it here."
            pause 1 
            scene hiding_place with dissolve
            $ tetto_escaped = False
            "You leave the place with a look of sorrow, before barely sealing the plank at the entrance."
            "Indecisively, you close your eyes, and let your mouth blow a soft wind through the whistle."
            "A loud sound emulating wolf howling can be heard through the whole forest."
            "You run away from the shelter, knowing what will happen to them."
            "And you do not even dare to look behind."
            "You do not have the courage to see what you're doing to them."
            "Soon, a group of werewolves emerges from the corner, running in opposite direction of yours."
            "One of the werewolves stops you."
            ww "You got their doors unlocked?"
            "You nod."
            ww "Good job there, Uffe will be very pleased."
            "You wish it was a sarcasm, but he genuinely believed you did a good thing."
            e "Are they going to die?"
            ww "What? Hah- If we wanted to kill them, they'd die a long time ago."
            ww "We just didn't want them to escape, or die that easily."
            "The werewolf points at his head, and grins at you menacingly."
            "You are not sure what he means, how would Uffe not kill a threat to their own pack."
            "What's even the purpose of catching them alive?"
            ww "Leave the hard works to us, little prey."
            ww "Oh, and you should go tell Uffe about the good news, I'm sure he has something better ready for you."
            "The werewolf chuckles, before heading the direction to the shelter."
            scene black with dissolve
            "And you are left standing there, speechless."
            "You can only hope they have fled, somehow. Even if it's unrealistic."
            pause 3
            $ quest36.status = 4
            $ quest36.qComp(_("Report to Uffe"))
            jump Dark_Forest_Map
        "Tell them to escape":
            $ tetto_escaped = True
            e "Hey, Tetto, you need to leave... now."
            tt "W-what?"
            e "Carry your brother and leave the forest, the werewolves are chasing after you."
            e "They are coming here right now! So please... run."
            "You shout at the other end of the tunnel, the werewolf seems to be pondering for a moment."
            "He ponders for a moment, before looking outside through a peephole."
            "It only get him much more anxious, as he immediately rushes towards his brother."
            tt "Fuck- you're right. Okay, I'm so lucky he built a secret exit right here, I'll carry my brother."
            e "I'll do whatever I can, please, run as far as you can."
            tt "Alright, alright. I can do this."
            "Tetto groans as he carries his brother on his back, you can still hear a few whimpers from the brother."
            tt "[e], may we meet outside."
            "A faint gruntle echoes from the other end of the tunnel. And you can only hope they've escaped."
            "You wait for a few seconds alone in the hiding place."
            "They must not catch them until you blow your whistle, as you believe."
            e "Hey! I should accompany you two, it's too dangerous."
            "You shout loudly, but receive no response except for your echoes."
            "Despite the silence, you climb into the tunnel, hoping to catch up to the brothers."
            "With a certain ease and dust on your body, you reached where his brother was resting."
            "There are an incredible amount of blood left behind, almost enough to stain a whole carpet."
            "But, without another thought, you hurry to flip away layers and layers of leaves hiding the other exit."
            scene dark_forest with dissolve
            "Running into several huge bushes, you see the back of a werewolf moving slowly above the grasses."
            "When you walk up to the werewolf's side, you realise he's sleeping soundly, being carried by his brother underneath."
            e "Tetto, I figured maybe you can use an extra pair of eyes."
            tt "Hnnngh... Good."
            "Tetto gruntles as his brother almost slips off."
            tt "I figured that sooner or later, they're gonna track down Rumma's blood. Luckily he's left his share of evidence back there."
            tt "It's how we work, even if we can't kill our preys, they'll just keep bleeding until we finish our jobs."
            tt "Didn't h-hnngh... think we'd be the prey today."
            "You walk alongside the wolf, peeking from left to right."
            tt "Anyway, usually we have to move past the nightwatches, but I know a path ahead that the werewolves seldom use."
            tt "The path is longer, but doable. Walt taught me about this path, he was the herbalist wolf."
            tt "He was fairly old, and it's been a while since I last saw him, maybe the toxic herbs just eventually caught up with him."
            tt "Or, maybe it was Uffe."
            "Tetto glances at you."
            tt "But, still. Back to the business, I think we shouldn't be talking that much."
            e "Yeah? You think so?"
            tt "Forgot we were supposed to be fleeing."
            "Tetto picks up his pace from merely walking, and you follow closely."
            tt "See anything funny?"
            e "Ehm, nothing yet."
            tt "My brother is heavy, I thought I should let you carry him but then you're just this tweenzy little small dude."
            tt "Not saying small dudes are weak but his sheer weight is going to break your bones."
            tt "Of course, we're born heavier and our strength comes with that extra weight."
            "The werewolf continues rambling about random talks, which just causes you to be much more nervous looking around."
            tt "Blessed by our ancestors, and Metsikka, we'd be able to shred down anyone in the forest."
            tt "But we have abandoned our gods, as they said, our prayers went unheard for centuries almost."
            e "Gods?"
            "You look backwards, luckily no one is tailing you right now."
            tt "Ancestors with quite a bit of power. Every tribe has their own."
            tt "But we're not really a tribe, we don't do rituals and festivals."
            tt "Wait, are we a tribe?"
            e "Maybe."
            "He's getting increasingly annoying while you're trying to focus on any potential threats."
            tt "Probably a better tribe than those at the sea."
            "Tetto chuckles as you hear a weak snoring from the back."
            "The maned werewolf turns his attention to his brother, who is sleeping comfortably on his back."
            tt "I wonder what he's dreaming about, he's been having nightmares since getting clawed."
            tt "It's no-"
            e "Are you sure people aren't going to hear that?"
            tt "What, the snores?"
            tt "It's the first time I've heard him snore since we escaped, and it was all because of me."
            e "I mean, it's that, and you're really talking like we're not hiding from a whole pack of vicious werewolves."
            tt "Ha, well. And you're talking like my brother. He always did all the worrying for me."
            tt "Should've helped when he built the small cave alone, I think that's when the elder got his eyes on him."
            "You continue listening to Tetto as he half-heartedly whispers, but something caught onto your eyes."
            with vpunch
            e "Duck!"
            tt "Huh? Where- Oh!"
            "Tetto abruptly pauses mid-sentence as his gaze fixates upon a familiar figure, it was another werewolf."
            "You drag him behind a weirdly bulky tree, just in time before the werewolf turns towards your direction."
            ww "Could've sworn I smelled something suspicious here."
            "The werewolf tilts his head left and right, trying to make sense of the scent probably from the wounded brother."
            tt "{size=25}So, how are we going to get out of this?{/size}"
            e "{size=15}Are you seriously still talking while we're being tracked down?{/size}"
            tt "{size=15}Sorry!{/size}"
            "At last, he finally quiets down. But that doesn't stop the werewolf's pursuit."
            "Instead, you notice another similar figure approaching."
            ww "Got any tails? Uffe's gonna be pissed if we let them escape."
            ww2 "No, but I just received order from the alpha. We better take them back as soon as we can."
            ww "Including the small one?"
            ww2 "No."
            "The werewolves talks amongst themselves nonchalantly, sharpening their claws as they search."
            "You hold your breath behind the giant tree, and signal Tetto to escape as soon as the werewolves leave."
            ww "Someone's been here."
            "The two look across the path you just took, and they immediately follows the scent down there."
            "You continue to hold your breath, just a few more seconds before they leave."
            pause 1
            "One... More..."
            with vpunch
            "Alas, you flinch and step on the dry branches, eliciting a loud cracking sound."
            "Tetto puts down his sleeping brother silently, he knows the werewolves turned around."
            "And he was right, they are approaching the source of the sound with no other way to escape."
            tt "{size=15}Prepare to fight, [e]. We need to make this quick.{/size}"
            "A black snout pokes from behind the tree, revealing the inquisitive dark werewolf."
            with vpunch
            ww "Ha, caught you."
            ww2 "And his little accomplice."
            "You have no way to escape now, being caught between the two werewolves."
            tt "W-well, let's get this over with."
            jump werewolf_tetto_battle
label Uffe_Territory_Quest_Inquire:

    e "Uffe, what do I need to do again?"
    "The werewolf leader gives you a side glance, and it's demeaning as usual."

    if quest34.status == 2:
        u "Get to the Hollow on your map, clear shrubs. And retrieve the amulet."
        e "Uhm, where's the amulet?"
        u "I've assigned a fellow capable hunter where it lies, help him, and you'll get my amulet."
        e "O-ok."
    jump Uffe_Normal_Talk



label Uffe_Normal_Talk:

    show uffe normal with dissolve
    menu:
        u "What's the matter, trespasser."
        "Report about the Whispering Hollow" if LookForItem("Moonstone Amulet", inventory) and quest34.status >= 4:
            jump Uffe_Territory_Quest_Return_After_Amulet
        "Inquire about the Quest in the Hollow" if quest34.status != False and ((not LookForItem("Moonstone Amulet", inventory) or quest34.status != 4) and quest34.status != True):
            jump Uffe_Territory_Quest_Inquire
        "Ask about his plan after killing the feral werewolf" if quest34.status == False and quest22.status == True and quest22.completed_date < timenow.day - 3:
            jump Uffe_Territory_Quest
        "Ask about the next step of his plan" if quest36.status == False and quest34.completed_date < timenow.day - 1:
            jump Uffe_Territory_Quest_Start_Runaways
        "Report about the escaped werewolves" if quest36.status == 4 and tetto_escaped != True:
            jump Uffe_Territory_Quest_Runaways_End
        "Ask about the price" if quest22.status == False:
            e "Why can't you just tell me about the stone?"
            u "Because nothing is free in this world, trespasser."
            u "You do me this favor and I'll return one to you."
            u "All's fair in the world."
            e "Alright. What do you need from me?"
            u "To help me kill someone."
            e "What?"
            u "Calm down. It's a creature who has been doing harm to the den."
            e "What is it?"
            u "It's a werewolf who has gone feral."
            e "What is this about a feral werewolf?"
            u "It's a curse that has struck our kind."
            u "One of us has been cursed and turned feral."
            u "It will attack everything on sight."
            e "Why don't you send your pack after it if it's so dangerous?"
            u "The pack can't afford to be affected by its curse."
            u "And they're not feeble enough to squeeze through the cave."
            u "You need to pull your weight, trespasser if you wish to know more about the stone."
            u "You should be able to find the beast hiding in the cavern."
            e "Fine. Any advice to deal with the feral werewolf?"
            u "Don't die."
            u "To ensure that you are not just shitting me, I will need some proof."
            e "What else do you need me to do?"
            u "Fetch me the feral's nipple rings."
            e "Nipple rings?"
            u "Yes."
            "The alpha works his pec."
            u "Similar to these."
            "You have to admit. It's quite sexy on him."
            u "Bring me them and I'll tell you more about the stone."
            $ QuestBegin(quest22)
            $ quest22.qProgress(__("Visit the Split Trail"))
            $ split_trails.discovered = True
            jump Uffe_Normal_Talk
        "Report about the feral werewolf" if quest22.status == 3:
            if not vurro_lives:
                u "Hello again, Trespasser."
                e "...Hello Uffe."
                "Uffe's eyes widen, and his mouth twists in a predatory grin."
                u "I smell his scent on you."
                u "You have killed the feral then."
                "His body language shows pure, unadulterated greed."
                e "Yes. I have."
                e "The cave he was in collapsed on top of him."
                u "Excellent! You have done well little trespasser."
                u "Now, hand over the nipple rings."
                "You quickly fumble with your belongings until you pull out the rings."
                u "I have been waiting a long time for that thing to be dead."
                u "This calls for a celebration."
                "Uffe turns to leave, but you stop him."
                e "Uffe, what about our deal?"
                "He turns back around, confused."
                e "The one where you tell me about the stone in return for me killing the feral?"
                u "Oh, yes, our deal."
                "Uffe puts on a look of feigned innocence."
                u "The stone isn't ours."
                "He once more turns to leave."
                e "Wait, what?"
                e "Where are you going?!"
                u "To plan the celebration. Much meat needs to be hunted, and ground cleared for breeding."
                "You are too angry to process that last bit at this point."
                e "What the fuck?!"
                e "I thought we had a deal!"
                "Uffe turns to look at you, a devious look on his face."
                u "We did."
                u "I told you more about the stone, didn't I?"
                "Uffe leaves you alone with that."
                pause 1
                "You stand there, frozen, for longer than you know."
                "You only snap back to reality when a werewolf bumps into you."
                pause 1
                "You killed somebody for him."
                pause 1
                "You killed somebody for him, and he spits on your face as he did their life."
                pause 1
                "What have you done..."
            else:
                u "Hello again, Trespasser."
                e "...Hello Uffe."
                "Uffe's eyes widen, and his mouth twists in a predatory grin."
                u "I smell the nipple rings on you."
                u "You have killed the feral then."
                "His body language shows pure, unadulterated greed."
                e "Yes... I have."
                e "The cave he was in collapsed on top of him."
                u "Excellent! You have done well little trespasser."
                "Your terrible attempt at lying goes completely unnoticed as he is utterly enraptured by the knowledge of the feral's death."
                "It's to the point where you can see saliva dripping from the corner of his mouth."
                u "Now, hand over the nipple rings."
                "You quickly fumble with your belongings until you pull out the rings."
                u "I have been waiting a long time for that thing to be dead."
                u "This calls for a celebration."
                "Uffe turns to leave, but you stop him."
                e "Uffe, what about our deal?"
                "He turns back around, confused."
                e "The one where you tell me about the stone in return for me killing the feral?"
                "You did cheat your part of the bargain, but... he doesn't need to know that."
                u "Oh, yes, our deal."
                "Uffe puts on a look of feigned innocence."
                u "The stone isn't ours."
                "He once more turns to leave."
                e "Wait, what?"
                e "Where are you going?!"
                u "To plan the celebration. Much meat needs to be hunted, and ground cleared for breeding."
                "You are too angry to process that last bit at this point."
                e "What the fuck?!"
                e "I thought we had a deal!"
                "Uffe turns to look at you, a devious look on his face."
                u "We did."
                u "I told you more about the stone, didn't I?"
                pause 1
                "Uffe leaves you alone with that."
                pause 1
                "You stand there, frozen, for longer than you know."
                "You only snap back to reality when a werewolf bumps into you."
                pause 1
                "While it might be hypocritical to feel betrayed by his taking advantage of a loophole in the bargain, you can't help but feel spit on."
                "And perhaps feel the inkling of a desire for revenge blossoming in your bosom."
            $ pc.gold += 150
            "You received 150 gold."
            $ QuestFinish(quest22)
            jump Moonlit_Wolf_Den_Loop
        "Ask about the werewolves":
            e "How is life in the dark forest?"
            u "Life is hard. We stick to ourselves and the world leave us be."
            u "That's why your presence here is disconcerting, trespasser."
            "He glares at you."
            e "What about the raids on the nearby goat tribe?"
            "The glare intensifies."
            u "I don't control the whole pack, trespasser. What they do outside the dark forest is beyond my control."
            "You have a feeling he's irked that you bring up this topic."
            e "How did you become the alpha?"
            "The werewolf grins proudly."
            u "The strongest always come out on top. The weaker ones are exiled or banished."
            u "There can only be one alpha."
            u "It's kill or be killed, trespasser."
            jump Uffe_Normal_Talk
        "Ask to stop werewolves' attack":
            e "Can you get the werewolves to stop attacking me as I travel through the forest?"
            u "No."
            e "Why?"
            u "Because no."
            u "Plus, if you can't handle a normal werewolf, you are of no help to me anyway."
            jump Uffe_Normal_Talk
        "That's all for now":
            e "That's all, thank you U-"
            e "Alpha."
            u "Good."
            jump Moonlit_Wolf_Den_Loop

screen Dark_Forest_Mappy():
    tag menu_bar
    zorder 99

    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "map_hover"
        hover "map_idle"
        style "footstep_button"
        action Return("To Entrance")
    imagebutton:
        xalign 0.39
        yalign 0.83
        idle "mapentrance"
        hover "mapentrancehover"
        style "footstep_button"
        hovered SetVariable("selected_location", dark_forest)
        action Return("To Entrance")
    imagebutton:
        xalign 0.43
        yalign 0.59
        idle "mapsite"
        hover "mapsitehover"
        style "footstep_button"
        hovered SetVariable("selected_location", forest_nightwatch)
        action Return("To DF1")
    if moonlit_wolf_den.discovered == True:
        imagebutton:
            xalign 0.53
            yalign 0.31
            idle "mapsite"
            hover "mapsitehover"
            style "footstep_button"
            hovered SetVariable("selected_location", moonlit_wolf_den)
            action Return("To Wolf Den")
    if split_trails.discovered == True:
        imagebutton:
            xalign 0.49
            yalign 0.41
            idle "mapsite"
            hover "mapsitehover"
            style "footstep_button"
            hovered SetVariable("selected_location", split_trails)
            action Return("To Split Trail")
    if whispering_hollows.discovered == True:
        imagebutton:
            xalign 0.31
            yalign 0.36
            idle "mapsite"
            hover "mapsitehover"
            style "footstep_button"
            hovered SetVariable("selected_location", whispering_hollows)
            action Return("To Hollow")
    if slumbrous_well.discovered == True:
        imagebutton:
            xalign 0.37
            yalign 0.49
            idle "mapsite"
            hover "mapsitehover"
            style "footstep_button"
            hovered SetVariable("selected_location", slumbrous_well)
            action Return("To Well")
    if cavern_entrance.discovered == True:
        imagebutton:
            xalign 0.65
            yalign 0.55
            idle "mapsite"
            hover "mapsitehover"
            style "footstep_button"
            hovered SetVariable("selected_location", cavern_entrance)
            action Return("To Cave Entrance")
    if chelforte_cavern.discovered == True:
        imagebutton:
            xalign 0.71
            yalign 0.59
            idle "mapsite"
            hover "mapsitehover"
            style "footstep_button"
            hovered SetVariable("selected_location", chelforte_cavern)
            action Return("To Cavern")
    if viscid_streams.discovered == True:
        imagebutton:
            xalign 0.27
            yalign 0.64
            idle "mapsite"
            hover "mapsitehover"
            style "footstep_button"
            hovered SetVariable("selected_location", viscid_streams)
            action Return("To Stream")

    if forgotten_sanctuarys.discovered == True:
        imagebutton:
            xalign 0.21
            yalign 0.34
            idle "mapsite"
            hover "mapsitehover"
            style "footstep_button"
            hovered SetVariable("selected_location", forgotten_sanctuarys)
            action Return("To Sanctuary")
    if quest31.status == 2:
        imagebutton:
            xalign 0.23
            yalign 0.30
            idle "mapsite"
            hover "mapsitehover"
            style "footstep_button"
            hovered SetVariable("selected_location", forgotten_sanctuarys)
            action Return("To Slime")
    if creek_thickets.discovered == True:
        imagebutton:
            xalign 0.11
            yalign 0.44
            idle "mapsite"
            hover "mapsitehover"
            style "footstep_button"
            hovered SetVariable("selected_location", creek_thickets)
            action Return("To Thicket")
    if selected_location != None:
        vbox:
            xpos 1635
            yalign 0.035
            xmaximum 265
            spacing 30
            frame:
                xpadding 10
                ypadding 10
                label "[selected_location.name!t]" text_color "#301410"
            label "[selected_location.description!t]" text_color "#111111" text_size 25
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
