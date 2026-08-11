label Arthur_Dialogue:
    if isNight():
        scene backyard_barn
    else:
        scene backyard_barn
    with dissolve
    show arthur normal with dissolve
    ar "Good Day, Pup."
    if arthur_encounter >= 2 and arthur_welcome == False:
        $ arthur_welcome = True
        if arthur_2ndChoice == "Good":

            if pc.armor["Mask"] != None and pc.armor["Mask"].img == "Dog Collar":
                "As you approach Arty, you see the old dog is smiling at you."
                ar "You're a very good boy, already having your collar on."
                "Your heart does a small backflip at the doting look on his face."
                ar "Every day I'm more sure that I made the right decision making you mine."
                "You blush slightly."
                e "And I am glad to be yours."
            else:
                "As you approach Arty, you see the old dog is smiling at you."
                ar "Go ahead and put your collar on, pup."
                "Obediently, you take it out of the inventory, and put it on."
                ar "It's good to see you again."
                "You can't help but smile at your master's happiness."
                e "It's good to see you too, master."
        elif arthur_2ndChoice == "Bad":
            "As soon as you get close to Arty, he gives you a command."
            ar "Clothes off, leash on. Now."
            "You whine a bit at the intensity of his voice, but obey, quickly stripping and putting your collar on."
            "Arty reaches for your leash and tugs down, bringing you to your knees as he puts his foot on top of the cord."
            "Your head is pointed at Arty's boots now, and you have to strain to look up at him."
            ar "There. You may talk to me now."

    jump Arthur_Normal_Talk

label Arthur_Normal_Talk:
    $ timenow.addTime(0, 0, 3)
    menu:
        ar "What's the occassion?"
        "Learn his opinion on the vote" if quest37.status == 2 and quest37.start_date + rahim_vote_duration - 1 >= timenow.day:
            jump Arthur_Voting_Opinion
        "Deliver the goods" if is_recipient("Arthur"):
            $ recipient_name = "Arthur"
            call Courier_Delivery_Dialogues from _call_Courier_Delivery_Dialogues_11
        "Pick up the delivery" if is_client("Arthur"):
            $ client_name = "Arthur"
            call Courier_Pickup_Dialogues from _call_Courier_Pickup_Dialogues_11
        "Ask about the Plum Plunderer" if quest33.status == 2:
            jump Arthur_Bandit_Meet_Quest
        "Ask about the Plum Plunderer" if quest33.status == 3:
            jump Arthur_Bandit_Meet_Quest_Inquire
        "Wear the Collar" if arthur_2ndChoice == "Noo" or arthur_2ndChoice == "No":
            $ arthur_2ndChoice = "Good"
            jump Arthur_Wear_Collar
        "Ask for another round" if arthur_encounter >= 2:
            jump Arthur_Ask_Another_Round
        "Ask about the next plan" if arthur_2ndChoice == "Good":
            jump Arthur_Ask_Next_Plan
        "Ask about the lesson" if arthur_2ndChoice == "Bad":
            jump Arthur_Ask_Lesson
        "Ask about the Farm":
            jump Arthur_Ask_Farm
        "That's all for now":
            if arthur_2ndChoice == "Good" or arthur_2ndChoice == "Bad":
                e "I think that's all, thank you Master."
            else:
                e "I think that's all, thanks Arthur."
            ar "You're Welcome, and see you around."
            jump main_backyard_barn
label Arthur_Wear_Collar:
    ar "So, you ready to accept the collar and be mine, pup?"
    menu:
        "No{#arthurcollar}":
            e "No, sorry. I was wondering if you'd like to mess around anyways...?"
            "Arty gives you a bemused look, if one tempered by disappointment."
            ar "No, pup. Be mine, and you'll get the knotting you want. Until then, we can sit and chat, but we won't be fucking around."
            "It seems he's only willing to fuck you if you're his."
            ar "The collar will be here waiting for you if you decide your rightful place is under me."
            jump Arthur_Normal_Talk
        "Yes{#arthurcollar}":
            "You take a moment to work up the courage to say what you've taken time to think on."
            e "Yes, please, be my master, Arty. I promise I'll serve you well."
            "Arty looks extremely pleased, and his cock is already peeking out of his sheath underneath his pants, forming a quickly growing bulge."
            ar "Alright then, pup. Put it on."
            "Hesitantly, you bring each side of the collar up to your neck, your breath shaking. You somehow manage to loop the buckle despite your nerves, and finish standing there in nothing but a harness and collar, leaky cock twitching and throbbing."
            jump Arthur_Second_Scene_Yes
label Arthur_Ask_Another_Round:
    e "Hello, sir. I hope you're doing well...?"
    "The horny shepherd dog greets you with a small smile."
    ar "After the other day, I'm doing very well."
    "You feel a bit embarrassed when he mentions it so casually, but that is why you're here after all."
    e "About that... I was wondering if you'd like to go another round, sir?"
    "Arty gives you a long look, massaging his sheath gently as he does."
    ar "Tempting."
    "Just when you think he's going to ask you to suck him off again, he takes his hand off of his bulge, and lets out a long sigh."
    ar "Unfortunately, I have something planned for you, and I can't fuck you until I have it ready."
    ar "Come back in a few days, and you'll get what you want, pup."
    "This is a surprising amount of self-control coming from Arty. Whatever it is he's preparing, he must {i}really{/i} want to do it right."
    e "Alright, I'll see you later, I guess."
    "Arty gives you a small wave before going back to relaxing on his chair."

    ar "I look forward to it."
    jump Arthur_Normal_Talk
label Arthur_Ask_Next_Plan:
    "You fidget nervously for a moment, but quickly work up the courage to speak. He's been very generous with you so far."
    e "Sir, do you have any plans for what we'll do together next time?"
    "Arty cocks an eyebrow, but soon breaks out into a grin."
    ar "That excited to serve your master?"
    "Embarrassed, you nod, but find yourself staring at the floor."
    ar "Hey, hey. It's alright. You're doing great, pup."
    "You look back up at Arty, who looks slightly concerned about your bashfulness."
    "Once your eyes meet, your master taps his lips impishly."
    ar "Let me prove it to you. Come and kiss me, pup."
    "Surprised, you hesitate before moving in for him to kiss you."
    "It's a gentle thing, his tongue carefully invading your mouth and playing with your tongue."
    "He knows you're his, but wants to show you that he wants to take care of you."
    "Before you know it, Arty moves his head back, ending the kiss."
    "Breathless, your eyes flicker up and down from Arty's smile, to the bulge you see forming in his trousers."
    e "Thank you, master."
    ar "Of course, pup. I'll take care of you to the best of my ability as long as you do a good job."
    "You nod once again, this time feeling no urge to look at the floor. You're proud to be where you are."
    "This almost makes you miss the mindless tapping of Arty's hand on his leg."
    "He appears to be lost in thought."
    "Whatever it is, it seems to be something he quite enjoys, his bulge growing larger as you wait."
    ar "To answer your question, I plan to see how well you do fucking your master."
    ar "A good pup has to know how to fuck his master properly, after all."
    "Your own cock responds favorably to this news, twitching violently."
    e "I'll do my best when the time comes."
    "Arty nods to you with a pleased smile."
    ar "Yes, you will."
    jump Arthur_Normal_Talk
label Arthur_Ask_Lesson:
    if arthur_asked_lesson == False:
        $ arthur_asked_lesson = True
        e "Earlier, you mentioned giving me lessons. What did you mean by that?"
        "In response, Arty unbuttons his overalls. You hadn't noticed it before, but your master is rock hard right now."
        "He grabs you by the horns and takes his foot off your leash, pulling you forwards towards his cock."
        ar "Fit my knot in your mouth."
        "You look up at him in question, only for him to take one hand off of your horns and force your mouth open with it."
        "Immediately, he shoves your now open mouth onto his cock, forcing you down faster and harder than you can acclimate to."
        "You're only about 3/4ths of the way down his cock, and already it's tickling the back of your throat."
        ar "These are your lessons."
        ar "How to make yourself useful."
        ar "You should be thankful I'm even giving you the opportunity to learn this, worthless pup that you are."
        "Your master moves you a little further down, only to let go a moment later."
        "You pause, confused on what to do."
        ar "Fit my knot in your throat before I fit it in there for you. Neither of us want me to have to do that."
        "Understanding, you get to work, sucking off your master, and slowly working yourself down his cock."
        "In the meantime, Arty sighs in disgust."
        ar "I shouldn't have to be telling you this."
        "Already, you're at his knot, pushing yourself to get even a little of it past your lips."
        "Bored, but intent on training you, your master leans back in his chair as you fit more of him inside of you."
        "Once you've fit half of his knot into your mouth, the fullness of the sensation forces you to take a second."
        "This disruption to your activities displeases the dog above you, his hand briefly returning to the top of your head to force you further down."
        "A bead of pre leaks from your cock and onto the floor, something Arty takes note of."
        ar "At least you're starting to figure out that pleasing me should be what brings you the true pleasure."
        "Your master kicks off a boot, and brings his foot up to your cock."
        "You flinch in surprise, only for Arty to use his hand to put your head back to where it belonged."
        ar "Even the most worthless bitch should receive rewards for their actions."
        "It's hard to focus on his words when the action of going up and down his cock requires your full attention, especially now that his foot is rubbing your cock against your belly."
        "The mix of sensations and degradation quickly bring you past your edge, cumming on the ground as Arty puts his foot away, so you don't get it dirty with your cum."
        "Only a short while later, you manage to get his knot all the way inside your throat."
        "You feel completely full, much of his cock stuffed down your throat, and the remaining part completely occupying all of the free space in your maw."
        "It is only for a moment, as Arty grabs you by the horns again, and forces you off."
        ar "Next time you'll do that from the start, rather than make me show you, yes?"
        "You nod obediently."
        e "Yes, master."
        "Arty gives you no approval, but lets you take a second before you move back to your previous position on the floor."
        ar "Those are what your lessons are."
        "He buttons up his overalls again, covering his erection."
        ar "Pay attention, and you might learn to be worth something."
    else:
        e "Can you teach me another lesson, master?"
        "Arty gives you an imperious glare."
        ar "I decide when and how you are taught, pup."
        ar "Remember your place."
        "Chastised, you shut up on that topic."
    jump Arthur_Normal_Talk
label Arthur_Ask_Farm:
    if arthur_2ndChoice == "Bad":
        "You make sure to keep any possible sound of disrespect out of your voice when you ask your master. This is a supplication for an answer."
        e "Pardon my asking, master, by how did you start farming?"
        "Arty answers after a few moments of scratching his bulge"
    elif arthur_2ndChoice == "Good":
        e "Sir, I was wondering if you could tell me how you started farming?"
        "Arty gives you a slight smile, happy to see you take an interest."
        ar "Of course, pup. I'd be happy to."
    ar "My family has been farming here for a few generations now."
    ar "Though the house is the same one I got years ago, I've managed to expand our lands considerably, in exchange for a few risky business decisions."
    "A lazy smile spreads across his face."
    ar "I'm pretty happy with how things are for me."
    jump Arthur_Normal_Talk

label Arthur_First_Scene:
    stop music fadeout 1.0
    $ arthur_encounter += 1
    $ arthur_first_encounter = timenow.day
    "You can feel your heartbeat pounding as you make your way up the road to Arthur's house."
    "The old dog did tell you to come over whenever you'd like to have some fun, but actually going through with it is slightly scary."
    "Luckily for you, he's out on the porch in his rocking chair as usual."
    "He hasn't spotted you yet, but it's too late for you to turn back."
    e "Heya Arty! How's it going?"
    "At the sound of your voice, the somewhat chubby shepherd shifts his rocking chair over to look at you."
    "Already you see his eyes roam over your body, drinking in your figure. He has a small smile on his face, happy to see you take him up on his offer."
    show arthur normal with dissolve
    ar "Hey there, pup. You here to show an old man a good time?"
    "It seems that the old man is raring to go, despite his age. Already you can see a small bulge emerging from his trousers."
    "You do your best to give him a charming smile despite the nerves."
    e "That's the plan, sir."
    "Arthur's eyes light up at that word. It seems you've hit a button of his."
    ar "Oh my, already calling me sir. You don't mind if I call you pup then, right?"
    pause 1
    "You gulp and nod to him. Right now, all you care about is making the old man happy."
    ar "That's a good boy. It's good to see you're happy to be my pup."
    "There's a hunger in his chuckling voice. You suspect his bulge is reaching full mast, a long and fat piece of meat if the outline is anything to go by."
    e "Thank you sir, I'm glad I can make you happier. I do plan to do better though."
    "You're making your way up the stairs at this point. Arthur looks like he wants to reach out and grab you, but he seems to decide otherwise."
    scene barn_interior with dissolve
    show arthur normal with dissolve
    ar "Then you'll be back for this again, yes, pup?"
    "The bastard is already planning to make this a regular thing. It doesn't hurt to say yes for now... and it's definitely not out of the question."
    e "Yes, sir. As long as you want me back."
    "At this point the old man can't seem to take it anymore, his hands finally reaching beneath his overalls and into his pants to massage his cock, foregoing any sense of decency."
    ar "I planned to do this inside, and give you a proper rutting. Or see how you rut me, but..."
    "A hungry growl enters his voice."
    show arthur horny with dissolve
    pause 1
    ar "Since you're coming back, you'll be helping me by sucking my cock out here this time, alright, pup?"
    "It's good that Arthur has the presence of mind to ask. You can see his cock throb inside of his trousers, a dark spot already forming despite the thick material."
    e "I'd love to, sir."
    ar "Good boy. I knew you'd say that. Now... why don't you lose those clothes and kneel in front of me like a good little puppy."
    "Doing as he says, you strip each layer off your body one by one, until you're in nothing but your birthday suit."
    pause 1
    ar "Somebody's excited. I'll let you take care of that while you blow me. Though I'd recommend you didn't, because you'll be here a while. Don't want you running out of gas too soon."
    "You hadn't realized it before, but your cock is rock hard, a sight Arthur is more than happy to see."
    "Remembering your prior orders, you get on your knees in front of the Shepherd."
    "Arthur, satisfied to no end by the show you've given him, reaches down to cup your cheek gently."
    "Quickly, however, his other hand begins to undo his buttons, and unzip his pants. The hand on your cheek gets busy as well, shoving a finger into your mouth for you to suck on."
    "You oblige while you wait for the older dog to disrobe."
    "Before you know it, a fat red cock springs free from its confines, which Arthur immediately grabs the back of your head and pushes your face towards, removing his fingers."
    show arthur erected with dissolve
    "The Shepherd is excited enough to not even fully disrobe -- his clothes are half taken off, his only goal having been getting his cock out for you to suck on."
    "Despite that, you can see the mix of muscle and fat the old man has. A mix of a hard worker's body, and an old man who indulges in whatever food he wants."
    ar "Like what you see?"
    "The man says that with a self-satisfied grin. He knows you like it, and even if you didn't, that he's going to fuck you to his heart's content."
    "Helpless, you nod, his hand still against the back of your head."
    with vpunch
    e "Yes Si-"
    "In your moment of weakness, Arthur shoves your face onto his cock, pushing his tip into your mouth."
    with vpunch
    ar "Ah... that's more like it. A warm hole to put my dick in, and a pretty face to look at while I get my rocks off."
    "As he says this, he begins to push your head further down his cock, feeding more and more of it to you."
    "Thick, warm drops of pre spill out into your mouth, filling your head with the strong scent of earthy virility."
    show arthur norgasm with dissolve
    ar "You happy as I am down there?"
    "As you cannot speak, and the iron grip on your head prevents you from nodding, all you can do is let out a content rumble."
    ar "Good boy. I knew you'd be the perfect pup for me from the moment I saw you."
    ar "You're good enough that I think I'll have to knot you."
    "The dog seems so content saying that, you'd think he was in heaven right now."
    ar "What do you think, pup, do you want to get your muzzle knotted?"
    with vpunch
    "He punctuates his question by pushing your mouth up against his knot, a wide, intimidating thing so far down his cock you can feel his tip tickling the back of your throat even now."
    ar "Well?"
    "You break out of your fugue state and snap to attention, making your best attempt at a sound of joy as you can with a cock stuffing your throat."
    ar "You never disappoint."
    "Seemingly content with leaving things there, Arthur begins moving your head up and down his shaft, not in any particular rush to finish."
    with vpunch
    "He wants to take this at his pace, and have a good time."
    "After a few minutes of face fucking you, Arthur reaches over -- without letting you get off his dick -- and grabs a cigar, lighting it and sitting back to watch the farm as you serve him."
    with vpunch
    "The Shepherd says little, speaking only to tell you you're doing well, scratching your ears from time to time and making small sounds of contentment."
    "After thirty minutes of gently facefucking you, Arthur's pace begins to pick up slightly, his content sighs turning into short groans."
    "You can tell he's getting close, his unsteady breathing and sudden urgency letting you know that the old man wants release."
    "Luckily, that let you prepare for what came next, as Arthur began to thrust his hips up into your mouth, shoving his cock deeper and deeper into you, forcing your mouth to acclimate to his knot."
    with vpunch
    "Already, you can feel small spurts of pre shooting into your mouth as he struggles to hold himself back from cumming until he's well and properly knotted."
    with vpunch
    with vpunch
    with flash
    pause 1
    "Before long, he gets his wish, as a particularly hard pump of his hips drives the rest of his cock into your mouth."
    show arthur cum with dissolve
    "You feel rope after rope of cum hit your throat as the old man shoots his load as deep into you as he can."
    with flash
    "It takes minutes for him to finish, his powerful thrusts turning into gentle bobbing once more as his cock locks with your mouth."
    with flash
    ar "Woof. You know that a dog's most basic instinct is to knot a bitch so she has to stay and take it all?"
    ar "I'm pretty sure you would have stayed on my cock like a good boy, knot or not."
    "The older dog begins petting you affectionately as he waits for his knot to shrink."
    "You can't speak down here, so all you can do is gently nurse on his slowly softening cock. He seems to take this as encouragement to keep talking."
    ar "You're the best lay I've had in years, and I've bred a lot of bitches in my time."
    ar "And next time I'll be giving you a proper breeding."
    ar "I'm already looking forward to getting to rut you like a bitch in heat."
    "It's a long time until he speaks again, his knot close to slipping out of your mouth."
    ar "It really was a pleasure to have you over."
    ar "Next time I'll make sure to get you a treat for good behavior."
    "He meets the skeptical look in your eyes and chuckles softly."
    show arthur nstare with dissolve
    ar "No, I don't just mean my cock, though that too."
    ar "You'll see when the time comes."
    ar "For now, just enjoy a full throat and stomach."
    ar "And give Amble my regards."
    "As if knowing the exact moment he'd soften enough to get out, his cock slips out of your mouth as he says that."
    "You pull back and wipe your mouth with the back of your arm."
    pause 1
    e "I will."
    "Arthur gives you a small smile."
    ar "Thank you. I trust you had a good time?"
    e "I did, actually. Though I'm afraid I'll have to go for now. I didn't realize I'd be here this long."
    ar "I understand. See you next time, pup."
    pause 1
    "You quickly put on your clothes and head out, a smiling dog waving at you as you leave."
    "Long time or no, the main reason you hurried off is that you know given fifteen minutes, Arthur would be raring to go again."
    "The man may have cum, but he was incurably horny."
    jump main_backyard_barn
label Arthur_Second_Scene:
    $ arthur_encounter += 1
    stop music fadeout 1.0
    "Walking up to the farm wasn't as scary this time. Your heart was certainly still pounding, but it was with excitement, not nerves."
    "This time, the difficulty came from trying to walk with an erection."
    "You couldn't help it, you'd been thinking about all the things Arty might do to you all the way here."
    "He'd promised to take you further this time, and no erection was going to stop you from seeing how he'd go about that."
    "Just like last time, you see Arty in his rocking chair."
    show arthur normal with dissolve
    "This time, however, you see an odd bundle of rope or cloth next to him."
    e "Hello, sir! It's good to see you again!"
    "The German Shepherd turned to you, a deeply pleased smile already on his lips."
    ar "Hello, pup. It's a pleasure to see you around here as well."
    "Unlike last time, however, Arty immediately gets up to greet you, moving to the top of his steps before beckoning you over."
    "Happily, you obey the old dog, practically skipping your way up the stairs."
    "As you reach the top step, you stand directly in front of him."
    "He takes this opportunity to grab your ass greedily and push you against him."
    e "Art-mmph!"
    "Arty shuts you up by pushing his mouth against yours, kissing you hungrily, shoving his tongue into your mouth without hesitation."
    "Ceding any resistance to him, you melt into the kiss, back arching with the kiss as the dog's hands begin to grope your ass."
    "Arty breaks the kiss only momentarily, giving you a moment to breath, on purpose or not, you can't be sure - he himself uses the opportunity to growl at you assertively."
    ar "That's a good boy, pup."
    "Without warning, and without fully stopping his growl, he pushes his mouth against yours once more."
    "At first, it was only your erection pressing against his belly, but now you can feel his cock pressing against you as well, already grinding against you to pleasure himself."
    "Unsatisfied with just groping, Arty grabs the side of your pants before hesitating, and pulling away from you entirely. You lean towards him greedily as he pulls away, but give up as you see it is a full move."
    ar "I wasn't sure about this before, but now that you're here again, and reminding me of how good a pup you are, I'm sure."
    "The German Shepherd is giving you a smile that sends shivers down his back. It is a smile that tells you he knows how much you want him, and how much you'll let him do to you."
    "It's a smile of someone hungry to get that out of you."
    ar "Strip for me while I go grab something."
    "Obediently, you begin to take off your clothes as Arty moves towards the pile of rope you saw earlier."
    "As he picks it up, you see that it's a harness, collar and leash. Looking closely, the leash even has a tiny metal heart with your name on it."
    "He sees your look, and opens the harness as he moves towards you."
    ar "I thought that if you'd be my pup, you better look the part."
    "As soon as he reaches you, he begins to put the harness on you - a red flat-fabricked thing - with complete confidence, but with little enough force that you know you could stop him if you wanted to."
    "The thing is... he was right. You don't want to push him away. This is new to you, but it's making your heart race with excitement."
    "As he finishes up the harness, he attaches the leash to the collar before unbuckling it."
    "The horny old german shepherd presents the collar to you flat, so you can see all of its features. You can now see that tag with your name on it has his name and address on the back, labeling you as his property."
    ar "Wearing this means you belong to me. You'll be accepting me as your master, and acknowledging that your purpose is to please me."
    "You stare at the collar, wide-eyed. A glob of pre drips off of your dick and onto the floor. You barely manage to croak out a question without immediately accepting."
    e "Can I still continue being my own person if I say yes?"
    "Arty gives you an approving look."
    ar "Yes, you can. You can keep adventuring and meeting people, having relationships... everything. A part of you will always belong to me, but never will that inhibit the rest of your life."
    ar "I'll be your master, and part of being a master is taking good care of your pups. Do you trust me to take good care of you, pup?"
    "That's not a question. He knows the answer is yes, but he wants to hear you say it - to make you hear yourself say it."
    e "Y-yes. I trust you to take care of me."
    "Arty gives you a fond smile."
    ar "Good."
    ar "Now. As long as you wear this collar, you're mine, and mine to do with as I please, within reason."
    ar "I'm also not going to make you walk around with this everywhere, unless you want to. But, I'm going to need you to wear this at all times while you're with me, and have you obey me when you do."
    "The dog grins devilishly at you."
    ar "Not that I think obeying me will be an issue for you, pup."
    "Arty hands you the collar at this point, the leash still attached and held in his hand."
    ar "Now, with all of that out of the way, do you accept that I am your master, and you my pup? I think we both know the answer, but let's hear you say it for me."
    menu:
        "Is Arthur your Master?"
        "Yes{#arthurmaster}":
            "You gulp, nervous but excited, and dangerously aroused."
            e "Yes, please, be my master, Arty. I promise I'll serve you well."
            "The German Shepherd's smile makes you want to beg for him to just finish this already and let you be his, it lets you know he wants to play with his food a little longer."
            ar "Alright then, pup. Put it on."
            "Hesitantly, you bring each side of the collar up to your neck, your breath shaking. You somehow manage to loop the buckle despite your nerves, and finish standing there in nothing but a harness and collar, leaky cock twitching and throbbing."
            jump Arthur_Second_Scene_Yes
        "No{#arthurmaster}":
            $ arthur_2ndChoice = "No"
            "You gulp, dreading what comes next."
            e "No, I'm sorry. I don't think I'd like to get into something like this."
            "Arty is shocked by your answer, but he recovers after a moment."
            ar "That's unfortunate, but entirely understandable."
            jump main_backyard_barn

label Arthur_Second_Scene_Yes:
    ar "Now there's a sight I could get used to."
    ar "Come on, pup, I'll take you to a spot where I can give you what you want. Too many prying eyes out here. I'd do it if it weren't for the fine, though."
    "Arty says this as he marches down the steps, and begins leading behind the house, into the barn proper."
    e "I... have a question."
    "Your master looks back at you kindly at your worried tone."
    ar "You should never feel afraid to ask, or speak in general. I'll tell you if I'm unhappy, but you're a good pup, you'll be fine."
    "A relief, at least. Learning the rules will be a difficult, but rewarding task."
    e "Should I still call you sir? Or should I call you master now...?"
    "The two of you enter the barn at this point, Arty leading, and you obediently letting him tug you in. You're pretty sure you see your destination over in the corner, what seems to be a small living quarters."

    menu:
        ar "Both are good."
        "Master":
            e "I think I prefer calling you master."
            "Arty grins, putting a hand calloused from decades of farm work on your head, and gently petting you."
            ar "I'm glad to see you're already acclimating to your new role."
            $ arthur_2ndChoice = "Good"
            call Scene_Arthur_Yes from _call_Scene_Arthur_Yes
            $ pc.lust = 0
            $ pc.add_active_status(stuffed)
            jump main_backyard_barn
        "Sir":
            e "I think I quite like calling you sir - it's what I'm used to."
            "Arty gives you a satisfied look."
            $ arthur_2ndChoice = "Good"
            call Scene_Arthur_Yes from _call_Scene_Arthur_Yes_1
            $ pc.lust = 0
            $ pc.add_active_status(stuffed)
            jump main_backyard_barn
        "I should just call you Arthur":
            e "I don't want to call you either of those things."
            e "Last time I put up with it, but I want to call you Arthur."
            "Arthur stops tugging you forwards, instead getting a better grip on the leash, and pulling you closer."
            ar "You will call me master, or sir. Are we clear?"
            menu:
                "Yes{#arthurmasterask}":
                    $ arthur_2ndChoice = "Good"
                    "Yes, sir. I'm sorry sir."
                    "Arty stays there, looking at you."
                    ar "I will give you rewards as you earn them, but you will always, {i}always{/i} treat me with respect."
                    ar "Now. Tell me what you are."
                    "You lower your head slightly, only for Arty to raise it back up, pushing your chin up with his free hand."
                    ar "With pride. If you do well enough, I'll give you the treat I was planning to earlier."
                    "You almost let your head go back down in shame, but stop yourself just in time."
                    e "I'm your puppy, sir. I belong to you, and my job is to do my best to please you."
                    "Arty pulls on your leash to get you close for a kiss."
                    "As you lurch forwards, you're met with your master's snout, his tongue greedily plunging into your mouth."
                    "Before you know it, the kiss is over."
                    ar "Good boy."
                    "The old dog lets your leash hang loose once more, guiding you forward to it like before."
                    call Scene_Arthur_Yes from _call_Scene_Arthur_Yes_2
                    $ pc.lust = 0
                    $ pc.add_active_status(stuffed)
                    "..."
                    "You wake up to the feeling of extreme warmth."
                    scene barn_interior with dissolve
                    "However nice the cuddle was last night, the heat of day has made it nearly unbearable."
                    e "M-master."
                    "He continues to snore. You take a risk and speak a bit louder."
                    e "Master?"
                    "There is only a short break in his snoring before he continues like before."
                    "Unable to take the heat anymore, you yell loudly, consequences be damned."
                    e "MASTER!"
                    with vpunch
                    show arthur naked with dissolve
                    "Immediately, Arty sits up, his head swiveling back and forth in confusion. As soon as he spots you, he relaxes."
                    ar "Oh, right. I have a guest over."
                    "The dog gets out of bed with a little hop, and heads over to put his clothes on."
                    "You, on the other hand, stay in bed a little longer, thoroughly confused."
                    e "Aren't you mad I woke you up?"
                    "Arty slows down in the middle of buttoning his overalls."
                    ar "Hmm?"
                    ar "No, I'm a very deep sleeper. I don't particularly mind being woken up like that."
                    "He continues where he left off."
                    ar "A blowjob would be a welcome wake-up next time, however."
                    ar "It is good you did not do so this time. I hadn't allowed you to do so yet."
                    "Humming contentedly, Arty makes his way out into the farm."
                    "He calls back to you before he goes out of sight."
                    ar "Come into the house when you're ready! I'll be making breakfast."
                    hide arthur with dissolve
                    "The thought of food snaps you back into reality - the bellyful of cum you received yesterday was fantastic, but not actual food."
                    "It might have been a good breakfast had he cum in your throat, however."
                    "As you get up, you tap your throat, suddenly remembering the collar."
                    "Maybe this was a good decision after all. It's certainly been a fun time so far."
                    "You look around for your clothes briefly. It takes only a few minutes before you realize you left them outside."
                    "Quietly, you sneak forwards to the barn door. Once there, you make sure nobody is around before moving to the discarded pile of clothes."
                    "They're a bit dirty after 8 hours of sitting out in the open, but you put them on anyways."
                    "Confident that you have everything ready, you walk into your master's home."
                    "The rich scent of old wood fills your nose - this is a home that has seen several generations of use."
                    "On the walls near the entrance, you can see portraits of old dogs that look a bit like Arty."
                    "As you move further in however, you see one of your master himself, As well as many pictures of younger shepherd dogs - some clearly mixed with other species, but undeniably similar to him."
                    if arthur_breed:
                        "It seems he wasn't kidding about his litters."
                        "If these are his kids, he has a lot of them, and he seems to care quite deeply for them, if the little notes within the portraits are anything to go by."
                    "As you reach the end of the hallway, you see your master at the stove, a runny egg, spinach, cheese and bacon sandwich already in his hands."
                    "He spots you and opens the oven, taking out a sandwich identical to the one in his hands from inside."
                    show arthur normal with dissolve
                    ar "I don't know what you like, so I did my best to guess."
                    "You quickly find the sandwich pushed into your hands. A tentative bite fills your mouth with the savory warmth of well-prepared egg yolk and homemade bacon."
                    "The bite goes down faster than you'd like, but plenty of sandwich remains for you to enjoy."
                    e "It's great, thank you."
                    "Once again, the old dog begins to hum contentedly. He leans back on the counter as he eats his own sandwich."
                    if arthur_breed:
                        e "I saw the pictures on the wall. Are they all yours?"
                        "Arty gives you a knowing smile before swallowing his bite to respond."
                        ar "Yup! It can be pretty expensive to make sure they all have the money to live a proper life, but it's worth every penny, and hour of work."
                        ar "Even so, I'd spend as much as I had to if I had another with you. I had a lot of fun breeding you earlier."
                        "You choke on your bite of sandwich. It takes a bit for you to swallow it, but when you do, you see a devilish smile on Arty's snout."
                        e "Ahem. Thank you master, I'll keep that in mind."
                        "Your image of composure is somewhat ruined by your cock chubbing up a bit, but you did well enough."
                        "At least, that's what you thought before you heard Arty snort in amusement."
                        ar "I can see someone's already thinking about next time."
                        "Embarrassed, you focus on eating your sandwich, and {i}not{/i} on the thought of last night."
                        "Arty lets up on you, but you can see his own bulge out of the corner of your eyes."
                        "You get the feeling that the only reason he's not fucking you over the table and giving you another filling right now is out of consideration for your sore hole."
                    else:
                        e "So, what do you tend to do in your free time, sir?"
                        "The shepherd dog shrugs, swallowing the food in his mouth before replying."
                        ar "Most seasons, I work for most of the day - making sure the farm stays healthy and running is time consuming, even with folks like Amble and you helping keep things safe."
                        "He sighs, thinking about his work."
                        ar "Right before the harvest season, like now, is when I'm most free - all I really have to do is watch and make sure nothing tries to eat my crops."
                        "He takes another bite of his sandwich, giving you time to reply."
                        e "But what is it you do during this season, master?"
                        "This time, it takes a while for him to respond, though that may be because he wants to savor the sandwich in his mouth."
                        ar "I watch the plants, read, fuck, sleep, watch the plants again... boring, maybe, but it makes money."
                        ar "Plus, I don't mind how relaxed it is."
                        "There's a hungry glint in his eyes."
                        ar "Or what it does to my body. There's a lot you can do with strength and weight."
                        "You certainly felt the effects of both of those last night. You can feel yourself chubbing up a little thinking about last night."
                        "It seems Arty is doing something similar, going by his growing bulge."
                        "You get the feeling that the only reason he's not fucking you over the table right now is out of consideration for your sore hole."
                    ar "I have something to give you before you leave, actually."

                    "Arty finished his sandwich in four bites, a terrifying feat given the size of the sandwich."
                    "Dusting his hands, he heads off to somewhere outside."
                    "Privately thankful that he stopped before he actually did fuck you, you try to finish your own sandwich before he gets back."
                    "It really is delicious - The only way it could have really been improved on was adding some fresh tomato slices."
                    "You sit on the counter to wait for your master after you finish your sandwich."
                    "Before long, he's back with a... purple vegetable in his hands? It looks like a radish, but much smaller, and purple."
                    ar "I think this might help you on your adventures. You did a good job last night, so I figured you deserved something like this."
                    "The old farmer passes you the odd root vegetable. Unsure of what to say, you accept it, awkwardly holding it in your hands."
                    "It's surprisingly heavy."
                    e "Thank you master, I really appreciate it!"
                    "You mean what you say, but you also have no idea what the hell this is."
                    "The Shepherd Dog chuckles a bit, and pats you on the leg."
                    ar "I like the enthusiasm, but you {i}can{/i} ask me about it - I don't want to be a stifling master to you."
                    "Carefully, very carefully, you nod to him, trying to find a polite way to say 'what use could an odd radish possibly have."
                    "He'd probably appreciate honesty, when you stop and think about it."
                    e "While I am very happy to receive a gift from you, I have no idea what this is, or how to use it. Could I have some hints as to either?"
                    "Arty nods approvingly to you, letting a finger from the hand on your leg brush up against your balls gently."
                    ar "Mhmm. It's a Purple Panacea."
                    ar "Before you get excited, it doesn't actually cure literally everything, but it should help close any non-lethal wounds and give you a pick-me-up when you eat it."
                    e "H-how much would this go for on the market?"
                    "Arty flashes you a grin."
                    ar "A couple thousand gold coins."
                    "You feel your eyes widen in shock."
                    e "Are you sure you should give me something so expensive?!"
                    "Your master just brings a hand up to your chin, and rubs it gently."
                    ar "I told you I'd take care of you if you did well, pup."
                    ar "This is my main cash crop, and I grow quite a few every year. It's the reason I'm this strong, and have to keep such a close watch on my fields. Monsters, animals, bandits... lots of things want 'em."
                    ar "But I work hard to grow the bastards, so I get to decide what I do with them."
                    "You gulp, and put the Purple Panacea into your inventory."
                    $ addItem("Purple Panacea", inventory, 1)
                    "He steps away from you, content with what he's given you."
                    ar "Now, while I'd love to stay and talk to you all day, you'd walk out of here limping."
                    "You're about to open your mouth to say that that wouldn't be too bad, but quickly shut it as you realize that he is liable to fuck you until neither of you can move anymore."
                    e "Alright, sir. I'll be on my way then."
                    "You walk towards the door to the hallway. Just as you pass by Arty, you feel one of his hands cup your ass as you leave."
                    "Well, he can do pretty much whatever he wants to you, as per your agreement."
                    "Pretty good deal all things considered."
                    "Unfortunately for you, it's time to get to work."
                    "You do a few stretches once you get outside, working out all of the sore spots from what Arty did to you, and move back out onto the road."
                "No{#arthurmasterask}":
                    $ arthur_2ndChoice = "Bad"
                    e "I don't want to. I'm going to call you Arthur."
                    "Arty's eyes narrow. He grabs your leash so you have little space to move around."
                    ar "It sounds like somebody's being disobedient."
                    "Your master begins to drag you over in a different direction from before, towards some hay bales in the corner. Unlike the gentle treatment you received before, Arty is forcing you forwards by the neck."
                    ar "Do you know what we do with disobedient puppies?"
                    "You open your mouth to answer, only for Arty to sit on one of the bales, and tug you down with extreme force."
                    "Unable to keep your balance, you fall forwards, across the shepherd dog's lap."
                    ar "We punish them, until they learn how to serve."
                    "Arty punctuates this by tugging your collar in the other direction, preventing you from falling over, but also pulling against your throat."
                    ar "Now. What do you call me?"
                    "Unwilling to bend on this point, you speak in defiance."
                    e "Arthur."
                    ar "{i}Wrong.{/i}"
                    "Arty shoves his right hand between your shoulderblades and presses down, as he tugs on your leash."
                    "The resulting effect is that the collar around your neck is digging into your throat, completely obstructing your breathing, while his other hand keeps you down."
                    ar "You call me master, or sir."
                    "It is difficult to hear him, your mind trapped in the feeling of choking with no way out."
                    ar "You are mine, and you do as I want."
                    "He still isn't relenting. You can feel a painful pressure against your stomach."
                    "He's enjoying this as much as he enjoyed fucking your mouth."
                    "Right when you see spots in your eyes, Arty ceases to asphyxiate you, letting the leash lay a bit slack."
                    ar "Say it. Say who I am."
                    "You barely manage to croak out a word."
                    e "...A-Arthu-."
                    "Once again, the collar digs into your throat."
                    "This time, the dog seems to have no words for you, grimly watching as you grow weaker on his lap."
                    "You feel woozy from the lack of oxygen. Some deep, fucked up part of you is enjoying this, and you can't tell whether to love or hate that."
                    "As if sensing your moment of weakness, Arty removes his hand from your shoulder blades."
                    "The collar still presses against you, but the absence of the hand gives you just enough space to sneak in the air you need to stay woozy, but nothing more."
                    "In the corner of your mind, you hear the sounds of Arty unbuckling and unbuttoning his clothes. You feel his overalls fall over your back."
                    "Finished with disrobing, Arty forces you up and off his lap by the leash."
                    "He stands up, his clothes falling down to his ankles. Revealed underneath is his long, fat cock, completely covered in precum."
                    ar "You don't deserve the lube. I should fuck your mouth first, and clean it off in there, but you've left me impatient."
                    "The shepherd dog forces you back onto the hay bale, standing over you now."
                    ar "I'll give you one last chance to redeem yourself even a little. Raise your ass so I can fuck you."
                    jump Arthur_Second_Scene_NoNo

label Arthur_Second_Scene_NoNo:
    menu:
        "Reject":
            $ arthur_2ndChoice = "Noo"
            "Coughing, you shake your head."
            e "No. I don't want to do this."
            "Arty's eyes widen at that. It seems this wasn't at all within his expectations."
            ar "Alright. I'll leave you be then."
            ar "I think I misjudged what you're into."
            "Immediately, Arthur lets go of the leash, and steps back."
            "It's a struggle to sit, your arms are slow to react to your commands. Eventually, they do listen, and you sit there, cock hard, but feeling altogether miserable."
            "Arty is already putting on his clothes in front of you."
            ar "I'm going to go get you water."
            "With that, he's on his way out."
            "It's a good thing too, you need the time to get yourself back in control."
            "Slowly, you bring enough air into your lungs, and your mind begins to return to normal function."
            "Soon after, Arty comes over with your clothes, and a canteen of water."
            ar "I'm sorry about what happened. I know that no apology will really make up for it, but... I didn't mean to hurt you in a way you didn't like."
            "You grimace internally. The man's words sound genuine, but he also just choked you for a few minutes over a small slip-up."
            "Then again, choking is a fairly common kink within certain communities."
            e "I forgive you. Just... don't do that again."
            "Arty nods."
            ar "Of course. I don't think the master-pup situation is a good fit for the two of us after this, anyways."
            ar "There's no point in it if you don't enjoy it as well."
            "You take a deep breath and get up. Misjudging the strength in your legs, you tilt over and nearly stumble, but Arty catches you and hands you your clothes."
            ar "Are you alright?"
            "It's a bit of a stupid question, but you can tell he's asking if you need him to fetch you medicine."
            e "I'll be fine."
            "Arty lets you go, and shifts awkwardly."
            ar "I'm going to leave you be now. Sorry, again."
            "There isn't really anything to say to him. You give him a nod as you put your clothes on."
            "The dog makes his way outside. You follow shortly after, heading home."
            jump main_backyard_barn
        "Comply":
            call Scene_Arthur_NoNo from _call_Scene_Arthur_NoNo
            $ pc.lust = 0
            $ pc.add_active_status(stuffed)
            jump main_backyard_barn
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
