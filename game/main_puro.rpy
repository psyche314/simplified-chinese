label Puro_Beginning_Talk:

    hide screen menu_buttons 
    scene black

    "Both of you are sitting in the elder's tent, the lantern on Hezzong's hand glows faintly."

    pause 2.0
    scene puro_hezzong_lodge with dissolve
    show hezzong lookaway with dissolve
    hz "On the paper, it says you volunteered to be the watcher tonight."

    "Hezzong, the elder chief of the tribe, checks the paper on his hand before looking back at you."
    "This was meant to be a routine job, but you certainly have a different plan in mind."
    yu "Yes, I did."
    "You nod, your eyes are fixed on the elder. A pleading gaze is all you can muster."
    "The red dragon is sitting across the table, his brows are furrowed."
    show hezzong normal with dissolve
    "Everyone in the tribe calls him the Allfather, he has been the elder chief for as long as you can remember."
    "He is the one who taught you how to read and write, took you into his house as you help him manage the books."
    with vpunch
    hz "I don't think you're ready for this, espcially after what happened to Chime."
    yu "I- I am ready, Hezz."
    "You stutter, your voice is shaking. This is a crucial decision to make but you are determined in your path."
    hz "You understand the duty of being the tribe's watcher, right?"
    yu "I understand."
    show hezzong lookaway with dissolve
    hz "Mhmm... just to make sure, I will tell you again."
    hz "As a watcher, you have to keep the tribe safe at night, and keep those sprites from ever entering our place."
    yu "I know."
    show hezzong normal with dissolve
    "The elder reads through the paper again, before he takes another glance at you and notices your mind wandering off."
    "He sighs, and puts the paper down."
    hz "How is the search for Chime going? I heard you guys have been looking for him for a week now."
    yu "I- I haven't found him yet."
    "You look down at your feet, your hands are shaking."
    "Chime has been your best friend ever since you were young, and losing him was the last thing you want to happen."
    show hezzong talk with dissolve
    hz "That is worrying, I didn't think he would be missing for this long."
    hz "People don't just disppear like that. Especially not him, he is a good kid."
    yu "The thing is, I saw a flickering light around our post last week, I think it was him."
    hz "I see... are you sure you're not hallucinating... or dreaming? It's been a long time since you slept."
    hz "At least that's what the folks back there told me, they are all tired after following your lead for a week."
    yu "I know, I understand if they withdraw from the search, but I won't quit until I find him."
    hz "At some point, maybe the best way ahead is to stop walking forward and think for a moment."
    yu "I just want to find him and bring him back safe, allfather. Please, let me be the watcher for today."
    show hezzong closeeyes with dissolve
    "He shakes his head, and sighs."
    hz "You have to go in alone, if you were to be the watcher today, I'm not sure anyone is available after all the turmoils they've been put through."
    yu "I am aware of that, allfather."
    hz "Is this really what you think?"
    hz "What if you go missing next? Where do I find someone who can manage my books?"
    hz "And someone foolish enough to stay up late with me?"
    "You don't know what to say, you look at the elder's eyes, and despite his chuckle, you can see the worry in his eyes."
    "It's been a long time since he appointed you as his assistant. Apart from spending time with Chime, helping the elder was your second most treasured time to spend."
    yu "I- I don't know, allfather. I just want to find Chime."
    "The elder shakes his head."
    hz "Perhaps, a glimpse of hope is what my little red dragon needs. Maybe you'll prove me wrong and bring him back alive."
    "Hezzong feints a weak smile, he lowers the lantern and slowly shoves it across the table."
    show hezzong lookaway with dissolve
    hz "I am going to trust you on this. But you have to promise me you will be extra careful."
    hz "Take this with you, I should be able to track you down if you get lost in the night."
    yu "Thank you, Hezz."
    "You take the lantern and put it on your side, the warmth of the lantern is strangely hot even on your hand."
    hz "When it's dawn, just come back safe, you don't need to stay until the morning."
    yu "Okay, allfather."
    hz "That's good. Okay, then let us head out, I will show you the way."
    "The allfather pushes open the door, and you follow him out."
    scene black with dissolve
    pause 1.0
    scene puro_forest with dissolve
    "The night is quiet, the moon is shining bright, and the stars are twinkling in the sky."
    show hezzong closeeyes with dissolve
    "Everyone else is sleeping, the lifeless silence has you shiver down to the core, but Hezzong's mere presence made you feel a lot safer."
    "Hezzong whistles softly as you follow close behind, the torch in his hand is lighting up the path just enough."
    "You hold your own latern tightly, your heart is beating faster than your feet, your fear of being stranded haunts you again."
    $ hezzong_talks = [0, 0, 0, 0]
    $ tutorial_stage = 0
    call Hezzong_Puro_Forest_Dialogue from _call_Hezzong_Puro_Forest_Dialogue

    "Catching up with Hezzong, you follow him into the forest."

    scene black with dissolve
    $ moine_first_impression = 0
    jump Puro_Watch_Post_Enter

label Hezzong_Puro_Forest_Dialogue:

    menu:
        "Maybe it's best for you to talk to Hezzong in the meantime..."

        "The recent situation in the tribe" if hezzong_talks[0] != 1:
            $ hezzong_talks[0] = 1
            yu "Hezz, how's the tribe going lately?"
            show hezzong normal with dissolve
            hz "Well, we're doing fine. The harvest is good this year, and we have enough food to last us through the winter."
            hz "But, we're still missing Chime, and that's a big problem."
            hz "Afterall, he is not one who wanders off without telling anyone."
            hz "Shudo and Pairon were worried pant-less, especially after you told them you had to get in the forest by yourself."
            yu "I'm sorry Hezz, I didn't mean to worry them. But they know I will keep searching while they rest."
            show hezzong talk with dissolve
            hz "Hmm, don't worry about it, I will tell them you're safe when you come back."
            hz "Look, we are not a big tribe, we need to look for each other's back, especially in times like this."
            yu "I know, I know. I just want to find Chime and bring him back."
            hz "You know, I'm worried about you too. You haven't slept for a week, and you look like a mess."
            "You look down at your feet, maybe he's right, but what is the alternative... do you just give up on the search."
            "You don't ever want to think about living in a world without your best friend, even at the cost of wearing out your body bit by bit."
            yu "Would he be okay? I mean, if I don't find him now, what's the chance of him... ever coming back."
            hz "I- uh... Well."
            hz "I will be honest with you, the chance is only getting lower and lower as time passes."
            hz "But we aren't giving up on him, our search party hasn't stopped yet, and we will keep looking for him."
            yu "Okay."
        "Chime's disappearance" if hezzong_talks[1] != 1:
            $ hezzong_talks[1] = 1
            yu "Hezz, do you know why... Chime's missing?"
            show hezzong normal with dissolve
            hz "There is no way I can know, but I have a feeling that it's not a good sign."
            yu "Why are you saying that?"
            show hezzong talk with dissolve
            hz "I only just recalled now, but the day before he went missing, he told me about a pair of eyes while we were hunting."
            hz "He said there were horns behind the eyes, and it was staring at him from the bushes."
            hz "I didn't think much of it at the time, so I told him, well. Maybe it's your friend messing with you."
            hz "But now that I think of it, it's a little worrying."
            yu "Hezz, couldn't you have told me this earlier?"
            hz "I didn't think it was important... I thought it was you or someone else, after all, horns aren't something rare in our tribe."
            yu "W-what if he's kidnapped by that pair of eyes?"
            hz "Or, it can still be something else innocent, and uhm... he just got lost in the forest."
            yu "After you told me this, I'm not sure if I can believe he {i}just{/i} got lost."
            hz "Maybe you are right."
            hz "Didn't you mention having seen a glowing light somewhere?"
            yu "I thought it was Chime, but I'm not sure now."
            hz "Well, maybe it's someone else's."
            hz "If he's kidnapped, then we have to track that person down, somehow. But we have no trails to start off of."
            yu "You're right."

        "The duty as a watcher" if hezzong_talks[2] != 1:
            $ hezzong_talks[2] = 1
            yu "Hezz, what do I need to do as a watcher?"
            show hezzong normal with dissolve
            hz "Well, as a normal watcher, you just need to keep the tribe safe at night, and alert us if anything suspicious happen."
            hz "Usually, we assign two watchers every night to perform this job, but they don't seem to be available tonight."
            hz "It's a routine job, but it's important. You know, we don't want those sprites to come in and steal our food."
            yu "What should I do if I see one?"
            show hezzong talk with dissolve
            hz "Fight, of course. You have a sword, right?"
            yu "Yes, I do. But it's not very sharp."
            hz "It's fine, it's not like you're going to fight a demon or something."
            yu "Well I hope not."
            hz "If you lost your sword, just raise your arm, puff out your chest and make a loud noise. These sprites are not very brave, they will scramble at the slightest bit of sound."
            show hezzong closeeyes with dissolve
            "Hezzong demonstrates as he pulls his shoulders back, showing off his huge chest muscles in confidence."
            hz "See, that's pretty easy."
            "He smirks at your blushed gaze, obviously proud of his act having an opposite effect on you."
            yu "Well..."
            yu "Who are those sprites, actually?"
            show hezzong normal with dissolve
            "The elder shrugs, returning to his normal position, but his chest is still puffed out."
            hz "Wandering pests, nothing more. They are not dangerous, but they can be annoying."
            yu "I see."
            yu "You know, I haven't seen one before, so it's all new to me."
            hz "That's because the watchers are doing their job. Wouldn't you prefer that?"
            yu "You are right, allfather."
        "Whine about his chores" if hezzong_talks[3] != 1:
            $ hezzong_talks[3] = 1
            yu "Hezz, maybe I need to take a breather tomorrow."
            show hezzong normal with dissolve
            hz "What? Why?"
            yu "I- I am still looking for Chime, just need some extra time to sleep."
            show hezzong talk with dissolve
            hz "You know, I can't do all the work by myself, right?"
            yu "Yeah, but you did, last time I checked you finished all the books and accounts by yourself while I was away."
            hz "But I can't finish all of these all the time, that's why I hired you."
            yu "But you did! You are perfectly capable to do so."
            show hezzong closeeyes with dissolve
            hz "Yeah, you're right."
            hz "Hey, how about this, I'll be honest with you. I care more about you than the ever-stacking books, I just want to keep you around while you're looking for Chime."
            hz "Perhaps, you can use my bed if you happen to be tired after the post. It's the closest from the tower, and I can keep an eye on you."
            hz "And, I will make sure you get those extra sleep tomorrow. No need to worry about the books."
            yu "Really? Thank you, Hezzong."
            hz "I hope you don't mind sharing a bed with an old white-bearded dragon, or having to make it through my snores."
            hz "I will try to keep it down, but I can't promise anything."
            yu "You're my allfather afterall, of course I don't mind. I'm already grateful to have a warm bed."
            hz "Good, then it's settled."
        "Ask about the training" if tutorial_stage > 0:
            if tutorial_stage == 1:
                yu "Hezzong, what should I do right now?"
                hz "Just try to take a look at the crate over there."
                msg "Hint: Try to use Space, or the Interact button on the screen to interact with objects."
            elif tutorial_stage == 2:
                yu "Hezzong, what should I do right now?"
                hz "You should pick up the turnips over there, and bring them into the crate."
                msg "Hint: Try to use {i}E{/i}, or the hand button on the screen to pick up or drop objects."
        "That's it for now" if tutorial_stage > 0:
            yu "That's it for now, Hezz."
            show hezzong normal with dissolve
            hz "Alright, then let's keep up with the training."

    return

label Puro_Get_Onto_Watchtower:
    hide screen dungeon_map
    $ on_watch_post = 1

    "You enter the watchtower and climb upstairs, passing by the bell that Hezzong mentioned about."
    scene puro_forest with dissolve
    "On the top, you can see the entire tribe, and the forest surrounding it."
    yu "I guess this way I'll know it when the light comes back again."
    "You have been waiting for a while, but nothing seems to be happening."
    "It's a little boring, but you have to keep your eyes open somehow..."
    "You look around, and see the lantern Hezzong gave you."
    yu "Ring the bell... when something happens... right? Allfather said so."
    yu "No, allfather is always right, don't you dare to doubt him."
    "Bored as you are, you start to play with the lantern, and the bell."
    yu "Maybe I should go down and take a closer look, if there is light wouldn't the trees have covered it...? I won't be able to see from here."
    yu "But allfather said I should stay here, and I should stay here."
    "Under the moonlight, you can see the forest, and the trees are swaying in the wind."
    "You can hear the sound of the leaves rustling, and the wind is blowing through the trees."

    jump Puro_Watchtower_Thoughts

label Puro_Watchtower_Thoughts:

    menu:
        "It was a perfect night, but there is one thing missing..."
        "Chime":
            $ one_watch_post = 1
            "You can't help but think about Chime, and how he's doing right now."
            "Everything just reminds you of him, the games you used to play together, the stories he used to tell you, and the way he used to smile."
            "You miss him, and you want to find him, but you don't know where to start. You are afraid that you might never see him again."
            "That thought is unbearable, maybe it's the exact reason why you have not slept for days."
            "You nudge at the skull necklace that he gave you, and it gives you a little bit of comfort to make it through the night."
        "Hezzong" if hezzong_talks[3] == 1:
            $ one_watch_post = 2
            "Maybe you should have accepted Hezzong's offer to sleep in his bed."
            "How would it feel to be in his bed, and to be held by your own elder?"
            "He has always been fond of you, and lately, he has been more caring than usual."
            "Wouldn't you be a jerk to reject that old man? The way he's been worked up about you, and Chime, it's never seen on other people."
            "Plus, who would not want a huge, warm dragon pillow to hug through the night..."
        "{s}Hezzong{/s}" if hezzong_talks[3] == 0:
            jump Puro_Watchtower_Thoughts
        "Sleep{#faa5aba2}":
            "You should probably sleep, you are tired after all."
            "It's perfect for a full night's sleep, but you have to find Chime, and you can't sleep until you find him."
            "But... you are so tired, and you can't keep your eyes open, they are too dry."
            menu:
                "Maybe, a nap is necessary."
                "Sleep in the tower":
                    $ on_watch_post = 6
                    "You decide to take a nap, and you lay down on the cold floor on top of the tower."
                    yu "Just a little nap, I won't sleep for long."
                    "As soon as you finish your sentence, you have already fallen asleep."
                    "..."
                    yu "Ahhh!"
                "Make it through the night":
                    $ on_watch_post = 5
                    "You decide to make it through, and you keep your eyes open."
                    "There is no way you are sleeping, you have to fi-"
                    "..."
                    "You fell asleep, right on the table."
                    yu "Ahhh!"
            jump Encountering_Moine

    "Shaking away your thoughts, you look around, trying to spot anything suspicious."
    "..."
    "Suddenly a light flickers in the distance, and you can see it from the tower."
    "It's not far from the tower, maybe if you run down right now, you can catch it."
    "But you have to ring the bell, and you have to stay here. Just like what Hezzong said."
    menu:
        "What should you do...?"
        "Chase the light":
            $ on_watch_post *= -1
            "You sprint down the tower, carrying Hezzong's lantern with you and run towards the flickering light, leaving the bell behind."
            yu "Sorry Hezzong, it might be Chime..."
            "You run through the forest, and you can see the light getting closer and closer."
            scene black with dissolve
            "It's not long before you find the source of the light, and you can see a figure standing in front of you."
            yu "Chime...? Is that you?"
            "You can see the shadow of a horn slowly turns into a pair of antlers..."
            scene puro_forest with dissolve
            $ moine_first_impression = 0
            jump Moine_Introduction
        "Ring the bell":
            "You run down the tower, and ring the bell as loud as you can."
            "Suddenly, something is lit up in the tribe, it seems your strategy is working."
            "M-maybe they can catch Chime now, or the culprit."
            "You go back a step to take a look through the windows, but, there's something missing."
            "The light is gone, you can't see it anymore."
            "You scratch your head, and you can't help but feel a little bit of regret."
            yu "M-maybe I should have chased it, what if it was Chime."
            scene black with dissolve
            "You go downstairs to check if there's any remaining light, and suddenly, something is awry."
            "You can hear the sound of dirts and leaves being kicked up, and you can feel something pushing against you."
            scene puro_forest with dissolve
            yu "Huh?"
            jump Moine_Quick_Introduction

label Encountering_Moine:
    $ moine_first_impression = 0
    scene puro_forest with dissolve
    if spriteling.lose > 0 or spritebinder.lose > 0:
        "The sleep was short, as you are suddenly awaked by a strange sound."
        yu "Huh?"
        "You think to yourself, as the sound of dirts and leaves being kicked up wakes you from the short slumber."
        "Oddly enough, it doesn't sound like another sprite, or anything you've heard before."
        "It's only after a few seconds that you realise something is pushing against you."
        $ renpy.music.play(mOpen1b, loop=False)
        $ renpy.music.queue(mOpen2, loop=True)
        "Your eyes flutter open as you are lying on the ground, both arms holding your weight as you try to catch your breath... but something is awry."
        if on_watch_post >= 5:
            yu "Wait... wasn't I on the tower?"
            "You look around, and you can see the trees, the sky, and the moon, but you can't see the tower you were just sleeping in seconds ago."
        "It took you more than a second to realise that you are not alone."
        my "Muzz lus baerz acha."
        show moine_normal with dissolve
        "A rough voice calls your attention. You look up, and see a figure kneeling in front of you."
        "It was an elk, wearing a green hood, the moonlight is so dim you can barely make up the outline of his body."
        "The hood is covering his face, in fact, his arms are pressing on your chest, and you can barely move."
        if spritebinder.lose > 1:
            "The elk tilts his head, perhaps confused by your nude body, or the fact that your body is covered with your own cum."
        my "Telaa."

        menu:
            "Struggle away":
                $ moine_first_impression = 3
                "You try to push him away, but he doesn't budge."

                my "Grikzrutt, fiinsti upik Kyllanoaf bezme luglan."
                with vpunch
                "He doesn't seem to be affected by your attempt to wring your arms out, but it is more than a nuisance for you."
                "The strange man lean in closer, to the point you can feel his breath on your face."
                "You turn your head away immediately, but you can't help but feel the fear in your mind."
                with vpunch
                yu "G-get off me!"

                my "Gumlaa. Lus ruttup oozik acha."
                "The elk makes his way to position his bottom on your chest, and you can feel the weight of his body pressing down on you."
                with vpunch
                yu "What do you want from me?"
                "From the pupils in his eyes you can feel he is mildly bothered, but he stopped saying anything at all."
                "You find yourself in between the stranger's thighs, his odorous loincloth almost covering your face."

                "Beneath the loincloth it traces the shape of a weighty bulge, emanating a strange, musky scent and heat right on your chest."
                "Instantly, your mind is filled with a confused mix of fear and arousal."
                "Your body soon responed with a shiver down the spine, and you can only attempt to cover the bulge in your own pants."
                yu "Uh... I- I don't want to hurt you, but you have to get off me right now."
                yu "Hezzong is coming, do you know a Hezzong? He's going to have a talk with you if you don't g-get off..."
                "The stranger doesn't respond, though his gaze is much less threatening now."
                "You can see his hands slowly moving away from you, instead he is reaching for something in the back."
                "You try to ready your weapon, but the way he is sitting on your body, you are afraid there is nothing you can do if he decides to attack you."

                my "Chak hezzillikaad zruhez ettu adenni, denni supz grikz fiinklo."
                yu "What?"
                "For some reason, the stranger decides sitting on top of you with his... barely-showing member is a good idea, but you can't do anything but to let him be."
            "Ask who he is":

                $ moine_first_impression = 1
                yu "W-wait, who are you...?"
                "You exhale, trying to keep your voice steady underneath the weight of the stranger."
                "The stranger stares at you, he stopped pushing you down, it's clear that he heard you."

                my "Muzz lus hezzikom acha ik criv ziklo, tenkzom lus puro hylan."
                "It sounds like he is mumbling to himself, but you can't make out what he is saying."

                my "Ik lu, paidzrutt lu gliiz acha, ome acha slanivik. Haav supz chak hezzillmur... ptaalzan."
                "You remain calm in face of the stranger speaking in a language you can't understand, but you can't help but feel the fear in your mind."
                "You find yourself in between the stranger's thighs, his odorous loincloth almost covering your face."
                "Beneath the loincloth it traces the shape of a weighty bulge, emanating a strange, musky scent and heat right on your chest."
                "Weirdly, your body responeded with a shiver down the spine, and you can only attempt to cover the bulge in your own pants."
                yu "Uh..."
                "Your gaze is fixated on the stranger's... crotch, it's just barely showing, and has no intention of hiding it."

                my "Grulliad alu, pob te acha hezzik. Ik lus, paidzrutt grikz fiinslan acha."
                "But the stranger doesn't seem to be bothered by your gaze, instead he is reaching for something in the back."

                my "Wru fiinklo, chak hezzillikaad zruhez ettu adenni, denni supz grikz fiinklo."
                "The elk just keeps mumbling, and you still have no idea of anything he's talking about."

        "Soon, the stranger pulls out a large, wooden box. There are a few strings attached to it, and he is fiddling with them."
        "He stares at you for a few seconds, before playing a tune on the box."
        yu "What are you doing?"
        "The stranger gives you a side glance, before returning to tend to his box."
        jump Moine_Inbetween_Land
    else:


        "The forest is quiet, as if it was waiting for the sound of a blade to pierce through the silence."
        "The moon is shining bright. You look up and see the usual stars."
        "Hezzong used to tell you stories all about these twinklers, now that you've thought of it, looking at the sky makes you feel a little safer."
        "Without warning, you notice Hezzong's lantern starts flickering, and then it goes out."
        yu "Shit."
        "You hold your breath, straining your ears, trying to catch the faintest sound."
        "Soon, a faint sound of footstep in a distance."
        yu "Sprites float in the air, and allfather never made a sound walking, someone else is coming..."
        yu "But who else could be walking outside the tribe."
        "Your eyes are fixed on the forest, something is out there. You can feel it."
        menu:
            "Run away":
                $ moine_first_impression = 2
                "You take a deep breath and start running through the trees."
                with vpunch
                "Your heart is beating faster than your feet, you have no idea what could be out there but whatever it is, but it can't be good."
                yu "Shit."
                "You almost run into someone."
                yu "Sorry, I didn't mean t-"
                show moine_normal with dissolve
            "Remain calm":




                $ moine_first_impression = 1
                "You take a deep breath and try to calm yourself down."
                "Being as brave as you wish to be, you puff up your chest, that's what Hezzong had taught you to do so, even though you are shaking on the inside."
                "A glimpse of hope tells you it could be Chime, maybe finally you've found him."
                if hezzong_talks[2] == 1:
                    "You puff out your chest, just as Hezzong had taught you to do so."
                "Turning your head everywhere, you try to find the source of the sound."
                yu "Who is ther-"
                yu "Ahhh!"
                "As soon as you turn your head, you see a figure standing in front of you."
                show moine_normal with dissolve
        jump Moine_Introduction

label Moine_Introduction:

    "It was an elk, with a pair of majestic antlers, wearing a green hood, the moonlight is so dim you can barely make up the outline of his body."
    show moine_normal with dissolve
    $ renpy.music.play(mOpen1b, loop=False)
    $ renpy.music.queue(mOpen2, loop=True)
    "The hood is covering his face and he is standing very still, facing you, as if he had been expecting you."
    "You couldn't even tell if he is looking at you or if his eyes were fixed on something else."
    "Suddenly, the fear in your mind overwhelms your entire body, causing your legs to give up."

    my "Muzz lus baerzom acha."

    my "Kiz chime, ik Lus muzz ru yaglo laarelan."
    "The elk doesn't move. He stands there, looking at you as you hear his gruff voice."
    yu "Huh? Chime? W-who are you."
    "You are lying on the ground, both arms holding your weight as you try to catch your breath."
    "You raise your head, the reflection of his pupil gives you barely an insight onto the figure."
    "His antlers are shining under the moonlight. You have never seen a creature like this before. It was something only shown on story books."

    my "Ru, ru. Rutt chak Chime."
    "It sounds like he is mumbling to himself, but you can't make out what he is saying."
    yu "What do you want from me?"
    "You can feel his gaze piercing through your soul, pacing you left and right. You are not sure how much time has passed but your body is trembling."

    my "Ik cha, paidzrutt cha gliiz alu. Svupz chak tek... ptaalzan."
    "You can't understand what he is saying, but you are certain that he is not moving his mouth when he speaks, and it's sending goosebumps right into your spine."
    "Your mind is screaming at you to get away from here, but your body never responded, instead you freeze in place, like a prey to be feasted upon."

    my "Muzz lus hezzikom acha ik criv ziklo, tenkzom lus puro hylan."
    menu:
        "You can't just stay here and let him do whatever he wants, but... what if he knows about Chime? You have to ask him."
        "Ask about Chime":
            $ moine_first_impression = 4
            yu "Do you know about Chime? Have you seen him?"
            my "Chime...?"
            "You nod, your voice is shaking, maybe after all there hope of seeing Chime again."
            "You wait in anticipation, but the stranger only scratches his head, probably in confusion or disbelief."

            my "Ik lus frizzrutt, chaenni up eniof fiinslan."
            yu "This is not helping, even if you are giving me the answer I won't have understood."

            my "Telaa."
            "You furrow your brows, trying to read between his words, but you still can't make out what he is saying."
            "The stranger extends his hand, patting your head, and you can feel the warmth of his palm."
            "Still, you are unsure of his intention, but you can't help but feel a little bit of relief with his gesture."
        "Stay calm":



            my "Grulliad alu, pob te acha hezzik. Ik lus, paidzrutt grikz fiinslan acha."
            "The stranger walks a few steps forwards, each steps only makes you much more anxious."

            my "Wru ettuiad denn gwidd olozor."
            "The stranger looks left and right, as if he is expecting something."



    my "Wru fiinklo, chak hezzillikaad zruhez ettu adenni, denni supz grikz fiinklo."
    "You stare as the man reaches for something in the back, and pulls out a large, wooden box."
    "There are a few strings attached to it, and he is fiddling with them."
    "He stares at you for a few seconds, before playing a tune on the box."
    yu "What are you doing?"
    "The stranger gives you a side glance, before returning to tend to his box."

    jump Moine_Inbetween_Land

label Moine_Quick_Introduction:
    $ moine_first_impression = 0
    show moine_normal with dissolve
    $ renpy.music.play(mOpen1b, loop=False)
    $ renpy.music.queue(mOpen2, loop=True)
    "It was an elk, with a pair of majestic antlers, wearing a green hood, the moonlight is so dim you can barely make up the outline of his body."
    "The hood is covering his face and he is standing very still, facing you, as if he had been expecting you."
    "You couldn't even tell if he is looking at you or if his eyes were fixed on something else."
    "Suddenly, the fear in your mind overwhelms your entire body, causing your legs to give up."

    my "Muzz lus baerzom acha."

    my "Kiz chime, ik Lus muzz ru yaglo laarelan."
    yu "W-what are you talking about?"
    "The elk is rushing through his speech, he seems very agitated, maybe he's trying to avoid getting caught because of the bell."

    my "Denni supz grikz fiinklo!"
    "You stare as the man reaches for something in the back, and pulls out a large, wooden box."
    "There are a few strings attached to it, and he is fiddling with them."
    "He stares at you for a few seconds, before playing a tune on the box."
    yu "What are you doing?"
    "The stranger gives you a side glance, before returning to tend to his box."
    jump Moine_Inbetween_Land

label Moine_Inbetween_Land:
    $ renpy.music.stop()
    pause 1.0
    $ renpy.music.play(mOpen2b, loop=False)
    $ renpy.music.queue(mOpen3, loop=True)
    "Is he playing a tune? It's a strange melody, but it's unnerving."
    with flash
    "Surely the stranger is not here just to play you a song, but with the tune he's playing, you doubt he has any malice to begin with."
    yu "Huh?"
    "You are not sure if it was gradual or sudden, but everything around you starts to glow faintly blue in this dark night."
    with blueflash
    "The stranger's tune is getting louder and faster, and the glow is getting brighter."
    yu "What is happening?"
    scene puro_forest:
        zoom 1.2
        parallel:
            matrixcolor TintMatrix("#eee") blur 4
            easein 1.25 matrixcolor TintMatrix("#4af") blur 8
            easeout 1.25 matrixcolor TintMatrix("#eee") blur 4
            repeat
        parallel:
            linear 0.1 xpos -0.08 ypos -0.05
            linear 0.1 xpos -0.01 ypos -0.02
            linear 0.1 xpos -0.1 ypos 0
            linear 0.1 xpos -0.02 ypos -0.01
            linear 0.1 xpos -0.06 ypos -0.03
            linear 0.1 xpos -0.07 ypos -0.03
            linear 0.1 xpos -0.02 ypos -0.04
            linear 0.1 xpos -0.05 ypos -0.05
            linear 0.1 xpos -0.01 ypos -0.02
            linear 0.1 xpos 0 ypos -0.06
            repeat
    show moine_normal:
        xalign 0.5
        easein 1 zoom 1.2 yalign 0.3 xalign 0.5
    "For the first time, you see a glimpse of the stranger's face under the hood, a lush of brown hair, and rings of fur around his eyes."
    if moine_first_impression == 1 or moine_first_impression == 4:
        my "Kiz chime."
        "The stranger sings with a rather gruff voice, it's clashing with the soothing melody he's playing."
        "Everytime you hear him utter the word Chime, you keep yourself composed. This time it's no different."
        "A cold breeze is swirling around you, and you can feel the chill on your skin."
        "Perhaps this is how you get closer to what's happening right now, but at least, you are not feeling as scared as before."
    elif moine_first_impression == 2:
        "The stranger says nothing, he slowly closes his eyes, and continue to fling his fingers on the strings."
        "Gusts of wind blows you away, you almost topple over the ground with the force of the airflow."
        "You take a deep breath, and try to keep your eyes open, but the wind is too strong, and everything is too bright."
    else:
        "As he continues to play, the stag suddenly flings a gust of wind towards you, rendering you unable to move."
        yu "W-what, get off me!"
        show moine_normal:
            easein 1 zoom 1.25 yalign 0.35
        "You try to push away the spell, but it's futile. You have never seen anything like this before, and you are not sure if you can do anything about it."
        "He gives you another side glance, before continuing to play his tune."
    "Suddenly, the ground pulses, and your toes begin to leave the ground."
    yu "Huh?"
    scene puro_forest:
        zoom 1.3
        parallel:
            matrixcolor TintMatrix("#4af") blur 8
            easein 1.0 matrixcolor TintMatrix("#015192") blur 16
            easeout 1.0 matrixcolor TintMatrix("#4af") blur 8
            repeat
        parallel:
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
    show moine_normal:
        zoom 1.2 yalign 0.3 xalign 0.5
        easein 1 zoom 1.4 yalign 0.2 xalign 0.5 matrixcolor TintMatrix("#4af")

        parallel:
            matrixcolor TintMatrix("#4af")
            easein 1.5 matrixcolor TintMatrix("#015192")
            easeout 1.5 matrixcolor TintMatrix("#4af")
            repeat
    with vpunch

    "You are floating in the air, and everything around you is glowing bluer and bluer."
    with vpunch
    "The stranger flicks his wrist around the strings, and it almost feels like time is getting faster and faster."
    with vpunch
    yu "S-shit... I should've waited for Hezzong..."
    with vpunch
    "You think out loud, both of you float in the air, before you are high enough to see the top of the tree, and the watch tower from afar."
    "It's only now that you've noticed that everything becomes to blurred, all the trees in the forest, blends into a mixture of slurry blue in your vision."
    "Looking up, even the moon begins to bleed into the starry night as you rub your eyes to get a clearer view."
    with vpunch
    yu "What is happening..."
    "The stag elk doesn't bat an eye, only focused solely on the chaotic tunes that's entangling you along with him."
    "Slowly the world around you turns into pure nothingness, there is nothing beneath your feet, nothing except for the stranger's chorus."
    with vpunch
    "You look around, everything is glowing blue, with occassional white streaks passing through towards the supposed sky."
    menu:
        "Trust the process":
            $ moine_first_impression += 10
            "You cross your arms, waiting for his music to end."
            "His fingers are still dancing on the strings, each of his movement only sends you further and further away from the land."
            "The only thing you can to is to look around into the nothingness, it's a strange feeling, but you are not feeling scared anymore."
            "Slowly, you close your eyes, and let the music take you away."
            "..."
            "..."
            scene black with fade
            yu "Chime... I hope you are okay..."
            yu "Even if you are out on the other lands, I'll find you, I promise."
            scene black
            "You think to yourself, as you are floating idly in the air."
            yu "Huh?"
            scene puro_forest:
                zoom 1.3 matrixcolor TintMatrix("#4af") xalign 0.2 yalign 0.2 blur 32
                easeout 1.5 zoom 1 matrixcolor TintMatrix("#fff") blur 0
            with dissolve
            $ renpy.music.play(mOpen3b, loop=False, fadeout=5.0)
            "Suddenly, everything around you turns back to normal, and you are falling back to the ground."
            with vpunch
            yu "Arghhhhhh-!"
            scene black with fade
            "You can still feel the frigid air on your skin as you fall, you look up, and finds that the stranger has already disappeared."
            "The last thing you know, you hit the ground with a loud thud."
        "Interrupt the stranger":

            $ moine_first_impression += 20
            yu "Let me go!"
            "You float towards the stag, demanding an answer of this madness, but he doesn't respond."
            "His fingers are still dancing on the strings, each of his movement only sends you further and further away from the land."
            "You try to push him away, but he doesn't budge."
            with vpunch
            "The stranger stares at you violently, which takes you aback."
            yu "Answer me first! Where did you hide Chime?"
            with vpunch

            with vpunch
            "You push against the stranger again, this time it messes up his tune, and you can feel the world around you starts to crumble."
            with vpunch
            scene puro_forest:
                zoom 1.3 matrixcolor TintMatrix("#4af") xalign 0.2 yalign 0.2 blur 32
                easeout 1.5 zoom 1 matrixcolor TintMatrix("#fff")
            with dissolve

            "The stranger's eyes are wide open, and he is staring at you, as if he is trying to tell you something."
            with vpunch
            yu "Huh?"
            with vpunch
            "But it's too late, suddenly everything around you turns back to normal, and you are falling back to the ground."
            yu "Arghhhhhh-!"
            $ renpy.music.play(mOpen3b, loop=False, fadeout=5.0)
            scene black with fade
            "You can still feel the frigid air on your skin as you fall, you look up, and see the stranger floating idly, staring at you."
            "The last thing you know, you hit the ground with a loud thud."

    "..."

    "..."

    "..."



    jump Sebas_First_Meet
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
