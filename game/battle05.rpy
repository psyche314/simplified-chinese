label caproot_battle:


    $ enemy_num = 1
    $ enemy = caproot
    $ enemy.max_hp = 500
    $ enemy.min_damage = 15
    $ enemy.max_damage = 80
    $ enemy.min_lust_damage = 10
    $ enemy.max_lust_damage = 22
    $ enemy.dodge = 5
    $ enemy.defense = 55
    $ enemy.lust_defense = 20
    $ enemy.exp_drop = 220
    call beginningBattle from _call_beginningBattle_17
    $ caproot.beginbattle()
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    scene dark_forest:
        blur 8
    show caproot:
        xalign 0.5
        yalign 0.7
    if pc.weapon == None:
        "You raise your fist against the caproot, it seems to be flapping its elastic carrot limbs..."
    else:
        "You raise your [pc.weapon.name!t] against the caproot, it seems to be flapping its elastic carrot limbs..."
    jump caproot_battle_loop
label caproot_battle_loop:
    show caproot:
        xalign 0.5
        yalign 0.7
    if check_party(pc) == "lost":
        call Battle_Finish from _call_Battle_Finish_16
        jump caproot_lose
    $ turn_action = ui.interact()
    call Battle_ASF from _call_Battle_ASF_15
    if oa[0] == "A":
        if oa[1] == "M":
            if oa[3] == "A" or oa[3] == "B":
                "You aim and slash your [pc.weapon.name!t] at the caproot, but you simply miss him by inches."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the caproot, but you simply miss him by inches."
            if oa[3] == "N":
                "You throw your fist at the caproot, but you simply miss him by inches."
        else:
            call Enemy_Damaging (target, oa[4]) from _call_Enemy_Damaging_18
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the caproot, your blade grazes through his body."
                "You hear a cracking sound as some pieces falls off."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] at the caproot, knocking him sideway."
                "He stands there unfazed, albeit disheveled."
            if oa[3] == "C":
                "You run while shooting your [pc.weapon.name!t] at the caproot, knocking him sideway."
                "He stands there unfazed, albeit disheveled."
            if oa[3] == "N":
                "You punch into the caproot's core body for multiple times."
            if oa[2] == "N":
                "His health decreases by [oa[4]] HP."
            else:
                "You've critically hit the caproot, dealing [oa[4]] HP!"

    if oa[0] == "S":
        "You struggle against the caproot, trying to break free."
        "You dealt [player_damage] damage to the caproot in the process, his grip has loosen as well."
    if oa[0] == "F":
        "As much as you try to grind your hips against the caproot, he doesn't flinch, or get aroused."
        "It doesn't seem that he is affected by your flirt...."
        "You back off before he tries to grab a hold of your body."
    if oa[0] == "E":
        if oa[1] == "M":
            "You slowly back down from the caproot's attack, you turn around and run as fast as you can."
            "The caproot catches you with his arms and flings your body right back to his roots. Your escape seems to have failed!"
        else:
            "You slowly back down from the caproot's attack, you turn around and run as fast as you can."
            "The caproot tries to catch you with his arms but it barely slips from your body, You successfully escaped from the caproot!"
            call Battle_Finish from _call_Battle_Finish_67
            hide screen battle_buttons
            hide screen battle_enemy_stat
            hide screen battle_player_stat
            jump Split_Trail_Loop
    if oa[0] == "U":
        "You fall to your knees, exhausted all your energy, you grasp for breath as you lie on the ground, surrendering yourself to the caproot."
        "The caproot uses his roots to bring you closer, trying to see if you're breathing..."
        call Battle_Finish from _call_Battle_Finish_17
        jump caproot_lose
    call Ability_Item from _call_Ability_Item_17
    call Battle_Mid_Check from _call_Battle_Mid_Check_15
    if oa[0] == "W":
        call Battle_Finish from _call_Battle_Finish_18
        jump caproot_win
    if oa[0] == "T":
        call Battle_End_Check from _call_Battle_End_Check_34
        jump caproot_battle_loop
    show caproot:
        linear 0.1 zoom 1.04
        linear 0.05 zoom 1
    if caproot.hp > 0 or caproot.lust == caproot.max_lust:
        if check_party(caproot) == "lost":
            call Battle_Finish from _call_Battle_Finish_19
            jump caproot_win
        $ dia = renpy.random.random()
        if dia < 0.50:
            if renpy.random.random()*100 > pc.dodge+extra_dodge:
                $ raw_damage = int(renpy.random.randint(caproot.min_damage, caproot.max_damage))
                $ enemy_damage = damageFormula(raw_damage, pc.defense)
                call Damaging (enemy, pc, enemy_damage) from _call_Damaging_37
                if pc.hp < 0:
                    $ pc.hp = 0
                $ random_chance = renpy.random.random()
                if random_chance < 0.5:
                    "The caproot flings his arm towards you, you are not quick enough to dodge his blow. Your health decreases by [enemy_damage] HP."
                else:
                    "The caproot scrapes at your skin with his roots. Your health decreases by [enemy_damage] HP."
            else:
                $ random_chance = renpy.random.random()
                if random_chance < 0.5:
                    "The caproot flings his arm towards you, but you manage to dodge the attack."
                else:
                    "The caproot tries to catch you with his metal claws, but he misses it by inches."
        elif dia < 0.67 and bound not in status:
            "The caproot wraps your body with his roots..."
            "He is holding you in place."
            $ status.append(bound)
            $ grip_strengtrh = bound.effect
        elif dia < 0.83 and silenced not in status:
            $ silenced.rounds = silenced.max_rounds
            $ status.append(silenced)
            "The caproot's root binds your horns, you are silenced for 2 rounds."
        else:
            $ heal_amount = int((enemy.max_hp - enemy.hp) * (renpy.random.random() * 0.25 + 0.1))
            call Enemy_Self_Healing (enemy, heal_amount) from _call_Enemy_Self_Healing_6
            "The caproot heals himself with his own carrot."
        call Battle_End_Check from _call_Battle_End_Check_35
    jump caproot_battle_loop
label caproot_win:
    "As you defeat the caproot, it soon collapses..."
    "It seems like it shrinks quickly into its normal state..."
    "You pick up the carrot, and put it in your bag."
    $ addItem("Carrot", inventory, 1)
    $ gold_drop = renpy.random.randint(28, 44)
    $ exp_drop = renpy.random.randint(180, 220)
    "You found [gold_drop] gold and [exp_drop] EXP."
    $ pc.exp += exp_drop
    $ pc.gold += gold_drop
    if pc.exp > pc.expCap and pc.level <= levelCap:
        $ pc.LevelUp()
        msg "You are now Level [pc.level]! Check your inventory to allocate your level points."
    scene black
    with dissolve
    pause 1.0
    if mimic_num == 1:

        $ removeSprite(split_trail, caproot_sprite1)
    elif mimic_num == 2:
        $ removeSprite(split_trail, caproot_sprite2)
    elif mimic_num == 3:
        $ removeSprite(split_trail, caproot_sprite3)
    elif mimic_num == 4:
        $ removeSprite(split_trail, caproot_sprite4)
    jump Split_Trail_Loop
label caproot_lose:
    hide screen dungeon_buttons
    hide screen dungeon_map
    "You fell on the ground, the caproot is slowly approaching you."
    "It slaps you across with its root, knocking you out."
    $ lost_gold = int(pc.gold * 0.07*renpy.random.random()) + 40
    "You lost [lost_gold] Gold."
    $ pc.gold -= lost_gold
    if pc.gold < 0:
        $ pc.gold = 0
    scene black
    with dissolve
    pause 1.0
    $ timenow.hour += 5
    $ timenow.passTime()
    if mimic_num == 1:

        $ removeSprite(split_trail, caproot_sprite1)
    elif mimic_num == 2:
        $ removeSprite(split_trail, caproot_sprite2)
    elif mimic_num == 3:
        $ removeSprite(split_trail, caproot_sprite3)
    elif mimic_num == 4:
        $ removeSprite(split_trail, caproot_sprite4)
    "You wake up after a certain amount of time, a carrot on your hand... weird, as you thought to yourself."
    "The caproot is no where to be seen, must be a coincidence..."
    "Shaking your head, you stand right back up and resume your adventure."
    $ addItem("Carrot", inventory, 1)
    jump Split_Trail_Loop
label feral_battle:

    $ status = None
    hide screen dungeon_map

    $ enemy_num = 1
    $ enemy = feral
    $ enemy.max_hp = 550
    $ enemy.min_damage = 55
    $ enemy.max_damage = 84
    $ enemy.min_lust_damage = 10
    $ enemy.max_lust_damage = 22
    $ enemy.dodge = 2
    $ enemy.defense = 60
    $ enemy.lust_defense = 25
    $ enemy.exp_drop = 420
    $ feral.beginbattle()
    call beginningBattle from _call_beginningBattle_18
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen dungeon_buttons
    scene chelforte_cavern:
        blur 8
    show feral:
        xalign 0.5
        yalign 0.4
    "You are facing the feral werewolf, he extends his claws, staring at you with a mix of lust and innate hunger."
    vw "Succumb..."

    jump feral_battle_loop
label feral_battle_loop:

    show feral:
        xalign 0.5
        yalign 0.4

    if check_party(pc) == "lost":
        call Battle_Finish from _call_Battle_Finish_20
        jump feral_lose
    $ turn_action = ui.interact()
    call Battle_ASF from _call_Battle_ASF_16
    if oa[0] == "A":
        if oa[1] == "M":
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the arms of the feral werewolf, it slides right off his fluffy arm, while you look back in disbelief."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] at the arms of the feral werewolf, it slides right off his fluffy arm, while you look back in disbelief."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the arms of the feral werewolf, it pierces right through his soft fur without touching his skin, leaving you frozen in disbelief."
            if oa[3] == "N":
                "You hold your fist and throw it at the feral werewolf, but it hits nothing and leaves you standing instead."
            if renpy.random.random() > 0.5:
                vw "Mine..."
            "The feral werewolf growls loudly."
        else:
            call Enemy_Damaging (target, oa[4]) from _call_Enemy_Damaging_19
            if oa[3] == "A":
                if renpy.random.random() > 0.5:
                    "You slash your [pc.weapon.name!t] at the feral werewolf, your blade grazes through the feral's stomach. Drops of blood drips through his body."
                else:
                    "You slash your [pc.weapon.name!t] at the feral werewolf, knocking him on the ground. He growls at you before getting up, albeit disheveled."
            if oa[3] == "B":
                if renpy.random.random() > 0.5:
                    "You slam your [pc.weapon.name!t] at the feral werewolf, your blade grazes through the feral's stomach. Drops of blood drips through his body."
                else:
                    "You slam your [pc.weapon.name!t] at the feral werewolf, knocking him on the ground. He growls at you before getting up, albeit disheveled."
            if oa[3] == "C":
                if renpy.random.random() > 0.5:
                    "You aim and shoot your [pc.weapon.name!t] at the feral werewolf, the arrow hit right into his shoulder and he screams in agony."
                else:
                    "You run while shooting your [pc.weapon.name!t] at the feral werewolf, knocking him on the ground. He growls at you before getting up, albeit disheveled."
            if oa[3] == "N":
                if renpy.random.random() > 0.5:
                    "You throw your fist at the feral werewolf, hitting him right across his face, the sheer impact knocks him on the ground."
                else:
                    "You punch into the feral werewolf's stomach, grabbing him and slam him on the ground hard."
            if oa[2] == "N":
                "His health decreases by [oa[4]] HP."
            else:
                "You've critically hit the feral werewolf, dealing [oa[4]] HP!"
            $ dia = renpy.random.random()
            if feral.hp >  feral.max_hp * 0.5:
                if dia < 0.3:
                    vw "D-die..."
                elif dia < 0.6:
                    vw "Fear..."
                "The feral werewolf howls, he extends his claws, slashing at anything on sight."
            else:
                if dia < 0.3:
                    vw "Broth-."
                elif dia < 0.6:
                    vw "Cease..."
                "You can barely hear barking sound of the feral werewolf, it almost seems he is acting out his feral rage with a glimpse of confusion."

    if oa[0] == "F":
        $ dia = renpy.random.random()
        if dia > 0.334:
            "You turn around and rub your hand all over your own burly cheeks, feeling and brushing against your ass while you shake your hip."
        elif dia > 0.667:
            "You scrape your member lightly, running your claw from your inner thigh to the back of your balls, you tug at it tightly while staring at the feral seductively."
        else:
            "You cup at your fluffy chest, drawing circles around the area of your nipples. You smile at the feral while your chest bounce up and down slightly."
        if oa[1] == "M":
            "You continue your act for about a minute, but the feral just stares at you in confusion."
        else:
            if feral.lust > feral.max_lust / 2:
                if renpy.random.random() > 0.5:
                    "Within a few seconds you can already see a tingly sight at the feral werewolf."
                    "The sturdy beast man licks his lips, grumbling at your beautiful sight. His lust is increased by [player_flirt]."
                else:
                    "You notice the feral is staring at your crotch, you slightly wink at him and his rage breaks into slight frustration."
                    "His lust is increased by [player_flirt]."
                $ dia = renpy.random.random()
                if dia < 0.33:
                    vw "C-come..."
                elif dia < 0.66:
                    vw "Mmhngh..."
            else:
                if renpy.random.random() > 0.5:
                    "The feral is squirming in reaction to your advance."
                    "You can already hear his rapid breathing and grunting, grasping at his own claws. His lust is increased by [player_flirt]."
                else:
                    "You can tell the feral is already playing with himself when his claws goes under his pants, staring at your ass intently."
                    "His lust is increased by [player_flirt]."
                $ dia = renpy.random.random()
                if dia < 0.33:
                    vw "H-hold."
                elif dia < 0.66:
                    vw "Grrrgh...."

    if oa[0] == "E":
        "You slowly back down from the feral's attack, you turn around and run as fast as you can."
        "But the beast's claw instantly grips onto your tail and you fall on the ground. You cannot escape from this fight."
        vw "N-no..."

    if oa[0] == "U":
        "You fall to your knees, exhausted all your energy, you grasp for breath as you lie on the ground."
        "Maybe surrendering yourself to the feral is the best choice."
        "The beast man jeers at your submission, and he paces around you, poking you to see if you'd still react."
        "You slowly close your eyes and wait for him to decide your fate."
        call Battle_Finish from _call_Battle_Finish_21
        jump feral_lose
    call Ability_Item from _call_Ability_Item_18

    call Battle_Mid_Check from _call_Battle_Mid_Check_16
    if oa[0] == "W":
        call Battle_Finish from _call_Battle_Finish_22
        jump feral_win
    if oa[0] == "T":
        call Battle_End_Check from _call_Battle_End_Check_36
        jump feral_battle_loop
    show feral:
        linear 0.1 zoom 1.04
        linear 0.05 zoom 1
    $ dia = renpy.random.random()
    if dia < 0.35:
        if renpy.random.random()*100 > pc.dodge+extra_dodge:
            $ raw_damage = int(renpy.random.randint(feral.min_damage, feral.max_damage))
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_38
            if pc.hp < 0:
                $ pc.hp = 0
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The feral flaunts his claw towards you. Your health decreases by [enemy_damage] HP."
            else:
                "The feral charges at you, knocking you on the ground. Your health decreases by [enemy_damage] HP."
        else:
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The feral flaunts his claw towards you, you manage to dodge the attack."
            else:
                "The feral charges at you, trying to kick at your but you leap to your side in time."
        $ rand = renpy.random.random()
        if pc.hp > pc.max_hp/2:
            if rand > 0.5:
                vw "Die..."
        else:
            if rand > 0.5:
                vw "A-away..."
    elif dia < 0.7:
        $ raw_damage = int(renpy.random.randint(feral.min_damage, feral.max_damage))
        $ enemy_damage = damageFormula(raw_damage, pc.defense)
        call Damaging (enemy, pc, enemy_damage) from _call_Damaging_39
        if pc.hp < 0:
            $ pc.hp = 0
        "The feral swings his claw at you, scraping against your side. Your health decreases by [enemy_damage] HP."
        if wounded not in status:
            $ wounded.max_rounds = 5
            $ wounded.rounds = wounded.max_rounds
            $ status.append(wounded)
            "You begin bleeding from your wound."
            vw "Bleed..."
        else:
            $ wounded.rounds += wounded.max_rounds
            "Your bleeding has gotten worse from the feral."
    elif dia < 0.75 and bruised not in status:
        $ bruised.rounds = bruised.max_rounds
        $ status.append(bruised)
        "The feral scratches your wound deep, your healing is now reduced by [bruised.effect] percent."
    else:
        $ random_chance = renpy.random.random()
        if random_chance < 0.5:
            "The feral scratches at his pants, he runs two fingers along the shape of his cock in front of you."
            vw "Come."
        else:
            "The feral stretches his body, flaunting his muscular physiques, you can tell his soft is almost bulging in front of you."
            vw "Obey..."

        $ raw_flirt = int(renpy.random.randint(feral.min_lust_damage, feral.max_lust_damage))
        $ enemy_flirt = damageFormula(raw_flirt, pc.lust_defense)
        $ pc.lust += enemy_flirt
        if pc.lust > pc.max_lust:
            $ pc.lust = pc.max_lust
        if dia > 0.9:
            "You gulp at the feral's attempt at seduction. As much as he is feral... his attempt at seduction has left you salivating..."
            "You are extremely aroused, thinking about how his cock would taste like."
            "Your lust increased by [enemy_flirt]."
        else:
            "You are stunned by his gorgeous muscles, you mind wanders through scenarios of him being inside your body."
            "Your lust increased by [enemy_flirt]."

    call Battle_End_Check from _call_Battle_End_Check_37
    jump feral_battle_loop

label feral_win:
    hide feral
    scene chelforte_cavern with dissolve
    $ feral.win += 1
    $ exp_drop = 400
    if feral.hp <= 0:
        "The feral werewolf falls, pased out, but still breathing slightly..."
    else:
        "The feral werewolf falls, pased out, with his cock fully erected..."
    $ pc.exp += exp_drop
    $ found_gold = renpy.random.randint(200, 300)
    "You found [found_gold] gold and [exp_drop] experience from the feral. You pick them up swiftly."
    $ pc.gold += found_gold
    if pc.exp > pc.expCap and pc.level <= levelCap:
        $ pc.LevelUp()
        msg "You are now Level [pc.level]! Check your inventory to allocate your level points."

    if wuldon_meet:
        jump Vurro_Battle_Win_With_Wuldon
    else:
        jump Vurro_Battle_Win_Without_Wuldon

label feral_lose:
    hide feral
    scene chelforte_cavern with dissolve
    if pc.hp <= 0:
        "You struggle against the feral, you have already exhausted all your energy. He pounces on your helpless body like you are a feast to be served."
    if pc.lust >= pc.max_lust:
        "You struggle against the feral, your mind is filled with unquenchable lust over the feral. He pounces on your helpless body like you are a feast to be served."

    scene black with dissolve
    "..."
    $ feral.lose += 1
    call scene_feral_lose from _call_scene_feral_lose
    if pc.cor > 80:
        "After you wake up, you realize the feral is fast asleep."
        "The air still smells of sex."
        "The intercourse was intense and it was an exhilarating feeling."
        "However, you know that your journey still awaits you, you cannot succumb to the lust in your mind... yet."
        "You steal out of the cave."
        $ pc.add_active_status(stuffed)
        call lost_gold_check (0.07, 40, True) from _call_lost_gold_check_12
        jump main_dark_forest
    else:
        jump BadEnd_FeralLose

label goatranger_battle:



    $ enemy_num = 1
    $ enemy = goatranger

    $ enemy.max_hp = 500
    $ enemy.min_damage = 55
    $ enemy.max_damage = 72
    $ enemy.defense = 60
    $ enemy.min_lust_damage = 20
    $ enemy.max_lust_damage = 25
    $ enemy.dodge = 50
    $ enemy.lust_defense = 30
    $ enemy.exp_drop = 60
    $ goatranger.beginbattle()
    call beginningBattle from _call_beginningBattle_19
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons

    scene kechioeren_training_ground:
        blur 8
    show goat ranger:
        xalign 0.5
        yalign 0.7
    if pc.weapon == None:
        "You are facing a goat ranger, he is waving his bow in arrogance, gesturing you to come closer. You hold and clench your fist."
    else:

        "You are facing a goat ranger, he is waving his bow in arrogance, gesturing you to come closer. You hold your [pc.weapon.name!t] in defence."

    jump goatranger_battle_loop
label goatranger_battle_loop:

    show goat ranger:
        xalign 0.5
        yalign 0.7

    if check_party(pc) == "lost":
        call Battle_Finish from _call_Battle_Finish_23
        jump Kari_Goat_Practice_Lose
    $ turn_action = ui.interact()
    call Battle_ASF from _call_Battle_ASF_17
    if oa[0] == "A":
        if oa[1] == "M":
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the arm of the goat, but he leaps back and avoid the blow by inches."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] at the goat's head, but he leaps back and avoid the blow by inches."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the goat, but he leaps back and avoid the arrow by inches."
            if oa[3] == "N":
                "You throw your fist at the goat, but he leaps back and avoid the blow by inches."
            if renpy.random.random() > 0.5:
                gtr "T-that wasn't a good attempt, you need to do better."
            else:
                gtr "Didn't general tell you I'm good at dodging? Probably not as good as your weapon dodging me."
        else:
            call Enemy_Damaging (target, oa[4]) from _call_Enemy_Damaging_20
            if oa[3] == "A":
                if renpy.random.random() > 0.5:
                    "You slash your [pc.weapon.name!t] at the arm of the goat, your blade grazes through the goat's stomach. Drops of blood drips through his body."
                else:
                    "You slash your [pc.weapon.name!t] at the arm of the goat, knocking him on the ground. He growls at you before getting up, albeit disheveled."
            if oa[3] == "B":
                if renpy.random.random() > 0.5:
                    "You slam your [pc.weapon.name!t] at the goat's abdomen, your blade grazes through his stomach. Drops of blood drips through his body."
                else:
                    "You slam your [pc.weapon.name!t] at the goat's head, knocking him on the ground. He growls at you before getting up, albeit disheveled."
            if oa[3] == "C":
                if renpy.random.random() > 0.5:
                    "You aim and shoot your [pc.weapon.name!t] at the goat, the arrow hit right into his shoulder."
                else:
                    "You run while shooting your [pc.weapon.name!t] at the goat, knocking him on the ground. He growls at you before getting up, albeit disheveled."
            if oa[3] == "N":
                if renpy.random.random() > 0.5:
                    "You throw your fist at the goat, hitting him right across his face, the sheer impact knocks him on the ground."
                else:
                    "You punch into the goat's stomach, grabbing him and slam him on the ground hard."
            if oa[2] == "N":
                "His health decreases by [oa[4]] HP."
            else:
                "You've critically hit the ranger, dealing [oa[4]] HP!"
            $ dia = renpy.random.random()
            if goatranger.hp > goatranger.max_hp * 0.5:
                if dia < 0.33:
                    gtr "Well, that hadn't happened before?"
                elif dia < 0.67:
                    gtr "Grrrrr! L-lucky hit... Let me teach you how to fight properly!"
            else:
                if dia < 0.33:
                    gtr "Damn... didn't know a courier can hit that hard...!"
                elif dia < 0.67:
                    gtr "H-hey, be gentle, I haven't gotten hit before."

    if oa[0] == "F":
        $ dia = renpy.random.random()
        if dia > 0.334:
            "You turn around and rub your hand all over your own burly cheeks, feeling and brushing against your ass while you shake your hip."
        elif dia > 0.667:
            "You scrape your member lightly, running your claw from your inner thigh to the back of your balls, you tug at it tightly while staring at the goat seductively."
        else:
            "You cup at your fluffy chest, drawing circles around the area of your nipples. You smile at the goat while your chest bounce up and down slightly."
        if oa[1] == "M":
            "You continue your act for about a minute, but the ranger doesn't even flinch."
            gtr "Well..."
        else:
            if goatranger.lust > goatranger.max_lust / 2:
                if renpy.random.random() > 0.5:
                    "Within a few seconds you can already see some movements under the goat's loincloth. He doesn't say anything, except for licking his lips. His lust is increased by [player_flirt]."
                    gtr "...I-if you do this one more time I'm going to grab that huge ass and never let you go..."
                else:
                    "You notice the goat is floundering, trying his best not to get aroused by your seduction, but it is evident that his flushed face tells it all. His lust is increased by [player_flirt]."
                    gtr "You are w-wasting your time. I'm n-not... I'm not... I- uhh... nooo..."
            else:
                if renpy.random.random() > 0.5:
                    "The goat ranger is squirming in reaction to your advance. You can already hear his rapid breathing and grunting, holding his bow tightly. His lust is increased by [player_flirt]."
                    gtr "N-noooo. I c-can't control... my mind. Please..."
                else:
                    "You can tell the ranger is already playing with himself when his hand goes under his loincloth, staring at your ass intently. His lust is increased by [player_flirt]."
                    gtr "Hnnnngh... I n-need to... come."
    if oa[0] == "E":
        "You cannot run away from battle practice..."

    if oa[0] == "U":
        "You fall to your knees, exhausted all your energy, you grasp for breath as you lie on the ground, surrendering yourself to the ranger."
        call Battle_Finish from _call_Battle_Finish_24
        jump Kari_Goat_Practice_Lose
    call Ability_Item from _call_Ability_Item_19
    call Battle_Mid_Check from _call_Battle_Mid_Check_17
    if oa[0] == "W":
        call Battle_Finish from _call_Battle_Finish_25
        jump Kari_Goat_Practice_Win
    if oa[0] == "T":
        call Battle_End_Check from _call_Battle_End_Check_38
        jump goatranger_battle_loop
    show goat ranger:
        linear 0.1 zoom 1.04
        linear 0.05 zoom 1

    $ dia = renpy.random.random()
    if dia < 0.325:
        if renpy.random.random()*100 > pc.dodge+extra_dodge:
            $ raw_damage = int(renpy.random.randint(goatranger.min_damage, goatranger.max_damage))
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_40
            if pc.hp < 0:
                $ pc.hp = 0
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The goat ranger shoots his bow towards you, you are not quick enough to dodge his blow. Your health decreases by [enemy_damage] HP."
            else:
                "The goat bounces around and hit you with the wooden part of the bow. Your health decreases by [enemy_damage] HP."
            gtr "Heh, you're getting beaten by a prodigy at battle."
        else:
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The goat ranger swings his bow towards you, you managed to deflect his bow and dodge the attack."
            else:
                "The goat bounces around and try to hit you with the wooden part of the bow, but you block the blow and push him back."
            gtr "Well, I'm the best dodger, not the best shooter. Stop staring at me like that."
    elif dia < 0.65:
        $ raw_damage = int(renpy.random.randint(goatranger.min_damage, goatranger.max_damage))
        $ enemy_damage = damageFormula(raw_damage, pc.defense)
        call Damaging (enemy, pc, enemy_damage) from _call_Damaging_41
        "The ranger shoots his bow, right into your arms. Your health decreases by [enemy_damage] HP."
        if wounded not in status:
            $ wounded.max_rounds = 4
            $ wounded.rounds = wounded.max_rounds
            $ status.append(wounded)
            "You begin bleeding from your wound."
            gtr "Well, sorry about that, but surely general will heal you back after this."
        else:
            $ wounded.rounds += wounded.max_rounds
            "Your bleeding has gotten worse from the ranger."
    elif dia < 0.80 and trapped not in status:
        "While you are calculating your next move, you fall into his trap, your dodges are now reduced by half for 3 rounds."
        $ trapped.rounds = trapped.max_rounds
        $ status.append(trapped)
        $ extra_dodge -= pc.dodge/2
        $ extra_lust_dodge -= pc.lust_dodge/2
    else:
        if renpy.random.random()*100 > pc.lust_dodge + extra_lust_dodge:
            $ raw_flirt = int(renpy.random.randint(goatranger.min_lust_damage, goatranger.max_lust_damage))
            $ enemy_flirt = damageFormula(raw_flirt, pc.lust_defense)
            $ pc.lust += enemy_flirt
            if pc.lust > pc.max_lust:
                $ pc.lust = pc.max_lust
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The goat scratches at his loincloth, he put two of his fingers across his crotch, tracing the shape of his cock in front of you."
                gtr "You thristy? Surrender to me and maybe you'll have the best time of your life."
                "You gulp at his attempt at seduction. Admittedly you are extremely aroused, thinking about how his cock would taste like. Your lust increased by [enemy_flirt]."
            else:
                "The ranger stretches his body, flaunting his muscular physiques, you can tell his soft chest is almost bulging in front of you."
                gtr "You see how strong of a specimen I am. Come closer to get a better look!"
                "You are stunned by his gorgeous muscles, you mind wanders through scenarios of him being inside your body. Your lust increased by [enemy_flirt]."
        else:
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The goat scratches at his loincloth, he put two of his fingers across his crotch, tracing the shape of his cock in front of you."
                gtr "You thristy? Surrender to me and maybe you'll have the best time of your life."
                "You stare at him, giving him weird side eyes. You have evaded his attempt at seduction. And the goat seems to feel a little dejected."
            else:
                "The ranger stretches his body, flaunting his muscular physiques, you can tell his soft chest is almost bulging in front of you."
                gtr "You see how strong of a specimen I am. Come closer to get a better look!"
                "His attack at your lust seems to have failed as you stand there and wait for him to finish his taunt. Both of you would never speak about it again."

    call Battle_End_Check from _call_Battle_End_Check_39
    jump goatranger_battle_loop

label heftyslime_battle:


    $ enemy_num = 1
    $ enemy = heftyslime

    if wslime_progress > 0 and not quest31.status == True:
        $ enemy.max_hp = 40+10*wslime_progress+125**(wslime_progress/7)
    else:
        $ enemy.max_hp = 500
    $ enemy.max_damage = 58
    $ enemy.max_damage = 88
    $ enemy.defense = 50
    $ enemy.dodge = 5
    $ enemy.lust_dodge = 5
    $ enemy.lust_defense = 35
    $ enemy.min_lust_damage = 18
    $ enemy.max_lust_damage = 26
    call beginningBattle from _call_beginningBattle_15
    $ heftyslime.beginbattle()
    hide screen dungeon_map
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen dungeon_buttons
    scene dark_forest:
        blur 8
    if isinstance(current_location, MapPat) and current_location.img == "Forgotten Sanctuary":
        scene forgotten_sanctuary:
            blur 8
    if wslime_progress > 0 and not quest31.status == True:
        scene forgotten_sanctuary:
            blur 8
    $ enemy_image = "heftyslime"
    if pc.weapon == None:
        "You are facing a hefty slime, the viscous goo is dripping slightly, and bounces towards you. You raise your fist in response."
    else:
        "You are facing a hefty slime, the viscous goo is dripping slightly, and bounces towards you. You raise your [pc.weapon.name!t] in response."
    jump general_battle_loop

label heftyslime_battle_loop:

    if heftyslime.hp > 0 or heftyslime.lust == heftyslime.max_lust:
        if check_party(heftyslime) == "lost":
            call Battle_Finish from _call_Battle_Finish_63
            jump heftyslime_win
        $ dia = renpy.random.random()
        if dia < 0.50:
            if renpy.random.random()*100 > pc.dodge+extra_dodge:
                $ raw_damage = int(renpy.random.randint(heftyslime.min_damage, heftyslime.max_damage))
                $ enemy_damage = damageFormula(raw_damage, pc.defense)
                call Damaging (enemy, pc, enemy_damage) from _call_Damaging_42
                $ random_chance = renpy.random.random()
                if random_chance < 0.5:
                    "The slime flings itself towards you, but you are not quick enough to dodge it. It drains your health by [enemy_damage] HP."
                else:
                    "The slime slaps your leg, knocking you on the ground. It drains your health by [enemy_damage] HP."
                call Enemy_Self_Healing (heftyslime, (enemy_damage / 1.5)) from _call_Enemy_Self_Healing_7
            else:
                $ random_chance = renpy.random.random()
                if random_chance < 0.5:
                    "The slime flings itself towards you, but you manage to dodge its attack."
                else:
                    "The slime tries to slaps your leg, but it misses by inches."
        elif dia < 0.67 and silenced not in status:
            "The slime wraps itself around your hands, coating it with slippery goo before letting go of you."
            "You are now silenced."
            $ status.append(silenced)
            $ silenced.rounds = silenced.max_rounds
        else:
            $ raw_flirt = int(renpy.random.randint(heftyslime.min_lust_damage, heftyslime.max_lust_damage))
            $ enemy_flirt = damageFormula(raw_flirt, pc.lust_defense)
            $ pc.lust += enemy_flirt
            if pc.lust > pc.max_lust:
                $ pc.lust = pc.max_lust
            $ random_chance = renpy.random.random()
            "The slime splashes itself onto your body, and infuses some form of... aphrodisiac through your fur."
            $ pc.cor -= 1
            if pc.cor < 0:
                $ pc.cor = 0
            "Instantly your mind is filled with sexual scenes, you can't shake that thought... that image of you being naked with everyone else. Your lust increased by [enemy_flirt]."
        call Battle_End_Check from _call_Battle_End_Check_31

    jump general_battle_loop

label heftyslime_win:
    if wslime_progress > 0 and not quest31.status == True:
        jump Slimy_Fight_Begin
    "As you defeat the slime, the entity seems to disintegrate completely before your eyes."
    "Only leaving behind drips and drops of green goo on the grass."
    if equippedTrinket("Lindbloom"):
        $ rnd = .7
        $ rnd2 = .6
    else:
        $ rnd = .35
        $ rnd2 = .3
    if mimic_num == 3:
        if slime1_dp[1] != 1:
            $ addItem("Flagitious Ooze", inventory, 1)
            "You found a... Flagitious Ooze, what Haskell called."
        $ slime1_dp[1] = 1
    if mimic_num == 4:
        if slime1_dp[2] != 1:
            $ addItem("Teratoid Mucus", inventory, 1)
            "You found a... Teratoid Mucus, it was pretty slick."
        $ slime1_dp[2] = 1
    $ gold_drop = renpy.random.randint(44, 60)
    $ exp_drop = renpy.random.randint(180, 230)
    "You found [gold_drop] gold and [exp_drop] EXP."
    $ pc.exp += exp_drop
    $ pc.gold += gold_drop
    if pc.exp > pc.expCap and pc.level <= levelCap:
        $ pc.LevelUp()
        msg "You are now Level [pc.level]! Check your inventory to allocate your level points."
    if mimic_num == 1:
        $ removeSprite(viscid_stream, hefty_sprite1)
        $ hefty_sprite1.lp = 0
    if mimic_num == 2:
        $ removeSprite(viscid_stream, hefty_sprite2)
        $ hefty_sprite2.lp = 0
    if mimic_num == 5:
        $ removeSprite(creek_thicket, hefty_sprite3)
        $ hefty_sprite3.death = True
        $ hefty_sprite3.lp = 0
    if mimic_num == 6:
        $ removeSprite(creek_thicket, hefty_sprite4)
        $ hefty_sprite4.death = True
        $ hefty_sprite4.lp = 0
    if mimic_num == 7:
        $ removeSprite(creek_thicket, hefty_sprite5)
        $ hefty_sprite5.death = True
        $ hefty_sprite5.lp = 0
    if mimic_num == 8:
        $ removeSprite(creek_thicket, hefty_sprite6)
        $ hefty_sprite6.death = True
        $ hefty_sprite6.lp = 0

    if current_location.img == "Viscid Stream":
        jump Viscid_Stream_Loop
    elif current_location.img == "Creek Thicket":
        jump Creek_Thicket_Loop
    else:
        jump Forgotten_Sanctuary_Loop
label heftyslime_lose:
    hide screen dungeon_buttons
    hide screen dungeon_map
    if wslime_progress > 0 and not quest31.status == True:
        jump Slimy_Fight_Lose
    "You fell on the ground, but the slime continues to slither towards you."
    "There's no strength left inside you to struggle against its grasp..."
    call Scene_Hefty_Slime_Lose from _call_Scene_Hefty_Slime_Lose
    $ pc.add_active_status(stuffed)
    $ pc.add_active_status(soremouthed)
    call lost_gold_check (0.04, 50, True) from _call_lost_gold_check_13
    $ pc.cor -= 3
    if pc.cor < 0:
        $ pc.cor = 0

    scene black
    with dissolve
    pause 1.0
    if current_location.img == "Viscid Stream":
        call Leaving_Viscid_Stream from _call_Leaving_Viscid_Stream_3
        jump main_dark_forest
    elif current_location.img == "Creek Thicket":

        call Leaving_Creek_Thicket from _call_Leaving_Creek_Thicket
        jump main_dark_forest
    else:
        call Leaving_Forgotten_Sanctuary from _call_Leaving_Forgotten_Sanctuary_1
        jump main_dark_forest

label malignantslime_battle:


    $ enemy_num = 1
    $ enemy = malignantslime
    $ enemy.max_hp = 800
    $ enemy.max_damage = 58
    $ enemy.max_damage = 88
    $ enemy.defense = 65
    $ enemy.dodge = 5
    $ enemy.lust_dodge = 5
    $ enemy.lust_defense = 35
    $ enemy.min_lust_damage = 18
    $ enemy.max_lust_damage = 26
    $ enemy_image = "malignantslime"
    call beginningBattle from _call_beginningBattle_20
    $ malignantslime.beginbattle()
    hide screen dungeon_map
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen dungeon_buttons
    scene forgotten_sanctuary:
        blur 8
    $ enemy_image = "malignantslime"
    if pc.weapon == None:
        "You are facing a malignant slime, the viscous goo is dripping slightly, its eyes drooling towards you. You raise your fist in response."
    else:
        "You are facing a malignant slime, the viscous goo is dripping slightly, its eyes drooling towards you. You raise your [pc.weapon.name!t] in response."
    jump general_battle_loop

label malignantslime_battle_loop:

    if enemy_num == 2:
        if check_party(heftyslime) == "lost":
            $ enemy_num = 1
            $ enemy.item_chance01 = 0.5
            hide heftyslime with dissolve
            show expression enemy_image:
                xalign 0.5
                yalign 0.5
            with move
        if check_party(malignantslime) == "lost":
            call Battle_Finish from _call_Battle_Finish_7
            jump malignantslime_win

    $ dia = renpy.random.random()
    if dia < 0.50:
        if renpy.random.random()*100 > pc.dodge+extra_dodge:
            $ raw_damage = int(renpy.random.randint(malignantslime.min_damage, malignantslime.max_damage))
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_43
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The malignant slime throws its gooey arms towards you, but you are not quick enough to dodge it. It drains your health by [enemy_damage] HP."
            else:
                "The malignant slime slaps you in your sides, knocking you on the ground. It drains your health by [enemy_damage] HP."
            call Enemy_Self_Healing (enemy, int(enemy_damage / 1.5)) from _call_Enemy_Self_Healing_8
        else:
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The malignant slime throws its gooey arms towards you, but you manage to dodge its attack."
            else:
                "The malignant slime tries to slap you in your sides, but it misses by inches."
    elif dia < 0.67:
        if enemy_num == 2:
            "The malignant slime glows faintly, connecting itself with the smaller slime."
            $ healing = int(20 + (enemy.max_hp - enemy.hp)*0.15*renpy.random.random())
            "It drains [healing] HP from the hefty slime."
            $ heftyslime.hp -= healing
            $ malignantslime.hp += healing
            call Trinket_Weeping_Willow from _call_Trinket_Weeping_Willow_10

        if enemy_num == 1:
            $ enemy_num = 2
            $ enemy2 = heftyslime
            $ enemy2.max_hp = 300
            $ enemy2.max_damage = 38
            $ enemy2.max_damage = 58
            $ enemy2.defense = 30
            $ enemy2.lust_defense = 35
            $ enemy2.min_lust_damage = 18
            $ enemy2.max_lust_damage = 26
            $ enemy2.beginbattle()
            $ enemy.item_chance01 = 0.1
            show expression enemy_image:
                xalign 0.1
                yalign 0.5
            with move
            show heftyslime:
                xalign 1.0
                yalign 0.5
            "A part of the malignant slime split apart! It is forming... another slime."
            "You are now also facing Hefty Slime."

    elif dia < 0.83 and bound not in status:
        "The malignant slime wraps itself around you, refusing to let go of you."
        "You are now bound."
        $ status.append(bound)
        $ grip_strengtrh = bound.effect
    else:
        $ raw_flirt = int(renpy.random.randint(malignantslime.min_lust_damage, malignantslime.max_lust_damage))
        $ enemy_flirt = damageFormula(raw_flirt, pc.lust_defense)
        $ pc.lust += enemy_flirt
        if pc.lust > pc.max_lust:
            $ pc.lust = pc.max_lust
        $ random_chance = renpy.random.random()
        "The malignant slime splashes itself onto your body, and infuses some form of... aphrodisiac through your fur."
        "Instantly your mind is filled with sexual scenes, you can't shake that thought... that image of you being naked with everyone else. Your lust increased by [enemy_flirt]."

    if enemy_num == 2:
        if check_party(heftyslime) == "lost":
            $ enemy_num = 1
            $ enemy.item_chance01 = 0.5
            show expression enemy_image:
                xalign 0.5
                yalign 0.5
            with move
        else:
            show heftyslime:
                linear 0.1 zoom 1.04
                linear 0.05 zoom 1
            jump heftyslime_battle_loop

    call Battle_End_Check from _call_Battle_End_Check_41
    jump general_battle_loop

label malignantslime_win:
    hide expression enemy_image with dissolve
    "As you defeat the slime, the entity seems to disintegrate completely before your eyes."
    if enemy_num == 2:
        hide heftyslime with dissolve
        "The smaller slime soon follow suit, slowly shrinking into a puddle of goo."
        $ gold_drop = renpy.random.randint(100, 140)
        $ exp_drop = renpy.random.randint(380, 520)
    else:
        $ gold_drop = renpy.random.randint(44, 60)
        $ exp_drop = renpy.random.randint(180, 230)
    "Only leaving behind drips and drops of green goo on the grass."
    if wslime_progress > 0 and not quest31.status == True:
        jump Slimy_Fight_Begin
    if equippedTrinket("Lindbloom"):
        $ rnd = .7
    else:
        $ rnd = .35
    if renpy.random.random() < .35:
        "You found a Slime ball."
        $ addItem("Slime Ball", inventory, 1)
    if slime1_dp[3] != 1:
        $ addItem("Slime Grancrystal", inventory, 1)
        "You found a Slime Grancrystal... embedded on the slime, it was quite a big one, might be bigger than what Haskell described."
    $ slime1_dp[3] = 1
    "You put the material into your bag."


    "You found [gold_drop] gold and [exp_drop] EXP."
    $ pc.exp += exp_drop
    $ pc.gold += gold_drop
    if pc.exp > pc.expCap and pc.level <= levelCap:
        $ pc.LevelUp()
        msg "You are now Level [pc.level]! Check your inventory to allocate your level points."
    jump Forgotten_Sanctuary_Loop

label malignantslime_lose:
    hide screen dungeon_buttons
    hide screen dungeon_map
    if wslime_progress > 0 and not quest31.status == True:
        jump Slimy_Fight_Lose
    "You fell on the ground, but the slime continues to slither towards you."
    "There's no strength left inside you to struggle against its grasp..."
    call Scene_Hefty_Slime_Lose from _call_Scene_Hefty_Slime_Lose_1
    $ gold_lost = int(50 + renpy.random.random()*0.4*pc.gold)
    $ pc.gold -= gold_lost
    if pc.gold < 0:
        $ pc.gold = 0

    $ pc.cor -= 4
    if pc.cor < 0:
        $ pc.cor = 0
    "You lost [gold_lost] gold."
    scene black
    with dissolve
    pause 1.0
    if current_location.img == "Viscid Stream":
        call Leaving_Viscid_Stream from _call_Leaving_Viscid_Stream_4
        jump main_dark_forest
    else:
        call Leaving_Forgotten_Sanctuary from _call_Leaving_Forgotten_Sanctuary_2
        jump main_dark_forest

label nosferat_battle:


    $ enemy_num = 1
    $ enemy = nosferat
    if current_location.img == "Chelforte Cavern":
        $ enemy.max_hp = 400
    $ nosferat.item_drop02 = 0
    $ enemy.max_damage = 48
    $ enemy.max_damage = 78
    $ enemy.defense = 50
    $ enemy.dodge = 14
    $ enemy.lust_defense = 35
    $ enemy.min_lust_damage = 25
    $ enemy.max_lust_damage = 26
    call beginningBattle from _call_beginningBattle_21
    $ nosferat.beginbattle()
    hide screen dungeon_map
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen dungeon_buttons

    scene chelforte_cavern:
        blur 8
    show nosferat:
        xalign 0.5
        yalign 0.25
    if pc.weapon == None:
        "You are facing a nosferat, it is holding a form of dripstone while drooling at your body. You raise your fist in response."
    else:
        "You are facing a nosferat, it is holding a form of dripstone while drooling at your body. You raise your [pc.weapon.name!t] in response."
    jump nosferat_battle_loop

label nosferat_battle_loop:
    $ nosferat.item_drop02 += 1
    show nosferat:
        xalign 0.5
        yalign 0.25
    if check_party(pc) == "lost":
        call Battle_Finish from _call_Battle_Finish_70
        jump nosferat_lose
    $ turn_action = ui.interact()
    call Battle_ASF from _call_Battle_ASF_20
    if oa[0] == "A":
        if oa[1] == "M":
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the nosferat's arm. It slides right off his fluffy arm. You can only look on in disbelief."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] into the nosferat's arm. It bounces right off. You can only look back in disbelief."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the nosferat's arms. It pierces right through his soft fur but fails to make a dent in his skin, leaving you frozen in disbelief."
            if oa[3] == "N":
                "You raise your fist and throw it at the nosferat, but miss and hit nothing, leaving you standing there like a fool instead."
            if renpy.random.random() > 0.5:
                "The nosferat growls loudly, flinging his arms in your direction."
        else:
            call Enemy_Damaging (target, oa[4]) from _call_Enemy_Damaging_21
            if oa[3] == "A":
                if renpy.random.random() > 0.5:
                    "You slash your [pc.weapon.name!t] at the nosferat, grazing its stomach and drawing blood."
                else:
                    "You slash your [pc.weapon.name!t] at the nosferat, knocking him to the ground. He growls at you before getting up, somehow angrier than albeit disheveled. "
            if oa[3] == "B":
                if renpy.random.random() > 0.5:
                    "You slam your [pc.weapon.name!t] into the nosferat, cutting a bright red gash into his purple hide. The fur around the weeping wound grows matted with blood."
                else:
                    "You slam your [pc.weapon.name!t] into the nosferat's face, tipping him off balance with a loud thump and roar."
            if oa[3] == "C":
                if renpy.random.random() > 0.5:
                    "You aim and shoot your [pc.weapon.name!t] at the nosferat. The arrow hits him right in the shoulder. He screams in agony."
                else:
                    "You run while shooting your [pc.weapon.name!t] at the nosferat, knocking him to the ground. He growls at you before getting up, albeit disheveled."
            if oa[3] == "N":
                if renpy.random.random() > 0.5:
                    "You throw your fist at the nosferat, hitting him across his face, the sheer impact of which knocks him to the ground."
                else:
                    "You punch into the nosferat's stomach making him double over in pain. You use this opportunity to knee him in the face. It feels like hitting a stone wall, but the nosferat slams into the ground hard."
            if oa[2] == "N":
                "His health decreases by [oa[4]] HP."
            else:
                "It seems you've hit the nosferat critically, dealing [oa[4]] HP!"
            $ dia = renpy.random.random()
            if nosferat.hp >  nosferat.max_hp * 0.5:
                if dia < 0.5:
                    "The nosferat grunts in anger, he definitely doesn't appreciate getting battered by a feeble watcher."
            else:
                if dia < 0.5:
                    "You can barely hear the groaning sound of the nosferat. He is in absolute distress, and ready to slaughter his attacker without mercy."
    if oa[0] == "S":
        "You struggle against the nosferat, trying to break free. You dealt [oa[4]] damage to the mimic in the process, his grip has loosen as well."
    if oa[0] == "F":
        $ dia = renpy.random.random()
        if dia > 0.334:
            "You turn around and rub your hand all over your burly cheeks, feeling up and brushing against your ass while you shake your hips."
        elif dia > 0.667:
            "You gently brush by your member, running a claw from your inner thigh to the back of your balls. You tug at them lightly while staring at the nosferat seductively."
        else:
            "You cup your fluffy chest, drawing circles around the area of your nipples. You smile at the nosferat while bouncing your chest up and down slightly."

        if oa[1] == "M":
            "You continue your act for about a minute, but the nosferat just stares at you in confusion."
        else:
            if nosferat.lust > nosferat.max_lust / 2:
                if renpy.random.random() > 0.5:
                    "Within a few seconds you can already see some movements direction in the nosferat's cock. The sturdy beast man licks his lips, grumbling at your beautiful sight. His lust is increased by [player_flirt]."
                else:
                    "You notice the nosferat is staring at your crotch. You give him a subtle wink. He already looks like he can't breath from his arousal. His lust is increased by [player_flirt]."
            else:
                if renpy.random.random() > 0.5:
                    "The nosferat is squirming in reaction to your advance. You can already hear his rapid breathing and grunting, holding his dripstone tightly. His lust is increased by [player_flirt]."
                else:
                    "You can tell the nosferat is already playing with himself when his hand wanders on his crotch, staring at your ass intently. His lust is increased by [player_flirt]."
    if oa[0] == "E":
        if oa[0] == "M":
            "You slowly back down from the nosferat's attack, you turn around and run as fast as you can."
            "But the beast easily catches up to you and throws your entire body on the ground. Your escape seems to have failed!"
        else:
            "You slowly back down from the nosferat's attack, you turn around and run as fast as you can. The beast tries to outrun you but he trips and falls on the ground, You successfully escaped from the huntsman!"
            call Battle_Finish from _call_Battle_Finish_71
            show screen dungeon_buttons
            jump Chelforte_Cavern_Loop
    if oa[0] == "U":
        "You fall to your knees, exhausted of all your energy. You grasp for breath as you lie on the ground, thinking surrendering yourself to the nosferat might be the best choice."
        "The beast man jeers at your submission, he walks around you, poking you to see if you'd still react. You slowly close your eyes and wait for him to decide your fate."

        call Battle_Finish from _call_Battle_Finish_72
        jump nosferat_lose
    call Ability_Item from _call_Ability_Item_21
    call Battle_Mid_Check from _call_Battle_Mid_Check_19
    if oa[0] == "W":
        call Battle_Finish from _call_Battle_Finish_73
        jump nosferat_win
    if oa[0] == "T":
        call Battle_End_Check from _call_Battle_End_Check_42
        jump nosferat_battle_loop
    show nosferat:
        linear 0.1 zoom 1.04
        linear 0.05 zoom 1


    if nosferat.item_drop02 % 3 == 0:
        if renpy.random.random()*100 > pc.dodge+extra_dodge:
            $ raw_damage = int(renpy.random.randint(nosferat.min_damage, nosferat.max_damage))
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_44
            if pc.hp < 0:
                $ pc.hp = 0
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The nosferat swings his giant dripstone towards you. You are not quick enough to dodge his blow. Your health decreases by [enemy_damage] HP."
            else:
                "The nosferat charges at you, knocking away your guard with his off-hand before hitting you with a kick to the chest. Your health decreases by [enemy_damage] HP."
        else:
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The nosferat swings his giant dripstone towards you. You barely manage to deflect his heavy mace and dodge the attack."
            else:
                "The nosferat charges at you, trying to kick your chest, but you block the blow and push him back."
    elif nosferat.item_drop02 % 3 == 1:
        if bound not in status:
            "The nosferat wraps his arms around you, you try to struggle free but his fluffy arms are too strong!"
            "He is holding you in place."
            $ status.append(bound)
            $ grip_strength = bound.effect
        else:
            $ raw_damage = int(renpy.random.randint(nosferat.min_damage, nosferat.max_damage))*2
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_45
            if pc.hp < 0:
                $ pc.hp = 0
            "As you're already in his embrace. The nosferat slams you against the ground. Causing you to scream in pain."
            "You are no longer bound, but your Health decreases by [enemy_damage] HP."
    else:
        $ raw_flirt = int(renpy.random.randint(nosferat.min_lust_damage, nosferat.max_lust_damage))
        $ enemy_flirt = damageFormula(raw_flirt, pc.lust_defense)
        $ pc.lust += enemy_flirt
        if pc.lust > pc.max_lust:
            $ pc.lust = pc.max_lust
        $ random_chance = renpy.random.random()
        "The nosferat licks his lips, positioning his hip forward so your sight are locked into his gorgeous cock..."
        "You instantly become extremely aroused. Thinking about how it would fit inside you... Your lust increased by [enemy_flirt]."
    call Battle_End_Check from _call_Battle_End_Check_43
    if renpy.random.random() < 0.33:
        "It seems... there's a pattern in nosferat's Attack, maybe you can utilise it to your advantage..."
    jump nosferat_battle_loop
label nosferat_win:

    "You defeat nosferat quite easily. The nosferat quietly slips away and hide into the depth of the cave again."
    $ gold_drop = renpy.random.randint(24, 40)
    $ exp_drop = renpy.random.randint(160, 200)
    if renpy.random.random() < 0.25:
        if sunderingsurge not in learnedabilities and checkNoShopItem("Book of Sundering Surge") and not LookForItem("Book of Sundering Surge", inventory):
            "You found a skill book called '{i}Sundering Surge{/i}', maybe it can prove useful later on..."
            $ addItem("Book of Sundering Surge", inventory, 1)
    "You found [gold_drop] gold and [exp_drop] EXP."
    $ pc.exp += exp_drop
    $ pc.gold += gold_drop
    if pc.exp > pc.expCap and pc.level <= levelCap:
        $ pc.LevelUp()
        msg "You are now Level [pc.level]! Check your inventory to allocate your level points."

    if mimic_num == 1:
        $ nosferat_sprite1.death = True
        $ removeSprite(chelforte, nosferat_sprite1)
    if mimic_num == 2:
        $ nosferat_sprite2.death = True
        $ removeSprite(chelforte, nosferat_sprite2)
    if mimic_num == 3:
        $ nosferat_sprite3.death = True
        $ removeSprite(chelforte, nosferat_sprite3)
    scene black
    with dissolve
    pause 1.0
    jump Chelforte_Cavern_Loop

label nosferat_lose:
    hide screen dungeon_buttons
    hide screen dungeon_map
    "You fell on the ground, the nosferat slowly jogs towards you.."
    $ pc.cor -= 3
    call Scene_Nosferat_Lose from _call_Scene_Nosferat_Lose
    call lost_gold_check (0.05, 70, True) from _call_lost_gold_check_14
    $ pc.add_active_status(stuffed)

    scene black
    with dissolve
    pause 1.0

    call Leaving_Chelforte from _call_Leaving_Chelforte_3
    jump main_dark_forest

label werewolf_tetto_battle:

    $ status = None

    $ enemy_num = 2
    $ enemy = werewolf
    $ enemy2 = werewolf2
    $ enemy.max_hp = 550
    $ enemy.min_damage = 45
    $ enemy.max_damage = 60
    $ enemy.min_lust_damage = 16
    $ enemy.max_lust_damage = 22
    $ enemy.dodge = 2
    $ enemy.defense = 55
    $ enemy.lust_defense = 46
    $ enemy2.max_hp = 400
    $ enemy2.min_damage = 35
    $ enemy2.max_damage = 70
    $ enemy2.min_lust_damage = 10
    $ enemy2.max_lust_damage = 16
    $ enemy2.dodge = 2
    $ enemy2.defense = 75
    $ enemy2.lust_defense = 30
    $ enemy.exp_drop = 220
    $ enemy.beginbattle()
    $ enemy2.beginbattle()
    $ tetto_flirt = 0
    $ target = enemy
    $ ally = tetto
    $ ally_num = 2
    $ ally.beginbattle()
    call beginningBattle from _call_beginningBattle_25
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    hide screen dungeon_buttons
    scene dark_forest:
        blur 8
    if pc.weapon == None:
        "You are facing two werewolves, you are ready to fight them off alongside Tetto."
    else:
        "You are facing two werewolves, you hold out your [pc.weapon.name!t], you are ready to fight them off alongside Tetto."

    jump werewolf_tetto_battle_loop
label werewolf_tetto_battle_loop:
    if enemy.lust < enemy.max_lust / 3:
        show werewolf1:
            xalign 0.1
            yalign 0.4
    elif enemy.lust < enemy.max_lust / 3 * 2:
        show werewolf2:
            xalign 0.1
            yalign 0.4
    else:
        show werewolf3:
            xalign 0.1
            yalign 0.4
    if enemy2.lust < enemy.max_lust / 3:
        show werewolf1:
            xalign 0.9
            yalign 0.4
    elif enemy2.lust < enemy.max_lust / 3 * 2:
        show werewolf2:
            xalign 0.9
            yalign 0.4
    else:
        show werewolf3:
            xalign 0.9
            yalign 0.4

    if check_party(pc) == "lost" and check_party(ally) == "lost":
        call Battle_Finish from _call_Battle_Finish_81
        jump werewolf_tetto_lose

    if battleTurn == "Player":
        if check_party(pc) != "lost":
            "It's your turn now."
            $ turn_action = ui.interact()
        else:
            $ turn_action = "No"
    else:

        if check_party(ally) != "lost":
            "It's [ally.name]'s turn now."
            $ turn_action = ui.interact()
        else:
            $ turn_action = "No"

    call Battle_ASF from _call_Battle_ASF_23
    if oa[0] == "A":
        if oa[1] == "M":
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the arms of the werewolf, it slides right off his fluffy arm, while you look back in disbelief."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] at the arms of the werewolf, it slides right off his fluffy arm, while you look back in disbelief."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the arms of the werewolf, it pierces right through his soft fur without touching his skin, leaving you frozen in disbelief."
            if oa[3] == "N":
                "You hold your fist and throw it at the werewolf, but it hits nothing and leaves you standing instead."
            if renpy.random.random() > 0.5:
                ww "Unlucky. But not surprised, hmmm..."
            if renpy.random.random() > 0.5:
                tt "You will make it next time."
            "The werewolf growls loudly while flexing his claws, it almost seems he's scoffing at your attempt of attack."
        else:
            call Enemy_Damaging (target, oa[4]) from _call_Enemy_Damaging_22
            if battleTurn == "Ally":
                if oa[3] == "A":
                    if renpy.random.random() > 0.5:
                        "You slash your [pc.weapon.name!t] at the werewolf, your blade grazes through the werewolf's stomach. Drops of blood drips through his body."
                    else:
                        "You slash your [pc.weapon.name!t] at the werewolf, knocking him on the ground. He growls at you before getting up, albeit disheveled."
                if oa[3] == "B":
                    if renpy.random.random() > 0.5:
                        "You slam your [pc.weapon.name!t] at the werewolf, your blade grazes through the werewolf's stomach. Drops of blood drips through his body."
                    else:
                        "You slam your [pc.weapon.name!t] at the werewolf, knocking him on the ground. He growls at you before getting up, albeit disheveled."
                if oa[3] == "C":
                    if renpy.random.random() > 0.5:
                        "You aim and shoot your [pc.weapon.name!t] at the werewolf, the arrow hit right into his shoulder and he screams in agony."
                    else:
                        "You run while shooting your [pc.weapon.name!t] at the werewolf, knocking him on the ground. He growls at you before getting up, albeit disheveled."
                if oa[3] == "N":
                    if renpy.random.random() > 0.5:
                        "You throw your fist at the werewolf, hitting him right across his face, the sheer impact knocks him on the ground."
                    else:
                        "You punch into the werewolf's stomach, grabbing him and slam him on the ground hard."
            else:
                "Tetto slashes his claws into the werewolf, scraping against the long grey fur on his body."
            if oa[2] == "N":
                "His health decreases by [oa[4]] HP."
            else:
                "The werewolf is critically hit, his health decreased by [oa[4]] HP!"
            $ dia = renpy.random.random()
            if werewolf.hp >  werewolf.max_hp * 0.5:
                if dia < 0.3:
                    ww "Come here... little prey, stop resisting."
                elif dia < 0.6:
                    ww "Huh... This prey is definitely moving. And I'll prefer a moving one when I get a hold of you."
                "The werewolf howls in anger, you can feel the imminent danger as other werewolves in the forest respond to his howl."
            else:
                if dia < 0.3:
                    ww "Argh...! You can really pack a punch do you not? Can't wait to pin you down and get a taste of your flesh."
                elif dia < 0.6:
                    ww "Hnnngh!!! Now I'm getting real angry. And you don't want to see me when I'm angry, little prey."
                "You can barely hear barking sound of the werewolf, it seems like he doesn't appreciate a trespasser, and you've angered him further."

    if oa[0] == "A_T":
        $ dia = renpy.random.random()
        if dia > 0.5:
            tt "Take my claw!"
        else:
            tt "Hyaah! Leave it to me!"
        call Damaging (ally, target, oa[4]) from _call_Damaging_46
        "Tetto thrashes his claws at the werewolves, dealing [oa[4]] HP!"
        ww "F-fuck! We'll take you down in no time!"
        "The werewolf is now wounded."
    if oa[0] == "F":
        $ dia = renpy.random.random()
        if battleTurn == "Ally":
            if dia > 0.334:
                "You turn around and rub your hand all over your own burly cheeks, feeling and brushing against your ass while you shake your hip."
            elif dia > 0.667:
                "You scrape your member lightly, running your claw from your inner thigh to the back of your balls, you tug at it tightly while staring at the werewolf seductively."
            else:
                "You cup at your fluffy chest, drawing circles around the area of your nipples. You smile at the werewolf while your chest bounce up and down slightly."
        else:
            if tetto_flirt == 0:
                tt "What?"
                e "You know, do something sexy..."
                tt "W- Alright."
                $ tetto_flirt += 1
            "Tetto puffs up his chest, flaunting his red brown fur in front of the werewolf."

        if oa[1] == "M":
            if battleTurn == "Ally":
                "You continue your act for about a minute, but the werewolf just stares at you in confusion."
            else:
                "The werewolf just stares at Tetto... Eventually he stops out of embarrassment."
        else:
            if battleTurn == "Ally":
                if target.lust > target.max_lust / 2:
                    if renpy.random.random() > 0.5:
                        "Within a few seconds you can already see some movements under the werewolf's ripped pants."
                        "The sturdy beast man licks his lips, grumbling at your beautiful sight. His lust is increased by [player_flirt]."
                    else:
                        "You notice the werewolf is staring at your crotch, you slightly wink at him and he already looks like he can't breath under such arousal."
                        "His lust is increased by [player_flirt]."
                    $ dia = renpy.random.random()
                    if dia < 0.33:
                        ww "Hmm... Come closer... little prey."
                    elif dia < 0.66:
                        ww "You have a nice body, little prey. Our pack would be delighted to see you."
                else:
                    if renpy.random.random() > 0.5:
                        "The werewolf is squirming in reaction to your advance."
                        "You can already hear his rapid breathing and grunting, grasping at his own claws. His lust is increased by [player_flirt]."
                    else:
                        "You can tell the werewolf is already playing with himself when his claws goes under his pants, staring at your ass intently."
                        "His lust is increased by [player_flirt]."
                    $ dia = renpy.random.random()
                    if dia < 0.33:
                        ww "I-I can't hold... back- if you keep being like that."
                    elif dia < 0.66:
                        ww "L-little prey, y-our hole is mine. Now give up already and let me... f-fuck."
            else:
                "You can see that for some reason, the werewolf is weirdly attracted by Tetto's performance."
                ww "Hmmph...."
                "His lust is increased by [player_flirt]."

    if oa[0] == "E":
        $ battleTurn = "Player"
        $ AbilityTab = False
        $ ItemTab = False
        "You look around, there's no way to escape without abandoning Tetto, and you're not ready for that."
        jump werewolf_tetto_battle_loop
    if oa[0] == "U":
        "You raises your hand. Showing to the werewolves that you've accepted your fate."
        tt "We can still win this... right? [e]?"
        "You remain silent as Tetto lowers his arms, staring at the two werewolves in defeat."
        tt "...I cannot fight them all by myself."
        call Battle_Finish from _call_Battle_Finish_82
        jump werewolf_tetto_lose
    call Ability_Item from _call_Ability_Item_24

    call Battle_Mid_Check from _call_Battle_Mid_Check_22
    if oa[0] == "W":
        call Battle_Finish from _call_Battle_Finish_83
        jump werewolf_tetto_win
    if oa[0] == "T":
        call Battle_End_Check from _call_Battle_End_Check_48
        jump werewolf_tetto_battle_loop

    if battleTurn == "Ally":
        if check_party(werewolf) != "lost":
            $ eny = werewolf
            show werewolf:
                linear 0.1 zoom 1.04
                linear 0.05 zoom 1
        else:
            $ target = enemy2
            $ eny = werewolf2
            show werewolf2:
                linear 0.1 zoom 1.04
                linear 0.05 zoom 1
    else:
        if check_party(werewolf2) != "lost":
            $ eny = werewolf2
            show werewolf2:
                linear 0.1 zoom 1.04
                linear 0.05 zoom 1
        else:
            $ target = enemy
            $ eny = werewolf
            show werewolf:
                linear 0.1 zoom 1.04
                linear 0.05 zoom 1
    if check_party(enemy) == "lost" and target == enemy:
        $ target = enemy2
    if check_party(enemy2) == "lost" and target == enemy2:
        $ target = enemy
    $ dia = renpy.random.random()
    $ ttg = renpy.random.choice([pc, ally])

    if dia < 0.45:
        if renpy.random.random()*100 > pc.dodge+extra_dodge:
            $ raw_damage = int(renpy.random.randint(eny.min_damage, eny.max_damage))
            $ enemy_damage = damageFormula(raw_damage, ttg.defense)
            call Damaging (enemy, ttg, enemy_damage) from _call_Damaging_47

            if ttg.hp < 0:
                $ ttg.hp = 0
            $ random_chance = renpy.random.random()
            if ttg == pc:
                if random_chance < 0.5:
                    "The werewolf flaunts his claw towards you. Your health decreases by [enemy_damage] HP."
                else:
                    "The werewolf charges at you, knocking you on the ground. Your health decreases by [enemy_damage] HP."
            else:
                if random_chance < 0.5:
                    "The werewolf flaunts his claw towards Tetto. His health decreases by [enemy_damage] HP."
                else:
                    "The werewolf charges at Tetto, clashing his body onto the ground. His health decreases by [enemy_damage] HP."
        else:
            $ random_chance = renpy.random.random()
            if ttg == pc:
                if random_chance < 0.5:
                    "The werewolf flaunts his claw towards you, you manage to dodge the attack."
                else:
                    "The werewolf charges at you, trying to kick at your chest but you leap to your side in time."
            else:
                if random_chance < 0.5:
                    "The werewolf flaunts his claw towards Tetto, but he manage to dodge the attack."
                else:
                    "The werewolf charges at Tetto, trying to push him on the ground, but he leaps away in time."
        $ rand = renpy.random.random()
        if ttg.hp > ttg.max_hp/2:
            if rand > 0.5:
                if ttg == pc:
                    ww "Heh... little prey. Give up now and maybe we'll give you and your friends a quick death."
                if ttg == ally:
                    ww "Tetto, we knew you're one of the weaklings, but we didn't expect such cowardice in you."
        else:
            if rand > 0.5:
                if ttg == pc:
                    ww "I'm almost done with you, little prey. Uffe will be elated to see your demise."
                if ttg == ally:
                    ww "It's time, my friend, you know we can't let you escape, so why not make this quick?"
    else:
        $ raw_damage = int(renpy.random.randint(eny.min_damage, eny.max_damage))
        $ enemy_damage = damageFormula(raw_damage, ttg.defense)
        call Damaging (eny, ttg, enemy_damage) from _call_Damaging_48
        if ttg.hp < 0:
            $ ttg.hp = 0

        if ttg == pc:
            "The werewolf swings his claw at you, scraping against your side. Your health decreases by [enemy_damage] HP."
            $ ttg_status = status
        else:
            "The werewolf swings his claw at Tetto, scraping against his side. His health decreases by [enemy_damage] HP."
            $ ttg_status = ally.status
        $ isWounded = next((x for x in ttg_status if x.img == "Wounded"), None)
        if isWounded != None:
            $ isWounded.rounds += 3
            if ttg == pc:
                "Your bleeding has gotten worse from the werewolf."
            else:
                "Tetto is bleeding much worse now."
        else:
            $ ApplyStatus(ttg_status, wounded, 3)
            if ttg == pc:
                "You begin to bleed from your wound as the werewolf watches in jeer."
            else:
                "Tetto begins to bleed from the newly-formed wound clawed by the werewolf."



    call Battle_End_Check from _call_Battle_End_Check_49
    jump werewolf_tetto_battle_loop
label werewolf_tetto_win:
    hide werewolf
    hide werewolf2
    $ werewolf.win += 1
    scene black with dissolve
    "You pant heavily as both werewolves falls on the ground."
    "Without hesitation, you turn around to leave, only to see Tetto still staring at the werewolves."
    ww "F-fuck. Uffe is going to kill us for letting you two go."
    ww2 "Ugh..."
    scene dark_forest with dissolve
    tt "You can leave with us, escape the forest. Uffe can't reach you outside."
    "You are quite honestly stunned by how quickly Tetto invites them to tag along, considering 10 seconds ago you were fighting to death."
    "The two defeated werewolves look at each other."
    pause 2
    "Without another words, they staggers away from you two, towards the path you two took."
    "It's clear the decision they've made was grim, but understandable."
    ww2 "We didn't see anything."
    "As they walk, the two turns to you and Tetto as they support each other's weights."
    "They slightly nods at you, eyes with a sorrowful look, before slowly disappearing into the mist."
    pause 1
    tt "Shall we continue? It's almost there."
    "You nod."
    "The maned werewolf picks up his brother, who's still in deep slumber."
    "His step falters, but he manages to keep his balance despite the wounds and injuries."
    tt "Say, [e]. You need to recommend me that lizard of yours, he's got a good recipe for an ointment, right?"
    e "Yeah, I think so."
    tt "Good, I can use a whole jar right now."
    "Tetto smiles."
    "It's clear Tetto has less of a mood to talk right now, considering what has panned out in the fight."
    "And you decide to stay quiet as well, just to let your thought sinks in."
    scene black with dissolve
    pause 3 
    scene dark_forest with dissolve




    tt "What do you think the outside world has for us? Will it be good? Or the same."
    "After a while, the werewolf speaks once more."
    e "I believe you will meet so much more people outside, there will be bad things within, but you'll also discover something good, something worthwhile."
    tt "Good is good enough."
    "Tetto takes another step, before he comes to a halt."
    e "We're out of the forest now."
    "You look around, hearing the splurging sound of water, you three seem to be near the cascades now."
    tt "Oh my- Everything is so bright here."
    e "Yeah!"
    scene sundersilkcascades with dissolve
    "Tetto walks around in awe as he lays down his sleeping brother."
    e "You sure you two are fine here? There are still monsters around, even though they're not as vicious as your people."
    tt "Well, we're werewolves too!"
    "He chides loudly, with a friendly smile."
    tt "Rumma is almost awake here, we'll be okay."
    tt "However, we still want to get away as far as possible from Uffe, for now."
    "The werewolf grins."
    e "I'm so glad to be able to help you."
    "He turns to you, this time with a warm glance."
    tt "And I'm glad you turned around, from Uffe."
    e "Huh?"
    tt "I just deduced that you had some tasks given by the alpha, from how those two in the forest spoke."
    tt "But regardless, you defied his order just to help strangers like us. That just makes me admire you more, little friend."
    "Tetto gives you a warm embrace, covering you easily in his red brown fur."
    "You don't know how to respond, you felt as if you've betrayed Tetto's trust, but somehow, he's grown to like you more."
    tt "You helped treat Rumma's wound, and you escaped with us. That'll spell you a lot of troubles from Uffe."
    tt "Don't ever get near the den, and remember to conceal your smell around if you decide to go back."
    if quest26.status == True:
        e "Actually, I've had help from Wuldon, he's just like you two, very good at hiding."
        tt "W-wuldon? The herbalist's son?"
        e "Huh?"
        tt "I've seen that big blue werewolf before, but it's been so long."
        tt "What is he up to?"
        e "Well, a few things. Maybe after everything, you'll be able to return to the forest whenever you'd like."
        tt "Hah, well, don't get my hopes up like that."
    else:
        e "I- I know."
        tt "Well, I've seen a big blue werewolf carrying water around the split trails, perhaps you should go visit him sometimes."
        if wuldon_meet:
            e "I think I know him, we talked quite a lot about the pack's history."
            tt "That's great, he was the herbalist's son, actually. So I suppose he can get you around the forest easily."
        else:
            e "Where can I find him?"
            tt "Through some sort of riddle in the split trails, I think he definitely has his genius method of concealing his location, unlike us."
            "Tetto smiles."
    tt "Oh, and speaking of the herbalist, there's something that I want to give you."
    "The werewolf takes out a pair of old gloves, and put them on your hand."
    tt "Here, it was the herbalist's gloves, he gave it to me the last time I saw him. It should help you pick up some herbs very easily."
    e "Thank you, Tetto."
    tt "Anyway, my brother is still sleeping like a baby now. His wound's recovered, I should make a bed around here soon."
    e "I guess we'll split here."
    tt "Yep. May we meet again, [e]."
    e "Take care, Tetto."
    "Tetto raises his hand to wave you goodbye as you leave."
    $ QuestFinish(quest36)
    $ addItem("Herbalists Gloves", inventory, 1)
    jump main_sundersilk_cascades

label werewolf_tetto_lose:
    hide werewolf1
    hide werewolf2
    scene black
    "The werewolves jeer, instead of the usual banters, you see actual bloodlust in their eyes."
    "And soon you realise, it's the end of the journey."
    menu:
        "Continue to your End":
            pass
        "Back to Main Menu":
            $ MainMenu(confirm=False)()


    "Without another second thought, the werewolf in front of you swings his claws one last time, hitting across your face."
    "He doesn't spare any energy left, just letting his claws bury inside your head for just the mere tenth of a seconds it collides."
    "It was quicker than you thought, perhaps it was his unique method of showing mercy, your vision goes dark immediately."
    "You can hear Tetto gasps surprisingly as your body goes limp, and you slump on the ground hard, before he's taken away by the two werewolves."
    tt "G-get off me! You monsters."
    "The sound of Tetto being dragged away are faintly heard, but the majority of the senses goes to the pain from your crushed head."
    "Soon, you hear his brother is dragged away as well, leaving you alone on the forest floor."
    "You take your last breath before everything comes to a halt."
    menu:
        "You died. Reload an old save to continue your journey."
        "Back to Main Menu":
            $ MainMenu(confirm=False)()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
