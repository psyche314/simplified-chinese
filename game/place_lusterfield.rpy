screen place_bedroom():
    zorder 10 tag place






    imagebutton:
        xalign 0.65
        yalign 0.95
        idle "bedroom_arrow"
        hover "bedroom_arrow_hover"
        style "footstep_button"
        action Return("To Kingspawn")

screen place_kingspawn():
    zorder 10 tag place

    if isNight():
        imagebutton:
            xalign 0.8067
            yalign 0.0836
            idle "kings_pawn_door_night_idle"
            hover "kings_pawn_door_night_hover"
            style "door_button"
            action Return("To Bedroom")
        if checkNoShopItem("Battle of Lusterfield"):
            imagebutton:
                xalign 0.094
                yalign 0.088
                idle "kings_pawn_book_night"
                hover "kings_pawn_book_night_hover"
                style "door_button"
                action Return("Book")

        imagebutton:
            xalign 0.3805
            yalign 0.2507
            idle "kings_pawn_statue_night"
            hover "kings_pawn_statue_night_hover"
            style "door_button"
            action Return("Statue")

        imagebutton:
            xalign 0.314
            yalign 0.123
            idle "kings_pawn_plush_night"
            hover "kings_pawn_plush_night_hover"
            style "door_button"
            action Return("Plush")

        imagebutton:
            xalign 0.671
            yalign 0.394
            idle "kings_pawn_account_night"
            hover "kings_pawn_account_night_hover"
            style "door_button"
            action Return("Account")

        imagebutton:
            xalign 0.8796
            yalign 0.0683
            idle "kings_pawn_drawing_night"
            hover "kings_pawn_drawing_night_hover"
            style "door_button"
            action Return("Drawing")
    else:
        imagebutton:
            xalign 0.8067
            yalign 0.0836
            idle "kings_pawn_door_day_idle"
            hover "kings_pawn_door_day_hover"
            style "door_button"
            action Return("To Bedroom")
        if checkNoShopItem("Battle of Lusterfield"):
            imagebutton:
                xalign 0.094
                yalign 0.088
                idle "kings_pawn_book_day"
                hover "kings_pawn_book_day_hover"
                style "door_button"
                action Return("Book")

        imagebutton:
            xalign 0.3805
            yalign 0.2507
            idle "kings_pawn_statue_day"
            hover "kings_pawn_statue_day_hover"
            style "door_button"
            action Return("Statue")

        imagebutton:
            xalign 0.314
            yalign 0.123
            idle "kings_pawn_plush_day"
            hover "kings_pawn_plush_day_hover"
            style "door_button"
            action Return("Plush")

        imagebutton:
            xalign 0.671
            yalign 0.394
            idle "kings_pawn_account_day"
            hover "kings_pawn_account_day_hover"
            style "door_button"
            action Return("Account")

        imagebutton:
            xalign 0.8796
            yalign 0.068
            idle "kings_pawn_drawing_day"
            hover "kings_pawn_drawing_day_hover"
            style "door_button"
            action Return("Drawing")

    if sebas_location == "kingspawn":
        imagebutton:
            xalign 0.53
            yalign 0.24
            idle "sebasidle"
            hover "sebashover"
            action Return("Sebas")

    if ole_location == "kingspawn":
        imagebutton:
            xalign 0.135
            yalign 0.152
            idle "oleidle"
            hover "olehover"
            action Return("Ole")

    imagebutton:
        xalign 0.59
        yalign 0.93
        idle "kingspawn_arrow"
        hover "kingspawn_arrow_hover"
        style "footstep_button"
        action Return("To Lusterfield")

screen place_lusterfield01():
    zorder 10 tag place


    imagebutton:
        xalign 0.25
        yalign 0.74
        idle "ancienttree_arrow"
        hover "ancienttree_arrow_hover"
        style "footstep_button"
        action Return("To Alleyway")

    if not isNight():
        imagebutton:
            focus_mask "lusterfield_kingspawn_door_open"
            idle "lusterfield_kingspawn_door_closed"
            hover "lusterfield_kingspawn_door_open"
            action Return("To Kingspawn")
    else:
        imagebutton:
            focus_mask "lusterfield_kingspawn_door_open"
            idle "lusterfield_kingspawn_door_closed_night"
            hover "lusterfield_kingspawn_door_open_night"
            action Return("To Kingspawn")

    if lothar_location == "lusterfield01":
        imagebutton:
            xalign 0.03
            yalign 0.99
            idle "lotharidle"
            hover "lotharhover"
            action Return("Lothar")

    imagebutton:
        xalign 0.49
        yalign 0.62
        idle "sparklinglagoon_arrow"
        hover "sparklinglagoon_arrow_hover"
        style "footstep_button"
        action Return("To Lusterfield2")

    imagebutton:
        xalign 0.42
        yalign 0.95
        idle "kingspawn_arrow"
        hover "kingspawn_arrow_hover"
        style "footstep_button"
        action Return("To Green Forest")

screen place_lusterfield02():
    tag place
    zorder 10


    imagebutton:
        xalign 0.2
        yalign 0.95

        idle "kingspawn_arrow"
        hover "kingspawn_arrow_hover"
        style "footstep_button"
        action Return("To Lusterfield")

    if isNight():

        imagebutton:
            xalign 0.205
            yalign 0.33

            idle "lusterfield02_rahimdoor_idle_night"
            hover "lusterfield02_rahimdoor_hover_night"
            style "door_button"
            action Return("To Rahim")

    else:

        imagebutton:
            xalign 0.205
            yalign 0.33

            idle "lusterfield02_rahimdoor_idle"
            hover "lusterfield02_rahimdoor_hover"
            style "door_button"
            action Return("To Rahim")

    imagebutton:
        xalign 1.005
        yalign 0.215

        idle "lusterfield02_canedoor_idle_night"
        hover "lusterfield02_canedoor_hover_night"
        style "door_button"
        action Return("To Nocturnal Trunk")

    imagebutton:
        focus_mask "haimo_idle"
        idle "haimo_idle"
        hover dayHover("haimo_idle")
        activate_sound clickd
        hover_sound clickhover
        action Return("Haimo")

    imagebutton:
        focus_mask "courier_board"
        idle "courier_board"
        hover dayHover("courier_board")
        activate_sound clickd
        hover_sound clickhover
        action Return("Board")


    if quest01.status == True:

        imagebutton:
            xalign 0.9
            yalign 0.85

            idle "lusterfield_arrow2"
            hover "lusterfield_arrow2_hover"
            style "footstep_button"
            action Return("To Range")

screen place_lusterfield_range():
    tag place
    zorder 10


    imagebutton:
        xalign 0.07
        yalign 0.55

        idle "lusterfield_arrow1"
        hover "lusterfield_arrow1_hover"
        style "footstep_button"
        action Return("To Lusterfield02")

    if summery_farmland.discovered == True:

        imagebutton:
            xalign 0.87
            yalign 0.85

            idle "lusterfield_arrow2"
            hover "lusterfield_arrow2_hover"
            style "footstep_button"
            action Return("To Farmland")
    if isNight():
        imagebutton:
            focus_mask "lusterfield_range_poster01"
            idle AlphaMask("lusterfield_range_night", "lusterfield_range_poster01")
            hover AlphaMask(dayHover("lusterfield_range_night"), "lusterfield_range_poster01")
            activate_sound clickd
            hover_sound clickhover
            action Return("Poster1")

        imagebutton:
            focus_mask "lusterfield_range_poster02"
            idle AlphaMask("lusterfield_range_night", "lusterfield_range_poster02")
            hover AlphaMask(dayHover("lusterfield_range_night"), "lusterfield_range_poster02")
            activate_sound clickd
            hover_sound clickhover
            action Return("Poster2")
    else:
        imagebutton:
            focus_mask "lusterfield_range_poster01"
            idle AlphaMask("lusterfield_range", "lusterfield_range_poster01")
            hover AlphaMask(dayHover("lusterfield_range"), "lusterfield_range_poster01")
            activate_sound clickd
            hover_sound clickhover
            action Return("Poster1")

        imagebutton:
            focus_mask "lusterfield_range_poster02"
            idle AlphaMask("lusterfield_range", "lusterfield_range_poster02")
            hover AlphaMask(dayHover("lusterfield_range"), "lusterfield_range_poster02")
            activate_sound clickd
            hover_sound clickhover
            action Return("Poster2")

    if not range_chest_opened:
        if not isNight():

            imagebutton:
                focus_mask "lusterfield_range_chest"
                idle AlphaMask("lusterfield_range", "lusterfield_range_chest")
                hover AlphaMask(dayHover("lusterfield_range"), "lusterfield_range_chest")
                activate_sound clickd
                hover_sound clickhover
                action Return("Open Chest")
        else:
            imagebutton:
                focus_mask "lusterfield_range_chest"
                idle AlphaMask("lusterfield_range_night", "lusterfield_range_chest")
                hover AlphaMask(nightHover("lusterfield_range_night"), "lusterfield_range_chest")
                activate_sound clickd
                hover_sound clickhover
                action Return("Open Chest")
    else:
        if not isNight():

            add "lusterfield_range_chest_opened"
        else:
            add "lusterfield_range_chest_opened_night"


    if (quest42.status == True or vote_result < 0) and quest43.status != False and quest43.status != True:

        if not isNight():

            imagebutton:
                focus_mask "lusterfield_range_door_open"
                idle AlphaMask("lusterfield_range", "lusterfield_range_door")
                hover "lusterfield_range_door_open"
                activate_sound clickd
                hover_sound clickhover
                action Return("To Longhouse")
        else:
            imagebutton:
                focus_mask "lusterfield_range_door_open"
                idle AlphaMask("lusterfield_range_night", "lusterfield_range_door")
                hover "lusterfield_range_door_open_night"
                activate_sound clickd
                hover_sound clickhover
                action Return("To Longhouse")

    else:
        if not isNight():
            add "lusterfield_range_door_barred"
        else:
            add "lusterfield_range_door_barred_night"

    if amble_location == "lusterfieldrange":

        imagebutton:
            xalign 0.25
            yalign 0.98

            idle "amble_idle"
            hover "amble_hover"
            action Return("Amble")

    if jog_location == "lusterfieldrange":

        imagebutton:
            xalign 0.95
            yalign 0.62

            idle "jog_idle"
            hover "jog_hover"
            action Return("Jog")

screen place_lusterfield_mayors_longhouse():
    tag place
    zorder -1


    for i, j in mayors_longhouse_moss.items():
        if j == 0:
            imagebutton:
                focus_mask i
                idle AlphaMask("mayors_longhouse_mossy", i)
                hover AlphaMask(dayHover("mayors_longhouse_mossy"), i)
                activate_sound clicksweep
                hover_sound clickhover
                action Return("Moss"+i[-1])

    for i, j in mayors_longhouse_marking.items():
        if j == 0:
            imagebutton:
                focus_mask i
                idle AlphaMask("mayors_longhouse", i)
                hover AlphaMask(nightHover("mayors_longhouse"), i)
                action Return("Marking"+i[-1])

    for i, j in mayors_longhouse_interaction.items():
        if all(x == 1 for x in mayors_longhouse_moss.values()):
            imagebutton:
                focus_mask i
                idle AlphaMask("mayors_longhouse_clean", i)
                hover AlphaMask(nightHover("mayors_longhouse_clean"), i)
                action Return(i[17:].capitalize())
        else:
            imagebutton:
                focus_mask i
                idle AlphaMask("mayors_longhouse", i)
                hover AlphaMask(nightHover("mayors_longhouse"), i)
                action Return(i[17:].capitalize())

    imagebutton:
        xalign 0.27
        yalign 0.95

        idle "bedroom_arrow"
        hover "bedroom_arrow_hover"
        action Return("To Range")


screen place_lusterfield_alleyway():
    tag place
    zorder 10


    imagebutton:
        xalign 0.47
        yalign 0.95

        idle "bedroom_arrow"
        hover "bedroom_arrow_hover"
        style "footstep_button"
        action Return("To Lusterfield")

    imagebutton:
        xalign 0.28
        yalign 0.41

        idle "empty2"
        hover "dummy_hover"
        action Return("Dummy Battle")

screen place_nocturnaltrunk():
    tag place
    zorder 10


    imagebutton:
        xalign 0.6
        yalign 0.95

        idle "bedroom_arrow"
        hover "bedroom_arrow_hover"
        style "footstep_button"
        action Return("To Lusterfield2")

    if quest07.status == True and task02.completedtimes > 1:

        imagebutton:
            xalign 0.16
            yalign 0.18

            idle "lusterfield_arrow1"
            hover "lusterfield_arrow1_hover"
            style "footstep_button"
            action Return("To Upstairs")

    if cane_location == "nocturnaltrunk":
        imagebutton:
            xalign 1.015
            yalign 0.555
            idle "caneidle"
            hover "canehover"
            action Return("Cane")

    if ole_location == "nocturnaltrunk":
        imagebutton:
            xalign 0.215
            yalign 0.34


            idle "ole_nt_idle"
            hover "ole_nt_hover"
            action Return("Ole")

    if sebas_location == "nocturnaltrunk":
        imagebutton:
            xalign 0.32
            yalign 0.37


            idle "sebas_nt_idle"
            hover "sebas_nt_hover"
            action Return("Sebas")

    elif trunk_patron["Back"]["Current Seat"] == "Merchant":
        imagebutton:
            xalign 0.268
            yalign 0.355
            idle "trunk_patron_back1"
            hover dayHover("trunk_patron_back1")
            action Return("Merchant")

    elif trunk_patron["Back"]["Current Seat"] == "Drunk":
        imagebutton:
            xalign 0.303
            yalign 0.445
            idle "trunk_patron_back2"
            hover dayHover("trunk_patron_back2")
            action Return("Drunk")

    if trunk_patron["Left"]["Current Seat"] == "Pair":
        imagebutton:
            xalign 0.0
            yalign 0.575
            idle "trunk_patron_left1"
            hover dayHover("trunk_patron_left1")
            action Return("Pair")

    if trunk_patron["Left"]["Current Seat"] == "Mage":
        imagebutton:
            xalign 0.142
            yalign 0.492
            idle "trunk_patron_left2"
            hover dayHover("trunk_patron_left2")
            action Return("Mage")

    if trunk_patron["Right"]["Current Seat"] == "Fighters":
        imagebutton:
            xalign 0.436
            yalign 0.321
            idle "trunk_patron_right2"
            hover dayHover("trunk_patron_right2")
            action Return("Fighters")

        imagebutton:
            xalign 0.534
            yalign 0.501
            idle "trunk_patron_right1"
            hover dayHover("trunk_patron_right1")
            action Return("Fighters")

    if trunk_patron["Right"]["Current Seat"] == "Sneaks":
        imagebutton:
            xalign 0.562
            yalign 0.554
            idle "trunk_patron_right3"
            hover dayHover("trunk_patron_right3")
            action Return("Sneaks")

    if trunk_patron["Front"]["Current Seat"] == "Eater":
        imagebutton:
            xalign 0.345
            yalign 0.635
            idle "trunk_patron_front1"
            hover dayHover("trunk_patron_front1")
            action Return("Eater")

    if trunk_patron["Front"]["Current Seat"] == "Guild":
        imagebutton:
            xalign 0.275
            yalign 0.755
            idle "trunk_patron_front2"
            hover dayHover("trunk_patron_front2")
            action Return("Guild")

    if trunk_patron["Front"]["Current Seat"] == "Rat":
        imagebutton:
            focus_mask "trunk_patron_front3"
            idle "trunk_patron_front3"
            hover dayHover("trunk_patron_front3")
            activate_sound clicksweep
            hover_sound clickhover
            action Return("Rat")

    if lothar_location == "nocturnaltrunk":
        imagebutton:
            xalign 0.68
            yalign 0.65
            idle "lothar_ntidle"
            hover "lothar_nthover"
            action Return("Lothar")

screen place_nocturnaltrunk_upper():
    tag place
    zorder 10


    imagebutton:
        xalign 0.75
        yalign 0.25

        idle "lusterfield_arrow2"
        hover "lusterfield_arrow2_hover"
        style "footstep_button"
        action Return("To Downstairs")

    if pirkka_location == "nocturnalupper":
        imagebutton:
            xalign 0.37
            yalign 0.425

            idle "pirkka_idle"
            hover "pirkka_hover"
            action Return("Pirkka")

    imagebutton:
        xalign 0.12
        yalign 0.65

        idle "patron4_idle"
        hover "patron4_hover"
        action Return("Patron4")

    imagebutton:
        xalign 1.005
        yalign 1.0

        idle "cardpatron_idle"
        hover "cardpatron_hover"
        action Return("Cardy")

screen place_rahimshop():
    tag place
    zorder 10


    if isNight():
        imagebutton:
            xalign 0.678
            yalign 0.546

            idle "rahims_house_crafting_night"
            hover "rahims_house_crafting_night_hover"
            action Return("Craft")

        imagebutton:
            xalign 0.3875
            yalign 0.315

            idle "rahims_house_drawing_night"
            hover "rahims_house_drawing_night_hover"
            action Return("Drawing")

        imagebutton:
            xalign 0.922
            yalign 0.711

            idle "rahims_house_tanning_night"
            hover "rahims_house_tanning_night_hover"
            action Return("Tanning")

        imagebutton:
            xalign 0.206
            yalign 1.001

            idle "rahims_house_basket_night"
            hover "rahims_house_basket_night_hover"
            action Return("Basket")
    else:

        imagebutton:
            xalign 0.678
            yalign 0.546

            idle "rahims_house_crafting_day"
            hover "rahims_house_crafting_day_hover"
            action Return("Craft")

        imagebutton:
            xalign 0.3875
            yalign 0.315

            idle "rahims_house_drawing_day"
            hover "rahims_house_drawing_day_hover"
            action Return("Drawing")

        imagebutton:
            xalign 0.922
            yalign 0.711

            idle "rahims_house_tanning_day"
            hover "rahims_house_tanning_day_hover"
            action Return("Tanning")

        imagebutton:
            xalign 0.206
            yalign 1.001

            idle "rahims_house_basket_day"
            hover "rahims_house_basket_day_hover"
            action Return("Basket")

    imagebutton:
        xalign 0.57
        yalign 0.97

        idle "bedroom_arrow"
        hover "bedroom_arrow_hover"
        style "footstep_button"
        action Return("To Lusterfield2")

    if rahim_location == "rahimshop":
        imagebutton:
            xalign 0.57
            yalign 0.68

            idle "rahimidle"
            hover "rahimhover"
            action Return("Rahim")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
