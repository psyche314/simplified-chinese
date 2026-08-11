define mage_patron = Character(_("Mage"), color="#8f4fbe", who_outlines=[ (2, "#000") ])
define merchant_patron = Character(_("Merchant"), color="#8f4fbe", who_outlines=[ (2, "#000") ])
define eater_patron = Character(_("Binge Eater"), color="#8f4fbe", who_outlines=[ (2, "#000") ])
define sneak_patron = Character(_("Sneaky Patron"), color="#8f4fbe", who_outlines=[ (2, "#000") ])
define sneak_patron2 = Character(_("Sneaky Patron"), color="#8f4fbe", who_outlines=[ (2, "#000") ])
define drunk_patron = Character(_("Drunkard"), color="#da7784", who_outlines=[ (2, "#000") ])
define pair_patron1 = Character(_("Dragon Patron"), color="#8f4fbe", who_outlines=[ (2, "#000") ])
define pair_patron2 = Character(_("Wolf Patron"), color="#8f4fbe", who_outlines=[ (2, "#000") ])

define fighter_patron1 = Character(_("Bull Wrestler"), color="#61463f", who_outlines=[ (2, "#000") ])
define fighter_patron2 = Character(_("Hyena Wrestler"), color="#cfac7d", who_outlines=[ (2, "#000") ])
define fighter_patron3 = Character(_("Coyote Watcher"), color="#d8b17e", who_outlines=[ (2, "#000") ])
define fighter_patron4 = Character(_("Watcher"), color="#92908b", who_outlines=[ (2, "#000") ])
define guild_patron1 = Character(_("Guild Member"), color="#8f4fbe", who_outlines=[ (2, "#000") ])
define guild_patron2 = Character(_("Guild Member"), color="#8f4fbe", who_outlines=[ (2, "#000") ])
define guild_patron3 = Character(_("Guild Member"), color="#8f4fbe", who_outlines=[ (2, "#000") ])

default drunkard = {"Encounter": 0, "Dialogue": 0, "Status": "None", "Beer Count": 0, "Ale Count": 0, "Ignore Count": 0, "Gold": 180}
label Trunk_Drunk_Dialogue:
    show trunk_patron_back2:
        xalign 0.303
        yalign 0.445
    $ drunkard["Encounter"] += 1
    if drunkard["Status"] == "Another Beer":
        if LookForItem("Beer", inventory) or LookForItem("Ale", inventory):
            drunk_patron "I'm still waiting for my beer, server!"
            e "There it is, enjoy."
            if not LookForItem("Beer", inventory):
                $ removeItem("Ale", inventory, 1)
                $ drunkard["Ale Count"] += 1
                "You hand him the ale, watching as he takes a long gulp from the mug."
                drunk_patron "Whatever... it's not beer, but it'll do... for now."
            else:
                $ removeItem("Beer", inventory, 1)
                $ drunkard["Beer Count"] += 1
                "You hand him the beer, watching as he takes a long gulp from the mug."
                drunk_patron "Ah... that's the stuff. Thanks, server. You're a good one, you are."
            e "You're welcome. Now, pay up, for the price of two beers."
            drunk_patron "Pay up? But... bu-"
            "You cross your arms, waiting for him to finish his sentence."
            drunk_patron "Fine... fine... it's not like I'm broke... here you go, server."
            "He hands you 40 coins, his hand shaking slightly as he does so."
            $ pc.gold += 40
            $ drunkard["Gold"] -= 40
            $ drunkard["Ignore Count"] = 0
            e "Thank you. Enjoy your drink."
            $ drunkard["Status"] = "None"
            return
    if drunkard["Status"] == "Waiting For Beer":
        drunk_patron "Where's my beer? I've been waiting for ages!"
        if LookForItem("Beer", inventory) or LookForItem("Ale", inventory):
            if not LookForItem("Beer", inventory):
                e "Here you go."
                if drunkard["Ale Count"] > 0:
                    "You hand him the ale, watching as he takes a long gulp from the mug."
                    drunk_patron "Whatever... it's not beer, but it'll do... for now."
                else:
                    drunk_patron "Ah-... wait... this isn't beer!"
                    drunk_patron "I asked for beer, not ale! I can't drink this!"
                    e "Beggars can't be choosers, you know."
                    drunk_patron "B-but... I... I can't drink this! I said I wanted beer!"
                    e "Take it or leave it."
                    drunk_patron "Fine... whatever..."
                    "He takes the ale from you, grumbling under his breath."
                    "You watch as he takes a sip, his face scrunching up in disgust as he swallows the bitter liquid."
                    drunk_patron "Ugh... what is this? It tastes like... like... uhh..."
                    "Ostensibly, he raises his mug to his lips and chugs down the rest of the ale, grimacing as he does so."
            else:

                e "Yeah, here you go."
                drunk_patron "Ah, finally! Beer... I thought you'd forgotten about me!"
                "You hand him the beer, watching as he takes a long gulp from the mug."

            if drunkard["Gold"] < 20:
                "He looks at you, his eyes wide with panic as he fumbles in his pockets."
                drunk_patron "I... I don't have enough... I... I... hic... I'm broke!"
                e "Uh... Is this another one of your tricks?"
                drunk_patron "No! No... I swear! I... I... I don't have enough! Look!"
                "He shows you his empty pockets, his hands shaking as he does so."
                e "You'll have to pay... or I'll have to let Cane know about this. He won't be happy about this."
                drunk_patron "No! No... don't tell the barkeep! I... I... I'll pay you back! I swear! I-"
                "His voice trails off as he looks around the tavern, before turning back to you with pleading eyes."
                "You can see the realization dawning on his face as he pulls out something from his pocket."
                drunk_patron "Here... take it... it's my amulet... it's worth... worth more than the beer!"
                "He hands you the amulet with gold inlay, nodding at you as you squint at the tiny etchings."
                e "What's this?"
                drunk_patron "It's... it's my old amulet... they said the storekeepers would give you discounts if you wear it..."
                e "This is worth more than the beer, you know."
                drunk_patron "I... I... I don't need it anymore... just... hic... just take it, server."
                "You take the amulet, nodding at him as you pocket the item."
                $ addItem("Haggler's Amulet", inventory, 1)
                $ drunkard["Status"] = "Broke"
                return
            elif drunkard["Beer Count"] + drunkard["Ale Count"] > 2 and renpy.random.random() < 0.5:
                drunk_patron "Here it is... hic... here it is... the money... ready for you, server."
                "He points on the table, feinting a drunken smile as he stare at you."
                drunk_patron "Look... this is a boon for being a good friend with me."
                "You take the 25 coins, nodding at him as you pocket the money."
                e "A boon for paying what you bought, you mean."
                drunk_patron "I'll take it as an approval."
                $ drunkard["Status"] = "None"
                $ drunkard["Ignore Count"] = 0
                $ pc.gold += 25
                $ drunkard["Gold"] -= 25
                return
            else:
                if not LookForItem("Beer", inventory):
                    $ removeItem("Ale", inventory, 1)
                    $ drunkard["Ale Count"] += 1
                    e "You're welcome. Now, pay up."
                    "You crosses your arms, watching him as he finishes the ale."
                    drunk_patron "Pay up? That wasn't... hic... that wasn't beer! I can't pay for that!"
                    e "You drank it, you liked it, so you pay for it."
                    drunk_patron "But... but... I didn't like it! It was... it was... hic... it was disgusting!"
                    "He looks at you with pleading eyes, the redness in his cheeks clearly betrays his fondness for the ale."
                else:
                    $ removeItem("Beer", inventory, 1)
                    $ drunkard["Beer Count"] += 1
                    drunk_patron "You're a good one, you are. I like you. You're... hic... you're my friend now."
                    drunk_patron "And... as my friend... you should know... I'm... I'm... hic... I'm broke."
                    "He looks at you with a sheepish grin."
                    e "You promised to pay me last time, remember?"
                    drunk_patron "I did? Oh... I did, didn't I?"
                    "You can see the realization dawning on his face as he tries to remember."
                    drunk_patron "I'm... I'm sorry. I'll pay you back my friend, I swear! Just... just give me another beer, okay?"
                    "He looks at you with pleading eyes, the beer in his hand is already almost empty."
            menu:
                "Bring him another beer":
                    e "Fine, but you have to pay for both's price."
                    drunk_patron "I will... now give me the beer... server."
                    "You shake your head as you pull back from the table."
                    $ drunkard["Status"] = "Another Beer"
                    return
                "Rebuke the drunkard":
                    e "I'm not giving you another beer until you pay me back."
                    drunk_patron "What? But... but... I'm your friend! Friends don't... hic... don't do that to each other!"
                    e "The barkeep won't be happy if you don't pay up, he certainly would've been happier to free up the table for someone else."
                    drunk_patron "W-what? Cane won't do that to me! I'm... I'm... hic... I'm his best customer!"
                    "He looks around the tavern, his eyes wide with panic."
                    drunk_patron "...fine. I'll pay you back. Just... just don't tell the barkeep, okay?"
                    "You stare at him, waiting for him to make good on his promise."
                    "He fumbles in his pockets and pulls out a few coins, handing them to you."
                    drunk_patron "Here. Take it, server. A-and a tip for your t-trouble."
                    "You take the 50 coins, nodding at him as you pocket the money."
                    e "Thank you. Enjoy your drink."
                    $ pc.gold += 50
                    $ drunkard["Gold"] -= 50
                    $ drunkard["Ignore Count"] = 0
                    "Grumbles and complaints can be heard as you walk away from the table, the drunkard's voice quickly fading into the background."
                    $ drunkard["Status"] = "Rebuked"
                    return
    if (drunkard["Status"] == "Waiting for Beer" or drunkard["Status"] == "Another Beer") and not LookForItem("Beer", inventory) and not LookForItem("Ale", inventory):
        "You look at the drunkard, shaking your head."
        e "I'm sorry, but I don't have any beer on me right now."
        drunk_patron "No beer? Then what are you doing here? You should be... should be... hic... serving me!"
        "The drunkard slams the bottles on the table, spilling some of the beer on the table."
        return

    if drunkard["Encounter"] < 4:
        if drunkard["Encounter"] == 1:
            "You approach the drunk patron, who is slumped over the wooden table, his head resting on his arms."
            drunk_patron "Mhmm... more beer..."
        elif drunkard["Encounter"] == 2:
            "The drunkard is now snoring loudly, his head resting on the table."
            drunk_patron "Hic... beer... whatever you've got... give me more of 'em."
        elif drunkard["Encounter"] == 3:
            "The drunkard mumbles incoherently."
            drunk_patron "More..."
        return
    "You walk up to the drunkard's table, the smell of alcohol hitting you like a wall."
    "He glances up. You can see the feeble attempts he has made by the furrowed eye brows he's making."
    if nocturnal_serve > 0 and drunkard["Status"] != "Rebuked" and drunkard["Ignore Count"] < 3 and drunkard["Beer Count"] + drunkard["Ale Count"] < 2:
        drunk_patron "I saw you before, you are the one who served me the beer! Mind if I have another one?"
        e "Sorry, but I am not working now."
        drunk_patron "You're not working? Then why are you here? You should be... should be... hic... serving me!"
        drunk_patron "Don't talk to me until you bring me another beer! I... I'll pay you."
        "The drunkard drools on the table, his eyes half-closed."
        drunk_patron "W-with tips..."
        menu:
            "Bring him beer":
                e "Okay, I'm off duty so I will buy from Cane directly, but you have to pay for my cut as well."
                drunk_patron "For what?"
                e "For the service, of course."
                drunk_patron "...fine. Just... just give me the beer, server."
                "You shake your head as you pull back from the table."
                $ drunkard["Status"] = "Waiting For Beer"
                return
            "Refuse":
                e "I told you, I'm not working now, you'll have to wait for the barkeep to serve you."
                "You watch as he grumbles under his breath, his eyes narrowing as he watches you walk away."
                $ drunkard["Ignore Count"] += 1
    else:
        $ drunkard["Dialogue"] = [renpy.random.randint(0, 5), renpy.random.random()]
        if sebas_drunk_day > 0 and drunkard["Dialogue"][1] < 0.5 and drunkard["Dialogue"][0] == 0:
            drunk_patron "I'm fine! I'm fine! I can drink more! I can drink more than anyone!"
            e "You reminded me of a friend of mine. He's a good friend, but he's a bit of a handful when he's drunk."
            drunk_patron "A good friend... no one's a good friend when they're drunk! They're all... all... hic... messed up."
            e "You're right. I'll leave you to your drink then."
        elif drunkard["Dialogue"] == 0:
            drunk_patron "You've ever heard of the... the... the... the tale of the dewdrop beer?"
            e "I can't say I have."
            drunk_patron "It's... it's... it's said that... that... hic... that the beer was made from the tears of a... a... scary werewolf!"
            drunk_patron "And... every day... on the earliest of mornings... you can find him weeping... weeping... hic... weeping for his lost love..."
            e "That's... quite a story. Did you make it up just now?"
            drunk_patron "No! No... I... I heard it from... somewhere... else... hic... I think."
        elif pirkka_location == "nocturnalupper" and drunkard["Dialogue"][1] < 0.33 and drunkard["Dialogue"][0] == 1:
            drunk_patron "That damn bard... he's... he's... hic... he's playing that song again!"
            "The drunkard points a finger upwards to the source of the music, his eyes squinting in annoyance."
            e "Which one?"
            drunk_patron "...the one about the... the... the... bastard or something."
            drunk_patron "You know what... now that I think of it, I could've been... been... hic... a bastard too."
            e "Oh, really?"
            "He nods, his head bobbing up and down as he does so."
            drunk_patron "Yeah... yeah... I could've been a bastard and not even know it! Can you... can you imagine that?"
            e "I can't imagine that, no."
        elif pirkka_location == "nocturnalupper" and drunkard["Dialogue"][1] < 0.66 and drunkard["Dialogue"][0] == 1:
            "The drunkard buries his head in his arms, his voice muffled as he sings."
            drunk_patron "{i}Kins turned foes,... hic... and the... king's... turned fool's.{/i}"
            "He raises the empty bottle to his lips, pretending to take a sip."
            drunk_patron "{i}Benea- thic... the palace floor, laid unto... hic the bereaved bastard boy!{/i}"
            "You listen as he follows the tune from the bard above, his voice cracking as he tries to hit the high notes."
        elif drunkard["Dialogue"][0] == 1:
            drunk_patron "This place used to be... used to be... hic... better back in my day. The beer was... was... was much stronger than this piss in my mouth!"
            e "What changed?"
            drunk_patron "I don't know! I don't know! But I'm... I'm... hic... I'm not happy about it!"
            e "About what?"
            drunk_patron "About... about... hic... the change! Now, it's all... uh... bad!"
            "You shake your head as you listen to him ramble on for a good minutes before slurring on his words again."
        elif drunkard["Dialogue"][0] == 2 and drunkard["Dialogue"][1] < 0.5 and drunkard["Encounter"] > 10:
            e "Say... you seem to be drinking a lot here, do you have a home to go back to?"
            drunk_patron "Home? Yeah I've got one, right in my... my... hic... my crotch!"
            e "That's not a great home to live in, you know."
            drunk_patron "What? You... you... you don't like my home? It's... it's... it's cozy! I'm sure you'll love it, friend."
            "He winks at you, hands gesturing to his bulging crotch as he does so."
            e "I think I'll pass on that offer."
            drunk_patron "Suit yourself! I have... I have... hic... plenty of friends who'd love to visit my home!"
            drunk_patron "You... you... you're missing out, friend! You're missing out on the best... the best... hic... the best time of your life!"
            e "I'm sure I am."
            "You shake your head as you walk away from the table, the drunkard's laughter echoing in your ears."
        elif drunkard["Dialogue"][0] == 2:
            drunk_patron "Just one more... just one more... hic... and I'm done, gotta go home and sleep it off..."
            drunk_patron "I swear... I swear... I won't drink again... until tomorrow! Haha!"
        elif drunkard["Dialogue"][0] == 3 and nocturnal_serve > 2 and drunkard["Dialogue"][1] < 0.5 and drunkard["Status"] == "Rebuked":
            drunk_patron "Bring me more beer... hic... serv-"
            "He stops mid-sentence, his eyes widening as he sees you approach the table."
            drunk_patron "You know what... I... I... I don't want any more beer... I... I... I'm good."
            e "Are you sure? You seemed pretty insistent on having more beer earlier."
            "The drunkard shakes his head, his hand waving you away as he does so."
            drunk_patron "I... I... I was? Oh... I... I don't remember that... I... I... hic... I must've been drunk."
            drunk_patron "Please don't kick me out of the tavern, server! I... I... I promise I won't cause any more trouble!"
        elif drunkard["Dialogue"][0] == 3 and nocturnal_serve > 2 and drunkard["Dialogue"][1] < 0.5:
            drunk_patron "Server, where is your apron... and your tray? You're... you're... hic... you're not working!"
            e "I told you I'm off duty, you'll have to wait for the barkeep to serve you."
            drunk_patron "Barkeep? I don't... I don't... hic... I don't want him to serve me! I want you to serve me!"
            drunk_patron "You... I've seen you under that apron before, you're... you're... hic... you're good at serving!"
            e "Uhm... thanks, I guess?"
            drunk_patron "Yeah! Yeah! You should put that mouth to good use and serve me under the table too! Haha!"
            "The drunkard points on the ground, his grin wide as he winks at you."
        elif drunkard["Dialogue"][0] == 3 and drunkard["Status"] == "Broke" and drunkard["Dialogue"][1] < 0.5:
            drunk_patron "Bring me more be-..."
            e "What were you saying?"
            drunk_patron "I... I... I'm broke! I... I... I can't pay for the beer! hic..."
            drunk_patron "I spent all my money on... on... hic... on the beer! I... I... I don't have any left!"
            e "You are still drunk, aren't you?"
            drunk_patron "I'm not! I'm not... hic... I'm just... just... a little... tipsy!"
            "He shoves his hand in his pocket, trying to look for something until he stares at you with a realisation."
            drunk_patron "Can you give... give me back the amulet? I... I... I need it back to earn more coins!"
            e "You gave it to me, remember?"
            drunk_patron "I... I... I did? Oh... I did, didn't I?"
            "The drunkard hides his head back in his crossed arms, his voice muffled the loud scream that would have deafened you."
        elif drunkard["Dialogue"][0] == 3:
            e "You should probably slow down, you're going to pass out soon."
            drunk_patron "You better not... hic... you better not tell me what to do! I can drink more than anyone in this tavern!"
            "You watch as he takes another swig of his beer, taking in a big gulp after another."
        elif drunkard["Dialogue"][0] == 4 and drunkard["Dialogue"][1] < 0.5 and nocturnal_serve > 0 and drunkard["Status"] != "Rebuked" and drunkard["Ignore Count"] < 3 and drunkard["Beer Count"] + drunkard["Ale Count"] >= 2:
            drunk_patron "Uhh... server... I... I... I need another beer... I... I... I'll pay you back!"
            e "Again, I'm not working now."
            drunk_patron "Not working? But... but... you served me before! You... you... hic... you have to serve me again!"
            menu:
                "Bring him beer":
                    e "Okay, I'm off duty so I will buy from Cane directly, but you have to pay for my cut as well."
                    drunk_patron "Uhm... okay."
                    "You shake your head as you pull back from the table."
                    $ drunkard["Status"] = "Waiting For Beer"
                    return
                "Refuse":
                    e "I told you, I'm not working now, you'll have to wait for the barkeep to serve you."
                    "You watch as he grumbles under his breath, his eyes narrowing as he watches you walk away."
                    $ drunkard["Ignore Count"] += 1
        elif drunkard["Dialogue"][0] == 4:
            drunk_patron "Hic! You're a fine lookin' one, a-a-aren't you?"
            "The drunkard slurs his words as he tries to focus on you. His breath reeks of alcohol."
            drunk_patron "Y-you ever seen a dragon... hic... with a beard?"
            drunk_patron "Swear I saw one just now! It was... was... right after my fifth ale. Or maybe it was the sixth..."
            e "Were you talking about me...?"
            drunk_patron "Huh? Oh, you're not a dragon... hic... are you?"
            e "Are you sure it's safe drinking all those beer, you look like you're on the verge of passing out."
        elif drunkard["Dialogue"][0] == 5:
            drunk_patron "You... you're a good listener, you know that? Not like the others... they... they don't understand me."
            e "I'm here to listen, what's on your mind?"
            "The drunkard looks at you with bleary eyes, his gaze unfocused."
            drunk_patron "You know... you know... I used to be... a-a-a great warrior... I fought... fought... hic... the goats..."
            "His voice trails off as he buries his face in his arms."
            drunk_patron "W-whatever... I don't care... give me another beer..."

    return

label Trunk_Eater_Dialogue:
    "You approach the imfamous regular in Nocturnal Trunk, the frog has been eating and drinking since you enter the tavern."
    "He looks up at you and smiles, his mouth full of food."
    eater_patron "You may want to check it out, friend. it's a stew that'll stick to your ribs and bones."
    eater_patron "Cane's got that recipe. It's a secret, but I can tell you that it's got a bit of everything in it."
    eater_patron "Mhmm... I'm drooling just thinking about it."
    e "You are eating the stew right now."
    eater_patron "Oh my apologies, I'm already thinking about the next one, mhmmmmmm..."
    msg "Work in Progress!"
    return

init python:
    def merchantProduct(inventory, amount):
        merchant_products = {}
        available_product = copy.deepcopy(inventory)
        for i in range(max(amount, 3)):
            product = renpy.random.choice(available_product)
            product.value = int(product.value * renpy.random.randint(14, 18) * 0.1)
            available_product.remove(product)
            merchant_products[product] = renpy.random.randint(1, 3)
        return merchant_products

default trunk_merchant = {"Restock Day": 0, "Restock Interval": 2, "Products": {}, "Bought Times": 0, "Level": 1}

label Trunk_Merchant_Dialogue:
    show trunk_patron_back1:
        xalign 0.268
        yalign 0.355
    $ selling_products = [redberry_item, blueberry_item, goldenberry_item, slaterock_item, cashmere_item, flax_item, reed_item, rosemary_item, feather_item]
    $ selling_products2 = [slimecrystal_item, apple_item, redrose_item, herbofgrace_item, hemp_item, iron_item, ginger_item, chrysanthemum_item, sage_item, hawthorn_item, hydrangea_item, mugwort_item]
    $ selling_products3 = [strap_item, clay_item, lodestone_item, chestnut_item, softfur_item, leatherstrips_item, snowberry_item, slimybone_item, chamomile_item]
    $ selling_products4 = [limestone_item, elderwood_item, vine_item, moonstone_item, coal_item, spearmint_item, archaicice_item, bearfur_item, hops_item]

    "You approach the hooded merchant and he looks up at you, hands holding a handful of coins."
    $ level = trunk_merchant["Level"]
    $ all_products = selling_products.copy()
    if level >= 2:
        $ all_products.extend(selling_products2)
    if level >= 3:
        $ all_products.extend(selling_products3)
    if level >= 4:
        $ all_products.extend(selling_products4)
    if trunk_merchant["Restock Day"] < timenow.day:
        $ trunk_merchant["Restock Day"] = timenow.day + trunk_merchant["Restock Interval"]
        $ trunk_merchant["Products"] = merchantProduct(all_products, 2+int(level/1.5))
    if sum(trunk_merchant["Products"].values()) <= 0:
        merchant_patron "I'm sorry, but I'm all out of wares for today. Come back next time, my friend."
        jump main_nocturnaltrunk
    merchant_patron "Greetings, traveler! Care to browse wares from distant lands? I have spices, fabrics, and trinkets aplenty."
    e "Greetings. What are you selling?"


    if trunk_merchant["Bought Times"] > 30:
        $ trunk_merchant["Level"] = 4
        merchant_patron "I have the finest goods from all corners of the world, even the most northern lands. Step right up and take a look!"
    elif trunk_merchant["Bought Times"] > 15:
        $ trunk_merchant["Level"] = 3
        merchant_patron "My wares are the best on and under this land. You won't find better anywhere else."
    elif trunk_merchant["Bought Times"] > 5:
        $ trunk_merchant["Level"] = 2
        merchant_patron "My inventory expands every day, friend. I assure you, you'll find something new every time you visit."
    else:
        $ trunk_merchant["Level"] = 1
        merchant_patron "I have a variety of local goods for sale, friend. Take a look and see if anything catches your eye."




    if trunk_merchant["Products"] != {}:
        $ trunk_merchant_items = trunk_merchant["Products"].items()
        jump Trunk_Merchant_Loop
    return

label Trunk_Merchant_Loop:

    if sum(trunk_merchant["Products"].values()) <= 0:
        merchant_patron "I'm sorry, but I'm all out of wares for today. Come back next time, my friend."
        jump main_nocturnaltrunk
    menu:
        "Buy one [trunk_merchant_items[0][0].name!t] for [trunk_merchant_items[0][0].value] Gold" if trunk_merchant["Products"][trunk_merchant_items[0][0]] > 0 and pc.gold >= trunk_merchant_items[0][0].value:
            $ trunk_merchant["Products"][trunk_merchant_items[0][0]] -= 1
            e "I'll take one [trunk_merchant_items[0][0].name!t]."
            $ pc.gold -= trunk_merchant_items[0][0].value
            $ addItem(trunk_merchant_items[0][0].name, inventory, 1)
        "Buy one [trunk_merchant_items[1][0].name!t] for [trunk_merchant_items[1][0].value] Gold" if trunk_merchant["Products"][trunk_merchant_items[1][0]] > 0 and pc.gold >= trunk_merchant_items[1][0].value:
            $ trunk_merchant["Products"][trunk_merchant_items[1][0]] -= 1
            e "I'll take one [trunk_merchant_items[1][0].name!t]."
            $ pc.gold -= trunk_merchant_items[1][0].value
            $ addItem(trunk_merchant_items[1][0].name, inventory, 1)
        "Buy one [trunk_merchant_items[2][0].name!t] for [trunk_merchant_items[2][0].value] Gold" if trunk_merchant["Products"][trunk_merchant_items[2][0]] > 0 and pc.gold >= trunk_merchant_items[2][0].value:
            $ trunk_merchant["Products"][trunk_merchant_items[2][0]] -= 1
            e "I'll take one [trunk_merchant_items[2][0].name!t]."
            $ pc.gold -= trunk_merchant_items[2][0].value
            $ addItem(trunk_merchant_items[2][0].name, inventory, 1)
        "Buy one [trunk_merchant_items[3][0].name!t] for [trunk_merchant_items[3][0].value] Gold" if len(trunk_merchant_items) >= 4 and trunk_merchant["Products"][trunk_merchant_items[3][0]] > 0 and pc.gold >= trunk_merchant_items[3][0].value:
            $ trunk_merchant["Products"][trunk_merchant_items[3][0]] -= 1
            e "I'll take one [trunk_merchant_items[3][0].name!t]."
            $ pc.gold -= trunk_merchant_items[3][0].value
            $ addItem(trunk_merchant_items[3][0].name, inventory, 1)
        "Buy one [trunk_merchant_items[4][0].name!t] for [trunk_merchant_items[4][0].value] Gold" if len(trunk_merchant_items) >= 5 and trunk_merchant["Products"][trunk_merchant_items[4][0]] > 0 and pc.gold >= trunk_merchant_items[4][0].value:
            $ trunk_merchant["Products"][trunk_merchant_items[4][0]] -= 1
            e "I'll take one [trunk_merchant_items[4][0].name!t]."
            $ pc.gold -= trunk_merchant_items[4][0].value
            $ addItem(trunk_merchant_items[4][0].name, inventory, 1)
        "That's it for now":
            e "Oh... that's it for now, thank you."
            jump main_nocturnaltrunk
    merchant_patron "A wise choice, friend! May it bring you good fortune on your travels."
    $ trunk_merchant["Bought Times"] += 1
    if sum(trunk_merchant["Products"].values()) <= 0:
        merchant_patron "I'm sorry, but I'm all out of wares for today. Come back next time, my friend."
        jump main_nocturnaltrunk
    else:
        merchant_patron "Anything else you need?"

    jump Trunk_Merchant_Loop

default mage_patron_shop = {"Scrolls": [], "Encounter": 0}
label Trunk_Mage_Dialogue:

    "You approach the hooded mage, who is sitting at a table with a few books and scrolls spread out in front of him."
    if not quest24.status == True:
        "The mage stares at you with a curious expression, pulling his scrolls away."
        e "What's wrong?"
        mage_patron "You don't look like someone who would use a trinket, would you?"
        "He looks you up and down, then shrugs."
        mage_patron "My apologies for wasted time, the scrolls have no use to you."
        mage_patron "Come back when you have a trinket, perhaps the lone alchemist knows a thing or two."
        return
    $ mage_patron_shop["Encounter"] += 1
    if mage_patron_shop["Encounter"] < 2:
        e "Hello, what are you studying?"
        mage_patron "Ah, greetings. I am not studying, actually, I'm just reading some old tomes. I find it quite relaxing while having a mug of beer."
        mage_patron "In fact, there are some interesting scrolls here that I would like to sell, if you're interested."
        e "What kind of scrolls?"
        mage_patron "Scrolls for you to find trinkets on your way. There are some spare ones that I don't need anymore, so I thought I could sell them to you."
    else:

        mage_patron "Ah, greetings again. I have some scrolls that might interest you, if you're looking for trinkets to find on your travels."

    $ available_scrolls = ["None"]
    if snowbound_summit_place.discovered == True and scrollofshiveringshard_item not in mage_patron_shop["Scrolls"] and not hasTrinket("Shivering Shard"):
        $ available_scrolls.append(scrollofshiveringshard_item)
    if grove_of_harvest.discovered == True and scrollofspirespike_item not in mage_patron_shop["Scrolls"] and not hasTrinket("Spirespike"):
        $ available_scrolls.append(scrollofspirespike_item)
    if slumbrous_well.discovered == True and scrollofbruisersbite_item not in mage_patron_shop["Scrolls"] and not hasTrinket("Bruisers Bite"):
        $ available_scrolls.append(scrollofbruisersbite_item)
    $ chosen_scroll = renpy.random.choice(available_scrolls)
    if chosen_scroll == "None":
        "The mage flips through his scrolls, then looks up at you with a shrug."
        mage_patron "...looks like I don't have any scrolls to sell you right now. Come back later, maybe I'll have something for you."
        mage_patron "Try discovering more places as well, I'll only be able to sell you scrolls for trinkets in places that you have discovered."
    else:
        "The mage flips through his scrolls, then looks up at you with a smile."
        mage_patron "I do have a scroll for you, actually. It's [chosen_scroll.name!t]."
        menu:
            mage_patron "[chosen_scroll.scroll.name!t], sounds like something you might be interested in, right? I can sell it to you for... [chosen_scroll.value] gold."
            "Buy the scroll" if pc.gold >= chosen_scroll.value:
                $ pc.gold -= chosen_scroll.value
                $ addItem(chosen_scroll.img, inventory, 1)
                $ mage_patron_shop["Scrolls"].append(chosen_scroll)
                e "I'll take it."
                mage_patron "Excellent choice! This scroll will help you find [chosen_scroll.scroll.name!t] on your travels. I'm sure of it."
            "Decline the offer":
                e "I'll pass for now, thank you."
                mage_patron "No problem, friend. If you change your mind, I'll be here. Perhaps with another scroll."
    "The mage returns to his tomes once more."
    return

default arm_wrestler = {"Encounter": 0, "Winner": "None", "Status": "None", "Opponent": 1, "Win": 0, "Lose": 0, "Bet Win": 0, "Bet Lose": 0, "Gold": 550}
default wrestle_value = 0.5
screen fighting_bar():
    if arm_wrestler["Opponent"] == "Bull":
        add "armwrestle_bull_battle" xpos 0.5 ypos 0.4 anchor (0.5, 0.5)
    else:
        add "armwrestle_hyena_battle" xpos 0.5 ypos 0.4 anchor (0.5, 0.5)
    vbox:
        xalign 0.5
        yalign 0.75
        xmaximum 300
        ymaximum 400
        spacing 20
        bar value AnimatedValue(wrestle_value, 1.0, 0.5) left_bar Frame("left_red", 6, 6) right_bar Frame("left_blue", 6, 6)
        if can_wrestle:
            frame:
                xpadding 20
                ypadding 10
                style "coolframe"
                textbutton _("Wrestle") text_color "#eeeeee" style "tap_button" action SetVariable("wrestle_value", wrestle_value + 0.0075 * tenki_wrestling_strength), Return(wrestle_value), SetVariable("can_wrestle", False) xalign 0.5 yalign 0.5
        else:
            frame:
                xpadding 20
                ypadding 10
                style "coolframe"
                textbutton _("Wrestle") text_color "#eeeeee" style "tap_button" action NullAction() xalign 0.5 yalign 0.5

    timer 0.025 repeat True action If(wrestle_value > 0, true=SetVariable("wrestle_value", wrestle_value - 0.001 * wrestler_strength), false=[Hide('fighting_bar'), Jump("Trunk_Fighters_Lose")]), Return(wrestle_value)
    if can_wrestle == False:
        timer 0.01 repeat True action SetVariable("can_wrestle", True)

label Trunk_Fighters_Dialogue:
    "You hear the sound of grunting and cheering as you approach the corner of the tavern."
    "A group of patrons are gathered around a table, watching two arm wrestlers go at it."
    $ arm_wrestler["Encounter"] += 1
    if arm_wrestler["Encounter"] < 2:
        fighter_patron3 "Come on, I bet good money on you! Don't let me down!"
        "You watch as the two arm wrestlers struggle against each other, their muscles straining as they try to overpower their opponent."
        "The tension in the air is almost palpable as the two fighters lock eyes, their faces contorted in concentration."
        "You can see the sweat dripping down their faces as they strain against each other, their arms trembling with the effort."
        "It looks like a close match, but you can't help but feel a sense of excitement as you watch the two fighters battle it out."
        fighter_patron1 "Ahh-"
        "The bull wrestler slams his opponent's arm down on the table, the sound of the impact echoing through the tavern."
        fighter_patron2 "I win this round! Pay up, everyone!"
        "The crowd cheers as the bull wrestler raises his arms in victory, a triumphant grin on his face."
        "As the bull collects his winning, you notice the coyote walking close to you."
        fighter_patron3 "New to the tavern, huh? The bets are open, you want to try your luck?"
        e "What's the prize?"
        fighter_patron3 "This is just some casual bets, how does 10 gold sound? The odds are in the bull's favor, I can tell you that."
        fighter_patron3 "So, what do you say? Wanna join the bet?"
    else:
        fighter_patron3 "You're back! Ready to try your luck again?"
        e "I'm ready to bet."
        fighter_patron3 "Alright, let's see if you can beat the odds this time."
    jump Trunk_Fighters_Bet


label Trunk_Fighters_Bet:

    menu:
        "Bet 10 coins on the bull":
            $ arm_wrestler["Status"] = "Bull"
            e "I'll bet on the bull."
        "Bet 10 coins on the hyena":

            $ arm_wrestler["Status"] = "Hyena"
            e "I'll bet on the hyena."
        "Decline":
            e "I'll pass."
            fighter_patron3 "Suit yourself, pal. Now, if you'll excuse me..."
            "You watch as the coyote walks back to the crowd."
            $ arm_wrestler["Encounter"] -= 1
            return
    "You hand the coyote 10 coins, watching as he adds your bet to the pile."
    "Another round of arm wrestling begins, you watch intently as the two fighters lock arms."
    if renpy.random.random() < 0.7:
        $ arm_wrestler["Winner"] = "Bull"
        "As the two fighters struggle against each other, it's clear that the bull has the upper hand."
        "It didn't take long for the bull to overpower the hyena, slamming his arm down on the table with a loud thud."
        fighter_patron3 "It's a win for the bull again! Pay up, everyone!"
    else:
        $ arm_wrestler["Winner"] = "Hyena"
        "The hyena is able to hold his own against the bull, the two fighters locked in a fierce struggle."
        "Just as the bull slacken to take a breath, the hyena takes the opportunity to slam his arm down on the table, winning the match."
        fighter_patron4 "Ha! I knew you could do it! Pay up, everyone!"
    if arm_wrestler["Status"] == arm_wrestler["Winner"]:
        $ arm_wrestler["Bet Win"] += 1
        if arm_wrestler["Winner"] == "Bull":
            $ arm_wrestler["Gold"] += 10
        else:

            $ arm_wrestler["Gold"] += 17

        $ arm_wrestler["Gold"] += 17
        e "A win for me! That was a good fight!"
        "The coyote hands you 17 coins, a smile on his face as he does so."
    else:
        $ arm_wrestler["Bet Win"] += 1
        $ arm_wrestler["Gold"] -= 10
        e "That was a close one... I'll get you next time."
        "The coyote smiles as he collects your coins, adding them to the pile."
    fighter_patron3 "Well, hope to see you again next time."

    return

label Trunk_Fighters_Arm_Wrestling_Begin:
    $ can_wrestle = True
    $ wrestle_value = 0.5
    jump Trunk_Fighters_Arm_Wrestling

label Trunk_Fighters_Arm_Wrestling:
    if arm_wrestler["Opponent"] == "Bull":
        $ wrestler_strength = renpy.random.randint(5, 15) * 1.7
    else:
        $ wrestler_strength = renpy.random.randint(5, 15) * 1
    $ tenki_wrestling_strength = renpy.random.randint(10, 20) + pc.stg * 0.1
    if wrestle_value > 0.7:
        $ wrestler_strength = renpy.random.randint(5, 15) * arm_wrestler["Opponent"] * 1.4
    call screen fighting_bar
    if wrestle_value >= 1:
        jump Trunk_Fighters_Win
    jump Trunk_Fighters_Arm_Wrestling

label Trunk_Fighters_Lose:
    ""
    return

label Trunk_Fighters_Win:
    "Winner!"
    return


default dyad = {"Encounter": 0, "Dialogue": 0, "Status": "None"}

label Trunk_Pair_Dialogue:
    "A bit of chattering catches your attention, as you see a pair of patrons sitting at the corner of the tavern."
    $ dyad["Encounter"] += 1
    $ dyad["Dialogue"] = (renpy.random.randint(0, 10), renpy.random.random())
    if dyad["Dialogue"][0] == 0:
        pair_patron1 "-remember the time we tried to brew our own ale? That was a disaster, worst drink we've ever had."
        pair_patron2 "Aye, tasted like straight piss, we were never allowed near the kitchen again, but it's for ol' Lusty's good."
    elif dyad["Dialogue"][0] == 1:
        pair_patron1 "You know, I've been thinking about joining the hunters. What do you think?"
        pair_patron2 "You? Joining the hunter's guild? You can't even swing a sword properly, let alone take on a quest."
        pair_patron1 "Hey, I can swing a sword just fine! I just... prefer not to. I'm more of a thinker, you know?"
        pair_patron2 "A thinker, huh? Well, let's put it this way. They could use more brains than brawn if you don't actively sabotage the team by your mere presence."
    elif dyad["Dialogue"][0] == 2 and dyad["Dialogue"][1] < 0.5 and sum(tavern_date) > 0:
        pair_patron1 "Why do you think the "
    elif dyad["Dialogue"][0] == 2:
        pair_patron2 "I thought it was quite fascinating, the name of the tavern. Nocturnal Trunk, it's quite poetic, don't you think?"
        pair_patron2 "It's like the night is a tree, and we're all just leaves, hanging on for dear life."
        pair_patron1 "No... the name comes from the tree that grew in the middle of the tavern. There were purple fruits from the tree that glows at night. It was like, one of the three trees that stood from since the primordial days."
        pair_patron2 "Really? I thought it was just a name. I never knew there was an actual tree in here."
        pair_patron1 "It's long gone now, supposedly it began rotting after the moss problems back in the day."
        pair_patron1 "You'd think Cane'd change the name, but I guess it's got a nice {i}ring{/i} to it."
    elif dyad["Dialogue"][0] == 3:
        pair_patron1 "You hear about the alleyway brawl last night? I heard it was a real bloodbath."
        pair_patron2 "Aye, I heard screaming and shouting all night. Sounds like someone's got a bone to pick with someone else."
        pair_patron1 "They said that a man came out of the alleyway covered in bruises and cuts, must have been a real fight."
        pair_patron2 "Who else was there?"
        pair_patron1 "No idea... I don't dare to go near that place. It sounds like a dangerous place, that alleyway must have hidden a scary secret."
        pair_patron2 "Aye, me neither, best to stay away from there."
    elif dyad["Dialogue"][0] == 4 and dyad["Dialogue"][1] < 0.4 and quest10.status == False and quest05.status == True:
        pair_patron1 "Last time I was in the forest, I saw the blue man... you know, the one with the glowing blue mask."
        pair_patron2 "Did you? I've heard stories about him, they say he's looking for something, but no one knows what."
        pair_patron1 "He is from the goatspeople, I think."
        pair_patron2 "Wait... aren't all the goats... goats? Is he one of them?"
        pair_patron2 "Of course when we talk about the goatspeople we mean both the goats and the deers, they're like the same tribe now."
    elif dyad["Dialogue"][0] == 4 and dyad["Dialogue"][1] < 0.7 and quest10.status == True:
        pair_patron1 "What's up with the goatspeople? I heard some goats wailing from over the river. They're usually so quiet."
        pair_patron2 "I heard some of them went missing. They say the buggbears are behind it, but I don't know if I believe that."
        pair_patron1 "Why not? The buggbears are known for their mischief, they could've done it."
        pair_patron2 "They said the missing goats had brought nothing with them, not even a weapon. It's not like them to go out unprepared."
        pair_patron1 "That's true... but they couldn't have vanished into the thin air."

    elif dyad["Dialogue"][0] == 4:
        pair_patron1 "Have you heard about the goats? They're always around that damn tree for some reason."
        pair_patron2 "The goats? What are they planning?"
        pair_patron1 "They said they are holding the burials, carrying them to the tree and leaving a mark before they return to the tribe."
        pair_patron2 "Burials? Who died?"
        pair_patron1 "How do I know... do I look like a goat to you?"
        pair_patron2 "Yeah, you're hornier than a goat, that's for sure."
    elif dyad["Dialogue"][0] == 5:
        pair_patron2 "So, speaking of, what happened to the ol' Lusty's mayor? Do we even have one?"
        pair_patron1 "I think the last one died of old age, or maybe he just got tired of the job."
        pair_patron2 "And no one's taken his place yet?"
        pair_patron1 "Shhh... Don't you know? The mayor's seat is cursed, no one wants to take it."
        pair_patron2 "Cursed? How so?"
        pair_patron1 "They say that when the old mayor died, everyone who tried to take his place met with an untimely end."
        pair_patron2 "That's... unsettling. Maybe we should just leave it empty, then."
    elif dyad["Dialogue"][0] == 6:
        pair_patron2 "The iron shortage is really starting to affect the town. I heard the blacksmiths are struggling to keep up with demand."
        pair_patron1 "I heard that too, too bad the werewolves stopped mining their damn ore veins... they could've been our lords right now with the gold they are sitting on."
        pair_patron2 "I don't think they'd be too unhappy about that, they're not exactly the most sociable of creatures."
        pair_patron1 "Yeah, but they could've been rich! Richer than the king, even."
    elif dyad["Dialogue"][0] == 7:
        pair_patron1 "Have you heard about that bard? The one who's been playing in the tavern lately?"
        pair_patron2 "Yeah, I've seen that sweet tongue of his, he's got a way with words, that's for sure."
        pair_patron2 "That bard is a real charmer, he smacks his mouth for a few times and everyone's getting tipsy topsy-turvy."
        pair_patron1 "I don't like the kinds of people he brings in, it's getting crowdier upstairs."
    elif dyad["Dialogue"][0] == 8:
        pair_patron1 "What's new with the capital? I heard the king's been making some changes."
        pair_patron2 "They've started sending out more patrols from the east, I heard. Something about curbing the bandits in the area."
        pair_patron1 "Is that so? I wonder if they'll come this way next. Lusty's been quiet for too long."
        pair_patron2 "I doubt it, we're too far out of the way for them to bother with us. Maybe quietness is all they needed from us."
    elif dyad["Dialogue"][0] == 9 and dyad["Dialogue"][1] < 0.5 and sebas_suck > 0:
        pair_patron1 "They said the pawnbroker's been acting strange lately, have you noticed anything?"
        pair_patron2 "I don't know, I haven't been there in a while. What's he been doing?"
        pair_patron1 "The wall says he's squirming and panting hard, like he's got something to hide."
        pair_patron1 "Maybe he's just nervous or something."
        pair_patron2 "Not only that, one of the client said he's got something... white on his finger after reaching underneath."
    elif dyad["Dialogue"][0] == 9:
        pair_patron2 "I went to the pawn the other day, had to pledge some of my old stuff."
        pair_patron1 "What did you pledge?"
        pair_patron2 "My family bronze armor, it's been passed down for generations, but I needed the coins."
        pair_patron1 "You pledged your family armor? Are you mad?"
        pair_patron2 "I will get it back, the pawnbroker said he'd keep it safe for me. He's not as discourteous as the others said."
        pair_patron1 "If you say so."
        pair_patron1 "He probably loses more coins drinking beer here, I don't think lack of coin is at issue there."
    elif dyad["Dialogue"][0] == 10:
        pair_patron2 "What's up with those sneak thieves? Are they stealing the beers again?"
        pair_patron1 "Cane just lets them get off scot free. I wonder how much more beer does it take for him to finally kick them off the bar."


    "The dragon patron looks up at you and grins, while the wolf patron nods at you."

    return

label Trunk_Guild_Dialogue:
    msg "Work in Progress!"
    return

label Trunk_Sneaks_Dialogue:
    sneak_patron "You lookin' for something, or just here to wet your throat?"
    "You can't help but notice the sly grin on the patron's face as he pours himself a mug full of beer."
    msg "Work in Progress!"
    return



label Trunk_Rumor_Patron_Quest:
    "You approach the table where a mysterious patron sits, his eyes scanning the room as you approach."
    msg "Work in Progress!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
