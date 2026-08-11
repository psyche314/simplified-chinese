screen place_ardent_cauldron():
    zorder 10 tag place

    imagebutton:
        xalign 0.325
        yalign 0.37
        idle "gwyddyon_idle"
        hover "gwyddyon_hover"
        action Return("Gwyddyon")
    imagebutton:
        xalign 0.80
        yalign 0.76
        idle "bedroom_arrow"
        hover "bedroom_arrow_hover"
        style "footstep_button"
        action Return("To Kechioeren01")

    imagebutton:
        xalign 1.004
        yalign 0.575
        idle "cauldron_idle"
        hover "cauldron_hover"
        action Return("Cauldron")

    imagebutton:
        xalign 0.145
        yalign 0.273
        idle "ardent_cauldron_basin"
        hover "ardent_cauldron_basin_hover"
        action Return("Basin")

    imagebutton:
        xalign 0.5365
        yalign 0.2506
        idle "ardent_cauldron_wanted"
        hover "ardent_cauldron_wanted_hover"
        action Return("Wanted")

    imagebutton:
        xalign 0.763
        yalign 0.05
        idle "ardent_cauldron_crawler"
        hover "ardent_cauldron_crawler_hover"
        action Return("Crawler")


label main_ardent_cauldron:
    $ current_location = "ardent_cauldron"
    $ renpy.music.play(mCauldron, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ timenow.minute += 12
    $ timenow.passTime()
    if gwyddyon_tut == 1:
        $ gwyddyon_tut += 1
        jump Gwyddyon_First_Meet
    call kechioeren_schedule from _call_kechioeren_schedule_4
    scene ardent_cauldron

    with dissolve
    show screen menu_buttons
    window hide

    call screen place_ardent_cauldron
    if _return == "Basin":
        show gwyddyon normal with dissolve
        "A poster of the progress of mossy rocks coming to life after pouring the flowing water from a special basin."
        "It seems to be what created the moss guardians in the past. But the graph explicitly says that a long growth cycle is needed to raise a guardians, which includes an extensive amount of flowing water."
        e "Gwyd, is what the poster behind you true?"
        g "Ah yes, so this is why you were staring at me for so long, wanderer."
        g "You can say, the guardians comes from water dripped from some stones, onto some stones, and moss grows on the stones, which gives life to these, stones."
        g "And these stones, guarded the magical stone which gives it sustenance in return, until said stone was stolen, and the guardians just went for the closest source of the flowing water."
        g "Now, imagine the general consulted me when they went searching for the chief."
        e "That doesn't sound, logical?"
        g "Nothing in a magical world is logical, wanderer, though I suppose you aren't one familiar."
        g "These are one of the more fascinating creatures of Mokken, the other ones are the mimics, which are just pesky fellows pretending to hide precious gems and crystals."
        e "It sounds like you got into some troubles with the mimics."
        g "Who doesn't. But, if you're one experienced adventurer, wanderer. You just have to slip away when it tries to strangle hold you with its tongue."
        g "Afterall, it's just pure inconvenience when you get trapped inside."
    if _return == "Wanted":
        show gwyddyon normal with dissolve
        "A magical diagram of a rather ambiguous face, with descriptions on the bottom of the poster, you wonder if it has anything to do with the runes."
        e "Gwyd, what's this? Can you translate it for me?"
        g "Ah, that's just the wanted poster for the thief who stole the primordial runes."
        g "It was such a long time ago, the chief had already gave up on the chase, but I didn't bother to take it down, let's just say the thief's still out there somewhere."
    if _return == "Crawler":
        show gwyddyon normal with dissolve
        "A crawler plant that's been growing in the shop, it's a rare sight to see one thriving on top of the shelves."
        "You've seen these plants before, they're usually found in the dark forest, and they're known to grow everywhere, even in the most unlikely places."
    if _return == "Gwyddyon":
        jump Gwyddyon_Dialogue
    if _return == "To Kechioeren01":
        jump main_kechioeren01
    if _return == "Cauldron":
        $ selected_recipe = None
        jump Cauldron_Screen
    jump main_ardent_cauldron

label Gwyddyon_First_Meet:
    scene black with dissolve
    pause 1
    scene ardent_cauldron with dissolve
    "You stumble inside the magical structure, it is much bigger than what you saw from outside."
    "And just like everywhere in the Goat Tribe, the cottage is brimming with sparkling blue light."
    "At the counter, you see a dark sheep, staring at what you think is a mana crystal."
    show gwyddyon normal with dissolve
    my "Welcome to the Ardent Cauldron. Blissful as the name suggests, do not get close with our cauldron, lest you fear for a self-immolation."
    pause 0.5
    "The shopkeeper does not look at you for one moment, instead he continues inspecting the crystal with his monocle. Completely unaware of your presence."
    "Ignored, you try to look around the place, the shop is filled with shelves, but most of them are already empty."
    "However, it was overall kept clean and elegant. You doubt there was ever a trace of dust ever landed on the shelf."
    "You see the aforementioned Cauldron on the right side of the shop, fueled by blue crystals, but it doesn't seem running very well."
    pause 1
    "For a while you stand there, checking out the blue marks on the surface of the empty shelves, up until the shopkeeper glances back at you."
    "He returns to look at the crystal soon after, until he raises his eyebrows again. The sheep repeats this actions for a few times before breaking the silence."
    pause 0.5
    my "Why are you still here?"
    "The shopkeeper sounds impatient, he's not exactly rude, instead, he's the opposite of rude. But the way he speaks makes you feel like you've offended him personally."
    pause 1
    my "Wait, who are you?"
    "You are as confused as he is, especially when he raises his glass to examine you from over the counter like the crystal on his hand."
    e "I'm [e], nice to meet you."
    my "Oh?"
    my "The famous [e] from Lusterfield who saved the chieftain that other day? Needless to say, didn't expect you to look like a goat, horns jutting out like the others."
    e "Well, dragons can have horns too."
    g "Ahem, the name's Gwyddyon. And in case you don't know, I own this place."
    g "There's only one rule here - no discussion about where you came from."
    e "You sound like you know something..."
    g "Second rule, no discussion about that missing friend of yours."
    e "You have seen him?"
    "Gwyddyon raises his eyebrows again."
    g "What did I say about the rules again?"
    g "Now, any other topics you would like to discuss?"
    menu:
        "Why did you ask the reason I am still here?":
            e "Why did you ask me why I'm still here?"
            g "Like I said, you looked just like any goats that wander around here."
            g "But then, you just stood there, staring at me for a while, and I thought you were just another idiot who got lost and wandered into my shop."
        "What caused you to be this petty":
            e "Hmmm... What caused you to be this petty?"
            g "Third rule, no disrespec-"
            e "Alright, alright. I get it."
    e "So what now, I just wait until you decide I'm worth talking to?"
    g "More or less. If you want my rules to bend, you'll need patience."
    g "As a wise man once said, A watched cauldron never b-"
    e "Boils?"
    "Gwyddyon squints at you with repulsion."
    g "Who taught you that, Haskell? That old dragon done stealing my sayings."
    e "I didn't even know you two knew each other."
    g "It doesn't matter. Crystals are far superior than potions, that's all you need to know."
    e "Wait, you don't sell potions here?"
    g "I have potions, but I tell you, even if his potions look better than mine, crystal is still the best choice."
    g "Look at this."
    "Gwyddyon holds the blue crystal over to you, it glistens directly above your eyes."
    g "This little fella here stores such much potentials in there. Just putting it on gives you a huge boost in magical performance."
    g "Think for a second, if you use his potions, by the time you finish a bottle, you'd already been stabbed thousands of times."
    "The sheep bluffs, pulling the crystal from your view."
    e "You're right, but I suppose the mana they provide can't last in the battle... right?"
    "Gwyddyon shakes his head."
    g "That's where you're wrong, these things regenerate mana by themselves over time."
    g "I know you can see what those goats don't understand, even if the primordial runes are gone, they still have these magnificent crystals."
    g "I tell you, they're as good as flowing water, albeit scarce, but that's the price you need to pay."
    e "How much do they cost?"
    g "Necklace made from one of them costs 1750 gold. It's not that expensive considering how much goats like magic."
    "Needless to say, the price is not anything you've seen before. Even back at The King's Pawn, the price's only at most a few hundreds."
    e "A-alright. Thanks for letting me know, Gwyddyon."
    g "You're most likely welcome. In any case, guess I'll have to see you another time."
    "You decide to probe Gwyddyon again."
    e "If you ever learn anything about Chime, will you let me know?"
    g "Again? Who's he to you anyway?"
    e "He's my best friend, just back in our tribe. I suppose you already kno-"
    g "No, I don't know anything about him. I've heard his name a few times, but I'm sure they were talking about bells."
    e "W-wait. Are you sure...? How can you be so sure?"
    g "A rather easy explanation would be that you're chasing answers no one here can give, if I may."
    "You exhale deeply. It sounds like he's just done with your topic."
    g "Alright that's it. Like I said, no discussion regarding your missing friend. We ought to stop here and you move on."
    "The sheep retires to lean back, looking at his crystal."
    g "Settle in this world, wanderer. There's something in this world you'd be better off not knowing."
    "The word sends your body full of shivers, he definitely knows something about you. But he refuses to elaborate."
    "And thinking about what happened back then, with every day gone by, you feel your memory in the home world is fading bit by bit, you're not sure how long you can cling onto these memories..."
    "Regardless, you could live the rest of your life here, but these fond memories with Chime compels you to find out the truth of what exactly happened."
    "You politely nods, and let Gwyddyon return to his task."
    jump main_ardent_cauldron
label Gwyddyon_Dialogue:
    show gwyddyon normal with dissolve
    g "Welcome to The Ardent Cauldron. Take a look around, crystals, weapons, wares. All for sale at a fair prices."
    "Gwyddyon raises his head to take a good glance at you."
    g "If it's not the famous [e]."
    jump Gwyddyon_Normal_Talk

label Gwyddyon_Normal_Talk:
    menu:
        g "We have everything you'd ever need right here, Wanderer."
        "Check out the shop":
            jump Gwyddyon_Shopping
        "Ask about his rocks" if taskAvailable(task05, quest23):
            jump Gwyddyon_Mining_Task
        "Pick up the delivery" if is_client("Gwyddyon"):
            $ client_name = "Gwyddyon"
            call Courier_Pickup_Dialogues from _call_Courier_Pickup_Dialogues_10
        "Deliver the goods" if is_recipient("Gwyddyon"):
            $ recipient_name = "Gwyddyon"
            call Courier_Delivery_Dialogues from _call_Courier_Delivery_Dialogues_10
        "Inquire about the mining task" if task05.status == 2 and LookForItemNumber(mineralofchoicy, inventory) < 10:
            jump Gwyddyon_Mining_Task_Inquire
        "Report about the mining task" if task05.status == 2 and LookForItemNumber(mineralofchoicy, inventory) >= 10:
            jump Gwyddyon_Mining_Task_End
        "Inquire about his business for Ole" if quest39.status == 2:
            jump Gwyddyon_Voting_Trade
        "Ask about the history of his shop":
            jump Gwyddyon_Ask_Cauldron_History
        "Ask about the business":
            jump Gwyddyon_Ask_Business
        "Ask how he's doing":
            jump Gwyddyon_Ask_How_Doing
        "That's all for now":
            e "That's all I need to know, thank you Gwyddyon."
            g "And until next time, Wanderer."
            jump main_ardent_cauldron

label Gwyddyon_Ask_Business:

    e "Gwyddyon, what is the business like now?"
    g "It's acceptable. We no longer have a strong inventory of imports, but the goats still keeps a few crystals in their house."
    g "What Furkan did, didn't help the shop as well. And I doubt it helps the tribe."
    e "What do you think about trading with Lusterfield?"
    g "Ah, that's why you're here. Advocating sales for your Lusterfolks?"
    g "Well I don't mind. As long as the wolf is permanently removed from this realm."
    e "By removed from this realm, you mean...?"
    g "Mostly my shop, and if I have to trade with the Lusterfolks I can't have him step foot in there too."
    "Gwyddyon almost says this nonchalantly, if not with a sprinkle of fury."
    "But still, it was his most emotional side you've seen so far."
    e "That's another weird rule."
    g "You can always, not strike a trade deal with me."
    g "And it's not like your people over there are fond of magic. Most of the trade might result in a loss considering the transportation."
    e "A-alright."
    g "However, those two... other dimwits weren't exactly hard to deal with, I can consider the trade if they ever contact me."
    jump Gwyddyon_Normal_Talk
label Gwyddyon_Ask_How_Doing:
    e "What are you doing... Gwyddyon?"
    g "Inspecting Crystals, obviously."
    e "When are you not inspecting crystals...?"
    g "When you're gone."
    e "Ouch... that hurts."
    "You says sarcastically, trying to get a reaction out of Gwyddyon."
    g "Good."
    "The shopkeeper never take a gander at you, he just continues with his crystal. Leaving you alone."
    jump Gwyddyon_Normal_Talk

label Gwyddyon_Ask_Cauldron_History:
    e "So, when did you open the shop?"
    if gwyddyon_tut == 2:
        g "Oh, getting too ambitious now. Aren't we?"
        g "Well, I can't share my precious knowledge without getting a few bucks."
        "Gwyddyon stares at your bag, clearly sizing up your gold carefully."
        $ gwydd_gold = int(pc.gold / 3)
        if gwydd_gold < 100:
            g "Well, no point for you to pay through the snout."
            g "Fill your pouch, and maybe we'll talk."
            "The sheep points at your gold, perhaps you've got too little gold for his taste. But he"
            jump Gwyddyon_Normal_Talk
        else:
            $ gwyddyon_tut += 1
            g "Misleading as a name often is, I'm not that greedy, in fact the opposite. You can buy my secret for only [gwydd_gold] gold."
            g "One Time Offer."
            if gwydd_gold >= 200:
                e "That's daylight robbery. I can just ask others about you..."
                g "Well. Who knows me better, a random stranger, those dimwits making out with each other up top, or me?"
                g "You can always keep your money, and I can always keep my secret."
            else:
                e "I suppose that's affordable."
                g "That's a bargain considering how broke you are for an adventurer."
            menu:
                e "Ehhphmmm..."
                "Ask about the History of the shop for [gwydd_gold] gold":
                    $ pc.gold -= gwydd_gold
                    $ gwyddyon_tut += 1
                    e "Alright, [gwydd_gold] it is."
                    "You hand the exact amount of gold to the complacent sheep."
                    g "Good. Would be a bummer for you to miss out on the deal of the century."
                    e "It's still extremely overpriced for a story."
                    g "I know."
                    g "Anyway, The Ardent Cauldron. I got here for quite a long time actually."
                    jump Gwyddyon_Ask_History_Cauldron
                "Decline the Offer":
                    e "I can't afford that, Gwyddyon."
                    g "Unfortunate."
                    "The shopkeeper glances back at the crystal, and returns to his usual pose."
                    jump Gwyddyon_Normal_Talk
    if gwyddyon_tut == 4:
        g "The Ardent Cauldron... I got here for quite a long time actually."
        jump Gwyddyon_Ask_History_Cauldron
    if gwyddyon_tut == 3:
        g "Can't help, wanderer. You declined the offer the last time we talked."
        e "What if I have the money... now?"
        g "Still a no. take a look at my other gadgets instead."
        jump Gwyddyon_Normal_Talk
label Gwyddyon_Ask_History_Cauldron:

    g "It was right after the previous shopkeeper was gone."
    e "Gone?"
    g "Died of Old age. Condolences."
    "Gwyddyon puts his hands together to pray for a second, before immediately returning to his usual boast."
    g "I was studying jewelry in the capital when her son planned to sell the place."
    g "See, what can be a better duo than me and a magic shop."
    e "Uhm... anything?"
    "The sheep scoffs at your comment."
    g "Anyhow, I bought the place at the highest price. Who knows all you need to beat a goat is with a bag of gold, and the shop is sold!"
    g "After I took over, the sale was better than ever. That old dragon Haskell's potion were good. But I had something much more useful."
    e "Mmhmm... Crystal?"
    g "That's right. Crystal. You know what they are capable of."
    g "Tevfik, Chieftain at the time, helped with the research. We basically reinvented different ways to harvest magical energy from crystal."
    g "Well, we planned to do the same for the primordial runes. Perhaps offer a movable magical source that's also unlimited."
    g "It could have been the most glorious discovery of a lifetime."
    g "And it was until the primordial runes was stolen, that everything took a turn for the worse."
    g "We lost that cheeky old bastard. Condolences."
    "Gwyddyon repeats the action of putting his hands together, but quickly put them away before he prays."
    e "I'm sorry about what happened, Gwyddyon."
    g "After that, his son took over the tribe. The research was put to a pause."
    g "Furkan, that dimwit tried to shift our tribe away from using magic. So thereafter, my shop hasn't been making the best money."
    "You wish to console the sheep, but before you can do so he begins to speak once more."
    g "That's the history of the shop in my hand. I don't know much about what happened to the previous owner."
    g "But her son was wise enough to let someone competent to take over, not a common occurence here apparently."
    g "..."
    "Gwyddyon pauses for a second, looking back at you with a slight repulsion."
    menu:
        g "Anything else you want to know...?"
        "How did you meet Tevfik":
            e "How did you meet Tevfik?"
            g "When I bought the shop, obviously. But we only formally met after opening the shop."
            g "He came to visit us during the soldiers' routine training. They bought almost everything from the shop, apart from the crystals."
            g "And I sold the first crystal to Tevfik."
            e "Did he know what it does?"
            g "He didn't. But he was fairly interested in these little precious novelty."
            g "The old ram invited me to his quarter soon after, we talked about magic the whole day, I didn't leave until the next morning."
            g "He was, quite a ram. But he had one weakness."
            e "What was it...?"
            g "He cared for his son too much."
            e "Oh..."
        "What was your life before being the shopkeeper":
            e "What were you doing before buying this place?"
            g "Did I forget to tell you? Anyhow, I was studying Jewelry Trading in the Capital."
            g "It was a breeze living in the capital. You've got everything you need as long as you're born rich."
            g "And I was, but I wasn't fond of the king over there."
            g "Gold had never been an issue for me. So I just bought the shop when I saw their poster flying in the street."
            e "Oh... That's it?"
            g "I didn't exactly care for the shop, until Tevfik came and saw the crystal I had for sale."
            g "Honestly, I didn't expect them to be sold, it was just my personal research."
            g "But after that day, customers keep coming right at my doorstep. Tevfik must have shared the news of my work."
            g "Living here was better than my life back then."
    "Gwyddyon give you a slight glance."
    g "Well, honestly, we have to call it a day here. I'd like to keep my remaining secret safe and sound."
    g "And so should you."
    e "W-wait, I've paid for this..."
    g "You've paid for a lot of my history already. A shopkeeper has to tend his shop, not to tell you bed-time stories."
    g "However, feel free to check out what I have here, spend as much as you want."
    "The shopkeeper returns to stare at his crystal, ignoring your silent protest and pleading."
    "Disheartened, you leave the sheep alone."
    jump main_ardent_cauldron

label Gwyddyon_Mining_Task:

    e "What's up with the rocks."
    g "They're minerals! Wanderer."
    g "I know you've been living with that dimwit of a lion, but please do not mistake my life-long invention just as another rock."
    e "Oh... Is that why Seb has a weird rock collection in his shop?"
    g "Those are rocks, I taught him when he first started with the shop with his lizard friend."
    g "But instead of getting fascinated by the amazing properties of magical crystals like a normal person would, he went to look at normal rocks!"
    g "Like this one."
    "Gwyddyon takes out a crumbly rock from his counter, it's coarse with patches of moss on top."
    "You stare at it for a while, it looks just like what Sebas has in his rock collection."
    e "Is this one magical?"
    g "NO! It's a normal rock I picked up from the road!"
    e "A-ah... alright. Seb would happily take it home and frame this thing along with the other rocks."
    g "Yes, and don't get me started with his unwillingness of learning basic rock classifying."
    e "But I think he knows what he's doing, if not for his study on the guardian's hand, I wouldn't have known about your Chief's situation."
    g "You're talking like I cared about the chief."
    "He pauses suddenly, staring at you with a raised brow."
    g "How are you still here anyway, shouldn't you be gone looking for your friend?"
    e "Maybe if you give me the clues as to where he went... that'd be much appreciated."
    g "Ambitious, aren't you?"
    g "Look, there's something I needed, getting me enough of them could grant you a privilege of talking to me."
    e "Is that a fair trade?"
    g "Depends on whether you're hardworking and all."
    g "You've been in the mines?"
    e "Uh? What mines?"
    g "Any mines at all, presumably from the werewolves."
    e "I did, how did you know?"
    g "You're shining of crystals. Those who are dimwits can't see the light, but I can."
    "Gwyddyon taps his finger on the monocles. Perhaps the glass has something reflective in it?"
    e "Am I a dimwit?"
    g "Yes, a different kind of dimwit, I must say."
    g "I don't require much effort, just give me a few of the minerals you've seen in the cave."
    g "I used to get them all the time when the brown one was alive, but every day in the dark forest is a dangerous one."
    g "Now they're killing each other again."
    e "Uhm... What do you need?"
    $ mineralofchoicy = renpy.random.choice(["Lodestone", "Copper"])
    $ task05.selection.append(mineralofchoicy)
    if mineralofchoicy in task05.selection:
        g "Like the last time, I'll need 10 pieces of [mineralofchoicy]."
    else:
        if mineralofchoicy == "Lodestone":
            g "Have you seen Lodestones?"
            g "Those are magical rocks that is embedded in nature."
            e "Why are they magical?"
            g "These rocks don't have magic. But they attract metal rocks, earlier folks used them for navigation dangerous forest."
            e "They're magnetic, aren't they?"
            g "Correct, that's why they come in handy for some ingenious devices I'm making."
            g "I don't need much, just 10 pieces of Lodestones would deem enough."
            e "Oh... ok."
        elif mineralofchoicy == "Copper":
            g "You know about copper, right?"
            g "Nothing fancy, just give me 10 of them."
    if task05.completedtimes == 0:
        g "After you finished, I'll give you what you deserve, 100 gold."
        e "That sounds fair."
        "You say sarcastically, with a raised voice."
        g "Fair? That's probably the greatest trade deal of the century, if not all time."
        "You were not sure if he's not too bright to notice the sarcasm, or he's willfully ignoring the glaring difference in rewards."
        g "And on top of that, if you've done enough, I can sell you some information about what I know."
        e "Really?"
        g "Real. For maybe 450 gold."
        e "But wait, doesn't that mean, I have to give you 350 gold, AND give you the [mineralofchoicy]?"
        "That was far too steep of a price, and you know Gwyddyon knows it too."
        g "It's what it costs."
        e "Damn, Gwyd. You're more of a ruthless businessman than Cane."
        g "Maybe we're both eying that bulge in your pant for a long time."
        "Was he flirting at you? He doesn't look like the type but admittedly you feel your crotch getting hard just from Gwyddyon staring at it."
        e "W-what?"
        g "It's the gold in your pouch. As an ardent researcher it's normal to require a substantial sum of capital investment."
        g "And I've not had access to anywhere up there because of those dimwits, so it makes sense why I'm squeezing every little gold out of you."
        g "I used to be an exception, under his father's order. But now, no one is allowed anywhere near the site."
        g "It turns out that apple does fall far from the tree."
        "Gwyddyon scractches at his monocle."
        e "I think Furkan is just a different leader than who Tevfik was."
        "He raises his brow again, this time paired with a concerned look."
        menu:
            g "Do you trust him?"
            "I trust Furkan":
                $ gwyd_trust_furk = True
                e "I do. He's loyal and capable."
                g "It's going to cost you a lot trusting someone who you know nothing about..."
                "You still believe Furkan deserves some merits, regardless of what the goat tribe has been lately."
            "I do not trust Furkan":

                $ gwyd_trust_furk = False
                e "He is a good friend, but sometimes his decisions are... questionable."
                g "Well, see? I know we'd have more in common than a clueless ram who's out of his depth."
                "You remain silent, even you've advocated for Furkan, you can't stop but see the deep troubles goat tribe has gotten into."
        g "Now I know a little more about you, with the price of nothing."
    else:
        e "Still the same reward?"
        g "Yes, 100 gold, and an additional opportunity to talk about anything else you need."
        e "You're really talking like it's worth the price."
    "Gwyddyon shows you a faint smile, before he sends you away."
    g "Go now, Wanderer. Don't come back until you've gotten what I needed."
    $ TaskBegin(task05)
    jump Gwyddyon_Normal_Talk

label Gwyddyon_Mining_Task_Inquire:
    e "Hey, Gwyd. What do I need again?"
    if mineralofchoicy == "Lodestone":
        g "Lodestone, inside the cavern in the dark forest."
    if mineralofchoicy == "Copper":
        g "Copper, inside the cavern in the dark forest."
    g "I need 10 of them so you better hurry up."
    e "O-ok..."
    jump Gwyddyon_Normal_Talk

label Gwyddyon_Mining_Task_End:
    e "Gwyd, I've returned with the [mineralofchoicy]."
    g "Is the number right?"
    e "You put forth all of the [mineralofchoicy], and push in front of him."
    e "Yes, all 10, on the counter, right now."
    g "Hmm. That one's a little funky, but I'll accept your effort."
    g "Here's your reward. all 100 gold, fair price, isn't it?"
    if task05.completedtimes == 2:
        g "And I'll tell you what you needed, for another price, as promised."

    e "T-thank you?"
    g "That's not a sincere one but I'll let you off the hook for now."
    msg "You received 100 gold from Gwyddyon."
    if task05.completedtimes == 2:
        msg "New Shop Item from Gwyddyon Unlocked!"
    $ TaskFinish(task05)
    jump Gwyddyon_Normal_Talk



label Gwyddyon_Research_Quest:

    g "W-welcome to the Ardent Cauldron, we're almost closed-"
    "You hear the usual accosting, only this time it's in a raspy voice."
    "The magic shopkeeper looks up, and he is greeted by your dumbfounded face."
    g "Wanderer, you're just in time, look at this thing."
    e "H-hey Gwyd, what's that?"
    g "A crystal I found in my stash. It was from near the primordial runes."
    g "I collected the crystal back before it was gone, I never got to learn of its true power."
    g "I just happened to remember it when you just arrived to my shop."
    g "But I gotta say, the dust on that thing is going to give me hack of a cough no magic is going to cure."
    "Gwyddyon points to his throat, you can still hear the croaky breathing as he speaks."
    e "Uh... I hope you recover soon?"
    g "Yeah. We're talking crystal here, don't distract yourself from my sore throat."
    g "Nothing is going to fit inside this for a while- I mean food, eating."
    "You give him a concerned glance, only to for him to ignore you entirely and stare back at the crystal."
    g "C-crystal. Don't you ever fiddle with this one, my friend. It can only be handled with a professional hand."
    g "Especially when there's not many evidence or research ever done on the subject matter."
    g "We shall be extra careful, regardless of how many times you helped me deliver the minerals, or the discount I spared you."
    e "What discount?"
    g "That's the spirit, you need to forget they have ever existed."

label Gwyddyon_Voting_Trade:

    e "Gwyd? Would you mind if I ask some questions?"
    g "Would you mind if I say no? I'm onto something much more important here."
    e "Uh... yes."
    g "Hmmph, well wanderer. Since I care too much about a courier's opinion of me, as you may have believed. You may ask away."
    "Gwyddyon continues glancing into his lens, not even trying to acknowledge your presence."
    $ gwyddyon_sussy = 0
    $ gwyddyon_cockorbutt = False
    menu:
        e "Uh..."
        "Where did you find the crystals?":
            $ gwyddyon_sussy += 2
            e "So! Where did you find these crystals?"
            "You point at the one Gwyddyon is holding."
            g "Why... why do you need to know?"
            e "Uh- I was just making up conversations, Gwyd. And it's never you who start one."
            g "Maybe because I'm not as interested in you than you'd think. Also, that's a fairly weird thing to ask, [e]."
            g "Are you trying to open another shop?"
            e "No! Of course no."
            "Gwyddyon squints his eyes, his brows still remain furrowed as he resumes his inspections on the crystals."
        "Lovely weather today, isn't it?":
            $ gwyddyon_sussy += 1
            e "Lovely weather today, isn't it?"
            "Gwyddyon continues ignoring you, doesn't even sparing another glance."
            e "Gwyd!"
            g "Do I have to engage in meaningless small talks with you right now?"
            e "You said I can ask any questions."
            g "Well, it doesn't mean ALL questions, you dimwit."
        "What are the rocks on the counter?":
            $ gwyddyon_sussy += 1
            e "So, what are those rocks in that display?"
            g "Uh, they're just decorative rocks, nothing magical about those."
            e "But these look kinda pretty, no?"
            g "Yeah, I told that lion from the other shop to collect them for me so he can finally leave me alone."
            g "Little did I know, he spent days and weeks trying to collect useless rocks, soon he started giving me different shapes of rocks as some weird gifts."
            g "And I considered that... a toll on my mental capacity."
        "Cock or Butt?":
            $ gwyddyon_cockorbutt = True
            $ gwyddyon_sussy += 2
            e "Cock or Butt?"
            g "What?"
            e "well, which side are you on?"
            "Gwyddyon furrows his brows and stares at you with a weird look."
            g "I'm not answering that."
            e "So, it's butt, right?"
            g "Alright now can you stop this circus for once? I thought we're here for civil, enlightening discussions."
            e "That question was very enlightening."
        "How many customers will buy these crystals from you?":
            $ gwyddyon_sussy += 3
            e "So, how many customers are interested in these crystals?"
            g "Uh, are you Furkan? Because you ask the same nonsense as that dimwit of a leader does."
            e "Well, I suppose the number is low."
            g "Wanderer, there's a limit to my patience here. If you're not here for my goods, the door's right there and you're welcomed to pass through, one way trip."
    "Just as Gwyddyon turn around for another procedures to his job, you shout to get his attention quickly."
    menu:
        e "Wait..."
        "Where do your top products come from?":
            $ gwyddyon_sussy += 1
            e "So, I see there were some gemstones and crystals you have there on the shelves. Did you make them all by yourself?"
            g "Yes, I did. Where else do you think they come from?"
            e "I don't know, I thought you were working on a magic shop, not a mineral reserve."
            g "Huh, well. Maybe you're right, those are from someone else who lives far away from here, admittedly a little more fastidious than Haskell, or, a little more."
            g "But, there's one thing about him that's been generally troublesome."
            e "What's it?"
            g "Ugh, don't ask. I'm working on it."
            g "Still, a crystal is useless unless you understand how to harness its power. I've raised his stones' value almost nine-fold selling them here. How can he not appreciate my work."
        "How did your shop earn such a reputation?":
            e "How did you get your reputation as the shopkeeper of the goats?"
            g "Don't know much about reputation, but this? This place is the heart of the tribe. A central hub for every goats to trade and talk."
            menu:
                g "How would you associate goats? The magic. And what do you think of when someone talks about magic?"
                "The goats?":
                    $ gwyddyon_sussy += 2
                    e "Well, the goats?"
                    g "No! You dimwit of a dimwit. That doesn't even make any sense, are you going to think about magic next? How creative."
                    e "Uh, I thought it was a question...?"
                    g "Yeah, perhaps I expected too much of you. The answer is right here, the Ardent Cauldron."
                "Ardent Cauldron?":
                    e "Ah! Ardent Cauldron, of course!"
                    g "Needless to say, you are undeniably correct."
                "Uh...":
                    $ gwyddyon_sussy += 1
                    e "Uh..."
                    g "Uh what?"
                    "You stumbles on just a little silence, before Gwyddyon pouts."
                    g "Yeah, perhaps I expected too much of you. The answer is right here, the Ardent Cauldron."
            g "I've spent dozens of years, building up this shop step by step. Moreso invested my whole life's saving into promoting our crystals."
            g "To be recognised by everyone, of course the placement of the shop is important. But more importantly we sell only carefully selected items right here. No more subpar potions or common rocks you pick up by the road."
            g "We are here to sell something magical. Something that makes you feel luxurious, and of course, the price is one of the experience."
            e "Wait, you mean you set the price this high, just because people liked... expensive things?"
            g "It'd be a lapse in judgement to say our everyday customers can discern between high grade crystals and the lower ones, wouldn't you say? We need a high profit margin here to maintain a sustainable line-up of our daily magical necessities."
            g "Besides, doesn't a cheap item, makes you feel cheap? Doesn't it feel too effortless?"
            e "I- but these are people's necessities, right?"
            g "Don't you worry, wanderer. They can absolutely pay for that. Our customers are wealthy bunch who'd pay to maintain their flamboyant magical lifestyle. The only concern is our chief unfortunately had taken that away, along with many other things."
            e "Alright, but I'm still baffled you said that so nonchalantly."
        "Are there any particular disdain you had with Furkan?":
            e "So, Gwyddyon, why do you seem to hold a particular grudge against Furkan?"
            g "What about my story that you are still interested in? Thought we were over that, by the first day you enter the shop."
            e "Perhaps I was a little fascinated by your obsession of, slandering your own chief."
            g "Well, speaking of fascination, I'm just a little more fascinated by your insatiable lust for knowledge, isn't the lusterfolks enough of an experience for you?"
            e "No..."
            "You shoot him with a captious stare, which surprisingly tamed his arrogance, to some extent."
            g "Ahem, I'd like to keep my secret for myself. But mayhaps that obsession you mentioned, tipped over my rational edge, so I can explain away."
            g "You know what happened to Tevfik, his father. It was pure tragedy."
            g "I am but an outsider to their internal affairs, but when it affected my livelihood directly, how could I not speak out?"
            e "Why would they affect your livelihood?"
            g "Once in a while, his mate brings his guards here to check out my shop, scoops around like the shop's theirs."
            g "And of course, that always spooks my customers away like flies they go. And it worked every time."
            menu:
                g "In what world does that make sense, that they're driving their own tribe's main business away, I truly have no idea."
                "Maybe you're hiding something?":
                    $ gwyddyon_sussy += 2
                    e "Well, maybe he believes you're hiding something? You know, especially with how cagey you get every time I bring Chime up?"
                    g "What are you trying to tell me, wanderer?"
                    e "Nothing much."
                    g "Then I'm just gonna pretend I didn't hear any of those."
                "Furkan's just overly cautious":
                    $ gwyddyon_sussy += 1
                    e "I mean, he's just cautious, after everything that went down, how can you expect him not to do so?"
                    g "I reckon, if you can justify his cautiousness, then it's only fair you justify mine."
                    g "Plus, it's my shop that they're ruining."
        "Any secrets about the shop that you've been holding off?":
            $ gwyddyon_sussy += 3
            e "Would you share any secrets about the shop that you've been holding off?"
            g "No, I would not."
            e "Uh... that's it?"

    g "Any more of those interesting questions? Get it out of your system while I'm still on the mood."
    menu:
        e "Well..."
        "Are there any new products for sales?":
            e "So, any new stuff that I can probably take a peek?"
            g "W-what's this new stuff matter you're talking about?"
            e "Uh... you know, new invention, cool gadgets. Any insider news for a potential buyer?"
            if gwyddyon_sussy > 2:
                g "I don't think you're buying anything worthwhile for me, or I'm not selling them to you."
                e "Why not? I am a fan of your shop!"
                g "Unfortunately I'm not a fan of the conversation we've had. So no, wanderer."
            else:
                $ ole_got_gwyd_answer = 0
                g "Honestly, I don't see you as a potential buyer or investor type, wanderer. But, there is one thing I was working on."
                e "Ooooh! What's it?"
                g "Hmmph... actually it's not for sale. I just had to work on a toy to impress my mineral supplier. He's a finicky type."
                e "A toy?"
                g "Ugh, yes. He's not the typical reasonable businessman who'd like to talk pragmatic, no time for that. He wanted something called... a harp, just to extend our agreed-upon contract."
                g "And he was not making a joke, nor exaggerating. I had known him since I first got into business, and I know he'd still bail on my business... just because I don't get his requirements right."
                "Gwyddyon places his hand over his face, sighing in frustration."
                g "Call it, an artist's pertinacity."
                e "What does that word mean?"
                g "A grudge, stubbornness, or unwillingness to listen to anyone at all. This is a magic shop afterall, not a music shop, how would I know how to make a harp?"
                g "Not a thoughtful comparison, but he's like Haskell except he quits on people too easily. Even though I had helped him by selling his crystals, which majorly contributed to his current wealth."
                g "But, well. Some people don't ever listen."
                "Gwyddyon sighs, suddenly turns to you and shakes his head."
                g "What am I talking about! Nonsense, no one should know about this, wanderer."
                e "A-alright, you'll have my words."
                g "I mean no one."
                "He furrows his brows while looking at you up and down for a few seconds, only turning onto his other work after you make out a wide awkward smile."
        "Any secrets about the shop that you've been holding off?":
            e "Would you share any secrets about the shop that you've been holding off?"
            g "Yeah, been keeping my secret for years."
            g "Actually, I lied when I say you are welcomed in my shop any time."
            jump Gwyddyon_Voting_Fail
        "Cock or Butt?":
            e "Cock or Butt?"
            if gwyddyon_cockorbutt:
                g "Are you seriously asking this one again? Do you seriously think I forgot the last time you asked and this time I will magically answer something."
                g "Or do you think I use my balls to think like those other dimwits walking around half-naked for some reason?"
                e "Uh, neither? Just asking for your opinion."
                g "You know what? You're out now."
                jump Gwyddyon_Voting_Fail
            else:
                g "What?"
                e "well, which side are you on?"
                "Gwyddyon furrows his brows and stares at you with a weird look."
                g "I'm not answering that."
                e "So, it's butt, right?"
                g "Alright now can you stop this circus for once? I thought we're here for civil, enlightening discussions."
            e "That question was very enlightening."
        "How did losing the primordial runes affect your shop?":
            e "So, how did losing the primordial runes affect your shop?"
            g "Hugely, there were a lot more folks interested in our magics before the whole debacle. Not anymore, now people are looking into potions, and moreso ranged weapons."
            g "But I tell you, crystals. They'll replace whatever the runes had in the people's heart. This situation, it's only temporary. Sooner or later, everything will be back to normal."
            e "Alright."
    g "Okay then, that marks the end of your interrogation time."
    e "W-wait, I still have a few more quest-"
    g "Nope, not interested in answering, now if you're interested in my products, feel free to buy them."
    e "Can I ask some more questions if I buy some products?"
    g "No, obviously."
    e "Ugh, alright. Just like what you say - you're missing out on a valuable business opportunity."
    g "And just like what you say - uh nuh."
    e "I didn't say that?"
    g "Yes you did, now stop bothering me."
    "You sigh, Gwyddyon lets out a genuine chuckle before quickly returning to his work as he continues pretending you don't exist."
    $ quest39.status = 3
    $ quest39.qComp(_("Report to Ole"))
    jump main_ardent_cauldron

label Gwyddyon_Voting_Fail:
    $ quest39.status = 3
    $ quest39.qComp(_("Report to Ole"))
    e "W-what? What did I do?"
    g "It's too obvious how you're probing information from my shop. More obvious that you're fidgeting non-stop here."
    g "Do you think I'm foolish enough to fall for that?"
    e "Why would I do that?"
    g "Ask that yourself, and I'm not interested in knowing, thank you for the offer though."
    g "Now, let's get you out of here."
    "Gwyddyon puts down his crystals as he walks out of his counter. You're looking at him in both confusion and shock."
    g "Excuse me."
    "He holds onto your waist like it's butter, it's impossible to imagine how delicate his touch is, despite him essentially throwing you out of his shop."
    "The shopkeeper pushes you further as you struggle against his grasp."
    e "Hey! Get off me, Gwyd."
    "He doesn't respond. Only grunts as he forcibly wraps his arms around you, raising you up so high up that you feet begin to leave the ground."
    "You yelp, stomping against his shoulder as he carries you over, his hands moves to your ass naturally for support, making you squirm loudly."
    e "Can you put me down? I can walk over there myself actually."
    g "Unfortunately, I don't believe you have that capability on your own, and intention."
    "It feels like a daily chore to Gwyddyon, he doesn't even react when your fist stomps his back, he is just moving you around like a heavy crate."
    "You're soon standing on the ground outside as he puts you down, patting on his shoulder to tidy up his attires."
    g "I should've written a sign that says, 'information thief is not welcomed here'."
    e "Okay, I get it, Gwyd. You don't have to hammer it in on my face over and over again."
    "He chides, before returning to his shop, he didn't say you can't enter his shop, but it's pretty obvious that he's onto your plan now."
    jump main_kechioeren01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
