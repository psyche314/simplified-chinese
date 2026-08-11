
label start:
    call after_load from _call_after_load
    $ addItem("Storage Room Key", inventory, 1)
    $ addItem("Small HP Potion", inventory, 1)
    $ addItem("Tribe Loincloth", inventory, 1)
    $ addItem("Tribe Necklace", inventory, 1)
    $ addItem("Short Sword", inventory, 1)
    $ el = "Tenki"
    $ renpy.music.play(mOpen1, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ equippinginitial()
    scene black
    with dissolve
    jump Puro_Beginning_Talk

































































































































label Sebas_First_Meet:

    "..."
    "Everything fades to darkness, as your consciosuness slips away."
    "The last thing you thought of were Chime, maybe you had fallen the same fate as him."

    "You don't know how much time has passed, minutes, hours."
    "You don't know how many sun and moon passed right above you as you slumber."
    "You don't even know where you are."
    "Everything became so fuzzy after you fell."
    "You can't even remember how you fell, or why."
    "It's all futile, everything is gone. You are gone."
    "..."

    "..."

    "It's the sound of water, flowing around you, for a long while your consciousness is just floating in the sea of nothingness."
    "You have had a long dream in this void, but you can't even remember what it was about."
    "Your memory is fading away, emptiness fills the space where your mind used to be."
    "It doesn't even feel like it is the first time to forget everything."
    "Hezzong, the tribe, and the forest, everyone is gone."
    "Time doesn't matter now, you are not sure if you're still alive."
    "Maybe you are already dead, and this is the afterlife. Afterall, who would survive a fall like that?"
    "You can't even feel your body, you can't even feel your heart beating."
    "But somehow, you persist."
    pause 1.0
    "..."
    $ abilities = [selfheal, fortifying, None]
    $ renpy.music.play(mForest, loop=True, fadein=2.0, fadeout=2.0)
    "You are not ready to open your eyes yet, but you can hear the forest's music."
    "..."
    "And then you hear a bright male voice blabbering around you."
    "His young voice is definitely opposite from the rough voice of the figure before."
    my "..."
    my "You waking up yet, you know... you shouldn't have slept in."
    my "Especially in the middle of a forest like here."
    "You wish for him to shut up, or take your belongings so he can leave you alone."
    my "A grown up boy like you should know there's a lot of dangerous monsters out there."
    my "As my ma said, Safety is always your number one priority."
    my "She also said not to trust any strangers so easily, especially those who sleep in the forest."
    my "but oh well... you know what they say."
    my "You snooze, you get slapped in the ass!"
    my "...and lose, of course."
    "You wonder if this is what hell sounds like, endless blabbering like a fly buzzing around your ears."
    my "..."
    my "Okay, it's time."
    my "Hey. Wake up."
    m2 "WAKE THE FUCK UP!!!"
    m3 "WAKE THE FUCK UP!!!"
    "As much as you don't wish to open your eyes yet, you feel that he's not going to stop until so."
    scene forest
    with fade
    pause 0.5
    scene black
    with fade
    pause 0.5
    scene forest
    with fade
    pause 0.8
    scene black
    with fade
    pause 1.0
    scene forest
    with fade
    pause 0.5
    show sebas normal
    with dissolve
    my "Good... Fucking Morning, Stranger."
    my "See, you probably have a job but it is not that hard to get up on Sunday, I know."
    "You see a fluffy lion grinning in front of you, he wears a leather messenger bags with odds and ends inside."
    "His soft fur is messy but he looks charmingly handsome."
    yu "...what?"
    my "Hello, little snoozy ass."
    my "My name is Sebas, in case you don't know."
    show sebas grin
    with dissolve
    s "I'd say... you look like some other goat folks... There's no problem with that though."
    s "Apart from sleeping in the middle of nowhere, of course."
    s "and you look a little scruffy, dare I say."
    "He chuckles uncontrollably, looking at you up and down."
    s "..."
    s "So..., what's your name, buddy."
    "You scratch at the side of your head."
    jump name

    label name:
        yu "Uh..."
        python:
            el = renpy.input(_("What's your name?"), length=20)
            el = el.strip() or __("Tenki")
        menu:
            "Is your name [el]?"
            "Yes{#name}":
                $ e = Character("[el]", who_color="#ffffff", who_outlines=[ (2, "#000") ], image="player")
                $ persistent.player_name = el
                jump namedetermine
            "No{#name}":
                jump name
    label namedetermine:
        if el == "Ole" or el == "Sebas" or el == "Cane" or el == "Lothar" or el == "Rahim" or el == "Furkan" or el == "Haskell" or el == "Wuldon" or el == "Vurro" or el == "Uffe":
            e "My name is... [e]."
            s "[el]? No. You can't call that. I'm 99 percent sure uhh... that's not your name."
            e "Wait, why can't I call... [e]?"
            s "No, No, No. Get another name."
            e "..."
            jump name
        if el != __("Tenki"):
            jump name1
        else:

            jump name2
    label name1:
        e "My name is [e]..."
        s "[e], that's a good name! Isn't that right?"
        jump name_done
    label name2:
        e "My name is [e]..."
        s "[e]... Seems like I've heard it before... that's a little mysterious name! Isn't that right?"
        jump name_done
    label name_done:
        s "Anyways, Mr. [e]. You seem to be a little exhausted after your deep sleep."
        s "Had a bad dream?"
        e "No... I don't think so...?"
        e "Where am I?"
        s "The green forest of course, the greenest forest out of all forest in Mokken."
        e "Mokken?"
        s "Hmmm... You're not from here? Now that I thought of it, you do sound a little different..."
        s "But... anyways, where are your clothes?"
        e "Ehh?"
        "You look at your naked form, your tribe cowl has disappeared... the only thing remaining is your necklace lying on the grass nearby."
        e "Where are my... clothes?"
        s "I don't know. Where have you been? Had a sexy night with a handsome fella?"
        e "I can't remember much before. The stranger, I saw him in the forest in the middle of the night."
        e "He was talking in some strange language..."
        show sebas normal
        with dissolve
        s "Wait... you saw a stranger?"
        e "I don't know what it is, I have never seen that before."
        s "How did he find you?"
        e "It was in the middle of the night, I was walking in the forest."
        if on_watch_post:
            e "I was... I was on the watch tower, I was supposed to be the watcher tonight."
            e "And then I saw a flash of light, and I ran towards the source."
            e "I was hoping to find Chime, but it was him..."
        elif spriteling.lose > 0:
            e "I was fighting the spritelings, and I wasn't faring well."
            s "Spritelings?"
            e "Ghosts, they are like ghosts, but they are not."
            e "And when I woke up, he was already there."
        elif spritebinder.lose == 1:
            e "I was fighting the spritebinder, and I wasn't faring well."
            e "When I was about to lose, I saw him."
        elif spritebinder.lose == 2:
            e "I was fighting the spritebinder, and I wasn't faring well."
            e "Uh, after that... he was there."
        e "I don't know what he did to me, but I only remember falling from the sky."
        s "So, that means you're one of the outsider goats, right?"
        e "What outside? I'm... a dragon from the Puro Tribe."
        s "Dragon? I don't think I've ever saw a dragon like you, [e]. You look like a goat pretending to be a dragon."
        e "There are dragons who looks like a wolf? Like Chime. But we call ourselves dragons because that's what our tribe is."
        s "So, what's there outside of your tribe? Another tribe? A town full of people?"
        e "Now that I think of it, I don't think I've ever been, outside, outside. I spent my whole life in my tribe."
        e "Is Hezzong here? I need to find him."
        s "Uh? Who's that? Your boyfriend?"
        e "No, he's the elder of my tribe."
        "Sebas scratches his chin."
        s "I did hear something about a Hezz... something."
        s "Uhhh... Hezzong? Where did I hear this name before. I could've swore it came up somewhere, maybe the goats across the river know something."
        s "But I assure you he's not cheating on your tribe... thing. But I don't actually know because I haven't met him yet."
        e "He's Chime. I need to bring him back."
        s "Do you know how to go back?"
        e "N-no... I don't know."
        s "Hey, if you can go back to wherever you were. I would pray for you and your tribe, but I don't even know where to begin with."
        e "Maybe I can begin by finding Chime. I have a feeling he's somewhere here."
        "Sebas chuckles."
        s "Hey, I like your spirit. But you're not going to find him in the forest, especially not in the middle of the night."
        s "Oh, what's that thing under your head?"
        "You flinch as Sebas moves you around, he gently sweep through your head with his hands."
        show sebas scared
        with dissolve
        s2 "AHHHHHH!!"
        e "Tsssk, you're hurting me..."
        s "Hey, [e]... It's bleeding, the back of your head... I think."
        "Sebas' hand trembles but he still holds your head tightly, preventing blood loss from your head as he looks around."
        "You try to open your eyes a little wider to stay awake."
        s "Ahhhhh! Don't fucking die now."
        "He sits on the forest floor and raise your head on his laps, brushing against your head tensely."
        s "Hey, d-don't fall asleep! That's what my ma said too when I was sick."
        s "My dude is nearby, he is coming, we're supposed to meet here. J-just wait a second, okay? We good?"
        e "o-ok. I- uh... I'm fine."
        "Sebas looks distressed, completely different from the lion a few minutes ago."
        "It doesn't feel as bad as how he reacted, but you can see blood around him."
        "You can barely move your head, unable to shift your gaze from his glimmering eyes."
        show sebas scared at l1
        with move
        show ole normal at r2
        with move
        show ole normal at r1

        my "Seb, what's wrong with-"
        show ole shocked
        with dissolve
        s "H-hurry the fuck up... this guy needs some bandages."
        my "He... Where did you find him. Alright, hold him tight."
        "A lizard comes into your view, the clothes he has on looks like one of the custodians you had in your tribe."
        "The lizard holds your head up with his giant green scaled arm while taking out a roll of bandages with the other."
        "The white gauze instantly turns red as soon as it touches your head."
        "He carefully avoids the blood from leaking further as the bandages are wrapped around your head a few times."
        show ole normal
        with dissolve
        my "This should stop the bleeding for a while."
        my "You feeling okay?"
        e "Yes... thank you so much."
        my "No, don't thank me yet, I haven't treated the wound yet."
        s "But is he alright now?"
        my "He's fine."
        show sebas normal
        with dissolve
        s "Hey, that's my fucking Ol, gifting us mere mortals with his kind blessing."
        my "Very funny, what's your name, kid?"
        e "My name is-"
        s "He's [e]! And this lovely lizard in front of you here is Ole."
        o "Alright."
        o "Hey Seb, why don't you get me and [e] over here some herbs. We're gonna need some ointment before he can quickly heal up."
        s "Gotcha! My her-ooooooo."
        show sebas normal at l2
        with move
        pause 0.5
        show ole understand at c1
        with move
        "Ole gawks at him as Sebas leaves for some herbs. He is much more gentle with you, you don't know why but you feel a lot safer in the hands of this stranger."
        o "Don't mind him, he's such a moron sometimes. But he's a good lion."
        e "You're right."
        o "Heh, good that you can talk pretty well now. I presume you aren't from our province right?"
        e "Uhmm, I'm from Puro... but where are we?"
        o "This is Mokken. You're one of that outsider we heard?"
        e "Yes... I think. Is this really Mokken? The trees are so different here."
        "You look around, the forest is indeed filled with trees and bushes you have never seen before."
        o "It is, because you are definitely not from lizard tribe, or the goats, or anywhere else I know of."
        o "Now, that makes two outsiders. I wonder if there's more of you."
        show ole grin
        with dissolve
        e "Uh, I don't think so, unless that stranger send the other people here."
        o "Ha... maybe you guys can settle around here if the whole tribe comes, but I doubt the werewolves would like that."
        o "So, what's your plan now? You're not going to go back to your tribe?"
        show ole normal
        with dissolve
        e "I want to find Chime, and then go back, but I don't know where I can go."
        o "Hey, I don't even know where your supposed Tribe is. Stay with us. Seb and me live in a little village nearby, we can spare you a room there."
        e "...I need to bring him back to my Tribe."
        o "Wait, you meant the other outsider?"
        e "Yes."
        o "He, honestly I don't even know where he is now."
        e "I thought uh, the lion... Sebas told me he's in a goat tribe?"
        o "He left them some time later, as of a few days ago. I hadn't hear from him since, I assumed he found a way to go back?"
        e "Oh... fuck, then why am I here."
        o "I don't think a way would be found so easily, maybe he's still out there."
        o "And if he did find a way, then I think you can too. Don't you think?"
        e "Maybe, but I can't stay here long, I... I already missed the bed back in my tribe."
        o "Like I said, stay with us. We'll try to hatch a plan while you recover for a while."
        o "I just don't want you to get lost in the wood before you go back, okay?"
        e "Okay."
        "You glance at Ole's drowsing eyebrows, you can't help but to listen to the big lizard. He quickly picks up on your gaze."
        show ole grin
        with dissolve
        e "Hmmmph..."
        "Ole snickers a bit while bringing you closer to him, and your thoughts are instantly overflowed with his warmth and odor."
        "When you turn your head around, you see a shaggy figure from afar holding some shrubs."
        "It's Sebas. He quickly approaches as soon as he sees you two."
        show ole normal at r1
        with move
        show sebas normal at l2
        with move
        show sebas normal at l1
        with move
        s "Seems like you two are getting very along!"
        "Sebas winks at both of you, he gives Ole the herbs to make some ointment and quickly applies them on the back of your head."
        with vpunch
        "Your wound suddenly boils with intense pain and anguish, you let out a long scream while Ole and Sebas both give you a concerned look."
        "After a few minutes of suffering, the head pain quickly subsides and turns numb."
        o "You feeling alright?"
        e "Yeah, the medicine worked."
        o "Good! Time to get up and see if you can walk."
        s "You sure he can walk with that in the head?"
        o "Yes, have you never gotten one of my ointment before?"
        show sebas grin
        s "I mean I have never had that serious of an injury like this."
        "Ole squeezes your left hand and pull you up, your legs are still weak."
        "You stagger a little before Ole immediately lets your body weight presses on his rippled chest."
        o "Take it slowly. We have a lot of time."
        "Slowly you begin to regain some strength in your body, every step becomes easier than before, and with Ole's help you can quickly walk normally."
        s "Looking good, buddy."
        e "Thank you so much, Ole."
        s "Hey, what about me?"
        e "Thank you to you too! Sebas."
        "Sebas grins wide."
        o "[e] still needs some patching up work to do, injuries like this is going to affect his head for some times."
        o "How about we sweep our storage room and free up some space for him?"
        s "Wooah, new roommate! I like your idea."
        e "Really? You two are letting me sleep in your house?"
        show sebas normal
        with dissolve
        s "Yeah, why not? There's literally too much space for us since his friend moved out."
        show ole stare
        with dissolve
        o "Hey Seb, stop bringing random people up in front of [e]."
        s "If your friend is here, I think our new friend will be the first to kick his ass, and teach that sucker a lesson."
        o "You know what, I think [e] would be kicking your ass first. And then kick you out of the house."
        s "Hey I own the shop, ok? You can't fucking kick me out."
        e "Hey, who are you talking about and why am I suddenly kicking people's asses."
        o "I don't know, ask the lion."
        s "It doesn't matter now. Come on, let's get [e] home. We have a lot more to show around our store."
        "Sebas grins wide again and gives your back a few big pat, Ole stares at him for a few seconds before continuing on the path."
        scene black
        with dissolve
        scene lusterfield02
        with fade
        show ole normal at r1
        show sebas grin at l1
        $ renpy.music.play(mLusterfield, loop=True, fadein=2.0, fadeout=2.0)
        "After a few minutes, you have arrived at the village of Lusterfield, the houses and dwellings are dominated by white and orange colour."

        "You have never seen a civilisation like this before."
        "You take a deep breath as you smell the scent of fresh air and green grass."
        "The bustling village is filled with all kinds of locals walking around."
        s "Welcome to the village of Lusterfield, our village is fucking amazing!"
        s "It's chilling and you.. uhh. the village you live to love!... love to live!"
        o "That's the most coherent thing I've heard from him."
        s "What?"
        e "I don't think he's dumb."
        show sebas grin
        s "That's right!"
        show ole stare
        with dissolve
        s "Hey thanks buddy, finally someone who can understand me!"
        e "I can understand you perfectly."
        o "Don't stroke his ego that much, kiddo."
        s "You know what, that lizard here is jealous that I got to be your first friend in Mokken."
        s "So as a really friendly friend, you should be calling me Seb now, as a term of endearment."
        e "Oh! Alright Seb!"
        s "Hehe, good boy."
        o "Come on, kid. Let's get you to the bed first, I'll take care of the lion later."
        s "Hey what do you mean?"
        o "You will get what I mean. [e], let's go."
        scene lusterfield01
        with fade
        show ole normal at r1
        show sebas normal at l1
        "You arrived at the entrance of Sebas and Ole's shop, in the corner of your vision you see a wolf standing alone in a distance, staring at the three of you."
        "He seems curious, if not cautious. You quickly avert your gaze back to the duo."
        s "Here it is! The magnificent sign, {size=-10}made by me by the way{/size}. Isn't it beautiful?"
        e "Oh? It's looking good!"
        s "I told you so Ole, everyone loves it."
        o "Our kid here's just being polite."
        s "Why're you calling [e] kid. He looks at most only a few years younger than you."
        s "[e], hey. This weirdo lizard here is only 27. Don't get fooled by his croaky voice."
        "Sebas points at Ole, while whispering to you."
        show ole bored
        with dissolve
        o "Seb, did you really think I can't hear you from over here."
        "Ole puts his left fist behind Sebas's back, striking him forcefully with the knuckles of his hand."
        show sebas shocked:
            linear 0.1 xalign 0.0
            linear 0.1 xalign 0.05
            linear 0.1 xalign -0.05
            linear 0.1 xalign 0.05
        s2 "STOPPP, A-ALRIGHT. I GET IT, TOUGH OLD GUY. STOPPP!"
        "You look in shock and surprise as the lion gets his spine slammed, slumping forwards instinctively as Ole laughs and looks back at you."
        show ole smile
        with dissolve
        o "Good. Anyways kid, why don't we take a look at the store."
        e "Ok...?"
        "You follow Ole closely, while glancing backwards at the lion still hunching and nudging at his back."
        scene kings_pawn
        with fade
        show ole normal at r1
        show sebas normal at l1
        o "Welcome to the King's Pawn. We sell general goods and we do a little pawning!"
        s "Hey! Stop stealing my lines."
        show sebas bored
        o "Anyways, the storage room is over there in the back, it already came with the wooden bed someone sold us earlier. Seb will tidy it up for you."
        s "What, me? Isn't it your job?"
        o "Hey! No talking back in front of our guests."
        s "...this fucking lizard."
        "You can only see Ole fiercely stares back at Sebas without a single word, before the lion quickly slip away into the storage room."
        show sebas bored at l2
        with move
        hide sebas bored
        show ole normal at c1
        with move
        o "So, what do you think?"
        e "This place looks cozy, think I can stay here forever."
        o "Oh? You're not going home?"
        e "Uhh- No... That's just exaggeration, but I really do appreciate the place you have here."
        "You awkwardly smiles at Ole, who stands beside you and pats your back."
        o "Hey... you can definitely stay as long as you wish. Our Seb here have been wanting a company for a long time you know."
        e "What really? He looks like the type that attracts a lot of friends."
        o "Well... it's still good to see new faces around here, the village is too small, you often see the same faces here once or twice per day."
        o "Enough about him, if you want to repay us while you are here, there's a job you might be interested."
        show ole understand
        with dissolve
        e "What's it?"
        o "We have a lot of goods that's waiting to come to the shop recently."
        o "So, we would be very grateful if you can be our courier, and deliver those wares between us and our clients."
        e "Oh... That sounds easy."
        o "The thing is, it's not that easy. The forest is not safe anymore."
        o "Ever since that someone brought your Chime into our land. A lot of monsters and wild folks are emerging in the wilds. It's a dangerous job if you presume."
        e "You can count on me, Ole. I'm a good fighter."
        e "Maybe I can look for Chime while I'm at it."
        o "That's good to know, kid! Then I'll talk to Seb later, he will give you a messenger bag and map and other materials."
        show ole normal
        with dissolve
        o "We also have a fighter in the village, Lothar. I will ask him to give you some basic training, before you head outside the village."
        o "I'll think about the detail later, but the point is to prepare you before you try to go back to your tribe."
        o "You should rest for now, though. The wound is not going to heal itself-"
        my "Ole, who are you talking to."
        "You hear a mysterious gruff voice from upstairs, you turn your back to the stairs and notice a beefy figure walking down and with his hand along the rails."
        "As the figure reveals himself, you see a brown bull with curly hairs, his left hand holding tape measures."
        show ole normal at r1
        with move
        show rahim normal at l1
        with move
        show rahim normal at l1
        with move
        o "Good morning, Rahim, this guy is [e], He's moving into our shop today."
        r "Where did you find this goat, Ole? Don't tell me you invited those people here..."
        o "From the green forest down south, Sebas and I found him lying there. He is an outsider dragon, so we thought we'd bring him here to be our courier."
        r "Courier? Didn't that fox courier from the town disappeared last week?"
        o "Yes, that's why our village should need one for our goods, and your textiles as well."
        r "I suppose."
        r "Greetings. [e]. I'm Rahim, the tailor of the village."
        e "Nice to meet you, Rahim."
        "You look between Ole and Rahim, trying to force a smile on your face as Rahim suddenly gives you an intimidating look."
        r "A dragon... huh. Didn't know you kinds have this much fur."
        "Rahim quickly brushes you in the waist, the old bull wraps the tape around your body and tighten it up with a pull, you lightly gasped before he takes the tape away."
        e "Ouch! What are you doing?"
        r "Measuring your waist."
        o "Our Rahim here is a very talented tailor. He worked for the King of Mokken as well."
        o "He can create any fitting clothes and equipment that makes you feel like heaven."
        "Rahim gives Ole a weird look, scoffing off at his compliment."
        r "43 inches, did you eat a lot lately?"
        e "Hmmm... No?"
        r "Well then you're really fit as a butcher's dog, aren't you."
        e "U-uhhhh...Thank you?"
        "The tailor puts his tape measure away and turns to Ole."
        r "Ole, I thought you and Sebas were out delivering materials today so I checked out your little place, your orders are upstairs."
        o "Thanks, Rahim. I'll get you the money right away."
        show ole normal at r2
        with move
        "Ole quickly walks towards the cash register. Rahim glances at you for a moment, before turning back."
        r "I'll make you a leather armor, it's going to take a couple days, if you want the armor, just go to my place across the road."
        e "O-ok! Thank you so much, Rahim."
        show ole normal at r1
        with move
        o "Here it is."
        r "Good. See you tomorrow, boy."
        r "And you, new lizard, no hanky-panky with the two while I'm away. Got it?"
        e "Yes... Sir."
        r "Good, see you boys around."
        "The bull steadily tramps outside, giving you another look before closing the door."
        hide rahim normal
        "You can still feel the heavy aura and scent he left behind, you and Ole went silent for a few seconds."
        o "So... how do you feel about Rahim?"
        e "I don't know. He's a serious guy for sure."
        o "He had some beef with the goat. You'll get used to him."
        "You hear some loud clanking sound emitted from the storage room, with a roaring sound a few seconds after."
        show sebas normal at l2
        with move
        show sebas normal at l1
        with move
        s2 "Hey [e], the room is ready!"
        "You see a sweaty and exhausted lion walks out of the room, clearly unaccustomed to all the hard cleaning work he did for you."
        o "Alright kid, get in the room and take some rest. We can talk later."
        e "Thanks Seb."
        "Seb chuckles for a while, You can feel he could hardly hide the elation in his eyes."
        s "You're welcome, buddy. Sleep tight!"

        "You waves to them back and quickly walk into your new room."
        scene bedroom
        with fade
        hide ole
        hide sebas
        "As soon as you open the door, your eyes are immediately fixated at a lion plushie, its belly lies a card saying \"Welcome to your new room! [e]\"."
        "Your heart is instantly melted by Sebas' tender roomwarming gift, You put it at the front of your bed and quickly get in the blanket."
        s2 "HEY, HOW'S THE ROOMMATE OVER THERE."
        "A roaring sound, a mix between excitement and warmth, comes from outside the room. You instantly recognise it as the lion's shout."
        e "I'm fine! The gift is incredible! Thanks Seb!!"
        s2 "Good! I made it last year, just picked it up from the storage, thought you'd probably like that in your room."
        s2 "I have a spare one too, for if you want to get bring me with you outside!"
        s2 "Ouch! Ole here is pinching me now. Gotta let you go to bed. Have a nice sleep, new roommate!"
        "You can still hear Sebas and Ole mumbling outside fondly, You try to listen to them but you find yourself slowly slump over the bed."
        "Without knowing, you drift away to sleep very quickly..."
        scene black
        with dissolve
        "..."
        $ timenow.day = 1
        $ timenow.hour = 8
        $ timenow.minute = 5
        jump bedroom_beginning
    label bedroom_beginning:
        $ wilderness = False
        scene bedroom
        with fade
        "You wake up full of energy, you try to clutch the back of your head but the wound apparently had already healed itself over the night."
        "You glance at the drawer and found a brown leather bag, with a journal and a piece of map inside. (You can access them at the bottom right corner of the screen.)"
        "You feel ready to start the day."
        show screen menu_buttons
        show screen daytime
        jump main_bedroom





    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
