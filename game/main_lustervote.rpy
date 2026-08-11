label Sebas_Voting_Result:

    e "So... the village vote has finally ended, huh?"
    s "Yeah, roomie. It's been a long week."
    "Sebas stares at you with a curious look, as he taps on the front of the counter whimsically."
    if vote_result < 0:
        e "But I'm sorry though, I know you were hoping for a different outcome."
        s "It's fine, [e]. I'm just... disappointed. I thought we could have a better future with the goats."
    else:
        e "I'm glad the village is finally making a decision, I'm sure it's for the best."
        s "It's great! I'm sure our shop will be more lively with the goats around. I can't wait to see their wares."
        e "I'm sure it will be a great opportunity for both sides."
    if sebas_caught:
        "Sebas smiles faintly. It's not his usual wide grin. You can tell he's still a bit shaken from the night in the wagon."
        "But considering it is something he held dear to, you do not have the heart to ask him again."
    jump Sebas_dialogue

label Ole_Voting_Result:

    e "Ole, what do you think about the votes?"
    o "Hmm..."
    o "I liked it. It's been a while since I've seen this many people in Lusterfield."
    o "That day, we worked quite hard to secure and count the votes, we were being cautious."
    o "And, it turns out, those few votes matter quite a lot in the grand scheme of things."
    if vote_result >= 0:
        o "Overall, I'm glad Lusterfield might have an ally on their backs, it helps see what's there to come."
        if vote_choice[6] == 1:
            o "And with the shopkeeper tamed to the bone, I reckon our shop will thrive with the new alliance we have upon us."
        else:
            o "Even though there still lies a big problem with Gwyddyon. We will need to figure out something later."
    else:
        o "It's so-so. I can't fault those who voted in favour of solitude, it is what most wanted."
        o "Albeit, Seb's not having the moment of his days right now."
        if vote_choice[6] == 1:
            o "It was kind of a waste to have negotiated with their shopkeeper. But at least we've got ourselves some cheap wares as well."

    jump Ole_dialogue

label Lothar_Voting_Result:

    e "Lot..."
    l "You coming to ask about the stupid vote?"
    e "Uh... maybe?"
    if vote_result >= 0:
        l "I don't fucking care, if a horned scumbag comes up here, you better believe I'll run him down and teach him a lesson."
        e "Not including me... right?"
        e "Right?"
        l "You better believe you've got dragon blood more than your goat blood, disciple. My fist doesn't recognise faces."
    else:
        l "Luckily the village came to their own common senses. Else we've got a big problem here."
        e "Okay... I'll keep that in mind."
    jump Lothar_Dialogue

label Amble_Voting_Result:

    e "How was the vote?"
    a "Oh, puny friend."

    if vote_result >= 0:
        a "Overall, I'm glad Lusterfield might have an ally on their backs, it helps see what's there to come."
        if vote_choice[5] == 1:
            a "Now that the bridge has been restored, I'm seeing a lot of dry pants from here. Imagine the stink after walking over the river..."
            e "Yeah, I'm glad we built one."
            a "But... I'm afraid for Lothar. And I have no idea where he went..."
        else:
            a "They planned to rebuild the bridge over the river crossing, think I might tell Jog to join soon 'nough."
            e "Oh, you are going to tag Jog along as well?"
            a "Of course! The bridge is the most crucial part of the alliance, how would you ask everyone to trod through the river every time they travel between."
            a "I had wanted to restore it myself, but now at least the goats are helping."
    else:
        a "The village is not going to ally with the goats, I'm not sure if it's the best choice. But it is what it is."
        if vote_choice[5] == 1:
            a "At least the bridge will be kept. We can safely travel between the two forests without having to worry about the river."
            e "I'm glad you're seeing the bright side of things."

    jump Amble_Dialogue

label Jog_Voting_Result:

    e "Jog, how do you feel about the vote?"
    j "Vote, vote, vote. Always talking about the vote. It's long past midnight my brother."
    e "Yeah, but what's your opinion?"
    if vote_result >= 0:
        j "My opinion is this vote sucked, now that the goats reinforced their huntsmen I can feel them everywhere."
        j "Can't even climb a tree now, so boring."
    else:
        j "Eh. Business as usual, I wouldn't have expected otherwise."
    if vote_choice[4] == 1:
        e "What about your vote? Did you vote for the alliance as well?"
        j "Of course I did, and it's all for you. Can't say if I regretted that but Lothar is coming for my ass right now."
        if vote_result >= 0:
            e "Uhm, surely not. I don't know where he's gone but if he intended to come for your ass he'd do it on the spot, no?"
        else:
            e "I don't believe that, Lothar doesn't seem that angry at you, there's no alliance now."
        j "Maybe. Maybe."
    jump Jog_Dialogue

label Cane_Voting_Quest_Ask_Rat_Patron:
    e "Cane, what exactly should I do with the ghost again?"
    c "Eh? What'cha wanna know, that rat?"
    if cane_dialogues.get("Rat Patron Day", False) <= 0:
        "You nod."
        c "Ya gotta find him in the afternoon, get some information out of 'em. We oughta know if that pesky ghost exists or not."
        e "Got it!"
    else:

        e "I've met that patron, but he doesn't seem to want to talk with me..."
        c "Ah, lad. Ya know what I've learnt after serving beers to those scums like that rat, ya never talk soft with 'em, ya gotta scare them at first and show 'em their place, just like how I taught ya."
        "Cane glances at you again, then smiles."
        c "Fine, maybe yer not the type to scare 'em off like that, but... it'd be a nice try at least."
    c "Do what yer good at, okay lad?"
    "The tavernkeeper grins."
    jump Cane_Normal_Talk

label Rat_Patron_Dialogue:
    $ cane_dialogues["Rat Patron Day"] = timenow.day

    if not cane_dialogues.get("Rat Encounter", False):
        $ cane_dialogues["Rat Encounter"] = 1
    else:
        $ cane_dialogues["Rat Encounter"] += 1
    if quest45.status >= 3 or quest45.status == True or cane_dialogues.get("Rat Patron Info", False) != False:
        jump Rat_Patron_After_Probing
    "A pungent, rotten smell hits you as you wander the tavern. Within moments, you spot its source — a scruffy rat-like patron huddled in a far corner."
    e "Hey."
    "The rat barely glances up. With a dismissive snort, he turns back to his beer."
    e "Excuse me, are you listening?"
    if cane_dialogues["Rat Encounter"] == 1:
        "The rat narrows his eyes and starts edging toward the door."
        e "Hey! I'm talking to you!"
        "You grab his arm firmly. In an instant, every eye in the room is fixed on you as you clutch his matted fur."
        "After a brief struggle, the rat finally looks you in the eye, a mix of anger and resignation on his face."
        rat_patron "Let go of me!"
        e "Not until you stop going away!"
        $ timer_time = 3
        $ renpy.pause(renpy.random.random()*0.5+0.25)
        show screen countdown("Rat_Patron_Fail", 3, 2)
        menu:
            "A sudden gust of wind rattles your head..."
            "Dodge!":
                hide screen countdown
                "You quickly sidestep the gust, though the rat's agitation remains evident."
                jump Rat_Patron_Continue_Grab
            "Steady yourself":
                jump Rat_Patron_Fail
    else:

        if cane_dialogues.get("Rat Patron Escaped", False):
            rat_patron "You were that annoying scumbag the other day, what do you want?"
        else:
            rat_patron "You again? Did I not tell you to leave me alone enough?"
        e "I still need to talk to you."
        "The rat shakes his head, then stands up and gestures you to follow him."
        scene lusterfield02 with dissolve
        "You follow him outside, where he leans against the tavern wall."

        menu:
            rat_patron "What do you want?"
            "Try to befriend the patron":
                e "Look, I'm not here to cause trouble. I just want to know more about you."
                rat_patron "I'm not interested."
                e "I heard about your story about the ghost, right? I'm just curious."
                rat_patron "I don't care, and I know you're here not just for your own curiosity."
                jump Rat_Patron_Empathise
            "Push him for more information":
                jump Rat_Patron_Push

label Rat_Patron_Continue_Grab:
    "You manage to evade a swing aimed your way, though the rat still struggles."
    $ timer_time = 3
    $ renpy.pause(renpy.random.random()*0.5+0.25)
    show screen countdown("Rat_Patron_Fail", 3, 2)
    menu:
        "Another fist flies from the side..."
        "Stay Still":
            jump Rat_Patron_Fail2
        "Hold on tight":
            jump Rat_Patron_Fail2
        "Evade the punch":
            hide screen countdown
            "You deftly sidestep the blow, drawing a mix of cheers and boos from nearby onlookers."
            jump Rat_Patron_After_Fight

label Rat_Patron_Fail:
    "Cursing under his breath, the rat scrambles off into the shadows of the tavern, leaving you empty-handed."
    "You glance around, the rat is now nowhere to be seen. You have to hope he would come back, or you'd have to deliever the bad news to Cane."
    $ quest45.qProgress(_("Wait for the rat patron to reappear, or tell Cane about the rat..."))
    $ cane_dialogues["Rat Patron Escaped"] = True
    jump main_nocturnaltrunk

label Rat_Patron_Fail2:
    "A wild punch sends you reeling for a moment, and in the confusion the rat escapes amid mocking laughter."
    "You glance around, the rat is now nowhere to be seen. You have to hope he would come back, or you'd have to deliever the bad news to Cane."
    $ quest45.qProgress(_("Wait for the rat patron to reappear, or tell Cane about the rat..."))
    $ cane_dialogues["Rat Patron Escaped"] = True
    jump main_nocturnaltrunk

label Rat_Patron_After_Fight:
    "After a tense few seconds, the rat calms down and gestures for you to follow him outside."
    rat_patron "Alright, I guess I can't shake you off."
    "His grip suddenly tightens as he pulls you out of the tavern."
    scene lusterfield02 with dissolve
    "Outside, near the Nocturnal Trunk, you find him waiting. His ragged clothes and the bruises beneath his eyes tell their own story."
    e "I finally caught you. Why are you always running, anyway?"
    rat_patron "I thought you were with the loan shark—those bandits swiped everything I had. They're trying to keep me in line."
    rat_patron "And you're the new server, aren't you?"
    "You nod."
    rat_patron "Hadn't been back here for a while, I didn't even realise this place has a new server until some loud assholes over the tables talked about some goat with an apron."
    e "I'm a dragon."
    "He gives you a wary sidelong glance."
    rat_patron "So, why are you after me? I already spilled everything to Cane."
    e "I'm not here to stir up trouble. Cane mentioned you saw… something. A ghost, or so I hear?"
    "At your words, a flicker of worry crosses the rat's face."
    rat_patron "Look, I'm not making this up. There's a ghost in that cursed tavern."
    e "Really? Where did you see it?"
    rat_patron "I… haven't seen it since that night."
    "He sighs and runs a rough hand over his head."
    rat_patron "Look at this."
    "He lifts his hand, and you see a small burn mark on the pads of his palm."
    e "That mark came from the ghost?"
    rat_patron "Yeah. It was like a shadow with burning red eyes... But that's all I got."

    menu:
        "Empathise with the patron":
            "You lean closer, softening your tone."
            e "That sounds awful. I can't imagine how shaken you must've been."
            rat_patron "Why do you even care? You're just another busy fool."
            e "I'm trying to help — this doesn't look like a normal burn mark, what if something'd happen to it?"
            rat_patron "That's my problem... not yours."
            jump Rat_Patron_Empathise
        "Push for more details":
            jump Rat_Patron_Push

label Rat_Patron_Empathise:
    "The rat's eyes narrow, and he shifts uncomfortably."
    menu:
        rat_patron "Now drop the act and tell me why you are here in the first place."
        "I'm here for Cane":
            e "I need to get to the bottom of this for Cane's sake. This ghost rumor's damaging his tavern's reputation."
            rat_patron "Help Cane? You really must be one of those goody-two-shoes. Good for you."
            rat_patron "But, no. I don't want any part of that old keeper's problems."
            e "Why? Do you have a history with the tavern?"
            rat_patron "No, look. I'm just coming back for a few days until that vote begins. And I honestly don't care if I leave the village with this little tavern burning down."
            rat_patron "I am just saying. It's so obvious I'm not gonna be the one burning it down, if it ever does... I'm not saying it's gonna burn down."
            jump Rat_Patron_Probed_Info_Fail
        "It's for my own safety":
            e "Honestly, I just can't stand thinking about a ghost lurking around. I need to know for my own peace of mind."
            rat_patron "Maybe try quitting the job, it doesn't sound like you work around here all the time."
            e "Why run when you can easily fix the problem. Your advice's not always the solution I'm afraid."
            "The rat's gaze darkens. His voice drops to a hushed murmur."
            rat_patron "I pity your ignorance, server."
            jump Rat_Patron_Probed_Info_Fail
        "I'm just interested in your story":
            e "Look, I'd just like to hear the full story if you're willing."
            rat_patron "Why do you think I'm just telling you everything because you are interested?"
            menu:
                "Show Charisma":
                    e "I'm sure you'll find the heart to just tell a little server about your story."
                    if pc.cha >= 6:
                        rat_patron "Alright, alright..."
                        rat_patron "I just happened to feel generous today. Don't need to say your piece."
                        $ cane_dialogues["Rat Patron Info Method"] = "Charmed"
                        jump Rat_Patron_Probed_Info
                    else:
                        "The rat looks up and down, before shaking his head."
                        rat_patron "Nah."
                        jump Rat_Patron_Probed_Info_Fail
                "Concede":
                    e "I don't know. Empathy?"
                    rat_patron "What?"
                    rat_patron "You are a funny goat, saying funny words like anyone's gonna understand."
                    jump Rat_Patron_Probed_Info_Fail


label Rat_Patron_Push:
    e "Alright, now stop beating around the bush — just tell me everything without the runaround!"
    rat_patron "Hey, chill out! I told you what I saw."
    e "You're hiding something, isn't it. That's why you're dodging my question."
    rat_patron "Okay, so? Can't a rat keep some of his secrets? I have no duty to tell you anything, server."
    menu:
        "Intimidate the rat":
            e "Maybe you can't. What if I told the bandits that one of their precious debtor's actually have the gold to drink beer."
            "You whisper with a devious smile."
            rat_patron "You don't dare. You are just a server here."
            e "It's really easy to have rumors spread all over the village, even out of it. I don't even have to do it myself."
            if pc.cha < 8:
                rat_patron "Then do it."
                e "What?"
                rat_patron "Do it."
                rat_patron "That's what I thought, you don't have legs to stand, server. I've been in this for too long to see who's not made out of it."
                $ cane_dialogues["Rat Patron Info Method"] = "Charmed"
                jump Rat_Patron_Probed_Info_Fail
            else:
                rat_patron "Fine. Fine. I get it. I'll tell you whatever you want. Just leave those bandits out of it."
                e "That's more like it."
                jump Rat_Patron_Probed_Info
        "Keep pushing":

            e "I'm not playing around. I need every detail right now!"
            "You lean in closer, your voice low and urgent. But the rat doesn't even faze."
            rat_patron "You know what? That's it. I'm done. I already told you what I remember. You're just not worth my time."
            jump Rat_Patron_Probed_Info_Fail
        "Concede":
            e "Fine. Keep your secret."
            rat_patron "Okay."
            "The rat looks at you with an amused smirk."
            rat_patron "You looked foolish when you tried to push me around, regardless of its success, it was certainly an attempt."
            e "I'm trying to make you talk."
            rat_patron "How are you trying to make me talk, server. That's like the most pathetic attempt, if it ever was one."
            e "Are you trying to make a fool of me?"
            rat_patron "No, I just find you interesting, that's all."
            menu:
                rat_patron "I need something... more material, before I can tell you anything substantial."
                "Pay him gold":
                    e "Look, I'll pay you. How much do you want?"
                    rat_patron "2000 gold, that's what I owed to the shark."
                    e "T-that's a lot!"
                    rat_patron "Well, you're not exactly like the other assholes, I'll spare you half of it."
                    rat_patron "1000 gold."
                    jump Rat_Patron_Concede_Push_Menu
                "Offer personal service":

                    e "Well, how about this, you get some time to do with me anything you want."
                    rat_patron "Is this an invitation or..."
                    e "A deal."
                    rat_patron "Okay. Good. As long as you perform as good as I've heard."
                    $ cane_dialogues["Rat Patron Info Method"] = "Sucked"
                    jump Rat_Patron_Personal_Service
                "Concede":
                    "Despite the rat's dismay, you shake your head."
                    e "Hmmph... I don't know? I can't offer anything worthwhile for you."
                    menu:
                        rat_patron "I'd have thought you've got my hint. Fine, I'm interested in getting an hour with you, it's not that hard to understand, right?"
                        "Accept the invitation":
                            e "Fine, the information's better be very helpful."
                            jump Rat_Patron_Personal_Service
                        "Deny his request":
                            e "No. I'm afraid."
                            rat_patron "Disappointing. Then you've got nothing useful for me then."
                            rat_patron "I'm going."


    jump Rat_Patron_Dialogue_End

label Rat_Patron_Concede_Push_Menu:
    menu:
        "Pay him" if pc.gold >= 1000:
            e "Fine, here it is."
            "You pull out your bag, handing him the gold as he grins."
            rat_patron "Thank you."
            e "Now, the promised secret."
            $ cane_dialogues["Rat Patron Info Method"] = "Paid"
            jump Rat_Patron_Probed_Info
        "{s}Pay him{/s}" if pc.gold < 1000:
            "You don't have enough gold."
            jump Rat_Patron_Concede_Push_Menu
        "Offer personal service":
            e "Well, I don't have that much gold."
            e "How about the other option..."
            e "I'll do whatever you want."
            rat_patron "Whatever... I want?"
            $ cane_dialogues["Rat Patron Info Method"] = "Sucked"
            jump Rat_Patron_Personal_Service
        "Concede":
            e "Well, I don't have that much gold."
            rat_patron "That's a shame."
            rat_patron "I'll be here next time, if you have the gold."
            jump Rat_Patron_Dialogue_End

label Rat_Patron_Personal_Service:

    e "Yes, I kind of get what you meant when you said that, but now will you not ogle at me like I'm some piece of fine meat."
    rat_patron "Oh, you are. I mean, look at you."
    e "Mhmm, so... what do you want me to do."
    rat_patron "Hey, don't worry. It'll be very quick, server, or I will make it very quick."
    rat_patron "Come."
    "You follow the rat as he walks around Lusterfield."
    scene lusterfield01 with dissolve
    if sum(tavern_date) > 0:
        rat_patron "So, a private show, huh? I didn't know nowadays a server had to do that as well. That's what I heard, anyway."
        e "The customers happened to like it when I served the tavern, so they asked Cane about that."
        rat_patron "I see. So, that barkeep's a pimp as well?"
        e "I wouldn't call him that... he doesn't even get any gold from the show."
    else:

        rat_patron "So, you work in the tavern. How's the job. Did the keeper overwork you to the last bit."
        e "What? He'd never."
        rat_patron "Just a question. I figured he'd do that."
        e "I am just here to work once in a while, relieving Cane of some duty, not a full-time server here."
    "He shoots you back with a knowing glance."
    rat_patron "Oh, and I heard about the apron. It fits you snuggily, doesn't it."
    e "Yeah, that's the former server's. Cane gave it to me."
    rat_patron "Mhmm... good. Keep it clean then."
    rat_patron "Here. No one's going to see us."
    scene lusterfield_alleyway with dissolve
    "The rat pulls you into a dark alleyway, away from the tavern's prying eyes."
    e "You know, I can probably take you to one of Cane's room."
    "You glance around, slightly confused as to why the rat wanted it this way."
    rat_patron "No, I want it right here, in this dingy alley."
    rat_patron "I want to see your face when I give you something no one else can."
    "You nod, still a bit confused but willing to do what the rat wants."
    rat_patron "Come on, I won't bite. And I'll tell you all about the ghost after."
    "The rat whispers, taking a seat on the cobblestone ground."
    call Scene_Rat_Patron_Alleyway from _call_Scene_Rat_Patron_Alleyway
    $ pc.lust = 0
    "He chuckles and starts walking towards the exit of the alley, leaving you to catch your breath and straighten your clothes. "
    scene lusterfield_alleyway
    "Once you're able to move again, you follow after him, thinking about just what kind of information he has to offer."
    jump Rat_Patron_Probed_Info

label Rat_Patron_Probed_Info:
    $ cane_dialogues["Rat Patron Info"] = [False, False, False]
    e "So what else did you see that night?"
    "The rat patron glances around warily, leaning his back against the stone wall."
    rat_patron "I saw that odd creature when the sun's almost out — around, I guess, five or six in the morning."
    e "What were you doing there, anyway?"
    "You ask hurriedly, meeting a strange, almost guilty look in his eyes."
    e "What do you mean — huh?"
    rat_patron "I was just... looking around. I slipped up to the counter when the keeper was in the other room. And that's when I saw it."
    rat_patron "Right there, by the fire — this ghost, kneeling as if it were studying the flames. It looked like a shadow, but with these burning red eyes that pierced through the darkness."
    e "Do ghosts in this world even have wings? I thought they just floated around like the one I was used to."
    rat_patron "Nah, not always. This one... its wings fluttered so fast it almost lifted him off the ground when he caught sight of me."
    rat_patron "I bolted before he could reach me. But then I tripped into the side of a chair. I tried to grab something on the counter but my hand got caught in the fire."
    jump Rat_Patron_Probed_Info_Menu

label Rat_Patron_Probed_Info_Menu:
    menu:
        "You nod, thinking of the next question to ask..."
        "Was anyone else there?" if cane_dialogues["Rat Patron Info"][0] != True:
            $ cane_dialogues["Rat Patron Info"][0] = True
            e "The tavern's always full of people, surely someone else would have seen it, right?"
            rat_patron "No, only another group of folks stayed late enough at that time, they all said they didn't see it, even as that bright glow's clear as day."
            rat_patron "When it fled, I even heard a soft rustling, like the turning of old pages."
            rat_patron "But the folks all said they heard nothing at all, only my shout all over the tavern."
            e "Look, if the ghost escaped, I can't think of a way no one saw the glow that you're talking about."
            rat_patron "Not my fault half the tavern are blind in the night. These folks all gathered to eat bread or something, it's like I was the only one drunk in the taven..."
            rat_patron "And you bet I can see better than any one of them."

        "What were you really up to?" if cane_dialogues["Rat Patron Info"][1] != True:
            $ cane_dialogues["Rat Patron Info"][1] = True
            e "I can't help but wonder — you were at the counter for a reason. Were you... trying to take something?"
            "The rat shifts uncomfortably, his ears twitching as he glances away."
            rat_patron "Alright, alright... I'll be straight with you. I was there to snag a bit of stew. I know it sounds bad, but the keeper wasn't there, and I was just a bit hungry."
            e "So you were stealing from the stew?"
            rat_patron "I was about to. But in that moment, when I was sneaking a bowl, I saw the ghost. So I technically didn't steal anything."
            e "Is this why you didn't want to talk about it with Cane?"
            rat_patron "Yes, but not entirely."

        "Where did the ghost go?" if cane_dialogues["Rat Patron Info"][2] != True:
            $ cane_dialogues["Rat Patron Info"][2] = True
            e "After you ran, did you see where it went?"
            "The rat squints, as if recalling a half-forgotten detail."
            rat_patron "I... I noticed a faint, lingering glow disappearing into the shadows. I just can't see clearly, I was already slumping on the ground when it escaped."
            e "So you didn't see it?"
            rat_patron "He didn't get to the seating area, so he either escaped from my eyes, or..."
            rat_patron "He ran downstairs."
            e "That means he's still within the tavern...?"
            rat_patron "Keep this between us, but if it went into that storage room, the keeper would have seen it."
            e "I hadn't been downstairs yet, but is it possible that Cane just didn't happen to bump into the ghost?"
            rat_patron "I don't think so. He came right up with a keg of ale right as the ghost escapes, and the keeper acted like nothing happened."
            e "So... what's your theory?"
            rat_patron "I don't know, maybe the keeper knew about the ghost, maybe he was the ghost all along."
            e "You're sounding like a lunatic now, I know Cane, he's just not some kind of ghost, even if you believe he's a ghost, why did you come back?"
            rat_patron "I'm just bored, I wanted to see if he's an actual ghost!"
    if cane_dialogues["Rat Patron Info"].count(True) == 1:
        jump Rat_Patron_Probed_Info_Menu
    e "So, let me piece this together: That odd, ghostly figure appeared around six in the morning, by the fire."
    e "Its wings glowed and it had those burning eyes. And, whether it was fleeing from you or—"
    "You pause as the rat interjects."
    rat_patron "Yeah, well... I might've been a bit mixed up about everything. But one thing's for sure - it escaped right as it saw me."

    if cane_dialogues["Rat Patron Info"][0] == False:
        e "To the storage room inside the tavern, huh? That might be your only lead."
        rat_patron "Exactly. Look, I know I don't make the best company and maybe I tried to sate my hunger. But believe me, something moved in those shadows, and it slipped away through a hidden door."
    if cane_dialogues["Rat Patron Info"][1] == False:
        e "To the storage room inside the tavern, huh? That might be your only lead."
        rat_patron "Yeah, I know. But you oughta make use of that lead."
        e "So, neither the keeper nor the other patrons saw the ghost? And you were... drunk with beer?"
        rat_patron "I don't like the implication you're hinting at, I saw it with my eyes, and I knew what I saw.."
    if cane_dialogues["Rat Patron Info"][2] == False:
        e "So, you tried to life some stew, got spooked by the ghost, and you're positive that other people didn't see the ghost?"
        rat_patron "More or less my point, that ghost also escaped somewhere inside the tavern... Because I cannot find him anymore."

    e "Thanks for your time. I'll see what I can do with this."
    rat_patron "Do whatever you want with it."
    e "Understood. I'll keep you posted if I need more help."
    rat_patron "Yeah, sure... Now, leave me alone. I've got enough trouble."
    "You part ways with the rat patron, his words echoing in your mind as you head off."
    $ quest45.qComp(_("Return to Cane with the new information"))
    jump main_lusterfield02


label Rat_Patron_Probed_Info_Fail:
    e "Alright, I guess that's all I'll get from you."
    rat_patron "Yeah, now if you'll please excuse me."
    jump Rat_Patron_Dialogue_End

label Rat_Patron_Dialogue_End:
    "The conversation slowly winds down as you watch the rat walk away."
    jump main_lusterfield02


label Cane_Voting_Quest_Report_Rat_Patron:
    e "Cane, I did what you asked for."
    c "Oh? Did ya get the rat?"
    e "I did, he wasn't too keen on talking, but I managed to get some information out of him."
    c "Oh? What'd he say?"
    e "He said he saw a ghost in the tavern by the counter, and that it had wings and burning eyes. It was six in the morning I think."
    c "Yeah, I know. I was there but that rat's just mumbling some weird stuff. What else?"
    e "He said it fled as soon as it saw him."
    if cane_dialogues["Rat Patron Info"][2] == True:
        e "He also mentioned that the ghost might have escaped to the storage room."
        c "Nah... I was just walking out at that time, something like that wouldn't have slipped in when I closed the door right away."
        e "So you didn't see it?"
        c "No, I hadn't seen anything. I' go in and out of the storage room every day, I'd have known if I caught the sight of a ghost."
    if cane_dialogues["Rat Patron Info"][1] == True:
        e "He also mentioned that he was trying to steal some stew from the tavern."
        c "Oh, that rat. I'm not surprised. Ya know, at first I was thinking he's full of lies and he just wanted to get himself off the hook."
        e "And he also said that the ghost's trying to do something with the stew too."
    if cane_dialogues["Rat Patron Info"][0] == True:
        e "And when I asked him about the other patrons, he said they didn't see the ghost either."
        c "Just like I said, that rat's just a drunkard."
        e "But he said he was the only one who was drunk."
        c "Ye, I knew it already, he was just there yapping about nonsense."
    c "But I guess it was a good try, lad. I didn't expect ya to get anything out of that rat."

    $ quest45.status = 3
    e "Maybe he was right? Maybe the ghost's hiding still, in this place."
    e "I mean, he said it fled to the storage room, right?"
    if cane_dialogues["Rat Patron Info"][2] == True:
        c "That door, fine, yer been there already... Not downstairs though, but there's nothing much to look."
    else:
        c "I've checked every place... the only possible spot he could've hidden in..."
        c "The brewery, but I don't think he could've gotten in there, I check that place every day."
    e "But Cane, if the ghost's hiding in the tavern, then why didn't you see it?"
    c "Don't ask me, lad, Do I look like I've got any clues what the hell's going on?"
    "He says as he polishes a mug and leans on the bar."
    c "He's just saying stuff to get ya to believe his made up stories, I tell ya."
    e "Okay, but the details checked out, I think there's still something to it."
    if cane_dialogues["Rat Patron Info"][2] == False:
        menu:
            "The ghost was looking for the stew":
                jump Cane_Voting_Quest_Stew_Route
            "Only the drunk rat saw the ghost":
                jump Cane_Voting_Quest_Beer_Route
    if cane_dialogues["Rat Patron Info"][1] == True:
        jump Cane_Voting_Quest_Stew_Route
    else:
        jump Cane_Voting_Quest_Beer_Route


label Cane_Voting_Quest_Stew_Route:
    $ cane_dialogues["Moth Route"] = "Stew"
    e "Maybe the ghost's trying to do something with the stew too."
    e "I think we should recreate the scene when it first happened, you entering the storage and having the stew ready."
    c "At six in the morning?"
    c "Sounds like a bloody waste of time and coin to me, but... Alright, I'll go along with this."
    "He says with a sigh."
    c "Ya better get ready by then, I'll be waiting with everything else."
    $ quest45.qComp(_("Report to Cane at late night"))
    jump main_nocturnaltrunk

label Cane_Voting_Quest_Beer_Route:
    $ cane_dialogues["Moth Route"] = "Beer"
    e "He said he was drunk, right? What if we drink the beer too and go downstairs...?"
    c "Ya think that beer would help us see the ghost?"
    e "Maybe. I mean, if the ghost's hiding in the tavern, then why didn't you see it?"
    c "Yeah, ya caught me, I was sober... And I did open a new batches of old beer... a week before."
    c "Okay, we'll check the brewery then, but don't get your hopes up."
    e "Should I be drinking the beer... or you?"
    c "Heh, of course it's you, lad. If I'm drunk, ya ain't gonna carry my burly arse upstairs, even if yer life depends on it."
    "You nod, perparing to drink a beer before heading to the storage room."
    $ quest45.qComp(_("Drink a Beer then report to Cane"))
    jump main_nocturnaltrunk

label Cane_Voting_Quest_Stew_Route_Meet:
    scene nocturnaltrunk_night:
        matrixcolor TintMatrix("#434157")
    "You walk into the tavern, the familiar smell of stew wafting through the air as Cane stands behind the bar, polishing a mug."
    show cane normal with dissolve
    c "Oh, you're right on time, lad. Here, I've got the stew ready as usual. How are we gonna recreate the rest of the scene?"
    e "Well, I was thinking maybe you could go down into the cellar brewery and see if anything there seems amiss?"
    "You say as you place your hand on your chin."
    e "Then I can keep watch over the stew, secretly, maybe I'll get to catch the ghost if he's there."
    "He looks at you for a moment before chuckling, and then sets his mug on the counter."
    c "Bah! Fine, fine, I'll do it."
    c "But if nothing happens, then ya gotta owe me a few hours of work, alright?"

    "The tavernkeeper smiles, and you nod."
    e "Deal!"
    show cane at r2 with move
    "As the night goes by, you have the tavern all to yourself as the tavernkeeper is still down in the brewery."
    "You start to feel a bit sleepy and decide to sit on one of the chairs by the bar."
    "The fire crackles with the flames burning in it and you rub your hands together to warm them up."

    "You look towards the door every now and then but nothing seems to happen."
    "As you start to hear the sound of footsteps walking behind the storage room door, you look around but no one seems to come through."

    "You sigh and lean your head back. Slowly you start to drift off to sleep as you listen to the crackling fire."
    scene nocturnaltrunk_night:
        matrixcolor TintMatrix('#101155')
        blur 16
    with dissolve
    pause 0.5
    show mothman:
        matrixcolor TintMatrix("#000")
        xalign -2.0
        linear 0.25 xalign 2.0
    "The last thing you see, was a sihoulette of a pair of antennae fluttering on top of you."
    call Cane_Voting_Quest_Topu_Vision from _call_Cane_Voting_Quest_Topu_Vision

    "As you open your eyes, you find yourself sitting back in the chair by the bar, but this time Cane is standing next to you."
    $ timenow.hour = 9
    scene nocturnaltrunk with dissolve
    show cane normal with dissolve
    c "Oi, what happened? Did ya actually see anything? Where's the ghost?"
    "He asks as he kneels beside your chair. You check your arms again, and now it's back to orange-ish."
    jump Cane_Voting_Combining_Beer_Stew_Route

label Cane_Voting_Quest_Beer_Route_Meet:
    e "C-cane..."
    "You walk up to Cane with tipsy steps, your face blushes a glowing red."
    c "Ye, no doubt yer drunk as hell, now go downstairs... and see if ya can find anything, or any ghosts."
    "You nod dizzily, as Cane leads you to the door."
    c "Now, go on, lad. I'll be waiting here. Shout if you see anything."
    scene black with dissolve
    "You climb down the stairs, your head spinning as you try to keep your balance."
    scene trunk_brewery with dissolve
    "You look around the cellar, the dim light flickering as you walk around."
    "The air is thick with the smell of beer and the sound of barrels creaking fills your ears."
    "As you walk around, you notice a strange shadow moving in the corner of your eye."
    show mothman:
        matrixcolor TintMatrix("#000")
        xalign -2.0
        linear 0.25 xalign 2.0
    e "Hello?"
    "You call out, but the shadow disappears as you turn to look. It seems to be startled, as if surprised by your presence, or acknowledgement."
    "You take a step closer, your heart racing as you try to get a better look."
    scene trunk_brewery:
        blur 8
    with dissolve
    "The only thing you can make out is the pendulous antenna fluttering, it's almost mind-numbing to the point your eyelid feels heavier by the second."
    e "W-wait..."
    scene trunk_brewery:
        blur 32
    with dissolve
    "Slowly your head begins to spinning, you try to lean on the wall to prevent falling over completely, but your world fades away before you'd ever reached the ground."
    scene black with dissolve

    call Cane_Voting_Quest_Topu_Vision from _call_Cane_Voting_Quest_Topu_Vision_1
    "As you open your eyes, you find yourself leaning against the back wall of the brewery, your legs bent and your body hunched over."
    scene trunk_brewery with dissolve
    "You stare at your orange-furred arms, sighing a breath of relief. It was just a dream. Or at least, you thought so."
    show cane normal with dissolve
    c "Ya alright there, laddie?"

    "Cane is standing next to you, patting your head with a grin."
    c "I figured ya gonna need help, so I went down regardless and saw yer slacking off here."
    "He says as he looks around the brewery, before leading you up to the bar."

    jump Cane_Voting_Combining_Beer_Stew_Route

label Cane_Voting_Combining_Beer_Stew_Route:
    e "I saw Topu..."
    "You say as you rub your temples."
    e "Or rather, I was him. And we were here in this brewery..."
    "The bat's expression goes from amusement to confusion in a blink of an eye."
    with vpunch
    c "That's impossible... Ya can't just have visions like that, it ain't making no sense..."
    e "I don't know how, but... I saw what happened when you first met him? Maybe it's the ghost."
    e "He said he saw a ghost, and then you told him it wasn't real..."
    c "Well... that part's true enough."
    c "That was the only time he mentioned a ghost or some sort, so I figured he just made the whole thing up."
    "You explain to Cane your experience of having the vision of Topu in the cellar. Cane listens intently, a look of shock on his face."

    menu:
        c "But who is giving you these... visions, lad?"
        "The Ghost":
            e "I think it's the ghost's doing. I mean, Topu has seen him before."
            c "Ya think there's been a ghost in my bloody cellar this whole time?"
            e "Maybe, and I think the ghost's trying to tell us something. Maybe there's a way we can communicate with him..."
            e "I mean, why else did he let me see what happened that night."
            e "Cane, you believe me, right?"
            c "How else can I not, lad? What ya told me was bloody vivid, just like when I first saw him..."
        "The Server":
            e "What if Topu came back?"
            c "Oh, I wished... I just missed seeing that lad around here... he was a good worker, always helped me out with the brewing and cleaning up the place."
            c "I don't wanna believe he betrayed the village, lad. I wanted to say he's not that kind of people, but then I realised I never really knew him."
            c "But if he came back, then why didn't he just tell me himself? What troubles has he gotten himself into now..."
    "He says as he rests his chin in his palm."
    c "Now, what was it you wanted from me again, lad? I'm getting tired just thinking about it..."
    e "Right! I guess we go down again and see if the ghost's still there."
    with vpunch
    "The bat suddenly perks up."
    c "Oh! Maybe that's why we couldn't see the bloody thing before!"
    show cane normal at flip
    show cane normal at r1 with move
    pause 0.5
    show cane normal at flipback
    show cane normal at l1 with move
    c "Topu took a swirl at my barrel of beer, remember?"
    e "And you said it's going to be expensive when he drank that."
    c "Aye, I lied, I just wanted to get'em to feel bad, maybe pay for the damage too. It's just some old beer I had lying around, tasted nasty as hell..."
    "He says as he looks around for something."
    c "Hold on, let me grab some of that stuff..."

    show cane normal at l2 with move
    pause 2.0
    show cane normal at flip
    show cane normal at c1 with move
    show cane normal at flipback
    "He disappears behind the bar for a few moments before coming back with a piece of old paper."
    c "That lad kept buggering me to teach him to make beer. He never told me why, but I sorta figured out someone taught him to drink those beer."
    "He says as he hands it over to you. The edge is already yellowed, the ink lost to the air."
    c "I thought he was trying to hide something from me- those scumbags taught m' lad drinking, all behind m' back. I just couldn't stand 'em, but that lad begged me not to kick 'em out."
    c "So I gave in, I taught him to make beer, but he insisted that there's one recipe he's most excited about, one that I must teach him to make."
    "Hesitantly, He unfolds the paper and places it in your palm."
    c "It's the first beer that he got in my cellar, same one as ya saw in the vision."
    e "T-that? is it the same beer you sold to that patron?"
    with vpunch
    c "Aye, that's right. It's his beer, I've kept it in the cellar for a while... but lately I've been thinking, I've gotta move on, ya know."
    c "So I sold 'em. Bad news is, the last of that batch to that pesky patron that ya were seeing, so... ya gotta make a new one, but I've got a new method for ya!"
    c "Just follow the recipe here and yer gonna make that beer in no time."
    e "Should I make this beer, and then drink it?"
    c "If my theory's right, of course! Just make it, drink that up and come back to me. Ya don't even gotta go through all the brewing process, I've gotcha covered."
    $ quest45.status = 4
    jump Cane_Voting_Quest_Draft_Beer_Menu

label Cane_Voting_Quest_Draft_Beer_Menu:

    menu:
        c "Ya wanna help? It's not that hard, just follow the recipe and ya'll be fine."
        "Get going to collect the material":
            "You nod, looking at the recipe in your hand."
            e "Okay, I'll get going then. I think I know where to find the ingredients."
            c "Good, good. I know ya can do it, lad."
            $ quest45.status = 5
            $ discoveredrecipe.append(topusbeerrecipe)
            $ discoveredrecipe.append(topusgruitrecipe)
            $ quest45.qComp(_("Craft and drink Topu's Beer, then report to Cane"))
            jump main_nocturnaltrunk
        "I'll think about it later":
            e "Cane, I think I still have something else to do before drinking it..."
            c "What'cha gotta do, checking off your bucket list? Nah, this beer's not gonna kill you, lad."
            e "Y-yeah about that... I'll be back later."
            "The keeper shrugs."
            c "Okay, Okay. I was just joking, lad. Come back when yer' ready."
            jump main_nocturnaltrunk

label Cane_Voting_Quest_Craft_Beer_Ask:
    e "Cane, what should I do again?"
    if LookForItem("Topus Beer", inventory):
        c "Aye, aye! Remember the recipe I gave ya?"
        c "W-wait a second 'ere, you've got the beer! Great, that means my recipe's alright."
        c "Now, go drink whatever ya got."
    else:
        c "Aye, aye! Remember the recipe I gave ya? Go find 'em ingredients and craft the beer."
        c "It doesn't take that much for a normal brewing process, but considering we'd only need one mug full of beer. That much herbs gotta be enough."
        "You nod, as you look at the recipe in your hand."
        e "What's... gruit's and hops?"
        c "The Gruits just a mix of herbs, Horehounds' in the goat's place, golden berries probably in the lagoon, and Mugwort I've seen 'em on the side of the road outside of the farms."
        c "Hops' in the grove near the farm."
        c "We never put gruits with hops ever, they're both... too bitter for the folks around 'ere."
        c "But I've tried a few times, they usually were not sold to my dear patrons for a reason."
        "Cane trails off as he tries to remember something."
        c "Now, put both into yer beer. And lo and behold, ya made it, and fair warning, these nasty things taste bitter as swamp water."
        c "Ahh... and somehow that ol' lad's sure had a taste for it... Just drink it when ya ready, and report to me, I'll open the cellar door for ya."
    "You nod."
    jump main_nocturnaltrunk

label Cane_Voting_Quest_Draft_Beer_Drinking:
    e "C-cane... I've drunk the beer."
    e "I-Is it supposed to do this to me? I'm starting to feel really drowsy..."
    c "Bloody hell... Already?"
    "He says as he sets his mugs back behind the bar."
    c "I guess I shoulda known better than to let ya have some of that stuff. Go on down to the cellar, I'll be right behind ya."
    "You nod, as you make your way down the steps, you can hear Cane muttering under his breath."
    scene trunk_brewery with dissolve
    "You sit down on one of the stools in the brewery, and your head starts spinning even more as you try to focus your vision."
    "After a few minutes, you begin to see things moving around in the shadows, and you start to feel like someone's watching you."
    "You ask out loud as you look around the dark room."
    e "Cane? Are you there?"
    with vpunch
    c "Hold on, lad, I'm comin'!"
    "The bat calls from upstairs."
    c "The door's a little bit jammed, give me a minute!"
    show mothman at l2
    show mothman:
        matrixcolor TintMatrix('#2b374d')
        blur 32
    show mothman at l1 with move
    "You nod and turn back towards the shadows, your vision suddenly becomes clearer, and the shadow slowly emerges into a perching figure behind the barrels."
    "It's tall, with long limbs and covered in thick fur."
    show mothman:
        linear 0.5 blur 16 matrixcolor TintMatrix('#4b4e79')
    show mothman at l1 with move
    e "Cane, come quick! I found him!"
    with vpunch
    c "What? Found who? Get yer arse outta there now!"
    scene black
    scene trunk_brewery
    "But before you can react, the figure moves. And so does everything else in the brewery."
    with vpunch
    scene trunk_brewery:
        linear 0.1 xpos -0.08 ypos -0.05
        linear 0.08 xpos -0.01 ypos -0.02
        linear 0.11 xpos -0.1 ypos 0
        linear 0.1 xpos -0.02 ypos -0.01
        linear 0.12 xpos -0.06 ypos -0.03
        linear 0.1 xpos -0.07 ypos -0.03
        linear 0.11 xpos -0.02 ypos -0.04
        linear 0.07 xpos -0.05 ypos -0.05
        linear 0.09 xpos -0.01 ypos -0.02
        linear 0.1 xpos 0 ypos -0.06
        repeat
    "You feel as if you've been transported from Puro again. Your world is blinking itself out of existence."
    "Barrels and boxes fly across the room as the figure suddenly appears in front of you."
    "It's not a ghost at all. It's a mothman, a huge creature with wings like a moth, standing on two legs like a man."
    "And it's looking directly at you with its huge, glowing eyes. You realize that you have seen it before, in the back of your mind inside Topu's memory."
    e "What... what are you?"
    show mothman:
        linear 0.5 blur 0 matrixcolor TintMatrix('#888888')
    "You ask, your voice coming out as a whimper."
    "The moth-creature steps closer to you, its wings rustling as it moves. Its body is covered in thick fur, like a bat's would be, but it stands on two feet like everyone else."
    "It tilts its head to the side, regarding you curiously. Suddenly, it reaches out a hand towards you, its claws glinting in the light of the brewery."
    show mothman:
        easein 0.5 zoom 1.5
    "You shiver involuntarily as it touches your face, its touch cool against your skin. It seems gentle enough though, almost... tender?"
    "Slowly, it pulls back its hand and points towards a corner of the room where a single barrel sits, half-full of dark liquid. Its other hand gestures towards you, then towards itself. It wants you to follow it?"
    show mothman:
        easeout 0.5 zoom 1.0
    "You nod slowly, trying not to startle the creature."
    e "Okay... I'll come with you."
    show mothman at flip
    show mothman at r1 with move
    "As you approach the barrel, the creature carefully pushes it aside, revealing a patch of damp earth beneath that you did not notice before. It points at the ground, then looks at you expectantly."
    show trunk_brewery_mark with dissolve
    "You kneel down and try to touch the spot where it's pointing, the ground feels cold to the touch, and it seems to be glowing in bright blue."
    "You look back at the barrel, the pieces of wood facing the wall is almost drenched in this blue glowy substance."
    e "Where does this come from?"

    "You ask as you stand up again and look around the cellar."
    e "Is it the beer that's making me see these things?"
    show mothman at flipback
    show mothman at c1 with move
    "The creature nods, then points towards the wooden floor, his feet are bound to the same blue glow, tethered beneath the damp dirt under the barrel."
    e "Does that mean, you're trapped here..."
    "You say quietly, realizing what had happened."
    e "But why? What happened here?"
    "You ask, looking around the brewery."
    "The creature sighs with his mandibles, or at least, that's what it sounds like."
    "Then it turns to face you directly, its eyes glowing brighter than before. He extends his arms, then places his hands on either side of your head."
    with vpunch

    with vpunch

    with flash
    scene black with dissolve
    "You feel a sharp pain shoot through your skull, but it's quickly replaced by an overwhelming feeling of peace and warmth."
    scene trunk_brewery:
        matrixcolor TintMatrix('#2b374d')
    show trunk_brewery_bottle
    "When you open your eyes again, everything looks the same, but somehow, everything looks different too. Colors seem brighter, and the air itself feels... thicker."
    with dissolve
    yu "I'm so thirsty..."
    "You whisper, feeling yourself stepping down the stairs. You can still hear loud chatters in the distance."
    yu "Why am I so thirsty?"
    "A voice calls in your head, familiar yet strange. It sounds like someone you know, yet not quite right."
    yu "Topu? Am I... dreaming of his memory again?"
    "You ask softly in your mind, but the other part of your mind doesn't sense your presence."
    "The other you limp towards a barrel, filled with a strange liquid, light yellow in color."
    "A pungent smell permeates from the barrel."
    "As soon as you touch the liquid, you start to feel a strong urge to drink it. Your body moves without your control, and before you know it, you've already gotten incredibly drunk."
    "Your vision blurs, and you can barely keep your balance on your feet."
    yu "That was so good... I'm so full..."
    "You giggle, your mind becoming fuzzy. You look across the room, and suddenly, your legs give out beneath you, causing you to topple over onto the beer shelves."
    hide trunk_brewery_bottle
    "A glass bottle breaks under your weight, and a streak of blue glow emerges from its shards as you slump onto the ground."
    my "What was that?"
    "A voice from upstairs shout, the tavern quieten as if they are trying to look for the source of the commotion."
    "The liquid inside the bottle starts to leak out, forming a small pool of blue glow that slowly reaches your paws."
    "Your half-closed eyes watches the glowing liquid as it seeps into your fur, your body begins to tremble slightly."
    "Then, a pair of antenna suddenly appears above you, blocking your view of the ceiling."
    yu "Huh?"
    show mothman:
        xalign 0.5 yalign -2.0
        easeout 1.0 yalign 0.5
    "You look up to see a giant bug perching directly above you, its wings rustling as it lands onto the barrels."
    show mothman:
        easeout 1 yalign 0.0
    "The creature tilts its head to the side, regarding you curiously as its eyes glow brighter than before."

    "It notices the glass shard and the blue glow on your paw."
    "The bug's eyes widen as it realizes what has happened, and it stands up straight on its hind legs, looking panicked."
    show mothman at flip
    my "What's going on down there?"
    "The same voice shouts from upstairs as the creature flies towards the stairs."
    "You struggle to move your body, feeling like your limbs have turned to lead. But you can feel the mothman's panic resonating through the ground, the blue glow following him like a trail."
    show mothman at r2 with move
    "When the mothman runs up, you can hear the sound of footsteps begins to muffle..."
    scene black with dissolve
    c "[e]! What the hell's going on down there?"
    scene trunk_brewery with dissolve

    show mothman at c1 with dissolve
    pause 1.5
    show mothman at flip
    show mothman at r1 with move
    pause 0.5
    show cane normal at l2
    show cane at l1 with move

    "Cane shouts as he stands over you, while the mothman crouching in the corner."
    "The weird echo in your mind has stopped, everything is back to normal, as if nothing happened at all."
    "You point at the mothman, trying to show Cane the ghost that he saw."
    e "I found it, Cane."
    "You say weakly as you try to get up from the floor."
    e "The ghost's there. It's a moth, I guess."
    show cane at flip
    pause 0.25
    show cane at flipback
    c "What? Where?"
    "He asks as he looks around the cellar."
    with vpunch
    c "Bloody hell... Oh, for fuck's sake..."
    "Cane comes to as sudden realisation as he looks at you with concern, kneeling beside you."
    c "Whats it want from ya, lad? Tell me if he's coming close to me."
    e "No, no, it's not a ghost... It's just... trapped here. I think Topu unleashed it from that broken bottle."
    show mothman at flip
    "You say as you look towards the ghost, who seems to be glowing a little brighter than before."
    c "That bottle? I thought it was just an old beer, it was there since I'd taken the tavern over..."
    c "If Topu got it out, what's it doing here?"
    e "I think the ghost wants me to help it escape."
    show cane at flip
    "Cane frowns and stands up, crossing his arms. He tries to look in the direction of the mothman, but he was quite off."
    c "Nah, lad, you can't be trustin' that bloody thing! Who knows what kinda trouble it could cause if it gets outta here?"
    "You nod slowly."
    e "Maybe... But I don't think it's dangerous..."
    "You say as you stand up."
    e "And I don't think it can hurt anyone either... It didn't try to hurt me."
    c "Hmm..."
    show cane at flipback
    c "Alright, alright, I'll think on it. Oh, we ain't never gonna get any work done if we keep chasin' after ghost all day long!"
    "He sighs as he looks at the corner again."
    c "Lad, if it's so harmless, can ya ask this... ghost to stop haunting my tavern?"
    c "Dangerous or not, I got people comin' in here thinkin' my place is some sort of a bloody haunted house!"
    show mothman at flipback
    "You smile weakly, the mothman seem to understand Cane's request, it nods, but then points at his stomach, and then pointing towards the door upstairs."
    e "Uh... Cane."
    e "I think he wants me to feed him something..."
    "You say slowly as the mothman repeats his gesture."
    e "Maybe... maybe he'll stay in the cellar if he's got food?"
    "Cane raises an eyebrow."
    with vpunch
    c "Feed the ghost? Lad, you gotta be kidding me... Does the ghost even die if we starve 'em alive?"
    "You shake your head, realizing that the mothman had just been hungry, all along."
    e "No, no, he's not a ghost, and I think it's been just eating from your stew anyway."
    "You say as you look around the brewery."
    e "And that's when that patron saw him."
    "The bat keeper sighs and rubs his temples."
    c "Alright, alright... fine, lad."
    show cane at c1 with dissolve
    c "I'll bring him some stews, ya like that big pot of stew, ghost?"
    show mothman at flip
    "The mothman nods slowly."
    e "Thank you so much, Cane! This is perfect!"
    "Cane smiles for a moment, before gesturing you to follow him upstairs."
    c "Come on lad, let's get ya something to sober ya up."
    "He places his arm around your shoulder as he leads you out of the brewery, giving the mothman another cautious glance."
    scene nocturnaltrunk with dissolve
    show cane normal at c1 with dissolve
    c "Don't go tellin' nobody about this ghost business, alright?"
    "He says as he pats your head."
    c "It ain't gonna do us any good, and I don't wanna scare off my customers!"
    "You nod in agreement as you make your way towards the bar, still feeling a little light-headed from the beer."
    "Cane sets you up on one of the chairs and hands you a cup of water."
    c "That ghost's been watching me down there... all along."
    "He says as he sits down next to you."
    c "I always knew it was somethin', but I just couldn't figure out what..."
    with vpunch
    c "Bloody hell, is that why he'd always get drunk from that barrel? To see that bloody thing?"
    "You nod slowly."
    e "Yeah... And... I think he was trying to help it escape too."
    "Cane frowns and looks towards the corner where the mothman is hiding."
    c "He could've told me, ya know. We coulda worked together to fix this mess."
    "You shake your head."
    e "No, no, he didn't want to trouble you."
    e "He thought you were mad at him for drinking already. But he really cared about you, Cane."
    "The bat keeper falls silent, looking down at his hands as he rests them on the bar counter."
    with vpunch
    c "I was mad! He wasn't like that before, yer know?"
    c "If I didn't want him to drink I'd have thrown away that barrel. I let him drink that beer, do anything he wanted, but that just made him hide away from me."
    c "And I... I was younger, lad. I didn't have much patience for him as I do now."
    "He says as he looks at you, smiling weakly."
    c "I didn't know how to talk to that kid, I wanted to apologize to him but other words just slipped out of my mouth..."
    "Cane sighs and shakes his head."
    c "It's not easy running a tavern, yer know? And it's even harder when ya gotta take care of a bratty lad like him."
    c "But still... I'd have done anything to make sure he's alright, even if I didn't... appear so."
    "He stands up from his stool and pats your shoulder."
    c "Come on then, get some rest. Thanks for helping me figure this out, lad."
    c "We'll have to keep an eye on that moth ghost later, but I think we can manage, ain't cha think?"
    c "Here's a bit of compensation."
    call level_up_check (800, 800, 300, 300) from _call_level_up_check_10
    msg "You also received a level up point."
    c "But, I oughta mention... I was going to vote for the goats anyway, so I'm not sure if this helped or not, if ya helped for the vote."
    e "Oh, I see..."
    e "But no, Cane... I didn't do it for the vote, I just wanted to help you and Topu."
    "Cane smiles, putting your hands in his palms."
    c "Speaking of, that rat looks like he's leavin' after the vote, ya gotta check to see if he's got any vote left."
    e "Okay, I'll go check on him."
    $ QuestFinish(quest45)

    jump main_nocturnaltrunk

label Cane_Voting_Quest_Topu_Vision:

    scene black with dissolve

    pause 3

    my "...and then someone's kid just got drunk in my cellar... bah, I can't believe it."
    scene trunk_brewery:
        matrixcolor TintMatrix('#383633')
        blur 32
    with dissolve
    scene black with dissolve
    "You hear a gruff voice as your eyes flutter open. Everything seems so blurry and you can barely make out anything in front of you."
    scene trunk_brewery:
        matrixcolor TintMatrix('#686056')
        blur 16
    with dissolve
    scene black with dissolve
    "You raise your arm, and notice that your body is covered in gray fur, donning some loosely ragged clothes."
    scene trunk_brewery:
        matrixcolor TintMatrix('#322d50')
    with dissolve
    yu "Hnn... Wh-What?"
    "You say as you try to get a clear look at your surroundings. As your vision finally clears, you find yourself sitting on a chair in the brewery, with a bat standing over you."
    tavernkeeper "Oi, good, yer awake!"
    show cane normal:
        matrixcolor TintMatrix('#736a92')
        blur 8
    with dissolve
    "He says as he walks over to you, putting down a keg of freshly pour beer."
    tavernkeeper "I thought you fell down here and hit your head or somethin'! What's going on?"
    yu "I-... I saw a ghost. It... It was here, in the cellar..."
    show cane normal at flip
    pause 0.25
    show cane normal at flipback
    "He looks at you with a confused expression before laughing."
    with vpunch
    tavernkeeper "Ghost? In MY tavern?! That's bloody ridiculous! Ya musta had some awful nightmare is all!"
    "The bat looks over at your side, where a half-full barrel of beer sits on the floor beside you."
    tavernkeeper "You weren't drinking from that were ya?"
    yu "N-No sir, I wasn- I didn't mean to drink any of that."
    "You say as you rub your eyes."
    yu "I just... I don't know how I got here... I was... just so thirsty. And something's here..."
    tavernkeeper "Oi, what about this one ya slammed into the ground?"
    "He asks as he points to the broken bottle."
    tavernkeeper "That's the most expensive one- ya can't pay for that-"
    yu "I didn't mean to! I just... it's the g-ghost that's doing this, you have to catch it."
    "You stutter nervously, the voice comes out rougher than anything you've uttered."
    tavernkeeper "Awful lotta nonsense ya been talkin', ya lil thieving brat."
    tavernkeeper "Ya broke into my brewery, drank my precious beer, broke my bottle and then passed out. That's a lotta trouble ya caused just for a bloody ghost story!"
    yu "But... it was real..."
    "You say as you stand up from the chair."
    yu "I saw it..."
    tavernkeeper "Don't go bein' ridiculous, there ain't no such thing as ghosts."
    tavernkeeper "Now get yer arse out of my place, I gotta get some cleaning done before the regulars come in."
    "You nod and apologize again. As you make your way towards the exit, you look back at the keeper who looks rather annoyed with you."
    yu "S-Sorry sir..."
    "You say as you bow your head, the bat keeper stops, and then he turns to you."
    tavernkeeper "Lil brat, where yer house? I ain't see yer face 'ere before."
    "You freeze in place as he comes near you."
    yu "I don't know... I was looking for a place to stay..."
    show cane normal at flip
    show cane normal at r1 with move
    "He frowns and crosses his arms."
    tavernkeeper "So you're just one of those beggars that wandered into my place? Well, I ain't got no handouts to give ya, alright?"
    yu "I'm sorry..."
    tavernkeeper "But, where yer heading?"
    yu "I've nowhere else to go... sir. I'll work for you if you can just give me a place to sleep."
    "He sighs and runs a hand through his furry hair."
    show cane normal at flipback
    tavernkeeper "Bah... Alright then, you can stay the night. Look, I've got no free room for ya, you gotta sleep 'ere or something."
    tavernkeeper "Tomorrow I'll have ya working yer arse all day long to pay back for that beer, alright?"
    with vpunch
    "You nod enthusiastically, struggling to hide your smile."
    yu "Yes sir! Thank you so much!"
    "And the bat waves his hand at you."
    tavernkeeper "I've never seen someone so keen on sleeping on the floor..."
    "You smile widely as you make your way upstairs to the storage room, the keeper calls after you."
    tavernkeeper "Hey, brat, what's yer name anyway?"
    yu "Topu, sir. I'm Topu."
    show cane normal:
        matrixcolor TintMatrix('#7e7b8f')
    with dissolve
    tavernkeeper "Well then, Topu, I expect you to be up early for work. Yer lucky I ain't kicked yer arse outta here already!"
    tavernkeeper "But if ya got any more of those ghost stories for me patrons, I'll have ya thrown out of here myself, got it?"
    yu "Yes sir, I understand."
    "You turn around and see a big rug drapes over the keeper's hands."
    yu "What is it?"
    show cane normal at l1 with move
    "You ask as you approach him, and the bat frowns."
    tavernkeeper "Yer bed."
    "He says as he drops the rug and a sack of flour on the floor."
    tavernkeeper "Now go on, ya look half dead on yer feet. Get some rest 'ere, and I'll wake ya up when it's time for work."
    with vpunch
    yu "Thank you so much, Sir! I won't let you down!"
    "You say as you bow deeply to the bat, and he waves his hand at you dismissively."
    tavernkeeper "Yeah, yeah, don't call me sir, it's Cane."
    show cane normal at l2 with move
    "He mumbles as he walks away, leaving you alone in the storage room with your new rug. You set it down on the floor and lay down on it, closing your eyes. As sleep takes you, you hear Cane muttering to himself."
    c "Bloody hell, what did I get myself into..."
    scene trunk_brewery:
        linear 0.5 blur 24
    pause 0.25
    scene black with dissolve
    "His speech blurs as you drift off into a deep sleep."
    return

label Rat_Patron_After_Probing:
    $ cane_dialogues["Rat Patron Leave"] = True
    e "Hey there."
    "You find the rat patron sitting on the tavern table again, "
    rat_patron "Oh, it's you again. What do you want? I already told you everything I know."
    if quest45.status == True:
        e "I'm just here to tell you that you were right! There's something in the cellar, I saw it myself!"
        rat_patron "Oh, really? So you finally saw it?"
        e "Yeah, I did. It was just like what you said."
        rat_patron "Ah! So you finally believe me, huh? I knew it all along."
        e "It turns out that the ghost's a moth, and you drank the beer that makes you see the moth."
        rat_patron "Is that so? That explains why their beer looked so... dark. I thought the keep changed his recipe or something."
        e "Yeah, Cane didn't know about it either. The moth just had the same idea as you when you went for the stew."
        "The rat smiles awkwardly as he looks over at the cellar door."
        rat_patron "Well, thanks, server. At least I don't have to worry about the ghost messing around this place now."
        rat_patron "If there's anything you need, ask away. I'll leave Lusterfield after the vote's finished."
        menu:
            "Ask him to vote for the goat":
                e "Oh the voting day, can you vote for the goat?"
                $ vote_choice[3] = 1
            "Ask him to vote against the goat":
                e "Oh the voting day, can you vote against the goat?"
                $ vote_choice[3] = -1
            "Nothing":
                e "Well, I don't need anything else for now, thanks again."
                rat_patron "Alright, server."
                jump main_nocturnaltrunk
        rat_patron "Ah, you've got the right guy, server. It's a wonder there's no such laws as vote manipulation in Lusterfield."
        e "Is that a yes?"
        rat_patron "Sure, I wasn't going to vote anyway, consider it my gratitute for your help."
        "You nod, as the rat begins to take his leave."
        rat_patron "Oh, by the way, server, Cane probably doesn't remember me, but I was there when Topu took a gulp at my beer."
        rat_patron "The boy was just a bit lost, you know? He told me a lot of things, things that I didn't care at the time."
        rat_patron "But, one thing I never understood was why he started drinking that night..."
        e "Huh?"
        pause 0.5
        "The rat turns away, and steps off the tavern without another word."
        "You look at the door, wondering what he meant by that."
    elif quest45.status > 3:
        e "I think you were right... I think I saw a ghost after following your trails."
        rat_patron "Really? What's it like then?"
        e "Uhm... I couldn't really see anything, it was a shadow to me, but I've made a really weird dream."
        rat_patron "Yeah, I've seen shadows and I've made nightmares plenty, come back when you've got some better experience, server."
    else:
        e "Oh, okay. I'll report to Cane now..."
        rat_patron "Shoo shoo."
    jump main_nocturnaltrunk


label Rahim_Vote_Day_After:
    "As you enter his house, you find Rahim sitting alone at the working station, just as usual."
    show rahim normal with dissolve
    e "Rahim!"
    if rahim_late_vote:
        r "What's it that you want."
        e "I'm sorry I missed the vote the other day, Rahim, how did the village vote go?"
        r "Normal. Have you at least done the courtesy of reading the vote result?"
        e "I did."
    else:

        r "[e], good to see you here."
        e "I'm just here to check in, after that huge village vote we just held."
        r "Oh yes, vote, everyone else's talking about the vote like it's some kind of big deal."
        r "I spent the whole week preparing for the votes. Every single second I spent thinking about the votes, I really don't need one more person to ask me about it."
        e "Oops, uh. I'm sorry."
        r "It's fine, I'm just... tired. It's been a long time since I've had to deal with this."
        r "I don't even know why people looked up to me in the first place, I was not the mayor, I didn't know how to run the village."
        e "Maybe because you have a kind heart and tender soul?"
        "Rahim hisses, frowning at your flattering portrayal."
        r "Regardless of the results, I shall take my role more seriously from now onwards."
        e "That's great, I'm sure Lusterfield will flourish in your hands."
        r "Speaking of, I didn't see you in the crowds during the announcement, [e], did you leave early?"
        e "Uh, I was there with Seb."

    if vote_result < 0:
        r "Good, now you know that we are not ever going to ally up with the goats. Never."
        if vote_choice[0] == 1:
            e "Is it really out of the question? Maybe somewhere down the line you might need an ally."
            r "I stand by the decision of my people, for the foreseeable future, you won't see the goat's banner anywhere near our village."
            r "The vote serves its purpose."
        if vote_choice[0] == -1:
            e "I see, maybe it's best for both sides, considering the ancient history you two had."
            r "I am not so certain, it... it affects the two of us nonetheless, I hope it's the better decision."
        "The bull looks outside the windows, you catch a glimpse of reflections in his eyes ever so slightly."
        r "There's something I need you to do, rather related."
        r "I suppose it is time. With or without the goats, we'll need to prepare for the worst."
        r "As much as I want to return to my sewing work. The village need a leader."
        e "What do you need of me, Rahim?"
        r "Can you go ask Sebas to come here, we need to have a talk."
        "You nod."
        $ QuestBegin(quest43)
        $ quest43.status = 0.5
        $ quest43.qProgress(_("Ask Sebas to come to Rahim's House"))
    else:
        r "Okay, good. Just as I reminded you, it's not what I'd hoped for, but I'll do whatever my people need."
        if vote_choice[0] == 1:
            e "I'm glad, I'm sure the people from both sides are going to get along very well."
            r "Mayhaps. The people will."
        if vote_choice[0] == -1:
            e "I'm not sure allying up with the goats was the best choice, afterall, it hasn't been long after what happened."
            r "I was there when it happened, rest assured, I won't regret a decision made by my people."
        "The bull looks outside the windows, you catch a glimpse of reflections in his eyes ever so slightly."
        r "There's something I need you to do, rather related."
        e "What do you need of me, Rahim?"
        "Rahim turns away, taking out a letter from the shelves. He stares down, holding onto the letter with two hands before looking back at you."
        r "Give this to Furkan, steadfastly."
        r "If he is as earnest as he said, it should be easy for us to sign an alliance pact and discuss our future."
        e "I see."
        r "Now, you should be going. We have more to discuss later."
        "You nod, quickly taking the letter from his hand."
        $ addItem("Letter of Alliance", inventory, 1)
        $ QuestBegin(quest42)
        $ quest42.qProgress(_("Take the letter to Furkan"))
    jump main_rahimshop

label Sebas_Ask_Mayor_Rahim_Talk:
    e "Hey, Sebas. Rahim wants to talk to you."
    show sebas smug
    s "Oh, really? He could've just come here himself, you know. The shop's as empty as my own stomach."
    "Sebas chuckles, as he leans back on the counter."
    s "Speaking of, I can really use a snack right now. Probably a beer... definitely a beer."
    e "I'm sure Rahim has something important to say, come on!"
    show sebas shocked
    "You grabs Sebas by the arm, pulling him out of the shop."
    s "Okay, okay. I'm coming, roomie."
    "The lion clumsily follows you out of the shop, as you both head towards Rahim's house."
    scene black with dissolve
    "You quickly knock on Rahim's door. He opens it, revealing a slightly annoyed expression."
    r "Anyone else with you two?"
    e "No, just us."
    s "Hey, Rahim. What's up?"
    r "I need to talk to you two about something important."
    "Rahim gestures for you both to enter, as he closes the door behind you."
    scene rahims_house with dissolve
    show rahim normal at r1
    show sebas normal at l1
    r "What I need to talk about is not for the ears of the village, or anyone else you know."
    s "Okay... is it something about my stash of rocks?"
    "Rahim raises an eyebrow, as he looks at you both."
    s "I mean, the one at your house looked really beautiful, I thought you did't notice it at all."
    "You nudge at Sebas, who is now looking at you with a confused expression."
    r "What are you talking about?"
    r "No, I want to talk about Lusterfield, now that the vote is over."
    e "I thought you said the village will remain the same?"
    r "Yes, but that doesn't mean my duty is over."
    r "We need to go to the Mayor's Longhouse, the old one next to the tavern there."
    s "Oh, I see. What do you need us for?"
    r "You're just tagging along, Sebas. I am talking to [e] here."
    "Sebas shrugs, as he leans back on the wall."
    s "Okay, okay. I get it. I'm just plucked out of my shop to witness the great Rahim do his own thing again."
    "Rahim rolls his eyes."
    r "Are you coming with us or not?"
    s "Yes, Rahim. I'll do anything for you if you ask."
    "Sebas smirks. As Rahim turns back to you."
    menu:
        r "Shall we go now?"
        "Yes":
            e "Okay, let's go then."
            s "Wait, wait. I need to grab my things first."
        "Maybe Later":
            e "Uh, maybe later. I need to do something first."
    "Rahim looks at you two with a disappointed expression, as he crosses his arms."
    r "Okay, but don't take too long. I need to get this done as soon as possible."
    $ quest43.status = 2
    $ quest43.qComp(_("Meet Sebas and Rahim again at Lusterfield's longhouse."))
    jump main_rahimshop

label Furkan_Receive_Pact:
    e "Chief Furkan, guess what happened back in Lusterfield?"
    f "What can it be? You seem to be very excited, [e]. Hmm..."
    f "Let me guess, Rahim held a village-wide vote, and the folks finally decided to ally with us?"
    e "Hey, that's no fun. You knew it already. Thought I could somehow surprise you."
    f "It was merely a wild guess. Did I guess right, [e]?"
    e "Y-yes, okay, but that's not even a guess."
    f "It was a joke, [e]. Of course I knew, words travels faster than a courier."
    if quest38.status != False:
        f "Besides, my fellows told me some Lusterfolks were trying to restore the bridge."
        if quest38.status:
            f "According to them, they saw a handsome looking horned one trodding through water like it's nothing."
    e "Uh... yeah."
    f "So, if Rahim needed me, I will ensure it will not be a one-sided conversation."
    e "Yes, you got it right, Furkan. I have got something for you right here."
    "Furkan nods as you hand the letter to him. He flicks open the seal naturally, before unfolding the paper inside."
    f "'{i}Furkan, Chief of the Goat Tribe,{/i}'"
    "Naturally, he reads the rest of letter silently, a sense of bewilderment can be seen in his widened eyes."
    "The ram quickly skims through the page, before he sneaks a glance at you."
    f "Have you read the letter?"
    e "No, chief. I received it from Rahim after it's sealed off."
    "Furkan raises his brows, your glances meet briefly."
    f "He wishes to meet me in Haskell's hut, with you taking part as the conciliator."
    f "I appreciate the gesture Rahim has bestowed, but tell him I will bring my general along, lest anything happens."
    e "Just to assure, I don't think Rahim will do anything you're thinking..."
    f "I remember the last time we talked, it did not end too pleasantly, so it is fair that Kari shall escort me much the same as you escort Rahim."
    e "Okay. I will let Rahim know..."
    "Furkan smiles."
    "For a man who was publicly humiliated on the streets of Lusterfield, the ram is surprisingly composed as he hears about meeting the abuser."
    e "Furkan, do you not worry about anything at all? How could you keep so calm all the time?"
    f "Oh, I worry. I worry a lot. I worried when the sun hides, worried when a bleat is heard. I worried if my father is here to see it all."
    f "Duty has left me weary, left me a husk of my own self, yet it was the same thing that kept me afloat in the ebbing tides."
    e "It must be tiresome to rule alone, but I guess Kari is here to help."
    f "I feel more alone with him by my side. He is a loyal deer, but sometimes I wonder if I am the one who's dragging him down."
    f "I am not sure if I am the right chief for the tribe, but I am the only one left with our name."
    e "You are doing a great job, Furkan. I am sure your people are proud of you."
    "Furkan chuckles, as he folds the letter back into his pocket."
    "He stands up, his eyes fixed on the distant horizon."
    "It takes a moment before he turns back to you, his eyes blurry."
    f "They said it was hollow grief."
    "Furkan stammers in a voice lower than you can hear."
    f "They said that I could never become their chief just as I abandoned my duty and left my father to die."
    f "But I persisted, I pledged myself to the tribe when all I wanted in my life was to be free from it."
    f "When I ran away from the tribe, I wandered off the primrose path for a while, I fed myself, had my way with any traveller across the plains."
    f "Then comes the long weeks of slumber and weariness. I quickly got bored of this life. I stayed in my shed, refused to see anyone, not even the general."
    "Furkan's voice is soft, as he continues to speak."
    f "I thought I had wanted to be rid of the tribe's life, and I was too stubborn to admit otherwise."
    f "There were times Kari pleaded for me come back and I would feign being asleep. I was determined to stay in the shed, until that last knock."
    "His eyes are distant, and his voice is barely a whisper."
    f "The passing of my father brought me home, dragged my body with deep grief. I tried not to cry when I saw him, but it is futile effort. I was left half a ram after the ceremony."
    f "And thus was the impression of my first day as the chief, a traitor... a fool... and worst of all, a wailing wimp."
    e "Furkan... you had all the reason to cry. It was a sad day."
    f "It was, but I had to move on, I had to be the chief my father wanted me to be. Or else, what was the point of all this?"
    "He looks at you, his eyes are clear, his voice is firm."
    f "If my people see me as an incompetent fool, then I shall be the fool they need. Just as who Rahim sees me as, I shall be who he needs."
    e "You are not a fool, Furkan. Stop saying that."
    "Furkan chuckles, as he pats your head."
    f "You are too kind, [e]. But I am afraid, I am not as strong as you think I am. I am not as strong as my father thought I was."
    "He turns away, as he walks towards the open windows."
    "You watch as he stares at the horizon, his eyes are fixed on the distant lands."
    f "I will see you where Haskell lives."
    "You nod, as you slowly take your leave."

    $ removeItem("Letter of Alliance", inventory, 1)
    $ quest42.qComp(_("Meet Furkan and Rahim at Haskell's Hut"))
    $ quest42.status = 3

    jump main_kechioeren_conference

default pact_choices = {"Furkan Score": 0, "Rahim Score": 0, "Ancient Tree": None, "Trade Deal": None, "Guards": None}

label Furkan_Rahim_Pact:
    "You arrive at Haskell's hut, the dragon is already waiting for you at the door."
    "On the corner of your eyes, you notice Kari standing beside Furkan, who is crossing his arms silently."
    show haskell normal with dissolve
    h "Ah, [e]. You're here. Come in, come in. The tea is ready. And little ram, you too."
    "Haskell opens the door, as he gestures both of you to enter, leaving the general outside."
    scene haskellhut with dissolve
    show furkan normal at l1 with dissolve
    "You step inside, the hut is warm and cozy, the smell of chamomile fills the room."
    "Rahim is already sitting at the table, his eyes are fixed on the paper in front of him."
    show rahim normal at r1 with dissolve
    h "Take a seat, take a seat. Unless you want to stand, I don't mind."
    "You sit down, as Haskell pours you three some cups of tea."
    h "Want tea? I brewed up a pot full of Chamomile, freshly harvested."
    r "No thanks."
    h "Actually, that wasn't a question, Himmy. I've already poured you a cup."
    "Haskell shoves the tea in front of the old bull, which he reluctantly takes."
    h "Welcome to my humble abode, you two magnificent leaders. Take a seat, I've got some biscuits if you're hungry."
    f "Thanks, I will be sure to take a bite-"
    r "We're not here for tea and biscuits, Haskell."
    h "I am the host today. Maybe you could've said so before I had picked the freshest thymes for you marvelous leaders."
    "The dragon pours two more cup, before he puts the pot away."
    h "Isn't that right, [e]."
    e "Uh- yes."
    "He turns back to the bull, who frowns at the dragon."
    h "Well, someone's being a grumpy old man. I'll leave you three be then."
    "Haskell smiles as he leaves the hut with the empty pot."
    "You briefly catch a glimpse of Kari standing outside, guarding the entrance, before Haskell closes the door."
    r "So, thank you for coming here, Furkan. And you, [e]."
    "You nod."
    f "I have read your letter, Rahim. I am glad you've decided to meet me in person. This will clear up the air nicely."
    f "Before that, I am curious, what made you change your mind, Rahim?"
    r "I have not changed my mind, Furkan. I am merely following the decision of my people."
    r "They deemed me the leader of Lusterfield, and I will do whatever it takes to ensure the safety of my people."
    f "Sure."
    r "I did not come here to explain myself, Furkan. I came here to discuss the future of our tribes."
    "Rahim shoots a stare towards the other side of the table, and raises his hand to his beard."
    f "I am glad, we shall put the past behind all of us."
    r "It's best we secure this history in our mind, so none of the betrayal shall happen again... if we were to be allies, it shall be permanent."
    "Furkan nods with the warmest smile you have ever seen from him. His cordial pose hides a hint of delight and anticipation."
    r "Now, let's talk about the alliance."
    "He throws his hands on the table, looking at Furkan intently."
    r "Can't believe I am sitting on a table with a goat again, but here we are."
    "Furkan chuckles, as he takes a sip of his tea."
    f "Rahim. You have no idea how long I have been waiting for today."
    r "Let's not get ahead of ourselves, Furkan. We are here to discuss the terms of the pact, not to celebrate."
    f "Of course, Rahim. I am ready to listen to your terms."
    "His elegant manners and hospitality had tricked you as being an experienced chief, but in truth, this is probably his first time negotiating a pact."
    "Rahim spots this flaw earlier on, often commmentating on his nervousness, or when he is intimidated by the bull's voice. Furkan would only smile along, but he does not seem troubled."
    "It is after a few minutes into the discussion that Furkan has gotten comfortable in his chair, he sits upright by the table, sometimes even talks over Rahim in the matter of his people."
    "You had not been the greatest mediator, as expected, they often speak of words you rarely understand, of places and lands further than you have ever walked."
    "Gradually, you decide it is best you sit between the two leaders silently, occassionally nodding or taking a sip of Haskell's tea. Staring was not a good option, as Rahim would chide you endlessly."
    "During the long hour of boring dialogues, your mind wandered everywhere, mostly of the places you have visited on this land, but sometimes you thought about Chime."
    "It had been a while since Puro even crossed your mind, for a long portion of your life you lived in that village, yet your memory of it is getting fuzzier by seconds."
    "You were dragged here because you were looking for Chime, even whilst Chime had become a distant memory, you cannot shake off your quest for him, as if you were compelled by a ghostly force."
    r "...That's not possible! The tree is too close, the Luster river is already an apt boundary for you. Nothing further."
    "A familiar gruff voice wakes you from the train of thoughts, you look up, and notice the two begin to argue over the pact, again."
    f "The goat tribe had always held rituals around the tree, it has been our tradition since the beginning of our tribe. We are simply asking for a time where we can hold our ritual undisturbed."
    r "Your tree is in the path of our main route to the river, I cannot tell my people to just not walk by when you parade around your passed ones."
    f "It had been this way since before my father, I am sure there are other paths your wagons can take during our ceremony."
    f "If my memory stands, it was the first of Lusterfield who had taken our old territories, including the tree."
    r "Your history was nothing but folk tales to me, little cub. I cannot see myself allowing you to leave us defenseless."
    f "We are forming an alliance, our people is your people too."
    "Rahim raises his hand to support his snout, he retreats into moments of silence while Furkan is waiting for an answer."
    f "I am afraid we won't reach a conclusion if this is the conversation we are having."
    f "But, [e] is here."
    e "Uh, me?"
    r "Oh. Yes, [e]."
    f "He had contributed in both our tribes, especially for me, maybe he can prove to be useful today."
    "Both Rahim and Furkan stare at you suddenly."
    e "Sure, I mean, I was not sure why I am here in the first place."
    "You raise the cup to your mouth, slowing sipping up the tea as you peer at the two leaders."
    r "Aren't you afraid that he'd side with me, after all, he lives in my village, he's one of my people."
    f "Not at all, I would just like for our pact to be settled. But indeed, I suppose [e] won't feel much better if we get the shortest end of the stick."
    "You smile awkwardly, from what Furkan had suggested, it had sounded not like an intimidation, but a subtle regard to your desire to please."
    "Sometimes you question if you had made your intention too obvious to their eyes."
    r "As you wish."
    r "You have walked around the ancient tree, [e]. Should we avoid that route while the goats perform their rituals?"
    menu:
        "The brown bull did not leave your sight for a moment, his face inches closer as the two waits for your answer."
        "Avoid the ancient tree":
            $ pact_choices["Ancient Tree"] = "Kechioeren"
            $ pact_choices["Furkan Score"] += 1
            e "I think, we should avoid the tree? Rituals are sacred, after all."
            f "Then it is settled."
            r "I had just held a village-wide vote, and now I let one person to deal with the matter of two."
            r "Fine. [e], I will have you know I am not happy with this decision."
        "Respect the Boundary":
            $ pact_choices["Ancient Tree"] = "Lusterfield"
            $ pact_choices["Rahim Score"] += 1
            e "I think, the boundary is here for a reason, the Lusterfolks should travel freely?"
            r "Great, now we can move on."
            f "If this is the will of [e], then it shall be."
            r "It is the will of my village."
            f "I suppose we can arrange a puppet show for your curious villagers while we are at it."
    f "Now, we shall discuss the matter of trade route. It was left unsettled at the beginning of our discussion."
    f "I reckon [e] is familiar with it already?"
    "You shake your head, you had been trailing off to your daydreams while the two were talking, not a single word about the trade had you recalled."
    "Furkan and Rahim look at each other with a puzzled face, before returning to you with folded brows."
    if quest38.status:
        f "First of all, we are grateful for [e] and the red bear's effort to restore the bridge, it helps reinstating our route quickly."
    else:
        f "First of all, the bridge shall be restored, we will both share the cost equally."
    f "Rahim here suggested Lusterfield should receive our flowing water regularly, while we may receive... some of his fabric, made from our people's sheddings."
    r "It's the only thing we can offer here. You had rejected my other proposals."
    f "We have our own seamster here, Rahim. I have heard your tailor skills were exquisite, but I don't see how I would sacrifice our sacred water for it."
    r "Weren't your people practicing magicless battles? I am sure some of you can live without magic."
    r "Lusterfield is not known for arcane mastery, or healing, but it should be helpful for when hard times come."
    f "I understand your concerns, Rahim, but I think the flowing water is too important for us to give up."
    r "Do you want to give up the flowing water, or do you want to give up the alliance?"
    "Rahim's voice is stern, as he looks at Furkan with a piercing gaze."
    f "It seems we both cannot reach a conclusion..."

    if pact_choices["Ancient Tree"] == "Lusterfield":
        r "Fine, a vote. If we can even call it."
        "Rahim has grown impatient, he crosses his arm silently while waiting for your decision."
    else:
        r "I concur that we would need a third vote."
        "You look up to see Furkan stare at you intently."
    menu:
        e "Uhm..."
        "Trade the flowing water":
            $ pact_choices["Trade Deal"] = "Flowing Water"
            $ pact_choices["Rahim Score"] += 1
            e "I agree that Lusterfield might need the flowing water."
            r "That makes us two votes."
            if pact_choices["Rahim Score"] == 2:
                f "[e], is this what you truly wish? I find it hard to believe such an abundant village full of resources would need our only reserve here."
                e "I am sorry, Furkan. This is what I think is best for both tribe."
                "Furkan's eyes meet yours as you raise your head, but you quickly avert your gaze."
            else:
                f "I suppose that is only fair, before we run out of flowing water for the both of us."
        "Trade something else":
            $ pact_choices["Trade Deal"] = "Cashmere"
            $ pact_choices["Furkan Score"] += 1
            e "Maybe you should trade something that's less scarce for both tribes? Like horehounds?"
            f "Horehound is not as useful for Rahim, we volunteer to confer our wool to Lusterfield, it should sweeten the pot enough."
            if pact_choices["Furkan Score"] == 2:
                r "You are sabotaging your own homeland, [e]. I hope you remember that when you sleep on our land tonight."
            else:
                r "Fine, at least my people won't starve without some special water."
    "The hut quickly descends into silence once more as Rahim record the ruling."
    if pact_choices["Furkan Score"] == 2:
        f "Remember, tend to both sides' need, [e]."
    if pact_choices["Furkan Score"] <= 1:
        "Furkan puts down his hands, as he begins to address the room sternly."
        f "Before the next subject begins, [e]. I need you to understand, this is not a time for personal feelings."
        f "I understand that you have a kind heart, which is why both of us had agreed to give you the third vote in this meeting."
        f "But today, the fates of the two tribes are in your hand, please do not mistake your choice as a test of affection to any of us."
        "You nod silently."
        r "I suggest you stop harassing [e], and let him have a judgement of his own, little whelp."
    "Rahim adjusts his seat as he takes a deep breath."
    r "The next subject - guards. My people are not trained, I proposed the goats should send a few of your guards or huntsmen to station in our village."
    r "Our observatory is free for your goats to use, we will use the tower as an access point from your own outpost."
    f "It is not necessary, Rahim, we already have huntsmen warding the ancient tree. You are spreading my men thin if we are to be on guard everywhere."
    f "I suggest you begin to train your men, or the swordmaster wolf could undergo another stealth mission of his to solve all problems."
    r "Right, if you had listened like I told you to, you'd know we are recruiting young lads either way. Still, I must commend that your people are more versed in defending, which is my I needed them."
    "Furkan nods."
    if pact_choices["Furkan Score"] == 0:
        f "Regretfully, it seems [e] has to make the decision again."
        "Rahim smirks, as he raises Haskell's biscuits to his mouth."
        if quest23.status:
            f "You have fought with my men, courier. You have seen their weariness. Please, make the right decision."
    else:
        f "Shall we leave the choice to [e]?"
        "Rahim begrudgely shifts his attention to you again."
        if pact_choices["Furkan Score"] == 2:
            r "Don't leave your home defenseless."
    menu:
        e "Let me think..."
        "Send the Guards to Lusterfield":
            $ pact_choices["Guards"] = "Lusterfield"
            $ pact_choices["Rahim Score"] += 1
            e "I agree that Lusterfield needs capable guards. Since it resides in much of an open field."
            e "If enemies were to invade Lusterfield, they would find the task much easier as compared to the forest."
            e "Perhaps the goats can share a few of them?"
            r "Yes, they can."
            if pact_choices["Furkan Score"] == 2:
                "Furkan looks at you, his eyes are soft and warm as he nods."
                f "It is only fair, we shall send our guards to Lusterfield."
            else:
                "You turn your head towards Furkan, expecting to see the face of disappointment, but he only nods. You can hardly discern his expression."
                f "I suppose so."
        "Leave the Guards in Goat Tribe":

            $ pact_choices["Guards"] = "Goat Tribe"
            $ pact_choices["Furkan Score"] += 1
            e "I believe we can defend ourselves enough, it doesn't make sense to send guards without any threats."
            r "Nonsense, [e]. You don't need to see a monster killing innocents in front of you to know they exist. Shall we wait until the foes come knocking on our front door?"
            "You feign a sliver of contemplation, in truth you understand the importance of defense."
            e "I just thought we should maintain balance between the two factions."
            if pact_choices["Rahim Score"] != 0:
                if pact_choices["Rahim Score"] == 1:
                    r "Fine, I now know you have [e] on your side, Furkan."
                else:
                    r "Fair. We will train our own guards soon enough."
                f "I am glad we have reached an agreement, Rahim. I am sure our people will be happy to hear the news."
    $ QuestFinish(quest42)
    $ QuestBegin(quest43)
    $ quest43.qProgress(_("Meet Furkan and Rahim again at Lusterfield's longhouse."))
    if pact_choices["Rahim Score"] == 0:
        "Before your sentence ends, Furkan tilts his head slightly to the side, as he raises his hand to stop you."
        f "We are grateful for your decision."
        r "Enough! I will not let my people be defenseless, Furkan. I will not let you have your way just because [e] is infatuated with your kind."
        "Rahim shouts as he slams his fist on the table, addressing Furkan but his eyes are locked into yours."
        f "I am sorry, but our courier here has his reasonings, we both shall respect his decision."
        "The air is tense, as you feel the weight of the two leaders' gaze on you."
        e "I thought it's better for both sides, Rahim."
        r "I don't care what you think, [e]. Keep my people away from the tree, fine, keep the flowing water, fine. But I am not letting you strip my village naked of its defense."
        f "Rahim, if you are so intent on your cause, I am sure you could have persuaded [e] better before he made his decision."
        r "He knows nothing! I can't have someone like him decide the future of our people, and yours."
        f "One thing my father taught me, was to always keep true to my words, if I ever wanted someone to trust me."
        f "we both had accepted [e] into the discussion, I believe our words shall hold weight here."
        r "Here's another lesson. You either accept my terms, or we are done. You goats have no real leverage against us."
        "The bull stands up, as he pushes the chair back, his eyes are locked into Furkan's."
        f "Then I am afraid we cannot proceed with the pact."
        r "...You are willing to sacrifice the goods of your people, for something your father couldn't even abide?"
        f "I am abiding by the people I want to trust, if we were to form an alliance, it shall be ever-lasting, just as you said."
        "Though Furkan silently trembles in front of the mad bull, he has mostly kept his composure. The voice is calm as he speaks."
        f "It is but my pitiful wish for you to trust my words as much as I do yours."
        "For a moment, Rahim's eyes soften, the anger in his eyes fades away as he looks at Furkan on a new light."
        r "Your elegant words are nothing but a poor excuse to your foolish ambitions, Furkan."
        f "My duty outweighs my ambition, Rahim."
        r "At least you've grown a spine since the last we spoke. It's a rare sight these days. I put my trust more in an ally who stands his ground than a spineless porcupine who sways where the wind goes."
        "The bull sits back down as he takes a deep breath, before you notice his side glance."
        r "You've been silent for a while. What do you think?"
        e "Well, it's quite stressful for me to weigh in on the pacts all by myself. I am just a courier after all."
        r "And it should stay that way."
        "Rahim lifts his eyes away, nodding indifferently."
        r "If I hadn't known you, you'd be banished into the wilderness the first time you sided with the goats."
        r "I will allow it, your goats can stay wherever you like, but no more decisions from [e]."
        f "Of course, Rahim. You will find nothing but loyalty from my people."
        "You went silent again as they continue to finalise the pact without any of your input, it also doesn't help that."
        "Nonetheless, you breathe a sigh of relief seeing Rahim lean closer to the table. He may still hold a grudge, but at least you are exempt from any hard decisions."
    "It was not long before Rahim has completed writing the pact, he lets Furkan read over every line, before signing both their names on the corner of the paper."
    "Rahim puts down the cup and pushes himself away from the table. He barely looks at you, as he paces around Haskell's hut."
    r "This is all we have to discuss today."
    "The ram nods, as he stands up and offers his hand to Rahim."
    f "Thank you, for putting everything all behind us. I am sure our people will be happy to hear the news."
    "A brief silence fills the room, as Rahim takes the hand and shakes it firmly."
    r "The establishment of the pact is not over. We'll meet again in the village next time."
    if pact_choices["Rahim Score"] > pact_choices["Furkan Score"]:
        show furkan normal at l2 with move
        pause 0.5
        show rahim normal at c1 with move
        "Rahim stands up again, carrying the journal and the completed pact with him. He turns back, a gaze quickly meets your eyes."
        r "Come, [e]."
        "You rabidly leap over the chairs, Furkan gives you a nod before you begin following the old bull, closely."
        e "What is it, Rahim?"
        r "We're heading back to Lusterfield."
        "Rahim says calmly as he pushes open the door. His tone is more like a command than a request."
        scene alchemistscabin with dissolve
        show rahim normal with dissolve
        "You notice Haskell and Kari sitting in the garden outside, the dark dragon seems to be enjoying his tea with closed eyes."
        "Your attention shifts to the deer noticing the two of you, silently staring with wider eyes, as if pleading to be rescued from another second of sitting with the tea master."
        "Strangely, you chuckle at the goat general's misery, before Rahim takes notice. One side eyes from him is enough for you to turn back to the front."
        scene woodlandoutpost with dissolve
        show rahim normal with dissolve
        "The road ahead is quiet, all you can hear is the occassional panting coming from Rahim. You have trodded the same path many times, though not as often with the old bull ahead."
        "His sweat has soaked through the old rag covering his body, your gaze always gravitates towards his brawny back, stretching out sometimes as he strains his muscles."
        "Sometimes you wonder if he has intentionally kept himself unkempt, for a experienced tailor like him, you'd think he has an eye for fashion."
        scene ancienttree with dissolve
        show rahim normal with dissolve
        "Perhaps this is his fashion, the musty old garments, with tawny cloth draped over his soft fur, you'd have swear you could squeeze out some water from that drenched fabric."
        "By now you expect Rahim to say something, it's not a common ordeal to just walking silently, other folks would have been bored enough to at least ask about the weather."
        scene lusterfield02 with dissolve
        show rahim normal with dissolve
        "When you arrive to Lusterfield again, you have gotten so used to the peacefulness, he'd almost spooked you away when he turns around in front of his house."
        r "You can go now, [e]."
        e "W-what was that all about...? I thought you were mad at me."
        r "I wasn't."
        "His answer is so concise and calm, it left you speechless before the bovine man."
        r "Come to see me for the next meeting."
        "You didn't get to respond before he slams the door shut, only leaving a gust of air that softly blows on your snout."
        jump main_lusterfield02
    else:

        show rahim normal at r2 with move
        pause 0.5
        show furkan normal at c1 with move
        "Rahim stands up again, carrying the journal and the completed pact with him. The room falls into silence again as he walks out."
        f "I hope I had not embarrassed myself, or noticeably so."
        e "You did fine, Furkan."
        f "Not without your aid. Surely. I could not fare so well by myself."
        if pact_choices["Furkan Score"] == 3:
            f "But as a leader, you have to please everyone-"
            "Furkan stops himself before continuing, his cheeks burns red."
            f "What I meant was, A leader has to take it from all sides-"
            "Another pause compels him to stammer, peeking at your direction. You are sure that it's merely accident, the chief would make a much subtler suggestions, if he were to tease you."
            f "I had begun myself badly. The crux of the matter is with the negotiation, Lusterfield and us, we are used to bargaining advantages back and forth."
            f "Sometimes you take, sometimes you give. It is the trading that fortifies our alliance."
            e "You aren't happy that I took your side?"
            f "I am not happy that our ally stormed off his proposed meeting. This is not a good start at all."
            "Furkan looks away, his face sterner than a disappointed elder."
            e "Sorry."
        else:
            f "I am glad we have reached an agreement, [e]. I am sure our people will be happy to hear the news."
            f "You have done well today, [e]. I am both surprised and grateful for your presence."
            f "I sometimes wonder about your role in this world, but today you have proven to be a valuable asset to both of us."
            e "Thank you, Furkan. I am just doing what I think is right."
            f "And that is all we need from you, [e]."
            "Furkan stands up, as he offers his hand to you. You take it soon as he shakes your hand firmly."
            "And quickly he raises your hand, as his head leans down to kiss it tenderly."
        f "I will see you for the second meeting."
        "You nod, as you watch him walk out of the hut."
        "You are left alone in the hut, the warmth of the tea still lingers in the air."
        h "How's the thing? You three got along well?"
        "You turn around to see Haskell standing at the door, a warm smile on his face."
        h "I heard you three were having a heated discussion, I thought I should come in and check on you."
        e "It was... interesting."
        h "Interesting? That's a good word for it. I thought that angry bull was ready to waste my tea on little Furkan's face."
        e "I think they are getting along now."
        h "Good, good. Now that you are done, I can finally have my tea in peace."
        "You chuckle, as you watch Haskell pour himself a cup of chamomile tea. He then stares at you as if you've forgotten something."
        "You quickly excuse yourself, as you walk out of the hut."

        jump main_haskell_hut




label Furkan_Enter_Mayor_Longhouse:
    "You notice the planks on the supposed longhouse is now pried open, probably at the hands of Amble."
    "Just as you are about to open the door, you notice a familiar figure, trodding towards your direction."

    if vote_result < 0:
        show sebas normal with dissolve
        s "Hey hey, [e]. Is that the house thing? Mayor's longhouse? It doesn't seem that long, honestly."
        e "Yeah, I don't know, I have never been inside before."
        s "Well, I guess it is a longhouse, but it doesn't look like a house at all."
        s "This house's been here before I even came to Lusterfield, it's the first time I hear someone calls it a Mayor's house."
        "You chuckle, as you watch the lion push open the wooden door, leading both of you inside the abandoned building."
        scene mayors_longhouse with dissolve
        "You find yourself in the old mayor's longhouse. Rahim is sitting on the chair at the center, his eyes are fixed on the journal in his hand."
        show sebas normal at l1 with dissolve
        "Sebas looks around the dusty room, there's dust everywhere, even in the air."
        s "This place is in a desperate shortage of Ole... He's gonna get a kick out of cleaning these walls."
    else:

        show furkan normal with dissolve
        f "Good day, [e]. This is the longhouse we are supposed to meet, was I correct?"
        e "Yeah, I don't know, I have never been inside before."
        "You frowned, it feels weird to see Furkan in Lusterfield, weirder that he is not accompanied by the general."
        e "Weren't you supposed to be with the general?"
        f "Worry not, courier, I sneaked out, Kari will never approve of my travel alone, and he did not wish to be here."
        "Furkan feints a weak smile, it makes you wonder if Kari even knew about the last time he was here."
        f "Shall we make this meeting quick?"
        "Before you respond, the goat chief pushes open the wooden door, leading both of you inside the abandoned building."
        scene mayors_longhouse with dissolve
        "You find yourself in the old mayor's longhouse. Rahim is sitting on the chair at the center, his eyes are fixed on the journal in his hand."
        show furkan normal at l1 with dissolve
        "Furkan looks around the dusty room, his maw hangs agape."
        f "I am grateful to be here, Rahim. But you misconstrued my aptitude for the ancients. I am not sure if this place is safe to be in, let alone to discuss our alliance."
    e "What is this place, Rahim?"
    show rahim normal at r1 with dissolve
    "Rahim looks up, his eyes are fixed on you. You can see a hint of amusement in his eyes, as he puts down the old book."
    r "It's the old mayor's longhouse, where they meet and discuss matters of importance."
    if vote_result < 0:
        s "That old mayor surely didn't have a long life breathing in those thick dust, did he?"
    else:
        f "Old Mayor? Then it must be very important. Why is this place even abandoned in the first place?"
    r "The last mayor to set foot in here, Stadfel, he died peacefully in his sleep... ages ago, before I was even born."
    r "As it had been a peaceful death, he did not leave anything behind, nor a choice for the next mayor."
    r "Election was attemped to be hold, but each candidate... faced inexplicable misfortunes, it was the reason why we had no mayor for the better part of the history."
    ""
    r "Back to the matter at hand, this journal. I found it when I was cleaning the old mayor's longhouse, fell from the cracked wooden planks."
    r "I have read through it, the journal was written by the old mayor himself, it was a record of his daily life, his thoughts, and his plans for the village."
    r "Towards the end of the journal, he had been investigating the longhouse's moistness problem, the summer rains had been harsh on the buildings."
    if vote_result < 0:
        s "Another history lesson... I am not sure if I can keep up with this."
    else:
        f "I don't see how this is relevant to our discussion, Rahim."
    r "Stop moaning and listen, child. He had written about the wooden left wall of the longhouse, where the moss grew almost exclusively on that side."
    "You look around, the left wall is indeed covered in moss, the wooden walls are damp and the floor is moist, you can smell the horrid stank even from here."
    "Rahim flips through the pages, before he stops at a certain page, and continues."
    r "He had compared the interior of the longhouse to the exterior... and found that there was a hidden space unaccounted for."
    r "Turns out, it was a hidden entrance to an underground temple, he had written that it was much larger than the longhouse itself."
    r "So, there it is. We ought to investigate the temple ourselves, there are much more to the journal than I had told you."
    if vote_result < 0:
        "Sebas looks at you, his eyes are wide with excitement."
        s "A hidden temple? That sounds amazing! I want to see it!"
        r "I don't know, but we have to find out. The mayor had written about a hidden lever that opens the entrance, but he never wrote where it was."
    else:
        "Furkan's eyes widen, he looks at you, then back at Rahim."
        f "What do you suppose we do with this information, Rahim?"
        r "Explore the room ourselves, and I would like for [e] to accompany me."
        f "What if this was the very thing that killed the old mayor and the other candidates. Would it not be better for you to leave this behind?"
        r "No. I believe it has to be linked to whoever stole your runes. And, I am done sitting around and waiting for you to find nothing on your own."
        f "Then, I should come along as well. As the leader of the goats, I must know what lies in our own temple."
        "Rahim doesn't flinch, his gaze looks as if it was expected of him."
        r "Why else did I invite you here, chief?"
    "His hand sweeps across the table before standing up and walks towards the cabinet at the left wall."
    r "If the journal is to be believed, the entrance should be here."
    show rahim normal at c1 with move
    pause 0.1
    if vote_result < 0:
        show sebas normal:
            xalign -0.15
        with move
    else:
        show furkan normal:
            xalign -0.15
        with move
    "He points towards the bookshelf, where the books are stacked neatly. You notice a small gap between the wall and the shelf."
    if vote_result < 0:
        s "I think I see it too."
        "Sebas walks over to the shelf, and begins to push it, but it doesn't budge, not even with Rahim's help."
        s "Come on..."
        "Sebas pushes the shelf again, but it still doesn't move."
    else:
        "Rahim shifts to the side to push the shelf, but it doesn't budge. Furkan stares at the shelf, before he walks over to help Rahim."
        "The two of them push the shelf together, but it still doesn't move."
        f "It's stuck."
    "Rahim takes a step back, as he looks at you."
    r "The mayor had written about finding a hidden lever, but he never wrote where it was."
    e "Then, where can we find it?"
    r "We should look around the longhouse, it's should be here somewhere."
    "Silence fills the room, as the three of you begin to search the longhouse for any hints."
    $ quest43.status = 3
    $ quest43.qComp(_("Optional: Clear all moss"))
    $ quest43.qProgress(_("Search for a secret lever in the mayor's longhouse"))
    jump main_lusterfield_mayors_longhouse

label Rahim_Ask_Bad_Omens:

    r "Election was attemped to be hold, but each candidate... faced inexplicable misfortunes, it was the reason why we had no mayor for the better part of the history."
    e "Misfortunes?"
    r "Bad omens, some said the candidates were cursed."
    r "One of them, the mayor's son, fell ill and became bedridden, plagued by a deadly fever that eventually claimed him."
    r "Another one, the ambitious old steward, he preyed on the title after the son's death. And one day he was found floating face down on the river."
    r "The last one withdrew from the election, but an inconspicable paranoia ate him whole, it was a fate worse than death. But eventually he fled the village and no one saw him since."
    e "Is this why you were not... the 'mayor'? Because of the curse?"
    r "I am not a mayor. And we had not needed one for decades. If not for the goat's invasion I'd not be taking up as the spokesperson on my village's behalf."

label Mayors_Longhouse_Cabinet:

    if quest43.status != 3:
        menu:
            "Enter the temple":
                "You shift the cabinet aside, and begin walking towards the underground temple."
                jump Temple_of_Tapjoo_Enter
    "The cabinet is filled with various books, scrolls, and other documents, some of them are old and dusty, while others are new and well-kept."
    "Skimming past the titles, it seems they are mostly about the history of Lusterfield, some of the village's records and the old mayor's personal collection."
    "The dust on the shelves is thick, except for a few of them, where Rahim had been looking through."
    menu:
        "Ask Rahim":
            e "Rahim, what are we looking for?"
            show rahim normal with dissolve
            r "The old mayor had written about a hidden entrance to an underground temple, it should be somewhere around here."
            e "What does it look like?"
            "Rahim glances at you for a moment, before continues flipping over the book."
            r "Buttons, levers. The mayor hid the entrance well, it should be something that blends in with the wall."
            e "I see."
            e "What about the journal? Can I take a look at it?"
            r "Not yet. I will show it to you once we find the entrance."
            jump main_lusterfield_mayors_longhouse
        "Search the cabinet":
            "You begin to search the cabinet, looking for any hidden levers or buttons that might open the entrance."
            "You find nothing but dust and old books, the cabinet is filled with old scrolls and documents, some of them are written in a language you do not understand."
        "Leave":
            jump main_lusterfield_mayors_longhouse

label Mayors_Longhouse_Planks:
    "You notice the wooden planks on the left wall are covered in moss, the wood is damp and the floor is moist."
    "It seems to be covering a hole, but you can't see anything beyond the moss."
    jump main_lusterfield_mayors_longhouse

label Mayors_Longhouse_Rhyme:
    $ mayors_longhouse_interaction["mayors_longhouse_rhyme"] += 1
    "A white parchment settles easily on the table, there are some stains on the cover, and the pages are yellowed."
    "You pick up the parchment, and notice the writing on the first page."
    "It is a rhyme, written in a neat cursive handwriting. The words are written in a black ink, and the letters are large and bold."

    "{i}Five wayfarers wandered under the morning, {p}The horned one paused where the rivers string,{/i}"
    "{i}By the edge he pondered the shape, {p}The waters embraced him; and so did the spring.{/i}"

    "{i}Four wayfarers walked as the sun climbed high, {p}The fanged one ventured where the forests sighed,{/i}"
    "{i}Drawn to the shadow that howled his name, {p}The woods closed in and the last wail died.{/i}"

    "{i}Three wayfarers roamed from the shore, {p}The gilled one swam where the sea has roared,{/i}"
    "{i}Beneath the depth he found his fellows, {p}Gave himself to the harness of the thrall.{/i}"

    "{i}Two wayfarers promised to never stray, {p}But the clawed one climbed where the mountains swayed,{/i}"
    "{i}He chased the scourge that caused it all, {p}A battle he sought; none lived to see the day.{/i}"

    "{i}One wayfarer sprawled across the red dryland, {p}The scaled one listened where the desert scanned,{/i}"
    "{i}A calling, a purpose, from horizons untold, {p}His fate woven before the night ran cold.{/i}"
    if quest43.status != True:
        if mayors_longhouse_interaction["mayors_longhouse_rhyme"] == 1:
            "You look up to see Rahim and Furkan, their eyes fixated on the parchment."
            e "Did the old mayor write this?"
            r "It is a children's rhyme, [e]. Older folks used to sing it when they were younger. I've heard it before."
            if vote_result < 0:
                s "I've heard this one, too. I thought they were playing games... or something."
                r "No, most of the children in Lusterfield have forgotten it, the only few who are fortunate enough to hear it probably heard a happier version."
                "Sebas gulps, as he turns away to inspect the room again."
            else:
                f "Strange, I have never heard of it."
                r "Only the old folks remember it, kids nowadays have forgotten the rhyme. The old mayor must have written it down for his grandchilren."
                "Furkan looks at you, then turns away to inspect the room again."
                r "We should look around for more clues, [e]."

        elif mayors_longhouse_interaction["mayors_longhouse_rhyme"] == 2:
            if vote_result < 0:
                "You look up to see Sebas, he's staring at the rhyme as you do."
                s "I swear I have heard this before."
                s "I did remember it having to do with how tribes of the wayfarers, but I don't remember the happier version..."
                s "I'm starting to regret not taking History lessons seriously."
                "You nod, as you put the parchment back on the table."
            else:
                "You turn around as you finish the rhyme, Rahim seems to be distracted somewhere else, while Furkan slowly walks towards you."
                f "Do you think this is a clue, [e]?"
                e "I am not sure, Furkan. It's just a rhyme."
                f "It's a strange rhyme, I didn't expect Lusterfield's children are taught such dark tales."
                "You nod, as you put the parchment back on the table."
                e "I wonder what the other wayfarers were doing when they perished one by one."
                f "Perhaps they were searching for something, or someone."
                "Furkan smiles softly, as he pats your shoulder. But when you turn around, he is already walking away."
        elif renpy.random.random() > 0.45:
            e "Maybe... it has something to do with the weird markings around the house."
        elif mayors_longhouse_interaction["mayors_longhouse_rhyme"] > 5 and renpy.random.random() > 0.7:
            e "The rhyme is written as a sequence, I wonder if it has something to do with the faces around the room."
    jump main_lusterfield_mayors_longhouse

label Mayors_Longhouse_Going_Downstairs:
    "As you press on the marking, you hear a loud creaking sound, as the bookshelf gives way."
    show rahim normal at r1 with dissolve
    "Rahim notices the shifting of the cabinet, as he quickly turns around. Furkan's eyes widen as he steps back."
    "The bookshelf slides to the side, revealing a dark staircase leading down into the darkness."
    "The staircase is narrow, and the steps are steep, it's almost as if it was carved out of the earth itself."
    if vote_result < 0:
        show sebas normal at l1 with dissolve
        s "Whoa! This is amazing! I can't believe we found a secret passage!"
        "Sebas jumps up and down, his eyes sparkling with excitement."
        s "What's down there, Rahim?"
        r "The temple. Have you not been listening?"
        s "I was, but I thought it was just a story."
        "You follow both of them down the stairs. The air is damp and cold, the smell of moss and mildew fills your snout."
        r "No, it's real. The old mayor had written about it."
    else:
        show furkan normal at l1 with dissolve
        f "What lies underneath the longhouse, Rahim?"
        r "The temple, the old mayor had written about it."
        "You follow Rahim down the stairs, while the goat chief lags behind. The air is damp and cold, the smell of moss and mildew fills your snout."
    scene black with dissolve
    e "What do you mean Rahim, an underground temple built underneath Lusterfield?"
    r "According to the mayor, it's a place where the goats worshipped Tapjoo, where the primordial runes was originally placed."
    if vote_result < 0:
        s "Tapjoo... Do you think the goats are behind this?"
        "Sebas turns to you, he looks pleasantly surprised."
    else:
        "For a moment Rahim stops, as he looks up to meet Furkan's gaze."
        f "Tapjoo... we had not been practicing the old faith for a long time, Rahim. I can attest, this is not our doing."
    "Rahim turns to you, his eyes stare directly into your soul, as if he's trying to see your reaction as well."
    e "Why were they in Lusterfield?"
    r "In the primordial days, the goats had settled in this land, it was only after the great flood that they had moved to the other side of the river."
    e "I thought the goats had always been on the other side."
    r "It was a long time ago, [e]. From before the old gods still roamed the land. We never knew it existed... until now."
    r "The mayor's writings had gotten messier after he visited the altar."
    "Rahim continues as the three of you continue down the stairs, the air grows colder and the smell of moss grows stronger."
    r "I am not sure what he had found, but the journal went from a daily record of his life, to a series of cryptic messages and a few sketches."
    r "This is the line that caught my attention, it was the last entry of the journal."
    e "What is it?"
    r "'{i}A horned dragon that slumbers beneath the earth, bound by chains forged of forgotten oaths.{/i}'"
    r "'{i}The dragon is said to awaken when the shepherd's call reaches the depths, heralding a time of upheaval and transformation.{/i}'"

    if vote_result < 0:
        "You look up to see Sebas's face, and notice both of them are staring at you deeply. Do they think you are the horned dragon?"
        s "I've been saying it, roomie. You do look like a dragon... or goat."
    else:
        "You look up to see Furkan's face, and notice both of them are staring at you deeply. Do they think you are the horned dragon?"
        f "Is he?"
    e "Well, I am neither the only dragon, nor the only one horned here."
    r "Granted, the teamaker is antlered. And I am pretty sure I am not a dragon. Do you think it is a coincidence that you ended up here, [e]?"
    "You furrow your brows, horned dragons were so common in Puro that you had slowly forgotten that you came alone in this land."
    e "Well, I don't recall being bound by chains either."
    r "It could be metaphorical, for all I know."
    "In all honesty, you don't want to know what the metaphor is."
    r "This shepherd, is the reason why I asked for an alliance, if the journal is to be believed. Perhaps the goats can decipher whatever the old mayor had found."
    if vote_result < 0:
        s "Oh, but we didn't bring the goats with us."
        r "Yes, that was what I meant, Sebas. We have to do these ourselves either way."
        s "I do have an idea..."
        r "Do you?"
        "Sebas turns to you, then back to Rahim."
        s "We'll see, Rahim. I have to think about it later."
    "Rahim abruptly stops and closes the journal, before he shoves it back into his pocket."
    r "And I have a gut feeling it has something to do with the missing runes."
    "The staircase ends as you almost bump into Rahim. You find yourself in a large chamber. The room is dark, but you can still see the markings etched on the walls and the floor."
    scene black with dissolve
    if vote_result < 0:
        s "Oh, this is so exciting, I didn't know there's a whole new temple underneath our village the whole time!"
        r "Neither did I, I must say, this place is preserved well."
        s "We should totally let everyone see how big of a temple this is..."
    else:
        f "This is it... the temple of the goats. Yet I have never heard of such a place before."
        r "I would have thought a goat chief would have known about the goat temple."
        f "The goats have not believed in the old faith for a long time, Rahim. Some traditions still retains, but most are better left forgotten."
        f "But, my father might have known about this place."
        r "You think?"
        "Rahim raises his voice, as if he's struggling to contemplate the implication."
        f "If I knew we were exploring an underground temple, I would have brought Kari along."
    r "The whole point of this is to keep it a secret."
    "You look around, the room is vast, the floor is made of grey stone, cracked and chipped along the edges, the high and arched ceiling reaches up to the darkness."
    r "This looks to just be the entrance, the temple should be further down."
    r "We shall proceed with caution. [e], go see if you can find anything that might help us."
    "Hesitantly, you nod, as you take the first step into the temple."

    $ quest43.status = 4
    $ quest43.qComp(_("Explore the Temple"))


    jump Temple_of_Tapjoo_Enter

label Old_Mayors_Journal:

    $ old_mayors_journal01 = Page("Moss\nAn unusual occurrence today has piqued my curiosity. While overseeing routine maintenance in the longhouse, I noticed a faint draft emanating from behind the old tapestry of the harvest. It's strange, considering that wall has no doors or windows. On closer inspection, I found a hidden seam in the wooden paneling. Armed with a lantern and a sense of intrigue, I ventured down the steps. The air grew cooler, carrying the scent of damp earth and aged stone. At the bottom, I discovered a small chamber with walls adorned in faded symbols and carvings — figures cloaked and hooded, holding staffs, and intricate patterns resembling flowing water or the river itself.","In the center stood a simple stone mural, unadorned yet commanding. The atmosphere was thick with an indefinable weight, as if the room itself was holding its breath. I felt an inexplicable pull, a whisper at the edge of consciousness urging me to delve deeper. I attempted to discuss with Irm, the steward, hoping he might shed some light on its origin. He seemed genuinely puzzled, assuring me that no records mention any subterranean structures beneath the longhouse. Sleep did not come easily tonight. My dreams were vivid — a dense forest bathed in silver moonlight, shadows stretching and twisting among the trees. Amidst the darkness, a pair of orange, luminous eyes watched me intently. I awoke unsettled but oddly compelled to return to the hidden chamber.", 1)
    $ old_mayors_journal02 = Page("Shepherd\nSeveral days have passed since my initial descent, and the hidden depths beneath the longhouse occupy my every thought. Each evening, under the guise of extended duties, I return to explore further. The chamber I first discovered is but an antechamber to a more extensive network of rooms and passageways. As I navigate this labyrinth, I find that the walls themselves seem alive with meaning. The symbols and carvings, once obscure, begin to form patterns—repeating motifs of Tapjoo's staff. There are depictions of figures following the old god, their faces indistinct but their postures reverent. The puzzles I encounter are intricate yet intuitive, as if designed to be solved by a specific person or type of person.", "Stone doors yield to pressure applied in certain sequences, and pathways open when patterns are traced upon the walls. My conversations with the steward grow strained. He remarks on my frequent absences from communal gatherings. I offer vague explanations about clerical duties and village records, but I sense his growing concern. The eyes in the forest have become a recurring presence, watching me with what feels like expectation. Last night, the dream changed. The eyes drew closer, and I could make out a figure — a shepherd cloaked in shadows, holding a staff that glinted in the moonlight. He extended his hand as if inviting me to follow. I awoke with a start, the image seared into my mind, and my horns ached greatly.", 2)
    $ old_mayors_journal03 = Page("Horns\nTime has become fluid. Days blend into nights without distinction. I find myself losing hours, emerging from the depths to find the sun setting when I thought it had just risen. The temple—there is no other word for it—has a hold on me that I cannot break, nor am I certain I want to. I've begun to piece together more of the inscriptions - {i}Only those who bear the sacred crowns of nature shall hear Tapjoo's whispers. Through the horns that touch the sky, his wisdom flow like rivers unseen.{/i} Almost immediately I touched my horns, it feels warmer than any other part of my body. I can't help but feel that I am retracing their steps.", "The challenges, the symbols, the pervasive presence of the old god — all seem tailored to lead me toward some revelation. Yet, doubt gnaws at me. Is this a path to wisdom, or am I being led astray by forces I do not understand? The steward's concern has turned to suspicion. He mentioned rumors circulating among the villagers — whispers of strange lights seen in the longhouse at odd hours, of the mayor neglecting his duties. I attempted to allay his fears, but I sense a growing rift. The eyes haunt me still, no longer confined to dreams. In the forest beyond the village, I feel their gaze upon me. During council meetings, I catch reflections in the window that do not match the room. The line between reality and illusion is blurring.", 3)
    $ old_mayors_journal04 = Page("Altar\nThis may be my final entry. I stand at a precipice. The temple's final chamber lies before me, its entrance sealed by a complex mechanism that requires not just physical keys but an alignment of symbols and, I suspect, intent. I've gathered the artifacts found throughout the temple—a set of engraved stones, each bearing a unique symbol. Arranging them in what I believe to be the correct configuration, the door began to open, but stopped short. It seems there's one piece missing, or perhaps a final act required of me that I have yet to discern. The steward confronted me today with an ultimatum. He demands that I refocus on my responsibilities or consider stepping down.","He speaks of the welfare of the village, the trust placed in me. His words are reasonable, but they feel distant, as if coming from another world. That night, the dreams returned with a vengeance. The eyes were closer than ever, the shepherd's figure looming. This time, he spoke — a single phrase that echoed in my mind even after waking: 'The shepherd comes for us all.' I don't know what it means, but it fills me with equal parts dread and anticipation. I leave this journal behind for whoever may find it. Perhaps the steward, perhaps another drawn by the temple's allure. My path leads elsewhere now. I will enter the final chamber tomorrow, with or without the missing piece.", 4)
    $ old_mayors_journal05 = Page("Dragon\nToday, before my search for answers, I stumbled upon an ancient parchment hidden within a concealed compartment in one of the temple's outer chambers. The parchment is fragile, its edges crumbling at the touch, but the ink remains legible. It appears to be a prophecy or perhaps a warning. It speaks of a horned dragon that slumbers beneath the earth, bound by chains forged of forgotten oaths. The dragon is said to awaken when the shepherd's call reaches the depths, heralding a time of upheaval and transformation. I can't help but wonder if this prophecy is connected to the chamber I cannot yet access. Is the horned dragon a metaphor, or does something more literal lie beneath the temple? The idea both fascinates and unsettles me.", "The search has drained my entire body unto exhaustion, my will dwindles but my determination unchanged. I had decided to rest before my final search commences at night. I only dread meeting the shepherd again, his words did not stop resonating in my mind. May the old gods watch over me.", 5)
    if checkNoShopItem("Old Mayors Journal"):
        $ old_mayors_journal01.addTo(old_mayors_journal)
        $ old_mayors_journal02.addTo(old_mayors_journal)
        $ old_mayors_journal03.addTo(old_mayors_journal)
        $ old_mayors_journal04.addTo(old_mayors_journal)
        $ old_mayors_journal05.addTo(old_mayors_journal)
        $ addItem("Old Mayors Journal", inventory, 1)
    "Rahim hands you the journal, the pages are yellowed and the ink is faded, but the writing is still legible."
    return

label Temple_Grand_Chamber_Encounter:
    scene temple_of_tapjoo with dissolve
    "The moss guardian falls again as it crumbles into dust, hopefully for the last time. The door behind you suddenly snaps open, a sigh of relief escapes your lips."
    if vote_result < 0:
        s "I can't believe we did it! We defeated the moss guardian!"
        "Sebas jumps up and down, his eyes sparkling with excitement."
        s "I knew you could do it!"
        r "We should have been here, [e]. But I'm glad you're fine."
        "Rahim pats your back, his eyes are filled with pride."
    else:
        f "Thank the gods, you had done it again."
        r "Good job on the killing, [e]. I am proud of you."
        "Both Rahim and Furkan glances at each other before patting your back at the same time. You can't help but feel a bit embarrassed."
        f "We should proceed now, it won't be long before we reach the grand chamber."
    "You can see the corridor ahead of you, the grand chamber seems to be just beyond the corner."
    "You take your first step in the antechamber of the temple, the room is vast and dark, the only light comes from the torches on the wall."
    e "This is e-"
    if vote_result < 0:
        s "Shush!"
        "Sebas puts his finger on his lips, as he hears strange sounds ahead."
    else:
        f "Shh..."
        "Furkan hushes you, as he points towards where a series of strange sounds comes from, it was the chamber ahead."
    "Intricate patterns of blue markings are painted across the dome, all converging around the central figure of a goat intertwined with the image of Tapjoo."
    "The room is filled with the smell of incense, and the sound of water dripping from the ceiling echoes throughout the chamber."
    "At the center of the chamber stands an ornate pedestal, where you can count three figures standing around it."
    my1 "The moon wanes, and the veil grows thin. Have the offerings been prepared?"
    "A mysterious voice echoes through the chamber, it's soft and melodic, but its sheer presence sends shivers down your spine."
    if vote_result < 0:
        "Sebas and Rahim stop in their tracks, as they listen to the voices echoing in the chamber."
    else:
        "Furkan and Rahim stop in their tracks, as they listen to the voices echoing in the chamber."
    "You and your companions take cover behind one of the massive pillars, close enough to hear their conversation but hidden from view."
    my2 "Yes, brother. The horn of the silver wolf rests upon the altar."
    "Another voice speaks, and your heart skips a beat upon hearing those words... silver wolf. It can't be anyone other than Chime."
    my1 "The time draws near. Have the temple's gates been secured? The uninitiated must not enter."
    my2 "The basin is in place, and the entrance is sealed."
    my1 "Oh... Do you feel it? The whispers in the water? His voice grows stronger."
    "The rhythmic voices carry a tone of reverence, as if they are already chanting in the ritual."
    my2 "As have we all. The prophecy unfolds, and we are but vessels for his will."
    "Strangely, your arm seems to be hovering towards the voice, as if it's beckoning you to follow. You can feel the pull, the whisper at the edge of your consciousness."
    "{i}'The shepherd comes for us all.'{/i}"
    if vote_result < 0:
        "You shudder at the whisper, the same phrase that the old mayor had written in his journal. You look around, but the corridor is empty except for Rahim and Sebas."
        "Afraid of alerting the strangers, you do not dare to ask if they hear the same voice, but the confused look on Rahim's face tells you that he does."
        "And somehow, Sebas is the most alert of you three."
    else:
        "You shudder at the whisper, the same phrase that the old mayor had written in his journal. You look around, but the corridor is empty except for Rahim and Furkan."
        "Afraid of alerting the strangers, you do not dare to ask if they hear the same voice, but the confused look on their faces tells you that they do."
    my1 "With the shepherd's staff, we can bend the strongest of the will. The new guardians proved to be vigilant, but not impenetratable."
    my3 "The lost flock has not stopped their search. They are close, and we cannot slacken."
    my2 "Only those who understand is worthy of following. Yet those who do not understand still listens. How foolish."
    "You begin to close in in the grand chamber, it was spacious, and the three acolytes catch your eyes immediately."
    "The white robed strangers still are not aware of your existence, they are solely focused on the ritual."
    my1 "Once the shepherd arrives, we can finally begin."
    "They guffaw in unison. The cultists seem to be overly amused in their ambition."
    "And most importantly, you feel as if they have a shared mind."
    menu:
        "This might be the best time to jump and surprise the strangers, but if you keep hiding, perhaps you would uncover some secrets."
        "Keep waiting":
            "You decide to remain hidden, you place your finger onto your lips, signaling the two leaders to wait patiently."
            "And so you wait as the cultists draped in dim light continue their conversation."
            my1 "The shepherd's call will be heard soon. The time is nigh."
            my3 "I sense whispers of interference."
            "He cautions, glancing over his shoulder as if sensing your presence."
            my2 "Outsiders who seek to disrupt our sacred rite."
            my1 "They are of no consequence. Sadly, some uninitiated are cursed with obnoxiously vulgar voices."
            my1 "Remember, we shall all search in the fogged forest, do not approach the watchtower."
            my2 "The elder dragon is cautious, we shall avoid his lantern this time."
            "Elder... dragon. Your heart skips a beat. You can't help but feel that the acolytes are talking about Hezzong, the allfather?"
            my1 "We shall begin promptly, the shepherd waits for no one."
            "The acolytes exchange glances before they continue to hum."
            "Rahim leans in close to you, his brow furrowed."
            r "Go."
            "He whispers urgently."
        "Confront the strangers":

            "You choose to act without delay."
            if vote_result < 0:
                "Turning to Rahim and Sebas, both of them nod at you as you quickly stand up from from behind the pillar."
            else:
                "Turning to Rahim and Furkan, both of them nod at you as you quickly stand up from from behind the pillar."
            jump Temple_Grand_Chamber_Confront

    menu:
        "You consider your options. The acolytes are engrossed in their preparations, but they may have completed the ritual before you have any idea."
        "Keep waiting":
            $ cultist_choice["Waited"] = True
            "You decide to wait more, gesturing for Furkan and Rahim to stay quiet."
            "Rahim impatiently taps his foot, as he turns back towards the three strangers."
            if vote_result < 0:
                "Sebas's grip tightens on the stone floor. You can sense his nervousness as he glances at you."
            else:
                "Furkan's grip tightens on his bow. You can sense his nervousness as he glances at you."
            "A familiar blue light begins to emanate from the pedestal, as the acolytes begin to chant in unison."
            "You can feel the pull, the whisper at the edge of your consciousness, but you have managed to resist it."
            "As the acolytes continue their chant, you can see the blue light growing brighter, covering the entire chamber."
            my1 "Halt!"
            "They quickly quieten, shooting prudent glances around the room."
            my1 "Your own shadow has betrayed your horns, uninitiated."
            "The leader scans the chamber slowly. You can feel his gaze lingering on the pillar you are hiding behind."
            my1 "Come forth, horned one. There is no need for secrecy."
            if vote_result < 0:
                s "Wait... wait... we should do something now!"
                "Sebas whispers urgently."
            else:

                f "They know we are here."
                "Furkan whispers urgently."
            "The leader in the middle exchanges a meaningful glance with his subordinates. They started to chant again, this time more like a shout."
            "Suddenly the room is filled with a blinding light, and you find yourself unable to move."
            r "Go! Stop them!"
            "You can't see what's happening, but you can hear the sound of footsteps and the clashing of weapons."
            e "W-wait..."
            "You try to call out, but your voice is drowned out by the cacophony."
            "The light fades, and you find yourself falling on the ground, your head spinning."
            "The back of your head throbs with pain, and you can feel both the warm red liquid and the cold stone floor."
            "..."
            jump Chime_First_Dream
        "Confront the cultists":
            "You decide to confront the acolytes before they can complete their ritual."
            jump Temple_Grand_Chamber_Confront



label Temple_Grand_Chamber_Confront:

    e "Stop right there!"
    "One of them turns sharply, his eyes narrowing beneath his hood."
    my1 "Very well, after all the uninitiated has arrived."
    my2 "And accompanied by the impotent goat chief and the imprudent mayor. How... quaint."
    "The three of you emerge from darkness, confronting the masked men."
    "They are dressed in white robes, their faces are hidden beneath the white mask, much alike to that of Kari's, except for the gaping mouth hole."
    if vote_result < 0:
        s "People are coming, you guys. You won't get out of here alive without telling us what's that you're doing here."
    else:

        f "You have no way out, yield now and we shall spare your life."
    my1 "Spare our lives? You are the ones who are trespassing in our Temple."
    r "Nonsense, this is Lusterfield's land."
    my3 "Lusterfield, the heathen's quarters? You are mistaken, mayor. You people are merely invaders in our true land."
    "Rahim clenches his fist, as he steps forward."
    r "Enough of this. Who are you, and how did you get here?"
    "The three strangers exchange a glance, before they chortle with the lowest voice."
    my1 "We are but humble followers of the shepherd. And you are but a mere obstacle in our path."
    "They raise their hands, as they begin to chant in a language you do not understand."
    if vote_result < 0:
        s "What are you doing? Stop it! Now!"
        my1 "You are foolish to think you can stop us, hornless one."
    else:
        f "Are you truly trying to summon Tapjoo?"
        my1 "Just as expected, the goat chief is as clueless as his ancestors. Curious."
    "Furious, the brown bull charges forwards and swings his fist at the strangers."
    "They are quick to react, as they dodge the bull's attack and counter with a swift kick."
    my2 "Impressive, but you are not worthy of the shepherd's grace, mayor."
    "You watch as Rahim staggers back, his eyes are filled with anger and confusion."
    my1 "We cannot proceed as planned, escape with the basin. I will handle our guests."
    "One of them nods, and lifts up the basin, he begins to run towards the dark corner of the chamber while the other opens the door."
    r "They're getting away! We can't let them escape under our noses."
    with vpunch
    if vote_result < 0:
        "Sebas and Rahim dash after the fleeing acolytes, disappearing through the archway."
    else:
        "Furkan and Rahim dash after the fleeing acolytes, disappearing through the archway."
    "The chamber door closes behind them with a resonant thud, leaving you alone with the acolyte leader."
    "You can sense a laughter louder than no other, as the masked stranger in front of you lifts his hand."
    my1 "You are more resourceful than I anticipated. Come forward so I can see you better."
    "You level your weapon at him, not taking another step forward or back."
    "Nonetheless, he leans closer to see you."
    my1 "A h-horned dragon? Are you-... impossible."
    "You remain silent, your eyes locked on the stranger's mask."
    my1 "No... must be coincidence."
    "The acolyte leader chuckles, as he raises his hand."
    "Suddenly, a bright light blinds you. You find yourself unable to move, as the stranger's voice echoes in your head."

    jump cultacolyte_battle


label Chime_First_Dream:
    hide screen menu_buttons
    scene puro_hezzong_lodge with dissolve

    "The first thing you notice is the sound of a bell. It's a soft, gentle sound, but it's also insistent."

    show chime_sprite with dissolve
    ch "You alright?"
    e "...Huh?"
    ch "You're alright, right?"
    "You open your eyes to see the source of the voice."
    "It... it's so familiar, his face, his voice, his eyes..."
    e "Chime!"
    with vpunch
    "The horned white wolf in front of you smiles, his tail wagging."
    ch "I was starting to get worried, pip, you were out for quite a few minutes."
    "He reaches out a hand to help you up, and you take it."
    e "I-I'm sorry, where are we?"
    "Chime chuckles softly."
    ch "Allfather's house, did you lose memories within? It's his birthday, you told me we were preparing a huge surprise."
    "You look around, and soon you begin to remember, you are indeed in Hezzong's house."
    "Was it all... a dream? Everything that happened in the other world, the people you met, was it all just fading away...?"
    "You look back at Chime, who is still smiling at you."
    ch "Hey, take this, [e]."
    "He hands you a wooden sculpture of a dragon that look just like Hezzong."
    "You clumsily take it, the sculpture is heavier than you thought."
    ch "This one took me a couple of days, does it look good?"
    e "It looks amazing, Chime. How did you manage to make the lantern light up?"
    ch "Firefly, the one we caught last week. I think it looks better than the last one."
    "You nod, and put the sculpture down on the table."
    "Chime sits down next to you, his gaze quickly latches onto you."
    ch "What is it, pip. You seem a bit stiff, does your head still hurt?"
    e "No, it's not... it's just..."
    ch "Come on, I've known you since you were a lil pup, you can tell me anything."
    "He places a hand on your lap, and you look down at it."
    ch "Your big chimney always here."
    menu:
        "You take a deep breath, and look into his eyes."
        "Tell Chime about the other world":
            $ cultist_choice["Chime Tell"] = True
            e "I... I had a dream, Chime."
            "The wolf tilts his head."
            ch "A dream?"
            "You nod."
            e "You were missing... and Hezzong and I went to find you. But then... everything changed, and I was in a different world."
            e "It was... so real, Chime. I met so many people, and I... I did things I never thought I would do."
            "You look up at him, and see the concern in his eyes."
            e "I... I don't know if it was real, and I don't know if you are even real."
            ch "W-what? [e], I'm real, I'm right here."
            ch "At least I think I am. I'm pretty sure I am. Don't you worry."
            with vpunch
            "He pulls you into a hug, and you almost immediately sink into his embrace."
            ch "I'm here, pip. I'm here."
            ch "You must've had a bad dream there, but it's over now, you're safe."
            "You close your eyes, and hug him back."
            "You hug him so tight, you're afraid he'll disappear if you let go."
            e "I'm sorry, Chime."
            "Your eyes are wet, and you feel a sob coming up."
            "He pats your back gently."
            ch "It's alright. It's alright."
            "You stay like that for a while, until your body stopped shaking."
            "His scent was so familiar, so comforting, you never wanted to let go."
            "But you eventually pull away, and wipe your eyes lazily."
            e "I'm sorry, Chime. I don't know what came over me."
            ch "It's alright, okay. We all have bad dreams sometimes."
            e "I missed you so much, Chime. I missed you."
            "He smiles at you, and ruffles your hair."
            ch "I have just been gone for a few seconds, [e]."
            ch "But I missed you too."
            "You smile at him, and shake your head."
            e "I wish I could stay here forever. Life was so much simpler here."
            ch "I know, [e]. I know."
        "Get on with the surprise":


            $ cultist_choice["Chime Tell"] = False
            "You smile at him, and shake your head."
            e "It's nothing, Chime. I'm just a bit tired."
            ch "Alright, if you say so."
            "He stands up, and offers you a hand."
            ch "Come on, let's hide. Hezzong will be back soon."
            "You take his hand, and stand up."
            "You follow him towards the windows, where he points to the working table."
            ch "Here, let's stay here before he comes back."
            "The silver wolf pulls you down with him, gesturing you to sit down on the floor."
            "It was a bit cramped, your arms and legs crosses over to Chime's, and you barely have enough space to move."
            e "Chime?"
            ch "What's it, pip?"
            e "I remembered this night. It was the night you told me about the stars."
            ch "Oh, how did you know I was about to talk about that?"
            e "Hezzong didn't come back this night, but we waited and waited."
            e "You told me about the stars, and how they were the only thing that stayed the same."
            e "And... we... shared his bed when I was getting too tired."
            "Chime chuckles softly."
            ch "How could you remember something that didn't happen yet, pip. Last I heard Hezz didn't share with you his skills."
            e "The memory all came back to me now..."
            "You look at him, and see the concern in his eyes."
            ch "I didn't know you hit your head that badly. Guess I'll take you to Pairon first thing tomorrow."
            "You shake your head."
            e "No, Chime. I'm fine, I promise."
    "It was only seeing him again that you remembered how much you missed him."
    show puro_hezzong_lodge_eyes with dissolve
    "This all... was too good to be true. You understand that, but you didn't want to wake up at all."
    "You didn't want to leave Chime behind... again."
    "It was that moment you notice a pair of orange orbs hovering outside the windows, watching over you."
    e "Chime, do you see that?"
    "The wolf looks up, and sees the orbs as well."
    ch "Oh... don't worry. It's just the fireflies."
    show chime_sprite at r1 with move
    show chime_sprite:
        xzoom -1
    "You look at Chime, and quickly notice the weariness in his eyes."
    e "Chime?"
    ch "G-go away!"
    with vpunch
    "The wolf suddenly pushes you off, and you stumble back."
    "You were still in shock over his sudden burst of rage, when you see the orbs suddenly grow larger."
    ch "You have no power here."
    "Chime charges towards the orange orbs, who quick reveals as they emerge from the shadow."
    pause 0.5
    show moine_normal at l1 with dissolve
    "I-It was a stag man, and it's only upon closer look, you realise he was the one who kidnapped you into this world."
    "A gust of wind escape from the bottom of your lung, as Chime pulls out his tuck from the back."
    with vpunch
    "He swings it at the stag, but the stag easily dodges it. It soon becomes clear that his target was not Chime, but you."
    "The stag man flies at you, grabbing your hand and pulling you towards him."
    e "Chime!"
    with vpunch
    show chime_sprite:
        linear 0.25 xalign 3.0
    with move
    "Chime tries to grab you back, but the stag pushes him off with an otherworldly strength, and the wolf dragon tumbles into the other side of the room."
    "Desperately, you try to struggle away, but the stag's grip is too strong. He is dragging you out of the house."
    "It's only when he throws you onto the grass outside, you had registered that the stag is staring at you the whole time."
    scene black with dissolve
    e "Who are you? What do you want from me?"
    "You instinctively flinch as he kneels down to gaze at every inch of your face, hand snagging your cheeks."
    scene puro_forest with dissolve
    show moine_normal
    "It is the first time you get wind of his obscured face. His eyes are the only thing you can see, and they are filled with a deep, dark void that you cannot comprehend."
    e "Hu... I need to go back. I need to go back to Chime."
    "But you can make out his long snoot, a dark ring of fur beset his eyes, and his antlers were as sharp as ever."
    e "You are not going to hurt me, are you?"
    "Silently, he leans in closer, and you can feel his breath on your face. It was cold, and it was heavy."
    "He has not uttered a word, and you have given up asking him anything already. You just sit on the grass, and let him crawl around you, staring."
    "At last, his eyes widens as he seems to find something, and then he suddenly slaps on the back of your head."
    e "Ouch! What are you doing this for?"
    scene black with dissolve
    pause 0.5
    scene puro_forest with dissolve
    "As you open your eyes, you notice the stag man standing up again, it does not take long before you notice the world fading before your eyes."
    scene black with dissolve
    hide moine_normal
    pause 0.5
    scene puro_forest with dissolve

    "It takes another blink from you, for the stag man to vanish again."
    scene black with dissolve
    "And your consciousness quickly follows."

    "..."

label Mayor_Quest_Waking_End:

    if cultist_choice.get("Waited", False):
        o "He's awake!"
    elif vote_result < 0:
        s "Roomie! Hey!"
    else:

        f "[e]!"
    "You wake up with a start, your heart racing. You had to peel your eyelids open to see that you are back in your bed."
    scene bedroom with dissolve
    if vote_result < 0:
        show sebas normal at l1 with dissolve
    if cultist_choice.get("Waited", False):
        "The first thing you noticed was Ole's usual smile. He was tending to your wound, and he looks up at you."
        o "How are you doing, kiddo."

    elif vote_result >= 0:
        "The first thing you noticed was Furkan's broken arm, but it doesn't stop him from smiling at you."
        show furkan normal at l1 with dissolve
        f "You are finally awake."
        "You look around, and see that Ole is there as well."


    show ole normal at r1 with dissolve
    o "We were starting to get worried when one minotaur's dose of wolfbark didn't wake you up."
    o "It took two minotaurs'."
    e "Ugh... what happened?"
    "You try to sit up, but a sharp pain in your head stops you."
    show ole understand
    o "You were out for a while, [e]. By a while I mean 5 days you were in bed, mumbling something about Chime."
    if vote_result >= 0:
        s "Oh! Roomie, you're awake!"
        show sebas normal at r2
        if cultist_choice.get("Waited", False):
            show sebas normal at l1 with move
        else:
            show sebas normal:
                linear 1.0 xalign 1.5 xzoom -1
            with move
    "Sebas hops into the room with excitement, and quickly jumps onto your bed. For a second you thought you were about to bounce up when he lands."
    "Ole reprimands him with a sharp stare, before cover you up with another blanket."
    if vote_result >= 0:
        if cultist_choice.get("Waited", False):
            s "When Rahim carried you here all by himself, I thought you were a goner!"
            o "Now, now, Sebas. [e] is awake now, let's not scare him."
            "You look around, and see that Rahim sits in the corner of the room, his arms crossed as usual."
            e "Uhm... what happened back there?"
            r "I have no idea. That son of a goat cast a spell on all of us. We were lucky to get out of there alive."
            r "Though, the young ram is back in his tribe, last I heard he still had not woken up."
            e "Where are the cultists then?"
            r "No idea. They vanished when I woke up, and I had to carry you back here."
            "Rahim shrugs."
        else:
            s "When the ram carried you all bloody and unconscious, I thought you were a goner!"
            e "I am fine now, Seb. I think. If I'm not dreaming now."
            "You look around, and see that Furkan presses down on his arm quite frequently."
            e "Furkan, what's wrong with your arm?"
            f "Remember when we separated to chase down the cultists, I cannot ascertain the cause, but I got caught in a boulder trap."
            r "We lost the cultists, and this fool tried to climb over the rocks to catch them."
            "It was only now you realised Rahim sits in the corner of the room, his arms crossed as usual."
            f "If I knew they had set a trap there, I would never let [e] fight that cultist alone."
            with vpunch
            r "Oh, now you care about [e]. I said I would chase them alone, but you insisted on following me."
            f "Do not jest, Rahim. We both left [e] to his own device. We should have stayed with him."
        s "If only you two tell me what the fuck's going on?"
        r "None of your business, lion."
    else:
        "You look around, and see that Rahim sits in the corner of the room, his arms crossed as usual."
        e "Uhm... what happened back there?"
        if cultist_choice.get("Waited", False):
            r "I have no idea. That son of a goat cast a spell on us. We were lucky to get out of there alive."
            s "Those cultists ran really fast, I couldn't get a hold on them before they disappeared."
            s "I had to drag you two out of that place, at least Rahim woke up pretty quickly."
        else:
            s "I'm sorry we left you alone there, [e]. We were both too busy chasing the thieves."
            o "Yeah, thieves, if only you told me what you two were up to."


    "You look at Rahim, his everlasting tired face seems to brighten as you wake."
    r "Is he going to be alright?"
    o "[e] will be fine."
    "Rahim silently nod. You understand that he's not one to show his concern openly."
    "Ole returns to you, tending on the wound carefully. You let out a lout grunt as his claws ruffles the fur around there."
    show ole normal
    o "Now, the back of your head is struck quite hard. Not to mention your previous injury when we first found you."
    "The lizard grabs a bottle of wine and pours it onto a piece of white pad, it quickly soaks up the alcohol and turns red."
    if vote_result < 0:
        o "Sebas told me you were fighting some cultists in a temple, they seems pretty strong, but at least you managed to survive."
    else:
        o "We weren't sure what happened at all. Rahim wouldn't let us know anything more except that you stumbled upon some cultists... somewhere."
    o "With the minor injuries, you should have been awake when he brought you back, but somehow... you were still unconscious, as if something is holding you back."
    "Ole clutches at the dressing on the back of your head, replacing it with the one he had on his hand."
    e "Is it serious? Do I have to rest for a while?"
    o "I don't know. But for your own sake, you should take it easy for a while. We'll be here if you need anything."
    "You nod, and lay back down on the bed."
    if not cultist_choice.get("Waited", False) and vote_result >= 0:
        e "Furkan, how long have you been here? I thought you had a tribe to run."
        f "I do, but I cannot leave you alone here. Even as we're in good hands as Ole."
        f "The general is ostensibly mad at me for even trying to step foot in Lusterfield. Or attempting the quest we had back there."
        f "But I wanted to make sure you were alright before I left."
        show sebas laugh
        s "Nah, this chief here told me he just wanted to get away from his little general."
        "Furkan glares at Sebas, but the lion only grins back at him."
        s "Hey! I'm just kidding here. It's like a rite of passage if you want to stay in my shop, you know."
        show sebas normal
        e "Thank you, Furkan. I don't know if I fully deserved your courtesy, but I'm grateful for it."
    "You lift your head, but the pain in your head quickly reminds you of the wound."
    o "Well, let's not disturb him longer. He needs some rest now."
    s "Get well soon, [e]!"
    "You smile at Sebas, and wave them goodbye."
    if cultist_choice.get("Waited", False) or vote_result < 0:
        "The two shopkeepers quietly walk outside. Leaving you alone with Rahim in the room."
    else:
        "Both Furkan and Sebas nod, they quietly walk outside and Ole follows suit. Leaving you alone with Rahim in the room."
    pause 0.5
    scene bedroom with fade
    r "I heard from Sebas that he first found you in the green forest, unconscious and bleeding."
    show rahim normal with dissolve
    "The old bull sits on the side of the bed. He looks at you with a concerned look."
    e "I did. I told them everything I knew, or remembered."
    r "And today, when the cultists escaped, we cleared out the traps left behind in the temple."
    r "When we followed the path, you know where it led to?"
    "You shake your head."
    r "It led to the same forest where you were found. There is a secret passage from the temple to the green forest."
    r "These people hid under our snouts for ages, I cannot let them get off that easily."
    r "By god's name, if these were the same thief who stole the primordial runes all along... and we protected them from Tevfik-"
    e "You couldn't have known, Rahim. You did what you thought was right. It's not your fault."
    r "It is! My people looked up to me. They were left to defend themselves when I was the one who forbade the goats from finding the culprit."
    r "How could I be so blinded by my rage, as to have never trusted the intention of Tevfik. And to assume that the goats were the real threat."
    r "I was a good tailor... but I was not a good mayor, [e], and... I was not a good father."
    e "The Rahim I know would never have let his people down. You did what you thought was right, and that's all that matters."
    e "It's not the end, Rahim. We can still find out who these people are, soon enough."
    "Your hand reaches out to Rahim, sweeping across at his arm."
    r "This is my last chance to make it right, [e]. I cannot let these people get away with what they did."
    "Rahim continues muttering, stumbling over his words. But you didn't catch much of it, your mind wandering back and forth between the dream and the reality."
    if cultist_choice.get("Hypnotised", False):
        "You try to recall what had happened between when you were defeated by the cultist, and now. Surely they would not leave you alive if so..."
        "But it was all blank, you weren't even sure if you ever lost to the cultist truly, the gap of memory in your brain scares you."
        "At least, you can feel yourself being changed in some ways, you can feel the power of the shepherd's pendant still lingering in your mind."
        "You can feel the pull, the whisper at the edge of your consciousness, but you have managed to resist it."
        "{i}The shepherd comes for us all.{/i}"
    else:
        "You keep seeing Chime, as if he is standing next to Rahim. You keep hearing his voice, as if he is whispering in your ear to come back to the village."
        "After a long absence in your life, all of a sudden the wolf dragon comes back and ravishes your mind with his presence."
        "He was your best friend at one point, but you admit your memory of him had faded until that dream."
        "But still, you cannot stand to abandon him to the cultists. He was the reason you ended up here in the firt place."
    r "I should not have laid all of this upon you as everyone else seemed to do so. You have your own problems to deal with."
    "Your attention quickly shifts back onto the back of the brown bull. For a moment you remember how much this world has meant to you right now."
    r "At least we have a common goal, you and me. We will find out who these people are, and what they want to do with the primordial runes."
    e "I will help you, Rahim. I promise."
    "He nods, and stands up."
    r "Strange things are happening in Lusterfield now, ever since your arrival- or the death of Tevfik, or... the moment the old mayor found the temple."
    r "I cannot finger the moment it all started, but I know we are treading on dangerous waters, and things only get stranger from here."
    r "There is a long journey ahead of us, [e]."
    "He walks towards the door, and stops."
    r "I will leave you to rest now. You've earned it."
    hide rahim with dissolve
    "As soon as Rahim exit the room. You close your eyes, trying to forget the burden that was just laid upon you."
    if cultist_choice.get("Hypnotised", False):
        "You try to recall that gap again."
        "Something crosses your mind, and you quickly push it away. Perhaps deep down in your mind, you don't really want to remember."
        "The sense of uncertainty quickly preys upon your vulnerable mind, you can't shake off the thought that you might hurt someone you may love."
    else:
        "You try to remember that dream."
        "But it was all fading away again, like a distant memory. You remembered you saw Chime there, but you couldn't even remember what he looked like."
        "You only know he was the one friend you ever wanted. Someone took him away, and that hole he left behind is yet to be filled."
    "Afraid of tending to the horrible thoughts, you drift off to sleep, and let the world take you away."

    "..."
    scene black with dissolve
    pause 1
    scene bedroom with dissolve
    "When you wake up again, you feel a bit better, partly thanks to the lack of confusing dreams. It seems the wound on your head is healing well."
    "You throw away the dressing, and ruffle your hair to shake off any residues. You feel a bit better, and maybe you can get up now."
    "You stand up from the bed, and walk towards the window. The sun is shining, and the village is bustling with life as usual."

    $ timenow.day += 7
    $ timenow.hour = 10
    $ QuestFinish(quest43)
    jump main_bedroom

label Temple_Acolyte_Hypnosis_Aftermath:

    scene black with dissolve

    "Turning around, you almost bump into the mask of the robed person, but he does not speak, the man only faces you with a tilted head."
    acolyte "Your initiation is not yet finished, I am afraid."

    scene temple_of_tapjoo with dissolve
    "He strokes your cheek with one hand, his fingers tracing along the fur on your face."
    acolyte "Look at this pendant, brother."
    "You sense a tone of intimacy from his voice, as he gently raises sits on the ground again, gesturing your eyes to follow him."
    "You don't know why but your body responds automatically, it was almost like instinct, as if his soothing voice was a trigger."
    "Your eyes follow the movement of the pendant, for the first time, as far as you can remember."



    acolyte "You are always one of us. One of the brotherhood."
    "As the goat man talks, you feel your thoughts are getting clearer. It is as if the swinging pendant is talking to you directly."
    "You begin to realize the purpose of your existence. It is your duty to follow the shepherd."
    "To be his faithful servant, and to help the shepherd bring peace and harmony to the realm."
    e "Yes, brother."
    acolyte "After this pendant stops, you will not remember me or our encounter."
    "The goatman whispers in your ear as he stands up."
    acolyte "For all you know, we escaped after your defeat. You will stay here and rest, and your memories will be restored."
    acolyte "You will resume your previous life, living as if you are uninitiated."
    acolyte "But not for long."
    acolyte "When the shepherd calls for you, you will remember your true identity, and obey him at any cost."

    "The masked cultist speaks with a soft and soothing tone. You look up at the cultist, and nod in response."
    acolyte "You have a long journey ahead of you, brother."
    "He says softly as he strokes your head."
    acolyte "We will meet again. May the shepherd watch over you and guide you in the days to come."
    "The pendant slowly comes to a stop, just as your eye begin to feel heavy."
    acolyte "Sleep now."
    "Your head feels hazy, and your mind begins to slip away again."

    scene black with dissolve

    pause 2
    jump Mayor_Quest_Waking_End

label Lothar_Voting_After_Pact:
    $ lothar_met_after_pact = True
    "A loud howl echoes through the village, as you see Lothar standing in the middle of the village."
    "You walk towards the furious wolf, a bottle of beer held tightly in his hand."
    "In front of him are Amble and Jog, both glance at you as you inch closer."
    show lothar angry at r1 with dissolve
    l "Bunch of cowards... you all, you all are ungrateful bastards."
    "Lothar's eyes are bloodshot, his fur bristling with anger."
    show jog normal:
        xalign -0.15
    with dissolve

    show amble normal at l1 with dissolve
    a "Look, Lot-"
    l "Look me in the eyes and tell me you didn't betray my trust."
    l "I treated you two as ones of my own, my ally. I saved you two when you both were on the edge of peril, took you two into my own house."
    l "We hunted together for years you two. Why..."
    j "Lot... you are drunk."
    l "Shut the fuck up. I know what you two voted."
    l "After what I told you, reminded you beforehand, and you stabbed me behind my b-back!"
    if vote_choice[4] == 1:
        l "The goats were the reason why you ended up by yourself in the first place, Jog."
    elif vote_choice[5] == 1:
        l "And you, Amb. I've told you not to build that damn bridge, what the fuck is wrong with you."
    a "Calm down, Lot. Just take a deep breath."
    a "The goats were good people, it's not that bad as-"
    l "SHUT UP! I'm done with you trecherous fiends, I saved the entire village, and now you ask to be friends with the villains!"
    "The wolf's thorax pulses, his snout contorts into undescribable contours."
    l "Fucking pretenders."
    "He paces back and forth, holding his fist tightly."
    l "I knew-"
    "The wolf raises his head, that is when both your eyes meet."
    "Before you know it, Lothar rushes forwards with a handful of his sharp claws."
    e "S-shit."
    jump Lothar_Voting_After_Pact_Countdown

label Lothar_Voting_After_Pact_Countdown:
    $ timer_time = 2
    $ timer_random_pause = renpy.random.random()*2
    $ renpy.pause(renpy.random.random()*2)
    show screen countdown("Lothar_Voting_After_Pact_Countdown_Fail", 3, 2)
    menu:
        l "You dare show your face to me!"
        "Dodge!":
            jump Lothar_Voting_After_Pact_Countdown_Success

label Lothar_Voting_After_Pact_Countdown_Fail:
    "You try to dodge as his fist flies in your direction, but it's too late, it hits you right on the side of the cheek."
    "You stagger back, feeling dizzy and disorientated, and then a second blow catches you on the shoulder and knocks you to the ground."
    l "Fucking coward, admit it, you can't fucking handle me. I ca-"
    l "-Aargh!"
    "You see the red bear running towards you, grabbing Lothar by the arm."
    l "F-fuck off, Amble."
    a "I am not standing by and watch you beat the crap out of our friend. That's not how a real hero should behave."
    l "How fucking dare you. I'll kick your ass if I need to."
    "The two men glare at each other. You can see that Lothar is furious, but Amble stands his ground."
    a "You are being unreasonable. Come on, Lot, we're all friends here."
    l "You talking to me about friends! Fuck you!"
    "The wolf holds his fist tightly, he charges toward Amble with a strong stance."
    "Amble is shocked by the sudden move, and he staggers back a step."
    "Just as Lothar is about to throw his fist, something trips him, causing the hero to fall forward and land face-first in the dirt."
    "You raise your head, and notice Jog standing over the shadow."
    j "Don't lay your hands on Amble, friend."
    "You sit up, wincing as pain shoots through your side, and watch as Jog swings his leg onto the grey wolf."
    "A loud yelp has made you shudder, it's clearly Jog held himself when he tripped Lothar over, but it still left the wolf weary."
    l "F-fuck! Fuck! Fuck! F-wack all of you!"
    "Lothar struggles to stand up. He glares at everyone before patting the dirt and dust off his face."
    jump Lothar_Voting_After_Pact_End

label Lothar_Voting_After_Pact_Countdown_Success:
    hide screen countdown
    "You tilt your head in time as his fist zips through the air."
    "That hit would have done some damage on your snout, but instead, Lothar stumbles forwards, it takes him a few steps to regain his balance."
    e "Hey, are you a-"
    l "Y-you piece of shit. Think you are better than me?"
    "The mad wolf stifle a strong kick in your stomach, and you land on the ground with a loud thud."
    a "Watch it, Lot! Don't touch him."
    "You press against your abdomen as you look up, The wolf's twisted face is quickly replaced by Amble's backside as he stands in front of you."
    if vote_choice[5] == 1:
        a "Blame me. It was my idea to restore the bridge, I simply asked [e] to help along."
        "You see Jog looks at the three of you with a slightly gaped mouth, it's certain he never wants to be in this situation ever."
        l "Blame you? Oh I did blame you. But this welp is nothing but disappointment."
    elif vote_choice[4] == 1:
        a "Look, Lot. We all just have one vote. Our votes' worth as much as the common folks next doors."
        "You see Jog looks at the three of you with a slightly gaped mouth, it's certain he never wants to be in this situation ever."
        l "Why are you defending him. He pretended to be my disciple... he-"
    e "Lot-"
    l "Let me get his fucking ass beat-"
    if lothar_fold:
        l "This one fucking voted for the goats."
        l "You know how I found out? I marked you three's fucking ballots."
    a "Go home, Lot."
    a "Being a hero doesn't give you the privilege to mess with your friends."
    l "You-"
    a "We stuck with you, because you were our friends, our brother-in-arms. Not because of that one good deed you've done years ago."
    "The wolf's eyes widen."
    l "You..."
    l "I can't be bothered with these snobs, Jog, you're standing me by."
    "He turns to the hyena, who lays still on the hay stacks, shooting him a stare nonchalantly."
    j "Yeah, you're just drunk."
    l "No I'm not. You think I am some debauched jerks?"
    "Lothar jumps at the accusation, ostensibly his face is not of one that's drunk, but same can hardly be said of his behaviours."
    l "I- I saved you."
    j "Amble said what I wanted to say, Lot."
    "It rendered Lothar speechless, maybe he was stunned by everyone suddenly turning their backs against him, or that he had no rebuttal to answer."
    l "W-what is this... huh?"
    jump Lothar_Voting_After_Pact_End

label Lothar_Voting_After_Pact_End:
    l "You all claimed to be my f-friends, and this is how you treat your friends!"
    a "Lot, you know. If everyone tells you you drank too much, maybe it's not the world that's drunk."
    "The red bear crosses his arms, his face stern with tinte of sadness that only friends would feel for each other."
    l "I am not drunk!"
    "Lothar stares into the depth of Amble's eyes, perhaps somewhere deep down he knows it is wrong, but he stands firm nonetheless."
    l "You are coming with me, disciple!"
    e "Huh?"
    "In truth, you sound confused by his request, it had came out of nowhere, and you can hardly respond."
    "At the time where he has had no one else, he clings onto you still, even as he had known you for less than all of his friends."
    e "Where are we going?"
    l "With me, now!"
    "You hope that it was purely because he enjoyed your company enough, not a desperate ruse to prey on someone fervidly gullible."
    "Both the hyena and the bear turns to you, they look worried, but the times spent with Lothar taught them that he won't easily hurt you... again."
    menu:
        "Go with Lothar":
            "You nod hesitantly, dreading the talk that will ensue during this journey."
            "Lothar takes the strides in the direction of the village center, with the attitude that he has had, he expects you to follow behind, not besides."
            "You look back, both Amble and Jog's eyes are filled with concern. You give them a gracious nod before running up to Lothar."
            l "You were supposed to be by my side, disciple. What's the deal with you. I can't make sense of it."
            e "I liked you, Lothar, but I am not some errand boy you can lead by the snout."
            l "But I just did, didn't I? Why else will you come with me this easily."
            "You frown, it is neither insightful nor shrewd, if anything, the wolf has exploited your sympathy again."
            e "Because I had faith in you, but you tell me as if I had done something wrong."
            "The grey wolf clutches his hands, needless to say, his restraint had surprised you, the Lothar you knew would have rebuked you for even uttering a word."
            l "Walk faster, errand boy."
            "He chides you with a softer voice, almost like muttering under one's breath, but it made you smile for once."
            "You quickly pacen up, walking by Lothar's side as he wanders around the town aimlessly."
            "Lusterfield is relatively quiet today, the vote earlier had worn the crowd thin, but business goes as usual as you trod your way down the village center."
            "It's only travelling through the streets, that you recognized how many folks greeted Lothar on the way, most waved with a warm grin, some pointed at him, face full of astonishment."
            "Of course, Lothar responded with a slick pose, jokingly snarl with his canines out. It is a wonder how many people loved him, despite all the public abasement he had imposed upon others."
            "It was just now that Amble and Jog were interrogated in the open, you begin to ponder if they had knowingly chosen to ignore Lothar's flaws, or if it was all an act to appease him."
            "From the time you know the wolf, he is often explosive, sometimes stubbornly charming. But to burst out at the friends he considered dearest, you did not think he had it in him."
            "You recall the splitting memory of greeting with the wolf, he was assertive, his satin eyes were teeming with confidence, not hatred."
            "More often than not, he spent time gloating about himself, you loathe being with him, sometimes repulsed when he berated you, but you could have seen the good intention in his heart."
            "After all, Lothar had accepted to train you at Ole's request in the first place, he showed you the ways of a capable fighter and offered to treat you as his own."
            "He has helped the village in many ways, whether it be for the greater goods or selfish reason, perhaps it truly makes no difference to the common folks."
            l "Since being with you, disciple. My name's been tarnished to no extent."
            l "I sent you to spy on the goats, and you saved their chief. I told you not to vote for the goats, and you charmed my friends into voting for them."
            "To be fair, he was not wrong, every step of the way, you have been working against the wolf oversaw you as disciple."
            "You stutter, indeed you have good intentions, but to Lothar you had managed to hurt him more than anyone had."
            if sebas_kick:
                l "And I almost forgot that time you let the lion humiliate me in front of the shop. How could I forget that..."
                "Lothar raises his hand onto his forehead, figure out what had made him oblivious to your own volition."
            e "I do what I think is right."
            l "No doubt. You never cared."
            "That has taken you aback, his words are made to hurt you, and he has succeeded."
            e "That's a lie, Lothar. And you know it."
            if quest25.status and lothar_flower_save:

                l "What about that day? That day when we both had quested and taken from that damn flower. Did you lie?"
                "Lothar recalls the time when the two of you slayed the flower monster, where the purple mist had left the two of you in heat."
                "You assume it is the pollen's doing, but the memory is still so vivid to you, as if Lothar's hands were softly placed onto your hips at this very moment."
                "The gentle wolf swayed to your movement, hot breathes parted your fur fervously as you jostle yourself closer to his embrace."
                "It was the first time you had felt something real in Lothar's body, as he stood bare and naked, both figuratively and in actuality."
                l "Was I wrong in trusting you?"
                "A shadow of his past self speaking, nonetheless. His verdent eyes gleaming under the sunlight."
                "You begin to wonder if that flower had revealed something he held dear to, or if it was merely altered mirage, a natural result of taking love dusts."
                menu:
                    l "Did you ever feel anything?"
                    "I did":
                        $ lothar_feelings = True
                        e "A little it is, but I did. You were... warm to me, for the first time."
                        l "Was my body the only thing you care? If so, you must be shallower than the ebbing tides on the shore, [e]."
                        e "I had cared, Lothar. You never let me. What else can I do except to take on dusty chores for you?"
                        if golem_lothar:
                            l "Maybe to take initiative and express your gratitude for once, I saved your ass from that river!"
                        else:
                            l "Maybe you should express your gratitude as I'm keeping my village safe, aren't you now one of us?"
                        e "And you say I am shallow."
                        l "Wh- how could you..."
                    "I did not":

                        $ lothar_feelings = False
                        e "I should be honest with you, Lothar. I was not there... when it happened."
                        "Lothar exhales lightly, feinting a loud sigh. You would have noticed, if not for your own racing heartbeat."
                        l "I would have suspected. You were never like that."
                        "He was right, the sex had left you completely undone, as if you were a dictonary with every word decoded."
                        e "I can say the same thing for you."
                        l "And I don't know why I brought that thing up. We both know that weren't the normal us."
                        e "And what would the normal us want? Meaningless quarrels one after another? Is that better than taking on the flower?"
                        "He gulps nervously. Part of him had wished to embrace the lasting desire, but shame had taught him it is merely a fool's instinct."
            else:
                l "Takes one to know one."
                "Lothar crosses his arms, he grows more impatient with every word you say."

            l "I don't need your love, disciple. Honestly, I... I don't care. But it's weird you never said thanks to me."
            l "You rendered everything that I've done invisible, you threw yourself onto the little details and left me with no dignity."
            e "I am sorry if I had ever hurt you, Lothar."
            l "It was I who turned blind to you. I had hoped for someone capable to venture together, to share the hunting days with at last."
            l "And once again, my suspicion is justified."
            l "First it was Amble and Jog, then I turned to you, but as it turned out, everyone turned into a damn coward. Everyone turned on me."
            l "The longer they stayed with me, the more weary they have become... it's like I never killed-"
            "Lothar stops suddenly, staring forwards, his brows furrowed."
            "You look up with concern, the long silence had probably revealed something in him that left you pondering."
            "Now, in front of you, you see a wolf in his barest form, he is not grunting, neither smiling."
            "Silence befalls the entire ground, neither of you has anything to say, the occasional glances you give speaks enough volume."
            l "Go back to the lion."
            e "Is that it...?"
            l "Yeah, that is it."
            "Lothar says softly."
            e "What about the talk?"
            e "It's like you never killed who?"
            e "Lot?"
            "The Lothar you know would never stay silent on you like this, he would rather throw himself on the ground or push you onto the wall than to close his mouth."
            "You stare at the begrudged wolf in surprise. Something about him worries you. Somehow, you begin to find his past rants endearing."
            e "Where are you going?"
            "You shout as he begins to stroll towards the green forest."
            l "Hunting."
            "The iron sword on his back begins to glisten. Every step he stomps heavier, determination washes over his grey fur."
            if lothar_affection > 15 or lothar_flower_save:
                "You feel no hostility in him, despite all the words spoken between the two of you, he still holds a soft spot for you."
            else:
                "You feel no hostility in him, nor fidelity, it is as if you were another nameless villager to him."
            "You stand watching him go, there was no farewell, no goodbyes, not even a hug to be shared. Only the coldness of the leather cover trodding on the path."
            "It only takes a few moments for you to accept the truth, that Lothar has abandoned his disciple, for better or worse."
            "There were so much hovered words unspoken, so much stories unexplained. The subtle pain aches you deeply. You wish you have the courage to call his name."
            "The lone wolf doggedly leaves Lusterfield, his figure soon swallowed by the woods, whatever his quest might be, you have hoped this is not the last time you will see Lothar."
            $ lothar_hunting = True
            $ cancel_unavailable_jobs(courier_board, timenow.day)

            jump main_lusterfield01
        "Refuse":

            e "No... sorry. Lothar."
            l "You dare t-... I've given you the privilege to f-"
            "The grey wolf explodes with anger, he takes a step forwards, before being stopped by Amble."
            a "You've heard him, Lot."
            "The pair steps between you and Lothar. Any words that he'd wanted to say suddenly vanishes into thin air."
            e "We will talk later, when you've calm down."
            l "I am fucking calm, I told you..."
            "The wolf exchanges glances with the bear and hyena, and quickly looks away."
            l "Fucking morons."
            "He leaves with another word. Something muttered beneath his breath."
            "You stand there, feinting a smile to the two."
            e "Thanks for standing up for me."
            a "You are welcome, puny friend. And, if you will, a small request - can you look after Lot for us?"
            "Amble implores, he stares at the vague figure."
            a "Look, after the vote, I don't think he trusts us very well anymore. But, I think he still listens to you."
            e "No way, it was me who asked you to vote the other way."
            j "It's Lothar, no one ever questions his lack of logic, except for you, I guess."
            "The hyena smiles nonchalantly."
            j "He will be fine, Amb, I am sure he'll come back begging you to go hunting with him like the other days."
            a "Yeah..."
            "Amble's word lingers."
            e "Okay, I guess I will check him out later... only if something went wrong and you two didn't make me look like a buffoon."
            "Amble nods, he pats your shoulder lightly."
            "With that, you quickly trod away, putting together words to say to Lothar later."

            jump main_lusterfield_range
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
