label Vurro_Ask_How_Doing:
    e "So, what are you doing, Vurro?"
    "You politely speak. Vurro does not turn his head towards you, but you can see a slight raise in the corner of his mouth."
    v "Nothing much, just thinking."
    "He continues looking ahead into the depth of the dark forest, his gaze blurred yet unmoving."
    e "Well, what are you thinking?"
    "The brown werewolf turns to you, his shaggy fur is evidence of either his pondering, or his exhaustion."
    v "Oh... you know, just thinking about what's Wuld gotta cook for dinner."
    "Your eyes soften. Despite his uplifting voice, it is clear that Vurro is not telling you the whole truth."
    v "He better be cooking up something real good, like... a nice stew to satiate... my... appeti-"
    "Vurro sinks into silence, his eyes turning back to the forest."
    "You struggle to find words to comfort him, and he seems to have quickly caught that."
    v "Don't worry about me, [e]. I'll be fine, for the time being."
    "He gives you a small smile, but it doesn't seem to reach his eyes."
    return

label Wuldon_First_Meet:
    scene slumbrous_well with dissolve
    "You come across a small wooden hut, sides and top partway consumed by the surrounding forest."
    "If you hadn't happened to stumble into it by chance, you never would have found it."
    "At first, it seems like the area is completely abandoned, but... looking closely, you can see a well."
    "And beside it, the large form of a dark blue werewolf pulling water up from said well."
    show wuldon normal with dissolve
    $ wuldon_meet = True
    if quest22.status == True:
        $ wuldon_like += 1
    elif quest22.status == 3:
        $ wuldon_like += 2
    else:
        $ wuldon_like += 3
    "His arms glisten with sweat, his powerful frame ill-hidden by his pale-green cloak."
    "Despite that, he himself blends in with the terrain itself as well, his blue fur and green cloak blending in with the blues and greens of the river and shrubs."
    my "Hello there little one."
    "You hear a deep voice, rich and rumbling like the sound of a far distant storm."
    e "Hello?"
    "The blue wolf turns around and reveals himself to be the one speaking to you."
    my "Yes, hello. I hope you weren't trying to spy on me, as you would be a rather poor excuse for one if so."
    "There is a light grin playing across his face. It doesn't quite reach his eyes."
    my "You somehow managed to snap a twig under your foot with every step you took."
    "You can't help but wince."
    e "Sorry, I didn't mean to bother you."
    "The wolf relaxes. Even so, he is still an entire head higher than you, far wider, and stronger."
    my "It's no problem. I will need you to start paying if you ogle me any longer, though."
    "He smirks."
    my "I don't think you could afford my rates."
    w "The name's Wuldon, by the way. Thought I'd give it since you seem intent on sticking around."
    e "O-oh. Yes! My name is [e]!"
    w "Mm. Nice name."
    "Wuldon gets back to filling up the buckets."
    w "So, what are you doing this far away from civilization, [e]."
    e "Well, I was originally sent in this direction to find out what was going on with this magic stone..."
    "You pull out the stone in question."
    e "But then I met Uffe and his tribe-"
    "You see Wuldon freeze for a second, before continuing as if nothing happened."
    e "And he told me to go kill this feral werewolf for him if I wanted to get any information."
    w "And, what did you do?"
    if quest22.status == 2:
        e "Well, I haven't gotten that far yet. I was on my way to find it, and I found you first."
        "Wuldon, turns to look at you, relief on his face."
        w "Well, I suppose I should tell you the story of the feral werewolf and its curse before you get there."
        w "Uffe, mangy dog that he is, wants you to kill someone for him without even telling you how it happened."
        "There is a cold light in his eyes. A grudge held and festering from years of denial."
        w "Regardless, the story."
        w "Once upon a time, two brothers led the dark forest tribe together."
        w "One, a domineering and predatory man who wished for his tribe to hunt in isolation from the world."
        w "The other, kinder, and more mercantile, wishing to find ways to lead his brethren out of a life of kill or be killed."
        w "One day, the mercantile brother found a cave filled with precious ores. Ores that he knew the surrounding tribes and villages wanted."
        w "Here, he saw his opportunity to lead his people out of the shadows, and into civilization."
        w "He told his pack about the cave, and told his brother about his dream."
        w "The hunting brother did not understand."
        w "This lifestyle of hunting and killing was all they had ever had. All they would ever need."
        e "This sounds a lot like something I've heard before."
        "Rather than respond, Wuldon grins a knowing grin."
        w "It was this very lifestyle that let his brother and he be alpha. They had carved their place in the tribe with their superior fangs and claws."
        w "Even if they proved this by killing their brethren, that was how things should be."
        w "The mercantile brother asked that he still be allowed to try his dream."
        w "They were equals, and they could follow both lifestyles."
        e "Could they really? It's only one pack."
        w "It was a pack with two alphas, little one. This was not the first disagreement."
        w "They had their solutions, though sometimes one or both sides were unhappy with it."
        e "What kind of solutions were they?"
        w "All will be revealed in time."
        "Wuldon's tone carries a sense of finality to it, telling you to be quiet so he can keep telling the story."
        w "In order to make sure his brother would not be disrupted, he took half of the tribe with him to the mines."
        w "The hunting brother was furious."
        w "His foolish wretch of a brother wished to betray him and their way of life."
        w "He had to be rid of him, but they were equals, as his brother had intimated."
        w "They had fought before, and had to stop every time before they both died."
        w "As he fumed, lashing out and beating his fellow wolves in anger, we, the followers of the mercantile brother, left."
        e "And the hunting brother? What happened when you left?"
        w "I do not know what happened in the other half of the pack."
        w "I left, and never looked back."
        e "Why did you leave?"
        "Wuldon looks unimpressed with you. His bright eyes betrayed his next line before he even spoke.:"
        w "You have seen the pack today."
        w "I hear them hunting and dying like wild animals under the leadership of Uffe."
        e "But you didn't know that would happen!"
        "Wuldon's face is creased with the beginning of a disgusted snarl."
        w "Yes. I didn't. But I knew Uffe, and I knew he would become alpha."
        "Having gotten his hatred of Uffe out of his system, his face returns to its neutral, somber state."
        e "Yeah... I can see what you mean."
        e "But, why would Uffe become alpha after this?"
        w "Well, I was going to finish before you interrupted me, impatient little one."
        w "You will understand by the end of the story."
        "Wuldon is chastising you, but not unkindly, as if indulging you. He seems to have something of a soft spot for you."
        "... He also may or may not be checking you out."
        e "I understand, I'll let you continue."
        "Wuldon looks like he wants to chuckle... but as he recalls the story, he cannot seem to bring himself to."
        w "I remember we spent hours in that cave, setting up the beginnings of a support structure."
        w "Wooden beams set up between us brothers as we moved deeper and deeper."
        w "But, before we even got down to the ore..."
        "Wuldon's eyes are hollow as he approaches the true beginning of his story, his story bleeding into the present."
        w "The mercantile brother began to scream."
        w "We in the mines felt it scratching at our minds, trying to etch its agony into our beings, as it did to him."
        w "The cave shook."
        w "Our leader, this brother we trusted most, turned on us."
        w "When we looked at him, we found nobody looking back."
        w "He howled. A terrible, all-consuming sound of our basest instincts come to the fore."
        w "Rocks fell."
        w "We ran. Less than half of us made it out."
        "Wuldon looks empty as he remembers. Each death a person remembered and mourned."
        e "W-what happened to them? How did they die?"
        w "We were slaughtered by our trusted leader, and the crushing rocks he had called."
        w "As the last of us escaped, the cave's mouth shrunk, smaller than even a werewolf runt could fit through."
        w "We could hear our brothers screaming, saw their faces as they tried to make it out, as we tried to pull them out..."
        w "Invariably, they were pulled back in by the feral werewolf."
        "..."
        "Wuldon is simply looking at you, face locked into the grim features you first spied on him when you arrived."
    elif vurro_lives:
        e "Well, I found him in this cave a bit further out from here."
        e "We fought, and I knocked him unconscious."
        e "Unfortunately, our fight caused the cave to collapse. I managed to rescue him, but..."
        "Wuldon looks both relieved and concerned."
        w "But what?"
        e "Well, he's not waking up. He's been unconscious since I left the cave, and I have nowhere to hide him."
        "Wuldon turns sharply to look at you, his face filled with unease."
        w "You're not going to return him to Uffe, are you?"
        e "No, probably not, but... he is a feral animal at this point."
        w "..."
        w "Well, yes and no."
        e "What do you mean?"
        "Wuldon has an extremely complicated look on his face."
        w "Well, I suppose the best way to explain is to tell you the story of the feral werewolf and his curse."
        w "Uffe wants you to kill someone for him without even telling you who it was."
        "Wuldon's gaze has hardened somewhat."
        w "He wants you to do his dirty work. Get rid of someone he sees as an obstacle."
        "Wuldon lets out a sigh, and seems to center himself, preparing to tell a story."
        w "Once upon a time, two brothers led the dark forest tribe together."
        w "One, a domineering and predatory man who wished for his tribe to hunt in isolation from the world."
        w "The other, kinder, and more mercantile, wishing to find ways to lead his brethren out of a life of kill or be killed."
        w "One day, the mercantile brother found a cave filled with precious ores. Ores that he knew the surrounding tribes and villages wanted."
        w "Here, he saw his opportunity to lead his people out of the shadows, and into civilization."
        w "He told his pack about the cave, and told his brother about his dream."
        w "The hunting brother did not understand."
        w "This lifestyle of hunting and killing was all they had ever had. All they would ever need."
        e "This sounds a lot like something I've heard before."
        "Rather than respond, Wuldon grins a knowing grin."
        w "It was this very lifestyle that let his brother and he be alpha. They had carved their place in the tribe with their superior fangs and claws."
        w "Even if they proved this by killing their brethren, that was how things should be."
        w "The mercantile brother asked that he still be allowed to try his dream."
        w "They were equals, and they could follow both lifestyles."
        e "Could they really? It's only one pack."
        w "It was a pack with two alphas, little one. This was not the first disagreement."
        w "They had their solutions, though sometimes one or both sides were unhappy with it."
        e "What kind of solutions were they?"
        w "All will be revealed in time."
        "Wuldon's tone carries a sense of finality to it, telling you to be quiet so he can keep telling the story."
        w "In order to make sure his brother would not be disrupted, he took half of the tribe with him to the mines."
        w "The hunting brother was furious."
        w "His foolish wretch of a brother wished to betray him and their way of life."
        w "He had to be rid of him, but they were equals, as his brother had intimated."
        w "They had fought before, and had to stop every time before they both died."
        w "As he fumed, lashing out and beating his fellow wolves in anger, we, the followers of the mercantile brother, left."
        e "And the hunting brother? What happened when you left?"
        w "I do not know what happened in the other half of the pack."
        w "I left, and never looked back."
        e "Why did you leave?"
        "Wuldon looks unimpressed with you. His bright eyes betrayed his next line before he even spoke.:"
        w "You have seen the pack today."
        w "I hear them hunting and dying like wild animals under the leadership of Uffe."
        e "But you didn't know that would happen!"
        "Wuldon's face is creased with the beginning of a disgusted snarl."
        w "Yes. I didn't. But I knew Uffe, and I knew he would become alpha."
        "Having gotten his hatred of Uffe out of his system, his face returns to its neutral, somber state."
        e "Yeah... I can see what you mean."
        e "But, why would Uffe become alpha after this?"
        w "Well, I was going to finish before you interrupted me."
        w "You will understand by the end of the story."
        "Wuldon is chastising you gently. You have been interrupting a lot, so you suppose it makes sense"
        e "I understand, I'll let you continue."
        "Wuldon takes a deep breath, and begins once more."
        w "I remember we spent hours in that cave, setting up the beginnings of a support structure."
        w "Wooden beams set up between us brothers as we moved deeper and deeper."
        w "But, before we even got down to the ore..."
        "Wuldon's eyes are hollow as he approaches the true beginning of his story, his story bleeding into the present."
        w "The mercantile brother began to scream."
        w "We in the mines felt it scratching at our minds, trying to etch its agony into our beings, as it did to him."
        w "The cave shook."
        w "Our leader, this brother we trusted most, turned on us."
        w "When we looked at him, we found nobody looking back."
        w "He howled. A terrible, all-consuming sound of our basest instincts come to the fore."
        w "Rocks fell."
        w "We ran. Less than half of us made it out."
        "Wuldon looks empty as he remembers. Each death a person remembered and mourned."
        e "Having fought him, I can't imagine the feral werewolf could kill that many of you."
        e "How did they die?"
        "Wuldon lets out a hollow laugh."
        w "We were slaughtered not only by our trusted leader, but the crushing rocks he had called."
        w "As the last of us escaped, the cave's mouth shrunk, smaller than even a werewolf runt could fit through."
        w "We could hear our brothers screaming, saw their faces as they tried to make it out, as we tried to pull them out..."
        w "Invariably, they were pulled back in by the feral werewolf."
        "..."
        "Wuldon is simply looking at you, face locked into the grim features you first spied on him when you arrived."
    else:
        e "Well... I killed him."
        "Wuldon goes still."
        e "More accurately, we fought, and I knocked him unconscious."
        e "I was deciding what to do with him when the cave started to collapse due to our fight."
        e "I had to leave him behind and escape."
        "Wuldon sits down. His eyes are filled with grief"
        w "Vurro..."
        e "Who's Vurro?."
        "Wuldon turns to look at you. He is still clearly mourning, but there is a sort of grim determination written on his face."
        w "The person Uffe made you kill."
        "A sense of unease grips your chest."
        e "I thought he was just some feral werewolf, no?"
        "Wuldon lets out a humorless chuckle."
        w "In a way, yes."
        w "But no. That feral werewolf was once a man with friends and loved ones."
        "He sighs deeply, deflating slightly"
        w "One who has now died through no fault of his own."
        "There is a long stretch of silence in the conversation."
        "You are both just... looking at the floor, before Wuldon looks up at you."
        w "You know... I don't really blame you for his death."
        w "It's that rat Uffe that I hate more than ever for this."
        e "Well, from what he was saying, he just wanted to make sure the disease didn't spread..."
        "Wuldon laughs. An actual, deep laugh. A laugh filled with hateful contempt."
        w "No, little one. Knowing him, that was not why he did so at all."
        e "What do you mean?"
        "Wuldon turns to look you dead in the eye."
        w "Well, I suppose the best way to explain is to tell you the story of Vurro, and his curse."
        w "Uffe used you to kill a great man without even telling you who he was."
        "Wuldon's eyes have sharpened into flints."
        w "He got rid of an obstacle. He has no respect for others - only the veneration of the self."
        "Wuldon lets out a sigh, and seems to center himself, preparing to tell a story."
        w "So, I'm going to tell you the story of the man you were forced to kill."
        w "Once upon a time, two brothers led the dark forest tribe together."
        w "One, a domineering and predatory man who wished for his tribe to hunt in isolation from the world."
        w "The other, kinder, and more mercantile, wishing to find ways to lead his brethren out of a life of kill or be killed."
        w "One day, the mercantile brother found a cave filled with precious ores. Ores that he knew the surrounding tribes and villages wanted."
        w "Here, he saw his opportunity to lead his people out of the shadows, and into civilization."
        w "He told his pack about the cave, and told his brother about his dream."
        w "The hunting brother did not understand."
        w "This lifestyle of hunting and killing was all they had ever had. All they would ever need."
        e "This sounds a lot like something I've heard before."
        "Rather than respond, Wuldon shoots you a glare."
        w "It was this very lifestyle that let his brother and he be alpha. They had carved their place in the tribe with their superior fangs and claws."
        w "Even if they proved this by killing their brethren, that was how things should be."
        w "The mercantile brother asked that he still be allowed to try his dream."
        w "They were equals, and they could follow both lifestyles."
        e "Could they really? It's only one pack."
        w "It was a pack with two alphas, little one. This was not the first disagreement."
        w "They had their solutions, though sometimes one or both sides were unhappy with it."
        e "What kind of solutions were they?"
        w "The only ones you can make when your co-leader is a disgusting creature driven only by primal desire."
        "Wuldon's tone carries a sense of finality to it, ordering you to be quiet so he can keep telling the story."
        w "In order to make sure his brother would not be disrupted, he took half of the tribe with him to the mines."
        w "The hunting brother was furious."
        w "His foolish wretch of a brother wished to betray him and their way of life."
        w "He had to be rid of him, but they were equals, as his brother had intimated."
        w "They had fought before, and had to stop every time before they both died."
        w "As he fumed, lashing out and beating his fellow wolves in anger, we, the followers of the mercantile brother, left."
        e "And the hunting brother? What happened when you left?"
        w "I do not know what happened in the other half of the pack."
        w "I left, and never looked back."
        e "Why did you leave?"
        "Wuldon looks disappointed in you. His bright eyes betrayed his next line before he even spoke.:"
        w "You have seen the pack today."
        w "I hear them hunting and dying like wild animals under the leadership of Uffe."
        e "But you didn't know that would happen!"
        "Wuldon's face is creased with the beginning of a disgusted snarl."
        w "Yes. I didn't. But I knew Uffe, and I knew he would become alpha."
        e "Yeah... I can see what you mean."
        e "But, why would Uffe become alpha after this?"
        w "If you would let me speak, rather than interrupt me at your every whim, you would know by now."
        "There is disgust in his words. He seems to see your interruptions as a form of contempt for the story of the life you took."
        w "I remember we spent hours in that cave, setting up the beginnings of a support structure."
        w "Wooden beams set up between us brothers as we moved deeper and deeper."
        w "But, before we even got down to the ore..."
        "Wuldon's eyes are hollow as he approaches the true beginning of his story, his story bleeding into the present."
        w "The mercantile brother began to scream."
        w "We in the mines felt it scratching at our minds, trying to etch its agony into our beings, as it did to him."
        w "The cave shook."
        w "Our leader, this brother we trusted most, turned on us."
        w "When we looked at him, we found nobody looking back."
        w "He howled. A terrible, all-consuming sound of our basest instincts come to the fore."
        w "Rocks fell."
        w "We ran. Less than half of us made it out."
        "Wuldon looks empty as he remembers. Each death a person remembered and mourned."
        e "Having fought him, I can't imagine the feral werewolf could kill that many of you."
        e "How did they die?"
        "Wuldon lets out a hollow laugh."
        w "We were slaughtered not only by our trusted leader, but the crushing rocks he had called."
        w "As the last of us escaped, the cave's mouth shrunk, smaller than even a werewolf runt could fit through."
        w "We could hear our brothers screaming, saw their faces as they tried to make it out, as we tried to pull them out..."
        w "Invariably, they were pulled back in by the feral werewolf."
        "..."
        "Wuldon is simply looking at you, face locked into the grim features you first spied on him when you arrived."
    if quest22.status == 2:
        e "I... take it Uffe was the hunting brother, wasn't he."
        w "Yes. That sick excuse for a werewolf was Uffe."
        w "Is Uffe. He has not changed."
        e "And... you were among those in the mines, with..."
        "Grief briefly fills Wuldon's features, an alien look on the otherwise unerringly confident man."
        w "Vurro. Our leader, the mercantile brother Vurro."
        e "So. He is..."
        w "Yes. He is the feral werewolf you have been sent to kill."
        e "And you have no idea what happened to make him go feral?"
        w "No, but I strongly suspect Uffe had something to do with it."
        "Wuldon crosses his arms, a portrait of pent up frustration."
        e "What makes you say that?"
        "The look of frustration has only turned into an ill-contained snarl."
        w "It is the kind of thing a creature like him would do."
        e "Well... fine. We don't know what happened to him, but..."
        e "Is there no way we can... you know... save him?"
        w "Perhaps there is, but... I cannot reach him, nor do I have the expertise in medicines to find the cure."
        e "Should I... kill him...?"
        w "It is up to you, little one. I have told you his story, and it is your choice."
        "Wuldon turns to focus on drawing water from the well once more."
        w "Merely know that before his curse, he did not deserve to die alone and forgotten."
        e "...Okay."
        e "I think I will be going now."
        e "I will not tell Uffe about where you are."
        w "I appreciate it, little one. You seem to be as kind as you are handsome."
        "The entirely serious tone he took when saying that feels at odds with his words, but... you suppose he means it."
        w "Best of luck. Try to survive."
        w "And do tell me what happens with Vurro."
        jump main_slumbrous_well
    elif vurro_lives == True:
        e "I... take it Uffe was the hunting brother, wasn't he."
        w "Yes. That sick excuse for a werewolf was Uffe."
        w "Is Uffe. He has not changed."
        e "And... you were among those in the mines, with..."
        "Grief briefly fills Wuldon's features, an alien look on the otherwise unerringly confident man."
        w "Vurro. Our leader, the mercantile brother Vurro."
        e "So. He is..."
        w "Yes. He is the feral werewolf you were sent to kill."
        e "And you have no idea what happened to make him go feral?"
        w "No, but I strongly suspect Uffe had something to do with it."
        "Wuldon crosses his arms, a portrait of pent up frustration."
        e "What makes you say that?"
        "The look of frustration on his face deepens, turning into an ill-contained snarl."
        w "It is the kind of thing a creature like him would do."
        e "Well... fine. We don't know what happened to him, but..."
        e "Is there no way we can... you know... save him?"
        w "There might be..."
        w "I do not have the expertise in medicine to save him, but I believe I may be able to help him."
        w "If you tell me where you left him, I can go get him, and bring him back to my home."
        "Wuldon looks somewhat hopeful."
        e "I suppose I can do that."
        e "How do you plan on trying to find a cure though?"
        "Wuldon spends a while deep in thought before answering you."
        w "I know a few herbs that might be able to help. I will need to trial and error them."
        w "This would of course be faster with an alchemist, but..."
        "Wuldon gestures around him."
        w "As you can see, we have a relative paucity of alchemists around these parts."
        "You immediately think of Haskell, but remember his reluctance to mix potions."
        e "Well, I'll see if I can figure out some way to help."
        e "For now, though, you can find Vurro hidden in a large bush to the right of the collapsed cave."
        w "Thank you, little one."
        "Wuldon's voice is a grateful growl. It seems he genuinely appreciates your desire to help."
        w "I will be heading there now. I do not want to risk Uffe or any of his minions finding Vurro first."
        w "I hope to talk to you later."
        "And with that, Wuldon turns around and begins to quietly make his way through the forest, in the direction of the cave."
        e "See you later!"
        jump main_slumbrous_well
    else:
        e "I... take it Uffe was the hunting brother, wasn't he."
        w "Yes. That sick excuse for a werewolf was Uffe."
        w "Is Uffe. He has not changed."
        e "And... you were among those in the mines, with..."
        "Grief briefly fills Wuldon's features."
        w "Vurro. Our leader, the mercantile brother Vurro."
        e "So. He is..."
        w "Yes. He is the feral werewolf you were sent to kill."
        e "And you have no idea what happened to make him go feral?"
        w "No, but I strongly suspect Uffe had something to do with it."
        "Wuldon crosses his arms, a portrait of pent up frustration."
        e "What makes you say that?"
        "The look of frustration on his face deepens, turning into an ill-contained snarl."
        w "It is the kind of thing a creature like him would do."
        e "Well... fine. We don't know what happened to him, but..."
        e "Is there some way we can find out?"
        w "There might be, but... I don't really care."
        w "Vurro is dead."
        "There is a long silence."
        e "So... what will you do now?"
        w "I don't know."
        w "For now, live out here. Think about things for a while."
        w "After that...?"
        "Wuldon's eyes turn cold."
        w "Find the most painful way to kill Uffe I can think of."
        "..."
        "..."
        e "Oh."
        e "Well, I'll... leave you to that. I'm sorry about Vurro."
        "There is a long pause."
        w "Yes. I do not blame you, as I said before."
        w "Goodbye. We may meet again. Until then."
        e "Until then."
        "With that, you get out of there as quickly as you can without running."
        jump main_slumbrous_well

screen place_slumbrous_well():
    zorder 10 tag place

    if wuldon_location == slumbrous_well:
        if vurro_lives:
            imagebutton:
                focus_mask "wuldon_sprite_idle"
                idle "wuldon_sprite_idle"
                hover "wuldon_sprite_friend_hover"
                action Return("Wuldon")
        else:
            imagebutton:
                focus_mask "wuldon_sprite_idle"
                idle "wuldon_sprite_idle"
                hover "wuldon_sprite_revenge_hover"
                action Return("Wuldon")
    else:
        imagebutton:
            focus_mask "slumbrous_well_door"
            idle "empty"
            hover "slumbrous_well_door"
            action Return("Door")

    imagebutton:
        xalign 0.4
        yalign 0.95
        idle "kingspawn_arrow"
        hover "kingspawn_arrow_hover"
        action Return("To Dark Forest")

    if not hasTrinket("Bruisers Bite") and LookForItem("Bruisers Bite", discoveredtrinket):
        imagebutton:
            focus_mask "slumbrous_well_barrel"
            idle AlphaMask("slumbrous_well", "slumbrous_well_barrel")
            hover AlphaMask(dayHover("slumbrous_well"), "slumbrous_well_barrel")
            action Return("Barrel")
    if vurro_lives and vurro_location == slumbrous_well:

        imagebutton:
            focus_mask "vurro_sprite_idle"
            idle "vurro_sprite_idle"
            hover "vurro_sprite_hover"
            action Return("Vurro")


label main_slumbrous_well:

    $ current_location = slumbrous_well
    $ renpy.music.play(mWell, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ wilderness = True
    $ timenow.minute += 15
    $ timenow.passTime()
    scene slumbrous_well with dissolve
    show screen menu_buttons
    $ wuldon_location = "None"
    $ vurro_location = "None"
    if quest27.status == 4:
        "Arriving at Wuldon's house, you see the big blue werewolf sitting on a chair outside."
        "Taking a closer look, you can tell that his eyes are closed. You think he's messing with you until you hear a quiet snore from him."
        "Grinning, you sneak over close to Wuldon, making sure not to snap any twigs this time."
        "Just as you're about to try and spook him, you see one of his eyes snap open."
        w "Good morning little one. You didn't really think you'd be able to catch me sleeping, did you?"
        e "..."
        w "..."
        e "I was hoping I would."
        "Wuldon chuckles, getting up out of his chair."
        w "Well, maybe next time."
        w "For now, let's go take care of Vurro. Follow me."
        jump Wuldon_Cure_Vurro
    if quest30.status == True and quest30.completed_date +1 < timenow.day and quest31.status == False:
        jump Wuldon_Slime_Country_Curse
    if quest27.status == True and not asked_mine and quest27.completed_date + 2 < timenow.day:
        jump Wuldon_Vurro_Mine_Quest
    if quest31.status == True:
        "You walk up and knock on Wuldon's door."
        "There is no answer."
        "He's either not here, or doesn't want to talk to you right now."
        jump Dark_Forest_Map
    if quest41.status == 2 and quest41.start_date < timenow.day and 7 < timenow.hour < 11:
        jump Wuldon_Raid_Planning
    if quest28.status == 2:
        if quest28.start_date < timenow.day:
            jump Wuldon_Vurro_Cavern
    call screen place_slumbrous_well

    if _return == "Door":
        if quest22.status == 2:
            jump Wuldon_Cavern_Return_Early
        elif quest27.status == True and quest27.completed_date + 5 < timenow.day and ((quest28.status and quest28.completed_date + 5 < timenow.day) or (quest28.status != True)) and quest41.status == False:
            jump Wuldon_Raid_Preparation
        elif quest22.status == True and quest22.completed_date + 3 < timenow.day and quest30.status == False and vurro_lives == False:
            jump Wuldon_After_Vurro_Death
        elif quest22.status == True and quest22.completed_date + 1 < timenow.day and quest22.completed_date + 3 >= timenow.day and (quest26.status == False and quest30.status == False):
            jump Wuldon_After_Cavern_Talk
        elif quest27.status == 2:
            jump Wuldon_Meeting_Shop
        elif quest27.status == True and not asked_mine:
            jump Wuldon_Check_Vurro
        elif quest28.status == True:
            jump Wuldon_After_Cave
        else:
            "No one opens the door when you knock on it. They are either not here, or too busy to hear you."
    if _return == "Barrel":
        jump Bruisers_Test
    if _return == "To Dark Forest":
        jump Dark_Forest_Map

    jump main_slumbrous_well

label Bruisers_Test:
    $ bruiserstest = MapPat([], "Slumbrous Well", 3, 2, "grass2", background = "slumbrous well")
    $ bruiserstest.floorPlan([
    [4, 8, 8, 8, 8, 9, 9],
    [5, 0, 0, 0, 0, 9, 9],
    [0, 0, 0, 0, 0, 3, 3],
    [5, 0, 0, 0, 0, 0, 5],
    [9, 9, 9, 0, 0, 0, 5],
    [3, 3, 3, 5, 4, 5, 4]
    ], viscid_stream_map)
    $ addSprite(bruiserstest, bruiserstest.playerSprite)
    $ barrel_sprite1 = MapUser(4, 2, "barrel_sprite", 120, 120, "Barrel")
    $ barrel_sprite2 = MapUser(3, 3, "barrel_sprite", 120, 120, "Barrel")
    $ back_sprite = MapUser(0, 2, "grass3", 120, 120, "To Well")
    $ addSprite(bruiserstest, barrel_sprite1)
    $ addSprite(bruiserstest, barrel_sprite2)
    $ addSprite(bruiserstest, back_sprite)
    $ addBackQuick(bruiserstest, 4, 2, "crosssign_sprite")
    $ addBackQuick(bruiserstest, 2, 2, "crosssign_sprite")
    $ current_location = bruiserstest
    jump Bruisers_Test_Loop

label Bruisers_Test_Loop:
    show screen dungeon_buttons
    $ disableC = False
    $ sprite = bruiserstest.playerSprite
    call screen dungeon_map(bruiserstest)

    if _return == "To Well":
        menu:
            "Leave the area to this placement of barrels?"
            "Leave":
                if bruiserstest.getSprite(4, 2) and bruiserstest.getSprite(4, 2).img == "barrel_sprite":
                    if bruiserstest.getSprite(2, 2) and bruiserstest.getSprite(2, 2).img == "barrel_sprite":
                        "The ground rumbles and a green bush appears ahead, it seems you have successfully passed the test."
                        "You walk towards the bush, and discovers a trinket on the ground, a bitten mushroom that smells like blood."
                        "You pick it up and put it in the bag, and continue on your path to the well."
                        $ addTrinket(bruisersbite_item, tinventory)
                hide screen dungeon_buttons
                jump main_slumbrous_well
            "Reset":
                jump Bruisers_Test
            "Stay"


    jump Bruisers_Test_Loop


label Wuldon_After_Cave:
    "No one opens the door when you knock on it. They are either not here, or too busy to hear you."
    msg "Author's Note: The final stage (stage 4/4) of the werewolf plot line isn't ready yet."
    jump main_slumbrous_well
label Wuldon_After_Vurro_Death:
    $ QuestBegin(quest30)
    $ quest30.qProgress(__("Wait for a few days"))
    "..."
    pause 1
    "The forest is oddly silent as you approach Wuldon's house."
    "The only sounds you can hear are the quiet gurgling of the stream, and the soft rustling of the leaves underfoot."
    e "Hello? Is anyone there?"
    pause 1
    "Silence. Your voice echoes out into the woods."
    "As you turn around to leave, you see Wuldon far back on the path behind you, holding his khopesh."
    pause 1
    show wuldon nobo with dissolve
    w "Hello, little one."
    w "I heard you while I was on my way to pay my respects at Vurro's grave."
    "Already you feel uncomfortable. The werewolf in front of you seems void of any emotion, his body driven only by purpose, or some vague promise."
    w "Would you like to come along with me?"
    "Again, there is no intonation. Despite that, you get the feeling ,Wuldon isn't quite asking."
    "Not that he'd harm you if you said no... you think. It's more that he understands how guilty you feel about the death of his friend."
    e "Y-yes. I think I would like to go and apologize to him."
    pause 2
    "Look at you. You can't even say his name properly."
    "Wuldon says nothing, only turning around and heading off, leaving you to run after him."
    "In complete silence, the two of you make your way over to the cave where Vurro died."
    scene black with dissolve
    "When you get there, the front of the cave is nothing but a pile of rocks."
    "Less of the cave collapsed than you thought, but still enough to kill the poor werewolf inside."
    "Wuldon leads you forwards, onto the pile, towards a specific group he has covered with flowers."
    "While at first you can't realize why he placed the flowers where he did, soon you see the small splotches of red underneath each of the stones with flowers on them."
    e "He... he was much smaller than that. What happened?"
    pause 1
    "The living werewolf next to you turns."
    "You can see in his eyes that he should feel angry. He chooses to express nothing."
    w "Blood splatters far under immense weight."
    "Shivering, you take him at his word."
    "The two of you stand there in silence, looking out at Vurro's remains."
    pause 1
    w "I'm going to kill Uffe."
    "You turn to look at him in alarm, but Wuldon either doesn't notice, or doesn't care."
    pause 1
    w "I'm going to kill Uffe, and you're going to help."
    "Again, not a question. You're about to ask why you would, when he speaks again."
    w "You're going to help me, because if you don't, the guilt will eat you whole. There will be nothing left of you but a husk of who you were."
    "As if unaware of what he just said, he bends down to pick up one of the rocks with Vurro's blood on it."
    pause 1
    w "If I don't, I will be eaten whole."
    if wuldon_meet_before_vurro:
        "He did everything he could to prevent Vurro's death when he talked to you, but he still sees it as his fault."
        "Then again, you could say much the same, and you're about to help someone kill another out of that same guilt."
    else:
        "Considering that he left Vurro alone in that cave for what might have been years, it makes sense that he'd be beating himself up over it."
        "...Not that actual guilt matters, considering you feel awful for killing Vurro despite thinking he was a wild animal when you did."
    "As you roll the thoughts around in your head, Wuldon takes the opportunity to do some thinking of his own."
    "He turns to you, bloody rock in hand, and asks you a question you wish you didn't know the answer to."
    pause 1
    w "Do you know anybody who could tell me about Vurro's curse? How it came about, how it could be spread. Anything."
    "A nervous gulp later, and you're ready to answer."
    pause 2
    e "Yes, I know of one."
    e "He's an alchemist that goes by the name of Haskell, he doesn't actually like ma-"
    "Wuldon cuts you off without warning."
    w "Take me to him."
    pause 1
    "It's difficult to muster up the courage, but you feel you have to ask."
    e "Can I trust you not to hurt him?"
    "For the first time today, you see a flash of emotion in his eyes, one of pure anger and frustration."
    w "I'm not going to hurt anybody that doesn't deserve it, unlike a certain someone."
    w "I am still the person I was, I am just ridding the world of a pest before I have the luxury of kindness."
    pause 1
    "Done with tearing you apart verbally, Wuldon once more returns to a state of active calm."
    e "...Then yes, I'll take you to him."
    e "I can't promise he'll help, but he should at least give something of value."
    "Wuldon just nods at you, and gestures for you to get going."
    pause 1
    scene alchemistscabin with dissolve

    "Reluctantly, you begin picking your way through the Dark Forest, and over to Haskell's house."
    pause 1
    "Once again, neither of you say a word. You could cut the tension with a knife, but any knife you knew of would snap at the haft in trying to do so."
    "After what feels like years, you arrive at Haskell's. Never before having you wanted to see the red dragon this badly, if only to save you from this fresh hell."
    e "Haskell? I'm here with a guest!"
    pause 2
    "There is a moment of silence before you hear the sound of a tea kettle go off."
    "His tea thus having finished, you hear him pour some into a mug, before going and opening the door."
    show haskell normal at l2
    show haskell normal at l1 with move
    h "What do you want."
    e "...Help? If possible?"
    "The dragon glances at you suspiciously, before looking at Wuldon in much the same way."
    pause 1
    h "With what? I might consider it if it's not a potion."
    e "Well..."
    "You fidget nervously, not knowing how to broach the topic. Wuldon does it for you."
    show wuldon nobo at r1 with dissolve
    w "He killed a friend of mine who had gone insane under the effects of a curse. It was not his fault, but I want to know what happened and why."
    "Haskell pauses in taking a sip from his mug of tea."
    pause 1
    h "I'm genuinely sorry to hear that."
    "Considering this is the first time you've ever seen him look anything close to mournful or remorseful, you can only assume he's telling the truth."
    w "Unimaginable horrors occur everyday. I would like to stop some of them from happening. Can you help tell me what happened."
    "The mourning in Haskell's face has shifted to unease now, having picked up on Wuldon's emotionlessness, and pure determination."
    h "Alright. I don't know how much I can help, but I might as well give it a go."
    w "Thank you."
    pause 2
    scene haskellhut with dissolve
    show haskell normal at l1
    show wuldon nobo at r1
    "The werewolf moves to go into the hut, Haskell moving to let him go through."
    "You go to enter as well, reaching the door as Wuldon sits down and drops the bloody rock on the table with a dull thud."
    "He waits, motionless, for the two of you to sit down."
    "Haskell refuses to once he sees the stone."
    pause 2
    h "I understand you are grieving, but that rock is going to have to be explained before I sit down."
    "Wuldon looks up at him with empty eyes."
    w "This is one of the rocks from the cave that collapsed on Vurro."
    w "It has his blood on it. I thought it would be useful to you in researching his curse."
    "Haskell moves over and picks up the rock, making sure to touch none of the blood."
    h "...You're right, it will help me. I would have preferred some warning, but I'll cut you some slack."
    h "I'm going to need you to give me some time before I can tell you what happened - or at least, some of the mechanisms of it."
    h "You can stick around, but I'd recommend coming back in a few days."
    pause 1
    "Wuldon makes no move to leave - reason enough for you to get out of here."
    e "Alright, I'll see you then."
    pause 1
    "Haskell immediately regrets saying that Wuldon could stay. It's not going to be a fun few days for the dragon."

    "You leave before Haskell can figure out a way to get you to stay."
    jump main_alchemists_cabin
label Wuldon_Slime_Country_Curse:
    $ QuestBegin(quest31)
    $ quest31.qProgress(__("Visit the Slime... Country with Wuldon"))
    "When you arrive at Wuldon's house, the werewolf is already outside with his khopesh at the ready."
    show wuldon nobo with dissolve
    w "Slime country is up north."
    pause 1
    w "I researched the two slimes we need to kill. They're both in the same area, in an arena."
    "You give Wuldon a confused look."
    e "An arena? Like, a ring you fight in for rewards?"
    "The werewolf nods without betraying any emotion."
    w "Slime country is named for the odd behaviors of its slimes. They often hide behind puzzles and traps, or engage with visitors in very specific circumstances."
    "Of all creatures, slimes seem the least likely to think, but if they like puzzles, then you have to wonder how accurate that is."
    w "The arena only allows one fighter in at a time - you cannot fight twice in a row, somebody else has to challenge it after you."
    w "That's the only reason I'm taking you with me."
    "Ouch. You didn't think it would be because he liked you, but it still hurts to see your worth reduced to that of literally any other person."
    pause 1
    e "What happens if two people go in at once?"
    w "Nobody comes out. It is irrelevant."
    "Seeing the explanation as complete, Wuldon begins marching off towards slime country."
    scene black with dissolve
    pause 2
    scene dark_forest with dissolve
    "The walk is once again, quiet. This gives you the perfect opportunity to hear how the sounds of the forest change as you go along."
    "The Dark Forest is filled with the sounds of clicks and scrapes - moles and beetles being the prevalent species."
    "As you move towards Slime Country, the sounds slowly shift to wet slopping noises, the animals of the area slowly being replaced by slimes."
    "Even the trees start to look different, near-black evergreens gaining a bright green sheen, before changing to have thicker leaves and thinner branches."
    "The nettle underfoot changes to reflect that, eventually becoming a bright green muck that sucks on your boots as you trek through it."
    "In the distance, you see marble pillars and gates standing or lying down, but always cracked and weathered."
    "The fact that you walk past them, ignoring them, makes you think these aren't what you're looking for."

    "It's after the 8th such area that you reach your destination."
    pause 2
    scene forgotten_sanctuary with dissolve2
    "A tall white circle of Marble, maybe 200 feet in diameter, stands in front of you."

    "It is clearly constructed, with crenellations and small signatures in the marble confirming the theory you've slowly formed as you went through slime country."
    "Interestingly, this is the only such structure you've seen that wasn't four-sided - perhaps due to a difference in purpose."
    "Regardless of all that, here is where Wuldon turns around to look at you, hand tight around his weapon."
    show wuldon normal with dissolve
    w "This is the arena. I will be going first to give you an idea of how this works, but I expect you to enter and fight after I finish."
    "So saying, the werewolf turns around and enters the structure through an absurdly large, imposing archway through the front."
    "Once again, you have to wonder who could have built this. Only a giant would need a gate like this, but those are only myths and fables. At least... in your world."
    "Whatever was here, the slimes have replaced them, a fact made abundantly clear as you enter after Wuldon."
    "The circle forms a bowl on the inside - a bowl with a flat bottom of marble coated in ooze."
    "The sides of the bowl are covered in stairs, where you can see hundreds of slimes... watching? The floor."
    "You can see Wuldon making his way downstairs, and you make to follow, only to be interrupted by a slime with what seems to be a vest inside of it."
    show wuldon normal at l2 with move
    hide wuldon
    "Most of the slimes here have something similar in them now that you think about it."
    "The one currently in front of you is shaking violently, agitated little bubbling sounds coming out of it every time you try to move forwards."
    "When you stop in front of it, it calms down and slowly slides towards the stairs."
    "You start going up the side of the bowl, and look down at the slime - an odd thought to have, honestly - to see if it's still agitated."
    "It is standing where it was when it guided you to the stairs, much more calmly than previously."
    "You find a seat as far away from the other slimes as possible, taking you rather high up, where you have a pretty good view of the arena floor."
    "Just as long as you're willing to strain your eyes, that is."
    "As you get settled, you take a look around and see what seem to be rows of weapons, all of them of rather high quality, if you were willing to look past the slime and rust covering them."
    "All of them seem to be quite well worn, a sign that whatever purpose they have comes quite often."
    "You're left to your own devices for longer than you expected. After what feels like ages of looking at an empty field, you see Wuldon and a slime emerge come out onto the field."
    "There is a sound coming from all around you, like someone is popping their knuckles repeatedly."
    "Looking for the source, you see the slimes in your area rapidly opening holes in themselves to create a vacuum, and then breaking them. Each time they do this, a pop is heard."
    pause 1
    "This is only able to distract you for a moment, as your attention is grabbed incredibly quickly by the sight of Wuldon."
    pause 1
    show wuldon nakednobo with dissolve
    "He's completely naked, stripped of everything but his khopesh."
    "His stomach bounces slightly with every step he takes, if far less than it would had it been all fat, the muscle helping keep things compact."
    "You can see a surprisingly short, if not small, package bouncing along beneath as well, a fat cock and balls swinging freely as he walks out onto the field."
    "This, and his plump-but-firm ass are almost enough to distract you from the fact that Wuldon still looks vacant of anything but determination."
    "The pair walk out onto the field, and walk a short distance away from each other."
    "Both figures are giant, the slime somehow managing to be slightly larger than Wuldon."
    "If you fight something like that, you're pretty sure you're going to be in trouble."
    "A slime with a checkered shirt inside of it slides over to the edge of the arena."
    "It pops once, twice, and on the third pop, Wuldon and the slime explode into action."
    "The fight is over in a flash."
    "The slime was rushing forward one moment, and the next, Wuldon was on the other side of the arena, khopesh covered in slime, a slime core in his hand."
    "Silence fills the arena, the pops of the other slimes stopping as the slime Wuldon fought dissipates, joining the ooze covering the floor."
    pause 2
    w "I nominate [e] as the next participant."
    "With that, Wuldon jumps out of the pit, and walks up to where you're sitting, stunned."
    hide wuldon with dissolve
    w "You need to go down there and do your own fight."
    w "Clothes are banned - it's unfair to the slimes, and they won't fight you as long as you have them on."
    pause 1
    e "Alright, well. Here goes nothing."
    "You take a nervous gulp, get up, and obediently begin to strip."
    "Once you are completely naked of even your accessories, you pick up your weapon, and dash down to where you saw Wuldon disappear."
    "You find yourself in a poorly lit room, bare of practically anything, except for Wuldon's clothes over in the corner."
    "Wuldon's loincloth is at the top of the pile, the last thing he took off. A sudden urge overtakes you."
    menu:
        "Do you sniff Wuldon's loincloth?"
        "Yes{#sniffwuldon}":
            $ wuldon_sniff = True
            "Tentatively, as if afraid to be caught - which you are - you reach over for Wuldon's loincloth."
            "The fabric hangs loosely between your fingers as you bring it up to your nose."
            "It seems that the werewolf bathes fairly often, as the smell is not quite that strong, but you can definitely catch a whiff of earthy musk, likely from the walk over here."
            "The smell is intoxicating, and frustratingly thin, growing elusive every time you get close to being satisfied with it."
            "He has the smell of a working man, a mix of sweat and musk coming together to create a rich scent."
            "You put Wuldon's loincloth back where it was sooner than you'd like, knowing that you have to get out into the arena soon if you don't want people asking questions."
        "No{#sniffwuldon}":
            e "I'm better than that."
            e "Plus, Wuldon and I aren't even friends right now. I mean, I killed his best friend for god's sake."

    $ wslime_progress += 1
    jump Slimy_Fight_Begin
label Slimy_Fight_Begin:
    $ pc.stripAll()
    scene forgotten_sanctuary with dissolve
    $ pc.sleep()
    if wslime_progress == 1:
        "You head out onto the field, where a slime is now waiting for you, emerging from a room much like your own."
        "It is far larger than you. Larger even than Wuldon's opponent."
        "The two of you meet in the middle before stepping back a few feet."
        "Once again, the checker slime pops three times, starting the fight."
    elif wslime_progress == 2:
        if wslime_lost <= 0:
            "You lay there, panting, after taking down the giant slime."
            "Even if the slime didn't hurt you that much, the muck beneath you made every step that much harder."
            "This isn't done, however. Wuldon is already climbing down for his round."
            if enemy.lust > 60:
                "His face betrays nothing about how he may feel about how you won, but his cock definitely seems a bit bigger than before, if not hard."

            "You get up off the floor and back towards your seat."
            "You're given a canteen full of what looks like purple muck on your way up."
            "A gift from the slimes of the arena it seems."
            "You're too tired and thirsty to think twice, and you drink from it."
            "Health and Mana fully restored!"
            "The concoction tastes surprisingly good."
            "It's like if someone mixed grape juice, milk, and honey together, and then made the unfortunate decision of turning it all into jello."
            "Reinvigorated, you take a seat and watch Wuldon's match."
            "Or at least, you were going to, when you realize that Wuldon is already wiping his khopesh clean of his opponent."
            "You get ready to head back down when another slime enters the ring to fight the werewolf."
            w "Waves. This will be time consuming."
            "You somehow hear Wuldon from all the way up here."
            "Ultimately, however, you find that he's right."
            "However quickly he finishes off each individual enemy, it takes him a while to chunk through the twenty enemies that go to fight him."
            "By the end, even he's exhausted."
            "Once declared the victor, Wuldon walks out of the arena, and up to where you are, tagging you in."
            w "It would be best if you didn't get what I did. It's rough work, and I'm not sure you'd make it."
            "You can't help but agree. Still, you're going to have to go and see what nasty surprise they have waiting for you."
            "Little time is spent on the way down this time - you know full well where you're going."
            "As you emerge onto the field, you see a small slime."
            e "It's going to be waves isn't it."
            "The slime in front of you wiggles slightly in response. You couldn't tell what it said even if someone gave you three thousand gold."
            "For now, let's just assume a yes."
            "This is going to be an endurance battle, where I'll want to come out as close to fresh as I can after each battle."
            "The lack of clothing means you have none of your items, so resource management is going to be tight, especially if there are twenty, like Wuldon had."
            "Nothing for it but to get in a fighting stance."
        else:
            "That wasn't that bad, especially now that you're getting used to the muck on the floor."
            "Here comes another one."
    elif wslime_progress == 3:
        "You can definitely feel the fights wearing on you, but you have a lot of fight left. Send in the next one, let's get it over with."

    elif wslime_progress == 4:
        "One more."
    elif wslime_progress == 5:
        e "Oh God, when will this end. Please tell me it's only five I have to beat."
    elif wslime_progress == 6:
        "Oh no, it's more than five, what is it, ten?! Please don't be twenty like Wuldon had to deal with."
    elif wslime_progress == 7:
        "Each of these slimes has been identical to the last. It feels like you're trapped in a neverending hell."
    elif wslime_progress == 8:
        "Whatever you did to get here, you're sorry. God, Wuldon, anything out there, please, help."
    elif wslime_progress == 9:
        "You're covered in slime, though you can barely feel it. Whatever happens in the end, you'll at least have the resources you need."
        $ wslime_progress += 1
        jump malignantslime_battle
    else:
        jump Wuldon_Slime_Country_Curse_End
    $ wslime_progress += 1
    jump heftyslime_battle
label Slimy_Fight_Lose:
    $ wslime_lost += 1
    "You fall unconscious in front of one of the slimes."
    "They hit softly, but something about them tires you out when you fight them."
    "..."
    "You wake up outside of the arena with an expressionless Wuldon in front of you."
    w "You're a newcomer, so they'll let you pick up where you left off. Special treatment."
    w "You can also leave and prepare a bit."
    "The flat look he gives you tells you what he thinks of that plan."
    $ wslime_progress = 1
    menu:
        "What should you do?"
        "Rechallenge":
            jump Slimy_Fight_Begin
        "Recoup":
            e "I think I'll prepare."
            "Wuldon tosses your clothes at you. He's still not wearing his."
            w "I'll be at the arena."
            "Within moments, he's back inside of the arena."
            jump Dark_Forest_Map

label Slimy_Fight_Recoup:
    scene forgotten_sanctuary with dissolve
    "You're back at the slime arena."
    "You don't know what you expected, but it wasn't a slowly wobbling slime at the entrance."
    "It tentatively reaches out for your hand. You let it grab you."
    "The little thing begins to drag you into the arena, and down into the changing room."
    "Understanding its demands, you quickly strip once it leaves, and step into the arena's fighting grounds once more."
    jump Slimy_Fight_Begin

label Wuldon_Slime_Country_Curse_End:
    scene forgotten_sanctuary with dissolve
    "You stand there, panting, your feet struggling to find a grip in the slime below."
    "Waiting for the next slime has started to feel like an eternity."
    "You stand in that eternity, taking in gulps of air as you slowly realize that nobody is coming."
    "The adrenaline rushes out of you, the desperate energy in your muscles giving out as you collapse onto the floor."
    "Whatever happens next, you'll never know. The world loses its color as you sink into a deep sleep."
    pause 1
    scene black with dissolve

    scene forgotten_sanctuary:
        blur 8
    with dissolve
    pause 1
    scene black with dissolve
    scene forgotten_sanctuary:
        blur 40
    with dissolve
    pause 2
    scene black with dissolve
    "..."
    "..."
    "You wake up to the feeling of your body being dragged on the forest floor by Wuldon."
    "He had the decency to keep your head off the floor, as well as clothe and heal you, but your feet almost definitely have some bruising on them from this."
    "However undignified it is, you're too tired to complain, let alone walk, so you just stay quiet for the walk."
    w "We got what we needed."
    w "You were covered in one of the ingredients, and I collected one of them from the first slime I fought."
    w "I'm taking you home so we can make the mixture and get ready for war."
    "You hate the certainty with which he speaks."
    "While you'd love to get up and tell him you weren't going, the fact that you killed his best, and quite possibly only friend keeps you from doing so."
    "That, and you can't really say he's mistreated you."
    "The worst he's done has been this, and even then he went through the process of patching you up and getting everything on you, which had to be no small task."
    pause 1
    "So, you keep your mouth shut, and you let the werewolf take you where he wants."
    "At some point, you decide to get some rest again. Those fights left you more worn out than you've been in a long while."
    "..."
    "The next time you open your eyes, you're seated at Wuldon's house."
    scene wuldonshack with dissolve
    "In front of you, there are three jars. One has a thimble of water mixed with dried blood, another is filled with a dimly glowing dark purple sludge, and the last has what looks like pureed vomit coated along the inside."
    "How appetizing."
    e "Are you there, Wuldon?"
    "The werewolf comes in through the door, fresh vegetables in his hands."
    show wuldon normal with dissolve
    w "You're awake."
    w "You took long enough that I went out and gathered food for myself."
    "He sets down what you assume to be said food on a shelf, and moves over to the table."
    w "Mix these for me. I would, but alchemy is one of the things I have no talent for."
    "Wuldon sits down in front of you to watch, as you gingerly reach out for the three jars."
    "It really isn't a complicated process. All it consists of is pouring the contents of the other two jars into the one with Vurro's blood."
    "The disgusting elements swirl together and become exponentially worse in the others presence."
    "The vomit and sludge meld to become some form of bright brown, with yellow globs of... something, floating around in it."
    "While those two combined instantly, it takes a bit for the blood to seep in, letting you watch as it moves up the jar in a horrid, slow wave."
    "If the mixture was disgusting before, it is now offensive to one's very being."
    "Aesthetically, it is beautiful, a light purple substance that shines like diamond in the light."
    "Despite that, every nerve in your body is screaming when you look at it."
    "Something about its very essence triggers a need for violence in you, the memory of a torture you never went through flooding your mind."
    "You catch yourself and look away, panting."
    e "I'm pretty sure it works."
    "Being careful not to look at the mixture, you move to check on Wuldon."
    "The werewolf appears to be transfixed by the liquid."
    "He is not breathing hard like you were, nor is his body tensed."
    "He looks exactly the same as he has these past few days."
    "You shiver thinking about what that might mean."
    e "Wuldon, I think it works."
    "He looks up at you slowly."
    w "Yes, it should do."
    w "Come back to me when you're ready to kill Uffe."
    w "Everything on my end is ready. It is only a matter of the conditions being right for the occasion."
    "God, this sucks."
    e "Yeah, I will."
    "There isn't anything more you can think to say."
    "Nor do you think Wuldon cares about what you could say right now."
    "All you can hope for is that the werewolf wakes up from whatever fugue he's in once he's gotten his revenge."
    $ QuestFinish(quest31)
    jump Dark_Forest_Map

label Wuldon_Vurro_Cavern:
    "Ready to start your adventure into the caves, you walk up to Wuldon's front door."
    "Nobody spooked you on the way here this time. Either Wuldon was too busy for his antics, or your wariness kept him at bay."
    "You raise your fist to knock on the door, only for it to open just before your hand met the wood."
    scene wuldonshack with dissolve
    "Standing in front of you is Wuldon. The Big Blue Werewolf is looking down at you approvingly."

    show wuldon normal at l1 with dissolve
    if wuldon_like > 4:
        w "Looking good, little one."
        "There's a small smirk on his face."
        w "It won't help you where we're going, but I certainly don't mind."
        "You raise an eyebrow at that."
        e "Aren't you worried I'll get hurt or something?"
        "A merry glint sparkles in Wuldon's eye, as he leans against the doorframe."
        w "I thought you felt safe around me?"
        "You take a nervous gulp, working up the courage to continue this."
        e "Are you saying you'll protect me?"
        "Wuldon reaches out, cupping your face slightly. You don't know when it happened, but he's suddenly far closer, looming over you."
        w "I promised, didn't I?"
        "You move to close the gap between the two of you, only for a loud coughing noise to come from behind you."
    v "Is that [e]? I can't tell, because a certain someone is blocking the door."
    show vurro clothed at r1 with dissolve
    "Wuldon immediately turns around and steps out of the way, but not before giving Vurro a look of amused skepticism."
    "As your eyes move over to Vurro, you see what he's wearing. A leather shirt and pants, armbands, and of course:"
    "A green cape like Wuldon's."
    "There also appears to be some odd buckle on his head, but whatever it is is unknown to you."
    e "Could you not tell it was me? Wuldon always seems to be able to tell."
    v "I don't know your scent and sounds as well, but yes, I could tell. I just wanted Wuldon to get out of the doorway."
    e "...Alright. Well, I'm here now."
    v "Yes, you are! Ready to head out?"
    "You check over your inventory one last time."
    e "I think I am, yes."
    v "Good. Now, let's get out there."
    "Vurro points at a bag over on the right side of the room."
    "You hadn't noticed it previously, but Vurro and Wuldon have their own bags near them - on them, in the case of Vurro."
    e "Caving supplies I assume?"
    w "About a week's worth of food and water, should you ration it properly, two buckets, a pickaxe, and a flint and steel with tiny sticks."
    "You look at Wuldon curiously."
    e "This isn't enough wood for a fire. Why the firestarter's kit then?"
    w "Darkfog. There's are invisible, odorless zones in the mines sometimes."
    w "If you're not careful, you'll drown in them."
    "You wait for further explanation, but you get none out of Wuldon."
    v "The only way to get rid of darkfog, at least that we know of, is to burn it."
    e "So, the mines will not only have dangerous monsters, but invisible kill zones."
    "Vurro gives you a nod."
    v "You can always back out if you want."
    "You shake your head, determined to see your promise to its completion."
    e "No. I'll be heading in there. I can hold my breath for a long time anyways, so I'll be fine."
    w "I'll be the one scouting for darkfog anyways. You just worry about the monsters."
    "You head over to pick up your bag, hefting the surprisingly heavy load onto your back."
    e "Well, I'll hold you to that. Monsters I can handle just fine."
    "Both werewolves give you a nod, readying their packs and heading out the door as they see you get ready."
    scene slumbrous_well with dissolve
    show wuldon normal at l1 with dissolve
    show vurro clothed at r1 with dissolve
    w "I've already scouted ahead a bit, so we have an entrance in mind."
    w "It's good that you can hold your breath for a long time."
    e "What do you mean by that?"
    "Wuldon just picks up the pace as Vurro snickers from his spot next to you."
    show wuldon normal:
        easeout 4 xalign -2.0

    e "Hey-"
    show vurro clothed at c1 with move
    "You bite your tongue trying to talk and move at this pace, causing Wuldon to slow down slightly."
    v "It's alright, we promise it's nothing dangerous. You'll see when we get there."
    e "I'm scared of what 'not dangerous' means to you two after darkfog, but alright."
    e "How {i}did{/i} you two start going out on trips like this, anyways?"
    v "You mean exploring new places and scouting out their worth for the tribe?"
    "Not quite how you'd put it, but you still give Vurro a nod. It seems Wuldon's nonverbality is starting to rub off on you."
    if wuldon_like > 4:
        "Not the only thing of Wuldon's you want rubbing off on you-"
        with vpunch
        "{i}THUMP{/i}. Vurro's hand smacks into the back of your head mercilessly."
        v "Do you want your answer, or do you want to daydream about that big lug over there."
        "In the corner of your vision, you think you see the distant werewolf's ear twitch. You can't be sure, as he makes no other sign of having heard."
        e "Ow, ow. I want my answer. Please don't hit me like that again."
        "Vurro's eyes soften."
        v "Sorry, your skull isn't as thick as I thought it was. I'm used to Wuldon."
        v "We can talk about your daydreams later, anyways."
        e "I... don't know if we should, but please, carry on."
        v "Alright."
    v "We started out when we were very young. Wuldon was never a particularly sociable werewolf, always going off on his own, listening to the peace and quiet of the forest..."
    v "You can imagine, he was not particularly popular with most of the other werewolves."
    v "Still, one day I decided to follow him into the less visited parts of the woods."
    scene dark_forest with dissolve

    show vurro clothed at c1 with dissolve
    "Vurro smiles, remembering the halcyon days of youth."
    v "It was pretty boring, I remember. The little blue werewolf walked slowly, drinking in the atmosphere."
    v "After hours of seemingly aimless wandering, he brought me over to a creek, grabbing a stick with string and calling up to me."
    v "That was how we first became friends. Fishing together by the creek."
    v "Eventually I became bored of that spot, and asked him if he wanted to find another, which led us to a clearing of beautiful flowers..."
    v "Each month, we'd find something new, and enjoy it to our heart's content."
    e "Did you have a favorite?"
    "Vurro gives you a surprised look."
    v "Well, yes! I loved caves the most. They were like little worlds, each one different in its atmosphere, smells, and inhabitants."
    e "What about Wuldon?"
    "This time, Vurro gives you a cheeky grin."
    v "The creek, clearly."
    v "He spent most of his time without me fishing. How else do you think he'd get a gut like that?"
    if wuldon_like > 4:
        "Vurro lowers his voice conspiratorially."
        v "If you ever want the perfect evening with him, go fishing and bring the fish back to his house to cook."
        "You raise an eyebrow at him."
        e "Any reason you're giving me this advice?"
        "Vurro shrugs."
        v "I want the best for my friend. I think he's happier with you around."
        v "...especially since I won't be around."
        "You both grow solemn, briefly, before Vurro breaks the mood by shoving you teasingly."
        v "Though I think your relationship with him is going to be a bit different than ours was."
        "The wink Vurro gives you is enough to turn you cherry red. It's time to change the subject."
    "You clear your throat slightly to clear away that last awkward statement."
    e "Still, you continued it even into adulthood?"
    v "Well, yes, but for different reasons."
    v "As children, we explored to find things for ourselves. Later, we searched for ways to make our tribe greater without the need for stealing or conquest."
    e "And your brother? What would he do?"
    "Vurro gives you a shrug."
    v "Hunt and train, mostly. There's a reason he's stronger than me, you know."
    e "And you never tried to catch up?"
    v "Why bother? I thought that he'd leave me alone as long as I left him alone. By the time I learned better, it was too late."
    e "I can't blame you. Being paranoid is unpleasant. I'd rather die having lived a happy life, than live afraid of the beast in the dark."
    e "Maybe that's why I'm here though. Can't say I regret meeting everyone all that much."
    v "Would you go back if you could?"
    e "Depends. Would I be able to visit everyone here afterwards?"
    "Vurro takes a few seconds to think."
    v "No. That would be too easy. Life rarely works to our benefit."
    "You sigh. It's a melancholy sort of question you've been asked."
    e "I... I don't know right now."
    e "Maybe I'll be able to decide someday... maybe I'll have to decide."
    e "I don't like thinking about it. Everyone here is important, but so are some of the folks back home, even if I can't remember them that clearly."
    v "Well, as long as it's your decision, I'm sure you'll make the right one in the end."
    "You nod."
    e "It'll all be easier once I know how my friend is doing. Until then, there's not really much point in making up my mind."
    "Looking to your right, you see Vurro staring wistfully up at the sky, beams of light filtering down through the leaves of the canopy."
    v "It's a bit like how I feel about dying."
    "That sentence hits you like a punch to the gut."
    e "H-how so?"
    "Vurro shakes his head, snapping himself back to reality to look over to you."
    v "Sorry, I shouldn't have said that. To answer your question, though... I don't really mind dying."
    v "It's the people I'll leave behind that I'm worried about."
    v "I want to do all of this before I die so that I can know for sure that Wuldon and the tribe will be fine."
    v "It's alright for things to be rough for them for a while, but what I need to know is that they'll survive, and someday prosper."
    "The two of you mull over what's been said, walking together, hearing only the sound of leaves crunched underfoot."
    "Wuldon has gone far ahead of the two of you, in an effort to give you true privacy."
    "It's good to see he trusts you enough to leave you alone with Vurro."
    v "...For that reason, I'd like to ask if you could make sur-"
    w "We're at the entrance you were worried about, Little One."
    "Unfortunately, Wuldon's attempts to give you privacy also meant that he didn't know when not to interrupt."
    "Vurro sighs, looking over to you helplessly."
    v "I'll talk to you about it later. Maybe when we go over your daydreams."
    "He says that last part with a wink, as if it did anything to hide the melancholy still dancing behind his eyes."
    v "Let's get over there before he gets worried."
    "Vurro starts running, leaving you no recourse but to chase after."
    pause 2
    "You find the two of them by a small lake, talking amiably as you arrive panting. There's a familiar looking mountain behind them."
    scene cavernside_lake with dissolve
    show wuldon normal at l1 with dissolve
    show vurro clothed at r1 with dissolve
    e "Why did you go so far ahead of us? That was almost seven minutes of running!"
    "Wuldon is unphased by your whining."
    w "You two were being annoyingly loud. I just wanted some peace and quiet while I walked."
    show vurro clothed at c1 with move
    with vpunch
    "Vurro jabs Wuldon in the side with his elbow."
    v "I think I remember a certain someone saying they missed talking to me in their journal."

    "Wuldon grimaces, giving the two of you an exasperated look."
    w "I missed what you'd say. I didn't miss how you'd scare away everything within five miles every time you opened your mouth."
    "Vurro laughs at Wuldon."
    v "Yes, yes. Whatever you say, alpha."
    pause 1
    show wuldon normal with vpunch
    show wuldon normal:
        linear 0.3 xalign -0.2
        linear 0.1 xalign 0.05
    show vurro clothed:
        pause 0.5
        easein 0.5 xalign 1.2 ypos 2.0
    "Wuldon picks up Vurro, and tosses him into the lake unceremoniously."
    pause 1
    show wuldon normal at c1 with move
    w "Well, your alpha says get your ass in the cave."
    "You're almost certain Vurro didn't hear him."
    "It's also worrying that Vurro hasn't come up from underwater."
    "The two of you wait by the water's edge for two minutes. Wuldon is completely calm, as if his friend {i}weren't{/i} drowning right now."
    "While you trusted in his calm expression for a while, the extreme length of time Vurro had spent underwater was beginning to make you antsy."
    e "Should we not go in after him?"
    "Wuldon looks at you, slightly bemused."
    w "Well, if you want to help him scout the cave, be my guest."
    e "The cave? But-"
    e "I understand you're implying there's a tunnel into the cave through here, but I explored most of the cave, and found it to be almost completely dry!"
    "Wuldon nods."
    w "Yes. We never excavated the part of the cave this connects to. It's a good thing we didn't, or else we'd be facing an even larger collapse in all likelihood."
    "You shake your head, simultaneously impressed and frustrated by how easily Wuldon shrugs off the danger in this."
    e "I'll trust the two of you on this one. If I start getting short of breath... I'll come back here."
    e "I don't want to run out of breath."
    "The blue werewolf looks faintly bemused, if also approving."
    w "Making an air vent is part of why we're here. I'm glad you thought of it before diving in though."
    w "Speaking of..."
    if wuldon_like <= 4:
        w "You should be getting in there right about now."
        "He gestures towards the water."
        e "Why don't you go in first?"
        w "I want to make sure nobody follows us in, or anything like that."
        e "..."
        e "Alright. Good luck!"
        "Wuldon dips his head in acknowledgement, turning away to look at the treeline."
        "Getting the message, you dive into the refreshing waters of the lake."
        "Looking down, you spot a dark cave a few feet beneath you."
        "You swim towards it, passing through and into a long tunnel. At its end, you see a faint glimmer of light above you. Deciding you've reached the spot, you swim up, and into the cave."
    else:
        "Wuldon picks you up, holding you in his arms in a princess carry."
        "He holds you close for a moment, a wide grin on his face."
        e "I could get used to th-"
        pause 1
        show wuldon normal:
            easein 0.3 ypos 1.2
            easeout 0.5 ypos 1.5 zoom 1.5
        "In the blink of an eye, you find yourself above the treeline, looking down at a laughing werewolf."
        w "Good luck down there! I'll be with you in just a second!"
        "You plummet down into the cool waters of the lake, flailing around briefly in confusion."
        scene lakewater with dissolve2
        "While you could go back up and scold Wuldon, it's probably just better to look for the entrance."
        "He said he'd be with you soon, so it'll be fine regardless. The big guy seemed to be looking for something in the treeline, based off of the last glimpse you caught before you hit the water."
        "Shaking your head, you look down and spot a dark cave a few feet down."
        "You head down and in, passing into a long tunnel. At its end, you see a faint glimmer of light above you. Deciding you've reached the spot, you swim up, and into the cave."
    jump Chelforte_Cavern_Enter

label Wuldon_Check_Vurro:
    "Coming back to Wuldon's house, you see the werewolf on his doorstep."
    show wuldon normal with dissolve
    if wuldon_like <= 4:
        "He's shaking his head at you, telling you that it's not time yet."
        "That, or he's making fun of you for being too loud again."
        "It's probably both."
        "Getting the message, you head back."
    else:
        "He's smiling at you. It seems he's quite happy to see you."
        w "Not yet, little one - Vurro still needs some more time."
        "You nod."
        e "I understand. I'll see you soon!"
        "Wuldon is once again pleased by this."
        w "I look forward to it. Stay safe."
        e "You too!"
        "All you get in response is a self-confident smirk. Fair enough."
        "Once again, he watches you until you disappear from sight."
    jump main_slumbrous_well

label Wuldon_Cure_Vurro:
    "Wuldon guides you into the house, bringing you to a tiny drawer, which he grabs a mortar and pestle from."
    scene wuldonshack with dissolve
    show wuldon normal with dissolve
    "Ever so gently, he hands it over to you."
    w "I could make the mixture myself, but... I feel it'd only be right if you did, seeing as you got all of the ingredients."
    e "But... okay. I'll make sure it comes out okay."
    "You grab the tools and bring them outside."
    "Once you're there, you lay everything you'll need out on the grass - the two gels, the crystal, and the root."
    w "Here, we'll need this to hold and mix tincture."
    "Wuldon hands you a tall jar with a long wooden spoon in it."
    "Nodding, you grab it from him, before popping open the vial of teratoid mucus and pouring it in."
    scene black with dissolve
    "You follow that up by opening the jar of flagitous ooze, which... refuses to follow gravity."
    "Thinking quickly, you grab the grancrystal, and use it to scrape all of the flagitous ooze down and into the jar."
    "It's a long process - the flagitous ooze takes a bit to cling to the crystal, acting a bit like a drowsy slime, requiring the same time to cling to the jar from the spoon."
    "Finished with that, you hand the mixture of the slime components to Wuldon, who begins to stir the whole thing vigorously."
    "The once separate gels begin to meld together into a substance like water, but even clingier."
    "While he does that, you take the hexroot out of your bag, and place it in the mortar along with the grancrystal."
    "Picking up the pestle, you crush them together, into the mortar. There is a sickening crunch and juicy snap, both materials giving way to your blow."
    "Over and over again you repeat this process, slowly but surely grinding them down into a paste."
    "The hexroot's juice is immediately absorbed into the crystal's shards, turning both materials a light purple."
    "The final product looks a bit like a nebula - a purple haze surrounding the mixture, with little glinting pieces here and there signaling the pieces of crystal."
    "Holding up the mortar once you're done, Wuldon takes it, and begins scraping it into the gel."
    scene wuldonshack with dissolve
    show wuldon normal with dissolve
    w "I'll let you do the honors."
    "He proffers the spoon to you."
    e "Thank you."
    "You take the spoon, put it into the jar in his hands, and begin to mix it all together such that there is no precipitate to speak of."
    "The end result is a purple gel, gently glowing and glittering, generating a purple mist that soon fills up the entire jar."
    e "Well, it definitely looks magical."
    "Wuldon smirks a little."
    w "Not the first thing I would have said, but yes, it certainly does."
    "You blush, embarrassed at his teasing."
    e "What's the first thing you would have said then?"
    "He shrugs."
    w "Good job, probably."
    "You narrow your eyes at the werewolf, only to receive a teasing smile."
    e "Well, at least you're in a good mood."
    w "Mhmm, and it's all thanks to a little dragon and his friends."
    "The praise was a bit heavy there - you clear your throat to ignore the mix of pride and embarrassment welling up within you."
    e "We should really get this to Vurro now."
    "Wuldon chuckles, fully knowing why you changed the subject."
    w "Yes, we should."
    "Remembering what he'll have to face now, his smile dies a little."
    w "Here, let me show you where he is."
    "You follow Wuldon over to the entrance to his cellar. You can hear a steady thumping sound of flesh on wood, the chain locking the entrance straining with every beat."
    scene black with dissolve
    e "He's making less noise than I thought - I couldn't even hear this out front."
    "Wuldon looks a bit conflicted."
    w "He's still a bit sedated, but he's mainly just been trying this for a long time now, and has tired himself out."
    w "Having you here will make giving him medicine much easier though. Stand back for a second."
    "Following his orders, you get back from the cellar's entrance, while Wuldon bends down to unlock it."
    "The moment the chain comes undone, the world erupts into action."
    "The feral - Vurro - erupts from the cellar, lunging straight for Wuldon's neck."
    "Expecting this, Wuldon brings his hand up to Vurro's throat, bends backwards so that Vurro would lunge straight over him, and brings his leg up on Vurro's belly."
    "Rolling backwards like this, Wuldon comes out on top of Vurro, having used his momentum to reverse their positions, The feral held down by the throat and belly."
    "Just as quickly, the feral reacts, trying to rip through Wuldon's arms with its claws. In response, Wuldon sits on Vurro's chest, letting go of his throat, using the newly freed up arm to pin his opponent's hands above their head."
    "Once properly positioned, all Vurro could do was snap his jaws at nothing, and kick his legs uselessly."
    w "Alright, can you pass me the chain?"
    "Confused, but somewhat awed, you go over and pick up the chain that previously barred the entrance."
    "Handing it over to Wuldon, you see his plan. By draping the chain over the feral's mouth, it would try to bite him, only to find itself unable to close its mouth."
    "Leaving it like this was a bit cruel, but it is also what would have allowed Wuldon to feed the feral on his own."
    w "Bring the jar here and pour the cure down his throat. I can hold him for a long time, but I'm pretty sure this hurts for him."
    "You hurriedly bring over the jar, tipping it over so that the solution first drips into his mouth, and then falls in a steady purple waterfall."
    "It only takes a few moments for everything to go down his throat, but somehow, not a single of medicine was wasted."
    w "And now we wait."
    e "Yeah..."
    e "How long do you think we'll have to wait?"
    "Wuldon makes an odd movement with his head, which you realize is his best attempt at a shrug, given his inability to do so at present."
    e "Ah. Well, anything I can do to help in the meantime?"
    w "Can you go into the house and get him some of the food I prepared him? Should be on the desk near where the mortar and pestle were."
    "You leave Wuldon and the struggling feral behind, making your way inside."
    scene wuldonshack with dissolve
    "The house is fairly orderly, though there are a few things that do not seem to be in the right spot."
    "Looking around for the little drawer Wuldon grabbed the tools from, you spot a little table with scraps of red meat mixed with strong-smelling root fiber."
    "This would be the food he mentioned, you think, considering you find the little drawer shortly after, slightly to the left and up of where the food was."
    "Satisfied that you found the right thing, you pick your way over. On your way there, you notice a small object being revealed, previously covered by the bowl of food."
    "It is a little book, worn and ragged - Brown from end to end, with thick pages of what appear to be vellum."
    "You could ignore it and do what Wuldon said, but... something about it looks so inviting."
    "You step right past the food, and towards the book, grabbing and opening it."
    "The smell of dried leather floods your nostrils as the pages reveal their contents to you."
    e "...a diary?"
    show wuldonjournal000 with dissolve
    "The contents towards the beginning are all about the changes to the dark forest, and the days after the mine collapse."
    "There appears to be a long time gap after that, where the author gave up on writing, only for it to be picked up later..."
    "At that point, the writing style changes from present tense to past tense, with the dates often being accompanied by little notes saying 'roughly' or 'I think'."
    "Most of these later entries are accompanied by little drawings of the things in question, well made, and with a careful for anatomy."
    "Moving forward through it, you eventually reach an entry with a drawing that looks a bit like you."
    show wuldonjournal001 with dissolve
    w "Here we get to the reason I'm writing these."
    w "This little guy has singlehandedly given me hope that you'll come back again."
    w "He's a bit silly and doesn't look particularly reliable, but he went and saved you from that cave."
    if wuldon_like > 4:
        show wuldonjournal003 with dissolve
        w "He passed right out after the cave collapsed - having both of you here at home made me very happy."
        w "It was really cute to see him all tuckered out."
    "It's a little weird how often you've been called small or cute recently - you were taller than average back home. Now the only person you're taller than is Jog."
    show wuldonjournal002 with dissolve
    "Turning the page, you see that the next set of entries detail Wuldon's attempts to help Vurro, as well as notes on his condition."
    show wuldonjournal004 with dissolve
    "You see a small drawing of yourself bent over, harvesting plants in the wheat fields."
    w "The little guy seems determined to help, no matter how much I tell him he doesn't have to."
    w "I really hope you can meet him. I think you'd really get along with him."
    "The next few entries detail your recent exploits."
    "There are only about 10 pages left in the book."
    show wuldonjournal005 with dissolve
    "The first half talk about the visit with Haskell - a little drawing of him looking pouty and wrinkly is appended to the entry, along with a little note saying 'smart dumbass'."
    "The text itself is fairly dreary. It outright tells Vurro that he will likely become Feral once more."
    show wuldonjournal006 with dissolve
    "You felt the journal was likely written for Vurro, but this page really confirmed it for you."
    w "I thought we'd be able to have you here with us for a while - and while that might still become a reality, deep down I know Haskell is right."
    w "We have no way of curing you. We can stop it for a bit, but you will die again someday soon. I know it's unfair, but it might be best to try and find how you'd like to spend your last few days."
    "The writing on these last few words is noticeably worse - as if Wuldon had been struggling to write them down."
    "The next entry is the last."
    show wuldonjournal000 with dissolve
    w "The little one and I will be hunting for the last of the materials soon."
    w "I don't know what I'll do after all of this. Up until now, I've just been doing things my way, and hoping to find a way to bring you back."
    w "With the end so close in sight, I've had some time to think about the future."
    w "I owe the people of Lusterfield; the little one most of all. I am going to repay them, even if I don't know exactly how, yet."
    w "Though I'm strong, I am one person alone. I could help people one by one like the little one, but that is not my role."
    w "I know what it is I should do, but I do not want to."
    w "If you ask it of me, Vurro, I shall do it. I leave it up to you, not out of laziness, but because I do not wish to force people into my narrative."
    w "It also does not help that it would require me to find a mate at some point."
    if wuldon_like > 1:
        w "As you know, that is a bit complicated for me - I fear I may have to break tradition, and in doing so, put others in peril for my selfishness."
    if wuldon_like > 4:
        w "I have one in mind, but... unless I find a way around the obvious, it is a choice that puts the future in danger."
    "The journal ends there."
    "Maybe you shouldn't have read it, but... there was something about how the book was placed that made it clear he wanted somebody to find it."
    "You'll apologize to him about reading the journal when this is all over - hopefully he'll find it in him to forgive you."
    scene wuldonshack with dissolve
    "Grabbing the food, you return to Wuldon."
    scene black with dissolve
    "He is still on top of the feral, but much more relaxed than before. It has stopped thrashing, twitching slightly instead."
    w "Good to see you again, little one. Can you go ahead and put the food down next to me? I think he'd choke if we tried to feed him now."
    "Looking down at Vurro's limp form, you can see why. He is out cold, his muscles, teeth, and claws shrinking little by little, as they return to a normal size."
    "It seems the curse made him stronger."
    e "It seems like he's getting better."
    "Wuldon nods."
    "You both sort of just... stand there for a bit."
    w "You should probably find a seat while we wait."
    e "But what if something happens?"
    "You get a small grin back from Wuldon."
    if wuldon_like <= 4:
        w "You can handle yourself."
    else:
        w "Then I'll protect you."
        "You blush a little."
    e "I guess..."
    w "Just relax a little. You've earned yourself at least a bit of a break."
    "Sitting down with your back against the cabin wall, you get a good look at the area in front of you."
    "The only thing you can hear is Vurro's labored breathing, and the constant, underlying gurgling of the nearby stream."
    "The wind caresses your cheek, bringing with it the smell of verdure. Everything is as it should be - not a single thing out of place."
    "You think you can understand why Wuldon likes it here. It's kind of... making you...... sleepy."
    pause 5
    "..."
    my "... -e!"
    "Mrgg... is this a dream?"
    w "Wake up, little one!"
    scene wuldonshack with dissolve
    pause 0.1
    scene black with dissolve
    pause 0.5
    scene wuldonshack with dissolve
    pause 0.3
    scene black with dissolve
    pause 1
    scene wuldonshack with dissolve
    pause 0.5
    "Light floods your world as your eyes slam open, Wuldon's yelling finally cracking through the haze of sleep."
    e "AAH, WHAT, ARE WE UNDER ATTACK?!"
    if wuldon_like <= 4:
        "Wuldon catches your flailing limbs, laughing."
    else:
        "Wuldon suddenly snatches you up in a big, fluffy hug, just as quickly letting go."
    w "No! Vurro is finally coming to!"
    "The big werewolf appears to be in an excellent mood, a genuine smile spreading from ear to ear."
    w "Come, come!"
    "He moves over to Vurro's side, beckoning you over."
    e "Alright, alright, give me a second."
    "Getting up takes you longer than you thought. It feels like you've been batted around by 80 of Lothar's dummies."
    "When you do walk over, you see that Vurro's eyes have fluttered open."
    "His lips are moving slightly as well, as if he's trying to say something - all that comes out is a faint groan, however."
    show wuldon normal with dissolve
    w "He's been like this for a little bit, but it's getting better."
    "Wuldon's foot is tapping nervously."
    w "Can you go and bring me the small brown book from inside my house? It's on the table, next to where the food was."
    "At any other time, you'd think he was fucking with you, and telling you he knew you read the journal, but right now he seems too distracted to play around."
    e "Alright. I'll be right back."
    "Once again heading inside, you make your way over to where you last left the book."
    "It's... on the floor. Not where you left it."
    "Maybe Wuldon did that? You'll ask him, just in case."
    e "Hey! Wuldon! Did you go in here and use the book while I was sleeping?"
    w "No! Why do you ask?"
    e "No reason! I'll explain later!"
    "Well, as much as yelling like that isn't really your style, it's starting to feel more and more warranted."
    "Creeping forwards, you crouch down, looking at the book."
    "It's opened up on its very last page, previously left blank."
    "On them are two eyes, staring straight at you. I know what you're doing, they seem to say."
    "When you blink, they're gone, and the book is back on the table."
    e "...what?"
    "That wasn't supposed to happen."
    "Scrambling for the book, you open it to the last page."
    "It's blank again."
    e "I... I know I'm not that tired. Something's going on here."
    "But there's no proof of that."
    "For now, you'll just have to bring the book over to Wuldon. You can hear some faint murmuring from over there already."
    "Hurrying outside, still a bit spooked from what just happened, you get to Wuldon's side."
    w "Look! Vurro is almost forming words!"
    "Listening closely, you can hear small murmurs from him."
    v "Wher- -wh- h-"
    "Still not really coherent though."
    e "I got the book for you though."
    "You pass it over to him."
    w "Thank you, little one."
    "His nose twitches, confused."
    w "Did you spill blood on this? It... reeks of the stuff."
    e "...no. I found it on the floor, not where I left it."
    "Wuldon looks over to you, deeply concerned."
    w "Any other signs of someone being there?"
    "You shake your head."
    e "No, when I went down to pick it up, I saw that someone had left it open to the final page, where a pair of eyes stared up at me. Immediately after, it was back on the table, and the eyes were gone."
    w "..."
    if wuldon_like <= 4:
        w "We're going to have to figure out what that means. For now, let's pay attention to Vurro, though."
        e "Yeah. He should be the number one priority right now."
    else:
        "Wuldon's throat rumbles as a deep growl rips through the clearing."
        w "If they dare lay a finger on you, they'll lose the whole fucking arm. I don't care if they're magic, or if they're hiding - I will leave nothing of them but the smell left on this book."
        "He means that. You can see it in his body. His teeth are bared, claws flexed to rip and tear... you've never seen Wuldon like this."
        v "Wul- w- -ing -n -lp."
        "Wuldon's head snaps down, and his body relaxes, remembering where he is."
        w "Sorry Vurro, we'll focus on you for now."
        e "We can worry about everything else later. Right now, let's just take care of Vurro"
    "You both wait patiently for Vurro's words to gain cohesion. It's not a long wait, but the worry from the book looms over the two of you like a stormcloud."
    v "W-wuldon?"
    show wuldon normal at l1 with move
    show vurro normal at r1 with dissolve
    "And just like that, the worry dissipates, a grin coming to both of your faces."
    w "Good morning Vurro. How are you feeling?"
    v "...confused."
    w "I take it you don't remember anything from after we were mining?"
    "Vurro shakes his head, no. Now that his body has returned to normal, you can tell that he's definitely the smaller of the two brothers."
    "Despite that, you can also see a sharp wit living behind those ears, where you couldn't with Uffe."
    v "I've had a very long dream - a dream of a dire wolf chasing me throughout the cave, and towards the end, the forest. Otherwise, nothing."
    w "..."
    "Wuldon clears his throat."
    w "Well, you've definitely been doing things out here in the waking world."
    w "I prepared this journal for you to catch you up on everything."
    "Wuldon holds out the journal to Vurro, who slowly reaches out and takes it."
    v "So... I've been gone for a while?"
    "You both nod."
    w "A lot has changed."
    "Vurro turns to look at you."
    v "And who is this one? Did we finally manage to convince the tribe to talk to the others?"
    "Ouch. He is {i}really{/i} going to hate reading that journal."
    w "No, we... we're even more isolated than before."
    if wuldon_like <= 4:
        w "This is my friend, [e]. He's been an incredible help when it comes to your recovery."
        w "All of this would likely have been impossible without him."
        w "I wanted you to meet him at least once, and for him to meet you as you are now."
    else:
        w "This is [e]. I don't know where we'd be without him."
        "A satisfied rumble comes out of his throat."
        w "Hopefully you'll be seeing a lot of him in the coming days. He's a wonderful person and friend."
        "A knowing smile crosses Vurro's lips."
        v "I see your tastes haven't changed."
        e "What?"
        v "Nothing."
        "Wuldon claps his hands together gently, getting your attention."
        w "Point is, he has been crucial to helping you get better, and I wanted you to meet him, and for him to be here."
    "Vurro props himself up better to face you directly, offering his hand to you."
    v "It is a pleasure to meet any friend of Wuldon's. He is and was my most trusted advisor and friend - any friend of his is a friend of mine."
    "You take his hand, shaking it."
    e "It is a pleasure to meet you as well, Vurro! I have heard much and more about you from Wuldon. To hear him say it, you were the greatest werewolf to ever live."
    "That ends the handshake, as Vurro promptly turns to glare at Wuldon."
    v "I see he hasn't gotten better, then."
    "Wuldon is looking back at him with a face that told Vurro what he thought of that statement."
    w "I'll get better when your brother does. Or when we develop an actual history."
    "Vurro shakes his head, disappointed."
    e "No, I think Wuldon is onto something. Other than him, you're pretty much the only werewolf I've seen have an actual conversation."
    "All that does is earn you a frustrated look."
    v "Fine, I'll take it. Even if our fellow werewolves are only like that due to a lack of proper leadership, I see your point."
    "Vurro taps his claws together, looking down at them."
    "In there he sees long dried blood - a reminder of the time that has passed."
    v "I don't mean to be rude, but... I just woke up from whatever this was."
    v "You seem like a wonderful person, and I'll want to talk to you later, if you'd be happy to."
    "He grimaces."
    v "But for now I'd like to read this journal, and have Wuldon help me fill in the gaps."
    "You nod. It's not hard to see how this could be overwhelming."
    e "Alright, I'll come back later. It really was a pleasure meeting you, Vurro."
    e "Best of luck."
    if wuldon_like <= 4:
        "Wuldon walks up to you, and puts a hand on your shoulder."
        w "I owe you much and more for this, little one. It would be nice if we talked again soon."
        "He tilts his head towards Vurro."
        w "Once he is properly caught up, of course."
        "You nod."
        e "Of course. I'll see you later, Wuldon."
        "Turning away from him, it is your turn to raise your hand in farewell to the werewolf."
    else:
        "As you begin to move away, to give the two space, Wuldon quickly closes the distance between the two of you."
        "As he gets to you, he wraps you up in a big hug, one hand pressed against your lower back, right against your hip, and the second on your neck."
        "You're smushed against his soft fur and chubby body, held protectively and dotingly."
        "It's a surprising move from Wuldon, but you can't say you mind."
        "After a few brief moments, Wuldon pulls away from you."
        w "Stay safe. Come back and talk to me when Vurro's done catching up, okay?"
        "You were already planning to, but..."
        e "How am I supposed to know when that'll happen?"
        "Wuldon grins wolfishly."
        w "You'll be stopping by regularly to see if he's still reading that journal. You'll know."
        "You blush a little."
        e "Fair enough."
        e "I'll see you two later then. Hopefully Vurro gets through reading everything okay."
        "Wuldon nods to you, smiling."
        w "I'll make sure he does. Now, get going, we'll see each other again soon."
        "He waits for you to turn around and go, watching over you until you finally disappear from sight."

    $ removeItem("Hexroot", inventory, 1)
    $ removeItem("Slime Grancrystal", inventory, 1)
    $ removeItem("Teratoid Mucus", inventory, 1)
    $ removeItem("Flagitious Ooze", inventory, 1)
    $ QuestFinish(quest27)
    jump main_slumbrous_well

label Wuldon_Meeting_Shop:
    "You find Wuldon in front of his house, sharpening his khopesh."
    "There is a look of deep concentration on his face, as he gently applies the whetstone to the blade, over and over."
    e "You ready to go?"
    "Wuldon looks up from his blade, before putting his whetstone to the side, sheathing his sword, and standing up."
    show wuldon normal with dissolve
    w "Mhmm. I've just been waiting for a certain little one to finish his own preparations."
    e "But I didn't even take that long!"
    "Wuldon shrugs."
    w "Maybe, but it's still fun to tease you."
    e "Am I just bullyable or something?"
    "He shakes his head."
    w "No, just cute."
    "You grumble a bit, but still follow Wuldon as he starts walking towards Lusterfield."
    "The way there is fairly quiet. The only notable thing to happen was that Wuldon asked you to take the lead once you got past the river."
    "Lusterfield was rather quiet at this time of day, something you were thankful for. You don't want to think about how a crowd of people would react to seeing Wuldon."
    scene lusterfield01 with dissolve
    show wuldon normal with dissolve
    w "Huh, this place is smaller than I thought?"
    e "I thought so too, but you have to keep in mind that this is only a small part of Lusterfield, even excluding the vast stretches of farmland you've seen."
    "Wuldon shakes his head."
    w "No, no. I mean that nobody's here."
    e "Oh. That's less typical. There's normally at least one person on this street."
    "You look over at the space Lothar usually lounges at."
    e "But they don't seem to be here today."
    w "Probably for the best."
    "You shiver, thinking about the fit Lothar would pitch at a werewolf being in town."
    e "Agreed."
    "So saying, you walk into the King's Pawn. Inside are Ole and Sebas, both of which look bored out of their mind, checking and rechecking their wares."
    scene kings_pawn with dissolve
    show wuldon normal at r1 with dissolve
    e "Good morning! It's good to see you two again."
    "Sebas' tail immediately starts swishing back and forth."
    show sebas normal at l1 with dissolve
    s "Roomie! It's good to see you too! How has the day been treating you? Seen anything cool?"
    "Before you can answer the gush of information Sebas has thrown your way, Ole cuts in."
    show ole normal:
        xalign -0.35 yalign 0.5
    with dissolve
    o "You see us every morning, but it's good to see you, yes. You don't have to tell us about your day. I wouldn't mind if you did, but Sebas just wants a distraction."
    s "Yeah, because it's booooooring. If you don't tell me anything cool I might just fall asleep at the desk!"
    "Ole rolls his eyes."
    "At that moment, you hear the quiet jingling of bells, signaling a new customer. It's Wuldon, of course. Both Ole and Sebas' eyes widen."
    s "H-hello, and welcome to the King's Pawn."
    "Wuldon chuckles, looking between them and you."
    w "You know, you were much less scared of me than these two, little one. Do I have blood on my face today or something?"
    "It's a terrible joke, and it makes you smile, but Sebas and Ole seem to be petrified in fear."
    e "I don't think it's a good idea to joke about that yet, Wuldon, they still don't get why you're here, and they think you're like the other werewolves."
    w "Fair enough. I can introduce myself if you think that'd be best?"
    "It seems that Wuldon is looking to you for help on this one. He isn't particularly used to talking to 'normal people'."
    e "It's fine, I'll introduce you three to each other."
    e "Alright, Ole, Seb, this is Wuldon. He's a friendly werewolf I met during my travels - he might look scary, but he means no harm, I promise."
    e "Wuldon, the green lizard to your left is Ole, and the yellow lion to your right is Sebas. They're both friends of mine, so try not to scare them too much, okay?"
    "Wuldon smiles at the two of them, a big smile full of confidence you're pretty sure he doesn't have."
    w "It's a pleasure to meet both of you."
    o "...it's a pleasure to meet you too?"
    o "[e], where did you meet him exactly? Is he your friend?"
    "The whole time you and Wuldon were talking, Seb's tail was thrashing, the lion clearly upset by something."
    s "Or maybe something more? You never tell us what you're doing out in the forest - maybe you've found a big werewolf lover and came here to say goodbye to civilization."
    "He's definitely saying it as a joke, but there's a tinge of something unpleasant in it. A bit more bite than you're used to hearing in Seb's voice."
    menu:
        "He's... just a Friend":
            $ sebas_wuldon = 1
            e "He's a friend. I've spent a good amount of time with him, but that's because he's been going through a lot recently, and I'm not one to leave a friend in need."
            o "Oh, is he having trouble with the other werewolves?"
            "You nod."
            e "Sort of. It's mainly that his friend got cursed... which is why we're here actually."
            e "Haskell told us that any cure for him would involve hexroot, and that it would be best to get that from you."
            $ sebas_like += 1
        "He's a friend who happens to be hot":
            $ sebas_wuldon = 2
            e "He's a friend. A very handsome friend, sure, but we've spent most of our time together trying to resolve an issue we've both encountered."
            "Ole rolls his eyes at the mild flirting, before returning to what actually interests him."
            o "An issue you've both encountered?"
            e "Yeah. A friend of his got cursed, and we need to buy some hexroot from you."
            $ wuldon_like += 3
            $ sebas_like -= 1
        "No, but...":
            $ sebas_wuldon = 3
            if wuldon_like < 2:
                "Your cheeks go a bit red, embarrassed at Seb's suggestion."
                e "He's someone I trust a great deal."
                e "He's strong, kind, and dependable... we've spent a lot of time together recently because of something he's been going through."
                "You didn't answer the question, and while Ole just chuckles, Seb and Wuldon take note of that."
                "Wuldon looks deeply amused, and perhaps a bit interested. Seb, on the other hand, has a very strained smile on his face, tail once again thrashing."
                w "Nah, even if he is sorta cute, we're just friends."
                o "Alright then, how did you and your 'friend' meet?"
                "Seb is struggling to contain himself, quietly fuming in the background."
                e "I was hired to do a certain job by the werewolves, and I met Wuldon on the way there. He told me not to do the job, because it would hurt his friend, which is..."
                e "Well, helping that friend of his is why we're here, actually. We need to buy some hexroot off of you, if possible."
            else:
                "Your face grows complicated."
                e "He's someone I trust a great deal."
                e "He's strong, kind, and dependable, and I want to make sure everything goes well for him and Vurro."
                "You didn't answer the question, and while Ole just chuckles, Seb and Wuldon take note of that."
                "Wuldon seems deeply satisfied, an oddly protective look plastered across his face."
                "Seb, on the other hand, looks just about ready to kick Wuldon out of the store."
                w "We're just friends for now."
                "Your blush deepens, turning your face near-scarlet."
                o "Alright then, how did you and your 'friend' meet?"
                "Seb is struggling to contain himself, quietly fuming in the background."
                e "Oh, umm..."
                e "We met because I had a job to do for the werewolves, and I found him along the way."
                e "One thing led to another, and now we're trying to cure a friend of his from a curse."
                "You hear a gruff grunt from behind you, and feel the warm weight of Wuldon's hand on your shoulder."
                w "We came here to buy some hexroot from you."
            $ wuldon_like += 4
            $ sebas_like -= 2
    $ addItem("Hexroot", inventory, 1)
    "Regardless of how they felt previously, Seb and Ole grow sympathetic to Wuldon's plight - both of them disgusted by the idea of a curse."
    o "Oh dear, a curse... I haven't heard of one of those in a long time."
    "Seb lets out a quiet hiss."
    s "And it would have been better not to hear it at all."
    s "What asshole needs to get a fist to the face for doing that to your friend."
    "Both you and Wuldon sigh."
    w "We don't know. There are a couple leads, but we'll try and figure it out after we cure him."
    o "Not a bad idea. Curses are bad business, but helping your friend comes first."
    o "Here, I have some hexroot in the back, let me go grab it for you - I'll just be a second."
    "With that, Ole runs to the back, soon coming back with a thick purple root with conical protrusions randomly interspersed. He hands it over to you almost immediately."
    o "Good luck - I hope your friend recovers alright."
    "Seb nods, getting up and walking over before giving you a big hug."
    s "If you find out who did it, kick their ass, roomie. I know you can do it."
    "This entire situation is overwhelming, but Wuldon appears to be completely shell-shocked."
    w "I... appreciate the well wishes for both [e] and I, but..."
    w "What about your payment? How much do you need?"
    "Ole waves his hand dismissively."
    o "This isn't something that should be paid for. Please just use it to help your friend as soon as possible."
    "Wuldon's ears go flat against his head in dismay."
    w "I can't just... not pay you, right?"
    s "He means it you oaf. Now stop wasting time and leave."
    "Sebas was not nearly as gentle as Ole was, but it is not nearly as spiteful as he seemed earlier."
    w "I'll find a way to pay you all back later. I cannot thank you enough for your help with Vurro."
    "Taking their words to heart, Wuldon gently nudges you towards the door."
    w "I know you said you wanted to come with me, so... I'm heading there now. If you'd like to come, do so now."
    w "Otherwise, please stay safe while I go get the rest of the materials."
    "You shake your head at Wuldon."
    e "No, I'm coming with you."
    "With that, Wuldon walks out of the door, making his way towards the dark forest."
    "You turn your head back to Sebas and Ole."
    e "Thank you so much for all of the help again. You're incredible people and housemates."
    s "Anytime, roomie! Just make sure to get your fluffy butt back here safe and sound!"
    o "Yes, what he said. Run if it ever looks too dangerous."
    e "I know Wuldon has my back."
    e "I need to go after him now though, he's getting away from me. Bye! See you again in a bit!"
    scene lusterfield01 with dissolve
    "Dashing out of the door, you run towards Wuldon's distant form, determined to make your way to slime country side by side."
    scene black with dissolve
    "After a while of walking, you notice that the trees are slowly changing, growing closer together to each other, and occasionally dripping unknown goo at your feet."
    "Wuldon keeps disappearing from your side, returning with a significantly slimier khopesh every time."
    "Your surroundings only grow stranger as you go forward, eventually leading to an area completely choked by trees."
    "Looking through a small hole in the trees, you see a clearing with a similar opening on the opposite side of you."
    "Giant slimes are roaming freely around the area - likely the ones you need to hunt for Vurro."
    w "Well, here we are."
    scene dark_forest with dissolve
    show wuldon normal with dissolve
    w "I'll be out here making sure none of the area's slimes try to come in after you."
    "He takes out his khopesh with a grim look on his face."
    w "I'd let you do this part, if it weren't for how sneaky they are, like -"
    "Wuldon slashes his Khopesh at an inconspicuous patch of grass, piercing through a translucent slime you hadn't realized was there."
    e "Yeah... I think I'm better suited for the clearing anyways. I'm not sure if you can fit through the gap."
    "You point at the hole between the trees."
    w "I'm pretty sure I could if I tried, but... it would be unpleasant."
    "Wuldon lets out a deep sigh."
    w "Wait, wait... I almost forgot to explain how these slimes behave."
    w "Slimes are stupid, and will only follow you when you get near."
    w "The small ones don't hurt very much, but they do tend to wear you down at least a little with how clingy they are."
    w "Bigger ones are more dangerous - they'll chase you down and attack you. The upside is that they're pretty slow."
    w "All slimes eventually give up when you get far enough from where they consider 'home', slipping off and returning to their original spot after a certain time."
    e "...and my goal is to beat all of them in the hopes of getting the right material, yeah?"
    "Wuldon shakes his head."
    w "No, the only one you really need to fight is that one, I imagine."
    "He points at what you thought was a goo-covered boulder."
    w "The bigger slimes should be what you're looking for - creatures that big tend to be where the best reagents come from."
    e "But there's only one of them."
    w "And there's more than one room."
    "Wuldon chuckles lightly."
    w "I'm sorry about all the work I'm throwing your way with this."
    w "Regardless, good luck, little one. I'm counting on you."
    "You give him a nod, and walk into the dungeon, his smile disappearing into an expression of worry."
    "In the distance behind you, you hear Wuldon whisper to himself, underestimating your sense of hearing."
    w "He'll be fine. If worse comes to worst, I'll just pull him out of there. Just focus on protecting him out here."
    $ viscid_streams.discovered = True
    $ quest27.qComp(__("Collect slimy materials from the Slime Country"))
    $ quest27.status = 3
    jump Dark_Forest_Map

label Wuldon_Vurro_Mine_Quest:
    $ asked_mine = True

    "You've been to Wuldon's house enough times that you've memorized the way there."
    "It's extremely relaxing to walk through this section of the woods. There are no werewolves to terrorize you here."
    "A cool breeze tickles your cheeks, the gentle rustling of the leaves lulling you into a feeling of deep cal-"
    with vpunch
    if wuldon_like > 4:
        "Right as you thought that, a large, heavy mass slams into the back of your head, throwing you to the ground. Right before your face makes impact however, you find your momentum halted by two fluffy arms."

        show wuldon normal with dissolve
        w "I thought I told you to look above you?"
        "Wuldon's rumbling voice comes from right behind you. His warm breath tickles your ear as you dangle just above the ground, held only by his embrace. He seems to be teasing you."
        e "I thought I was safe..."
        "Your protests only make Wuldon chuckle, a sensation you hear and feel with your whole body at this proximity."
        w "Nowhere is safe, little one. Why would my house be?"
        "As he says this, he lifts you a bit so you can properly get up on your feet, letting go of you when you find your balance."
        e "Because you're there."
        "Wuldon raises an eyebrow at you, trying to look skeptical. It fails to hide the content look on his face."
        w "Well, I'm glad you trust me that much. Can't promise I can keep you safe from everything, but..."
        "Wuldon's ear wiggles slightly. He seems... embarrassed? It's a bit hard to tell, as he turns around and starts heading home."
        w "I'll try."
        "He doesn't turn around, or make any particular motion when he says that, but you can't help but believe him."
        e "I know."
        "You walk after him, nearing the house in the distance once more. You can definitely tell that Wuldon is a lot happier now than when you first met him."
    else:
        "Suddenly, you feel a strong tug on your horns."
        show wuldon normal with dissolve
        w "Convenient little handlebars you got there, little one."
        "Wuldon drops down from above you, a faint grin on his face."
        w "You really do need to get better at looking out for danger at all times."
        "The big werewolf immediately starts walking towards his house."
        e "What if I don't want to spend all of my time on edge, and just relax every once in a while."
        "You hear Wuldon chuckle, a hollow thing void of mirth."
        w "If you want to die, be my guest."
        "You follow after Wuldon after a moment of thought."
        e "Do you really care so little?"
        "Wuldon doesn't turn around, but he shakes his head slightly."
        w "No, but it's your life. I'll try to help, as thanks for helping Vurro, but I won't live your life for you."
        "You keep walking a bit."
        e "I guess we'd both be miserable if you did."
        "You get no response other than a nod."
    "The two of you have gotten quite near the entrance at this point, and the closer you get, the louder the background noise you've been hearing for a while now."
    "It's something of a deep dull ringing, pausing briefly for irregular intervals."
    "You think about asking Wuldon about it, but he seems to be completely unaffected."
    "As the two of you reach the door, you find out where the sound is coming from."
    "As Wuldon opens the door, the ringing turns to a roar, as the sounds of Vurro snoring fill the forest."
    e "Did he always snore this loudly?!"
    "Wuldon taps his ear to signal that he can't hear you, and beckons for you to follow him inside."
    scene wuldonshack with dissolve
    "Going in, the two of you find a heap of fur and blankets on the bed, which you can only assume to be Vurro."
    "Just as you consider asking if you should leave, Wuldon walks up to the bed, and rips off all of the covers at once."
    with vpunch
    "Vurro, tucked away as he was within the comfortable confines of his blanket-den, falls onto the floor, rotating slightly from the sheer force of Wuldon's tug."
    "Vurro continues to sleep, his face now smushed against the floor."
    "Wuldon lets out an inaudible sigh of frustration, the only sound occupying the air being the loud snoring of the lithe brown werewolf."
    "He heads over to a small cabinet on the far wall, and grabs a small container off of it. The contents appear to be a grainy black paste of some form."
    "Wuldon moves the container next to Vurro's nose, and uncorks it."
    pause 1
    "A smell like burnt flesh mixed with rotten tomatoes and spoiled milk fills the air, hitting you like a punch to the gut."
    "Wuldon was clearly prepared, as he was visibly holding his breath, ready to pop the cork back in at any moment."
    "The person who took it the worst out of all of you, though, is Vurro."
    "The brown werewolf immediately begins coughing violently, eyes flashing open as his body moves to scramble away from the vile smell."
    w "Awake now?"
    "His voice is teasing, but also... sad?"
    show wuldon normal at r1 with move
    show vurro normal at l1 with dissolve

    v "Fuck, yes, I'm awake."
    v "Please, never do that again."
    "All he gets is a shrug, as Wuldon recorks the bottle, and begins moving it back to its shelf."
    w "It worked. It's getting harder and harder to wake you up, you know."
    "At that, all of the energy in Vurro's body dissipates into defeated acceptance."
    v "I know."
    "No one speaks. All you can hear are the clinks of containers being moved around."
    "Silence is normal with Wuldon, but right now it hangs over the three of you, draping you in a smog that threatens to suffocate you."
    "You try to stomach it for a little while, but break under the pressure."
    e "Okay, what are the two of you talking about? Please be a little less cryptic."
    "Both Vurro and Wuldon sigh, breaking the uncomfortable silence."
    v "I've been sleeping longer and longer, deeper and deeper as time goes on."
    v "We're both pretty sure it means the curse is coming back. We don't have definitive proof, but it's a feeling. Doesn't help that my claws have started growing out again."
    "Just as he says, his body is starting to change ever so slightly - his teeth larger, claws sharper, eyes just a bit more animalistic."
    w "It's also that we know it's going to come back. Haskell said as much."
    "Wuldon's voice is clipped and terse, frustration written across his face when you turn to look."
    "A short silence falls again, far less intense than the last."
    e "I take it you finished reading the journal?"
    v "Yes. It was nice to catch up on everything that's happened."
    v "It's definitely made me reach a few decisions I wouldn't have otherwise."
    "Unlike Wuldon, Vurro seems to have accepted his death, fists clenched and eyebrows furrowed in grim determination. His eyes pierce through you, the kindly werewolf from before, seemingly gone."
    v "I'll be needing your help for a lot of this."
    v "You'll come with Wuldon and I, and help him put me down if I turn. I don't want him to have to deal with that alone."
    "You gulp nervously, giving the werewolf a small nod."
    e "I'd rather it not come to that, but I'll help if it does."
    "Vurro's face breaks out into a sunny smile."
    v "Wonderful! I also just wanted to have you along. A friend of Wuldon's is a friend of mine after all!"
    "You turn to look at the bigger werewolf. He has one hand against his head, rubbing his forehead slightly, as if nursing a headache."
    pause 1
    w "You could have just told him that from the beginning."
    v "Yes, but then it'd be less fun!"
    "Vurro's face sobers up a little again."
    v "Well, that, and I wanted to be sure you were ready for the possibility that you'd have to kill me out there."
    "It's uncomfortable, but you have been aware this entire time that Vurro could change at any moment, and the two of you would have to put him down on the spot."
    e "Is there anything you need me for in particular?"
    pause 1
    v "Well, one thing is that I want to finish exploring the caves I turned feral in."
    v "My nose has gotten better since I turned, and from what I can tell, a new area should have opened up with the front of the cave collapsing."
    v "If the scent is to be trusted, the new area should be extremely rich in metals. That should hopefully open up our future in trading once more."
    e "Well, first Uffe has to let that happen. I don't think he's going to roll over and let you do what you want."
    "Vurro pauses briefly, scanning your face for a moment."
    v "Well, that brings me to my next point. It's okay if you refuse to go with me to the caves. The caves don't need to be reopened now, and Wuldon will know about them after my death."
    v "What I do need you to do for me, is help me kill my brother."
    "That does solve the issue of Uffe refusing to let the werewolves become mercantile. Still, you didn't really think he'd be asking you to kill the man out of the blue like this."
    pause 1
    e "O-oh. Any reason you need me for that in particular?"
    "Vurro shrugs."
    v "Three versus an entire tribe is bad odds for us, but two versus an entire tribe is substantially worse."
    v "Plus, I have some plans for doing it that involve you."
    "Uffe is pretty awful, but does he really deserve to die? Your potential role in making it come to pass feels... guilty."
    e "Why would I help you kill him though? I understand removing him from power, but killing him?"
    "Vurro gives you an approving nod, seemingly happy with your reticence to kill."
    v "Look what happened the last time I let him live. He'll keep climbing his way to the top no matter what, no matter what he has to break."
    v "I'm pretty confident he's been looking for a good opportunity to make you disappear without drawing attention to his pack for a while now."
    "A shiver crawls down your spine."
    e "Still... that's your own brother, no?"
    "Vurro winces at the accusation."
    v "Yes. We share blood, and I did love him at one point."
    v "He threw all of that away the day our father died. He tried to kill me not thirty minutes after finding out."
    "You feel pretty uncomfortable after hearing that. It seems everyone else is in a similar mood, Vurro not looking you in the eyes, and Wuldon turned around, organizing medicine jars."
    menu:
        "Help Vurro":
            $ wuldon_like += 1
            $ QuestBegin(quest28)
            $ quest28.qProgress(__("Return to the cave with Wuldon and Vurro"))
            e "Well... I trust that killing Uffe is not a decision you would reach easily."
            e "I'll help you with both of the things you've mentioned... better to do them while you're still around to see it."
            "Vurro gives you a grateful smile."
            v "Thank you, [e]. I appreciate it more than you could know."
            v "Wuldon might not be saying much, but I'm sure he appreciates your help greatly as well."
            "Looking over at Wuldon, you see that he still isn't looking your way."
            if wuldon_like > 4:
                "Further down his back, however, you see his tail wagging slightly."
                "It seems the big guy is really happy to have you along."
                "You turn back to Vurro, who's looking at you with a knowing smile."
            else:
                "It seems he can somehow tell you're looking at him anyways, though, as he immediately begins speaking."
                w "Yes, I do. You are someone I always seem to be able to rely on."
                "There's a small pause."
                w "I will find a way to pay it back."
                "You turn your head to look at Vurro again, who's rolling his eyes."
                v "Not every relationship is transactional. People can do things for you expecting nothing in return."
                "He gets no response. Shaking his head, Vurro stage-whispers to you."
                v "This is why he's alone all the time, he sucks at letting people know that he's happy to help regardless of if you help him."
                "Thwap."
                "A carrot bounces off of Vurro's skull, falling in between the two of you."
                w "Oops. My hand slipped."
                "Vurro picks up the carrot and throws it at Wuldon, who still hasn't turned around."
                "Just as he does this, Wuldon bends down to grab a jar from a lower cabinet, the carrot sailing over him, where his head just was."
                "Vurro turns back to you."
            v "As I was saying, thank you for offering to help."
            v "We'll be heading out soon with some buckets, pickaxes, and food."
            v "If you have anything you need to go do, please hurry and do so. We will depart once you get back."
            w "Assuming we aren't asleep."
            "Vurro winces."
            v "Please don't use the jar again."
            "All he gets is a snort from Wuldon."
            "Vurro looks at Wuldon a moment longer, concern creasing his features. After he sees that Wuldon isn't joking, he turns to you."
            v "Well, you heard the man. Please hurry."
        "Do not help Vurro":

            $ wuldon_like -= 2
            e "I don't really know if I have the time to help with either of those things..."
            "As you say this, Wuldon's ear twitches violently. The big wolf turns towards you, face schooled into neutrality."
            "Despite his best efforts, however, you can see the disappointment in his eyes."
            w "I understand if you can't, but it would be nice to have you there with us."
            menu:
                msg "Continuing with this decision will likely decrease Wuldon's affection for you drastically. Do you still wish to reject Vurro's petition for help?"
                "Reject Vurro":
                    $ quest28.status = 69
                    e "I really can't help you, sorry."
                    "Vurro's face wears a small frown now, rather than the smile of before."
                    v "Unfortunate."
                    v "I completely understand. We will not hold it against you."
                    v "I will, however, ask you to reconsider your refusal to kill Uffe. If you don't help us kill him, or kill him on your own, he'll kill you someday soon."
                    e "...how can you be so sure?"
                    v "Let's just say I know my brother."
                    w "And also that I've heard him boast about how he'll gut you to his lieutenants."
                    "That's... well, it's not entirely unexpected, but it's certainly disturbing."
                    e "And why hasn't he done it yet?"
                    "Wuldon gives you a shrug."
                    w "Uffe likes fighting, but not war. He knows that if he kills you while the goats or village know you're in here, they'll come and attack him."
                    e "So he's waiting for the day I leave without telling anyone?"
                    "Wuldon gives you a nod."
                    w "That, and waiting for your scent trails near both locations to grow old enough that they can't trace you back to us."
                    v "Though he's not omniscient, my brother knows how to do things like this."
                    v "Using your scent to figure out how long it's been since you visited either place is good enough for him."
                    v "When that day comes, he will lunge for your throat, with no hesitation."
                    "If it's really you or him, it might be necessary to kill him after all."
                    e "Fine. You'll have my help when the time comes for you to kill Uffe."
                    e "I'm still not going to help you with the exploration. The last time I went into a cave, it almost killed me."
                    e "If there's nobody that needs saving in there, I think I'll pass."
                    "Vurro nods at that."
                    v "Fair enough."
                    v "Wuldon and I are probably going to try and scout out a little bit on our own, though not nearly as far as we'd go otherwise."
                    v "We need to plan for that though, so... please come back and talk to us about our plan for taking down Uffe in a few days, alright?"
                    "Wuldon waves at you with a gruff g'bye, quickly returning to his job organizing the jars."
                    "Taking your queue, you head out of Wuldon's house."
                "Reconsider":
                    $ QuestBegin(quest28)

                    "Sighing, you turn to face Vurro."
                    e "Well... I trust that killing Uffe is not a decision you would reach easily."
                    e "I'll help you with both of the things you've mentioned... better to do them while you're still around to see it."
                    "Vurro gives you a grateful smile. You catch a glimpse of a similar expression on Wuldon's face before he turns back around to continue working with the jars."
                    v "Thank you, [e]. I appreciate it more than you could know."
                    v "Wuldon might not be saying much, but I'm sure he appreciates your help greatly as well."
                    "Looking over at Wuldon, you see that he isn't looking your way at the moment."
                    "Further down his back, however, you see his tail wagging slightly."
                    "It seems the big guy is really happy to have you along, far more than he let on earlier."
                    "You turn back to Vurro, who's looking at you with a knowing smile."
                    v "As I was saying, thank you for offering to help."
                    v "We'll be heading out soon with some buckets, pickaxes, and food."
                    v "If you have anything you need to go do, please hurry and do so. We will depart once you get back."
                    w "Assuming we aren't asleep."
                    "Vurro winces."
                    v "Please don't use the jar again."
                    "All he gets is a snort from Wuldon."
                    "Vurro looks at Wuldon a moment longer, concern creasing his features. After he sees that Wuldon isn't joking, he turns to you."
                    v "Well, you heard the man. Please hurry."
    jump main_slumbrous_well




label Wuldon_Enter_Cure_Transition:
    "You finally make it out of the slime chambers."
    hide screen Dark_Forest_Mappy
    scene dark_forest with dissolve
    show wuldon normal with dissolve
    $ quest27.qComp(__("Report to Wuldon and Cure Vurro"))
    $ quest27.status = 4
    "Your body is covered in mildly acidic goo. You could kill for a bucket of water right about now."
    w "Nice job in there - hopefully you got everything you needed from there, because I don't know of any other spots where big ones swarm together like that."
    "You reach into your pocket and pull out 3 vials."
    "You have one filled with deep green goo, more viscous than molasses, which should be the teratoid mucus."
    "The second has a far more liquid ooze in it, bright green and hollow in the middle, the goo clung to the side of the glass, ignoring gravity from the moment you put it in there. Flagitous ooze, at a guess."
    "The last of the three vials is empty aside from a bright green crystal the size of your thumb. If this isn't the grancrystal, you may as well give up on guessing anything ever again."
    e "Yeah, I think this is everything."
    menu:
        w "Perfect. You ready to head back and cure Vurro?"
        "Yes{#wuldoncuringvurro}":
            e "Yeah, we should do that as soon as possible."
            w "Definitely. Let's just hope it works."
            "The two of you begin walking towards Wuldon's home."
            e "Thank you for standing guard by the way."
            w "No problem. It's the least I could do for all the help you've given us. Doesn't even begin to cover the debt I owe you."
            "..."
            "There's a small while of silence between the two of you."
            e "You know you don't owe me anything, yeah?"
            w "I disagree, but if you don't want to call it debt, then it barely contributes to how much I want to help you in return."
            "You get the feeling he's not going to back down on this issue."
            "Staying quiet, the two of you make your way home."
            scene black with dissolve
            scene wuldonshack with dissolve
            show wuldon normal with dissolve
            "Arriving at Wuldon's house, you hear a faint scrabbling sound."
            "It seems the two of you took a bit too long. That or the sedatives have stopped working as they should."
            w "Sounds like we need to make that cure as soon as we can."
            "You nod, agreeing wholeheartedly."
            e "Do you have a Mortar and Pestle anywhere?"
            w "Yes, come with me."
            $ wuldon_like += 2

            jump Wuldon_Cure_Vurro
        "No{#wuldoncuringvurro}":
            e "No, sorry, I'm not quite ready to do that yet."
            w "Alright, well, I'll keep Vurro pacified until you're ready."
            e "Why not just heal Vurro while I'm not there?"
            "Wuldon once again has a complicated expression on his face."
            w "You've done a lot to help him, and... we don't know how long the cure will last."
            w "I want you to at least meet him, and him meet you."
            "A short silence hangs between the two of you."
            w "It would be sad if neither of you got to know the other."
            e "..."
            w "..."
            e "Alright. I'll come over as soon as I can, okay?"
            "Wuldon gives you a nod."
            w "Take as much time as you need. We have the cure now, and I trust you to come back eventually."
            w "Good luck with whatever it is you're doing."
            e "Thank you, and good luck with Vurro."
            "You both nod at each other, and go your separate ways for now."
            jump Dark_Forest_Map

label Wuldon_Meeting_Field:
    "Searching through the fields for a while, you struggle to find him."
    "You'd think dark blue would be hard to hide in a sea of light brown, but apparently you'd be wrong."
    e "I should probably just go and ask Jog to help me find him, even if it makes things a bit harder."
    "Giving up for now, you turn around, only to find yourself face to face with a cream colored wall of fur."
    w "Boo."
    show wuldon normal with dissolve
    "The wall, now identifiable as Wuldon, rushes downwards as he bends down to put his face close to yours."
    w "Looking for something, little one?"
    e "Y-yeah! I was looking for you!"
    "Wuldon cracks a little smile."
    w "Ooh, should I be worried? Has the little hero come here to put down the big bad wolf?"
    "You roll your eyes."
    e "As if. We both know you're harmless."
    "Wuldon stands up straight and steps back a bit, grinning."
    w "Maybe, but the farmers don't know that."
    "He turns to his right, to an inconspicuous patch of farmland."
    w "AND NEITHER DOES THE HYENA WATCHING FROM OVER THERE. I'VE HAD ENOUGH VOYEURISM FROM YOU, SHOO."
    "You hear a faint rustling sound, before a small area of wheat shifts."
    pause 1
    with vpunch
    j "Aww, man, I thought I had you for sure this time."
    "You and Wuldon both look at Jog for a little while, until he gets the hint and leaves you alone."
    e "How do you keep doing that, anyways?"
    w "Mm. He forgets that the natural dyes he uses have scents."
    w "It's not exactly normal to smell a field's worth of crushed honeyberries."
    e "Oh. I hadn't realized your nose was that sensitive."
    e "None of the other werewolves have ever noticed him."
    "A touch of pride enters Wuldon's face."
    w "That's because none of those idiots have bothered to learn the scents of anything other than animals."
    "You lift an eyebrow in question."
    e "So all the other werewolves are pure carnivores?"
    "A nod."
    w "They only eat non-meats if they'll starve without them. Only my father, Vurro, and a couple others have really bothered to have diets with plants in them."
    e "Does that have anything to do with why you all are so different from the other werewolves?"
    "Wuldon gives you a shrug."
    w "No idea. All I know is that some werewolves are just... born different - often with unnatural strength, intelligence, charisma, and so on."
    w "Some people... hm. {i}people{/i} is a strong word."
    w "Uffe thinks it's werewolves that are meant to lead, 'natural alphas'."
    pause 0.5
    "Considering the other werewolves, Uffe might not be entirely wrong for once."
    e "I get what you're saying, but... the rest of the pack isn't particularly bright, no?"
    "Wuldon looks at you, as if considering whether to give you a legitimate answer or not."
    w "You're not wrong. It's something I've thought a lot about after seeing many of Vurro's loyal followers happily assimilate with Uffe."
    "He heaves a small sigh, and gives you a somewhat helpless smile."
    w "Still, I believe it should be based on merit or public support, not simply birthright."
    e "Oh. That'll probably have the same end result, no?"
    w "Yes, but it is fairer - better for the pack to be able to choose between the two brothers, rather than have it decided by a fight."
    e "Fair point."
    "Wuldon gives you a nod, content with that argument being sealed away."
    "He doesn't say anything else, looking at you, as if expecting you to do something."
    "An awkward silence falls between you."
    pause 1
    e "So, uhh. What are you gathering exactly?"
    w "Nothing, right now."
    "His face is completely deadpan. If he wasn't gathering, what was he doing?"
    e "Oh, I heard that you'd been cutting plants in the area, though not much beyond that. What are you doing in the area?"
    "Wuldon cracks a grin."
    w "I'm here to gather some plants that grow around the area, or at least, I would be if a cute little dragon weren't taking up all of my time."
    e "...okay. What plants are you {i}going{/i} to gather while you're here."
    "Wuldon begins laughing."
    w "Tsk, tsk, tsk, little one. First you call the average werewolf dull, and then you fail to ask the right question? Not making a very good impression, are you."
    "You smack your hand to your face."
    e "Fine. You don't know if you'll be able to gather them, I get it."
    e "Can we please just get to the part where you tell me the actual answer?"
    "Wuldon's uproarious laughter comes down to a lighthearted chuckle, waving his hand towards you in apology."
    w "Fine, fine, enough teasing. I'm here to collect medicine for Vurro, little one."
    e "...Aren't you in a bit of a hurry then?"
    "Wuldon lips form a weary smile."
    w "Yes, I suppose I am."
    "He sighs, turning away from you to bend down and look through the grass underfoot."
    "You stand there for a while, watching him sift through the grass... expecting him to do something special or something."
    "Instead, he just keeps checking plant by plant for something, occasionally moving slightly forwards to get to a new patch of turf."
    e "Is... is that it?"
    "Wuldon looks over his shoulder briefly, before turning his head back down to the plants."
    w "What do you mean?"
    e "Is this what the farmers have been so scared about?"
    w "Yeah."
    e "But you're just looking through grass."
    w "Yup."
    "Silence falls between you again."
    e "Mind if I help?"
    "Wuldon pauses, before turning to look at you with a bemused expression."
    w "And here I thought you'd prefer to stare at my ass all day instead."
    "You blush red."
    w "Please, feel free to. We're looking for milkweed, a plant with an orb of pink flowers on top, with a green stalk that lets out thick white liquid when you squeeze it."
    e "F-first of all, I wasn't staring at your ass."
    "You mutter the next bit to yourself, remembering your first meeting."
    e "not that I could pay your rates according to you."
    "Wuldon's ear twitches slightly."
    e "And second, are you pranking me about the thick white liquid? Because that sounds like the kind of joke you'd make."
    "You hear a snort from the stout werewolf in front of you."
    "You'd already been looking at it before, but now that he mentioned it, He really does have a nice ass."
    w "I'm not messing with you. Whatever you do, don't drink that fluid, or put it near your eyes - it's poisonous."
    w "And for the other point, I'm going to ignore the first bit, and just tell you that ogling me is free of charge for a while. Flash sale."
    e "O-okay. I'll get to helping, I guess."
    "Wuldon just makes a short grunting noise to signal his satisfaction with this."
    scene black with dissolve
    "..."
    pause 5
    "You and Wuldon carefully work side by side, checking for milkweed together."
    "Every once in a while one of you will find some and put it in one of the buckets Wuldon carries at his side."
    "After a long while, you hear Wuldon begin to hum happily to himself, a deep, rumbling noise, comforting in its warm timbre."
    "You continue your work together, picking through yards and yards of grass to Wuldon's tune."
    "Eventually, you work up the courage to talk to him again."
    scene summery_farmland with dissolve
    show wuldon normal with dissolve
    e "You know, I never really asked how you knew about the effects of Milkweed, or to come here to get it."
    "The humming cuts off, leaving only the sounds of the rustling wheat around you."
    w "My father taught me."
    "His body language shifts to show that he is paying attention to you, despite continuing his work at the exact same pace as before."
    "Being with Wuldon like this sort of gives you time to think before you speak... he seems to take life at a somewhat slower pace, doing things at a slow but steady rhythm."
    "Because of that, it takes a bit before you speak."
    e "Was he like you? Like..."
    "You point at his fur and size."
    w "Yes, though he was very much not a leader."
    "He sighs, thinking back to someone long gone."
    w "He was as close to a doctor as the tribe ever had."
    "Steady quiet falls once more, as you think on how to respond."
    e "Uffe doesn't really have a need for a doctor, does he. A need for you."
    "For the first time, Wuldon shifts uncomfortably, and his pace slows significantly."
    w "I know nothing compared to my father. But no, Uffe has no need for learned men like him, especially one with a tendency to talk to other groups."
    e "I take it that's where he found out about the milkweed?"
    pause 1
    "Wuldon's pace resumes as he nods."
    w "Yup. I only learned about the plants he told me stories about - regrettably little now that I have to treat Vurro."
    e "Yeah..."
    "And with that, silence falls once more."
    "The mood is less lighthearted than before, but you still have a sort of understanding between the two of you."
    "You continue to work until the sky begins to darken."
    w "Alright. I think that's enough for the day."
    "Wuldon declares this as he cuts the final piece of milkweed, both buckets halfway full with the plants."
    "Brushing the dirt on his hands off, he stands upright again."
    e "Are you sure that's going to be enough?"
    "Wuldon shakes his head."
    w "But I don't even know if this will work."
    w "I have an idea of the next thing to try after this, but after that, I'm not really sure."
    "He seems a bit dispirited. It makes sense when you consider that Vurro is still just as feral as when you left him, despite Wuldon's best efforts."
    e "You'll figure something out. And if not, I'll do my best to help anyway."
    w "Thank you, little one."
    "You both stand there for a bit."
    pause 1
    e "So, umm. What now?"
    "Wuldon looks at you somewhat oddly."
    w "Well, I go home and give this to Vurro, see if it works."
    w "Then, if it doesn't, I go to the river to collect some Boneset or Roundleaf Sundew."
    e "Oh. So, we should get going?"
    w "Yeah, probably."
    "..."
    "You both keep standing there."
    e "Why are we still standing here?"
    "Wuldon shrugs."
    w "I'm not in a huge rush, and I don't mind spending time in good company."
    w "Not much of that where I come from."
    "He's smiling, but it's a rather unhappily."
    e "Are... are you lonely, Wuldon?"
    w "No, little one. I'm not lonely."
    w "I am happiest when I am alone, in the quiet, but..."
    "He shrugs."
    if wuldon_like < 3:
        w "You saved Vurro for no reason other than mercy. I appreciate that, and don't want to just leave without letting you say what you need."
        w "Plus, as I said before, you're fairly good company."
    else:
        w "You saved Vurro just because a handsome stranger asked you to. Made me approve of you quite a bit."
        "He lets out a sigh."
        w "As I said, regrettably little of that in the tribe."
        w "While I prefer to be alone, I don't mind having you around. Feel free to stop by anytime, little one."
        "You don't know how he said all of that without a hint of embarrassment, but it's good to know you're on the werewolf's good side."
    e "That's... good to know. Thanks, Wuldon."
    w "Anytime."
    w "I now understand that you are waiting for me to end the conversation though."
    w "I'll see you next time, little one. Stay safe out there."
    "Wuldon turns around and walks off without another word."
    e "Good luck! I hope the medicine works!"
    "Wuldon gives you a thumbs up without turning around."
    $ QuestBegin(quest26)
    $ quest26.qProgress(__("Search for Wuldon... around the river?"))
    $ slime2_dp[1] = 4
    jump main_summery_farmland

label Wuldon_Meeting_River:
    "You decide to look for Wuldon over by the river, where he said he'd be if things didn't work out with Vurro."
    "While you could have checked his home first, he'd probably just not be there again, either gathering more milkweed, or looking for any of the river plants he mentioned."
    "You wander around for a while, eyes roaming fairly aimlessly around the area."
    "The fields were much harder for him to hide in, but this area shares many of his colors... he's probably just going to find you again anyway."
    "Actually, speaking of."
    e "Hey Wuldon, how's it going?"
    "Nothing. No sound."
    "Absolutely mortifying."
    "Blushing deeply, you start to move forwards, hoping nobody heard you."
    "Immediately, you hear a tiny whisper - so quiet it feels like you may have imagined it."
    w "Giving up so soon?"
    "You whip your head up, looking around rapidly."
    "You look behind you to see if he's there, like last time."
    "Just then, you hear a quiet thump from behind you, where you were just facing."
    w "You forgot to look up. Rookie mistake."
    show wuldon normal at c1:
        linear 0.1 zoom 1.1
        linear 0.05 zoom 1
    "You jump in surprise, the voice coming from right next to your ear."
    e "STOP DOING THAT!"
    "Actually stopping to look at Wuldon, he's got a bemused expression on his face, an eyebrow cocked in merciless mirth."
    w "Stop being so easy to surprise."
    "..."
    e "I'll work on it."
    "He lets out a small laugh at that."
    w "Please do, I don't want you getting killed out there because you didn't see something like the LITTLE HYENA STILL WATCHING US."
    "Neither of you even look in the direction of the crash from the trees this time."
    e "So... the milkweed didn't work?"
    "A brief flash of pain."
    w "No... not even a little bit."
    "You both stand there for a bit."
    e "Do you want help gathering again?"
    "Wuldon shakes his head."
    w "No, not this time... I'm close to being done, and I am in an actual hurry this time. Vurro is growing restless."
    e "Well, is there anything else I can help you with?"
    "Wuldon sighs."
    w "Yes. But before then, I want to see if this doesn't work."
    e "So then, if it doesn't work, you'll come find me? Or..."
    w "I'll be somewhere near this area - I can smell a ton of different medicinal herbs on the other edge of the river, which will be my last spot to check."
    "Hopefully that isn't what you think it is."
    e "Alright. Let's hope this works!"
    if wuldon_like < 2:
        "Wuldon lets out a sigh."
        w "Yeah... for Vurro, if nothing else."
        w "I'll be heading over to him now, unless you have anything else you need to talk to me about."
        e "No, I'm all good."
        "Wuldon gives you a nod."
        w "Alright, I'll see you later then."
        "Once more, Wuldon heads off, going deeper into the woods and towards his home."
        e "See you!"
    else:
        "Wuldon has a soft, weary smile on his face."
        w "Yeah. Let's."
        "He readjusts the carrying pole in preparation for the trip home."
        w "I know you'll come find me later. See you then, little one."
        "You blush a little bit, knowing he's most likely right."
        e "I'll see you then, Wuldon."
        "He heads off towards his home, a hand lifted in farewell."
    $ quest26.qComp(__("Look for Wuldon... somewhere near, with a lot of herbs?"))
    $ quest26.status = 3
    jump main_mossy_freshwater
label Wuldon_Meeting_Haskell:
    "Looking for Wuldon is a bit less certain this time - he didn't tell you exactly where he is."
    "Still, you're pretty sure he's here, by Haskell's house. Nowhere else matches his description from earlier."
    "You can't see Wuldon at the front of the house, so you decide to circle around and see if he's in the back."
    "This is the first time you get a good look of this place... it's definitely bigger than you expected, but it's well within the bounds of reason."
    "Knowing full well that you won't be able to find Wuldon, but that he'll find you, you start walking down the little road through the garden."
    "Unlike last time, you don't call his name, for fear that Haskell might wisen up to you being here."
    "After a bit of walking, you see a blue clump of flowers shift to your left. It soon reveals itself to be the crouched form of Wuldon, beckoning you towards him."
    "You creep over, mindful of Haskell."
    show wuldon normal with dissolve
    e "Heya Wuldon. I take it the medicine didn't work?"
    "Wuldon shakes his head."
    w "No such luck. He's calmed down a bit because some of the herbs were sedatives, but... it moves me no closer to the solution."
    e "Ah..."
    "He grimaces."
    w "I've still got this place, but I doubt any of this'll work. Even if it did, I don't feel particularly happy about having to steal from someone else."
    w "Unless you've got any tricks up your sleeve like you were suggesting, I think this is going for the long haul."
    "Sighing, Wuldon begins harvesting small cuts of Haskell's herbs - rosemary, myrtle, rhubarb, and more."
    e "I do have a couple ideas, but they all involve going to other people for help."
    w "What kinds of people..."
    "You think about Haskell and Ole."
    e "Good people. Well, one of them definitely is. The other is a bit selfish, but only for the oddest things."
    "Wuldon nods, before looking at you quizically at that last bit."
    w "Oddest things?"
    e "Tea. I'm pretty sure he would sell his soul if it meant getting good tea."
    w "Maybe let's start with the other guy first, then. I don't exactly have much tea to offer in return for help."
    "You nod, and gesture for him to get up."
    e "Alright, let's head over there then, yeah?"
    "Wuldon stays there for a bit, considering his options."
    w "Yeah, let's go. This wouldn't have worked, anyways."
    w "So, we're heading over to your village?"
    e "Yeah."
    "You both head up the small garden path, whispering to each other the whole way."
    e "So why didn't you spook me this time?"
    w "Wasn't in the mood for once."
    e "You sure it wasn't because I've figured out all your tricks?"
    "You get a flat look."
    w "Sounds like you want me to trick you by pulling you into a pit from underneath you next time."
    e "Underneath?!"
    "Wuldon leaps at you, clasping his rough, callused hand over your mouth, using the other one to wrap right under your waist, and push you against his body to lift you up."
    "His shoulderpole falls to the ground, buckets clanging loudly."
    "He begins running away at full tilt, heading towards Lusterfield."
    with vpunch
    h "HEY! GET BACK HERE!"
    "Wuldon keeps running."
    "You can see Haskell running towards you two with a bow in his hands from over Wuldon's shoulder. You can also see that he can't recognize you from his position, body mostly blocked by Wuldon's."
    show wuldon normal at l1 with move
    show haskell normal at r2
    show haskell normal at r1 with move
    h "THIS IS YOUR FINAL WARNING, STOP NOW, OR GET SHOT."
    "Wuldon, again, ignores him."
    "You see Haskell grab an arrow from the quiver around his back, and nock it."
    "You begin to try and squirm your way free."
    h "WHELP, DON'T SAY I DIDN'T WARN YOU."
    with vpunch
    "As soon as Haskell shoots the arrow, you feel one of Wuldon's ears twitch, as he leaps to the side into a running roll, dodging the arrow without breaking his stride."
    "Looking at it though, Haskell wasn't aiming to hit, just going for a warning shot."
    h "Hey, is that-"
    h "Put [e] down, you mangy werewolf!"
    "At that, Wuldon finally slows down, stopping to turn and look at Haskell, who is looking at the two of you with great indignance.."
    if wuldon_like < 1:
        "Wuldon is still holding you, ready to run away at any moment if Haskell proves to be violent. You'd probably be into it if it weren't for the fact that you sort of feel like a sack of potatoes."
        "The hand around your mouth has shifted to be near your back, for better grip, and to let you speak."
        w "I'm sorry for having to steal from you, I don't know who you are, but I cannot pay you back right now."
        w "This is an emergency situation, so let us go without a fight, and I'll figure out a way to repay you - [e] as my witness."
        "Going by his voice, he really does mean that, the apology ringing true in his throat."
        "Haskell is just sort of standing there, dumbfounded at this."
        "You whisper to him."
        e "Wuldon, this is the second guy. I think we should probably just talk to him about this."
        "In response, he puts you down on your feet, letting you join the conversation with much more agency."
    else:
        "Wuldon puts you down and places himself between you and Haskell."
        "You can see his legs and back tense, ready to protect you if the dragon makes any suspicious movement."
        "When he speaks, it is a terse growl."
        w "Who are you, and what do you want with [e]."
        "Haskell squints at Wuldon."
        h "I'm Haskell, and I could ask much the same of you."
        h "From my perspective I heard [e] shout, and looked outside to see what looked like a kidnapping."
        "He points a thumb back to the buckets half-full of herbs."
        h "A kidnapping of my business partner, done by a thief."
        "Wuldon looks back at you carefully, never fully taking his eyes off of Haskell."
        w "Is he a friend, little one?"
        "You were kind of surprised to hear Haskell call you that, but it's not exactly a problem."
        e "He's the second guy I told you about. The guy who loves tea."
        "You shrug slightly."
        e "We get along alright."
        "Wuldon relaxes greatly at your words, a relieved smile crossing his face before he turns back to face Haskell."
        w "Well, however much it's worth, sorry for scaring you like that."
        w "And sorry for stealing from you. I have a feeling we'll be telling you more about this, but. I promise it was an emergency, and that I'll figure out a way to pay you back somehow."
    h "I'm not going to say it's no problem, if that's what you're looking for."
    h "[e]. Explain what's going on here."
    "Wuldon looks slightly annoyed at how Haskell is treating you, but you're honestly pretty used to the dragon being a big whiny baby at this point."
    e "Well... I've been over with the werewolves recently, trying to figure out a couple things, and on the way I met Wuldon here."
    "You gesture at the fluffy werewolf."
    e "He's not a complete and utter asshole like the other werewolves - him and his friend, Vurro."
    "Haskell grunts."
    h "Withholding judgment on that for now. First thing I've seen him do is steal my herbs, after all."
    "Your eyebrow twitches."
    e "Yes. Regardless, said friend is..."
    "You look over at Wuldon, who gives you a small nod, telling you it's alright with him."
    e "Horrifically sick. He was transformed from a normal, trustworthy person, to a wild animal."
    h "So, he went from being an unusual werewolf to just like all the others."
    "Wuldon snorts, mildly amused."
    w "Yes, something like that."
    w "Vurro doesn't deserve to be someone like that though, and I've been trying to find a cure for a while now... nothing's worked."
    "Haskell scoffs."
    h "So your immediate solution was to steal from me."
    w "No, that was my third solution."
    h "And that makes it so much better."
    w "Yes, it does."
    "This entire exchange of mocking sarcasm has taken about 15 seconds to unfold - the conversation taking exactly as long to completely get out of your hands."
    h "Well, I'd like to hear what else you tried, Mr. 'Tried Two Other Things First.'"
    w "Alright, I'll tell you exactly what I tried. Maybe that way you'll have something actually useful to say."
    "Wuldon promptly explains what herbs he's tried, how he's prepared them, and their effects."
    w "Hopefully that was enough trying for you to be happy with, you overgrown lizard."
    "He gets a derisive snort in response."
    h "Yes, sure, that's satisfactory."
    h "If you want nothing to change, I mean."
    h "I knew more about medicine than you when I was 10."
    w "Perfect, because I learned all of that by the time I was 5."
    "You're just standing there dumbfounded as all of this happens."
    "Neither of them even seem to be angry at each other - the trading of barbs apparently deeply satisfying for both parties."
    h "Well, if you want to actually get anywhere, come inside and talk. All of the nice smells from my house are leaking out, and I have a feeling you're not going to leave me alone until you find a solution."
    "With that, Haskell turns around to go back to his house."
    "Wuldon nods."
    w "Sounds good. Not because I'll learn anything, but because I'll be getting free tea."
    "Haskell swivels {i}sharply{/i}"
    h "Who told you about the tea."
    "His eyes narrow."
    h "And who said it'd be free."
    "Wuldon jerks his thumb your way, throwing you under the wagon."
    h "Figures."
    "Haskell turns to face you."
    h "You're getting more tea for me in return for that."
    e "But I didn't even say you'd give him tea! Or that it'd be free!"
    "He shakes his head."
    h "Well, it's what he got out of what you said. Reason enough for you to get me more."
    "You look over to Wuldon, pleadingly. He shrugs."
    e "Okay, fine..."
    e "But only as long as you do your best to help Wuldon."
    "Haskell looks at you oddly."
    h "I was planning to, but what's it matter to you?"
    "You shrug."
    e "What's that matter to you?"
    "He snorts and rolls his eyes."
    h "Fair enough. Keep your secrets."
    "You nod, Haskell turning back around and leading you and Wuldon inside."
    scene black with dissolve
    "As soon as you get in, Haskell begins brewing more tea."
    scene haskellhut_night with dissolve
    show haskell normal at r1 with dissolve
    show wuldon normal at l1 with dissolve
    w "So, are we paying for that, or is that included in the pity."
    h "It's free for you. Your friend over there is going to need to pay if he wants any, though."
    "You narrow your eyes at him."
    e "Good thing I don't like tea."
    "This is a lie."
    "Haskell turns to Wuldon."
    h "And if he doesn't go get me more tea after this, he'll have to pay for your tea."
    "Now both you and Wuldon are looking at Haskell in disbelief at the sheer audacity of this man."
    w "If that's the case, then I think I'll pass on the 'free' tea."
    "Haskell shakes his head, a lazy smile on his face."
    h "If you don't drink the tea, I'm not going to help you with your friend Vurro. What kind of guest refuses their host's drink?"
    "Wuldon doesn't even have a barb in response to that."
    e "Okay, fine, I'll go get you your tea, just... please get on to the important bit."
    "Haskell tisks, fake shaming you."
    h "Ah, but tea {i}is{/i} important, [e]."
    "You sit down and put your head in your hands, nursing an oncoming headache."
    "The werewolf to your side shakes his head and begins getting up, only to be stopped by you putting a hand on his shoulder."
    e "Please, just... I'll be fine. I'm not mad at him or anything, just getting a headache."
    "He looks at you with some concern."
    e "I'm glad you want to stand up for me, but he's my burden to bear."
    "You're starting to regret rejecting the tea earlier. It would probably help a lot with the dull throb behind your eyes."
    "While you're thinking about this, however, Haskell has moved to the other side of the table, two mugs of tea now ready."
    "He passes one to Wuldon without asking, and begins sipping on his."
    "Wuldon stares at it with a mixture of amusement and frustration, split between the two feelings. After a second he decides to settle on amusement, chuckling as he grabs the mug."
    w "Fine. But you're helping me with Vurro."
    "Haskell raises an eyebrow at the werewolf."
    h "Yup. Just wanted to make sure I'd be getting a new shipment of goods from Ole's store. One can never have enough plants, alchemical ingredients, or tea."
    w "Have you ever considered going and getting them yourself?"
    "He gets a nod in return."
    h "Of course I've considered it. But why would I ever do it if I can just send this guy out to do it."
    "He points to you sitting at the table like an alcoholic nursing a hangover after a long night out."
    "Wuldon still looks a bit concerned, all things considered, but he respects your wishes and keeps quiet about it."
    w "I'm going to lay the situation with Vurro out before I get incapacitated like [e] over there. He looked less tired after escaping a collapsing cave than he does right now."
    "That earns him an amused snort from Haskell, though the dragon does appear to be listening attentively now."
    h "I'm glad my voice is that powerful. Now, go ahead and tell me all about it."
    "Wuldon takes him up on that, explaining Vurro's situation with excruciating detail."
    "He tacks on more details every time - more than he needs, you're sure."
    "At first you suspect he's just being careful, but by the end you realize he's messing with Haskell in his own way as well."
    "Once he's wrapped up, Haskell is looking at him with a faintly bemused expression."
    h "You just about done?"
    w "Mhmm. Just thought I'd be extra detailed so that your mind would have to do less of the work. Thought I'd save you the time, just like [e] does"
    "Haskell cracks a grin."
    h "Fair enough. I'm still not getting my own tea though."
    h "All of the extra details didn't help, but I do think I have a pretty good idea of what's happened with Vurro."
    "The grin fades into a somewhat more businesslike expression - something in between teasing and sober."
    h "This really doesn't sound like a sickness, or anything treated with the easy stuff."
    "He takes a sip of his tea, before turning his gaze on Wuldon."
    h "You sure you and Vurro aren't awful people? Because this is 10,000 percent a curse."
    h "You don't tend to get those by frolicking around holding hands with your friends, making daisychains."
    w "No, we're not terrible people. We aren't the ones that have been attacking people that come near the forest."
    "Haskell looks mildly skeptical, though it quickly transitions into amusement."
    h "Alright, not terrible - just annoying."
    "Wuldon sits with that for a moment."
    w "Then why haven't you been cursed yet?"
    "This time, Haskell was caught mid-sip. He somehow managed to look composed even while choking on tea and laughing."
    "After the worst of it passed, he looked up at you two with some merriment twinkling in his eyes."
    h "Because I know how annoying I am. I'm in the middle of nowhere, and don't spend my time putting my nose in other people's business, unlike some people."
    "He's mostly kidding, but there is a tiny inkling of truth somewhere, you think."
    "To your side, you can hear Wuldon muttering something about that being familiar."
    "The mood fairly light, the two of you wait for the last of Haskell's laughter to die away. Wuldon takes that as a good time to steer the conversation back to Vurro."
    w "So, curses are always done by other people, yeah?"
    "Haskell nods."
    h "Yup. Typically more than one, too."
    w "Any way to find out who did it?"
    "Haskell shakes his head."
    h "No. The best you can do is identify likely people. Magic is very difficult to trace without an expert in the field."
    "You hear a deep, frustrated growl from the werewolf to your right."
    h "That many people to choose from?"
    w "No, not really, only one real suspect. I'm pretty confident he couldn't cast curses even if he wanted to though."
    "There's a shrug from Haskell."
    h "Maybe they found someone from outside to fix their problem for them, like you're doing with me."
    "Wuldon rolls his eyes."
    w "You're probably right, but can you fix our problem like the other outsider did?"
    "Haskell shakes his head with a slight grimace."
    h "If you had ruffled a few less feathers, maybe."
    h "As it stands, I don't know. The curse can almost certainly be mitigated briefly, but a permanent solution is unlikely."
    "Wuldon's face is creased in frustration, worry, and anger. He lets it all out of his system with a deep breath."
    w "Well, thank you for being honest about it."
    "You all look at each other in silence, stewing over the fact that Vurro most likely can't be saved."
    e "Okay, well, how do we help him?"
    "Both sides are a bit surprised to hear you speak up. Thankfully, your headache is gone now, so you're good to talk to them."
    w "Yeah, what [e] said."
    h "..."
    "Haskell seems reluctant to share any information."
    h "It'll require a lot of rare materials, hidden in dangerous places. Don't think either of you two are suited for that kind of job."
    h "A messenger and loner wolf are what places like that have as victims."
    "Wuldon shrugs at that."
    w "Okay, that's not a problem for me."
    "You nod in agreement."
    e "Not my first time doing something like that."
    "Wuldon looks over to you with some consternation. Haskell on the other hand is looking at {i}both{/i} of you with resigned concern."
    h "Okay, well... first things first: You'll need to go into town and buy some hexroot from Ole and Sebas."
    h "While you're there, you'll buy me some Jasmine to make tea with."
    "You give him a look."
    e "I don't think I can carry a full shipment with me while I do this."
    "Haskell waves you down."
    h "No, no. The shipment comes later. The jasmine is to tide me over until then."
    e "...I'll do it. I don't know how much tea you drink in a day, but I'll try to bring enough to last you a good while."
    "Haskell gives you a genuine smile at that."
    h "Thank you. Unfortunately, the next step on your journey is far more unpleasant. You'll need to go into the more savage areas of the dark forest."
    w "'{i}More{/i}' being the imperative term there."
    "Wuldon and Haskell share a chuckle at that."
    h "Surprisingly wise words."
    h "Regardless, I specifically mean the depths of slime country."
    "You didn't know there was an area with lots of slime around here, but you can tell it's not particularly pleasant by how Wuldon's snout wrinkles in disgust."
    h "Therein you should be able to find Slime Grancrystals, Flagitous Ooze, and Teratoid Mucus."
    w "I assume all of those are from different kinds of slime?"
    "Haskell nods."
    w "And all of them are heavily acidic variants, aren't they."
    h "Yes. Though they all look pretty similar to each other, so good luck figuring out if you have the right one."
    "You narrow your eyes at Haskell."
    h "If you want to figure it out by comparing which one melts your hand faster, be my guest."
    h "I do know their goo behaves radically differently after death, so even if you don't know what kind of slime you're fighting, you'll know if they were different or not."
    "That's... unfortunate, honestly. It's frustrating to hear that you'll have to fight multiple different slimes just to have a chance at getting the right ingredients."
    h "Once you're done with that, take the ingredients home and mix the ooze and mucus into a catalytic jelly."
    h "It should help you catch whatever curse is in Vurro."
    h "The Hexroot is to draw out the curse and put it in the jelly, while the grancrystal is crushed and sprinkled over the mixture to speed up the process so that it doesn't take literal years."
    "Both you and Wuldon nod."
    w "Alright. However irritating and tea-obsessed you are, you've been a big help."
    "Despite what he says, there's a smile on his face. It seemed the blue bastard enjoyed the back and forth."
    w "Knowing all this though, I've got little time to waste. I'll be back at a later date - pay you back somehow."
    h "Alright. Good luck in hell."
    e "You better wish me luck too, because I'm going with him!"
    "Wuldon pins you with a gaze that says '{i}we're going to talk about this later{/i}' before turning back to Haskell."
    w "I don't know what made you this cynical, but I appreciate you ignoring it a bit."
    "Haskell waves his hand dismissively, drinking his tea."
    h "Not any one thing. The cynicism comes with age."
    w "You know, I'm not exactly young, right?"
    "Haskell snorts."
    h "Maybe not for most people, but you could be my grandson."
    h "Let me tell you, the world beats suspicion into you by 117, no matter who you are."
    "This honestly explains a lot about Haskell. Him being a crotchety old man in a middle-aged body recontextualizes some of your earlier conversations."
    "Wuldon lets out a hearty chuckle."
    w "I did not realize I was in the presence of someone so much my elder. My 43 pales in comparison to you in retrospect."
    w "Old men deserve their turn to be grumpy, my apologies for failing to treat you with the respect an elder like you deserves."
    "You mutter at that."
    e "...maybe if he earned it, he'd get it."
    "Haskell laughs at that this time."
    h "Yes, I rather think [e] is correct. Dragons age a bit differently, even if we experience time the same."
    h "Not to say your age as a werewolf excuses your poor manners from earlier. You're still going to have to make it up to me."
    w "Yes. As I've said, I'll be repaying you in the future, old man."
    "Haskell raises an eyebrow at that."
    h "I'm still in my prime, just like you two, if you couldn't tell from my body."
    "Wuldon snorts in amusement."
    h "Look, if you want to point out anybody here as the least handsome, it'd have to be [e]."
    w "I'm not so sure about that. The little one is quite cute to my eyes."
    "Haskell nods with a smile."
    h "Exactly, he's cute - he can't pull off the dashing adventurer nearly as well."
    "You think you're going to melt into a puddle out of sheer embarrassment."
    w "I don't disagree, though I think we should stop before our adorable little friend here explodes."
    h "Make sure he doesn't get knocked about too hard in there. I don't think his look would work with scars."
    w "And what about me, am I chopped liver?"
    h "Not yet, though if you're not careful out there, you might be."
    "Both Wuldon and Haskell are smiling. Meanwhile, you've got your head in your hands in a feeble attempt to try and hide your cherry red face, hoping they assume it's another headache."
    h "Regardless, dealing with curses is no joke, and it means there's a real threat running about in our area. It'd be appreciated if you could take care of that for me."
    w "That's the plan. I'm currently dealing with Uffe, but taking down whoever cursed Vurro is my next priority."
    "You get out of hiding briefly, feeling the need to say something."
    e "I also plan to take down whoever this guy is - especially because they might be related to why I'm here in the first place."
    h "I appreciate the confidence, but going by looks, I'm not feeling much more confident in him being brought to justice."
    w "You'd be surprised, the little guy packs a lot of power in that petite frame of his."
    "Haskell snorts."
    h "Well, good luck to you and the petite powerhouse."
    h "I'm pretty sure you know where Slime Country is, Wuldon, so if you don't mind, please leave me alone so I can enjoy my tea in peace."
    "Wuldon laughs."
    w "Sure, sure. Come on, little one, get out before he decides to make you get more stuff for him."
    "There's a little glimmer in Haskell's eyes as Wuldon says that."
    "You get out of the house as quickly as possible within the bounds of politeness, giving Haskell a brief farewell, soon joined by a chuckling Wuldon."
    scene alchemistscabin with dissolve
    show wuldon normal with dissolve
    w "You know, I kinda like that guy. Bit of an ass, sure, but funny."
    "You shiver."
    e "I get what you mean, but I think I'm going to avoid him for a bit, at least until I get his shipment."
    w "A wise decision. Speaking of that shipment though, let's head over to that shop of yours, yeah?"
    e "Alright. I might need some time to get things in order before then though, so I'll meet you at your house when I'm ready, alright?"
    "Wuldon gives you a nod."
    w "Fine by me. Also lets me sedate Vurro again, as well as prepare my own gear for the slimes."
    "You both head your separate ways as you reach the tree."
    $ QuestFinish(quest26)
    $ quest28.qProgress(__("Visit the Slime Country"))
    $ QuestBegin(quest27)
    jump main_alchemists_cabin

label Wuldon_After_Cavern_Talk:
    if vurro_lives:
        "As you approach Wuldon's house, you notice that the owner is not currently home."
        "However, you can hear a loud snoring sound coming from the cellar in the back of the house."
        "Looking in, you see the slumbering form of the feral werewolf."
        "..."
        "Honestly, he's pretty cute when he's not trying to kill everything in sight."
        "Things here seem relatively stable for the foreseeable future."
        "Wuldon told you he'd be back later. Maybe you should turn your attention somewhere else for now."
    else:
        "As you approach Wuldon's house, you can hear the sound of metal on metal."
        "Warily, you sneak forward, using the treeline as cover."
        "..."
        show wuldon normal with dissolve
        w "I know you're there."
        e "Ah, sorry."
        "You step out of the treeline."
        "Now that you get a good look at him, Wuldon is sharpening his khopesh with a grindstone."
        w "As I said. I need time to think."
        w "Please leave."
        "He said please, but... you can tell that he is ordering you to leave him alone."
        e "Okay. Sorry, again."
        "You quickly turn tail and leave."
    jump main_slumbrous_well

label Wuldon_Cavern_Return_Early:
    w "Back already?"
    e "Yes..."
    w "I take it you wanted to talk with me again."
    e "Yes."
    w "Well, before that, can i ask what happened to Vurro in the end?"
    e "I haven't found him yet."
    w "I'd rather we talk after that, if possible. I don't want Uffe to get any ideas and send someone else to kill his brother."
    e "Fair enough. I will talk to you later."
    w "I look forward to it. Good luck."
    jump main_slumbrous_well
label Vurro_Battle_Win_With_Wuldon:
    scene chelforte_cavern with dissolve
    $ wuldon_meet_before_vurro = True
    $ quest22.qComp(__("Return to Uffe"))
    $ quest22.status = 3
    "The Feral Werewolf finally falls unconscious."
    e "That... that was... way harder than expected."
    "It's difficult to get the words out between gasps of breath."
    "You sit down next to the werewolf's - Vurro's - crumpled form, and take a second to breath."
    "It is now that you have taken a second to clear the sound of rushing blood from your ears that you hear it."
    "A rumbling."
    "Panicked, you look around, and notice the walls of the cave spilling rubble and dust."
    "You realize the cave is going to crumble on top of you if you do not escape."
    "The support beams around you are beginning to tremble under the ceiling's shifting weight."
    "You rush to get up, but look back at the pitiful, defeated clump of fur behind you."
    "He might be feral, but... you can still remember Wuldon's story. Should someone like him really be left here to die?"
    "At the same time, however, the cave could come tumbling down at any moment, crushing both of you beneath it."
    menu:
        "What do you do...?"
        "Rescue the werewolf":
            $ vurro_lives = True
            "Looking at him, you can't help but see the pain on his muzzle, present even as he lays unconscious."
            "He found this cave. Wanted to use it to help his fellow werewolves."
            "He does not deserve to die here, alone and insane."
            "You rush over to his side, dropping to one knee and putting one arm between his legs, the other grabbing his forearm."
            "As you heft Vurro onto your back, you stumble forward, nearly thrown off balance by his unexpected weight."
            "Regardless, you turn to the distant light of the cave mouth, barely filtering through the falling brown sheets of dust before you."
            "You sprint forward, charging with the full weight of two people, doing your best not to fall off balance."
            "Just as you reach the cave entrance, you remember an important detail Wuldon had mentioned."
            "The cave entrance is too small for werewolves."
            "Horrified, you drop Vurro, and look for something, anything to save you."
            "There, in the corner, you see a pickaxe, rusted and covered in cobwebs. A faded remnant of a man's dream, and your only hope."
            "Immediately, you grab it, and run to hack open the entrance."
            "Now that the cave is falling apart, the opening to the cave is cracked and poorly held together."
            "You slam the pickaxe into the cave's entrance with the desperation of a man on the edge of the abyss."
            "A wide chunk is cut into the stone."
            "You bring the pick down again and again, frantically chipping as much as you can, before finally, the already damaged metal crumbles to uselessness."
            "Terrified and desperate, you throw the remnants of the pickaxe through the cave mouth, and begin heaving the displaced chunks of rock out of the way with your hands."
            "You widen the cave this way until it looks big enough to fit the feral werewolf's frame, before grabbing his arms and dragging him through the hole arms-first."
            "You make it 10 feet away from the cave before you hear a crash."
            "The first beam has fallen."
            "With that, the cave collapses. For the next 3 minutes, the world is incomprehensible to you."
            scene black with dissolve
            "There is only brown dust. It fills the air, coats the trees, the dirt..."
            "... it is in your lungs and eyes, and if you could feel them through the ringing left behind by the cave's collapse, inside your ears too."
            "Eventually, things become normal again. The world is still covered in a coat of brown, but you can open your eyes, blink out the filth, and cough out the invasive filth."
            "Vurro's brown form at your side is now several shades lighter, and firmly unconscious."
            scene dark_forest with dissolve
            "His breath is thin and raspy, each breath a strained whistle."
            "Part of his windpipe seems to be constricted by the cave's dust, feeding him enough oxygen to stay alive, but not to wake up."
            "You get on your knees and put your hands and head against his chest."
            "Despite still being unable to hear, you can hear his pulse is steady."
            "Relieved by this fact, you reach over and unclasp his nipple rings, before promptly passing out by his side."
            scene black with dissolve
            "..."
            "..."
            "..."
            pause 1
            scene wuldonshack with dissolve
            "The first thing you hear when you wake up is the crackling of a fire."
            "It is warm. There is something on top of you."
            "Opening your eyes, you see a rich brown-and-green ceiling, lit warmly by flickering firelight."
            "Looking down, to see what is on top of you, you see a green cloak."
            "To your right is the fire you've noticed the signs of."
            "It is not a large thing. It is only a few feet to your right, tongues of flame licking hungrily at the air, releasing the warmth you've felt caressing you since you woke."
            "It was due to all of this that you didn't wake up screaming, not knowing where you were."
            "You had a pretty good guess of where you were, but it was only confirmed as you saw a hulking blue form peer in through the cabin door."
            w "Well well well! Look at what we have here."
            show wuldon topless with dissolve
            "Wuldon is shirtless. This should have been obvious due to his cloak being on you, but..."
            "It was another thing to see it in person."
            "It might have just been the shadows cast by the firelight, but the werewolf at your door was massive in every sense of the word."
            "More so than you had thought before."
            "His muscles were clearly visible throughout his body, even at his plentiful gut."
            "His shoulders were nearly as broad as the door, which you were confident could fit two of you walking side-by-side."
            "At any other time, he would be terrifying, but all you could feel was relief."
            "With someone like this watching over you, you could rest soundly."
            "Your body still felt like it had been run over by a wagon, so that knowledge was comforting to say the least."
            w "Hello? Anybody there?"
            "The werewolf's normally gruff face and voice were at this point tinged by a note of concern."
            "It is rather difficult to think quickly."
            "You may have suffered a concussion."
            e "H-hello, Wuldon."
            "He cracked a smile to hear that."
            w "Ah, good, you're not dead."
            w "You're going to have to pay me rent for the night, and I don't want to have to take that from a dead man."
            "Wuldon's shit-eating smirk made you pretty sure that he was kidding, but..."
            e "You're kidding... right?"
            "Wuldon said nothing, just keeping that smirk on his face, and raising an eyebrow."
            e "...please say you're kidding."
            "Wuldon finally broke out into a laugh."
            w "Yes, I'm kidding."
            w "Even if I did charge to take care of folks, you'd have paid more than enough by saving Vurro."
            e "...How is he?"
            "Actually... you sit up in alarm, cloak slipping into your lap."
            e "Wait, where is he!?"
            "Wuldon's face is somewhat complicated."
            w "Well, I currently have him outside."
            w "He's... well, he's definitely still feral, but. He's alive and in stable condition."
            "He sighs."
            w "I'm glad to finally have him back, but... I'll need to find a way to save him."
            w "For now though, you need to rest up and get back to Uffe before he kills you."
            w "Find out more about that magic stone of yours."
            e "Okay."
            "You dutifully lay back down, and pull Wuldon's cloak back over you."
            e "How did I get here, by the way?"
            w "I heard the cave collapse."
            e "Oh, yeah. I guess that was pretty loud, wasn't it."
            "Wuldon chuckles."
            w "Yeah, that's one way to put it. And even if it hadn't been, I'd have put two and two together when I saw a massive dust-cloud kick up from over there."
            w "Regardless, I ran over to check on you, and sure enough..."
            "Wuldon gestures wordlessly."
            "You guess you were pretty pathetic right now. You can't even imagine how you must have looked when he found you."
            "Wait..."
            e "Hey, Wuldon... why aren't I covered in dust?"
            w "Oh, I thought you and Vurro could use some cleaning, so I took you two over by the well and cleaned you of your filth."
            "You blush."
            w "Oh calm down. It's nothing I haven't seen before."
            w "Though, one of the nicer bodies I've had the pleasure to be hands-on with."
            "Wuldon nods, his gruff voice putting this matter of factly."
            w "Not that I did anything untoward. Even kept your clothes on so you'd have your privacy."
            "...still embarrassing."
            w "Now, get some rest. I need to go check on Vurro."
            w "I'll be gone when you wake up. I'll be out trying to find some herbs that I think might help keep Vurro sedated."
            w "He'll be staying here, hidden in a small cellar beneath the house."
            e "Okay. What should I do if I want to find you again?"
            "Wuldon smiles slightly. He seems to find the suggestion sweet."
            w "I'll be checking back in here every once in a while. We'll coincide at some point."
            "Wuldon leaves the cabin. The last thing you see of him is the back of his massive hand raised in farewell through the doorway."
            w "I look forward to that time."
            "..."
            "You fall back asleep soon after."
            scene black with dissolve
            pause 5
            $ timenow.day+= 1
            $ timenow.hour+=12
            $ timenow.passTime()
            scene slumbrous_well with dissolve
            "When you woke up, Wuldon is nowhere to be seen..."
            "You better go back to report to Uffe."
            jump main_slumbrous_well
        "Take the Rings and Leave":
            $ vurro_lives = False
            "You turn to Vurro, and quickly spit out the reasons for your decision."
            e "Shit, I'm sorry Vurro."
            e "You're feral, with no cure in sight, and trying to help might kill me."
            e "I have to leave you behind."
            "With that done, you feel just a bit less guilty about leaving him here."
            "Bending down, you remove his nipple rings, and turn towards the exit."
            "You run at a dead sprint for the light of the cave entrance."
            scene black with dissolve
            "The cave is still shifting and shaking as you reach the entrance."
            with vpunch
            "You dash out onto the grass, and keep on running without looking back."
            with vpunch
            "That many tons of rock all falling at once will create a sizable shockwave. It is best to get as much distance between you and it as possible."
            "Eventually, your lungs give out, and you have to sit down and catch your breath."
            with vpunch
            "Legs and lungs burning, you rest your back and head against a tree."
            "..."
            "What a day."
            scene dark_forest with dissolve
            "You can only hang your head in defeat at how it has all gone, looking down at the nipple rings in your hands."
            with vpunch
            "At least you will be able to find out more about what happened with the stone."
            "Your head snaps up as you hear an enormous booming sound."
            "Moments after, you see an enormous plume of dust erupt from the direction of the cave."
            "Well... that confirms what you feared."
            "You're glad you made it out alive, but... you can't help but think about Vurro, dead and alone in that cave."
            "Soon, you see a blinding flash of blue streaking through the forest."
            "It's Wuldon."
            show wuldon normal with dissolve
            e "WULDON!"
            "The blur comes to a crashing stop; hundreds of pounds of force halting and pivoting in an instant."
            w "[e]?"
            "He looks concerned. He seems to be looking around for someone or something."
            e "Yup."
            e "I went into the cave to fight Vurro, and, well..."
            "You gesture vaguely to the giant plume of dust still drifting down from the sky."
            "Wuldon looks... sad. Sad, but not surprised."
            w "...I take it you left him in there?"
            e "... Yeah."
            "You look down, too ashamed to meet his eyes."
            e "The cave was coming down on top of us, and I didn't know if I could get out if I took him with me."
            e "I'm sorry."
            "There is a long silence between you after that."
            "When you finally get the nerve to look at Wuldon's face once more, you see a complicated expression on his face."
            pause 3
            w "..."
            w "I understand. It is good that you are alive."
            w "I will be going home now. Do not visit me for a while. I need time to think."
            hide wuldon with dissolve
            "Wuldon leaves without another word, heading straight back in the direction he came from."
            "Your eyes go back to the floor. All you can do is mumble a defeated okay, and get back up."
            jump main_dark_forest

label Vurro_Battle_Win_Without_Wuldon:
    $ quest22.qComp(__("Return to Uffe"))
    $ quest22.status = 3
    scene chelforte_cavern with dissolve
    "The Feral Werewolf finally falls unconscious."
    e "That... that was... way harder than expected."
    "It's difficult to get the words out between gasps of breath."
    "You sit down next to the werewolf's crumpled form, and take a second to breath."
    "It is now that you have taken a second to clear the sound of rushing blood from your ears that you hear it."
    "A rumbling."
    "Panicked, you look around, and notice the walls of the cave spilling rubble and dust."
    "You realize the cave is going to crumble on top of you if you do not escape."
    "The support beams around you are beginning to tremble under the ceiling's shifting weight."
    "You rush to get up, but look back at the pitiful, defeated clump of fur behind you."
    "He might be feral, but... he spoke. Should he really be left here to die?"
    "But you don't know when exactly the cave is going to crumble, crushing both of you beneath it."
    menu:
        "What do you do...?"
        "Rescue the werewolf":
            $ vurro_lives = True
            "Looking at it, you can't help but see the pain on its muzzle, present even as it lays unconscious."
            "Feral it might be, but nothing deserves to spend so long in a cave, all alone, only to die crushed."
            "You rush over to its side, dropping to one knee and putting one arm between its legs, with the other grabbing its arm."
            "As you heft the werewolf onto your back, you stumble forward, nearly thrown off balance by its unexpected weight."
            "Regardless, you turn to the distant light of the cave mouth, barely filtering through the falling brown sheets of dust before you."
            "You sprint forward, charging with the full weight of two people, doing your best not to fall off balance."
            "Just as you reach the cave entrance, you realize something you hadn't thought of."
            "It's too small for werewolves."
            "Horrified, you drop the feral werewolf, and look for something, anything to save you."
            "There, in the corner, you see a pickaxe, rusted and covered in cobwebs."
            "Immediately, you grab it, and run to hack open the entrance."
            "Now that the cave is falling apart, the opening to the cave is cracked and poorly held together."
            "You slam the pickaxe into the cave's entrance with the desperation of a man on the edge of the abyss."
            "A wide chunk is cut into the stone."
            "You bring the pick down again and again, frantically chipping as much as you can, before finally, the already damaged metal crumbles to uselessness."
            "Terrified and desperate, you throw the remnants of the pickaxe through the cave mouth, and begin heaving the displaced chunks of rock out of the way with your hands."
            "You widen the cave this way until it looks big enough to fit the feral werewolf's frame, before grabbing his arms and dragging him through the hole arms-first."
            "You make it 10 feet away from the cave before you hear a crash."
            "The first beam has fallen."
            "With that, the cave collapses. For the next 3 minutes, the world is incomprehensible to you."
            "There is only brown dust. It fills the air, coats the trees, the dirt..."
            "... it is in your lungs and eyes, and if you could feel them through the ringing left behind by the cave's collapse, inside your ears too."
            "Eventually, things become normal again. The world is still covered in a coat of brown, but you can open your eyes, blink out the filth, and cough out the invasive filth."
            "The already brown feral werewolf at your side is now several shades lighter, and firmly unconscious."
            "Its breath is thin and raspy."
            "Part of its airway seems to be constricted by the cave's dust, feeding it enough oxygen to stay alive, but not to wake up."
            "Relieved by this fact, you bend down and unclasp its nipple rings, before promptly passing out by its side."
            scene black with dissolve
            "..."
            "..."
            "..."
            pause 1
            "The first thing you see when you wake up is the night sky."
            "You have no idea how long you slept."
            "Looking to your side, you see the still unconscious form of the feral werewolf."
            "You hadn't really thought this far, but... what do you do with this guy."
            "He seems immune to starvation, which is nice, as it means you don't have to take care of him, but..."
            "What if he wakes up?"
            scene dark_forest with dissolve
            "You quickly answer this question by remembering that you can bind him."
            "Over the course of the next few hours, you make impromptu set of bindings using some loose scraps of cloth you'd accumulated over time, from messing up various projects for Rahim or others."
            "Now that his mouth, arms, and legs have been bound, you can properly think."
            "..."
            "..."
            "Well, shit."
            "You really didn't think things through before you saved him, did you."
            "Uffe sent you here with the specific goal of killing this werewolf."
            "But now that you almost died trying to save him, you might as well keep him alive. Try to find a cure or something."
            "You probably shouldn't tell Uffe about him if you want to do that, but... you'll cross that bridge later, you suppose."
            "...A hiding place is probably in order."
            "On the other edge of the clearing is a brown bush, likely previously green, big enough to hide your charge."
            "Dragging him over there, you get to see in full detail just how mangy and depressing he is."
            "You really cannot do anything with him in this state. He is instantly recognizable compared to the other werewolves."
            "Not only that, what with him being bigger than you, you cannot possibly hope to carry him without being caught."
            "So... you resolve to leave him behind, and either try and find a cure, or tell Uffe about him."
            "Until then, however, he will be staying in this bush."
            jump main_dark_forest
        "Take the Rings and Leave":

            $ vurro_lives = False
            "This is a feral creature, even if it might have once been a person."
            "However much you might want to save him, you know it would be risking your life for what is essentially a rabid animal."
            "Bending down, you remove his nipple rings, and turn towards the exit."
            "You run at a dead sprint for the light of the cave entrance."
            "The cave is still shifting and shaking as you reach the entrance."
            "You dash out onto the grass, and keep on running without looking back."
            "That many tons of rock all falling at once will create a sizable shockwave. It is best to get as much distance between you and it as possible."
            "Eventually, your lungs give out, and you have to sit down and catch your breath."
            "Legs and lungs burning, you rest your back and head against a tree."
            "..."
            "What a day."
            scene black with dissolve
            "You can still feel the adrenaline coursing through your system, and a newly released chemical slurry flooding your brain and filling you with relief at your survival."
            "You mess with the nipple rings in your hands."
            "It was a lot of work, but now you'll finally be able to find out more about what happened with the stone."
            "Your head snaps up as you hear an enormous booming sound."
            "Moments after, you see an enormous plume of dust erupt from the direction of the cave."
            "Well... that confirms what you had feared."
            "You sigh, tension coming out of your body all at once."
            "You're glad you made it out alive."
            "The feral werewolf's death was what you were asked for, and... however unintentionally, it's what you brought about."
            "You apologize to the person they may have once been, and get up."
            jump main_dark_forest

label Wuldon_Raid_Preparation:

    $ QuestBegin(quest41)
    $ quest41.qProgress(_("Meet Wuldon and Vurro at 8:00 in the morning"))
    "Once more, you return to Wuldon's house."

    if quest28.status:

        "It seems like Wuldon and Vurro are finally here, if the snoring is anything to go by. Unfortunately, the already deafening snores only seem to be louder than before."
    else:


        "It seems like Wuldon and Vurro are done preparing, if the snoring is anything to go by. Unfortunately, the already deafening snores only seem to be louder than before."

    "Unlike your prior experiences coming here, Wuldon's door is open, and you make it inside undisturbed."
    scene wuldonshack with dissolve

    pause 
    "Inside, you see Wuldon sharpening his khopesh. For once, he doesn't seem to notice you immediately."
    "Sneaking closer, you see that the werewolf's ears are stuffed with a copious amount of wax, clearly having lost his patience long ago, wariness be damned."
    "A wicked grin comes over your face as you realize you can finally exact revenge on him."
    "You creep closer and closer, stopping only when you're worried your breath may alert him to your presence. The range should be sufficient for what you want to do, however."
    "Foregoing stealth, you strike out like a snake, putting your hands on Wuldon's shoulders to spook him."
    pause 0.5

    with vpunch
    with blackflash
    "Unfortunately for you, rather than jump in surprise, Wuldon turns and gets up in the same action while slamming his hand into your throat."
    scene wuldonshack:
        blur 8
    with dissolve
    with blackflash

    scene wuldonshack with dissolve
    "Moving on pure instinct, the werewolf shoves you against the wall, where he holds you by only your neck."
    scene wuldonshack:
        blur 32
    with dissolve
    "His teeth are bared in a snarl, his muscles bulging as his body tenses. Looking into his eyes, you see nothing of the blue werewolf you know - there is only the rage and fear of a cornered animal."
    with vpunch
    "You try to yell for him to stop, but his hand against your throat prevents any coherent sound from escaping your lips."
    with hpunch
    "After a few moments spent fearing for your life, you see the blue werewolf's eyes begin to clear."
    scene wuldonshack with dissolve
    "Immediately, he removes his hand from your throat and takes two steps back. The rage is gone, but the fear remains."
    show wuldon nobo with dissolve
    "It's entirely likely that you're mistaken, given your own sorry state, choking and spluttering as you sag against the wall."
    w "Are yo-"
    "Wuldon realizes his voice sounds odd after only moments, taking a little longer to realize the cause. He begins speaking once more the instant he removes the wax from his ears."
    w "Are you okay, [e]? If you're hurt, can I help you?"
    "You shake your head, but realize he doesn't know what you're saying no to."
    e "No, I'm- {i}HRRK{/i}."
    e "I'm-"
    "You shove down the wretch that threatens to wrack your body."
    e "I'm fine."
    w "Is it okay for me to come over to you?"
    "As soon as you nod your head, Wuldon comes over to check on you, looking at your throat and back for any signs of bruising."
    show wuldon nobucket with dissolve
    if wuldon_like > 4:

        w "Thank god, you're alright."
        w "I don't know what I would have done if I had hurt you."
        "Before you can process his words, Wuldon grabs you and pulls you into a deep hug that buries your head into his chest."
        "His hands reach upwards tentatively. When you hug him back, he begins doing what he was holding himself back from, rubbing the back of your head and middle of your back gently with his hands."
        "The two of you stay like that for a good while. You say nothing, worried that doing so will end the moment."
        "It is only when the two of you realize that the snoring has stopped that you break off the hug."
    else:


        w "I told you to always be on guard, but seem to have forgotten to do so myself."
        "Wuldon scratches the back of his head awkwardly."
        w "Sorry about choking you like that."
        w "At least it teaches the lesson of training your body to react to any threat instinctively?"
        "He says this with a weak grin, fully knowing he's fucked up, and that there is no lesson here."
        e "It's fine, though you may not want to kill me before we kill Uffe. It would be a bit unfortunate for both of us."
        "You get an awkward chuckle at that."
        "When it ends, you both sit in silence."
        "..."
        "It takes a bit for the two of you to realize that the house should not be silent."
    show wuldon at l1 with move
    show vurro clothed at r2
    show vurro at r1 with move

    "The two of you look over at Vurro, who is staring at the two of you owlishly."
    "You have no idea how much he saw or heard, and it seems neither does Wuldon."
    v "Good morning to you too."
    pause 0.1
    "Regardless of whatever he just witnessed, the brown werewolf seems to care not, slipping out of bed to grab some breakfast from a shelf."
    with vpunch
    w "Hey! Who said you could use the good jams?"
    "Vurro gives Wuldon a blank shrug."
    v "Mm. You woke me up. Compensation."
    "It's at around this moment that the two of you realize Vurro is still half-asleep. He pulls out a seat for himself, dropping the food - sliced bread with jam - haphazardly on the table."
    e "Do you mind if I sit down with you?"
    v "Mm."
    "That and a shake of the head are all you get. Looking at Wuldon at your side, he gives you a shrug, pulling out a seat for himself to sit at."
    e "I'll take that as permission."
    "Grabbing a chair of your own, you sit down on Wuldon's surprisingly well made furniture."
    pause 1.0
    e "I'm here to talk about what we're going to do about Uffe."
    "Both werewolves look at you in surprise, the shock of it waking Vurro up completely."
    v "I'm surprised you're the one bringing it up, I thought you wouldn't want to do this?"
    "You give them a nod."
    e "I don't. But I know I have to. We've talked about it, and it's the only way for me to live."
    e "It doesn't hurt that it helps the werewolves and you either."
    v "Well. I'm glad that you want to help."
    "The three of you wait in silence."
    e "Do you, um. Do - Please tell me you have a plan."
    "This draws amused looks from the two werewolves sitting across from you."
    v "Yes, we have a plan."
    v "It's dangerous, and you'll have to play an important role, but it's a plan."
    "A shiver goes down your spine."
    e "How dangerous are we talking?"
    "Vurro gives you a toothy grin."
    v "You'll be the one killing Uffe. Us two will handle fighting off the werewolves."
    "You raise an eyebrow at Vurro."
    e "Isn't fighting Uffe the most dangerous part?"
    v "Normally I'd say yes, but when you weigh fighting Uffe alone versus fighting fifteen werewolves at once, it's not as clear."
    e "Ah. I see your point."
    "You fall back into silence."
    pause 2
    e "Can I get something more detailed though?"
    "Wuldon nods your way, not teasing you for your impatience for once."
    "It seems he's not in the mood to mess around."
    w "To lay the groundwork, our plan will start at 9:30 pm, with you inside of the tribe's grounds, and us watching from as far away as possible."
    w "The tribe has developed the tradition of hunting together at 9 pm every night. It's only about half the tribe that will leave, but if we want our plan to succeed, that is when we must start."
    "Wuldon's explanation is somewhat cryptic, as it feels like he expects you to understand the reason behind everything he's doing."
    "Helpfully, Vurro pipes up."
    v "We don't plan on fighting everyone that stays, but the less people nearby, the better our odds."
    "The smaller werewolf nods to Wuldon, telling him to keep going. The only reason Vurro isn't explaining is probably the breakfast he's tiredly working through."
    w "The actual plan itself is roughly as follows."
    "The werewolf takes a deep breath, working past some sort of hesitation."
    pause 2
    w "At around 9:30 in the morning, you'll go talk to Uffe and tell him you've been exploring for a while - make it clear you haven't been in town for about a week."
    "You raise your hand to interrupt and ask a question."
    e "Why would he believe that? If he wants to get rid of me, he'll have been monitoring me, putting this entire plan in jeopardy."
    e "Do you have anything planned for that?"
    "Both werewolves give you an appreciative look."
    w "Frankly, we don't need to have anything planned."
    w "Uffe relies heavily on his sense of smell, so as long as we get the smell of Lusterfield off of you, he should be fooled. I'll let you use my bath so that you don't have to go into the river."
    "That made sense, up until you remember an important fact about Wuldon's house."
    e "You have a bath? I've looked all over your house, and found nothing like that."

    if wuldon_like > 4:

        "Wuldon briefly looks over at you, opening his mouth as if to tease you, before thinking better of it. It seems it is not the time for flirting."

    w "Yes, I have a bath. It's a few minutes away, and known only to Vurro and I."
    "Calling it 'his bath' when it was in the middle of nowhere was a bit generous, but that at least explained why you hadn't found it."
    w "The plan depends entirely on Uffe being the bastard we think he is. If he doesn't try to capitalize on what he thinks is a moment of weakness, we can't kill him, and maybe shouldn't kill him."
    w "Regardless. After you tell him where you're going, he's most likely going to tail you with a few werewolves of his own."
    w "As soon as you get somewhere he thinks he can get rid of you quietly, he'll go for it."
    "So far, this plan is just you inviting Uffe to come over and kill you. If this is it, you're going to beat them over the head with the nearest blunt object."
    w "Before he can do that, Vurro will ambush him."
    "Much better."
    e "And you? Your role isn't very clear to me."
    "The blue werewolf shrugs his shoulders."
    w "You won't be completely isolated. Uffe is too impatient for that, and if he isn't, that's not a bet we're willing to take."
    w "Your safety is priority number one. In order to help with that, my job is to incapacitate any werewolves that try and interfere."
    "Holding a massive perimeter against most of a tribe sounds outright insane, but he's given you reason enough to trust his abilities."
    "Wuldon leaves things at that, clearly seeing the debriefing as done, but Vurro pipes up again to clarify things further."
    v "Our job is made harder by the need to kill Uffe and {i}only{/i} Uffe. None of the other werewolves we fight are to be permanently injured or killed."
    "Vurro looks slightly irritated as he says that. When he sees you looking askance, he elaborates."
    v "It is far easier to kill someone than knock them out. Because of that, I likely won't be able to help you very much with Uffe."
    v "It's also just a bit frustrating to see his lack of morality give him an edge over me. Again."
    "The brown werewolf smiles weakly at you, clearly wishing he didn't have to rely on others for help with his plan - that he were strong enough to do it on his own."
    v "While I don't think I'll be able to help you with my brother, I can at least promise to take care of the werewolves he brings with him."
    "Fighting Uffe alone sounds extremely dangerous, but it's definitely better than any of the alternatives. Fighting anything more than two werewolves at once sounds like a death sentence."
    e "I understand, and thank you for having my back."
    "This did kind of suck, but it was the kind of awful you could work with. Plus, you couldn't exactly complain when he looked so guilty about it."
    e "Alright. That doesn't sound terrible. Better than anything I'd thought up anyways."
    "Wuldon looks up with a bit too much interest."
    w "Really? I want to hear your plans."
    pause 0.5
    "The corners of the werewolf's lips are twitching slightly as he does his best to look genuine, and not at all mischievous. It only makes you raise an eyebrow at him."
    e "I'm not falling for that."
    "Maybe you'd believe him if he didn't look like he was holding back a laugh. Then again, there was also something off with it this time."
    "The blue werewolf chuckled softly, acting greatly amused by your response."
    show wuldon:
        linear 0.15 xalign 0.5
        linear 0.06 xalign 0.3
        linear 0.06 xalign 0.5
        linear 0.15 xalign 0.05

    w "It seems you're learning! More than what I could say for a certain someone."
    "Wuldon gently nudged the smaller werewolf to his right, who gave him a half-hearted kick to the shins in return."
    v "I've learned. I only indulge you out of pity."
    "The two werewolves stare at each other with fake anger, only to snort at their shared gag."
    "Unlike normal, however, their laughter rings hollow."
    v "I wish we had more time, or that we didn't have to do this… but I wasn't supposed to get this second chance in the first place."
    v "And I'm not going to let it go to waste."
    "Vurro lets out a long sigh as Wuldon pats him on the back. However much both of them try and laugh it won't truly make them feel better."
    v "Thank you for being with me for this, both of you."
    "You and Wuldon exchange a somewhat concerned glance."
    e "Well, of course I'm here! You already know I need to do this if I want to stay safe."
    "Wuldon only lets out a deep rumble, his thoughts on the matter not even needing to be stated."
    "Vurro gives you both a weary smile."
    v "I suppose I had no reason to worry, then."
    "Despite his words, Vurro is practically trembling from a mix of fear and anticipation."
    "The shaking stops when Wuldon places a giant hand on Vurro's shoulder."
    w "It's alright. We all know our parts of the plan, so why don't we all take some time to rest, and prepare ourselves before the fight?"
    "Wuldon projects unwavering confidence, cutting any rising worries from growing further."

    if wuldon_like > 4:
        "Despite his best attempts, however, both you and Vurro see the way his muscles twitch as he tries to keep his unease from surfacing."

    v "..."
    v "Alright."
    "The tired werewolf lifts his gaze up off the table to look at you."
    v "You'll need to be here by 8:00 in the morning so you can bathe before we start our plan. I'll be setting up everything you need for it in the meanwhile."
    "What might take hours to prepare for a bath, you have no idea."

    if quest28.status:

        "But you do get the feeling Vurro wants to have one last talk with you before you go."

    e "I'll be there."

    if wuldon_like > 4:

        "Wuldon looks like he wants to say something to you, but seems to settle for moving over to you for a warm hug."
        "You feel a brush of warm air by your ear as he moves his head down next to yours."
        w "Stay safe, little one."
        "The unguarded worry in his voice makes you hug him back a bit harder than normal."
        e "You too."
        "After a few more moments spent holding each other, the two of you separate reluctantly."

    "With nothing else to say, you turn around and head out, leaving the two werewolves to their preparations."


    jump main_slumbrous_well

label Wuldon_Raid_Planning:

    $ quest41.qComp(_("Spar with Vurro"))
    "As you approach Wuldon's house, you hear a sharp ringing noise, which you recognize as the sound of a whetstone on a blade."
    "Sure enough, when Wuldon's house comes into view you see the blue werewolf at his doorstep, ritually sharpening his khopesh."
    show wuldon nobucket with dissolve
    "As always, Wuldon notices you instantly, putting aside his weapon and calling for Vurro to come out front."
    "Wuldon turns to you with a mischievous grin."
    w "He's preparing the bath for you right now."
    "His grin turns to a small chuckle as Vurro comes into view, sopping wet and thoroughly unamused."
    show wuldon at r1 with move
    show vurro clothed at l2
    show vurro at l1 with move
    v "I think [e] could have figured that out on his own, Wul."
    v "Just because you won the spar to determine who would do it doesn't mean you have to crow about it whenever you have the chance."
    "Vurro pauses to shake some of the water out of his fur, making sure to catch Wuldon in the spray as the latter attempts to bat him away with his paw."
    "The incident ends with two slightly wet werewolves grinning at each other, both pausing as they see your bemused expression."
    pause 1.0
    e "And here I thought you two were in a bad mood?"
    "Both werewolves wave you off, clearly dismissive of the thought."
    v "We had to be serious while we discussed the plan earlier - killing my brother is no small task, and it deserves both focus and respect."

    v "And yes, even now, giving that task the gravity it is due is important."
    pause 0.5
    v "But we are all friends, and friends who may not get to spend time together again."
    pause 1.5
    "You hadn't noticed it at first, but hidden under the joy writ across their faces was also the pain of knowing that tomorrow would always come, with or without the people by your side."
    v "We can talk about the task to come, or anything else. But I'd like to do it as friends."
    "His voice falters slightly as he struggles to finish his request."
    v "It might be selfish, but I want your last memory of me to be a good one. I want to be remembered for who I was, not for what is going to happen."
    "By the end, Vurro had his hands clasped together nervously, struggling to keep the smile on his face in the silence following his request."
    if quest27.status and wuldon_like < 4:
        "You reach out to Vurro before you even realize what you're doing, putting your hand on his shoulder and looking him in the eyes."
        e "Of course. I want to cherish whatever time we have left together."
        "Before you could figure out anything else to say, Wuldon wrapped the two of you up in a hug, nuzzling his head against Vurro's."
    elif quest27.status:
        "You reach out to Vurro before you even realize what you're doing, putting your hand on his shoulder and looking him in the eyes."
        e "Of course. I want to cherish whatever time we have left together."
        "Before you could figure out anything else to say, Wuldon wrapped the two of you up in a hug, nuzzling his head against Vurro, before turning to you, hesitating slightly before planting a soft kiss between your ears."
    else:
        "The silence didn't end for a while, as you struggled to form a response."
        e "I can't say I deserve the honour the same way Wuldon does, but I am happy to make more memories with a new friend."
        "In response to your words Wuldon gets up and wraps him in a hug that lifts his feet off the ground."


    w "Like I said when you asked me this earlier, it was always going to be a good memory - it's a memory of you, after all."

    if wuldon_like > 4:
        "So saying, Wuldon lets go of Vurro, though he still keeps his arm around your shoulders, pressing you close protectively. "
        "You look up at the werewolf next to you, preparing to tease him - but as you open your mouth, you hesitate, taken aback by the strange look on his face."
    else:
        "So saying, Wuldon lets go of Vurro. A strange expression on face."
    "Wuldon's expression was one caught between joy and grief, a melancholy smile paired with eyes that glinted with mirth."
    "It reminded you that even when you first found him, at the depths of despair, he had not lost his humor."
    pause 0.5
    w "Let's make it the best memory we can."
    "He looks at you significantly, urging you to speak."
    e "You'll hear no complaints from me."
    "Rolling his eyes at your choice of words, Wuldon reached over and wrapped his arms around."
    if wuldon_like > 4:
        "Instinctually, you reach out and grab hold of the two werewolves, reciprocating the hug."
        "It took you a while to realize that this was as much a hug as it was an excuse for Wuldon to hold the two of you and protect you while he still could."
        "You can't help but laugh at the werewolf's actions."
        e "Alright, fine. I'll outright say it."
        "As you speak, you wrap one arm around Vurro, and the other around Wuldon."
        e "However much I want to get rid of Uffe, I also want to treasure the little time we've got remaining."
    else:
        "You let out a small sigh at the pair of silly werewolves' antics."
        "Still, it's hard not to like them, and at the end of the day, they were looking out for you just like you were looking out for them."
        "Even if part of the reason you were helping them was to avoid death."
        e "You could have just asked, and I'd have come over for a hug."
        "Despite the grouchiness of your tone, you turn to properly hug the two of them. Well, you try to - your hand can't really reach very far across Wuldon's back."
        w "This was more fun."
        "The blue werewolf began to laugh as you grumbled good naturedly, a sound that snapped Vurro out of his temporary funk."


    e "Vurro, do you have any tips for fighting Uffe? I was told that you've fought him a few times before, and I need any edge I can get."
    "Vurro nodded genially, while Wuldon walks over to his station to prepare for his weapon."
    show wuldon at r2 with move
    v "I was actually planning on covering that with you one on one. It would be good for us to spar so that I had some idea of your fighting abilities."


    v "Not trying to judge your battling skills, you know."
    show vurro at c1 with move
    "Vurro's reassuring you, but the raised corners of his mouth tells you otherwise."
    e "I wasn't thinking that."
    v "You've already beaten my feral self, the state that I'm in right now is definitely not stronger in any plane of existence."
    e "Vurro, you just woke up, are you sure you want to spar with me? If anything I have this little blue werewolf over here to train with."
    v "Heh I don't doubt that, but I have to face Uffe with you too, I suppose sparring before our bath would prove useful to prepare for."
    "Vurro furrows his brows as he inspects the sharp hooks on his hand. A sense of bewilderment can be sensed on his face."
    e "No objection from me."
    w "Me neither."
    "The blue werewolf replies from afar."
    v "Good, though I didn't remember asking the big lug over there."
    w "Hmmm... just don't get yourselves caught before I sharpened my weapon."
    v "Oh don't you worry, in [e]'s hand I'm just safer than you can ever imagine."
    v "Look at thes-"
    "Vurro raises his nails, his twinkly eyes doesn't hide his own struggle to stay awake, with scrawny furs all over the place."
    "Wuldon seems to have noticed, his smile fades almost instantly, turning back and focusing on his weapon instead."
    "Without another word, you follow the brown werewolf from the slumbrous well."
    scene dark_forest with dissolve

    show vurro clothed with dissolve
    e "What if they somehow come here and spot you? Will Uffe know?"
    v "Nope, no trace or smell of any other werewolves around. We're safe out here. Uffe doesn't even know Wuldon."
    v "Actually, I never expected one day this little paradise between me and Wuldon had turned into a hiding place."
    v "Much much before everything changed, our father had me and Uffe playing hunting games. And at first, we both had a lot of fun."
    v "We-"
    "Vurro stutters for a moment. His gaze hangs ahead."
    v "Maybe I spoke too fondly of a person who just tried to doom me into eternal rampage. Sometimes, I just wonder if I could have done something before our relationship became so strained."
    e "I don't believe you could've done anything, he is just going to end up being evil, in another way."
    v "Could be. You're right. There's no use reminiscing the person we're planning to kill right now."
    "Vurro silently walks ahead. You follow him to an opening enveloped by the forest."
    v "There it is."
    "Vurro pulls up his poncho, stretches his jaws while kicking against the dirts to get a feel of the ground."
    "He turns around and faces you."
    v "Let's do it."
    e "Hey, Vurro. Are you really sure we've got to fight? You seem... sleepy."
    v "Fighting helps me stay awake. Come on."
    "Vurro raises his fist at you, his legs extends into a stable position. The fight is on."
    jump vurro_spar_battle

label Wuldon_Raid_Bath:
    scene dark_forest with dissolve
    v "I could've turned into the monster and killed you."
    e "And I'm still alive."
    show vurro clothed with dissolve
    "You says, but quickly lower your head, obviously you don't want your friend to transform in front of you, but right now it almost seems like a certainty, the matter is just when."
    v "Fuck, why do this even happen. Why can't we just be normal for once."
    "Vurro mumbles underneath his breath, he squints his eyes shut forcefully, just to open once more."
    e "Vurro, I- I'm here for you. Wuldon is too."
    pause 0.5
    "The brown werewolf blinks, almost like he's snapped back into reality. He slouches against the tree, struggling to stand."
    v "I'm sorry."
    "You stand, and pulls up the werewolf as he rises. In spite of his short of breath, he doesn't bother more than he's worried."
    "He takes a couple seconds to look around, peering ahead between trees and bushes."
    v "But, we're fine now. So, that's a relief."
    e "Are you sure?"
    v "Yes, I'm not dead yet."
    "It's painful having to watch your friend slowly descend into the monstrous form, powerless to the inevitability. Maybe there's a light at the end of this dark tunnel, but you doubt it."
    "But the brown werewolf quickly picks up on your lowered head, Vurro's brows relax immediately, he just seems much less distressed than you do."
    v "Come on, little one. The bath's getting cold."
    pause 1
    "He extends a faint smile, before heading back."
    if vurroSpar.win > 0:
        v "By the way, your fighting abilities are certainly impressive to say the least. I've not seen many folks who can hit me. You've got me good there."
    else:
        v "By the way, your fighting abilities are certainly impressive to say the least. If not for my... feral strength, you might as well beat me up there."
    e "Thank you, Vurro."
    v "I'm confident we'll take him down, that I have no doubt."
    "You anticipate the next sentence from Vurro, but he seems to have stuck in his thought once more."
    pause 1
    "Towards the path back, it's almost all silence, Vurro does not utter a word, and you don't even dare to speak."
    scene slumbrous_well with dissolve
    "But soon, you two cross the well. Wuldon waves at you from afar, unknowing that his friend almost died in a fight ten minutes ago."
    "Vurro waves back, and you follow suit, passing the blue werewolf a wobbly smile."
    v "So, this is the bath. Very primitive I know. But just enough to cleanse the scents on you for a while."
    show vurro clothed with dissolve
    "He points at the wooden tub situated just near the well. The water is steaming with white mist, seemingly just carried out by Wuldon."
    "You notice a few strips of herbs scattered on the surface of the water. With a piece of towel that Vurro picks up lazily."
    e "Am I supposed to be sitting in there?"
    v "Yeah, and you need to take off your clothes too. Do that separately if you want to keep your clothes dry."

    "You nod, though how many times you've been through this, it's still embarrassing to strip naked in front of Vurro, despite how many times you've been that way."
    e "O-okay."
    "His gaze is still onto you and your clothes, which makes it much more difficult."
    v "Relax, I swear I won't tell Wuldon I saw your private part earlier than he does."
    "The brown werewolf jokes, and it doesn't ease you anyhow. So you stand staring at him."
    v "I'm gonna see that when you're done stripping anyway."
    "Vurro sighs as the pair of eyes gazing in your direction quickly tilts away as he turn on his back."
    "You continue taking off your clothes, one by one until you're bare naked."
    e "Done."
    v "Alright then, now get in there."

    pause 1
    "You lift your leg up, just enough to step onto the ledge of the wooden tub. Then you leap through with the other leg, dropping leg first into the water."
    "Submerged inside the heating water, you take a few seconds to get used to the heat."
    pause 1
    v "How's the bath? Feeling the scent leaving you yet?"
    e "I think it's my fur that's leaving my skin right now."
    "Vurro pinches your shoulders, brushing his claws against the wet fur."
    v "Huh, you will get used to the heat, don't worry."
    v "Scream if it's really hot though."
    "He lifts a wooden ladle from the side, then scoop up some water before pouring onto the back of your neck."
    pause 0.5
    e "Thanks, Vurro, for preparing the bath."
    v "Look, I'm not gonna die soon so you can save these gratitude for when we actually fight my brother."
    "He places his elbow onto the edge of the wooden tub, before leaning forwards, stiring the water lazily."
    v "The way I see how it'll end for me, is when we're fighting Uffe. The perfect moment for me to leave this world would be right after knowing he's dead."
    pause 1
    "The brown werewolf takes out a bath towel to scratch your back, scrubbing off all scents that you can or cannot smell from your fur."
    v "I'll likely transform then, the panic and exertion will speed the process up, like what we just had, but ten times more painful."
    "He stands idly, staring blankly onto the forests ahead."
    pause 1
    v "I will turn into what Uffe wanted me to be, that disgusting form of existence without a thought of humanity."
    "Even if your back is against Vurro, you can feel that sense of dread and sorrow from Vurro."
    v "[e], when I'm gone, and Uffe is dead, please end that other monster."
    "What is Vurro talking about, to... kill him? That came as a pure shock to you that your body instantly froze, even in hot water."
    e "T-that... I don't know if I can."
    v "You're doing that for the safety of other people."
    "His speech quickens, looking for a response from you, and you only slide deeper into the water."
    v "The werewolf you saw in the cave, and the same werewolf that you will see fighting against Uffe, they are not me. You know that, right?"
    e "But the passionate and loving werewolf is still there, deep inside. Just like when we woke you up."
    v "Even so, you can't cure a werewolf twice."
    "Vurro replies as he pour a bucket of bathwater onto your head, a few leaves left hanging on your head."
    pause 1
    e "I... I can't, you're my friend."
    "Vurro looks down, his palm scrubbing against your fur as it keeps soaking in the bathwater."
    v "I remembered telling myself that I didn't mind dying, if it's for the good of our pack."
    v "Maybe I am not as noble as I thought I am, but this dreading thought of losing myself has been plaguing my mind every second since I woke up. It's a nightmare that never stops ceasing."
    "He says it with a deeper voice, as if he knew the doom is impending, it's worrying, honestly."
    v "I know I am being selfish, but a part of me hoped I was never cured. I could have died not knowing that the monster I've became killed everyone in the cave."
    e "That werewolf is not you. You told me that."
    "He doesn't respond, instead he wraps his arm around your shoulder, rubbing every inches on your chest."
    v "I could have died without seeing Wuldon and you reminding me how much I've had, just to lose them all again."
    "The brown werewolf reaches lower, hands tracing around"
    v "But, I'm glad I did. I'm glad to share some more memories with you, finishing my business before I leave, that's not a luxury everyone can afford."
    "You enjoy the time in the bath with Vurro sniffing and brushing, but at the same time you're just extremely distressed by the unfateful reality."
    v "So, thank you for saving me back in the cave."
    "His voice rises, feinting a wide smile to you."
    v "[e], take care of Wuldon for me, would you?"
    "You nod, you understand the severity of the situation, but it's still surreal to see your own friend telling you his death wishes."
    e "I- I will."
    v "No, that's not right... I can't tell you what to do on my behalf. Both in whether to kill me, or to take care of Wuldon."
    v "That is a huge cross to bear, and I don't wish it upon you."
    v "I won't be here by the time you two had killed Uffe, it's pointless for you to promise me anything."
    "His breathing begins to slow down to a normal pace."
    v "But, on a brighter side, you and Wuldon will survive."
    v "You know, however that blue dork might look gruff on the outside, he's still that sweet little werewolf with no friend deep down."
    "Vurro smiles faintly."
    if wuldon_like > 4:
        v "Not to talk him down, but it's pretty clear that he likes you a lot, [e]."
        v "He sucks at letting people know his feelings, but I saw his face blushing like a tomato everytime we talked about you."
        v "I guess what often happens is, you don't resonate that feeling, or that things don't end up working out between you two."
        v "Even so, please be gentle with him, he won't have anybody left when I'm gone."
        "You turn to stare at Vurro, who's tapping on the side of the bathtub."
        e "No, Vurro, I don't think I will ever leave Wuldon after everything we've been through."
        v "Hah, good to know. I won't interfere with whatever's going on with you two further."
    else:
        v "Well, at least now he has you on his side. That makes me feel a lot better."
    "Before you have even processed what he said, Vurro extends his scrawny hand in front of you."
    v "Time to get out of the water, little one."
    e "Oh!"
    with vpunch
    "You reach out to grasp onto his hand, but he retreats immediately."
    v "Nuh uh. You don't wanna clean yourself again do you?"
    "He chides, wiggling his finger in front of you."
    e "O-okay. You got me there."
    menu:
        msg "Work in Progress! You can save here and continue in the next update, and/or reset the quest and return to the beginning of the quest."
        "Return":
            $ quest41.status = False
            $ quest41.progress = []
            $ quest41.start_date = 0
            $ quest41.start_hour = 0
            $ activequests.remove(quest41)
            jump main_slumbrous_well
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
