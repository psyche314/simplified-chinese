
default forgotten_sanctuary_map = {"None": 0, "tree1": 1, "tree2": 2, "bush6": 3, "tree4": 4,  "tree5": 5, "shrinewall": 6, "shrine2": 7, "cliff1": 8, "bush5": 9}

image pawprint_sprite front:
    "pawprint_sprite1"
    rotate (180)
    anchor (0, 0.5)

image pawprint_sprite back:
    "pawprint_sprite1"
    rotate (0)
    anchor (0, -0.5)

image pawprint_sprite right:
    "pawprint_sprite1"
    rotate (90)
    anchor (0.5, 0)

image pawprint_sprite left:
    "pawprint_sprite1"
    rotate (270)
    anchor (-0.5, 0)


label Forgotten_Sanctuary_Enter:
    $ forgotten_sanctuary = MapPat([], "Forgotten Sanctuary", 11, 11, "grass2")
    $ forgotten_sanctuary.playerSprite = MapUser(11, 11, "e_dungeon", 120, 120, {})
    $ forgotten_sanctuary.floorPlan([
        [0, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 0],
        [7, 0, 6, 6, 0, 0, 0, 0, 0, 6, 6, 0, 7],
        [7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7],
        [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
        [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
        [7, 6, 6, 0, 0, 0, 0, 0, 0, 0, 6, 6, 7],
        [0, 0, 0, 7, 6, 6, 0, 6, 6, 7, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7],
        [4, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 8, 0, 0, 3, 9, 9, 9, 0, 0, 0, 0, 9],
        [1, 0, 0, 0, 0, 3, 3, 3, 8, 8, 8, 8, 3],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 5, 5, 0, 5, 5],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    ], forgotten_sanctuary_map)

    $ dg = forgotten_sanctuary.playerSprite.interaction
    $ dg["Path1"] = [(4, 12), (1, 10), (4, 10)]
    $ dg["Path2"] = [(11, 7), (8, 8), (10, 8), (11, 6)]
    $ dg["Path3"] = [(3, 4), (5, 1), (8, 3), (11, 4), (6, 3)]
    $ dg["Num"] = 0
    $ dg["On Path"] = "Path1"

    $ slime_sprite1 = MapChaser(10, 12, "slime_sprite_a", 120, 120, "Slime1", [False, "", "", ""], 5, 1,"slime_sprite_a", "slime_sprite_0")
    $ button_sprite1 = MapUser(9, 11, "button_sprite2", 120, 120, "Button")
    $ button_sprite2 = MapUser(4, 7, "button_sprite3", 120, 120, "Button2")
    $ button_spritea = MapUser(11, 7, "button_spritea", 120, 120, "Button")
    $ button_spriteb = MapUser(8, 8, "button_spriteb", 120, 120, "Button")
    $ button_spritec = MapUser(10, 8, "button_spritec", 120, 120, "Button")
    $ button_sprited = MapUser(11, 6, "button_sprited", 120, 120, "Button")
    $ button_spritee = MapUser(4, 12, "button_spritee", 120, 120, "Button")
    $ button_spritef = MapUser(1, 10, "button_spritef", 120, 120, "Button")
    $ button_spriteg = MapUser(4, 10, "button_spriteg", 120, 120, "Button")
    $ button_spritel = MapUser(3, 4, "button_spritel", 120, 120, "Button")
    $ button_spriteh = MapUser(5, 1, "button_spriteh", 120, 120, "Button")
    $ button_spritei = MapUser(8, 3, "button_spritei", 120, 120, "Button")
    $ button_spritej = MapUser(11, 4, "button_spritej", 120, 120, "Button")
    $ button_spritek = MapUser(6, 3, "button_spritek", 120, 120, "Button")
    $ page_sprite1 = MapUser(1, 6, "botanical_page", 120, 120, "Page")
    $ barrel_sprite1 = MapUser(3, 11, "barrel_sprite", 120, 120, "Barrel")
    $ wooddoor_sprite1 = MapUser(5, 11, "wooddoor_sprite", 120, 165, "Door")
    $ wooddoor_sprite2 = MapUser(5, 11, "wooddoor_sprite2", 120, 165, "Door")
    $ wooddoor_sprite3 = MapUser(12, 8, "wooddoor_sprite", 120, 165, "Door")
    $ wooddoor_sprite4 = MapUser(12, 8, "wooddoor_sprite2", 120, 165, "Door4")
    $ wooddoor_sprite5 = MapUser(0, 12, "wooddoor_sprite", 120, 165, "Door")
    $ wooddoor_sprite6 = MapUser(0, 12, "wooddoor_sprite2", 120, 165, "Door6")
    $ cliff_sprite1 = MapUser(2, 9, "cliff2",120, 120, "Cliff")
    $ shrine_sprite1 = MapUser(0, 0, "shrine1",120, 132, "Shrine")
    $ shrine_sprite2 = MapUser(1, 1, "shrine1",120, 132, "Shrine")
    $ shrine_sprite3 = MapUser(12, 0, "shrine1",120, 132, "Shrine")
    $ shrine_sprite4 = MapUser(11, 1, "shrine1",120, 132, "Shrine")
    $ shrine_sprite5 = MapUser(3, 5, "shrine1",120, 132, "Shrine")
    $ shrine_sprite6 = MapUser(9, 5, "shrine1",120, 132, "Shrine")
    $ shrine_sprite7 = MapUser(0, 6, "shrine1",120, 132, "Shrine")
    $ shrine_sprite8 = MapUser(12, 6, "shrine1",120, 132, "Shrine")
    $ shrinedoor_sprite1 = MapUser(6, 0, "shrinedoor1", 120, 120, "ShrineDoor1")
    $ shrinedoor_sprite2 = MapUser(6, 0, "shrinedoor3", 120, 120, "ShrineDoor2")
    $ shrinedoor_sprite3 = MapUser(6, 6, "shrinedoor1", 120, 120, "ShrineDoor3")
    $ shrinedoor_sprite4 = MapUser(6, 6, "shrinedoor2", 120, 120, "ShrineDoor4")
    $ pillar_sprite1 = MapUser(3, 3, "pillar_sprite",120, 180, "Pillar1")
    $ pillar_sprite2 = MapUser(6, 4, "pillar_sprite2",120, 120, "Pillar2")
    $ pillar_sprite3 = MapUser(9, 3, "pillar_sprite",120, 180, "Pillar3")
    $ pillar_sprite4 = MapUser(7, 2, "pillar_sprite",120, 180, "Pillar4")
    $ exit_sprite1 = MapUser(12, 11, "grass3",120,120,"Exit")
    $ fsign_sprite1 = MapUser(3, 9, "gsign_sprite1",120,120, "Fsign")
    $ current_location = forgotten_sanctuary
    $ pawprint_sprite1 = MapUser(4, 1, "pawprint_sprite1", 120, 120, "Pawprint")
    $ pawprint_sprites = []
    $ addSprite(forgotten_sanctuary, forgotten_sanctuary.playerSprite)
    $ addSprite(forgotten_sanctuary, slime_sprite1)
    $ addSprite(forgotten_sanctuary, barrel_sprite1)
    $ addBack(forgotten_sanctuary, wooddoor_sprite2)
    $ addBack(forgotten_sanctuary, cliff_sprite1)
    $ addSprite(forgotten_sanctuary, wooddoor_sprite3)
    $ addSprite(forgotten_sanctuary, wooddoor_sprite5)
    $ addSprite(forgotten_sanctuary, shrine_sprite1)
    $ addSprite(forgotten_sanctuary, shrinedoor_sprite1)
    $ addSprite(forgotten_sanctuary, shrinedoor_sprite3)
    $ addSprite(forgotten_sanctuary, shrine_sprite2)
    $ addSprite(forgotten_sanctuary, shrine_sprite3)
    $ addSprite(forgotten_sanctuary, shrine_sprite4)
    $ addSprite(forgotten_sanctuary, shrine_sprite5)
    $ addSprite(forgotten_sanctuary, shrine_sprite6)
    $ addSprite(forgotten_sanctuary, shrine_sprite7)
    $ addSprite(forgotten_sanctuary, shrine_sprite8)
    $ addSprite(forgotten_sanctuary, pillar_sprite1)
    $ addSprite(forgotten_sanctuary, exit_sprite1)
    $ addSprite(forgotten_sanctuary, fsign_sprite1)
    $ addSprite(forgotten_sanctuary, pillar_sprite2)
    $ addSprite(forgotten_sanctuary, pillar_sprite3)
    $ addSprite(forgotten_sanctuary, pillar_sprite4)
    $ addBack(forgotten_sanctuary, page_sprite1)
    $ addBack(forgotten_sanctuary, button_sprite1)
    $ addBack(forgotten_sanctuary, button_sprite2)
    $ addBack(forgotten_sanctuary, button_spritea)
    $ addBack(forgotten_sanctuary, button_spriteb)
    $ addBack(forgotten_sanctuary, button_spritec)
    $ addBack(forgotten_sanctuary, button_sprited)
    $ addBack(forgotten_sanctuary, button_spritee)
    $ addBack(forgotten_sanctuary, button_spritef)
    $ addBack(forgotten_sanctuary, button_spriteg)
    $ addBack(forgotten_sanctuary, button_spritel)
    $ addBack(forgotten_sanctuary, button_spriteh)
    $ addBack(forgotten_sanctuary, button_spritei)
    $ addBack(forgotten_sanctuary, button_spritej)
    $ addBack(forgotten_sanctuary, button_spritek)
    $ dungeon_timers = []
    $ slime1_dp[0] = 0
    $ slime2_dp[0] = 0
    $ slime3_dp[0] = 0
    $ slime4_dp[0] = 0
    $ slime5_dp[0] = 0

    jump Forgotten_Sanctuary_Loop


label Forgotten_Sanctuary_Loop:
    show screen dungeon_buttons
    $ sprite = forgotten_sanctuary.playerSprite
    $ disableC = False
    $ dungeon_timers = []
    if forgotten_sanctuary.mappy[7][4].user != None or slime3_dp[0] > 0:
        if forgotten_sanctuary.mappy[7][4].user != None:
            $ slime3_dp[0] = 2
            $ removeBack(forgotten_sanctuary, shrinedoor_sprite4)
        if forgotten_sanctuary.mappy[6][6].back == None:
            if forgotten_sanctuary.mappy[6][6].user == shrinedoor_sprite3:
                $ removeSprite(forgotten_sanctuary, shrinedoor_sprite3)
            $ addBack(forgotten_sanctuary, shrinedoor_sprite4)
        $ slime3_dp[0] -= 1
    else:
        $ slime3_dp[0] = 0
        $ removeBack(forgotten_sanctuary, shrinedoor_sprite4)
        $ addSprite(forgotten_sanctuary, shrinedoor_sprite3)

    if forgotten_sanctuary.mappy[11][9].user != None or slime1_dp[0] > 0:
        if forgotten_sanctuary.mappy[11][9].user != None:
            $ slime1_dp[0] = 2
            $ removeBack(forgotten_sanctuary, wooddoor_sprite2)
        if forgotten_sanctuary.mappy[11][5].user == None:
            $ removeBack(forgotten_sanctuary, wooddoor_sprite2)
            $ addSprite(forgotten_sanctuary, wooddoor_sprite1)
        $ slime1_dp[0] -= 1
    else:
        $ slime1_dp[0] = 0
        if forgotten_sanctuary.mappy[11][5].user == wooddoor_sprite1:
            $ removeSprite(forgotten_sanctuary, wooddoor_sprite1)
        $ addBack(forgotten_sanctuary, wooddoor_sprite2)

    if dg["Num"] > 0:
        if forgotten_sanctuary.locateBackOnTop(sprite) != None and forgotten_sanctuary.locateBackOnTop(sprite).interaction == "Pawprint":
            $ forgotten_sanctuary.clearBack(interaction = "Pawprint")
            $ dg["Num"] = 0
        elif forgotten_sanctuary.locateBackOnTop(sprite) == None:
            $ x, y = sprite.getLocation()
            $ newSpriteImg = "pawprint_sprite " + e_d
            $ addBack(forgotten_sanctuary, MapUser(x, y, newSpriteImg, 120, 120, "Pawprint"))
        else:
            $ x, y = sprite.getLocation()
            $ newSpriteImg = "pawprint_sprite " + e_d
            $ addFront(forgotten_sanctuary, MapUser(x, y, newSpriteImg, 120, 120, "Pawprint"))

    if forgotten_sanctuary.locateBackOnTop(sprite) != None and forgotten_sanctuary.locateBackOnTop(sprite).interaction == "Button":
        if dg["Num"] <= len(dg["Path1"])-1 and sprite.getLocation() == dg["Path1"][dg["Num"]]:
            $ dg["Num"] += 1
            $ dg["On Path"] = "Path1"
            if dg["Num"] == len(dg["Path1"]):
                if forgotten_sanctuary.mappy[8][12].user == wooddoor_sprite3:
                    $ removeSprite(forgotten_sanctuary, wooddoor_sprite5)
                    $ addSprite(forgotten_sanctuary, wooddoor_sprite6)
                $ dg["Num"] = 0
        elif sprite.getLocation() == dg["Path1"][0]:
            $ forgotten_sanctuary.clearBack(interaction = "Pawprint")
            $ dg["Num"] = 1
            $ dg["On Path"] = "Path1"
        elif dg["On Path"] == "Path1":
            $ forgotten_sanctuary.clearBack(interaction = "Pawprint")
            $ dg["Num"] = 0
            $ dg["On Path"] = "None"

        if dg["Num"] <= len(dg["Path2"])-1 and sprite.getLocation() == dg["Path2"][dg["Num"]]:
            $ dg["Num"] += 1
            $ dg["On Path"] = "Path2"
            if dg["Num"] == len(dg["Path2"]):
                if forgotten_sanctuary.mappy[8][12].user == wooddoor_sprite3:
                    $ removeSprite(forgotten_sanctuary, wooddoor_sprite3)
                    $ addSprite(forgotten_sanctuary, wooddoor_sprite4)
                $ dg["Num"] = 0
        elif sprite.getLocation() == dg["Path2"][0]:
            $ forgotten_sanctuary.clearBack(interaction = "Pawprint")
            $ dg["Num"] = 1
            $ dg["On Path"] = "Path2"
        elif dg["On Path"] == "Path2":
            $ forgotten_sanctuary.clearBack(interaction = "Pawprint")
            $ dg["Num"] = 0
            $ dg["On Path"] = "None"
        if dg["Num"] <= len(dg["Path3"])-1 and sprite.getLocation() == dg["Path3"][dg["Num"]]:
            $ dg["Num"] += 1
            $ dg["On Path"] = "Path3"
            if dg["Num"] == len(dg["Path3"]):
                if forgotten_sanctuary.mappy[0][6].user == shrinedoor_sprite1:
                    $ removeSprite(forgotten_sanctuary, shrinedoor_sprite1)
                    $ addSprite(forgotten_sanctuary, shrinedoor_sprite2)
                $ dg["Num"] = 0
        elif sprite.getLocation() == dg["Path3"][0]:
            $ forgotten_sanctuary.clearBack(interaction = "Pawprint")
            $ dg["Num"] = 1
            $ dg["On Path"] = "Path3"
        elif dg["On Path"] == "Path3":
            $ forgotten_sanctuary.clearBack(interaction = "Pawprint")
            $ dg["Num"] = 0
            $ dg["On Path"] = "None"



    if slime_sprite1.x == 6 and sprite.x < slime_sprite1.x:
        $ slime_sprite1.kp = 5
    call screen dungeon_map(forgotten_sanctuary)
    if _return == "Restart":
        call Leaving_Forgotten_Sanctuary from _call_Leaving_Forgotten_Sanctuary
        jump Dark_Forest_Map
    if _return == "Page":
        $ disableC = True
        show screen dungeon_map(forgotten_sanctuary)
        "Yet another page is on the ground."
        "There is nothing that immediately pops out to you."
        if not LookForItem("Botanical Journal", inventory):
            "You have nowhere to store this page in. For now, you'll have to leave it where it is."
        else:
            menu:
                "Would you like to pick it up?"
                "Yes{#pickupbotanicalpage2}":
                    "You've already picked up the book. There's no reason not to fill it out."
                    $ removeSprite(forgotten_sanctuary, page_sprite1)
                    $ botanical_journal02.addTo(botanical_journal)
                    $ book_page = LookForPage(botanical_journal, botanical_journal02)
                    show screen book_read(botanical_journal)
                    "You bend down to pick up the page, and brush off the slime. Taking the book out of your inventory, you place this page behind the first you found."
                    "Now that you have everything organized, you start to read the new fragment."

                    pause 1
                    "There is a short gap in the writing, as if the author was unsure of what to say."
                    call Book_Botanical_Journal from _call_Book_Botanical_Journal
                    msg "New Page has been added to the Book."
                "No{#pickupbotanicalpage2}":

                    "It's for the best if you leave it here for now - it's been preserved up until now, why disturb it."



    if _return == "Door4":
        $ disableC = True
        scene black
        hide screen dungeon_map
        "You walk through the door, there seem to be a huge... slime right in front of you..."
        $ mimic_num = 3
        jump Forgotten_Sanctuary_Hefty
    if _return == "Door6":
        $ disableC = True
        scene black
        hide screen dungeon_map
        "You walk through the door, there seem to be a huge... slime right in front of you..."
        $ mimic_num = 4
        jump Forgotten_Sanctuary_Hefty
    if _return == "ShrineDoor2":
        $ disableC = True
        scene black
        hide screen dungeon_map
        "You walk through the back of the shrine... A huge slime, almost twice your height, appears in front of you."
        "Instead of merely a ball shaped goo, this... this one has arms extruded in front of it..."
        jump malignantslime_battle
    if _return == "Fsign":
        $ disableC = True
        scene black
        pause 1
        scene buttonadvicefriend with dissolve
        hide screen dungeon_map
        "You take a look at the note in front of you, it seems to be left here by a werewolf."
        "The sign describes the plate puzzle in front of you in a symbolic manner."
        "The plate buttons seem to suggest a certain pattern and sequence that you have to walk over..."
        "And the catch is, the adventurer cannot step on the same square twice."
        "Finishing the puzzle unlocks a door in which leads to where slimes reside."
        scene black with dissolve
    if _return == "Exit":
        "You leave the forgotton sanctuary along the path ahead of you."
        call Leaving_Forgotten_Sanctuary from _call_Leaving_Forgotten_Sanctuary_3
        jump Dark_Forest_Map

    jump Forgotten_Sanctuary_Loop
label Leaving_Forgotten_Sanctuary:
    $ removeSprite(forgotten_sanctuary, forgotten_sanctuary.playerSprite)
    $ removeSprite(forgotten_sanctuary, slime_sprite1)
    hide screen dungeon_map
    hide screen dungeon_buttons
    return
label Forgotten_Sanctuary_Hefty:
    "The big slime begins approaching you..."
    e "F-fuck, that's bigger than those in the green forest..."
    jump heftyslime_battle

default tenki_sprite10 = MapUser(12, 11, "e_dungeon", 120, 200, no_op)

image lwerewolf_sprite0:
    "lwerewolf_sprite1"
    size (300, 300)
    pause 0.7
    "lwerewolf_sprite2"
    size (300, 300)
    pause 0.5
    "lwerewolf_sprite1"
    size (300, 300)
    pause 4
    "lwerewolf_sprite3"
    size (300, 300)
    pause 0.5
    repeat

image empty8:
    "empty"
    size (90, 90)

label Whispering_Hollow_Enter:
    hide screen menu_buttons
    $ d10x = 17
    $ d10y = 10
    $ tenki_sprite10 = MapUser(d10x, d10y, "e_dungeon", 120, 200, no_op)
    $ dungeon_timers = []
    $ dungeon10_map = [
    [MapTile(MapThing("bush5")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("tree1")), MapTile(MapThing("bush5"))],
    [MapTile(MapThing("bush6")), MapTile(MapThing("bush5")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("tree2")), MapTile(MapThing("bush5")), MapTile(MapThing("bush6"))],
    [MapTile(MapThing("tree4")), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush5")), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush1")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(MapThing("bush1")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("cliff1")), MapTile(), MapTile(MapThing("cliff1")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("bush5")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(), MapTile(MapThing("cliff1")), MapTile(), MapTile(MapThing("cliff1")), MapTile(MapThing("bush5")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("tree4"))],
    [MapTile(MapThing("tree4")), MapTile(), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(MapThing("bush5")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile()],
    [MapTile(MapThing("tree5")), MapTile(), MapTile(), MapTile(MapThing("cliff1")), MapTile(), MapTile(), MapTile(MapThing("bush6")), MapTile(MapThing("bush1")), MapTile(), MapTile(MapThing("bush6")), MapTile(), MapTile(MapThing("bush1")), MapTile(), MapTile(MapThing("bush1")), MapTile(MapThing("bush1")), MapTile(MapThing("bush1")), MapTile(MapThing("bush1")), MapTile(MapThing("bush1")), MapTile(MapThing("bush1"))],
    [MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1")), MapTile(MapThing("cliff1"))],

    ]


    $ whispering_hollow = MapPat(dungeon10_map, "Whispering Hollow", d10x, d10y, "grass2")
    $ current_location = whispering_hollow
    $ sprite = tenki_sprite10
    $ cliff2_sprite1 = MapUser(7, 8, "cliff2", 120, 120, "cliff2")
    $ cliff2_sprite2 = MapUser(9, 8, "cliff2", 120, 120, "cliff2")
    $ cliff2_sprite3 = MapUser(8, 6, "cliff2", 120, 120, "cliff2")
    $ cliff2_sprite4 = MapUser(17, 6, "cliff2", 120, 120, "cliff2")
    $ barrel_sprite1 = MapUser(4, 9, "barrel_sprite", 120, 120, "Barrel")
    $ barrel_sprite2 = MapUser(4, 10, "barrel_sprite", 120, 120, "Barrel")
    $ barrel_sprite3 = MapUser(14, 10, "barrel_sprite", 120, 120, "Barrel")
    $ crosssign_sprite1 = MapUser(5, 11, "crosssign_sprite", 120, 120, "Crosssign")
    $ crosssign_sprite2 = MapUser(1, 8, "crosssign_sprite", 120, 120, "Crosssign")
    $ mimic_sprite1 = MapUser(8, 7, "mimic_sprite", 120, 120, "Mimic")
    $ lwerewolf_sprite1 = MapUser(13, 5, "lwerewolf_sprite0", 180, 210, "lwerewolf")
    $ gate_sprite1 = MapUser(17, 4, "gate_sprite1", 120, 120, "Gate")
    $ gate_sprite2 = MapUser(17, 4, "gate_sprite2", 120, 120, "Gate")
    $ whillar_sprite1 = MapUser(10, 4, "whillar_sprite1", 120, 135, "Whillar1")
    $ whillar_sprite2 = MapUser(3, 3, "whillar_sprite2", 120, 135, "Whillar2")
    $ whillar_sprite3 = MapUser(5, 4, "whillar_sprite3", 120, 135, "Whillar3")
    $ whillar_sprite4 = MapUser(9, 3, "whillar_sprite4", 120, 135, "Whillar4")
    $ whillar_sprite5 = MapUser(12, 3, "whillar_sprite5", 120, 135, "Whillar5")
    $ whillar_sprite01 = MapUser(10, 4, "whillar_sprite1", 120, 135, "Whillar1")
    $ whillar_sprite02 = MapUser(3, 3, "whillar_sprite2", 120, 135, "Whillar2")
    $ whillar_sprite03 = MapUser(5, 4, "whillar_sprite3", 120, 135, "Whillar3")
    $ whillar_sprite04 = MapUser(9, 3, "whillar_sprite4", 120, 135, "Whillar4")
    $ whillar_sprite05 = MapUser(12, 3, "whillar_sprite5", 120, 135, "Whillar5")
    $ whilly_sprite1 = MapUser(6, 3, "whilly_sprite", 120, 135, "Whilly")
    $ whilly_sprite01 = MapUser(6, 3, "whilly_sprite", 120, 135, "Whilly")
    $ leave_sprite1 = MapUser(18, 10, "grass3", 120, 120, "Leave")
    $ shrub_sprite1 = MapUser(13, 9, "shrub_sprite", 130, 135, "Shrub")
    $ shrub_sprite2 = MapUser(11, 10, "shrub_sprite", 130, 135, "Shrub")
    $ shrub_sprite3 = MapUser(10, 9, "shrub_sprite", 130, 135, "Shrub")
    $ shrub_sprite4 = MapUser(9, 9, "shrub_sprite", 130, 135, "Shrub")
    $ shrub_sprite5 = MapUser(2, 9, "shrub_sprite", 130, 135, "Shrub")
    $ shrub_sprite6 = MapUser(3, 8, "shrub_sprite", 130, 135, "Shrub")
    $ shrub_sprite7 = MapUser(4, 8, "shrub_sprite", 130, 135, "Shrub")
    $ shrub_sprite8 = MapUser(3, 10, "shrub_sprite", 130, 135, "Shrub")
    $ shrub_sprite9 = MapUser(12, 5, "shrub_sprite", 130, 135, "Shrub")
    $ shrub_sprite10 = MapUser(6, 5, "shrub_sprite", 130, 135, "Shrub")
    $ shrub_sprite11 = MapUser(9, 4, "shrub_sprite", 130, 135, "Shrub")
    $ shrub_sprite12 = MapUser(14, 2, "shrub_sprite", 130, 135, "Shrub")
    $ shrub_sprite13 = MapUser(15, 2, "shrub_sprite", 130, 135, "Shrub")
    $ shrub_sprite14 = MapUser(16, 6, "shrub_sprite", 130, 135, "Shrub")
    $ shrub_sprite15 = MapUser(17, 7, "shrub_sprite", 130, 135, "Shrub")
    $ shrub_sprite16 = MapUser(17, 8, "shrub_sprite", 130, 135, "Shrub")
    $ shrub_sprite17 = MapUser(15, 8, "shrub_sprite", 130, 135, "Shrub")
    $ shrub_sprite18 = MapUser(3, 4, "shrub_sprite", 130, 135, "Shrub")
    $ shrub_sprite19 = MapUser(11, 3, "shrub_sprite", 130, 135, "Shrub")
    $ shrub_sprite20 = MapUser(1, 5, "shrub_sprite", 130, 135, "Shrub")
    $ whillar_score = 0
    $ addSprite(whispering_hollow, shrub_sprite1)
    $ addSprite(whispering_hollow, shrub_sprite2)
    $ addSprite(whispering_hollow, shrub_sprite3)
    $ addSprite(whispering_hollow, shrub_sprite4)
    $ addSprite(whispering_hollow, shrub_sprite5)
    $ addSprite(whispering_hollow, shrub_sprite6)
    $ addSprite(whispering_hollow, shrub_sprite7)
    $ addSprite(whispering_hollow, shrub_sprite8)
    $ addSprite(whispering_hollow, shrub_sprite9)
    $ addSprite(whispering_hollow, shrub_sprite10)
    $ addSprite(whispering_hollow, shrub_sprite11)
    $ addSprite(whispering_hollow, shrub_sprite12)
    $ addSprite(whispering_hollow, shrub_sprite13)
    $ addSprite(whispering_hollow, shrub_sprite14)
    $ addSprite(whispering_hollow, shrub_sprite15)
    $ addSprite(whispering_hollow, shrub_sprite16)
    $ addSprite(whispering_hollow, shrub_sprite17)
    $ addSprite(whispering_hollow, shrub_sprite18)
    $ addSprite(whispering_hollow, shrub_sprite19)
    $ addSprite(whispering_hollow, shrub_sprite20)
    $ addBack(whispering_hollow, cliff2_sprite1)
    $ addBack(whispering_hollow, cliff2_sprite2)
    $ addBack(whispering_hollow, cliff2_sprite3)
    $ addBack(whispering_hollow, cliff2_sprite4)
    $ addSprite(whispering_hollow, whillar_sprite1)
    $ addSprite(whispering_hollow, whillar_sprite2)
    $ addSprite(whispering_hollow, whillar_sprite3)
    $ addSprite(whispering_hollow, whillar_sprite4)
    $ addSprite(whispering_hollow, whillar_sprite5)
    $ addSprite(whispering_hollow, whilly_sprite1)
    $ addSprite(whispering_hollow, leave_sprite1)
    $ addSprite(whispering_hollow, lwerewolf_sprite1)
    $ addSprite(whispering_hollow, gate_sprite1)
    $ addSprite(whispering_hollow, barrel_sprite1)
    $ addSprite(whispering_hollow, barrel_sprite2)
    $ addSprite(whispering_hollow, barrel_sprite3)
    $ addSprite(whispering_hollow, mimic_sprite1)
    $ addBack(whispering_hollow, crosssign_sprite1)
    $ addBack(whispering_hollow, crosssign_sprite2)


    $ addSprite(whispering_hollow, sprite)
    jump Whispering_Hollow_Loop
default pillar_item = [None, None, None, None, None]
default lwerewolf_status = 0
label Whispering_Hollow_Loop:
    show screen dungeon_buttons
    $ disableC = False
    $ sprite = tenki_sprite10
    call screen dungeon_map(whispering_hollow)

    if whispering_hollow.mappy[11][5].user != None and whispering_hollow.mappy[11][5].user.img == "barrel_sprite":
        if whispering_hollow.mappy[8][1].user != None and whispering_hollow.mappy[8][1].user.img == "barrel_sprite":
            if gate_sprite1.img == "gate_sprite1":
                $ disableC = True
                show screen dungeon_map(whispering_hollow)
                "You hear a wooden clank sound from afar, it seems something has opened."

                $ removeSprite(whispering_hollow, gate_sprite1)
                $ gate_sprite1.img = "gate_sprite2"
                $ addBack(whispering_hollow, gate_sprite1)

    if _return == "Mimic":
        $ mimic_num = 4
        $ disableC = True
        show screen dungeon_map(whispering_hollow)
        "You run into a chest in the forest, you walk towards it, trying to open the chest."
        "Suddenly the chest jumps right into your face, it's not a chest, it is a mimic."
        "Mimic" "RAWAWWWR-"
        "You scream, its tongue is slithering out, trying to latch on you..."
        hide screen dungeon_map
        jump mimic_battle

    if _return == "Restart":
        call Leaving_Whispering_Hollow from _call_Leaving_Whispering_Hollow
        jump Whispering_Hollow_Enter
    if _return == "lwerewolf":
        $ disableC = True
        show screen dungeon_map(whispering_hollow)
        if lwerewolf_status > 1 and quest34.status == True:
            ww "Hey, dude. Guess what, Uffe doesn't let me return to our den."
            e "That's a bummer."
            ww "Yeah, yeah."
            "The werewolf continues watching over the empty hollow."

        elif LookForItem("Moonstone Amulet", inventory):
            $ lwerewolf_status += 1
            ww "Oh... damn. You've done it."
            ww "Turns out, what I need to put there is in my pocket all along!"
            "The werewolf reveals a piece of iron from his loincloth."
            ww "I was going to solve it so easily, if only all of the answers were meat, hmmm..."
            e "Yeah, guess I'm going back to Uffe with the amulet."
            ww "Good luck, dude."
            if quest34.status == 4 or quest34.status == True:
                ww "Oh, and remember to clear the shrubs. We're going to hunt down much more preys here."
            "He waves you a farewell, before sitting lazily."
        elif lwerewolf_status == 0:
            "You notice a huge werewolf peeking by the side of the hollow."
            "He looks worried, to say the least. Not overly aggressive like the others."
            ww "Oh?"
            "The werewolf notices you."
            ww "Uffe sent you?"
            e "Uhm... yes. I was worried you're going to attack me."
            ww "N-no. We don't have time for that."
            "Both of you remain silent for a minute, as the werewolf removes his gaze on you."
            "He takes another glance at the paper, and looks over the hollow."
            ww "Fuck, man. Why do we even bother with this thing."
            pause 1
            ww "We can't even speak our words among us werewolves, the situation has been tense ever since the brother became a monster."
            ww "We missed the time where we simply hunt our prey, or dig out some rocks."
            "It seems the werewolf is spilling out everything onto you."
            if vurro_lives:
                "As much as you want to tell him that you, alongside Wuldon and Vurro, will make sure the present would not last."
                "That won't be a possibility unless you fully trust this werewolf."
            else:
                ww "The brother was dead, thanks? Uffe told us he can smell what had happened in the cave."
                "The werewolf scratches his snout with uncertainty."
                ww "We can only hope times will get better, maybe if Uffe trusts me I can finally be the one who hunts."
            ww "Anyway, the hollow, we have no clue what that pillar's talking about..."
            "The werewolf points at the plate, with a paragraph of words."
            ww "{i}I am hard and unyielding, yet shaped by skilled hands.{w}{p}I can be honed to a deadly point, or used to till the land.{p}{w}What am I?{/i}"
            "He finishes the riddle with a loud sigh."
            ww "W-what can it be? We've spent a whole week over this, maybe it's food, or... meat? That's not right."
            ww "Or..."
            ww "Maybe it's food! Y-yes. Food. W-wait a minute..."
            "The werewolf falls into another period of pondering, you decide to leave him alone, and inspect the pillars."
            $ lwerewolf_status += 1
        elif lwerewolf_status == 1:
            $ lwerewolf_status += 1
            "You notice a huge werewolf peeking by the side of the hollow."

            ww "W-what can that mean? Hard and Unyielding... My cock can be like that, maybe not {i}honed to a deadly point.{/i}"
            ww "Wouldn't make sense to {i}till the land{/i} also."
            ww "But I can put my cock on the pillar, it'll probably fit."
            "Yes, that would not make sense, as you thought."

        elif whilly_sprite1.img == "Moonstone Amulet":
            ww "Oh hey! The amulet is right there! How did you do that?"
        else:
            $ lwerewolf_status += 1
            $ lwerewolf_dialogue = []
            if whillar_sprite4.img.lower() != "feather":
                $ lwerewolf_dialogue.append("feather")
            if whillar_sprite5.img.lower() != "iron ingot":
                $ lwerewolf_dialogue.append("iron ingot")
            if whillar_sprite1.img.lower() != "pocket bell":
                $ lwerewolf_dialogue.append("pocket bell")
            if whillar_sprite3.img.lower() != "horehound":
                $ lwerewolf_dialogue.append("horehound")
            if whillar_sprite2.img.lower() != "beer" and whillar_sprite2.img.lower() != "ale":
                $ lwerewolf_dialogue.append("beer")

            $ lwerewolf_speak = renpy.random.choice(lwerewolf_dialogue)
            if lwerewolf_speak == "horehound":
                ww "Wait, the beasts of the night, isn't that... us?"
                ww "Why would they repel us, must be something from the tasty goats again..."
                ww "They could have something there up their slippery sleeves."
            if lwerewolf_speak == "feather":
                ww "Whisper that brushes, sounds like my fur. Mine's delicate also."
                ww "My cock's... uh... more like a howl. But... dances with the wind?"
                ww "Stop being poetic! This is getting me so angry I can tear a bird in half!"
            if lwerewolf_speak == "pocket bell":
                ww "Chime... gentle? That sounds so obvious, it's the fuckin' bear's horn, right?"
                ww "That gives me shivers every time they try that across the mountains from here."
                ww "But seriously, where can I get a horn, from somwhere that's close enough, preferably a prey?"
            if lwerewolf_speak == "beer":
                ww "Warmth, bones. Sounds like a proper feast in my pack. the only thing missing is the meat."
                ww "But meat's not bitter, and it's a drink. Doesn't sound like something we have... unless we're talking about blood."
                ww "Though, what did we drink in the feast? We always had that at full moon, Can't bring myself to remember that stuff."
            if lwerewolf_speak == "iron ingot":
                ww "Hard and Unyielding..."
                ww "...What if it's something from the ground? We've had that in the mines before..."
            "You leave the werewolf alone to his thought once again."

    if _return == "Shrub":
        $ removeFrontSprite(whispering_hollow)
        if whispering_hollow.searchUser("shrub_sprite") == 0:
            $ disableC = True
            show screen dungeon_map(whispering_hollow)
            "After cutting through the last shrub, it seems you've cleared the area."
            if len(quest34.progress) > 1:
                $ quest34.progress[1].status = True
            $ quest34.status += 1

    if _return == "Whillar1":
        $ disableC = True
        show screen dungeon_map(whispering_hollow)
        $ mimic_num = 0
        "The Pillar says..."
        "{i}Small and dainty, I fit in your hand, my chime is gentle, but can be grand.{w}{p}With a flick of your wrist, I sing a tune, a sound that echoes, morning or noon.{p}{w}What am I?{/i}"
        call screen whinventory_screen()
    if _return == "Whillar2":
        $ disableC = True
        show screen dungeon_map(whispering_hollow)
        $ mimic_num = 1
        "The Pillar says..."
        "{i}I am a drink that can be sweet or bitter, a liquid that flows from a wooden splitter.{w}{p}I make you forget your troubles and strife, and bring warmth to your bones on a cold winter's night.{p}{w}What am I?{/i}"
        call screen whinventory_screen()
    if _return == "Whillar3":
        $ disableC = True
        show screen dungeon_map(whispering_hollow)
        $ mimic_num = 2
        "The Pillar says..."
        "{i}Bitter and rough, my leaves do abound, a herb of magic, both lost and found.{w}{p}My scent repels the beasts of the night, but for the cough, I bring relief in sight.{p}{w}What am I?{/i}"
        call screen whinventory_screen()
    if _return == "Whillar4":
        $ disableC = True
        show screen dungeon_map(whispering_hollow)
        $ mimic_num = 3
        "The Pillar says..."
        "{i}I am a whisper that brushes the air, a delicate thing that's both here and there.{w}{p}My touch is gentle, my sway is light, I dance with the wind, and vanish from sight.{p}{w}What am I?{/i}"
        call screen whinventory_screen()
    if _return == "Whillar5":
        $ disableC = True
        show screen dungeon_map(whispering_hollow)
        $ mimic_num = 4
        "The Pillar says..."
        "{i}I am hard and unyielding, yet shaped by skilled hands.{w}{p}I can be honed to a deadly point, or used to till the land.{p}{w}What am I?{/i}"
        call screen whinventory_screen()

    if _return == "Refresh":
        $ whillar_score = 0
        if pillar_item[0] != None:
            $ whillar_sprite1.img = pillar_item[0].img.lower()
            $ whillar_sprite1.w = 100
            $ addBack(whispering_hollow, whillar_sprite01)
        else:
            $ whillar_sprite1.img = "whillar_sprite1"
            $ whillar_sprite1.w = 120
            $ removeBack(whispering_hollow, whillar_sprite01)
        if pillar_item[1] != None:
            $ whillar_sprite2.img = pillar_item[1].img.lower()
            $ whillar_sprite2.w = 100
            $ addBack(whispering_hollow, whillar_sprite02)
        else:
            $ whillar_sprite2.img = "whillar_sprite2"
            $ whillar_sprite2.w = 120
            $ removeBack(whispering_hollow, whillar_sprite02)
        if pillar_item[2] != None:
            $ whillar_sprite3.img = pillar_item[2].img.lower()
            $ whillar_sprite3.w = 100
            $ addBack(whispering_hollow, whillar_sprite03)
        else:
            $ whillar_sprite3.img = "whillar_sprite3"
            $ whillar_sprite3.w = 120
            $ removeBack(whispering_hollow, whillar_sprite03)
        if pillar_item[3] != None:
            $ whillar_sprite4.img = pillar_item[3].img.lower()
            $ whillar_sprite4.w = 100
            $ addBack(whispering_hollow, whillar_sprite04)
        else:
            $ whillar_sprite4.img = "whillar_sprite4"
            $ whillar_sprite4.w = 120
            $ removeBack(whispering_hollow, whillar_sprite04)
        if pillar_item[4] != None:
            $ whillar_sprite5.img = pillar_item[4].img.lower()
            $ whillar_sprite5.w = 100
            $ addBack(whispering_hollow, whillar_sprite05)
        else:
            $ whillar_sprite5.img = "whillar_sprite5"
            $ whillar_sprite5.w = 120
            $ removeBack(whispering_hollow, whillar_sprite05)
        if whillar_sprite4.img.lower() == "feather":
            $ whillar_score += 1
        if whillar_sprite1.img.lower() == "pocket bell":
            $ whillar_score += 1
        if whillar_sprite5.img.lower() == "iron ingot":
            $ whillar_score += 1
        if whillar_sprite3.img.lower() == "horehound":
            $ whillar_score += 1
        if whillar_sprite2.img.lower() == "beer" or whillar_sprite2.img.lower() == "ale":
            $ whillar_score += 1
        if not LookForItem("Moonstone Amulet", inventory) and whillar_score == 5:
            $ disableC = True
            show screen dungeon_map(whispering_hollow)
            "The broken pillar next to you begin to glow."
            pause 0.5 
            "As you blink, an amulet suddenly appears out of thin air on top of the stone pillar."
            $ whilly_sprite1.img = "moonstone amulet"
            $ whilly_sprite1.w = 100
            $ addBack(whispering_hollow, whilly_sprite01)
        else:
            $ whilly_sprite1.img = "whilly_sprite"
            $ whilly_sprite1.w = 120
            $ removeBack(whispering_hollow, whilly_sprite01)

    if _return == "Whilly":
        $ disableC = True

        show screen dungeon_map(whispering_hollow)
        if whilly_sprite1.img == "whilly_sprite" and not (LookForItem("Moonstone Amulet", inventory) or quest34.status == 4 or quest34.status == True):
            "You stare at the broken pillar, there seems to be an aura of magic inside it that's pulling your life force in..."
            "There are 5 holes at the center of the broken pillar, and [whillar_score] of them are dimly lit."
            "It seems that something will happen here, if all five lights are ignited."
            "You retreat from the pillar."
        elif whilly_sprite1.img == "whilly_sprite":
            "You read the dim paragraph on the pillar."
            "{i}I am a moonstone of werewolf might, a symbol of strength in the fight.{w}{p}But to harness my true power and glory, the price of sacrifice must be your story.{/i}"
            "Without the amulet, all that's left in the pillar is its own self..."
        else:

            "You read the shining paragraph on the pillar."
            "{i}I am a moonstone of werewolf might, a symbol of strength in the fight.{w}{p}But to harness my true power and glory, the price of sacrifice must be your story.{/i}"
            "It fades soon after, leaving only the amulet on top of the pillar."
            "You snatch the moonstone amulet from its light, and put it in your bag."
            $ quest34.progress[0].status = True
            $ quest34.status += 1
            $ addItem("Moonstone Amulet", inventory, 1)
            $ whilly_sprite1.img = "whilly_sprite"
            $ whilly_sprite1.w = 120
            $ removeBack(whispering_hollow, whilly_sprite01)
    if _return == "Leave":
        $ disableC = True
        show screen dungeon_map(whispering_hollow)
        menu:
            "Do you wish to leave the dungeon? Game state will not be saved before its completion, items on the pillar will be automatically returned to your inventory."
            "Yes":
                call Leaving_Whispering_Hollow from _call_Leaving_Whispering_Hollow_1
                scene black with dissolve
                "Through the dirt trail, you leave the whispering hollow and return to the dark forest."
                jump Dark_Forest_Map
            "No":
                pass

    jump Whispering_Hollow_Loop

label Leaving_Whispering_Hollow:
    if whillar_sprite1.img != "whillar_sprite1":
        $ whretrieveItem(0)
    if whillar_sprite2.img != "whillar_sprite2":
        $ whretrieveItem(1)
    if whillar_sprite3.img != "whillar_sprite3":
        $ whretrieveItem(2)
    if whillar_sprite4.img != "whillar_sprite4":
        $ whretrieveItem(3)
    if whillar_sprite5.img != "whillar_sprite5":
        $ whretrieveItem(4)
    hide screen dungeon_map
    hide screen dungeon_buttons
    $ removeSprite(whispering_hollow, tenki_sprite10)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
