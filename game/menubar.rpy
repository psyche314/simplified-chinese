screen menu_buttons():
    tag menu_buttons

    zorder 98
    vbox:
        xalign 0.99
        yalign 0.89
        if renpy.get_screen("inventory_screen"):
            imagebutton:
                idle "inventory_hover"
                style "click_button"
                action Hide("inventory_screen"), SetVariable("hovered_item_num", 0), SetVariable("inventoryPage", 0), SetVariable("pinventory", 0), SetVariable("sort_num", 0), SetVariable("cate_num", 0)
        else:
            imagebutton:
                idle "inventory_idle"
                hover "inventory_hover"
                style "click_button"
                action Show("inventory_screen"), SetVariable("hovered_item_num", 0), SetVariable("inventoryPage", 0), SetVariable("pinventory", 0), SetVariable("sort_num", 0), SetVariable("cate_num", 0)

    vbox:
        xalign 0.99
        yalign 0.99
        if renpy.get_screen("map_screen"):
            imagebutton:
                hover "map_idle"
                idle "map_hover"
                style "click_button"
                action Return("Return"), Show("daytime")
        else:
            imagebutton:
                idle "map_idle"
                hover "map_hover"
                style "click_button"
                action Jump("lusteroeren_map"), Hide("daytime"), SetVariable("selected_location", None), SetVariable("selected_mapitem", None)

    vbox:
        xalign 0.99
        yalign 0.79
        if renpy.get_screen("qlog"):
            imagebutton:
                idle "journal_hover"
                style "click_button"
                action Hide("qlog")
        else:
            imagebutton:
                idle "journal_idle"
                hover "journal_hover"
                style "click_button"
                action Show("qlog"), SetVariable("journalPage", "Quest"), SetVariable("quest_progress", ""), Function(CheckQuestProgress), Show("menu_buttons")

screen dungeon_buttons():
    tag menu_buttons

    zorder 100
    vbox:
        xalign 0.99
        yalign 0.99
        if renpy.get_screen("inventory_screen"):
            imagebutton:
                idle "inventory_hover"
                style "click_button"
                action Hide("inventory_screen"), SetVariable("inventoryPage", 0), SetVariable("pinventory", 0)
        else:
            imagebutton:
                idle "inventory_idle"
                hover "inventory_hover"
                style "click_button"
                action Show("inventory_screen"), SetVariable("inventoryPage", 0), SetVariable("pinventory", 0)

    vbox:
        xalign 0.99
        yalign 0.89
        if renpy.get_screen("qlog"):
            imagebutton:
                idle "journal_hover"
                style "click_button"
                action Hide("qlog")
        else:
            imagebutton:
                idle "journal_idle"
                hover "journal_hover"
                style "click_button"
                action Show("qlog"), SetVariable("journalPage", "Quest")



screen daytime():
    zorder 90

    text _("Day [timenow.day], [timenow.dayofweek], [timenow.hours]:[timenow.minutes]") style_prefix "screen_content"

    python:
        now = (timenow.day, timenow.hour, timenow.minute)

        for st in pc.active_status:
            if st.get("Modifiers") and not st.get("Effect Applied", False):
                for attr, delta in st["Modifiers"].items():
                    setattr(pc, attr, getattr(pc, attr) + delta)
                st["Effect Applied"] = True

        for st in pc.active_status[:]:
            exp = (st["Expire Day"], st["Expire Hour"], st["Expire Minute"])
            if now >= exp:
                if st.get("Modifiers"):
                    for attr, delta in st["Modifiers"].items():
                        setattr(pc, attr, getattr(pc, attr) - delta)
                status_name = st["Status"].lower()
                renpy.notify(_("You are no longer ") + status_name + ".")
                pc.active_status.remove(st)
            
            if st["Status"] == "Drunk":
                if pc.lust < 10:
                    pc.lust = 10
            if st["Status"] == "Buzzing":
                if pc.lust < 20:
                    pc.lust = 20



        if current_location == snowbound_summit or current_location == skullstrewn_pass:
            
            if not has_active_status("Freezing") and not pc.checkEquipped("Winterworn Coat"):
                eh = (timenow.hour + 1) % 24
                ed = timenow.day + (1 if timenow.hour == 23 else 0)
                pc.active_status.append({
                    "Status": "Freezing",
                    "Name": _("Freezing"),
                    "Description": _("Your body is freezing from the coldness of the snow region, dealing 10 HP damage every hour you spent here."),
                    "Expire Day": ed,
                    "Expire Hour": eh,
                    "Expire Minute": timenow.minute,
                })
                renpy.notify(_("Your body is now freezing from the coldness of the snow region."))
            else:
                for st in pc.active_status:
                    if st["Status"] == "Freezing":
                        if pc.checkEquipped("Winterworn Coat"):
                            pc.active_status.remove(st)
                        else:
                            st["Expire Day"] = timenow.day + (1 if timenow.hour == 23 else 0)
                            st["Expire Hour"] = (timenow.hour + 1) % 24
            
            if store.hourly_check % 24 < timenow.hour and has_active_status("Freezing"):
                store.hourly_check = timenow.hour
                damage = 10  
                pc.restore(hp = -damage)
                renpy.notify(_("You lost ") + str(damage) +_(" HP to the freezing cold in the snow region."))

        for delivery in active_deliveries[:]:
            if timenow.day > delivery["start day"] + delivery["expire days"]:
                pc.rep -= 10
                if pc.rep < 0:
                    pc.rep = 0
                fail_job(delivery, timenow.day)

screen baddaytime():
    add "clocky":
        pos (110, -30)
        rotate (-((int(timenow.hours)*60.0+int(timenow.minutes)) / 4.0)-158.5)
    add "clockarrow":
        pos (0, -5)
    if int(timenow.hours) < 12:

        add "clock":
            pos (0, 0)
    else:
        add "clock2":
            pos (0, 0)

    $ gold_num = [int(x) for x in str(pc.gold)]
    $ hour_num = [int(x) for x in str(int(timenow.hours) % 12)]
    $ minute_num = [int(x) for x in str(timenow.minutes)]
    if len(gold_num) < 7:
        for x in range(7-len(gold_num)):
            $ gold_num = [0] + gold_num
    if len(hour_num) < 2:
        $ hour_num = [0] + hour_num
    if hour_num == [0, 0]:
        $ hour_num = [1, 2]
    if pc.gold >= 10000000:
        $ gold_num =[9,9,9,9,9,9,9]
    hbox:
        xalign 0.03
        yalign 0.01
        spacing 9
        for x in gold_num:
            text "[x]" color ("#382717") size 29 font "kingthing.ttf"

    hbox:
        xalign 0.03
        yalign 0.055
        spacing 13
        for x in hour_num:
            text "[x]" color ("#382717") size 32 font "kingthing.ttf"

    hbox:
        xalign 0.06
        yalign 0.055
        spacing 11
        for x in minute_num:
            text "[x]" color ("#382717") size 32 font "kingthing.ttf"

    text __("Day: [timenow.day]") xalign 0.028 yalign 0.103 color ("#382717") size 25 font "kingthing.ttf"

    text timenow.dayofweek xalign 0.073 yalign 0.103 color ("#382717") size 29 font "kingthing.ttf"

init python:

    def show_quest_log():
        renpy.show_screen("qlog")


label Testing_Ground:

    show screen qlog()

    show screen menu_buttons()



    ""

    ""

    jump Testing_Ground
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
