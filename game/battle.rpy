style button_text2:
    size 40
    idle_color "#ffffff"
    hover_color "#351208"
    font "chaparral.otf"
    outlines [ (absolute(1), "#351208", absolute(0), absolute(0))]

style button_text3:
    size 40
    idle_color "#171417"
    hover_color "#351208"
    font "chaparral.otf"
    outlines [ (absolute(1), "#351208", absolute(0), absolute(0))]

style enemy_text2:
    size 35
    color "#ffffff"
    font "chaparral.otf"
    outlines [ (absolute(1), "#351208", absolute(0), absolute(0))]

style button2:
    xpadding 20
    ypadding 10


screen battle_player_stat():

    if len(status) > 0:
        for i in range(len(status)):
            $ j = status[i]
            $ xNum = 0.195 + i*0.05
            $ xNum2 = 0.225 + i*0.05
            vbox:
                xalign xNum
                yalign 0.705
                imagebutton:
                    idle j.img.lower()
                    hovered SetVariable("selected_status", i)
                    unhovered SetVariable("selected_status", None)
                    action NullAction()
            text "[j.rounds]" xalign xNum2 yalign 0.695 color "#eeeeee" outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
    if selected_status != None:
        $ k = status[selected_status]
        frame:
            xalign xNum
            yalign 0.615
            xmaximum 1000
            xpadding 20
            ypadding 10
            label _("[k.description] Expires in [k.rounds] rounds.") text_color "#eeeeee"

    if ally_num == 2:
        if len(ally.status) > 0:
            for i in range(len(ally.status)):
                $ j = ally.status[i]
                $ xNum = 0.825 - i*0.05
                $ xNum2 = 0.84 - i*0.05
                vbox:
                    xalign xNum
                    yalign 0.705
                    imagebutton:
                        idle j.img.lower()
                        hovered SetVariable("selected_ally_status", i)
                        unhovered SetVariable("selected_ally_status", None)
                        action NullAction()
                text "[j.rounds]" xalign xNum2 yalign 0.685 color "#eeeeee" outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
        if selected_ally_status != None:
            $ k = ally.status[selected_ally_status]
            frame:
                xalign xNum
                yalign 0.615
                xmaximum 1000
                xpadding 20
                ypadding 10
                label _("[k.description] Expires in [k.rounds] rounds.") text_color "#eeeeee"

screen battle_enemy_stat():














    if enemy_num == 1:
        if enemy.item_drop01 != None and len(enemy.item_drop01) > 0:
            for i in range(len(enemy.item_drop01)):
                $ j = enemy.item_drop01[i]
                $ xNum = 0.245 + i*0.05
                $ xNum2 = 0.275 + i*0.05
                vbox:
                    xalign xNum
                    yalign 0.155
                    imagebutton:
                        idle j.img.lower()
                        hovered SetVariable("selected_enemy_status", i)
                        unhovered SetVariable("selected_enemy_status", None)
                        action NullAction()
                text "[j.rounds]" xalign xNum2 yalign 0.155 color "#eeeeee" outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]

        if enemy.item_drop01 != None and selected_enemy_status != None and selected_enemy_status < len(enemy.item_drop01):
            $ k = enemy.item_drop01[selected_enemy_status]
            frame:
                xalign xNum
                xmaximum 1000
                yalign 0.235
                xpadding 20
                ypadding 10
                label _("[k.description] Expires in [k.rounds] rounds.") text_color "#eeeeee"

        vbox:
            xalign 0.3
            yalign 0.01
            xmaximum 300
            frame:
                xminimum 80
                xmaximum 300
                yminimum 100
                ymaximum 150
                vbox:
                    spacing 10
                    text "[enemy.name!t]" xalign 0.1 yalign 0.5 style "enemy_text2"
                    bar value AnimatedValue(enemy.hp, enemy.max_hp) left_bar Frame("left_red", 6, 6)
                    bar value AnimatedValue(enemy.lust, enemy.max_lust) left_bar Frame("left_yellow", 6, 6)
                vbox:
                    xalign 0.06
                    yalign 0.775
                    spacing 25
                    text _("HP: [enemy.hp] / [enemy.max_hp]") size 20
                    text _("LUST: [enemy.lust] / [enemy.max_lust]") size 20
    elif enemy_num == 2:
        if ally_num == 2:
            $ enemy2_status_xalign = 0.79
            $ enemy2_status_num_xalign = 0.81
            $ enemy2_xalign = 0.64
            $ enemy2_target_xalign = 0.75
        else:
            $ enemy2_status_xalign = 0.885
            $ enemy2_status_num_xalign = 0.905
            $ enemy2_xalign = 0.99
            $ enemy2_target_xalign = 0.81
        if len(enemy.item_drop01) > 0:
            for i in range(len(enemy.item_drop01)):
                $ j = enemy.item_drop01[i]
                $ xNum = 0.195 + i*0.05
                $ xNum2 = 0.23 + i*0.05
                vbox:
                    xalign xNum
                    yalign 0.155
                    imagebutton:
                        idle j.img.lower()
                        hovered SetVariable("selected_enemy_status", i)
                        unhovered SetVariable("selected_enemy_status", None)
                        action NullAction()
                text "[j.rounds]" xalign xNum2 yalign 0.155 color "#eeeeee" outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]

        if enemy.item_drop01 != None and selected_enemy_status != None and selected_enemy_status < len(enemy.item_drop01):
            $ k = enemy.item_drop01[selected_enemy_status]
            frame:
                xalign 0.5
                xmaximum 1000
                yalign 0.235
                xpadding 20
                ypadding 10
                label _("[k.description] Expires in [k.rounds] rounds.") text_color "#eeeeee"
        if enemy2.item_drop01 != None and len(enemy2.item_drop01) > 0:
            for i in range(len(enemy2.item_drop01)):
                $ j = enemy2.item_drop01[i]
                $ xNum = enemy2_status_xalign + i*0.05
                $ xNum2 = enemy2_status_num_xalign + i*0.05
                vbox:
                    xalign xNum
                    yalign 0.155
                    imagebutton:
                        idle j.img.lower()
                        hovered SetVariable("selected_enemy2_status", i)
                        unhovered SetVariable("selected_enemy2_status", None)
                        action NullAction()
                text "[j.rounds]" xalign xNum2 yalign 0.155 color "#eeeeee" outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]

        if enemy2.item_drop01 != None and selected_enemy2_status != None and selected_enemy2_status < len(enemy2.item_drop01):
            $ k = enemy2.item_drop01[selected_enemy2_status]
            frame:
                xalign 0.5
                xmaximum 1000
                yalign 0.235
                xpadding 20
                ypadding 10
                label _("[k.description] Expires in [k.rounds] rounds.") text_color "#eeeeee"
        vbox:
            xalign 0.25
            yalign 0.01
            xmaximum 300
            frame:
                xminimum 80
                xmaximum 300
                yminimum 100
                ymaximum 150
                vbox:
                    spacing 10
                    text "[enemy.name!t]" xalign 0.1 yalign 0.5 style "enemy_text2"
                    bar value AnimatedValue(enemy.hp, enemy.max_hp) left_bar Frame("left_red", 6, 6)
                    bar value AnimatedValue(enemy.lust, enemy.max_lust) left_bar Frame("left_yellow", 6, 6)
                vbox:
                    xalign 0.06
                    yalign 0.775
                    spacing 25
                    text _("HP: [enemy.hp] / [enemy.max_hp]") size 20
                    text _("LUST: [enemy.lust] / [enemy.max_lust]") size 20
        vbox:
            xalign enemy2_xalign
            yalign 0.01
            xmaximum 300
            frame:
                xminimum 80
                xmaximum 300
                yminimum 100
                ymaximum 150
                vbox:
                    spacing 10
                    text "[enemy2.name!t]" xalign 0.1 yalign 0.5 style "enemy_text2"
                    bar value AnimatedValue(enemy2.hp, enemy2.max_hp) left_bar Frame("left_red", 6, 6)
                    bar value AnimatedValue(enemy2.lust, enemy2.max_lust) left_bar Frame("left_yellow", 6, 6)
                vbox:
                    xalign 0.06
                    yalign 0.775
                    spacing 25
                    text _("HP: [enemy2.hp] / [enemy2.max_hp]") size 20
                    text _("LUST: [enemy2.lust] / [enemy2.max_lust]") size 20
        if enemy.hp > 0 and enemy2.hp > 0:
            frame:
                xalign 0.4
                yalign 0.05
                has button
                action SetVariable("target", enemy)
                text _("Target") style "button_text"
            frame:
                xalign enemy2_target_xalign
                yalign 0.05
                has button
                action SetVariable("target", enemy2)
                text _("Target") style "button_text"

screen battle_buttons():

    frame:
        xalign 0.02
        yalign 0.02
        xpadding 20
        ypadding 20
        xmaximum 300
        xminimum 80
        ymaximum 800
        yminimum 100
        vbox:
            style "button2"
            spacing 12
            xmaximum 400
            if bound in status:
                if battleTurn == "Player":
                    hbox:
                        spacing 10
                        imagebutton:
                            action Return("Struggle")
                            idle "battle_attack"
                        button:
                            yalign 0.5
                            action Return("Struggle")
                            text _("Struggle") style "button_text2"
                else:
                    hbox:
                        spacing 10
                        imagebutton:
                            action NullAction()
                            idle "battle_attack"
                        button:
                            yalign 0.5
                            action NullAction()
                            text _("Struggle") style "button_text3"
            else:
                if battleTurn == "Player":
                    hbox:
                        spacing 10
                        imagebutton:
                            action Return("Attack")
                            idle "battle_attack"
                        button:
                            yalign 0.5
                            action Return("Attack")
                            text _("Attack") style "button_text2"
                else:
                    hbox:
                        spacing 10
                        imagebutton:
                            action NullAction()
                            idle "battle_attack"
                        button:
                            yalign 0.5
                            action NullAction()
                            text _("Attack") style "button_text3"
            if bound in status:
                if battleTurn == "Player":
                    hbox:
                        spacing 10
                        imagebutton:
                            action Notify("You are still Bound. You cannot use any abilities.")
                            idle "battle_ability"
                        button:
                            yalign 0.5
                            action Notify("You are still Bound. You cannot use any abilities.")
                            text _("Ability") style "button_text2"
                else:
                    hbox:
                        spacing 10
                        imagebutton:
                            action NullAction()
                            idle "battle_ability"
                        button:
                            yalign 0.5
                            action NullAction()
                            text _("Ability") style "button_text3"
            else:
                if battleTurn == "Player":
                    hbox:
                        spacing 10
                        imagebutton:
                            action ToggleVariable("AbilityTab")
                            idle "battle_ability"
                        button:
                            yalign 0.5
                            action ToggleVariable("AbilityTab")
                            text _("Ability") style "button_text2"
                else:
                    hbox:
                        spacing 10
                        imagebutton:
                            action NullAction()
                            idle "battle_ability"
                        button:
                            yalign 0.5
                            action NullAction()
                            text _("Ability") style "button_text3"
            if battleTurn == "Player":
                if pc.checkEquipped("Idol of Virtue"):
                    hbox:
                        spacing 10
                        imagebutton:
                            action Notify("You cannot flirt with the enemy while wearing Idol of Virtue.")
                            idle "battle_flirt"
                        button:
                            yalign 0.5
                            action Notify("You cannot flirt with the enemy while wearing Idol of Virtue.")
                            text _("Flirt") style "button_text2"
                else:
                    hbox:
                        spacing 10
                        imagebutton:
                            action Return("Flirt")
                            idle "battle_flirt"
                        button:
                            yalign 0.5
                            action Return("Flirt")
                            text _("Flirt") style "button_text2"
                hbox:
                    spacing 10
                    imagebutton:
                        action Return("Surrender")
                        idle "battle_surrender"
                    button:
                        yalign 0.5
                        action Return("Surrender")
                        text _("Surrender") style "button_text2"
                hbox:
                    spacing 10
                    imagebutton:
                        action ToggleVariable("ItemTab")
                        idle "battle_item"
                    button:
                        yalign 0.5
                        action ToggleVariable("ItemTab")
                        text _("Item") style "button_text2"
                hbox:
                    spacing 10
                    imagebutton:
                        action Return("Escape")
                        idle "battle_escape"
                    button:
                        yalign 0.5
                        action Return("Escape")
                        text _("Escape") style "button_text2"
            else:
                hbox:
                    spacing 10
                    imagebutton:
                        action NullAction()
                        idle "battle_flirt"
                    button:
                        yalign 0.5
                        action NullAction()
                        text _("Flirt") style "button_text3"
                hbox:
                    spacing 10
                    imagebutton:
                        action NullAction()
                        idle "battle_surrender"
                    button:
                        yalign 0.5
                        action NullAction()
                        text _("Surrender") style "button_text3"
                hbox:
                    spacing 10
                    imagebutton:
                        action NullAction()
                        idle "battle_item"
                    button:
                        yalign 0.5
                        action NullAction()
                        text _("Item") style "button_text3"
                hbox:
                    spacing 10
                    imagebutton:
                        action NullAction()
                        idle "battle_escape"
                    button:
                        yalign 0.5
                        action NullAction()
                        text _("Escape") style "button_text3"


        frame:
            xalign 0.025
            yalign 0.965
            ypadding 10
            has vbox
            spacing 10
            bar value AnimatedValue(pc.hp, pc.max_hp) left_bar Frame("left_red", 6, 6)
            bar value AnimatedValue(pc.mp, pc.max_mp) left_bar Frame("left_blue", 6, 6)
            bar value AnimatedValue(pc.lust, pc.max_lust) left_bar Frame("left_yellow", 6, 6)
        vbox:
            xalign 0.15
            yalign 0.94
            spacing 26
            text "[e]" xalign 0.1 yalign 0.5 style "enemy_text2"
            text _("HP: [pc.hp] / [pc.max_hp]") size 20
            text _("MP: [pc.mp] / [pc.max_mp]") size 20
            text _("LUST: [pc.lust] / [pc.max_lust]") size 20

    if AbilityTab == True:
        vbox:
            xalign 0.2
            yalign 0.1
            spacing 30
            if abilities[0] != None:
                if pc.mp >= abilities[0].cost and silenced not in status and abilities[0].coolDownTimer <= 0:
                    $ ab0_cd = abilities[0].coolDownTimer
                    frame:
                        has button
                        hovered SetVariable("ability_show1", True)
                        unhovered SetVariable("ability_show1", False)
                        action Return(abilities[0].name), SetVariable("ab0_cd", abilities[0].coolDown)
                        text "[abilities[0].name!t]" style "button_text"
                else:
                    frame:
                        has button
                        hovered SetVariable("ability_show1", True)
                        unhovered SetVariable("ability_show1", False)
                        action NullAction()
                        text "{s}[abilities[0].name!t]{/s}" style "button_text"
            if abilities[1] != None:
                if pc.mp >= abilities[1].cost and silenced not in status and abilities[1].coolDownTimer <= 0:
                    $ ab1_cd = abilities[1].coolDownTimer
                    frame:
                        has button
                        hovered SetVariable("ability_show2", True)
                        unhovered SetVariable("ability_show2", False)
                        action Return(abilities[1].name), SetVariable("ab1_cd", abilities[1].coolDown)
                        text "[abilities[1].name!t]" style "button_text"
                else:
                    frame:
                        has button
                        hovered SetVariable("ability_show2", True)
                        unhovered SetVariable("ability_show2", False)
                        action NullAction()
                        text "{s}[abilities[1].name!t]{/s}" style "button_text"
            if abilities[2] != None:
                if pc.mp >= abilities[2].cost and silenced not in status and abilities[2].coolDownTimer <= 0:
                    $ ab2_cd = abilities[2].coolDownTimer
                    frame:
                        has button
                        hovered SetVariable("ability_show3", True)
                        unhovered SetVariable("ability_show3", False)
                        action Return(abilities[2].name), SetVariable("ab2_cd", abilities[2].coolDown)
                        text "[abilities[2].name!t]" style "button_text"
                else:
                    frame:
                        has button
                        hovered SetVariable("ability_show3", True)
                        unhovered SetVariable("ability_show3", False)
                        action NullAction()
                        text "{s}[abilities[2].name!t]{/s}" style "button_text"

    if ItemTab == True:
        vbox:
            xalign 0.2
            yalign 0.4
            spacing 30
            if LookForItem("Small HP Potion", inventory):
                $ item_num = LookForItemNumber("Small HP Potion", inventory)
                frame:
                    has button
                    action Return("Small HP Potion")
                    text _("[item_num] x Small HP Potion") style "button_text" size 20
            if LookForItem("Small MP Potion", inventory):
                $ item_num = LookForItemNumber("Small MP Potion", inventory)
                frame:
                    has button
                    action Return("Small MP Potion")
                    text _("[item_num] x Small MP Potion") style "button_text" size 20
            if LookForItem("Buggbear Sedative", inventory) and enemy == buggbear:
                $ item_num = LookForItemNumber("Buggbear Sedative", inventory)
                frame:
                    has button
                    action Return("Buggbear Sedative")
                    text _("[item_num] x Buggbear Sedative") style "button_text" size 20
            if LookForItem("Strength Potion", inventory):
                $ item_num = LookForItemNumber("Strength Potion", inventory)
                frame:
                    has button
                    action Return("Strength Potion")
                    text _("[item_num] x Strength Potion") style "button_text" size 20
            if LookForItem("Accuracy Potion", inventory):
                $ item_num = LookForItemNumber("Accuracy Potion", inventory)
                frame:
                    has button
                    action Return("Accuracy Potion")
                    text _("[item_num] x Accuracy Potion") style "button_text" size 20
            if LookForItem("Tenacity Potion", inventory):
                $ item_num = LookForItemNumber("Tenacity Potion", inventory)
                frame:
                    has button
                    action Return("Tenacity Potion")
                    text _("[item_num] x Tenacity Potion") style "button_text" size 20
            if LookForItem("Green Ointment", inventory):
                $ item_num = LookForItemNumber("Green Ointment", inventory)
                frame:
                    has button
                    action Return("Green Ointment")
                    text _("[item_num] x Green Ointment") style "button_text" size 20

    if ability_show1:
        frame:
            xalign 0.195
            yalign 0.525
            xpadding 20
            ypadding 10
            label "[abilities[0].description!t]" text_color "#eeeeee"
    if ability_show2:
        frame:
            xalign 0.195
            yalign 0.525
            xpadding 20
            ypadding 10
            label "[abilities[1].description!t]" text_color "#eeeeee"
    if ability_show3:
        frame:
            xalign 0.195
            yalign 0.525
            xpadding 20
            ypadding 10
            label "[abilities[2].description!t]" text_color "#eeeeee"


    if ally_num == 2:

        $ ally_ability1_img = "battle_" + ally.ext1.lower()
        $ ally_ability2_img = "battle_" + ally.ext2.lower()
        $ ally_ability3_img = "battle_" + ally.ext3.lower()
        frame:
            xalign 1.00
            yalign 0.02
            xpadding 20
            ypadding 20
            xmaximum 300
            xminimum 80
            ymaximum 800
            yminimum 100
            vbox:
                style "button2"
                spacing 12
                xmaximum 400
                if battleTurn == "Ally":
                    hbox:
                        spacing 10
                        imagebutton:
                            action Return("Attack")
                            idle "battle_attack"
                        button:
                            yalign 0.5
                            action Return("Attack")
                            text _("Attack") style "button_text2"
                    if ally.mp >= 15:
                        hbox:
                            spacing 10
                            imagebutton:
                                action Return(ally.ext1)
                                idle ally_ability1_img
                            button:
                                yalign 0.5
                                action Return(ally.ext1)
                                text ally.ext1 style "button_text2"
                        hbox:
                            spacing 10
                            imagebutton:
                                action Return(ally.ext2)
                                idle ally_ability2_img
                            button:
                                yalign 0.5
                                action Return(ally.ext2)
                                text ally.ext2 style "button_text2"
                        hbox:
                            spacing 10
                            imagebutton:
                                action Return(ally.ext3)
                                idle ally_ability3_img
                            button:
                                yalign 0.5
                                action Return(ally.ext3)
                                text ally.ext3 style "button_text2"
                    else:
                        hbox:
                            spacing 10
                            imagebutton:
                                action NullAction()
                                idle ally_ability1_img
                            button:
                                yalign 0.5
                                action NullAction()
                                text ally.ext1 style "button_text3"
                        hbox:
                            spacing 10
                            imagebutton:
                                action NullAction()
                                idle ally_ability2_img
                            button:
                                yalign 0.5
                                action NullAction()
                                text ally.ext2 style "button_text3"
                        hbox:
                            spacing 10
                            imagebutton:
                                action NullAction()
                                idle ally_ability3_img
                            button:
                                yalign 0.5
                                action NullAction()
                                text ally.ext3 style "button_text3"

                else:
                    hbox:
                        spacing 10
                        imagebutton:
                            action NullAction()
                            idle "battle_attack"
                        button:
                            yalign 0.5
                            action NullAction()
                            text _("Attack") style "button_text3"
                    hbox:
                        spacing 10
                        imagebutton:
                            action NullAction()
                            idle ally_ability1_img
                        button:
                            yalign 0.5
                            action NullAction()
                            text ally.ext1 style "button_text3"
                    hbox:
                        spacing 10
                        imagebutton:
                            action NullAction()
                            idle ally_ability2_img
                        button:
                            yalign 0.5
                            action NullAction()
                            text ally.ext2 style "button_text3"
                    hbox:
                        spacing 10
                        imagebutton:
                            action NullAction()
                            idle ally_ability3_img
                        button:
                            yalign 0.5
                            action NullAction()
                            text ally.ext3 style "button_text3"


            frame:
                xalign 0.925
                yalign 0.965
                ypadding 10
                has vbox
                spacing 10
                bar value AnimatedValue(ally.hp, ally.max_hp) left_bar Frame("left_red", 6, 6)
                bar value AnimatedValue(ally.mp, ally.max_mp) left_bar Frame("left_blue", 6, 6)
                bar value AnimatedValue(ally.lust, ally.max_lust) left_bar Frame("left_yellow", 6, 6)
            vbox:
                xalign 0.85
                yalign 0.94
                spacing 26
                text "[ally.name]" xalign 0.1 yalign 0.5 style "enemy_text2"
                text _("HP: [ally.hp] / [ally.max_hp]") size 20
                text _("MP: [ally.mp] / [ally.max_mp]") size 20
                text _("LUST: [ally.lust] / [ally.max_lust]") size 20
init python:
    def check_party(x):
        
        
        
        if x.hp <= 0 or x.lust >= x.max_lust:
            return "lost"


label slime_battle:


    $ enemy_num = 1
    $ enemy = slime

    $ enemy.img = "Slime"
    $ enemy.max_hp = 50
    $ enemy.min_damage = 7
    $ enemy.max_damage = 20
    $ enemy.min_lust_damage = 0
    $ enemy.max_lust_damage = 0
    $ enemy.dodge = 10
    $ enemy.defense = 36
    $ enemy.lust_defense = 100
    $ enemy.exp_drop = 45
    $ enemy.beginbattle()
    call beginningBattle from _call_beginningBattle_13

    scene forest:
        blur 8
    if pc.weapon == None:
        "You are facing a green slime, it is slowly slithering at you. You raise your fists, ready to strike at the gelatinous mass."
    else:
        "You are facing a green slime, it is slowly slithering at you. you pull out your [pc.weapon.name!t]."

    $ enemy_image = "slime"

    jump general_battle_loop

label slime_battle_loop:

    $ raw_damage = int(renpy.random.randint(slime.min_damage, slime.max_damage))
    $ enemy_damage = damageFormula(raw_damage, pc.defense)
    call Damaging (enemy, pc, enemy_damage) from _call_Damaging
    if renpy.random.random() < 0.5:
        "Slime lunges forward and slams into your waist with its gelatinous body. Your health decreases by [enemy_damage] HP."
    else:
        "The slime slithers towards you and traps you within its body. You struggle for a few seconds before getting out of the slime. Your health decreases by [enemy_damage] HP."
    call Battle_End_Check from _call_Battle_End_Check_8
    jump general_battle_loop

label slime_win:

    $ slime.win += 1
    if pc.weapon == None:
        "You pull your arm away from the slime as you punch it for the last time. The slime slowly ceases all motion as it melts into the grass, forming a pond of green mass."
    else:
        "You pull your [pc.weapon.name!t] out of the slime as you cut into it for the last time. The slime slowly ceases all motion as it melts into the grass, forming a pond of green mass."
    show screen menu_buttons
    scene forest
    $ exp_drop = renpy.random.randint(int(slime.exp_drop*0.8), int(slime.exp_drop*1.25))
    if lindbloom_item in pc.trinket:
        $ rnd = .7
    else:
        $ rnd = .35

    $ addItem("Slime Ball", inventory, 1)
    if renpy.random.random() <= rnd:
        "As you search around the slime, you found a [slimeball_item.name], a [slimecrystal_item.name] and [exp_drop] EXP!"

        $ addItem("Slime Crystal", inventory, 1)
    else:
        "As you search around the slime, you found a [slimeball_item.name] and [exp_drop] EXP!"

    call level_up_check (slime.exp_drop*0.8, slime.exp_drop*1.25, 12, 22) from _call_level_up_check_3
    jump main_green_forest

label slime_lose:
    $ slime.lose += 1
    scene forest
    "You stumble, your knees feel weak, you can barely catch your breath facing against the oozy mass of slime. Expectedly, you collapse on the grass floor, holding on to the sliver of energy in your body."
    if slime.lose >= 1 or pc.lust >= 40:
        menu:
            msg "Do you wish to replay the losing Scene?"
            "Yes{#slimelose}":
                call scene_slime_sex from _call_scene_slime_sex
            "No{#slimelose}":

                "You fall unconscious shortly after..."
    else:
        "Its goo runs over your body, soaking up your scent with the viscous chemicals."
        "Maybe it'll be a bad idea if you ever lose to the creature once again..."
    scene black
    pause .5
    scene forest
    with fade
    show screen menu_buttons
    "When you wake up, you find that the slime is already gone. There are still puddles of slimy residue around your crotch area."
    "You can't bring yourself to think about the incident again, so you quickly get up, pat away all the slime around your member and leave the place."
    call lost_gold_check (0.02, 15, True) from _call_lost_gold_check_3
    jump main_green_forest

label dummy_battle:


    $ enemy_num = 1
    $ enemy = dummy
    $ enemy.img = "Dummy"
    if dummylvl2 > 0:
        $ enemy.max_hp = 300
        $ enemy.min_damage = 40
        $ enemy.max_damage = 70
        $ enemy.min_lust_damage = 13
        $ enemy.max_lust_damage = 21
        $ enemy.dodge = 12
        $ enemy.defense = 55
        $ enemy.lust_defense = 35
        $ enemy.exp_drop = 95
    else:
        $ enemy.max_hp = 35
        $ enemy.min_damage = 25
        $ enemy.max_damage = 35
        $ enemy.min_lust_damage = 13
        $ enemy.max_lust_damage = 21
        $ enemy.dodge = 12
        $ enemy.defense = 25
        $ enemy.lust_defense = 35
        $ enemy.exp_drop = 45

    call beginningBattle from _call_beginningBattle_6
    $ enemy.beginbattle()

    if isNight():
        scene lusterfield_alleywaynodummy_night:
            blur 8
    else:
        scene lusterfield_alleywaynodummy:
            blur 8

    $ enemy_image = "dummy"

    "You are facing the practice dummy, it is waving at you, getting ready for you to begin."

    jump general_battle_loop

label dummy_battle_loop:
    $ raw_damage = int(renpy.random.randint(dummy.min_damage, dummy.max_damage))
    $ enemy_damage = damageFormula(raw_damage, pc.defense)
    call Damaging (enemy, pc, enemy_damage) from _call_Damaging_1
    "You get closer to let the dummy slap you on the side. Your health decreases by [enemy_damage] HP."
    call Battle_End_Check from _call_Battle_End_Check_9
    jump general_battle_loop

label dummy_win:
    $ dummy.win += 1
    if pc.weapon == None:
        "When you finish your last strike on the dummy, it crosses its arm, signaling its defeat."
    show screen menu_buttons
    scene lusterfield_alleyway

    if dummylvl2 > 0:
        $ exp_drop = renpy.random.randint(int(dummy.exp_drop*16/(pc.level+5)), int(dummy.exp_drop*20/(pc.level+5)))
        "The dummy hands you 3 [patch_item.name!t], and [exp_drop] EXP!"
        $ addItem("Patch", inventory, 3)
    else:
        $ exp_drop = renpy.random.randint(int(dummy.exp_drop*0.8/pc.level), int(dummy.exp_drop*1.25/pc.level))
        "The dummy hands you a [patch_item.name!t], and [exp_drop] EXP!"
        $ addItem("Patch", inventory, 1)

    call level_up_check (exp_drop*0.9, exp_drop, 5, 15) from _call_level_up_check_4
    jump main_lusterfield_alleyway

label dummy_lose:
    $ dummy.lose += 1
    show screen menu_buttons
    scene lusterfield_alleyway
    "Your health reaches 0, you are exhausted to the point of collapsing on the grass floor. The world slowly fades away along with the motionless dummy."
    scene black
    with fade
    pause 1.0
    scene lusterfield_alleyway
    with fade
    "When you wake up, you check your pockets and find nothing missing. You see the dummy still mounted in the alleyway. It's waving at you, probably scoffing at someone who lost to a dummy."
    jump main_lusterfield_alleyway

label goathuntsman_battle:

    show Goat:
        xalign 0.5
        yalign 0.25
    if goat_num == 0:
        $ goat_num = 1
    $ enemy_num = 1
    $ enemy = goat
    if goat_num == 1:
        $ enemy.max_hp = 140
        $ enemy.min_damage = 22
        $ enemy.max_damage = 36
        $ enemy.defense = 50
        $ enemy.exp_drop = 90
    if goat_num == 2:
        $ enemy.max_hp = 240
        $ enemy.min_damage = 37
        $ enemy.max_damage = 50
        $ enemy.defense = 60
        $ enemy.exp_drop = 60
    $ enemy.min_lust_damage = 12
    $ enemy.max_lust_damage = 20
    $ enemy.dodge = 25
    $ enemy.lust_defense = 30

    $ goat.beginbattle()
    call beginningBattle from _call_beginningBattle_7
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    if goat_num == 1:
        scene ancienttree:
            blur 8
    if goat_num == 2:
        scene kechioeren_training_ground:
            blur 8
    $ enemy_image = "Goat e1"
    if pc.weapon == None:
        "You are facing a goat huntsman, he is waving his spear in arrogance, daring you to come closer. You raise your fists and enter a fighting stance."
    else:

        "You are facing a goat huntsman, he is waving his spear in arrogance, gesturing you to come closer. You hold your [pc.weapon.name!t] in defence."

    jump general_battle_loop

label goathuntsman_battle_loop:

    $ dia = renpy.random.random()
    if dia < 0.50:
        if renpy.random.random()*100 > pc.dodge+extra_dodge:
            $ raw_damage = int(renpy.random.randint(goat.min_damage, goat.max_damage))
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_2
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The goat huntsman swings his spear towards you, you are not quick enough to dodge his blow. Your health decreases by [enemy_damage] HP."
            else:
                "The goat charges at you, hitting you with a kick to the chest. Your health decreases by [enemy_damage] HP."
        else:
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The goat huntsman swings his spear towards you. You managed to deflect his spear and dodge the attack."
            else:
                "The goat charges at you, trying to kick at your chest, but you block the blow and push him back."
    elif dia < 0.67 and trapped not in status:
        "While you are calculating your next move, you fall into his trap, your dodges are now reduced by half for 3 rounds."
        $ trapped.rounds = trapped.max_rounds
        $ status.append(trapped)
        $ extra_dodge -= pc.dodge/2
        $ extra_lust_dodge -= pc.lust_dodge/2
    else:
        if renpy.random.random()*100 > pc.lust_dodge + extra_lust_dodge:
            $ raw_flirt = int(renpy.random.randint(goat.min_lust_damage, goat.max_lust_damage))
            $ enemy_flirt = damageFormula(raw_flirt, pc.lust_defense)
            $ pc.lust += enemy_flirt
            if pc.lust > pc.max_lust:
                $ pc.lust = pc.max_lust
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The goat scratches at his loincloth, he put two of his fingers across his crotch, tracing the shape of his cock through the fabric."
                gt "You thirsty? Surrender to me and maybe you'll have the best time of your life."
                "You gulp at his attempt at seduction. Admittedly you are extremely aroused, thinking about how his cock would taste. Your lust increased by [enemy_flirt]."
            else:
                "The huntsman stretches his body, flaunting his muscular physique, you can tell his soft chest is almost bulging in front of you."
                gt "You see how strong of a specimen I am. Come closer to get a better look!"
                "You are stunned by his gorgeous muscles, you mind wanders through scenarios of him being inside your body. Your lust increased by [enemy_flirt]."
        else:
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The goat scratches at his loincloth, he put two of his fingers across his crotch, tracing the shape of his cock through the fabric."
                gt "You thirsty? Surrender to me and maybe you'll have the best time of your life."
                "You stare at him, giving him weird side eye. You have evaded his attempt at seduction. The goat seems to feel a little dejected."
            else:
                "The huntsman stretches his body, flaunting his muscular physique, you can tell his soft chest is almost bulging in front of you."
                gt "You see how strong of a specimen I am. Come closer to get a better look!"
                "His attack at your lust seems to have failed as you stand there and wait for him to finish his taunt. Both of you would never speak about it again."



    if enemy.lust < enemy.max_lust / 3:
        $ enemy_image = "Goat e1"
    elif enemy.lust < enemy.max_lust / 3 * 2:
        $ enemy_image = "Goat e2"
    else:
        $ enemy_image = "Goat e3"
    call Battle_End_Check from _call_Battle_End_Check_10
    jump general_battle_loop
label goathuntsman_win:

    show screen menu_buttons
    hide Goat

    $ goat.win += 1
    if goat.hp <= 0:
        "You strike the huntsman for the last time, before he falls on the ground. Luckily he is still breathing."
    elif goat.lust >= goat.max_lust:
        "The goat huntsman cannot stop himself from stroking his cock. He lies on the ground, surrendering himself at your will."
        gt "P-please... I...w-want... c-cock, m-make me... cum."
    if quest23.status == 3:
        $ goat_num = 3
        k "...Well. The second one, or should I say, ones. They're our best duo in the tribe... B-best warrior duo..."
        jump goat_guard_battle
    if goat.win >= 1:
        menu:
            "You stare at the goat lying on the ground, barely able to catch a breath..."
            "Have fun with the huntsman":
                if goat_num == 2:
                    gt "W-wait... not here..."
                    "The goat looks at you with the pleading eyes... you decide to bring him to the forest..."
                "..."
                scene black
                pause 2.0
                call Scene_Goat_Win from _call_Scene_Goat_Win
                $ pc.lust = 0
            "Leave him alone{#huntsmanwin}":
                "As much as you wish to relieve all your pent up anger on the poor goat, you decide against it."
    else:
        "As much as you wish to relieve all your pent up anger on the poor goat, you decide against it."

    $ exp_drop = renpy.random.randint(int(goat.exp_drop*0.8), int(goat.exp_drop*1.25))
    if lindbloom_item in pc.trinket:
        $ rnd = 0.4
    else:
        $ rnd = 0.2

    $ addItem("Cashmere", inventory, 1)
    if renpy.random.random() <= rnd:
        "As you search around the huntsman, you find a Cashmere Wool, a Pocket Bell and [exp_drop] EXP!"
        $ addItem("Pocket Bell", inventory, 1)
    else:
        "As you search around the huntsman, you find a Cashmere Wool and [exp_drop] EXP!"
    $ pc.exp += exp_drop
    $ found_gold = renpy.random.randint(7, 17)
    "You also filch [found_gold] gold from the huntsman's loincloth. You pick the coins up, and put them in your pouch."
    $ pc.gold += found_gold
    if goat_num == 1:
        "You leave the huntsman alone in the forest, he will probably wake up in a few hours."
    if goat_num == 2:
        gt "...well. Good job."
        "You leave the huntsman still panting profusly on the side of the training ground..."
    if pc.exp > pc.expCap and pc.level <= levelCap:
        $ pc.LevelUp()
        msg "You are now Level [pc.level]! Check your inventory to allocate your level points."
    if goat_num == 1:
        jump main_ancient_tree
    if goat_num == 2:
        jump main_kechioeren_training_ground

label goathuntsman_lose:
    $ goat.lose += 1
    hide Goat

    if pc.hp <= 0:
        "You struggle against the huntsman, but you have already exhausted all your energy. He stands above you like a hunter with his prey, licking his lips while thinking about his next move."
    if pc.lust >= pc.max_lust:
        "You fall to your knees, your hands all over your body, you cannot resist your lust..."
        "The huntsman stands above you like a hunter with his prey, licking his lips while thinking about his next move."
    if goat.lose > 0 and (goat_num == 1 or goat_num == 2 and enemy.lust > 60):
        menu:
            "Do you wish to replay the lose Scene?"
            "Yes{#goatlose}":
                gt "Heh... gotta bring you to somewhere discreet..."
                "The goat carries you out of the goat tribe..."
                call Scene_Goat_Lose from _call_Scene_Goat_Lose
            "No{#goatlose}":
                pass
    else:
        call Scene_Goat_Lose from _call_Scene_Goat_Lose_1

    "You fall unconscious soon after..."
    show screen menu_buttons
    call lost_gold_check (0.05, 10, True) from _call_lost_gold_check_8
    "You wake up a few hours later, your body still sore. The huntsman is nowhere to be found, vanishing along with some of your gold."

    $ pc.add_active_status(stuffed)
    jump main_ancient_tree

label buggbear_battle:

    $ status = None

    $ enemy_num = 1
    $ enemy_extra_damage = 0
    $ enemy = buggbear
    $ enemy.max_hp = 210
    $ enemy.min_damage = 22
    $ enemy.max_damage = 50
    $ enemy.min_lust_damage = 0
    $ enemy.max_lust_damage = 0
    $ enemy.dodge = 8
    $ enemy.defense = 30
    $ enemy.lust_defense = 5
    $ enemy.exp_drop = 85

    $ enemy_image = "buggbear"
    $ buggbear.beginbattle()
    call beginningBattle from _call_beginningBattle_8
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    scene woodlandoutpost:
        blur 8
    show expression enemy_image with dissolve
    "You are facing a wild buggbear. He looks at you with rage-filled eyes, a clear desire to smash your head in with his mace painted on his face."

    jump general_battle_loop

label buggbear_battle_loop:


    if turn_action == "Buggbear Sedative":
        if buggbear.hp < buggbear.max_hp /2 or buggbear.lust > buggbear.max_lust /2:
            hide expression enemy_image
            jump buggbear_sedated
        else:
            "You cann't use the Sedative yet, the buggbear is too responsive... Perhaps you need to make him weaker, or hornier..."
            jump general_battle_loop

    $ dia = renpy.random.random()
    if dia < 0.50:
        if renpy.random.random()*100 > pc.dodge+extra_dodge:
            $ raw_damage = int(renpy.random.randint(buggbear.min_damage, buggbear.max_damage)) + enemy_extra_damage * 10
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_3
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The buggbear swings his giant mace towards you. You are not quick enough to dodge his blow. Your health decreases by [enemy_damage] HP."
            else:
                "The buggbear charges at you, knocking away your guard with his off-hand before hitting you with a kick to the chest. Your health decreases by [enemy_damage] HP."
        else:
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The buggbear swings his mace towards you. You barely manage to deflect his heavy mace and dodge the attack."
            else:
                "The buggbear charges at you, trying to kick your chest, but you block the blow and push him back."
    else:
        "The buggbear raises his left fist and chants the tune of his tribe's warsong. It increases his attack damage by 10 for the rest of the fight."
        $ enemy_extra_damage += 1
    call Battle_End_Check from _call_Battle_End_Check_13
    jump general_battle_loop

label buggbear_sedated:

    "You throw your sedative powder right into the buggbear's face, hitting him in the nose."
    e "Take this!"
    "The monster takes a big whiff of the powder before noticing what the substance is."
    show buggbear:
        xalign 0.5 yalign 0.25
        linear 0.1 zoom 1.2
        linear 0.05 zoom 1
    "Your sedative definitely worked, as he coughs violently, his limbs growing weaker."
    show buggbear:
        linear 0.1 zoom 1.1
        linear 0.05 zoom 1
    "He staggers for a few seconds before growling back at you, and collapses in front of your weapon."
    show buggbear:
        linear 0.1 zoom 1.04
        linear 0.05 zoom 1
    "..."
    show buggbear:
        linear 0.2 yalign 8.0
    "After it falls flat, you walk towards the buggbear, and poke him with your wooden stick."
    hide screen battle_buttons
    hide screen battle_enemy_stat
    hide screen battle_player_stat

    "You take a while to actually confirm that he is indeed knocked out, and begin taking out an empty bottle from your bag."
    e "Just... get close..."
    "You raise your hand over the unconscious buggbear, he is surely asleep now."
    $ buggbear_woke_early = False
    $ buggbear_hp_margin = max(0.0, (buggbear.max_hp / 2.0 - buggbear.hp) / (buggbear.max_hp / 2.0))
    $ buggbear_lust_margin = max(0.0, (buggbear.lust - buggbear.max_lust / 2.0) / (buggbear.max_lust / 2.0))
    $ buggbear_sedation_margin = max(buggbear_hp_margin, buggbear_lust_margin)
    $ buggbear_wakeup_chance = max(0.15, 0.95 - buggbear_sedation_margin * 0.75)
    "Without waking up the monster, you gently lower his chin and open his mouth."
    if renpy.random.random() < buggbear_wakeup_chance:
        $ buggbear_woke_early = True
        jump buggbear_sedated_wakeup
    "His loud snore almost startled you, but you calm down and quickly scoop up the extra sticky liquid around his tongue."
    "..."
    e "fuck..."
    "You drop the bottle and his saliva spills all over your body. Luckily the buggbear doesn't seem to take notice of your clumsiness."
    "In a few seconds, you abruptly scrape the rest of his saliva back into the bottle and get up from the mess."
    jump buggbear_sedated_reward

label buggbear_sedated_wakeup:

    "You feel it before you understand it."
    "The buggbear's snoring catches in his throat and subsides, and his lip twitches sharply against your fingers."
    "One bloodshot eye cracks open and fixes on you at once."
    $ buggbear_escape_time = min(3.2, 1.8 + pc.agi * 0.1)
    $ timer_time = buggbear_escape_time
    $ renpy.pause(renpy.random.random()*0.35+0.15)
    show screen countdown("buggbear_sedated_escape_fail", buggbear_escape_time, 2)
    menu:
        "A massive claw jerks toward your wrist."
        "Freeze":
            jump buggbear_sedated_escape_fail
        "Pull back!":
            hide screen countdown
            "You wrench your hand away just before his claws snap shut, sending saliva splattering across his chin and your sleeve."
            jump buggbear_sedated_escape_2
        "Keep filling the bottle":
            jump buggbear_sedated_escape_fail

label buggbear_sedated_escape_2:

    "The buggbear lurches up with a furious, guttural growl, his huge body swaying as the sedative wars with his rage."
    "Even half-drugged, the force of his swing tears through the air hard enough to make you flinch."
    $ timer_time = buggbear_escape_time
    $ renpy.pause(renpy.random.random()*0.35+0.15)
    show screen countdown("buggbear_sedated_escape_fail", buggbear_escape_time, 2)
    menu:
        "His arm scythes across the dirt where you were kneeling an instant ago."
        "Shove him":
            jump buggbear_sedated_escape_fail
        "Back away slowly":
            jump buggbear_sedated_escape_fail
        "Duck under the swing":
            hide screen countdown
            "You throw yourself flat and scramble beneath his flailing arm while he snarls and struggles to steady his footing."
            jump buggbear_sedated_escape_3

label buggbear_sedated_escape_3:

    "The bottle is slick in your trembling grip."
    "Behind you, the buggbear crashes through the brush with a roar, dragging his heavy body forward through sheer fury."
    $ timer_time = buggbear_escape_time
    $ renpy.pause(renpy.random.random()*0.35+0.15)
    show screen countdown("buggbear_sedated_escape_fail", buggbear_escape_time, 2)
    menu:
        "He roars behind you and lunges one last time."
        "Run for the brush":
            hide screen countdown
            "You throw yourself into the undergrowth and hear the buggbear slam bodily into a tree behind you with a crack of bark and a burst of leaves."
            "By the time he rips himself loose, the sedative is pulling at him again, turning his furious charge into a sluggish, stumbling pursuit."
            "That single opening is all you need to vanish into the forest."
            jump buggbear_sedated_reward
        "Turn and fight":
            jump buggbear_sedated_escape_fail
        "Protect the bottle":
            jump buggbear_sedated_escape_fail

label buggbear_sedated_escape_fail:

    hide screen countdown
    "You hesitate for one fatal heartbeat."
    "The buggbear surges into you before you can recover, knocking the bottle from your hand and sending it spinning into the dirt."
    "His hot, rancid breath crashes over your face as he realizes exactly what you were trying to do."
    jump BadEnd_Buggbear_Sheath

label buggbear_sedated_reward:

    if buggbear_woke_early:
        "You do not stop running until the buggbear's enraged roars have faded into the distance."
        "Only then do you dare look down at the bottle clenched in your hand."
        "Despite the mess and the chase, enough of the buggbear's saliva still sloshes inside to make the risk worthwhile."
    $ removeItem("Buggbear Sedative", inventory, 1)
    $ addItem("Buggbear Saliva", inventory, 1)
    $ item_number = LookForItemNumber("Buggbear Saliva", inventory)
    "You have collected a bottle of buggbear saliva, you now own [item_number] bottle."

    if buggbear_woke_early:
        jump buggbear_sedated_escape_win
    jump buggbear_win2

label buggbear_sedated_escape_win:
    $ buggbear.win += 1
    "There is no chance to circle back for the rest of the buggbear's belongings, not while he is still somewhere behind you in the woods."
    "Still, you made it out with the saliva sample, which is more than you expected when his eyes snapped open."

    call level_up_check (int(buggbear.exp_drop*0.55), int(buggbear.exp_drop*0.85), 4, 15) from _call_level_up_check_12
    jump main_woodland_outpost

label buggbear_win:

    menu:
        "Do you want to have fun with the buggbear?"
        "Yes{#buggbearwin}":
            call scene_buggbear_win from _call_scene_buggbear_win
            $ pc.lust = 0
        "No{#buggbearwin}":
            pass
label buggbear_win2:
    $ buggbear.win += 1
    $ exp_drop = renpy.random.randint(int(buggbear.exp_drop*0.8), int(buggbear.exp_drop*1.25))
    if lindbloom_item in pc.trinket:
        $ rnd = 0.8
    else:
        $ rnd = 0.4

    $ addItem("Raw Meat", inventory, 1)
    if renpy.random.random() <= rnd:
        "As you search around the buggbear, you find a Raw Meat, a Strap and [exp_drop] EXP!"
        $ addItem("Strap", inventory, 1)
    else:
        "As you search around the buggbear, you find a Raw Meat and [exp_drop] EXP!"

    $ pc.exp += exp_drop
    $ found_gold = renpy.random.randint(9, 20)
    "You also find [found_gold] gold in the buggbear's leather pouch. You pick the coins up swiftly."
    $ pc.gold += found_gold
    "You leave the buggbear alone in the forest, he will probably wake up in a few hours."
    if pc.exp > pc.expCap and pc.level <= levelCap:
        $ pc.LevelUp()
        msg "You are now Level [pc.level]! Check your inventory to allocate your level points."
    jump main_woodland_outpost
label buggbear_lose:

    if pc.hp <= 0:
        "You struggle against the buggbear, but your mind succumbs to your unquenchable lust for the buggbear. He pounces on your helpless body like you are a feast to be served."
    if pc.lust >= pc.max_lust:
        "You struggle against the buggbear, your mind is filled with unquenchable lust over the buggbear. He pounces on your helpless body like you are a feast to be served."
    "..."
    $ buggbear.lose += 1
    menu:
        "Do you want to replay the losing scene?"
        "Yes{#buggbearlose}":
            call scene_buggbear_lose from _call_scene_buggbear_lose
        "No{#buggbearlose}":
            pass
    show screen menu_buttons
    call lost_gold_check (0.07, 30, True) from _call_lost_gold_check_9

    $ pc.add_active_status(stuffed)
    jump main_woodland_outpost

label mossgolem_battle:



    $ enemy_num = 1
    $ grip_strength = 100
    $ enemy = mossgolem
    $ enemy.max_hp = 240
    $ enemy.min_damage = 35
    $ enemy.max_damage = 55
    $ enemy.min_lust_damage = 13
    $ enemy.max_lust_damage = 21
    $ enemy.dodge = 12
    $ enemy.defense = 25
    $ enemy.lust_defense = 35
    $ enemy.exp_drop = 85
    $ mossgolem.beginbattle()
    call beginningBattle from _call_beginningBattle_9
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen menu_buttons
    scene mossy_freshwater:
        blur 8
    show moss_golem:
        xalign 0.5
        yalign 0.25
    with dissolve
    "It is a Moss Golem. He is standing before you, he looks enraged by your intrusion."
    "You can feel his blue aura radiating throughout the river. His left hand is missing, instead covered with layers of moss and vines."
    if pc.weapon != None:
        "You raise your [pc.weapon.name!t], defending yourself from the golem's attack."
    else:
        "You raise your fists in a block, defending yourself from the golem's attack."

    jump mossgolem_battle_loop
label mossgolem_battle_loop:

    show moss_golem:
        xalign 0.5
        yalign 0.25
    if check_party(pc) == "lost":
        call Battle_Finish from _call_Battle_Finish_56
        jump mossgolem_lose
    $ turn_action = ui.interact()
    call Battle_ASF from _call_Battle_ASF_11
    if oa[0] == "A":
        if oa[1] == "M":
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the arm of the golem, but his magical aura repels the attack."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] at the golem's head, but his magical aura repels the attack."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the golem, but it seems to have missed."
            if oa[3] == "N":
                "You throw a punch at the golem, but your punch meets air rather than the block of stone you expected."
        else:
            call Enemy_Damaging (enemy, oa[4]) from _call_Enemy_Damaging
            if oa[3] == "A":
                if renpy.random.random() > 0.5:
                    "You slash your [pc.weapon.name!t] at the arm of the moss golem. Your blade scrapes against the stone, chipping pieces off of his body."
                else:
                    "You slash your [pc.weapon.name!t] across the golem's body, knocking him back a few steps. The golem quakes silently in anger."
            if oa[3] == "B":
                if renpy.random.random() > 0.5:
                    "You slam your [pc.weapon.name!t] at the arm of the moss golem, your blade crashes against the stone with a harsh, grating sound. Chunks of his arm crumble under the force of the blow."
                else:
                    "You slam your [pc.weapon.name!t] across the golem's body, knocking him back a few steps. The golem quakes silently in anger."
            if oa[3] == "C":
                if renpy.random.random() > 0.5:
                    "You aim and shoot your [pc.weapon.name!t] at the moss golem, the arrow hits him right in the arm, reducing a chunk of the limb to rubble."
                else:
                    "You run while shooting your [pc.weapon.name!t] across the golem's body, knocking him back a few steps. The golem quakes silently in anger."
            if oa[3] == "N":
                if renpy.random.random() > 0.5:
                    "You throw a punch at the golem, catching him straight on the glowing blue core, it wavers, and he seems to lose some of whatever force is holding him together, as it grows dimmer."
                else:
                    "You punch into the golem's stomach, knocking him back a few steps. The golem quakes silently in anger."
            if oa[2] == "N":
                "His health decreases by [oa[4]] HP."
            else:
                "It seems you've hit the golem critically, dealing [oa[4]] HP!"
    if oa[0] == "S":
        "You struggle against the spell, trying to break free. You dealt [oa[4]] damage to the golem in the process. His grip has loosened as well."
    if oa[0] == "F":
        $ dia = renpy.random.random()
        if oa[2] == "B":
            "You struggle against the golem as you try to reach under the golem's crotch in an attempt to get a reaction from it."
            "The golem instanly reacts to your advance, the moss on his surface vibrating profusely. His grip seems to have weakened as well."
        else:
            if dia > 0.334:
                "You turn around and rub your hand all over your burly cheeks, feeling and brushing against your ass while you shake your hips."
            elif dia > 0.667:
                "You gently brush by your member, running a claw from your inner thigh to the back of your balls. You tug at them lightly while staring at the moss golem seductively."
            else:
                "You cup your fluffy chest, drawing circles around the area of your nipples. You smile at the moss golem while you bounce your chest up and down slightly."
            "You approach the golem before gently letting your hands wander inside the huge bush in his crotch area."
            if oa[1] == "M":
                "You continue your act for about a minute, but the moss golem doesn't even flinch."
                "Disappointed, you back away before the golem can grab a hold of you."
            else:
                if renpy.random.random() > 0.5:
                    "You cannot detect his lust on his face, but by the vibration of the moss you can deduce that he's enjoying this a lot. His lust is increased by [player_flirt]."
                else:
                    "The golem doesn't speak, but he is extremely distracted by your performance. His lust is increased by [player_flirt]."
    if oa[0] == "U":
        "You fall to your knees, exhausted all your energy, you grasp for breath as you lie on the ground, surrendering yourself to the golem."
        call Battle_Finish from _call_Battle_Finish_57
        jump mossgolem_lose
    if oa[0] == "E":
        "Try as you might, you cannot escape from the golem's magical aura."
        jump mossgolem_battle_loop
    call Ability_Item from _call_Ability_Item_13
    call Battle_Mid_Check from _call_Battle_Mid_Check_11
    show moss_golem:
        linear 0.1 zoom 1.04
        linear 0.05 zoom 1
    if oa[0] == "W":
        "The golem falls with a huge thud on the ground."
        if mossgolem.hp > 0:
            "You don't know if your flirting worked, but it certainly put down the golem."
        call Battle_Finish from _call_Battle_Finish_58
        jump mossgolem_win
    if mossgolem.hp < mossgolem.max_hp / 5 and golem_stay == 1:
        $ golem_lothar = True
        "As soon as the golem tries to attack, it is stabbed by a mysterious figure."
        l "Another save. You are lucky I went with you, disciple."
        "You quickly recognise the gruff voice. It's Lothar, he appears behind the golem as it falls with a thud on the ground."
        call Battle_Finish from _call_Battle_Finish_59
        jump mossgolem_win
    if oa[0] == "T":
        call Battle_End_Check from _call_Battle_End_Check_27
        jump mossgolem_battle_loop
    $ dia = renpy.random.random()
    if dia < 0.13 and bound not in status:
        "The Moss Golem holds you in place with his right arm. You try to struggle free, but it doesn't work."
        $ status.append(bound)
        $ grip_strength = bound.effect
    elif dia < 0.87:
        if renpy.random.random()*100 > pc.dodge+extra_dodge:
            $ raw_damage = int(renpy.random.randint(mossgolem.min_damage, mossgolem.max_damage))
            $ enemy_damage = raw_damage * (100 - pc.defense) / 100
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_4
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The golem swings his fist in your direction, hitting you in the chest. Your health decreases by [enemy_damage] HP."
            else:
                "The golem strikes you down with his vines. You pass out for a few seconds before getting up. Your health decreases by [enemy_damage] HP."
        else:
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The golem swings his fist in your direction, but you manage to dodge the blow."
            else:
                "The golem tries to strike you down with his vines, but he missed the attack just by inches."
    else:
        "The Moss Golem channels the water into a blue orb of regeneration. His body becomes revitalised by the power of water."
        $ raw_damage = int(renpy.random.randint(mossgolem.min_damage, mossgolem.max_damage))
        $ healing = int(raw_damage * 0.9)
        call Enemy_Self_Healing (mossgolem, healing) from _call_Enemy_Self_Healing
    call Battle_End_Check from _call_Battle_End_Check_12
    jump mossgolem_battle_loop

label mossgolem_lose:

    hide moss_golem

    "The golem stares at your vulnerable state, but doesn't stop there. You realise that you are not making it out of this alive."
    menu:
        "Restart Quest":
            $ pc.hp = saved_hp
            $ pc.mp = saved_mp
            $ pc.lust = saved_lust
            "You close your eyes. You tell yourself that everything will be back to normal."
            "..."
            jump Sebas_Lothar_Adventure


label mossgolem_win:
    hide moss_golem

    $ exp_drop = renpy.random.randint(int(mossgolem.exp_drop*0.8), int(mossgolem.exp_drop*1.25)) + 300
    "You have gained [exp_drop] experience from the battle."
    $ pc.exp += exp_drop
    if pc.exp > pc.expCap and pc.level <= levelCap:
        $ pc.LevelUp()
        msg "You are now Level [pc.level]! Check your inventory to allocate your level points."
    jump Sebas_Lothar_Adventure_End
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
