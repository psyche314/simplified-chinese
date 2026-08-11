label Otsovaara_Introduction:


    scene frostedtaiga with dissolve
    "The snow-covered taiga stretches out as far as the eye could see, a serene yet harsh wilderness."
    "Your breath mists in the cold air, and you can't help but shiver under your soft fur."
    "Tall pines stands sentinel, their branches are heavy with snow, and the ground is blanketed in a pristine, icy layer..."
    "You press on, the crunch of your boots on the snow is the only sound breaking the stillness."
    with vpunch
    "As you venture deeper into the forest, a sudden rustling in the underbrush catches your attention."
    e "W-who's there?"
    "Your senses heighten as you scan the surroundings, your hand instinctively reaching for your weapon."
    show herd_normal with dissolve
    "From between the trees, someone stumbles into your view. His breath came in ragged gasps, and his clothing ripped."

    "It was an elk, the white fur shawl draped over his shoulders, his arctic blue pupils glisten as your eyes meet."
    "His gaze is locked with yours, desperation in his eyes."
    "Moments later, a group of armed guards burst into the clearing, their tribal markings distinct on their armor."
    "His cheeks turn white, just like his fur. Fear etched across his face as he glances back over his shoulder."
    "For a few seconds, you wait for the man to speak, but instead he remains silent."
    e "C-can I help you?"
    "He doesn't respond, but instead hold your hand in between his cold palms. His eyes are pleading, but you do not know how to help him."
    "You hesitate, nodding nervously, torn between the instinct to help and the wariness of getting involved in a situation you didn't fully understand."
    "The stranger nudges at your hand before releasing it, and he turns and bolts down the small hill behind you."
    hide herd_normal with dissolve
    bearGuard2 "He can't be far, where did that damn deer go?"
    bearGuard "You there, did you see the man with a hood there?"
    "The guards quickly catches up and turns to you, their expressions demanding answers."
    "It's only when they get closer, that you can peek under their helmet, along with their clothing lined with thick fur."
    "The bear guards are out of breath and disoriented, their breath forming clouds in the frigid air."
    e "W-who are you? And who is the man you're looking for?"
    "His eyes narrowing as he sizes you up, while the other guard looks all around for the fugitive."
    bearGuard2 "Stay out of this, stranger! This is none of your concern."
    "You stare at the guard's hand, he is holding a long harpoon, one that would have been lethal..."
    menu:
        bearGuard "Quit wasting our time, where is the man? I know he ran this way."
        "Into the forest":
            jump Otsovaara_Introduction_Mislead
        "Down the hill":

            jump Otsovaara_Introduction_Chase

label Otsovaara_Introduction_Mislead:

    $ bearGuard_mislead = True
    e "I saw him heading there."
    "You point towards the wrong direction, fully understanding that you're leading them to a false trail."
    bearGuard "Good."
    "They head off towards the direction you pointed, their footsteps crunching through the snow as they tread deep into the taiga forest."
    "In the distance, the hooded man takes advantage of the diversion and continues his frantic escape, you watch as he nods to you, and runs away behind the guard's back."
    "Soon, he disappears among the tall pines and snowdrifts, leaving no trace of his whereabouts."
    "Once more, you stand alone in the quiet taiga, the snow-covered landscape enveloping you in solitude."
    "You shake your head, perhaps it's an everyday occurence to the unforgiving snow around here, but just as the guard says, you might as well stay out of this matter."
    "Suddenly, the quiet is broken by the sound of approaching footsteps."
    with vpunch
    "When you turn back, you're greeted by another guard, his armor adorned with intricate tribal markings, this time without a makeshift helmet."
    show daggi normal with dissolve
    "His fur is white, a youthful expression across his face as he arrives alone."
    bearCommander "E-excuse me, Sir, please stay, at least until we're finished."
    "You wait for another question from the guards, instead the only thing you hear is the clear yet deep note as he raises the horn to his lips and blows softly."
    "You can feel the whole forest vibrating, resonating through the whole snow-covered ground. The call to action has probably alerted the rest of the guards as you see them quickly abandoning the chase."
    "Another loud horn reverberates, at the same time the guards have made their way towards the white bear guard."
    show daggi normal at r1 with move
    "Soon, you're surrounded by the same guards chasing after the hooded man mere minute ago."
    pause 1

    bearGuard "You! You knowingly led us astray! We could have caught him right there."
    "One of the bears approaches you with a stern expression, pointing his harpoon at you with his accusation."
    bearCommander "Calm down-"
    bearGuard2 "How! Did Herd conspire with you together?"
    "You raise both your hands defensively, they hang heavy in the frigid air, your heart is pounding so quickly as the tip of the harpoon is mere inches apart from your chest."
    "The rest of the guard falls silent, even the white bear is waiting anxiously for your response."
    menu:
        "Admit your deception":
            $ bearGuard_admit = True
            e "I-I did, he looked scared of you guys, and I don't even know anyone here."
            bearGuard "W-what? Can you even fathom the consequences of your actions? Do you even know who you're talking to?"
            "You cannot fathom, probably because you have probably not ever heard about that name before, but, it's merely a thought you don't dare to speak out loud."
            "The guards' faces are darkened with anger, you can feel the tip of the harpoon pokes into the fur on your chest, in the brink of puncturing your thin skin."
            bearGuard2 "Commander, we should capture him. Chief Kaurhu needs to know what happened here."
            "The commander nods and steps forward, his demeanor remaining composed, much different from the other guards' fury."
            bearCommander "Needless to say, stranger. Your actions have hindered our mission."
            "He turns to you, his tone is stern and soothing, you wouldn't ever imagine that voice coming from a bear, but honestly, you've never seen a bear up close before, to your knowledge."
            bearCommander "But I don't see why you would admit anything if you're truly guilty."
            e "Yes, I really have no idea he's a bad person, I just got here and I don't know anything..."
            bearCommander "Where are you heading?"
            e "I'm not sure, I was just traveling around."
            bearCommander "An adventurer...? Well, we appreciate your intention, you should continue o-"
            bearGuard "Commander, don't you think, Chief would like to see this man and make his own judgement?"
            "An old guard from behind cuts off the white bear, the guards exchange glances, nodding all at the same time."
            "His expression comes off as a shocked face, but not very surprised. If it was your elder back in your land he'd never once let the follower disrespect him like that."
        "Deny your intention":

            $ bearGuard_admit = False
            e "No! I didn't know where he's headed. I must have mistaken that, but I didn't know."
            bearGuard "You think you're fooling us? You think you can just lie to our faces and get away with it?"
            "The first guard's face reddens with anger, and his fists clench at your response and you can feel the harpoon begins to pierce through your skin."
            "The rest of the guards, equally infuriated, close in around you. They exchange heated whispers and stern glances, clearly debating their course of action."
            "You're not sure what happened to lead you to this point, how come this brief encounter has turned into something that could've taken your life right here."
            bearCommander "What's the odd that he's truly innocent, would you all rather attribute wrongdoings to malice than pure ignorance?"
            bearGuard "Commander, we can all tell he's lying, he must be with Herd."
            bearCommander "What can Herd offer him, a stranger, that he would risk his life for?"
            bearCommander "Even if he's lying, it could've been because he's scared of you all, isn't that right?"
            "He turns to you with a faint smile, you're not sure why he would do that as a commander of the tribe you've never met, but at least the guard's animosity has simmered down."
            bearGuard "Well, commander, don't you think, if we're not sure which is which. Then maybe it's best we let chief decide instead?"
            bearGuard2 "Chief should be informed about him at least, we should lock him up before Chief gives any judgement."
            "The white bear nods, his expression is calm, but you can see hesitation in his eyes."

    bearCommander "I-I understand, well. Stranger, would you like to come with us for a brief discussion, as a witness?"
    e "U-uh..."
    "Before the commander finishes his sentence, the guards have already working on cuffing your hands, and honestly, you're starting to think they intent to convict you on the spot if not for the commander."
    bearCommander "Please uncuff our guest, we wouldn't want him to get hurt before Kaurhu's judgement."
    "You notice the guards have grown much more impatient, but they comply quickly."
    bearGuard "Follow us closely, stranger. If I see you wander off anywhere, I won't hesitate to pierce you with my harpoon."
    "You're not sure if he's being suggestive or literal, probably latter. But there's no way you can escape from this situation anyway."
    scene frostedtaiga with fade
    show daggi normal at c1
    "The guards lead you through the snow-covered wilderness, as the supposedly commander follows from behind you."
    bearCommander "Traveller, what's your name?"
    e "[e]."
    "He taps your shoulder, signaling for you to walk beside him, which attracts some glances from the guards in the front."
    d "My name's Daggi, the commander of the bear tribe."
    d "The elk man you just saw, Herd, we tried to track him down, but he kept running away from us. We are afraid he might be planning something against our tribe."
    e "Why are you telling me this now?"
    d "I don't believe you're involved with Herd personally, therefore, I want you to prepare when you meet our chief, [e]."
    "You nod respectfully, and Commander Daggi nods back, he slowly walks up to the front as you follow the guards."
    "After some time, the thick taiga giving way to a well-trodden path that winds its way down into a snow-filled valley."
    scene otsovaara01 with dissolve
    "The tall pine trees gradually thin out, replaced by the sprawling landscape of the village around, and below."
    "Already you hear loud clanking sounds, some wooden wheels are spinning by themselves, with carts full of goods sprawling around the village."
    "You walk up, and talk to one of the guards."
    e "Hey, is this the bear tribe?"
    "You'd expect a nod at least, but he doesn't respond, not even giving you a worthy glance. So you quickly returns to the back, and let the guards lead you away."
    "With a begrudging wave from the commander, the guards escort you back toward their village, their frosty silence punctuated only by the loudness of the village itself."
    "The roof of their houses are covered in thick snow, and you're soon led up a flight of snowy stairs, leading to a bridge that stands over a deep icy chasm."
    scene otsovaara_station with dissolve
    "The Chief's Hall awaits on the other side of the bridge, a formidable structure just like the others, albeit much more grandiose."
    "Daggi gestures for you to follow him, and you walk across the bridge, the icy wind biting at your fur."

    scene otsovaara_throne with dissolve
    "Inside the council, you hear a few coughing sound from within the settlement. A chair surrounded by advisors and elders, chattering amongst themselves."

    pause 0.5 

    "As you enter, the room suddenly falls silent, the weight of their collective gaze falls upon you and the guards."
    d "Chief! Are you alright?"
    show daggi normal at l1 with dissolve
    "A voice calls for the chief as you see the commander runs up in front of the throne."
    "On the throne sits an old brown bear, one whose wrinkles etch deep into his weathered face. He coughs once more, drawing the attention of the young commander."
    show kaurhu normal at r1 with dissolve
    "His beard, a cascade of icy white, messily hangs around the brownish stubbles."
    bearChief "I'm fine, you little snowball."
    "The brown bear clears his throat, then glances at the guards in front of you briefly."
    bearChief "What's the matter? Where's that sack of shit, shouldn't he be rotting in my prison ten minutes ago?"
    bearGuard "C-chief Kaurhu, we couldn't catch him yet, but we found one of his accomplices."
    "Your eyes widen as the bear guard beside you points his finger, both bears on the throne furrow their brows on this accusation."
    e "I-I don't know anything about Herd! This is my first time being here."
    bearGuard "We caught him trying to distract us from catching Herd, he helped him to escape."
    "The elders around the chief look at one another, then they scatter and walk away, revealing the old chief slumped against the throne, raising his brows."
    kh "Explain yourself."
    e "Uh, I have never been here, or seen you guys. I was walking by and I saw the guards chasing after someone."
    "The chief listens intently, his gaze almost unrelenting as he absorbs your words."
    if bearGuard_admit:
        e "I wanted to save that poor guy, so I... might have led the guards somewhere else so that man can escape."
        e "But I don't know anything!"
    else:
        e "I didn't see him too clearly, so when they asked me I might have pointed to the wrong direction."
    d "We still don't know what Herd was doing yesterday. We need to find him first!"
    "The commander exclaims, his words assured."
    bearGuard "Then we should lock this strange face down there right now, so the rest of us can focus on trailing him."
    d "No, he's not involved, and we need to find out what happened yesterday first. We can't just lock him up without any evidence."
    bearGuard "He's a stranger, and he's lying to us. We can't just let him go like that, we need to lock him up right now-"
    with vpunch
    kh "Enough!"
    show kaurhu normal at c1 with move
    pause .3
    show daggi normal:
        linear 0.5 xalign -0.2

    "The chief bellows, his patience has worn thin, slamming his hand down on the side of the throne."
    kh "Instead of arguing non-stop in front of my throne, how about focus on the task at hand, I need that sack of shit caught right now."
    "He glances around the hall, and addresses the guards, and everyone else, it's clear he's trying to keep his composure over his wrath."
    kh "And before we find out what he intended yesterday, don't you ever try to spread meaningless rumors around my tribe."
    kh "Or I will have your head on the plate before you all ever know it, understand?"
    "The room becomes silent once more."
    kh "You are dismissed."
    "The guards nod, they bedgrudgingly exchange reluctant glances before turning back and leave the room."
    d "Thank you, chief."
    show daggi normal at l1 with dissolve
    show kaurhu normal at r1 with dissolve
    kh "Commander Daggi, the guards, they're yours now. I expect a better discipline and unity among your men. Use what you were taught."
    kh "Don't make me worry about you again."
    "The chief coughs loudly, before turning to you with a rougher voice."
    kh "You, what's your name?"
    e "My name is [e], chief. I'm a courier from Lusterfield."
    kh "Oh, a courier, got any letters for me?"
    e "N-no... I was just travelling by."
    "Kaurhu shakes his head."
    kh "[e], go about your own business back south. We have enough troubles to deal with, I don't need another fly buzzing around my ears."
    kh "And I'll be honest, don't ever talk to our folks about what happened today. Or I will send you to the prison myself."
    kh "Am I clear?"
    "You nod."
    kh "Commander, escort [e] out of our tribe, quietly. We won't be accepting any more visitors."
    d "Yes, chief."
    "Commander Daggi stands behind you, and gestures to lead you the way."
    d "This way, [e]."

    jump Otsovaara_Introduction_Aftermath

label Otsovaara_Introduction_Chase:

    $ bearGuard_mislead = False
    "You point toward the small hill behind you, fully understanding that you're aiding the guards in their pursuit."
    e "He... he went down there."
    "The first guard nods approvingly, his intimidating demeanor softening just slightly."
    bearGuard "Good."
    "He grumbles, and the guards follow your indicated path, moving down by each step."
    bearGuard "Right there..."
    "You watch them descend a small hill, their footsteps muffled by the thick snow, but they are careless with the way they talk, supposedly that much noise is going to startle whoever hiding around here."
    bearGuard "I see h-"
    "In an instant, the hooded man jolts away from behind a tree, the guards instantly shout, calling out for him."
    bearGuard "Hey! Stop right there!"
    bearGuard2 "Herd, you can't run away forever."
    "Seeing that the man is about to escape, the guards grips onto his weapon tightly, closing one eye as he aims for the man."
    e "No!"
    with vpunch

    scene frostedtaiga with fade
    "Just as it seems he is disappearing from your sight, a harpoon zooms through the frigid air, piercing through the escapee's shoulder."
    with vpunch
    "You hear a loud yelp as the man cries in pain, but he continues on staggering, leaving behind a blood trail on the white snow."
    e "Oh no..."
    "The guards quickly give chase, their heavy boots crunching through the snow."
    "Despite the injury, the man manages to put some distance between himself and the guards, heavy breaths echoes as the guards keep on chasing."
    "You cautiously follow the guards, there is no way you can leave this place without knowing what happened to the man."

    bearGuard2 "S-shit."
    "You notice the blood trail seem to be much thicker by the time, it's not a good sign..."
    "A long horn can be heard from a distance before you finally catches up to the two guards."
    "After the chase, the two bears in front of you finally stops, but you sense something, eerie about them."
    "You stare at their backs, head droops down, seemingly focused on something ahead."
    "The shouts turn into complete silence, it is almost jarring, knowing that they just sent a harpoon flying a few minutes ago."
    "Out of curiosity, you approach, as you peek from behind the bear..."
    "Lied on the snow, the man you just saw, is now soaked in a pood of blood."
    "The harpoon seem to puncture deep from behind his back, it could almost come out from the other side."
    "His eyes are barely opened, but they never close again. The lack of breath tells you that he is already gone."
    e "Is he dead?"
    bearGuard "We just arrived..."
    bearGuard "Shit, I told you to take it steady, the architect is not built for this!"
    bearGuard2 "I- I didn't mean to, I aimed at his arms, we had to stop him no matter what."
    bearGuard2 "How could I know that's going to kill him... he seemed fine."
    e "D-did I just kill him...?"
    "You stutter in pure sorrow, you can't even comprehend being the cause of someone's death, because you told the truth."
    "Afterall, you were just wandering about, how could you expect that five minutes later, someone is killed in front of your eyes?"
    "You kneel on the ground, trying to get a sense of his heartbeat, even as the blood begins to soak through your fur."
    "The bear guards stare at you, they exchange glances before lending a hand."
    bearGuard "You won't be blamed for any of this, traveller."
    "He takes a deep breath."
    bearGuard "He is already gone."
    bearGuard2 "How do we tell chief?"
    bearCommander "W-what's going on? Whose blood was that-"
    "When you turn back, you're greeted by another guard, his armor adorned with intricate tribal markings, this time without a makeshift helmet."
    show daggi normal with dissolve
    "His fur is white, a youthful expression across his face as he arrives alone."
    bearCommander "H-Herd!"
    "He gasps, his eyes widens as he notices the limp body floating on the pool of blood."
    "The two guards turn their head in unison, their expressions are grim, but they remain silent."
    bearCommander "W-what happened? How did he die?"
    bearGuard2 "We were chasing him, he was running away, so I tried to stop him."
    bearGuard2 "I did not know that could kill him, I swear."
    bearCommander "No, no, no, no..."
    "The commander paces around, his eyes are wide, his hands are shaking as he tries to comprehend the situation."
    bearCommander "How could this happen? He wasn't supposed to die..."
    bearGuard "Keep calm, we will report to Chief directly."
    "The white bear glances at you for a few times before noticing you."
    "He composes himself quickly from the shock, and turns to you with a stern expression."
    bearCommander "Excuse me, Sir. Are you involved in this matter?"
    e "Uh..."
    bearGuard "He's a traveller, he was just here when we were chasing Herd."
    bearCommander "I see... Okay. You may need to follow us to see Chief Kaurhu, it will take only a while."
    e "C-come with you? I have no idea who you people are, I just got here."
    bearCommander "Our chief would like to know what happened here, please, follow me."
    "You hear a clear yet deep note as he raises the horn to his lips and blows softly."
    "You can feel the whole forest vibrating, resonating through the whole snow-covered ground. You can already sense more guards are coming."
    bearCommander "You two, stay with Herd until the rest arrive, I will take the stranger to Chief Kaurhu."
    "The two guards standing by you, exchange glances in silence, before they turn back to the commander."
    bearGuard "Yes, commander."
    "The white bear nods, and he turns to you, gesturing for you to follow him."

    "He leads you through the snow-covered wilderness, as you show some form of discomfort."
    bearCommander "Hey, what's your name?"
    e "[e]."
    "He taps your shoulder, signaling for you to walk beside him."
    d "My name's Daggi, the commander of the bear tribe."
    e "Shouldn't we be walking along with the other guards?"
    d "No, the guards are scared of Chief right now. and I am their commander, so it should be me who break the news first."
    "You nod, and follow the white bear as he leads you through the forest."
    d "The hooded man you just saw, his name was Herd."
    d "I... well... I'm not sure how to explain this, but all you needed to know was we needed to talk to him."
    e "Was he bad?"
    d "No! No... he was our architect. He designed most of the mechanical structures in our tribe, made sure they won't collapse and all."
    d "But, ever since the avalanche..."
    "Commander Daggi ponders for a moment, his expression darkening as he recalls the events of the past few days."
    d "He just didn't deserve to be killed, and I believed he was merely lost in the moment."
    e "I'm sorry."
    "You turn to the white bear, who stares forward blankly."

    d "M-maybe we should keep going."
    "After some time, the thick taiga giving way to a well-trodden path that winds its way down into a snow-filled valley."
    scene otsovaara01 with dissolve
    "The tall pine trees gradually thin out, replaced by the sprawling landscape of the village around, and below."
    "Already you hear loud clanking sounds, some wooden wheels are spinning by themselves, with carts full of goods sprawling around the village."
    "With a begrudging wave from the commander, the guards escort you back toward their village, their frosty silence punctuated only by the loudness of the village itself."
    d "This is our small town, please make yourself at home, we won't bite, or maul."
    e "I don't doubt that."
    d "The Chief is downstairs. Please follow me."
    "The roof of their houses are covered in thick snow, and you're soon led up a flight of snowy stairs, leading to a bridge that stands over the icy chasm."

    scene otsovaara02 with dissolve
    "The Chief's Hall awaits on the other side of the bridge, a formidable structure just like the others, albeit much more grandiose."
    "Daggi gestures for you to follow him, and you walk across the bridge, the icy wind biting at your fur."
    d "I will explain the situation very briefly to the Chief, you just need to follow my lead, [e]."
    e "Alright, I suppose it will be quick and easy?"
    d "Depends on who you ask, but I'll try to make it as painless as possible."
    scene otsovaara_throne with dissolve
    "Inside the council, you hear a few coughing sound from within the settlement. A chair surrounded by advisors and elders discussing, some carrying towels."
    "As you enter, the room suddenly falls silent, the weight of their collective gaze upon you and the guards."
    d "Chief, I'm back."
    show daggi normal at l1 with dissolve
    "A voice calls for the chief as you see the commander runs up in front of the throne."
    "On the throne sits an old brown bear, one whose wrinkles etch deep into his weathered face. He coughs once more, drawing the attention of the young commander."
    bearChief "Great."
    show kaurhu normal at r1 with dissolve
    "His beard, a cascade of icy white, messily hangs around the brownish stubbles."
    "The brown bear looks around, seemingly searching for someone other than you and the commander."
    bearChief "Where is the rest of the guards? Did you catch Herd?"
    "The brown bear clears his throat, then glances at the commander briefly."
    d "Chief Kaurhu..."
    "The commander averts his gaze, his expression darkening as he tries to find a word to explain."
    kh "What's the matter? Where's that sack of shit, shouldn't he be rotting in my prison ten minutes ago?"
    d "Herd is dead."
    kh "What?"
    d "They are taking Herd's body back here."
    kh "H-how?"
    d "H-he tried to run, I mean, Gren and Illoch were losing him, a-and we accidentally..."
    d "...killed him."
    d "This stranger was there too, he can attest for my claim, Chief Kaurhu."
    e "Uhm..."
    "Daggi takes a deep breath as the entire room turn their attention to you."
    "The elders around the chief look at one another, then they scatter and walk away, revealing the old chief slumped against the throne, raising his brows."
    kh "Explain yourself."

    "The chief slouches over, his eyes are fixed on you, waiting for your response."

    e "Yes, the commander is correct, Chief."
    kh "Where are you from, traveller?"
    e "I'm from Lusterfield, Chief. I was just passing by when I saw the guards chasing after someone."
    kh "What else did you see?"
    e "The guards saw him running further down the hill, and one of them hurls a harpoon towards his direction."
    e "He was running at the time, but when I arrived, Herd was already lying on the snow, on top of a pool of blood, he probably bled out."
    kh "Ugh..."
    "The chief sighs as he straightens his body."
    kh "Poor bastard, he lost his family and lost himself."
    d "Illoch and the others are bringing him back now. I am sorry, Chief."
    kh "No, no. You're doing fine, commander. I'm not blaming you for this."
    d "It was just an accident, Chief. Please, do not blame it on the guards too."
    kh "How many accidents do we need to make before we learn, Daggi?"
    kh "I'm not blaming you, but I need you to understand the weight of one's actions, we're talking about Herd who we lost here."
    "The chief coughs loudly, before turning to you with a rougher voice."
    kh "You, what's your name?"
    e "My name is [e], chief. I'm a courier from Lusterfield."
    kh "Oh, a courier, got any letters for me?"
    e "N-no... I was just travelling by."
    "Kaurhu shakes his head."
    kh "Great."
    "As he clears his throats, you can hear the footsteps of the guards outside."
    kh "Commander, escort [e] out of our tribe, quietly. I'll need some time to talk with your folks."
    kh "We'll talk about this later."
    d "Yes, chief."
    "Commander Daggi stands behind you, and gestures to lead you the way."
    d "This way, [e]."

    jump Otsovaara_Introduction_Aftermath

label Otsovaara_Introduction_Aftermath:
    scene black with dissolve
    pause 1 
    scene otsovaara02 with dissolve
    show daggi normal
    if bearGuard_mislead:
        $ herd_dead = False
        "As you are escorted out of the Council Hall by the commander, you can't help but notice the simmering tension that still lingers among the guards outside."
        bearGuard "Filthy outsider."
        "The guard standing nearby taunts, crossing their arms, they're clearly disturbed with the chief letting you go scot-free."
        d "Show some respect to our guest, Chief has made his mind, or do you want to change that?"
        "He rolls his eyes, returning to exchange series of murmurs you can barely faintly hear."
        "You follow the commander idly, who's leading the way out."
        scene otsovaara_station with dissolve
        show daggi normal
        d "Sorry for their behaviour, they can be hot-headed, sometimes."
        e "And thanks for helping me, I'd not know what to do if you weren't there."
        d "That's the least I can do."
        "He glances at you sincerely."
        e "You still hadn't answered me, who is Herd?"
        d "He was the former architect of the tribe, he designed and helped construct most mechanical structures in our tribe."
        d "The wheels, the rails, he took up the difficult job to make use of our abundant resources. We were thankful of him at the time."
        e "Then, why are you trying to catch him now?"
        call Daggi_Asking_About_Herd from _call_Daggi_Asking_About_Herd_1
        d "Did the answer satisfy you?"
        e "You answered more than I expected, truly. You know you're escorting me out of this land, right?"
        e "Are you expecting me to come back?"
        "The white bear smiles, but he remains silent."
        d "That's your choice to make, [e]. I'm sure Chief Kaurhu won't bite your head off if you ever come back."
        "You try to justify Daggi's intention, there is no way a commander's treating a stranger this well, without any reason."
        "Unless perhaps, he's trying to use someone to tame his guards. You try to go along with suspicion, but his affectionate smile has already melted your heart."
        e "Thanks, Commander Daggi."
        scene frostedtaiga with dissolve
        show daggi normal
        "He pauses as you two have reached the forest where Herd was last seen. Some guards from distant are still looking for the man."
        d "I will be around the forest until Herd is caught. Before that, if you want to come, stay with me and don't get yourself caught by the guards first."
        "You nod."
        d "See you around, then."
    else:
        $ herd_dead = True
        "As you are escorted out of the Council Hall by the commander, you take notice of the guards outside, along with a sack the size of a normal bear."
        "The guards are still discussing among themselves, they glance at you and the commander, before entering the hall."
        scene otsovaara_station with dissolve
        show daggi normal
        d "Sorry for the troubles you've been through, [e]."
        e "It's fine, I guess I didn't expect this to be my first-time experience with the bear tribe."
        "You chuckle, but the commander remains silent."
        d "I hope you forgive us for the trouble, we're not usually like this. Everyone has been on edge ever since the avalanche."
        e "What happened in the avalanche?"
        call Daggi_Asking_About_Herd from _call_Daggi_Asking_About_Herd
        d "Oh, uhm, I didn't mean to dump this all onto you, [e]."
        e "It's fine, but it did make me feel a little worse knowing this... Herd."
        "The commander takes a deep breath, then turns to you."

        d "When the dust settles, I hope to see you visit us again, perhaps I can be your guide around the tribe, as my personal apology."
        e "Are you sure? I don't want to be a burden to the Commander of the tribe."
        d "I insist, it's the least I can do for my guest."
        "You try to justify Daggi's intention, there is no way a commander's treating a stranger this well, without any reason."
        "But staring at his sincere eyes, you can't help but to trust the valiant commander."
        scene frostedtaiga with dissolve
        show daggi normal
        d "The guards will be patrolling the area around here, try not to get caught by them."
        d "I hope to see you around, [e]."
        "You nod."
        e "Thanks, Commander Daggi."

    jump main_frosted_taiga

label Daggi_Asking_About_Herd:

    "Daggi goes still for a moment, the set of his shoulders tightening as he gathers the words."
    d "There was a snowfall from the mountain not long ago. It became an avalanche before anyone could answer it properly."
    d "We lost many people that day."
    e "I'm sorry for your tribe's loss."
    d "Herd's house was buried. When we found it, his family was still inside."
    d "He was there too, kneeling in the snow and staring at the wreck as if he could still force it to come undone by looking at it long enough."
    d "I do not think any of us knew what to say to him after that."
    d "The avalanche injured him as well. His hearing was badly damaged. Afterward, he could not hear us, and he would barely look at us long enough to try."
    d "He stopped eating properly. Stopped sleeping. He would not speak, and when anyone approached him, he looked as if he was bracing for another wall of snow."
    "Daggi exhales slowly, not quite looking at you."
    d "We tried to make room for him. That sounds pitiful when I say it aloud, but we did try."
    d "In the end he returned to what was left of the house, and after that he would hardly communicate with anyone at all."
    e "That came out of nowhere."
    d "I think he blamed us, at least in part. Maybe for the avalanche. Maybe for surviving it badly. Maybe for failing to reach him after."
    d "I cannot say he was wrong to grieve. He lost his whole family, and then most of the world went silent on him."
    d "The Herd I knew before that was patient, reassuring, and wiser than most of the tribe gave him credit for."
    d "He advised Chief Kaurhu often. He built half the things in this settlement that still stand straight in winter."
    d "After the avalanche, he was not the same. He kept to himself. Sat near the furnace through the night. Watched everyone as if waiting for something worse."
    d "Then yesterday he got into the council hall somehow. Chief Kaurhu caught him near his room before anyone understood how far he had already made it."
    e "Did he try to do anything?"
    d "Not that I saw. That is part of what made it worse."
    d "We could not question him properly. We could not calm him. We cornered him because we did not know what else to do, and he escaped anyway."
    d "Even now I am still not sure how he got out of the council hall with guards at every door."
    d "After that, one of the patrols saw him trying to flee the tribe, so they gave chase into the forest."
    d "And you already know what happened next."
    pause 2
    return


label Kaurhu_Dialogue:
    scene otsovaara_throne with fade
    hide screen menu_buttons
    show kaurhu normal with dissolve

    "As you walk up to the throne. The brown bear catches you in his peripherals, but only notices your presences after a few blinks."
    if kaurhu_tut == 1:
        $ kaurhu_tut += 1
        kh "Oh, great, the courier is back. I thought I told you we are not accepting any visitors."
        e "I-I'm sorry, Chief Kaurhu, I think Commander Daggi didn't mind that."
        kh "I don't care what Daggi said, I'm the chief here, and I say we're not accepting any visitors."
        e "Sorry, I will leave right away."
        kh "Good..."
        pause 1.0
        "The chief furrows his brows as you turn back."
        kh "Is a proper courier supposed to be this spinelessly subservient?"
        e "Huh? I-I'm sorry, Chief Kaurhu."
        kh "I will make an exception this time, but only because you're a courier and Daggi vouched for you."
        kh "You can come back if you have any letters for me, but don't step in this place if you have nothing."
        e "I understand, Chief Kaurhu."
        kh "Now, leave."
        "You nod, and quickly leave the hall."
        jump main_otsovaara_station
    kh "It's you again, Courier, got any letters for me?"
    e "N-no..."
    "The bear chief sighs, slightly raising the edge of his lips, as if he's been expecting it."
    kh "Then you better speak up, [e]. I don't have all day."
    jump Kaurhu_Normal_Talk

label Kaurhu_Normal_Talk:
    $ cave_state = bearguard_dialogues.get("Chilly Ice Cave", {})
    menu:
        kh "What is it that you have to say?"
        "Report about the noise in the cave" if quest47.status == 2:
            jump Bear_Guard_Report_To_Chief
        "Head to the cave with Daggi and others" if quest47.status == 3:
            jump Bear_Guard_Report_To_Chief_Continue
        "Ask about the tribe's relationship with the other villages":
            e "What's the relationship between your tribe and the other villages? We haven't heard much about the bears around here."
            kh "I take pride in not relying on anyone else."
            kh "I have my own resources, my own people, and my own land. I don't need anyone else to tell me what to do."
            e "I see."
            kh "I can see you pulling down your brows, got any problems with that?"
            e "No, no, I was just surprised. Don't you have outside friends... or allies?"
            kh "Look, the only reason you aren't denied entry like everyone else is because you are a courier, who passes me letters, now do that job and stop pestering me about stupid questions."
            e "I-I'm sorry, Chief Kaurhu, I didn't mean it like that."
            kh "I accept your apology."
            "He grumbles, then turns back to the throne."
            kh "You are not the first one to ask me that, and you won't be the last."
            e "Well, I'm sorry for asking."
            kh "The fact is, they either are too far away, or never got used to the weather."
            kh "That is why I never bothered talking with some annoying sullen sorts and what not. We have enough to worry about."
        "Ask about the rumors of his retirement" if bearGuard_retirement:
            e "I heard rumors about your retirement, Chief Kaurhu. Is that true?"
            kh "Retirement? Who told you that?"
            e "I-I heard it from the guards, they said you were planning to retire, but that avalanche got in the way."
            kh "The guards, huh? They're always talking about something they don't understand."
            kh "I'm not abdicating. I'm not going anywhere, I'm staying here, and I'm not going to let anyone else take my place."
            e "Not even your son?"
            kh "Daggi? He's not ready to take my place. I love him, and all, but he's not born to lead the tribe."
            e "That was surprising, do you not trust your own son?"
            kh "I trust him when he's playing wooden blocks in my room, not when he's leading the bears who had no trust in him."
            kh "I know my son better than anyone else, he is not ready to be a leader, not yet, at least."
            kh "The fact is, as soon as he's sitting on my throne, the outsider boars are going to eat my tribe alive."
            kh "I'll stay here until he's ready, but I can't see that happening anytime soon."
        "Ask about the avalanche":
            e "Daggi told me about the avalanche, Chief Kaurhu. What happened on that day?"
            kh "I thought Commander had already told you what I had to say."
            e "Uh, he did, but I want to hear it from you, Chief. If that is fine."
            kh "Look, I don't need you spreading around the news outside, that gives me more headaches than you being here."
            e "Of course not, Chief. I'm just curious about what happened."
            kh "Fine. What do you want to know?"
            e "How did the avalanche happen?"
            kh "Because there were a snowstorm earlier, the snow was piling up on the mountain ranges, and then it came crashing down."
            e "Was it common in the snow region?"
            kh "No, not at all. My people have always prepared for snowslides. They've been living here for generations, they know how to handle it."
            kh "But the day it happened, there were some, unusual circumstances in the tribe. The guards responsible were somehow caught... off guard."
            e "The guards?"
            kh "There are signs of avalanche where you can predict such things hours before it happens. But on the day it happened, the guards were distracted."
            kh "And then, the snow came crashing down."
            e "So, you're saying they are responsible for the avalanche?"
            kh "No, not all of them. Commander Bedwyr, he was the one who was supposed to be on duty that day, he failed the tribe when it matters the most."
            e "What happened to him?"
            kh "I sent him to the prison. He's been there ever since, and he's not coming out any time soon."
            e "Isn't that a bit too harsh, Chief? I don't think he was solely responsible for the tragedy."
            kh "I don't care what you think, courier. My people died because of his incompetence, someone had to pay for this."
            e "Okay."
            kh "Yeah, I'm done talking about this."
        "Ask about the bear tribe":
            e "Chief Kaurhu, can you tell me more about the bear tribe?"
            kh "You need to be more specific, courier. I have a tribe to rule."
            e "O-okay, what about the bear tribe's history?"
            kh "Well, you see. The bear tribe, or in my people's tongue - Otsovaara, has been around since before the ancient times."
            kh "We are the descendants of the great snow bear, Ookko. That's why we're the only few who can survive in this cold."
            e "What about the other tribe in the snow region? I saw them on the map."
            kh "The boars? They're a bunch of thick-furred pigs who think they can take over my land. Just nothing but savages who can't even handle a snowstorm like a true bear."
            e "Uhm... What was the history between you two?"
            "Kaurhu chuckles, his eyes gleaming with pride as he recounts the tale of his ancestors."
            kh "There were a time when the bears and the boars shared the land, but they were too greedy, they wanted more than what they already have."
            kh "Long story short, an ancient war broke out, and the conqueror, my ancestor, Stigandr sacrificed himself, and led the bears to victory."
            kh "Ever since his death, the region has been under the protection of his spirit, there were no snowstorms, or avalanche, and the boars have never dared to step foot on our land again."
            e "Was the warrior really that powerful?"
            kh "Not sure, it was an old story from my ancestors, I don't believe in gods or spirit, I believe in my people, and my tribe."
            e "If he's still blessing the tribe, then why did he let the avalanche happen?"
            "The chief's eyes narrow, his expression darkening as he tries to comprehend your question. It doesn't even seem like he's ever pondered about it."
            kh "Don't you dare question my ancestor, courier. The avalanche happened because of the incompetence of my guards, not because of some superficial blessing."
            "He growls, the white fur on his neck bristling as he glares at you. Even though he just said he doesn't believe in spirits, the mention of his ancestor seems to have struck a nerve."
            kh "And I don't want to hear any more of this nonsense, courier."
        "Ask about Herd the architect":

            if quest47.status == True and herd_dead:
                e "Chief Kaurhu, after what we found in the crypt... do you still think Herd went there to sabotage the tribe?"
                kh "No."
                kh "Not that simply."
                e "So the noises in the cave had nothing to do with Herd coming back?"
                kh "No."
                kh "And I do not intend to let the tribe tell itself that story."
                e "Does that change anything for you?"
                kh "Not in any way that helps him."
            elif quest47.status == True and (not cave_state.get("Returned Herd Lost Item", False) or cave_state.get("Daggi Found Herd", False)):
                e "Chief Kaurhu, do you still think Herd went to that cave just to hide?"
                kh "No."
                kh "He had a reason to be there."
                e "And the noises?"
                kh "Enough to rattle the guards. That is all that matters now."
            else:
                e "Chief Kaurhu, can you tell me more about Herd?"
                kh "That sack of shit? What's the matter?"
                if herd_dead:
                    e "I wanted to know more about what happened before he... got caught in this matter."
                else:
                    e "I wanted to know more about why you guys wanted to catch him."
                kh "Well, with everything in mind, he was a good, trusted counsel. Had some great thoughts about the frameworks about expanding the tribe into the icy chasm beneath us."
                kh "I heralded the idea, of course. but Herd was a hustler. His parents were great builders, traditional ones, but he had something different in his mind."
                kh "You can say he's dedicated, while he's working, they said someone could sneak up and stab him and he won't notice a thing."
                e "You speak very fondly of Herd, I thought you hated him, judging by how you called him, sack of shit."
                kh "What can I say, I'm just a charitable person. As much as a sack of shit he became, credits are where credits due."
                kh "After his parents retired, he was the one who helped build most of the newer shacks. They were warmer, safer, and helped my tribe make it through the long winter."
                kh "Then, he designed the great furnace, something that burns well for the whole tribe and makes smelting metals, grinding grains, woodworking a little easier."
                kh "My people were in the process of building a pipe system underneath the ground, Herd had his whole life dedicated into it."
                kh "I approved him and his family to move outside just so he can oversee the project more clearly."
                e "He moved out of the tribe?"
                kh "He proposed to build the network down the icy chasm, it made sense. but the network of pipe have to be built on the other side, somewhere with a lot of space."
                e "Do you think his family could have survived if he didn't move out?"
                kh "How would I know? He was the one who wanted to move out, I didn't force him to do anything. The tribe was destroyed as much as his new house was, our people were buried in snow."
                kh "It's lucky that he survived, but he left the team that day. Apparently, that old brown-snout had his ears stuffed or something."
                kh "Couldn't hear, couldn't talk, my tribe's healer had him checked everywhere. But they found nothing."
                e "So, why did you want to catch the architect?"
                kh "He broke the pipes when the rest of the building team picked up where he left off, then he tried to get near the furnace, he never gave me a reason why."
                kh "It's probably his grief, or he's trying to sabotage the tribe for someone else."
                kh "How can you even think to let him get away with that, no, not on my watch."
                kh "So I sent the guards after Herd, just trying to throw him in the prison so I can talk him out of it."
                e "I thought he couldn't hear anything?"
                kh "Figuratively."
                kh "I would have figured out a way to talk to him, long as he didn't run away the first glance he sees the guards."
                e "Maybe he was scared you were going to put him in prison."
                kh "I don't care, he was not going to get away with breaking my buildings apart. I would have let him out as soon as we figured out what the fuck was going on."
                if herd_dead:
                    kh "If only I got to him before my guards killed him, I have to commend them for their great aim, too well-trained."
                    e "It's really hard to straight up kill a person with a harpoon, wasn't it?"
                    kh "Not as hard as it seems. Outside, he was fine. But with the barbed edges in our harpoon, it won't be long until he bled out."
                    e "I wonder why he tried to sabotage the tribe in the first place."
                    kh "Well, there is no use asking a dead man, isn't it."
                    kh "I'll leave it as it was, it was a tragic end to one of my greatest counsels, but the building will continue as usual."
                else:
                    kh "Some day, some day I'll catch him, make him repair the damages he caused, maybe invite him back to work for the tribe again, we'll figure out a way to talk with each other."
                    kh "After he admits being a sack of shit ruining the tribe, of course, but I will make it work nonetheless."
        "That's it for now":
            e "That's all I need to know, thank you for your time, Chief."
            kh "Good."
            jump main_otsovaara_council_hall

    jump Kaurhu_Normal_Talk


label Daggi_Dialogue:

    $ cave_state = bearguard_dialogues.get("Chilly Ice Cave", {})

    show daggi_normal with dissolve
    d "Hello, [e]. Is there something you needed, or did you just want to talk?"

    menu:
        "Join Daggi to investigate the cave" if quest47.status == 3:
            jump Bear_Guard_Journey_With_Daggi
        "Ask about the Chief of the bear tribe":
            e "Daggi, can you tell me more about the chief?"
            d "Chief Kaurhu? Yes. I think he is a great leader."
            d "He would hate hearing me repeat it, but the elders still tell stories about the time a Jotunn nearly broke into the tribe and he climbed onto the thing himself to bring it down."
            d "He is harsher in manner than he is in judgment. Most people only notice the first part."
            if bearGuard_retirement:
                e "Oh, the guards told me Chief was your father, was it not?"
                d "...Yes. Chief never liked our family being treated differently, so we did not speak of it much."
                e "That explains everything, the guards thought he was about to abdicate and hand you the title."
                e "Even though we've met only for a while, you've never striked me as an ambitious leader, why do you want to be the chief?"
                d "To be honest, [e], I have wanted that for a long time. Since I was a cub, Chief Kaurhu trained me as if I might one day succeed him."
                d "Most of my life has been spent trying to become someone worthy of that place."
                e "But he never gave you that nod?"
                d "No. He keeps waiting for something. A sign, perhaps. Proof that I am ready."
                d "I am still not certain what he expects to see."
                e "I see..."
            else:
                e "Now that you mentioned it, Chief Kaurhu did seem to have his brows furrowed all the time."
                d "Yes, he often does. I think he carries the whole tribe on his face whether he means to or not."
                d "Still, I trust him."
        "Ask more about Herd and the avalanche":
            if quest47.status == True and herd_dead:
                e "Daggi, after the cave... what do you think Herd was doing there?"
                d "Looking for something he lost, I think. Or following some line of thought only he could still see."
                d "Whatever was making the new noises, it was not Herd somehow returning."
                d "I do not want the tribe telling itself that story."
                d "But he had been there before he died, and he had a reason I failed to see in time."
            elif quest47.status == True and (not cave_state.get("Returned Herd Lost Item", False) or cave_state.get("Daggi Found Herd", False)):
                e "Daggi, do you think the cave answered what Herd was doing?"
                d "Part of it, yes."
                d "He had been there, and none of it was random."
                d "I think the guards heard Herd moving through the upper cave at first, and deeper in, something older answered back."
                d "By the time we reached the crypt properly, he was already gone. But at least now I know he was chasing something personal, not just breaking things to spite us."
            else:
                e "Daggi, can you tell me more about the avalanche?"
                d "If you must."
                call Daggi_Asking_About_Herd from _call_Daggi_Asking_About_Herd_2
        "Ask about his role as the commander":
            e "Daggi, I was wondering, how did you become the commander of the bear tribe?"
            d "How did I become commander? It was not anything grand."
            e "I'm sure it is, you're kinda leading the tribe, after all."
            if bearGuard_retirement:
                d "I was just a guard, same as the others. But when Bedwyr, the old commander, was taken to prison, Chief Kaurhu needed someone to hold the tribe together, and he chose me."
                e "Why you?"
                d "I was the one who said yes."
                d "That is the plain answer. The less plain answer is that he trusted me to carry it, and I am still trying not to disappoint him."
                e "That's a lot of responsibility, Daggi. I hope you're doing great."
                d "I am trying my best, [e]. Some days that feels sufficient. Some days it does not."
            else:

                d "I was only a guard before the avalanche. Then there were... complications, and the commander at the time, Bedwyr, was sent to prison."
                d "There were evidence connecting him to the Avalanche, but I don't want to talk about it."
                e "I see..."
            if herd_dead:
                e "What about the guards, are they always like that?"
                d "The guards... I do what I can to keep them in line, but some of them use my inexperience as permission to make their own decisions first."
                e "I thought you were the commander."
                d "I am the commander. That does not mean every guard is wise enough to remember it when they are angry."
                d "They listen to Chief Kaurhu without question. They listen to me when it suits them, or when I can make myself impossible to ignore."
                "The bear leans back, then looks away. His eyes are distant, as if he's trying to avoid the topic."
        "That's all for now":
            e "That's all I need to know, thanks Daggi."
            d "Of course."
            if daggi_location == "otsovaara_council_hall":
                jump main_otsovaara_council_hall
            elif daggi_location == "frosted_taiga":
                jump main_frosted_taiga

    jump Daggi_Dialogue


label Methis_Introduction:
    scene finnkels_gaze with dissolve
    "You push open the wooden door, it opens with a small tinkling sound."
    "The warmth in the air inside startles you for a second, as you have been mostly accustomed to the tribe's chilling weather."
    "Peeking over the small shop, it looks very clean, fills with shelves and display cases with golden linings, holding a variety of expensive items."
    with vpunch
    "All of a sudden, the door behind you closes shut, as if a strong wind just slammed the door in your face."
    show methis normal with dissolve
    m "Well met, young one, to my humble abode. My name is Methis. How can I call you?"
    show methis at l1 with move
    e "Hey, I'm [e]."
    "A one-horned figure pops up from behind the counter, it was a middle-aged rhino who has skin of turquoise and scales of a dark-blue colour."
    m "Ah, exotic name for an exotic fellow."
    m "What is it that you seek today? Weapons, trinkets, scrolls of enchantment? All you see are mine to give, for a price."
    show methis at flip
    show methis at r1 with move
    "You are startled by his over-enthusiastic greetings, not to mention the throaty and rasp voice that shakes the entire store."
    m "Ah, sorry for the fright, little adventurer."
    show methis at flipback
    show methis at c1 with move
    m "I just haven't had many visitors lately, so you're a sight for sore eyes. Now, what is it that you seek?"
    e "I-I'm just looking, sir. But what is all this about?"
    "You gesture to the windows, wondering why a shopkeeper is keeping a collection of mannequins as decoration."
    m "Oh, these?"
    show methis at l1 with move
    "He says as he gestures towards the wooden statures."
    m "Well, they are my assistants, they tend to my shop when I go to bed. These two are always eager to please, aren't you, boys?"
    "You look at the owner, expecting some kind of reaction or a joke, but he remains staring at the two."
    m "This armored stud, is called Kivy; and the right one, he's Aerik, he enjoys basking in some sunlight once in a while, it's not like we're well illuminated down this abyss."
    m "And... they seem to be very interested in you, young one."
    "You look back at the two mannequins, they don't seem to even move an inch. You can hardly believe these materials allow any movement at all, let alone talking."
    e "I don't think these mannequins are real."
    m "What are you talking about? My assistants are just doing their job right now, which is showing off the shop's items, you wouldn't want a moving display that runs around the shop, wouldn't you?"
    m "They're just a little shy, is all. They'd take care of the shop while I rest at night, and, they're cheaper than a bear cause I don't even need to pay them."
    e "If you say so..."
    "You shrug and walk further into the shop. But Methis doesn't stop following you."
    show methis at c1 with move
    m "So, what do you seek? Weapons? Trinkets? Scrolls?"
    e "I- I uh... I will take a look myself. Thank you, Methis."
    m "Very well."
    "Methis gives an unnaturally wide smile, one that makes you question if you somehow got under his skin."
    show methis at l2 with move
    "You can feel the shopkeeper's stare burning the back of your neck as you try to inspect the merchandise."
    m "Give me a shout, if you need anything."
    jump main_finnkels_gaze

label Methis_Dialogue:
    scene finnkels_gaze with fade
    hide screen menu_buttons
    show methis normal with dissolve

    m "I am here, at your service."
    jump Methis_Normal_Talk

label Methis_Normal_Talk:
    m "What can I do for you today, [e]?"

    menu:
        "Check out the shop":
            jump Methis_Shopping
        "Ask about history of the shop":
            e "So, Methis. How did you come to own this shop?"
            m "You see, the Finnkel's Gaze was merely a smaller, humble forge a few decades back then."
            m "My friend, Eirik, was an excellent blacksmith, he made all the tailored armors and weapon to each guards of the tribe at the time."
            e "That name sounds familiar..."
            m "And I, I was a simple merchant, but I know a good business when I see one, and I know how to rope in some customers with my presentation."
            m "So, after a period of consideration, we decided to merge our shops together, and the Finnkel's Gaze was born."
            e "So, why did you name it Finnkel's Gaze?"
            m "Because, this is where we are, the Finnkel Abyss, it stretches far outside of the tribe, and I liked the sound of '{i}Gaze{/i}'. It's catchy, don't you think?"
            e "Ah, I see."
            m "Look, I handle the marketing side of the business, and Eirik handles the crafting side of the business."
            m "And, together, we are the best shop in the tribe, we have the best armors, the best weapons, and everything in between."
            m "The other shops in the tribe, they couldn't even compare to us, we basically ate them all, consumed nicely in the belly of the beast."
            "The rhino slaps his belly, giving you a hearty smile."
            m "Not literally, of course."
            e "It sounds like you two were a great team."
            m "He has the craftmanship, and I have the showmanship. We are a match made in heaven, I tell you, and we... we were unstoppable."
            e "So, what happened to Eirik? Is he still around?"
            "The shopkeeper suddenly takes a long pause, his mouth hangs agape before resuming back to his usual self."
            m "D-don't worry, he is still around, he's just busy at this time. I'm sure... he will grow to like you when he's back."
            e "Oh..."
            "The rhino chuckles, staring out the windows."
            m "{size=20}He'll be back, any moment now.{/size}"
            "You can't help but feel a little bit of unease, as if there's something wrong, but you decide to brush it off."
        "Ask about his shop's reputation":

            e "So, what's your reputation in the bear tribe?"
            m "Maybe you should ask the bears yourself, I'm just a humble shopkeeper."
            m "For what I know, the chief's got a bigger fish to fry, so he doesn't bother me much."
            m "But the guards, they love my shop, they come here to buy armors, weapons, and all other stuff, they're my best customers."
            e "Ah, I see. What about the other shops? Do you have any competition?"
            m "The other shops? They're just a bunch of amateurs, if you need anything at all, you come to Finnkel's Gaze."
            e "How about... like from the other tribes?"
            m "Uh... oh... the others. We don't wander out much, but I heard there's a lone potion maker back in the warm land, I've heard a lot about him."
            m "But, I'm not worried about anyone out of our land, I have my own customers, and they're loyal to me."
            e "I see."
        "How is it going?":
            e "So, what's new about you?"
            m "Ah well, the shop's getting some new collections after uncovering some of the artifacts from the avalanche."
            m "It will be very exciting, I promise."
            e "I see."
        "That's it for now":
            e "Okay, thanks for your time, Methis."
            m "No problem."
            jump main_finnkels_gaze
    jump Methis_Normal_Talk
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
