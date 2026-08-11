




label Ability_Item:
    $ isAbility = next((x for x in abilities if x != None and x.img == turn_action), None)
    if isAbility != None:
        $ isAbility.coolDownTimer = isAbility.coolDown

    if turn_action == "Fiery Charge":

        if target == minostatue:
            "You cannot use this ability against the enemy."
        else:
            call Ability_Fiery_Charge from _call_Ability_Fiery_Charge

    if turn_action == "Fortify":

        call Ability_Fortify from _call_Ability_Fortify

    if turn_action == "Resolution":

        call Ability_Resolution from _call_Ability_Resolution

    if turn_action == "Self Heal":

        call Ability_Self_Heal from _call_Ability_Self_Heal

    if turn_action == "Alluring Lust":

        call Ability_Alluring_Lust from _call_Ability_Alluring_Lust

    if turn_action == "Camouflage":

        call Ability_Camouflage from _call_Ability_Camouflage

    if turn_action == "Piercing Blow":
        if target == minostatue:
            "You cannot use this ability against the enemy."
        else:
            call Ability_Piercing_Blow from _call_Ability_Piercing_Blow

    if turn_action == "Tranquil Mend":

        call Ability_Tranquil_Mend from _call_Ability_Tranquil_Mend

    if turn_action == "Immolation":

        if target == minostatue:
            "You cannot use this ability against the enemy."
        else:
            call Ability_Immolation from _call_Ability_Immolation

    if turn_action == "Spectral Orb":

        if target == minostatue:
            "You cannot use this ability against the enemy."
        else:
            call Ability_Spectral_Orb from _call_Ability_Spectral_Orb

    if turn_action == "Sundering Surge":

        if target == minostatue:
            "You cannot use this ability against the enemy."
        else:
            call Ability_Sundering_Surge from _call_Ability_Sundering_Surge

    if turn_action == "Core Strike":

        if target == minostatue:
            "You cannot use this ability against the enemy."
        else:
            call Ability_CoreStrike from _call_Ability_CoreStrike

    if turn_action == "Tenacity Potion":
        call Use_Tenacity_Potion from _call_Use_Tenacity_Potion
    if turn_action == "Accuracy Potion":
        call Use_Accuracy_Potion from _call_Use_Accuracy_Potion
    if turn_action == "Green Ointment":
        call Use_Green_Ointment from _call_Use_Green_Ointment
    if turn_action == "Small HP Potion":
        call Use_Small_HP from _call_Use_Small_HP
    if turn_action == "Strength Potion":
        call Use_Strength from _call_Use_Strength
    if turn_action == "Small MP Potion":
        call Use_Small_MP from _call_Use_Small_MP
    return

label Use_Green_Ointment:
    $ pc.hp += 80
    if pc.hp >= pc.max_hp:
        $ pc.hp = pc.max_hp
    $ pc.mp += 80
    if pc.mp >= pc.max_mp:
        $ pc.mp = pc.max_mp
    $ pc.lust -= 30
    if pc.lust <= 0:
        $ pc.lust = 0
    $ consuming("Green Ointment", inventory, 1)
    "You used a green ointment and restored 80 HP and 80 MP, your Lust is also lowered by 30."
    $ cleanse(status)
    "The green ointment cleansed all your negative effect as well."
    return

label Use_Small_HP:
    $ pc.hp += 40
    if pc.hp >= pc.max_hp:
        $ pc.hp = pc.max_hp
    $ consuming("Small HP Potion", inventory, 1)
    "You used a bottle of Small HP Potion and healed 40 HP."
    return

label Use_Small_MP:
    $ pc.mp += 40
    if pc.mp >= pc.max_mp:
        $ pc.mp = pc.max_mp
    $ consuming("Small MP Potion", inventory, 1)
    "You used a bottle of Small MP Potion and recovered 40 MP."
    return

label Use_Strength:
    $ empowered.rounds = empowered.max_rounds
    $ status.append(empowered)
    $ extra_damage += empowered.effect
    $ consuming("Strength Potion", inventory, 1)
    "You used a bottle of Strength Potion, your damage is now increased for 3 rounds."
    return

label Use_Accuracy_Potion:
    $ accuracy_using = 3
    $ extra_accuracy = 20
    $ consuming("Accuracy Potion", inventory, 1)
    "You used a bottle of Accuracy Potion, your accuracy is now increased for 3 rounds."
    return

label Use_Tenacity_Potion:
    $ pc.defense += fortifying.effect
    $ fortify = True
    $ consuming("Tenacity Potion", inventory, 1)
    "You used a bottle of Tenacity Potion, your defenses is now increased for 3 rounds."
    return

label Ability_Self_Heal:
    $ healing = 50 + renpy.random.randint(int(selfheal.effect*pc.itg*0.15), int(selfheal.effect*pc.itg*0.2))
    $ pc.mp -= selfheal.cost
    $ pc.hp += healing
    if pc.hp > pc.max_hp:
        $ healing -= (pc.hp - pc.max_hp)
        $ pc.hp = pc.max_hp
    "You used self heal, your health goes up by [healing] HP."
    return

label Ability_Fiery_Charge:


    if isScorched not in enemy.item_drop01:
        $ scorch_damage = int((1+pc.itg*3) * renpy.random.randint(pc.itg-2, pc.itg+1) * (renpy.random.random()+0.15) /10)
        call Enemy_Damaging_Spell (enemy, scorch_damage) from _call_Enemy_Damaging_Spell
        "You use Fiery Charge on [target.name], dealing [scorch_damage] HP Damage. They are now scorched."
    else:
        $ scorch_damage = int((1+pc.itg*3) * renpy.random.randint(pc.itg-2, pc.itg+1) * (renpy.random.random()+0.15) * isScorched.effect / 250)
        "You use Fiery Charge on [target.name], they continue to be scorched for two additional rounds."
    $ ApplyScorch(enemies, scorched)
    $ pc.mp -= fierycharge.cost

    call Trinket_Weeping_Willow from _call_Trinket_Weeping_Willow
    if enemy_num == 2:
        call Trinket_Weeping_Willow from _call_Trinket_Weeping_Willow_1

    return

label Ability_Piercing_Blow:
    $ pb_round = 2
    "You use piercing blow, your normal attack next round will critically strike, and your critical damage increases as well."
    $ pc.mp -= piercingblow.cost

    return
label Ability_Fortify:
    "You use fortify, your body glistens with radiance as you cast the magic. Your defense goes up this round."
    $ pc.mp -= fortifying.cost
    $ pc.defense += fortifying.effect
    $ fortify = True
    return
label Ability_Alluring_Lust:
    "You cast the spell on your body. Your body appears much softer and pliable now, enticing the [enemy.name] to grab and grope at it."
    $ alluring_lust = int(alluringlust.effect/30*(pc.itg + pc.cha*1.5))
    $ adorned.rounds = adorned.max_rounds
    $ status.append(adorned)
    $ pc.mp -= alluringlust.cost

    return

label Ability_Tranquil_Mend:
    "You cast tranquil mend, and heals yourself for the next few rounds."
    $ tranquilmend_heal = 10 + renpy.random.randint(int(pc.itg*0.3), int(pc.itg*0.5))*int(tranquilmend.effect/2)
    $ pc.mp -= tranquilmend.cost
    $ ApplyStatus(status, mended, 3)
    if ally_num == 2:
        $ ApplyStatus(ally.status, mended, 3)
    return

label Ability_Camouflage:
    "You camouflage your body in front of your enemy. Your dodge rate is increased for the rest of the battle."
    $ extra_dodge += int(camouflage.effect/30*(pc.itg + pc.agi*1.5)) + 1
    $ pc.mp -= camouflage.cost
    return

label Ability_CoreStrike:
    $ raw_damage = renpy.random.randint(int(pc.damage*0.6), int(pc.damage*1.4 * ((corestrike.effect+4*pc.ten+2*pc.itg)/30))) * ((100 + extra_damage) / 100 )
    $ player_damage = damageFormula(raw_damage, enemy.defense)
    $ pc.mp -= corestrike.cost
    $ stunned.rounds = stunned.max_rounds
    if enemy_num == 1:
        "You strike the core of [enemy.name], causing [enemy.name] to fall over. You dealt [player_damage] and stuns [enemy.name] for [stunned.max_rounds] round."
        $ enemy.item_drop01.append(stunned)

        call Enemy_Damaging_Spell (target, player_damage) from _call_Enemy_Damaging_Spell_1

    if enemy_num == 2:
        "You strike the core of [target.name], causing [target.name] to fall over. You dealt [player_damage] and stuns [target.name] for [stunned.max_rounds] round."
        $ target.item_drop01.append(stunned)

        call Enemy_Damaging_Spell (enemy, player_damage) from _call_Enemy_Damaging_Spell_2
        call Enemy_Damaging_Spell (enemy2, player_damage) from _call_Enemy_Damaging_Spell_3
    call Trinket_Weeping_Willow from _call_Trinket_Weeping_Willow_2
    return

label Ability_Resolution:
    $ rnwdg = 67.5/((pc.itg/2)+10)
    $ raw_lust = 70 + resolution.effect - 5*(1.6**rnwdg)+pc.itg**0.666
    $ reduced_lust = renpy.random.randint(int(raw_lust*0.8), int(raw_lust*1.25))
    $ pc.restore(mp =-resolution.cost)
    "You used Resolution, and reduced your current lust by [reduced_lust]."
    $ pc.restore(lust =-reduced_lust)
    return

label Ability_Immolation:

    $ immolation_damage = int(30 + (1+pc.itg*2) * renpy.random.randint(pc.itg-3, pc.itg) * (renpy.random.random()+0.15))
    $ extra_damage = int(20 + renpy.random.randint(pc.itg, pc.itg+3) * (renpy.random.random()+0.15))
    $ enemy_isScorched = next((x for x in enemy.item_drop01 if x.img == "Scorched"), None)
    if enemy_isScorched == None:
        "You cast your spell on [target.name] and immolate all enemies, dealing [immolation_damage] HP Damage."
        call Enemy_Damaging_Spell (enemy, immolation_damage) from _call_Enemy_Damaging_Spell_4
    else:

        $ immolation_damage = int(30 + (1+pc.itg*2) * renpy.random.randint(pc.itg-3, pc.itg) * (renpy.random.random()+0.15) * enemy_isScorched.effect / 40)
        "You cast your spell on [target.name] and immolate all enemies, scorched targets are dealt [immolation_damage] HP Damage."
        $ enemy_isScorched.effect += 15
        call Enemy_Damaging_Spell (enemy, immolation_damage+extra_damage) from _call_Enemy_Damaging_Spell_5
    if enemy_num == 2:
        $ enemy2_isScorched = next((x for x in enemy2.item_drop01 if x.img == "Scorched"), None)
        if enemy2_isScorched == None:

            call Enemy_Damaging_Spell (enemy2, immolation_damage) from _call_Enemy_Damaging_Spell_6
        else:
            $ immolation_damage = int(30 + (1+pc.itg*2) * renpy.random.randint(pc.itg-3, pc.itg) * (renpy.random.random()+0.15) * enemy2_isScorched.effect / 40)
            $ enemy2_isScorched.effect += 15
            call Enemy_Damaging_Spell (enemy2, immolation_damage+extra_damage) from _call_Enemy_Damaging_Spell_7
    $ pc.mp -= immolation.cost


    call Trinket_Weeping_Willow from _call_Trinket_Weeping_Willow_8
    if enemy_num == 2:
        call Trinket_Weeping_Willow from _call_Trinket_Weeping_Willow_9

    return

label Ability_Spectral_Orb:
    $ orbed = next((x for x in status if x.img == "Orbs"), None)
    if orbed == None:
        $ ApplyStatus(status, orbs, 1)
        $ orbed = next((x for x in status if x.img == "Orbs"), None)
    else:
        $ orbed.rounds += 1
    $ pc.mp -= spectralorb.cost
    $ raw_orb_damage = orbed.rounds * spectralorb.effect * pc.itg * renpy.random.randint(9, 15) * 0.01
    "You conjures a spectral orb, and it floats around you."
    $ orb_damage = damageFormula(raw_orb_damage, target.defense)
    call Enemy_Damaging_Spell (enemy, orb_damage) from _call_Enemy_Damaging_Spell_8
    if enemy_num > 1:
        $ orb_damage = damageFormula(raw_orb_damage, enemy2.defense)
        call Enemy_Damaging_Spell (enemy2, orb_damage) from _call_Enemy_Damaging_Spell_9
    "You now have [orbed.rounds] orbs, blasting them all forwards, all enemies are dealt [orb_damage] HP."
    return

label Ability_Sundering_Surge:

    $ raw_damage = renpy.random.randint(int(pc.damage*0.6), int(pc.damage*1.4)) * ((100 + extra_damage) / 100)
    $ player_damage = damageFormula(raw_damage, target.defense)

    call Enemy_Damaging_Spell (target, player_damage) from _call_Enemy_Damaging_Spell_10

    if pc.checkEquipped("Idol of Virtue"):
        call ApplyWounded (target, 1 + int((pc.stg + pc.cha) / 3), 1 + int(pc.itg / 4)) from _call_ApplyWounded
    else:
        call ApplyWounded (target, 1 + int(pc.stg / 3), 1 + int(pc.itg / 4)) from _call_ApplyWounded_1

    $ isBruised = next((x for x in target.item_drop01 if x.img == "Bruised"), None)
    if isBruised != None:
        $ isBruised.rounds += 2
        if isBruised.rounds >= 3:
            $ isBruised.rounds = 3
    else:
        $ ApplyStatus(target.item_drop01, bruised, 2)


    return

label ApplyWounded(wounded_enemy, base, stacks):
    $ isWounded = next((x for x in wounded_enemy.item_drop01 if x.img == "Wounded"), None)
    if isWounded != None:
        $ isWounded.rounds += stacks
        $ isWounded.effect = base
    else:
        $ ApplyStatus(wounded_enemy.item_drop01, wounded, stacks)
        $ next((x for x in wounded_enemy.item_drop01 if x.img == "Wounded"), None).effect = base

    return

label Enemy_Damaging_Spell(enemy, damage):
    if equippedTrinket("Bruisers Bite"):
        call ApplyWounded (enemy, 5, 5) from _call_ApplyWounded_2
    call Enemy_Damaging (enemy, damage) from _call_Enemy_Damaging_5
    return

label Trinket_Weeping_Willow:
    if equippedTrinket("Weeping Willow"):
        $ healing = int(pc.itg * renpy.random.random() * 3) + 1
        $ pc.hp += healing
        if pc.hp >= pc.max_hp:
            $ pc.hp = pc.max_hp
    return

label Enemy_Self_Healing(healed_enemy, heal_amount):
    $ isBruised = next((x for x in healed_enemy.item_drop01 if x.img == "Bruised"), None)
    if isBruised != None:
        $ heal_amount_int = int(heal_amount * (100 - isBruised.effect) / 100)
    else:
        $ heal_amount_int = int(heal_amount)
    $ healed_enemy.restore(heal_amount_int)
    "[healed_enemy.img] healed for [heal_amount_int] HP."

    return

label Enemy_Self_Purifying(purified_enemy, lust_amount):

    $ purified_enemy.restore(lust = -int(lust_amount))
    "[purified_enemy.img] has reduced [lust_amount] Lust."

    return

label Enemy_Damaging(enemy, damage):

    if hasStatus(enemy, thorned) != False:
        $ thorned_rounds = hasStatus(enemy, thorned).rounds
        $ pc.restore(hp=-thorned_rounds)
        "You are wounded from the enemy's thorns, your health decreases by [thorned_rounds] HP."

    $ enemy.restore(hp=-damage)

    return

label Damaging(aggressor, victim, damage):

    $ victim_thorned = hasStatus(victim, thorned)
    if equippedTrinket("Spirespike") and victim == pc and aggressor != pc and aggressor != ally:
        if victim_thorned == False:
            $ ApplyStatus(status, thorned, 5)
            $ victim_thorned = hasStatus(victim, thorned)
        else:
            $ victim_thorned.rounds += 5

    if victim_thorned != False:
        $ thorned_rounds = victim_thorned.rounds
        $ aggressor.restore(hp=-thorned_rounds)
        $ aggressor_name = aggressor.name
        if equippedTrinket("Spirespike") and victim == pc:
            if thorned_rounds == 5:
                "[aggressor_name!t] is wounded from the thorns, losing [thorned_rounds] HP. Spirespike sprouts five thorns around you."
            else:
                "[aggressor_name!t] is wounded from the thorns, losing [thorned_rounds] HP. Five more thorns are added from Spirespike."
        else:
            "[aggressor_name!t] is wounded from the thorns, losing [thorned_rounds] HP."


    $ victim.restore(hp=-damage)
    if victim.hp < 0:
        $ victim.hp = 0

    return

label beginningBattle:
    if pc.hp <= 0:
        $ pc.hp = 1
    $ grip_strength = 100
    $ status = []
    $ battleTurn = "Player"
    $ extra_dodge = 0
    $ extra_lust_dodge = 0
    $ extra_damage = 0
    $ extra_accuracy = 0
    $ alluring_lust = 0
    $ buffed_attack = 0
    if ally == None or ally_num != 2:
        $ ally = None
        $ ally_num = 1
    else:
        $ ally_num = 2
    $ enemy.max_mp = 50
    $ enemy.mp = 50
    if enemy.item_drop01 == None:
        $ enemy.item_drop01 = []
    if enemy2 != None and enemy2.item_drop01 == None:
        $ enemy2.item_drop01 = []

    if pc.checkEquipped("Idol of Virtue"):
        $ temp_pcdamage = pc.damage
        $ pc.damage = pc.level*1 + 2*(pc.stg+pc.cha) + pc.cha
    if enemy_num == 1:
        $ enemies = [enemy]
        $ enemy.item_chance01 = 0.5

    elif enemy_num == 2:
        $ enemies = [enemy, enemy2]
        $ enemy2.max_mp = 50
        $ enemy2.mp = 50
    if equippedTrinket("Eversprout"):
        $ temp_max_hp = pc.max_hp
        $ eversprout_growth = 0
        $ eversprout_penalty = 20 + int(temp_max_hp*0.3) + pc.ten*8
        $ pc.hp = max(1, pc.hp - eversprout_penalty)
    hide screen menu_buttons
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    stop music fadeout 1.0
    $ renpy.music.queue(mBattleIn, loop=False, fadein=1.0)
    $ renpy.music.queue(mBattle, loop=True)
    $ AbilityTab = False
    $ ItemTab = False
    return

label Battle_End_Check:
    $ timenow.addTime(0, 0, 3)
    if adorned in status:
        $ adorned.selfUpdate()
        if adorned.rounds == 0:
            $ alluring_lust = 0
            $ status.remove(adorned)
    if empowered in status:
        $ empowered.selfUpdate()
        if empowered.rounds == 0:
            $ extra_damage -= empowered.effect
            $ status.remove(empowered)
    if bruised in status:
        $ bruised.selfUpdate()
        if bruised.rounds == 0:
            $ status.remove(bruised)
    if fortify == True:
        $ fortify = False
        $ pc.defense -= 30
    if pb_round > 0:
        $ pb_round -= 1
    if accuracy_using > 0:
        $ accuracy_using -= 1
        if accuracy_using == 0:
            $ extra_accuracy = 0



    if silenced in status:
        $ silenced.selfUpdate()
        if silenced.rounds == 0:
            $ status.remove(silenced)
    if wounded in status:
        $ wounded_damage = wounded.rounds * wounded.effect
        call Damaging (enemy, pc, wounded_damage) from _call_Damaging_13
        "Your health decreases by [wounded_damage] from the bleeding."
        $ wounded.selfUpdate()
        if wounded.rounds == 0:
            $ status.remove(wounded)
    if trapped in status:
        $ trapped.selfUpdate()
        if trapped.rounds == 0:
            $ extra_dodge += pc.dodge/2
            $ extra_lust_dodge += pc.lust_dodge/2
            $ status.remove(trapped)

    if pc.weapon != None and pc.weapon.img == "Crystal Staff":
        $ pc.mp += 5
        if pc.mp >= pc.max_mp:
            $ pc.mp = pc.max_mp

    if equippedTrinket("Eversprout") and pc.hp > 0:
        $ eversprout_growth += max(0, int(temp_max_hp*0.03 + pc.ten*7))
        $ pc.max_hp = temp_max_hp + eversprout_growth
        $ pc.hp += max(0, pc.ten*5)
        if pc.hp > pc.max_hp:
            $ pc.hp = pc.max_hp

    $ isCharmed = next((x for x in status if x.img == "Charmed"), None)
    if isCharmed != None:
        $ charmed_damage = isCharmed.rounds * isCharmed.effect
        $ pc.lust += charmed_damage
        "Your lust increases by [charmed_damage] by the charm."
        $ isCharmed.selfUpdate()
        if isCharmed.rounds == 0:
            $ status.remove(isCharmed)

    $ isFrozen = next((x for x in status if x.img == "Frozen"), None)
    if isFrozen != None:
        if isFrozen.rounds >= 30:
            $ frozen_damage = isFrozen.rounds * isFrozen.effect
            $ pc.restore(hp = -damageFormula(frozen_damage, pc.defense))
            "Your health decreases by [frozen_damage] HP from the frostbite."
        if renpy.random.random()*100 < isFrozen.rounds:
            "You are stunned for the next round."
            jump expression enemy.img.lower().replace(" ","") + "_battle_loop"
        $ isFrozen.selfUpdate()
        if isFrozen.rounds == 0:
            $ status.remove(isFrozen)

    $ isMended = next((x for x in status if x.img == "Mended"), None)
    if isMended != None:
        $ healamount = int(tranquilmend_heal*((4-isMended.rounds)**1.2))
        $ isMended.selfUpdate()
        $ pc.hp += healamount
        if pc.hp >= pc.max_hp:
            $ pc.hp = pc.max_hp
        "You healed [healamount] from Traquil Mend!"
        if isMended.rounds == 0:
            $ status.remove(isMended)

    if ally_num == 2:
        $ isMended = next((x for x in ally.status if x.img == "Mended"), None)
        if isMended != None:
            $ healamount = int(tranquilmend_heal*((3-isMended.rounds)**1.2))
            $ isMended.selfUpdate()
            $ ally.hp += healamount
            if ally.hp >= ally.max_hp:
                $ ally.hp = ally.max_hp
            "[ally.name] healed [healamount] from Traquil Mend!"
            if isMended.rounds == 0:
                $ ally.status.remove(isMended)
        if battleTurn == "Player":
            $ ally.mp += 5
            if ally.mp > ally.max_mp:
                $ ally.mp = ally.max_mp

    $ isScorched = next((x for x in enemy.item_drop01 if x.img == "Scorched"), None)
    if isScorched != None:
        $ isScorched.selfUpdate()

        call Enemy_Damaging (enemy, isScorched.effect) from _call_Enemy_Damaging_6
        "[enemy.name] is still burning, receiving [scorched.effect] HP damage."
        if isScorched.rounds == 0:
            $ enemy.item_drop01.remove(isScorched)
        call Trinket_Weeping_Willow from _call_Trinket_Weeping_Willow_3

    $ isWounded = next((x for x in enemy.item_drop01 if x.img == "Wounded"), None)
    if isWounded != None:
        $ wounded_damage = isWounded.rounds * isWounded.effect
        call Enemy_Damaging (enemy, wounded_damage) from _call_Enemy_Damaging_7
        "[enemy.name]'s health decreases by [wounded_damage] from the bleeding."
        $ isWounded.selfUpdate()
        if isWounded.rounds == 0:
            $ enemy.item_drop01.remove(isWounded)
        call Trinket_Weeping_Willow from _call_Trinket_Weeping_Willow_4

    $ isBruised = next((x for x in enemy.item_drop01 if x.img == "Bruised"), None)
    if isBruised != None:
        $ isBruised.selfUpdate()
        if isBruised.rounds == 0:
            $ enemy.item_drop01.remove(isBruised)

    if enemy_num > 1:
        $ isScorched = next((x for x in enemy2.item_drop01 if x.img == "Scorched"), None)
        if isScorched != None:
            $ isScorched.selfUpdate()

            call Enemy_Damaging (enemy2, isScorched.effect) from _call_Enemy_Damaging_8
            "[enemy2.name] is still burning, receiving [scorched.effect] HP damage."
            if isScorched.rounds == 0:
                $ enemy2.item_drop01.remove(isScorched)
            call Trinket_Weeping_Willow from _call_Trinket_Weeping_Willow_5

        $ isWounded = next((x for x in enemy2.item_drop01 if x.img == "Wounded"), None)
        if isWounded != None:
            $ wounded_damage = isWounded.rounds * isWounded.effect
            call Enemy_Damaging (enemy2, wounded_damage) from _call_Enemy_Damaging_9
            "[enemy2.name]'s health decreases by [wounded_damage] from the bleeding."
            $ isWounded.selfUpdate()
            if isWounded.rounds == 0:
                $ enemy2.item_drop01.remove(isWounded)
            call Trinket_Weeping_Willow from _call_Trinket_Weeping_Willow_6

        $ isBruised = next((x for x in enemy2.item_drop01 if x.img == "Bruised"), None)
        if isBruised != None:
            $ isBruised.selfUpdate()
            if isBruised.rounds == 0:
                $ enemy2.item_drop01.remove(isBruised)



    if abilities[0] != None and abilities[0].coolDownTimer > -2:
        $ abilities[0].coolDownTimer -= 1
    if abilities[1] != None and abilities[1].coolDownTimer > -2:
        $ abilities[1].coolDownTimer -= 1
    if abilities[2] != None and abilities[2].coolDownTimer > -2:
        $ abilities[2].coolDownTimer -= 1



    return

label Battle_Mid_Check:
    if stunned in target.item_drop01:
        $ oa[0] = "T"
        $ target.item_drop01.remove(stunned)
    if (oa[0] == "A" or oa[0] == "S") and oa[1] == "S":
        call Trinket_Weeping_Willow from _call_Trinket_Weeping_Willow_7
    if enemy_num == 1:
        if target.hp < 0:
            $ target.hp = 0
        if check_party(target) == "lost":
            $ oa[0] = "W"
    if enemy_num == 2:
        if enemy.hp < 0:
            $ enemy.hp = 0
        if enemy2.hp < 0:
            $ enemy2.hp = 0
        if enemy.lust > enemy.max_lust:
            $ enemy.lust = enemy.max_lust
        if enemy2.lust > enemy2.max_lust:
            $ enemy2.lust = enemy2.max_lust
        if check_party(enemy) == "lost" and check_party(enemy2) == "lost":
            $ oa[0] = "W"
    return

label Battle_Finish:
    $ renpy.music.play(mBattleOut, loop=False, fadeout=1.0)
    $ timenow.addTime(0, 0, 40)
    if equippedTrinket("Eversprout"):
        $ pc.max_hp = temp_max_hp
        $ eversprout_growth = 0
        if pc.hp >= pc.max_hp:
            $ pc.hp = pc.max_hp
    hide screen battle_enemy_stat
    hide screen battle_buttons
    hide screen battle_player_stat
    if pc.checkEquipped("Idol of Virtue"):
        $ pc.damage = temp_pcdamage
    if pc.lust == pc.max_lust:
        $ pc.lust = 0
    if pc.hp <= 0:
        $ pc.hp = 0
    $ ally = None
    $ ally_num = 1
    $ battleTurn = "Player"
    return

label Battle_Kari:
    $ kari_damage = renpy.random.randint(24, 35)
    $ kari_healing = renpy.random.randint(34, 55)
    if renpy.random.random() < 0.75:
        $ target.hp -= kari_damage

        "After your turn, Kari steps forward and strikes the [enemy.name] with his scepter, dealing [kari_damage] to the [enemy.name]."
        k "Evil monster, now it's the time for you to die!"
        e "H-hey... it probably can't hear you."
    else:

        $ pc.hp += kari_healing
        if pc.hp > pc.max_hp:
            $ pc.hp = pc.max_hp
        "After your turn, Kari uses the power of the flowing water to heal your wound, your HP increases by [kari_healing]."
        k "Hmm... finally get to use my spell, guess it's for you, courier."
        e "Thanks, Kari. You've been a great help."
    return
label Battle_ASF:
    $ fortify = False

    if ally_num == 2 and ally != None and battleTurn == "Player":
        $ battleTurn = "Ally"
        $ mee = pc
    elif ally_num == 2 and ally != None and battleTurn == "Ally":
        $ battleTurn = "Player"
        $ mee = ally
    else:
        $ battleTurn = "Player"
        $ mee = pc


    if enemy_num == 1:
        $ target = enemy

    if check_party(pc) == "lost":
        $ oa[0] = "L"
    elif turn_action == "Attack":
        $ oa[0] = "A"

        if equippedTrinket("Devils Snare"):
            $ raw_damage = renpy.random.randint(int(pc.damage*0.6+pc.lust_damage), int(pc.damage*1.4+pc.lust_damage)) * ((100 + extra_damage) / 100)
        else:
            $ raw_damage = renpy.random.randint(int(mee.damage*0.6), int(mee.damage*1.4)) * ((100 + extra_damage) / 100)
        $ player_damage = damageFormula(raw_damage, target.defense)
        $ crit_damage = int(player_damage * mee.crit_damage*(0.6 + renpy.random.random()*0.55))
        $ rnd = renpy.random.random()
        if equippedTrinket("Lindbloom") and rnd > 0.8:
            $ rnd = 0.8
        if rnd*100 < pc.crit_chance:
            $ oa[2] = "C"
            $ oa[4] = crit_damage
            if equippedTrinket("Shivering Shard"):
                $ extra_dodge -= int((pc.dodge+extra_dodge)*0.15)
        elif pb_round > 0:
            $ oa[2] = "C"
            $ oa[4] = crit_damage*(1+pc.agi/15)
            if equippedTrinket("Shivering Shard"):
                $ extra_dodge -= int((pc.dodge+extra_dodge)*0.15)
        else:
            $ oa[2] = "N"
            $ oa[4] = player_damage
        if rnd*20 + pc.accuracy + extra_accuracy >= target.dodge:
            $ oa[1] = "S"
        elif pb_round > 0:
            $ oa[1] = "S"
        else:
            $ oa[1] = "M"
        $ orbed = next((x for x in status if x.img == "Orbs"), None)


        if oa[1] == "S" and orbed != None:
            $ heal_amount = int(orbed.rounds * pc.itg * (renpy.random.random() + 0.15) * spectralorb.effect * 0.2)
            $ pc.restore(hp = heal_amount)
            "You consumed all the spectral orbs around you and healed yourself for [heal_amount] HP."
            $ status.remove(orbed)

        if pc.weapon != None:
            if pc.weapon.wpn_type == "Sword":
                $ oa[3] = "A"
            elif pc.weapon.wpn_type == "Axe":
                $ oa[3] = "B"
            elif pc.weapon.wpn_type == "Bow":
                $ oa[3] = "C"
        else:
            $ oa[3] = "N"

    elif turn_action == "Struggle":
        $ oa[0] = "S"
        $ raw_damage = renpy.random.randint(int(pc.damage*0.6), int(pc.damage*1.4)) * ((100 + extra_damage) / 100)
        $ player_damage = damageFormula(raw_damage, target.defense) / 5 * 3
        $ oa[4] = player_damage
        call Enemy_Damaging (target, oa[4]) from _call_Enemy_Damaging_10
        if pc.checkEquipped("Idol of Virtue"):
            $ oa[1] = renpy.random.randint(int(pc.ten*2 + (pc.cha + pc.stg)*1),int(pc.ten*3 + (pc.cha + pc.stg)*2))
        else:
            $ oa[1] = renpy.random.randint(int(pc.ten*2 + pc.stg*1),int(pc.ten*3 + pc.stg*2))
        $ grip_strength -= oa[1]
        if equippedTrinket("Lindbloom"):
            $ coolnum = 35
        else:
            $ coolnum = 25
        if pc.agi > renpy.random.randint(2, coolnum):
            $ oa[2] = "S"
            $ grip_strength = 0
        else:
            $ oa[2] = "F"
        if grip_strength <= 0:
            "You break free from the [enemy.name]'s grip."
            $ status.remove(bound)

    elif turn_action == "Flirt":
        $ oa[0] = "F"
        $ raw_flirt = renpy.random.randint(int(mee.lust_damage*0.6), int(mee.lust_damage*1.4 + alluring_lust))
        $ player_flirt = damageFormula(raw_flirt, target.lust_defense)
        $ rnd = renpy.random.random()
        if equippedTrinket("Lindbloom") and rnd > 0.8:
            $ rnd = 0.8
        if rnd*100 < target.lust_dodge:
            $ oa[1] = "M"
        if target == mimic or target == dummy or target == stoneward:
            $ oa[1] = "M"
        else:
            $ oa[1] = "S"
            $ target.lust += player_flirt
        if bound in status:
            $ oa[3] = "B"
            $ grip_strength -= 10
        else:
            $ oa[3] = "A"
        $ oa[4] = player_flirt

    elif turn_action == "Thrash":
        $ oa[0] = "A_T"
        $ raw_damage = renpy.random.randint(int(mee.damage*0.6), int(mee.damage*1.4)) * ((100 + extra_damage) / 100)
        $ player_damage = damageFormula(raw_damage, target.defense)
        $ isWounded = next((x for x in target.item_drop01 if x.img == "Wounded"), None)
        if isWounded != None:
            $ isWounded.rounds += 3
        else:
            $ ApplyStatus(target.item_drop01, wounded, 3)
        $ oa[4] = player_damage
    elif turn_action == "Defend":
        $ oa[0] = "A_D"
        $ pc.defense += fortifying.effect
        $ ally.defense += fortifying.effect
        $ fortify = True
        $ ally.mp -= 15
        return
    elif turn_action == "Strike":
        $ oa[0] = "A_S"
        $ raw_damage = renpy.random.randint(int(ally.damage*0.7), int(ally.damage*1.4 * ((55)/30)))
        $ ally_damage = damageFormula(raw_damage, enemy.defense)
        $ stunned.rounds = stunned.max_rounds
        $ enemy.item_drop01.append(stunned)
        call Damaging (ally, enemy, ally_damage) from _call_Damaging_14
        if bound in status:
            $ oa[1] = "B"
            $ status.remove(bound)
        else:
            $ oa[1] = "NB"
        $ ally.mp -= 15

    elif turn_action == "Escape":
        $ oa[0] = "E"
        if equippedTrinket("Lindbloom"):
            $ coolnum = 2
        else:
            $ coolnum = 0
        $ player_escape_chance = renpy.random.randint(0, pc.dodge - coolnum)
        if player_escape_chance > 5:
            $ oa[1] = "M"
        else:
            $ oa[1] = "S"

    elif turn_action == "Surrender":
        $ oa[0] = "U"
    else:
        $ oa[0] = "I"
    return

label goat_guard_battle:

    if goat_num == 3:
        $ gguard = Monster(_("Goat Warrior"), "Goat Guard", 240, 100, 16, 25, 10, 16, 15, 40, 30, 60)
        $ gguard2 = Monster(_("Goat Warrior"), "Goat Guard2", 240, 100, 16, 25, 10, 16, 15, 40, 30, 60)
        scene kechioeren_training_ground:
            blur 8
    else:
        $ gguard = Monster(_("Goat Guard"), "Goat Guard", 120, 100, 16, 25, 10, 16, 15, 15, 15, 60)
        $ gguard2 = Monster(_("Goat Guard"), "Goat Guard2", 120, 100, 16, 25, 10, 16, 15, 15, 15, 60)
        scene kechioeren:
            blur 8

    $ enemy_num = 2
    $ enemy = gguard
    $ enemy2 = gguard2
    $ enemy.beginbattle()
    $ enemy2.beginbattle()
    $ target = enemy
    call beginningBattle from _call_beginningBattle_3
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    if goat_num == 3:
        if pc.weapon == None:
            "You are facing two goat warriors, they are waving their spear in arrogance, gesturing you to come closer. You hold and clench your fist."
        else:
            "You are facing two goat warriors, they are waving their spear in arrogance, gesturing you to come closer. You hold your [pc.weapon.name!t] in defence."
    else:
        if pc.weapon == None:
            "You are facing two goat guards, they are waving their spear in arrogance, gesturing you to come closer. You hold and clench your fist."
        else:
            "You are facing two goat guards, they are waving their spear in arrogance, gesturing you to come closer. You hold your [pc.weapon.name!t] in defence."
    msg "Press the Target button to change your attack target!"
    jump goat_guard_battle_loop

label goat_guard_battle_loop:
    if enemy.hp > 0:
        if enemy.lust < enemy.max_lust / 3:
            show gg1 e1:
                xalign 0.1
                yalign 0.25
        elif enemy.lust < enemy.max_lust / 3 * 2:
            show gg1 e2:
                xalign 0.1
                yalign 0.25
        else:
            show gg1 e3:
                xalign 0.1
                yalign 0.25
    if enemy2.hp > 0:
        if enemy2.lust < enemy2.max_lust / 3:
            show gg2 e1:
                xalign 0.9
                yalign 0.25
        elif enemy2.lust < enemy2.max_lust / 3 * 2:
            show gg2 e2:
                xalign 0.9
                yalign 0.25
        else:
            show gg2 e3:
                xalign 0.9
                yalign 0.25
    $ fortify = False
    if check_party(pc) == "lost":
        if goat_num == 3:
            k "W-well... I guess it was already remarkable that you made it thus far."
            call Battle_Finish from _call_Battle_Finish_26
            jump Kari_Goat_Practice_Lose
        else:
            call Battle_Finish from _call_Battle_Finish_27
            jump goat_general_lose
    $ players_turn = True
    $ turn_action = ui.interact()
    call Battle_ASF from _call_Battle_ASF_18
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
                if goat_num == 3:
                    if target == gguard:
                        goatguard "Well, like our general says, you need to improve your aiming."
                    else:
                        goatguard2 "That was a bummer, go on and try again, Lusterfolk."
                else:
                    if target == gguard:
                        goatguard "By the order of our general, I won't let you come any closer!"
                    else:
                        goatguard2 "By the order of our general, I won't let you come any closer!"
        else:
            call Enemy_Damaging (target, oa[4]) from _call_Enemy_Damaging_11
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
                "It seems you've hit the goat critically, dealing [oa[4]] HP!"
            $ dia = renpy.random.random()
            if goat_num == 3:
                if target.hp > target.max_hp * 0.5:
                    if target == gguard:
                        goatguard "Lucky hit, you learned that from those Lusterfolks?"
                    else:
                        goatguard2 "That was a good one, but I won't overestimate you."
                else:
                    if dia < 0.33:
                        goatguard "Shit, that hurts. I'm gonna forfeit if I can."
                    elif dia < 0.67:
                        goatguard2 "Hnnnngh....that was n-nothing."
            else:
                if target.hp > target.max_hp * 0.5:
                    if target == gguard:
                        goatguard "Aggghh.... W-what the... You little fur lizard intruder, I'll strike you down without mercy!"
                    else:
                        goatguard2 "Grrrrr! L-lucky hit... Let me teach you how to fight properly!"
                else:
                    if dia < 0.33:
                        goatguard "Ummmph.. How... I-I can't. General, we need... back-up!"
                    elif dia < 0.67:
                        goatguard2 "Hnnnngh....I'm going... to...pass out."
    if oa[3] == "F":
        $ dia = renpy.random.random()
        if dia > 0.334:
            "You turn around and rub your hand all over your own burly cheeks, feeling and brushing against your ass while you shake your hip."
        elif dia > 0.667:
            "You scrape your member lightly, running your claw from your inner thigh to the back of your balls, you tug at it tightly while staring at the goat seductively."
        else:
            "You cup at your fluffy chest, drawing circles around the area of your nipples. You smile at the goat while your chest bounce up and down slightly."
        if oa[1] == "M":
            "You continue your act for about a minute, but the guard doesn't even flinch."
            if goat_num == 3:
                if target == gguard:
                    goatguard "Huh...? What was that for?"
                else:
                    goatguard2 "Now this is a real bummer, I should let you finish it yourself."
            else:
                if target == gguard:
                    goatguard "No... I'm not going to fall for this."
                else:
                    goatguard2 "I closed my eyes..."
        else:
            if gguard.lust > gguard.max_lust / 2:
                if goat_num == 3:
                    if target == gguard:
                        "Within a few seconds you can already see some movements under the goat's loincloth. He doesn't say anything, except for licking his lips. His lust is increased by [player_flirt]."
                        goatguard "...I-if you do this one more time I'm going to grab that huge ass and never let you go..."
                    else:
                        "You notice the goat is floundering, trying his best not to get aroused by your seduction, but it is evident that his flushed face tells it all. His lust is increased by [player_flirt]."
                        goatguard2 "You are w-wasting your time. I'm n-not... I'm not... I- uhh... nooo..."
                else:
                    if target == gguard:
                        "Within a few seconds you can already see some movements under the goat's loincloth. He doesn't say anything, except for licking his lips. His lust is increased by [player_flirt]."
                        goatguard "I'm not sure...what I'm seeing but I got a boner..."
                    else:
                        "You notice the goat is floundering, trying his best not to get aroused by your seduction, but it is evident that his flushed face tells it all. His lust is increased by [player_flirt]."
                        goatguard2 "Argh...Fuck, I knew it, you're too hot for battle practice."
            else:
                if goat_num == 3:
                    if target == gguard:
                        "The goat guard is squirming in reaction to your advance. You can already hear his rapid breathing and grunting, holding his spear tightly. His lust is increased by [player_flirt]."
                        goatguard "N-noooo. I can't think straight now, damn it."
                    else:
                        "You can tell the guard is already playing with himself when his hand goes under his loincloth, staring at your ass intently. His lust is increased by [player_flirt]."
                        goatguard2 "Hnnnngh... I want to say meet me after the session but general is here..."
                else:
                    if target == gguard:
                        "The goat guard is squirming in reaction to your advance. You can already hear his rapid breathing and grunting, holding his spear tightly. His lust is increased by [player_flirt]."
                        goatguard "N-noooo. I c-can't control my mind. Please"
                    else:
                        "You can tell the guard is already playing with himself when his hand goes under his loincloth, staring at your ass intently. His lust is increased by [player_flirt]."
                        goatguard2 "Hnnnngh... I n-need to... come."
    if oa[0] == "E":
        if goat_num == 3:
            "You tries to escape from the situation, but the warriors doesn't let you go..."
        else:
            "You tries to escape from the situation, but the guards doesn't let you go..."
    if oa[0] == "U":
        if goat_num == 3:
            k "W-well... I guess it was already remarkable that you made it thus far."
            call Battle_Finish from _call_Battle_Finish_28
            jump Kari_Goat_Practice_Lose
        else:
            "You fall to your knees, exhausted all your energy, you grasp for breath as you lie on the ground, surrendering yourself to the guards."
            goatguard "Ha... We got him, General. He didn't even have the courage to fight us."
            "The general looks you up and down while the guards sits besides you. Thinking carefully about his next step..."
            call Battle_Finish from _call_Battle_Finish_29
            jump goat_general_lose
    call Ability_Item from _call_Ability_Item_5
    if check_party(gguard) == "lost" and check_party(gguard2) == "lost":
        hide gg1
        hide gg2
        hide screen battle_enemy_stat
        hide screen battle_buttons
        hide screen battle_player_stat
        "As the battle ends, you can see both guards falls unconscious, they're still breathing... luckily."
        if goat_num == 3:
            k "Huh, that was unexpected. Let's see, final battle."
            k "Courier, I'll give you our best, most hardworking solder, Tikhon."
            k "He is agile and can dodge a lot of attacks, probably will give you more of a hard time."
            jump goatranger_battle
        gg "Useless guards."
        show kari masked
        with dissolve
        gg "It's you and me now, courier."
        e "We, don't have to fight... General. We can find Furkan together."
        gg "N-no- nooo I can't..."
        e "Do you not want to find him?"
        gg "You don't even know who you're talking to."
        e "You can introduce yourself."
        gg "..."
        gg "Shut up and fight me now!!"
        "The General is extremely furious right now, you still don't understand his wrath but it seems you have no choice but to raise your weapon..."
        jump goat_general_battle
    if check_party(gguard) == "lost" and target == gguard:
        "The Guard slumps on the ground from exhaustion."
        goatguard "G-general... I- I-I think I'm going to p-pass out..."

        hide gg1
        $ target = gguard2
    if check_party(gguard2) == "lost" and target == gguard2:
        "The othar Guard slumps on the ground from exhaustion."
        goatguard "Sorry, I... I can't take him... G-general."
        hide gg2
        $ target = gguard
    if enemy.hp > 0:
        show gg1:
            linear 0.1 zoom 1.04
            linear 0.05 zoom 1
    if enemy2.hp > 0:
        show gg2:
            linear 0.1 zoom 1.04
            linear 0.05 zoom 1
    if gguard.hp > 0 or gguard.lust == gguard.max_lust:
        $ dia = renpy.random.random()
        if gguard.item_drop01 == "Stunned":
            call Battle_End_Check from _call_Battle_End_Check_18
            $ gguard.item_drop01 = None
        else:
            if dia < 0.75:
                if renpy.random.random()*100 > pc.dodge+extra_dodge:
                    $ raw_damage = int(renpy.random.randint(gguard.min_damage, gguard.max_damage))
                    $ enemy_damage = damageFormula(raw_damage, pc.defense)
                    call Damaging (enemy, pc, enemy_damage) from _call_Damaging_15
                    $ random_chance = renpy.random.random()
                    if random_chance < 0.5:
                        "The goat guard swings his spear towards you, you are not quick enough to dodge his blow. Your health decreases by [enemy_damage] HP."
                    else:
                        "The goat charges at you, hitting you with a kick to the chest. Your health decreases by [enemy_damage] HP."
                else:
                    $ random_chance = renpy.random.random()
                    if random_chance < 0.5:
                        "The goat guard swings his spear towards you, you managed to deflect his spear and dodge the attack."
                    else:
                        "The goat charges at you, trying to kick at your chest but you block the blow and push him back."
            else:
                if renpy.random.random()*100 > pc.lust_dodge + extra_lust_dodge:
                    $ raw_flirt = int(renpy.random.randint(gguard.min_lust_damage, gguard.max_lust_damage))
                    $ enemy_flirt = damageFormula(raw_flirt, pc.lust_defense)
                    $ pc.lust += enemy_flirt
                    if pc.lust > pc.max_lust:
                        $ pc.lust = pc.max_lust
                    $ random_chance = renpy.random.random()
                    if random_chance < 0.5:

                        "The goat scratches at his loincloth, he put two of his fingers across his crotch, tracing the shape of his cock in front of you."
                        if goat_num == 3:
                            goatguard "You thristy? Surrender to our general and maybe you'll have the best time of your life."
                        else:
                            goatguard "Well, come and get some of this."
                        "You gulp at his attempt at seduction."
                        "Admittedly you are extremely aroused, drooling at the thought of how his cock would taste like."
                        "Your lust increased by [enemy_flirt]."
                    else:
                        "The guard stretches his body, flaunting his muscular physiques, you can tell his soft chest is almost bulging in front of you."
                        if goat_num == 3:
                            goatguard "You see how strong of a specimen I am. Come closer to get a better look!"
                        else:
                            goatguard "See? This is what I'm talking about, we won a lot of battle with this down here."
                        "You are stunned by his gorgeous muscles, you mind wanders through scenarios of him being inside your body. Your lust increased by [enemy_flirt]."
                else:
                    $ random_chance = renpy.random.random()
                    if random_chance < 0.5:
                        "The goat scratches at his loincloth, he put two of his fingers across his crotch, tracing the shape of his cock in front of you."
                        if goat_num == 3:
                            goatguard "You thristy? Surrender to our general and maybe you'll have the best time of your life."
                        else:
                            goatguard "Well, come and get some of this."
                        "You stare at him, giving him weird side eyes. You have evaded his attempt at seduction. And the goat seems to feel a little dejected."
                    else:
                        "The guard stretches his body, flaunting his muscular physiques, you can tell his soft chest is almost bulging in front of you."
                        if goat_num == 3:
                            goatguard "You see how strong of a specimen I am. Come closer to get a better look!"
                        else:
                            goatguard "See? This is what I'm talking about, we won a lot of battle with this down here."
                        "His attack at your lust seems to have failed as you stand there and wait for him to finish his taunt. Both of you would never speak about it again."
    if enemy2.hp > 0:
        show gg2:
            linear 0.1 zoom 1.04
            linear 0.05 zoom 1
    if gguard2.item_drop01 == "Stunned":
        $ gguard2.item_drop01 = None
        call Battle_End_Check from _call_Battle_End_Check_19
        jump goat_guard_battle_loop
    if gguard2.hp > 0 or gguard2.lust == gguard2.max_lust:
        $ dia = renpy.random.random()
        if dia < 0.75:
            if renpy.random.random()*100 > pc.dodge+extra_dodge:
                $ raw_damage = int(renpy.random.randint(gguard2.min_damage, gguard2.max_damage))
                $ enemy_damage = damageFormula(raw_damage, pc.defense)
                call Damaging (enemy2, pc, enemy_damage) from _call_Damaging_16
                $ random_chance = renpy.random.random()
                if random_chance < 0.5:
                    "The second goat guard swings his spear towards you, you are not quick enough to dodge his blow. Your health decreases by [enemy_damage] HP."
                else:
                    "The second goat charges at you, hitting you with a kick to the chest. Your health decreases by [enemy_damage] HP."
            else:
                $ random_chance = renpy.random.random()
                if random_chance < 0.5:
                    "The second goat guard swings his spear towards you, you managed to deflect his spear and dodge the attack."
                else:
                    "The second goat charges at you, trying to kick at your chest but you block the blow and push him back."
        elif dia < 0.875 and trapped not in status:
            "While you are calculating your next move, you fall into his trap, your dodges are now reduced by half for 3 rounds."
            $ trapped.rounds = trapped.max_rounds
            $ status.append(trapped)
            $ extra_dodge -= pc.dodge/2
            $ extra_lust_dodge -= pc.lust_dodge/2
        else:

            if renpy.random.random()*100 > pc.lust_dodge + extra_lust_dodge:
                $ raw_flirt = int(renpy.random.randint(gguard2.min_lust_damage, gguard2.max_lust_damage))
                $ enemy_flirt = damageFormula(raw_flirt, pc.lust_defense)
                $ pc.lust += enemy_flirt
                if pc.lust > pc.max_lust:
                    $ pc.lust = pc.max_lust
                $ random_chance = renpy.random.random()
                if random_chance < 0.5:
                    "The second goat scratches at his loincloth, he put two of his fingers across his crotch, tracing the shape of his cock in front of you."
                    if goat_num == 3:
                        goatguard2 "You thristy? Surrender to our general and maybe you'll have the best time of your life."
                    else:
                        goatguard2 "Well, come and get some of this."
                    "You gulp at his attempt at seduction. Admittedly you are extremely aroused, thinking about how his cock would taste like. Your lust increased by [enemy_flirt]."
                else:
                    "The second guard stretches his body, flaunting his muscular physiques, you can tell his soft chest is almost bulging in front of you."
                    if goat_num == 3:
                        goatguard2 "You see how strong of a specimen I am. Come closer to get a better look!"
                    else:
                        goatguard2 "See? This is what I'm talking about, we won a lot of battle with this down here."
                    "You are stunned by his gorgeous muscles, you mind wanders through scenarios of him being inside your body. Your lust increased by [enemy_flirt]."
            else:
                $ random_chance = renpy.random.random()
                if random_chance < 0.5:
                    "The second goat scratches at his loincloth, he put two of his fingers across his crotch, tracing the shape of his cock in front of you."
                    if goat_num == 3:
                        goatguard2 "You thristy? Surrender to our general and maybe you'll have the best time of your life."
                    else:
                        goatguard2 "Well, come and get some of this."
                    "You stare at him, giving him weird side eyes. You have evaded his attempt at seduction. And the goat seems to feel a little dejected."
                else:
                    "The second guard stretches his body, flaunting his muscular physiques, you can tell his soft chest is almost bulging in front of you."
                    if goat_num == 3:
                        goatguard2 "You see how strong of a specimen I am. Come closer to get a better look!"
                    else:
                        goatguard2 "See? This is what I'm talking about, we won a lot of battle with this down here."
                    "His attack at your lust seems to have failed as you stand there and wait for him to finish his taunt. Both of you would never speak about it again."
    call Battle_End_Check from _call_Battle_End_Check_5
    jump goat_guard_battle_loop
label goat_general_battle:

    $ galper = Monster(_("Goat General"), "goat general", 200, 100, 14, 23, 0, 0, 20, 10, 30, 200)
    show goat general:
        xalign 0.5
        yalign 0.25

    $ enemy_num = 1
    $ enemy = galper

    $ enemy.max_hp = 260
    $ enemy.min_damage = 25
    $ enemy.max_damage = 65
    $ enemy.min_lust_damage = 0
    $ enemy.max_lust_damage = 0
    $ enemy.dodge = 25
    $ enemy.defense = 45
    $ enemy.lust_defense = 40
    $ enemy.exp_drop = 200
    $ spell_orb = 0
    $ galper.beginbattle()
    call beginningBattle from _call_beginningBattle_4
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    scene kechioeren:
        blur 8
    if pc.weapon == None:
        "You are facing the General of the Goat Tribe, luckily he seems to be weakened without his magic in the scepter. You hold and clench your fist."
    else:
        "You are facing the General of the Goat Tribe, luckily he seems to be weakened without his magic in the scepter. You hold your [pc.weapon.name!t] in defence."
    jump goat_general_battle_loop
label goat_general_battle_loop:

    show goat general:
        xalign 0.5
        yalign 0.25
    if check_party(pc) == "lost":
        call Battle_Finish from _call_Battle_Finish_30
        jump goat_general_lose
    $ turn_action = ui.interact()
    call Battle_ASF from _call_Battle_ASF_4
    if oa[0] == "A":
        if oa[1] == "M":
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the arm of the general, but he leaps back and avoid the blow by inches."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] at the general's head, but he leaps back and avoid the blow by inches."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the general, but he leaps back and avoid the arrow by inches."
            if oa[3] == "N":
                "You throw your fist at the general, but he leaps back and avoid the blow by inches."
            if renpy.random.random() > 0.5:
                gg "Give up now, and you may live. Dare to battle me... and you die!"
        else:
            call Enemy_Damaging (target, oa[4]) from _call_Enemy_Damaging_12
            if oa[3] == "A" or oa[3] == "B":
                if renpy.random.random() > 0.5:
                    "You slam your [pc.weapon.name!t] at the General's head, your blade grazes through the General's stomach. Drops of blood drips through his body. "
                else:
                    "You slam your [pc.weapon.name!t] at the General's head, knocking him on the ground. He growls at you before getting up, albeit disheveled."
            if oa[3] == "C":
                if renpy.random.random() > 0.5:
                    "You aim and shoot your [pc.weapon.name!t] at the General, the arrow hit right into his shoulder."
                else:
                    "You run while shooting your [pc.weapon.name!t] at the General, knocking him on the ground.He growls at you before getting up, albeit disheveled."
            if oa[3] == "N":
                if renpy.random.random() > 0.5:
                    "You throw your fist at the General, hitting him right across his face. The sheer impact knocks him on the ground."
                else:
                    "You punch into the General's stomach, grabbing him and slam him on the ground hard."
            if oa[2] == "N":
                "His health decreases by [oa[4]] HP."
            else:
                "It seems you've hit the general critically, dealing [oa[4]] HP!"
            $ dia = renpy.random.random()
            if galper.hp > galper.max_hp * 0.5:
                if dia < 0.33:
                    gg "F-fuck... No."
                elif dia < 0.67:
                    gg "Y-you... are a formidable courier, only because I lost my magic..."
            else:
                if dia < 0.33:
                    gg "F-furk... I-I have to w-win this one for him..."
                    gg "Come at me! You Insolence!"
                elif dia < 0.67:
                    gg "I-I can't lose here. N-no, I can't let you win..."
    if oa[0] == "F":
        $ dia = renpy.random.random()
        if dia > 0.334:
            "You turn around and rub your hand all over your own burly cheeks, feeling and brushing against your ass while you shake your hip."
        elif dia > 0.667:
            "You scrape your member lightly, running your claw from your inner thigh to the back of your balls, you tug at it tightly while staring at the goat seductively."
        else:
            "You cup at your fluffy chest, drawing circles around the area of your nipples. You smile at the General while your chest bounce up and down slightly."
        if oa[1] == "M":
            "You continue your act for about a minute, but the General doesn't even flinch."
            gg "No... You are not teasing me while we fight..."
        else:
            if galper.lust > galper.max_lust / 2:
                if renpy.random.random() > 0.5:
                    "Within a few seconds you can already see some movements under the General's loincloth."
                    "He doesn't say anything, except licking his lips. His lust is increased by [player_flirt]."
                    gg "hnnn-nngh..."
                else:
                    "You notice the goat is floundering, trying his best not to get aroused by your seduction."
                    "But it is evident that his flushed face tells it all. His lust is increased by [player_flirt]."
                    gg "no..."
            else:
                if renpy.random.random() > 0.5:
                    "The General is squirming in reaction to your advance."
                    "You can already hear his rapid breathing and grunting, holding his scepter tightly. His lust is increased by [player_flirt]."
                    gg "f-fuck..."
                else:
                    "You can tell the general is already playing with himself when his hand goes under his loincloth, staring at your ass intently. His lust is increased by [player_flirt]."
                    gg "s-stop..."
    if oa[0] == "E":
        "You can't get away from the Tribe..."
    if oa[0] == "U":
        "You fall to your knees, exhausted all your energy, you grasp for breath as you lie on the ground, surrendering yourself to the Goat General."
        gg "I thought you were weak, didn't even expect you'd surrender so easily, Huh."
        "He walks around your weakened form, thinking carefully about his next step..."
        call Battle_Finish from _call_Battle_Finish_31
        jump goat_general_lose
    call Ability_Item from _call_Ability_Item_6
    call Battle_Mid_Check from _call_Battle_Mid_Check_4
    if oa[0] == "W":
        call Battle_Finish from _call_Battle_Finish_32
        jump goat_general_win
    if oa[0] == "T":
        call Battle_End_Check from _call_Battle_End_Check_20
        jump goat_general_battle_loop
    show goat general:
        linear 0.1 zoom 1.04
        linear 0.05 zoom 1
    $ dia = renpy.random.random()
    if dia < 0.33:
        if renpy.random.random()*100 > pc.dodge+extra_dodge:
            $ raw_damage = int(renpy.random.randint(galper.min_damage, galper.max_damage))
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_17
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The General swings his scepter across your body. Your health decreases by [enemy_damage] HP."
            else:
                "The General charges at you, hitting you with a kick to the chest. Your health decreases by [enemy_damage] HP."
        else:
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The General swings his scepter across your body, but you managed to deflect and dodge the attack."
            else:
                "The General charges at you, trying to kick at your chest but you block the blow and push him back."
    elif dia < 0.83 and spell_orb > 0:
        $ spell_amount = spell_orb * 15
        $ spell_damage = spell_orb * 30
        "The General uses his scepter to unleash the power of all his spell orbs around him. The magical aura knocks you off on the ground. Your health decreases by [spell_damage]."
        call Damaging (enemy, pc, spell_damage) from _call_Damaging_18
        $ pc.lust += spell_amount
        if pc.lust > pc.max_lust:
            $ pc.lust = pc.max_lust
        "The strange aura causes you to have a tingly feeling in the crotch as well. Your lust increases by [spell_amount]."
        $ spell_orb -= 1
        "The charge consumes 1 spell orb from the General. He now has [spell_orb] spell orbs."
        gg "Taste my orbs, courier. I'll make sure you- Wait... {size=15}I didn't mean my orbs...{/size}"
    else:
        $ spell_orb += 1
        $ pc.mp -= 10
        if pc.mp < 0:
            $ pc.mp = 0
        "The General drains your mana energy and conjures a spell orb on his side."
        "he is ready to unleash the power any time from now. He now has [spell_orb] spell orbs."
        gg "Finally, someone who I can drain your magic from..."

    call Battle_End_Check from _call_Battle_End_Check_6
    jump goat_general_battle_loop
label goat_general_win:
    $ damp_cave.discovered = True
    scene black
    with dissolve
    pause 1.0
    scene kechioeren
    with dissolve
    hide goat general
    show kari masked
    with dissolve
    "The General falls on the ground... breathlessly panting..."
    $ pc.gold += 100
    $ pc.lvluppt += 1
    $ pc.exp += 1000
    "You've received 300 gold from the general. 1000 Exp and 1 extra level point."
    $ pc.exp += exp_drop
    if pc.exp > pc.expCap and pc.level <= levelCap:
        $ pc.LevelUp()
        msg "You are now Level [pc.level]! Check your inventory to allocate your level points."
    gg "No... n-nonono I can't breath..."
    "The General takes off his mask to gasp for air... he looks at you in exhaustion, seems to be waiting for you to do something."
    show kari normal
    with dissolve
    "You stare at his youthful face, you've never imagined a general would be this... soft and cuddly."
    gg "W-what?"
    e "You look cute."
    gg "F-fuck you."
    e "S-sorry... You alright?"
    gg "No..."
    gg "Be a man and finish me right here, courier."
    "His words shocked you a little, you try to sit besides him and give him a little more comfort."
    e "Don't be dramatic, I'm not here to kill anyone."
    gg "What else do you want."
    "The general is still panting, staring down at the floor in frustration, he is sweating profusing after the battle."
    "And you see bruises all over his body."
    e "I'm sorry I hit you that hard."
    e "I just want to not get seized by you and your guards I guess."
    goatguard2 "G-general! General! I just woke up... are you alright?"
    gg "Y-yes."
    goatguard2 "I think I'm gonna pass out again after making sure you're fine now, g-general."
    "The guard falls asleep again near the general. He scoffs for a moment before looking back at you."
    e "So- Can I ask about your name?"
    gg "W-what?"
    e "Y-your name?"
    k "Kari."
    e "Oh, Hey, Kari. So, what's the matter with Furkan?"
    k "He went missing."
    e "So where is he?"
    k "He didn't tell me. Usually he told me where he'd go."
    k "But no, this time. If he's not kidnapped by someone, I don't know where he is."
    k "That's why I needed to ask you."
    e "O-oh."
    e "I haven't seen him anywhere near here."
    e "But talking about weird, there's one thing I thought about."
    e "The Moss Golem's hand."
    k "Golem?"
    k "Oh."
    k "I think I know where he might be."
    e "W-wait, where?"
    k "The Damp Cave... near the lagoon."
    k "We had two guardians protecting our runes, they went rogue after the rune disappeared."
    k "We know one of them is in the damp cave."
    e "I met one golem when I was exploring the river down there, but it got hostile and I had to put it down."
    k "You're lucky it didn't kill you. The guardian is extremely powerful, if not weakened a bit by the disappearance."
    e "Uhm, it's actually weakened a lot, its hand is gone."
    k "No..."
    k "Then the one in the damp cave must be the left one."
    k "I told Furkan not to get them back, b-but maybe he has another idea."
    k "I just needed to s-save him."
    k "Ah---argh..."
    "He groans loudly."
    with vpunch
    "Kari tries to stand up, but he quickly slump forwards with his injuries in the legs."
    e "H-hey you alright..?"
    k "I- have to go."
    "He tries to stand up again, you grabs his arm to lift him up but he lost his balance and falls again."
    with vpunch
    e "I can help you find Furkan."
    k "Y-you?"
    e "Yes."
    k "W-why? Aren't you on the Lusterfield's side?"
    e "I'm simply a courier, I just wanted to save him."
    e "And I'm sorry again, for your injuries."
    k "N-no..nono. Leave me alone."
    "Kari clutches at his bruised body, and he stares at you with pleading eyes."
    k "But please bring Furkan back..."
    e "Yes, should I take you and the guards back to your house?"
    k "No."
    k "The other guards will have you killed after seeing me like that. Just leave us here."
    e "A-alright..."
    $ QuestBegin(quest11)
    $ quest11.qProgress(__("Visit the Damp Cave"))
    $ kari_accompany = False
    $ damp_cave.discovered = True
    $ quest10.status = 4
    $ quest10.qComp(_("Report to Lothar"))
    jump main_woodland_outpost

label goat_general_lose:
    scene black
    with dissolve
    pause 1.0
    scene kechioeren
    with dissolve
    hide goat general
    show kari masked
    with dissolve
    "You slump back against the ground. Waiting for the general to decide your fate."
    e "S-sorry, can I go now?"
    gg "First, we need to find Furkan."
    gg "Guards, get his bag."
    goatguard "Yes, General."
    "He grabs your bag from his guard and kneels down in front of you."
    gg "Hmm."
    if LookForItem("Mossy Artifact", inventory):
        gg "W-what's this..."
        e "U-uhh, the golem's hand."
        gg "Where did you find this?"
        e "From the river, I killed it."
        gg "You killed it?"
        e "Y-yes..."
    else:
        gg "Nothing useful."
        e "I- uhhh... I think I know something."
        gg "W-what?"
        e "I was in the river some time before, and I saw a golem."
        e "It's really big and it's ready to kill me there, but I defeated it."
        gg "You-... killed it?"
        e "Y-yes."
    "The general looks at you with a little bit of surprise, but he quickly hides it."
    gg "I got it. He's there."

    e "W-what?"
    gg "He's with the Golem."
    e "But we killed it."
    gg "The other one. We have two rune guardians."
    e "W-what happened to them?"
    gg "Our guardians went rogue after the primordial runes stopped supplying spell energy."
    gg "And those guardians were supposed to be guarding the runes, right on top of our mountain."
    e "What do this have to do with where the Golems have been."
    gg "Because Furkan's in the damp cave."
    e "W-what Cave?"
    gg "The one near sparkling lagoon."
    e "Are you sure?"
    gg "Yes."
    gg "But I can't leave the tribe unattended."
    "The general walks back and forth, trying to conjure up a plan to rescue his chief."
    gg "Come with me, courier. I need your help."
    "He points at you, not even waiting for your approval."
    e "Uh... are you sure?"
    gg "I'll tell you everything I know on our way."
    "You feel the general drags your hand, and turns towards the guards."
    gg "Cev and Hakki, stay here until I come back."
    goatguard2 "Yes, General."
    $ QuestBegin(quest11)
    $ quest11.qProgress(__("Visit the Damp Cave with Kari"))
    $ kari_accompany = True
    $ kari_battle_lose = 1
    if pc.hp <= 0:
        $ pc.hp = 1
    jump Kari_Adventure
label lothar_battle:

    "You see Lothar beginning to strip off his upper body armor, he holds his long sword in front of you."
    l "Disciple, do not disappoint me this time. I expect some decent combat before you lose."


    $ enemy_num = 1
    $ enemy = lothspar
    $ enemy.max_hp = 550
    $ enemy.max_damage = 105
    $ enemy.min_damage = 30
    $ enemy.defense = 65
    $ enemy.dodge = 27
    $ enemy.lust_defense = 32
    $ enemy.min_lust_damage = 16
    $ enemy.max_lust_damage = 23
    call beginningBattle from _call_beginningBattle_10
    $ lothspar.beginbattle()
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    scene lusterfield_alleyway:
        blur 8
    show lothar_sprite:
        xalign 0.5
        yalign 0.4

    if pc.weapon == None:
        "You are facing the hero of Lusterfield, Lothar. He seems to be having fun, gloating about his muscles. You hold and clench your fist."
    else:
        "You are facing the hero of Lusterfield, Lothar. He seems to be having fun, gloating about his muscles. You hold your [pc.weapon.name!t] in defence."

    jump lothar_battle_loop
label lothar_battle_loop:

    show lothar_sprite:
        xalign 0.5
        yalign 0.4
    if check_party(pc) == "lost":
        jump lothar_battle_lose
    $ turn_action = ui.interact()
    call Battle_ASF from _call_Battle_ASF_5
    if oa[0] == "A":
        if oa[1] == "M":
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at Lothar's arm, but he leaps back and avoid the blow by inches."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] at Lothar's arm, but he leaps back and avoid the blow by inches."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at Lothar's chest, but he leaps back and avoid the arrow by inches."
            if oa[3] == "N":
                "You throw your fist at Lothar, but he leaps back and avoid the blow by inches."
            if renpy.random.random() > 0.5:
                l "Heh... your aiming needs some training, disciple."
        else:
            call Enemy_Damaging (target, oa[4]) from _call_Enemy_Damaging_13
            if oa[3] == "A" or oa[3] == "B":
                if renpy.random.random() > 0.5:
                    "You slam your [pc.weapon.name!t] at Lothar's body, your blade grazes through the Hero's stomach."
                    "Drops of blood drips along his body."
                else:
                    "You slam your [pc.weapon.name!t] at Lothar's head, knocking him on the ground."
                    "He growls at you before getting up, albeit disheveled."
            if oa[3] == "C":
                if renpy.random.random() > 0.5:
                    "You aim and shoot your [pc.weapon.name!t] at Lothar, the arrow hit right into his shoulder."
                else:
                    "You run while shooting your [pc.weapon.name!t] at Lothar, knocking him on the ground."
                    "He growls at you before getting up, albeit disheveled."
            if oa[3] == "N":
                if renpy.random.random() > 0.5:
                    "You throw your fist at Lothar, hitting him right across his face."
                    "the sheer impact knocks him on the ground."
                else:
                    "You punch into Lothar's stomach, grabbing him and slam him on the ground hard."
            if oa[2] == "N":
                "His health decreases by [oa[4]] HP."
            else:
                "It seems you've hit Lothar critically, dealing [oa[4]] HP!"
            $ dia = renpy.random.random()
            if lothspar.hp > lothspar.max_hp * 0.5:
                if dia < 0.33:
                    l "Lucky h-hit. T-that... was nothing... Agh..."
                elif dia < 0.67:
                    l "I-I can beat you... Heh... so easily, [e]."
            else:
                if dia < 0.33:
                    l "Hnnnnngh... The hero c-can't lose..."
                elif dia < 0.67:
                    l "Fuck... I need some more potions after this..."
    if oa[0] == "F":
        $ dia = renpy.random.randint(1, 4)
        if dia == 1:
            "You turn around and rub your hand all over your own burly cheeks, feeling and brushing against your ass while you shake your hip."
        elif dia == 2:
            "You scrape your member lightly, running your claw from your inner thigh to the back of your balls, you tug at it tightly while staring at Lothar seductively."
        elif dia == 3:
            "You walk towards Lothar, groping at his chest like he did with Amble."
        else:
            "You cup at your fluffy chest, drawing circles around the area of your nipples. You smile at Lothar while your chest bounce up and down slightly."
        if oa[1] == "M":
            "You continue your act for about a minute, but Lothar doesn't even flinch."
            l "Your flirting... well... that was embarrassing..."
        else:
            if lothspar.lust > lothspar.max_lust / 2:
                if renpy.random.random() > 0.5:
                    "Within a few seconds you can already see some movements behind Lothar's underwear."
                    "He stares at your alluring pose while licking his lips. His lust is increased by [player_flirt]."
                    l "Hmm... Disciple, since when did you become... so fuckable..."
                else:
                    "You notice the wolf is floundering, trying his best not to get aroused by your seduction."
                    "But it is evident that his flushed face tells it all. His lust is increased by [player_flirt]."
                    l "Get it over with... Lot. You're a hero, not a lustful beast..."
            else:
                if renpy.random.random() > 0.5:
                    "Lothar is squirming in reaction to your advance."
                    "You can already hear his rapid breathing and grunting, while holding his sword tightly. His lust is increased by [player_flirt]."
                    l "F-fuck... I n-need your ass... d-discip-"
                else:
                    "You can tell Lothar is already playing with himself when his hand goes under his pants, staring at your ass intently."
                    "Lothar's legs are trembling, his bulge only gets bigger after he removes his hand."
                    "His lust is increased by [player_flirt]."
                    l "S-stop... disciple. I can literally fuck your mouth r-right here..."
    if oa[0] == "E":
        e "H-hey... Lothar, I need to take some rest..."
        l "After this, disciple."
        "It seems the hero doesn't allow you to escape."
    if oa[0] == "U":
        "You fall to your knees, exhausted all your energy, you grasp for breath as you lie on the ground, surrendering yourself to Lothar."
        l "Really...?"
        l "Disciple... You disappointed me, I never expected my student to surrender so easily."
        l "But oh well, it may be your only option facing the one and only almighty hero of Lusterfield... Heh."
        "He walks around your weakened form, thinking carefully about his next step."
        jump lothar_battle_lose
    call Ability_Item from _call_Ability_Item_7
    call Battle_Mid_Check from _call_Battle_Mid_Check_5
    if oa[0] == "W":
        call Battle_Finish from _call_Battle_Finish_33
        jump lothar_battle_win
    if oa[0] == "T":
        call Battle_End_Check from _call_Battle_End_Check_21
        jump lothar_battle_loop
    show lothar_sprite:
        linear 0.1 zoom 1.04
        linear 0.05 zoom 1
    jump lothar_battle_loop2
label lothar_battle_loop2:
    if stunned in status:
        $ status.remove(stunned)
    $ dia = renpy.random.random()
    if dia < 0.3:
        if renpy.random.random()*100 > pc.dodge+extra_dodge:
            $ raw_damage = int(renpy.random.randint(lothspar.min_damage, lothspar.max_damage))
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_19
            $ random_chance = renpy.random.random()
            $ dia = renpy.random.random()
            if random_chance < 0.5:
                "Lothar slams his sword down, and you fall on the ground."
                "He stomps on your chest. Your health decreases by [enemy_damage] HP."
            else:
                "Lothar charges at you, kicking you hard. Your health decreases by [enemy_damage] HP."
            if dia < 0.33:
                l "Heh... Taste the mighty feet of the hero..."
            elif dia < 0.67:
                l "Your inexperience really shows, disciple."
            else:
                l "Now I've shown you what's real power, compared to your inferior battle tactics."
        else:
            $ random_chance = renpy.random.random()
            $ dia = renpy.random.random()
            if random_chance < 0.5:
                "Lothar slams his sword down on you, but you managed to dodge in time, his sword strikes the ground and sparks fly."
            else:
                "Lothar charges at you, trying to kick at your chest but you quickly roll backwards and dodge the attack."
            if dia < 0.33:
                l "Lucky... that was so lucky of you..."
            elif dia < 0.67:
                l "Come back here and let me slam your fucking ass!"
    elif dia < 0.6:
        $ random_chance = renpy.random.random()
        if random_chance < 0.5:
            "The hero scratches at his groin, he put two of his fingers across his crotch, tracing the shape of his cock in front of you."
            "Lothar approaches you with his hard-on..."
            l "Don't lie... Disciple, you must be wanting my cock inside of you, don't you...?"
        else:
            "Lothar stretches his body, flaunting his muscular physiques, you can tell his soft chest is almost bulging in front of you."
            l "Well... It seems that you can't move your eyes away from... the hero right here."
        if renpy.random.random()*100 > pc.lust_dodge + extra_lust_dodge:
            $ raw_flirt = int(renpy.random.randint(lothspar.min_lust_damage, lothspar.max_lust_damage))
            $ enemy_flirt = damageFormula(raw_flirt, pc.lust_defense)
            $ pc.lust += enemy_flirt
            if pc.lust > pc.max_lust:
                $ pc.lust = pc.max_lust
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "You gulp at his attempt at seduction. Admittedly you are extremely aroused, thinking about how his cock would taste like. Your lust increased by [enemy_flirt]."
            else:
                "You are stunned by his gorgeous muscles, you mind wanders through scenarios of Lothar being inside your body. Your lust increased by [enemy_flirt]."
        else:
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "You stare at him, giving him weird side eyes. You have evaded his attempt at seduction. And Lothar seems to feel a little dejected."
            else:
                "His attack at your lust seems to have failed as you stand there and wait for him to finish his taunt. Both of you would never speak about it again."

    elif enemy.hp < enemy.max_hp / 2:
        l "Let me... drink this premium health potion first..."
        $ heal_amount = 75
        call Enemy_Self_Healing (lothspar, heal_amount) from _call_Enemy_Self_Healing_5
    else:

        "Lothar raises his sword, and strikes you with his full force. Your health decreases by [enemy_damage] HP."
        $ raw_damage = int(renpy.random.randint(lothspar.min_damage, lothspar.max_damage))
        $ enemy_damage = damageFormula(raw_damage, pc.defense)
        call Damaging (enemy, pc, enemy_damage) from _call_Damaging_20
        "The sheer impact of his blow knocks you on the ground."
        "You are stunned for a round."
        $ status.append(stunned)
    call Battle_End_Check from _call_Battle_End_Check_7
    if stunned in status:
        jump lothar_battle_loop2
    jump lothar_battle_loop

label lothar_battle_lose:
    hide screen battle_buttons
    hide screen battle_enemy_stat
    hide screen battle_player_stat
    scene lusterfield_alleyway
    with dissolve
    show lothar grin
    with dissolve
    $ lothspar.lose += 1
    l "Heh... look at you... Disciple."
    if pc.hp <= 0:
        "You kneel on the grass, and pant heavily. You've exhausted all the energy in your body."
        "You look up and see Lothar smiling."
        e "F-fuck... my legs..."
        l "Another win right into my pocket! Not surprising, actually."
        l "Not one bit surprising considering your physique."
        e "C-can I get some rest?"
        l "Some rest, heh well. Easiest 500 Gold I've got."
        l "Pay me back any time. Before I hand you to Cane and his clients."
        l "Maybe I'll consider sparring with you again after that. maybe."
    if pc.lust >= pc.max_lust:
        "You kneel on the grass, and pant heavily. There is an immediate urge to satisfy your own lust in front of Lothar."
        "You look up and see Lothar smiling."
        e "F-fuck... me- Lothar..."
        l "Another win right into my pocket! Not surprising, actually."
        l "Not one bit surprising considering your mental strength."
        e "Ahhh- I'm so... horny. C-can I get... some rest?"
        l "Some rest, heh well. Easiest 500 Gold I've got."
        l "Pay me back any time. Before I hand you to Cane and his clients..."
        l "Maybe I'll consider sparring with you again after that... maybe."
    e "Hmm..."
    l "..."
    l "You alright?"
    e "N-no."
    "You lie on the ground, breathing rapidly... and you can feel two strong arms are lifting you upwards."
    "Lothar carries your whole body on his warm back, you instantly grasp on his fur for support."
    e "Thanks... Lothar."
    l "Ugh... Now you can't say I'm a bad mentor..."
    "The hero awkwardly walks, his hands grazes across your bottom and you instantly squirm under your breath."
    l "It's for support."
    "He holds onto you more tightly, as your whole weight sinks onto his hands under your butt."
    "As much as you want to deny, his soft back feels like a dream to sleep on, slowly, you lost consciousnes-"
    l "Stop it disciple... I didn't remember hitting you that hard..."
    "Lothar smacks you before you fall asleep, apparently, you two have reached the entrance of the shop."
    e "Hmmm...?"
    l "Get down."
    e "C-can you bring me to my bed...?"
    l "I don't want to see the lion..."
    l "..."
    "The hero doesn't say anything, he only knocks on the door with the other hand and enters the shop."
    "There are a few customers in the shop, you can see Sebas and Ole glancing at you two before Lothar enters your room."
    l "So..."
    "Lothar throws you on the bed, luckily it's soft and bouncy, else you think you might get a concussion on top of your exhaustion."
    l "I've done my duty. Take some rest."
    e "Lot...?"
    l "Hmm, call me Lothar... but whatever..."
    e "Thank you for carrying me back here."
    l "Well... It's just one street across."
    l "Plus, I've never had a disciple before."
    l "Not those two, they're too strong to be a disciple."
    l "So, you should be grateful..."
    e "Thanks again..."
    "Lothar smiles at you before turning back and closing the door."
    "You can hear muttering between Lothar and the two shopowners, but more quickly so, you drift off to sleep."
    "..."
    "You wake up some time later, not knowing what time it is... but you look out and you see the sun shining..."
    "It should be morning..."
    "You get out of bed, glancing at your hand you see a strip of grey fur in your palm. It was still warm."
    "You still can't decide whether Lothar is a good teacher..., but you can still remember the tickly feeling when he carried you to your bed..."
    $ quest12.status = 4
    $ quest12.qComp(_("Report to Lothar"))
    $ timenow.day += 1
    $ timenow.hour = 7
    if pc.hp <= 0:
        $ pc.hp = 1
    jump main_bedroom
label lothar_battle_win:
    scene lusterfield_alleyway
    with dissolve
    show lothar angry
    with dissolve
    $ lothspar.win += 1
    if enemy.hp <= 0:
        l "Fuck..."
        l "A-ahhh."
        e "Lothar... You alright...?"
        "Lothar lies on the ground, still panting heavily as he loosens his grip on his sword."
        l "No. Fuck..."
        e "It's alright... It was just a sparring..."
        l "Fuck you, I've never seen any disciple hitting their hero this hard."
    if enemy.lust >= enemy.max_lust:
        l "Fuck..."
        l "A-ahhh....Why are you so fuckable..."
        e "Lothar, You alright...?"
        "Lothar lies on the ground, still panting heavily as he loosens his grip on his sword."
        l "No. Fuck..."
        e "It's alright... It was just a sparring..."
        l "Fuck you, I've never seen any disciple trying this hard to get their ass fucked."
        l "If I were not sober I'll literally grab your ass and eat it right here."
    l "And, you're just lucky because I was drunk last night."
    e "Aren't you drunk every night...?"
    l "No. Whatever, maybe I underestimated you, but if I'm in serious state, you can't even touch me!"
    l "Fuck..."
    e "About the be-"
    l "No bet, fuck off, and let me rest..."
    e "Lot...?"
    l "I said no bet."
    e "Do you need a hand?"
    l "No. Now leave me alone..."
    "You look at Lothar, who is clutching at his stomach while moaning lightly."
    "As much as you want to get closer with him. He obviously doesn't want your help."
    "Maybe he'll get over it soon, after recovering from your sparring."
    "Or he'll continue acting out his frustration on you... For whatever reason."
    "For now, you feel it's not your place to stay. So you glance at him one more time before getting back to the main road."
    $ quest12.status = 5
    $ quest12.qComp(_("Wait for a day and Report to Lothar"))
    $ timenow.hour += 3
    $ lothar_rest = timenow.day
    jump main_lusterfield01
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
