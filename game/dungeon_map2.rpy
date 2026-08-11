default d2x = 14
default d2y = 34
image mino_sprite0:
    "mino_sprite"
    pause 1.25
    "mino_sprite2"
    pause 0.75
    repeat

label Minotaur_Maze_Enter:
    $ dungeon_timers = []
    if maze_enter == 0:
        "There is a mountainous presence in the middle of the chamber that you can't ignore."
        "Sensing your presence, the creature whips its head at you."
        "It charges and slams into an invisible wall. After calming down from fear, you examine the area around the minotaur closer."
        "There seems to be a runic zone that keeps the creature in."
        "Unable to grab you, the minotaur roars. The chamber trembles but you hear no sound. The imprisonment runes appear to keep the sound inside the zone as well."
        "The minotaur grunts and seems to withers slightly. You believe it grumbled something but due to the runic prison, you can't hear anything."
        "In any case, you remember your mission. It is to draw the Minotaur's essence."
        "The first step will be to take down the runic prison to approach the minotaur."
        "That will mean exposing yourself to its aggression. You do not like the prospect of that but for the mission, you steel yourself."
    $ maze_enter += 1
    $ agi_numb = 0
    $ ms = MapUser(0, 0, "mist_sprite", 120, 120, "Mist")
    $ dungeon2_map = [
        [MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_side")), MapTile(), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(back = ms), MapTile(back = ms), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(back = ms), MapTile(back = ms), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(MapThing("bush_side")), MapTile(), MapTile(MapThing("bush_side")), MapTile(back = ms), MapTile(back = ms), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(),  MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(back = ms), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(back = ms), MapTile(back = ms), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(), MapTile(), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")),  MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top")), MapTile(MapThing("bush_top"))],
        [MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side")), MapTile(MapThing("bush_side"))]
    ]
    $ d2x = 14
    $ d2y = 34
    $ step = 0
    hide screen menu_buttons
    show screen dungeon_buttons
    $ mino_maze = MapPat(dungeon2_map, "Minotaur Maze", d2x, d2y, "grass")
    $ mino_maze.playerSprite = MapUser(14, 34, "e_dungeon", 120, 120, no_op)
    $ mino_sprite = MapUser(14, 18, "mino_sprite0", 120, 170, "Mino")
    $ pebble_sprite = MapUser(22, 19, "pebble_sprite1", 120, 120, "Pebble")
    $ pebble_sprite2 = MapUser(26, 19, "pebble_sprite2", 120, 120, "Pebble")
    $ pebble_sprite3 = MapUser(23, 10, "pebble_sprite2", 120, 120, "Pebble")
    $ pebble_sprite4 = MapUser(25, 10, "pebble_sprite1", 120, 120, "Pebble")
    $ minoRock_sprite1 = MapUser(25, 33, "rocky_sprite", 120, 120, "minoRock")
    $ pebble_sprite6 = MapUser(9, 32, "pebble_sprite1", 120, 120, "Pebble")
    $ pebble_sprite7 = MapUser(8, 6, "pebble_sprite1", 120, 120, "Pebble")
    $ pebble_sprite8 = MapUser(13, 4, "pebble_sprite1", 120, 120, "Pebble")
    $ sandstone_sprite = MapUser(21, 7, "sandstone_sprite", 120, 120, "Sandstone")
    $ sandstone_sprite3 = MapUser(12, 7, "sandstone_sprite", 120, 120, "Sandstone")
    $ sandstone_sprite2 = MapUser(27, 7, "sandstone_sprite2", 120, 120, "Sandstone")
    $ sandstone_sprite4 = MapUser(7, 17, "sandstone_sprite", 120, 120, "Sandstone")
    $ barrier_sprite = MapUser(14, 19, "barrier_sprite", 120, 120, "Barrier")
    $ barrier_sprite2 = MapUser(15, 19, "barrier_sprite", 120, 120, "Barrier")
    $ barrier_sprite3 = MapUser(14, 20, "barrier_sprite2", 120, 120, "Barrier")
    $ barrier_sprite4 = MapUser(15, 20, "barrier_sprite2", 120, 120, "Barrier")
    $ pyramid_sprite = MapUser(24, 16, "pyramid_sprite", 120, 120, "Pyramid")
    $ pyramid_sprite2 = MapUser(17, 7, "pyramid_sprite", 120, 120, "Pyramid")
    $ crater_sprite = MapUser(20, 6, "crater_sprite", 120, 120, "Crater1")
    $ crater_sprite2 = MapUser(28, 6, "crater_sprite2", 120, 120, "Crater2")
    $ figurineincrater_sprite = MapUser(20, 6, "figurineincrater_sprite", 120, 120, "FCrater1")
    $ figurineincrater_sprite2 = MapUser(28, 6, "figurineincrater_sprite2", 120, 120, "WFCrater1")
    $ figurineincrater_sprite3 = MapUser(28, 6, "figurineincrater_sprite3", 120, 120, "FCrater2")
    $ figurineincrater_sprite4 = MapUser(20, 6, "figurineincrater_sprite4", 120, 120, "WFCrater2")
    $ figurine_sprite = MapUser(13, 2, "figurine_sprite2", 120, 120, "Figurine")
    $ figurineincrater_sprite5 = MapUser(20, 11, "figurineincrater_sprite", 120, 120, "FCrater3")
    $ figurineincrater_sprite6 = MapUser(28, 11, "figurineincrater_sprite2", 120, 120, "FCrater4")
    $ agifigurine_sprite = MapUser(20, 33, "agifigurine_sprite", 120, 160, "AgiFigurine")
    $ agistand_sprite = MapUser(28, 25, "agistand_sprite", 120, 120, "AgiStand")
    $ figurineonstand_sprite = MapUser(28, 25, "figurineonstand_sprite", 120, 170, "FigurineOnStand")
    $ figurineonstand_sprite2 = MapUser(28, 25, "figurineonstand_sprite2", 120, 170, "FigurineOnStand2")
    $ figurineonpebble_sprite = MapUser(25, 33, "agionrock_sprite", 120, 170, "FigurineOnPebble")
    $ intfigurine_sprite = MapUser(2, 4, "intfigurine_sprite", 120, 120, "IntFigurine")
    $ intfigurine_sprite2 = MapUser(4, 5, "intfigurine_sprite", 120, 120, "IntFigurine")
    $ intfigurine_sprite3 = MapUser(3, 2, "intfigurine_sprite2", 120, 120, "IntFigurine2")
    $ intfigurine_sprite4 = MapUser(2, 4, "intfigurine_sprite2", 120, 120, "IntFigurine2")
    $ tenfigurine_sprite = MapUser(2, 15, "tenfigurine_sprite", 180, 170, "TenF1")
    $ tenfigurine_sprite2 = MapUser(3, 11, "tenfigurine_sprite", 180, 170, "TenF2")
    $ tenfigurine_sprite3 = MapUser(2, 15, "tenfigurine_sprite2", 180, 170, "TenF3")
    $ tenfigurine_sprite4 = MapUser(3, 11, "tenfigurine_sprite2", 180, 170, "TenF3")
    $ minoleave_sprite = MapUser(15, 34, "minoleave_sprite", 120, 120, "Leave")
    $ intrune_sprite = MapUser(3, 2, "intrune_sprite", 120, 120, "IntRune")
    $ intrune_sprite2 = MapUser(2, 4, "intrune_sprite", 120, 120, "IntRune")
    $ chafigurine_sprite = MapUser(5, 31, "chafigurine_sprite", 120, 170, "ChaFigurine")
    $ chafigurine_sprite2 = MapUser(5, 31, "chafigurine_sprite2", 120, 170, "ChaFigurine2")
    $ scripture_sprite = MapUser(14, 27, "scripture_sprite", 120, 120, "Scripture")
    $ str_sprite = MapUser(24, 13, "str_sprite", 120, 120, "Str")
    $ str_sprite2 = MapUser(24, 13, "str_sprite2", 120, 120, "Str2")
    $ agi_sprite = MapUser(28, 26, "agi_sprite", 120, 120, "Agi")
    $ agi_sprite2 = MapUser(28, 26, "agi_sprite2", 120, 120, "Agi2")
    $ int_sprite = MapUser(9, 3, "int_sprite", 120, 120, "Int")
    $ int_sprite2 = MapUser(9, 3, "int_sprite2", 120, 120, "Int2")
    $ ten_sprite = MapUser(3, 20, "ten_sprite", 120, 120, "Ten")
    $ ten_sprite2 = MapUser(3, 20, "ten_sprite2", 120, 120, "Ten2")
    $ cha_sprite = MapUser(2, 33, "cha_sprite", 120, 120, "Cha")
    $ cha_sprite2 = MapUser(2, 33, "cha_sprite2", 120, 120, "Cha2")
    $ addSprite(mino_maze, mino_maze.playerSprite)
    $ addSprite(mino_maze, mino_sprite)
    $ addSprite(mino_maze, pebble_sprite)
    $ addSprite(mino_maze, pebble_sprite2)
    $ addSprite(mino_maze, pebble_sprite3)
    $ addSprite(mino_maze, pebble_sprite4)
    $ addSprite(mino_maze, minoRock_sprite1)
    $ addSprite(mino_maze, pebble_sprite6)
    $ addSprite(mino_maze, pebble_sprite7)
    $ addSprite(mino_maze, pebble_sprite8)
    $ addSprite(mino_maze, barrier_sprite)
    $ addSprite(mino_maze, barrier_sprite2)
    $ addSprite(mino_maze, barrier_sprite3)
    $ addSprite(mino_maze, barrier_sprite4)
    $ addSprite(mino_maze, limestone_sprite1)
    $ addSprite(mino_maze, limestone_sprite2)
    $ addSprite(mino_maze, limestone_sprite3)
    $ addSprite(mino_maze, limestone_sprite4)
    $ addSprite(mino_maze, limestone_sprite5)
    $ addSprite(mino_maze, sandstone_sprite)
    $ addSprite(mino_maze, sandstone_sprite2)
    $ addSprite(mino_maze, sandstone_sprite3)
    $ addSprite(mino_maze, sandstone_sprite4)
    $ addSprite(mino_maze, pyramid_sprite)
    $ addSprite(mino_maze, pyramid_sprite2)
    $ addSprite(mino_maze, crater_sprite)
    $ addSprite(mino_maze, figurineincrater_sprite3)
    $ addSprite(mino_maze, figurine_sprite)
    $ addSprite(mino_maze, figurineincrater_sprite5)
    $ addSprite(mino_maze, figurineincrater_sprite6)
    $ addSprite(mino_maze, agifigurine_sprite)
    $ addSprite(mino_maze, agistand_sprite)
    $ addSprite(mino_maze, intfigurine_sprite)
    $ addSprite(mino_maze, intfigurine_sprite2)
    $ addSprite(mino_maze, tenfigurine_sprite)
    $ addSprite(mino_maze, tenfigurine_sprite2)
    $ addBack(mino_maze, intrune_sprite)
    $ addBack(mino_maze, intrune_sprite2)
    $ addSprite(mino_maze, chafigurine_sprite)
    $ addSprite(mino_maze, scripture_sprite)
    $ addSprite(mino_maze, str_sprite)
    $ addSprite(mino_maze, agi_sprite)
    $ addSprite(mino_maze, int_sprite)
    $ addSprite(mino_maze, ten_sprite)
    $ addSprite(mino_maze, cha_sprite)
    $ addSprite(mino_maze, minoleave_sprite)
    $ crater_num = 1
    $ has_figurineL = False
    $ has_figurineR = False
    $ has_agifigurine = False

    $ agi_num = 0
    $ ten_num = 0
    $ disableC = False
    $ gem_thing = 5
    $ current_location = mino_maze
    jump Minotaur_Maze_Loop

label Minotaur_Maze_Loop:
    $ disableC = False
    $ sprite = mino_maze.playerSprite
    show screen dungeon_buttons
    call screen dungeon_map(mino_maze)
    $ disableC = True
    if _return == "Sandstone":
        show screen dungeon_map(mino_maze)
        "You look at the sandstone... it seems to be made of sand... and stone, no... you've heard it's actually silicates."
    if _return == "Pyramid":
        show screen dungeon_map(mino_maze)
        "A small sand pyramid, there's nothing out of the ordinary except that it is horizontally symmetric."
    if _return == "Pebble":
        $ disableC = True
        show screen dungeon_map(mino_maze)

        "Some pebbles on the ground, and grasses. shouldn't be too common outside of the cave."
    if _return == "minoRock":
        show screen dungeon_map(mino_maze)
        if has_agifigurine and step - agi_num - 18 - pc.agi + agi_numb < 0:
            "The surface of this rock is pretty flat, maybe you can balance the statue on it..."
            menu:
                "Do you want to put it down?"
                "Yes{#putdownstatue}":

                    $ has_agifigurine = False
                    $ agi_numb = step - agi_num
                    $ mino_maze.unoccupy(25, 33)
                    $ addSprite(mino_maze, figurineonpebble_sprite)
                "No{#putdownstatue}":
                    pass
        else:
            "The rock looks flat, and there is a minotaur symbol at the center."
    if _return == "Mino":

        show screen dungeon_map(mino_maze)
        "You look at the Minotaur... he seems to be imprisoned in the magical bind."
        $ disableC = True
        menu:
            "Do you want to fight with the minotaur?"
            "Yes{#minofight}":

                "He seems to sense your scent in front of you. Suddenly, the binds snapped and detached from the wall."
                $ e_d = "front"
                pause 1
                $ addSprite(mino_maze, barrier_sprite3)
                $ addSprite(mino_maze, barrier_sprite4)
                pause 1
                $ e_d = "back"
                "The magically barrier reappear before your eyes, you cannot escape now..."
                scene black
                with dissolve
                pause 1.0
                scene mino_cave
                with dissolve
                "The minotaur stares at you... angrily. He holds the binds in front of you."
                mn "M-master...?"
                "You don't know what he is talking about... you stands here, readying your weapon."
                "This only made the minotaur more angry..."
                jump mino_battle
            "No{#minofight}":
                pass
    if _return == "Leave":
        show screen dungeon_map(mino_maze)
        $ disableC = True
        menu:
            "Do you want to leave the dungeon? Progress will be reset when you return."
            "Yes{#leaveminomaze}":
                $ removeSprite(mino_maze, mino_maze.playerSprite)
                hide screen dungeon_map
                hide screen dungeon_buttons

                jump main_gloomy_mountainside
            "No{#leaveminomaze}":
                pass
    if _return == "FigurineOnPebble":
        show screen dungeon_map(mino_maze)
        $ disableC = True
        menu:
            "Do you want to carry the statue?"
            "Yes{#carrystatue}":
                $ agi_num = step
                $ has_agifigurine = True
                $ mino_maze.unoccupy(25, 33)
                $ addSprite(mino_maze, minoRock_sprite1)
            "No{#carrystatue}":
                pass

    if _return == "Limestone1":
        $ mimic_num = 1
        jump Minotaur_Maze_Limestone
    if _return == "Limestone2":
        $ mimic_num = 2
        jump Minotaur_Maze_Limestone
    if _return == "Limestone3":
        $ mimic_num = 3
        jump Minotaur_Maze_Limestone
    if _return == "Limestone4":
        $ mimic_num = 4
        jump Minotaur_Maze_Limestone
    if _return == "Limestone5":
        $ mimic_num = 5
        jump Minotaur_Maze_Limestone
    if _return == "Barrier":
        show screen dungeon_map(mino_maze)
        $ disableC = True
        if gem_thing == 0:
            "As the five gems are activated, the magical barrier soon ceases its light in front of you."
            $ mino_maze.unoccupy(14, 19)
            $ mino_maze.unoccupy(14, 20)
            $ mino_maze.unoccupy(15, 19)
            $ mino_maze.unoccupy(15, 20)
        else:

            "A strong barrier barricading you from the minotaur inside..."
            "It seems to be controlled by the gems scattered at different section of the cave, maybe you need to activate them first."
            if quest14.status == True:
                menu:
                    "As you have knowledge of the past, do you wish to break the barrier?"
                    "Yes{#breakminobarrier}":
                        $ mino_maze.unoccupy(14, 19)
                        $ mino_maze.unoccupy(14, 20)
                        $ mino_maze.unoccupy(15, 19)
                        $ mino_maze.unoccupy(15, 20)
                    "No{#breakminobarrier}":
                        pass

    if _return == "FCrater3" or _return == "FCrater4":
        $ disableC = True
        show screen dungeon_map(mino_maze)
        "You look at the tiny statue of a minotaur, it seems to be flexing its muscles."
        "You try to pull it out of the crater on the ground, but it seems to be stuck."
        "Maybe it's not to be moved..."
    if _return == "Figurine":
        $ disableC = True
        show screen dungeon_map(mino_maze)
        "You look at the tiny statue of a minotaur, it seems to be flexing its muscles towards its right."
        menu:
            "Should you take it?"
            "Yes{#takestatue}":
                $ has_figurineR = True
                $ mino_maze.unoccupy(13, 2)
            "No{#takestatue}":
                pass
    if _return == "Str":
        $ disableC = True
        show screen dungeon_map(mino_maze)

        if mino_maze.mappy[6][20].user.img == "figurineincrater_sprite" and mino_maze.mappy[6][28].user.img == "figurineincrater_sprite2":
            "As soon as you touch the gem. It instantly convulses."
            "The gem seems to react to your placement of statue."
            "In a few seconds, the gem glows in bright red."
            "You can tell that the barrier at the center of the cave has been weakened."
            $ gem_thing -= 1
            $ mino_maze.unoccupy(24, 13)
            $ addSprite(mino_maze, str_sprite2)
        else:
            "There is a red gem on the pillar, it seems to be emanating dim light."
            "You feel like you need to do something here to make it glow."
            if pc.stg >= 6:
                "It comes to you that... maybe there's something to do with the statue."
                "The balance... must be restored. You begin to think how you can fill in the craters."

    if _return == "Str2":
        $ disableC = True
        show screen dungeon_map(mino_maze)
        "The gem is glowing in bright red. You feel that this zone has been completed."
    if _return == "Int":
        $ disableC = True
        show screen dungeon_map(mino_maze)
        if mino_maze.mappy[2][3].user != None and mino_maze.mappy[4][2].user != None:
            if mino_maze.mappy[2][3].user.img == "intfigurine_sprite" and mino_maze.mappy[4][2].user.img == "intfigurine_sprite":
                "As soon as you touch the gem. It instantly convulses."
                "The gem seems to react to your placement of statue."
                "In a few seconds, the gem glows in bright blue."
                "You can tell that the barrier at the center of the cave has been weakened."
                $ gem_thing -= 1
                $ mino_maze.unoccupy(9, 3)
                $ addSprite(mino_maze, int_sprite2)
                $ mino_maze.unoccupy(2, 4)
                $ mino_maze.unoccupy(3, 2)
                $ addSprite(mino_maze, intfigurine_sprite3)
                $ addSprite(mino_maze, intfigurine_sprite4)
                jump Minotaur_Maze_Loop
            else:
                pass
        else:
            pass
        "There is a blue gem on the pillar, it seems to be emanating dim light."
        "You feel like you need to do something here to make it glow."
        menu:
            "Do you want to reset?"
            "Get a Hint (Int > 5)" if pc.itg > 5:
                $ mino_maze.clearUser("intfigurine_sprite")
                $ mino_maze.occupy(2, 4, intfigurine_sprite)
                $ mino_maze.occupy(4, 4, intfigurine_sprite2)
            "Yes{#resetminopuzzle}":


                $ mino_maze.clearUser("intfigurine_sprite")
                $ mino_maze.occupy(2, 4, intfigurine_sprite)
                $ mino_maze.occupy(4, 5, intfigurine_sprite2)
            "No{#resetminopuzzle}":
                pass
    if _return == "Ten":
        $ disableC = True
        show screen dungeon_map(mino_maze)
        if mino_maze.mappy[11][3].user.img == "tenfigurine_sprite2" and mino_maze.mappy[15][2].user.img == "tenfigurine_sprite2":
            "As soon as you touch the gem. It instantly convulses."
            "The gem seems to react to your battle with the statues."
            "In a few seconds, the gem glows in bright green."
            "You can tell that the barrier at the center of the cave has been weakened."
            "Your health has also been replenished."
            $ pc.sleep()
            $ gem_thing -= 1
            $ mino_maze.unoccupy(3, 20)
            $ addSprite(mino_maze, ten_sprite2)
            jump Minotaur_Maze_Loop
        else:
            "There is a green gem on the pillar, it seems to be emanating dim light."
            "You feel like you need to do something here to make it glow."
    if _return == "Ten2":
        $ disableC = True
        show screen dungeon_map(mino_maze)
        "The gem is glowing in bright green. You feel that this zone has been completed."
    if _return == "Int2":
        $ disableC = True
        show screen dungeon_map(mino_maze)
        "The gem is glowing in bright blue. You feel that this zone has been completed."
    if _return == "IntFigurine":
        $ disableC = True
        show screen dungeon_map(mino_maze)
        "You look at the statue of minotaur, it seems to be pondering something..."
        "Surprisingly, it is extremely light, but you cannot lift it up."
        "Maybe you can push it around."
    if _return == "Scripture":
        $ disableC = True
        show screen dungeon_map(mino_maze)
        "You notice the writing on the wall of stone in front of you..."
        "When you investigate on these words, you realise it is a riddle... or poem."
        "The riddle reads..."
        "'O, Fearless, Intrepid Challenger. Standing in the Dungeon of the Mythical Creature.'"
        "'In order to remove the Barrier, Five tests of attributes he must clear. '"
        pause 1
        "'A Test of Strength, a Case of Symmetry.'"
        "'Restore the Balance, Solve the Mystery.'"
        pause 1
        "'A Test of Agility, a Delivery of the Creature's Mold.'"
        "'Watch your foothold for with every step, Death Tolls.'"
        pause 1
        "'A Test of Charisma, Yet a Trial It is Not to be.'"
        "'A record of the Creature's History. An Act of Charity to Thee.'"
        pause 1
        "'A Test of Tenacity, a Challenge for he to Toil and Suffer.'"
        "'A cue for Dangerous Encounters. To proceed, he must appear the Victor.'"
        pause 1
        "'A Test of Intelligence, a Puzzle, a Ritual Interrupted.'"
        "'The Casts' Placement be Corrected. The Runes thus Activated.'"
        pause 1
        "'Five Tests if proved Trifling, The barrier He Shall see Weakening.'"
        "'The beast, the bull, the man is awaiting.'"
        pause 1
        "'A reward or a penalty?'"
        "'Either a bull's spirit shall bent or remain unchallenged in victory."
        "..."

    if _return == "IntFigurine2":
        $ disableC = True
        show screen dungeon_map(mino_maze)
        "You look at the statue of minotaur, it seems to be pondering something..."
        "The weight of the statue grows heavier as it glows bright blue."
    if _return == "AgiFigurine":
        $ disableC = True
        show screen dungeon_map(mino_maze)
        "You look at the statue of minotaur, it seems to be ready to run..."
        "With the material it is made of, you feel like it is about to crumble..."
        menu:
            "Do you want to carry the statue?"
            "Yes{#carryagistatue}":
                $ has_agifigurine = True
                $ agi_num = step
                $ agi_numb = 0
                $ mino_maze.unoccupy(20, 33)
            "No{#carryagistatue}":
                pass
    if _return == "AgiStand":
        $ disableC = True
        show screen dungeon_map(mino_maze)
        if has_agifigurine and step - agi_num - 18 - pc.agi + agi_numb < 0:
            "You feel like you need to put something here..."
            menu:
                "Do you want to put the statue here?"
                "Yes{#putdownagistatue}":
                    $ has_agifigurine = False
                    $ mino_maze.unoccupy(28, 25)
                    $ addSprite(mino_maze, figurineonstand_sprite)
                "No{#putdownagistatue}":
                    pass
        else:
            "You feel like you need to put something here..."
    if _return == "Agi":
        $ disableC = True
        show screen dungeon_map(mino_maze)
        if mino_maze.mappy[25][28].user.img == "figurineonstand_sprite":

            "As soon as you touch the gem. It instantly convulses."
            "The gem seems to react to your placement of statue."
            "In a few seconds, the gem glows in bright yellow."
            "You can tell that the barrier at the center of the cave has been weakened."
            $ gem_thing -= 1
            $ mino_maze.unoccupy(28, 26)
            $ mino_maze.unoccupy(28, 25)
            $ addSprite(mino_maze, agi_sprite2)
            $ addSprite(mino_maze, figurineonstand_sprite2)
            jump Minotaur_Maze_Loop
        else:
            "There is a yellow gem on the pillar, it seems to be emanating dim light."
            "You feel like you need to do something here to make it glow."
        menu:
            "Do you want to reset?"
            "Yes{#resetagistatue}":

                $ agi_num = 0
                $ has_agifigurine = False
                $ mino_maze.occupy(20, 33, agifigurine_sprite)
            "No{#resetagistatue}":
                pass
    if _return == "TenF1":
        $ disableC = True
        $ ten_num = 1
        jump Minotaur_Maze_TenStatue
    if _return == "TenF2":
        $ disableC = True
        $ ten_num = 2
        jump Minotaur_Maze_TenStatue

    if _return == "Cha":
        $ disableC = True
        show screen dungeon_map(mino_maze)
        "There is a pink gem on the pillar, it seems to be emanating dim light."
        "You feel like you need to do something here to make it glow."
    if _return == "ChaFigurine2":
        $ disableC = True
        show screen dungeon_map(mino_maze)
        "You look at the statue of minotaur, it seems to be grasping at its chest..."
    if _return == "ChaFigurine":
        $ disableC = True
        show screen dungeon_map(mino_maze)
        "You look at the statue of minotaur, it seems to be grasping at its chest..."
        "After admiring the bull, you notice there is a paragraph of what seems to be a riddle."
        "Encrypted on its chest."
        "The riddle writes:"
        "'A beast I have captured with sorcery and magic.'"
        "'The purpose? The Muscle, the Strength and the Meat.'"
        pause 1
        "'The Minotaur proves to be highly energetic,'"
        "'for its member rises hard and majestic.'"
        pause 1
        "'The length, I have admired, as it's tight and erotic.'"
        "'Though trapped, it is capable of actions malefic.'"
        "'Caution is advised or result might be tragic.'"
        "..."
        "You are mildly shocked as to imagine the length of the minotaur described."
        "Hard... and Majestic...? You drool at the thought of seeing it yourself."
        "Shaking away at your sexual thoughts, you notice another stanza under the riddle."
        "It writes:"
        "'Alluring Lust:'"
        "'A tactic to make a battle easier, a skill to make the enemies' digits harder.'"
        "'Focus on your core and center, this is a charm and flirt enhancer.'"
        "'The Minotaur cannot be defeated with pure power, instead focus on awakening its member.'"
        pause 1
        "You feel your mind is suddenly filled with the power of ancient knowledge."
        "In mere seconds, you have learnt a new ability... All-luring... Lust?"
        msg "A new ability has been added to your skill menu."
        "You turn around and see the pink gem convulses."
        "The gem seems to react to your newly acquired ability."
        "In a few seconds, the gem glows in bright pink."
        "You can tell that the barrier at the center of the cave has been weakened."
        $ gem_thing -= 1
        if alluringlust not in learnedabilities:
            $ learnedabilities.append(alluringlust)
        $ mino_maze.unoccupy(2, 33)
        $ mino_maze.occupy(2, 33, cha_sprite2)
        $ mino_maze.unoccupy(5, 31)
        $ mino_maze.occupy(5, 31, chafigurine_sprite2)
    if _return == "FigurineOnStand":
        $ disableC = True
        show screen dungeon_map(mino_maze)
        "Now that the statue is on the stand, you just need to activate the gem."
    if _return == "FigurineOnStand2":
        $ disableC = True
        show screen dungeon_map(mino_maze)
        "You look at the statue of minotaur, it seems to be ready to run..."
        "The statue is glowing in yellow, and most importantly, it hardens enough to not ever crumble anymore."
    if _return == "Cha2":
        $ disableC = True
        show screen dungeon_map(mino_maze)
        "The gem is glowing in bright pink. You feel that this zone has been completed."

    if _return == "Agi2":
        $ disableC = True
        show screen dungeon_map(mino_maze)
        "The gem is glowing in bright yellow. You feel that this zone has been completed."
    if _return == "FCrater1":
        $ crater_num = 1
        jump maze_figurine_in_crater
    if _return == "FCrater2":
        $ crater_num = 2
        jump maze_figurine_in_crater
    if _return == "WFCrater1":
        $ crater_num = 3
        jump maze_figurine_in_crater
    if _return == "WFCrater2":
        $ crater_num = 4
        jump maze_figurine_in_crater
    if _return == "Crater1":
        $ crater_num = 1
        jump maze_crater
    if _return == "Crater2":
        $ crater_num = 2
        jump maze_crater
    $ disableC = False
    jump Minotaur_Maze_Loop

label maze_figurine_in_crater:
    $ disableC = True
    show screen dungeon_map(mino_maze)
    "You look at the tiny statue of a minotaur, it seems to be flexing its muscles."
    "It seems that the statue can be easily taken out of the crater..."
    menu:
        "Should you take it out?"
        "Yes{#takeoutcraterstatue}":
            if crater_num == 1:
                $ has_figurineL = True
                $ mino_maze.unoccupy(20, 6)
                $ addSprite(mino_maze, crater_sprite)
            if crater_num == 2:
                $ has_figurineL = True
                $ mino_maze.unoccupy(28, 6)
                $ addSprite(mino_maze, crater_sprite2)
            if crater_num == 3:
                $ has_figurineR = True
                $ mino_maze.unoccupy(28, 6)
                $ addSprite(mino_maze, crater_sprite2)
            if crater_num == 4:
                $ has_figurineR = True
                $ mino_maze.unoccupy(20, 6)
                $ addSprite(mino_maze, crater_sprite)
        "No{#takeoutcraterstatue}":
            pass
    $ disableC = False
    jump Minotaur_Maze_Loop

label Minotaur_Maze_Limestone:
    show screen dungeon_map(mino_maze)
    $ disableC = True
    if callInventoryItem("Copper Pickaxe", "Weapon"):
        "You stare at the chasm, it seems to be a weakpoint to extract some limestone."
        "However, you do not have the specific tool to get them out."
    else:
        $ mined = True
        if mimic_num == 1 and limestone_sprite1.status == 1:
            $ limestone_sprite1.reset()
        elif mimic_num == 2 and limestone_sprite2.status == 1:
            $ limestone_sprite2.reset()
        elif mimic_num == 3 and limestone_sprite3.status == 1:
            $ limestone_sprite3.reset()
        elif mimic_num == 4 and limestone_sprite4.status == 1:
            $ limestone_sprite4.reset()
        elif mimic_num == 5 and limestone_sprite5.status == 1:
            $ limestone_sprite5.reset()
        else:
            $ mined = False
        if mined:
            $ addItem("Limestone", inventory, 1)
            "You take out your pickaxe and start striking it against the chasm."
            "After a few long and grueling moments, a small chunk of the limestone falls out of the wall."
        else:
            "There's nothing for you to mine for now... Maybe the ore will replenish... eventually."
        $ item_number = LookForItemNumber("Limestone", inventory)
        "You have [item_number] limestones."
    jump Minotaur_Maze_Loop

label Minotaur_Maze_TenStatue:
    $ disableC = True
    show screen dungeon_map(mino_maze)
    "You run into the statue of minotaur in the cave, it seems to be resting, creating a strong barrier."
    menu:
        "Do you want to battle with the statue?"
        "Yes{#battlestatue}":
            jump minostatue_battle
        "No{#battlestatue}":
            pass
    $ disableC = False
    jump Minotaur_Maze_Loop
label maze_crater:
    $ disableC = True
    show screen dungeon_map(mino_maze)
    "There is a crater in the ground..."
    if has_figurineL or has_figurineR:
        "It seems that you can fit the statue in your hand right inside."
        menu:
            "Should you put the statue inside?"
            "Put the figurine facing left inside" if has_figurineL:
                if crater_num == 1:
                    $ has_figurineL = False
                    $ mino_maze.unoccupy(20, 6)
                    $ mino_maze.occupy(20, 6, figurineincrater_sprite)
                if crater_num == 2:
                    $ has_figurineL = False
                    $ mino_maze.unoccupy(28, 6)
                    $ mino_maze.occupy(28, 6, figurineincrater_sprite3)
            "Put the figurine facing right inside" if has_figurineR:
                if crater_num == 1:
                    $ has_figurineR = False
                    $ mino_maze.unoccupy(20, 6)
                    $ mino_maze.occupy(20, 6, figurineincrater_sprite4)
                if crater_num == 2:
                    $ has_figurineR = False
                    $ mino_maze.unoccupy(28, 6)
                    $ mino_maze.occupy(28, 6, figurineincrater_sprite2)
            "No{#putdownstrengthstatue}":
                pass
    $ disableC = False
    jump Minotaur_Maze_Loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
