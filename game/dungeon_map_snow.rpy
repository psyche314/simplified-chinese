default snow_region_floor = {"snow_floor1": 10, "snow_floor2": 10, "snow_floor3": 5, "snow_floor4": 5, "snow_floor5": 2, "snow_floor6": 2, "snow_floor7": 1, "snow_floor8": 1}

default ice_cave_floor = {"cave_ice01": 10, "cave_ice02": 8, "cave_ice03": 7, "cave_ice04": 5, "cave_ice05": 3, "cave_ice06": 1, "cave_ice07": 1, "cave_ice08": 1}

default snow_region_map = {}
default ice_cave_map = {}

default snowbound_summit = MapPat()
default chilly_ice_cave = MapPat()
default conquerors_crypt = MapPat()

image snow_ice_top:
    "snow_ice"
    crop (0, 0, 120, 120)

image snow_ice_wall:
    "snow_ice"
    crop (0, 120, 120, 120)

image snow_cliff01:
    "snow_cliff"
    crop (0, 0, 120, 120)

image snow_cliff02:
    "snow_cliff"
    crop (0, 120, 120, 120)

image snowball_break:
    xanchor 0.20
    "snowball_sprite04"
    pause 0.2
    "snowball_break01"
    pause 0.2
    "snowball_break02"
    pause 0.2
    "snowball_break03"
    pause 0.2
    "empty"

image snowball_drop:
    xanchor 0.20
    pause 0.1
    "snowball_drop01"
    pause 0.2
    "snowball_drop02"
    pause 0.2
    "snowball_drop03"
    pause 0.2
    "empty"

image snowman_sprite 1:
    xzoom -1
    "snowman_sprite0"
    pause 0.15
    "snowman_sprite1"

image snowman_sprite 2:
    "snowman_sprite0"
    pause 0.15
    "snowman_sprite1"

image snowman_sprite_1 = "snowman_sprite [snowman_sprite01.direction]"

image snowman_sprite_2 = "snowman_sprite [snowman_sprite02.direction]"

image snowman_sprite_3 = "snowman_sprite [snowman_sprite03.direction]"

image snow_bonus_pit:
    "snow_normal_pit"

image snow_caretaker_sprite:
    "snow_caretaker_sprite1"
    pause 2.0
    "snow_caretaker_sprite2"
    pause 1.2
    repeat

image cave_wall_half:
    "cave_wall"
    alpha 0.5

image cave_wall_top_half:
    "cave_wall_top"
    alpha 0.5

label Snowbound_Summit_Enter:
    $ snowbound_summit_path = 1
    jump Snowbound_Summit
label Snowbound_Summit:
    $ snow_region_map = {"None": 0, "snow_ice_top": 1, "snow_ice_wall": 2, "snow_cliff01": 3, "snow_cliff02": 4, "snow_trunk": 5, "snow_fell": 6, "snow_rock": 7, "snow_ice_half": 8, "snow_icefloor1": 9}
    $ dungeon_timers = []
    $ enct = None
    if snowbound_summit_path == 1:
        if _return == "Descend":
            $ snowbound_summit = MapPat([], "Snowbound Summit", 7, 2, snow_region_floor, background = "snowbound_summit")
        else:
            $ snowbound_summit = MapPat([], "Snowbound Summit", 7, 6, snow_region_floor, background = "snowbound_summit")
        $ snowbound_summit.floorPlan([
        [1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 2, 2, 1, 1, 0, 1],
        [1, 2, 2, 0, 0, 2, 2, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 8, 0, 0, 1],
        [2, 0, 0, 0, 0, 0, 0, 0, 2],
        [3, 3, 3, 3, 3, 3, 3, 0, 3],
        [4, 4, 4, 4, 4, 4, 4, 0, 4]
        ], snow_region_map)
        $ snow_hole01 = MapUser(2, 5, "snow_normal_hole", 120, 120, "Snow Hole")
        $ snow_tablet01 = MapUser(2, 4, "snow_tablet", 120, 120, "Tablet I")
        $ snow_sign01 = MapUser(5, 5, "snow_sign", 120, 120, "Snow Sign I")
        $ snow_hole02 = MapUser(4, 5, "snow_normal_hole", 120, 120, "Snow Hole")
        $ snowtrail_sprite01 = MapUser(7, 7, "snow_trail", 120, 120, "To Taiga")
        $ snowtrail_sprite02 = MapUser(7, 0, "snow_trail2", 120, 120, "Ascend")
        $ snowball_sprite01 = MapStorer(6, 3, "snowball_sprite01", 120, 120, "Snowball", 0)
        $ snowball_sprite02 = MapStorer(6, 4, "snowball_sprite01", 120, 120, "Snowball", 0)
        if "Snow_Crystal1" not in opened_chests:
            $ snow_crystal01 = MapUser(7, 1, "snow_crystal_sprite", 120, 120, "Snow Crystal")
            $ addSprite(snowbound_summit, snow_crystal01)


        $ addSprite(snowbound_summit, snowtrail_sprite01)
        $ addSprite(snowbound_summit, snowtrail_sprite02)
        $ addSprite(snowbound_summit, snow_tablet01)
        $ addSprite(snowbound_summit, snow_sign01)
        $ addBack(snowbound_summit, snow_hole01)
        $ addBack(snowbound_summit, snow_hole02)
        $ addSprite(snowbound_summit, snowball_sprite01)
        $ addSprite(snowbound_summit, snowball_sprite02)

    elif snowbound_summit_path == 2:
        if _return == "Descend":
            $ snowbound_summit = MapPat([], "Snowbound Summit", 4, 2, snow_region_floor, background = "snowbound_summit")
        else:
            $ snowbound_summit = MapPat([], "Snowbound Summit", 5, 13, snow_region_floor, background = "snowbound_summit")
        $ snowbound_summit.floorPlan([
        [1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 2, 2, 0, 2, 1, 1],
        [1, 2, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 7, 0, 2, 1],
        [2, 0, 0, 6, 5, 0, 0, 1],
        [7, 0, 0, 0, 0, 0, 0, 2],
        [3, 3, 0, 3, 7, 0, 0, 3],
        [1, 0, 0, 4, 3, 0, 0, 4],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 5, 6, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [2, 0, 0, 7, 0, 0, 0, 2],
        [3, 3, 3, 3, 3, 0, 3, 3],
        [4, 4, 4, 4, 4, 0, 4, 4]
        ], snow_region_map)
        if "Snowman2a" not in defeated_enemies:
            $ snowman_sprite01 = MapMover(3, 10, "snowman_sprite_1", 120, 180, "Snowman2a", 6, 2, 1, steppy = 2)
            $ addSprite(snowbound_summit, snowman_sprite01)
        else:
            $ snowball_sprite01 = MapStorer(2, 10, "snowball_sprite02", 120, 120, "Snowball", 3)
            $ addSprite(snowbound_summit, snowball_sprite01)
        if "Snowman2b" not in defeated_enemies:
            $ snowman_sprite02 = MapMover(1, 5, "snowman_sprite_2", 120, 180, "Snowman2b", 6, 2, 1)
            $ addSprite(snowbound_summit, snowman_sprite02)
        else:
            $ snowball_sprite02 = MapStorer(2, 5, "snowball_sprite02", 120, 120, "Snowball", 3)
            $ addSprite(snowbound_summit, snowball_sprite02)
        if "Snow_Crystal2" not in opened_chests:
            $ snow_crystal02 = MapUser(4, 1, "snow_crystal_sprite", 120, 120, "Snow Crystal")
            $ addSprite(snowbound_summit, snow_crystal02)
        $ snow_tablet02 = MapUser(5, 11, "snow_tablet", 120, 120, "Tablet II")
        $ snow_sign02 = MapUser(4, 9, "snow_sign", 120, 120, "Snow Sign II")
        $ snow_hole01 = MapUser(4, 8, "snow_normal_hole", 120, 120, "Snow Hole")
        $ snow_pit01 = MapUser(6, 6, "snow_normal_pit", 120, 120, "Snow Pit")
        $ snow_pit02 = MapUser(2, 2, "snow_normal_pit", 120, 120, "Snow Pit")
        $ snow_bonfire01 = MapUser(1, 4, "bonfire_sprite", 120, 132, "Bonfire")
        $ snowball_sprite03 = MapStorer(4, 10, "snowball_sprite01", 120, 120, "Snowball", 0)
        $ snowtrail_sprite01 = MapUser(5, 14, "snow_trail", 120, 120, "Descend")
        $ snowtrail_sprite02 = MapUser(4, 0, "snow_trail2", 120, 120, "Ascend")

        $ addSprite(snowbound_summit, snow_tablet02)
        $ addSprite(snowbound_summit, snow_sign02)
        $ addBack(snowbound_summit, snow_hole01)
        $ addSprite(snowbound_summit, snow_pit01)
        $ addSprite(snowbound_summit, snow_pit02)
        $ addSprite(snowbound_summit, snow_bonfire01)
        $ addSprite(snowbound_summit, snowball_sprite03)
        $ addSprite(snowbound_summit, snowtrail_sprite01)
        $ addSprite(snowbound_summit, snowtrail_sprite02)


        $ addBackQuick(snowbound_summit, 1, 3, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 2, 4, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 1, 5, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 1, 4, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 2, 6, "snow_stairs")
        $ addBackQuick(snowbound_summit, 5, 7, "snow_stairs")
        $ addBackQuick(snowbound_summit, 6, 7, "snow_stairs")

    elif snowbound_summit_path == 3:
        if _return == "Descend":
            $ snowbound_summit = MapPat([], "Snowbound Summit", 1, 2, snow_region_floor, background = "snowbound_summit")
        else:
            $ snowbound_summit = MapPat([], "Snowbound Summit", 13, 16, snow_region_floor, background = "snowbound_summit")

        $ snowbound_summit.floorPlan([
        [1, 0, 1, 8, 8, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 5, 0, 6, 0, 0, 0, 2, 2, 2, 1],
        [1, 0, 0, 0, 5, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 1],
        [2, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 2],
        [3, 0, 3, 0, 3, 0, 0, 4, 0, 0, 3, 0, 3, 0, 3, 3],
        [4, 0, 4, 0, 0, 0, 0, 0, 0, 7, 4, 0, 0, 0, 4, 4],
        [4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 3, 0, 0, 0, 3, 3, 3, 0, 0, 3, 5, 6, 0, 0, 2],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 7, 4, 3, 0, 0, 0, 3],
        [1, 0, 0, 8, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 8, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
        [2, 2, 0, 0, 0, 8, 8, 8, 2, 2, 2, 0, 0, 0, 2, 2],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4]
        ], snow_region_map)
        $ snowtrail_sprite01 = MapUser(13, 17, "snow_trail", 120, 120, "Descend")
        $ snowtrail_sprite02 = MapUser(1, 0, "snow_trail2", 120, 120, "Ascend")
        $ snowball_sprite01 = MapStorer(11, 13, "snowball_sprite01", 120, 120, "Snowball", 0)
        if "Snow_Crystal3" not in opened_chests:
            $ snow_crystal03 = MapUser(1, 1, "snow_crystal_sprite", 120, 120, "Snow Crystal")
            $ addSprite(snowbound_summit, snow_crystal03)
        $ snow_bonfire01 = MapUser(4, 3, "bonfire_sprite", 120, 132, "Bonfire")
        $ snow_bonfire02 = MapUser(7, 3, "bonfire_sprite", 120, 132, "Bonfire")
        $ snow_bonfire03 = MapUser(7, 7, "bonfire_sprite", 120, 132, "Bonfire")
        $ snow_bonfire04 = MapUser(12, 7, "bonfire_sprite", 120, 132, "Bonfire")
        $ snow_bonfire05 = MapUser(5, 8, "bonfire_sprite", 120, 132, "Bonfire")
        $ snow_bonfire06 = MapUser(2, 9, "bonfire_sprite", 120, 132, "Bonfire")
        $ snow_bonfire07 = MapUser(9, 9, "bonfire_sprite", 120, 132, "Bonfire")
        $ snow_bonfire08 = MapUser(5, 12, "bonfire_sprite", 120, 132, "Bonfire")
        $ snow_bonfire09 = MapUser(14, 12, "bonfire_sprite", 120, 132, "Bonfire")
        $ snow_bonfire10 = MapUser(5, 13, "bonfire_sprite", 120, 132, "Bonfire")
        $ snow_pit01 = MapUser(1, 8, "snow_normal_pit", 120, 120, "Snow Pit")
        $ snow_pit02 = MapUser(12, 2, "snow_bonus_pit", 120, 120, "Snow Pit")
        $ snow_tablet03 = MapUser(12, 13, "snow_tablet", 120, 120, "Tablet III")
        $ snow_sign03 = MapUser(13, 13, "snow_sign", 120, 120, "Snow Sign III")
        if "Snow_Chest01" not in opened_chests:
            $ snow_chest01 = MapUser(14, 2, "stone_chest_closed", 120, 120, "Snow_Chest01")
        else:
            $ snow_chest01 = MapUser(14, 2, "stone_chest_opened", 120, 120, "Snow_Chest01")


        $ addSprite(snowbound_summit, snow_chest01)
        $ addSprite(snowbound_summit, snowball_sprite01)
        $ addSprite(snowbound_summit, snow_bonfire01)
        $ addSprite(snowbound_summit, snow_bonfire02)
        $ addSprite(snowbound_summit, snow_bonfire03)
        $ addSprite(snowbound_summit, snow_bonfire04)
        $ addSprite(snowbound_summit, snow_bonfire05)
        $ addSprite(snowbound_summit, snow_bonfire06)
        $ addSprite(snowbound_summit, snow_bonfire07)
        $ addSprite(snowbound_summit, snow_bonfire08)
        $ addSprite(snowbound_summit, snow_bonfire09)
        $ addSprite(snowbound_summit, snow_bonfire10)
        $ addSprite(snowbound_summit, snowtrail_sprite01)
        $ addSprite(snowbound_summit, snowtrail_sprite02)
        $ addSprite(snowbound_summit, snow_pit01)
        $ addSprite(snowbound_summit, snow_pit02)
        $ addSprite(snowbound_summit, snow_tablet03)
        $ addSprite(snowbound_summit, snow_sign03)
        $ addFrontQuick(snowbound_summit, 14, 2, "snow_ice_top")
        $ addFrontQuick(snowbound_summit, 13, 2, "snow_ice_top")
        $ addFrontQuick(snowbound_summit, 12, 2, "snow_ice_top")
        $ addBackQuick(snowbound_summit, 4, 3, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 7, 3, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 7, 7, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 12, 7, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 5, 8, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 2, 9, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 9, 9, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 5, 12, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 14, 12, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 5, 13, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 4, 2, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 5, 3, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 3, 3, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 7, 2, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 7, 4, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 8, 7, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 6, 7, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 7, 8, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 13, 7, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 11, 7, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 12, 8, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 6, 8, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 5, 7, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 4, 8, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 9, 8, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 8, 9, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 3, 9, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 2, 10, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 4, 12, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 4, 13, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 5, 14, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 6, 12, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 6, 13, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 13, 12, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 14, 11, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 2, 9, "bonfire_light_stairs")
        $ addBackQuick(snowbound_summit, 3, 9, "bonfire_light_stairs")
        $ addBackQuick(snowbound_summit, 2, 9, "bonfire_light_stairs")
        $ addBackQuick(snowbound_summit, 8, 9, "bonfire_light_stairs")
        $ addBackQuick(snowbound_summit, 9, 9, "bonfire_light_stairs")
        $ addBackQuick(snowbound_summit, 4, 9, "snow_stairs")
        $ addBackQuick(snowbound_summit, 12, 10, "snow_stairs")
        $ addBackQuick(snowbound_summit, 13, 10, "snow_stairs")
        $ addBackQuick(snowbound_summit, 14, 10, "snow_stairs")
        $ addBackQuick(snowbound_summit, 11, 6, "snow_stairs")
        $ addBackQuick(snowbound_summit, 13, 6, "snow_stairs")
        $ addBackQuick(snowbound_summit, 1, 6, "snow_stairs")
        $ addBackQuick(snowbound_summit, 1, 7, "snow_stairs")
        $ addBackQuick(snowbound_summit, 3, 6, "snow_stairs")
        $ addBackQuick(snowbound_summit, 5, 6, "snow_stairs")
        $ addBackQuick(snowbound_summit, 6, 6, "snow_stairs")
        $ addBackQuick(snowbound_summit, 8, 6, "snow_stairs")
        $ addBackQuick(snowbound_summit, 9, 6, "snow_stairs")

    elif snowbound_summit_path == 4:
        if _return == "Descend":
            $ snowbound_summit = MapPat([], "Snowbound Summit", 4, 2, snow_region_floor, background = "snowbound_summit")
        else:
            $ snowbound_summit = MapPat([], "Snowbound Summit", 4, 12, snow_region_floor, background = "snowbound_summit")
        $ snowbound_summit.floorPlan([
        [1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 2, 2, 0, 2, 2, 1, 1],
        [1, 2, 0, 0, 0, 0, 0, 2, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 1, 1],
        [1, 2, 0, 1, 0, 1, 0, 2, 1],
        [1, 0, 0, 2, 0, 2, 0, 0, 1],
        [1, 1, 0, 3, 3, 3, 0, 1, 1],
        [1, 2, 0, 0, 0, 0, 0, 2, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1],
        [2, 0, 0, 0, 0, 0, 0, 0, 2],
        [3, 3, 3, 3, 0, 3, 3, 3, 3],
        [4, 4, 4, 4, 0, 4, 4, 4 ,4]
        ], snow_region_map)
        if "Snowman4a" not in defeated_enemies:
            $ snowman_sprite01 = MapMover(3, 10, "snowman_sprite_1", 120, 180, "Snowman4a", 6, 2, 1, steppy = 2)
            $ addSprite(snowbound_summit, snowman_sprite01)
        else:
            $ snowball_sprite01 = MapStorer(3, 10, "snowball_sprite02", 120, 120, "Snowball", 3)
            $ addSprite(snowbound_summit, snowball_sprite01)
        if "Snowman4b" not in defeated_enemies:
            $ snowman_sprite02 = MapMover(5, 10, "snowman_sprite_2", 120, 180, "Snowman4b", 6, 2, 1)
            $ addSprite(snowbound_summit, snowman_sprite02)
        else:
            $ snowball_sprite02 = MapStorer(5, 10, "snowball_sprite02", 120, 120, "Snowball", 3)
            $ addSprite(snowbound_summit, snowball_sprite02)
        $ snow_tablet04 = MapUser(4, 10, "snow_tablet", 120, 120, "Tablet IV")
        $ snow_pit01 = MapUser(6, 11, "snow_normal_pit", 120, 120, "Snow Pit")
        $ snow_pit02 = MapUser(4, 7, "snow_normal_pit", 120, 120, "Snow Pit")
        $ snow_bonfire01 = MapUser(4, 3, "bonfire_sprite", 120, 132, "Bonfire")
        $ snow_trail_sprite01 = MapUser(4, 13, "snow_trail", 120, 120, "Descend")
        $ snow_trail_sprite02 = MapUser(4, 0, "snow_trail2", 120, 120, "Ascend")
        if "Snow_Crystal4" not in opened_chests:
            $ snow_crystal04 = MapUser(4, 1, "snow_crystal_sprite", 120, 120, "Snow Crystal")
            $ addSprite(snowbound_summit, snow_crystal04)

        $ addBackQuick(snowbound_summit, 4, 3, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 4, 4, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 4, 2, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 3, 3, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 5, 3, "bonfire_light_tile")
        $ addBackQuick(snowbound_summit, 2, 5, "snow_stairs")
        $ addBackQuick(snowbound_summit, 2, 6, "snow_stairs")
        $ addBackQuick(snowbound_summit, 4, 5, "snow_stairs")
        $ addBackQuick(snowbound_summit, 4, 6, "snow_stairs")
        $ addBackQuick(snowbound_summit, 6, 5, "snow_stairs")
        $ addBackQuick(snowbound_summit, 6, 6, "snow_stairs")
        $ addBackQuick(snowbound_summit, 3, 5, "snow_stairs")
        $ addBackQuick(snowbound_summit, 5, 5, "snow_stairs")
        $ addBackQuick(snowbound_summit, 2, 8, "snow_stairs")
        $ addBackQuick(snowbound_summit, 6, 8, "snow_stairs")
        $ addSprite(snowbound_summit, snow_tablet04)
        $ addSprite(snowbound_summit, snow_pit01)
        $ addSprite(snowbound_summit, snow_pit02)
        $ addSprite(snowbound_summit, snow_bonfire01)
        $ addSprite(snowbound_summit, snow_trail_sprite01)
        $ addSprite(snowbound_summit, snow_trail_sprite02)

    elif snowbound_summit_path == 5:
        $ snowbound_summit = MapPat([], "Snowbound Summit", 7, 11, snow_region_floor, background = "snowbound_summit")
        $ snowbound_summit.floorPlan([
        [1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 2, 1, 1, 1, 2, 0, 2, 1, 1, 1, 2, 1, 1],
        [1, 2, 9, 2, 1, 2, 0, 0, 0, 2, 1, 2, 9, 2, 1],
        [1, 9, 9, 9, 1, 8, 0, 0, 0, 8, 1, 9, 9, 9, 1],
        [2, 1, 9, 1, 2, 0, 0, 0, 0, 0, 2, 1, 9, 1, 2],
        [0, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2, 0],
        [0, 0, 1, 8, 0, 0, 0, 0, 0, 0, 0, 8, 1, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 1, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1, 0],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [3, 0, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3],
        [4, 0, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4 ,4]
        ], snow_region_map)

        $ snowball_sprite01 = MapStorer(4, 6, "snowball_sprite04", 120, 120, "Snowball", 9)
        $ snowball_sprite02 = MapStorer(6, 6, "snowball_sprite02", 120, 120, "Snowball", 3)
        $ snowball_sprite03 = MapStorer(8, 6, "snowball_sprite03", 120, 120, "Snowball", 6)
        $ snowball_sprite04 = MapStorer(10, 6, "snowball_sprite01", 120, 120, "Snowball", 0)
        $ snowball_sprite05 = MapStorer(5, 7, "snowball_sprite02", 120, 120, "Snowball", 3)
        $ snowball_sprite06 = MapStorer(9, 7, "snowball_sprite03", 120, 120, "Snowball", 6)
        $ snowball_sprite07 = MapStorer(7, 5, "snowball_sprite02", 120, 120, "Snowball", 3)
        $ snowman_sprite01 = MapMover(4, 5, "snowman_sprite_1", 120, 180, "Snowman5a", 6, 2, 2)
        $ snowman_sprite02 = MapMover(10, 5, "snowman_sprite_2", 120, 180, "Snowman5b", 6, 2, 1, steppy = 3)
        $ snow_trail_sprite01 = MapUser(7, 12, "snow_trail", 120, 120, "Descend")
        $ snow_trail_sprite02 = MapUser(1, 12, "snow_trail", 120, 120, "To Taiga")
        $ snow_tablet05 = MapUser(7, 4, "snow_tablet", 120, 120, "Tablet V")

        if "The Caretaker" not in defeated_enemies or defeated_enemies["The Caretaker"] == "Defeated":
            $ snow_oolong_sprite = MapUser(7, 2, "snow_oolong", 120, 120, "Oolong")
            $ addSprite(snowbound_summit, snow_oolong_sprite)
        elif defeated_enemies["The Caretaker"] == "In Garden":
            $ snow_caretaker_sprite = MapUser(7, 2, "snow_caretaker_sprite", 120, 180, "The Caretaker")
            $ addSprite(snowbound_summit, snow_caretaker_sprite)

        $ addSprite(snowbound_summit, snowman_sprite01)
        $ addSprite(snowbound_summit, snowman_sprite02)
        $ addSprite(snowbound_summit, snow_tablet05)
        $ addSprite(snowbound_summit, snowball_sprite01)
        $ addSprite(snowbound_summit, snowball_sprite02)
        $ addSprite(snowbound_summit, snowball_sprite03)
        $ addSprite(snowbound_summit, snowball_sprite04)
        $ addSprite(snowbound_summit, snowball_sprite05)
        $ addSprite(snowbound_summit, snowball_sprite06)
        $ addSprite(snowbound_summit, snowball_sprite07)
        $ addSprite(snowbound_summit, snow_trail_sprite01)
        $ addSprite(snowbound_summit, snow_trail_sprite02)
        $ addBackQuick(snowbound_summit, 0, 8, "grass_flower1")
        $ addBackQuick(snowbound_summit, 0, 7, "snow_icefloor4")
        $ addBackQuick(snowbound_summit, 0, 6, "snow_icefloor5")
        $ addBackQuick(snowbound_summit, 0, 5, "snow_icefloor8")
        $ addBackQuick(snowbound_summit, 1, 6, "snow_icefloor2")
        $ addBackQuick(snowbound_summit, 13, 7, "snow_icefloor3")
        $ addBackQuick(snowbound_summit, 14, 7, "snow_icefloor7")
        $ addBackQuick(snowbound_summit, 14, 6, "snow_icefloor2")
        $ addBackQuick(snowbound_summit, 14, 5, "snow_icefloor6")
        $ addBackQuick(snowbound_summit, 1, 7, "grass_flower2")
        $ addBackQuick(snowbound_summit, 14, 8, "grass_flower1")
        $ addBackQuick(snowbound_summit, 13, 6, "grass_flower2")
        $ addBackQuick(snowbound_summit, 7, 10, "snow_stairs")
        $ addBackQuick(snowbound_summit, 7, 11, "snow_stairs")
        $ addBackQuick(snowbound_summit, 1, 11, "snow_stairs")

    $ addSprite(snowbound_summit, snowbound_summit.playerSprite)
    $ snowbound_summit.updateFloor(snow_region_floor)

    $ current_location = snowbound_summit
    $ snowbound_summit.entranceCount += 1
    jump Snowbound_Summit_Loop

label Snowbound_Summit_Loop:
    $ renpy.music.play(mOpen1, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ disableC = False
    $ sprite = snowbound_summit.playerSprite
    show screen dungeon_buttons()
    call screen dungeon_map(snowbound_summit)
    show screen dungeon_map(snowbound_summit)
    $ disableC = True
    $ spriteInFront = snowbound_summit.locateSpriteInFront(sprite)
    if enct == "Snowball" and spriteInFront != None and isinstance(spriteInFront, MapUser) and spriteInFront.interaction == "Snowball":
        $ enct = None
        $ x, y = getFacingTile(sprite)
        $ snow_back = snowbound_summit.mappy[y][x].back
        if snowbound_summit_path >= 3:
            if snow_back != None:
                if snow_back.img == "bonfire_light_tile":
                    $ spriteInFront.status -= 2
                    $ snow_back.img = "bonfire_light_blank"
                elif snow_back.img == "bonfire_light_blank":
                    $ spriteInFront.status -= 3
                    $ snow_back.img = "bonfire_light_tile"
                elif snow_back.img == "snow_floor_blank":
                    $ spriteInFront.status -= 1
                    $ removeBack(snowbound_summit, snow_back)
                elif snow_back.img == "snow_stairs_blank":
                    $ spriteInFront.status -= 1
                    $ snow_back.img = "snow_stairs"
                elif snow_back.img == "snow_stairs":
                    $ spriteInFront.status += 1
                    $ snow_back.img = "snow_stairs_blank"
            else:
                $ addBackQuick(snowbound_summit, x, y, "snow_floor_blank")
                $ spriteInFront.status += 1
        else:
            if snow_back != None and snow_back.img == "bonfire_light_tile":
                $ spriteInFront.status -= 2
            else:
                $ spriteInFront.status += 1
        if spriteInFront.status < 0:
            "The snowball melts down to nothing..."
            $ removeSprite(snowbound_summit, spriteInFront)
        if spriteInFront.status >= 12:
            $ snowball_sprite_img = "snowball_break"
            $ spriteInFront.img = snowball_sprite_img
            pause 1.0
            $ removeSprite(snowbound_summit, spriteInFront)
        else:
            $ snowball_sprite_img = "snowball_sprite0" + str(int(spriteInFront.status/3+1))
            $ snowball_sprite_img = Transform(snowball_sprite_img, rotate = renpy.random.randint(0, 360), anchor = (0.15, 0.15))
            $ spriteInFront.img = snowball_sprite_img

        if snowbound_summit.mappy[y][x].back != None and snowbound_summit.mappy[y][x].back.img == "snow_normal_hole":
            if spriteInFront.status < 9 and spriteInFront.status >= 6:
                $ snowball_sprite_img = "snowball_drop"
                $ snowball_sprite_img = Transform(snowball_sprite_img, anchor = (0.0, 0.0))
                $ spriteInFront.img = snowball_sprite_img
                pause 0.7
                $ removeSprite(snowbound_summit, spriteInFront)
                $ snowbound_summit.mappy[y][x].back.img = "snow_filled_hole"
            elif spriteInFront.status >= 9:
                $ spriteInFront.interaction = "Stuck Snowball"
                $ snowball_sprite_img = "snowball_drop"
                $ snowball_sprite_img = Transform(snowball_sprite_img, anchor = (0.0, 0.0))
                $ spriteInFront.img = snowball_sprite_img
                pause 0.7
                $ spriteInFront.img = "snow_blocked_hole"

    if snowbound_summit.searchBack("snow_normal_hole") + snowbound_summit.searchUser("snow_normal_pit") == 0 and snowbound_summit.searchForUser("snow_crystal_sprite") != []:
        "It seems like you have filled all the holes here, and you can hear the sound of a crystal shattering in the distance."
        $ opened_chests["Snow_Crystal" + str(snowbound_summit_path)] = True
        $ removeSprite(snowbound_summit, snowbound_summit.searchForUser("snow_crystal_sprite")[0])

    if _return == "Bonfire":
        "You approach the campfire and feel its warmth. It seems the snowball will melt down by 3 steps if it passes around the fire..."

    if _return == "Snow Sign":
        "It seems you can roll the snowball around, it'll get bigger every 3 steps, but it'll break apart if it gets larger than 12 steps."

    if _return == "Snow Hole":
        "The hole is empty, but it seems like you can fill it with some white snow. perhaps one large enough, but too large it may block the way..."

    if _return == "Snow Pit":
        "This pit goes deeper into the ground, it's impossible to walk through, you may need to fill the hole with a bigger one..."

    if _return == "To Taiga":
        "You walk through the snow away from the summit, and back into the familiar taiga forest."
        hide screen dungeon_map
        hide screen dungeon_buttons
        jump main_frosted_taiga

    if enct == "Snow Pit Filled":
        $ enct = None
        $ removeSprite(snowbound_summit, spriteInFront)
        $ addBack(snowbound_summit, spriteInFront)
        $ spriteInFront.img = "snow_filled_pit"

    if _return == "Snow_Chest01":
        if "Snow_Chest01" not in opened_chests:
            "You check the crack in the ice and find a strange shard inside."
            "The jagged shard is a bit cold to the touch, it rattles like loose icicles when you touch it."
            "The surface of the shard seems to be etched with runes that shimmer silver in dim light."
            "'A critical blow may slow one down, but a well-placed strike may shatter the ice.'"
            $ opened_chests["Snow_Chest01"] = True
            $ addTrinket(shiveringshard_item, tinventory)
            $ removeSprite(snowbound_summit, snow_chest01)
            $ snow_chest01 = MapUser(14, 2, "stone_chest_opened", 120, 120, "Snow_Chest01")
            $ addSprite(snowbound_summit, snow_chest01)

    if _return == "Oolong":
        if defeated_enemies.get("The Caretaker", False) != "Defeated":
            "You kneel at the edge of the summit's snowy slope, brushing aside the last tuft of frost-hardened drifts to reveal the stems of the Oolong."
            "The plant is a deep green, and the scent of tea wafts from it. Its leaves glimmer with a faint warmth even in the biting wind."
            e "That must be the Oolong Haskell was talking about, I should dig out the plant and leave."
            jump Snowbound_Summit_Oolong_Menu
        else:
            "You have harvested most of the Oolong leaves from the plant, leaving behind a few that are still growing."
            "The plant is still alive, you can see the roots are still intertwined with the Caretaker's fur."
            "But it does not seem to be growing, or not as much as you'd have hoped."
            menu:
                "Pick around the leaves":
                    "Your hand brushes against the leaves, trying to harvest any remaining leaves."
                    "But the plant seems to be resistant to your touch, as if it knows you have already taken enough."
                    "A low rumble echoes through the ground, and you hear a deep, grunting voice."
                    snow_caretaker "Mortal, you have already taken enough... Begone now, I'm trying to sleep."
                    e "Oh, sorry, I didn't mean to disturb you."
                    e "Uhm, are you gonna grow more Oolong?"
                    snow_caretaker "No, not until the tender of the garden takes over... with his axe."
                "Place the axe on top of the Caretaker" if LookForItem("Axe of Ookko", inventory):
                    "You take out the axe, and place it in front of the Oolong plant."
                    "The plant twitches, and you can see the roots moving slightly, as if they are trying to reach for the axe."
                    "Soon, the Caretaker emerges from the snow once more."
                    $ snow_oolong_sprite.h = 180
                    $ snow_oolong_sprite.img = "snow_caretaker_sprite"
                    snow_caretaker "Mortal, what is the meaning of this disturbanc-"
                    "The Caretaker stops mid-sentence, his eyes widening as he sees the axe in his eyes."
                    snow_caretaker "Ookko's axe... you have found it?"
                    e "Uhm, this one?"
                    snow_caretaker "Yes. His gardening axe, he has had many battle axes, but this one, this one is special."
                    snow_caretaker "If it is in your hand, then... you would be a good gardener, wouldn't you?"
                    e "I... I guess so?"
                    menu:
                        snow_caretaker "Then, are you willing to tend to the garden?"
                        "Yes":
                            $ defeated_enemies["The Caretaker"] = "In Garden"
                            $ snow_oolong_sprite.interaction = "The Caretaker"
                            e "Yes, I can take over the garden."
                            snow_caretaker "Very well, mortal. Then the growth of the Oolong with be at your hand. The Oolong from now on will be yours to harvest."
                            snow_caretaker "But know that, mortal, you are now bound to the responsibility of tending to the garden."
                            e "What is the responsibility?"
                            "The Caretaker pats away the snow stuck to his fur, then turns to you."
                            snow_caretaker "You will assist in the growth of Oolong."
                            "With a short answer, the caretaker turns away as it continues to bask in the sunlight."
                        "No":
                            e "Uhm, I don't know, I mean, I just wanted to get the Oolong."
                            snow_caretaker "I see, mortal. Then you're just not worthy enough to take on the responsibility."
                            "The Caretaker steps back, his eyes narrowing as he looks at you with a hint of disappointment."
                            $ snow_oolong_sprite.h = 120
                            $ snow_oolong_sprite.img = "snow_oolong"
                            "He quickly burrows into the snow, leaving you alone with the axe that you've brought."
                "Leave it for now":

                    pass


    if _return == "Tablet I":
        call Snowbound_Summit_Tablet_I from _call_Snowbound_Summit_Tablet_I

    if _return == "Tablet II":
        call Snowbound_Summit_Tablet_II from _call_Snowbound_Summit_Tablet_II

    if _return == "Tablet III":
        call Snowbound_Summit_Tablet_III from _call_Snowbound_Summit_Tablet_III

    if _return == "Tablet IV":
        call Snowbound_Summit_Tablet_IV from _call_Snowbound_Summit_Tablet_IV

    if _return == "Tablet V":
        call Snowbound_Summit_Tablet_V from _call_Snowbound_Summit_Tablet_V

    if _return == "Snow Sign I":
        "The sign reads: 'The snowball can be rolled around to fill the holes, it grows bigger each time it rolls, but it'll fall apart after 12 steps.'"
        "'In order to break the sealing crystal, all holes must be filled.'"

    if _return == "Snow Sign II":
        "The sign reads: 'The snowman is a being of snow, it may be reduced to its original form upon defeat.'"
        "'Rolling a snowball near the bonfire will melt it down a few steps.'"

    if _return == "Snow Sign III":
        "The sign reads: 'Here, the snow is shallow, a snowball will leave behind snow if it retreads the same tile.'"

    if _return == "The Caretaker":
        if haskell_dialogues.get("Caretaker", False) == False:
            $ haskell_dialogues["Caretaker"] = {}
        if haskell_dialogues["Caretaker"].get("Garden Tending", 0) != 0:
            $ haskell_dialogues["Caretaker"]["Garden Tending"] += 1
            if haskell_dialogues["Caretaker"].get("Garden Tending", False) - haskell_dialogues["Caretaker"].get("Essence Extraction", 0) > 3:
                "The Caretaker stares at you as you apporach, his glare seems to signal that he is not pleased with your presence."
                e "Uh, hey."
                snow_caretaker "You have betrayed my trust, mortal. You have not tended to my garden, and you have not brought me the essence I require."
                "He steps closer to you, looming over you imposingly."
                e "I... I was just about to do that, Caretaker. I just wanted to talk to you to see if I missed anything."
                snow_caretaker "No more lies, mortal. If you do not intend to fulfill your end of the bargain, I will just have to extract from you myself."
                snow_caretaker "But do not fret, for my fellow snowmen will assist."
                $ haskell_dialogues["Caretaker"]["Essence Extraction"] = haskell_dialogues["Caretaker"].get("Garden Tending")
                $ haskell_dialogues["Caretaker"]["Forced Count"] = haskell_dialogues["Caretaker"].get("Forced Count", 0) + 1
                $ haskell_dialogues["Caretaker"]["Extraction Scene"] = "Forced"
                hide screen dungeon_map
                scene black with dissolve
                call Scene_Caretaker_Extraction from _call_Scene_Caretaker_Extraction
                $ pc.lust = 0
                $ pc.add_active_status(stuffed)
                $ pc.add_active_status(soremouthed)
        "The Caretaker is standing in front of you, he seems to be waiting for you to approach him."
        if haskell_dialogues["Caretaker"].get("Garden Tending", False) == False:
            e "Hey. I thought you were going to sleep again?"
            "The Caretaker looks at you with a blank expression."
            snow_caretaker "You have awoken me from my deep slumber, I cannot fall back to sleep so soon, especially when the garden is in need of tending."
            e "How soon is so soon?"
            snow_caretaker "A few years, perhaps."
            e "Mood."
        snow_caretaker "You shall tend to the garden now, instead of asking worthless question."
        menu:
            "Harvest the Oolong" if haskell_dialogues["Caretaker"].get("Extraction Scene") != None or (haskell_dialogues["Caretaker"].get("Harvesting Day", 0) > 0 and haskell_dialogues["Caretaker"].get("Harvesting Day", 0) <= timenow.day):
                e "So, I can harvest the Oolong now?"
                if haskell_dialogues["Caretaker"].get("Extraction Scene", None) == "Forced":
                    snow_caretaker "Despite your reluctance, I have promised to give you the Oolong after you have tended to the garden, regardless of how you do it."
                else:
                    snow_caretaker "Yes, you have done well tending to the garden, mortal. The Oolong is growing well, and it is ready to be harvested."

                "You nod, as the Caretaker turns around and picks a few leaves from his head, handing them to you."
                snow_caretaker "Know that my brethens were satisfied with your work as well as I do. You are more than welcome to tend to the garden again."
                "You take the leaves from the Caretaker's hand, they are warm to the touch, and you can feel a faint pulse of energy coming from them."
                $ haskell_dialogues["Caretaker"]["Extraction Scene"] = None
                $ addItem("Oolong Leaves", inventory, 1)
            "Ask about the garden tending":
                if haskell_dialogues["Caretaker"].get("Garden Tending", 0) == 0:
                    $ haskell_dialogues["Caretaker"]["Garden Tending"] = 1
                if haskell_dialogues["Caretaker"].get("Garden Tending", 0) <= 1:
                    e "So, what did you actually mean by tending to the garden?"
                    snow_caretaker "You shall spray your essence on the Oolong plant, just as Ookko did."
                    e "Wait, what? You didn't say that before!"
                    snow_caretaker "You did not ask before, mortal."
                    "You shake your head, obviously you expected the task to be complicated, but you did not expect it to use your 'essence'."
                    e "So, I just spray it on you, right?"
                    snow_caretaker "Yes, but no, I assume you will miss the plant and waste the precious essence of your kind. I expect you to bring me a vial of yours, or anyone else better, or I can arrange a formality to extract essence from you."
                    e "Anyone else? So... not just mine?"
                    snow_caretaker "Yes, I have had many beings' essence on me, be it the primordials, the dragons, even the minotaur would suffice."
                    snow_caretaker "But I would much prefer to extract your fresh essence directly from the source."
                    "You nod."
                call Scene_Caretaker_Tending_Menu from _call_Scene_Caretaker_Tending_Menu
            "Ask about Ookko":
                e "So, who is Ookko?"
                snow_caretaker "Ookko is the primordial who watches over the snowland. His essence was the one that brought the Oolong to life, and with it, my purpose."
                e "The primordial? So, he is like a god?"
                snow_caretaker "One of the old gods who created the world, yes."
                snow_caretaker "He has long since left our realm, but I am bound to my duty still."
            "Ask about the Slumber" if haskell_dialogues["Caretaker"].get("Essence Extraction", 0) > 0:
                e "So, you said you were in a slumber?"
                snow_caretaker "Yes, the garden has not been tended to for a long time, and I have been placed in a deep slumber to preserve energy for the Oolong."
                e "Are there any other people who tended to the garden?"
                snow_caretaker "There were few, but they have all left, or died. I do not recall their names, but I remember their essence."
                "The Caretaker looks away with a blank expression, as if he's comparing the memory of each essence."
                if haskell_dialogues["Caretaker"].get("Essence Extraction", 0) > 0:
                    snow_caretaker "Your essence is different, mortal. It reminded me of the primordial."
            "Slip away":
                e "Uh, yeah... r-right away!"
                "You nod nervously, trying to sneak away from the creature."

    if _return == "Ascend":
        $ snowbound_summit_path += 1
        jump Snowbound_Summit

    if _return == "Descend":
        $ snowbound_summit_path -= 1
        jump Snowbound_Summit

    if isinstance(_return, str) and _return[:7] == "Snowman":
        $ current_enemy = _return
        hide screen dungeon_map
        jump snowman_battle

    if _return == "Restart":
        jump Snowbound_Summit


    jump Snowbound_Summit_Loop

label Scene_Caretaker_Tending_Menu:
    menu:
        snow_caretaker "Are you ready to tend to the garden?"
        "Yes, I have a vial of essence." if LookForItem("Minotaur Essence", inventory):
            e "Yes, I have a vial of the Minotaur's."
            "You hand the vial of essence to the Caretaker, who takes it with a nod of approval."
            snow_caretaker "The minotaur? How did yo-... Very well, mortal, I shall accept it."
            snow_caretaker "My gratitude for your service, mortal. Ookko watches over you."
            snow_caretaker "If you wish to harvest the Oolong, you may do so after a day. It will be ready by then."
            "You nod."
            $ removeItem("Minotaur Essence", inventory, 1)
            $ haskell_dialogues["Caretaker"]["Harvesting Day"] = timenow.day + 1
        "{s}Yes, I have a vial of essence.{/s}" if not LookForItem("Minotaur Essence", inventory):
            "You don't have any essence on you... You need to get one first."
            jump Scene_Caretaker_Tending_Menu
        "Extract essence from me":
            e "How about you just extract essence from me yourself?"
            snow_caretaker "I strongly advise against it, mortal, my size would break you easily, it's not going to be a pleasant experience."
            snow_caretaker "You are better off releasing your essence in a vial..."
            "You stare at the enormous shaft between the Caretaker's legs, you can only imagine how painful it would be to have it inside you."
            e "I can take it, Caretaker."
            "He nods."
            snow_caretaker "Very well, mortal, then I shall invite my fellow snowmen to assist in the extraction."
            "You gulp loudly, the thought of being surrounded by the already hung snowmen while the Caretaker extracts your essence would be unbearable, but you nod anyway."
            $ haskell_dialogues["Caretaker"]["Essence Extraction"] = haskell_dialogues["Caretaker"].get("Garden Tending")
            $ haskell_dialogues["Caretaker"]["Complied Count"] = haskell_dialogues["Caretaker"].get("Complied Count", 0) + 1
            $ haskell_dialogues["Caretaker"]["Extraction Scene"] = "Complied"
            hide screen dungeon_map
            scene black with dissolve
            call Scene_Caretaker_Extraction from _call_Scene_Caretaker_Extraction_1
            $ pc.lust = 0
            $ pc.add_active_status(stuffed)
            $ pc.add_active_status(soremouthed)
        "Maybe later":
            e "Maybe later, I-I need to think about it."
            snow_caretaker "Mortal, you promised to tend to my garden, so you better do it soon, or I will extract essence from you myself."
    return

label Snowbound_Summit_Tablet_I:
    "In the midst of the snow and ice, you find a strange stone tablet."
    "It is covered in strange markings, a mixture of ancient runes and letters you can barely make out."
    "But, through some effort and a lot of squinting, you manage to decipher the text."
    "Tablet I - The Warrior's Respite"
    "{i}'In the Age of Clashing Skies, when thunder rang not from clouds but from clashing blades, Ookko strode through the Vale of Withered Pines.'{/i}"
    "{i}'Silvered trunks groaned beneath wind's icy howl, and crystalline frost weighed upon every branch. He paused beside a frozen brook—its waters locked in time—where even the caw of ravens was swallowed by the white hush.'{/i}"
    "{i}'Weary of mortal squabbles and divine intrigues, he cast aside crown and axe, letting the wind strip away each memory of battle. '{/i}"
    "{i}'With each footfall crunching upon snow-hard earth, he felt the hunger for war slacken — and a strange urge dawn in his heart.'{/i}"
    return

label Snowbound_Summit_Tablet_II:
    "Tablet II - The Barren Crest"
    "{i}'Beyond the pines lay the Barren Crest: a plateau of shifting drifts, where spindrift danced like ghostly embers at dusk. '{/i}"
    "{i}'There, no beast dared roam, and the sky's pale curtain seemed to press earthward. He stripped away his armor and axe, casting it into the void, and knelt upon the frozen ground.'{/i}"
    "{i}'In utter frustration, deeper than any trench he had carved, Ookko stretched forth his gauntleted hand and spilled forth seeds — fragments of his own sovereign will, warmed by divine fire yet chilled by centuries of strife.'{/i}"
    return

label Snowbound_Summit_Tablet_III:
    "Tablet III - The First Sprout"
    "{i}'Winter's breath reigned supreme for thrice ten dawns and dusks. Yet, beneath the moonlit crust, a single tendril quivered.'{/i}"
    "{i}'It broke through crusted ice with a faint crack — an echo like brittle bone giving way.'{/i}"
    "{i}'Ookko, drawn by this marvel, encircled the spot with wards of living frost, shaping cages of ice to shelter the spawn from avalanche giants and lost wanderers.'{/i}"
    return

label Snowbound_Summit_Tablet_IV:
    "Tablet IV - The Leaf of Oolong"
    "{i}'When the young foliage crested its first cluster of leaves, it exhaled a fragrance that mingled honeyed dusk with molten steel.'{/i}"
    "{i}'Ookko plucked a leaf and steeped it in steaming summit snow — its heat carving steam veils that danced skyward. He tasted the brew: warmth without flame, calm without stillness.'{/i}"
    "{i}'In reverent hush he spoke a name into the swirling gale — 'Oolong.' Even now, those who sip its leaves speak of flickers in their dreams, watching from a place untouched by mortal sight.'{/i}"
    return

label Snowbound_Summit_Tablet_V:
    "Tablet V - The Last March"
    "{i}'At dawn's first glimmer, Ookko girded himself once more in armor of starlight. He knelt before the mass of Oolong's roots, half-buried in fur coils beneath snowdrifts.'{/i}"
    "{i}'He bowed his head, offering a silent vow: that this life, sprung from war's remnant, would endure when steel and thunder faded.'{/i}"
    "{i}'Then he turned his gaze away from the summit — where swirling flurries greased his steps — and strode into the gathering gloom to confront the devouring darkness.'{/i}"
    "{i}'The prints of his boots vanish here, along with the blunt axe of the garden. But beneath the snow, the roots of Oolong pulse still, as though bidding the Primordial a return.'{/i}"
    return

label Snowbound_Summit_Oolong_Menu:
    menu:
        "{s}Dig out the Oolong{/s}" if not LookForItem("Small Trowel", inventory):
            "It doesn't seem like I can dig out the Oolong without a trowel..."
            jump Snowbound_Summit_Loop

        "Dig out the Oolong" if LookForItem("Small Trowel", inventory):
            jump Snowbound_Summit_Oolong
        "Leave for now":
            jump Snowbound_Summit_Loop

    return

label Snowbound_Summit_Oolong:



    if LookForItem("Small Trowel", inventory):
        "You pull out the trowel and kneel down, digging into the snow around the Oolong plant."
        "The trowel bites into the frozen earth, and you feel a strange warmth radiating from the plant."
        e "I can feel it... I can almost taste it..."
    "Slowly you reveal the twisted roots of the plant, but as your fingers close around the stem, the ground shudders beneath you."


    e "Huh... what was that?"
    with vpunch
    "A low rumble splits the air. The snow around the plant buckles and cracks, and a hulking form erupts from the white - "
    $ snow_oolong_sprite.h = 180
    $ snow_oolong_sprite.img = "snow_caretaker_sprite"
    show screen dungeon_map(snowbound_summit)
    "It is a creature nearly double your height, its body covered in thick, russet fur shot through with loose snow and icy blue streaks."
    "The Oolong plant is rooted on its head, its leaves fanning out like a crown."
    "Its eyes are a bright, neon blue, and its breath comes in frosty puffs that hang in the air like clouds."
    my "O-... Ookko? Have you finally returned?"
    menu:
        "Pretend to be Ookko":
            "You nod your head, trying to feint a deep, rumbling voice."
            e "Yes, I have returned, and I'm here to harvest the plant."
            "The creature's eyes narrow, and it snorts, sending a plume of frost into the air."
            my "Your scent deceived me, but not your voice, mortal. And you dare to step foot on Ookko's domain?"
        "Be honest":

            e "No, I'm not Ookko. I'm just a traveler. I was looking for the tea leaves."
            "You take a step back, raising your hands in a placating gesture as you try to keep your distance from the hulking creature."
            my "A traveler? And you dare to step foot on Ookko's domain?"
            e "I just need the plant, for a friend. Please, I don't mean any harm."
            my "You've come to invade my garden, disturb my slumber, and now you dare to ask for my spawn?"
            if pc.cha <= 8 and not LookForItem("Axe of Ookko", inventory):
                my "You are more foolish than bold, mortal..."
            else:
                my "You are bold, mortal. But Ookko is not without mercy."
                if pc.cha > 8:
                    e "I can help you with the garden, if you let me just take some of it."
                    my "Huh... I cannot deny, the garden has been neglected for too long."
                    my "You have a deal, mortal. You may take some of the plant, but in exchange you must tend to the garden."

                elif LookForItem("Axe of Ookko", inventory):
                    my "I can smell Ookko's warmth on you. Tell me, mortal, how did you come to possess the axe?"
                    e "Uhm, this one?"
                    my "Yes. His gardening axe, he has had many battle axes, but this one, this one is special."
                    my "If it is in your hand, then... you would be a good gardener, wouldn't you?"
                "You nod your head, and the creature huffs a cloud of frost into the air."
                my "Take the plant, mortal. Ookko watches you."
                e "Oh, that's it? I can just take it?"
                my "Yes, as long as you promise to tend to the garden."
                e "Okay, I'll take care of it."
                e "How may I call you?"
                snow_caretaker "Ookko named me the Caretaker. I look after the garden, in his absence."
                e "Oh, Ookko did not give you a proper name?"
                "The caretaker ponders for a moment, you could see a hint of confusion in his eyes."
                snow_caretaker "But I am not who was important to Ookko, the plant was all he needed."
                snow_caretaker "I was spawned along with the plant, but I am not the plant. I am merely the caretaker."
                e "Can I just call you '{i}big fuzzy guy{/i}' or something?"
                snow_caretaker "No."
                "The response was rather quick, compared to his usual calculated speech."
                e "Okay, fair. I'm [e], by the way."
                snow_caretaker "Very well, [e]. You may take the plant, but know that, you are now bound to Ookko's garden."
                "You nod, and the creature steps back, he kneels before you as he bends his head down, allowing you to see the entirety of the plant."
                "His large claws brush against the leaves, and you can see the plant's roots are intertwined with the caretaker's fur."
                "You watch as the caretaker trims down the plant, carefully removing a few leaves, and placing them in your hands."
                e "Thank you. I appreciate it."
                if quest44.status == 2:
                    $ quest44.status = 3
                    $ quest44.qComp(_("Head back to Haskell"))
                $ addItem("Oolong Leaves", inventory)
                $ defeated_enemies["The Caretaker"] = "In Garden"
                "The caretaker nods, his palms graze against the remaining leaves, then stands back up, towering over you once more."
                jump Snowbound_Summit_Loop
        "Remain Silent":
            "You stand there, frozen in place as you remain silent, your heart pounding in your chest."
            my "Finally, you have returned to me, haven't you?"
            "The creature's eyes widen, and it takes a step forward, its massive form looming over you."
            my "It has been... perhaps centuries since you left. I thought you would never return."
            "You take a step back, waving your arms in front of the creature, but his eyes never moved."
            my "Albeit... you have grown smaller. Or did I grow larger?"
            "He takes another step forward, and you feel the ground shake beneath you."
            my "I will quiet down for now. M'lord. But know that I am keen to tend to the garden again."
            "The creature turns his back to you, he walks towards the edge of the summit once more, staring into the distance."
            "It doesn't seem to notice you, or your lack of response, perhaps he is quite used to it."
            menu:
                "What should you do now?"
                "Move away from the creature":
                    "You take a step back, trying to put some distance between you and the creature."
                    "The creature turns its head slightly, its eyes narrowing as it watches you."
                    my "Ookko...?"
                    "You take another step back, and the creature's eyes widen in surprise."
                    my "How did you... Who are you? Your scent deceived me."
                    e "I-"
                "Try to harvest the Oolong":

                    "You reach up for the plant, and as your fingers brush against the leaves, the creature's eyes widen in surprise."
                    my "Wait... what are you doing? You are no- Who are you?"
                    "The creature seems to have sensed your presence, and it takes a step back."
                    my "You are mere mortal. How did you enter Ookko's domain?"
                    "You freeze, your heart pounding in your chest as you try to think of a response."
            my "It does not matter, you are an intruder..."
    "With a roar, the creature lunges forward, its claws outstretched, and you barely manage to dodge out of the way."
    snow_caretaker "Face me, mortal. For I am the Caretaker of this garden, and you will not enter Ookko's garden without a fight!"

    jump caretaker_battle

image slushy_sprite:
    "slushy_sprite02"
    pause 0.3
    "slushy_sprite_loop"

image slushy_sprite_loop:
    "slushy_sprite03"
    pause 0.3
    "slushy_sprite01"
    pause 0.4
    repeat

image slushy_sprite up:
    xzoom -1
    "slushy_sprite"

image slushy_sprite down:
    "slushy_sprite"

image slushy_sprite left:
    xzoom -1
    "slushy_sprite"


image slushy_sprite right:
    "slushy_sprite"

label Chilly_Ice_Cave:

    $ bearguard_dialogues.setdefault("Chilly Ice Cave", {})
    $ cave_returning_from_crypt = bearguard_dialogues["Chilly Ice Cave"].pop("From Crypt", False)

    $ ice_cave_map = {"None": 0, "cave_wall": 1, "cave_wall_top": 2, "Back:cave_floor01": 3, 
    "empty": 4, "Back:cave_floor02": 5, "cave_ice_pillar": 6, "cave_pillar01": 7}
    $ ice_cave_floor = {"cave_ice01": 10, "cave_ice02": 8, "cave_ice03": 7, "cave_ice04": 5, "cave_ice05": 3, "cave_ice06": 1, "cave_ice07": 1, "cave_ice08": 1}
    $ dungeon_timers = []
    $ enct = None
    if cave_returning_from_crypt:
        $ cave_entry_x = 23
        $ cave_entry_y = 27
    else:
        $ cave_entry_x = 1
        $ cave_entry_y = 7

    $ chilly_ice_cave = MapPat([], "Chilly Ice Cave", cave_entry_x, cave_entry_y, ice_cave_floor, background = "chilly_ice_cave")

    $ chilly_ice_cave.floorPlan([
    [4, 4, 4, 4, 6, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [4, 4, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [4, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 2, 0, 2, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 5, 5, 0, 2, 2, 2, 1, 1, 1, 1],
    [1, 1, 1, 1, 2, 2, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 2, 2, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 5, 2, 1],
    [2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 2, 1, 1],
    [3, 3, 3, 3, 0, 0, 0, 0, 0, 7, 7, 0, 6, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 1, 1],
    [2, 1, 1, 1, 1, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [4, 2, 1, 1, 1, 3, 3, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 2],
    [4, 4, 2, 2, 1, 3, 3, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 5, 1, 1, 2],
    [4, 4, 4, 4, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [4, 4, 4, 1, 1, 1, 1, 1, 0, 1, 1, 1, 2, 0, 2, 1, 0, 1, 1, 1],
    [4, 4, 1, 2, 2, 1, 1, 2, 0, 2, 2, 2, 0, 0, 0, 2, 0, 2, 1, 1, 1],
    [4, 4, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 5, 0, 0, 0, 0, 7, 0, 5, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 5, 5, 0, 0, 0, 6, 0, 5, 5, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 7, 6, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 2, 0, 2, 0, 0, 0, 0, 0, 0, 7, 7, 0, 0, 2, 2, 2, 1, 1, 1],
    [1, 1, 1, 1, 3, 3, 3, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 1],
    [1, 1, 1, 1, 3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 3, 2, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 2, 0, 0, 2, 2, 2, 0, 2, 1, 1, 1, 0, 1, 1, 1, 1, 0, 2, 0, 1, 1, 1],
    [1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 0, 1, 2, 2, 1, 0, 0, 0, 1, 0, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 2, 2, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 1],
    [1, 0, 0, 5, 0, 0, 6, 1, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 1],
    [1, 0, 0, 5, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 5, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2],
    [4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        ], ice_cave_map)
    $ addFrontQuick(chilly_ice_cave, 12, 2, "cave_wall_top", 120, 120, "None")
    $ addFrontQuick(chilly_ice_cave, 12, 1, "cave_wall", 120, 120, "None")
    $ addFrontQuick(chilly_ice_cave, 11, 1, "cave_wall", 120, 120, "None")
    $ addFrontQuick(chilly_ice_cave, 10, 1, "cave_wall", 120, 120, "None")
    $ addFrontQuick(chilly_ice_cave, 9, 1, "cave_wall", 120, 120, "None")
    $ addFrontQuick(chilly_ice_cave, 8, 1, "cave_wall", 120, 120, "None")
    $ addFrontQuick(chilly_ice_cave, 7, 1, "cave_wall_top", 120, 120, "None")
    $ addFrontQuick(chilly_ice_cave, 6, 1, "cave_wall_top", 120, 120, "None")
    $ addFrontQuick(chilly_ice_cave, 5, 19, "cave_wall_top", 120, 120, "None")
    $ addFrontQuick(chilly_ice_cave, 5, 18, "cave_wall", 120, 120, "None")
    $ addFrontQuick(chilly_ice_cave, 4, 18, "cave_wall", 120, 120, "None")
    $ addFrontQuick(chilly_ice_cave, 4, 17, "cave_wall", 120, 120, "None")
    $ addFrontQuick(chilly_ice_cave, 21, 23, "cave_wall", 120, 120, "None")
    $ addFrontQuick(chilly_ice_cave, 21, 24, "cave_wall_top", 120, 120, "None")
    if "Slushy1" not in defeated_enemies:
        $ slushy_sprite01 = MapLooker(8, 26, "slushy_sprite down", 120, 120, "Slushy1", [["Right", 4], ["Down", 2], ["Left", 4], ["Up", 2]], 1, "slushy_sprite")
        $ addSprite(chilly_ice_cave, slushy_sprite01)
    if "Slushy2" not in defeated_enemies:
        $ slushy_sprite02 = MapLooker(16, 17, "slushy_sprite left", 120, 120, "Slushy2", [["Left", 4], ["Up", 2], ["Right", 4], ["Down", 2]], 1, "slushy_sprite")
        $ addSprite(chilly_ice_cave, slushy_sprite02)
    if "Slushy3" not in defeated_enemies:
        $ slushy_sprite03 = MapLooker(5, 25, "slushy_sprite left", 120, 120, "Slushy3", [["Left", 3], ["Down", 2], ["Right", 3], ["Up", 2]], 1, "slushy_sprite")
        $ addSprite(chilly_ice_cave, slushy_sprite03)
    if "Slushy4" not in defeated_enemies:
        $ slushy_sprite04 = MapLooker(18, 8, "slushy_sprite up", 120, 120, "Slushy4", [["Up", 3], ["Left", 2], ["Down", 3], ["Right", 2]], 1, "slushy_sprite")
        $ addSprite(chilly_ice_cave, slushy_sprite04)

    if daggi_accompany and not bearguard_dialogues["Chilly Ice Cave"].get("Rockfall", False):
        scene chilly_ice_cave with dissolve
        bearGuard "Commander, we've checked this cave out before, it was empty... except a few slushies. But we can take a quick look again."
        "A bear guard stomps the ground with his harpoon, causing a loud rumbling."
        d "Quiet. I don't think this place is empty."
        "The four of you only make it a few strides into the cave before a pale shape whips between the ice pillars ahead."
        bearGuard "Contact!"
        "One of the guards hurls his harpoon on instinct. The barbed head bites deep into a frost-sheathed column, with a crack that sounds like bones splitting."
        "For a heartbeat, everything holds. Then the ceiling above the entrance gives."
        with vpunch
        "Rocks and old frozen debris crash down behind you in a thunder of stone, sealing the cave mouth in a burst of white dust and shattered ice."
        bearGuard "Commander! The exit!"
        "Daggi and both guards throw themselves against the fallen rubble, but the larger slabs barely shift."
        d "Enough. Stop. You'll only bury yourselves deeper."
        bearGuard "We'll keep working it, Commander."
        d "Do that. Hold the entrance, clear what you can, and shout if anything moves behind us."
        "He turns to you, jaw set, one hand still tight on his harpoon shaft."
        d "Stay with me, [e]. Whatever caused that is still in here, and I would rather not lose sight of you too."
        $ bearguard_dialogues["Chilly Ice Cave"]["Rockfall"] = True
        $ bearguard_dialogues["Chilly Ice Cave"]["Alone"] = False
        $ cave_exit01 = MapUser(0, 7, "cave_rockfall", 120, 180, "Rockfall")
    elif quest47.status == True:
        if not bearguard_dialogues["Chilly Ice Cave"].get("Post Quest Cave Intro", False):
            scene chilly_ice_cave with dissolve
            "The cave mouth lies open again, the earlier collapse long since cleared away."
            "Only the cold drip of meltwater and the scrape of your own steps answer you now; whatever urgency once haunted this place is gone."
            $ bearguard_dialogues["Chilly Ice Cave"]["Post Quest Cave Intro"] = True
        $ cave_exit01 = MapUser(0, 7, "cave_exit", 120, 120, "Exit")
    elif not daggi_accompany and not bearguard_dialogues["Chilly Ice Cave"].get("Alone", False):
        scene chilly_ice_cave with dissolve
        if herd_dead:
            "A cold draft rolls up from deeper inside, followed by a heavy scrape of stone."
            e "No. Daggi needs to see this."
            "Whatever is hiding in the cave, this is no longer the kind of thing you should handle alone."
            "You back out of the cave."
            jump main_clawridge_ascent

        "The cave swallows the outside wind almost at once, replacing it with a muffled stillness broken only by the drip of melting water and the grind of your boots over frost."
        if bearguard_dialogues["Chilly Ice Cave"].get("Chief Sent Daggi", False):
            "The mouth of the cave is still empty, you reckon Chief and Daggi are still waiting for you."
        "Without anyone nearby, the ice pillars feel taller, the shadows between them deeper, and every pale patch of frost makes your shoulders tense."
        e "So this is the cave that guard talked about."
        "Somewhere deeper in the cave, something wet slides across stone and then goes quiet."
        e "Someone should be here."
        $ bearguard_dialogues["Chilly Ice Cave"]["Alone"] = True
        $ daggi_accompany = False
        $ cave_exit01 = MapUser(0, 7, "cave_exit", 120, 120, "Exit")
    else:
        $ cave_exit01 = MapUser(0, 7, "cave_exit", 120, 120, "Exit")

    $ addSprite(chilly_ice_cave, cave_exit01)
    $ cave_stairs1 = MapUser(23, 24, "cave_stairs", 120, 120, "Stairs")
    $ cave_stairs2 = MapUser(23, 25, "cave_stairs", 120, 120, "Stairs")
    $ cave_stairs3 = MapUser(23, 26, "cave_stairs", 120, 120, "Stairs")
    $ cave_pot1 = MapUser(20, 25, "puro_pot_sprite01", 120, 120, "Pot")
    if "Ice_Cave_Chest01" not in opened_chests:
        $ ice_cave_chest01 = MapUser(4, 1, "crypt_chest01", 120, 120, "Ice_Cave_Chest01")
    else:
        $ ice_cave_chest01 = MapUser(4, 1, "crypt_chest02", 120, 120, "Ice_Cave_Chest01")
    if "Ice_Cave_Chest02" not in opened_chests:
        $ ice_cave_chest02 = MapUser(3, 15, "crypt_chest01", 120, 120, "Ice_Cave_Chest02")
    else:
        $ ice_cave_chest02 = MapUser(3, 15, "crypt_chest02", 120, 120, "Ice_Cave_Chest02")
    if "Ice_Cave_Chest03" not in opened_chests:
        $ ice_cave_chest03 = MapUser(21, 21, "crypt_chest01", 120, 120, "Ice_Cave_Chest03")
    else:
        $ ice_cave_chest03 = MapUser(21, 21, "crypt_chest02", 120, 120, "Ice_Cave_Chest03")
    $ addSprite(chilly_ice_cave, ice_cave_chest01)
    $ addSprite(chilly_ice_cave, ice_cave_chest02)
    $ addSprite(chilly_ice_cave, ice_cave_chest03)
    $ addSprite(chilly_ice_cave, chilly_ice_cave.playerSprite)
    $ addSprite(chilly_ice_cave, cave_stairs1)
    $ addSprite(chilly_ice_cave, cave_stairs2)
    $ addSprite(chilly_ice_cave, cave_stairs3)
    $ chilly_ice_cave.updateFloor(ice_cave_floor)
    $ chilly_ice_cave.slippery_floor_prefixes = ("cave_ice",)
    $ chilly_ice_cave.autoMoveLookers()

    $ current_location = chilly_ice_cave
    jump Chilly_Ice_Cave_Loop

label Chilly_Ice_Cave_Loop:
    $ renpy.music.play(mOpen1, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ disableC = False
    $ sprite = chilly_ice_cave.playerSprite
    $ update_chilly_ice_cave_fronts(chilly_ice_cave)
    show screen dungeon_buttons()
    call screen dungeon_map(chilly_ice_cave)
    show screen dungeon_map(chilly_ice_cave)
    if isinstance(_return, tuple) and not disableC:
        $ tenki_moving = False
        if len(_return) == 3 and _return[0] == "Slide":
            $ chilly_ice_cave.continuePlayerSlide(_return[1], _return[2])
        elif len(_return) == 2:
            if len(dungeon_timers) > 0:
                $ dungeon_timers.pop(0)
            $ chilly_ice_cave.autoMoveLookers()
    else:
        $ disableC = True

    if _return == "Rockfall":
        "From the far side of the rubble, you hear the muffled strain of the guards shifting stone by hand."
        bearGuard "Almost got this one, keep it up!"
        d "They're still at it. Good."

    if _return == "Exit":
        "The open mouth of the cave lets in a blade of white daylight and the cleaner scent of snow outside."
        menu:
            "Leave the cave?"
            "Step back out into the open":
                "You back away from the freezing dark and retrace your path down the ridge, leaving the cave behind for now."
                hide screen dungeon_map
                jump main_clawridge_ascent
            "Stay inside":
                pass

    if _return == "Stairs":
        if quest47.status == True:
            "The cut stone stairs descend back toward the crypt below. The panic and scrambling from before are gone; only cold air rises to meet you."
        elif daggi_accompany and not bearguard_dialogues["Chilly Ice Cave"].get("Stairs Talk", False):
            $ bearguard_dialogues["Chilly Ice Cave"]["Stairs Talk"] = True
            "The cut stone stairs descend into a darker shaft below, each step rimed over with old frost that glimmers blue in the cave light."
            e "These were carved, weren't they? This isn't just a natural tunnel."
            d "No. Old burial stairs, if the stories are true. The tribe sealed the lower crypt and stopped coming here long before I was born."
            e "And now the noises are coming from down there."
            d "Most likely."
            "Daggi plants the butt of his harpoon against the stone and studies the dark below in silence for a moment."
            d "Let's check the chamber below first. If something is moving down there, I don't want it coming up behind us while we're staring into the dark."
            e "You really think the guards can clear the way in time?"
            d "I don't know. But if they cannot, then you and I will find another exit."
        elif not daggi_accompany and not bearguard_dialogues["Chilly Ice Cave"].get("Met Herd Alone", False):
            if not bearguard_dialogues["Chilly Ice Cave"].get("Stairs Alone", False):
                $ bearguard_dialogues["Chilly Ice Cave"]["Stairs Alone"] = True
                "The cut stone stairs vanish into a colder dark below, too even and deliberate to be anything but man-made."
                e "A crypt... The guard wasn't just hearing cave echoes... Right?"
                "You crouch and brush frost from the edge of the nearest step. The stone beneath is old, worn smooth by feet that haven't passed this way in a very long time."
                e "If whatever made those noises came from down there, going deeper alone would be stupid."
                "Still, the thin draft rising from below carries the same faint, wet scraping you heard near the entrance."
            else:
                "The same uneasy scrape rises from below, faint but deliberate, as if someone deeper in the crypt has heard you stop at the stairs again."
        elif not daggi_accompany and bearguard_dialogues["Chilly Ice Cave"].get("Met Herd Alone", False):
            "The old stairs lead back down toward the hidden chamber where Herd is sheltering."
        else:
            "The old stairs disappear into the dark below, carrying colder air up from whatever lies deeper in the crypt."
        menu:
            "What do you do?"
            "Go back down to Herd" if not daggi_accompany and bearguard_dialogues["Chilly Ice Cave"].get("Met Herd Alone", False) and not quest47.status == True:
                hide screen dungeon_map
                jump Chilly_Ice_Cave_Walk_Down
            "Go down into the crypt" if daggi_accompany or quest47.status == True:
                hide screen dungeon_map
                jump Chilly_Ice_Cave_Walk_Down
            "Follow the sound down into the crypt" if not daggi_accompany and not bearguard_dialogues["Chilly Ice Cave"].get("Met Herd Alone", False) and not quest47.status == True:
                hide screen dungeon_map
                jump Chilly_Ice_Cave_Walk_Down
            "Stay in the cave":
                pass

    if _return == "Ice_Cave_Chest01":
        if "Ice_Cave_Chest01" not in opened_chests:
            "You brush the frost from the chest lid and pry it open with both hands."
            "Inside, someone left two jars of green ointment packed around a lump of archaic ice to keep them cold."
            $ addItem("Green Ointment", inventory, 2)
            $ addItem("Archaic Ice", inventory, 1)
            $ opened_chests["Ice_Cave_Chest01"] = True
            $ ice_cave_chest01.img = "crypt_chest02"
        else:
            "The chest is empty now, its inside lined with a thin crust of old frost."

    if _return == "Ice_Cave_Chest02":
        if "Ice_Cave_Chest02" not in opened_chests:
            "The latch gives with a brittle snap. Beneath the lid, you find two iron ingots wrapped in old cloth beside a pair of snow berries."
            "A stone shard with a faded engraving lies at the bottom of the chest, you pick it up carefully, but it seems to be a part of a bigger figure..."
            $ addItem("Iron Ingot", inventory, 2)
            $ addItem("Snow Berry", inventory, 2)
            $ addItem("Engraved Stone Shard", inventory, 1)
            $ opened_chests["Ice_Cave_Chest02"] = True
            $ ice_cave_chest02.img = "crypt_chest02"
        else:
            "Only a little frozen cloth remains in the bottom of the open chest."

    if _return == "Ice_Cave_Chest03":
        if "Ice_Cave_Chest03" not in opened_chests:
            "You lift the heavier lid and uncover a small stash: three pieces of copper and a pair of bundled spearmint sprigs."
            "A stone shard with a faded engraving lies at the bottom of the chest, you pick it up carefully, but it seems to be a part of a bigger figure..."
            $ addItem("Copper", inventory, 3)
            $ addItem("Spearmint", inventory, 2)
            $ addItem("Engraved Stone Shard", inventory, 1)
            $ opened_chests["Ice_Cave_Chest03"] = True
            $ ice_cave_chest03.img = "crypt_chest02"
        else:
            "This chest has already been picked clean."

    if (isinstance(_return, str) and _return[:6] == "Slushy") or (isinstance(enct, str) and enct[:6] == "Slushy"):
        if isinstance(_return, str) and _return[:6] == "Slushy":
            $ current_enemy = _return
        else:
            $ current_enemy = enct
        jump Chilly_Ice_Cave_Slushy

    jump Chilly_Ice_Cave_Loop

label Chilly_Ice_Cave_Slushy:
    show screen dungeon_map(chilly_ice_cave)
    $ disableC = True
    $ enct = None
    if daggi_accompany:
        "A pale-blue slushy quivers across the ice and cuts off your path."
        d "Contact! Keep your footing, [e]!"
        "Daggi lowers his harpoon and steps up beside you as the thing surges forward in a spray of freezing gel."
    else:
        "A pale-blue slushy quivers across the ice and cuts off your path."
        "The thing surges forward in a spray of freezing gel, forcing you into a fight."
    hide screen dungeon_map
    if daggi_accompany:
        jump slushy_daggi_battle
    jump slushy_battle

label Chilly_Ice_Cave_Walk_Down:
    "You follow the stairs down until the passage opens into a round chamber half-choked with debris from the collapse."
    "The far wall is carved with a figure in a helmet, broad-shouldered and severe even under centuries of frost."
    jump Conquerors_Crypt

label Crypt_Herd_Meet_Alone:
    "A shape jerks in the corner."
    "The antlers conspicuously jut out from behind the fallen debris, though you aren't entirely sure its owner notices."
    "You slowly walk forward, hands open and visible, trying to see whose antlers hide behind the rubble."
    "It doesn't take long for you to see more of it, the brown arms wrapping around his legs, and the dark snout holding his breath, it's Herd."
    "The elk is wedged back against the wall so hard he looks like he'd climb into the stone if it would let him. His eyes are wide, his breathing ragged. One shaking hand comes up between you. Stop."
    e "Herd?"
    "Nothing changes."
    "You try again, quieter, palms open, but the sound of your voice only seems to make him brace harder."
    "You stop where you are, then sink down slowly into a crouch. Smaller. Less like a threat."
    "For a while neither of you does anything. The only noise in the chamber is his breathing and the occasional tick of stone settling overhead."

    menu:
        "What do you do next?"
        "Stay still and let him watch you":

            $ herd_trust += 1
            "You keep your hands where he can see them and do your best not to crowd him."
            "A long stretch passes before his shoulders loosen by even a fraction."
        "Offer an open hand":

            $ herd_trust += 3
            "You lift one hand a little, palm up, then stop there and let him decide what it means."
            "His gaze keeps flicking from your face to your fingers, uncertain but curious in spite of himself."

    "After a moment you try speaking again out of habit."
    e "I'm not going to hurt you."
    "He only stares."
    "You point to yourself, then toward the tunnel you came from, then shake your head."
    "Wrong move. He tenses so fast it is like you raised a weapon. You almost answer him aloud again before it finally lands."
    "When the chamber gives a low, dull groan, Herd reacts before you do. His palm is already on the floor, feeling the tremor through the stone."
    "He watches your hands, your shoulders, the set of your body, the way your breath catches."
    "You touch your throat, then shake your head and point gently toward him."
    "That gets through. Not a lot, but enough for him to understand."

    menu:
        "Herd stares at you."
        "Tap your chest and mouth your name":
            $ herd_trust += 1
            "You tap your chest."
            e "[e]."
            "Then you do it again, slower, making the shape of the word obvious even if it means nothing on its own."
        "Write your name in the dust":

            $ herd_trust += 3
            "You drag a finger through the dust at your feet, write your name, then tap your chest."

    "Herd watches the whole sequence, then presses a fist to his own chest. He does it again, firmer this time."
    "You point to him."
    e "Herd."
    "That, at least, seems right. You catch a glimpse of a smile in the perpetual frown."
    "The rest is rough going."
    "You point to yourself. He points to himself. You point to the stairs. He answers with a quick motion you don't understand, and when you guess wrong and shift forward, he knocks one antler against the wall trying to get away from you."
    "You frown trying to figure out where you went wrong."
    "He studies you for another long moment before trying again."
    "This time he keeps it simpler. A tap to the chest for himself. Two fingers flicked toward you. Flat palm for stop. Open hand for safe. A sharp cut of the wrist for no."
    "You still miss some of it. He still has to repeat himself. But he does, patient in the way of someone who has spent a long time being misread."
    "Once he realizes you will keep trying, he reaches down and smooths a patch of dust flat with the side of his hand. The movement is neat, practiced."
    "Then he starts drawing."
    "His fingers move quickly now. Lines for walls. Marks for breaks in the stone. Chips of rubble set down and moved aside to stand in for corners and turns."
    "This, more than anything, makes the man in front of you look like Herd the builder people kept talking about. Even cornered and half-starved with fear, his mind goes straight to structure."

    "Then his hand flies to the snapped cord at his wrist."
    "He looks down at it, then at the floor, then back at you with a flash of raw frustration."
    "You point to the cord and raise your brows."
    "He drops back to the dust and draws hard enough to leave deep grooves in it."
    "First the cave mouth collapsing. Then a small antler-work astrolabe tumbling into a crack below."
    "After that he sketches only a rough line of older stone beyond the collapse."
    e "It's the thing you're looking for?"
    "You trace the falling relic with one finger, then point down the passage."
    "He nods, quick and tight."
    "You spread your hands toward the deeper crypt in a question. Herd gives a small, irritated shrug and redraws the astrolabe bigger than everything else on the floor."
    "Fine. Point taken."
    e "So, it should be somewhere here?"
    "You tap your own chest, mime searching below, then mime lifting something small and handing it back."
    "He watches your hands so closely it feels like standing under a blade."
    "You do it again. Slower."
    "This time he lets out a breath and nods."
    "Maybe that's what it takes to be the bear tribe's greatest architect, but you still don't understand why he fears the tribe so much now."
    "When you mime the guards above and shake your head, he keeps looking at you for so long that you almost think you've lost him again."
    "Then he moves one hand over and sets it beside yours on the floor."
    "Before you can rise, Herd reaches into a narrow crack between two stones and pulls out a little bell no bigger than your palm, rigged with careful wire and a bone tongue."
    "He gives it a light shake, then immediately presses it into your hand so you can feel the thin buzzing vibration running through the metal."
    "Next he points to his broken ear, bares his teeth in frustration, and shakes his head. Deaf. Or near enough that the chime means little to him."
    "He taps the bell again, points deeper into the crypt, then drags one finger in a slow line through the dust until it stops over a crack in the drawn floorplan."
    "The message is clumsy but clear enough: the bell helps track the astrolabe, but only if someone can judge the sound better than he can."
    e "You want me to use this to find it?"
    "Herd nods once, sharp and immediate. He sets the detector where you can reach it easily, then retreats back toward the wall to watch."
    e "Alright, I'll look for it."
    "Before you stand, his hand catches your wrist for a second. Just long enough to make sure you look at him."
    "When he lets go, you nod with a smile he can surely see."

    $ bearguard_dialogues["Chilly Ice Cave"]["Met Herd Alone"] = True
    $ bearguard_dialogues["Chilly Ice Cave"]["Herd Lost Item"] = True
    $ bearguard_dialogues["Chilly Ice Cave"]["Bell Ready"] = True
    $ quest47.qComp(_("Search the crypt"))

    hide herd with dissolve
    scene chilly_ice_cave with dissolve
    jump Conquerors_Crypt_Loop

label Crypt_Herd_Return_Keepsake:
    show herds astrolabe:
        xalign 0.5
        yalign 0.5
    "Herd sees the astrolabe in your hand and goes perfectly still."
    "When you hold it out, he snatches it with both hands and closes his fingers around it so tightly the knuckles pale under the fur."
    "For a moment he does nothing but breathe with it pressed to his chest. The panic that has been living in his shoulders since you found him loosens by a degree."
    "He bows his head over it, eyes shut, as if feeling its weight alone is enough to steady him."
    hide herds astrolabe
    if conquerors_crypt.inventory != None and conquerors_crypt.inventory.interaction == "Astrolabe":
        $ conquerors_crypt.inventory = None
    $ bearguard_dialogues["Chilly Ice Cave"]["Crypt Held Item"] = None

    $ bearguard_dialogues["Chilly Ice Cave"]["Herd Lost Item Found"] = True
    $ bearguard_dialogues["Chilly Ice Cave"]["Returned Herd Lost Item"] = True
    $ bearguard_dialogues["Chilly Ice Cave"]["Crypt Statue Battle Ready"] = True
    with vpunch
    "A harsh scrape rolls through the crypt before either of you can settle."
    "Herd jerks around and points toward the front of the chamber, eyes wide."
    "Both guardian statues are moving, grinding off their bases in sprays of frost."

    jump Crypt_Statues_Awaken

label Conquerors_Crypt:



    $ crypt_map = {"None": 0, "crypt_top": 1, "crypt_wall01": 2, "crypt_wall02": 3, "crypt_wall03": 4, "Back:cave_floor01": 5, "Back:crypt_gutter": 6, "Back:crypt_gutter02": 7, "Back:crypt_gutter03": 8, "Back:cave_stairs": 9}
    $ crypt_floor = {"crypt_floor": 15, "crypt_floor02": 2, "crypt_floor03": 2, "crypt_floor04": 1}
    $ dungeon_timers = []
    $ enct = None
    $ cave_state = bearguard_dialogues["Chilly Ice Cave"]
    $ crypt_entry_x = 7
    $ crypt_entry_y = 19

    if daggi_accompany and not cave_state.get("Daggi Crypt Intro", False):
        scene chilly_ice_cave with dissolve
        if herd_dead:
            "The moment you and Daggi step off the stairs, a knife-thin gust slips through the crypt and combs loose frost across the floor."
            "It whispers past the side tombs and sends grains of grit skittering over the stone before something ahead answers with a low grind."
            "You both turn at once. Frost sifts from one sealed lid, then the chamber stills again. Four side tombs sit in the cold, all closed."
            d "I heard that."
            e "Yeah. And that wind wasn't coming from the stairs."
            d "No. It wasn't."
            d "I felt it through the floor too. Old places like this shift when the cold loosens, but... not usually like that."
        else:
            "The moment you and Daggi step off the stairs, stone grates somewhere in the dark ahead."
            "You both turn at once, but the chamber has already gone still again. Four side tombs sit in the frost, all closed."
            d "I heard that."
            e "You heard that too?"
            d "I felt it through the floor too. Old places like this shift when the cold loosens, but I don't think that was only the cold."
        "He circles the old offering table instead, then pauses over a little bell left on the stone beside it. A few careful wire wraps hold the clapper in place."
        if herd_dead:
            d "This wasn't buried here. I know that join work. Herd made this."
            e "But Herd's dead."
            d "Then he must have been here before he died. I just... I don't know why."
        else:
            d "This wasn't buried here. I know that join work. Herd made this."
            e "You can tell from this?"
            d "Yes. He always worked neatly, even when he was in a hurry. If he came down here, he came for a reason."

        $ cave_state["Herd Lost Item"] = True
        $ cave_state["Bell Ready"] = True
        $ quest47.qComp(_("Search the crypt"))
        $ cave_state["Daggi Crypt Intro"] = True

    $ conquerors_held_item = cave_state.get("Crypt Held Item", None)
    $ conquerors_crypt = MapPat([], "Conquerors Crypt", crypt_entry_x, crypt_entry_y, crypt_floor)

    $ conquerors_crypt.floorPlan([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 4, 4, 3, 2, 3, 2, 3, 4, 4, 1, 1, 1],
    [1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 1],
    [1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [8, 8, 8, 8, 8, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8],
    [1, 0, 0, 0, 0, 6, 0, 0, 0, 6, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 6, 0, 0, 0, 6, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 6, 0, 0, 0, 6, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 9, 9, 1, 1, 1, 9, 9, 1, 1, 1, 1],
    [1, 1, 4, 4, 9, 9, 2, 3, 2, 9, 9, 4, 4, 1, 1],
    [1, 1, 0, 0, 0, 6, 0, 0, 0, 6, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 6, 0, 0, 0, 6, 0, 0, 0, 4, 1],
    [1, 1, 0, 0, 0, 6, 0, 0, 0, 6, 0, 0, 0, 5, 1],
    [1, 4, 0, 0, 0, 6, 0, 0, 0, 6, 0, 0, 0, 5, 1],
    [1, 5, 0, 0, 0, 6, 0, 0, 0, 6, 0, 0, 5, 5, 1],
    [1, 5, 0, 0, 0, 6, 0, 0, 0, 6, 0, 0, 0, 1, 1],
    [1, 5, 1, 0, 0, 6, 0, 0, 0, 6, 0, 0, 1, 1, 1],
    [1, 0, 1, 5, 5, 1, 5, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 5, 4, 1, 0, 1, 4, 1, 1, 1, 1, 1],
    [4, 4, 4, 4, 1, 6, 4, 0, 4, 6, 4, 4, 4, 4, 4],
        ], crypt_map)

    $ addBackQuick(conquerors_crypt, 5, 6, "crypt_gutter02", 120, 120, "Gutter2")
    $ addBackQuick(conquerors_crypt, 9, 6, "crypt_gutter05", 120, 120, "Gutter2")
    if cave_state.get("Crypt Gutter Opened", False):
        $ addBackQuick(conquerors_crypt, 9, 16, "crypt_gutter04", 120, 120, "Gutter")
    else:
        $ addBackQuick(conquerors_crypt, 9, 16, "crypt_gutter", 120, 120, "Gutter")
    $ crypt_tomb1 = MapUser(3, 14, "crypt_tomb", 120, 180, "Tomb")
    $ crypt_tomb2 = MapUser(3, 17, "crypt_tomb", 120, 180, "Tomb")
    $ crypt_tomb3 = MapUser(11, 14, "crypt_tomb", 120, 180, "Tomb")
    $ crypt_tomb4 = MapUser(11, 17, "crypt_tomb", 120, 180, "Tomb")
    $ addSprite(conquerors_crypt, crypt_tomb1)
    $ addSprite(conquerors_crypt, crypt_tomb2)
    $ addSprite(conquerors_crypt, crypt_tomb3)
    $ addSprite(conquerors_crypt, crypt_tomb4)

    $ crypt_conquerors_tomb = MapUser(7, 8, "crypt_conquerors_tomb", 150, 180, "Conquerors Tomb")
    $ addSprite(conquerors_crypt, crypt_conquerors_tomb)
    $ addSpriteQuick(conquerors_crypt, 3, 4, "crypt_pillar01", 120, 150, "Pillar")
    $ addSpriteQuick(conquerors_crypt, 3, 8, "crypt_pillar01", 120, 150, "Pillar")
    $ addSpriteQuick(conquerors_crypt, 11, 8, "crypt_pillar01", 120, 150, "Pillar")
    $ addSpriteQuick(conquerors_crypt, 11, 4, "crypt_pillar03", 120, 120, "Pillar")

    $ addSpriteQuick(conquerors_crypt, 2, 12, "crypt_pillar03", 120, 120, "Pillar")
    $ addSpriteQuick(conquerors_crypt, 13, 14, "crypt_pillar03", 120, 120, "Pillar")
    $ addSpriteQuick(conquerors_crypt, 3, 2, "crypt_statue", 120, 180, "Statue")
    $ addSpriteQuick(conquerors_crypt, 4, 2, "empty")
    $ addSpriteQuick(conquerors_crypt, 10, 2, Transform("crypt_statue", xzoom = -1.0), 120, 180, "Statue")
    $ addSpriteQuick(conquerors_crypt, 11, 2, "empty")
    $ addSpriteQuick(conquerors_crypt, 7, 5, "crypt_table", 150, 180, "Table")
    $ addSpriteQuick(conquerors_crypt, 8, 5, "empty")
    $ addSpriteQuick(conquerors_crypt, 6, 5, "empty")
    $ addFrontQuick(conquerors_crypt, 1, 19, "crypt_top")

    $ addSpriteQuick(conquerors_crypt, 13, 5, "crypt_debris01", 120, 120, "Debris")
    $ addSpriteQuick(conquerors_crypt, 1, 6, "crypt_debris01", 120, 120, "Debris")
    $ addSpriteQuick(conquerors_crypt, 2, 9, "crypt_debris02", 120, 120, "Debris")
    $ addSpriteQuick(conquerors_crypt, 6, 13, "crypt_debris01", 120, 120, "Debris")
    $ addSpriteQuick(conquerors_crypt, 12, 12, "crypt_debris02", 120, 120, "Debris")
    $ addSpriteQuick(conquerors_crypt, 7, 21, "cave_stairs", 120, 120, "Stairs")

    if cave_state.get("Crypt Detector Dropped At", None) != None and conquerors_held_item != "Detector":
        $ detector_x, detector_y = cave_state["Crypt Detector Dropped At"]
        $ addSprite(conquerors_crypt, MapUser(detector_x, detector_y, "surveying_bell", 100, 100, "Detector"))

    if cave_state.get("Crypt Chisel At", None) != None and conquerors_held_item != "Ceremonial Chisel":
        $ chisel_x, chisel_y = cave_state["Crypt Chisel At"]
        $ addSprite(conquerors_crypt, MapUser(chisel_x, chisel_y, "small_chisel", 100, 100, "Ceremonial Chisel"))

    if conquerors_held_item == "Detector":
        $ conquerors_crypt.inventory = MapUser(0, 0, "surveying_bell", 100, 100, "Detector")
    elif conquerors_held_item == "Ceremonial Chisel":
        $ conquerors_crypt.inventory = MapUser(0, 0, "small_chisel", 100, 100, "Ceremonial Chisel")
    elif conquerors_held_item == "Astrolabe":
        $ conquerors_crypt.inventory = MapUser(0, 0, "herds astrolabe", 100, 100, "Astrolabe")

    $ addSprite(conquerors_crypt, conquerors_crypt.playerSprite)
    $ conquerors_crypt.updateFloor(crypt_floor)
    $ conquerors_crypt.slippery_floor_prefixes = ("cave_ice",)

    if daggi_accompany:
        $ addSpriteQuick(conquerors_crypt, 5, 4, Transform("daggi_hover", zoom=0.5), 150, 180, "Daggi")
    elif not quest47.status == True:
        $ addSpriteQuick(conquerors_crypt, 5, 4, "herd_sprite", 150, 180, "Herd")

    $ current_location = conquerors_crypt
    if quest47.status == True and not cave_state.get("Post Quest Crypt Intro", False):
        scene conquerors_crypt with dissolve
        "The crypt is still now, its old mechanisms spent and its guardians already broken."
        "Nothing waits for you here anymore except frost, stone, and whatever answers you choose to make of the place."
        $ cave_state["Post Quest Crypt Intro"] = True
    jump Conquerors_Crypt_Loop

label Conquerors_Crypt_Loop:
    $ renpy.music.play(mOpen1, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ disableC = False
    $ sprite = conquerors_crypt.playerSprite
    show screen dungeon_buttons()
    call screen dungeon_map(conquerors_crypt)
    show screen dungeon_map(conquerors_crypt)
    hide screen dungeon_buttons 
    $ cave_state = bearguard_dialogues["Chilly Ice Cave"]
    $ target_sprite = conquerors_crypt.locateSpriteInFront(sprite)
    $ target_back = conquerors_crypt.locateBackInFront(sprite)

    if _return == "Stairs":
        "The stairs lead back up toward the frozen cave above."
        menu:
            "Leave the crypt?"
            "Go back to the upper cave":
                $ bearguard_dialogues["Chilly Ice Cave"]["From Crypt"] = True
                hide screen dungeon_map
                jump Chilly_Ice_Cave
            "Stay in the crypt":
                pass

    if _return == "Take Detector":
        if conquerors_crypt.inventory != None:
            "Your hands are already full. You will need to set something down before you can take the surveying bell."
        else:
            $ conquerors_crypt.takeItem(sprite, target_sprite)
            $ cave_state["Bell Claimed"] = True
            $ cave_state["Crypt Held Item"] = "Detector"
            $ cave_state["Crypt Detector Dropped At"] = None
            if daggi_accompany:
                "You pick up the surveying bell Daggi found. The clapper is weighted and tuned with strips of wire so the vibration lingers in your fingers after each shake."
                d "Herd made this to look for resonance. That does sound like him."
            else:
                "You pick up Herd's surveying bell and feel the same thin buzz he showed you a moment ago travel into your palm."
                "He watches closely, then gives a short nod when you test the weight of it."

    if _return == "Take Ceremonial Chisel":
        if conquerors_crypt.inventory != None:
            "Your hands are already full. You will need to set something down before you can take the ceremonial chisel."
        else:
            $ conquerors_crypt.takeItem(sprite, target_sprite)
            $ cave_state["Crypt Held Item"] = "Ceremonial Chisel"
            $ cave_state["Crypt Chisel At"] = None
            if daggi_accompany:
                "You take the ceremonial chisel from the floor. The bronze has been polished and etched for burial rites, but its narrow edge is still sharp enough to slide into the frozen seam around the gutter."
                d "That looks like it should work."
            else:
                "You take the ceremonial chisel from the floor. Its bronze face is etched with grave lines and old rite marks, but the narrow tip is still sturdy enough to lever stone and ice apart."
                "Herd leans forward when he sees it, then points sharply toward the gutter."

    if _return == "Drop Detector" or _return == "Drop Ceremonial Chisel":
        $ drop_x, drop_y = getFacingTile(sprite)
        if drop_y >= len(conquerors_crypt.mappy) or drop_y < 0 or drop_x >= len(conquerors_crypt.mappy[drop_y]) or drop_x < 0:
            "You can't drop it there."
        elif conquerors_crypt.isEmpty(drop_x, drop_y) and conquerors_crypt.isEmptyBack(drop_x, drop_y):
            $ drop_item = conquerors_crypt.inventory
            $ conquerors_crypt.inventory = None
            $ drop_item.x = drop_x
            $ drop_item.y = drop_y
            $ addSprite(conquerors_crypt, drop_item)
            if drop_item.interaction == "Detector":
                $ cave_state["Crypt Held Item"] = None
                $ cave_state["Crypt Detector Dropped At"] = (drop_x, drop_y)
            elif drop_item.interaction == "Ceremonial Chisel":
                $ cave_state["Crypt Held Item"] = None
                $ cave_state["Crypt Chisel At"] = (drop_x, drop_y)
        else:
            "You can't drop it here."

    if conquerors_crypt.inventory != None and conquerors_crypt.inventory.interaction == "Detector" and not _return.startswith("Take ") and _return != "Drop Detector" and _return != "Stairs":
        $ detect_x, detect_y = getFacingTile(sprite)
        $ token_distance = None
        if not cave_state.get("Herd Lost Item Found", False):
            $ token_distance = abs(detect_x - 9) + abs(detect_y - 16)
        if not cave_state.get("Crypt Debris Cache Looted", False):
            $ debris_distance = abs(detect_x - 12) + abs(detect_y - 12)
            if token_distance == None or debris_distance < token_distance:
                $ token_distance = debris_distance
        if not cave_state.get("Crypt Statue Cache Looted", False):
            $ statue_distance = abs(detect_x - 3) + abs(detect_y - 2)
            if token_distance == None or statue_distance < token_distance:
                $ token_distance = statue_distance

        if token_distance == None or token_distance >= 9:
            "You give the bell a careful shake. Only a dull little tremor answers your hand. Whatever it is tuned to, it is nowhere near here."
        elif token_distance >= 6:
            "A faint answering hum lingers in the bell after you ring it. The signal is weak, but stronger than silence."
        elif token_distance >= 3:
            "The chime carries more clearly here. The bell's vibration settles into your fingers with enough force that you know you are closing in."
        elif token_distance >= 1:
            "The bell chatters hard against your palm, bright and insistent. Whatever it is tracking has to be close now."
        elif not cave_state.get("Herd Lost Item Found", False) and detect_x == 9 and detect_y == 16:
            if not cave_state.get("Crypt Chisel Found", False):
                "The instant you angle the bell over the gutter, the metal thrums so sharply it almost jumps in your grip."
                show herds astrolabe:
                    xalign 0.5
                    yalign 0.5
                "Looking down into the ice-choked channel, you finally spot Herd's astrolabe jammed deep between old grit and frozen runoff."
                if daggi_accompany:
                    "Daggi leans in beside you, his shoulder nearly brushing yours as he follows the line of the bell's pull into the gutter."
                    d "There. That's it. Has to be what he came here for."
                    e "I can see it, but I can't get fingers around it."
                    d "Then we need something narrow. If this place has any tools left in it, they'll be in the side tombs."
                elif quest47.status != True:
                    "Herd drops into a crouch beside you, sees where you are pointing, and bares his teeth in frustrated agreement."
                    "He mimes wedging something thin into the seam, then jerks his hand upward. A tool."
                hide herds astrolabe
            else:
                "The bell thrums over the gutter again. Whatever is down there is still lodged fast in the ice."
        elif not cave_state.get("Crypt Debris Cache Looted", False) and detect_x == 12 and detect_y == 12:
            "The bell gives a hard, uneven buzz here. Something hidden is tucked away under the rubble."
        elif cave_state.get("Crypt Statue Battle Won", False) and not cave_state.get("Crypt Statue Cache Looted", False) and detect_x == 3 and detect_y == 2:
            "The bell jitters wildly here. Something is lodged inside the broken guardian."
        else:
            "The bell hums in your hand, but the signal slips oddly through the stone here and doesn't show you anything yet."

    if _return == "Herd":
        if not daggi_accompany and not cave_state.get("Met Herd Alone", False):
            hide screen dungeon_map
            scene conquerors_crypt with dissolve
            show herd_normal with dissolve
            jump Crypt_Herd_Meet_Alone
        elif cave_state.get("Herd Lost Item Found", False) and not cave_state.get("Returned Herd Lost Item", False):
            hide screen dungeon_map
            scene conquerors_crypt with dissolve
            show herd_normal with dissolve
            jump Crypt_Herd_Return_Keepsake
        elif not cave_state.get("Crypt Chisel Found", False):
            if conquerors_crypt.inventory == None or conquerors_crypt.inventory.interaction != "Detector":
                "Herd looks from you to the surveying bell, then taps two fingers against his ear with an annoyed little huff through his nose."
                "Then he points down toward the old runoff channel and gives you a quick, encouraging nod."
            else:
                "Herd watches the bell in your hand, then crouches and drags a quick line through the dust to mark the gutter's path."
                "He taps the deepest part of the channel, pantomimes a small shake of the bell, then glances up to make sure you're following."
                "When you nod, he answers with a small nod of his own and taps the runoff line one more time."
        elif not cave_state.get("Herd Lost Item Found", False):
            if conquerors_crypt.inventory != None and conquerors_crypt.inventory.interaction == "Ceremonial Chisel":
                "Herd drops into a crouch beside you and acts the whole thing out with exaggerated care, like he's making sure you can laugh at how obvious it is."
                "One hand becomes the gutter seam, the other drives an invisible chisel into the crack and twists upward."
                "He looks up at you at the end, brows raised, then points toward the channel with a small, eager flick of his fingers."
            elif cave_state.get("Crypt Chisel Found", False):
                "Herd points first at the ceremonial chisel, then at the gutter, then curls his fingers as if levering something free."
                "When you look back at him, he gives a quick nod and lightly taps your arm, almost pleased that you've found what you need."
            else:
                "Herd crouches beside you and sketches the gutter, then marks the lodged astrolabe with a quick jab of his finger."
                "After that he pauses and scans the crypt with you, eyes moving from the table to the rubble to the sealed tombs before he mimes a thin wedge prying upward."
                "When you follow his gaze around the chamber, he gives a small nod. Somewhere in here, there has to be a tool narrow enough to free it."

    if _return == "Daggi":
        if not cave_state.get("Crypt Chisel Found", False):
            if conquerors_crypt.inventory == None or conquerors_crypt.inventory.interaction != "Detector":
                "Daggi glances from your empty hands to the little surveying bell and then back toward the old runoff channel."
                e "You really think a bell is going to find it?"
                "He reaches out and stills the clapper with one thumb, as if testing the thing in his head before he answers."
                d "Herd wouldn't have built it for nothing."
                d "Take the surveying bell first."
                d "If Herd tuned it for the astrolabe, it should lead us where it is."
            else:
                "Daggi listens to the last faint vibration fade from the bell in your hand, his eyes fixed on the channel cutting across the floor."
                e "And when the sound changes?"
                d "Then we stop guessing."
                d "Keep sounding the bell near the runoff channel."
                d "The resonance should sharpen when you're close."
        elif not cave_state.get("Herd Lost Item Found", False):
            if conquerors_crypt.inventory != None and conquerors_crypt.inventory.interaction == "Ceremonial Chisel":
                "Daggi drops into a crouch beside the gutter and studies the seam where the ice has locked the astrolabe in place."
                e "Straight into the seam?"
                d "Straight into the seam."
                d "If the ice gives, the astrolabe should come free with it."
            elif cave_state.get("Crypt Chisel Found", False):
                "His gaze flicks from the opened tomb to your empty hands and then back to the gutter."
                e "So the chisel was what we were missing."
                d "Looks that way."
                d "You've found the right tool. Now pry the gutter open."
            else:
                "Daggi studies the lodged astrolabe for a moment, then lets his eyes travel over the sealed tombs and the dust-choked edges of the chamber."
                e "You think one of the side tombs has a tool in it?"
                d "If this crypt kept burial tools anywhere, that is where I'd start."
                d "We need something narrow enough to pry the gutter open."
        else:
            "For a moment Daggi only watches the dark beyond the tombs, listening to the crypt settle around you both."
            e "What do we do once we leave?"
            d "We report to Chief Kaurhu and let the dead keep the rest of their secrets."
            d "We've got what we came for. Let's finish this and get back to Chief Kaurhu right away."
    if _return == "Pillar":
        "The stone support is carved in the same funerary style as the tombs around it."
    if _return == "Tomb":

        if target_sprite.x == 3 and target_sprite.y == 14:
            if not cave_state.get("Crypt Tomb 1 Opened", False):
                $ cave_state["Crypt Tomb 1 Opened"] = True
                "Reading the etched text on the front of the tomb, it says: '{i}The Hand of the Conqueror{/i}'"
                "You wedge your fingers under the frozen lip and force the lid aside with a long scraping groan."
                "Inside lies little more than old linen, brittle splinters of wood, and a bed of black dust where the contents rotted away long ago."
                if not cave_state.get("Crypt Chisel Found", False):
                    $ cave_state["Crypt Chisel Found"] = True
                    $ cave_state["Crypt Chisel At"] = (5, 16)
                    $ crypt_pry_tool = MapUser(5, 16, "small_chisel", 100, 100, "Ceremonial Chisel")
                    $ addSprite(conquerors_crypt, crypt_pry_tool)
                    "When you peel the linen back farther, a ceremonial chisel slides free from beneath the linen."
                    "The bronze is worked with burial etchings and soot-darkened rite marks. It was laid here with the dead, but its narrow edge is still fine enough to work into a crack."
            else:
                "The opened tomb yields nothing new beyond frost, dust, and old stone."
        elif target_sprite.x == 3 and target_sprite.y == 17:
            "Reading the etched text on the front of the tomb, it says: '{i}The Eye of the Conqueror{/i}'"
            if daggi_accompany:
                "You and Daggi try the lid together, but it only grinds a fraction before locking in place again."
                d "Stuck fast. Leave it."
            elif not cave_state.get("Crypt Tomb 2 Opened", False):
                $ cave_state["Crypt Tomb 2 Opened"] = True
                "The lid shifts with more ease than the others, as if it has been moved not that long ago."
                "Inside, the stone shelf is bare except for a torn scrap of bedding, fresh scrape marks in the frost, and a snapped leather cord caught in the corner. Whatever hung from it is gone."
                "The snapped cord and the marks in the frost make the tomb feel less like a grave than a place someone used in a hurry."
                if not cave_state.get("Herd Lost Item", False):
                    $ cave_state["Herd Lost Item"] = True
                    $ quest47.qComp(_("Search the crypt for Herd's missing astrolabe"))
            else:
                "The opened tomb still shows the same scrape marks and the snapped leather cord lying in the corner."
        elif target_sprite.x == 11 and target_sprite.y == 14:
            "Reading the etched text on the front of the tomb, it says: '{i}The Voice of the Conqueror{/i}'"
            "You brace yourself against the stone and shove, but the tomb lid does not move at all. Frost has sealed it into one solid block."
        else:
            "Reading the etched text on the front of the tomb, it says: '{i}The Shield of the Conqueror{/i}'"
            "This tomb refuses to open. The lid only answers with a dull grind before settling back into place."

    if _return == "Statue":
        if target_sprite.x == 3 and target_sprite.y == 2 and not cave_state.get("Crypt Statue Cache Looted", False):
            $ cave_state["Crypt Statue Cache Looted"] = True
            "Working your fingers through a split seam in the shattered guardian, you pull free a pouch wedged inside the bronze shell. It holds 3 pieces of copper and 1 Small HP Potion that somehow survived the years."
            $ addItem("Copper", inventory, 3)
            $ addItem("Small HP Potion", inventory, 1)
        elif cave_state.get("Crypt Statue Battle Won", False):
            "The guardian statues are nothing but broken slabs and scattered stone now. Whatever was moving in them is gone."
        elif cave_state.get("Crypt Statue Battle Ready", False) and not cave_state.get("Crypt Statue Battle Won", False):
            "The stone guardians are no longer just carvings. Frost keeps breaking loose around their feet."
        elif daggi_accompany:
            "The statue depicts an armored bronze warrior under a closed helm, its weathered plating still wrapped around a heavy shield and old battlefield gear."
            d "Older than our tribe's halls. Whoever built this place must've wanted to protect the conqueror's pride."
        else:
            "The armored bronze statue's face has been worn almost smooth, but its plated stance still carries a hard pride. The sculptor wanted this chamber to feel watched."

    if _return == "Table":
        if cave_state.get("Bell Ready", False) and not cave_state.get("Bell Claimed", False):
            if conquerors_crypt.inventory != None:
                "The little surveying bell rests on the table within easy reach, but your hands are already full."
            else:
                $ cave_state["Bell Claimed"] = True
                $ cave_state["Crypt Held Item"] = "Detector"
                $ cave_state["Crypt Detector Dropped At"] = None
                $ crypt_detector = MapUser(8, 4, "surveying_bell", 100, 100, "Detector")
                $ conquerors_crypt.inventory = crypt_detector
                if daggi_accompany:
                    "Resting on the table is a little surveying bell, neatly wired and weighted. Daggi picks it up, turns it once in his palm, then passes it to you."
                    d "It's Herd's. He didn't leave it here by accident."
                else:

                    "The little surveying bell rests where Herd left it, almost like he knew you would come back for it."
                    "You take it from the table, and he watches with the smallest easing of tension in his shoulders."
        elif cave_state.get("Herd Lost Item", False):
            if daggi_accompany:
                "The stone table is coated in dust except where a recent hand has cleared a few neat arcs across it."
                e "This surface got used more recently than the rest."
                d "I think so. Herd liked keeping his work in order, even when everything around him wasn't."
            else:
                "Dust lies thick across the stone table, except for a few recent sweeps made by careful hands."
                "The marks remind you of the way Herd flattened the floor before drawing. Even cornered, he still reaches for order."
        else:
            "The old offering table is bare. Time has stripped it down to stone dust and shallow tool marks."

    if _return == "Gutter":
        if not cave_state.get("Herd Lost Item Found", False):
            if conquerors_crypt.inventory != None and conquerors_crypt.inventory.interaction == "Ceremonial Chisel":
                $ cave_state["Crypt Gutter Opened"] = True
                $ target_back.img = "crypt_gutter04"
                $ dropped_chisel = conquerors_crypt.inventory
                $ drop_x = target_back.x - 1
                $ drop_y = target_back.y
                if sprite.x > target_back.x:
                    $ drop_x = target_back.x + 1
                if not conquerors_crypt.isEmpty(drop_x, drop_y):
                    if conquerors_crypt.isEmpty(target_back.x - 1, target_back.y):
                        $ drop_x = target_back.x - 1
                    elif conquerors_crypt.isEmpty(target_back.x + 1, target_back.y):
                        $ drop_x = target_back.x + 1
                $ dropped_chisel.x = drop_x
                $ dropped_chisel.y = drop_y
                $ addSprite(conquerors_crypt, dropped_chisel)
                $ conquerors_crypt.inventory = MapUser(target_back.x, target_back.y, "herds astrolabe", 100, 100, "Astrolabe")
                $ cave_state["Crypt Held Item"] = "Astrolabe"
                $ cave_state["Crypt Chisel At"] = (drop_x, drop_y)
                if daggi_accompany:
                    "You drive the ceremonial chisel into the frozen seam and lever upward while Daggi braces the stone with one hand."
                    "Ice cracks with a sharp report. The stone lip gives, the gutter opens, and Herd's astrolabe breaks free into your palm. The ceremonial chisel slips from your hand and clatters onto the floor beside the channel."
                    "Daggi wipes the astrolabe clean with his thumb and lets out a short breath."
                    d "There... yes. That's it."
                    "A deep grind rolls through the crypt before either of you can say more. Both guardian statues begin to move."
                    $ cave_state["Crypt Statue Battle Ready"] = True
                else:
                    "You work the ceremonial chisel into the gutter while Herd steadies the stone edge beside your wrist."
                    "With a stubborn snap of old ice, the gutter breaks open. Herd's astrolabe finally comes loose into your hand, slick with black melt and ancient grit, while the ceremonial chisel drops from your fingers and knocks against the stone beside your boots."
                $ cave_state["Herd Lost Item Found"] = True
                if daggi_accompany:
                    hide screen dungeon_map
                    jump Crypt_Statues_Awaken
            else:
                "The astrolabe is still wedged too deep in the frozen seam to free with your fingers alone."
                "You need something thin and sturdy enough to pry the gutter open."
        else:
            "A shallow gutter cuts the chamber, likely meant to carry melting water away from the tombs."

    if _return == "Gutter2":
        "A shallow gutter cuts the chamber, likely meant to carry melting water away from the tombs."

    if _return == "Debris":
        if target_sprite.x == 12 and target_sprite.y == 12 and not cave_state.get("Crypt Debris Cache Looted", False):
            $ cave_state["Crypt Debris Cache Looted"] = True
            "You dig into the marked rubble and pry loose a small cache pinned under broken stone. Inside are 2 iron ingots wrapped in old cloth and 2 bottles of Small HP Potion kept intact by the cold."
            $ addItem("Iron Ingot", inventory, 2)
            $ addItem("Small HP Potion", inventory, 2)
        elif not cave_state.get("Herd Lost Item", False):
            "The fallen stone is cold, damp, and old. Nothing about the pile stands out beyond the fact that part of the chamber clearly came down hard."
        elif not cave_state.get("Herd Lost Item Found", False):
            "You sort through the rubble, but it is only broken stone, frozen dust, and old scraps dragged down by the collapse."
        else:
            "You move a few more stones aside, but the rest of the pile is just rubble. Whatever mattered here has already been found."

    if _return == "Conquerors Tomb":
        if cave_state.get("Crypt Statue Battle Ready", False) and not cave_state.get("Crypt Statue Battle Won", False):
            "The great tomb is already split and weathered along one side, but the movement at the front of the chamber matters more right now."
        elif daggi_accompany:
            "The central tomb dominates the chamber, but age and collapse have already broken part of its stone shell. Daggi studies the damage in silence for a beat."
            d "Fresh damage. That means someone else has touched the tomb."
            e "Could it be the avalanche?"
            d "It could."
        else:
            "The great tomb sits at the heart of the chamber like an altar, but one side is already broken and sagging from age."
        "You stare at the leftover residues and bone fragments, but there is nothing left of the conqueror's remains."
        "Whatever was here has long since rotted away, leaving only dust and old stone behind."

    jump Conquerors_Crypt_Loop

label Crypt_Statues_Awaken:
    if daggi_accompany:
        "You and Daggi both turn toward the front of the crypt as the scrape of moving stone swells into a roar."
        d "That astrolabe woke them."
        e "Then we break them first."
        "The two guardian statues wrench free from their pedestals in a spray of frost and ancient grit."
        jump crypt_bearstatue_daggi_battle
    else:
        "Herd clutches the recovered astrolabe tight and recoils as the scrape of stone rolls through the chamber again."
        "At the front of the crypt, both guardian statues grind off their bases and turn toward you in stiff, deliberate jerks."
        "Herd snatches up a broken length of stone from the floor, points at the left statue, then the right, and squares up beside you."
        jump crypt_bearstatue_battle
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
