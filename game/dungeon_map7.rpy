default tenki_sprite11 = MapUser(12, 11, "e_dungeon", 120, 200, no_op)
default d11x = 11
default d11y = 11

image bandit_sprite up:
    anchor (0.25, 0.5)
    "bandit_spriteu2"
    pause 0.2
    "bandit_spriteu1"
    pause 0.2
    "bandit_spriteu2"
    pause 0.2
    "bandit_spriteu1"

image bandit_sprite down:
    anchor (0.25, 0.5)
    "bandit_sprited2"
    pause 0.2
    "bandit_sprited1"
    pause 0.2
    "bandit_sprited2"
    pause 0.2
    "bandit_sprited1"

image bandit_sprite left:
    anchor (0.25, 0.5)
    "bandit_spritel2"
    pause 0.2
    "bandit_spritel1"
    pause 0.2
    "bandit_spritel2"
    pause 0.2
    "bandit_spritel1"

image bandit_sprite right:
    anchor (0.25, 0.5)
    "bandit_spriter2"
    pause 0.2
    "bandit_spriter1"
    pause 0.2
    "bandit_spriter2"
    pause 0.2
    "bandit_spriter1"

default bchest_sprite_img = "bchest_sprite1"
label Bandits_Hideout_Enter:
    $ dungeon_timers = []
    $ d11x = 6
    $ d11y = 23
    $ tenki_sprite11 = MapUser(d11x, d11y, "e_dungeon", 120, 200, no_op)

    $ dungeon11_map = [
    [MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt")), MapTile(MapThing("bbrickt"))],
    [MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrickl")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrickr")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrickl")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrickr")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2"))],
    [MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrickr")), MapTile(MapThing("bbrick2"))],
    [MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrickl")), MapTile(), MapTile(MapThing("bbrickr")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrickl")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2"))],
    [MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(), MapTile(MapThing("bbrick2"))],
    [MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick")), MapTile(), MapTile(MapThing("bbrick"))],
    [MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(), MapTile(MapThing("bbrickr")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile()],
    [MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2"))],
    [MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(MapThing("bbrick2")),MapTile(MapThing("bbrick2")),MapTile(MapThing("bbrick2")), MapTile(), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrickr")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(MapThing("bbrick")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2"))],
    [MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(MapThing("bbrick2")),MapTile(MapThing("bbrick2")),MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrickr")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2"))],
    [MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(MapThing("bbrick")),MapTile(MapThing("bbrick")),MapTile(MapThing("bbrick")), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2"))],
    [MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2"))],
    [MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick"))],
    [MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2"))],
    [MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrickl")), MapTile(MapThing("bbrickr")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrickl")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrickr")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2"))],
    [MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2"))],
    [MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(MapThing("bbrick")), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrickl")), MapTile(), MapTile(MapThing("bbrickr   ")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2"))],
    [MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2"))],
    [MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2"))],
    [MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2"))],
    [MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2"))],
    [MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2"))],
    [MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2"))],
    [MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick")), MapTile(), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2"))],
    [MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(), MapTile(), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2")), MapTile(MapThing("bbrick2"))],
    [MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(), MapTile(), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick")), MapTile(MapThing("bbrick"))]

    ]

    $ bandit_floor1 = MapPat(dungeon11_map, "Bandit's Hideout", d11x, d11y, "bfloor")
    $ sprite = tenki_sprite11
    $ current_location = bandit_floor1

    $ bandit_sprite1 = MapLooker(11, 18, "bandit_sprited1", 140, 200, "Bandit", [["Left", 1], ["Up", 2], ["Right", 1], ["Down", 2]])
    $ bandit_sprite2 = MapLooker(2, 7, "bandit_sprited1", 140, 160, "Bandit", [["Right", 4], ["Down", 4], ["Left", 4], ["Up", 4]])
    $ bandit_sprite3 = MapLooker(16, 14, "bandit_sprited1", 140, 160, "Bandit", [["Up", 1], ["Down", 1], ["Right", 1], ["Up", 1], ["Down", 1], ["Right", 1], ["Up", 1], ["Down", 1], ["Right", 1], ["Up", 1], ["Down", 1], ["Left", 1], ["Up", 1], ["Down", 1], ["Left", 1], ["Up", 1], ["Down", 1], ["Left", 1]])
    $ bandit_sprite4 = MapLooker(15, 5, "bandit_sprited1", 140, 160, "Bandit", [["Up", 1], ["Right", 3], ["Down", 1], ["Up", 1], ["Left", 3], ["Down", 1]])
    $ bandit_sprite5 = MapLooker(2, 6, "bandit_sprited1", 140, 160, "Bandit", [["Left", 1], ["Up", 1], ["Left", 1], ["Up", 1], ["Right", 1], ["Down", 1], ["Right", 1], ["Down", 1]])
    $ bandit_sprite6 = MapLooker(18, 18, "bandit_sprited1", 140, 160, "Bandit", [["Down", 1], ["Right", 1], ["Up", 2], ["Left", 2], ["Down", 2], ["Right", 1], ["Up", 1]])
    $ bandit_sprite7 = MapLooker(10, 10, "bandit_sprited1", 140, 160, "Bandit", [["Down", 1], ["Up", 1], ["No", 2], ["Right", 1], ["Left", 1], ["No", 2]])

    if quest35.status == True:
        $ banditbed_sprite1 = MapUser(25, 2, "banditbed_sprite_shark", 120, 180, "BanditBedShark")
        $ banditbed_sprite2 = MapUser(26, 2, "empty0", 120, 150, "BanditBedShark")
    else:
        $ banditbed_sprite1 = MapUser(25, 2, "banditbed_sprite", 120, 180, "BanditBed")
        $ banditbed_sprite2 = MapUser(26, 2, "empty0", 120, 150, "BanditBed")
    $ bonfire_sprite1 = MapUser(25, 3, "bonfire_sprite", 120, 120, "Bonfire")
    $ bonfire_sprite2 = MapUser(26, 3, "bonfire_sprite", 120, 120, "Bonfire")
    $ borner_sprite1 = MapUser(1, 2, "borner_sprite", 120, 120, "S")
    $ borner_sprite2 = MapUser(6, 2, "borner_sprite2", 120, 120, "S")
    $ borner_sprite3 = MapUser(25, 2, "borner_sprite", 120, 120, "S")
    $ borner_sprite4 = MapUser(27, 2, "borner_sprite2", 120, 120, "S")
    $ borner_sprite5 = MapUser(11, 4, "borner_sprite", 120, 120, "S")
    $ borner_sprite6 = MapUser(13, 4, "borner_sprite2", 120, 120, "S")
    $ borner_sprite7 = MapUser(15, 4, "borner_sprite", 120, 120, "S")
    $ borner_sprite8 = MapUser(30, 3, "borner_sprite2", 120, 120, "S")
    $ borner_sprite9 = MapUser(12, 9, "borner_sprite2", 120, 120, "S")
    $ borner_sprite10 = MapUser(16, 7, "borner_sprite2", 120, 120, "S")
    $ borner_sprite11 = MapUser(21, 10, "borner_sprite2", 120, 120, "S")
    $ borner_sprite14 = MapUser(5, 15, "borner_sprite", 120, 120, "S")
    $ borner_sprite15 = MapUser(12, 15, "borner_sprite2", 120, 120, "S")
    $ borner_sprite16 = MapUser(17, 17, "borner_sprite", 120, 120, "S")
    $ borner_sprite17 = MapUser(19, 17, "borner_sprite2", 120, 120, "S")

    $ btripwire_sprite1 = MapUser(22, 4, "tripwire_sprite1", 120, 120, "Tripwire1")
    $ btripwire_sprite2 = MapUser(22, 5, "tripwire_sprite", 120, 120, "Tripwire")
    $ btripwire_sprite3 = MapUser(22, 6, "tripwire_sprite", 120, 120, "Tripwire")
    $ btripwire_sprite4 = MapUser(22, 7, "tripwire_sprite", 120, 120, "Tripwire")

    $ bstairs_sprite1 = MapUser(6, 25, "bstairs1", 120, 120, "Exit")
    $ bstairs_sprite2 = MapUser(7, 25, "bstairs2", 120, 120, "Exit")
    $ bstairs_sprite3 = MapUser(12, 0, "bstairs1", 120, 120, "Floor2")
    $ bstairs_sprite4 = MapUser(12, 1, "bstairs1", 120, 120, "Floor2")
    $ bshelf_sprite1 = MapUser(21, 10, "bookshelf_sprite", 170, 165, "Bookshelf")
    $ bshelf_sprite2 = MapUser(13, 6, "bookshelf_sprite", 170, 165, "Bookshelf")
    $ btable_sprite1 = MapUser(17, 11, "btable_sprite1", 120, 165, "Table")
    $ btable_sprite2 = MapUser(3, 4, "btable_sprite1", 120, 165, "Table")
    $ btable_sprite3 = MapUser(27, 8, "btable_sprite2", 150, 180, "Table2")
    $ bdresser_sprite1 = MapUser(5, 3, "bdresser_sprite", 120, 170, "Dresser")
    $ debris_sprite1 = MapUser(12, 12, "debris_sprite1", 120, 120, "Debris")
    $ debris_sprite2 = MapUser(16, 7, "debris_sprite1", 120, 120, "Debris")
    $ bcabinet_sprite1 = MapUser(2, 15, "bcabinet_sprite", 120, 185, "Cabinet")
    $ bwine_sprite1 = MapUser(3, 16, "bwine_sprite2", 120, 120, "Wine")
    $ bwine_sprite5 = MapUser(17, 20, "bwine_sprite2", 120, 120, "Wine")
    $ bwine_sprite2 = MapUser(12, 15, "bwine_sprite1", 120, 120, "Wine")
    $ bwine_sprite3 = MapUser(15, 14, "bwine_sprite2", 120, 120, "Wine")
    $ bwine_sprite6 = MapUser(4, 3, "bwine_sprite2", 120, 120, "Wine")
    $ bwine_sprite4 = MapUser(30, 3, "bwine_sprite1", 120, 120, "Wine")
    $ bflag_sprite1 = MapUser(6, 21, "banditflag_sprite", 125, 120, "Flag")
    $ bflag_sprite2 = MapUser(1, 8, "banditflag_sprite", 125, 120, "Flag")
    $ bflag_sprite3 = MapUser(12, 20, "banditflag_sprite2", 120, 120, "Flag")
    $ bflag_sprite4 = MapUser(28, 5, "banditflag_sprite2", 120, 120, "Flag")
    $ bpainting_sprite1 = MapUser(19, 4, "bpainting_sprite1", 120, 230, "Painting")

    $ bchest_sprite1 = MapUser(18, 23, bchest_sprite_img, 120, 120, "Chest")


    $ addSprite(bandit_floor1, banditbed_sprite1)
    $ addSprite(bandit_floor1, banditbed_sprite2)
    $ addSprite(bandit_floor1, bonfire_sprite1)
    $ addSprite(bandit_floor1, bonfire_sprite2)
    $ addSprite(bandit_floor1, bchest_sprite1)
    $ addSprite(bandit_floor1, bandit_sprite1)
    $ addSprite(bandit_floor1, bandit_sprite2)
    $ addSprite(bandit_floor1, bandit_sprite3)
    $ addSprite(bandit_floor1, bandit_sprite4)
    $ addSprite(bandit_floor1, bandit_sprite5)
    $ addSprite(bandit_floor1, bandit_sprite6)
    $ addSprite(bandit_floor1, bandit_sprite7)
    $ addSprite(bandit_floor1, sprite)
    $ addSprite(bandit_floor1, bstairs_sprite1)
    $ addSprite(bandit_floor1, bstairs_sprite2)
    $ addSprite(bandit_floor1, bstairs_sprite3)
    $ addSprite(bandit_floor1, bstairs_sprite4)
    $ addBack(bandit_floor1, borner_sprite1)
    $ addBack(bandit_floor1, borner_sprite2)
    $ addBack(bandit_floor1, borner_sprite3)
    $ addBack(bandit_floor1, borner_sprite4)
    $ addBack(bandit_floor1, borner_sprite5)
    $ addBack(bandit_floor1, borner_sprite6)
    $ addBack(bandit_floor1, borner_sprite7)
    $ addBack(bandit_floor1, borner_sprite8)
    $ addBack(bandit_floor1, borner_sprite9)
    $ addBack(bandit_floor1, borner_sprite10)
    $ addBack(bandit_floor1, borner_sprite11)
    $ addBack(bandit_floor1, btripwire_sprite1)
    $ addBack(bandit_floor1, btripwire_sprite2)
    $ addBack(bandit_floor1, btripwire_sprite3)
    $ addBack(bandit_floor1, btripwire_sprite4)
    $ addBack(bandit_floor1, borner_sprite14)
    $ addBack(bandit_floor1, borner_sprite15)
    $ addBack(bandit_floor1, borner_sprite16)
    $ addBack(bandit_floor1, borner_sprite17)
    $ addSprite(bandit_floor1, bshelf_sprite1)
    $ addSprite(bandit_floor1, bshelf_sprite2)
    $ addSprite(bandit_floor1, btable_sprite1)
    $ addSprite(bandit_floor1, bdresser_sprite1)
    $ addBack(bandit_floor1, debris_sprite1)
    $ addBack(bandit_floor1, debris_sprite2)
    $ addSprite(bandit_floor1, bcabinet_sprite1)
    $ addBack(bandit_floor1, bwine_sprite1)
    $ addBack(bandit_floor1, bwine_sprite2)
    $ addBack(bandit_floor1, bwine_sprite3)
    $ addBack(bandit_floor1, bwine_sprite4)
    $ addBack(bandit_floor1, bwine_sprite5)
    $ addBack(bandit_floor1, bwine_sprite6)
    $ addSprite(bandit_floor1, btable_sprite2)
    $ addSprite(bandit_floor1, btable_sprite3)
    $ addBack(bandit_floor1, bflag_sprite1)
    $ addBack(bandit_floor1, bflag_sprite2)
    $ addBack(bandit_floor1, bflag_sprite3)
    $ addBack(bandit_floor1, bflag_sprite4)
    $ addBack(bandit_floor1, bpainting_sprite1)
    $ dungeon_timers = []
    $ bandit_floor1.autoMoveLookers()

    hide screen menu_buttons
    $ bandit_floor1.entranceCount += 1
    jump Bandits_Hideout_Loop

label Bandits_Hideout_Loop:

    show screen dungeon_buttons
    $ disableC = False
    $ sprite = tenki_sprite11
    call screen dungeon_map(bandit_floor1)
    if isinstance(_return, tuple):
        $ dungeon_timers.pop(0)
        $ bandit_floor1.autoMoveLookers()

    if bandit_floor1.mappy[sprite.y][sprite.x].back != None and (bandit_floor1.mappy[sprite.y][sprite.x].back.img == "tripwire_sprite" or bandit_floor1.mappy[sprite.y][sprite.x].back.img == "tripwire_sprite1"):
        if btripwire_sprite1.img == "tripwire_sprite1":
            $ disableC = True
            show screen dungeon_map(bandit_floor1)
            "You step on the wire right on the floor, making a loud chime sound from the device."
            jump Bandit_Encounter_Bandit

    if enct == "Bandit":
        if pc.armor["Mask"] != None and pc.armor["Mask"].img == "Bandit Hood":
            $ enct = None
        else:
            $ disableC = True
            show screen dungeon_map(bandit_floor1)
            $ enct = None
            bd "Ha, caught cha sneaking right here!"

            jump Bandit_Encounter_Bandit

    if _return == "Tripwire1":
        if btripwire_sprite1.img == "tripwire_sprite1":
            $ disableC = True
            show screen dungeon_map(bandit_floor1)
            "You work on the tripwire, disabling it from making any loud noise."
            $ btripwire_sprite1.img = "tripwire_sprite2"

    if _return == "Exit":
        $ disableC = True
        show screen dungeon_map(bandit_floor1)
        menu:
            "Do you wish to exit the bandit's hideout?"
            "Yes":
                call Leaving_Bandits_Hideout from _call_Leaving_Bandits_Hideout_2
                jump main_bandits_hideout
            "No":
                pass

    if _return == "Bandit":
        $ disableC = True
        show screen dungeon_map(bandit_floor1)
        $ enct = None
        if pc.armor["Mask"] != None and pc.armor["Mask"].img == "Bandit Hood":
            bd "Fella, what cha doing here? Go guard outside or raid a house with the rest of us."
            e "A-aye!"
        else:
            bd "Ha, caught cha sneaking right here!"
            jump Bandit_Encounter_Bandit
    if _return == "Dresser":
        $ disableC = True
        show screen dungeon_map(bandit_floor1)
        "You take a look at the mirror, it is too foggy for you to see your own image."
        if callInventoryItem("Songweaver Breeches", "Pants"):
            "Searching around the dresser, you found a dusty piece of clothing."
            "It's only after patting away some of the dust, you discovered that it's a pair of colourful pants, something that a famous bard may wear..."
            "Without a second thought, you put the piece of garment into your bag."
            $ addItem("Songweaver Breeches", inventory, 1)
        else:
            "Searching around the dresser leaves nothing important. Only a few rusty coins here and there."
            "With a few old notes, coming from the bandit's gibberish."

    if _return == "Bookshelf":
        $ disableC = True
        show screen dungeon_map(bandit_floor1)
        "You take a gander around the bookshelf, it's all old books with a wide variety of colours."
        "Doesn't seem it's been used at all."

    if _return == "Cabinet":
        $ disableC = True
        show screen dungeon_map(bandit_floor1)
        "You open the cabinet, it seems to be mostly empty. Some of them can't even be opened properly."

    if _return == "Table2":
        $ disableC = True
        show screen dungeon_map(bandit_floor1)
        "There were a little food, some treasures and shiny loot scattered across the table."

    if _return == "Table":
        $ disableC = True
        show screen dungeon_map(bandit_floor1)
        "Books, and some pen and pencils can be seen on this table, but there's no chair. Do the bandits never sit down?"

    if _return == "BanditBed":
        $ disableC = True
        show screen dungeon_map(bandit_floor1)
        "You stare at the empty bed, it seems to be owned by a rather hefty man, with the way these frames bend down."
        "The worst is, you can still smell the heavy sweaty scent, one that is rather fishy..."

    if _return == "BanditBedShark":
        $ disableC = True
        show screen dungeon_map(bandit_floor1)
        "You see the bandit boss sitting on the bed casually, loudly munching on the apple or plum on his hand."
        if pc.armor["Mask"] != None and pc.armor["Mask"].img == "Bandit Hood":
            sbd "What are you looking at?"
            sbd "Get back to work, or bring me my plums. We need some more gold otherwise."
        elif isBandit:
            if callInventoryItem("Bandit Hood", "Mask"):
                sbd "What are you looking at?"
                e "Uh..."
                sbd "Ugh, I remembered you, you should be out of training by now, where's your hood?"
                e "Hood? I didn't get a hood, boss."
                sbd "Fine."
                sbd "Hey! Come here."
                bd "What's it, boss?"
                sbd "How did the newcomer not get a hood?"
                if bandit_gangbanged > 0:
                    bd "Wait, did we not just banged his as-"
                    bd "I think we must have mistaken something..."
                    sbd "What?"
                    bd "I'll get him a hood, sorry boss."
                else:
                    bd "Uh newcomer? I've never seen him before"
                    sbd "I don't want to hear any excuses, now get him a hood."
                    bd "Y-yes, boss."
                "The bandit quickly grabs a hood and brings it to you."
                bd "Well, put it on if you don't want us to mistake you as an adventurer."
                $ addItem("Bandit Hood", inventory, 1)

            elif pc.armor["Mask"] != None and pc.armor["Mask"].img == "Bandit Hood":
                sbd "What are you looking at?"
                sbd "Get back to work, or bring me my plums. We need some more gold otherwise."
            else:
                sbd "What are you looking at?"
                sbd "And where's your hood? Didn't we just gave you one?"
        else:

            sbd "Hey! Who the fuck are you?"
            e "I- I was just walking by..."
            sbd "How dare you walking up to me like nothing happened."
            sbd "Ugh... pesky adventurer. My men will catch you one way or the other. Start running now."
            e "Are you... not going to do anything?"
            sbd "Trust me, you don't want me to be the one catching you, adventurer. Now let me finish my plum in peace."


    if _return == "Chest":
        if bchest_sprite_img == "bchest_sprite1" or quest35.status == 2:
            $ disableC = True
            $ book_page = 0
            $ bchest_sprite_img = "bchest_sprite2"
            $ bchest_sprite1.img = bchest_sprite_img
            show screen dungeon_map(bandit_floor1)
            "You open the chest, it contains a few stolen goods, there's no prose inside, but you found an accounting journal..."
            $ bandit_accounting_journal01 = Page("Day 1214\nAin't we just the luckiest sons of benches? We've been robbin' folks left and right, and our coffers are brimming with shiny bits and bobs. Here's what we've got to show for it:\n\n10 flowin' robes of silk. We'll probably sell these to some rich fool in the city who's willing to pay through the nose for some fancy cloth.\nA roll of paper, Looka told us it's an old poem about some hero and monster, forgot what he said. We took it from that bard who's been making noise outside, should fetch a good price with it.\nThink we've got like, whole lotta gold tradin some goods, Buck's gonna get us some good wine today.","Day 1215\nWe had ourselves a real good time the other night. We got drunk on wine and told stories of our exploits. \nSpeaking of selling things, we managed to offload that piece of paper from the bard to a fence we know in the village. Got a good price for it too. 3000 gold right in our pocket.\n\nWe took some other stuff also:\n25 pieces of iron ore, think some werewolves came out of nowhere and delivered them right at our doorstep.\n1 magical wand, swiped from a traveling wizard. We're not sure what to do with this yet, so we'll hold on to it for a bit.", 1)
            $ bandit_accounting_journal01.addTo(bandit_accounting_journal)
            show screen book_read(bandit_accounting_journal)
            "You flip over the pages, and something caught your eyes in one page."
            "It reads... that the bandit stole the prose from the bard?"
            "And in the next day, they sold it to someone in the village, you wonder what that means."
            "But regardless, it's not in the bandit's hand anymore, you should probably just go back to Pirkka and ask what he should do next."
            if quest35.status != False:
                $ quest35.qComp(_("Report back to Pirkka"))
                $ quest35.status = 2.5
            hide screen book_read
        else:
            $ disableC = True
            show screen dungeon_map(bandit_floor1)
            "The chest has been opened, but you intend to check the journal again."
            call screen book_read(bandit_accounting_journal)



    jump Bandits_Hideout_Loop
default bandit_accounting_journal = Book(_("{i}Loots and Lays{/i}"),"bandit_accounting_journal", "Book_Bandit_Accounting_Journal")

label Bandit_Encounter_Bandit:

    hide screen dungeon_map
    scene bandit_floor1 with dissolve
    "A bandit exclaims when he catches you."
    "You have to do something right now, else the other bandits are just going to come here..."
    menu:
        "What should you do now?"
        "Escape with Agility":
            "You try to slip away from the bandit."
            bd "This is our territory, boy. You're not getting away with this."
            if pc.agi > renpy.random.randint(1,5):
                "You barely escape from the masked man's grasp."
                bd "H-hey! Come back here."
                "Not listening to him, you sprint quickly towards the exit of the fortress."
                "And finally, you arrive to a safer place with all your energy exhausted."
                call Leaving_Bandits_Hideout from _call_Leaving_Bandits_Hideout
                jump main_bandits_hideout
            else:
                "Suddenly, the bandit grips your tail easily."
                e "F-fuck!"
                "You fall face first on the floor, dragged towards the bandit, who's laughing hysterically."
                bd "Hah, what a dumbass, come back here, won't ya."
        "Surrender":
            e "Alright, I give up. Please just take my coins."
            "The bandit smirks, he drags you towards him, checking you out with a sinister look."
            bd "Well, at least you're smart knowing you can't escape from us."
    $ bandit_gangbanged += 1
    hide screen menu_buttons 
    call Scene_Bandit_Gangbang from _call_Scene_Bandit_Gangbang
    $ pc.lust = 0
    if bandit_gangbanged + bandit.lose >= 3:
        if pc.cor < 85:
            jump BadEnd_Bandit_Bondage
        else:
            "For some reason, the bandits releases you from their camp, perhaps they still have a little conscience towards someone... as {i}pure{/i} as you."
    call Leaving_Bandits_Hideout from _call_Leaving_Bandits_Hideout_1
    $ lost_gold = int(pc.gold*0.3*renpy.random.random() + renpy.random.random()*25 + 25)
    $ pc.gold -= lost_gold

    scene bandits_hideout
    "And when you wake up from the darkness, you're already out of the bandit's hideouts."
    "Apparently they've decided to let you go, you are so wasted from these few hours serving those bandits."
    "You can't imagine what a lifetime of being used for pleasure would feel like, not that you'd want to know."
    "But at least, you're spared of your freedom, for now."
    if pc.gold <= 0:
        $ pc.gold = 0
    "You lost [lost_gold] gold."
    jump main_bandits_hideout

label Leaving_Bandits_Hideout:
    hide screen dungeon_map
    hide screen dungeon_buttons
    $ removeSprite(bandit_floor1, sprite)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
