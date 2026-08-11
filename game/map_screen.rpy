label lusteroeren_map:
    $ wilderness = True
    $ timenow.minute += 20
    $ timenow.passTime()
    hide screen menu_buttons
    if eversprout_route != 8:
        $ eversprout_route = 0
    if current_map == lusterfield_map:
        if kechioeren.discovered:
            scene map01 with dissolve
        else:
            scene map01wok with dissolve
    elif current_map == darkforest_map:
        $ renpy.music.play(mDforest, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
        scene darkforest_map with dissolve
    elif current_map == grassland_map:
        scene grassland_map with dissolve
    elif current_map == otsovaara_map:
        scene otsovaara_map with dissolve
    window hide
    call screen map_screen()

    if quest27.status == 3 and LookForItem("Flagitious Ooze", inventory) and LookForItem("Teratoid Mucus", inventory) and LookForItem("Slime Grancrystal", inventory):
        jump Wuldon_Enter_Cure_Transition

    if _return == "Lusterfield":

        jump main_lusterfield01

    if _return == "Green Forest":

        jump main_green_forest

    if _return == "Ancient Tree":

        jump main_ancient_tree

    if _return == "Sparkling Lagoon":

        jump main_sparkling_lagoon

    if _return == "Mossy Freshwater":

        jump main_mossy_freshwater

    if _return == "Woodland Outpost":

        jump main_woodland_outpost

    if _return == "Alchemist Cabin":

        jump main_alchemists_cabin

    if _return == "Dark Forest":

        jump main_dark_forest

    if _return == "Riverside Crossing":

        jump main_riverside_crossing

    if _return == "Dark Forest Map":

        $ current_map = darkforest_map
        jump lusteroeren_map

    if _return == "Lusterfield Map":

        $ current_map = lusterfield_map
        jump lusteroeren_map

    if _return == "Grassland Map":

        $ current_map = grassland_map
        jump lusteroeren_map

    if _return == "Otsovaara Map":

        $ current_map = otsovaara_map
        jump lusteroeren_map

    if _return == "Damp Cave":

        jump main_damp_cave

    if _return == "Gloomy Mountainside":

        jump main_gloomy_mountainside

    if _return == "Kechioeren":
        hide screen map_screen 
        jump main_kechioeren01

    if _return == "Sundersilk Cascades":
        hide screen map_screen 
        jump main_sundersilk_cascades

    if _return == "Grove of Harvest":
        hide screen map_screen 
        jump main_grove_of_harvest

    if _return == "Summery Farmland":
        hide screen map_screen 
        jump main_summery_farmland

    if _return == "Ursinia Glade":
        jump main_ursinia_glade

    if _return == "Bandits Hideout":
        jump main_bandits_hideout

    if _return == "Prattlefell Meadow":
        jump main_prattlefell_meadow

    if _return == "Frosted Taiga":
        jump main_frosted_taiga
    if _return == "Otsovaara":
        jump main_otsovaara
    if _return == "Skullstrewn Pass":
        jump main_skullstrewn_pass
    if _return == "Clawridge Ascent":
        jump main_clawridge_ascent
    if _return == "Avalanche Site":
        jump main_avalanche_site
    if _return == "Snowbound Summit":
        jump Snowbound_Summit_Enter
    if _return == "Snowbound Summit Top":
        $ snowbound_summit_path = 5
        jump Snowbound_Summit
    if _return == "To Cave Entrance":
        jump Cavern_Entrance_Enter
    if _return == "To Entrance":
        jump main_dark_forest
    if _return == "To Cavern":
        scene black with dissolve
        "You enter the Chelforte Cavern..."
        jump Chelforte_Cavern_Enter
    if _return == "To Well":
        scene black with dissolve
        "You enter the Slumbrous Well..."
        jump main_slumbrous_well
    if _return == "To DF1":
        scene black with dissolve
        "You enter the forest nightwatch..."
        jump Forest_Nightwatch_Enter
    if _return == "To Wolf Den":
        "You enter the werewolves' den..."
        jump main_moonlit_wolf_den
    if _return == "To Slime":
        jump Slimy_Fight_Recoup
    if _return == "To Hollow":
        jump Whispering_Hollow_Enter
    if _return == "To Thicket":
        jump Creek_Thicket_Enter
    if _return == "To Stream":
        if quest27.status == 3:
            "As you walk through the gap at the other end of the dungeon floor, you see Wuldon burst in through the treeline after you, making sure to keep you in his sights."
            "You half expect him to join you in the next room, but he stops at the gap once again, poised to clear out any and all slimes trying to come after you."
        jump Viscid_Stream_Enter
    if _return == "To Sanctuary":
        jump Forgotten_Sanctuary_Enter
    if _return == "To Split Trail":
        scene black with dissolve
        "You enter the split trails..."
        jump Split_Trail_Enter

    if _return == "Return":
        hide screen map_screen 
        if current_location != None:
            if isinstance(current_location, str) or isinstance(current_location, unicode):
                $ curlotion = current_location.lower().replace(" ","_").replace("'","")
                $ renpy.jump("main_"+curlotion)
            elif isinstance(current_location, Place):
                $ curlotion = current_location.name.lower().replace(" ","_").replace("'","")
                $ renpy.jump("main_"+curlotion)
            else:
                if isinstance(current_location, MapPat) and current_location.img == "Forest Nightwatch":
                    jump Dark_Forest1_Loop
                $ curlotion = current_location.img.replace(" ","_").replace("'","")
                $ renpy.jump(curlotion+"_Enter")

    jump lusteroeren_map

screen map_screen():
    tag menu_bar
    zorder 98

    imagebutton:
        xalign 0.99
        yalign 0.99
        idle "map_hover"
        hover "map_idle"
        style "click_button"
        action Return("Return"), Show("daytime")

    if current_map == lusterfield_map:
        imagebutton:
            xalign 0.69
            yalign 0.35
            idle "mapsite2"
            hover "mapsite2hover"
            style "walk_button"
            hovered SetVariable("selected_location", lusterfield)
            action Return("Lusterfield")

        imagebutton:
            xalign 0.62
            yalign 0.49
            idle "mapsite2"
            hover "mapsite2hover"
            style "walk_button"
            hovered SetVariable("selected_location", green_forest)
            action Return("Green Forest")

        if ancient_tree.discovered == True:

            imagebutton:
                xalign 0.48
                yalign 0.45
                idle "mapsite2"
                hover "mapsite2hover"
                style "walk_button"
                hovered SetVariable("selected_location", ancient_tree)
                action Return("Ancient Tree")

        if sparkling_lagoon.discovered == True:

            imagebutton:
                xalign 0.56
                yalign 0.69
                idle "mapsite2"
                hover "mapsite2hover"
                style "walk_button"
                hovered SetVariable("selected_location", sparkling_lagoon)
                action Return("Sparkling Lagoon")

        if riverside_crossing.discovered == True:

            imagebutton:
                xalign 0.37
                yalign 0.79
                idle "mapsite2"
                hover "mapsite2hover"
                style "walk_button"
                hovered SetVariable("selected_location", riverside_crossing)
                action Return("Riverside Crossing")

        if mossy_freshwater.discovered == True:

            imagebutton:
                xalign 0.41
                yalign 0.40
                idle "mapsite2"
                hover "mapsite2hover"
                style "walk_button"
                hovered SetVariable("selected_location", mossy_freshwater)
                action Return("Mossy Freshwater")

        if woodland_outpost.discovered == True:

            imagebutton:
                xalign 0.30
                yalign 0.58
                idle "mapsite2"
                hover "mapsite2hover"
                style "walk_button"
                hovered SetVariable("selected_location", woodland_outpost)
                action Return("Woodland Outpost")

        if damp_cave.discovered == True:

            imagebutton:
                xalign 0.53
                yalign 0.78
                idle "mapsite2d"
                hover "mapsite2dhover"
                style "walk_button"
                hovered SetVariable("selected_location", damp_cave)
                action Return("Damp Cave")

        if gloomy_mountainside.discovered == True:

            imagebutton:
                xalign 0.07
                yalign 0.12
                idle "mapsite2d"
                hover "mapsite2dhover"
                style "walk_button"
                hovered SetVariable("selected_location", gloomy_mountainside)
                action Return("Gloomy Mountainside")

        if dark_forest.discovered == True:

            imagebutton:
                xalign 0.15
                yalign 0.11
                idle "mapsite2"
                hover "mapsite2hover"
                style "walk_button"
                hovered SetVariable("selected_location", dark_forest)
                action Return("Dark Forest")

            imagebutton:
                xalign 0.24
                yalign 0.01
                idle "map_transition_arrow1_idle"
                hover "map_transition_arrow1_hover"
                style "walk_button"
                hovered SetVariable("selected_location", dark_forest)
                action Return("Dark Forest Map")

        if alchemists_cabin.discovered == True:

            imagebutton:
                xalign 0.32
                yalign 0.27
                idle "mapsite2"
                hover "mapsite2hover"
                style "walk_button"
                hovered SetVariable("selected_location", alchemists_cabin)
                action Return("Alchemist Cabin")

        if sundersilk_cascades.discovered == True:

            imagebutton:
                xalign 0.53
                yalign 0.11
                idle "mapsite2"
                hover "mapsite2hover"
                style "walk_button"
                hovered SetVariable("selected_location", sundersilk_cascades)
                action Return("Sundersilk Cascades")

        if summery_farmland.discovered == True:

            imagebutton:
                xalign 0.78
                yalign 0.11
                idle "mapsite2"
                hover "mapsite2hover"
                style "walk_button"
                hovered SetVariable("selected_location", summery_farmland)
                action Return("Summery Farmland")

            imagebutton:
                xalign 0.80
                yalign 0.18
                idle "map_transition_arrow2_idle"
                hover "map_transition_arrow2_hover"
                style "walk_button"
                hovered SetVariable("selected_location", grove_of_harvest)
                action Return("Grassland Map")

        if kechioeren.discovered == True and quest11.status == True:

            imagebutton:
                xalign 0.12
                yalign 0.67
                idle "mapsite2"
                hover "mapsite2hover"
                style "walk_button"
                hovered SetVariable("selected_location", kechioeren)
                action Return("Kechioeren")

    if current_map == darkforest_map:
        imagebutton:
            xalign 0.45
            yalign 0.97
            idle "map_transition_arrow3_idle"
            hover "map_transition_arrow3_hover"
            style "footstep_button"
            action Return("Lusterfield Map")
        imagebutton:
            xalign 0.99
            yalign 0.99
            idle "map_hover"
            hover "map_idle"
            style "footstep_button"
            action Return("To Entrance")
        imagebutton:
            xalign 0.39
            yalign 0.83
            idle "mapentrance"
            hover "mapentrancehover"
            style "footstep_button"
            hovered SetVariable("selected_location", dark_forest)
            action Return("To Entrance")
        imagebutton:
            xalign 0.43
            yalign 0.59
            idle "mapsite"
            hover "mapsitehover"
            style "footstep_button"
            hovered SetVariable("selected_location", forest_nightwatch)
            action Return("To DF1")
        if moonlit_wolf_den.discovered == True:
            imagebutton:
                xalign 0.53
                yalign 0.31
                idle "mapsite"
                hover "mapsitehover"
                style "footstep_button"
                hovered SetVariable("selected_location", moonlit_wolf_den)
                action Return("To Wolf Den")
        if split_trails.discovered == True:
            imagebutton:
                xalign 0.49
                yalign 0.41
                idle "mapsite"
                hover "mapsitehover"
                style "footstep_button"
                hovered SetVariable("selected_location", split_trails)
                action Return("To Split Trail")
        if whispering_hollows.discovered == True:
            imagebutton:
                xalign 0.31
                yalign 0.36
                idle "mapsite"
                hover "mapsitehover"
                style "footstep_button"
                hovered SetVariable("selected_location", whispering_hollows)
                action Return("To Hollow")
        if slumbrous_well.discovered == True:
            imagebutton:
                xalign 0.37
                yalign 0.49
                idle "mapsite"
                hover "mapsitehover"
                style "footstep_button"
                hovered SetVariable("selected_location", slumbrous_well)
                action Return("To Well")
        if cavern_entrance.discovered == True:
            imagebutton:
                xalign 0.65
                yalign 0.55
                idle "mapsite"
                hover "mapsitehover"
                style "footstep_button"
                hovered SetVariable("selected_location", cavern_entrance)
                action Return("To Cave Entrance")
        if chelforte_cavern.discovered == True:
            imagebutton:
                xalign 0.71
                yalign 0.59
                idle "mapsite"
                hover "mapsitehover"
                style "footstep_button"
                hovered SetVariable("selected_location", chelforte_cavern)
                action Return("To Cavern")
        if viscid_streams.discovered == True:
            imagebutton:
                xalign 0.27
                yalign 0.64
                idle "mapsite"
                hover "mapsitehover"
                style "footstep_button"
                hovered SetVariable("selected_location", viscid_streams)
                action Return("To Stream")

        if forgotten_sanctuarys.discovered == True:
            imagebutton:
                xalign 0.21
                yalign 0.34
                idle "mapsite"
                hover "mapsitehover"
                style "footstep_button"
                hovered SetVariable("selected_location", forgotten_sanctuarys)
                action Return("To Sanctuary")
        if quest31.status == 2:
            imagebutton:
                xalign 0.23
                yalign 0.30
                idle "mapsite"
                hover "mapsitehover"
                style "footstep_button"
                hovered SetVariable("selected_location", forgotten_sanctuarys)
                action Return("To Slime")
        if creek_thickets.discovered == True:
            imagebutton:
                xalign 0.11
                yalign 0.44
                idle "mapsite"
                hover "mapsitehover"
                style "footstep_button"
                hovered SetVariable("selected_location", creek_thickets)
                action Return("To Thicket")

    if current_map == grassland_map:

        imagebutton:
            xalign 0.06
            yalign 0.67
            idle "mapsite2"
            hover "mapsite2hover"
            style "walk_button"
            hovered SetVariable("selected_location", grove_of_harvest)
            action Return("Grove of Harvest")

        imagebutton:
            xalign 0.03
            yalign 0.48
            idle "map_transition_arrow4_idle"
            hover "map_transition_arrow4_hover"
            style "walk_button"
            hovered SetVariable("selected_location", grove_of_harvest)
            action Return("Lusterfield Map")

        if prattlefell_meadow.discovered == True:

            imagebutton:
                xalign 0.15
                yalign 0.45
                idle "mapsite2"
                hover "mapsite2hover"
                style "walk_button"
                hovered SetVariable("selected_location", prattlefell_meadow)
                action Return("Prattlefell Meadow")

        if bandits_hideout.discovered == True:

            imagebutton:
                xalign 0.35
                yalign 0.29
                idle "mapsite2"
                hover "mapsite2hover"
                style "walk_button"
                hovered SetVariable("selected_location", bandits_hideout)
                action Return("Bandits Hideout")

        if ursinia_glade.discovered == True:

            imagebutton:
                xalign 0.28
                yalign 0.05
                idle "mapsite2"
                hover "mapsite2hover"
                style "walk_button"
                hovered SetVariable("selected_location", ursinia_glade)
                action Return("Ursinia Glade")

            imagebutton:
                xalign 0.16
                yalign 0.01
                idle "map_transition_arrow1_idle"
                hover "map_transition_arrow1_hover"
                style "walk_button"
                hovered SetVariable("selected_location", grove_of_harvest)
                action Return("Otsovaara Map")

    if current_map == otsovaara_map:

        imagebutton:
            xalign 0.14
            yalign 0.98
            idle "map_transition_arrow3_idle"
            hover "map_transition_arrow3_hover"
            style "walk_button"
            hovered SetVariable("selected_location", grove_of_harvest)
            action Return("Grassland Map")

        if frosted_taiga.discovered == True:

            imagebutton:
                xalign 0.04
                yalign 0.73
                idle "mapsite2"
                hover "mapsite2hover"
                style "walk_button"
                hovered SetVariable("selected_location", frosted_taiga)
                action Return("Frosted Taiga")

        if avalanche_site.discovered == True:

            imagebutton:
                xalign 0.03
                yalign 0.42
                idle "mapsite2"
                hover "mapsite2hover"
                style "walk_button"
                hovered SetVariable("selected_location", avalanche_site)
                action Return("Avalanche Site")

        if skullstrewn_pass.discovered == True:

            imagebutton:
                xalign 0.07
                yalign 0.21
                idle "mapsite2"
                hover "mapsite2hover"
                style "walk_button"
                hovered SetVariable("selected_location", skullstrewn_pass)
                action Return("Skullstrewn Pass")



        if snowbound_summit_place.discovered == True:
            imagebutton:
                xalign 0.21
                yalign 0.80
                idle "mapsite2"
                hover "mapsite2hover"
                style "walk_button"
                hovered SetVariable("selected_location", snowbound_summit_place)
                action Return("Snowbound Summit")

            if "Snow_Crystal4" in opened_chests:
                imagebutton:
                    xalign 0.31
                    yalign 0.74
                    idle "mapsite2"
                    hover "mapsite2hover"
                    style "walk_button"
                    hovered SetVariable("selected_location", snowbound_summit_place)
                    action Return("Snowbound Summit Top")

        if otsovaara.discovered == True:

            imagebutton:
                xalign 0.4
                yalign 0.4
                idle "mapsite2"
                hover "mapsite2hover"
                style "walk_button"
                hovered SetVariable("selected_location", otsovaara)
                action Return("Otsovaara")

            imagebutton:
                xalign 0.16
                yalign 0.38
                idle "mapsite2"
                hover "mapsite2hover"
                style "walk_button"
                hovered SetVariable("selected_location", clawridge_ascent)
                action Return("Clawridge Ascent")

    if selected_location != None:

        vbox:
            xpos 1635
            yalign 0.035
            spacing 20
            frame:
                style "coolframe"
                xpadding 10
                ypadding 10
                xmaximum 300
                text "[selected_location.name!t]" style_prefix "screen_content"
            label "[selected_location.description!t]" text_color "#111111" text_size 25 xmaximum 270

            if len(selected_location.item) != 0:
                label _("Collectable materials:") text_color "#301410" text_size 25
                hbox:
                    spacing 5
                    for j in range(3):
                        if j < len(selected_location.item):
                            $ i = selected_location.item[j]
                            if LookForItem(i.img, inventory):
                                frame:
                                    style "slot"
                                    imagebutton:
                                        idle i.img.lower()
                                        unhovered SetVariable("selected_mapitem", None)
                                        style "click_button"
                                        action SetVariable("selected_mapitem", i)

                            else:
                                frame:
                                    style "slot"
                                    imagebutton:
                                        idle "missingitem"
                hbox:
                    spacing 5
                    for j in range(3,6):
                        if j < len(selected_location.item):
                            $ i = selected_location.item[j]
                            if LookForItem(i.img, inventory):
                                frame:
                                    style "slot"
                                    imagebutton:
                                        idle i.img.lower()
                                        unhovered SetVariable("selected_mapitem", None)
                                        style "click_button"
                                        action SetVariable("selected_mapitem", i)
                            else:
                                frame:
                                    style "slot"
                                    imagebutton:
                                        idle "missingitem"


            if len(selected_location.enemy) != 0:
                $ enemynamymap = ""
                $ enemylisty = []
                for i in selected_location.enemy:

                    if i.win + i.lose > 0:
                        $ enemylisty.append(i.name)
                    else:
                        $ enemylisty.append("???")
                $ enemynamymap = ", ".join(enemylisty)
                label _("Enemies: [enemynamymap!t]") text_color "#301410" text_size 25




            if len(selected_location.drop) != 0:
                label _("Enemy drops:") text_color "#301410" text_size 25
                hbox:
                    spacing 5
                    for i in selected_location.drop:
                        if LookForItem(i.img, inventory):
                            frame:
                                style "slot"
                                imagebutton:
                                    idle i.img.lower()
                                    style "click_button"
                                    unhovered SetVariable("selected_mapitem", None)
                                    action SetVariable("selected_mapitem", i)
                        else:
                            frame:
                                style "slot"
                                imagebutton:
                                    idle "missingitem"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
