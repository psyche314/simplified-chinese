label werewolf_battle:

    $ status = None
    show werewolf1:
        xalign 0.5
        yalign 0.4
    $ enemy_num = 1
    $ enemy = werewolf
    $ enemy.max_hp = 350
    $ enemy.min_damage = 35
    $ enemy.max_damage = 50
    $ enemy.min_lust_damage = 10
    $ enemy.max_lust_damage = 22
    $ enemy.dodge = 2
    $ enemy.defense = 45
    $ enemy.lust_defense = 26
    $ enemy.exp_drop = 220

    $ enemy_image = "werewolf e1"
    $ werewolf.beginbattle()
    call beginningBattle from _call_beginningBattle_5
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    hide screen dungeon_buttons
    scene dark_forest:
        blur 8
    "You are facing a wild werewolf, he extends his claws, staring at you with a mix of lust and innate hunger."
    ww "...Come here, little prey."

    jump general_battle_loop

label werewolf_battle_loop(acting_enemy=enemy):
    if acting_enemy == enemy:
        if enemy_num == 2:
            $ werewolf_image_xalign = 0.1
        else:
            $ werewolf_image_xalign = acting_enemy.item_chance01
        if acting_enemy.lust < acting_enemy.max_lust / 3:
            $ enemy_image = "werewolf e1"
        elif acting_enemy.lust < acting_enemy.max_lust / 3 * 2:
            $ enemy_image = "werewolf e2"
        else:
            $ enemy_image = "werewolf e3"
        show expression enemy_image:
            xalign werewolf_image_xalign
            yalign 0.4
    else:
        if acting_enemy.lust < acting_enemy.max_lust / 3:
            $ enemy2_image = "werewolf e1"
        elif acting_enemy.lust < acting_enemy.max_lust / 3 * 2:
            $ enemy2_image = "werewolf e2"
        else:
            $ enemy2_image = "werewolf e3"
        show expression enemy2_image:
            xalign 0.9
            yalign 0.4

    $ dia = renpy.random.random()
    if dia < 0.4:
        if renpy.random.random()*100 > pc.dodge+extra_dodge:
            $ raw_damage = int(renpy.random.randint(acting_enemy.min_damage, acting_enemy.max_damage))
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_5
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The werewolf flaunts his claw towards you. Your health decreases by [enemy_damage] HP."
            else:
                "The werewolf charges at you, knocking you on the ground. Your health decreases by [enemy_damage] HP."
        else:
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The werewolf flaunts his claw towards you, you manage to dodge the attack."
            else:
                "The werewolf charges at you, trying to kick at your chest but you leap to your side in time."
        $ rand = renpy.random.random()
        if pc.hp > pc.max_hp/2:
            if rand > 0.5:
                ww "Heh... little prey. Give up now and maybe I'll consider not messing up your body."
        else:
            if rand > 0.5:
                ww "I'm almost done with you, little prey. After this I'll have my way with you however I want."
    elif dia < 0.8:
        $ raw_damage = int(renpy.random.randint(acting_enemy.min_damage, acting_enemy.max_damage))
        $ enemy_damage = damageFormula(raw_damage, pc.defense)
        call Damaging (enemy, pc, enemy_damage) from _call_Damaging_6
        "The werewolf swings his claw at you, scraping against your side. Your health decreases by [enemy_damage] HP."
        if wounded not in status:
            $ wounded.max_rounds = 3
            $ wounded.rounds = wounded.max_rounds
            $ status.append(wounded)
            "You begin bleeding from your wound."
            ww "Heh... little prey. Now I just have to wait until you bleed to your demise."
        else:
            $ wounded.rounds += wounded.max_rounds
            "Your bleeding has gotten worse from the werewolf."
    else:
        $ random_chance = renpy.random.random()
        if random_chance < 0.5:
            "The werewolf scratches at his pants, he runs two fingers along the shape of his cock in front of you."
            ww "Look at this, this is all you want. You want this to fill you up don't you."
        else:
            "The werewolf stretches his body, flaunting his muscular physiques, you can tell his soft is almost bulging in front of you."
            ww "Come, little prey. You are all thirsting over my perfect muscles."
        if renpy.random.random()*100 > pc.lust_dodge + extra_lust_dodge:
            $ raw_flirt = int(renpy.random.randint(acting_enemy.min_lust_damage, acting_enemy.max_lust_damage))
            $ enemy_flirt = damageFormula(raw_flirt, pc.lust_defense)
            $ pc.lust += enemy_flirt
            if pc.lust > pc.max_lust:
                $ pc.lust = pc.max_lust
            if dia > 0.9:
                "You gulp at the werewolf's attempt at seduction. Admittedly you are extremely aroused, thinking about how his cock would taste like."
                "Your lust increased by [enemy_flirt]."
            else:
                "You are stunned by his gorgeous muscles, you mind wanders through scenarios of him being inside your body."
                "Your lust increased by [enemy_flirt]."
        else:
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "You stare at him, giving him weird side eyes. You have evaded his attempt at seduction. And the werewolf seems to feel a little dejected."
                ww "...Really...? Nothing at all?"
            else:
                "His attack at your lust seems to have failed as you stand there and wait for him to finish his taunt."
                "Both of you would never speak about it again."
                ww "Come on... closing your eyes doesn't count..."
    call Battle_End_Check from _call_Battle_End_Check_11

    if enemy_num == 2:
        return
    jump general_battle_loop
label werewolf_win:
    hide expression enemy_image
    hide werewolf1
    hide werewolf2
    hide werewolf3
    $ werewolf.win += 1
    call Battle_Finish from _call_Battle_Finish_34
    $ exp_drop = renpy.random.randint(200, 260)
    if equippedTrinket("Lindbloom"):
        $ rnd = 0.8
    else:
        $ rnd = 0.4
    "The werewolf is lying on the floor, still panting..."
    if werewolf.win >= 1 and werewolf.lust > 50:
        menu:
            "Do you want to... have fun with the werewolf?"
            "Yes{#fuckwerewolf}":
                "..."
                call scene_werewolf_win from _call_scene_werewolf_win
                $ pc.lust = 0
            "No{#fuckwerewolf}":
                pass
    if renpy.random.random() <= rnd:
        "As you search around the werewolf, you found an Iron ore, a Pelt and [exp_drop] EXP!"
        $ addItem("Iron Ingot", inventory, 1)
        $ addItem("Pelt", inventory, 1)
    else:
        "As you search around the werewolf, you found a Pelt and [exp_drop] EXP!"
        $ addItem("Pelt", inventory, 1)
    if got_huntertrousers == 0 and renpy.random.random() < rnd:
        $ got_huntertrousers = 1
        "You also found a pair of trousers... from a Hunter."
        $ addItem("Hunter Trousers", inventory, 1)
    elif checkNoShopItem("Copper Pickaxe") and renpy.random.random() < rnd:
        "You also found an old copper pickaxe."
        $ addItem("Copper Pickaxe", inventory, 1)

    $ pc.exp += exp_drop
    $ found_gold = renpy.random.randint(25, 41)
    "You also found [found_gold] gold from the werewolf. You pick them up swiftly."
    $ pc.gold += found_gold
    "You leave the werewolf alone in the forest, he will probably wake up a few hours later."
    if pc.exp > pc.expCap and pc.level <= levelCap:
        $ pc.LevelUp()
        msg "You are now Level [pc.level]! Check your inventory to allocate your level points."

    if isinstance(current_location, MapPat) and current_location.img == "Forest Nightwatch":
        if mimic_num == 1:
            $ werewolfD[0] = 1
            $ dark_forest1.unoccupy(werewolf_sprite.x, werewolf_sprite.y)
        elif mimic_num == 2:
            $ werewolfD[1] = 1
            $ dark_forest1.unoccupy(werewolf_sprite1.x, werewolf_sprite1.y)
        elif mimic_num == 3:
            $ werewolfD[2] = 1
            $ dark_forest1.unoccupy(werewolf_sprite2.x, werewolf_sprite2.y)
        elif mimic_num == 4:
            $ werewolfD[3] = 1
            $ dark_forest1.unoccupy(werewolf_sprite3.x, werewolf_sprite3.y)
        elif mimic_num == 6:
            "The Werewolf falls right onto his mat... he's sleeping for a while this time."
            $ sleeping_wolf = 1
        jump Dark_Forest1_Loop
    elif isinstance(current_location, MapPat) and current_location.img == "Split Trail":
        if mimic_num == 7:
            $ werewolfDa[0] = 1
            $ split_trail.unoccupy(werewolf_sprite_a1.x, werewolf_sprite_a1.y)
        elif mimic_num == 8:
            $ werewolfDa[1] = 1
            $ split_trail.unoccupy(werewolf_sprite_a2.x, werewolf_sprite_a2.y)
        jump Split_Trail_Loop

    jump main_dark_forest

label werewolf_lose:
    hide expression enemy_image
    hide werewolf1
    hide werewolf2
    hide werewolf3
    call Battle_Finish from _call_Battle_Finish_35
    if pc.hp <= 0:
        "You struggle against the werewolf, you have already exhausted all your energy. He pounces on your helpless body like you are a feast to be served."
    if pc.lust >= pc.max_lust:
        "You struggle against the werewolf, your mind is filled with unquenchable lust over the werewolf. He pounces on your helpless body like you are a feast to be served."
    if tetto_escaped and quest36.status == True:
        "But, instead of searching around your body, he just knocks you out in one mere punch, you fall unconscious soon as the werewolf brings you somewhere else."
        ww "Uffe's gotta love this one, heh."
        pause 2
        "As you wake up, a familiar face greets you from above, someone that you know, but never wants to meet again."
        jump BadEnd_Werewolf_Capture
    "..."

    $ werewolf.lose += 1
    if werewolf.lose > 1:
        menu:
            "Do you want to replay the losing scene?"
            "Yes{#werewolffuck}":
                call scene_werewolf_lose from _call_scene_werewolf_lose
            "No{#werewolffuck}":
                pass
    else:
        call scene_werewolf_lose from _call_scene_werewolf_lose_1
    call lost_gold_check (0.07, 40, True) from _call_lost_gold_check_10
    $ pc.add_active_status(stuffed)
    if hasattr(current_location, "name") and current_location.name == "Forest Nightwatch":
        $ dark_forest1.unoccupy(tenki_sprite3.x, tenki_sprite3.y)
        $ dark_forest1.unoccupy(werewolf_sprite.x, werewolf_sprite.y)
        $ dark_forest1.unoccupy(werewolf_sprite2.x, werewolf_sprite2.y)
        $ dark_forest1.unoccupy(werewolf_sprite1.x, werewolf_sprite1.y)
        $ dark_forest1.unoccupy(werewolf_sprite3.x, werewolf_sprite3.y)
        $ dark_forest1.unoccupy(barrel_sprite1.x, barrel_sprite1.y)
        $ dark_forest1.unoccupy(barrel_sprite2.x, barrel_sprite2.y)
        $ dark_forest1.unoccupyback(wooddoor_sprite2.x, wooddoor_sprite2.y)

        jump main_dark_forest
    show screen menu_buttons
    jump main_dark_forest

label scarecrow_battle:


    $ enemy_num = 1
    $ enemy = scarecrow
    $ enemy.max_hp = 410
    $ enemy.min_damage = 25
    $ enemy.max_damage = 40
    $ enemy.min_lust_damage = 10
    $ enemy.max_lust_damage = 22
    $ enemy.dodge = 2
    $ enemy.defense = 30
    $ enemy.lust_defense = 20
    $ enemy.exp_drop = 220
    call beginningBattle from _call_beginningBattle_14
    $ scarecrow.beginbattle()
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons

    if current_location.name == "Summery Farmland":
        scene summery_farmland:
            blur 8
    else:
        scene grove_of_harvest:
            blur 8
    show scarecrow:
        xalign 0.5
        yalign 0.75
    if pc.weapon == None:
        "You raise your fist against the scarecrow, it seems to be standing in solitude, only turning back at you in confusion."
    else:
        "You raise your [pc.weapon.name!t] against the scarecrow, it seems to be standing in solitude, only turning back at you in confusion."
    jump scarecrow_battle_loop

label scarecrow_battle_loop:
    show scarecrow:
        xalign 0.5
        yalign 0.75
    if check_party(pc) == "lost":
        call Battle_Finish from _call_Battle_Finish_37
        jump scarecrow_lose
    $ turn_action = ui.interact()
    call Battle_ASF from _call_Battle_ASF_12
    if oa[0] == "A":
        if oa[1] == "M":
            if oa[3] == "A" or oa[3] == "B":
                "You aim and slash your [pc.weapon.name!t] at the scarecrow, but you simply miss him by inches."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the scarecrow, but you simply miss him by inches."
            if oa[3] == "N":
                "You throw your fist at the scarecrow, but you simply miss him by inches."
        else:
            call Enemy_Damaging (target, oa[4]) from _call_Enemy_Damaging_1
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the scarecrow, your blade grazes through the cloth on his body."
                "You hear a tearing sound as some cotton falls."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] at the scarecrow, knocking him sideway."
                "He stands there unfazed, albeit disheveled."
            if oa[3] == "C":
                "You run while shooting your [pc.weapon.name!t] at the scarecrow, knocking him sideway."
                "He stands there unfazed, albeit disheveled."
            if oa[3] == "N":
                "You punch into the scarecrow's stomach for multiple times."
            if oa[2] == "N":
                "His health decreases by [oa[4]] HP."
            else:
                "You've critically hit the scarecrow, dealing [oa[4]] HP!"
    if oa[0] == "S":
        "You struggle against the scarecrow, trying to break free."
        "You dealt [player_damage] damage to the scarecrow in the process, his grip has loosen as well."
    if oa[0] == "F":
        "As much as you try to grind your hips against the scarecrow, he doesn't flinch, or get aroused."
        "It doesn't seem that he is affected by your flirt...."
        "You back off before he tries to grab a hold of your body."
    if oa[0] == "E":
        if oa[1] == "M":
            "You slowly back down from the scarecrow's attack, you turn around and run as fast as you can."
            "The scarecrow catches you with his arms and flings your body right back to him. Your escape seems to have failed!"
        else:
            "You slowly back down from the scarecrow's attack, you turn around and run as fast as you can."
            "The scarecrow tries to catch you with his arms but it barely slips from your body, You successfully escaped from the scarecrow!"
            hide screen battle_buttons
            hide screen battle_enemy_stat
            hide screen battle_player_stat
            jump main_summery_farmland
    if oa[0] == "U":
        "You fall to your knees, exhausted all your energy, you grasp for breath as you lie on the ground, surrendering yourself to the scarecrow."
        "The scarecrow looks at you... it's still looking at you unfazed, except the head tilt..."
        call Battle_Finish from _call_Battle_Finish_38
        jump scarecrow_lose
    call Ability_Item from _call_Ability_Item_14

    call Battle_Mid_Check from _call_Battle_Mid_Check_12
    if oa[0] == "W":
        call Battle_Finish from _call_Battle_Finish_39
        jump scarecrow_win
    if oa[0] == "T":
        call Battle_End_Check from _call_Battle_End_Check_28
        jump scarecrow_battle_loop
    show scarecrow:
        linear 0.1 zoom 1.04
        linear 0.05 zoom 1
    if scarecrow.hp > 0 or scarecrow.lust == scarecrow.max_lust:
        if check_party(scarecrow) == "lost":
            call Battle_Finish from _call_Battle_Finish_40
            jump scarecrow_win
        $ dia = renpy.random.random()
        if dia < 0.50:
            if renpy.random.random()*100 > pc.dodge+extra_dodge:
                $ raw_damage = int(renpy.random.randint(scarecrow.min_damage, scarecrow.max_damage))
                $ enemy_damage = damageFormula(raw_damage, pc.defense)
                call Damaging (enemy, pc, enemy_damage) from _call_Damaging_7
                $ random_chance = renpy.random.random()
                if random_chance < 0.5:
                    "The scarecrow flings his arm towards you, you are not quick enough to dodge his blow. Your health decreases by [enemy_damage] HP."
                else:
                    "The scarecrow scrapes at your skin with his metal claws. Your health decreases by [enemy_damage] HP."
            else:
                $ random_chance = renpy.random.random()
                if random_chance < 0.5:
                    "The scarecrow flings his arm towards you, but you manage to dodge the attack."
                else:
                    "The scarecrow tries to catch you with his metal claws, but he misses it by inches."
        elif dia < 0.67 and bound not in status:
            "The scarecrow wraps your arm in his embrace..."
            "He is holding you in place."
            $ status.append(bound)
            $ grip_strength = bound.effect
        elif dia < 0.83 and enemy.hp < enemy.max_hp / 2:
            $ enemy.defense += 5
            $ heal_amount = 60
            call Enemy_Self_Healing (enemy, heal_amount) from _call_Enemy_Self_Healing_1
            "The scarecrow puffs up his stuffing, increasing his defense for the rest of the battle."
        else:
            $ enemy.max_hp += 80
            "The scarecrow expands, increasing his maximum health by 80 for the rest of the battle."
        call Battle_End_Check from _call_Battle_End_Check_29
    jump scarecrow_battle_loop
label scarecrow_win:
    "As you defeat the scarecrow, it soon collapses..."
    "It seems like it's not completely dead..."
    "You searches around the scarecrow, you found a loose button."
    $ addItem("Loose Button", inventory, 1)
    $ gold_drop = renpy.random.randint(24, 40)
    $ exp_drop = renpy.random.randint(160, 200)
    "You found [gold_drop] gold and [exp_drop] EXP."
    $ pc.exp += exp_drop
    $ pc.gold += gold_drop
    if pc.exp > pc.expCap and pc.level <= levelCap:
        $ pc.LevelUp()
        msg "You are now Level [pc.level]! Check your inventory to allocate your level points."
    scene black
    with dissolve
    pause 1.0
    if current_location.name == "Summery Farmland":

        jump main_summery_farmland
    else:
        jump main_grove_of_harvest
label scarecrow_lose:

    hide screen dungeon_buttons
    hide screen dungeon_map
    "You fell on the ground, the scarecrow is slowly approaching you."
    "It stops in front of you, just barely touching you with his claws, he carries you out of the farmland."
    "You lost 0 gold."
    scene black
    with dissolve
    pause 1.0
    "The scarecrow drops you off right outside the farm, and then continues its patrol around the farm."
    jump main_lusterfield_range

label landshark_battle:


    $ enemy_num = 1
    $ enemy = landshark
    $ enemy.max_hp = 410
    $ enemy.min_damage = 45
    $ enemy.max_damage = 60
    $ enemy.min_lust_damage = 10
    $ enemy.max_lust_damage = 22
    $ enemy.dodge = 2
    $ enemy.defense = 50
    $ enemy.lust_defense = 20
    $ enemy.exp_drop = 220
    $ buffed_attack = 0
    $ landshark.beginbattle()
    call beginningBattle from _call_beginningBattle_16
    hide screen dungeon_map
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    scene summery_farmland:
        blur 8
    show landshark:
        xalign 0.5
        yalign 0.25
    if pc.weapon == None:
        "You are facing a landshark, it burrows around the ground. You raise your fist in defence."
    else:
        "You are facing a landshark, it burrows around the ground. You raise your [pc.weapon.name!t] in defence."
    jump landshark_battle_loop
label landshark_battle_loop:
    show landshark:
        xalign 0.5
        yalign 0.25
    if check_party(pc) == "lost":
        call Battle_Finish from _call_Battle_Finish_41
        jump landshark_lose
    $ turn_action = ui.interact()
    call Battle_ASF from _call_Battle_ASF_14
    if oa[0] == "A":
        if oa[1] == "M":
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the fin of the landshark, but you simply missed him by inches."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] at the landshark's head, but you simply missed him by inches."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the landshark, but you simply missed him by inches."
            if oa[3] == "N":
                "You throw your fist at the landshark, but you simply missed him by inches."
        elif buffed_attack == 1:
            "You can't aim at the landshark, it's burrowing underground..."
            jump landshark_battle_loop
        else:
            call Enemy_Damaging (target, oa[4]) from _call_Enemy_Damaging_2
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the fin of the landshark, causing a bruises on his skin."
                "He roars at you, albeit disheveled."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] at the landshark's head, knocking him on the ground."
                "He roars at you, albeit disheveled."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the landshark, the arrow hit right around his fin."
            if oa[3] == "N":
                "You throw your fist at the landshark, hitting him right across the side."
            if oa[2] == "N":
                "His health decreases by [oa[4]] HP."
            else:
                "You've critically hit the landshark, dealing [oa[4]] HP!"
    if oa[0] == "F":
        "As much as you move your hip and grind your ass against the landshark, it doesn't seem to flinch."
        "You eventually give up before he can actually latch onto you."
    if oa[0] == "E":
        if oa[1] == "M":
            "You slowly back down from the landshark's attack, you turn around and run as fast as you can."
            "Suddenly you slip and fall on the ground! Your escape has failed."
        else:
            "You slowly back down from the landshark's attack, you turn around and run as fast as you can."
            "The landshark tries to slither after you but he is too slow, You successfully escaped from the landshark!"
            hide screen battle_buttons
            hide screen battle_enemy_stat
            hide screen battle_player_stat
            show screen dungeon_buttons
            jump main_summery_farmland
    if oa[0] == "U":
        "You fall to your knees, exhausted all your energy, you grasp for breath as you lie on the ground, surrendering yourself to the landshark."
        call Battle_Finish from _call_Battle_Finish_42
        jump landshark_lose
    call Ability_Item from _call_Ability_Item_16

    call Battle_Mid_Check from _call_Battle_Mid_Check_14
    if oa[0] == "W":
        call Battle_Finish from _call_Battle_Finish_43
        jump landshark_win
    if oa[0] == "T":
        call Battle_End_Check from _call_Battle_End_Check_32
        jump landshark_battle_loop
    show landshark:
        linear 0.1 zoom 1.04
        linear 0.05 zoom 1
    $ dia = renpy.random.random()
    if buffed_attack == 1:
        $ buffed_attack = 0
        $ raw_damage = int(renpy.random.randint(landshark.min_damage, landshark.max_damage)) * 2
        $ enemy_damage = damageFormula(raw_damage, pc.defense)
        call Damaging (enemy, pc, enemy_damage) from _call_Damaging_8
        "The landshark jumps up from below and strikes on your body, he draining [enemy_damage] HP from you."
        call Enemy_Self_Healing (landshark, int(enemy_damage / 1.5)) from _call_Enemy_Self_Healing_2

    elif dia < 0.50:
        if renpy.random.random()*100 > pc.dodge+extra_dodge:
            $ raw_damage = int(renpy.random.randint(landshark.min_damage, landshark.max_damage))
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_9
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The landshark swings his left fin towards you, you are not quick enough to dodge his blow. Your health decreases by [enemy_damage] HP."
            else:
                "The landshark dives at you, hitting you with a strong bite. Your health decreases by [enemy_damage] HP."
        else:
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The landshark swings his left fin towards you, but you managed to deflect his attack."
            else:
                "The landshark charges at you, trying to feast on you but you block the blow and push him away."
    elif dia < 0.83 and buffed_attack == 0:
        $ buffed_attack = 1
        "The landshark dives under the soil... seems like his next attack can be dangerous."
    else:
        "The landshark roars, and reduces your MP by 20."
        $ pc.mp -= 20
        if pc.mp < 0:
            $ pc.mp = 0

    call Battle_End_Check from _call_Battle_End_Check_33
    jump landshark_battle_loop
label landshark_win:

    "As you defeat the landshark, it begins to collapse and fall into a spiral underground..."
    "There's nothing useful for now..."
    $ gold_drop = renpy.random.randint(13, 23)
    $ pc.gold += gold_drop
    $ landshark.win += 1
    $ exp_drop = renpy.random.randint(150, 190)
    "You found [gold_drop] gold and [exp_drop] EXP."
    if equippedTrinket("Lindbloom"):
        $ rnd = 0.8
    else:
        $ rnd = 0.1
    if renpy.random.random() < rnd:
        if checkNoShopItem("Knight Longsword"):
            $ addItem("Knight Longsword", inventory, 1)
            "You pick up a longsword from the where the landshark lands, it seems almost brand new."
        else:
            "You pick up a piece of clay..."
            $ addItem("Clay", inventory, 1)

    $ pc.exp += exp_drop
    if pc.exp > pc.expCap and pc.level <= levelCap:
        $ pc.LevelUp()
        msg "You are now Level [pc.level]! Check your inventory to allocate your level points."

    scene black
    with dissolve
    pause 1.0
    jump main_summery_farmland
label landshark_lose:
    "The landshark swims around you, it seems to be ready to feast on you... but he didn't..."
    "He dives right before the scarecrow in the farm spots him."
    $ gold_lost = int(30 + renpy.random.random()*0.3*pc.gold)
    $ pc.gold -= gold_lost
    if pc.gold < 0:
        $ pc.gold = 0
    if pc.hp <= 0:
        $ pc.hp = 1
    "You lost [gold_lost] gold."
    scene black
    with dissolve
    jump main_summery_farmland
label ratbandit_battle:



    $ enemy_num = 1
    $ enemy = ratbandit
    $ enemy.max_hp = 600
    $ enemy.min_damage = 55
    $ enemy.max_damage = 72
    $ enemy.defense = 60
    $ enemy.min_lust_damage = 20
    $ enemy.max_lust_damage = 25
    $ enemy.dodge = 75
    $ enemy.lust_defense = 50
    $ enemy.exp_drop = 260
    $ ratbandit.beginbattle()
    call beginningBattle from _call_beginningBattle_22
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    $ bandit_escaping = False
    $ bandit_rat_critical = False

    scene grove_of_harvest:
        blur 8
    show rat bandit:
        xalign 0.5
        yalign 0.7
    if pc.weapon == None:
        "You are facing a rat bandit in the field, it's hard to catch him in the middle of the tall grasses. You hold and clench your fist."
    else:

        "You are facing a rat bandit in the field, it's hard to catch him in the middle of the tall grasses. You hold your [pc.weapon.name!t] in defence."

    jump ratbandit_battle_loop
label ratbandit_battle_loop:

    show rat bandit:
        xalign 0.5
        yalign 0.7

    if check_party(pc) == "lost":
        call Battle_Finish from _call_Battle_Finish_75
        jump ratbandit_battle_lose
    $ turn_action = ui.interact()
    call Battle_ASF from _call_Battle_ASF_21
    if oa[0] == "A":
        if oa[1] == "M":
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the arm of the rat, but he leaps back and avoid the blow by inches."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] at the rat's head, but he leaps back and avoid the blow by inches."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the rat, but he leaps back and avoid the arrow by inches."
            if oa[3] == "N":
                "You throw your fist at the rat, but he leaps back and avoid the blow by inches."
            if renpy.random.random() > 0.5:
                rbd "I'm not that easily caught, friend."
            else:
                rbd "Look, loser's weeper. I'm not giving those plums back to you."
        else:
            $ bandit_escaping = False
            call Enemy_Damaging (target, oa[4]) from _call_Enemy_Damaging_3
            $ bandit_escaping = False
            if oa[3] == "A":
                if renpy.random.random() > 0.5:
                    "You slash your [pc.weapon.name!t] at the arm of the rat, your blade grazes through the rat's stomach. Drops of blood drips through his body."
                else:
                    "You slash your [pc.weapon.name!t] at the arm of the rat, knocking him on the ground. He growls at you before getting up, albeit disheveled."
            if oa[3] == "B":
                if renpy.random.random() > 0.5:
                    "You slam your [pc.weapon.name!t] at the rat's head, your blade grazes through the rat's stomach. Drops of blood drips through his body."
                else:
                    "You slam your [pc.weapon.name!t] at the rat's head, knocking him on the ground. He growls at you before getting up, albeit disheveled."
            if oa[3] == "C":
                if renpy.random.random() > 0.5:
                    "You aim and shoot your [pc.weapon.name!t] at the rat, the arrow hit right into his shoulder."
                else:
                    "You run while shooting your [pc.weapon.name!t] at the rat, knocking him on the ground. He growls at you before getting up, albeit disheveled."
            if oa[3] == "N":
                if renpy.random.random() > 0.5:
                    "You throw your fist at the rat, hitting him right across his face, the sheer impact knocks him on the ground."
                else:
                    "You punch into the rat's stomach, grabbing him and slam him on the ground hard."
            if oa[2] == "N":
                "His health decreases by [oa[4]] HP."
            else:
                "You've critically hit the bandit, dealing [oa[4]] HP!"
            $ dia = renpy.random.random()
            if ratbandit.hp > ratbandit.max_hp * 0.5:
                if dia < 0.33:
                    rbd "Argh! I haven't been hit for a long time!"
                elif dia < 0.67:
                    rbd "What's the thing that made you aim that well. That's impossible!"
            else:
                if dia < 0.33:
                    rbd "e-eeeek...! You're not going to hit me twice in a row!"
                elif dia < 0.67:
                    rbd "fffff- I have to get out of this soon."

    if oa[0] == "F":
        $ dia = renpy.random.random()
        if dia > 0.334:
            "You turn around and rub your hand all over your own burly cheeks, feeling and brushing against your ass while you shake your hip."
        elif dia > 0.667:
            "You scrape your member lightly, running your claw from your inner thigh to the back of your balls, you tug at it tightly while staring at the rat seductively."
        else:
            "You cup at your fluffy chest, drawing circles around the area of your nipples. You smile at the rat while your chest bounce up and down slightly."
        if oa[1] == "M":
            "You continue your act for about a minute, but the bandit doesn't even flinch."
            rbd "Well..."
        else:
            if ratbandit.lust > ratbandit.max_lust / 2:
                if renpy.random.random() > 0.5:
                    "Within a few seconds you can already see some movements under the rat's loincloth. He doesn't say anything, except for licking his lips. His lust is increased by [player_flirt]."
                    rbd "...I-if you do this one more time I'm going to grab that huge ass and never let you go..."
                else:
                    "You notice the rat is floundering, trying his best not to get aroused by your seduction, but it is evident that his flushed face tells it all. His lust is increased by [player_flirt]."
                    rbd "You are w-wasting your time. I'm n-not... I'm not... I- uhh... nooo..."
            else:
                if renpy.random.random() > 0.5:
                    "The rat bandit is squirming in reaction to your advance. You can already hear his rapid breathing and grunting, holding his bow tightly. His lust is increased by [player_flirt]."
                    rbd "N-noooo... I'm not- h-horny!"
                else:
                    "You can tell the bandit is already playing with himself when his hand goes under his loincloth, staring at your ass intently. His lust is increased by [player_flirt]."
                    rbd "Hnnnngh... I n-need to... come."
    if oa[0] == "E":
        "You slowly back down from the bandit's attack, you turn around and run as fast as you can."
        rbd "T-thought you were catching me, but you're the one running-..."
        rbd "A-alright then."
        "The thief just smirks before taking back his plums and walks the other direction as you run."
        call Battle_Finish from _call_Battle_Finish_76
        hide screen battle_buttons
        hide screen battle_enemy_stat
        hide screen battle_player_stat
        show screen menu_buttons
        jump main_grove_of_harvest

    if oa[0] == "U":
        "You are not ready to surrender to a person you're catching yet."
        jump ratbandit_battle_loop
    call Ability_Item from _call_Ability_Item_22
    call Battle_Mid_Check from _call_Battle_Mid_Check_20
    if oa[0] == "W":
        call Battle_Finish from _call_Battle_Finish_77
        jump ratbandit_battle_win
    if oa[0] == "T":
        call Battle_End_Check from _call_Battle_End_Check_44
        jump ratbandit_battle_loop
    show rat bandit:
        linear 0.1 zoom 1.04
        linear 0.05 zoom 1

    $ dia = renpy.random.random()
    if bandit_escaping:
        "The bandit grabs a handful of dirt, he immediately splash it right onto your face while you're unaware."
        scene black
        hide screen battle_buttons
        hide screen battle_enemy_stat
        hide screen battle_player_stat
        call Battle_Finish from _call_Battle_Finish_78
        "You scramble to get the dirts out of your eyes. But you know he's getting away with the plum."
        rbd "See you later, loser."
        scene grove_of_harvest:
            blur 32
        pause 1.0
        scene black with dissolve
        scene grove_of_harvest:
            blur 16
        pause 1.0
        scene black with dissolve
        scene grove_of_harvest:
            blur 8
        pause 1.0
        scene black with dissolve
        scene grove_of_harvest
        show screen menu_buttons
        "When you get rid of the dirt, the thief is already gone. You return empty-handed."
        jump main_grove_of_harvest
    elif bandit_rat_critical:
        $ bandit_rat_critical = False
        $ raw_damage = int(renpy.random.randint(ratbandit.min_damage, ratbandit.max_damage))
        $ enemy_damage = int(damageFormula(raw_damage, pc.defense)*(renpy.random.random()*1.1+1.3))
        call Damaging (enemy, pc, enemy_damage) from _call_Damaging_10
        if random_chance < 0.5:
            "The rat bandit strikes his dagger towards you, it was a critical blow! Your health decreases by [enemy_damage] HP."
        else:
            "The rat bounces around and hit you with a fistful of force, it was a critical blow! Your health decreases by [enemy_damage] HP."
        rbd "Heh, this is what precision looks like."
    if dia < 0.325:
        if renpy.random.random()*100 > pc.dodge+extra_dodge:
            $ raw_damage = int(renpy.random.randint(ratbandit.min_damage, ratbandit.max_damage))
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_11
            $ random_chance = renpy.random.random()

            if random_chance < 0.5:
                "The rat bandit strikes his dagger towards you, you are not quick enough to dodge his blow. Your health decreases by [enemy_damage] HP."
            else:
                "The rat bounces around and hit you with a fistful of force. Your health decreases by [enemy_damage] HP."
            rbd "Heh, didn't see it coming do you?"
        else:
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The rat bandit strikes his dagger towards you, you managed to deflect his bow and dodge the attack."
            else:
                "The rat bounces around and try to hit you with a fistful of force, but you block the blow and push him back."
            rbd "Stop jumping around like I do!"
    elif dia < 0.60:
        "The bandit watches your movement, he is looking at your body intently making you all nervous."
        $ bandit_rat_critical = True

    elif dia < 0.75:
        "The bandit looks around, he's trying to escape while you're not aware! You need to stop him before he successfully escape."
        $ bandit_escaping = True
    else:

        $ raw_flirt = int(renpy.random.randint(ratbandit.min_lust_damage, ratbandit.max_lust_damage))
        $ enemy_flirt = damageFormula(raw_flirt, pc.lust_defense)
        $ pc.lust += enemy_flirt
        if pc.lust > pc.max_lust:
            $ pc.lust = pc.max_lust
        $ random_chance = renpy.random.random()
        if random_chance < 0.5:
            "The rat scratches at his pants, he put two of his fingers across his crotch, tracing the shape of his cock in front of you."
            rbd "You thristy? Let me go and maybe I'll let you jerk me off."
            if renpy.random.random()*100 > pc.lust_dodge + extra_lust_dodge:
                "You gulp at his attempt at seduction. Admittedly you are extremely aroused, thinking about how his cock would taste like. Your lust increased by [enemy_flirt]."
            else:
                "You stare at him, giving him weird side eyes. You have evaded his attempt at seduction."
        else:
            "The bandit stretches his body, flaunting his muscular physiques, you can tell his soft chest is almost bulging in front of you."
            rbd "Take a look at this, well you get to touch it if you promise not to chase after me ever again."
            if renpy.random.random()*100 > pc.lust_dodge + extra_lust_dodge:
                "You are stunned by his gorgeous muscles, you mind wanders through scenarios of him being inside your body. Your lust increased by [enemy_flirt]."
            else:
                "His attack at your lust seems to have failed as you stand there and wait for him to finish his taunt."

    call Battle_End_Check from _call_Battle_End_Check_45
    jump ratbandit_battle_loop
label ratbandit_battle_win:
    $ ratbandit.win += 1
    "The thief slumps on the ground, he's too exhausted to escape from your grasp."
    rbd "D-damn it. A-alright you caught me..."
    e "Y-yeah you were an ass to get a hold of."
    e "Why did you take the plums?"
    rbd "My boss wanted those, I needed to impress him after failing him last time."
    e "But the plums are ours. Give me back those and maybe you can- leave."
    rbd "He's going to kill me if I don't give him back the plums."
    rbd "I mean like, kill."
    e "..."
    rbd "Like, death. Dude."
    e "Uh..."
    "The thief gestures his hand over his neck. You're not sure if you should trust him or not."
    rbd "Dude, I promise I won't come back again."
    e "Why would you even come here without thinking about getting caught?"
    rbd "I don't know, I thought I was safe because of the hyena."
    e "Hyena?"
    rbd "Yeah, boss told me the hyena takes care of the farm."
    e "Are you talking about Jog? Do you know him?"
    rbd "The small one, he was one of us long time ago. boss said if I- I- don't follow him I'd end up like the hyena..."
    e "Why are you implying he's doing worse than you are right now."
    rbd "...well. I don't know."
    "You remain silent, the rodent thief doesn't feel as easy as you do right now."
    rbd "That's all I can tell you, dude. Please just let me take the plum and I won't bother your farm again."

    "If the rat's telling the truth, not returning the plum basically means death sentence to him..."
    "On the other hand, you'd love to impress Jog by getting back the plums."
    if isBandit:
        "You know the shark doesn't kill anyone as easily as the rat proclaims."
        "But perhaps it can divert some suspicion away from you, what if the rat reports to the shark that a goat was there."
        "And his boss connects the dots?"
    else:
        "Even though you don't know what Jog has to do with the thieves."
        "Was he always working for the bandit? Surely he won't betray everyone's trust for the bandit boss."
        "Or, maybe he was just a former one, who abandoned his bandit life to live in Lusterfield."
    "You're not sure. But you need to make a choice here."
    menu:
        e "Hmmph...."
        "Get the plums back":
            $ bandit_has_plum = False
            e "N-no. I can't risk getting you to come back."
            rbd "D-dude. Please. I-I can't go back empty-handed."
            rbd "M-my boss is goin-"
            e "No. Get your stuff and leave. And do not come back."
            rbd "You're so cruel, dude."
            e "One more whine and you're not leaving this place."
            rbd "O-ok. You're bad at scaring me but I'll do whatever you want."
            rbd "The plums are over there."
            "He points at the small dirt lump a few steps next to him."
            rbd "A-and I'll be going."
            "You watch silently as the thief gets up, and runs away from your sight."
            "He quickly disappear, leaving you with the lump of plums."
            "You dig the fruits up with your hand and soon return to the garden."
        "Let him keep the plums":
            $ bandit_has_plum = True
            e "Uhh, keep it. But if the others and I see your face again here, you're never going back to your boss."
            rbd "Y-yes, ok. Thank you. I'll remember this."
            "The rat scrambles to run a few steps towards a lump in the ground. He begins digging down with his hands."
            "He uncovers some plums that he had been hiding right there."
            rbd "I'll be on my way! Thanks."
            e "Go now."
            "You stare at the agile bandit with hands full of plums, he waves back at you."
            "Soon, the thief disappears into the grasses again."
            "Despite returning empty-handed, at least you know the plums are safe again."
            "Perhaps you also did the thief a favour, knowing he won't get into trouble with his boss."
    $ quest33.status = 4
    $ quest33.qComp(__("Return and Report to Jog"))
    jump main_grove_of_harvest
label ratbandit_battle_lose:
    $ ratbandit.lose += 1
    if pc.hp <= 0:
        "You are too exhausted to fight back against the rat."
    else:
        "Your cock is pumping, filled with lust over the flirtation the rat has been showering you."
    rbd "Alright, let's make this quick."
    $ lost_gold = int(pc.gold*0.15*renpy.random.random()) + 50
    $ pc.gold -= lost_gold
    "He swindles [lost_gold] out of your pocket."
    rbd "And I get to keep my plums. That's the best deal I've ever seen."
    "The thief doesn't even give you another glance, he just whistles his way out of the farm."
    "Your consciousness fades."
    scene black with dissolve
    pause 5
    ar "-Pup?"
    scene grove_of_harvest with dissolve
    "At some point, you wake up with Arthur glaring over you."
    ar "You looking rough here, feeling any body parts missing?"
    e "N-no, I- I just let the thief slip away."
    if pc.hp <= 0:
        ar "That cunning son of a thief must have been a bitch to handle."
    else:
        ar "Good, thought you're just too excited to see me with the bulge down there."
        "You blush intensely."
    ar "Look, got you some potions while you were passed out, should feel better now."
    "You slowly get up from the grass ground."
    if arthur_2ndChoice == "Yes" or arthur_2ndChoice == "No":
        e "T-thanks, Master."
    else:
        e "Thanks, Arthur."
    "He smiles."
    ar "You should prepare some potions that makes you aim better, especially against sneaky bastards like these thieves."
    "You nod."
    ar "I'll be around, but he probably won't come back today at least."
    "The shepherd leaves to a spot near you, continuing taking care of his plants."
    $ timenow.hour = 14
    $ pc.rest()
    jump main_grove_of_harvest
label sharkbandit_battle:



    $ enemy_num = 1
    $ enemy = sharkbandit
    $ enemy.max_hp = 900
    $ enemy.min_damage = 80
    $ enemy.max_damage = 105
    $ enemy.defense = 65
    $ enemy.min_lust_damage = 16
    $ enemy.max_lust_damage = 20
    $ enemy.dodge = 5
    $ enemy.lust_defense = 30
    $ enemy.exp_drop = 260
    $ sharkbandit.beginbattle()
    call beginningBattle from _call_beginningBattle_23
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    $ bandit_escaping = False
    $ bandit_shark_critical = False

    scene bandits_hideout:
        blur 8
    show shark bandit:
        xalign 0.5
        yalign 0.7
    if pc.weapon == None:
        "You are facing a shark bandit against the wall. You hold and clench your fist."
    else:
        "You are facing a shark bandit in the field, it's hard to catch him in the middle of the tall grasses. You hold your [pc.weapon.name!t] in defence."

    jump sharkbandit_battle_loop

label sharkbandit_battle_loop:

    show shark bandit:
        xalign 0.5
        yalign 0.7

    if check_party(pc) == "lost":
        call Battle_Finish from _call_Battle_Finish_79
        jump sharkbandit_battle_lose
    $ turn_action = ui.interact()
    call Battle_ASF from _call_Battle_ASF_22
    if oa[0] == "A":
        if oa[1] == "M":
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the arm of the shark, but it only scratches his skin."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] at the shark's head, but it only scratches his skin."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the shark, but it only scratches his skin."
            if oa[3] == "N":
                "You throw your fist at the shark, but it only scratches his skin."
            if renpy.random.random() > 0.5:
                sbd "That's all you got?"
            else:
                sbd "Huh."
        else:
            call Enemy_Damaging (target, oa[4]) from _call_Enemy_Damaging_4
            if oa[3] == "A":
                if renpy.random.random() > 0.5:
                    "You slash your [pc.weapon.name!t] at the arm of the shark, your blade grazes through the shark's stomach. Drops of blood drips through his body."
                else:
                    "You slash your [pc.weapon.name!t] at the arm of the shark, knocking him on the ground. He growls at you before getting up, albeit disheveled."
            if oa[3] == "B":
                if renpy.random.random() > 0.5:
                    "You slam your [pc.weapon.name!t] at the shark's head, your blade grazes through the shark's stomach. Drops of blood drips through his body."
                else:
                    "You slam your [pc.weapon.name!t] at the shark's head, knocking him on the ground. He growls at you before getting up, albeit disheveled."
            if oa[3] == "C":
                if renpy.random.random() > 0.5:
                    "You aim and shoot your [pc.weapon.name!t] at the shark, the arrow hit right into his shoulder."
                else:
                    "You run while shooting your [pc.weapon.name!t] at the shark, knocking him on the ground. He growls at you before getting up, albeit disheveled."
            if oa[3] == "N":
                if renpy.random.random() > 0.5:
                    "You throw your fist at the shark, hitting him right across his face, the sheer impact knocks him on the ground."
                else:
                    "You punch into the shark's stomach, grabbing him and slam him on the ground hard."
            if oa[2] == "N":
                "His health decreases by [oa[4]] HP."
            else:
                "You've critically hit the bandit, dealing [oa[4]] HP!"
            $ dia = renpy.random.random()
            if sharkbandit.hp > sharkbandit.max_hp * 0.5:
                if dia < 0.33:
                    sbd "Argh! I haven't been hit for a long time!"
                elif dia < 0.67:
                    sbd "It's just a scratch..."
            else:
                if dia < 0.33:
                    sbd "N-not, giving... up."
                elif dia < 0.67:
                    sbd "I'll beat you RIGHT HERE! Come closer!"

    if oa[0] == "F":
        $ dia = renpy.random.random()
        if dia > 0.334:
            "You turn around and rub your hand all over your own burly cheeks, feeling and brushing against your ass while you shake your hip."
        elif dia > 0.667:
            "You scrape your member lightly, running your claw from your inner thigh to the back of your balls, you tug at it tightly while staring at the shark seductively."
        else:
            "You cup at your fluffy chest, drawing circles around the area of your nipples. You smile at the shark while your chest bounce up and down slightly."
        if oa[1] == "M":
            "You continue your act for about a minute, but the bandit doesn't even flinch."
            sbd "Well..."
        else:
            if sharkbandit.lust > sharkbandit.max_lust / 2:
                if renpy.random.random() > 0.5:
                    "Within a few seconds you can already see some movements under the shark's loincloth. He doesn't say anything, except for licking his lips. His lust is increased by [player_flirt]."
                    sbd "...I-if you do this one more time I'm going to grab that huge ass and never let you go..."
                else:
                    "You notice the shark is floundering, trying his best not to get aroused by your seduction, but it is evident that his flushed face tells it all. His lust is increased by [player_flirt]."
                    sbd "You are w-wasting your time. I'm n-not... I'm not... I- uhh... nooo..."
            else:
                if renpy.random.random() > 0.5:
                    "The shark bandit is squirming in reaction to your advance. You can already hear his rapid breathing and grunting, holding his bow tightly. His lust is increased by [player_flirt]."
                    sbd "...It's nothing."
                else:
                    "You can tell the bandit is already playing with himself when his hand goes under his loincloth, staring at your ass intently. His lust is increased by [player_flirt]."
                    sbd "Hnnnngh... ."
    if oa[0] == "E":
        "The shark is blocking your escape..."
        jump sharkbandit_battle_loop

    if oa[0] == "U":
        "You are not ready to surrender yet."
        jump sharkbandit_battle_loop
    call Ability_Item from _call_Ability_Item_23
    call Battle_Mid_Check from _call_Battle_Mid_Check_21
    if oa[0] == "W":
        call Battle_Finish from _call_Battle_Finish_80
        jump sharkbandit_battle_win
    if oa[0] == "T":
        call Battle_End_Check from _call_Battle_End_Check_46
        jump sharkbandit_battle_loop
    show shark bandit:
        linear 0.1 zoom 1.04
        linear 0.05 zoom 1

    $ dia = renpy.random.random()

    if dia < 0.2 or (dia < 0.4 and enemy.hp < enemy.max_hp*0.5):
        "The shark slows down, and drinks his red health potion."
        $ health_restored = int((enemy.max_hp - enemy.hp)*(abs(renpy.random.random()-0.7)*0.4)+50)

        call Enemy_Self_Healing (enemy, health_restored) from _call_Enemy_Self_Healing_3
        sbd "Well, I'm good to go now."
    elif dia < 0.65 or (dia < 0.65 and pc.hp < pc.max_hp*0.5):
        if renpy.random.random()*80 > pc.dodge+extra_dodge:
            $ raw_damage = int(renpy.random.randint(sharkbandit.min_damage, sharkbandit.max_damage))
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_12
            $ random_chance = renpy.random.random()


            "The shark bandit swings his axe towards you, you are not quick enough to dodge his blow. Your health decreases by [enemy_damage] HP."

            sbd "I'll strike you down, like anyone else in my way."
        else:
            $ random_chance = renpy.random.random()

            "The shark bandit swings his axe towards you, you managed to deflect his bow and dodge the attack."

            sbd "Lucky dodge."

    elif dia < 0.85 or (dia < 0.55 and pc.lust < pc.max_lust*0.5):

        $ raw_flirt = int(renpy.random.randint(sharkbandit.min_lust_damage, sharkbandit.max_lust_damage))
        $ enemy_flirt = damageFormula(raw_flirt, pc.lust_defense)
        $ pc.lust += enemy_flirt
        if pc.lust > pc.max_lust:
            $ pc.lust = pc.max_lust
        $ random_chance = renpy.random.random()
        if random_chance < 0.5:
            "The shark scratches at his pants, he put two of his fingers across his crotch, tracing the shape of his cock in front of you."
            sbd "Come here, traveller. Need a drink?"
            if renpy.random.random()*100 > pc.lust_dodge + extra_lust_dodge:
                "You gulp at his attempt at seduction. Admittedly you are extremely aroused, thinking about how his cock would taste like. Your lust increased by [enemy_flirt]."
            else:
                "You stare at him, giving him weird side eyes. You have evaded his attempt at seduction."
        else:
            "The bandit stretches his body, flaunting his muscular physiques, you can tell his soft chest is almost bulging in front of you."
            sbd "I can see your lustful eyes, you must be wanting this, don't you."
            if renpy.random.random()*100 > pc.lust_dodge + extra_lust_dodge:
                "You are stunned by his gorgeous muscles, you mind wanders through scenarios of him being inside your body. Your lust increased by [enemy_flirt]."
            else:
                "His attack at your lust seems to have failed as you stand there and wait for him to finish his taunt."
    else:
        sbd "Ughhh-!!"
        "The shark bulges his muscle, he takes some food from his pocket and starts eating..."
        $ health_increased = int(renpy.random.random()*60+25)
        call Enemy_Self_Healing (enemy, health_increased) from _call_Enemy_Self_Healing_4
        "He's getting bigger than before... with this, his maximum HP is also increasing by [health_increased]."
        $ enemy.max_hp += health_increased

    call Battle_End_Check from _call_Battle_End_Check_47
    jump sharkbandit_battle_loop
label sharkbandit_battle_lose:
    $ sharkbandit.lose += 1
    "You pant heavily, at this point it is just better to admit your defeat to the colossal shark in front of you."
    sbd "So rare would we see a traveler just deliver himself right at my front door."
    sbd "Often we have to actually round these guys up, beat them up and take whatever we want."
    sbd "You were a good fighter."
    sbd "But, it still ends the same way it ends, with me on top."
    sbd "Now..."
    sbd "Why are you here, traveller."
    "The bandit kneels, holding the edge of his axe over your neck."
    e "...To catch the thief that stole our plums, that's it."
    sbd "Nothing else?"
    "You nod. The bandit boss seems rather perplexed, but he just continues with his questioning."
    sbd "Where are you from?"
    e "Lusterfield, I f-followed the r-rat thief here."
    sbd "The one where the hyena lives, huh? how's he?"
    e "Uh... doing well."
    "He chuckles, slowly pulling his axe away."
    sbd "Alright, you came over dangerous place here just for some plums."
    sbd "Tell me, what's the end goal here."
    e "I-I... I just wanted to catch the thief. I didn't know about you people."
    sbd "Fair."
    sbd "Then, well."
    sbd "Let's get to the fun part, shall we?"
    e "W-wait..."
    call Scene_Shark_Bandit_Lose from _call_Scene_Shark_Bandit_Lose
    $ pc.add_active_status(stuffed)
    "You don't know when his cumming stopped, but he is merely holding you in place until at some point he lets you down on the ground again."
    "It feels like such a long time since you haven't felt the power of gravity."
    sbd "Normally, I'd keep travellers like you for the my fellow bandits to use all day long."
    "You lie on the ground, mixture of sweat and cum dribbling all over your body, as the bandit boss stands above you."
    sbd "But, I'm fond of you. Brave little soul picking up random fights and all."
    "He kneels down, glancing over your twitching cock and cum on the ground like a trophy he got."
    sbd "I'll let you go back to your village and what not, but if you somehow end up in my hands once more, I wouldn't hesitate to tie you up and let the others have fun."
    sbd "Or, if you are too much trouble, I'll just sell you out."
    "The shark smiles, his cocks remains hanging in the air until he walks back and picks up his armors."
    "You are left here, still completely exhausted from the fight."
    sbd "Well, I'll let you go now. your hole was probably better than a few stale red plums, but I'm not risking getting visited by a village full of peasants."
    sbd "You can keep your plums, but don't ever come back, I'd hate to break a good toy so soon."
    "Soon, you black out as the boss approaches you with full clothes, dragging you along the road."
    "A few hours passed."
    "You wake up once more, your belongings are all safe except for a large portion of gold. At least the plum thief won't visit the farm now."
    "Your muscles are sore, ass still gaping from the cocks you've had."
    "It seems your belly is getting smaller and smaller, but you're still leaking some leftover cum as you stand up."
    "But, it was so good... feeling his cocks inside of you, being violently thrusted and-"
    "Shaking off the thoughts, you pick up your belongings and quickly carry onto your journey."
    pause 1.0 
    call lost_gold_check (0.25, 150, True) from _call_lost_gold_check_11
    pause 1.0
    $ quest33.status = 4
    $ quest33.qComp(__("Return and Report to Jog"))
    jump main_grove_of_harvest
label sharkbandit_battle_win:
    $ sharkbandit.win += 1
    sbd "F-fuck."
    "He lies on the ground, panting heavily. And his belly doesn't help but rolls him further down."
    msg "Bandit Boss Winning Scene WIP!"
    scene black with dissolve
    pause 2
    scene bandits_hideout with dissolve
    sbd "What do you want?"
    e "Where's the thief that stole my plums?"
    sbd "Plums? They're over there, just take it."
    sbd "Look, if you kill me right here, my people will make sure to destroy where you live, and you'll suffer for eternity."
    sbd "Think you can handle all of them?"
    e "Just tell me where the thief is."
    sbd "..."
    sbd "He's out there, but I'm not giving him up."
    e "Not at the risk of your life?"
    sbd "No. Take your plums and gold, but not my men."
    e "A-alright, I don't want to kill anyone here."
    e "But if you and your thieves ever come back to our farm, I can't promise anything."
    sbd "Whatever you say, adventurer."
    e "Can I trust your words?"
    sbd "People often say you shouldn't trust a bandi-"
    "You blankly stare at him, with your weapon still on your hand."
    sbd "But y-yes."
    "You leave the bandit boss behind and take the plum inside the hideout before you pick up your stuff, and move on."
    "The shark gives you a few glances before getting up, going back to his shelter pretending like nothing happened."
    "With the boss' promise. At least you can now go back with the plums and not having to worry about the thief."
    "..."
    $ pc.exp += 300
    $ pc.gold += 150
    "You received 300 exp and 150 gold."
    if pc.exp > pc.expCap and pc.level <= levelCap:
        $ pc.LevelUp()
        msg "You are now Level [pc.level]! Check your inventory to allocate your level points."
    $ quest33.status = 4
    $ quest33.qComp(__("Return and Report to Jog"))
    jump main_grove_of_harvest
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
