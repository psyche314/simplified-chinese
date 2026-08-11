style invnumber_label:
    xalign 0.15 yalign 0.12 color "#eeeeee" font "leafy.otf" outlines [(absolute(1), "#000")] size 30


style invlevel_label:
    color "#eeeeee" xalign 0.85 outlines [(absolute(1), "#000")] yalign 0.9 size 30

style screen_content_button_text:
    font "kingthing.ttf"
    size 30
    color "#edd3bf"

style screen_storage_button_text:

    size 40
    idle_color "#eeeeee"
    hover_color "#695336"
    outlines [(absolute(1), "#000")]
    font "leafy.otf"

style tap_button:
    xalign 0.5
    yalign 0.5
    activate_sound click1
    hover_sound clickhover

style click_button:
    xalign 0.5
    yalign 0.5
    activate_sound click2
    hover_sound clickhover

style click_button_text:
    color "#2e1b15"
    font "kingthing.ttf"
    hover_color "#111111"
    size 30

style kaching_button:
    activate_sound clickg
    hover_sound clickhover

style pling_button:
    activate_sound click3
    hover_sound clickhover

style pling_button_text:
    hover_color "#584040"
    color "#edd3bf"
    font "leafy.otf"

style walk_button:
    activate_sound click4
    hover_sound clickhover

style potion_button:
    xalign 0.5
    yalign 0.5
    activate_sound clickpt
    hover_sound clickhover

style material_button:
    xalign 0.5
    yalign 0.5
    activate_sound clickm
    hover_sound clickhover

style page_button:
    xalign 0.5
    yalign 0.5
    activate_sound clickp
    hover_sound clickhover

style page_button_text:
    hover_color "#fee4d0"
    color "#cf805b"
    size 21
    font "kingthing.ttf"

style footstep_button:
    activate_sound clickfs
    hover_sound clickhover

style footstep_button_text:
    size 30
    color "#edd3bf"
    hover_color "#202020"
    font "kingthing.ttf"

style door_button:
    activate_sound clickd
    hover_sound clickhover

style stash_button:
    activate_sound clicksh
    hover_sound clickhover

style stash_button_text:
    size 30
    color "#edd3bf"
    font "kingthing.ttf"
    hover_color "#111111"

style bushchime_button:
    activate_sound clickchime

style coolframe:
    background Frame("coolframe", 10, 10, 10, 10)
    xalign 0.5

style iron_frame:
    background Frame("iron_frame", 10, 10, 10, 10)
    xalign 0.5

style blue_cloth_frame:
    background Frame("blue_cloth_frame", 10, 10, 10, 10)
    xalign 0.5

style gold_frame:
    background Frame("gold_frame", 10, 10, 10, 10)
    xalign 0.5

style framy:
    background Frame("framy", 10, 10, 10, 10)
    xalign 0.5

style slot:
    background Frame("square", 0, 0)
    minimum (80, 80)
    maximum (80, 80)
    xalign 0.5

style stats_label_text:
    size 20
    color "#ffffff"
    font "leafy.otf"

style vitals_label_text:
    size 15
    color "#ffffff"
    font "leafy.otf"

image body_torn_tavern_apron = "body_tavern_apron"

default equipment_layered = {}
default equipment_layering = {}
screen stat_screen():
    $ crit_damage = round(pc.crit_damage, 3)
    $ crit_chance = round(pc.crit_chance, 3)
    frame:
        xpadding 30
        ypadding 20
        xpos 0.083
        ypos 0.51
        style "coolframe"
        has hbox
        spacing 15
        vbox:
            xmaximum 500
            spacing 15
            style_prefix "stats"

            label _("Damage: [pc.damage]")
            label _("Defense: [pc.defense]")
            label _("Dodge: [pc.dodge]")
            label _("Crit: [crit_damage]")
            label _("Gold: [pc.gold]")
            if pc.lvluppt > 0:
                label _("Level Point: [pc.lvluppt]")

        vbox:
            xmaximum 500
            spacing 15
            style_prefix "stats"

            label _("Flirt: [pc.lust_damage]")
            label _("Lust Resist: [pc.lust_defense]")
            label _("Lust Dodge: [pc.lust_dodge]")
            label _("Crit Chance: [pc.crit_chance]")
            label _("Accuracy: [pc.accuracy]")



    frame:
        xalign 0.02
        yalign 0.4
        xpadding 10
        ypadding 10
        style "coolframe"
        has vbox
        style_prefix "screen_content"
        spacing 12
        textbutton _("STR: [pc.stg]") xalign 0.0 hovered SetVariable("stat_description1", True) unhovered SetVariable("stat_description1", False) action NullAction()
        textbutton _("AGI: [pc.agi]") xalign 0.0 hovered SetVariable("stat_description2", True) unhovered SetVariable("stat_description2", False) action NullAction()
        textbutton _("INT: [pc.itg]") xalign 0.0 hovered SetVariable("stat_description3", True) unhovered SetVariable("stat_description3", False) action NullAction()
    frame:
        xalign 0.09
        yalign 0.4
        xpadding 10
        ypadding 10
        style "coolframe"
        has vbox
        style_prefix "screen_content"
        spacing 12
        textbutton _("TEN: [pc.ten]") xalign 0.0 hovered SetVariable("stat_description4", True) unhovered SetVariable("stat_description4", False) action NullAction()
        textbutton _("CHA: [pc.cha]") xalign 0.0 hovered SetVariable("stat_description5", True) unhovered SetVariable("stat_description5", False) action NullAction()
        textbutton _("PUR: [pc.cor]") xalign 0.0 hovered SetVariable("stat_description6", True) unhovered SetVariable("stat_description6", False) action NullAction()


    frame:
        style "coolframe"
        xmaximum 200
        ymaximum 300
        xalign 0.02
        yalign 0.14
        xpadding 20
        ypadding 20
        has vbox
        yalign 0.15
        spacing 6
        bar value AnimatedValue(pc.exp, pc.expCap)
        bar value AnimatedValue(pc.hp, pc.max_hp) left_bar Frame("left_red", 6, 6)
        bar value AnimatedValue(pc.mp, pc.max_mp) left_bar Frame("left_blue", 6, 6)
        bar value AnimatedValue(pc.lust, pc.max_lust) left_bar Frame("left_yellow", 6, 6)

    vbox:
        xmaximum 300
        ymaximum 400
        xpos 0.02
        ypos 0.03
        spacing 6
        frame:
            xalign 0.0
            style "coolframe"
            xpadding 50
            ypadding 10
            text "[e]" size 30 style_prefix "screen_content"
        if pc.level > levelCap:
            text _("Level [pc.level] (Max)") xalign 0.0 size 20 style_prefix "screen_content"
        else:
            text _("Level [pc.level]") xalign 0.0 size 20 style_prefix "screen_content"

    vbox:
        xmaximum 300
        ymaximum 600
        xpos 0.031
        ypos 0.122
        spacing 28
        style_prefix "vitals"

        label _("EXP: [pc.exp]/[pc.expCap]")
        label _("HP: [pc.hp]/[pc.max_hp]")
        label _("MP: [pc.mp]/[pc.max_mp]")
        label _("Lust: [pc.lust]/[pc.max_lust]")

    vbox:
        xmaximum 300
        spacing 12
        xpos 0.01
        ypos 0.51

        if stat_description1 == True:
            frame:
                label _("Strength (STR) determines [e]'s physical power, including Attack Damage, and small amount of HP and Defense.") xalign 0.0 xpadding 20 ypadding 10 text_size 30 text_color "#ffffff"
        if stat_description2 == True:
            frame:
                label _("Agility (AGI) determines [e]'s speed, including Hit Rate, Critical Damage, Critical Chance and Dodge Chance.") xalign 0.0 xpadding 20 ypadding 10 text_size 30 text_color "#ffffff"
        if stat_description3 == True:
            frame:
                label _("Intelligence (INT) determines [e]'s wisdom and spell abilities, including spell effectiveness, MP and Lust Resistance.") xalign 0.0 xpadding 20 ypadding 10 text_size 30 text_color "#ffffff"
        if stat_description4 == True:
            frame:
                label _("Tenacity (TEN) determines [e]'s endurance, including Defense and Lust Resistance.") xalign 0.0 xpadding 20 ypadding 10 text_size 30 text_color "#ffffff"
        if stat_description5 == True:
            frame:
                label _("Charisma (CHA) determines [e]'s appeal to other characters, including Flirt effectiveness.") xalign 0.0 xpadding 20 ypadding 10 text_size 30 text_color "#ffffff"
        if stat_description6 == True:
            frame:
                label _("Purity (PUR) determines [e]'s sexual innocence, and interaction with characters.") xalign 0.0 xpadding 20 ypadding 10 text_size 30 text_color "#ffffff"

    if pc.lvluppt > 0:
        vbox:
            spacing 35
            xpos 0.07
            ypos 0.36
            imagebutton:
                idle "plus"
                action Function(pc.addstat, 1)
            imagebutton:
                idle "plus"
                action Function(pc.addstat, 2)
            imagebutton:
                idle "plus"
                action Function(pc.addstat, 3)
        vbox:
            spacing 35
            xpos 0.145
            ypos 0.36
            imagebutton:
                idle "plus"
                action Function(pc.addstat, 4)
            imagebutton:
                idle "plus"
                action Function(pc.addstat, 5)

screen inventory_screen():
    tag menu_bar
    zorder 99
    style_prefix "inventory"

    add "inventorybackground"
    use stat_screen
    use sort_screen

    if not pinventory:
        frame:
            style "coolframe"
            xpos 0.62
            ypos 0.03
            xanchor 0
            xpadding 50
            ypadding 10
            text _("Inventory") xalign 1 style_prefix "screen_title"
    else:
        frame:
            style "coolframe"
            xpos 0.625
            ypos 0.03
            xanchor 0
            xpadding 50
            ypadding 10
            text _("Trinket") xalign 1.1 style_prefix "screen_title"


    $ equipment_list = [pc.armor["Mask"], pc.armor["Clothes"], pc.armor["Pants"], pc.armor["Accessory"], pc.armor["Bccessory"], pc.weapon]
    $ equipment_layered = {}
    for eq in equipment_list:
        if eq is not None:
            if eq.body_layer == "Robe 3 Parts":
                $ equipment_layered.setdefault("Head", []).append(eq)
                $ equipment_layered.setdefault("Cover", []).append(eq)
                $ equipment_layered.setdefault("Back", []).append(eq)
            $ equipment_layered.setdefault(eq.body_layer, []).append(eq)

    add "player_tail" xpos 0.20 ypos 0.032
    if "Cover" not in equipment_layered:
        add "player_left_arm" xpos 0.20 ypos 0.032
    add "player_left_leg" xpos 0.20 ypos 0.032
    add "player_body" xpos 0.20 ypos 0.032
    if pc.armor["Clothes"] is None or pc.armor["Clothes"].img != "Assistant Costume":
        add "player_cock_flaccid" xpos 0.20 ypos 0.032
    add "player_right_leg" xpos 0.20 ypos 0.032
    if "Cover" not in equipment_layered:
        add "player_right_arm" xpos 0.20 ypos 0.032
    if pc.armor["Mask"] == None or pc.armor["Mask"].img != "Enchanted Chaperon":
        add "player_head" xpos 0.20 ypos 0.032

    for slot_name in ["Back","Left Arm","Body","Trunk","Right Arm","Chest","Robe","Hands","Cover","Head"]:
        if slot_name in equipment_layered:
            for item in equipment_layered[slot_name]:
                if item.body_layer == "Robe 3 Parts":
                    if slot_name == "Back":
                        add "body_"+item.img.lower().replace(" ", "_")+"3":
                            xpos 0.20 ypos 0.032
                    if slot_name == "Cover":
                        add "body_"+item.img.lower().replace(" ", "_")+"1":
                            xpos 0.20 ypos 0.032
                    if slot_name == "Head":
                        add "body_"+item.img.lower().replace(" ", "_")+"2":
                            xpos 0.20 ypos 0.032

                else:
                    add "body_"+item.img.lower().replace(" ", "_"):
                        xpos 0.20 ypos 0.032


    if bag_show == True:
        imagebutton:
            xpos 0.20
            ypos 0.032
            idle "body_courier_bag"
            action SetVariable("bag_show", False)
    if bag_show == False:
        imagebutton:
            xpos 0.20
            ypos 0.032
            idle "body_empty"
            action SetVariable("bag_show", True)


    vbox:
        xmaximum 500
        spacing 15
        xpos 0.20
        ypos 0.10
        style_prefix "tap"
        frame:
            style "slot"
            if isinstance(pc.weapon, Equipable):
                imagebutton:
                    idle pc.weapon.img.lower()

                    hovered SetVariable("hovered_item", pc.weapon), SetVariable("hovered_item_num", -1), SetVariable("selected_equipment", pc.weapon)

                    action Function(pc.weapon.unequip)
            else:
                add "weapon_icon"
        frame:
            style "slot"
            if isinstance(pc.armor["Accessory"], Equipable):
                imagebutton:
                    idle pc.armor["Accessory"].img.lower()

                    hovered SetVariable("hovered_item", pc.armor["Accessory"]), SetVariable("hovered_item_num", -2), SetVariable("selected_equipment", pc.armor["Accessory"])
                    action Function(pc.armor["Accessory"].unequip)
            else:
                add "accessory_icon"

        frame:
            style "slot"
            if isinstance(pc.armor["Bccessory"], Equipable):
                imagebutton:
                    idle pc.armor["Bccessory"].img.lower()

                    hovered SetVariable("hovered_item", pc.armor["Bccessory"]), SetVariable("hovered_item_num", -3), SetVariable("selected_equipment", pc.armor["Bccessory"])
                    action Function(pc.armor["Bccessory"].unequip)
            else:
                add "accessory_icon"
    vbox:
        xmaximum 500
        spacing 15
        xpos 0.20
        ypos 0.40
        style_prefix "tap"
        frame:
            style "slot"
            if isinstance(pc.armor["Mask"], Equipable):
                imagebutton:
                    idle pc.armor["Mask"].img.lower()
                    hovered SetVariable("hovered_item", pc.armor["Mask"]), SetVariable("hovered_item_num", -4), SetVariable("selected_equipment", pc.armor["Mask"])
                    action Function(pc.armor["Mask"].unequip)
            else:
                add "mask_icon"

        frame:
            style "slot"
            if isinstance(pc.armor["Clothes"], Equipable):
                imagebutton:
                    idle pc.armor["Clothes"].img.lower()
                    hovered SetVariable("hovered_item", pc.armor["Clothes"]), SetVariable("hovered_item_num", -5), SetVariable("selected_equipment", pc.armor["Clothes"])
                    action Function(pc.armor["Clothes"].unequip)
            else:
                add "clothes_icon"

        frame:
            style "slot"
            if isinstance(pc.armor["Pants"], Equipable):
                imagebutton:
                    idle pc.armor["Pants"].img.lower()
                    hovered SetVariable("hovered_item", pc.armor["Pants"]), SetVariable("hovered_item_num", -6), SetVariable("selected_equipment", pc.armor["Pants"])
                    action Function(pc.armor["Pants"].unequip)
            else:
                add "pants_icon"

    if quest24.status == True:


        imagebutton:
            xalign 0.52
            yalign 0.03
            idle "trinket"
            hover "trinkethover"
            style "potion_button"
            action ToggleVariable("pinventory")

    if pinventory == 0:

        grid 6 8:
            xalign 0.745
            yalign 0.27
            for i in range(inventoryPage*48, inventoryPage*48+48):
                if i < len(inventory):
                    $ item = inventory[i]
                    frame:
                        style "slot"
                        if item != None:
                            if isinstance(item, Equipable):
                                imagebutton:
                                    idle item.img.lower()
                                    style "tap_button"
                                    hovered SetVariable("hovered_item", item), SetVariable("hovered_item_num", i), SetVariable("selected_item", item)
                                    action Function(item.equip,pc)
                            if isinstance(item, Consumable):
                                imagebutton:
                                    idle item.img.lower()
                                    style "potion_button"
                                    hovered SetVariable("hovered_item", item), SetVariable("hovered_item_num", i), SetVariable("selected_item", item)
                                    action Function(item.consume,pc)
                                text "[item.number]" style "invnumber_label"
                                if any(x.img == item.img for x in leveluppableconsumables):
                                    $ item_level = romnum(item.level)
                                    text "[item_level]" style "invlevel_label"
                            if isinstance(item, KeyItem):
                                imagebutton:
                                    idle item.img.lower()
                                    style "tap_button"
                                    hovered SetVariable("hovered_item", item), SetVariable("hovered_item_num", i), SetVariable("selected_item", item)
                                    action NullAction()
                            if isinstance(item, Material):
                                imagebutton:
                                    idle item.img.lower()
                                    style "material_button"
                                    hovered SetVariable("hovered_item", item), SetVariable("hovered_item_num", i), SetVariable("selected_item", item)
                                    action NullAction()
                                text "[item.number]" style "invnumber_label"
                            if isinstance(item, Learnable):
                                if item.learn_type == "Book":
                                    imagebutton:
                                        idle item.img.lower()
                                        style "tap_button"
                                        hovered SetVariable("hovered_item", item), SetVariable("hovered_item_num", i), SetVariable("selected_item", item)
                                        action [SetVariable("book_page", 0), Hide("inventory_screen"), Function(renpy.call_in_new_context, item.scroll.read if hasattr(item.scroll, "read") else item.scroll)]
                                elif item.learn_type == "Keepsake" or item.learn_type == "Special":
                                    imagebutton:
                                        idle item.img.lower()
                                        style "tap_button"
                                        hovered SetVariable("hovered_item", item), SetVariable("hovered_item_num", i), SetVariable("selected_item", item)
                                        action [Hide("inventory_screen"), Function(renpy.call_in_new_context, item.scroll)]
                                else:
                                    imagebutton:
                                        idle item.img.lower()
                                        style "tap_button"
                                        hovered SetVariable("hovered_item", item), SetVariable("hovered_item_num", i), SetVariable("selected_item", item)
                                        action Function(item.learn), Function(removeItem, item, inventory, 1)


            if len(inventory) <= (inventoryPage+1)*48:

                for i in range(48*(inventoryPage+1)-len(inventory)):
                    frame:

                        style "slot"
                        imagebutton:
                            idle "empty7"
                            hovered SetVariable("hovered_item", None)

        if len(inventory) > 48:
            $ nowPage = inventoryPage + 1
            text "[nowPage]" xalign 0.685 yalign 0.715 size 30 color "#eeeeee"
            $ numPage = (len(inventory) - (len(inventory) % 48)) / 48
            if inventoryPage < numPage:
                textbutton ">" xalign 0.73 yalign 0.715 text_size 30 text_color "#eeeeee" style "tap_button" action SetVariable("inventoryPage", inventoryPage + 1)
        if inventoryPage > 0:
            textbutton "<" xalign 0.63 yalign 0.715 text_size 30 text_color "#eeeeee" style "tap_button" action SetVariable("inventoryPage", inventoryPage - 1)

    else:

        vbox:
            xalign 0.52
            yalign 0.15
            spacing 15

            for i in range(len(pc.trinket)):
                $ item = pc.trinket[i]
                frame:
                    style "slot"
                    if item != None:
                        imagebutton:
                            idle item.img.lower().replace("'", "")
                            style "tap_button"
                            hovered SetVariable("hovered_item", item), SetVariable("selected_item", item), SetVariable("hovered_item_num", i+100000)
                            action Function(item.unequip)
                    else:
                        add "trk_ico"

        grid 6 4:
            xalign 0.745
            yalign 0.5773

            for item in tinventory:
                frame:
                    style "slot"
                    imagebutton:
                        idle item.img.lower()
                        style "tap_button"
                        hovered SetVariable("hovered_item", item), SetVariable("selected_item", item)
                        action Function(item.equip)

            for item in range(len(tinventory), 24):
                frame:
                    style "slot"

    if hovered_item != None:
        if pinventory == 0:
            if hovered_item_num >= 0:
                add "hovery":
                    pos (1073+(hovered_item_num%48%6)*80, 118+int(hovered_item_num%48/6)*80)
        elif hovered_item_num >= 0:
            if hovered_item_num >= 100000:
                add "hovery":
                    pos (958, 148+int((hovered_item_num-100000+1)%48/6)*80)
            else:
                add "hovery":
                    pos (1073+(hovered_item_num%48%6)*80, 438+int(hovered_item_num%48/6)*80)
        elif hovered_item_num > -4:
            add "hovery":
                pos (384, 13+int(abs(hovered_item_num))*95)
        else:
            add "hovery":
                pos (384, 52+int(abs(hovered_item_num))*95)
        use inventory_description(hovered_item)


    for i in range(len(pc.active_status)):
        $ j = pc.active_status[i]["Status"].lower()
        vbox:
            xalign 0.525
            yalign 0.645 - i*0.1
            imagebutton:
                idle j
                hovered SetVariable("selected_status", i)
                unhovered SetVariable("selected_status", None)
                action NullAction()

    if selected_status != None:
        $ k = pc.active_status[selected_status]["Description"]
        $ status_name = pc.active_status[selected_status]["Status"]
        $ status_expire_day = pc.active_status[selected_status]["Expire Day"] - timenow.day
        if timenow.hour > pc.active_status[selected_status]["Expire Hour"]:
            $ status_expire_day -= 1
        $ status_expire_hour = (pc.active_status[selected_status]["Expire Hour"] - timenow.hour) % 24
        if status_expire_day > 0:
            $ status_expire_date = _("\nExpires in [status_expire_day] days and [status_expire_hour] hours.")
        else:
            $ status_expire_date = _("\nExpires in [status_expire_hour] hours.")
        $ status_description = "[status_name!t]: [k!t]"
        frame:
            style "coolframe"
            xalign 0.525
            xmaximum 1000
            yalign 0.715 - selected_status*0.1
            xpadding 20
            ypadding 10
            label status_description+status_expire_date text_color "#eeeeee" style "invlevel_label"

label Storage_Screen:
    $ sort_message = [_("Sorted by Name in Ascending Order"), _("Sorted by Name in Descending Order"), _("Sorted by Value in Decending Order"), _("Sorted by Value in Ascending Order")]
    $ category_order = {Weapon:1, Armor:2, Equipable:3, Consumable:4, Learnable:5, KeyItem:6, Material:7}
    $ sort_num = 0
    $ storage_moveall = False
    $ cate_num = 0
    $ selected_item = None
    $ hovered_item = None
    jump Storage_Screen_Loop

label Storage_Screen_Loop:
    call screen Storage_Screen
    if _return == "Exit":
        show screen daytime()
        hide screen Storage_Screen
        jump main_bedroom
    if _return == "Deposit All":
        $ storage_gold += pc.gold
        $ pc.gold = 0
    if _return == "Withdraw All":
        $ pc.gold += storage_gold
        $ storage_gold = 0
    jump Storage_Screen_Loop

screen sort_screen():

    style_prefix "click"
    imagebutton:
        xalign 0.59
        yalign 0.03
        idle "sort_symbol"
        hover "sort_symbol_hover"

        action SetVariable("sort_num", sort_num+1), Notify(sort_message[sort_num%4]), Function(SortInventory, inventory, sort_num)

    imagebutton:
        xalign 0.79
        yalign 0.034
        idle "category_symbol"
        hover "category_symbol_hover"
        action SetVariable("cate_num", cate_num+1), Notify(_("Sorted by Item Type")), SetVariable("inventory", CategorizeInventory(inventory, cate_num, category_order))

screen moveall_screen():
    style_prefix "click"
    if storage_moveall == True:
        imagebutton:
            xalign 0.45
            yalign 0.025
            idle "moveall_on"
            action ToggleVariable("storage_moveall")
    else:
        imagebutton:
            xalign 0.45
            yalign 0.025
            idle "moveall_off"
            action ToggleVariable("storage_moveall")
screen Storage_Screen():

    add "inventorybackground"
    use stat_screen
    use moveall_screen
    use sort_screen
    frame:
        style "coolframe"
        xpos 0.62
        ypos 0.03
        xanchor 0
        xpadding 50
        ypadding 10
        text _("Inventory") xalign 1 style_prefix "screen_title"

    frame:
        style "coolframe"
        xpos 0.27
        ypos 0.03
        xanchor 0
        xpadding 50
        ypadding 10
        text _("Storage") xalign 1 style_prefix "screen_title"

    add "coin":
        pos (390, 80)

    text "[storage_gold]" xalign 0.22 yalign 0.074 size 30 color "edd3bf" font "leafy.otf"

    imagebutton:
        xalign 0.175
        yalign 0.074
        style "click_button"
        idle "deposit"
        action Return("Deposit All")

    imagebutton:
        xalign 0.19
        yalign 0.074
        style "click_button"
        idle "withdraw"
        action Return("Withdraw All")



    grid 6 8:
        xalign 0.745
        yalign 0.27
        for i in range(inventoryPage*48, inventoryPage*48+48):
            if i < len(inventory):
                $ item = inventory[i]
                frame:
                    style "slot"
                    if item != None:
                        imagebutton:
                            xalign 0.5
                            yalign 0.5
                            idle item.img.lower()
                            style "stash_button"
                            hovered SetVariable("hovered_item", item), SetVariable("hovered_item_num", i), SetVariable("selected_item", item), SetVariable("selected_myItem", "Sell")
                            action SetVariable("selected_item", item), Function(sellItem, item, storage, 1, storage_moveall)
                        if isinstance(item, Consumable) or isinstance(item, Material):
                            text "[item.number]" style "invnumber_label"

        if len(inventory) <= (inventoryPage+1)*48:

            for i in range(48*(inventoryPage+1)-len(inventory)):
                frame:
                    style "slot"

    if len(inventory) > 48:
        $ nowPage = inventoryPage + 1
        text "[nowPage]" xalign 0.385 yalign 0.715 size 30 color "#eeeeee"
        $ numPage = (len(inventory) - (len(inventory) % 48)) / 48
        if inventoryPage < numPage:
            textbutton ">" xalign 0.43 yalign 0.715 text_size 30 text_color "#eeeeee" style "tap_button" action SetVariable("inventoryPage", inventoryPage + 1)
    if inventoryPage > 0:
        textbutton "<" xalign 0.33 yalign 0.715 text_size 30 text_color "#eeeeee" style "tap_button" action SetVariable("inventoryPage", inventoryPage - 1)



    grid 9 8:
        xalign 0.275
        yalign 0.27
        for i in range(storagePage*72, storagePage*72+72):
            if i < len(storage):
                $ item = storage[i]
                frame:
                    style "slot"
                    if item != None:
                        imagebutton:
                            idle item.img.lower()
                            style "stash_button"
                            hovered SetVariable("hovered_item", item), SetVariable("hovered_item_num", -i-1), SetVariable("selected_item", item), SetVariable("selected_myItem", "Buy")
                            action SetVariable("selected_item", item), Function(buyItem, item, storage, 1, storage_moveall), SetVariable("selected_item", None), SetVariable("hovered_item", None)
                        if isinstance(item, Consumable) or isinstance(item, Material):
                            text "[item.number]" style "invnumber_label"

        if len(storage) <= (storagePage+1)*72:

            for i in range(72*(storagePage+1)-len(storage)):
                frame:
                    style "slot"

    if len(storage) > 72:
        $ nowPage = storagePage + 1
        text "[nowPage]" xalign 0.685 yalign 0.715 size 30 color "#eeeeee"
        $ numPage = (len(storage) - (len(storage) % 72)) / 72
        if storagePage < numPage:
            textbutton ">" xalign 0.73 yalign 0.715 style "tap_button" text_size 30 text_color "#eeeeee" action SetVariable("storagePage", storagePage + 1)
    if storagePage > 0:
        textbutton "<" xalign 0.63 yalign 0.715 style "tap_button" text_size 30 text_color "#eeeeee" action SetVariable("storagePage", storagePage - 1)

    if hovered_item != None:
        if hovered_item_num >= 0:
            add "hovery":
                pos (1073+(hovered_item_num%48%6)*80, 118+int(hovered_item_num%48/6)*80)
        else:
            add "hovery":
                pos (331+(abs(hovered_item_num+1)%72%9)*80, 118+int(abs(hovered_item_num+1)%72/9)*80)
        use inventory_description(hovered_item)



    textbutton _("Return") xalign 0.9 yalign 0.65 style_prefix "screen_storage" action Return("Exit")










screen inventory_description(item=None):
    vbox:
        xpos 1600
        yalign 0.035
        xmaximum 300
        spacing 20
        vbox:
            spacing 15
            frame:
                xpadding 10
                ypadding 10
                style "coolframe"
                text "[item.name!t]" style_prefix "screen_title"
            label "[item.description!t]" text_color "#eeeeee" text_size 25
            if LookForItem(item.img, leveluppableconsumables):
                label _("Current Level: [item.level]") text_color "#eeeeee" text_size 25
            if isinstance(item, Consumable) or isinstance(item, Weapon) or isinstance(item, Equipable):
                for stat_num in range(len(stat_names)):
                    $ itemStatName = stat_names[stat_num]

                    $ itemStatValue = item.stat[stat_num]
                    if itemStatValue > 0:
                        label "[itemStatName!t] : +[itemStatValue]" text_color "#eeeeee" text_size 25
                    elif itemStatValue < 0:
                        label "[itemStatName!t] : [itemStatValue]" text_color "#eeeeee" text_size 25
        if not isinstance(item, Trinket) and item != None:
            label _("Value: [item.value] Gold") text_color "#eeeeee" text_size 25

screen whinventory_screen():
    default wh_hovered_item = None

    add "inventoryonly"
    use sort_screen
    grid 6 8:
        xalign 0.745
        yalign 0.27
        for i in range(inventoryPage*48, inventoryPage*48+48):
            if i < len(inventory):
                $ item = inventory[i]
                frame:
                    style "slot"
                    if item != None:
                        imagebutton:
                            idle item.img.lower()
                            hover "hovering"
                            style "tap_button"
                            hovered SetScreenVariable("wh_hovered_item", item), SetVariable("selected_item", item), SetVariable("selected_myItem", "Sell")
                            action Function(whmoveItem, item, mimic_num), Return("Refresh")
                        if isinstance(item, Consumable) or isinstance(item, Material):
                            label "[item.number]" xalign 0.1 yalign 0.1 text_size 30 text_color "#eeeeee"

        if len(inventory) <= (inventoryPage+1)*48:

            for i in range(48*(inventoryPage+1)-len(inventory)):
                frame:
                    style "slot"

    if len(inventory) > 48:
        $ nowPage = inventoryPage + 1
        text "[nowPage]" xalign 0.685 yalign 0.715 size 30 color "#eeeeee"
        $ numPage = (len(inventory) - (len(inventory) % 48)) / 48
        if inventoryPage < numPage:
            textbutton ">" xalign 0.73 yalign 0.715 text_size 30 text_color "#eeeeee" action SetVariable("inventoryPage", inventoryPage + 1)
    if inventoryPage > 0:
        textbutton "<" xalign 0.63 yalign 0.715 text_size 30 text_color "#eeeeee" action SetVariable("inventoryPage", inventoryPage - 1)





    if wh_hovered_item != None:
        vbox:
            xpos 1600
            yalign 0.035
            xmaximum 300
            spacing 20
            frame:
                xpadding 10
                ypadding 10
                label "[wh_hovered_item.name!t]" text_color "#301410"
            label "[wh_hovered_item.description!t]" text_color "#eeeeee"
            if hasattr(wh_hovered_item, "value"):
                label _("Value: [wh_hovered_item.value] Gold") text_color "#eeeeee"

    frame:
        xalign 0.9
        yalign 0.65
        ymaximum 200
        textbutton _("Return") text_size 30 text_color "#eeeeee" action Jump("Whispering_Hollow_Loop"), Hide("whinvetory_screen")

    if pillar_item[mimic_num] != None:
        frame:
            xalign 0.9
            yalign 0.55
            ymaximum 200
            textbutton _("Retrieve") text_size 30 text_color "#eeeeee" action Function(whretrieveItem, mimic_num), Return("Refresh")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
