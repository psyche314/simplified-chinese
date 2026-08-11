default d3x = 1
default d3y = 7
default tenki_sprite3 = MapUser(d3x, d3y, "e_dungeon", 120, 200, no_op)
default inDarkForest = 0
image bonfire_sprite:
    "bonfire1"
    pause 1
    "bonfire2"
    pause 1
    repeat
default werewolf_d1 = "left"
default werewolf_d2 = "right"
default dungeon3_map = [
[MapTile(MapThing("tree3")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree3"))],
[MapTile(MapThing("tree4")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("bush5"))],
[MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(MapThing("bush6"))],
[MapTile(MapThing("tree4")), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile()],
[MapTile(MapThing("tree4")), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
[MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cliff1")), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
[MapTile(MapThing("bush6")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
[MapTile(), MapTile(), MapTile(), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
[MapTile(MapThing("tree4")), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
[MapTile(MapThing("tree4")), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cliff1")), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
[MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cliff1")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("tree4"))],
[MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("tree4"))],
[MapTile(MapThing("tree4")), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
[MapTile(MapThing("tree4")), MapTile(), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("tree4"))],
[MapTile(MapThing("tree5")), MapTile(), MapTile(), MapTile(MapThing("cliff1")), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("tree5"))],
[MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1"))],
[MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2"))]
]

image werewolf_sprite_0 = "werewolf [werewolf_d1]"
image werewolf_sprite_1 = "werewolf [werewolf_d2]"
image werewolf_sprite_2 = "werewolf [werewolf_d1]"
image werewolf_sprite_3 = "werewolf [werewolf_d2]"
image werewolf left:
    "werewolf_sprite3"
    pause 0.25
    "werewolf_sprite1"
image werewolf right:
    "werewolf_sprite4"
    pause 0.25
    "werewolf_sprite2"
image werewolf 2:
    "werewolf left"
image werewolf 1:
    "werewolf right"

label Forest_Nightwatch_Enter:
    $ dungeon_timers = []
    $ d3x = 1
    $ d3y = 7
    $ step = 0
    hide screen menu_buttons
    show screen dungeon_buttons
    $ dungeon3_map = [
    [MapTile(MapThing("tree3")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree3"))],
    [MapTile(MapThing("tree4")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("bush5"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(MapThing("bush6"))],
    [MapTile(MapThing("tree4")), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile()],
    [MapTile(MapThing("tree4")), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cliff1")), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("bush6")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(), MapTile(), MapTile(), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cliff1")), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(MapThing("cliff1")), MapTile(), MapTile(MapThing("cliff1")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree5")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("tree5"))],
    [MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1"))],
    [MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2"))]
    ]

    $ werewolfD[0] = 0
    $ werewolfD[1] = 0
    $ werewolfD[2] = 0
    $ werewolfD[3] = 0
    $ dark_forest1 = MapPat(dungeon3_map, "Forest Nightwatch", d3x, d3y, "grass2")
    $ tenki_sprite3 = MapUser(d3x, d3y, "e_dungeon", 120, 200, no_op)
    if dungeon3_enter == 0:
        $ chest_sprite = MapUser(4, 7, "chest_sprite", 120, 120, "Chest")
    $ bonfire_sprite = MapUser(6, 7, "bonfire_sprite", 120, 132, "Bonfire")
    $ werewolf_sprite = MapUser(8, 10, "werewolf_sprite_0", 140, 204, "Werewolf1")
    $ werewolf_sprite1 = MapUser(9, 14, "werewolf_sprite_1", 140, 204, "Werewolf2")
    $ werewolf_sprite2 = MapUser(2, 5, "werewolf_sprite_2", 140, 204, "Werewolf3")
    $ werewolf_sprite3 = MapUser(10, 3, "werewolf_sprite_3", 140, 204, "Werewolf4")
    $ barrel_sprite1 = MapUser(2, 12, "barrel_sprite", 120, 120, "Barrel")
    $ barrel_sprite2 = MapUser(2, 13, "barrel_sprite", 120, 120, "Barrel")
    $ barrel_sprite3 = MapUser(3, 13, "barrel_sprite", 120, 120, "Barrel")
    $ barrel_sprite4 = MapUser(3, 14, "barrel_sprite", 120, 120, "Barrel")
    $ crosssign_sprite1 = MapUser(1, 13, "crosssign_sprite", 120, 120, "Crosssign")
    $ crosssign_sprite2 = MapUser(1, 14, "crosssign_sprite", 120, 120, "Crosssign")
    $ crosssign_sprite3 = MapUser(2, 14, "crosssign_sprite", 120, 120, "Crosssign")
    $ crosssign_sprite4 = MapUser(3, 14, "crosssign_sprite", 120, 120, "Crosssign")
    $ wooddoor_sprite1 = MapUser(5, 12, "wooddoor_sprite", 120, 165, "Door")
    $ wooddoor_sprite2 = MapUser(5, 12, "wooddoor_sprite2", 120, 165, "Door2")
    $ wooddoor_sprite3 = MapUser(5, 13, "wooddoor_sprite3", 120, 45, "Door2")
    $ flower_sprite1 = MapUser(9, 6, "flower_sprite", 120, 120, "Flower")
    $ flower_sprite2 = MapUser(10, 6, "flower_sprite", 120, 120, "Flower")
    $ flower_sprite3 = MapUser(11, 6, "flower_sprite", 120, 120, "Flower")
    $ mimic_sprite = MapUser(1, 2, "mimic_sprite", 120, 120, "Mimic")
    $ pebble_sprite1 = MapUser(6, 9, "pebble_sprite1", 120, 120, "Pebble")
    $ pebble_sprite2 = MapUser(5, 3, "pebble_sprite1", 120, 120, "Pebble")
    $ sleepingmat_sprite = MapUser(4, 9, "sleepingmat_sprite", 120, 210, "Mat")
    $ wolfsleeping_sprite = MapUser(4, 9, "wolfsleeping_sprite", 120, 210, "WolfSleep")
    $ leavegrass_sprite = MapUser(0, 7, "grass3", 120, 120, "Leave")
    $ leavegrass_sprite2 = MapUser(15, 3, "grass3", 120, 120, "Leave2")
    $ cornershade_sprite1 = MapUser(2, 7, "cornershade_sprite2", 120, 120, "S")
    $ cornershade_sprite2 = MapUser(3, 11, "cornershade_sprite2", 120, 120, "S")
    $ cornershade_sprite3 = MapUser(7, 10, "cornershade_sprite", 120, 120, "S")
    $ cornershade_sprite4 = MapUser(11, 10, "cornershade_sprite2", 120, 120, "S")
    $ cornershade_sprite5 = MapUser(5, 5, "cornershade_sprite2", 120, 120, "S")
    $ cornershade_sprite8 = MapUser(3, 10, "cornershade_sprite2", 120, 120, "S")
    $ cliff_sprite2 = MapUser(7, 5, "cliff2", 120, 120, "C")
    $ cliff_sprite3 = MapUser(9, 9, "cliff2", 120, 120, "C")
    $ addSprite(dark_forest1, werewolf_sprite)
    $ addSprite(dark_forest1, bonfire_sprite)
    $ addSprite(dark_forest1, werewolf_sprite1)
    $ addSprite(dark_forest1, werewolf_sprite2)
    $ addSprite(dark_forest1, werewolf_sprite3)
    $ addSprite(dark_forest1, barrel_sprite1)
    $ addSprite(dark_forest1, barrel_sprite2)
    $ addSprite(dark_forest1, barrel_sprite3)
    $ addSprite(dark_forest1, barrel_sprite4)
    $ addBack(dark_forest1, crosssign_sprite1)
    $ addBack(dark_forest1, crosssign_sprite2)
    $ addBack(dark_forest1, crosssign_sprite3)
    $ addBack(dark_forest1, crosssign_sprite4)
    $ addBack(dark_forest1, pebble_sprite1)
    $ addBack(dark_forest1, pebble_sprite2)
    $ addSprite(dark_forest1, wooddoor_sprite1)
    $ addSprite(dark_forest1, flower_sprite1)
    $ addSprite(dark_forest1, flower_sprite2)
    $ addSprite(dark_forest1, flower_sprite3)
    $ addSprite(dark_forest1, chest_sprite)
    $ addSprite(dark_forest1, mimic_sprite)
    $ addBack(dark_forest1, sleepingmat_sprite)
    $ addSprite(dark_forest1, wolfsleeping_sprite)
    $ addSprite(dark_forest1, leavegrass_sprite)
    $ addSprite(dark_forest1, leavegrass_sprite2)
    $ addBack(dark_forest1, cornershade_sprite1)
    $ addBack(dark_forest1, cornershade_sprite2)
    $ addBack(dark_forest1, cornershade_sprite3)
    $ addBack(dark_forest1, cornershade_sprite4)
    $ addBack(dark_forest1, cornershade_sprite5)
    $ addBack(dark_forest1, cornershade_sprite8)
    $ addBack(dark_forest1, cliff_sprite2)
    $ addBack(dark_forest1, cliff_sprite3)


    $ addSprite(dark_forest1, tenki_sprite3)
    $ current_location = dark_forest1
    jump Dark_Forest1_Loop
label Dark_Forest1_Loop:
    show screen dungeon_buttons
    $ disableC = False
    $ sprite = tenki_sprite3
    show screen dungeon_buttons
    call screen dungeon_map(dark_forest1)
    if _return == "Bonfire":
        show screen dungeon_map(dark_forest1)
        $ disableC = True
        "The fire is still burning bright. Meat and random beer scattered around the area."
        "Seems like you're stepping into the werewolves' turf."
    if _return == "Chest":
        show screen dungeon_map(dark_forest1)
        $ disableC = True
        "You notice a chest near the campsite, it seems to belong to the werewolves."
        if dark_forest1.mappy[9][4].user != None and dark_forest1.mappy[9][4].user.img == "wolfsleeping_sprite":
            "But you hear a werewolf... snoring near the chest..."
            ww "Haaa... ARFFF... I- Bones...!"
            "It seems dangerous to get the chest content without waking the werewolf up."
            "Unless you're stealthy enough... or you have a decent amount of {color=#d1e431}Agility{/color}."
            "Plus, you're so close to the werewolf... you might be in danger if you get caught..."
            menu:
                "Do you open the chest?"
                "Yes{#opennightwatchchest}":
                    $ agicheckkk = renpy.random.randint(1,2) + renpy.random.randint(0,2) + renpy.random.randint(0,1)
                    if pc.agi > agicheckkk:
                        "You successfully opened the chest without the werewolf's notice."
                        $ addItem("Hunter Hat", inventory, 1)
                        $ addItem("Green Ointment", inventory, 1)
                        $ pc.gold += 50
                        "You found a Green Ointment, a Hunter Hat and 50 gold."
                        $ dark_forest1.unoccupy(4, 7)
                        $ dungeon3_enter += 1
                    else:
                        "As you are trying to open the chest, the werewolf on your side becomes startled by your movement."
                        jump Dark_Forest1_Sleeping_Wolf
                "No{#opennightwatchchest}":

                    pass
    if _return == "WolfSleep":
        show screen dungeon_map(dark_forest1)
        $ disableC = True
        if sleeping_wolf == 0:
            "You poke the sleeping werewolf on his snout, he instantly jumps like getting electrocuted."
            jump Dark_Forest1_Sleeping_Wolf
        else:
            ww "Uhm... bones... meat... prey... ahhh... so good. mhmmm..."
            ww "I want them all... aAWWOOOO...."
            "For a sleeptalker, this werewolf surely sleeps a lot... and talks a lot."

    if _return == "Leave":
        show screen dungeon_map(dark_forest1)
        $ disableC = True
        menu:
            "Do you want to return to the entrance of the dark forest?"
            "Yes{#leavenightwatch}":
                "You follow the path back to the entrance."
                $ dark_forest1.unoccupy(tenki_sprite3.x, tenki_sprite3.y)
                $ dark_forest1.unoccupy(werewolf_sprite.x, werewolf_sprite.y)
                $ dark_forest1.unoccupy(werewolf_sprite2.x, werewolf_sprite2.y)
                $ dark_forest1.unoccupy(werewolf_sprite1.x, werewolf_sprite1.y)
                $ dark_forest1.unoccupy(werewolf_sprite3.x, werewolf_sprite3.y)
                $ dark_forest1.unoccupy(barrel_sprite1.x, barrel_sprite1.y)
                $ dark_forest1.unoccupy(barrel_sprite2.x, barrel_sprite2.y)
                $ dark_forest1.unoccupyback(wooddoor_sprite2.x, wooddoor_sprite2.y)
                hide screen dungeon_map
                hide screen dungeon_buttons

                jump Dark_Forest_Map
            "No{#leavenightwatch}":

                pass
    if _return == "Leave2":
        show screen dungeon_map(dark_forest1)
        $ disableC = True
        if moonlit_wolf_den.discovered == False:
            $ moonlit_wolf_den.discovered = True
            scene black with dissolve
            "You leave the forest through the dirt path."
            "After a few minutes of walking, you discover a cave shaped as wolf in front of you."
            "It must be the werewolf den..."
            $ dark_forest1.unoccupy(tenki_sprite3.x, tenki_sprite3.y)
            $ dark_forest1.unoccupy(werewolf_sprite.x, werewolf_sprite.y)
            $ dark_forest1.unoccupy(werewolf_sprite2.x, werewolf_sprite2.y)
            $ dark_forest1.unoccupy(werewolf_sprite1.x, werewolf_sprite1.y)
            $ dark_forest1.unoccupy(werewolf_sprite3.x, werewolf_sprite3.y)
            $ dark_forest1.unoccupy(barrel_sprite1.x, barrel_sprite1.y)
            $ dark_forest1.unoccupy(barrel_sprite2.x, barrel_sprite2.y)
            $ dark_forest1.unoccupyback(wooddoor_sprite2.x, wooddoor_sprite2.y)
            hide screen dungeon_map
            hide screen dungeon_buttons

            jump moonlit_wolf_den_enter
        else:
            pass

        $ dark_forest1.unoccupy(tenki_sprite3.x, tenki_sprite3.y)
        $ dark_forest1.unoccupy(werewolf_sprite.x, werewolf_sprite.y)
        $ dark_forest1.unoccupy(werewolf_sprite2.x, werewolf_sprite2.y)
        $ dark_forest1.unoccupy(werewolf_sprite1.x, werewolf_sprite1.y)
        $ dark_forest1.unoccupy(werewolf_sprite3.x, werewolf_sprite3.y)
        $ dark_forest1.unoccupy(barrel_sprite1.x, barrel_sprite1.y)
        $ dark_forest1.unoccupy(barrel_sprite2.x, barrel_sprite2.y)
        $ dark_forest1.unoccupyback(wooddoor_sprite2.x, wooddoor_sprite2.y)
        hide screen dungeon_map
        hide screen dungeon_buttons

        jump Dark_Forest_Map

    if _return == "Door":
        show screen dungeon_map(dark_forest1)
        $ disableC = True
        "You reach to the wooden door. It seems to be sealed from the other side."
        "There's a symbol of wolf carved on the door, with the sign saying... 'no- enter. wolf inside'"
        "There must be some way for you to unlock the door."

        if dark_forest1.mappy[13][1].user != None and dark_forest1.mappy[14][1].user != None and dark_forest1.mappy[14][2].user != None and dark_forest1.mappy[14][3].user != None and dark_forest1.mappy[13][1].user.img == "barrel_sprite" and dark_forest1.mappy[14][2].user.img == "barrel_sprite" and dark_forest1.mappy[14][1].user.img == "barrel_sprite" and dark_forest1.mappy[14][3].user.img == "barrel_sprite":
            "CLICK. You hear a crisp noise before the door is suddenly unlocked."
            $ dark_forest1.unoccupy(5, 12)
            $ addBack(dark_forest1, wooddoor_sprite2)
        else:
            menu:
                "Do you want to reset?"
                "Yes{#resetnightwatchpuzzle}":
                    $ dark_forest1.unoccupy(werewolf_sprite.x, werewolf_sprite.y)
                    $ dark_forest1.unoccupy(werewolf_sprite2.x, werewolf_sprite2.y)
                    $ dark_forest1.unoccupy(werewolf_sprite1.x, werewolf_sprite1.y)
                    $ dark_forest1.unoccupy(werewolf_sprite3.x, werewolf_sprite3.y)
                    $ dark_forest1.unoccupyback(wooddoor_sprite2.x, wooddoor_sprite2.y)
                    $ dark_forest1.unoccupy(barrel_sprite1.x, barrel_sprite1.y)
                    $ dark_forest1.unoccupy(barrel_sprite2.x, barrel_sprite2.y)
                    $ dark_forest1.unoccupy(barrel_sprite3.x, barrel_sprite3.y)
                    $ dark_forest1.unoccupy(barrel_sprite4.x, barrel_sprite4.y)
                    $ dark_forest1.unoccupy(sprite.x, sprite.y)

                    jump Forest_Nightwatch_Enter
                "No{#resetnightwatchpuzzle}":
                    pass
    if _return == "Werewolf1":
        $ mimic_num = 1
        jump Dark_Forest1_Werewolf
    if _return == "Werewolf2":
        $ mimic_num = 2
        jump Dark_Forest1_Werewolf
    if _return == "Werewolf3":
        $ mimic_num = 3
        jump Dark_Forest1_Werewolf
    if _return == "Werewolf4":
        $ mimic_num = 4
        jump Dark_Forest1_Werewolf
    if _return == "Mimic":
        $ mimic_num = 5
        jump Dark_Forest1_Mimic
    jump Dark_Forest1_Loop
label Dark_Forest1_Sleeping_Wolf:
    ww "Uhm... W-what?"
    "The werewolf looks at you in confusion, still trying to figure out if this is his dream or not."
    menu:
        "W-what do you say?"
        "You're still dreaming, mister werewolf":
            ww "W-what? I'm obviously awake... Do you think I'm that dumb..."
        "Uhh... I'm just passing by":
            ww "uhmm... a breakfast just in time...."
    ww "Come here... little prey."
    $ mimic_num = 6
    hide screen dungeon_map
    jump werewolf_battle
label Dark_Forest1_Werewolf:
    show screen dungeon_map(dark_forest1)
    $ disableC = True
    $ enct = None
    "As you walk through the forest, you encountered a werewolf."
    "Immediately, you begin to run towards the opposite direction, but soon a dark figure comes into your view."
    e "Fuck..."
    hide screen dungeon_map
    jump werewolf_battle
label Dark_Forest1_Mimic:
    $ disableC = True
    show screen dungeon_map(dark_forest1)
    "You run into a chest in the forest, you walk towards it, trying to open the chest."
    "Suddenly the chest jumps right into your face, it's not a chest, it is a mimic."
    "Mimic" "RAWAWWWR-"
    "You scream, its tongue is slithering out, trying to latch on you..."
    hide screen dungeon_map
    jump mimic_battle

image uffe_sprite0:
    "uffe_sprite1"
    pause 1.8
    "uffe_sprite2"
    pause 0.5
    repeat

image wolfsleeping_sprite0:
    "wolfsleeping_sprite"
    size (140, 210)

image sleepingmat_sprite0:
    "sleepingmat_sprite"
    size (140, 210)

image werewolf left0:
    "werewolf left"
    size (180, 205)

image werewolf right0:
    "werewolf right"
    size (180, 205)

image lwerewolf_sprite00:
    "lwerewolf_sprite0"
    size (240, 240)

label Moonlit_Wolf_Den_Enter:
    $ dungeon_timers = []
    $ d12x = 5
    $ d12y = 10
    $ step = 0
    hide screen menu_buttons
    show screen dungeon_buttons
    $ dungeon12_map = [[MapTile(MapThing("moonlittop2")), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop2")), MapTile(MapThing("moonlittop2")), MapTile(MapThing("moonlittop2")), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop2")), MapTile(MapThing("moonlittop2")), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop2")), MapTile(MapThing("moonlitwall")), MapTile(), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlittop2"))], 
    [MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlittop2")), MapTile(MapThing("moonlittop2")), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlittop2")), MapTile(MapThing("moonlittop2")), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlittop")),  MapTile(),  MapTile(),  MapTile(), MapTile(MapThing("moonlittop2"))],
    [MapTile(MapThing("moonlitwall")), MapTile(), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop2")), MapTile(MapThing("moonlitwall")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop")), MapTile(), MapTile(), MapTile(MapThing("moonlitwall")),  MapTile(),  MapTile(),  MapTile(), MapTile(MapThing("moonlittop2"))],
    [MapTile(), MapTile(), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlittop2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlitwall")), MapTile(), MapTile(), MapTile(),  MapTile(),  MapTile(),  MapTile(), MapTile(MapThing("moonlittop2"))],
    [MapTile(MapThing("moonlittop2")), MapTile(), MapTile(), MapTile(MapThing("moonlittop2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("moonlittop2")),  MapTile(),  MapTile(),  MapTile(), MapTile(MapThing("moonlittop2"))],
    [MapTile(MapThing("moonlittop2")), MapTile(), MapTile(), MapTile(MapThing("moonlittop")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("moonlittop2")),  MapTile(),  MapTile(),  MapTile(), MapTile(MapThing("moonlittop2"))],
    [MapTile(MapThing("moonlittop2")), MapTile(), MapTile(), MapTile(MapThing("moonlitwall")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlitwall")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("moonlittop")),  MapTile(MapThing("moonlittop")),  MapTile(MapThing("moonlittop")),  MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop"))],
    [MapTile(MapThing("moonlittop2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("moonlittop2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("moonlitwall")),  MapTile(MapThing("moonlitwall")),  MapTile(MapThing("moonlitwall")),  MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlitwall"))],
    [MapTile(MapThing("moonlittop2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("moonlittop2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("moonlittop2")), MapTile(), MapTile()],
    [MapTile(MapThing("moonlittop2")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("moonlittop2")), MapTile(), MapTile(MapThing("moonlittop2")), MapTile(MapThing("moonlittop2")), MapTile(MapThing("moonlittop2")), MapTile(MapThing("moonlittop2")), MapTile(), MapTile(), MapTile(MapThing("moonlittop2")), MapTile(MapThing("moonlittop2")), MapTile(MapThing("moonlittop2"))],
    [MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop")), MapTile(), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop")), MapTile(MapThing("moonlittop"))],
    [MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlitwall")), MapTile(), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlitwall")), MapTile(MapThing("moonlitwall"))]
    ]

    $ moonlit_dungeon = MapPat(dungeon12_map, "Moonlit Wolf Den", d12x, d12y, "moonlitfloor")
    $ tenki_sprite12 = MapUser(d12x, d12y, "e_dungeon", 120, 200, no_op)

    $ moonlitcorner_sprite1 = MapUser(1, 2, "moonlitcorner", 120, 120, "Corner")
    $ moonlitcorner_sprite2 = MapUser(5, 2, "moonlitcorner", 120, 120, "Corner")
    $ moonlitcorner_sprite3 = MapUser(6, 2, "moonlitcorner", 120, 120, "Corner")
    $ moonlitcorner_sprite4 = MapUser(7, 2, "moonlitcorner", 120, 120, "Corner")
    $ moonlitcorner_sprite5 = MapUser(8, 2, "moonlitcorner", 120, 120, "Corner")
    $ moonlitcorner_sprite6 = MapUser(9, 2, "moonlitcorner", 120, 120, "Corner")
    $ moonlitcorner_sprite7 = MapUser(12, 2, "moonlitcorner", 120, 120, "Corner")
    $ moonlitcorner_sprite8 = MapUser(13, 2, "moonlitcorner", 120, 120, "Corner")
    $ moonlitcorner_sprite9 = MapUser(15, 1, "moonlitcorner", 120, 120, "Corner")
    $ moonlitcorner_sprite10 = MapUser(17, 1, "moonlitcorner", 120, 120, "Corner")
    $ moonlitcorner_sprite11 = MapUser(2, 4, "moonlitcorner", 120, 120, "Corner")
    $ moonlitcorner_sprite12 = MapUser(4, 3, "moonlitcorner", 120, 120, "Corner")

    $ moonlitexit_sprite1 = MapUser(5, 11, "moonlitcorner", 120, 120, "Exit")

    $ uffe_sprite = MapUser(5, 3, "uffe_sprite0", 120, 180, "Uffe")
    $ uffe_sprite1 = MapUser(6, 3, "empty", 120, 180, "Uffe")
    $ tart_sprite = MapUser(8, 3, "tart_sprite1", 120, 180, "Tart")
    $ tart_sprite1 = MapUser(9, 3, "empty", 120, 180, "Tart")
    $ moonstone_sprite1 = MapUser(3, 8, "moonstone_sprite", 120, 120, "Moonstone")
    $ moonstone_sprite2 = MapUser(11, 7, "moonstone_sprite", 120, 120, "Moonstone")
    $ moonstone_sprite3 = MapUser(8, 7, "moonstone_sprite", 120, 120, "Moonstone")
    $ moonpebble_sprite1 = MapUser(2, 4, "moonpebble_sprite", 120, 120, "Moonpebble")
    $ moonpebble_sprite2 = MapUser(16, 5, "moonpebble_sprite", 120, 120, "Moonpebble")
    $ moonpebble_sprite3 = MapUser(4, 3, "moonpebble_sprite", 120, 120, "Moonpebble")
    $ meat_sprite1 = MapUser(5, 2, "meat_sprite", 120, 120, "Meat")
    $ meat_sprite2 = MapUser(13, 5, "meat_sprite", 120, 120, "Meat")
    $ barrel_sprite1 = MapUser(1, 9, "barrel_sprite", 120, 120, "Barrel")
    $ barrel_sprite2 = MapUser(12, 2, "barrel_sprite", 120, 120, "Barrel")
    $ sleepingmat_sprite1 = MapUser(15, 2, "sleepingmat_sprite0", 116, 175, "Mat")
    $ sleepingmat_sprite2 = MapUser(17, 2, "sleepingmat_sprite0", 136, 170, "Mat")
    $ sleepingmat_sprite4 = MapUser(15, 1, "empty", 116, 175, "Mat")
    $ sleepingmat_sprite5 = MapUser(17, 1, "empty", 136, 170, "Mat")
    $ sleepingmat_sprite3 = MapUser(17, 5, "sleepingmat_sprite0", 140, 168, "Mat")
    $ wolfsleeping_sprite1 = MapUser(17, 5, "wolfsleeping_sprite0", 140, 168, "WolfSleep")
    $ goatskull_sprite1 = MapUser(11, 9, "goatskull_sprite", 120, 120, "Goat")
    $ lwerewolf_sprite1 = MapUser(14, 8, "lwerewolf_sprite00", 150, 180, "Lister")
    $ werewolf_sprite1 = MapUser(1, 8, "werewolf left0", 120, 167, "Werewolf1")
    $ werewolf_sprite2 = MapUser(17, 2, "werewolf right0", 160, 167, "Werewolf2")
    $ werewolffist_sprite1 = MapUser(0, 3, "werewolffist_sprite", 140, 180, "Fister")
    $ bchest_sprite1 = MapUser(17, 3, "bchest_sprite1", 120, 120, "Chest")
    $ bonfire_sprite1 = MapUser(7, 5, "bonfire_sprite", 120, 120, "Bonfire")
    $ bwine_sprite1 = MapUser(7, 8, "bwine_sprite1", 120, 120, "Wine")
    $ bwine_sprite2 = MapUser(3, 9, "bwine_sprite2", 120, 120, "Wine")
    $ addBack(moonlit_dungeon, sleepingmat_sprite1)
    $ addBack(moonlit_dungeon, sleepingmat_sprite2)
    $ addBack(moonlit_dungeon, sleepingmat_sprite3)
    $ addSprite(moonlit_dungeon, sleepingmat_sprite4)
    $ addSprite(moonlit_dungeon, sleepingmat_sprite5)
    $ addBack(moonlit_dungeon, moonlitcorner_sprite1)
    $ addBack(moonlit_dungeon, moonlitcorner_sprite2)
    $ addBack(moonlit_dungeon, moonlitcorner_sprite3)
    $ addBack(moonlit_dungeon, moonlitcorner_sprite4)
    $ addBack(moonlit_dungeon, moonlitcorner_sprite5)
    $ addBack(moonlit_dungeon, moonlitcorner_sprite6)
    $ addBack(moonlit_dungeon, moonlitcorner_sprite7)
    $ addBack(moonlit_dungeon, moonlitcorner_sprite8)
    $ addBack(moonlit_dungeon, moonlitcorner_sprite9)
    $ addBack(moonlit_dungeon, moonlitcorner_sprite10)
    $ addBack(moonlit_dungeon, moonlitcorner_sprite11)
    $ addBack(moonlit_dungeon, moonlitcorner_sprite12)
    $ addSprite(moonlit_dungeon, moonlitexit_sprite1)
    $ addSprite(moonlit_dungeon, wolfsleeping_sprite1)
    $ addSprite(moonlit_dungeon, lwerewolf_sprite1)
    $ addSprite(moonlit_dungeon, goatskull_sprite1)
    $ addSprite(moonlit_dungeon, barrel_sprite1)
    $ addSprite(moonlit_dungeon, barrel_sprite2)
    $ addSprite(moonlit_dungeon, meat_sprite1)
    $ addSprite(moonlit_dungeon, meat_sprite2)
    $ addSprite(moonlit_dungeon, moonstone_sprite1)
    $ addSprite(moonlit_dungeon, moonstone_sprite2)
    $ addSprite(moonlit_dungeon, moonstone_sprite3)
    $ addSprite(moonlit_dungeon, moonpebble_sprite1)
    $ addBack(moonlit_dungeon, moonpebble_sprite2)
    $ addSprite(moonlit_dungeon, moonpebble_sprite3)
    $ addSprite(moonlit_dungeon, werewolf_sprite1)
    $ addSprite(moonlit_dungeon, werewolf_sprite2)
    $ addSprite(moonlit_dungeon, werewolffist_sprite1)
    $ addSprite(moonlit_dungeon, tart_sprite)
    $ addSprite(moonlit_dungeon, tart_sprite1)
    $ addBack(moonlit_dungeon, bwine_sprite1)
    $ addBack(moonlit_dungeon, bwine_sprite2)
    $ addSprite(moonlit_dungeon, bchest_sprite1)
    $ addSprite(moonlit_dungeon, bonfire_sprite1)
    $ addSprite(moonlit_dungeon, uffe_sprite)
    $ addSprite(moonlit_dungeon, uffe_sprite1)
    $ addSprite(moonlit_dungeon, tenki_sprite12)
    $ current_location = moonlit_dungeon
    jump Moonlit_Wolf_Den_Loop

label Moonlit_Wolf_Den_Loop:
    $ disableC = False
    $ sprite = tenki_sprite12
    show screen dungeon_buttons
    call screen dungeon_map(moonlit_dungeon)

    if _return == "Exit":
        $ disableC = True
        show screen dungeon_map(moonlit_dungeon)
        hide screen dungeon_buttons
        "You exit the werewolves' den."
        call Leaving_Moonlit_Wolf_Den from _call_Leaving_Moonlit_Wolf_Den
        jump Dark_Forest_Map

    if _return == "Uffe":
        $ disableC = True
        hide screen dungeon_buttons
        scene moonlit_wolf_den with dissolve
        show uffe normal with dissolve
        jump Uffe_Normal_Talk

    if _return == "Werewolf1":
        $ disableC = True
        show screen dungeon_map(moonlit_dungeon)
        hide screen dungeon_buttons
        ww2 "Ready to hunt, little prey? I can give you a private lesson. Only us two."
        e "Uh, no thanks..."

    if _return == "WolfSleep":
        $ disableC = True
        show screen dungeon_map(moonlit_dungeon)
        hide screen dungeon_buttons
        "The werewolf is snoring loudly, much of what's expected from a werewolf in dark forest."
        ww4 "Duh, duh, duh, duh... duh..."
        "He seems to be mumbling some tunes, but you don't recognise that."

    if _return == "Fister":
        $ disableC = True
        show screen dungeon_map(moonlit_dungeon)
        hide screen dungeon_buttons
        ww5 "See this, I call this un-clawing."
        "The werewolf says as he throws a fist towards you."
        ww5 "I'm using my claws, but instead of opening my palm, I close it like this."
        e "Isn't that just punching?"
        ww5 "No! I call this un-clawing, didn't you hear? I hide all these nails to increase my raw power."
        ww5 "It's good for when you want to knock someone out. Do you wanna try?"
        e "To punch?"
        ww5 "No, I am the one un-clawing."

    if _return == "Lister":
        $ disableC = True
        show screen dungeon_map(moonlit_dungeon)
        hide screen dungeon_buttons
        ww "Three pieces of meat, one piece of bone... 5 or 6 bottles of wine... and a book?"
        ww "Which son of a tool put a book in our inventory again, you can't eat all that pages."
        ww "Unless...?"

    if _return == "Werewolf2":
        $ disableC = True
        show screen dungeon_map(moonlit_dungeon)
        hide screen dungeon_buttons
        ww3 "You're not werewolf-shaped... you are not even wolf-shaped."
        e "Uffe allowed me here."
        ww3 "Alright, walking meat. I'll one-up the alpha and allow you in my stomach, wanna come in?"
        e "Uhmm..."

    if _return == "Meat":
        $ disableC = True
        show screen dungeon_map(moonlit_dungeon)
        hide screen dungeon_buttons
        if renpy.random.random() > 0.5:
            tart "No take! Tres-Passers deserves no meat."
        else:
            tart "Alpha says, food is for Alpha."


    if _return == "Tart":
        $ disableC = True
        show screen dungeon_map(moonlit_dungeon)
        hide screen dungeon_buttons
        if not tart_first_meet:
            $ tart_first_meet = True
            tart "What you doing, tres-Passer?"
            e "Uh... I'm just looking around, who are you?"
            tart "Is Tart."
            e "Oh, you mean the food?"
            tart "No, food doesn't like Tart. I am Tart."
            e "O-ok, that was confusing to say the least."
            tart "You are watching out. Alpha says what, you do what."
            tart "Alpha saying, you keep silent."
            tart "Saying no means death. No?"
            "You're not entirely sure what he means, so you just nod."
            e "Uh, yes."
            e "Are you very close with Uffe?"
            tart "He's Alpha, Tart helps alpha. Very easy to under-Stand."
            "Tart says as he scratches the ground with his nails."
            e "What do you do other than... defending the alpha?"
            tart "Tart's purpose is to keep alpha safe."
            "The grey werewolf scratches the fur on his chin, then continues staring at you."
            tart "If you raise weapon, Tart will kill. Don't do that, no?"
            e "A-alright, you have my words."
        elif quest34.status == 2:
            tart "Alpha is mad. No one solves the puzzle."
            e "Uffe told me to go there as well, what's the puzzle like?"
            tart "Not seen. Tart sends one of us to stay. He stucks still. It takes too long."
            tart "We need hunt, not think. Alpha is not understanding. But Tart... protects alpha."
            tart "You need please alpha. Think. Think!"
        elif quest36.status == 2:
            tart "Were-Wolves escaped. Alpha is mad again. You blow whistle, easy."
            e "Who are these werewolves that we needed to catch, Tart?"
            tart "Tart's frien-"
            tart "Enemy! They are alpha's enemy."
            e "Friends? Have you talked with them before?"
            tart "Yes, but they changed."
            tart "I never know when they leave. I... not under-Stand."
            tart "Our pack is always good. Why they want to leave..."
        elif quest34.status and renpy.random.random() < 0.4:
            tart "It's end. Amulet is back for alpha."
            e "Can you let me know what's the use of that moonstone amulet?"
            tart "More power. You sacrifice something for more power."
            tart "Alpha says he can use full potential of the amulet, but Tart does not under-Stand."
            tart "Soon we conquer out of dark forest, amulet is only first step."
        elif quest36.status and renpy.random.random() < 0.4:
            tart "The brothers are back."
            e "W-wait, so where are they... did Uffe really killed them?"
            tart "No, no yet. They're locked away."
            tart "Alpha says there is some use to them, so Tart guards Tetto and Rumma."

        elif True:
            if renpy.random.random() < 0.4:
                "The grey werewolf stares at you silently."
            else:
                "You hear a rumbling sound in the direction of the grey werewolf."
                e "Uh, Tart, you need some food?"
                tart "N-no. Tart is not to eat at this time."
                "He turns his head away."

        elif TaskAvailable(task07, quest22) and task07.completedtimes == 0:

            tart "Hey, tres-Passer, Tart's hungry. Meat?"
            e "D-don't your pack have food?"
            tart "Food's not for Tart, it's for alpha."
            e "Uh... Can't you just ask Alpha? You're like his right-hand wolf after all."
            tart "Meat, give meat. Tart's tummy shouting."
            e "Alright, how much do you want?"
            menu:
                tart "If tres-Passer has 5 meat, Tart gives toys."
                "Accept the Task {#TartTask}":
                    e "Alright, I'll get you the meat."
                "Decline {#TartTask}":
                    e "Sorry, I don't have that many meat."
                    tart "Ok. Tart stays, hungry."



    jump Moonlit_Wolf_Den_Loop

label Leaving_Moonlit_Wolf_Den:

    $ removeSprite(moonlit_dungeon, tenki_sprite12)
    hide screen dungeon_map
    hide screen dungeon_buttons

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
