label Pirkka_Dialogue:

    jump Pirkka_Tavern_Talk

label Pirkka_Tavern_Talk:

    $ dospirk = renpy.random.randint(1,4)
    show pirkka normal with dissolve
    if dospirk == 1:
        p "My dear friend, how was your day!"
        e "Very well, and meeting you now just made my day better."
        "You notice a curious smile tugging at the corners of his lips."
        p "Y'know, I played some music up 'ere, looking at the audience and I find that funny little fella looking away from me."
        p "A wolf type, muscles sprawling on his body and he has this, outfit that showed his plump flurry chest."
        "The songsinger gleefully exclaims, cupping against his chest to mimic the wolf's sheer size."
        p "Mayhaps he's the Nocturnal Hunk I've been hearing about."
    elif dospirk == 2:
        p "Greetings! My dear friend. How does the road treat you?"
        "As usual, Pirkka's voice danced with enthusiasm, his words like musical notes that filled the tavern."
        e "I'm holding up very well, you?"
        p "The generous keeper told me a lot of stuff about you. You were serving plates down there?"
        e "It was just my side job."
        p "And from what I've heard, it was you who brought us the finest ale in the continent?"
        e "The recipe was from Cane. I just helped him get the materials."
        p "The only reason I can enjoy this fine refreshment is because of you. There's no song in the world that expresses my gratitude enough, [e]."
        "Pirkka raises his cup of ale, and gentle smiles."
    elif dospirk == 3:
        p "Well met, my friend."
        p "Sit down, sit down! It's been quite a day here at the tavern."
        "Pirkka motions you to sit incredibly close in front of him."
        e "Hello, Pirkka. Hope you like hanging out in the Tavern."
        p "Pray tell, have your travels brought you adventure and tales to share?"
        p "I'm eager to hear of your triumphs and trials, for every wanderer carries a world within their heart."
        e "Your words just warms me up everytime you speak, Pirkka."
        p "Ha, not my words. It was from a famous scribe back in the Old Times."
        e "Fascinating."
    elif dospirk == 4:
        p "{i}Kins turned foes when his name is spoken, for years he deemed the last heir of the lion...{/i}"
        p "{i}From none but his stronger brother, 'twas a claim sturdier than blood and tether.{/i}"
        "The bard's voice was like a whisper, yet it echoed through the entire tavern."
        "He slowly opens his eyes, and his gaze meets yours."
        p "Ah, [e]. I didn't see you there. I was just singing about the story I've heard from the East."
        e "It's a beautiful song, Pirkka. What's it about?"
        p "Oh... did you not know? It's about some rumors of the royal bastard in the palace."
        p "Granted, I don't usually sing over the grapevines, but it's a tale that's been known to everyone in the town I travelled from."
        e "I see."
    if quest35.status and pirkka_show_day <= 0 and pirkka_show_day != -timenow.day and renpy.random.random() < 0.5:
        p "Hey, [e]. May I borrow you a few minutes to go somewhere with me?"
        jump Pirkka_Show

    jump Pirkka_Normal_Talk

label Pirkka_Normal_Talk:

    menu:
        p "How may I help you?"
        "Ask about his stay in the Tavern":
            jump Pirkka_Ask_Tavern
        "Ask about his role as a wandering Bard":
            jump Pirkka_Ask_As_Bard
        "That's all for now":
            e "That's all."
            p "Until next time, my friend."
            "Pirkka strums another pleasant chord as you walk away."
            jump main_nocturnaltrunk_upper

label Pirkka_Ask_Tavern:
    e "How's it going in the Tavern?"
    p "Ah, the Nocturnal Trunk, a place that sets my spirit ablaze!"
    p "This joint has got a lively vibe, I tell ye."
    "Pirkka grins and leans back, his fingers tapping a playful rhythm on the table."
    p "The air here is thick with stories, as potent as the aroma of ale and roasted meat."
    p "And then there's Cane, the keeper of the tavern."
    p "He could juggle mugs with such finesse, it seemed the very stars danced in his hands."
    p "There is a flair of mystery I can feel within his heart. Especially when we were talking about you."
    e "Maybe because I sometimes work in the Tavern."
    p "Not merely this reason, I'm afraid. I've heard something much more endearing, but it shall be strictly between you two."
    "You ponder over his words, but the tiger quickly continues before you can even understand the implication."
    p "Regardless, this place's truly a haven of merry spirits and lively tales. Seems like people are very enthusiastic about my music."
    p "Indeed, me friend. The sound of mirth and jest echoed through the halls, as if the very walls themselves joined in the revelry."
    p "I've sung many a song in that tavern, and I can tell ye, the spirits of joy and camaraderie were alive and well."
    "Pirkka leans in closer against your face, his voice lowered."
    p "Anyway, be careful with the card slingers just at the corners, they're friendly bunch, as long as you've got your gold."
    e "Have you had any encounters with them?"
    p "Oh indeed. One evening, they invited me to a friendly game of cards."
    p "I considered it hard to play opposite to the alligator with those teeth, I could've lost a hand, and the hand."
    p "Might be hard to deal with."
    "He chuckles, a mischievous glint in his eyes."
    p "We had quite the match, and in the end, I left them dumbfounded and a few coins richer."
    p "Keep yer peepers peeled, or they might just snatch more than your purse."
    e "Thanks for the heads up, Pirkka. I'll be sure to stay on guard if I decide to test my luck."
    p "Hope I've gotten yer heads up too."
    jump Pirkka_Normal_Talk

label Pirkka_Ask_As_Bard:
    e "So, how did you become a bard?"
    "Pirkka leaned back against the table, his eyes reflecting the flickering flames of the tavern hearth."
    p "Let me sing you my story, [e]."
    "With a wistful smile, he began his tale, his accent lending a distinct charm to his words."
    p "Well, ye see, it all began in a humble village nestled amidst verdant hills and singing streams."
    p "'Twas a place where stories echoed in every corner and melodies danced upon the wind."
    p "From a tender age, I found meself captivated by the ancient ballads and tales spun by the village elders, their words like magic spells enchantin' the air."
    "Pirkka's voice hung in the air, like the lingering notes of a haunting melody."
    p "One fateful eve, as the moon ca'est its silver glow upon the village square, a wanderin' minstrel arrived."
    p "With his weathered lute and a voice that could charm even the stones, he regaled us with sagas of heroes and monsters, of love and loss."
    p "That night, as the melodies wove their way int'me soul, I knew me fate was sealed."
    p "I took to the road, me heart aflame with a hunger for music and stories."
    p "From bustling taverns t' outer wilds, I wandered far and wide, learnin' from every bard, minstrel, and troubadour I met along the way."
    p "They tau-yt me the secryts of the lyre, t'ze power of a well-placed jest, and the ancient lore hidden in forgotten scrolls."

    p "And so, me friend, that's how this wanderin' soul found his place as a bard, a teller of tales and a weaver of dreams."
    p "With each strum of me lute and every lyric that dances from me lips, I carry the echoes of those who came before, keepin' the ancient arts alive in a world thirstin' for magic and wonder."

    "The tavern patrons, including you, are all enchanted by his story, listened in awe, your hearts touched by the passion that emanated from the whimsical bard."
    "You clapped your hands slowly, as Pirkka stares at you with an alluring smile."
    e "That was quite beautiful, Pirkka."
    p "Thank you, my friend. 'Twas but a tuneful words imbued with the story of my own."
    jump Pirkka_Normal_Talk

label Pirkka_First_Meet:
    if isNight():
        scene prattlefell_meadow_night with dissolve
    else:
        scene prattlefell_meadow with dissolve
    "Walking through the plains, you notice a lone figure sitting on a nearby rock, strumming a lute."
    $ renpy.music.play(mBard, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ pirkka_meet = True
    my "{i}-land of bloom, roaming with a heart of tune.{/i}"
    my "{i}Words of legends and olden tale, dark ink of valor and fair rune.{/i}"
    my "{i}Percolating upon scripts of paper, newly trimmed, browned by the tides in days of yore.{/i}"
    my "{i}And lost.{/i}"
    my "{i}Oh, my champion, how should I atone for my shameful prune.{/i}"
    "The stranger fingers his lute with ease, singing with his amazingly soothing voice."
    my "{i}What's the future of Mokken without your lore, Kantele.{/i}"

    "As you approach, the figure stops his singing. He looks up and grins at you, revealing a charming smile."
    show pirkka normal with dissolve
    my "Well met, traveller! Didn't expect audience in zis vast land."
    my "What brings you to these parts?"
    "He exclaims in a sing-song voice, with a hint of a medieval accent."
    e "I'm just passing through. Looking to explore the land a bit."
    my "Ah, an adventurer! How exciting! Pirkka's the name, I'm just a 'umble bard, wand'rin' from town to town to spread the joy of music."
    "The bard smiles, strumming a few chords on his lute."
    pause 0.5
    e "My name is [e]. It was nice to meet you, Pirkka."
    e "I couldn't help but hear your song from afar. It was quite lovely."
    p "Ah, thank you kindly, it's not often I get to perform for such a fine audience."
    "Pirkka replies, giving a small bow. And your cheeks blush of bright red."
    e "Uhm- What's the song you've been singing about?"
    p "Ah, that's only improvisation, as ye say, about a long-winding, echoes of tales of yore."
    "He looks up at you, his eyes twinkling mischievously."
    p "Well, 'nough about me, what brings you on zis journey?"
    "You notice he'd tone down his accent to match yours subtly."
    e "I'm not sure, just walking around and discovering new adventures."
    "Pirkka pauses for a moment, seemingly pondering something."
    pause 0.5
    p "So, you too are a wand'rer, aye? 'onestly, I find it quite {b}roam-{/b}antic."
    with vpunch
    "Before you can react, Pirkka has already burst into laughter at his own joke."
    "You can't help but chuckle along with him, despite the corniness of the pun."
    e "Does that mean you wanders around as well?"
    p "Of course, I'm a bard. I tell stories with my sweet and kindred voice, everywhere I goes."
    p "Say, you seem like a sprightly one. Zere's one reason I roam around this beautiful valley, not just for ze sight."
    pause 0.5
    "The bard leans in closer to you, his eyes lighting up with excitement."
    e "What's the task?"
    p "It's simple, really."
    "Pirkka says, twirling his lute absentmindedly."
    p "A group of bandits made off with a precious scroll of mine, and I'm in dire need of its contents."
    p "A ballad, written by ze ancient poet Kantele, who's also my ancestor. It's the original text zat 'olds true to my heart of passion."
    e "And how can I help with that?"
    p "I need you, to sneak into their camp and retrieve ze scroll for me."
    menu:
        p "So, 'ow you say? I smell a certain grit and bravery in ze air."
        "Help Pirkka find his scroll":
            "You hesitate for a moment, but the gleam in Pirkka's eyes is infectious."
            e "Alright, I'm in."
        "Decline Pirkka's request":
            "You shake your head."
            "Pirkka looks disappointed, but he quickly puts on a smile."
            p "Ah, zat's not good. me friend. But I'll find a way to retrieve it on my own."
            e "I'm sorry, Pirkka. It's too dangerous of a task."
            p "Understood, understood."
            "The bard says with a wave of his hand."
            p "May your journey be filled with wondrous adventures and grand tales to tell, [e]."
            e "And... you too!"
            "With a bow, Pirkka bids farewell to you and set off onto a different path."
            "As you walk away, you can still hear Pirkka humming a familiar tune, the one he sang earlier."
            "Despite their separate paths, you couldn't help but feel a connection to Pirkka and his quest."
            "It may have been the last you two will ever see each other."
            "Or perhaps, you would meet again someday, and Pirkka would regale you with more of his whimsical tales."

            jump main_prattlefell_meadow
    "Though you never want to mess with the bandits, looking at the pleading eyes of Pirkka, you can't help but to make his smile brighter."
    if bchest_sprite_img == "bchest_sprite2":
        menu:
            "Tell Pirkka about what you saw earlier":
                e "I've sneaked into the bandit's place earlier, actually."
                p "Oh, you already did? That's perfectly splendid!"
                p "Did you find the scroll?"
                e "Sadly, no. But I found some clues as to where it went."
                e "They sold it to someone else in the village, I suppose it's Lusterfield?"
                $ QuestBegin(quest35)
                $ bandits_hideout.discovered = True
                $ quest35.qProgress(__("Enter the bandit's hideout and sneak pass the bandits to find clues about Pirkka's prose."))
                $ quest35.qComp(_("Report back to Pirkka"))
                jump Pirkka_Bandit_Quest_Report
            "Continue":
                pass
    if isBandit:
        "Perhaps you can take advantage of the bandit boss recognising you as one of them."
        e "I can get into their camp quite easily, actually."
        p "Are you saying what I think you're saying?"
        "You nod slowly."
        p "Say, you're a t-zief in disguise, aren't you, lad."
        e "I just happen to stumble upon their boss at the right time. I'm not a fan of stealing someone else's property."
        p "Eh? So am I gonna be grateful ye aren't stealing the rest of my {b}lute{/b}?"
        "His pun flew through your head for a moment, until Pirkka waves his instrument, and you both chuckles loudly over that stupid pun."

    elif bandit_sneak:
        "You've looked into the camp when there were no one but the bandit boss, perhaps you can get into there quite easily again."
        e "I know where they're hiding. I've been to their place a while ago."
        if sharkbandit.win > 0:
            e "H-heh... The boss was all alone when I beat him to submission."
            "Pirkka's eyes widened in surprise."
            p "By the deities, you have? That's impressive, you're a brave one indeed."
            p "If you be willing to help me retrieve the lost prose? I'll make it worth your while, and it would mean the world to me."
            "The bard stares at you with admiration, and he holds his hand onto yours expectantly."
            "Pirkka's enthusiastic smile has definitely worked on you. And almost immediately, you nod your head."
        else:
            e "And I... I can only say the bandit boss's not one to be underestimated."
            "Pirkka chuckles at your words."
            p "Aye, at the least you're not taken captive and has all your {b}lute{/b} stolen."
            "His pun flew through your head for a moment, until Pirkka waves his instrument, and you both chuckles a little."
            p "Fear not, my friend, for with your help, we shall retrieve the lost prose and teach those bandits a lesson they won't soon forget!"
            "You can't help but smile at his enthusiasm."
    else:
        "The rat thief you've met wasn't quite the stud you were expecting, but surely given that you've tracked him down successfully. It'd be the same for a whole band of bandit."
        e "One of them stole from our farm recently. But I don't know where they're hiding in."
        "Pirkka grins."
        p "Ah, that's the beauty of it. I already have the location of their camp, thanks to a little birdie."
        p "All you have to do is find the scroll and bring it back to me."
        e "Sounds easy enough."

    jump Pirkka_Bandit_Quest_Begin

label Pirkka_Bandit_Quest_Begin:
    e "What exactly happened between you and the bandits?"
    p "The thieving rascals took my prose, in the middle of the road, they came in groups, and alas, I wasn't able to stop them."
    e "W-why would they take some pieces of paper?"
    p "Well, they were invaluable to those who understands ancient tales, I guess they knows."
    p "It was a delicate parchment, bound with a faded red ribbon with ancient markings."
    "Pirkka shrugs, but his smile doesn't fade."
    e "I will get it back for you."
    p "Aye, I trust in you, adventurer. May Gods ever be in your favour."
    p "And it's time for me to start moving, [e]. I can feel inspiration coming in waves after waves."
    p "Perhaps my new ballad will be for a bard ever be in patronage for a brave soul."
    p "May we meet once more."
    e "See you, Pirkka."
    "Pirkka walks away, he positions his hand on the lute, and begins singing."
    p "{i}-Oh, fair listener, lend me your ears.{/i}"
    p "{i}And I'll sing a tale of a hero who appears.{/i}"
    p "{i}To vanquish the bandits who caused such fea-{/i}"
    "You glance at the back of the wandering bard, he's walking further and further away, along with a simple tune that eventually fades."
    $ QuestBegin(quest35)
    $ bandits_hideout.discovered = True
    $ quest35.qProgress(__("Enter the bandit's hideout and sneak pass the bandits to find clues about Pirkka's prose."))
    jump main_prattlefell_meadow


label Pirkka_Bandit_Quest_Report:
    $ renpy.music.play(mBarn, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)

    p "But we have a lead, at least. Let's think... who in this land has a particular fondness for ancient tales?"
    "You two pause for a long while, as Pirkka's face falls lower."
    p "Alas, I don't know anyone in Lusterfield."
    e "I don't think I know one either."
    p "Oh, that's a darn shame. We had our hopes up, didn't we?"
    e "I'm sorry, Pirkka. I've tried my best to find the script."
    p "Don't fret about it, friend. I'm grateful for your help nonetheless."
    p "Maybe it'll pop up again, somewhere. Here's the 150 gold, for your trouble."
    $ pc.gold += 150
    "The bard strums a few chords as he hands you the gold."
    "You ponder over your words for a moment."
    e "Do you want to go back to Lusterfield with me? I suppose we can find the buyer over there."
    e "Plus, staying here can be dangerous, those bandits might come again."
    p "I wander over the plains, it's what bestows me, call it inspiration for new songs."
    e "Do you want to stay over at our village for the nights?"
    "Pirkka taps on his lute for a few times."
    p "Is there a Tavern?"
    e "Yes, Nocturnal Trunk. I bet the keeper is going to like you, a lot."
    p "I should rent a room in the Tavern, like you said, it's dangerous to stay in the wild at night."
    p "And I should find the prose with you, my friend."
    "Another huge grin is plastered over his face as he hurries to put out the campfire."
    p "Making sure I'm not burning down the whole place."
    "He gets up soon, making sure he didn't drop anything at all."
    p "C'mon then. Lead the way!"
    "You two begin to walk towards the direction of Lusterfield."
    scene grove_of_harvest with dissolve
    show pirkka normal with dissolve
    e "So, how did you hear about the village?"
    p "I've traveled from taverns to taverns, everywhere in Mokken. Theirs are one of the fews I've yet to visit."
    e "If you've visited everywhere, then you must be very famous, no?"
    p "Famous is a word up for debate, but I aspire to be a legendary bard one day, like Kantele."
    e "Was he the poet who wrote the prose we're looking for?"
    "Pirkka nods."
    p "Say, the one that bought the prose from bandits, maybe they took an interest in Kantele's work."
    e "And the buyer couldn't be anywhere too far, he's a regular to the bandits."
    p "Ah, fair. T'is but a mere challenge for a young adventurer and a bard, we'll find him, soon 'nough."
    "Along the way, Pirkka shares with you another sweet tunes, this time without the singing."
    "He's much more lively, strolling the path with fleet footworks."
    "It's a long of fun talking with the tiger, his soft-spoken voice is just calming to your ears."
    "And after crossing the farm, you've arrived to Lusterfield."
    scene lusterfield02 with dissolve
    show pirkka normal with dissolve
    p "Ah, 'tis a fine village ye've brought us to, lad."
    p "I can smell the ale already. Let's go find ourselves the mysterious Nocturnal Trunk."
    scene nocturnaltrunk with dissolve
    show pirkka normal with dissolve
    "As you entered the tavern, Pirkka looked around and noticed a few locals staring at him curiously."
    p "By my troth, this is a lively place."
    p "Good evening, good folks!"
    "Pirkka exclaims, and immediately walks towards the counter, with Cane working on cleaning the silverwares."
    show pirkka normal at r1 with move
    show cane normal at l1
    c "Welcome to the Nocturnal Trunk! Ye' a bard? Haven't been fancied by a singing one for a while."
    c "And ya, good lad. C'mon here."
    "You sits comfortably on the seat besides Pirkka, as Cane gives your head a light pat."
    c "How shall I call ye, lad? Mine's Cane."
    p "I'm Pirkka. I'm travelling from Tavern to Tavern, looking for inspiration and all."
    c "Talkin inspiration, it's all we have over here at Nocturnal Trunk, maybe [e] here can teach ye one thing or two with his skills and all."
    "You blush intensely over Cane's comment."
    e "W-well, not the one Pirkka is looking for."
    p "Ha. I'm also looking for a lost prose, good sir. It was sold by a bandit, somewhere near, I reckon."
    c "Prose? I'm afraid I don't know anything about songs and such, ye shall go ask that cheeky little lion, over at King's Pawn, maybe he'll meet more buyers."
    p "Well, 'tis better than nothing. Many thanks."
    "Pirkka ponders for a moment."
    p "And may I stay for a night here?"
    c "Price's 75 gold, per night. But since my lad invited you here, it's 25 gold."
    c "Our rooms are big, but probably just barely big enough for ye hunky ass."
    p "Ohh!"
    "The bard exclaims with a hint of surprise."
    p "And might I sit in front of your lively hearth, I shall grace your tavern with my sweet tunes."
    c "Aye, be my guest."
    "Cane hands a key to Pirkka, as the latter briskly shoves the gold forward."
    c "This is for the room upstairs, should be quieter if ye like privacy."
    p "I enjoy a lovely company, but solitude is better with eyes closed. Thank you, Cane."
    p "And thank you, [e], for leading me to this village with many merriment."
    p "Please, if you can. Ask around the village to see where my prose ends up."
    "You smile, and Pirkka strums a few chords before taking his leave."
    $ quest35.qComp(_("Ask around Lusterfield to find the prose' buyer."))
    $ quest35.status = 3
    jump main_nocturnaltrunk

label Pirkka_Show:
    scene nocturnaltrunk_upper with dissolve
    show pirkka normal with dissolve

    e "Where are we heading, Pirkka?"
    p "The tavernkeeper rented me a room for free. And, with his consent, I figured we shall repurpose that space into a performance room for today."
    e "A performance room?"
    p "Yes, yes. I did recall promising a certain red dragon fellow with a personal performance of the ancient prose."
    p "So perhaps this would be a perfect opportunity to show you the wonder of poetry."
    e "Is that, me."
    menu:
        p "Call it, an invitation to a magical journey. And my gratitude for your perseverence to locate this precious prose."
        "Accept his invitation":
            $ pirkka_show_day = timenow.day
            e "Well, lucky me. I wouldn't miss it for the world."
            p "Come, my muse, allow me to escort you to ze front-row seat."
            "Pirkka winks, his eyes sparkle mischievously."
            "From there, he leads you to the door closest to the stairs, a sign with Pirkka's name hangs lazily on the door."
            scene canebedroom with dissolve
            show pirkka normal with dissolve
            "In the room, it was filled with papers and books, some notes left on the table as you noticed the returned prose still presented on top of the pile of books."
            p "What do you think, m' dearest companion. Isn't zis room special?"
            e "It's a delight indeed. Can't believe you've decorated his room with such delicacy already."
            p "Cane offered me a place to live, and in return I shall transform his place into a stage full of enchanting presence."
            "He turns around, eyes staring right at you."
            p "You offered me a second chance at my prose, and in return..."
            "Pirkka pauses, then raises the corner of his mouth, showing an infectious smile."
            "He closes the door behind you, and all of a sudden, the noise from the tavern simmered down into silence."
            "And the only thing you can focus on, is the purple tiger in front of you."
            p "I shall sing you the prose you've recovered for me."
            "He sits on the chair, hand positioning on the strings of the lute. Slowing adjusting the tunes."
            "At the same time, you quietly finds the corner of the bed to sit on, heart pounding in anticipation of his singing."
            p "Legends of Mokken, part three, by Kantele Koskin."
            pause 1
            $ renpy.music.play(mBard, loop=False, fadeout=1.0)
            p "{i}In days of yonder, when the world was fair,{p}A monster, Etch, trapped beneath the darkest lair.{/i}"
            p "{i}With a flaming soul and ominous hair, {p}he threatened and reigned over the land of bare.{/i}"
            "Pirkka begins with the ancient ballad, you can hear such gritty details contrasted with his soft and pleasant voice."
            p "{i}Its power immense, its wrath so rare,{p}Of mortals and lizards, their mind molten and bare.{/i}"
            p "{i}But a wandering hero, with sword in hand,{p}Did march forth to fight this foul demand.{/i}"
            p "{i}He fought so long, he fought so well,{p}And with his might, the beast did still.{/i}"
            "Between verses, he shares fleeting glances with you, his orange eyes lingering for a moment longer than necessary."
            p "{i}Yet the monster was crafty, and did deceive,{p}It played on the hero's sense of believe.{/i}"
            "Your pupil widens, losing focus, entirely magnetized to the depth of his glistening pupil."
            p "{i}A shadow room, and a reckless ruler,{p}came to his rescue, but naught the warrior.{/i}"
            p "{i}Futile was the wicked turns and tricks,{p}for at long last, our hero set free of sticks.{/i}"
            p "{i}With a final strike, the beast was slain,{p}but the hero too, was taken in pain.{/i}"
            "He winks playfully as he starts tuning his lute, fingers dancing over the strings with finesse."
            p "{i}Cursed by the wicked hex it bore,{p}the monster's essence forevermore.{/i}"
            p "{i}And so the hero fell, yet also arose,{p}for his soul weakened, the end was close.{/i}"
            "The melody is lively, and his voice, rich with emotion, fills the air around you."
            p "{i}The champion wandered, as his husk hollowed, {p}drifted by the wind, until death followed.{/i}"
            p "{i}Wandering Spirit, protector of the forests,{p}blessed by the seasons, bestowed us our harvests.{/i}"
            p "{i}Messenger, Walker, roam this land with your might,{p}and may all spectres be doused in fright.{/i}"
            p "{i}A song of sacrifice, in whispers and tale,{p}and hear, everyone, a brave soul is now at rest.{/i}"
            p "{i}A hero's struggle, a soul in despair,{p}in tapestry of time, shall the story live on in air.{/i}"
            "As the last note fades away, Pirkka takes a bow, his gaze fixed on you."
            stop music fadeout 1.0
            "He stands up once more, fur scruffles softly, leaving you with a warmth that transcends the lively ambiance of this room."
            p "How's the poem, Kantele's words are certainly a perfect blend of story and heroism, no?"
            "Your eyes refuse to lift off of his handsome face, completely oblivious to what he just said."
            p "Oi!"
            "His fluffy ears perk up as he notices your drooling mouth. His face blushing with a mix of embarrassment and flattery."
            e "O-oh. Yeah. I love your voice by the way, Pirkka."
            p "Never have I experienced such an reaction from mine audience, you're one of a kind, [e]."
            e "Your hand moves like magic. I can never figure out how it works with this instrument."
            "The bard paces lightly, taking a seat by your side."
            p "Sounds like someone wants to learn to play my lute! No?"
            "You nod."
            e "Of course!"
            p "Alright, first thing first, ze posture is important, crucial even."
            "Pirkka sits upright, puffing his chest outwards, you watch on the side, gasping as his puffy front bulges out of his cape."
            p "Come, try it yourself. Show me you're confident."
            "He puffs up once more, showing you his sturdy physique. You watch and mimic his posture."
            e "Am I doing it right?"
            p "Yes, yes. Perfect. Now hold onto ye posture."
            "He gently places his hands onto yours, the soft fur on his finger soothes the gaps between your paws, causing you to flinch a little."
            "A tender grasp sends warmth down to your spine, he adjusts to sit closer, just to reach onto your hand better."
            "Pirkka positions your hands onto his wooden lute."
            p "Cradle my lute as if it were a delicate lover of yours, not too tight, not too loose."
            p "Ye gotta feel ze curve, as if ze wood's speaking to you."
            "You awkwardly move your fingers along with Pirkka's movement, quickly come to a realisation that they're much stiffer than Pirkka's."
            e "Damn, that's harder than I imagined."
            p "Oy, relax, try touching it gently instead. My lute's a shy darling."
            "His hand presses onto you, signaling for you to move in his direction."
            e "Okay."
            "With a plinch, you pluck your fingers onto the instrument, eliciting a loud squeaking sound."
            p "Not quite right, mine muse. Not too timidly, not too boldly, feel the vibrations beneath your fingertips."
            "Pirkka leans in on you, getting incredibly close, his breath almost tickling your ear."
            p "Follow my lead here, [e]."
            "You can feel his heartbeat from behind you, his embrace warming you up into a gentle craddle."
            "The bard begins to lead you through a simple, alluring tune, all the while he's gazing into you with a twinkle in his eyes."
            "It was such a mesmerising experience, having this reputable bard essentially hugging you from behind, at the same time learning to play such music to your ears."
            p "Oh my oh my, you have the touch of a maestro now, see. The lute responds with your desire, music is a conversation, no?"
            "The warmth from the back of your neck sends you shiver as he speaks."
            p "It's all about the intimacy between the musician and the instrument."
            e "It's mostly your doing, Pirkka. I wasn't moving much on my own."
            p "Well, it'z your first time, but now you've learnt it, try it on your own!"
            "The bard behind you releases his clutches, making you feel so cold, it's almost as if you've lost something outright."
            p "Picture someone you hold dear to your heart, let the music tell your story, like a love letter to the heart."
            "Suddenly, he taps onto your leg, humming to the tunes you've just played."
            p "Ready?"
            "You get your hands in position, keep reminding yourself the advice Pirkka just gave you."
            "He hums again, slapping onto your thigh playfully as you begin to straddle the lute."
            "He's flicking your finger messily to his tunes, sometimes out of rhythm."
            "It was a short and simple tune, yet so catchy that you're beginning to hum to it over and over."
            e "Pirkka, I think I-"
            "With the end of the tune, you turn around to look at Pirkka's reaction, only to see his gaze lingers onto your eyes."
            e "Am I getting the hang of it?"
            p "Very."
            "You're embarrassed by his comment, obviously your first time playing was a mess, but his enthusiasm is coursing through your body like a charm."
            p "I'm already thinking about a duet with you, [e]."
            "He whispers under his warm breath, and it's all you can hear."
            p "Sad we don't have a second lute around here."
            "The corner of his lips raises, slowly revealing an alluring smile, of which you can't help but to follow."
            "Your lips are so close to touching each together, Pirkka tilts his head slightly, seemingly adjusting to meet your face."
            pause 1
            scene black with dissolve
            "In an instant, you reach out to kiss Pirkka, it almost feel like an instinct, your lips just attracted to each other like magnets."
            "It almost comes as a shock to Pirkka at first, he pulls out for a second, your saliva dripping in his maw."
            "You stare at each other in lustful gaze, then again, reaching out for another kiss at the same time."
            "This time, it was much longer, your teeth grazing against his lower lips, savoring the aroma of his taste."
            "You close your eyes, fully submerge yourself into the delight of kissing this handsome tiger. He's not more experienced as you thought, but you can tell he's enjoying the moment also."
            "His tongue makes way into your mouth, exploring, licking clean inside while you do the same."
            "Slowly, you wrap your arms around Pirkka, holding him tight as you continue smooching this tiger man."
            "Both of you are so immersed in the moment, that you've almost forgotten to breath, but, a part of you wish this moment will never end."
            pause 1
            scene canebedroom with dissolve
            show pirkka normal with dissolve
            "When it's time, you pull out, just to breath in his hot breath. You open your eyes, gazing deep into his eyes as he reaches out once more."
            "The bard smiles, then laugh loudly."
            p "I didn't expect that."
            e "Me neither."
            p "You're a great kisser, [e]."
            e "Thanks, you too."
            e "I... I just admire you too much. From the time we met, I feel that whenever you play the music, I just get pulled in in front of you."
            "Pirkka raises his eyebrows in awe, his tail wags on the bed excitedly."
            p "You're such an inspiration to me, my muse. Even being a courier, everywhere in zis Lusterfield village, I hear your name spoken fondly."
            p "Like ze ancient heroes sung by us bards."
            e "Pirkka, you're too flattering."
            p "What can I say, you embody that definition pretty well, my prose-keeper."
            "The bard grins wholeheartedly, all the while he's staring at you at mere few inches. He's still so close."
            e "I am no hero, I just like walking around the world, maybe helping people."
            p "If you're no hero, you will be one now, come."
            "Pirkka smirks as he grabs his lute, climbing to the back of the bed."
            e "What are you doing, Pirkka."
            "You exclaim as you turn your head curiously."
            p "Singing a song for you. Of course."
            "He adjusts the instrument, hands warming up to the tunes he has in mind."
            "You place your hands on the bed, curious as to what he has come up."
            p "Here goes what I heard from the people in Lusterfield, of this legendary character in front of me, [e]."
            "Pirkka clears his throat, and begins to sing."
            $ renpy.music.play(mBard, loop=False, fadeout=1.0)
            p "{i}A dragon of origin, a goat of history, {p} raised from a village from another world.{/i}"
            "Pirkka's fingers move effortlessly across the strings, creating a mesmerizing tune."
            p "{i}Stammering, searching out, {p}a dear friend's trail, in his path he hurled.{/i}"
            p "{i}Out of your depth, A change of hart, {p}he channels a door out the other side.{/i}"
            p "{i}Your eyes of stars, night's reflection, {p}fades before setting off for a sleigh r-ide.{/i}"
            "It's mind-blowing how much he has heard about your backstory, without you ever telling him."

            p "{i}Out of this land, the wanderer has drifted, {p}where he's been, an echo of slumber.{/i}"
            "He leans in, strumming the lute with an almost hypnotic rhythm. You're too busy listening to the lyrics in this way."
            p "{i}A stranger, a lion. Someone is awoken. {p}The world has been shifted, does he still remember.{/i}"
            p "{i}Taken in, a pawn shop in Lusterfield. {p}A friendly custodian offered the role of courier.{/i}"
            p "{i}And there he went, a brand new life, {p}adventures lied ahead of our new traveler.{/i}"
            "Pirkka gives you a playful wink, and licks his lips. You lean in closer, just to feel his warmth."

            p "{i}Slime, Buggbears, evil monsters {p}emerged from deepmost of the forest.{/i}"
            p "{i}He slashed, trampled, under his weapon {p}no contender put him to the test.{/i}"
            "The bard praises you like a real hero, something you never did hear anyone say."
            p "{i}And soon he arrived, a tribe of goats, {p}weavers of magic sent him on a conquest.{/i}"
            p "{i}A treaty of peace, stuck between two factions, {p}he sees a calm before the tempest.{/i}"


            p "{i}Apprentice of a great hunk, he embarks an adventure, {p}together they encountered a figure of moss.{/i}"
            p "{i}A weird stone, nonetheless. {p}He traces to the chief of buck a stream across.{/i}"
            "Pirkka does make writing a poem sounds so easy, taking only a brief pause in between each sentences."
            p "{i}Through twists and turns, the chief is no where to be seen, {p}goat village erupts in chaos.{/i}"
            p "{i}But he emerged, a journey in the damp cave, {p}a lump of moss and stone, it's the boss.{/i}"
            p "{i}So the wanderer fought, brave and wild. {p}Your eyes of fire dawned on the maddened spirit.{/i}"
            p "{i}Under the crumbling golem, he saved the chief, {p}with the heroic act it comes merit.{/i}"
            "His fingers dance on the lute, the music wrapping around the air like a gentle embrace."
            p "{i}The people of forest furnished the wanderer, {p}he's a courier of the village, but hero of the goat.{/i}"
            p "{i}He's an icon, a figure of inquisition. {p}For he has travelled far and wide, with his pride afloat.{/i}"

            $ pirkkasverses1 = []
            $ pirkkasverses2 = []
            if quest33.status:
                $ pirkkasverses1.append(_("A quest from the farm, {p}reveals the swindler from the plains, and the plums he tore."))
                if sharkbandit.win >= 1:
                    $ pirkkasverses2.append(_("He hid in sight, followed the thief, {p}and triumphed over the boss before."))
                else:
                    $ pirkkasverses2.append(_("He tracks him down, with ease and agility, the farm is safe once more."))

            if quest25.status:
                $ pirkkasverses1.append(_("Travelling citizens, attacked by a flowerless plant, {p}He followed Lothar, a challenge to the nature's wrath."))
                $ pirkkasverses2.append(_("Without a second, the evil plant fell, {p} the heroes returned on a victorious path."))

            if quest38.status:
                $ pirkkasverses1.append(_("Keen for building, he meets a logger bear, {p}an endeavor to mend the tie of two factions."))
                $ pirkkasverses2.append(_("He rebuilds the bridge, brick by brick, {p}a generous posture that no one expected."))

            if task03.completedtimes > 0:
                $ pirkkasverses1.append(_("A dangerous adventure, between the wheat field, {p}two rows of teeth lies beneath the ground."))
                $ pirkkasverses2.append(_("He challenged, overcome, and eventually, beaten, {p}For he is greater than a shark unbound."))

            if nocturnal_serve > 0:
                $ pirkkasverses1.append(_("A new server, in the tavern of Lusterfield, {p}he restores not only the duty, but the passion of service."))
                $ pirkkasverses2.append(_("Plates by plates, he delivered, {p}patron's favourites are he and his practice."))

            if len(pirkkasverses1) > 1:
                $ pirkkasversenum = renpy.random.randint(0, len(pirkkasverses2) - 1)
                $ pirkkasverse1 = pirkkasverses1[pirkkasversenum]
                $ pirkkasverse2 = pirkkasverses2[pirkkasversenum]
                $ pirkkasverses1.remove(pirkkasverse1)
                $ pirkkasverses2.remove(pirkkasverse2)
                p "{i}[pirkkasverse1]{/i}"
                p "{i}[pirkkasverse2]{/i}"

            if len(pirkkasverses1) > 1:
                $ pirkkasversenum = renpy.random.randint(0, len(pirkkasverses2) - 1)
                $ pirkkasverse1 = pirkkasverses1[pirkkasversenum]
                $ pirkkasverse2 = pirkkasverses2[pirkkasversenum]
                $ pirkkasverses1.remove(pirkkasverse1)
                $ pirkkasverses2.remove(pirkkasverse2)
                p "{i}[pirkkasverse1]{/i}"
                p "{i}[pirkkasverse2]{/i}"

            p "{i}In a fateful encounter, this wanderer meets with a graceful bard. {p}His curiosiiity intrigued this fortuitous tiger.{/i}"
            p "{i}A dance, a song, a ballad of ancient hero. {p}It was stolen by no one but the baneful bandits over.{/i}"
            p "{i}He barges in the bandit's den, a challenge no one feated, {p}the robbers and thieves all ran elsewhere.{/i}"
            menu:
                "Although it's a story, you didn't defeat all the bandits. Should you correct his inaccuracy?"
                "Correct the story":
                    e "Well, I didn't beat every bandits in their hideout, just sneaking the place."
                    p "Okay, it was all but pretty words mixed with some stories I've heard here and zere, but let me think of a better way."
                    p "{i}He sneaks in, past the glimpses of the ever-vigilant evilness, {p}an endeavor no one dared, but he did so for a total stranger.{/i}"
                "Ignore":
                    pause 1


            p "{i}Yet, the prose was not placed within, {p}instead it was basked in the very place where resides the wanderer.{/i}"

            p "{i}There, he invited the minstrel to the village he now lives. {p}A deal with his fellow, and the prose is back.{/i}"

            p "{i}The bard could not have forgotten, his face, his laughter, {p}and an affectionate heart, despite the courage of the pack.{/i}"

            p "{i}Now in this room, the wanderer's desireful eyes, {p}so let the lute speak, and the story shall be continued written.{/i}"


            "You lean your head forward, the distances between you two are mere inches now."
            "A mischievous smile playing on his lips as you get closer, he is almost anticipating what is coming."
            "But he doesn't stop singing."
            "You reach out, trying to grab Pirkka's face, but he nudges your hand out of it."
            p "Your laughter, a melody, your touch is a rhyme. In face of a performance, you never slack, a symphony of pleasure."
            "His smile widens, an enchanting wink from him just teases your heart more."
            menu:
                "Your body is boiling with insatiable heat right now, perhaps you should cool off, or take your advance on the bard who is clearly waiting for your move."
                "Take off his clothes":

                    call Scene_Pirkka_Show from _call_Scene_Pirkka_Show
                    $ pc.lust = 0
                    if timenow.hour < 12:
                        $ timenow.addTime(0,20-timenow.hour,57-timenow.minute)
                    else:
                        $ timenow.addTime(0,32-timenow.hour,57-timenow.minute)

                    jump main_nocturnaltrunk_upper
                "Back down":

                    p "{i}All along, you wander, your trail left on every inch of Mokken's soil.{/i}"
                    "Pirkka notices your distance has gotten further, but he doesn't bother."
                    p "{i}On the darkest night, the restless day, {p}the hopeless place, you show up, never foil.{/i}"

                    "Your attention is all focused on his music and the lyric. At least, you've never been praised like this before."
                    p "{i}Because he is the symbol of a hero, {p}a brave adventurer no one wish to stand in his way.{/i}"

                    p "{i}A foreign visitor, a traveller at heart, {p}he will flourish, by the blessing of this bard.{/i}"
                    "He points at himself, before bowing half-heartedly on the bed."
                    "You clap your hands loudly, admiring the entire performance from the beginning to the end."
                    p "How's it? Does it do you justice enough?"
                    e "I love it, though, I'm still not believing I'm actually qualified to be a hero here."
                    p "Every hero starts somewhere, I'll sing this song to the tavern regulars, and maybe add some polish and fantasy."
                    p "They'll soon think you're a hero regardless."
                    "You both grin brightly, before the room fall silent to the lack of music."
                    p "Well, you're happy, I'm happy. Again, this was just m' little gift for the prose."
                    p "Do you want to head out? I'm ready to play some more music for the tavern."
                    e "Sure."
                    "As such, he strums a few chords as usual, before leaving the room with you."
                    $ timenow.addTime(0,0,30)
                    jump main_nocturnaltrunk_upper
        "Maybe Later":



            $ pirkka_show_day = -timenow.day
            e "There's something else I need to work on, Pirkka."
            p "Okay, but I'm not leaving the village anywhere soon."
            "He shoots you a wide grin, before fiddling with his lute once more."
            jump main_nocturnaltrunk_upper

label Lothar_Prose_Ask:

    e "Hey, Lothar. Have you seen a prose?"
    l "Oh don't tell me you've talked with that stupid bard, disciple."
    e "W-what, Pirkka?"
    l "Yeah, stupid, annoying, totally ruins the vibe we've had in the Tavern with his supposed music to the ears."
    l "And no, I have not seen any Kantele, any prose, any paper in the existence of the entire Mokken."
    e "Did he piss you off?"
    l "I don't like how he talks, now the regulars in the trunk calls me 'Nocturnal Hunk' instead of 'Hero of Lusterfield', thanks to him."
    e "I think that fits you mor- I mean, uh... both are good."
    l "Ugh, anyway, no prose. I don't deal with the bandits so I have no idea how you get them to trade."
    e "Well, thank you anyway for letting me know."
    jump Lothar_Normal_Talk

label Sebas_Prose_Ask:

    e "Seb, have you seen a prose?"
    s "Hey roomie. What's the prose look like?"
    e "It's... a parchment, paper? There's a red ribbon with ancient markings on it."
    s "Well, I don't think I've had been pawned a prose lately. Last one was a few months before."
    e "There's a bard, Pirkka. Who are looking for the stolen prose."
    if quest26.status == True:
        s "Another friend of yours? How's the old Wuldon you've brought to us last time?"
        e "He's doing just fine."
    s "Well well, Mister Ole over there are always there reading books and whatnot."
    s "But he's not the thief type, though. So maybe you're looking at someone smaller."
    e "Thanks, Seb."
    s "Good luck with your friend."
    jump Sebas_Normal_Talk

label Rahim_Prose_Ask:

    e "Hello, Rahim. May I ask if you've seen any prose in Lusterfield?"
    "Rahim raises an eyebrow towards you."
    r "Prose?"
    e "Yeah. I suppose it's a ballad."
    r "What's it about?"
    e "It's about an old hero... who killed a monster or some sort. I've not read the whole thing yet."
    r "Old hero."
    r "Monster."
    "Rahim taps on his needle."
    "He stares on the floor for a while."
    r "I don't have the prose."
    e "Uhm... do you know about any other people with a prose?"
    r "Ole had one before, rolled. He showed it to me a while ago."
    "Rahim goes back to work once more, you're not sure if he has ended the conversation alltogether."
    e "Thanks, Rahim."
    "The bull gives you another glance, and nods as you leave."
    jump Rahim_Normal_Talk

label Amble_Prose_Ask:
    e "Hey, Amble, have you seen a prose? Or anyone that's interested in poems and ballads?"
    a "Oh, hey there, puny friend."
    "Amble scatches his chin."
    a "I- I don't think so. I've only been chopping wood around the village, and Jog's not the one to read."
    j "Maybe that lizard."
    "Jog exclaims from afar."
    j "Ole seems like the guy to read books, I've lived with him long enough."
    e "Oh?"
    a "Aha, I've heard him talk about collecting some paper as well, maybe he's your guy?"
    a "But Rahim, on the other hands tells stories that are good for bedtime, I think he reads a lot too."
    j "That's not poems, ya oaf."
    a "Oh!"
    "Amble brushes the back of his head."
    e "Well, thank you you two for the help, I'll go ask the others."
    a "Good luck to you!"
    jump Amble_Normal_Talk

label Ole_Prose_Ask:

    e "Ole, have you seen a prose?"
    show ole shocked with dissolve
    o "Uhm... prose?"
    e "Yeah. There's an ancient marking on a red ribbon that bounds the parchment."
    "Ole looks uncomfortable, he puts down the brush and slightly nudges on his dewlaps."
    o "Can we go to your room?"
    "Your cheeks instantly blush."
    e "It's in the middle of the day! I'm not ready-"
    o "It's something important."
    "The lizard leads you to your own room, he closes the door delicately before turning to you."
    scene bedroom with dissolve
    show ole stare with dissolve
    o "Uhm... well. Let's talk."
    e "Ole, why are we in this room?"
    o "Seb's not going to like what we're going to talk about."
    o "But first, why are you looking for the prose?"
    e "There's a bard, Pirkka. Who recently got stolen the prose from a bandit."
    "He sits on your bed, trying to close the windows shut."
    show ole normal
    o "I can't hide anything from you, can I?"
    o "His prose is upstairs."
    "You gasp in surprise, but Ole puts a finger in front of your mouth."
    o "[e], I don't take pride with dealing with bandits, but they've just found a work I've been collecting."
    e "Collecting?"
    o "I collected a lot of books, prose, all manuscripts, they're all right upstairs."
    "Ole sits close to you, you can almost smell his breath as he nervously speaks."
    o "It's been a while since I last bought... collected anything."
    o "It's really been a while, until I saw it in the alleyway. They'd been trying to get me to buy stuff for years."
    o "I didn't know what I was thinking, I bought the prose with 3000 gold. You must not tell Seb about this."
    e "T-that... that's a lot of gold, Ole."
    o "Not just about the gold, but I promised myself I'm not collecting anything like them ever again."
    o "I don't know what's going on, but ever since you came, I've not been the one who I was proud of being."
    "Ole exclaims, he seems much more fidgety than usual."
    e "Alright."
    o "The prose should go back to its owner."
    o "W-where's Pirkka?"
    e "He's in the Tavern."
    o "Let's go then. I should apologise to him personally."
    "The lizard pats your back, before you both get up from the room."
    scene sebasshop with dissolve
    show ole normal with dissolve
    "You look up as Ole tells the lion to take care of the shop for a moment."
    "Sebas stares at both of you with a puzzled look as Ole goes upstairs to retrieve the poem."
    s "Hey, buddy. What's going on with my big O?"
    s "Don't tell me he's done stuff in your room."
    e "Seb, it's nothing like that."
    s "Ha, you're just making me much more curious now."
    "Sebas pauses as Ole arrives with a side glance."
    s "Uhm, I see nothing."
    "The lizard gestures you to follow him."
    scene nocturnaltrunk with dissolve
    show ole normal with dissolve
    "And soon, you two arrive to the Nocturnal Trunk."
    "Inside the dimly lit tavern, you and Ole spots Pirkka sitting at a table in the corner, tapping on his lute on a certain beat."
    show ole stare at r1 with move
    show pirkka normal at l1 with move
    p "There you are, come here, my friend."
    "Pirkka points at you."
    p "And who's this fella over here?"
    e "He's Ole, we lived together in a shop nearby actually."
    "The bard notices the familiar parchment from Ole's hand."
    p "Greetings, dear Ole. I see you have something that belongs to me."
    o "I apologise, Pirkka. I didn't know it was yours. I can return the prose to you unscathed, with a bit of price."
    p "I'm willing to pay 1000 gold for its safe return."
    o "But, I can't let it go for any less than 2500 gold. It's a rare piece of literature, you know."
    o "And I bought it for 3000 gold, that 500 gold should cover for all your troubles."
    e "H-hey Ole, didn't we talk about this?"
    "You whisper as you grab Ole's arm tightly."
    o "I didn't tell you I'm letting it go for free."
    p "Fair, but [e] here went the trouble to retrieve the prose from the depth of bandit's den. 500 gold can't cover all that."
    p "1500 gold."
    o "2300, that should be the final price."
    p "How about 1700?"
    menu:
        "Ole remains silent, only staring at a confused Pirkka. And the bard looks at you instead."
        "Convince Ole to lower the price":
            $ pirkka_negotiate = True
            e "H-hey, Ole. Shouldn't you lower the price a little? You said you didn't want to collect them in the first place."
            o "That doesn't mean I'm not going for a better price."
            o "And I trust Pirkka here has the gold for it."
            "Pirkka smiles at Ole's statement."
            e "Ole, the prose was stolen."
            pause 2.0

            "It's only now that Ole's stare turns into some realization."
            o "..."
            o "Sorry, old habit."
            show ole normal with dissolve
            e "I thought Seb was the one that deal with the customers and all."
            o "Who do you think taught him all that."
            "The lizard chuckles."
            o "Yeah, I'm so sorry for pushing it, Pirkka. I'll take 1500 gold."
            p "Oh? You are so interesting, Ole. But thank you so much."
        "Remain Silent":



            $ pirkka_negotiate = False
            "You remain silent, waiting for the two men to settle the deal."
            p "Very well. 2250 gold it is."
            p "I've never paid for something this expensive, especially those that should've been mine."
            o "Sorry, but I bought it fair and square from a bandit."
            p "No need to apologize, you're not the one who stole the prose from me, if anything I should thank you for willing to give it back."


    "Pirkka gives Ole a pouch full of gold, and he's returned his prose."
    "Both of them stares at the item they have received, before they shake their hand."
    p "It's been a pleasure seeing you two, but I should store this precious artifact in a better place first."
    p "I'll be returning to the tavern soon enough, play the full ballad in front of you."
    p "May we meet again."
    "The bard flings his lute, and he leaves you and Ole with another simple tune."
    hide pirkka with dissolve
    "Ole nods, he pauses for a few moment before standing up."
    o "Kiddo, ready to go?"
    e "Yeah."
    "You stare at Ole, who only looks at you with a regretful glance."
    "Perhaps you now know him more than what he lets you see, you can only hope it's a good thing."
    e "Ole?"
    o "I'm sorry, [e], but I don't want to talk about this yet."
    e "Alright, I understand."
    o "It's all me, please don't blame yourself for what happened."
    e "I- I didn't."
    show ole understand with dissolve
    "Ole nods, he smiles at you before leaving the tavern as well."
    $ QuestFinish(quest35)
    jump main_nocturnaltrunk



label Bandit_Meet_Quest:
    hide screen menu_buttons
    "You hear wheat ruffling from afar, it sounds like it was from the plum tree..."
    e "The thief must be here... right now."
    "There's no doubt someone's here."
    "Immediately, You race through the grasses back to the plum trees. All the ripe plums you saw just a moment ago are gone. The thief has already taken them all."
    e "F-fuck, I have to catch him..."
    "You can still hear the muffled sound coming from your left, but you see another trail on the right, freshly stomped by someone."
    menu:
        "Where did the thief go?"
        "Towards Left":
            "You follow the shuffling noise, raising your ears to detect the source of the sound."
            "The sound doesn't fade away, instead it's kept constant as you approach."
            "You try to stay as quiet as possible, for the thief to not notice you."
            "Jog had taught you about stealth in one of your training, but you're not sure if you are ever experienced enough to tail a thief who's probably more skilful than you are."
            "But still, it had helped you figure out how to muffle your own noise."
            "You crouch, sneaking just below the small grass while the sound somewhere near you continues walking away from the farm."
            "Suddenly, you hear a loud cracking sound just below your right foot."
            with vpunch
            "C-CRACK!"
            "Without further glance, you accidentally step on a flail twig. And for a second, your heart sinks."
            "The pacing noise stops, perhaps someone has noticed your presence."
            "You are unsure if he has noticed you, but if he does, you'd think you're ready for a fight."
            "Something is awry, he might have already seen you and is thinking of the fastest way to escape."
            "You know which direction he is in, and with certain agility, you might as well be able to catch him."
        "Towards Right":
            "Perhaps the thief was the one that stepped on the stalks, you choose to follow the trails."
            "..."
            "Taking the faint footstep by the flattened plants, you walked for a while that the ruffled sound from the other side stopped."
            "You are still figuring out which direction it leads to, before noticing that as you go forwards, the trail seems to get more and more obscure, until it disappears at one point."
            "It leads to a muddy footstep that's facing your direction."
            "It was a dead end."
            "You look around one last time, just to make sure the thief is not nearby."
            "But eventually, you return to the farm empty handed, knowing that the plums are gone, again."
            jump main_grove_of_harvest
    menu:
        "What should you do?"
        "Chase after":
            $ bandit_sneak = False
            "You run after the thief, solely based on the direction of the sound."
            "The rash movement you've made immediately reveals your presence to him. Now standing tall, you can see a gray figure hidden in grass and flowers."
            rbd "S-shit."
            "You hear a hushed voice just in front of you."
            "The thief starts running away, he looks relatively small in size, and it seems he runs swiftly just like Jog does."
            "You speed up, draining all your energy just to catch a glimpse of the thief. but he doesn't slow down as well."
            if pc.agi > 7 or (pc.agi > 5 and renpy.random.random() > 0.5) or (pc.agi > 3 and renpy.random.random() > 0.75):
                "You try to run as fast as you can, and you manage to keep a constant distance between you and the thief."
                "And eventually, he loses stamina pretty quickly, and you closes distance with him bit by bit."
                "Suddenly, you lose sight of him."
                "Did he just, escaped? There's no way as he was just here seconds ago."
                "..."
                "There's no sigh of the thief, anywhere."
                "..."
                with vpunch
                "SMACK!"
                "Suddenly, an enraged rat just jumps in front of you."
                "There's no plum on his hands, instead you see daggers pointing towards you."
                rbd "Let's get over with it, fool."
                jump ratbandit_battle
            else:
                "You try to run as fast as you can, but... he is faster."
                "It doesn't take long before you lose sight of the thief."
                "You look around one last time, just to make sure the thief is not nearby."
                "But eventually, you return to the farm empty handed, knowing that the plums are gone, again."
                jump main_grove_of_harvest
        "Stay Still" if not isBandit:
            "You decide to stand still, not moving a single muscle or making a single sound."
            "Somehow, the farm is weirdly quiet for a few seconds. You know the thief is looking around, and you can only hope that he doesn't see you."
            "The twig underneath your foot is still making faint noise from any minor movement."
            "You can only lay your weight onto the other foot, waiting for the thief to continue on their way."
            "Something moved, you are sure that the thief has started moving around, perhaps he continues on his path, or perhaps he's trying to search for you."
            "You are not coping with the nervousness very well, sweat pours from the side of your head, moistens your fluffy beard."
            "And now that even a drop of sweat has become so noticeable in such a quiet place, there's really nowhere to hide."
            rbd "Must have been the... scarecrows."
            "The thief mutters softly to himself, you are sort of surprised how pleasant his voice sounds, even if you haven't seen his face yet, you still can't imagine the look of a thief with such a high-pitched cadence."
            "You are more certain that the thief has continued on his way now, you sigh a breath of relief silently, and you continue following the man."
            "This time you are a hundred percent careful, and certain that no twigs can make you fumble the mission now, so you ready your items and weapons, in case the target confronts you any time soon."
            "Luckily, he doesn't, he doesn't even seem to notice your presence, just walking forward, towards somewhere outside of the farm."
            "You wish to continue, but he's walking further and further away from Jog and Arthur's territories. There's just too much uncertainty."
    menu:
        "Or. perhaps you should stay on the farm, and confront him next time he's stealing the plums again."
        "Stay in the farm":


            "You figured out that Jog and Arthur were right, there's no reason for you to venture outside the farm."
            "Plus, you may get caught out there, and no one could have helped you."
            "The thief doesn't even know he's being followed, perhaps another time you'll just catch him red-handed."
            "Regardless, you give up your pursuit and return to Lusterfield."
            jump main_grove_of_harvest
        "Follow the thief":
            $ bandit_sneak = True
            "You decide to follow him out of the farm, he still doesn't notice your presence in the farm, and by the way you sneak past the grass, you might be able to confront him when he takes a rest."
            scene prattlefell_meadow with dissolve
            "He walks out of the field very quickly, and you peek over, just to see who this grey figure really is."
            "You raise your head, from the back of the thief, he looks like... a rat, with a pair of round ears and thin tails."
            "He is covered in fur clothing, a leather mask and hard fabric covering his face."
            "Definitely someone that walks sneakily, just like Jog usually does."
            "Leaving the field, your means of camouflage is rendered obsolete, he is walking towards the green plains, and there's no way you can hide in plain sight..."
            "You decide to wait it out, just for the rat thief to walk far away from you, and you tails him loosely, often taking advantage of small hills as cover."
            "And luckily, he doesn't ever turn back, just tossing his stolen plums around like a circus show."
            "You continue walking for a long time..."
            pause 2.0
            scene bandits_hideout with dissolve
            "Soon, the thief arrives at a large hideout. He casually moves inside, looks around and closes the door."
            "There're flags just floating around the stone building, with dried red paint all over the cloth."
            "No one's watching the door..."
            "You try to get close, listening in on whatever is happening inside."
            "..."

    sbd "Got the plums?"
    "You hear a gruff voice from the other side of the wall. It is certainly not from the thief you were following."
    rbd "Here are the plums, boss."
    rbd "Almost got eaten alive by that scarecrow."
    rbd "I think the farmers noticed, I've heard footsteps coming back, maybe we shouldn't go there again."
    sbd "Who cares what they think- The hyena's got our back."
    "The hyena...? Was he talking about Jog?"
    sbd "I'm gonna beat your ass hard if you don't come back with a handful of plums next time."
    rbd "Yes, boss."
    "The bandit with a gruff noise begins chomping on the plums, making loud noises across the room."
    rbd "Where are the others?"
    sbd "We've got some drifters out there, they're handling them."
    rbd "Are they all gone? I didn't know we are on patrol today."
    sbd "Everyone else all knew, I just told you to get plums for me, clodhopper."
    sbd "Maybe if you stayed quiet and didn't spoil our plan last time I'd trust you with our shit."
    rbd "Boss! Last time was a mistake, I won't disappoint you again."
    rbd "I promise!"
    "You can hear a loud sigh."
    sbd "It's still early, you should join them."
    rbd "Do I get to keep my share of the gold?"
    sbd "Half the share."
    rbd "Yes, boss."
    "You hear the sound of the thief promptly leaving the hideout, and you quickly hide behind another wall before he sees you."
    "You sigh a breath of relief, and remember what his boss talked about... Jog. He wouldn't betray the farm's interest for them, right?"
    "And Jog was the one that got his plums stolen, he was the one that sends you on this mission in the first place."
    "There's no way he is complicit with a group of bandits."
    "But it does explain why he was so hesitant to share his information with you."
    if quest16.status == True:
        "But, what if Sebas was right about him?"
    "You're still pondering the possibility, but a window flying in your face snaps you out of the train of thoughts completely."
    with vpunch
    "SMACK-"
    pause 0.5
    "The window pane slaps you pretty hard, and you are not quick enough to react before the bandit boss peeks out of it."
    "A shark's face comes staring right at you, he is covered in leather armor, giving you a weird glance."
    sbd "Who the hell are you?"
    "It takes a few seconds for you to process that you've been caught, you are still pressing on the back of your head."
    menu:
        "What should you say...?"
        "I'm just passing by":
            e "I'm just passing by this place, taking off now."
            sbd "Not so easy."
        "You caught me":
            e "Well, you caught me... "
            sbd "I did."
        "I'm the new bandit recruit":

            e "I... uh... am new, bandit recruit, boss."
            if bandit_floor1.entranceCount > 0 or bandit_gangbanged > 0:
                "The shark squints his eyes."
                sbd "Hmm... you look like someone I've seen before..."
                e "Of course, it's because I'm the new recruit, boss."
                "Suddenly, the shark's eyes widen, feinting a smile of realization."
                sbd "N-no! Now I know, you're the adventurer that broke into our camp earlier! Think you can fool me?"
                e "U-uh... no I'm not."
            else:
                sbd "New? We haven't had any new recruits for a while."
                e "Did the others not tell you about me? I'm really good at taking... people's things, boss."
                "The shark looks at you with a face full of confusion."
                sbd "I don't recall any goats being a new recruit... well, you know what you should bring me... right?"
                e "Bring you?"
                "He points at his belly, and the surroundings."
                sbd "Everyone of us know."
                jump Bandit_Recruit_Shark
    "You prepare to run away from the bandit, but the shark just jumps across the window."
    "He lands right next to you, holding an axe over his shoulder."
    "You walk a few steps backwards, your body is trembling, the shark bandit is extremely bulky as compared to you."
    sbd "A walking bag of gold, huh?"
    sbd "Now, hand over everything, traveler."
    jump sharkbandit_battle
label Bandit_Recruit_Shark:
    menu:
        "What should you bring to the shark?"

        "Red Rose" if LookForItem("Red Rose", inventory):
            e "Here's your... rose, boss."
            sbd "The fuck is this?"
            sbd "You wanna propose or something?"
            jump Bandit_Recruit_Fail
        "{s}Red Rose{/s}" if not LookForItem("Red Rose", inventory):
            jump Bandit_Recruit_Shark
        "Raw Meat" if LookForItem("Raw Meat", inventory):
            e "Here's your meat, boss."
            sbd "Ugh, meat?"
        "{s}Raw Meat{/s}" if not LookForItem("Raw Meat", inventory):
            jump Bandit_Recruit_Shark

        "Blue Berry" if LookForItem("Blue Berry", inventory):
            e "Here's the blue berry you need."
            sbd "What?"
            e "What?"
            sbd "You're kidding."
            jump Bandit_Recruit_Fail
        "{s}Blue Berry{/s}" if not LookForItem("Blue Berry", inventory):
            jump Bandit_Recruit_Shark
        "Apple" if LookForItem("Apple", inventory):
            e "Here's the apple."
            sbd "That looks like the plums I have here."
        "{s}Apple{/s}" if not LookForItem("Apple", inventory):
            jump Bandit_Recruit_Shark
        "Iron" if LookForItem("Iron Ingot", inventory):
            e "Here's your iron, boss."
            sbd "What's this, you think I'm a smither?"
            jump Bandit_Recruit_Fail
        "{s}Iron{/s}" if not LookForItem("Iron Ingot", inventory):
            jump Bandit_Recruit_Shark
        "100 Gold" if pc.gold >= 100:
            e "Here's the gold, I have 100 of them, boss."
            sbd "T-that's a pathetic amount of gold."
            jump Bandit_Recruit_Fail
        "{s}100 Gold{/s}" if pc.gold < 100:
            jump Bandit_Recruit_Shark
        "Cashmere" if LookForItem("Cashmere", inventory):
            e "Here's the cashmere you need, boss."
            sbd "What the fuck is the use of these."
            e "It's for knitting, boss."
            sbd "You think I'm here to fucking knit a sweater for you like an old grandma?"
            jump Bandit_Recruit_Fail
        "{s}Cashmere{/s}" if not LookForItem("Cashmere", inventory):
            jump Bandit_Recruit_Shark
        "Nothing":
            e "Uh... Sorry B-boss... I do not have anything ready, yet."
            sbd "Nothing?"
            "The shark scratches his chin, his impatient look is beginning to worry you."
            sbd "Well that means you don't know shit about us then."
            "He lands right next to you, holding an axe over his shoulder."
            "You walk a few steps backwards, your body is trembling, the shark bandit is extremely bulky as compared to you."
            sbd "A walking bag of gold, huh?"
            sbd "Now, hand over everything, traveler."
            jump sharkbandit_battle
    sbd "Whatever, it looks fresh red, that's good enough."
    e "Fresh red?"
    sbd "Yeah, red food. Did you not know what you were bringing?"
    e "Uh... yes of course, red food, right. I love blood, and stealing people's hard-earned food!"
    e "May I ask whose are the blood on the flags outside?"
    sbd "Blood? We don't do blood here."
    sbd "It's food paint, we're not killing travelers left and right just to paint these fucking flags."
    sbd "But they do scare off a few of those pesky local heroes trying to prove their worth."
    sbd "Also, why are you asking?"
    e "Uh, just curious, boss."
    sbd "Suspicious, but well. You've passed my test, which is the official one, not the riddles those goons been doing."
    e "Thank you, boss."
    sbd "Now, go out and patrol, or whatever you were doing."
    sbd "Don't stand here again. Next time I open the window it's gonna smash your face in."
    sbd "And bring me some red food when you get them."
    e "Got it, boss."
    "The shark returns back inside the hideout, he casually sits on the table with the newly acquired plums and other food."
    "You stare at the bandit boss, he's just munching down on the food like you're not here."
    "But he quickly picks up on your glare."
    sbd "Get lost, meathead."
    "You take your leave, and run away as fast as you can. The shark doesn't seem to mind that though."
    "..."
    "What just happened...? Everything happened so quickly..."
    "Are you a bandit now? That doesn't sound like a proper bandit initiation, but to be honest, you aren't sure how bandits are recruited either."
    "He does seem to believe you are a bandit..."
    "Perhaps you can return here later to see if the shark recognised you..."
    "It... would be extremely unlikely that you'd willingly return here though."
    "...and."
    "Plums. You still haven't stopped the thief, yet. Perhaps you'd have to catch him red-handed later."
    "..."
    "You return to the farm with thoughts about the bandits along the way."
    $ isBandit = True
    jump main_grove_of_harvest

label Bandit_Recruit_Fail:
    e "B-boss n-no...I-"
    sbd "You're clearly either deaf or aren't my bandit."
    sbd "In both case you're dead!"
    e "..."
    sbd "Dead-f..."
    jump sharkbandit_battle

label Keepsake_Lothar_Gnoll:
    hide screen menu_buttons
    stop music fadeout 1.0
    "As you touch the flute, your vision suddenly darkens as new memories flood your mind."
    scene black with dissolve
    "..."

    scene lusterfield_range with dissolve
    "Jog lounged atop a pile of hay, twirling his flute absentmindedly, his gaze distant."
    show amble normal at l1 with dissolve
    a "This is a death wish, Lot. You cannot go through with it."
    "Lothar, perched on a tree stump, waved off the warning with a grin."
    show lothar normal at r1 with dissolve
    l "Don't underestimate me, Amble. I'm the hero of Lusterfield! A few bandits won't stop me!"
    "The wolf declared, his voice was brimming with confidence. Amble rose from the wall, shaking his head."
    a "That's the problem, Lot. We're not in Lusterfield anymore. If they catch you off guard for even one second, I don't know who can even save you."
    l "You worry too much, Amble. I will easily make them pay for what they did to our village."
    l "The villagers looked up to me, did you know how much they fawned over me after I said it'd be an easy job?"
    l "I can't let them down after that. Plus, those bandit are just a few stealing thieves, what can even go wrong?"
    "Amble sighed, he tried to reason with Lothar, but he couldn't find a word."
    l "Hey, Jog, you coming or what?"
    "Lothar turned away from the big guy to face the lounging hyena."
    "They briefly exchanged a gaze, and Jog leaped onto the fence, spinning the flute once more before tucking it into his belt."
    j "Sure... You'll need me to scout anyway, so let's get this done before the night comes."
    "Lothar grinned, his eyes gleaming."
    with vpunch
    l "I knew you'd come through! If only Amble here would stop being such a fucking prick."
    l "Guess we'll leave without you then, Amble. Us two will handle this the grown-men way, and maybe we'll even bring you back a piece of that shark meat."
    "Amble shook his head, he opened his mouth briefly, but Lothar is already walking away from the village."
    show lothar at r2 with move
    a "Jog, this isn't safe. You know that, right?"
    show amble at c1 with move
    "The logger called out to Jog, who was already halfway to the gate."
    "Jog turned, blocking Lothar's view, and whispered in the bear's ear."
    j "Trust me, Amble. I'll keep him safe. He won't ever set foot inside that bandit fort."
    j "Not ever..."
    "Jog put on his devious smile, before turning around and catching up to Lothar."
    show black with dissolve

    scene prattlefell_meadow with dissolve
    "The two set off toward the bandits' hideout, trodding past the green grass up the hills."
    show jog normal at l1 with dissolve
    j "So, Lothar."
    j "What's your master plan when we reach their place? Charge in, sword swinging, and hope for the best?"
    "Jog twirled his bow between his fingers."
    show lothar chuckle at r1 with dissolve
    "Lothar laughed, striding on the tall grass confidently."
    l "Something like that, Jog. I know they're not expecting us, and I can take them by surprise."
    l "You'll be my eyes and ears, right? Make a distraction while I slip in and take down their boss."
    "He clapped a hand on Jog's shoulder, nearly knocking him off balance."
    "The hyena scowled silently."
    j "Is this the famous origin of the Hero of Lusterfield? Sneaking into the most guarded camp without getting caught?"
    show lothar grin with dissolve
    l "Exactly! I'll take their leader's head, and the rest will scatter like rats."
    j "Oh, right. You must be somehow walking stealthier than I do."
    "Jog couldn't help but furrowed his brow awkwardly. This was all too reckless, even for Lothar. But he played along nonetheless."
    "On any other day, he would laugh in front of Lothar's face, and tell him how stupid he was."
    "But this time, the wolf was stubborn enough to go through with it, and it made him utterly irked."
    "Jog sighed, his eyes scanning the horizon. The green meadow stretched out before them, a sea of swaying weed."
    "They are not far from the bandit's camp now, the only thing between them was the vast plain of Prattlefell."
    j "I'm going to scout ahead."
    with vpunch
    l "Wait-"
    j "Just stay here Lot. It won't be long."
    show jog normal at l2 with move
    "Before Lothar could respond, Jog had already slipped away into the tall grass, his form quickly disappearing from view."
    show lothar bored with dissolve
    l "Now I'm stuck here waiting... great!"
    "Lothar stood alone on the path, tapping his foot impatiently, his hand resting on the hilt of his sword."
    l "How dare he allowed a hero like me to wait for him, what a witless brat."
    show lothar at c1 with move
    pause 0.5
    "As the hero continued to rant, Jog climbed a nearby tree, using its branches to get a better view of the surrounding."
    "He crouched low, peering through the leaves to spot any signs of the bandits, but all he could see was the endless expanse of grass."
    "A grin spread across his face as he spotted something else, a flicker of movement in the distance."
    j "There they are."
    "Jog glances at the clueless wolf standing alone amidst the tall grass, his fingers brushed the flute at his belt, and he pulled it free."
    "He brought it to his lips, hesitating for a moment, then, softly, he began to play."
    "Slowly but surely, a long, grueling whine could be heard, as if it was a wild creature's calling to his mates."
    "Lothar's ears perked up at the strange, yipping sound. He raised his head, trying to locate the source."
    l "Jog?"
    show lothar at flip
    pause 0.5
    show lothar at flipback
    "His claws unsheathed, sword tightly held in hand, eyes darting as he searched for any sign of danger."
    "The yipping grew louder, more frantic, and Lothar's heart raced. He could feel the tension in the air, the anticipation of a fight."
    l "Who's there? Show yourself."
    "Jog hid behind the leaves, he watched Lothar's every move as he put away the flute."
    "It was dangerous to put his own friend in a situation like this, but Lothar was too reckless, too stubborn to listen to reason, he thought."
    "Maybe this will teach him a lesson."
    show lothar at r1 with move

    show gnoll at l1 with dissolve
    "Soon, a group of gnolls followed the voice of the flute to the clearing, their eyes locked on to the hero wolf."
    show lothar angry with dissolve
    l "What the- Where did yall come from?"
    l "No matter, just a few small fries like you won't stop me!"
    "He roared, readying himself for battle."
    "The gnolls stared at him intently, saliva dripping from their maws."
    "The leader gnoll stepped forward, his eyes fixed on the wolf before it."
    gnl "Need help, pup?"
    "He growled, and Lothar's eyes widened in shock."
    with vpunch
    l "Who are you calling a pup, damn it! I am the mighty Lothar, hero of Lusterfield!"
    "The gnolls laughed, pointing at the annoyed face of Lothar."
    gnl "Lotta? Gnolls know lotta folks, but no know such name."
    "They growled menacingly, circling around him."
    "Lothar backed up slowly, keeping a wary eye on them."
    l "Such arrogant beasts... Fine, have it your way!"
    "He unsheathed his sword, ready to fight back."
    gnl "Gnolls' way?"
    "The leader gnoll chuckled, and the rest of them jeered amongst themselves."
    gnl "We chase Lotta."
    show gnoll at r2 with move
    "Suddenly, the gnolls scattered, disappearing into the tall grass."
    l "What the hell are these little wimps doing?"
    "He muttered, unsure of what to do next."
    show lothar angry at c1 with move
    l "Show yourselves, evil creatures! Fight me like a real man."
    "He shouted, but there was no response."
    "He felt a chill run down his spine as he realized that he was truly alone, facing a group of wild gnolls that seemed to be playing a dangerous game with him."
    l "You guys better watch out, this is not a joke, I am going to-"
    with vpunch
    "Lothar couldn't finish his sentence as he felt something poking his ass."
    l "Ouch! What the..."
    "He turned around and saw a gnoll, laughing at him."
    gnl "Haha... Lotta no like that?"
    "It taunted, and Lothar turned red with anger."
    l "I will make you regret that!"
    with vpunch
    "He shouted as he swung his sword at the wild hyena, but another gnoll appeared, swatting his sword away."
    gnl "Not so fast, pup."
    "It snarled as the sword toppled on the ground."
    call Scene_Lothar_Gnoll_Keepsake from _call_Scene_Lothar_Gnoll_Keepsake
    $ pc.lust = 0
    j "Lot, I'm back!"
    show jog normal at r2 with dissolve
    show jog normal at r1 with move
    "Jog called, shaking Lothar awake."
    show lothar naked at l1 with move
    j "Almost didn't make it back alive, those damn bandits found me, and I had to lead them on a wild chase."
    "The hyena yawned, stretching his arms."
    with vpunch
    l "What, it's been hours! Where were you? You left me alone out here!"
    "Lothar snapped, rubbing his eyes."
    j "Sorry Lot, but you know how it is. Can't let the bandits catch me, can I?"
    "Jog shrugged, lying down next to him."
    j "So, were you waiting this whole time... naked?"
    "He teased, nudging Lothar with his foot. Lothar scowled, looking away."
    l "None of your business."
    "He mumbled, standing up and gathering his clothes."
    j "...Fine then, shall we continue to the bandit camp? I'll be extra careful this time around."
    "Jog asked, grinning. Lothar shook his head, putting his clothes on."
    l "No way, that's it for me. I'm going home."
    show lothar at l2 with move
    "He declared, heading back towards the village."
    show jog at c1 with move
    j "Aw, come on! Don't let those bandits get the best of you!"
    "Jog called after him. But Lothar didn't reply, he just kept walking, leaving his friend behind."
    "The hyena watched him go, laughing softly to himself as he noticed the wet stain on the back of his pants."
    j "Gotta clean that up later..."
    "He whispered softly, sheathing the flute into his pocket."

    return

label Ribba_First_Show:

    scene travelling_carousal_night with dissolve
    "A considerable crowd has gathered all around the carousal. Drinks and snacks are being passed around, the air thick with the smell of roasted meat, spiced ale, and festival excitement."
    "At the center of the tents stands a large makeshift stage, lit by floating orbs and flickering bonfires. In the middle of it, a short, hooded rabbit stands proudly, cape billowing even though there's barely any wind."
    show ribba normal at sihoulette with dissolve

    rb "Welcome, welcome everyone, to the grand opening of Ribba's Ribald Magic Show!"
    show ribba normal at c1 with move
    rb "Tonight, your twitchy little host will dazzle you with the most wondrous, the most marvelous, the most downright lewd feats of magic you've ever seen!"
    "The rabbit's voice is surprisingly loud for his size, carrying easily across the meadow. Despite his height - or maybe because of the cheeky confidence - he commands the entire crowd's attention, yours included."
    show ribba normal at normal with dissolve
    "You stand near the back, craning your neck to get a better view as he begins waving his wand with theatrical sweeps."
    rb "For my first trick... I shall make this very wand disappear right before your eager eyes!"
    "With a dramatic flourish, he snaps his fingers."
    rb "Boof!"
    with vpunch
    "In an instant, the wand vanishes from his paw."
    "The crowd gasps, then erupts into applause. You find yourself clapping along as Ribba takes a low, exaggerated bow, ears flopping forward."
    rb "Not bad, eh? But we're just warming up!"
    show ribba tease at flip
    show ribba at l1 with move
    pause 0.5
    show ribba at flipback
    show ribba at r1 with move
    "He grins wide, showing a flash of sharp little teeth."
    rb "Next! I shall conjure dozens of the juiciest carrots... straight from the depths of my mysterious hood!"
    "The rabbit opens his mouth wide-impossibly wide-and reaches in with both paws."
    show ribba lick at flip
    show ribba lick at c1 with move
    "You watch, half in disbelief, half in morbid fascination, as he pulls out one long, glistening carrot... then another... then another."
    with vpunch

    with vpunch
    "They're slick, coated in saliva, dripping slightly as they pile up on the stage in a messy, suggestive heap."
    with vpunch
    "The crowd cheers louder. A few whistles pierce the air, someone in the front row laughs nervously."
    crowd "Was that... actually in his throat the whole time?"
    crowd "No way. It's gotta be hidden somewhere inside the hood, maybe?"
    crowd "I don't even care anymore. Keep going!"
    "You can't look away. The carrots keep coming, each one wetter than the last, until the pile is almost comically obscene."
    "Ribba finally stops, wiping the saliva off his mouth theatrically with the back of his paw."
    show ribba tease at flipback
    rb "See? Magic should always leave you a little... moist."
    "The laughter is louder now, edged with hungrier guffaws."
    "He continues through several more tricks - cards that flutter out of his ears and land on volunteers' laps, illusory contours that traces his plump hips under the thin costume."
    "And a silk scarf that ties the rabbit tightly against the wall, as it teasingly flutters between his thighs all by itself."
    "With each act, the cheers grow rowdier. More drinks are downed. And voices start calling out."
    crowd "Show us something really spicy, bunny!"
    crowd "Come on, Ribba! Give us the good stuff!"
    "Ribba pauses mid-bow, ears perking straight up. His grin turns sly."
    show ribba normal with dissolve
    rb "Oh-ho? My lovely crowds are feeling frisky tonight, aren't they?"
    "He hops to the edge of the stage, leaning forward, voice dropping into a teasing purr that still somehow carries to the back."
    rb "I hear you. I do. But a magician's got to save the really naughty bits for the encore..."
    rb "Can't show all my tricks up the sleeves so soon, after all."
    "He winks directly toward the thicker part of the crowd, though you swear his eyes flick toward you for half a second."
    "The murmurs rise, excited and impatient."
    "Still, he straightens up, cape swirling dramatically."
    rb "That's the end of tonight's main show! Thank you all for coming - and for coming so loudly!"
    with vpunch
    "The crowd roars with laughter and applause. A few people surge forward, kneeling at the stage edge, reaching up to touch his fluffy feet or the hem of his cape."
    "Ribba jumps back, swatting their hands away with mock scandal."
    show ribba tease with dissolve
    rb "Ah-ah! That's not included in today's show! It could be in the next one, maybe."
    "He gives one last flourishing bow, then hops off the back of the stage in a puff of glittering smoke."
    hide ribba with dissolve
    "The crowd slowly disperses, buzzing with chatter and half-drunken theories about how he did it. Some linger near the stage, hoping for one last glimpse."
    "Soon, you find yourself almost alone in front of the now-quiet platform. The floating orbs dim. Only the crackle of dying bonfires and distant festival music remains."
    "The short rabbit magician is nowhere in sight... but you can still smell the remnant of his salacious scent, lingering in the air."
    "You wonder if he's already preparing for the next show he teased about."
    jump main_travelling_carousal

label Ribba_First_Encounter:
    "The rabbit magician is collecting some of his props from the ground, as you approach him."
    show ribba normal with dissolve
    rb "Oh-ho! What's this I spy with my twitchy little eye? It's a stranger who wanders in the yonder."
    show ribba tease
    rb "You, yes, you. Are you lost? No matter, come hop closer and help me grab that thing."
    "The rabbit gestures to a small pouch lying on the tall shelf. It was right on the edge, but the short rabbit couldn't seem to reach it."
    e "Yeah, sure. Need a lift?"
    "He crosses his arms, looking up at you with a frown."
    rb "I'm not stooping that low to get a lift, tallie! Just a hand."
    menu:
        "What do you do?"
        "Help him":
            $ ribba_dialogues["Help Reach"] = True
            e "Yeah, sure."
            show ribba smile
            "You step forward, and reach for the pouch. It was surprisingly easy."
            "It was a small leather bag, with a fake pocket inside that seems to be bottomless. You scratch your head as you hand it to the rabbit below."
            rb "Boof! Saw my little secret there, didn't you."
            "The rabbit snatches the pouch from you slickly."
            rb "A magician never reveals his tricks, but since you happen to catch it in a happy little happenstance, we'll call it even then."
            e "What's even?"
            rb "Why, you help me out, and in return, you've seen my little trick."
            e "Little trick for a little guy, what does that make me? Two gold?"
            rb "Hey! Stop with your stupid short jokes."
            e "S-sorry! I'm just kidding alright."
        "Decline":
            $ ribba_dialogues["Help Reach"] = False
            e "Sorry, I'm in a hurry."
            show ribba cry
            rb "Wait no, hey! Don't be a rude little rutabaga now, wouldn't ask ya if I've got arms longer than my legs."
            show ribba sus
            e "Nah..."
            "You watch as the rabbit sighs as he hops a few times more, just barely reaching the pouch."
            rb "Not in a hurry to watch me stumble, huh? Fine, fine. You teensy little tease."
            "The rabbit grumbles, before he climbs on his own wand and leaps up high enough to grab it. He lands back on the ground with a thud."
            show ribba tease
            rb "How's that? Still got it, don't I?"
            "You clap lightly."
            e "That's impressive for your-"
            show ribba sus
            rb "Hey, don't call me short! I know you're thinking that!"
            e "No, I wasn't."
            "The rabbit huffs, crossing his arms."
            rb "Sure you weren't. I know what you're thinking."
            e "I wasn't. Swear."
            "He stares at you with squinting eyes, until a grin spreads across his face again."
    show ribba lick
    rb "Anyway, I'm Ribba, the greatest magician in all of the land!"
    "Ribba spreads out his arms. A wide grin on his hooded face."
    rb "And you are..."
    e "I'm-"
    show ribba tease
    rb "No, no. Don't tell me. I knew I knew. Yes- oh yes. You are..."
    rb "You are [e], right? And a busty courier from the lusty Lusterfield, a must-see, I must say."
    "The rabbit winks at you, and you feel your cheeks flush."
    e "H-how do you know that?"
    show ribba smile
    rb "A magician's secret. Don't fuss about it."
    "After a pause, the rabbit feints a mischievious grin as he swirls his wand around the pouch."
    show ribba tease with vpunch
    rb "Oh, never mind. Fuss about it. Cause I've got your bad little Badge."
    show ribba at r2 with move
    show ribba at flip
    show ribba at l2 with move
    show ribba at flipback
    show ribba at c1 with move
    "The rabbit suddenly pulls out a small badge, and you recognise it immediately."
    show ribba smile
    $ removeAllItem("Courier Badge")
    if LookForItem("Courier Badge", inventory):
        e "That's... mine! How did you do that?"
    else:
        e "It wasn't even in my bag! Where did you get it?"
    rb "Like I said, magic..."
    if not ribba_dialogues.get("Help Reach", False):
        rb "It's a good thing you didn't help me, or else I would feel bad about it."
        e "Hey! Give that back to me."
        "You reach for the badge, but the rabbit pulls it back quickly."
    else:
        show ribba tease
        e "Hey! Give that back to me."
        rb "Even though you helped me, you tallies are still due a proper lesson."
        e "What's a tallie?"
        rb "A tall little tease like you, of course."
        e "I-I'm not even that tall! Have you seen anyone else back in the village?"
    show ribba lick
    "The rabbit chuckles, shaking his head."
    rb "Now, now. Don't be hasty. I can give it back to you, but only if you do something for me first."
    rb "You see, my audience, I didn't know they're so... excited about the show, horny, to be concise."
    show ribba smile
    rb "They wanted to see more of me, and I can't just let the show become all about my cock, can I?"
    rb "So, I'll need someone to prepare some props for me. A sweet little treat with fleet footwork."
    $ ribba_dialogues["First Encounter"] = True
    menu:
        rb "You look like you fit the bill, [e]. What do you say?"
        "Agree":
            e "Sure, I can help you out."
            jump Ribba_Prop_Quest_Accept
        "Decline":

            $ ribba_dialogues["Prop Quest Known"] = True
            e "Sorry, I can't help you right now."
            show ribba sus
            rb "Oh... I see. Well, that's a shame. I'll keep your badge safe though."
            e "What? No, I want it back."
            rb "Sorry, can't do that."
            e "Why not?"
            show ribba smile
            rb "Well, I can't very well give it back to you if you don't help me out, can I?"
            "You grumble under your breath, before leaving the stage to the magician."

    jump main_travelling_carousal

label Ribba_Dialogue:
    "You see the magician, busy moving around the stage for the performance ahead."
    show ribba normal with dissolve
    if ribba_dialogues.get("Broken", False):
        jump Ribba_Broken_Dialogue
    elif quest46.status == False or quest46.status < 4:
        rb "Psst! Hey, you! About to ask me something?"
        e "O-oh, you've caught me."
    elif ribba_dialogues.get("Master", False):
        rb "Ah, my dear little toy! Ready for another day of work?"
        e "Yes, master."
    else:
        rb "Oh, my assistant, inquisitive as always. Back for more questions, yes?"
        e "Yeah, I had a few things to ask you."

    jump Ribba_Normal_Talk

label Ribba_Normal_Talk:
    $ chosen_prop = ribba_dialogues.get("Chosen Prop", None)
    $ available_devices = ribba_dialogues.get("Available Devices", [])
    if ribba_dialogues.get("Broken", False):
        rb "Yes, master. What do you need?"
    else:
        rb "Quick, quick. What's on your mind?"
    menu:
        "Accept Ribba's Prop Quest" if quest46.status == False and ribba_dialogues.get("Prop Quest Known", False):
            e "Actually, Ribba, you know... I can help you out with the props."
            jump Ribba_Prop_Quest_Accept
        "Ask about the Carrot Prop" if quest46.status == 2 and LookForItemNumber("Carrot", inventory) < 6:
            jump Ribba_Prop_Quest_Ask_Carrot
        "Perform in Ribba's Show" if isNight() and len(ribba_dialogues.get("Available Shows", [])) > 0:
            jump Ribba_Magic_Show
        "Report about the Carrot Prop" if quest46.status == 2 and LookForItemNumber("Carrot", inventory) >= 6:
            jump Ribba_Prop_Quest_Report_Carrot
        "Accept being Ribba's assistant" if quest46.status == 3:
            e "Alright, Ribba. After a bit of thinking... I'm ready to be your assistant."
            jump Ribba_Prop_Quest_New_Prop_Begin
        "Choose a prop device" if quest46.status == 4 and not chosen_prop and len(available_devices) != 0:
            e "[ribba_title!t], I think I'm ready to choose a prop."
            jump Ribba_Prop_Quest_Choosing_Devices
        "Ask about the Quest as his assistant" if quest46.status == 4 and chosen_prop and not LookForItem(chosen_prop, inventory):
            jump Ribba_Prop_Quest_Ask_Device
        "Ask about the needed prop" if quest46.status == True and chosen_prop and not LookForItem(chosen_prop, inventory) and chosen_prop in available_devices:
            jump Ribba_Prop_Quest_Ask_Device
        "Report about finished Device" if quest46.status == 4 and chosen_prop and LookForItem(chosen_prop, inventory):
            jump Ribba_Prop_Quest_Report_Device
        "Report about finished Device" if quest46.status == True and chosen_prop and LookForItem(chosen_prop, inventory) and chosen_prop in available_devices:
            jump Ribba_Prop_Quest_Report_Device
        "Help create other devices for his show" if quest46.status == True and len(available_devices) != 0 and chosen_prop not in available_devices:
            if ribba_dialogues.get("Broken", False):
                e "More devices for the show?"
            else:
                e "[ribba_title!t], are there any other devices that you want me to help make?"
            jump Ribba_Prop_Quest_Choosing_Devices
        "Ask about his Magic skill":
            jump Ribba_Ask_Magic
        "Ask about the empty hood" if ribba_dialogues.get("Broken", False) and ribba_dialogues.get("Broken Magic Learned", False):
            jump Ribba_Ask_Hood
        "Ask about learning Magic" if not ribba_dialogues.get("Broken", False):
            jump Ribba_Ask_Learning
        "Ask How he's doing":
            jump Ribba_Ask_How_Doing
        "That's all for now":
            e "That's all I wanted to ask. Thank you, [ribba_title!t]."
            if ribba_dialogues.get("Broken", False):
                rb "Yes, master. I'll be here."
            else:
                rb "Anytime, anytime."
            jump main_travelling_carousal
    jump Ribba_Normal_Talk

label Ribba_Magic_Show:
    e "[ribba_title!t], I'm ready for the show."
    $ available_shows = ribba_dialogues.get("Available Shows", [])
    if ribba_dialogues.get("Last Show Day", -1) >= timenow.day:
        show ribba tease
        rb "Oh, are you now? Well, well. I've planned for a solo show tonight."
        rb "Can't very well have you stealing my spotlight every day, can I?"
        e "Well... what I am supposed to do now?"
        rb "Watch in the crowd, if you wish, or do something else. You can perform tomorrow."
        jump main_travelling_carousal
    elif callInventoryItem("Assistant Costume", "Clothes"):
        rb "Wait. Wait... where is your costume? To whom will you perform, without your costume, I assume no one?"
        e "Oh... right. I forgot to bring it with me."
        rb "Hmph. Go get it then. I can't have you performing without your proper attire."
        jump Ribba_Normal_Talk
    else:
        if ribba_dialogues.get("Show History", False) == False:
            if LookForItem("Assistant Costume", inventory):
                rb "Wait. Wait... where is your costume?"
                e "H-here! Here!"
                rb "Oh, do you mean for me to put them on for you...? I did promise that... but never did I figured you'd dare."
                e "Y-yes, [ribba_title!t]. Please."
                "The magician sighs, he signals you to the chair, and begins to strip off all your clothes."
                "With a slick motion, your bare body is exposed to the open air, and the rabbit brushes his hands all over your fur."
                "He grabs the pairs of the glove and tightly wraps them around your wrist."
                "Then, he takes the corset, and laces it up tightly around your chest, making sure to accentuate your figure."
                rb "Lookie there, are you shy now all of a sudden."
                "His hands occassionally brushes against your member, and he wouldn't hesitate to give it a light squeeze."
                rb "Hmm, nice and hard, just how I like it."
                "With experienced hands, he puts thigh-high socks on your legs. Around your neck, he fastens a tie, completing the look."
                "Finally, the rabbit adjusts the rubber corset around your crotch, making sure it was snug and secure while accentuating your plump chest."
                rb "There, all done. How do you feel?"
                e "A bit... tight. Isn't it a bit restrictive? I don't think I can move very naturally, or even at all."
                rb "Well, that's the perfect news - you don't."
            else:
                rb "Look at you, all dressed up and ready to go."
                e "Y-yes, [ribba_title!t]."
                rb "How do you feel? All tight and snugly, I bet."
                e "I feel tight, yes. The rubber around my crotch... it's like it's squeezing it, just like my chest, they feel so heavy."
                rb "Good, good. That's how it's supposed to feel."
            rb "Now stop wasting any time and come get prepared for the show."
        else:
            if LookForItem("Assistant Costume", inventory):
                rb "Right, right, then put on the custume altogether will you?"
            else:
                rb "Look at you, all dressed up and ready to go."
        "The rabbit signals you to the drawing board, with the available props lying around."

        menu:
            rb "Which show shall we do tonight?"
            "Portal Ring" if "Portal Ring" in available_shows:
                $ ribba_dialogues["Magic Show"] = "Portal Ring"
                if ribba_dialogues.get("Broken", False):
                    rb "Ribba bows his head and waits for your cue."
                call Scene_Magic_Show_Portal_Ring from _call_Scene_Magic_Show_Portal_Ring
            "Growth Potion" if "Growth Potion" in available_shows:
                $ ribba_dialogues["Magic Show"] = "Growth Potion"
                if ribba_dialogues.get("Broken", False):
                    rb "Ribba bows his head and waits for your cue."
                call Scene_Magic_Show_Growth_Potion from _call_Scene_Magic_Show_Growth_Potion
                $ pc.lust = 0

            "Bondage Box" if "Bondage Box" in available_shows:
                $ ribba_dialogues["Magic Show"] = "Bondage Box"
                if ribba_dialogues.get("Broken", False):
                    rb "Ribba bows his head and waits for your cue."
                call Scene_Magic_Show_Bondage_Box from _call_Scene_Magic_Show_Bondage_Box
                $ pc.lust = 0
            "Command Controller" if "Command Controller" in available_shows:
                $ ribba_dialogues["Magic Show"] = "Command Controller"
                if ribba_dialogues.get("Broken", False):
                    rb "Ribba bows his head and waits for your cue."
                call Ribba_Magic_Show_Command_Controller_Intro from _call_Ribba_Magic_Show_Command_Controller_Intro

                call Scene_Magic_Show_Command_Controller from _call_Scene_Magic_Show_Command_Controller
                $ pc.lust = 0
            "Maybe Later":
                e "You know what, maybe I should join the next one instead..."
                rb "Oh? Why...?"
                rb "Alright, don't tell me. I might get jealous. Come back when you're done with your side quests."
                jump main_travelling_carousal

        if quest46.status == 5:
            msg "Quest Finished! You gained a level up point! Check your inventory to distribute your points!"
            $ pc.lvluppt += 1
            $ QuestFinish(quest46)
            "You also gained 150 gold from performing in the show."
        else:
            "You gained 150 gold from performing in the show."
        $ pc.gold += 150
        if timenow.hour > 7:
            $ timenow.day += 1
        $ timenow.hour = 7
        if ribba_dialogues.get("Show History", False) == False:

            $ ribba_dialogues["Show History"] = []
        $ ribba_dialogues["Show History"].append(ribba_dialogues["Magic Show"])
        $ ribba_dialogues["Last Show Day"] = timenow.day
        scene travelling_carousal with dissolve
        "You wake up the next morning, at Ribba's tent."

    jump main_travelling_carousal

label Ribba_Prop_Quest_Ask_Device:
    $ chosen_prop = ribba_dialogues.get("Chosen Prop", None)
    if not chosen_prop:
        e "[ribba_title!t], about that prop you wanted me to make..."
        show ribba sus
        rb "Ah, still choosing, are we? Pick one properly first, then I'll do the nagging."
        jump Ribba_Prop_Quest_Choosing_Devices
    e "[ribba_title!t], about that prop you wanted me to make..."
    show ribba tease
    rb "Yes, yes. The prop. What about it?"
    e "What exactly do you want me to make again?"
    rb "Oh... "
    show ribba lick
    if chosen_prop == "Portal Ring":
        rb "The Portal Ring. I've given you the recipe haven't I?"
        rb "Be careful with these things, nothing happens with one single ring."
    elif chosen_prop == "Growth Potion":
        rb "A Growth Potion. I've given you the recipe haven't I?"
        rb "Just make sure you don't drink it, nothing will happen to you but it'll taste really bad."
        e "Then... [ribba_title!t], how would you grow bigger?"
        rb "Like I said, magic is an illusion. Don't fuss about the details."

    elif chosen_prop == "Bondage Box":
        rb "A Bondage Box. I've given you the recipe haven't I?"
        rb "Just make sure you make it the right size, you can't very well fit in a box that's too small."
        rb "Well, I guess you can try, but I don't think you'll like it when I ask my crowd to carry you around."

    elif chosen_prop == "Command Controller":
        rb "A Command Controller. I've given you the recipe haven't I?"
        show ribba sus
        rb "Just because I give you control... doesn't mean you should try to use it on me outside of the stage, g-got it?"
    e "Yes, [ribba_title!t]..."
    show ribba lick
    rb "Good, good. Now, get to work, I need that prop as soon as possible."
    jump main_travelling_carousal

label Ribba_Prop_Quest_Report_Device:
    $ chosen_prop = ribba_dialogues.get("Chosen Prop", None)
    if not chosen_prop:
        e "[ribba_title!t], I've made the prop you wanted."
        show ribba sus
        rb "Which prop, exactly? You need to choose one first, my eager little assistant."
        jump Ribba_Prop_Quest_Choosing_Devices
    e "[ribba_title!t], I've made the prop you wanted."
    show ribba lick
    rb "You have? Yes, oh yes. Let me see, let me see."
    "You hand the prop to the rabbit, who inspects it closely."
    show ribba tease
    if chosen_prop == "Portal Ring":
        rb "Ah, splendid! It's perfect!"
        show ribba smile
        "The rabbit says as he duplicates the ring with ease. Pulling a ring over his arm, it quickly appears out of the other portal."
        rb "Now, you should be able to use this on stage, excited?"
        "You nod."
    elif chosen_prop == "Growth Potion":
        rb "Oh my, it's the potion I've wanted."
        show ribba lick
        rb "No one is gonna call me short after drinking this."
        "The rabbit takes a sip of the potion, and you watch as he grows in a bit of size."
        rb "I can feel it, my meat is going to be huge! You'll see when we're on stage!"
    elif chosen_prop == "Bondage Box":
        rb "Yes, yes! Such an elegant little box."
        show ribba lick
        rb "Perfect size for a goat toy like you!"
        rb "You just need to hop in, and put your tight little pucker over that hole, I'll take it from there."
    elif chosen_prop == "Command Controller":
        rb "Oh! The controller! Such a great design."
        e "Should we... test it a bit?"
        show ribba sus
        rb "W-wait, don't use it on me yet. I'll keep it, until we're both on stage."
        "You nod."
    show ribba smile
    rb "Thank you, my dear assistant. You've done well."
    show ribba lick
    if quest46.status == 4:
        rb "Now, I think it's time for you to become my official assistant."
        rb "We will be performing together from now on, and I expect you to be ready for it."
        e "Y-yes, [ribba_title!t]."
        rb "Good, good. Now, just come back to me at night, and we'll make a great showing with this nice prop here."
        $ quest46.status = 5
        $ quest46.qComp(_("Perform a show with Ribba"))
        $ ribba_dialogues["Available Shows"] = [chosen_prop]
    else:

        rb "Now we have another routine together added to my pockets, yes! The audience is going to love it."
        e "Yes, [ribba_title!t]. I'm sure they will."
        rb "Good, good. We can choose which one we'd want to perform now. Such a good idea, this is going to make a great scene with the crowd."
        $ ribba_dialogues["Available Shows"].append(chosen_prop)
    if chosen_prop in ribba_dialogues.get("Available Devices", []):
        $ ribba_dialogues["Available Devices"].remove(chosen_prop)
    $ ribba_dialogues.pop("Chosen Prop", None)
    jump main_travelling_carousal

label Ribba_Prop_Quest_New_Prop_Begin:
    show ribba lick
    rb "Yes, yes! That's the spirit!"
    rb "Now, an assistant like you must be properly dressed for the occasion."
    show ribba tease
    rb "Here, take this, you'll need to put them on for my show."
    $ addItem("Assistant Costume", inventory, 1)
    "The magician hands you a few pieces of black and white cloth."
    e "Oh, that... doesn't look like a lot of fabric."
    show ribba sus
    rb "What else do you want, little tallie, you're here to get the crowd riled up, while I perform my trick."
    show ribba lick
    rb "You must put them on before stepping foot on my stage, or... I will put them on for you."
    rb "Speaking of which, I reckon, an assistant should obey his magician whenever the show is on..."
    show ribba sub
    rb "Oh Yes! Yes! You shall address me as Master from now on."
    menu:
        e "I... calling you master?"
        "Agree":
            $ ribba_dialogues["Master"] = True
            $ ribba_title = _("Master")
            e "A-alright, master. I'll follow your order."
            rb "Good, good. Little assistant. That's right."
        "Decline":
            $ ribba_dialogues["Master"] = False
            e "No! I'm your assistant, not your servant. We should be seen as equal partners if you want me to work for you."
            "The rabbit raises his open palms in surrender."
            show ribba sus
            rb "E-equal? Fine, fine. Call me Magician, or Ribba as you wish... No need to shout like you own the place."
    rb "Now, to the crux of the matter, we need a new performance routine! Something for the crowd to ogle about."
    show ribba tease
    rb "I've had several ideas, but none of them I've had the materials to craft..."
    rb "That's where you come in, my dear assistant. You will gather the materials I need, and prepare them for me."
    "The magician shows you a few stacks of notes, each pile a blueprint for a new prop and device."
    "He flips through them, showing you the sketches and designs."
    $ ribba_dialogues["Available Devices"] = ["Portal Ring", "Growth Potion", "Bondage Box", "Command Controller"]
    $ quest46.status = 4
    jump Ribba_Prop_Quest_Choosing_Devices

label Ribba_Prop_Quest_Choosing_Devices:
    $ ribba_dialogues.pop("Chosen Prop", None)
    $ available_devices = ribba_dialogues.get("Available Devices", [])
    if len(available_devices) == 0:
        rb "Looks like we're out of new blueprints for now. A tragic day for innovation, yes."
        jump Ribba_Normal_Talk
    if quest46.status == True:
        if ribba_dialogues.get("Master", False) and not ribba_dialogues.get("Broken", False):
            rb "Yes, yes, I have more shows to perform, with my little toy."
        else:
            rb "Of course, which of the remaining catches your eyes here?"
    else:
        if ribba_dialogues.get("Master", False):
            rb "So, my little toy, choose wisely."
        else:
            rb "So, which prop do you prefer, partner?"


    menu:
        "Portal Ring" if "Portal Ring" in available_devices:
            $ ribba_dialogues["Chosen Prop"] = "Portal Ring"
            e "That one looks interesting."
            show ribba lick
            rb "Ah, yes. A classic. With these rings, I can fix it around any part of your body, and it'll poke out on the other side."
            e "A-any part?"
            rb "Well, not any part, I can't teleport your insides out. No, ha-... just kidding."
            e "Is this even safe?"
            rb "Very. Oh, don't even worry, my dear. You'll feel everything on the other side."

        "Growth Potion" if "Growth Potion" in available_devices:
            $ ribba_dialogues["Chosen Prop"] = "Growth Potion"
            e "What about this, the growth potion?"
            show ribba lick
            rb "Oh, this recipe is special, with it I can finally be as big as I'd like, not that I'm not already big..."
            show ribba smile
            rb "This way, I can finally get revenge on those tallies, all 'em bullies who tried to mock my height."
            rb "...who will be played by you, of course."
            "You gulp nervously, on the blueprint it depicts a very huge Ribba... and a bite size... you."
        "Bondage Box" if "Bondage Box" in available_devices:
            $ ribba_dialogues["Chosen Prop"] = "Bondage Box"
            e "What's the use of this box?"
            show ribba tease
            rb "Oh, this is no ordinary box, its size is perfectly fit for your body only. leaving marginally no space inside."
            rb "Just hop in, and try your best to fit in, you'll be packed like a compact size, easy-to-carry suitcase that you are."
            e "What's that hole down there then?"
            show ribba lick
            rb "Well, obviously a traveller would have pent up urge needing to release, so all they need is to insert his cock into this hole of you."
        "Command Controller" if "Command Controller" in available_devices:
            $ ribba_dialogues["Chosen Prop"] = "Command Controller"
            e "This one doesn't even look like anything I've seen before."
            show ribba tease
            rb "Because it's my design! Well, due to the popular demand of my dear crowd, I... I might be subjected to this little gadget's control."
            rb "If you make this, I'll give the ownership of this device to you. B-but only for the purpose of the performance only."
            e "Alright, but what does this one do actually?"
            show ribba sub
            rb "It's a device to control one's mind. To make him do anything as the owner wishes."
            e "A-anything?"
            show ribba sus
            rb "I have to preface this, this is all illusions, just a performance. I do mind, if you control my mind outside of the stage..."
        "I'll think about it":
            show ribba sus
            e "I'll think about it."
            rb "Well, well? Don't sleep on it, whatever that prop is, that is."
            jump main_travelling_carousal

    menu:
        rb "So?"
        "Choose this device":
            e "Okay, I'll make this one."
            show ribba smile
            $ chosen_prop = ribba_dialogues.get("Chosen Prop", None)

            if chosen_prop == "Portal Ring":
                rb "So, the Portal Ring it is then."
                $ discoveredrecipe.append(portalringrecipe)
                $ quest46.qComp(__("Craft the Portal Ring"), chosen_prop, 1)
            elif chosen_prop == "Growth Potion":
                rb "Right, my next performance will be the Growth Potion."
                $ discoveredrecipe.append(growthpotionrecipe)
                $ quest46.qComp(__("Craft the Growth Potion"), chosen_prop, 1)
            elif chosen_prop == "Bondage Box":
                rb "A Bondage Box, alright."
                $ discoveredrecipe.append(bondageboxrecipe)
                $ quest46.qComp(__("Craft the Bondage Box"), chosen_prop, 1)
            elif chosen_prop == "Command Controller":
                rb "Ah, the Command Controller... interesting."
                $ discoveredrecipe.append(commandcontrollerrecipe)
                $ quest46.qComp(__("Craft the Command Controller"), chosen_prop, 1)
            else:
                rb "Wait. Which one did you mean again? Choose a prop first, then we can make it official."
                jump Ribba_Prop_Quest_Choosing_Devices


            rb "Great, then I shall give you the recipe you need. And you'll prep my prop."
            "The magician explains as he hands you the blueprint, detailing the ingredients required."
            if ribba_dialogues.get("Master", False):
                e "Yes, master."
            else:
                e "Alright, I'll be back with everything you need."
            rb "On you go then, shoo shoo."
        "Take a look at the others":

            e "How about the other ones?"
            rb "Be my guest!"
            jump Ribba_Prop_Quest_Choosing_Devices
    jump main_travelling_carousal

label Ribba_Magic_Show_Command_Controller_Intro:

    rb "Yes, yes. The Command Controller. A very special little prop for a very curious crowd."
    rb "And one that makes me a touch nervous, nevertheless."
    scene travelling_carousal_night with dissolve
    show ribba normal with dissolve
    "Backstage, Ribba turns the metal device over in his paws, checking each button and crystal with unusual care."
    "It is small enough to fit in one hand, but it looks far more serious than Ribba's usual props."
    show ribba sus
    rb "Now lend me those ears of yours, assistant. Once the show begins, this little gizmo only works on me while I'm on stage."
    rb "For two hours, it listens to the one holding it. After that, boof, I'm back to my usual self."
    e "So no matter what happens during the show, you'll snap out of it after two hours?"
    rb "Exactly. I'm not stupid enough to let you take me over for the rest of time."
    rb "And, I've curated a set of acceptable commands for you. Anything outside of those are forbidden."
    "Ribba exhales slowly, ears drooping for a moment before he squares his shoulders again."
    rb "Still... while it's humming along, if you press a command, I will have to follow through."
    rb "So keep that clever little head of yours clear, and stick to the script."
    e "Doesn't it sound a little dangerous, still?"
    show ribba tease
    rb "Yes, yes, but a magician who never risks a thing is just a juggler with a prettier cape."
    show ribba normal
    rb "More importantly, keep those eyes peeled for the bars when the act begins. Three of them."
    rb "My Willpower, my Lust, and Hype. Those are tonight's little scorecards, if you will."
    e "Alright."
    show ribba sus
    rb "And listen carefully here. Do not let my Willpower drop to zero. No jokes on that one."
    rb "If that bar empties out, bad things may happen, and I'd rather not find out how bad in front of a paying audience."
    e "You think it could actually go that wrong?"
    rb "I have no idea what's gonna happen, but I don't wanna find out."
    show ribba tease
    rb "My Lust bar should be obvious enough, yes? The higher it climbs, the closer I'm getting to cum. Simple, simple."
    e "That is not simple at all."
    show ribba smile
    rb "No, but it is exciting, so stay close and let me do the talking until it's time for the demonstration."
    e "Right. You start with the intro, and I watch the bars once the controller is live."
    rb "Exactly."
    "You take your place near the curtain while the carousal fills with onlookers."
    "Bonfires crackle, drinks are passed between paws, and a low hum of anticipation rolls through the grounds."
    "Ribba steps into the light with his usual flourish, cape swishing behind him."

    scene black with dissolve
    pause 1
    scene travelling_carousal_night with dissolve
    show ribba normal at c1 with move
    rb "Welcome back, my lovely lads! To another Ribba's Ribald Magic Show!"
    "The audience answers with cheers, whistles, and eager laughter."
    rb "Tonight's finale is not just magic trick or illusion, or even my naturally impeccable stage presence."
    show ribba tease
    rb "No, tonight we explore something far more mysterious: control."
    "He raises the device above his head. Its crystals catch the firelight, sending thin glimmers over the faces in the front row."
    crowd "What's that thing?"
    crowd2 "Looks expensive. Or dangerous."
    rb "Ah-ah, insightful. This, my dear audience, is tonight's special little prop."
    rb "And rather than spoil the trick, I'd much rather show you what it can do."
    "The reveal earns a fresh wave of anticipation, and the crowd leans in all the same."
    show ribba at flip
    show ribba at l1 with move
    rb "And because every good experiment needs a brave and charming assistant..."
    show ribba at flipback
    show ribba at r1 with move
    rb "I have brought my own dear helper to the stage once again."
    "He gestures for you to step forward."
    show ribba at flip
    show ribba smile at c1 with move
    rb "And because I am feeling especially generous, reckless, and confident tonight, I shall be the one under its effects."
    crowd "You're letting him control you?"
    crowd2 "No way. He's bluffing."
    rb "Maybe I am. Maybe I'm teasing and acting. That's why you're all here, isn't it?"
    show ribba at flipback
    "Ribba circles around you once, making a show of inspecting your stance while keeping the controller visible to the audience."
    rb "Now then, no peeking behind the curtain. My assistant and I will handle the fiddly bits, and you lot can focus on being properly amazed."
    rb "We'll begin with something simple. No more stalling."
    "The crowd quiets as Ribba lifts one thumb over the controller's top button."
    show ribba tease
    rb "Eyes forward. Let's get on with it."
    scene black with dissolve
    "Ribba's first command begins at once, and the audience leans forward in perfect silence."

    return

label Ribba_Prop_Quest_Ask_Carrot:
    e "About the carrots you wanted, where should I get them?"
    show ribba sus
    rb "Carrots, yes. Fresh carrots, I wonder..."
    "The magician ponders as he strokes his invisible chin under the hood."
    show ribba lick
    rb "Aha, the dark forest! That's where the best carrots grow, yes! Juicy, crunchy, and sweet."
    rb "You can find them just inside, somewhere where the caproots grow. Pick'em up or fight'em."
    e "Got it, I'll head there now."
    rb "Wonderful! Also, in case you were wondering, I did not pull those carrots out of thin air."
    "He winks."
    jump Ribba_Normal_Talk

label Ribba_Prop_Quest_Report_Carrot:
    e "Ribba, here's all the carrots you need."
    "You pull out 6 carrots from your bag, and hand them to the magician."
    show ribba lick
    rb "Great, Splendid! These will do just fine."
    e "Are you sure 6 is enough, last time I saw, you pulled out... at least 30 ones from your mouth."
    rb "Oh, don't you worry, I can always duplicate them with my magic."
    show ribba tease
    "The magician covers the carrot in his hand, and with a snap of his fingers, the amount of carrots on the top suddenly doubles."
    rb "There you go, now I have enough for the show."
    rb "Here, take your badge back, and a little something extra for your trouble."

    e "Well, thank you, Ribba, I was worried you were about to have me go on another errand."
    show ribba smile
    rb "Nonsense, nonsense. You did well, [e]."
    "The magician hands you back your courier badge, along with a small pouch of coins."
    $ removeItem("Carrot", inventory, 6)
    $ addItem("Courier Badge", inventory, 1)
    $ pc.gold += 300
    show ribba lick
    rb "Now, this is where the show gets exciting. You see, I need a proper propper to help me with... getting my audience excited."
    rb "So I was thinking, maybe I might as well get an assistant for the show. Someone with a nice pair of chest and balls."
    rb "What do you say, [e]? Care to join me on stage?"
    menu:
        "Accept":
            e "S-sure, why not. It sounds fun."
            jump Ribba_Prop_Quest_New_Prop_Begin
        "Decline":

            $ quest46.status = 3
            $ quest46.qComp("Return to Ribba")
            e "I think I'll pass, Ribba. I'm not really cut out for performing."
            show ribba sus
            rb "Oh... I see. Well, maybe some other time then."
            rb "Anyway, I don't think I'll bother finishing your quest... yes, that quest on your journal will always stay unfinished..."
            show ribba tease
            rb "But at least you can keep the badge and the money."
            e "W-what? You don't have to do that."
            rb "You can always come back, any time for sure, if you've changed your little mind."
    jump main_travelling_carousal


label Ribba_Prop_Quest_Accept:
    rb "Yes, yes! You're such a doll, [e]."
    show ribba tease
    rb "Now, listen closely. For the every performance I can show, I'll need some proper props propped by you, the propper."
    show ribba lick
    rb "But first, for our first step, you'll need to bring me some carrots. The juicer the better."
    rb "Bring them to me, and I'll give you your badge back, plus a little something extra for your trouble."
    e "Alright, I'll get them for you."
    rb "Wonderful! I'll be waiting here, show will start at night, so don't take too long now."
    e "I won't. See you later, Ribba."
    rb "On you go! Chop Chop!"
    "You turn around and leave Ribba to himself."
    $ QuestBegin(quest46)
    $ quest46.qProgress(__("Collect 6 Carrots"), "Carrot", 6)
    jump main_travelling_carousal

label Ribba_Ask_Magic:
    if ribba_dialogues.get("Broken", False):
        $ ribba_dialogues["Broken Magic Learned"] = True
        e "If I may ask, how did your magic come to be, Ribba?"

        show ribba sub with dissolve
        "Ribba lowers his head slightly, ears twitching with hesitation."
        rb "Oh... that truth, is it? Yes, yes. If master wants it, I'll tell it plainly."
        "His voice is soft and obedient, though a trace of his old theatrical lilt still clings to the words."
        rb "The past me would've hidden it behind a trick. But if you ask, I answer."
        rb "My magic... it isn't tricks. Not really."
        "He touches the center of his chest, right beneath the cloak."
        rb "A shard from the old war found me when I was young, and boof... that was that."
        rb "It didn't leave me as something plain and mortal after."
        rb "Since then, magic has sat closer to me than blood does."
        rb "The stage steadies it. Or steadies me. Hard to tell which is which now, especially when you're watching."
        rb "...When people watch, I feel more real."
        e "So the carrots, the floating crystals, everything...?"
        rb "Real enough to hold, or maybe taste. It was no illusions. The magic gives them shape... much the same way it gives me mine."
        "He hesitates again, his voice quieter now."
        rb "The magic can only last for a short while, if anything is to interfere, it would go very wrong in very different ways."
        "He bows his head gently, waiting for your reaction."
        rb "I've never told anyone else, but... for you, master, the words come easy."
        "You shudder, unsure how to respond."
        e "Uh... is that what caused you to be... so obedient?"
        "Ribba nods."
        rb "Was that enough? If you ask for more, I'll give it."
    else:
        e "If I may ask, how did your magic come to be, [ribba_title!t]?"
        rb "Gettin- curious, aren't you. Yes, yes. I like that."
        rb "Well. My magic, it's different from all those wanton wanna-be wand wavers out there."
        show ribba tease
        rb "It exists not in the wand, nor in the hat, but in the performance of the magician."
        e "It's... all performed?"
        show ribba lick
        rb "Yes! You can say it's all an illusion, one that feels real, even though you know it isn't."
        e "So, it's all just tricks? "
        rb "In a way, yes. But it's also about the experience, the emotions it evokes."
        e "But that's not real? Even the carrots that came from your mouth?"
        "The magician prods his arm into the void that is his face, and he swirls around as if nothing's in the hood."
        show ribba tease
        rb "If even you can't tell my tricks from reality, then what's the difference?"
        rb "Oh, little tallie, enjoy the show. Or better off, become a part of mine if you will."
    jump Ribba_Normal_Talk

label Ribba_Ask_Hood:
    e "Ribba... your hood. Why is there nothing where your face should be?"
    show ribba sub with dissolve
    "The rabbit goes still at once. One of his ears twitches, then lowers."
    rb "Ah... so master noticed it at last."
    "He lifts a paw, hovering near the dark opening of the hood without quite touching it."
    rb "This hood has held more of me than skin has for a long while now."
    rb "I used it for the act, again and again, until the magic decided the face I showed was the truer one."
    e "So there is really nothing there?"
    rb "There is. Just... not the kind of thing a proper little body ought to keep there."
    rb "If you need to know for certain, master... put your hand in and feel for yourself."
    "He tilts his head forward and stays perfectly still for you."
    "Carefully, you slide your hand past the edge of the hood."
    "There is cloth. Cool air. The faint prickling hum of magic through the lining."
    "At first there is only depthless emptiness, a void where his face should be."
    "Then something in it notices your touch, and the hollowness gathers itself around your hand."
    "It materializes as something impossibly soft, like warm velvet and down with no true shape beneath it."
    $ ribba_dialogues["Touched Hood"] = True
    e "There's a void in there... and then it just... formed around my hand."
    rb "Yes, yes. It knows when it's being touched. When I need one, the magic inside can materialize anything from it. When I don't... it stays hollow."
    "He folds his paws together, with a expectant grin on his face."
    rb "If it troubles you, master, I'll pull the hood low and hide it for you at once."
    e "No, it's alright, I don't mind it."
    jump Ribba_Normal_Talk

label Ribba_Ask_Learning:
    e "What's the magic that you are performing, [ribba_title!t]?"
    rb "Magic, my performance you say?"
    show ribba tease
    rb "A magician is nothing without his audience, and you know the secret behind a good magician?"
    rb "The folks barely cares about the tricks. It's all about the showmanship, the flair!"
    e "A-alright, and what about the tricks?"
    rb "Tricks? Oh, those are just little things I picked up along the way."
    rb "A routine, you'd need to grab a few tricks from your handbook."
    show ribba smile
    rb "Make things vanish, make things appear, maybe move it, or penetrate it, they're all the same tricks you'd show in different ways."
    rb "The real magic lies in how you present them, how you misdirect them from the real action behind the counter."
    jump Ribba_Normal_Talk

label Ribba_Ask_How_Doing:
    e "How are you doing, [ribba_title!t]?"
    if ribba_dialogues.get("Broken", False):
        if isNight():
            show ribba sub
            rb "I'm alright, master. Just doing the show for you."
            rb "I'll keep smiling until you want me closer."
        else:
            show ribba sub
            rb "Quiet, mostly. Just getting ready for the show later tonight."
            rb "If you want me before then, master, I'll be right here."
    else:
        if isNight():
            show ribba angry
            rb "Look at the crowd, little tallie. I'm performing!"
        else:
            rb "Well, I'm just preparing for a few tricks later tonight. Catch me there if you want to see."
    jump Ribba_Normal_Talk

label Ribba_Broken_Dialogue:
    if not ribba_dialogues.get("Broken Dialogue Seen", False):
        "Ribba notices you immediately. He stops what he's doing and turns toward you with calm, undivided attention."
        "His posture is meek and obedient, but the old showman spark flickers back to life the moment he sees you."
        rb "Oh... master. There you are. Call for me, and I come."
        "His voice is soft and submissive, but now warmed by the same theatrical sweetness he used to wear so easily."
        rb "Ask whatever you like. I'll give it gladly."
        e "...You really are different now, aren't you?"
        "You study him carefully. The confident, teasing rabbit you knew is nowhere to be found."
        rb "Yes. Different."
        "He answers without hesitation, no defensiveness in him at all."
        rb "Softer. Quieter. Better at listening."
        rb "When you look at me, I feel full. When you speak, I want to kneel and hear every word."
        rb "I love the stage... but I love serving you more, master."
        $ ribba_dialogues["Broken Dialogue Seen"] = True
    else:
        "Ribba turns to you at once, quiet and attentive."
        rb "Oh... master. Here again? Good."
    jump Ribba_Normal_Talk
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
