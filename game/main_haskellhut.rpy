screen place_haskell_hut():
    zorder 10 tag place


    imagebutton:
        xalign 0.57
        yalign 0.99
        idle "bedroom_arrow"
        hover "bedroom_arrow_hover"
        style "walk_button"
        action Return("To Cabin")

    if haskell_location == "haskellhut":
        imagebutton:
            xalign 0.503
            yalign 0.726
            idle "haskell_idle"
            hover "haskell_hover"
            action Return("Haskell")


label main_haskell_hut:
    $ current_location = "Haskell Hut"
    $ renpy.music.play(mHaskell, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)

    $ timenow.minute += 3
    $ timenow.passTime()
    if isNight():
        scene haskellhut_night
    else:
        scene haskellhut
    with dissolve
    if quest30.status == 2:
        jump Haskell_Report_Wuldon_Curse
    if haskell_tut <= 2:
        jump Haskell_Meet_Hut
    if quest24.status == 2 and LookForItemNumber("Chrysanthemum", inventory) >= 3:
        jump Haskell_Report_Trinket_Quest
    if quest44.status != True and haskell_dialogues.get("Licking", 0) != 0:
        $ QuestFinish(quest44)
    show screen menu_buttons
    window hide
    call screen place_haskell_hut

    if _return == "Haskell":
        jump Haskell_Dialogues
    if _return == "To Cabin":
        jump main_alchemists_cabin
    jump main_haskell_hut



label Haskell_Dialogues:



    hide screen menu_buttons
    if isNight():
        scene haskellhut_night
    else:
        scene haskellhut
    with dissolve
    show haskell normal
    with dissolve

    if haskell_tut == 3:
        if haskell_dialogues.get("Kiss", 0) > 0:

            h "Well hello there, kiddo."

            h "Bringing some good news for your old dragon again?"

        elif renpy.random.random() > 0.5 and isNaked():

            h "Lost your clothes to the monsters again?"

            e "Uhh."

            e "U-uhmm... I felt a little hot today."

            h "I think the word you're looking for, is audacious."

            jump Haskell_Normal_Talk

        h "mmmph..."

        h "M-mm!! Hey! Didn't see you there."

        e "Hey, Haskell!"

    jump Haskell_Normal_Talk

label Haskell_Normal_Talk:

    menu:
        h "So, how are you doing, [e]."


        "Ask about another Tasting Session" if quest44.status == True and haskell_dialogues.get("Kiss", None) == False and haskell_dialogues.get("Loopable Oolong", False) == False:

            jump Haskell_Ask_Oolong_After

        "Get another Tasting Session" if haskell_dialogues.get("Looping Oolong", False) == True:

            jump Haskell_Ask_Loopable_Oolong

        "Ask about your performance on him" if haskell_dialogues.get("Kiss", False) == True:

            jump Haskell_Ask_Kissing

        "Ask about the research on buggbears" if quest08.status == 2:

            jump Haskell_Buggbear_Quest

        "Ask about the Oolong Tasting" if quest44.status == False and haskell_dialogues["Dialogue"].get("Apothecary", False) and pc.level >= 14 and not haskell_dialogues["Dialogue"].get("Oolong Get In", False):

            jump Haskell_Oolong_Quest_Begin

        "Ask about the Oolong Tasting" if haskell_dialogues["Dialogue"].get("Oolong Get In", False) and quest44.status == False:

            jump Haskell_Oolong_Quest_Begin_Back_In

        "Ask about the Snowbound Summit" if quest44.status == 2:

            jump Haskell_Oolong_Quest_Summit

        "Report about the Oolong Leaves" if quest44.status == 3 and LookForItem("Oolong Leaves", inventory):

            jump Haskell_Oolong_Quest_Back

        "Ask about the Oolong Tasting" if haskell_dialogues.get("Preparing Oolong", False) == True and haskell_dialogues.get("Oolong Finish Day", 0) < timenow.day:

            if haskell_dialogues["Kiss"] == True:
                jump Haskell_Oolong_Tasting_Kiss
            else:
                jump Haskell_Oolong_Quest_Tea_Tasting

        "Ask about the Oolong Tasting" if quest44.status == 4 and haskell_dialogues.get("Oolong Finish Day", 0) < timenow.day:

            jump Haskell_Oolong_Quest_Tea_Tasting

        "Ask about the Oolong Tasting" if quest44.status == 4 and haskell_dialogues.get("Oolong Finish Day", 0) >= timenow.day:

            jump Haskell_Oolong_Quest_Waiting

        "Ask for Strength Potions" if task01.status == 2:

            jump Haskell_Potion_Order

        "Ask what's going on with Haskell" if quest14.status == True and taskAvailable(task06, quest14) and task06.completedtimes == 0:

            jump Haskell_Herb_Fetch_Task

        "Fetch some herbs for Haskell" if quest14.status == True and taskAvailable(task06, quest14) and task06.completedtimes > 0:

            jump Haskell_Herb_Fetch_Task

        "Ask about the herb fetching task" if task06.status == 2 and LookForItemNumber(herbofchoicy, inventory) < 3:

            jump Haskell_Herb_Fetch_Task_Inquire

        "Report for herb fetching task" if task06.status == 2 and LookForItemNumber(herbofchoicy, inventory) >= 3:

            jump Haskell_Herb_Fetch_Task_End

        "Ask for Strength Potions" if task01.status == 3 and haskell_potion_day < timenow.day and not Haskell_Promise:

            jump Haskell_Potion_Order_Finish

        "Ask if the potion is ready" if quest08.status == 3:

            jump Haskell_Buggbear_Wait

        "Ask about the magic that took you here" if quest24.status == False and quest08.status == True and quest08.completed_date + 2 < timenow.day:

            jump Haskell_Trinket_Quest
        "Ask about Haskell's Apothecary":


            jump Haskell_Ask_Apothecary

        "Ask about his Special Request" if timenow.day >= 15 and quest08.status == True and quest14.status == False:

            jump Haskell_Minotaur_Dungeon

        "Report about the minotaur's essence" if quest14.status == 2 and LookForItem("Minotaur Essence", inventory):

            jump Haskell_Report_Minotaur_Dungeon

        "Ask about your outfit" if quest09.status != False and quest09.status != True and opinions_Outfit[8] > 0:

            jump Haskell_Outfit_03

        "Ask about Ole's sickness" if quest15.status == 2:

            jump Haskell_Sick_Quest

        "Ask about after Ole's sickness" if quest15.status == 4 or quest15.status == True and sick_ask[1] == 0:

            jump Haskell_After_Sick_Quest
        "Ask about Haskell's clients":


            jump Haskell_Ask_Clients
        "Ask how Haskell is doing":


            jump Haskell_How_Doing
        "That's all for now":


            jump Haskell_Dialogues_End

label Haskell_Ask_Clients:

    e "Haskell, can I ask you more about your clients?"

    menu:
        h "Who do you want to know, kiddo."


        "Ask about Gwyddyon" if gwyddyon_tut > 1:

            jump Haskell_Ask_Gwyddyon
        "Ask about Goat Tribe":


            jump Haskell_Ask_Goat_Tribe
        "Ask about Lusterfield{#HaskellAAL}":


            jump Haskell_Ask_Lusterfield
        "Ask about other business":


            jump Haskell_Ask_Other_Business
        "That's all I need":


            jump Haskell_Normal_Talk

label Haskell_Ask_Gwyddyon:

    e "Hey, Haskell. Do you supply potions to Gwyddyon?"
    h "Yes, The Ardent Cauldron was an old name. You should know that."
    e "What's it like working with him?"
    h "Nothing fancy. He collects my potions with a cart every month, usually comes with plants he deemed useful for me."
    e "Do you two talk?"
    h "No. I usually banish him right before he sells me one of his blue crystals."
    h "Why do you ask? did the oaf mentioned me?"
    e "Well, something like that, not in a good light."
    h "Hmmph... It is flattering to know someone has put so much attention onto me."
    h "But if there's anyone that knows close to everything about every goat, it's him."
    e "O-oh... Thanks, Haskell."
    h "Mpph..."
    "Haskell takes another sip."
    jump Haskell_Normal_Talk

label Haskell_Report_Wuldon_Curse:

    if timenow.day < quest30.start_date + 1:

        "As soon as you open Haskell's door, you see the dragon sitting in the corner, a bubbling vat of dark red liquid in front of him."

        show haskell normal at l1 with dissolve
        show wuldon nobo at r1 with dissolve

        "His eyes don't even flicker towards you, so attentively is he looking at the mixture."
        h "Please do not distract me. Wuldon - who introduced himself only after I asked - is only allowed to be here because he is quiet. If creepily so."
        "It seems the dragon is a bit annoyed that you didn't introduce Wuldon to him, causing what appears to have been an awkward, if brief, conversation."
        "Speaking of, Wuldon is sitting over at the table, looking at the stone, now covered in considerably less blood."
        "You take that as your queue to leave."
    else:


        "Enough time has passed that Haskell should probably be done with his analysis."

        show haskell normal at l1 with dissolve
        show wuldon nobo at r1 with dissolve
        "That's what you tell yourself as you head towards Haskell's house, at least. Part of the active effort to shove the guilt and desire to get this all over with to the back of your mind."
        "Whatever other thoughts were running in your head come to a sudden stop as you see Wuldon staring straight at you from inside Haskell's house."
        "As soon as your eyes meet, Wuldon breaks contact and sits down expectantly, looking over at something inside the house."
        "Quite possibly against your better judgment, you head inside."
        "Haskell is sitting across from Wuldon, trying very hard not to look at the werewolf's mile-long stare, drumming his fingers on the table and looking at the door."
        pause 1


        h "There you are, [e]. We can get started now."
        "His voice is a mix of dread and excitement, fitting for someone that hates work, but is dearly looking forward to no longer having a terrifying husk of a man in his home."
        h "I spent the last few days analyzing Vurro's blood, to mixed success."
        w "Tell us anything useful you found."
        "Haskell shoots the werewolf an irritated glance, which of course has no effect on Wuldon's face."
        h "Alright. Vurro was definitely cursed."
        h "His blood was highly reactive to curse-related catalysts, and practically inert to everything else."
        "Curses are unfamiliar territory for you - this is probably something you should ask questions about."
        e "What exactly do you mean by a curse? Does that tell us anything about who could have done this?"
        pause 1
        "Haskell gives you a slight nod, approving of your attitude."
        h "A curse is negative magic cast upon any person or thing."
        h "The most famous curses are those used on others, but they have just as often been used on water sources or farmland."
        "The red dragon sighs in frustration before broaching the next point."
        h "Regarding who did it, all it tells me is that the caster was most likely some form of shaman or mage."
        h "Whether Vurro had the curse cast on him by that person directly, I do not know. There are ways to spread curses even without being able to cast magic yourself, but that requires access to a previously existing curse."
        "Wuldon breaks his silence, the topic drawing his attention."
        pause 1
        w "Explain. How would you spread it, and what would be a curse source."
        "Haskell gives him a concerned look, reaching out for tea that isn't there on reflex."
        h "I'd normally say that spreading a curse like that would be far too difficult, but I know that some of the slime materials from up north in slime country would make it quite easy."
        h "A mixture of any cursed material and rotten discharge, for example, would trap the curse quite easily. From there it would be a matter of mixing in some corrupting sludge, and you'd have a working vector."
        h "It would only be a matter of feeding somebody that cursed material, and they would be afflicted within moments."
        "Considering Wuldon's story, that is extremely doubtful, nobody was next to Vurro when he turned - but it isn't out of the question, you suppose."
        w "That sounds about right."
        "You give Wuldon a surprised look at the same time as Haskell gives him a saddened one."
        h "It would be a matter of finding out what cursed material they used, I suppose. That would be the best way to see who did it."
        h "Cursed material can be anything ranging from a patch of soil from cursed farmland, to the water of a cursed river... even Vurro's blood would work."
        h "Not that Vurro could have been cursed by his own blood, hehe..."
        pause 3
        "A painfully awkward laugh echoes throughout the hut - the first time the hut has ever had an echo. Haskell clears his throat awkwardly and carries on as if nothing had happened."
        h "I don't know of any other such items in the area, so finding that should give a large lead."
        "Satisfied that his explanations should suffice, Haskell begins to usher the two of you towards the door."
        "You still aren't satisfied with this, however, even if Wuldon is."
        e "Just to know, how would a mage, sorcerer, shaman... whatever, cast magic like this?"
        "An uncomfortable frown crosses Haskell's face, removing the happiness at getting you out of his house."
        pause 1
        h "They need your name or image to cast magic on you. The actual way they cast it is with words of great power, and sacrifice."
        "The two of you are out of the door now, as Haskell looks down at you from inside."
        h "Most curses would cost the lives of several people to cast. Those willingly given are worth more than otherwise, but either can be used. The same applies to the lives of the young as compared to the old."
        "A shiver goes down your spine as you imagine what that could mean for Vurro's curse."
        "...Or your presence in this world."
        e "Thank you, Haskell. I'll try and bring you some tea later."
        "Haskell smiles slightly, but loses it when he looks at Wuldon again."
        h "Maybe some other time. I've had enough of guests for a while."
        "You wince as you imagine spending more than an hour with Wuldon like this."
        e "Alright, well. I hope you enjoy the tea you do have then."
        "All you get is a nod in response, as Haskell turns and closes the door."
        scene black with dissolve
        pause 2

        scene alchemistscabin with dissolve
        show wuldon nobo with dissolve
        "You turn around to see Wuldon looking at you."
        pause 1
        w "Visit my house when you're ready to go to slime country."
        "The certainty in his voice fills you with unease."
        e "I was worried you'd suggest something like this after what you said earlier."
        e "Why... why would you spread the curse further? I get that it would be the ultimate revenge against Uffe to make him feral, but."
        e "Is that really worth it?"
        "A bit of Wuldon comes back up from the depths he's hit himself in, his calm veneer disrupted by grief and frustration."
        w "I'm not going to make Uffe a feral. He would enjoy the power it gave him, if anything."
        w "Even if you help me with killing Uffe, it's going to be two against a tribe and their warmongering leader."
        pause 2
        "You narrow your eyes at the werewolf."
        e "Okay, then what are you planning?"
        "Wuldon's melancholy morphs into of rage and guilt, a battle between morality and hatred writ across his face."
        w "Uffe has a second in command - a general of sorts. Someone I know has blood on their hands, and deserves the same fate as Uffe."
        pause 1
        w "If you're worried about proving it, the plan won't work if he isn't a vicious murderer. We will lure him into attacking and killing you on your own, only for me to grab him and shove the curse mixture down his throat."
        w "That way, we get rid of a threat, gain a body to fight on our side, and make a beast of a creature look like what it actually is."
        "He spits to the side as he talks about the general. It is clear Wuldon genuinely thinks less of him than a worm."
        e "Alright. I'll help you with that - but if I catch you trying to feed it to someone else, we're quits."

        if wuldon_meet_before_vurro:
            w "I should be the one worried about you killing an innocent person, don't you think."
        else:

            w "If I do such a thing, I fully trust you to kill me where I stand. You have a good track record of killing things you think are monsters."
        pause 1
        "You can't help but grimace at that. He's not wrong to accuse you of that, but you wish he were."
        e "Fair enough. I'll see you at your house then."

        "Wuldon's face goes back to schooled neutrality."
        w "Yes. I'll see you there."

        $ QuestFinish(quest30)


    jump main_alchemists_cabin


label Haskell_Buggbear_Wait:

    if haskell_questday < timenow.day - 2 or ( haskell_questday < timenow.day - 1 and haskell_questhour < timenow.hour):

        e "Hey... Haskell? Is the deeds done?"

        h "Wha-... Oh. Right. The Potion. I was enjoying my cup of tea."

        h "Tell Ole to set a better price. Else you're going to come back again for restock."

        e "Oh..."

        h "How about this, I just teach you how to make the basic potions."

        e "Haskell, do you not like me visiting...?"

        h "No..."

        h "I'm tired of making potions. Look at the garden I have, all the ingredient to make the best tea."

        h "And I'm stuck here making meaningless potions."

        e "I thought they're the same."

        h "Yeah they're the same if you don't own a taste bud, bud."

        h "So, here's the potions, all 30 of them."

        e "Thanks, Haskell, I really appreciate your help."

        h "Yeah, anyways, there's one more thing."

        h "I'll teach you how to make potions. All of them basic ones, health, magic..."

        h "But... promise me if Ole ask you to bring him potions again, you'll make the potions for him instead."

        e "Haskell, I'm not sure if you should lie to Ole like that."

        h "Well. I'll tell him when I need to tell him."



        menu:
            h "So? Deal?"
            "I'll make the potion for Ole":



                $ Haskell_Promise = True

                e "Alright, I'll make them."

                h "And... don't tell Ole about it, alright?"

                e "Hmm."

                h "Alright?"

                e "Yeah, yeah."

                e "Did Sebas talk about this to you as well?"

                h "Well he's not that good at making potions anyways, did you see that clumsy lion try to grind his herbs?"

                h "No, Ole will see the difference instantly."

                e "Oh... So, you think I can do it?"

                h "Sure. I've seen your samples. Looks good enough."

                h "Here's your recipes. If he does ask you again, just tell them I made it."

                h "Here's the health, and mana potion recipe, and strength."

                e "Alright."

                h "Good, thanks kiddo."

                $ quest08.qComp(__("Return and Report to Ole"))

                $ discoveredrecipe.append(hppotionrecipe)

                $ discoveredrecipe.append(mppotionrecipe)

                $ quest08.status = 4
            "You need to make them yourself":


                $ Haskell_Promise = False

                e "I can't lie to him."

                h "Come on, kiddo. Don't be a douchbag."

                e "You should tell him yourself that you don't want to make potions anymore."

                h "I can't."

                "Haskell takes a moment, seemingly pondering the possibility ahead of him."
                h "..."

                h "Alright, keep this between us."

                h "Just don't tell Ole I asked you about this."

                e "You'll keep making the potions for him?"

                h "Sure, Sure."

                h "Right."

                $ quest08.qComp(__("Report to Ole"))

                $ quest08.status = 4

        h "Oh, I almost forgot. The Balm."

        e "You said you were making it for the buggbears?"

        h "Yeah. Right. I still need some time to perfect the recipe."

        h "Come back later, again. I'll talk to you about it."

        e "Alright, thank you so much anyways, Haskell."

        h "Sure."

        $ quest08.description = _("As my courier job, Ole told me about helping him get potion from an old friend. {p} I need to report back to Ole for the 30 strength potion.")

        $ addItem("Strength Potion", inventory, 30)

        $ discoveredrecipe.append(strengthpotionrecipe)

        jump Haskell_Normal_Talk
    else:


        e "Hey, Haskell. Are you ready with the potion for Ole?"

        h "Yes, uhhh, just a few adjustment and here and there..."

        h "No."

        e "Alright."

        h "Come back later, alright. Patience is a virtue."

        e "You seem to have a lot of patience for your potions."

        h "A watched pot never boils, your potions will be back in no time."

        e "Hmmph..."

        jump Haskell_Normal_Talk

label Haskell_Buggbear_Quest:

    if LookForItemNumber("Buggbear Saliva", inventory) >= 2:

        e "Hey, Haskell. I've got the... Saliva you need."

        h "Sure, Sure. But what's the problem with those, liquid."

        e "Uhh... it's just saliva."

        h "Look, I don't mind if you get too along with the buggbears, just take a bath or something."

        e "I've told you, it's just spilt saliva... not anything you're thinking of..."

        h "Alright. Alright. It was merely a joke, and not that there's any problem with buggbear cum."

        "You stare at the dragon."

        h "But thanks for your hard work anyways."

        e "Can I get the strength potion?"

        h "About that, I think I haven't brew them yet."

        h "Don't look at me like that, kiddo. I-I uhh... I'll do it right away. With your saliva."

        e "So, when can I get the potions..."

        h "Soon. Soon."

        h "Hey, come back in 2 days. You'll get your little potions."

        h "I'll teach you how to make it too. Don't get mad at me. At this age I'm just forgetful."

        e "Alright..."

        $ quest08.description = _("As my courier job, Ole told me about helping him get potion from an old friend. {p} I need to wait for two days for Haskell to complete his potions.")

        $ quest08.qComp(__("Wait for 2 days and Report to Haskell"))

        $ removeItem("Buggbear Saliva", inventory, 2)

        $ quest08.status = 3

        $ haskell_questday = timenow.day
        $ haskell_questhour = timenow.hour

        jump Haskell_Normal_Talk
    else:


        e "Hey Haskell. I was wondering, if you can help with the buggbear?"

        h "You've not gotten the saliva?"

        e "No, I forgot how to get them."

        h "Alright. You're getting more forgetful than me. I gave you two sedatives, just throw the stuff on them when they're weak."

        e "When will they be weak?"

        h "I don't know, half as strong? or at least a bit horny?"

        e "What if I lost the... powder."

        h "Then, well. Let's say I'll be too lazy to make you a new one. Just make another from scratch."

        h "I gave you the recipe already, just go to whatever workstation you have in Lusterfield."

        e "You mean Rahim's... sewing machine?"

        h "Whatever, just get some flowers and sew them up, I'm sure that'll work."

        e "Alright... I'll try."

        h "Go now. Before you accidentally sedate yourself with that powder."

        jump Haskell_Normal_Talk

label Haskell_Outfit_03:

    $ opinions_Outfit[8] += 1

    h "Are you here for another potion order? Haven't I told you that you can brew the potions yourself in the future?"

    e "No. I'm actually here because Ole asked me to."

    h "Huh? What is this about?"

    e "It's nothing serious. Ole notices that you wear robes often and our town tailor is attempting to make a robe as an everyday wear. We would like to get your comments on it."

    h "Your town tailor?"

    e "Yes. His name is Rahim."

    "Haskell examines the robe you're wearing with his eyes."

    h "Yes. He has good craftsmanship. Maybe I should visit him sometime to have him make me some new clothes."

    e "That is very high praise. I'll be sure to tell Rahim about it."

    "Haskell nods."

    "You don't move because you have something to ask Haskell but don't know how to phrase it."

    "Haskell notices you fidgeting."

    h "What is it? Is there anything else?"

    "You decide it's best to be direct."

    e "Haskell, is it true that you wear nothing under the robe?"

    "Haskell raises his brow at you."

    h "Wouldn't you like to know, kiddo?"

    "You realize how that sounded in your ears and you blush."

    e "I mean, in general. Not you specifically, but if you want to tell me..."

    "Haskell chuckles lowly."

    h "It's different for everyone. Some do and some don't."

    "You are quite disappointed and relieved that Haskell didn't hound you on the slip of the tongue."

    h "Personally, I don't wear anything underneath. Maybe one day I can show you."

    "Your face burns."

    jump Haskell_Normal_Talk

label Haskell_Ask_Lusterfield:

    e "Haskell, how's your business with Lusterfield?"

    h "I only do business with King's Pawn, Seb's little shop."

    e "Oh, you're supplying them the potions?"

    h "It's not business per se, I just gift them the potions."

    e "Why are you doing this?"

    h "It's their most popular products, every adventurer needs a few potions in their pocket."

    h "Just don't tell other I give them potions for free, it'll drag their prices down a lot."

    e "You seem really protective of them."

    h "Ole and I, had a really long history. He didn't really like me talking about it. One of the reason he left the hut."

    e "He used to live here?"

    h "Yeah, did you know about the Spikekeep?"

    e "Hmm... what?"

    h "Lizard Tribe?"

    e "I've never heard about it before."

    h "Makes sense for an outsider. Then I best not to tell you anything further."

    e "Why not?"

    h "Didn't I tell you? Ole doesn't talk about it, I don't talk about it."

    e "A-alright."

    jump Haskell_Normal_Talk

label Haskell_Potion_Order_Finish:

    "Haskell passes you 10 vials from off of a shelf."

    "They glow orange, and appear more viscous than mana or health potions."

    "You hope that's not because the slimeballs haven't been prepared properly."

    if task01.completedtimes == 0:

        e "I'll probably be here again in the future."

        e "Do you think we can talk about what's going on between you and Ole someday?"

        h "Ask me again some other time."

        h "Preferably after you've already asked him about it."

        e "Okay. I'll see you later, Haskell."
    else:


        e "Thank you Haskell, they look really nice. As usual."

        h "Good to know, now go and let this old dragon finish his tea."

        e "O-ok, see you later!"

    $ addItem("Strength Potion", inventory, 10)

    jump main_haskell_hut

label Haskell_Potion_Order:

    if Haskell_Promise:

        e "Hey there Haskell..."

        h "Hey, [e]! How is everything going? Get kicked out by Seb and Ole or something?"

        e "You still have a terrible sense of humor."

        e "No, I came because Ole wants more potions."

        h "Ah. You promised you would make those for me from now on."

        h "Now... if you're an honest courier, you'd be going out already."

        e "Haskell, this is getting weird for me to lie to Ole."

        e "I think he deserves to know at least."

        h "It's between me and Ole, and I intend it to stay this way."

        h "And you promised me about this one little thing. Can't you just help this old dragon out...?"

        e "Yeah, but-"

        h "No buts. Though, I might not complain if it's a butt like yours."

        e "What?"

        h "What what?"

        "Haskell waves his tea-holding hand to the door in front of you."

        "It seems like you'll have to go back and make the potions in Rahim's shop like you promised."



        $ task01.status = 3
    else:



        if task01.completedtimes == 0:

            e "Hey there Haskell..."

            h "Let me guess, Ole needs more strength potions?"

            e "Hehe, you got it..."

            h "...can I say no?"

            e "I mean, probably, but Ole would be sad."

            h "...fine, I can't argue with that."

            "The dragon gets up from his desk with an annoyed huff"

            h "All of these wonderful tea ingredients and I have to spend my time making these potions."

            e "You know, I still think you should tell Ole-"

            h "No."

            h "Sorry, just, absolutely not doing that."

            h "Look, come back in a day."

            h "The potions'll be ready then."

            e "O-ok... thank you, Haskell."

            $ task01.tProgress(__("Wait for a day"))

            $ haskell_potion_day = timenow.day

            $ task01.status = 3
        else:


            h "I can already see that you're here for more strength potions."

            e "How?"

            h "It's written all over your face."

            e "Really?"

            h "No, it was a lucky guess, but it was fun watching you get all confused like that."

            e "That's mean!"

            h "You should have thought about that before being fun to tease."

            h "...and cute, according to the lion."

            h "...and personal observation."

            e "What?"

            h "What What?"

            if renpy.random.random() < 0.5 or task01.completedtimes > 5:

                h "Hmm, Here are the potions."

                "Haskell hands you 10 strength potions, nonchalantly."

                e "Haskell, you actually prepared something this time?"

                h "This was from my last batch, kid."

                h "Now take them and go, I'll get more batches done next time you come."

                e "Hmm... where did you hide the real Haskell."

                h "Heh, don't make this old dragon spit my tea. I might actually do it if your joke is funnier."

                e "mhmm..."

                h "It was an exaggeration, kiddo. Take the potion now and have a great day, [e]."

                e "...You too, Haskell!"

                $ addItem("Strength Potion", inventory, 10)

                $ task01.status = 4
            else:


                h "Either way, come back in a day or so."

                e "Ah... Not ready?"

                h "Not started."

                e "O-ok. I'll be back to collect them."

                h "Have a nice day then."

                $ haskell_potion_day = timenow.day

                $ task01.status = 3

    jump main_haskell_hut


label Haskell_Ask_Goat_Tribe:

    e "Haskell, what's your relationship with the Goat Tribe?"

    h "Yeah I know them, they're called Kechioeren."

    e "Uh, Ke-K-eso... Kechieoeo-"

    h "Just call them Goat Tribe like the rest of us do."

    e "Hmmm... Kechi-kechiren?"

    h "Kechioeren."

    e "What does it mean?"

    h "Goat Tribe."

    e "Oh..."

    h "Or, in the ancient tongues, the flock."

    e "So what's your relationship with them?"

    h "Business relationship, I just give them potion, usually they need a lot of magic potions."

    e "Didn't you say they work on the primordial runes? The Spell... energy it gives them?"

    h "Yeah, but you still need potion if you go outside of the runes' influence."

    e "O-oh... that makes sense. I think."

    h "They're sending some folks to guard their huge tree though, it's the only few remnants of the rune's influence left there."

    h "They can't really extract the energy from there. I asked Furkan about this, but he insisted he should protect it."

    h "But you know, they're in a really vulnerable place."

    e "Did you tell Sebas and Ole about it?"

    h "Yeah, I don't know if the rest of the village noticed though."

    e "A-alright. Then, you're helping the goats?"

    h "I advised Furkan to stay calm, nothing else."

    e "Ok, thank you so much for letting me know."

    h "Sure, Sure."

    jump Haskell_Normal_Talk

label Haskell_Ask_Other_Business:

    e "Haskell, do you have any other business?"
    h "Lusterfield and Goat Tribe is the closest to me, other places were too far away."
    h "The bears... barely come here. It's very far away."
    h "And wandering merchants from the town need refill sometimes."
    h "But I usually charge them higher than Ole's shop."
    e "Oh... Alright."

    jump Haskell_Normal_Talk

label Haskell_Ask_Apothecary:
    $ haskell_dialogues["Dialogue"]["Apothecary"] = True
    e "Haskell, what's with your deal with potion making?"
    h "Common Potion making is actually really easy, but you won't get specific effects very easily without me."
    h "I'm not bluffing, it takes years to learn to be adaptive and creative with your potion invention."
    h "But I just make them for a living, buying myself herbs and stuff so I can afford to make myself some tea."
    e "Tea?"
    h "Tea. I make tea in my free time, it's refreshing, much tastier than those nasty ass potion."
    e "Oh..."
    h "I used to make tisana, it's not really that good."
    h "I've grown Kapor, Chamomile. My favourite is Oolong."
    if quest44.status == False:
        e "Uhh... Oolong?"
        h "It takes some time to make, you have to wait for the plant to wither first, under strong sunlight out there."
        h "After the process of oxidation, the leaves would twist and curl. One has to pay utmost attention to its timing and temperature."
        e "Oh... that sounds, interesting."
        h "I'll let you taste it once they're ready, but you need to be here for it though."
        e "It's a deal then."
        h "Good, Good. You'll know about it soon."

    jump Haskell_Normal_Talk

label Haskell_How_Doing:

    e "How are you doing, Haskell?"

    h "Mmmh drinking tea. You want some?"

    e "You know... your mug seems usually big."

    h "I need to drink much more of them to get its effect."

    e "Ohh..."

    h "You want the tea or not."

    e "Yeah, why not?"

    h "Come on, open your mouth."

    e "Wait- I can take the mug from you..."

    h "I can't trust you slurping up all my drink can't I."

    e "...Alright."

    "Haskell holds the back of your head gently, he pours down a few drops onto your tongue."

    "Then he tilts his mug to spill more into your throat, almost drowning you with his drink."

    e "A-coff- cof..."

    "You choke a little, only see Haskell sitting there and watching your reaction."

    e "Fuck, you made me cough, Haskell."

    h "Ha, Sorry about that. Like it?"

    e "You mean the tea. Yeah, it's pretty good."

    h "Good, good. Now let me drink my tea in peace."

    jump Haskell_Normal_Talk

label Haskell_Dialogues_End:

    e "I think that's all for now, thank you so much, Haskell."

    h "Yeah, take care out there."

    jump main_haskell_hut

label Haskell_Meet_Hut:

    hide screen menu_buttons

    "You peek inside the hut filled with green plants. If not informed by Ole, you would think it is owned by a gardener, not a potion maker."

    "Once you stare long enough, you can see different shapes of glasses scattered around the hut, you think they should be empty potion bottles."

    "Remembering what Ole told you about the potion maker, you feel safe enough to step into the hut."

    "But upon a greater look, you spot a white hair in your peripheral vision."

    "When you look closely to the weird hair, it becomes more obvious that it's a whisker from a dark red dragon."

    e "..."

    if haskell_tut == 1:

        show haskell normal at c1:
            linear 0.01 zoom 3
            linear 0.05 zoom 1

        show haskell normal

        my "What are you looking at?"

        e "Ahhh...!!"

        "You instinctively jumps backwards from the shock, and slam your head hard into the cabinet behind you."

        e "F-fuck!"

        e "I hit my head..."

        e "You scared me."

        "You suddenly realise the dragon is dangerously close to you, only a few inches apart."

        my "What, How did you hit your head again..."

        my "I've got ointment on my hand, just wait."

        "The dragon sighs at your blunt injury, he walks off nonchalantly to fetch himself an ointment and bring it to where you lie."

        e "What did you mean by 'again'?"

        my "Didn't you hit your head when you arrive?"

        e "Uhh... how did you know?"

        my "I just know."

        my "And maybe if Seb didn't jump on his feet and tell me about his new roommate that's kinda cute, according to him."

        e "...kinda c-cute?"

        my "His word, not mine."

        h "I'm Haskell, by the way."

        e "Ahhh... fuck... I'm [e]."
    else:


        show haskell normal at c1:
            linear 0.01 zoom 3
            linear 0.05 zoom 1

        h "What are you looking at?"

        e "Ahhh...!!"

        "You instinctively jumps backwards from the shock, and slam your head hard into the cabinet behind you."

        e "F-fuck!"

        e "I hit my head..."

        e "You... scared me."

        h "What... How did you hit your head again..."

        h "I've got ointment on my hand, just wait."

        "The dragon sighs at your blunt injury, he walks off nonchalantly to fetch himself an ointment and bring it to where you lie."

        e "What did you mean by 'again'?"

        h "Didn't you hit your head when you arrive?"

        e "Uhh... how did you know?"

        h "I just know."

        h "And maybe if Seb didn't jump on his feet and tell me about his new roommate that's kinda cute, according to him."

        e "...kinda c-cute?"

        h "His word, not mine."

        e "Ahhh... fuck. Haskell, didn't expect to see you here..."

    "Haskell slaps his ointment on your head, it feels cool on the wound."

    "You can feel it is healing very quickly, almost like what Ole had..."

    e "Do you know Ole?"

    h "Uh... Yes?"

    h "I saved him from his doom and I taught him about the way of herbalism."

    e "...Doom?"

    h "..."

    h "Let's talk about your feeble head, it's fine, the furs will cover it up."

    "Haskell kneels to nudge on your head several times, and stands back up to check on you."

    h "So, Are you here for the delivery?"

    e "Ahh... yes. If you didn't sneak up on me like that."

    h "How many did Ole told you to get?"

    e "30..."

    h "Yeah. That's too much for me."

    e "What do you mean?"

    h "You need to help me with something else, before I give you the potions for free."

    e "Uhh- my head still hurts. I thought you two had negotiated already."

    h "Sure, Sure. I have a lot of other clients to worry about, the goats, the bears, the-"

    e "Bears?"

    h "Yeah, they're a little bit annoying with the secrecy policy."

    h "..."

    h "Oops, it seems I just leaked their information."

    e "Haskell, are you this careless or is this intentional..."

    h "Uh... I'll just pretend I have a plan all along so you'll think I'm smart or something."

    e "O-ok."

    h "Look, have you seen the buggbears?"

    if buggbear.win + buggbear.lose > 0:

        e "Yes, I've seen them around the outpost."
    else:


        e "No... What are they?"

        h "They're some kind of monsters lurking around the outpost, walking distance from here."

    h "The goats used to be on the look out there. Until their primordial runes got stolen recently, and it drained their spellcraft reserve."

    e "R-recently?"

    h "Well, four years to be exact. That's why they started the war with the folks back."

    h "These goat folks are much weaker than they're now. Furkan is furious that they lost the outpost to the buggbears, more recently."

    e "Hmm... primordial runes?"

    h "The rock thing, that used to be on their mountain. It just generates magical energy for the goat folks, magically."

    e "Who stole it?"

    h "Me."

    e "Y-you?"

    h "No you dumbass, who do you think I am, do you think I even use magic?"

    e "I thought potion making is related to magic somehow."

    h "Yeah no."

    h "The only reason I'm making potion is for me to get enough herbs from elsewhere for my tea."

    e "Alright, so who stole the runes?"

    h "I don't know. The leader doesn't know either."

    e "Do you think it's related to me... being here?"

    h "I told you, I don't know. Best ask Furkan about that."

    h "Anyways, it's kinda causing me some troubles, with the buggbears roaming around."

    h "I can't pick up grasses and flowers like I used to now."

    e "What do you want me to do with them?"

    h "Well you probably won't want to meet them head to head."

    h "Come here, get this. I'll give you a recipe for knocking them off."

    e "So we're beating them?"

    h "Beating the buggbears off, if you will. There's too many of those huge monsters."

    h "We can't just show them the door and tell them to leave."

    e "So, what's your plan here?"

    h "See, they work by smell alone. If I can make a lotion, or ointment that makes our scent undetectable, then they won't attack us."

    e "You're proposing for us to live with the buggbears?"

    h "It's called mutualism, they get those pesky meddling goats away from me, and I leave them alone."

    e "Is that what it's called?"

    h "Yes. Alright, the plan is simple. You use my powder to knock them off, and they'll produce extra saliva for you to collect."

    h "Give them to me, it'll take me some time to make the lotion, so, after that, I'll give you the copious amount of strength potion."

    e "Can't you just get them yourself..."

    h "I'm lazy. Plus now I need a replacement lion."

    e "You mean... Seb."

    h "Of course I mean Sebas. Now I can't drink tea with him because of his supposedly 'busy' business."

    h "It's all an excuse, why wouldn't he come and talk with me."

    e "I... I'm here."

    h "You? H-ha. I'd be surprised if you don't get bashed in the head by those buggbears."

    e "I can handle them. Really."

    h "Alright, now go and prove yourself then, kiddo. Else I'll go to the village myself and kidnap them both back to my hut."

    e "O-ok. Thanks Haskell."

    $ addItem("Buggbear Sedative", inventory, 2)

    $ discoveredrecipe.append(buggbearsedativerecipe)

    $ quest08.description = _("As my courier job, Ole told me about helping him get potion from an old friend. {p} I need to sedate two Buggbears with the powder Haskell gave me.")

    $ haskell_tut = 3

    jump main_haskell_hut

label Haskell_First_Meet:

    stop music fadeout 1.0

    if haskell_tut < 3 and haskell_first_meet != 1:

        $ haskell_first_meet = 1

        hide screen menu_buttons

        "While you explore the area around the wood, you run into someone sitting on a tree trunk."

        "It doesn't seem to be someone you know, so you raise your weapon, and sneak behind the figure..."

        "As soon as you try to approach him, you step on a dry leaf, making loud cracking sound across the forest."

        show haskell normal
        with dissolve

        my "Hmmm...?"

        "A blunt voice comes out of the figure's mouth, you realise that he is a dragon."

        my "Ohh. You're not supposed to be here."

        "The figure turns around and wave at you, apparently he is holding his cup of tea..."

        e "Uhh... Who are you?"

        h "Haskell. This is my place, kiddo, go play around somewhere else."

        e "Sorry... My name is [e]. I was just looking around, I didn't mean to disturb you."

        h "The weapon you are holding seems too sharp for this little old me."

        e "I didn't know if you are dangerous or not."

        h "Sure. Sure."

        e "Hmm... You're living nearby?"

        h "No."

        h "What else do you think, you little dick head, I just told you this is my place."

        e "I am not familiar with anything around here. You don't need to be this aggressive, Haskell."

        h "Ha. Funny kid aren't you. You look new around here, where do you live?"

        e "Lusterfield?"

        h "Ohh, and what's your name again?"

        e "[e]."

        h "S-So. You are the one living with Ole?"

        e "Yeah, I just arrived here... like [timenow.day] days ago."

        e "Do you know me?"

        h "No. Are you an outsider?"

        e "Yes... Wait, are you interrogating me right now?"

        h "What else do you think I'm doing... Fucking your bubbly butt?"

        e "..."

        "Haskell takes a giant sip at his cup, while looking up to you and peeking at your reaction."

        e "No?"

        h "Ugh... boring."

        e "Hey, you are the one sitting there sipping tea and judging me for no reason at all."

        h "Sure. Sure."

        h "..."

        h "You wanna try this? I made it this morning."

        menu:
            "The dragon points at his cup, signaling you to sit down with him and relax."
            "Sit with Haskell":



                "You take your seat with Haskell, he seems to be very nonchalant with a stranger in the forest."

                "You can smell the floral aroma of the herbal tea from here, enticing you to try it out."

                e "Uhh, What's in the cup?"

                h "Poison."

                e "...What?"

                h "Calm down... It was just a joke."

                e "You have a weird sense of humour, Haskell."

                h "Look, it's chrysanthemum, with the best looking roots of angelica and rehmannia in my garden."

                e "How does it taste...?"

                h "You will know when you take a sip."

                "Haskell adjusts his posture to sit closer to you, he brings the cup to your hand and motion you to hold it."

                "He stares at you while you taste the tea, it's surprisingly sweet, with a hint of buttery warmth in your mouth, much like honey."

                h "How does it taste?"

                e "Nice? I've never drank anything like that."

                "You take a big slurp before he takes the cup from you, sipping from the cup himself."

                h "Drink slowly, or no drink at all."

                e "Sorry, Haskell, it tastes so good."

                h "You'd be surprised how many years of research it takes to create such... masterpiece of refreshment."

                e "You're good at making tea?"

                h "I'm good at making anything you can drink."

                e "That's... cool. It feels so cozy here drinking tea in the forest."

                h "Sure, kiddo. Sure."

                "You admire the scenery with Haskell by your side. He doesn't speak much, only drinking from his cup from time to time."

                "You would think it's a bad idea to share tea with a stranger, but strangely you feel much relaxed, and clear-minded."

                msg "Your HP and MP is replenished, and your lust turns to 0."

                pause 1.0

                e "..."

                e "You seem to be too laidback to be sitting here out in the dangerous forest."

                h "How would you know if I'm not prepared. If anything, it was you who sit beside me not knowing what I'm capable of."

                e "...Al-right."

                h "I should go now. Tea time is over."

                e "W-wait... You're going... already?"

                h "I've finished my drink, which means I need a refill."

                h "But don't worry kiddo, I assume we'll meet again somewhere else soon."

                $ pc.sleep()

                "You see Haskell casually walks away, and then disappears into the darkness of the forest, leaving you sitting on the tree trunk alone."

                $ haskell_tut = 2

                jump main_woodland_outpost
            "Decline":


                e "Uhh... I'm gonna pass."

                h "Your loss."

                "Haskell continues sipping his tea, looking around the forest as it is his piece of work."

                "He ignores you for the time being, eventually you just slip away from his sight and carry on with your adventure."

                jump main_woodland_outpost
    else:


        show haskell normal

        "You see the back of a dragon sitting under the shade of the forest, it's Haskell."

        e "Hey, Haskell. Nice seeing you around here."

        h "Sure, Sure."

        if quest08.status == True:

            h "Now that I hide among the buggbears, I can rest as much as I want here."
        else:


            h "The buggbears are still around the corner, we have to be cautious, somehow."

        e "Oh..."

        menu:
            h "You want a drink?"
            "Accept":



                "You sit besides Haskell and try to take the mug from him, only to see him holding onto it."

                "Haskell adjusts his posture to sit closer to you, he brings it to your palm and motion you to hold the mug."

                "He stares at you while you taste the tea, it's surprisingly sweet, with a hint of buttery warmth in your mouth, much like honey."

                pause 2.0

                msg "Your HP and MP is replenished, and your lust turns to 0."

                e "Thank you for the drink, Haskell. I think I got to go."

                h "Right. See you around."

                $ pc.sleep()

                e "See you, Haskell."

                jump main_woodland_outpost
            "Decline":


                e "Uhh... I'm gonna pass."

                h "Your loss."

                "Haskell continues sipping his tea, looking around the forest as it is his piece of work."

                "He ignores you for the time being, eventually you just slip away from his sight and carry on with your adventure."

                jump main_woodland_outpost

label Haskell_Minotaur_Dungeon:

    h "[e], you remember me telling you about how sometimes I'd receive special requests?"

    e "Yes."

    h "Well, one just came in."

    h "A special customer has requested me to mix a unique potion."

    h "However, it requires an ingredient that is exceptionally rare."

    e "What is it?"

    h "The essence of a Minotaur."

    e "A Minotaur?"

    h "Yes. A large bullman that is capable of smashing through pure stone walls with brute force alone."

    h "However, there are not many of them left."

    e "Then, how are we supposed to get its essence?"

    h "Through my channels, I've caught wind of a living Minotaur trapped inside a sandstone cave."

    h "Leave the hut and find a path through the outpost. Hurry past the dark forest and you should be able to find the dungeon."

    e "Okay. Sounds easy enough."

    "Haskell smiles indulgently at your naivete."

    h "The confidence of youth."

    "Then, his tone turns serious."

    h "Listen. A Minotaur is unlike any enemy that you face in the wilds. There is a reason why this one is trapped inside a cave."

    h "It is highly dangerous and can probably snap you in half in a twig. Plus, there are also the dangers lurking within the cave itself."

    h "According to rumors, the cave was owned by a powerful mage and the Minotaur was his captive."

    h "Beware."

    h "They say that only an adventurer with well-rounded five attributes will be able to face the Minotaur in combat."

    "Haskell sizes you up and nods."

    h "I believe you have what it takes, courier."

    e "Uhm? Me...?"

    h "Plus, unlike me, you haven't gotten tired of adventures yet."

    h "I'd rather stay here and work with my salves."

    h "Speaking of..."

    "Haskell turns to rummage in his shelves before turning back."

    h "These are health potions. They might come in handy."

    h "And I've prepared you some vials. It's for you to store the Minotaur's essence."

    e "By essence, do you mean..."

    "Haskell raises his brow."

    h "Yes, courier. Your adventure will be hard but well-rewarded."

    menu:
        h "So, will you take this on this job for me?"
        "Yes{#haskelltakeminojob}":



            $ QuestBegin(quest14)

            $ quest14.qProgress(__("Visit the Minotaur Cave in Dark Forest"))
            e "Yes."
            h "Alright... then."
            h "Take these potions."
            e "Thank you, Haskell."
            $ addItem("Small HP Potion", inventory, 3)
            $ gloomy_mountainside.discovered = True
        "Maybe Later":


            e "Maybe... later?"

            h "Huh. I'll be patiently waiting, very patiently..."

    jump Haskell_Normal_Talk

label Haskell_Sick_Quest:

    e "Haskell, Ole needs your help!"

    "Haskell rises up, more perturbed than you've ever seen him."

    h "Courier, what do you mean? What's wrong with Ole?"

    e "We don't know. Ole is currently at the shop and his body is extremely cold."

    "As you explain Ole's situation to Haskell, the latter's expression slowly relaxes and he soon reverts to his insouciant self."

    "Haskell stops you from rambling on."

    h "I think I've heard enough to reach a diagnosis."

    h "I believe our friend is suffering from an immuno-weakening disease."

    e "Immo... what?"

    h "I'm too lazy to explain it to you but what you need to know is that this is not a serious illness and it can be easily cured."

    "You sigh in relief."

    e "Can you cure Ole then?"

    h "Of course. However, I need your help."

    e "Anything you need."

    h "To brew a potion to help Ole, I need you to gather 4 pieces of gingers. It's quite easy. You should be able to dig them up in the clearing outside my hut."

    h "In the mean time, I'll go to the shop to monitor Ole's condition."

    h "I already have other herbs on my ends, so when you've gathered enough ingredients, get back to the shop."

    e "Of course!"

    $ quest15.qComp(__("Gather 4 Gingers"), "Ginger", 4)

    $ quest15.status = 3

    jump main_haskell_hut

label Haskell_Report_Minotaur_Dungeon:

    e "Haskell, I got the essence."
    "You hand the vial over to Haskell."
    "Haskell swirls the viscous liquid."
    h "It looks like you had a great time harvesting this product."
    "You scratch your head and nod shyly."
    "To change the subject, you ask."
    e "Haskell, who is your client that gave you this request anyway?"
    h "That's for me to know, and not for you to find out."
    h "But, I did do some research while you were off in the dungeon."
    h "The minotaur you fought is technically not an evil monster."
    h "It was imprisoned for it had no idea how to control its immense power."
    h "In my calculation, it's since been some time as the beast had some company in its captivity."
    h "So, I believe it is thankful that someone went to visit it, regardless of the outcome."
    e "That's... quite sad."
    h "Well, in the end, the minotaur is merely a freak of nature, an anomaly that shouldn't even be there in the first place."
    h "It might not mean harm but the beast was imprisoned for a reason."
    e "Haskell, the minotaur is still a living being."
    h "Yes, and so are the slimes. And the mimics, and everything else. For them, this is the way of life, and so does the minotaur."
    h "So don't get too attached to anyone, kiddo. It's a fool's errand, nothing more."
    e "I think, you're oversimplifying things, Haskell."
    h "Well, kiddo. I'm not here to lecture you about morality, you learnt enough from the folks back in the village already."
    h "Anyway, enough story. Now let me get on with the potion making. I have a customer to serve."
    h "Here's your reward, by the way. Use them wisely."
    e "Thank you so much, Haskell."

    msg "You received 3 Strength Potions, 3 Green Ointments, and 400 gold."
    $ addItem("Strength Potion", inventory, 3)
    $ addItem("Green Ointment", inventory, 3)
    $ pc.gold += 400
    $ removeItem("Minotaur Essence", inventory, 1)

    $ QuestFinish(quest14)

    jump main_haskell_hut

label Haskell_After_Sick_Quest:

    h "Ole's better now, yes?"

    e "Yes. Thank you for your help, Haskell."

    h "It was convenient and you did most of the work."

    h "If it involved more tasks on my part, I wouldn't have bothered."

    "That was what Haskell said but you remembered how nervous he was when you first mentioned Ole was ill."

    "However, you do not feel the need to argue with Haskell about that."

    "Everyone has their own way of showing concern."

    e "Either way, thank you Haskell."

    h "Well don't come screaming for help when this happens again."

    h "I'm not as free as Ole, going around offering help."

    h "Next time, I'll just offer you some tea and call it a day."

    $ sick_ask[1] = 1

    jump Haskell_Normal_Talk

label Haskell_Trinket_Quest:

    e "Hey, Haskell?"
    h "Yes, [e]?"
    e "I've been wondering about something for a while now, and thought you'd probably be the one that knew best."
    "Haskell takes a long draught of tea."
    h "yeeeees...?"
    e "Oh, no, it's nothing too bad."
    e "I was just wondering if you had any idea about the magic that took me here."
    "Haskell looks visibly relieved."
    h "Oh, thank God, I thought it was going to be potion related."
    h "Well, I can't really tell you much right now, as I don't really know the details, but... I might be able to figure something out if you tell me about it?"
    e "Oh. Well... my memories about it are pretty hazy?"
    "You start fidgeting nervously as you try to recall the events of that day."
    "Haskell is waiting patiently in his seat, giving you time as he pours you a cup of tea in a mug he had hidden under the table for some reason."
    e "Most of what I remember are dark shapes and feelings of loss."
    e "I remember being with my friend, and losing him."
    e "... and I remember a shaman that looked a lot like Kari."
    "Haskell takes a deep sigh, staring into his tea, stirring it as he thinks."
    h "And you say you don't recognize this area?"
    e "No. This is all new to me."
    e "Even many of the species are new to me - though some are the same."
    "Seeing that this is going to be a while, Haskell motions you to sit down across from him, in front of the absurdly large mug of fragrant tea."
    h "Hmm... what about the landscape and plants? Are those very different?"
    h "I ask because you say it's all new, but... the similarities you mention imply that wherever you came from isn't too different after all."
    "..."
    "Oh."
    e "I... don't know?"
    "Haskell looks at you oddly."
    h "What do you mean you don't know."
    "You scratch the back of your head awkwardly."
    e "I guess I never paid attention to the plants back home?"
    "You find it hard to believe that, even as the one saying it."
    h "You're telling me someone who can now identify dozens of useful plants for medicine and tailoring, who already knew how to navigate difficult landscapes just..."
    "He motions vaguely."
    h "Never paid enough attention to the world around him to know if the land itself was different from ours."
    e "I... I guess that's what I'm saying?"
    "Haskell puts his mug down, crossing his arms."
    h "Yeah, no."
    "He puts his hand up to preempt your response."
    h "I'm not saying you're lying. I don't think you are."
    h "I just think there's something else going on here."
    "That's not alarming at all."
    e "Like what?!"
    "Haskell puts a hand up to his head, rubbing it as if to try and prevent an oncoming headache."
    h "Oh, god, so many things."
    h "Great Magic, let alone something that sounds almost at the level of pact magic, tends to leave sequelae on the people and parts of the world it affects."
    "You don't want to seem stupid, but also, you have to ask."
    e "What is a sequelae?"
    h "The singular would be a sequela, but... basically, lingering after-effects. Some of which may never go away."
    h "These can range from something as mundane as the hair on your pinky disappearing for 2 weeks, to something as massive as teleporting 20 feet every hour on the dot."
    h "Luckily, you don't seem to be that bad off, though it does seem like you have a bit of amnesia at the very least."
    "This is really not how you expected this conversation to go for you."
    e "So you're saying I might be ill or something? Is there any way I can figure out what might be wrong with me?!"
    h "Well..."
    h "I could give you a medical examination?"
    e "I... I think I'd really appreciate that."
    h "Alright, sounds good to me."
    h "I'll need you to get some chrysanthemums for me before we start."
    e "That's... odd. What do you need those for?"
    "Haskell scratches his cheek."
    h "I need them for uhh... the check up."
    "You narrow your eyes at him."
    h "I need them for the check up. I'll get some stuff ready while you go do that."
    $ quest24.qProgress(__("Collect 3 Chrysanthemums"))
    $ QuestBegin(quest24)

    jump Haskell_Normal_Talk

label Haskell_Herb_Fetch_Task:
    if task06.completedtimes > 0:
        e "Hey, Haskell. Do you need anything for your tea?"
        h "Yes, I do. Come."
    else:
        e "Hey, Haskell, you seem pretty stressed. What happened?"
        "The dragon stares at you, before sipping on his tea like usual, stresslessly."
        h "Please keep going if you want to piss this old dragon off."
        e "I was just joking, Haskell. You're... doing just the same."
        h "Yes, I am. And you?"
        e "I am alright as well. I just wanted to know what happened to the minotaur in that cave."
        h "Well, like I said last time, he's been in captivity for some time."
        e "Can he be released?"
        h "No, sadly. It'd be a spell to be broken by its own caster, and it's not that I know where the magician resides, or if he's even alive anymore."
        "You nod your head. Feeling down for a moment."
        pause 1.0
        "Haskell takes notice very quickly, giving you a concerned look."
        h "Rather than occupying your mind with a hapless situation, maybe you can help me fetch some herbs for the garden."
        e "Ah...? What are those?"
        h "Plants, flowers and trees [e]. You're talking like you haven't seen one before."
        e "Oh, sure. Haskell, what are you planning to do with them?"
        h "For the tea, of course. What else were you thinking?"
        e "Uhm... Nothing?"
        h "Mmhmm, as expected."
        h "Just as a motivator, I might be able to share you some gold for the potion I sold."
        h "And perhaps recipes for potion, or clues for new trinket, if you've done enough."
        menu:
            h "What do you think?"
            "Accept the Task":
                e "Alright, I'm down. What do I need to collect?"
                h "Good."
            "Maybe Later":
                e "Maybe later? I have something important on my hand."
                h "Hmm... Sure."
                "Haskell casually takes another sip, as you take your leave silently."
                jump main_haskell_hut
    $ herbofchoicy = renpy.random.choice(["Hydrangea", "Hawthorn", "Horehound"])

    "The dragon points at the empty chair in front of you."
    h "Take a seat, kid."
    "You gently move the wooden chair closer with Haskell and sit, the dragon takes notice and grins."
    "Haskell turns around and takes out a book from the shelf, he flips over the page and soon opens it in front of you."

    if herbofchoicy in task06.selection:
        h "I need ten more of [herbofchoicy], you know where to find them, right?"
        e "Yeah, I think I know."
        h "Good, good. Then I'll be waiting for good news from you soon."
    else:
        $ task06.selection.append(herbofchoicy)
        if herbofchoicy == "Hydrangea":
            h "So, I want you to get this one for me. Hydrangea."
            "He points to a drawing of a shrub with clusters of white and bluish flowers."
            e "Where can I find this?"
            h "Near Lusterfield, the garden right next to their farm, theirs are usually blue, like this, the farmers has had messed with the soil long time ago."
            h "Just get me a few of those, 10 pieces of hydrangea will be fair, I've been craving this tea for so long."
            e "Is it any good?"
            h "Yes, of course. Hydrangea is exceptionally sweet without the bitterness. And it's been decades since I've savored its taste."
            h "It was found in places far away from here, but one of the travellers in Lusterfield found some and planted them there."
            h "So, if you help deliver me ten of these flowers, it'd be much appreciated."

        if herbofchoicy == "Hawthorn":
            h "What I want you to do, is to get me this one, Hawthorn."
            "He points to a drawing of a red berry fruit on a tree with steep thorns."
            h "I've had elderberries and all other berries you can think of, but not this."
            h "And before you ask, yes. Hawthorn is one of my favorites, it has this pleasantly tangy flavor which is a lot more pronounced when you cook it just right."
            h "Obviously, you'd need to steep them for a few hours before taking a sip. And it helps improve your health, by a huge margin."
            e "So... where can I find this Hawthorn?"
            h "Sundersilk Cascades, just close to the freshwater out there."
            h "I just want the berry, not the Mayflowers."
            h "So, if you help deliver me ten of these fruits, it'd be much appreciated."

        if herbofchoicy == "Horehound":
            h "Maybe you should get me one of these, Horehound."
            "He points at the wrinkled leaves of a plant with white flowers."
            h "Just like that eccentric wolf who calls himself Lothar."
            "Haskell chuckles to himself, while you look at him in confusion."
            h "Because he's a... ho-... forget it."
            h "Some people call it Hound's bane, repels hostile wolves in the wild, and it's fairly useful in getting rid of parasites, or treating colds and coughs."
            e "How does it taste like?"
            h "You'd recognise the similarity if you have drunk enough root beer in your youth, it has a bitter taste but with a minty undertone."
            e "And... where can I acquire it?"
            h "Hold your horses, kiddo. I still haven't explained how it works."
            "He looks at you for a moment, before putting down his mug."
            h "...if I continue talking you'd have to sleep here for the night so I'll be brief."
            h "Horehound can be found somewhere around the goat tribe, perhaps on top of that goat shop?"
            e "Gwyddyon? Aren't you selling potions to his shop?"
            h "Talking to that man is exhaustive to say the least, and to a much higher degree when you ask him anything at all."
            h "So no. I won't owe him any favor other than selling potions to his measly shop."
            h "So, if you help deliver me ten of these leaves, it'd be much appreciated."

    e "I won't disappoint you, Haskell."
    h "Mmmhm, looking forward to your return."
    $ TaskBegin(task06)
    jump main_haskell_hut

label Haskell_Herb_Fetch_Task_Inquire:
    e "Haskell, what do I need to collect again?"
    "The dragon turns to you, takes a sip of his mug while giving you a strange stare."
    h "You definitely need some tea to improve your memory."
    if herbofchoicy == "Hydrangea":
        h "Now, you should get me ten Hydrangea, from the Sundersilk Cascades."
    if herbofchoicy == "Hawthorn":
        h "Now, you should get me ten Hawthorn somewhere in the garden near the Lusterfield farm."
    if herbofchoicy == "Horehound":
        h "Now, you should get me ten Horehounds near the goat tribe, somewhere up top."
    e "Alright, thank you so much again."
    h "Mhmm..."
    jump main_haskell_hut

label Haskell_Herb_Fetch_Task_End:
    if task06.completedtimes > 0:
        e "Hello, Haskell, I've returned with your desired [herbofchoicy]."
        "You put the herbs on the table, right next to his mug."
        h "Oh, that was pretty quick."
        h "Thanks, kiddo. I'll put them to good use."
    else:
        e "Hello, Haskell, I've returned with your desired [herbofchoicy]."
        "You put the herbs on the table, right next to his mug."
        h "You're just on time, just when I needed these [herbofchoicy] the most."
        e "H-hey, Haskell, do you do nothing but cook tea?"
        h "I cook up potions too, as much as I don't want to. What's the matter?"
        e "I just feel like you have too much time on your hands, Haskell."
        h "What, you mean time for drinking tea? No, there's always more."
        e "And there's always more things to do, than... this."
        e "It mustn't have been more enjoyable than talking with others, right?"
        h "Mind you, I have a whole garden to tend to, Ole, you, and those pesky buyers already have me on edge for the whole day. So yes, those are enough fellowship for an old dragon like me."
        e "We really haven't met for long, but, are you always like this?"
        h "No, but there's one point in life where you've done everything already, and you'll slow down."
        h "And I don't hope you live for as long as I do."
        e "W-why?"
        h "Mhmm..."
        "Haskell takes a sip out of the mug, as usual. You glance at him intently, expecting some form of an intelligent conversation."
        h "It's senseless to continue this topic, spare me some time for the best tea I'll have ever made."
        e "I understand."
        h "Yeah, well. One day you will, kid."

    "Haskell says as he pulls out a pouch full of gold coins."
    h "Here's the 75 gold, as promised."
    h "And it was nice doing business with you."
    e "It was my pleasure too."
    $ pc.gold += 75
    if task06.completedtimes == 3:
        h "Oh, and, I promised you I'd let you know about some potions when you've done enough... right?"
        h "Give me your Journal."
        h "I've put where you need to find them right inside your journal."
        e "Thank you for everything, Haskell."
        h "Everything?"
        "Haskell smirks, him looking up and down on you causes you to squirm."
        e "No, I-"
        "You can see Haskell chuckling, mildly amused by your flustered looks."
        h "Well, look at you, it's just too easy to mess with you isn't it."
        h "All in all, I appreciate your company, [e]. You're one of the few people I don't mind spending time with."
        "You want to ask what that means, but you remain silent as Haskell might make fun of you again..."
        h "Well, I'll see you next time then."
        "With that, you take your leave with new recipe for the potions."
        $ discoveredrecipe.append(accuracypotionrecipe)
        $ discoveredrecipe.append(tenacitypotionrecipe)
    $ TaskFinish(task06)
    jump main_haskell_hut

label Haskell_Report_Trinket_Quest:

    "You open the door, and find Haskell drinking tea, his room barely changed from how it was when you left."
    show haskell normal with dissolve
    h "Oh, there you are, I was wondering when you'd get here."
    h "Could you do me a favor and pass me the chrysanthemums?"
    "Odd that he wants them so soon, when the check-up hasn't even begun."
    "Regardless, you pass them his way."
    h "Thank you, this'll just be a second. Promise it's worth it."
    "So saying, he tosses the chrysanthemum into a pot of boiling water he had apparently prepared while waiting for you to arrive."
    e "Haskell, are you kidding me."
    h "What? I said I needed them for the check up."
    e "How is this at all necessary for the check up?!"
    "Haskell puts a hand on your shoulder, looking into your eyes with a serious gaze."
    h "One always needs tea for a check up."
    "He has to be fucking with you."
    e "You already have-"
    "You gesture wildly around yourself, indicating the smorgasbord of tea-making materials cluttering his room, including..."
    "You pause, eyes narrowing on some dried chrysanthemums in the corner."
    e "YOU HAD SOME IN HERE ALREADY!"
    "He gives you a helpless shrug."
    h "Needed it fresh."
    "He has no shame. None. You don't know why you even bothered trying."
    "You take a deep breath, and imagine all of your frustration and desire to strangle Haskell ebbing away with your breath."
    "There. It's fine. You don't mind what he did. It was almost funny in a way - as long as you don't think too hard on how the joke was on you."
    e "Fine. You have your chrysanthemum... is everything ready otherwise?"
    "Haskell sighs, getting up and beginning to clear off the table."
    e "What are you doing?"
    h "Clearing off the table and organizing my room so that I have all of the materials I need on hand, and a place where I can examine you."
    h "I'm not going to make you lie down outside butt-naked."
    "That makes sense."
    "Wait, no, something there was a bit off."
    "Well, besides the fact that he told you he was going to be ready for when you came back with the chrysanthemums."
    e "What do you mean, naked?!"
    "Haskell responds without looking at you, continuing his cleaning as if your shock were an afterthought."
    h "Well, I need to look at your entire body to figure out what's wrong, don't I?"
    h "So, I need you naked."
    h "Speaking of, if you could take off your clothes and leave them there."
    "He points at a small drying rack with several pairs of identical robes on them."
    h "It would be much appreciated."
    "Weighing the shame of stripping in front of Haskell against the need for a proper check-up, you quickly strip and bundle up your clothes in the corner Haskell indicated."
    h "I meant hung up there, but... that's good enough I suppose."
    "Haskell worked very quickly."
    "The table previously littered with tea ingredients and mugs is now spotless."
    "Behind him you can see several crystals and herbs lined up for easy access."
    h "Please, lay down on the table."
    "Flushed from being bare-naked in front a handsome dragon, you climb up onto the desk."
    "As you do so, you hear Haskell sigh."
    h "Well, at least we know that your dick is working."
    "Momentarily confused, you look down, only to see that you are rock hard."
    e "I'm so sor-"
    "Haskell waves you down."
    h "Don't worry about it. Normally I'd be pretty interested in this sight actually, but I need to concentrate on finding out what's going on with you."
    "You gulp, and nod, fully laying down for his examination."
    h "Good, this shouldn't take too long. Would you like something to relax you through this process?"
    e "Yes, please."
    "Haskell briefly steps outside, and returns with a handful of small white flowers."
    h "Here. Dreamflower. Eating a few should help make things go quickly, but let you be conscious enough to respond properly to the checkup."
    e "Are you sure this is safe?"
    "Haskell pinches the bridge of his snout."
    h "Yes. This flower developed slight hallucinatory strength in order to drug pollinators into returning again and again to them."
    h "They are inherently designed to be pleasant and addictive to insects."
    h "For us more sentient creatures, they calm us down, and are non-addictive."
    h "Okay?"
    e "Okay."
    "You take the proffered flowers from Haskell's hand, and pop them in your mouth."
    "Within moments, you feel pleasantly sleepy, like you just woke up from a long nap."
    scene black with dissolve

    pause 1
    scene haskellhut_night with dissolve
    show haskell normal
    h "Okay. Please be patient, this may take a few hours."

    $ timenow.hour += 4
    $ timenow.passTime()
    "So saying, he began."
    scene black with dissolve

    pause 3
    "..."
    "It is difficult to say exactly what happened over the course of the examination due to a mix of the flowers, and the sheer amount of things Haskell did to check on you."
    "You distinctly remember him checking your vitals - fingers on your throat for pulse, ear on your throat for breathing..."
    "Temperature checks at various parts of the body..."
    "All of these were vaguely familiar to you, but things began to get odd when Haskell pulled out the mortar and pestle."
    "He began to crush different mixtures of the herbs behind him, and take blood samples from you."
    "You don't know exactly what he did, but he told you he was using the herbs to check for various kinds and effects of magic, which amplify in the presence of certain reagents."
    "Eventually, after going through dozens of blends, Haskell moved on to the crystals."
    "He brought each one up to various parts of your body, some of them glowing bright, and others remaining dim."
    "Each one was supposed to check for a different kind of magic, as well as measure the strength of it."
    "Some of the crystals were supposed to light up - many of the ones that lit up for you were those signifying the presence of an internal mana reservoir."
    "Some crystals however, lit up when they were very much not supposed to."
    "With each irregular result, spreading across blood results and crytals, Haskell's brows only furrowed further."
    "If it weren't for the flowers, you'd be very concerned."
    "Instead, you're mildly worried."
    "Eventually, Haskell finishes up, and tells you to sleep while he conducts further analyses with the herbs."
    "Your dreams are filled with dark cloaks and bright lights, a muddled mass of shapes and figures blending into one another."
    "Each one feels important, and yet... all elude you."

    "You wake up."
    scene haskellhut_night with dissolve
    show haskell normal
    e "Mrggh"
    h "Ah, you're awake. Good."
    e "I feel like shit."
    h "That would probably be the blood loss. Here."
    "Haskell tosses you a healing potion, which you promptly shove into your mouth."
    h "I would have fed you it earlier, but you were so out of it that I wasn't sure if you would drown or not."
    "Feeling much better, you sit up, mind sharp in the absence of the dreamflower."
    e "It's alright. I was too out of it to care much about it anyway."
    "Haskell taps his chin a few times, considering how to say what comes next."
    h "About that."
    h "I may have given you too powerful a dose."
    "Ah, that would explain why you struggled to feel emotion during that time."
    e "It's alright. Did you misjudge my body weight or something?"
    "Haskell sighs."
    h "If only it were that easy."
    h "It's more that your body is extremely susceptible to the effects of environmental magic."
    h "Think along the lines of someone with a weak liver drinking alcohol."
    "For a second there, you were almost excited."
    "Luckily, Haskell always manages to find a way to nip that in the bud."
    e "And the memory loss?"
    "Haskell takes a sip of tea, which he somehow always has around."
    h "No clue, honestly."
    h "The most I got was that it was probably magical, but I couldn't tell you if there's a pattern to the memory loss, what's been altered...."
    "He shrugs in defeat."
    h "I think the best you can do for now is pay close attention to differences in your memory and that of others'."
    e "What do you mean, nobody else was there with me."
    "Well, except your friend..."
    "He was real, right? He has to have been real."
    h "I mean to say that we don't know if you have anterograde amnesia - that your ability to make new memories may have been impaired."
    "..."
    "None of your recent memories seem foggy, but... your old ones didn't either until you were forced to remember the details."
    e "...Is there any good news?"
    "Haskell nods emphatically."
    h "Well, first things first. You are in excellent shape."
    h "While your body does show some signs of strain from the battles you've been in, it also reacts remarkably quickly to injury."
    e "Responds quickly...?"
    h "Your body patched up many of its injuries in the hour you slept."
    "Well, yeah, sleeping and health potions are the cure to most of your physical ailments."
    e "Is that not normal?"
    "Haskell scratches his cheek, seemingly flummoxed."
    h "No. Not really, [e]. People do heal while they sleep, but probably about half as fast as you do."
    h "You also reacted unusually well to the potion I gave you."
    e "Well, that's good."
    h "Yes, it is."
    h "Which brings me to my other point."
    "Haskell pours you a mug of tea, passing it your way."
    h "Your strong reaction to environmental magic is not unheard of."
    h "People like you were prized members in groups like the goat tribes."
    e "Why? This seems objectively bad if it means things like dreamflowers can do me in more easily."
    h "Given proper resources and knowledge, people like you can significantly alter their bodies at will, augmenting the inherent effects of magical items to passively cast magic on themselves and a small area around them."
    e "Haskell...?"
    "He looks at you quizzically"
    h "Yes? Did I fail to explain things clearly?"
    e "Well, yes, somewhat."
    e "My main issue is... why do you keep using the past tense?"
    "For the first time in this conversation, Haskell looks genuinely uncomfortable."
    h "You... you have to remember that this isn't something you were born with."
    h "This was a side-effect of great magic. Magic that often requires sacrifice."
    "Oh. You think you know where this is going, and you very much hope you're wrong."
    h "The king banned the creation of people like you because, well..."
    "It seems Haskell really doesn't want to have to say it either. He is visibly forcing himself to continue."
    h "A lot of people died, [e]. The recipients of the magic would often die rather than gain powers."
    h "And the magic itself was incredibly difficult to fuel, which meant..."
    e "I understand. You don't have to say it."
    "Haskell sags, relief written all over his body."
    "You are not relieved, however. Having been affected by a ritual like that yourself..."
    "What was the cost on the other side?"
    "You decide not to dwell on it, and instead distract yourself."
    e "So I can channel magic like this, you think?"
    "Haskell nods in affirmative."
    h "Yes. I have a few of the materials you might need here in the hut, but..."
    h "You have to be careful with this."
    h "Your aftereffects mean you can alter things more significantly than usual."
    e "Ah, so I need to be careful not to abuse my power or something?"
    "Haskell winces."
    h "Well, yes, that too. The main issue is that greater magic means greater sacrifice..."
    h "Outside of extremely mild catalysts like dreamflowers, most of your magic will come with some form of detrimental effect to yourself."
    e "Could it kill me, do you think?"
    "Haskell spends a moment on that thought."
    h "No, not really. Your ability to channel magic is excellent, but not to the point where significant physical manifestations will occur."
    h "Which is really for the best for everyone involved. I like you, but I wouldn't trust anyone with that sort of power."
    e "Alright, well... that sounds good to me?"
    e "You mentioned resources. What do I need?"
    "Haskell claps his hands together."
    h "Finally, the fun part."
    h "First off, you're going to need one of these."
    "He hands you an empty vial on a string. Looking closely, the glass is glowing faintly orange, and it is only large enough to fit a few small sprigs or gems."
    "As soon as you grab it, the flask turns ash grey, matching your fur."
    h "This is a flask that emulates the body of the person it is touching, meaning you don't have to carry everything in your hands like an idiot."
    h "I recommend tying it around your neck and tucking it under your shirt, but... it's honestly up to you."
    "You continue to stare down at the little vial laying in your palm."
    "It's sort of bizarre to think that this thing is supposed to alter your body, but... you've been given no reason to distrust Haskell so far."
    h "On its own, the flask won't do anything, but..."
    h "Well, here."
    "Haskell hands you a cork for the vial, so that things you put in won't fall out."
    h "The cork I usually use for this thing is made from sage's root."
    h "These two objects are pretty common for alchemists, though one of the most expensive things in their workshops."
    h "I can get a pretty good idea of the magical properties of anything I put in that flask as long as the cork is on it."
    e "I don't know if I can pay you back, but if you give me some time, I-"
    "Haskell kicks you in the leg, hard enough to sting, but not enough to hurt."
    e "Ow, what was that for!?"
    h "You've been making Ole and the others a lot happier these days."
    "Haskell takes a sip."
    h "...and I've maybe made quite a bit more money since you started up as a courier."
    "You open your mouth to speak, only to see Haskell staring daggers at you."
    "Maybe it would be a good idea not to look a gift horse in the mouth."
    e "You think it'll do the same for me?"
    h "Not quite."
    h "I think it should let you identify objects that might serve as catalysts when near your body, as well as get a general idea of their effects."
    h "Should make them a little easier to find, and cut out a lot of the experimentation you have to do. We don't want you putting magical toxic mushrooms in that vial, after all."
    e "That's amazing! Thank you Haskell!"
    "Haskell chuckles gently."
    h "Don't thank me yet. I swear, you're like a puppy, always excited and hopeful."
    h "We still don't know if it works."
    h "Here, give me a second."
    "You wait patiently as Haskell heads outside."
    "He returns shortly afterwards with more of the dreamflowers."
    e "Can I please not eat those again?"
    "Haskell shakes his head."
    h "That's the point of the vial [e]. You shouldn't have to eat them to see what they'll do to you."
    "Sure enough, when you look closely at the dreamflowers, you feel a small pulse from the vial, accompanied by a sudden urge to yawn."
    e "I see-"
    "Fuck, there comes the yawn."
    "You put a finger up to tell Haskell to wait, as you let out a deep yawn."
    "Haskell finds this absolutely hilarious."
    e "As I was saying. I see what you mean now."
    h "Yes. I think I saw how it affected you too."
    "The bastard is still laughing at you as he says this."
    "You can't actually be mad at him, but you might have to slip some dreamflowers in his tea or something sometime."
    h "Anyway. I don't have any materials that I think would actually be useful for you on hand right now, but..."
    h "I do know a few spots that might have something helpful."
    h "They're places with decently high ambient magic, as well as plants or rocks that have condensed a bit of that in themselves."
    h "In the dark forest, you can find Lindblooms, often sought after for their use as good luck charms."
    h "On the river's side are weeping willows, trees constantly covered in a thin film of water, dripping it onto the nearby soil. They are brittle, but prized for their regenerative properties."
    h "Near the lake, are devil's snares, smaller versions of another local plant - they are known for strong aphrodisiac properties."
    "That's a lot of information all at once, all of it too useful to forget."
    e "I hate to ask this of you, but... could you write that down for me? I'm not sure if I'll get to all of it otherwise."
    "Haskell shrugs, picking up a nearby quill, and gesturing for you to give him your questbook."
    h "Sure. I'll also include instructions regarding how to harvest most catalysts."
    h "The main thing to keep in mind is that only a certain amount of it will be useful."
    h "Carrying extra will only take up more of the vial, without letting you reach greater effects."
    h "The other thing is that you have to get something that carries a bit of life in it - for plants, that is a cutting, and for rocks and minerals, structural integrity."
    "It's good to know that these things follow rules, however weird and arbitrary they may be."
    e "Okay, that sounds good, but... aren't the plants going to die?"
    "Haskell sighs, mulling it over in his head for a bit."
    h "Sometimes. For the list I gave you, it should be okay, as each of these plants can live off of mana alone, meaning they can drink from your reservoir to stay topped up."
    h "Some things may give certain effects, but fade away with time."
    "He's finished writing at this point, slamming the book together, and putting the quill back in its place."
    h "I'd love to talk more on this, but I'm really quite busy, so... unless you have something urgent regarding this topic, I would rather stop now."
    e "...You do nothing but drink tea all day, Haskell."
    h "And if you don't let me get back to that, I'm going to add kicking you out of my house on your ass to my list of daily activities."
    "However much you know he wouldn't actually do that, he does seem to want this conversation to end."
    e "Okay, I'll be on my way, but..."
    h "Yes?"
    e "Thank you Haskell. I really appreciate this, it means a lot."
    "Haskell waves you off."
    h "It's no problem. Keep doing deliveries for me, and your debt will be more than repaid."

    msg "Journal Updated!"

    $ QuestFinish(quest24)


    jump Haskell_Normal_Talk

label Haskell_Oolong_Quest_Begin:
    $ haskell_dialogues["Dialogue"]["Oolong Get In"] = True
    e "Haskell, remember when you told me about that tea?"
    "He looks up from the pile of dried tea leaves, his eyebrow raised."
    h "What's it kiddo?"
    e "Uh... Oo...long?"
    h "Right, Oolong. Did I ever mention that to you? I don't remember..."
    "He scratches his head. You could have sworn a few strands of his hair fell down onto the book."
    e "You did. You said it was your favourite."
    h "Huh. My old memory is failing me then."
    "You walked to a table near a fireplace and stand beside the old dragon."
    e "And I'm pretty sure you promised we could taste it together."
    "Haskell turns his head to the side, looking at the garden outside."
    h "Well. Don't get too ahead of yourself, if I ever did tell you about that... there's still one thing you need to do."
    "He spoke with a raspy voice, deep yet not imposing."
    e "What is it?"
    "You ask as Haskell is busy pouring some notes into the parchment on the desk."
    "You lean down over him, staring into the writing with curiosity."
    h "Getting me the tea leaves, of course! You can't make the tea without the tea leaves."
    "His eyes flicker over to yours before returning back to his writing, his hand scribbling furiously across the page."
    h "It's not that far, just a bit of a walk once you head east from the taiga forest."
    "He scratches his beard, looking at you with a smile."
    h "I would go myself, but these old legs of mine are a bit stiff."
    "The dragon laughs to himself while you sigh in disbelief, the idea of collecting a few plants on a snow mountain is not something you'd expect to be doing."
    jump Haskell_Oolong_Quest_Begin_Menu

label Haskell_Oolong_Quest_Begin_Back_In:
    e "Haskell, didn't you ask about the Oolong a while back?"
    h "Oolong? Oh, right. I thought you'd already given up on that."
    jump Haskell_Oolong_Quest_Begin_Menu

label Haskell_Oolong_Quest_Begin_Menu:
    menu:
        h "So, want to help an old dragon out?"
        "Of course":
            e "Yeah. I can handle a short trek."
            h "It will be quick, trust me!"
            "He looks over to you with an innocent smile, winking with one of his large blue reptilian eyes."
            e "And... I can get going once you tell me what I need to look for."
            h "A lone plant on the peak of the snowy mountains, it is where the Oolong grows."
            e "Why is it so high up? I thought your garden is full of everything."
            "A mischievous laugh breaks onto his lips as he looks at you."
            h "Oolong is a special tea, its flavour profile is heavenly compared to any other inferior tea."
            h "The colder and thinner air up there produces a smoother and much sweeter taste in the Oolong, that is what gives its unique flavour."
            "His claw tips lightly scratched the wooden surface of his table as he continued."
            h "It is simply where the Oolong belongs. Only the lone plant that survives against the harsh weather, brews the best tea."
            "He stops for a moment to gaze into the distance."
            e "Have you ever tried planting it here?"
            "Haskell sighs, his shoulders slouching."
            h "No, never. It'll ruin the taste."
            "The old dragon shakes his head slightly and returns back to the parchment and quill."
            h "Here. Take this. This is the place you should be looking for."
            "Haskell pulls up the parchment from the table, tapping a claw on a point near the peak of a snowy mountain."
            h "You'll want a trowel to dig that beauty up. Don't pick it yourself, it's most likely you'll ruin the taste."
            if smalltrowelrecipe not in discoveredrecipe:
                e "Wait, a trowel?"
                "He hands you a small piece of paper, the recipe for a small trowel."
                h "Yes, I don't have a spare one, but you can properly craft one yourself."
                $ discoveredrecipe.append(smalltrowelrecipe)
            "He reaches down, pushing his chair back and leaning towards you. His eyes lock on your face, his expression stern, but his voice soft."
            h "Be careful with the bears' territories, kiddo. They are not friendly, however much they might lead you to believe."
            h "Once you get back, we'll have a tea tasting session. You and I. This tea is always to be shared."
            "He leans back in his chair, a satisfied smile on his face."
            e "Alright, do I get to drink much of it? Or is the rest all for you?"
            h "Hey, I didn't brew the other tea for you, it was for myself. I promise you, kiddo. You'll get to drink every drop of it."
            "You nodded slowly as you watch the older dragon turn to his room, rummaging through some cupboards while you slowly move over the book on the table."
            h "And..."
            "A heavy cloak lands on you, nearly sending you stumbling forwards."
            e "Ouch! This is heavy."
            "Your eyes roll back to the old dragon, and it takes a moment before you realise that there's an additional layer draped over you, you look down to find a thick leather hide."
            h "Take it, you are going to need it more than me."
            e "Wait, is this... yours?"
            h "Its gonna get colder when you hike up to a higher ground, especially for a thin-furred like you."
            e "Thin-furred are still better than having no fur at all, Haskell."
            h "Doesn't matter, you'll freeze up there unless you've got fur thick as a bear."
            "You nod to Haskell, who stands behind the doorway, the leather hide feeling heavy in your arms."
            "Holding it almost makes you feel like a child again."
            h "One thing... don't try to sniff it, it's been a while since I've last washed this thing, don't want you to get sick on the way."
            "The two of you stare at the other for a second, neither of you moving. You only dare to clutch at the cloak, feeling the warmth of the leather hide."
            $ addItem("Winterworn Coat", inventory)
            $ QuestBegin(quest44)
            $ quest44.qProgress(_("Trek to Snowbound Summit, near the Frosted Taiga in the snow area"))
            e "Thank you. I guess I'll be off then."
            h "Off you go, kiddo. Don't get lost up there."
            "You turn around, the cloak dragging behind you as you walk out of the hut."
            jump main_alchemists_cabin
        "Let me think about it":
            e "I'll think about it first."
            h "Alright, just come back when you're ready."
            jump main_haskell_hut

label Haskell_Oolong_Quest_Summit:

    e "Haskell, what do I need to do again?"
    h "Uh, you need to get me the Oolong leaves."
    e "Right, right. I remember now."
    h "And, to get the leaves, you need to trek up to the snowy mountain called Snowbound Summit."
    h "The Oolong plant is a lone plant that grows on the peak of the mountain."
    e "And... how do I get there?"
    h "By using your legs... what else?"
    e "I mean, I know that, but... is there a path or something?"
    h "Oh, right. Sorry, I forgot to mention that there's probably some puzzles, the old god probably put them there to keep the bears away."
    h "Just fill the holes, and you'll be fine."
    h "And, oh... remember to take the trowel with you. You don't want to ruin the plant."
    e "Well, thanks... I guess."
    jump main_haskell_hut


label Haskell_Oolong_Quest_Back:

    h "Back already? Did you find the leaves?"
    e "Of course I did. Here."
    "You hand over the Oolong leaves to Haskell, who spreads them on the table with a smile."
    h "See? It's not that hard, I told you."
    e "Yeah, but I had to fight a bunch of snowmen."
    h "Oh, those? They are just snow. You can just walk past them."
    e "If only the puzzles doesn't require dead snowmen... and some fuzzy creature on the top there."
    h "You met the caretaker? I thought you're just going to trim his head a bit and go."
    e "Wait, you knew about it all along?"
    h "Look, how else would I know about Oolong in the first place... besides, I told you to be careful."
    h "Sounds like skill issues to me."
    "You roll your eyes at him, but he just shrugs nonchalantly."
    pause 1
    h "Now, calm down, it's time for the main event."
    e "And what is that?"
    "Haskell looks at you with a grin."
    h "The tea, of course! I told you we could taste it together."
    h "Now, just you wait for a few days, the tea leaves will be ready for brewing by then."
    e "Oh, just a few days. I was worried it's going to take you years to prepare a cup of tea."
    h "Well, someone's a little impatient today. But I can't blame you, it's a once in a lifetime experience."
    e "I just wanted to have that tea with you, Haskell. I hope you aren't forgetting it the next day."
    h "Of course not. I share the same sentiment, kiddo. Don't you worry, I'm going to dry these leaves up very quickly when you leave."
    e "You better."
    h "Yeah, any time now... {size=10}when you leave.{/size}"
    e "Okay, okay. I get it. I'll leave you to your tea."
    h "And, oh... don't forget to come back in a few days. I promise you, it'll be worth it."
    $ quest44.status = 4
    $ haskell_dialogues["Oolong Finish Day"] = timenow.day + 2
    $ quest44.qComp(_("Wait for 3 days"))
    jump main_haskell_hut

label Haskell_Oolong_Quest_Waiting:

    e "Haskell, is the tea ready yet?"
    h "Not yet. They're going pretty well anyway."
    e "Uh, so... when's it done?"
    h "In a few days, I told you. The more time we waste on talking, the less time I have to prepare the tea..."
    "Despite his tired demeanor, the dragon's usual snark is not lost on you."
    e "Okay, okay, Haskell. Now would you please continue your precious work."

    jump main_haskell_hut

label Haskell_Oolong_Quest_Tea_Tasting:
    e "Haskell, is the tea ready yet?"
    h "Yes, yes. It's finally ready."
    "Haskell chuckles as he dangles some small pouches of tea leaves in front of you."
    e "Oh, thank god. I thought you were going to take forever."
    h "Just a bit more than forever judging by your giddy face."
    "You blush, and Haskell cackles as he pours the tea leaves into a small kettle, filling it with water."
    "A strong herbal scent emanates in the hut as you watch the Oolong leaves slowly unfurl in the hot water."
    if haskell_dialogues.get("Loopable Oolong", 0) == True:
        h "Now, kiddo, I know you are excited, but we have to wait a bit longer."
        e "Wait? For how long?"
        h "Just a few minutes. The tea needs to steep properly before we can drink it."
    else:
        e "What should we do now?"
        h "Just wait a little longer, kiddo. I've already boiled the water for you."
        e "Oh, right..."
        e "So, how is it different than the other tea we've tasted?"
        h "Well, first off, the Oolong is a bit more complex than the other teas, but it has a very smooth finish."
        h "The aftertaste is a bit more pronounced, but it doesn't linger for too long."
        h "It's not exactly a 'happy' tea, but it does have a certain calming effect."
        e "Ahh, that sounds nice."
    "You watch as the black dragon carefully pours the Oolong into a small cup, the steam quickly rising up in the air."
    "He fills it almost to the brim before sliding it across the table. The surface of the tea shimmers amber in the lantern light."
    h "Here you go, kiddo. One cup of Oolong tea."
    "You reach out and pick it up, smiling at the hot cup of tea made from your hard work."
    if haskell_dialogues.get("Loopable Oolong", 0) == True:
        e "Wow, it smells amazing!"
        "You say, bringing the cup closer to your nose. The aroma is rich and earthy, with a hint of sweetness."
        h "It should be. Oolong is a special tea, after all."
        h "Just remember to take it slow. Oolong is meant to be savored, not rushed."
    else:
        e "So... how do we begin?"
        "You ask, curiously observing how the water turns orange, and aromas begin wafting around the hut."
        h "First, smell the tea."
        "Haskell says, pouring himself a cup of the steaming brew. You lean closer, inhaling deeply. The scent reminds you of sandalwood mixed with something else — something uniquely Haskell."
    "It feels warm in your hands. Haskell watches you with a grin as you take a sip."

    if haskell_dialogues.get("Loopable Oolong", 0) == True:
        "You take a sip, letting the hot liquid slide down your throat, tasting it as fully as possible."
        e "Mmm... It taste just as good as last time."
    else:

        "You take a cautious sip, allowing the liquid to swirl around your mouth before swallowing."
        e "Mmm... It tastes amazing!"
        "The flavor bursts on your tongue, sweet yet bitter with underlying notes of flowers and smoke. It's different from any tea you've ever tasted before."
    "The afterglow was a subtle mineral note, the faintest whisper of a coolness of the snow, along with a lingering sweetness that warms your chest."
    e "It's... incredible."
    "You say, opening your eyes to find Haskell leaning forward, eyes alight as he grins at you."
    h "Harvesting the tea is the first step, but the main step? It's the oxidation."
    "The dragon explains, taking a sip from his own cup."
    h "Oolong is a balance — neither fully oxidized nor entirely fresh. It's the perfect in-between."
    e "I see..."
    "You murmur, reaching for another sip of the tea. It tastes even better this time around. Richer, deeper."
    e "Thank you, for sharing this with me."
    h "It's my pleasure, kiddo. Tea is meant to be shared."
    "Haskell's expression softens. He takes a measured sip, savoring the taste."
    h "Though, I may need to start charging you if you keep making such an adorable face while drinking it."
    "You blush again, ducking your head in embarrassment. But even with your face hidden behind your head of fur, you can't help but smile at Haskell."
    "The way he teases you so gently, you know he cares about you. And that's all you ever needed to know."
    if haskell_dialogues.get("Loopable Oolong", 0) == 0:
        h "You know, when I was younger, I used to be obsessed with making potions. Alchemical elixirs, magical concoctions..."
        h "I experimented with every ingredient I could find, I travelled across Mokken just to get the formula just right. And over time I quickly became everyone's alchemist."
        h "Brewing love potions, anti-venoms, life potions... But, no matter how many potions I made, none of them tasted as good or felt as wonderful as this one."
        "He points at the Oolong in your cup."
        h "This stuff is the real potion. It doesn't work like magic, or science. It works like life."
        e "Is this why you stopped making potions for everyone?"
        "Haskell looks away, his bright blue eyes seeming far off in the distance. "
        h "Because I got tired of people coming to me for miracles. They wanted everything fixed instantly. And I... I just couldn't do that anymore."
        "He looks at you, his eyes glimmering with something deeper."
        e "You were giving them something too powerful?"
        h "Maybe."
        "Haskell replies, shrugging."
        h "Or maybe I was just getting old and cranky. Either way, I stopped brewing altogether."
        e "But you still make tea."
        h "Yes. Because it's simple. It doesn't promise anything. But it delivers anyway."
        h "They are two sides of the same coin. The potion is a quick fix, the other is a slow burn."
        h "One would change you, but the other would teach you."
        h "And one gives you things that you don't have, the other would show you what you already have."
        h "You know, kiddo, sometimes people think they need miracles. They think they need some special power to change their lives for the better. But the truth is, all we really need is patience and time."
        "Haskell's breath catches. He sets down his cup and slides closer on the chair, so the wooden table no longer separates you."
        h "And to know what we truly want."
        "You look up, meeting Haskell's gaze. His eyes are half-lidded, reflecting the dancing flames of the fireplace."
        "There's a warmth in them you've never seen before. A tenderness you didn't know he was capable of showing."
        menu:
            e "Haskell-"
            "Let him finish":
                jump Haskell_Oolong_Tasting_Kiss
            "Pull away":
                $ haskell_dialogues["Oolong Tasting"] = haskell_dialogues.get("Oolong Tasting", 0) + 1
                $ haskell_dialogues["Kiss"] = False
                pass
        "You pull away, your heart racing as you try to process what just happened."
        "Haskell looks at you, his expression a mix of surprise and concern."
        h "Did I... did I go too far?"
        "He asks, worry evident in his tone."
        e "No, no. It's not that. I just... I wasn't expecting that."
        h "Ah, I see. I didn't mean to make you uncomfortable, kiddo. It's an old man thing."
        "He takes a deep breath, awkwardly trying to rearrange the table."
        e "That doesn't mean I didn't want it..."
        "You add quietly, feeling your face heat up again. You're not sure how Haskell will react to this, but you find yourself wanting to reassure him anyway."
        e "You were right about tea being a slow burn..."
        e "But sometimes, the slow burn is worth waiting for."
        "Haskell smiles at you, a genuine, warm smile that reaches his eyes. "
        h "Is that so?"
        "You nod, smiling back at him."
        e "Yes. Definitely yes."
        "The two of you share another moment of silence, the crackling of the fire and the clinking of empty cups the only sounds in the room."
        "But this time, there's no discomfort in the silence. No awkwardness or tension. Just peace and understanding between you."
        "And you realize that maybe, just maybe, you've finally found what you truly want after all."
        "Right here with an old dragon, sharing tea inside a simple hut."
        $ QuestFinish(quest44)
    else:
        "You take another sip, letting the warmth of the tea spread through your body."
        h "You know, kiddo, I think you might be the only person who truly appreciates this tea."
        "Haskell says, his voice low and soft."
        "You smile back at him, feeling warm and fuzzy all over."
        "The tea really does taste amazing — like nothing you've ever had before. It's soothing and invigorating at the same time, making you feel more alert yet deeply relaxed."
        "And the fact that Haskell made it especially for you only makes it taste even sweeter."
        e "Thanks again for the tea, Haskell. It's perfect."
        "You say, setting your cup down. Haskell nods, smiling warmly at you."
        h "Any time, kiddo. Any time."
        "The rest of the session passes peacefully as you both sit there, sipping tea and enjoying each other's company."

    scene black with dissolve
    pause .5
    scene haskellhut with dissolve

    "You spend the rest of the session with Haskell. Discussing more about alchemy, or perhaps even about life."
    "Haskell seems happy to have someone who actually wants to listen to him, not trying to take advantage of him."
    "And you're glad that he's willing to open up to you."
    "To share this side of himself. The tender, thoughtful side that he usually keeps hidden behind his cranky demeanor."
    "You leave the hut with a smile on your face, feeling lighter than you have in a long time."
    msg "Your Purity is restored by 10 points."
    $ pc.cor += 10
    if pc.cor > 100:
        $ pc.cor = 100
    $ timenow.hour += 2
    $ haskell_dialogues["Preparing Oolong"] = False
    jump main_haskell_hut

label Haskell_Ask_Oolong_After:
    $ haskell_dialogues["Loopable Oolong"] = True
    e "Haskell, how was the Oolong tasting last time?"
    h "Ah, it was quite pleasant actually. But why don't you tell me what you thought of it?"
    "You eagerly reminisce about the experience."
    e "Oh, it was absolutely amazing."
    e "The flavor was so rich and complex, I couldn't get enough of it."
    "Haskell listens attentively, nodding along as you describe every detail of the taste."
    "He seems genuinely pleased by your reaction, even though he knew exactly how you would respond."
    h "Well, well..."
    h "It looks like we have another tea enthusiast on our hands."
    "You laugh, feeling your face grow hot at the compliment."
    h "I don't mind brewing another batch of Oolong for you, if you're interested in trying it again."
    e "Really? That would be fantastic!"
    "Haskell nods with a satisfied smile."
    h "Good, well... let me know if you've got more of the leaves."
    jump main_haskell_hut

label Haskell_Ask_Loopable_Oolong:
    e "Haskell, can we do the Oolong tasting again?"
    menu:
        h "As long as you've got those Oolong for me, of course."
        "Yes, I have some" if LookForItem("Oolong Leaves", inventory):
            $ removeItem("Oolong Leaves", inventory, 1)
            $ haskell_dialogues["Loopable Oolong"] = True
            $ haskell_dialogues["Preparing Oolong"] = True
            e "Yes, I have some Oolong leaves right here."
            h "Great! I'll prepare the tea then, guess I can get it done in a day or so."
            "Haskell smiles, taking the batch of leaves from you."
            h "Mmmm... These smell amazing."
            "Haskell purrs appreciatively, sniffing the leaves hungrily."
            if haskell_dialogues.get("Licking", 0) > 0:
                e "I thought they might help loosen up that old cock of yours."
                "You tease playfully, grinning up at him impishly."
                "He snorts, laughing softly."
                h "Kiddo, I'm just old, not... infertile, I can still pump you full of little tots if you can."
                e "That I don't doubt."
                h "Why don't you come over here tomorrow and show me just how well you can taste them?"
                "He suggests, patting his thigh enticingly."
                e "With pleasure, sir!"
                "You chirp brightly, already envisioning the delicious treats that await you as you leave."
            else:
                h "You gotta show up tomorrow, I can't wait to have a taste of it."
                e "Deal."
        "No":

            e "Ah, no... but I can get some."
            "The old dragon nods slowly."
            h "Well, I'm looking forward to your return."
    jump main_haskell_hut

label Haskell_Ask_Kissing:
    e "Did you like it?"
    "You ask coyly, smirking up at him impishly."
    e "Did I do a good job?"
    h "Hmm... Not bad kiddo, not bad at all."
    "He chuckles, running a hand through your fur affectionately."
    h "You certainly know how to put an old dragon in his place."
    e "You love it though, don't you old man?"
    "You tease, patting the old dragon's head. He snorts, laughing softly before taking a sip from his mug."
    h "I suppose I do..."
    "He admits, his eyes twinkling mischievously as he looks up at you."
    h "But let's see how much you can handle next time, huh?"
    jump main_haskell_hut

label Haskell_Oolong_Tasting_Kiss:
    $ haskell_dialogues["Oolong Tasting"] = haskell_dialogues.get("Oolong Tasting", 0) + 1
    $ haskell_dialogues["Kiss"] = True
    $ haskell_dialogues["Preparing Oolong"] = False
    $ haskell_dialogues["Loopable Oolong"] = True
    if haskell_dialogues.get("Licking", 0) == 0:
        $ haskell_dialogues["Licking"] = 1
    else:
        $ haskell_dialogues["Licking"] += 1
    if haskell_dialogues.get("Licking", 0) >= 2:
        $ pc.cor += 10
        if pc.cor > 100:
            $ pc.cor = 100
        e "Haskell, is the tea ready yet?"
        h "Yes, yes. It's finally ready."
        "Haskell chuckles as he dangles some small pouches of tea leaves in front of you."
        e "Oh, thank god. I thought you were going to take forever."
        h "Just a bit more than forever judging by your giddy face."
        "You blush, and Haskell cackles as he pours the tea leaves into a small kettle, filling it with water."
        "A strong herbal scent emanates in the hut as you watch the Oolong leaves slowly unfurl in the hot water."
        e "Haskell, I love you so much for this."
        "You smile, watching him carefully tend to the brewing tea. Haskell sets down his mug and turns to you with a sly smirk."
        h "Well, well... aren't we sentimental today? If I had to hear this stuff just once more..."
        "He winks."
        h "I wouldn't mind hearing it again."
        "Haskell pours you both cups of tea, and hands one to you. You eagerly lift it to your snout, taking a deep whiff."
        "The Oolong leaves are still steaming hot, and they smell even more potent than before."
        "You take a sip, letting the hot liquid slide down your throat, tasting it as fully as possible."
        e "Mmm... This is amazing, just like the first time."
        "Your eyes flutter closed in pleasure, savoring every drop."
        h "Oh kiddo, you're going to make me blush."
        "Haskell laughs, taking a sip from his own cup. After he swallows, he looks at you with an affectionate gaze."
        h "But then again, I suppose that's all part of the fun."
        "You giggle and drink some more tea, watching Haskell contentedly. The old dragon leans back in his chair, drinking from his mug as he watches you."
        "There's something soothing about his presence — something that makes you feel safe and secure."
        "As you finish your tea, Haskell reaches over and takes the empty cup from your hands. He sets it aside before pulling you close, wrapping his thick arms around your body."
        "You rest your head against his chest, feeling his heartbeat thumping steadily against your ear. It's such a comforting sound, one that puts you at ease almost instantly."
        "I'm glad I could help satisfy your cravings."
        "Haskell murmurs into your ear, stroking your fur gently."
        "You purr happily, nestling closer to him. It feels so good to be held by someone who cares for you deeply."
        "Someone who would go through great lengths just to make you happy."
        e "Thank you, Haskell."
        "You whisper softly, looking up at him with loving eyes."
        "He smiles down at you tenderly, leaning forward to press a gentle kiss against your muzzle."
        "Your heart flutters with affection as his warm lips make contact with yours. And you return the gesture, capturing his mouth in a sweet kiss."
        "After several moments of passionate lip-locking, Haskell pulls back slightly, gazing at you with adoration in his eyes."
        h "Let's continue this tasting session elsewhere."
        "He whispers, taking your hand and leading you towards the bedroom."
        "Your tail swishes excitedly behind you as you follow the old dragon."
    else:
        "You lean forward, your heart racing as you close the distance between you and Haskell."
        "His other hand reaches out to tuck a loose strand of your fur behind your perked ear. The scent of sandalwood and dried oolong fills the hush between you."
        "He replaces your hand with his own, entwining your fingers."
        "Then, ever so slowly, he closes the gap and brushes his lips against yours — tender, exploratory, as if greeting a long-lost friend."
        "His lips press against yours, soft yet firm. He tastes like Oolong tea and fresh herbs and dragon scales and... everything else in this hut."
        "The kiss is soft, a gentle caress that sends shivers down your spine."
        "Your world blossoms in warmth. The old dragon pulls back, his eyes searching yours."
        h "You know, I never thought I'd find someone who could appreciate this tea as much as I do."
        e "And I never thought I'd find someone who could appreciate me as much as you do."
        "You both chuckle, the sound echoing in the quiet hut."
        h "You're a good learner, aren't you?"
        "Haskell asks, smirking."
        h "I think you might just be my favorite drinking partner yet."
        e "Oh? And why is that?"
        "You ask, quirking an eyebrow at him."
        "Haskell pulls you closer, leaning down to murmur in your ear."
        h "Because you'd actually take the time to learn from me. And you let me teach them to you."
        "It's the first time you've gotten so close with the old dragon, the fine lines around his eyes and mouth - it's the map of every smile, and every sorrow he's ever felt."
        "You can tell this dragon has seen some things. Been through so many battles, so many wars."
        "But all he wants now is to share his peace with you. And you want to give him everything in return."
        "It's so easy to fall into his embrace, to lose yourself in the warmth of his presence."
        "You reach up and place your hand on his cheek, feeling the rough skin beneath your palm."
        "He closes his eyes, tilting his head into the touch."
        e "Haskell."
        "You whisper, your voice trembling."
        e "I think I know what I truly want..."
        "Pulling him closer, feeling the hardness of his body pressing against your own."
        h "Me too."
        "He murmurs, pressing a gentle kiss to the corner of your muzzle."
        "His words hang in the warm air as you lean in, lips barely brushing his. You want it to last forever, to feel the black dragon's smile, and the warmth of his body against yours."
        "But you know that this is just the beginning."
        h "Want to take another sip?"
        "He whispers, as you look down at the empty cup on the table."
        e "We'll need a refil-"
        h "No, we have plenty more where that came from here, don't we?"
        "The old dragon just laughs, leaning in once more to capture your lips in a searing kiss."
        "The Oolong tea in your mouth tastes sweeter than ever, the leaves seeming to dance in harmony with the dragon's tongue, mixed together with your own saliva."
        "Your body aches for more of it, for the taste of Haskell's lips, for the warmth of his scales against your fur."
        "You pull back, panting slightly as the two of you gaze at each other in wonder."
        h "Well, well, It looks like I've created quite the monster yet again."
        e "W-what monster..."
        "You stutter, your cheeks flushing red."
        h "An addicted one, if you will."
        h "But don't worry, kiddo. I'll make sure to satisfy your cravings."
        "And with those words, the old black dragon takes you by the hand and leads you to his bedroom, a small but cozy space filled with the scent of herbs and dragon musk."
        scene black with dissolve
        h "I told you, didn't I? You'll get to drink every drop of the Oolong."
        "Haskell murmurs, his voice low and seductive."
        e "E-every... drop?"
        "You ask breathlessly, your eyes glued to the impressive sight before you. Haskell just grins, his tail swishing lazily behind him."
        h "Just you wait, kiddo. You're about to have the most delicious tasting session of your life."
    call Scene_Haskell_Blowjob from _call_Scene_Haskell_Blowjob
    $ pc.lust = 0
    "The next morning, you wake up to find yourself still nestled in Haskell's embrace. He looks down at you with soft eyes, a warm smile playing across his lips."
    h "Good morning, kiddo."
    "He murmurs, his voice rough with sleep. You stretch languidly, feeling the familiar warmth of Haskell's scales against your skin."
    e "Morning..."
    "You reply groggily, yawning widely."
    if haskell_dialogues.get("Licking", 0) != 1:
        "He laughs softly, nuzzling the top of your head affectionately."
        h "How'd you sleep?"
        "He asks gently, rubbing soothing circles along your back. You purr happily, snuggling closer to him."
        e "Like a log. It was amazing waking up to your hugs every morning."
        "You say, gazing up at him adoringly."
        "He smiles warmly, leaning down to press a soft kiss against your forehead."
        h "That's good to hear, but you gotta get used to my old scent if you want to wake up here every morning."
        "He teases gently, nudging your snout playfully. You giggle, leaning forward to capture his muzzle in a sweet kiss."
        e "I wouldn't have it any other way."
        "You whisper softly against his lips before pulling back slightly, looking up at him with bright eyes. He grins affectionately, ruffling your fur gently."
        "Alright then, I'll be seeing you, kiddo."
        "He says, rising from the bed and stretching languidly. You watch him walk away towards the door, unable to take your eyes off his majestic figure."
        "As he reaches for the doorknob, he turns back to look at you with warm eyes."
        h "Oh, and don't forget to bring some Oolong next time we have our tasting session."
        "He chuckles as he steps out of the room, closing the door behind him."
        "And as you lay there in his now-empty bed, surrounded by his comforting scent, you can't help but to take a whiff before you get going as well."
    else:
        e "Did we... did we really...?"
        "You ask, remembering last night's events. Haskell chuckles softly, rubbing his nose against yours affectionately."
        h "No, it's just a dream."
        "He says gently."
        h "A very pleasant one, though."
        "You laugh softly, feeling a blush creep onto your face."
        e "I guess that means we can do it again, right?"
        "You suggest playfully. Haskell grins down at you, his eyes twinkling with mischief."
        h "Oh [e], you have no idea how much I'd like to make this a daily thing."
        "Your heart flutters at the thought, and you snuggle closer against him, nuzzling into his chest happily."
        h "But I'll need you to help me out with the Oolong too."
        "He continues, a slightly pained expression crossing his face."
        h "Gotta find a way to get it going... you know."
        "You giggle, nipping playfully at his scales."
        e "Deal."
        "You say, leaning up to press a gentle kiss against his lips."
        "The old dragon smiles, he rolls himself out of the bed with a low rumble, and puts on his usual robe."
        h "Alright kiddo, I'm gonna go brew some tea. Make yourself at home."
        "With those words, he leaves you alone in his room, surrounded by the warmth of his scent and the remnants of last night's activities."
        "You stretch lazily, feeling sore from yesterday's exertions. Your body aches pleasantly as you remember the feeling of Haskell's shaft pulsing in your throat, shooting jets of hot seed directly into your stomach."
        "A grin spreads across your face at the memory as you head out, ready for a new day."
        $ QuestFinish(quest44)
    msg "Your Purity is restored by 10 points."
    $ timenow.day += 1
    $ timenow.hour = 7
    $ timenow.minute = renpy.random.randint(0, 59)
    $ pc.add_active_status(soremouthed)
    jump main_haskell_hut
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
