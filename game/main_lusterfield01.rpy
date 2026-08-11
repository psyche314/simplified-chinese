label main_bedroom:
    $ current_location = "bedroom"
    $ timenow.minute += 3
    $ timenow.passTime()
    if isNight():
        scene bedroom_night
        with dissolve
    else:
        scene bedroom
        with dissolve
    menu:
        "What are you going to do?"
        "Sleep" if isNight():
            jump bedroom_sleep
        "Rest":
            jump bedroom_rest
        "Pleasure yourself" if pc.lust >= 0.4*pc.max_lust:
            if isNight():
                call Scene_Exhibition_Masturbation from _call_Scene_Exhibition_Masturbation
            else:
                "You cannot resist your lust anymore, you lunge into your own bed, grinding yourself against the bedsheet before looking down at your crotch, it is remarkably hard now."
                "The sexual desire in your mind is overrunning your logical thinking, you cannot wait any longer. Quickly, you strip off all your equipment except for the loincloth."
                call scene_masturbation from _call_scene_masturbation

            $ timenow.hour += 4
            $ timenow.passTime()
            $ pc.rest()
            $ pc.lust = 0
            "You wake up 4 hours later, all of the lust in your body is gone now. You feel ready to go out again."
            jump main_bedroom
        "Open Storage":
            hide screen daytime
            jump Storage_Screen
        "Debugging":
            menu:
                msg "This is a debug screen for fixing all bugs related issues in some saves."
                "Unlock All Gallery Scenes":
                    msg "This function is only available to {b}Roommate{/b} and {b}Keeper{/b} Tier on Patreon. Passcode will change every update."
                    if gallery_open:
                        menu:
                            msg "Turn off Gallery Unlock feature? You have to re-enter the passcode to access it again."
                            "Yes":

                                $ gallery_open = False
                                jump main_bedroom
                            "No":
                                jump main_bedroom
                    else:
                        jump Gallery_Input_Passcode
                "Clear Quest Progress":

                    msg "This fix is for when you constantly get approached by an error screen regarding quest progress."
                    menu:
                        "Proceeding will refresh your quest progress, and delete unnecessary progresses with string type."
                        "Confirm":
                            $ clearQuestProgress(quest_dictionary)
                            $ clearQuestProgress(task_dictionary)
                        "Cancel":
                            pass
                    jump main_bedroom
                "Fix/Complete Whispering Hollow's Quest (v0.0.16 up)":
                    msg "This fix is for when you are stuck in the whispering hollow, not able to turn in Uffe's quest."
                    if quest34.status != False and quest34.status != True and quest34.status < 4:

                        menu:
                            msg "If you hold a Moonstone Amulet. Proceeding while the quest is active will refresh your quest status, allowing you to complete the quest again."
                            "Confirm":
                                if LookForItem("Moonstone Amulet", inventory):
                                    if len(quest34.progress) <= 2:
                                        $ quest34.qProgress(__("Solve the riddles and retrieve the amulet in the Whispering Hollow"))
                                        $ quest34.qProgress(__("Cut all grasses in the Whispering Hollow"))
                                    $ quest34.status = 3
                                    msg "You may need to cut the grass again to complete the quest."
                            "Cancel":

                                jump main_bedroom
                    jump main_bedroom
                "Fixing Player Stats (v0.0.16 up)":
                    msg "This fix is for when your stats are lower than normal after unequipping."
                    menu:
                        msg "Proceeding will unequip all your equipment and recalculate your stats."
                        "Confirm":
                            if pc.armor["Clothes"] != None:
                                $ pc.armor["Clothes"].unequip()
                            if pc.armor["Accessory"] != None:
                                $ pc.armor["Accessory"].unequip()
                            if pc.armor["Bccessory"] != None:
                                $ pc.armor["Bccessory"].unequip()
                            if pc.armor["Mask"] != None:
                                $ pc.armor["Mask"].unequip()
                            if pc.armor["Pants"] != None:
                                $ pc.armor["Pants"].unequip()
                            if pc.weapon != None:
                                $ pc.weapon.unequip()



                            $ pc.eqdamage = 0
                            $ pc.eqmax_lust = 0
                            $ pc.eqmax_hp = 0
                            $ pc.eqmax_mp = 0
                            $ pc.eqaccuracy = 0
                            $ pc.eqdodge = 0
                            $ pc.eqdefense = 0
                            $ pc.eqlust_defense = 0
                            $ pc.eqlust_dodge = 0
                            $ pc.eqlust_damage = 0
                            $ pc.eqcrit_chance = 0
                            $ pc.eqcrit_damage = 0
                            msg "Done! Please put your clothes back on after reset, or not!"
                            jump main_bedroom
                        "Cancel":
                            jump main_bedroom
                "Leave":
                    jump main_bedroom
        "Leave":

            window hide
            call screen place_bedroom

    if _return == "To Kingspawn":
        hide screen place_bedroom
        jump main_kingspawn
        return
    jump main_bedroom

default persistent.passcode = "empty"
label Gallery_Input_Passcode:
    python:
        gallery_input = renpy.input(_("Enter the Passcode:"), length=20, exclude="!@#%^&|\"'\\")
        gallery_input = gallery_input.strip()
    if gallery_input == persistent.passcode:
        $ gallery_open = True
        msg "All gallery scenes are successfully unlocked!"
        jump main_bedroom
    else:
        menu:
            msg "Passcode incorrect. Do you want to try again?"
            "Yes":
                jump Gallery_Input_Passcode
            "No":
                jump main_bedroom

label bedroom_sleep:
    "You get on the bed and slowly fall asleep."
    if timenow.hour > 18:
        scene black
        with fade
        pause 0.5
        $ timenow.day += 1
        $ timenow.hour = 7
        $ timenow.minute = 0
        $ timenow.passTime()
    if timenow.hour < 6:
        scene black
        with fade
        pause 0.5
        $ timenow.hour = 7
        $ timenow.minute = 0
        $ timenow.passTime()
    $ pc.sleep()
    "You wake up in the morning, feeling energized and ready for the day."
    if renpy.random.random() > 0.7 and asked_cleaning and quest15.status == False:
        stop music fadeout 1.0
        jump Ole_Sick_Quest
    if renpy.random.random() > 0.7 and quest09.status == True and quest12.status == True and quest15.status == True and quest14.status == True and quest16.status == False:
        stop music fadeout 1.0
        jump Ole_Party_Begin
    jump main_bedroom

label bedroom_rest:
    "You get on the bed and rest for a few hours."
    scene black
    with fade
    $ timenow.hour += 4
    $ timenow.passTime()

    $ pc.rest()
    "You recovered a portion of your HP and MP."
    jump main_bedroom

label main_kingspawn:
    $ current_location = "kingspawn"
    $ timenow.minute += 3
    $ timenow.passTime()
    $ renpy.music.play(mShop, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call Lusterfolk_Schedule from _call_Lusterfolk_Schedule
    if isNight():
        scene kings_pawn_night
    else:
        scene kings_pawn
    with dissolve
    if renpy.random.random() > 0.9 and quest32.status == False and quest08.status == True and quest07.status == True and quest11.status == True and task04.completedtimes > 0:
        jump Sebas_Night_Out_Quest_Begin
    if quest32.status == 2 and quest32.start_date == timenow.day and timenow.hour > 18:
        jump Sebas_Night_Out_Before_Tavern
    if quest32.status == 2 and quest32.start_date < timenow.day and timenow.hour > 7:
        jump Sebas_Not_Going_Night_Out
    if quest15.status == 2 or quest15.status == 3:
        jump Ole_Sick_Quest_End
    if quest40.status == 2 and timenow.day == quest37.start_date + rahim_vote_duration - 1 and timenow.hour < 23 and timenow.hour >= 20:
        menu:
            "It seems it's around the time to follow Sebas, do you want to hide here and wait, or give up following him?"
            "Wait to follow Sebas":
                $ quest40.status = 4
                jump Jog_Vote_Follow_Sebas
            "Do not wait":
                $ quest40.status = 3
    if quest16.status == 2:
        jump Ole_Party_Quest
    show screen menu_buttons
    window hide
    call screen place_kingspawn
    if _return == "Drawing":
        "A doodle of Sebas' and Ole's portrait, it captures the lion's charming smile, and the lizard's kindness, they seem to be situated behind the same wall this drawing is hanged."
        "The paper has aged quite a bit, but seemingly well-groomed along the years."
        if sebas_location == "kingspawn":
            e "Seb, I like this drawing, maybe I should pay the drawer a visit."
            s "Oh! That's my favourite doodle right there, it's quite old, honestly, we invited Rahim's... partner to sketch us when the shop first opened."
            s "That's a long time, damn. She is quite an artist isn't she, look at those strokes, you might have thought it takes longer than 10 minutes."
            e "You two looks so cozy here."
            s "Well, we should've made a better pose if we knew she's going away, maybe request a full body ones like those you hang in a palace or something, but Ole's too piffy-puffy."


    if _return == "Book":
        $ battle_of_lusterfield01 = Page("\n\n\n\n\n\n\n\n                Battle of Lusterfield\n", "\n\n\n\n\nIhktn the annals of history, few tales are as poignant as the conflict between the peaceful village of Lusterfield and the proud Kechioeren tribe. This book aims to preserve the memory of the events that led from friendship to ferocious battle, as a part of the history and culture of Mokken as a whole.", 1)
        $ battle_of_lusterfield02 = Page("Lusterfield, nestled in the verdant embrace of gentle hills, had long been a beacon of peace and prosperity. Battle and wars are rarity, if not non-existent, hence the reason no one has been pronounced the Mayor of Lusterfield for decades. Its people lived in harmonious trade with the Kechioeren, a tribe renowned for their mana-rich flowing water and its close ties with the primordial runes. Season after season, the village square buzzed with the exchange of goods from both communities. The Goat Tribe brought wools, water, intricately mined crystals, while Lusterfield offered grains, textiles, and crafted beers. It was a partnership built on mutual respect and benefit.\n\n","The turning point came unexpectedly during one morning when a goat wagon, heavy with trade goods bound for Lusterfield, was ambushed.\n\nThe assailants were never seen, leaving no trace of their identity, but the carnage spoke of a deliberate act to incite fury. Lives were lost, and treasures plundered, and almost at the same time, the Primordial runes at the high mountain was stolen mysteriously. Despite Lusterfield's protests of innocence, the seeds of distrust were sown in blood-soaked soil.\n\nTevfik, the stalwart leader of the goats, consumed by grief and the cries for justice", 2)
        $ battle_of_lusterfield03 = Page(" for his people, he pointed his fingers at Lusterfield. War cries echoed through the hills as Tevfik led his warriors in a vengeful strike against the village.\n\nTevfik and his fighters quickly surrounded the village with their camps, threatening to capture their supposed leader, Rahim. The Lusterfolks, unprepared for the ferocity and feeling the sting of betrayal, scrambled to defend their homes and families.\n\nBattle after battle, neither side gained ground. The goats, fierce but few, and the villagers, resolute yet unskilled in the ways of war, found themselves locked in a stalemate that threatened to drag on until both were but memories in the wind.\n\nDespite the violent battle, only few lives were lost, the reluctance of both side's soldiers remains strong.", "However, Tevfik did not retreat, the leader was not known for his indolence, many buildings of the village crumbled under the goat's magic, as the battle continues.\n\nAfter the dawn, a shadow moved through the night. Lothar Faelon, an adventurer who lived in Lusterfield seeking solace from his own battles, could not stand idly by. Armed with little more than his wits and a keen blade, he infiltrated the Kechioeren camp under the cover of darkness. It's not known the details of his attempt. Only that he eventually found Tevfik, weary and exposed. The confrontation was swift, a silent struggle that ended with the leader's fall.", 3)
        $ battle_of_lusterfield04 = Page("Lothar disappeared into the night as quietly as he had come, leaving a leaderless tribe to grapple with the reality of their loss.\n\nWith Tevfik gone, the battle's fever broke. The goats, leaderless and confused, retreated, their will to fight sapped by their leader's untimedly demise. Lusterfield mourned its dead but also breathed a sigh of relief. Lothar, known to the villagers only as a mysterious benefactor, became a legend whispered in awe.\n\nPeace was restored between the both sides, but destruction remains permanent, the broken bridge inbetween was never repaired, haunted by the shadows of what had been lost between them.", "With this in mind, the mystery of primordial runes remained unsolved, Furkan, son of Tevfik, succeeded as the new chief of the goats. Memorials were erected on both sides, not just for the fallen, but for the friendship that had once blossomed.", 4)
        if checkNoShopItem("Battle of Lusterfield"):
            $ battle_of_lusterfield01.addTo(battle_of_lusterfield)
            $ battle_of_lusterfield02.addTo(battle_of_lusterfield)
            $ battle_of_lusterfield03.addTo(battle_of_lusterfield)
            $ battle_of_lusterfield04.addTo(battle_of_lusterfield)
            $ addItem("Battle of Lusterfield", inventory, 1)

        "You found a book on the top of the cabinet, flipping over the pages, it seems to be a brief history of Lusterfield."
        call screen book_read(battle_of_lusterfield)
        "It doesn't look like Ole will mind you taking an old book, probably. With that in mind, you slowly place the book in your bag."

    if _return == "Account":
        $ kings_pawn_account_journal01 = Page("Date: 15th of Frostfall\n\nEntries:\n1. {b}10 pieces of Rahim's Small Cloth{/b}\nNotes: Excellent condition, it's Rahim so it must be good.\nPurchase Price: 1 Gold\n\n2. {b}Wide-brimmed Hat of Sorcery{/b}\nCondition: Excellent, albeit some burn and wear on the brim\nNote: Recovered from the wild ruins near the dark forest\nPawned by: Ferrit the sorcerer, with a purple staff, he looks like a lion but his mane's not as majestic as mine.\nLoan Amount: 450 Gold\nRedemption Due Date: 15th of Sproutsong","3. {b}3 bottles of Small Health Potions{/b}\nNotes: Excellent condition, gotta start pressing Haskie to make more of them potions, Ole, is it that hard to juice up some red berries???\nPurchase Price: my soul for walking a whole hour for 3 potions\n\n4. {b}Likkathian Iron Helmet{/b}\nCondition: Excellent, except the left side is completely destroyed by fire magic, most of the right side is burned to a crisp.\nNote: Recovered from a retired soldier in Likkathia\nSell by: duh\nPurchase Price: 10 gold", 1)

        $ kings_pawn_account_journal02 = Page("5. {b}Book of Fiery Charge{/b}\nCondition: Excellent, some wear on the bottom corner in the back\nNote: Recovered from Ole's {i}friends{/i}, been in his collections for a long time\nSold by: Ole, it's fucking Ole\nPurchase Price: 0 gold\n\n6. {b}Crystal Orb of Mending{/b}\nCondition: Excellent, but it's a bit used\nNote: Seems to be popular among the healers, he gotta get it back quick or we'll sell it to someone else\nPawned by: Baird the scavenger, the frog dude living next to Rahim.\nLoan Amount: 300 Gold\nRedemption Due Date: 24th of Frostfall", "7. {b}Steel Dagger{/b}\nCondition: Excellent, pristine even.\nNote: Straight out of the anvil, looks good.\nPawned by: Pickard the blacksmith, he never redeems his weapon, should've just sold them\nLoan Amount: 55 Gold\nRedemption Due Date: 12th of Suncrest\n\n8. {b}Sapphire Necklace of Vitality{/b}\nCondition: Excellent\nNote: says it's gilded with pure gold, but it's not reflective enough, not sure if it's real, gotta need an appraiser like Gwyd\nPawned by: Hooded guy, can't hear half of what he says\nLoan Amount: 120 Gold\nRedemption Due Date: 30th of Frostfall", 2)
        $ kings_pawn_account_journal03 = Page("9. {b}Likkathian Iron Helmet{/b}\nCondition: Excellent, the seller should put it on himself\nNote: Nah\nPurchased by: duh\nSale Price: 3000 gold\n\n10. {b}Ring of Eldest{/b}\nCondition: Excellent, it sounds just as cheesy as it should\nNote: Not to be confused with another ring, this one is cosmetic only, referenced by the northern supplier\nTraded for: Crystal Orb of Mending, gotta say sorry to Baird.", "11. {b}Elixir of Fleeting Agility{/b}\nCondition: Excellent, never opened before.\nNote: Seems to be a rip-off of Haskie's old recipe, looks good though.\nSold by: Andri the travelling merchant\nPurchase Price: 60 Gold\n\n12. {b}Rock Sculpture of Tapjoo{/b}\nCondition: Excellent, small crack in the bottom\nNote: Seller refused to elaborate on the origin but this is real old, matches Tapjoo's mask in other goat painting so it's legit\nSold by: Another Hooded guy, with horn this time.\nPurchase Amount: 2150 Gold", 3)
        $ kings_pawn_account_journal04 = Page("13. {b}Old Bronze-plated Armor{/b}\nCondition: Excellent\nNote: it was pretty lame, get it Ole? Lame? \nPawned by: Ludvar the wolf, he keeps bugging me about the price\nLoan Amount: 301 gold\nRedemption Due Date: Negotiable\n\n14. {b}Copy of the History of Otsovaara{/b}\nCondition: Excellent?\nNote: Sturdy paper, clean handwriting but too modern for any scholar with self-respect. \nSale Price: 40 Gold", "15. {b}12 pieces of Werewolf Pelts{/b}\nCondition: Excellent, freshly harvested.\nNote: The hunters are on their hunt again, will pass this to Rahim later, {i}no werewolves involved are hurt during this process, I think.{/i}\nSold by: Est the leader\nPurchase Price: 240 Gold\n\n", 4)
        $ book_page = 0
        if kings_pawn_account_journal01 not in kings_pawn_account_journal.content:
            $ kings_pawn_account_journal01.addTo(kings_pawn_account_journal)
        if kings_pawn_account_journal02 not in kings_pawn_account_journal.content:
            $ kings_pawn_account_journal02.addTo(kings_pawn_account_journal)
        if kings_pawn_account_journal03 not in kings_pawn_account_journal.content:
            $ kings_pawn_account_journal03.addTo(kings_pawn_account_journal)
        if kings_pawn_account_journal04 not in kings_pawn_account_journal.content:
            $ kings_pawn_account_journal04.addTo(kings_pawn_account_journal)
        show screen book_read(kings_pawn_account_journal) with dissolve 

        "You find an account journal lying on top of the counter. It seems to record the daily activities of the pawn shop."
        call screen book_read(kings_pawn_account_journal) with dissolve 
    if _return == "Plush":
        "A lizard plush doll that closely resembles Ole, except that it seems to stand on four legs."
        "You stare at the doll, it aged well over the years, the scales seem to be painted on, but it falls off quite easily."
        if ole_location == "kingspawn":
            e "Is this you, Ole?"
            "You point towards the plush doll, urging Ole to look this way."
            o "Oh, there're not many green lizards crawling around here are there, kiddo."
            o "And, well, before you ask, this is not for sale, even for a roommate."
            e "Well, it's not like I was about to ask you about it. Did Seb make this too?"
            o "Yes, he did. There was a time when he was fervent about making some cute dolls, of him mostly but sometimes he used the doll as an excuse to... study my proportions."
            o "I just let him have his fun anyway, the proportion never turned out that well because he's not cutting the fabric correctly, and the wool isn't filling up all the nooks and crannies inside."
            "Ole picks up the doll, feinting a soft smile."
            o "But, it looks pretty cute, and I've never received such a gift before, so this one has a special place in my heart."
            o "And, maybe, he'll pick the needle up and sew you one! Seb's totally fond of you being here so I can't see a world where there won't be a dragon plush in the shop one day."
            e "You bet."
    if _return == "Statue":
        "A mysterious statue of a goat sitting and wearing a simple mask. Doesn't seem to be for sale like the other items in the shop."
        if ole_location == "kingspawn":
            e "Hey, Ole, what's this statue about? It looks kinda creepy."
            o "A traveller pawned this away a long time ago, it's from an old religion of some sort, it's very valuable, actually, considering the rarity."
            e "Wait, what's this old religion?"
            o "According to the old Kechioeren tales, the goats seemed to worship Tapjoo, who they believe to give them the magical flowing water."
            o "But, I suppose they stopped worshipping when the god's been gone for such a long time."
            o "It's hastily made, bad texture and materials, but the value comes from its history."
            o "this is what Tapjoo's supposed to look like, at least it's what the goats imagined him to be."
            e "Oh, I see I see."



    if _return == "To Bedroom":
        hide screen place_kingspawn
        jump main_bedroom

    if _return == "Sebas":
        jump Sebas_dialogue

    if _return == "Ole":
        jump Ole_dialogue

    if _return == "To Lusterfield":
        hide screen place_kingspawn
        jump main_lusterfield01
    jump main_kingspawn

label main_lusterfield01:
    $ current_location = "lusterfield01"
    $ renpy.music.play(mLusterfield, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ l = Character(_("Lothar"), color="#92939f", who_outlines=[ (2, "#000") ])
    $ wilderness = False
    $ timenow.minute += 3
    $ timenow.passTime()
    if isNight():
        scene lusterfield01_night
    else:
        scene lusterfield01
    call Lusterfolk_Schedule from _call_Lusterfolk_Schedule_1
    if quest37.status == 2 and timenow.day == quest37.start_date + rahim_vote_duration and timenow.hour >= 12 and timenow.hour < 23 and vote_choice[0] == 0:
        jump Rahim_Vote_Day
    if quest37.status == 2 and timenow.day > quest37.start_date + rahim_vote_duration:
        jump Rahim_Vote_Day_Late
    if quest05.status != False and quest05.status != True and sebas_kick == True:
        $ lothar_location = "No"
    if quest12.status > 4 and timenow.day < lothar_rest + 1:
        $ lothar_location = "No"
    with dissolve
    if not seen_lothar:
        $ seen_lothar = True
        jump Lothar_First
    else:
        show screen menu_buttons
        window hide
        call screen place_lusterfield01
    if _return == "To Alleyway":
        hide screen place_lusterfield01
        jump main_lusterfield_alleyway

    if _return == "To Kingspawn":
        hide screen place_lusterfield01
        jump main_kingspawn

    if _return == "Lothar":
        jump Lothar_Dialogue

    if _return == "To Green Forest":
        hide screen place_lusterfield01
        jump main_green_forest

    if _return == "To Lusterfield2":
        hide screen place_lusterfield01
        jump main_lusterfield02


label main_lusterfield02:
    $ current_location = "lusterfield02"
    $ renpy.music.play(mLusterfield, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ timenow.minute += 3
    $ timenow.passTime()

    if isNight():
        scene lusterfield02_night
    else:
        scene lusterfield02
    with dissolve
    show screen menu_buttons
    if quest37.status == 2 and timenow.day == quest37.start_date + rahim_vote_duration and timenow.hour >= 12 and timenow.hour < 23 and vote_choice[0] == 0:
        jump Rahim_Vote_Day
    if quest37.status == 2 and timenow.day > quest37.start_date + rahim_vote_duration:
        jump Rahim_Vote_Day_Late
    if quest22.status == True and quest22.completed_date < timenow.day - 2 and quest26.status == False and vurro_lives == True and wuldon_meet == True and (slime2_dp[1] == 0 or slime2_dp[1] == []):
        $ slime2_dp[1] = 1
        "Right as you walk into the main square, in front of Cane's tavern, You hear a shout from over to your right, where you normally meet Jog and Amble."
        my "Hey, [e] get over here!"
        "Realistically, you should head over there now, but it's honestly up to you at the end of the day."
        jump main_lusterfield02
    window hide
    call screen place_lusterfield02
    hide screen menu_buttons
    if _return == "To Nocturnal Trunk":
        hide screen place_lusterfield02
        jump main_nocturnaltrunk

    if _return == "To Rahim":
        hide screen place_lusterfield02
        jump main_rahimshop

    if _return == "To Lusterfield":
        hide screen place_lusterfield02
        jump main_lusterfield01

    if _return == "To Range":
        hide screen place_lusterfield02
        jump main_lusterfield_range

    if _return == "Board":
        jump Lusterfield_Courier_Board

    if _return == "Haimo":
        jump Haimo_Dialogue

label main_lusterfield_alleyway:
    $ current_location = "lusterfield_alleyway"
    $ renpy.music.play(mLusterfield, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ timenow.minute += 3
    $ timenow.passTime()

    if isNight():
        scene lusterfield_alleyway_night
    else:
        scene lusterfield_alleyway
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_lusterfield_alleyway
    if _return == "Dummy Battle":
        jump dummy_battle
    if _return == "To Lusterfield":
        hide screen place_lusterfield_alleyway
        jump main_lusterfield01


label main_rahimshop:
    $ current_location = "rahimshop"
    $ renpy.music.play(mRahim, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ timenow.minute += 3
    $ timenow.passTime()
    call Lusterfolk_Schedule from _call_Lusterfolk_Schedule_2



    if isNight():
        scene rahims_house_night
    else:
        scene rahims_house
    with dissolve
    if rahim_recon == 0 and quest23.status == True and (quest16.status == True or quest32.status == True) and renpy.random.random() > 0.5:
        $ rahim_recon = timenow.day
        jump Rahim_Reconciliation_Begin
    if quest37.status == True and timenow.day > quest37.completed_date and (quest42.status == False and quest43.status == False):
        jump Rahim_Vote_Day_After
    show screen menu_buttons
    window hide
    call screen place_rahimshop
    if _return == "Craft":
        hide screen menu_buttons
        $ hovered_item = None
        $ selected_recipe = None
        $ discoveredrecipe = checkDuplicateRecipe(discoveredrecipe)
        call screen craft_screen
    if _return == "Drawing":
        "A series of drawings scatters around the house, but you notice two distinctively different style in them, one looks like innocent doodles, while the others are almost exclusively detailed drawing of a young Rahim."
        "One of them describes his choice of clothes. And the arrows point to the materials used and sewing techniques."
        if rahim_location == "rahimshop":
            e "Hey Rahim, who drew these drawings?"
            "Rahim turns his head towards the wall half-heartedly, before turning again to stare at you."
            r "Who do you think?"
            e "Uhm... I- uh I don't want to guess."
            r "The better looking ones were my former wife's. She has a tendency to draw whatever was in front of her eyes."
            e "I see, it seems you were in front of her eyes a lot."
            e "And, I'd say she captured your handsomeness perfectly. You looked pretty cheerful in the drawings."
            "You turn to Rahim, waiting for a response, but it seems he'd already returned to work."
    if _return == "Tanning":
        "A tanning station with a stack of some leathers of uneven shapes, waiting to be tanned for use in certain equipment and clothing."
        "You don't doubt these are ethically collected."
    if _return == "Basket":
        "A basket full of miscellaneous items placed on the ground, one of them were a golden badge, seemingly from somewhere fancy."
        if rahim_location == "rahimshop":
            e "Rahim, what's the use of this basket over here?"
            r "Hey, don't put your dirty hands on my old stuff, they're most delicate and flimsy."
            e "I saw a crown, and... a badge? Are they yours?"
            r "These were leftovers from when I tailored the king's wardrobe."
            r "Obviously, when I retired from the palace, we left on good terms, so I took some high-quality fabric and sundry items for myself."

    if _return == "To Lusterfield2":
        hide screen place_rahimshop
        jump main_lusterfield02

    if _return == "Rahim":
        jump Rahim_Dialogue

    jump main_rahimshop


label main_lusterfield_range:
    $ current_location = "lusterfield_range"
    $ renpy.music.play(mLusterfield, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ timenow.minute += 3
    $ timenow.passTime()

    call Lusterfolk_Schedule from _call_Lusterfolk_Schedule_3
    if timenow.day > 20 or task02.status != False or task03.status != False:
        $ summery_farmland.discovered = True
    if isNight():
        scene lusterfield_range_night
    else:
        scene lusterfield_range
    with dissolve
    if quest37.status == 2 and timenow.day == quest37.start_date + rahim_vote_duration and timenow.hour >= 12 and timenow.hour < 23 and vote_choice[0] == 0:
        jump Rahim_Vote_Day
    if quest37.status == 2 and timenow.day > quest37.start_date + rahim_vote_duration:
        jump Rahim_Vote_Day_Late
    if quest37.status == True and vote_result >= 0 and timenow.day > quest37.completed_date and not lothar_met_after_pact:
        hide screen menu_buttons
        jump Lothar_Voting_After_Pact
    if quest43.status == 2:
        hide screen menu_buttons
        jump Furkan_Enter_Mayor_Longhouse
    show screen menu_buttons
    if quest22.status == True and quest22.completed_date < timenow.day - 2 and quest26.status == False and vurro_lives == True and slime2_dp[1] == 1:
        $ slime2_dp[1] = 2
        jump Jog_Wuldon_Quest
    window hide
    call screen place_lusterfield_range
    if _return == "To Lusterfield02":
        hide screen place_lusterfield_range
        jump main_lusterfield02

    if _return == "To Farmland":
        hide screen place_lusterfield_range
        jump main_summery_farmland

    if _return == "Amble":
        hide screen place_lusterfield_range
        jump Amble_Dialogue

    if _return == "Jog":
        hide screen place_lusterfield_range
        jump Jog_Dialogue

    if _return == "To Longhouse":
        hide screen place_lusterfield_range
        jump main_lusterfield_mayors_longhouse

    if _return == "Poster1":
        "The paper is an old flyer reporting on the news. It writes:"
        "'Hear ye, hear ye, good folk of Lusterfield! Our beloved champion, Lothar the Brave, has once again proven why his name echoes in the hearts of Lusterfolks!'"
        "'Yesterday, a dire threat descended upon our peaceful village — a loincloth thief, caught by the local tailor, fled across the streets and brushed off a basket of oranges!'"
        "'With the courage of a goat-slayer, Lothar, strode forth to strike down the thief. Eyewitness report that our hero wrestled the loincloth from the hands of the running thief.'"
        "''It was like lightning - Lothar shoved that guy into the ground in one swoop!' Witness proclaimed.'"
        "'The thief was quickly apprehended by the hero. 'It's not fair, the whole village can smell that bull's musk from streets away.' The loincloth thief is now prohibited from using the local clothsline.'"
        "'But the stolen loincloths, lost in the chaos, are nowhe-'"
        "The flyer tears off from here."

    if _return == "Poster2":

        "'Archery Skill Showdown'"
        "'For every points won over the other, the winner gets to slap the loser's ass. Everyone gets three arrows.'"
        "'Bull's Eye is 10 points, the inner white ring is worth 5 points, then 3 points, then 1 points.'"
        "'Amble (Left) against Jog (Right)'"
        "'First shot, out of bound-'"
        "The note ends here."
        "There's another line behind the notes: 'Finally he said yes! I'm gonna slap his ass so much both cheek's gonna go red for weeks.'"

    if _return == "Open Chest":
        jump main_lusterfield_range_chest

    jump main_lusterfield_range

label main_lusterfield_range_chest:
    hide screen menu_buttons
    hide screen dungeon_buttons
    call screen range_chest()
    if _return[:2] == "Up" or _return[:4] == "Down":
        if _return[:2] == "Up":
            $ range_chest_number[int(_return[-1])] += 1
        else:
            $ range_chest_number[int(_return[-1])] -= 1
        $ range_chest_number[int(_return[-1])] %= 10
    if _return == "Open Chest":
        if range_chest_number != [0, 2, 2]:
            "The metal clank against each other with a heavy, dull thud. It doesn't seem to be correct..."
        else:
            "With a swift twist, the tumblers behind the lock quickly fall into places, you can hear a smooth, subtle click before the chest's lid bounces up."
            "You push the lid up curiously, there doesn't seem to be a lot of items lying inside. It was mostly a pile of yellow leaves, papers with faded inks and some dried plum pits..."
            "Within the leaves, you find an old white rag that says 'small hyena, wanted alive, bounty 10 gold-' with the red doodle of a poorly-drawn face."
            "You also find two green ointments, and five pieces of patches scattered around the chest."
            "At the bottom of the chest, you find a wooden cylinder, it seems to be a flute of some sort."
            "There's a hyena head at one end, it looks primitive, the canines poking outwards does not resemble someone like Jog at all."
            "You can feel your mind fluttering as you hold the mouthpart in your hand, your eyes roll back as you find yourself staring at a group of gnolls surrounding something."
            "With a heavy breath, you return to reality once more, staring at the flute, you feel compelled to keep it for now."
            msg "The ruttish flute keepsake is added to your inventory. You can use the item to experience its past."
            $ addItem("Green Ointment", inventory, 2)
            $ addItem("Patch", inventory, 5)
            $ addItem("Ruttish Flute", inventory, 1)
            $ range_chest_opened = True
            jump main_lusterfield_range
    if _return == "Leave":
        "You stand up from the chest."
        jump main_lusterfield_range
    jump main_lusterfield_range_chest
default range_chest_number = [0, 0, 0]
default range_chest_opened = False
screen range_chest():

    add "lusterfield_range_chest_background"

    text str(range_chest_number[0]) color "#190702" font "moria.ttf" size 60 xalign 0.406 yalign 0.535
    text str(range_chest_number[1]) color "#190702" font "moria.ttf" size 60 xalign 0.5 yalign 0.53
    text str(range_chest_number[2]) color "#190702" font "moria.ttf" size 60 xalign 0.585 yalign 0.53

    imagebutton:
        xalign 0.85
        yalign 0.85
        idle "bedroom_arrow"
        hover "bedroom_arrow_hover"
        action Return("Leave")

    imagebutton:
        xalign 0.4
        yalign 0.338
        idle "lusterfield_range_chest_background_empty"
        hover nightHover("lusterfield_range_chest_background_up")
        action Return("Up 0")

    imagebutton:
        xalign 0.5
        yalign 0.338
        idle "lusterfield_range_chest_background_empty"
        hover nightHover("lusterfield_range_chest_background_up")
        action Return("Up 1")

    imagebutton:
        xalign 0.59
        yalign 0.338
        idle "lusterfield_range_chest_background_empty"
        hover nightHover("lusterfield_range_chest_background_up")
        action Return("Up 2")

    imagebutton:
        xalign 0.4
        yalign 0.778
        idle "lusterfield_range_chest_background_empty"
        hover nightHover("lusterfield_range_chest_background_down")
        action Return("Down 0")

    imagebutton:
        xalign 0.5
        yalign 0.778
        idle "lusterfield_range_chest_background_empty"
        hover nightHover("lusterfield_range_chest_background_down")
        action Return("Down 1")

    imagebutton:
        xalign 0.60
        yalign 0.775
        idle "lusterfield_range_chest_background_empty"
        hover nightHover("lusterfield_range_chest_background_down")
        action Return("Down 2")

    imagebutton:
        focus_mask "lusterfield_range_chest_background_side"
        idle AlphaMask("lusterfield_range_chest_background", "lusterfield_range_chest_background_side")
        hover nightHover("lusterfield_range_chest_background_side")
        activate_sound clickd
        hover_sound clickhover
        action Return("Open Chest")

label main_lusterfield_mayors_longhouse:
    $ current_location = "lusterfield_mayors_longhouse"
    $ renpy.music.play(mVote, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ timenow.minute += 3
    $ timenow.passTime()

    call Lusterfolk_Schedule from _call_Lusterfolk_Schedule_8
    if all(x == 1 for x in mayors_longhouse_moss.values()):
        scene mayors_longhouse_clean
    else:
        scene mayors_longhouse
    with dissolve
    show screen menu_buttons
    jump main_lusterfield_mayors_longhouse_loop

label main_lusterfield_mayors_longhouse_loop:
    if quest43.status == 3 and quest43.progress[1].status != True and all(x == 1 for x in mayors_longhouse_moss.values()):
        $ quest43.progress[1].status = True
        "After clearing the last patch of moss, you stand back to admire your efforts."
        scene mayors_longhouse_clean with dissolve
        r "Well, that's all of them. The place looks much better now, don't you think?"
        e "It does, it's a lot brighter in here as well, and the air's drier."
        "Rahim pats your back lightly enough to make you stagger forward. At least you've bought a faint smile from his face."
        jump main_lusterfield_mayors_longhouse
    call screen place_lusterfield_mayors_longhouse
    if _return == "To Range":
        hide screen place_lusterfield_mayors_longhouse
        jump main_lusterfield_range

    if _return == "Rhyme":
        scene mayors_longhouse_clean
        jump Mayors_Longhouse_Rhyme

    if _return != None and isinstance(_return, str) and _return[:4] == "Moss":
        show screen place_lusterfield_mayors_longhouse
        pause 0.75
        $ mayors_longhouse_moss["mayors_longhouse_moss"+ _return[-1]] = 1

    if _return == "Cabinet":
        jump Mayors_Longhouse_Cabinet

    if _return == "Planks":
        jump Mayors_Longhouse_Planks

    if _return[:7] == "Marking":
        show screen place_lusterfield_mayors_longhouse
        pause 0.75
        $ marking_num = int(_return[-1])
        $ mayors_longhouse_marking["mayors_longhouse_marking"+ _return[-1]] = max(list(mayors_longhouse_marking.values())) + 1
        if max(list(mayors_longhouse_marking.values())) > 5 or mayors_longhouse_marking["mayors_longhouse_marking"+ _return[-1]] is not marking_num:
            $ mayors_longhouse_marking = {"mayors_longhouse_marking1": 0, "mayors_longhouse_marking2": 0, "mayors_longhouse_marking3": 0, "mayors_longhouse_marking4": 0, "mayors_longhouse_marking5": 0}
        if mayors_longhouse_marking == {"mayors_longhouse_marking1": 1, "mayors_longhouse_marking2": 2, "mayors_longhouse_marking3": 3, "mayors_longhouse_marking4": 4, "mayors_longhouse_marking5": 5}:
            hide screen place_lusterfield_mayors_longhouse
            jump Mayors_Longhouse_Going_Downstairs

    jump main_lusterfield_mayors_longhouse_loop


label main_nocturnaltrunk:
    $ current_location = "nocturnaltrunk"
    $ timenow.minute += 3
    $ timenow.passTime()
    $ renpy.music.play(mTavern, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call Lusterfolk_Schedule from _call_Lusterfolk_Schedule_4
    if isNight():
        scene nocturnaltrunk_night
    else:
        scene nocturnaltrunk
    with dissolve
    if trunk_last_enter_day < timenow.day:
        $ updatePatronSeat(trunk_patron, timenow.day - trunk_last_enter_day)
        $ trunk_last_enter_day = timenow.day
    if quest45.status == 3 and timenow.hour > 4 and timenow.hour < 8 and cane_dialogues.get("Moth Route", False) == "Stew":
        jump Cane_Voting_Quest_Stew_Route_Meet
    if quest45.status != False and timenow.hour > 11 and timenow.hour < 17 and cane_dialogues.get("Rat Patron Day", False) < timenow.day and cane_dialogues.get("Rat Patron Leave", False) != True and quest37.start_date + rahim_vote_duration - 1 >= timenow.day and not cane_dialogues.get("Rat Patron Leave", False):
        $ trunk_patron["Front"]["Current Seat"] = "Rat"
    if trunk_patron["Front"]["Current Seat"] == "Rat" and cane_dialogues.get("Rat Patron Leave", False):
        $ trunk_patron["Front"]["Current Seat"] = None
    if quest32.status == 2 and ((quest32.start_date == timenow.day and timenow.hour > 18) or (quest32.start_date == timenow.day - 1 and timenow.hour < 3)):
        jump Sebas_Night_Out_In_Tavern
    if not seen_cane:
        $ seen_cane = 2
        jump Cane_First
    if seen_cane == 2 and cane_bet == True:
        $ seen_cane = True
        jump Cane_Second
    if quest16.status == 3:
        jump Event_Party01
    if quest40.status == 2 and timenow.day == quest37.start_date + rahim_vote_duration - 1 and timenow.hour < 23 and timenow.hour >= 20 and sebas_location == "nocturnaltrunk":
        menu:
            "It seems it's around the time to follow Sebas, do you want to hide here and wait, or give up following him?"
            "Wait to follow Sebas":
                $ quest40.status = 4
                jump Jog_Vote_Follow_Sebas
            "Do not wait":
                $ quest40.status = 3
    show screen menu_buttons
    window hide
    call screen place_nocturnaltrunk
    hide screen menu_buttons

    if _return == "Guild":
        call Trunk_Guild_Dialogue from _call_Trunk_Guild_Dialogue

    if _return == "Drunk":
        call Trunk_Drunk_Dialogue from _call_Trunk_Drunk_Dialogue

    if _return == "Pair":
        call Trunk_Pair_Dialogue from _call_Trunk_Pair_Dialogue

    if _return == "Sneaks":
        call Trunk_Sneaks_Dialogue from _call_Trunk_Sneaks_Dialogue

    if _return == "Eater":
        call Trunk_Eater_Dialogue from _call_Trunk_Eater_Dialogue

    if _return == "Merchant":
        call Trunk_Merchant_Dialogue from _call_Trunk_Merchant_Dialogue

    if _return == "Fighters":
        call Trunk_Fighters_Dialogue from _call_Trunk_Fighters_Dialogue

    if _return == "Mage":
        call Trunk_Mage_Dialogue from _call_Trunk_Mage_Dialogue

    if _return == "Rat":
        jump Rat_Patron_Dialogue

    if _return == "Ole":
        jump Ole_dialogue

    if _return == "Sebas":
        jump Sebas_dialogue

    if _return == "Lothar":
        jump Lothar_Dialogue

    if _return == "Cane":
        jump Cane_JumpFirst

    if _return == "To Upstairs":
        if upper_explore == 0:
            $ upper_explore += 1
            jump Cane_First_Time_Upstairs
        jump main_nocturnaltrunk_upper

    if _return == "To Lusterfield2":
        hide screen place_nocturnaltrunk
        jump main_lusterfield02
    jump main_nocturnaltrunk2

label main_nocturnaltrunk2:
    $ current_location = "nocturnaltrunk2"
    $ renpy.music.play(mTavern, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ timenow.minute += 3
    $ timenow.passTime()
    call Lusterfolk_Schedule from _call_Lusterfolk_Schedule_5
    if isNight():
        scene nocturnaltrunk_night
    else:
        scene nocturnaltrunk
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_nocturnaltrunk
    if _return == "Guild":
        call Trunk_Guild_Dialogue from _call_Trunk_Guild_Dialogue_1

    if _return == "Drunk":
        call Trunk_Drunk_Dialogue from _call_Trunk_Drunk_Dialogue_1

    if _return == "Pair":
        call Trunk_Pair_Dialogue from _call_Trunk_Pair_Dialogue_1

    if _return == "Sneaks":
        call Trunk_Sneaks_Dialogue from _call_Trunk_Sneaks_Dialogue_1

    if _return == "Eater":
        call Trunk_Eater_Dialogue from _call_Trunk_Eater_Dialogue_1

    if _return == "Merchant":
        call Trunk_Merchant_Dialogue from _call_Trunk_Merchant_Dialogue_1

    if _return == "Fighters":
        call Trunk_Fighters_Dialogue from _call_Trunk_Fighters_Dialogue_1

    if _return == "Mage":
        call Trunk_Mage_Dialogue from _call_Trunk_Mage_Dialogue_1

    if _return == "Ole":
        jump Ole_dialogue

    if _return == "Sebas":
        jump Sebas_dialogue

    if _return == "Lothar":
        jump Lothar_Dialogue

    if _return == "To Upstairs":
        if upper_explore == 0:
            $ upper_explore += 1
            jump Cane_First_Time_Upstairs
        jump main_nocturnaltrunk_upper

    if _return == "Cane":
        jump Cane_JumpFirst

    if _return == "To Lusterfield2":
        hide screen place_nocturnaltrunk
        jump main_lusterfield02
    jump main_nocturnaltrunk2

label main_nocturnaltrunk_upper:
    $ current_location = "nocturnaltrunk_upper"
    $ renpy.music.play(mTavern, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ timenow.minute += 3
    $ timenow.passTime()
    call Lusterfolk_Schedule from _call_Lusterfolk_Schedule_6
    if isNight():
        scene nocturnaltrunk_upper
    else:
        scene nocturnaltrunk_upper
    with dissolve
    show screen menu_buttons
    window hide
    call screen place_nocturnaltrunk_upper
    if _return == "To Downstairs":
        jump main_nocturnaltrunk2
    if _return == "Cardy":
        jump Nocturnal_Trunk_Cardy
    if _return == "Patron4":
        jump Patron4_Dialogue
    if _return == "Pirkka":
        jump Pirkka_Dialogue
    jump main_nocturnaltrunk_upper



label Lusterfolk_Affection:

    $ lothar_affection = 10

    $ lothar_affection += (lothar_knows - lothar_argue - ole_told + lothar_flower_save + night_out_lothar + party01[2])

    $ lothar_affection += (lothar_like/15 - lothar_lies + golem_lothar + lothar_along - sebas_kick - lothar_know_sebas_suck - lothar_spar)
    $ lothar_affection += 1 if quest12.status else 0
    $ lothar_affection += 1 if quest05.status else 0
    $ lothar_affection += 1 if quest25.status else 0

    $ ole_affection = 10

    $ ole_affection += (ole_told + ole_compliment - ole_known + ole_trust_cane + ole_got_gwyd_answer)

    $ ole_affection += (ole_asked_sebas_suck + party01[1] - night_out_lothar + pirkka_negotiate)
    $ ole_affection += 1 if quest15.status else 0
    $ ole_affection += 1 if quest08.status else 0
    $ ole_affection += 1 if quest16.status else 0
    $ ole_affection += 1 if quest32.status else 0
    $ ole_affection += 1 if quest37.status else 0

    $ sebas_affection = 10

    $ sebas_affection += (sebas_like + sebas_night_out + sebas_asked + sebas_kick + sebas_suck)

    $ sebas_affection += (party01[0])
    $ sebas_affection += 1 if quest15.status else 0
    $ sebas_affection += 1 if quest32.status else 0
    $ sebas_affection += 1 if quest05.status else 0


    return

label Lusterfolk_Schedule:
    if isNight():
        if isWeekend():
            $ sebas_location = "nocturnaltrunk"
            if timenow.day > 14 and (ole_trust_cane or renpy.random.random() > 0.5):
                $ ole_location = "nocturnaltrunk"
            else:
                $ ole_location = "kingspawn"
        else:
            $ ole_location = "kingspawn"
            $ sebas_location = "kingspawn"
        $ lothar_location = "nocturnaltrunk"
        $ amble_location = "No"
        $ jog_location = "No"
        $ cane_location = "nocturnaltrunk"
    elif isMidnight():
        $ ole_location = "kingspawn"
        $ rahim_location = "No"
    else:
        $ lothar_location = "lusterfield01"
        $ sebas_location = "kingspawn"
        $ ole_location = "kingspawn"
        $ amble_location = "lusterfieldrange"
        $ jog_location = "lusterfieldrange"
        $ rahim_location = "rahimshop"
        $ cane_location = "nocturnaltrunk"
    if quest33.status == True and quest33.completed_date > timenow.day - 1:
        $ amble_location = "No"
        $ jog_location = "No"
    if quest20.status == 2 or (quest20.status == True and quest20.completed_date + 4 > timenow.day and not lothar_along):
        $ lothar_location = "No"
    if quest05.status != False and quest05.status != True and sebas_kick == True:
        $ lothar_location = "No"
    if quest12.status > 4 and timenow.day < lothar_rest + 1:
        $ lothar_location = "No"
    if lothar_hunting == True:
        $ lothar_location = "No"
    if quest35.status == True and pirkka_show_day + 1 < timenow.day:
        if timenow.day % 2 == 0:
            $ pirkka_location = "nocturnalupper"
        else:
            $ pirkka_location = "prattlefellmeadow"
    else:

        $ pirkka_location = "No"
    if quest39.status == 4 and ole_votequestminute >= timenow.anal():
        $ ole_location = "No"
    if quest38.status >= 3 and not isNight():
        $ amble_location = "riverside_crossing"
    if timenow.day < rahim_recon + 3 and rahim_recon != 0:
        $ rahim_location = "No"
    if timenow.day == quest37.start_date + rahim_vote_duration - 3:
        $ ole_location = "No"
    if quest42.status == 2 or (quest43.status != True and quest43.status != False):
        $ rahim_location = "No"
        $ furkan_location = "No"
    if timenow.day == quest37.start_date + rahim_vote_duration and quest37.status != False and 6 < timenow.hour < 22:
        $ rahim_location = "No"
        $ sebas_location = "No"
        $ lothar_location = "No"
        $ cane_location = "No"
        $ ole_location = "No"
        if quest40.status == True:
            $ jog_location = "No"
        $ amble_location = "No"

    return


label Sebas_dialogue:
    call Lusterfolk_Affection from _call_Lusterfolk_Affection
    hide screen menu_buttons
    scene black
    if isNight():
        if sebas_location == "nocturnaltrunk":
            scene nocturnaltrunk_night
        if sebas_location == "kingspawn":
            scene kings_pawn_night
    else:
        scene kings_pawn
    with fade
    if quest43.status == 2 and vote_result < 0:
        e "Sebas, are you ready to go to the Mayor's house?"
        s "Hey, I'll be there very soon, roomie. As long as you're there."
    if sebas_location == "nocturnaltrunk":
        if sebas_night == 0:
            show sebas grin
            with dissolve
            s "Good... Mo-rning fu-"
            s "You- ?? I-uh... h-haven't seen in... d-drink.."
            e "...Seb?"
            s "G-goo..."
            if ole_location == "nocturnaltrunk":
                e "Ole, is Seb alright?"
                o "Cane and his dudes were betting with Seb..."
                o "He's just drunk... Give him a couple hours and he'll be fine."
                e "A-alright."
            $ sebas_night += 1
            jump Sebas_Drunk_Talk
        elif sebas_night > 0:
            if sebas_drunk_day < timenow.day:
                show sebas grin
                with dissolve
                s "Good... Mo-rning fu-"
                e "...Seb... Why are you so drunk."
                s "G-goo..."
                if ole_location == "nocturnaltrunk":
                    e "Hey Ole, how much did he drink..."
                    o "Probably 5, I told him not to bet with Cane, but he kept losing..."
                    e "A-alright."
                $ sebas_night += 1
            else:
                s "...b-butt... hmmph..."
                e "I think I should leave him alone now..."
            jump Sebas_Drunk_Talk
    elif sebas_location == "kingspawn":
        if renpy.random.random() > 0.5 and isNaked():
            show sebas grin
            with dissolve
            s "Good Fucking Morning, [e]!"
            e "Good Morning, Seb!"
            s "Buddy, running around with your thing out... Is it for me?"
            e "Hmm... Do you want... to?"
            s "Hehe, Look I still have works to do. But if you keep walking around my shop naked I'm going to do something really reckless!"
            jump Sebas_Normal_Talk
        else:
            if sebas_tut == 1:
                show sebas grin
                with dissolve
                s "Good Fucking Morning, [e]."
                s "You literally slept through yesterday, we almost thought you were dead."
                e "Wait, did I really sleep for that long!?"
                s "Yes! Look outside, the sun is rising and shining for you! I guess our bed is too comfortable... but anyways how's your wound doing?"
                e "I'm feeling pretty well right now, Ole's ointment really worked!"
                s "Heh... He has his own recipe for all medicines like this, if you want to know more you can always ask him for some."
                show sebas normal
                $ sebas_tut += 1
                jump Sebas_Normal_Talk
            if sebas_tut >= 2 and timenow.hour in range(7, 13):
                show sebas grin
                with dissolve
                s "Good Fucking Morning, [e]!"
                e "Good Morning, Seb!"
                show sebas normal
                jump Sebas_Normal_Talk

            if sebas_tut >= 2 and timenow.hour > 13:
                show sebas grin
                with dissolve
                s "Good Fucking Morning, [e]."
                e "It isn't really morning now, Seb."
                s "Who cares, it's always morning with my roomies around."
                e "You're so silly."
                show sebas normal
        jump Sebas_Normal_Talk

label Sebas_Drunk_Talk:
    show sebas normal
    menu:
        s "M-mo...in..."
        "Ask how he is doing":
            jump Sebas_Drunk_How_Doing
        "Ask about his betting":
            jump Sebas_Drunk_Bet_Cane
        "That's all for now":
            jump Sebas_Drunk_End


label Sebas_Normal_Talk:
    show sebas normal
    menu:
        s "So... how can I help you today?"
        "Tell him to go to Rahim's House" if quest43.status == 0.5:
            jump Sebas_Ask_Mayor_Rahim_Talk
        "Go to Tavern with Sebas and Ole tonight" if sebas_night_out == True and quest32.status == False:
            jump Sebas_Rejoining_Night_Out
        "Talk about the night with the wagon" if (quest40.status == True or quest40.status == 4) and sebas_caught and not sebas_talkaftercaught:
            jump Sebas_After_Castor_Caught
        "Learn his opinion on the vote" if quest37.status == 2 and quest37.start_date + rahim_vote_duration >= timenow.day and quest39.status == False:
            jump Sebas_Voting_Opinion
        "Deliver the goods" if is_recipient("Sebas"):
            $ recipient_name = "Sebas"
            call Courier_Delivery_Dialogues from _call_Courier_Delivery_Dialogues_4
        "Pick up the delivery" if is_client("Sebas"):
            $ client_name = "Sebas"
            call Courier_Pickup_Dialogues from _call_Courier_Pickup_Dialogues_4
        "Ask about his opinion on the vote" if quest37.status == True and timenow.day < quest37.completed_date + 14:
            jump Sebas_Voting_Result
        "Ask about his night with Cane" if sebcane == 1 or sebcane == 3:
            jump Sebas_After_Cane_Tavern_Night
        "Ask where Ole is" if quest37.status != False and timenow.day == quest37.start_date + rahim_vote_duration - 3:
            jump Sebas_Voting_Ask_Where_Ole
        "Ask about Pirkka's Prose" if quest35.status == 3:
            jump Sebas_Prose_Ask
        "Ask about Postal Training" if quest01.status == 2 and quest02.status == False:
            jump Sebas_Postal_Training
        "Report to Postal Training" if quest02.status == 2:
            jump Sebas_Postal_Report
        "Go to the river with Sebas and Lothar" if quest05.status == 2 and quest05_epd <= timenow.day and isDaytime():
            stop music fadeout 1.0
            jump Sebas_Lothar_Adventure
        "Ask to relieve his stress at work" if quest05.status == True and sebas_sneak and isDaytime() and sebas_suck == 0:
            stop music fadeout 1.0
            jump Sebas_Under_Counter

        "Ask about after Ole's sickness" if quest15.status == 4 or quest15.status == True and sick_ask[0] == 0:
            jump Sebas_After_Sick_Quest
        "Ask about the time under the counter" if sebas_suck > 0:
            jump Sebas_Ask_Under_Counter
        "Ask about your outfit" if pc.armor["Clothes"] != None and pc.armor["Pants"] != None and quest09.status != False and quest09.status != True:
            if pc.armor["Clothes"].img == "Adventurer Armor" and pc.armor["Pants"].img == "Adventurer Leggings":
                jump Sebas_Ole_Outfit_01
            elif pc.armor["Clothes"].img == "Tavern Cloth" and pc.armor["Pants"].img == "Tavern Chaps":
                jump Sebas_Ole_Outfit_02
            elif pc.armor["Clothes"].img == "Flowy Robe" and pc.armor["Pants"].img == "Flowy Wrap":
                jump Sebas_Ole_Outfit_03
            else:
                "As you are about to ask, you realise you are not putting on the right clothes to judge..."
                jump Sebas_Normal_Talk
        "Check out the shop":
            jump Sebas_Shopping
        "Ask for his opinion on Goat Tribe" if quest06.status == True and quest06.completed_date + 1 < timenow.day and opinions_GoatTribe[0] == 0:
            jump Sebas_Ask_Goat_Tribe
        "Ask about Lusterfield{#SebAAL}":
            jump Sebas_Ask_Lusterfield
        "Ask about the shop" if sebas_suck == 0:
            jump Sebas_Ask_Kingspawn
        "Ask how he is doing":
            jump Sebas_Ask_Himself
        "That's all for now":
            jump Sebas_Dialogue_End

    jump Sebas_Normal_Talk


label Sebas_After_Cane_Tavern_Night:
    if sebcane == 1:
        $ sebcane = 2
    if sebcane == 3:
        $ sebcane = 4
    e "You were so drunk that night."
    s "It was fine. I had a drink at the tavern like usual. It's not like it was my first time to drink."
    s "Then I had a stern talking-to with the bat about you."
    e "A-a stern talk?"
    s "Well, I- I got sober pretty quickly, and I know you've been working there."
    s "The old bat sometimes gets out of line. You need to stand up against him."
    s "I told him to treat you better. And I believe I was quite persuasive. Quite very."
    "Seb's face blushes slightly at this point but you pretend not to notice."
    e "Thanks Seb."
    s "It's the least I can do for my Roomie!"
    jump Sebas_Normal_Talk


label Sebas_Drunk_Bet_Cane:
    e "Seb... how's your bet with Cane?"
    s "W-what? B-bear.... Coin? Y-"
    e "Can you hear me..."
    s "Uh... No? I w-will bet... 20 coins. Y-yeah."
    if ole_location != "nocturnaltrunk":
        menu:
            s "B-bet? Hmmm... b-n..."
            "'Bet' with drunk Sebas":
                e "He's going to bet his gold away to random stranger anyway, I might as well... take it."
                e "Ok. I'll bet 20 coins with you, Seb."
                s "B-bet..."
                s "12... 20... Hmmmph... hehe."
                e "You're really drunk, Seb."
                "You pretend to walk around the tavern. And then comes back with a grin on your face."
                e "Oh... You lost."
                s "...Ah...hahahaha...[e]...2-20."
                "Sebas takes his pouch from his bag, clumsily counting coins in his hand."
                s "20..."
                "You received 12 gold."
                $ pc.gold += 12
                $ sebas_drunk_day = timenow.day
                jump main_nocturnaltrunk2
            "Leave him alone{#sebasdrunk}":
                e "I think I should leave Sebas alone..."
                jump Sebas_Drunk_Talk
    else:

        o "Hey, [e]. don't bet with him... he's not thinking anything now."
        e "Alright, Ole."


label Sebas_Drunk_End:
    e "I should go now..."
    if ole_location == "nocturnaltrunk":
        o "Don't worry about us, I'll drag this little lion back when I'm done."
        e "O-ok... See you then, Ole."
        o "See you."
    else:
        s "..."
        "You wave to the drunk lion before leaving him alone in the tavern."
    jump main_nocturnaltrunk2


label Sebas_Drunk_How_Doing:
    e "Seb? Are you alright?"
    s "Hmmmm... ye. All... left."
    "Sebas points at his left direction and chuckles at his own joke."
    e "I thought I can hang out with Seb here..."
    e "Do you need anything? Seb?"
    s "Uh... U-hm.. Beer! I- uh... need uh beer. more... I told y-you I can take 6 bottles, 7-...uhh."
    if ole_location != "nocturnaltrunk":
        if LookForItem("Beer", inventory):
            menu:
                e "He seems... too drunk already. Should I give him... a beer?"
                "Give a beer":
                    e "Here's your... beer."
                    s "Bier Beer... uhh- t-thanks server."
                    "Sebas takes a beer from your hand and pour it straight into his mouth."
                    e "Hey... Slow down, Seb."
                    "The lion continues gulping down the alcohol like a whale gulping water. You look at him, can't decide if you are mesmerised or traumatised."
                    s "Haaaah...so... good."
                    "Sebas looks at his now empty bottle... and stares at you for a few seconds before laughing again."
                    s "S-server... you look like... a d-dragon. Like [e]."
                    s "I wanna... f-fuck your ass, [e]. Y-you're... so. hot. Hotty. hot-"
                    if sebas_suck > 0:
                        s "Hmmph... your mouth... it was s-so... good."
                    s "L-lemme hug you... and p-put yer good ass and mouth to use..."
                    "You are a little confused as to what's going on, or whether all of this is true."
                    "But he soon fell asleep... so you decide against asking nor confirming his words."
                    $ removeItem("Beer", inventory, 1)
                    $ sebas_drunk_day = timenow.day
                    jump main_nocturnaltrunk2
                "Refuse":
                    e "I don't think you should drink more, Seb."
                    s "Ugh. one star S-service. Hmm..."
                    jump Sebas_Drunk_Talk
        else:
            e "Hmm... I don't have any beer here."
            s "Ugh. one star S-service. Hmm..."
            jump Sebas_Drunk_Talk
    else:
        o "He's doing fine, just don't give him any beer."
        e "I won't."
        jump Sebas_Drunk_Talk


label Sebas_Ask_Under_Counter:
    e "Hey... Seb?"
    s "Hello! My favourite little furball."
    e "Do you... want to talk about last time, under the counter?"
    s "Haha. Well. You were really good, I'd give you that, but that customer almost scared me somehow."
    s "And yes. Ole knew."
    e "I guess we better not do that... in the public."
    s "Of course! If we have time, I'd tug you to my bed instantly."
    e "Ah... alright."
    jump Sebas_Normal_Talk


label Sebas_Ole_Outfit_03:
    show sebas normal at l1
    show ole normal at r1
    $ opinions_Outfit[8] += 1
    s "Hi, Roomy! You look different today... What is it?"
    "Seb frowns deeply as he studies you."
    e "Seb, it's the outfit! Rahim made this new outfit for everyday wear. He asked me to model it and ask your opinion on it."
    s "Of course I know that! I was only kidding with my best roomy!"
    "Seb runs away to touch the fabric."
    s "Wow, it's so fluffy!"
    "While Seb is examining the robe, his paws keep rubbing against your muscles and furs."
    s "It's so smooth too!"
    "Seb is so intrigued by the new fabric that he wants to touch every inch of it."
    "His hands slowly travel to the cloth that wraps around your waist."
    e "Seb... Wait..."
    "Seb is too absorbed by the new fabric that he doesn't seem to hear you."
    "Your crotch has reacted to Seb's continuous touching."
    "That has finally garnered Seb's attention."
    "With his hand still near your crotch, Seb shines a mischievious grin on you."
    s "Roomy, are you wearing nothing underneath?"
    e "Well... yes..."
    s "Cool."
    "Seb continues with his massage."
    s "I like this outfit. It makes things a lot more expedient."
    s "It means that I can technically take you right now? And no fabric standing in the way once I lift up the cloth around your waist?"
    "You gulp with anticipation and nod."
    "Suddenly, there was a cough that came from the corner of the shop."
    "You immediately freeze. You turn and see Ole standing there. Seb is still wrapped around you."
    o "Have you two forgotten that the shop is still open?"
    "You scratches your head awkwardly."
    e "Sorry, Ole. Didn't see you there."
    s "Oh, I know Ole is there. I thought my roomy would appreciate an audience."
    "you punch seb in his arm. Seb bounces away from you and chuckles."
    s "ouch, i was only joking."
    o "Anyway, you two can do whatever you want after business hour but i need you to focus when the shop is still open."
    o "[e], I also think you need a professional opinion with regards to your new outfit. Don't trust this blockhead that is blinded by lust."
    s "hey."
    e "Who do you suggest?"
    o "You've met Haskell, right? I believe he's familiar with robes as everyday wear. You should go find him at the apothecary."
    jump main_kingspawn


label Sebas_Ole_Outfit_01:
    $ opinions_Outfit[2] += 1
    show sebas normal at l1
    show ole normal at r1
    s "Roomie! Oh Wow, you cut a stunning figure in that new armor of yours."
    o "Is it the leather armor Rahim has promised you?"
    o "It really fits you really well. No wonder it has taken him so long to make."
    "Seb is still looking at you with twinkling eyes."
    e "So I take it that you two like this? Rahim would like to get some feedbacks."
    o "Of course. I can see the effort and heart he has put into it."
    s "Roomie, you are so dashing! It'll take no time for you to replace that snotty wolf as the hero."
    s "Then, perhaps you'll get some customer perks exclusive to the hero."
    "Seb grins mischievously at you."
    jump main_kingspawn


label Sebas_Ole_Outfit_02:
    $ opinions_Outfit[5] += 1
    show sebas normal at l1
    show ole normal at r1
    s "Good Fucking Morning, buddy."
    s "Oh? Another new outfit?"
    o "As we know, Rahim is ever the overachiever."
    "Seb looks at your crotch and frowns."
    "You feel rather bothered and hot."
    s "Roomie, is this really comfortable?"
    "You are confused because you do not expect this question."
    "Seb must have noticed your expression."
    s "I mean that pair of briefs looks pretty tight."
    s "Can you even fit everything in?"
    s "I am sure I can't."
    "Seb guffaws. Ole shakes his head weakly."
    "You know Seb is only joking but your head can't help but wander off to Seb's crotch."
    "You can see Seb's bulge through the kiln he's wearing."
    "Try as you might, you can't help but picture Seb in the outfit you are wearing. Perhaps your roommate is right."
    "He might really destroy Rahim's clothing. But the mental image of that is really turning you on."
    "You feel a nudge from your side."
    o "[e], are you alright? Your face is all flushed."
    "Ole looks at you with concern."
    e "Erm. Of course. I..."
    "You try to calm your wandering imagination and focus on the issue at hand. You do not want an accident."
    s "Ole, my buddy. What about you? Do you think you can fit in it?"
    o "What are you talking about?"
    s "Oh. I'm just kidding. Looking over the shop for the whole day has been quite boring."
    "Thankfully, Seb and Ole are too busy bantering. Because your dick is starting to harden from picturing Ole in your outfit."
    "Seb and Ole. You wonder who would look better."
    "You wonder if this is the effect of this outfit, because you find it easier to wander over to sexual thoughts."
    "While Seb and Ole are laughing about something, you shuffles off to your room."
    e "Thanks guys for the comments. I'll be telling Rahim about them."
    "Ole and Seb watch you scurry away."
    o "But why is [e] running to his room if he's going to report to Rahim?"
    s "Ole, haven't you noticed? Our courier probably needs some private time first!"
    o "Huh?"
    o "AHH! Nevermind! I get it..."
    jump main_kingspawn


label Sebas_Ask_Lusterfield:
    menu:
        s "What do you want to learn about us?"
        "Ask about the villagers":
            jump Sebas_Ask_Lusterfield_People
        "Ask about Lothar" if seen_lothar and quest05.status == False:
            jump Sebas_Ask_Lusterfield_Lothar
        "That's all I needed":
            jump Sebas_Normal_Talk

label Sebas_Night_Out_Quest_Begin:
    show sebas grin at l1 with dissolve

    "As soon as you step into the main lobby of the pawn shop, you are greeted by a familiar face."
    s "Goooood Fuckin- Morning Roomie!"
    e "Gooood Morning Seb!"
    s "Got any time today?"
    e "Ehem... W-what do you mean?"
    s "Well I'd say we should get a drink at the Tavern, you and me. And Ole of course."
    "The lion tilts his head to his right and shouts."
    s "Hey! Ole! We're going there right?"
    "Before you turn your head, a scaled hand drifts into your hair and ruffles it."
    show ole understand:
        xalign 2.5
        linear 2 xalign 0.95
    o "Yes. Is [e] going too?"
    show sebas smug
    s "Of course he's in! This little buddy here deserves the best drink in the town."
    if task02.completedtimes > 0:
        "Sebas suddenly seems to remember something."
        s "I dunno what he puts in there actually, but what's important is that it tastes damn good."
        o "I don't love it like this guy does, but I can't deny that it's pretty good."
        s "You didn't even get to the mellow part! Ales are supposed to be quaffed, not sipped on."
    e "W-wait..."
    menu:
        "Go with Sebas and Ole?"
        "Accept Invitation":
            $ QuestBegin(quest32)
            $ quest32.qProgress(__("Hang out with the roommates"))
            $ ole_compliment = True


            e "hmm... Alright, I'll go with you guys."
            show ole smile
            o "That's great news, Seb's got a new drinking buddy now."
            "The lizard squats down, laying his head on the counter. He has the look of a man finally seeing the light at the end of a tunnel."
            show sebas grin
            s "Ha, we'll see, we'll see. The winner gets tea."
            s "...for Ole. We'll get a bunch of fucking beer!"
            e "Ahem... so! What's the plan...?"
            o "As usual, we'll meet at the Tavern."
            s "Meet us there at night time. Alright."
            s "Uh... No need to bring anything, we've got gold."
            s "But bring some for yourself so you can actually bet on something."
            if ole_trust_cane:
                o "I suppose that bat friend of yours can get you a bag of coins if you ever need one."
            else:
                o "Don't bring too much, you're gonna lose it to Cane anyway."
            "Ole chuckles, casually fidgeting with his dewlap."
            "You haven't ever seen Ole look this... this relaxed. He's always seemed so cautious, so attentive."
            "It Somehow comes as a surprise to you that he can actually relax, even as he closes his eyes in front of you."
            s "Well buddy, we'll see you there then."
            e "See you, Seb and Ole."
            o "Hmmph... I've told you this a few times, but, it's good to have you here."
            "Ole stands back up, and gets back to work."
            o "Remember to come tonight. We'll be waiting for you."
            jump main_kingspawn
        "Maybe Later":

            $ sebas_night_out = True
            e "Well I'd maybe, uh. I'll- Uhem..."
            "You have no idea what your brain is doing, but it's not going great. Only a mush of words comes out of your mouth, leaving the lion confused."
            e "I'll go with you guys next tim-"
            show sebas scared
            s "Why?"
            "The sudden injection of the lion caught you off guard. His tone is much more firm and stern than you're used to."
            e "I'll need to uhm... attend other businesses."
            s "But I'm your buddy, right?"
            e "Seb. I'm still here, I'll go with you whenever I'm ready."
            s "But I have been always ready for you."
            "Sebas stares at you, his mouth hangs agape. All the while Ole furrows his brows, interjecting."
            show ole bored
            o "Stop with the whining, Seb. Let him decide for himself."
            "The shop soon becomes silent as Ole finishes his sentence."
            "Sebas is still in shock. You didn't expect his reaction to be this strong. But he slowly calms down."
            show sebas normal
            s "I- uhm... yes. Well, sorry if I acted strange."
            e "You're fine with this... right?"
            s "I am. I'll probably just wait until the frivolous lizard is done with his inventory and we'll go to the Tavern."
            "The lion shifts back to his lively self quite quickly, as opposed to your expectation."
            show ole normal
            o "Well, this frivolous lizard isn't going to bring your drunk butt back home if you're still bubbling with your gabby mouth."
    s "Ha, he can't even beat a drunk lion in that disk game."
    s "He lost to me last time we did, it was soooo embarrassing. I was drunk as hell and I drank like a full barrel of that beer."
    o "I only lost because you begged me to take it easy to impress that someone else."
    s "Excuses!"
    o "Believe it or not, there was one time when we went there, you got so drunk you basically fell on the pile of bottles."
    s "That's not relevant to what we're talking about, you lost!"
    "You are not sure if Seb is still angry over your answer... but seeing him back to his old self is certainly a bit of relief."
    menu:
        e "Uhmm..."
        "Compliment Sebas":
            $ ole_compliment = False
            e "Give some credit to Seb, I think he may have really nailed the throw."
            show sebas laugh
            s "See? Even [e] agrees with my amazing talent at throwing."
            o "Don't get flattered. [e] is just being polite after you threw a tantrum at him just minutes ago."
            if sebas_suck > 0:
                s "Heh, if this is being polite then I'd gladly tantrum all over [e]... Is there something as tantruming?"
            else:
                s "Hey, that's not fair, I don't see him as rude at any point."
            e "I wasn't just being polite, I genuinely believe in Seb."
            s "Aww... Don't worry, [e]. Ole is just salty that I am your favourite roomie."
            s "His aiming was so fucking bad he hit a dude's crotch from the other side of the tavern. It's amazing actually how you can do that."
            o "Ok, you should go back to attend your table now before I take over the shop and kick you out of it."
            s "Oh No! I'm so scared!. Ha."
            show sebas grin
            "He turns back at you and gives your hand a huge squeeze."
        "Defend Ole":


            $ ole_compliment = True
            e "I don't think Ole's gonna unintentionally be that bad, and I doubt Seb's going to remember the score that vividly when he's drunk."
            show ole understand
            s "Really? Don't get fooled by this guy's appearance, he's a master of sucking at tavern games I tell you buddy."
            show sebas shocked
            s "His aiming was so fucking bad he hit a dude's crotch from the other side of the tavern. It's amazing actually how you can do that."
            o "[e] said it. You're too complacent just because I played one game badly."
            "Wait, Ole, you actually lost to a drunk Seb?"
            o "No... I mean, the ball there was chipped, it steered off mid-way there."
            s "See? I told you, it actually happened. Maybe you should join us next time so we can hang out, and see how bad this little lizard throws."
            e "O-okay! But I'll bet on Ole over a drunk lion any other day."
            show sebas grin
            s "Ha, you'll see, you'll see, you naughty little roomie."
            o "At least [e] has my back."
            "Ole gives you a gentle smile."
    s "Anyway, we shouldn't keep [e] here too long."
    s "But you have to remember to let me know when you have time, alright?"
    e "Yes, thanks Seb."
    s "Hehe."
    jump main_kingspawn

label Sebas_Night_Out_Before_Tavern:
    show sebas grin with dissolve
    s "Gooooo-d Fu-"
    "Sebas pauses."
    s "Anyway, [e]! we were just going to head out. Want to join us here?"
    e "I thought you two were there...?"
    show sebas:
        linear 1 xalign 0.05
    show ole normal:
        xalign 3
        linear 2 xalign 0.95
    o "If it didn't take Seb so long to pack his stuff we'd be there already."
    s "You're making me so nervous here looking at me all the time."
    "The lizard looks away as he opens the door for both you and Seb."
    s "Forget it, let's go..."
    scene black with dissolve
    pause 3 
    scene nocturnaltrunk_night with dissolve
    "The bell on the door clanks as you three have arrived at the Nocturnal Trunk."
    show sebas normal at l1
    show ole normal at r1
    "You are beginning to anticipate the familiar scent of alcohol and meat, the frequented patrons wave at you, seemingly greeting a familiar face here."
    "Sebas swiftly finds an empty table at the center of the tavern."
    if ole_compliment:
        o "Well, take a seat here, [e]."
        "Ole drags out a chair gently, gesturing you to sit between Ole and Sebas."
    else:
        "You take the empty seat between the lion and the lizard."

    jump Sebas_Night_Out

label Sebas_Night_Out_In_Tavern:
    show sebas grin at l1
    show ole normal at r1
    s "H-hey! Goooooo-d Fuckin- Morning- [e]-."
    o "Heya!"
    "You notice the two familiar faces in the Tavern, one is Sebas, and the other Ole. You wave at them, heartily walking towards the two shopkeepers."
    if ole_compliment:
        o "Well, take a seat here, [e]."
        "Ole drags out a chair gently, gesturing you to sit between Ole and Sebas."
    else:
        "You take the empty seat between the lion and the lizard."
    jump Sebas_Night_Out

label Sebas_Night_Out:
    $ renpy.music.play(mParty, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    show sebas normal at l1
    "As you settle, you lean forwards in anticipation, waiting for shopkeepers to start talking."
    "But immediately, you notice both of them are staring towards your posture, causing you to sit up straight."
    e "Are you two doing alright?"
    s "Yep. So very alright, I've finally got my favorite roommate out."
    o "Not as so when I waited for almost an hour for Seb to actually get going."
    s "Hey, that's not my problem at all. It wasn't even evening and you closed the shop much earlier than usual."
    o "That should give you more time to organize your bags, not the other way around."
    show ole understand
    e "You two usually come here at this time right?"
    if ole_trust_cane:
        s "Well, Ole and I come here on the weekend."
    else:
        s "It's usually just me who comes to drink here on the weekend, sometimes I can get Ole to go with me, but it's not like he's drinking beer."
    o "I'm just cruising, bread is good enough for me."
    e "So, what are we doing here today?"
    s "We feast! That's what we do. That disk game looks available today, perhaps you should try it out."
    e "I suppose I have been in the Tavern more than a couple times."
    s "Yes but I can ask Cane to set up those little games here-"
    show ole normal:
        linear 2 xalign 0.3
    show sebas grin
    "Before Sebas finishes his sentence, you notice a familiar figure arriving to your table."
    "It's Cane, you can smell his scent from afar without even looking at him."
    show cane normal at r1
    s "Ha, talk of the devil."
    c "If it ain't my favorite customer and server on the same table! And the lizard fella too."
    c "What'cha like, same one beer for the lion eh?"
    s "The usual best dinner you have, and a pot of that hearty Hunter's Stew, with extra portions for my buddy right here."
    s "And give me the best of the best beer! I'm gonna get so fucking drunk tonight."
    "Cane chuckles as he writes down his order on a piece of paper."
    c "Sure, and lizard, ye in fer a treat today. We've got some rye bread fresh out of the oven."
    if ole_trust_cane:
        o "Alright, then I'll have two... or three."
        "Ole smirks."
        o "And give me some water please."
    else:
        o "It's fine, I'll just get a piece of maslin as usual."
        "Ole looks around, before reluctantly turning back to Cane."
        c "We're on it."
    menu:
        c "And lad, anything yer like?"
        "Ale" if task02.completedtimes > 0:
            $ night_out_order = 1
            e "I'll have some Ale."
            "Cane raises his brows slightly."
            c "Ain't cha hardy little fella. Alright, ale it is."
        "Beer":

            $ night_out_order = 2
            e "I'll have a Beer."
            s "You can have mine, heh. I've ordered lots of them just for me and you!"
            c "Then one more for the lad. How ya say, lion."
            s "Well, my beer is his and his beer is mine."
            "Sebas gives you a wink."
        "Bread":
            $ night_out_order = 3
            e "I'll just get some bread."
            c "Oh? Not drinking tonight eh?"
            o "He's staying sober so we can both drag Seb back home."
            c "Well we have rooms here."
            s "Not today, Cane. I have my best buddy [e] here, isn't that right."
    c "Alright then, we've got yer order."
    if nocturnal_serve > 0:
        c "And lad, remember to check us out more often, we've got a nice job fer ya."
    show cane:
        linear 2 xalign 4.0
    show ole normal:
        linear 2 xalign 0.95
    "Cane turns back towards his counter, preparing food and drinks for your table."
    e "So... what's a Hunter's Stew?"
    show sebas normal
    s "Oh? Didn't you work for the Tavern for quite a while? You should know that already."
    e "Hmmph... I didn't work in the kitchen, and it's not like Cane let me eat here. But it seems like the ingredients change every time I work here."
    s "Damn, how can he do that to [e]. The Hunter's Stew is pretty good here, but it depends on the day."
    e "W-why's that?"
    s "The hunters... namely, Lothar and others alike. Brings in meat and ingredients they collected today, and Cane puts them into a single stew."
    s "If they get something good today, we'll get to taste something good."
    e "And if they get nothing..."
    o "You'll still get something to eat, the stew is never emptied all the way, but it's replenished every day."
    e "S-so... I'll have something from yesterday's hunt?"
    "Ole nods."
    "The lion looks away for a second, and he smiles."
    show sebas laugh
    s "Well there he goes, and here he comes."
    show cane:
        linear 2 xalign 1.0
    "The tavern keeper arrives at your table with a plate full of beer, with some bread on the side."
    "Another plate comes with a variety of glistening meat pies, a pot of stew and a basket of fruits and tarts."
    "Soon, the table is filled to brim with food and drinks, with a very happy lion on the side, drooling."
    c "There ya go, enjoy the night fer me, young lads."
    s "Thanks a lot, Cane."
    "Cane chuckles, he gives the lion a pat on the shoulder, before leaving to serve another table."
    show cane:
        linear 2 xalign 4.0
    o "So, anything interesting going on lately, [e]?"
    show ole grin
    "Ole says as he scoops up a spoonful of the pottage, you can see him gulping down different ingredients cheerfully."
    e "I ran some errands for Haskell lately."
    s "Haskell? You mean the potions for our shop, right."
    e "Yeah."
    "Ole stands and scoops up another portion onto your bowl, dropping a huge chunk of meat inside."
    "He doesn't need to speak, just gestures for you to take the stew from his hand."
    if quest15.status == True:
        "You extend your arm to accept the bowl, only to lightly scrape against his scaled paws."
        "He gasps and flinches a little before you wrap your paws around it, feeling the warmth emanating from the handsome lizard."
        "Ole looks completely flustered, he puts the stew in front of you, as he sits and nudges against the back of his claws for some time."
    else:
        "You take the bowl of stew from Ole, thanking him with a slight nod."
    s "Ha, we were actually collecting materials for ourselves before you came along."
    show sebas grin
    s "But it really feels like you're part of the shop now, getting us materials and all."
    o "Yeah, we've got a lot of the strength potions sold so I'm just grateful [e] is here."
    e "And I'm happy that you didn't mind it taking some extra long time."
    "You slurp up the stew from your spoon, and you can feel the warmth of the variety of ingredients nourishing your whole body."
    "Meanwhile Sebas takes a bite out of the meaty pie. He never hesitates to show his messy side as oil and meat drips from his maw."
    s "Mhmm... yes."
    "He wipes away the mess with his palm, the lion notices you staring at him and grins foolishly at you."
    o "Well, I know it's just Haskell, he's mostly the one that takes his time, letting things go on their full course and all."
    o "He has been like this since I first met him, just habits of an old dragon."
    "Sebas burps as Ole continues talking."
    e "Yeah, and sometimes I just have tea with him in the forest."
    o "Hmm... You know, Haskell picked up on tea making only after I met him."
    o "He has a vast amount of knowledge on potion-making, but he grew bored of it at some point."
    if Haskell_Promise and task01.completedtimes > 0:
        o "I never talked to him about the potions anyway, the quality dropped pretty drastically since I asked you to bring them over."
        s "Ha- sch-we'll. I 'e-tsh he's b-ushy making ano-tshker round of tea for hims-schelf."
    else:
        o "The potions are still as good as ever, but he doesn't sound too pleased when I come over to his hut."
        s "Ye-r, he deed ent even off-shr me that herbal t-ehe was-sh mak-ching, wha'a a shel-bish jer-ksh."
        s "N-ot st-hat I 'refsh-er te-a over my 'rec-shious be'er, h-heh."
    "The lion talks with full mouth as he continues chewing through the meat, he doesn't even bother to enunciate his word clearly."
    "He also mutters something else, but it was too indistinguishable from the sputtering sound of the pie."
    show ole bored
    "Ole gives Sebas a side eye, the messy lion looks away, before swallowing the content silently."
    e "Perhaps he just likes making tea for himself."
    o "Well, the dragon did promise us he'd help with the shop when the shop first opened."
    o "But I can't blame him for losing his passion..."
    "A new idea comes across your mind, and that it might actually help both Ole and Haskell."
    e "You know what? I think there's a way that both of you'd be satisfied..."
    e "How about, ask Haskell to sell his tea in your shop?"
    show sebas laugh
    s "Oh? That's a good idea! We can make him sell his tea leaves and herbs, else those teas are gonna expire very quickly."
    o "You're right, just the plants would suffice."
    o "It's not going to sell that much like potions, but I bet some people in the town are going to like it a lot."
    e "I assure you, his tea is really great!"
    s "I don't doubt that, roomie. We'll have to take some notes, perhaps we should talk to the sleazy old dragon later."
    "Sebas takes a mouthful of the beer, leaving remnants of white foams on his snout."
    o "Alright, so... anything else?"
    call Ole_Night_Out_Chat from _call_Ole_Night_Out_Chat
    if night_out_order == 1:
        "You take a sip out of the Ale you ordered, the bitter and barley scent of the drink entices your snout, but the bitterness is too strong as you choke a bit."
        "The lion and the lizard stare at you with concern before you gobble down the rest of the drink."
        "Surprisingly, there's an aftertaste of the mellow and fruity sweetness emanating from within your throat, it was quite a refreshing drink."
        "You know you collected rosemary and barleys for the Ale, but you still wonder what other ingredients were put in there..."
        s "Haha [e], I told you the ale here is really good! And I heard you collected the ingredients for Cane, so it's extra good!"
        o "Oh? Really. Sad I didn't get to taste [e]'s Ale."
        s "Well O, the Ale is right in front of you."
        "The lizard quickly shakes his head."
        o "No, no. I told you I don't drink."
    elif night_out_order == 2:
        "You take a cup of beer from Sebas' pile. And begin gulping them down, a few drops of the beer spills right on your chest."
        s "Hey, take it easy, I- I don't even drink that fast."
        o "Well, I'm sure [e] is going to be a little more careful with his cup than you do with half a dozen cups of beer here."
        "You put down the empty cup, licking off the white foam around your lips."
        e "What were you guys talking about...?"
        o "Nothing at all."
    else:
        "You take a huge bite out of the bread in front of you, it was surprisingly soft and emitting a light scent of sourdough."
        e "O-oh, this is pretty good."
        s "Take it slowly [e]. Cane adds so much sourdough from this bread you might as well get drunk from it."
        o "Well maybe that's why they're so good."
        "Ole taps the side of his head in front of Sebas with a slight chuckle."

    s "Ha, well, [e]. Anything else going on with you?"
    call Ole_Night_Out_Chat from _call_Ole_Night_Out_Chat_1
    "Sebas doesn't hesitate to guzzle down another cup of beer, beer leaking from his mouth right down to his lower jaw."
    show sebas grin
    "Some of it drizzles on his loincloth, but he doesn't even seem to notice."
    s "A-ah... so-o good."
    s "Damn, it's really fun to hang out with you, [e]. Despite the bad stuff, at least we get to know what's going on with you more!"
    show ole understand
    o "Well, [e], whenever you're free, you can definitely hang out with us!"
    e "Thank you, you both are really flattering sometimes."
    s "I feel we're slowly becoming like a family. I remembered when I first met Ole, he was shy as hell! He was sitting in the forest alone there."
    o "That... that was so long ago, Seb."
    s "Anyway, Ole here doesn't really like me talking about ancient histories."
    o "And neither do you too."
    s "Uhm, anyway, we both settled in Lusterfield after his thing, and the thing is, we've been living together for like a decade, I see him just like a family."
    s "Sure, we took in roomies from time to time, but if you can settle here for the years to come, we'd just be like... family."
    show sebas grin blush
    "Sebas screams in excitement, you wonder if he's drunk or if he means what he said, but his usual bright grin convinces you it's the latter."
    e "I would like to live here for a long time too, Seb."
    s "Yeah! Stay for as looooooong as you wis-."
    "Sebas lets out a huge burp."
    "You chuckle slightly towards the embarrassed lion, as Ole takes another huge chunk out of his bread, finishing off the basket with a few bites."
    "The table is almost cleared all the way, only a few cup of beer left standing, and a stuffed roommate."
    show ole normal
    o "Looks like we're finished."
    s "We did, now it's time for Skittles, come on, [e]."
    "Sebas says with his glistening eyes, you have seen it played a couple times from when you work in the Tavern, but you still don't know how it works."
    o "Right, let's go then."
    scene black with dissolve
    pause 2 
    scene disk_tavern with dissolve
    "You follow the two towards a long lane in between tables of talking patrons, the floor seems to be varnished with shiny wax."
    show sebas grin blush at r1 with dissolve
    s "Don't you walk on the lane buddy, you're gonna slip and snap your back like a twig in winter."
    s "Should be good for some games... [e], have you played it before?"
    e "I've peeked at some patrons playing the game before, but I haven't tried it myself..."
    s "Well, you're missing a lot of fun in your work, aren't you. We just put bottles on the floor, and guess what. You have got to roll the disks towards the bull's eye, not the real one."
    show ole understand at l1 with dissolve
    o "You don't roll the disk, Seb. You'd just throw it there."
    s "I know. I know. I'm explaining it to [e]. Mister advisor lizard. Plus, rolling it sounds like a better game."
    o "That's the rule in the Nocturnal Trun-"
    s "Anyway, you just score more points the closer you get to the center."
    show sebas normal
    "Sebas pauses, you notice that he raises his head slightly, and you can feel a shadow looms over you."
    "The lion and the lizard do not look exactly surprised, or scared. So you turn around, and you are greeted by a leather glove right in front of your face."
    show ole:
        linear 2 xalign 0.3
    show lothar normal at l1
    l "Did someone say throwing disks?"
    show sebas bored
    s "Nobody said that, you can go now."
    e "Good evening, Lothar, good to see you in the Tavern. You wanna join us?"
    s "Hey-"
    show lothar grin
    l "Well, I'll have to say, apart from being the hero of Lusterfield. I am also a master of tavern games."
    l "S-so, how can you throw disks without the hero's demonstration!"
    s "The disks rented from Cane are only enough for three of us."
    o "And we can get a few more from Cane, it's very cheap-"
    s "Ole! The fuck are you talking about. We have no more disks."
    show lothar chuckle
    if sebas_kick:
        l "It's quite unfortunate that our little lion here has no dicks."
        s "You deaf or somethi-"
        l "It does show how he's afraid of losing to the hero of the village in a tavern game."

        s "Say that again Lothar and I will break your dick after that last time we met."
    else:
        l "You think I have forgotten the last time you went for the kick? Ha, that's right, you didn't even manage to do that."
        s "I'm not playing your stupid game, Lothar."
    "Ole glances at you, pointing at the lion and the wolf as he furrows his brows, and you both let out an awkward chuckle."
    l "You already know who's going to win, Ha, ask my disciple, he knows who's a better skilled player."
    show lothar normal
    s "I already know he's going to root for me, isn't it right, [e]?"
    show sebas normal
    "Both of them suddenly look towards you, you look left and right, can't even believe you have to make the decision again..."
    menu:
        e "U-uhmm...."
        "Lothar":
            $ sebas_disk_bet = False
            show lothar chuckle
            e "I'd say... Lothar? He has... good aiming, afterall... I mean maybe."
            show sebas bored
            l "Ha, see, my disciple knows who's the best."
            s "Well- let's see then, don't you lose this smug ass face when I beat you right here."
            "Sebas leaves as he walks to Cane and returns with some disks on his hand."
            s "Alright then."
            "He tosses the disks towards Lothar with full force, luckily Lothar catches them right before they smash into his face."
            "Still surprised, you and Ole each take some disks from Sebas' pile."
            o "Looks like everything's all set up here. Any questions?"
        "Sebas":
            $ sebas_disk_bet = True
            show sebas smug
            e "Perhaps Sebas. H-he... is tough? I-I'm not sure."
            show lothar bored
            l "My disciple, how does toughness even remotely play a role on one's bowlin-"
            s "You've heard [e]. Now get the fuuu-ck off before embarrassing yourself."
            l "Uuuuugh-... Watch out for your balls, lion. I'll be sure to kick them off the next time I see you."
            "Lothar doesn't look pissed as you would imagine, instead he looks... defeated. His eyes unfocused."
            "A scaled hand latches on his shoulder, it's Ole."
            o "Stay here, Lothar. I'll get you your disk."
            show lothar normal
            l "W-well. At least someone knows to respect their hero."
            o "More people makes for more fun."
            "As Ole walks towards the counter, Lothar stands in a weird pose between you and Sebas."
            show sebas bored
            "Sebas looks away, and Lothar just stares at you silently. You are not even sure how you got into this position of choosing in between these two."
            "But you are constantly dragged into it. Deep down you want them to hang around nicely, at least not arguing and getting mad at each other all the time."
            "You thought comes to a pause as Ole arrives with a few different coloured disks. He hands some to the flustered wolf before taking a few for himself."
            o "Any questions...?"
            s "Well, there's one right there."
            "He points towards the wolf."
            l "Cry more, lion. You're gonna prepare for when you lose against the hero."
            "You awkwardly stand in between the arguing pair, as Ole hands you and Sebas each three disks."
    show sebas normal
    e "Uh... one question... how do I get a good score?"
    s "Just aim, buddy."
    "Sebas smiles as Ole furrows his brows."
    o "Well, aside from your aiming, you also need to have enough {color=#d1e431}Strength{/color} to knock them down. Of course, {color=#d1e431}Agility{/color} definitely can help you aim better."
    o "Start at any position and just throw the disk out, see if you can get close to the bull's eye."
    o "And we'll play twelve rounds, three for each of us."
    show lothar normal
    l "Yeah, we know how to play the game, let's get started already."
    o "I'll go first then, Lothar next. [e]'s the third, and Sebas last."
    "Ole says as he writes down your names on a piece of yellow paper, before holding a disk for himself."
    call Play_Disk_Game from _call_Play_Disk_Game
    scene black with dissolve
    pause 3 
    scene nocturnaltrunk_night with dissolve
    show sebas grin blush at r1
    show ole normal:
        xalign 0.3
    show lothar drunk at l1
    "The game is finished, as Sebas and Lothar finish the last sips of their beer."
    "Their cheeks are all red now, eyes barely open, you're almost surprised how they're more peaceful after drinking."
    "Ole reads out the score he gets from the paper..."
    $ winner = disky.calculation()[3][0]
    $ winnerScore = disky.calculation()[3][1]
    $ fstrunner = disky.calculation()[2][0]
    $ fstrunnerScore = disky.calculation()[2][1]
    $ sndrunner = disky.calculation()[1][0]
    $ sndrunnerScore = disky.calculation()[1][1]
    $ lastplace = disky.calculation()[0][0]
    $ lastplaceScore = disky.calculation()[0][1]
    o "Ahem..."
    if winner == "Lothar":
        l "Well, unsurprisingly we all know who's going to win..."
        o "Ehrem, you're right, Lothar with [winnerScore] score won the game."
        "Ole claps with the paper still in his hand, Sebas soon follows suit, albeit sluggishly."
        s "Mhmmm..."
        e "Congrats!"
    else:
        show lothar normal blush
        if winner == "Ole":
            show ole smile
            o "Oh! I won, alright, with [winnerScore] score, congratulations to me!"
            "Ole claps with the paper still in his hand, Sebas soon follows suit, albeit sluggishly."
            l "Did we just lost to this fucking lizard, what is even going on..."
            l "Hey, lion. You just lost."
        elif winner == e:
            o "Hey! [e] just won the game with [winnerScore] score. That's quite a lot of score."
            "Ole claps with the paper still in his hand, Sebas soon follows suit, albeit sluggishly."
            e "Aw... thanks."
            l "Ugh, I swear my disciple has not surpassed me in any other form except this useless game."
            l "It's for fun anyway."
            l "As long as the winner is not this lion."
        else:
            o "Seb won with [winnerScore] score, hmm."
            "Ole claps with the paper still in his hand, Sebas soon follows suit, albeit sluggishly."
            l "Why are you clapping to yourself... lion. Ugh, the ego on this guy."
    "Lothar shakes Sebas' shoulder, who is still licking up the beer foam from the obviously empty cup."
    e "I think he's drunk."
    o "The second place is [fstrunner] with [fstrunnerScore] score."
    if fstrunner == "Lothar":
        l "At least I'm still better than this stupid lion..."
    elif fstrunner == "Ole":
        o "That's me! What a pleasant surprise."
    elif winner != "Lothar":
        l "Ugh, I just got a little rusty."
    show sebas:
        linear 1 ypos 2.0
    "Lothar turns to the drunk lion again as he collapses and passes out on the floor."
    e "Is... Seb alright?"
    show ole at l1 with move
    show lothar at r1 with move
    o "Yeah, I think so. He's just sleeping."
    show lothar grin
    l "And he's not listening to me. Hey, dumbass lion. Stupid ass lion. Say nothing if you love dicks."
    "It doesn't seem like Sebas is answering him anytime soon."
    l "Yes we all know that, hmm... Give me your pen, lizard."
    o "Oh? Don't go overboard with the drawing, Lot."
    l "Hah- You can hope."
    e "W-what are you doing, Lothar?"
    l "Revenge."
    show lothar:
        linear 1 yalign 1.5
    "Lothar takes the pen from Ole's hand, and he sits on top of Sebas' chest, getting incredibly close to Sebas face."
    "He's not being subtle, neither is he afraid of Sebas waking up, Lothar begins to scribble, staining Sebas' orange fur with black ink."
    l "This is good, look."
    pause 1
    "Watching from behind Lothar, you can see a... cock-shaped doodle being drawn dangerously close to the lion's mouth."
    "Looking from afar, Ole seems to be laughing along with you and Ole as he stares at Lothar's scribblings."
    "And Lothar draws a knot at the base of the shaft."
    show lothar chuckle blush:
        linear 2 xalign 0.95
    l "That's my cock in your face, stupid lion."
    show lothar:
        linear 1 yalign 1
    "You can see Sebas feeling something itchy on his face, his tongue sticks out and licks around the... cock-shaped doodle."
    l "Ha, he likes it, how does it taste, S-Seb."
    "Lothar stands back up, returning Ole his pen. He looks at both of you, unaware that you both are staring at the slight bulge in his crotch."
    o "Uhm... Alright. We should take Sebas home, Tavern people are watching us."
    l "Alright, but don't you clean that masterpiece off, it's too funny."
    s "m-mpph..."
    show lothar normal blush:
        linear 0.1 xalign 1.0
        linear 0.1 xalign 0.9
        linear 0.1 xalign 1.0
        linear 0.1 xalign 0.9
        linear 0.1 xalign 0.95
    "Sebas turns and tugs on Lothar's leg, drooling on his leather shoes."
    l "Ugh, you really need to bring him home now. Why was he drinking so much beer if he can't even handle it."
    "Lothar turns his attention to you."
    l "Regardless, I'll stay in the Tavern for a while."
    e "Your cheeks are still red, Lothar."
    l "Disciple, do I look like I'm gonna collapse at any moment?"
    o "No, but you seem like you need to rest."
    "Lothar chides, and he points his finger towards your direction."
    menu:
        l "Lizard can bring the lion back, you want to stay here for a while?"
        "Stay with Lothar":
            $ night_out_lothar = True
            e "I can stay for a while."
            o "Hmm... I'll take Seb home by myself then."
            o "And you two, don't stay up for too long."
            "You and Ole nod towards each other, and Ole begins tugging at Sebas."
            show ole at l2 with move
            show lothar at c1 with move
            "Lothar leads you to the counter in front of the tavern keeper."
            show cane normal at r1 with dissolve
            c "Aye-, back from tha- little disk game, eh?"
            e "Yeah, Ole's taking Seb back home. He's quite drunk."
            c "Bummer, he could-a stay here for a while. What about ya two? Drank a lot?"
            l "Not as much as that stupid lion did."
            c "Good. Then, enjoy the rest o- yer night. I gotta run errands for these hungry patrons."
            "Cane quickly leaves you two alone with a few extra cup of beer."
            show cane normal at r2 with move
            l "Mmmph... What do you think?"
            e "Oh?"
            l "Why did you choose to stay here."
            e "I just thought you wanted someone to hang out with."
            l "I have Amble and Jog. They just ditched me today to patrol the farm, as they said."
            "Lothar takes a gulp of the beer."
            l "But fair enough, your hero will accept your reasoning."
            "The wolf chuckles loudly, is he laughing at his own talk of heroism?"
            "Regardless, Lothar begins to talk with you again, telling you what he had done today or yesterday. It quickly spirals into a constant conversation."
            "Often you two pause for a few seconds before responding to each other. But unlike every other time, Lothar never sounds overly confident, or self-assured."
            "Instead, he's almost too natural, his voice a little deeper than the usual hero and disciple speech."
            "You feel you're no longer intimidated by his aura of dominance, you feel much safer, talking with him inside of this crowded tavern."
            "Sometimes he laughs with you for all the misfortune you've been through since you wake up in this world."
            "Sometimes you chuckles at how he and Jog messes with Amble without him ever noticing."
            "And it was... magical how that feels to have your mentor drinking beer alongside you, peaceful all around."
            "Most importantly, you get to know who Lothar is. Despite thousands of exaggerations thrown at your face each sentence, there's some form of truth buried inside."
            "You wish to talk with Lothar for the entire night, but at some point, you feel your eyelids droop. You lean on the counter and lie your head on your arms."
            "You two continue to talk for some time before you completely fall asleep."
            scene black with dissolve
            pause 3
            scene bedroom with dissolve
            "The next thing you know, it's already morning. You're inside your room, sleeping on your own bed."
            if lothar_spar:
                "Did he carry you back onto your bed like that time you lost to him...? You're not too certain."
            "It doesn't seem like Lothar is anywhere close to you..."
            "You went to bed again for a while before a scream interrupt your sleep."
        "Leave with Ole":
            $ night_out_lothar = False
            e "I should help Ole bring him home. And I'm tired and all."
            l "Well then, see you later, disciple."
            l "..."
            l "I have to say it again, but don't you two wipe that dick off his face."
            "You two nods towards Lothar as he leaves for the counter."
            show lothar at r2 with move
            show ole at c1 with move
            e "Mhmm... Ole, how do we carry him?"
            o "Usually I'd have you taking his arms and myself holding his legs. But I've prepared a cart just to carry him home."
            e "O-oh, so you didn't need my help?"
            o "Well, for the cart to work we first have to put him inside, right? I need you to take his arms."
            e "A-alright."
            "Your arms wrap around Sebas from behind under his armpits, you can sense the scent of beer, and faint musk coming from there."
            "Ole puts his legs first inside the cart, before you lower him inside of it."
            s "Mmmmph..."
            "You can still see the drawn cock on his mouth, clearly. And Sebas is drooling all over it as well."
            "Ole begins pushing the cart with Sebas inside, gesturing you to follow him."
            scene black with dissolve
            o "[e], was tonight good?"
            e "I enjoy spending time with you two, and Lothar."
            o "Yeah, more so if Lothar and Seb don't argue all the time. But, it was a lot of fun."
            if night_out_order == 3:
                o "Did you enjoy the food there? I thought the bread was amazing."
                e "You're right, I really like the rye bread."
            else:
                o "And at least you're not already drunk like Seb is."
            scene kings_pawn_night with dissolve
            "After a while, you arrive to the shop."
            o "Hey, [e]. Help me carry this cart upstairs."
            "You run in front of the cart, lifting it up and begin walking towards Sebas' room."
            "Soon, Ole gestures you to put the cart down, just for Ole to bring Seb onto his bed."
            o "Finally... another drunk Seb saved."
            e "That's great. I suppose you'd want to sleep too...?"

            o "Well, the problem is..."
            o "Usually, we share a bed. But I don't want him to vomit all over me while I'm sleeping."
            e "Oh, my bed's big enough for you, I think."
            o "If you don't mind, kiddo. I'd probably trust you not to throw up than this lion."
            "You and Ole walks downstairs towards your room."
            scene bedroom_night with dissolve
            o "Damn, it's still amazing how this room was full of crates, empty barrels and all."
            e "That was before I arrived here... right?"
            o "Yeah. That's right. I'd probably prefer you living in here instead, of course."
            o "It was a nice bedroom."
            scene black with dissolve
            "Ole sits on the bed, before fully leaning on your pillow."
            "You lie as near as you can without touching his scaled skin."
            "But it was his skin that touches you first, and his arm wraps around your shoulder."
            o "I lied about the bed, by the way. I just wanted to take a look at your room."
            o "..."
            o "I also lied about that."
            "You suddenly blush intensely, you can feel the lizard's hot breaths enveloping your face."
            "Is he right on top of you? The room is too dark to know exactly what happened."
            e "Ole?"
            o "S-sorry, I was just taking a good look at you."
            e "What are you doing...?"
            "You feel something soft taps your lips, it was Ole's finger, probably signaling you to be silent..."
            "The lizard let out a huge yawn as he returns to his position."
            o "Well, I'm exhausted."
            e "Me too."
            o "Good Night, roommate."
            "You head slowly leans into Ole's, as you soon drift into slumber."
            "..."
            scene bedroom with dissolve
            "The next thing you know, a glimmer of sunlight flickers on your eyes. It's already morning."
            "Ole is gone, he probably woke up before you did."
    "You try to close your eyes again to get some more sleep, before a scream interrupts your sleep."
    s3 "WHAT IS THAT THING ON MY FACE!!"
    s2 "OOOOOOO-OOOOO!!"
    "A calm and collected voice follows."
    s "YOU LET HIM DO WHAT?"
    "You hear a hysterical scream, followed with a long shout between the two shopkeepers."
    "Annoyed, you cover your ears with the pillow, and you snooze for at least a few hours."
    $ pc.sleep()
    $ timenow.addTime(0,15,0)
    $ QuestFinish(quest32)
    jump main_bedroom

label Ole_Night_Out_Chat:
    menu:
        "Talk about learning from Lothar" if night_out_talk[0] == 0:
            $ night_out_talk[0] = 1
            show sebas normal with dissolve
            show ole normal
            e "I learned from Lothar, like- a lot."
            s "Yeah, I still don't get why Ole here recommended you to learn from him. It's not like he's the only one that knows how to fight."
            o "Well, he definitely should be the best at it, regardless."
            s "You don't think I can beat him? I can literally kick him in the nuts, hard."
            if sebas_kick:
                s "I literally did, and he had to stay home for a whole day."
                s "My [e] here knows he's a fucking ass hat."
                o "Yeah I still don't get why you two are so obsessed with your nuts. It can cause some serious problems if you two are... regularly doing it."
                s "I can assure you after that kick he never appears in my shop, ever again, it was quite effective in that sense."
            else:
                s "Well, [e] stopped me. But I guess someone should be an actually responsible adult and stop the nuts kicking."
                o "I agree with [e], you two are just fighting constantly all the time for no reason at all."
                s "It's still better than you defending him for some reason."
                s "Whatever, I don't care about him. At least he's not coming into our shop now."
                s "For a hero like he claims to be, he's quite an example of what you shouldn't be, [e]."
                e "I thought his lessons were quite nice, to be fair. He was a decent mentor."
                s "Is that so?"
                "Sebas takes a sip of his beer, while Ole looks around."

        "Talk about attending Jog and Amble's training" if night_out_talk[1] == 0:
            $ night_out_talk[1] = 1
            show ole normal
            e "I attended battle training from Jog and Amble... it was quite good."
            show sebas bored
            "Sebas' eyes immediately squint upon hearing about Jog."
            s "Those two again, huh, found any gold missing in your pocket afterwards?"
            e "Uh... no? Probably?"
            s "Probably."
            "You can hear the change in Seb's tone when you mention them, you still are not sure what happened between them. But at this point, you don't even want to find out."
            o "Apart from certain personality and habits, I trust they possess some skills that can be useful for [e]."
            s "And maybe the problem is you trust too much, Ole."
            "Ole remains silent, he doesn't seem too startled by Sebas' response."
            e "So... why are you against them, Seb?"
            s "Amble's an honest guy, not like I've lived with him before. But the hyena is not someone you should hang out with."
            s "If you do, watch out for the backstabs."
            menu:
                "Defend Jog":
                    e "I don't think Jog is the person you think he is, Seb."
                    $ sebguessingmonth = int(timenow.day / 30)
                    s "I've known that thief for a decade. I know all his tricks, his jokes, everything about him."
                    s "You've only met him for how long? [sebguessingmonth] months at most."
                    e "B-but still, he doesn't strike me as someone who would... backstab."
                    o "[e] is still new around here, just change the topic."
                    "The lion pouts, he just guzzles down a whole cup of beer."
                    "You shudder for a second as Sebas slams the cup hard on the table, without saying a single word."
                    "Your table remains silent for a short while."
                "Stay Silent":

                    "You remain silent while the two shopkeepers talk among themselves."
                    o "Seb, honestly we shouldn't bring that up ever again. You're never going to get over it."
                    s "Get over what, that we kicked him out of our shop?"
                    o "You're like this everytime someone mentions him."
                    s "What's the fucking problem, O. That we live in this shithole of a village and we have to see his face every single fucking day?"
                    "The lion gulps down another whole cup of beer, before catching you staring at him in the eyes."
                    s "..."
                    "He calms down a bit, looking down at the cup."
                    s "Uhm... sorry roomie. It's not your fault."
                    "Ole moves his arm over the lion's shoulder, and pats on the back of his head lightly."
                    e "I-it's okay, Seb."
            o "Anyway, we should talk about something else."


        "Talk about Rahim's tailoring Job" if night_out_talk[2] == 0:
            $ night_out_talk[2] = 1
            show ole normal
            e "I started to sew up some clothes for Rahim."
            show sebas normal
            s "Oh? Rahim let you take care of his clients' orders? He didn't even let me touch his stuff."
            o "He did at one point, before you ruined the stitches of that whole tunic."
            "Sebas scoffs."
            e "Did Rahim know Seb did this?"
            s "No... that wasn't my fault, alright- I didn't even know how to stitch at that time."
            o "You also borrowed his sewing scissors to cut the paper in our shop."
            s "Stop, how am I supposed to know his scissors aren't for cutting stuff."
            s "And I gifted him another pair I got from the town, alright. It's not that big of a deal. I promise."
            "Sebas laughs awkwardly, while Ole squints his eyes towards him."
            show sebas bored
            s "Well, anyway, [e]'s got in touch with Rahim a lot too. Anything you learned from the grumpy old bull?"
            o "I trust he must have done a better job than you."
            s "Stop embarrassing me in front of [e], O-..."
            e "Uhm... I think I did somewhat of a good job?"
            if rahim_yarn == 1:
                e "Sometimes I stayed listening to him, just random stories. It was pretty nice talking to Rahim."
                o "Aw... It's such a rare occasion to hear him open up. You must be quite a special protégé."
                s "Oh yeah, Rahim's not the type to talk while working."
            else:
                e "I don't know, our conversation's been short. I just worked for him for some money."
                s "Ah, well most of us do too. He's not the type to talk that much."
            show ole understand
            o "How's he with Cane anyway, I didn't catch them speaking to each other..."
            e "I'm not sure, Cane was apologetic, but Rahim doesn't seem to respond well."
            s "Bummer. They were quite friendly before the whole goat thing started."
            s "A-and I assure you he's really trying to become quite a better bat. You should definitely see the improvement."
            if sebcane > 0:
                "You suddenly remember how he acted when he was with Cane in bed."
            else:
                "It was quite weird for Sebas to talk about Cane like that, perhaps they've been in touch a lot?"
            if ole_trust_cane:
                o "Well if you both say so."
                "Ole takes a bite off from his rye bread, he seems surprised at first, before chomping down the whole bread in his mouth."
                o "Now I see what you mean Seb, it's really an improvement."
                "Sebas and you chuckle at Ole's comment, it's quite rare for him to enjoy something other than cleaning, and much rarer for something made by Cane."
            else:
                o "I'll have to see for my eyes... regardless."

        "Talk about Furkan and Kari from the Goat Tribe" if night_out_talk[3] == 0:
            $ night_out_talk[3] = 1
            show ole normal
            show sebas normal
            e "Well... Did I ever tell you about.... What happened in the Goat Tribe?"
            s "Not that I've heard a lot from them, any juicy news we ought to hear?"
            "Ole raises his brows, both of them are looking at you, patiently waiting for you to speak."
            e "Just a lot of stuff happened, their general, Kari, told me that their leader was stuck somewhere in a cave, so I was kind of thrusted into their situation."
            if not kari_accompany:
                e "And I just went to the damp cave to get him out. And another guardian attacked me."
            else:
                e "We saved their leader, Furkan, back in the cave."
            s "Wait, how was Furk inside a random cave?"
            e "I didn't understand as much, just that, they needed to look for their guardian there, and something attacked him, stealing the basin that Furkan had."
            o "For a goat leader, Furkan wasn't the most careful type. I appreciate his courage though."
            s "And where is it now?"


            e "I don't know. The thef is still out there, we didn't even know why the two guardians went rogue in the first place."
            o "Perhaps someone out there was trying to fetch a good price with the basin."

            s "Or, they wanted to make more guardians, for themselves."
            if not ole_told:
                if not lothar_argue:
                    e "I just got there myself. They keep asking me about their leader, and Kari kind of threatened to hold me down..."
                    e "Lothar told me to pretend to pass out, but I had to fight back before they capture me."
                    o "Lothar?"
                    "Right upon hearing Ole's inquiry, you realize you had lied to Ole about the whole plan of infiltration before."
                    "You hold your breath, waiting for Ole's response, but he doesn't say anything."
                    s "Something wrong?"
                    show ole stare
                    "Sebas notices the awkward stare between you and Ole as he breaks out of contemplation."
                    o "What?"
                    s "S-sooo... what happened between you two?"
                    e "I'm just sorry I didn't tell Ole the truth about Lothar's plan."
                    o "Honestly, I-I... don't want to blame you, [e]. In fact, I'm just glad you turned out safe."
                    e "Ole..."
                    o "[e], I'm already over it. We should really move on before Seb gets bored to death."
                    show ole normal
                    "Ole gives you a faint smile."
                else:
                    e "I met the general in the forest, he was looking for Furkan."
                    o "Oh? He doesn't seem like the type to wander in the forest alone."
                    e "It was almost night. He found out about the guardian that Seb and I met back in the river. So he asked me to see if Furkan was there."
                    s "That golem? Well, we had a hunch it was from the goats. I thought these huge fellas should have been protecting their runes, or whatever the runes were in."
                    s "Did Furkan tell you what happened?"
                    e "No, I don't really know what happened, even after helping him I'm not sure if they'd share all of their secrets to me."
                    o "It was already a miracle Furkan trusted a stranger, not mentioning that you're living in Lusterfield."
            else:
                o "Well, Lothar did tell you to sneak into the tribe, if I remembered correctly."
                o "He's really stupid when it comes to asking someone to help him."
                s "Ha- you're giving him too much credit, O. I'd say he's just stupid."
                o "In any case, I've talked to him about you already, he won't be putting you in any dangerous situation again."
                e "Really? I didn't hear him talk about you that much."
                o "You're going to worry if he talks about me, ha. He's given me enough troubles already in the past."
                s "He's still a dumb wolf, I don't get why so many folks here still praise him like he's some kind of hero."
                s "Not mentioning that he's cooking up frictions with the goats, does he want another war or something?"
                e "I'm sure Lothar just sees them as being dangerous, he will come to his senses when he knows more."
                s "Ha, sure."
    return

label Sebas_Rejoining_Night_Out:
    $ QuestBegin(quest32)
    e "Hey, Seb. Do you think we can hang out today?"
    "Seb bounces up, he's suddenly more energetic than ever."
    s "Oh! You mean, like... hang out at night?"
    e "Yes, just like what I promised you last time we talked?"
    s "H-ha! Well, yes. I'll have to tell Ole we close the shop earlier, but..."
    s "I'll see you in the tavern tonight! Don't be late!"
    jump main_kingspawn

label Sebas_Not_Going_Night_Out:
    $ QuestFinish(quest32)
    "As you return to the shop, you notices the lion at the counter is watching you, he waves and walks towards your direction."
    s "Hey, roomie."
    e "Hello, Seb."
    "You didn't go to the Tavern with Seb, yesterday. That must be why Sebas looks this... grumpy."
    "Ole minds his own business, he either didn't notice you returning, or he didn't want to talk to you... Both are possible."
    s "You must be pretty busy last night... Yes?"
    e "Mhmm... yes. I'm sorry about ditching you, and Ole."
    s "Hey, don't be sorry. Of course you being there makes it more fun, but Ole and I could just be hanging out like normal."
    s "OOOOOO! [e] is here!"
    "The lizard reluctuantly turns to you, before putting on a slight grin."
    o "Good to see you alive, [e]."
    e "I'm so sorry to you both, you two must be waiting for so long..."
    o "Seb didn't wait for long before he finished up all the food and beer. I'll say you missed out on a lot of the food, though."
    e "Yeah, I probably did."
    o "Anyway, we are not jerking you or anything, but it was pretty fun last night, and I wished you were there, kiddo."
    s "I agree. but it was what it was, I hope you enjoy whatever you did last night though!"
    "Sebas pets your head for a few times, before returning to his counter."
    "You already feel quite bad for abandoning them, making them wait for you for the whole night."
    "And you feel even more guilty that they're not even blaming you..."
    "Regardless, you look at the shopkeepers keeping the pawn running. You hope someday you can show the worth of their kindness towards you."
    "..."
    jump main_kingspawn

label Sebas_After_Sick_Quest:
    s "Ole gave us quite a scare, didn't he?"
    "Seb looks over at Ole who is cleaning."
    s "But he's alright now."
    s "Glad to see that."
    s "Roomie, you've pulled through too. I'm not sure I would have stayed as calm without you."
    e "I'm sure you'll be fine without me, Seb."
    s "Not true, Roomie! It's nice to have someone with a clear mind around."
    s "Normally that person would be Ole but it's nice to know that we now have you too."
    $ sick_ask[0] = 1
    jump Sebas_Normal_Talk

label Sebas_Ask_Goat_Tribe:
    $ opinions_GoatTribe[0] = 1
    e "Seb! What do you think... about the goat tribe?"
    s "Oh yeah, I've heard about that letter, I think Rahim came and asked us afterward."
    e "Hmmph... Well. Which side are you leaning?"
    s "Look, [e]. I have no side. The only side is my side, which is pretty fucking huge."
    s "But I have to say, we lost a lot of business opportunity since we lost contact. It would be pretty great if we can... you know. Get them back."
    e "Oh..."
    s "I'll choose whatever you choose, buddy. Don't worry about me."
    e "Seb, why are you... so nice to me."
    s "I like seeing you smile, you're a good roommate."
    e "What about Ole?"
    s "He's fine. I'm just happy you're here."
    e "Me too... Seb."
    jump Sebas_Normal_Talk

label Sebas_Under_Counter:
    e "...Seb? Are you free... to hang out?"
    s "Hmm...? I'm working right now. Like, right now."
    e "But there's no one here."
    s "Ole is here. I can't sneak away to get some fuck with you."
    e "S-Seb! I think that wasn't what I meant."
    "Your face turns instantly red from Sebas' charming smile."
    s "Yeah, I know what you are thinking, this fluffy lion is so fucking handsome, aren't I?"
    s "Look, how about this buddy. Just sneak under the counter. And... do whatever you like."
    e "Ok. But Seb, are you sure...? I don't know if your customers are going to visit at any time."
    s "[e], it's my shop! I can do whatever I want! Plus, I'm super discreet about stuff like this."
    e "A-and... Ole?"
    menu:
        s "Don't worry. He's not gonna spank you or something if he finds out. He won't get angry because of this."
        "Sneak under counter":
            "You glance at Ole... who seems to be minding his own business, but you can feel that he knows what you two have been talking about..."
            e "Alright, how... do I-"
            s "Come on, and do whatever you want to this lion."
            "Sebas points at himself, putting up a huge grin on his face, his warm smile is warming your heart. You cannot believe it is happening, now."
            "Not just in a private setting, but somewhat out in the open. Like telling the whole world you are about to have fun with Sebas."
            "But it doesn't stop you, it makes you more excited instead. You climb under the counter as Sebas moves to adjust to his new leg space."
            e "Ouch..."
            "You head seems to hit something hard, but you quickly explore the area, and sit inside this tight dark space. The only thing is Sebas' fluffy but muscular legs."
            s3 "You like it there, buddy?"
            e "It's alright."
            "You hear a few footsteps towards the table, but it stops there."
            show sebas shocked at r1 with move
            show ole shocked at l1 with dissolve
            s "Ole?"
            o "Uhh... Look, I didn't see anything. I'll just check the goods upstairs."
            o "Enjoy yourselv-... I mean take care of the shop, Seb."
            s "O-ok... We'll be done soon..."
            hide ole with dissolve
            show sebas shocked at c1 with move
            "You can feel Ole going upstairs, he probably already knows about you two..."
            show sebas grin
            s "Look it'll be very quick. There's no one h-"
            "As soon as Sebas starts to speak, the shop door creaks and a customer walks in."
            s "Fuck..."
            "Sebas tries to act as normal as possible while you begin exploring his lower body."
            call Scene_Sebas_Under_Counter from _call_Scene_Sebas_Under_Counter
            "You wish to sleep right now, but Sebas has already pulled you up."
            "He tucks you to your bed and leaves you there."
            e "Good luck with your work, Seb."
            "Sebas nods at you, then goes back to pick up his discarded kilt."
            "You lie on the bed. Quickly you drift to sleep."
            $ timenow.hour += 2
            scene black
            with dissolve
            pause 1
            "..."
            scene bedroom
            with dissolve
            "You wake up slowly. Remnant of cum still remains on your face and fur."
            $ pc.add_active_status(soremouthed)
            $ sebas_suck += 1
            jump main_bedroom
        "Maybe next time":
            e "Uhh... m-maybe next time?"
            s "Aww... maybe. I'll be here if you need anything, like, anything."
            jump Sebas_Normal_Talk

label Sebas_Postal_Report:
    show sebas normal
    with dissolve
    e "Hey! Seb. I'm back from the green forest."
    s "Good to see you! Buddy! I was worried you're getting in trouble from the slime."
    e "I thought we were going to... train together?"
    s "Don't blame me on this alright, it was Ole's idea. He told me you have to get some experience in the wild."
    e "Yes, but... ok."
    s "Haha, don't be sad. Come on, let's take a look at what you got! You remember the 3 stones right?"
    $ item_number = LookForItemNumber("Stone", inventory)
    if item_number >= 3:
        show sebas grin
        with dissolve
        if item_number == 3:
            s "Hey, here it is, the three stones, you're really good at adventuring aren't you?"
        else:
            s "Hey, you got even more stones in your bag here, we should let you bring us all the materials in the shop, shouldn't we?"
        e "Well at least I brought you the stones you asked."
        s "Yeah, yeah. Not like I'm gonna sell them anyways. It just feels pretty good asking you to bring me some useless stones."
        e "Hmmph..."
        e "So... Seb. Is my training finished?"
        s "Yes! Of course! I'm gonna keep the stones here, to commemorate this special occasion."
        e "Thanks, Seb."
        s "You're welcome! And now I have to let Ole know about these stones, so pretty."
        $ quest01.progress[0].status = True
        $ QuestFinish(quest02)
        $ removeItem("Stone", inventory, 3)
        jump Sebas_Normal_Talk
    elif item_number > 0:
        show sebas normal

        s "[e]... I see... only [item_number] stones here. Are you sure there's enough?"
        e "Wait... really. I thought I had enough stones for you."
        s "Hey. No worries, you must have picked them up and lost some of them on your way here. Just go back and pick it up and it's gonna be fine."
        e "Of course! I'll report you back when I've got enough stones for you."
        s "Haha. You gotta stay safe on your way back there!"
        jump Sebas_Normal_Talk
    else:
        show sebas normal

        s "Wait... You don't seem to have any stones here... [e]?"
        e "..."
        s "Buddy?"
        e "I forgot..."
        s "Awww... It's okay. Really. Just go back and bring me 3 stones, alright? You can track it on your journal if you really forgot."
        e "I'm sorry, Seb. I'll bring you those 3 stones."
        s "Good! Don't be sad alright. Everybody makes mistake here. Come here, let me give you a hug."
        "Sebas walks around the counter and step towards you. He opens his fluffy arm and put them around your back, he hugs you tightly, bumping his head into you."
        s "Good roomie."
        "You can almost feel his hot breath on your face as he whispers to you, you want to bury your face into his soft manes, but he suddenly releases his grip on your back."
        s "Alright. See you later with the stones, buddy."
        e "...Yes, Seb."
        jump Sebas_Normal_Talk

label Sebas_Postal_Training:
    $ QuestBegin(quest02)
    $ quest02.qProgress(__("Collect 3 Stones"), "Stone", 3)
    show sebas normal
    with dissolve
    e "Hello, Sebas. Can I get a training from you."
    s "Of course you can, any time buddy! I have been waiting for you when Ol told me about the postal thing."
    e "Thanks, Seb. I really appreciate you spending time with me."
    show sebas grin
    with dissolve
    s "Like I said, any time with my little buddy."
    s "So Ole asked me to teach you expedition right, I'll keep it very short."
    s "You'll see you have three things I gave you yesterday, Journal, Inventory and Map."
    "You look at Sebas from his own counter, pointing his fuzzy paws onto the your bag."
    s "Look at the map in your bag, just imagine it is something you can click in the bottom right corner."
    s "What am I saying. Click? What a dumb comparison, haha. Just open your map, alright."
    e "Ok..."
    s "Aha, you are really smart! Ok, ok. You see the shapes right, it's a magical map, one I bought from an auction in the town."
    s "It will show locations you have explored for now, if you have not sneaked away from the village, right now it will only show Lusterfield and the green forest."
    e "I see the green forest in the south. Is that correct?"
    s "Yes, Ok. There's not a lot to teach if we're not there. Let's go there, us two."
    e "Really, now?"
    s "Yesss, come on. You and me. Mister [e] and Sebas."
    e "O-ok!"
    "Sebas grabs your hand tightly, and jogs right from the cashier towards the door, tugging you behind him. You can barely follow him with the speed he is going."
    jump Sebas_Expedition

label Sebas_Expedition:
    scene forest
    with fade
    show sebas normal
    with dissolve
    "After a few minutes, you and Sebas has arrived to the green forest, he soon releases his grip on you, but you can still somehow feel the warmth from his fluffy paws."
    s "Here we are. Oh... I'm your teacher now, so exciting!"
    s "Haha, Ok. Ok. [e]. The thing here is different than our village area. You'll see that you can explore the area."
    e "Sebas, you seem really excited being here."
    s "Aren't you? We first met here, on the grass bed. And the forest too! It's so green here."
    s "Anyways, I can't stay here long enough for us to really take in the nature-y nature here. Holy hell, [e], look at this."
    s "It's tulip on a tree! I've never seen a flower growing out of there, not mentioning it's a fucking tree! Woah!"
    e "Seb-"
    s "Ahhh- There it is, my favourite rock. It's mineral actually. Look at its shiny surface. I want to keep it for my pawn shop. That can surely fetch a good price."
    e "S-"
    s "Wait- Is that a colony for ants? I can see the holes and those little guy running around like it can't see. What a silly creature."
    e "Seb!"
    "The lion's joyful adventure in the green forest was brought to a halt, he freezes for a second before turning back to you."
    s "Heyy! [e]! I almost forgot about you. The most beautiful product of nature. Let's see. What was I talking about."
    e "Did you just forget we're in a middle of some sort of training?"
    s "Sorry buddy, I had a train of some crazy thoughts going on right now. Ok. A- sorry I was just really excited!"
    show sebas normal
    with dissolve
    s "It's super easy, alright. You can explore the surroundings. Sometimes there will be scary enemies to attack you, or cool things you can marvel at."
    s "Look, there's a stone right there, if you explore enough. Surely you can collect some rocks, minerals, stones all sort of things."
    s "So that's it, that's the training."
    e "That's it? Seb, we've just been here for 3 minutes."
    s "Alright what do you want, some real expedition in action? I'm still running a business in Lusterfield, I have to get back before Ole gets angry at me."
    e "Ok... I thought we're gonna-"
    s "You know what you can do? You can collect some stones, and then report back to me. Is that a training you can get behind with?"
    e "You're not coming along?"
    s "I gotta get back! Plus, you can learn to read maps, and arrows for directions."
    e "Alright Seb. You are really gonna leave me here."
    s "Don't worry it's a part of the fun. I promise the next time we go out like this, we're gonna do something entirely different."
    e "Oh...? Wha-"
    s "You and me."
    "Sebas looks deeply into your eyes, he winks at you and put both his hands into your palm."
    s "Something you're going to like, ok?"
    e "O-ok."
    "As soon as he releases his hand, he begins to walk back towards the village, leaving you alone here in the green forest."
    hide sebas
    with dissolve
    e "ok..."
    "You nudges your palms for a bit, seeing a few strips of orange fur are left on your hand, it makes you feel strangely tickled."
    "You quickly snap back to reality, what a strange conversation he left behind. You still need to bring 3 stones to him."
    jump main_green_forest

label Sebas_Ask_Lusterfield_People:
    e "So... Can you tell me more about Lusterfield?"
    s "Look, [e]. I'm not an expert on the village history, but I can assure you that this is just your good old tutorial spawn."
    e "...what?"
    s "...You're supposed to laugh at the clever fourth wall breaking joke. [e]."
    s "Anyways, you are safe here. No one would bother coming here and steal your wallet or something."
    e "But what about the village...? Or do you know any people that I can talk to?"
    show sebas grin
    with dissolve
    s "Well obviously me and Ole."
    s "You can visit Rahim's shop if you insist, I'm pretty sure he will be glad to talk to you, as long as you don't break any of his rules."
    s "Ahh... also Lothar's just wandering outside our shop on daytime. You should get along with that motherfucker and get him out of there."
    e "Who is he...? Did something happen between you two?"
    s "Nothing, He just kicked me somewhere down there last week."
    "Sebas points at his crotch in annoyance. You can clearly feel he is not happy about it."
    s "My nuts hurt like hell. Why would he do that. Why did he think he can do that just because I accidentally took away his arrows. That guy is fucking insane I tell you."
    e "Alright... that's cool-"
    s "If you see him later, tell him Sebas' got the hardest fist in the whole Lusterfield and he should watch out for his own nuts."
    s "...Also You can visit the Nocturnal Trunk, uhhh... the inn around Rahim's place. You can take some jobs from Cane..."
    e "What kind of job does he offer?"
    s "Nothing special to be honest, fetching him some materials would be enough for a few golds."
    s "He seems kinda shady but I think you two will get along pretty nicely!"
    s "That sounds wrong... but you know what I mean."
    e "Oh... I'll keep that in mind. Thanks Sebas."
    s "No problem, my [e]."
    jump Sebas_Ask_Lusterfield

label Sebas_Lothar_Adventure:
    scene kings_pawn
    show sebas normal

    e "Sebas, are we going to the river today?"
    menu:
        s "Well it all depends on you buddy, are you ready?"
        "Yes{#seblotgoesadventure}":
            e "Yeah! I'm ready!"
            s "Sure... Then, Let's go."
        "No{#seblotgoesadventure}":
            e "No... I think I forgot about something else..."
            s "Take your precious time, mister [e]."
            jump Sebas_Normal_Talk
    $ saved_hp = pc.hp
    $ saved_mp = pc.mp
    $ saved_lust = pc.lust
    e "Oh.. Seb, where's Ole."
    s "I told him to take care of the shop. You know, I'm not going to let customers leave the shop disappointed."
    show sebas normal at r1 with move
    show ole normal at l1 with dissolve
    show ole grin
    o "Or so you've heard. Kiddo, take care of Seb right here okay. I don't want him to lose an eyeball out there in the forest."
    o "And Seb, I packed you some lunch, right in your bag over there. Don't leave it too cold though."
    s "Can we not talk about this in front of [e]."
    e "Hey, Ole. I was asking if you'd come as well."
    o "I trust you have more than enough abilities to protect this little fuzzy lion. You three will be fine."
    show sebas grin
    s "Haha I'm oweing good old Ole a huge favour. So, here I am. Going out with my favourite roommate."
    o "Well, stay safe out there. And Seb, don't forget to get me the herbs."
    s "It's time to go, take care of the shop for me alright!"
    e "Goodbye, Ole!"
    hide ole normal at l1 with dissolve
    scene lusterfield01 with dissolve
    show sebas normal at r1

    if sebas_kick == True:
        s "I think Lothar is- Yeah, he's right there."
        show lothar stare at l1 with dissolve
        l "...Lion you moron. The lizard prescribed me with the ointment down there and it still hurts like hell to just walk."
        show sebas grin
        l "Not to mention you kicked me in the dick, not balls."
        e "Lothar, are you feeling alright?"
        s "He's good, I might as well give him another kick to revert the damage."
        show lothar bored
        l "...Disciple, don't think I'll forget about what you did yesterday."
        e "...Ok."
        s "Just a taste of his own medicine. Plus, I didn't think he'll come with us today."
        l "I have to lead you to where I found the stone, don't I? You two will just get lost and die without the hero's interference."
        e "Hey... Stop arguing you two, let's just go there and find out what's wrong with the rock."


    if sebas_kick == False:
        s "I think Lothar is- Yeah, he's right there."
        show lothar chuckle at l1 with dissolve
        l "Here I am, the hero of Lusterfield. The Myth, The Lege-"
        s "Yeah, it's him, we should get going now."
        show sebas bored
        e "Uhh- how are you doing Lothar?"
        l "Disciple, I suppose you remember what happened yesterday with the lion."
        l "I came in there with a transaction opportunity, and he threatened me with a, kick in the nuts."
        s "Uh Huh. Tread carefully, Lothar. You won't know when the payback will come, maybe not yesterday, but most certainly today if you keep talking."
        e "Hey... Stop arguing you two, let's just go there and find out what's wrong with the rock."
    scene forest with dissolve
    show sebas normal at r1 with dissolve
    show lothar normal at l1 with dissolve
    "The three of you continue on the adventure. Sebas and Lothar don't seem to get along too well, only occassionally asking about your experience in the village."
    "You feel a little awkward walking between the two dudes, their arguing slowly turns into quietness."
    "But after a few minutes of silence, you decide to break the stalemate..."
    menu:
        "Who should you talk to...?"
        "Talk with Lothar":
            $ sebas_asked = False
            e "Hey, Lothar. Where exactly did you find the stone?"
            show lothar chuckle
            l "Hmm, on the riverside, usually there are spears around there, I just walked past it."
            e "Did you see any other people around there?"
            l "Of course no. I was just strolling around, slaying slimes and bunch of stuff."
            l "But now that you said it, after you arrived, there has been so much more sighting of buggbears."
            e "Buggbears?"
            s "Oh yeah, those big ones that took over the goat's outpost a while ago."
            l "They're extremely vicious when they go about their business. I'd suggest you not to approach them without me nearby."
            e "Hmm, I'll be sure to take a look around more, with you."
            s "Buddy, did you just forget I'm still by your side?"
        "Talk with Sebas":
            $ sebas_asked = True
            e "Hey, Seb. What's with your fascination of stones?"
            show sebas grin
            s "My stones? No, they just sells good prices to the merchants around the continents. I'm just making sure I do my part in the classification."
            s "And possibly earn some good money from those stones. Some of them got me over a thousand gold, that's insane."
            l "Yeah, I thought mine looks pretty much like your expensive ones."
            s "It certainly does, but they're made of the same material, this one, its stripes are glowing all the time."
            if goat.win + goat.lose > 0:
                e "Doesn't it looks like, the pattern from the members of goat tribe?"
                s "We need much more information than that to confirm if it's from them."
            e "Seb, you seem... weirdly serious when you get into making out this weird stone."
            s "Do I?"
            s "Well, I can get into making out with you instead."
            show lothar stare
            l "Lion, stop flirting with my disciple, you buffoon."
    "Sebas and Lothar continues arguing for a while."
    scene mossy_freshwater with dissolve
    show sebas normal at r1 with dissolve
    show lothar normal at l1 with dissolve
    e "Ahhhh- I think we're getting close to the river."
    "You three arrive very quickly. There's a lot of small cavern around the hills nearby."
    s "How about splitting right here? I'll collect the water sample and Lothar you should find if there's any other similar rocks."
    l "I accept your arrangement, lion."
    s "Then [e], how about you guarding for us and make sure no dangerous animal comes by?"
    e "Yes, boss."
    s "Haha, do I look like a boss to you now all of a sudden. Now get going, we'll be back soon."
    hide sebas
    hide lothar
    "The three of you split in the mossy river. You stay in place and look around the scenery, everything is covered in green. The air is surprisingly fresh."
    "Sebas and Lothar walks in opposite direction, you glance at their back before they disappear from your field of vision."
    "You sit there, wait for Sebas and Lothar to return."
    "To pass the time, you begin to daydream about being in the room with Sebas, or Lothar."
    "They seem to have an unexplainable interest in you, somehow. Maybe you're just reading too much into it."
    "..."
    "Suddenly, you see a shadow in the reflection of the freshwater. You turn around, but there's nothing at all."
    "You are afraid it's something dangerous, but it would be risky if you don't chase and find out what's happening."
    menu:
        e "Should I... investigate further, or stay until Sebas and Lothar are back?"
        "Search around":
            "You climb up the hill and try to locate the shadow that you spotted."
            "But as soon as you get up, the shadow is already gone, leaving only a few footprints that leads to the somewhere else."
            menu:
                e "Should I... follow the footprint?"
                "Follow the footprint":
                    $ golem_stay = 2
                    "You decide to follow it, you examine the trail carefully and walk along the hills."
                    "After some time, you have already reached the end of the trail, but there's no one to be seen."
                    "You scratch your head, dissappointed to have wasted your time tracking some weird footstep."
                    e "I should really go back... Sebas and Lothar might have already come back."
                    "As you turn back, you see the same shadow looming over you."
                    "The figure is mostly green, its moss tries to wrap around you but you escape in time."
                    jump mossgolem_battle
                "Climb back down":
                    $ golem_stay = 3
                    "There is no point following something that has already left the river. You climb back down the hill and wait for Sebas and Lothar to come back."
        "Remain in place":
            $ golem_stay = 1
            "You convince yourself that it must just be the wind, so you wait for Sebas and Lothar to come back."
            "..."
    "You relax yourself at the riverside, but another shadow emerges in the water again."
    "You immediately look back, but it's already too late. A huge green monster punches you in the head."
    "SMACK!!"
    "Your HP drops by 20."
    $ pc.hp -= 20
    jump mossgolem_battle



label Sebas_Lothar_Adventure_End:
    if golem_lothar == True:
        e "Thanks for the help, Lothar. But I think I can handle myself."
        show lothar chuckle at l1 with dissolve
        l "You think? Well, think again. If not for me you'd be beaten to a pulp in a few seconds."
        e "Alright. You're right, Lothar. Thank you for saving my life."
        show lothar normal

        l "Good Disciple."
        e "So... what's the creature?"
    if golem_lothar == False:
        e "Oh... my... What was this creature...?"
        l "What happened."
        e "Holy- You scared me Lothar."
        show lothar normal at l1 with dissolve
        "Lothar appears behind where the golem stands, looking at the fallen golem."
        l "Seems like I was too late to the party."
        e "The Golem, it attacked me. What's this creature?"
    l "I don't know... I haven't seen a golem before. Especially this one with moss on it."
    show lothar grin
    l "Now that I think of it... the stone I found. It might have been his hand."
    e "What? Why did you take his hand?"
    l "It was glowing in the dark. I just picked it up near the river. Something might have been going on without our knowledge."
    l "We best wait for the lion to come back, he must be watching the grass grow or something."
    "You and Lothar wait for a few minutes before Sebas comes back."
    show sebas shocked at r2
    show sebas shocked at r1 with move
    s "What the fuck is going on!"
    l "It's a Golem, calm your ass down, lion."
    s "I was collecting samples out there for just a few minutes and now you're telling me [e] killed a golem?"
    if golem_lothar == True:
        e "Hey, Lothar helped as well."
    else:
        e "Hey, I didn't know there're monsters here."
    s "I'm sorry, buddy. I shouldn't have left you alone here."
    show sebas normal
    l "My disciple can take care of himself. After all, he learnt all his fighting tricks from me."
    s "Hey, look. Your stone is his left hand."
    l "Yeah we discovered this like ten minutes ago."
    e "So, what's wrong with the golem?"
    s "It is conjured by someone, very intelligent I suppose. But why the mossy stone?"
    l "A rolling stone gathers no moss."
    s "Ok, you are being too obvious with this line. Holy Fuck."
    e "Hmm... so what's your findings?"
    s "Let me get the rock sample..."
    "As Sebas touches the golem, it immediately crumbles into dust and particles, even the moss is gone now..."
    show lothar grin
    show sebas shocked
    l "Good job, lion."
    show sebas bored
    s "..."
    s "I can gather some more details by myself later here. But we should go back now, we don't know if there's any other golems here."
    l "Look, I will protect you two."
    show lothar normal
    show sebas normal
    s "Uhh- no thanks. Let's go buddy."
    "The three of you travel back to Lusterfield. Sebas and Lothar are arguing, as usual."
    "You are walking in between them, occasionally getting bumped by one of them's beefy shoulder."
    "Glancing at both of them, they seem to be oddly enjoying each other's company, despite all the taunting and dickering."
    pause 1
    scene kings_pawn with dissolve
    show sebas normal at r1 with dissolve
    show lothar normal at l1 with dissolve
    "Soon, you three are back to the shop."
    l "Lion, what do I get from the stone?"
    s "How about 800 gold. I'm already being too generous with the pricing."
    show lothar stare
    l "...900."
    s "850."
    l "You're pushing it lion."
    s "..."
    show sebas laugh
    s "700."
    show lothar bored
    l "Ok. Ok. 850 gold."
    "Sebas hands Lothar the gold while he takes the stone away, putting it in a precious box."
    e "Wait... this rock is worth 850 gold?"
    s "Yeah, buddy. It's no ordinary glowing stone. It contains a fragment of the golem's soul."
    show sebas grin
    s "I can fetch a great price selling it to those merchants, at least 1200 gold."
    e "Oh... that sounds really good. Can I buy it?"
    s "Yeah. Sure you can, but no discount this time."
    e "Hmm... I'll think about it."
    show lothar chuckle
    l "So, lion. We're done here?"
    s "Yeah, I will have to see you later. Lothar."
    l "Alright. Guess I should pick up another stone next time."
    "Lothar nods to you two and leaves the shop."
    hide lothar with dissolve
    show sebas normal at c1 with move
    s "Hey, buddy. I'm gonna polish my rock here. You're free to go now."
    e "Ummm... can I ask a question, Seb?"
    s "What's up, [e]."
    e "Can we hang out sometimes later, like this, I really enjoyed the time we had."
    e "Minus the arguing with Lothar part of course."
    show sebas grin
    if sebas_kick or sebas_asked:
        $ sebas_sneak = True
        s "Hmm..."
        s "Maybe if you found another interesting place to go."
        e "R-really?"
        s "I mean. I'm really busy for most of the day. And I have already used my only day-off of the year to go out with you and Lothar."
        s "We can fool around. I had a great idea about what we're gonna do though."
        s "We'll talk later, alright? Stay safe, buddy. And don't get hit by another rock."
        e "Oh. O-ok, see you then, Seb."
    else:
        s "Hmm... Sorry buddy. I'm just too busy in the shop. And I used my only day-off of the year to go out with you and Lothar."
        e "O-oh... Ok."
        s "I really don't have much spare time, I guess."
        e "It's alright, Seb."
        s "Yeah? Promise me you won't get angry because of me?"
        e "Yes... I don't mind."
        s "Haha then we'll talk later, alright? Stay safe, buddy. Don't get hit by another rock."
        e "O-ok, see you then, Seb."
    $ QuestFinish(quest05)
    "Sebas gives you a nod while continue looking at his newly-acquired rock."
    hide sebas normal with dissolve
    "He doesn't seem to concerned of you... compared to your first meeting. You feel a little uneasy, as if you did something wrong."
    "But at the end, you decide it's better for you to continue with your adventure."
    $ addItem("Mossy Artifact", sebasInventory, 1)
    $ mossy_artifact_inshop = True
    $ timenow.hour += 4
    jump main_kingspawn

label Sebas_Ask_Lusterfield_Lothar:
    e "Hey, I saw you were here when Lothar and I were... uhh.. talking outside."
    s "Oh... Haha. You two were having some kind of heated fighter moments didn't you."
    e "What?"
    s "Yeah. Alright. I was there. Lothar is a weird dude, don't get me wrong, he is just not right in the head."
    e "Is he always like this?"
    s "I don't know, I didn't talk to him before he become some sort of hero of the village. People were grateful for his act. But he always takes it too far."
    show sebas bored
    with dissolve
    s "Since then he became more and more arrogant. I should've warned you more about him, [e]... and my balls... they're still sore from his fucking high kick."
    s "Needless to say, that guy has a really flexible legs."
    e "You ok there...?"
    s "I might need a reliev... I- uh... nevermind. haha- what? Yes, they are still functional."
    e "Seb, what the hell are you talking about."
    s "Look, I'm just telling you, that Lothar guy is a huge bully. I just don't want him to give you any troubles."
    e "Ok... thanks, Sebas."
    jump Sebas_Ask_Lusterfield

label Sebas_Ask_Himself:
    e "Soo... what about you?"
    s "What about me?"
    e "Yeah, what are you up to?"
    s "Me? I don't know, just bored from all the cashier stuff."
    s "Ole is cleaning the shelves like usual, nothing is happening right now."
    s "I'd say it's a normal day for a normal lion like me."
    e "That sounds cozy."
    jump Sebas_Normal_Talk

label Sebas_Ask_Kingspawn:
    e "Hey Seb, how's it in the shop?"
    s "Ha. You're a curious dragon, aren't you."
    s "Well I manage the shop from 7am to 11pm every day. With the help of Ole, of course. He helps me restock most of the products here, every Monday and Thursday."
    s "People pawns expensive stuff in this house. I had some clients that gave me like a thousand gold worth of pledges."
    e "But how do pawn shops work?"
    s "I offer loans based on the value of their collaterals, the item I mean. And they can redeem it back sometimes later for the value of the loan plus a percentage of interest."
    s "But after a certain period of time if they don't come back with the money, I'll just put it on the display and sell their collaterals."
    s "That's where the word \"shop\" comes, we also do normal shop thing. People can buy and sell whatever they want."
    e "Oh... So if I sell you a necklace that worth 100 gold. I have to buy it back later for something like 105 gold?"
    show sebas grin
    with dissolve
    s "Technically, it starts from 140 gold. But I always give my roomies a huge discount. So don't worry about it, hehe."
    e "Wait really? Thanks Seb. What's the discount?"
    s "The interest is 50 percent off for you! That's almost half. And don't worry, I won't sell your important items."
    e "Awww... Sweet!"
    s "No problem, [e]. It's nice seeing my buddy smile."
    jump Sebas_Normal_Talk

label Sebas_Ask_Transport_Task:
    e "Hey, Seb. You seem to need some help...?"
    "You see Sebas glances at his rocks, and then glances back at you."
    s "Hah, roomie."
    e "Seb...?"
    s "You can help with the crates. If you so wish."
    e "Uhmm... How can I help again...?"
    s "You know, we used to trade with the goats, a lot."
    s "Hasn't been the case for a long time, heh..."
    s "Anyways, usually Big Ol' Ole here should deal with inventory..."
    s "I uh... [e]?"
    e "Seb... What's wrong with you?"
    s "N-nothing out of the ordinary! I'm serious."
    s "Wanna help a lion out?"
    "Sebas scratches the back of his head. Needless to say, you are surprised at his attitude, he seems... a little more fidgety and nervous."
    e "S-sure."
    s "Well what did I say, who needs a wagon when your pocket's got more space than the wagon itself."
    s "So, take my crates, give them to Furkan."
    s "It's sealed magically by magic."
    e "W-wait, you are resuming your trade route with the goats?"
    s "It's about time I get my hand back on those little minerals and fur."
    e "What about Rahim, he doesn't seem welcoming to the goats...?"
    s "Don't worry roomie, I can convince him pretty easily with my illustrious charm."
    e "...Is he that easily charmed."
    s "Yes of course, last time he gave me a 50 percent off offer, just after 2 hours of seeing my huge charm."
    e "2 hours!?"
    s "Yep... He's pretty charmed. Even though he kind of wanted me gone after the trade. I suppose it wore off."
    "You stare at the lion, and he's just laughing on his own, somehow reverting back to the old Seb you know."
    "Seeing the smile plastered on his cheeks, you sigh a breath of relief."
    e "A-alright."
    s "Anyway, crates! Furkan has a deal with us, so...."
    s "Take the crates to... his general? And they'll give you another crate to carry back to us."
    s "Just telling you, that general really doesn't like jokes."
    s "Like Rahim, but boring."
    e "Mhm..."
    menu:
        s "So... take the job? I'll give you a special stone... in return."
        "Accept the task":
            e "A-alright, give me the crates."
            s "Sure thing, here."
            "Sebas points at the wooden crates, he picks it up and casually drops it on your arms."
            s "Don't lose them! It's worth mor-... uh... worth less than you... but still. Be careful."
            e "I will!"
        "Maybe Later":
            e "M-maybe later?"
            s "Heh, sure thing."



label Sebas_Dialogue_End:
    e "That's all for now, Seb."
    s "Hehe, take care buddy."
    hide sebas
    if sebas_location == "kingspawn":
        jump main_kingspawn
    if sebas_location == "nocturnaltrunk":
        jump main_nocturnaltrunk2


label Ole_dialogue:
    call Lusterfolk_Affection from _call_Lusterfolk_Affection_1
    hide screen menu_buttons
    scene black
    if isNight():
        if ole_location == "kingspawn":
            scene kings_pawn_night
        if ole_location == "nocturnaltrunk":
            scene nocturnaltrunk_night
    else:
        scene kings_pawn
    with fade
    show ole normal
    if ole_location == "nocturnaltrunk":
        $ ole_night += 1
        if ole_night == 0:
            o "Hey, [e]. Finally got to see you in the tavern."
            e "Oh, Ole! I didn't really expect you to hang out here."
            o "Well... Seb asked me so much time to come with him... I have got to take care of this dumb lion."
            if sebas_drunk_day == timenow.day:
                o "And he's not even conscious now... I would have to drag him back to the shop..."
            e "You- feeling okay with Cane?"
            if ole_trust_cane:
                o "I'll have to see for my eyes, but if you vouched for him, he wouldn't be that bad, I presume."
                o "I didn't really know why I... disliked him, but Rahim really hated him for a while."
                e "You should do what you want to do... Ole."
                o "Sure, Sure. If Rahim changed now... Maybe I should too."
                e "Alright, it's good to see you here."
                o "Same goes for me."
            else:
                o "Hmm... I'm just avoiding him for now."
                e "Oh..."
                o "I will always side with Rahim on this matter. I trust his judgement."
                o "But it's still better to see for my eyes."
                e "Ole, you seem to rely on Rahim a lot."
                o "A little, he knows a lot more stuff than I do, and he saved my life when I was still young."
                e "Aren't you... relatively young?"
                o "Ahem, the older the wiser you are."
            o "Anyways, I've heard about you in the tavern, haha."
            o "You sound like a real server now don't you, kiddo."
            e "I-uh... do I sound really bad...?"
            o "Heh... I like you this way."
            jump Ole_Normal_Talk
        else:
            if renpy.random.random() > 0.6:
                o "Hey, kiddo. Care to join for a quick while?"
                e "Oh Ole! Nice to see you here in the tavern."
                jump Ole_Normal_Talk
            if renpy.random.random() < 0.3:
                o "Hey kiddo."
                e "Ole, are you having enough bread here in the tavern?"
                o "Just enough for me to fill my belly. Cane should really consider opening a bakery as a side business."
            if renpy.random.random() < 0.3 and sebas_location == "nocturnaltrunk":
                o "Kiddo. Good to see you here."
                e "Ole! Is Seb still drunk?"
                o "He's always been drunk the second he gets into Cane's place. You'll get used to his gibberish."
                s "Eh- Ol-ol-ole who are you t-shtalking to..."
                "You hear a loud burp between you and the lizard."
    elif ole_location == "kingspawn":
        if renpy.random.random() > 0.5 and isNaked():
            o "Hey, kiddo... Did you forget to put on your clothes."
            e "Yes..."
            o "You can put them on anytime... now, I mean anytime..."
        elif sebas_location == "nocturnaltrunk" and isNight():
            o "Hey kiddo, Seb's gone to drink again."
            e "Ah! He's at the nocturnal trunk?"
            o "Yeah, in case you're looking for him."
        elif renpy.random.random() > 0.7:
            o "Kiddo, what are you doing here?"
            e "Just snooping around, I suppose you don't mind my company?"
            o "Heh, watch out your back then, I'm still dusting the shop here."
        elif renpy.random.random() > 0.75 and quest15.status:
            o "Hey, kiddo."
            e "Hello, Ole. Feeling great lately?"
            o "Good, at least I won't be sick for the forseeable future."
        elif renpy.random.random() > 0.7 and quest32.status:
            o "Hey kiddo. Having fun out there?"
            e "Yes, but never fun without having you, and Seb."
            o "Wanna go for a round two of that night we had in the tavern? I did hone my throwing skill there ever since."
            e "Of course!"
        else:

            if ole_tut == 1:
                o "Hey kid, how's your head doing?"
                e "It's healing really quick, Ole. Thanks to you and Sebas."
                o "Good. Do you like the bed? We got the whole bed from a customer long ago, a bad investment at the time, but I'm glad it came in handy for you."
                e "I slept pretty well yesterday. It's definitely something I haven't slept on before."
                o "Heh, good to know."
                $ ole_tut += 1
            else:
                o "Hey, kiddo."
                e "Hello, Ole!"
        jump Ole_Normal_Talk

label Ole_Normal_Talk:
    menu:
        o "You doing well today, kid?"
        "Ask about Pirkka's Prose" if quest35.status == 3:
            jump Ole_Prose_Ask
        "Learn his opinion on the vote" if quest37.status == 2 and quest37.start_date + rahim_vote_duration  >= timenow.day and quest39.status == False:
            jump Ole_Voting_Opinion
        "Ask about his opinion on the vote" if quest37.status == True and timenow.day < quest37.completed_date + 14:
            jump Sebas_Voting_Result
        "Report about Gwyddyon's secret with the supplier" if quest39.status == 3:
            jump Ole_Voting_After_Gwyddyon
        "Get ready to meet with Pirkka" if quest39.status == 4 and ole_votequestpirkka:
            jump Ole_Voting_Asking_Pirkka
        "Continue with the Harp's materials" if quest39.status == 4 and not ole_votequestpirkka:
            jump Ole_Voting_Finding_Number
        "Ask to check the Harp" if (quest39.status == 6 or quest39.status == 8) and LookForItem("Harp", inventory):
            jump Ole_Voting_Testing_Harp
        "Pick up the Delivery" if is_client("Ole"):
            $ client_name = "Ole"
            call Courier_Pickup_Dialogues from _call_Courier_Pickup_Dialogues_5
        "Deliver the goods" if is_recipient("Ole"):
            $ recipient_name = "Ole"
            call Courier_Delivery_Dialogues from _call_Courier_Delivery_Dialogues_5
        "Start with the Recipe" if quest39.status == 5:
            jump Ole_Voting_Starting_Recipe
        "Start with the Recipe" if quest39.status == 7 and LookForItemNumber("Crystal String", inventory) >= 10 and LookForItemNumber("Elderwood", inventory) >= 12:
            jump Ole_Voting_Report_Pirkka
        "Ask about the meeting with Gwyddyon" if quest37.start_date + rahim_vote_duration < timenow.day and quest39.status != False and ole_after_meeting == False:
            jump Ole_Voting_After_Meeting
        "Ask about Postal Training" if quest01.status == False:
            jump Ole_Postal_Training
        "Finish with Postal Training" if quest01.status == 2:
            jump Ole_Postal_Finish
        "Ask for his potion request" if quest08.status == True and taskAvailable(task01, quest08):
            jump Ole_Potion_Task_Start
        "Report for Potions" if task01.status != True and task01.status != False and LookForItemNumber("Strength Potion", inventory) >= 5:
            jump Ole_Potion_Task_Finish
        "Ask about ingredient for Cane's Apron" if quest07.status == 3 and not (LookForItem("Green Dye", inventory) or LookForItem("Green Dye", sebasInventory)):
            jump Ole_Apron_Quest
        "Report about Amble and Jog's Training" if quest17.status == 8:
            jump Ole_Report_Courier_Quest
        "Ask if he sees you under the counter" if sebas_suck > 0 and ole_asked_sebas_suck == 0:
            jump Ole_Ask_Under_Counter
        "Ask about Further training and lessons" if timenow.day > 20 and quest17.status == False and quest01.status == True:
            jump Ole_Ask_Courier_Quest
        "Ask about his habit of cleaning" if quest08.status == True and quest08.completed_date + 1 < timenow.day and quest15.status == False:
            jump Ole_Ask_Cleaning
        "Ask for his opinion on Goat Tribe" if quest06.status == True  and quest06.completed_date + 1 < timenow.day  and opinions_GoatTribe[1] == 0:
            jump Ole_Ask_Goat_Tribe
        "Ask about his sickness" if quest15.status == 4:
            jump Ole_After_Sick_Quest
        "Ask about his Ointment" if timenow.day > 12 and quest08.status == False:
            jump Ole_Ask_Ointment_Quest
        "Finish with his Strength Potion Request" if quest08.status == 4:
            jump Ole_Ointment_Finish
        "Ask about the Shop":
            jump Ole_Ask_Kingspawn
        "Ask about Lusterfield{#OleAAL}":
            jump Ole_Ask_Lusterfield
        "Ask how he is doing":
            jump Ole_Ask_Himself
        "That's all for now":
            jump Ole_Dialogue_End
    jump Ole_Normal_Talk

label Ole_Ask_Lusterfield:
    menu:
        o "What do you want to learn about the village?"
        "Ask about the people in Lusterfield":
            jump Ole_Ask_Lusterfield_People
        "Ask about Lothar" if seen_lothar:
            jump Ole_Ask_Lusterfield_Lothar
        "That's all I needed":
            jump Ole_Normal_Talk

label Ole_Potion_Task_Start:
    if task01.completedtimes == 0:
        o "Alright [e] ,I've got another Courier job for you."
        e "What is it this time, Ole?"
        o "I need you to go get 5 strength potions from Haskell."
        o "Normally I send Seb out to do this."
        o "But the last few times I did, this cheeky lion stayed for tea and came back empty-handed..."
        show ole understand at r1 with move
        pause 0.5
        show sebas normal at l1 with dissolve
        s "Hey! That's not fair! I at least got them last time!"
        o "Don't listen to him, that was only because I sent him back out there."
        o "..."
        menu:
            o "So... Wanna help us out?"
            "Take the task":
                e "Okay, sounds good; I'll go get the potions as soon as possible."
                if Haskell_Promise:
                    $ task01.description = _("Ole wants me to take up the potion order and get 5 strength potions from Haskell, but I promised Haskell to make them myself...")
                    $ task01.tProgress(__("Craft 5 Strength Potions"), "Strength Potion", 5)
                else:
                    $ task01.description = _("Ole wants me to take up the potion order and get 5 strength potions from Haskell, I should go to his hut and ask him to make some.")
                    $ task01.tProgress(__("Ask Haskell to make 5 Strength Potions"), "Strength Potion", 5)
                $ task01.reward = _("50 Gold")

                $ TaskBegin(task01)
            "Maybe Later":
                e "Maybe later...?"
                o "Well... we're counting on you."
                jump main_kingspawn
        s "I could totally go out and do that right now, watch me!"
        o "I actually want to get the potions this time."
        o "Also, did you already forget you have to watch the shop?"
        "The customers browsing through the wares are doing their best to act like they're not hearing this."
        show sebas bored
        s "No!"
        s "...okay, maybe I did, but if it weren't for that, I'd go out and show you that I could get those potions!"
        e "I'm just going to go do the delivery now."
        "It doesn't seem like Ole or Sebas heard you, as they are a bit busy bickering with each other."
        o "Sure, and Lothar would let you kick him in the nuts if I asked him nicely."
        s "It wouldn't hurt to try."
        o "Oh come on, you can't be trying to tell-"
        "You have stopped listening."
        jump main_lusterfield01
    elif task01.completedtimes == 1:
        o "Hey, [e]. We're running short on potions again."
        e "I take it that means you want me to go on a delivery?"
        o "I'd much rather you do it over Seb."
        s "I know we talked about this, but you don't have to be so mean about it."
        o "Sorry, but it's true. Say what you will, but [e] always gets the job done right."
        s "And looks cute doing it!"
        "Ole snorts."
        o "I won't disagree with you, but maybe get your eyes back to focusing on your job rather than our courier friend's butt."
        e "So, umm, just the same task as last time?"
        o "Just so."
        o "I'll give you the same reward as last time."
        e "Thank you Ole. I'll get it done as soon as I can!"
        o "No worries, and don't rush yourself too much."
        o "It's not urgent."
        e "Got it! Thank you."
        $ TaskBegin(task01)
    else:
        o "Hey, [e]! You ready for another round of potion deliveries?"
        e "Yeah! I've gotten quite used to these by now."
        o "I'm glad to hear it, because we're never going to have enough potions."
        e "Okay, maybe not that used to this."
        e "I don't mind this every once in a while, but I'd rather not do this every day."
        o "Too late! You can't take it back!"
        e "Okay... I can't really say no after everything you've done for me."
        o "I'm kidding [e]."
        o "Well, I'm kidding about you needing to do this constantly."
        o "I do still want those potions, if you're willing."
        e "Yeah, I don't mind!"
        e "I like helping."
        o "I imagine the gold doesn't hurt either."
        e "Yeah, the gold helps."
        e "Anyways, I'll catch you later with a new batch of potions, Ole!"
        o "Alright, see you [e]!"

        $ TaskBegin(task01)
    jump main_lusterfield01

label Ole_Potion_Task_Finish:
    $ removeItem("Strength Potion", inventory, 10)
    if task01.start_date == timenow.day or (task01.start_date == timenow.day - 1 and task01.start_hour > timenow.hour + 12):
        "Seb and Ole are still bickering, as you haven't even left the store to try and fake that the potions come from Haskell."
        e "Here are the potions, Ole!"
        o "You didn't even leave, how are you going to tell me you already got the potions from him."
        e "Oh, umm... I, uhh."
        e "He gave me some last time I visited, just in case you asked!"
        o "That doesn't sound like him at all, but I don't see how else you could have gotten them."
        o "Here's your reward."
        "You received 50 gold"
        $ pc.gold += 50
        o "And tell Haskell thank you for being so thoughtful."
        "You're pretty sure that might kill him from guilt."
        e "Sure! Though I think he already knows."
        e "You know how well he knows you, hehe!"
        o "Oooookay."
        o "You sure everything is okay with Haskell?"
        e "Mhmm! Everything is just fine!"
        "Everything is fine with him, but absolutely not with you"
        e "I've got to get going now. I've got important courier business."
        o "No you don't. I know all of the jobs you've taken in the village."
        e "Hehe, yeah! Just umm, gotta make sure I'm properly trained."
        e "Just ask Lothar! He'll tell you how hard I've been training these days."
        o "I don't think I will, but thank you."
        "You quickly walk away, ending the conversation before you fit even more of your foot in your mouth."
    else:
        if task01.completedtimes == 0:
            o "Hey, [e], I see you got the potions!"
            e "Yeah, it was an easy enough job."
            e "Didn't even have to deal with any buggbears this time."
            o "I'm glad to hear it."
            o "Tell Haskell I'm thankful as always for the potions."
            e "You got it!"
            "You are absolutely not going to do this"
            e "Anything else you need?"
            o "Nothing comes to mind."
            o "Aside from that though, everything okay on your end?"
            o "Any bumps or bruises you've gotten from venturing out there?"
            e "Nothing I can't sleep off, thank you Ole."
            o "Anytime. Please remember I'm happy to help anytime you get sick or anything."
            o "Just umm."
            o "Don't get me sick as well if that happens, please."
            e "I'll do my best?"
            e "I'm going to head out now."
            o "You do that. I'm going to get to putting these potions where they belong."
            o "Before that though, here, have this as thanks for a job well done."
            "You received 50 gold."
            $ pc.gold += 50
        else:
            e "I got the potions for you Ole!"
            o "Thank you, [e]."
            o "Can you put them over on that table for now?"
            e "Sure, give me a sec."
            "You turn around and put the potions on a little table Ole indicated."
            "It is clearly a temporary spot so that Ole can handle these later."
            "As you turn back around, you see Ole very close to your face."
            o "Thank you for continuing to help us like this, [e]."
            o "Please, take this."
            "You received 50 gold."
            $ pc.gold += 50
            e "Thank you, Ole."
            o "It's the least I can do."
    $ TaskFinish(task01)
    jump main_kingspawn


label Ole_Report_Courier_Quest:
    e "H-hey...I'm back. From Amble and Jog."
    o "Hey, [e]. What's going on, why did you look so tired?"
    e "...because...training?"
    o "Fair enough. So, nothing else?"
    e "I've gotten a few new skills and tricks I can use. They're really useful!"
    o "Ha. That's good to know. Remember you can check out your skills in the journal."
    o "Anything else?"
    e "W-what? What else...?"
    o "Hmmm... Sure then."
    o "Hope it proves useful for your future adventures."
    e "It definitely will!"
    e "Thank you, Ole, for helping with the trainings."
    o "Thank them, not me, kiddo. But I see you're appreciative enough."
    e "Hmm?"
    o "mhmm... take a bath!"
    e "O-ok! Didn't know you can smell that..."
    $ QuestFinish(quest17)
    jump main_kingspawn

label Ole_Ask_Courier_Quest:
    e "Ole, it has been quite some time since my first courier mission. Do you have a new mission?"
    o "Speaking of, you've been a great help with Haskell and the potions."
    show ole understand with dissolve
    o "Glad to see that you're in such a spirit too."
    o "But there aren't any new courier jobs for the taking at the moment."
    o "With the goat tribe and the roads still filled with danger, there hasn't been much need for courier work."
    o "We wouldn't want you to repeat the last courier's fate."
    "Ole's face dims."
    e "It's fine then. I was just asking. I can wait."
    e "I'm sure there are other odd jobs I can do in the meantime."
    "As you turn to leave, Ole stops you."
    show ole normal with dissolve
    o "Actually, wait. Eventually, you'll have to venture far away from Lusterfield to complete your courier job."
    o "The world at large is not exactly safe."
    e "Don't worry, Ole. I can take care of myself."
    o "That's good to know. But it's better to be safe than sorry."
    e "What do you mean, Ole?"
    o "You know that Jog and Amble are just like you too, right? Or at least, they patrol the roads to keep it safe for couriers like you."
    "You nod."
    o "While we wait for more courier jobs to open up, why don't you get them to teach you some new skills?"
    o "As your seniors, I'm sure they have much knowledge to impart."
    o "At least, I'm sure Amble will be able to help. Jog..."
    "Ole frowns at the name."
    o "Why don't you ask Amble first?"
    e "Hmm... alright."
    $ QuestBegin(quest17)
    $ quest17.qProgress(__("Ask Amble and Jog for training"))
    jump main_kingspawn

label Ole_Party_Begin:
    scene kings_pawn
    "As you walk out of your room, you can hear Seb and Ole whispering at the corner of the shop."
    show ole understand at r1
    with dissolve
    o "That'll be fun..."
    show sebas laugh at l1
    with dissolve
    s "He's going to be so shocked..."
    "You walk over to them."
    e "What are you guys talking about?"
    show sebas shocked
    with dissolve
    "Seb jumps as he whips around to look at you. Ole is much more collected."
    s "I-it's nothing!"
    e "Really?"
    show ole normal
    o "Yes. We're just talking about the shop's business."
    show sebas grin
    with dissolve
    s "Yes, yes!"
    "Seb nods vehemently."
    "You still find this suspicious."
    s "Anyway, Roomie, good fucking morning!"
    e "Good morning to you too."
    "Then, this is this awkward silence."
    "You have a feeling these two are hiding something but you don't know what."
    show sebas normal
    "Seb fidgets and eventually cracks."
    s "Alright, fine. We're talking about your..."
    show ole stare
    o "Training!"
    s "Yes, training!"
    e "Training? What kind of training?"
    "Seb turns to Ole with pleading in his eyes."
    o "Your courier training."
    show sebas smug
    s "Yes, yes."
    e "I thought I've finished my courier training."
    show sebas laugh
    s "The training is never done. So, we need you to... erm..."
    "Seb ponders as a crease appears between his brows."
    show ole smile
    with dissolve
    o "Forage some stones from the woods."
    s "Yes!"
    e "But haven't I already done that?"
    s "Yes, but this time, you'll have to find four stones!"
    e "Huh?"
    s "Yes, yes. It's good for your courier training. Now off you go."
    "Still confused, you are pushed out of the shop."
    $ QuestBegin(quest16)
    $ quest16.qProgress(__("Collect... Stones"))
    jump main_lusterfield01

label Ole_Party_Quest:
    scene kings_pawn
    e "Hello? Seb? Ole?"
    if timenow.day <= quest16.start_date or timenow.hour <= quest16.start_hour + 2:
        show sebas normal
        s "H-hey! M-My Best Roomie! Didn't I tell you to get the stones?"
        e "Hmm... I've got enough stones... or rocks."
        show sebas shocked
        s "Uh..."
        show sebas grin
        s "Then uhmm!!! Get more of them!"
        e "W-what?"
        e "How many should I get?"
        s "Uhh... it's gonna take some time. Just. Get Them As much as you can!"
        e "Hmmm... ok. But where is Ole?"
        s "No..."
        e "No?"
        s "He's busy with... uh... stuff. Now go and get those rocks!"
        e "Fine, I will find out what you two are planning."
        s "Hmm! Good Luck!!"
        jump main_lusterfield01
    "You look around and the shop is empty."
    "No one responds to your call either."
    "You look around and notice a note on the counter."
    "It is written in Seb's quirky handwriting."
    s "Roomie! Come meet us at Cane's tavern! We'll meet you there for ----"
    "Something was crossed out and Ole's flourishing handwriting corrected it to 'your training'."
    "This is befuddling. Honestly, you are intrigued too."
    e "...Hmmm what are they planning..."
    "You decide to leave the shop, and head to the tavern..."
    $ quest16.qComp(__("Head to the Tavern"))
    $ quest16.status = 3
    jump main_lusterfield01

label Ole_Ask_Ointment_Quest:
    $ quest08 = Quest(_("Mutual Apothecary Arrangement"), _("King's Pawn"), "Ole", _("As my courier job, Ole told me about helping him get potion from an old friend."))
    e "Hey! Ole. I'm ready for the first... courier job!"
    o "Alright kiddo. Looking good with your badge here."
    e "Oh yeah! It looks really good! I certainly love the shape I have here."
    o "Sure, I designed the badge with Rahim's advice. He's certainly a great mentor."
    o "But back to the job, I remembered you asked about the ointment... that I gave you when we met."
    e "Oh, yes. I was a little curious how you made it."
    o "Well, let's not get ahead of ourselves here, [e]. I'll teach you how to make it after your job."
    o "I need you to visit... a-a potion maker, if you will."
    e "Should I take... a memo?"
    o "I'll mark it... on your map. You pass the river after the giant tree, and then reach the outpost and you'll see a cabin."
    e "Uh... Ok. What's the job about?"
    o "Just ask him for 30 strength potions. He'll know what you're talking about."
    e "O-hh... But does the potion maker know me, if I went there?"
    o "Yeah, Sebas told him about your badge last time he went there."
    o "Alright, courier, don't disappoint me with your first job."
    e "O-ok. Yes, chief."
    "Ole chuckles at your gesture. He soon turns back to the cabinet and resume cleaning."
    $ QuestBegin(quest08)
    $ quest08.qProgress(__("Visit the Potion maker"))
    $ alchemists_cabin.discovered = True
    jump main_kingspawn

label Ole_Ask_Cleaning:
    e "Ole, I really haven't gotten to know what do you do specifically at the shop."
    o "I help Seb with the logistics side of things."
    o "Arranging new couriers, doing inventory, tallying up the accounts and so on."
    e "That is amazing."
    o "It is more like a necessity."
    o "If you leave those things to Seb, this shop would have gone under a long time ago."
    show ole normal at r1 with move
    show sebas grin at l1 with dissolve
    s "Hey, I heard that!"
    s "Just verifying that O is telling the truth!"
    o "See."
    "Ole shakes his head helplessly."
    o "Other than that I also help make some simple potions for the store to sell and clean up around here."
    e "Why don't you ask Seb to help you clean?"
    s "Roomie, you're making it sound like I don't pull my weight around here!"
    s "That's not true! Right, O?"
    show ole grin
    "Ole smiles indulgently."
    o "Yes. Seb does his part and I do mine."
    o "But let's just say cleaning is not his calling."
    s "Hey, I clean too.... That one time."
    o "What a catastrophe that was."
    e "What happened?"
    show ole normal
    o "I'll just say that I ended up doing more cleaning than I should've if I didn't ask for Seb's help."
    s "Hey! That wasn't my fault."
    s "Am I supposed to know that glassware are so fragile?"
    e "Isn't that common knowledge?"
    s "Roomy, whose side are you on? The glass or mine?"
    o "Alright. Stop pestering our friend."
    "Ole shoos Seb back to work before turning back to you."
    show sebas normal at r2 with move
    show ole normal at c1 with move
    o "Now you understand why I don't ask him for help when it comes to cleaning."
    o "It's something I picked up when I was an apprentice working for Haskell."
    o "You wouldn't know it but cleanliness plays a huge-role in potion making."
    o "If an ingredient is contaminated, the final product's effect might be affected."
    o "I've spent quite a long time cleaning vials and bottles before Haskell would allow me to brew my first potion."
    o "I've kept that habit every since."
    "You glance at the glass vials and bottles on the table and shelves. They are all sparkling clean."
    e "But, Haskell doesn't seem like someone who would mind cleanliness that much."
    e "Speaking of, I don't think I've seen him clean the big mug he often drinks out of...."
    show ole grin
    "Ole chuckles warmly."
    o "Sharp observation there."
    o "Haskell is already a master when I studied under him."
    o "His mastery of alchemy easily overrides the negative influence any grim or dirt can bring."
    o "Can't say Haskell's one to take his own advice. He just can't kick that slothful habit."
    o "So occasionally I'd go back to his hut to help with the clean up."
    e "That's very kind of you, Ole."
    show ole understand
    "Ole accepts the compliment."
    o "He has taught me everything I know about alchemy. Some cleaning is nothing."
    o "Plus, I like to clean. A clean mind is a healthy mind."
    o "That's why you'll normally see me cleaning up around here."
    e "Thanks for the chat, Ole. I feel like I know you better now."
    show ole normal
    o "It was fun talking to you."
    s "Hey. Don't forget me!"
    $ asked_cleaning = True
    jump main_kingspawn

label Ole_Ask_Under_Counter:
    e "Ole?"
    o "Hmm?"
    e "Did you happen to see-"
    o "You and Seb?"
    "You nod."
    o "Yeah. It's fine. It was too awkward for me once I realised you're not fixing the counter or something."
    e "I'm sorry, Ole."
    o "I know you young boys have some weird impulses, but I thought you knew better than this..."
    e "..."
    o "Seb shouldn't be putting the shop under the risk of bad reputation. That's reserved for the nocturnal trunk."
    e "I think we won't do it again..."
    o "Ha. I must look like a boring elderly who denies you instant gratification in your eyes, am I not?"
    e "Of course no. You're always right, Ole. I'm glad you're by my side."
    o "Yeah. Stay with Seb more, I think he likes your company."
    e "Do... you like my company as well."
    o "I do, not as much in an essence of Seb's though."
    o "Now, let me continue with my work. I'll see you later."
    e "Ok."
    $ ole_asked_sebas_suck += 1
    jump Ole_Normal_Talk

label Ole_Ask_Goat_Tribe:
    $ opinions_GoatTribe[1] = 1
    e "Hey, Ole. What's your opinion... on the Goat Tribe?"
    o "Rahim told me about your letter from Furkan. He's not very happy with it."
    e "So... what do you think?"
    o "Me? I liked Furkan, but I don't think we should change what has been working out for us."
    o "I think Furkan's hiding something, they wouldn't make peace with us just to... make peace."
    e "Oh, you think they have another motive?"
    o "Yeah, all those unusual things, with outsiders getting teleported from nowhere."
    o "And so much more monsters we see in the forest. I would assume it's from the goats."
    o "After all... they're famous for conjuring monsters."
    e "You think that they made all the monsters appear?"
    o "I guess, but it's just an assumption. You would be better off asking Furkan yourself."
    e "Alright, thank you so much for talking with me, Ole."
    o "Yeah, anything for my little outsider."
    jump Ole_Normal_Talk

label Ole_Apron_Quest:
    e "Ole, I need to ask you for a specific ingredients."
    o "Hmm? What do you need?"
    e "A Green Dye. For Cane's Apron."
    o "His apron, did Rahim tell you the recipe?"
    e "Yeah, he's helping with fixing the apron, I just need something that matches the colour of the fabric."
    o "That's weird, I didn't recall Rahim ever forgiving the tavern owner..."
    o "You know what, I need to ask him about this. [e]. This is a weird occasion for him."
    e "He just told me-"
    o "Come on, let's go kiddo. Just go for a walk to the shop with me."
    hide ole normal
    with dissolve
    if isNight():
        scene rahims_house_night
    else:
        scene rahims_house
    with fade
    show ole normal:
        xalign 0.05
        yalign 1.0
    with dissolve
    o "Hey, Rahim. I've got the courier with me."
    show rahim normal:
        xalign 0.95
        yalign 1.0
    r "Hmm? What's the matter?"
    e "Hi Rahim, I just told Ole about the apron..."
    o "Yeah. Apron, what happened over there?"
    r "I gave [e] the recipe. Is there something wrong?"
    o "No, I was just asking, why are you suddenly helping Cane."
    r "I'm only trying to help [e]. I don't really care about him anymore."
    o "Are you sure?"
    r "Yes."
    o "Have you two, met yet?"
    r "No, like I said, I don't care about him. But [e] is a good person."
    o "Alright. I understand now. I won't ask too much questions, Rahim, see you later."
    r "Take care Ole, and you [e]."
    e "Oh... Goodbye, Rahim."
    hide rahim normal
    with dissolve
    hide ole normal
    with dissolve
    scene black
    with fade
    "You and Ole walk back towards the shop, he didn't say a word along the journey, he simply looks forward, almost ignoring your existence."
    scene kings_pawn
    with fade
    show ole normal
    with dissolve
    o "Alright, kiddo."
    e "Ole, May I g-get the ingredient... from you?"
    o "Well I trust Rahim's judgement. You must be the best visitor he has had, at least you actually made him help the bat."
    e "U-uh... I didn't do anything actually. I was just asking him for help."
    o "You are brave to ask that in the first place. I'd give you that."
    o "Anyways, I don't have strong opinion on Cane anyways. Just wanted to be sure of Rahim's decision."
    o "And you wanted some green dyes right? I can make one right here, Seb and me picked the leaves from the town area. We have no use of that anyways."
    e "Thank you so much, Ole. This is really great news."
    o "So... what do you think?"
    e "Hmm...?"
    o "Cane, the Tavern owner."
    o "Do you think I should trust Cane?"
    e "Wait... are you asking for my opinion?"
    o "Yes, it's always better to judge from someone who haven't gotten used to the village yet."
    menu:
        o "Do you think I should trust Cane? I can't speak for Rahim, obviously, but is he decent enough now?"
        "Yes, you can trust him":
            $ ole_trust_cane = True
            e "Of course, Cane is not a bad person I believe."
            o "Hmm... really? Seb told me the same, but you know, I don't really interact with the tavern that much."
            o "But I see, I see. I'll take your advice into my consideration."
        "No, you cannot trust him":
            $ ole_trust_cane = False
            e "No... I guess you really shouldn't trust him too easily."
            o "That was what I was thinking, he must have scammed you so hard you work for him now."
            o "Alright I see, I see. I'll take your advice into my consideration."
    e "Well... you should definitely judge him yourself when you meet him."
    o "I've met him, a lot of times. But since the infiltration, I haven't talked with the bat."
    e "People do change, I believe."
    o "It depends, really. Could you really forgive someone entirely just because they're a different person now?"
    o "I don't know, but I can see how you made Rahim talk now, roommate."
    e "Look, if you need me, I'll be right around the corner."
    o "Sure thing. Here's the dye you need."
    e "Thanks a lot, Ole."
    o "See you, kiddo."
    $ addItem("Green Dye", inventory, 1)
    jump main_kingspawn

label Ole_Sick_Quest:
    scene kings_pawn
    with dissolve
    "As you open the bedroom door, you see Sebas jumping just outside the door."
    show sebas scared
    s "Roomie, roomie! You are just in time. Come with me. Something's wrong with O!"
    "Before you can get an understanding of what's going on, Seb drags you along."
    "Both of you enter Ole's room."
    scene ole_bedroom
    with dissolve
    "Ole lays in his bed. He looks like he is asleep if not for the paleness on his face and his faint breathing."
    e "Seb, what happened?"
    s "I don't know. I came to wake up O this morning and I found him like this."
    s "I tried to wake him up but he didn't give me any response."
    s "I shook him and realized his body is extremely cold."
    "Seb grabs your hand and places it on Ole's forehead. Seb's right. You feel like touching ice."
    "Ole doesn't respond to your touch either."
    "Seb pulls your hand away."
    s "Roomie, what should we do?"
    s "Normally, we'd go to the doctor but O is our doctor!"
    "Seb starts to fidget."
    e "Seb, you need to calm down."
    e "Let me think."
    e "Yes. We can go to Haskell. He was once Ole's teacher. I'm sure he can help us!"
    "Seb claps his hands together."
    s "Roomie, that's a great idea! You should hurry to get Haskell. I'll stay here and watch over O! Come back quickly!"
    "Seb basically throws you out of the shop."
    $ QuestBegin(quest15)
    $ quest15.qProgress(__("Visit Haskell"))
    jump main_lusterfield01

label Ole_Sick_Quest_End:
    scene kings_pawn
    with dissolve
    show sebas normal
    with dissolve
    if quest15.status == 2:
        s "Hey... Why are you still here... buddy?"
        e "Uhm..."
        s "Hurry! Go ask Haskell what's going on with Ole!"
        e "Alright!"
        jump main_lusterfield01
    elif quest15.status == 3 and LookForItemNumber("Ginger", inventory) < 4:
        s "Hey, Roomie... D-did you get.... the... ginger?"
        e "Uhm... I still need some of them."
        s "Haskell is taking care of Ole inside. Just come back as soon as you found 4 gingers"
        e "Alright!"
        jump main_lusterfield01
    "As you enter the shop with all the required herbs, you see a nervous and slightly dejected Seb posted at the counter."
    "Seb brightens up when he sees you."
    s "Roomie, thank you for getting Haskell here so fast! And for keeping a cool head."
    e "It's nothing. Seb, why are you out here and not with Ole?"
    "Sebas' lips turn down."
    show sebas scared
    s "Haskell kicked me out because I was distracting him too much with my endless pacing."
    s "His words, not mine."
    s "I suppose everyone's a bit stressed."
    s "I would like to stay but I didn't want to disturb Haskell if he's here to help O."
    "Seb notices the thing you're carrying."
    s "Have you gotten everything?"
    e "Yes."
    s "Good! Roomie, you're amazing as always. Quick. You need to get to Ole's room."
    s "Then, we'll be sure to get O on his feet soon."
    "Seb pushes you along."
    s "I'll stay out here to hold the fort, so don't worry."
    s "I trust you and Haskell."
    "You walk into Ole's room."
    scene ole_bedroom
    with dissolve
    "Haskell is seated before Ole's bed. Hearing your footsteps, he turns around."
    show haskell normal
    with dissolve
    h "Wonderful. You're here."
    "You are gobsmacked because as Haskell stands up and moves away, you notice that Ole is naked in bed."
    "Haskell follows your gaze and nods with understanding."
    h "Remember my diagnosis? It was correct."
    h "Basically, the hemostatic system in Ole is out of fritz. That's why his body temperature is so low."
    h "But with the herbs that you bring, we should be able to fix a potion that will correct that."
    "Haskell takes the gingers from you. You are still quite in disbelief at what you're seeing."
    h "With regards to Ole's state of undress, it's to ease ventilation of body heat."
    "Haskell hands you a towel."
    h "Here. We do not want any liquid to form on Ole's skin. It'll mess with the heat dissipation."
    "You accept the towel that is slightly damp."
    e "Okay. What should I do then?"
    h "You do nothing for now. I will go make the potion and will be back in a minute."
    "Haskell strides out of the room."
    "You stand there, not knowing what to do."
    "You wring the towel. There's an unmistakable scent of Ole that wafts off the towel. You believe Haskell has been using it to wipe down Ole's naked body."
    "Speaking of... Your eyes wander naturally back to the bed."
    "Ole is normally under a lot of layers, so you have no idea that he is so buff."
    "Spikes run along the back of his arm and different from what you imagined, scales do not cover the entirety of his body."
    "His pecs and abs are pure muscle."
    "You clear you mind and try to focus. Thankfully, at that moment, Haskell strides back in."
    h "Alright. The potion is done."
    "Haskell cradles Ole's head and rather roughly tips a potion down into Ole's mouth."
    h "That should do the trick."
    "He says after the vial is empty."
    "Haskell lays Ole back down and stands up to face you."
    h "The hard part's over. With the potion, Ole should be recovering. He'll be active again by tomorrow."
    e "That's it?"
    h "Yes. Told you it's just a normal disease. You and the lion worry too much."
    h "If you don't believe me, see for yourself."
    "Haskell gestures at Ole's face."
    "You can see colors returning to Ole's cheeks."
    h "If you really want to help, you can help wipe down his body."
    h "The potion will raise the heat of Ole's body and he will perspire."
    h "Use the towel to keep him dry."
    h "I'm much too lazy so I'm off."
    "Haskell walks out and disappears like the wind."
    hide haskell normal
    with dissolve
    "Seconds later, you hear bouncing footsteps coming down the hall."
    "Seb pokes his head through the door."
    show sebas normal
    with dissolve
    s "Roomie, I hear that O is doing better?!"
    "Seb glances at Ole and lets out a big sigh."
    s "Yes, our friend does look better than before!"
    s "Right. I ran into Haskell as he left the shop."
    s "He told me what we're supposed to do."
    show sebas grin
    with dissolve
    s "I have to man the counter while the shop is open but I'll take over the shift from you at night."
    e "Alright."
    s "Haskell might not look like it but he really cares about Ole. I doubt he would have done this for anyone else."
    s "Anyway..."
    "Seb's eyes appear to take in Ole's state of undress for the first time."
    "He then looks over at you with a cheeky smile."
    s "Roomie, just remember that O is still sick. So don't go pushing his body too much."
    "You blush as Seb turns and walks away with a laugh."
    hide sebas
    "You sit down on the chair Haskell vacated earlier."
    "You look down on Ole. You see more of Ole's recovery signs."
    "His breathing is more regular, and his chest is rising and falling evenly."
    "This comes as a relief for you."
    "You sit there for a while..."
    "And suddenly Ole groans softly."
    "He turns his head away from the sun filtering through the window."
    "You can see a sheen of sweat on his forehead."
    "The potion is working."
    "You quickly move to wipe away the sweat."
    "Ole responds positively to your touch. He calms down and stops fussing as much."
    "After you sit back down, you notice a bead of sweat sliding down the crevice between Ole's pec."
    "You swallows nervously as you reach over. You keep reminding yourself that you're only doing a doctor's work."
    "The surface of Ole's pecs are supple and perky. But you can feel the wiry and taut muscles underneath."
    "He must have done a lot of training."
    "You believe that they must be as hard as steel when Ole flexes them."
    "You sheepishly wipe away the sweat."
    "Your hands then move to wipe down Ole's stomach."
    "Even at rest, Ole's abs are well-defined."
    "The scales resting between the creases gives the abs great musculature."
    "You cannot help but be impressed."
    "Ole's body tightens at the sensations."
    "His pecs firm up."
    "The nipples rise as the muscles get pulled."
    "The abs become rigid with temporary tension."
    "The sheen of sweat glistens off Ole's torso."
    "It looks like a sculpture chiseled in stone."
    "Soon after, Ole settles."
    "Everything relaxes into place."
    "You took another wipe around Ole's chest."
    "His bust is bouncy. You know it'd be comfortable to lay in his embrace."
    "After that, you decide you have to deal with Ole's lower body too."
    "You look over and Ole's crotch immediately catches your attention."
    "The skin closes over his crotch and forms a well-defined slit."
    "The skin around the slit is very soft to the touch."
    "You remind yourself that you're only helping."
    "You note that this is the warmest body part you've touched."
    "Even though you move as gingerly as you can, you can still feel Ole's endowment underneath."
    "The head of the member stops quite near the slit."
    "You gulp and move the towel to clean up the sweat that has trickled down the sides of the inner thigh."
    "As you swipe the condensation away, you can feel something throbbing."
    "You believe Ole's crotch has gotten more engorged than before."
    "The seams of the slit open up marginally."
    "Seeing this, you quickly pull your hand back."
    "You understand that Ole is still a patient and do not require this additional stimulation."
    "You sigh and shakes your head."
    "Suddenly, you feel a touch on your wrist."
    "You turn and see that Ole is looking at your with slightly open eyes."
    e "Ole! You're awake! Are you feeling better?"
    "Ole nods and mumbles something weakly."
    show ole nshocked
    with dissolve
    o "Water..."
    "You hurry to grab a glass."
    "Ole consume the water slowly. You take the glass away and Ole sleeps back down."
    e "Erm, since you're awake, I'll just..."
    "You point at the door."
    "Ole grabs your wrist again."
    o "Do stay to accompany me."
    "How could you reject that?"
    e "Do you need anything? Anything I can help to make you more comfortable?"
    "Ole smiles his usual kindly smile."
    o "Actually, I like what you've been doing earlier. It's very comfortable."
    "You blush immediately."
    e "You knew..?"
    o "Why did you think I wake up?"
    show ole naked
    "Then, Ole manages a weak chuckle."
    "You move the towel back to the slit."
    "Ole winces slightly."
    e "Are you alright? Maybe we should..."
    o "It's fine. Carry on, kiddo. I'm just sensitive down there."
    "You have to agree with Ole. As you massage the area around the slit, Ole's crotch protrudes further and further."
    "Your fingers press along Ole's inner thigh as the slit slowly open."
    "The dick begins its journey poking through."
    "The dickhead peeks out and it is quivering with anticipation."
    "Perhaps it is the potion kicking up Ole's inner temperature, you swear the temperature rise as Ole's slit pulls back further."
    o "Hng..."
    "All of sudden, Ole moan. You quickly turn to him."
    e "Are you alright? Should we stop?"
    o "No. It's not that..."
    "Ole's cheeks burn. His voice lowers."
    o "Can you help me? I think my cock is stuck. I would normally pull back the slit myself but I'm too weak to reach down."
    "Ole's face heats up even more."
    "You find this very charming and hot."
    e "Of course."
    "Your fingers pinch the rims of the slit and gently eases them back."
    "Without the obstruction, Ole's pole resumes its rise."
    "Ole moans with satisfaction."
    show ole erect
    with dissolve
    "Ole's dickhead is smooth, but the shaft is veiny."
    "The veins travel all the way down to end beyond the slit."
    e "Let me just wipe it down."
    "You wrap the towel around Ole's cock and massage it."
    "Ole's cock responds greatly."
    "The crown turns pinkish and you can feel the cock pumping even though the fabric."
    "You believe the graininess of the towel provide stimulating sensation."
    "To prove your point, Ole's dick started to leak precum."
    o "Thankfully, you have a towel ready."
    "Ole jokes with a red face."
    "You use the towel to catch the leaking beads of precum."
    "You rub the wet towel back on Ole's cock."
    "Ole's cock bounces and twitches."
    "It is waiting desperately for release."
    o "[e]..."
    e "Hmm?"
    "It is sure that Ole doesn't say this often but the words take a long time before they move out of his mouth."
    o "Can you jerk me off? I would do it myself but I'm much too stimulated and too feverish."
    e "Okay."
    "You grip the base of Ole's cock with the towel."
    "Then, you run it up along the entire length of Ole's dick."
    "When you reach the top, you use the towel to rub the tip of Ole's crown."
    "Ole's dick rewards you by shooting out several drips of sticky precum."
    o "Hmm..."
    "You work your way back down to Ole's base."
    "Ole's cock shivers as your hand trails downward."
    "When you press against the open slit, Ole moans softly."
    "You look up and Ole is blushing furiously."
    "Then, he admits shyly."
    o "I'm very sensitive at that spot."
    "You immediately know what to do."
    "Your fingers dig through the edge of the slit."
    "Ole's slit has gotten quite supple from the stimulation."
    "Therefore, even with his cock in the way, your fingers wedge through the slit and into Ole's inner cavity."
    "You press your fingers on the underside around Ole's slit."
    "Ole moans at the sharp stab of pleasure."
    "His dick jostles about and sends more precum flying."
    "While you keep one hand massaging Ole's slit, your other begins to pump his dick more violently."
    "The double stimulation is sending Ole into ninth heaven."
    "He is sweating openly all over his body and the heat rising off his skin in waves."
    with vpunch
    "The base of Ole's shaft pools with concentration and you know that he is close to ejaculation."
    "You quickly withdraw your hand from inside the slit and grab the towel."
    o "Ah... Ngh..."
    with vpunch
    show ole erect cum with dissolve
    "Rocking with spasms, Ole's well-worked cock shoots out hot spunk."
    "You capture it all with the ready towel."
    "The towel soon gets wet with the copious amount of cum."
    "You slowly let the towel soaks up all the cum. Then you walk to the corner and deposit it in the laundry basket."
    "You walk back."
    e "That should save you the trouble of cleaning."
    "Still gasping for air, Ole look at you through feverish eyes and smiles."
    "Drained, Ole's cock slowly returns to its limp state."
    "No longer erect, the edge of the slit starts to reclaim the cock."
    show ole naked -cum with dissolve
    "The length slowly disappears into Ole's cavity. Eventually, the slit closes up again."
    "By then, Ole had drifted off from the exertion."
    "You clean up all the vestiges of the handjob."
    "You return to keep vigil over Ole."
    "You stay there, just watching Ole's peaceful sleeping face until Seb comes to take over from you."
    "After a worrying and exciting day, you return to your room and immediately slumber."
    $ quest15.status = 4
    $ quest15.qComp(__("Report to Ole"))
    scene black
    with dissolve
    pause 2
    jump bedroom_sleep

label Ole_After_Sick_Quest:
    o "Thank you for taking care of me when I was down."
    e "Don't mention it, Ole."
    o "It's mostly me taking care of others. It's nice to have the roles switched once in a while."
    "Ole lets the conversation linger. You wonder if you should bring up the other thing that happened that day."
    e "Also about the other thing..."
    "Ole's cheeks reddens as he looks into the clear bottle he's holding and scrubbing."
    e "I'm sorry if I was out of line."
    o "It's not that. Don't think that."
    o "It's just... I'm not very experienced in these things."
    o "You're one of the few I've done that with."
    "Ole rubs on that one spot for so long that you swear it cannot be cleaner."
    o "But I'm glad that it happened."
    e "Me too."
    $ QuestFinish(quest15)
    jump main_kingspawn

label Ole_Ointment_Finish:
    e "Ole... I'm back from Haskell's place."
    o "Good! Have you brought back the potions?"
    if LookForItemNumber("Strength Potion", inventory) >= 30:
        $ removeItem("Strength Potion", inventory, 30)
        e "Here they are."
        o "Good, took you some time though."
        e "Yeah, Haskell had to brew the potions for a few days."
        o "Hmm... He does take everything slowly. Like, too slow."
        o "That's why I didn't want to live with him."
        e "I thought... cleaning after a shop is pretty slow, isn't it?"
        o "No. Not at all. You need to appreciate the nuances of it all."
        o "Everything here, we built it from scratch, the counter, the wardrobe, the floor."
        o "I'd love to maintain them. Keep it the same, even when I'm just stressed. It helps me relax."
        e "I've never seen as much of a hardworking cleaner like you."
        o "Am I?"
        e "It's like, you're focused on cleaning... all day."
        o "Well of course I don't only clean stuff, I took a lot of responsibility in maintaining the business as well."
        o "Like getting you to fetch me 30 strength potions."
        o "Speaking of which, did Haskell tell you anything...?"
        e "Uhhmmm.... no...?"
        o "I guess so."
        o "Alright, then. I'll give you my recipe for ointment. Helps with health, and your magic, and if you are horny, lust."
        o "It'll cleanse you of your negative effects if you use it during a combat."
        e "I see. Thank you so much, Ole."
        o "No problem."
        $ QuestFinish(quest08)
        $ discoveredrecipe.append(greenointmentrecipe)
        jump Ole_Normal_Talk
    else:
        e "...I think I took a few... of them."
        o "Then... get Haskell to make more of them, you know."
        o "I want the number to be exact. Hmm..."
        e "Alright."
        jump Ole_Normal_Talk

label Ole_Postal_Finish:
    e "Ole! I'm back from all three training you gave me!"
    if quest02.status == True and quest03.status == True and quest04.status == True:
        o "Hmm... I've heard so! Congratulation, [e]. You are now the courier of the lusterfield!"
        e "Thank you Ole. Your training is really useful. I think I can handle a few adventures right now!"
        o "Ha. Tell that to Seb, Lothar and Rahim. They're pretty helpful teachers, aren't they?"
        e "Yes, they are!"
        o "Now our goods are in your hand, you better be really careful out there, for your own safety."
        e "Haha, I will certainly do!"
        o "Great! Now I'll give you a badge of honor. Courier of Lusterfield."
        "Ole searches around his pocket, and hands you a grey badge, it has the shape of your head, and you can see the word 'Courier' written in the middle of it."
        $ addItem("Courier Badge", inventory, 1)
        e "Woah is that my face on the badge?"
        o "Yeah, I thought I should make it represent you in someway. It should be enough to let people know you are the courier of Lusterfield."
        e "Thanks, Ole. I won't disappoint you."
        o "I know you won't."
        o "Check out the board to start your job. If you have any questions, the Postmaster is there."
        o "You can come up to me as well, for any other questions."
        e "Of course!"
        $ QuestFinish(quest01)
        jump Ole_Normal_Talk
    else:
        o "Hmm, are you sure? Cause I don't think you finished all three of them."
        e "Ahh... You are right."
        o "Then what are you waiting for, I've got to get ready for your badge in the mean time."
        e "Yes! Ole. I'll be back soon."
        jump Ole_Normal_Talk

label Ole_Ask_Kingspawn:
    e "Hey, Ole. How did you and Sebas built this shop?"
    o "Hmm... should I tell you this? I don't know if Seb mentioned it to you yet."
    e "Mention what?"
    o "His Uncle. This shop was built by him actually. We're just working."
    e "Wait... didn't Seb say he owns this place?"
    o "Technically yes, his uncle gave it to him, some kind of consolidation gift."
    e "Hmm... for what?"
    o "It would be unwise for me to continue further. I've already spoken too much. Just know that Seb and me took over this place. End of story."
    e "But now I'm a little curious."
    o "You'll know if you're here long enough. I'm just an outsider to this family matter."
    e "Alright, thanks Ole."
    jump Ole_Normal_Talk

label Ole_Postal_Training:
    $ QuestBegin(quest01)
    $ quest01.qProgress(__("Complete task from Sebas"))
    $ quest01.qProgress(__("Complete task from Rahim"))
    $ quest01.qProgress(__("Complete task from Lothar"))
    e "Ole. Did you mention about the postal training yesterday?"
    o "Yes. so this training I designed it just for you. There's three things you need to learn before your little adventure."
    o "First thing first, I talked to Lothar about you. I think he can give you some basic idea about tackling on a battle."
    o "Second, Sebas can bring you around the corners of the village, he used to travel a lot so just ask him anything about delivering your items."
    o "Third one is just Rahim talking about your equipment, item and making your own clothes."
    e "Are you going to teach me anything particular?"
    o "Nope, I'm gonna stay and watch over the shop. When you finish all three trainings just come back to me and I'll give you a badge of certificate."
    e "This is so elaborate, I thought couriers just take and deliver stuff."
    o "You see, there was another courier from the town, we were pretty friendly. Just like you, he told me that he just takes and delivers stuff. "
    o "Two weeks later, he died to the monsters on the way to Lusterfield."
    e "Really? How did you know..."
    o "Well no one has seen him again. We assumed he was unfortunately eaten by the monster. The moral of the story is, always be prepared for any kind of threat."
    o "Things doesn't always happen like how you imagined. So just take the training seriously, I don't want to lose you to the wild just like the last courier."
    o "Alright, enough serious talk. I wrote all the details of the training in your journal, remember to check it out if you forget about anything."
    e "I will, Ole."
    msg "Your Journal has been updated."
    jump Ole_Normal_Talk

label Ole_Ask_Lusterfield_People:
    e "Hey, Ole! How are the people in Lusterfield doing?"
    o "Good! It's a beautiful day today isn't it. Everyone's enjoying their life right now."
    o "You might wanna get some training, if you still remember."
    o "After that, you can go check out the courier board for some odd jobs. Haimo can help you with that."
    o "If you need some other informal training, Lothar is also here, I'm sure you can always learn some more from him."
    o "And we have Rahim, of course, I think he's making you a leather armor for travel purposes, remember to go visit him before you set out on your little adventure."
    o "Maybe when you fancy yourself a drink, you can always get one from Cane's place. It's where Seb usually visit at weekend."
    e "Oh... Does Sebas drink a lot?"
    o "Usually, he is the flirty type there. Don't take the lion too serious when he's drunk though."
    o "To be fair, our villagers have a tendency to get themselves drunk all the time."
    e "Do they like the alcohol a lot?"
    o "I don't know, not like I've tried that stuff..."
    o "The thing is, if you do visit Cane's place, be careful when you owe them money for a beer. You don't want to know what may happen there."
    e "What may happen there?"
    o "I don't know... you have to be careful even in the village. Not a lot of villagers are kind like us."
    e "Ok. I'll be on the look out, thanks Ole."
    jump Ole_Ask_Lusterfield

label Ole_Ask_Lusterfield_Lothar:
    e "Hey, Ole."
    o "What's going on, [e]?"
    e "Do I really need to go to Lothar for training?"
    o "You are still bothered by that? Oh... I'm sorry I didn't give you a heads up. He hasn't acted this way before."
    e "But... What's his deal with people, is he always like that?"
    o "Deep down inside, Lothar is a good person. He just has some kind of grudge against newcomers."
    o "I don't want to dig up ancient history, but once he gets along with you, he'll be fine to handle."
    e "He seemed like a different person when you talked to him. Are you two friends?"
    o "Kind of. It really depends."
    e "Depend on what?"
    o "If I can control his temper a little bit. Usually he is fine, like a normal wolf."
    o "So, just come to me if he does anything bad. Ok? I'll take care of him. Plus, if you two get along you can learn a few tricks and tips about fighting."
    e "Alright Ole, I'll trust you."
    o "Thanks, kiddo."
    jump Ole_Ask_Lusterfield

label Ole_Ask_Himself:
    if ole_location == "kingspawn":
        e "How are you doing, Ole."
        o "Doing Fantastic. I'm cleaning up the Cabinets right now."
        e "Anything interesting going on in the shop?"
        o "You want something interesting? I can tell you something interesting."
        o "We just got a new tenent here and this new tenent is going to pay their part of the rent, every month."
        e "W-wait..."
        o "Ha. Just kidding kiddo. You don't need to pay any rent. We bought the place, mostly from Seb's side."
        o "Honestly though, traffic is not in our favour here today. Most of our customers are local regulars."
        e "Is it always like this?"
        o "No. Not really, we used to have travellers abroad the continent visit us to sell their valuables."
        e "What happened? Why are they not coming here now?"
        o "Well [e], people are scared of the monsters. They've been roaming on the path a lot lately."
        e "I can help with clearing up the path."
        o "Yeah kiddo. Meanwhile let me clean this scrub off the cabinet."
        jump Ole_Normal_Talk
    if ole_location == "nocturnaltrunk":
        e "Hey, Ole. What are you doing?"
        o "Eating some bread."
        e "Are you not drinking with the others? I thought lizards are pretty alcohol resistant."
        o "I'm not drinking kiddo, especially not here."
        e "Why not? Sebas is pretty drunk now."
        o "Someone's gotta be sober, and be the responsible one for the lion."
        o "Else no one's taking him home, kiddo."
        e "Ole, you might want to relax sometimes, you know."
        o "I'm relaxed. Don't worry."
        e "Alright, I'll see you later."
        jump Ole_Normal_Talk

label Ole_Dialogue_End:
    o "Alright kid, have a good day."
    hide ole normal
    if ole_location == "kingspawn":
        jump main_kingspawn
    if ole_location == "nocturnaltrunk":
        jump main_nocturnaltrunk2
    jump main_kingspawn


label Rahim_Dialogue:

    hide screen menu_buttons
    scene black
    if isNight():
        scene rahims_house_night
    else:
        scene rahims_house
    with fade
    show rahim normal
    with dissolve

    if quest01.status and timenow.day > 2 and checkNoShopItem("Leather Armor"):
        jump Rahim_Leather_Armor
    if isNaked():
        if rahim_letnaked == 2:
            show rahim normal
            with dissolve
            r "You, better cover yourself up."
            e "Hmm."
            r "..."
            r "Is this one of your tribe's weird tradition?"
            menu:
                r "I don't mean to offend but having your dicks out... in the cold wouldn't make sense... right?"
                "Being Naked is my Tribe's Tradition":
                    $ rahim_letnaked = True
                    e "Yes, it is. I'm just so sorry I forgot to... put on something."
                    r "Look, I'll respect your tradition, whatever it is."
                    r "Just don't get a random boner when we talk..."
                    e "Uhh- I'll try...{size=15} if only you aren't looking that hot... {/size}"
                    r "What?"
                    e "Nothing."
                    jump Rahim_Normal_Talk
                "Being Naked is not my Tribe's Tradition":
                    $ rahim_letnaked = False
                    e "No, I just like to... let it out sometimes."
                    r "Disgusting."
                    e "Uhh- I didn't know you don't lik-..."
                    r "Sorry, but I don't want you to swing your dick around my shop."
                    r "Put on whatever you wish, at least cover it up. Then we'll talk."
                    jump main_rahimshop
        elif rahim_letnaked:
            show rahim normal
            with dissolve
            r "You are naked again?"
            e "I forgot to put them on, Rahim."
            r "No leave it be... I'll have to get used to that..."
            r "But I'll have to remind you again, don't get a boner while we talk. Understand?"
            e "Uhh, alright."

            jump Rahim_Normal_Talk
        else:
            r "You better cover yourself up."
            e "Hmm..."
            r "I feel ashamed for you, [e]. Just put on your clothes. I'm not telling you again."
            e "I'm sorry about that, Rahim."
            r "..."
            jump main_rahimshop
    if pc.armor["Clothes"] != None and pc.armor["Clothes"].img == "Woven Tunic" and renpy.random.random() < 0.5:
        r "Oh? That tunic looks good on you, [e]."
        e "Yeah, it is. After all it's made by the best tailor in the world..."
        "You catch a small grin from the old bull, but he quickly hides it."
    elif quest43.status == 2 and vote_result < 0:
        e "Rahim, should we go to the Mayor's house now?"
        r "Yes. Now go."
    elif rahim_tut == 1:
        r "You are [e]. Correct?"
        e "Yes. Nice to meet you, Rahim."
        r "Ok."
        $ rahim_tut += 1
    else:
        r "How goes it, [e]."
        e "I'm well, thanks Rahim."
    jump Rahim_Normal_Talk

label Rahim_Normal_Talk:
    menu:
        r "So, what are you up to, boy."
        "Learn his opinion on the vote" if quest37.status == 2 and quest37.start_date + rahim_vote_duration  >= timenow.day:
            jump Rahim_Voting_Opinion
        "Ask about his talk with Furkan" if quest37.status == False and timenow.day >= rahim_recon + 3 and rahim_recon != 0 and rahim_recon > -9999:
            jump Rahim_Voting_Quest_Begin
        "Begin preparation for the vote" if quest37.status == False and rahim_recon < -9999 and rahim_recon != 0:
            jump Rahim_Voting_Quest_Begin_Ready
        "Ask about Pirkka's Prose" if quest35.status == 3:
            jump Rahim_Prose_Ask
        "Ask about Postal Training" if quest01.status == 2 and quest03.status == False:
            jump Rahim_Postal_Training
        "Pick up the delivery" if is_client("Rahim"):
            $ client_name = "Rahim"
            call Courier_Pickup_Dialogues from _call_Courier_Pickup_Dialogues_6
        "Deliver the goods" if is_recipient("Rahim"):
            $ recipient_name = "Rahim"
            call Courier_Delivery_Dialogues from _call_Courier_Delivery_Dialogues_6
        "Ask about Fixing with the Apron" if quest07.status == 2:
            jump Rahim_Apron_Quest
        "Ask about the fixed apron" if quest07.status == 3 and LookForItemDefense("Tavern Apron", inventory) == 6:
            jump Rahim_Apron_Fixed
        "Ask about Rahim's Request" if quest19.status == False and quest11.status == True and quest11.completed_date + 3 < timenow.day:
            jump Rahim_Flower_Quest_Begin
        "Report about his flowers" if quest19.status == 3 and LookForItemNumber("Chrysanthemum", inventory) > 3:
            jump Rahim_Flower_Quest_Finish
        "Finishing Postal Training" if quest03.status == 2:
            jump Rahim_Postal_Finish
        "Ask to help Rahim" if quest19.status == True and taskAvailable(task04, quest19) and task04.completedtimes == 0:
            jump Rahim_Yarn_Quest_01
        "Take Rahim's Commission" if taskAvailable(task04, quest19) and task04.completedtimes == 1:
            jump Rahim_Yarn_Quest_02
        "Take Rahim's Commission" if taskAvailable(task04, quest19) and task04.completedtimes == 2:
            jump Rahim_Yarn_Quest_03
        "Report to Rahim about the clothing" if task04.status != True and task04.status != False:
            if task04.completedtimes == 0:
                jump Rahim_Report_Yarn_Quest_01
            if task04.completedtimes == 1:
                jump Rahim_Report_Yarn_Quest_02
            if task04.completedtimes == 2:
                jump Rahim_Report_Yarn_Quest_03
        "Ask about his new outfit design" if quest07.status == True and quest08.status == True and timenow.day > quest07.completed_date + 3 and quest09.status == False and timenow.day > 12:
            jump Rahim_Outfit_Quest
        "Report to Rahim{#OutfitReport}" if quest09.status == 2 and opinions_Outfit[0] > 1:
            jump Rahim_Outfit_02
        "Report to Rahim{#OutfitReport}" if quest09.status == 3 and opinions_Outfit[4] > 0:
            jump Rahim_Outfit_03
        "Report to Rahim{#OutfitReport}" if quest09.status == 4 and opinions_Outfit[8] > 1:
            jump Rahim_Outfit_End
        "Tell Rahim you are ready for the vote" if rahim_vote_ready and quest37.status == False:
            e "Alright, I think we're ready for the vote now."
            jump Rahim_Voting_Announcement
        "Ask for his opinion on Goat Tribe" if quest06.status == True and quest06.completed_date + 1 < timenow.day and opinions_GoatTribe[2] == 0:
            jump Rahim_Ask_Opinion_Goat_Tribe
        "Deliver the Letter from Furkan" if quest06.status == 2:
            jump Rahim_Letter_Furkan
        "Ask about Lusterfield{#RahimAAL}":
            jump Rahim_Ask_Lusterfield
        "Ask about his Tailor job":
            jump Rahim_Ask_Tailor
        "How is he doing":
            jump Rahim_Ask_Himself
        "That's all for now":
            jump Rahim_Dialogue_End
    jump Rahim_Normal_Talk

label Rahim_Ask_Lusterfield:
    menu:
        r "You want to know about...?"
        "Ask about the people here":
            jump Rahim_Ask_Lusterfield_People
        "Ask about the Goat Tribe invasion":
            jump Rahim_Ask_GoatTribe
        "That's all I need to know":
            jump Rahim_Normal_Talk

label Rahim_Leather_Armor:
    e "Hello, Rahim."
    "Rahim is still threading his needles, until he's distracted by your voice."
    "He doesn't even move his head, just staring at your general direction as he tries again with a new needle."
    r "Oh, right. I just finished your leather outfit. It's right there."
    "The tailor raises his head to point at the cabinets, where you see a piece of leather armor tidily placed inside a wooden box."
    e "Thank you so much, Rahim. Is it the one made after you measured my waist?"
    r "Yes."
    e "I don't know what to say, thank you for being so kind to me."
    "You reach over and take the armor, trying to check the size."
    e "Oh, I think it fits me perfectly, and the leather is very light-weight too."
    "Rahim lowers his head, eyes focused on the piece of garment on his table."
    e "Ah, should I try it out now? This will come in handy when I go on adventures. How did you get all these quality fabrics."
    e "Rahim?"
    r "No, I'm working right now, you can take the box back to the shop. And the door is right there."
    "His response comes to a shock for you, paired with the stern face he gives, it feels like he didn't even want you here."
    "You freeze for a moment, holding the box with the leather armor in it. As if you're waiting for some kind of follow up."
    "The tailor is still staring at his work, pausing for a few seconds, he furrows his brows before looking up again."
    r "Welcome to Lusterfield, [e]."
    e "Hey, I get it. Thank you for the armor again. I- I'll go now."
    "You pat on Rahim's shoulder, which caused him to shudder a bit. Rahim stares at you blankly until you finally leave him alone."
    e "Bye, Rahim!"
    $ addItem("Leather Armor", inventory, 1)
    jump main_lusterfield02

label Rahim_Yarn_Quest_03:
    if rahim_yarn == 1:
        e "I was wondering if you had any more commissions for me to do? I learned a lot last time, and I'd love to try again."
        "Rahim looks up from his sewing, and looks at you with what seems to be bemused exasperation."
        r "Excited, aren't you."
        e "Yeah! I hear awesome stories, get to learn tailoring, and earn money. What's there not to like?"
        "The bull heaves a sigh, grumbling about unexpected work and having to find the materials."
        "Despite that, the bull's permanent scowl is missing from his face. He still looks grumpy, of course, but he seems to be in a good mood."
        r "I do have a commission ready for you, [e]."
        r "It's also, luckily for the both of us, not a hat."
        "There being no hats seems to be a genuine relief for the bull. The process was annoying, certainly, but it's surprising that they cause him this much trouble."
        e "So, I'll be learning something new?"
        "Rahim gives you a curt nod before taking out several bolts of colorful cloth."
        r "Yes. You'll be making a scarf this time."
        "You look at him quizzically."
        e "Isn't that sort of easier than a hat?"
        "You get a nod, and a look of annoyance."
        r "I was trying to go easy on you."
        r "Despite that, this isn't going to be a walk in the park for you."
        r "Scarves need to be lightweight but durable - soft, but pliable. To make things harder for you, the patterning on this scarf is difficult, alternating blue, gold and red in irregular rings."
        e "Ah. And here I was celebrating."
        r "Never celebrate if you're helping me. You know who taught me, and I haven't learned a teaching method other than his."
        "Raising an eyebrow at him only earns an eyebrow raise in response."
        e "I don't see any wolves around here."
        "You say this, entirely joking."
        "Rahim snorts lightly, closing his eyes in a mockery of lacking patience."
        r "No, I suppose you don't."
        r "If you want, I can provide them?"
        "That's the first joke you've ever seen Rahim cra-"
        "Oh. He's serious. That light in his eyes is serious."
        e "No, I think I'll pass on that, thank you Rahim! I am reasonably challenged by this and appreciate the commission! I'll be going now!"
        "Despite your best effort to slip out before Rahim managed to track down a feral wolf, you stop when a loud voice yells your name."
        "Guiltily, you turn around to a now {i}genuinely{/i} unhappy bull."
        r "If you're going to take a commission from me, you're going to do it right."
        r "You don't even have the list of materials, or the materials I was going to generously provide you with myself."
        e "M-my apologies, Rahim. I didn't mean to dash out like that."
        "Rahim sighs yet again, a pained expression on his face."
        r "I understand. You understand I'm not going to throw you to an actual wolf, yes?"
        "A sense of relief floods your body."
        e "R-really?"
        "The peeved look on Rahim's face is all you needed as an answer."
        r "Yes. Throwing you at a wolf would do nothing for you as a tailor - neither would it help my shop."
        "Those are some of the worst reasons you could ask for, as none of them involve your safety, but it is certainly better than the alternative."
        e "What about if I require wolf fur?"
        r "Then I'll probably buy it for you. You could make these bolts of cloth."
        "Rahim drops the bolts of cloth he took out into your hands as he speaks."
        r "But I'm not going to make you do that. It'd be a waste of my time and yours."
        "Chastened by Rahim's harsh rebuke, you dip your head in acknowledgement and apology."
        e "You're right. I'm sorry about that, Rahim."
        "Again, Rahim sighs deeply. While he doesn't look grumpy, you can't tell if that's better or not - the complex mix of amusement and frustration isn't something you can easily categorize or understand."
        "Undeniably bad was the disappointment you saw flicker across his face when you told him you were genuinely worried about the wolf."
        r "It's alright. You took me seriously when I was making a bad joke."
        r "Just... go finish the commission. I'll figure out a story I can tell you when you come back."
        "You clearly don't understand this man. He was joking before? His face was dead serious."
        "Then again, it always is."
        e "Can I make a request about the story?"
        "Rahim opens his mouth to make an irritated comment, but closes it and considers what to say more carefully."
        r "You can make it. I cannot promise I will deliver."
        "You gulp, and nod."
        e "I want to hear about what group of people taught you the most about sewing after you started adventuring. Who they were, their culture... all of it."
        "Of all the things you expected that to bring out of Rahim, pain was not one of them."
        "Despite that, Rahim looks as gutted as a man just told his pet had died."
        r "That... It's a good question. I'll have to think about it."
        r "Farewell."
        "He's schooled his face back into neutrality and returned to sewing at this point. Despite that, you know that both of you know what you saw."
        e "Yes, I'll... I'll be back when I finish the scarf."
        e "Thank you for giving me the commission."
        "Rahim doesn't react to your words."
    else:
        e "I hope things are going well, Rahim."
        "The bulky bull grunts at you noncommittally."
        e "I was wondering if you had another commission for me?"
        "This time, the bull looks up at you."
        r "I have another hat for you to make."
        "After last time, you understand why the man hates hats."
        e "Would you happen to have any other commission I could work on?"
        "Rahim gives you a level glare."
        "You refuse to quail under his gaze, looking back at him with what you hope is confidence."
        r "Fine. I have a scarf that you can work on."
        "Rahim passes you a list of ingredients you'll need."
        e "Sounds good. I'll come back once it's ready."
        "Done with the conversation, Rahim focuses on his work once more."
    $ discoveredrecipe.append(longscarfrecipe)
    $ TaskBegin(task04)
    jump main_rahimshop

label Rahim_Report_Yarn_Quest_03:
    if not callInventoryItem("Long Scarf", "Mask"):
        if rahim_yarn == True:
            e "I'm pretty happy with how the scarf turned out."
            e "I wasn't happy with it at first, but a few finishing touches helped patch things up."
            "Rahim looks up from his project in pleasant surprise."
            "He drops his project completely for now, getting up to take the scarf from your hands."
            r "Let's see how it went."
            "Rahim first gives the scarf a light look-over for anything out of the ordinary."
            r "At first glance, it seems quite well made, if even more patterned than the original commission requested."
            "You scratch the back fo your head, beneath your horns, embarrassed."
            e "Those were the finishing touches."
            e "I didn't like the original design that much, so I got a bit carried away adding small improvements here and there."
            e "Before I knew it, I had touched up the entire scarf."
            "Rahim snorts in amusement."
            r "You're supposed to do what the commissioner asks and nothing more or less. Personal projects and original designs are where you get to explore."
            r "I'd chew you out for it if you didn't do such a damn good job of it."
            "Rahim's scowl is once again absent from his face. In its place is a very small smile."
            r "Don't let your head get too big, but I can tell you've been listening to my lessons. Your work lacks many of its prior faults."
            e "I've improved?"
            "Rahim gives you a sidelong glance, mildly irritated and amused."
            r "I'd recommend you don't fish for compliments with me. You already know the answer from what I've told you."
            "He's right. You still wanted to hear him say it though."
            "Rahim sees your disappointment - not difficult considering the poor job you did of hiding it. He looks a bit guilty after that."
            r "It's good to have someone else with an interest in tailoring. Up until now your work was uninspired, if high quality, but the scarf shows actual passion."
            "...He really sucks at giving compliments. You clear your throat to try and take some of the awkwardness out of the air."
            e "You're right. I noticed the time go by when I did the other projects, but with the scarf, it felt like I sat down to work on it, and suddenly had the completed scarf in my hands."
            "Rahim lets out an approving grunt."
            r "I do not notice time pass while I am working either."
            r "It is as much of a boon as it is a bane."
            "You raise an eyebrow at that."
            e "What downsides does it have?"
            r "It can be hard to remember to go check up on people or eat. There have been especially interesting projects that have lead me to work for three days without sleeping."
            r "I hadn't noticed the changing of the days in the moment, but lit and unlit my candle by instinct so I could keep working."
            "A shiver goes through your body. Hopefully you never quite reach that level of passion."
            e "You only realized when you finished?"
            "Rahim snorts dismissively."
            r "No, I noticed when I woke up 12 hours later, having collapsed over my work."
            "It sounds dangerous for a person like this to live on his own. Does nobody take care of him?"

            menu:
                "The answer to the question comes to you shortly after. It's a good thing you didn't ask."
                "Offer to help":
                    $ rahim_like += 2
                    e "You know, if you ever start an especially big project or something, you can tell me, and I'll bring you food and make sure you sleep, Rahim."
                    "Rahim blinks at you in surprise. You cringe, expecting him to chew you out for what you said."
                    "Instead, his expression softens."
                    r "I haven't had anybody offer something like that in..."
                    "He clears his throat slightly."
                    r "...years."
                    "The bulky bull looks you over, as he would one of his tailoring pieces. Despite his eyes seeing only skin, fur, and cloth, it feels like he's peering into your soul."
                    e "Well, it sounds dangerous. If I can't convince you to take care of yourself, I can at least try and help."
                    e "I know you'd do the same for me"
                    "If reluctantly."
                    r "I know you well enough to know that you will visit me regularly to make sure I'm eating and sleeping if I say no."
                    r "So I'll say yes."
                    "Not quite the answer you wanted, but good enough for now."
                    e "Alright, my cooking services are only 100 gold a meal-"
                    "Rahim narrows his eyes."
                    r "I can still take back what I said, you know."
                    "The intensity of his gaze makes you break a sweat."
                    e "I was just kidding, please have mercy, Rahim."
                    e "You know I wouldn't make you pay for helping you out."
                    "Rahim snorts skeptically."
                    r "So you don't want the gold from making the scarf?"
                    "Your eyes widen in shock, before returning to normal as you realize he's joking."
                    "Going by when he assigned you the commission, Rahim's style of joking is to say something brutal, and be even more deadpan than usual."
                    "You should probably start a guide to how to interact with him properly - he's frustratingly difficult to understand sometimes."
                    e "You know that's not what I meant. But I'll give you the scarf for free if I have to - I don't do this for the money alone."
                    "Rahim looks pleasantly surprised by your reaction to his joke. Well, as 'pleasant' or 'happy' as the grumpy bull's scowl can look."
                    r "There's no need. You'll get your gold, as well as your story."
                    r "I give credit where it's due."
                    "The bulky bull snorts, and his tail flicks to the side rapidly as he finishes his thoughts on the matter."
                    r "As a citizen of Lusterfield, you knew this already, but."
                    "You meet Rahim's eyes, and find yourself trapped there by the determination they are filled with."
                    r "I'll come to your assistance if ever you need me."
                    "A nervous gulp later, and you find yourself nodding."
                    "A lot happened after your offer, and you don't quite know how Rahim feels about it all. All you can do is hope that he appreciated it."
                "Express condolences":

                    e "That sounds like an awful experience."
                    "Rahim shrugs his shoulders at that."
                    r "It's the cost of passion."
                    r "I can and do pay it every single day of my life."
                    "You grimace subconsciously."
                    e "Is passion really worth risking life and limb over?"
                    "The bull just looks at you with his typical scowl highlighting his features."
                    r "I'm not exactly risking all that anymore."
                    r "If anything, I wish I had risked more. A life without passion is one not worth living."
                    "There is no doubt in his voice. You hope never to be his enemy. You get the feeling he'd die sooner than let you get away scot-free."

            e "So the scarf has no issues that stand out to you?"
            "Rahim blinks, suddenly realizing he's been distracted from something tailoring related."
            r "Oh, at surface level it certainly seems so."
            "Surface level isn't good enough for you at this point, and neither is it for Rahim, apparently. The bull brings the scarf back under his attentive gaze."
            "His expression doesn't shift the entire time he looks at it."
            "The longer he spends, checking different angles and prodding seams, the more anxious you get."
            "Did you make a mistake with the weft? Maybe one of the adornments is lopsided?"
            "After what feels like an eternity, the bull looks up at you."
            r "The actual quality of your tailoring is quite high."
            r "Any improvements at this stage will be difficult to achieve, and are ones you most likely already identified."
            r "In case you haven't, the main thing you have to worry about is planning ahead as you work. I see spots where you had to change the distance between each stitch to account for an unexpected lack of space."
            r "Despite this being nearly irrelevant to the commissions I've given you before, the main thing you have left to improve upon is design."
            "You tilt your head, questioning, and a bit hurt."
            e "I thought the design was good?"
            "Rahim grimaces slightly."
            r "I said it was passionate. It is flawed to say the least."
            r "It is good for a first attempt."
            "He's being gentle about it, but it still hurts like a knife to the guts."
            e "I understand. What is it that most needs working on?"
            r "Color theory."
            "Rahim points at a patch of bright blue, a snowflake you patterned in against a blood red background."
            r "Discarding the issue of a snowflake being an odd choice for for the Summer, you generally want to have contrasting or similar colors together."
            r "Without something to balance or add further contrast, these two are just in between contrast and similarity."
            r "It looks bad."
            "Ouch. This wasn't what you expected to hear when you came here."
            r "I tell you this not to be cruel, but to see you improve."
            r "You've consistently listened to my instructions, I think you'd prefer honesty over mercy."
            "He could still be nicer about it."
            e "Y-yeah. I understand."
            e "Different is good, so is similar. Anything in between is bad unless it has something to balance."
            "Rahim gives you a nod."
            r "Precisely."
            e "Where did you learn design from anyway? Rayleigh?"
            r "It feels a bit like you're trying to escape further criticism, but I was just about done."
            r "I'll tell you the story - it is the same one you were looking for earlier, the group that taught me the most."
            "Rahim gestures for you to sit down, giving you a good angle to watch him sew as he tells you the story. He hasn't started, but he's preparing the materials."
            r "You already know the group that taught me, but they wouldn't come to mind when one thinks of good tailoring."
            r "At least, anymore."
            "Rahim picks up his needle and thread, and begins to weave the story."
            r "When I first came to Lusterfield, I did so as an adventurer."
            r "I fully intended to stay here only a few days, helping a few folks here and there, learning a little, and continuing my travels."
            "The bull heaves a sigh, his hand tentatively weaving the cloth, struggling to externalize something stored deep in himself, complicating it by thinking about, rather than experiencing it."
            "It's like you can see his mind clicking pieces together, putting himself in the shoes of a self long past."
            r "It was only when I met the goat tribe that my journey was halted."
            r "Never before had I seen cloth so beautifully textured, so vividly colored."
            "He looks at you and snorts dismissively."
            r "Don't even bother thinking about what they wear now. Only echoes of past glory remain in that place."
            e "What they wear isn't exactly... complex, but the colors are still vivid, I'd say?"
            "Rahim gives a grudging nod."
            r "They have access to the same materials, and remember how to use them."
            r "Blue, at least. I haven't seen them recently enough to know if they've kept the other colors."
            e "But, I wouldn't think of you as all that old...? How fast did all of this disappear?"
            "The bull grimaces."
            r "A matter of years, though her techniques are still around. I {i}do{/i} still remember them, even if they don't."
            "The two of you are briefly quiet as you process what he said, and he reaches for a new color to sew with."
            e "Who was the, umm, the woman in the goat tribe you learned from?"
            "Rahim blinks twice, as if suddenly remembering something."
            r "I forgot you weren't here for that, sorry."
            r "The goats' greatest - and only - tailor was a grizzled old water buffalo by the time I met her."
            e "A mentor to you?"
            "Rahim's face is in an expression you've seen only a few times before, a melancholy reserved mainly for when he spoke of his daughter."
            r "As much as a master can be a mentor to an experienced tailor. I haven't met a better tailor to this day, and I don't think I ever will."
            "You chuckle lightly, trying to break the heavy mood."
            e "You never know, someday I may become that good!"
            "Rahim raises his eyebrows at that, amused. Despite that, there is a piece of him that seems to take you seriously."
            r "If you are serious about tailoring, aim for it. I am close to her level, but I have a ways to go yet. You'll have nothing but respect from me if you manage it."
            if rahim_like > 1:
                "You feel a sudden urge to start tailoring just from hearing that."
            e "So, she was amazing, and incredibly old. I can't meet her, I at least want to know who she was."
            "Rahim slaps you upside the head, careful not to stab himself on your horns, or hit you too hard."
            r "I should kick you out for impatience or impertinence."
            "Your head doesn't quite hurt, but you're just irritated enough to snap back."
            e "And why don't you?"
            r "I don't mind it."
            "Just as you open your mouth to speak, Rahim finishes his sentence."
            r "Within reason of course. I still expect you to treat me with the respect I deserve."
            "You squirm a bit in your seat."
            e "And me? Do I get any respect in return?"
            "Rahim lets out a dark chuckle, a joke at both of your expenses."
            r "You deserve a little. I give you it as you continue to earn it."
            "You grumble a bit under your breath, unsatisfied with that answer."
            r "What was that?"
            e "Nothing."
            "He gives you a look that tells you exactly how much he believes that."
            r "Sure."
            r "If you think I'm demanding, you should have met Larra."
            r "She only used my name after a month of teaching me. Up until then I was just 'that one', or 'the bull over there.'"
            "A shiver goes down your spine. You don't want to think about learning from someone like that."
            "It took you long enough to be able to talk to Rahim without being insulted... too much."
            e "That sounds. Unpleasant?"
            "You quickly correct yourself, not meaning to be so rude."
            e "Not to speak ill of the dead, of course."
            "To your surprise, Rahim only snorts in amusement."
            r "Oh, I wouldn't worry about it, I think she'd take it as a compliment if anything."
            r "She had two pleasures in life: Tailoring, and making people uncomfortable. She excelled in both."
            "You have to bite your tongue to prevent yourself from asking if she taught him both or just tailoring."
            e "And she's the one you learned the most from?"
            "Rahim nods, the piece now identifiable as a sock in his hands nearly finished."
            r "She was stingy with compliments, but not with lessons."
            r "It was her that taught me how to actually {i}design{/i} what I tailored. She's the one that made me look at tailoring as an art form, and not just a profession."
            "It takes a bit for you to phrase the question this raises - Rahim has been quite understanding so far, but you have a feeling you're on thin ice."
            e "But none of the goats picked up her lessons because...?"
            "You don't say any of the reasons you thought of. None of them are particularly favorable."
            "Rahim just rolls his eyes as he sews."
            r "Same reason people didn't pick up mine."
            "He pauses briefly to correct himself."
            r "Probably."
            r "Nobody there or here was interested in tailoring, except for myself and her. Her personality didn't help matters either."
            "There's a pause. You very intentionally stay silent."
            r "Neither does mine, I suppose."

            menu:
                "Now that he's said it, you might as well comment on it."
                "Maybe, but you're admirable just like her":
                    $ rahim_like += 2
                    e "I won't say you're wrong, but from what you're saying, Larra seemed like somebody worthy of admiration and love."
                    e "I'd say the same of you."
                    "Rahim freezes in his tailoring. You're pretty sure he's stopped breathing. It takes only a few moments for him to recover, but the bull's expression remains strained."
                    r "I had my chance at that."
                    r "That you believe I do may be because you weren't here to see what I lost."
                    e "..."
                    e "I can't tell you if that's true or not for sure - I wasn't there, and I will never have been there. We'll never know."
                    "You take a deep breath before you continue. It is a difficult sentence, and one that cannot be botched."
                    e "But the bull I've met since coming here."
                    if rahim_like > 1:
                        "Taking a risk, you reach out and tap his chest gently."
                    e "He deserves it. If not from everyone, then from me at least."
                    "Said bull turns to you, looking completely bewildered."
                    r "Where is this coming from? I'm a good tailor, and maybe even a good teacher, but I'm otherwise just a grouchy old bull."
                    "It's your turn to look at him confused."
                    e "Those are fairly admirable things? Except for the bad temper, which I don't really mind."
                    "Rahim's face goes from confusion to outright suspicion."
                    e "...that much. It can be a bit rough to deal with, but I've learned it's just part of who you are."
                    r "That's still not exactly admirable, but I'll concede the point considering I admire Larra to this day."
                    r "Even if she was, as the old chieftain phrased it 'a crotchety old bitch.'"
                    "That's good enough for you. The man really needs to learn how to accept a compliment."
                    r "I appreciate the sentiment. Even if we disagree, it's... nice to know someone like you thinks that of me."
                    "You can't help but smile. Even if he didn't mean to, that was the best compliment he'd given tonight."
                    r "Don't think I'm going to go any easier on you just because you said a couple of nice words, though."
                    "Alas, he couldn't let you get away without at least a drop of negativity."
                    if rahim_like > 1:
                        "Even so, you can't seem to help but like him."
                "That's true, but I'm used to it, like you probably were":

                    e "Yes, it definitely doesn't help, but I'm used to it."
                    "The bull raises an eyebrow at that."
                    e "Just like you got used to Larra's bad temper, I've gotten used to yours."
                    "All you get is a light shrug - limited in scope to not interrupt his sewing."
                    r "Fair enough. But just like her, I'm probably going to wind up dying only having taught one person."
                    e "I think you might be getting ahead of yourself there, but it's definitely a possibility."
                    "A sardonic smile splays across your lips."
                    e "It seems only us adventurers have the patience for each other."
                    "Rahim snorts lightly."
                    r "Larra wasn't an adventurer, but yes. It is an interesting chain of inheritance."
            "The conversation sort of falls flat after that."
            "Rahim sews, nearly having completed his project, while you sit there silently, twiddling your thumbs."
            "Unable to think of anything else to ask, you finally broach that most uncomfortable of questions."
            e "So, what happened to her?"
            "The bull flinches, accidentally piercing himself with the needle. The cut is small enough not to need medical attention, but you can tell it hurts."
            "He continues as if nothing happened."
            r "She was on the cart the day the war started."
            "Oh."
            "This time, silence really {i}does{/i} fall, and you wouldn't be the one to break it even if you had to spend the next three hours here."
            "Luckily, Rahim breaks the silence after only five minutes, his sock laying finished in his hands."
            "He does not look as satisfied as you thought he would."
            r "I believe it would be best if you went home for now."
            "A pang of discomfort surges through you as you hear just how tired he sounds."
            r "As far as I'm concerned, our deal is still on, and I didn't give you much of a story this time around."
            "He slides a small pile of gold your way."
            r "I tried to compensate a bit with the reward. Hopefully it should be more than equal to its worth in stories."
            r "I truly do not understand why you wish to hear them."
            "You open your mouth to say something, but realize that now isn't the time. He can't hear you - his eyes are looking at something that isn't there."
            "Quietly, you pick up the 100 Gold Coins and store them in your pouch."
            "There is nothing you can say to the man that lost his mentor and friend, daughter, and wife to a war he is still trapped in."
            "All you can do is mumble a brief 'Thank you.' and head out."
        else:

            e "I finished the scarf."
            "You present your work to the bull, who gives it a cursory glance before accepting it."
            r "It's of acceptable quality."
            r "Here, your reward."
            "Rahim pours 100 Gold into your hands."
            e "Thank you. It's much appreciated."
            "The bull grunts at that, turning to some unidentifiable clothing he's working on."
            r "You'll get compensated for as much as your work is worth. Nothing to thank me for."
            "You're about to accept that and leave, but pause as you step out."
            e "What about your profit margin?"
            "Rahim gives you a skeptical look."
            r "Mine to worry about. Don't worry, it's more than made, if it even matters."
            "He doesn't seem very happy that you're digging into this. You should probably leave."
            e "Alright, well. Farewell, Rahim."
            "Rahim gives you a terse nod, and nothing more."
    else:

        e "Rahim, I finished the Scarf!"
        "Rahim says nothing. He just looks straight into your eyes from his seat, and stares at you."
        e "Rahim?"
        "Rahim's glare only grows harsher in response to your attempt to call out to him."
        e "I guess I should come back when it's all properly done?"
        r "Yes. Do not try to lie to me again. It reflects poorly upon my decision to trust you."
        "Rahim continues to stare into your soul."
        "You take this as a sign that you should leave now."
        jump main_rahimshop

    $ pc.gold += 100

    if pc.armor["Mask"] != None:
        if pc.armor["Mask"].img == "Long Scarf":
            $ pc.armor["Mask"] = None
        else:
            $ removeItem("Long Scarf", inventory, 1)
    else:
        $ removeItem("Long Scarf", inventory, 1)
    $ TaskFinish(task04)

    jump main_rahimshop


label Rahim_Yarn_Quest_02:
    $ TaskBegin(task04)
    if rahim_yarn == 1:
        e "I think I'm ready to take on another commission, Rahim!"
        "Rahim snorts."
        r "Good. I've got a project set aside for you, since you mentioned having interest in doing this again."
        "He reaches behind him and grabs a couple bolts of cloth, as well as a loop of thin metal wire."
        r "You'll need that enthusiasm for this one - you're making my least favorite, hats."
        "You look at him slightly confused."
        e "Your least favorite thing is... hats?"
        "Rahim nods, dead serious."
        r "Yes. They're the farthest thing away from normal clothing as I can get, and I have to buy a specific size of metal loop with each commission..."
        r "It's a huge hassle."
        "And he's making you do it."
        r "I see that look on your face."
        r "I did give you the worst thing in here to do, but I did also do the most annoying part for you already."
        "He hands the materials your way."
        r "This isn't everything you need, by the way. Just the hardest stuff. Here's the list of everything else you'll need."
        "You sigh, looking down the list of ingredients... yarn, feather, wire... These are all a bit out of the way."
        e "Alright, I guess I should get to it."
        r "That's the spirit."
        r "Tell me when you're done so I can inspect your work and give you your payment."
        "You nod, and head out."
    else:
        e "Can I do another commission?"
        r "...sure."
        "He reaches behind him and grabs a couple bolts of cloth, as well as a loop of thin metal wire."
        r "Here. I was recently asked to make a hat."
        r "I do not like making hats."
        r "It's not a high profile commission, so I don't have to worry about your quality."
        e "...My work isn't that bad."
        "Rahim nods."
        r "It's not. But it also isn't good enough for anything beyond functionality."
        "Ouch. that hurt to hear."
        r "You'll need to grab metal hoop, some yarn, and feather in addition to the materials I'm giving you."
        r "I'll pay you when you finish."
        "You nod, grabbing the materials Rahim hands your way."
        e "Okay. I'll come back when I'm done."
        "You get a grunt in return. The conversation is over, it seems."
    $ addItem("Metal Hoop", inventory, 1)
    $ discoveredrecipe.append(flatbonnetrecipe)
    jump main_rahimshop

label Rahim_Report_Yarn_Quest_02:
    if callInventoryItem("Flat Bonnet", "Mask"):
        e "Rahim, I finished the hat!"
        "Rahim says nothing. He just looks straight into your eyes from his seat, and stares at you."
        e "Rahim?"
        "Rahim's glare only grows harsher in response to your attempt to call out to him."
        e "I guess I should come back when it's all properly done?"
        r "Yes. Do not try to lie to me again. It reflects poorly upon my decision to trust you."
        "Rahim continues to stare into your soul."
        "You take this as a sign that you should leave now."
        jump Rahim_Normal_Talk
    $ TaskFinish(task04)
    if rahim_yarn == 0:
        e "I finished."
        "You hand the hat over to Rahim."
        r "Mm. About as good as I expected."
        r "Here. Your commission."
        "Rahim pours 50 gold into your hands."
        r "I'll have more work for you later."
        e "Sounds good to me."
        r "Mm."
        "Silence stretches out between the two of you."
        e "Alright. I'll see you later then, I guess."
        "All you get is another grunt."
        $ pc.gold += 50
        jump main_lusterfield02
    else:

        e "Alright, Rahim. I think I'm just about done."
        "Rahim looks at you appraisingly."
        r "Faster than I expected. Give me a moment to look over it."
        "You put the hat in Rahim's hands, who promptly takes it under his lamp for closer inspection."
        "He turns it this way and that, flipping it repeatedly."
        r "Okay, you have some extra pieces of material hidden in a couple of spots here. It's a clever solution to an avoidable problem you faced."
        "Ah. He noticed how you sort of had to trim and tuck some of the cloth and interfacing you made within the folds."
        r "This was almost certainly caused by you failing to align the pattern pieces with the fold when you first started cutting."
        r "The solution almost makes it seem like you just added some extra interfacing on the edges, but the unevenness of it gives it away."
        "That... yeah. He's absolutely right on the sequence of events. He's also right about what he's clearly implying you need to do next time."
        r "Of course, this is still higher quality than the person needed - it is far above the craft of an amateur, but far below that of a professional."
        "Rahim mutters to himself."
        r "...well, any professional worthy of the title."
        r "You know what to do for next time, yes?"
        "You nod."
        e "Yes."
        r "Good. As long as you learn from your mistakes."
        e "I do my best to."
        "A shadow of a grin flickers across Rahim's face."
        r "A rarity for this town."
        "He reaches into his belt for your payment."
        r "Here, for a job well done."
        $ pc.gold+= 50
        "You receive 50 gold from Rahim."
        e "Thank you, Rahim. It sort of feels like a lot of money to give me for that, but I appreciate it all the same."
        "Rahim snorts."
        r "You gathered materials, made it into cloth, and then made the hat. That is worth a lot of money."
        "He seems to be in a good mood, so I might as well go for a joke."
        e "So it wasn't due to the high quality of the craft?"
        "Rahim laughs, before slapping you on the back."
        r "No, [e]. It is pretty good, but not good enough to warrant a price increase."
        r "I believe I owe you a story however."
        e "You do. I was wondering how you even got to start adventuring in the first place?"
        "Rahim looks mildly entertained."
        r "You had asked for something else the other day."
        e "Oh. I did?"
        r "Yes, but I'll just tell you about how I started, instead."
        "Once again, Rahim picks a project to work on while he talks to you."
        "This time it seems to be a half finished scarf?"
        r "I grew up in a small town. Smaller than this one."
        r "My father was the town's tailor - that is to say, as with most tailors in places that small, he was a farmer that knew how to sew moderately well."
        e "I assume you learned how to sew from him?"
        "A small snort from Rahim."
        r "Something like that. I learned how to repair clothes while I lived with him."
        r "All of my actual skill as a tailor was gained on my adventures."
        "You nod, remembering that he said something similar last time."
        e "Yes. Learning as you traveled was what you decided on."
        r "Well, back then, I was only 14. I didn't know what my goals were."
        r "There wasn't much to be done about that, because there was nothing for me to look at or aspire to - I was completely isolated in that rinkydink place."
        r "That was, until Rayleigh stopped by."
        r "He was an old man, gruff, calloused, and cynical to his core. Much like me today, I suppose."
        r "He needed a bodyguard - someone young that could protect him from the monsters that roamed the roads."
        r "We had nobody like that in town. Right as he was about to give up, I asked if I could join him."
        r "One of my greatest regrets is that I never told my father I was going to do that... I hated the man, but no father deserves that."
        r "...well, at least, he didn't. He was bad, but not truly evil"
        r "Regardless, he accepted, saying that he could at least train me into something half-decent due to my young age."
        e "And that's how you started?"
        r "Yes, that's how I started. I wasn't truly an adventurer of course, but I had essentially started an apprenticeship."
        r "I later learned that the old bastard was an ex-adventurer, one that made his money killing and cleaning monsters, taking all of their valuable parts, and making them into things."
        r "He tried to teach me leatherworking, bonecraft, alchemy... but the only thing that really stuck was tailoring."
        e "He sounds like a pretty good teacher, but... You sound like you don't remember him fondly?"
        "Rahim snorts, waving his hand at you."
        r "Oh, I remember him fondly enough, considering what he did to me."
        r "The man taught me to fight by throwing me at monsters and yelling what I should do."
        r "Do you know how injured I got when he threw me at a full grown wolf with nothing but a dagger the first day?"
        "Rahim grimaces slightly, if more out of habit than anything, reaching for a small scar on the back of his shoulder."
        r "But, I do owe him everything."
        r "Without him, I would not have become an adventurer, or a tailor."
        r "I would have died in that small town, killed by boredom or something."
        e "So all the pain and suffering was worth it?"
        "Rahim goes silent for a bit."
        r "For me, yes."
        r "I was a weak and stupid bull back then. I would be disgusted by myself if I stayed like that for my whole life."
        e "And me? I'm just starting out, like you... do you think I'm quite that bad?"
        "Rahim fixes you with a level glare."
        r "Sounds like you're fishing for compliments."
        r "No, you're not that stupid, or weak, but you definitely have your shortcomings."
        r "If you learn, you may grow. The ability to change is all one needs in life."
        "Rahim's voice betrayed no deep love or care, but... it seems he respects you more than most, if only by a bit."
        "Definitely an improvement over when you first came here."
        "You sit in silence as Rahim continues sewing."
        e "Is that the story?"
        r "Unless you have any pressing questions, yes."
        e "Alright, well. Thank you."
        "You get up to go, heading for the door. As you put your hand on the doorknob, you hear Rahim speak up."
        r "I may have been a bit rough with you before. Speaking about Rayleigh makes me a bit irritated."
        "You hear the bull sigh in slight annoyance. When you turn your head, he is looking you in the eyes."
        r "I think you are doing well [e]. I believe you have a bright future ahead of you, if you continue on this path."
        "Just as suddenly as that came out, Rahim has turned back to sewing."
        "What a weird guy."
    if pc.armor["Mask"] != None:
        if pc.armor["Mask"].img == "Flat Bonnet":
            $ pc.armor["Mask"] = None
        else:
            $ removeItem("Flat Bonnet", inventory, 1)
    else:
        $ removeItem("Flat Bonnet", inventory, 1)
    e "...Thanks, Rahim."
    "All you get in response is a grunt."
    "With nothing else to say or do, you walk out of the door, and into the streets of Lusterfield."
    jump main_lusterfield02


label Rahim_Flower_Quest_Finish:
    e "Rahim, I got the mums for you."
    "For a moment, you swear you could see a smile on Rahim's face."
    "But it disappears quickly."
    "Rahim takes the flowers from you."
    r "Thanks."
    "He grunts as he passes you 75 gold."
    $ pc.gold += 75
    "He looks at the flowers and his expression dims."
    r "..."
    e "Is there anything wrong, Rahim?"
    "Rahim looks at you with temporary blankness."
    "Then, he snaps back to attention."
    r "No. It's the flowers..."
    e "Did I get the wrong ones? I'm sorry."
    r "No. They're my daughter's favorite flowers."
    r "Today is her death anniversary."
    "Rahim's tough shell breaks a little."
    r "That's why I sent you to get these."
    r "I'll bring them to her later. She'll love these."
    e "I'm sorry."
    r "Why should you be?"
    "Rahim's grip on the flowers tightened."
    r "You're not the reason why she's not with us anymore."
    "Rage radiates off Rahim."
    "He's about to break the chrysanthemums you've picked."
    "Looking at the mums, Rahim slowly calms down."
    r "I'm not sure how are you getting on with the goats but remember this."
    r "They've slaughtered some of us mercilessly."
    "You get closer to Rahim and put your hand on his palm, and he looks away."
    "You decide to stay silent for the moment."
    "For a few minutes, both of you didn't move. Only a brief whistling of the wind can be heard through the shop."
    "You stares at Rahim, he is still holding onto the chrysanthemums tightly, and holding back the tear from his eyes."
    "Rahim sniffs and looks back at you."
    r "I can't move on."
    "The bull flings your hand away, and resume to his work with the clothes."
    "You stares at the working bull. He is already back at focusing on the thin threads."
    "And the chrysanthemums were left on the table."
    "His response left you disappointed... but when you stare at his eyes. You noticed that something has changed."
    "Maybe it's the anger inside him, maybe it's the grieve and regret."
    "You can't decide if it's for the better or worse, but there's a sliver of hope you still hold onto for him."
    $ QuestFinish(quest19)
    jump main_rahimshop

label Rahim_Flower_Quest_Begin:
    e "Hey, Rahim, is there anything you need?"
    r "I hear that you're getting chummy with the goats."
    "Rahim levels you with a disapproving gaze."
    "You feel cowed."
    e "Erm... Not technically... It's more like they tolerate my presence as a courier."
    "Rahim nods pensively. After some time, he continues."
    r "Lusterfield was once close to the goats too... And see where it got us."
    "There is a hint of melancholy and sadness in Rahim's voice."
    "You do not know how to respond. Thankfully, Rahim picks up the thread of conversation."
    r "Look behind your back when you're around them."
    e "I don't think they..."
    r "You were not here."
    "Rahim huffs."
    r "That's beside the point. Sorry for being emotional. I need something from you."
    "You're glad for the topic change. You had a feeling Rahim was close to exploding earlier."
    e "What do you need, Rahim?"
    r "I need you to go to the outpost near the goat tribe to collect 4 bunches of chrysanthemum for me."
    "You are confused."
    e "Chrysanthemum? Why?"
    if quest08.status == True:
        e "Sounds like I've heard it somewhere..."
    r "I need it for a garment."
    "Rahim grunts but you have a feeling there's more to this."
    e "But aren't there flowers around Lusterfield?"
    r "This one only grows near the goats."
    r "I'm not sending any other Lusterfolks to go there lest I put them in danger. So you're the perfect candidate."
    e "Okay..."
    r "If you run into any goats, just tell them you're foraging. Now, get going."
    $ QuestBegin(quest19)
    $ quest19.qProgress(__("Collect 4 chrysanthemums from the Outpost"), "Chrysanthemum", 4)
    jump main_rahimshop

label Rahim_Ask_Opinion_Goat_Tribe:
    $ opinions_GoatTribe[2] = 1
    e "Hey, Rahim... Would you want to talk more about... the letter?"
    r "I'm busy."
    e "Uh... How about... Goat Tribe in general?"
    r "..."
    r "Look, boy. You need to stop snooping in other people's business-"
    r "I said no. Then it's a no. Got me?"
    e "Ok, Rahim. You don't need to be... this grumpy."
    r "You want to get into my nerves or what?"
    r "...Just leave the village be, life is simpler this way."
    e "...A-alright, I guess... I'm sorry to bother you, Rahim."
    r "You just don't understand... You all..."
    r "Cherish the peace you have now."
    e "I understand."
    jump Rahim_Normal_Talk

label Rahim_Yarn_Quest_01:
    $ clothing = "Sweater"
    e "So, Rahim...?"
    r "Yes, [e]?"
    e "I know you are always busy, so... I was wondering if you had anything I could help with?"
    e "I don't know... making some orders for you or something?"
    "Rahim snorts, a gruff sound somewhere between derision and appreciation."
    r "I appreciate the thought, [e], but as if I could trust you with making the clothes my business produces."
    r "People see me as the best tailor for miles and miles around, and they expect that quality when they order from me."
    e "...Well, I still want to help. Maybe I can't deal with the high profile clients, but..."
    e "Maybe some of the more mundane orders?"
    "Rahim takes a moment to think about your proposition."
    r "I've seen you make a few things in here before."
    r "They were of acceptable quality, so I will let you complete some of my orders."
    "Rahim suddenly looks at you with cutting intensity, as if staring into your soul."
    r "If I see you try anything funny, however, you will not be welcome back in this shop."
    e "Hehe, well... I want to think you can trust me not to betray you like that."
    "Rahim sighs."
    r "Maybe, but it was worth saying anyways."
    e "I understand. Courier, adventurer, or tailor, you have to be careful about who you trust."
    "The bull looks at you flatly."
    r "Yes."
    r "Trust may not be as critical as back when I was out adventuring, where trusting the wrong person could end with you bleeding out in the middle of the woods with no coin purse..."
    "You are suddenly aware of how tightly Rahim is gripping the scissors in his hands."
    r "It is still important here."
    "You gulp. There has to be some way to change the subject away from the possibility of you betraying him."
    e "I remember you told me a bit about having traveled."
    e "Could you tell me a bit about your adventures?"
    "Rahim's ear flicks, seemingly flummoxed by your question."
    r "...I have not spoken about them in quite some time, but..."
    r "If you do a good job with the clothing, then perhaps."
    e "I'm interested in what such a big, strong bull got up to in his youth."
    "Rahim gives you an irritated glare."
    "It seems he did not like what you were implying there."
    r "I am going to act like I didn't hear that."
    "That's probably for the best."
    r "I need you to make [clothing]."
    r "It's a rather simple recipe, requiring only... some yarns, and pelts... and others."
    r "If you need to remember what you need at any point, I wrote the task and recipe down for you."
    e "Okay. Thank you, Rahim!"
    r "No need to thank me. I am just making sure I get what I asked for."
    r "I'll make sure you get a cut of the sale should it be of good quality."
    e "Sounds good to me. I'll get on it now!"
    r "Good. This isn't an emergency commission, but get it done as soon as you can."
    r "Speak to me again when you've made the product."
    "And with that, Rahim returned to his work, signaling the end of the conversation."
    $ TaskBegin(task04)
    $ discoveredrecipe.append(yarnrecipe)
    $ discoveredrecipe.append(sweaterrecipe)

    jump Rahim_Normal_Talk

label Rahim_Report_Yarn_Quest_01:
    if callInventoryItem("Sweater", "Clothes"):
        e "Rahim, I finished the [clothing]!"
        "Rahim says nothing. He just looks straight into your eyes from his seat, and stares at you."
        e "Rahim?"
        "Rahim's glare only grows harsher in response to your attempt to call out to him."
        e "I guess I should come back when it's all properly done?"
        r "Yes. Do not try to lie to me again. It reflects poorly upon my decision to trust you."
        "Rahim continues to stare into your soul."
        "You take this as a sign that you should leave now."
        jump Rahim_Normal_Talk
    else:
        e "Hello Rahim! I have finished with the [clothing]!"
        "Rahim looks at you appraisingly."
        r "I saw you working on it here, but it is good to see it finished so soon."
        r "Please, hand it here so I may review your work."
        "You hand Rahim the [clothing]."
        r "Hrmm... This is mostly good, but you left a few loose ends in these two spots."
        "Rahim points at a couple loose seams that you seem not to have noticed."
        e "I'm so sorry! I can fix it at once if you need!"
        "Rahim motions for you to calm down."
        r "It's okay. This would be difficult for you to fix regardless."
        r "Here, have this, for working diligently."
        "Rahim reaches into his pouch, and drops 50 gold in your hand."
        $ pc.gold += 50
        if pc.armor["Clothes"] != None:
            if pc.armor["Clothes"].img == "Sweater":
                $ pc.armor["Clothes"] = None
            else:
                $ removeItem("Sweater", inventory, 1)
        else:
            $ removeItem("Sweater", inventory, 1)
        $ TaskFinish(task04)
    menu:
        r "If you wish to stay, I can teach you how to avoid this next time, and tell you that story you asked for."
        "Stay":
            $ rahim_yarn = 1
            e "I would love to!"
            e "As I said before, I want to hear all about what a-"
            "Rahim cuts you off with a look."
            "However, you can see he's doing his best to keep a straight face, clearly entertained by your unabashed attempts at flirting with him."
            e "W-what I was going to say was, what an exemplary figure like yourself did when he was younger!"
            "Rahim's look shifts into one of amused skepticism."
            r "Mm. Well. You will hear all about them in a second."
            r "First we need to talk about how to avoid making loose ends in clothes you tailor. I expect you to do better next time."
            r "To be clear, you did better than I expected. This is fairly passable."
            "He says this not unkindly. Knowing Rahim, this is most likely high praise."
            r "Here, look."
            "Rahim reaches over to the [clothing], smooths it out, and brings the faulty stitches under the brightest spot on his desk."
            r "These might seem like small mistakes, but over time..."
            "He pulls on one of the loose strings, and you see how your work begins to unravel."
            r "It compromises the piece's structural integrity."
            e "Piece?"
            r "Yes, piece. Every single item I tailor has its unique requirements and touches, so calling them by their eventual purpose is inaccurate considering their deviations."
            "Rahim said this with an entirely straight face, but as he turns back to the [clothing] you see a faint glimmer of pride in his eyes."
            r "Regardless, to avoid this, one must make sure to plan out each individual stitch as they go along."
            r "Failing to do so may lead to slanted lines, poorly anchored or uneven stitches, or loose ends."
            "It is interesting to watch Rahim as he talks about this."
            "His normally reserved nature fades like a fall breeze, bringing with it his true personality."
            "A diligent, passionate, and proud bull, unerringly attentive to what is important to him."
            r "To summarize everything I've said, just remember to cut and knot loose ends, and measure precisely."
            "Oh god, you stopped paying attention to what he was saying."
            e "Got it! I'm going to make sure to do that next time I tailor something!"
            "Rahim fixes you with a knowing look."
            r "I know you missed half of that, going by how your eyes glazed over partway through."
            e "I'm sorry Ra-"
            r "It's okay."
            "Rahim chuckles a bit and smacks you lightly on the shoulder."
            r "You'll get the lessons drilled into you the next few times we have this talk."
            "Wait... what?"
            e "N-next time?"
            r "Oh. Yes. We had not agreed on that. I had just assumed, apologies..."
            "Rahim trails off, looking for the right words. He seems a bit embarrassed."
            r "You were right that it was useful to have a helping hand to reduce my workload a bit."
            r "And... I don't mind teaching you. Not like there's anybody else in town who wants to learn."
            r "Point is, I will be offering more tasks like this in the future if you are willing to take them."
            "Well, it's good to know that, at least."
            r "Regardless. I owe you a story, and it's about time I got to it."
            "Despite saying this, Rahim has only slightly turned your way, pulling out a new piece to work on."
            "It seems like he will work while explaining this to you. Perhaps it helps him think?"
            pause 1
            r "Many years ago, I couldn't tell you precisely how many, one of my adventures took me to the."
            "Rahim pauses."
            r "You have never been to the capital, correct, [e]?"
            "Surprised to be called on, you jump a little bit in your chair."
            e "N-no. I've never been! What's it like?"
            "Rahim hums to himself in thought, continuing his tailoring work all the while."
            r "It's a place of many faces."
            r "Some streets are grand, towering marble structures laced with runework on every side..."
            r "Others are... squalid. The scent of death and sewage in the air, slimes living just beneath the surface, roaming out and eating what has been left out at night."
            e "Oh..."
            "Rahim snorts gently, pulling his needle up through the fabric."
            r "Quite."
            r "Awe-inspiring the capital might be, but it is not kind to all of its people."
            r "I hope Lusterfield never becomes like that."
            r "It should be a place to welcome anyone with open arms, a warm plate of food, and a bed to sleep in at night."
            "Sure, unless they're a goat."
            "But you leave that one to yourself."
            e "I still remember what everyone did for me when I first arrived."
            e "...I'm thankful for it to this day."
            "Rahim lets out a satisfied rumble."
            r "And look how you have paid us back for it so far."
            r "Regardless, I digress."
            r "My trip to the capital was not one done on purpose."
            r "I spent most of my early adventuring days wandering aimlessly, helping people however I could, wherever I went."
            e "Sounds pretty noble to me."
            "Rahim snorts."
            r "Sure. Something like that."
            r "I think I was more interested in the food it got in my belly at the time."
            r "..."
            r "As I was saying. Didn't get there on purpose."
            r "I went over as the guard for a caravan I'd found under attack by giant spiders."
            "Rahim flicks one eye your way."
            r "If you ever encounter them, aim for the joint connecting their head and body plates."
            r "I didn't know that at the time, so I stabbed one in the back, and got sprayed with an... unfortunate amount of acid."
            r "Needless to say, I needed new clothes by the end of it."
            "You try imagining a younger Rahim covered in sweat from killing several giant monsters, clothes riddled with holes... things peeking out..."
            "Your head hits the table somewhat hard as Rahim smacks you upside the head."
            r "That wasn't why I mentioned that."
            "If you didn't know better, you'd think the big guy was snickering. You're not though. Your head hurts."
            r "Point is, I had to get myself some new clothes before I got to the capital, and... all I had was some dyes and spiderwebs left by the giant bastards."
            e "I take it you already knew how to sew by that point?"
            r "Somewhat. I got better later, but by that point I'd learned some of the more important tricks of the trade."
            r "When I arrived at the capital, I had a full spiderweb-silk suit, dyed black and light green, a pattern stolen from the spiders themselves."
            r "All of this to say that I made quite the splash when I got there."
            r "People really liked the look, and I started to get commission after commission, until finally, I was given one by the king himself."
            r "It would be many years before I would become his personal tailor, but..."
            r "That success is what gave me the gold to truly go wherever I wanted, and set me on the path of becoming a tailor in addition to an adventurer."
            e "...but you would still go on adventures despite being a tailor?"
            "While you were listening, Rahim got most of the way through the clothing he was making."
            "It is a pale white dress shirt with bright green accents on the shoulders and hems."
            r "Yes. I originally traveled just to see the world, but..."
            r "After that I began to stay at every place I visited for a short while, and learn from that place's tailor."
            r "Learning from all of those different people is what really let me blossom into the tailor I am today."
            r "But those are stories for another time."
            "You cock an eyebrow."
            e "I take it next time is the next few times I help you with the clothes?"
            r "Mm. We made a deal, so if you wish to continue it, I do not mind sharing more."
            e "Alright."
            r "Not sure if that was what you wanted, but. There's the story."
            e "...No, that was nice to listen to."
            r "Mm."
            r "Well, that's all I have to say for now."
            "He is making it pretty clear that it's time to leave now."
            e "Well, I'm happy to hear more next time, if you're willing."
            r "Mm."
            r "Next time."
            "Taking the hint, you step outside."
        "Leave":


            $ rahim_yarn = 0
            e "I have other things to do. Plus, I am a courier, and not a tailor."
            e "Thank you for the offer, however!"
            "Rahim grunts, and shoos you with his hand, already picking over the strands with a needle."
            r "Well, off with you then. If you are busy, you should get to that."
            "There's no reason for you to stick around here, so... you leave."
    jump Rahim_Normal_Talk

label Rahim_Letter_Furkan:
    e "Hello, Rahim. I've gotten a letter from Furkan."
    r "What?"
    e "Uhh... A letter from Furkan from the Goat Tribe."
    r "Why?"
    e "He wanted to propose a Truce. For Lusterfield and the Goat Tribe."
    r "Let me see the letter."
    "You hand the letter to Rahim, he yanks it away immediately, you have never seen him being this urged. He put on his reading glasses and begin skimming through the letter."
    r "'Deer-... Dear Rahim, I am writing this letter to express my sorrow and regret over the past few years. I...'"
    r "'...You could never feel how sorry I am for the battle and I wish if time could go back...'"
    r "'...A sign of peace, let us negotiate in person, we will negotiate in the old place where my father...'"
    r "'...Yours...Furkan...'"
    "You cannot tell if Rahim is holding back his tear, or anger, or frustration. He simply put the paper back in the envelope as soon as he finishes reading."
    r "Duly Noted."
    e "Hmm... Are you sure... Rahim? I thought he was writing the letter as a sign of peace. I think we shou-"
    r "I'm sorry but I don't recall needing your opinion. He wrote the letter to me, I'm saying no."
    e "...Ok. Rahim. Can you at least tell me what's going on."
    r "I'll tell you when the time comes."
    e "... Alright. I'll let him know."
    r "Ahem... I'm sorry about my attitude. There's just a lot of stuff you don't understand yet. I don't want to involve my village in another conflicts."
    e "I understand. Take care, Rahim."
    r "You are good."
    $ quest06.status = 3
    $ quest06.qComp(__("Report to Furkan"))
    jump main_rahimshop

label Rahim_Postal_Training:
    $ QuestBegin(quest03)
    $ quest03.qProgress(__("Craft a Tunic"), "Tunic", 1)
    e "Rahim, did Ole talk to you about my training?"
    r "Yes...?"
    e "..."
    e "Can I get a training from you?"
    r "Okay. I'll keep it simple and quick."
    e "Thanks, Rahim."
    r "You've gone through your bag I presume. You can put on different types of equipment."
    r "Your weapon, your outfit. and accessories."
    r "To make the item you need, just come here and check out the workstations."
    e "Hmm... where is it?"
    r "The sewing machine."
    e "Ah... I see."
    r "You probably already know what crafting is. You need to learn a recipe to make your item."
    r "Hmm... I've got one."
    r "You probably want something to cover your upper part. I can teach you to make tunic."
    e "Hmm... should I cover my upper part?"
    r "Yes."
    e "O-ok. What ingredients do I need?"
    r "Two pieces of cloth. Look I'll give you these. Your task is very simple, just make the tunic and bring it to me."
    e "Thanks Rahim. I'll bring it to you very quickly."
    $ addItem("Small Cloth", inventory, 2)
    jump Rahim_Normal_Talk

label Rahim_Postal_Finish:
    e "Hello, Rahim! I've finished the tunic!"
    r "Let me see."
    if pc.armor["Clothes"] != None or LookForItem("Plain Tunic", inventory):
        if LookForItem("Plain Tunic", inventory) or pc.armor["Clothes"].img == "Plain Tunic":
            r "Hmm... looking good. The sewing is slightly amateur but I can see the effort you put in there."
            e "Thank you...?"
            r "Yeah... Good. Nice. I'll talk to Ole about your performance."
            e "That's really nice. Thanks, Rahim."
            r "No problem, you've been pleasant to talk to. Come here often."
            e "Of course! Thanks again!"
            $ quest01.progress[1].status = True
            $ QuestFinish(quest03)
            jump Rahim_Normal_Talk
        else:
            r "You... don't have the tunic."
            e "Wait..."
            r "Come back and talk to me when it's done. I'm going to do something else."
            e "Ok, I'll be back soon."
            jump Rahim_Normal_Talk
    else:
        r "You... don't have the tunic."
        e "Wait..."
        r "Come back and talk to me when it's done. I'm going to do something else."
        e "Ok, I'll be back soon."
        jump Rahim_Normal_Talk

label Rahim_Ask_Lusterfield_People:
    e "Rahim, what do you think about the people here?"
    r "Meaning?"
    e "Uh... like... what do you know about them?"
    r "Alright, boy. If you wish, I reckon you have met those two in the store."
    r "They sell my clothes elsewhere, so they're good."
    e "Hmm... what do you think of other people?"
    r "You really want to poke around with your nose, [e]. Don't make me scare you, you're gonna hit the wall hard sooner or later."
    r "... that wolf, I don't like him. Lothar. But we talk sometimes."
    e "Ok..."
    r "And just a little advice from an old man, don't ever trust Cane. No matter how good you treat that ruthless rat, he will stab you in the back some day."
    "Rahim continues mumbling some unintelligible words about rats for a few minutes, you stand there, looking at him closely until he snaps back to reality."
    r "...That's it."
    jump Rahim_Ask_Lusterfield

label Rahim_Ask_GoatTribe:
    e "Hey, Rahim. Lothar told me about the Goat Tribe. What happened there?"
    r "Why do you ask?"
    e "I just wanted to know more about them."
    r "That arrogant son of a wolf told you about my stuff, didn't he?"
    e "What? No... He was just talking about how he defeated the Goat Leader."
    r "...If he spills the beans I'm going to sew his mouth shut once and for all. You hear me?"
    e "Yes... I promise he didn't talk about you."
    r "Ok. So what else do you want to know."
    e "Lothar didn't explain very well, but why did the goats came to Lusterfield?"
    r "We used to be... friendly. with them. We have wagons of wares and goods transported between us."
    r "They had a wagon full of wares and people, gone. In the middle of the forest."
    r "They found the remains of their couriers East to our village, near the pond."
    r "They thought it was our doing... It was a long story but the war was planned for a while before it finally broke out."
    r "Those Goat bastards came and destroyed everything we had, we built. At the end, we won. Kind of. But at what cost."
    "Rahim looks around depressively, his hand reaches forward to the walls. You try to console him but it seems he is busy reminiscing the past."
    e "That was horrible. Do you know who actually raided their wagon?"
    r "No... We didn't."
    e "What if they come back again for revenge?"
    r "Then I'll be the first one to kill them all under my blades. I don't care, I just wanted to protect this village."
    e "You still have to look out for your safety, Rahim."
    r "You don't understand. That wolf thinks it's all a game, a fight for glory and a tool to boast about his reputation."
    r "But in the end it's just slaughter. It's them or us. And there will be casualties, always."
    r "If you really wish to go there, be careful. And if not, don't bring them to our village."
    e "Rahim..."
    r "Think about the people living here. I respect that you are going to risk your life, but you are NOT bringing them down with you."
    "Rahim stares at you fiercely, you have never felt this much of hostility before, you feel like he could grab his scissors and stab you at any moment, but he is just sitting there, staring."
    r "Ahem- I'm sorry, I was thinking out loud. Just... stay safe."
    "The bull calms down after a while, he looks away in contempt."
    "Was that just a fleeting lapse of judgement in his mind? You wanted to know what he was thinking, but he keeps backing up on his words."
    e "I will... Thank you Rahim."
    jump Rahim_Ask_Lusterfield

label Rahim_Ask_Tailor:
    e "How long have you been a tailor for the village?"
    r "A few decades, twenty, thirty. I've lost tracks. There was a time I became a personal tailor for the town's king.. Well I still do, remotely."
    r "Time passed so fast, boy. I used to be an ambitious adventurer like you. Going around poking at the other's business."
    r "I settled down someday. Never got out of my job, and that's my life. Just a normal old bull in a normal old village."
    r "And it's all downhill from here."
    e "Rahim... I'll be there if you need me."
    "Rahim ponders, glancing at the floor for a few seconds. He signs and looks around before turning back at you."
    r "You are a helpful boy."
    jump Rahim_Normal_Talk

label Rahim_Ask_Himself:
    e "How is your tailor job here, Rahim?"
    r "Hmm...?"
    r "Good, I'm sewing together a loincloth for a client."
    r "And, a whole yard of requests for stitching up loosen seams."
    r "..."
    r "Which means I'm working."
    e "Alright, Rahim."
    jump Rahim_Normal_Talk

label Rahim_Apron_Fixed:
    e "Hey, Rahim... the apron is fixed."
    r "You should take it to him if you think it's fine... but I can take a look."
    "Rahim raises the apron to your level, almost imagining your body in the apron. He calculates for a few seconds before looking back at you."
    r "Looks really good, the material is almost the same."
    e "Thanks to your recipe, of course!"
    r "Hmm... Yeah there's no problem here, just take it to Cane."
    e "Alrighty, thank you so much Rahim."
    r "You're welcome, [e]."
    jump Rahim_Normal_Talk

label Rahim_Apron_Quest:
    e "Rahim, I have a piece of... apparel, that I think you can help..."
    r "What's it?"
    e "...This one."
    "Rahim looks through your bag and found the tavern apron, his eyes widen, you would have thought that he's going to rip apart the apron once and for all."
    r "Did the bat sent you?"
    e "No, I asked him to take the apron to you... He ripped a hole in there accidentally."
    "You point at the hole on the apron, but Rahim didn't even bother to inspect it. Instead, he stares at you intensely while grasping on the apron."
    r "Why did you help him?"
    e "Look, I was just looking out for you both, he said he's sorry for whatever happened in the past-"
    r "Sorry? Did I mishear? If he said sorry he wouldn't be sending his little precious server here like a coward he is."
    r "If he's sorry then he wouldn't hide in his pathetic tavern for years and years just to avoid seeing me across the road."
    r "It's been 4 years. And I've never heard a sorry from his damn stupid mouth."
    r "He didn't even show up on my daughter's funeral, I don't care if he's guilty or not, is this how a person is supposed to treat his friends?"
    r "..."
    e "Rahim... I- I thought you assumed he helped with the raid of the goat's wagon..."
    r "I don't care if he's guilty or not. It's the goats that attacked our village. We had decades of friendship and memory, but right when I needed my friend the most, he disappeared."
    r "Vanished. Out of thin air. What a good friend. This whole time, I felt betrayed, I lost both people that I loved that day."
    e "I'm so sorry to hear... Rahim. I think he'll certainly be happy to reconcile with you, if you wish."
    r "No, it's too late. Now a single sorry isn't going to be enough."
    r "..."
    "Rahim stares at the hole on the apron, mumbling to himself when suddenly he realises something."
    r "It's Topu, isn't it?"
    e "I'm sorry?"
    r "Was his server the one... that took the deal to help with the raid?"
    e "I don't know, but I believe it wasn't Cane."
    r "Ok."
    "The cold air in this place slowly returns to normal, you glance at Rahim's crossed arms."
    "His shoulder is... not as strained as before, even though he still looks intimidating."
    r "I'm helping you with the Apron. Just know that I'm not doing this for the bat, I'm doing this for you."
    e "Thank you... Rahim. I thought you might tear the apron apart..."
    r "Ha. Maybe later."
    r "Here's the recipe. There are two... actually. You might need to find Ole. He has the dye you would be looking for."
    r "For the other materials, you can find them quite easily if you venture outside, step on some grass."
    r "I suppose the dummy from Lothar has the patches you need."
    r "And Flax, find them near the lagoon."
    e "What about Cashmere, that sounds like a tree."
    r "Mhmm... No. You need to get them from the goat, either ask them or beat a few of them up."
    if quest06.status != True:
        r "I've seen some of the hunters around the ancient tree."
    else:
        r "I don't know where you can find them. But the ancient tree is the best bet."
        r "Something tells me they're plotting... another plan of theirs."
    e "Thanks a lot for the recipe."
    r "No, Thank you for doing all the boring chores, for us folks in the Lusterfield. It's rare to see such an energetic youth for a while."
    r "Apart from the lion, of course."
    e "You are too humble, Rahim. I'll certainly be keeping this in mind."
    r "Good, see you around, [e]."
    $ quest07.status = 3
    $ quest07.qComp(__("Repair the Tavern Apron"))
    if fabricrecipe not in discoveredrecipe:
        $ discoveredrecipe.append(fabricrecipe)
    $ discoveredrecipe.append(apronrecipe)
    jump main_rahimshop

label Rahim_Outfit_Quest:
    e "Hey, Rahim... Everything alright?"
    r "No."
    r "Even though you are not a good tailor, you seem to have a talent in something related to it."
    e "What do you mean?"
    r "The cutting and form of the clothes you made are imperfect, amateur level at most."
    r "But I have many other customers praising how you wear them."
    r "Maybe because your appearance at the tavern has caused quite a buzz."
    e "Thank you, i guess?"
    r "That was not a praise."
    e "O-ok..."
    r "Since you have talent in modelling, I have some professionally-made clothes for you to model."
    r "I made them just to experiment with the pattern and design, with your size in mind."
    e "W-wait... How did you know...?"
    r "I measured your waist when you first came, and I know that apron fit you quite nicely."
    r "Anyways, usually I would judge the quality of the outfit by myself."
    r "But these, they are... not quite what I'd usually create."
    e "That sounds like fun."
    r "No, this is serious. I'll give you some sets of clothes."
    r "And you will wear them and get responses from the townspeople and report back to me."
    r "Do not tear or dirty them or you'll have to pay for them."
    e "Ehm... "
    r "If everything goes well, i might let you keep one of them."
    $ QuestBegin(quest09)
    r "So, this set is for the adventurers in the village. Put this one and see what the folks have to say about it."
    "You excuses yourself to change. The adventurer's armor is very minimal. You blushes."
    e "Isn't this a bit too little protection for adventuring?"
    r "The important parts are covered. And that's what matters to you. Now go and get their opinions and come back."
    $ addItem("Adventurer Leggings", inventory, 1)
    $ addItem("Adventurer Armor", inventory, 1)
    $ quest09.qProgress(__("Put on the Outfit and ask around the Village"))
    jump Rahim_Normal_Talk

label Rahim_Outfit_02:
    $ quest09.status = 3
    e "Rahim. I got the feedback you need. Lothar, Jog and Amble like it. Lothar even wants one for himself."
    "Rahim grunts."
    r "As if he can pay for one. Anyway, well done. Now onto the next set."
    r "This is... for the tavern."
    r "That bat never come to visit but I hear that he has been entertaining more customers since you arrived."
    "For the customers' sake, I've designed a new waiter's outfit. Try it on."
    "Rahim hands you what appears to be a pair of chaps."
    "After you changes, you can't help but feel a little breezy."
    e "Rahim, are you sure this is alright?"
    r "Keep the questions for the townspeople. Since this set is designed with the tavern in mind, you should get the bat's feedback. Don't forget everyone else too."
    $ addItem("Tavern Cloth", inventory, 1)
    $ addItem("Tavern Chaps", inventory, 1)
    $ removeOwnedItem("Adventurer Armor")
    $ removeOwnedItem("Adventurer Leggings")

    $ quest09.qComp(__("Put on the Outfit and ask around the Village"))
    jump Rahim_Normal_Talk

label Rahim_Outfit_03:
    $ quest09.status = 4
    r "That took longer than expected and why are you all flushed?"
    "You open your mouth and you don't quite know how to answer."
    r "No matter. I see that bat hasn't changed at all."
    r "that kid also would react like this whenever he came from the tavern..."
    "Rahim lets the sentence linger."
    r "You should know that the apron belonged to the kid who worked for the bat before he... He was a good kid."
    r "You reminded me a lot of him."
    e "Cane... said that about me... too."
    r "However, you are your own person. I've come to realize that. It's one of the reasons why this piece is created."
    r "The apron is yours because the bat has given it to you."
    r "But you are you."
    "Rahim coughs and turns serious."
    r "I'm sure the tavern has enjoyed that new outfit."
    "Rahim sighs and breathes under his breath."
    r "Just be careful."
    r "...Enough sad talk."
    r "This is an everyday wear. It's quite long so make sure you don't step on it accidentally."
    "You change."
    e "Rahim, I don't see any innerwear. Am I not supposed to wear anything underneath?"
    r "yes."
    e "But..."
    "Rahim cuts you off."
    r "Go off now. Walk around town and get people's reaction."
    $ addItem("Flowy Robe", inventory, 1)
    $ addItem("Flowy Wrap", inventory, 1)
    $ removeOwnedItem("Tavern Cloth")
    $ removeOwnedItem("Tavern Chaps")
    $ quest09.qProgress(__("Put on the Outfit and ask around the Village"))
    jump Rahim_Normal_Talk

label Rahim_Outfit_End:
    e "Rahim, I got the comments for the outfit. Haskell especially likes it."
    r "Haskell? You mean Ole's friend who makes all their potions at the shop?"
    e "Yes. He wears a lot of robes. He said he might visit you to have you make some for him."
    r "Interesting."
    $ removeOwnedItem("Flowy Robe")
    $ removeOwnedItem("Flowy Wrap")
    menu:
        r "Now that you've tried out all three outfits. Which one do you prefer?"
        "Adventurer Outfit":
            $ addItem("Adventurer Leggings", inventory, 1)
            $ addItem("Adventurer Armor", inventory, 1)
            r "Good choice. Take good care of it."
            r "Don't let Lothar pressure you into give you the armor."
            r "He might Lutherfield's hero but he's not getting anything for free."
        "Tavern Outfit":
            $ addItem("Tavern Cloth", inventory, 1)
            $ addItem("Tavern Chaps", inventory, 1)
            r "Not a bad choice."
            r "And... Um... Don't let the bat knows that I'm giving you this for free."
            r "That creep will never stop taking advantage of it if you do."
        "Flowy Outfit":
            $ addItem("Flowy Robe", inventory, 1)
            $ addItem("Flowy Wrap", inventory, 1)
            r "Practical and fashionable."
            r "Thanks for bringing to my attention Haskell's appreciation for this style of clothing. Maybe I shall visit him first."
            r "I also added some tailoring changes with Ole and Sebas's input."
    r "I've added some tailoring changes based on the feedback."
    r "Thanks for treating this seriously. I'm not sure you would. This doesn't normally fall under the job scope of a courier."
    e "No... Thank you Rahim, for letting me try out all of your designs and gifting this one to me."
    r "Hmm..."
    $ QuestFinish(quest09)
    jump main_rahimshop

label Rahim_Reconciliation_Begin:

    r "That's been the final decision for years, Sebas. I am not changing my mind whatever you say."
    "A calm and collected voice emerges from inside the house, who you assume to be the house' owner."
    s "That was YOUR decision, not our village's. Stop living in the past, old bull."
    menu:
        "Should you go in, or continue to eavasdrop from outside?"
        "Get into Rahim's House":
            if isNight():
                scene rahims_house_night
            else:
                scene rahims_house
            r "If you want to go and get kil-"
            "You enter the house, rather casually, pretending you didn't hear anything from them."
            show sebas normal at r1 with dissolve
            s "Hey, there buddy."
            "Sebas' eyes widen as he notices you, waving his hands nervously."
            e "Oh... am I interrupting?"
            s "Nah, not even slightly, we were just chatting. Buddy you should just join in!"
            show rahim normal at l1 with dissolve
            "Rahim crosses his arms, staying on his chair while you find a chair to sit on."
            r "Sebas, anything else you want to know...?"
            s "Oh, well. How about fixing the bridge..."
            r "No."
            show sebas grin
            s "...Between us and the goat tribe."
            "Sebas coughs."
            s "You know, our relationships are like ropes, you can cut them off, but when you put them back in, you pull both ends closer together."
            "It was a weird metaphor, but the way Sebas presents it he doesn't seem to find it odd."
            e "Is that really how it works."
            r "No."
            "He scritches his chins again."
            s "You must know this one. Well, relationships are like stray threads, when it frays. It's our hands that must mend it, weaving... trust, and understanding, back into the fabric."
            r "That's the same thing."
            s "N-no it's not. If you keep those relationship unchecked, they'll unweave and you get a huge hole, in your fabric, but also, your heart. It's a different metaphor."
            r "No."
            s "Relationship is a garden that needs nurturing, forgivness is the fertilizer and magic-"
            r "No."
            s "Relationship is a ship that sails-"
            r "No."
            s "Relat-"
            e "I don't think Rahim is gonna be convinced by you, Seb."
            s "Well, Ole loved these lines from his books, ughhh. Mister Rahim please reconsider your position before I go absolutely insane."
            "Sebas turns to you, with the same pleading eyes he uses on Rahim."
            s "Buddy, don't you also agree that we should keep the peace?"
            e "Well, I've been there lately, so yeah, I agree with Seb."
            "You notice Rahim scoffs at your response."
            r "Goats? I've heard you became their hero overnight. Saving the chief from a cave?"
            e "Well-"
            r "I'm actually not interested."
            r "I'm not going to change my mind, so you two conspirators better give up soon and leave, the door's right ther-."
            "Just as he was about to point at the door, it opens to reveal a familiar figure."
            o "Hey, Rahim, door's not closed."
            r "What is it, Ole."
            o "Someone wants to see you now."
            r "W-who?"
        "Eavesdrop their conversation":

            r "If you want to go and get killed by those treachous goats, so be it. But you're not dragging us with you. There's no way I'm allowing this."
            s "See, I don't even fucking kno-"
            r "Language, kid."
            s "I don't even know why you're so... pressed. It's been years. What happened to Hala, it wasn't even the goat's fault, it was just an accident!"
            r "If you put my daughter's name in your mouth one more time, I'll stitch you up with this needle right here, kid."
            r "How about you stop crying all over the ground and accept what's been reality for years already, I'm not your father."
            r "Go on with your own life, didn't I give all my business to your pawn? Isn't that enough?"
            s "Rahim. You know how much we earn."
            if quest27.status == True:
                s "The most I've earned was from that blue werewolf [e] brought us the other day. And it was... "
                r "[e] brought a werewolf to our village?"
                s "I-I... he doesn't look ferocious. O-Or something."
                s "My point is, only regulars are in the shop, travelling merchant's been getting rar-"
            else:
                s "The shop's been dead, and in a few months it's going away for real."
                r "You're supposed to have the biggest shop in the village, if anything, it's on you. No one else."
                s "There's something else-"
            "Your hand slips, making a loud thumping sound right on the wall, you can feel they pause just to your voice."
            s "What's that sound?"
            "Someone is approaching..."
            menu:
                "There's a small spot right under the window, if you have enough agility, maybe you can hide undetected."
                "Hide under the window":
                    if pc.agi > 10 or (pc.agi > 8 and renpy.random.random() > 0.5):
                        "Instinctively, you hop and throw yourself right under the window."
                        "A lion, peeks out of the window. Sebas looks left and right, unaware of you under the window."
                        "You can barely hold your breath, just enough for Sebas to take a sigh and returns to Rahim."
                        s "Doesn't seem like anything out there."
                        r "What were you talk about again."
                        s "Uh, I forgot. That sound distracted me."
                        "The two takes a quick pause, before you hear someone reaching into their pockets."
                        r "Are they coming after you."
                        s "No, not them. And... well."
                        r "For gods' sake. Can't you just cut off your tail and call it a day? You don't need to see him to survive."
                        s "Shhh! Stop shouting like you're talking to a goat."
                        r "Huh, maybe I am, if I stab these two needles on your head you'll look like one."
                        s "O-OUCH! Fuck! Alright, I get it. Don't need to actually do what you're threatening to."
                        s "I am just a messenger, okay? Maybe if you consider this option we can finall-"
                        r "Did I not make myself clear enough, don't ever mention them in front of me again. It's all useless."
                        s "I didn't mention the forbidden word, yet..."
                        r "Kid, you're giving me a headache, as if two aren't already enough."
                        r "I'm tired of all of you trying to ruin the only thing left for me to live."
                        s "Mister Rahim..."
                        r "I could have just minded my own business here, but no, you have to going around buzzing like a fly in my ears."
                        r "Everything would've been fine if you young people do your job, live for the day, and learn to listen for once."
                        "He pauses for a moment, scratching his head."
                        r "No more talks, aren't you here for the shop's spares?"
                        "As you press your ear against the wall, a shadow looms over you."
                        "Your eyes widen, but the familiar shape of a lizard tells you it's Ole."
                        show ole normal
                        pause .5
                        o "{size=30}W-what are you doing here, [e].{/size}"
                        "He whispers quietly, seems to have already understood your intention perfectly before answering."
                        "You turn your head and face the lizard, who just smiles at you."
                        o "Well, Kiddo. Next time find a better hiding spot if you want to listen more clearly."
                        e "Huh?"
                        o "There's something more important now, stand up."
                        "He pats your shoulder to gesture you to stand, while you're still in shock."
                        if isNight():
                            scene rahims_house_night with dissolve
                        else:
                            scene rahims_house with dissolve
                        show ole normal
                        "You follow behind Ole as he knocks on the door three times, the discussion has stopped, almost immediately."
                        o "Hey, Rahim. Someone's outside our village."
                        "You glances at the lion and the bull, staring at the lizard awkwardly."
                        s "Goooooood F-"

                        r "Who?"
                    else:

                        $ rahim_caught = True
                        "Instinctively, you hop and throw yourself right under the window."
                        "But a small misstep plunges you into the grass right next to you."
                        "Sebas pokes his head out of the window, and immediately notices your weak attempt at hiding."
                        show sebas grin with dissolve
                        s "Uh...buddy? You cozy right here?"
                        "You see the lion stares at your posture, face full of grasses and leaves."
                        e "Y-yes."
                        "Caught right in the act, you nod slowly and get up from the greenery."
                        r "[e]? How much did you hear."
                        "The bull peeks from the window, noticing your feeble attempt at hiding yourself."
                        e "Uh... not much, I was about to come in like a minute ago."
                        r "R-right..."
                        s "Our buddy's just curious haha! I've been listening into the nature lately too."
                        r "That's not the same!"
                        e "I'm so sorry, Rahim. I didn't mean to interrupt you two talking."
                        r "And those words wasn't meant for you to listen, yet you choose to sneak up."
                        r "Ugh... you young people are really the same, huh? No matter the worlds you live in."
                        s "Well, you should still come in, [e]."
                        if isNight():
                            scene rahims_house_night with dissolve
                        else:
                            scene rahims_house with dissolve
                        show rahim normal at l1 with dissolve
                        show sebas grin at r1 with dissolve
                        "You reluctantly enter Rahim's house, directly facing the frustrated bull."
                        r "Should I take your blind honesty as some kind of virtue?"
                        r "So, what are you doing here? Just casually spying on us like a fly on the wall?"
                        s "Or, a flea on the bull."
                        "Rahim shakes his head."
                        pause 1
                        e "I'm-"
                        "Just as you open your mouth once more, a familiar figure emerges from behind you."
                        o "Hey, door's not closed."
                        "Ole walks in casually, not aware of the situation you're currently in."
                        r "What! Are everyone going to come here right now?"
                        o "Someone wants to see you now."
                        r "W-who?"
                "Enter the door":

                    "You walk over the door, right as Sebas was about to peek out of the window."
                    e "Hey, R-... Seb?"
                    if isNight():
                        scene rahims_house_night with dissolve
                    else:
                        scene rahims_house with dissolve
                    show rahim normal at l1 with dissolve
                    show sebas grin at r1 with dissolve
                    "Sebas turns right, glancing at you with an awkward smile."
                    s "Well, good fu-"
                    r "Language."
                    s "-King Morning, [e]."
                    "You see Rahim rolls his eyes, obviously tired of Sebas' shenanigans."
                    e "Hey, I heard someone talking here, what were you guys talking about?"
                    s "Of course it's you, buddy. Haha, guess we spoke of the devil."
                    s "Whoops, Rahim might not seem like it but he's obviously enjoying his time with you!"
                    r "Huh...?"
                    s "Just kidding haha, if Rahim does, he's definitely the one who doesn't say anything about it."
                    s "Buddy, did you hear anything? Like... anything while you came through the door."
                    e "N-nothing really, I just wanted to use Rahim's tool."
                    r "I-it's right ther-."
                    "Just as Rahim opens his mouth once more, a familiar figure emerges from behind you."
                    o "Hey, door's not closed."
                    r "What is it, Ole."
                    o "Someone wants to see you now."
                    r "W-who?"

    o "Furkan. He said he wants to see you, in person."
    r "T-that... You are joking right? Isn't the lion enough of a nuisance already?"
    s "He didn't mean that."
    "Sebas whispers to you."
    r "Bring me to him right now! I need to know what he's thinking coming to our place like this."
    r "And Sebas, I don't want to hear a words about the goats again."
    "He points at you and Sebas."
    r "Stay put until I come back."
    "You nod, along with the oblivious lion."
    pause 2
    show rahim normal at r2 with move
    s "Well, roomie. Didn't know our bull has so much visitors today."
    s "Me, you, Ole, Furkan. That's four more buddies than the average buddies he sees in a day!"
    e "So that was... zero?"
    s "Uh..."
    pause 1
    s "Anyway, that's pretty silly for him to think we're staying here until he's back, isn't that right roomie?"
    menu:
        s "Speaking of, are we following Rahim?"
        "Follow Rahim":
            $ rahim_follow = True
            e "Maybe we should take a look?"
            s "Good idea! It's gonna be something very important. Well, that's why we should join in!"
            "You are not sure if he is sarcastic or genuinely oblivious. But, you've made the choice to go along with Sebas."
            scene lusterfield01 with dissolve
            show sebas normal with dissolve
            "Walking through the paths in Lusterfield, it's actually not too far until you hear the familiar grumpy voice of Rahim."
            r "You had the guts to talk to me right here... we could've had you killed here for what your people had done on this land."
            f "You can, you are too reasonable to be doing that."
            "You soon realise it's a bad idea to join in. Sebas takes a few steps backwards as the bull rolls his eyes, furiously."
            r "Leave."
            s "We're just-"
            with vpunch
            r "Don't make me say it again."
            show sebas shocked with dissolve
            "Sebas immediately turns back, he brings you a few steps away from the two leaders."

            s "Let's go back to our shop instead, buddy."
            "You nod. It's certainly not a good idea to have a target on your back when Rahim is angry."
            scene kings_pawn with dissolve
            show sebas normal with dissolve
            "Entering the shop, you can still faintly hear Rahim and Furkan talking in the middle of the village."
            "Ole is nowhere to be seen. You assume perhaps he's working on the shop inventory upstairs."
            "Sebas presses his ears against the wall curiously. Trying to figure out what they're talking about as you join in."
            show sebas normal at l2 with move
            r "-talk me through your thought process, what happened to your measly little goat brain- why do you think coming up to me is not a complete waste of time?"
            f "We have to talk."
            f "The primordial runes, we sensed its energy being unleashed again lately."
            r "We know it's capability."
            f "But-... the problem is, our general can feel its power being somewhere very near. We are afraid if they were the same personels who had stolen our basin."
            f "Someone is brewing up a plan, and it's unfathomable how the runes would be used for."
            r "Get to the point."
            f "We should join our forces, our people, and your people. To prepare for the looming threat."
            f "We're the closest to each other, we need to rebuild the bridg- and figure out what exactly happened. At least if someone is preparing for an attack, we will be ready for it."
            r "Why?"
            f "W-why... for our people of course. Do you really believe we have the intention to hurt yours at any point."
            "The bull doesn't even speak."
            pause 2
            "Furkan shakes his head."
            f "It was all a misunderstanding from the beginning to the end. We were about to retreat from you when casualties happene-"
            r "Casualties."
            r "So you think all of the lost lives here were just casualties out of nowhere?"
            r "It was your people's doing. Your father and his reckless soldiers' spell crumpled our houses like they were his playthings, must be accidents that people happen to be inside."
            f "We didn't mea-"
            r "Your spells and magicks doesn't work now, so you come here and do what? Beg me to send you more casualties to waste away?"
            f "Someone was behind what happened between us, Rahim. And, I think you know this. My father would never... risk his whole tribe to conquer your village."
            r "Maybe you don't know your father, then."
            f "Look, I don't know what you two had talked about, right before the war broke out. But Tevfik would never try to do something like this, to their most loyal ally."
            f "Rahim, I know it's a difficult situation, and it takes time to consider. We all trusted you, and I trust you to make the wise decision that's the best for both of us."
            "Furkan turns around with a nod, he turns around slowly until Rahim shouts."
            r "...Don't you walk away from me, coward."
            "The chief turns back, with a doubtful glance."
            f "Excuse me?"
            r "You come here all alone, showing me all this grand gesture of peace. Yet you walk away, right after you lay all that responsibility onto me?"
            r "Is that what you always end up doing, Furkan. Just walk away from all the troubles you've made."
            f "That's not my intention."
            "Furkan retorts, crossing his arms as Rahim chides."
            r "I can't even imagine, how naive are you to think that things could ever go back to the way it was."
            r "Or are you so thick in the head that you want to live with the person who killed your father right there."
            "You and Sebas stare at each other in disbelief as Rahim shouts louder and louder."
            f "I- I will try, if it means my tribe will thriv-."
            r "For years we have been living through the loss of our loved ones. A-and you come here and tell me that I should try... like you?"
            "It's rare to see Rahim gets, this emotional. His voices are trembling and he's choking in his words."
            f "We... I just think we should put away our own ambition when it comes to the safety of the tribe."
            r "Ambition. How charitable, I should just forget about everything that had happened because you did. Because you weren't even there for your father when everything went down."
            f "Rahim, I came here to talk- not to dwell over what happened between us."
            r "All I wanted was a peaceful life, and it all went to ruins because you goats were too stubborn to take a hint."
            f "My apologies, if that is how you feel."
            f "But I reckon I shall not stay this long."
            f "Take care, Rahim."
            "Furkan turns around once more."
            r "Leave, that's all you know."
            "The streets falls into dead silence as Furkan leaves the village. There is not a sound of footsteps so you assume Rahim is still standing there."
            "You and Sebas are in shock, the lion steps away from the wall soon after."
            s "Damn..."
            "He whispers, trying to keep it low as you both can still feel the anger of Rahim looming by."
            s "That- just happened."
            e "Stop talking."
            "You shake your head as the both of you get back to work."
            e "Should we go check on Rahim?"
            s "Wait it out, roomie. With this loud he's screaming today, he's gonna sew your mouth shut if you're existing within his visible distance."
            "Sebas grins for the while. But he's right, perhaps it'd really be a good idea not to bother Rahim so soon."
            $ timenow.addTime(0, 2, 0)
            jump main_lusterfield01
        "Stay put":

            $ rahim_follow = False
            e "Maybe... we should stay here for a while, like what he talked about?"
            s "Eh, yeah you're right, roomie. It's between him and Furk."
            pause 3
            "Sebas grins as you two stay put, occasionally you hear Rahim's shout, though it's not loud enough for you to make out what he's saying. And soon Rahim is back."

            show rahim normal at r2 with move
            r "Y-you two are still here...?"
            s "So... shall we contin-"
            r "Leave me be, would you?"
            "Rahim is completely exhausted. His eyes watering up."

            e "We understand."
            "You feel he's desperately holding back his breath, his teeth gritting against each other."
            r "T-thank you."
            "Sebas raises his brows, tugging on his snouts curiously."
            "Without any question, you lead the still confused Sebas out of his house."
            s "Uh, that was weird."
            e "I- I'm not sure what has happened there."
            s "I told you buddy we should've followed Rahim, the mystery is making me go absolutely insane like he does!"
            s "But, uh. Yeah, privacy. I get it, how fucking cool was that."
            if rahim_caught:
                s "Anyway, how long were you sitting there, well. Usually Rahim really doesn't like people being sneaky around him."
                e "Uh... just a minute. I was wondering if I should knock on the door."
                s "Hah, fair, fair. I guess he's not really that angry with you anyway, not after what he and Furkan talked about."
            s "But wait it out before you go knock on his door again, roomie. With this loud he's screaming today, he's gonna sew your mouth shut if you're existing within his visible distance."
            "Sebas grins for the while. But he's right, perhaps it'd really be a good idea not to bother Rahim soon."
            $ timenow.addTime(0, 2, 0)
            jump main_lusterfield02

label Rahim_Voting_Quest_Begin:

    e "Hey, Rahim. Everything going right... after that day Furkan was here?"
    r "W-why are you asking."
    e "Uh- I'm just looking out for you, Rahim."
    "Rahim gives an inquisitive eye, he puts down his needle and stares at you."
    if rahim_caught:
        r "You can just sneak outside my house again. That'd make it easier."
    else:
        if rahim_follow:
            r "Do you? I don't see you ever listening to what I say."
        else:
            r "...yeah. Thanks."
    "You two remain silent for a while as Rahim frowns."
    pause 0.5
    "He glances at you for a few more times. One that's more awkward than it needs to be."
    r "I... I've been distracting myself with the same thing ever since everything went down."
    r "Yet all I had in my mind, was reliving that terrible memory take place right in front of me, over and over again."
    r "I was stuck in the past, and I allowed myself so."
    "Rahim looks down in frustration, you try to offer your hand but he waves it away."
    pause 1
    r "Furkan, he was a much better boy than I am. He surrendered his dignity to talk to me, and I... I was the one who ran away."
    e "What do you mean, Rahim?"
    r "After talking with Furkan, everything was crammed into my head all at once. And all I could do, was to hide myself behind that closed door."
    r "I had been awake the whole night, day, and then night. And the only time I fell asleep, I saw my daughter."
    e "Y-your daughter? Was it... in a dream?"
    r "I don't remember it very well. But... I- recall hugging my precious princess right there, I held her tight in the air."
    r "I saw her chuckling, making a silly face. And- I was frozen. I stood there for a long while."
    r "Her features are getting foggy, and I just realised I didn't even recognise what her face looks like."
    r "One day I'll forget her voice, her face. Or... even her whole existence."
    e "Rahim..."
    r "In that dream, she was just in my hand, until whatever happened and she turned into a giant spider, wrapping me there inside of the spiderwebs-"
    "Rahim squints his eyes, his lips curls into a state of sadness."
    pause 2
    r "Well, I'm starting to talk nonsense now."
    e "No, no. It's a nightmare what you've been going through, I- I really can't compare my experience, but coming to this, whole new place. It's been largely different."
    e "Everyone has been nice all around the place, I can't even imagine you two being in war for each other's head."
    e "I remembered... my allfather- the chief of my tribe. He would gather us all around him. I forgot most of what he said... but he has a verse he likes to recite whenever some of us are sad."
    e "{i}'Like the eternal stars that flicker in the night, let us sparkle with the timeless light.'{/i}"
    e "{i}'The past is a lullaby of memories, but the present is where the undying forces take flight.'{/i}"
    e "I'm not sure if this finds you well- but I guess it left all of us at peace at the time."
    r "It does. That was a comforting wisdom that I never imagined coming out of your mouth. Thank you, [e]."
    r "If anything, a part of me wants to move on with my life, and another part forbids me so."
    r "But this is never just about an old bull like me as painful as it would be for me to realise."
    "You look back up and notice Rahim's sharp glare, it's not as stern as he usually does."
    r "Maybe after everything has settled down with your problems, we'll share some more wisdom with your chief."
    "He smiles at you, it's just so rare to see him finally be happy, even if it's just a glimpse."
    "You indulge in the silence once more, Rahim kneads on his tense forehead, before taking a deep breath."
    r "There's just one thing, I've made up my mind."
    r "I will announce that a voting day is to come soon. It will decide whether we will form an alliance with the goats once more."
    e "W-wait, Rahim. Are you sure?"
    r "Well, take it as I am not the one to decide the fate of our people. I can't take all that baggages onto my back."
    r "I have my grudge with them. But there are people like you, you see things more differently than an old bull does."
    r "You deserve something on your plate, for the better or worse."
    e "I'm glad you turned around, Rahim."
    r "Don't be so sure we'll ally up with the goats I tell you, and if so, good. I've done my part, Sebas would have no reason to come and bother me once more."
    r "This is a once-and-for-all vote. We'll never talk about this again, alright?"
    e "Alright."
    $ rahim_recon = -10000
    jump Rahim_Voting_Quest_Begin_Ready

label Rahim_Voting_Quest_Begin_Ready:
    menu:
        r "If so, we'll start preparing for the announcement. It should take five days for everyone to make up their mind."
        "Let's begin the preparation":
            e "Ok, I think it's fair. We're ready."
            jump Rahim_Voting_Announcement
        "Maybe later":

            $ rahim_vote_ready = True
            e "Maybe we still need more time."
            r "Okay."
            jump main_rahimshop

label Rahim_Voting_Announcement:

    r "Good."
    scene black with dissolve
    pause 1 
    scene lusterfield02 with dissolve
    show rahim normal
    "You follow Rahim out of his hut. Towards the center of the village. A few people gathers, some murmurs."
    r "Ahem."
    r "Greetings, everyone. Please gather around here, I have something to say."
    "More people approach as Rahim stands on the stage, he clears his throat and takes a deep breath."
    r "I have not been standing here for, well. Since the last mayor passed away long ago."
    r "For the past few years, Lusterfield has been living on its own, isolated."
    "The crowd stares curiously, if not with a surprised face."
    r "And it was my sole decision. You all had looked up upon me during hard times. You elected me as the leader."
    r "But ultimately, I was selfish. And I had lost my way of leading the village to prosperity out of personal vendetta."
    r "So, I suppose it's only appropriate for us to embrace a change."
    $ todaydayofweekfromrahimvote = weekdictionary[weektuple[int((timenow.day - 1 + rahim_vote_duration) % 7)]]
    r "On [todaydayofweekfromrahimvote!t], we will hold a vote to decide whether we should form an alliance with Goat Tribe once more."
    r "It has been a long time coming, and I can only hope whatever the result will be, both sides of you are satisfied."
    r "Thank you, everyone, and may the spirits bless our endeavors."
    "Rahim gives a solemn sigh, and returns to his house without another words."
    "You hear some crowd murmurs, both sides are discussing the result of the vote. Some of them in protest of Rahim's decision."
    "There are 5 days until the vote begins, perhaps you should ask others about their opinions."
    $ QuestBegin(quest37)

    $ quest37.qProgress(_("Vote for the future of Lusterfield on next ") + todaydayofweekfromrahimvote)
    $ quest37.qProgress(_("Talk with other Lusterfolks about their opinions"))

    jump main_lusterfield02

label Rahim_Voting_Opinion:

    e "So, what do you think about the vote?"
    r "The vote I'm holding...? I've already told you what I felt. If I had to decide, there won't be one to begin with."
    e "But you did decide to hold a vote."
    r "You people's voices sometimes get on my nerve, I just wanted to shut all your mouth up, once and for all."
    "Rahim says with a monotone, puncturing the fabric with the needle."
    e "Maybe sometimes it's good to take a step back, you know."
    r "I took a step back, I took a step back back when the goats come here taking everyone hostag-"
    "He suddenly stops mid-sentence, something must be bothering him for ages."
    r "Ugh..."
    e "Maybe the fact that you changed your mind... is because you never considered them a threat?"
    "You try to console the bull, but he gives you the grumpy face instead."
    r "That's what a part of me wants to believe, but it's not the reality."
    r "If histories want to repeat itself, I don't want to get in its way again."
    e "What changed?"
    r "Nothing."
    "He says, before you even finished your sentence."
    e "Really? I don't believe a ruthless bulls like you will suddenly change your mind over night, after what happened with Furkan."
    r "I said Nothing. I will still vote against the goats, if that is what you want to say."
    r "I am just doing this for the welfare of the village, whatever it means."
    "Rahim remains calm, before he shifts his attention back on the cloth."
    e "O-okay, I guess so."
    "He continues working as you pondering leaving, but suddenly he speaks to you again."
    r "Once the vote is over, come back and see me."
    "You nod, before taking your leave."

    jump main_rahimshop

label Sebas_Voting_Opinion:
    e "Hey, Seb, how do you think about the vote?"
    s "Ha buddy, well. I guess maybe my charm is just so much to handle for Rahim."
    s "Look."
    "Sebas leans his head forwards, showing you his two blinking eyes."
    s "See, even that old bull's not invulnerable to my persuasion skills on those blinkers."
    e "I was pretty sure the vote wasn't because of you."
    s "Ha, buddy you know me the best, of course! It's Rahim who announced the vote."
    e "Uh-"
    s "And he's letting me organise everything, like a stamp with this lion face here."
    "He grins, showing you a box full of stamps with the gleaming eyes."
    s "These precious little chops are from some pledges I got earlier, just repurposed it and added my own pattern."
    "Basically, I've prepared for everyone a paper with two boxes, when the day comes you come here and make a stamp on either box to vote."
    e "T-that's very impressive actually."
    s "I know! I'm dreading the day we vote so I can collect papers with a lion face from everyone."
    e "Ah, so, how will you vote?"
    s "Well, ally with the goats of course, trade, let the goats come and visit our shop, that'll probably solve everything."
    e "Did something changed your mind on the goats? You didn't sound too enthusiastic about them the last time we talked."
    s "Hah, well. I didn't change my mind, I-I just thought it's cool to have more customers, to you know... give us money."
    s "But my Big Ol' didn't look very happy about it. At least as compared to how I feel, hah."
    s "Maybe you'd be better off asking him, maybe make him change his mind."
    e "Why are you not asking?"
    s "I did! But Ole is a stubborn lizard, you know. Once he believes in something, he really does stuck with it all the way through."
    e "Oh, so your presuasion skills on those blinkers aren't working on Ole?"
    s "No way, how can my blinkers not work? I know they'd already worked on you, heh."
    "Sebas chuckles as he whistles playfully."
    jump main_kingspawn

label Lothar_Voting_Opinion:
    e "Hey, Lothar, how do you think about the vote."
    l "Bad, disciple. It's bad. What was Rahim even thinking, after so much I've proven that the goats are evil incarnation of cult following brainless magical dirtball. I can't believe he's still choosing to not just trust them, but ally?"
    e "He's giving all of us an option, Lothar. I think he won't really vote for the goats himself."
    l "The bull's disrespecting the hero's opinion once again. Afterall, I eliminated that whole threat for him."
    l "I guess people forgets what was done to them too easily, huh?"
    e "So... you're voting against it?"
    if lothar_affection > 15:
        l "Yeah. Are you not?"
    else:
        l "Are you asking a stupid question or trying to rile me up again, disciple."
    "He glances at you for a moment, before averting his gaze."
    l "Either way, I've told Amble and Jog what to do already, there's no way the goat sympathizers can win this one."
    e "Uh..."
    l "There's no way I tell you, [e]. And don't let me see you vote otherwise."
    jump main_lusterfield01

label Amble_Voting_Ask_Cement:

    e "What do I need for the bridge again?"
    a "20 wooden logs, and three buckets of mortar, known as masonry fix."
    a "So, we'll need some irons, some clays, some slate rocks."
    a "You know where to find them. There are stone wards at the damp cave, which you may find slate, sometimes."
    "You smile uncomfortably as Amble begins pointing at random directions at where the materials should be."
    "And you're fairly sure that Jog is not one of them."
    a "Clays are right under the river, with a powerful shovel you can easily dig them up."
    a "And the iron, I'm sure the werewolves will gladly lend you some, puny friend."
    "He winks at you confidently, you hope he's saying this to praise your battle ability."
    a "Mix them together and you'll get some seme-... cement. And then you'll need to mix them with limestones."
    "Amble gestures his hand together, stroking the air up and down to mimic the mixing motion."
    "You stare in embarrassment, well, it really does look like he's stroking a huge... pillar."
    a "Limestones are very abundant in a yellowish cave, near the goat tribe. You might need to get someone knowledgeable enough to show you that entrance of the cave. It should be easy to get a pickaxe from werewolves!"
    a "But, I've heard there is a minotaur inside the cave. So stay safe there, [e]."
    a "Anyway, mix them, and then get a bucket for yourself, and tada-! A bucket of mortar is done, perfect for sticking stones together."
    a "Then you bring them back to me, and we'll get started on the bridge!"
    e "Alright, I got it now."
    jump Amble_Normal_Talk

label Amble_Voting_Opinion:

    e "Hey, Amble, how do you think about the vote?"
    a "Good, and how about you, puny friend?"
    a "Are you more of a goat person? or a... lustery person-?"
    menu:
        e "Well, now you're the one asking."
        "Support the accord":
            e "I- I think I do wish both of the tribes are thriving, so I'll support it."
            a "Ah, you sure brings a lot of wisdom to the table, [e]."
        "Oppose the accord":

            e "I guess it's not necessarily for us to, ally up. I don't see an imminent threat lurking to take us down one by one."
            a "That's... true. Actually, I hadn't thought about that perspective."
    e "And what about you? What would you vote?"
    a "That's a good question. Hmm... I haven't decided yet, but Lot, he told me I needed to vote no."
    a "It's an important decision, that's why we should get educated on both sides before making a decision."
    a "But Lot seemed so serious about this, I can't tell, if going against his wish would be a good idea."
    "Amble looks left and right, he's still undecided as he scrubs his palms together."
    e "Did Lothar really tell you what to vote?"
    a "Indeed! Jog was there too. The whole conversation was very weird, even to Lot's standard."
    e "No, that's the least surprising things that I've heard out of his mouth."
    a "Ha, you're funny, [e]."
    "Amble gives it a chuckle, before returning to his usual smile."
    a "Anyway, I still haven't decided yet. But there's still one thing I wanted to do before making a decision, are you coming with me, puny friend?"
    e "Oh? What is it?"
    a "It's the stone bridge between our tribes, we need to clean up the debris, get ourselves some foundation, and return it to its previous glory!"
    a "If we have to vote for some kind of reconciliation, wouldn't it be better if we have a means of transportation there?"
    e "But what if the vote goes the other way?"
    a "Well, it doesn't hurt to fix something for once, does it?"
    "Amble gives you a lopsided grin with a slightly narrowed eyes."
    menu:
        a "So, I suppose you're coming?"
        "Accept Amble's Offer":
            e "Alright. So, how do we start?"
            a "First thing first, we need some basic building materials before we head there."
            a "It's going to be very grindy, puny friend. You'd need to grind a lot for these."
            e "Uh, grind?"
            a "Grinding the limestones into cement! For the stone bridge of course! We're not allowed to make any jokes that's out of the scope of our world anymore."
            a "Anyway, I'll prepare some large rocks there myself, how about you bringing me some small rocks?"
            e "I'm definitely more than capable than bringing some small rocks."
            a "Hah, well. I don't doubt that! But the large rocks I need is probably bigger than you do, so it's safer for me to carry."
            a "But, we'll need some more logs. I suppose you know how to cut down the trees, right?"
            e "I do!"
            a "Good, and then, for the sticky materials, we'll need a bucket of mortar, which is just a mixture of limestone and cemen-."
            e "S-semen?"
            a "I can't ever say that right without remembering what Jog said! Cement. What a silly name, right?"
            a "So, we'll need some irons, some clays, some slate rocks."
            a "You know where to find them. There are stone wards at the damp cave, which you may find slate, sometimes."
            "You smile uncomfortably as Amble begins pointing at random directions at where the materials should be."
            "And you're fairly sure that Jog is not one of them."
            a "Clays are right under the river, with a powerful shovel you can easily dig them up."
            a "And the iron, I'm sure the werewolves will gladly lend you some, puny friend."
            "He winks at you confidently, you hope he's saying this to praise your battle ability."
            a "Mix them together and you'll get some seme-... cement. And then you'll need to mix them with limestones."
            "Amble gestures his hand together, stroking the air up and down to mimic the mixing motion."
            "You stare in embarrassment, well, it really does look like he's stroking a huge... pillar."
            a "Limestones are very abundant in a yellowish cave, near the goat tribe. You might need to get someone knowledgeable enough to show you that entrance of the cave. It should be easy to get a pickaxe from Gwyd!"
            a "But, I've heard there is a minotaur inside the cave. So stay safe there, [e]."
            a "Anyway, mix them, and then get a bucket for yourself, and tada-! A bucket of mortar is done, perfect for sticking stones together."
            e "Hmmph... alright."
            a "Yeah, I think that's really all. We should get going! Time doesn't wait for a collapsed bridge!"
            $ QuestBegin(quest38)
            if cementrecipe not in discoveredrecipe:
                $ discoveredrecipe.append(cementrecipe)
            if masonrymixrecipe not in discoveredrecipe:
                $ discoveredrecipe.append(masonrymixrecipe)
            $ quest38.qProgress(__("Prepare 3 Masonry Mix for Amble"), "Masonry Mix", 3)
            $ quest38.qProgress(__("Prepare 20 Wooden logs for Amble"), "Wooden Log", 20)
        "Maybe Later":

            e "Maybe I'll join you later?"
            a "I have a hunch we'll learn so much more after rebuilding the bridge."
            "Amble raises both his thumbs up, with the same old smile he has."

    jump Amble_Normal_Talk

label Amble_River_Talk:
    call showing_riverside_crossing from _call_showing_riverside_crossing_3
    if quest38.status == 3 and amble_hauling_progress != 0 and amble_hauling_progress < 100:
        $ amble_hauling_progress = ((timenow.hour+timenow.day*24) - amble_hauling_amble)*2 + amble_hauling_tenki
    show amble normal with dissolve
    a "It's really hot out here in the forest, puny friend."
    menu:
        a "[e]! What's on your mind?"
        "Rebuild the bridge with Amble" if quest38.status == 3 and amble_hauling_progress == 0:
            jump Amble_Voting_Clearing
        "Continue on your hauling work with Amble" if quest38.status == 3 and amble_hauling_progress > 0:
            jump Amble_Voting_Clearing_Work_Back
        "Continue on the construction work" if quest38.status == 4:
            jump Amble_Voting_Construction_Work
        "Check in on Amble and the moss monster" if quest38.status == 5 and timenow.day * 24 + timenow.hour <= amble_hauling_amble + 7:
            jump Amble_Voting_Continue_Bridgeroot_Break
        "Continue on the construction work" if quest38.status == 5 and (timenow.day * 24 + timenow.hour > amble_hauling_amble + 7 or bridgeroot.win >= 1):
            jump Amble_Voting_Continue_Bridgeroot_Finish
        "That's all for now":
            jump Amble_Dialogue_End

label Amble_Voting_Cement:
    $ removeItem("Masonry Mix", inventory, 3)
    $ removeItem("Wooden Log", inventory, 20)
    e "Hey, Amble. I've gotten us the materials you need. 20 Logs, and 3 buckets of masonry mix."
    a "Great! Now we can get started with building it."
    e "There's one question."
    a "What's on your mind, puny friend?"
    e "Why do you ask me to get so many logs, when you already have some much lying right around here?"
    "You point at the massive amount of wood, chopped or unchopped, all placed peacefully behind Amble."
    a "Oh, good question!"
    pause 2
    a "A-a-anyway, I think we're ready to get our work done."
    a "I've inspected the bridge, luckily when it was broken, the goats preserved their structural integrity rather well. That'd save us a lot of time and energy."
    if not riverside_crossing.discovered:
        $ riverside_crossing.discovered = True
        a "I've marked down the location of the bridge on your map."
    a "Meet me right there, then we'll start moving the old debris!"
    e "A-alright..."
    $ quest38.status = 3
    $ amble_hauling_progress = 0
    jump main_lusterfield_range

label Amble_Voting_Clearing:
    $ amble_hauling_tenki = 0
    $ amble_hauling_progress += 1
    $ amble_hauling_amble = timenow.day * 24 + timenow.hour
    e "Hey! Amble, so, what do I need to do here?"
    a "Oh! I like your attitude, keep it going for the bridge and we'll be finishing in no time!"
    e "Ah? We... both, building an entire bridge?"
    a "Ha, not quite. You see, some huge debris are already stuck down here, so we just need to put them back where they were."
    e "It doesn't look like the stones are in perfect condition, though."
    a "You're right, that's why we need some mortar and rocks, to fill in the small gaps that corroded away during this whole time."
    e "Damn, Amble. You've really thought about everything."
    "Amble turns to you, with a slightly raised eyebrows."
    a "Puny friend, are you trying to get something out of me?"
    e "W-what? N-no..."
    a "Or make my cheeks go red by praising me?"
    "He gets uncomfortably close to you, with one hand essentially wrapped around your shoulder."
    e "A-amble, how would-"
    "Amble glances at you, his grin widens very quickly as he breaks into a heartful laughter."
    a "I learnt this from Jog, hah. Looks like it did get a reaction out of you."
    "You avert your gaze, still haven't recovered from his attempt at teasing you."
    e "Huh?"
    e "Not fair! I didn't expect you to joke around like this, Amble."
    a "You're fun, puny friend."
    "He quickly turns his attention back towards the stones, and stretches his arms extensively."
    a "Let's get everything started, shall we?"
    menu:
        msg "Do you wish to spend 2 hours and some HP to remove the rocks? Higher STR will increase each session's progress and HP cost."
        "Remove some rocks with Amble":
            e "Alright! Let's get into it."
            a "You've got the right attitude! Keep it up!"
            "You walk down the river and begins to work on the rocks with Amble."
            jump Amble_Voting_Clearing_Work
        "Let Amble start working by himself":
            jump Amble_Voting_Clearing_Work_Leave

label Amble_Voting_Clearing_Work:
    $ pc.hp -= 10*pc.stg
    $ amble_hauling_tenki += int(pc.stg*1.5)
    if pc.hp < 0:
        $ pc.hp = 0
    "For the next two hours, you dig up the rocks with the shovel Amble has given you, and he carries them on the land, trying to figure out where they come from from the bridge."
    if renpy.random.random() < 0.5:
        "Occassionally, he gets into the water as well, helping you remove huge rocks from the side with water."
        "Somehow, you can feel his jock submerged into the water completely, lightly brushing against your side as he hauls the rock above water."
        "You moan quite loudly when you realise his slick bulge is pressed against your thigh under the water, and it unceremoniously slides to the side of your leg as he leans forward."
        a "Hey, something wrong?"
        e "Uhm... nothing. Keep doing what you were doing."
        a "You're truly fascinating, [e]."
        "Carelessly, he holds onto your arms tightly to pull out the rock, you get to feel his soft bulge scraping, as if he's intentionally teasing with you."
        "That, that was an experience."
    "As you've finished your session, you look towards the pile of rocks you've hauled out of the river."
    $ amble_hauling_progress = ((timenow.hour+timenow.day*24) - amble_hauling_amble)*2 + amble_hauling_tenki
    if amble_hauling_progress < 33:
        "It seems most of the rocks are yet to be removed, more works needs to be done before the river is unclogged."
    elif amble_hauling_progress < 67:
        "Amble gives you a thumbs up as he shows you all the rocks on the river bank, some river water begins to flow to the other side now."
    elif amble_hauling_progress < 100:
        "There's still something needed to be done, but at least the river water can now flow to the other side."
    else:
        a "Aha, I think all huge rocks are removed now. Look at that beautiful river, clear as crystal!"
        "He's right, this part of the river is no longer clogged, and the water flows freely to the other end once more."

        e "That was some hard work."
        a "And it all thanks to you, [e]."
        e "Ha, well most of it was your doing, I was just digging some dirts there, I think you deserve all the credits."
        jump Amble_Voting_Construction_Begin

    jump Amble_Voting_Clearing_Work_Continue

label Amble_Voting_Clearing_Work_Back:

    e "Hey! Amble, I'm back."
    if amble_hauling_progress >= 100:
        "Amble sits on the river bank, seemingly pondering something."
        "You glance over the river, surprisingly, the hauling work seems to be completed, leaving all soaked debris on the shore in front of Amble."
        a "Oh! Didn't notice you, puny friend. Welcome back!"
        "He turns around, and gives you a friendly wave."
        a "Well, please pardon me. I wanted to finish the job with you but, I got way over my head."
        "Amble scratches the back of his head squirmishly, his cheeks perks up, revealing a wide grin."
        e "Damn, no worries, Amble."
        jump Amble_Voting_Construction_Begin
    else:

        "You see Amble still hauling the rocks all by himself, his chest is drenched in sweat, glistening under the sunlight."
        "He turns around, and gives you a friendly wave."
        a "H-hello, puny friend."
        if amble_hauling_progress < 33:
            "It seems most of the rocks are yet to be removed, more works needs to be done before the river is unclogged."
        elif amble_hauling_progress < 67:
            "Amble gives you a thumbs up as he shows you all the rocks on the river bank, some river water begins to flow to the other side now."
        else:
            "There's still something needed to be done, but at least the river water can now flow to the other side."
        e "Damn, Amble, did you just dig them up and haul them out of the river all by yourself?"
        "You wipe off the sweat from Amble carefully, he leans forwards so you can reach his chest, and closes his eyes for a moment."
        a "Thanks, puny friend. I feel much cooler now."
        e "You seem so tired, do you need to take a rest?"
        a "Carrying these rocks surely is an exhausting work, but isn't it so great to take a deep breath right here?"
        a "I can go on, and on. This is just why I like working in the forest, it makes you feel alive."
        "He gives you a bright smile, and you smile back."
        a "Anyway, [e], do you want to join? It would be much quicker to have another pair of hands digging these heavy rocks up."
    jump Amble_Voting_Clearing_Work_Continue

label Amble_Voting_Clearing_Work_Continue:
    menu:
        "Should you continue for another 2 hours?"
        "Remove some rocks with Amble" if pc.hp > 0:
            e "Let's keep going, I believe we can complete it very quick!"
            a "Ha! That's the spirit, keep that positivity flowing!"
            jump Amble_Voting_Clearing_Work

        "{s}Remove some rocks with Amble{/s}" if pc.hp <= 0:
            "Your HP is too low to continue work."
            jump Amble_Voting_Clearing_Work_Continue
        "Let Amble continue himself":

            jump Amble_Voting_Clearing_Work_Leave

label Amble_Voting_Clearing_Work_Leave:
    e "Well, actually, I need to go."
    a "Ah, is there something wrong, [e]?"
    if pc.hp <= 10:
        e "Well, I'm getting really exhausted, so I'll need to take some rest."
    else:
        e "Nothing really, I just remembered there's something I need to do right now."
    e "C-can I come back later?"
    if amble_hauling_progress == 0:
        a "Sure thing, puny friend. I'll get started myself, it's gonna take some time without an extra pair of hands here."
    else:
        a "Sure thing, puny friend. I'll continue with the work, it's gonna take some time without an extra pair of hands here."
    a "But leave it to me! You've already gotten me a lot of materials to work with. You've been a great friend, and I'll always have your back!"
    e "Thanks, Amble. You're just too wholesome, I'll make sure I'd come back and help you with everything I can do."
    "With a friendly wave, you part ways with Amble."

    jump main_riverside_crossing

label Amble_Voting_Construction_Begin:
    $ quest38.status = 4
    "Amble gives you a bright smile as he walks along the river."
    a "There are still work yet to be done, will you offer me some more assistance?"
    a "I can do it all by myself, but, it's great to have someone to work along. Communication is key, isn't that right?"
    e "I'll lend you all the help you need, Amble! Plus, your enthusiasm is just too contagious!"
    a "That's the [e] I know!"
    "He gives your back a quite powerful pat, bashing you forwards for a few steps."
    a "Oops, sorry puny friend. Forgot you were Jog's size."
    e "It's fine, I think you broke a few rib bones there."
    a "Did I?"
    "You're not sure if he's too dense or cheeky, but he extends his large hand from behind you, in the direction of your chest."
    menu:
        "Should you let Amble check on you?"
        "Show him where you're hurt":
            "You nod, and let his hands touch your scruffy fur."
            scene black with dissolve
            "His whole arm exploring your front with no resistance from you at all. Much attributed to yourself enjoying his rough paws."
            "Both of his hands advance on your chest from underneath your arm, searching for your rib bones through all the muscles you have."
            "He's pressing hard, hands drifting through all the scruffy furs of yours, your hand lightly grabs his to guide him onto your bulging chest."
            "Amble doesn't seem surprised, instead he intentionally trails his way onto your sensitive nipples, flicking it with rather ease."
            e "Hey! Are you really checking my ribs?"
            a "Sorry, had to check this one as well, we gotta be very thorough, don't we?"
            "You can't see him from this angle but you know damn well he's smiling or grinning at you."
            "Maybe also because your nipples perk up instantly in response to his touch, his hands are rough, and the texture on his paw pads causes you to shudder constantly."
            "His hand continue exploring your chest for a moment, squishing it like a heavy bag of milk."
            "You audibly moan when his bear claws lift up your bare chest for a moment."
            a "Did that hurt?"
            e "N-no... but please continue."
            "He stretches open his hands, and grasps onto your chest with much force, his huge palm moves around, squeezing your chest in all position or direction."
            "Amble continues fondling with you for a moment as you feel all the ecstacy building up, but he suddenly releases, and retreating his hand from your chest."
            "You can see the red marks imprinted all over your chest there, in the shape of Amble's large hands."
            a "Well, puny friend, your bones are strong as ever."
            a "Shall we continue?"
            "You stare at Amble with a pleading eyes, hoping he'd continue with his act but the bear has already continued his walk, you caress your front for a moment, before tidying yourself and catching up with Amble."
            call showing_riverside_crossing from _call_showing_riverside_crossing_4
            show amble normal with dissolve
        "Excuse yourself":
            e "H-hey, Amble I don't think... Maybe we should keep on going..."
            a "No? How else do I know if you're fine, [e]?"
            e "Well, I was joking. You didn't break anything, {size=25}or at lease I hope...{/size}"
            a "Haha, you're funny, puny friend. Alright, let us continue then."
            "Amble gives you a bright smile, as usual. And continues to walk onto the water."

    a "Alright, now if we're building an entirely new bridge, we'll need a cofferdam to build to base of the bridge."
    a "We can enclose and drain the area around the base with some wood, that's going to take a lot of days and nights."
    e "But we already have the base of the bridge right here, don't we?"
    a "You're right! That's why we can take some break."
    a "Now, we'll need the wood you just collected, get as much wooden planks there and connect the two ends together with an arch. That'll fix the shape the bridge, so we know where to insert these rocks later on."
    "He motions with his hand with where the planks should go, either vertically or horizontally, squinting his eyes to imagine their position."
    e "Okay, so... how do we start?"
    a "We'll measure the distance, make sure they are as concise as possible, and we'll set the wooden planks in place with some ropes."
    a "That's going to be much quicker than removing all these rocks, but I can't do it by myself, measuring is not my strongest suit."
    "Amble takes a sigh."
    a "But, if you need some time to rest, please feel free to do so. It's still going to be exhausting."
    menu:
        a "Would you like to lend me a hand, [e]?"
        "Let's go":
            jump Amble_Voting_Construction_Work
        "I'll continue later":
            e "I guess I'll take a little rest for now. I'll be right back."
            a "Alright, [e]. Find me here when you're ready."
            jump main_riverside_crossing

label Amble_Voting_Construction_Work:
    $ amble_hauling_amble = timenow.day * 24 + timenow.hour
    $ quest38.status = 5
    e "Alright then. Let's go!"
    a "Hah, I knew you had it in you, well. Let's get down to the business, then."
    scene black with dissolve
    pause 1
    "Amble walks towards the river, with the planks as you begin to take measurement of the river with his tools, it's not very wise to work under the current of the river but Amble doesn't seem to mind."
    "You point to where Amble needs to put down the planks, and he does so, with rather ease as the pole digs through the river bed with one plunge."
    e "Is this stable?"
    a "No, this is a bridge."
    "Amble gives you a cheeky grin."
    a "You can say, these planks are set in stone, I don't think it's going to go anywhere."
    "You struggle to hold your own chuckle as Amble smile at his own joke, again. Perhaps you are even entranced, staring at his dumb yet cheer smile dazzles you with undescribable happiness."
    pause 1
    "For the next 4 hours, Amble continues jabbing the planks into the river, and fixing them with the ropes you prepared."
    "You're almost finished with the job, and the river is now filled with planks and an arch over the bridge."
    "Staring at the bear's beefy body, it seems he's sweating all over again, his fur is drenched in either river water or his own sweat."
    "For a moment, your gaze is fixated on his strong physique, until you are distracted by something green in a distance."
    "You point towards the direction, and Amble begins to notice it as well."
    call showing_riverside_crossing from _call_showing_riverside_crossing_5
    "It seems to be approaching in your direction, not particularly in a malicious way, but still rather intrusive."
    "As it closes in, you realise it's a mossy monster, one that is similar to the golem you encountered while travelling with Sebas and Lothar."
    e "What's that?"
    a "I have never seen something like him before, something like this is a work of nature, [e]."
    "The monster is covered in all kinds of greenery, roots, leaves, moss, flowers, fungi. His eyes staring at the bridge blankly."
    "Amble spends a moment to admire this green construct, before it takes a seat on the construction right in front of you two."
    a "Hey there, mister, we're working on a construction right now."
    "It doesn't seem to listen to Amble at all, just sitting on one end of the bridge casually."
    "He settles into the position rather quickly, and any yanking or pulling effort by you and Amble remains futile."
    a "Mister... this is not for sitting."
    "Amble is genuinely distressed right now, his brows furrow intensely as he's trying to talk sense into someone who can't understand him."
    a "Mister?!"
    a "{size=50}MISTER-!!{/size}"
    "No responses are spared by the mossy monster, leaving the bear all frustrated."
    e "We can't work if this... guy keeps sitting on our bridge."
    a "Of course! Well, we need to do something."
    e "Maybe we should fight this guy! I think it'll get out if it knows we're here for business."
    a "I- well... We can't kill him. We're here to build something beautiful, not to destroy the nature."
    "Amble exclaims as he furrows his brows, thumb is rubbing against his palm nervously."
    e "Hmm... then should we just wait?"
    a "Well, yeah! You're right, [e]. But, how long is it going to take?"
    "You shake your head, both of you have no idea when will the monster leave."
    menu:
        a "So... what should we do?"
        "Fight the monster":
            e "We'll just fight it until it gets scared and leave, okay? No killing."
            a "Puny friend, do you think that'll work?"
            e "I think so."
            a "Alright then, let's go."
            jump bridgeroot_battle
        "Wait it out":

            e "I think we should just wait."
            a "You're right, puny friend. Killing is not the only option we have here."
            a "In another word, how magnificent that a creature like this is bestowed upon us by mother nature?"
            e "That's really rare I agree."
            a "Alright, if you need some rest, I'll stay and maybe wait until the guy's gone."
            e "Thanks, Amble!"
            jump main_riverside_crossing

label Amble_Voting_Continue_Bridgeroot_Break:
    e "Hey, Amble, is that monster not gone yet?"
    a "Not yet, I'm afraid."
    "You notice the green shaped monster is still sitting on the edge of the bridge, his thin legs swinging in the air as his head veer around idly."
    "Amble sighs as he continues waiting."
    jump main_riverside_crossing

label Amble_Voting_Continue_Bridgeroot_Finish:
    $ quest38.status = 6
    e "Hey, Amble, where is the monster?"
    a "Oh! Puny friend, you're right on time! It just left. I saw him got up and started walking south of the river."
    a "We actually ended up talking to each other for a while. He's a kind friend."
    e "Talking? I didn't know a bundle of moss can talk."
    a "Nah, it's basically me talking myself and he's listening. Isn't that the same thing?"
    e "Well, at least you two got along with each other."
    a "Hah, thanks, puny friend. But we have something else ahead of us now - the bridge! We should get back to construction right now."
    e "Alright, let's get on with it."
    jump Amble_Voting_Continue_Last_Stretch_Start

label Amble_Voting_Continue_Last_Stretch_Start:

    "For the next few hours, you two begin using the masonry mix to stablize the rocks in between these wooden structure you have created."
    "Moments after moments, you stare at Amble's sweaty posture, he's always been so eager to work on this project, and you're glad to see him putting all his effort into rebuilding the bridge between Lusterfield and the goat tribe."
    if bridgeroot.win >= 1:
        "He's been working so hard, that it almost seems like he has forgotten what happened to the green creature you two had just fought."
        "At least that's what you believed, until he turns around in the middle of moving the stone bricks."
        a "My father always taught me not to interfere with the nature's balance, it's truly a beautiful habitat here."
        e "Are you still thinking about that... monster?"
        a "You can't make it a habit to kill wild creatures. We can't. There are consequences, it always comes back to bite us."
        a "[e], it's a gift of the old gods, to see such a creature in this land. I am just sad to see it go."
        "The bear ponders for a moment as he looks down into the water."
        a "We are here to build bridges, aren't we?"
        e "Y-yes, of course, that's why I came here with you."
        a "Then let us continue..."
        "Amble turns around once more, and resumes to his work."

    "You thought comes to a halt as he hands you another stone brick to be stacked, you two have been working so hard, but it doesn't even seem like the construction is close to finished."
    "Almost 5 hours has passed, all the towels Amble has prepared are already drenched in his sweat. You pant heavily, as you see Amble sits on the half-completed bridge."
    "Suddenly, something pokes its head out of the trees behind you. You come to a jolt before readying your weapon behind Amble."
    gt "Uh... what are you guys doing here?"
    "It reveals to be a goat, probably guarding the ancient tree nearby. He's holding his spear cautiously, staring at you two with widened eyes."
    a "We're rebuilding this bridge, my friend. Want to join us?"
    gt "B-but it's been abandoned for years, why do you want to build it all of a sudden?"
    a "It was a beautiful bridge, don't you agree? It'd be a waste to let it dry out from here."
    "The goat says nothing, his eyes squint together as if he was pondering something. But just as you're about to open your mouth, he vanishes from the trees."
    e "Where did he go?"
    a "Probably just left, well. Let's resume our work then."
    "You nod, and begin hauling the next stone brick onto the bridge. Amble does so as he prepares the next rock."
    "It continues for almost an hour, before you are suddenly greeted by another uninvited visitor."
    gt "Hey, that's the lusterfolks building the bridge."

    "It seems to be the same goat that talked to you earlier, except that he's bringing a few more of his friends along the way."

    gt "Do you guys need some help? Maybe we can lend a hand, or something."
    a "Oh, sure! Of course. Please do, my friend. It's our bridge."
    e "A-amble, are you sure we can... allow that?"
    a "I'm sure, puny friend, they'll save a lot of time and effort for us."
    if bridgeroot.win >= 1:
        "He smiles with a lopsided grin, probably the first time since you two had fought the moss monster."
    else:
        "He grins. It puts a smile on your face to see him genuinely happy."
    "The goats all jumps into the water as they murmur among themselves, Amble leads them to the bridge with ease as he instructs them what to do."
    "Some of them had started working already, and soon the rest of you join in, on the other side of the bridge. Amble hands them the rock with a relieved face."
    "Surprisingly, the goats are eager to help, you'd think they might be opposed to building it, but they seem to be wishful to see the bridge back to its previous glory."
    "Amble pats your back as he tumbles the rest of the rocks across the river. It could have taken days, if not a week to finish the bridge, but with the goats it seems almost a breeze to blow through."
    "For the next few hours, some goats joins and some leaves to return home, but you can see the progress very clearly, as both ends of the bridge slowly reaches to the center."
    "At least the masonry mix you've crafted is sufficient to do its job, filling in the gaps between stone bricks."
    "Amble seems pleasantly surprised by how quick the bridge seems to be finishing, with only a few rocks remaining, it's only a matter of time before the bridge can be walked across once again."
    a "Well, that's the last one."
    "Amble sighs as the rock settles perfectly onto the cracks, the magical material does help quickly sealing the deal with its extra stability and cohesion."
    "Everyone cheers, including you and the goats, after hours and hours of work, it was quite amazing to see what the two village had before finally reinstated."
    gt "Haah! Damn, we didn't know it'd be this easy... it had been an honour."
    gt2 "Well, you've got good hearts in ya. The bridge will help both sides a lot, no matter whatever happens to the votes."
    "You nod, receiving a few thumbs up from the goats."
    "They are laughing amongst themselves as they soon depart."
    a "Farewell, my friends."
    "Amble stands pridefully as he waves goodbye to the goats, as you stand by his side."
    a "Well, here's the bridge. Doesn't it look wonderful, puny friend?"
    e "It does! It's been a great journey working with you, Amble."
    a "True, and the goats too. I was pleasantly surprised they're such an enthusiastic bunch of fellows. Well, I guess that settles it."
    e "Ah, did you decide what you're gonna vote?"
    if quest37.start_date + rahim_vote_duration >= timenow.day:
        a "Yeah, I'm gonna have to say sorry to Lot a lot after the vote."
    else:
        a "Well... I changed my mind. But it's already past the vote day."
    "You nod."
    a "Anyway, don't step on the bridge too soon, the mix's not dried yet."
    e "Of course, well. It's been an honour for me too."
    a "Yes, well. Maybe if we have some fun projects with Jog later on we'll be sure to include you, [e]."
    "You put on a wide grin."
    if bridgeroot.win >= 1:
        "It seems Amble is putting behind all matter with the bridgeroot. You're sort of glad he did so, at least what happened might not have changed him as much."
        "Though, perhaps it's only because it's something he doesn't like to talk about."
    "You two part way, as Amble finishes decorating the bridge."
    if guard_tree:
        $ timenow.addTime(0,6,10)
    else:
        $ timenow.addTime(0,10,30)
    $ riverside_crossing_finished = True
    $ QuestFinish(quest38)
    jump main_riverside_crossing

label Ole_Voting_Opinion:

    e "Ole, how do you think about the vote that's coming soon?"
    o "The voting day? Well, let's say I didn't expect Rahim to actually hold something like that."
    e "Uh... Why not?"
    o "For starter, he's not fond of goats, that was kind of an obscure fact."
    "Ole raises his voice, telling you that he's clearly sarcastic."
    o "I guess he has had a change of heart, after what transpired when he shouted at Furkan."
    e "Yeah, did you hear it too?"
    o "Who didn't? Rahim has such a rough shouting voice, you'd be surprised if someone in the village didn't hear it."
    o "Anyway, kiddo. What were you about to ask?"
    e "I just wanted to ask, uh... how would you vote?"
    o "I'm rather confused if you're asking for my opinion or an instruction."
    o "Let me assume it's opinion. Well, I haven't decided yet, but in most scenarios I can foresee, I would vote no."
    o "It's not much of a problem with the goats essentially, but their guards had been giving me a headache I'd rather not ally with them."
    e "Hey, but Seb was quite adament about this whole change, right?"
    o "I know his reasons."
    o "Seb's going to hate me for that, but it's true. The goats were really nosy about where our goods come from, well before everything took a bad turn."
    e "But, you trusted me, even at the first day we met."
    o "Ha, well. You have no ulterior motives. It was just too easy to see what's your heart's made of."
    e "Oh... my heart?"
    o "Mmm-hmm, that's why we let you stay, it didn't take a lot to see through you, but it's not a bad thing, kiddo."
    e "Ole, are you serious."
    o "Well, that's the fun right. Much like, I already know why you're asking me about the vote."
    "You notice Ole staring deep into your eyes as he leans closer."
    o "Because, you wanted to see if I have the same opinion as you do! Isn't it?"
    e "That's very insightful, but why would you vote otherwise, firstly?"
    o "I said it's about the goats, but it was not all of them, just one."
    o "Their shopkeeper, Gwyddyon, when we first made our trade deals, and I was away, he took advantage of Seb."
    o "Not the other advantage. But by strangling all source materials for all stones and crystals, he backed Seb into a corner-"
    "Ole shifts his gaze around, weirdly he seems unconfortable with the words he has spoken."
    o "At the end of the day, we got the worst end of the deal. And we ended up working together, but not out of mutual benefits, but obligations."
    o "We've worked this way for some time, before our contact was severed, naturally. And after all these years, Seb might have forgotten about this, but I didn't."
    "He turns his attention back to you, with a significantly more confident stare, ones that feels as if he staring into your very being."
    "You naturally squirm, even as a friend who rescued you on your first day in this world, he seems... too ambitious for the Ole you knew."
    o "So, if we have to make a better deal, maybe I should know fully what his intention is."
    o "We have already arranged a meeting in Haskell's place beforehand, just three days before the voting begins."
    o "I'll be there talking with Gwyd. And Haskell will be... some sort of mediator."
    o "But, before that, I need your help to, perhaps make the negotiation smoother."
    e "Am I the only one who can do it?"
    menu:
        o "Of course, kiddo. The only question is, are you going to help?"
        "Help Ole":
            e "Sure. How do I get started?"
            o "Well, that's very easy, unless Gwyd's not being coperative, which I can already envision him so."
            "The lizard steps away and cleans his towel, before leading you to your table."
            o "In the old trade route we- {i}agreed{/i} upon, we exports the herbs and harvests and some potions. And them with the assistance of the dark forest, exported building materials, rocks and minerals."
            o "And it will probably stay the same if we ever cooperate again."
            o "So, there's something I need you to do, which involves something rather dangerous."

            if quest35.status == True:
                e "Okay then, but you're being pretty suspicious lately, Ole."
                if pirkka_negotiate:
                    o "Maybe, but you didn't know how badly we got out of that deal."
                    o "We were basically working under him, as the majority of our profit are just sent directly to his magic shop."
                    o "And Haskell was rightfully pissed too."
                else:

                    o "That's not true, even if we're counting Pirkka's prose."
                    e "Oh we are surely counting that."
                o "Well, the truth is, there was something I noticed while engaging with the bandits."
                e "What's it?"
                o "I happened to run into the supplier of Gwyd's shop. That was one of the reasons I talked with the bandits after all, to track where his products come from."
                o "If we need to end up on the better end of the deal, well, Gwyd has to need us more than we need them."
                o "And that means, that supplier needs to stop, for lack of a better word, supplying Ardent Cauldron."
                e "Is that necessary? Can we not, talk this over?"
                o "Trusting him like Seb does was a mistake, maybe we need to take a form of revenge to make Gwyd reconsider his position a little better."
                "Ole gives you a cheeky wink, one with a warm intention, but also a tint of craftiness."
                e "So, what should I do?"
                o "The supplier will be present in the negotiation. They had heard about what happened in Lusterfield too, so I think they'll be discussing a new contract."
            else:


                e "What does that mean, Ole-"
                o "Through my own observation, I've got to know some mysterious individual that supplies Gwyd his everyday goods."
                o "If we need to end up on the better end of the deal, well, Gwyd has to need us more than we need them."
                o "And that means, that supplier needs to stop, for lack of a better word, supplying Ardent Cauldron."
                e "Is that necessary? Can we not, talk this over?"
                o "Trusting him like Seb does was a mistake, maybe we need to take a form of revenge to make Gwyd reconsider his position a little better."
                "Ole gives you a cheeky wink, one with a warm intention, but also a tint of craftiness."
                e "So, what should I do?"
                o "Gwyd meets up with his supplier in the morning, they had heard about what happened in Lusterfield too, so I think they'll be discussing a new contract."
                e "Wait, how did you know so much things?"
                o "It's a secret, kiddo."
            o "So, you'll need to talk to Gwyd about his latest product, try to get some information about it, and then, we'll probably try to one-up him, and make something much more impressive for the supplier."
            o "The hardest part is to probe some information out of him. From what I've already experienced, you only have one chance before he gets nosy. So don't mess it up."
            e "Alright, I'll try my best to poke around, for whatever's worth."
            "Ole gives you a smile, before turning back his attention to the dressers."
            o "I trust you, [e], both for finishing the task, and for indulging with my own affair."
            e "You saved my life, right over at the green forest when I was passed out. And I'll forever be indebted."
            o "Yeah? Forever?"
            "He leans in, just one inch short of being uncomfortably close. And you look into his eyes, uncertain yet attentive."
            o "Don't kid, [e]. You'll need more than forever."
            "The whole world seems to have taken a pause at this moment, your hands touch without you both knowing, and it naturally clenches against each other."
            "His mouth hangs agape slightly, and you can feel his breath, directly coming out of his mouth as he gasps in surprise or confusion."
            "Something is pulling you into his scaly embrace, you can't tell what it is exactly, but right now everything suddenly goes blurry, except for Ole."
            "With a quick blink, Ole snaps back into reality, and you feel his scaly hand releases yours, and instead quickly pinches onto your red cheeks."
            o "Something's on your face."
            "He lets go of your soft cheeks, nudges his fingers for quite a few times, as you stand still, still processing what had happened."
            "Some of Ole's warmth lingers as your palm feels for your cheeks. as if you are still being pinched by his plump claws, and that small action has made your heart racing so fast."
            e "Hey, Ole-"
            o "Get going now, kiddo."
            "Ole returns his attention to the furniture, scrubbing onto another dark spot so hard that he's scraping off the paint from the dresser."
            $ todaydayofweekfromolemeeting = weekdictionary[weektuple[int((timenow.day - 4 + rahim_vote_duration) % 7)]]
            $ QuestBegin(quest39)

            $ quest39.qProgress(_("Complete the quest before Ole meets with Gwyddyon on ") + todaydayofweekfromolemeeting)
            $ quest39.qProgress(_("Collect information about a secret product from Gwyddyon"))
        "Maybe Later":


            e "W-well, maybe later?"
            o "Alright, then I'll keep on scrubbing on the dresser."
            "Ole smiles, before returning his attention to his own towel."

    jump Ole_Normal_Talk

label Ole_Voting_After_Gwyddyon:

    e "Hey, Ole. I'm back... from asking Gwyd some questions."
    o "Did you find anything useful?"
    if type(ole_got_gwyd_answer) == int:
        menu:
            e "Hmm..."
            "Tell Ole about Gwyd's secret":
                $ ole_got_gwyd_answer = 1
                e "Actually, Gwyd's supplier wanted a harp at the meeting."
                jump Ole_Voting_Got_Gwyd_Answer
            "Pretend you don't know":
                pass
    e "Well... I don't think I found anything that helps find your supplier... his lips were pretty tight about it. Just overall very sensitive."
    o "That's the Gwyddyon I know. Don't worry, you've tried your best, kiddo."
    e "So, what are you gonna do?"
    o "Now's the time I try my best too. I'll go to the meeting with Gwyd. Hopefully what I had already prepared will prove sufficient."
    e "I'm sorry I couldn't help more, Ole."
    o "It's fine, not really your fault that Gwyddyon was so stingy. But well, if the plan falls apart, I guess there's no use for me to change my vote."
    "You nod, as Ole pats your shoulder softly."
    o "But, that doesn't mean you're still a helpful friend to me. No matter what the vote will end up."
    "He smiles as the lizard hovers his hand over your hair, and scruffles it playfully."
    $ QuestFinish(quest39)

    jump Ole_Normal_Talk

label Ole_Voting_Got_Gwyd_Answer:

    o "A... A musical harp?"
    e "Yeah, the one you play with finger, I guess. I'm not sure why he wanted that though, Gwyddyon was confused also."
    o "Hmm..."
    "Ole ponders for a moment, tapping his finger at the dresser."
    o "Perhaps he wanted to test if Gwyd understands his materials. He didn't want him to just put his products on the shelves and then forget about it."
    o "Maybe I'm stretching it, maybe he just wants a harp. In this case, we can make one ourselves, we may have even secured the deal if ours are better than what Gwyd comes up with."
    e "I guess so. But where can we find a harp...?"
    o "Find? No, no. Judging by what you said, we will need to make them from the supplier's materials."
    o "Lucky for us, I happen to know the entire catalogue of the products he sells."
    e "But we don't even know where is the supplier. Even if we know, why would he sell his products to us."
    o "You're right, maybe we'll end up buying from Gwyd, without him knowing what they're used for."
    o "Alright, we'll settle onto this first. But how can we make a Harp, we need much more than these materials."

    if quest35.status == True:
        menu:
            o "I've seen pawned musical instruments before, but making one myself... I'm not so sure."
            "Ask for Pirkka's help":
                $ ole_votequestpirkka = True
                e "Maybe, we can ask Pirkka. He's a bard, right? He must know about Lutes and Harps a little."
                o "Ah! You're right, [e]. Well, after what happened with his prose, I hadn't even given him a proper apology."
                e "I'm sure he doesn't hold grudges."
                o "Maybe, we'll see. Where is he staying anyway, still in Nocturnal Trunk?"
                e "I suppose so."
                o "Alright then, give me a second to prepare the catalogue and some coins, we'll go when we're both ready, okay?"
                "Ole smiles, and swiftly rushes up the stairs."
                $ ole_votequestminute = timenow.anal() + 10
                $ quest39.status = 4
                $ quest39.qComp(__("Get ready with Ole"))
                jump main_kingspawn
            "Do it ourselves":
                $ ole_votequestpirkka = False
                pass

    jump Ole_Voting_Doing_Ourselves

label Ole_Voting_Doing_Ourselves:

    e "I guess we can do it ourselves? Do we have any clues about the materials we have?"
    o "Mmhmm... I have the list of the current exports they're sending to Gwyddyon."
    e "Damn, Ole. You sure did a lot of research on that supplier you don't even know."
    o "Well, the bandits hold the only route from the North. So it only takes a few... persuasions."
    o "But that doesn't matter. The only thing that matters is the materials. If the supplier wants us to utilise his materials, then we should start from looking at his materials."
    o "It'll take a while to research, I have previous records of old string instrument we got from the shop, hopefully that'll get us a lead."
    e "It sounds like some heavy work, can I help?"
    "Ole ponders for a moment, and then smiles awkwardly as he scratches the back of his neck."
    o "I should handle those researches myself, but please do come back once I'm done with finding out which materials we need."
    e "A-alright. I'll trust your judgement."
    o "Thank you, [e]."
    $ quest39.status = 4
    $ quest39.qComp(__("Wait for Ole to finish his research"))
    $ ole_votequestminute = timenow.anal() + 630
    jump main_kingspawn

label Ole_Voting_Finding_Number:

    e "Hey, Ole. Did you find which materials we need?"
    o "Yeah, after studying for the past day I feel like I've... become a instrument expert."
    o "Like the strings-"
    s "Yo, what'chu talking about?"
    show sebas normal at l2
    show sebas normal:
        linear 0.5 xalign -0.55
    "Sebas suddenly pokes his head between the both of you. Turning his head to both of you curiously."
    show ole understand:
        linear 0.5 xalign 0.5
    e "Uh..."
    o "We're reading books, do you want to chime in?"
    show sebas shocked
    s "Aw, don't count me in! I don't want to get dragged in your '{i}boring yourself to death session{/i}' for 10 hours."
    o "You sure? I've got some book recommendations for new beginners."
    s "I'll go play wit-... by myself. Hey, have fun with your books! Don't let me get between you two!"
    s "-Good luck! Enjoy your books, my big O and [e]!"
    "Sebas exclaims as he retreats from between you and returns to his counter."
    show sebas normal at l2 with move
    e "Uh, Ole. Is it something we can't talk about?"
    "You whisper, as Ole leans in to listen."
    o "No, Seb can know about it. I really was reading a book about instruments last night. There were a lot of crucial information."
    e "Crucial information?"
    o "Yes, well. Let's cut it short, alright. I think basically we'll need wood materials and strings."
    show ole normal
    o "I've already gotten myself Resonator Gems from deep inside our storage, 3 of them to be exact."
    o "Elderwood sounds perfect for the harp we need to make, but there are some choices we'll need to make here."
    o "For the strings, we can either use Nylon or Crystal strings. Nylon's sound is more balanced, smooth. While Crystal strings have a richer, more resonant and harmonic sound."
    menu:
        o "From the information I have right now, I really don't know which of them is better. Just that Nylon is cheaper in Gwyd's shop."
        "Nylon":
            $ ole_voting_string = "Nylon"
            e "Nylon? It sounds cool."
            o "[e], we need the sound of the instruments, not the words themselves."
            o "But I don't have a better idea to reject your choice, so Nylon it is."
        "Crystal String":

            $ ole_voting_string = "Crystal String"
            e "Maybe crystal strings? I think it'll look awesome."
            o "Crystal strings... personally I have no problems of it, myself."
            o "That sounds solid, so Crystal it is."
    e "Ah, so how much do I need?"
    o "That's the hardest part. I don't know how many we'll need."
    o "The only thing I know is, the string number hovers from... 8 to 15."
    o "And we'll need at least two more elderwood than strings, but the most wood we can use is also 15."
    e "That was such a huge range, how do we know the exact number."
    o "I'm not sure, but I guess we can try. We'll settle on a specific number, and after crafting it we can always test whether the number should be is higher and lower."
    o "Lucky for us, I read up a lot about the Harp, so I know what the perfect harp sounds like, but it looks like we'll need to play it out first."
    o "But don't you worry, [e]. We can always demolish the harp and take back the materials."
    e "Wait, we can?"
    "Ole nods."
    o "Yes, the only thing is, we have only three resonator gems, they cannot be retrieved. So there are only 3 chances before we send a subpar version of the harp."
    o "Let's hope the supplier doesn't recognise the subpar harp immediately."
    e "Alright, I hear you."
    o "Here are the three resonator gems. Take good care of them, alright?"
    o "Indeed, if you need to make one, we can create a recipe together so you can make a harp with your desired numbers."
    o "After that, you can come back and I'll test it out. I can probably tell if the harp sounds good, and we'll go from that."
    e "Alright."
    $ quest39.status = 5
    $ addItem("Resonator Gem", inventory, 3)
    $ ole_voting_string_name = LookForItemName(ole_voting_string)
    $ ole_voting_max_wood = 15
    $ ole_voting_min_wood = 9
    $ ole_voting_max_string = 15
    $ ole_voting_min_string = 8

    if ole_voting_string == "Nylon":
        if renpy.random.random() > 0.5:
            $ ole_voting_string_answer = 8
            $ ole_voting_wood_answer = 14
        else:
            $ ole_voting_string_answer = 11
            $ ole_voting_wood_answer = 15
    if ole_voting_string == "Crystal String":
        if renpy.random.random() > 0.5:
            $ ole_voting_string_answer = 9
            $ ole_voting_wood_answer = 15
        else:
            $ ole_voting_string_answer = 10
            $ ole_voting_wood_answer = 12

    jump main_kingspawn

label Ole_Voting_Starting_Recipe:

    e "Ole, I think I'm ready for the recipe of the harp."
    if LookForItemNumber("Resonator Gem", inventory) == 3:
        $ ole_voting_wood_num = 12
        $ ole_voting_string_num = 12
        o "Alright, remember, the numbers of the wood and string should be between 8 and 15."
    else:

        o "From what we've gathered..."
        o "Elderwood should be between [ole_voting_min_wood] and [ole_voting_max_wood]."
        o "[ole_voting_string_name] should be between [ole_voting_min_string] and [ole_voting_max_string]."
    o "It's just that we'll always need at least two more pieces of wood than the strings."
    o "So, let's decide the number of the wood first."
    jump Ole_Voting_Making_Recipe_Wood

label Ole_Voting_Making_Recipe_Wood:
    $ rrrand = renpy.random.random()

    if ole_voting_wood_num > ole_voting_max_wood:
        $ ole_voting_wood_num = ole_voting_max_wood
    if ole_voting_wood_num < ole_voting_min_wood:
        $ ole_voting_wood_num = ole_voting_min_wood

    if rrrand > 0.2:
        o "So, we'll need [ole_voting_wood_num] pieces of wood, right?"
    elif rrrand > 0.4:
        o "Maybe [ole_voting_wood_num] pieces?"
    elif rrrand > 0.6:
        o "Alright, is [ole_voting_wood_num] pieces of wood correct?"
    elif rrrand > 0.8:
        o "For elderwood, we'll have to buy... [ole_voting_wood_num] pieces?"
    else:
        o "Oh, so you think [ole_voting_wood_num] would be enough for elderwood?"
    menu:
        o "Should we change the number? Or should we stick with [ole_voting_wood_num]?"
        "+3":
            $ ole_voting_wood_num += 3
        "+1":
            $ ole_voting_wood_num += 1
        "The number is Right":
            e "I think the elderwood number is right."
            o "Oh, good. Let me write that down... The next is the string."
            jump Ole_Voting_Making_Recipe_String
        "-1":
            $ ole_voting_wood_num -= 1
        "-3":
            $ ole_voting_wood_num -= 3
        "Cancel":
            e "I think I'll need some moment to think, Ole."
            o "Sure, take your time, kiddo."
            jump main_kingspawn

    jump Ole_Voting_Making_Recipe_Wood

label Ole_Voting_Making_Recipe_String:
    $ rrrand = renpy.random.random()

    if ole_voting_string_num > ole_voting_max_string:
        $ ole_voting_string_num = ole_voting_max_string
    if ole_voting_string_num < ole_voting_min_string:
        $ ole_voting_string_num = ole_voting_min_string

    if rrrand > 0.2:
        o "So, we'll need [ole_voting_string_num] [ole_voting_string_name], right?"
    elif rrrand > 0.4:
        o "Maybe [ole_voting_string_num] [ole_voting_string_name]?"
    elif rrrand > 0.6:
        o "Alright, is [ole_voting_string_num] [ole_voting_string_name] correct?"
    elif rrrand > 0.8:
        o "For [ole_voting_string_name], we'll have to buy... [ole_voting_string_num]?"
    else:
        o "Oh, so you think [ole_voting_string_num] would be enough for [ole_voting_string_name]?"
    menu:
        o "Should we change the number? Or is [ole_voting_string_num] [ole_voting_string_name] alright?"
        "+3":
            $ ole_voting_string_num += 3
        "+1":
            $ ole_voting_string_num += 1
        "The number is Right":
            e "I think the [ole_voting_string_name] number is right."
            o "Oh, good. Let me write that down... Alright, I think it's good to go now."
            "Ole gives you the recipe with the number you have."
            if LookForItemNumber("Resonator Gem", inventory) == 3:
                e "Wait, the recipe... is that a goat's pattern on the harp?"
                o "Yeah, I learned that from a book from the goat tribe long ago, I'm not sure if removing that has any effect on the Harp so I decided to keep it."
            $ harprecipe = Recipe(harp_item, resonatorgem_item, 1, elderwood_item, ole_voting_wood_num, fyi(ole_voting_string), ole_voting_string_num)
            $ harpcheck = next((x for x in discoveredrecipe if x.product.img == "Harp"), None)
            if harpcheck == None:
                $ discoveredrecipe.append(harprecipe)
            else:
                $ harpcheck.num2 = ole_voting_wood_num
                $ harpcheck.num3 = ole_voting_string_num
            $ quest39.status = 6
            if LookForItemNumber("Elderwood", inventory) < ole_voting_wood_num or LookForItemNumber(ole_voting_string, inventory) < ole_voting_string_num:
                o "Oh, and remember to buy some materials from Gwyd. It seems there's not enough of that from your recipe."
            "You nod, and head your way outside."

            jump main_kingspawn
        "-1":
            $ ole_voting_string_num -= 1
        "-3":
            $ ole_voting_string_num -= 3
        "Cancel":
            e "I think I'll need some moment to think, Ole."
            o "Sure, take your time, kiddo."
            jump main_kingspawn

    jump Ole_Voting_Making_Recipe_String

label Ole_Voting_Testing_Harp:
    if ole_votequestpirkka == False:
        $ ole_voting_string_answer = 8
    $ removeItem("Harp", inventory, 1)
    e "Hey, Ole. Can you test out this Harp?"
    o "Oh! Alright, then let's go to your room."
    scene black with dissolve
    pause 1 
    scene bedroom with dissolve
    show ole normal with dissolve
    "Upon entering your bedroom, Ole immediately takes the hefty harp from your hand, he pulls out a few notes from his pocket and begins tuning the harp."

    o "T-this one here... gotta loosen that string."
    o "Hmm..."
    "He continues for a while as you wait patiently."
    "And then, he strums a few chords at each string, listening closely as he checks the scrambled paper."
    if ole_votequestpirkka == True or (ole_voting_wood_num == ole_voting_wood_answer and ole_voting_string_num == ole_voting_string_answer):
        jump Ole_Voting_Good_Finish
    else:
        if LookForItemNumber("Resonator Gem", inventory) == 2:
            o "Nope..."
            e "Anything you found?"
            o "I did find something, but nothing too promising."
            "He continues testing out the tone and sound. Working almost like a professional now."
            e "Damn, Ole. Have you really not learnt any instruments at all? Your hand looks so skilful turning around these buttons."
            o "It's not that impressive I assure you. Just that when you've worked in a general store for so long, you start to figure out that every sort of gadgets has their own common method to disect them."
            o "And once you sort that out, reading manuals and books about this specific topics just makes the rules crystal clear."
            o "Learning this helps you verify any gadgets and goods you get from the pawn customers, afterall, you'll have to take everything your customer throw at you, right?"
            o "For example, if you tweak this one... there's should be a sound, and squeaking doesn't count."
            o "And this one should be a higher note."
            "He strums another chord, but it's almost the same as the previous string, if not lower."
            "The lizard sighs playfully as he takes a quick glance at you."
            "He proceeds to check the other strings, noticing that the first few are already wrong, it doesn't take long for him to finish."
            o "So, the harp's good, but not as perfect as we need it to be."
            "You gulp, it's quite disappointing to hear, but Ole's reassuring voice makes you feel a little better."
        else:
            o "No... this one isn't it."
        e "What's wrong with it?"
        if ole_voting_wood_num > ole_voting_wood_answer:

            o "Well, it seems the sound is way too sturdy. And do you hear that squeak?"
            "He says as he brushes his finger across the strings."
            o "There's too many wood. Perhaps, the right number should be lower."
            e "So, it should be lower than [ole_voting_wood_num]."
            $ ole_voting_max_wood = ole_voting_wood_num
            $ ole_voting_wood_num -= 1
        elif ole_voting_wood_num < ole_voting_wood_answer:

            o "I don't think the wood is supporting the strings too well. You see?"
            "He points at the loose string, it almost seems as if the strings are about to fall off any seconds."
            o "We'll need more wood to support, probably tighten the strings up a little more."
            e "So, it should be higher than [ole_voting_wood_num]."
            $ ole_voting_min_wood = ole_voting_wood_num
            $ ole_voting_wood_num += 1
        else:
            o "I think the wood is built perfectly, there's not much more a problem here, but..."
        "You nod as he turns to the glistening strings."
        if ole_voting_string_num > ole_voting_string_answer:

            o "Maybe there shouldn't be too much strings here, the spacing between them are too crammed."
            "He plays the harp once more, you can hear a lot of echoes meshing together."
            o "Yep, definitely a problem. Unless the supplier wants to strum ten chords at once, I think we should lower than the number of strings here."
            e "So, it should be lower than [ole_voting_string_num]."
            $ ole_voting_max_string = ole_voting_string_num
            $ ole_voting_string_num -= 1
        elif ole_voting_string_num < ole_voting_string_answer:

            o "I think the strings are too sparse, the air might affect how the sound turns out."
            e "So, it should be higher than [ole_voting_string_num]."
            "He nods."
            $ ole_voting_min_string = ole_voting_string_num
            $ ole_voting_string_num += 1
        else:
            o "However, the strings are perfect as it seems."
        if checkNoShopItem("Resonator Gem"):
            e "Well... that was the last gem I have."
            o "It's all good. The harp is useable, and I sort of start to understand why the supplier insisted on Gwyddyon making a harp like this."
            o "There were a lot of nuances and nitty-gritty hidden in the building of a harp, I was even pleasantly surprised you can make one so quickly."
            e "I did, but it wasn't too perfect and I've wasted your gems."
            o "Hah, it's all good. Regardless of how the meeting goes, I think I've learnt a lot from this, from both the books, and you."
            e "Really? I didn't think I've done that much."
            o "Yes, you've got my vote, kiddo."
            e "Thank you so much, Ole."
            "He scruffles your hair as he packs away the harp."
            e "Are you not going t-"
            o "Here's the rewards for your help. Be sure to spend them wisely."
            o "Oh, the harp. I'm putting it away. It's not as wise to present up a subpar harp to someone who didn't ask for that."
            e "Aw..."
            o "Don't worry, kiddo. With this one, maybe I'll learn to play some Harp for myself once in a while."
            "He speaks softly, patting your shoulder for a few times."
            $ pc.gold += 500
            $ ole_gwyd_success = -1
            msg "You received 500 gold from Ole."
            $ QuestFinish(quest39)
        else:

            e "Alright, I got it. I'll adjust the number."
            o "Wait, one second."
            "Ole holds his harp and suddenly demolishing it into different pieces of Elderwood and [ole_voting_string_name]."
            e "Wait, how did you do that?"
            "He hands you the remaining materials as the resonator gem inside is easily shattered."
            o "Nothing fancy, these materials are just reuseable."
            e "A-alright, thank you, Ole."
            $ addItem("Elderwood", inventory, ole_voting_wood_num)
            $ addItem(ole_voting_string, inventory, ole_voting_string_num)
            $ quest39.status = 5
        "Ole waves at you as he walks out of the door."
        jump main_bedroom

label Sebas_Voting_Ask_Where_Ole:

    e "Hey, Seb. Where's Ole?"
    s "Uh, going on a meeting with Gwyddyon, that's what he told me. He's coming back late tonight though."
    if quest39.status:
        s "Roomie, I think he's bringing a Harp over there, my big ole Ole's playing music now, haha."
    jump Sebas_Normal_Talk

label Ole_Voting_Asking_Pirkka:

    e "Should we go now?"
    o "Yes well, I've got everything ready, hopefully we won't bother the bard too much."
    "You nod as Ole waves to Sebas, who's sitting on the counter rather boredly."
    scene black with dissolve
    pause 1 
    if isNight():
        scene nocturnaltrunk_night with dissolve
    else:
        scene nocturnaltrunk with dissolve
    show ole normal at l1 with dissolve
    "And soon, you arrive to Nocturnal Trunk, Cane walks up swiftly to greet the both of you."
    show cane normal at r1 with dissolve
    c "Hiya, rare pair to see 'ere, anything I can help?"
    o "Mhm... may I ask if Pirkka the bard is here?"
    c "Hah, do I look like his caretaker or somethin', caus' that'll probably be a better earning job than working 'ere."
    c "Did yer two lads hear how much fuzz that minstrel's causing here? Haha, business' been better than ever."
    c "Well, 'nough of the ol' blabbering, m' lads. He's right upstairs, yer gonna hear him soon enough."
    o "Thank you, Cane."
    "The tavernkeeper smiles as he returns to scrub the tankards with his towels."
    hide cane normal with dissolve
    scene nocturnaltrunk_upper with dissolve
    "As soon as you walk upstairs, you spot Pirkka near the fireplace, entertaining a small crowd with his lively tunes."
    show ole normal at l1 with dissolve

    p "Well met, m' friends! What brings you to my corner of the world today?"
    show pirkka normal at r1 with dissolve
    p "Corner being, the generous Cane's newly refurbished floor. I'm slowly gettin' to love this tavern."
    p "Though, everyone's been talking about the alliance accord, so I might as well, strum {i}a chord{/i} on my lute."
    "His jokes are corny as always, but nonetheless you still laughed wholeheartedly with Pirkka."
    p "So... how may I help you?"
    e "We're looking to ask some question about a harp, and we've heard you might be able to help."
    o "We thought your musical expertise might come in handy."
    "Pirkka's eyes light up with excitement, and he sets his lute aside."
    p "A harp, ye say? 'Tis but a noble instrument, indeed. As what we say among the minstrels, a good harp befits a soul in search of beauty and harmony."
    menu:
        p "Well, I {i}harp-pen{/i} to know some gists of making these fine instruments, but {i}string{/i} me along, what will be the story of this harp."
        "I wanted to learn to play Harp":
            e "Well, I actually wanted to learn to play harp, but there's nothing like that anywhere else."
            "Ole stutters as he glances at you, probably a little shocked as you speak."
            p "Admittedly, I'm not an expert on harp, I've been known to strum a harp or two in my time. Perhaps you'll one day sing a great song with me."
        "Ole's supplier wanted it":

            e "Ole's supplier for his shop wanted a harp, it's a long story actually."
            p "What a strange requirement for your supplier, after all, a harp isn't something an ordinary person might be interested in."
            o "Of course. That's why we thought of asking you."
        "Remain Silent":

            "You remain silent and wait for Ole to speak."
            o "It's kind of embarrassing to say, but it's for a friend who's really into harp."
            p "Oooh, a friend? Someone significant?"
            o "Can't say if he's significant enough by your standard, but can you help us make one?"
    "Pirkka chuckles softly and nods, his fingers tapping a gentle rhythm on his knee."
    p "It's a certain surprising development since the last time we met, Misters. But I can feel we'll mesh together perfectly."
    p "Crafting a harp is like coaxing music from the heart of the wood itself, now, tell me, what kind of harp are you looking to create?"
    o "Just one that you think is perfect, we're not experienced enough to pinpoint which kind suits the best."
    p "Aye, crafting a harp requires patience and a keen eye for detail. The wood must be chosen with care, resonating with the melodies that lie within."
    p "And the strings… ah, the strings are like the very threads of fate, binding the instrument to the soul of the musician."
    p "Different materials weaves together to make for music in different tones. Are you sure {i}any{/i} materials will suit you?"
    o "Well, we don't have all materials in the world, but here's the materials we have."
    "Ole hands Pirkka the catalogue he wrote down a while ago, containing all materials that the supplier sells to Gwyddyon."
    "Pirkka leans forward, his expression thoughtful, as if pondering the possibilty of each combination."
    p "Crystal strings... moonstones, elderwood... enchanted pearls?"
    p "These are... some exotic materials you have there, Ole."
    p "I'd suggest you use the crystal strings, some people might use silk or nylon but they're not easily tuned for a mellow and warm sound."
    p "Elderwood can provide a rich sound and reverb for the harp, it can be tergid enough to support these strings, oak will suffice if you can't find enough elderwood."
    p "You'll need some small resonator gems also, that'll vibrate upon the lateral side of the harp."
    p "These are the basic materials you'll need for a traditional harp, well, if you're not looking for anything too fancy."
    o "What about the numbers? Can you help us figure out how many of these materials we need?"
    "Pirkka ponders for a moment, before he asks for Ole's pen and drawings on the catalogue Ole gave him."
    "With a couple of strokes, he drew a small harp, and begins counting how many strings he has drawn."
    p "These are the general numbers that'll fit your harp."
    e "Thank you, Pirkka, for the advice."
    p "'Tis my pleasure to assist, dear friends. After all, you've been very helpful in retrieving my dear prose."
    if pirkka_negotiate:
        p "And I'd have loved a better deal than what we had the other day, well. Consider it a lesson learned."
    else:
        p "I've even written songs about our story, it's a memorable ones, but nonetheless fantastic."
    o "Thank you so much, Pirkka. I'm sorry for both your troubles the first time we met. May this compensates for your favour."
    "Ole hands Pirkka a pouch of gold, but he simply rejects and waves the bag away."
    p "You're pulling on my heartstring on this one, but no. Consider it my thanks for the prose, they're one of the few things in this land that golds cannot buy."
    "Pirkka smiles as Ole puts away the gold."
    o "Well, you're leaving me restless, Pirkka. How else can I repay you?"
    p "How about, you start spending some times of your days to come take a seat, I'll play you a nice song."
    p "I'd like to get to know some friends around the village. And both of you are worth knowing more, might I say."
    o "I don't come to the Tavern too often, but if that's what floats your boat, I'm down."
    e "Me too."
    "Pirkka picks up his lute again, and strungs a few chords."
    p "May your hands craft a harp that weaves dreams into melodies, and may the muse bless your efforts."
    "With his soft voice echoing in your ears, you and Ole bid farewell to Pirkka."
    scene black with dissolve
    pause 2
    if isNight():
        scene lusterfield02_night with dissolve
    else:
        scene lusterfield02 with dissolve
    e "Ole, what should we do now?"
    o "Gathering materials, of course. You'll just need to buy the silk and elderwood from Gwyddyon's shop. Take a look at the numbers..."
    o "And I'll take care of the resonator gems, I don't think Gwyd sells them directly so I'll have to source from other places."
    o "But that's the plan. Luckily Pirkka gave us the exact numbers we need."
    e "Yeah, he's very helpful."
    o "Mhmm... I didn't expect him to ask us to listen to his songs exactly, I'm not one for music."
    e "Well, maybe you'll grow to love it, I think he sings very well."
    o "That I don't doubt, mhmm."
    "Ole raises his head once more, his scaled hand lands onto your shoulder with a certain weight."
    o "I'm so sorry for getting you between all of these, after getting the harp done, I'll handle everything from here."
    e "We're in this together, don't we? You can always count on me if you need anything."
    if ole_affection > 15:
        "He chuckles, perhaps Ole didn't think that as the helper he had always been, one day he'd get someone by his side."
        "Maybe it's been a while since he's got this feeling, the same as you do."
        "Right now, everything's quiet and serene, but perhaps that's what it takes for you to fall for someone like that..."
        "Your heart pumps faster and faster, just as you see your own reflection in his eyes, there were so much things you want to say, all emotion scatters around your head, Appreciation, admiration, embarrassment... nervousness, love..."
        "Ole's face blushes red, his hand hovers from your shoulder for quite a moment before he turns around."
        o "I-..."
        "Almost by instinct, your hand reaches out to his back, and he stops for a moment."
        e "I'll... see you back home."
        o "Y-yes."
        "You can almost hear Ole gulping, before he walks away slowly."
    else:

        o "That I don't doubt, kiddo."
        "He raises his palm and pinches onto your cheeks."
        e "Ouch... Do you really need to do that?"
        o "No. See you back in the shop."
        "He turns around slowly, and returns to the shop."
    $ timenow.addTime(0, 0, 30)
    $ ole_votequestminute = timenow.anal()
    $ quest39.status = 7
    $ quest39.qComp(__("Buy 12 pieces of Elderwood"), "Elderwood", 12)
    $ quest39.qProgress(__("Buy 10 pieces of Crystal String"), "Crystal String", 10)
    jump main_lusterfield01

label Ole_Voting_Report_Pirkka:

    e "Hey, I've got the materials you need, Ole."
    o "Oh, good. Then hold this resonator gem. I found it around the storage in our shop."
    o "I reckon according to Pirkka, we can build a Harp, with this gem and the materials you have."
    "You nod, and take the gem from Ole's scaled hand."
    e "Thank you, Ole."
    o "Good luck!"
    $ quest39.status = 8
    $ addItem("Resonator Gem", inventory, 1)
    $ harprecipe = Recipe(harp_item, resonatorgem_item, 1, elderwood_item, 12, crystalstring_item, 10)
    $ harpcheck = next((x for x in discoveredrecipe if x.product.img == "Harp"), None)
    if harpcheck == None:
        $ discoveredrecipe.append(harprecipe)
    $ quest39.qProgress(__("Craft a Harp"), "Harp", 1)
    jump main_kingspawn

label Ole_Voting_Good_Finish:

    o "Hmmph..."
    "Ole handles the harp, adjusting the sound as it plays, he seems satisfied, if not surprised as everything so far has gone so well."
    "If it's not for living with him for so long, you'd think he has had decades of experience on musical instruments, not hours."
    o "Oh, that's good. The sound is just right."
    "He flings the strings for a few more times."
    o "This is just perfect. I'll present this to the supplier later."
    e "You seem so much more experienced than Seb. Why aren't you the one on the counter."
    o "Don't worry, I'm always watching over his back. And he's one talented pawnbroker too."
    o "Sometimes, being good with your brain doesn't always translate well with getting what your customers want."
    o "And sometimes a good heart and a good mouth gets you more money than if you play it straight."
    o "Just know that it doesn't always mean either side is more deserving. I'd like to think of us as two opposite sides that complements each other nicely."
    e "Damn, am I the third wheel here?"
    o "No-no! I don't mean that. I think you're the one in the middle, always pulling everyone together a little closer to each other, and... to you."
    e "Haha, stop teasing me, Ole."
    if ole_affection > 15:
        o "You've always seemed to have that invisible string in your hand."
        o "The first day you woke up, you've got Seb entranced, going crazy over seeing you. And then Lothar suddenly had almost like an obsession over you."
        o "And now, after so many days have passed, even Rahim, a stoic, withdrawn guy. Suddenly he flipped everything around and gave us a ballot to vote for the one he hated the most?"
        "He stares forwards, mindlessly plucking his finger onto the soft strings. The sound was terrible, but he doesn't even seem to be aware."
        e "I didn't even realise that."
        o "Just bit by bit, the village changed ever since you live under our roof. Even if it's so small, it's the first time I've felt, that there's a bright future ahead of us."
        "He takes a pause to lean forward, your snout is so close to him you feel they're gonna touch anytime soon."
        "His hand reaches towards your direction, and slowly climbs onto yours as he nudges against you."
        if quest15.status:
            o "That time I was sick, I can feel you there."
            e "M-me?"
            o "It was the first time someone took a hold of me, it felt like such a shock when you wiped away my sweat."
            o "Well, it wasn't how I imagined you'd see me... without clothes."
            e "It's not like I haven't seen cock and slits before."
            o "Ha, you're right."
        "His glances are so... loving, you wish you have the courage to reach forward and kiss him. But both of you aren't taking the chance."
        o "So... how did you pull that off?"
        e "Hmm?"
        o "The strings."
        "Ole sits beside you, he turns his head towards your face unbelievably close."
        e "I... I just tried my best to help people. Anyone, really. I liked being around you a lot."
        o "Heh, I meant crafting the harp."
        e "Hey! Are you teasing again?"
        o "Nope."
        "Ole stands up swiftly, his tail softly brushes against your legs."
        if ole_votequestpirkka:
            o "Thank you so much for the Harp. I'll bring that to the meeting, hopefully I can impress the supplier."
        else:
            o "Thank you and the bard for the Harp. I'll bring that to the meeting, hopefully I can impress the supplier."
        e "Ole."
        o "If we can do that, it'll give me a much higher leverages against Gwyd. Then, well. We can start talking about price."
        e "Ole!"
        "You hear a soft sigh as you shout."
        o "It's be fun hanging out with you, kiddo. You've impressed me everytime we're together, here's the reward for you."
        e "W-wait! Can you at least tell me what you were thinking about?"
        "Ole takes another pause as he stares at you, almost frozen in place, just pondering something."
        o "Nothing."
        "He quickly picks up the harp and hops onto the stairs, leaving you staring into the wall."
    else:
        o "It's true! I think you're a great newcomer- I shouldn't say that, you're already one of us."
        e "R-really?"
        o "Yes, there's a certain magic to you that whatever you do, it seems people suddenly forget all anger and frustration, like a hot spa."
        e "If I'm that good... Why don't I have an effect on you?"
        o "Ha..."
        "Ole glances at you deeply with a bright smile."
        o "You have an effect on this Harp, it's perfect and I think we can snatch an easy agreement out of Gwyd now."
        o "With that leverage, it's gonna save us a lot of future money of being scammed by that ram."
        "He picks up the Harp with ease as he stands up from your bed."
        o "Well, you should spend more time with Seb too."
        e "I get it, Ole."
        o "Hey! Don't worry kiddo, you've got my vote."
        "Ole faces you with a slight concern, perhaps he'd become aware that your vision is becoming so much more blurry."
        "For a moment, your heart seems to have paused."
        pause 3
        "As soon as you've returned to your sanity, Ole's already gone... leaving you alone inside your own room."
        e "Shit... what did Ole mean by that."
    $ pc.gold += 500
    $ ole_gwyd_success = True
    msg "You received 500 gold from Ole."
    $ QuestFinish(quest39)
    jump main_bedroom

label Ole_Voting_After_Meeting:
    $ ole_after_meeting = True
    e "Hey, Ole. How did that meeting go?"
    if ole_gwyd_success:
        o "Perfectly, weird as I say. I think the harp we got wasn't miles better than Gwyd's one."
        o "And the supplier, he was quite peculiar. I guess he wasn't ready for a competition, nor did Gwyddyon."
        o "But, in the end. Gwyd wasn't the wisest one when it comes to holding in their emotion in his face. He wasn't having it when I mentioned... everything."
        o "I guess that tantrum he threw really hurt the chance of him signing another exclusive contract with the supplier."
        e "Oh? Was Gwyd that angry?"
        o "Not as much as you'd expect actually, but the supplier... also is a combative type of person, so there're some turbulence during the meeting."
        o "And well, long story short, I've got the piece of paper."
        "He shows you the contract, signed with both Ole and the supplier's name in the corner."
        o "Now, of course I wasn't going after Gwyd entirely. He got his own contract also, but at least we have the upper hand now, with Haskell's deal, and some part of Rahim's clothes."
        e "Does that mean, you're choking Gwyd out of the business?"
        o "No, no. Our contract is more or less equal for both parties, last contract we had, he got a lot more from it than we did, so I just wanted to see him squirm now."
        o "Anyway, that's gonna ensure some money and reputations in our pocket, all thanks to the harp you helped making."
        e "I-I'm just glad."
        o "Regardless of the outcome, I'll be voting for the goats. As a part of the contract we just had, and also an appreciation for your help."

    elif ole_gwyd_success == -1 or (quest39.status == 5 or quest39.status == 6):

        if ole_gwyd_success == -1:
            o "It went alright. Gwyd's harp was just better than ours, I think it was a right choice to leave the harp."
            e "Aw... I'm sorry we couldn't make one in time."

        elif quest39.status == 5 or quest39.status == 6:
            o "Well, we didn't get to finish the Harp, I guess it takes more time than we expected."
            e "Aw... I'm sorry we couldn't make one in time."

        o "It's okay, [e]. We still have Haskell helping so the meeting went so and so."
        o "Turns out, the supplier really was looking for Gwyd to understand his materials, so the meeting ended up being the two of them talking."
        o "But, we've got a better contract from Gwyd. That's gonna save the shop some money."
        e "I'm glad it turns out fine, Ole."
        o "Yeah, I guess there's no excuse for me to not vote for teaming up with the goats now."
        "Ole smiles faintly as he pats your shoulder."
        if quest39.status != True:
            $ QuestFinish(quest39)
    else:


        o "We didn't get to know what Gwyddyon was up to with his supplier, but apparently he made a harp for him. And the supplier seemed pleasantly surprised."
        e "Damn, I should've known."
        o "It's okay, [e]. We still have Haskell helping so the meeting went so and so."
        o "So in the end, we've got a better contract from Gwyd. That's gonna save the shop some money."
        e "I'm glad it turns out fine, Ole."
        "Ole smiles faintly as he pats your shoulder."
        if quest39.status != True:
            $ QuestFinish(quest39)

    jump main_kingspawn

label Cane_Voting_Opinion:
    e "Hey, Cane. Have you heard of the Vote from Rahim?"
    c "Aye, everyone in the tavern was talking about the news."
    c "Ain't that old geezer a sight to behold, eh? I betcha he's missing the goats."
    e "I thought he said he's voting against allying up with the goats."
    c "Heh, the nefarious bull has a softer heart than ye think, m' lad."
    e "I hope you're right, kinda. But how would you vote yourself?"
    c "I ain't votin' for nothing. I've got a whole tavern 'ere waiting for an extra mug of beer."
    "Cane says carelessly, his hands scrubbing the tankards almost by instinct."
    e "So you're not voting for anything?"
    c "Laddie, it's a waste of time whatever sides yer' on. What's the odds yer single slide of paper makes a difference."
    menu:
        "Berate him":
            $ cane_dialogues["Vote Quest Rebuke"] = True
            e "Hmm... that's odd. The Cane I knew cared about many more than money."
            "The barkeep's eyes widen, his face contorts into a lingering grin that hides a hostility."
            c "Yeah, but-"
            "There seems to be much to be told, but the bat stops himself before you hear anything."
            c "I was just saying... lad."
            "Weirdly, the bat does not bring himself up to your eyes, his hands are still scrubbing the tankards, thoughtlessly."
            c "Ya know what? If yer ass is free, why don't cha come help a needy fella 'ere."
            "He brought his voice back up again, as if someone suddenly pushed a lever."
        "Accept his opinion":

            $ cane_dialogues["Vote Quest Rebuke"] = False
            e "I guess so. It's your choice to make after all."
            "You shrug, the disappointment in your face is not entirely subtle to the bat."
            c "Aye, aye. Look at that pouty face, I get it-... yer mad I hadn't have time to leave my tavern for one second."
            e "I didn't say that."
            c "Laddie, I've known ya for how long, ya think I can't tell when yer trying to make me feel better?"
            "Cane's hands slams onto either sides of your neck tenderly, his fingers trace across your shoulder before squeezing it softly."
            c "Lookie 'ere. Ya don't need to go soft on this ol' geezer."
            "His thumbs gently press against your shoulder, and you lean closer to Cane, just enough to feel his warmth emanating over you."
            c "If I ain't right, ya gotta tell me."
            c "I make lotta mistakes, too many to count. And my eyes' not working like it used to, ya know... It's part of the perks of growing older, not wiser."
            "You smile faintly, as your palms wrap around the bat's waist, forming a mutual embrace between the two of you."
            e "If you need a hand, Cane... I'm always here."
            c "A hand? I've got just the right job for ya."
    e "Oh? You wanted me to serve the tavern?"
    c "Naaa-ah, it's just that someone's been bugging the ol' trunk, or rather, something."
    e "So... what is it?"
    c "I have no idea. A ghost, maybe, a patron of mine said he spotted a shadow 'ere at night, right 'ere."
    "The bat points at where he stands, right behind the counter."
    c "I ain't gonna lie, he's been making a scene these past days, on that day he claimed to see the ghost, that lad's scream enough to spook some of m' dearest patrons away."
    c "Ya haven't seen it either, did ya?"
    e "Not really, have you?"
    c "Nah, nothing. Those peeps listened to his story, and now telling me the ale's tasting off, like someone dropped a jar of honey in it..."
    c "But I ain't seeing nothin-, the ale tastes fine, nothing caught my eyes at all."
    c "And now he's saying I'm some kinda ghost inside a bat's body, what a bunch of hogwash."
    "The tavernkeeper furrows his brow."
    e "Why did he accuse you like that? Do you two have some sort of history?"
    c "Ya remember Topu? That lad? Oh, Topu was a good lad, he liked helping with the tavern, he doesn't complain, and he has no temper. Up until he fell in with bad influences all around."
    c "The lad stopped talking with me as much after, he's gotten drunk all the time. And when I asked he always said nothing as if hiding something from me."
    c "It was proper to kick 'em bad influence out of my tavern, right? Even though m' lad shouted at me for doing that."
    c "And now, one of 'em came back, now spreading rumors all around my place? I'd not respect m'self if I didn't give 'em a lesson."
    menu:
        c "Ya wanna help?"
        "Accept Cane's request":
            e "Alright, fine, you're the boss. What should I do again?"
            c "First thing first, find that fella who's been spreading the buzz. Blokes' came here a while ago, should be easy to spot him here."
            e "What's he look like?"
            c "Looks like a grey rat. A nasty one, yer lil snout here might smell it from miles away."
            e "Mhmm, doesn't sound very appetising, won't he stink up your tavern?"
            c "Ya bet, that stink's so strong it's the first time I ain't smelling beer since I've been a bat."
            "Cane's grin widens into a prideful smile."
            c "Either way, go find that stinker and either ask something useful or just tell'em to shut it up."
            e "What if what he said is true, then?"
            c "Then we gotta catch that devious thief, [e]. You and I."
            $ QuestBegin(quest45)
            $ quest45.qProgress(_("Ask the rat patron for information about the rumoured ghost"))
        "Maybe Later":
            e "Perhaps some time later, Cane. I've got something else to do."
            c "Dang, well... okay lad."

    jump Cane_Normal_Talk

label Rahim_Vote_Day:
    hide screen menu_buttons
    "The day of voting is here. Lusterfield is bustling with people, a lot more than usual."
    $ renpy.music.play(mVote, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    "It was a momentous occasion, one that had the villagers abuzz with excitement and trepidation alike."
    scene lusterfield02 with dissolve
    "Banners, that leads to the voting stage fluttered in the breeze as you follow the path slowly towards the town center."
    "As you made your way to the center of the village, you could feel the weight of this moment in every step."
    "Everyone is standing around, chatting, discussing the idea of allying up with the goats."
    "A wooden platform, a makeshift stage for the event dominated the scene. At its center stood a modest, yet significant, wooden ballot box."
    "You see a long line of people at the front of the platform, snaking all the way around the center."
    "Rahim stands in the middle while Ole is at the side of the ballot box."
    "You take a piece of paper from the counter, and swiftly join the line, a sense of responsibility and duty guiding your steps."
    "The choice is clear, yet... its implication might sprawl deep. A solemn sense of uneasiness pervades over your body as you inch forward."
    show lothar stare with dissolve
    l "Disciple?"
    e "Lothar? Have you voted yet?"
    l "Of course I did, as stupid as this whole event is, I guess it's time to settle all unneccessary noise these goat-lovers make."
    l "What are you voting?"
    e "Uh... No?"
    l "Huh."
    show lothar bored with dissolve
    l "I've strongly advised Amble and Jog to vote no. So, you better choose your choice wisely."
    pause 1
    "Lothar pats all around your hips, it felt genuinely intrusive but he doesn't seem to care."
    menu:
        "Let him continue":
            $ lothar_fold = True
            "You remain silent as Lothar's hands wander all over your body, and it's right in front of the people behind you in the line."
            e "Lothar?"
            if lothar_affection > 15:
                l "You better behave, Disciple. I'm not fucking joking around."
            else:
                l "This is your last fucking chance, Disciple. You don't want to see me mad."
            "Lothar leans forward as you instinctively lean back, your snouts are only an inch apart, you can clearly see his eyes glowing red."
            "His hot breath tells you his heart is pumping faster and faster. But something tells you it's not about you, and it gets awkward really fast."
            show lothar angry with dissolve
            "For a moment it almost seems he's about to hit you with him holding onto you tighter and tighter. His face is distorting in one resembling pain and anguish."
            "You don't even dare to breath."
            "Suddenly, he releases his grip on you. And you fall over."
        "Protest":
            $ lothar_fold = False
            e "Hey! Stop that."
            show lothar angry with dissolve
            "Your shout turns almost the whole village's attention onto you and Lothar. He retreats immediately but his furrowed brows doesn't fade."
            "Lothar looks around, he sees a few dozen pairs of eyes just glancing at your direction."
    "Without leaving another word, he glances at you once more and leaves."
    hide lothar with dissolve
    "T-that was a weird interaction, even for Lothar's standard. It does seem he takes the ballot very seriously, perhaps too seriously."
    "You're genuinely scared of Lothar now, even though you know he can be possessive, there's still a point where you think it's too much for you."
    "Some people's eyes remain onto your direction."
    "They are murmuring something, but you don't know what that is. So you pat your waists slowly to look for your voting paper."
    "At least it is still here, you reckon Lothar could have easily stolen from you, but maybe he thought against it."

    "After a while, the line clears fast, and soon it's your time to walk on the stage."
    if lothar_fold:
        scene lusterfield_votingtable with dissolve
    else:
        scene lusterfield_votingtable_nofold with dissolve
    "Ole greets you with a usual hug, he gestures toward the wooden platform ahead, where a modest, yet significant, wooden ballot box stood."
    o "Here's where you'll cast your vote."
    "He hands you a stamp with red ink on the table."
    o "Simply stamp your choice with that chop in either box."
    menu:
        "Should Lusterfield form an alliance with Goat Tribe?"
        "Yes":
            $ vote_choice[0] = 1
            "You voted yes in the booth, and cast your ballot in front of Ole."
        "No":
            $ vote_choice[0] = -1
            "You voted no in the booth, and cast your ballot in front of Ole."
    o "Hey, thanks for voting, [e]. You can wait out there, and after tallying all of them, Rahim will make an announcement."
    "With a friendly pat on the back, Ole moved to assist the next villager, leaving you to get off the stage quickly."
    scene lusterfield02 with dissolve
    "A few of the other helpers like Ole begin to count, and suddenly, you notice Lothar hovering around the counters, his gaze fixating on something."
    s "Gooooooood fricking morning, [e]!"
    show sebas grin with dissolve
    "A bright voice snatches your back as your attention turns to Sebas."
    e "Oh Seb, didn't expect to see you here, and why aren't you swearing?"
    s "Ha, I have to cast my super duper important vote, isn't that what the whole event is about?"
    s "Also, it's so much better seeing people use my stamp. Hearing that crisp chop sound makes me feel a little tingly inside. HMmmmmmm!"
    "He raises you a thumbs up, which you follow suit."
    e "Good, I voted just now, your stamp is awesome though."
    s "I know, right? I've spent a lot of time thinking what I should use as the icon of Lusterfield."
    e "And you chose... lion?"
    s "How are you so smart, roomie! Of course! That's why every vote has my face on it, and... well the fellas on the stages are still counting."
    s "You know, there aren't too many people in Lusterfield, so I'm not sure why they are taking so long, ugh."
    e "I think they're recounting everything thrice."
    s "Yeah, by this rate, it'll probably be done... at nine, earliest."
    hide sebas with dissolve
    "As you wait alongside Sebas, the weight of your decision settled upon you, and you couldn't help but feel the significance of this moment in the heart of Lusterfield."
    "One side is with the goats, you'd love to see Furkan satisfied for once as the two factions mend their relationship, but on the other hand you have Lothar, who's guaranteed to rage if you are not voting no."
    "You stay with Sebas for a while, waiting for the villagers to count the rest of the votes as more comes in."
    scene lusterfield02_night with dissolve
    "Eventually, the line gets shorter and shorter, until there are no more people waiting to vote."
    "It's only when you look back you notice Jog in the corner, and Amble talking with him. They look much more distressed than their normal selves."
    "When they notice you, they quickly avert their gaze and leave. So you shrug and continue waiting with Sebas."
    r "Greetings, everyone."
    "Rahim walks up onto the stage as the last ballot box is closed and put away."
    if quest38.status == True:
        $ vote_choice[5] = 1
    if quest39.status == True and ole_got_gwyd_answer == 1:
        $ vote_choice[6] = 1
    if quest40.status == True:
        $ vote_choice[4] = 1

    $ vote_result = sum(vote_choice, -2)

    r "We've counted the final number of votes. And, I have the fate of Lusterfield on my hand."
    "Suddenly, the whole town center is silent, everyone is holding their breath, even Sebas."
    r "This is the first time the people of Lusterfield has spoken, I hope everyone respects the result, whatever that will be."
    r "And we had to confirm the total votes over a few times to avoid any miscalculation."
    "Rahim, holds the final tally in his trembling hands, sweat glistening on his furrowed brow."
    r "So..."
    pause 4
    $ vote_difference = abs(vote_result)
    if vote_result >= 0:
        $ goat_reconciliation = True
        if vote_result > 0:
            r "As the majority have already decided, we will reinstate our alliance with the goats."
            r "It was a close vote, this decision is decided by only [vote_difference] vot-."
            "A mixed chorus of cheers and murmurs ripples through the crowd around the stage. Seb raises his eyebrows beside you, his mouth hangs agape."
            "Some villagers exchange smiles and pats on the back, while others bear expressions of uncertainty, their eyes revealing lingering doubts."
            "You hear the sound of breaking porcelain rings out, alongside with a loud grunt coming from Lothar."
            "He sweep his arm across a table filled with plates, sending them crashing to the ground."
            r "Remember, the decision was made collectively by everyone. It is not my place, nor anyone, to question their choice."
            "Rahim says calmly, obviously targetting this statement to Lothar."
            "Lothar stares at the broken shards for a moment, until suddenly his gaze is locked onto yours."
            "His brows slowly furrow, there is a flash of sorrow in his eyes."
            "Without a single word, Lothar turns and storms off, his heavy footsteps echoing through the square."
            r "Ahem, although, I personally have voted against it, but it was a decision of everyone who has voted here."
            r "Following today, we'll arrange a meeting with the Goat's leader. We will protect each other, from whatever might be happening out there."
            r "Their people are allowed to visit our village, and same goes to ours."
            r "Thank you."
            "The crowd soon begins to desperse also, while you and Seb walk away."
        else:
            r "The result, is surprising to say the least, I know some of us did not vote, but to end with the same vote to each side, is a miracle."
            r "I wish to resolve this as smoothly as possible, however we have to consider the logistics and your own time. So, it's not fair for us to waste everyone's time to hold another vote."
            r "Therefore, as the leader of our village, I hereby forfeit my own vote against the alliance."
            "A mixed chorus of cheers and murmurs ripples through the crowd around the stage. Seb raises his eyebrows beside you, his mouth hangs agape."
            "Some villagers exchange smiles and pats on the back, while others bear expressions of uncertainty, their eyes revealing lingering doubts."
            l "What the fuck, Rahim?"
            "Lothar's voice, a thunderous growl, cuts through the commotion."
            l "The fuck are you doing? You're not helping the goats I tell you. You're-"
            "His rugged face, lined with years of determination, contorts into a fierce scowl."
            "The hero wolf climbs on top of the stage. Rahim is undeterred, calmly steps forwards to address Lothar."
            r "Are you done?"
            l "How could you be this dumb. I told you I have proof, their stones. Their fucking golem."
            "His words, laden with frustration, resonates through the square, commanding the attention of the villagers and elders alike."
            "Lothar, his fists clench and eyes burning with anger, strides toward Rahim who had announced the result."
            r "We will continue in a moment."
            "Rahim addresses the crowd, then quietly runs towards Lothar."
            l "You don't DO THAT! I tell you-"
            r "What I vote myself, is my own business. It's not your place to judge, Lothar."
            "Sebas stares with bewilderment, the tension in the square escalates, as whispers of astonishment and concern spread among the crowd."
            l "Not mine? I'm the fucking hero of Lusterfield, I saved you all from the goats and now, instead of TRYING to stay away from them like a normal person you're allying with them?"
            l "Half of the Lusterfield voted No, why didn't you respect their opinion you fuckin' hypocrite."
            l "The time I've spent, looking for evidence for you. And you're saying everything is fine now?"
            r "Again, the vote today has already concluded-"
            "Lothar's face reddened, and his voice thundered across the town center."
            l "Where the fuck did you hide Rahim, huh? They fucking killed your daughter, stop pretending opinions of mere commoners matter anything to you-"
            "A slap, powerful enough to tear your ears apart, can be heard on the stage, the sound echoed through the square."
            "Suddenly all murmur and rumbles has stopped as everyone stares at the hero and the leader."
            "Lothar staggers back, his grey cheek reddens from Rahim's rebuke."
            r "If what you're saying is true, then maybe it's time for the hero to protect the village for once."
            "Rahim says calmly, but his stare seems to say otherwise."
            "Seb almost spilled his food as he watches the event unfold, the crowd comes to a complete silence as the hero is somehow humbled by Rahim's palm."
            r "Following today, we'll arrange a meeting with the Goat's leader. We will protect each other, from whatever might be happening out there."
            r "Their people are allowed to visit our village, and same goes to ours."
            "Lothar stares as Rahim quietly steps away from the platform. The crowd soon begins to desperse also, while you and Seb walk away."
            "Just as you turn back, you notice Lothar is still... standing. But his gaze suddenly fixates onto yours. You quickly look away."
        show sebas normal with dissolve
        s "You see what Lothar did there?"
        if vote_result == 0:
            s "I still can't believe Rahim slapped him that hard. He tolerated him the most out of everyone in this entire village, apart from the two lackeys."
        "You walk alongside Sebas, whose expression remain astonished but cheerful."
        "You remember Lothar searching around your body just as you stood in line, and then... when they counted the votes, he stood in the back row, observing something."
        "What could he have been possibly doing..."
        show sebas grin with dissolve
        e "What's wrong with Lothar?"
        s "It's typical Lothar. Whenever something doesn't go along his plan, that wolf will go craaa-zy..."
        s "He's like a caged beast, a ticking time-bomb. You won't want to get near him when he explodes."
        if sebas_kick:
            s "Maybe I should kick his balls more than once. That'll fix him."
        else:
            s "I still couldn't believe we didn't get to kick his balls while I've got the chance. Maybe that'll fix him."
        e "You can't fix people that way, Seb."
        s "Roomie, you're absolutely right. Some people can't be fixed."
        "The lion raises his fingers, with a lopsided grin."
        s "A-anyway, we've got the goats on our side now!"
        e "To be honest, Rahim kind of shifted his opinions completely over nights. I wonder if there's any secrets he's still holding back."
        if vote_result == 0:
            s "Rahim forfeited his vote, I'd never think an old grumpy guy like him will ever want to see them goats again."
        s "Hey, I told you Rahim's under my infatuating charm's control, wooooHOOO! Maybe I can make him return my favourite pebbles now."
        "You smile as Seb enters the shop."
        s "It's getting late, I should sleep after such a long day."
        s "Gotta get ready for some goat clients, Ole should also be coming back soon."
        s "Have a good night, [e]."
        e "Good night, Seb."
    else:
        $ goat_reconciliation = False
        r "As the majority have already decided, our village will continue our business as usual."
        r "Which means, we will not form alliance with the goats."
        r "It was a close vote, this decision was decided by only [vote_difference] votes."
        "Rahim declares, his voice steady yet laden with the gravity of the moment."
        r "We will only communicate with the goats, should we encounter any threat to the existence of our tribe."
        "A mixed chorus of cheers and murmurs ripples through the crowd around the stage. Seb raises his eyebrows beside you, his mouth hangs agape."
        "Lothar seems to be in the cheering crowd, without the cheering part. He looked void of any emotion, turns away and walks off."
        r "There shouldn't be any further questions. Let's consider this the end of a chapter of Lusterfield."
        "Some villagers exchange smiles and pats on the back, while others bear expressions of uncertainty, their eyes revealing lingering doubts."
        "Sebas stands alongside you, his shoulders slumped, and his eyes downcast."
        r "Our business will continue as usual, and we will embrace any challenges by our own selves."
        r "Thank you."
        "As the crowd begins to disperse, Sebas lingers for a moment, he can't help but to sigh, exchanging a glance with you."

        show sebas bored with dissolve
        s "Damn, didn't think we'd lose, and by such a small margin."
        e "Well, you tried your best, Seb."
        "Sebas chuckles while he's looking down."
        s "Yeah, business continues as usual I guess."
        show sebas normal with dissolve
        "The path forward is clear, but the final decision still weighs heavily on his heart."
        e "Seb, do you need anything from the goats?"
        s "No, roomie, I accept gold from anyone."
        s "But it's definitely miles better for me that we're not in a perpetual stalemate with the goats."
        "Sebas sighs once more, before he enters the shop."
        s "Well, I need to go to bed soon. Have a great night, [e]."
        "You nod as you watch Sebas slowly walks upstairs."

    $ timenow.hour = 22
    $ timenow.minute = 30
    $ QuestFinish(quest37)
    jump main_lusterfield01

label Rahim_Vote_Day_Late:

    "As you walk in the streets of Lusterfield, you are suddenly reminded of the voting day."
    "Quickly, you run towards the town center, where the voting would be taking place."
    "As you arrive, the crowd has already emptied, and Rahim is no where to be seen."
    e "Shit, did I miss the vote?"
    "Walking towards the post. There were a large banner in the middle of the town center."
    if quest38.status == True:
        $ vote_choice[5] = 1
    if quest39.status == True and ole_got_gwyd_answer == 1:
        $ vote_choice[6] = 1
    if quest40.status == True:
        $ vote_choice[4] = 1

    $ vote_result = sum(vote_choice, -2)
    $ vote_difference = abs(vote_result)
    "It reads..."
    if vote_result >= 0:
        "As voted by the majority of Lusterfield, we will reinstate alliance with the goat tribe, a gratitude to everyone who participated in the vote."
    else:
        "As vote by the majority of Lusterfield, we will continue as usual, a gratitude to everyone who participated in the vote."
    "Apparently, the result of the vote is already announced. You stare at the banner in shock."
    "With the way how Rahim worded the announcement, you are somewhat convinced he might not be happy with your absence."
    "You might want to talk with Rahim after..."
    $ rahim_late_vote = True
    $ QuestFinish(quest37)
    jump main_lusterfield01





label Jog_Voting_Opinion:
    e "So, Jog. What do you think about... Lusterfield's Voting Day?"
    j "Voting? That's the most booooo-oring activity someone can do, why don't people go to something more useful instead?"
    e "Well, I wouldn't consider it exactly boring, the whole thing might take you... maybe ten seconds."
    j "Yeah, well. And everyone's else are voting, in a millions in a million's case, my vote won't even end up being useful in any shape of form."
    j "Not to mention the time you're wasting on getting to know the goats, well, even though I already know what they're up to, it's still a chore to actually talk to these fools."
    e "What about the one in a million's case, what if that vote end up mattering and you didn't vote?"
    j "Ha, not too shabby if you're trying to pursue a debating career, but don't you worry, I'll vote no."
    e "May I ask... why?"
    j "Eh, nothing special. I don't have that strong of an opinion over them personally. Even though you and I... had already been there."
    "Jog averts his gaze, and continues lying lazily on the hay piles."
    j "Don't ask, alright. Amble's probably gonna tell you about it anyway but, eh, I'd rather keep my plums to myself."
    e "A-alright then."
    "You turn your back on the nimble scout before he lightly taps your shoulder."
    j "One thing, unrelated to them goats but I've been meaning to do something, would like a hand to help and what not."
    "Jog sits upright as he faces you properly, setting the half-eaten plum to his side."
    e "How may I help, Jog? And would that change your mind on the goats?"
    j "I guess helping me can somewhat convince me to risk something just to vote for your goats."
    "Jog bites on the fruity plum. He's being extremely vague about his vote, but it seems you've got to help him before he helps you."
    j "I mean, that's what you're coming for, right?"
    "You nod, palm clenching in anticipation for his request."
    j "Anyway, you might know about one or two things about this, but I used to live in that lion's shop, long before you came here."
    j "And, well. Something happened between us."
    e "Did Sebas kick you out? I remembered hearing about this, only briefly."
    j "I can only tell you, I didn't steal anything at all. Neither would I have interest in his stupid stuff."
    j "But long story short, there's something about your cutesy little roommates that you oughta know."
    j "I found out that, at least once in a while, they'll disappear into the night, only coming back an hour later."
    j "Of course I can't get close, Ole's got a crazy pair of eyes in the dark. I can't just follow them. Neither can Amble, he's too much of a hunk to hide properly in bushes."
    j "So, what I want from you is just simple, follow Seb to where the hell they are, and snoop, listen in, eavesdrop, just find out what he's doing."
    e "Why are you asking me to do this?"
    j "Look, I know we have some kind of histories with your so-called roommates, but I guess I never knew what exactly happened before I was kicked out, not in a good way."
    j "And who knows what happens! Maybe the lion is just wanking out there, maybe with Ole."
    e "I'm still not convinced that Ole's not gonna spot us right away, that's Ole we're talking about."
    j "Come on, just cheat a little bit here, you don't need to hide from Ole if Ole's never there."
    e "Excuse me?"
    j "Ha, that was a strange sentence, I'm not... doing anything to him, don't you worry. We deserve more of those plum-shaped ass."
    j "I'll try to distract him with a talk while you follow the lion."
    e "Alright."
    e "But before I help you, may I ask one question, what do you get out of this?"
    j "Getting philosophical aren't you. like I said, I'm just naturally curious, that's all. Not gonna hurt them in any shape or form."
    j "Are you helping or not? And I think I've made it clear by the nature of what I'm asking, no one will ever know about this."
    j "I have to tell you though, if you got caught I have no idea what will happen to you. So, I understand if you don't take it."
    menu:
        j "So, what'chu think? Care to help quench a fella's thrist of curiosity?"
        "Accept the quest{#JogVoteQuest}":
            pass
        "Maybe Later{#JogVoteQuest}":
            e "Maybe... later?"
            j "Well, somehow I guessed exactly what you're about to say, but yeah. Takes time to think and stuff."
            j "Come back when you have the time."
            jump Jog_Normal_Talk
    e "Sure, how do I get started."
    j "Oh it's very easy."
    jump Jog_Vote_Countdown

label Jog_Vote_Countdown:
    j "Watch this..."
    $ timer_time = 3
    $ timer_random_pause = renpy.random.random()*2
    $ renpy.pause(renpy.random.random()*2)
    show screen countdown("Jog_Vote_Countdown_Fail", 3, 2)
    menu:
        j "H-Hyah!"
        "Dodge!":
            jump Jog_Vote_Countdown_Success


label Jog_Vote_Countdown_Fail:
    "Jog throws a fist onto you, but you didn't react in time."
    j "Hah! Too slow!"
    e "W-what was that?"
    j "To test your reaction speed, as usual. Now do it again."
    jump Jog_Vote_Countdown

label Jog_Vote_Countdown_Success:
    hide screen countdown
    "Jog throws a fist onto you, but you slip away in mere inches."
    j "Hey, not bad."
    e "You almost punched me there."
    j "Calm down, I won't hurt a single strip of your fur. You just need this instinct when you're going on a mission without me."
    e "Why aren't you coming along with me?"
    j "So I have an alibi if you end up failing, and distracting Ole. What kind of stupid question is that."
    j "But, you've proven to be quite capable, so we can proceed to the next stage. Getting Ole out of the equation."
    j "Ethically."
    e "Alright, thanks for letting me know about that."
    j "Is that sarcasm I smell, or are you just being unapologetically grateful."
    e "Both, maybe."
    j "Well cool, you're just one step away from being Amb. We just need to get rid of some of your smart little quips."
    j "So, thanks to the same hunk. I've heard Sebas' going out {b}One day before the vote{/b}, at night, you gotta wait for that."
    j "I had already ask Ole to meet at Cane's place in the meantime so the lion's going alone."
    e "A-alright, why don't we just ask Seb what's going on?"
    j "Uh, because then he'll question why would you know about this in the first place?"
    j "Plus, he'd have already told you if he wanted to let you know, the fact that you don't know anything about it is proof that he doesn't want to."
    e "I'd rather trust him first hand."
    j "You can ask him, if you're not afraid of getting your ass blasted by that jackass, I had taken that first hand when I still lived there."
    j "{i}Not literally.{/i}"
    e "So, is that it? Just follow him?"
    j "Yeah, but I can't keep you safe out there, no responsibility from me if you ended up joining some stupid deer cult after following him."
    j "But that's the gist of it. Come back and just let me know, and I'll vote what you want."
    e "Okay, I'll get it done."
    $ QuestBegin(quest40)
    $ todaydayofweekfromsebasmeeting = weekdictionary[weektuple[int((timenow.day - 2 + rahim_vote_duration) % 7)]]
    $ quest40.qProgress(_("Follow Sebas from the King's Pawn on ") + todaydayofweekfromsebasmeeting + _(" night"))

    jump main_lusterfield_range

label Jog_Vote_Follow_Sebas:
    $ quest40.status = 4
    "You hide outside, behind the windows, just enough to hear the conversation between the two shopkeepers and the customers."
    "Slowly, time has passed as you eavesdrop behind the wall."
    s "Where you going to... again?"
    o "Jog, he asked to talk today, I can't make it with you today."
    s "Ugh, it's fine. I'll talk to him by myself, it's easier that way."
    o "I thought you'd have a bigger reaction for me talking with Jog."
    o "'UGH I CANT GIVE A FLYING FUCK ABOUT THAT SCOUNDREL.', or something to that effect."
    s "Something else happened, big O. I'll talk to you after tonight."
    o "Cool, I'd take that as an okay then. Take care."
    "You hear some other muffled noise before the door outside opens. The lizard turns the sign in front of the shop over."
    "Ole lingers for some moment outside the door, but he quickly picks up his pace and leaves."
    "Only one voice remains in the shop, and it is Seb's."
    s "Fucking hell, why the fuck did he do that, fuck fuck fuck fuck fuck fuck fuck fuck..."
    "The only two conclusion you can draw from his mumbling are that he's alone, and he really likes to curse."
    s "'You motherfucker! I should've never believ-'"
    s "No I can't say that word to him."
    "He stares at the mirror above the counter, fixing his hair and fur."
    s "Uhm... HOW COULD YOU DO THIS! WHAT A FUCKING SCUMBAG YOU FUCKING ARE."
    s "I'M NEVER GONNA TALK TO YOU AGAIN. NO MORE, FUCK YOU."
    "While Sebas is adjusting his clothes, you're still hiding behind the windows, just enough to see the counter."
    s "That sounds about right. Now, should I punch him in the face, or..."
    s "Maybe not, that's gonna leave a mark."
    s "Where the fuck is [e]... I thought I just saw him somewhere."
    "Sebas knocks on your room, which you're just relieved that you were not hiding there."
    pause 3
    s "Fuck, it's time to go."
    "Sebas runs out of the counter quickly, pushing away the doors into the roads, you sneak up just behind the shop to peek at him."
    scene lusterfield01_night with dissolve
    "He is running out of the village, at a pace so quick you might not even be able to catch up."
    "Crossing the green forest, you have no idea where Sebas is heading, the only thing you're doing is to keep your distance and follow the lion."
    scene forest_night with dissolve
    "The night is too dark for you to see anything, so you just listen to where the sound of his footsteps come from."
    "Soon, he slows down as he enters the clearing, a wooden wagon, seated at the center, is waiting for him."
    scene mossy_freshwater_night with dissolve
    "You hide behind a decaying tree, somewhere close enough to see the shape of Sebas."
    "The aged wagon, almost camouflaged in the natural surroundings with its yellowish-green hue, emitting an eerie glow from within."
    "It illuminates a mysterious figure, casting a dark silhouette against the dimly lit interior."
    "Maybe Sebas is collecting goods for the shop? But why the need to venture out in the dead of night? You ponder aloud."
    "Leaning in for a closer look, you observs Seb walking toward a shadowy figure at the wagon's front."
    "Their conversation was brief, and the mysterious man disembarks, disappearing into the night."
    "As your roommate stealthily enters the concealed wagon, it presents the perfect opportunity to eavesdrop on his secretive exchange."
    "Coincidentally, you hear shuffling inside the wagon, before the soft rustling from within subsided, prompting your curiosity to peak."
    my "Good morrow."
    "A gravelly, hoarse voice breaks the silence, addressing the expected visitor."
    s "Mhmm."
    "Seb replies in a hushed tone, his attention seemingly elsewhere."
    my "I assume no one followed you?"
    "The stranger inquires, prompting you to press your ear against the wagon's wall to catch every word."
    s "No."
    "Seb responds, lacking the expected enthusiasm. His voice holds a tinge of detachment, as if he isn't fully engaged in the conversation."
    my "Good."
    my "My herald had news of the proposed pact from the old tailor. Had he no say in this?"
    "The mysterious man continues, his tone soft-spoken despite the implied familiarity."
    s "I convinced Rahim to consider getting along with the goats again. Mind you, it was pure persuation, I never lied to him."
    my "By all means, I was merely curious, I desire but take no part in this matter."
    s "Yes, because I'm doing the dirty work all by myself."
    "Seb retorts, his bitterness surprising even to you."

    my "I see the ire in your face. You're still mad your Uncle aided with your little pawn?"
    my "I bought the shop years ago just so you and your village friend can live there without ever worrying about gold. I expected you to understand."
    "He... is Sebas' Uncle? The revelation sends you a wave of confusion. Seb has never spoken of family, save for his mother."
    "The tension escalated as Seb's uncle addressed past grievances and Seb's sarcastic tone emerged."
    my "The only complaint from me was that you could've chosen a less revealing name for your shop, but I did not meddle with your business."
    s "I never said I'm not grateful."
    "The lion raises his voice, he sounds sarcastic, you've never heard this side of him before."
    my "So what's the matter. Why are you putting up a pout in front of me?"
    s "Oh give me a fucking break, do I really have to say {i}Your Majesty{/i} and suck your fucking cock like the others do?"
    my "Fine, keep your pout if that makes you happier. It was my fault I never had you shown in public nor did I teach you manners in court."
    "He calmly concedes, leading to a heavy silence that hangs in the frigid air."
    my "Hmm..."
    my "How fared your lizard friend? He should be here today. Is he sick again?"
    "Seb's Uncle tries to start another conversation, you notice the sihouette of the larger figure slides closer."
    s "He's talking with Jog right now."
    my "I beg your pardon, but which one?"
    s "The roommate I kicked out."
    my "Ah, forgive me. I've had more important matters on my mind over these years."
    s "I know. You should go back and attend to your more important matters."
    "Seb retorts once more, bitterness seeping through his words."
    my "Seb, you're being too careless with your words today. Remember what I said-"
    "The gruff voice begins, but Seb's interruption cut through."
    s "Fuck you, Uncle Castor."
    "Seb's outburst rattled the atmosphere, it reminds you of the practice he just had moments prior."
    ct "Huh?"
    ct "You bemuse me. Where is all this aggresion coming from?"
    s "I'm sick of you. Why can't you go away and mind your own palace and court."
    ct "You are my family. It goes without saying, I want to keep you not merely safe but thriving, be it in the palace or Lusterfield."
    s "No, you do what you do because it favours you and Lusterfield, because you're the King of Likkathia."
    ct "Nephew, I know not why I am suddenly beset by your scorn. We have trodden this path countless times before, haven't we?"
    ct "It's but a rarity I steal away every day with my guard, you know this better than anyone in the palace."
    "Castor's tone remained consistently graceful, the mild accent suggests perhaps he's from somewhere far away."
    s "Shut up with your fancy words."
    ct "Pray tell, what is in your mind, my cub?"
    "Sebas starts sniffing, you're not sure what's going on, to all you know they're just sitting inside the wagon."
    s "When I first heard Jog's meeting with Ole, I remembered what happened when we kicked him out. You remember the reason."
    ct "If my memory serves right, I recalled your fellow scout had it stolen."

    if bridgeroot.win <= 0:
        $ sebas_meetbridgeroot = True
        with vpunch
        "You hear a loud stomping sound somewhere afar, not a sound from you, but it has certainly caught the attention of the two in the wagon."
        ct "What's the matter?"
        s "Don't you change the to-"
        with vpunch
        "Sebas begins, cut off abruptly by another thunderous stomp. The tension between the two lions is momentarily overshadowed by the imminent danger approaching."
        with vpunch
        "You crawl out, squinting at the source, catching the faint outline of a massive creature along the river."
        "It is heading to the wagon, undoubtedly on the verge of attacking the two lions."
        s "Stay here, uncle Castor."
        "Sebas stands and peeks out of the wagon."
        menu:
            "Sebas could've seen you if you stay around... but the monster might hurt Sebas and his uncle. What should you do?"
            "Stay":
                $ sebas_caught = True
                "You run head first against the dark figure, leaving the explaining for your future self."
                "Its form becomes clearer as it closes in, the green moss and leaves covers most of its body."
                "Expectedly, Sebas notices your presence the moment he lifts up the curtain, but he doesn't react."
                "The sheer size looms over you, but it doesn't look to be aggressive."
                kg "My liege, the enemy approaches. We must make haste to return to the palace at once."
                "Your heart skips a beat. What have you done..."
                "The Guard rushes back towards the wagon, as Sebas walks up to you, silently."
                ct "Wait."
                ct "Sebas, what is it?"
                "He stares at the walking moss figure."
                s "No. It's... just moss."
                kg "This may be the work of a spy. We can't afford to risk it."
                "The guard pauses abruptly."
                ct "Then let us continue another time, Sebas. Stay vigilant."
                "As you and Sebas turn around, the wagon has already set off in the opposite direction."
                "Soon, you two are left alone, the leafy monster walks between the two of you, sluggishly looks ahead."
                e "Uh. I didn't expect to see you here, Seb."
                s "I should be the one saying that."
                "You watch as the moss monster wanders off in to the forest, you had thought it was a threat."
                if rahim_caught:
                    s "You were there, when me and Rahim were talking."
                    s "Why is this happening so many times? [e]."
                    e "U-uh..."
                e "I was walking down the forest at night, then I heard a loud noise and came over."
                s "Did you hear anything?"
                menu:
                    "Just a little":
                        $ sebas_justalittle = True
                        e "I only hear a little, King of... Likkathia? You shouted that word so loud the whole forest might as well hear that."
                        "Sebas squints his eyes, staring in both suspicion and uneasiness."
                        s "Just, a little?"
                        e "Yes, sorry if that was not intended for me to hear."
                    "Nothing":

                        $ sebas_justalittle = False
                        e "I just arrived here, didn't hear anything except for that loud stomp this guy's been making."
                        e "I mean, he's really a show stopper, isn't that right?"
                        "Sebas squints his eyes, staring in both suspicion and uneasiness."
                        s "Nothing, really?"
                        e "Not any words I can make out."
                s "Whatever, it's not my secret to keep."
                s "I can't believe I let him slip away again."
                if (quest32.status and not sebas_night_out) or rahim_caught:
                    $ sebas_noromance = True
                if sebas_justalittle:
                    e "Uh, was that... the king of Likkathia?"
                    s "Capital of Mokken, or whatever you call that part of the land."
                else:
                    e "I mean, I thought I was here to deal with a monster as well."
                    e "And he's just chilling."
                    "You point at the continued stomping of the moss monster, who's wandering aimlessly around the forest."
                s "I wanna go home, roomie. I'm tired."
                e "O-okay."
                s "A-and... forget what happened here, alright? Including the wagon, everything."
                if rahim_caught:
                    s "I- is it weird that I don't believe a single word you say, roomie?"
                    "Your heart sinks faster than a hurled cannonball, dragging you down."
                    s "It didn't use to be like that, I... I liked you, I still like you now. But..."
                    s "I hope this feeling goes away the next time I wake up, [e]."

                "You don't even dare to look at Seb anymore, instead the path towards Lusterfield has been all but silence, both of you has had something to ponder, and perhaps, a new perspective on each other."
                "Outside the shop, Ole is already greeting to two of you with a shocked look."
                o "You two are together? what happened-"
                s "I'm going to bed."
                "Ole inquires Sebas, who ignores him and runs upstairs quickly. His attention quickly shifts to you."
                "In shame, you lower your head."
                o "You saw the wagon?"
                "You nod."
                o "Oh... no..."
                e "I'm sorry."
                o "It's fine. I'll talk to Seb, don't fret about it. Everything will be back to normal tomorrow."
                "Despite Ole's assurance, you do not believe it ends, if ever."
                jump main_lusterfield01
            "Leave":
                $ sebas_caught = False
                "Without hesitation, you slip away through the thick grasses and run back to Lusterfield."
                "You pant heavily, wondering about the safety of Sebas and the wagon."
                "But, you can only hope they come out unscathed."
                "The conversation was cut off by the river monster, the night was so dim you couldn't even see it clearly, but it did have a shape resembling the guardian you saw."
                "Either way, it seems that Sebas secretly met with the man, perhaps talking about the Vote and its consequences on Lusterfield."
                "Jog might want to hear that nonetheless."
                jump main_lusterfield01
    s "That was the only thing I had of my mom's. And it vanished in thin air."
    s "All those days, I thought it was fucking Jog's doing, Ole believed it too."
    ct "W-what are you implying, Sebas?"
    s "It was you all along. You fucking stole the plush from me."
    ct "..."
    "Castor stammered, struggling to comprehend."
    ct "How did you know?"
    s "I thought it was weird how he had the guts to make amends. So I started looking over and over again."
    s "And I saw one of your guards walking by the shop, looking around the village."
    s "I never thought there were anyone else who's petty enough to do this, but then I remembered that same guard disguised as customer on that day."
    s "And then it dawned on me, that day your guard distracted me to check the storage so he can steal ma's plush away from me."
    s "Why?"
    pause 1
    ct "In truth, I expected you would have known sooner. We made but no effort to hide that."
    s "That's worse!"
    ct "The only reason I took it, was when I asked your lizard valet. And, I know you still missed her."
    s "So you took the only thing I had of her?"
    "His voice wavered with a mix of disbelief and disappointment."
    ct "It was a plush sewn with pure gold threads, one that was only used by the royals."
    ct "Anyone could have easily regonized the threads, and you have been careless."
    ct "And I thought getting rid of it could've allowed you to move on with your life."
    ct "I knew not you loved the doll so much, at weeks time you turned the village on its head just to find it."
    ct "Listen, I'm sorry, Sivas."
    s "That name is not for you. You're not my ma, Castor. I don't need to listen to you."
    ct "It was a tragedy what happened to her, and it pained me to pull you away from where you live. Even if you enjoyed it here."
    ct "You understand that, right?"
    ct "Sebas?"
    "Castor called, seemingly waiting for a response."
    ct "If you don't want to say anything. Shall we have a hug?"
    "You hear nothing but a slight shift in the wagon. Sebas probably nodded. And you only see the two sihoulettes overlap for a brief second."
    s "Fuck..."
    "After a long pause, you hear a few patting sound before a sihoulette of the lion getting up slowly emerges."
    ct "Stay safe, Sebas, I promised your mother that."
    s "O-okay."
    s "Next time you do this to me, you're not gonna see me again."
    ct "I don't foresee a need."
    s "You are doing this again."
    ct "What did I do?"
    s "Weaseling out of a promise with a fake one."
    ct "I promise."
    s "Fine, but I'm going back now. I'm tired."
    "Another pause between the two silhouettes ensues as you patiently wait outside the wagon, anticipating the end of their conversation."
    ct "If nothing else befalls us, then we shall meet again after the vote."
    "Sebas stands up slowly, coughing twice before he takes a step out."
    "As the shadow of a lion figure walks away, you hear a shuffling sound as he slides off the door."
    $ timer_time = 3
    $ timer_random_pause = renpy.random.random()*2
    $ renpy.pause(renpy.random.random()*2)
    show screen countdown("Jog_Vote_Sebas_Escape_Fail", 3, 2)
    menu:
        "Sebas is walking out of the wagon now."
        "Slip Away!":
            jump Jog_Vote_Sebas_Escape_Success

label Sebas_After_Castor_Caught:
    $ sebas_talkaftercaught = True
    e "About that night..."
    "Sebas sighs, his eyes fixated onto somewhere distant near the wooden door."
    s "Yeah, I know. Don't worry, I'm not blaming you, or anyone."

    if sebas_noromance:
        s "Whether you heard it or not, I don't care. In truth, it's really not my secret to keep."
        "His voice turns rough, much lower pitched than what you're used to."
        s "Last night was a mistake, my thought was wandering to a different realm it seems, but I was not in a good place."
        s "Neither am I right now."
        "He chuckles slightly, much in a dire attempt to inject his usual brightness to this awkward conversation."
        s "Well, at least now we know each other a little better! Could have hosted a roomies sleepover but whatever."
        "Swiftly, he shifts his focus onto you, a certain look in his eyes catches you off guard."
        e "Uhm... I suppose. But-"
        s "It's fine, I still like you a lot. And I don't care why you're there last night."
        e "I-"
        "You try to speak, but Sebas cuts you off again."
        s "We should really look ahead of us. I don't wanna dwell on this issue on and on... and on..."
        s "And truly, after the moment I saw you last night. There's nothing you can say that's gonna satisfy me, so please just skip over all the explaining and move on."
        "You lower your head, eyes wandering to his finger tapping on the wooden counter incoherently."
        "He's as nervous and uncomfortable as you are, but you understand, someone has to break off the stalemate."
        e "Seb, are we still friends?"
        "Letting out another sigh, you gather up the courage to ask Sebas. The weight of the question hangs in the frigid air of the pawn shop, much to the shock of the lion in front."
        s "Yes, of course! You're my roomie. That's the one thing that won't ever change!"
        "His grin wide and straight as a line, it sounds reassuring as always, but you sense a hesitation within."
        e "O-okay. I just wanted to say sorry."
        s "I know."
    else:
        s "I needed to trust you more, don't I?"
        e "Hmm, y-yes...?"
        s "That really was dumb of me to just assume the worst of you, I don't know, my head wasn't in the right place."
        s "What happened there, I'm not supposed to tell anyone at all. It could spell pretty big troubles for us if rumours' spread like wildfires. You get that... right?"
        e "I understand, Seb. I won't press on further."
        s "Thanks, roomie. You're the best."

    jump Sebas_Normal_Talk

label Jog_Vote_Report:

    e "Okay, I'm back."
    j "Got anything useful? Did Sebas do any freakish stuff back there?"
    if quest40.status == 3:
        e "I didn't do it, sorry Jog."
        jump Jog_Vote_Report_Nothing
    menu:
        "Tell Jog":
            $ jog_told = True
            if sebas_caught:
                if sebas_meetbridgeroot:
                    e "Yeah, well. But Sebas caught me when I tried to fight off a mossy monster."
                    j "Mossy monster? I've never seen that thing before."
                    j "So, what's his reaction?"
                else:
                    e "Yeah, well. But Sebas caught me while I was trying to leave."
                    j "Unlucky, so what's his reaction?"
                if sebas_noromance:
                    e "He ran away, I guess back at the shop but after that I think he recovered pretty well."
                else:
                    e "Uh, disappointed? Sad, maybe. I don't think he likes me that much now."
                j "Oh wow, he really doesn't want you to know the secret. Wait, did you involve me into that?"
                e "Nah, I was the one following him."
            else:
                e "Yeah, well. Do you really want to know?"
                j "Not as much as before, but sure, give me all ye got."
            e "Okay, Sebas was actually talking with his uncle, who's kind of asking about this alliance in Lusterfield."
            e "He's called... Castor, lives in a palace, in a town called something like Likkathia."
            j "Alright, that's... King Castor. Woah... but that makes sense, they're both lions."
            e "Yeah, they had a heated argument in the wagon there."
            if sebas_meetbridgeroot:
                e "But I got cut off when they talked about... some plush."
                e "From Castor's sister?"
                j "His mom?"
                e "I guess. After that a moss monster came and they had to leave."
                j "Eh, it's all good. I've got what I wanted so you know what, screw his plush."
            else:

                e "Seb's mother made him a plush when he was a kid, and when he arrived here, Seb lost it, and he thought you were the one stealing it."
                j "That's where I was left off of. The doll was right there on his bed if I recall correctly."
                e "And it turns out, Castor sent his guard guy to steal that plush."
                e "He didn't want him to linger over his mother, and probably obscures his identity."
                j "Did that mean what I think it means? The jackass now doesn't think I'm some evil bully that stole his thing?"
                e "Yeah, that's pretty much it."
                j "So... how did Seb do? Did he flip over the table and call him words like he did to me?"
                e "Not that I can recall, they probably hugged it out in the end, but Seb was pretty angry."
                j "Heh. Expected. I'm not gonna say anything about it."
                j "Honestly, I liked Ole more anyway, the love and praises that Seb showers you with, it's more for him than it is for you."
                j "At least Ole knows he fucked up. I would rather keep in touch with him than the lion."
                if not sebas_noromance:
                    e "I think he's gonna talk to you soon."
                    j "Maybe, we'll see."
                else:
                    e "I think I fucked up too."
                    "You sigh as Jog begins staring straight at you."
                    j "U- Don't tell me he found you there."
                    e "Well, only towards the end."
                    j "How did you explain it?"
                    e "I-I just told him I was curious. I didn't mention anything about you."
                    j "For real, I don't think you're gonna be pissing him off that much."
                    j "But, I suppose they kept it a secret for a reason. So, you'd better shut up about this for your own safety."
                    j "Especially now that you're out of the dark."
                    "You nod slowly."
        "Lie and withhold the secret":


            e "Uh, no. I couldn't risk it. There's a guard standing by when Sebas went in the wagon."
            j "Surely the guards can't be close enough. Last time I checked he's walking far far away when Sebas got inside."
            e "Uh, not this time though."
            jump Jog_Vote_Report_Nothing


    j "Either way, thanks for going through this plan with me, I wouldn't have talked to Ole in ten lifetimes."
    e "No problem."
    j "For the record, you've got my vote. Mhmm, But I gotta go and think about some explaining on the spot when Lot come asking."
    j "See ya."
    "He waves at you until you begin moving once more."
    $ QuestFinish(quest40)
    jump main_lusterfield_range

label Jog_Vote_Report_Nothing:

    $ jog_told = False

    j "Fair. Anyway, I'm past this whole curiosity now. While you were trying to stalk your precious roomie, I got my fair share of tough deal with Ole."
    j "I planned to just hang out, catching up with each other. But that guy even got nervous when I talked about the weather."
    j "So I went straight to the elephant in the room."
    j "That said, the talk was surprisingly peaceful, I mean at least after talking it out, he's finally chatting like a normal person."
    j "I don't even know why I asked at the first place, I never decided to work it out until when you asked about this whole vote."
    e "You don't want to know about Seb now?"
    j "It's not like you've got anything, but now that I got it out of my system, it's all good."
    e "Now I'm curious what Ole said to you that night."
    j "One thing about Ole is, he used to be scared of hanging out in the same tavern as we do, just stopped being there at one point. like, I'm not gonna eat his lizard ass or something."
    j "Gettin' all that scales up my tongue, nah I'm very opposed to that."
    "Jog exclaims as he takes a huge bite out of the plum."
    if quest16.status:
        j "The last time we talked, it was at that party Seb held, I was surprised Ole gave me that invitation, but face to face he's just been spewing the same type of bullshit as we last met."
    else:
        j "Hadn't talked to him since the lion flipped all over the place and kicked me out."
    j "But this time, he finally apologized, I don't know what took him so long, but he said he still didn't know who was the thief."
    j "I guess he was sorry for not talking as friends after all these years."
    j "Well, apologies accepted."
    e "Couldn't you, just talk to Ole at the first place?"
    j "Didn't bother, don't wanna. Big Ol's not the type to dwell over the past, neither am I. Why would I talk to someone who thinks I steal from them?"
    j "Either way, thanks for going through this plan with me, I wouldn't have talked to Ole in ten lifetimes."
    e "No problem."
    j "For the record, you've got my vote. Mhmm, But I gotta go and think about some explaining on the spot when Lot come asking."
    j "See ya."
    "He waves at you until you begin moving once more."
    $ QuestFinish(quest40)
    jump main_lusterfield_range

label Jog_Vote_Sebas_Escape_Fail:
    $ sebas_caught = True
    "Without enough time to react, you're stunned in place, too scared to move a muscle."
    "But the light inside of the wagon is already enough to illuminate your prescence in the dark night."
    "And consequently, you're still crouching on the side of the wagon when you see Sebas once more."

    "He seems lost in thought, contemplating something as he silently walks back towards the village."
    "And suddenly, he turns around and your eyes meet."
    show sebas scared with dissolve
    "He didn't say anything, but you're certain he noticed you right away. His eyes only widen, and his mouth hangs open."
    "The air seems frozen in place when your gaze locked, even seconds passed feels like years."
    "Sebas slowly waves away the guard, you can't see what's in the front. But the wagon soon sets off, disappearing from behind you."
    "Regardless, his gaze remains fixated onto yours, and you find yourself clutching the grasses in nervousness."
    "It's only after the wagon is completely out of your sight, does Sebas finally speak."
    menu:
        s "H-how much did you hear?"
        "Just a little":
            $ sebas_justalittle = True
            e "J-just a little. I was just curious where you've been, Seb."
            "Sebas' eyes droops lower, he furrows his brows, giving you a sullen look."
        "Everything":
            $ sebas_justalittle = False
            e "I- I followed you here, and heard everything inside the wagon."
            "Sebas' still taking time to process whatever happened here, but his stare has soften."
    s "Okay."
    if (quest32.status and not sebas_night_out) or rahim_caught:
        $ sebas_noromance = True
    "Sebas mutters under his breath, his voice is much lower than what you normally hear from the lion."
    "Frustration and disappointment etch his face, and you sense the weight of his emotions."
    "You catch a glimpse of Sebas looking away, he wants to forgive you so much even in face of the betrayal of his trust, but he's not able to."
    "Instead, he turns away without another word."
    hide sebas with dissolve
    "Quickly, you rise to your feet to chase after him, but he's already running back to Lusterfield, leaving you alone in the forest once more."
    jump main_mossy_freshwater

label Jog_Vote_Sebas_Escape_Success:
    $ sebas_caught = False
    hide screen countdown
    "Without hesitation, you slip away through the thick grasses and run back to Lusterfield."
    jump main_lusterfield01

screen countdown(jump_label, timer_range=1, timer_multi=2):
    timer 0.05 repeat True action If(timer_time > 0, true=SetVariable("timer_time", timer_time - timer_multi*0.05), false=[Hide('countdown'), Jump(jump_label)])

    bar value timer_time+1 range timer_range xalign 0.5 yalign 0.7 xmaximum 300 at alpha_dissolve

label Arthur_Voting_Opinion:
    if arthur_2ndChoice == "Good" or arthur_2ndChoice == "Bad":
        e "M-master, how do you think about the vote...?"
    else:
        e "Arty, how do you think about the vote in Lusterfield?"
    ar "Vote? What vote. Why hadn't I heard of that?"
    e "Aren't farmers also invited for the voting day? I really thought Amble or Jog would tell you about it."
    msg "Arthur's Vote currently working in progress, will be continued in the next update!"

    jump Arthur_Normal_Talk


label Rahim_Dialogue_End:
    e "That's all, thank you for chatting, Rahim."
    r "Ok. Take care."
    jump main_rahimshop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
