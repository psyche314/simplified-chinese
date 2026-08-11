default diskscore = {"Ole":[0, 1, 3], "Lothar":[2, 5, 3], "Player":[5, 5, 3], "Sebas":[3, 3, 2]}
default diskscore2 = {"Ole":3, "Lothar":10, "Player":13, "Sebas":8}
default diskscore3 = sorted(diskscore2.items(), key= lambda x:x[1])
default disk_moving = False

default cardgame_ddeck = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12]
default cdg_p = []
default cdg_c1 = []
default cdg_c2 = []
default cdg_c3 = []
default cdg_hover1 = False
default cdg_hover2 = False
default cdg_hover3 = False
default cardgame_dseq = [cdg_p, cdg_c1, cdg_c2, cdg_c3]
default selected_card = None
default unhovering_card = 0
default show_card_remaining = False
default show_taking_pile = False
default cardgame_pile = []
default cdg_peeking = False
default cdg_winner = []
init python:

    import math

    class Disk():
        def __init__(self, dx, dy, velocity = [0, 0], acceleration = 2):
            self.dx = dx 
            self.dy = dy
            self.velocity = velocity
            self.acceleration = acceleration
        
        def rolling(self, friction = 0.95):
            self.dx += self.velocity[0]
            self.dy -= self.velocity[1]
            self.velocity[0] *= friction
            self.velocity[1] *= friction
        def is_moving(self):
            return abs(self.velocity[0]) > 0.01 or abs(self.velocity[1]) > 0.01

    class DiskGame():
        
        def __init__(self):
            
            self.disk_radius = 25
            self.dx = 1920/2
            self.dxmin = 100
            self.dxmax = 1820
            self.dy = 750
            self.turn = 3
            self.minV = 5
            self.maxV = 20
            self.disk_num = 0
            self.setV = 0
            self.diskin = None
            self.aiming = False
            self.score = {"Ole":[0, 0, 0], "Lothar":[0, 0, 0], "Player":[0, 0, 0], "Sebas":[0, 0, 0]}
            
            self.disks = []
        
        def disking(self):
            self.disks.append(Disk(self.dx, self.dy))
        
        def moveX(self, ddx):
            
            self.diskin.dx += ddx 
        
        def checkScore(self, disk):
            dist = (abs(disk.dx - 948)**2 + abs(disk.dy - 150)**2) ** 0.5
            if dist < 80:
                scory = 5
            elif dist < 170:
                scory = 3
            elif dist < 250:
                scory = 2
            elif dist < 350:
                scory = 1
            else:
                scory = 0
            return scory
        
        def checkCollision(self, disk1, disk2):
            dist = (abs(disk1.dx - disk2.dx)**2 + abs(disk1.dy - disk2.dy)**2) ** 0.5
            if dist <= self.disk_radius * 4:
                
                return True 
            else:
                return False
        
        def npcStartRolling(self, velo, angle, dx, dy):
            global disk_moving 
            disk_moving = True
            
            angle = math.radians(angle)
            self.disks.append(Disk(dx, dy, [velo*1.4*math.sin(angle), velo*1.4*math.cos(angle)], 0.97))
        
        def startRolling(self, velo, angle):
            global disk_moving 
            disk_moving = True
            
            velo *= 0.05*(pc.stg - 3) + 0.7              
            angle = angle-(1.3**(8-pc.agi))/2+(1.3**(8-pc.agi))*renpy.random.random()
            angle = math.radians(angle)
            self.disks.append(Disk(self.diskin.dx, self.diskin.dy, [velo*1.4*math.sin(angle), velo*1.4*math.cos(angle)], 0.97))
            
            self.diskin = None 
        
        def calculation(self):
            scoring = {"Ole":sum(self.score["Ole"]),"Lothar":sum(self.score["Lothar"]),e:sum(self.score["Player"]),"Sebas":sum(self.score["Sebas"])}
            scoring2 = sorted(scoring.items(), key=lambda x:x[1])
            return scoring2            
        
        def all_disks_stopped(self, threshold=0.05):
            for disk in self.disks:
                if abs(disk.velocity[0]+disk.velocity[1]) > threshold:
                    return False
            return True
        
        def collideCal(self, disk1, disk2):
            
            normal_x = disk2.dx - disk1.dx
            normal_y = disk2.dy - disk1.dy
            distance = math.hypot(normal_x, normal_y)
            
            
            if distance == 0:
                
                return
            normal_x /= distance
            normal_y /= distance
            
            
            rel_vel_x = disk1.velocity[0] - disk2.velocity[0]
            rel_vel_y = disk1.velocity[1] - disk2.velocity[1]
            
            
            vel_along_normal = rel_vel_x * normal_x + rel_vel_y * normal_y
            
            
            if vel_along_normal > 0:
                return
            
            restitution = 1.0
            
            
            impulse = -(1 + restitution) * vel_along_normal / 2 
            
            
            impulse_x = impulse * normal_x
            impulse_y = impulse * normal_y
            disk1.velocity[0] += impulse_x
            disk1.velocity[1] += impulse_y
            disk2.velocity[0] -= impulse_x
            disk2.velocity[1] -= impulse_y
        
        
        
        
        def getDiskArrowAngle(self, disk1, diskinx, diskiny):
            slope = (disk1.dy - diskiny) / (disk1.dx - diskinx)
            dangle = math.atan(slope)

    def update_disks():
        moving = False
        for disk in disky.disks:
            if disk.is_moving():
                disk.rolling()
                moving = True
        if not moving:
            pass
        else:
            
            renpy.restart_interaction()


    def initial_dealing(deck, c1, c2, c3, c4):
        for i in range(20):
            new_card = deck[len(deck)-1]
            if i % 4 == 0:
                c1.append(new_card)
            elif i % 4 == 1:
                c2.append(new_card)
            elif i % 4 == 2:
                c3.append(new_card)
            else:
                c4.append(new_card)
            deck.pop()

    def WeightedChoice(choices):
        
        totalweight = 0.0
        for choice, weight in choices:
            totalweight += weight
        randval = renpy.random.random() * totalweight
        for choice, weight in choices:
            if randval <= weight:
                return choice
            else:
                randval -= weight
    def checking_weights(deck, pile, comp):
        sorted_comp = sorted(comp)
        weighted_comp = []
        lene = len(sorted_comp)
        for i in range(lene):
            
            weights = int(1.5*((0.15+(lene/100))**(i-3.5))+1)
            weighted_comp.append((sorted_comp[i],weights))
        return weighted_comp

    def removeallbutburner(pile):
        ped = []
        for i in pile:
            if i == 11:
                ped.append(i)
        
        return ped

    def playing_cards(deck, pile, comp):
        sorted_comp = sorted(comp)
        weighted_comp = []
        lene = len(sorted_comp)
        for i in range(lene):
            weights = int((lene*15)*((0.066*(i+1))**((i+1)-0.66))+5)
            weighted_comp.append((sorted_comp[i],weights))
        if len(pile) == 0:
            picked_card = WeightedChoice(weighted_comp)
            stacky = []
            for i in range(lene):
                if comp[i] == picked_card:
                    stacky.append(i)
            
            if len(stacky) > 1 and renpy.random.random() > 0.2:
                for i in range(len(stacky)):
                    pile.append(picked_card)
                    comp.remove(picked_card)
                    if renpy.random.random() > 0.5*(3-i):
                        return (len(stacky), picked_card)
            else:
                pile.append(picked_card)
                comp.remove(picked_card)
            return (len(stacky), picked_card)
        else:
            playable_weighted_comp = []
            for i in weighted_comp:
                if pile[-1] < i[0] and not (pile[-1] < 7 and i[0] >= 10):
                    playable_weighted_comp.append(i)
            if len(playable_weighted_comp) > 1 or len(playable_weighted_comp) == 1 and renpy.random.random() < 0.5:
                picked_card = WeightedChoice(playable_weighted_comp)
                stacky = []
                for i in range(lene):
                    if comp[i] == picked_card:
                        stacky.append(i)
                if len(stacky) > 1 and renpy.random.random() > 0.2:
                    for i in range(len(stacky)):
                        pile.append(picked_card)
                        comp.remove(picked_card)
                else:
                    pile.append(picked_card)
                    comp.remove(picked_card)
                return (len(stacky), picked_card)
            else:
                for i in pile:
                    comp.append(i)
                return (0, "Took the pile")

    def pp_playing_cards(deck, pile, comp, picked_card):
        stacky = []
        for i in range(len(comp)):
            if comp[i] == picked_card:
                stacky.append(picked_card)
        for i in range(len(stacky)):
            pile.append(picked_card)
            comp.remove(picked_card)
        return len(stacky)

    def pp_taking_pile(deck, pile, comp):
        for i in pile:
            comp.append(i)

    def drawing_card(deck, c1, c2, c3, c4):
        if len(c1) < 5:
            for i in range(5-(len(c1))):
                if len(deck) > 0:
                    new_card = deck[len(deck)-1]
                    c1.append(new_card)
                    deck.pop()
        if len(c2) < 5:
            for i in range(5-(len(c2))):
                if len(deck) > 0:
                    new_card = deck[len(deck)-1]
                    c2.append(new_card)
                    deck.pop()
        if len(c3) < 5:
            for i in range(5-(len(c3))):
                if len(deck) > 0:
                    new_card = deck[len(deck)-1]
                    c3.append(new_card)
                    deck.pop()
        if len(c4) < 5:
            for i in range(5-(len(c4))):
                if len(deck) > 0:
                    new_card = deck[len(deck)-1]
                    c4.append(new_card)
                    deck.pop()

    def choosing_peek(c1, c2, c3):
        compare_list = [None, None, None]
        if len(c2) < len(c1):
            compare_list[0] = c2
            if len(c3) < len(c1):
                compare_list[1] = c3
                compare_list[2] = c1
            else:
                compare_list[1] = c1
                compare_list[2] = c3
            if len(c3) < len(c2):
                compare_list[0] = c3 
                compare_list[1] = c2
                compare_list[2] = c1
        elif len(c3) < len(c1):
            compare_list[0] = c3
            compare_list[1] = c1
            compare_list[2] = c2
        else:
            compare_list[0] = c1
            if len(c3) < len(c2):
                compare_list[1] = c3
                compare_list[2] = c2
            else:
                compare_list[1] = c2
                compare_list[2] = c3
        if len(compare_list[0]) == 0:
            if len(compare_list[1]) == 0:
                picked_peek = compare_list[2]
            else:
                picked_peek = WeightedChoice([(compare_list[1], 70), (compare_list[2], 30)])        
        else:
            picked_peek = WeightedChoice([(compare_list[0], 50), (compare_list[1], 30), (compare_list[2], 20)])
        return picked_peek

    def swapping_hand(c1, c2):
        temp = []
        for i in range(len(c1)):
            new_card = c1[-1]
            temp.append(new_card)
            c1.pop()
        for i in range(len(c2)):
            new_card = c2[-1]
            c1.append(new_card)
            c2.pop()
        for i in range(len(temp)):
            new_card = temp[-1]
            c2.append(new_card)
            temp.pop()

    def random_pile_pos():
        new_deck = []
        for i in range(52):
            cardxposition = int(540+renpy.random.random()*50)
            cardyposition = int(400+renpy.random.random()*40)
            cardrotation = (renpy.random.random()*160)-80
            new_deck.append([cardxposition, cardyposition, cardrotation])
        return new_deck

style tavern_disk_text:
    font "leafy.otf"
    size 30
    hover_color "#000000"
    color "#ffffff"

style tavern_disk_shoot_text:
    font "leafy.otf"
    size 40
    hover_color "#fff"
    color "#000"

style tavern_disk_score_text:
    font "leafy.otf"
    size 60
    color "#3d2111"

style tavern_disk_winner_text:
    font "leafy.otf"
    size 50
    color "#3d2111"

screen disk_game():
    default diskyv = 5
    default diskyangle = 20

    if disky.diskin != None:
        imagebutton:
            xpos disky.diskin.dx
            ypos disky.diskin.dy
            idle "bowlingball"
            action NullAction()
        vbox:
            xalign 0.5
            yalign 0.925
            spacing 20

            text _("Strength") style "tavern_disk_text"
            text _("Angle") style "tavern_disk_text"
        vbox:
            xminimum 80
            xmaximum 300
            xalign 0.5
            yalign 0.925
            spacing 20

            bar value ScreenVariableValue("diskyv", 40) style "bar"
            bar value ScreenVariableValue("diskyangle", 40) style "slider"

        add "diskyarrow":
            rotate ((diskyangle-20)*2)
            pos (disky.diskin.dx-200, disky.diskin.dy-220)

        frame:
            xalign 0.7
            yalign 0.9
            textbutton _("Shoot") style_prefix "tavern_disk_shoot" action [Function(disky.startRolling, (diskyv*25/40)+15, (diskyangle-15)), Return("Oh")]


        imagebutton:
            xalign 0.2
            yalign 0.8
            idle "dungeon_left"
            hover "dungeon_left_hover"
            action [Function(disky.moveX, -10)]

        imagebutton:
            xalign 0.8
            yalign 0.8
            idle "dungeon_right"
            hover "dungeon_right_hover"
            action [Function(disky.moveX, 10)]
    else:
        timer 0.1 repeat True action If(disky.all_disks_stopped() and disk_moving, [Return(), SetVariable("disk_moving", False)])

    for i in range(len(disky.disks)):
        $ disk = disky.disks[i]
        for disk2 in disky.disks:

            if disky.checkCollision(disk, disk2) and disk != disk2:
                $ disky.collideCal(disk, disk2)

        if not disky.all_disks_stopped() or disk_moving == True:
            textbutton _("Skip") xalign 0.1 yalign 0.9 style "tavern_disk_text" action [Return(None), SetVariable("disk_moving", False)]
            timer 0.075 repeat True action Function(update_disks)

        $ disk.rolling()
        if i % 4 == 2:
            $ disky.score["Player"][(i-2)/4] = disky.checkScore(disk)
            add "bowlingball":
                pos (int(disk.dx), int(disk.dy))
        elif i % 4 == 0:
            $ disky.score["Ole"][i/4] = disky.checkScore(disk)
            add "bowlingball1":
                pos (int(disk.dx), int(disk.dy))
        elif i % 4 == 3:
            $ disky.score["Sebas"][(i-3)/4] = disky.checkScore(disk)
            add "bowlingball3":
                pos (int(disk.dx), int(disk.dy))
        else:
            $ disky.score["Lothar"][(i-1)/4] = disky.checkScore(disk)
            add "bowlingball2":
                pos (int(disk.dx), int(disk.dy))

    add "diskscoreboard"
    text _("Score") xalign 0.93 yalign 0.025 style "tavern_disk_score_text"
    hbox:
        xalign 0.985
        yalign 0.15
        spacing 55
        for i in disky.score["Ole"]:
            text "[i]" style "tavern_disk_winner_text"
    hbox:
        xalign 0.985
        yalign 0.27
        spacing 55
        for i in disky.score["Lothar"]:
            text "[i]" style "tavern_disk_winner_text"
    hbox:
        xalign 0.985
        yalign 0.38
        spacing 55
        for i in disky.score["Player"]:
            text "[i]" style "tavern_disk_winner_text"
    hbox:
        xalign 0.985
        yalign 0.50
        spacing 55
        for i in disky.score["Sebas"]:
            text "[i]" style "tavern_disk_winner_text"

screen card_game():







    for i in range(len(cdg_c1)):
        $ cardimg = "card_" + str(cdg_c1[i])
        if len(cdg_c1) <= 5:
            $ card_w = 200
        else:
            $ card_w = 200+(len(cdg_c1)-5)*4
        if card_w > 240:
            $ card_w = 240
        $ cardyposition = 540-len(cdg_c1)*140+((len(cdg_c1)-1)*card_w/2)+i*(280-card_w)
        if cdg_peeking and not cdg_hover1:
            imagebutton:
                xpos 100
                ypos cardyposition
                idle "card_back"
                hovered SetVariable("cdg_hover1", True)
                action NullAction()
        elif cdg_hover1 and cdg_swapping == None:
            imagebutton:
                xpos 200
                ypos cardyposition
                idle "card_back"
                hovered SetVariable("cdg_hover1", True)
                unhovered SetVariable("cdg_hover1", False)
                action SetVariable("cdg_peeking", False), SetVariable("cdg_swapping", cdg_c1)
            text "Swap?" xpos 200 ypos 540 style "button_text2"
        elif cdg_swapping == cdg_c1:
            imagebutton:
                xpos 100
                ypos cardyposition
                idle cardimg
                action NullAction()
        else:
            imagebutton:
                xpos 100
                ypos cardyposition
                idle "card_back"
                action NullAction()

    for i in range(len(cdg_c2)):
        $ cardimg = "card_" + str(cdg_c2[i])
        if len(cdg_c2) <= 5:
            $ card_w = 60
        else:
            $ card_w = 60+(len(cdg_c2)-5)*5
        if card_w > 160:
            $ card_w = 180
        $ cardxposition = 960-len(cdg_c2)*100+((len(cdg_c2)-1)*card_w/2)+i*(200-card_w)
        if cdg_peeking and not cdg_hover2:
            imagebutton:
                xpos cardxposition
                ypos 50
                idle "card_back"
                hovered SetVariable("cdg_hover2", True)
                action NullAction()
        elif cdg_hover2 and cdg_swapping == None:
            imagebutton:
                xpos cardxposition
                ypos 150
                idle "card_back"
                hovered SetVariable("cdg_hover2", True)
                unhovered SetVariable("cdg_hover2", False)
                action SetVariable("cdg_peeking", False), SetVariable("cdg_swapping", cdg_c2)
            text "Swap?" xpos 960 ypos 150 style "button_text2"
        elif cdg_swapping == cdg_c2:
            imagebutton:
                xpos cardxposition
                ypos 50
                idle cardimg
                action NullAction()
        else:
            imagebutton:
                xpos cardxposition
                ypos 50
                idle "card_back"
                action NullAction()
    $ cdg_lc1 = len(cdg_c1)
    $ cdg_lc2 = len(cdg_c2)
    $ cdg_lc3 = len(cdg_c3)
    $ cdg_lp = len(cdg_p)
    vbox:
        xalign 0.05
        yalign 0.05
        spacing 10
        frame:
            background Frame("coolframe", 10, 10, 10, 10)
            xpadding 20
            ypadding 20
            text _("Gato: [cdg_lc2]") style "button_text2" color "#78957e"

    vbox:
        xalign 0.05
        yalign 0.95
        spacing 10
        frame:
            background Frame("coolframe", 10, 10, 10, 10)
            xpadding 20
            ypadding 20
            text _("[e]: [cdg_lp]") style "button_text2" color "#ffffff"

    vbox:
        xalign 0.95
        yalign 0.05
        spacing 10
        frame:
            background Frame("coolframe", 10, 10, 10, 10)
            xpadding 20
            ypadding 20
            text _("Fokk : [cdg_lc1]") style "button_text2" color "#a39291"

    vbox:
        xalign 0.95
        yalign 0.95
        spacing 10
        frame:
            background Frame("coolframe", 10, 10, 10, 10)
            xpadding 20
            ypadding 20
            text _("Coit: [cdg_lc3]") style "button_text2" color "#c68079"

    vbox:
        xalign 0.05
        yalign 0.84
        spacing 10
        button:
            background Frame("coolframe", 10, 10, 10, 10)
            xpadding 20
            ypadding 20
            action Call("Nocturnal_Trunk_Cardy_Tutorial")
            text _("Game Instruction") style "button_text2" color "#edd3bf"


    for i in range(len(cdg_c3)):
        $ cardimg = "card_" + str(cdg_c3[i])
        if len(cdg_c3) <= 5:
            $ card_w = 200
        else:
            $ card_w = 200+(len(cdg_c3)-5)*4
        if card_w > 240:
            $ card_w = 240
        $ cardyposition = 540-len(cdg_c3)*140+((len(cdg_c3)-1)*card_w/2)+i*(280-card_w)
        if cdg_peeking and not cdg_hover3:
            imagebutton:
                xpos 1700
                ypos cardyposition
                idle "card_back"
                hovered SetVariable("cdg_hover3", True)
                action NullAction()
        elif cdg_hover3 and cdg_swapping == None:
            imagebutton:
                xpos 1600
                ypos cardyposition
                idle "card_back"
                hovered SetVariable("cdg_hover3", True)
                unhovered SetVariable("cdg_hover3", False)
                action SetVariable("cdg_peeking", False), SetVariable("cdg_swapping", cdg_c3)
            text "Swap?" xpos 1600 ypos 540 style "button_text2"
        elif cdg_swapping == cdg_c3:
            imagebutton:
                xpos 1700
                ypos cardyposition
                idle cardimg
                action NullAction()
        else:
            imagebutton:
                xpos 1700
                ypos cardyposition
                idle "card_back"
                action NullAction()



    $ card_remaining = len(cardgame_deck)
    for i in range(len(cardgame_deck)):

        $ cardyposition = 450-i*2
        imagebutton:
            xpos 1300
            ypos cardyposition
            idle "card_back"
            hovered SetVariable("show_card_remaining", True)
            unhovered SetVariable("show_card_remaining", False)
            action NullAction()

    if show_card_remaining:
        text _("[card_remaining] Cards in Deck") xpos 1250 ypos 350 style "button_text2"



    for i in range(len(cardgame_pile)):

        $ cardimg = "card_" + str(cardgame_pile[i])
        $ cardxposition = int(540+renpy.random.random()*50)
        $ cardyposition = int(450+renpy.random.random()*40)
        $ cardrotation = (renpy.random.random()*180)-90
        add cardimg:
            rotate (cdg_setrandom[i][2])
            pos (cdg_setrandom[i][0], cdg_setrandom[i][1])
    if cdg_player_turn and len(cardgame_pile) > 0:
        imagebutton:
            xpos 565
            ypos 470
            idle "empty2"
            action Return("Take the Pile")
            hovered SetVariable("show_taking_pile", True)
            unhovered SetVariable("show_taking_pile", False)

        if show_taking_pile:
            text _("Take the pile?") xpos 565 ypos 400 style "button_text2"

    for i in range(len(cdg_p)):

        $ cardimg = "card_" + str(cdg_p[i])
        if len(cdg_p) <= 5:
            $ card_w = 40
        else:
            $ card_w = 40+(len(cdg_p)-5)*8
        if card_w > 160:
            $ card_w = 180
        $ cardxposition = 960-len(cdg_p)*100+((len(cdg_p)-1)*card_w/2)+i*(200-card_w)
        if i != selected_card:
            imagebutton:
                xpos cardxposition
                ypos 780
                idle cardimg
                action NullAction()
                hovered SetVariable("selected_card", i)

    if selected_card != None:
        $ cardo = str(cdg_p[selected_card])
        $ cardimg = "card_" + cardo
        if len(cdg_p) <= 5:
            $ card_w = 40
        else:
            $ card_w = 40+(len(cdg_p)-5)*8
        if card_w > 160:
            $ card_w = 180
        $ cardxposition = 960-len(cdg_p)*100+((len(cdg_p)-1)*card_w/2)+selected_card*(200-card_w)
        if not cdg_player_turn:
            imagebutton:
                xpos cardxposition
                ypos 740
                idle cardimg
                action Notify(__("It's not your turn yet!"))
                unhovered SetVariable("selected_card", None)
        elif len(cardgame_pile) > 0 and cdg_p[selected_card] < cardgame_pile[-1] and cdg_p[selected_card] < 10:
            imagebutton:
                xpos cardxposition
                ypos 740
                idle cardimg
                action Notify(__("The card is too small!"))
                unhovered SetVariable("selected_card", None)
        elif len(cardgame_pile) > 0 and cardgame_pile[-1] < 7 and cdg_p[selected_card] > 10:
            imagebutton:
                xpos cardxposition
                ypos 740
                idle cardimg
                action Notify(__("Special Cards can only be played on numbers higher than 6!"))
                unhovered SetVariable("selected_card", None)
        else:
            imagebutton:
                xpos cardxposition
                ypos 740
                idle cardimg
                action Return(cardo), SetVariable("selected_card", None)
                unhovered SetVariable("selected_card", None)

        if cdg_p[selected_card] == 10:
            text _("Watcher: Watch and Swap with other.") xpos cardxposition ypos 700 style "button_text2"
        if cdg_p[selected_card] == 11:
            text _("Kindler: Burn the entire pile") xpos cardxposition ypos 700 style "button_text2"
        if cdg_p[selected_card] == 12:
            text _("Drifter: Highest Rank in the game.") xpos cardxposition ypos 700 style "button_text2"

    if cdg_swapping != None:
        frame:
            xpos 600
            ypos 540
            xpadding 15
            ypadding 15
            style "coolframe"
            textbutton "Swap" style "button_text2" action Return("Swap")
        frame:
            xpos 1300
            ypos 540
            xpadding 15
            ypadding 15
            style "coolframe"
            textbutton "Keep" style "button_text2" action Return("Ok")

label Card_Game_Begin:
    scene cardgame_table with dissolve
    hide screen daytime
    hide screen menu_buttons
    $ cardgame_played += 1
    $ cardgame_ddeck = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12]
    $ cdg_winner = []
    $ cdg_player_turn = False
    $ cdg_setrandom = random_pile_pos()
    $ cdg_p = []
    $ cdg_c1 = []
    $ cdg_c2 = []
    $ cdg_swapping = None
    $ cdg_c3 = []
    $ cardgame_pile = []
    $ cardgame_dseq = [cdg_p, cdg_c1, cdg_c2, cdg_c3]
    $ cardgame_deck = cardgame_ddeck
    $ renpy.random.shuffle(cardgame_deck)
    $ cdg_seq = renpy.random.randint(0,3)
    $ cdg_turns = 0
    $ initial_dealing(cardgame_deck, cardgame_dseq[cdg_seq%4], cardgame_dseq[(cdg_seq+1)%4], cardgame_dseq[(cdg_seq+2)%4], cardgame_dseq[(cdg_seq+3)%4])
    show screen card_game()
    "Fokk hands each of you a pile of cards, and throws a 4-sided dice on the table."
    if cdg_seq == 0:
        fokk "Our server 'ere will start the round."
    if cdg_seq == 1:
        fokk "The dice's decided, I'll start the round."
    if cdg_seq == 2:
        fokk "Let's see, it says Gato gets the first turn."
    if cdg_seq == 3:
        fokk "Coit's going to start this round."
    jump Card_Game_Turn

label Card_Game_Turn:
    show screen card_game()

    if cdg_turns % 4 == cdg_seq%4 and len(cdg_p) > 0:
        "It's your turn!"
        $ cdg_player_turn = True
        call screen card_game()
        if _return.isnumeric():
            $ cdg_action = int(_return)
            $ stacked_card = pp_playing_cards(cardgame_deck, cardgame_pile, cdg_p, cdg_action)
            show screen card_game()
            if cdg_action == 11:
                "You played the kindler, and burnt the pile away."
                $ cardgame_pile = removeallbutburner(cardgame_pile)
            elif cdg_action == 10:
                if len(cdg_p) == 0:
                    "You played the watcher, and subsequently emptied your hand!"
                else:
                    $ cdg_player_turn = False
                    $ cdg_peeking = True
                    call screen card_game() 
                    show screen card_game()
                    if _return == "Swap":

                        if cdg_swapping == cdg_c3:
                            "You played a watcher, and swapped your entire hand with Coit."
                            if len(cdg_c3) < len(cdg_p):
                                coit "Ye sly little creature, I'd had won with that hand."
                            else:
                                coit "Hah, take it. It's free fer ye."
                        elif cdg_swapping == cdg_c2:
                            "You played a watcher, and swapped your entire hand with Gato."
                            if len(cdg_c2) < len(cdg_p):
                                gato "'em stupid overpowered cards. Well, enjoy the hand while it lasts."
                            else:
                                gato "Well, ye think yev got me cornered? Think again."
                        elif cdg_swapping == cdg_c1:
                            "You played a watcher, and swapped your entire hand with Fokk ."
                            if len(cdg_c1) < len(cdg_p):
                                fokk "Ha! Yer making me sweat with this card, barely."
                            else:
                                fokk "Oi, should've kept yer hand, don't cha think?"
                        $ swapping_hand(cdg_p, cdg_swapping)
                    else:
                        "You played a watcher, and kept the hand."
                    $ cdg_swapping = None
                    $ cdg_peeking = False
                    $ cdg_hover1 = False
                    $ cdg_hover2 = False
                    $ cdg_hover3 = False
            else:
                if cdg_action == 12:
                    $ cdg_action = "Drifter"
                if stacked_card == 1:
                    "You played a [cdg_action] to add onto the pile!"
                elif stacked_card == 2:
                    "You played a pair of [cdg_action]!"
                else:
                    if stacked_card == 3:
                        $ stacked_card = "three"
                    if stacked_card == 4:
                        $ stacked_card = "four"
                    "You played [stacked_card] cards of [cdg_action] right on the pile."

                if renpy.random.random() < 0.15:
                    fokk "Not too shabby, but don't think the game's over yet."
                elif renpy.random.random() < 0.3:
                    coit "Hmm, decent move there."
                elif renpy. random.random() < 0.45:
                    gato "Me friend, that [cdg_action] was a nice play, fer a novice like ye."





        elif _return == "Take the Pile":
            $ pp_taking_pile(cardgame_deck, cardgame_pile, cdg_p)
            $ cardgame_pile = []
            show screen card_game()
            if renpy.random.random() < 0.1:
                fokk "Heh, bummer isn't it, getting cozy with the party yer having in your hand?"
            elif renpy.random.random() < 0.2:
                coit "Aye, ye've got a lot to learn."
            elif renpy.random.random() < 0.3:
                coit "Haha, keep ye wits taking plates and mugs, cards' definitely not a valid option for ye."
            elif renpy.random.random() < 0.4:
                gato "Hah, now I know why we must invite ye, to take away the entire pile from us!"
            elif renpy.random.random() < 0.5:
                gato "Should've gone back to serving drinks, don't ye think?"
            "You took the entire Pile!"
            jump Card_Game_Turn

    elif cdg_turns % 4 == (cdg_seq+1)%4 and len(cdg_c1) > 0:
        $ cdg_player_turn = False
        $ cdg_doer = playing_cards(cardgame_deck, cardgame_pile, cdg_c1)
        $ cdg_stacked = cdg_doer[0]
        $ cdg_action = cdg_doer[1]
        if isinstance(cdg_action, int):
            if cdg_action == 11:
                "Fokk burnt the whole pile."
                fokk "Don't need to thank me."
                $ cardgame_pile = removeallbutburner(cardgame_pile)
            elif cdg_action == 10:
                if len(cdg_c1) == 0:
                    "Fokk plays a watcher, and finishes the game!"
                else:
                    $ chosen_peek = choosing_peek(cdg_p, cdg_c2, cdg_c3)
                    if renpy.random.random() < 0.5:
                        fokk "Fancy little combo you've got there."
                        if chosen_peek == cdg_c3:
                            "Fokk played a watcher, and decides to swap their hand with Coit!"
                            coit "Feckin Fokk , that's MY hand."
                            $ swapping_hand(cdg_c3, cdg_c1)
                        elif chosen_peek == cdg_c2:
                            "Fokk played a watcher, and decides to swap their hand with Gato!"
                            gato "Yer lucky I've perfected my hand there."
                            $ swapping_hand(cdg_c1, cdg_c2)
                        else:
                            "Fokk played a watcher, and decides to swap their hand with you!"

                            $ swapping_hand(cdg_c1, cdg_p)
                    else:
                        fokk "Heh, keep ye hand."
                        if chosen_peek == cdg_c3:
                            "Fokk played a watcher, and decides not to swap their hand with Coit!"
                        elif chosen_peek == cdg_c2:
                            "Fokk played a watcher, and decides not to swap their hand with Gato!"
                        else:
                            "Fokk played a watcher, and decides not to swap their hand with you!"
            else:
                if cdg_action == 12:
                    $ cdg_action = "Drifter"
                if cdg_doer[0] == 1:
                    "Fokk played a card of [cdg_action]."
                elif cdg_doer[0] == 2:
                    "Fokk played a pair of [cdg_action]."
                else:
                    if cdg_stacked == 3:
                        $ cdg_stacked = "three"
                    if cdg_stacked == 4:
                        $ cdg_stacked = "four"
                    "Fokk played [cdg_stacked] cards of [cdg_action]!"
                if renpy.random.random() < 0.4:
                    fokk "Oi, take that. Didn't see this one coming didn't ye."
                elif renpy.random.random() < 0.7 and "You" not in cdg_winner:
                    fokk "Wonder if our server here can handle a little pressure, seen many a novice crumble under it, during and after the game."
        else:


            if cardgame_pile[-1] == 12:
                fokk "Damn, ye giving me headache with these drifter antics."
            elif renpy.random.random() < 0.4:
                fokk "What a shit hand I'm dealing with 'ere, but just so ye know, I've got more tricks up my sleeves."
            $ cardgame_pile = []
            "Fokk took the whole pile!"

            jump Card_Game_Turn
    elif cdg_turns % 4 == (cdg_seq+2)%4 and len(cdg_c2) > 0:
        $ cdg_player_turn = False
        $ cdg_doer = playing_cards(cardgame_deck, cardgame_pile, cdg_c2)
        $ cdg_stacked = cdg_doer[0]
        $ cdg_action = cdg_doer[1]
        if isinstance(cdg_action, int):
            if cdg_action == 11:
                gato "I know Fokk's watchin, that card he wanted is so gone now."
                "Gato burnt the whole pile!"
                $ cardgame_pile = removeallbutburner(cardgame_pile)

            elif cdg_action == 10:
                if len(cdg_c2) == 0:
                    gato "Well, a final card for ye."
                    "Gato uses a peeker, and finishes the game!"
                else:
                    $ chosen_peek = choosing_peek(cdg_c1, cdg_p, cdg_c3)
                    if renpy.random.random() < 0.5:
                        gato "I'm taking that sweet lil hand."
                        if chosen_peek == cdg_c1:
                            "Gato played a watcher, and decides to swap their hand with Fokk !"
                            fokk "That's a bo'om of the barrel move there, Gato."
                            $ swapping_hand(cdg_c2, cdg_c1)
                        elif chosen_peek == cdg_c3:
                            "Gato played a watcher, and decides to swap their hand with Coit!"
                            coit "Ye cheeky gator and yer devious tactics. Should've done it to Fokk instead!"
                            $ swapping_hand(cdg_c3, cdg_c2)
                        else:
                            "Gato played a watcher, and decides to swap their hand with you!"
                            $ swapping_hand(cdg_c2, cdg_p)
                    else:
                        if chosen_peek == cdg_c1:
                            "Gato played a watcher, and decides not to swap their hand with Fokk !"
                        elif chosen_peek == cdg_c3:
                            "Gato played a watcher, and decides not to swap their hand with Coit!"
                        else:
                            "Gato played a watcher, and decides not to swap their hand with you!"
            else:
                if cdg_action == 12:
                    $ cdg_action = "Drifter"
                if cdg_doer[0] == 1:
                    "Gato played a card of [cdg_action]!"
                elif cdg_doer[0] == 2:
                    "Gato played a pair of [cdg_action]!"
                else:
                    if cdg_stacked == 3:
                        $ cdg_stacked = "three"
                    if cdg_stacked == 4:
                        $ cdg_stacked = "four"
                    "Gato played [cdg_stacked] cards of [cdg_action]!"
                if renpy.random.random() < 0.4:
                    gato "I've been shufflin' these cards since before you three could walk, now take this."
                elif renpy.random.random() < 0.6:
                    gato "This one is going to stink for the three of ye."
        else:

            if cardgame_pile[-1] == 12:
                gato "What a load of bullshit. Stop giving me drifters fer once."
            elif renpy.random.random() < 0.3:
                gato "The cards are fickle, me little server. I'll clean up these shit hand in no time."
            $ cardgame_pile = []

            "Gato took the whole pile!"
            jump Card_Game_Turn
    elif cdg_turns % 4 == (cdg_seq+3)%4 and len(cdg_c3) > 0:
        $ cdg_player_turn = False
        $ cdg_doer = playing_cards(cardgame_deck, cardgame_pile, cdg_c3)
        $ cdg_stacked = cdg_doer[0]
        $ cdg_action = cdg_doer[1]
        if isinstance(cdg_action, int):
            if cdg_action == 11:
                coit "Spicin things up little here, should've we?"
                "Coit burnt the whole pile!"
                $ cardgame_pile = removeallbutburner(cardgame_pile)
            elif cdg_action == 10:
                if len(cdg_c3) == 0:
                    coit "Looks like lady luck is on me side here."
                    "Coit uses a peeker, and finishes the game!"
                else:
                    $ chosen_peek = choosing_peek(cdg_c1, cdg_c2, cdg_p)
                    if renpy.random.random() < 0.5:
                        if chosen_peek == cdg_c1:
                            fokk "Well played, Coit. Take my entire hand with yer overpowered card."
                            "Coit played a watcher, and decides to swap their hand with Fokk !"
                            $ swapping_hand(cdg_c3, cdg_c1)
                        elif chosen_peek == cdg_c2:
                            gato "Ye might regret this decision, Coit."
                            "Coit played a watcher, and decides to swap their hand with Gato!"
                            $ swapping_hand(cdg_c3, cdg_c2)
                        else:
                            "Coit played a watcher, and decides to swap their hand with you!"
                            $ swapping_hand(cdg_c3, cdg_p)
                    else:
                        if chosen_peek == cdg_c1:
                            "Coit played a watcher, and decides not to swap their hand with Fokk !"
                        elif chosen_peek == cdg_c2:
                            "Coit played a watcher, and decides not to swap their hand with Gato!"
                        else:
                            "Coit played a watcher, and decides not to swap their hand with you!"
            else:
                if cdg_action == 12:
                    $ cdg_action = "Drifter"
                if cdg_doer[0] == 1:
                    "Coit played a card of [cdg_action] onto the pile."
                elif cdg_doer[0] == 2:
                    "Coit played a pair of [cdg_action]!"
                else:
                    if cdg_stacked == 3:
                        $ cdg_stacked = "three"
                    if cdg_stacked == 4:
                        $ cdg_stacked = "four"
                    "Coit played [cdg_stacked] cards of [cdg_action] onto the pile."
                if renpy.random.random() < 0.4:
                    coit "Let's see if ye wankers can handle this one."
                elif renpy.random.random() < 0.6:
                    coit "I've been waiting to play this card!"
        else:


            if cardgame_pile[-1] == 12:
                coit "Yer scoundrel! I swear ye're never winning with this shit move I tell ye."
            elif renpy.random.random() < 0.3:
                coit "Ugh, bet'cha my lady's going against me today. Serving a full pile o' crap right 'ere."
            $ cardgame_pile = []
            "Coit took the pile!"
            jump Card_Game_Turn

    if len(cardgame_pile) >= 4 and cardgame_pile[-1] == cardgame_pile[-2] and cardgame_pile[-1] == cardgame_pile[-3] and cardgame_pile[-1] == cardgame_pile[-4]:
        $ burnt_card = cardgame_pile[-1]
        "All 4 cards of [burnt_card] on the top created a fire! The pile is burnt now."
        $ cardgame_pile = []
    if len(cardgame_deck) != 0:
        $ drawing_card(cardgame_deck, cdg_c1, cdg_c2, cdg_c3, cdg_p)
    else:
        if len(cdg_c1) == 0 and "Fokk" not in cdg_winner:
            if len(cdg_winner) == 0:
                fokk "Ha! I told ye all, I'm the bloody king of this game! Another game claimed right in my pocket."
            elif len(cdg_winner) == 1:
                fokk "Damn it! Well, if not for the cards I'd be winning right now."
            elif len(cdg_winner) == 2:
                fokk "It must be this cursed deck! It's possessed, I tell ye."
            $ cdg_winner.append("Fokk")
        if len(cdg_c2) == 0 and "Gato" not in cdg_winner:
            if len(cdg_winner) == 0:
                gato "Aye, isn't this little server 'ere my best lucky charm, I'm winning finally."
            elif len(cdg_winner) == 1:
                gato "Bah, I was this close to bein' the champion. Next time, I'll show ye the true meanin' of defeat!"
            elif len(cdg_winner) == 2:
                gato "Almost caught me off guard, could've ended last if this disgrace of a hand ends up on our little tankard tamer 'ere."
            $ cdg_winner.append("Gato")
        if len(cdg_c3) == 0 and "Coit" not in cdg_winner:
            if len(cdg_winner) == 0:
                coit "Haha! Look at that yall! Winner's 'ere. Who needs m' lady when we 'ave best goblet smacker in the tavern, ami' right?"
            elif len(cdg_winner) == 1:
                if cdg_winner[0] != "You":
                    coit "M' lady luck's on [cdg_winner[0]]'s side today, doesn't mean I'll be one of yall losers 'ere."
                else:
                    coit "M' lady luck's on server's side today, doesn't mean I'll be one of yall losers 'ere."
            elif len(cdg_winner) == 2:
                coit "I'm blaming it on the stars, the moon, and every blasted celestial body! They were aligned against me, I swear!"
            $ cdg_winner.append("Coit")
        if len(cdg_p) == 0 and "You" not in cdg_winner:
            e "Damn, I've finished all my cards now."
            if len(cdg_winner) == 0:
                if renpy.random.random() < 0.2:
                    gato "Aint yer a lucky little beginner? I'd have sworn this game's all about luck, no skill involved at all."
                elif renpy.random.random() < 0.4:
                    fokk "Well, we gotta let Cane's favourite server's here win some games shouldn't we? I wasn't even playing seriously at all."
                elif renpy.random.random() < 0.6:
                    coit "Did ye steal my remaining luck? How are ye winning against an experienced cardslinger like me."
            $ cdg_winner.append("You")
    if len(cdg_winner) == 3:
        if "Fokk" not in cdg_winner:
            fokk "What a load of bollocks. Blame it on the server! He's clearly cloudin' me judgment..."
            $ cdg_winner.append("Fokk")
        if "Gato" not in cdg_winner:
            gato "Bloody 'ell, last again? Yer all cheating little scoundrels dealing me such a weak hand."
            $ cdg_winner.append("Gato")
        if "Coit" not in cdg_winner:
            coit "Bugger me boots, that's a total bullshit. I've never seen this shit deck before. Lemme shuffle the cards next game!"
            $ cdg_winner.append("Coit")
        if "You" not in cdg_winner:
            e "O-oh, did you all finished all your cards?"
            $ cdg_winner.append("You")
        "This round is finished."
        hide screen card_game
        show screen daytime()
        jump Nocturnal_Trunk_Cardy_End


    $ cdg_turns += 1
    jump Card_Game_Turn

label Disk_Game_Loop:

    call screen disk_game

    if disky.all_disks_stopped():
        $ disk_moving = False
        return

    jump Disk_Game_Loop

label Play_Disk_Game:
    $ disky = renpy.random.random()
    $ disky = renpy.random.random()
    $ disky = DiskGame()
    scene disk_tavern with dissolve

    show screen disk_game

    o "Alright, let me show you guys how it's done."
    "Ole throws a disk forward..."
    window hide

    $ disky.npcStartRolling(15, -0.2618, 650, 750)
    call screen disk_game
    show screen disk_game
    "His disk steers off the path very quickly."
    o "Ok, wait. That wasn't the best demonstration."
    "You can hear the wolf and the lion burst into loud laughter at the back, slapping their knees while pointing at Ole."
    s "HAHah- Is this a demonstration of what not to do? I told you [e] he's really bad at this game."
    l "Well-"
    "Lothar can't hold onto his laughter, and chuckles for another few seconds again."

    l "Even my grandfather could probably throw better than this lizard does."
    o "Hands slipped."
    o "Hey- I haven't played the game for a while, this is just a warm-up."
    s "No warm up. We're drawing a zero onto the paper."
    "Eventually you let out a slight grin, but at least Ole didn't feel bad about this."
    "He returns to stand by. And it's Lothar's turn."

    window hide

    $ disky.npcStartRolling(25, 0.1, 700+renpy.random.random()*300, 750)
    call screen disk_game
    show screen disk_game
    call Lothar_Aiming_Disk from _call_Lothar_Aiming_Disk
    "It's your turn now."
    $ disky.diskin = Disk(disky.dx, disky.dy)
    call screen disk_game
    show screen disk_game
    call Player_Aiming_Disk from _call_Player_Aiming_Disk

    s "Alright, now look at this."
    window hide

    $ disky.npcStartRolling(renpy.random.random()*15+25, ((renpy.random.random()*20-10)), renpy.random.random()*1220+300, 750)
    call screen disk_game
    show screen disk_game
    call Sebas_Aiming_Disk from _call_Sebas_Aiming_Disk
    "It's another round. and Ole prepares his disk."
    o "Alright, let's see."
    window hide


    $ disky.npcStartRolling(renpy.random.random()*15+25, ((renpy.random.random()*20-10)), renpy.random.random()*1220+300, 750)
    call screen disk_game
    show screen disk_game
    call Ole_Aiming_Disk from _call_Ole_Aiming_Disk
    "The wolf takes a beer from the table, and guzzling it down like it's water."
    l "Alright, let me show you how it's done."


    $ disky.npcStartRolling(renpy.random.random()*15+25, ((renpy.random.random()*20-10)), renpy.random.random()*1220+300, 750)
    call screen disk_game
    show screen disk_game
    call Lothar_Aiming_Disk from _call_Lothar_Aiming_Disk_1

    show screen disk_game
    "It's your turn now."
    $ disky.diskin = Disk(disky.dx, disky.dy)
    call screen disk_game
    show screen disk_game
    call Player_Aiming_Disk from _call_Player_Aiming_Disk_1
    "Sebas takes a huge gulp of the beer, before putting it down and letting out a burp."
    s "I'm going to blow that stupid Lot away with this throw."

    $ disky.npcStartRolling(renpy.random.random()*15+25, ((renpy.random.random()*20-10)), renpy.random.random()*1220+300, 750)
    call screen disk_game
    show screen disk_game
    call Sebas_Aiming_Disk from _call_Sebas_Aiming_Disk_1

    "Ole walks up to the line, and throws his last disk."


    $ disky.npcStartRolling(renpy.random.random()*15+25, ((renpy.random.random()*20-10)), renpy.random.random()*1220+300, 750)
    call screen disk_game
    show screen disk_game
    call Ole_Aiming_Disk from _call_Ole_Aiming_Disk_1

    s "Well, it's your turn now, Lothar."
    l "Mhmm, I'm calibrating my aim, lion."

    $ disky.npcStartRolling(renpy.random.random()*15+25, ((renpy.random.random()*20-10)), renpy.random.random()*1220+300, 750)
    call screen disk_game
    show screen disk_game
    call Lothar_Aiming_Disk from _call_Lothar_Aiming_Disk_2

    "It's your turn now."
    $ disky.diskin = Disk(disky.dx, disky.dy)

    call screen disk_game
    show screen disk_game
    call Player_Aiming_Disk from _call_Player_Aiming_Disk_2
    s "F-final throw, h-eh here I go..."

    $ disky.npcStartRolling(renpy.random.random()*15+25, ((renpy.random.random()*20-10)), renpy.random.random()*1220+300, 750)
    call screen disk_game
    show screen disk_game
    call Sebas_Aiming_Disk from _call_Sebas_Aiming_Disk_2

    hide screen disk_game

    return

label Sebas_Aiming_Disk:
    $ coolScore = disky.checkScore(disky.disks[len(disky.disks)-1])
    if coolScore == 5:
        "He quite easily hits the center of the board."
        if renpy.random.random() > 0.5:
            s "See... that's what I call- skill."
            l "Ugh- That's not even close to the bull's eye."
        else:
            s "Ohhhh! I'm soooo good at this. Take note, Ole."
            o "Note, taken."
    elif coolScore == 3:
        "The lion misses the center by a slight margin, he instead gets a solid 3."
        if renpy.random.random() > 0.5:
            s "Should be all good. I'm satisfied."
            e "It looked like it can hit a 5 easily."
        else:
            s "Almost! If only the floor is a little bit more slippery."
            l "It's going to slide right off like how your luck's gonna run out, lion."
    elif coolScore == 2 or coolScore == 1:
        "Sebas gets [coolScore] as he fumbles the disk."
        if renpy.random.random() > 0.5:
            l "Ha, not even close, lion."
            s "Shut up, I know what I'm doing..."
        else:
            o "Oh? Seb, you don't need to hold back. We know how well you can play."
            s "O! Stop laughing!"
    else:

        "Sebas' disk seems to stray far away... you don't even know where it went."
        if renpy.random.random() > 0.5:
            o "Where's the disk?"
            e "I think it's right there. By that patron's foot."
            s "..."
        else:
            l "How embarrassing."
            s "Sh----uttt-tt Up! I've never missed before I swear."

    return

label Ole_Aiming_Disk:
    $ coolScore = disky.checkScore(disky.disks[len(disky.disks)-1])
    if coolScore == 5:
        "Surprisingly, Ole's disk hits the center of the board."
        if renpy.random.random() > 0.5:
            o "Oh? Didn't even know how this game work."
            s "That must not be blind luck... right?"
        else:
            e "Woah, nice throw, Ole!"
            o "Haha, is this game always that easy?"
            l "Hmmph... don't push your luck, lizard."
    elif coolScore == 3:
        "The lizard gets 3 score for hitting near the bull's eye."
        if renpy.random.random() > 0.5:
            o "Ah- That's something else."
            s "Oh damn, that shot was actually quite good."
        else:
            o "Is that a 3 or a 5. I feel it can be a 5."
            l "That's not even close to 5. But I'll give you props for getting a positive score."
    elif coolScore == 2 or coolScore == 1:
        "His disk goes wide open, scoring a [coolScore]."
        if renpy.random.random() > 0.5:
            o "That's an improvement from the... demonstration."
            s "Now this is the Ole I know."
        else:
            o "I swear it was a good throw, but the disk just steers off for some reason..."
            l "And we can safely assume the problem's not the disk."
    else:
        "Ole misses again, completely."
        if renpy.random.random() > 0.5:
            s "OH MY L-ORD! He did it again! Look!"
            "Sebas gets so excited for a miss that he shakes the wolf's shoulder."
            l "Wh- Hahah- how are you soooo bad at throwing, lizard?"
        else:
            l "Heheh... You missed the bull's eye by such a small margin, lizard."
            s "I-I can't... That's the worst throw I have ever seen!"

    return

label Lothar_Aiming_Disk:
    $ coolScore = disky.checkScore(disky.disks[len(disky.disks)-1])
    if coolScore == 5:
        "With a relative amount of ease, Lothar's disk hits the center."
        if renpy.random.random() > 0.5:
            l "Ha- That's right. That's what I'm talking about."
            s "T-that doesn't even count."
            l "Cry more, lion."
        else:
            o "That was a good shot, Lothar."
            l "What can I say, another proof that the hero's skill is unfathomably superior."

    elif coolScore == 3:
        "The wolf's aim is slightly off the mark, only getting a 3."
        if renpy.random.random() > 0.5:
            l "Is this disk chipped or something, that bat must not be cleaning them more often."
            s "Hah- Now you're blaming the disk."
        else:
            l "Ugh... Must have been the wind."
            "Ole sneezes beside the defeated Lothar."
    elif coolScore == 2 or coolScore == 1:
        "Despite his boast, Lothar's disk steers off early on, only scoring a [coolScore]."
        if renpy.random.random() > 0.5:
            l "How is the floor so tilted! This game is soooo fucking bad!"
            e "I don't think it matters that much..."
            l "Yes it does!"
        else:
            s "Ha- Where did it even go!"
            l "Say that one more time and it'll go straight into your skull."
    else:
        "Lothar's disk went for a completely different direction, it lands somewhere...."
        if renpy.random.random() > 0.5:
            l "W-wait what. What just happened... Someone just cursed me."
            s "Haha- And you laughed at Ole back then."
        else:
            l "Someone touched my arm when I threw. That's wasn't where it's supposed to go!"
            e "Are you sure? We're all back here."
            l "Yes I'm fucking sure, disciple."

    return


label Player_Aiming_Disk:
    $ coolScore = disky.checkScore(disky.disks[len(disky.disks)-1])
    if coolScore == 5:
        "Your disk slides easily into the bull's eye."
        if renpy.random.random() > 0.5:
            s "W-wait, is this really your first time... That was actually good."
            l "My disciple has his talent that's boundless to mere lion."
        else:
            o "That was a good throw, [e]."
            e "I just happened to get it right this time."
    elif coolScore == 3:
        "The disk doesn't hit the center smoothly, but instead you score a solid 3."
        if renpy.random.random() > 0.5:
            e "Damn, it just touches the border."
            l "Almost there, that's why you still have something to learn from the best of the best."
        else:
            s "It's pretty good already, I'm sure Ole doesn't get this close to the target."
            o "I'm also sure Seb's gonna regret saying that when he gets a lower score than I do."
            s "Yeah, only in your dream."
    elif coolScore == 2 or coolScore == 1:
        "With the disk sliding far away from the bull's eye, you score a [coolScore]."
        if renpy.random.random() > 0.5:
            l "How did you miss that obvious angle right there! Disciple."
            o "Hey, [e] is doing pretty well for a beginner, a [coolScore] is better than nothing."
        else:
            e "W-what happened? I swear i was aiming towards... somewhere else."
            s "It was quite wide actually, I gotta practice with you more often!"
    else:

        "You miss the target, and it doesn't even seem to hit any lines."
        if renpy.random.random() > 0.5:
            s "Damn, didn't know you're as bad as Ole did, buddy!"
            l "A few more throw like this and I'm no longer your mentor... [e]. "
        else:
            o "Oh? Did your hand slip as well...?"
            e "Uhrm... probably not."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
