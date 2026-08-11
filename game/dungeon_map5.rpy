default d7x = 13
default d7y = 2
default ctChest01 = False
default slime1_kp = 5
default slime2_kp = 5
default slime3_kp = 5
default slime4_kp = 5
default slime1_dp = [False, 0, 0, 0]
default slime2_dp = [False, 0, 0, 0]
default slime3_dp = [False, 0, 0, 0]
default slime4_dp = [False, 0, 0, 0]
default slime5_dp = [False, 0, 0, 0]
default slime6_dp = [False, 0, 0, 0]
default slime_sprite1 = MapUser(8, 3, "slime_sprite_0", 120, 120, "Slime")
default slime_sprite2 = MapUser(1, 3, "slime_sprite_1", 120, 120, "Slime")
default slime_sprite3 = MapUser(5, 8, "slime_sprite_2", 120, 120, "Slime")
default slime_sprite4 = MapUser(1, 15, "slime_sprite_3", 120, 120, "Slime")
image slime_sprite_a:
    "slime_sprite1"
image hefty_sprite_a:
    "hefty_sprite1"
image slime_sprite_0:
    "slime_sprite2"
    pause 0.3
    "slime_sprite3"
    pause 0.2
    "slime_sprite1"
image hefty_sprite_0:
    "hefty_sprite2"
    pause 0.3
    "hefty_sprite3"
    pause 0.2
    "hefty_sprite1"

image stream_line_straight_NS:
    "stream_line_straight"
    anchor (0.15, 0.15)
    rotate 360

image stream_line_straight_EW:
    "stream_line_straight"
    anchor (0.15, 0.15)
    rotate 90

image stream_line_bend_NE:
    "stream_line_bend"
    anchor (0.15, 0.15)
    rotate 360

image stream_line_bend_NW:
    "stream_line_bend"
    anchor (0.15, 0.15)
    rotate 270

image stream_line_bend_SE:
    "stream_line_bend"
    anchor (0.15, 0.15)
    rotate 90

image stream_line_bend_SW:
    "stream_line_bend"
    anchor (0.15, 0.15)
    rotate 180

image stream_line_fork_NSE:
    "stream_line_fork"
    anchor (0.15, 0.15)
    rotate 360

image stream_line_fork_NSW:
    "stream_line_fork"
    anchor (0.15, 0.15)
    rotate 180

image stream_line_fork_EWS:
    "stream_line_fork"
    anchor (0.15, 0.15)
    rotate 90

image stream_line_fork_EWN:
    "stream_line_fork"
    anchor (0.15, 0.15)
    rotate 270

image river_fork_NSE:
    "river_fork"
    anchor (0.15, 0.15)
    rotate 270

image river_fork_NSW:
    "river_fork"
    anchor (0.15, 0.15)
    rotate 90

image river_fork_EWS:
    "river_fork"
    anchor (0.14, 0.14)
    rotate 360

image river_fork_EWN:
    "river_fork"
    anchor (0.14, 0.14)
    rotate 180

default viscid_stream_map = {"None": 0, "tree1": 1, "tree2": 2, "bush6": 3, "bush7": 4,  "bush8": 5, "river1": 6, "river2": 7, "cliff1": 8, "bush5": 9}

label Viscid_Stream_Enter:
    $ viscid_stream_map = {"None": 0, "tree1": 1, "tree2": 2, "bush6": 3, "bush7": 4,  "bush8": 5, "river1": 6, "river2": 7, "cliff1": 8, "bush5": 9}
    $ dungeon_timers = []

    $ viscid_stream = MapPat([], "Viscid Stream", 15, 2, "grass2")
    $ viscid_stream.floorPlan([
        [9, 9, 9, 9, 8, 8, 9, 9, 6, 9, 8, 8, 8, 9, 9, 9, 9],
        [9, 3, 3, 3, 0, 0, 3, 3, 6, 3, 0, 0, 0, 3, 3, 3, 3],
        [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 9, 6, 9, 0, 0, 0, 9, 8, 8, 9],
        [9, 9, 0, 9, 8, 8, 8, 3, 6, 3, 9, 8, 8, 3, 0, 0, 9],
        [3, 3, 0, 3, 0, 7, 7, 0, 0, 0, 3, 9, 0, 0, 0, 0, 9],
        [7, 7, 0, 7, 0, 0, 0, 6, 0, 0, 0, 3, 0, 5, 4, 4, 3],
        [9, 4, 0, 5, 4, 8, 0, 6, 0, 0, 0, 7, 0, 7, 7, 7, 7],
        [9, 0, 0, 0, 0, 0, 8, 6, 9, 5, 4, 5, 0, 0, 5, 5, 4],
        [9, 0, 0, 0, 0, 9, 9, 6, 9, 0, 0, 5, 0, 0, 4, 0, 0],
        [9, 0, 0, 0, 0, 9, 9, 6, 9, 0, 0, 0, 0, 0, 0, 0, 9],
        [3, 0, 0, 0, 0, 9, 3, 6, 3, 5, 4, 4, 0, 4, 5, 4, 9],
        [8, 8, 8, 8, 0, 3, 0, 0, 7, 7, 7, 7, 0, 7, 7, 0, 9],
        [7, 7, 7, 7, 0, 7, 0, 4, 5, 5, 4, 9, 0, 0, 9, 6, 9],
        [4, 4, 5, 4, 0, 4, 0, 0, 0, 0, 0, 3, 0, 0, 9, 6, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 3, 6, 3],
        [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 6, 8]
    ], viscid_stream_map)

    $ addSprite(viscid_stream, viscid_stream.playerSprite)
    $ hefty_sprite1 = MapChaser(3, 8, "hefty_sprite_a", 130, 145, "Hefty1", [False, "", "", ""], 5, 2, "hefty_sprite_a", "hefty_sprite_0")
    $ hefty_sprite2 = MapChaser(12, 8, "hefty_sprite_a", 130, 145, "Hefty2", [False, "", "", ""], 5, 2, "hefty_sprite_a", "hefty_sprite_0")
    $ viscid_slime_sprite1 = MapMover(12, 1, "slime_sprite_0", 120, 120, "Slime", 0, 0, (1, 0))
    $ viscid_slime_sprite2 = MapMover(3, 3, "slime_sprite_0", 120, 120, "Slime", 0, 0, (1, 0))
    $ viscid_slime_sprite3 = MapMover(1, 10, "slime_sprite_0", 120, 120, "Slime", 0, 0, (1, 0))
    $ viscid_slime_sprite4 = MapMover(3, 11, "slime_sprite_0", 120, 120, "Slime", 0, 0, (0, 1))
    $ viscid_slime_sprite5 = MapMover(12, 14, "slime_sprite_0", 120, 120, "Slime", 0, 0, (0, 1))
    $ viscid_slime_sprite6 = MapMover(13, 10, "slime_sprite_0", 120, 120, "Slime", 0, 0, (2, 0))
    $ viscid_river1 = MapToggler(8, 2, "river1", 120, 120, "River1", "Block", [(10, 1)], "river1b")
    $ viscid_river2 = MapToggler(2, 6, "river2", 120, 120, "River1", "Block", [(4, 1)], "river2b")
    $ viscid_river3 = MapToggler(4, 13, "river2", 120, 120, "River1", "Block", [(5, 8), (1, 11)], "river2b")
    $ viscid_river4 = MapToggler(12, 12, "river2", 120, 120, "River1", "Block", [(7, 15)], "river2b")
    $ viscid_river5 = MapToggler(12, 7, "river2", 120, 120, "River1", "Block", [(12, 9)], "river2b")
    $ viscid_leave_map = MapUser(16, 2, "grass3", 120, 120, "To Map")
    $ viscid_leave_sanctuary = MapUser(0, 15, "grass3", 120, 120, "To Sanctuary")
    $ viscid_leave_thicket = MapUser(16, 9, "grass3", 120, 120, "To Thicket")
    $ viscid_scripture = MapUser(14, 4, "scripture_sprite", 120, 120, "Scripture")
    $ viscid_scripture2 = MapUser(15, 4, "empty", 120, 120, "Scripture")
    if "viscid_chest1" in opened_chests or "Viscid_Chest1" in opened_chests:
        $ viscid_chest1 = MapUser(3, 10, "stone_chest_opened", 120, 120, "viscid_chest1")
    else:
        $ viscid_chest1 = MapUser(3, 10, "stone_chest_closed", 120, 120, "viscid_chest1")
    $ addSprite(viscid_stream, viscid_slime_sprite1)
    $ addSprite(viscid_stream, viscid_slime_sprite2)
    $ addSprite(viscid_stream, viscid_slime_sprite3)
    $ addSprite(viscid_stream, viscid_slime_sprite4)
    $ addSprite(viscid_stream, viscid_slime_sprite5)
    $ addSprite(viscid_stream, viscid_slime_sprite6)
    $ addSprite(viscid_stream, viscid_river1)
    $ addSprite(viscid_stream, viscid_river2)
    $ addSprite(viscid_stream, viscid_river3)
    $ addSprite(viscid_stream, viscid_river4)
    $ addSprite(viscid_stream, viscid_river5)
    $ addSprite(viscid_stream, viscid_leave_map)
    $ addSprite(viscid_stream, viscid_leave_sanctuary)
    $ addSprite(viscid_stream, viscid_leave_thicket)
    $ addSprite(viscid_stream, viscid_scripture)
    $ addSprite(viscid_stream, viscid_chest1)
    $ addSprite(viscid_stream, hefty_sprite1)
    $ addSprite(viscid_stream, hefty_sprite2)
    $ addSprite(viscid_stream, viscid_scripture2)
    $ addBackQuick(viscid_stream, 10, 1, "stream_pool_button")
    $ addBackQuick(viscid_stream, 10, 2, "stream_line_bend_NW")
    $ addBackQuick(viscid_stream, 9, 2, "stream_line_straight_EW")
    $ addBackQuick(viscid_stream, 4, 1, "stream_pool_button")
    $ addBackQuick(viscid_stream, 4, 2, "stream_line_straight_NS")
    $ addBackQuick(viscid_stream, 4, 3, "stream_line_bend_NW")
    $ addBackQuick(viscid_stream, 3, 3, "stream_line_straight_EW")
    $ addBackQuick(viscid_stream, 2, 3, "stream_line_bend_SE")
    $ addBackQuick(viscid_stream, 2, 4, "stream_line_straight_NS")
    $ addBackQuick(viscid_stream, 2, 5, "stream_line_straight_NS")
    $ addBackQuick(viscid_stream, 5, 8, "stream_pool_button")
    $ addBackQuick(viscid_stream, 4, 8, "stream_line_bend_SE")
    $ addBackQuick(viscid_stream, 4, 9, "stream_line_straight_NS")
    $ addBackQuick(viscid_stream, 4, 10, "stream_line_straight_NS")
    $ addBackQuick(viscid_stream, 4, 11, "stream_line_fork_NSW")
    $ addBackQuick(viscid_stream, 4, 12, "stream_line_straight_NS")
    $ addBackQuick(viscid_stream, 1, 11, "stream_pool_button")
    $ addBackQuick(viscid_stream, 2, 11, "stream_line_straight_EW")
    $ addBackQuick(viscid_stream, 3, 11, "stream_line_straight_EW")
    $ addBackQuick(viscid_stream, 7, 15, "stream_pool_button")
    $ addBackQuick(viscid_stream, 7, 14, "stream_line_bend_SE")
    $ addBackQuick(viscid_stream, 8, 14, "stream_line_straight_EW")
    $ addBackQuick(viscid_stream, 9, 14, "stream_line_straight_EW")
    $ addBackQuick(viscid_stream, 10, 14, "stream_line_bend_SW")
    $ addBackQuick(viscid_stream, 10, 15, "stream_line_bend_NE")
    $ addBackQuick(viscid_stream, 11, 15, "stream_line_straight_EW")
    $ addBackQuick(viscid_stream, 12, 15, "stream_line_bend_NW")
    $ addBackQuick(viscid_stream, 12, 14, "stream_line_straight_NS")
    $ addBackQuick(viscid_stream, 12, 13, "stream_line_straight_NS")
    $ addBackQuick(viscid_stream, 12, 9, "stream_pool_button")
    $ addBackQuick(viscid_stream, 12, 8, "stream_line_straight_NS")

    $ addBackQuick(viscid_stream, 7, 5, "river_fork_EWS")
    $ addBackQuick(viscid_stream, 8, 5, "river_fork_EWN")
    $ addBackQuick(viscid_stream, 7, 12, "river_fork_EWN")

    $ addBackQuick(viscid_stream, 4, 5, "rivertl")
    $ addBackQuick(viscid_stream, 4, 6, "riverbr")
    $ addBackQuick(viscid_stream, 9, 5, "rivertr")
    $ addBackQuick(viscid_stream, 9, 6, "riverbl")
    $ addBackQuick(viscid_stream, 10, 6, "rivertr")
    $ addBackQuick(viscid_stream, 10, 7, "riverbl")
    $ addBackQuick(viscid_stream, 6, 12, "rivertl")
    $ addBackQuick(viscid_stream, 6, 13, "riverbr")
    $ addBackQuick(viscid_stream, 15, 12, "rivertr")




    $ current_location = viscid_stream
    jump Viscid_Stream_Loop
label Viscid_Stream_Loop:
    show screen dungeon_buttons
    $ disableC = False
    $ sprite = viscid_stream.playerSprite

    call screen dungeon_map(viscid_stream)

    if _return == "viscid_chest1":
        $ disableC = True
        show screen dungeon_map(viscid_stream)
        if "viscid_chest1" in opened_chests or "Viscid_Chest1" in opened_chests:
            "The Chest is empty."
        else:
            "You look inside the chest, there seem to be some items stored in the chest."
            "You found a slime necklace, 2 pieces of iron and a green ointment."
            $ addItem("Slime Necklace", inventory, 1)
            $ addItem("Iron Ingot", inventory, 2)
            $ addItem("Green Ointment", inventory, 1)
            $ opened_chests["viscid_chest1"] = True
            $ viscid_chest1.img = "stone_chest_opened"

    if _return == "Scripture":
        $ disableC = True
        show screen dungeon_map(viscid_stream)
        if resolution in learnedabilities:
            "You look at the scripture, it seems to be written in an entirely different language."
        else:

            "You look at the scripture, there seem to be an aching aura surrounding you."
            "The ancient scripture is speaking to your mind directly..."
            "You hold both sides of your head, the pain in your head grows more unbearable."
            "Suddenly, the aching stops."
            "You look around, nothing has changed, but your body feels weird."
            "You look at the scripture again... it seems you've learnt a new skill."
            "{i}Resolution: Reduce your Lust based on your INT.{/i}"
            $ learnedabilities.append(resolution)

    if _return == "To Thicket":
        $ disableC = True
        show screen dungeon_map(viscid_stream)
        call Leaving_Viscid_Stream from _call_Leaving_Viscid_Stream_5
        if creek_thickets.discovered == False:
            "You follow the dirt path in the Viscid Stream."
            "There's a dense forest ahead of you, but you squeeze your body through tight spots here and there."
            "After a few minutes, you've finally arrived to somewhere open."
            "You've arrived to another riverside area. Maybe there's something you can find here..."
            $ creek_thickets.discovered = True
            jump Creek_Thicket_Enter
        else:
            jump Dark_Forest_Map

    if _return == "Gate":
        $ disableC = True
        show screen dungeon_map(viscid_stream)
        if sprite.y < 12:
            "The door seems to be barred from the other side..."
        else:
            "You push the horizontal plank upwards. The door is now unlocked."
            $ removeSprite(viscid_stream, gate_sprite1)
            $ addBack(viscid_stream, gate_sprite2)
    if _return == "To Map":
        $ disableC = True
        scene black
        with dissolve

        menu:
            "Do you wish to leave? All dungeon status will not be saved."
            "Yes{#LeaveViscid}":
                call Leaving_Viscid_Stream from _call_Leaving_Viscid_Stream
                jump Dark_Forest_Map
            "No{#LeaveViscid}":
                pass
    if _return == "To Sanctuary":
        $ disableC = True
        scene black
        with dissolve
        call Leaving_Viscid_Stream from _call_Leaving_Viscid_Stream_1
        if forgotten_sanctuarys.discovered == False:
            "You follow the dirt path in the Viscid Stream."
            "There's a dense forest ahead of you, but you squeeze your body through tight spots here and there."
            "After a few minutes, you've finally arrived to somewhere open."
            "You notice there's a hint of white rock in front of you... it looks... like an abandoned sanctuary..."
            $ forgotten_sanctuarys.discovered = True
            jump Forgotten_Sanctuary_Enter
        else:
            jump Dark_Forest_Map
    if _return == "Restart":
        $ disableC = True
        show screen dungeon_map(viscid_stream)
        call Leaving_Viscid_Stream from _call_Leaving_Viscid_Stream_2

        scene black
        with dissolve
        pause 1
        "You enter the viscid stream."
        jump Viscid_Stream_Enter
    if _return == "Slime1":
        $ slime1_kp = 3
    if _return == "Slime2":
        $ slime2_kp = 3
    if _return == "Slime3":
        $ slime3_kp = 3
    if _return == "Slime4":
        $ slime4_kp = 3
    if _return == "Hefty1":
        $ mimic_num = 1
        jump Viscid_Stream_Hefty
    if _return == "Hefty2":
        $ mimic_num = 2
        jump Viscid_Stream_Hefty

    jump Viscid_Stream_Loop

label Leaving_Viscid_Stream:
    hide screen dungeon_map
    hide screen dungeon_buttons
    return
label Viscid_Stream_Hefty:
    $ disableC = True
    show screen dungeon_map(viscid_stream)
    $ enct = None
    "The big slime begins to approach you..."
    e "F-fuck, that's bigger than in the green forest..."
    jump heftyslime_battle

image bush6a:
    "bush6b"
    pause 2.5
    "bush6c"
    pause .5
    repeat

label Creek_Thicket_Enter:
    $ dungeon_timers = []
    $ d9x = 10
    $ d9y = 2
    $ tenki_sprite9 = MapUser(d9x, d9y, "e_dungeon", 120, 200, no_op)
    $ dungeon9_map = [
    [MapTile(MapThing("tree8")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree7"))],
    [MapTile(MapThing("tree4")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2"))],
    [MapTile(MapThing("tree4")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile()],
    [MapTile(MapThing("tree4")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("bush5"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush1")), MapTile(MapThing("bush1")), MapTile(), MapTile(), MapTile(MapThing("bush1")), MapTile(MapThing("bush1")), MapTile(), MapTile(MapThing("bush6"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush1")), MapTile(MapThing("rivertl")), MapTile(MapThing("river2")), MapTile(), MapTile(MapThing("river2")), MapTile(MapThing("river2")), MapTile(), MapTile(MapThing("river2"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(MapThing("bush1")), MapTile(MapThing("bush1")), MapTile(MapThing("river1")), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(MapThing("bush1")), MapTile(MapThing("bush1")), MapTile(MapThing("river1")), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(MapThing("bush1")), MapTile(), MapTile(MapThing("bush1")), MapTile(MapThing("rivertl")), MapTile(MapThing("riverbr")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(MapThing("cliff1")), MapTile(), MapTile(MapThing("cliff1")), MapTile(MapThing("river1")), MapTile(MapThing("bush1")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cliff1")), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("river1")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(MapThing("bush1")), MapTile(MapThing("river1")), MapTile(MapThing("bush1")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush1")), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(MapThing("bush1")), MapTile(MapThing("river1")), MapTile(MapThing("bush1")), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(MapThing("bush1")), MapTile(MapThing("river1")), MapTile(MapThing("bush1")), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(MapThing("bush1")), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree5")), MapTile(), MapTile(), MapTile(MapThing("bush1")), MapTile(MapThing("river1")), MapTile(MapThing("bush1")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree7")), MapTile(MapThing("river1")), MapTile(MapThing("tree8")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1"))],
    [MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("river1")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2"))]
    ]
    $ creek_thicket = MapPat(dungeon9_map, "Creek Thicket", d9x, d9y, "grass2")

    $ hefty_sprite3 = MapChaser(4, 4, "hefty_sprite_a", 130, 145, "Hefty1", [False, "", "", ""], 5, 2, "hefty_sprite_a", "hefty_sprite_0")
    $ hefty_sprite4 = MapChaser(2, 6, "hefty_sprite_a", 130, 145, "Hefty2", [False, "", "", ""], 5, 2, "hefty_sprite_a", "hefty_sprite_0")
    $ hefty_sprite5 = MapChaser(1, 10, "hefty_sprite_a", 130, 145, "Hefty3", [False, "", "", ""], 5, 2, "hefty_sprite_a", "hefty_sprite_0")
    $ hefty_sprite6 = MapChaser(2, 16, "hefty_sprite_a", 130, 145, "Hefty4", [False, "", "", ""], 5, 2, "hefty_sprite_a", "hefty_sprite_0")
    $ barrel_sprite1 = MapUser(7, 6, "wolf_statue", 120, 120, "Wolf")
    $ barrel_sprite2 = MapUser(9, 6, "wolf_statue", 120, 120, "Wolf")
    $ barrel_sprite3 = MapUser(2, 15, "barrel_sprite", 120, 120, "Barrel")
    $ crosssign_sprite1 = MapUser(7, 5, "crosssign_sprite", 120, 120, "Crosssign")
    $ crosssign_sprite2 = MapUser(10, 5, "crosssign_sprite", 120, 120, "Crosssign")
    $ smol_sprite1 = MapUser(1, 4, "bush6a", 120, 120, "Smol")
    $ river_sprite1 = MapUser(7, 8, "river2", 120, 120, "River1")
    $ leave_sprite1 = MapUser(11, 2, "grass3", 120, 120, "Leave")
    $ river_sprite2 = MapUser(10, 8, "river2", 120, 120, "River2")
    $ river_sprite3 = MapUser(7, 8, "river2b", 120, 120, "River3")
    $ river_sprite4 = MapUser(10, 8, "river2b", 120, 120, "River4")
    $ river_sprite5 = MapUser(4, 13, "river_barrel", 120, 120, "River3")
    $ button_spritea = MapUser(10, 13, "button_spritea", 120, 120, "Button")
    $ button_spriteb = MapUser(7, 15, "button_spriteb", 120, 120, "Button")
    $ button_spritec = MapUser(9, 17, "button_spritec", 120, 120, "Button")
    $ button_sprited = MapUser(7, 13, "button_sprited", 120, 120, "Button")
    if botanical_journal01 not in botanical_journal.content:
        $ book_sprite1 = MapUser(10, 11, "botanical journal", 120, 120, "Book")
        $ addSprite(creek_thicket, book_sprite1)
    if ctChest01:
        $ chest_sprite1 = MapUser(6, 17, "chest_sprite4", 120, 120, "Opened")
    else:
        $ chest_sprite1 = MapUser(6, 17, "chest_sprite2", 120, 120, "Chest")

    $ addSprite(creek_thicket, chest_sprite1)
    $ pawprint_sprite1 = MapUser(4, 1, "pawprint_sprite1", 120, 120, "Pawprint")
    $ addSprite(creek_thicket, leave_sprite1)
    $ addSprite(creek_thicket, tenki_sprite9)
    $ addSprite(creek_thicket, hefty_sprite3)
    $ addSprite(creek_thicket, hefty_sprite4)
    $ addSprite(creek_thicket, hefty_sprite5)
    $ addSprite(creek_thicket, hefty_sprite6)
    $ addSprite(creek_thicket, smol_sprite1)
    $ addSprite(creek_thicket, river_sprite1)
    $ addSprite(creek_thicket, river_sprite2)
    $ addSprite(creek_thicket, barrel_sprite1)
    $ addSprite(creek_thicket, barrel_sprite2)
    $ addSprite(creek_thicket, barrel_sprite3)
    $ addBack(creek_thicket, button_spritea)
    $ addBack(creek_thicket, button_spriteb)
    $ addBack(creek_thicket, button_spritec)
    $ addBack(creek_thicket, button_sprited)
    $ addBack(creek_thicket, crosssign_sprite1)
    $ addBack(creek_thicket, crosssign_sprite2)

    $ current_location = creek_thicket
    jump Creek_Thicket_Loop

label Creek_Thicket_Loop:
    show screen dungeon_buttons
    $ disableC = False
    $ sprite = tenki_sprite9
    if creek_thicket.mappy[13][4].user != None and creek_thicket.mappy[13][4].user.img == "barrel_sprite":
        $ removeSprite(creek_thicket, barrel_sprite3)
        $ addBack(creek_thicket, river_sprite5)
    if creek_thicket.mappy[5][7].user != None and creek_thicket.mappy[5][7].user.img == "wolf_statue":
        if creek_thicket.mappy[5][10].user != None and creek_thicket.mappy[5][10].user.img == "wolf_statue":
            if creek_thicket.mappy[8][7].user != None and creek_thicket.mappy[8][7].user.img == "river2":
                if creek_thicket.mappy[8][10].user != None and creek_thicket.mappy[8][10].user.img == "river2":
                    $ removeSprite(creek_thicket, river_sprite1)
                    $ removeSprite(creek_thicket, river_sprite2)
                    $ addBack(creek_thicket, river_sprite3)
                    $ addBack(creek_thicket, river_sprite4)
    if creek_thicket.mappy[13][10].user != None:
        if slime2_dp[0] == 0:
            $ slime2_dp[0] = 1
        else:
            $ creek_thicket.clearBack(interaction = "Pawprint")
            $ slime2_dp[0] = 0
    if creek_thicket.mappy[15][7].user != None:
        if slime2_dp[0] == 1:
            $ slime2_dp[0] = 2
        else:
            $ creek_thicket.clearBack(interaction = "Pawprint")
            $ slime2_dp[0] = 0
    if creek_thicket.mappy[17][9].user != None:
        if slime2_dp[0] == 2:
            $ slime2_dp[0] = 3
        else:
            $ creek_thicket.clearBack(interaction = "Pawprint")
            $ slime2_dp[0] = 0
    if creek_thicket.mappy[13][7].user != None:
        if slime2_dp[0] == 3:
            $ slime2_dp[0] = 4
        else:
            $ creek_thicket.clearBack(interaction = "Pawprint")
            $ slime2_dp[0] = 0
    if slime2_dp[0] > 0 and slime2_dp[0] < 4:
        if creek_thicket.locateBackOnTop(sprite) != None and creek_thicket.locateBackOnTop(sprite).interaction == "Pawprint":
            $ creek_thicket.clearBack(interaction = "Pawprint")
            $ slime2_dp[0] = 0
        if creek_thicket.mappy[sprite.y][sprite.x].back == None:
            $ x, y = sprite.getLocation()
            $ newSpriteImg = "pawprint_sprite " + e_d
            $ addBack(creek_thicket, MapUser(x, y, newSpriteImg, 120, 120, "Pawprint"))
    if slime2_dp[0] == 4 and chest_sprite1.img == "chest_sprite2":
        $ chest_sprite1.img = "chest_sprite4"
        $ chest_sprite1.interaction = "Open"
    if (enct != None and enct[:5] == "Hefty") or (isinstance(_return, str) and _return[:5] == "Hefty"):
        if enct != None:
            $ mimic_num = int(enct[5]) + 4
        else:
            $ mimic_num = int(_return[5]) + 4
        $ disableC = True
        show screen dungeon_map(creek_thicket)
        $ enct = None
        "The big slime begins to approach you..."
        e "F-fuck, that's bigger than in the green forest..."
        jump heftyslime_battle

    call screen dungeon_map(creek_thicket)
    if _return == "Smol":
        $ disableC = True
        show screen dungeon_map(creek_thicket)
        "You peek at the small creature inside the bush."
        if (hefty_sprite3.death and hefty_sprite4.death and hefty_sprite5.death and hefty_sprite6.death) or little_guy_shop:
            if little_guy_shop:
                "It seems to be quite friendly towards your presence, despite the infestation of slime around the forest."
            else:
                "It seems to be a little too excited to see the slimes gone from the area."
            $ little_guy_shop = True

            "You snoop around its place, you realise there's a few items it's been hoarding for a while."
            "The little guy seems to be curious about you items too... perhaps you can come to an agreement or some sort..."
            jump Little_Guy_Shopping
        else:

            "It was too dark to properly see the little guy, and it seems to be too scared to come out."
            "Only staring at huge slime in fright..."
            "Maybe you need to... defeat all the slime in the area to comfort it a little."

    if _return == "Book":
        $ disableC = True
        show screen dungeon_map(creek_thicket)
        "You pick up the book..."
        $ removeSprite(creek_thicket, book_sprite1)
        $ botanical_journal01.addTo(botanical_journal)
        $ addItem("Botanical Journal", inventory, 1)
        $ book_page = 0
        show screen book_read(botanical_journal)

        booky "{i}'Botanical Journal of Plants In and Around the Dark Forest: Species, Uses, and Dangers.'\n {b}-y W—t-r A-z-var- {/b}{/i}"
        "You sigh as you open the book to the first page. It seems like the writing quality will deteriorate the further you go down the page."
        "It's a bit pathetic to see the one remaining entry at the end, laying loose against the back cover. You pick it up and read it."
        call Book_Botanical_Journal from _call_Book_Botanical_Journal_1
        "The words have barely faded, so deeply etched are they into the bottom of the page."
        "It is upsetting to think that a large part of this person's thoughts have disappeared, even from their writing."
        "Only the lucky, and those which were most important to him survived unblemished."
        "There is nothing more for you to read right now. You decide to stick the book into your inventory."
        "Perhaps there are more fragments somewhere around here."
        msg "The book 'Medicinal Botany, by ???' is now stored in your inventory."
        msg "To read the book again, interact with the book in the inventory."
    if _return == "Restart":
        scene black with dissolve
        call Leaving_Creek_Thicket from _call_Leaving_Creek_Thicket_1
        jump Creek_Thicket_Enter
    if _return == "Chest":
        $ disableC = True
        show screen dungeon_map(creek_thicket)
        "You try to open the chest, but to no avail... Maybe there's something around the area that can unlock the chest..."
    if _return == "Open":
        $ disableC = True
        show screen dungeon_map(creek_thicket)
        "You open the chest in front of you, there's a Tribal Spear and 3 pieces of Green Ointment inside."
        "You put them in your pocket, and continues on your way."
        $ addItem("Green Ointment", inventory, 3)
        $ addItem("Tribal Spear", inventory, 1)
        $ chest_sprite1.img = "chest_sprite3"
        $ chest_sprite1.interaction = "Opened"
    if _return == "Leave":
        "You leave the creek thicket along the path ahead of you."
        call Leaving_Creek_Thicket from _call_Leaving_Creek_Thicket_2
        jump Dark_Forest_Map

    jump Creek_Thicket_Loop
label Creek_Thicket_Hefty:
    $ disableC = True
    show screen dungeon_map(creek_thicket)
    $ enct = None
    "The big slime begins approaching you..."
    e "F-fuck, that's bigger than in the green forest..."
    jump heftyslime_battle
label Little_Guy_Shopping:
    menu:
        "Buy 2 pieces of chestnut for 3 carrots" if LookForItemNumber("Carrot", inventory) >= 3:
            "You take out 3 pieces of carrot, the creature immediately blushes with excitement, it runs towards the back of the bush..."
            "After mere seconds, it carries two pieces of chestnut in its embrace, and drops it in front of your leg."
            "The little creature greedily drags the carrots in the back, you can hear a few cackle emanating from the direction."
            $ addItem("Chestnut", inventory, 2)
            $ removeItem("Carrot", inventory, 3)
        "{s}Buy 2 pieces of chestnut for 3 carrots{/s}" if LookForItemNumber("Carrot", inventory) < 3:
            "You... don't seem to own enough carrots for the little creature's appetite."
        "Leave":

            "You wave farewell to the little creature, and continues on your journey."
            jump Creek_Thicket_Loop

    jump Little_Guy_Shopping
label Leaving_Creek_Thicket:
    $ removeSprite(creek_thicket, tenki_sprite9)

    $ removeSprite(creek_thicket, hefty_sprite3)
    $ removeSprite(creek_thicket, hefty_sprite4)
    $ removeSprite(creek_thicket, hefty_sprite5)
    $ removeSprite(creek_thicket, hefty_sprite6)
    hide screen dungeon_map
    hide screen dungeon_buttons
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
