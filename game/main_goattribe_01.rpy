

label Kari_Dialogue:

    show kari masked
    with dissolve
    if kari_tut == 1 and quest11.status == True:
        $ kari_tut += 1
        e "Hey, General."
        k "Courier? Had Chief given you the approval to enter the tribe?"
        e "Yes."
        k "...so, another face I'll have to remember well."
        if not kari_accompany:
            e "Are you ok?"
            k "No, I told you to kill me right there, so I didn't have to suffer such a long week of resting."
            e "Stop... I didn't mean any harm."
            k "Whatever, I'm not arguing with you, I still have to recover somehow."
            k "Thanks for saving Furkan anyway."
        else:
            e "So, how are you doing."
            e "I remembered you had to carry Furkan back to the Tribe."
            k "Well, I'll just say he's quite heavier than maybe 20 years ago."
            e "How did it go... after saving Furkan in the cave."
            k "It's fine."
            e "I mean, did anything happened between you two?"
            k "W-what?"
            k "No?"
            e "Alright alright."
            k "But, I have to say."
            k "Thanks for helping me save Furkan."
        e "No problem."
    else:
        if renpy.random.random() > 0.5 and isNaked():
            k "What's the meaning of this, courier."
            e "Uhm..."
            k "You dare come up to me bare-skinned? How insolent."
            e "S-sorry."
            k "Now, speak your words, the sooner we end this, the better."
    jump Kari_Normal_Talk

label Kari_Normal_Talk:
    menu:
        k "Courier."
        "Pick up the delivery" if is_client("Kari"):
            $ client_name = "Kari"
            call Courier_Pickup_Dialogues from _call_Courier_Pickup_Dialogues_9
        "Deliver the goods" if is_recipient("Kari"):
            $ recipient_name = "Kari"
            call Courier_Delivery_Dialogues from _call_Courier_Delivery_Dialogues_9
        "Ask about his warriors" if quest23.status == False and quest19.status == True and quest19.completed_date + 1 < timenow.day and kari_location == "kechioeren_training_ground":
            jump Kari_Ask_Warrior_Practice
        "Ask about the aftermath of the search in the temple" if quest43.status == True and vote_result >= 0:
            jump Kari_Ask_After_Temple
        "Ask about Goat Tribe's Festival" if LookForItem("Stained Scroll", inventory):
            jump Kari_Ask_About_Festival
        "Ask why he is staring at you" if quest23.status == True and quest23.completed_date + 2 < timenow.day and kari_trusty == 0 and kari_location == "kechioeren_training_ground":
            jump Kari_Trusty
        "Join the warrior practice" if quest23.status == 2 and kari_location == "kechioeren_training_ground":
            e "Hey, Kari, I'm ready for the practice."
            jump Kari_Warrior_Practice_Start
        "Ask about the Goat Tribe":
            jump Kari_Ask_Goat_Tribe
        "Ask about his status of being a general":
            jump Kari_Ask_General
        "Ask how he is doing":
            jump Kari_Ask_How_Doing
        "That's all for now":
            jump Kari_Dialogue_End

label Kari_Ask_Goat_Tribe:
    e "So, how's the tribe going?"
    k "Good, I'm training a new troop currently."
    k "We have to reduce the number of mages. So, we're training in tradional combat right now."
    e "I see. What are you planning to do with them...?"
    k "Huh? To fight. What else do you think. We're fighting for glory, for the safety of our tribe."
    k "We are talking about none other than honour. And being the general, I will lead my fellow soldiers to whereever they need to be."
    k "You either cowardly live, or die with honour."
    e "Hmm..."
    e "You're so cute when you talk like this."
    k "W-what?"
    k "F-fuck you. I am being serious here."
    jump Kari_Normal_Talk

label Kari_Ask_Warrior_Practice:
    e "H-hey, general. How's the practices lately."
    "Kari pauses a moment, face contorting as if he were remembering a particularly unpleasant experience."
    k "I have a request to ask of you."
    e "Oh? The Great General is asking me for help?"
    "It is entertaining to watch Kari try and rub his forehead to nurse a growing headache, only to be stopped by the bone of his mask."
    k "Yes, Courier, though only because Furkan convinced me it would be a good idea."
    e "That makes sense. So, what do you want me to do?"
    k "Well, as you know, we've been running out of rune power."
    k "As such, many of our warriors have been recruited to train in non-magical combat."
    k "Results have left much to be desired."
    "This is an understatement. You see all of one goat warrior training right now, the rest petulantly sitting around."
    e "And you want me to help them train?"
    k "Yes. Specifically, I want you to spar them."
    k "I hate to say it, but being beaten so soundly by someone they've never met will likely motivate them."
    e "I thought you of all people would be okay with seeing your warriors learn lessons the hard way."
    k "Yes, but I am unhappy that you are stronger than them, courier."
    k "But after your performance in the cave, I must acknowledge your strength as a warrior."
    e "You know, it's kind of cute to hear you compliment me like that."
    k "Not a compliment."
    e "Still cute."
    "A murderous smile is creeping across Kari's face at this point."
    "You fear you may have gone a bit too far."
    k "Call me cute one more time, and we'll see how cute you think I am after you have this rod shoved 5 feet up your ass."
    "It takes great effort not to tease him for his word choice, but you have to, for your own safety."
    e "So, how do I start?"
    k "I'm going to assume you mean sparring. Well."
    $ QuestBegin(quest23)
    $ quest28.qProgress(__("Spar with Kari's warriors"))
    menu:
        k "I presume you are not ready yet. Am I not right...?"
        "I'm ready":
            e "I'm ready."
            jump Kari_Warrior_Practice_Start
        "Maybe Later":
            e "I am going to need some time to prepare..."
            k "Fair. I'll be waiting with my warriors."
            jump Kari_Normal_Talk

label Kari_Warrior_Practice_Start:
    "Kari nods, he steps away from you and turns to face the guards."
    k "ATTENTION."
    "Despite being in a wide open space, Kari's booming voice manages to echo from sheer volume alone."
    "Every goat in the camp ducks, covering their ears, before turning towards Kari and snapping to attention."
    k "TODAY, A GUEST WILL BE JOINING US FOR TRAINING, THE COURIER [e]."
    k "HE WILL BE YOUR SPARRING PARTNER. DO YOUR BEST TO BEAT HIM WITHOUT USING MAGIC."
    "Any hopeful sounds coming from the assembled goats turn to groans at the words 'without using magic'."
    e "Well, line up for the sparring, I guess."
    "A line of goats gripping spears quickly forms."
    "The first goat in that line approaches."
    $ quest23.qComp(_("Practise with the Goats"))
    $ quest23.status = 3
    $ goat_num = 2
    jump goathuntsman_battle

label Kari_Goat_Practice_Lose:
    hide screen battle_background
    hide screen battle_buttons
    hide screen battle_enemy_stat
    hide screen battle_player_stat
    scene kechioeren_training_ground
    show kari masked with dissolve
    k "I'm surprised you lost to them."
    e "Maybe they're stronger than you think?"
    k "No, you're just weaker than I thought."
    k "That or you didn't really try."
    "The assembled goats look like they've eaten a particularly sour lemon."
    gtr "Why can't you just believe that we're strong?"
    k "Because none of you have ever come close to beating me, even two on one."
    k "I am your general, not your paragon."
    k "If we want to be able to protect the tree, and find the one who stole the rune, we have to be stronger than this."
    "It's unclear if Kari is trying to convince the recruits or himself at this point."
    k "You see, our soldiers are not up to battle standard, but it seems you'd need more experience to, teach them."
    e "I guess so."
    k "..."
    k "Then, we'll see you next time, recover soon."
    e "See you, Kari."
    jump main_kechioeren_training_ground

label Kari_Goat_Practice_Win:
    hide screen battle_background
    hide screen battle_buttons
    hide screen battle_enemy_stat
    hide screen battle_player_stat
    scene kechioeren_training_ground with dissolve
    show kari masked with dissolve
    gtr "F-fuck..."
    if goatranger.lust >= 100:
        $ kari_disgust = 1
        k "..."
        "Kari is looking at the horny goat with a mix of disgust and contempt."
        "He turns his gaze to look at you, and the expression only intensifies."
        k "That is not how a warrior fights."
        e "Well, it worked, no?"
        k "Yes, but still, one should not debase themselves to win. Morality has a purpose in this world."
        k "It is like how one could earn much money stealing from their fellow man, but does not because they should not."
        e "I strongly disagree. A fight won through flirtation is much less harmful than one won through violence."
        "Kari is still disgusted, but accepts this for what it is."
        k "Regardless, you have shown a weakness we must work on."
        k "Everyone, I am disgusted by your show of animalistic lust."
        gt "As if you could do better!"
        "Kari walks over and hits the protesting goat over the head with his staff."
        k "I can and did do better. I watched the entire affair, and was completely unaffected."
        "You are pretty sure he is lying somewhat, but he certainly showed more restraint than his warriors."
        k "Work on your discipline, both in not talking back to your general, and in controlling your lust."
        k "We must be strong. Must be prepared."
        k "If we are not, we may lose more than just the rune."
        k "No matter what, we must keep the tribe safe."
    else:
        $ kari_disgust = 0
        k "Huh, thanks for breaking his spirit on his day one, Courier."
        k "I think we have a clear winner."
        "There is a collective groan at this declaration, though nobody can quite disagree."
        k "I think it's clear that you all need to work on your non-magical combat."
        gt "Why can't we just keep using magic! We still have the tree!"
        k "The tree does not supply nearly enough magic for that."
        k "Maintaining our buildings and water supply is already straining what it can produce."
        e "Is it really that bad?"
        k "Yes. That is why we need to find the rune as soon as possible, and make sure nobody disturbs the tree."
    "Just as Kari finishes his lecture, Furkan appears from the center of the tribe."
    show kari masked at l1 with move
    show furkan normal at r1 with dissolve
    f "Oh, hello there [e]! I couldn't help but overhear our general talking about the situation with the tree."
    k "We've already talked about this chieftain..."
    f "Yes, but we've never agreed on it."
    "Kari looks a bit unhappy about that, but can't quite disagree."
    k "Yes... but should we not talk about this in private, chieftain?"
    k "It involves quite confidential information."
    f "Perhaps, but I wanted to get [e]'s opinion on the matter."
    "Kari looks surprised, and a bit tired, but still nods his head in assent."
    k "Well, if it's alright with you then, I will order everyone else to clear out."
    "Furkan gives an assenting nod."
    "Kari turns to face the other goats present."
    k "Everybody, we will cover how to improve on your performance today at a later date."
    k "Please vacate the premises to allow for an impromptu meeting."
    "With a chorus of unhappy grumbles, the surrounding goats clear out, returning to their normal activities."
    e "If I can ask... why do you want my opinion?"
    k "Not to be rude or doubt you, chieftain, but I was wondering the same."
    f "Well, you saved me... I can't think of anything else that could make me trust you more."
    "Furkan's face is completely genuine and trusting as he says this."
    "He really does believe that you'll pick the right thing."
    k "I don't trust you as much as the chieftain does, but... I trust him on any decision he makes."
    e "Well, I don't really know what I'm supposed to be choosing between."
    f "Right, was getting to that."
    f "You have already heard most of Kari's thoughts, but I will let him elaborate."
    "Furkan turns to Kari, nodding his head to signal him to explain."
    k "As he said, you've heard most of it, but."
    k "I think we should keep our warriors trained and guarding the tree."
    k "Protect the last source of magic to our last breath, and through that, protect ourselves."
    "Kari emphasizes the end of this statement by tapping his staff against the ground."
    "He then turns to face Furkan, bowing slightly."
    f "You know you do not have to do that, Kari."
    "Kari gets out of his bow, as if he hadn't heard that."
    k "I just want to show the proper respect to my chieftain, and thank him for letting me express my opinion."
    "Furkan lets out a small sigh, likely too small for Kari to have noticed."
    f "Well, I respect your feelings on the matter, both regarding respect for me, and the tree."
    f "However, I believe the correct choice of action is to withdraw our troops from the tree."
    e "Wait, why?! Isn't it literally holding your village together with its magic?"
    f "Yes, it is."
    "Furkan takes a breath before continuing, as if convincing himself to keep going."
    f "But we can survive without it for a while."
    f "We will have to ration our magic, moreso than ever."
    f "I want to do this to show the village that we can be trusted, considering how close the tree is to their territory."
    f "Additionally, by retreating the troops, we can hold a tighter perimeter around the village."
    e "But nobody is attacking it, no? Why do you need to hold that perimeter?"
    f "We can better track the people of the village by doing this."
    "A pained expression crosses his face."
    f "I believe whoever stole the rune is either in or nearby the village."
    k "The thought hurts me deeply, as I know it hurts our chieftain, but..."
    k "Nobody outside of the village knew where the rune was, so, it's what would make sense."
    e "Couldn't somebody have just followed you up to where the rune was?"
    f "It is extremely unlikely, as we rarely visited."
    f "Additionally, the guardians would have reacted and attacked anyone who was not of our tribe."
    f "Considering they did it while our leader... was distracted from the caravan."
    f "It is a loathsome conclusion, but the one that makes the most sense."
    f "Regardless, those are our positions."
    "Both turn to face you."
    menu:
        f "Well [e], what do you think?"
        "Keep Guarding the tree":
            $ guard_tree = True
            e "I'd say... keep the huntsmen there?"
            k "Well..."
            k "Thank you for helping the chieftain and I reach an agreement on this."
            "You have a feeling Kari is mainly thankful that he doesn't have to leave the tree unguarded."
            f "If you believe that is for the best, [e], I will trust your decision, as much as mine and Kari's."
            k "I will continue to train our troops to be ready for any attack."
            f "Thank you for doing so."
            f "There is no one I would rather trust with our safety."
            "Furkan sighs sadly."
            f "Now there is only the question of how else we could patch up relationships with Lusterfield..."
            f "Both groups have yet to recover... the wounds cut deep, and scarred into prejudice and distrust."
            f "If we wish to have any future cooperation or mutual existence in general, it should be done."
            k "I understand chieftain. I think we should make amends as well."
            k "Hopefully, we will have ample opportunity to when we have the rune back."
            "Furkan looks slightly melancholy."
            menu:
                "Kari looks like he wishes to speak, but something is holding him back."
                "Remain Silent":
                    $ fk_silent = 1
                    f "Well, we will protect what we have for now."
                    f "Thank you again, [e]. I hope to see you again soon."
                    f "And of course, thank you as always, Kari."
                    "With that, Furkan leaves, a cloud of wistful bygones hanging over his head."
                    show furkan normal at r2 with move
                    show kari masked at c1 with move
                "Ask Kari what he has to say":

                    $ fk_silent = 0
                    e "Kari, you look like you want to say something, what is it?"
                    "Furkan's head whips back up, seemingly jolted out of his pensive haze."
                    k "Well, I didn't want to say anything, as it wasn't something I had the right to tell my chieftain."
                    f "Okay, then do not tell your chieftain."
                    f "Tell a fellow tribesman, Kari. I have not always been chieftain, nor you my general."
                    f "I value your opinion as an equal, even if we are not so."
                    k "I just wanted to say thank you for listening to me. Even if it wasn't how I thought it would go..."
                    k "...You're doing great."
                    f "I'm glad one of us thinks so."
                    f "I'll keep trying my best."
                    "And with that, both goats flash each other quick smiles, radiating a warmth you hadn't seen from them before."
                    f "I should get back to work at the tent."
                    k "I'll see you there."
                    "Furkan walks off, whatever somber mood had enveloped him seemingly gone for now."
                    show furkan normal at r2 with move
                    show kari masked at c1 with move
            k "Courier. I would not have trusted you with making this decision, but I cannot say I regret it."
            e "...you're welcome?"
            k "Fair enough."
            "Kari chuckles a bit at your clear confusion."
            k "I'm off to go find where my recruits have run off to. Picking berries or something, surely."
            "And with that, Kari struts off, leaving you alone once more."
        "Withdraw the Huntsman":
            $ guard_tree = False
            f "Thank you for your candor."
            k "I hope you have the right reasons for making the decision you have, but, I see the wisdom in the position."
            "Kari doesn't seem to be a sore loser going by his eyes. They are filled with distrust rather than frustration."
            f "If he had wanted to hurt us, he could have back when I was trapped in the cave."
            k "I understand, I just want to protect you and our tribe, chieftain."
            "Furkan looks to be on the edge of saying something, but can't quite bring himself to."
            "Looking across at Kari, you can see that he sees the same as you, but sees himself as too low rank to speak on it."
            menu:
                "Remain Silent":
                    $ fk_silent = 1
                    "Seeing Furkan will not in fact say what he wants to, Kari opens his mouth to speak."
                    k "I need to go tell the warriors of this change of plans."
                    k "I will report back to the tent when I am done."
                    "With that, Kari walks out in the direction the majority of the goat warriors went."
                    show kari masked at l2 with move
                    show furkan normal at c1 with move
                "Ask Furkan what he has to say":
                    $ fk_silent = 0
                    e "Furk, what's wrong?"
                    f "Nothing is wrong, I just..."
                    "You can see Furkan take in a deep breath, preparing to take the leap and say whatever it is he's been thinking."
                    f "Kari, I want you to know that I trust you to protect the tribe, and myself."
                    f "There is nobody I trust more than you."
                    "Kari bows low, like a knight accepting their oath."
                    k "Thank you chieftain, I appreciate your trust in my abilities as a general."
                    f "No, Kari. It is not about you as a general, though I trust that as well."
                    f "You have always supported me, since we were children, even up until now."
                    f "I trust you, and you, Kari, will always have that trust."
                    f "General of the goats or not."
                    k "I... I trust you as well, chieftain - Furkan."
                    "Kari's cheeks are a bit flushed, clearly embarrassed by saying that."
                    k "Now, to make good on that trust of yours, I will go tell the warriors about our change of plans."
                    "Swiftly exiting the scene, Kari heads in the direction most of the goat warriors disappeared to."
                    "You are left with an affectionately chuckling Furkan."
                    show kari masked at l2 with move
                    show furkan normal at c1 with move
            f "Well, [e], I appreciate what you have done for us today."
            e "I would do it anytime, Furk."
            f "I know. You are a great friend to the tribe."
            "You can't help but think Furkan looks quite cute right now."
            "His cheeks are a bit red, and he is rubbing the back of his head."
            f "...and a great friend to me."
            e "You give me too much credit, I am just a courier who does his best to help."
            f "Well, simple courier, you have my thanks."
            f "I do need to return to work now, but... I hope to see you around soon."
            f "It's always a pleasant sight."
            "You can't help but blush at the implications of that statement."
            e "Hehe... Thank you Furkan. See you soon!"
            "Furkan heads towards the hut, leaving you alone once more."
    $ QuestFinish(quest23)
    $ pc.gold += 200
    $ pc.exp += 700
    "You have received 200 gold and 700 experience."
    if pc.exp > pc.expCap and pc.level <= levelCap:
        $ pc.LevelUp()
        msg "You are now Level [pc.level]! Check your inventory to allocate your level points."
    jump main_kechioeren_training_ground

label Kari_Ask_General:
    e "How did you become the general...?"
    k "Furkan's father, Tevfik trained me to become the protector of the tribe."
    k "I used to play with Furk, hang out. while his father was the chief."
    k "Those were the days, where we both do not need to care about anything."
    e "But do you like being the general?"
    k "How can I not? I have to protect the tribe, protect Furkan."
    k "Everything is on the line now, I can't let my own desire sabotage what we've been building."
    e "You need to relax sometimes..."
    k "I am relaxing."
    k "What else to you think I'm doing."
    e "Hmmm..."
    jump Kari_Normal_Talk

label Kari_Ask_How_Doing:
    e "How are you doing, General."
    if kari_location == "kechioeren_conference":
        k "I'm talking with Furkan."
        e "I see, can I help you?"
        k "Help- w-what?"
        e "Uhm... nothing."
    elif kari_location == "kechioeren_training_ground":
        k "Training my troops."
        e "It doesn't look like they're... training."
        k "They're just rebellious, after their training we'll send them to the ancient tree anyway."
        e "Some of them really don't like using these weapons."
        k "I won't waste my energy on them, just let them sit there and think about their poor decisions."
        e "Uhm..."
        k "W-what?"
        e "N-nothing."
    jump Kari_Normal_Talk

label Kari_Dialogue_End:
    e "That's all, general, I'll see you... later?"
    k "See you... Courier."
    if kari_location == "kechioeren_conference":
        jump main_kechioeren_conference
    elif kari_location == "kechioeren_training_ground":
        jump main_kechioeren_training_ground
    jump main_kechioeren01

label Kechioeren_Enter:
    scene black
    with dissolve
    "You cautiously walk towards the direction Lothar sent you."
    scene kechioeren
    with dissolve
    "Soon, you discover the huge tribe area."
    "The tribe is lined with almost hundreds of huts, spread throughout the mountains."
    "You see two guards at the entrance of the goat tribe, standing carelessly."
    e "Ahem- Hey!! Hey!!"
    $ guard_sus = 0
    goatguard "..."
    goatguard "Who are you?"
    e "I- I- uhh... I'm lost."
    goatguard "I haven't seen you kind here, where're you from?"
    menu:
        e "Uhm I'm from."
        "Puro":
            e "I'm from Puro. Have you heard?"
            goatguard "No?"
            e "Really, I thought there's a dragon who looked like me?"
            goatguard "Look I don't know where you're from... maybe I can ask when our huntsmen come back."
            e "H-hey I just need a direction, and I'll go."
            goatguard "Alright."
            $ guard_sus += 1
        "Lusterfield{#goattribeenter1}":
            e "I'm from Lusterfield. I'm a courier. Look."
            goatguard "Ugh, fucking Lusterfolks."
            goatguard "What do you want, you can't enter the tribe, I've warned you."
            e "Alright- you don't need to. I just need a direction, and I'll go."
            goatguard "Ok, where do you want to go?"
            $ guard_sus += 2
        "The Town":
            e "I'm from the town..? I just got lost in the forest here."
            goatguard "Really? From that far away?"
            e "Yes, I just need a direction, and then I'll go."
            goatguard "Alright, sure."
    menu:
        e "Mhmm I want to go to..."
        "Lusterfield{#goattribeenter2}":
            e "Lusterfield?"
            goatguard "Really? Ehrm."
            if guard_sus == 2:
                goatguard "And you said you're from... Lusterfield."
                e "Yeah but I didn't know where I am."
            else:
                goatguard "Lusterfield- Why are you heading there?"
                e "Just for trading with the lion merchant."
        "Haskell's Hut{#goattribeenter2}":
            e "Haskell's place?"
            goatguard "It's just over there."
            e "Uhmm."
            goatguard "Just walk until you see the cabin."
            e "I don't know I need a map at least so I won't get lost again, Please?"
        "The Town":
            e "the Town?"
            if guard_sus == 0:
                goatguard "Didn't you say you lived in the town."
                e "Yes, but I don't know where I am... Please?"
            else:
                goatguard "The town? It's really far away."
                e "I don't know where it is, I just got lost in this forest."
    goatguard "Ughh... alright. I'll call the general to make you a map..."
    e "Thanks!"
    "The guard leaves you at the entrance of the goat tribe, you try to peek inside but the other guard keeps staring at you."
    "He is staring at you intensely, almost like he secretly knows about your plan."
    menu:
        "You might need to do something here."
        "Stand in place":
            "You stand solemnly in place, ignoring the piercing gaze of the guard."
            "Yet, you feel he is looking at you up and down, he goes around you and searches your bag."
            e "Hey, what are you doing."
            goatguard2 "Searching."
            if LookForItem("Raw Meat", inventory) or LookForItem("Raw Mutton", inventory):
                goatguard2 "What t-the."
                goatguard2 "It's... meat. someone elses."
                e "Oh, what? No no no, I just took it from the buggbears!"
                goatguard2 "Why would you take it... if not for eating the meat for yourself."
                goatguard2 "What kind of sick being are you."
                e "Hey I helped you defeat the buggbears that plagued your outpost over there..."
                goatguard2 "Watch your mouth stranger."
                e "Whatever."
            goatguard2 "Nothing suspicious..."
            e "Now may you get your hand off me?"
            goatguard2 "Not if you're so fluffy under there."
            "You can feel the guard's hand running up and down from the back to your stomach."
            "His fingers tracing deeper and deeper into your crotch."
            if isNaked():
                goatguard2 "Is this why you run around the forest... naked. Just for us to grope a feel."
            e "Get- off..."
            goatguard2 "Alright. I'll leave you be, but I see you showing off your body again here, I can't promise I'll let you go."
            e "Hmmm..."
            "The goat guard walks back to his guarding duty, while you patiently wait for the other guard to come back."
            "Soon the other guard comes back with another figure, he is wearing a short cowl around his shoulder, and holding a scepter with a bell on top of it."
            show kari masked
            with dissolve
            "He doesn't speak much, only staggering towards you while holding his scepter for balance."
            my "Who- is this you say?"
            if guard_sus == 2:
                goatguard "General, he's from Lusterfield."
            elif guard_sus == 1:
                goatguard "General, he said he's from Hawk-"
            else:
                goatguard "General I think he's from the town."
            e "Hmm ye-"
            gg "And why is he here?"
            goatguard "He said he got lost in the forest, and he asked me for directions, general."
            gg "Huh... Directions."
            e "Can I sa-"
            "The masked figure turns towards you and stare at your eyes intensely, you can feel the wrath behind his mask..."
            gg "You know something about Furkan don't you."
            e "Hmm? Furkan?"
            gg "Furkan. Our Chief. You know where he is, don't you."
            e "I- uhh... I don't know? I thought your chief would be in the tribe?"
            "The news surprised you for a moment, you thought Furkan would be in the Tribe, and it would be somewhat safer to see a familiar face."
            "But now he's gone, and you are not sure if there's anyone you can actually trust here."
            "Not mentioning the person in front of you seem to be suspicious towards you."
            "If you say nothing, maybe you can leave this place alive, at least."
            "But if you say you know Furkan, the general must want more information, that you don't know about."
            menu:
                "You need to say something."
                "I don't know anything":
                    e "Look, look, I don't know anything. I'm just a passerby."
                    gg "Bullshit, I know Furkan said he met a courier from Lusterfield, you seem to fit his description very nicely."
                    gg "And you say you don't know about him?"
                    gg "You must have a serious case of dementia, don't you."
                    e "Uh... I don't know, I swear."
                    gg "I gave you a chance, and now you've wasted it."
                "I knew about Furkan, but I don't know where he is":
                    e "Look, I know about him, alright."
                    e "I'm a courier from Lusterfield, and he asked me to give a letter to Rahim earlier."
                    gg "Yes, I know about that. You're lucky that you came forward yourself."
                    gg "So, why are you here if not for collecting ransom."
                    e "I don't know where he is now, I swear. Alright, I made an excuse just to see him here."
                    gg "Why do you want to see him?"
                    e "Uhh..."
                    jump Kechioeren_Enter_Artifact
                "I am sent by Lothar":
                    e "Alright you caught me."
                    e "I'm here to scout any information I can get..."
                    gg "And you dared to tell me about this?"
                    e "I don't know... alright. I don't know about anything."
                    e "Except that I'm just a courier."
                    gg "Wh-who sent you?"
                    e "Lothar, he told me to. Now can I go?"
                    gg "That monster. I'll kill him myself... once I get my magic back."
                    gg "And don't you dare try to escape now..."
                    e "I've told you everything, I don't know where Furkan is."
                    gg "I know."
            gg "Guards, seize him."
            $ goat_num = 1
            jump goat_guard_battle
        "Pretend to Faint":
            e "Ugh... I'm not feeling so good."
            goatguard2 "w-what?"
            e "I- haven't eaten for a long time."
            "You soon falls backwards on to the ground, luckily it's all grass but you can feel a concussion on your butt."
            "The guard stares at you, not knowing what to do, he then rings his bell on the chest for exactly three times before calling for help."
            goatguard2 "This guy... he fell! Anyone here to help."
            "Soon, the other guard and a masked figure runs towards your reclined form."
            goatguard "Hey w-what? What did you do to him?"
            goatguard2 "He said he didn't eat anything and then fainted, how would I even know?"
            goatguard "Did you just give him that classic dirty hand?"
            goatguard2 "I didn't! But I... planned to."
            goatguard "You moron."
            my "Hmm..."
            my "Let's bring him back to our place."
            goatguard "Wait, are you sure, general? I don't know if chief would like a stranger in our tribe."
            gg "Yes, I'm sure... Or are you willing to just let him die here?"
            if guard_sus == 2:
                goatguard "General, but he's from Lusterfield."
            elif guard_sus == 1:
                goatguard "General, he said he's from Hawk... something."
            else:
                goatguard "General I think he's from the town."
            gg "I know."
            gg "I'll have to lock him up later and make him spill out any information about Furk, if he has any."
            goatguard2 "Oh General, that's a good idea."
            "Your heart stops for a moment here, you're not supposed to be locked up in the Goat Tribe."
            "And you thought, at least Furkan would be in the Tribe."
            "Not this grouchy general with a delicate voice."
            "You are not ready to get locked up as a prisoner for no reason at all."
            gg "W-wait."
            "The general seems to notice you furrowing your brows. He stares at you for a second."
            e "OUCH! W-what are you doing."
            gg "Seeing if you are passed out."
            "You screamed as soon as the general touches somewhere near your groin."
            e "Y-you could have chosen somewhere else!"
            gg "Uh... Do I look like I care."
            "The guards turns back at you, looking all dumbfounded."
            goatguard2 "Didn't he just faint.?"
            gg "He faked it. Look at this guy, healthy as a hors-... fit like a fiddle."
            e "Uhmm..."
            gg "Who are you... answer now."
            jump Kechioeren_Enter_Artifact
label Kechioeren_Enter_Artifact:
    menu:
        "What should I tell him..."
        "Show him the Golem Hand" if LookForItem("Mossy Artifact", inventory):
            e "My Friend and I discovered a golem hand."
            e "And they suggested that we should look for Furkan because, it's symbol looks like something from yours."
            gg "Ugh... let me see."
            "The deer yanks the stone off your hand, and he shudders for a moment, like coming to a realisation somehow."
            gg "Oh."
            e "What?"
            gg "He's with the Golem."
            e "But we killed it."
            gg "The other one. We have two rune guardians."
            e "W-what happened to them?"
            gg "Our guardians went rogue after the primordial runes stopped supplying spell energy."
            gg "They were summoned by Furkan's father with the basin, which went missing as well."
            gg "And those guardians were supposed to be guarding the runes, right on top of our mountain."
            goatguard "Uhmm... general, is it wise to share information to a Lusterfolk?"
            gg "No, but we need to save our chieftain."
            gg "He's in the cave."
            e "W-what Cave?"
            gg "The one near sparkling lagoon."
            e "Are you sure?"
            gg "Yes."
            gg "But I can't leave the tribe unattended."
            "The general walks back and forth, trying to conjure up a plan to rescue his chief."
            gg "Come with me, courier. I need your help."
            "He points at you, not even waiting for your approval."
            e "Uh... are you sure?"
            gg "Yes. I'll tell you anything I know on our way."
            "You feel the general drags your hand, and turns towards the guards."
            gg "Cev and Hakki, stay here until I come back."
            goatguard2 "Yes, General."
            $ QuestBegin(quest11)
            $ quest11.qProgress(__("Visit the Damp Cave with the general"))
            jump Kari_Adventure
        "{s}Show him the Golem Hand{/s}" if not LookForItem("Mossy Artifact", inventory):
            "You do not have the Golem Hand..."
            jump Kechioeren_Enter_Artifact
        "Lie about a Truce between Lusterfield and the Goats":
            e "I...came here to talk with Furkan about potential reconciliation of Lusterfield... and the Goats."
            gg "W-what reconciliation."
            e "A Truce. Actually."
            gg "Why?"
            e "Look, Rahim rejected Furkan's idea, but we actually were pretty happy to... you know."
            e "Become friends with the Goats again."
            e "But we're scared... that you'll shoot us on sight, so I came to represent them."
            gg "You're brave to come here."
            "The general ponders for merely a second, before he glances back at you again."
            gg "But no."
            gg "Guards, seize him."
            e "W-what?"
            goatguard2 "Yes, General."
            $ goat_num = 1
            jump goat_guard_battle
        "Stay Silent":
            e "..."
            gg "W-what?"
            e "I didn't say anything."
            gg "No, you have nothing to say?"
            e "..."
            gg "Guards, seize him."
            e "Uhm..."
            goatguard2 "Yes, General."
            $ goat_num = 1
            jump goat_guard_battle

label Kari_Trusty:
    "Walking into the training camps once more, you see Kari staring at you with barely-disguised distrust."
    "The skull-masked goat's eyes looked like they were trying to pick you apart, figure out your origin, beliefs, goals..."
    "As if looking at you would confirm or deny his suspicions."
    "The first few times this happened, it was funny, but at this point, it's something between frustrating and pathetic."
    "Deciding it's high time to address this, you walk over to him."
    e "Good morning, Kari, anything seem to be the issue?"
    "The goat's eyes somehow find a way to narrow further."
    k "Why do you ask?"
    e "I couldn't help but see the way you were looking at me. I was wondering if there was something I was doing, or unaware of that I should know of."
    "A small noise of disgust comes out of Kari's nose."
    pause 1
    k "I am merely watching out for anything that may affect the tribe negatively. While you have earned your place here, we know next to nothing about you."
    k "So it is my responsibility as general of the tribe to monitor you and your actions, even if our chieftain won't."
    "He says that last part with visible remorse. It seems Furkan's treatment of you has upset him somewhat, though you probably could have guessed that already."
    e "Well, I don't know how much you'll learn about me just watching from afar like that. If you want to learn about who I am and why I do things, you only have to ask, you know."
    k "I had considered this, but what would I do if you were to lie?"
    pause 1
    "You pause to give that some thought. It's a good question, all things considered, if a bit paranoid."
    e "Well, more knowledge is better than none."
    k "Debatable."
    e "... You could also ask others to see if my story makes sense with what they've seen or heard from me previously."
    "Kari stares at you like you're an idiot."
    k "And who do you suppose I would ask?"
    e "The people of Luste-"
    pause 1
    e "Oh, I think I see your issue now.."
    k "I'm glad of that at least."
    "The note of derision in his voice is not lost on you."
    e "Look, it's not my fault the two of you aren't on good terms."
    e "At the very least you could ask Haskell -- he's on good terms with both of you."
    k "good is a relative term..."
    "The goat's unhappy muttering helps you know you're onto something."
    e "You could ask him if my story matches up, and have him ask Ole!"
    pause 1
    "At this point, Kari's exasperation is writ plain on his face. He's not even trying to mask it."
    k "Why are you trying to prove yourself so badly? You do not benefit from it at all, especially considering you already have free reign of the camp!"
    k "If anything, that's the most suspicious thing about you!"
    "Before you can stop yourself, you snap back at him."
    e "Maybe it's because I'm tired of you watching me like a werewolf does its prey! Have you ever considered that?"
    e "Or were you too busy evaluating me as a threat to remember that I'm a person."
    pause 1
    "Kari looks like he just swallowed an exceptionally big bug. It's gratifying to see his shock, and it helps take the edge off the worry you feel about your outburst's consequences."
    k "..."
    k "It is difficult to see you as a person when all you do is try and help. Anger like this helps make you feel... real, to me."
    "You fling your arms up in the air in frustration."
    e "So the least suspicious thing for me to do is be unhelpful and angry?"
    "Kari nods without hesitation."
    k "Yes."
    "It's difficult to hold back the scream of frustration welling up in your throat, as well as not strangle Kari to death right then and there, but somehow, you control yourself."
    e "Fine. Do you have any questions you'd like me to answer, now that you know I have a spine or whatever?"
    k "I can acknowledge the value of hearing what you have to say. Even if it means checking with Haskell."
    "Well, it's better than nothing."
    e "Alright, well."
    e "Considering my own frustrations with you, I believe it would be fair for me to be able to ask a few questions of you."
    "Kari opens his mouth to speak, but you hold your hand up to preempt him."
    e "If I ask a question you feel touches on matters of your tribe's safety or security, tell me, and I'll drop it entirely."
    "The goat gives you a tentative nod."
    k "I think we have a deal."
    k "I do not entirely understand why you want answers about me individually, but it if it is all I must trade for information that may help the tribe..."
    k "So be it."
    "However paranoid and frustrating he is, you can't help but admire his devotion to his people. It would be easier to admire if said devotion didn't make him an ass to deal with."
    e "Well, I want to know about you, like who put that stick up your ass, and whether you like it there."
    with vpunch
    "Kari's face flushes red. With anger or embarrassment, you can't tell."
    k "To show good faith, I'll answer that."
    k "Nobody did, and it's what's necessary for the tribe. It doesn't matter if I like it."
    e "You sure it wasn't Fur-"
    pause 1
    "You were in the middle of waggling your eyebrows teasingly when you had to duck Kari's slap."
    k "My turn to ask questions."
    "Considering the threat of violence just seen, it might be wise to let him lead for now."
    k "My first question is: Where are you from?"
    "Oh dear."
    e "I'm not entirely sure of that myself."
    k "What do you mean by that?"
    "You clear your throat, ready to go into a lengthy spiel."
    k "Just the important bits."
    "You shoot him a glare, but continue regardless."
    e "Well, I remember that I came from somewhere far away, and that I came here while looking for a friend."
    e "I cannot remember where it was, nor do I know where my friend is now, but I do know that I woke up dazed and confused just a bit away from Lusterfield."
    "Kari looks mildly skeptical, more from the outlandish nature of your story than anything else."
    k "You do realize how suspicious that sounds."
    e "Yeah. It's pretty unfortunate, but even if I wanted to lie and say I was from somewhere other than Lusterfield, I couldn't."
    e "I don't even know the name of the capital city."
    e "Plus, I almost died out there. I probably would have if not for Seb finding me and bringing me into town."
    pause 1
    "No response from Kari on that front."
    k "Well, I'll accept that answer for now."
    k "Next question-"
    e "What about mine?"
    "Your interruption earns you a glare, but Kari still answers your question."
    k "I was thinking you'd get them at the end."
    k "We also never specified that it had to be an equal number of questions on both sides."
    "He's technically right about that, but it still goes against the spirit of mutual collaboration."
    e "Fine. We'll go with those rules."
    k "I appreciate your cooperation."
    k "Now, what are your primary goals now that you're here?"
    e "Why does everybody have to ask me that?"
    e "I don't know! I'm figuring things out as I go along."
    e "First I'm trying to repay Seb and Ole for helping me, as well as the rest of Lusterfield while I'm at it."
    e "Second, and I'm going to stop numbering because I'm going to lose my train of thought, I want to find if there's a way back home."
    pause 1
    k "No other goals?"
    e "Well, yes, a few others."
    e "I want to live, find a place for myself in my time here, especially because I don't know how long my stay will be for."
    e "Try to figure out what's wrong with your magic-"
    "Up until now, the goat had been nodding along to your words, but at the mention of helping them find their magic, his eyes narrow once again."
    k "See, this is what I mean. Why do you want to help with that if it doesn't benefit you."
    e "It's ironic that you're asking me that, considering your own reasons to be general, but..."
    e "I care because it seems important, and it might be related to what brought me here."
    e "Also, and I'm sorry to say this, but your magic going out of control already almost killed me once."
    e "The golem I fought before meeting you all wasn't exactly cuddly and nonthreatening."
    "Kari's gaze flickers with guilt before returning to normal."
    k "You could have run away, or tried to notify us..."
    "He's hesitant to suggest these, as if even he realizes the issues with those ideas."
    e "Had I ran, it would have just attacked someone else later on, or even come and attacked Lusterfield, which could have reignited the war."
    e "Even then, had I come and sought your help, you would have just called me an outsider and attacked me."
    "This time, the guilt stays in Kari's eyes."
    k "We, we wouldn't have ignored you. We're suspicious of outsiders, but we'll never kill them unless they themselves use deadly force."
    k "Regarding the golem... I appreciate you stopping it. I wish you hadn't destroyed it, but I am glad you stopped it from hurting others."
    k "...Even if it meant losing one of our tribe's great protectors."
    "While he values the lives of his people most, it seems he does have an inherent appreciation for the value of life."
    e "Thank you for understanding. Helping you restore your magic would help make it a bit safer for me."
    e "That's only part of it though. Outside of altruism, I also help because I do actually stand to gain from this."
    e "The more I look, the more I think it may have something to do with my appearance in this world."
    "Kari seems satisfied with your answers. At least, for now."
    k "There are other things I wanted to ask, but it's probably best to approach this a bit at a time."
    k "I'm decently confident you aren't an immediate threat to the tribe, at least."
    k "So, I've learned enough for now, and it would be unfair to you to ask for more without giving a bit back."
    "His eyes harden once more."
    pause 1
    k "Though I hope it is clear that I only do this with the expectation that you will answer more questions should I ask them of you."
    e "Yeah, of course. Just as long as you let me ask questions too."
    k "Alright, well... It's your time to ask questions. Go ahead."
    e "Hrmm... I suppose my most pressing question is... what exactly is your relationship to Furkan?"
    "Kari responds nearly immediately."
    k "He is my chieftain."
    "This is going to be difficult, it seems, as the goat seems unwilling to elaborate on the subject."
    e "You know I mean more than that."
    "You can see Kari visibly struggling with the question."
    k "I am unsure as of now."
    k "We used to be the best of friends -- it was harder to get any closer than the two of us were."
    menu:
        "What should you ask?"
        "Did you sleep together?":
            e "Did you sleep together?"
            show kari masked:
                linear 0.05 xalign 0.45
                linear 0.05 xalign 0.55
                linear 0.05 xalign 0.5
            "You see Kari blush a furious red."
            k "Yes, we often shared the same bedroll, why?"
            "You shake your head."
            e "Again, you know that's not what I meant."

            "You're pretty sure that if it weren't impossible, Kari's face would have reddened further, burning with embarrassment as it is."
            k "I don't want to answer that."
            e "Does it touch on issues of security?"
            "Kari looks as if he just bit into a lemon."
            k "...no."
            e "Then aren't you suppose to answer?"
            show kari masked:
                linear 0.05 xalign 0.45
                linear 0.05 xalign 0.55
                linear 0.05 xalign 0.5
            "The look of anguish on Kari's face is almost funny, until you realize just how badly Kari doesn't want to answer this question."
            k "...yes."
            pause 1
            e "And would you do it again if you could?"
            "Kari's face is warping into a face of rigid fury at this point."
            k "Yes, I would. That is the last question you had available to you."
            k "I will ask you questions again when next I have some."
            pause 1
            k "Goodbye."
            "With that, Kari marches off, embarrassed and angry to have admitted his secret."
            $ kari_trusty = 2
        "Do you miss those days?":
            e "Do you ever look back on those days, and miss what you had?"
            k "..."
            "The question visibly pains Kari."
            k "Yes... yes, I do."
            "Kari holds his hand up as you try and begin to respond."
            k "But I'd never give up what I have now either."
            k "The goats need a general and chieftain, not two best friends having fun and experiencing life together."
            e "Do you not think you can do both?"
            "Kari goes silent, he's looking you in the eye, but it feels like he could look down at his feet in regret at any moment."
            k "We've yet to figure out how."
            "Kari sighs, clearly melancholy after your questions."
            k "I think we've talked enough about that for today. Do you have any other questions? Less personal ones, maybe?"
            e "Yes, actually. I've noticed that you don't actually seem to be a goat, from what I can tell? And neither is Furkan, for that matter."
            "The ram across from you seems to find humor in your question, as if it should be obvious to you."
            k "You're right in saying that neither Furkan or I are goats. I am a red deer, and he is a ram."
            k "The name 'Goat Tribe' only really came to be when we started interacting with people from Lusterfield."
            k "They noticed that the vast majority of us were goats, and so the name was born."
            e "...and you're fine with that?"
            "Kari shrugs."
            k "We've never really cared what our name is. We know who we are, and a title won't change that."
            e "..."
            k "..."
            e "I don't really have anything left to ask right now."
            k "Well, we can pick things up next time."
            "Kari turns to leave, but pauses briefly as a thought crosses his mind."
            k "It would be good for the goats to have someone like you on their side. If you are who you say you are... I don't mind that person at all."
            k "It just depends on whether or not you're trustworthy in the end."
            e "I think that's the nicest thing you've ever said to me, even with the paranoid doubt thrown in there."
            k "My job is to be a general, not to be nice."
            "He's right, but it's still somewhat frustrating. Right as you consider saying something, Kari picks up speaking once more."
            k "Not that I don't like being nice. People just have to earn it."
            e "Do you think you could try showing me what nice is to you?"
            "The deer sits there thinking for a while, until he finally finds something fitting."
            k "Today was... refreshing. It is good to get a new perspective."
            "6/10. Lacking style, but wins points for honesty at least."
            e "Well, I'll do my best to continue making a good impression."
            "You wait a couple seconds, unsure on whether or not you should give Kari advice or not. Eventually, you cave into your need to be helpful."
            e "Regarding Furkan... I think it might be good for you to try and talk to him about how you've been feeling."
            "There are a few moments where it looks like Kari is going to yell at you for making a recommendation like that, but..."
            "Instead, Kari gives you a nod."
            k "I think I just might."
            k "You're free to go. Make sure to stay out of trouble."
            "You roll your eyes."
            e "I will."
            $ kari_trusty = 1
    jump main_kechioeren_training_ground

label Kari_Adventure:
    $ damp_cave.discovered = True
    $ quest23.qComp(_("Report to Lothar"))
    $ quest10.status = 4
    scene woodlandoutpost
    show kari masked
    with dissolve
    "The General leads you to the path towards the cave, you follow his direction and walks across the forest."
    "You stare at the General, he seems so mysterious under the mask of his."
    gg "Over there."
    "You are still not used to his young voice, but the mysterious general doesn't bother to utter a word."
    "So, you decide to strike a conversation."
    e "Hey, General, Can I ask your name?"
    gg "W-what?"
    e "U-hm... your name?"
    k "Kari."
    e "That's an unusual name."
    k "Furkan's dad gave me this name."
    e "You seemed like a mage, or shaman."
    k "It's a long story. His father, Tevfik... he was a great man."
    k "And he had always wanted me to be the protector of the tribe."
    e "You two are not related?"
    k "No, but I've been with the family since I have my first memory."
    k "Now... that Furkan's brother and father's gone. I don't want to lose him too."
    e "Hey, I think Furkan will be alright."
    "Kari turns and stares at you, you feel very uneasy seeing him under the eerie mask."
    k "What about you?"
    e "Me...?"
    k "Hmm?"
    e "I uhh... come from another place. You know about that, right?"
    k "Yeah, Puro. Furkan told me that."
    e "Do you know anything about Chime?"
    k "No, but I've heard his name."
    k "Nothing I can tell you about where he's gone, but I'd still like to know what's the deal with you."
    e "..."
    e "He's my best friend, we've been together since I have any memories of existence."
    e "I've never felt a single moment we had separated, not until he just disappeared one day."
    e "That was the first time I hadn't seen him, he was always smily, cheerful. And I felt lost without him."
    e "So... I left the tribe, just to look for him. I searched around places where he used to hang out with me."
    e "But I found nothing."
    k "What happened after?"
    e "Well. I stumbled upon some masked guy, and he was speaking gibberish. All I remembered was that he cast a blue... spell."
    e "And I woke up here."
    k "What about the other folks? Do they know...?"
    e "O-other folks?"
    k "Tribesmen."
    e "I-I'm not sure. Now that I think of it, my memory has been really blurry since I woke up in this place."
    e "I can't remember anything concrete ever since, but I can still remember everything that happened right here."
    k "You are weird."
    e "Uh... thank you?"
    "You two continue to walk down the trail, sometimes the general awkwardly stares at you as you glance back."
    "He averts his gaze quickly."
    k "I suppose you understand where I'm coming from."
    e "Sorry?"
    k "Searching for my chief."
    e "Oh... you two have been best friends also, right?"
    k "Yes, I find it baffling how much similar our stories are."
    e "... At least I didn't end up becoming a general."
    "Kari stares at you, his unintentional pout causes you to laugh."
    pause 1
    k "What are you laughing at?"
    e "N-nothing."
    "His pout gets bigger."
    k "Well, Furkan can handle himself better than your Chime, also."
    e "Huh...?"
    k "He is as strong as his father. I trust he'll be safe."
    k "But your friend, I can't speak for him."
    "The general remains silent, he picks up his pace and you're falling behind of him."
    "It continues for a while until you are bored of the silence."
    "You walk a little faster to catch up with him."
    menu:
        "What do you want to talk with Kari?"
        "The monster you saw at that night":
            e "You know what you reminded me of?"
            k "W-what?"
            e "That monster, with the cape."
            k "I've told you already, I'm not wearing a cape."
            e "Alright, but you both have antlers, a scepter. and the X-shaped strap around you..."
            e "You know he brought me to this place, maybe for some sick reason, right?"
            k "Look, I told you, I don't walk in the dark trying to kidnap some savages into our tribe."
            e "Alright... I thought so..."
        "What is under his mask":
            e "So... what's under your mask?"
            k "W-what?"
            e "Can you put down your mask?"
            k "Why?"
            e "Cause... uhh... I'm curious?"
            show kari normal
            with dissolve
            "Kari takes off his mask for a second, before putting it back on."
            show kari masked
            with dissolve
            "The face behind his mask is a surprisingly young face, with a cleanly kept beard on his chin."
            e "You... look cute."
            k "Fuck you."
            e "Can you put it down one more time so I can see more clearly."
            k "I know what you're doing, [e]."
            k "And don't let me see you looking at me that way again."
            e "Al-alright..."
        "What is the relationship between him and Furkan":
            e "What's the relationship between you and the chief?"
            k "Furk? I've been with him since the day I had memory."
            k "He, he's like a brother to me."
            e "Hmm... just brother?"
            k "W-what?"
            k "Look, he's my friend and we've been through a lot."
            e "I mean... do you two...share the bed?"
            k "w-what no. Why would I want to get into bed with another man."
            k "..."
            k "w-hat?"
            e "What?"
            k "No. I wouldn't. and I shouldn't... but... n-nooo."
            "Kari continues shaking his head, muttering something under his breath."
            "You decide to let him be with his thought for a while."
    scene sparklinglagoon
    with dissolve
    show kari masked
    with dissolve
    "You and Kari reached the Lagoon, he motions you to drink from it to heal yourself."
    k "Drink?"
    if LookForItem("Wooden Bucket", inventory):
        e "Alright..."
        "You drink from the lagoon and feel instantly revitatlised."
    else:
        e "I... don't have a bucket."
        k "Alright, courier..."
        "The general takes out his woodle bottle and scoop up some water before handing it to you."
        e "Can you help me?"
        k "Why are you like this."
        if kari_battle_lose == 1:
            e "I don't know, maybe because I just lost a battle."
        k "Whatever. Open your mouth."
        "He slowly pours the water into your mouth, you can smell his sweating palm holding the bottle."
        "You stick your tongue out and lick his finger. He instantly gets startled and drops his bottle on your face."
        e "Ouch..."
        k "What touched me..."
        e "My tongue?"
        k "W-what? Why. Why would you do that."
        e "Sorry, just wanted to taste you."
        k "Fuck you."
        e "Alright. I'm sorry, can you help me, please?"
        k "No, no. take my bottle and drink it yourself."
        e "..."
        "You drink a few bottle of it and feel instantly revitalised."
    $ pc.sleep()
    "Kari waits for you to stand up and continue on your journey."
    pause 2
    "After a while, you feel like you should chat with Kari again."
    menu:
        "What do you want to talk with Kari?"
        "About the forest":
            e "This, this forest, it's pretty nice to walk, right?"
            k "No."
            e "Al-alright."
            k "I liked it but my antler often gets stuck in the branches..."
            e "W-wait, really?"
            "You chuckles a bit from his unfortune, he doesn't seem to mind, though."
            k "You're lucky that your horn isn't forked."
            e "Yeah, I feel very lucky now."
            k "..."
        "About his general status":
            e "So, how did you become a general in the tribe?"
            k "W-what?"
            k "One day Tevfik, Furkan's father just told me."
            k "Hmm... that I should protect the tribe for him when he's gone."
            e "O-oh."
            k "So, there's that."
            e "I see."
        "About his tribe":
            e "What's your tribe like?"
            k "W-what?"
            e "Do you people believe in any?"
            k "We did. The god of intelligence, Tapjoo. Like any other Tribes."
            k "We didn't have a huge belief and ritual after, Tevfik, Furkan's father is gone."
            k "Furkan is handling everything well, even without worshipping our god."
            k "I believe in him."
            e "Alright, that's... good to know."
        "Stay Silent":
            e "(I should probably stay silent for now.)"
    scene cave_interior1
    with dissolve
    show kari masked
    with dissolve
    "At last, you and Kari reach the cave. It seems almost dark, luckily Kari stands beside you."
    "He is way taller than you, not mentioning his antler sticking out of his head."
    "You try to grasp into his hand for comfort but he instantly flinches."
    k "What are you doing?"
    e "Uhmmm, sorry, I was a little scared."
    "The general holds onto your arm for a moment, his palm is very warm, it almost melts your heart with his little actions."
    k "Stay Alert, courier."
    e "I will, Kari."
    k "Call me General."
    e "Alright... General."
    $ kari_accompany = True
    jump Damp_Cave_Enter
label Furkan_First_Meet:
    stop music fadeout 1.0
    "You stroll around the forest aimlessly, there's probably nothing interesting in the area anyway. It's almost getting exhausting exploring the endless forest."
    "In the middle of your own reflection, you detect a weird bell ringing sound from afar. You look around and scratch your head, confused for not making out the source of the noise."
    "A shooting sound turns you from frustration to horror, You don't know where the sound comes from. You only know that you life is in danger if you stay in place for one more second."
    "'SWOOOOF' An arrow blasts just in front of you, hitting the tree right beside you, embedded deep within the center of the tree."
    "You are sure that you would have been instantly shot in the head if you stand 1 inch further, your body freezes from shock, not knowing what to do."
    "The bell ringing is getting louder and louder with each seconds passing, you are completely stunned looking at the arrow, unaware of the mysterious figure approaching you."
    my "Who are you. You are not from our tribe, are you?"
    "You still can't move your head away from the arrow that could have killed you, it makes you at least ignore the fact that someone is aiming their bow at you, ready to release it."
    e "Uh, Can you put your weapon down...?"
    my "I can kill you here right now. Last chance. Who are you?"
    "You turn around, and see a ram right in front of you. He is probably not joking around. You stare at his bow, panicked. He's pulling his bow further now."
    e "I- uhh... I'm [e]."
    my "Where are you from."
    e "I am from Puro, uhhh... I live in Lusterfield now."
    my "The village?"
    e "Yes..."
    "You notice the ram is slightly lowering his bow now, but still he doesn't let go, instead he asks you another question."
    my "Why are you here?"
    e "I'm out adventuring."
    my "You know about the ritual, do you not?"
    e "U-uh? Look I don't know who you are. Just let me go and you'll not see me here again."
    my "I need to talk to your chief."
    e "Uhh... who?"
    my "The Bull, Rahim. I have something to discuss with him."
    e "Alright... Can you lower your weapon now?"
    "You see the figure rest his bow, putting away his arrows. You breath a sigh of relief, at least you made it out alive."
    show furkan normal
    with dissolve
    my "I'm Furkan. Chieftain of the Goat Tribe."
    e "Hmmm... I thought you are a ram?"
    f "It's the same."
    e "Alright. Nice to meet you... I guess."
    f "Look, I need someone I can trust to deliver an important letter to Rahim. It's about our people, I think it's time for us to break the ice."
    e "Hmm... Why don't you just go to the village yourself?"
    f "I can't. That wolf asshole will hunt me down as soon as he sees me. And I don't want to unnecessarily kill anyone. It's just a letter of peace."
    e "So... it's a Truce."
    f "A reconciliation. I suppose."
    e "You can give me the letter, I'll just take it to Rahim and let you know how it goes."
    "Furkan hesitantly take out the letter from his loincloth, he ponders for a second, probably wondering whether you are to be trusted."
    "Eventually he puts away the letter, staring at you instead."
    f "How do I know I can trust you. Are you a courier?"
    if quest01.status == True:
        e "I have my courier badge here, look. I will abide by the rules of courier."
        f "Hmm... But how can I trust you?"
        e "I don't know."
        f "I see. Take the letter. Deliver to Rahim. His eyes only."
        e "Wait... Why are you suddenly trusting me now."
        f "I don't think you are lying, and I know who made the badge."
        e "Hmm... alright, I guess. I'll take it to Rahim."
        f "You know where to find me."
        e "Alright... I'll take off now... See you Furkan."
        $ addItem("Letter of Peace", inventory, 1)
        $ QuestBegin(quest06)
        $ quest06.qProgress(__("Give the letter to Rahim"))
        hide furkan
        jump main_ancient_tree
    else:
        e "I am not the courier... yet."
        f "Hmm..."
        f "Would you become a courier later or would you find someone else?"
        e "I'll be right back and I'll show you a proof of being a courier."
        f "I suppose so. You know where to find me."
        hide furkan
        jump main_ancient_tree

label Furkan_Before_Reconciliation:
    scene kechioeren_conference with dissolve
    $ kari_furk_dialogue = True
    "You walk into Furkan's hut. The general and the chieftain are discussing as usual."
    "But upon another look, it seems more clear that it wasn't just some discussion."
    show kari masked at r1 with dissolve
    k "What do you mean, Furkan. You already kno-"
    "The general pauses as he notices your presence. Both of them turn to you with a face of surprise."
    k "Mert! Come escort the courier out."
    goatguard "Yes, general."
    e "S-sorry, I'll be gone in a second."
    "You awkwardly smile as a guard flips open the curtain from behind you."
    "He grapples onto your arm, which causes you to flinch instinctively."
    show furkan normal at l1 with dissolve
    f "No, guard. Let him stay, he is trusted."
    "Kari furrows his brows under the mask, but he remains silent as Furkan gives him a side glance."
    "And without another word, the guard leaves the room almost immediately, as if he also knows the gravity of the situation."
    "You can sense an aura of uneasiness emanating within this room, an unspoken aggression between the chieftain and the general."
    f "Come, take a seat, [e]."
    e "Uhmm... You sure that's fine? We can always talk later."
    f "Yes, I am sure."
    "...And you're sure the tension raises tenfold as you sit across the table where Kari is standing, still silent."
    "In fact, the room has been nothing but silence for a few seconds before Furkan speaks."
    f "It has been a while since we last talked to Lusterfield, and we're thinking, if there is a possibility of reconciliation, a solution to the problem of both of us."
    f "Our primordial runes remains stolen, and we need a trusted ally that can help us fight this unknown entity."
    e "How would this help Lusterfield in any way?"
    f "Monsters are arriving from every corner of the world, ever since everything that happened."
    f "We should combine our force, lest when the threat finally knocks on our door, we should stand together."
    e "So, what's the threat exactly."
    f "We don't know yet. It could be anyone who's powerful enough, it could be a tribe, like the bears from the far north."
    "You glance at Kari, and he looks away."
    e "Uhm, general, what do you think?"
    k "You're not listening."
    "The general is directly addressing Furkan, who sits on the chair, stoic to a disgruntled general."
    f "I listened, and I said no, with respect."
    k "I trust your judgement, Furk. But you can't keep repeating the same mistake."
    k "The old bull has already made up his mind, nothing can change that."
    f "Why are you so certain?"
    k "Because we've already done that?"
    k "Tevfik died for this, and you're suggesting things can go back to what it really was?"
    f "Don't you bring my father into this conversation."
    f "Tevfik died for us. You are not the one to speak on his behalf, like you did not send him on his path of destruction."
    f "You were his advisor, Kari."
    k "What are you talking about?"
    k "I was not the one that left us all alone when the tribe needs help the most, he thought you were gone for good."
    k "Did you know how that destroyed him while I was watching there?"
    k "Every night, I can swear I hear him cr-"
    "Kari stops abruptly, he stares back at you again."
    f "Keep going."
    k "I don't think that's necessary."
    f "If you wanted to tear another hole in my heart, then do it now."
    k "That was not my intention."
    f "Was it not?"
    k "You know I'd never mean it like that-"
    k "I-"
    "Both of them look away from each other."
    k "I apologise for my language, a general should not speak to his chief like this."
    "He exclaims, looking at both of you."
    k "I'll excuse myself."
    "Kari walks off with uncertainty, as Furkan stares."
    "The chieftain looks down and takes a deep breath."
    f "Kari."
    "The general turns halfway towards the chieftain."
    f "I'm sorry."
    "It's hard to see emotion under his mask, but the general eventually leaves without another word."
    "Moments of silence continues as sounds of Kari's footstep fades."
    "And now, it's just you and Furkan sitting across each other."
    f "What do you think?"
    "Furkan speaks as he elicit a faint smile."
    e "I'd say, go for it. Besides, I suppose you don't accept no as an answer."
    f "Something else in your mind?"
    menu:
        "Tell Furkan to Listen to Kari":
            $ furkan_listens = True
            e "I don't really mean to talk about who's right or wrong, but maybe listen more to Kari?"
            e "-And I know you've made up your mind. You make the final decision here."
            f "Then what is the problem?"
            e "He's been there, every time you need anything, and I can see the desperation in his eyes when you went missing."
            e "It's just, maybe it goes a long way to make Kari feel appreciated in the discussion."
            e "Either as your general, or... your friend."
            f "Do not worry, courier. I am not angry at him."
        "Support Furkan's Decision":

            $ furkan_listens = False
            e "Nothing else, I think you're on the right path here."
            e "Kari did suggest some troubles you might face, but I trust you'll prevail."
            f "It seems a courier has more faith in my leadership than my general."
            e "I just think that, Lusterfield's not looking for another war, so there's really nothing worse that can happen."
            f "Hah, you are hilarious, [e]."
            f "Either way, do not worry about Kari, I am not angry at him."
            "Furkan speaks as he looks at the shifting curtains, but it was just wind."
    f "We are caught between a rock and a hard place here, and as protectors of the tribe, we cannot let personal emotions get in the way of what is best for the tribe."
    f "I am sure Kari will soon come to understand."
    "You nod."
    f "You should go now, do not let me bother you any further."
    e "I-it's ok."
    f "Guard!"
    "The chieftain shouts, as a guard at the door arrives."
    f "Please escort [e] outside. Make sure he is pampered and well."
    goatguard "Yes, chief."
    f "Thank you, Hakki."
    goatguard "It's Mer-"
    "The guard stops midway through his sentence, before nervously leading you outside."
    "Furkan smiles awkwardly towards both of you."
    "As you turn your head before the curtain closes, you notice Furkan rushing quickly towards the back of the hut."
    "It seems fairly obvious Furkan is using you to make Kari nervous, despite how uncomfortable it makes both of you feel."
    "But it's still surprising that he dismissed you this fast."
    "Maybe there's pent-up emotion after arguing about the former chief, underneath the smile he's putting up."
    "Or maybe he's brewing up another actual plan, you don't know what it is."
    "You can only hope it's better for everyone involved."
    jump main_kechioeren_conference

label Furkan_Second_Meet:
    show furkan normal
    with dissolve
    f "We met again."
    "You found furkan sitting on a giant wooden log, he is chewing on some meat, with bones scattering on the ground."
    if quest01.status == True and quest06.status == False:
        e "I brought you my badge, I'm the courier of Lusterfield now."
        f "Hmm... But how can I trust you?"
        e "I don't know."
        f "I see."
        f "Take the letter. Deliver to Rahim. His eyes only."
        e "Wait... Why are you suddenly trusting me now."
        f "I don't think you are lying, and I know who made the badge."
        e "Hmm... alright, I guess. I'll take it to Rahim."
        f "You know where to find me."
        e "Alright... I'll take off now. See you Furkan."
        $ addItem("Letter of Peace", inventory, 1)
        $ QuestBegin(quest06)
        $ quest06.qProgress(__("Give the letter to Rahim"))
        jump main_ancient_tree
    if quest01.status != True and quest06.status == False:
        e "Hey... I was just walking around. I am not the courier... yet."
        f "Hmm..."
        f "Would you become a courier later or would you find someone else?"
        e "I'll be right back and I'll show you a proof of being a courier."
        f "I suppose so. You know where to find me."
        jump main_ancient_tree
    if quest01.status == True and quest06.status == 3:
        $ removeItem("Letter of Peace", inventory, 1)
        e "Hey... Furkan. I've delivered the letter."
        f "What did they say?"
        e "Uh... Rahim, he said... Duly Noted."
        f "What does that mean? [e]?"
        e "I don't think he wanted to reconcile..."
        f "Really?"
        "You notice a sign of frustration in Furkan's voice."
        f "The battle had been ages, 4 years already, and the old bull still does not think it is enough."
        f "It was not just his daughter. Did he not remember my father was lost to the war?"
        "The goat chief walks around aimlessly, continuing to whine under his breath."
        f "What was I thinking-"
        f "I should not have tried. Not to have let him embarrass me like that."
        "He looks down for a few seconds, before turning to you, expecting a response."
        e "I think Rahim just wanted everything to stay as it is now."
        f "Of course he does."
        "Furkan scoffs at you, and prepares to take off."
        e "Now that I helped you... can we talk about Ch-"
        f "I will return to my Tribe now. No reason to stay. Everything else stays the same."
        e "W-wait..."
        e "You won't start a war over this... right?"
        f "No. Forget we ever have any such conversation. Do not come back, my people will not spare a courier."
        "You stand on the grass, looking at the back of the ram as he walks away in disgruntled sigh. You probably won't see him here again."
        $ QuestFinish(quest06)
        hide furkan
        jump main_ancient_tree
    e "Hey... Furkan. We met again."
    f "So, have you delivered the letter?"
    e "Not yet... But I wanted to talk about oth-"
    f "We shall stay civil, we would talk when you deliver the letter."
    e "Hmm... Alright, thanks, Furkan."
    hide furkan
    jump main_ancient_tree

label Furkan_Ask_After_Temple:
    e "Furkan, I'm sorry about what happened at the temple."
    f "I blame the cultists, not you, [e]. Never had I thought the cult were still alive and well. I thought they were mere myth."
    e "What were those myths about? It's the first time I've heard of them."
    f "They spoke of dark rituals, of sacrifices made to ancient gods, and of power that could bend the mind amongst our people."
    f "As you may have guessed, those ancient gods, or the primordials, have forsaken the mortals long ago."
    f "They left behind only traces of their power, and even that eroded with time."
    f "We have heard that some time ago, our tribe had stopped worshipping Tapjoo, our old god."
    f "However, some of the elders, they still cling onto the old ways, believing that Tapjoo will return one day."
    f "These goats formed a secret coterie dedicated to the forest god, and they stole part of the power of the runes for themselves."
    f "When the chieftain at the time found out, they were banished, and we never heard of them since."
    e "I see... so they are the ones who stole the runes?"
    f "Yes, but what were these cultish goats planning to do with the runes?"
    e "Furkan, you said your head was dizzy earlier... Do you think it was because of the runes?"
    f "It is possible. The runes hold a lot of power, and they are capable of affecting the mind in ways we cannot comprehend."
    f "I am not certain of the cultists' plan, but I am sure it was no benevolent intent."
    jump Furkan_Normal_Talk

label Kari_Ask_After_Temple:
    e "Kari... do you know anything about the cultists?"
    k "All I know is you took our chief into some temple and risked his life for it."
    e "I... I didn't mean to put him in danger. We didn't know there were others in the temple."
    k "Fuck you, [e]. Furkan is our chief... what if something happened to him. We can't-..."
    k "This is a huge mistake, the alliance and all. If not for you meddling the water, this wouldn't have all happened."
    e "I'm sorry, Kari. I truly am."
    k "You are not. You say this but you keep doing it over and over again. You'd always run headfirst into danger, then expect everyone to bail you out."
    k "You've never changed, even after being the chief it didn't stave you off being a reckless kid, you just stopped asking for forgiveness."
    e "I... being the chief?"
    "Kari's eyes suddenly widens as he turns to you."
    k "No, I misspoke."
    k "What else were you going to say?"
    jump Kari_Normal_Talk

label Furkan_Ask_About_Festival:
    e "Furkan, what's the festival that your tribe celebrates?"
    f "The festival? It has not been held for years... how do you know about it?"
    e "Uh... I've heard from a goat."
    f "I see. Well, we celebrate the festival of flowing water here, it's a tradition that has been passed down since the beginning of our tribe."
    f "It is held every year, on the first full moon of spring. The chief will grant everyone in our tribe a blessing for the year to come."
    f "There would be merchants and visitors coming from far and wide, stalls lined around the tribe, and we would have a feast to celebrate the occasion."
    f "We had stopped holding the festival lately. The flowing water had become scarce ever since the primordial runes were stolen..."
    e "Hmm, I'd like to see it one day."
    f "If the water flows once more, I would be happy to show you."
    "Furkan smiles."
    jump Furkan_Normal_Talk

label Kari_Ask_About_Festival:
    e "Hey, Kari. I've heard about some festival here... Do you know anything about it?"
    k "What? Where did you stick your nosy snout into this time?"
    e "Uh... Somewhere?"
    k "Hmph... whatever, I don't care who you couriers listen to. What else do you want to know?"
    e "Maybe how was the festival like for you?"
    k "It was... fine, I guess. I don't like the crowds, so I usually stood by the ceremony sometimes."
    k "Hmm... I guess I did miss the cabbage rolls and stuff, that was nice."
    e "Cabbage rolls?"
    k "Yeah? Do I have to explain to you what a cabbage is as well?"
    e "N-no, I just-"
    k "It's a vegetable, [e]. You wrap some cheese and rice in it. Is it that hard to understand?"
    k "Sorry, I didn't mean to snap. The rolls were good."
    e "It's okay. I guess at least I learnt something new about you."
    k "Yeah, well. Don't get used to it."
    jump Kari_Normal_Talk
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
