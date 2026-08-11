

label Cane_JumpFirst:
    hide screen menu_buttons
    if cane_bet == True:
        jump Cane_Bet_Dialogue
    if nocturnal_serve >= 3 and renpy.random.random() > 0.4 and quest07.status == False:
        jump Cane_Apron_Quest
    else:
        jump Cane_Dialogue

label Cane_Bet_Dialogue:
    scene black
    if isNight():
        scene nocturnaltrunk_night
        with fade
    else:
        scene nocturnaltrunk
        with fade
    show cane normal
    with dissolve
    e "Hey, Cone. How's the Tavern doing."
    c "Ya want me to tell ya my name again? No way."
    e "I already know your name. I just wanted to talk..."
    c "Look, come here next time and ya can talk all ya want. Respect the bet integrity ya dink donk."
    e "Ok..."
    jump main_nocturnaltrunk2

label Cane_Dialogue:
    if isNight():
        scene nocturnaltrunk_night
    else:
        scene nocturnaltrunk
    show cane normal
    with dissolve
    if isNight() and sebas_location == "nocturnaltrunk":
        if ole_location != "nocturnaltrunk":
            c "Welcome to the Nocturnal Trunk!"
            c "Yer little lion friend is there, see him?"
            e "Hmm... what did you do?"
            c "I don't know, he voluntarily betted with me. It's not my fault he lost or something."
            e "A-alright..."
            jump Cane_Normal_Talk
        else:
            c "Welcome to the Nocturnal Trunk!"
            c "Yer two little fuckmates are waiting for yer ass, come go join them."
            e "Hmm... you mean Ole and Sebas?"
            c "Aye. Lion is always here. But I didn't know lizards eat bread until now, colour me surprised."
            e "A-alright..."
            jump Cane_Normal_Talk
    if renpy.random.random() > 0.5 and pc.armor["Clothes"] == None and pc.armor["Pants"] == None:
        c "Welcome to the Nocturnal Trun-...?"
        e "Hello, Cane."
        c "Ya really think I'd take the bait here, [e]."
        e "What are you talking about, Cane."
        c "Cover yer cock, ya dink. I'm not serving some donks who goes out naked in the public."
        $ naked_cane += 1
        jump Cane_Normal_Talk
    elif renpy.random.random() < 0.5 and nocturnal_serve > 1:
        c "Welcome, welcome, [e]. Fancy helping with our plates and mugs 'ere? We're gettin' a lil busy now."
    elif renpy.random.random() < 0.3 and tavern_date[0] + tavern_date[1] + tavern_date[2] > 1:
        c "Welcome [e]. Just so ye know, some patrons requested private shows from yer ass."
    elif renpy.random.random() < 0.3 and cane_favour:
        c "Aye, welcome again, [e]. How's it going, my lad."
        e "Very good, actually. Thank you, Cane."
        c "I've been feelin' better, since that night I spent wit' ye."
        if cane_lick:
            c "Ye was still a good lad, just that I hadn't been myself for years, forgot what that means."
            e "I understand, Cane. Don't fret about it."
        else:
            c "I'm glad to have ye around. Visit m' more often, lad."
            e "Of course, don't ye worry, Cane. I'll be here helping you out."
    elif renpy.random.random() < 0.2 and quest22.status:
        c "Welcome, [e]. The nocturnal trunk always welcome ye cute lil face here, lad."
        e "Hello, Cane."
        c "I heard ye running into some werewolves folks there, I wanna worry for ye, but..."
        c "Well, always be careful."
        if cane_favour:
            c "For m' and everyone who cares for ye, alright?"
        else:
            c "For everyone 'ere, right? We don't wanna lose a good lad to them scoundrels."
        e "I will! How else can I come back to see you, Cane."
    elif renpy.random.random() < 0.35 and quest16.status and quest16.completed_date + 10 > timenow.day:
        c "Welcome, [e]. Gettin' used to 'ere now?"
        e "I do, Cane."
        c "That party the lion threw was somethin' else. Been a while since we see everyone in the same place."
        e "Yeah, I think despite some hiccups, everyone had fun, I saw you talking with Rahim there too."
        c "Heh, everything can change in seconds, but that stubborn old bull's still the same, after all those years."
    elif renpy.random.random() < 0.5 and quest33.status and pirkka_location == "nocturnalupper":
        c "Welcome to the Nocturnal Trunk, m' lad."
        e "Hey, how's it going?"
        c "Good, tavern's gettin busier with a bard by the hearth, but I've got no goddamn idea what he's singing about."
        e "Oh, Pirkka? He does have a thick accent when he's singing sometimes."
        c "Aye, he's upstairs right now, told him about private shows and all that. Lad has a good heart, wonder if he'll stay for long."
        c "Maybe I'll pay for him to stay even. Rumor says he has a way with his mouth."
    elif renpy.random.random() < 0.4 and upper_explore > 0:
        c "Welcome to the Nocturnal Trunk, m' lad."
        c "Heard some banging upstairs that other day, turns out the regular's been playing cards again."
        e "Oh, they've been sitting there for a while."
        c "The card and table gettin messier everytime they borrow from m' shelves. But they stay up for days there."
        c "Just don't break m' tables when ye... go upstairs, lad. Or straight up don't owe money. They've got more up their sleeves than ye think."
    else:
        if cane_tut == 1:
            c "Welcome to the Nocturnal Trunk, outsider."
            e "Why are you calling me that name?"
            c "Well are ya not an outsider? Why can't I call ya outsider, outsider?"
            e "Hmmph..."
            c "How about [e], does that sound better?"
            e "Yes... Thank you.. Cane."
            $ cane_tut += 1
            jump Cane_Normal_Talk
        else:
            c "Welcome to the Nocturnal Trunk!"

    jump Cane_Normal_Talk

label Cane_Normal_Talk:
    menu:
        c "Whatcha going for, [e]?"
        "Ask to work in the Tavern" if lothar_night > 1 and timenow.day > 1:
            jump Cane_Work
        "Learn his opinion on the vote" if quest37.status == 2 and quest37.start_date + rahim_vote_duration - 1 >= timenow.day and quest45.status == False:
            jump Cane_Voting_Opinion
        "Ask about the rat patron" if quest45.status == 2 and cane_dialogues.get("Rat Patron Info", False) == False:
            jump Cane_Voting_Quest_Ask_Rat_Patron

        "Report about the rat patron" if quest45.status == 2 and cane_dialogues.get("Rat Patron Info", False) != False:
            jump Cane_Voting_Quest_Report_Rat_Patron
        "Report that you have gotten drunk" if quest45.status == 3 and cane_dialogues.get("Moth Route", False) == "Beer" and has_active_status("Drunk"):
            jump Cane_Voting_Quest_Beer_Route_Meet
        "Continue with crafting Topu's Beer" if quest45.status == 4:
            jump Cane_Voting_Quest_Draft_Beer_Menu
        "Ask about Topu's beer recipe" if quest45.status == 5 and not has_active_status("Buzzing"):
            jump Cane_Voting_Quest_Craft_Beer_Ask
        "Report that you have drunk Topu's Beer" if quest45.status == 5 and has_active_status("Buzzing"):
            jump Cane_Voting_Quest_Draft_Beer_Drinking
        "Pick up the delivery" if is_client("Cane"):
            $ client_name = "Cane"
            call Courier_Pickup_Dialogues from _call_Courier_Pickup_Dialogues
        "Deliver the goods" if is_recipient("Cane"):
            $ recipient_name = "Cane"
            call Courier_Delivery_Dialogues from _call_Courier_Delivery_Dialogues
        "Give Cane the Fixed Apron" if quest07.status == 3 and (LookForItemDefense("Tavern Apron", inventory) == 8 or (pc.armor["Clothes"] != None and pc.armor["Clothes"].img == "Tavern Apron" and pc.armor["Clothes"].stat[12] == 8)):
            jump Cane_Apron_Quest_End
        "Ask to drink the mysterious beer" if quest45.status == 4:
            jump Cane_Voting_Quest_Draft_Beer_Menu
        "Ask about his opinion on the Goat Tribe" if quest06.status == True  and quest06.completed_date + 1 < timenow.day and opinions_GoatTribe[4] == 0:
            jump Cane_Ask_Goat_Tribe
        "Ask about the Beer Task" if quest07.status == True and timenow.day > 12 and taskAvailable(task02, quest07):
            jump Cane_Beer_Task_Begin
        "Report to the Beer Task" if task02.status == 2:
            jump Cane_Beer_Task_Report
        "Talk about the Night with Sebas" if sebcane == 1 or sebcane == 2:
            jump Cane_After_Sebas_Tavern_Night
        "Ask about the favour" if task02.completedtimes >= 3 and tavern_date[0] + tavern_date[1] + tavern_date[2] >= 3 and cane_favour == False:
            jump Cane_Favour_For_Ya
        "Accept the Private Show Offer" if privateshowing == 1 and quest18.status == False:
            jump Cane_Private_Show_Quest_Accept
        "Report for the Private Show Preparation" if quest18.status == 2 and LookForItemNumber("Cheap Pillow", inventory) >= 2:
            jump Cane_Private_Show_Quest_Finish
        "Ask about your outfit" if pc.armor["Clothes"] != None and pc.armor["Pants"] != None and quest09.status != False and quest09.status != True:
            if pc.armor["Clothes"].img == "Adventurer Armor" and pc.armor["Pants"].img == "Adventurer Leggings":
                jump Cane_Outfit_01
            elif pc.armor["Clothes"].img == "Tavern Cloth" and pc.armor["Pants"].img == "Tavern Chaps":
                jump Cane_Outfit_02
            elif pc.armor["Clothes"].img == "Flowy Robe" and pc.armor["Pants"].img == "Flowy Wrap":
                jump Cane_Outfit_03
            else:
                "As you are about to ask, you realise you are not putting on the right clothes to judge..."
                jump Cane_Normal_Talk
        "Order something":
            jump Cane_Order
        "Ask about Lusterfield{#CaneAAl}":
            jump Cane_Ask_Lusterfield
        "Ask about the tavern":
            jump Cane_Ask_Tavern
        "How is he doing":
            jump Cane_Ask_Himself
        "That's all for now":
            jump Cane_Dialogue_End
    jump Cane_Normal_Talk

label Cane_Work:
    if quest18.status == True:
        e "Cane, Can I get some work here?"
        menu:
            c "What'cha thinkin. Ya be a Server or show yer patron some ass?"
            "Work in the Private Show":
                e "Hey, Cane! Can I... ask if I can work on the private show?"
                c "Yer in luck, my lad! Or rather, we've got a lucky patron."
                c "Ye've a patron waitin' for ye in the backroom."
                c "I'll hand ye the pay once yer done."
                menu:
                    "The pay's 100 gold, ya in?"
                    "Yes":
                        pass
                    "No":
                        e "I'll need to think more, thanks Cane."
                        c "Eh... Alright. don't leave 'em hanging for too long, lad."
                        jump main_nocturnaltrunk
                e "O-ok! Thank you, Cane."
                stop music fadeout 1.0
                jump Cane_Private_Show
            "Work as a server":
                pass
    if nocturnal_serve < 1:
        e "Hey... Cane. You talked about working in the tavern, right?"
        c "Yeah?"
        e "It looks pretty interesting, how is the wage here?"
        menu:
            c "Aye, its 50 gold for 4 hours, I'd pay more if yer work hard enough."
            "Take the job":
                $ lastServe = timenow.hour + 4
                $ dayServe = timenow.day
                jump Cane_Serve_First
            "I'll think about it":
                e "I'll think about it, Cane."
                c "All good. Well then, enjoy yer stay in the Nocturnal Trunk!"
                jump Cane_Normal_Talk
    else:
        e "Hey... Cane. Can I work in the tavern again?"
        if timenow.hour - 4 > lastServe or timenow.day > dayServe:
            menu:
                c "Aye, same wage. Its 50 gold for 4 hours."
                "Take the job":
                    $ lastServe = timenow.hour + 4
                    jump Cane_Serve_Later
                "I'll think about it":
                    e "I'll think about it, Cane."
                    c "All good. Well then, enjoy yer stay in the Nocturnal Trunk!"
                    jump Cane_Normal_Talk
        else:
            c "Mister [e], ya had already served the whole village 'ere. Come back after a few hours ya thirsty lad."
            e "...Ok, Cane."
            jump main_nocturnaltrunk2

label Cane_Order:
    e "I want to order something from you..."
    if task02.completedtimes > 0:
        c "Of course ya dink donk, we've got beer for 15, and our new Ale for 20 gold. Want one?"
    else:
        c "Of course ya dink donk, we have some beer right now, takes ya 15 gold. Want one?"
    menu:
        e "hmmm...."
        "Get a beer for 15 gold":

            if pc.gold >= 15:
                $ pc.gold -= 15
                $ addItem("Beer", inventory, 1)
                e "I'll take one beer."
                c "Good, here's yers, enjoy."
            else:
                e "I'll take one."
                c "Uhh... Ya dummy, look at yer pouch, [pc.gold] gold is not enough for a beer, mister."
                e "Oh... sorry about that."

            jump Cane_Normal_Talk
        "Get an Ale for 20 gold" if task02.completedtimes > 0:
            if pc.gold >= 20:
                $ pc.gold -= 20
                $ addItem("Ale", inventory, 1)
                e "I'll take an ale."
                c "Good, here's yer ale, enjoy."
            else:
                e "I'll take one."
                c "Uhh... Ya dummy, look at yer pouch, [pc.gold] gold is not enough for an ale, lad."
                e "Oh... sorry about that."
        "I'll think about it.":
            e "I'll think about it later."
            c "Ya better."
    jump Cane_Normal_Talk

label Cane_First_Time_Upstairs:

    c "Hey, lad. Right 'ere!"
    "Cane shouts from behind you as you go upstairs, you turn around and see him quickly leaves his usual counter."
    e "Oh! Cane, I was about to ask you about what's up there."
    show cane normal with dissolve
    c "Well. And I was about to tell ya."
    c "Just renovated the place. With the pink bear lad's help too. We re-decorated everything from scratch, and cleaned up old tables for use."
    e "Isn't it the same as down here?"
    c "Well, lad. For what it's worth, my knee's been sore for the better part of m' life, I can't keep handing out dishes and beer up there and down. That's why we'd closed off the floor at first."
    e "What changed your mind?"
    pause 1
    "Your curiosity causes the old bat to smile nervously. A kind of friendliness that you seldom see with other patrons."
    c "I ought'a thought with yer help and everyone else, somethin' getting me all excited about..."
    c "Cane smiled warmly at you, his eyes twinkling with affection."
    "Cane chuckles again."
    c "W-well, the tavern. It's gettin' quite filled 'ere. "
    c "The regulars understands and they'll get what they want themselves, so I thought, why not let 'em have their fun, y'know, bringing in all 'em customers and gold."
    e "That's really good to know, Cane. I'll do my best to help."
    c "Aye, after all, upstairs' reserved for the most loyal regulars and visitors..."
    c "...and the finest lad right 'ere. Haha, c'mon then, give ye old bat a hug."
    pause 2
    "Without thinking, Cane steps forward and wraps his arms around you on his giant belly."
    "You are momentarily startled, but quickly recovers and returns the hug warmly."
    c "I'm gonna miss ye little sleazy ass when yer away."
    e "Cane, I'm not going anywhere else."
    "You talk right inside of Cane's intimate embrace, his purple fur strokes your cheeks as you dig your head deeper into him."
    if cane_favour:
        c "Lad, I still haven't forgot that time we were in my room..."
        e "You trust me, right?"
        if cane_lick:
            c "I do, lad. I really do."
            c "And I can't let you go that easily."
            "You can feel him hugging you tighter, one with an irrational amount of regret."
        else:
            c "Mhmm... I wish ye'd stay with me, and the tavern every day."
            c "But it's impossible to ask for an adventurer like ya."
            c "So, this is the second greatest thing I'd wish for..."
            "You can feel him hugging you tighter, savouring what's happening in the present."
    else:
        "He doesn't speak, instead he hugs you tighter, savouring what's happening in the present."
    pause 3
    "Eventually, you two pull away from each other, you don't know if it's his unique odor or his cheeky smile, but a sense of warmth can still be felt across your body seconds later."
    if not cane_favour:
        c "Ya better be."
    "His smile widens, his hand raises above your head, playfully scruffling your hair."
    c "There's no rules upstairs, and some of 'em I know, are... mischievous. So keep yer eyes out for me, ye?"
    e "I will."
    c "Good, 'en I'll leave it up to ye."
    "Cane turns away, and returns to take care of his business."
    "You unwittingly smiles at the kindness of the tavernkeeper, and quickly runs upstairs."
    jump main_nocturnaltrunk_upper


label Nocturnal_Trunk_Cardy:

    "You walk over a table in the corner, it seems to be scattered with coins and bags, almost as if you've stumbled upon a treasure trove."
    if cardgame_encountered >= 1:
        "As usual, it's the three regulars, playing and bantering around the table."
        "They take notice of your prescence rather quickly, and wave their cards at you."

        if cardgame_played == 0:
            fokk "Well, well well. Look who he is! Our all and mighty server of the tavern."
            gato "Bet this sorry arse' coming to ruin our fun again not even sitting down"
            "Fokk chuckles, and motions you to sit on the chair."
            fokk "Changed ye mind? There's always an empty chair for ye to sit on."
            $ cardgame_encountered += 1
            menu:
                "Play Card Game with the regulars":
                    jump Nocturnal_Trunk_Cardy_Ready
                "Decline":
                    e "Well... I'll pass."
                    coit "What a party stopper ye're, get me some bread at least on yer way down, would ya?"
                    gato "Or, get yer arse beaten fer wasting our time."
                    "Fokk awkwardly smiles."
                    fokk "Alright then, the chair's not going away anytime soon."
                    fokk "And Coit's joking, he doesn't eat bread."
                    jump main_nocturnaltrunk_upper
        else:
            fokk "Well, well, well. Look who it is! Our server here on the table."
            e "Hey, are you all playing cards?"
            if cardgame_lost_sex > 0:
                fokk "Playing cards we are, just taking a break to count the coins and talk about yer arse."
                gato "Bet'cha he's coming for the bloody table."
                coit "If ye want to be the tavern's cum rag, we can always, ye know, skip to the main course."
                gato "His pucker must be clenching so hard right now, keepin' it tight fer us to use right 'ere."
                fokk "'ey, ye tosspots, don't scare our precious server away with ye blabbering mouth, we can always go for a round of Cumrag, first."
                menu:
                    "Sit down":
                        "You nod, getting yourself seated between the three large men."
                        gato "'bout time! Let's get everything started Fokk."
                        "The fox shuffles the cards, and hands each of you a stack of card before putting the rest in the center."
                        fokk "Good t' go."
                        coit "Get ready, server. And may the best player wins."
                        jump Card_Game_Begin
                    "Decline":
                        e "Uhm, I think I'll pass."
                        fokk "'ight then."
                        fokk "Either way I'll teach these two sods to behave around ya more, with their wallets."
                        coit "Well, server ye be'ter not stay around. Gettin' me distracted and what not. Or-"
                        gato "Let's say we've seen which spot hits ye with the most pleasure, we'll make ye leak right away, heh."
                        jump main_nocturnaltrunk_upper
            else:
                fokk "Playing cards we are, wanna join?"
                coit "Aye, don't think ye can escape us that easily! Ye're hooked now, like a fish on a line. Ye'll be back for more, mark me words!"
                fokk "I've come t' respect this scruffy lad a li' more, ye be shi'ing ye pants he's winning all yer money, along with me."
                menu:
                    "Sit down":
                        "You nod, getting yourself seated between the three large men."
                        e "I must admit, the game was quite addicting. Count m' in, you lots."
                        gato "Ah, there's the spirit! I hope ye'v been practising, caus' we won't go easy on ya this time."
                        "The fox shuffles the cards, and hands each of you a stack of card before putting the rest in the center."
                        fokk "Good t' go."
                        coit "Get ready, server. And may the best player wins."
                        jump Card_Game_Begin
                    "Decline":
                        e "Uhm, I think I'll pass."
                        fokk "'ight then."
                        coit "What a stinker, ye be'ter be back next time yer' free from passing plates and mugs."
                        jump main_nocturnaltrunk_upper

    patron2 "How did ye even get those 3 drifters in a row!"
    patron2 "Ah, bugger me with a rusty sword! My bloody pockets are emptier than a beggar's arse."
    "The table was cluttered with an assortment of playing cards and shimmering coins."
    "Amongst which were the three men chattering, echoed with a symphony of gruff, deep voices of casual banters."
    patron "Ain't that the truth, Gato? We need a feckin' miracle to turn this shite around."
    "One of the tavern regular frowns, tossing the rest of his cards on the table without a care."
    gato "Well, bugger me sideways! My purse's always drier than the desert sands. And it's all lost to this smug lil ol' bastard Fokk."
    "The alligator shakes his head, pointing his finger towards the Lemur."
    fokk "Hold your bloody horses, ya gits! Hand m' yer coins before opening ye mouth would ya?"
    "The Lemur exclaims, glancing at the purse with his large round eyes."
    gato "Oi, ye tosspot. Don't get on ye high horse. A change of pace is what I need. Somethin' that brings back lady luck to m' side. What say ye, Coit?"
    "Another regular, a beefy wolf-like Coyote smirks."
    coit "Aye, A change of pace, Huh. A feckin' kick in the bollocks will change his pace perfectly fine."
    fokk "No change of pace will fix yer damn stinky mouth won't ya."
    pause 1
    "Sensing unknown presence, the alligator turns his head around, and notices your glance."
    gato "Hey, you there."
    gato "Aren't you the server downstairs? I could've sworn I've seen yer pretty face around here."
    fokk "Ye be carrying plates and mugs around the tavern don't ye. I've seen what's under that measly little cloth of yours."
    $ cardgame_encountered += 1
    "The regular speaks with mischievous glint, flipping a coin on the table as he speaks."
    fokk "What's ye name again, server?"
    e "Hey, I've only served plates downstairs, I'm [e]."
    "You retort nervously, but the three patrons don't even give you another sign except for a quiet chuckle."
    coit "Aye, that means yer nothing but a glorified mug carrier, so get yer ass over here. We could use some extra luck, or feast fer m' eyes will suffice."
    e "I was just looking around, I'm not actually working right now."
    fokk "Ye, and maybe ye should start working full-time under our table. That'd be what Cane hired you for innit?"
    "Their tease was rather playful, yet much more intimidating with their throaty voices."
    e "But I've never played this game before, wouldn't I just lose?"
    gato "Sit yer arse down and play the bloody game, for gods' sakes. We'll teach ye."
    menu:
        "Sit down":
            jump Nocturnal_Trunk_Cardy_Ready
        "Decline the regulars' request":

            e "W-well, I'll just pass."
            coit "Oh, listen to Mr. High and Mighty! Thinks he's too good for our little game, eh?"
            coit "Well, suit yourself. We'll manage just fine without your fancy help."
            gato "Don't let the door hit you on the way out, server."
            fokk "Oi, server. These two are just sour about losing to the best card player of all time. If ye change yer mind, there's always a chair for yer to sit on, or under."

    jump main_nocturnaltrunk_upper

label Nocturnal_Trunk_Cardy_Ready:

    "You nod, getting yourself seated between the three large men."
    coit "'bout time, let's see if yer as skilled with cards as you are with mugs."
    e "Alright, I'm interested. How do I get started?"
    gato "That's the bloody spirit! Now, let's get down to business. We'll be playing a game of {i}Cumrag{/i}, ye know the rules I suppose?"
    e "W-what are you talking about? Cum Rag?"
    gato "It's the name of the game. The loser is the cum rag, metaphorically."
    e "Ah, then who's last game's cum rag?"
    "You notice two hands pointing their fingers towards the one in front of you."
    coit "Feck off, I ain't do nothin' to ye sorry lot, we're paying with real gold 'ere anyway."
    "The alligator squints his eyes towards you."
    menu:
        "Speaking of, do ye know how to play Cumrag?"
        "I need some guidance":
            call Nocturnal_Trunk_Cardy_Tutorial from _call_Nocturnal_Trunk_Cardy_Tutorial
        "I'm good to go":
            pass
    coit "If ye don't know, ye can always ask. We're playing a fair game 'ere."
    gato "Quit blabberin' and let's get to the shuffling. The sooner we start, the sooner we'll know what luck our punny little server here brings."
    fokk "The stake's simple, if ye the last one, yev gotta pay up."
    e "What exact amount are we betting here?"
    gato "40 gold per-"
    coit "Hush!"
    "Coit slaps his finger in front of Gato's mouth, motioning for his silence."
    coit "Nothing servers like ye can't afford, we ain't got enough gold to bet on anyway, amirite, Gato?"
    "Gato glances at you for a while, then raises his voice once more."
    gato "Yer a cheeky ol' Coyo'. We've got all sorts of wagers on this table, if it's not gold then we can spice things up a lil."
    e "Spice things up?"
    gato "Ye well. Favors. Losers gotta do something for the ones who win. It adds a bit of entertainment for the winners, ye know."
    menu:
        "Ask for clarification":
            e "W-wait, what favours are we talking about exactly?"
            coit "Like I said, nothing ye can't do."
            coit "Fokk here once had to sing a bawdy song in front of the tavern, let's say we lost some customers for our beloved Cane that day."

            fokk "Ya wanker, Cane stopped me there right when I was about to reach the climax of the song, they never got to the end there."
            "Fokk pouts, shuffling the cards on his hands thoroughly."
            fokk "Still, what a load of bullshit yer brewing with these {i}favours{/i}."
            "Gato nods, with a mischievous glint in his eyes."
            gato "We'll change things up a bit now that Cane's favourite cupbearer's on the table, don't ye worry."
            "Both Gato and Coit chuckle loudly."
            e "B-but, am I not going to lose anyway, you all have played the game for far longer than I do."
            coit "Don't fret, aren't ye the brightest server in the room? I'm sure yer'll handle it well."
            gato "If ye lose, just consider it an initiation to become a cardslinger!"
            "As you ponder the risk of such favours, Fokk hands you the last stack of cards, moving the rest on the center of the table."
        "Go along":
            e "I guess so. Favours' am I right?"
            fokk "That's the spirit, server. Keeps ye eyes on the prize and soon, ye'll wake up a couple thousand gold richer."
            "Fokk grins, shuffling the cards on his hands thoroughly."
            e "Take it easy on me though, I-I still don't know anything about the game."
            gato "Aye, we will."
            "Both Gato and Coit wink at each other and chuckle loudly, though you still don't know what's going on."
            coit "I like yer attitude. Ye'll fit right in on our table."
            "Gato nods, with a mischievous glint in his eyes."
            "As clueless as you are, you scratch your head as the regulars glancing at each other, which just makes them grin wider as they notice you."
            fokk "Now I see why Cane liked this one more. Definitely up his alley too."
            "The other two laugh wholeheartedly, as Fokk hands you the last stack of cards, moving the rest on the center of the table."
    coit "Get ready, server. And may the best player wins."
    jump Card_Game_Begin

label Nocturnal_Trunk_Cardy_Tutorial:
    fokk "Alright, listen up, ye scoundrels."
    "Fokk clears his throat, showing you off the cards."
    fokk "Cards can be in the deck, your hand, or a pile. As the game starts, all 52 cards are in the deck."
    gato "We got that part, you long-winded sod! Get on with it!"
    fokk "Don't ye worry, server. Losers loves acting like impatients lot."
    fokk "Anyway, each of us gets 5 cards. And the first one can play any number of cards of the same rank to start a new pile."
    fokk "Then, the next one plays, and they can only play cards with number higher than the one on top of the pile-"
    coit "Unless it's them pilgrim cards, then there's a twist to it!"
    "Fokk rolls his eyes, obviously annoyed at the interruption."
    fokk "Right, right. If there's 4 cards of the same rank on top of the pile, it'll burn the whole pile."
    e "What does burning mean?"
    gato "It means the cards in the pile are removed from the game, and the next sod will start a new pile. Simple as that!"
    fokk "Well he's not wrong. Now, where was I? Ah, if ye can't play or don't want to play, ye have to take the entire pile and add it to your hand, starting a new pile."
    coit "Or if ye're a wee coward and too scared to take the risk, like Fokk!"
    fokk "Have it yer way, stinker, see who has yer gold now. Either way, if ye have less than 5 cards, then ye must take cards from the deck to refill yer hand."
    fokk "After that, it's the next player's turn."
    fokk "We'll repeat the same cycle until the deck is depleted. After that, you have no cards to refill and you'll win if you play all your cards."
    e "uhmm... so what does the pilgrim cards do?"
    fokk "Ah, those pilgrim cards! They're special, see? The fire one is the kindler. It lets you burn down the pile, just like Gato mentioned earlier."
    "The Coyote leans in, emphasizing on the symbols on the pilgrim cards."
    fokk "And the watcher lets you peek at one of the other players' hands. Then ye can choose to swap hands or keep 'em."
    fokk "Lastly, the drifter! It's the highest value in the entire game. If it's on the pile and ye don't have any other drifters, ye're stuck takin' the pile, me matey!"
    gato "Aye, ye heard 'em, player! That's the rule of the game in a nutshell."
    e "A-alright, I think I got a hang of it."

    return "no"

label Nocturnal_Trunk_Cardy_End:
    $ cardgame_result_history.append(cdg_winner)
    if cdg_winner[-1] != "You":

        if cdg_winner[-1] == "Coit":
            coit "That's no fair round. I had such a great hand and yer tactics be ruining all me plans, ughhh..."
            fokk "Oi, we know who's the cumrag this round."
            coit "N-no wait, I still have money to spare yall. What was the stake, again. 40 gold per card?"
            gato "Beat'n by a glorified mug carrier didn't ya? Quickly m' coyo', my pocket's waitin'."
        elif cdg_winner[-1] == "Gato":
            fokk "Been losing for a while now. Aren't ya a proper cumrag?"
            gato "My luck's drier than the desert sands, same goes for m' pocket, Ugh."
            coit "Aye, ye better pay us up, including our server right 'ere. 40 gold per card."
        else:
            coit "Hah, Looks like our all and mighty Fokk ain't so invincible after all, I knew we'd take back the gold from ye."
            gato "The god has fallen, hah. What a disaster, ye might wanna reconsider yer self-proclaimed title of a card master."
            fokk "Ain't ye lots comedians. 'ight, 40 gold per card as promised."

        e "W-wait... How much would we get?"
        fokk "The first gets about two third of the gold, and the rest are spread even by the second and third."

        if cdg_winner[-1] == "Coit":
            $ cdg_stake_amount = len(cdg_c3)*40
            "The fox grins, accepting coins from the coyote."
            coit "There goes m' ale money for the week, but just so yer know, I'm makin' it back next round."
        elif cdg_winner[-1] == "Gato":
            $ cdg_stake_amount = len(cdg_c2)*40
            "The fox grins, accepting coins from the alligator."
            gato "My pocket's lighter than a feather now. Spend those coins wisely yall, caus' yer paying me back more next round."
        else:
            $ cdg_stake_amount = len(cdg_c1)*40
            "The fox frowns, handing you three a pile of gold."
            gato "Hah' finally ye taking a taste of yer own medicine."
            fokk "Aye, I ain't minding once in a while if m' medicine is winning."
        if cdg_winner[0] == "You":
            $ cdg_stake_amount = int(cdg_stake_amount*0.667)
        else:
            $ cdg_stake_amount = int(cdg_stake_amount*0.167)
        "You take [cdg_stake_amount] gold from Fokk."
        $ pc.gold += cdg_stake_amount
        $ cdg_earned_total += cdg_stake_amount
        fokk "Well, 'twas a good game with our server here."
        e "It was quite fun playing with you guys too!"
        coit "The more the merrier, and the chance of m' losing ain't going up too."
        gato "As if yer' just tossing a dice, ye dumb scoundrel, that's why yer pocket's been empty most of the time."
        pause 1
        "The four of you laugh wholeheartedly, with Fokk patting your back."
        fokk "Come back anytime, we'll be 'ere playing."
        "You stand up from the chair, and take your leave."
        jump main_nocturnaltrunk_upper
    else:
        $ cardgame_lost += 1
        fokk "Ah, today's cumrag - our little server here."
        if cardgame_lost > 0:
            e "That was a confusing game... right?"
            $ cdg_stake = len(cdg_p)
            $ cdg_stake_amount = len(cdg_p)*40
            coit "Aye, but ye lost. It looks like ye owe us a little something now, don't ya think?"
            e "Can't we... just let it slide this time? I ha- had a lot of fun playing with you guys."
            "The three regulars smirks, it doesn't seem to affect them."
            gato "Can't just let ye off the hook that easily."
            "Fokk extends his hand, motioning you to hand over something."
            fokk "40 gold per card, ye'v got [cdg_stake] cards left 'ere. That's... [cdg_stake_amount] gold ye owe us."

            menu:
                "What should you say?"
                "Hand over the gold" if pc.gold >= cdg_stake_amount:
                    $ cardgame_lose_history.append(1)
                    e "W-well, I guess fair's fair."
                    "You take out your bag, handing it over to Fokk."
                    "He quickly snatches it, and begins counting the coins."
                    gato "Well, we're a generous bunch, so don't ye worry yer arse. It'll be a drop in the bucket."
                    fokk "See, we'll take no more, and no less. Rules are rules and a few coins will do."
                    e "Still, you don't need to take all my gold to count it."
                    "You grumble under your breath, and the fox quickly takes notice and looks up."
                    fokk "We'll put'em to good use, server. After all, some of these are hard earned gold you've gotten from serving mugs and plates."

                    coit "Ye mean more ale?"
                    fokk "Especially more ale."
                    "Fokk returns the rest of the gold to you, and shares it with his cardmates."
                    fokk "There goes [cdg_stake_amount] gold."
                    e "Thanks for the game, anyway. I had a lot of fun."
                    coit "The more the merrier, and the chance of m' losing ain't going up too."
                    gato "As if yer' just tossing a dice, ye dumb scoundrel, that's why yer pocket's been empty most of the time."
                    pause 1
                    "The four of you laugh wholeheartedly, with Fokk patting your back."
                    $ pc.gold -= cdg_stake_amount
                    $ cdg_earned_total -= cdg_stake_amount
                    fokk "Come back anytime, we'll be 'ere playing."
                    "You stand up from the chair, and take your leave."
                    jump main_nocturnaltrunk_upper
                "I don't have any gold":

                    e "I don't have any gold on me right now."
                    e "Mind if I l-leave to get them... very quickly?"
                    "The three regulars lean forward almost at the same time, their intimidating gaze only causes you to stutter more."
                    gato "No gold? Well, hand over ye wallet."
                    e "T-there's nothing inside... Can't we just work something out? I promise I'll p-pay back."
                    coit "Work something out, ye say? Gimme yer wallet and we'll work something out."
                    "The Coyote smirks, his demeanor has shifted quite drastically, especially when they are all staring at you, not just your eyes but glancing over your whole body."
                    gato "It's all in good fun, wouldn't we all agree?"
                    "Without hesitation, Fokk swipes the bag from you."
                    e "Hey!"
                    fokk "Well, a debt is a debt, and we'll take whatever ye can pay."
                    if pc.gold < cdg_stake_amount:
                        $ cardgame_lose_history.append(2)
                        if pc.gold == 0:
                            "He turns the bag upside down, but nothing falls out of the bag."
                            "You awkwardly watch as the fox shakes your bag for a few times, just to confirm that no gold was ever in the bag."
                            fokk "Well, not even one gold?"
                            gato "That was miserable, even for a mug carrier like ye."
                            e "I told you I don't have any money..."
                        else:
                            "He turns the bag upside down, and you see only a few coins drop on the table, one of them almost rolls out of the table's edge until Gato stops it."
                            "The fox raises his brows."
                            fokk "That wasn't enough for what ye owed us."
                        "Fokk scratches his chin for a bit, before coming up with an idea."
                        fokk "Look, server, we ain't a greedy bunch, I'll spare ye the rest of the coins, if ye pay with yer body."
                        fokk "I've seen what's underneath that apron of ye, when ye came forward to serve plates and mugs bare-furred."
                        coit "That was a sight to behold, m' lad. I even got to squeeze ye bouncy arse down there."
                        "The regular walks out of their chairs, and blocks your exit in an uncomfortably close proximity."
                        gato "And it's free, this lusty little server 'ere ain't the shameful type. I know he's gettin' hard knowing what comes next, just like when he's serving plates."
                        e "You can't do this..."
                        fokk "I hate to break it to ye, but this is our district 'ere. And we can do whatever we want with ye."
                        e "I-I... that wasn't what I signed up for."
                        gato "He's talkin' like he didn't want this... Haha, look at his poorly disguised thirst beneath his eyes."
                        fokk "Ain't that a truth, ye've been eyeing us for a while now. So why don't we skip to the great part with ye."
                        coit "You've got no choice 'ere, server. Should've saved up a little before playing the game don't ye think?"
                        e "That was so unfair, all three of you are so experienced in the game."
                        fokk "Look, all we need is just some of your precious time. Considering ye've got no gold to pay, why not relax for the while."
                        call scene_tavern_cardgame_lose from _call_scene_tavern_cardgame_lose
                        $ pc.add_active_status(stuffed)
                        $ pc.add_active_status(soremouthed)
                        $ pc.lust = 0
                        jump main_nocturnaltrunk_upper
                    else:

                        "He turns the bag upside down, and coins immediately rain on the table, making a small pile that grows by each seconds."
                        gato "Did ye hit a jackpot? Cause that's a lot of gold 'ere. "
                        e "Well, I... uh... guess I must have forgotten about those. Can I have my wallet back now?"
                        fokk "Not so fast, server. Since ye conveniently forgot about these coins, they rightfully belong to us now. Consider it a lesson learned."
                        e "W-wait, can't you just take what I owed?"
                        coit "Not since ye lied to us. We value honesty more than ye think, little server."
                        fokk "But we ain't a greedy bunch, I'll spare ye the rest of the coins minus those ye owed us, in the form of another payment."
                        e "W-what another payment."
                        fokk "I've seen what's underneath that apron of ye, when ye came forward to serve plates and mugs bare-furred."
                        coit "That was a sight to behold, m' lad. I even got to squeeze ye bouncy arse down there."
                        "The regular walks out of their chairs, and blocks your exit in an uncomfortably close proximity."
                        gato "And it's free, this lusty little server 'ere ain't the shameful type. I know he's gettin' hard knowing what comes next, just like when he's serving plates."
                        e "You can't do this..."
                        fokk "I hate to break it to ye, but this is our district 'ere. And we can do whatever we want with ye."
                        e "I-I... that wasn't what I signed up for."
                        coit "Maybe if ye're being honest with the gold ye've got, you could've got out of this properly clothed."
                        gato "Look, loser's loser. Don't even think about tryin' any tricks on us experienced lots."
                        "You turn your head."
                        menu:
                            fokk "Well, as a token of merit, and respect for Cane, I'll let ye choose, pay with ye body, or ye entire wallet belongs to us now."
                            "Pay with body":
                                $ cardgame_lose_history.append(3)
                                e "Body... I guess."
                                gato "He's talkin' like he didn't want this... Haha, look at his poorly disguised thirst beneath his eyes."
                                fokk "Ain't that a truth, ye've been eyeing us for a while now. So why don't we skip to the great part with ye."
                                "You flinch as you feel a strong arm touches you from your side, he squeezes your shoulder harshly."
                                call scene_tavern_cardgame_lose from _call_scene_tavern_cardgame_lose_1
                                $ pc.add_active_status(stuffed)
                                $ pc.add_active_status(soremouthed)
                                jump main_nocturnaltrunk_upper
                            "Give wallet":

                                $ cardgame_lose_history.append(4)
                                e "W-well... take the wallet then."
                                gato "O-oh? Perhaps we misjudged ye. Thought ye horny-brained sod might be interested in somethin' else."
                                "The fox scratches the back of his neck, either in confusion or disappointment."
                                "They all returns to their seat like nothing happened, and you can finally take a deep breath without smelling the regular's heavy scent of alcohol."
                                fokk "Aye, it's what's fair. He really didn't want to have his arse plowed, must've heard how hard we fucked, haha."
                                coit "Keep ye gold, server. We've had enough of 'em. Well, Fokk has. Ain't no fun if ye don't come back later."
                                e "W-wait, really?"
                                fokk "I'd have preferred ye paying with ye body, ye know, I've been gettin' my meat prepared for a tight hole."
                                "The fox scratches his crotch nonchalantly, as if it was to calm his nerve rather than releasing his lust."
                                coit "Ye can trust us, server. We'll treat ye gold nicely, could've puttin'em mouth to good use though."

                                gato "With a skill like yours, it's only a matter of time until ye pocket's emptied anyway."
                                e "I-... I've only just started with this game, I'll get better once I've gotten a hold of it."
                                coit "Aye, that's the spirit. Come back when you've refilled ye gold."
                                e "A-alright, thanks for... not taking away all my gold."
                                $ pc.gold -= cdg_stake_amount
                                fokk "Ye're welcome."
                                fokk "Come back anytime, we'll be 'ere playing."
                                "You stand up from the chair, and take your leave."
                                jump main_nocturnaltrunk_upper


label Cane_Beer_Task_Begin:
    if task02.completedtimes == 0:
        c "Ey, Lad. Care for a minute?"
        e "A-alright."
        c "Aye, just need ya here."
        "The barkeeper leads you behind the counter."
        c "Come closer little lad, not like I haven't seen ya naked already."
        e "Ehm... what can I do for you?"
        c "Heh, look at ya squirming like I'm gonna catch cha off guard."
        c "Nothing fancy, I was gonna ask ya about making some beer."
        e "Ehh...?"
        c "Look, I've got myself some work to do and ass to beat."
        c "And those new lads you attracted from the work, they had a qualm with my classical beer."
        e "Classical Beer...?"
        c "Classic, or Traditional. Ya think I don't know ya fancy words?"
        c "Anyway, I came up with another recipe for my beer. But I need some more ingredients."
        e "Ehm... you want me to get them for you."
        c "Exactly, heh... ya surely know what I'm thinking."
        "The Bat nonchalantly squeezes your shoulder."
        c "So, ya get me some barley from the field, and uhh... get some rosemary from that potion maker too."
        menu:
            c "I'll give ya yer fair share, 50 gold's right. Sounds fair?"
            "Take the Task":
                e "Sure!"
                c "Ya need a scythe for the field too. I'll give cha the recipe..."
                c "Not like the lion shop is gonna help ya on this one."
                e "W-wait... I didn't know I need a recipe for this?"
                c "Yeah, it's easy. Just get some iron and wood..."
                e "So... I have to gather them?"
                c "Well, ya promised me, now getcha ass in the field."
                e "O-ok... but can you not... withhold information from me next time..."
                c "Aye... Sorry my lad. Old habit is all. I'll be easy on ya."
                $ discoveredrecipe.append(ironscytherecipe)
                $ task02.tProgress(_("Collect 3 Barley from the Farm"), "Barley", 3)
                $ task02.tProgress(_("Collect 3 Rosemary from the Potion maker"), "Rosemary", 3)
                $ TaskBegin(task02)
                jump main_nocturnaltrunk
            "Maybe Later":
                e "Maybe... Later?"
                c "Eh... alright lad. Think quickly."
                jump main_nocturnaltrunk
    else:
        c "Bet cha know what I'm thinking?"
        e "Hmm... gathering more materials for you to brew?"
        c "Yer goddamn right."
        e "I can do it."
        c "Well then, get cha ass in the field."
        e "O-ok!"
        $ TaskBegin(task02)
        jump main_nocturnaltrunk

label Cane_Beer_Task_Report:
    if LookForItemNumber("Rosemary", inventory) >= 3 and LookForItemNumber("Barley", inventory) >= 3:
        if task02.completedtimes == 0:
            c "Ay, finally, the lad of the day!"
            e "Hey, Cane, got everything you need."
            c "Good, Good."
            c "That's enough, I'll go brew them right away."
            c "Here's the reward for ya."
            "You received 50 gold."
            e "Ah Thanks Cane."
            c "No thank you!"
            c "Thanks for making this good ol' bat having the time of his life."
            c "Been a good while since I've got someone like cha here."
            c "Well, that'd be an understatement. Yer the best lad out here."
            e "Cane, I think you flatter me a lot."
            c "No, lemme do this at least. It's the least I can do, and all I ever did was asking ya favours."
            e "No, I was having fun working with you, Cane."
            e "And well, and getting money from you."
            c "Ya know, lad... I should... do something for ya once."
            e "W-what's on your mind?"
            c "Uhm... Yer making this old bat's cheeks red."
            "Cane casually slaps your ass, but this time he spent a little more time gripping onto your butt."
            e "H-hey..."
            c "I'd do something for ya for once."
        else:
            c "Ay, finally, the lad of the day!"
            e "H-hey!"
            "Cane casually slaps your ass."
            c "Good job!"
            c "Thanks for making this bat's day."
            e "I'm glad I can help."
            c "Either way, here's your reward."
            "You received 50 gold"
            $ pc.gold += 50
            e "Thanks!"
            c "Well, be back any time, for the ale."

        $ pc.gold += 50
        $ removeItem("Rosemary", inventory, 3)
        $ removeItem("Barley", inventory, 3)
        $ TaskFinish(task02)
    else:

        c "Got the stuff I need?"
        e "Y-yes..."
        c "Nah... that's a no."
        e "I'm sorry Cane."
        c "Well, go and get 'em then."
    jump main_nocturnaltrunk

label Cane_Favour_For_Ya:

    c "'ello there, lad!"
    "Cane looks at you with his usual cheeky grin."
    c "Anything ye wantin' today?"
    "He waggles his eyebrows at you suggestively."
    c "Maybe a bit o' tavern work, or quality time with some patrons?"
    "You blush red like a tomato."
    e "No, no. I'm not here for that this time."
    "Cane lets out a hearty chuckle straight from his gut, throwing a wink your way in the meanwhile."
    c "Shame. I know 'ow much ye enjoy yer work back there."
    e "A-anyway! I was here to ask about, umm. That favor you mentioned last time, when I helped you source more alcohol?"
    "Cane's face sobers up immediately."
    c "Ah, yeah. Mentioned somethin' 'bout that, didn' I."
    "He shifts uncomfortably, looking down at his hands, grabbing a mug to his right and wiping it down."
    c "I been thinkin' on it."
    c "I just... dunno what I could give ya that would be worth as much a' what ye do fer this tavern and I."
    "Letting out a monumental sigh, Cane puts away the mug and towel, before spreading his arms out on the table."
    menu:
        c "Still can't think o' nothin'. So... what'cha want me to do fer ya. Promise I'll do it fer ya if it's reasonable."
        "Money":
            $ cane_favour = 1500
            e "Well... I could use some extra cash, on top of what I usually make serving the patrons."
            "Cane looks relieved, despite his firm desire to keep his money."
            c "Sure. 'ere."
            "Cane reaches into his belt pouch, and hands you 1,500 gold pieces."
            $ pc.gold += 1500
            c "This good enough fer ya?"
            e "Y-yeah. That's honestly more than I expected."
            "Cane laughs, reaching out and ruffling your head."
            c "Least I could do fer a cute lad like yer fine piece o' ass."
            e "Thank you Cane!"
            "He waves you off, as if it were nothing."
            c "No need ta thank me. We'll be makin' much more money together in the future."
            c "Now, I best be gettin' back to servin' these louts. I can see some of 'em starin' daggers at ye."
            "Cane walks out from behind the counter toward said patrons with two mugs of beer, briefly setting one down to smack you on the rump as he passed by."
            c "I'll see ya later, lad."
            e "See you later, Cane."
        "Sex":
            $ cane_favour = True
            stop music fadeout 1.0
            jump Cane_Favour_For_Ya_Sex

label Cane_Favour_For_Ya_Sex:
    if _in_replay:
        show screen Replayexit
    "You shift uncomfortably, face cherry red just thinking about what you're going to suggest."
    e "Well... I was wondering if maybe you could..."
    "You clear your throat."
    e "If you could do to me what your patrons have been doing to me."
    "Cane's grin is briefly frozen on his face."
    c "Ah! No worries lad. I already pay ya for yer services, but I'm fine with paying ya more."
    "He's not looking you, his eyes instead focused on the mug he left to his right."
    e "That's not what I mean Cane... I'd really like to spend a night with you."
    e "I thought you'd want to too, considering how often you slap my ass or call me cute."
    "Cane is pausing, as if considering his words."
    c "I... don't think that'd be a good idea."
    "It's his turn to shift uncomfortably now."
    c "Ye... yer a cute lad, yes. I think anyone'd be lucky ta bed ya, but... I shouldn't."
    "For the first time in all the time you've known him, Cane seems to be on the backfoot with you."
    e "Why not?"
    c "I can't be trusted ta be all intimate-like with a lad like ye."
    "His accent only seems to be growing stronger in his panic."
    e "Well..."
    "You take a risk. You reach your hand over, and place it over his webbed one."
    e "I trust you."
    "Cane flinches at your touch, but doesn't take his hand away."
    c "..."
    "He looks so conflicted, two parts of himself warring over his face, desire and guilt meeting each other failing to resolve."
    e "It doesn't have to be sex...? I'm happy just jacking off together."
    "Closing his eyes, Cane lets out a sigh. He looks up at you helplessly."
    c "Fine. I can work with that."
    "His face returns once more to its sly grin, if one a bit more hollow than normal."
    c "I'll close up shop early tonight, and meet ya in my room later."
    "Cane throws a wink your way."
    c "Hope yer ready ta see this old bat in all 'is glory."
    e "Thank you Cane! I'm really looking forward to it!"
    "You aren't lying. You've had a wet spot on your loincloth for a while now, having grown quite large since it first appeared when you thought of what to ask for."
    c "I'm glad."
    "With that, Cane turns around to work on some of the mugs behind him."
    "...but not before you catch a glimpse of a large bulge in the front of his pants, accompanied by a wet spot of its own."
    "Well. At least it seems like he's excited for it, despite his misgivings."
    "..."
    scene black with dissolve
    "You spend the rest of the day working at the tavern."
    "You keep catching Cane sneaking glances at you."
    "...It's hard to blame him when you're doing the same."
    "The catcalling and playful slaps given to you by the patrons is much more intense than usual."
    "Probably has to do with your poorly-concealed hard-on."
    "Soon enough, however, the bar is cleared out. It is just Cane and you in here, cleaning up the patrons' mess."
    "As you finish wiping off the last table, you feel a hand on your shoulder."
    "Turning to look up at the source, you see Cane looking down at you."
    "His other hand takes this opportunity to cup your chin, and rub your cheek."
    scene nocturnaltrunk_night with dissolve
    show cane normal with dissolve
    c "Ye sure ye want this, lad? 'S not too late to call it off."
    e "As if I'd want to give this up."
    "Cane sighs."
    c "Well... can't say I don't find the idea excitin'."
    "A grin spreads across his face."
    c "It's great to see a young, handsome, hardworkin' lad fall 'ead over 'eels for an old bat like me."
    "He's motioning for you to get up and face him properly."
    "You do, without hesitation."
    c "'ere. Why don't ye see for yerself what I mean."
    "Cane grabs your hand, slowly and gently pulling it towards his crotch, making sure you know what's happening, and have ample time to stop if you want."
    "He presses your hand under his belly, to the fat, warm bulge beneath."
    c "That a good enough reward for ya, lad?"
    "You can't help but gulp as he smiles down at you knowingly, removing his hand from yours to grab and snuff out his cigar."
    c "I'm not hearin' a yes or no."
    e "Y-yes! This is great."
    "Cane's smile turns into a teasing grin as he steps away from you at this information."
    c "Alright! Then I suppose we're done 'ere if that's enough for ya."
    e "Wait! No! That's not what I meant!"
    "He turns around in mock surprise, one eyebrow cocked in question."
    c "Ah, so ya didn' like it?"
    e "N-no, I did, but-"
    c "Oh, then what seems to be the problem, lad?"
    e "You know exactly what it is!"
    "Shit, it's really hard not to get caught up in his rhythm."
    "Cane walks up and ruffles your head."
    c "I do, 's just cute ta watch ya squirm like that."
    c "Now, let's get ta my bedroom."
    scene black with dissolve
    pause 2
    "Pointing up the stairs, to a door on the second floor, Cane tells you to get going."
    "As you start to move forwards, you feel a sharp slap on your ass."
    c "Plump little thing ye've got right there, lad."
    "He grabs you by the hips as you reach the top of the stairs, pressing his bulge between your cheeks, and his gut against your back, whispering in your ear as you move."
    c "Yer lucky I'm holdin' myself back 'ere, because the fella down there wants ta leave that hole unrecognizable."
    "You shudder with excitement at those words, eliciting a lustful chuckle and thrust from Cane behind you."
    "As you arrive in the room, Cane detaches from behind you, much to your chagrin."
    scene canebedroom with dissolve
    "You turn around after taking a couple steps in."
    "Cane has closed the door, and is standing in front of you with a confident smirk."
    show cane normal with dissolve
    c "Well, lad, it's all yours."
    "He shoots a wink at you."
    c "Though you'll need ta take care ah the unwrapping process yerself."
    "Getting his meaning, you begin to disrobe."
    "Cane laughs, grabbing you and bringing you close before reaching for your clothes."
    c "No, lad, I'll take care of yers for ya."
    "He pauses, stopping himself."
    c "As long as ye want, of course."
    e "I, umm... yeah, I'd like that."
    "Cane grins widely, putting his hands back on your outfit, feeling you up a bit."
    c "Ye wanna do the same for me, lad? I'll let ya, as part of that reward of yers."
    c "Let ya get a good feel of this here old bat."
    "He presses you against him as he says that, his cock grinding against yours, both struggling to stay within the confines of their pants."
    "As he holds you there, he moves his hands down your back, and hooks his hands on your waistband."
    "He makes as if to pull it down, but puts his hands underneath it instead, grabbing and squeezing at your rump, pulling your cheeks apart as he continues grinding."
    c "Well lad? Ye up for it?"
    e "Y-yes!"
    c "Then why don't ye start by unbuttoning my vest, handsome."
    "You move your hands up to his buttons, and struggle with them for a bit before popping it loose."
    "Taking some of the initiative, as Cane seems both pleased by your actions so far, and distracted by your ass, you reach under his shirt."
    "You brush your hands up his rough belly hair, and up to his fluffy chest."
    c "Now yer gettin' into it, lad. Keep goin' just like that."
    "Needing no further encouragement, you grab his pecs."
    "It's like feeling steel wrapped in cushions. His muscles ripple underneath the outer layer of fat, somehow managing to tow the line between soft and rough."
    "Just like the rest of him, you suppose."
    "Wanting a better look, you grab the base of Cane's shirt and vest, and pull up."
    "Cane briefly pulls his hands out of your pants and steps back slightly, helping you lift his shirt off of him, as he is too tall for you to fully take it off of him."
    "Cane stands there for a moment afterwards, so you can properly take it all in."
    "And oh boy is there is a lot to take in."
    "From his strong, plump gut, to his powerful pecs, to arms that look like they could pick up three of you..."
    "You reach out for his arms, tracing some of his markings and scars with your fingers, rough fur pressing against our own soft fluff."
    c "Hehe. Ye like those, lad?"
    "He flexes for you."
    c "Got 'em back when I was too big for my britches, and thought I could make a livin' on the rougher side 'o life."
    "He pauses slightly, throwing you another wink."
    c "Well, bigger for my britches than I am right now."
    c "Now, I wanna see my cute lad under there."
    c "'s not like I haven't seen it before, but..."
    c "Les jus' say it's one of the highlights o' my day when ya put on yer shows fer the tavern."
    "Saying this, Cane reaches for your top, and begins to gently pull it off of you, slowly revealing inch after inch of your fur to him."
    c "Mmh. Looks even better up close."
    "Cane says this looking down at your own fluffy pecs."
    c "Can I?"
    "You don't know exactly what he's asking, but you nod."
    c "Good."
    "Grabbing your pecs in each of his webbed hands, Cane begins to massage them much as he was your ass."
    c "Nice and soft little things ye got here. I'd think ye were some innocent little guy if I didn't know better."
    "He begins to get rougher with them, slowly pushing you back onto the bed, before pushing you down so you are pinned beneath his much larger form."
    c "Mind if I get a taste, lad?"
    e "N-not at all! Please, go right ahead!"
    "With nothing left to hold him back, Cane moves his head down to where his hands were, gently licking around one of your nipples."
    "Feeling you jolt in reaction, he suckles on it lightly, getting an even larger reaction out of you as you melt under his ministrations."
    e "F-fuck... Cane..."
    "Seeing you writhing with pleasure, and hearing no protest from you, Cane takes his hands and pins your arms to keep you in place, as he begins gently nibbling."
    e "C-Cane! This wasn't what, ah- what we agreed on."
    "Cane immediately stops, looking up at you with a concerned look on his face, vestigial vampire teeth drooling slightly."
    c "Do ye want me to stop, lad?"
    e "Yes please. It felt great, but..."
    e "I'd really like to see you."
    "Cane shrugs apologetically"
    c "I'm glad ye were enjoyin' it as much as ye seemed to be."
    c "Lemme see if I can make ya enjoy this next part even more."
    "Cane props himself back up onto his feet, undoing the strained buttons of his trousers."
    "Catching you staring, Cane smirks."
    c "I'd love it if ye'd take yers off too fer me."
    e "A-ah! Yeah! Got a bit distracted there, hehe."
    "Cane only looks more self-satisfied as he strolls over to the other side of the bed, laying down."
    c "One can only wonder why."
    "You can see a bit of his cock peeking over the top of his pants, tip already slick with pre."
    "Getting the hint, you take your pants off and move up next to him as he removes his own."
    show cane naked with dissolve
    "Laying there, side by side, you can really appreciate just how big Cane is."
    "He's almost half as wide as you, and more than twice so thick, towering over a head above you."
    "The same goes for his cock, a thick club of a thing - not nearly so long as it is girthy."
    c "Well, lad? Is it everythin' ya thought it'd be?"
    c "I know I'm enjoyin' the view from here."
    "Cane's look would be considered undressing you with his eyes if it weren't for your complete lack of clothes."
    "As it is, he just looks greedy and lustful."
    e "Yes... it's a lot to take in."
    "Cane lets out a throaty chuckle, the bedframe quivering a little bit with the rumble of his voice."
    c "Well, it's a good thing yer not takin' it in today."
    c "Now..."
    "Cane reaches over slowly, hand drifting towards your cock."
    c "How'd ya like to get a feel for each other for now?"
    "You try to say yes, but your breath catches in your throat, leaving you with no recourse but to nod desperately."
    c "Good lad."
    scene black with dissolve
    pause 2
    scene canefavour004 with dissolve
    "Cane takes advantage of your affirmation, and wraps his hand around your cock, gently tugging it to see what the best grip he can get here is."
    "Before figuring it out, he chuckles lightly."
    c "I was thinkin' of gettin' the lube out fer this, but..."
    "He brings his webbed fingers up in front of your face."
    "Each and every one is glistening with your pre."
    c "...cute."
    "With that, he returns to your cock, gently grasping it, and rubbing his thumb over the tip."
    e "Mmmf..."
    "Although the webbing between his fingers is leathery, they completely wrap your cock up in his grasp, firmly cocooning your cock like a fleshlight."
    e "Can I... can I play with yours?"
    c "Hehe, it seems yer listenin' skills get worse when yer all riled up."
    "He gives your cock a firm tug, getting another gasp out of you."
    c "I already gave ye permission. Please, have at it."
    "So saying, he juts out his hips slightly, so that his fat cock slides firmly out of reach of his prolific gut."
    "Cane waits patiently as you slowly reach out for his cock, spending the time gently massaging the head of your cock with his thumb."
    "Finally working up the nerve, you grab it."
    pause 2
    scene canefavour007 with dissolve
    "Fuck... you can feel it throb in your hands in response. It's warm, too thick to fully wrap your hand around, and slick with pre."
    "You gently pull down, still firmly grasping it."
    "His foreskin glides off of his cock with no resistance, revealing the fat purple head of his drooling cock."
    c "Oof... Good lad."
    c "Here, let me just..."
    "Cane begins to properly stroke you, slowly, but relentlessly pumping the length of your cock with his hand."
    "The way you quiver and twitch slightly seems only to excite him, as he tightens his grip slightly, creating a slight sensation of suction in his webbed hands."
    "It feels most similar to when you had the slime jack you off - the sensation of having your cock completely enveloped by a hungry form."
    c "Hrmm... I'm glad ye like that, lad."
    c "'S awful cute ta watch ye squirm like that."
    "He looks so satisfied with himself, seeing you melt in his hands like this."
    "However hot that may be, you can't exactly let him get away with it without some revenge."
    "Fighting against the urge to go catatonic from the lustful haze coming from your dick, you begin pumping at Cane's cock, bringing your hand from just under the head of his cock all the way down to the base, such that your fingers graze his plump balls with each stroke."
    "It's his turn to struggle now. You see his breath catch in his throat, and feel the way his cock throbs in response, leaking sticky pre between your fingers."
    e "You were saying?"
    c "Was sayin' that-"
    "Stealing a page from his book, you take this opportunity to gently rotate your hand on his cock as you pump down this time, stimulating as much of him as you can despite your inability to reach around the fat fucker."
    c "{i}Mnnng~{/i}"
    "Cane's groan is a satisfying thing to hear, especially when you hear his breathless voice after the fact."
    c "Damn, lad, yer good at this."
    "You feel Cane begin to rock his hips forward, gently fucking your hand."
    "Every time he shoves forwards, you feel his belly on your arm, and his balls on the back of your fingers."
    "At the same time as he does this, he moves his other arm over onto your body, and begins to fondle anything and everything in reach."
    "...Looking more closely, it's very much like he is imagining actually fucking you, rather than just jacking each other off."
    "His eyes are closed, his mouth slightly open as if to bite a neck in front of him... even his hand is jerking you off in time with his thrusts."
    e "Fuck, Cane..."
    "Hearing that needy gasp of yours seems to push some button deep inside of him, as his pace picks up, a fresh glob of pre slicking your hand."
    "With a low, needy growl, the hand roaming around your body moves down to your ass, roughly grabbing and pulling at it, tugging you slightly closer to him."
    "Getting the hint, you move yourself closer, and lean in to kiss him."
    c "Mmph!"
    "Surprised by this move, Cane takes a moment to respond, giving you the chance to slip your tongue into his mouth."
    c "Mmm"
    "As if taking this as a challenge, Cane wraps his arm around your lower back, tugging you even closer against him so that all you can feel against your front is coarse fur, and the contradictory plush hardness of his body."
    "Satisfied with how you're locked in place, Cane pushes his tongue against yours, guiding them out of his mouth and into yours."
    "Firmly in control now, Cane begins to buck his hips, rubbing his cock against your soft fur, matting it with his pre, as your own cock rubs against his plush belly."
    "You open your mouth to moan out of reflex, but Cane presses deeper, locking your lips in place, eating any attempt you could make at noise."
    "Cane's body enters a full rut, his hips pumping more and more powerfully."
    "Soon, he finds himself unsatisfied with having you at his side, and pulls up from under you, breaking the kiss and slamming you on your back."
    "His cock is lined up with yours, its base resting on your balls."
    "Your field of view is dominated by Cane, a dark purple mass with drooling white teeth looming over you."
    "His gaze can only be described as hungry as he stares down at you, pinned under his larger, more powerful form."
    "You're left breathless."
    "Literally. He was a bit too rough when he slammed you on your back, as he knocked the wind out of you."
    "As he approaches for a kiss once more, you put a hand up against his chest to ask for a second to breathe."
    "Suddenly, the lustful look in Cane's eyes disappears, replaced instead by terror."
    scene black with dissolve
    pause 2
    scene canebedroom with dissolve
    show cane naked with dissolve
    c "I-... La-... I don-..."
    "He can't even figure what to say, his large form pushing up and off of you, backing off as if burned."
    e "Cane? What's wrong?! Is everything okay?"
    "At your words, he pauses, a hint of normalcy returning to his eyes."
    "No longer panicked, he instead looks hollow and frustrated."
    "Shoulders sagging, Cane sits at the side of the bed, and puts his head in his hands."
    c "I'm sorry, lad."
    e "Wh- but, I was having a great time!"
    "Shaking his head, Cane turns to look you in the eyes."
    c "Maybe, but it was further than we agreed to go, and far rougher than I ever wanted ta be with ya."
    "And? So what? You kind of liked how rough he was."
    e "That's fine! I liked it a lot."
    "Once again, your words do not have their desired effect on Cane."
    "Although he looks tempted, he still hesitates to agree with you."
    c "I'm glad, lad, but..."
    c "I lost control of myself."
    c "I told myself I wouldn't let things go this far, that I wouldn't make the same mistakes I made with Topu, and yet... here we are."
    "Taking a moment, you remember that Topu was the original owner of your apron - the one that disappeared."
    e "Well, yeah, we took things a little fast, but... that doesn't mean the same stuff is going to happen again."
    "Cane briefly looks lost for words."
    c "Maybe, but... yer too fine a lad ta risk havin' that happen to just fer some sex."
    c "Yer worth far too much for that."
    "There's a brief pause, before you hear him mutter to himself."
    c "...even if it were some damn good sex."
    "Silence lays between you for a bit. Neither of you know what to say now."
    "You both just... sit there, cocks softening, and precum drying on your fur."
    e "Well... even if you don't trust yourself, I trust you."
    "Cane pulls his gaze away from the floor, eyes instead turned to you with a lost look you'd never thought you'd see on his face."
    "It... hurts to look at."
    "A person as confident and boisterous as Cane should never look this defeated."
    "He lets out a deep sigh."
    c "Thank ye lad. I dunno if I can say the same for myself."
    "Silence falls once more, as you both fidget slightly, waiting for the other to speak."
    e "... I really did enjoy this, and I very much don't want this to be the last time this happens."
    "Cane looks deeply uncomfortable."
    c "I know lad. I enjoyed it a great deal as well."
    c "...Too much, even."
    c "But we shouldn't be doin' this if there's nothin' to stop me from goin' too far."
    "You can sort of see where he's coming from, though you think he also might be worrying a bit too much."
    e "Well... if you could do stuff like this without going too far, would you want to...?"
    "Cane heaves a deeply conflicted sigh."
    c "I'm not sure lad. I know it would feel amazin', and I very much want ta in that sense, but..."
    c "Even then I'm not too sure if I could be trusted with ya. I'd need some time ta think about it."
    e "I think I might have something we could try out...?"
    "It's hard to keep the doubt out of your voice, but you do your best to sound convincing."
    c "I'm listenin'."
    e "If you can't trust yourself not to go too far, you can tell me how far you're willing to go, and have me stop us from going there - that way we can have some sort of check in place."
    "Cane closes his eyes to think about it."
    "The look on his face tells you he's quite worried about this, but the way his dick is starting to chub up again tells you that he's definitely considering it."
    e "We can try it this time, and if we ever go too far, we don't do anything like this again, okay?"
    "With that, Cane lets out a short huff, and turns to look at you."
    c "...Okay."
    c "I'm not sure if I'm comfortable relyin' on it, but I'm willin' ta try it out."
    "Right as you're about to celebrate, Cane lifts a finger in warning."
    c "This might be unfair, but... if things go too far, we're definitely never doin' somethin' like this again, okay?"
    "You nod emphatically."
    e "I understand 100 percent."
    "Cane gives you a slow nod."
    c "Alright, well... ya got any things ya want as limits?"
    "He takes his pillows, and props them so that he has something to rest his head against while he talks to you."
    e "Nothing I can think of!"
    "Especially not while his hard cock is less than a foot away from you, with nothing but air in the way."
    "Cane sighs, before letting out a small chuckle."
    c "Of course ya don't."
    e "And what about you? What are your limits?"
    c "Hrmm..."
    "You can see Cane's brows furrow in thought, though his hands are drumming out a gentle little rhythm on his belly."
    c "I think I'm okay with most'a the things ye can do with yer hands. I just don't want to get on top of ya, or be anywhere near yer mouth or ass."
    "Mostly what you expected, but..."
    e "Why, you don't like them?"
    "Cane gives you a skeptical look."
    c "No, ye know as well as I do what I think ah those."
    e "Maybe, but I still want to hear you say it."
    "Cane brings his hands up to his face, taking a deep breath."
    c "Lad. Stop makin' this difficult."
    c "I'm tryin' {i}not{/i} ta fuck ye inta next week, stop makin' me want to so bad."
    "As he says this, he gently strokes himself a bit, as if trying to get a bit of relief from his urge to destroy your ass."
    e "Fine, fine. I'm happy with those conditions."
    e "...Are a few spare licks here and there acceptable? It's fine if not, but I'd... really like to."
    "Cane closes his eyes for a long moment."
    c "Maybe. I'll give ye a yes or no when it comes up, but at most only lickin' ta get a taste."
    c "No actual suckin' me off, got it, lad?"
    "You nod rapidly."
    e "Absolutely!"
    "Cane heaves out a long breath, before returning to stroking himself slowly."
    c "Alright lad, well... this is still yer reward from earlier, so ya get ta choose what ya want ta do within my limits."
    "A naughty idea crosses your mind, a way to get some of what you want without breaking his limits."
    e "I wanna have you right there, and jack both of us off with my head right there to get a good look, smell... and if you let me, taste."
    c "Yer almost as greedy as me, lad."
    e "Maybe, but I do want it pretty bad."
    "Cane lets out a deep growl."
    c "Get down there and stop talkin' before I fuck that pretty face ah yours."
    "Even letting you take the lead, Cane finds a way to remind you who teases who around here."
    e "Don't have to tell me twice."
    "You move down to the foot of the bed, and crawl back on, on your knees."
    "Cane shifts his legs open to give you room to move forwards."
    "You move closer and closer to the big bat, looking straight into his teasing grin."
    scene black with dissolve
    pause 2
    scene canefavour001 with dissolve
    e "You look like you're having a good time. What happened to all that apprehension?"
    "Cane lets out a deep rumble of a laugh, tinged with a bit of bitterness."
    c "'S still there, 's just a nice view from up here."
    c "Ya look good between my legs."
    "Fuck. That made you twitch just a little with excitement."
    "Can't let him get away with that without some revenge."
    e "The view from here is great too... maybe I should show you something similar sometime."
    "You've paused at this point, too focused on teasing the bastard of a bat to keep going."
    "Cane seems just as interested in the back-and-forth you've got going on, as you see his cock leak just a bit more pre-cum with every line."
    c "Hah! Good one lad."
    c "Maybe ya will, but... I think we know what ya prefer."
    "His grin stretches to go from ear to ear, a look of triumphant avarice."
    c "There's a reason ye asked for this, and not that."
    "He got you there."
    "You're not going to be able to beat him if you keep teasing each other like this."
    "However much both of you are enjoying this, you need to get to the main event before he reduces you to a submissive puddle with no impulse control."
    "Resuming your crawl forwards, you finally reach a comfortable spot in front of the bat's cock."
    "You have to stop yourself from reaching out and slipping his tip between your lips."
    "Instead, you move your face closer to his shaft, until your snout is tickling its underside."
    c "I see yer gonna prove me right with yer actions rather than yer words."
    c "More than fine by me."
    "Goddamnit, why does his confidence have to be so hot. It makes it that much harder not to get him to fuck you right now however you can."
    "For now, you're going to have to settle for this."
    "You wrap your hand around his cock, its girth working to your advantage, as you have space enough for both it and the tip of your snout."
    c "Fer somethin' someone else picked, this really is quite indulgent ta my tastes."
    "In response to his gentle ribbing, you gently slide his foreskin off of his tip, and press your snout closer so that your breath teases against his skin."
    c "F-fuck... got it lad, ye can tease too."
    "Smirking, you begin gently pumping his cock, letting your snout meander up and down his shaft, just barely stimulating enough to feel good, but bait him into wanting more."
    menu:
        "What do you do...?"
        "Begin licking his cock":
            $ cane_lick = True
            scene canefavour002 with dissolve
            "Right as your cock reaches the base of his shaft, you bring out your tongue, gently dragging it up to the tip."
            "You feel Cane briefly tense up, but give in to the moment."
            "When you get to the apex of your climb, you encounter a fresh glob of pre, beckoning for you to get an even better taste."
            "Ever so slowly, you trace a swirl around his head with your tongue, slowly reaching further and further down as you push his foreskin off of his tip."
            c "Yer drivin' me crazy down there. Any more than this and I dunno how much I'll be able ta hold back."
            "Taking that as encouragement, you finally bring your tongue below the ridge of his head, leaving it fully exposed, right in front of your open maw."
            "A deep flavor of sex and lust clouds your mind and his, as you bob your head down further, sliding his tip between your lips, and against the roof of your mouth."
            c "L-lad, Tha-"
            "Not letting him protest further, you push down even further, fitting half of his cock down your throat, feeling its girth greedily devour as much space as it can in your mouth."
            "Cane groans deeply, a groan of needy, ill-restrained desire."
            "Soon, you feel a pair of web hands grab you by the horns."
            c "Fine, ya want ta suck my cock that bad, ye can suck my cock the way {i}I{/i} like it."
            scene canefavour008 with dissolve
            "So saying, your face is shoved down against his belly."
            "Your eyes tear up, and you struggle not to cough as his cock slams down into your throat, bending both itself and your trachea to fully accommodate it."
            "Before you can fully process any of this, Cane pulls you halfway off his dick once more, pushing forwards all the while to make sure you're stuck there as he gets off of his back and onto his knees."
            "At this point he has your head forced down onto his cock, as your body spasms trying not to tense up."
            "Seeing this, Cane relents slightly, pulling you off his cock."
            c "Ye alright lad? Enjoyin' what ye've earned yourself?"
            "You nod in between your coughs and splutters, trying to catch your breath."
            c "I thought so. Now, on your back."
            "His tone of voice makes it clear that if you don't do it, he'll make you do it, so you flip over onto your back."
            with vpunch
            "Cane takes this opportunity to kneel with his ass against your chest, cock laying flat against your face."
            c "Good. Now, open your mouth."
            "You oblige, bending forwards as well to try and take his cock into your mouth on your own terms."
            "Unfortunately, you're not given enough time."
            "Cane leans forwards into a position much like yours earlier, balling his hands into fists for support far above your head on either side."
            "Unlike when you were in that position, there's no cock in front of him, but a throat below him."
            "He slams his hips forwards, driving his cock into your open maw, immediately hilting it, his balls slapping the bottom of your mouth."
            with vpunch
            "He lets out a satisfied groan."
            with vpunch
            c "Ffffuuuuck. That hits the spot."
            "He yanks his cock out of your mouth so that only the tip stays inside, before slamming back in again, each repetition punctuated by the slap of his balls against your chin, and a similar statement from Cane."
            "None of it is praising like earlier. It is entirely devoted to how good his cock feels using a throat like yours."
            "Turned on to all hell and back, you begin jacking off underneath him."
            "Over and over again, he slams his cock into you with no regard for anything but your basic wellbeing, until finally, he shoves in, and doesn't pull out."
            "You hear him grunt, and feel his cock spasm throughout your snout and throat, a warm and heavy sensation punching deep in your throat."
            "Having him this deep inside of you this long makes you start to run low on oxygen."
            with flash
            with flash
            with vpunch
            "The lightheaded feeling of both unbridled lust and asphyxiation push you to the brink, causing your own orgasm to spray cum all over your belly."
            scene canefavour009 with dissolve
            "Cane doesn't pull out his cock until he's sure his orgasm has well and truly finished."
            "You don't know that for sure of course, you passed out before he finished, but you have a feeling."
            scene black
            pause 5
            scene canebedroom with dissolve
            "You wake up to a fully dressed Cane staring at you from a seat in his bedroom, cigar once more perched between his lips."
            show cane normal with dissolve
            c "Clean up."
            pause 2
            e "W- but I just woke up?"
            c "Yes lad, but yer my employee, and cute as ye are, ya need ta clean up."
            "Well, at least he's still calling you cute. Even if the way he says it isn't filled with as much affection as it was before you sucked him off."
            e "...Are you mad at me...?"
            "Cane sighs heavily, pinching the bridge of his nose and furrowing his eyebrows in a face of pure exasperation."
            c "No, lad. I'm not mad at ya."
            c "I'm mad that I let things go that far."
            "A touch of the frustration in his expression disappears, replaced instead by sadness."
            c "And irritated that I let myself believe we could figure somethin' out."
            "You pick up your clothes off the floor, and look at him questioningly."
            e "I thought you had fun?"
            e "I know I did."
            "Cane frowns deeply, taking his hand away from his face."
            pause 2
            c "Yes lad, I had fun, but that wasn't healthy."
            c "Yer my lad, and it's my responsibility to take care of ya, and not have ya meet the same fate as Topu."
            if canerahim > 0:
                c "Promised Rahim that, and look at me now."
                c "He'd be even more right than he was that I can't be trusted with ya if I let this continue."
            c "We're not doin' this again."
            c "Yer still welcome at the bar, and still my valued lad, but."
            "Cane gestures around."
            c "None ah this."
            e "We could-"
            "Cane raises a hand in frustration."
            c "We agreed on the terms, and we couldn' keep 'em."
            c "Please, just... no more. I'll keep teasin' you in front of patrons to keep up appearances, but that's as far as we'll go."
            pause 2
            "Oh."
            "You visibly deflate, and you're pretty sure Cane saw it, from the way he looked guiltily at the floor."
            e "I understand."
            "You quickly put your clothes on, the room heavy with lingering regret."
            "..."
            "There's only silence in the room, neither of you are willing to break it."
            "You leave the room before Cane can catch you crying, but... you're pretty sure he knows."
            scene black with dissolve
            "Not wanting anybody to see you as you are, you sneak home, making sure Seb and Ole aren't there before heading upstairs to clean up and get some rest."
            pause 2
            "After you wake up, you realize you left your apron in his room."
            "Opening the door to the bar to retrieve it, you see a horribly drunk Cane, moving around the bar with a cheer that seems real to all but you."
            pause 1
            "Near the door is the apron."
            "You pick it up and take it home."
            "When you open it on the way there, you see a small note on it."
            c "I'm sorry for what happened. You're always welcome in the tavern, but... I'll do whatever I need to to keep what happened to Topu from happening to you."
            pause 2
            "Maybe it would be good to spend the day at home - give yourselves more time to shore up and act like everything is okay."
            $ timenow.day += 1
            $ timenow.hour = 7
            $ timenow.passTime()
            jump main_bedroom
        "Ask Cane if it's alright to use your tongue":
            $ cane_lick = False
            e "So, Cane..."
            "You take your time asking the question, letting him get more and more riled up."
            c "Yes, Lad?"
            "The bastard knows what you want to ask, and is trying to act like he wasn't huffing and grunting a second ago."
            e "How about that question from earlier?"
            "Cane gives you a smirk. You give his cock a tug, quickly destroying the smirk."
            c "I should say no as punishment fer all the teasin', but yer too cute fer that."
            "He reaches down with his hand and ruffles the back of your neck, before gently guiding you back to the underside of his shaft."
            c "'S long as ye don' use yer maw, go wild, lad."
            "He stops guiding your head, but leaves his hand resting on your head, gently rubbing his fingers through your fur."
            "To let him know you heard him, you gently slip your tongue forwards, and press it against his thick, purple skin."
            "You hear a contented huff above you, as Cane really gets comfortable, resting his other hand on his belly."
            "Cane's cock is lathered in a salty-sweet mix of sweat and pre, the taste heady enough to overwhelm you if you're not careful."
            "To make sure that doesn't happen, you make sure to savor it."
            scene canefavour002 with dissolve
            "The first lick was just to test... slowly, you work your way up the shaft, gradually working towards the shaft."
            c "Mmmh, just like that, lad..."
            "You feel him gently massage the back of your head with his fingers."
            c "'s nice... makes me wanna make this last a while."
            "Despite that, you feel the sickly sweet taste of fresh pre drip onto your tongue."
            e "I've been waiting a while for this, so fine by me."
            "Cane looks down at you in surprise, before further ruffling your fluffy fur with his rough, calloused hands."
            c "How forward, lad!"
            "He continues looking down at you, watching you carefully lap up his pre with your tongue, never quite reaching for his tip, for fear that it'll mean you've run out."
            c "Hrmmmm... lad?"
            "You pause, still holding his cock, but moving your head up to look at him."
            "He seems to be blushing?"
            c "Ye can kiss it if ye'd like. Still no maw, but... should be alright ta feel yer lips at least a little."
            "You're not going to say no to that, but... it might be good to check."
            e "Are you sure? Isn't that going against our original rules?"
            "Cane scratches his belly, looking a bit embarrassed."
            c "'s fine. It doesn't break 'em... just bends 'em to our advantage a bit."
            "During your short exchange, Cane's cock had oozed out a fresh trail of pre down his cock, this time reaching down to his balls."
            e "...alright. Stop me if it gets to be too much."
            "Given your newly vested power, you immediately return to Cane's cock."
            "You figure the best start is to pull Cane's foreskin back up once more, pooling the pre on his head into one small spot."
            "Ever so gently, you move your head down to that spot, and lick between the folds of foreskin present there."
            "Your reward is a cloying sweetness that elicits some pre of your own."
            "Wanting more, you pull his foreskin down, and begin the arduous process of kissing around his head, lubricating your lips with his pre as you jack him off."
            "All the while, Cane is rumbling contentedly above you, whispering praise about 'how good a lad ye are', and 'how well yer doin'"
            "It's a slow and sweet few minutes of exploration for both of you, Cane fully exploring your head with his hands, as well as your lips and tongue with his cock - you exploring his cock with your hands and mouth."
            "You can't do this forever though, as much as you want to. You need to actually move forward rather than just soak in the feeling of having Cane dote on you like this."
            "Giving his head one last kiss, you begin kissing your way down his shaft."
            "The further down you move, the more space you have to properly jack the bat off, increasing the power and speed of your strokes as you move closer to his balls."
            with vpunch
            "Cane's sounds and praise have only grown louder and sweeter, groans turning to baritone growls, his voice husky with breathless desire as it tells you how wonderful you are."
            "Eventually you do reach down to Cane's balls."
            "You take a short moment to appreciate that fat purple orbs in front of you, watching as they pull up slightly every time a new spurt of pre comes out of his tip."
            c "Feel free, lad. I like havin' those played with."
            c "Fair warnin' though, I'm close, and ye might get caught in the splash zone if yer not careful."
            "You don't even have to look up at Cane to know he's got a sultry smirk on his face."
            e "Sounds like a plan to me."
            "Cane's balls briefly tug up once more, cock throbbing in your hand."
            c "Good lad."
            "Given all the encouragement you need, you take your free hand and use it to gently tug on his balls."
            "Moving your head down, you get a good angle to gently lick and kiss his sack, getting a fresh taste of sweat and pre mixed together."
            "You've been pumping his cock with fast, steady strokes the entire time you've been doing this."
            "On the other hand, Cane has stopped speaking, transitioning fully to groans, grunts and growls."
            "When you look up to him, you see that he's leaning his head back into his pillows with his eyes closed - losing himself in the feeling of you jacking him off."
            "He cracks an eye open to grin at you as he's noticed you've stopped cleaning him with your tongue."
            with vpunch
            "You feel a gentle tug from the everpresent hand on your head, as it transitions away from just petting you to guiding you to what he wants."
            "Letting him take control, you find your nose pressed firmly beneath his balls, so that they hang on either side."
            "You feel his hand come closer to the side of your cheek, indicating that you should get to licking and kissing."
            "Obedient dragon that you are, you alternate between licking the underside of his balls, and tugging on his sack with your lips."
            "Slowly but surely, Cane begins guiding you up his balls, further and further."
            "His balls have been tugging up more and more often, and his groans have begun to grow more vocal than even before."
            c "Last call fer ya ta get out of a face full ah bat cum, lad."
            "In response, you begin kissing the base of his cock once more, jacking him off with renewed vigor."
            c "Hey, hey, hey! Hold yer horses lad, I had an idea I thought ya'd like, gotta hold it in 'til then."
            "You huff out a disappointed breath, slow your pumping and kissing down to a gentler pace."
            "Cane pets you affectionately in response."
            c "Good lad. Now, c'mere."
            "Once more, his hand begins to guide you further up his cock, prompting you to lather it once more in hungry licks and kisses."
            with vpunch
            "The mixture of sweat and pre grows sweeter as you move up, reaping the results of your time with his balls as you move up."
            "The pre itself is also stronger than before, taste deepening as he gets closer to his threshold."
            "Before you know it, you're back at his head, foreskin and tip fully lubed and glistening."
            c "Alright lad, I'm gonna need ya ta open yer mouth when I tell ya to, okay?"
            "Cane talks to you in a voice shaky with effort and lust."
            "You nod, but never stop your pumping, licking, or kissing."
            with vpunch
            "The hand on your head shakily drags you up to the very tip of his cock."
            with vpunch
            "With the better view afforded here, you can see how Cane's stomach tenses and relaxes with pulses of lust."
            "The hand on the back of your head grips you tightly and shoves your lips flush with his tip as you see a particularly strong pulse rock his body."
            with vpunch
            c "{i}Mnng!{/i} Here comes that reward 'a yours, open up lad."
            with vpunch
            "You happily oblige, lips parting moments before the first spurt of cum exits Cane's cock, only to be caught in the back of your throat."
            with vpunch
            with flash
            with flash

            scene canefavour003 with dissolve
            "Cane's body is rocking and twitching so hard that you can't realistically catch everything in your mouth, some of his spunk spraying across your muzzle."
            "Every drop you catch is rich, a deep, bitter tasting rush of flavor accompanied by a heavy warmth in your mouth."
            with flash
            "Cane has completely lost himself in the moment, calling out your name between groans as he holds your head in place, hips bucking, just barely not fucking your throat at various points."
            "Unable to hold yourself back anymore, you move your free hand down to your own cock, which has been painfully throbbing in neglect this whole time."
            "You cum before Cane even finishes riding out his orgasm, the pervasive taste of his cum, as well as the denial you've given yourself up until now quickly pushing you past your threshold."
            with flash
            "Unfortunately, all good things must come to an end, as the gap between shots slows to a trickle, no longer enough to fill your mouth."
            "Drowned in a lustful haze, you barely notice yourself continuing to jack him off after he's already finished, licking all over his cockhead in the hopes of finding more."
            "An affectionate chuckle from above you snaps you out of it."
            "Looking up, you see a very satisfied Cane smiling down at you."
            "He finally takes his hand off of your head, and beckons you closer to his face with a finger."
            scene black with dissolve
            pause 2
            scene canebedroom with dissolve
            show cane naked with dissolve
            "You're both too spent for words, but Cane manages to express his feelings despite that."
            "As you get closer to his face, you see him lean forward slightly, silently asking you for a kiss."
            "As much as you want one..."
            e "Cane."
            c "Yes, lad?"
            "You're both still panting, talking between labored breaths and grins."
            e "You know that-"
            "You cough, needing to take a breath."
            e "That I can't see a kiss here as anything other than romantic."
            "Cane's eyes widen in surprise. You see a hint of affirmed desire in there as he starts to lean forwards for a kiss again."
            "But, right before you actually close the gap between you, he stops you with a hand."
            c "I'm gonna to have to think on that, lad."
            "You can't help but feel a bit... disappointed, a feeling you're quickly snapped out of as you feel Cane's finger brush across the top of your snout."
            "At first you think it's a just a kindhearted caress, but when you see his finger again, it's right in front of your mouth, with the cum on your face slathered on it."
            c "I said I'd think on it. Be a bit patient, lad."
            "Despite that, he nudges his finger towards your mouth - you oblige, gently sucking his cum off of it, rich taste once more flooding your mind."
            c "Fer now, all I can say is that ya did great... I might not mind doin' somethin' like this again sometime."
            "As he says this, he takes his finger out of your mouth, briefly disappointing you before you feel it wrap around your back a moment later, as his other hand wraps around your waist."
            e "I think I'd like that too."
            "Cane doesn't miss the slight sarcasm in your voice, calling him out on his sarcasm, his belly rumbling with you on top of it, vibrations rumbling through you."
            c "Fine, fine. I'll let ya hear it."
            "Cane moves the hand on your back so that his elbow stays on your back, but his hand moves up to tuck your head under his chin."
            c "That was great, lad. If it weren't fer my reservations from earlier, I'd be askin' ya what nights yer free ta do more of this."
            "It's nice to bask under his praise like this..."
            e "Mm. You mean about not turning me rotten?"
            "You feel a twinge of tension go through Cane's previously completely relaxed body."
            e "I wouldn't worry about it. Even if you could, I wouldn't let you."
            "And like that, you feel the belly under you return to its softer form - Well, as soft as something covered in rough fur can be."
            "Cane begins rubbing the back of your head with his thumb, thinking."
            c "Lad, I can't tell ya for sure if I wanna do this again, even if yer right that ye wouldn't let me ruin ya."
            c "Had fun, but I ain't too keen on anythin' beyond the casual. An' before ye say anythin' ye know as well as I that ya wouldn' be able ta keep it casual."
            "You grumble faintly into his fluffy neck fur."
            c "I told'ja I'm gonna think on it."
            "You grumble louder, so your voice is actually heard this time."
            e "Okay... is there nothing more we can do until then?"
            "Cane's hand briefly pauses, before resuming as if nothing happened."
            c "...We can stay like this if ye like fer now."
            "His voice becomes slightly embarrassed, an ill-fitting sound for his gravelly voice."
            c "Consider the night as part of yer reward."
            "Not wanting to move from your comfortable spot nestled deep inside Cane's fluffy mane, you mumble out a muffled response."
            e "I'll just go to sleep here if that's okay with you then."
            "Cane chuckles before clutching you closer, so that you fit more snugly on him."
            c "I'd normally go take a bath before that, but I have a feelin' ya'd rather fight 30 landsharks than move from where ya are."
            "You give him a tiny nod. It was meant to be an emphatic one, but that was rather difficult given the tiny hollow you'd fit yourself into."
            "Cane laughs as you don't even rise to the bait, and just admit to it."
            c "Alright, alright, since ye were so honest about it we can just take the bath tomorrow mornin'."
            c "Gotta make sure my lad is nice'n clean fer work, don' I?"
            "Mmmmmmhm... Whatever... you...... say."
            "Everything goes dark as you slowly sink into sleep."
            scene black with dissolve
            pause 2
            "..."
            "The last thing you remember is warmth."
            "Cane's entire body radiated heat like a furnace, since its fur couldn't count on retaining it for him."
            "That'd normally make you feel uncomfortable, but... it feels like being in front of a happy hearth with a loved one."
            "Fading into the soft, warm bed that is Cane, you spend the night in his room, safely wrapped in his arms."
            "..."
            "You let out a colossal yawn as soon as you wake up."
            scene canebedroom with dissolve
            show cane naked with dissolve
            c "Tired already?"
            "You jolt, hopping to your feet, already off the bed."
            "Looking at where you were, you see a rather amused Cane."
            e "Sorry, I forgot where I was! I'm used to sleeping in my room at the King's Pawn."
            "Cane raises an eyebrow with mock skepticism."
            c "Surprisin', given how much ya sleep around."
            "You flush red. He's... not wrong."
            c "Mm, well, I don't mind the end result - we needed to get outta bed soon anyway."
            e "Is it opening time?"
            "Looking out the window, the sun is fully up..."
            e "Wait, shouldn't you be working in the tavern right now? These are business hours for you."
            "Cane yawns in response."
            c "I could use the rest, especially after a night like that."
            "Cane throws you a playful wink before shaking his head."
            c "Not really, it's just that I haven't taken a day off in what feels like months, so... I decided it might be nice."
            "It's really hard to tell if he means this, or if he was just trying to let you sleep a little longer, but... you're not going to get the answer out of him either way."
            e "Well, I'm glad you're taking time off... especially because I dunno if I want all of the patrons to tease me more about what we do together."
            "Cane let's out a hearty chuckle."
            c "Oh, lad... I'm sorry, but it's impossible to stop the rumors in this town."
            e "...I guess."
            "Seeing you pause pensively, Cane gets out of bed and pats you on the shoulder."
            c "Alright, while yer thinkin', why not get yerself cleaned up."
            c "There's still dried cum all over yer chest."
            "Looking down, you see that he's right - your fur is matted and clumped with cum."
            e "Alright."
            c "I'll give ya the keys to the inn's tub fer now - might not have much water, but there's a bucket ye can use to get the worst off, before gettin' home and finishin' up."
            "So saying, Cane walks over to his pants, fishes in its pockets, and pulls out a key."
            c "Here."
            "He walks over and affectionately ruffles your head."
            c "If ya wanna keep it a secret, I'll keep actin' how I always do, but..."
            "He winks."
            c "Well, we'll see how long we can keep that up for."
            scene black
            pause 3
            $ timenow.day += 1
            $ timenow.hour = 7
            $ timenow.passTime()
            if _in_replay:
                $ renpy.end_replay()
            jump main_nocturnaltrunk


label Cane_Ask_Goat_Tribe:
    $ opinions_GoatTribe[4] = 1
    e "...Cane? Have you heard of... the letter?"
    c "Ye, ye. The lion spread around the news yesterday like strawberry jam on my bread."
    e "Hmm... What do you think?"
    c "The Ram is a good lad... What's his name again? F-far? Fuck? Furk- Furkan."
    e "Yeah, have you met him?"
    c "Ye ye. Yer ass was not here when we're kinda buddy buddy with the goat Tribe."
    c "He's the son of the leader, our hero Lothar killed that bastard when they invaded us though."
    e "I-I see... Do you trust them?"
    c "Look, I still got myself some secret ingredients from them."
    c "So... perhaps a yes."
    c "But they're doing some shady things around our forest, I guess, so ya be the judge."
    e "Oh... Alright, thank you so much for the information, Cane."
    c "No problem, good lad."
    jump Cane_Normal_Talk

label Cane_Event_Patron_Show:
    "After a hard day of working at the tavern, you walk over to the counter to get your pay."
    "As Cane hands you the gold, he stops you for a moment."
    c "Wait- care for a proposal, lad?"
    e "What is it, Cane?"
    c "Let's say... Yer service at the tavern has drawn quite a bit of attention."
    c "I've gotten a lotta requests... for a private show."
    e "Private show? What does that mean?"
    c "It means yer gonna put that body to use and spend some quality time with patrons who have ya ass reserved... for their enjoyment."
    "The idea makes your face blush cherry red."
    e "H-huh? But... Why would I do that?"
    c "Money?"
    $ pc.gold += 50
    c "...And ah get the feelin' that yed have a good time doin' it."
    "Cane gives you a wink, and purposefully looks down at crotch"
    c "Don't think I can't see mah special lad perkin' up at the idea down there."
    "If you were cherry red before, now you've somehow hit a shade of red brighter than a raspberry."
    c "Cute as it is to watch ye flounder all embarrassed like, I do got to get back to work at some point."
    c "These goons're gonna be payin' extra to spend some quality alone time with my tavern's star server."
    e "W-would people really pay for that?"
    "Cane gives you a skeptical look, only to grin devilishly when he realizes you're being genuine."
    c "My lad, ya have no idea how many people in this here tavern want a piece of ya."
    "You are too shy to respond."
    c "Anyway, I know this is a lil' sudden. Why don't ya go and sleep on it? No pressure."
    c "Just talk to me... if ya tight on money, or wanna have a good time."
    e "I- Uh... I'll think about it..."
    c "Think on it, my lad. I wouldn't hold a grudge... It's yer choice, and I won't push ya either way."
    c "Yer my special lad, I owe ye at least that much."
    c "But do make sure yer ready if ye say yes."
    c "Because once you've taken their money, the patron'd be yer king... mmhmm..."
    "Suddenly, Cane walks out from behind the counter, and gets up behind you, making sure to look you in the eyes, continuing only when he sees your approval."
    "He grasps your hips lightly before brushing his hands up your side and whispering in your ear."
    c "Let 'em have the time o' their life with me sexy lad."
    $ privateshowing = 1
    jump main_nocturnaltrunk


label Cane_Private_Show_Quest_Accept:
    e "Cane, I think I'll accept doing the private shows."
    c "Heh, guess I was right about ya."
    "Cane nonchalantly smacks you on the ass, eliciting a surprised yelp out of you."
    c "Very nice, kid. Know that yer gonna make them very happy."
    "Your face reddens."
    e "So... When do I start?"
    "Cane chuckles."
    c "Not so fast, me sexy lad. We'll do them in the backroom."
    c "Cause, ya know.. We don't wanna make a mess in the guest rooms. That be bad business."
    c "I've cleared out a space for ya, but we need to spruce it up some. Ya know, make it look all prettylike to match ye."
    c "Ye'll also need somethin' more suitable to wear for the job..."
    c "Ye often won' be wearin' any, but ye know how it be, some patrons like the tease."
    e "That... sounds like a lot."
    c "Already done most o' the work. Only need ye to help with the finishin' touches."
    "Cane hands you a list. It's the recipe for pillows."
    c "'Ve moved some chairs into the room, but they're a bit nekkid. Believe me, ya don't want to have splinters in certain places."
    "Cane winks at you. Seems like he's had experience, or past mistakes with this before."
    c "So get'em done and we'll proceed."
    $ discoveredrecipe.append(cheappillowrecipe)
    $ QuestBegin(quest18)
    $ quest18.qProgress(__("Craft 2 cheap pillows"), "Cheap Pillow", 2)
    jump main_nocturnaltrunk

label Cane_Private_Show_Quest_Finish:
    e "Cane! I've got the... pillows."
    c "Ah...lemme see."
    c "Well done with the preparations, lad."
    c "Everything is set up and ready."
    c "In the future, just come to me and I'll inform you if there's any patron that needs attending in the backroom."
    $ removeItem("Cheap Pillow", inventory, 2)
    $ QuestFinish(quest18)
    jump main_nocturnaltrunk

label Cane_Private_Show:
    "Cane ruffles your hair, and smacks your ass, ushering you to the back of the tavern."
    $ rwegw = renpy.random.random()
    if rwegw < 0.34:
        $ tavern_date[0] += 1
        call Scene_Tavern_Meet_01 from _call_Scene_Tavern_Meet_01
        $ pc.lust = 0
    elif rwegw < 0.67:
        $ tavern_date[1] += 1
        call Scene_Tavern_Meet_02 from _call_Scene_Tavern_Meet_02
        $ pc.lust = 0
    else:
        $ tavern_date[2] += 1
        call Scene_Tavern_Meet_03 from _call_Scene_Tavern_Meet_03
        $ pc.lust = 0
    if tavern_date[0] + tavern_date[1] + tavern_date[2] == 1:
        if isNight():
            scene nocturnaltrunk_night
        else:
            scene nocturnaltrunk
        show cane normal with dissolve
        c "Hey, kid. Here's the payment for the job."
        "You take the money."
        c "Must'a put in quite a bit of work, eh?"
        "Cane gives you a wink and a smack on the ass."
        e "Eep!"
        c "I could 'ear the voices from 'ere"
        "You're embarrassed to death, but you can't let Cane get away with this much teasing without trying to get some in return."
        e "Maybe I wanted you to hear."
        c "Well if ya did, ya did a good job of it."
        c "Me an' 'alf the tavern heard yous goin' at it."
        c "Sounded like ye did a good job, 'specially if the patron's faces were anything to go by"
        "Cane lets out a hearty laugh, before lowering his voice a bit."
        c "Can't say I blame 'em with a lad like you."
        "Having looked down from how flustered you were, you notice a particular protrusion and wet spot on Cane's pants."
        e "Looks like they weren't the only ones that enjoyed the show. Bet you were thinking about getting in there sometime too."
        c "Hah! Don' get ahead o' yourself lad. Ye'll need more than that to woo this old bat."
        c "Ye keep this up, and soon enough the backrooms'll be more popular than the front of the tavern!"
        "You blush."
        e "I... I only did what felt natural."
        c "Chin up, lad, ye did a great job, just like I knew ye would."
        c "Did ye make sure to clean everythin'?"
        e "I did."
        "Cane once again ruffles the fur between your horns."
        c "Good lad."
        "His voice is unusually warm when he says this, his husky voice tinged in a way you never heard before."
        c "Things keep goin' this way, we might need ta add some new features to the tavern soon, to highlight our star lad, ye know."
        "Your body heats, and your face flushes red with equal parts excitement and embarrassment from the potential inherent to that sentence."
        e "You got it, boss."
        c "Jus' call me Cane, lad. Ye deserve at least that."
    else:
        "Cane greets you with a ruffle of the head when you leave the backroom."
        c "Ye did a great job, my lad."
        e "Well... I can't say it's not fun."
        "Cane lets out a gruff laugh."
        c "'S easy to tell, ye keep comin' back for more."
        c "Well, I won't stop ye, 's good business."
        e "I have a feeling you get a bit more than money out of this..."
        c "Won' deny that. 'S nice to see ya like this, lad."
        "Cane flicks his eyes down to the tent pitched in his pants, where the thick outline of his cockhead is clearly visible. He leans in to whisper, warm breath tickling your ear."
        c "I know fer sure the guy down don't mind. 'F it were up to him, yed be comin' with me to the backroom to give me some o' that special service o' yours."
        e "I... wouldn't mind doing that at all."
        "You hear Cane tut, chastising your desire to rush, leaning away again to stop whispering."
        c "Enough talkin' 'bout this now. 'Ve gotta get back to servin' these layabouts."
        "Cane gives you a firm smack on the ass, and a devilish smile."
        c "Lookin' forward to yer next visit to the backroom."
    $ pc.gold += 100
    $ timenow.hour += 4
    $ timenow.passTime()
    jump main_nocturnaltrunk

label Cane_Ask_Lusterfield:
    e "Hey, Cane. What do you know about the village?"
    c "I know a lotta bout the village, [e]. Everyone talks to me about their little stories."
    e "How about the people here, do you know them?"
    c "Ya smartarse, of course I know them. Our hero, Lothar is our regular here, ya can probably see him here at night."
    c "And he has those bozos flying around him like flies buzzing around a piece of bread."
    e "Got it, what about Rahim?"
    c "That old bull? Why are ya talking about him, did he send ya here?"
    e "Uhhh... noo?"
    c "Ya wanna cause troubles, go to his old arse shop, eh? No wacky business here."
    e "Ok."
    e "How about the people in the shop?"
    c "Ya mean the lion? and the shopkeeper?"
    e "Isn't Sebas the shopkeeper?"
    c "I don't know, do I seem like the kinda man to visit a pawn shop?"
    e "Maybe?"
    c "Whatever, the lion comes here sometimes. I don't know when. Probably weekends."
    c "I usually can squeeze some rumours outta the lion when he's drunk. Like really drunk."
    e "Can you not do it when he's sober?"
    c "Ha, look at him. Ya think I'd bother with that. It's much easier talking to a drunk lion, like shooting fish in a barrel."
    e "What does that mean?"
    c "Whatever. The other one in the shop, Ole, we had a few talks, not much. He's siding with the bull."
    e "For what?"
    c "The trouble from the Goat Tribe, that bull thinks I'm some kinda snitch."
    e "But.... are you?"
    c "No, why would I. I have my whole business here. Ya think letting them wreck my home is a viable business strategy?"
    e "Did you explain to him?"
    c "No matter. It's been a few years."
    e "I'll try to see if you two can work out..."
    c "Don't bother, [e]. Yar wasting yer time."
    e "Hmm...?"
    c "Ahem... {p} You are wasting your time."
    jump Cane_Normal_Talk

label Cane_Ask_Tavern:
    e "Hey, Cane. Can you tell me the history of the Tavern?"
    c "Yea, yea, yea. People ask about this every time they come, like they found some gold treasure."
    c "This tavern has been here since the beginning of the village, like 80 years ago?"
    e "Woah that's a long time."
    c "My dad gave it to me when I was 20, somewhere ya age. I've been taking care of it for a whopping 37 years."
    c "This tavern is my everything, and I intend to keep it this way."
    e "Do you need anyone else to help out with the tavern?"
    c "Someone. Ya think finding a person to serve drinks is so easy? That's why I want ya to work for me just for a few hours."
    e "Mayber later..."
    c "Ha. Later it is."
    jump Cane_Normal_Talk

label Cane_Ask_Himself:
    e "Cane, how are you doing?"
    c "What chu think I'm doing?"
    e "Hmm... you were talking with your customer?"
    c "Wrong. I'm talking to a alleged dragon who comes here and get all the talks for free."
    e "Hey... look, look. I'll buy a drink later, ok?"
    c "Good. Don't waste my time with yer chit-chatting, [e]."
    jump Cane_Normal_Talk

label Cane_Dialogue_End:
    e "That's all. Thank you, Cane."
    c "Well, then enjoy ya stay in the Nocturnal Trunk."
    jump main_nocturnaltrunk

label Cane_First:
    hide screen menu_buttons
    if isNight():
        scene nocturnaltrunk_night
        with fade
    else:
        scene nocturnaltrunk
        with fade
    "A scent of alcohol and yeast infiltrates your nose as soon as you open the door, you try to pinch your nose under the strong alcohol as a purple figure emerges in front of you."
    show cane normal
    with dissolve
    my "Welcome to the Nocturnal Trunk, [e]."
    e "Hello- wait how did you know my name?"
    if el == "Goat":
        my "That hunky dunky Lothar told me a goat outsider disrespected him. Ya got the guts to mix up his name like that, [e]."
        e "I'm a dragon... but yes, that's me. Nice to meet you, uh- what's your name again?"
    else:
        my "That hunky dunky Lothar told me a goat fella came to good ol Lusterfield yesterday, it's gotta be ya name, [e]."
        e "I'm a dragon... but yes, that's me. Nice to meet you, uh- what's your name again?"
    c "Aye, lemme tell ya my name, it's Cone. I own this place. *burp* 'cuse me mister. Ya don't remember people's name don't ya?"
    e "I just arrived like yesterday... how can I remember everyone's name."
    c "How about this, mister. Wanna bet if you can remember my name next time ya come here?"
    e "What are we betting on?"
    menu:
        c "50 gold, that fair for ya? If ya don't get my name next time, That 50 gold is mine."
        "Yes{#canebet}":
            $ cane_bet = True
            e "Of course I can remember your name, you just told me."
            c "I gotta be sure ya can actually use ya brain, its only bets."
            c "But if ya lose and ya don't have the 50 gold for me. Ya will have to see what's gonna happen."
            e "That's so easy, Cone. You really think I'm that stupid."
            c "Well then, enjoy ya stay in the Nocturnal Trunk!"
            jump main_nocturnaltrunk2
        "No{#canebet}":
            $ cane_bet = False
            e "Not really, I don't trust your bet."
            c "Ya sure about that? Cause this is a one in a thousand years oppourtunity."
            e "No."
            c "Ok then, guess ya small brain is only reserved for lil wolf, not me."
            $ c = Character("Cane", color="#a1a281", who_outlines=[ (2, "#000") ])
            c "Look... my name is Cane, not Cone. What kinda stupid arse name was that anyway."
            e "Wait so you were lying after all."
            c "I reckon Sebas and Ole took ya in their lil pawn shop, must be a sweet dream living with those young boys ain't it?"
            e "Stop avoiding my question, Cane."
            c "Ya think 50 gold is that easy to earn, it was a simple misdirection. Plus, those goons in the shop would've given my name away one way or the other."
            e "You still lied to me, misdirection or not."
            c "Yeah, huh. What cha gonna do about it. Cry to your lizard daddy like he cried to that old bull bastard?"
            c "..."
            c "Ok, that was a lil too much even for my standard, how bout this, take the 50 gold and enjoy the rest of ya day."
            e "No."
            c "Look, take it or leave it."
            e "..."
            c "... 100 gold."
            e "Ok then. (You received 100 gold.)"
            c "My friend, ya got a bright future ahead of ya, [e]. Well then, enjoy yer stay in the Nocturnal Trunk."
            $ pc.gold += 100
            jump main_nocturnaltrunk2

label Cane_Second:
    if isNight():
        scene nocturnaltrunk_night
        with fade
    else:
        scene nocturnaltrunk
        with fade
    show cane normal
    with dissolve
    my "Welcome back to the Nocturnal Trunk, [e]. Ya remember my name?"
    $ cane_bet = 2
    menu:
        e "Sure, I think you are..."
        "Cona":
            e "...Cona? Is that right?"
            jump Cane_SoWrong
        "Cone":
            e "...Cone? Is that right?"
            jump Cane_Wrong
        "Ceno":
            e "...Ceno? Is that right?"
            jump Cane_SoWrong
        "Cana":
            e "...Cana? Is that right?"
            jump Cane_SoWrong
        "Cena":
            e "...Cena? Is that right?"
            jump Cane_SoWrong
        "Cane":
            e "...Cane? I've heard of your name elsewhere."
            jump Cane_Correct

label Cane_Apron_Quest:
    scene black
    if isNight():
        scene nocturnaltrunk_night
        with fade
    else:
        scene nocturnaltrunk
        with fade
    show cane normal
    with dissolve
    c "Ya bastard dragon. Come here."
    e "What's going on? Cane...?"
    "You follow Cane into the closet room. He picks up the apron you used to work from the dusty floor and shows it to you."
    c "Ya see the problem here?"
    e "Hmm... I don't. W-wait... there's a hole in the apron now."
    c "Yes ya dickhead. Ya broke my apron. T'is the only apron I have and ya broke it bad."
    e "I swear the last time I worked, it looked fine to me. Are you sure no one else touched it?"
    c "Ya think I broke it? Poked a hole in it like how yer shop friends poke yer hole every night? Only ya have touched it son."
    e "Uh... I didn't know... I'm so sorry."
    c "Ye... Well. I reckon yer not gonna have an apron when ya work."
    e "But... I thought your patrons liked the apron?"
    c "Aye, that's why I ain't gonna let you destroy it more. I'm putting it away until the end of time."
    e "Hey, Cane. I thought of a way to fix... the apron. Rahim, I'm sure he knows how to fix a hole easily."
    c "...No. Don't do it."
    e "How about I take it to him? I'll explain to him that it's my apron."
    c "He made the apron, ya cronky head. I can't take it to its maker who fooking hated me for no reason."
    e "I... You have to fix it one way or another. Do you really want to bring this secret to your grave?"
    c "Let it rest. It's ancient history."
    e "Is it really that hard?"
    c "..."
    c "Ya spoke like the finest lad I've met."
    e "Whoo?"
    c "The one who that fat bull made this apron for."
    e "Stop distracting me again..."
    c "It's true. I don't always get this unstoppable energy of young boys. But ya both took it to another level."
    c "That lad. I took him in during a thunderstorm."
    c "He was the greatest, the most passionate and generous being that I've ever seen."
    e "Was...? Uh... I'm sorry-"
    c "He's still alive, at least the last I've heard of. He used to be like you. But... the tavern, it corrupted him."
    e "Hmm... H-how?"
    c "It's me. Those little ten years he's spent here. I've made him this way.."
    e "Hey... Cane. What are you talking about."
    "Cane sighs, looking at the ceiling, he ponders for a second, you can feel his sorrow even when he doesn't shed a tear."
    c "I made him like me. The gluttonous, selfish me."
    c "The lad, he's gone, long before he actually left the village. But the apron, it's still something to reminisce, at least I reckon."
    e "It must mean a lot to you."
    c "Yes... I am who I am, [e]. That ya can't change."
    c "..."
    c "Take the apron to him."
    e "Wait... really?"
    c "Well were ya not insisting on licking his cock like a few minutes ago? Go take this dang apron to him."
    c "Hey, I got an idea. Wanna take another bet with me?"
    e "What? Cane are you drunk?"
    if cane_bet == False:
        c "Ya cowardly ass didn't even take one before, it's time. Say yes."
    elif cane_bet == 2:
        c "This time it's different, yer not betting on yerself, this is too easy."
    e "Uhhh... What's the bet...?"
    c "You think he would come back?"
    menu:
        c "I'll let ya ass decide, whatcha bet for 100 gold."
        "Yes{#canebettopu}":
            e "I'm sure he'd come back for you, Cane."
            c "Ya think so? I've been preparing the apron for him."
            e "I just want you to be hopeful."
            c "I'd have picked the same choice. I missed that lad so much."
            $ cane_lad_bet = True
        "No{#canebettopu}":
            e "Cane... you need to let him go... I don't think he's ever coming back."
            c "Huh...? Why not?"
            e "You said it yourself, that version of him you liked, was gone long before he left."
            c "Whatcha know about him anyway."
            c "However, I respect yer bet integrity."
            $ cane_lad_bet = False
    e "So... what should I do now?"
    c "Take ya apron. Tell that old fart I need a fix. Most probably he will rip the apron up like the old farty bull he is."
    e "Hmm... Ok. I'll let him know."
    c "And remember the bet between me and ya, sleazy ass."
    $ QuestBegin(quest07)
    $ quest07.qProgress(__("Ask Rahim for help"))
    $ addItem("Torn Tavern Apron", inventory, 1)
    jump main_nocturnaltrunk

label Cane_Sebas_Tavern_Night:
    "You go around, handing out drinks as per usual."
    "From the corner of your eyes, you see Seb slumped on the table in the corner."
    "This time, however, he seems to be betting with a handful of people at his table."
    "You shake your head. Typical Seb."
    "A stern glare pierces straight through you from the counter. While he was being toasted by the customers, Cane still had time to glare at you for slacking."
    "Fearful of Cane deducting your pay, you quickly hurry back to work."
    "The situation with Seb out of mind, you jerk in surprise as a commotion erupts in the tavern."
    "It's coming from Seb's table."
    "The group from earlier is shouting at a drunken Seb."
    patron "Hey, lion. Pay up! You owe us 1000 gold!"
    "The lion only grumbles unintelligibly."
    patron "Don't play drunk! We're getting that money today one way or another!"
    "You hurry to go help your roommate, but before you can, a shadow flies out from behind the counter."
    "Cane grabs the main aggressor by the collar, and easily lifts him off the ground with one arm."
    show cane normal with dissolve
    c "Just what do ye think yer doin' in my tavern?"
    "Cane sounds furious. Never in the time you've met him have you seen him raise his voice like this."
    patron "We... we just want to get... what the lion owes us."
    "Cane's face shifts into a mask of pure, visceral disgust, a growl entering his normally soothing voice."
    c "I can' tell if ye think I'm blind or stupid. I've been watching ya'll all evenin'."
    c "Ain't nobody gonna take advantage o' another Lusterfield citizen while I'm still around."
    c "Now do ya wanna get out of here walkin', or do ya want me to throw you out on yer asses to crawl like maggots?"
    "The troublemakers shiver in fear as the whole tavern rises up to support the barkeep."
    "Outnumbered, they quickly retreat."
    "Now that they're gone, Cane's face shifts mostly back to normal, though you still see his anger from the way his face is tensed rigid despite his smile."
    "Cane, waves you over."
    c "[e], come 'ere."
    "You oblige."
    "Cane gestures at the prone Sebas."
    c "Ah think the lion boy's 'ad too much to drink again."
    c "'e's not gonna walk back on his own like this, and I think yer not strong enough to haul him back either."
    "Cane has calmed down significantly at this point, his body language returning to normal."
    c "Why don't ya bring 'im to my room. I need to clear the table. Got a business to run 'ere."
    "You pick Seb up and off the table, and carry him to the room at the back of the counter."
    "The bed is made. You gingerly lay Seb down on it."
    "Seb grumbles something nonsensical."
    "You tuck him under the covers and return to work."
    "The night is drawing to a close. There were an unexpected number of patrons that night."
    "You were able to deflect most of the invitations to drink, but Cane was not so lucky."
    "He had drunk a lot. At closing time, he stood swaying at the door, reminding you of the first time you met him."
    c "Ye... Go home now... Good job... Today..."
    "You thank him but you're not quite sure if Cane understands you."
    "You walk back to the shop."
    scene black with dissolve
    "You enter the door. You walk past the counter. And..."
    scene kings_pawn with dissolve
    "Oh crap."
    "You've forgotten something, or rather, someone important."
    "You turn back and head to the tavern."
    scene nocturnaltrunk with dissolve
    "To your surprise, the tavern door is left unlocked. Cane was probably too drunk to remember locking it. Thankfully, Lusterfield doesn't have much crime."
    scene black with dissolve
    "Cane is not perched at his usual post behind the counter. Then again, that's to be expected. It's already past the tavern's business hours."
    "You move to the room you left Seb in."
    "You are about to call out either Seb's or Cane's name, when you hear a creaking sound coming from the room."
    "You pause at the door."
    "You perk up your ears. You believe you hear someone moaning. But whether it was Seb or Cane, you are unsure."
    "Curiosity compels you to ease the door open slightly."
    call Scene_Cane_Sebas_Tavern_Night from _call_Scene_Cane_Sebas_Tavern_Night
    "You pack a raging boner as you run back to the shop."
    "You rush into your room and quickly rub one out while the scene you saw is still fresh in your mind."
    "After the moment of ecstasy is gone, you calm down and ponder over what you saw and heard."
    "Seb always has your best interests in mind."
    "Cane might not look the part, but it seems like he has taken some sort of responsibility over you."
    "You feel warm... Spent from a hot night, you slowly drift off to sleep."
    jump bedroom_sleep


label Cane_After_Sebas_Tavern_Night:
    if sebcane == 1:
        $ sebcane = 3
    if sebcane == 2:
        $ sebcane = 4
    c "So, how did yer lion friend get home last night?"
    e "Huh?"
    c "I dragged him back."
    c "Ye weren't there to help."
    e "Did nothing else happen?"
    c "What do ye mean?"
    "Cane narrows his eyes at you."
    "You avert your eyes."
    e "Nothing."
    c "Good. What d'ya need? A drink? Wanna work ya job?"
    e "Maybe later."
    "That was close. You're lucky to have gotten away from that without more questions from Cane."
    c "Hey, [e]!"
    "You turn around and see Cane grin dirtily at you."
    c "Thanks ye fer lockin' the tavern door when you left yesterday night."
    "You blush as red as a tomato."
    jump main_nocturnaltrunk

label Cane_Apron_Quest_End:
    e "Hey... Cane. I've got your apron back, and no... he didn't rip it apart."
    c "Ya got the apron? For real?"
    c "Oh... look at this beautiful boy. All brand new. Yer the best laddity lad out there."
    e "What... does that mean?"
    c "Well I don't know. Since you're working in my place, I might as well give yer ass the apron you need!"
    e "I thought you were leaving the apron for your guy."
    c "I've been waiting for what? 4 years? No, he's not coming back, and I shouldn't waste my time waiting."
    c "Plus, I've got a much better substitute. Right here and then. No lie. Yer the best second finest lad I've had out there."
    e "What about the bet?"
    c "Ye, ye. Yer bet continues regardless of what I think, eh? Just take the apron."
    e "Thank you so much for the apron, Cane. I'd surely be hoping to meet your expectation of... uhh.. finest lad."
    c "Ya know what... It's actually funny, I blamed ya for breaking the apron. But it's me, I was taking it out to do the laundry. But it got torn by the door handle over there."
    e "I knew it... that's why I had no idea it was torn when I worked here."
    c "Ya can blame me for whatever happens here, it's fair game."
    e "It's fine."
    c "Ha, yer already like thousand times better than when he left the place. That lad, I treated him like my own son."
    c "You'd never imagine, he was 14 when he first worked here. No family, just him alone in the village, he lived in one of my room over there."
    "Cane points to the guest room on the second floor, it seems to be much fancier than the other room, with a shade of a sign on the door that was once mounted."
    c "He was someone like a humble, and loving person when he first worked for tavern. And I, eh. I was so relieved to have a helping hand delivering the dishes."
    c "I asked the old bull to make something that he'd like, on his birthday. Well of course, he made him a perfect-fit apron on the fly. That lad liked it."
    e "The apron, it fits me as well...?"
    c "Yeah. yeah it does. He liked the apron so much, that during those 10 years, he never spilt anything, or poked a hole in it. He was so careful and gentle with it."
    c "But over time, he got used to the scent of the tavern, the gold-hungry, self-indulgent scent. And I felt I was losing control on him."
    e "But... What made him leave the village?"
    c "That one from the town, the inspector as they'd call him, he told the lad he'd get much more attention, much more money from working in the town. He instantly loved the idea."
    c "But he didn't have the money. When he asked me for the gold to to apply for the job, I told him no. Because why would I? I wanted him to stay."
    c "He wouldn't listen, he didn't even talk to me again after that, he was just doing his job."
    c "I shouldn't care, but I did, I took away his gold, thinking he wouldn't dare to leave the tavern."
    c "...I don't know what happened. But he got the money anyway. And he just vanished, one day before the goat tribe attacked the village."
    e "...What? Are you sure...? What happened to him?"
    c "I don't know, I'd love to believe he wasn't the one helping with the raid on the goat wagon. But I don't know."
    e "Is that... why you didn't tell Rahim about all of this?"
    c "He isn't the kind of lad that'd do this. I am. Everyone knows this. I didn't want to give him a bad name when he comes back eventually."
    e "But... is he coming back?"
    c "..."
    e "Cane... Can I give you a hug at least?"
    "You reach in, embracing his whole body, he's so tall that your head can only rest on his chest, while he leans in, burying his booze-scented face on your shoulder."
    c "Good lad."
    "Slap!! You hear a huge smack on your buttock as Cane's hand finds his way to make the loudest sound possible."
    "You gasped for a moment, couldn't even comprehend what just happened. Maybe Cane just has to ruin this heartfelt moment somehow."
    c "HAAA Gotcha."
    e "Hey, Cane. I thought you were sad."
    c "Well, I'm fine now. Fine fiddity fine. Gotta get back to work like the good old bat I am."
    e "Hmm... I guess."
    e "If you need any support, I'll be here for you."
    c "Alright, finest lad, ya bet I'll come and ask ya to work for me again."
    msg "Quest Finished! You gained a level up point! Check your inventory to distribute your points!"
    $ pc.lvluppt += 1
    $ QuestFinish(quest07)
    jump main_nocturnaltrunk

label Cane_SoWrong:
    $ c = Character("Cane", color="#a1a281", who_outlines=[ (2, "#000") ])
    c "What kinda name was that? Don't make me laugh, [e]."
    c "That wolf was right about ya all along, I thought that was a joke he made. My name is Cane. Not some kinda stupid name ya pulled out of yer arse."
    e "Wait... Cane? How could I have forgotten about it..."
    c "Yea ya stupid lizard got half a brain about fucking and sucking. I reckon those goons in the shop already told you my name already. And ya still forgot it."
    c "Now, ya got the 50 gold for me?"
    if pc.gold >= 50:
        jump Cane_GotTheMoney
    else:
        jump Cane_NoMoney

label Cane_Wrong:
    $ c = Character("Cane", color="#a1a281", who_outlines=[ (2, "#000") ])
    c "Cone? Really? Ya think I've got that stupid name like that?"
    e "Wait a minute, I thought you told me your name was Cone..."
    c "What? Ya ask around other patrons, they remember my name better than ya do ya stupid lizard."
    "Cane walks around the tavern tables by tables, then he gently taps a patron's shoulder while they were talking."
    c "Aye, Mister, enjoying ya stay?"
    patron "Yeah, this beer is buzzing awesome as always!"
    c "I just wanna ask a simple question for my clueless lizard here, what's my name?"
    patron "Uhhh- Duhh. You are Cane right? How could anybody around here have not known about your name?"
    e "Wait... what?"
    c "Well apparently this lizard doesn't."
    patron "Ha... What the hell? Little lizard you gotta step up your game, and pay some respect to the tavernkeeper."
    e "I thought..."
    c "I'm sure he does now, alright mister, enjoy ya beer!"
    "Cane turns back to you with an evil smirk on his face. He seems to be oddly satisfied with you not getting his name right."
    e "Did I mix it up with other people in the village? How could that. I'm sorry... Cane."
    c "Well don't say sorry to me, say sorry to ya wallet."
    c "Speaking of which, ya got the money eh?"
    if pc.gold >= 50:
        jump Cane_GotTheMoney
    else:
        jump Cane_NoMoney

label Cane_Correct:
    $ c = Character("Cane", color="#a1a281", who_outlines=[ (2, "#000") ])
    c "Ha... damn, that's fair. It's Cane with a C."
    e "I almost mixed you up with Cone... where did that name come from?"
    c "Ya sure? I'm not Cone for the record, just letting ya know."
    e "Yeah... whatever. Glad at least I got this right."
    c "I reckon those goons at the shop had told you my name already anyway. That's a free 50 gold to you."
    e "Thanks, Cane. (You received 50 gold.) "
    $ pc.gold += 50
    c "Ha! Well then, remember to spend some on here while ya at it... We've got a number of food and drinks."
    e "I'll think about it."
    c "Alright, enjoy ya stay in the Nocturnal Trunk!"
    jump main_nocturnaltrunk2

label Cane_GotTheMoney:
    e "Yeah... I've got... let me see... [pc.gold] gold on my hand."
    c "Gimme that."
    "Cane yanks your pouch away from your palms, he swiftly pour all the coins on the counter and split them into two piles."
    $ pc.gold -= 50
    e "Hey! What are you doing!"
    c "Here's ya [pc.gold]. And the other's my 50 gold as we promised."
    "The bat gently swipe the first pile all up back into your pouch, and throws it back at you, you can barely catch it in the air."
    e "Is that all..."
    c "No... come here a second, gotta give ya something."
    "You hesitantly walk in front of the tavern owner."
    c "Closer."
    "You take another step into the side of the counter, while Cane seems to be licking his lips, waiting for you to get closer."
    "He walks closer to you, his meaty belly almost touching your own, you shudder as you see his arm reaching behind your back."
    "SMACK!"
    "Cane slapped your ass as hard as he can, you let out a loud gasp but the other patrons don't seem to notice."
    "You glance at your behind and then back to Cane. Your ass has already turned red by his forceful slap."
    c "This is an extra punishment for forgetting my name, [e]."
    e "Agh-- Do you really need to do that..."
    c "First time loser always gets a taste of my slap, mister. Yar surely welcomed when I come up with another bet."
    e "I don't know if I want to bet with you again."
    c "Well then, that concludes our lil business. Enjoy ya stay in the Nocturnal Trunk."
    "Your ass still feels sore after Cane's slap. You nudge on the cheeks as you walk around the tavern."
    jump main_nocturnaltrunk2

label Cane_NoMoney:
    e "Let me see... I've got... uhh- [pc.gold] gold..."
    c "How poor are ya lil goat. Shouldn't have bet if ya ain't got no money."
    e "I'm sorry, Cane. I thought I'd remember..."
    c "Well well well, gimme that."
    "Cane yanks your pouch away from your palms, he swiftly pour all the coins on the counter and took them away. He then hands you back the empty pouch."
    $ owed_gold = 50 - pc.gold
    $ cane_owed = True
    c "... ya still owe me [owed_gold], pal."
    $ pc.gold = 0
    e "I'll come back soon and get you the money."
    c "No I don't think so. C'mon, ya not gonna leave this place until ya paid ya debt. Look, ya be serving my patrons for a few hours and I'll consider our debt forgotten."
    e "Hey, it's just [owed_gold] gold, I'll earn this back elsewhere."
    menu:
        c "It's only a few hours, if not, ya gonna pay double the price ya owed me. Just be our server for a while, what can it hurt ya?"
        "Yes{#caneserverjob}":
            jump Cane_Serve_First
        "No{#caneserverjob}":
            jump Cane_NoMoney_No

label Cane_Outfit_02:
    $ opinions_Outfit[4] += 1
    "As you enters the tavern, you immediately draw the attention of everyone present."
    "You feel hot even though you were used to serving this crowd with the trusty apron and sometimes even less than that... Perhaps its the effect of the new outfit."
    "You quickly slinks over to the counter where Cane stands waiting. He observes you with a glint in his eyes."
    c "Ahem... Nice new outfit. I don't know where yau get the idea, but I'll have to consider paying ya extra if ya keep coming up with ideas and drawing in my customers like this."
    e "This is not my idea. Rahim made this outfit and he wanted to get your feedback on it."
    c "Rahim made this? For the tavern?"
    "You can see Cane's normal smile waver slightly."
    "You are about to explain the situation and defend Rahim when Cane continues."
    c "Eh, now that yer here. Come and let me take a look."
    c "It's not like I can chase yer sleazy little ass out."
    "You shuffles over to Cane. Cane suddenly pats your butt that is exposed through the chaps."
    "You yelp."
    c "Heh, that bull has done a good job of capturing the shape of the buns. The cutting cups and highlights everything."
    "Cane proceeds to pat down the insides of your thighs."
    c "The fabric is tough and can stand a washing. A good quality when ya work around drunk patrons."
    c "It also sticks close to yer muscles."
    "As Cane pulls his hands away, his fingers hooks the buttons that held your shorts inside the chaps togethers."
    "You feel a jolt of electricity."
    c "Maybe you should consider coming to work just in the chaps and without the shorts. I'm sure many customers will like that."
    "You blush just thinking about it. The cutouts on the chaps allow your digit to hang freely should you want to go commando."
    "Cane notices your discomfort and chuckles."
    c "The bandana is a nice touch. It'll be handy to clean up spilled drink and other... liquids."
    c "I'd say this outfit is a homerun. If ya still have any doubt, look around."
    "You did and saw the whole tavern looking at you hungrily."
    "Part of you want to hide but another part of you want to surrender to that desire."
    "You feel the front of your pants stretching. This is a problem because opening of the chaps mean that your boner can be seen clearly."
    "The shame and thrill of being discovered seem to excite you even more."
    "At that moment, you feel a pinch on your butt. The pain slightly silences the lust."
    c "Alright lad, ya better get back to the bull. Believe me, that bull has a temper and he doesn't like to wait."
    "Cane glances down at the front of your chaps."
    c "And it seems, neither do ya."
    "You quickly shuffles out of the tavern."
    "Before you exit, you believe you heard the barkeep say, Thank the bull for me."
    jump main_nocturnaltrunk

label Cane_Outfit_03:
    $ opinions_Outfit[7] += 1
    "Cane thumps his fingers on his cheek as he examines you."
    c "Can't say I'm a fan of this one."
    c "The bull's design is either hit or miss. This one is a miss."
    c "With how long the clothes is dragging, it'll keep hitting the floor."
    c "And you know how dirty our floors are."
    "Cane winks at you when he says the word dirty."
    "You think you have gathered enough feedback from Cane when you notice the barkeep staring at your crotch. You can't help but blush."
    c "No worries. This set does less for your figure than the other set."
    c "However, I am wondering. What is under all those layers?"
    "You blush even harder."
    "Cane chuckles."
    c "Alright. Maybe my impression of this set has improved slightly."
    c "Next time, consider coming without so many layers and we'll see how the patrons will react."
    c "Out you go. I have to get on with business."
    jump main_nocturnaltrunk

label Cane_Outfit_01:
    $ opinions_Outfit[1] += 1
    c "Now, ya look a bit more like a real adventurer."
    e "I am an adventurer."
    c "Never said you're not. Now you just look the part a bit more."
    e "So, you like it?"
    c "I suppose. Although I do wonder if this armor set makes you more adventurous in bed too."
    "Your cheeks color."
    c "It's not bad. But it's not for me or for this place."
    c "Those armor plates are more likely to hurt and bruise my patrons."
    e "Hmm... Alright."
    jump main_nocturnaltrunk

label Cane_Serve_Later:
    e "Ok. I'll take the job."
    c "Good, same as last time. Take yer monkey suit out and start serving."
    "You pick up the apron from the closet room again, it seems less dusty than the last time. You put on your uniform and walk out of the counter."
    call Scene_Nocturnal_Serve from _call_Scene_Nocturnal_Serve
    $ timenow.minute += 246
    scene nocturnaltrunk
    with fade
    show cane normal
    with dissolve
    if quest18.status == False and nocturnal_serve > 6 and quest07.status == True:
        jump Cane_Event_Patron_Show
    if naked_serving:
        "Cane looks back at you and grins widely."
        c "Ya liked stripping naked in front of everyone, eh?"
        e "Hey, Cane... I was just doing what your patrons asked."
        c "Ye ye. They're all perverts, didn't know yer one as well."
        e "Hmmph... I just didn't want to disappoint people, plus, you got more patrons coming to your tavern."
        c "Yer right. Ok. At least we can put the apron to rest or something now."
        c "Ya don't even need to put on anything."
        "Cane chuckles at your naked form, he is pleasantly surprised to say the least."
        "Maybe you really should think about working naked all the time..."
        c "Look, put on yer normal clothes when ya leave the tavern, eh?"
        c "Not everyone loves a slutty server in the village."
        c "...Not that I don't like yer style. I love it."
        e "Ohh... Cane."
        c "Here's yer 150 gold. I've got so much more people here now thanks to yer fat juicy ass."
        e "That was... a lot."
        $ pc.gold += 150
        c "Aye. As long as you keep working for me like this maybe yer ass will earn more."
        e "O...ok then, I'll think about it! See you Cane."
        c "Put on yer clothes first!"
    else:
        "Cane... he looks to be satisfied with your performance around the place."
        c "Good job, fine lad. Lemme see, 50 gold for you. Ye, that's it!"
        $ pc.gold += 50
        e "Thanks, Cane."
        c "The apron still looks good on ya. Come back more often and be my server for a few hours."
        e "Ok... as long as I get paid."
        c "Same as always."
        e "Great, that's a promise now. See you Cane."
        c "Ye ye."
    if sebas_location == "nocturnaltrunk" and isNight() and sebcane == 0 and sebas_affection < 13:
        $ sebcane = 1
        jump Cane_Sebas_Tavern_Night
    jump main_nocturnaltrunk2

label Cane_Serve_First:
    stop music fadeout 1.0
    e "Yeah, alright, just a few hours."
    c "Ye, ye. Ya donk, ya think I'd scam yer arse out eh?"
    e "No... Of course. So, how do I start?"
    c "Ya go over there in the closet, get ya lil monkey suit out. And then come get me some order."
    e "Hmm... what's the.. uh... suit?"
    c "Don't worry. It's not exposing ya arse or something. Just an apron and a trouser for ya."
    e "Oh... Thank god. I was worried I have to wear a literal monkey suit."
    c "Ha, yer moron! Now get yer arse over to the closet before I take away yer trouser."
    e "Ok..."
    "When you turn you back towards the closet room, Cane raised his hand and lightly slapped your butt."
    "You flinched at the bounce, you can only see Cane's creepy look in response when you look behind. You decide to ignore it and continue with your business."
    hide cane normal
    with fade
    scene black
    with dissolve
    pause 0.5
    "As you open the closet door, you found a discarded apron and trouser on the floor. The room is dusty and probably hadn't been entered for a while."
    "You pick up the uniform, and pat away the dust. You begin putting them on yourself. Surprisingly they fit like a glove in your hand, but it doesn't seem to be what Cane would wear."
    scene nocturnaltrunk
    with dissolve
    show cane normal
    with fade
    "You walk out of the closet and show Cane your new server outfit. He gesture you to turn around for him and you do so. You notice that the stitches of the clothes is exceptionally clean."
    "Moving in the outfit feels like a graceful prance, like you are meant to be inside the clothes. You see Cane chuckles for a bit, almost mesmerised, he is probably really satisfied with your look."
    c "Looking good, yer a fine lad now eh?"
    e "Your clothes, they feel really good to wear. And it fit me very well."
    c "Ye, ye. Clothes and stuff. It's been in that room for years now. So, why don't ya put yer arse to work."
    e "Alright, I'll get some order now."
    c "Wait, lemme get something done."
    "Cane walks in front of you, he raises his hand and clap for a few times, everyone in the tavern seems to go silent immediately, looking back at Cane."
    c "Gentlemen, let me introduce my new server, [e]. He will be handling your request for the next few hours."
    "You look at the tavern owner in surprise, he is speaking in a completely different accent than you are used to. You scratch your head, and wave to the patron."
    "Every one of the patron clapped probably the loudest they have ever been in their lives, some of them even chant with your name, screaming in celebration."
    "You begin to walk towards the patron who raised their hand, and take your first order. You can almost hear other patron mumbling around you, talking something about the apron."
    call Scene_Nocturnal_Serve from _call_Scene_Nocturnal_Serve_1
    $ timenow.minute += 246
    scene nocturnaltrunk
    with fade

    show cane normal
    with dissolve
    if naked_serving:
        "Cane looks back at you and grins widely."
        c "Ya liked stripping naked in front of everyone, eh?"
        e "Hey, Cane... I was just doing what your patrons asked."
        c "Ye ye. They're all perverts, didn't know yer one as well."
        e "Hmmph... I just didn't want to disappoint people, plus, you got more patrons coming to your tavern."
        c "Yer right. Ok. At least we can put the apron to rest or something now."
        c "Ya don't even need to put on anything."
        "Cane chuckles at your naked form, he is pleasantly surprised to say the least."
        "Maybe you really should think about working naked all the time..."
        c "Look, put on yer normal clothes when ya leave the tavern, eh?"
        c "Not everyone loves a slutty server in the village."
        c "...Not that I don't like yer style. I love it."
        e "Ohh... Cane."
        c "Here's yer 150 gold. I've got so much more people here now thanks to yer fat juicy ass."
        e "That was... a lot."
        $ pc.gold += 150
        c "Aye. As long as you keep working for me like this maybe yer ass will earn more."
        e "O...ok then, I'll think about it! See you Cane."
        c "Put on yer clothes first!"
        jump main_nocturnaltrunk2
    else:
        "Cane... he looks to be satisfied with your performance around the place, yet it still seems there're some sorrow on his face."
        "His furrowed brows are so obvious that something is troubling him."
        "You dare not to ask him about anything other than your job, so you apporoach Cane. You wave to him to let him know about your presence."
        if cane_owed == True:
            c "Good job, fine lad. Lemme see, [owed_gold]. Ye, that's it!"
        else:
            c "Good job, fine lad. Lemme see, 50 gold for you. Ye, that's it!"
            $ pc.gold += 50
            e "Thanks!"
        e "Hey, Cane. There seem to be some people who are really into me, like really."
        c "Hah... Don't make me laugh, not everyone is a horny bastard like you. They're just here for the apron."
        e "Hmm? Why?"
        c "Forget about it. The apron looks good on ya though."
        e "Hmm..."

    c "If ya want, come back more often and be my server for a few hours."
    e "Ok... as long as I get paid."
    c "Much more than yer actual job."
    e "Great, that's a promise now. See you Cane."
    c "Ye ye."
    jump main_nocturnaltrunk2


label Scene_Nocturnal_Serve:
    stop music fadeout 1.0
    $ nocturnal_serve += 1

    scene black
    with dissolve
    scene tenkiserve001
    "For the next couple of hours you rush among tables in the tavern, taking orders after order, holding trays after trays of beer."
    "Sometimes you might spill a few drops of beer on the ground, but the patrons are surprisingly gentle with you."
    "Almost overly gentle, even apologise when you bump into them."
    "You feel like the center of attention in the tavern, everyone is looking at you, even Cane gives you a side-eye from time to time."
    "But after the first hour you seem to get used to this feeling."
    "Yet, they're not looking at you in a normal way. Are they not?"
    "They look... almost lustful, passionate to order anything just to get you closer to them."
    "Every time you turn back at the tavern, there seem to be more customers than you checked last time."
    "Are they attracted by the news of a new server in the tavern? How are they this crazed about a worker."
    "You decided to put these unresolved thoughts to rest. Afterall, you are here to serve your patron, not to solve a mystery."
    "You focus on delivering your order in time, dashing between the counter and the tables."
    "But after a while, you'd get slapped in the ass for a few times by some random patrons."
    "You don't even know who they are, but you are sure the bounce of your own butt can be heard loud and clear around the place."
    patron "Another beer, please."
    "You turn up to the source of the voice as soon as you hear it. The patron begins gesturing you to introduce to his friend."
    e "...Hey, I'm [e], I'll be taking your order today."
    patron2 "Yeah, you can probably take my dick in your mouth, waiter."
    e "Ahem... I don't think I will..."
    patron2 "You sure you won't? I'd be sad to not get your pretty little fuzzy face to work."
    e "I've told you, no... I don't do this."
    if quest07.status == True:
        patron2 "Look... I know about the story behind you and the old man Cane, you probably like this a lot, don't you? Don't worry, we like you here."
        patron2 "We can start with something very light. How about you strip off that old apron, and shake your ass for all of us who wants to see."
        e "Uhmm..."
        "You instantly blush at his comment. Maybe he is right, you have been working here so much that the patrons begin to recognise you as their eager server."
        "Everyone at the tavern is cheering for you. Even whistling towards you. Cane is looking at you as well, cheering along with the patrons."
        "You feel like you are in the center of attention, and somehow... it feels amazing."
        menu:
            "Should you... take off your apron for the enthusiatic patrons?"
            "Take off your Apron":
                "Yes. As much as you do not wish to admit, you are still desperately trying to please the men in front of you."
                "You are not the adventurer, you are a mere server here in the tavern. And you love this."
                e "O-ok."
                "The Tavern instantly fills with roar and praise, everyone is watching you now."
                "You leave the tray on the table in fluster, and begin loosening your apron straps."
                patron "YYEAH! WOO-HOO!!!"
                patron "[e]! [e]! [e]! [e]! ..."
                "The patrons begin chanting your name as you take off the apron completely, revealing your bare chest."
                patron2 "He looks so much more delicious now."
                patron "Yes, he is. Look at his tits."
                patron2 "Ha, Keep going! Take off your trousers for us!!!"
                "You are reveling in their lustful comments, but you could never imagine that you would strip naked one day in front of dozens of customers."
                "With everyone's eyes on you, you slowly take your belt off and unbutton your trousers."
                "You lower your pants gradually, teasing the patrons with inches and inches of your skin revealed to the public."
                scene tenkiserve002 with dissolve
                "Soon, everyone can see your uncut cock, completely exposed."
                "You take the apron and trousers away to Cane, who looks surprised, but still smiles at you."
                "Some of them gasped at the sheer size of your cock, some of them cheer."
                "All of them begin chanting your name again, clapping at the sight of your member flopping around as you walk."
                "After you undressed, you can see much more people entering the tavern just to see you."
                "You are now sure that, it's not the apron they want, it's you."
                "They continues slapping you ass whenever you pass, in fact, they now slap harder because of your exposed fluffy behind."
                "The patrons pay you fat tips, which by Cane's rules the money should belong to him. But the action itself already makes you flush with euphoria."
                "People begin groping at your chest casually, whispering dirty words in your ears, while fondling your cock."
                "Some even invite you to a room upstairs, in a group."
                "But you deny politely, there's still a red line drawn, and you are not planning to cross that any time soon."
                "Taking in plates from plates. Time passes so quick that you only now realises you have already finished your job."
                "You walk to Cane, asking to complete your shift."
                $ naked_serve += 1
                $ naked_serving = True
                return
            "Continue with your work":
                e "As I said. No."

    patron2 "Ok... Ok. Calm down. It's not like it's not your sole purpose in the tavern anyway. Haha."
    "His other friends begins to laugh at his comment. You look back at the reflection in your tray, you are an adventurer, [e]."
    "Since when did it become serving stranger and letting them take advantage of you."
    "You know it is for money. But deep inside your heart, you love the spotlight they shine on you."
    "You feel this constant shower of praise and love, and this urge to take another order from all the fine gentlemen."
    "With every second passing, this feeling gets stronger that little rush of dopamine every time someone calls you a good boy."
    "Soon, your mind is clouded by thoughts of getting pampered and complimented."
    "You shake your head, these intrusive thoughts better stay as thoughts only."
    "There's no way you are going to belittle yourself like that. And so you continue with your orders."
    "Taking in plates from plates. Time passes so quick that you only now realises you have already finished your job."
    "You walk to Cane, asking to complete your shift."
    $ naked_serving = False
    return

label Cane_NoMoney_No:
    e "No... I'll pay you back later."
    c "Really? Ya don't wanna get free money here instead? Well... I guess that's ya loss."
    c "Just pay me back the amount ya owed me then, it's [owed_gold], whenever ya want."
    e "Alright... Thanks Cane."
    c "Aye, remember to call ya lizard friend to come here often."
    jump main_nocturnaltrunk2


label Lothar_First:
    hide screen menu_buttons
    if isNight():
        scene lusterfield01_night
        with fade
    else:
        scene lusterfield01
        with fade
    show lothar normal
    with dissolve
    my "You are the outsider everyone has been talking about."
    "A giant wolf comes into your view as you open the door, his crossed arm waves at you. His aggressive gaze stares into your eyes intensely, refusing to drift it anywhere else."
    e "Huh?"
    my "I saw you yesterday. The goat. Are you not a goat?"
    e "What are you talking about?"
    my "Hmmmph... something like a dragon? with furs? Don't tell me you're a bull..."
    show lothar bored
    with dissolve
    my "Whatever. Forget about it. Don't tell me."
    e "I'm a dragon..."
    my "Yes, dragon. Ole talked to me about you, those two in the shop wanted me, the hero of Lusterfield to train you. You must be something else, are you not?"
    show lothar stare
    with dissolve

    menu:
        my "So, I suppose you know who I am?"
        "Who are you?":
            jump Lothar_Who
        "Are you Rahim?":
            jump Lothar_Wrong
        "Are you Lothar?":
            jump Lothar_Correct

label Lothar_Correct:
    e "Are you... Lothar?"
    show lothar normal
    with dissolve
    "The wolf raised his brows for a bit, then you see a huge grin on his face, certainly telling you you are correct."
    l "Ha. Good, Good. I reckon your lizard friend had taught you well, really well."
    e "Uhmm... is he not like a gator..."
    l "Don't get bogged down into the details, shall we? You should be remembering my name for sure, let's move on."
    jump Lothar_Correct2

label Lothar_Correct2:
    "Lothar approaches you, he reached for your hands and arms, then turn to your face and slowly raises your chin with his claws. He nods in approval."
    l "So. I see you have a lot of potential in you, especially as a fighter."
    l "I suppose I can teach you a thing or two, probably more if you are willing to practice and learn."
    e "That's great, I'd be certainly learning from you."
    l "Good. I am the hero of Lusterfield, after all. I suppose you can learn carrying my bags, and scrubbing the floor in my house like your lizard friend does all day."
    e "What...? Lothar, you can't be serious about this..."
    l "I was joking. Your lizard friend can take a few jabs in the back."
    "The wolf is clearly chuckling at his own joke, he doesn't seem to be aware of your presence, you only stared at him, trying to calm yourself down before you punch his face."
    l "Alright, nice to meet you. [e]. I got your name from the lizard by the way. He was so adamant in making me teach you some tips and tricks."
    e "Nice to meet you, Lothar..."
    l "I'll have to prepare some equipment for you to try out for the little training we have. So, meet me here a few hours later."
    e "Ok..."
    l "Good boy."
    "You see Lothar breezes away, whistling slowly while crossing his arm. You glance at him until he walks upstairs and disappear into the room."
    $ lothar_like = 20
    jump main_lusterfield01

label Lothar_Who:
    e "Uhhhh... W-who are you?"
    l "You-???"
    show lothar angry
    with dissolve
    "The wolf is getting visably irritated, almost threatening you in some way, until he calm down after a few seconds and let out a long sigh."
    l "An arrogant settler aren't you. I'm Lothar, the protector of Lusterfield, if you forgot about it. Now, what is your name."
    e "My name is [e]. Nice to meet you Lothar. I've only arrived here yesterday, I'm so sorry that I didn't know about you."
    menu:
        l "Yes, the lizard talked to me about your name. He talked to you about me as well, didn't he. But I forgive you, [e]."
        "Thank you...?":
            jump Lothar_Who_Smile
        "Ok.":
            jump Lothar_Who_Angry

label Lothar_Aphrodisiac_Quest:
    l "Disciple, I have an adventure planned for you to see a real hero in action."
    e "That sounds good... but didn't I already see you with the golems?"
    $ QuestBegin(quest25)
    $ quest28.qProgress(__("Go Defeat the Flower with Lothar"))
    menu:
        l "It was not sufficiently heroic. Today we will be wiping out a monster the villagers have been complaining about."
        "I'm ready":
            "This is a statement, It seems you have no choice in this matter."
            e "Okay. Can you give me a moment to get ready?"
            l "A hero should always be ready, disciple."
            l "To learn that, you must be caught unawares. You are coming with me."
            "You groan. You really did not expect to get ferried off like this out of nowhere."
            "Lothar looks at you with that ever-present arrogant face of his."
            l "And a hero never complains. Get off your ass and come with me."
            "Lothar begins walking off. You hurry after him."
            "Probably a good thing he didn't give you time to talk, honestly, considering you were going to point out how often he complains."
            jump Lothar_Aphrodisiac_Adventure
        "I need to prepare":

            e "I have courier work to attend to today, sorry... but can we do it some other day?"
            "Lothar narrows his eyes."
            "It wasn't a lie... you're just stretching the truth is all."
            l "Well, it cannot be helped if you are busy."
            l "You will need to report back to me soon, however. A hero never shirks responsibility."
            jump Lothar_Normal_Talk

label Lothar_Aphrodisiac_Quest_Ready:
    e "Lothar, didn't you mention the monster the Lusterfolks have been complaining about?"
    menu:
        l "Yes, now... you ready?"
        "Yes{#lotharaphrodisiac}":
            e "Okay. Can you give me a moment to get ready?"
            l "A hero should always be ready, disciple."
            l "To learn that, you must be caught unawares. You are coming with me."
            "You groan. You really did not expect to get ferried off like this out of nowhere."
            "Lothar looks at you with that ever-present arrogant face of his."
            l "And a hero never complains. Get off your ass and come with me."
            "Lothar begins walking off. You hurry after him."
            "Probably a good thing he didn't give you time to talk, honestly, considering you were going to point out how often he complains."
            jump Lothar_Aphrodisiac_Adventure
        "No{#lotharaphrodisiac}":
            e "I have courier work to attend to today, sorry... but can we do it some other day?"
            "Lothar narrows his eyes."
            "It wasn't a lie... you're just stretching the truth is all."
            l "Well, it cannot be helped if you are busy."
            l "You will need to report back to me soon, however. A hero never shirks responsibility."
            jump Lothar_Normal_Talk

label Lothar_Aphrodisiac_Adventure:
    stop music fadeout 1.0
    scene black with dissolve
    "You and Lothar have been walking through the forest for a while now, Lothar following some unknown set of directions, and you following him."
    pause 2
    scene ancienttree with dissolve
    show lothar normal with dissolve
    "..."
    e "So... Lothar."
    "Lothar grunts in acknowledgement, but keeps walking."
    e "What kind of monster are we hunting exactly?"
    l "A hero should be prepared for any kind of enemy!"
    e "...Please? Can I know?"
    "Lothar sighs and shakes his head."
    l "Fine, but you are lucky to have such a generous mentor."
    l "We are hunting a plant monster that has been reported to be bothering the locals."
    "He continues marching, as if that short note explained everything."
    e "How is it bothering them? Is it hurting them or something?"
    "Lothar does not turn around, but you can feel his grin even without seeing it."
    l "What, are you afraid of getting hurt, disciple? I thought I trained you better than that."
    e "No, I just want to understand what's been happening to the townspeople."
    "Lothar dips his head in acknowledgement as he walks."
    l "Fair enough. It is good for a hero to be concerned about his people."
    l "It has been attacking villagers, but not lethally."
    l "Most of the townspeople came back with rumpled clothes, and maybe a couple bruises."
    e "Then why is it so important to take down?"
    l "Well, a hero should never back down from a fight, mainly."
    l "But it also seems to mess with their minds a bit. They report feeling a bit woozy and euphoric after meeting it."
    "That's... odd."
    e "Do they behave any differently in that situation?"
    l "I asked, and..."
    "Lothar pauses his speech for the first time so far."
    l "They were all very dodgy about it. I assumed they were just in awe of being in front of the Hero of Lusterfield."
    "..."
    "You have a feeling that is not why they wouldn't answer. Despite that, you can't figure out why they actually would."
    l "That's enough questioning, however. You must pay attention to how I move, so you can imitate it and become a fraction of the hero I am."
    scene black with dissolve
    "After a long while of walking, and going past various different landmarks like the tree, Lothar puts his arm out in front of you."
    pause 2
    scene sparklinglagoon with dissolve
    show lothar normal with dissolve
    l "We are approaching the monster."
    "Lothar removes his sword from its sheath."
    "..."
    "He turns to look at you."
    l "Why aren't you taking out your sword."
    e "I didn't know I was supposed to yet?"
    "Lothar takes one hand off of his sword and slaps it to his face."
    l "Do as your mentor says and does, disciple. This is beginner stuff, it reflects badly on me for you to mess up like this."
    e "I-"
    "You decide against saying anything, and instead unsheathe your blade."
    "Lothar sees this as enough, and turns to begin moving forward once more."
    "Almost as if it were waiting for the perfect moment where both of your guards were down, you see a massive root lunge out of the earth at you."
    "Right as it is about to land its blow, Lothar leaps forwards, blocking the strike with his sword."
    show lothar at l1 with move
    l "Sneak attacks are useless against a hero!"
    "As he says this, a second root erupts from the earth behind him, moving to slam into Lothar's skull."
    show lothar with vpunch
    "Your body moves before your mind does, lunging forward and blocking it with your weapon."
    l "Well done disciple! Maybe not all hope is lost for you after all."
    "Standing back to back with Lothar now, the plant releases all pretenses of stealth."
    "Dozens of roots burst out of the ground."
    "You and Lothar are a blur, blocking and nudging, redirecting the roots to anywhere but your bodies."
    "You are making no progress however."
    with vpunch
    l "Let's see how long you can keep this up for!"
    "You have no idea if he's talking to you or the plant, but Lothar is clearly having the time of his life."
    show lothar with vpunch
    "Every muscle, joint, and tendon of his body is ready - waiting for the next blow to come."
    l "This is how a hero fights, disciple!"
    "He seems to have forgotten that you are doing only slightly less than half of the work here."
    "You have no idea how long this continues for, your every thought dominated by the plant and Lothar."
    "Eventually however, there is movement in the canopy above you."
    "A bright orange pod emerges from above you and Lothar."
    "Extending from its sides are thousands of tendrils, all of which snake down into the ground to become roots."
    l "There you are, you bastard!"
    show lothar with vpunch
    "Despite the colorful language, Lothar is the happiest you've ever heard him, his voice an overjoyed roar."
    "Lothar turns to look at you, somehow still managing to block all of the roots coming his way."
    menu:
        l "Go get it disciple! I can handle all of the roots down here on my own!"
        "Get the monster":

            $ lothar_flower_save = False
            $ quest23.qComp(_("Talk to Lothar after... the incident"))
            $ quest25.status = 3
            e "Okay! I will do my best!"
            "With that, you slide under the attacking roots, kicking off the ground when your momentum begins to lag."
            "A couple roots attempt to follow you, but Lothar blurs forwards to block them off."
            "You reach one of the trees underneath the pod, and begin to climb."
            "On your way up, you look down at Lothar."
            "He is a whirlwind of silver. If you don't look closely, it looks like there are 4 of him at every moment, each one blocking and shoving one of dozens of roots."
            "As you continue your climb, you get a better look at the pod above you."
            "Bright orange, the pod has a spherical shape. The light it emits renders it transparent."
            "Inside, it is pulsing with millions of tiny dots, each one floating around like dandelion seeds in a hurricane."
            "This is clearly vital to the plant. You are certain that attacking the pod will kill it."
            "Removing one arm from the trunk of the tree, you once more grab your sword."
            "The pod is within reach."
            "You plunge your blade into the center of the pod."
            $ pc.cor -= 3
            if pc.cor < 0:
                $ pc.cor = 0
            call Scene_Lothar_Aphrodisiac_Quest from _call_Scene_Lothar_Aphrodisiac_Quest
            $ pc.lust = 0
            $ timenow.hour += 4
            $ timenow.passTime()
            $ pc.add_active_status(stuffed)
            jump main_sparkling_lagoon
        "Help Lothar":
            $ lothar_flower_save = True

            e "No! You can't do this on your own!"
            e "Please let me stay and help."
            $ QuestFinish(quest25)
            show lothar stare with dissolve
            "Lothar growls in displeasure."
            l "You think I can't handle this?!"
            l "I've been holding back so that you can get experience too, disciple."
            "Lothar's body language shifts radically, from one reveling in violence, to one poised to kill."
            "Abandoning all pretense of staying on the defensive, he shifts his blade such that the fuller is no longer at front - instead, the sharp edge is poised to cut and shear."
            "As you continue to block roots, Lothar's body accelerates to the point where it is difficult to track with your eyes."
            "Silver flashes through roots, cutting through rough wood as if it were paper."
            "More and more roots fall lifeless to the ground, until a small wall of roots lay in front of Lothar."
            "After he is satisfied that no more roots can attack from that side, he grabs you by the shoulder, and shoves you behind him."
            show lothar angry with dissolve
            l "If you aren't going to help or learn, you might as well stay where you won't be in the way."
            "Once more exploding into motion, Lothar begins to exterminate the roots on your side of the field."
            "After only a few brief minutes, no more roots are left to attack you or Lothar."
            "Above you, the pod is trembling. It cannot move anymore, its body connected to the ground and trees through vines that now chain it to its grave."
            l "I've had enough of you. The sooner you die, the sooner I can go back to town and drink."
            "As he says this, Lothar jumps for one of the nearby trees."
            "His feet land on the trunk - his knees tense, his legs rippling with muscle underneath his grey fur."
            "With an incredible leap, Lothar reaches the plant, cutting an enormous swath of vines from it, before landing on another tree, and repeating the action."
            "With each jump, The pod sags lower and lower, until eventually, it rests against the earth, robbed of all connections."
            l "We're done here."
            "He marches off without another word."
            e "What about the plant? Are you not going to kill it?"
            "Lothar turns on you."
            l "What right do you have to ask that, when you refused to do so earlier?"
            l "You are my disciple, you are supposed to follow my directions and learn from me."
            l "I will continue to teach you, but what kind of fool doesn't listen to their mentor."
            "Lothar shakes his head, spitting on the floor."
            l "If you paid attention, you would realize that plants survive based on their connections to the environment around them."
            l "Without roots or vines, the monster will die of starvation. That is one of the most efficient ways to kill a plant monster."
            show lothar bored with dissolve
            "Lothar once more turns away, and stalks off towards town."
            scene black with dissolve
            pause 2
            "Before long, you arrive at Lusterfield."
            scene lusterfield02 with dissolve
            show lothar stare with dissolve
            l "I am disappointed in how you did today, disciple."
            "..."
            "Okay, enough is enough."
            e "What am I supposed to do, listen to you blindly if you tell me to do anything?"
            e "If you're holding back to let me do things, maybe TELL me that, so that I can actually have a good understanding of the battle."
            e "Rather than just being led along."
            "Lothar looks furious."
            l "Maybe I wouldn't have to coddle you like that if you were as strong as me."
            l "But you aren't."
            l "So maybe, instead of talking back to a hero, you should listen to him."
            e "You say that like the spar wasn't closer than you'd like to admit."
            l "I was going easy on you back then too."
            e "I don't believe that for a second."
            l "You want to go again right now?!"
            e "You know what, maybe I do!"
            "Right as you both begin to reach for your swords, Rahim steps out of his shop, bellowing at the top of his lungs.."
            show rahim normal at l2
            show rahim normal:
                linear 1 xalign -0.25
            r "I swear to god, if you two don't shut up and let me work in peace, I'm going to go over there and beat both of you."
            "..."
            "You and Lothar are frozen by this sudden display of anger from Rahim."
            show rahim normal:
                linear 1 xalign -1.25
            "After a while of staring at both of you, Rahim goes back inside, slamming the door behind him."
            show lothar bored with dissolve
            "You and Lothar turn to face each other once more."
            l "...fine."
            l "Make sure you get strong enough to actually make your own decisions like that in the future."
            "...This argument isn't going to end if you don't let it."
            e "...okay."
            "With that, Lothar leaves you alone, returning to his usual spot, a dark look creasing his features."
            $ timenow.hour += 3
            $ timenow.passTime()
            jump main_lusterfield02

label Lothar_Who_Smile:
    e "Thank... you? Lothar..."
    l "Yes, you are correct, for the first time. Anyways, I should introduce myself, if you have forgotten."
    l "I am Lothar, the hero of Lusterfield."
    e "I thought you told me about it already? The whole hero thing."
    l "What? I was being genuinely considerate about your memory, I saw it on the courier news that brain worms can eat your memory away."
    e "I'm not sure that is a real-"
    "Lothar cut you off before you can finish your sentence, he is visibly irritated, refusing to elaborate further."
    show lothar stare
    with dissolve
    l "You want your training or not."
    e "Yes..."
    jump Lothar_Correct2

label Lothar_Who_Angry:
    l "Ok?"
    show lothar angry
    with dissolve
    l "Did your elder teach you manners, especially talking to a hero in front of you?"
    e "I didn't know who you are, I'm sorry."
    l "You little piece of shit. I know Ole talked to you about me. I made sure he does every time."
    "The wolf apparently was not pleased with your demeanor. He advances towards you, making you pace backward, almost to the point of hitting the door behind you."
    l "You know what? If it isn't for that green lizard I would never even approach you in first place."
    "You can smell the wolf's bitter scent from such a close distance, it doesn't smell like he had bathed for a while. His bulging chests are almost touching you."
    l "And now you are treating me with such inappropriate manners? And you don't feel ashamed of yourself? Are you really sure?"
    "Lothar is adamant in his way of teaching you manners, he growls forcefully at you, while you flinches, trying to turn your face away. You can feel his barking rattling the doors."
    e "Look... I'm sorry."
    l "Are you?"
    e "Yes."
    l "..."
    l "Hmmmph."
    jump Lothar_First_End

label Lothar_Wrong:
    e "Uhhhh... Are you Rahim?"
    show lothar angry
    with dissolve
    my "You-???"
    "The wolf is getting visably irritated, almost threatening you in some way, until he calm down after a few seconds and let out a long sigh."
    my "How the hell could you have mixed up with me and that Old Bull, Does he even look like a hero of Lusterfield?"
    my "Alright then, now tell me, what's your name."
    e "My name is [e]."
    my "Good. Good. The lizard told me about you. I'll just call you the goat now. Considering that you don't even know what a hero looks like."
    "The wolf apparently was not pleased with your demeanor. He advances towards you, making you pace backward, almost to the point of hitting the door behind you."
    "You can smell the wolf's bitter scent from such a close distance, it doesn't even smell like he had bathed for a while. His bulging chests are almost touching yours."
    my "You know me now?"
    e "What's your name?"
    l "Lothar. It's Lothar. Put my name into your horny brain, now. Don't you ever forget about it."
    e "Y-yes... nice to meet you. Lothar..."
    l "Tell me again. What's my name?"
    e "l-lothar."
    l "Good, good. I'm the hero of the village. Don't you ever, ever try to play me like that, you understand?"
    e "Ok?"
    jump Lothar_First_End

label Lothar_First_End:
    show lothar normal
    with dissolve
    "Lothar now satisfied with your performance, backs off slowly and gives you room to breath properly. He crosses his arms more tightly now, almost squishing his chest further."
    l "Alright. You've learnt your lesson. I've shown you."
    l "Did the lizard mentioned the word \"training\" to you by any chance, [e]?"
    e "I think so. He told me to get the training from you before I go out for an adventure."
    l "A new adventurer I see. Maybe sometimes I can get you to carry the bags for me outside. Maybe even wash my back on the river down there."
    e "What? N-no... I can't-"
    l "Ha. You little thing. You think I'll let you touch me even slightly? Don't be so silly."
    l "Now. I haven't prepared my weapons for you to try out yet. So, come find me later. I'll meet you here when I'm ready. You understand?"
    e "Yes... Lothar."
    l "Where are you meeting me?"
    e "H-here?"
    l "You're goddamn right. Ok. Good. Now that lizard owes me a huge favour to take care of his little outsider friend."
    jump Lothar_First_Ending

label Lothar_First_Ending:
    e "His name is Ole..."
    show lothar angry
    with dissolve
    l "What did you say? You think I don't know his name? You've met him only just yesterday, and I've been with him before he's even born-"
    "The door behind you moves, Lothar still angrily staring at you when you see Ole comes out of the store in the corner of your vision. He gave Lothar a side eye before walking towards you."
    show lothar bored:
        xalign 0.1
        yalign 1.0
    with move
    pause 0.5
    show ole understand:
        xalign 0.9
        yalign 1.0
    with dissolve

    o "What's going on, [e]?"
    l "Nothing, I was talking to him about the training I promised you."
    show ole bored
    with dissolve
    o "Doesn't sound like talking."
    l "Alright then, I'll tone down my voices for the newcomer. I'm just trying to teach him something important."
    o "Then teach silently."
    l "..."
    l "Ok."
    show lothar stare
    with dissolve
    "Ole stares at Lothar for a few seconds while the wolf tries to avoid his gaze, looking away like a defeated puppy. The lizard then turns to you calmly."
    show ole normal
    with dissolve
    o "[e], you alright? If he ever harasses you again, I'll teach him a lesson myself."
    "With that, the lizard walks back towards the door and closes it, you could see Sebas peeking out from the door in a glimpse of a second."
    hide ole
    with dissolve
    show lothar stare:
        xalign 0.5
        yalign 1.0
    with move
    l "Ahem..."
    "The wolf clears his throat, obviously bothered by the presence of Ole. He unnaturally places his arms apart, scratching his head for a few times before stretching."
    l "So, See you then... [e]."
    e "See you Lothar."
    "Lothar frowns upon you as he walks away towards the stairs on the other side of the road. You sigh heavily, finally getting out of the sticky situation."
    $ lothar_like = 10
    jump main_lusterfield01



label Lothar_Dialogue:
    hide screen menu_buttons
    call Lusterfolk_Affection from _call_Lusterfolk_Affection_2
    if isNight():
        scene nocturnaltrunk_night
        show lothar normal blush
        with dissolve
    else:
        scene lusterfield01

        show lothar normal
        with dissolve
    if lothar_night > 1 and not isNight() and quest05.status == False:
        if timenow.day > 6:
            l "Hey! Are you trying to hide from me, disciple?"
            e "N-no! I was looking for you."
            l "{b}Meet, me, in, the, tavern, at, night.{/b} And don't tell me you don't drink. I don't care."
            e "Uh, alright."
            jump Lothar_Normal_Talk
        elif timenow.day > 3:
            l "Hey, I see you here, disciple."
            e "Uh... Lothar?"
            l "Meet me in the tavern at night if you want to learn from the best."
            l "Don't you make me wait further."
            jump Lothar_Normal_Talk
    if quest25.status == 3:
        e "Heyyyy, Lothar."
        "You can't help but look down, twiddling your fingers as you think about how to talk to Lothar after what happened."
        l "Hello, disciple."
        l "I look forward to carrying on like normal."
        $ QuestFinish(quest25)
        menu:
            "But-...":
                e "But-..."
                l "Nothing happened, and we will not talk about it."
                e "Okay."
                "Lothar sighs, looking to the side and blushing slightly."
                l "You did a good job in the fight."
            "Okay":
                e "O-okay..."
                l "Thank you, disciple."
                "Lothar is smiling at you. It seems that despite... what has happened between you, he still likes you quite a bit."
                l "Now, get back to training. You've been making good progress, but you're not a hero yet!"

    if not isNight() and quest06.status == True and quest05.status == True and opinions_GoatTribe[0] == 1 and opinions_GoatTribe[1] == 1 and opinions_GoatTribe[2] == 1 and opinions_GoatTribe[3] == 1 and opinions_GoatTribe[4] == 1 and timenow.day > quest05.completed_date + 1 and quest10.status == False:
        jump Lothar_Invasion_Quest
    if not isNight() and timenow.day > quest10.completed_date + 1 and quest10.status == True and quest12.status == False:
        jump Lothar_Battle_Training
    if lothar_night == 1 and isNight():
        $ lothar_night += 1
        jump Lothar_Night_Greet
    if isNight() and sebas_location == "nocturnaltrunk":
        if ole_location != "nocturnaltrunk":
            l "Greetings, disciple."
            e "Hello, Lothar."
            e "How're you doing, Lothar?"
            l "Bad. Especially when I see the lion here."
            e "Oh..."
            jump Lothar_Normal_Talk
        else:
            l "Greetings, disciple."
            e "Hello, Lothar."
            e "How're you doing, Lothar?"
            l "Have you seen the lizard here before, I think he's spying on me."
            e "Oh..."
            jump Lothar_Normal_Talk
    if naked_serve >= 1 and isNight() and renpy.random.random() > 0.5:
        l "Hey, [e]. I heard you're serving people naked. When are you serving me this way?"
        e "Uhhhmmm? Lothar?"
        l "You know, being a hero is really tiring, I might need a personal server."
        e "O-oh, If you would like?"
        l "Yeah, no. I'm not one of those horny patrons Cane serves in his tavern."
    elif renpy.random.random() < 0.3 and quest01.status == True:
        l "You know what I did today, disciple? I killed 10 slimes, in a day. Protecting Lusterfield from the dangerous slime threats."
        e "Uh, that's... very impressive."
        l "What are you trying to say? I bet you can't even beat a dummy."
        e "I did! I beat it the first days we met."
    elif renpy.random.random() < 0.2 and quest25.status == True:
        if not lothar_flower_save:
            l "Don't talk about what happened with the flower."
            e "I- Lot, do you want to talk about it?"
            l "NO! Stop asking me about the flowers. You're making me uncomfortable."
            e "O-ok."
        else:
            l "I feel like Lusterfolks respected me now more than when I killed that goat."
            e "Well, maybe because you were actually saving them from that flower?"
            l "What do you mean, everyone knows I am the saving grace of Lusterfield because I killed him, not some random flowers."
            l "Speaking of, I still remember what you did there."
            e "Uh, I just wanted to save you there, but alright."
    elif renpy.random.random() < 0.1 and quest13.status:
        l "I actually saved Amble and Jog, long ago from the bandits."
        e "Hello Lothar, what are you talking about?"
        l "I feel I have to make them remember that once in a while, else they forget."
    elif renpy.random.random() < 0.2 and quest20.status:
        l "Anything new with the werewolves in the dark forest?"
        e "Uh, actually, aren't you a wolf, Lothar?"
        l "I'm not a werewolf, that's a whole different species. They are vicious and hunts anyone they see like cavemen."
        e "Well, technically, you're correct. I think the-"
        l "Still, werewolf or not, they're mere smokescreens. All teeth, not brain."
        l "The only thing I care is the goats, get it, disciple? One day we'll unveil the evil plans those goats are brewing up."
        l "That's what heroes do."
    elif renpy.random.random() > 0.5 and pc.armor["Clothes"] == None and pc.armor["Pants"] == None:
        l "Hmmph, [e]. Why are you naked..."
        e "Sorry, Lothar."
        l "Whatever."
    elif isNight():
        l "A-ahhhh, [e]. Rarely do I see you in the tavern."
        e "Hello... Lothar?"
    else:
        if lothar_like < 15:
            l "Greetings. [e]."
            e "Hello Lothar."
        else:
            l "Hello, my disciple."
            e "Hello Lothar."
    jump Lothar_Normal_Talk


label Lothar_Normal_Talk:
    menu:
        l "What brings you to the hero today?"
        "Ask about Pirkka's Prose" if quest35.status == 3:
            jump Lothar_Prose_Ask
        "Learn his opinion on the vote" if quest37.status == 2 and quest37.start_date + rahim_vote_duration - 1 >= timenow.day:
            jump Lothar_Voting_Opinion
        "Ask about the Gnolls" if LookForItem("Ruttish Flute", inventory):
            jump Lothar_Ask_About_Gnolls
        "Report about your fight with dummy" if quest12.status == 2 and not isNight() and dummy.win > dummylvl2:
            stop music fadeout 1.0
            jump Lothar_Report_Dummy
        "Spar with Lothar" if quest12.status == 3 and not isNight():
            stop music fadeout 1.0
            jump Lothar_Sparring
        "Deliver the goods" if is_recipient("Lothar"):
            $ recipient_name = "Lothar"
            call Courier_Delivery_Dialogues from _call_Courier_Delivery_Dialogues_1
        "Pick up the delivery" if is_client("Lothar"):
            $ client_name = "Lothar"
            call Courier_Pickup_Dialogues from _call_Courier_Pickup_Dialogues_1
        "Ask about the sparring bet" if quest12.status > 3 and not isNight():
            jump Lothar_After_Sparring
        "Ask about the monster nearby" if quest25.status == False and quest37.status != True and quest11.status == True and not isNight() and timenow.day >= 30:
            jump Lothar_Aphrodisiac_Quest
        "Go to hunt the monster nearby" if quest25.status == 2:
            jump Lothar_Aphrodisiac_Quest_Ready
        "Ask about the stone from the caravan" if quest20.status == False and quest13.status == True and not isNight():
            jump Lothar_Caravan_Stone
        "Ask about his opinion on the vote" if quest37.status == True and timenow.day < quest37.completed_date + 14:
            jump Lothar_Voting_Result
        "Ask about Amble and Jog" if timenow.day > 12 and quest11.status == True and timenow.day > quest11.completed_date + 1 and quest13.status == False:
            jump Lothar_Ask_Amble_Jog
        "Ask about your outfit" if pc.armor["Clothes"] != None and pc.armor["Pants"] != None and quest09.status != False and quest09.status != True:
            if pc.armor["Clothes"].img == "Adventurer Armor" and pc.armor["Pants"].img == "Adventurer Leggings":
                jump Lothar_Outfit_01
            elif pc.armor["Clothes"].img == "Tavern Cloth" and pc.armor["Pants"].img == "Tavern Chaps":
                jump Lothar_Outfit_02
            elif pc.armor["Clothes"].img == "Flowy Robe" and pc.armor["Pants"].img == "Flowy Wrap":
                jump Lothar_Outfit_03
            else:
                "As you are about to ask, you realise you are not putting on the right clothes to judge..."
                jump Lothar_Normal_Talk
        "Report for Amble and Jog's Training" if quest13.status == 5:
            jump Lothar_Report_Amble_Jog
        "Ask about Postal Training" if quest01.status == 2 and quest04.status == False and not isNight():
            jump Lothar_Postal_Training
        "Finishing Postal Training" if quest04.status == 2 and not isNight():
            jump Lothar_Postal_Finish
        "Ask about his Loot" if lothar_night > 1 and not isNight() and quest05.status == False:
            jump Lothar_Mossy_Artifact
        "Ask about his opinion on the Goat Tribe" if quest06.status == True  and quest06.completed_date + 1 < timenow.day and opinions_GoatTribe[3] == 0:
            jump Lothar_Ask_Goat_Tribe
        "Report about the visit to Goat Tribe" if quest10.status == 4:
            jump Lothar_Report_Goat
        "Ask Lothar about Trainings from Ole" if quest17.status == 3:
            jump Lothar_Ask_Ole_Training
        "About sneaking into the Goat Tribe" if quest10.status == 2 or quest10.status == 20:
            jump Lothar_Ask_Invasion
        "Ask about the trip to the river" if quest05.status == True and quest05.completed_date + 10 > timenow.day:
            jump Lothar_After_River_Trip
        "Ask about Lusterfield{#LotharAAL}" if quest06.status != True:
            jump Lothar_Ask_Lusterfield
        "Ask about him being a hero":
            jump Lothar_Ask_Hero
        "How are you doing?":
            jump Lothar_Ask_Himself
        "That's all for now":
            jump Lothar_Dialogue_End
    jump Lothar_Normal_Talk

label Lothar_Caravan_Stone:
    e "Hey, Lothar, what's wrong with the... stone. again?"
    l "Disciple, remember the wagon attack info you've gotten with Jog?"
    e "Yea."
    l "I went back to the site around the tree to do some digging."
    "Lothar takes out the stone to show you."
    show magical stoneBig with dissolve
    e "What is it?"
    l "Hard to say. But based on this hero's experience, it is imbued with magic."
    e "Magic?"
    l "Yes. And the only magic user around here is that deer."
    "Lothar bristles with anger."
    l "I'll tell you, they set this all up just for an excuse to attack us."
    "There is a rage in his eyes that you have not seen before."
    "You can finally understand why he's the Hero of Lusterfield. Lothar can be quite frightening."
    e "Lothar, what are you going to do?"
    "You are worried about Lothar's condition. He has a tendency to do rash things."
    l "This is a sign of their guilt. I'm going to kill them all!"
    e "Maybe we should look at this closer."
    menu:
        l "What's there to look? The evidence is clear as day."
        "Look at the colour":
            $ lothar_angry += 3
            e "Lothar, do you think the stone... has a different colour?"
            l "W-what."
            e "Colour. I think it's different than the hue the goat tribe usually have."
            l "N-no... even if the colour is d-different..."
            l "I-I..."
            l "Maybe you're right. But these fuckers can use magic, what else can they not do?"
            l "I'm not convinced, disciple."
        "Look at the roughness":
            $ lothar_angry += 2
            e "Lothar, look at the roughness of the stone. Does that feel like a stone from the goats?"
            l "Yes, Disciple what's your point."
            e "I-I mean... it's smoother?"
            l "They have all kinds of stones, and how can't these fuckers polish one?"
            e "Uhm..."
            l "Disciple, if you want to help, then stop trying to convince me."
        "Look at the wetness":
            $ lothar_angry += 1
            e "Lothar, look at the wetness of the stone, does that feel like a stone that the goats would make?"
            l "Yes."
            e "W-what? No?"
            l "Disciple, their whole tribe is powered by a waterfall with magic."
            e "Uhm..."
            l "Do you even know what you're talking about..."
    hide magical stoneBig with dissolve
    l "I'm going to get an explanation, and kill their leader!"
    menu:
        e "Stop! I know..."
        "Think about the golem":
            e "The golem, right? Their golems went rogue."
            l "I know, and we killed one of them, so?"
            if guardian_alive:
                $ lothar_angry += 5
                e "I saved the other one. With a stone just like this!"
                l "W-wait. What?"
                e "Yes... It's from the cave."
                l "When? What happened?"
                e "I saved Furkan from the cave when someone hit him from behind."
                e "And they stole... the basin."
                l "Why didn't you tell me, disciple."
                e "Look, the point is, that stone belongs to something in the cave."
                e "And it's not used to kill anyone."
                l "Are you... sure?"
                e "Yes."
                l "I'm rather disappointed you didn't tell me about this earlier, disciple."
                l "But I'll trust you, for now."
            else:
                $ lothar_angry += 1
                e "So... Uh... the golem..."
                l "The golem has nothing to do with their caravan attack, disciple."
                l "It's that fucking deer that's using the magic."
        "Think about the Goat Victims":
            $ lothar_angry += 3
            e "Those goats who died in the caravan. Do you really think they'll do something like this?"
            l "What else can't they do?"
            e "Their leader, Tevfik, loved their people so much that they attack on Lusterfield after the caravan incident."
            e "You really think they did that on themselves?"
            l "I-... I don't know? Why else would their stone be there."
            e "Maybe it's from the carriage?"
            l "No, they cleaned it up very quick. It couldn't have been from the attacked caravan."
            l "I found this one hidden under the tree stump. Something must've stopped it..."
            e "Well maybe there's other magic user than the general?"
            l "...Fine, you win this one. But I'll still go there an you can't stop me."
        "Think about the tree":
            $ lothar_angry += 2
            e "The tree, the ancient tree, why else would they need magical stone?"
            l "W-what do you mean."
            e "The ancient tree has all the magical reserve they need, why would they want another magic source?"
            l "It's still pretty far away from the tree."
            e "My thing is, they could just do it when the caravan arrived to the tree."
            l "No? I mean you're right. But why not anywhere with the stone they have."
            e "I-I... because that's the most convenient way...?"
            l "No, that doesn't sound very right..."
    l "I'll kill their guards first if they dare to block me."
    e "Uhmm...."
    menu:
        e "I know, I know!"
        "Analyse Lothar's emotion":
            e "Look, Lothar. I know what you're going through."
            l "What I am going through?"
            e "I know that you're still grieving and in a lot of pain sinc-"
            l "What are you talking about, disciple."
            l "I'm angry because I'm only finding this out now!"
            l "I'm angry that they're getting away with this for so long."
            l "These pieces of trash living up on the mountain looking down upon us."
            e "W-what?"
            l "You think this is one thing? That goat leader? I'm fucking glad I get to kill him."
            e "Maybe you're jealo-"
            l "I'm not. I'm the hero, and I do what a hero would do."
        "Tell Lothar to think rationally":
            $ lothar_angry += 4
            e "Think, Lothar. Look at all the evidence that proved otherwise."
            l "W-what do you mean."
            e "Take a deep breath, Lothar."
            l "I... I'm starting to hate how you're talking to me this way, disciple."
            e "I-... just breath."
            l "I'm breathing all the time."
            e "Then stop shaking and think about the reasons. Maybe you're blinded by emotions."
            l "I'm not."
            e "There's a lot more groups other than the goats and Lusterfield."
            l "Y-you mean the other tribes?"
            e "Maybe, but much more."
            l "...Maybe."
        "Give Lothar a beer to drink" if LookForItem("Beer", inventory) or LookForItem("Ale", inventory):
            $ lothar_angry += 3
            e "Look, Lothar. You need a beer."
            l "I-I... I can't drink a beer, I'm going to kill them."
            e "But... you need a beer first, here."
            l "..."
        "Ask for a small Talk with Lothar":
            $ lothar_angry += 2
            e "Well, what a sunny day it is today..."
            l "Disciple, stop."
            e "We could have gone for a walk, just you and me."
            l "We could but there's something much more important."
            e "I've defeated a mimic before, have you seen a monster that mimics a chest?"
            l "..."
            e "And Seb seems like he wanted his nuts kicked, don't you want to take a revenge?"
            l "Mhmm..."
    $ QuestBegin(quest20)
    $ quest20.qProgress(__("Visit the Goat Tribe"))
    if lothar_angry < 5:
        l "It doesn't seem you're that convincing, disciple."
        l "I'm going there myself, and don't try to stop me."
        $ lothar_along = False
        "Lothar rushes away and you already lose sight of him when you realise..."
        "You feel like you should go to the goat tribe to check on Lothar..."
        jump main_lusterfield01
    elif lothar_angry < 8:
        l "I've thought about your argument, but... I trust my intuition."
        l "And I can just get all I need before I finish them."
        l "I'm going there myself, and don't try to stop me."
        $ lothar_along = False
        "Lothar rushes away and you already lose sight of him when you realise..."
        "You feel like you should go to the goat tribe to check on Lothar..."
        jump main_lusterfield01
    else:
        l "I've thought about it..."
        l "I don't need a beer, or a small talk."
        l "But I need an explanation at least, as a hero."
        e "So... can I go with you?"
        l "Fine. You can come, maybe you can get them to start talking."
        $ lothar_along = True
        jump Lothar_Along_Goat_Tribe

label Lothar_Along_Goat_Tribe:
    scene kechioeren with dissolve
    "As you and Lothar approach the goat tribe, you can feel your companion becoming a lot more tense."
    show lothar bored with dissolve
    "Lothar's hand reaches towards his sword."
    e "Lothar, we're not here to kill anyone. We should talk before we resort to violence."
    l "Why shouldn't we, Disciple? They've killed so many of us. Plus, the stone is proof that they're in on this."
    e "Again, that's not yet verified."
    l "This Hero will not be seen groveling or begging any goats. I'll kill before that happens."
    e "We're not going to do that either."
    l "Disciple, for all we know, we might be walking into a trap."
    e "Now, you're just being paranoid."
    l "I am being experienced as I am. A lesson you need to learn when you're dealing with goats, Disciple."
    "The conversation is cut short as two goat guards appear out of the bushes."
    goatguard "Halt!"
    "Lothar instantly gears up to fight."
    "You quickly intervene."
    e "Wait. We would like to talk to the General. We have found something that he might be interested to see."
    "The guards look at each other. They are familiar with your presence but they clearly are wary of Lothar."
    "Then again, you can't really blame them. Lothar is on the offensive mode."
    l "Get the general or we're going to cut our way into your village!"
    l "Try and stop me!"
    e "Lothar, you're not helping!"
    "More guards immediately appear."
    "Lothar pushes you behind him as he brandishes his sword."
    "The tension in the air is so thick that it could cut."
    e "Lothar, calm down please."
    "At that moment, there is a silvery chime."
    "The goats part to reveal Furkan and Kari."
    show lothar normal at l3 with move
    pause .5
    show furkan normal with dissolve
    show kari masked at r3 with dissolve
    "Furkan's eyes darken when he lays his eyes on Lothar."
    "Kari is still as serious as usual."
    k "What is the meaning of this, courier?"
    k "We give you the permission to visit our village and you bring a murderer into our midst?"
    l "Who are you calling a murderer?"
    k "You know what you did, murderer."
    "You try to break up the tension. You figure the easiest way is to cut straight to the point."
    e "Kari, we believe we found something of magical nature at the caravan attack site."
    l "Yes, an evidence of your guilt."
    "Kari frowns."
    k "I wasn't even part of that caravan trip 4 years ago. If I were there, the tragedy wouldn't have happened."
    show lothar bored with dissolve
    l "Lies!"
    k "Why would I lie about something like that?"
    f "Kari is telling the truth... He went with me while the caravan attack happened."
    f "Of course, in retrospect, things would have been a lot more different if he was in the caravan."
    e "Lothar, I think they're right."
    l "Disciple, the goats are deceitful creatures. We mustn't be too trusting."
    f "In that case, how about we show some trust in you."
    f "I will have the guards pull back. No more blood needs to be shed."
    k "Furkan, is that really..."
    "Furkan stops his general."
    f "Kari, it will be fine. Plus, I trust the courier."
    "The goat guards back away under Furkan's order."
    "Furkan smiles at you and points to the wolf."
    e "Thank you, Furkan."
    "You turn to Lothar."
    e "Lot, perhaps you should put down your weapon too."
    "You see the veins of Lothar's hand pop."
    e "It's fine. Furkan is not going to harm us."
    "Reluctantly, Lothar puts his sword away."
    f "Thank you."
    jump Lothar_Stone_Goat_Tribe

label Lothar_Stone_Goat_Tribe:
    "Kari holds the magical stone in his palm and closes his eyes."
    "Everyone is silent, even Lothar."
    "After who knew how long, Kari opens his eyes."
    k "This is strange..."
    f "What is it?"
    k "The source of this magic is surprisingly close to us."
    show lothar angry with dissolve
    l "See! I told you they're the culprit!"
    "Lothar immediately turns aggressive."
    k "That's not what I meant."
    e "Kari, what is it then?"
    k "The lingering magic on this stone can be traced back to the dark forest."
    e "Dark forest? Where is that?"
    "Both Furkan and Lothar frown."
    show lothar stare with dissolve
    l "How are they involved in this?"
    f "Dark forest is a forest north of our outpost."
    f "It is a place where all kinds of dangerous creatures lurk."
    f "The most dangerous of them all is a pack of werewolves."
    e "Werewolves?"
    k "Yes. They are highly dangerous and fiercely territorial."
    k "Thankfully, they rarely leave dark forest. We get the occasional werewolf raid, but nothing more than that."
    e "Then, what are we supposed to do now?"
    "Furkan is silent. Kari contemplates for a moment."
    k "The trail leads us to the dark forest. You can do anything in the dark forest without the permission or at least having the werewolves tolerate your presence."
    k "The werewolves are led by an alpha. To proceed, we'll need to get his aid."
    f "But that is not going to be easy. They are highly suspicious of outsiders and have no qualms to resort to sinister means to deal with outsiders."
    f "I wish the tribe can help but with our magic dwindling, we can't afford to assign any soldiers away from the tribe."
    l "The Hero will handle this."
    e "Lothar, don't be silly. This is much too dangerous. Plus, Lusterfield still needs its hero."
    "Lothar mulls over this."
    f "Thanks for bringing this to our attention, Kari and I will see what we can do about this."
    f "I know we can't stop you from doing your fair share of adventuring. But no matter what you do, be careful."
    e "I... I will, if I go there..."
    "The general and the chief walks back to the mountain."
    scene black with dissolve
    "You go back to Lusterfield with Lothar."
    scene lusterfield01 with dissolve
    show lothar normal with dissolve
    if not lothar_along:
        e "H-hey... Lothar. You... doing alright?"
        l "...no."
        "You look at the bruises on Lothar's back and arm."
        l "And I didn't get to kill them before they get to explain."
        e "Hmm... do you need anything?"
        l "No, if I need... I'll ask that lizard to give me free ointment."
        l "..."
    l "Disciple, I may not trust the goats but they are not joking about how dangerous the dark forest is."
    e "W-what do you mean?"
    l "The werewolves, let's say they are not as heroic and honourable as me."
    l "If you set your foot in there, I'm afraid you may not come out alive."
    e "Are you scared, Lothar?"
    l "O-of course not! Why would I be scared... I'm the hero! HE-RO."
    l "..."
    l "As much as you and those filthy goats want me to believe otherwise."
    l "I'm still keeping my eyes on the goats. So I have to stay in Lusterfield."
    l "..."
    l "What?"
    e "Fine... then I'll go to the dark forest?"
    l "I didn't say that."
    l "...But it's getting weird that I'm telling you this."
    e "Tell me what?"
    l "Keep yourself... safe."
    l "You're my disciple after all. I trust that you possess half of my power."
    l "It would suffice already to survive in the forest."
    e "O-ok..."

    $ QuestFinish(quest20)
    msg "You received a level point."
    $ pc.lvluppt += 1
    jump main_lusterfield01

label Lothar_Found_Goat_Tribe:
    scene kechioeren with dissolve
    "As you approach the goat village, you can sense the palpable tension in the air."
    "You get closer and see a group of goats surrounding Lothar."
    "You take a quick sweep around and are relief to see that no one has been injured."
    "You quickly step in before things spiral out of control."
    e "Stop!"
    "Everyone turns to you."
    "The goat guards still have their spear poised at Lothar but Kari levels his penetrating gaze at you."
    "Lothar regards you with caution."
    show lothar angry at l1 with dissolve
    l "Disciple, what are you doing here? Go back. This Hero can handle this!"
    "You can see bruises on lothar's arms."
    show kari masked at r1 with dissolve
    k "Are you responsible for this idiot?"
    "Kari addresses you."
    "Lothar snarls in response. He would have attacked if not for the ring of guards suppressing him."
    e "What happened?"
    k "I would like to know that. This wolf charged into the tribe without warning to attack me."
    k "The guards held him back. We fought to a stalemate and you arrived."
    l "There's no stalemate. I would have gotten your head if not for these pesky guards!"
    e "Let Lothar go."
    k "And have the wolf attacks us? Courier, you do not make the rules here."
    "Kari eyes you threateningly."
    l "Disciple, don't worry about me. I'll cut a bloody way out if I have to."
    "The goats move into a fighting stance."
    "The ring closes in on Lothar. A guard goes in for a stab. Lothar dodges it with ease, just to step into the trap of another goat."
    "The guard smacks Lothar's wrist and his weapon falls to the ground."
    l "Arughhhh!"
    "Lothar gnashes his teeth and looks like he's going to go into rage."
    l "You can't fight me you filthy goats!"
    "Suddenly, a dignified voice carries over."
    show furkan normal with dissolve
    f "Enough. There shall be no bloodshed today."
    "Furkan walks over with the bearing of the chief."
    "Furkan's eyes darken slightly when he sees Lothar but he soon reverts to his charismatic self."
    f "What have you trespassed into our tribe, wolf?"
    l "Of course, it's to exact vengeance on our people."
    k "It was the goats who lost more in that battle."
    f "Plus, what evidence do you have to say that we're responsible for that caravan?"
    l "This!"
    "Lothar brandishes the magic stone."
    "Both Kari and Furkan frown."
    f "Where did you find that?"
    l "Wouldn't you know?"
    f "Based on what you've said, I presume you found this at the caravan attack site?"
    "Lothar growls and says nothing."
    "He's not really known for lying."
    f "Kari, what do you make of this object?"
    "Furkan turns to ask his general."
    k "It's definitely a magical artifact. As for what it does, I need to take a closer look at it to tell."
    "Lothar quickly puts the stone away."
    l "You're not destroying the evidence! I won't allow that!"
    "Furkan sighs."
    f "We're not going to do that."
    k "Plus, the artefact does not even originate from this tribe."
    e "How can you tell?"
    k "Simple. As you can see around us, we use blue magic in our glyphs. The glyphs on that stone are not blue."
    "Furkan turns to you."
    f "Courier, would you mind talking to your friend to let us take a look at that stone? So that we can put this misunderstanding behind us?"
    k "In fact, we would like to find the real culprit behind the caravan attack and avenge our people too."
    "Kari's eyes shine with determination and power."
    show lothar bored with dissolve
    "You turn to Lothar. He snaps his teeth at the goats around him."
    "You realize Furkan and Kari do have a point."
    e "Lothar, perhaps we should let them see the stone."
    l "Disciple, do not be fooled by their words! They will cut us down once we give them what they want."
    f "We will not do that. As a show of faith, I will have my people put down their weapons too."
    k "Furkan, is that really a good idea?"
    f "We need to meet halfway for peace to work."
    "Kari contemplates that for a while before giving the order for the goats to stand back."
    "The ring of weapons around Lothar loosens."
    "This gives Lothar pause."
    "You hurry to Lothar's side."
    e "Lothar, you alright?"
    l "Why wouldn't I be, Disciple?"
    e "Lothar, perhaps we should show them the stone."
    l "..."
    "Lothar hesitates."
    l "Fine. But I will keep a very close eye on them. Any funny move and I will move to kill."
    "Lothar reluctantly hands the magic stone over."
    jump Lothar_Stone_Goat_Tribe

label Lothar_Sparring:
    e "Lothar, about the sparr-"
    menu:
        l "Well, well... disciple. Finally, Are you ready to get your ass beat?"
        "Yes{#lotharsparring}":
            e "Yes... I'm ready."
            jump lothar_battle
        "No{#lotharsparring}":
            e "Hmmm... not yet."
            l "Ugh, make it quick, I'm waiting..."
            jump Lothar_Normal_Talk

label Lothar_Battle_Training:
    l "Hmm..."
    e "What are you looking at, Lothar?"
    l "You know... Amble and Jog saw you a few days ago."
    e "W-what?"
    l "And they ask me. Lot, why is your disciple so small."
    l "And I can't say anything back, usually I could tease them to oblivion."
    l "Like, not being as handsome as me, or not being the hero of Lusterfield."
    e "Hmm..."
    l "But now I don't even know what to say... because that's not my problem! That's your problem, disciple."
    e "Is it really my fault though... it's not like I can get any bigger in size..."

    if slime.lose < 1:
        l "Ugh, I'll give you the credit. For a smaller guy like you, you actually do fight like a warrior."
        e "I'll bet I can beat you, quite easily."
        e "I've had no problem punching these slimes into pulps, quite easily actually."
        l "You're a mere disciple, stop being so smug."
        e "Lothar, you just don't trust me enough."
    else:
        l "You know, that's the problem with you, everything negative about you reflects much worse on my name."
        l "Next thing Amble would tell me you got fucked by a feeble little slime..."
        l "And then they'll ask. Hu hu hu, Lot why did your disciple get fucked by a slime!"
        l "Hu hu hu! And they laugh like an idiot for hours straight."
        "Lothar imitates Amble and Jog's voices, while chuckling."
        e "How... did you know..."
    l "I really do need to train you myself, do I not...?"
    e "No, I-I can actually handle being out there. Look, I'm strong enough."
    "You try to swing your weapon in front of Lothar, who doesn't seem very impressed."
    e "Huh...? H-uh... Is t-that... g-good?"
    "After a while you started panting rapidly, you look up to Lothar."
    l "..."
    e "W-what?"
    l "Yeah, I should give you some training..."
    l "I'll level up the dummy now. You should beat it quite easily if you're... capable."
    e "I Am... capable... H-hey..."
    l "Prove to me then... And then we'll talk about training."
    e "A-alright..."
    $ dummylvl2 = dummy.win
    $ QuestBegin(quest12)
    $ quest12.qProgress(__("Defeat the dummy"))
    jump Lothar_Normal_Talk

label Lothar_After_Sparring:
    e "Lothar...?"
    l "Huh...?"
    e "About the Sparring..."
    if quest12.status == 4:

        $ lothar_spar = True
        l "Look... like I said, you can pay me any time."
        e "I-I'm fine now... thanks for carrying me back to my bed."
        l "..."
        l "Well you know what, you don't need to pay me anything."
        l "It's already expected of you to unfortunately lose to an experienced sword master like me."
        l "And also Ole found out about this and he really hated the idea of me sparring and getting money from a disciple."
        e "But... a bet is a be-"
        l "If I needed money, I can get it right from Amble's 200 gold, and Jog's after he show his face in the tavern."
        e "Hmm... Thank you... Lothar."
        l "My sword strikes are not what normal beginners are supposed to handle, I can understand that..."
        l "..."
        l "And... well you beat the advanced dummy, let's focus on the progress."
        e "I remembered..."
        l "So, anyways, take care. I should be here for you regardless, as a mentor."
        e "Thank you again."
        $ QuestFinish(quest12)
        $ pc.exp += 600
        $ pc.lvluppt += 2
        msg "You received 600 EXP and 2 level points!"
        jump main_lusterfield01

    if quest12.status == 5:
        $ lothar_spar = False
        l "You won. Feeling good about yourself?"
        e "Look, Lothar, I was just asking-"
        l "Whatever... I promised you a bet."
        l "But don't you ever tell this to any other people. I'm serious."
        l "That's gonna damage my reputation if I ever lost... to a disciple."
        e "Ok, ok..."
        if lothar_prize == 1:
            l "Here's your 500 gold."
            l "Happy?"
            e "Very..."
            l "Luckily I've got these suckers Amble and Jog to get me some free cash..."
            e "Thanks, Lothar."
            l "Yeah come to see us at night more, maybe I can get you to toss me back those golds."
            e "Hmm..."
            l "Well, that's it, champ. Now get the fuck off."
            e "Alright, Lothar..."
            $ pc.gold += 500
        if lothar_prize == 2:
            "Lothar let out a huge sigh... he is obviously annoyed by the fact that you get to squeeze his chest..."
            l "You've got what you wanted... I guess."
            call scene_lothargrope from _call_scene_lothargrope
        if lothar_prize == 3:
            l "W-what, are you that excited to kick me in the nuts?"
            e "Well I didn't know you'd actually accept that in the first place."
            l "Huh..."
            l "Let's get this over with..."
            e "A-alright- hmmm."
            l "Stop giving me your impression of a shit-eating grin, Fucking shit."
            e "I'm ready now..."
            l "I've trained my balls, So give me all you've got..."
            "You kick into Lothar as hard as you can, apparently he didn't scream or yelp, just swallowed all of his pain..."
            "However, you've felt something hard around his crotch, which is probably not his cock."
            l "F-fuck..."
            e "Lot?"
            e "Did you, have something inside...?"
            l "W-what?"
            e "Why did I feel something hard right there. Is it a protection?"
            l "No, It's done. There's nothing..."
            l "Go now..."
            e "Lot-!"
            l "Nothing is there, your bet is over. No more kick in the balls."
            e "That was so lame..."
            l "No, you are lame, I never promised to kick you in the balls, it was your idea."
            l "It was your idea to ruin the fun, why the fuck can't you just bet gold like everyone else does!"
            l "Fuck!"
            e "Al-right..."
            l "Now fuck off, for real this time."
    $ QuestFinish(quest12)
    $ pc.exp += 900
    $ pc.lvluppt += 1
    msg "You received 900 EXP and 1 level point!"
    if pc.exp > pc.expCap and pc.level <= levelCap:
        $ pc.LevelUp()
        msg "You are now Level [pc.level]! Check your inventory to allocate your level points."
    jump main_lusterfield01

label Lothar_Ask_Ole_Training:
    l "What do you want, Disciple?"
    e "Lothar, Ole suggests that I learn new skills from Jog and Amble in preparation for future courier jobs."
    e "However, they won't teach me anything without a permission from you."
    l "Of course. How can there be courier training without permission from this Hero?"
    l "Without guidance from this Hero, I doubt you can even defeat the basic training dummy."
    "You listen to Lothar wax his heroics. During a lull in his speech, you cut in."
    e "So Lothar, will you give them the permission to teach me some new skills?"
    "Lothar looks at you."
    l "Fine. When you get stronger, it'll reflect on this Hero's prestige."
    l "We can't have people saying that the Hero of Lusterfield has a weak Disciple, can we?"
    e "Sure. Sure."
    $ quest17.status =4
    jump main_lusterfield01

label Lothar_Report_Dummy:
    e "Lotharrrrrrr..."
    l "Huh? Disciple...?"
    e "I- I did it..."
    e "I took down the dummy."
    l "Oh, the dummy I told you to defeat...?"
    l "You sure have proven yourself, disciple."
    e "All he did was just punching me."
    "Lothar gives you a satisfied grin."
    l "Well I didn't even expect you're gonna actually do it."
    l "I need to tell them about this..."
    l "Follow me."
    e "Huh...?"
    scene lusterfield02
    with dissolve
    "You see lothar smirks while he looks for Amble in the village."
    "He seems to be very proud of your achievement... almost too proud."
    show lothar grin at r1
    with dissolve
    show amble normal:
        xalign -0.9
        linear 0.5 xalign 0.05
    l "Hey, Amb, where's Jog."
    a "Out scouting."
    "Amble says as he notices you."
    a "Oh, puny friend. What are you doing here?"
    e "Well, I live in this place."
    e "And I'm practising with Lothar."
    "Amble nods with a sluggish smile."
    l "I'd tell you but you won't believe stuff like this."
    l "My disciple... he beat my advanced dummy."
    a "Eh...? That's impossible! It was ridiculously strong."
    a "Like the tailor doesn't even know how to adjust their proper strength."
    "Amble scratches his head with frustration."
    scene lusterfield_alleyway
    with dissolve
    show amble normal at l1
    show lothar grin at r1
    "Amble walks towards the dummy and he soon returns in defeat, it's apparent to him that you won against the dummy."
    l "How does it go...?"
    a "I didn't even know you can possibly do it. Even Lot can't beat it every time."
    l "Now hand me those 200 gold, Ambie."
    "Lothar exclaims, he seems to be getting more impatient with Amble."
    a "Hmmmmmm..."
    l "See? [e], great job at shutting up doubters, and earning me some gold."
    "Lothar says, as he smuggishly takes the gold from Amble."
    e "Were you guys betting if I will win?"
    a "Yeah, I suppose so."
    e "And Lothar was betting for me?"
    l "Don't get ahead of yourself, disciple. He was the one betting, I was the house."
    a "Fair is fair, our puny friend here can definitely throw a few punches."
    "Amble's strong body towers over you as he stares at you physiques, perhaps trying to make sense of your victory."
    l "Heh."
    l "A few punches, yeah. Maybe under the best teaching in Mokken he can get nearly as good as I am."
    l "Not saying he can ever surpass my level, but he can try."
    "Lothar gives you a side glance."
    l "So, let's get back to the lesson."
    e "Lesson? I thought I'm just here to fight a dummy."
    l "Well Amble's here, look at him. perfect for an actual training dummy."
    show lothar normal
    with dissolve
    a "W-what?"
    l "We had a deal."
    "Amble pauses, he lets out a long sigh, before he turns to face Lothar."
    a "Deals' are deals. But make it quick."
    l "Don't you worry, lil Ambie, I will make your bet worthwhile."
    "Lothar turns towards you, and he begins to explain."
    l "So, disciple. You see, I am the hero, and Amble is the monster in the scary forest."
    e "Lothar, I know this- already, I've been outsi-"
    l "Well there's different actions you can do, against the monster."
    l "Amble?"
    "You can see Amble exhaling heavily, while Lothar is thoroughly enjoying the scene."
    show amble normal
    with dissolve
    with vpunch
    a "RAWWWWWWRRRRR-!!"
    "Amble raises his claws while pretending to shout like a monster."
    l "I'd have to beat him up to win this fight, figuratively."
    l "There are two ways actually, you can beat him up, or beat him off."
    a "Huh?"
    l "Come on, Amble."
    l "Just a little touch, won't hurt."
    e "Uhmmm...."
    "Lothar approaches Amble, who is standing there, reluctantly lettiing Lothar touch him on the chest."
    l "Well, long time no see, buddy you got a little... beefier... your chest... are you happy to see me?"
    a "I... uh-m. RAWWWWR-R!"
    "Lothar's claw wanders across Amble's front, he gropes at his plump chest, trying to get a reaction out of the lumberjack."
    "Evidently, his attempt at flirting worked as the bulge in Amble's underwear seem to only grow larger by each second."
    "If it's not noticeable already."
    l "Disciple, what do you do with the monster, if you are too weak to beat them properly..."
    e "Hmm... I think escap-"
    l "Kiss them."
    pause 0.5
    show lothar grin blush:
        linear 1.0 xalign 0.4
    "Lothar suddenly pushes himself against Amble, their lips easily touches."
    "Amble wraps his arms around Lothar's back, while Lothar continues to explore his front, rubbing against his sensitive nipples."
    "You can see Lothar's tongue entering Amble's mouth, sharing saliva as they continue to passionately kiss in front of you."
    "The alleyway begins to fill with noise of Lothar and Amble's moans, they're certainly very into this..."
    "..."
    "Lothar wants to advance on groping at Amble's crotch, but Amble holds on to his arm tightly."
    "The act suddenly reminds them of your presence... watching both of them kissing."
    "Admittedly you've grown a huge boner down there, you try to hide it but the two companions has already noticed it."
    show lothar normal:
        linear 1.0 xalign 0.95
    l "So- that's how you defeat a monster."
    l "Amble, do your thing."
    a "Eh? Oh... Right..."
    a "AHHHHH! I'M SO HORNY NOW, I'LL LOSE MY FIGHT NOW, PLEASE FUCK MY ASS."
    e "..."
    a "..."
    "Your glance and Amble's meet at the worst time possible."
    a "This is just a demonstration, [e]. I'm not actually-"
    l "Alright Amb- then that's it."
    a "Well, I'll get back to work. Good luck with your disciple."
    l "Be seeing you and Jog same place tonight."
    "Amble walks away, tugging at his underwear while, waving his hand back at you two."
    show amble normal:
        linear 0.5 xalign -2.0
    pause 0.5
    show lothar -blush at c1 with move
    e "..."
    l "What?"
    "You can see Lothar snickers while licking his lips."
    e "Are you two, in love?"
    l "What? this is just brothers being brothers. We practised kissing like that all the time."
    e "Practised- Kissing?"
    l "Well, for an all-rounded fighter like me... it's no secret you need some specialised battle training."
    e "Uhm..."
    l "So, this is how flirting works, if you're inclined to flirt with a monster, or enemy in general."
    e "I still can't believe you would flirt like this."
    l "Do I look like I'd flirt with actual kissing?"
    e "W-wait, you just said you practised flirting all the time."
    l "Practices are not real battles! You need to get your facts straight, disciple."
    "Lothar shouts, his face is getting red as he quickly explains himself."
    e "So, your pratices aren't for real battles?"
    l "NO! Stop this nonsense or I'll be the one teaching you a lesson."
    e "Alright I guess. What are you planning now?"
    l "Sparring, you and me."
    l "I have to see how you actually fight, one way or another, no question asked."
    e "Sure, I can learn more from you if I can see how you actually fight."
    l "Look, treat it like a bet, with huge stakes. If you lose to me, you'd have to pay me 500 gold."
    e "What happens if you lose to me then?"
    "Lothar chuckles, he doesn't seem to have faith in you winning."
    l "Well, you should be the one who decide, disciple."
    menu:
        l "That would be a big 'if', that I would happen to lose to my disciple. But I'll let you dream on, Heh..."
        "500 Gold":
            $ lothar_prize = 1
            e "Same thing. 500 Gold."
            l "Uhm... Are you underestimating my power?"
            e "W-what? isn't this how bet works, we bet with the same money?"
            l "Obviously, I'm stronger than you. So, the odds should favour me, by a huge margin."
            e "...You want me to get more gold if I win?"
            l "I want you to give more respect for the hero, you really think you can beat me?"
            l "Fighting you... well- this was just a demonstration sparring, to show you how strong I am."
            e "A-alright."
        "Grope Lothar like he did with Amble":
            $ lothar_prize = 2
            e "C-can, I do the same thing you did to Amble?"
            l "What, you want me to handle your chest?"
            e "Uhm..."
            l "What?"
            e "T-the opposite?"
            "Lothar pauses, until he actually realises what's happening."
            l "Why should I let you touch me."
            e "Maybe to learn from your physique?"
            l "Ugh, Alright."
            l "It's not like you can actually win against the hero right here."
            e "I'll try my best."
            l "Yeah, well try- try your breast instead, Heh..."
        "Kick him in the nuts once":
            $ lothar_prize = 3
            e "I think I should kick you... in the nuts."
            if sebas_kick:
                l "No...What's wrong with you, and your fascination with my nuts..."
                e "I just thought Sebas did it too..."
                l "That's not my point! Why would I let you kick me in the balls."
                l "Especially after that fucker of a lion fucked up my meat."
                e "Can I soothe it...?"
                l "No."
                l "Disciple, you just reminded me that you sided with the lion."
                l "For that, I'll beat you so hard, you shall give me 1000 gold instead."
            else:

                l "Huh, are you trying to avenge your little lion?"
                l "And I thought you were on my side, disciple."
                e "I just wanted to kick you..."
                l "What's wrong with you, and your fascination of my nuts..."
                l "I've never met people like you, with such audacity to argue with your hero..."
                if golem_lothar:
                    l "I saved you from the golem, it could've killed you easy if it wasn't for me."
                e "Uhm..."
            e "So... do I get to kick you?"
            l "Alright, but it's not like you can actually win against the hero right here."
            l "I mean, I've got over 2 decades of fighter training."
            l "It's totally alright for you to be just a little intimidated."
    e "I get it."
    l "Anyways, are you ready?"
    menu:
        l "For our legendary sparring... of course."
        "I am ready":
            e "Yes... I'm ready."
            jump lothar_battle
        "I need to prepare":
            e "No, I still have to prepare, I had already spent all my energy beating the dummy."
            l "Alright, alright, go ask your little lizard friend for tips or something."
            l "You can't win against me anyhow."
            e "Uhm, we're just sparring, right?"
            l "Yes, I suppose, this is your big opportunity to learn from the best out here."
            l "This hero right here aren't always here to fight with someone like you."
            e "I get it. I should go now?"
            l "Yes, you can go now, I'll just be waiting..."
            $ quest12.status = 3
            $ quest12.qComp(_("Spar with Lothar"))
            jump main_lusterfield01

label Lothar_Ask_Invasion:
    if ole_told and quest10.status == 2:
        e "Lothar, can you tell me again about your plan?"
        show lothar angry
        with dissolve
        l "You dare to ask me this? After you outright told Ole about our secret plan?"
        l "Are you ever on my side."
        e "Uhm... What?"
        l "Stop pretending you're innocent in every fucking matter, I trained you, made you an adventurer..."
        l "And this is how you repaid me?"
        l "Fucking stab me in the back?"
        pause 0.5
        e "I just think Ole deserves to know the truth, I didn't have the heart to lie to him."
        l "Fuck off."
        "Lothar leans on the brick wall, he gives you a side eye before looking away..."
        "The air becomes frozen for a moment as both of you stay silent."
        menu:
            "You feel like you need to say something..."
            "Apologise":
                e "I'm sorry, Lothar."
                l "You all are like this, taking my kindness for granted..."
                e "I'm... really sorry, Lothar."
                l "..."
                show lothar bored
                "Lothar continues looking away, but his expression seems to soften a bit."
                e "I'm sorrrrry."
                "You grasp at Lothar's paw, slowly nudges at the fur on the back of his hand."
                e "Hey, Sorry."
                l "You need to do much better than that..."
                e "W-what do I need to do? My boss."
                l "..."
                l "Since when did you learn talking like this..."
                e "When I feel like I'm really really sorry, I guess."
                show lothar stare

                l "Huh... Well I'm not impressed, yet, disciple."
                l "And don't you think you can seduce a hero with your big..."
                e "Big what?"
                l "Ahem- No. Back to the topic. The plan."
                e "Do you accept my apology...?"
                l "Y-yes, but watch your back..."
                l "Anyways, the plan. Ask for direction, pretend you're fainting. Get inside, and ask around."
                e "Alright... I'll think about it."
                l "Don't think for too long. Else, I'll be angry... again."
                $ quest10.status = 20
                $ quest10.qComp(_("Report to Lothar"))
                jump Lothar_Normal_Talk
            "Protest":
                e "Look Lothar, I don't know what you want, but that wasn't my fault."
                l "..."
                e "Ole was right, you shouldn't even try to spy on the goat tribe at the first place."
                l "Y-you say what? Fuck you and your devious little tactics."
                l "Trusting your sweet little lies was a mistake, I don't even know how you became my disciple."
                l "I shouldn't have listened to that lizard, teaching you, mentoring you."
                l "And now you stab me in the back and tell me I'm wrong?"
                e "..."
                e "What I'm telling you is, you are a big dumb wolf!"
                e "And don't you blame me for having an intact, functional brain that can think for itself!"
                "You feel as if you are tired of being a pushover for such a long time."
                "And it somehow feels good. Almost... a relieve."
                "But the excitement fades soon when you snap back to reality and see Lothar staring at you..."
                l "Y-"
                l "Fuck the fuck off before I fucking stomp you into a pile of useless dragon pulp."
                pause 1 
                l "GET YOUR ASS OFF RIGHT NOW!"
                "You retreat immediately as your sudden momentary courage fades out... and you're left with feeling bad for speaking out."
                "The wolf doesn't seem to appreciate it as well..."
                $ lothar_argue = 1
                $ QuestFinish(quest10)
                jump Lothar_Normal_Talk
    else:

        show lothar normal
        e "Lothar, can you tell me again about your plan?"
        l "Yes, it's very simple actually. Ask for direction... somewhere, then pretend you're going to faint."
        l "Then get inside, ask around. They'll be easy on you because of your badge."
        e "...Alright."
        l "So, what do you say, disciple. Are you going to do me a favour?"
        if golem_lothar:
            l "Maybe considering I saved your ass from that stone golem?"
    menu:
        l "I don't usually owe someone a favour, though. If you are curious."
        "I'll get into it":
            e "I'll get into it."
            l "Hmmm... Good."
            l "Just remember what I told you, because getting caught might be a little dangerous for you."
            e "W-what?"
            l "I mean surely you wouldn't get caught right?"
            l "It's like fighting a slime and lose, that's impossible."
            l "But if you do, well... they probably won't kill a courier."
            e "..."
            e "Alright..."
            l "Here's the location. Goat Tribe. Let me mark it on your map."
            l "West to the Outpost..."
            e "Got it. Thanks Lothar. I'll be back soon."
            $ kechioeren.discovered = True
            $ quest10.status = 3
            $ quest10.qComp(_("Visit the Goat Tribe"))
            jump Lothar_Normal_Talk
        "Maybe Later":
            e "Maybe... Later?"
            e "I need to think about it."
            l "Okay then."
            jump Lothar_Normal_Talk

label Lothar_Report_Goat:
    e "Lothar, I'm back from the goats."
    l "Oh...?"
    menu:
        l "So what did you find?"
        "Tell everything you know":
            $ lothar_knows = True
            e "Uhh... I think they were... looking for their guardians..."
            l "Hmm?"
            e "The Golem we met, it's their Guardian that got lost somewhere."
            l "Ah... Their guardian..."
            l "Alright then."
            l "I'll have to see it for myself."
        "Conceal your knowledge":
            $ lothar_knows = False
            e "Uhm... I didn't find much."
            l "Really?"
            e "Yeah, I just get inside and they seem pretty normal."
            l "Meh... Alright."
    e "So... that's it?"
    l "I guess so."
    l "If they aren't planning anything, I wouldn't be the one that attacks."
    l "Did you learn anything about your little friend?"
    e "I don't know..."
    l "Alright."
    l "I'll meet you another time then, disciple."
    e "See you, Lothar."
    $ QuestFinish(quest10)
    jump Lothar_Normal_Talk

label Lothar_Outfit_01:
    $ opinions_Outfit[0] += 1
    e "Lothar, do you have some time?"
    l "Disciple, what do you want? Don't you know my time is precious? And what the fuck are you wearing?"
    "Lothar's eyes wandered over to your lower body and you cheeks turn red."
    e "Does this look weird? Rahim wants me to get your opinion regarding this set of clothes as adventuring gear. Its stupid, right?"
    l "Disciple, what are you talking about? This is marvelous. Despite his pissy behaviour, that bull's creations are the best in town."
    l "This armor will provide all the arsenal you need in battle to distract and overcome your opponent."
    e "... If you say so."
    jump Lothar_Normal_Talk

label Lothar_Outfit_02:
    $ opinions_Outfit[3] += 1
    l "What is it that you're wearing?"
    l "Does it even provide any protection?"
    e "Well, it's not really an outfit to go fighting in..."
    l "Hmm, perhaps the lack of protection is intentional."
    l "That's not a bad way to win some battles."
    l "Disciple, it looks like you've been practicing hard at the art of seduction."
    l "However, you can't just focus on one style of fighting."
    "Lothar closes his eyes and starts to launch into a lecture..."
    "You decide to thank him and slip away before he notices."
    jump Lothar_Normal_Talk

label Lothar_Outfit_03:
    $ opinions_Outfit[6] += 1
    l "I have seen combat outfits like that before."
    l "Can't say that I'm a fan of it."
    l "They're normally worn by magic users."
    l "Real heroes charge in the front. Get it, Disciple?"
    e "Uhmm... Yes?"
    l "Now, move so I can continue with my training."
    e "What training?"
    l "Endurance training. For if I see that outfit one more second."
    jump Lothar_Normal_Talk

label Lothar_Invasion_Quest:
    pause 0.5
    show lothar stare
    with dissolve
    l "Disciple, sounds like you've been trying to meddle with the goat business a lot."
    e "Lothar. What do you mean?"
    l "There's something wrong with the goats. I can sense that they're plotting something against our village..."
    l "And that goat leader. Doesn't he look a bit suspicious...?"
    show lothar normal
    e "Uhhh... What?"
    l "I need some information, before I decide on my action against the goats as the hero of Lusterfield."
    l "It's best we talk about this in the alley."
    e "Alright..."
    scene black
    with dissolve
    pause 1.0
    scene lusterfield_alleyway
    with dissolve
    show lothar normal
    e "So, you want me to go to the goat village?"
    l "Yes. Don't talk too loud, disciple, the lizard might be eavesdropping somewhere..."
    e "Uhm, why me? Why don't you ask one of your friend..."
    l "Look, they already recognise most of us hero squad. But you're the courier... I think they won't try to kill you."
    e "But... uhh... the goats already tried to kill me, the huntsmen."
    if goat.lose > 1 or goat.win > 1:
        l "Uh no..."
        l "I see you and those huntsmen had a lot of fun in the forest, didn't you?"
        l "Not necessarily trying to kill you in anyway..."
        e "...How did you know?"
        if sebas_kick:
            show lothar bored
            l "Plus, you owed me last time when you sided with the lion."
    show lothar normal
    l "I just need to know what's going on, the golem hand, and the whole riverside. They're hiding some secrets..."
    l "And if they're planning for an attack, we need to at least be prepared."
    e "Lothar, Furkan told me he's not going for a war."
    l "Hey, maybe he still holds a grudge after I killed his little father."
    e "Uhm..."
    l "Disciple."
    if golem_lothar:
        l "You know I, a hero, saved you from the golem, right?"
    l "It's time you prove yourself as a decent adventurer, you won't be the hero, of course, but an adventurer for sure."
    l "And I've heard your little buddy, Chime? That's who you've been chasing this whole time?"
    e "..."
    e "What's your plan...?"
    l "Just get near the tribe, tell them you are lost or something."
    l "And then pretend you are almost going to faint, just ask for some food, or something."
    e "Ehm... should I bring anything there?"
    l "Well, of course you're not bringing your food there, it wouldn't make sense actually."
    l "Just get inside, ask around... And that'll do, ask what happened to their magical stone."
    l "Or peek into the ram's room if you can. Of course, you'll have to be sneaky enough."
    l "But generally, a quick tour would suffic-"
    "You senses a figure overshadows you and Lothar from behind, it's Ole. The wolf instantly turns away from you."
    show lothar bored at l1
    with move
    show ole bored at r1
    with move
    o "What the hell do you think you are doing, Lot."
    l "Fuck... Hey, Lizard."
    o "Lothar?"
    l "We're talking about training... advanced sword fighting skills- tactics."
    o "No. I've heard you say peek inside something... And a tour?"
    l "Ahem...Disciple?"
    menu:
        o "What did the wolf say... [e]."
        "Tell Ole about Lothar's plan":
            $ ole_told = True
            e "Uhm... Lothar asked me to get inside the goat tribe."

            if sebas_kick:
                show lothar angry
                l "No... not again."
            else:
                show lothar stare
                l "Look, Ole, it's not what you think."
            o "What do you mean, getting inside the goat Tribe?"
            o "Why would you... Lothar."
            o "Did you just ask [e] to do this stuff for you?"
            l "It was an offer, a consensual offer."
            o "...You're lying again."
            o "Don't you ask him the same thing again... you hear me? Now go."
            show lothar bored
            l "What... I go?"
            o "Go back to live out your pretend hero fantasy, Lothar. Don't make me tell you twice."
            l "Huh..."
            hide lothar
            with dissolve
            show ole normal at c1
            with move
            o "[e]... don't listen to that wolf's bullshit excuse, he's trying to sway you into doing cheap labour for him."
            e "I am not sure, I wanted to ask the goats about my friend."
            o "Look, the goat tribe is too dangerous, we don't know what they'll do to you if you get too close."
            o "So, just stay, go out and do your usual stuff. I suspect Lothar will ask you the same offer again."
            o "Come on. We'll think of a much safer way for you to look for your friend."
            e "Yeah, I don't know."
            o "..."
            o "Trust me, [e]. It's a road you never want to go."
            e "I have to think about it."
            o "Look, opportunity will come and you will see your friend soon, just don't take shortcut and get into Lothar's stupid hero business."
            e "..."
            e "Alright, thanks again, Ole."
            o "Yeah. I'll be here."
        "Lie to Ole":
            $ ole_told = False
            e "Ole, Lothar just told me to peek inside his pants, or something."
            e "And the tour is metaphorical, you know, enormou-"
            show ole shocked
            if sebas_suck > 0:
                o "Oh... [e]. Why do you have to fuck everyone in the village..."
                e "Hey, he asked me."
                e "The thing with Seb was a one-time thing, I promise."
                show lothar shocked
                $ lothar_know_sebas_suck = 1
                l "Wait you fucked the lion?"
            else:
                o "What? Why didn't you tell me you two have been... fucking."
                e "We're... uhh... just checking."
            o "You- Alright. I don't want to know. Don't tell me, don't make me think."
            show lothar stare
            l "Well, lizard, asked and answered."
            "Ole looks as uncomfortable as he can."
            o "Uhm... I gotta go."
            o "Have fun, you two."
            hide ole
            with dissolve
            show lothar normal at c1
            with dissolve
            l "Ahem... so, good job, disciple."
            if not sebas_kick:
                l "Impressive almost, if we count the one time that lowly lion dared to ask you to kick me."
            e "Look, Lothar... I'm still not sure about whole getting into the goat Tribe thing..."
            e "I'll think about it, later."
            l "Hey, disciple, it's your only chance to prove yourself."
            e "Alright...Lothar, you're pushing me too hard."
            show lothar stare
            l "So, let me know if you're read-... when you're ready."
    $ QuestBegin(quest10)
    $ quest10.qProgress(__("Talk to Lothar"))
    jump main_lusterfield_alleyway

label Lothar_Report_Amble_Jog:
    l "Disciple, I've heard back from Jog and Amble about your training."
    e "Did I pass?"
    l "You have passed by their standards, but by the hero's standards, you still have a long way to go."
    if amble_train == 1:
        l "Amble said that you showed good form during his training."
        l "With enough, you should be as large as he is... or at least that's what Amble thinks."
        e "Thanks? I'll continue to work hard."
        l "Amble also provides some notes here for you on how to tone your muscles."
        "Lothar hands you what appears to be a drawing of yourself."
        e "This is very nice. I shall thank Amble later."
    else:
        l "Amble said you are a bit unsteady at first."
        l "But after some lessons, you starts to get it."
        e "I learned a lot from Amble."
    l "So... he concludes that you have great potential, but will keep his eyes on you."
    l "And... for Jog..."
    if jog_train == 1:
        l "He commented that you are quick on your feet."
        l "Nice job following through with the plan."
        e "All I did was follow his lead."
    else:
        l "He observed that you are light on your feet."
        l "But he says you can use some more practice in your landing."
        l "Then, he drew something that looks like a W here."
        e "..."
        "You believe that is a butt but you say nothing."
    l "So disciple, you and Jog have discovered something important."
    e "But we're not sure what they..."
    l "The goats are clearly up to no good."
    if lothar_knows:
        l "As the hero predicted, the goats are not trustworthy people."
        l "They said they've been outright and are willing to form a truce."
        l "But they are still plotting something without telling Lusterfield."
        e "But it sounds like they're not really trying to harm Lusterfield."
        l "You have helped saved one of their own and take down their rampaging golem."
        l "You'd think that will help you earn their trust."
        l "Clearly, everything is a front with the goats."
        l "They are not as forthcoming as this Hero."
    else:
        l "The goats are clearly still wary of outsiders."
        l "You've been invited into their tribes, but they didn't really reveal anything to you."
        l "This showcases a lack of trust."
        "You feel rather guilty that you didn't tell the truth earlier."
        l "Something is fishy. Perhaps they have something to do with the golem attack at the river."
        l "I wouldn't put it past them."
    if lothar_argue:
        l "I know I can count on Jog to infiltrate into the goat tribe."
        l "You... still have more to learn from him, Disciple."
        l "After you dared to argue with me last time. Now I got you to go there either way."
        e "Hmm..."
        l "But thanks to you two, now we have this valuable info."
        e "But we don't know what to do with it..."
    l "Either way, it is clear that the goats are up to coming."
    l "The hero will naturally thwart them."
    l "They mention something about the caravan?"
    e "Yes, I believe so. Something about the attack that doesn't sit right with them."
    l "They have so much blood on their hands. Of course, it would never sit right with them."
    l "So, the Hero will look further into this."
    l "Do not worry now... I will handle everything... Heh."
    l "And..."
    "Lothar coughs and then straightens himself."
    "You believe he is examining your body."
    l "Ahem. Both Jog and Amble suggest that you join us for the special training."
    l "They think you'll be an interesting asset."
    e "What is the special training?"
    "You believe you see Lothar's cheeks redden slightly."
    l "It is a group training that is currently between us."
    l "Jog has specially mentioned that you will have a lot to contribute to the training."
    "Maybe you have imagined it, but there appears to be a stress when Lothar said the word, a lot."
    e "It sounds fun. If the training can help with my adventure, I'm all for it."
    l "Not so fast, Disciple."
    l "They might have suggested that you can join."
    l "But my judgement on you is still out."
    l "You need to prove yourself further."
    e "How can I do that?"
    l "I haven't thought about it yet..."
    l "Now, leave the hero in front of you to his thoughts."
    $ QuestFinish(quest13)
    jump main_lusterfield01

label Lothar_Ask_Amble_Jog:
    l "Those two? They are good company."
    l "Amble can be a bit gullible and Jog sometimes takes thing too lightly."
    "You think to yourself. 'They don't sound that reliable'."
    l "However, they are very good at their job."
    l "For example, Amble can crush the training dummy with one direct smash."
    l "Jog can shoot through its head from a mile away."
    l "However, neither of them is a match for me."
    "Lothar puffs up his chest proudly."
    if not lothar_spar:
        l "You're going to be fine because you lost to the hero as well. You're in good company."
        l "Similar to you, they have not beaten the hero in a battle either."
    else:
        l "I doubt you can win either of them, so in a way, you would still have lost to this hero."
        l "Uhh... They will prove that your win last time is just a lucky coincidence..."
    e "..."
    l "In any case, since they call me their Boss, I have a responsibility to watch over them."
    e "That's very nice of you, Lothar."
    "Lothar's cheeks redden a bit at your compliment. He coughs to cover it."
    l "This is nothing, Disciple. It's part of my job as the hero of Lusterfield."
    l "Speaking of, Disciple. They seem to have a less-than-favorable view of you."
    e "Why would they think that?"
    l "No idea."
    "Lothar shrugs."
    l "However, I need you to prove to them that no Disciple of this hero is a weakling."
    l "So... Go on solo training with each of them."
    l "Don't let me down, Disciple."
    $ QuestBegin(quest13)
    $ quest13.qProgress(__("Train with Amble and Jog"))
    jump main_lusterfield01

label Lothar_Night_Greet:
    l "Hmm... Ahoy! Little disciple, Don't see you often in the tavern. Down to drink a few beer?"
    e "Hey... Lothar. I heard you'd go to tavern at night."
    l "You are right. Try some beer, it's the best in the whole continent."
    l "Hey, Cane. Get some beer, for this little guy here."
    show lothar drunk blush:
        xalign 0.05
        yalign 1.0
    with move
    show cane normal:
        xalign 2.95
        yalign 1.0
    with move
    show cane normal:
        xalign 0.95
        yalign 1.0
    with move

    if nocturnal_serve > 0:
        c "Aye, Lot. I reckon this lad worked in our tavern before, he probably should be serving ya ass instead."
        menu:
            l "Hmm... A server? And I thought you were an adventurer like me. How disappointing."
            "I was forced to do it":
                $ lothar_lies += 1
                e "Hey... I was just working for Cane because I don't have any money on me. I really don't like doing it."
                l "The Cane I know aren't that guy to force someone to work for money, ya seriously trying to fool me or what."
                c "Lot, Ya really should come here on daytime, this thirsty lad is seriously trying to seduce all his customers or something."
                e "No... I didn't."
                l "Well, I'll take Cane's word for it. Let me know when you come to work again, I'll totally let you serve me."
            "I enjoyed the job":
                e "Look, I can go for some side hustle, can't I. Besides, serving people is really fun."
                l "I see, I see. You definitely need to hone your serving skill though, because I don't see you serving me here."
                c "Hah, the apron fit yer ass at least, come here more often, we all need yer sweet ass."
        l "Hey, Cane. You forgot about the beer thing?"
        c "Ye, ye. Shut up Lot. I'm brewing the finest stuff here."
        c "Here it is, one for our hero, and one for our lowly server."
        e "Hey... Why am I lowly."
        c "Cause yer not the hero."
        e "Hmm..."
    else:
        c "Aye, Lot. Here's yer beer. And here's one for our new proper lad, [e]."
        e "Thank you Cane. This tavern is actually really cozy."
        c "Look, I need someone to help me take care of the tavern, [e]. Serving food and drink to our misters and misses."
        e "Hmm... me?"
        c "Ya look like a proper candidate, real perfect size. Let me know when yer interested."
        e "A-alright, maybe next time?"
    l "Thanks for the beer anyway, Cane."
    c "You are Welcome, let's see. I'm gonna serve the others while you two chit chat. Alright?"
    l "Ya."
    e "See you, Cane."

    show cane normal:
        xalign 2.95
        yalign 1.0
    with move
    show lothar drunk blush:
        xalign 0.5
        yalign 1.0
    with move
    l "Hmm... Like the beer?"
    e "A little bitter for my taste, not that I've drank it before."
    l "You'll get used to it, you all do."
    l "Speaking of which, let me introduce my comrade to you. They're coming back right now I believe."
    "As you look behind, you see two beefy dudes at the tavern door, walking toward you and Lothar. Lothar waves at them in excitement."
    "One of them seems like a red bear, and the other a hyena. They both hold a few meat in their hands, throwing them on the table."
    comrade "Lot, who is this new guy over here."
    "Both of them stand behind Lothar, staring at you with suspicion."
    l "He's [e]. This is Jog, and that's Amble."
    jog "Oh, Lot you brought a new member or what.. Nice to meet you though, [e]."
    e "Nice to meet you, Jog. And nice to meet you too, Amble."
    amble "Hmm... has he proven himself to be capable enough to join us."
    l "No, he's not joining us. He's still got a long way to go to prove himself."
    menu:
        l "Talking about proof... You got your courier badge yet?"
        "Yes{#lotharhavebadge}":

            e "Hmm... Yes."
            if pc.armor["Bccessory"] != None:
                if pc.armor["Bccessory"].img == "Courier Badge":
                    l "Ahhh.... I see that on your chest now. It's got your face in it, isn't it. Ole really did something."
                    amble "I'd get his cute little face in my chest, like right now."
                    l "Hey, he's mine. Go get your diciple somewhere else."
                    jog "Not gonna lie though, where did you find this little fella."
                    l "He's from that lizard, told me he's another outsider or something."
                else:

                    show lothar angry
                    $ lothar_lies += 1
                    l "Wait... Where's your badge... [e]?"
                    e "Uhh... I forgot about it."
                    l "Are you really lying to me again? You moron..."
                    e "Hmm... I'm sorry about that Lothar, I think I haven't finished Ole's quest yet."
                    jog "Hey, he's just a kid, Lot. I'm sure he didn't mean it."
                    l "Whatever, I'm gonna need more beer after talking with this... kid."
                    e "Hmmph... I've got to do other things now... I gotta take off, Lothar, and you guys."
                    l "Good, if you stayed for one more minute I'll make sure you get the taste of a real kick in the nuts."
                    amble "He meant see you later. Good night, [e]."
                    e "Good Night."
                    "Looking at Lothar's annoyed face, you decided it's better for your safety to leave the three drinking their beer in peace."
                    jump main_nocturnaltrunk2
            elif LookForItem("Courier Badge", inventory):
                l "Ahhh.... it's in your bag now. It's got your face in it, isn't it. Ole really did something."
                jog "I'd get his cute little face in my bag, like right now."
                l "Hey, he's mine. Go get your diciple somewhere else."
                amble "Not gonna lie though, where did you find this little fella."
                l "He's from that lizard, told me he's another outsider or something."
            else:
                show lothar angry
                $ lothar_lies += 1
                l "Wait... Where's your badge... [e]?"
                e "Uhh... I forgot about it."
                l "Are you really lying to me again? You moron..."
                e "Hmm... I'm sorry about that Lothar, I think I haven't finished Ole's quest yet."
                jog "Hey, he's just a kid, Lot. I'm sure he didn't mean it."
                l "Whatever, I'm gonna need more beer after talking with this... kid."
                "Looking at Lothar's annoyed face, you decided it's better for your safety to leave the three drinking their beer in peace."
                e "You know what, I've got to do other things now... I gotta take off."
                l "Good, if you stayed for one more minute I'll make sure you get the taste of a real kick in the nuts."
                amble "He meant see you later. Good night, [e]."
                e "Good Night."
                jump main_nocturnaltrunk2
            amble "Outsider? I thought he was from the Goat, look at his horn."
            l "Surely it's something. The lizard asked me to take care of this guy, teach him some stuff."
            e "Hmm... may I say something-"
            l "No. Let me finish with you, And I'll let you go, eh?"
            e "Alright, Lothar."
            l "I'm telling you, come here more often. We'll talk about some informal training with you. Get you stronger to fend off your enemy or something."
            if slime.lose > 0:

                l "It's not easy watching you managing to lose to a little slime."
                e "How did you.... know."
                l "I mean, look at those stains of slime on you down there. Gotta wash it off completely tonight, [e]."
                e "Lothar, can we not talk about this in front of everyone..."
            else:
                e "I'm not sure I want to fight the dummy again, Lothar."
                l "Ahem, I'll make him stronger for your level, alright. Plus, if you're strong enough, you can attempt dueling me."
                e "Really?"
            jog "Look, [e]. Lot is putting in some precious time for you. You better pay him back when you actually get stronger."
            amble "Yeah, you don't even look like a courier right now. Better step up your game before you get eaten by some monster elsewhere."
            e "I guess... Thanks Lothar."
            l "Good. Now, why not leave me and my guys in peace. We'll catch up later, [e]."
            e "Alright, see you."
            jump main_nocturnaltrunk
        "No{#lotharhavebadge}":
            e "No... I haven't finished it yet."
            if pc.armor["Bccessory"] != None and pc.armor["Bccessory"].img == "Courier Badge":

                l "[e], that was really a low lie. You have your badge on your chest right now. Who are you even lying to?"
                e "Uh... Sorry I forgot about it."
                l "It doesn't even make sense, [e]. You're just messing with me now aren't you. Aren't you funny. You feel better about yourself messing with the hero?"
                l "Whatever you wish. You're lucky you have that lizard watching your back... Look, he even made the badge out of your face."
                jog "I'd get his cute little face in my chest, like right now."
                show lothar normal blush
                with dissolve
                l "Hey, he's mine, you flake. Go get your diciple somewhere else."
                amble "Not gonna lie though, where did you find this little fella."
                l "He's from the lizard, told me he's another outsider or something."

            elif LookForItem("Courier Badge", inventory):
                $ lothar_lies += 1

                l "[e], I can see the courier badge in your messager bag right now. Who are you even lying to?"
                e "Uh... Sorry I forgot about it."
                l "It doesn't even make sense, [e]. You're just messing with me now aren't you. Aren't you funny? You feel better about yourself messing with the hero?"
                l "Whatever you wish. You're lucky you have that lizard watching your back... Look, he even made the badge out of your face."
                jog "I'd get his cute little face in my bag, like right now."
                l "Hey, he's mine, you flake. Go get your diciple somewhere else."
                amble "Not gonna lie though, where did you find this little fella."
                l "He's from the lizard, told me he's another outsider or something."
            else:
                if quest04.status == False:
                    l "Well, you haven't finished my training for you, of course you don't have the badge."
                else:
                    $ lothar_like += 2
                    l "Hmm... You haven't finished with the others yet?"
                    e "I was out adventuring after your training. Lothar."
                    l "Hmm... well then keep up with your training! Don't even think about slacking off."
                jog "So... Lot, where did you find this little fella?"
                l "He's from the lizard, told me he's another outsider or something."

            amble "Outsider? I thought he was from the Goat, look at his horn."
            l "Surely it's something. The lizard asked me to take care of this guy, teach him some stuff."
            e "Hmm... may I say something-"
            l "No. Let me finish with you, And I'll let you go, eh?"
            e "Alright, Lothar."
            l "I'm telling you, come here more often. We'll talk about some informal training with you. Get you stronger to fend off your enemy or something."
            if slime.lose > 0:
                l "It's not easy watching you managing to lose to a little slime."
                e "How did you.... know."
                l "I mean, look at those stains of slime on you down there. Gotta wash it off completely tonight, [e]."
                e "Lothar, can we not talk about this in front of everyone..."
            else:
                e "I'm not sure I want to fight the dummy again, Lothar."
                l "Ahem, I'll make him stronger for your level, alright. Plus, if you're strong enough, you can attempt dueling me."
                e "Really?"
            jog "Look, [e]. Lot is putting in some precious time for you. You should really pay him back when you get stronger."
            amble "Yeah, you don't even look like a courier right now. Better step up your game before you get eaten by some monster elsewhere."
            e "I guess... Thanks Lothar."
            l "Good. Now, why not leave me and my guys in peace. We'll catch up later, [e]."
            e "Alright, see you."
            jump main_nocturnaltrunk2

label Lothar_Ask_Goat_Tribe:
    $ opinions_GoatTribe[3] = 1
    e "Lothar, What do you think about the Goat Tribe?"
    l "Goat Tribe? Are they planning for a round two and I can beat their ass again?"
    l "Yeah, maybe I'll be the hero of the hero of Lusterfield."
    e "Uhh... What's a hero of the hero."
    l "It's the... thing, with word."
    e "O-ok. I thought you knew about what happened..."
    l "I- what? What happened?"
    e "Furkan asked me to send a letter to Rahim... for peace with Lusterfield."
    l "...Why did no one told me... about this."
    l "I'd instantly go kill that son of a goat and get his head as a trophy, for we Lusterfield people deserve it."
    e "...Now I know why they didn't tell you."
    l "What are you implying, disciple."
    e "Uh... nothing."
    jump Lothar_Normal_Talk

label Lothar_After_River_Trip:
    e "Lothar? How did you feel after the trip?"
    if sebas_kick == True:
        show lothar bored
        l "My balls still hurt."
        e "Really? I didn't know Seb hit you that hard."
        l "Yeah, and I didn't believe you would side with the lion."
        e "Hey, I just thought you kicked him first."
        show lothar stare
        l "Well that was justified because he kept talking about my-"
        l "Whatever."
        e "...What were you talking about?"
        l "Nothing."
        l "If you betray me again next time, I'm gonna kick your nuts instead."
    else:
        show lothar chuckle
        l "Did you see that lion's fucking face."
        l "I was gonna punch him in the nuts."
        e "Hey Lothar, you two should just make up for whatever happened."
        e "I just don't want to come and see you two arguing who has the bigger dick."
        show lothar grin
        l "You know what, mine's obviously bigger than his."
        e "Hey, that was not meant to be taken literally."
        l "I'm gonna show him my cock when I see him next time."
        e "Are you serious..."
        l "Well you can be the judge, or the lizard. I think he's a fairer judge."
    show lothar normal
    e "Uhmm..."
    e "Anyways... What did you make of the golem?"
    l "Golem?"
    l "Oh... the one with the moss."
    if golem_lothar:
        show lothar chuckle
        l "Ha, I saved your ass from that golem. I was right about you all along."
        e "You just happened to be the one killing him..."
        l "No...You need me, [e]. You need me to protect you."
        e "Ummm I guess... Thank you for saving me?"
        l "That's the spirit. You know what... Come here more often so I can protect you."
        l "Drink a few beers with me and the squad you know."
        show lothar grin
        e "I will, I just don't want to get too drunk..."
        l "Ha. Like I said, I'll protect you, you oaf."
        e "O-ok."
        l "If you don't get drunk, how can I take care of you?"
        "Lothar raises his soft hand and pats your head several times, he smiles when you squirm under his paws."
        l "You are a really cute oaf."
        e "...thank you?"
    else:
        show lothar chuckle
        l "That stone got me some real gold. Like I'm not kidding."
        l "I got some expensive ale for Amble, he loves beer too much if I have to say."
        e "Uhh, did you spend a lot on the beer?"
        l "Yeah, where do you think the money goes. Straight to the tavern."
        e "That's why Cane loves you so much."
        show lothar grin
        l "What? Can't a wolf have fun drinking after saving the village once again?"
        e "No... I just was thinking maybe you should save some money for yourself."
        l "Money isn't alive, people are. I'm not gonna waste time saving something that's not even breathing."
        e "..."
        e "You got a point."
        show lothar stare
        l "I've gotta save you somehow, but you seem to be able to handle yourself... too much."
        e "Why am I... too much?"
        l "You're not supposed to be strong. How can I protect you otherwise..."
        l "Whatever, time will come when you need me."
        e "Ok... Lothar."
    jump Lothar_Normal_Talk

label Lothar_Mossy_Artifact:
    e "Lothar, what are you holding... on your hand?"
    l "It's an artifact, from my grand mythical adventure through the mysterious jungle of forest last night."
    e "Uhhh... you found it in the green forest?"
    l "You're close, it's near the river."
    e "What are you going to do with it?"
    show lothar chuckle
    l "I'll take it to the pawn shop and get a good price for a few extra beers tonight, of course. Except that I'm not gonna go inside, and it's your chance to help a hero out."
    e "W-What... You want me to sell the stone... for you?"
    l "Why yes. Just go in and ask that stupid lion to buy it off or something..."
    e "...Lothar, I think you should come with me."
    l "What??? Why would I, a hero, listen to an inferior disciple."
    show lothar angry
    e "I'm not doing this for you, Lothar. You either go alone or go with me."
    l "I don't even... need to sell this to the pawn shop. [e], you really disappointed me this time."
    e "..."
    l "..."
    show lothar bored
    "Lothar looks away for a few moments, but you can already see through his witless tantrum. He glances at you for a few time before turning back at you."
    l "You... take the lead."
    e "Good- Lothar."
    l "...Go before I change my mind and beat you up..."
    scene kings_pawn
    with fade
    show lothar bored at r1
    with dissolve
    "You lead Lothar to the pawn shop, there's no customers for now. You can see the wolf awkwardly peeking through to door before entering, he hides behind you while wagging his tail."
    l "..."
    s "Go-od... Fuc-"
    show sebas bored at l1
    with dissolve
    "Sebas becomes aware of the wolf behind your shorter frame. He is visibly annoyed, almost angry at both of you."
    s "Lothar."
    l "Lion."
    s "Why are you here? Did you miss the sign 'No dogs allowed' outside the shop?"
    l "This little friend of yours kept pulling me in, I have little to no interest in visiting your feeble shop."
    show lothar angry
    s "Fuck you. Lothar."
    l "Back at you."
    e "...I can lend you the bed if you two need-"
    l "Look, Lion. I have a better deal here. I've got a stone for that silly little stone collection of yours. We're only here for a little transaction."
    s "A transaction huh? Well... A transaction needs a little exchange from both side. And I reckon there's a debt you owed me..."
    l "...Debt?"
    s "The kick. You kicked me in the nuts last time, fuck! Let me give you the fucking foot and I'll consider a transaction between us."
    show lothar shocked
    l "No way... I'm not- There's no way you're going to touch me anywhere, let alone kick."
    e "Wait... Are you sure... we're doing it here?"
    s "Yes, Lothar. Be a man and accept the consequence of your action."
    l "I've told you... No! Go fuck yourself, lion."
    show sebas normal
    s "Alright, if you don't want to do it the right way. Let's go ask [e], he knows what's right and what's wrong."
    show lothar stare
    e "What... me?"
    s "Yeah, buddy. Make the call. Give me the go ahead and I'll make him taste the lion legs."
    l "Disciple, I highly advise you not to trust the lion's words. There will be consequences, for both of you. For real. Don't."
    menu:
        s "What do you think, you want to punish this arrogant wolf for so long, right? It's time to teach him a lesson."
        "Let Sebas kick Lothar in the balls":
            $ sebas_kick = True
            jump Lothar_Sebas_Kick_Yes
        "Do not let him kick Lothar":
            $ sebas_kick = False
            jump Lothar_Sebas_Kick_No

label Lothar_Sebas_Kick_No:
    e "No... I think Lothar's had enough."
    s "[e], I thought you had my back on this one..."
    show lothar chuckle
    with dissolve
    l "Ha, I know my disciple won't betray me for some scruffy lion."
    s "Look, don't you look so smug now, if I see you alone next time, you'll be sure your nuts are gonna get fucking cracked."
    show lothar grin
    with dissolve
    l "You seem to really want another kick in the nuts, don't you."
    s "Don't you fucking dare."
    show sebas bored
    e "Hey, you two. Stop with the kick in the nuts thing..."
    l "Ask him to stop squirming like a little girl when I kicked him last time."
    s "..."
    l "Here's the stone, lion."
    "Seb takes the artifact away from Lothar's hand. Examining it with his tools."
    show sebas normal
    s "Look at this, this stone... it's organic."
    e "What does it mean? Isn't organic the opposite of stones?"
    s "Hmm..."
    show lothar chuckle
    l "What? Is there some problem?"
    s "Where did you find it, Lothar?"
    l "The river with moss. You know where it is. The place Ole used to make moss soup."
    e "Moss Soup? Does it ta-"
    s "Yeah alright. We'll need to go there to find out its origin. Seems a little weird to me."
    "You feel a little embarrassed to get cut off by Sebas. He seems a little more irritated than usual, which is more or less justified, but it still doesn't sit well with you..."
    l "Alright then. I'll go with you to see. I know exactly where I found it."
    s "Yeah..."
    s "[e], you wanna tag along?"
    e "Hmm... Ok."
    s "Alrighty, then we'll get ready for tomorrow! I'll see you two here."
    $ quest05_epd = timenow.day + 1
    $ QuestBegin(quest05)
    $ quest05.qProgress(__("Report to Sebas after a day"))
    jump main_kingspawn

label Lothar_Sebas_Kick_Yes:
    e "I think you should take the revenge, Seb. Let's do it."
    show lothar angry
    l "Y-You two morons. I'll... I'll beat you two to the pulp you hear me!"
    "Lothar slowly backs away. Only to see Sebas walks behind him without speaking a single word. He locks the door and flips the sign to Closed, then walks back to look at Lothar again."
    l "D-don't you two... touch me... I'll scream. I'll let everyone know about this."
    show sebas laugh
    s "Scream. No one will hear you now, silly wolf. Accept your fate now."
    l "Let me go!"
    e "It will be over soon."
    s "Yeah. Don't worry, I'll take care of you and your nuts very nicely."
    l "You... betrayed me, disciple."
    s "[e] did the right thing. Now, why don't you come closer."
    "Sebas yanks Lothar towards him, the wolf is squirming undeaneath his legs as the lion barely touches him."
    l "Let me go now, and I might be able to forget this, lion."
    "The lion didn't respond, only practising his kick for a few times while warming up himself..."
    s "You might want to prepare your balls, it's gonna hurt a lot."
    show lothar shocked
    with dissolve
    l "W-what? I... Y-You. Don't you dare..."
    "You take a seat at the corner of the shop, spectating the legendary kick between the lion and the wolf. Sebas is ready now."
    s "Three."
    show sebas:
        linear 0.1 xalign 0.1
        linear 0.1 xalign 0.15
    l "No..."
    s "Two..."
    show sebas:
        linear 0.1 xalign 0.2
        linear 0.2 xalign 0.3
    l "I'll kill you..."
    s "O-"
    show sebas:
        linear 0.1 xalign 0.4
        linear 0.2 xalign 0.5
    show lothar shocked
    l "aaaa-"
    show lothar:
        linear 0.1 xalign 1.0
        linear 0.1 xalign 0.95
        linear 0.05 xalign 1.1
        linear 0.1 xalign 0.95
    "For the first time you hear Lothar's slightly high-pitched scream, it sounds almost like a kid's voice."
    show sebas grin
    s "What, I didn't even kick you yet."
    show sebas:
        linear 0.1 xalign 0.05
    show lothar stare
    with dissolve
    l "You scared me, lion..."
    s "Whatever, three."
    show sebas laugh
    show sebas:
        linear 0.2 xalign 0.1
        linear 0.1 xalign 0.2
    show lothar shocked
    with dissolve
    s "Two."
    show sebas:
        linear 0.1 xalign 0.25
        linear 0.1 xalign 0.3
    s "One."
    show sebas:
        linear 0.1 xalign 0.5
        linear 0.05 xalign 0.9
        linear 0.1 xalign 0.2
        linear 0.05 xalign 0.3
    show lothar shocked
    with dissolve
    show lothar:
        linear 0.1 xalign 1.0
        linear 0.05 xalign 2.0
        linear 2 xalign 1.55
        pause 0.5
        linear 2 xalign 1.05
        pause 0.5
        linear 1 xalign 0.95
    "Sebas shove his foot right between Lothar's legs."
    "You hear a loud thump spread through the shop, followed with Lothar gripping at his own crotch."
    "His anguished face and furrowed brows make it seem much more painful than it is."
    "Lothar's body writhes with agony, he slowly kneel on the ground before slumping over, still holding onto his crotch."
    e "Is this what you two do in your free time? Kicking each other in the balls..."
    show sebas grin
    s "Hey, you wanted to see it too. Also, it's him who kicked me first."
    l "M-mommy... h-help..."
    e "..."
    s "He's fine. His kick is way worse than mine. I just slightly raised my feet."
    "You and Sebas stays for a few minutes while Lothar is groaning on the ground, almost out of air."
    l "My balls... it's... g---one. aaaaa-a..."
    "Sebas kicks the wolf one more time, he doesn't seem to respond, so the lion takes the artifact to his counter. Examining it with his tools."
    show sebas normal
    show sebas:
        linear 0.4 xalign 0.05
    s "[e]. Look at this, this stone... it's organic."
    e "What does it mean? Isn't organic the opposite of stones?"
    s "Well... Where did you found it, wolf?"
    l "S-save.... m-me..."
    e "He said it's from the river, nearby the forest I think?"
    s "Hey, I know where it is, its condition is really exclusively damp."
    s "We might need to go back there, this is really unusual."
    show lothar shocked
    l "J-just give me back the stone, the transaction is cancelled."
    s "No I don't think so. It's on my hand now anyways. So, buddy, wanna go on an expedition with me?"
    e "Uhhh... Alright."
    show lothar bored
    l "Wait, I'm g-going with you then."
    s "Then we'll go tomorrow. Let Lothar lie here a little bit."
    e "Seb, are you going to leave him there?"
    s "I'll ask Ole to take care of his... balls."
    show lothar stare
    l "..."
    e "..."
    s "Ointment, [e]. If you think of dirty things I'll take you to my room."
    e "Uh... What were you thinking..."
    s "What do you think I'm thinking?"
    e "I don't mind though."
    s "Hehe. Maybe after my work, you impatient little guy."
    $ quest05_epd = timenow.day + 1
    $ lothar_disappear_hour = timenow.hour + 4
    $ QuestBegin(quest05)
    $ quest05.qProgress(__("Lothar is taking his rest, I should report to Sebas after a day"))
    jump main_kingspawn

label Lothar_Postal_Training:
    show lothar normal
    with dissolve
    $ QuestBegin(quest04)
    $ quest04.qProgress(__("Defeat the dummy"))
    e "Lothar! I'm ready for the training!"
    l "It seems like you are. Are you ready for some epic battles with the hero?"
    e "Yes, Lothar. I'll show you what I got."
    l "Ha, bring it on... on the practice dummy I had over there."
    e "Wait... I thought our training was us brawling and practicing together?"
    l "Who do you think I am, some kind of low-life who have nothing to do? I have a village to protect."
    e "Hmm..."
    l "Does this look like a tutorial to you? Do I really need to hold your hand to fight?"
    e "No... but you can teach me something useful?"
    show lothar chuckle
    l "Alright, you needy fur lizard."
    l "We have different types of weapons, sword, axe and bow, all different for different usages."
    l "For example, you'd be better off shooting bow at things that fly, because you won't get close to them to use your weapon until they kill you and dump you in the middle of the road."
    e "Got it. So I need a sword, axe and bow with me for special occasions."
    l "Sure. I prefer sword, easy, simple, no mess hanging around."
    l "Back to the main point, battles. The aim of a battle is of course, defeating your opponents. I'm sure you know that."
    e "Hmm, this I know."
    l "Stop cutting off, disciple. You normally have two ways to defeat them, make their physical health go down, or make their arousal go up."
    e "Hmm... what do you mean arousal?"
    l "You know what I mean, something like teasing your opponents, making them flush or something."
    e "But how will this defeat my enemies?"
    l "People in this world are easily aroused, outsider. If you're really charming then the enemies will gravitate towards submitting to you."
    e "Hmmph... what a weird world. Is this how you defeated the goat leader?"
    show lothar stare
    with dissolve
    l "W-what? I'm the hero of lusterfield, a-alright. I don't do dirty tricks."
    "Lothar crosses his arm much harder, you can clearly see him awkwardly trying to shift topic. You can imagine that if it was true, that would be a messed up situation."
    l "Ahem. Anyways, you can try to escape, or if you are tired you can just surrender yourself to the enemy."
    l "It probably leads to bad things though, so I won't advice you to do that."
    e "Yes... They'd steal all my gold."
    l "Ha, not all of them, but if you make them angry you better be very sorry."
    show lothar normal
    with dissolve
    l "Also, Abilities, or spells. Those that requires some amount of magic."
    e "Yes, I know... hmm... Self Heal and Fortify? Is that it?"
    l "You'd probably learn more along your journey anyway, I'm not a magic user so don't think I'll teach you any spells."
    l "However, my practice dummy has a little magic to it, it can simulate fighting a battle with you."
    l "So... I want you to defeat the dummy in the alleyway. If you win, he'll give you a patch."
    e "Hmm... can I not? I already know how to fight."
    l "Yeah... Sure. How about that, you probably don't know how to fight the other way, if you defeat your dummy, I'll show you what I know about flirting."
    e "What about flirting?"
    l "Something like this..."
    "Lothar directs his finger on your chest until it barely touches, your heart suddenly jumps as he slides his finger lower. You shudder at his touch."
    "He seems to be oddly amused by your reaction, looking you up and down."
    l "Look, defeat the dummy, and we'll talk."
    e "O-Okay, Lothar."
    jump Lothar_Normal_Talk

label Lothar_Postal_Finish:
    show lothar normal
    with dissolve
    e "Lothar, I'm back from the practice."
    l "Are you? Let me ask that dummy if you won or lost."
    if dummy.win > 0:
        "Lothar walks into the alleyway, a few seconds later he came back, giggling at your confused look."
        l "He told me you got beaten up pretty badly, didn't you?"
        e "Well I just get closer for the dummy to hit me, I didn't know it'd hurt that much..."
        l "Sure you did. If I was practicing, I won't be letting that dummy touch me anywhere."
        e "That would make it a one-sided fight."
        l "What do you know about fights anyway, [e]. I'm not some beginners at battles, I had been fighting for the majority of my life."
        l "This dummy, it's getting old. It's been here for like what? 19 years? Almost older than you."
        e "Woah... it must take a lot of time to maintain the dummy, almost incredible you hadn't beat it to a pulp of cotton yet."
        show lothar stare
        with dissolve
        l "I would never do it to him."
        e "Yeah, but it's just a dummy."
        l "You don't understand... whatever. You better pay some respect to my dummy if you want to keep training with him."
        e "Yes, I will... is there any history between you and the dummy?"
        "Strangely Lothar didn't cut you off before you finish asking, instead, he looks back into the alleyway, staring at the dummy."
        l "I don't have time for story."
        e "Ok..."
        l "I'll talk to the lizard with your training. It's done now."
        e "What about teaching me flirting?"
        l "Later I will. You will know when the lesson comes."
        e "Okay, thanks. See you Lothar."
        $ quest01.progress[2].status = True
        $ QuestFinish(quest04)
        jump Lothar_Normal_Talk
    else:
        show lothar stare
        with dissolve
        "Lothar walks into the alleyway, a few seconds later he came back with a strange look on his face."
        menu:
            l "Did you just lie to me, [e]."
            "Yes{#lothardummylie}":
                e "I'm sorry Lothar... I thought the dummy wouldn't notice..."
                l "I, the hero of Lusterfield, treated you give hospitality, giving you practice and such, and this is how you return the favour?"
                e "I didn't mean to..."
                l "If you were a lion I would kick you down there so hard you wouldn't need to learn flirting anymore, luckily you aren't."
                e "Hmm... I'll go and fight the dummy now..."
            "No{#lothardummylie}":
                e "I was sure I was fighting the dummy, did he really tell you the truth?"
                l "No, are you really trying to get away lying to the hero of the lusterfield?"
                e "..."
                l "You must really want to get punished by the hero then... Luckily I'm not in a mood to beat up a disciple today, maybe later."
                l "Now, go back to the alleyway before I change my mind."
                e "Yes..."
        jump Lothar_Normal_Talk

label Lothar_Ask_Lusterfield:
    show lothar normal
    with dissolve
    e "Lothar, what do you think about the village?"
    l "Hmm? Is this a stupid question?"
    e "I mean... how are other people in the village doing?"
    l "You should be asking them yourself, goat."
    e "I'm a dragon... but ok."
    l "I guess I can tell you a few insider scoops..."
    l "The lizard, Ole. He's just staying in the shop all the time. Except for hunting with the lion sometimes."
    show lothar stare
    l "You see the lion? Lion is too full of himself, I will not tolerate him making fun of anything related to me. If he gets himself hurt because of his blabbering mouth, that's on him."
    e "Uhh.... I heard Seb talking about something like this?"
    l "Yeah. Tell him next time I'll use my fist... on his face."
    e "Ok..."
    l "Next one, the bat is laidback, I'd bring you to his tavern sometimes if that lizard wouldn't spy on me and you all the time."
    e "What lizard? Wait... Ole is watching?"
    l "He somehow always knows what I am doing. The lizard must be watching me somewhere."
    l "And the bull. That bull makes some nice clothes. I used to teach his kids parrying and sword fighting."
    l "But you know, times changed. Now I come over to his house for dinner once in a while."
    e "Ok... Is there anyone else I need to know?"
    l "Not really. No."
    jump Lothar_Normal_Talk

label Lothar_Ask_Hero:
    show lothar normal
    with dissolve
    e "Hey, Lothar, how did you become the hero of Lusterfield."
    show lothar grin
    l "Ha, little goat. Are you planning to build me a statue?"
    e "Uhh... yes."
    l "Good, good. Ok. Let's begin. Ok. So, uh... Let me take a look."
    show lothar chuckle
    "Lothar takes out a notebook from his left pocket, a few pages fly out of the little crumbling book and he hurried to pick them up one by one, reading them out excitedly."
    l "So... I was always meant to be a hero, since I was a little pup."
    l "My parents were very supportive of me being an adventurer, they taught me hunting and fishing."
    l "I used sword at like 3 years old. Obviously I was very talented at the art of sword fighting. So I defeated my father in an epic sword battle at only 3."
    l "One day, when I was still 3. My mother gave me a paper cone and a long sword. I threw the paper cone away, because I was determined."
    l "At the age of 4-"
    e "Hey, Lothar. Can you summarize a little?"
    l "What do you mean, That story was extremely important for my character development and growth, it will all make sense about my own motivation-"
    l "Ok... whatever. Ole taught you about skipping my dialogues as well didn't he."
    e "What? I didn't ski-"
    l "Anyways, you know how I got the title? I set out on an adventure when I was 23, I brought with myself some water and my old long sword."
    l "I went to the forest for the mysterious potion maker, but I found nothing... So I came back to the village."
    e "Wait... you found nothing? How are you the hero in thi-"
    l "Stop cutting off my story, [e]. I haven't even been halfway through yet."
    "The wolf flips through pages of notes, picking up words from different pages."
    l "So I came back to the village, and I found Lusterfield to be infiltrated by the cult. That goat leader of the cult was ordering his little troops to destroy Lusterfield. And I was hiding in the bush."
    l "I was so furious they dare to show their face here, everyone was fighting for their lives, so I sneaked into the cult outpost. They didn't even notice me from behind."
    e "Were they fighting as well?"
    l "No, the higher-ups were just looking, so I infiltrated their camp and found their goat leader. I don't even remember his name. Tel... or something."
    l "I had the best battle with the goat while everyone was outside. Long story short, I overwhelmed him and knocked him off, he just falls on the ground and rang his bell for help."
    l "The goat keeps ringing and shaking his bell like it could possibly save him from the inevitable death, but I simply yanked it off from his neck and struck him with my long sword."
    e "That's a little crue-"
    show lothar normal
    l "He got what he deserved, [e]."
    l "So when all their goat gangs arrived, I've already escaped from the outpost. Soon after the cult retreated from Lusterfield. They were acting like a bunch of headless chicken without their arrogant leader."
    e "That's why you are the hero of Lusterfield."
    l "Of course. The fight was legendary and it takes an immeasurable amount of courage to face the whole faction alone. Everyone in the village loves me after that."
    e "Wow, that was one hell of a story."
    l "You bet it is. Now you have a role model to learn from, and pray that you can get half as good as me."
    e "...Ok, Lothar."
    jump Lothar_Normal_Talk

label Lothar_Ask_Himself:
    if isNight():
        show lothar drunk blush
        with dissolve
        e "How are you doing, Lothar?"
        l "I had a few beer, these little bottles of shit are fantastic!"
        e "Hmm... are you here very often?"
        l "Yes... Every night and then I come around the inn and mess with the bat. That was some good stuff."
        e "Are you drunk... Lothar? Your face seems pretty red..."
        l "A-ahem. No. I've been drinking for decades now, you think I'm going to suddenly get beaten up by these tiny glasses?"
        e "That's good, Lothar. See you next day then."
        l "Good. Whatever."
    else:
        show lothar normal
        with dissolve
        e "How are you doing, Lothar."
        l "Good. I'm watching over the village, not a lot of activities here today."
        e "Is there anything I can help?"
        l "No. You better keep up with your training."
        e "Ok, Lothar."
    jump Lothar_Normal_Talk

label Lothar_Dialogue_End:
    e "That's all I need, thank you, Lothar."
    if isNight():
        l "Hmm..."
    else:
        if lothar_like < 15:
            l "Ok. I'll continue my hero business then."
        if lothar_like >= 15:
            l "Good, stay safe out there, disciple."
    hide lothar
    if isNight():
        jump main_nocturnaltrunk2
    else:
        jump main_lusterfield01


label Patron1_Dialogue:
    if isNight():
        scene nocturnaltrunk_night
    else:
        scene nocturnaltrunk
    e "Hey..."
    patron "Don't you see we're battling among ourselves?"
    e "Yeah. Arm wrestling, right? Who's winning here."
    patron "I'd say Vult, the cougar. He has been beating him every time we come here."
    e "Aww... You guys seems pretty strong."
    patron "Look we're still battling, and I don't want to miss a single second of this exciting match. I'll see you when we're done."
    e "Alright. Have fun!"
    jump main_nocturnaltrunk2

label Patron2_Dialogue:
    if isNight():
        scene nocturnaltrunk_night
    else:
        scene nocturnaltrunk
    patron "You see, the stars in the skies are actually monsters, and the sun is probably the most fierce one, that's why my eyes hurt when I look at him."
    patron "I think the sun is a wolf... maybe... a dragon. Like a sun dragon monster. You get what I mean. And the moon. He's an elephant... I think, small elephant."
    patron2 "Yeah... monsters in the skies. You know what I see? I can see there's another huge monster out there though..."
    patron "Hmm a monster? where?"
    patron2 "not in the skies, underneath the table..."
    patron "What? How? I don't see no creatures there..."
    e "'I think I should leave these two alone...'"
    jump main_nocturnaltrunk2

label Patron3_Dialogue:
    if isNight():
        scene nocturnaltrunk_night
    else:
        scene nocturnaltrunk
    e "Hello...?"
    patron "...He-... {p} wha-... he...hnnngh... so handsome. {p} au-uuugh... hnnnnngh......."
    patron "h-hmmmph.... hnnnn... o-ohhhhhhh... {p} mine... he... h-hahaha... {p} hmmmm... asssssss..."
    e "'He's so drunk I don't think I can talk to him now... But I wonder who he is talking about...'"
    jump main_nocturnaltrunk2

label Patron4_Dialogue:
    e "Hey there..."
    "You approach a pair of patrons standing on the edge, they raise their tankards and take a sip before turning their attention to you."
    e "How's it going?"
    if pirkka_location == "nocturnalupper":


        patron2 "The bard's good, I tell ye."
        patron "Aye, he's got a voice that could charm a dragon. And his skills with that lute of his, simply mesmerizing."
        patron2 "I've seen my fair share of bards, but this one's got a unique flair. There's something about his performances that draws you in, makes you forget all your worries."
        e "He's a talented songsinger indeed."
        patron "Remember that one tale about the hero? I wonder if it'd actually happen, the way he tells the stories almost feels as if I was there."
        patron2 "Are you serious, of course no. That's nothing but a mere ghost tale to scare kids."
        patron2 "But still, credit's where credit's due, there's been more than a crowd paid to be here, just to listen to his songs and dance."
        patron "I've heard he's a travelling one, gonna miss him while he's gone."
        patron2 "Cane's gonna pay him huge to stay, I tell ye. There's no way he'll be gone anytime soon considering the patrons he's brought."
        patron "Yeah right..."
    else:
        patron "Good, server. Cane just redecorated this floor, finally feels like we're breathing now."
        patron2 "Yea, I do get why he stopped opening the second floor since after that lad was gone, but the tavern's been too busy for casual dwellers like us."
        e "Ah, is this floor any different?"
        patron "Well, incase you're still getting used to here, we've been one of the most loyal regulars here, so Cane lets us go up with a proper discount."
        patron "We just have to get food and drinks by ourselves, and we're more than capable to do that. Plus, this place is so much more quiet and cozy than downstairs."
        patron2 "He's right, server. Sorry to say but you'd better appeal to the newcomers of the tavern. Not saying I won't get my hand on you if ye want though."
        "You blush profusely."
        patron2 "Eh, that wasn't flirting, just saying you've gotta have to stay here for a while, else Cane's gonna close this floor down again."
    jump main_nocturnaltrunk_upper
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
