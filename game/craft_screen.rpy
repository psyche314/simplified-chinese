style screen_title_text:
    size 40
    color "#edd3bf"
    font "kingthing.ttf"

style screen_content_text:
    color "#edd3bf"
    font "kingthing.ttf"

style screen_content_white_text:
    color "#eeeeee"
    font "leafy.otf"

style screen_content_yellow_text:
    color "#edd3bf"
    font "leafy.otf"

screen craft_screen():
    tag craft
    add "shopbackground"

    frame:
        style "coolframe"
        xpos 0.69
        ypos 0.03
        xanchor 0.5
        xpadding 50
        ypadding 10
        text _("Inventory") xalign 1 style_prefix "screen_title"
    frame:
        style "coolframe"
        xalign 0.95
        yalign 0.63
        xpadding 10
        ypadding 10
        textbutton _("Leave") action Hide("craft_screen"), Jump("main_rahimshop"), Show("daytime") style_prefix "footstep"

    frame:
        style "coolframe"
        xalign 0.03
        yalign 0.03
        xpadding 50
        ypadding 10
        text _("Recipes") xalign 1 style_prefix "screen_title"

    viewport:
        xpos 0.015 ypos 0.12
        xminimum 0
        xmaximum 260
        ymaximum 610
        child_size (None, 1000)
        xfill True
        draggable True
        mousewheel True
        arrowkeys True
        scrollbars "vertical"
        has vbox
        xalign 0.6
        spacing 10
        for i in discoveredrecipe:
            if isinstance(i, Recipe):
                hbox:
                    style_prefix "page"
                    frame:
                        style "slot"
                        imagebutton:
                            idle i.product.img.lower()
                            action SetVariable("selected_recipe", i)
                    if i.checkAvailable() == True:
                        textbutton " >    [i.product.name!t]" action SetVariable("selected_recipe", i)
                    else:
                        textbutton " -   [i.product.name!t]" action SetVariable("selected_recipe", i) text_color "#301410"



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
                            style "tap_button"
                            xalign 0.5
                            yalign 0.5
                            idle item.img.lower()
                            hovered SetVariable("hovered_item", item), SetVariable("hovered_item_num", i)
                            action NullAction()
                        if isinstance(item, Consumable) or isinstance(item, Material):
                            text "[item.number]" style "invnumber_label"
                            if any(x.img == item.img for x in leveluppableconsumables):
                                $ item_level = romnum(item.level)
                                text "[item_level]" style "invlevel_label"

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

    if len(inventory) == inventoryPage*48 and len(inventory) != 0:
        $ inventoryPage -= 1

    if selected_recipe != None:
        vbox:
            xalign 0.24
            yalign 0.1
            spacing 20
            frame:
                style "slot"
                imagebutton:
                    style "tap_button"
                    idle selected_recipe.comp1.img.lower()
                    hovered SetVariable("hovered_item", selected_recipe.comp1)
                    action NullAction()
            if selected_recipe.comp2 != None:
                frame:
                    style "slot"
                    imagebutton:
                        style "tap_button"
                        idle selected_recipe.comp2.img.lower()
                        hovered SetVariable("hovered_item", selected_recipe.comp2)
                        action NullAction()

            if selected_recipe.comp3 != None:
                frame:
                    style "slot"
                    imagebutton:
                        style "tap_button"
                        idle selected_recipe.comp3.img.lower()
                        hovered SetVariable("hovered_item", selected_recipe.comp3)
                        action NullAction()

        vbox:
            xalign 0.34
            yalign 0.11
            spacing 70
            style_prefix "screen_content"
            if selected_recipe.comp1 != None:
                $ item_num = LookForItemNumber(selected_recipe.comp1.img, inventory)
                if item_num >= selected_recipe.num1:
                    text "[selected_recipe.comp1.name!t] : [item_num] / [selected_recipe.num1]" xanchor 0
                else:
                    text "[selected_recipe.comp1.name!t] : [item_num] / [selected_recipe.num1]" color "#da5d5d" xanchor 0
            if selected_recipe.comp2 != None:
                $ item_num = LookForItemNumber(selected_recipe.comp2.img, inventory)
                if item_num >= selected_recipe.num2:
                    text "[selected_recipe.comp2.name!t] : [item_num] / [selected_recipe.num2]" xanchor 0
                else:
                    text "[selected_recipe.comp2.name!t] : [item_num] / [selected_recipe.num2]" color "#da5d5d" xanchor 0
            if selected_recipe.comp3 != None:
                $ item_num = LookForItemNumber(selected_recipe.comp3.img, inventory)
                if item_num >= selected_recipe.num3:
                    text "[selected_recipe.comp3.name!t] : [item_num] / [selected_recipe.num3]" xanchor 0
                else:
                    text "[selected_recipe.comp3.name!t] : [item_num] / [selected_recipe.num3]" color "#da5d5d" xanchor 0


        frame:
            xalign 0.28
            yalign 0.56
            style "framy"
            xpadding 50
            ypadding 30
            xmaximum 650
            xminimum 650
            yminimum 310
            has vbox
            yalign 0.3
            label "[selected_recipe.product.description!t]" text_color "#3b2a25" text_size 25
            if LookForItem(selected_recipe.product.img, leveluppableconsumables):
                label _("Current Level: [selected_recipe.product.level]") text_color "#3b2a25" text_size 25
                $ csgo = ""
                for i in range(len(selected_recipe.product.stat)):
                    $ j = selected_recipe.product.stat[i]
                    if j > 0:
                        $ csgo += "{p} - " + stat_names[i] +": " + str(j)
                label "[csgo!t]" text_color "#3b2a25" text_size 25

        frame:
            xalign 0.24
            yalign 0.41
            style "coolframe"
            xpadding 50
            ypadding 10
            text "[selected_recipe.product.name!t]" style_prefix "screen_content"




        if selected_recipe.checkAvailable() == True:
            if selected_recipe.checkMulticraftAvailable():
                frame:
                    style "coolframe"
                    xalign 0.35
                    yalign 0.63
                    xpadding 10
                    ypadding 10
                    textbutton _("Craft All") action Function(selected_recipe.multicraft) style_prefix "stash"

                frame:
                    style "coolframe"
                    xalign 0.45
                    yalign 0.63
                    xpadding 10
                    ypadding 10
                    textbutton _("Craft One") action Function(selected_recipe.craft) style_prefix "stash"

            else:
                frame:
                    style "coolframe"
                    xalign 0.45
                    yalign 0.63
                    xpadding 10
                    ypadding 10
                    textbutton _("Craft") action Function(selected_recipe.craft) style_prefix "stash"


        else:
            frame:
                style "coolframe"
                xalign 0.45
                yalign 0.63
                xpadding 10
                ypadding 10
                textbutton _("Craft") action Notify(_("You do not have enough materials to craft this item.")) style_prefix "click"


    if hovered_item != None:

        add "hovery":
            pos (1073+(hovered_item_num%48%6)*80, 118+int(hovered_item_num%48/6)*80)

        vbox:
            xpos 1600
            yalign 0.035
            xmaximum 300
            spacing 20
            frame:
                style "coolframe"
                xpadding 10
                ypadding 10
                text "[hovered_item.name!t]" style_prefix "screen_content"
            label "[hovered_item.description!t]" text_color "#eeeeee" text_size 25
            if LookForItem(hovered_item.img, leveluppableconsumables):
                label _("Current Level: [hovered_item.level]") text_color "#eeeeee" text_size 25
                $ csgo = ""
                for i in range(len(hovered_item.stat)):
                    $ j = hovered_item.stat[i]
                    if j > 0:
                        $ csgo += "{p} - " + stat_names[i] +": " + str(j)
                label "[csgo!t]" text_color "#eeeeee" text_size 25

label Cauldron_Screen:
    scene cauldron_bg with dissolve
    $ selected_recipe = None
    $ selected_recipee = None
    $ hovered_item = None
    $ hovered_item_num = -1
    jump Cauldron_Screen_Loop

label Cauldron_Screen_Loop:
    call screen cauldron_screen()
    if _return == "Exit":
        hide screen cauldron_screen
        jump main_ardent_cauldron
    if _return == "Level Up":
        show screen cauldron_screen()
        "You've successfully increased [selected_recipe.name!t]'s Level!"


    jump Cauldron_Screen_Loop

screen cauldron_screen():
    frame:
        xpadding 10
        ypadding 10
        style "coolframe"
        xalign 0.015
        yalign 0.10
        text _("Dynamic Potions") style_prefix "screen_title"
    frame:
        xalign 0.01
        yalign 0.22
        xpadding 10
        ypadding 10
        style "coolframe"
        has grid 3 3

        spacing 10
        $ consumable_num = 0
        for item in inventory:
            if LookForItem(item.img, leveluppableconsumables):
                $ consumable_num += 1
                frame:
                    style "slot"
                    $ item_level = romnum(item.level)
                    imagebutton:
                        style "tap_button"
                        idle item.img.lower()
                        hovered SetVariable("hovered_item_num", consumable_num-1)
                        action SetVariable("selected_recipe", item), SetVariable("hovered_item", item)
                    label "[item_level]" xalign 0.85 yalign 0.9 text_size 30 text_color "#eeeeee" text_outlines [(absolute(1), "#000")]

        for i in range(9-consumable_num):
            frame:
                style "slot"
                imagebutton:
                    idle "missingitem"
                    hovered SetVariable("hovered_item_num", consumable_num+i)
                    action NullAction()

    if selected_recipe != None and LookForItem(selected_recipe.img, leveluppableconsumables):
        $ selected_recipee = selected_recipe.recipe
        frame:
            xpadding 10
            ypadding 10
            style "coolframe"
            xalign 0.24
            yalign 0.1
            text _("Level Up Ingredients:") style_prefix "screen_title"

        $ component_num0 = LookForItemNumber(selected_recipe.img, inventory)
        text "- [component_num0] / [selected_recipee.product_num]" xalign 0.52 yalign 0.67 style_prefix "screen_content_white"
        frame:
            xalign 0.47
            yalign 0.67
            style "slot"

            imagebutton:
                style "tap_button"
                idle selected_recipe.img.lower()
                hovered SetVariable("hovered_item", selected_recipe), SetVariable("hovered_item_num", 10)
                action NullAction()
            if any(x.img == selected_recipe.img for x in leveluppableconsumables):
                $ item_level = romnum(selected_recipe.level)
                label "[item_level]" xalign 0.85 yalign 0.9 text_size 30 text_color "#eeeeee" text_outlines [(absolute(1), "#000")]

        $ component_num1 = LookForItemNumber(selected_recipee.comp1.img, inventory)
        text "- [component_num1] / [selected_recipee.num1]" xalign 0.32 yalign 0.24 style_prefix "screen_content_white"
        frame:
            xalign 0.27
            yalign 0.24
            style "slot"

            imagebutton:
                style "tap_button"
                idle selected_recipee.comp1.img.lower()
                hovered SetVariable("hovered_item", selected_recipee.comp1), SetVariable("hovered_item_num", 11)
                action NullAction()

        if selected_recipee.comp2 != None:
            $ component_num2 = LookForItemNumber(selected_recipee.comp2.img, inventory)
            text "- [component_num2] / [selected_recipee.num2]" xalign 0.72 yalign 0.24 style_prefix "screen_content_white"
            frame:
                xalign 0.67
                yalign 0.24
                style "slot"

                imagebutton:
                    style "tap_button"
                    idle selected_recipee.comp2.img.lower()
                    hovered SetVariable("hovered_item", selected_recipee.comp2), SetVariable("hovered_item_num", 12)
                    action NullAction()
        if selected_recipee.comp3 != None:
            $ component_num3 = LookForItemNumber(selected_recipee.comp3.img, inventory)
            text "- [component_num3] / [selected_recipee.num3]" xalign 0.52 yalign 0.16 style_prefix "screen_content_white"
            frame:
                xalign 0.47
                yalign 0.16
                style "slot"
                imagebutton:
                    style "tap_button"
                    idle selected_recipee.comp3.img.lower()
                    hovered SetVariable("hovered_item", selected_recipee.comp3), SetVariable("hovered_item_num", 13)
                    action NullAction()

    if selected_recipee != None and LookForItem(selected_recipe.img, leveluppableconsumables):
        if selected_recipee.product.level >= 5:
            frame:
                style "coolframe"
                xalign 0.9
                yalign 0.5
                xpadding 20
                ypadding 15
                textbutton _("{s}Level Up{s}") action Notify(_("The item's level is currently maxed!")) style_prefix "stash"
        elif selected_recipee.checkAvailableLevel() == True:
            frame:
                style "coolframe"
                xalign 0.9
                yalign 0.5
                xpadding 20
                ypadding 15
                textbutton _("Level Up") action Function(selected_recipee.levelUp), Return("Level Up") style_prefix "stash"
        else:
            frame:
                style "coolframe"
                xalign 0.9
                yalign 0.5
                xpadding 20
                ypadding 15
                textbutton _("{s}Level Up{s}") action Notify(_("You have insufficient ingredients.")) style_prefix "stash"

    if hovered_item_num >= 0 and hovered_item_num < 10:
        add "hovery":
            pos (27+(hovered_item_num%3)*90, 187+int(hovered_item_num/3)*90)
    elif hovered_item_num == 10:
        add "hovery":
            pos (0.45, 0.62)
    elif hovered_item_num == 11:
        add "hovery":
            pos (0.26, 0.223)
    elif hovered_item_num == 12:
        add "hovery":
            pos (0.643, 0.223)
    elif hovered_item_num == 13:
        add "hovery":
            pos (0.45, 0.146)

    if hovered_item != None:
        frame:
            xalign 0.82
            yalign 0.05
            style "slot"

            imagebutton:
                idle hovered_item.img.lower()
                action NullAction()
        vbox:
            xpos 1600
            yalign 0.035
            xmaximum 300
            spacing 20
            frame:
                xpadding 10
                ypadding 10
                style "coolframe"
                text "[hovered_item.name!t]" style_prefix "screen_title"

            label "[hovered_item.description!t]" text_color "#eeeeee" text_size 25

            if selected_recipe != None and selected_recipe.recipe != None and hovered_item.img == selected_recipe.img:
                label _("Current Level: [hovered_item.level]") text_color "#eeeeee"
                $ csgo = _("Next Level Effect:")
                for i in range(len(selected_recipee.product.stat)):
                    $ j = selected_recipe.stat[i]
                    if j > 0:
                        $ poggy = selected_recipe.recipe.multiplier[0] * selected_recipe.recipe.multiplier[1]
                        $ poggy = j + int(poggy)
                        $ csgo += "{p} - " +stat_names[i] +": " + str(j) + " -> " + str(poggy)
                label "[csgo!t]" text_color "#eeeeee"
    frame:
        xalign 0.9
        yalign 0.75
        xpadding 20
        ypadding 15
        style "coolframe"
        ymaximum 200
        textbutton _("Return") text_color "#edd3bf" text_hover_color "#312e2e" style "stash_button" action Return("Exit")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
