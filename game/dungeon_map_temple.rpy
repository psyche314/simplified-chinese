default temple_of_tapjoo_floor = {"temple_floor1": 10, "temple_floor2": 10, "temple_floor3": 5, "temple_floor4": 5, "temple_floor5": 2, "temple_floor6": 2, "temple_floor7": 1, "temple_floor8": 1}
default temple_of_tapjoo_map = {"None": 0, "temple_top1": 1, "temple_wall1": 2, "temple_wall2": 3, "temple_wall3": 4,  "temple_wall4": 5}


default temple_entrance = MapPat([], "Temple of Tapjoo", 5, 1, temple_of_tapjoo_floor)
default temple_hall = MapPat([], "Temple of Tapjoo", 5, 1, temple_of_tapjoo_floor)
default temple_scriptorium = MapPat([], "Temple of Tapjoo", 5, 1, temple_of_tapjoo_floor)
default temple_undercroft = MapPat([], "Temple of Tapjoo", 4, 1, temple_of_tapjoo_floor)
default temple_sanctum = MapPat([], "Temple of Tapjoo", 1, 7, temple_of_tapjoo_floor)
default temple_of_tapjoo = temple_entrance

default temple_totem_dummy2 = MapStorer(2, 8, "temple_totem_dummy", 120, 120, "Dummy", None)

init python:
    def temple_room(location):
        if location == "entrance":
            return temple_entrance
        if location == "hall":
            return temple_hall
        if location == "scriptorium":
            return temple_scriptorium
        if location == "undercroft":
            return temple_undercroft
        if location == "sanctum":
            return temple_sanctum
        return location

    def temple_room_id(location):
        if location == temple_entrance:
            return "entrance"
        if location == temple_hall:
            return "hall"
        if location == temple_scriptorium:
            return "scriptorium"
        if location == temple_undercroft:
            return "undercroft"
        if location == temple_sanctum:
            return "sanctum"
        return location

    def temple_room_is_current(location):
        return temple_of_tapjoo == temple_room(location)

image temple_stallion2:
    "temple_stallion"
    crop (0, 120, 120, 120)

image temple_stallion1:
    "temple_stallion"
    crop (0, 0, 120, 120)

label Temple_of_Tapjoo_Enter:
    $ renpy.music.play(mUforest, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ temple_of_tapjoo = temple_entrance
    $ temple_entrance.start_x = 5
    $ temple_entrance.start_y = 1
    jump Temple_of_Tapjoo

label Temple_of_Tapjoo:
    $ dungeon_timers = []
    $ temple_entrance.floorPlan([
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 2, 1, 2, 3, 0, 3, 2, 1, 2, 1],
    [1, 0, 2, 0, 0, 0, 0, 0, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 2, 2, 2, 2, 2, 2, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 4, 4, 4, 0, 4, 4, 4, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 2, 2, 3, 0, 3, 2, 2, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 4, 4, 4, 0, 4, 4, 4, 1, 1],
    [2, 2, 4, 4, 4, 0, 4, 4, 4, 2, 2]
    ], temple_of_tapjoo_map)

    $ temple_hall.floorPlan([   
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 2, 1, 2, 3, 0, 3, 2, 1, 2, 1],
    [1, 1, 2, 0, 0, 0, 0, 0, 2, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 2, 2, 3, 0, 3, 2, 2, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 2],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2]
    ], temple_of_tapjoo_map)

    $ temple_scriptorium.floorPlan([
    [1, 1, 1, 1, 1, 0, 1 ,1, 1, 1, 1, 1],
    [1, 2, 2, 2, 3, 0, 3, 2, 2, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 2, 2, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 2, 2, 2, 3, 0, 0, 3, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 3, 0, 3, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 2, 2, 2, 2, 0, 2, 2, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    ], temple_of_tapjoo_map)

    $ temple_undercroft.floorPlan([
    [1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 2, 2, 3, 0, 3, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 2, 2, 3, 0, 3, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 2, 2, 3, 0, 3, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 3, 0, 3, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 2, 2, 2]
    ], temple_of_tapjoo_map)

    $ temple_sanctum.floorPlan([
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 2, 2, 2, 1, 1, 3, 0, 3, 1, 1, 1, 3, 0, 3, 1, 1],
    [1, 1, 0, 0, 0, 2, 2, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 3, 0, 3, 1, 1], 
    [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1], 
    [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 3, 0, 0, 0, 3, 1], 
    [2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 2, 2, 0, 0, 4, 0, 0, 2], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 4, 0, 0], 
    [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 5, 0, 0, 1],
    [1, 1, 0, 0, 0, 2, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 2, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 2, 0, 2, 2, 2, 2, 2, 0, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 2]
    ], temple_of_tapjoo_map)

    if temple_entrance.entranceCount == 0:
        $ temple_totem_moss = MapStorer(5, 3, "temple_totem_moss", 120, 120, "Totem Moss", None)
        $ temple_totem_horn = MapStorer(3, 2, "temple_totem_horn", 120, 120, "Totem Horn", None)
        $ temple_totem_shepherd = MapStorer(3, 9, "temple_totem_shepherd", 120, 120, "Totem Shepherd", None)
        $ temple_totem_dragon = MapStorer(4, 15, "temple_totem_dragon", 120, 120, "Totem Dragon", None)
        $ temple_totem_kantele = MapStorer(2, 8, "temple_totem_kantele", 120, 120, "Totem Kantele", None)
        $ temple_totem_dummy1 = MapStorer(2, 8, "temple_totem_dummy", 120, 120, "Dummy", None)
        $ temple_totem_dummy2 = MapStorer(2, 8, "temple_totem_dummy", 120, 120, "Dummy", None)
        $ temple_rahim_sprite = MapStorer(2, 4, "temple_rahim_sprite", 150, 180, "Rahim", {"Location": "entrance"})
        $ temple_furkan_sprite = MapStorer(9, 10, "temple_furkan_sprite", 150, 180, "Furkan", {"Location": "entrance"})
        $ temple_sebas_sprite = MapStorer(9, 10, "temple_sebas_sprite", 150, 180, "Sebas", {"Location": "entrance"})


    if temple_room_is_current(temple_totem_moss.status) and temple_of_tapjoo.inventory != temple_totem_moss:
        $ addSprite(temple_room(temple_totem_moss.status), temple_totem_moss)
    if temple_room_is_current(temple_totem_horn.status) and temple_of_tapjoo.inventory != temple_totem_horn:
        $ addSprite(temple_room(temple_totem_horn.status), temple_totem_horn)
    if temple_room_is_current(temple_totem_shepherd.status) and temple_of_tapjoo.inventory != temple_totem_shepherd:
        $ addSprite(temple_room(temple_totem_shepherd.status), temple_totem_shepherd)
    if temple_room_is_current(temple_totem_dragon.status) and temple_of_tapjoo.inventory != temple_totem_dragon:
        $ addSprite(temple_room(temple_totem_dragon.status), temple_totem_dragon)
    if temple_room_is_current(temple_totem_kantele.status) and temple_of_tapjoo.inventory != temple_totem_kantele:
        $ addSprite(temple_room(temple_totem_kantele.status), temple_totem_kantele)
    if temple_room_is_current(temple_totem_dummy1.status) and temple_of_tapjoo.inventory != temple_totem_dummy1:
        $ addSprite(temple_room(temple_totem_dummy1.status), temple_totem_dummy1)
    if temple_room_is_current(temple_totem_dummy2.status) and temple_of_tapjoo.inventory != temple_totem_dummy2:
        $ addSprite(temple_room(temple_totem_dummy2.status), temple_totem_dummy2)
    if temple_room_is_current(temple_rahim_sprite.status["Location"]):
        $ addSprite(temple_room(temple_rahim_sprite.status["Location"]), temple_rahim_sprite)
    if vote_result < 0:
        if temple_room_is_current(temple_sebas_sprite.status["Location"]):
            $ addSprite(temple_room(temple_sebas_sprite.status["Location"]), temple_sebas_sprite)
    else:
        if temple_room_is_current(temple_furkan_sprite.status["Location"]):
            $ addSprite(temple_room(temple_furkan_sprite.status["Location"]), temple_furkan_sprite)

    if temple_of_tapjoo == temple_entrance:
        $ temple_stair_sprite1 = MapUser(5, 0, "temple_stair_front", 120, 120, "To Longhouse")
        $ temple_stair_sprite2 = MapUser(5, 17, "temple_stair_front", 120, 120, "Entrance To Hall")

        $ temple_mural_sprite1 = MapUser(4, 8, "temple_mural1", 120, 140, "Mural")
        $ temple_mural_sprite2 = MapUser(7, 8, "temple_mural2", 120, 140, "Mural")
        $ temple_mural_sprite3 = MapUser(3, 8, "temple_mural3", 120, 140, "Mural")
        $ temple_mural_sprite4 = MapUser(6, 8, "temple_mural4", 120, 140, "Mural")
        $ temple_mural_sprite5 = MapUser(8, 8, "temple_mural5", 120, 140, "Mural")
        $ temple_mural_sprite6 = MapUser(2, 8, "temple_mural6", 120, 140, "Mural")
        $ temple_mural_sprite7 = MapUser(5, 8, "temple_mural7", 120, 140, "Mural")

        $ temple_button_sprite1 = MapUser(5, 14, "button_sprite3", 120, 120, "Button1")


        $ addSprite(temple_entrance, temple_mural_sprite1)
        $ addSprite(temple_entrance, temple_mural_sprite2)
        $ addSprite(temple_entrance, temple_mural_sprite3)
        $ addSprite(temple_entrance, temple_mural_sprite4)
        $ addSprite(temple_entrance, temple_mural_sprite5)
        $ addSprite(temple_entrance, temple_mural_sprite6)
        $ addSprite(temple_entrance, temple_mural_sprite7)
        $ addBack(temple_entrance, temple_button_sprite1)
        $ addSprite(temple_entrance, temple_stair_sprite1)
        $ addSprite(temple_entrance, temple_stair_sprite2)
        $ addSprite(temple_entrance, temple_entrance.playerSprite)


        if temple_entrance.playerSprite.interaction == "Opened":
            $ temple_gate_sprite1 = MapUser(5, 11, "temple_gate_open", 120, 120, "Ghost Gate")
            $ addBack(temple_entrance, temple_gate_sprite1)
            $ temple_door_sprite1 = MapUser(5, 16, "temple_door_front_open", 120, 130, "Door")
            $ addBack(temple_entrance, temple_door_sprite1)
        else:
            $ temple_gate_sprite1 = MapUser(5, 11, "temple_gate_closed", 120, 120, "Ghost Gate")
            $ addFront(temple_entrance, temple_gate_sprite1)
            $ temple_door_sprite1 = MapUser(5, 16, "temple_door_front_closed", 120, 130, "Door")
            $ addSprite(temple_entrance, temple_door_sprite1)

    if temple_of_tapjoo == temple_hall:
        $ temple_stair_sprite1 = MapUser(5, 0, "temple_stair_front", 120, 120, "To Entrance")
        $ temple_stair_sprite2 = MapUser(5, 14, "temple_stair_front", 120, 120, "To Scriptorium")
        $ temple_stair_sprite3 = MapUser(10, 11, "temple_stair_side", 120, 120, "Hall To Sanctum")
        $ temple_lantern_sprite1 = MapUser(2, 3, "temple_lantern_left", 120, 120, "Lantern")
        $ temple_lantern_sprite2 = MapUser(8, 3, Transform("temple_lantern_left", xzoom = -1), 120, 120, "Lantern")
        $ temple_top_sprite1 = MapUser(3, 4, "temple_top1", 120, 120, "Top")
        $ temple_top_sprite2 = MapUser(5, 4, "temple_top1", 120, 120, "Top")
        $ temple_top_sprite3 = MapUser(7, 4, "temple_top1", 120, 120, "Top")
        $ temple_top_sprite4 = MapUser(10, 12, "temple_top1", 120, 120, "Top")
        $ temple_top_sprite5 = MapUser(9, 12, "temple_top1", 120, 120, "Top")
        $ temple_pillar_sprite1 = MapStorer(3, 5, "temple_pillar_hart", 120, 120, "Pillar", 2)
        $ temple_pillar_sprite2 = MapStorer(5, 5, "temple_pillar_bull", 120, 120, "Pillar", 3)
        $ temple_pillar_sprite3 = MapStorer(7, 5, "temple_pillar_ram", 120, 120, "Pillar", 1)

        $ temple_button_sprite1 = MapUser(4, 11, "button_sprite3", 120, 120, "Button1")
        $ temple_button_sprite2 = MapUser(6, 11, "button_sprite3", 120, 120, "Button2")
        if temple_hall.getMapStatus(0):
            $ temple_door_sprite1 = MapUser(5, 8, "temple_door_front_open", 120, 130, "Door")
            $ addBack(temple_hall, temple_door_sprite1)
        else:
            $ temple_door_sprite1 = MapUser(5, 8, "temple_door_front_closed", 120, 130, "Door")
            $ addSprite(temple_hall, temple_door_sprite1)
        if temple_hall.getMapStatus(1):
            $ temple_door_sprite2 = MapUser(9, 11, "temple_door_side_open", 120, 120, "Door")
            $ addBack(temple_hall, temple_door_sprite2)
        else:
            $ temple_door_sprite2 = MapUser(9, 11, "temple_door_side_closed", 120, 120, "Door")
            $ addSprite(temple_hall, temple_door_sprite2)

        if temple_hall.getMapStatus(4) and temple_hall.getMapStatus(5):
            $ temple_boulder_sprite1 = MapStorer(6, 11, "temple_boulder", 120, 120, "Ball Boulder", "temple_boulder")
            $ temple_boulder_sprite2 = MapStorer(4, 11, "temple_boulder", 120, 120, "Ball Boulder", "temple_boulder")
            $ addSprite(temple_hall, temple_boulder_sprite1)
            $ addSprite(temple_hall, temple_boulder_sprite2)
        elif temple_hall.getMapStatus(2):
            if not temple_hall.getMapStatus(4) and not temple_hall.getMapStatus(5):
                if temple_hall.getMapStatus(3):
                    $ temple_boulder_sprite2 = MapStorer(5, 11, "temple_boulder", 120, 120, "Ball Boulder", "temple_boulder")
                    $ addSprite(temple_hall, temple_boulder_sprite2)
                $ temple_boulder_sprite1 = MapStorer(7, 11, "temple_boulder", 120, 120, "Ball Boulder", "temple_boulder")
            elif temple_hall.getMapStatus(4):
                $ temple_boulder_sprite1 = MapStorer(4, 11, "temple_boulder", 120, 120, "Ball Boulder", "temple_boulder")
                if temple_hall.getMapStatus(3):
                    $ temple_boulder_sprite2 = MapStorer(7, 11, "temple_boulder", 120, 120, "Ball Boulder", "temple_boulder")
                    $ addSprite(temple_hall, temple_boulder_sprite2)
            elif temple_hall.getMapStatus(5):
                $ temple_boulder_sprite1 = MapStorer(6, 11, "temple_boulder", 120, 120, "Ball Boulder", "temple_boulder")
                if temple_hall.getMapStatus(3):
                    $ temple_boulder_sprite2 = MapStorer(7, 11, "temple_boulder", 120, 120, "Ball Boulder", "temple_boulder")
                    $ addSprite(temple_hall, temple_boulder_sprite2)
            $ addSprite(temple_hall, temple_boulder_sprite1)



        $ addSprite(temple_hall, temple_pillar_sprite1)
        $ addSprite(temple_hall, temple_pillar_sprite2)
        $ addSprite(temple_hall, temple_pillar_sprite3)
        $ addBack(temple_hall, temple_button_sprite1)
        $ addBack(temple_hall, temple_button_sprite2)

        $ addFront(temple_hall, temple_lantern_sprite1)
        $ addFront(temple_hall, temple_lantern_sprite2)
        $ addFront(temple_hall, temple_top_sprite1)
        $ addFront(temple_hall, temple_top_sprite2)
        $ addFront(temple_hall, temple_top_sprite3)
        $ addFront(temple_hall, temple_top_sprite4)
        $ addFront(temple_hall, temple_top_sprite5)
        $ addSprite(temple_hall, temple_stair_sprite1)
        $ addSprite(temple_hall, temple_stair_sprite2)
        $ addSprite(temple_hall, temple_stair_sprite3)
        $ addSprite(temple_hall, temple_hall.playerSprite)

    if temple_of_tapjoo == temple_scriptorium:
        $ temple_stair_sprite1 = MapUser(5, 0, "temple_stair_front", 120, 120, "Scriptorium To Hall")
        $ temple_table1_sprite1 = MapUser(2, 2, "temple_scriptorium_table", 120, 120, "Table")
        $ temple_table2_sprite1 = MapUser(3, 2, "temple_scriptorium_table_right", 120, 120, "Table")
        $ temple_table1_sprite2 = MapUser(8, 2, "temple_scriptorium_table", 120, 120, "Table")
        $ temple_table2_sprite2 = MapUser(9, 2, "temple_scriptorium_table_right", 120, 120, "Table")
        $ temple_scrolls_sprite1 = MapUser(4, 2, "temple_scrolls", 120, 120, "Scroll")

        $ temple_lever_sprite1 = MapUser(7, 2, "temple_lever_left", 120, 120, "Reset Lever")
        $ temple_chair_sprite1 = MapUser(7, 3, "temple_chair", 120, 120, "Chair")
        $ temple_lever_sprite2 = MapUser(1, 12, "temple_lever_left", 120, 120, "Door Lever")
        $ temple_lever_sprite3 = MapUser(3, 12, ghostlyFilter("temple_lever_left"), 120, 120, "Invisible Lever")
        $ temple_stair_sprite2 = MapUser(9, 7, "temple_stair_front", 120, 120, "Background Stair")
        $ temple_stair_sprite3 = MapUser(9, 6, "temple_stair_front", 120, 120, "Background Stair")
        $ temple_stair_sprite4 = MapUser(8, 7, "temple_stair_front", 120, 120, "Background Stair")
        $ temple_stair_sprite5 = MapUser(8, 6, "temple_stair_front", 120, 120, "Background Stair")
        $ temple_spriteling_sprite1 = MapLooker(6, 13, "bandit_sprite", 120, 120, "Invisible Spriteling", [["Right", 4],[ "Down", 2], ["Left", 4], ["Up", 2]], 2, "temple_spriteling")
        $ addSprite(temple_scriptorium, temple_spriteling_sprite1)
        $ temple_scriptorium.autoMoveLookers()
        $ addSprite(temple_scriptorium, temple_chair_sprite1)
        $ addSprite(temple_scriptorium, temple_lever_sprite1)
        $ addSprite(temple_scriptorium, temple_lever_sprite2)
        $ addFront(temple_scriptorium, temple_lever_sprite3)
        $ addBack(temple_scriptorium, temple_stair_sprite2)
        $ addBack(temple_scriptorium, temple_stair_sprite3)
        $ addBack(temple_scriptorium, temple_stair_sprite4)
        $ addBack(temple_scriptorium, temple_stair_sprite5)
        $ addSprite(temple_scriptorium, temple_stair_sprite1)
        $ addSprite(temple_scriptorium, temple_table1_sprite1)
        $ addSprite(temple_scriptorium, temple_table2_sprite1)
        $ addSprite(temple_scriptorium, temple_table1_sprite2)
        $ addSprite(temple_scriptorium, temple_table2_sprite2)
        $ addSprite(temple_scriptorium, temple_scrolls_sprite1)
        $ addSprite(temple_scriptorium, temple_scriptorium.playerSprite)




        if temple_scriptorium.getMapStatus(0):
            $ temple_gate_sprite1 = MapUser(4, 13, "temple_gate_open", 120, 120, "Ghost Gate")
            $ temple_gate_sprite2 = MapUser(5, 13, "temple_gate_open", 120, 120, "Ghost Gate")
            $ addBack(temple_scriptorium, temple_gate_sprite1)
            $ addBack(temple_scriptorium, temple_gate_sprite2)
            $ temple_lever_sprite3.img = ghostlyFilter("temple_lever_right")
        else:
            $ temple_gate_sprite1 = MapUser(4, 13, "temple_gate_closed", 120, 120, "Ghost Gate")
            $ temple_gate_sprite2 = MapUser(5, 13, "temple_gate_closed", 120, 120, "Ghost Gate")
            $ addFront(temple_scriptorium, temple_gate_sprite1)
            $ addFront(temple_scriptorium, temple_gate_sprite2)

        if temple_scriptorium.getMapStatus(1):
            $ temple_door_sprite1 = MapUser(2, 10, "temple_door_front_open", 120, 130, "Door")
            $ addBack(temple_scriptorium, temple_door_sprite1)
            $ temple_lever_sprite2.img = "temple_lever_right"
        else:
            $ temple_door_sprite1 = MapUser(2, 10, "temple_door_front_closed", 120, 130, "Door")
            $ addSprite(temple_scriptorium, temple_door_sprite1)

        if temple_scriptorium.getMapStatus(2) and temple_scriptorium.getMapStatus(3):
            $ temple_door_sprite2 = MapUser(8, 11, "temple_door_front_open", 120, 130, "Door")
            $ addBack(temple_scriptorium, temple_door_sprite2)
        else:

            $ temple_door_sprite2 = MapUser(8, 11, "temple_door_front_closed", 120, 130, "Door")
            $ addSprite(temple_scriptorium, temple_door_sprite2)

        if temple_scriptorium.getMapStatus(2):
            if temple_scriptorium.getMapStatus(3):
                $ temple_crater_sprite2 = MapUser(2, 8, "temple_crater_filled", 120, 120, "Crater")
                $ addSprite(temple_scriptorium, temple_crater_sprite2)
            else:
                $ temple_crater_sprite2 = MapUser(2, 8, "temple_crater_empty", 120, 120, "Crater")
                $ addBack(temple_scriptorium, temple_crater_sprite2)
                $ temple_boulder_sprite2 = MapStorer(4, 4, "temple_boulder", 120, 120, "Ball Boulder", "temple_boulder")
                $ addSprite(temple_scriptorium, temple_boulder_sprite2)
            $ temple_crater_sprite1 = MapUser(9, 9, "temple_crater_filled", 120, 120, "Crater")
            $ addSprite(temple_scriptorium, temple_crater_sprite1)
        else:

            $ temple_crater_sprite1 = MapUser(9, 9, "temple_crater_empty", 120, 120, "Crater")
            $ temple_crater_sprite2 = MapUser(2, 8, "temple_crater_empty", 120, 120, "Crater")
            $ addBack(temple_scriptorium, temple_crater_sprite1)
            $ addBack(temple_scriptorium, temple_crater_sprite2)
            $ temple_boulder_sprite1 = MapStorer(2, 3, "temple_boulder", 120, 120, "Ball Boulder", "temple_boulder")
            $ temple_boulder_sprite2 = MapStorer(4, 4, "temple_boulder", 120, 120, "Ball Boulder", "temple_boulder")
            $ addSprite(temple_scriptorium, temple_boulder_sprite1)
            $ addSprite(temple_scriptorium, temple_boulder_sprite2)


    if temple_of_tapjoo == temple_undercroft:
        $ temple_stair_sprite1 = MapUser(4, 0, "temple_stair_front", 120, 120, "Undercroft To Sanctum")

        $ addSprite(temple_undercroft, temple_stair_sprite1)
        $ addSprite(temple_undercroft, temple_undercroft.playerSprite)

    if temple_of_tapjoo == temple_sanctum:
        $ temple_stair_sprite1 = MapUser(0, 7, "temple_stair_side", 120, 120, "Sanctum To Hall")
        $ temple_stair_sprite2 = MapUser(14, 14, "temple_stair_front", 120, 120, "To Undercroft")

        $ temple_cullion1 = MapUser(2, 13, "temple_cullion1", 120, 120, "Cullion1")
        $ temple_cullion2 = MapUser(4, 12, "temple_cullion2", 120, 120, "Cullion2")
        $ temple_stallion1 = MapUser(3, 8, "temple_stallion1", 120, 120, "Stallion")
        $ temple_stallion2 = MapUser(3, 9, "temple_stallion2", 120, 120, "Stallion")
        $ temple_broken_wall2 = MapUser(4, 6, "temple_wall2_broken_right", 120, 120, "Broken Wall")
        $ temple_broken_wall4 = MapUser(8, 14, "temple_wall2_broken_right", 120, 120, "Broken Wall")
        $ temple_broken_wall3 = MapUser(1, 6, "temple_wall2_broken_left", 120, 120, "Broken Wall")
        $ temple_broken_wall1 = MapUser(2, 6, "temple_wall2_debris", 120, 120, "Broken Wall")

        $ temple_lever_sprite1 = MapUser(3, 2, "temple_lever_left", 120, 120, "Reset Lever")
        $ temple_lever_sprite2 = MapUser(13, 4, "temple_lever_left", 120, 120, "Door Lever")
        $ temple_lever_sprite3 = MapUser(15, 4, ghostlyFilter("temple_lever_left"), 120, 120, "Invisible Lever")

        $ temple_stair_sprite3 = MapUser(14, 0, "temple_stair_front", 120, 120, "To Grand Chamber")
        $ addBack(temple_sanctum, temple_broken_wall1)
        $ addSprite(temple_sanctum, temple_broken_wall2)
        $ addSprite(temple_sanctum, temple_broken_wall3)
        $ addSprite(temple_sanctum, temple_broken_wall4)
        $ addSprite(temple_sanctum, temple_stallion1)
        $ addSprite(temple_sanctum, temple_stallion2)
        $ addSprite(temple_sanctum, temple_cullion1)
        $ addSprite(temple_sanctum, temple_lever_sprite1)
        $ addSprite(temple_sanctum, temple_lever_sprite2)
        $ addFront(temple_sanctum, temple_lever_sprite3)
        $ addSprite(temple_sanctum, temple_cullion2)
        $ addBack(temple_sanctum, temple_stair_sprite1)
        $ addSprite(temple_sanctum, temple_stair_sprite2)
        $ addSprite(temple_sanctum, temple_stair_sprite3)
        $ addSprite(temple_sanctum, temple_sanctum.playerSprite)

        if not temple_hall.getMapStatus(2):
            $ temple_boulder_sprite1 = MapStorer(2, 11, "temple_boulder", 120, 120, "Ball Boulder", "temple_boulder")
            $ addSprite(temple_sanctum, temple_boulder_sprite1)
        if not temple_hall.getMapStatus(3):
            $ temple_boulder_sprite2 = MapStorer(3, 12, "temple_boulder", 120, 120, "Ball Boulder", "temple_boulder")
            $ addSprite(temple_sanctum, temple_boulder_sprite2)
        if temple_sanctum.getMapStatus(1):
            $ temple_gate_sprite1 = MapUser(10, 7, "temple_gate_open", 120, 120, "Ghost Gate")
            $ temple_lever_sprite2.img = "temple_lever_right"
            $ addBack(temple_sanctum, temple_gate_sprite1)
        else:

            $ temple_gate_sprite1 = MapUser(10, 7, "temple_gate_closed", 120, 120, "Ghost Gate")

            $ addFront(temple_sanctum, temple_gate_sprite1)
        if temple_sanctum.getMapStatus(2):
            $ temple_door_sprite1 = MapUser(14, 3, "temple_door_front_open", 120, 120, "Door")
            $ addBack(temple_sanctum, temple_door_sprite1)
            $ temple_lever_sprite3.img = ghostlyFilter("temple_lever_right")
        else:

            $ temple_door_sprite1 = MapUser(14, 3, "temple_door_front_closed", 120, 120, "Door")
            $ addSprite(temple_sanctum, temple_door_sprite1)
        if not temple_sanctum.getMapStatus(3):
            $ temple_guardian_sprite1 = MapUser(14, 1, "temple_guardian_sprite", 150, 150, "Guardian")
            $ addSprite(temple_sanctum, temple_guardian_sprite1)


    $ temple_of_tapjoo.updateFloor(temple_of_tapjoo_floor)
    $ current_location = temple_of_tapjoo
    $ temple_of_tapjoo.entranceCount += 1
    jump Temple_of_Tapjoo_Loop

label Temple_of_Tapjoo_Loop:

    $ renpy.music.play(mOpen1, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ disableC = False
    $ sprite = temple_of_tapjoo.playerSprite
    call screen dungeon_map(temple_of_tapjoo)

    show screen dungeon_map(temple_of_tapjoo)
    if isinstance(_return, tuple) and not disableC:
        $ tenki_moving = False
        if len(_return) == 4:

            if temple_of_tapjoo.mappy[_return[1]][_return[0]].back != None and temple_of_tapjoo.mappy[_return[1]][_return[0]].back.img == "temple_crater_empty":
                pause 0.05
                $ removeSprite(temple_of_tapjoo, temple_of_tapjoo.mappy[_return[1]][_return[0]].user)
                $ temple_of_tapjoo.mappy[_return[1]][_return[0]].back.img = "temple_crater_filled"
                $ filled_crater = temple_of_tapjoo.mappy[_return[1]][_return[0]].back
                $ removeBack(temple_of_tapjoo, temple_of_tapjoo.mappy[_return[1]][_return[0]].back)
                $ addSprite(temple_of_tapjoo, filled_crater)
                pause 0.5 
                if _return[0] == 9 and _return[1] == 9:
                    $ temple_scriptorium.playerSprite.interaction[2] = True
                    $ temple_totem_horn.status = temple_room_id(temple_of_tapjoo)
                    $ temple_totem_horn.x = 2
                    $ temple_totem_horn.y = 8
                    $ addSprite(temple_of_tapjoo, temple_totem_horn)
                    $ addBack(temple_of_tapjoo, temple_crater_sprite2)
                if _return[0] == 2 and _return[1] == 8:
                    $ temple_scriptorium.playerSprite.interaction[3] = True
                    $ removeSprite(temple_of_tapjoo, temple_door_sprite2)
                    $ addBack(temple_of_tapjoo, temple_door_sprite2)
                    $ temple_door_sprite2.img = "temple_door_front_open"
            elif temple_of_tapjoo == temple_sanctum:
                if temple_of_tapjoo.mappy[_return[1]][_return[0]].back != None and temple_of_tapjoo.mappy[_return[1]][_return[0]].back.img == "temple_stair_side":
                    $ removeSprite(temple_of_tapjoo, temple_of_tapjoo.mappy[_return[1]][_return[0]].user)
                    if temple_hall.getMapStatus(2):
                        $ temple_hall.playerSprite.interaction[3] = True
                    else:
                        $ temple_hall.playerSprite.interaction[2] = True
                    $ temple_sanctum.playerSprite.interaction[0] = True
                elif isinstance(temple_of_tapjoo.mappy[_return[1]-1][_return[0]].user, MapUser) and temple_of_tapjoo.mappy[_return[1]-1][_return[0]].user.interaction == "Furkan":
                    f "Aghhh!"
                    "Your hear a loud scream coming from above, it seems like that ball has caught Furkan by surprise."
                    r "I told you to stand aside while [e] is working his magic. Why won't you listen to me?"
                    f "My apologies. I was almost rolled over by that boulder."
                    "Rahim shakes his head as you awkwardly watch Furkan dust himself off."
                    $ temple_furkan_sprite.status["Got Rolled"] = True
                    $ temple_furkan_sprite.moveToTile(temple_of_tapjoo, temple_furkan_sprite.x + 2, temple_furkan_sprite.y - 2)
                else:
                    $ temple_of_tapjoo.pushBall(_return[0], _return[1], _return[2], _return[3])
            elif temple_of_tapjoo == temple_hall:
                if temple_hall.mappy[11][4].user != None and temple_hall.mappy[11][4].user != temple_hall.playerSprite and (temple_hall.mappy[11][4].user.interaction[:5] == "Totem" or temple_hall.mappy[11][4].user.interaction[:5] == "Dummy" or temple_hall.mappy[11][4].user.interaction[:4] == "Ball"):
                    if temple_hall.mappy[11][6].user != None and temple_hall.mappy[11][6].user != temple_hall.playerSprite and (temple_hall.mappy[11][6].user.interaction[:5] == "Totem" or temple_hall.mappy[11][6].user.interaction[:5] == "Dummy" or temple_hall.mappy[11][6].user.interaction[:4] == "Ball"):
                        if temple_hall.getUserInteraction(4, 11, "Ball", -4):
                            $ temple_hall.playerSprite.interaction[4] = True
                        else:
                            $ temple_hall.playerSprite.interaction[4] = False
                        if temple_hall.getUserInteraction(6, 11, "Ball", -4):
                            $ temple_hall.playerSprite.interaction[5] = True
                        else:
                            $ temple_hall.playerSprite.interaction[5] = False
                        $ removeSprite(temple_of_tapjoo, temple_door_sprite2)
                        $ addBack(temple_of_tapjoo, temple_door_sprite2)
                        $ temple_door_sprite2.img = "temple_door_side_open"
                    else:
                        if temple_hall.getUserInteraction(4, 11, "Ball", -4):
                            $ temple_hall.playerSprite.interaction[4] = True
                        else:
                            $ temple_hall.playerSprite.interaction[4] = False
                        if temple_hall.getUserInteraction(6, 11, "Ball", -4):
                            $ temple_hall.playerSprite.interaction[5] = True
                        else:
                            $ temple_hall.playerSprite.interaction[5] = False
                        $ removeBack(temple_of_tapjoo, temple_door_sprite2)
                        $ addSprite(temple_of_tapjoo, temple_door_sprite2)
                        $ temple_door_sprite2.img = "temple_door_side_closed"
                        $ temple_of_tapjoo.pushBall(_return[0], _return[1], _return[2], _return[3])
                elif temple_of_tapjoo.mappy[_return[1]][_return[0]].back != None and temple_of_tapjoo.mappy[_return[1]][_return[0]].back.img == "temple_stair_side":
                    $ removeSprite(temple_of_tapjoo, temple_of_tapjoo.mappy[_return[1]][_return[0]].user)
                    if temple_hall.getMapStatus(3):
                        $ temple_hall.playerSprite.interaction[3] = False
                    else:
                        $ temple_hall.playerSprite.interaction[2] = False
                else:
                    if temple_hall.getUserInteraction(4, 11, "Ball", -4):
                        $ temple_hall.playerSprite.interaction[4] = True
                    else:
                        $ temple_hall.playerSprite.interaction[4] = False
                    if temple_hall.getUserInteraction(6, 11, "Ball", -4):
                        $ temple_hall.playerSprite.interaction[5] = True
                    else:
                        $ temple_hall.playerSprite.interaction[5] = False
                    $ removeBack(temple_of_tapjoo, temple_door_sprite2)
                    $ addSprite(temple_of_tapjoo, temple_door_sprite2)
                    $ temple_door_sprite2.img = "temple_door_side_closed"

                    $ temple_of_tapjoo.pushBall(_return[0], _return[1], _return[2], _return[3])
            else:


                $ temple_of_tapjoo.pushBall(_return[0], _return[1], _return[2], _return[3])
        elif len(_return) == 2:
            $ dungeon_timers.pop(0)
            $ temple_of_tapjoo.autoMoveLookers()
    else:
        $ disableC = True
    if _return == "Dummy":
        "Looks like a poor imitation of the other totems, the blue markings are dully faded, almost as if they were painted on."
        "But you presume there are still some use for it."

    if _return == "Pillar" or _return == "Take Pillar":
        $ pillar_pattern = ["temple_pillar_buck", "temple_pillar_ram", "temple_pillar_hart", "temple_pillar_bull"]
        $ temple_pillar = temple_hall.locateSpriteInFront(sprite)
        if isinstance(temple_pillar, MapStorer):
            $ temple_pillar.status += 1
            $ temple_pillar.status %= 4
            $ temple_pillar.img = pillar_pattern[temple_pillar.status]
            if temple_pillar_sprite1.status == 1 and temple_pillar_sprite2.status == 0 and temple_pillar_sprite3.status == 2:
                $ removeSprite(temple_of_tapjoo, temple_door_sprite1)
                $ addBack(temple_of_tapjoo, temple_door_sprite1)
                $ temple_hall.playerSprite.interaction[0] = True
                $ temple_door_sprite1.img = "temple_door_front_open"
                "A loud thump can be heard as the stone door behind you slowly creaks open."
                pause 0.5
                if vote_result < 0:
                    s "Oh, I see. You are trying to open the door with the pillars."
                    e "Seb, I've already opened the door."
                    s "Did you? Oh! You're the best, roomie, let's see what's in this room."
                    $ temple_sebas_sprite.status["Location"] = "scriptorium"
                    $ temple_sebas_sprite.x = 1
                    $ temple_sebas_sprite.y = 2
                    $ temple_sebas_sprite.img = Transform("temple_sebas_sprite", xzoom = -1)
                else:
                    f "I certainly did not expect you to figure it out so soon, well done, [e]."
                    "Furkan smiles as he explores past the door."
                    f "Hmm... another locked door. We need some more totems here."
                    pause 0.5
                    f "I will explore the next chamber, Rahim."
                    r "Go, go. Take [e] with you."
                    $ temple_furkan_sprite.status["Location"] = "scriptorium"
                    $ temple_furkan_sprite.x = 1
                    $ temple_furkan_sprite.y = 2
                    $ temple_furkan_sprite.img = Transform("temple_furkan_sprite", xzoom = -1)

    if _return == "Invisible Spriteling" or enct == "Invisible Spriteling":
        $ disableC = True
        $ enct = None
        "A ghostly spectral force seems to be blocking your path. You can feel its presence emanating around your body."
        hide screen dungeon_map
        jump spriteling_battle

    if _return == "Take Mural":
        $ x, y = getFacingTile(sprite)
        $ temple_of_tapjoo.inventory = temple_of_tapjoo.getSprite(x, y)
        $ temple_of_tapjoo.getSprite(x, y).h += 30

    if _return == "Drop Mural":
        $ x, y = getFacingTile(sprite)
        if x >= 2 and x <= 8 and y == 8:
            $ removeSprite(temple_of_tapjoo, temple_of_tapjoo.inventory)
            $ temple_of_tapjoo.moveTo(x, y, temple_of_tapjoo.inventory.x - x, 0)
            $ temple_of_tapjoo.inventory.h -= 30
            $ temple_of_tapjoo.inventory.x = x
            $ temple_of_tapjoo.occupy(x, y, temple_of_tapjoo.inventory)
            $ temple_of_tapjoo.inventory = None
            if temple_mural_sprite1.x == 2 and temple_mural_sprite2.x == 3 and temple_mural_sprite3.x == 4 and temple_mural_sprite4.x == 5 and temple_mural_sprite5.x == 6 and temple_mural_sprite6.x == 7 and temple_mural_sprite7.x == 8:
                if temple_totem_moss.status == None:
                    $ temple_totem_moss.status = "entrance"
                    $ addSprite(temple_of_tapjoo, temple_totem_moss)

                    "When you put down the last piece. A loud thump can be heard in front of you."
                    "The next thing you hear was Rahim's growl, its echo reverberating through the chamber, as if he was hit by a sudden force."
                    e "What was that?"
                    if vote_result < 0:
                        s "I don't know, Rahim practicing his daily whiny routine?"
                    else:
                        "You turn around to see Furkan clutching at his horns, his eyes wide with shock."
                        f "Something is messing with my head... [e], I am fine, but please go see if Rahim need anything."

    if _return == "Guardian":

        "The golem stands alone in the corridor, it seems to be guarding the door in front of you."
        $ temple_rahim_sprite.moveToTile(temple_of_tapjoo, 13, 6)
        if vote_result < 0:
            $ temple_sebas_sprite.moveToTile(temple_of_tapjoo, 14, 5)
            s "Oh man, [e]. I still haven't done looking around these chambers, you're really good at thi-"
            $ temple_door_sprite1.img = "temple_door_front_closed"
            "Sebas's voice is cut off as the door shuts in front of his face."
            s "Uh... What's going on?"
            s "[e]?"
            "You look at the golem, there is no way for you to escape if you anger it somehow."
            r "What's going on? Why can't you open it?"
            s "Why can't You open it? I don't think it's working, Rahim."
            e "Look, there is a guardian in front of me. I think it was a trap."
            s "A guardian? We have to help him right now, Rahim."
            r "I am pushing the door, stop screaming."
            s "Roomie, you can beat the guardian, okay. I've seen you do it before."
            "Sebas shouts from the other side of the door."
            e "Okay..."
            "You can feel the tension in the air as the golem's head seem to track your every movement."
        else:
            $ temple_furkan_sprite.moveToTile(temple_of_tapjoo, 14, 5)
            f "We finally caught up to you, [e]. I have to say, you were brisking through the chambers like a bree-"
            $ temple_door_sprite1.img = "temple_door_front_closed"
            "Furkan's voice is cut off as the door shuts in front of his face."
            f "I... I cannot open it. The door is sealed shut. Are you well, [e]?"
            e "Yeah, I am, for now I guess."
            "You look at the golem, there is no way for you to escape if you anger it somehow."
            r "What's going on? Why can't you open it?"
            f "I have no idea, the lever is stuck, and the totems do not even work."
            e "Look, there is a guardian in front of me. I think it was a trap."
            f "A guardian? We have to help him right now, Rahim."
            r "I thought you had control of the guardians."
            "Rahim's voice is low, almost a whisper."
            f "They had not been ours ever since the primordial runes were stolen. We only had two guardians, we kept them in our tribe until they broke out of their chains."
            f "As a matter of fact, [e] slain both of them eventually."
            r "Then what is this one doing here?"
            f "It was me. We had the basin to create new guardians, but they had stolen the basin from me."
            "You can feel the tension in the air as the golem's head seem to track your every movement."
            e "Do I have to kill it, he's blocking the way and I have no way out."
            f "I believe in you, [e]. Do whatever you must."
            r "You can't just let [e] kill the guardian by himself. Be useful for once."
            "Rahim tries to push open the door, you can see a faint glow between the door but he quickly runs out of energy."
            r "...What?"
            "Rahim shouts in exasperation, but Furkan says nothing in return."
        r "Scream out if you need help, [e]. We'll be right here."
        e "Okay, I'll try."
        "You take a deep breath and prepare yourself for the worst."
        hide screen dungeon_map 
        jump runeguardian_battle


    if _return[:10] == "Take Totem" or _return[:10] == "Take Dummy":
        $ x, y = getFacingTile(sprite)
        if temple_of_tapjoo == temple_entrance:
            if x == 5 and y == 14:
                $ removeBack(temple_of_tapjoo, temple_door_sprite1)
                $ addSprite(temple_of_tapjoo, temple_door_sprite1)
                $ temple_door_sprite1.img = "temple_door_front_closed"
            if x == 5 and y == 3 and not temple_rahim_sprite.status.get("Dialogue", False):
                $ temple_rahim_sprite.status["Dialogue"] = 1
                with flash
                "As you lift up the totem, a hazy bleam washes over your entire body. You feel a sudden chill, as if the air around you has been sucked dry."
                "Rahim stares at you in disbelief. The totem in your hand seems to be the cause of his sudden discomfort. Instinctively, you put down the totem."
                r "You alright?"
                e "I'm fine, just a little cold."
                r "You disappeared for a moment there. I thought you were going to vanish."
                e "Did I? I didn't feel anything."
                r "Pick it up again."
                $ temple_of_tapjoo.takeItem(sprite, temple_of_tapjoo.locateSpriteInFront(sprite))
                "You hesitantly pick up the totem again. The same glow washes over you, but this time Rahim seems to be more certain of his theory."
                r "Must be the totem, it's turning you invisible... Go see if you can do something about it."
                e "You can't see me?"
                r "No, but I can feel you, somewhat. You're still here, just... invisible."
                e "I'll see what I can do."
                r "And... don't even try to scare me, or do anything weird around me. I'll bite your arm off."
                "You gulp nervously. His eyes seem to track at your general direction, but you can tell he can't find your exact direction."
        if temple_of_tapjoo == temple_hall and y == 11:
            if x == 4 or x == 6:
                $ removeBack(temple_of_tapjoo, temple_door_sprite2)
                $ addSprite(temple_of_tapjoo, temple_door_sprite2)
                $ temple_door_sprite2.img = "temple_door_side_closed"
        $ temple_of_tapjoo.takeItem(sprite, temple_of_tapjoo.locateSpriteInFront(sprite))

    if _return[:10] == "Drop Totem" or _return[:10] == "Drop Dummy":

        $ x, y = getFacingTile(sprite)
        if temple_of_tapjoo.isEmpty(x, y):
            $ temple_of_tapjoo.occupy(x, y, temple_of_tapjoo.inventory)
            $ temple_of_tapjoo.inventory.x = x
            $ temple_of_tapjoo.inventory.y = y
            $ temple_of_tapjoo.inventory.status = temple_room_id(temple_of_tapjoo)
            $ temple_of_tapjoo.inventory = None
        else:

            "You can't drop the totem here."

        if temple_of_tapjoo == temple_entrance:
            if temple_entrance.mappy[14][5].user != None and temple_entrance.mappy[14][5].user != sprite and (temple_entrance.mappy[14][5].user.interaction[:5] == "Totem" or temple_entrance.mappy[14][5].user.interaction[:5] == "Dummy"):
                if temple_entrance.playerSprite.interaction != "Opened":
                    $ temple_entrance.playerSprite.interaction = "Opened"
                    $ removeFront(temple_of_tapjoo, temple_gate_sprite1)
                    $ addBack(temple_of_tapjoo, temple_gate_sprite1)
                    $ temple_gate_sprite1.img = "temple_gate_open"
                    $ temple_rahim_sprite.status["Location"] = "hall"
                    $ temple_rahim_sprite.x = 8
                    $ temple_rahim_sprite.y = 6
                    $ temple_rahim_sprite.img = Transform("temple_rahim_sprite", xzoom = -1)
                    if vote_result < 0:
                        $ temple_sebas_sprite.status["Location"] = "hall"
                        $ temple_sebas_sprite.x = 3
                        $ temple_sebas_sprite.y = 7
                        $ temple_sebas_sprite.img = Transform("temple_sebas_sprite", xzoom = -1)
                    else:
                        $ temple_furkan_sprite.status["Location"] = "hall"
                        $ temple_furkan_sprite.x = 3
                        $ temple_furkan_sprite.y = 7
                        $ temple_furkan_sprite.img = Transform("temple_furkan_sprite", xzoom = -1)
                $ removeSprite(temple_of_tapjoo, temple_door_sprite1)
                $ addBack(temple_of_tapjoo, temple_door_sprite1)
                $ temple_door_sprite1.img = "temple_door_front_open"
        elif temple_of_tapjoo == temple_hall:
            if temple_hall.mappy[11][4].user != None and temple_hall.mappy[11][4].user != sprite and (temple_hall.mappy[11][4].user.interaction[:5] == "Totem" or temple_hall.mappy[11][4].user.interaction[:5] == "Dummy" or temple_hall.mappy[11][4].user.interaction[:4] == "Ball"):
                if temple_hall.mappy[11][6].user != None and temple_hall.mappy[11][6].user != sprite and (temple_hall.mappy[11][6].user.interaction[:5] == "Totem" or temple_hall.mappy[11][6].user.interaction[:5] == "Dummy" or temple_hall.mappy[11][6].user.interaction[:4] == "Ball"):
                    if not temple_hall.playerSprite.interaction.get(1, False):
                        $ temple_hall.playerSprite.interaction[1] = True
                        $ temple_rahim_sprite.status["Location"] = "sanctum"
                        $ temple_rahim_sprite.x = 4
                        $ temple_rahim_sprite.y = 5
                        $ temple_rahim_sprite.img = "temple_rahim_sprite"
                        if vote_result < 0:
                            $ temple_sebas_sprite.status["Location"] = "sanctum"
                            $ temple_sebas_sprite.x = 7
                            $ temple_sebas_sprite.y = 2
                            $ temple_sebas_sprite.img = Transform("temple_sebas_sprite", xzoom = -1)
                        else:
                            $ temple_furkan_sprite.status["Location"] = "sanctum"
                            $ temple_furkan_sprite.x = 2
                            $ temple_furkan_sprite.y = 4
                            $ temple_furkan_sprite.img = Transform("temple_furkan_sprite", xzoom = -1)
                    $ removeSprite(temple_of_tapjoo, temple_door_sprite2)
                    $ addBack(temple_of_tapjoo, temple_door_sprite2)
                    $ temple_door_sprite2.img = "temple_door_side_open"

    if _return == "Reset Lever":
        if temple_of_tapjoo == temple_scriptorium:
            if temple_scriptorium.mappy[3][2].user != None or temple_scriptorium.mappy[4][4].user != None:
                "It seems that the lever is supposed to reset the boulder, but something is blocking the way."
            else:
                if temple_crater_sprite1.img != "temple_crater_filled":
                    $ removeSprite(temple_of_tapjoo, temple_boulder_sprite1)
                    $ temple_boulder_sprite1.x = 2
                    $ temple_boulder_sprite1.y = 3
                    $ addSprite(temple_of_tapjoo, temple_boulder_sprite1)
                if temple_crater_sprite2.img != "temple_crater_filled":
                    $ removeSprite(temple_of_tapjoo, temple_boulder_sprite2)
                    $ temple_boulder_sprite2.x = 4
                    $ temple_boulder_sprite2.y = 4
                    $ addSprite(temple_of_tapjoo, temple_boulder_sprite2)
                $ temple_lever_sprite1.img = "temple_lever_right"
                pause 0.4
                $ temple_lever_sprite1.img = "temple_lever_left"
        else:
            if temple_sanctum.mappy[3][2].user != None or temple_sanctum.mappy[4][4].user != None:
                "It seems that the lever is supposed to reset the boulder, but something is blocking the way."
            if not temple_hall.getMapStatus(2):
                $ removeSprite(temple_of_tapjoo, temple_boulder_sprite1)
                $ temple_boulder_sprite1.x = 2
                $ temple_boulder_sprite1.y = 11
                $ addSprite(temple_of_tapjoo, temple_boulder_sprite1)
            if not temple_hall.getMapStatus(3):
                $ removeSprite(temple_of_tapjoo, temple_boulder_sprite2)
                $ temple_boulder_sprite2.x = 3
                $ temple_boulder_sprite2.y = 12
                $ addSprite(temple_of_tapjoo, temple_boulder_sprite2)

    if _return == "Door Lever":
        if temple_of_tapjoo == temple_scriptorium:
            $ removeSprite(temple_of_tapjoo, temple_door_sprite1)
            $ addBack(temple_of_tapjoo, temple_door_sprite1)
            $ temple_door_sprite1.img = "temple_door_front_open"
            $ temple_scriptorium.playerSprite.interaction[1] = True
            $ temple_lever_sprite2.img = "temple_lever_right"
        else:
            $ removeFront(temple_of_tapjoo, temple_gate_sprite1)
            $ addBack(temple_of_tapjoo, temple_gate_sprite1)

            $ temple_gate_sprite1.img = "temple_gate_open"
            $ temple_sanctum.playerSprite.interaction[1] = True
            $ temple_lever_sprite2.img = "temple_lever_right"

            if temple_totem_dummy2.status == None:
                $ temple_totem_dummy2.status = temple_room_id(temple_of_tapjoo)
                $ temple_totem_dummy2.x = 15
                $ temple_totem_dummy2.y = 6
                $ addSprite(temple_of_tapjoo, temple_totem_dummy2)

    if _return == "Invisible Lever":
        if temple_of_tapjoo == temple_scriptorium:
            if temple_totem_dummy1.status == None:
                $ removeFront(temple_of_tapjoo, temple_gate_sprite1)
                $ addBack(temple_of_tapjoo, temple_gate_sprite1)
                $ temple_gate_sprite1.img = "temple_gate_open"
                $ removeFront(temple_of_tapjoo, temple_gate_sprite2)
                $ addBack(temple_of_tapjoo, temple_gate_sprite2)
                $ temple_gate_sprite2.img = "temple_gate_open"
                $ temple_lever_sprite3.img = ghostlyFilter("temple_lever_right")
                $ temple_scriptorium.playerSprite.interaction[0] = True
                $ temple_totem_dummy1.status = temple_room_id(temple_of_tapjoo)
                $ temple_totem_dummy1.x = 2
                $ temple_totem_dummy1.y = 15
                $ addSprite(temple_of_tapjoo, temple_totem_dummy1)
        else:
            $ removeSprite(temple_of_tapjoo, temple_door_sprite1)
            $ addBack(temple_of_tapjoo, temple_door_sprite1)
            $ temple_door_sprite1.img = "temple_door_front_open"
            $ temple_sanctum.playerSprite.interaction[2] = True
            $ temple_lever_sprite3.img = ghostlyFilter("temple_lever_right")

    if _return[4:] == "Gate":
        "A metal gate cage that blocks the way. It seems to be locked, but you can't see any keyhole or any other way to open it."
        "The thin bars suggest that something slimmer perhaps can pass through the cage."

    if _return == "To Entrance":

        $ temple_entrance.start_x = 5
        $ temple_entrance.start_y = 1
        $ temple_of_tapjoo.passInventory(temple_entrance)
        $ temple_of_tapjoo = temple_entrance
        jump Temple_of_Tapjoo

    if _return == "Entrance To Hall":

        $ temple_hall.start_x = 5
        $ temple_hall.start_y = 1
        $ temple_of_tapjoo.passInventory(temple_hall)
        $ temple_of_tapjoo = temple_hall

        jump Temple_of_Tapjoo

    if _return == "Sanctum To Hall":

        $ temple_hall.start_x = 9
        $ temple_hall.start_y = 11
        $ temple_of_tapjoo.passInventory(temple_hall)
        $ temple_of_tapjoo = temple_hall
        jump Temple_of_Tapjoo

    if _return == "Scriptorium To Hall":

        $ temple_hall.start_x = 5
        $ temple_hall.start_y = 13
        $ temple_of_tapjoo.passInventory(temple_hall)
        $ temple_of_tapjoo = temple_hall
        jump Temple_of_Tapjoo

    if _return == "To Scriptorium":

        $ temple_scriptorium.start_x = 5
        $ temple_scriptorium.start_y = 1
        $ temple_of_tapjoo.passInventory(temple_scriptorium)
        $ temple_of_tapjoo = temple_scriptorium
        jump Temple_of_Tapjoo

    if _return == "To Longhouse":
        if temple_of_tapjoo.isEmpty(1, 2) and temple_of_tapjoo.isSpirit():
            $ temple_of_tapjoo.occupy(1, 2, temple_of_tapjoo.inventory)
            $ temple_of_tapjoo.inventory.x = 1
            $ temple_of_tapjoo.inventory.y = 2
        $ temple_of_tapjoo.inventory = None
        $ disableC = True
        hide screen dungeon_map
        jump main_lusterfield_mayors_longhouse

    if _return == "To Undercroft":

        msg "Work in Progress!"




    if _return == "Hall To Sanctum":

        $ temple_sanctum.start_x = 1
        $ temple_sanctum.start_y = 7
        $ temple_of_tapjoo.passInventory(temple_sanctum)
        $ temple_of_tapjoo = temple_sanctum
        jump Temple_of_Tapjoo

    if _return == "Undercroft To Sanctum":

        $ temple_sanctum.start_x = 18
        $ temple_sanctum.start_y = 13
        $ temple_of_tapjoo.passInventory(temple_sanctum)
        $ temple_of_tapjoo = temple_sanctum
        jump Temple_of_Tapjoo

    if _return == "Rahim":
        show rahim normal with dissolve
        "You walk up to the brown bull, who is standing near the stone wall."
        if temple_of_tapjoo.isSpirit():
            "Rahim looks at your direction with a curious expression, but he doesn't say anything."
            "It is rousing to look at his body and the way he stands, without having to worry about his fastidious gaze as you do so."
            "Though, he is looking increasingly annoyed at your presence, or lack thereof."
        elif temple_of_tapjoo == temple_entrance:
            if temple_entrance.playerSprite.interaction != "Opened":
                r "I still cannot believe this temple was built underneath our feet for so many years, it is a wonder that we have never found it before."
                e "What were we supposed to do again?"

                if temple_totem_moss.status == None:
                    r "Find your way into the grand chamber. I think we need to look for the totems first. That mural over there would be a good start."
                else:
                    r "This stone just fell from the ceiling. Think you can do something with it?"
                "You nod."
            else:
                r "The door's unlocked. We better get moving."
        elif temple_of_tapjoo == temple_hall:
            if not temple_hall.getMapStatus(0):
                r "Another door blocking our way, maybe these pillars have something to do with it."
            elif temple_room(temple_rahim_sprite.status["Location"]) == temple_hall:
                r "Two pressure plates here that only works with totems."
                r "You need to find more totems, [e]. Or, try to look for the first one you left behind."
                "You nod sheepishly."
            else:
                r "Door's opened. Let's go then."
        elif temple_of_tapjoo == temple_sanctum:
            e "Hey, Rahim. Do you think you can help me with the puzzle...?"
            if not temple_sanctum.getMapStatus(1):
                "The bull looks at you, his eyes narrowing at the boulder."
                r "Obviously, you need that totem that makes you invisible. Think you can roll that rock down in the hall?"
            elif not temple_sanctum.getMapStatus(2):
                r "I can see something glowing blue over the gate, maybe the other totem of yours can be useful."
        if checkNoShopItem("Old Mayors Journal"):
            menu:
                r "And here is the journal. Keep it safe."
                "Take the journal":
                    call Old_Mayors_Journal from _call_Old_Mayors_Journal
                "Leave":
                    pass
        hide rahim

    if _return == "Sebas":
        $ disableC = True
        hide screen dungeon_map 
        scene temple_of_tapjoo
        show sebas normal with dissolve
        if temple_of_tapjoo.isSpirit():
            "Sebas does not even notice your presence as a ghostly form, he just looks ahead."
            "You try to talk to him, but he doesn't seem to hear you."
        elif temple_of_tapjoo == temple_entrance:
            if temple_entrance.playerSprite.interaction != "Opened":
                if temple_totem_moss.status == None:
                    s "What's this mural about, you think?"
                    s "I can see the guardian there, a goat here... is that Tapjoo?"
                    e "Looks like it."
                    "Sebas looks at the mural, his eyes scanning the stone wall."
                    s "How about that one, a deer... or elk."
                    e "He seems familiar. Have I seen that one before?"
                else:
                    s "What's that noise behind the mural..."
            else:
                s "The door's unlocked. Come on, roomie, we gotta see what's the next room."
                "The lion smiles, pointing to the direction of the exit."
        elif temple_of_tapjoo == temple_hall:
            if not temple_hall.getMapStatus(0):
                s "Are those the goats... Now I wish Rahim'd invited Furkan here, because I have no idea what any of those mean."
                e "Yeah, me neither."
                s "Like, what is that one even doing there? There's not even hints in these damn puzzles. What were the builders thinking..."
                s "They drew very well, though. Like the mural over there."
            else:
                s "Go, go! We need to go down that chamber here."
        elif temple_of_tapjoo == temple_scriptorium:
            "Sebas looks at the tables in the scriptorium, his eyes scanning the papers."
            if not temple_scriptorium.getMapStatus(0):
                s "What are those about?"
                e "I don't know, but they look like some kind of ancient texts."
                s "I can see some symbols here, but I can't read them like the goats do."
                s "We should keep an eye on them though, someone else can probably translate those."
                menu:
                    "Ask about the puzzles":
                        e "Hey Sebas, think you can help with the stones lying around here?"
                        if not temple_scriptorium.getMapStatus(2):
                            "He turns around and look at the rounded boulders, furrowing his brows."
                            s "Just push the balls in the hole, right?"
                        elif not temple_scriptorium.getMapStatus(3):
                            "The lion points at the other hole. He scratches his head lightly."
                            s "How about that hole? Do you think you can fill that one?"
                            s "Just pull the lever if you mess something up."
                        elif not temple_scriptorium.getMapStatus(1):
                            pause 0.5
                            s "Uhmm, use some totems?"
                            e "What?"
                            s "I don't know, I'm getting stuck here, [e]."
                            e "Me too, Seb."
                        else:
                            s "Uhmm, totem?"
                    "Leave":
                        pass
            else:
                s "We should go down there. I think we need to find the other totem."
        elif temple_of_tapjoo == temple_sanctum:
            "The chamber is filled with the smell of incense and the sound of the wind. The lion stands near the stone wall."
            s "I'm just looking around... roomie. I don't think I'm solving these puzzles in the next ten years. I'm counting on you, [e]."
    if _return == "Furkan":
        $ disableC = True
        hide screen dungeon_map 
        scene temple_of_tapjoo
        show furkan normal with dissolve
        if temple_of_tapjoo.isSpirit():
            "You walk up to the white ram in your ghostly form, but he just looks ahead, not even registering your presence."
            "Despite your best efforts, he doesn't seem to notice you, at least you do not believe he's willfully trying to ignore you."
        elif temple_of_tapjoo == temple_entrance:
            if temple_entrance.playerSprite.interaction != "Opened":
                if temple_totem_moss.status == None:
                    f "Look at this mural, it is beautiful. Is this truly how Tapjoo looked like?"
                    e "He looks just like one of the goats."
                    "The goat chief stands in front of the stone mural, the brilliant colours of the mural reflecting off his fur."
                    f "So mesmerising. I cannot pull my eyes away from it."
                    e "It's nice... but, it looks like a mess, doesn't it?"
                    f "A beautiful mess indeed. But yes, the mural is ostensibly out of order. The maker must have intended it to be so."
                    "You furrow your brow, trying to make sense of Furkan's words. The ram's idle gaze looks as if he is lost in thought."
                else:
                    f "I think I heard something in the back. Did you find anything?"
            else:
                f "We should go, I... I would loathe staying here for one more second."
                "The ram's eyes fuzz with a hint of fear, his gaze darting around the mural as if he is expecting something to jump out at him."
        elif temple_of_tapjoo == temple_hall:
            if not temple_hall.getMapStatus(0):
                f "Do you see the pillars? They are all faces of our people, albeit more abstractly."
                e "They are not all goats, are they?"
                f "No, some are antlered, some are horned, they all belonged in our tribe."
                f "There is a pattern here, somewhere. Maybe we have missed something about these folks."
            else:
                f "We should explore the chamber down there. Rahim will stay to watch over this one."
        elif temple_of_tapjoo == temple_scriptorium:
            "The goat chief stands besides the tables in the scriptorium, skimming through the paper curiously."
            if not temple_scriptorium.getMapStatus(0):
                "You look at the ram, he places his hand on the pages, his eyes scanning the texts."
                menu:
                    "Furkan seems to be absorbed in the ancient texts and books, but you can still talk to him."
                    "Ask about the texts":
                        e "What are those about?"
                        f "Huh... I have not read these scripts before, but someone scratched out some of the texts."
                        e "Oh, really?"
                        "You try to look at the texts, only to be confused by the foreign symbols of ancient languages."
                        f "It reads, the flock is notably skilled with intelligence, but they are also notably susceptible to psychiatric influence."
                        f "Instinctively, the flock follows a bellwether, and the bellwether follows the shepherd, Tapjoo..."
                        f "Something... and... the horns of a Tapjoo's follower is where they may heed the echos of the bell-... I can't read the rest in these dim light."
                        "You look at Furkan, who seems to be lost in thought. His hand unwittingly brushes against the bell on his chest."
                        e "Furkan, what's a bellwether?"
                        f "The leading sheep of the flock... I thin-... Are we truly seeking our deity Tapjoo here?"
                        f "It seemed so impossible, we have not found any traces of him since... primordial times."
                        e "I don't know, but the mayor has written something about the shepherd, do you think the shepherd is Tapjoo?"
                        f "Who else can it be? He was the only one capable to build all of this. That mural at the entrance, it did something to me, I have been hearing the bell's chime since then."
                        "You look at the ram, his eyes are wide with shock."
                        f "Go, [e]. The sooner we find out about Tapjoo, the sooner we can leave this place."
                    "Ask about the puzzles":
                        e "Hey Furkan, think you can help with the stones lying around here?"
                        if not temple_scriptorium.getMapStatus(2):
                            "He turns around and look at the rounded boulders, furrowing his brows."
                            f "Try to push them around, maybe towards that hole over there."
                        elif not temple_scriptorium.getMapStatus(3):
                            "The brown ram points at the other hole. He scratches his head lightly."
                            f "You need to fill up the other hole as well. That totem might be useful here."
                            f "If you messed up you can always use the lever over there."
                            e "Oh! You are right, I should try that. You're really quick at figuring out these ones, Furkan."
                            f "We goats are the masters of puzzles, [e]. I have seen a lot of things."
                        elif not temple_scriptorium.getMapStatus(1):
                            pause 0.5
                            f "Another gate, I saw you pass through the gate so easily back at the entrance, correct?"
                            e "I did, but I don't have the totem with me..."
                            f "Maybe you should use that instead, then."
                            "Furkan smiles."
                        else:
                            f "There must be something you are not seeing."
                            f "Try using your totems, that might help."
                        "Quietly, Furkan returns to read the ancient texts and books."
                    "Leave":
                        pass
            else:
                f "We should go, now that we have three totems to spare."
        elif temple_of_tapjoo == temple_sanctum:
            if temple_furkan_sprite.status.get("Got Rolled", False):
                f "I do not mean to complain, but the boulder almost crushed me. I need to rest about."
            else:
                "The chamber is filled with the smell of incense and the sound of the wind. The white ram stands near the stone wall."
                f "This sanctum is damp, and eerie. I can feel something else in here. Especially when you walk with that totem..."
                f "But I took a look to the area down there, am I dreaming or did our ancestor design a weirdly phallic shape."



        hide furkan

    jump Temple_of_Tapjoo_Loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
