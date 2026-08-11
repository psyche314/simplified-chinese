image sebas cropped = Crop((0, 0, 1080, 744), "sebas grin")
image gwyddyon cropped = Crop((0, 0, 1080, 744), "gwyddyon normal")
image methis cropped = Crop((0, 0, 1080, 744), "methis normal")

screen shop_screen(merchant):
    tag shop
    zorder 91

    use moveall_screen
    if merchant == "Sebas":
        $ minventory = sebasInventory
        $ premium = 0.8
        frame:
            style "coolframe"
            xpadding 10
            ypadding 10
            xalign 0.025
            yalign 0.035
            text _("The King's Pawn") style "screen_content_text"
        imagebutton:
            xpos 0.06
            ypos 0.023
            idle "sebas cropped"

    elif merchant == "Gwyddyon":
        $ minventory = gwyddyonInventory
        $ premium = 0.75
        frame:
            style "coolframe"
            xpadding 10
            ypadding 10
            xalign 0.015
            yalign 0.035
            text _("The Ardent Cauldron") style "screen_content_text"
        imagebutton:
            xpos 0.06
            ypos 0.023
            idle "gwyddyon cropped"

    else:
        $ minventory = methisInventory
        $ premium = 0.7
        frame:
            style "coolframe"
            xpadding 10
            ypadding 10
            xalign 0.015
            yalign 0.035
            text _("The Finnkel's Gaze") style "screen_content_text"
        imagebutton:
            xpos 0.06
            ypos 0.023
            idle "methis cropped"
    if pc.armor["Accessory"] != None and pc.armor["Accessory"].img == "Hagglers Amulet":
        $ premium *= 1.05

    textbutton _("Leave") xalign 0.9 yalign 0.6 style_prefix "pling" action Return("Return")
    frame:
        style "coolframe"
        xpadding 15
        ypadding 15
        xalign 0.7
        yalign 0.035
        text _("Inventory") style "screen_content_text"



    text _("Gold: [pc.gold]") xalign 0.88 yalign 0.68 style "screen_content_yellow_text"

    grid 6 8:
        xalign 0.745
        yalign 0.27
        for i in range(inventoryPage*48, inventoryPage*48+48):
            if i < len(inventory):
                $ item = inventory[i]
                frame:
                    style "slot"
                    if isinstance(item, Equipable):
                        imagebutton:
                            idle item.img.lower()
                            hovered SetVariable("hovered_item_num", i)
                            style "tap_button"
                            action SetVariable("selected_shopItem", item), SetVariable("selected_myItem", "Sell"), Return("Sell_Equipable")
                    if isinstance(item, Consumable):
                        imagebutton:
                            idle item.img.lower()
                            hovered SetVariable("hovered_item_num", i)
                            style "potion_button"
                            action SetVariable("selected_shopItem", item), SetVariable("selected_myItem", "Sell"), Return("Sell_Consumable")
                        text "[item.number]" style "invnumber_label"
                        if next((x for x in leveluppableconsumables if item.img == x.img), None) != None:
                            $ item_level = romnum(item.level)
                            text "[item_level]" style "invlevel_label"
                    if isinstance(item, KeyItem):
                        imagebutton:
                            idle item.img.lower()
                            hovered SetVariable("hovered_item_num", i)
                            style "tap_button"
                            action SetVariable("selected_shopItem", item), SetVariable("selected_myItem", "Sell"), Return("Sell_KeyItem")
                    if isinstance(item, Material):
                        imagebutton:
                            idle item.img.lower()
                            hovered SetVariable("hovered_item_num", i)
                            style "material_button"
                            action SetVariable("selected_shopItem", item), SetVariable("selected_myItem", "Sell"), Return("Sell_Material")
                        text "[item.number]" style "invnumber_label"
                    if isinstance(item, Learnable):
                        imagebutton:
                            idle item.img.lower()
                            hovered SetVariable("hovered_item_num", i)
                            style "tap_button"
                            action SetVariable("selected_shopItem", item), SetVariable("selected_myItem", "Sell"), Return("Sell_Learnable")

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

    grid 3 8:
        xalign 0.025
        yalign 0.27
        for i in range(sebasInventoryPage*24, sebasInventoryPage*24+24):
            if i < len(minventory):
                $ item = minventory[i]
                frame:
                    style "slot"
                    if isinstance(item, Equipable):
                        imagebutton:
                            idle item.img.lower()
                            hovered SetVariable("hovered_item_num", -i-1)
                            style "tap_button"
                            action SetVariable("selected_shopItem", item), SetVariable("selected_myItem", "Buy"), Return("Buy_Equipable")
                    if isinstance(item, Consumable):
                        imagebutton:
                            idle item.img.lower()
                            hovered SetVariable("hovered_item_num", -i-1)
                            style "potion_button"
                            action SetVariable("selected_shopItem", item), SetVariable("selected_myItem", "Buy"), Return("Buy_Consumable")
                        text "[item.number]" style "invnumber_label"
                        if next((x for x in leveluppableconsumables if item.img == x.img), None) != None:
                            $ item_level = romnum(item.level)
                            text "[item_level]" style "invlevel_label"
                    if isinstance(item, KeyItem):
                        imagebutton:
                            idle item.img.lower()
                            hovered SetVariable("hovered_item_num", -i-1)
                            style "tap_button"
                            action SetVariable("selected_shopItem", item), SetVariable("selected_myItem", "Buy"), Return("Buy_KeyItem")
                    if isinstance(item, Material):
                        imagebutton:
                            idle item.img.lower()
                            hovered SetVariable("hovered_item_num", -i-1)
                            style "material_button"
                            action SetVariable("selected_shopItem", item), SetVariable("selected_myItem", "Buy"), Return("Buy_Material")
                        text "[item.number]" style "invnumber_label"
                    if isinstance(item, Learnable):
                        imagebutton:
                            idle item.img.lower()
                            hovered SetVariable("hovered_item_num", -i-1)
                            style "tap_button"
                            action SetVariable("selected_shopItem", item), SetVariable("selected_myItem", "Buy"), Return("Buy_Learnable")


        if len(minventory) <= (sebasInventoryPage+1)*24:
            for i in range(24*(sebasInventoryPage+1)-len(minventory)):
                frame:
                    style "slot"

    if len(minventory) > 24:
        $ nowPage = sebasInventoryPage + 1
        text "[nowPage]" xalign 0.085 yalign 0.715 size 30 color "#eeeeee"
        $ numPage = (len(minventory) - (len(minventory) % 24)) / 24
        if sebasInventoryPage < numPage:
            textbutton ">" xalign 0.13 yalign 0.715 text_size 30 text_color "#eeeeee" style "click_button" action SetVariable("sebasInventoryPage", sebasInventoryPage + 1)
        if sebasInventoryPage > 0:
            textbutton "<" xalign 0.03 yalign 0.715 text_size 30 text_color "#eeeeee" style "click_button" action SetVariable("sebasInventoryPage", sebasInventoryPage - 1)

    if hovered_item_num != None:
        if hovered_item_num >= 0:
            add "hovery":
                pos (1073+(hovered_item_num%48%6)*80, 118+int(hovered_item_num%48/6)*80)
        else:
            add "hovery":
                pos (43+(abs(hovered_item_num+1)%24%3)*80, 118+int(abs(hovered_item_num+1)%24/3)*80)

    if selected_shopItem != None:


        use inventory_description(selected_shopItem)

        if selected_myItem == "Sell":
            if storage_moveall:
                $ sell_value = selected_shopItem.value*selected_shopItem.number
            else:
                $ sell_value = selected_shopItem.value
            text _("Sell Value: [sell_value]") xalign 0.98 yalign 0.68 style "screen_content_yellow_text"
            if selected_shopItem.number == 1:
                frame:
                    xalign 0.96
                    yalign 0.6
                    xpadding 20
                    ypadding 15
                    style "coolframe"
                    textbutton _("Sell") text_color "#edd3bf" style "kaching_button" action Function(sellItem, selected_shopItem, minventory, premium), Return("Sell_Success")
            elif selected_shopItem.number > 1:
                frame:
                    xalign 0.96
                    yalign 0.6
                    xpadding 20
                    ypadding 15
                    style "coolframe"
                    textbutton _("Sell") text_color "#edd3bf" style "kaching_button" action Function(sellItem, selected_shopItem, minventory, premium, storage_moveall), Return("Sell_Success")


        if selected_myItem == "Buy":
            if storage_moveall:
                $ buy_value = selected_shopItem.value*selected_shopItem.number
            else:
                $ buy_value = selected_shopItem.value
            text _("Buy Value: [buy_value]") xalign 0.98 yalign 0.68 style "screen_content_yellow_text"
            if pc.gold >= buy_value:
                if selected_shopItem.number == 1:
                    frame:
                        xalign 0.96
                        yalign 0.6
                        xpadding 20
                        ypadding 15
                        style "coolframe"
                        textbutton _("Buy") text_color "#edd3bf" style "kaching_button" action Function(buyItem, selected_shopItem, minventory, premium), Return("Buy_Success")
                elif selected_shopItem.number > 1:
                    frame:
                        xalign 0.96
                        yalign 0.6
                        xpadding 20
                        ypadding 15
                        style "coolframe"
                        textbutton _("Buy") text_color "#edd3bf" style "kaching_button" action Function(buyItem, selected_shopItem, minventory, premium, storage_moveall), Return("Buy_Success")


label Sebas_Shopping:
    $ sebasInventoryPage = 0
    if quest11.status == True and canvasrecipe not in discoveredrecipe:
        $ discoveredrecipe.append(canvasrecipe)
    if pc.armor["Accessory"] != None and pc.armor["Accessory"].img == "Hagglers Amulet":
        $ value_mult = 0.9
    else:
        $ value_mult = 1
    if sebas_restock < timenow.day:
        $ sebas_restock = int(timenow.day / 7) * 7 + 5

        $ rnd = 30 - LookForItemNumber("Red Berry", sebasInventory)
        if rnd > 0:
            $ addItem("Red Berry", sebasInventory, rnd, value_mult)

        $ rnd = 30 - LookForItemNumber("Blue Berry", sebasInventory)
        if rnd > 0:
            $ addItem("Blue Berry", sebasInventory, rnd, value_mult)

        $ rnd = 12 - LookForItemNumber("Small Cloth", sebasInventory)
        if rnd > 0:
            $ addItem("Small Cloth", sebasInventory, rnd, value_mult)

        $ rnd = 3 - LookForItemNumber("Patch", sebasInventory)
        if rnd > 0:
            $ addItem("Patch", sebasInventory, rnd, value_mult)
        if checkNoShopItem("Small Axe"):
            $ addItem("Small Axe", sebasInventory, 1, value_mult)
        if quest01.status == True and checkNoShopItem("Wooden Bow"):
            $ addItem("Wooden Bow", sebasInventory, 1, value_mult)
        if quest11.status == True and checkNoShopItem("Knight Breastplate"):
            $ addItem("Knight Breastplate", sebasInventory, 1, value_mult)
        if quest10.status == True:
            $ rnd = 30 - LookForItemNumber("Hemp", sebasInventory)
            if rnd > 0:
                $ addItem("Hemp", sebasInventory, rnd, value_mult)
        if quest37.status == True and checkNoShopItem("Iron Greatsword"):
            $ addItem("Iron Greatsword", sebasInventory, 1, value_mult)
        if quest37.status == True and checkNoShopItem("Woven Tunic"):
            $ addItem("Woven Tunic", sebasInventory, 1, value_mult)
        if quest08.status == True:
            $ rnd = 10 - LookForItemNumber("Green Ointment", sebasInventory)
            $ searchForItemAttr("Green Ointment", "value", 120)
            if rnd > 0:
                $ addItem("Green Ointment", sebasInventory, rnd, value_mult)
        if quest15.status == True:
            $ rnd = 30 - LookForItemNumber("Ginger", sebasInventory)
            if rnd > 0:
                $ addItem("Ginger", sebasInventory, rnd, value_mult)
    if quest01.status == True:
        if fierycharge not in learnedabilities and not LookForItem("Book of Fiery Charge", inventory) and not LookForItem("Book of Fiery Charge", sebasInventory):
            $ addItem("Book of Fiery Charge", sebasInventory, 1, value_mult)
    if quest14.status == True:
        if alluringlust not in learnedabilities:
            $ learnedabilities.append(alluringlust)
    if quest17.status == True:
        if camouflage not in learnedabilities:
            $ learnedabilities.append(camouflage)
        if corestrike not in learnedabilities:
            $ learnedabilities.append(corestrike)

    $ stunned = Effect(_("Stunned"), "Stunned", _("Stunned: {p} Target cannot perform anything while you are stunned"), "N", 0, 1, 1)
    $ fortifying.cost = 10
    if quest11.status == True:
        $ kechioeren.discovered = True
    hide screen daytime
    hide screen menu_buttons
    show screen shop_screen("Sebas")
    scene shopbackground
    $ selected_shopItem = None
    $ selected_myItem = None
    s "Take a look, here's our finest collections in the shop."
    jump Sebas_Shopping_Loop


label Sebas_Shopping_Loop:
    $ shop_action = ui.interact()
    if shop_action == "Return":
        show screen daytime()
        show screen menu_buttons()
        hide screen shop_screen 
        jump main_kingspawn
    $ lll = selected_shopItem.img
    $ mmm = selected_shopItem.value
    $ ttt = selected_shopItem.name
    if shop_action == "Buy_Material":
        if selected_shopItem.img == "Small Cloth":
            s "Rahim sells me this Cloth a lot, seems to be a very popular components of many everyday items. Its [selected_shopItem.value] gold now."
        if selected_shopItem.img == "Hemp":
            s "It's funny when I smell this one. I don't know what's inside that made me trip... Saw some traders smoke this stuff though. so... I'll make it [mmm] gold for you?"
    if shop_action == "Buy_Learnable":
        if selected_shopItem.img == "Book of Fiery Charge":
            s "This one's from the collection of Ole. He had already sold most of them, but this one, well. Roomie you gotta have to buy this fire spell thingy, only for [selected_shopItem.value] gold!"
    if shop_action == "Buy_Consumable":
        if selected_shopItem.img == "Small HP Potion":
            s "This health potion is handmade from the most talented potion maker in the whole province of Mokken! Just [selected_shopItem.value] gold for you!"
        if selected_shopItem.img == "Green Ointment":
            s "My precious Ole made these himself, he says it cleanses all your negative effect... Its [selected_shopItem.value] gold now."
    if shop_action == "Buy_Equipable":
        if selected_shopItem.img == "Small Axe":
            s "Ahhh... if you have an axe to grind, it's probably the best one out there, no lie. And only [selected_shopItem.value] for you!"
        if selected_shopItem.img == "Lion Charm":
            s "Hey! That's a little charm of me! It's only [selected_shopItem.value] gold for you now! In case you wanna bring this cute version of me with you to your little adventure!"
        if selected_shopItem.img == "Knight Breastplate":
            s "Ha, this one I picked it up from the most famous merchant from the town, it's very expensive. But... [mmm] gold for my favourite buddy."
        if selected_shopItem.img == "Wooden Bow":
            s "Let me tell you a secret, this bow, along with many other bows, comes with their arrows. So, no more worries about forgetting to buy your arrows! Just for [mmm] gold!"
        if selected_shopItem.img == "Iron Greatsword":
            s "This greatsword is a bit too heavy for me to carry around, but I think you can handle it, roomie. It's only [mmm] gold for you!"
        if selected_shopItem.img == "Woven Tunic":
            s "Roomie, Rahim had it tailor made just for you after that vote we just held, but he's a bit grumpy about delivering handing it to you... So I guess you can just buy it from me for [mmm] gold!"
    if shop_action == "Buy_KeyItem":
        if selected_shopItem.img == "Mossy Artifact":
            s "That's the stone we got from the river! Remember it? [e], I think I'll give it to you... for [selected_shopItem.value] gold, if you buy it now!"
    if shop_action == "Sell_Consumable":
        if selected_shopItem.img == "Small MP Potion":
            s "Has this potion expired yet... I'm not sure. They're all the same, but you have to be really careful about it, especially when you're in danger. How about [selected_shopItem.value] gold."
        if selected_shopItem.img == "Small HP Potion":
            s "Where did you find this potion, is this mine? Hmm... I think you can get [selected_shopItem.value] from this one."
        if selected_shopItem.img == "Beer":
            s "I see what you're doing... selling beer to me. No I won't get drunk on work... b-but how about [selected_shopItem.value] gold?"
    if shop_action == "Sell_KeyItem":
        if selected_shopItem.img == "Storage Room Key":
            s "That's... my key! You can't be selling that... to me?"
        if selected_shopItem.img == "Letter of Peace":
            s "This is a letter for Rahim, right? I think you should let him see this first."
        if selected_shopItem.img == "Wooden Bucket":
            s "[selected_shopItem.value] gold. Here's an advice. You can prevent fall damage when you jump and use the water bucket... Wait... We have no fall damage here."
    if shop_action == "Sell_Equipable":
        if selected_shopItem.img == "Tribe Loincloth":
            s "Wasn't this what you were putting on...? You must got really desperate to sell your loincloth out like that, buddy."
        if selected_shopItem.img == "Short Sword":
            s "Hmm... it was your sword! Must've gotten a new favourite I suppose? [selected_shopItem.value] gold to you!"
        if selected_shopItem.img == "Lion Charm":
            s "That's my Lion Charm... [selected_shopItem.value] gold... You don't want to take me with you again?"
    if shop_action == "Sell_Learnable":
        if selected_shopItem.img == "Botanical Journal":
            s "A book about grasses and what not? My big Ol Ole'd be so elated to get his claws on this one. [selected_shopItem.value] gold that is!"
    if shop_action == "Sell_Material":
        if selected_shopItem.img == "Slime Ball":
            s "I like this one! Some slimy balls, how about [selected_shopItem.value] gold?"
        elif selected_shopItem.img == "Cashmere":
            s "Where did you find... Nevermind. You always get your hand on anyone, even the goats. [selected_shopItem.value] gold?"
        elif selected_shopItem.img == "Minotaur Essence":
            s "Uh... a minotaur? That's not milk! I- I can take that for [selected_shopItem.value] gold, maybe."
        elif selected_shopItem.img == "Slate Rock":
            s "This I haven't seen before, all too ancient for what I'm collecting. Perhaps I can get it for [selected_shopItem.value] gold? How about that."
        elif selected_shopItem.img == "Apple":
            s "Did you get this from the farm? Usually I don't take whatever produces that are meant for their farmer's market. But I can take [selected_shopItem.value]!"

        elif selected_shopItem.img == "Green Dye":
            s "Hey! That's where the green leaves went. I thought I lost it. Big old Ole gave it to you I presume? That'd be [selected_shopItem.value] gold."
        else:
            s "You wanna sell this thing to me? Probably worth [selected_shopItem.value] in the market."
    if shop_action == "Sell_Success":
        s "Okie Dokie! Thank you for your [selected_shopItem.name!t]! Mister [e]. Here's your [selected_shopItem.value]."
        if selected_shopItem.number < 1:
            $ selected_shopItem = None
    if shop_action == "Buy_Success":
        s "Alrighty! Thank you for your [selected_shopItem.value] gold! Mister [e]. Here's your [selected_shopItem.name!t]."
        if selected_shopItem.number < 1:
            $ selected_shopItem = None

    jump Sebas_Shopping_Loop

label Gwyddyon_Shopping:
    $ sebasInventoryPage = 0
    show screen shop_screen("Gwyddyon")
    $ selected_shopItem = None
    $ selected_myItem = None
    scene shopbackground
    hide screen daytime
    if pc.armor["Accessory"] != None and pc.armor["Accessory"].img == "Hagglers Amulet":
        $ value_mult = 0.9
    else:
        $ value_mult = 1
    if (LookForItemNumber("Elderwood", gwyddyonInventory) < 20 and gwyddyon_restock < timenow.day) or not LookForItem("Elderwood", gwyddyonInventory):
        $ addItem("Elderwood", gwyddyonInventory, 20 - LookForItemNumber("Elderwood", gwyddyonInventory), value_mult)
    if (LookForItemNumber("Crystal String", gwyddyonInventory) < 8 and gwyddyon_restock < timenow.day) or not LookForItem("Crystal String", gwyddyonInventory):
        $ addItem("Crystal String", gwyddyonInventory, 8 - LookForItemNumber("Crystal String", gwyddyonInventory), value_mult)
    if (LookForItemNumber("Nylon", gwyddyonInventory) < 25 and gwyddyon_restock < timenow.day) or not LookForItem("Nylon", gwyddyonInventory):
        $ addItem("Nylon", gwyddyonInventory, 25 - LookForItemNumber("Nylon", gwyddyonInventory), value_mult)
    if (LookForItemNumber("Moonstone", gwyddyonInventory) < 9 and gwyddyon_restock < timenow.day) or not LookForItem("Moonstone", gwyddyonInventory):
        $ addItem("Moonstone", gwyddyonInventory, 9 - LookForItemNumber("Moonstone", gwyddyonInventory), value_mult)
    if (LookForItemNumber("Vine", gwyddyonInventory) < 20 and gwyddyon_restock < timenow.day) or not LookForItem("Vine", gwyddyonInventory):
        $ addItem("Vine", gwyddyonInventory, 20 - LookForItemNumber("Vine", gwyddyonInventory), value_mult)
    if gwyddyon_restock < timenow.day:

        $ gwyddyon_restock = int(timenow.day / 10) * 10 + 6

        if LookForItemNumber("Crystal Gem", gwyddyonInventory) < 3:
            $ addItem("Crystal Gem", gwyddyonInventory, 3 - LookForItemNumber("Crystal Gem", gwyddyonInventory), value_mult)
        if LookForItemNumber("Horehound", gwyddyonInventory) < 2:
            $ addItem("Horehound", gwyddyonInventory, 2 - LookForItemNumber("Horehound", gwyddyonInventory), value_mult)
        if not LookForItem("Rebalancing Elixir", gwyddyonInventory) and not LookForItem("Rebalancing Elixir", inventory):
            $ addItem("Rebalancing Elixir", gwyddyonInventory, 1, value_mult)
        if tranquilmend not in learnedabilities and not LookForItem("Book of Tranquil Mend", gwyddyonInventory) and not LookForItem("Book of Tranquil Mend", inventory):
            $ addItem("Book of Tranquil Mend", gwyddyonInventory, 1, value_mult)
        if immolation not in learnedabilities and not LookForItem("Book of Immolation", gwyddyonInventory) and not LookForItem("Book of Immolation", inventory):
            $ addItem("Book of Immolation", gwyddyonInventory, 1, value_mult)
        if quest11.status == True and spectralorb not in learnedabilities and not LookForItem("Book of Spectral Orb", gwyddyonInventory) and not LookForItem("Book of Spectral Orb", inventory):
            $ addItem("Book of Spectral Orb", gwyddyonInventory, 1, value_mult)
        if checkNoShopItem("Crystal Staff"):
            $ addItem("Crystal Staff", gwyddyonInventory, 1, value_mult)
        if eversprout_item not in discoveredtrinket and not LookForItem("Scroll of Eversprout", gwyddyonInventory) and not LookForItem("Scroll of Eversprout", inventory) and quest24.status == True:
            $ addItem("Scroll of Eversprout", gwyddyonInventory, 1, value_mult)
        if checkNoShopItem("Iron Sword"):
            $ addItem("Iron Sword", gwyddyonInventory, 1, value_mult)
    g "See for yourself, these are some of the most wonderful adornments and incantations out here, I've got some odds and ends too."
    jump Gwyddyon_Shopping_Loop

label Gwyddyon_Shopping_Loop:
    $ shop_action = ui.interact()
    hide screen menu_buttons 
    if shop_action == "Return":
        show screen daytime()
        show screen menu_buttons()
        hide screen shop_screen 
        jump main_ardent_cauldron
    $ lll = selected_shopItem.img
    $ mmm = selected_shopItem.value
    $ ttt = selected_shopItem.name
    if shop_action == "Buy_Consumable":
        if lll == "Small MP Potion":
            g "You better believe it, this [ttt!t] is crafted only for the mana-thirsty goats and they're coming for the last ones! Now, it's for [mmm] gold, limited offer of course."
        else:
            g "Believe it or not, you can get this [ttt!t] for only [mmm] gold. One time offer."
    if shop_action == "Buy_KeyItem":
        g "That's not my specialty, but I say this [ttt!t] is worth... [mmm] gold, probably."
    if shop_action == "Buy_Equipable":
        if lll == "Crystal Staff":
            g "What's more impressive than a staff which can restore 5 MP every round? {size=20}Nothing.{/size} And, you don't even need to recharge, who would've thought!{size=20} Totally not me.{/size} {p}[mmm] gold, and this last one is yours."
        else:
            g "Well, how about [mmm] gold for this [ttt!t]? It's of the best quality, obviously."
    if shop_action == "Buy_Material":
        if lll == "Crystal Gem":
            g "Looking to enhance your magical prowess? Feast your eyes on these exquisite crystal gems. One of my greatest achievements of harnessing their energy, now only at [mmm] gold."
        elif lll == "Horehound":
            g "Horehound. they're useful in repelling a particular neighbour of our settlement. No, not Lusterfield. Should get yourself some from up there near the dimwits, or buy some for [mmm] gold."
        elif lll == "Moonstone":
            g "Oh, moonstone. These are quite the rare rocks. You'd think they would have gone depleted by now but some people keep discovering more moonstone veins around, just get some one [mmm] gold."
        elif lll == "Crystal String":
            g "This one? It's just gut strings covered in crystal shards- What? You don't know what guts are...? Ahem... well you don't need to know, nonetheless, these are [mmm] gold."
        elif lll == "Nylon":
            g "Good fabric, very resilient, and believe this or not, the fabric is popular among the nobles and rich people in the high castles, yes it's real. We can sell this for [mmm] gold."
        elif lll == "Elderwood":
            g "At first, people called its tree - Alder, but at some point I guess someone projected their personal experience into the name of a tree. What a tragedy... Hmm, maybe you too would like some for [mmm] gold?"
        elif lll == "Vine":
            g "Years ago, vines were ratherly popular as decorations around one's house, but over time they've outgrown where they are supposed to live, and quickly became a danger to the house and people made a huge fuzz over that. Thoughts and Prayer, and [mmm] gold."
        else:
            g "You want this [ttt!t]? I can do [mmm] gold."
    if shop_action == "Buy_Learnable":
        if lll == "Rebalancing Elixir":
            g "Looking to reset every skill you've learnt? This elixir can do just that. I invented it myself by crushing a few of those gems into one perfectly smooth concoction. It's quite expensive to make, so I can only offer you one for [mmm] gold."
        if lll == "Book of Tranquil Mend":
            g "This book was sold to me just a while ago. Said it was good for your healing power, perhaps it has something in common with my crystals. Anyhow, [mmm] gold and it's yours."
        elif lll == "Book of Spectral Orb":
            g "After the two dimwits came back from the cave, one of them, the general came and dropped his little spell book here."
            g "He said something along the lines of 'Sparing a spell for the courier.'. Heh, he didn't even tell you about it, did he? Well, [mmm] gold and it's yours."
        elif lll == "Book of Immolation":
            g "I don't know where this came from, but it's a good spell book for the fire wizards. I reckon the lion sells a book that could be a great combination for this. Now, would you pay [mmm] gold for the spell?"
        else:
            g "Looking to satisfy your insatiable knowledge? This [ttt!t] is just right for you! Only at [mmm] gold and only sold here!{size=15}I reckon{/size}."
    if shop_action == "Sell_Consumable":
        g "Let's see. I say it's at most [mmm] gold, do you wanna sell this [ttt!t]?"
    if shop_action == "Sell_KeyItem":
        if lll == "Mossy Artifact":
            g "Uhm? Is this from the rune guardians? Condolences. I can buy this hand for [mmm] gold now."
        elif lll == "Magical Stone":
            g "I can sense the immense power remnant from this stone, it's still transmiting a weak aura of magic... that are not inherent in this stone. [mmm] gold, and I'll take a deep look at the stone."
        else:
            g "Doesn't look too bad. Though, you should probably keep this [ttt!t] for yourself, but I can buy it for [mmm] gold."
    if shop_action == "Sell_Equipable":
        g "Could be useful, I think. How about [mmm] gold and I'll keep this [ttt!t] for you."
    if shop_action == "Sell_Material":
        if lll == "Minotaur Essence":
            g "Essence you say? Didn't know someone like you would tame the minotaur, but what do I know. They're quite mystical in essence, perhaps I can get a bottle for [mmm] gold?"
        elif lll == "Copper":
            g "Got yourself acquainted in the caves a lot lately? I can do [mmm] gold. These can be useful for my crystal equipment and gadgets."
        else:
            g "Not a specialist, but I can probably go for... [mmm] gold for this [ttt!t]."

    if shop_action == "Sell_Learnable":
        if lll == "Botanical Journal":
            g "Uhm, you wish to sell this book? Where did you find it- Whatever, doesn't matter. The book's been soaked in slime juice for a while, best I can do is [mmm] gold."
        else:
            g "This [ttt!t] seems promising. I can get you [mmm] gold for that."
    if shop_action == "Buy_Success":
        g "It was a great bargain, [e]. Thanks for the [mmm] gold and here's your [ttt!t]."
        if selected_shopItem.number < 1:
            $ selected_shopItem = None
    if shop_action == "Sell_Success":
        g "Mmmph. That can be useful. Here's the [mmm] gold for your [ttt!t]."
        if selected_shopItem.number < 1:
            $ selected_shopItem = None

    jump Gwyddyon_Shopping_Loop

label Methis_Shopping:
    $ sebasInventoryPage = 0
    if pc.armor["Accessory"] != None and pc.armor["Accessory"].img == "Hagglers Amulet":
        $ value_mult = 0.9
    else:
        $ value_mult = 1

    if methis_restock < timenow.day:
        $ methis_restock = int(timenow.day / 7) * 7 + 2

        $ rnd = 5 - LookForItemNumber("Snow Berry", methisInventory)
        if rnd > 0:
            $ addItem("Snow Berry", methisInventory, rnd, value_mult)

        $ rnd = 6 - LookForItemNumber("Spearmint", methisInventory)
        if rnd > 0:
            $ addItem("Spearmint", methisInventory, rnd, value_mult)

        $ rnd = 8 - LookForItemNumber("Archaic Ice", methisInventory)
        if rnd > 0:
            $ addItem("Archaic Ice", methisInventory, rnd, value_mult)

        if checkNoShopItem("Axe of Ookko"):
            $ addItem("Axe of Ookko", methisInventory, 1, value_mult)

        if checkNoShopItem("Idol of Virtue"):
            $ addItem("Idol of Virtue", methisInventory, 1, value_mult)

        if checkNoShopItem("Small Trowel"):
            $ addItem("Small Trowel", methisInventory, 1, value_mult)

    hide screen daytime
    hide screen menu_buttons
    show screen shop_screen("Methis")
    scene shopbackground
    $ selected_shopItem = None
    $ selected_myItem = None
    m "Take a look, here's our finest collections in the shop."
    jump Methis_Shopping_Loop


label Methis_Shopping_Loop:
    $ shop_action = ui.interact()
    if shop_action == "Return":
        show screen daytime()
        show screen menu_buttons()
        hide screen shop_screen 
        jump main_finnkels_gaze
    $ lll = selected_shopItem.img
    $ mmm = selected_shopItem.value
    $ ttt = selected_shopItem.name
    if shop_action == "Buy_Material":
        if selected_shopItem.img == "Spearmint":
            m "This is a very rare herb outside of the snow. Always a good punishment to teach those bastard bears who weren't feeling cold enough, maybe [mmm] gold?"
        if selected_shopItem.img == "Archaic Ice":
            m "Just a chunk of ice, totally useless, honestly I just used it to fill up my empty shelf space, don't know why you'd want this, but you'll need [mmm] gold to buy one."
    if shop_action == "Buy_Learnable":
        m "Alright, this sounds like an opportunity to learn, for [mmm] gold."
    if shop_action == "Buy_Consumable":
        if selected_shopItem.img == "Snow Berry":
            m "What you called... Health Potion, we use Snow berry here, these are very easily found in snow forest, and the white, gooey, juicy texture reminds me of a lot of stuff. It's [mmm] Gold each."
    if shop_action == "Buy_Equipable":
        if selected_shopItem.img == "Idol of Virtue":
            m "Look, a secret for those who only uses your charm, this idol is made for when you're against uncharmable monsters, time to learn some new tricks, maybe. This is [mmm] Gold."
        if selected_shopItem.img == "Axe of Ookko":
            m "They say Ookko, the god that blessed the snow region, once held a lot of axes, most are not for sales, but this one, well, it's a bit rusty, I can let it go for [mmm] Gold."
        if selected_shopItem.img == "Small Trowel":
            m "Just a small trowel, for [mmm] Gold maybe you can dig up some of the plants around here, if it's not buried in snow already."

    if shop_action == "Buy_KeyItem":

        m "[mmm] Gold, and this last one is yours."
    if shop_action == "Sell_Consumable":
        if selected_shopItem.img == "Small MP Potion":
            m "Is this the work of a famous potion maker in the South? Looks... drinkable. I'll take this for [mmm]."
        if selected_shopItem.img == "Small HP Potion":
            m "Ah, classic mana potion made for magic users. How about [mmm] gold for this one?"
        if selected_shopItem.img == "Beer" or selected_shopItem.img == "Ale":
            m "I don't drink on work... it makes your mind go dizzy, b-but how about [mmm] gold?"
    if shop_action == "Sell_KeyItem":
        m "This one... it looks important. I can't take this from you... can I? [mmm] gold... maybe?"
    if shop_action == "Sell_Equipable":
        m "Ah, smells just like it's worn yesterday. Give it to me and I'll make good use of it. And [mmm] gold for you!"
    if shop_action == "Sell_Learnable":
        m "Looks like a good learning experience, I can take this for [mmm] gold."
    if shop_action == "Sell_Material":
        if lll == "Coal":
            m "A piece of Coal? We mined this every day, don't tell me you stole from the carts outside... But how about... [mmm] gold."
        elif lll == "Chamomile":
            m "Ah, the flower of bears, they love this even though it doesn't grow much in snow. I'll take this for [mmm] gold."
        else:
            m "Hmm... this looks like it can sell for [mmm] gold."
    if shop_action == "Sell_Success":
        m "Thanks for the [ttt!t], and the [mmm] gold is yours now."
        if selected_shopItem.number < 1:
            $ selected_shopItem = None
    if shop_action == "Buy_Success":
        m "Nice, this [ttt!t] is now owned by you, young one. And thanks for the [mmm] gold."
        if selected_shopItem.number < 1:
            $ selected_shopItem = None

    jump Methis_Shopping_Loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
