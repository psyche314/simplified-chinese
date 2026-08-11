label bandit_battle:


    $ enemy_num = 1
    $ enemy = bandit
    call beginningBattle from _call_beginningBattle_24

    $ enemy.max_hp = 690
    $ enemy.min_damage = 53
    $ enemy.max_damage = 80
    $ enemy.min_lust_damage = 20
    $ enemy.max_lust_damage = 28
    $ enemy.dodge = 28
    $ enemy.defense = 65
    $ enemy.lust_defense = 36
    $ enemy.exp_drop = 35
    $ enemy.beginbattle()
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    scene bandits_hideout:
        blur 8
    show bandit:
        xalign 0.5
        yalign 0.25
    if pc.weapon == None:
        "You are facing a bandit, and he's waving his daggers, not hesitating to strike at you."
    else:
        "You are facing a bandit, and he's waving his daggers, not hesitating to strike at you. You pull out your [pc.weapon.name!t]."
    bd "So, you think you're tough? Let's see what you've got, adventurer!"
    jump bandit_battle_loop

label bandit_battle_loop:
    show bandit:
        xalign 0.5
        yalign 0.4

    if check_party(pc) == "lost":
        call Battle_Finish from _call_Battle_Finish_36
        jump bandit_lose
    $ turn_action = ui.interact()
    call Battle_ASF from _call_Battle_ASF_24
    if oa[0] == "A" or oa[0] == "S":
        call battle_attack_script from _call_battle_attack_script
    if oa[0] == "F":
        call battle_flirt_script from _call_battle_flirt_script
    call battle_escape_surrender_script from _call_battle_escape_surrender_script
    call Ability_Item from _call_Ability_Item_25
    call Battle_Mid_Check from _call_Battle_Mid_Check_23
    if oa[0] == "W":
        call Battle_Finish from _call_Battle_Finish_84
        jump bandit_win
    if oa[0] == "T":
        call Battle_End_Check from _call_Battle_End_Check_50
        jump bandit_battle_loop
    show bandit:
        linear 0.1 zoom 1.04
        linear 0.05 zoom 1


    $ dia = renpy.random.random()
    if dia < 0.35:
        if renpy.random.random()*100 > pc.dodge + extra_dodge:
            $ total_enemy_damage = 0
            $ raw_damage = int(renpy.random.randint(bandit.min_damage, bandit.max_damage) / 3)
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_49
            $ total_enemy_damage += enemy_damage
            pause .25
            $ raw_damage = int(renpy.random.randint(bandit.min_damage, bandit.max_damage) / 3)
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_50
            $ total_enemy_damage += enemy_damage
            pause .25
            $ raw_damage = int(renpy.random.randint(bandit.min_damage, bandit.max_damage) / 3)
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_51
            $ total_enemy_damage += enemy_damage
            if pc.hp < 0:
                $ pc.hp = 0
            "The bandit charges forwards, swinging his dagger onto you multiple times. Your health decreases by [total_enemy_damage] HP."
            $ rand = renpy.random.random()
            if pc.hp > pc.max_hp/2:
                if rand > 0.5:
                    bd "You're no match for my skills! Prepare to be defeated!"
            else:
                if rand > 0.5:
                    bd "Ha! I could do this all day. Can you even put up a fight?"
                else:
                    bd "You're no match for me! Surrender now and save yourself some bruises!"
        else:
            "The bandit charges forwards, trying to swing his dagger, but you manage to dodge the attack."
            if renpy.random.random() > 0.5:
                bd "You're slippery! Stand still and let me hit you!"
            else:
                bd "Damn! Just wait, I'll get you next time! It won't save you forever."

    elif dia < 0.6:
        $ raw_damage = int(renpy.random.randint(bandit.min_damage, bandit.max_damage))
        $ enemy_damage = damageFormula(raw_damage, pc.defense)
        call Damaging (enemy, pc, enemy_damage) from _call_Damaging_52
        "The bandit disappears for a moment..."
        "You look around, it seems he has escap-"
        "TW-ANGGG-"
        "He strikes at you from behind, while stealing gold from you. Dealing [enemy_damage] HP."
        call lost_gold_check (0.02, 25) from _call_lost_gold_check
        bd "Didn't see this coming, haha. Pethetic!"

    elif dia < 0.9 and bandit.hp > bandit.max_hp / 3 * 2:
        $ heal_amount = int(renpy.random.randint(40, 80))
        "The bandit drinks a health potion."
        call Enemy_Self_Healing (enemy, heal_amount) from _call_Enemy_Self_Healing_9
    else:

        $ random_chance = renpy.random.random()
        if random_chance < 0.5:
            "The bandit scratches at his pants, he runs two fingers along the shape of his cock in front of you."
            bd "You'd like my cock inside of you, adventurer!"
        else:
            "The bandit stretches his body, flaunting his muscular physiques, you can tell his soft chest is almost bulging in front of you."
            bd "Surrender and we'll just make you into our plaything. Isn't that what you're here for?"
        if renpy.random.random()*100 > pc.lust_dodge + extra_lust_dodge:
            $ raw_flirt = int(renpy.random.randint(bandit.min_lust_damage, bandit.max_lust_damage))
            $ enemy_flirt = damageFormula(raw_flirt, pc.lust_defense)
            $ pc.lust += enemy_flirt
            if pc.lust > pc.max_lust:
                $ pc.lust = pc.max_lust
            if dia > 0.9:
                "You gulp at the bandit's attempt at seduction. Admittedly you are extremely aroused, thinking about how his cock would taste like."

                "Your lust increased by [enemy_flirt]."
            else:
                "You are stunned by his gorgeous muscles, you mind wanders through scenarios of him being inside your body."
                "Your lust increased by [enemy_flirt]."
        else:
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "You stare at him, giving him weird side eyes. You have evaded his attempt at seduction. And the bandit seems to feel a little dejected."
            else:

                "His attack at your lust seems to have failed as you stand there and wait for him to finish his taunt."
                "Both of you would never speak about it again."
    call Battle_End_Check from _call_Battle_End_Check_51
    jump bandit_battle_loop

label bandit_win:
    hide bandit
    "The bandit is lying on the floor, still panting..."
    bd "My wounds will heal, and my brothers... we'll make you pay for this!"
    $ bandit.win += 1
    "He says furiously, but quickly composes when you stand in front of him."
    bd "S-shit alright, alright. You win this time. I won't collect your toll... today."
    "You raise your fist towards the bandit again."
    bd "O-ok, alright. 3 days without toll."
    $ bandit_toll_day = timenow.day + 3
    if bandit.lust >= 50:
        menu:
            "Do you want to... have fun with the bandit?"
            "Yes{#banditwin}":
                "..."
                call Scene_Bandit_Win from _call_Scene_Bandit_Win
                $ pc.lust = 0
            "No{#banditwin}":
                pass
    else:
        "You search around the bandit before letting him go."
    call level_up_check (305, 400, 165, 220) from _call_level_up_check
    jump main_bandits_hideout

label bandit_lose:
    hide bandit
    if pc.hp <= 0:
        "You struggle against the bandit, you have already exhausted all your energy. He pounces on your helpless body like you are a feast to be served."
    if pc.lust >= pc.max_lust:
        "You struggle against the bandit, your mind is filled with unquenchable lust over the bandit. He pounces on your helpless body like you are a feast to be served."
    $ bandit.lose += 1
    "The bandit smirks, he drags you towards the stone building, checking you out with a sinister look."
    if bandit.lose > 1:
        menu:
            "Do you want to replay the losing scene?"
            "Yes{#banditlosereplay}":
                call Scene_Bandit_Gangbang (True) from _call_Scene_Bandit_Gangbang_1
            "No{#banditlosereplay}":
                pass
    else:
        call Scene_Bandit_Gangbang (True) from _call_Scene_Bandit_Gangbang_2
    if bandit_gangbanged + bandit.lose >= 3 and pc.cor < 85:
        jump BadEnd_Bandit_Bondage
    $ pc.add_active_status(stuffed)
    call lost_gold_check (0.15, 90, True) from _call_lost_gold_check_1

    scene bandits_hideout
    "And when you wake up from the darkness, you're already out of the bandit's hideouts."
    "Apparently they've decided to let you go, you are so wasted from these few hours serving those bandits."
    "You can't imagine what a lifetime of being used for pleasure would feel like, not that you'd want to know."
    "But at least, you're spared of your freedom, for now."
    jump main_bandits_hideout

label gnoll_battle:


    $ enemy_num = 1
    $ enemy = gnoll
    call beginningBattle from _call_beginningBattle_26

    $ enemy.max_hp = 690
    $ enemy.min_damage = 51
    $ enemy.max_damage = 85
    $ enemy.min_lust_damage = 28
    $ enemy.max_lust_damage = 46
    $ enemy.dodge = 20
    $ enemy.defense = 62
    $ enemy.lust_defense = 35
    $ enemy.exp_drop = 35
    $ enemy.beginbattle()
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    scene prattlefell_meadow:
        blur 8
    show gnoll:
        xalign 0.5
        yalign 0.25

    "You are facing a gnoll, staring at you curiously, he raises his rock and prepares to fight you tooth and nails."

    jump gnoll_battle_loop

label gnoll_battle_loop:

    show gnoll:
        xalign 0.5
        yalign 0.4

    if check_party(pc) == "lost":
        call Battle_Finish from _call_Battle_Finish_85
        jump gnoll_lose
    $ turn_action = ui.interact()
    call Battle_ASF from _call_Battle_ASF_25
    if oa[0] == "A" or oa[0] == "S":
        call battle_attack_script from _call_battle_attack_script_1
    if oa[0] == "F":
        call battle_flirt_script from _call_battle_flirt_script_1
    call battle_escape_surrender_script from _call_battle_escape_surrender_script_1
    call Ability_Item from _call_Ability_Item_26
    call Battle_Mid_Check from _call_Battle_Mid_Check_24
    if oa[0] == "W":
        call Battle_Finish from _call_Battle_Finish_86
        jump gnoll_win
    if oa[0] == "T":
        call Battle_End_Check from _call_Battle_End_Check_52
        jump gnoll_battle_loop
    show gnoll:
        linear 0.1 zoom 1.04
        linear 0.05 zoom 1


    $ dia = renpy.random.random()
    if dia < 0.4:
        if renpy.random.random()*100 > pc.dodge + extra_dodge:
            $ total_enemy_damage = 0
            $ raw_damage = int(renpy.random.randint(gnoll.min_damage, gnoll.max_damage) / 3)
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_53
            $ total_enemy_damage += enemy_damage
            pause .25
            $ raw_damage = int(renpy.random.randint(gnoll.min_damage, gnoll.max_damage) / 3)
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_54
            $ total_enemy_damage += enemy_damage
            pause .25
            $ raw_damage = int(renpy.random.randint(gnoll.min_damage, gnoll.max_damage) / 3)
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_55
            $ total_enemy_damage += enemy_damage
            if pc.hp < 0:
                $ pc.hp = 0
            "The ferocious gnoll bursts out from nowhere, slashing you with his sharp claws multiple times. Your health decreases by [total_enemy_damage] HP."
            $ rand = renpy.random.random()
            if pc.hp > pc.max_hp/2:
                if rand > 0.5:
                    gnl "Swift and sly, gnoll strikes hard."
            else:
                if rand > 0.5:
                    gnl "You fast, but gnoll faster!"
                else:
                    gnl "Jump, spin, gnoll catches indeed."
        else:
            "The ferocious gnoll bursts out from nowhere, trying to slash you with his sharp claws multiple times, but you manage to dodge the attack."
            if renpy.random.random() > 0.5:
                gnl "Slippery toes, runs no more!"

    elif dia < 0.7:
        $ raw_damage = int(renpy.random.randint(gnoll.min_damage, gnoll.max_damage))
        $ enemy_damage = damageFormula(raw_damage, pc.defense)
        call Damaging (enemy, pc, enemy_damage) from _call_Damaging_56
        "The gnoll approaches and pushes you onto the ground."
        $ isCharmed = next((x for x in status if x.img == "Charmed"), None)
        if isCharmed not in status:
            $ ApplyStatus(status, charmed, 3)


            "He presses his chest against you as you're still struggling from his grasp, his snout draws near."
            "You can feel his hot breath exhaling all around you, driving you dizzy and your head spins even after he has released you."
            gnl "Dance with lust, gnoll charms!"
            "You are now charmed, and your HP decreases by [enemy_damage]."
        else:

            $ isCharmed.rounds += isCharmed.max_rounds
            "He licks your face, drenching your cheeks with his slobs, as you're already in your entranced state."
            gnl "More, more!"
            "You are much more entranced by the gnoll now, and your HP decreases by [enemy_damage]."
    else:

        $ random_chance = renpy.random.random()
        if random_chance < 0.5:
            "The gnoll scratches at his pants, he runs two fingers along the shape of his cock in front of you."
            gnl "Come, and get some!"
        else:
            "The gnoll stretches his body, flaunting his muscular physiques, you can tell his soft chest is almost bulging in front of you."
            gnl "Gnoll takes hold, and you release!"
        if renpy.random.random()*100 > pc.lust_dodge + extra_lust_dodge:
            $ raw_flirt = int(renpy.random.randint(gnoll.min_lust_damage, gnoll.max_lust_damage))
            $ enemy_flirt = damageFormula(raw_flirt, pc.lust_defense)
            $ pc.lust += enemy_flirt
            if pc.lust > pc.max_lust:
                $ pc.lust = pc.max_lust
            if dia > 0.9:
                "You gulp at the gnoll's attempt at seduction. Admittedly you are extremely aroused, thinking about how his cock would taste like."

                "Your lust increased by [enemy_flirt]."
            else:
                "You are stunned by his gorgeous muscles, you mind wanders through scenarios of him being inside your body."
                "Your lust increased by [enemy_flirt]."
        else:
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "You stare at him, giving him weird side eyes. You have evaded his attempt at seduction. And the gnoll seems to feel a little dejected."
            else:

                "His attack at your lust seems to have failed as you stand there and wait for him to finish his taunt."
                "Both of you would never speak about it again."
    call Battle_End_Check from _call_Battle_End_Check_53
    jump gnoll_battle_loop

label gnoll_win:
    hide gnoll
    $ gnoll.win += 1
    $ exp_drop = renpy.random.randint(295, 370)
    if equippedTrinket("Lindbloom"):
        $ rnd = 0.8
    else:
        $ rnd = 0.4
    "The gnoll is lying on the floor, still panting..."
    if renpy.random.random() <= rnd:
        "As you search around the gnoll, you found three strips of leather, and a bundle of soft fur!"
        $ addItem("Leather Strips", inventory, 3)
        $ addItem("Soft Fur", inventory, 1)
    else:
        "As you search around the gnoll, you found a bundle of soft fur!"
        $ addItem("Soft Fur", inventory, 1)
    if callInventoryItem("Songweaver Cloak", "Clothes"):
        "You also found a piece of colourful garment, a cloak that seems to be worn by... a famous bard?"
        $ addItem("Songweaver Cloak", inventory, 1)
    if gnoll.win >= 1 and gnoll.lust > 50:
        menu:
            "Do you want to... have fun with the gnoll?"
            "Yes{#gnollwin}":
                "..."
                call scene_gnoll_win_top from _call_scene_gnoll_win_top
                $ pc.lust = 0
            "No{#gnollwin}":
                pass
    else:
        "Quickly, the gnoll crawls away, just before your eyes."
    call level_up_check (295, 370, 45, 69) from _call_level_up_check_1
    jump main_prattlefell_meadow

label gnoll_lose:
    hide gnoll
    if pc.hp <= 0:
        "You struggle against the gnoll, you have already exhausted all your energy. He pounces on your helpless body like you are a feast to be served."
    if pc.lust >= pc.max_lust:
        "You struggle against the gnoll, your mind is filled with unquenchable lust over the gnoll. He pounces on your helpless body like you are a feast to be served."
    $ gnoll.lose += 1
    if gnoll.lose > 1:
        menu:
            "Do you want to replay the losing scene?"
            "Yes{#gnolllosereplay}":
                call scene_gnoll_lose from _call_scene_gnoll_lose
            "No{#gnolllosereplay}":
                pass
    else:
        call scene_gnoll_lose from _call_scene_gnoll_lose_1
    call lost_gold_check (0.11, 70, True) from _call_lost_gold_check_2
    jump main_prattlefell_meadow

label bridgeroot_battle:


    $ enemy_num = 1
    $ enemy = bridgeroot
    call beginningBattle from _call_beginningBattle_27

    $ enemy.max_hp = 950
    $ enemy.min_damage = 61
    $ enemy.max_damage = 95
    $ enemy.min_lust_damage = 0
    $ enemy.max_lust_damage = 0
    $ enemy.dodge = 15
    $ enemy.defense = 60
    $ enemy.lust_defense = 51
    $ enemy.exp_drop = 540
    $ enemy.beginbattle()

    $ ally = amblebr
    $ ally_num = 2
    $ ally.beginbattle()
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    scene riverside_crossing_construction_3:
        blur 8
    show bridgeroot:
        xalign 0.5
        yalign 0.25
    $ enemy_image = enemy.img.lower()

    "You are facing a bridgeroot, he slowly stands up in defense as you prepare to chase away the mossy creature with Amble."

    jump bridgeroot_battle_loop

label bridgeroot_battle_loop:

    show expression enemy_image:
        xalign 0.5
        yalign 0.4

    if check_party(pc) == "lost" and check_party(ally) == "lost":
        call Battle_Finish from _call_Battle_Finish_87
        jump expression enemy.img.lower().replace(" ","") + "_lose"

    if battleTurn == "Player":
        if check_party(pc) != "lost":
            "It's your turn now."
            $ turn_action = ui.interact()
        else:
            $ turn_action = "No"
    else:
        $ ItemTab = False
        $ AbilityTab = False
        if check_party(ally) != "lost":
            "It's [ally.name]'s turn now."
            $ turn_action = ui.interact()
        else:
            $ turn_action = "No"

    call Battle_ASF from _call_Battle_ASF_26
    if oa[0] == "A" or oa[0] == "S":
        call battle_attack_script from _call_battle_attack_script_2
    if oa[0] == "F":
        call battle_flirt_script from _call_battle_flirt_script_2
    call battle_ally_script from _call_battle_ally_script
    call battle_escape_surrender_script from _call_battle_escape_surrender_script_2
    call Ability_Item from _call_Ability_Item_27
    call Battle_Mid_Check from _call_Battle_Mid_Check_25
    if oa[0] == "W":
        call Battle_Finish from _call_Battle_Finish_88
        jump expression enemy.img.lower().replace(" ","") + "_win"
    if oa[0] == "T":
        call Battle_End_Check from _call_Battle_End_Check_54
        jump bridgeroot_battle_loop
    show expression enemy_image:
        linear 0.1 zoom 1.04
        linear 0.05 zoom 1


    $ ttg = renpy.random.choice([pc, ally])
    $ dia = renpy.random.random()
    call bridgeroot_turn from _call_bridgeroot_turn
    call Battle_End_Check from _call_Battle_End_Check_55
    jump bridgeroot_battle_loop

label bridgeroot_turn:

    if dia < 0.4:
        if renpy.random.random()*100 > ttg.dodge + extra_dodge:
            $ raw_damage = int(renpy.random.randint(bridgeroot.min_damage, bridgeroot.max_damage))
            $ enemy_damage = damageFormula(raw_damage, ttg.defense)
            call Damaging (enemy, ttg, enemy_damage) from _call_Damaging_57

            "The bridgeroot swings his grass fist, knocking you back with his sheer strength. Your health decreases by [enemy_damage] HP."
            $ raw_damage = int(renpy.random.randint(bridgeroot.min_damage, bridgeroot.max_damage))
            $ healing = int(raw_damage * 0.5)
            call Enemy_Self_Healing (bridgeroot, healing) from _call_Enemy_Self_Healing_10
        else:
            "The bridgeroot swings his grass fist, but you manage to dodge the attack."
    elif dia < 0.7 and bound not in status:
        "The bridgeroot holds you in place. You try to struggle free, but it doesn't work."
        $ status.append(bound)
        $ grip_strength = bound.effect
    elif dia < 0.7:
        if renpy.random.random()*100 > ttg.dodge + extra_dodge:
            $ raw_damage = int(renpy.random.randint(bridgeroot.min_damage, bridgeroot.max_damage))
            $ enemy_damage = damageFormula(raw_damage, ttg.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_58
            call Damaging (enemy, ally, enemy_damage) from _call_Damaging_59

            "The bridgeroot lurches, he shoots some sort of sharp grasses onto you. Draining both of your health by [enemy_damage] HP."
            call Enemy_Self_Healing (bridgeroot, raw_damage) from _call_Enemy_Self_Healing_11
        else:
            "The bridgeroot lurches, but you quickly dodge his attack."
    else:
        "Every green part of the bridgeroot begins to convulse. His body is suddenly revitalised by the power of water."
        $ raw_damage = int(renpy.random.randint(bridgeroot.min_damage, bridgeroot.max_damage))
        call Enemy_Self_Healing (bridgeroot, int(raw_damage * 0.5)) from _call_Enemy_Self_Healing_12

    if bound in status:
        "You can still feel yourself being wrapped around by the bridgeroot, refusing to let you go."
        "The herbs on his body is unbearably strong, causing your mind to go fuzzy... your lust is increased by 15."
        $ pc.lust += 15
    return

label bridgeroot_win:
    hide expression enemy_image
    $ bridgeroot.win += 1
    $ quest38.status = 6
    "A loud, shrieking growl of pain can be heard from the mossy monster, its pulsation can almost be felt as you take a step back."
    show bridgeroot:
        linear 0.1 xalign 0.45
        linear 0.1 xalign 0.55
        repeat 2
        linear 0.1 xalign 0.5
    "It... it doesn't look normal, and the bridgeroot charges at you, knocking you on the ground."
    "You try to make his arm let go, but his grasps are too tight. You can feel moss growing around you, locking you in place."
    "Perhaps this is a last resort from the brigeroot, as it keeps itself on top of you, the sheer weight of this giant is suffocating you bit by bit."
    e "A-amb!"
    "You stare at Amble, who just stands here, he is completely petrified, glancing between you and the bridgeroot."
    "He remains frozen for a few more seconds, and you seem to be running out of air, your vision blurs as it is replaced by patches of greenery."
    a "Haargh!"
    show bridgeroot:
        linear 0.08 xalign 0.45
        linear 0.08 xalign 0.55
        repeat 4
        linear 0.05 xalign 0.5
    "Amble swings his hammer towards its head, and its shrieks just get louder all at once, which has shaken your very soul."
    show bridgeroot:
        linear 0.06 xalign 0.45
        linear 0.06 xalign 0.55
        repeat 8
        linear 0.05 xalign 0.5
    with flash
    scene black with dissolve
    pause 1

    "The bridgeroot rises up, and then suddenly, it falls to the side with a resounding thump."
    pause 1
    call showing_riverside_crossing from _call_showing_riverside_crossing_2
    "It's a long time since you take a breath, so you just lie there, trying to take in your breath as Amble extends his hand for you to stand up."
    "You stare at the scene, the moss monster quickly fades into stillness as its green colour turns into a dull brown, before sinking itself into the earth."
    e "I-I am so sorry, I know I promised we wouldn't kill him."
    "He nods, almost hesitantly."
    show amble normal with dissolve
    a "You were in danger right there, I had to."
    "Amble kneels down, swirling his finger against the dirts where the monster once resided."
    a "It was like what Lot described."
    "You notice he slowly closes aimless eyes shut, his ears only droop lower."
    e "The monster?"
    a "Oh, yes. The monster, was it the golem... he mentioned to me that the one from the goats was making some troubles around the river."
    a "Maybe, he made a good friend in the river here?"
    e "Well, at least this one didn't want to outright murder us, immediately."
    "He gives you a few glances."
    a "Let's continue our work, good friend."
    "Amble grins, but you can tell there's still tint of sadness in his glistening eyes, even as he doesn't like to show this side of him."
    hide amble with dissolve
    call level_up_check (295, 370, 45, 69) from _call_level_up_check_2
    jump Amble_Voting_Continue_Last_Stretch_Start

label bridgeroot_lose:
    hide bridgeroot
    $ bridgeroot.lose += 1
    "You notice the bridgeroot staring at you for a moment, before sitting back on the pedestal again."
    "Both you and Amble shakes your head as you sigh in exhaustion."
    a "Ahhh! What a bummer, it doesn't look like we're scaring him away."
    e "W-what should we do?"
    a "I think we should just take some rest, and then come back and hope he's gone."
    e "Shouldn't we try again?"
    a "I... I don't want to kill him, if he's being this stubborn, we'll soon left with no choice if we keep on fighting."
    "Amble points at the bridgeroot, who's sitting on the bridge, watching water flow by."
    e "I suppopse you're right, Amble."

    jump main_riverside_crossing

label vurro_spar_battle:


    $ enemy_num = 1
    $ enemy = vurroSpar
    call beginningBattle from _call_beginningBattle_28
    $ enemy.max_hp = 450
    $ enemy.min_damage = 61
    $ enemy.max_damage = 100
    $ enemy.min_lust_damage = 31
    $ enemy.max_lust_damage = 48
    $ enemy.dodge = 34
    $ enemy.defense = 85
    $ enemy.lust_defense = 40
    $ enemy.exp_drop = 522
    $ enemy.beginbattle()
    $ enemy.img = "vurro_spar"
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    scene slumbrous_well:
        blur 8
    $ enemy_image = "vurro_spar"
    "Vurro raises his nails, his scrawny furs doesn't hide his tired face, but he still holds out a wide smile."

    jump general_battle_loop

label general_battle_loop:

    show expression enemy_image:
        xalign enemy.item_chance01
        yalign 0.4

    if check_party(pc) == "lost":
        call Battle_Finish from _call_Battle_Finish_91
        jump expression enemy.img.lower().replace(" ","") + "_lose"
    $ turn_action = ui.interact()
    call Battle_ASF from _call_Battle_ASF_27
    if oa[0] == "A" or oa[0] == "S":
        call battle_attack_script from _call_battle_attack_script_3
    if oa[0] == "F":
        call battle_flirt_script from _call_battle_flirt_script_3
    call battle_escape_surrender_script from _call_battle_escape_surrender_script_3
    call Ability_Item from _call_Ability_Item_28


    jump general_battle_midTurn

label general_battle_midTurn:
    $ enemy_loop = enemy.img + "_battle_loop"
    call Battle_Mid_Check from _call_Battle_Mid_Check_26
    if oa[0] == "W":
        call Battle_Finish from _call_Battle_Finish_92
        jump expression enemy.img.lower().replace(" ","") + "_win"
    if oa[0] == "T":
        call Battle_End_Check from _call_Battle_End_Check_56
        jump general_battle_loop
    show expression enemy_image:
        linear 0.1 zoom 1.04
        linear 0.05 zoom 1

    jump expression enemy.img.lower().replace(" ","") + "_battle_loop"



label vurro_spar_battle_loop:


    $ isWounded = next((x for x in status if x.img == "Wounded"), None)

    $ dia = renpy.random.random()
    if dia < 0.3:
        if renpy.random.random()*100 > pc.dodge + extra_dodge:
            $ total_enemy_damage = 0
            $ raw_damage = int(renpy.random.randint(vurroSpar.min_damage, vurroSpar.max_damage) / 3)
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_60
            $ total_enemy_damage += enemy_damage
            pause .25
            $ raw_damage = int(renpy.random.randint(vurroSpar.min_damage, vurroSpar.max_damage) / 3)
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_61
            $ total_enemy_damage += enemy_damage
            pause .25
            $ raw_damage = int(renpy.random.randint(vurroSpar.min_damage, vurroSpar.max_damage) / 3)
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_62
            $ total_enemy_damage += enemy_damage
            if pc.hp < 0:
                $ pc.hp = 0
            "Vurro gets near you and slashing you with his sharp claws multiple times."
            "At least he made sure to be gentle with you. Your health decreases by [total_enemy_damage] HP."
        else:
            "The brown werewolf bursts out from nowhere, trying to slash you with his sharp claws multiple times, but you manage to dodge the attack."

    elif dia < 0.5:
        if renpy.random.random()*100 > pc.dodge + extra_dodge:

            $ raw_damage = int(renpy.random.randint(vurroSpar.min_damage, vurroSpar.max_damage) / 3)
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_63

            if pc.hp < 0:
                $ pc.hp = 0
            "Vurro punches you directly with his fist. Knocking you out momentarily. Your health decreases by [enemy_damage] HP."
        else:
            "Vurro tries to punch you, but he misses just above your fur, he stands back in frustration."
            v "Look at that movement, you're doing pretty good."

    elif dia < 0.7:
        $ raw_damage = int(renpy.random.randint(vurroSpar.min_damage, vurroSpar.max_damage))
        $ enemy_damage = damageFormula(raw_damage, pc.defense)
        call Damaging (enemy, pc, enemy_damage) from _call_Damaging_64
        if renpy.random.random() < 0.3:
            v "Be careful, you might bleed for a while."
        "Vurro slashes his hand across you, his claws easily scraping against your side. Your health decreases by [enemy_damage] HP."

        if isWounded == None:
            $ ApplyStatus(status, wounded, 5)
            "You begin to bleed from your wound."
            v "Huh, my claws are really getting sharper."
        else:
            $ wounded.rounds += wounded.max_rounds
            "Your bleeding has gotten worse from Vurro."
            v "It's so weird... your blood scent is making me all dizzy."

    elif isWounded != None:
        $ missing_hp = vurroSpar.max_hp - vurroSpar.hp
        $ heal_amount = int(missing_hp*renpy.random.random()*0.2 + 30)
        "Vurro heaps a potion from his back pocket."
        if renpy.random.random() < 0.5:
            v "Technically, Uffe doesn't like potions, but he might heal himself in some ways."
        call Enemy_Self_Healing (bridgeroot, heal_amount) from _call_Enemy_Self_Healing_13
    else:

        "The brown werewolf raises his fist and swing swiftly towards your head."
        if renpy.random.random()*100 > pc.dodge + extra_dodge:
            "It hits you pretty hard as you hold onto your nose, you are stunned for one round."
            call Battle_End_Check from _call_Battle_End_Check_57
            jump vurro_spar_battle_loop
        else:
            "You quickly tilt your head to the side, narrowly dodging his attack."
            if renpy.random.random() < 0.3:
                v "Oh, you're quicker than I thought!"
    call Battle_End_Check from _call_Battle_End_Check_58
    jump general_battle_loop

label vurro_spar_win:
    $ vurroSpar.win += 1

    v "U...ughhh..."
    show expression enemy_image:
        linear 0.1 xalign 0.46
        linear 0.1 xalign 0.54
        linear 0.1 xalign 0.46
        linear 0.1 xalign 0.54
        linear 0.1 xalign 0.5

    e "V-vurro?"
    "The brown werewolf in front of you looks extremely exhausted, struggling to open his eyes in front of you."
    show expression enemy_image:
        easeout 0.5 yalign -1500.0
    "Suddenly, he falls forwards to the ground with a big thump, raising a gust of dirts and grasses."

    with vpunch
    e "H-hey! Vurro!"
    hide expression enemy_image
    e "F-fuck, no. Wake up. Vurro!"
    "You rush towards the werewolf in full speed, leaning onto his chest to check for his pulse."
    pause 0.5
    "For a few seconds, a loud doubt reverberates in your mind, telling you that you've just killed... your own friend."
    v "[e]...?"
    "He opens his eyes again, blinking. Staring at your worried face."
    v "I-... I heard you screaming."
    "You hold your hand over your mouth in shock, all of these transpired in mere seconds, and you have no idea how to react to that."
    v "S-shit... That was close. I almost fell asleep."
    "His eyes widen, nails almost bury themselves into his own skin, leaving behind lines of red marks underneath his fur."
    e "W-what happened? Vurro?"
    "Vurro's breathing rhythm quickens, his pupil expands just after having experienced being near death."
    pause 1
    "A few seconds have passed as you sit alongside Vurro, accompanied by a series of gasps and abrupt breathing."
    v "I- I think I almost died."


    jump Wuldon_Raid_Bath

label vurro_spar_lose:
    hide expression enemy_image
    $ vurroSpar.lose += 1
    e "I... I lost... Vurro?"
    "Without enough stamina to keep fighting, you shout to the brown werewolf, who seems a little different than usual."
    "He only grunts, loudly."
    e "Vurro?"
    "You shout once more, but he doesn't seem to notice."
    with vpunch
    "With a swing of his claws, a gust of wind come propelling you in the air, sending you across the forest."

    scene black with dissolve




    "You only stop when your back and head comes into contact with a tree, putting a brake on a fleeting flight."
    scene dark_forest with dissolve2
    pause 0.5
    with blackflash
    pause 0.5
    with blackflash
    v "Oh shit... Are you alright? [e]?"
    with blackflash
    "You fall limp on the dirt, consciousness fades in and out momentarily as your eyes almost closed."
    v "I- I'm so sorry. That feral's strength, it's coming back in me and I had no idea."
    e "Ugh...u-ugh..."
    "For a moment your vision blurred into blobs of green, but Vurro manages to get a hold of your injury."
    e "I- unngh... F-fuck. My head is hurting."
    "You clutch the back of head, almost the same place you were knocked out of."
    v "Shit. Any bleeding still needed to be taken care of?"
    e "I-I don't think so. I definitely underestimated your power, didn't expect a gust of wind to blow me away like that."


    jump Wuldon_Raid_Bath

label spriteling_battle:


    $ enemy_num = 1
    $ enemy = spriteling
    call beginningBattle from _call_beginningBattle_29
    if current_location == temple_of_tapjoo:
        $ enemy.max_hp = 450
        $ enemy.min_damage = 52
        $ enemy.max_damage = 70
        $ enemy.min_lust_damage = 8
        $ enemy.max_lust_damage = 15
        $ enemy.dodge = 32
        $ enemy.defense = 53
        $ enemy.lust_defense = 80
        $ enemy.exp_drop = 30
        scene temple_of_tapjoo:
            blur 8
    else:
        $ pc.mp = 0
        $ enemy.max_hp = 30
        $ enemy.min_damage = 8
        $ enemy.max_damage = 15
        $ enemy.min_lust_damage = 8
        $ enemy.max_lust_damage = 15
        $ enemy.dodge = 32
        $ enemy.defense = 22
        $ enemy.lust_defense = 80
        $ enemy.exp_drop = 30
        scene puro_forest:
            blur 8
    $ enemy.beginbattle()
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons

    $ enemy_image = "spriteling"
    "The small spriteling thrashes its ephereal claws about, but you doubt it deals any damage."

    jump general_battle_loop

label spriteling_battle_loop:


    $ dia = renpy.random.random()
    if dia < 0.3:
        if renpy.random.random()*100 > pc.dodge + extra_dodge:

            $ raw_damage = int(renpy.random.randint(enemy.min_damage, enemy.max_damage) / 3)
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_65

            if pc.hp < 0:
                $ pc.hp = 0
            "The spriteling wraps his spectral form around you, trying to bind you. Your health decreases by [enemy_damage] HP."
        else:
            "The spriteling swings his spectral form around you, but you manage to dodge the attack."
    else:

        "The ghostly creature raises its arm, and a gust of wind blows towards you."
        e "Huh?"
        "It doesn't seem to have any effect on you."

    call Battle_End_Check from _call_Battle_End_Check_24
    jump general_battle_loop

label spriteling_win:
    $ spriteling.win += 1
    if current_location == temple_of_tapjoo:

        "The whispy spriteling disperses into the air, leaving nothing but a faint scent of grass around."
        "You feel a little bit of energy returning to you, as if the spriteling itself has given you a little bit of its own energy."
        $ pc.restore(hp = 20)
        jump Temple_of_Tapjoo_Loop
    else:
        "The whispy spriteling disperses into the air, leaving nothing but a faint scent of moss around."
        "You feel a little bit of energy returning to you, as the speckles of the spriteling begin drifting around you."
        $ pc.restore(hp = 200)
        if mimic_num == 1:
            $ removeSprite(puro_forest, puro_spriteling_sprite1)
        if mimic_num == 2:
            $ removeSprite(puro_forest, puro_spriteling_sprite2)
        if mimic_num == 3:
            $ removeSprite(puro_forest, puro_spriteling_sprite3)
        $ enct = None
        jump Puro_Forest_Loop

label spriteling_lose:
    $ spriteling.lose += 1
    "Unable to continue, you faint on the ground, and the spriteling disappears into the air."
    if current_location == temple_of_tapjoo:
        "Unable to continue, you faint on the ground, and the spriteling disappears into the air."
        e "Ugh..."
        "The darkness envelops you, but not before you see a glimpse of Furkan and Rahim running towards you."
        "The next thing you know, you are already outside of the temple."
        if temple_of_tapjoo.isEmpty(1, 2) and temple_of_tapjoo.isSpirit():
            $ temple_of_tapjoo.occupy(1, 2, temple_of_tapjoo.inventory)
            $ temple_of_tapjoo.inventory.x = 1
            $ temple_of_tapjoo.inventory.y = 2
        $ temple_of_tapjoo.inventory = None
        jump main_lusterfield_mayors_longhouse

    "Exhausted all your energy, you struggle to get up, or to even open your eyes."
    yu "Allfather. Someone please... come save me."
    "Obviously, passing out on a wild forest isn't a great idea, but there are no other choice given here..."
    scene black with dissolve2
    "Soon, your world fades into darkness."

    "..."

    jump Encountering_Moine

label spritebinder_battle:


    $ enemy_num = 1
    $ enemy = spritebinder
    call beginningBattle from _call_beginningBattle_30
    $ pc.mp = 0
    $ enemy.max_hp = 400
    $ enemy.min_damage = 50
    $ enemy.max_damage = 90
    $ enemy.min_lust_damage = 8
    $ enemy.max_lust_damage = 15
    $ enemy.dodge = 30
    $ enemy.defense = 30
    $ enemy.lust_defense = 80
    $ enemy.exp_drop = 300
    $ enemy.beginbattle()
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    scene puro_forest:
        blur 8
    $ enemy_image = "spritebinder"
    "The hooded sprite flaunts its arms, seemingly preparing to cast a spell."

    jump general_battle_loop

label spritebinder_battle_loop:


    $ dia = renpy.random.random()
    if dia < 0.4:
        if renpy.random.random()*100 > pc.dodge + extra_dodge:

            $ raw_damage = int(renpy.random.randint(enemy.min_damage, enemy.max_damage))
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_66

            if pc.hp < 0:
                $ pc.hp = 0
            "The spritebinder strikes you with multiple arms, your health decreases by [enemy_damage] HP."
        else:
            "The spritebinder tries to strike you, but miraculously, you manage to dodge all of his arms."

    elif dia < 0.6 and bound not in status:
        "The spritebinder flings his arms to hold you in place. You try to struggle free, but it doesn't work."
        $ status.append(bound)
        $ grip_strength = bound.effect
    else:
        if renpy.random.random()*100 > pc.dodge + extra_dodge:

            $ raw_damage = int(renpy.random.randint(enemy.min_damage, enemy.max_damage) / 4)
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_67
            pause 1.0
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_68
            pause 1.0
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_69
            pause 1.0
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_70
            pause 1.0
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_71
            $ total_damage = enemy_damage * 5
            "The spritebinder forms a fist stance, and punches you with each of his arms, your health decreases by [total_damage] HP."
        else:
            "The spritebinder tries to strike you, but miraculously, you manage to dodge all of his arms."

    call Battle_End_Check from _call_Battle_End_Check_40
    jump general_battle_loop

label spritebinder_win:

    "Soon, the spritebinder falls to the ground, and the forest is quiet once again."
    "You take a deep breath, and you can feel the air is much more refreshing than before."
    "The arms of the spritebinder slowly fades into the air..."
    jump Encountering_Moine

label spritebinder_lose:

    $ spritebinder.lose += 1
    "Exhausted all your energy, you struggle to get up, and even open your eyes..."
    scene black with dissolve
    pause 2
    if timenow.hour <= 4:
        $ spritebinder.lose += 1
        call Scene_Spritebinder_Lose from _call_Scene_Spritebinder_Lose

    jump Encountering_Moine


label bearguard_battle:


    $ enemy_num = 1
    $ enemy = bearguard
    call beginningBattle from _call_beginningBattle_31
    $ enemy.max_hp = 540
    $ enemy.min_damage = 54
    $ enemy.max_damage = 67
    $ enemy.min_lust_damage = 16
    $ enemy.max_lust_damage = 26
    $ enemy.dodge = 20
    $ enemy.defense = 62
    $ enemy.lust_defense = 37
    $ enemy.exp_drop = 524
    $ bear_accuracy = 0
    $ bear_combo = 0
    $ enemy.beginbattle()
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    scene frostedtaiga:
        blur 8
    $ enemy_image = "bear guard"
    "The ferocious bear raises his harpoon, both legs steady and prepared for your attack."

    jump general_battle_loop

label bearguard_battle_loop:
    $ bear_combo = 0
    jump bearguard_battle_loop2

label bearguard_battle_loop2:
    $ bear_combo += 1

    $ dia = renpy.random.random()
    if dia < 0.45:
        if renpy.random.random()*(100 - bear_accuracy) > pc.dodge + extra_dodge and bear_combo <= 4:
            if bear_combo > 0:
                $ raw_damage = int(renpy.random.randint(enemy.min_damage, enemy.max_damage) * bear_combo * 1.25)
            else:
                $ raw_damage = int(renpy.random.randint(enemy.min_damage, enemy.max_damage))
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_72

            if pc.hp < 0:
                $ pc.hp = 0


            if renpy.random.random()*(100 - bear_accuracy) > pc.dodge + extra_dodge:
                if bear_combo > 0:
                    "The bear guard throws his harpoon towards you again, dealing extra damage! Your health decreases by [enemy_damage] HP."
                else:
                    "The bear guard throws his harpoon towards you, dealing [enemy_damage] HP."
                "You can feel the ice cold metal sending you shivers, your muscles are freezing from the impact."
                "It seems you are stunned for a round."
                $ rando = renpy.random.random()
                if rando < 0.33:
                    bearGuard "See, you're frozen now. We bears are not to be trifled with!"
                elif rando < 0.66:
                    bearGuard "You're not going anywhere, take this!"
                else:
                    bearGuard "We'll keep you in place forever if we want, you're not escaping from us!"
                call Battle_End_Check from _call_Battle_End_Check_22
                jump bearguard_battle_loop2
            else:
                if bear_combo > 0:
                    "The bear guard throws his harpoon towards you again, dealing extra damage! Your health decreases by [enemy_damage] HP."
                else:
                    "The bear guard throws his harpoon towards you, piercing into your skin. Your health decreases by [enemy_damage] HP."
                bearGuard "You're no match for us bears! Surrender now!"
        else:
            "The bear guard throws his harpoon towards you, you swiftly dodge the attack with ease."
            bearGuard "Hnnngh! How dare you dodge my attack!"
    elif dia < 0.6:
        if renpy.random.random() < 0.5:
            "The bear stretches and extends his abs, showing off his muscular body. You can see his fur is glistening in the sunlight."
            bearGuard "You must be feeling warm, huh? I'm sure something else of yours is heating up too."
        else:
            "The bear guard puts his hand on his loincloth, tracing the bulge around his crotch."
            bearGuard "This is what you're missing out on if you keep fighting, don't you want to see it up close?"
        if renpy.random.random()*(100 - bear_accuracy) > pc.lust_dodge + extra_lust_dodge:
            $ raw_flirt = int(renpy.random.randint(enemy.min_lust_damage, enemy.max_lust_damage))
            $ enemy_flirt = damageFormula(raw_flirt, pc.lust_defense)
            $ pc.lust += enemy_flirt
            if pc.lust > pc.max_lust:
                $ pc.lust = pc.max_lust
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "You take a heavy breath, it's too hard to resist the bear's charm and... perfect body."
                "Your lust increased by [enemy_flirt]."
            else:
                "You gulp, feeling a little bit of heat staring at his bare fur like that."
                "Your lust increased by [enemy_flirt]."
        else:

            "You don't seem to feel anything from his attack at your lust, but you're too focused in the battle to give him a better reason."

    elif dia < 0.73:
        "The bear roars, his voice echoing through the forest."
        "It seems to have given him a little bit of energy, as his harpoon seems to be sharper than before."
        "The highest damage from the bear is increased by 20 HP."
        $ enemy.max_damage += 20
        bearGuard "I will protect my tribe at all cost, I will unleash my undying wrath onto the whole of you!"
    elif dia < 0.86:
        "The bear guard raises his harpoon, and you can see the tip of the harpoon is glowing."
        "He is sharpening his weapon, your dodges are less effective against the bear now."
        bearGuard "You won't escape my harpoon that easily now."
        $ bear_accuracy += 10
    else:
        bearGuard "Hrrrrrgh!"
        "The bear chants, increasing both his defenses for the remaining of the battle."
        "You are afraid you can't drag the battle any longer, you have to defeat him more quickly."
        bearGuard "We are stronger than you think, you won't be defeating me with your weak attacks!"
        $ enemy.defense += 10
        $ enemy.lust_defense += 10

    call Battle_End_Check from _call_Battle_End_Check_25
    jump general_battle_loop

label bearguard_win:

    $ bearguard.win += 1

    "You manage to defeat the bear guard, as you see the bear fall into the thick snow."

    if enemy.lust > 50:
        menu:
            "Do you want to have fun with the bear guard?"
            "Yes{#bear_guard_win}":
                "..."
                call Scene_Bear_Win from _call_scene_bear_guard_win
                $ timenow.addTime(0, 6, 0)
                $ pc.lust = 0
            "No{#bear_guard_win}":
                "You retreat from the bear, signaling that you're not attacking him anymore."
                pass
    else:
        "He lets out a heavy sigh and shivers, the bear is probably not in the mood for anything else."

    if equippedTrinket("Lindbloom"):
        $ rnd = .2
    else:
        $ rnd = .1

    $ addItem("Bear Fur", inventory, 1)
    if renpy.random.random() <= rnd:
        "As you search around the bear guard, you found a piece of Bear Fur and a Bear Tribe Harpoon!"

        $ addItem("Bear Tribe Harpoon", inventory, 1)
    else:
        "As you search around the bear guard, you found a piece of Bear Fur!"

    call level_up_check (bearguard.exp_drop*0.8, bearguard.exp_drop*1.25, 52, 72) from _call_level_up_check_5

    "After a few moments, you leave the bear guard behind and continue your journey."

    jump main_frosted_taiga

label bearguard_lose:

    $ bearguard.lose += 1

    "The bear guard roars, his voice echoing through the forest as you fall to the ground."

    if bearguard.lose > 1:
        menu:
            "Do you want to replay the losing scene?"
            "Yes{#bearguardlosereplay}":
                call Scene_Bear_Lose from _call_Scene_Bear_Lose
            "No{#bearguardlosereplay}":
                pass
    else:
        call Scene_Bear_Lose from _call_Scene_Bear_Lose_1
    $ pc.add_active_status(stuffed)
    call lost_gold_check (0.075, 40, True) from _call_lost_gold_check_4

    jump main_frosted_taiga

label cultacolyte_battle:

    $ enemy_num = 1
    $ enemy = cultacolyte
    call beginningBattle from _call_beginningBattle_33
    $ enemy.max_hp = 800
    $ enemy.min_damage = 50
    $ enemy.max_damage = 65
    $ enemy.min_lust_damage = 24
    $ enemy.max_lust_damage = 38
    $ enemy.dodge = 29
    $ enemy.defense = 68
    $ enemy.lust_defense = 47
    $ enemy.exp_drop = 524

    $ enemy.beginbattle()
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    scene temple_of_tapjoo:
        blur 8
    $ enemy_image = "cult_acolyte"
    "The acolyte raises the pendant in his hand, his manhood proudly hanging in the damp air."

    jump general_battle_loop

label cultacolyte_battle_loop:


    $ dia = renpy.random.random()
    if dia < 0.3:
        if renpy.random.random()*100 > pc.dodge + extra_dodge:

            $ raw_damage = int(renpy.random.randint(enemy.min_damage, enemy.max_damage))
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_73


            "The cultist casts a ring of gloom towards your direction, dealing [enemy_damage] HP."

            $ rando = renpy.random.random()
            if rando < 0.33:
                acolyte "You will soon become one of us, it is your fate."
            elif rando < 0.66:
                acolyte "Let the darkness consume you, dragon."
            else:
                acolyte "The Shepherd will guide you to the right path, you will see."
        else:
            "The cultist casts a ring of gloom towards your direction, but you manage to dodge it just in time."
            acolyte "Run all you want, you won't escape his call."
    elif dia < 0.5:
        "The cult acolyte raises his pendant, and you can see the tip of the pendant is glowing."
        "He swings the pendant around, exuding a strange aura that makes you feel a little bit of heat."
        $ rando = renpy.random.random()
        if rando < 0.33:
            acolyte "Join us willingly, and you will be exalted."
        elif rando < 0.66:
            acolyte "Your destiny is intertwined with ours. Accept it."
        else:
            acolyte "We know who you are, dragon. Resistance only delays the inevitable."
        if renpy.random.random()*100 > pc.lust_dodge + extra_lust_dodge:
            $ raw_flirt = int(renpy.random.randint(enemy.min_lust_damage, enemy.max_lust_damage))
            $ enemy_flirt = damageFormula(raw_flirt, pc.lust_defense)
            $ pc.lust += enemy_flirt
            if pc.lust > pc.max_lust:
                $ pc.lust = pc.max_lust
            $ random_chance = renpy.random.random()

            "You feel a little bit of heat from the acolyte's charm, and his exposed manhood."
            "Your lust increased by [enemy_flirt]."
            $ isConfused = next((x for x in status if x.img == "Confused"), None)
            if isConfused != None:
                $ isConfused.rounds += 1
                if renpy.random.random() > 0.5:
                    "You are now much more confused, you have a feeling you might be hypnotised if this continues..."
                else:
                    "You are now much more confused, perhaps attacking him successfully can interrupt his psychic attack."
            else:
                $ ApplyStatus(status, confused, 1)
                "You are now confused, your attack has a chance to hit yourself instead."
        else:
            "You turn your head away from the acolyte's charm, dodging his attempt at your mind."


    elif dia < 0.67 and trapped not in status:
        "While you are calculating your next move, you fall into his trap, your dodges are now reduced by half for 3 rounds."
        acolyte "You have fallen for our oldest trick, dragon. I am afraid there is no way out now."
        $ trapped.rounds = trapped.max_rounds
        $ status.append(trapped)
        $ extra_dodge -= pc.dodge/2
        $ extra_lust_dodge -= pc.lust_dodge/2
    elif dia < 0.73 and bound not in status:
        $ status.append(bound)
        $ grip_strength = bound.effect
        "The cultist calls for the shepherd, and you can feel the ground beneath you shaking."
        "Suddenly, a dark tendril emerges from the ground, wrapping around your leg."
        "It seems you are now bound."
        acolyte "Let him guide you to your true destiny."
    else:

        "Chanting in an ancient tongue, he calls upon Tapjoo's wrath, unleashing a torrent of divine energy that sweeps across the chamber."

        $ raw_damage = int(renpy.random.randint(enemy.min_damage, enemy.max_damage))
        $ enemy_mp_damage = damageFormula(raw_damage / 3, pc.defense)
        $ enemy_damage = damageFormula(raw_damage, pc.defense)
        if renpy.random.random()*100 > pc.dodge + extra_dodge:

            $ pc.restore(mp = -enemy_mp_damage, hp = -enemy_damage)

            "The aftershock drains your mana. You lose [enemy_mp_damage] MP and [enemy_damage] HP."
            acolyte "We will cleanse you of your sins, dragon. The shepherd will guide you to the light."
        else:
            $ pc.restore(mp = -enemy_mp_damage)

            "You manage to dodge the attack, but the divine energy still manages to drain [enemy_mp_damage] MP."
            acolyte "Your willpower intrigues me, but it cannot withstand the shepherd's might."


    call Battle_End_Check from _call_Battle_End_Check_16
    jump general_battle_loop

label cultacolyte_win:

    $ cultacolyte.win += 1

    "The cult acolyte falls to the ground, his pendant shattering into pieces."
    acolyte "No... this is not going as planned."
    "He turns to you, trying to run away as a bright white light suddenly explodes from the pendant."
    "The light engulfs the acolyte, and soon yourself as your consciousness fades."
    scene black with dissolve
    "Your body falls backwards, hitting something hard as you lose your grip on reality."
    "And then, darkness is all you can see."
    "..."
    $ cultist_choice["Dreamed"] = True
    jump Chime_First_Dream

label cultacolyte_lose:

    $ cultacolyte.lose += 1

    "As you fall on the ground, you can hear the two werewolves howling at each other."
    $ cultist_choice["Hypnotised"] = True
    scene black with dissolve
    call Scene_Cult_Acolyte_Hypnosis from _call_Scene_Cult_Acolyte_Hypnosis
    $ pc.lust = 50
    $ pc.add_active_status(stuffed)
    jump Temple_Acolyte_Hypnosis_Aftermath



label general_double_battle_loop:

    show expression enemy_image:
        xalign 0.1
        yalign 0.4

    show expression enemy2_image:
        xalign 0.9
        yalign 0.4

    if check_party(pc) == "lost":
        call Battle_Finish from _call_Battle_Finish_47
        jump expression enemies_img.lower().replace(" ","") + "_lose"
    $ turn_action = ui.interact()
    call Battle_ASF from _call_Battle_ASF_6
    if oa[0] == "A":
        call battle_attack_script from _call_battle_attack_script_4
    if oa[0] == "F":
        call battle_flirt_script from _call_battle_flirt_script_4
    call battle_escape_surrender_script from _call_battle_escape_surrender_script_4
    call Ability_Item from _call_Ability_Item_8


    jump general_double_battle_midTurn

label general_double_battle_midTurn:
    $ enemy_loop = enemies_img + "_battle_loop"
    call Battle_Mid_Check from _call_Battle_Mid_Check_6

    if oa[0] == "W":
        call Battle_Finish from _call_Battle_Finish_48
        jump expression enemies_img.lower().replace(" ","") + "_win"
    if oa[0] == "T":
        call Battle_End_Check from _call_Battle_End_Check_30
        jump general_double_battle_loop

    if check_party(enemy) != "lost":
        show expression enemy_image:
            linear 0.1 zoom 1.04
            linear 0.05 zoom 1
        call expression enemy.img.lower().replace(" ","") + "_battle_loop" pass (acting_enemy=enemy) from _call_expression
    elif target == enemy:
        $ target = enemy2
    if check_party(enemy2) != "lost":
        show expression enemy2_image:
            linear 0.1 zoom 1.04
            linear 0.05 zoom 1
        call expression enemy2.img.lower().replace(" ","") + "_battle_loop" pass (acting_enemy=enemy2) from _call_expression_1
    elif target == enemy2:
        $ target = enemy

    jump general_double_battle_loop

label werewolf_werewolf_battle:


    $ enemy_num = 2
    $ enemy = werewolf
    $ enemy2 = werewolf2
    call beginningBattle from _call_beginningBattle_32
    $ enemy.max_hp = 400
    $ enemy.min_damage = 35
    $ enemy.max_damage = 50
    $ enemy.min_lust_damage = 10
    $ enemy.max_lust_damage = 22
    $ enemy.dodge = 2
    $ enemy.defense = 45
    $ enemy.lust_defense = 26
    $ enemy.exp_drop = 220
    $ enemy2.max_hp = 400
    $ enemy2.min_damage = 35
    $ enemy2.max_damage = 50
    $ enemy2.min_lust_damage = 10
    $ enemy2.max_lust_damage = 22
    $ enemy2.dodge = 2
    $ enemy2.defense = 45
    $ enemy2.lust_defense = 26
    $ enemy2.exp_drop = 220
    $ enemy.beginbattle()
    $ enemy2.beginbattle()

    $ target = enemy
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    scene dark_forest:
        blur 8
    $ enemy.img = "Werewolf"
    $ enemy2.img = "Werewolf"
    $ enemies_img = "werewolf_werewolf"
    $ enemy_image = "werewolf e1"
    $ enemy2_image = "werewolf e1"

    show expression enemy_image:
        xalign 0.1
        yalign 0.4

    show expression enemy2_image:
        xalign 0.9
        yalign 0.4
    "The werewolf duo raises their claws, their furs bristling in the wind as they reveal their sets of canines that can tear meat apart easily."

    jump general_double_battle_loop

label werewolf_werewolf_win:

    $ werewolf2.win += 1
    $ exp_drop = renpy.random.randint(500, 760)
    if equippedTrinket("Lindbloom"):
        $ rnd = 0.8
    else:
        $ rnd = 0.4
    "The werewolves are lying on the floor, still panting..."

    if renpy.random.random() <= rnd:
        "As you search around the werewolves, you found 2 Iron ores, 2 Pelts and [exp_drop] EXP!"
        $ addItem("Iron Ingot", inventory, 2)
        $ addItem("Pelt", inventory, 2)
    else:
        "As you search around the werewolves, you found 2 Pelt and [exp_drop] EXP!"
        $ addItem("Pelt", inventory, 2)
    if got_huntertrousers == 0 and renpy.random.random() < rnd:
        $ got_huntertrousers = 1
        "You also found a pair of trousers... from a Hunter."
        $ addItem("Hunter Trousers", inventory, 1)
    elif checkNoShopItem("Copper Pickaxe") and renpy.random.random() < rnd:
        "You also found an old copper pickaxe."
        $ addItem("Copper Pickaxe", inventory, 1)

    call level_up_check (werewolf2.exp_drop*1.6, werewolf2.exp_drop*2.5, 122, 200) from _call_level_up_check_6

    "You leave the werewolf alone in the forest, he will probably wake up a few hours later."

    jump main_dark_forest


label werewolf_werewolf_lose:

    $ werewolf2.lose += 1

    "As you fall on the ground, you can hear the two werewolves howling at each other."

    if werewolf2.lose > 1:
        menu:
            "Do you want to replay the losing scene?"
            "Yes{#werewolfdoublelosereplay}":
                call Scene_Werewolf_Double_Lose from _call_Scene_Werewolf_Double_Lose
            "No{#werewolfdoublelosereplay}":
                pass
    else:
        call Scene_Werewolf_Double_Lose from _call_Scene_Werewolf_Double_Lose_1
    $ pc.add_active_status(stuffed)
    call lost_gold_check (0.08, 35, True) from _call_lost_gold_check_5


    jump main_dark_forest

label seedsman_battle:

    $ enemy_num = 1
    $ enemy = seedsman
    call beginningBattle from _call_beginningBattle_34
    $ enemy.max_hp = 630
    $ enemy.min_damage = 55
    $ enemy.max_damage = 70
    $ enemy.min_lust_damage = 20
    $ enemy.max_lust_damage = 35
    $ enemy.dodge = 10
    $ enemy.defense = 60
    $ enemy.lust_defense = 40
    $ enemy.exp_drop = 600

    $ enemy.beginbattle()
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    scene grove_of_harvest:
        blur 8
    $ enemy_image = "seedsman"
    if pc.weapon == None:
        "You raise your fists. The Seedsman holds out his hands, and from his open palm a hail of razor-thin thorns spirals against you."
    else:
        "You draw your [pc.weapon.name!t]. The Seedsman raises an arm, and from his open palm a hail of razor-thin thorns spirals against you."

    jump general_battle_loop

label seedsman_battle_loop:


    $ dia = renpy.random.random()
    if dia < 0.3:
        if renpy.random.random()*100 > pc.dodge + extra_dodge:

            $ raw_damage = int(renpy.random.randint(enemy.min_damage, enemy.max_damage))
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_74

            $ rando = renpy.random.random()
            if rando < 0.33:
                "The seedsman throws a seed bomb towards your direction, dealing [enemy_damage] HP."
            elif rando < 0.66:
                "The seedsman sends a vine towards you, wrapping around your leg. Your health decreases by [enemy_damage] HP."
            else:
                "You try to dodge the seedsman's attack, but the thorns wraps around your leg tightly, dealing [enemy_damage] HP."
        else:
            "The seedsman throws a seed bomb towards your direction, you quickly step aside before the bomb even lands."
    elif dia < 0.5:
        "The gardener envelops his body around you, his vines wrapping around your body."
        if renpy.random.random()*100 > pc.lust_dodge + extra_lust_dodge:
            $ raw_flirt = int(renpy.random.randint(enemy.min_lust_damage, enemy.max_lust_damage))
            $ enemy_flirt = damageFormula(raw_flirt, pc.lust_defense)
            $ pc.lust += enemy_flirt
            if pc.lust > pc.max_lust:
                $ pc.lust = pc.max_lust
            $ rando = renpy.random.random()
            if rando < 0.33:
                "You can feel his vines wrapping around your body, and his exposed sower touching your skin."
            elif rando < 0.66:
                "You are suddenly brought closer to the seedsman's verdant manhood, it twitches as your snout lightly brushes against it."
                "The seedsman nods slowly as your tongue reaches the base of the trunk, the heat becomes more unbearable."
            else:
                "Your face is planted into his soft chest, the warmth of his body is intoxicating yet weirdly hypnotic."
            "Your lust increased by [enemy_flirt]."
        else:
            "But you manage to evade from the seedsman's embrace, successfully dodging his attempt to approach you."
    elif dia < 0.68 and enemy.hp < enemy.max_hp*0.65:
        "The seedsman wraps his vines around his body, his body begins to glow with a green aura."
        $ healing_amount = int((enemy.max_hp-enemy.hp)*(renpy.random.random()+0.5)*0.2)
        call Enemy_Self_Healing (enemy, healing_amount) from _call_Enemy_Self_Healing_14
    elif dia < 0.78 and bound not in status:
        $ status.append(bound)
        $ grip_strength = bound.effect
        "The seedsman casts his tendrils around you, engulfing your limbs in a tight grip."
        "You try to struggle free, but the vines are too strong."
        "You are now bound."
    else:

        "The seedsman suddenly clenches his body, growing 5 more thorns on his body."
        if hasStatus(enemy, thorned) != False:
            $ hasStatus(enemy, thorned).rounds += 5
            $ thorn_number = hasStatus(enemy, thorned).rounds
            $ raw_damage = int(renpy.random.randint(enemy.min_damage, enemy.max_damage) / 35 * thorn_number)
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            $ total_damage = enemy_damage * 3
            "All [thorn_number] of his thorns suddenly shoots towards you, dealing [total_damage] HP."
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_75
            pause 1.5
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_76
            pause 1.5
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_77
        else:


            $ ApplyStatus(target.item_drop01, thorned, 5)



    call Battle_End_Check from _call_Battle_End_Check_23
    jump general_battle_loop

label seedsman_win:

    "With a quiet rustle, the wispy seedsman falls to the ground, sinking into the grove he has nurtured."
    "The air is soon filled with the scent of blossoming flowers, and the grove seems to be more lively than before."
    "What remains of the seedsman was the verdant thorns, which pricles your paws as you pick it up."
    "You carefully store it in your trinket bag."
    $ addTrinket(spirespike_item, tinventory)
    $ seedsman.win += 1
    call level_up_check (seedsman.exp_drop*0.8, seedsman.exp_drop*1.25, 100, 150) from _call_level_up_check_7
    jump main_grove_of_harvest

label seedsman_lose:

    "You fall to the ground, exhausted from the battle."
    "The seedsman looks around as he towers over you, his vines still writhing around your body."
    "You shudder in the face of the green creature, he seems to hesitate for a moment, before releasing you."
    "He turns around and burrows into the rose bushes behind him, leaving you alone in the grove."
    $ seedsman.lose += 1
    "You sigh in relief, the seedsman seems to have spared you this time..."
    jump main_grove_of_harvest

label snowman_battle:

    $ enemy_num = 1
    $ enemy = snowman
    call beginningBattle from _call_beginningBattle_35
    $ enemy.max_hp = 800
    $ enemy.min_damage = 40
    $ enemy.max_damage = 80
    $ enemy.min_lust_damage = 10
    $ enemy.max_lust_damage = 20
    $ enemy.dodge = 5
    $ enemy.defense = 50
    $ enemy.lust_defense = 38
    $ enemy.exp_drop = 600

    $ enemy.beginbattle()
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    scene snowbound_summit:
        blur 8
    $ enemy_image = "snowman"
    "The snowman casually stands as you approach, he does not seem to be hostile, but he is definitely not too friendly either."

    jump general_battle_loop

label snowman_battle_loop:


    $ dia = renpy.random.random()
    if buffed_attack == 1:
        $ buffed_attack = 0

        $ enemy_damage = renpy.random.randint(snowman.min_damage, snowman.max_damage)
        call Damaging (snowman, pc, enemy_damage) from _call_Damaging_78

        "The snowman rolls the snowball towards you, it hits you hard, ignoring your defense and explodes into flurry of snow, dealing [enemy_damage] HP."
    elif dia < 0.2:
        if renpy.random.random()*100 > pc.dodge + extra_dodge:

            $ raw_damage = int(renpy.random.randint(snowman.min_damage, snowman.max_damage))
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (snowman, pc, enemy_damage) from _call_Damaging_79

            $ isFrozen = next((x for x in status if x.img == "Frozen"), None)
            if isFrozen not in status:
                $ ApplyStatus(status, frozen, renpy.random.randint(2, 5))
            else:
                $ isFrozen.rounds += renpy.random.randint(2, 5)

            $ rando = renpy.random.random()
            if rando < 0.33:
                "The snowman strikes the snow ground with his shovel, then launches a pile of snow towards you, dealing [enemy_damage] HP."

            elif rando < 0.66:
                "With a flick of his shovel, the snowman sends a wave of snowballs towards you, dealing [enemy_damage] HP."
            else:
                "A snowball flies towards you, hitting you square in the face. Your health decreases by [enemy_damage] HP."
            "You can feel the ice cold snow sending you shivers, your muscles are freezing from the impact."
        else:
            "The snowman strikes the snow ground with his shovel, hurling a pile of snow towards you, but it misses."

    elif dia < 0.3:
        "He kneels, packs his surface extra tight, and presents his dense chest like a shield."
        "The snow hardens around his body, and you can see the snowman is now much more resistant to your attacks."
        $ snowman.defense += 10
    elif dia < 0.5:
        if renpy.random.random()*100 > pc.lust_dodge + extra_lust_dodge:
            $ raw_flirt = int(renpy.random.randint(snowman.min_lust_damage, snowman.max_lust_damage))
            $ enemy_flirt = damageFormula(raw_flirt, pc.lust_defense)
            $ pc.lust += enemy_flirt
            if pc.lust > pc.max_lust:
                $ pc.lust = pc.max_lust
            $ rando = renpy.random.random()
            if rando < 0.33:
                "You can see the snowman's chest coated with melting snow, dribbling down his body like sweat."
                "He willfully leans forward, laying his hands on your shouders, his snow chest brushing against your fur as they mildly bounce up and down."
            elif rando < 0.66:
                "As the snowman thrusts his hips forwards, you can see the entire view of his glorious, drippy manhood, glistening as it catches the light."
                "He nods slowly as you inadvertently imagining your tongue wrapping around it, licking off the sweet snow off his chest like a slurry of ice."
            else:
                "Your body gravitates towards the snowman's belly, planting your head onto the soft, round pile of snow as you feel his gloves caressing your fur."
                "Something wet twitches underneath between your chest, his manhood traces up your body, filling your head with all the lewd thoughts you'd do with him."
            "Your lust increased by [enemy_flirt]."
        else:
            "Despite the illustrious gestures made by the snowman. Your eyes averts from the snowman's direction, as you try to focus on the battle."
    elif dia < 0.68 and snowman.hp < snowman.max_hp*0.65:
        "The snowman scoops up a pile of fresh snow, and hurls it onto his own body, followed by a few pats on his body and an extensive stretch."
        "He sighs a breath of relief, before turning up and staring at you again."
        $ healing_amount = int((snowman.max_hp-snowman.hp)*(renpy.random.random()+0.5)*0.2)
        call Enemy_Self_Healing (enemy, healing_amount) from _call_Enemy_Self_Healing_15
    elif dia < 0.78 and trapped not in status:
        $ trapped.rounds = trapped.max_rounds
        $ status.append(trapped)
        $ extra_dodge -= pc.dodge/2
        $ extra_lust_dodge -= pc.lust_dodge/2
        "The snowman raises both of his hands, and with a loud whirling, a wall suddenly bursts from the ground, surrounding you in a circle."
        "You are now trapped within the mound of snow."
    else:

        "The snowman begins to roll a snowball towards you, it gets bigger and bigger as it rolls, until it is the size of a boulder."
        "It looks like it's building up towards something powerful next turn."
        $ buffed_attack = 1

    if enemy.item_chance03 == 1:
        $ enemy.item_chance03 = 0
        return


    call Battle_End_Check from _call_Battle_End_Check_26
    jump general_battle_loop

label snowman_win:

    "You take a step back as the snowman topples over, quickly melting into the vast whiteness of the snow."
    "What was left in front of you was a small pile of snow which may be rolled into a ball..."

    if equippedTrinket("Lindbloom"):
        $ rnd = 0.6
    else:
        $ rnd = 0.3
    $ addItem("Carrot", inventory, 1)
    if renpy.random.random() <= rnd * 0.5:
        "As you search around the ball of snow, you find two pieces of carrot, coal and a chunk of archaic ice!"
        $ addItem("Archaic Ice", inventory, 1)
        $ addItem("Coal", inventory, 2)
        $ addItem("Carrot", inventory, 1)
    elif renpy.random.random() <= rnd:
        "As you search around the ball of snow, you find a piece of carrot and coal!"
        $ addItem("Coal", inventory, 1)
    else:
        "As you search around the ball of snow, you find a piece of carrot."

    $ snowman.win += 1
    call level_up_check (snowman.exp_drop*0.8, snowman.exp_drop*1.25, 100, 150) from _call_level_up_check_8

    if current_location == snowbound_summit:
        $ defeated_enemies[current_enemy] = True
        $ snowbound_summit.replaceSpriteInFront(sprite, MapStorer(0, 0, "snowball_sprite02", 120, 120, "Snowball", 3))

        $ enct = None
    jump Snowbound_Summit_Loop

label snowman_lose:

    "You clutch at your bruised body as your legs struggle to hold you up."
    e "W-wait-"
    "A big snowball shot towards you, knocking you off your feet."
    scene black with dissolve
    "The last thing you remember was the snowman standing over you, his shovel raised high above his head."
    "..."

    $ snowman.lose += 1
    jump main_frosted_taiga

label caretaker_battle:


    $ enemy_num = 1
    $ enemy = caretaker
    $ enemy.max_hp = 1500
    $ enemy.max_damage = 98
    $ enemy.max_damage = 132
    $ enemy.defense = 110
    $ enemy.lust_defense = 70
    $ enemy.min_lust_damage = 18
    $ enemy.max_lust_damage = 26
    $ enemy.dodge = 10
    $ enemy.exp_drop = 1300
    $ enemy_image = "caretaker"
    call beginningBattle from _call_beginningBattle_36
    $ caretaker.beginbattle()
    hide screen dungeon_map
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen dungeon_buttons
    scene snowbound_summit:
        blur 8
    $ enemy_image = "caretaker"
    if pc.weapon == None:
        "You are facing the caretaker, the guardian of the garden at the peak of Snowbound Summit."
    jump general_battle_loop

label caretaker_battle_loop:

    if enemy_num == 2:
        if check_party(snowman) == "lost":
            $ enemy_num = 1
            $ enemy.item_chance01 = 0.5
            hide snowman with dissolve
            show expression enemy_image:
                xalign 0.5
                yalign 0.5
            with move
        if check_party(caretaker) == "lost":
            call Battle_Finish from _call_Battle_Finish_8
            jump caretaker_win

    $ dia = renpy.random.random()
    if dia < 0.45:
        if renpy.random.random()*100 > pc.dodge+extra_dodge:
            $ raw_damage = int(renpy.random.randint(caretaker.min_damage, caretaker.max_damage))
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_80
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The Caretaker flings his huge hands towards you, his claws digging underneath your fur, dealing [enemy_damage] HP."
            else:
                "The Caretaker swings his claws towards you, the nails glinting in the light as it strikes you hard, dealing [enemy_damage] HP."
        else:
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The Caretaker flings his huge hands towards you, but you manage to dodge it just in time."
            else:
                "The Caretaker swings his claws towards you, but you manage to dodge it just in time."
    elif dia < 0.67 or (dia < 0.80 and renpy.random.random() > 0.5 and enemy.lust > enemy.max_lust*0.6):
        if enemy_num == 2:
            if ((enemy.max_hp - enemy.hp) / enemy.max_hp) > (enemy.lust / enemy.max_lust):
                "The Caretaker kneels, driving his claws into the snow like a trowel. Both of them are now revitalised."
                $ healing_amount = int((enemy.max_hp-enemy.hp)*(renpy.random.random()+0.5)*0.2)
                call Enemy_Self_Healing (enemy, healing_amount) from _call_Enemy_Self_Healing_16
                $ healing_amount = int((enemy2.max_hp-enemy2.hp)*(renpy.random.random()+0.5)*0.2)
                call Enemy_Self_Healing (enemy2, healing_amount) from _call_Enemy_Self_Healing_17
            else:
                "The Caretaker kneels, driving his claws into the snow like a trowel. Both of them are ridding of lustful thoughts."
                $ reduced_lust_amount = int((enemy.lust)*(renpy.random.random()+0.5)*0.4)
                call Enemy_Self_Purifying (enemy, reduced_lust_amount) from _call_Enemy_Self_Purifying
                $ reduced_lust_amount = int((enemy2.lust)*(renpy.random.random()+0.5)*0.4)
                call Enemy_Self_Purifying (enemy2, reduced_lust_amount) from _call_Enemy_Self_Purifying_1

        if enemy_num == 1:
            $ enemy_num = 2
            $ enemy2 = snowman
            $ enemy2.max_hp = 800
            $ enemy2.min_damage = 40
            $ enemy2.max_damage = 80
            $ enemy2.min_lust_damage = 10
            $ enemy2.max_lust_damage = 20
            $ enemy2.dodge = 5
            $ enemy2.defense = 50
            $ enemy2.lust_defense = 38
            $ enemy2.exp_drop = 600
            $ enemy2.beginbattle()
            $ enemy.item_chance01 = 0.1
            show expression enemy_image:
                xalign 0.1
                yalign 0.5
            with move
            show snowman:
                xalign 1.0
                yalign 0.5
            "With practiced strokes of his spade, the Caretaker pats loose snow into shape. A new Snowman lumbers to life, the eyes glinting."
            "The snowman quickly comes alive as it stands up!"

    elif dia < 0.83 and bound not in status:
        "The Caretaker lurches towards you, his claws outstretched, easily grabbing your arms and legs."
        "You are now bound."
        $ status.append(bound)
        $ grip_strengtrh = bound.effect
    else:

        if enemy_num == 2:
            "A single snowflake snap from the Caretaker's fingers, and he jerks the snowmen into sudden frenzy."
            "With the power of the Caretaker, the snowman is suddenly brought back to his verve, giving him a second round."
            if check_party(snowman) == "lost":
                $ enemy_num = 1
                $ enemy.item_chance01 = 0.5
                show expression enemy_image:
                    xalign 0.5
                    yalign 0.5
                with move
            else:
                show snowman:
                    linear 0.1 zoom 1.04
                    linear 0.05 zoom 1
                $ enemy.item_chance03 = 1
                call snowman_battle_loop from _call_snowman_battle_loop
        else:

            "The Caretaker slowly approaches you with his bulging member jerking out of the fur coats."
            if renpy.random.random()*100 > pc.lust_dodge + extra_lust_dodge:
                $ raw_flirt = int(renpy.random.randint(enemy.min_lust_damage, enemy.max_lust_damage))
                $ enemy_flirt = damageFormula(raw_flirt, pc.lust_defense)
                $ pc.lust += enemy_flirt
                if pc.lust > pc.max_lust:
                    $ pc.lust = pc.max_lust
                $ rando = renpy.random.random()
                if rando < 0.25:
                    "Your snout twitches as if the air is reek of his musk, and your body is getting hotter just by the smell."
                    "You'd bury your snout into his fur, and lick the sweat off his body, if only you weren't in the battle."
                elif rando < 0.5:
                    "The caretaker leans forward, his body brushing against yours as you feel the furred creature's warmth, the heat radiating from his body is intoxicating."
                    "You can feel the caretaker's manhood throbbing against your body, it's so big, and warm, you can't get rid of the thought of putting your lips on the tip of it."
                elif rando < 0.75:
                    "The caretaker slowly turns his back against you, flaunting his huge, round ass covered in fur coats."
                    "Your cock twitches as you stare at his ass, so enticing, as if asking for your cock to insert, how good would it feel, for his ass to tighten around your cock, the mere thought of it'd almost make you cum instantly."
                else:
                    "The caretaker's huge hands caress your body, his claws digging into your fur as he pulls you closer."
                    "Your entire body is enveloped just by his two strong hands, each exploring the curves of your body as you feel one of his rubbing against your shaft, another exploring your tight hole."
                    "Giving up now would be so enticing, he seems to know exactly what you want. After all, he is the caretaker."
                "Your lust increased by [enemy_flirt]."
            else:
                "You take a deep breath, and successfully dodge from his flirting attempt by keeping yourself calm."

    if enemy_num == 2:
        if check_party(snowman) == "lost":
            $ enemy_num = 1
            $ enemy.item_chance01 = 0.5
            show expression enemy_image:
                xalign 0.5
                yalign 0.5
            with move
        else:
            show snowman:
                linear 0.1 zoom 1.04
                linear 0.05 zoom 1
            jump snowman_battle_loop

    call Battle_End_Check from _call_Battle_End_Check_59
    jump general_battle_loop

label caretaker_win:
    $ caretaker.win += 1
    "The caretaker staggers, before both of his knees giving into the exhausion, slumping into the ground."
    snow_caretaker "I have failed... m'lord."
    "Slowly, the caretaker sinks into the pit of snow, his massive form half-lost in drifting snow."
    scene snowbound_summit with dissolve
    "Snow pours around the caretaker, filling the remainder of the pit as the Oolong plant struts upwards again."
    "You presume that means you can freely pluck some of the leaves now."
    if enemy_num == 2:
        "The snowman stares at you blankly, then lurches away as if nothing happened."
    call level_up_check (caretaker.exp_drop*0.8, caretaker.exp_drop*1.25, 200, 350) from _call_level_up_check_9

    scene snowbound_summit
    "You carefully trod through the heavy snow to reach where the caretaker lies."
    "With steady hands, you grasp the central stem of the Oolong — its leaves still warm against your hands."
    "You pluck some leaves here and there, and the plant seems to shudder in response. Perhaps it's a signal to stop."
    "You stand again, with enough Oolong leaves, you decide it's time to head back."
    $ addItem("Oolong Leaves", inventory)
    if quest44.status == 2:
        $ quest44.status = 3
        $ quest44.qComp(_("Head back to Haskell"))
    $ defeated_enemies["The Caretaker"] = "Defeated"
    $ snow_oolong_sprite.h = 120
    $ snow_oolong_sprite.img = "snow_oolong"
    jump Snowbound_Summit_Loop

label caretaker_lose:

    snow_caretaker "Feel the warrior's wrath, mortal."
    "Your exhaustion catches up to you, and you fall to the ground."
    scene black with dissolve
    "The caretaker looms over you, his claws glinting in the light as he raises them high above your head."
    "You can feel the cold air rushing past you as the caretaker's claws come crashing down."
    "And then... nothing comes after."
    menu:
        "You wake up in the taiga":
            "Except for the sound of the wind howling in your ears."
            "You open your eyes, and find yourself lying on the ground, the caretaker nowhere to be seen."
            "..."
            jump main_frosted_taiga
        "Back to Main Menu":
            $ MainMenu(confirm=False)()

label jotunn_battle:
    $ enemy_num = 1
    $ enemy = jotunn
    call beginningBattle from _call_beginningBattle_37
    $ enemy.max_hp = 850
    $ enemy.min_damage = 70
    $ enemy.max_damage = 90
    $ enemy.min_lust_damage = 25
    $ enemy.max_lust_damage = 40
    $ enemy.dodge = 5
    $ enemy.defense = 75
    $ enemy.lust_defense = 80
    $ enemy.exp_drop = 800
    $ enemy.beginbattle()
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    scene skullstrewn_pass:
        blur 8
    $ enemy_image = "jotunn"
    if pc.weapon == None:
        "The jotunn raises a massive fist glowing with blue runes as you clench your fists, bracing against the biting cold in front of you."
    else:
        "You draw your [pc.weapon.name!t]. The jotunn stomps the snow, sending icy shards flying as he charges."
    jump general_battle_loop

label jotunn_battle_loop:

    $ dia = renpy.random.random()
    if dia < 0.4:
        $ rando = renpy.random.random()
        if bound in status:
            $ drain_mp = 15 + int(renpy.random.random()*10)
            call Enemy_Self_Healing (enemy, drain_mp * 3) from _call_Enemy_Self_Healing_18
            "With his arms enveloped around you tightly, the glowing blue markings on the jotunn pulse rhythmically, siphoning your magic to rejuvenate his own strength."
            $ pc.restore(mp = -drain_mp)
            "You lost [drain_mp] MP as the jotunn releases you."
            $ status.remove(bound)
        elif renpy.random.random()*100 > pc.dodge + extra_dodge:
            $ raw_damage = int(renpy.random.randint(enemy.min_damage, enemy.max_damage))
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_81

            if rando < 0.33:
                "The jotunn slams his enormous fist into the ground, summoning a shockwave of ice that crashes into you, dealing [enemy_damage] HP."
            elif rando < 0.66:
                "With a deep guttural roar from behind the skull mask, the jotunn swings his arm, battering you for [enemy_damage] HP."
            else:
                "The ancient giant channels his frosted force, hurling a snow boulder engraved in blue-glowing frost at you, inflicting [enemy_damage] HP."

            $ isFrozen = next((x for x in status if x.img == "Frozen"), None)
            if isFrozen not in status:
                $ ApplyStatus(status, frozen, renpy.random.randint(2, 5))
                "You can feel the ice cold snow sending you shivers, your muscles are freezing from the impact."
            else:
                $ isFrozen.rounds += renpy.random.randint(2, 5)
        else:
            if rando < 0.33:
                "The jotunn slams his enormous fist into the ground, you quickly evade the shockwave unscathed."
            elif rando < 0.66:
                "The jotunn swings his arm, but you swiftly dodge the blow."
            else:
                "The ancient giant hurls a snow boulder at you, but you manage to step aside just in time."

    elif dia < 0.6:
        "The jotunn's glowing blue markings pulse hypnotically, drawing you closer as his loincloth shifts, hinting at the massive bulge barely hidden beneath."
        if renpy.random.random()*100 > pc.lust_dodge + extra_lust_dodge:
            $ raw_flirt = int(renpy.random.randint(enemy.min_lust_damage, enemy.max_lust_damage))
            $ enemy_flirt = damageFormula(raw_flirt, pc.lust_defense)
            $ pc.lust += enemy_flirt
            if pc.lust > pc.max_lust:
                $ pc.lust = pc.max_lust
            $ rando = renpy.random.random()
            if rando < 0.33:
                "His dark purple skin radiates an otherworldly heat, pressing against you as the alluring warmth overwhelms your senses."
            elif rando < 0.66:
                "The jotunn grinds his giant cock against your thigh, the throbbing heat through his loincloth drives you more itching."
                "His blue markings flare, drawing your gaze to the bulging outline, making your body sensitive with need."
            else:
                "Enveloped in his massive embrace, the jotunn's chest presses close, the unique primal scent intoxicating your mind as your snout is buried between the two giant mounds."
            "Your lust increases by [enemy_flirt]."
        else:
            "You shake off the hypnotic glow of his markings, stepping back before the jotunn ensnares you."

    elif dia < 0.7 and enemy.hp < enemy.max_hp * 0.65:
        "The jotunn kneels in the snow, his blue markings absorbing the frozen essence around him, mending his ancient form."
        $ healing_amount = int((enemy.max_hp-enemy.hp)*(renpy.random.random()+0.5)*0.25)
        call Enemy_Self_Healing (enemy, healing_amount) from _call_Enemy_Self_Healing_19
    elif dia < 0.8 and bound not in status:
        $ status.append(bound)
        $ grip_strength = bound.effect
        "The jotunn exhales a breath of arctic mist, freezing you in place as he approaches, his massive arms encasing your body in a relentless grip."
        "You are now bound."
    else:
        "The jotunn slams his fists together, sending a blast of icy wind swirling around you."
        $ isFrozen = next((x for x in status if x.img == "Frozen"), None)
        if isFrozen not in status:
            $ ApplyStatus(status, frozen, renpy.random.randint(2, 5))
        else:

            $ isFrozen.rounds += renpy.random.randint(2, 5)
            $ raw_damage = isFrozen.rounds
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            $ total_damage = enemy_damage * 3
            "The accumulated frost from the jotunn's icy assault intensifies, dealing [total_damage] HP."
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_82
            pause 1.5
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_83
            pause 1.5
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_84
            "A biting chill envelops you, sapping your strength as the jotunn stares at you beneath his mask."

    call Battle_End_Check from _call_Battle_End_Check_60
    jump general_battle_loop

label jotunn_win:

    $ jotunn.win += 1

    "The massive jotunn staggers backward, his breath ragged as he clutches his chest."
    "His glowing blue markings flicker weakly as he clutches the deer skull mask with one enormous hand."

    if enemy.lust >= 70:
        "Even in defeat, his huge member strains heavily against the loincloth, throbbing visibly."
        "He lets out a deep, frustrated growl."
    else:
        "His glowing eyes narrow in anger and pain."

    "With a thunderous roar, the jotunn slams his fist into the ground, sending a shockwave that knocks you off your feet."
    "When the frost clears, the giant has already vanished into the blizzard, leaving only massive footprints and swirling snow behind."

    if equippedTrinket("Lindbloom"):
        $ rnd = 1.2
    else:
        $ rnd = 0.75
    if renpy.random.random() <= rnd:
        "As you search around the snow, you find some cracked bone fragments, possibly dropped from the Jotunn's mask."
        if renpy.random.random()*2-1 <= rnd-1:
            $ addItem("Jotunn Bones", inventory, 2)
        else:
            $ addItem("Jotunn Bones", inventory, 1)
    call level_up_check (jotunn.exp_drop*0.8, jotunn.exp_drop*1.25, 140, 240) from _call_level_up_check_11

    jump main_skullstrewn_pass

label jotunn_lose:

    $ jotunn.lose += 1

    "You collapse into the deep snow, too exhausted to stand."
    e "Too tired..."
    "The towering jotunn looms over you, his dark purple body steaming in the cold air, glowing blue markings pulsing brightly."

    if enemy.lust >= 60:
        "His loincloth is barely containing his massive, fully erect member. Thick veins glow with the same icy blue light as his markings."
        "The jotunn lets out a low, hungry rumble as he reaches down and easily lifts your limp body with one hand."
        "He presses you against his cold, muscular chest, the heat of his throbbing cock already pushing against you through the loincloth."

        menu:
            "What do you do?"
            "Try to resist weakly":
                "You feebly push against his chest, but the giant doesn't even budge."
                call Scene_Jotunn_Lose from _call_Scene_Jotunn_Lose
            "Submit silently":
                "You hang limply in his grasp, heart racing as his overwhelming presence surrounds you."
                call Scene_Jotunn_Lose from _call_Scene_Jotunn_Lose_1
            "Skip Lose Scene" if jotunn.lose >= 1 and not (jotunn.lose > 3 and pc.cor < 85):
                pass
        "With the marks that the Jotunn has left on you, you can feel your purity drained away a little."
        $ pc.cor -= 5
        if pc.cor <= 0:
            $ pc.cor = 0
    else:
        "The jotunn stares down at you coldly, his glowing eyes showing little interest."
        "With a dismissive grunt, he slams his fist into the ground, sending a shockwave that knocks you off your feet."
        "When the frost clears, the giant has already vanished into the blizzard, leaving only massive footprints and swirling snow behind."
    call lost_gold_check (0.17, 100, True) from _call_lost_gold_check_6

    jump main_skullstrewn_pass

label slushy_battle:

    $ enemy_num = 1
    $ enemy = slushy
    call beginningBattle from _call_beginningBattle_38

    $ enemy.img = "Slushy"
    $ enemy.max_hp = 750
    $ enemy.min_damage = 60
    $ enemy.max_damage = 94
    $ enemy.min_lust_damage = 0
    $ enemy.max_lust_damage = 0
    $ enemy.dodge = 15
    $ enemy.defense = 80
    $ enemy.lust_defense = 100
    $ enemy.exp_drop = 70
    $ enemy.beginbattle()
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    hide screen dungeon_buttons
    scene chilly_ice_cave:
        blur 8

    $ enemy_image = "slushy"

    if pc.weapon == None:
        "You are facing a frigid slushy, its pale body sloshing over the frozen ground as you raise your fists."
    else:
        "You are facing a frigid slushy, its pale body sloshing over the frozen ground as you ready your [pc.weapon.name!t]."

    jump general_battle_loop

label slushy_battle_loop:

    $ ttg = pc
    $ dia = renpy.random.random()
    call slushy_turn from _call_slushy_turn
    call Battle_End_Check from _call_Battle_End_Check_61
    jump general_battle_loop

label slushy_daggi_battle:

    $ enemy_num = 1
    $ enemy = slushy
    call beginningBattle from _call_beginningBattle_39

    $ enemy.img = "Slushy"
    $ enemy.max_hp = 860
    $ enemy.min_damage = 56
    $ enemy.max_damage = 90
    $ enemy.min_lust_damage = 0
    $ enemy.max_lust_damage = 0
    $ enemy.dodge = 15
    $ enemy.defense = 82
    $ enemy.lust_defense = 100
    $ enemy.exp_drop = 90
    $ enemy.beginbattle()
    $ ally = daggi
    $ ally_num = 2
    $ ally.beginbattle()
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    hide screen dungeon_buttons
    scene chilly_ice_cave:
        blur 8

    $ enemy_image = "slushy"

    if pc.weapon == None:
        "The slushy surges across the ice as Daggi plants his feet beside you, harpoon leveled and ready. You clench your fists and prepare to bring it down together."
    else:
        "The slushy surges across the ice as Daggi plants his feet beside you, harpoon leveled and ready. You raise your [pc.weapon.name!t] and prepare to bring it down together."
    d "Keep it in front of us. I'll crack the shell when it hardens."

    jump slushy_daggi_battle_loop

label slushy_daggi_battle_loop:

    show expression enemy_image:
        xalign 0.5
        yalign 0.4

    if check_party(pc) == "lost" and check_party(ally) == "lost":
        call Battle_Finish from _call_Battle_Finish_9
        jump slushy_lose

    if battleTurn == "Player":
        if check_party(pc) != "lost":
            "It's your turn now."
            $ turn_action = ui.interact()
        else:
            $ turn_action = "No"
    else:
        $ ItemTab = False
        $ AbilityTab = False
        if check_party(ally) != "lost":
            "It's [ally.name]'s turn now."
            $ turn_action = ui.interact()
        else:
            $ turn_action = "No"

    call Battle_ASF from _call_Battle_ASF_2
    if oa[0] == "A" or oa[0] == "S":
        if battleTurn == "Player":
            call battle_attack_script from _call_battle_attack_script_5
        elif oa[1] == "M":
            if daggi_accompany:
                "Daggi steps in with a quick thrust, but [target.name] turns the blow aside with a grind of stone."
            else:
                "Herd darts in with his improvised stone rod, but [target.name] catches the angle and the strike skips off the carved shell."
        else:
            call Enemy_Damaging (target, oa[4]) from _call_Enemy_Damaging_23
            if daggi_accompany:
                "Daggi snaps his harpoon into [target.name]'s midsection, dealing [oa[4]] HP and shaving a strip of stone from its frame."
            else:
                "Herd lashes out with the broken rod and cracks it across [target.name]'s arm, dealing [oa[4]] HP."
    if oa[0] == "F":
        call battle_flirt_script from _call_battle_flirt_script_5
    if oa[0] == "A_S":
        if renpy.random.random() < 0.5:
            d "Now!"
            "Daggi drives his harpoon through the slushy's center, dealing [ally_damage] HP and forcing the icy mass to buckle inward."
        else:
            d "Right there."
            "Daggi lunges low and spears through a weak point in the slushy's crust, dealing [ally_damage] HP and stunning it for [stunned.max_rounds] round."
        if oa[1] == "B":
            "The blow breaks the creature's grip and gives you room to move again."
    if oa[0] == "A_D":
        d "Stay behind the shaft."
        "Daggi braces his harpoon across both of you and absorbs the slushy's next rush on cold steel, raising your defence for this round."
    if oa[0] == "A_T":
        $ oa[4] = damageFormula(renpy.random.randint(int(ally.damage*0.8), int(ally.damage*1.45)), target.defense)
        call Damaging (ally, target, oa[4]) from _call_Damaging_85
        if trapped in status and renpy.random.random() < 0.45:
            $ status.remove(trapped)
            $ extra_dodge += pc.dodge/2
            $ extra_lust_dodge += pc.lust_dodge/2
            d "Move."
            "Daggi hacks through the ice around your boots, freeing you as he tears a trench through the slushy's body for [oa[4]] HP."
        else:
            d "Split apart already."
            "Daggi rips the harpoon sideways through the slushy, dealing [oa[4]] HP and widening the wound through its frozen mass."
        "The slushy is now wounded."
    call battle_escape_surrender_script from _call_battle_escape_surrender_script_5
    if oa[0] == "E":
        "There is no safe path out while the slushy keeps the ice lane sealed."
    if oa[0] == "U":
        "You lower yourself in defeat, but Daggi still tries to keep the creature off you with his harpoon."
        d "Back! Move if you still can!"
        call Battle_Finish from _call_Battle_Finish_46
        jump slushy_lose
    call Ability_Item from _call_Ability_Item_2

    call Battle_Mid_Check from _call_Battle_Mid_Check_2
    if oa[0] == "W":
        call Battle_Finish from _call_Battle_Finish_49
        jump slushy_win
    if oa[0] == "T":
        call Battle_End_Check from _call_Battle_End_Check_62
        jump slushy_daggi_battle_loop

    show expression enemy_image:
        linear 0.1 zoom 1.04
        linear 0.05 zoom 1

    $ possible_targets = []
    if check_party(pc) != "lost":
        $ possible_targets.append(pc)
    if check_party(ally) != "lost":
        $ possible_targets.append(ally)
    $ ttg = renpy.random.choice(possible_targets)
    $ dia = renpy.random.random()
    call slushy_turn from _call_slushy_turn_1
    call Battle_End_Check from _call_Battle_End_Check_63
    jump slushy_daggi_battle_loop

label slushy_turn:

    if dia < 0.30:
        if renpy.random.random()*100 > ttg.dodge + extra_dodge:
            $ raw_damage = int(renpy.random.randint(slushy.min_damage, slushy.max_damage))
            $ enemy_damage = damageFormula(raw_damage, ttg.defense)
            call Damaging (enemy, ttg, enemy_damage) from _call_Damaging_86
            if ttg == pc:
                "The slushy bunches into a compact mass and rockets into your ribs. Your health decreases by [enemy_damage] HP."
            else:
                "The slushy skids across the ice and hammers into Daggi's side, coating his furs in freezing sludge. [ally.name]'s health decreases by [enemy_damage] HP."
        else:
            if ttg == pc:
                "The slushy shoots across the ice toward you, but you twist clear before it can bowl you over."
            else:
                "The slushy rushes Daggi, but he pivots on the ice and lets it rush past his guard."
    elif dia < 0.58:
        if renpy.random.random()*100 > ttg.dodge + extra_dodge:
            $ raw_damage = int(renpy.random.randint(slushy.min_damage - 4, slushy.max_damage - 6))
            $ enemy_damage = damageFormula(raw_damage, ttg.defense)
            call Damaging (enemy, ttg, enemy_damage) from _call_Damaging_87
            if ttg == pc:
                $ isFrozen = next((x for x in status if x.img == "Frozen"), None)
                if isFrozen not in status:
                    $ ApplyStatus(status, frozen, renpy.random.randint(2, 4))
                else:
                    $ isFrozen.rounds += renpy.random.randint(2, 4)
                "A spray of sleet bursts into your chest and face. Your health decreases by [enemy_damage] HP."
                "The cold bites deep, and frost starts clinging to your limbs."
            else:
                "The slushy lashes Daggi with a burst of jagged ice, forcing him back a step. [ally.name]'s health decreases by [enemy_damage] HP."
        else:
            if ttg == pc:
                "The slushy bursts outward in a fan of sleet, but you shield yourself from the freezing spray."
            else:
                "Daggi catches the sleet on the shaft of his harpoon and shakes the ice free before it can slow him down."
    elif dia < 0.78 and ttg == pc and trapped not in status:
        $ trapped.rounds = trapped.max_rounds
        $ status.append(trapped)
        $ extra_dodge -= pc.dodge/2
        $ extra_lust_dodge -= pc.lust_dodge/2
        "The slushy floods around your boots and flash-freezes into a heavy collar of ice."
        d "Break that before it pins you."
        "You are trapped in the slush and your footing becomes much harder to recover."
    elif dia < 0.88 and slushy.hp < slushy.max_hp * 0.55:
        $ healing_amount = int((slushy.max_hp - slushy.hp) * (renpy.random.random() + 0.4) * 0.22)
        call Enemy_Self_Healing (enemy, healing_amount) from _call_Enemy_Self_Healing_20
        "The slushy drags scattered frost and cave ice back into itself, swelling into a thicker, colder body."
        "Its icy shell knits shut as it restores [healing_amount] HP."
    else:
        if slushy.defense < 170:
            $ slushy.defense += 6
        "The slushy spreads thin across the ice, then compresses into a denser frozen slab that is harder to pierce."
        if ttg != pc and renpy.random.random() < 0.5:
            d "It's hardening. Hit the cracks."
    return

label slushy_win:
    hide expression enemy_image
    $ slushy.win += 1
    if daggi_accompany:
        if pc.weapon == None:
            "You drive your fist into the slushy's chilled core while Daggi tears its outer shell apart with a final wrench of his harpoon."
        else:
            "You tear your [pc.weapon.name!t] through the slushy's chilled core as Daggi hooks the creature open with his harpoon, ripping the frozen mass apart."
        d "There. Don't let it pool back together."
    else:
        if pc.weapon == None:
            "You drive your fist into the slushy's chilled core until the whole mass shudders apart."
        else:
            "You tear your [pc.weapon.name!t] free from the slushy's chilled core, and the whole thing collapses in on itself."

    "The pale sludge splashes across the cave floor, freezes into brittle sheets, and then cracks apart into slush and icy fragments."

    $ exp_drop = renpy.random.randint(int(slushy.exp_drop*0.8), int(slushy.exp_drop*1.25))
    if lindbloom_item in pc.trinket:
        $ rnd = .7
    else:
        $ rnd = .35

    $ addItem("Slime Ball", inventory, 1)
    if renpy.random.random() <= rnd:
        "As you search through the frozen sludge, you find a [slimeball_item.name], a [slimecrystal_item.name] and [exp_drop] EXP!"
        $ addItem("Slime Crystal", inventory, 1)
    else:
        "As you search through the frozen sludge, you find a [slimeball_item.name] and [exp_drop] EXP!"

    call level_up_check (slushy.exp_drop*0.8, slushy.exp_drop*1.25, 12, 22) from _call_level_up_check_13

    if current_location == chilly_ice_cave:
        $ defeated_enemies[current_enemy] = True
        $ encountered_enemies = chilly_ice_cave.searchForUser(interaction=current_enemy)
        if encountered_enemies:
            $ removeSprite(chilly_ice_cave, encountered_enemies[0])
        $ enct = None
        if e_d == "front":
            $ chilly_ice_cave.continuePlayerSlide(0, 1)
        elif e_d == "back":
            $ chilly_ice_cave.continuePlayerSlide(0, -1)
        elif e_d == "left":
            $ chilly_ice_cave.continuePlayerSlide(-1, 0)
        else:
            $ chilly_ice_cave.continuePlayerSlide(1, 0)
    jump Chilly_Ice_Cave_Loop

label slushy_lose:
    hide expression enemy_image
    $ slushy.lose += 1
    scene chilly_ice_cave
    if daggi_accompany:
        "The slushy floods across the ice and smashes into you with crushing frozen weight before Daggi can peel it off."
        "You hit the cave floor hard, the cold seeping into your bones as the slushy engulfs you in a suffocating embrace of ice and sludge."
        d "[e]? Get up!"
        "You try to respond, but none of your muscles seem to obey you as your body is entirely encased in the slushy."
        "It doesn't take long before your vision fade..."
        menu:
            "Back to Main Menu":
                $ MainMenu(confirm=False)()
    else:
        "Your boots lock in place as the slushy surges over your legs and hardens around them."
        "Before you can wrench yourself free, the creature slams into your chest and sends you crashing onto the frozen stone."
        "The last thing you feel is the wet, killing cold creeping through your clothes while the cave spins above you."
        "When you finally wake, you are sprawled near the cave mouth, shivering and soaked with half-frozen sludge."
    $ daggi_accompany = False
    jump main_frosted_taiga

label crypt_bearstatue_battle:

    $ enemy_num = 2
    $ enemy = Monster(_("Glaive Statue"), "bear glaive statue", 960, 100, 56, 84, 0, 0, 10, 78, 100, 120)
    $ enemy2 = Monster(_("Bulwark Statue"), "bear bulwark statue", 1180, 100, 44, 72, 0, 0, 6, 96, 100, 120)
    $ enemy.beginbattle()
    $ enemy2.beginbattle()
    $ target = enemy
    $ ally = Ally(_("Herd"), "herd", 780, 70, 100, 90, 0, 18, 42, 45, "Strike", "Defend", "Thrash")
    $ ally_num = 2
    $ ally.beginbattle()
    call beginningBattle from _call_beginningBattle_40

    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    hide screen dungeon_buttons
    scene conquerors_crypt:
        blur 8

    if pc.weapon == None:
        "The two bronze bear warrior statues wrench free together. You raise your fists as Herd snatches up a broken stone rod and plants himself at your side."
    else:
        "The two bronze bear warrior statues wrench free together. You ready your [pc.weapon.name!t] as Herd snatches up a broken stone rod and plants himself at your side."
    "Herd flashes a sharp hand signal toward the left statue, then the right, already tracking how they move."

    jump crypt_bearstatue_battle_loop

label crypt_bearstatue_daggi_battle:

    $ enemy_num = 2
    $ enemy = Monster(_("Glaive Statue"), "bear glaive statue", 1040, 100, 54, 82, 0, 0, 10, 82, 100, 135)
    $ enemy2 = Monster(_("Bulwark Statue"), "bear bulwark statue", 1260, 100, 42, 70, 0, 0, 6, 102, 100, 135)
    $ enemy.beginbattle()
    $ enemy2.beginbattle()
    $ target = enemy
    $ ally = daggi
    $ ally.beginbattle()
    $ ally_num = 2
    call beginningBattle from _call_beginningBattle_41

    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    hide screen dungeon_buttons
    scene conquerors_crypt:
        blur 8
    "The two bronze bear warrior statues wrench free from their pedestals as Daggi braces beside you with his harpoon leveled."
    if pc.weapon == None:

        "You clench your fists and meet the charge with him."
    else:
        "You raise your [pc.weapon.name!t] and meet the charge with him."

    jump crypt_bearstatue_battle_loop

label crypt_bearstatue_battle_loop:

    if check_party(enemy) != "lost":
        show bear glaive statue as crypt_bear_left:
            xalign 0.14
            yalign 0.4
    else:
        hide crypt_bear_left

    if check_party(enemy2) != "lost":
        show bear bulwark statue as crypt_bear_right:
            xalign 0.86
            yalign 0.4
    else:
        hide crypt_bear_right

    if check_party(enemy) == "lost" and target == enemy:
        $ target = enemy2
    elif check_party(enemy2) == "lost" and target == enemy2:
        $ target = enemy

    if check_party(pc) == "lost" and check_party(ally) == "lost":
        call Battle_Finish from _call_Battle_Finish_50
        jump crypt_bearstatue_lose

    if battleTurn == "Player":
        if check_party(pc) != "lost":
            "It's your turn now."
            $ turn_action = ui.interact()
        else:
            $ turn_action = "No"
    else:
        $ ItemTab = False
        $ AbilityTab = False
        if check_party(ally) != "lost":
            "It's [ally.name]'s turn now."
            $ turn_action = ui.interact()
        else:
            $ turn_action = "No"

    $ crypt_ally_action = None
    if battleTurn != "Player" and turn_action in ("Strike", "Defend", "Thrash"):
        $ crypt_ally_action = turn_action
        $ turn_action = "No"

    call Battle_ASF from _call_Battle_ASF_7
    if oa[0] == "A" or oa[0] == "S":
        if battleTurn != "Player":
            call battle_attack_script from _call_battle_attack_script_6
        elif oa[1] == "M":
            if daggi_accompany:
                "Daggi steps in with a quick thrust, but [target.name] turns the blow aside with a grind of stone."
            else:
                "Herd darts in with the broken rod, but [target.name] catches the angle and the strike skids off its carved shell."
        else:
            call Enemy_Damaging (target, oa[4]) from _call_Enemy_Damaging_24
            if daggi_accompany:
                "Daggi snaps his harpoon into [target.name]'s midsection, dealing [oa[4]] HP and shaving a strip of stone from its frame."
            else:
                "Herd lashes out with the broken rod and cracks it across [target.name]'s arm, dealing [oa[4]] HP."
    if oa[0] == "F":
        if oa[1] == "S":
            $ target.lust -= oa[4]
            if target.lust < 0:
                $ target.lust = 0
        $ oa[1] = "M"
        "You try to get a rise out of the carved guardians, but the statues answer with nothing but grinding stone."

    if crypt_ally_action == "Strike":
        if daggi_accompany:
            $ ally_damage = damageFormula(renpy.random.randint(int(ally.damage*0.72), int(ally.damage*1.35)), target.defense)
            call Damaging (ally, target, ally_damage) from _call_Damaging_88
            if renpy.random.random() < 0.5:
                d "There."
                "Daggi drives his harpoon into a seam in [target.name]'s chest, dealing [ally_damage] HP and knocking stone chips across the floor."
            else:
                d "Low, maybe?"
                "Daggi hooks low and tears [target.name] off balance, dealing [ally_damage] HP."
            if renpy.random.random() < 0.45 and stunned not in target.item_drop01:
                $ stunned.rounds = stunned.max_rounds
                $ target.item_drop01.append(stunned)
                "The blow staggers [target.name], freezing it in place for a moment."
        else:
            $ ally_damage = damageFormula(renpy.random.randint(int(ally.damage*0.72), int(ally.damage*1.3)), target.defense)
            call Damaging (ally, target, ally_damage) from _call_Damaging_89
            if target == enemy:
                "Herd darts in under the sweeping shaft and slams his stone rod into the Glaive Statue's arm, dealing [ally_damage] HP."
            else:
                "Herd slips around the shield rim and cracks the Bulwark across an exposed joint, dealing [ally_damage] HP."
            if renpy.random.random() < 0.35 and stunned not in target.item_drop01:
                $ stunned.rounds = stunned.max_rounds
                $ target.item_drop01.append(stunned)
                "The impact jars [target.name] and leaves it frozen in place for a moment."
        $ ally.mp -= 15

    if crypt_ally_action == "Defend":
        if daggi_accompany:
            d "Stay close."
            "Daggi catches the next incoming strike on the shaft of his harpoon and turns it aside, raising your defence for this round."
        else:
            "Herd yanks a fallen slab upright and braces it between you and the statues, signaling for you to keep close to the cover."
            if trapped in status:
                $ status.remove(trapped)
                $ extra_dodge += pc.dodge/2
                $ extra_lust_dodge += pc.lust_dodge/2
                "The shifted stone knocks the pressure off your footing and gives you room to move again."
        $ pc.defense += fortifying.effect
        $ ally.defense += fortifying.effect
        $ fortify = True
        $ ally.mp -= 15

    if crypt_ally_action == "Thrash":
        if daggi_accompany:
            $ oa[4] = damageFormula(renpy.random.randint(int(ally.damage*0.8), int(ally.damage*1.45)), target.defense)
            call Damaging (ally, target, oa[4]) from _call_Damaging_90
            d "Let's open it up."
            "Daggi slams the butt of his harpoon into an old fracture and widens it, dealing [oa[4]] HP to [target.name]."
            if target.defense > 36:
                $ target.defense -= 8
                "Stone dust spills from the wound as [target.name]'s shell weakens."
        else:
            $ ally_damage = damageFormula(renpy.random.randint(int(ally.damage*0.8), int(ally.damage*1.45)), target.defense)
            call Damaging (ally, target, ally_damage) from _call_Damaging_91
            if target == enemy:
                "Herd hammers the Glaive Statue again and again at the same cracked seam, dealing [ally_damage] HP."
            else:
                "Herd batters the Bulwark's shield arm in a flurry of brutal strikes, dealing [ally_damage] HP."
            if target.defense > 34:
                $ target.defense -= 8
                "Chips of stone rain to the floor as [target.name]'s shell weakens."
        $ ally.mp -= 15

    if oa[0] == "E":
        "The two statues close off the only clear way through the chamber. There is nowhere to run."
    if oa[0] == "U":
        if daggi_accompany:
            "You falter, but Daggi's warning comes a breath too late as both statues bear down."
            d "Stay up!"
        else:
            "You falter, and Herd's frantic warning gesture is swallowed by the roar of grinding stone."
        call Battle_Finish from _call_Battle_Finish_51
        jump crypt_bearstatue_lose
    call Ability_Item from _call_Ability_Item_9

    call Battle_Mid_Check from _call_Battle_Mid_Check_7
    if oa[0] == "W":
        call Battle_Finish from _call_Battle_Finish_52
        jump crypt_bearstatue_win
    if oa[0] == "T":
        call Battle_End_Check from _call_Battle_End_Check_64
        jump crypt_bearstatue_battle_loop

    if check_party(enemy) != "lost":
        show bear glaive statue as crypt_bear_left:
            linear 0.1 zoom 1.04
            linear 0.05 zoom 1
        $ acting_enemy = enemy
        call crypt_bearstatue_turn from _call_crypt_bearstatue_turn
        call Battle_End_Check from _call_Battle_End_Check_65
        if check_party(pc) == "lost" and check_party(ally) == "lost":
            call Battle_Finish from _call_Battle_Finish_53
            jump crypt_bearstatue_lose

    if check_party(enemy2) != "lost":
        show bear bulwark statue as crypt_bear_right:
            linear 0.1 zoom 1.04
            linear 0.05 zoom 1
        $ acting_enemy = enemy2
        call crypt_bearstatue_turn from _call_crypt_bearstatue_turn_1
        call Battle_End_Check from _call_Battle_End_Check_66
        if check_party(pc) == "lost" and check_party(ally) == "lost":
            call Battle_Finish from _call_Battle_Finish_54
            jump crypt_bearstatue_lose

    jump crypt_bearstatue_battle_loop

label crypt_bearstatue_turn:

    $ possible_targets = []
    if check_party(pc) != "lost":
        $ possible_targets.append(pc)
    if check_party(ally) != "lost":
        $ possible_targets.append(ally)
    if len(possible_targets) == 0:
        return
    $ ttg = renpy.random.choice(possible_targets)
    $ dia = renpy.random.random()

    if acting_enemy == enemy:
        if dia < 0.38:
            if renpy.random.random()*100 > ttg.dodge + extra_dodge:
                $ raw_damage = int(renpy.random.randint(enemy.min_damage, enemy.max_damage))
                $ enemy_damage = damageFormula(raw_damage, ttg.defense)
                call Damaging (enemy, ttg, enemy_damage) from _call_Damaging_92
                if ttg == pc:
                    "The Glaive Statue lunges in a brutal forward rush, its bronze spear point crashing into your guard. Your health decreases by [enemy_damage] HP."
                elif daggi_accompany:
                    "The Glaive Statue drives its spear into Daggi's side with a grinding thrust. [ally.name]'s health decreases by [enemy_damage] HP."
                else:
                    "The Glaive Statue spears toward Herd, clipping him hard across the ribs. [ally.name]'s health decreases by [enemy_damage] HP."
            else:
                if ttg == pc:
                    "The Glaive Statue launches at you, but you cut aside before the spear point can pin you."
                elif daggi_accompany:
                    "Daggi twists around the Glaive Statue's lunging spear and lets it carve empty air."
                else:
                    "Herd ducks under the spear thrust at the last possible instant."
        elif dia < 0.68 and ttg == pc and trapped not in status:
            $ trapped.rounds = trapped.max_rounds
            $ status.append(trapped)
            $ extra_dodge -= pc.dodge/2
            $ extra_lust_dodge -= pc.lust_dodge/2
            "The Glaive Statue drives its weapon down across your footing and locks you in place under splintered bronze and frost."
            if daggi_accompany:
                d "Break loose, quick!"
            else:
                "Herd chops sharply at the ground with one hand, warning you to move."
        else:
            $ total_enemy_damage = 0
            $ raw_damage = int(renpy.random.randint(enemy.min_damage - 8, enemy.max_damage - 10) / 2)
            if check_party(pc) != "lost":
                $ enemy_damage = damageFormula(raw_damage, pc.defense)
                call Damaging (enemy, pc, enemy_damage) from _call_Damaging_93
                $ total_enemy_damage += enemy_damage
            if check_party(ally) != "lost":
                $ ally_damage_taken = damageFormula(raw_damage, ally.defense)
                call Damaging (enemy, ally, ally_damage_taken) from _call_Damaging_94
                $ total_enemy_damage += ally_damage_taken
            "The Glaive Statue whips its spear in a wide crescent, showering both of you with bronze splinters and driving you back for [total_enemy_damage] total HP."
    else:
        if dia < 0.34:
            if renpy.random.random()*100 > ttg.dodge + extra_dodge:
                $ raw_damage = int(renpy.random.randint(enemy2.min_damage, enemy2.max_damage))
                $ enemy_damage = damageFormula(raw_damage, ttg.defense)
                call Damaging (enemy2, ttg, enemy_damage) from _call_Damaging_95
                if ttg == pc:
                    "The Bulwark slams forward with its bronze slab shield locked in place, crushing into your chest. Your health decreases by [enemy_damage] HP."
                elif daggi_accompany:
                    "The Bulwark bulldozes Daggi with a plated bronze shoulder and shield rim. [ally.name]'s health decreases by [enemy_damage] HP."
                else:
                    "The Bulwark drives its bronze weight into Herd and sends him skidding across the frost. [ally.name]'s health decreases by [enemy_damage] HP."
            else:
                if ttg == pc:
                    "You slide clear of the Bulwark's crushing charge before its full weight can catch you."
                elif daggi_accompany:
                    "Daggi braces, then slips off the line of the shield bash at the last moment."
                else:
                    "Herd pivots around the edge of the slab shield and stays just out of reach."
        elif dia < 0.67:
            if acting_enemy.defense < 130:
                $ acting_enemy.defense += 8
            if check_party(enemy) != "lost" and enemy.defense < 122:
                $ enemy.defense += 6
            "The Bulwark plants itself and beats its shield once. Stone grit shivers across both constructs as their guard tightens."
            if daggi_accompany and renpy.random.random() < 0.5:
                d "Ah, it's bracing the other one too."
        else:
            if check_party(enemy) != "lost" and enemy.hp < enemy.max_hp:
                $ heal_amount = int((enemy.max_hp - enemy.hp) * 0.18) + 30
                call Enemy_Self_Healing (enemy, heal_amount) from _call_Enemy_Self_Healing_21
                "The Bulwark drags loose bronze fragments across the Glaive Statue's cracked shell, sealing some of the damage and restoring [heal_amount] HP."
            else:
                $ raw_damage = int(renpy.random.randint(enemy2.min_damage + 8, enemy2.max_damage + 12))
                $ enemy_damage = damageFormula(raw_damage, ttg.defense)
                call Damaging (enemy2, ttg, enemy_damage) from _call_Damaging_96
                if ttg == pc:
                    "The Bulwark raises both arms and brings them down in an avalanche-heavy smash that jolts your whole body. Your health decreases by [enemy_damage] HP."
                elif daggi_accompany:
                    "The Bulwark's hammering slam crashes down on Daggi's guard with bone-deep force. [ally.name]'s health decreases by [enemy_damage] HP."
                else:
                    "The Bulwark hammers its slab arms down onto Herd's cover and nearly crushes him behind it. [ally.name]'s health decreases by [enemy_damage] HP."
    return

label crypt_bearstatue_win:
    hide crypt_bear_left
    hide crypt_bear_right
    $ bearguard_dialogues["Chilly Ice Cave"]["Crypt Statue Battle Ready"] = False
    $ bearguard_dialogues["Chilly Ice Cave"]["Crypt Statue Battle Won"] = True

    if daggi_accompany:
        if pc.weapon == None:
            "You hammer the Glaive Statue's split chest while Daggi tears the Bulwark off balance with his harpoon."
        else:
            "You drive your [pc.weapon.name!t] through the Glaive Statue's fractured core while Daggi hooks the Bulwark off balance with his harpoon."
        d "That's it. We've got them."
    else:
        if pc.weapon == None:
            "You shatter the Glaive Statue's balance while Herd smashes the Bulwark's weakened arm at the same instant."
        else:
            "You break the Glaive Statue's core while Herd slams his stone rod into the Bulwark's final crack."

    "Both bronze statues come apart almost together, collapsing into piles of broken metal, stone, and dead frost across the crypt floor."

    $ addItem("Copper", inventory, 2)
    $ addItem("Iron Ingot", inventory, 3)
    $ total_exp_min = int((enemy.exp_drop + enemy2.exp_drop) * 0.9)
    $ total_exp_max = int((enemy.exp_drop + enemy2.exp_drop) * 1.2)
    $ exp_drop = renpy.random.randint(total_exp_min, total_exp_max)
    "Among the rubble, you recover 2 Coppers and 3 Iron ingot."
    call level_up_check (total_exp_min, total_exp_max, 212, 312) from _call_level_up_check_14

    jump Bear_Guard_Cave_Finish

label crypt_bearstatue_lose:
    hide crypt_bear_left
    hide crypt_bear_right
    scene chilly_ice_cave
    if daggi_accompany:
        "The Glaive Statue pins you in place and the Bulwark's finishing blow caves the world in around you. Daggi's shout is the last thing you hear."
    else:
        "The Glaive Statue traps your footing and the Bulwark's follow-up crushes the last of your resistance flat into the crypt floor."
        "Herd lunges toward you, but the falling stone and grinding weight swallow the chamber before either of you can recover."
    scene black with dissolve
    pause 1.0
    "..."
    menu:
        "Back to Main Menu":
            $ MainMenu(confirm=False)()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
