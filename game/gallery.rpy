default gallery_view = Replay_items

default gallery_open = False
screen sound_loop_player(sound_list, interval=1.3):
    if squelch == sound_list or squelch in sound_list:
        timer renpy.random.randint(60, 140)/100.0*interval action Play("nsfw", squelch[ renpy.random.randint(0, len(squelch)-1) ], loop = False) repeat True
    if plap == sound_list or plap in sound_list:
        timer interval action Play("nsfw", plap[ renpy.random.randint(0, len(plap)-1) ], loop = False) repeat True

init python:

    maxthumbx = config.screen_width / (3 + 1)
    maxthumby = config.screen_height / (2 + 1)

    replay_page = 0

    class ReplayItem:
        def __init__(self, thumbs, replay, name, unlocked = False):
            self.thumbs = thumbs
            self.replay = replay
            self.name = name
            self.unlocked = unlocked
        
        def num_replay(self):
            return len(self.thumbs)

    renpy.music.register_channel("nsfw", "sfx", True)




    Replay_items = []
    Replay_items.append(ReplayItem(["cg01"], "scene_slime_sex", _("{color=#000}Losing in Slime Battle{/color}")))
    Replay_items.append(ReplayItem(["cg02"], "scene_masturbation", _("{color=#000}Masturbating at Day Time{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Exhibition_Masturbation", _("{color=#000}Masturbating at Night Time{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Sebas_Under_Counter", _("{color=#000}Giving Sebas at work a blowjob{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Goat_Lose", _("{color=#000}Losing in Goat Battle{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Goat_Win", _("{color=#000}Winning in Goat Battle{/color}"))) 
    Replay_items.append(ReplayItem(["cg01"], "scene_buggbear_lose", _("{color=#000}Losing in Buggbear Battle{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "scene_buggbear_win", _("{color=#000}Winning in Buggbear Battle{/color}"))) 
    Replay_items.append(ReplayItem(["cg01"], "Scene_Tavern_Meet_01", _("{color=#000}Serving in Private Show 1{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Tavern_Meet_02", _("{color=#000}Serving in Private Show 2{/color}"))) 
    Replay_items.append(ReplayItem(["cg01"], "Scene_Tavern_Meet_03", _("{color=#000}Serving in Private Show 3{/color}")))

    Replay_items.append(ReplayItem(["cg01"], "scene_lothargrope", _("{color=#000}Groping Lothar after Sparring{/color}"))) 
    Replay_items.append(ReplayItem(["cg01"], "scene_minolose", _("{color=#000}Losing in Minotaur Battle{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "scene_minowin", _("{color=#000}Winning in Minotaur Battle{/color}"))) 
    Replay_items.append(ReplayItem(["cg01"], "scene_mimiclose", _("{color=#000}Losing in Mimic Battle{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Cane_Sebas_Tavern_Night", _("{color=#000}Snooping on Sebas and Cane{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "scene_werewolf_lose", _("{color=#000}Losing in Werewolf Battle{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "scene_werewolf_win", _("{color=#000}Winning in Werewolf Battle{/color}"))) 
    Replay_items.append(ReplayItem(["cg01"], "scene_ambleskill", _("{color=#000}Learning Skill from Amble{/color}"))) 
    Replay_items.append(ReplayItem(["cg01"], "scene_jogskill", _("{color=#000}Learning Skill from Jog{/color}"))) 
    Replay_items.append(ReplayItem(["cg01"], "scene_feral_lose", _("{color=#000}Losing in Feral Battle{/color}"))) 
    Replay_items.append(ReplayItem(["cg01"], "Scene_Lothar_Aphrodisiac_Quest", _("{color=#000}Consuming Aphrodisiac with Lothar{/color}"))) 
    Replay_items.append(ReplayItem(["cg01"], "Cane_Favour_For_Ya_Sex", _("{color=#000}Asking Cane about his Favour{/color}"))) 

    Replay_items.append(ReplayItem(["cg01"], "Scene_Arthur_Yes", _("{color=#000}Being submissive with Arthur{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Arthur_NoNo", _("{color=#000}Being rebellious with Arthur{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Hefty_Slime_Lose", _("{color=#000}Losing to Hefty/Malignant Slime{/color}")))

    Replay_items.append(ReplayItem(["cg01"], "Scene_Nosferat_Lose", _("{color=#000}Losing in Nosferat Battle{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Shark_Bandit_Lose", _("{color=#000}Losing to Bandit Boss{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Bandit_Win", _("{color=#000} Winning in Bandit Battle{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Bandit_Gangbang", _("{color=#000}Captured by Bandits{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Werewolf_Gangbang", _("{color=#000}Joining Uffe's Celebration{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "scene_tavern_cardgame_lose", _("{color=#000} Paying Debt to Tavern Regulars{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "scene_gnoll_lose", _("{color=#000} Losing in Gnoll Battle{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "scene_gnoll_win_top", _("{color=#000} Winning and Topping the Gnoll{/color}")))

    Replay_items.append(ReplayItem(["cg01"], "Scene_Pirkka_Show", _("{color=#000} Joining Pirkka in his Tavern Room{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Spritebinder_Lose", _("{color=#000} Losing to a spritebinder before the elk arrives{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Bear_Lose", _("{color=#000} Losing in bear guard battle{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Bear_Win", _("{color=#000} Winning in bear guard battle{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Werewolf_Double_Lose", _("{color=#000} Losing to the werewolf duo at night{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Cult_Acolyte_Hypnosis", _("{color=#000} Losing to the cult acolyte{/color}")))

    Replay_items.append(ReplayItem(["cg01"], "Scene_Haskell_Blowjob", _("{color=#000} Drinking from Haskell in tea session{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Rat_Patron_Alleyway", _("{color=#000} Getting sucked by the rat patron{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Caretaker_Extraction", _("{color=#000} Getting extracted from the snow creatures{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Furkan_Kari_Keepsake", _("{color=#000} Meeting of Furkan and Kari{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Lothar_Gnoll_Keepsake", _("{color=#000} Lothar ambushed by Gnolls{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Jotunn_Lose", _("{color=#000} Losing to a Lustful Jotunn{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Magic_Show_Growth_Potion", _("{color=#000} Performing a Growth Potion Show{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Magic_Show_Bondage_Box", _("{color=#000} Performing a Bondage Box Show{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Magic_Show_Portal_Ring", _("{color=#000} Performing a Portal Ring Show{/color}")))
    Replay_items.append(ReplayItem(["cg01"], "Scene_Magic_Show_Command_Controller", _("{color=#000} Performing a Command Controller Show{/color}")))


    BadEnds = []
    BadEnds.append(ReplayItem(["cg01"], "BadEnd_FeralLose", _("{color=#000}Losing to Feral Werewolf with 80 Purity{/color}")))
    BadEnds.append(ReplayItem(["cg01"], "BadEnd_SlimeLose", _("{color=#000}Losing to Malignant/Hefty Slime with 70 Purity{/color}")))
    BadEnds.append(ReplayItem(["cg01"], "BadEnd_Werewolf_Capture", _("{color=#000}Captured by the werewolves after Tetto Escapes{/color}")))
    BadEnds.append(ReplayItem(["cg01"], "BadEnd_Bandit_Bondage", _("{color=#000}Getting Caught too many times by Bandits{/color}")))
    BadEnds.append(ReplayItem(["cg01"], "BadEnd_Buggbear_Sheath", _("{color=#000}Caught by the buggbear after failed sedation{/color}")))
    BadEnds.append(ReplayItem(["cg01"], "BadEnd_Jotunn_Suck", _("{color=#000}Losing to a Lustful Jotunn with 65 Purity{/color}")))


image black = "#000"






image cg01:
    "gallery_unlocked"
    size (384,216)

image cg02:
    "gallery_unlocked"
    size (384,216)




screen Replayexit():
    zorder 100
    imagebutton:
        yalign .99
        xalign .99
        idle "battle_escape"
        action EndReplay()







screen replay_gallery():
    tag menu


    use game_menu(_("Gallery")):

        $ start = replay_page * 6

        $ last_item = len(gallery_view) - 1
        $ end = min(start + 6 - 1, last_item)
        if end - start <= 6:
            grid 3 2:
                xalign 0.5
                yalign 0.02
                xspacing 60
                yspacing 225
                xmaximum 384

                for i in range(start, end + 1):
                    if renpy.seen_label(gallery_view[i].replay) or gallery_open:
                        hbox:
                            spacing maxthumbx - 20
                            xalign 0.5
                            yalign 0.1
                            frame:
                                xanchor 0
                                xpadding 50
                                ypadding 10
                                yalign 0.1
                                xminimum 384
                                text gallery_view[i].name color "#fff" size 25 xalign 0.5
                    else:
                        null

                for i in range(end - start + 1, 6):
                    null


            grid 3 2:
                xalign 0.50
                yalign 0.2
                xspacing 60
                yspacing 80

                for i in range(start, end + 1):
                    if renpy.seen_label(gallery_view[i].replay) or gallery_open:
                        imagebutton idle gallery_view[i].thumbs:
                            action Replay(gallery_view[i].replay, locked = False)
                            xalign 0.5
                            yalign 0.5
                    else:
                        vbox xalign 0.5 yalign 0.5:
                            add "gallery_locked"


                for i in range(end - start + 1, 6):
                    null





        if replay_page > 0:
            imagebutton:
                idle "dungeon_left"
                hover "dungeon_left_hover"
                action SetVariable("replay_page", replay_page - 1)
                xalign 0.1
                yalign 0.85
        $ replay_page1 = replay_page + 1
        text "[replay_page1]" xalign 0.5 yalign 0.85 font "leafy.otf" size 80 bold True color "#db9b3bff" outlines [(absolute(4), "#4d2e22")]

        if (replay_page + 1) * 6 < len(gallery_view):
            imagebutton:
                idle "dungeon_right"
                hover "dungeon_right_hover"
                action SetVariable("replay_page", replay_page + 1)
                xalign 0.9
                yalign 0.85


        if gallery_view != Replay_items:
            imagebutton:
                idle "gallerybe_idle"
                hover "gallerybe_hover"
                xalign 0.95
                yalign -0.2
                action SetScreenVariable("gallery_view", Replay_items), SetVariable("replay_page", 0)
        else:
            imagebutton:
                idle "galleryart_idle"
                hover "galleryart_hover"
                xalign 0.95
                yalign -0.2
                action SetScreenVariable("gallery_view", BadEnds), SetVariable("replay_page", 0)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
