
label Jog_Dialogue:
    if isNight():
        scene lusterfield_range_night
    else:
        scene lusterfield_range
    show jog normal
    with dissolve
    if quest33.status == True and quest33.completed_date < timenow.day - 1:
        if jog_accuse and piercingblow not in learnedabilities:
            jump Jog_Return_Bandit_End
    if jog_tut == 1:
        e "Hello! Jog?"
        j "Hmm."
        e "Are you jog?"
        j "Y-yes. I recognised your ass."
        j "Lothar's disciple, courier, outsider?"
        e "Yes, my name is [e]."
        j "Heh... I've got my eyes on you... and your ass... you get what I'm saying?"
        e "Hmm?"
        j "Just don't break anything here, Lot's order."
        e "Oh! Thank you so much, Jog."
        $ jog_tut += 1
    else:
        e "Hey, Jog!"
        j "If it isn't the courier with that cheeks clapping! Hey, [e]."
    jump Jog_Normal_Talk

label Jog_Normal_Talk:

    menu:
        j "What's up, Courier."
        "Learn his opinion on the vote" if quest37.status == 2 and quest37.start_date + rahim_vote_duration  >= timenow.day and quest40.status == False:
            jump Jog_Voting_Opinion
        "Report to Jog about the plums" if quest33.status == 4:
            jump Jog_Return_Bandit_Meet_Quest
        "Pick up the delivery" if is_client("Jog"):
            $ client_name = "Jog"
            call Courier_Pickup_Dialogues from _call_Courier_Pickup_Dialogues_7
        "Deliver the goods" if is_recipient("Jog"):
            $ recipient_name = "Jog"
            call Courier_Delivery_Dialogues from _call_Courier_Delivery_Dialogues_7
        "Ask about the Gnolls" if LookForItem("Ruttish Flute", inventory):
            jump Jog_Ask_About_Gnolls
        "Ask about Lusterfield{#JogAAL}":
            jump Jog_Ask_Lusterfield

        "Report after following Sebas" if quest40.status == 4 or quest40.status == 3:
            jump Jog_Vote_Report
        "Ask about his opinion on the vote" if quest37.status == True and timenow.day < quest37.completed_date + 14:
            jump Jog_Voting_Result
        "Ask about Training from Lothar" if quest13.status == 4 or quest13.status == 2:
            stop music fadeout 1.0
            jump Jog_Lothar_Training
        "Ask about Training Ole mentioned" if not isNight() and (quest17.status == 5 or quest17.status == 6) and day_training_aj < timenow.day:
            stop music fadeout 1.0
            jump Jog_Ole_Training_Scene
        "Ask about the team":
            e "What about the other dudes?"
            menu:
                j "Amble, and Lothar?"
                "Ask about Lothar":
                    jump Jog_Ask_Lothar
                "Ask about Amble":

                    jump Jog_Ask_Amble
        "What's going on?" if quest33.status == False and ((quest17.status == True and quest17.completed_date < timenow.day - 2) or(quest13.status == True and quest13.completed_date < timenow.day - 2)) and not isNight():

            stop music fadeout 1.0
            jump Jog_Bandit_Meet_Quest
        "Ask about the Plum Thief" if (quest33.status != False and quest33.status != True) or quest33.discovered == True:
            stop music fadeout 1.0
            jump Jog_Bandit_Meet_Quest_Inquire
        "Ask about your outfit" if pc.armor["Clothes"] != None and pc.armor["Pants"] != None and quest09.status != False and quest09.status != True:
            if pc.armor["Clothes"].img == "Adventurer Armor" and pc.armor["Pants"].img == "Adventurer Leggings":
                jump Jog_Amble_Outfit_01
            elif pc.armor["Clothes"].img == "Tavern Cloth" and pc.armor["Pants"].img == "Tavern Chaps":
                jump Jog_Amble_Outfit_02
            elif pc.armor["Clothes"].img == "Flowy Robe" and pc.armor["Pants"].img == "Flowy Wrap":
                jump Jog_Amble_Outfit_03
            else:
                "As you are about to ask, you realise you are not putting on the right clothes to judge..."
                jump Jog_Normal_Talk
        "Ask How is he doing":
            jump Jog_Ask_How_Doing
        "That's all for now":
            jump Jog_Dialogue_End
    jump Jog_Normal_Talk
label Jog_Lothar_Training:
    j "Courier, are you sure you can handle this?"
    j "Lot told us that you can't even beat the training dummy."
    e "That is not true."
    j "Now why would Lot lie about that?"
    "You don't know what to say..."
    j "It doesn't matter. Because I actually have a mission from him and I figure this is the perfect training opportunity for you."
    e "What is it?"
    j "We're going to infiltrate into the nucleus of the goat tribe."
    e "Why?"
    if lothar_knows:
        j "I've heard everything from Lot. You did good Courier."
        j "But you are too trusting. We have to check if the goats are lying. I won't be surprised if they are."
    elif lothar_argue:
        j "He said you don't have the balls to go face the goats."
        j "So this will be your training. Don't worry. I'll be there to watch over your ass, figuratively and maybe literally too."
    else:
        j "He said that you got nothing even though you've successfully gained access into their tribe."
        j "That won't do. But we're going to fix that."
    j "Either way, we have to find out what the goats are really up to."
    scene mossy_freshwater
    show jog normal
    e "So..."











    e "What do you think they're up to?"
    j "I don't know, based on their recent activity it seems they're searching for something."
    j "Not like I'd be interested unless they're taking their pants off in the middle of the forest."
    e "Have they?"
    j "Maybe they have. That's the perks of being a scout, you get to see all sorts of thing."
    e "Huh, what does a scout do?"
    j "Watching out for danger, being the first to explore a new area, and all."
    j "Sometimes I do see people pulling pants off, and that's why I like what I'm doing."
    e "Wouldn't you rather be the one that's... pulling their pants off?"
    j "What? Your brain is filled with lewd stuff much more than I do, and I won't tolerate being the second horniest person here."
    e "I mean, do you enjoy watching people from afar more than engaging with people?"
    j "I don't see anything wrong with that. If it's what I'm good at then it's what it is."
    e "Fair enough."
    j "Plus, if I needed any sex I'd come to you first since you're all up for this, aren't you."
    e "M-maybe?"
    "Jog chuckles slightly."
    j "Now, I've scouted ahead and determined that our biggest obstacles is the two guards at the tribe entrance."
    j "How do you suggest we deal with them?"
    e "Uhmm... what do you think?"
    j "I can see there's two ways we can approach."
    j "First way, I see there's a rock wall near the outer wall of the goat tribe. We can hike the rock and leap over the walls."
    j "Or, I can fire an arrow and distract the two guards away from the entrance. Then, we'll sneak in."
    j "Either way, we'll have to be fast."
    menu:
        j "What do you think?"
        "Distract the guards":
            $ jog_train = 1
            e "I'll choose... Distraction?"
            j "Alright, then."
            e "Hmm..."
            e "Jog, how did you pick up archery?"
            j "It... well... I never was a good survivor."
            j "I was left all alone, when I was very very young. Much like a little kid."
            j "And, I have to tell you this, I never liked being in the village. Most of the time I go to the forest and have fun."
            j "I picked up the bow pretty early on, not an exciting story really. I just practised outside with Amble."
            j "But I didn't live with him until much later on."
            e "Did you practice a lot?"
            j "Of course. Speaking of, it was Amble who carved and set up the archery range in town."
            j "We hang out there when we're in the village."
            j "But sometimes, the bear and I are up to something else."
            j "Let's just say on those times, I'd be handling something a lot more heftier than my bow."
            e "...heftier?"
            j "If I explain it it wouldn't be as much fun, [e]."
        "Sneak through with agility":
            $ jog_train = 2
            e "I'll choose... Sneaking?"
            j "Alright, then."
            e "So... Jog, how did you get designated as the scout?"
            j "The role came naturally to me."
            j "I was born... well. not as strong as the others."
            j "But, you know. It has its benefits, despite those other's pesky jeering and all."
            j "I can escape people's detection quite easily and I can fit into small crooks others can't."
            e "That sounds useful."
            "Jog looks over and cracks a smile."
            j "Well, you have no idea how many perks you'll get by just staying hidden."
            j "Let's just say Lusterfield lives up to the Lust in its name."
            j "Stuff sometimes get left behind after sex."
            j "Speaking of, a free tip."
            j "That lizard friend of yours at the shop packs a big one. You might want to prepare yourself before you proceed further."
            "Jog winks mischievously at you."
            j "I may or may not know from experience. Haha."

    "Soon... you and Jog arrive at the Goat Tribe."
    scene kechioeren
    with dissolve
    show jog normal
    if jog_train == 1:
        "You hide behind a bush."
        j "Be prepared. I'll shoot an arrow."
        j "Once the goats go investigating after it, we'll leg it into the tribe."
        j "Keep your body low to the ground."
        "You nod."
    else:
        "You and Jog stop at the rock wall."
        j "You should be able to find purchases on the crevices."
        j "When you reach a certain height, just jump over the wall."
        j "There are bushes on the other side to cushion your fall."
        "Jog stares at your butt."
        j "You have some padding back there to help with your landing too. They are more than just pleasing to the eyes."
    pause 1
    "The plan carries on smoothly. You and Jog find your way to the window of the chieftain's hut."
    scene kechioeren_conference
    with dissolve
    "You hear conversation drifting out from inside."
    k "..."
    k "This is so hard. Furk, this is impossible."
    "You hear Kari groans."
    f "You just need to power it through like we usually do."
    k "It's too tight. It won't go through."
    f "How about we oil them a little to loosen things up?"
    k "You're asking for too much. There's no way it'll fit."
    f "We've done it before, so why won't it work now?"
    k "Things have changed. That has gotten bigger."
    "You blush hearing the conversation. You look over at Jog."
    "Jog was looking at you with a dirty grin."
    j "{size=30} Well, I was not expecting that.{/size}"
    e "{size=30} What should we do?{/size}"
    pause 1
    "The two in the hut begins to talk again."
    show kari masked at r1
    k "Furkan, you are not going to get Lusterfield to agree to this."
    "Kari sighs."
    show furkan normal at l1
    f "...There must be some way."
    k "Their defenses are too tight."
    k "You have already tried a truce. How did that go? Things are not loosening up any time soon."
    k "You are demanding too much of them. Do you think it'll fit their agenda?"
    "You hear Furkan lets out a big sigh."
    k "Furkan, you have to see the bigger picture."
    "Things start to make sense again."
    "Beside you, Jog rolls his eyes."
    j "{size=30} lame.{/size}"
    f "Kari, yes. The bigger picture. The center of our conflict is the caravan attack."
    f "The stories didn't add up. We should look into it. It could ease the tension with Lusterfield if we find something."
    "Your eyes shine. This appears to be valuable information."
    "Jog appears to agree with you because you feel his hand closes around your wrist."
    "There's a warning in the village."
    goatguard "There are signs of intruders. Search every corner!"
    j "{size=30}Crap! Time to disappear.{/size}"
    scene kechioeren02
    with dissolve
    show jog normal
    "Jog pulls you along and you tries your best to keep up with the sprinting hyena. It's not that easy."
    "It amazes you how Jog manages to move at such a high speed without making much noise."
    scene kechioeren
    with dissolve
    show jog normal
    "You are not as graceful as Jog is but you try your best."
    "However, your heavy steps mean that you are unable to lose the trail of goat guards fast closing up on you two."
    j "Damn! We can't keep running!"
    j "Change of plans!"
    scene woodlandoutpost
    with dissolve
    show jog normal
    "Jog leads you into a bush."
    "You look around and see nothing but foliage."
    "You are sure that this is not a good hiding spot. The foliage is not dense enough to hide both of you."
    "Just as you are going to ask Jog what's going on, Jog pulls you along and pushes you into a nook hidden behind the bush."
    "You wedge into the nook. Jog squeezes in after you."
    "The nook is just enough for two."
    "Jog leans into you and arranges the bush to shield the nook from outside view."
    "With Jog blocking the entrance, you are basically stuck in place."
    "You have your back to the wall and Jog has his back to you."
    j "{size=30} Stay still.{/size}"
    "You want to heed Jog's advice but you find it hard to do because one part of you refuses to stay still."
    "As Jog backed into the space earlier, his butt landed right before your crotch."
    "Your heated breath from the running heats up the confined space."
    "You don't know where to put your hands but somehow they land on Jog's narrow waist."
    "The fabric of Jog's briefs is extremely thin and you can feel the suppleness of his ass readily."
    "The close proximity and the confined space makes you feel heady."
    "Your cock rises to attention. The tip brushes along the crack of Jog's ass."
    "You hope that Jog doesn't notice it."
    "At that moment, Jog turns around and rewards you with a naughty lift of his brow."
    "You take his advice and freeze. Your cock is erect but at least it is standing still."
    "At that moment, there is a rustling coming from outside."
    "Jog leans deeper into you."
    "His back lay into your body."
    "The warmth from his skin spread through your pecs and stomach."
    "Your cock tinkles as the warmth travels through your body."
    "Your boner pitches a tent through your loincloth."
    "Even to you, your cock feels hot. You wonder how Jog is handling it considering he has your cock wedged between his buns."
    "The rustling slowly moves away. You relax a little."
    "Once you let your guard down, your cock leaks some precum."
    "You can feel your underwear getting wet. The spot where your tip brushes against your underwear become sticky with precum."
    "You try your best to move your head. You can see the wet spot where your dick has made a stain."
    "The sight of your wet underwear excites you. You feel your cock pulses and more precum makes their way out of your penis."
    "The wet spot on your underwear gets larger."
    "Jog's ass is poised right before your dick."
    "As your dick releases more precum, the liquid seeps through the front of your underwear and stains the back of Jog's briefs."
    "You feel like saying something but fate appears to play a cruel trick on you."
    goatguard "Maybe they're here."
    "The goats announce their presence."
    "Jog wiggles further into the crook."
    "As he moves, Jog's ass tenses."
    "His butt cheeks pinch your boner."
    "A jolt of electricity powers through you."
    "You feel a moan escaping your throat. You know you have to swallow it out lest you risk exposure."
    "Your cock charges with tension. You feel like your cock is about to poke through your underwear."
    "Perhaps even through Jog's briefs and into his ready hole..."
    "Perhaps sensing the effect it's having on you, Jog tightens his ass a few more times."
    "The effect this has on you is electric."
    "Jog's soft cheeks massage your boner at quick intervals."
    "You are hit at all the right places and you can feel your blood rushing to your boner."
    "You grit your teeth and is approaching ejaculation."
    "At the cusp of release, Jog suddenly moves away."
    "You pull him back."
    e "{size=30} Wait! Aren't you worried about being caught?{/size}"
    j "Getting caught?"
    "Jog raises his brow and looks at the front of your wet underwear."
    "Under his stare, your cock twitches at the attention."
    "It is yearning for release."
    "Jog grins wickedly."
    j "Maybe you should be the one worried about getting caught."
    "Jog opens his arms and continues in a normal voice."
    j "The goats are already gone."
    e "When?"
    j "When that sexy moan escaped your mouth."
    "Jog chuckles as your cheeks flush red. You thought you had suppressed that moan but apparently you didn't."
    j "Thank you for showing me many things today. Overall you did help me complete the mission. I'll report that to Lothar."
    "Jog touches the back of the briefs where it's stained by your precum."
    "He rubs it between his fingers and grins at you."
    j "Nice to know what you're sporting."
    j "The things earlier are just a teaser. Maybe in the future, I'll show you more what I can do with my ass."
    "Jogs chuckles and disappears into the woods as your face flames with embarrassment."
    if quest13.status == 2:
        $ quest13.status = 3
    if quest13.status == 4:
        $ quest13.status = 5

    jump main_woodland_outpost
label Arthur_Bandit_Meet_Quest:



    if arthur_2ndChoice == "Good" or arthur_2ndChoice == "Bad":
        e "M-master, I was looking for the plum trees, would you point me where it is?"
    else:
        e "Arty, I was looking for the plum trees, would you point me where it is?"
    ar "Plum... you must be doing chores for that cheeky Jog, ain't you pup?"
    e "Y-yeah, Amble told me you gave him some apples instead, is there no plum left in the entire farm?"
    ar "Look, someone stole these juicy little bastards, they were right there in the grove of harvest."
    ar "You'd expect them to sneak over to my place late at night like a proper thief but no, that one took my harvests in the broad daylight."
    e "Did no one ever see them?"
    ar "Listen, pup, these are thieves, they come in pattern. They knew where our scarecrows patrolled and they sneaked up on the plums like a proper pest."
    ar "They've planted the seed for a while, they knew when we sleep, when we work, when we're away from our lands."
    e "Then, maybe you can catch these thieves if you just catch them out of guard, right?"
    ar "No, I need to tend to my crops, not catching plum thieves like a grumpy old hound."
    "Arthur pauses for a second."
    ar "What I'm saying is, these scumbags are sneaky, but if a pup wishes to help with pest extermination just like what you did with the landsharks, there's no one to stop you."
    e "Do I... get a reward for this?"
    ar "You already had one with another fella, pup."
    "Arthur points in the general direction somewhere towards Lusterfield."
    ar "If you want to help, I know something that might deem useful to you. I counted 3 occasions where my plums went missing."
    ar "I checked the grove garden every eight in the morning, the first day I saw them missing was, 2pm. The second, well- four. And the third, it was at around 12."
    e "Do they come at a specific time?"
    ar "They came in a pattern, was what I was saying. Perhaps if you wait in the farmland around that time you'd catch the thief red-handed."
    ar "It's all predictions, pup. Once you've been working on the farm for a couple of decades. You've sort of seen it all."
    "Arthur sighs, looking over the endless field."
    ar "Welp, time to work."
    ar "Good luck looking for the thief, pup, but stay inside the farm, that way I can actually protect you from any threats."
    if arthur_2ndChoice == "Good" or arthur_2ndChoice == "Bad":
        e "Thanks, M-master."
    else:
        e "Thanks, Arty."
    $ quest33.status = 3
    $ quest33.qComp(__("Catch the thief in the Grove"))
    jump main_backyard_barn
label Arthur_Bandit_Meet_Quest_Inquire:
    if arthur_2ndChoice == "Good" or arthur_2ndChoice == "Bad":
        e "Master, may I ask again what I should do to catch the thief?"
    else:
        e "Arty, what should I do to catch the thief again?"
    ar "It's easy, when it's morning, walk around right back there in the grove of harvest where the plums are at."
    ar "If they're greedy for more of the juicy plums, you'll see them there."
    e "Oh! Thank you again!"
    ar "Good, good pup."
    jump main_backyard_barn

label Jog_Bandit_Meet_Quest:
    e "Jog, is there something wrong?"
    j "What do you mean, something on my face? Amble broke the bucket again?"
    e "No, I mean generally, but what happened to the bucket...?"
    j "Ah, go ask Amb if you wanna know. But I do have something else on my hand at the moment."
    a "Hey, puny friend. Good to see you here."
    show jog normal at r1 with move
    show amble normal at l2
    show amble normal at l1 with move
    "A familiar red coloured bear walks inadvertently, with a few similarly coloured apples on his hands."
    j "Amb, you've got those precious red plums?"
    a "Oh, about that. I saw only a few rotten ones in the trees, but Arty gave me these healthy looking ones instead-"
    j "You idiot, these are apples! Not plums. Did that old dog tell you it's even more tastier than the real ones?"
    a "Wait, were you following me? How did you know..."
    j "You oaf."
    "The snarky hyena grins at the dumbfounded Amble."
    j "And I asked for a basket, what happened?"
    a "The last time I checked they were fine, but today the plums all disappeared, and I could only see some red juice stains on the grass."
    e "Did someone steal from the farm? I didn't see anyone doing that in broad daylight."
    j "And what I see, is someone getting hungry for these juicy babies. I'll miss them."
    "You notice Jog grabbing the apples from Amble, before munching down onto one of the red fruits."
    e "You aren't going to find out who took the plums?"
    j "No, Amble and I already know who did it."
    a "W-wait, I don't know who stole your plums."
    e "Me neither."
    "Jog takes another bite out of the apple, making loud crunch noises after another."
    j "Well, if you want to find out what's out there, be my guest, go ask Arthur about the area and follow that trail or whatever Amble was talking about."
    j "Amble and I have been out here scouting and fixing roads for a while, but you should still be cautious."
    j "If it's safe for you to walk on it, it's safer for them to walk as well."
    a "Puny friend, I should go with you for extra safety."
    "You feel warmer upon hearing Amble, but it soon dissipates as Jog yanks on the bear's hand hard to drag Amble towards him."
    j "You stay! I'm not done with your abs."
    j "Sorry, [e]. Amble's too busy, he can't go with you."
    e "It's ok, I can handle myself."
    "Amble gives you an awkward smile as he sits on the hay piles."
    j "But, anyway, if you can get me some of those plums back. I'll teach you how to perform a piercing blow."
    e "Is... that it?"
    "Jog gives you a side glance, and then chuckles."
    j "Since when did you learn to talk like this?"
    j "Alright, Amble will give you 400 gold as well, enough for your greedy ass?"
    menu:
        "Accept Jog's Quest":
            e "I guess that's enough for my greedy ass."
            j "Good, now get your ass out there and bring me back the plums before I get a hold of it."
        "Maybe Later":
            e "Maybe I'll check it out later."
            j "Plums don't wait, but I'll be eating my apples until your lazy ass comes back."
            jump main_lusterfield_range
    "The two wave you goodbye, before talking among themselves."
    "Unable to hear their conversation, you take your leave swiftly."
    $ QuestBegin(quest33)
    jump main_lusterfield_range
label Jog_Bandit_Meet_Quest_Inquire:

    e "Jog, I think I will look for your plums, what should I do again?"
    j "Good, you can't let these juicy devils go to waste in somebody else's belly, much like cum."
    "Jog gives you an evil grin and licks his lip intently."
    j "Just go to the old farmer's place, he'll tell you about the problem, stop the thief, and perhaps get me back the plums, if they're not already in someone else's belly."
    e "Is there anything I need to be careful of?"
    "The hyena stares at you for a moment, before taking another bite out of his apple."
    j "Just don't wander off the farm, you know. Stranger danger."
    j "Someone might take your money, and probably get your ass eaten, figuratively."
    e "A-alright."
    if quest33.status == False:
        $ QuestBegin(quest33)
    jump main_lusterfield_range
label Jog_Return_Bandit_Meet_Quest:
    e "About the plums..."
    "Jog glances at you, his face immediately turns serious."
    j "You've caught the thief?"
    if not bandit_sneak and not isBandit:
        e "Yeah."
        e "It was a rat, he said he is a bandit or something."
        j "What happened to him?"
        if bandit_has_plum:
            e "Uh... I let him take the plums and leave."
            e "But he's not coming back, which's the most important thing, right?"
            j "Maybe, why did he come here?"
            e "He, uh. uh. H-he thought he was safe, because of hyena."
            "Jog raises his brows, you're certain his glare isn't a kind one."
            j "Something about me?"
            e "Yeah, he said something along the line of the hyena will keep him safe."
        else:
            e "Well, I've got the plums, right here."
            j "W-well, and I was starting to get used to the taste of these apples."
            e "I beat him up pretty badly. Doesn't seem like he's coming back."
            e "I don't think so either. He begged to keep the plums though. I didn't give him back."
            j "Good, now I can finally enjoy these plums without these pesky varmints getting in the way."
            "Jog sounds disinterested. Almost void of any emotion despite getting the plums back."
            e "You know about him?"
            j "..."
            e "He talked about a hyena before, I thought it was talking ab-."
        j "What do you think?"
        e "Ah?"
        jump Jog_Bandit_Accuse_End
    else:
        e "Well, I followed him outside the farm."
        j "..."
        j "Did I not tell you to not go outside."
        e "Ye-yes, but I wanted to see who he was."
        j "You don't really listen, do you?"
        "Jog sighs."
        if jog_train == 2:
            j "I knew you were reckless as hell when you chose to distract those goats back then."
        j "What did you find out, then."
        e "He was a rat and I followed him to their hideout."
        e "I saw a shark, I think he is probably from the bandits."
        e "And... I got caught there."
        if isBandit:
            e "I didn't know what to do, so I just lied, saying I was a recruit, just to get out."
            j "O-ok."
            j "You knew about the red food thing?"
            e "I didn't know, I just guessed, I guess."
            j "S-so what. You're a bandit now?"
            e "They think I am, but not really."
            j "Are you joking right now? Did that shark just let you go like that?"
            e "Y-yeah."
            j "...Boring."
            j "Did they say something... about a hyena?"
            e "Yeah."
        elif sharkbandit.win > 0:
            e "I just won against him, he said he wouldn't come again."
            j "And you trust him?"
            menu:
                "I trust the shark":
                    e "Yeah, I do."
                    j "You'd trust a bandit?"
                    e "I trust a bandit that's just been beaten up."
                "I don't trust him":
                    e "Not really, but I'll have to take his word for now."
            j "If you piss him off you'll have a whole band of bandits storming Lusterfield, you know."
            e "...Uh. I didn't think that part through."
            e "He did mention a hyena in Lusterfield, though."
        else:

            e "And I limped back to Lusterfield."
            j "You can't be too careless."
            j "If you piss him off you'll have a whole band of bandits storming Lusterfield, you know."
            e "...Uh. I didn't think that part through."
            e "He did mention a hyena in Lusterfield, though."
            j "And hyena, huh."
    j "What do you think?"
    e "Ah?"
    jump Jog_Bandit_Ask_End

label Jog_Bandit_Ask_End:
    $ jog_accuse = False
    menu:
        j "He was talking about me, what do you think?"
        "The bandit has mistaken":
            e "I think he was talking about another hyena? Maybe he recognised a hyena from another place."
            j "N-no I'm pretty sure he's talking about me."
            j "Now, am I the one that helped those guys?"
        "Maybe Jog was one of them":
            e "I was just thinking, maybe you... knew him?"
            j "Do you think I helped those guys take advantage of the village?"
    e "Of course not, I look fondly of you, Jog."
    e "You're not like them at all."
    "Jog unclenches his fist, he stares at you."
    j "Why do you think that?"
    e "Well, I think you're pretty witty and funny, and you treat your friends really well."
    e "That, I don't see in any of them."
    j "..."
    "Jog looks away, his face filled with bewilderment."
    j "Huh."
    j "Did Sebas not warn you about me?"
    e "I don't think that matters at all, really."
    e "I can see it with my own eyes, and you're a good friend."
    j "..."
    j "A-alright."
    j "W-Who taught you to talk with butter in your mouth, was it Arthur?"
    e "No, not really, I really mean it well, Jog."
    "The hyena ponders for a minute."
    j "...S-shit."
    j "You know, I had been thinking of a way to know what you would think about me for a long time, and I didn't once expect that answer at all."
    j "Usually I wouldn't ask you to get the plums for me, if not for seeing how you'd react."
    e "Well you could've just asked me directly."
    j "Yeah, but that wouldn't be fun."
    "Jog chuckles."
    j "I know them, the bandits, I had been one of them a long time ago."
    j "I really thought I'd be a bandit for the rest of my life, I thought it became a part of me."
    j "But I got kicked out, for not being fierce enough."
    j "The fun part is, after I returned to Lusterfield, Sebas took me in, and they too kicked me out, because of something I didn't do."
    j "Because, there was no other thief in the house other than me."
    j "It was fun, I loved that."
    "It doesn't look like Jog is having fun saying it, and you stare at him with concern."
    j "Amble was the only one stupid enough to let me sleep in his place. he said I was good at scouting, hiding and warning people of monsters."
    j "He's the oaf that doesn't really see the worst in people."
    j "Perhaps you're an oaf too."
    e "I am?"
    j "Ha, you're a sexy oaf, I'll give you that. But Amble's got that cake I can eat for all day."
    "He smirks."
    j "And Lot, for a village hero he's another kind of oaf that protects his friends at all cost, regardless of right and wrong."
    j "You're really lucky to be his disciple, you know that."
    j "And- if I was like Ole, I'd be scolding you for a whole year for not listing to me and sneaking out to the bandits."
    e "He would. But he'd mean it well."
    j "I know. He is a good lizard overall."
    j "It's not like he did me anything wrong. Sometimes I was just paranoid."
    j "I hate that feeling, but it keeps coming back and I never know what to do."
    j "It was there all the time when I saw you, like when I see everyone else."
    j "And that feeling, it makes me do something I'd regret, which makes me just much more scared."
    j "I don't ever want to feel like that again."
    e "I wouldn't let that happen, Jog."
    j "..."
    "The hyena looks up for the first time in a while."
    j "I guess I'll trust you, for whatever's worth."
    j "But... yeah. I'm gonna stop with the downer talk."
    pause 2
    j "Well, what's the thing I promised I'd reward you again?"
    e "You promised to teach me a skill?"
    j "Oh."
    $ QuestFinish(quest33)
    jump Jog_Teach_Critical_Skill

label Jog_Bandit_Accuse_End:
    $ jog_accuse = False
    menu:
        j "He was talking about me, what do you think?"
        "The bandit has mistaken":
            e "I think he was talking about another hyena? Mayb-"
            j "Oh? What a conincidence, well I'm letting you know now, he is talking about me."
            j "He knew me."
            j "Now, am I the one that helped them?"
        "Maybe Jog was one of them":
            e "I was just thinking, maybe you... knew him?"
            j "Got it, now do you think I helped them get advantage of the village?"
    e "Of course not, I look fondl-"
    "Jog looks impatient, he clenches his fist tightly."
    j "You all are the same, what did Sebas tell you exactly back then, huh? That I was a backstabbing liar and thief?"
    e "Can I-"
    j "That I was born a thief and always a thief and I'm nothing but troubles always?"
    j "Why don't you say what you've been thinking the first second you see me for the first time?"
    "You pause."
    j "Now I see why they like you so much. His favourite new roommate, ha."
    e "Jog, I don't think that was fair-."
    j "Fair? Fair like everytime time something goes wrong and it's always my problem?"
    j "Or talking like I was always scheming, taking advantage of his wealth like a hemoworm sucking blood out of its host."
    e "Jog, I was just talking about what the rat thief said, nothing else."
    "You try to calm Jog down a little, but he is still staring right into you."
    j "Am I a rat too?"
    e "No, Jog. You're not."
    j "..."
    "He freezes, suddenly."
    e "You're not a thief, you're not a bandit, you're my friend, Jog."
    e "And I, really see you as one, no matter what those bandits said."
    "The hyena takes a few seconds to calm himself down, he is avoiding your concerned gaze."
    e "I just trust you, the first time I saw you and Amble in the Tavern."
    e "You are a good folk."
    j "..."
    "He was almost at the verge of tears, a few gurgles and coughs away from a full on cry."
    e "Whatever happened in the past, doesn't mean anything to who you are right now."
    e "And I believe in you, Jog."
    "Jog stares at you, bewildered. His eyes are watery, but it looks like he is holding back."
    e "I think Amble and Lot believe in you too."
    j "..."
    j "W-would you please buzz off?"
    "You don't dare to look at Jog's face, he hides himself pretty far away from you as well."
    j "We'll talk later."
    "By his own accord, he probably was once a part of the bandit. But it mustn't be easy to be accused of something he didn't do."
    "But you eventually oblige, leaving him alone to his own thoughts."
    "You see Amble walking straight towards him, he doesn't even greet you normally as he does."
    "You can only hope some time later he will return to his normal jovial self."
    $ QuestFinish(quest33)
    jump main_lusterfield_range
label Jog_Return_Bandit_End:
    j "Hey."
    "Jog walks towards you, with a sluggish pace."
    e "Hello, Jog."
    "You two both doesn't talk, resorting into a contest of awkward gaze."
    j "Last time, I wasn't myself."
    j "Thanks for not leaving me, well, until I tell you so, but."
    j "Uh."
    j "Thanks for your words."
    j "Amble talked with me after, I wasn't being a good friend to you, putting you through all that."
    e "It really wasn't your fault, Jog."
    e "We all have moments of outbursts like that sometimes."
    j "It just felt weird what you were doing, I didn't expect that."
    "He pauses for a moment again, giving you a slight grin."
    j "I cried really uglily there, weren't I?"
    j "That wasn't hot at all. On a matter of fact, pretty boner-killing."
    j "But, yeah. I promised you a reward, so let's get this over with."
    jump Jog_Teach_Critical_Skill
label Jog_Teach_Critical_Skill:
    j "This is what I call, Piercing Blow."
    j "It's not about blowing your enemy's cock, by the way."
    "Jog points at his squinting eyes."
    j "Here, you just take your time for a moment to look at their weakspot."
    j "And when you attack, you guarantee to hit them really hard."
    j "One thing is that, when you look at them closely, you expose your vulnerable self to their attacks."
    e "Can I just, not look at them as closely?"
    j "Then you can't find their weakspots, you oaf."
    j "So, knowing when to use them is a huge skill you need to learn to become a master."
    "You nod."
    j "That's it, it's not much but I suppose you'll learn that really quickly."
    j "And I'm lazy so I gotta take my leave now, here's the gold I promised. See you later, [e]."
    e "See you."
    msg "You learned the skill 'Piercing Blow'."
    $ pc.exp += 250
    msg "You received 250 experience points."
    $ timenow.addTime(0, 0, 10)
    $ learnedabilities.append(piercingblow)
    jump main_lusterfield_range
label Jog_Wuldon_Quest:
    "You find Jog tapping his foot impatiently."
    show jog normal with dissolve
    j "Took you long enough."
    show jog normal at l1 with move
    show amble normal at r1 with dissolve
    a "Ignore him, you're fine. We do need to talk to you about something though."
    "You can't really think of anything they might want from you – maybe something happened with the landsharks?"
    e "Did something bad happen?"
    j "Yes!"
    a "No."
    "They both look at each other for a moment."
    ja "Maybe."
    e "...alright, well, what's the maybe bad thing that's happened?"
    j "Well, we know you've been over in werewolf territory recently."
    "You never told him that, but sure."
    j "And we found one over in the farmlands."
    e "Was he attacking people?!"
    "This time it's Amble's time to step in."
    a "No... not as far as we can tell, but it's got the farmers on edge."
    a "Nothing like a big bad wolf right outside your home to scare you senseless."
    "That... doesn't really sound like any of the regular werewolves you know. They'd have attacked the farmers immediately."
    e "Do you know what they're doing out there?"
    "Jog shifts uncomfortably."
    j "That's what bothers me. Nobody can figure it out."
    j "He somehow always knows when I'm watching, and leaves before I can see what he's up to."
    a "And whenever somebody musters up the courage to walk up and talk to him, he gets up and disappears without a word."
    "...That's even weirder. A quiet werewolf?"
    "A thought begins scratching at your brain."
    e "What would this werewolf happen to look like?"
    "Jog's posture returns to confidence, something much more natural for him."
    j "Oh, that's easy. He's hot as hell."
    "Goddamnit."
    j "Okay, fine, you're no fun. He's a massive, dark blue werewolf with a big belly and rippling muscles."
    "Yeah, that's pretty much what you expected."
    j "He's also got this weird curved sword we think he's been using to cut grass in the area?"
    j "Any idea who that might be?"
    e "Yeah. That's a guy called Wuldon."
    e "He's just gathering medicine for a very sick friend of his."
    a "Oh. Good. We were pretty sure he meant no harm, but..."
    a "We still need to talk to him. The farmers aren't going to take kindly to letting him stick around."
    "Wuldon's probably not going to react very well to either of these two telling him to stop getting medicine for Vurro."
    "Maybe it'd work if you asked?"
    e "Don't worry about it, I'll go talk to him. Thanks for telling me about this."
    a "No problem, and thanks for taking care of it."
    j "Make sure to ask him how he could always tell where I was!"
    e "Got it, got it. I'll talk to you guys later."
    "Well. You've got a werewolf to go convince."
    jump main_lusterfield_range

label Jog_Ole_Training_Scene:
    show jog normal with dissolve
    e "Jog, I'm here for training."
    "Jog hops down from his haybale."
    j "Perfect timing. Let's go."
    e "Where are we going?"
    j "The bushes near the forest will be fine."
    e "What are we going to do?"
    j "You'll find out."
    e "Do I need to prepare anything?"
    j "Just bring your handsome self there."
    j "And enough with the 20 questions. I'll meet you there."
    scene black with dissolve
    "You are about to suggest that you two can travel there together, but as you turn the corner, you see he's already disappeared."
    "You arrive at the forest. The place is peaceful and serene."
    scene woodlandoutpost with dissolve
    show jog normal with dissolve
    "Jog is nowhere to be found."
    e "Jog? Are you there?"
    "The only answer you get is the chirping of birds."
    "Just as you wonder if this is a prank, you feel a pinch on your butt."
    j "That was your punishment for making me wait so long."
    "Jog appears out of the shadows."
    "He is carrying a basket of what appears to be different kinds of berries."
    e "What do you have there, Jog?"
    e "Are we going berry-picking?"
    j "Are we children frolicking through the woods? No."
    j "I'm going to teach you a skill vital to being a scout."
    e "What is it?"
    j "The art of camouflage."
    e "That sounds cool."
    j "And highly useful."
    e "But how are the berries involved?"
    "Jog shakes the basket."
    j "You wouldn't be carrying paint with you out in the wilds, would you?"
    e "No."
    j "Bingo. But these berries can be found everywhere. As long as you know your colors, you can basically mix up any hue you need for the perfect camouflage."
    e "That sounds neat."
    j "Alright. Now, strip."
    "You are surprised by the demand."
    e "Strip? Why?"
    j "Cause berries stain, and I'm not going have you blame me for ruining your clothes later."
    j "Plus, this makes the lesson a lot more fun."
    "Jog winks naughtily at you."
    j "Stop wasting time. Get those clothes off."
    j "You're not shy, are you?"
    e "No..."
    "You strip down to your loincloth."
    "Even though Jog is also just standing there in his briefs, you can't help but feel a little self-conscious."
    "Jog whistles."
    j "Nice bod."
    e "Jog, focus."
    j "I am."
    "He says this as he focuses his eyes on your exposed body."
    e "Jog, be serious."
    j "Alright. Loosen up a little... Or I might need to help you."
    j "Anyway, look at this."
    "Jog grabs a handful of blue and golden berries."
    "He mulches them in his paw. To your surprise, the berries slowly turn a green color that matches the color of the leaves around you."
    e "That's amazing."
    "You are genuinely in awe."
    j "You can get any color you want as long as you know how to combine them."
    "Jog adds a few more golden berries to the mix, and the color morphs to a brighter emerald shade."
    j "With some shading, you can create the illusion of shadows."
    j "Plus, you can use more than just berries. Everything around you can be used as a material."
    "To demonstrate, Jog picks up some soil and mashes it with some red berries."
    "The bright redness of the berries becomes more coppery. You then realize what he is trying to mimic."
    e "Is that blood?"
    j "Correct. Or at least, it's fake blood."
    j "Useful when trying to lead your enemies down a false trail."
    j "Now, onto the fun part."
    call scene_jogskill from _call_scene_jogskill
    $ pc.lust = 0
    $ learnedabilities.append(camouflage)
    if quest17.status == 5:
        $ quest17.status = 7
    if quest17.status == 6:
        $ quest17.status = 8
    jump main_woodland_outpost
label Jog_Ask_How_Doing:
    e "How are you doing, Jog?"
    j "Just practicing some archery."
    j "I'm the scout of the team."
    j "So the team relies on me to get some shots in before we get close and personal with the enemies."
    "Then, Jog looks around and lowers his voice to a whisper."
    j "Also if you hear anyone around town whispering about a thief fitting my profile."
    j "I can swear that it's not me."
    "Jog winks at you."
    e "Ehm... Ok."
    "You have no idea how to make of it."
    jump Jog_Normal_Talk
label Jog_Ask_Amble:
    e "What do you think about Amble?"
    j "That block of wood?"
    j "I guess he's alright."
    j "Every team must have a meatshield and there you have it."
    e "I don't think he's just a meatshield to you... right?"
    j "Not the sharpest nail in the toolbox, if you know what I mean."
    j "But hey. With a body like that, why would you need brain?"
    "Jog nudges you."
    j "Plus, the view's nice, isn't it?"
    jump Jog_Normal_Talk
label Jog_Ask_Lothar:
    e "What's Lothar to you, Jog?"
    j "Well, as you must know by now, Lot is the village hero."
    j "He's also a very GOOD leader!"
    "There is a rare trace of sincerity in Jog's tone."
    e "Ehm..."
    j "You might not have the best impression of Lot."
    j "I know how he might come across sometimes."
    j "But he has everyone's best interest at heart."
    j "Just don't ever tell him that I said these things or I'll never hear the end of it."
    e "Ok, I won't tell Lothar..."
    jump Jog_Normal_Talk
label Jog_Ask_Lusterfield:
    e "How is the life in Lusterfield?"
    j "The place's not bad."
    j "Born and raised here with Amble."
    j "There are some interesting characters around here."
    j "For example, the lizard at the shop."
    j "I don't get why people would go around giving away medicine for free."
    j "But I ain't complaining."
    j "That means the team has more budget for other things."
    j "And the lion, Sebasti-... Sebas."
    j "Let's just say we have some history."
    e "Hmm? What histor-"
    j "The tavern barkeep is fine."
    j "At least he doesn't kick us out when Amble is making chaos in his tavern."
    j "Rahim makes Lot's armor."
    j "Lots of respect for the man."
    j "But wouldn't you like to see what he's packing?"
    e "Uhm... I didn't notice."
    "Jog chuckles."
    jump Jog_Normal_Talk
label Jog_Dialogue_End:
    e "That's it, thank you so much for bearing with me, Jog."
    j "Yeah, well. 'Stay sharp, my disciple', heh."
    jump main_lusterfield_range
label Jog_Amble_Outfit_01:
    $ opinions_Outfit[0] += 1
    show amble normal at l1
    show jog normal at r1
    "You find Jog and Amble together."
    "Both of them spot you. Jog nods to acknowledge your presence. Amble waves and greets you."
    a "Hey. It's Lot's follower. What are you doing here today and what is it that you're wearing?"
    "you felt two pair of eyes scanning your body."
    e "This is an adventurer's outfit made by Rahim. I'm here to get your opinions on it."
    j "master Rahim made that for you? It looks like you're not just Lot's favorite."
    e "This is just a job. So what do you think of the outfit?"
    a "I think it's great."
    j "I agree."
    a "It shows off all your assets."
    j "Nice assets you're sporting, by the way."
    a "The straps can be used in first-aid emergency healing."
    j "Or to strap someone down, if you catch my drift."
    a "Could do without the undershirt though."
    j "100 percent."
    e "I will relay your feedback to rahim."
    "Jog and Amble nod. You look at them and something comes to mind."
    e "While we're on this topic, can I ask a question?"
    a "Go ahead."
    e "Why are you dressed so minimally as adventurers?"
    "The two seems surprised by your questions."
    a "Of course, it's for intimidation. Normally I would have won half the battle when the enemy sees a giant bulk of muscles stomping towards them."
    "Amble flexes his muscles."
    j "It's for agility and flexibility. Less of a chance to get hooked on stuff. Plus, it cuts down the time to get to the fun time of any battle."
    "Jog grins at you invitingly."
    j "You should try it and see where it gets you."
    "you swallows nervously."
    e "Alright. Thanks for the feedback."
    jump main_lusterfield_range
label Jog_Amble_Outfit_03:
    $ opinions_Outfit[6] += 1
    show amble normal at l1
    show jog normal at r1
    "You find Jog and Amble together."
    "Both of them spot you. Jog nods to acknowledge your presence. Amble waves and greets you."
    a "That is a cute outfit but definitely not suitable for combat. You'll most likely trip on yourself."
    j "Another ingenius way to submit yourself to the opponent."
    a "But it's cute for wearing around town. It makes me want to wrap you up and take you home."
    j "Yes. You're tied up with a knot. Makes me want to open you up like a present."
    e "Hmm... Alright- alright... I get it. Thank you!"
    jump main_lusterfield_range
label Jog_Amble_Outfit_02:
    $ opinions_Outfit[3] += 1
    show amble normal at l1
    show jog normal at r1
    "Once you walk up to the shooting range, both Jog and Amble come up to you."
    e "Hey, guys. This..."
    "Before you can start explaining, they have started to examine your outfit."
    "Their pats around your thighs and crotch turn you on slightly."
    "You wish you could hide the boner you're starting to have, but the outfit makes it impossible."
    e "Guys, stop."
    e "Guys... stop."
    "Amble obliges but not Jog. At least, it's better than nothing."
    "You try to calm down but it's hard with Jog's fingers trailing along your new outfit."
    "You are determined to finish your quest, so you turn your attention to Amble."
    e "What do you like about this new outfit? You two seem to be more into it than the actual adventurer's armor."
    a "Because it's quite reminiscent of our attire, other than the strange thing that's wrapped around your legs that is."
    a "Did Lothar put you up to this?"
    "You couldn't help but pause at the implication of that question."
    "Are Amble and Jog only in their underwear on Lothar's order?"
    "You find that to be quite hot."
    "Suddenly, a series of popping sound draws you out of your reverie."
    j "Hey. The pants are meant to be removed. You only need to pull the buttons on the belt."
    a "Really? That is a great design. Now, you really look like a part of the team."
    "You can feel the chaps sliding down as Jog's nimble fingers undo the buttons expertly."
    "You quickly slaps Jog's hand away and grab the chaps before they fully fall off, leaving you there only in your briefs."
    e "Guys. Stop joking. That's not how the outfit is meant to be used."
    "Although at the back of your mind, you wonder if you were wrong and they were right."
    "After all, the outfit was meant for the tavern."
    "Either way, you need to escape before things get even more out of hand."
    "You snap the buttons back on and turn away from the shooting range."
    j "Hey, we're not done examining the outfit yet!"
    a "That's right."
    jump main_lusterfield_range

label Amble_Dialogue:
    if isNight():
        scene lusterfield_range
    else:
        scene lusterfield_range
    show amble normal
    with dissolve
    if isNaked():

        e "Hello, Amble."
        a "Hey, [e]."
        a "You're... dressing like us now, only without the jock part."
    else:
        if amble_tut == 1:
            a "Hey, [e]... Haven't seen you around here before..."
            e "I was just walking around the village and I discovered you two!"
            a "We don't mind. Come more often... now that you're one of us."
            e "Am I? I didn't even get to know you and jog that much since the last time..."
            a "We're always here, if we're not already out hunting in the afternoon."
            a "Treat yourself like your home, this is where we usually practice."
            e "Didn't Lothar have the training dummy?"
            a "It's his. The dummies here never move, so there's one less thing to worry about."
            e "Oh... Thanks, Amble."
            $ amble_tut += 1
        else:
            e "Hello, Amble."
            a "Hey, [e]."
    jump Amble_Normal_Talk
label Amble_Normal_Talk:
    menu:
        a "[e]? What's on your mind?"
        "Ask about Pirkka's Prose" if quest35.status == 3:
            jump Amble_Prose_Ask
        "Learn his opinion on the vote" if quest37.status == 2 and quest37.start_date + rahim_vote_duration  >= timenow.day and quest38.status == False:
            jump Amble_Voting_Opinion
        "Report about the material for the bridge" if quest38.status == 2 and (LookForItemNumber("Wooden Log", inventory) >= 20 and LookForItemNumber("Masonry Mix", inventory) >= 3):
            jump Amble_Voting_Cement
        "Ask about the required material for the bridge" if quest38.status == 2 and not (LookForItemNumber("Wooden Log", inventory) >= 20 and LookForItemNumber("Masonry Mix", inventory) >= 3):
            jump Amble_Voting_Ask_Cement
        "Ask about his opinion on the vote" if quest37.status == True and timenow.day < quest37.completed_date + 14:
            jump Amble_Voting_Result
        "Pick up the delivery" if is_client("Amble"):
            $ client_name = "Amble"
            call Courier_Pickup_Dialogues from _call_Courier_Pickup_Dialogues_8
        "Deliver the goods" if is_recipient("Amble"):
            $ recipient_name = "Amble"
            call Courier_Delivery_Dialogues from _call_Courier_Delivery_Dialogues_8
        "Ask about Lusterfield{#AmbleAAL}":
            jump Amble_Ask_Lusterfield
        "Ask for Training" if quest13.status != False and quest13.status < 4 and quest13.status != True:
            stop music fadeout 1.0
            jump Amble_Lothar_Training
        "Ask about the training Ole mentioned" if quest17.status == 2:
            jump Amble_Ole_Training
        "Ask about the training Ole mentioned" if quest17.status == 4:
            stop music fadeout 1.0
            jump Amble_Ole_Training_Lothar
        "Ask about patrol in the farm" if quest13.status == True and timenow.day > 12 and taskAvailable(task03, quest13):
            jump Amble_Ask_Patrol_Task
        "Report about the patrol in the farm" if task03.status == 2:
            jump Amble_Report_Patrol_Task
        "Ask to follow Amble's Patrol" if quest29.status == False and landshark.win >= 3 and quest17.status == True and quest17.completed_date + 3 <timenow.day and timenow.day > 35:
            jump Amble_Patrol_Quest
        "Follow Amble's Patrol" if quest29.status == 2:
            jump Amble_Patrol_Farm
        "Ask about Training Ole mentioned" if not isNight() and (quest17.status == 5 or quest17.status == 7) and day_training_aj < timenow.day:
            jump Amble_Ole_Training_Scene
        "Ask about the team":
            e "What about the other dudes?"
            menu:
                a "My team?"
                "Ask about Lothar":
                    jump Amble_Ask_Lothar
                "Ask about Jog":

                    jump Amble_Ask_Jog
        "Ask how he is doing":
            jump Amble_Ask_How_Doing
        "That's all for now":
            jump Amble_Dialogue_End
label Amble_Ole_Training:
    e "Amble, do you have some time?"
    a "Sure."
    e "You and Jog have been travelling much longer than I am."
    a "Correct."
    e "So that you means you have more battle experience."
    a "Yes."
    e "In that case, Amble, do you have any battle skills that you can teach me?"
    a "Hmm... I think so."
    e "That's great."
    e "When do you think you can teach me?"
    a "How about now, my puny friend?"
    e "Okay."
    "A voice travels from the other end of the archery field."
    j "Hold on a second!"
    "You and Amble turn around to see Jog tapping his feet and staring at you."
    j "Are you here on Lot's behest?"
    e "Not really. But it's for the courier training..."
    "Jog interrupts you."
    j "Sorry, friend. Can't help you there. Our training in Lusterfield is supervised by Lot."
    j "We're not doing any extra training without going through him first."
    e "But..."
    j "We don't make the rules."
    "You turn to Amble for help."
    "Amble shrugs."
    a "What Jog says is right. Need to notify Lot first."
    "You sigh."
    e "Alright..."

    $ quest17.status = 3
    $ quest17.qComp(__("Ask Lothar for Permission"))
    jump main_lusterfield_range
label Amble_Ole_Training_Lothar:
    e "Alright. I got the permission from Lothar. He says the training is a go."
    a "Awesome. I knew he would agree. He's such a nice person."
    j "Color me surprised. I was a bit 50-50 on the result. I guess he does like you."
    "You are not so sure about that. The person Lothar likes is probably himself."
    e "So, back to the skill training."
    a "Yes. This is fun. [e], I'll teach you how to properly crush the enemy in battle."
    e "Sounds good."
    a "But I'll have to get things prepared first. Give me some time?"
    e "Of course."
    a "See you back here later, [e]."
    "Amble gets into the idea of the training faster than you anticipate. He trundles off to make his preparation."
    "After Amble leaves, Jog eyes you from his perch."
    e "So Jog, will you teach me some new skills too?"
    "Jog ponders."
    j "Eh, why not? Like the blockhead said, this will be fun."
    "Jog's eyes glow with a mischievous glint."
    j "Similarly, I too need to prepare for this lesson. I assure you this lesson will be fun for us both."
    e "...Okay."
    "Jog rustles away."
    $ day_training_aj = timenow.day
    $ quest17.status = 5
    $ quest10.qComp(__("Wait a day and report to Jog and Amble"))
    jump main_lusterfield_range
label Amble_Lothar_Training:
    a "A training? Are you sure you can handle it, puny thing?"
    a "We heard from Lot that you can barely handle yourself against a slime."
    e "That is not true. I've beaten many slimes on my journey."
    a "That's not what he said."
    "You really don't know what to say."
    "Amble sizes you up and down."
    a "Regardless, he did say that you are to go on a training with me."
    a "It'll prove that whether you have the strength to be part of the team or not."
    e "Alright."
    a "Come with me and be prepared for a grueling training session."
    "You anticipate a strenuous physical exercise as you follow Amble to the Sparkling Lagoon."
    scene ancienttree
    with dissolve
    show amble normal
    "You two stop at the forest near the lagoon."
    a "Alright, puny dragon. Start chopping."
    "With you looking on in shock, Amble grabs the axe off his back and starts hacking at a giant tree."
    "Amble pauses and looks at you with confusion."
    a "Of course. This is how I normally train my strength. Lot wants you to get stronger like him, right?"
    a "This is the most effective way."
    "Amble points to an axe on the ground."
    a "That's another one of my axes. You can use it."
    "Amble resumes his work. You pick up the axe and ponder your situation."
    "There is a big tree and a small tree near you."
    "The big tree is about the size of the tree Amble is chopping. It dwarfs you easily. Chopping this down will require a lot of energy."
    "The small tree is about twice your size. The trunk is thinner so it should be easier to fell this tree compared to the other one."
    menu:
        "Which will you chop?"
        "The big tree":
            $ amble_train = 1
            "Since Amble chose the big tree, you follow his example."
            "You raise the axe and swing. The axe cut into the bark and you arms buzz from impact."
            "This job is harder than it looks."
            a "You swing with your shoulders, not your arms."
            "Amble walks over."
            a "Let me show you."
            "Amble put his large hands over yours."
            "He encircles you from behind."
            "You feel a fuzzy warmth from the close contact."
            "Amble corrects your stance and the second swing you made feel smoother."
            a "Better."
            e "Thank you, Amble."
            "Amble nods, smiles and heads back to his work, leaving you with yours."
        "The small tree":
            $ amble_train = 2
            "You are too inexperienced of a logger to go for the big tree."
            "Plus, one has to work smart on top of working hard."
            "You pick up the axe and ready to chop down the smaller tree."
            "Suddenly, there is a roar."
            a "Wait!"
            "You halt. You turn and see Amble trundle over. He looks rather mad."
            a "What are you doing?"
            e "Chopping... tree?"
            a "Not this one!"
            e "Why?"
            a "This one still needs the time to grow."
            e "Does it make a difference?"
            a "Of course!"
            a "Nature is venerable. We have to respect it for the life that it has provided us."
            a "If we cut down all the saplings, will we even have enough logs to harvest in the future?"
            "You nod. You do not expect to see this philosophical side of Amble."
            e "I understand now. Sorry, Amble."
            a "It's alright. I shouldn't have roared at you. You are new at this too."
    "The two of you fall into a comfortable rhythm. Eventually, there's quite a sizeable pile of logs on the ground."
    scene black
    pause 1
    scene ancienttree
    show amble normal with dissolve
    a "Phew. That was quite a workout."
    "You nod. The training was unexpected but you did get to know more of Amble."
    a "Courier, that was not bad. Keep this up and I'm sure you'll be stronger soon."
    a "You'll never be as strong as him but it'll still be an improvement."
    e "... Thanks?"
    a "Nature is always there to provide. These logs will help Lusterfield and you get a good workout in the process."
    a "However, courier, understand that sometimes Nature can be dangerous too."
    e "What do you mean?"
    a "Dad was a logger too. He had come across many strange things in the forest."
    a "He used to warn us of treekins in the forest. People who are fiercely protective of nature."
    a "However, other than the goats who worship the big glowing tree, I've never seen any creature like that."
    a "Or perhaps Dad was talking about the goats?"
    a "Anyway, I'm sure it's nothing to worry about."
    "Amble scratches his head and smiles."
    "You ponder this legend."
    "Amble puts down the axe and walks to the nearby lagoon."
    scene sparklinglagoon
    with dissolve
    show amble normal
    a "Puny courier, I'm sure you are all sweaty from the training. We should wash ourselves in this lagoon."
    "You think that it is a good idea too. You follow Amble to the lagoon."
    e "Amble, wait a moment."
    "You look at the crystal clear water."
    e "Amble, is this safe?"
    "Amble guffaws."
    a "Of course, it is. I've done this many times."
    a "You are just like Jog. There is no hidden danger everywhere."
    a "Well, at least I'm sure there's no danger here."
    e "Alright."
    "You strip down to your loincloth."
    "Tired of waiting for you, Amble scoops up the water and splashes you."
    a "Come on. The water is really relaxing."
    "The water drips from your fur."
    e "Why did you do that for?"
    a "To get you to stop wasting time."
    "You pout as you wade into the water."
    "Amble is right. As the water laps around your body, you can feel the exertion of the day being washed away."
    "You ease into a spot right beside Amble."
    e "This is nice."
    a "Yea..."
    "Amble lets out a satisfied moans as he leans his head back and closes his eyes."
    "You try to relax but something catches your attention from the corner of your eyes."
    "Amble's briefs have turned semi-transparent in the water."
    "You turn your hardest not to look."
    "You notice that Amble's eyes are still closed. Your eyes subconsciously wander south."
    "Even in a limp state, Amble's cock is huge."
    "You cannot help but wonder how large it'll be when it's fully erect."
    "The cock is so large that you can see the details of the veins clearly."
    "Some of the veins pulse as the blood pumps through them."
    "Suddenly, the water doesn't feel as relaxing anymore."
    "Amble's cock curves downward."
    "The foreskin is pulled back because Amble's cock is so large."
    "A bit of the pinkish crown is peeking through near the tip."
    "As the water flows, Amble's cock and balls jostle slightly inside his briefs."
    "You wonder how he manage to fit all of them in."
    "The briefs look like it's already stretching to breaking point from your perspective."
    "Your mind wanders and you can't help but ponders if you could fit Amble's ample digit in your mouth... or even your hole."
    "You swallow nervously. You feel the front of your loincloth rising."
    "This is not a good situation."
    "You need to calm down before Amble wakes up and catches you ogling him."
    "You scoop up the lagoon water and splash it on your face."
    "You whips your head around to clear your mind."
    "The water splashes on Amble beside you."
    "The giant bear groans and opens his eyes."
    a "That was too comfortable. Did I fall asleep again?"
    "Amble turns to smile at you."
    a "Sorry for that. I hope you found this soak in the lagoon as relaxing as I do."
    "Your mouth feels dry and you could only nod."
    "Amble chuckles."
    a "Good. Shall we go back?"
    "Without waiting for your answer, Amble stands up and water flows off his body."
    "The surface of the water ripples violently, which is probably a good thing since it means that Amble won't see your waking boner."
    "You clear your throat and force out."
    e "Amble, perhaps you can go back on your own first. I feel like soaking here a little longer."
    a "Alright, puny friend. I'll tell Lot that you've finished your training with me. See you back in town."
    "Amble climbs out of the lagoon."
    "He waves at you."
    "You cover your boner with one hand and wave back at him with another."
    "Amble shakes off the water from his body."
    "All you can see is his cock swinging around in his briefs."
    "Out of the water, the fabric of the briefs stuck even closer to Amble's cock and balls."
    "It makes the outlines even clearer."
    "Amble turns around, rewarding with your another amazing sight."
    "The back of the briefs hugs Amble's perky ass."
    "As Amble leaves, his asscheeks spring with each of his steps."
    "After Amble disappear from view, you relax fully into the water. However, there's one part of you that refuses to calm down."
    $ timenow.hour += 4
    if quest13.status == 2:
        $ quest13.status = 4
    if quest13.status == 3:
        $ quest13.status = 5
    jump main_sparkling_lagoon
label Amble_Ole_Training_Scene:
    a "Puny friend, here you are!"
    e "Amble, were you looking for me?"
    a "Oh yes. Aren't we going to get to the skill training?"
    e "Yea, but I wasn't expecting you to be so into it."
    a "Of course. We have to do everything with everything we've got!"
    a "Come on now."
    "Amble turns and waves for you to follow."
    e "Amble, wait!"
    "Amble stops and turns to you."
    a "What's wrong?"
    e "Where are we going? Aren't we doing the training here?"
    "You gesture at the archery training field."
    a "Silly friend. Of course not. We're going to somewhere else for this special training. Come with me."
    "Amble walks away."
    "He waves, greets and nods at everyone along the way. Dwarfed by his size, you follow silently behind Amble."
    "You cannot help but admire the view before you."
    "Amble's large ass swings and bounces with each of the bear's steps."
    "You are reminded of what Jog said. Having a good view was a good perk when training with Amble."
    "You have to agree."
    scene black with dissolve
    "You two continues the journey in silence. You openly admiring Amble's assets from behind while Amble humming joyfully to himself."
    "Finally, you arrive at the logging site."
    scene ancienttree with dissolve
    show amble normal with dissolve
    a "Here we are!"
    "You look around."
    "It is the same place as you trained with Amble last time."
    e "Why are we here?"
    a "Because the lesson is related to the trees, silly."
    "He looks at you as if that cannot be more obvious."
    e "How can battle skill be related to trees?"
    a "You can learn a lot from nature. I'll show you. But before that..."
    if pc.armor["Pants"] != None and pc.armor["Pants"].img == "Adventurer Leggings":
        a "Let me just do this..."
        "Amble strides up to you and starts to remove your armor."
        "The plates and shoulder pieces fall to the ground with heavy thuds."
        "Flustered, you try to stop Amble but he's much too strong."
        e "Am-Amble, what are you doing?"
        a "I'm preparing you for the training of course!"
        "Amble explains as he continues to undress you."
        "What kind of training would require you to be naked?"
        "An answer pops up in your mind and your cheeks redden."
        e "Am-Amble, I don't mind that kind of training but..."
        "Your fingers undo the straps of your armor as you say that."
        "Eventually, you find yourself standing in only your briefs."
        "Just as you think Amble is going to strip you naked, he stops."
        a "Alright. We're ready!"
        "Amble straightens himself."
        "At that moment, you can't help but ask."
        e "Amble, why am I only in my briefs?"
        a "This is an adventurer's training so of course, you have to look the part."
        a "That's what Jog told me."
        a "Why do you think I go around dressed the way I am?"
        "Amble flashes you a bright grin like that's the most logical thing in the world."
        "You do not know how to argue with that logic. It makes both no sense and absolute sense."
        e "But why take off the other parts of the armor?"
    else:
        "Amble rummages at the back of his briefs and soon pulls something out."
        a "This is for you."
        "Amble opens his paw and you see what he is offering you."
        "It is the briefs from Rahim's adventurer outfit. Just the briefs."
        e "Erm... Why?"
        "Amble looks as confused as you are."
        e "I mean... What am I supposed to do with this?"
        a "Put it on of course! What else can you do with it"
        e "Again... Why?"
        a "This is an adventurer's training so of course, you have to look the part."
        a "That's what Jog told me."
        a "Why do you think I go around dressed the way I am?"
        "Amble flashes you a bright grin like that's the most logical thing in the world."
        "You do not know how to argue with that logic. It makes both no sense and absolute sense."
        a "Hurry up."
        "Amble tosses you the briefs."
        a "Also when I asked Rahim to loan this to me, I told him about that it's for a special training I'm doing with you."
        a "Rahim told me that we better not tear it. Not sure what he means by that, but you better be careful, puny friend."
        "You are not quite sure what to feel from that information."
        "In any case, the briefs are still warm from being wedged in Amble's clothes."
        "As you put the briefs on, you find that to be quite sexy."
        e "Why only the briefs?"
    a "If you have any iron parts on during the training, they'll cut into you. You'll hurt."
    a "We don't want that."
    e "Okay..."
    "That makes sense..."
    a "Come. It's time for training."
    "Dressed in only your briefs, you follow Amble to a big tree."
    a "Puny friend, how do you cut down this tree with just one swing?"
    "Amble asks as he taps the sturdy tree beside him."
    e "I... I have no idea."
    a "Puny friend, you're lucky cause I'm going to teach you that."
    "Really?"
    "Honestly, that sounds quite amazing."
    a "Course. Why else are we here?"
    "Amble stands before the tree and examines it for a few seconds."
    "Then, he swings his axe hard into the trunk. The axe cuts about halfway through the trunk."
    "However, the tree remains unmoved."
    e "Amble, you sure..."
    "Amble wiggles his axe that is lodged in the tree. The canopy rustles as the axe opens up the wound."
    "The tree starts to sway before your eyes."
    "Soon, Amble has opened up a large gap. With a chip in its large trunk, the tree loses its foundation and begins to tip."
    a "Hng!"
    "Amble pulls his axe out with a grunt."
    "The tree keels over from its own weight. As it lands, the forest ground trembles."
    "You are gobsmacked."
    a "How about that."
    e "That... that's amazing."
    e "How did you do it, Amble?"
    a "I'll teach you."
    a "This is something I've picked up from being a lumberjack."
    a "There's a core to every tree and once it is weakened, it'll be easier for you to make it fall."
    a "The same can be applied to enemies."
    a "Only need to find the core."
    e "How does one do that?"
    a "It's easy. Our core is around our belly button."
    e "Really?"
    "You find that rather hard to believe."
    a "I'll show you."
    "Amble takes quick steps towards you. Before you can react, he hits you as soft as he can around your lower stomach."
    "It doesn't hurt that much but you are assaulted by a sense of vertigo."
    e "Ahh..."
    "The world spins and there is a fleeting moment where you feel like falling."
    "It's like the wind has been knocked out of you."
    "You land on the floor with your back. There is a slight buzz and when you look up, the sunlight are shining through the canopy of the forest."
    e "Oof."
    call scene_ambleskill from _call_scene_ambleskill
    $ pc.lust = 0
    a "Puny friend, that is wild. If this is what I get from teaching you new skills, feel free to come find me whenever you want."
    e "Hmm... Hmm... Yes."
    "With the taste of Amble's cum on your lips and the scent of his musk in your mind, you slowly drift off."
    if quest17.status == 5:
        $ quest17.status = 6
    if quest17.status == 7:
        $ quest17.status = 8
    scene black with dissolve
    pause 5
    scene ancienttree with dissolve
    "That... was an amazing training."
    $ learnedabilities.append(corestrike)
    $ timenow.hour+= 4
    jump main_ancient_tree
label Amble_Ask_Lusterfield:
    e "How is the life in Lusterfield?"
    a "The town is wonderful. Many fine people here. And I know most of them, so you've come to the right people to ask about this!"
    a "Was raised a logger. So I've helped built most of the buildings in the town. Picked up the craft from dad."
    "Amble's eyes dim a bit at the mention of his father but then he perks up again."
    e "How is the Tavern?"
    a "Cane at the tavern is more ancient than you might expect. He's already keeping the tavern running when I was a mere cub."
    a "Rahim is amazing. He packs a mean punch. No one else in town can beat me in an arm wrestle but Rahim. But I've learned a lot from him."
    a "It's doubly amazing that he can refine his strength into something as delicate as tailoring."
    a "Can you imagine me at a sewing table? Haha."
    e "What about the shop?"
    a "Ole is very kind. You wouldn't think so but accidents happen more often than you think during logging."
    "Large falling woods and a giant axe? Recipe for disaster."
    a "Ole has patched me up many times."
    a "Used to be quite close to Sebas."
    a "But ever since Lot formed a group with Jog and me, He would give us the evil eyes from time to time."
    "Amble frowns."
    a "Jog told me that I was imagining it. Perhaps he's right."
    jump Amble_Normal_Talk
label Amble_Ask_How_Doing:
    e "How are you doing, Amble?"
    a "Not doing much."
    a "Just hanging out with Jog and working on the anvil."
    a "Ironing out the kinks in the armor and sharpening the blade."
    a "But honestly, I'm just waiting for night to come so the real fun starts at the tavern."
    jump Amble_Normal_Talk
label Amble_Ask_Lothar:
    e "How about Lothar?"
    a "He's my role model and he should be yours too."
    a "Jog and I weren't in the best shape when Lot found us."
    a "He was the one who helped us get clean clothes, food. After what went down with the goats."
    a "We owed him a lot."
    e "Why do you like him so much?"
    a "He is a simple man, if you treat him well, you'll be treated the same way."
    a "And I love simple stuff. Life doesn't have to be all complicated if you'd just take it easy."
    a "That's how I see things."
    e "Was it Lothar's idea that you two are taking care of the road?"
    a "After that incident with the goat's wagon, we thought we needed a better road protection."
    a "Plus, Lot got a lot of gold from his reputation in the village, he just gifted them to us to help killing monsters."
    a "We just wanted to keep the area around Lusterfield safe for travellers like you."
    jump Amble_Normal_Talk
label Amble_Ask_Jog:
    a "I like the puny little thing."
    a "We're complete opposites but that's probably why we work so good together."
    a "Lot keeps telling me that I have the tendency to charge into the battle. It's a bad habit I have to kick. Have no idea how."
    a "Therefore. I'm always caught in a pickle. Jog has saved my ass so many times now with his great scouting and archery skills."
    a "I'm glad to know that he has my back."
    a "I have his too."
    jump Amble_Normal_Talk
label Amble_Patrol_Quest:
    $ QuestBegin(quest29)
    $ quest29.qProgress(__("Go Patrol with Amble"))
    e "Hey, Amble, I've been wondering about something for a while."
    e "When I helped you with the landsharks, you mentioned patrolling the farms regularly."
    "Amble is looking at you quizzically."
    a "Yeah, I patrol the farms regularly. Is everything alright, puny friend?"
    e "Well, nobody else seems to visit the farmland much... I was wondering if you knew why that was?"
    a "Ah, I see now."
    "A goofy smile spreads across his face."
    a "Well, the farmland is pretty peaceful. It's one of the few places the goats haven't attacked, and there aren't any tribes in that direction, as far as we know."
    a "So, Lot sees it as beneath him."
    "You look over to your right, where Jog is lazing about."
    e "And Jog?"
    j "What am I going to do, sneak around and listen to the wheat? A scout is useful against groups of people, not the enemies of farms."
    "Amble's smile is warm and genuine, like a warm hug."
    a "So that's why it falls to me to take care of them!"
    e "Isn't it a lot of work to take care of that big an area though?"
    "The bear scratches underneath his chin, as if in deep thought."
    a "I never thought about it!"
    a "I guess it does get to be a bit much sometimes."
    "He laughs merrily."
    a "Not that it's ever too much for me. The only real issue I have is that my patrols sometimes have to go into the night."
    e "...How do you patrol in the dark. You can't see, and I know your other senses aren't that good."
    a "Well, I can't do all of the things I'm asked to do during my rounds, but I can reduce monster populations."
    e "Do you have a special strategy or something?"
    "You get a well meaning shrug from the man."
    a "Not really. I just wait for a landshark to bite my leg, and then I punch it very hard."
    a "Problem solved."
    e "..."
    e "I'm not going to address that."
    e "You have other tasks on patrol other than landsharks?"
    a "Of course! There are all sorts of things that need taking care of over there."
    "Amble wraps an arm around your neck and grinds his fist into your hair, giving you a noogie. It doesn't hurt, but your hair is a mess now."
    pause 1
    a "I just had a great idea!"
    a "Why don't I just {i}show{/i} you what I do out there!"
    "Amble's voice hurts at this range, but his good mood is infectious."
    menu:
        a "Are you coming with me?"
        "Yes{#amblepatrol}":
            e "I don't see why not. Sounds like it could be fun!"
            a "Almost as fun as the last time I took you somewhere."
            "Amble isn't teasing you when he says this, it's a statement of fact to him, it seems. Remembering your special training with Amble makes you flush with embarrassment, a feeling Amble seems immune to."
            e "Well..."
            "Amble's arm tightens around you slightly, cutting you off."
            a "Maybe not this time, little one. A bit too public out in the fields!"
            a "I have a reputation to uphold."
            "The wink Amble gives you leaves you confused as to whether or not he means what he's saying."
            "It's probably best to assume he's being serious."
            a "I won't say no to some other time though."
            "Just when you think you're free from teasing, you're suddenly struck with another attempt."
            "The worst part is, you're pretty sure he doesn't even mean to tease you. He's being entirely honest, and accidentally messing with your heart."
            e "...okay, it's good to know there might be another time, honestly."
            "You mumble that to yourself under your breath. Thankfully, Amble is distracted enough by his excitement not to notice."
            e "When do you want to go out and show me?"
            "Amble gives you a carefree shrug."
            a "Whenever you're free. Give me the word and I'll bring you along for one of my patrols."
            e "Alright."
            jump Amble_Patrol_Farm
        "Maybe Later{#amblepatrol}":
            e "Now?"
            a "Oh? Are you not available now, puny friend?"
            "Amble lets go of you."
            e "I've just recalled, I've got something else to do."
            a "Of course, no need to explain yourself."
            "Amble gives you a carefree shrug."
            a "Good luck on your something else, [e]. You can come back any time if you wanna visit the farm."
    jump Amble_Normal_Talk
label Amble_Patrol_Farm:
    $ backyard_barn.discovered = True
    e "Amble! I'm ready to go on the patrol with you."
    "Amble looks up at you with a smile, getting up while rolling his shoulders and popping his neck."
    a "Ah, it is good to see you excited to come, puny friend."
    a "You're the first person to actually take an interest in what happens out in the farmlands."
    "The jolly giant seems not at all bothered by this fact, though he does seem happy to see you."
    "Then again, he tends to look happy to see anybody."
    e "I can't imagine why. It's not like there aren't any threats out there."
    "Amble scratches the back of his neck for a moment."
    a "Yeah, well, they say the people are boring and talk too much, and that they're too dumb to have a conversation with."
    a "Needless to say, they think I'm a great fit."
    "Amble throws you a playful wink. It seems he's aware of his reputation. It's hard to believe that it doesn't make him upset, but his face betrays no hint of that."
    e "Maybe I'm a good fit too, who knows."
    "Amble laughs, slapping you on the back hard enough to send you stumbling."
    pause 1
    a "I think you will! The farmers will like you at the very least. Your efforts with the landsharks haven't gone unnoticed."
    "The statement catches you off guard, a blush coloring your face."
    e "Really? I thought nobody saw me out there..."
    "At this point, Amble's eyes are twinkling with mirth as he thinks on conversations he's had with farmers."
    a "Oh yes, the rumormill has been filled with stories about you. Everyone wants to know who the handsome young dragon is."
    e "They really call me handsome?"
    "Amble shrugs slightly."
    a "Sometimes, though they mainly say it when they call you 'a little too handsome for your own good.' Your flirting has apparently given a few farmers quite the show!"
    "Even if you didn't flirt against every enemy you fought, it's a little embarrassing to think of how many random people may have caught sight of your actions."
    "...Even if the idea turns you on a little."
    e "Ehem. Well. We should head out, yes?"
    "Amble throws his head back in a hearty laugh before leading you off towards the farmlands."
    a "As you wish, puny friend. We'll see if old Arthur will mention you like he did last time. Try not to run too far if he does."
    a "I don't want to have to spend half of my patrol chasing after you."
    "You act like you don't hear Amble, trying to move on with your life as soon as possible."
    scene summery_farmland with dissolve
    show amble normal with dissolve
    "You follow after Amble for a bit. It's easy to see why some of the farmers around here pay extra attention to the people fighting landsharks."
    "Amble's ass isn't exactly well hidden, what with the skimpy gear he always wears around."
    a "So, Puny friend."
    "Amble shocks you out of the meditative state his ass had lured you into."
    a "Other than Landsharks, what are the main dangers you can find in the farmlands?"
    e "Umm... There aren't exactly many, but I'd say the scarecrows."
    "Amble's ambling pace picks up a bit as your words put some pep in his step, for some reason."
    a "The scarecrows around here are a little {i}too{/i} good at scaring away scarecrows and the like sometimes."
    "You nod."
    e "They're a lot like Lothar's dummy."
    "Amble suddenly halts, turning to look at you."
    a "I never really thought about that. I wonder if he teaches them too?"
    "What does he mean by teach? Can you even teach cloth?"
    e "What do you mean, teach."
    "Amble gives you a quizzical look."
    a "Why, our first stop of cousre!"
    a "We're going to teach one of the newly made scarecrows how to scare crows. And also maybe landsharks."
    a "I've been working on that last one for a while. They're not particularly good at wielding axes."
    e "Where and how exactly are we going to be doing this?"
    "Amble looks slightly confused about your questions, as if thes should be things you know already."
    a "Where? That farmhouse over there."
    "Amble points to a distant farmhouse sitting cozily in the wheat fields."
    "Well, not that the farmlands only have wheat. It's just the predominant plant."
    a "How? Well, same way you teach anything really, by showing it."
    a "Same way I taught you how to strike the core."
    "You smirk at that. He's handed an opportunity for revenge to you on a silver platter."
    e "So you're going to suck is dick?"
    "Amble looks at you, completely bewildered."
    a "No? Why would we. What does that have anything to do with training."
    e "Wha- bu-"
    a "Plus, it's not like scarecrows even have dicks. You say the craziest things sometime, puny friend!"
    "He has to be fucking with you. There's no way this man is serious."
    "You'll go along with it, just in case."
    e "Yeah, haha. I sure do!"
    a "See, like that! Why would you agree with me."
    "..."
    "It's for the best if you just follow him for now."
    pause 2
    "Looking at your destination, it's quite a bit closer than when Amble first pointed it out. You crossed a considerable distance while talking to him."
    "Time flies when you're having fun, or... whatever it is you have with Amble. It's tough to know what to think of him. It's like he's constantly switching between two modes, and it's hard to keep up."
    "It's only a few more minutes before you can start to make out individual elements of the farmhouse Amble is taking you too."
    scene backyard_barn with dissolve
    show amble normal with dissolve

    "It's larger than you thought, its rich wooden walls reaching two floors up. From what Amble tells you, it also goes one floor down."
    "Not the biggest farm you've seen, but it could comfortably host a family with room to spare."
    "As you finally bring your gaze towards the front of the farm, you see someone on the porch gently rocking in their rocking chair, a cigar in his hand."
    "He seems to be some sort of Shepherd -- old, from the looks of things. Despite that, the man looks full of life."
    "The two of you spot each other at the same time. An excited grin spreads across the farmer's face as he waits patiently for the two of you to approach."
    a "Hello Mr. Arthur!"
    show amble normal at l1 with dissolve
    show arthur normal at r1 with dissolve
    "'Mr. Arthur's' smile morphs into a look of slightly irritated confusion."
    ar "I thought I told you to call me Arty?"
    a "I remember! I was just being polite because I brought a guest who wanted to come along on the patrols."
    "Arty waves Amble off the moment he mentions you again."
    ar "I understand, but there's no need to be formal."
    if landshark.win >= 7:
        ar "He's definitely gone above and beyond formality around these parts."
        "You turn scarlet when you look at the ravenous hunger in Arty's eyes."
        e "I apologize for being inappropriate, Mr. Arthur."
        ar "Please, call me Arty for now. And don't be ridiculous, if anything, I'd prefer you be more inappropriate."
        ar "If you like the sound of that, you're always welcome to come by for a fun time..."
        "The old man says this with a wink and waggle of the eyebrows. However playful, you're decently confident he's serious, if his slowly growing bulge was anything to go by."
        e "Yes, umm. We'll see! For now I'm on patrol with Amble."
        ar "Are you saying Amble is going to be keeping you busy instead?"
        with vpunch
        e "No! No! Nothing like that."
        "Arty lets out a disappointed sigh."
        pause 1
        ar "Aww, and here I thought the two of you had been up to some fun."
        ar "What do you say, Amble? Would you take him up on some fun if he offered?"
        "The question hits Amble out of nowhere, but the bear seems completely unsurprised as he gives a frustratingly honest answer."
        a "Yes! In fact, we already have before!"
        "If it were possible to turn more red, you would have. Unfortunately, you have no avenue by which to express your embarrassment properly."
        ar "And? As good as I suspect?"
        "Amble shrugs at Arty, a slight smile playing at his lips."
        a "Better, I think."
        ar "Ooh, perfect. Well, the offer is definitely still there if you want to!"
        "All you can do is nod."
    else:
        ar "I'm just a farmer. If anything, I should be speaking respectively of the two of you."
    ar "Oh, but I'm getting ahead of myself. What's your name, pup?"
    "This is the first time you've been called that that you can recall -- the proper term would be hatchling, but the meaning is understood."
    ar "Hello?"
    "It seems you had frozen for a few seconds to process what he said."
    e "Ah, sorry. I'm [e]."
    "Arty gives you what seems to be a genuine smile."
    ar "An excellent name, if not particularly common around these parts."
    e "I... like your name too, Arty."
    "The Shepherd looks at you skeptically, but decides to drop the topic."
    ar "Well, I'm glad you're here, Amble."
    ar "The scarecrow is already at the start of its learning period, and if we delay too much longer, it may become a dud."
    a "Bring him out here then! My puny friend here and I will teach him how to scare away crows and landsharks!"
    "Arthur walks into his farm at a brisk pace, it is only moments afterwards that the man reappears with a slightly twitching scarecrow."
    ar "I'll leave him out here with you for now. I'll be taking my morning nap inside if you need me."
    show arthur normal at l2 with move
    show amble normal at c1 with move
    "Amble gives him a nod and begins lugging the scarecrow out towards the clearing."
    e "So, do we do anything special to teach the scarecrow?"
    a "No, puny friend. He is learning the whole time! Even now he learns out to drag people away by their arms."
    "You give Amble a concerned look."
    e "Should we be teaching him that?"
    "The carefree bear gives you a shrug."

    a "Why not. Nobody but the farmers go around here, and the scarecrows know the score. If they attack me, well. That's just a patrol made more interesting."
    "A worrying thought process to say the least."
    e "Well, I guess we'll see how it goes."
    "Amble gives you a wide smile."
    a "Exactly! Take life as it comes."
    "The bear shifts his grip on the scarecrow, and pushes it into the farmland soil."
    a "For example! What do you think I should teach the scarecrow first?"
    e "I don't know... how to be scary?"
    a "That's easy. Here!"
    "Amble tilts his head back, teeth bared. A low growl begins to come from his throat."
    with vpunch
    pause 2
    "It quickly builds into a full roar, one that fills the air and leaves echoes for minutes."
    "The bear looks over at you, slightly hurt. You only realize why when you see that you had backed away from him in fear."
    e "Sorry, hehe -- It just worked so well! That's the first time I've seen you look anything but happy and sweet."
    a "I know. I have to work hard to maintain the image of a friendly bear. We don't exactly look harmless."
    "In fairness, you can see what he means. Never before now had you realized how sharp his teeth were, the size of his claws -- the fact that he stood over a foot over you."
    "It would be best to change the subject."
    pause 1
    e "Well, I think the scarecrow should have learned by now. How can we check?"
    "To that, Amble just gives you a smile. He takes a little drawing of a crow eating wheat out, and shows it to the scarecrow."
    with vpunch
    "Immediately, it begins to shake. It starts with the gentle dragging of branch against branch, the sounds of a suffering tree."
    with vpunch
    "The sound it ends with is... what you would imagine a tree screaming would sound like."
    e "Alarmingly efficient."
    "The bear turns to you with a cheeky grin."
    a "Right? Now, give me a second, this next one will take a while."
    e "...what are you teaching it now?"
    e "Isn't scaring all it has to do?"
    "Uproarious laughter is your immediate response."
    a "Maybe for most! But I'm raising a fighter if I have anything to do with it."
    "Amble begins punching the air and hopping back and forth, as if he had only one leg to move on."
    e "W-what are you doing?"
    "He looks like an insane person. A dangerous, two-hundred pound insane person."
    a "I'm teaching him boxing! They don't carry weapons, so I've practiced seeing if I could beat a landshark like this!"
    "It's nice to be Amble's friend, and not having to worry about dying at his hands. If the man can stop a landshark like this..."
    pause 1
    "He could probably snap your spine like a twig."
    e "So, umm. It's okay to talk while you teach it this?"
    a "Yeah! It's going to be a while, so talking would be the most fun!"
    "You have permission to talk from Amble, but... what can you even talk about?"
    "The best start you can think of is your commonalities as adventurers."
    e "Hey, Amble! I've never really asked why you do this? Adventure, I mean."
    a "Well! Being an adventurer is all about helping people."
    a "Helping people is fun! Even if helping sometimes means diving into a pit full of angry chickens to collect an eg."
    a "People smile when I help them. I wouldn't trade that for anything else in the world!"
    "Anyone else would have felt like they were opening up their soul, but Amble seems completely nonchalant, focused mainly on teaching the scarecrow boxing."
    e "Alright, well... what if you get a job you don't want? Like the person is bad or something?"
    "The bear momentarily slows in his boxing, before you realizing and picking the pace back up."
    a "I won't help them! If them smiling means most others don't, why would I help them?"
    a "Plus, I don't think anybody is inherently good or bad! Just better in the moment or not."
    e "What about the people that decieve you. Aren't they bad people? What do you do when that happens?"
    "Amble smiles as he boxes -- the question is quite fun to him for some reason."
    a "Depends what they made me do, or how they deceived me."
    a "Normally? I give them a pat on the back and tell them don't do it again, or chuckle that they got one over me."
    a "Sometimes I have to do much more. It brings me no pleasure to kill or imprison, but sometimes that is the only solution I see."
    "Again, the perfect clarity with which he says that scares you."
    "You have a feeling he would just as easily kill a man as a squirrel -- it all depended on the circumstances to him."
    "Your brain whirls with questions, but you can't bring yourself to ask them after that last one."
    scene summery_farmland with dissolve
    show amble normal with dissolve
    "It's Amble who breaks the silence with a question of his own."
    a "Why do you do it?"
    pause 2
    "You look up in shock."
    e "Because I enjoy it. I enjoy adventure, helping... but I enjoy meeting people most of all."
    e "At least, I think that's why I enjoy it. It's hard to know stuff like that."
    "Amble nods as he moves, but realizes that might give the scarecrow the wrong idea."
    a "I get that."
    a "Do you ever doubt yourself, though? I know I do, when I fail to help, or struggle to understand what's happening around me."
    e "You mean in general?"
    "Amble laughs softly."
    a "No. Everyone doubts themselves. I'm asking if you ever doubt your ability to be an adventurer -- if it would be better for someone else to."
    "There's a question you had never thought about. When you think about it, you're probably a pretty bad adventurer in most ways."
    "But the people around you seem to appreciate you for what you do. So maybe there's no reason to worry?"
    e "Yeah, but never enough to really matter."
    e "You?"
    "Amble's face forms a self-deprecating smile, even as he continues his boxing flawlessly."
    a "Always."
    e "And what do you do then?"
    a "What I always do when I struggle --"
    a "Believe I'm the good person I know I am, and find a way forward."
    a "Most of my problems tend to disappear if I punch them hard enough. The ones that don't, I find someone to fix."
    pause 1
    "You open your mouth to ask a question, but realize the bear hasn't stopped speaking."
    a "And before you ask what I do if that doesn't work. I try anyways."
    a "Giving up gets you nowhere. So fight, rage if you have to. Pull a way up to the surfa-"
    "The bear suddenly stops moving."
    a "I finished that sooner than I thought!"
    a "These next few require some more concentration, as they involve actually feeling out landsharks -- something hard for even me to teach."
    a "We can finish talking some other time, puny friend."
    e "O-okay."
    pause 1
    "Yet again, the jolly giant shows you an intensity you'd never thought was there. Should you be afraid of that? Or respect him all the more?"
    "It's hard to tell. The same person that told you to fight until death itself takes you is currently pressing against the floor with one finger and wiggling it around in front of a scarecrow."
    "There's something off about him. You know that now, and you want to know more."
    "For now, however, you'll have to content yourself with knowing he cares about you, and has a theoretically positive goal."
    "I mean, what's the worst you can do when your goal in life is to make people smile."
    "..."
    "Amble finishes teaching the scarecrow after a few hours."
    "It's mostly uneventful, except for a few moments here and there where he used you as a training dummy example for his student."
    "As soon as he's satisfied that the scarecrow is ready, Amble runs up to the Farmer's door and leaves it on the porch."
    "It seems Arty woke up and came out for a bit, as you see a small wooden plate with corn on it."
    if landshark.win >= 7:
        "There are two notes that go along with it."
        "One reads: 'To the two lovely gentlemen helping me with my farm, I leave this corn. It's not much, but I can promise that it's good stuff, raised with love and care.'"
        "The next, which is clearly for you considering the little winking face Arty has drawn on it reads: 'If you ever want to take me up on that offer, here are the directions to my house. You'll have fun if I'm right about you.'"
        "Blushing, you take a piece of corn off of the table, and stuff the note into your bag. You might need it later."
    else:
        "There is a note that goes along with it."
    "Amble leads you further on your patrol, the two of you eating Arty's corn with little small talk thrown in."
    "It really is good corn."
    "The rest of Amble's patrol is fairly uneventful -- farmers come out of their houses to say hello to Amble, and give him little gifts as thanks for his generosity."
    "'Thank you for getting rid of that rast infestation! Thank you for carrying my son to Lusterfield to get treated!' All the while giving the bear corn, peaches, even a keg of beer."
    "Amble took them all -- except the keg of beer, which he told the man to sell to Cane if anything -- with a smile on his face, and pride in his eyes."
    "Seeing him like this, you think you can understand a little better what Amble does and why."
    "Even if he still makes no sense sometimes."
    "Eventually, you find yourself back in Lusterfield, seven hours of patrol having flown by."
    $ timenow.addTime(0, 7, 0)
    scene black with dissolve
    pause 2 
    scene lusterfield_range with dissolve
    show amble normal with dissolve
    a "So, did you have fun?"
    "You take a moment to think about the day."
    "There wasn't all that much to do, but it was nice to see the houses and people. It was nice to help."
    e "I don't know if I had fun, but I enjoyed it."
    "Amble grins at you, happy to finally have someone that enjoyed a patrol with him."
    "The bear runs up to you and fittingly pulls you up in a bear hug."
    a "That's wonderful news, Puny Friend!"
    a "Would you be willing to go on patrol again someday?"
    "It's your turn to grin at Amble -- it seems he enjoyed your company after all."
    e "I think I would!"
    e "But for now, I should go get my things in order. It's been a long day."
    "Amble nods sagely."
    pause 1
    a "It has."
    a "Make sure to enjoy yourself out there!"
    "It's hard not to smile with the big lug around."
    e "I'll try. You do the same, alright?"
    a "Always, puny friend, always."
    $ QuestFinish(quest29)
    jump main_summery_farmland
label Amble_Ask_Patrol_Task:
    if task03.completedtimes == 0:
        a "Puny Friend, I have a small favor to ask of you."
        "Amble is looking at you with eyes filled to the brim with sweetness and innocence."
        "It's pretty intense, actually."
        e "S-Sure, what do you need, Amble?"
        a "Wonderful!"
        "He wraps you up in a tight hug and whirls you around"
        "It's a great feeling, except that all the air in your lungs has been forcefully pushed out"
        e "...Amble... please... I can't breathe."
        a "Oh! Sorry, Puny Friend, I was very happy to hear that you could help."
        "He gently puts you back down."
        a "It's very important that this gets done as soon as possible, and I've been too busy with Lot to do it."
        e "Is it okay if I take a couple days to do it?"
        "Amble gives you a sidelong look"
        a "It would be best if you didn't, but yes, in theory everything would be fine."
        "Amble coughs into his hand before straightening his back and puts his hand behind his back in imitation of a military officer."
        a "The farmlands of Lusterfield are regularly plagued by landsharks."
        a "Every so often, someone must go through and cull their numbers or otherwise render them harmless."
        e "Do the landsharks attack people often or something?"
        "Amble stops a moment to consider his next words. Turns out this issue may be more complex than you thought."
        a "No, not exactly, though they sometimes do."
        a "They're territorial creatures, and attack whatever walks into what they consider theirs."
        e "So why are they such a big problem?"
        a "Well, they do hunt outside of their territory, and in doing so, tear up the fields the farmers work so hard to tend to."
        a "That's why it's your job to patrol the area and kick out any landsharks that aren't where they're supposed to be"
        "Amble grins a bit, getting out of his military impression to his more casual and cuddly self."
        a "I normally go there and do some guard duty in my free time..."
        "Amble leans down to your ear, lowering his in a conspiratorial whisper, which for him is about as loud as a normal person's speech."
        a "But now I gotta stay around here and take care of those two. Y'know, make sure they're hale and hearty."
        a "Anyways!"
        "Amble yells that as he leans away from you, eliciting a pained yelp from the nearby Jog, clearly listening in on the conversation."
        a "Get out there and hunt some landsharks [e]!"
        e "You called me by my name!"
        a "Dunno what you're talking about, Puny Friend."
        a "Regardless, thanks for going out and doing this for me."
        e "Yeah, you got it."
        e "But, umm... How many sharks am I supposed to deal with for you?"
        a "Oh. Right."
        a "How about a quarter of a half what I usually do, meaning around 3!"
        "You take a moment to think about the fact that Amble is implying that he regularly goes out and beats up 24 sharks."
        "You're suddenly very grateful he's an ally, and not an enemy."
        e "S-sounds good to me!"
        e "How will you know that I've actually defeated them?"
        a "Well, I trust you, but... I'll know. Comes with knowing one of the best information sources in town."
        e "Fair enough. I'll be back after dealing with the land sharks!"
    else:
        a "Puny Friend!"
        e "...yes?"
        a "The landsharks are becoming a problem again."
        e "I take it you want me to clear them again?"
        a "It would be helpful, puny friend."
        e "Alright, I'll take it."
    $ TaskBegin(task03)

    $ landshark_reqwin = landshark.win + 3
    $ task03.tProgress(__("Defeat 3 Landsharks in the Farmland"), landshark, landshark_reqwin-1)
    jump main_lusterfield_range

label Amble_Report_Patrol_Task:
    if landshark.win < landshark_reqwin:
        if task03.completedtimes == 0:
            e "I finished with the landsharks!"
            "You see Amble look at you skeptically."
            a "I know you haven't beaten 3 yet. A little bird has been keeping me updated on your progress."
            a "You can do this, I believe in you, Puny Friend. Come back when you've finished."
        else:
            "A mischievous twinkle is visible in the corner of Amble's eye."
            a "Puny Friend, I know I'm not great at math, but I know that you haven't beaten 3 sharks."
            a "Come report back to me when you've done so!"
    else:

        if task03.completedtimes == 0:
            a "Ah! Puny Friend! I see you finished dealing with the landsharks!"
            e "How did you know?"
            a "Someone kept me updated on your progress the entire time."
            "You... aren't going to think about the implications of that."
            a "You also have the look of someone who just fought 3 sharks."
            e "What kind of look is that?"
            "Amble breaks out into a wide grin, slapping you on the back."
            a "Tired, Puny Friend. Tired, but satisfied."
            "Amble stops talking for a moment, a worryingly naughty smile playing across his lips."
            a "Lot also stopped by to see if we knew where you were."
            e "What did you tell him...?"
            "Amble scratches the side of his head for a moment, as if trying to recall what happened."
            "It would be convincing if he didn't look like he was trying to hold in a full-throated laugh."
            a "Ah, I just told him I had sent you off on a dangerous mission."
            a "He looked just about ready to kill me, saying we were going to go out and help you right that instant."
            e "... That doesn't really sound like Lothar."
            a "You'd be surprised at some of the things the Hero of Lusterfield really thinks deep down."
            "A playful twinkle shines in the corner of Amble's eye."
            a "But, if anyone asks, I said nothing."
            e "Amble... Jog is right there..."
            a "Eh, Jog already knows. Plus, Lothar can be pretty obvious when you start to look closer."
            a "He relaxed and went back to his usual spot when we told you Jog was making sure you were safe."
            j "Not after yelling at me for not telling him that first."
            a "Right, that. I wasn't really listening, so I forgot all about it."
            "Amble feigns at picking his ear."
            a "Regardless, thank you for getting the sharks dealt with!"
            a "I don't really have any grand reward for you."
            a "But sometimes that's just how it is for an adventurer."
            "Out of anyone else, especially Cane, you'd think this was them trying to get out of paying you, but..."
            "Amble seems to genuinely mean it."
            "You did help a lot of people today by dealing with the landsharks."
            "You feel a bit more like a hero."
        else:
            "Amble has a bigger, goofier smile than normal on his face right now."
            a "You did it again Puny Friend!"
            a "Thank you as always for being such a good friend!"
            "Amble wraps you up in a big hug, this time making sure to let you breathe."
            e "I-it's no problem Amble."
            "He puts you down, still smiling."
            a "Maybe, but I still appreciate it!"
            "There isn't really anything you can do but blush under the praise he's piling on."
        $ TaskFinish(task03)
        jump main_lusterfield_range

label Amble_Dialogue_End:
    e "I think that's all for now."
    e "Thank you so much, Amble."
    a "No need, and thank you for the time too."
    if amble_location == "lusterfieldrange":
        jump main_lusterfield_range
    else:
        jump main_riverside_crossing

label Jog_Ask_About_Gnolls:
    e "Hey, Jog, what do you think about the gnolls?"
    j "What... Gnolls? [e], are you asking about them because I look like one?"
    e "N-no! I just wanted to know what you thought about them. Since... you know, we live near them and all."
    j "Oh. Well, I don't think about them much. They're just another creature in the wilds to me."
    j "They're not really my kind of people, let's put it that way."
    j "But... I do know they usually hunt together, led by a leader. While the rest of them spread out in the plains."
    e "Interesting, do you think they follow some sort of sounds sometimes?"
    "Jog's eyes squints as he looks at you."
    j "Look, [e]. I know what happened to the flute, you could attract those gnolls with the sound of the flute, but it doesn't work anymore."
    j "Take it if you want, I lifted that thing myself anyway."
    "Your sigh a breath of relief, at least he doesn't seem to know what you saw from the flute..."
    jump Jog_Normal_Talk

label Lothar_Ask_About_Gnolls:
    e "Hey, Lothar, what do you think about the gnolls?"
    l "Gnolls! Where?"
    "Lothar immediately stands up, looking around wildly."
    e "No, not here. Just in general."
    l "Phew... These evil creatures must all be vanquished, wipe them off the map! We cannot let them roam free on the plains!"
    e "Whoa, calm down Lothar. They're not that bad."
    l "Not that bad? They are vile, disgusting creatures that poses dangers to everyone, Worse than the bandits!"
    e "I don't think they're worse than bandits... they just like to play around."
    e "But, what do you plan to do to stop them, if you... intend to?"
    l "W-what? Uh... I... I have more important quests to take care of, disciple. They are mere nuisances to my heroic ventures."
    e "Right..."
    jump Lothar_Normal_Talk
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
