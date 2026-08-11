default d4x = 2
default d4y = 1
default d5x = 2
default d5y = 2
default tenki_sprite4 = MapUser(d4x, d4y, "e_dungeon", 120, 200, no_op)
default tenki_sprite5 = MapUser(d5x, d5y, "e_dungeon", 120, 200, no_op)
default dungeon4_map = [
[MapTile(MapThing("tree3")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree3"))],
[MapTile(MapThing("tree4")), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(), MapTile(MapThing("tree4"))],
[MapTile(MapThing("tree4")), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
[MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("tree4"))],
[MapTile(MapThing("tree4")), MapTile(), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("tree4"))],
[MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
[MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("tree4"))],
[MapTile(MapThing("tree4")), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("tree4"))],
[MapTile(MapThing("tree4")), MapTile(), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5") ), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("tree4"))],
[MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("tree4"))],
[MapTile(MapThing("tree4")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
[MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("tree4"))],
[MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("tree1"))],
[MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2"))]
]

image werewolf_spritea1 = "werewolf [werewolf_sprite_a1.direction]"
image werewolf_spritea2 = "werewolf [werewolf_sprite_a2.direction]"

label Split_Trail_Enter:
    $ dungeon_timers = []
    $ dungeon4_map = [
    [MapTile(MapThing("tree4")), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("cliff2")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5") ), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(MapThing("cliff1")), MapTile(), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("flower_sprite")), MapTile(MapThing("flower_sprite")), MapTile(), MapTile(MapThing("flower_sprite")), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree7")), MapTile(), MapTile(MapThing("tree8")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree7")), MapTile(), MapTile(MapThing("tree8")), MapTile(MapThing("tree1"))],
    [MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(), MapTile(MapThing("tree2")), MapTile(MapThing("tree2"))]
    ]
    $ d4x = 2
    $ d4y = 1
    $ werewolfDa[0] = 0
    $ werewolfDa[1] = 0
    if carrot_check1.check():
        $ carrot_sprite1 = MapUser(2, 4, "carrot_sprite", 120, 120, "Carrot1")
    else:
        $ carrot_sprite1 = MapUser(2, 4, "carrot_sprite_0", 120, 120, "Carrot1")
    if carrot_check2.check():
        $ carrot_sprite2 = MapUser(5, 6, "carrot_sprite", 120, 120, "Carrot2")
    else:
        $ carrot_sprite2 = MapUser(5, 6, "carrot_sprite_0", 120, 120, "Carrot2")
    if carrot_check3.check():
        $ carrot_sprite3 = MapUser(6, 4, "carrot_sprite", 120, 120, "Carrot3")
    else:
        $ carrot_sprite3 = MapUser(6, 4, "carrot_sprite_0", 120, 120, "Carrot3")
    $ leaving_sprite3 = MapUser(2, 0, "cliff2", 120, 120, "Leave")
    $ caproot_sprite1 = MapUser(9, 7, "carrot_sprite", 120, 120, "Caproot1")
    $ caproot_sprite2 = MapUser(3, 11, "carrot_sprite", 120, 120, "Caproot2")
    $ caproot_sprite3 = MapUser(1, 8, "carrot_sprite", 120, 120, "Caproot3")
    $ caproot_sprite4 = MapUser(6, 7, "carrot_sprite", 120, 120, "Caproot4")
    $ tenki_sprite4 = MapUser(d4x, d4y, "e_dungeon", 120, 200, no_op)
    $ cornershade_sprite1 = MapUser(4, 2, "cornershade_sprite", 120, 120, "S")
    $ cornershade_sprite2 = MapUser(7, 2, "cornershade_sprite2", 120, 120, "S")
    $ cornershade_sprite4 = MapUser(10, 7, "cornershade_sprite2", 120, 120, "S")
    $ cornershade_sprite5 = MapUser(1, 3, "cornershade_sprite", 120, 120, "S")
    $ cornershade_sprite6 = MapUser(1, 11, "cornershade_sprite", 120, 120, "S")
    $ cornershade_sprite7 = MapUser(3, 8, "cornershade_sprite", 120, 120, "S")
    $ cornershade_sprite8 = MapUser(8, 3, "cornershade_sprite2", 120, 120, "S")
    $ cornershade_sprite9 = MapUser(4, 10, "cornershade_sprite", 120, 120, "S")
    $ fsign_sprite1 = MapUser(5, 3, "fsign_sprite", 120, 120, "Sign")
    $ fbush_sprite1 = MapUser(3, 12, "fbush_sprite", 120, 120, "Bush")
    $ cliff_sprite4 = MapUser(3, 13, "cliff2", 120, 120, "Cliff5")
    $ tulip_sprite1 = MapUser(3, 8, "tulip_sprite", 120, 120, "Tulip")
    $ pot_sprite1 = MapUser(10, 7, "pot_sprite", 120, 120, "Pot")
    $ potty_sprite1 = MapUser(10, 7, "potty_sprite", 120, 120, "Potty")
    $ cliff_sprite1 = MapUser(2, 10, "cliff2", 120, 120, "Cliff")
    $ cliff_sprite2 = MapUser(11, 3, "cliff2", 120, 120, "Cliff2")
    $ cliff_sprite3 = MapUser(12, 8, "cliff2", 120, 120, "Cliff3")
    $ cliff_sprite6 = MapUser(12, 0, "cliff2", 120, 120, "Cliff6")
    $ barrel_sprite1 = MapUser(1, 5, "barrel_sprite", 120, 120, "Barrel")
    $ barrel_sprite2 = MapUser(2, 5, "barrel_sprite", 120, 120, "Barrel")
    $ barrel_sprite3 = MapUser(4, 4, "barrel_sprite", 120, 120, "Barrel")
    $ barrel_sprite4 = MapUser(7, 4, "barrel_sprite", 120, 120, "Barrel")
    $ barrel_sprite5 = MapUser(7, 5, "barrel_sprite", 120, 120, "Barrel")
    $ barrel_sprite6 = MapUser(7, 6, "barrel_sprite", 120, 120, "Barrel")
    $ barrel_sprite7 = MapUser(8, 6, "barrel_sprite", 120, 120, "Barrel")
    $ barrel_sprite8 = MapUser(4, 3, "barrel_sprite", 120, 120, "Barrel")
    $ barrel_sprite9 = MapUser(6, 3, "barrel_sprite", 120, 120, "Barrel")
    $ barrel_spritea = MapUser(5, 7, "barrel_sprite", 120, 120, "Barrel")
    $ barrel_spriteb = MapUser(4, 7, "barrel_sprite", 120, 120, "Barrel")
    $ cliff_sprite5 = MapUser(11, 13, "cliff2", 120, 120, "Cliff4")
    $ werewolf_sprite_a1 = MapMover(4, 2, "werewolf_spritea1", 140, 204, "Werewolf1", 6, 1, 1)
    $ werewolf_sprite_a2 = MapMover(12, 10, "werewolf_spritea2", 140, 204, "Werewolf2", 6, 1, 2)

    $ step = 0
    hide screen menu_buttons
    show screen dungeon_buttons
    $ split_trail = MapPat(dungeon4_map, "Split Trail", d4x, d4y, "grass2")
    $ current_location = split_trail
    $ addSprite(split_trail, tenki_sprite4)
    $ addSprite(split_trail, tulip_sprite1)
    $ addSprite(split_trail, pot_sprite1)
    $ addSprite(split_trail, carrot_sprite1)
    $ addSprite(split_trail, carrot_sprite2)
    $ addSprite(split_trail, carrot_sprite3)
    $ addSprite(split_trail, caproot_sprite1)
    $ addSprite(split_trail, caproot_sprite2)
    $ addSprite(split_trail, caproot_sprite3)
    $ addSprite(split_trail, leaving_sprite3)
    $ addSprite(split_trail, caproot_sprite4)
    $ addSprite(split_trail, werewolf_sprite_a1)
    $ addSprite(split_trail, werewolf_sprite_a2)
    $ addBack(split_trail, cornershade_sprite1)
    $ addBack(split_trail, cornershade_sprite2)
    $ addBack(split_trail, cornershade_sprite4)
    $ addBack(split_trail, cornershade_sprite5)
    $ addBack(split_trail, cornershade_sprite6)
    $ addBack(split_trail, cornershade_sprite7)
    $ addBack(split_trail, cornershade_sprite8)
    $ addBack(split_trail, cornershade_sprite9)
    $ addBack(split_trail, cliff_sprite1)
    $ addBack(split_trail, cliff_sprite2)
    $ addBack(split_trail, cliff_sprite3)
    $ addSprite(split_trail, cliff_sprite4)
    $ addSprite(split_trail, cliff_sprite5)
    $ addSprite(split_trail, cliff_sprite6)
    $ addSprite(split_trail, fbush_sprite1)
    $ addSprite(split_trail, fsign_sprite1)
    $ addSprite(split_trail, barrel_sprite1)
    $ addSprite(split_trail, barrel_sprite2)
    $ addSprite(split_trail, barrel_sprite3)
    $ addSprite(split_trail, barrel_sprite4)
    $ addSprite(split_trail, barrel_sprite5)
    $ addSprite(split_trail, barrel_sprite6)
    $ addSprite(split_trail, barrel_sprite7)
    $ addSprite(split_trail, barrel_sprite8)
    $ addSprite(split_trail, barrel_sprite9)
    $ addSprite(split_trail, barrel_spritea)
    $ addSprite(split_trail, barrel_spriteb)

    jump Split_Trail_Loop
label Split_Trail_Loop:
    show screen dungeon_buttons
    $ disableC = False
    $ sprite = tenki_sprite4
    call screen dungeon_map(split_trail)
    if _return == "Werewolf1" or enct == "Werewolf1":
        $ mimic_num = 7
        jump Split_Trail_Werewolf
    if _return == "Werewolf2" or enct == "Werewolf2":
        $ mimic_num = 8
        jump Split_Trail_Werewolf
    if _return == "Caproot1":
        $ mimic_num = 1
        jump Split_Trail_Caproot
    if _return == "Caproot2":
        $ mimic_num = 2
        jump Split_Trail_Caproot
    if _return == "Caproot3":
        $ mimic_num = 3
        jump Split_Trail_Caproot
    if _return == "Caproot4":
        $ mimic_num = 4
        jump Split_Trail_Caproot
    if _return == "Carrot1" or _return == "Carrot2" or _return == "Carrot3":
        show screen dungeon_map(split_trail)
        $ disableC = True
        if (_return == "Carrot1" and split_trail.mappy[4][2].user.img == "carrot_sprite") or (_return == "Carrot2" and split_trail.mappy[6][5].user.img == "carrot_sprite") or (_return == "Carrot3" and split_trail.mappy[4][6].user.img == "carrot_sprite"):
            "You come across a carrot plant underneath the grass."
            menu:
                "Do you want to pick it up?"
                "Yes{#pickupcarrots}":
                    "You picked up a carrot, the plant will probably replenish in a few hours."
                    if _return == "Carrot1":
                        $ carrot_sprite1.img = "carrot_sprite_0"
                        $ carrot_check1 = CoolDown(0, 4)
                    if _return == "Carrot2":
                        $ carrot_sprite2.img = "carrot_sprite_0"
                        $ carrot_check2 = CoolDown(0, 4)
                    if _return == "Carrot3":
                        $ carrot_sprite3.img = "carrot_sprite_0"
                        $ carrot_check3 = CoolDown(0, 4)
                    $ addItem("Carrot", inventory, 1)
                "No{#pickupcarrots}":
                    pass
        else:
            "There doesn't seem to be any carrot in this plant, maybe come back later..."
    if _return == "Leave":
        show screen dungeon_map(split_trail)
        $ disableC = True
        if has_agifigurine:
            "You are not sure... if you should leave with the flower in your hand."
            jump Split_Trail_Loop
        menu:
            msg "Do you want to leave the area, states of the dungeon will not be saved."
            "Yes{#leavesplittrail}":
                scene black with dissolve
                call Leaving_Split_Trail from _call_Leaving_Split_Trail

                jump Dark_Forest_Map
            "No{#leavesplittrail}":
                pass
    if _return == "Sign" and tenki_sprite4.x == 5:
        show screen dungeon_map(split_trail)
        $ disableC = True
        if quest22.status == True:
            "Reading... the sign carefully, you notice there is a few lines hidden in the corner of the sign."
            "It says..."
            "{i}To receive the bow of the hunter, one must place barrels around a true carrot in all sides and corners...{/i}"
            if split_trail.mappy[5][4].user != None and split_trail.mappy[5][5].user != None and split_trail.mappy[5][6].user != None and split_trail.mappy[6][4].user != None and split_trail.mappy[6][6].user != None and split_trail.mappy[7][4].user != None and split_trail.mappy[7][5].user != None and split_trail.mappy[7][6].user != None:
                if split_trail.mappy[5][4].user.img == "barrel_sprite" and split_trail.mappy[5][5].user.img == "barrel_sprite" and split_trail.mappy[5][6].user.img == "barrel_sprite" and split_trail.mappy[6][4].user.img == "barrel_sprite" and split_trail.mappy[6][6].user.img == "barrel_sprite" and split_trail.mappy[7][4].user.img == "barrel_sprite" and split_trail.mappy[7][5].user.img == "barrel_sprite" and split_trail.mappy[7][6].user.img == "barrel_sprite":
                    "The carrot plant near the sign suddenly convulses..."
                    if checkNoShopItem("Hunting Bow"):
                        "A hunting bow drops from the carrot plant, you thank whoever is granting you the gift, and pick it up."
                        $ addItem("Hunting Bow", inventory, 1)
                    else:
                        "It seems you already own the bow, the bush slowly stops convulsing..."
        else:
            "There seems to be something underneath the text, maybe you should come back later... after visiting the cavern."
        menu:
            "Do you wish to reset the placement of barrels?"
            "Yes{#resetsplittrailpuzzle}":
                $ removeSprite(split_trail, barrel_sprite1)
                $ removeSprite(split_trail, barrel_sprite2)
                $ removeSprite(split_trail, barrel_sprite3)
                $ removeSprite(split_trail, barrel_sprite4)
                $ removeSprite(split_trail, barrel_sprite5)
                $ removeSprite(split_trail, barrel_sprite6)
                $ removeSprite(split_trail, barrel_sprite7)
                $ removeSprite(split_trail, barrel_sprite8)
                $ removeSprite(split_trail, barrel_sprite9)
                $ removeSprite(split_trail, barrel_spritea)
                $ removeSprite(split_trail, barrel_spriteb)
                $ barrel_sprite1 = MapUser(1, 5, "barrel_sprite", 120, 120, "Barrel")
                $ barrel_sprite2 = MapUser(2, 5, "barrel_sprite", 120, 120, "Barrel")
                $ barrel_sprite3 = MapUser(4, 4, "barrel_sprite", 120, 120, "Barrel")
                $ barrel_sprite4 = MapUser(7, 4, "barrel_sprite", 120, 120, "Barrel")
                $ barrel_sprite5 = MapUser(7, 5, "barrel_sprite", 120, 120, "Barrel")
                $ barrel_sprite6 = MapUser(7, 6, "barrel_sprite", 120, 120, "Barrel")
                $ barrel_sprite7 = MapUser(8, 6, "barrel_sprite", 120, 120, "Barrel")
                $ barrel_sprite8 = MapUser(4, 3, "barrel_sprite", 120, 120, "Barrel")
                $ barrel_sprite9 = MapUser(6, 3, "barrel_sprite", 120, 120, "Barrel")
                $ barrel_spritea = MapUser(5, 7, "barrel_sprite", 120, 120, "Barrel")
                $ barrel_spriteb = MapUser(4, 7, "barrel_sprite", 120, 120, "Barrel")
                $ addSprite(split_trail, barrel_sprite1)
                $ addSprite(split_trail, barrel_sprite2)
                $ addSprite(split_trail, barrel_sprite3)
                $ addSprite(split_trail, barrel_sprite4)
                $ addSprite(split_trail, barrel_sprite5)
                $ addSprite(split_trail, barrel_sprite6)
                $ addSprite(split_trail, barrel_sprite7)
                $ addSprite(split_trail, barrel_sprite8)
                $ addSprite(split_trail, barrel_sprite9)
                $ addSprite(split_trail, barrel_spritea)
                $ addSprite(split_trail, barrel_spriteb)
            "No{#resetsplittrailpuzzle}":
                pass
    if _return == "TulipDead" or enct == "TulipDead":
        $ enct = None
        show screen dungeon_map(split_trail)
        $ disableC = True
        "The flower withers in your hand..."
        $ has_agifigurine = False
        $ addSprite(split_trail, tulip_sprite1)
    if _return == "Tulip":
        show screen dungeon_map(split_trail)
        $ disableC = True
        "There is a flower... on the ground."
        menu:
            "Do you want to carry the flower...? It might wither after a while in your hand."
            "Yes{#tulipcarry}":
                $ agi_num = step
                $ num_tulip = 17
                $ has_agifigurine = True
                $ removeSprite(split_trail, tulip_sprite1)
            "No{#tulipcarry}":
                pass
    if _return == "Bush":
        show screen dungeon_map(split_trail)
        $ disableC = True

        "You notice the bush is blocking the pathway in front of you..."
        "There's a small drawing in the middle of the bush..."
        "Something... flower. And something... in the pot?"
        "You quickly put the drawing back, perhaps there's something that can remove this bush."
    if _return == "Cliff6":
        show screen dungeon_map(split_trail)
        $ disableC = True
        "You enter the northeast of the split trail."
        call Leaving_Split_Trail from _call_Leaving_Split_Trail_5
        jump Uffe_Territory_Quest_Runaways
    if _return == "Cliff5":
        show screen dungeon_map(split_trail)
        $ disableC = True
        if has_agifigurine:
            "You are not sure... if you should leave with the flower in your hand."
            jump Split_Trail_Loop
        if slumbrous_well.discovered == False:
            scene black with dissolve
            "You reach into the pathway in front of you, it seems to lead to the deeper part of the forest..."
            "You follow the step... eventually, you notice an old well in front of you..."
            $ slumbrous_well.discovered = True

            call Leaving_Split_Trail from _call_Leaving_Split_Trail_1

            jump Wuldon_First_Meet
        else:
            scene black with dissolve
            "You walk into the slumbrous well."
            call Leaving_Split_Trail from _call_Leaving_Split_Trail_2

            jump main_slumbrous_well

    if _return == "Cliff4":
        show screen dungeon_map(split_trail)
        $ disableC = True
        if has_agifigurine:
            "You are not sure... if you should leave with the flower in your hand."
            jump Split_Trail_Loop
        scene black with dissolve
        if cavern_entrance.discovered == False:
            "You reach into the pathway in front of you, it seems to lead to the deeper part of the forest..."
            "You follow the step... eventually, you see a cave in front of you..."
            $ cavern_entrance.discovered = True
            call Leaving_Split_Trail from _call_Leaving_Split_Trail_3
            jump Cavern_Entrance_Enter
        else:
            "You walk towards the cavern entrance..."
            call Leaving_Split_Trail from _call_Leaving_Split_Trail_4
            jump Cavern_Entrance_Enter
    if _return == "Pot":
        show screen dungeon_map(split_trail)
        $ disableC = True
        "There is a pot on the grass..."
        if has_agifigurine:
            menu:
                "Do you wish to put the tulip in the pot?"
                "Yes{#tulippotpuzzle}":
                    $ has_agifigurine = False
                    $ pot_sprite1.img = "potty_sprite"
                    $ pot_sprite1.h = 150
                    "It seems that a path has unlocked..."
                    $ removeSprite(split_trail, fbush_sprite1)
                "No{#tulippotpuzzle}":
                    pass


    jump Split_Trail_Loop
label Leaving_Split_Trail:
    $ removeSprite(split_trail, tenki_sprite4)
    $ removeSprite(split_trail, werewolf_sprite_a1)
    $ removeSprite(split_trail, werewolf_sprite_a2)
    $ removeSprite(split_trail, barrel_sprite1)
    $ removeSprite(split_trail, barrel_sprite2)
    $ removeSprite(split_trail, barrel_sprite3)
    $ removeSprite(split_trail, barrel_sprite4)
    $ removeSprite(split_trail, barrel_sprite5)
    $ removeSprite(split_trail, barrel_sprite6)
    $ removeSprite(split_trail, barrel_sprite7)
    $ removeSprite(split_trail, barrel_sprite8)
    $ removeSprite(split_trail, barrel_sprite9)
    $ removeSprite(split_trail, barrel_spritea)
    $ removeSprite(split_trail, barrel_spriteb)
    hide screen dungeon_map
    hide screen dungeon_buttons

    return
label Split_Trail_Werewolf:
    show screen dungeon_map(split_trail)
    $ disableC = True
    $ enct = None
    "As you walk through the forest, you encountered a werewolf."
    "Immediately, you begin to run towards the opposite direction, but soon a dark figure comes into your view."
    e "Fuck..."
    hide screen dungeon_map
    jump werewolf_battle
label Split_Trail_Caproot:
    show screen dungeon_map(split_trail)
    $ disableC = True
    "You come across a carrot plant underneath the grass."
    menu:
        "Do you want to pick it up?"
        "Yes{#pickupcarrotbutcaproot}":
            "As you pick up the carrot, it appears that it takes a little more strength to pull out."
            "You use the strength of your body to pull up the carrot, only to clumsily fall on the ground."
            "As you look up, you only see the carrot begins to strech itself... it is definitely not a carrot."
            "The Caproot monster is now almost bigger than twice your size... you need to defend yourself."
            hide screen dungeon_map
            jump caproot_battle
        "No{#pickupcarrotbutcaproot}":
            jump Split_Trail_Loop

image cward_sprite0:
    "cward_sprite"
    pause 1.25
    "cward_sprite_1"
    pause 0.75
    repeat
image cferal_sprite0:
    "feral_sprite1"
    pause 1.25
    "feral_sprite2"
    pause 0.75
    repeat
default nosferat_sprite1 = MapMover(4, 15, "nosferat_sprite_a", 120, 180, "Nosferat1", 6, 2, 1)
default nosferat_sprite2 = MapMover(8, 9, "nosferat_sprite_b", 120, 180, "Nosferat2", 8, 4, 1)
default nosferat_sprite3 = MapMover(11, 6, "nosferat_sprite_c", 120, 180, "Nosferat3", 6, 1, 1)
default first_chelforte_enter = False
image treem:
    "tree2"
    pause 5
    "treem1"
    pause 0.2
    "treem2"
    pause 0.1
    "treem1"
    pause 0.2
    repeat
image nosferat_sprite_a = "nosferat [nosferat_sprite1.direction]"
image nosferat_sprite_b = "nosferat [nosferat_sprite2.direction]"
image nosferat_sprite_c = "nosferat [nosferat_sprite3.direction]"
image nosferat 1:
    "nosferat_sprite2"
    size (240, 240)
    pause 0.25
    "nosferat_loop1"
image nosferat_loop1:
    "nosferat_sprite1"
    size (240, 240)
    pause 1
    "nosferat_sprite2"
    size (240, 240)
    pause 1
    repeat
image nosferat_loop2:
    "nosferat_sprite3"
    size (240, 240)
    pause 1
    "nosferat_sprite4"
    size (240, 240)
    pause 1
    repeat
image nosferat 2:
    "nosferat_sprite4"
    size (240, 240)
    pause 0.25
    "nosferat_loop2"

label Chelforte_Cavern_Enter:
    if quest28.status != False:
        $ d5x = 23
        $ d5y = 2
    elif quest22.status == True or quest22.status == 3:
        "The... entrance to the cave seems to be blocked for now..."
        jump Dark_Forest_Map
    else:
        $ d5x = 2
        $ d5y = 1
    if first_chelforte_enter == False:
        $ ccore_spritec1 = MapFarmer(11, 8, "cwore", 120, 120, "Core1", 2, 0, "cwore", "ccore_empty")
        $ ccore_spritec2 = MapFarmer(6, 8, "cwore", 120, 120, "Core2", 2, 0, "cwore", "ccore_empty")
        $ ccore_spritec3 = MapFarmer(13, 1, "cwore5", 120, 120, "Core3", 2, 0, "cwore5", "ccore_empty")
        $ ccore_spritec4 = MapFarmer(12, 1, "cwore4", 120, 120, "Core4", 2, 0, "cwore4", "ccore_empty")
        $ ccore_spritec5 = MapFarmer(25, 1, "cwore5", 120, 120, "Core5", 2, 0, "cwore5", "ccore_empty")
        $ ccore_spritec6 = MapFarmer(24, 1, "cwore4", 120, 120, "Core6", 2, 0, "cwore4", "ccore_empty")
        $ ccore_spritec7 = MapFarmer(19, 11, "cwore4", 120, 120, "Core7", 2, 0, "cwore4", "ccore_empty")
        $ ccore_spritec8 = MapFarmer(20, 11, "cwore5", 120, 120, "Core8", 2, 0, "cwore5", "ccore_empty")
        $ ccore_spritec9 = MapFarmer(24, 7, "cwore5", 120, 120, "Core9", 2, 0, "cwore5", "ccore_empty")


        $ ccore_spritec11 = MapFarmer(7, 4, "cwore2", 120, 120, "Core11", 5, 0, "cwore2", "ccore_empty")
        $ ccore_spritec12 = MapFarmer(11, 5, "cwore6", 120, 120, "Core12", 5, 0, "cwore6", "ccore_empty")
        $ ccore_spritec13 = MapFarmer(23, 6, "cwore2", 120, 120, "Core13", 5, 0, "cwore2", "ccore_empty")
        $ ccore_spritec14 = MapFarmer(22, 6, "cwore2", 120, 120, "Core14", 5, 0, "cwore2", "ccore_empty")
        $ ccore_spritec15 = MapFarmer(2, 12, "cwore6", 120, 120, "Core15", 5, 0, "cwore6", "ccore_empty")
        $ ccore_spritec16 = MapFarmer(8, 11, "cwore6", 120, 120, "Core16", 5, 0, "cwore6", "ccore_empty")
        $ ccore_spritec17 = MapFarmer(6, 4, "cwore2", 120, 120, "Core17", 5, 0, "cwore2", "ccore_empty")

        $ ccore_spritec21 = MapFarmer(7, 1, "cwore3", 120, 120, "Core21", 12, 0, "cwore3", "ccore_empty")
        $ ccore_spritec22 = MapFarmer(8, 1, "cwore3", 120, 120, "Core22", 12, 0, "cwore3", "ccore_empty")
        $ ccore_spritec23 = MapFarmer(15, 12, "cwore7", 120, 120, "Core23", 12, 0, "cwore7", "ccore_empty")
        $ ccore_spritec24 = MapFarmer(15, 7, "cwore7", 120, 120, "Core24", 12, 0, "cwore7", "ccore_empty")
        $ ccore_spritec25 = MapFarmer(5, 12, "cwore7", 120, 120, "Core25", 12, 0, "cwore7", "ccore_empty")

        $ first_chelforte_enter = True

    if quest28.status != False:
        $ dungeon5_map = [
    [MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(MapThing("cwall")), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("cwall")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall"))]
    ]
    else:
        $ dungeon5_map = [
    [MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(MapThing("cwall")), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("cwall")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop")), MapTile(MapThing("ctop"))],
    [MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall")), MapTile(MapThing("cwall"))]
    ]

    $ chelforte = MapPat(dungeon5_map, "Chelforte Cavern", d5x, d5y, "cfloor")
    $ dungeon_timers = []
    $ tenki_sprite5 = MapUser(d5x, d5y, "e_dungeon", 120, 200, no_op)
    $ leavecave_sprite1 = MapUser(1, 0, "cstep", 120, 120, "Leave")
    $ leavecave_sprite2 = MapUser(2, 0, "cstep", 120, 120, "Leave")
    $ leavecave_sprite3 = MapUser(3, 0, "cstep", 120, 120, "Leave")
    $ steppy_sprite1 = MapUser(9, 3, "cstep", 120, 120, "Leave")
    $ steppy_sprite2 = MapUser(10, 3, "cstep", 120, 120, "Leave")
    $ steppy_sprite3 = MapUser(13, 4, "cstep", 120, 120, "Leave")
    $ steppy_sprite4 = MapUser(14, 4, "cstep", 120, 120, "Leave")
    $ steppy_sprite5 = MapUser(1, 8, "cstep", 120, 120, "Leave")
    $ steppy_sprite6 = MapUser(2, 8, "cstep", 120, 120, "Leave")
    $ steppy_sprite7 = MapUser(16, 6, "cstep", 120, 120, "Leave")
    $ steppy_sprite8 = MapUser(17, 6, "cstep", 120, 120, "Leave")
    $ steppy_sprite9 = MapUser(25, 10, "cstep", 120, 120, "Leave")
    $ steppy_spritea = MapUser(26, 10, "cstep", 120, 120, "Leave")
    $ steppy_spriteb = MapUser(12, 10, "cstep", 120, 120, "Leave")
    $ steppy_spritec = MapUser(13, 10, "cstep", 120, 120, "Leave")
    $ steppy_sprited = MapUser(22, 8, "cstep", 120, 120, "Leave")
    $ steppy_spritee = MapUser(23, 8, "cstep", 120, 120, "Leave")
    $ steppy_spritef = MapUser(24, 8, "cstep", 120, 120, "Leave")
    $ steppy_spriteg = MapUser(24, 10, "cstep", 120, 120, "Leave")
    $ steppy_spriteh = MapUser(14, 10, "cstep", 120, 120, "Leave")
    $ cplank_sprite1 = MapUser(9, 4, "plank_sprite1", 120, 120, "Plank")
    $ cplank_sprite2 = MapUser(12, 3, "plank_sprite4", 120, 120, "Plank")
    $ cplank_sprite3 = MapUser(1, 7, "plank_sprite3", 120, 120, "Plank")
    $ cplank_sprite4 = MapUser(1, 9, "plank_sprite5", 120, 120, "Plank")
    $ cplank_sprite5 = MapUser(24, 11, "plank_sprite2", 120, 120, "Plank")
    $ cplank_sprite6 = MapUser(12, 11, "plank_sprite6", 120, 120, "Plank")
    $ cplank_sprite7 = MapUser(17, 4, "plank_sprite5", 120, 120, "Plank")
    $ cplank_sprite8 = MapUser(23, 9, "plank_sprite4", 120, 120, "Plank")
    $ cplank_sprite9 = MapUser(13, 5, "plank_sprite1", 120, 120, "Plank")
    $ cplank_sprite11 = MapUser(6, 5, "plank_sprite7", 120, 120, "Plank")
    $ cplank_sprite12 = MapUser(4, 5, "plank_sprite9", 120, 120, "Plank")
    $ cplank_sprite13 = MapUser(5, 10, "plank_sprite9", 120, 120, "Plank")
    $ cplank_sprite14 = MapUser(8, 9, "plank_sprite8", 120, 120, "Plank")
    $ cplank_sprite15 = MapUser(10, 9, "plank_sprite7", 120, 120, "Plank")
    $ cplank_sprite16 = MapUser(19, 3, "plank_sprite0", 120, 120, "Plank")
    $ cplank_sprite17 = MapUser(19, 7, "plank_sprite8", 120, 120, "Plank")
    $ cplank_sprite18 = MapUser(21, 7, "plank_sprite0", 120, 120, "Plank")
    $ cplank_sprite19 = MapUser(10, 12, "plank_sprite9", 120, 120, "Plank")
    $ crock_sprite1 = MapUser(7, 6, "crock_sprite", 120, 120, "Crock")
    $ crock_sprite2 = MapUser(1, 8, "crock_sprite", 120, 120, "Crock")
    $ crock_sprite3 = MapUser(1, 13, "crock_sprite", 120, 120, "Crock")
    $ crock_sprite4 = MapUser(7, 15, "crock_sprite", 120, 120, "Crock")
    $ crock_sprite5 = MapUser(25, 4, "crock_sprite", 120, 120, "Crock")
    $ crock_sprite6 = MapUser(18, 8, "crock_sprite", 120, 120, "Crock")
    $ crock_sprite7 = MapUser(5, 9, "crock_sprite2", 120, 120, "Crock")
    $ crock_sprite8 = MapUser(14, 14, "crock_sprite2", 120, 120, "Crock")
    $ crock_sprite9 = MapUser(24, 10, "crock_sprite2", 120, 120, "Crock")
    $ crock_spritea = MapUser(14, 6, "crock_sprite3", 120, 120, "Crock")
    $ crock_spriteb = MapUser(24, 8, "crock_sprite3", 120, 120, "Crock")
    $ crock_sprited = MapUser(15, 8  , "crock_sprite2", 120, 120, "Crock")
    $ crock_spritee = MapUser(2, 15, "crock_sprite2", 120, 120, "Crock")
    $ crock_spritec = MapUser(1, 1, "crock_sprite2", 120, 120, "Crock")
    $ cwalling_sprite1 = MapUser(9, 15, "cwall2", 120, 120, "Cwalling")

    $ crubble_sprite1 = MapUser(23, 12, "crubble_sprite", 120, 180, "Crubble1")
    $ crubble_sprite2 = MapUser(24, 11, "crubble_sprite2", 120, 180, "Crubble2")
    $ crubble_sprite3 = MapUser(26, 10, "crubble_sprite3", 120, 120, "Crubble3")
    $ crubble_sprite4 = MapUser(25, 11, "empty0", 120, 120, "Crubble3")

    $ cpond_sprite2 = MapUser(22, 3, "pond_sprite", 120, 120, "Pond")
    $ cpond_sprite0 = MapUser(21, 4, "pond_sprite", 120, 120, "Pond")
    $ cpond_sprite3 = MapUser(22, 4, "pond_sprite", 120, 120, "Pond")
    $ cpond_sprite4 = MapUser(25, 3, "pond_sprite", 120, 120, "Pond")
    $ cpond_sprite5 = MapUser(23, 3, "pond_sprite", 120, 120, "Pond")
    $ cpond_sprite6 = MapUser(23, 4, "pond_sprite", 120, 120, "Pond")
    $ cpond_sprite7 = MapUser(25, 4, "pond_sprite", 120, 120, "Pond")
    $ cpond_sprite8 = MapUser(24, 3, "pond_sprite", 120, 120, "Pond")
    $ cpond_sprite9 = MapUser(24, 4, "pond_sprite", 120, 120, "Pond")
    $ cpond_sprite1 = MapUser(26, 3, "pond_sprite", 120, 120, "Pond")
    if quest28.status != False:
        if quest28.status == 2:
            $ vurro_sprite1 = MapUser(24, 2, "vurro_sprite1", 130, 195, "Vurro")
            $ addSprite(chelforte, vurro_sprite1)
        if quest28.status == 3:
            $ vurro_sprite1 = MapUser(25, 9, "vurro_sprite1", 130, 195, "Vurro")
            $ addSprite(chelforte, vurro_sprite1)
            $ wuldon_sprite1 = MapUser(17, 8, "wuldon_sprite1", 130, 200, "Wuldon")
            $ addSprite(chelforte, wuldon_sprite1)
            $ wuldon_sprite2 = MapUser(18, 8, "empty0", 120, 120, "Wuldon")
            $ addSprite(chelforte, wuldon_sprite2)
        $ crubble_sprite7 = MapUser(7, 9, "crubble_sprite3", 120, 120, "Crubble7")
        $ addSprite(chelforte, crubble_sprite7)
        $ crubble_sprite8 = MapUser(5, 10, "crubble_sprite2", 120, 180, "Crubble7")
        $ addSprite(chelforte, crubble_sprite8)
        $ nosferat_sprite1 = MapMover(4, 15, "nosferat_sprite_a", 120, 180, "Nosferat1", 6, 2, 1)
        $ nosferat_sprite2 = MapMover(8, 9, "nosferat_sprite_b", 120, 180, "Nosferat2", 8, 4, 1)
        $ nosferat_sprite3 = MapMover(11, 6, "nosferat_sprite_c", 120, 180, "Nosferat3", 6, 1, 1)
        $ addSprite(chelforte, nosferat_sprite1)
        $ addSprite(chelforte, nosferat_sprite2)
        $ addSprite(chelforte, nosferat_sprite3)
        $ cward_sprite1 = MapUser(8, 2, "cward_sprite0", 120, 150, "Ward1")
        $ cward_sprite2 = MapUser(1, 7, "cward_sprite0", 120, 150, "Ward2")
        $ addSprite(chelforte, cward_sprite1)
        $ addSprite(chelforte, cward_sprite2)
    else:

        $ addSprite(chelforte, crock_sprite6)
        $ crubble_sprite5 = MapUser(16, 6, "crubble_sprite", 120, 180, "Crubble5")
        $ crubble_sprite6 = MapUser(17, 6, "empty0", 120, 120, "Crubble5")
        $ addSprite(chelforte, crubble_sprite5)
        $ addSprite(chelforte, crubble_sprite6)
        $ cward_sprite1 = MapUser(9, 9, "cward_sprite0", 120, 150, "Ward1")
        $ cward_sprite2 = MapUser(19, 3, "cward_sprite0", 120, 150, "Ward2")
        $ cward_sprite3 = MapUser(5, 5, "cward_sprite0", 120, 150, "Ward3")
        $ addSprite(chelforte, cward_sprite1)
        $ addSprite(chelforte, cward_sprite2)
        $ addSprite(chelforte, cward_sprite3)
        $ cferal_sprite1 = MapUser(16, 14, "cferal_sprite0", 120, 240, "Feral")
        $ addSprite(chelforte, cferal_sprite1)
    $ chelforte.entranceCount += 1
    $ addSprite(chelforte, leavecave_sprite1)
    $ addSprite(chelforte, leavecave_sprite2)
    $ addSprite(chelforte, cwalling_sprite1)
    $ addSprite(chelforte, leavecave_sprite3)
    $ addBack(chelforte, steppy_sprite1)
    $ addBack(chelforte, steppy_sprite2)
    $ addBack(chelforte, steppy_sprite3)
    $ addBack(chelforte, steppy_sprite4)
    $ addBack(chelforte, steppy_sprite6)
    $ addBack(chelforte, steppy_sprite5)
    $ addBack(chelforte, steppy_sprite7)
    $ addBack(chelforte, steppy_sprite8)
    $ addBack(chelforte, steppy_sprite9)
    $ addBack(chelforte, steppy_spritea)
    $ addBack(chelforte, steppy_spriteb)
    $ addBack(chelforte, steppy_spritec)
    $ addBack(chelforte, steppy_sprited)
    $ addBack(chelforte, steppy_spritee)
    $ addBack(chelforte, steppy_spritef)
    $ addBack(chelforte, steppy_spriteg)
    $ addBack(chelforte, steppy_spriteh)
    $ addBack(chelforte, cplank_sprite1)
    $ addBack(chelforte, cplank_sprite2)
    $ addBack(chelforte, cplank_sprite3)
    $ addBack(chelforte, cplank_sprite4)
    $ addBack(chelforte, cplank_sprite5)
    $ addBack(chelforte, cplank_sprite6)
    $ addBack(chelforte, cplank_sprite7)
    $ addBack(chelforte, cplank_sprite8)
    $ addBack(chelforte, cplank_sprite9)
    $ addBack(chelforte, cplank_sprite11)
    $ addBack(chelforte, cplank_sprite12)
    $ addBack(chelforte, cplank_sprite13)
    $ addBack(chelforte, cplank_sprite14)
    $ addBack(chelforte, cplank_sprite15)
    $ addBack(chelforte, cplank_sprite16)
    $ addBack(chelforte, cplank_sprite17)
    $ addBack(chelforte, cplank_sprite18)
    $ addBack(chelforte, cplank_sprite19)
    $ addSprite(chelforte, crock_sprite1)
    $ addSprite(chelforte, crock_sprite2)
    $ addSprite(chelforte, crock_sprite3)
    $ addSprite(chelforte, crock_sprite4)
    $ addSprite(chelforte, crock_sprite5)

    $ addSprite(chelforte, crock_sprite7)
    $ addSprite(chelforte, crock_sprite8)
    $ addSprite(chelforte, crock_sprite9)
    $ addSprite(chelforte, crock_spritea)
    $ addSprite(chelforte, crock_spriteb)
    $ addSprite(chelforte, crock_spritec)
    $ addBack(chelforte, crock_sprited)
    $ addSprite(chelforte, crock_spritee)

    $ addSprite(chelforte, cpond_sprite1)
    $ addSprite(chelforte, cpond_sprite2)
    $ addSprite(chelforte, cpond_sprite3)
    $ addSprite(chelforte, cpond_sprite4)
    $ addSprite(chelforte, cpond_sprite5)
    $ addSprite(chelforte, cpond_sprite6)
    $ addBack(chelforte, cpond_sprite7)
    $ addSprite(chelforte, cpond_sprite8)
    $ addSprite(chelforte, cpond_sprite9)
    $ addSprite(chelforte, cpond_sprite0)
    $ addSprite(chelforte, ccore_spritec1)
    $ addSprite(chelforte, ccore_spritec2)
    $ addSprite(chelforte, ccore_spritec3)
    $ addSprite(chelforte, ccore_spritec4)
    $ addSprite(chelforte, ccore_spritec5)
    $ addSprite(chelforte, ccore_spritec6)
    $ addSprite(chelforte, ccore_spritec7)
    $ addSprite(chelforte, ccore_spritec8)
    $ addSprite(chelforte, ccore_spritec9)
    $ addSprite(chelforte, ccore_spritec11)
    $ addSprite(chelforte, ccore_spritec12)
    $ addSprite(chelforte, ccore_spritec13)
    $ addSprite(chelforte, ccore_spritec14)
    $ addSprite(chelforte, ccore_spritec15)
    $ addSprite(chelforte, ccore_spritec16)
    $ addSprite(chelforte, ccore_spritec17)
    $ addSprite(chelforte, ccore_spritec21)
    $ addSprite(chelforte, ccore_spritec22)
    $ addSprite(chelforte, ccore_spritec23)
    $ addSprite(chelforte, ccore_spritec24)
    $ addSprite(chelforte, ccore_spritec25)
    $ addSprite(chelforte, crubble_sprite1)
    $ addSprite(chelforte, crubble_sprite2)
    $ addSprite(chelforte, crubble_sprite3)
    $ addSprite(chelforte, crubble_sprite4)



    $ addSprite(chelforte, tenki_sprite5)
    $ current_location = chelforte
    $ step = 0
    hide screen menu_buttons
    show screen dungeon_buttons

    jump Chelforte_Cavern_Loop
label Chelforte_Cavern_Loop:
    show screen dungeon_buttons
    $ disableC = False
    $ sprite = tenki_sprite5
    if enct == "Nosferat1" or _return == "Nosferat1":
        $ mimic_num = 1
        jump Chelforte_Nosferat
    if enct == "Nosferat2" or _return == "Nosferat2":
        $ mimic_num = 2
        jump Chelforte_Nosferat
    if enct == "Nosferat3" or _return == "Nosferat3":
        $ mimic_num = 3
        jump Chelforte_Nosferat

    call screen dungeon_map(chelforte)
    if _return == "Vurro":
        jump Chelforte_Vurro

    if _return == "Pond":
        "You jump into the water and quickly leave the cave..."
        if quest28.status != False and quest28.status != True:
            "You look back, Wuldon and Vurro are still working, you have to be quick before returning to them again."

        call Leaving_Chelforte from _call_Leaving_Chelforte_2
        jump Dark_Forest_Map
    if _return == "Core1":
        $ mimic_num = 1
        jump Chelforte_Cavern_Ore1
    if _return == "Core2":
        $ mimic_num = 2
        jump Chelforte_Cavern_Ore1
    if _return == "Core3":
        $ mimic_num = 3
        jump Chelforte_Cavern_Ore1
    if _return == "Core4":
        $ mimic_num = 4
        jump Chelforte_Cavern_Ore1
    if _return == "Core5":
        $ mimic_num = 5
        jump Chelforte_Cavern_Ore1
    if _return == "Core6":
        $ mimic_num = 6
        jump Chelforte_Cavern_Ore1
    if _return == "Core7":
        $ mimic_num = 7
        jump Chelforte_Cavern_Ore1
    if _return == "Core8":
        $ mimic_num = 8
        jump Chelforte_Cavern_Ore1
    if _return == "Core9":
        $ mimic_num = 9
        jump Chelforte_Cavern_Ore1
    if _return == "Core11":
        $ mimic_num = 1
        jump Chelforte_Cavern_Ore2
    if _return == "Core12":
        $ mimic_num = 2
        jump Chelforte_Cavern_Ore2
    if _return == "Core13":
        $ mimic_num = 3
        jump Chelforte_Cavern_Ore2
    if _return == "Core14":
        $ mimic_num = 4
        jump Chelforte_Cavern_Ore2
    if _return == "Core15":
        $ mimic_num = 5
        jump Chelforte_Cavern_Ore2
    if _return == "Core16":
        $ mimic_num = 6
        jump Chelforte_Cavern_Ore2
    if _return == "Core17":
        $ mimic_num = 7
        jump Chelforte_Cavern_Ore2
    if _return == "Core21":
        $ mimic_num = 1
        jump Chelforte_Cavern_Ore3
    if _return == "Core22":
        $ mimic_num = 2
        jump Chelforte_Cavern_Ore3
    if _return == "Core23":
        $ mimic_num = 3
        jump Chelforte_Cavern_Ore3
    if _return == "Core24":
        $ mimic_num = 4
        jump Chelforte_Cavern_Ore3
    if _return == "Core25":
        $ mimic_num = 5
        jump Chelforte_Cavern_Ore3

    if _return == "Ward1":
        $ ward_num = 1
        jump Chelforte_Cavern_Ward
    if _return == "Ward2":
        $ ward_num = 2
        jump Chelforte_Cavern_Ward
    if _return == "Ward3":
        $ ward_num = 3
        jump Chelforte_Cavern_Ward
    if _return == "Cwalling" and quest28.status != False:
        show screen dungeon_map(chelforte)
        $ disableC = True
        "You find a small hole partway up the wall at the end of the cavern. Judging by the small pile of rocks at its foot, it was revealed after the cavern collapsed."

        if quest28.status == True:
            msg "Work in Progress!"
            jump Chelforte_Cavern_Loop

        if not (nosferat_sprite1.death == True and nosferat_sprite2.death == True and nosferat_sprite3.death == True):
            "There's still monsters nearby, you decide it's better not to get yourself stuck while the nosferats... swing their meat around the cave."
            jump Chelforte_Cavern_Loop

        menu:
            "Do you want to go through the hole?"
            "Yes{#chelfortehole}":
                jump Chelforte_Discovery
            "No{#chelfortehole}":
                "Deciding you shouldn't go in for now, you turn around to keep exploring for a while."
    if _return == "Wuldon":
        jump Chelforte_Wuldon
    if _return == "Crubble5":
        show screen dungeon_map(chelforte)
        $ disableC = True
        "You look at the rubble in front of you..."
        "It doesn't seem like you can fit through it at all."
    if _return == "Feral":
        show screen dungeon_map(chelforte)
        $ disableC = True
        "You try to look at the Feral Werewolf... It is much different than the normal werewolves you're encountered..."
        "The monster in front of you, there's a lack of compassion in his face... only beastly instinct."
        if wuldon_meet:
            "You remember Wuldon telling you about his past... and seeing the lifeless husk of a man like him now, only brings you grief and remorse..."
        else:
            "Whoever he was, it doesn't matter now."
        "The beast howls."
        "It sprints towards you with full force, there's no time to think now..."
        jump feral_battle


    if _return == "Crubble3" or _return == "Crubble1" or _return == "Crubble2":
        show screen dungeon_map(chelforte)
        $ disableC = True
        if quest28.status != False:
            "The entrance has been sealed tight since the cave-in from your last visit..."
            jump Chelforte_Cavern_Loop
        "You look at the tight hole in front of you, you notice there's a moving figure on the other side of the rubble..."
        "The hole in front of you is too small to fit through."
        "Perhaps... if you have enough Agility, you can maybe fit through the hole..."
        "But it's very possible you might get stuck in the hole while the figure is approaching you."
        menu:
            "What should you do?"
            "Go through the hole":
                scene black with dissolve
                "You crawl into the tight hole, exhaling all air inside of you..."
                if 10*renpy.random.random() > pc.agi:
                    "Regardless of how much you breath, you soon realises you cannot make it."
                    "In the attempt to escape, you lost 30 health."
                    $ pc.hp -= 30
                    if pc.hp < 0:
                        $ pc.hp = 0
                    "Fortunately, you escaped unscathed, but you believe that you can make it in...if you try again maybe."
                else:
                    "You make it through, rather easily."
                    "Soon, you are at the other side of the hole, without the figure noticing."

                    $ chelforte.moveTo(sprite.x, sprite.y, 20 - sprite.x, 14 - sprite.y)
            "Leave":


                pass
    if _return == "Leave":
        show screen dungeon_map(chelforte)
        $ disableC = True
        if quest28.status != False:
            "The Entrance to the cave seems to be blocked..."
        else:
            menu:
                msg "Do you want to leave the area, states of the dungeon will not be saved."
                "Yes{#leavechelforte}":
                    scene black with dissolve
                    call Leaving_Chelforte from _call_Leaving_Chelforte

                    jump Dark_Forest_Map
                "No{#leavechelforte}":
                    pass
    jump Chelforte_Cavern_Loop
label Chelforte_Discovery:
    hide screen dungeon_map
    hide screen dungeon_buttons
    scene black
    pause 1 
    scene chelforte_cavern with dissolve

    "The hole is a bit too high up for you to reach easily."
    "Despite this, you muster up your courage, and jump up for the entrance."
    "As your hands grab the tunnel's mouth, you feel it begin to give under your weight."
    "Panicked, you begin scrabbling your way up, half pulling-half launching yourself up into the tunnel."
    "The tunnel's mouth is a good bit wider after all is said and done, but you've made it in."
    "The cave-in seems to have loosened up some of the rock around here. Looking closely, you can see hairline cracks in the stone beneath you, fractures caused by the vibrations left by the cave-in."
    "Luckily for you, the rock above you seems perfectly stable, clearly unaffected by whatever made the rocks below susceptible to the crash."
    "The tunnel goes diagonally down, a brief little thing. As you make your way down the increasingly claustrophobic tunnel, you begin to notice a gentle blue glow coming from in front of you."
    with vpunch
    "When you finally pop out on the other side of the hole, you find yourself in a large cavern, a ceiling perfectly black with moss but for crystals on the roof, gently reflecting blue light from the pond on the other end of the room."
    "Despite being deep underground, you feel like you are looking at the night sky. It is a mesmerizing sight, lights dancing in the crystals unceasingly."
    "Snapping yourself out of your daze, you move forward to the source of light."
    "As you thought, it is the water at the end of the cave that emits light. Whether it is the water itself, or some tiny creature within, you cannot tell."
    "You should go report this to Vurro and Wuldon."
    "Moving towards the hole in the wall, you realize a small mistake you've made. It's fairly easy to go down a tunnel. The inverse cannot be said."
    "As you try to move back into the hole despite that, you soon find yourself stuck."
    with vpunch
    "You try to move backwards, backing out of the tunnel, but find you cannot, as the rock presses down against your sides such that your arms find little purchase to push yourself backwards with."
    with vpunch
    pause 1
    with vpunch
    "At that moment, you realize where you are."
    "Trapped in a tiny tunnel inside of a cave prone to cave-ins."
    "Suddenly the minor pricks of stones poking into your skin stop being as unimportant."
    "The dearth of space, to the point of trapping your arms of head, makes your breath pick up as you fight against a rising feeling of panic."
    "Stuck as you are, and having no other recourse, you begin to yell for Vurro and Wuldon."
    "Soon, you hear the echoes of distant footsteps growing near."
    w "-ne?!"
    e "I'm here! In the hole in the wall!"
    "Your voice is deafening in your ears, echoing off of the tunnel walls."
    "Upon hearing your voice, the boots approach even faster, until they stop only a few feet above your head."
    if wuldon_like > 4:
        w "Are you safe, little one?!"
        "You've never heard the werewolf get this scared, he sounds nearly panicked with worry."
        e "Mmph. Mouth is full of dirt, and I'm stuck in a hole. Otherwise, I'm fine."
        w "No imminent danger?"
        e "No."
        "You hear an exasperated sigh from above you."
        w "Please don't scare me like that again."
        "There is nothing you can say to that."
    else:
        w "Are you in danger?"
        e "Not any immediate danger, no."
        w "That's good."
        w "I assume you're just stuck?"
        "You try to wiggle your arms, and find once again your space is too small for you to even readjust slightly."
        e "Yes, but it's really quite uncomfortable. Is there some way you could get me out?"
        w "It's possible to dig you out, but it would take a while."
    v "We could just leave him down there for a while to see if he learns."
    "It seems Vurro is here too."
    "Judging from the dull thwack above you, it also seems that Wuldon has made very clear to Vurro what he thinks of the idea."
    v "I was kidding, of course I wouldn't leave him down here."
    w "That's why I hit you softly."
    e "Hey, can you two bicker later please? I'd really like to get out now!"
    "There's a brief pause. You can almost feel the two of them looking down at you from above."
    w "Maybe we should just leave him here."
    e "Please don't."
    "You hear a soft snort from outside the tunnel."
    w "Fine, fine. We'll get you out."
    w "Give us a second to grab our shovels – the ground here seems loose enough for us to dig you out easily."
    if wuldon_like > 4:
        e "Can you stay, please? I don't want to be left alone down here."
        w "... Okay. I'll sit down next to the tunnel for you."
        "You hear a quiet shifting sound, followed by a soft whumph as the werewolf sits down."
        w "Sorry to trouble you, Vurro, but could you-"
        v "Don't worry about it, I'll go get the shovels."
        "You hear the other werewolf's footsteps grow distant. Soon, It's just you and Wuldon here."
        "Neither of you say anything. Despite that, you feel much safer. You can hear Wuldon's breathing, the small rustles of his movement."
        "You know he's here, and that he's staying vigilant for you."
        "Before you realize it, Vurro is already back with the shovels."
    else:
        "You hear the footsteps of somebody going to find the shovels."
        v "Hey. I decided to stay behind and make sure you got out okay."
        e "Shouldn't you be with Wuldon right now?"
        "You get the distinct feeling that Vurro is waving his hand at that, dismissing the thought outright."
        v "He'll get the shovels for me."
        "The two of you wait in awkward silence. You feel a rock digging into your stomach."
        v "You comfortable down there?"
        e "No. I'd really prefer to be out of here, if I'm being honest."
        v "Well, you're gonna be down there for a bit. Do you mind if I ask you a serious question?"
        v "I'd like to learn a bit more about the person who saved me."
        e "Sure, I don't see why not."
        "If you could hear a smile, you're pretty sure you did just now."
        v "Great!"
        v "So, do you have any hopes for the future?"
        "Starting out swinging, huh. Makes sense for a dead man, all things considered."
        e "What do you mean exactly?"
        v "Whatever you want it to mean, really. For example, is there something you want to have happen between the werewolves and Lusterfield?"
        "Yet again, Vurro is asking questions that you haven't really given much thought."
        e "I... don't know."
        v "Come on, there has to be {i}something{/i}."
        e "..."
        e "I want to know what caused the war with the goats. Why the magic is disappearing."
        e "Why I'm here."
        "You hear a chuckle from above you."
        v "I think Wuldon's coming back, so I'll keep it short, but..."
        v "I hope you figure it out."
        "Vurro straightens up, and leans against the wall. At least you think he does."
        v "Took you long enough."
        w "I'm going to hit you over the head with this shovel."
        "Both voices are extremely close above you now. It seems Wuldon walked over without you hearing his footsteps."
    w "I'd recommend you cover your ears if you can. If not... my condolences."
    with vpunch
    "Having said that Wuldon grips his shovel and slams it into the ground at full force. At least, you hope it's full force, as the metallic clang that fills your ears makes it feel like it was your skull that was split in two."
    with vpunch
    "Immediately following is another earsplitting peal, as Vurro's shovel hits the ground."
    with vpunch
    with vpunch
    "For hours, all you can hear is the banging of metal on stone, floor steadily making way for the werewolves."
    with vpunch
    with vpunch
    "As is smart of them, they dig diagonally down, using the cave's natural structure to reduce the work required."
    with vpunch
    "Eventually, the tip of Wuldon's boot enters your view."
    e "Be careful for this part! You're getting close to me!"
    "All you get are tired grunts of assent."
    "Even if the floor is weaker after the cave-in, it's still a fast pace, and enormous amount of work the two are undertaking for you."
    "Luckily, they're also nearing the cave you found."
    "The sound of metal on rock is far gentler now. Their shovels still pierce the earth, but with a delicacy previously absent."
    "Your ears still ache, but there's room for thought in your brain now, your voice no longer drowned out by the scream of metal."
    "The hole is still eminently uncomfortable, however. The closer the shovels get, the more dirt and stone falls from the ceiling onto your head."
    with vpunch
    "Within the first 30 minutes, the first shovel breaks ground above you."
    "Already you feel relief as a part of your prison breaks. You rotate your wrists gently, stretching your body where you couldn't before."
    "Bit by bit the shovels uncover and more of you. First your hands, then your head, and finally, your shoulders."
    with vpunch
    "As soon as they reach a part of your body they can reach, the shovelling stops."
    with vpunch
    with vpunch
    with vpunch
    "You feel a strong pair of hands reach down and tug you gently. It is difficult not to cry out in pain as your belly scrapes the ground, jagged pieces of rock dragging through your skin."
    "Half of your body is out now. The hands continue pulling you, but another pair begins patting down your back."
    with vpunch
    with vpunch
    v "You really need to be cleaned, you look like a statue."
    e "Having rocks and dust rain on you for hours on end will do that to you."
    with vpunch
    "As your legs finally leave the tunnel, your body completely free of the tunnel, you find yourself thrown onto someone's - Wuldon - back like a sack of potatoes."
    with vpunch
    show wuldon normal with dissolve

    e "It's alright! I'm out! I'm out! My legs still work, Wuldon!"
    "Wuldon begins running to the mouth of the tunnel, as if you had said nothing."
    w "I know, but you're filthy, and now we are too."

    "A confusing statement, but one you're too tired to argue with right now."
    "The only sounds in the tunnel are the echoes of Wuldon's feet on the ground, a rythmic beat steady as the tick of a clock."
    "It isn't long before you find yourself staring at the pool of water you entered from."
    w "You good to go in?"
    e "You're not going to throw me or something?"
    "Wuldon shakes his head, his fur brushing against your stomach."
    w "I think you deserve a break. Being stuck in a hole isn't fun."
    "A sigh escapes your lips as Wuldon puts you down."
    e "It isn't."
    if wuldon_like > 4:
        e "You werewolves seem to like the experience though."
        "It takes Wuldon a second to get it, at which point he laughs uproariously."
        w "Some don't - I'm glad I've never had to deal with having a knot, that's for sure."
        pause 1
        "You raise an eyebrow at that as Wuldon swings his arm around your side, pulling you into a semi-casual half hug."
        w "God knows it would make going multiple rounds or cuddling harder."
        "As you struggle to find a proper answer to that, Wuldon lets go off you."

    w "Well. Let's get clean, shall we?"
    "The blue werewolf immediately cannonballs into the water, covering your entire lower half with water."
    "Inspired by this, you take a running start and do the same."
    "You can feel the rocks leave your fur as you meet the water. The initial dive was enough to return your skin to its brown color, rather than the dull gray of before."
    "Sinking down into the dark depths, you take a moment to rub your body, pushing loose more and more rocks until you feel acceptably rock free."
    "Once done, you reach for the surface, swimming towards the torchlight."
    "Your head surges free of the water as you take a breath."
    e "Won't we not be able to breath if you put up a torch?"
    "The blue werewolf gives you a small shrug."
    w "I made a hole in the ceiling, remember?"
    w "Not sure if it's enough to supply three people and a torch, but only one way to find out, right?"
    pause 1
    "Unconcerned by the look of horror on your face, Wuldon turns back to the tunnel they got you out of. After a few moments of shock, you give choice."
    e "Hey, you're kidding, right?"
    "Wuldon gives you a lighthearted chuckle."
    w "What do you think, little one?"
    e "That you're messing with me."
    w "Attaboy."
    e "Were you going to say that regardless of what I said?"
    "Wuldon grins mischievously, eyes shining playfully."
    w "Maybe."
    "You get the feeling that's the most you're getting out of him, at least right now."
    w "So, anything of interest in that tunnel?"
    "You give your best smirk."
    e "Maybe."
    w "Ah, that's a yes. Good."
    "Not responding is the best you can do to maintain even a shred of ambiguity. Even if Wuldon guessed correctly, he might still doubt himself."
    "The two of you eventually reach the tunnel's entrance, where a sleepy Vurro sits with his back to the wall."
    "Wuldon bends down and gently shakes his friend's drowsiness away."
    w "Come on, we have to finish excavating the tunnel."
    "A halfway alert Vurro complies with his friend's demands, getting up and grabbing a shovel."
    show wuldon normal at l1 with move
    show vurro clothed at r1 with dissolve
    v "You can rest for a bit, [e], the tunnel is almost done, and I want to be the one to finish it. Well, with Wuldon, I mean."
    "The other werewolf rolls his eyes and strikes the ground without ceremony."
    "Vurro rushes after Wuldon and begins to do his part as well."
    "You drift off to the screech of the shovels, and the grunts of both werewolves pushing themselves."
    "It's pretty awful background noise, but you're too tired to care right now."
    scene black with dissolve2
    pause 1
    scene chelforte_cavern with dissolve2
    "The ground is softer than I thought..."
    scene black with dissolve2
    pause 1
    "Not... Compla..."
    "..."
    scene buriedshimmer with dissolve3
    "The ground is back to being hard rock again, much to your chagrin."
    "You can't quite bring yourself to care. You're tired, and they found the cave. That's all that matters."
    w "Finally waking up, little one?"
    show wuldon normal with dissolve
    if wuldon_like > 4:
        "He says this gently, as if afraid to disrupt your slumber."
    e "Mrrg."
    "Wuldon chuckles softly at your sleepy tone."
    "Looking over, you see him by your side, looking up at the roof of the cavern."
    w "It's a beautiful place you found here, little one."
    if cavern_help[0] > 0:
        w "This is what I meant when I called you a lucky charm."
    "You shift a bit on the floor, trying to find a softer spot."
    e "mrrf. Thanks..."
    "You stretch a bit, trying to work out the tension in your back. A few pops later, and your body floods with relief."
    if wuldon_like > 4:
        w "Looks like you're having trouble sleeping on the ground."
        "The werewolf shifts closer, so that your shoulder and his just barely don't touch."
        w "You mind if I help with that?"
        menu:
            "Accept Wuldon's Help?"
            "Yes{#letwuldonhelp}":
                $ wuldon_like += 1
                "Rather than speak, your response is to shift closer to Wuldon."
                "Wuldon shifts his body to face you, a small smile telling you all you need to know."
                "The blue werewolf wraps his arm across your front, as his other arm moves lower and grabs you by the legs."
                w "Here."
                "Wuldon picks you up gently, and slowly pulls you flush against his chest, ready to let go if you make even the slightest protest."
                "Letting it happen, you find yourself tucked next to the werewolf, his chin resting on your head between your horns."
                "He's warm. From his soft belly to the muscley arm you use as a pillow, his entire body radiates heat, a roaring hearth in the body of a man."
                "His other arm rests around your belly, hand idly scratching the fur within its reach."
                w "Better?"
                "He already knows, but he wants to hear you say it. For pride, or to tease you, you can't tell."
                "Too tired for words, you just nuzzle closer to Wuldon."
                "It seems this is answer enough for him, as he lets out a contented sigh above you."
                "You hate to break the happy silence, but you had a few questions to ask the big wolf."
                "At least he can still hold you as he answers."
            "No{#letwuldonhelp}":
                e "Sorry, I think it'd be better to try and figure it out on my own."
                "The werewolf's content expression looks strained as you say that."
                w "Alright. Good luck with that."
                "He shifts back to where he was."
    "Quietly, you speak back up, each word a challenge to form."
    e "Wuldon... where's Vurro."
    w "He's checking out the minerals in the area."
    w "They're fairly promising, apparently."
    "This is punctuated by a massive yawn."
    e "We... oof. We sleeping here?"
    w "We were planning to. It's alright if you have things to attend to."
    "Even if you wanted, you're too tired to go do them. It's been a long day."
    e "mrrg."
    w "Agreed."
    "Despite saying that, the two of you keep your eyes open for a bit, drinking in the mood."
    if wuldon_like > 5:
        "It was hard not to, considering the warm, hard lump poking into your back."
        "Neither of you outright acknowledged it or your own erection, not willing to do more than flirt right now, tired as you are."
        "Of course, Wuldon didn't quite let you go to sleep without telling you he knew, as his hand drifted further and further down your belly, until it occasionally brushed your tip when he scratched you."
        "The only revenge you could get on the werewolf was readjusting slightly every so often to tug on his shaft a bit."
        "Every time you did, Wuldon would let out a small growl and hump gently into your back."
        "Eventually, the two of you quiet down and return to cuddling without teasing."
        "You can tell Wuldon is holding himself back from going further right now - likely because of Vurro - but his body slowly relaxes as the gentle glow of the cave lulls him into drowsiness."
    "It's like laying under the night sky, crystalline rocks sparkling with thousands of colors like the stars far above."
    "There is no moon to provide light, but the slight blue glow of the pond fits the role well, drowning the cave in calm."
    scene black with dissolve
    pause 0.1 
    scene buriedshimmer with dissolve
    scene black with dissolve3

    if wuldon_like > 5:
        "You don't know when you fell asleep. One moment you were looking at the walls, and the next you were woken up by Wuldon affectionately nuzzling your neck."

        pause 5
        w "As much as I hate to say it, we need to get going, little one."
        "So saying, he pulls away from you and gets on his feet."
    else:
        "You don't know when you fell asleep. One moment you were looking at the walls, and the next you were woken up by Wuldon pushing you gently."
        pause 5
        w "Come on, we should get going."
    scene buriedshimmer with dissolve2
    show wuldon normal
    "Still a bit groggy, you get up and stretch a bit to wake up."
    w "Vurro is at the cave entrance, sleeping."
    "You look up at him in the middle of a stretch, feeling a bit ridiculous."
    e "Any reason why?"
    if wuldon_like > 5:
        w "He wanted to give us room or something, apparently."
    w "The snoring was the biggest reason for him, I think."
    "Wuldon checks to see if you're ready to go, and turns towards the exit."
    w "We should get going before his snoring causes another cave-in."
    "Together, you jog over to the water hole."
    "Vurro's unconscious form comes into view far after you hear the snoring."
    "He looks like passed out on his feet, considering the absurd heap he forms."
    "Wuldon, apparently not caring for his condition, grabs Vurro and dunks him into the water headfirst."
    "Vurro comes back out spluttering and indignant. He is put back down on the ground, where he spends a good minute sulking."
    show wuldon normal at l1 with move
    show vurro clothed at r1 with dissolve
    v "I know it's because it's hard to wake me up, but please don't scare me like that."
    "Wuldon shrugs."
    w "No promises."
    "Vurro just keeps on looking at Wuldon."
    w "Okay, okay, I'll move it down the list of ways to wake you up."
    "Vurro looks for a bit longer, until he gives up and accepts it for what it is."
    pause 1
    v "Alright. Well, now that I'm awake, I have a few things to say."
    v "First off, the cave is an incredible find. Not only can we invite other tribes to visit, some of the ore in that area is incredibly rare."
    v "Second, I'm hungry. We need to head back home and eat."
    w "What happened to our supplies?"
    "Vurro scratches the back of his head, embarrassed."
    v "I uhh... ate them."
    v "I got sudden and intense hunger pangs earlier, and next thing I know, I've eaten all of the food."
    "Incredibly concerning, but there's nothing you can really do."
    e "So we're headed back home?"
    v "Yes."
    v "Sorry that I couldn't talk to you about what we mentioned earlier, but I guess when we meet to hunt Uffe is as good a time as any."
    "Doubtful, but it'll have to do."
    e "It's alright. I'm sure you'll tell me someday."
    e "We could alwa-"
    show vurro clothed:
        linear 0.05 xalign 0.925
        linear 0.05 xalign 0.975
        repeat 3
        linear 0.05 xalign 0.95
    pause 2
    "A loud gurgle comes from Vurro's stomach, interrupting your thoughts."
    e "Nevermind. Let's get you some food."
    "The three of you look at the water with slight dismay. There's nothing for it to get in, but the three of you have had enough water for a long time."
    "Moving past the hesitance, the three of you take the first step home together and dive in."
    scene black with dissolve
    "Conversation is sparse on your journey home, thoughts occupied by the events of last night, or plans to take down Uffe."
    "Before you know it, you're back at Wuldon's house."
    scene slumbrous_well with dissolve
    show wuldon normal at l1 with dissolve
    show vurro clothed at r1 with dissolve
    v "Well, I guess we part ways for now."
    v "We'll be grabbing supplies or otherwise preparing to take down Uffe for the next few days. I recommend you do the same."
    v "When we're both ready, come back here to go out and kill the bastard."
    "Vurro walks up to you and throws his arms around you."
    pause 1
    v "Wuldon and I have been friends since we were little. He was the brother I never had."
    "You almost mention Uffe, but stop yourself. It's sad to see a brother disown another, but in this case, it's perfectly justified."
    v "Thank you for helping us, and for giving Wuldon company."
    v "It means more than you know, and I wish I had some way to even start to pay you back."
    v "But I don't. So all I can say is thank you."
    "You hug him back without a word. There is nothing you can say to that."
    "The two of you stay embraced for a long time, Vurro trying to make up for time he'll never have."
    "When it finally ends, Vurro backs off, looking... empty."
    v "I'll see you in a few days."
    "As he says that, he gives you a sad smile, and heads inside."
    show vurro clothed:
        easein 1.5 xalign 3.0
    pause 2
    show wuldon normal:
        easeout 1 xalign 0.5
    if wuldon_like > 5:
        "Wuldon is standing by the door somewhat awkwardly, a bittersweet smile on his mouth."
        "He walks forwards until he's less than a foot away from you."
        "You look up at his face as it looks down at you. Gentle, is how you'd describe him right now."
        w "There is a lot I want to tell you."
        "His face scrunches up in pain."
        w "But I want to wait until after we fight Uffe. Otherwise..."
        "You nod to him carefully, and beckon him down so you can whisper in his ears."
        e "I understand."
        "So saying, you grab both sides of Wuldon's head and gently kiss him on the cheek."
        pause 1
        "When you pull back, Wuldon stays there, looking at you sadly."
        w "You do."
        "The blue werewolf sighs as he stands back up."
        w "Stay safe. For both of us."
        "You give him a sad smile."
        e "I thought you said you'd keep me safe?"
        w "I said I'd try."
        pause 2
        "He pauses momentarily, gathering his thoughts."
        w "I wish I could promise I will."
        "With great difficulty, you give him a reassuring smile."
        e "You do your best. Vurro and I know that."
        "With a heavy heart, Wuldon turns around."
        pause 1
        w "I know. But my best doesn't do much if my best friend is slated to die, and all I can do is watch."
        e "..."
        e "We brought him back for a while, and we're going to get revenge."
        "Wuldon pauses at the doorway. When he finally speaks, his voice is tired, but determined."
        pause 1
        w "Yes. I'm infinitely grateful for what I have, and I'll do my best to treasure it while I can. You've helped me do that, and now you're also helping me finish this whole thing."
        w "We will get revenge, and I will hunt down whover did this and make sure he can't fuck with what's mine anymore."
        w "For that to happen, we both have to live. Sharpen your weapons, stock up on potions... do whatever you can to get ready."
        "Wuldon briefly turns to look at you again."
        w "I look forward to seeing you again when you are."
        "And so, with a true, genuine smile on his face, Wuldon walked into his home, leaving you alone to process everything from the last few minutes."
        "It's time to go home."
    else:
        "Wuldon is standing by the door somewhat awkwardly."
        w "You know how I feel, but... thank you. Stay safe, little one."
        e "I will. Gotta stay strong to fight Uffe, right?"
        w "Yeah. It's going to be an uphill battle."
        "Waving goodbye, Wuldon turns around and walks into his home, leaving you alone."
        "It's time to head home."
    scene black with dissolve
    msg "You received a level up point and 300 gold."
    $ pc.gold += 300
    $ pc.lvluppt += 1
    $ QuestFinish(quest28)
    jump main_slumbrous_well

label Chelforte_Nosferat:
    show screen dungeon_map(chelforte)

    $ disableC = True
    $ enct = None
    "You encounter a nosferat..."
    jump nosferat_battle
label Chelforte_Wuldon:
    scene chelforte_cavern with dissolve
    show wuldon normal with dissolve
    if cavern_help[0] == 0:
        $ cavern_help[0] += 1
        "Wuldon turns around from slamming his pickaxe into the wall."
        "Looking at him like this, you think you can understand why the farmers were scared of him."
        "His muscles bulge underneath his fur, which is matted with the dust and sweat of hard work in a mine. All of this contextualized by the sharp metal pickaxe in his hands, and the hole forming in the solid stone wall."
        if wuldon_like <= 4:
            w "You got any questions for me?"
            e "Where do you think I should explore first?"
            "Wuldon gives you a shrug, putting his pickaxe on the ground, and leaning on it."
            w "I don't know. That's why you're exploring, to figure out if there's anything worthwhile in this part of the cave."
            e "Anything else to keep in mind?"
            w "Try to take out any threats you see along the way. I don't think any will try to kill you, but they'll definitely inconvenience anyone trying to work here."
            e "Alright. I'll be on my way then."
            "Wuldon gives you a nod, hefting his pickaxe on his shoulder."
            w "Good luck."
        else:
            w "You're lucky I waived the viewing fees for you."
            e "..."
            "You hadn't really realized you'd been staring. Wuldon doesn't seem to mind though, as he simply reaches out to ruffle your hair with a smile."
            e "Fair enough. I originally came here because I wanted to ask you something, though."
            w "Hmm?"
            "Wuldon puts down his pickaxe for now, giving you his undivided attention."
            e "Where do you think I should explore first?"
            "The werewolf fidgets slightly, giving the question genuine thought."
            w "I don't know. That's a lot of why we want your help exploring. You always seem to find something interesting."
            e "So, I'm basically your good luck charm."
            "Wuldon nods, slightly sheepishly."
            w "That, and you can fit in the spaces we can't."
            e "No other reason I'm here?"
            w "...you're good at fighting, and clearing out the threats for us would be extremely helpful?"
            "You shake your head, knowing he's dodging the question."
            e "I know you can do all of this yourself with enough time and energy."
            w "That's... true. It's also not like I lack either of those."
            "He glances at Vurro."
            w "Well, normally. Right now we're on a timer with Vurro."
            w "But yes, you're right."
            e "Right about what."
            "The two of you know exactly what you mean, but Wuldon seems embarrassed to say it with Vurro nearby."
            w "That we want you here."
            "You narrow your eyes at Wuldon, who fidgets unhappily."
            w "Yes, he wants you here mostly because I want you here. Are you happy now?"
            e "As a matter of fact, I am."
            w "...you're lucky I like you. Anyone else would have been laid flat by now."
            "Satisfied with what you've gotten, you turn around with a smile."
            e "Good thing you like me then."
            "If he can mess with you, you can mess with him."
            "The last thing you hear out of Wuldon before you start exploring again is a vaguely annoyed grumble."
    else:
        $ cavern_help[0] += 1
        w "Didn't you just come here a second ago?"
        e "...Yeah. But I sort of forgot what I was looking for."
        "Wuldon shakes his head in the bemused confusion of a man watching a dog chase its own tail."
        w "I don't know if I'm hoping that this is caused by a monster hitting you in the head, or not."
        w "Both options have worrying implications."
        "He's being a bastard as always."
        e "If it was the monster hitting me, it must have taken my memories of that too."
        e "Now, please. Remind me of my task?"
        "The werewolf gives a helpless shrug."
        w "You're exploring the nearby area for anything interesting, and clearing out any monsters you see along the way."
        e "Got it."
        e "I'll talk to you later."
        w "Mmh. Hopefully not about the same question."
    jump Chelforte_Cavern_Loop
label Chelforte_Vurro:
    scene chelforte_cavern with dissolve
    if quest28.status == 2:
        show vurro clothed with dissolve
        v "Oh, hey there, [e]. Good to see you survived the few minutes alone with Wuldon."
        "As you dry yourself off, you see Vurro looking around somewhat vacantly."
        e "Did the scouting go alright?"
        v "Mm. Yeah."
        "Vurro feels slightly... off."
        e "You doing alright there?"
        "You get a gentle shake of the head from the brown werewolf."
        v "I'll be fine. It's just weird to be in this cave after everything that's happened."
        v "...I don't like thinking about how many of my people are buried down here."
        "You both stand there in silence for a moment."
        v "You know, even now, I'm scared that I'll turn down here."
        "It's hard to know what to say to that. Luckily, you don't have to. A nearly invisible blue arm camouflaged by the water reaches out, and grabs Vurro's leg."

        "With a tremendous heave, Wuldon bursts out of the water, using his weight to pull Vurro down into the tunnel."
        show vurro clothed:
            easein 1 ypos 2.0
        pause 1.5
        show wuldon normal:
            xalign 0.95 ypos 2.0
            easein 1 ypos 0.0
        pause 1.5

        "Wuldon lands sopping wet, but triumphant. He turns and waits for Vurro to appear."
        "After a few short moments, an annoyed brown werewolf resurfaces, dry fur now returned to its soggy state."
        show vurro clothed at l1 with move
        v "You already threw me in once. Why do it again."
        "Wuldon gives a shrug."
        w "I could see that you were getting depressed again, so I thought I'd help you feel better."
        v "..."
        v "Fine. But you're going to explain what we're doing down here to [e] while I dry off."
        show vurro clothed:
            easein 2 xpos -1.0
        w "Fair's fair."
        show wuldon normal at c1 with move
        "Wuldon turns to you."
        w "Alright, little one. Our goals down here are to make an air vent, clear out some of the rubble disconnecting us from other areas, and find any sites that may interest us."
        w "Vurro and I will mostly handle the first two, though he won't say no to extra help, if you want to give any."
        w "Your job will mainly be exploration. Having seen your performance in slime country, I have no doubt you'll find something interesting."
        w "Here's a pickaxe, you'll need it to get anything important."
        $ addItem("Copper Pickaxe", inventory, 1)
        w "Are we clear?"
        "You give Wuldon a nod."
        w "Perfect. Please stand back."

        "Cautiously, you move as far away from Wuldon as you can. As soon as you cross some sort of invisible line, Wuldon begins to shake himself violently, spraying water everywhere."
        show wuldon normal:
            linear 0.05 xalign 0.45
            linear 0.05 xalign 0.55
            repeat 5
            linear 0.05 xalign 0.5
        pause 2
        w "Good as new."
        "The Werewolf takes this opportunity to put down his pack and take out a pickaxe."
        w "Let's get going."
        scene black with dissolve
        $ wuldon_sprite1 = MapUser(17, 8, "wuldon_sprite1", 130, 200, "Wuldon")
        $ addSprite(chelforte, wuldon_sprite1)
        $ wuldon_sprite2 = MapUser(18, 8, "empty0", 120, 120, "Wuldon")
        $ addSprite(chelforte, wuldon_sprite2)

        $ chelforte.moveTo(vurro_sprite1.x, vurro_sprite1.y, 1, 7)
        $ quest28.qComp(__("Explore the Cave"))
        $ quest28.status = 3
    else:

        show vurro clothed with dissolve

        if cavern_help[1] == 0:
            $ cavern_help[1] += 1
            "The brown werewolf is turning around with a small boulder in his arms when he spots you."
            v "Hello [e]. Anything I can help you with?"
            e "No, I'm doing well enough on my end. I was actually wondering if you wanted any help?"
            "Vurro gives you a small grin as he drops the boulder over in a growing pile to his left."
            v "I think I have things well in hand over here, but if you want to help, be my guest."
            menu:
                "Do you want to help Vurro?"
                "Yes{#helpvurro}":
                    $ cavern_help[2] += 1
                    e "Alright, how should I go about this then?"
                    v "Just pick up rocks from that pile over there, and drag them over to the corner."
                    e "Sounds good. I'll stop when I need to take a break."
                    v "Absolutely. We still need you exploring after all!"

                    jump Vurro_Cave_Help
                "No{#helpvurro}":
                    e "I would, but I need to conserve my energy for exploring."
                    v "That's alright! Thanks for checking in!"
                    "The smiling werewolf turns around and begins hauling rocks once more."
                    "Maybe you shouldn't bother him again unless you want to help."
        else:

            "Vurro is wiping sweat off of his brow when you find him again."
            v "You here to help?"
            menu:
                "Do you want to help Vurro?"
                "Yes{#helpvurro2}":
                    e "I'm a bit bored of exploring, so I think I'll hop on if you don't mind."
                    if pc.hp <= 1:
                        "Vurro looks you up and down, noticing your exhaustion."
                        v "You look like you could use a break, [e]. Wuldon would tear me apart if I made you work more."
                        e "Are you sure? Those rocks look pretty heavy."
                        v "No, I insist, [e]. Go rest a bit or see if Wuldon need any help."
                    else:
                        "All you get is a smile from Vurro, as he begins hauling rocks once more."
                        "Seeing that Vurro understandably does not want to waste time, you join him at once."
                        "The two of you spend your time chatting and teasing, occasionally receiving a pebble to the back of the head by an annoyed Wuldon."
                        scene black with dissolve
                        "With that said, the two of you begin hauling rocks together, sharing small talk and laughing all the while."
                        pause 2
                        jump Vurro_Cave_Help
                "No{#helpvurro2}":
                    e "Sorry, I don't think I can really afford to right now."
                    "A small grin from the werewolf tells you he doesn't mind."
                    v "Alright, but make sure to come here and tell me if anything cool happens, alright?"
                    "He pauses for a moment."
                    v "Or scream if you're in trouble."
            "Deciding his break is over, Vurro begins hauling rocks once more."


    jump Chelforte_Cavern_Loop

label Vurro_Cave_Help:
    scene black with dissolve
    "With that said, the two of you begin hauling rocks together, sharing small talk and laughing all the while."
    pause 2
    "Your time hauling rocks with Vurro has dealt 50 HP damage."
    if cavern_help[2] < 3:
        $ wuldon_like += 1
    $ pc.hp -= 50
    if pc.hp < 1:
        $ pc.hp = 1
    "Despite that, the cave's water has soothed the aching in your muscles slightly as you drink from it. You gained 200 EXP."
    $ pc.exp += 200
    if pc.exp > pc.expCap and pc.level <= levelCap:
        $ pc.LevelUp()
        msg "You are now Level [pc.level]! Check your inventory to allocate your level points."
    "You also pick up a slate rock."
    $ addItem("Slate Rock", inventory, 1)
    jump Chelforte_Cavern_Loop

label Chelforte_Cavern_Ward:
    show screen dungeon_map(chelforte)
    $ disableC = True
    "You look at the pulsating rock in front of you..."
    "It's weird that the rock activated by the flowing water is seen here also..."
    "You shake your head."
    menu:
        "Do you want to fight the stone ward?"
        "Yes{#fightchelfortestoneward}":
            jump stoneward_battle
        "No{#fightchelfortestoneward}":
            pass
    jump Chelforte_Cavern_Loop
label Chelforte_Cavern_Ore1:
    show screen dungeon_map(chelforte)
    $ disableC = True
    if callInventoryItem("Copper Pickaxe", "Weapon"):
        "You stare at the ore vein, there seems to be some minerals inside the wall..."
        "However, you do not have the tool to extract the ore..."
    else:

        $ mined = True
        if mimic_num == 1 and ccore_spritec1.status == 1:
            $ ccore_spritec1.reset()
        elif mimic_num == 2 and ccore_spritec2.status == 1:
            $ ccore_spritec2.reset()
        elif mimic_num == 3 and ccore_spritec3.status == 1:
            $ ccore_spritec3.reset()
        elif mimic_num == 4 and ccore_spritec4.status == 1:
            $ ccore_spritec4.reset()
        elif mimic_num == 5 and ccore_spritec5.status == 1:
            $ ccore_spritec5.reset()
        elif mimic_num == 6 and ccore_spritec6.status == 1:
            $ ccore_spritec6.reset()
        elif mimic_num == 7 and ccore_spritec7.status == 1:
            $ ccore_spritec7.reset()
        elif mimic_num == 8 and ccore_spritec8.status == 1:
            $ ccore_spritec8.reset()
        elif mimic_num == 9 and ccore_spritec9.status == 1:
            $ ccore_spritec9.reset()
        else:
            $ mined = False
        if mined:
            $ addItem("Iron Ingot", inventory, 1)
            "You take out your pickaxe and start striking it against the ore."
            "After a few long and grueling moments, you finally obtain an iron ore."
        else:
            "There's nothing for you to mine for now... Maybe the ore will replenish... eventually."

    jump Chelforte_Cavern_Loop
label Chelforte_Cavern_Ore2:
    show screen dungeon_map(chelforte)
    $ disableC = True
    if callInventoryItem("Copper Pickaxe", "Weapon"):
        "You stare at the ore vein, there seems to be some minerals inside the wall..."
        "However, you do not have the tool to extract the ore..."
    else:
        $ mined = True

        if mimic_num == 1 and ccore_spritec11.status == 1:

            $ ccore_spritec11.reset()
        elif mimic_num == 2 and ccore_spritec12.status == 1:

            $ ccore_spritec12.reset()
        elif mimic_num == 3 and ccore_spritec13.status == 1:

            $ ccore_spritec13.reset()
        elif mimic_num == 4 and ccore_spritec14.status == 1:

            $ ccore_spritec14.reset()
        elif mimic_num == 5 and ccore_spritec15.status == 1:

            $ ccore_spritec15.reset()
        elif mimic_num == 6 and ccore_spritec16.status == 1:

            $ ccore_spritec16.reset()
        elif mimic_num == 7 and ccore_spritec17.status == 1:

            $ ccore_spritec17.reset()
        else:
            $ mined = False
        if mined:
            $ addItem("Lodestone", inventory, 1)
            "You take out your pickaxe and start striking it against the ore."
            "After a few long and grueling moments, you finally obtain a lodestone ore."
        else:
            "There's nothing for you to mine for now... Maybe the ore will replenish... eventually."

    jump Chelforte_Cavern_Loop
label Chelforte_Cavern_Ore3:
    show screen dungeon_map(chelforte)
    $ disableC = True
    if callInventoryItem("Copper Pickaxe", "Weapon"):
        "You stare at the ore vein, there seems to be some minerals inside the wall..."
        "However, you do not have the tool to extract the ore..."
    else:
        $ mined = True

        if mimic_num == 1 and ccore_spritec21.status == 1:
            $ ccore_spritec21.reset()
        elif mimic_num == 2 and ccore_spritec22.status == 1:
            $ ccore_spritec22.reset()
        elif mimic_num == 3 and ccore_spritec23.status == 1:
            $ ccore_spritec23.reset()
        elif mimic_num == 4 and ccore_spritec24.status == 1:
            $ ccore_spritec24.reset()
        elif mimic_num == 5 and ccore_spritec25.status == 1:
            $ ccore_spritec25.reset()
        else:
            $ mined = False
        if mined:
            $ addItem("Copper", inventory, 1)
            "You take out your pickaxe and start striking it against the ore."
            "After a few long and grueling moments, you finally obtain a copper ore."
        else:
            "There's nothing for you to mine for now... Maybe the ore will replenish... eventually."

    jump Chelforte_Cavern_Loop
label Leaving_Chelforte:
    $ removeSprite(chelforte, tenki_sprite4)
    $ removeSprite(chelforte, cferal_sprite1)

    hide screen dungeon_map
    hide screen dungeon_buttons
    return
label Leaving_Cavern_Ent:
    $ removeSprite(cavern_ent, tenki_sprite4)
    hide screen dungeon_map
    hide screen dungeon_buttons

    return

default d6x = 1
default d6y = 1
label Cavern_Entrance_Enter:
    $ dungeon_timers = []
    $ d6x = 1
    $ d6y = 1
    $ dungeon6_map = [
    [MapTile(MapThing("tree4")), MapTile(), MapTile(MapThing("tree8")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree3"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree5")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("tree5"))],
    [MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree7")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("tree8")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1"))],
    [MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree7")), MapTile(), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(), MapTile(MapThing("tree2"))],
    [MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("fcave2"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(MapThing("fcave3"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("fcave2")), MapTile(MapThing("fcave1"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("fcave3")), MapTile(MapThing("fcave1"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("fcave2")), MapTile(MapThing("fcave1")), MapTile(MapThing("fcave1"))],
    [MapTile(MapThing("tree5")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("fcave3")), MapTile(MapThing("fcave1")), MapTile(MapThing("fcave1"))],
    [MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree7")), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("fcave2")), MapTile(MapThing("fcavehole")), MapTile(MapThing("fcavehole4")), MapTile(MapThing("fcave1"))],
    [MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("fcave3")), MapTile(MapThing("fcavehole2")), MapTile(MapThing("fcavehole3")), MapTile(MapThing("fcave1"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("tree5"))],
    [MapTile(MapThing("tree5")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("tree5"))],
    [MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1"))],
    [MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2"))]
    ]
    $ cavern_ent = MapPat(dungeon6_map, "Cavern Entrance", d6x, d6y, "grass2")

    $ fsign_sprite2 = MapUser(7, 10, "fsign_sprite", 120, 120, "Sign")
    $ fleave_sprite2 = MapUser(1, 0, "cliff2", 120, 120, "Leave")
    $ fwood_sprite1 = MapUser(8, 12, "fwood", 120, 180, "Wood")
    $ fwood_sprite2 = MapUser(6, 12, "fwood", 120, 180, "Wood")
    $ treem_sprite = MapUser(11, 4, "treem", 120, 120, "Treem")
    $ tenki_sprite6 = MapUser(d6x, d6y, "e_dungeon", 120, 200, no_op)
    $ current_location = cavern_ent
    $ addBack(cavern_ent, fwood_sprite1)
    $ addBack(cavern_ent, fwood_sprite2)
    $ addSprite(cavern_ent, fsign_sprite2)
    $ addSprite(cavern_ent, fleave_sprite2)
    $ addSprite(cavern_ent, tenki_sprite6)
    $ addSprite(cavern_ent, treem_sprite)

    jump Cavern_Entrance_Loop
label Cavern_Entrance_Loop:
    show screen dungeon_buttons
    $ disableC = False
    $ sprite = tenki_sprite6
    call screen dungeon_map(cavern_ent)
    if _return == "Sign":
        show screen dungeon_map(cavern_ent)
        $ disableC = True
        "You look at the sign... it says Chelforte Cavern. With a drawing of a huge werewolf and rocks from the cave..."
        "It seems to signal danger ahead."
        "Shaking your head, you enter the cavern with caution..."
        $ chelforte_cavern.discovered = True
        scene black with dissolve
        call Leaving_Cavern_Ent from _call_Leaving_Cavern_Ent
        jump Chelforte_Cavern_Enter
    if _return == "Treem":
        show screen dungeon_map(cavern_ent)
        $ disableC = True
        "You notice a small creature right inside the bush... it seem to be craving for a plant inside your backpack..."
        if quest24.status != True:
            "However... it seems you don't know how to lure it out... maybe you need to learn from a certain person..."
        else:
            menu:
                "What do you wish to use...?"
                "Hemp" if LookForItem("Hemp", inventory):
                    $ removeItem("Hemp", inventory, 1)
                    "You give it a piece..."
                    "It seems it doesn't appreciate the gift, it snatches the piece right out of your hand."
                    "..."
                    "You lost a piece of Hemp, and the creature is still inside."
                "Ginger" if LookForItem("Ginger", inventory):
                    $ removeItem("Ginger", inventory, 1)
                    "You give it a piece..."
                    "It seems it doesn't appreciate the gift, it snatches the piece right out of your hand."
                    "..."
                    "You lost a piece of Ginger, and the creature is still inside."
                "Reed" if LookForItem("Reed", inventory):
                    $ removeItem("Reed", inventory, 1)
                    "You give it a piece..."
                    "It seems it doesn't appreciate the gift, it snatches the piece right out of your hand."
                    "..."
                    "You lost a piece of Reed, and the creature is still inside."
                "Rosemary" if LookForItem("Rosemary", inventory):
                    $ removeItem("Rosemary", inventory, 1)
                    "You give it a piece..."
                    "It seems it doesn't appreciate the gift, it snatches the piece right out of your hand."
                    "..."
                    "You lost a piece of Rosemary, and the creature is still inside."
                "Carrot" if LookForItem("Carrot", inventory):
                    if renpy.random.randint(3,6) <= pc.cha:
                        $ removeItem("Carrot", inventory, 1)
                        "You give it a piece..."
                        if lindbloom_item not in tinventory and lindbloom_item not in pc.trinket:
                            "It takes the carrot quickly back into the bush.... and returned with a weird flower..."
                            "You can instantly feel the effect of the flower when it touches your fur, you carefully store it in your bag."
                            $ addTrinket(lindbloom_item, tinventory)
                            "You thank the little creature, it blinks at you and retreats back into the bush."
                        else:
                            "It takes the carrot quickly back into the bush.... and returned with a weird flower..."
                            "When you look closely, you realise it's just a chrysanthemum."
                            $ addItem("Chrysanthemum", inventory, 1)
                            "You thank the little creature, it blinks at you and retreats back into the bush."
                    else:
                        $ removeItem("Carrot", inventory, 1)
                        "You give it a piece..."
                        "It takes the carrot quickly back into the bush.... but it doesn't return you anything..."
                        "..."
                        "Maybe.... you need a higher {color=#d1e431}Charisma{/color} for the little creature, or try again."
                "Barley" if LookForItem("Barley", inventory):
                    $ removeItem("Barley", inventory, 1)
                    "You give it a piece..."
                    "It seems it doesn't appreciate the gift, it snatches the piece right out of your hand."
                    "..."
                    "You lost a piece of Barley, and the creature is still inside."
                "Chrysanthemum" if LookForItem("Chrysanthemum", inventory):
                    $ removeItem("Chrysanthemum", inventory, 1)
                    "You give it a piece..."
                    "It seems it doesn't appreciate the gift, it snatches the piece right out of your hand."
                    "..."
                    "You lost a piece of Chrysanthemum, and the creature is still inside."
                "Herb of Grace" if LookForItem("Herb of Grace", inventory):
                    $ removeItem("Herb of Grace", inventory, 1)
                    "You give it a piece..."
                    "It seems it doesn't appreciate the gift, it snatches the piece right out of your hand."
                    "..."
                    "You lost a piece of Herb of Grace, and the creature is still inside."
    if _return == "Leave":
        show screen dungeon_map(cavern_ent)
        $ disableC = True
        menu:
            msg "Do you want to leave the area, states of the dungeon will not be saved."
            "Yes{#leavecavernentrance}":
                scene black with dissolve
                call Leaving_Cavern_Ent from _call_Leaving_Cavern_Ent_1
                jump Dark_Forest_Map
            "No{#leavecavernentrance}":
                pass
    jump Cavern_Entrance_Loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
