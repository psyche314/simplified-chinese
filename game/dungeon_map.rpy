default bandit_den = MapPat()
default puro_forest = MapPat()
default puro_watch_post = MapPat()
default mino_maze = MapPat()
default dark_forest1 = MapPat()
default moonlit_dungeon = MapPat()
default split_trail = MapPat()
default chelforte = MapPat()
default cavern_ent = MapPat()
default viscid_stream = MapPat()
default forgotten_sanctuary = MapPat()
default bandit_floor1 = MapPat()




init python:
    def puro_puzzle_drags(drags, drop):
        if not drop:
            drags[0].snap(piece_position[drags[0].drag_name][0], piece_position[drags[0].drag_name][1], 0.5)
            return
        drags[0].snap(tile_position[drop.drag_name][0], tile_position[drop.drag_name][1], 0.25)
        
        if puro_puzzle_tile_slots[drop.drag_name] != None:
            puro_puzzle_tile_slots[drop.drag_name].draggable = True
            puro_puzzle_tile_slots[drop.drag_name].snap(piece_position[puro_puzzle_tile_slots[drop.drag_name].drag_name][0], piece_position[puro_puzzle_tile_slots[drop.drag_name].drag_name][1], 0.25)
        
        if drop != None:
            puro_puzzle_tile_slots[drop.drag_name] = drags[0]
            drags[0].draggable = False 
        
        if puro_puzzle_tile_slots["north_tile"] != None and puro_puzzle_tile_slots["north_tile"].drag_name == "piece01" and puro_puzzle_tile_slots["south_tile"] != None and puro_puzzle_tile_slots["south_tile"].drag_name == "piece10" and puro_puzzle_tile_slots["east_tile"] != None and puro_puzzle_tile_slots["east_tile"].drag_name == "piece03" and puro_puzzle_tile_slots["west_tile"] != None and puro_puzzle_tile_slots["west_tile"].drag_name == "piece09":
            return "Congrats"

style stone_frame:
    background Frame("stone_frame", 10, 10, 10, 10)
    xalign 0.5

default puro_puzzle_tile_slots = {"north_tile": None, "south_tile": None, "east_tile": None, "west_tile": None}
default piece_position = {"piece01": (0.01, 0.01), "piece02": (0.11, 0.03), "piece03": (0.21, 0.02), "piece04": (0.02, 0.24), "piece05": (0.10, 0.23), "piece06": (0.23, 0.21), "piece07": (0.02, 0.44), "piece08": (0.12, 0.42), "piece09": (0.21, 0.41), "piece10": (0.05, 0.64), "piece11": (0.14, 0.70), "piece12": (0.22, 0.67)}
default tile_position = {"north_tile": (0.6, 0.08), "south_tile": (0.6, 0.68), "east_tile": (0.78, 0.38), "west_tile": (0.42, 0.38)}

image puro_spriteling_sprite 2:
    "puro_spriteling_sprite_0"
    pause 0.5
    "puro_spriteling_sprite_1"
    pause 0.5
    repeat

image puro_spriteling_sprite 1:
    "puro_spriteling_sprite_2"
    pause 0.5
    "puro_spriteling_sprite_3"
    pause 0.5
    repeat

image puro_spriteling_sprite1 = "puro_spriteling_sprite [puro_spriteling_sprite1.direction]"

image puro_spriteling_sprite2 = "puro_spriteling_sprite [puro_spriteling_sprite2.direction]"

image puro_spriteling_sprite3 = "puro_spriteling_sprite [puro_spriteling_sprite3.direction]"

image temple_spriteling up:
    "puro_spriteling_sprite 2"

image temple_spriteling down:
    "puro_spriteling_sprite 1"

image temple_spriteling left:
    "puro_spriteling_sprite 1"

image temple_spriteling right:
    "puro_spriteling_sprite 2"

image puro_puzzle_marking01:
    "forest_marking01"
    size (200, 200)

image puro_puzzle_marking02:
    "forest_marking02"
    size (200, 200)

image puro_puzzle_marking03:
    "forest_marking03"
    size (200, 200)

image puro_puzzle_marking04:
    "forest_marking04"
    size (200, 200)

image puro_puzzle_marking05:
    "forest_marking05"
    size (200, 200)

image puro_puzzle_marking06:
    "forest_marking06"
    size (200, 200)

image puro_puzzle_marking07:
    "forest_marking07"
    size (200, 200)

image puro_puzzle_marking08:
    "forest_marking08"
    size (200, 200)

image puro_puzzle_marking09:
    "forest_marking09"
    size (200, 200)

image puro_puzzle_marking10:
    "forest_marking10"
    size (200, 200)

image puro_puzzle_marking11:
    "forest_marking11"
    size (200, 200)

image puro_puzzle_marking12:
    "forest_marking12"
    size (200, 200)

image puro_tile01 = Composite(
    (240, 240),
    (0, 0), "puro_puzzle_blank",
    (20, 20), "puro_puzzle_marking01")

image puro_tile02 = Composite(
    (240, 240),
    (0, 0), "puro_puzzle_blank",
    (20, 20), "puro_puzzle_marking02")

image puro_tile03 = Composite(
    (240, 240),
    (0, 0), "puro_puzzle_blank",
    (20, 20), "puro_puzzle_marking03")

image puro_tile04 = Composite(
    (240, 240),
    (0, 0), "puro_puzzle_blank",
    (20, 20), "puro_puzzle_marking04")

image puro_tile05 = Composite(
    (240, 240),
    (0, 0), "puro_puzzle_blank",
    (20, 20), "puro_puzzle_marking05")

image puro_tile06 = Composite(
    (240, 240),
    (0, 0), "puro_puzzle_blank",
    (20, 20), "puro_puzzle_marking06")

image puro_tile07 = Composite(
    (240, 240),
    (0, 0), "puro_puzzle_blank",
    (20, 20), "puro_puzzle_marking07")

image puro_tile08 = Composite(
    (240, 240),
    (0, 0), "puro_puzzle_blank",
    (20, 20), "puro_puzzle_marking08")

image puro_tile09 = Composite(
    (240, 240),
    (0, 0), "puro_puzzle_blank",
    (20, 20), "puro_puzzle_marking09")

image puro_tile10 = Composite(
    (240, 240),
    (0, 0), "puro_puzzle_blank",
    (20, 20), "puro_puzzle_marking10")

image puro_tile11 = Composite(
    (240, 240),
    (0, 0), "puro_puzzle_blank",
    (20, 20), "puro_puzzle_marking11")

image puro_tile12 = Composite(
    (240, 240),
    (0, 0), "puro_puzzle_blank",
    (20, 20), "puro_puzzle_marking12")






screen puro_puzzle_board():

    add "puro_puzzle_board"
    frame:
        style "stone_frame"
        xalign 0.47
        yalign 0.23
        xpadding 20
        ypadding 20
        textbutton _("Leave") action Hide("puro_puzzle_board"), Jump("Puro_Forest_Loop") style_prefix "stash"


    draggroup:
        drag:
            drag_name "piece01"
            xpos 0.01
            ypos 0.01
            dragged puro_puzzle_drags
            draggable True
            droppable False
            add "puro_tile01"
        drag:
            drag_name "piece02"
            xpos piece_position["piece02"][0]
            ypos piece_position["piece02"][1]
            dragged puro_puzzle_drags
            add "puro_tile02"
            draggable True
            droppable False
        drag:
            drag_name "piece03"
            xpos piece_position["piece03"][0]
            ypos piece_position["piece03"][1]
            dragged puro_puzzle_drags
            add "puro_tile03"
            draggable True
            droppable False
        drag:
            drag_name "piece04"
            xpos piece_position["piece04"][0]
            ypos piece_position["piece04"][1]
            dragged puro_puzzle_drags
            add "puro_tile04"
            draggable True
            droppable False
        drag:
            drag_name "piece05"
            xpos piece_position["piece05"][0]
            ypos piece_position["piece05"][1]
            dragged puro_puzzle_drags
            add "puro_tile05"
            draggable True
            droppable False
        drag:
            drag_name "piece06"
            xpos piece_position["piece06"][0]
            ypos piece_position["piece06"][1]
            dragged puro_puzzle_drags
            add "puro_tile06"
            draggable True
            droppable False
        drag:
            drag_name "piece07"
            xpos piece_position["piece07"][0]
            ypos piece_position["piece07"][1]
            dragged puro_puzzle_drags
            add "puro_tile07"
            draggable True
            droppable False
        drag:
            drag_name "piece08"
            xpos piece_position["piece08"][0]
            ypos piece_position["piece08"][1]
            dragged puro_puzzle_drags
            add "puro_tile08"
            draggable True
            droppable False
        drag:
            drag_name "piece09"
            xpos piece_position["piece09"][0] ypos piece_position["piece09"][1]
            draggable True
            droppable False
            dragged puro_puzzle_drags
            add "puro_tile09"
        drag:
            drag_name "piece10"
            xpos piece_position["piece10"][0]
            ypos piece_position["piece10"][1]
            dragged puro_puzzle_drags
            add "puro_tile10"
            draggable True
            droppable False
        drag:
            drag_name "piece11"
            xpos piece_position["piece11"][0]
            ypos piece_position["piece11"][1]
            dragged puro_puzzle_drags
            add "puro_tile11"
            draggable True
            droppable False
        drag:
            drag_name "piece12"
            xpos piece_position["piece12"][0]
            ypos piece_position["piece12"][1]
            dragged puro_puzzle_drags
            add "puro_tile12"
            draggable True
            droppable False

        drag:
            drag_name "north_tile"
            xpos 0.6
            ypos 0.08
            add "puro_puzzle_tile"
            draggable False
            droppable True
        drag:
            drag_name "south_tile"
            xpos tile_position["south_tile"][0]
            ypos tile_position["south_tile"][1]
            add "puro_puzzle_tile"
            draggable False
            droppable True
        drag:
            drag_name "east_tile"
            xpos tile_position["east_tile"][0]
            ypos tile_position["east_tile"][1]
            add "puro_puzzle_tile"
            draggable False
            droppable True
        drag:
            drag_name "west_tile"
            xpos tile_position["west_tile"][0]
            ypos tile_position["west_tile"][1]
            add "puro_puzzle_tile"
            draggable False
            droppable True

label Puro_Forest_Enter:
    $ dungeon_timers = []
    $ puro_forest = MapPat([], "Puro Forest", 2, 17, "puro_floor1")
    $ puro_forest.playerSprite = MapUser(2, 17, "e_dungeon", 120, 200, no_op)
    $ puro_forest.mappy = [
        [MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree3")), MapTile(), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree3"))],
        [MapTile(MapThing("puro_tree2")), MapTile(), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(), MapTile(), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(), MapTile(MapThing("puro_tree2"))],
        [MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree1")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3"))],
        [MapTile(MapThing("puro_tree3")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree3")), MapTile(), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree1"))],
        [MapTile(MapThing("puro_tree2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree2")), MapTile(), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3"))],
        [MapTile(MapThing("puro_tree2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(), MapTile(), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree2"))],
        [MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree3")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree1"))],
        [MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3")), MapTile(), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree3"))],
        [MapTile(MapThing("puro_tree1")), MapTile(), MapTile(), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree1")), MapTile(), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree1"))],
        [MapTile(MapThing("puro_tree2")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2"))],
        [MapTile(MapThing("puro_tree2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2"))],
        [MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(), MapTile(), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2"))],
        [MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree3"))],
        [MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(), MapTile(MapThing("puro_tree3")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree3"))],
        [MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree2")), MapTile(), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3"))],
        [MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree1"))],
        [MapTile(MapThing("puro_tree3")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree3"))],
        [MapTile(MapThing("puro_tree3")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3")), MapTile(), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2"))],
        [MapTile(MapThing("puro_tree2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree1")), MapTile(), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1"))],
        [MapTile(MapThing("puro_tree1")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(), MapTile(), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree2"))]
    ]

    $ puro_marking_sprite01 = MapUser(13, 6, "forest_marking01", 120, 120, "Marking01")
    $ puro_marking_sprite02 = MapUser(5, 2, "forest_marking02", 120, 120, "Marking02")
    $ puro_marking_sprite03 = MapUser(14, 7, "forest_marking03", 120, 120, "Marking03")
    $ puro_marking_sprite04 = MapUser(4, 2, "forest_marking04", 120, 120, "Marking04")
    $ puro_marking_sprite05 = MapUser(2, 16, "forest_marking05", 120, 120, "Marking05")
    $ puro_marking_sprite06 = MapUser(4, 16, "forest_marking06", 120, 120, "Marking06")
    $ puro_marking_sprite07 = MapUser(8, 14, "forest_marking07", 120, 120, "Marking07")
    $ puro_marking_sprite08 = MapUser(9, 8, "forest_marking08", 120, 120, "Marking08")
    $ puro_marking_sprite09 = MapUser(6, 5, "forest_marking09", 120, 120, "Marking09")
    $ puro_marking_sprite10 = MapUser(8, 19, "forest_marking10", 120, 120, "Marking10")
    $ puro_marking_sprite11 = MapUser(13, 15, "forest_marking11", 120, 120, "Marking11")
    $ puro_marking_sprite12 = MapUser(6, 9, "forest_marking12", 120, 120, "Marking12")
    $ puro_egg_sprite1 = MapChecker(7, 5, "puro_egg_sprite01", 120, 120, "Egg", 0, "puro_egg_sprite02")
    $ puro_sword_sprite1 = MapUser(9, 19, "puro_sword_sprite", 120, 120, "Sword")
    $ puro_skull_sprite1 = MapStorer(14, 6, "puro_skull_sprite", 120, 120, "Skull", 1)
    $ puro_board_sprite1 = MapUser(10, 13, "puro_board_sprite01", 120, 120, "Board")
    $ puro_pot_sprite1 = MapStorer(9, 14, "puro_pot_sprite01", 120, 120, "Pot", 1)
    $ puro_board_sprite2 = MapUser(10, 13, "puro_board_sprite02", 120, 120, "Board2")
    $ puro_stone_sprite1 = MapUser(3, 2, "puro_stone1", 120, 120, "Stone")
    $ puro_candle_sprite1 = MapUser(13, 14, "puro_candle_sprite01", 120, 120, "Candle")
    $ puro_block_sprite1 = MapUser(3, 16, "puro_block_sprite01", 120, 120, "Block")
    $ puro_statue_sprite1 = MapUser(10, 8, "puro_statue_sprite01", 120, 120, "Statue")
    $ puro_stone_sprite2 = MapUser(14, 4, "puro_stone1", 120, 120, "Stone")
    $ puro_trunk_sprite1 = MapUser(5, 1, "puro_trunk1", 120, 120, "Trunk")
    $ puro_trunk_sprite2 = MapUser(6, 1, "puro_trunk2", 120, 120, "Trunk")
    $ puro_stone_sprite3 = MapUser(15, 8, "puro_stone1", 120, 120, "Stone")
    $ puro_stone_sprite4 = MapUser(2, 8, "puro_stone1", 120, 120, "Stone")
    $ puro_journal_sprite = MapUser(2, 8, "spritebinder_journal_sprite", 120, 120, "Journal")
    $ puro_stone_sprite5 = MapUser(7, 14, "puro_stone1", 120, 120, "Stone")
    $ puro_stone_sprite6 = MapUser(14, 16, "puro_stone1", 120, 120, "Stone")
    $ puro_stonegate_sprite1 = MapUser(5, 10, "puro_stonegate_sprite2", 120, 180, "Stonegate")
    $ puro_stonegate_sprite01 = MapUser(5, 11, "empty", 120, 180, "Stonegate")
    $ puro_stonegate_sprite2 = MapUser(5, 10, "puro_stonegate_sprite1", 120, 180, "Stonegate2")
    $ puro_stonegate_sprite02 = MapUser(5, 11, "empty", 120, 180, "Stonegate2")
    $ puro_floor_sprite1 = MapUser(3, 14, "puro_floor2", 120, 120, "Floor2")
    $ puro_barrel_sprite1 = MapUser(6, 8, "barrel_sprite", 120, 120, "Barrel")
    $ puro_spriteling_sprite1 = MapMover(5, 15, "puro_spriteling_sprite1", 120, 120, "Spriteling1", 6, 2, 1)
    $ puro_spriteling_sprite2 = MapMover(11, 7, "puro_spriteling_sprite2", 120, 120, "Spriteling2", 8, 4, 1)
    $ puro_spriteling_sprite3 = MapMover(10, 3, "puro_spriteling_sprite3", 120, 120, "Spriteling3", 6, 1, 1)

    $ puro_bone_token_sprite1 = MapUser(3, 14, "bone_token_sprite", 120, 120, "Bone")
    $ puro_bone_token_sprite2 = MapUser(4, 2, "bone_token_sprite", 120, 120, "Bone")
    $ puro_bone_token_sprite3 = MapUser(14, 11, "bone_token_sprite", 120, 120, "Bone")
    $ addBack(puro_forest, puro_marking_sprite01)
    $ addBack(puro_forest, puro_marking_sprite02)
    $ addBack(puro_forest, puro_marking_sprite03)
    $ addBack(puro_forest, puro_marking_sprite04)
    $ addBack(puro_forest, puro_marking_sprite05)
    $ addBack(puro_forest, puro_marking_sprite06)
    $ addBack(puro_forest, puro_marking_sprite07)
    $ addBack(puro_forest, puro_marking_sprite08)
    $ addBack(puro_forest, puro_marking_sprite09)
    $ addBack(puro_forest, puro_marking_sprite10)
    $ addBack(puro_forest, puro_marking_sprite11)
    $ addBack(puro_forest, puro_marking_sprite12)
    $ addBack(puro_forest, puro_journal_sprite)
    $ addBack(puro_forest, puro_floor_sprite1)
    $ addSprite(puro_forest, puro_bone_token_sprite1)
    $ addSprite(puro_forest, puro_stonegate_sprite1)
    $ addSprite(puro_forest, puro_stonegate_sprite01)
    $ addSprite(puro_forest, puro_bone_token_sprite2)
    $ addSprite(puro_forest, puro_bone_token_sprite3)
    $ addSprite(puro_forest, puro_barrel_sprite1)
    $ addSprite(puro_forest, puro_skull_sprite1)
    $ addSprite(puro_forest, puro_sword_sprite1)
    $ addSprite(puro_forest, puro_board_sprite1)
    $ addSprite(puro_forest, puro_pot_sprite1)
    $ addSprite(puro_forest, puro_egg_sprite1)
    $ addBack(puro_forest, puro_block_sprite1)
    $ addBack(puro_forest, puro_candle_sprite1)
    $ addSprite(puro_forest, puro_statue_sprite1)
    $ addSprite(puro_forest, puro_stone_sprite1)
    $ addSprite(puro_forest, puro_stone_sprite2)

    $ addSprite(puro_forest, puro_spriteling_sprite1)
    $ addSprite(puro_forest, puro_spriteling_sprite2)
    $ addSprite(puro_forest, puro_spriteling_sprite3)
    $ addSprite(puro_forest, puro_trunk_sprite1)
    $ addSprite(puro_forest, puro_trunk_sprite2)
    $ addSprite(puro_forest, puro_stone_sprite3)
    $ addSprite(puro_forest, puro_stone_sprite4)
    $ addSprite(puro_forest, puro_stone_sprite5)
    $ addSprite(puro_forest, puro_stone_sprite6)
    $ addSprite(puro_forest, puro_forest.playerSprite)
    $ current_location = puro_forest
    $ puro_forest.entranceCount += 1
    yu "What is this place, it's so... different from the rest of the forest."
    "You feel a sense of unease, as if even the trees are watching you. Perhaps you should go back and stay at the tower."
    "But something inside you tells you a secret lies in here."

    jump Puro_Forest_Loop

label Puro_Forest_Loop:
    $ renpy.music.play(mOpen1, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ disableC = False
    $ sprite = puro_forest.playerSprite
    call screen dungeon_map(puro_forest)


    if _return == "Spriteling1":
        $ mimic_num = 1
        jump Puro_Forest_Spriteling
    if _return == "Spriteling2":
        $ mimic_num = 2
        jump Puro_Forest_Spriteling
    if _return == "Spriteling3":
        $ mimic_num = 3
        jump Puro_Forest_Spriteling

    if _return == "Marking01":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "You see a faint marking on the ground, it shows a hefty figure with awry pair of arms."

    if _return == "Marking02":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "You find a marking as you look down, with a floating figure of eight ephemeral arms."

    if _return == "Marking03":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "A symbol beneath the grass meets your eyes, it seems to be of a whimsical three-eyed construct."

    if _return == "Marking04":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "In the dirt, you find a marking of a crounching creature with a pair of sharp claws."

    if _return == "Marking05":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "You find a marking of an abstract symbol, you can't make out what it depicts but at least it seems symmetrical."

    if _return == "Marking06":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "You find a marking of a creature of sophisticated structures, it seems to be related to some plants."

    if _return == "Marking07":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "There is a symbol on the ground, perhaps of an antlered man with musical notes on the side."

    if _return == "Marking08":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "A marking of a creature with a large horn is on the ground, it seems to be restrained in some form."

    if _return == "Marking09":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "From the ground, you see a symbol of a spherical form like the sun, emanating rays and cresant shapes."

    if _return == "Marking10":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "Scratching off the dirt, there is fluttering symbol of wings and shapes beneath it, if you have not mistaken it."

    if _return == "Marking11":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "You notice a symbol of a flying creature with two long arms, seemingly soaring over the forest."

    if _return == "Marking12":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "Incidentally, a small, dark symbol is etched on the ground, perhaps it depicts a whirlwind of some sort."

    if _return == "Egg":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        $ bone_num = puro_egg_sprite1.status
        "On the ground, you take notice of an egg-shaped altar, with a small hole on the top."
        "Some words are etched on the surface, albeit blurred, you can only make out one word - 'Offering-'."
        "You can't help but feel a sense of familiarity with it, as if you have seen it before."
        if bone_num == 0:
            "Looking closely, you discover 5 holes on the altar, maybe something can be done with it..."
        else:
            "Looking closely, you discover 5 holes on the altar, [bone_num] of which has been filled."

    if _return == "Stone":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "An ordinary stone, maybe you can lift it up if you have the strength."

    if _return == "Sword":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "A sword embedded within the rocky ground beneath the surface, you can't seem to pull it out with whatever strength you have."

    if _return == "Skull":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "A strange, dragon-like skull. It's somewhat smaller than the folks back in your tribe."
        "Staring at it, you can't help but to shiver, a shred of doubt plants its seed in your mind, you have to reassure yourself, it must not be Chime's..."

        if puro_skull_sprite1.status > 0:
            if puro_forest.inventory == None:
                $ puro_forest.inventory = puro_bone_token_sprite1
                $ puro_skull_sprite1.status -= 1
                "Giving another glance, you notice a bone token inside the skull."
                "You pick them up carefully, scraping off the dust on the bone before carrying on."
            else:
                "There's a bone token inside, but you can't carry more."

    if _return == "Board":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "You take notice of a small board lodged on the ground, and some stone tiles placed on the surface."
        "Three mysterious symbols are etched around the squares on the board, perhaps they are something from around the forest."
        $ puro_puzzle_tile_slots = {"north_tile": None, "south_tile": None, "east_tile": None, "west_tile": None}
        scene puro_puzzle_board
        call screen puro_puzzle_board()

        hide puro_puzzle_board
        hide screen puro_puzzle_board 
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "A click sound can be heard from within the stone board, as the four tiles suddenly becomes wedged in the slots."
        "Now the board seems to be glowing faintly, before you see the gate ahead silently opens."
        $ removeSprite(puro_forest, puro_board_sprite1)
        $ addSprite(puro_forest, puro_board_sprite2)

        $ removeSprite(puro_forest, puro_stonegate_sprite1)
        $ removeSprite(puro_forest, puro_stonegate_sprite01)
        $ addBack(puro_forest, puro_stonegate_sprite2)
        $ addBack(puro_forest, puro_stonegate_sprite02)

    if _return == "Pot":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "A cluster of weathered pots strewn haphazardly on the forest floor."
        "Upon closer inspection, you notice a subtle warmth emanating from the pots."
        if puro_pot_sprite1.status > 0:
            if puro_forest.inventory == None:
                $ puro_pot_sprite1.status -= 1
                $ puro_forest.inventory = puro_bone_token_sprite1
                "You pick one up and find a bone token inside, and take it with you."
            else:
                "There's a bone token inside, but you can't carry more."

    if _return == "Journal":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        $ book_page = 0
        $ spritebinder_journal = Book(_("{i}Pekoe's Note{/i}"),"spritebinder_journal", "Spritebinder_Note")
        $ spritebinder_journal01 = Page(_("Remind me, the spritebinder, or refer it as the collective consciousness of eight spectral entities. These individuals, a rather inquisitive bunch, seemed to be quite the genius scholars, or whatever such pursuits are called on the other side, who somehow brought themselves to this land.\n\nThe incident is unlikely to repeat itself. As far as the land is concerned, no one aside from Chime has laid eyes on them. I suspect he followed me into the heart of the forest, where I first encountered these peculiar intruders. However, the actual event transpired within the crypt, and I made sure that no one could access there."),_("Speaking of the scholars, they appeared to be affiliated with a tribe — a group of investigators seeking to trace the lost sprites that escaped during the Ookko incident. It seems they made contact with the runes, likely the reason for their journey to our tribe. Fortunately, magic has no influence here, allowing me to extract some information before their banishment.\n\nAll in all, I cannot let the scholars leave, so I opted to sever their ability to communicate instead. At least, some natural instincts of these poor souls remains manifested in the shape of their hands, consider them bane of the pesky sprites from now on."), 1)

        $ spritebinder_journal02 = Page(_("Now, the crux of the matter: I gleaned from the scholars that they were in pursuit of him, motive is still unknown, unless we fall back on their own curiosity. While they proved to be nothing but a chore, they are not my primary concern. What troubles me is that the passage towards our tribe may have been known from outside. I fear that the next time someone traverses that passage, I might not have caught them in time.\n\nRegardless, those on the other side should make a better effort to ensure that does not happen again, I should not have been the only one taking care of the mess. The potential consequences could be catastrophic to them if a malicious outsider somehow made contact"), _("with our tribe.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPekoe"), 2)

        $ spritebinder_journal01.addTo(spritebinder_journal)
        $ spritebinder_journal02.addTo(spritebinder_journal)
        show screen book_read(spritebinder_journal) with dissolve 

        "You found a few loose pages resting underneath the journal."
        "Flipping through the pages, it seems to be about something called spritebinder."
        yu "Pekoe...? It sounds so familiar, like I've heard of it before..."
        call screen book_read(spritebinder_journal) with dissolve 

        "The fact that it was hidden in the forest makes you nervous. So you decide to keep your knowledge and put the notes back."

    if _return == "Board2":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "The four tiles seem to be wedged in the slots of the board."


    if _return == "Candle":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "A collection of ethereal candles flicker, casting a soft glow in the eerie forest."
        "You feel somewhat uncomfortable, after all there should be no one around to light these candles."

    if _return == "Block":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "A large, heavy block of stone, it doesn't look like anything you've seen before."

    if _return == "Statue":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "The statue of a familiar dragon bear weathered expressions of accomplishment."
        "It appears to bear intricate carvings and faint runes that shimmer when touched."
        "Upon closer inspection, you notice the word {i}'Pekoe'{/i} carved on the base of the statue."

    if _return == "Trunk":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "A large, hollowed trunk, it seems to be a good place to store things."
        "Opening the trunk reveals nothing more than a few fallen leaves and the faint scent of damp earth."

    if _return == "Barrel":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        "As you approach the lone barrel, a subtle aroma wafts through the air, perhaps a blend of earthy moss and distant enchantments."

    if _return == "Take Bone":
        $ puro_forest.takeItem(sprite, puro_bone_token_sprite1)
        $ x, y = getFacingTile(sprite)
        $ puro_forest.unoccupy(x, y)

    if _return == "Take Stone":
        $ puro_forest.takeItem(sprite, puro_stone_sprite1)
        $ x, y = getFacingTile(sprite)
        $ puro_forest.unoccupy(x, y)

    if _return == "Drop Stone":
        $ x, y = getFacingTile(sprite)
        if puro_forest.isEmpty(x, y):
            $ puro_forest.inventory = None
            $ puro_forest.occupy(x, y, puro_stone_sprite1)
        else:
            $ disableC = True
            show screen dungeon_map(puro_forest)
            "You can't drop the stone here."
    if timenow.hour > 6:
        hide screen dungeon_map
        jump Encountering_Moine
    if _return == "Take Egg" and puro_egg_sprite1.status > 0:
        $ puro_forest.inventory = puro_bone_token_sprite1
        $ puro_egg_sprite1.status -= 1

    if _return == "Drop Bone":
        $ disableC = True
        show screen dungeon_map(puro_forest)
        $ x, y = getFacingTile(sprite)
        if puro_forest.isEmpty(x, y):
            $ puro_forest.inventory = None
            $ puro_forest.occupy(x, y, puro_bone_token_sprite1)

        elif x == puro_egg_sprite1.x and y == puro_egg_sprite1.y:
            $ puro_forest.inventory = None
            $ puro_egg_sprite1.status += 1
            if puro_egg_sprite1.status < 5:
                "You place the bone token into the hole on the egg-shaped altar."
                "The token fits perfectly, and the altar glows faintly before going dim again."
            else:
                "You place the bone token into the hole on the egg-shaped altar."
                "The token fits perfectly, and the altar glows faintly."
                "The altar seems to be full now, and the glow becomes more apparent."
                jump Puro_Summoning_Spritebinder
        else:

            "You can't drop the bone here."

    jump Puro_Forest_Loop

label Puro_Forest_Spriteling:

    $ disableC = True
    show screen dungeon_map(puro_forest)
    scene black
    "As you wander through the eerie forest, a soft glow materializes into a Spriteling."
    "You can feel the cold air around you, as the Spriteling's presence becomes more apparent."
    hide screen dungeon_map with dissolve
    jump spriteling_battle

label Puro_Summoning_Spritebinder:
    $ disableC = True
    show screen dungeon_map(puro_forest)
    yu "Huh?"
    scene puro_forest
    hide screen dungeon_map with dissolve 
    "The altar glows brighter and brighter, until the light becomes blinding."
    "A loud, otherworldly sound echoes through the forest, and you feel a sudden gust of wind."
    "When the light fades, you find yourself standing in front of a strange, ethereal figure."
    "A hooded strange sprite, with too many pairs of arms, manifested itself before your eyes."
    yu "What is this thing!"
    "It stares at you for a moment, before speaking in a voice that seems to come from everywhere at once."
    yu "Shit!"
    "Within a few seconds, it extends its arms towards you, and begins trying to grip onto you tightly."
    "You yank them away, and prepares to fight against this unknown entity."
    jump spritebinder_battle

label Puro_Watch_Post_Enter:
    $ dungeon_timers = []
    show screen daytime()
    $ puro_watch_post = MapPat([], "Puro Watch Post", 1, 3, "puro_floor1")
    $ puro_watch_post.playerSprite = MapUser(1, 3, "e_dungeon", 120, 200, no_op)
    $ puro_watch_post.mappy = [
        [MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree3")), MapTile(), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1"))],
        [MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3")), MapTile(), MapTile(), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree2"))],
        [MapTile(MapThing("puro_tree1")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1"))],
        [MapTile(MapThing("puro_tree1")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree2"))],
        [MapTile(MapThing("puro_tree2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree3"))],
        [MapTile(MapThing("puro_tree3")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree1"))],
        [MapTile(MapThing("puro_tree2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree2")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1"))],
        [MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1"))],
        [MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree2")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree3")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree1")), MapTile(MapThing("puro_tree3"))]
    ]
    $ hezzong_sprite1 = MapUser(2, 5, "hezzong_sprite", 140, 180, "Hezzong")
    $ watchtower_sprite1 = MapUser(4, 3, "puro_watchtower_sprite", 140, 240, "Watchtower")
    $ puro_crate_sprite1 = MapStorer(5, 5, "puro_crate_sprite", 120, 120, "Crate")
    $ turnip_sprite1 = MapUser(3, 2, "turnip", 120, 120, "Turnip")
    $ turnip_sprite2 = MapUser(5, 6, "turnip", 120, 120, "Turnip")
    $ puro_candle_sprite1 = MapUser(2, 1, "puro_candle_sprite01", 120, 120, "Candle")
    $ puro_candle_sprite2 = MapUser(7, 5, "puro_candle_sprite01", 120, 120, "Candle")
    $ puro_candle_sprite3 = MapUser(24, 4, "puro_candle_sprite01", 120, 120, "Candle")
    $ puro_path_sprite = MapUser(22, 0, "puro_path_sprite", 120, 120, "Path")
    $ puro_block_sprite1 = MapUser(11, 3, "puro_block_sprite01", 120, 120, "Block")
    $ puro_stone_sprite2 = MapUser(13, 3, "puro_stone1", 120, 120, "Stone")
    $ puro_stone_sprite3 = MapUser(13, 4, "puro_stone1", 120, 120, "Stone")
    $ puro_stone_sprite4 = MapUser(13, 5, "puro_stone1", 120, 120, "Stone")
    $ puro_stone_sprite1 = MapUser(13, 2, "puro_stone1", 120, 120, "Stone")
    $ addSprite(puro_watch_post, hezzong_sprite1)
    $ addSprite(puro_watch_post, watchtower_sprite1)
    $ addSprite(puro_watch_post, puro_watch_post.playerSprite)
    $ addSprite(puro_watch_post, puro_crate_sprite1)
    $ addSprite(puro_watch_post, puro_stone_sprite1)
    $ addSprite(puro_watch_post, puro_stone_sprite2)
    $ addSprite(puro_watch_post, puro_stone_sprite3)
    $ addSprite(puro_watch_post, puro_stone_sprite4)
    $ addSprite(puro_watch_post, puro_path_sprite)
    $ addBack(puro_watch_post, puro_candle_sprite1)
    $ addBack(puro_watch_post, puro_candle_sprite2)
    $ addBack(puro_watch_post, puro_candle_sprite3)
    $ addBack(puro_watch_post, puro_block_sprite1)
    $ addBack(puro_watch_post, turnip_sprite1)
    $ addBack(puro_watch_post, turnip_sprite2)
    $ current_location = puro_watch_post
    $ on_watch_post = False

    if tutorial_stage == 0:
        "You can hear the rustling of the leaves as hezzong strolls along the narrow trail, but his calmness doesn't relieve your anxiety."
        "The lack of sleep is getting to you, you can feel your eyes getting heavier and heavier."
        "Just as you are about to fall asleep, Hezzong stops in front of you."
        hz "Here we are."

        $ disableC = True
        $ sprite = puro_watch_post.playerSprite

        show screen dungeon_map(puro_watch_post)

        "You blink a few times, before you can see a tall tower in front of you, with a few equipment scattered on the ground."
        hz "We've arrived to the post, you should be able to see the tribe on the top there."
        hz "For a new watcher, we usually perform a quick formal training for a few weeks, but I don't think you need that."
        hz "But as a formality, I will still try to explain how you can navigate around the forest."
        yu "Allfather, I should just go now, I don't want to waste any more time."
        hz "Look, even though I wish to look the other way, you owe the tribe a due dilligence, considering I don't let anyone else use the duty as an excuse for travelling at night."
        yu "Alright, I understand."
        hz "Okay, let's begin then."
        "Hezzong walks up by your side, and begin explaining the basics of navigating in the forest."
        hz "Now, try moving around the forest."
        msg "Hint: Try to use arrow Key, WASD or the arrow buttons on the screen to move."

    jump Puro_Watch_Post_Loop

label Puro_Watch_Post_Loop:
    $ disableC = False
    $ sprite = puro_watch_post.playerSprite

    call screen dungeon_map(puro_watch_post)

    if _return == "Hezzong":
        $ disableC = True
        scene puro_forest with dissolve
        show hezzong normal with dissolve
        call Hezzong_Puro_Forest_Dialogue from _call_Hezzong_Puro_Forest_Dialogue_1


    if tutorial_stage == 0 and puro_watch_post.step == 4:
        $ disableC = True
        show screen dungeon_map(puro_watch_post)
        hz "Good, you are getting the hang of it."
        yu "Okay, but I am just walking, I thought it's supposed to be easy."
        hz "How about this, get to the crates over there, and take a look at the food over there."
        msg "Hint: Try to use Space, or the Interact button on the screen to interact with objects."
        $ tutorial_stage = 1

    if tutorial_stage == 1 and _return == "Crate":
        $ disableC = True
        show screen dungeon_map(puro_watch_post)
        hz "Great, you're doing a good job."
        yu "I can see some turnips in the crate, what should I do with them?"
        hz "Nothing, they are for the watchers, you can take them if you want."
        hz "Now, try to pick up the turnips over there, and bring them into the crate."
        msg "Hint: Try to use {i}E{/i}, or the hand button on the screen to pick up or drop objects."
        $ tutorial_stage = 2

    if puro_crate_sprite1.status == 2 and tutorial_stage == 2:
        $ disableC = True
        scene puro_forest with dissolve

        show hezzong normal with dissolve
        hz "Well done..."
        "Hezzong says as he yawns and stretches his furry arms outward lazily."
        yu "Allfather, is this training enough?"
        hz "I think you're ready as a watcher, at least for tonight."
        yu "Then, shall I go now?"
        "Hezzong looks at you, and then at the tower."
        show hezzong closeeyes
        hz "Yes, I am going back to the tribe to take my rest, maybe you should go up towards the watchtower."
        hz "Don't walk too far away from the tower, unless you are ready to fight some sprites, or some fellow."
        yu "Okay, but what if I see that light from Chime again? Should I run towards there?"
        show hezzong talk
        hz "No, it's too dangerous, you should strike the bell in our tower, and we'll be there swiftly and save him."
        hz "Even if we can't get a glimpse of Chime, at least we might save you from whatever's out there."
        yu "I understand, Hezz."
        "The elder pats your shoulder tenderly as he leans slightly towards you."
        hz "Well, stay safe and I'll see you tomorrow, good luck."
        "Hezzong gives you another few pats, squeezing your shoulder with his short claws."
        "His snout curls into a smile, he is so close against your face, you can feel his warmth and the faint scent."
        "You take a heavy breath as Hezzong walks away, leaving you alone in the forest."
        $ tutorial_stage = 3
        scene black with dissolve
        hide screen dungeon_map with dissolve 
        pause 0.5
        $ removeSprite(puro_watch_post, hezzong_sprite1)
        show screen dungeon_map(puro_watch_post) with dissolve 
        yu "I guess I should look around the forest, or get on the tower."

    if _return == "Take Turnip":
        $ x, y = getFacingTile(sprite)
        if puro_watch_post.mappy[y][x].back != None and puro_watch_post.mappy[y][x].back.interaction == "Turnip":
            $ picked_turnip = puro_watch_post.mappy[y][x].back
        elif puro_watch_post.mappy[sprite.y][sprite.x].back != None and puro_watch_post.mappy[sprite.y][sprite.x].back.interaction == "Turnip":
            $ picked_turnip = puro_watch_post.mappy[sprite.y][sprite.x].back
        else:
            $ picked_turnip = None
        $ puro_watch_post.takeItem(sprite, picked_turnip)

    if _return == "Watchtower":
        $ disableC = True
        show screen dungeon_map(puro_watch_post)
        if tutorial_stage == 3:
            menu:
                yu "Should I head onto the tower right now? I'll probably stay there for the rest of the night."
                "Get on top of the watchtower":
                    jump Puro_Get_Onto_Watchtower
                "Look around the forest first":

                    pass
        else:
            hz "It's our watchtower, you should be able to see the tribe from the top over there."
            yu "Allfather, it's really tall."
            hz "We built it a long time ago, too long. It's a good place to see the entire forest."

    if _return == "Path":
        $ disableC = True
        show screen dungeon_map(puro_watch_post)
        if tutorial_stage < 3:
            hz "What are you doing over there? Our training is not over yet."
            yu "Sorry! Allfather."
        else:

            "It seems to be a path leading deeper into the forest, you can't see the end of it, but you can see a faint light in the distance."
            menu:
                "Should you explore it?"
                "Yes{#PuroForestExplore}":
                    scene black with dissolve
                    hide screen dungeon_map with dissolve

                    $ removeSprite(puro_watch_post, puro_watch_post.playerSprite)
                    pause 1.0
                    jump Puro_Forest_Enter
                "No{#PuroForestExplore}":
                    pass
    if timenow.hour > 6:
        hide screen dungeon_map
        jump Encountering_Moine
    if _return == "Take Stone":
        $ puro_watch_post.inventory = puro_stone_sprite1
        $ x, y = getFacingTile(sprite)
        $ puro_watch_post.unoccupy(x, y)

    if _return == "Drop Stone":
        $ x, y = getFacingTile(sprite)
        if puro_watch_post.isEmpty(x, y):
            $ puro_watch_post.inventory = None
            $ puro_watch_post.occupy(x, y, puro_stone_sprite1)
        else:

            $ disableC = True
            show screen dungeon_map(puro_watch_post)
            "You can't drop the stone here."

    if _return == "Stone":
        $ disableC = True
        show screen dungeon_map(puro_watch_post)
        "An ordinary stone, maybe you can lift it up if you have the strength."

    if _return == "Drop Turnip":
        $ x, y = getFacingTile(sprite)
        if puro_watch_post.isEmpty(x, y) and puro_watch_post.isEmptyBack(x, y):
            $ puro_watch_post.inventory.x = x
            $ puro_watch_post.inventory.y = y
            $ puro_watch_post.occupyback(x, y, puro_watch_post.inventory)
            $ puro_watch_post.inventory = None

        elif x == puro_crate_sprite1.x and y == puro_crate_sprite1.y:
            $ puro_watch_post.inventory = None
            $ puro_crate_sprite1.status += 1
        else:

            $ disableC = True
            show screen dungeon_map(puro_watch_post)
            "You can't drop the turnip here."

    if _return == "Take Crate" and puro_crate_sprite1.status > 0:
        $ puro_watch_post.inventory = turnip_sprite1
        $ puro_crate_sprite1.status -= 1


    jump Puro_Watch_Post_Loop

default damp_cave_map = {"None": 0, "stone_top": 1, "stone_wall": 2}
label Damp_Cave_Enter:
    $ dungeon_timers = []
    $ d1x = 24
    $ d1y = 7
    $ saved_hp = pc.hp
    $ saved_mp = pc.mp
    $ saved_lust = pc.lust
    hide screen menu_buttons
    show screen dungeon_buttons
    $ bandit_den = MapPat([], "Damp Cave", 24, 7, "floor")
    $ bandit_den.floorPlan([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1],
        [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 0, 1, 1, 0, 2, 1, 1, 0, 1, 1, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    ], damp_cave_map)
    $ setthingstraight(bandit_den.mappy)
    $ bandit_den.playerSprite = MapUser(d1x, d1y, "e_dungeon", 120, 200, {})
    $ current_location = bandit_den

    $ mimic_sprite1 = MapUser(15, 7, "mimic_sprite", 120, 120, "Mimic")
    $ mimic_sprite2 = MapUser(1, 12, "mimic_sprite", 120, 120, "Mimic2")
    $ mimic_sprite3 = MapUser(16, 12, "mimic_sprite", 120, 120, "Mimic3")
    $ ward_sprite1 = MapUser(18, 2, "ward_sprite_0", 140, 150, "Ward")
    $ golem_sprite1 = MapUser(20, 12, "golem_sprite_0", 120, 170, "Golem")
    $ furkan_sprite = MapUser(22, 12, "furkan_sprite", 120, 150, "Furkan")
    $ ward_sprite2 = MapUser(9, 6, "ward_sprite_1", 140, 150, "Ward2")
    $ ward_sprite3 = MapUser(8, 10, "ward_sprite_0", 140, 150, "Ward3")
    $ leave_sprite = MapUser(24, 6, "door_exit", 120, 120, "Leave")
    $ leave_sprite = MapUser(23, 11, "door_exit", 120, 120, "Exit")
    $ chest_sprite = MapUser(8, 12, "chest_sprite", 120, 120, "Chest")
    $ chest_sprite2 = MapUser(23, 2, "chest_sprite", 120, 120, "Chest2")
    $ shelf_sprite = MapUser(4, 12, "shelf_sprite", 120, 120, "Shelf")
    $ shelf_sprite2 = MapUser(5, 12, "shelf_sprite", 120, 120, "Shelf")
    $ rock_sprite = MapUser(4, 2, "rock_sprite", 120, 120, "Rock")
    $ pond_sprite = MapUser(1, 2, "pond_sprite", 120, 120, "Pond")
    $ hole_sprite = MapUser(11, 9, "hole_sprite", 120, 120, "Hole")
    $ hole_sprite2 = MapUser(12, 2, "hole_sprite", 120, 120, "Hole2")
    $ hole_sprite3 = MapUser(4, 10, "hole_sprite", 120, 120, "Hole3")
    $ hole_sprite4 = MapUser(10, 9, "hole_sprite", 120, 120, "Hole4")
    $ hole_filled_sprite = MapUser(11, 9, "hole_filled_sprite", 120, 120, "Hole Plank")
    $ tenki_moving = True
    $ hole_stucked_sprite = MapUser(11, 9, "hole_stucked_sprite", 120, 120, "Hole Rock")

    $ plank_sprite = MapUser(22, 6, "plank_sprite", 120, 120, "Plank")
    $ puddle_sprite = MapUser(13, 6, "puddle_sprite", 120, 120, "Puddle")
    $ pond_sprite2 = MapUser(1, 3, "pond_sprite", 120, 120, "Pond")
    $ pond_sprite3 = MapUser(1, 4, "pond_sprite", 120, 120, "Pond")
    $ pond_sprite4 = MapUser(2, 2, "pond_sprite", 120, 120, "Pond")
    $ pond_sprite5 = MapUser(2, 3, "pond_sprite", 120, 120, "Pond")
    $ pond_sprite6 = MapUser(2, 4, "pond_sprite", 120, 120, "Pond")
    $ pond_sprite7 = MapUser(3, 2, "pond_sprite", 120, 120, "Pond")
    $ pond_sprite8 = MapUser(3, 3, "pond_sprite", 120, 120, "Pond")
    $ pond_sprite9 = MapUser(3, 4, "pond_sprite", 120, 120, "Pond")
    $ addSprite(bandit_den, bandit_den.playerSprite)
    $ bandit_den.occupy(mimic_sprite1.x, mimic_sprite1.y, mimic_sprite1)
    $ bandit_den.occupy(mimic_sprite2.x, mimic_sprite2.y, mimic_sprite2)
    $ bandit_den.occupy(mimic_sprite3.x, mimic_sprite3.y, mimic_sprite3)
    $ bandit_den.occupy(ward_sprite1.x, ward_sprite1.y, ward_sprite1)
    $ bandit_den.occupy(ward_sprite2.x, ward_sprite2.y, ward_sprite2)
    $ bandit_den.occupy(ward_sprite3.x, ward_sprite3.y, ward_sprite3)
    $ bandit_den.occupy(pond_sprite.x, pond_sprite.y, pond_sprite)
    $ bandit_den.occupy(pond_sprite2.x, pond_sprite2.y, pond_sprite2)
    $ bandit_den.occupy(pond_sprite3.x, pond_sprite3.y, pond_sprite3)
    $ bandit_den.occupy(pond_sprite4.x, pond_sprite4.y, pond_sprite4)
    $ bandit_den.occupy(pond_sprite5.x, pond_sprite5.y, pond_sprite5)
    $ bandit_den.occupy(pond_sprite6.x, pond_sprite6.y, pond_sprite6)
    $ bandit_den.occupy(pond_sprite7.x, pond_sprite7.y, pond_sprite7)
    $ bandit_den.occupy(pond_sprite8.x, pond_sprite8.y, pond_sprite8)
    $ bandit_den.occupy(pond_sprite9.x, pond_sprite9.y, pond_sprite9)
    $ bandit_den.occupy(shelf_sprite.x, shelf_sprite.y, shelf_sprite)
    $ bandit_den.occupy(shelf_sprite2.x, shelf_sprite2.y, shelf_sprite2)
    $ bandit_den.occupy(hole_sprite.x, hole_sprite.y, hole_sprite)
    $ bandit_den.occupy(hole_sprite2.x, hole_sprite2.y, hole_sprite2)
    $ bandit_den.occupy(hole_sprite3.x, hole_sprite3.y, hole_sprite3)
    $ bandit_den.occupy(hole_sprite4.x, hole_sprite4.y, hole_sprite4)
    $ bandit_den.unoccupyback(hole_sprite.x, hole_sprite.y)
    $ bandit_den.unoccupyback(hole_sprite2.x, hole_sprite2.y)
    $ bandit_den.unoccupyback(hole_sprite3.x, hole_sprite3.y)
    $ bandit_den.unoccupyback(hole_sprite4.x, hole_sprite4.y)
    $ bandit_den.occupy(plank_sprite.x, plank_sprite.y, plank_sprite)
    $ bandit_den.occupy(puddle_sprite.x, puddle_sprite.y, puddle_sprite)
    $ bandit_den.occupy(rock_sprite.x, rock_sprite.y, rock_sprite)
    $ bandit_den.occupy(24, 6, leave_sprite)
    if quest11.status != True:
        $ bandit_den.occupy(golem_sprite1.x, golem_sprite1.y, golem_sprite1)
        $ bandit_den.occupy(furkan_sprite.x, furkan_sprite.y, furkan_sprite)
    $ damp_cave_enter += 1


    if damp_cave_enter > 1 and kari_accompany == True:
        scene black
        with dissolve
        scene cave_interior1
        with dissolve
        show kari masked
        with dissolve
        if just_lost:
            $ just_lost = False
            k "You're back, are you prepared now."
            k "I don't want to carry you out of the cave again."
            e "Yes, let's keep going."
            k "I should have drafted my guards instead."
            e "H-hey, I'm a good fighter..."
            "The general stays silent, staring at you blankly."
            e "I-I am!"
            pause 2
            e "Alright, General."
        else:
            k "You're back."
            e "Yes, let's continue with the cave."
            "The general stays silent, staring at you blankly."
            k "I shouldn't wait for you."
            e "Look we can save Furkan together, alright?"
            k "...if you go out one more time I'm going to kill you myself."
            e "Alright, General."

    elif damp_cave_enter == 1:
        $ step = 0


        show screen dungeon_map(bandit_den)
        $ disableC = True
        if kari_accompany:
            k "I did not intend to come back after such a long time."
            e "Huh? Have you been here before?"
            k "So did Furkan, this place was an ancient research post for the origin of the flowing water."
            k "Our guardians, the golems, were first created with the basin from here."
            e "Uh, what's a basin?"
            k "Do you know nothing or what? A basin is a magical container, one that can hold the essence of the water."
            e "Okay, you don't need to be mean about this. I am not from your tribe."
            k "I'm not being mean, I'm just stating the fact."
            e "So, do you create guardians whenever you want?"
            k "No."
            k "You need to have the right gemstone."
            e "Alright."
            k "Stop bickering now, let's go find Furkan, he should be around somewhere."



















    if bandit_den.getMapStatus(chest_sprite) == True:
        $ bandit_den.playerSprite.interaction["chest_1"] = True
    if bandit_den.getMapStatus("chest_1") != True:
        $ chest_sprite = MapUser(8, 12, "chest_sprite", 120, 120, "Chest")

    if bandit_den.getMapStatus(chest_sprite2) == True:
        $ bandit_den.playerSprite.interaction["chest_2"] = True
    if bandit_den.getMapStatus("chest_2") != True:
        $ chest_sprite2 = MapUser(23, 2, "chest_sprite", 120, 120, "Chest2")


    jump Damp_Cave_Loop
label Damp_Cave_Loop:
    $ current_location = bandit_den
    show screen dungeon_buttons
    $ disableC = False
    $ sprite = bandit_den.playerSprite
    call screen dungeon_map(bandit_den)
    if _return == "Furkan":
        $ disableC = True
        if quest11.status == 3:
            e "Furkan?"
            f "Yeah, I'm still here, waiting for the guards."
            e "Oh..."
            e "I should go to the Goat Tribe now."
        else:
            "Furkan seems to be unconscious."

    if _return == "Golem":
        $ disableC = True
        if quest11.status == 2:
            scene black
            with dissolve
            pause 1.0
            scene cave_interior1
            with dissolve
            if kari_accompany == True:
                show kari masked
                with dissolve
                k "Courier, He's right there!"
                e "Uhm? Oh... I see Furkan."
                k "Yes, let's get this over with, Courier."
                k "Kill the Guardian."
            else:
                "You look at the Golem, who Kari told you was the rune guardian."
                "Furkan was behind him, unconscious..."
            menu:
                "Attack the standing Guardian?"
                "Yes{#guardianattack}":

                    jump runeguardian_battle
                "No{#guardianattack}":
                    pass
        else:
            "You look at the Guardian, it seems to be standing here..."

    if _return == "Rock":
        $ disableC = True
        show screen dungeon_map(bandit_den)
        if bandit_den.inventory == None:
            if guardian_alive:
                "There's an ordinary rock on the floor, Do you want to pick it up?"
            else:

                "There's a mossy rock on the floor, it seems to be glowing weakly in blue... Do you want to pick it up?"

            menu:
                "Pick up the Rock?"
                "Yes{#pickuprock}":
                    $ bandit_den.inventory = rock_sprite
                    $ x, y = getFacingTile(sprite)
                    $ bandit_den.unoccupy(x, y)
                "No{#pickuprock}":
                    pass


    if _return == "Plank":
        $ disableC = True
        show screen dungeon_map(bandit_den)

        if bandit_den.inventory == None:
            "There's a wooden plank on the floor, do you want to pick it up?"
            menu:
                "Pick up the plank?"
                "Yes{#pickupplank}":
                    $ bandit_den.inventory = plank_sprite
                    $ x, y = getFacingTile(sprite)
                    $ bandit_den.unoccupy(x, y)
                "No{#pickupplank}":
                    pass

    if _return == "Take Rock":
        $ bandit_den.inventory = rock_sprite
        $ x, y = getFacingTile(sprite)
        $ bandit_den.unoccupy(x, y)

    if _return == "Take Plank":
        $ bandit_den.inventory = plank_sprite
        $ x, y = getFacingTile(sprite)
        $ bandit_den.unoccupy(x, y)

    if _return == "Take Hole Rock":
        $ x, y = getFacingTile(sprite)
        if bandit_den.mappy[y][x].back == None or bandit_den.mappy[y][x].back.interaction != "Hole Rock":
            show screen dungeon_map(bandit_den)
            "You can't take this here."
            jump Damp_Cave_Loop
        if bandit_den.mappy[y][x].back != None and bandit_den.mappy[y][x].back.interaction == "Hole Rock":
            $ bandit_den.inventory = rock_sprite
            $ bandit_den.unoccupyback(x, y)
            $ bandit_den.occupy(x, y, MapUser(x, y, "hole_sprite", 120, 120, "Hole"))

    if _return == "Take Hole Plank":
        $ x, y = getFacingTile(sprite)
        if bandit_den.mappy[y][x].back == None or bandit_den.mappy[y][x].back.interaction != "Hole Plank":
            show screen dungeon_map(bandit_den)
            "You can't take this here."
            jump Damp_Cave_Loop
        if bandit_den.mappy[y][x].back != None and bandit_den.mappy[y][x].back.interaction == "Hole Plank":
            $ bandit_den.inventory = plank_sprite
            $ bandit_den.unoccupyback(x, y)
            $ bandit_den.occupy(x, y, MapUser(x, y, "hole_sprite", 120, 120, "Hole"))

    if _return == "Drop Rock":
        $ disableC = True
        show screen dungeon_map(bandit_den)
        $ x, y = getFacingTile(sprite)
        if bandit_den.isEmpty(x, y) and bandit_den.isEmptyBack(x, y):
            $ bandit_den.inventory = None
            $ bandit_den.occupy(x, y, rock_sprite)

        elif bandit_den.mappy[y][x].user != None:
            if bandit_den.mappy[y][x].user.img == "hole_sprite":
                $ bandit_den.inventory = None
                $ bandit_den.unoccupy(x, y)
                $ bandit_den.occupyback(x, y, MapUser(x, y, "hole_stucked_sprite", 120, 120, "Hole Rock"))
        else:

            "You can't drop it here."

    if _return == "Drop Plank":
        $ disableC = True
        show screen dungeon_map(bandit_den)
        $ x, y = getFacingTile(sprite)
        if bandit_den.isEmpty(x, y) and bandit_den.isEmptyBack(x, y):
            $ bandit_den.inventory = None
            $ bandit_den.occupy(x, y, plank_sprite)

        elif bandit_den.mappy[y][x].user != None:
            if bandit_den.mappy[y][x].user.img == "hole_sprite":
                $ bandit_den.inventory = None
                $ bandit_den.unoccupy(x, y)
                $ bandit_den.occupyback(x, y, MapUser(x, y, "hole_filled_sprite", 120, 120, "Hole Plank"))
        else:

            "You can't drop it here."



    if _return == "Mimic":
        $ mimic_num = 1
        jump Damp_Cave_Mimic
    if _return == "Chest":
        $ chest_num = 1
        $ bandit_den.playerSprite.interaction["chest_1"] = True
        jump Damp_Cave_Chest
    if _return == "Chest2":
        $ chest_num = 2
        $ bandit_den.playerSprite.interaction["chest_2"] = True
        jump Damp_Cave_Chest
    if _return == "Mimic2":
        $ mimic_num = 2
        jump Damp_Cave_Mimic
    if _return == "Mimic3":
        $ mimic_num = 3
        jump Damp_Cave_Mimic
    if _return == "Ward":
        $ ward_num = 1
        jump Damp_Cave_Ward
    if _return == "Ward2":
        $ ward_num = 2
        jump Damp_Cave_Ward
    if _return == "Ward3":
        $ ward_num = 3
        jump Damp_Cave_Ward
    if _return == "Shelf":
        jump Damp_Cave_Shelf
    if _return == "Puddle":
        jump Damp_Cave_Puddle

    if _return == "Leave" or _return == "Exit":
        show screen dungeon_map(bandit_den)
        if kari_accompany == True:
            k "Wait, where are you going?"
            e "I, need to get something..."
            k "But you can't leave me here."
            k "Uhm."
            k "Come back soon."
            e "A-alright. See you, General."
        "You leave the dungeon through the exit tunnel, soon you reach the surface where you came from."
        hide screen dungeon_map
        hide screen dungeon_buttons
        $ removeSprite(bandit_den, sprite)
        scene black
        with dissolve
        pause 1.0

        jump main_damp_cave
    jump Damp_Cave_Loop
label Damp_Cave_Ward:
    $ disableC = True
    show screen dungeon_map(bandit_den)
    "You approach the stone ward in front of you, he doesn't seem to notice you."
    "But he also doesn't move..."
    menu:
        "Should you attack the Stone Ward?"
        "Yes{#attackstoneward}":
            "You jump in front of the stone ward, ready to battle with him."
            jump stoneward_battle
        "No{#attackstoneward}":
            pass
    jump Damp_Cave_Loop
label Damp_Cave_Mimic:
    $ disableC = True
    show screen dungeon_map(bandit_den)
    "You run into a chest in the cave, you walk towards it, trying to open the chest."
    "Suddenly the chest jumps right into your face, it's not a chest, it is a mimic."
    "Mimic" "RAWAWWWR-"
    "You scream, its tongue is slithering out, trying to latch on you..."
    if kari_accompany == True:
        k "W-what did you just do?"
        e "I d-don't know, let's kill it first!"
        k "A-alright."

    jump mimic_battle
label Damp_Cave_Puddle:
    $ disableC = True

    show screen dungeon_map(bandit_den)
    "You discover the puddle in the front."
    "It seems to glowing in blue light but the water is stagnant..."
    menu:
        "Do you drink the water?"
        "Yes{#drinkwater}":
            "You drank the water, it seems to have healed you to full health."
            "But your Lust almost increased by 20."
            $ pc.hp = pc.max_hp
            $ pc.lust += 20
            e "Uhm... that made me feel so hot right now."
            if kari_accompany == True:
                k "W-what?"
                e "I drank the water."
                k "You drank from a dirty puddle on the ground, are you stupid?"
                e "Sorry..."
            "After drinking from the stagnant puddle, you decide to leave."
        "No{#drinkwater}":
            pass

    jump Damp_Cave_Loop

label Damp_Cave_Shelf:
    scene black
    with dissolve
    pause 1.0
    scene cave_interior1
    with dissolve
    if kari_accompany == True:
        show kari masked
        with dissolve
    e "Oh, there's a bookshelf here for some reason."
    "As you are searching around the bookshelf, you found out that most of the books are all unreadable..."
    "But after skimming through most of the shelf, there is a strip of paper that seems to be newer."
    if kari_accompany == True:
        k "Uhm, What did it say...?"
    e "Let me see."
    "You read from the paper..."
    "'T/e blessi/g of Tapj/o: Date/ Year 12/07...'"
    "'Accor/ding to the research by the King's a//isor, Kjarr Eli//.'"
    "'The recent explosion near Kechi//ren ({i}Goat Tr/be/{/i}, seems to /e caused by an unkn//n magi/al force.'"
    "'Thi/ force... o/ what the locals called {i}the Blessing of the Running Go/t{/i}. Has been speculated to contamin//e the water source.'"
    "'The aforement//ned water now appears to display a b/ight blue glow after the e//losion, while provi//ng heal/ng power to the drinker.'"
    "'It is /nknown if ther/ exists any possible side effect.'"
    "'For now, Goat Tri//'s Leader Goek/emir refused to cooperate with ou/ research team."
    "The piece of paper gets cut off here."
    e "Uhm... what a weird piece of information. Who actually writes like that."
    if kari_accompany == True:
        k "Is it talking about our Tribe?"
        e "Yeah."
        k "Goekdemir is Furkan's Great-Grandfather, at least they got it right."
        k "Otherwise, I consider it nothing but gibberish. You should do so as well."
        e "Oh... It is."
    "You put the piece of paper back to the bookshelf."
    if not LookForRecipe(bandanarecipe, discoveredrecipe):
        "You also discovered a recipe for a plain bandana among the books."
        $ discoveredrecipe.append(bandanarecipe)
        e "A plain bandana uses 2 fabric and 1 strap..."
    "After looking into the books, you decide you have discovered everything readable."
    scene black
    with dissolve
    jump Damp_Cave_Loop

label Damp_Cave_Chest:
    show screen dungeon_map(bandit_den)
    "You run into a chest in the cave, you walk towards it, trying to open it anything possible."
    if chest_num == 1:
        $ pc.gold += 100
        $ addItem("Strength Potion", inventory, 2)
        "You discovered 100 gold, and 2 strength potions inside the chest."
        $ bandit_den.unoccupy(8, 12)
    else:


        $ addItem("Iron Ingot", inventory, 4)
        $ pc.gold += 80
        $ discoveredrecipe.append(canvasrecipe)
        "You discovered 80 gold, 4 pieces of iron ingot and a recipe for canvas inside the chest."
        e "To make a canvas, you need... 3 hemps and 2 straps, got it."
        $ bandit_den.unoccupy(23, 2)
    if kari_accompany == True:
        e "Uhm... Kari? You want the stuff inside the chest?"
        k "Keep it, Courier. I just want to save Furk."
        e "Alright! Thanks, General."

    jump Damp_Cave_Loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
