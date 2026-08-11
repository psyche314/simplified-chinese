







default tenki_sprite9 = MapUser(10, 2, "e_dungeon", 120, 200, no_op)
default tenki_moving = True
default dungeon_timers = []

init python:

    class DungeonTimer:
        def __init__(self, time, interaction):
            self.time = time
            self.interaction = interaction


    class MapPat:
        
        def __init__(self, mappy = [], img = "", start_x = 0, start_y = 0, floor = "empty", entranceCount = 0, step = 0, playerSprite = None, inventory = None, background = None):
            self.mappy = mappy
            self.img = img
            self.center_x = start_x
            self.center_y = start_y
            self.background = background
            
            self.entranceCount = entranceCount
            self.step = step
            self.playerSprite = MapUser(start_x, start_y, "e_dungeon", 120, 200, {})
            self.inventory = inventory
            if isinstance(floor, dict):
                self.floor = floorTiling(self, floor)
            else:
                self.floor = floor
        
        def floorPlan(self, map, map_dictionary):
            floor = []
            for i in range(len(map)):
                floor.append([])
                for j in range(len(map[i])):
                    for image, value in map_dictionary.items():
                        if map[i][j] == value:
                            if image == "None":
                                floor[i].append(MapTile())
                            elif image.startswith("Back:"):
                                floor[i].append(MapTile(back = MapUser(j, i, image[5:], 120, 120, "None")))
                            else:
                                floor[i].append(MapTile(MapThing(image)))
                            break
            self.mappy = floor
            if hasattr(self, "start_x") and hasattr(self, "start_y"):
                self.setStart(self.start_x, self.start_y)
        
        def setStart(self, x, y):
            if len(self.mappy) == 0:
                return
            y = max(0, min(y, len(self.mappy) - 1))
            x = max(0, min(x, len(self.mappy[y]) - 1))
            self.center_x = x
            self.center_y = y
            self.playerSprite.x = x
            self.playerSprite.y = y
        
        def updateFloor(self, floor_dictionary):
            self.floor = floorTiling(self, floor_dictionary)
        
        def canSlide(self, offx, offy):
            x, y = sprite.x, sprite.y
            if self.mappy[y][x].back != None:
                return False
            
            if isinstance(self.floor, list):
                floor_tile = self.floor[y][x]
            else:
                floor_tile = self.floor
            
            if floor_tile not in getattr(self, "slippery_floor_tiles", ()): 
                if not isinstance(floor_tile, str):
                    return False
                sliding_here = False
                for prefix in getattr(self, "slippery_floor_prefixes", ()):
                    if floor_tile.startswith(prefix):
                        sliding_here = True
                        break
                if not sliding_here:
                    return False
            
            return self.moveCheck(x, y, offx, offy) == True
        
        def continuePlayerSlide(self, offx, offy):
            if self.canSlide(offx, offy):
                self.movingSelf(sprite.x, sprite.y, offx, offy)
                if self.canSlide(offx, offy):
                    self.sliding_direction = (offx, offy)
                    dungeon_timers.append(DungeonTimer(0.08, ("Slide", offx, offy)))
                else:
                    self.sliding_direction = None
            else:
                self.sliding_direction = None
        
        def isGhostlyInFront(self, x, y):
            tile = self.mappy[y][x]
            return hasattr(tile, "front") and tile.front != None and tile.front.interaction[:5] == "Ghost"
        
        def isInvisibleInFront(self, x, y):
            tile = self.mappy[y][x]
            return (tile.front != None and (tile.front.interaction[:9] == "Invisible")) or (tile.user != None and isinstance(tile.user, MapLooker)and tile.user.interaction[:9] == "Invisible")
        
        def isBall(self, x, y):
            if self.mappy[y][x].user != None and self.mappy[y][x].user.interaction[:4] == "Ball":
                return True
            else:
                return False
        
        def isEmpty(self, x, y):
            if (not self.isSpirit() and self.isGhostlyInFront(x, y)) or (self.isClairvoyant() and self.isInvisibleInFront(x, y)):
                return False
            if self.mappy[y][x].user == sprite:
                return False
            if self.mappy[y][x].user is None:
                
                return True
            else:
                if isPushable(self.mappy[y][x].user):
                    return True
                else:
                    return False
        
        def isEmptyFront(self, x, y):
            
            if self.mappy[y][x].front is None:
                return True
            else:
                return False
        
        def isEmptyBack(self, x, y):
            
            if self.mappy[y][x].back is None:
                return True
            else:
                return False
        
        def checkDistance(self, user, dRange):
            
            if user.direction == "Up":
                offy = -1
                offx = 0 
            elif user.direction == "Down":
                offy = 1
                offx = 0 
            elif user.direction == "Left":
                offx = -1
                offy = 0
            elif user.direction == "Right":
                offx = 1
                offy = 0
            else:
                offx = 0
                offy = 0
            
            for num in range(1, dRange):
                checker = self.mappy[user.y+offy*num][user.x+offx*num].user
                if isinstance(checker, MapThing) and not isinstance(checker, MapUser):
                    return
                
                if self.mappy[user.y+offy*num][user.x+offx*num].user == sprite:
                    global enct
                    enct = user.interaction
                    return
        
        def isSpirit(self):
            if self.inventory != None and self.inventory.interaction == "Totem Moss":
                return True
            else:
                return False
        
        def isClairvoyant(self):
            if self.inventory != None and self.inventory.interaction == "Totem Horn":
                return True
            else:
                return False
        
        def isHoldingTotem(self):
            if self.inventory != None and self.inventory.interaction[:5] == "Totem":
                return True
            else:
                return False
        
        def occupyfront(self, x, y, front):
            
            
            if self.boundaryCheck(x, y, 0, 0) != True:
                return
            self.mappy[y][x].front = front
        
        def occupyback(self, x, y, back):
            
            
            if self.boundaryCheck(x, y, 0, 0) != True:
                return
            self.mappy[y][x].back = back
        
        def occupy(self, x, y, user):
            if self.boundaryCheck(x, y, 0, 0) != True:
                return
            if not self.isEmpty(x, y):
                return
            self.mappy[y][x].user = user
        
        def unoccupyfront(self, x, y):
            if self.boundaryCheck(x, y, 0, 0) != True:
                return
            self.mappy[y][x].front = None
        
        def unoccupyback(self, x, y):
            if self.boundaryCheck(x, y, 0, 0) != True:
                return
            self.mappy[y][x].back = None
        
        def unoccupy(self, x, y):
            if self.boundaryCheck(x, y, 0, 0) != True:
                return
            self.mappy[y][x].user = None
        
        def isSprite(self, x, y):
            if self.mappy[y][x].user != None and self.mappy[y][x].user == sprite:
                return True
        
        def clearBack(self, img = None, interaction = None):
            for i in range(len(self.mappy)):
                row = self.mappy[i]
                for j in range(len(self.mappy[i])):
                    tile = row[j]
                    if interaction == None:
                        if tile.back != None and tile.back.img == img:
                            self.unoccupyback(j, i)
                    else:
                        if tile.back != None and tile.back.interaction == interaction:
                            self.unoccupyback(j, i)
                        if tile.front != None and tile.front.interaction == interaction:
                            self.unoccupyfront(j, i)
        
        def clearUser(self, img):
            for i in range(len(self.mappy)):
                row = self.mappy[i]
                for j in range(len(self.mappy[i])):
                    tile = row[j]
                    if tile.user != None and tile.user.img == img:
                        self.unoccupy(j, i)
        
        def searchUser(self, img):
            foundUser = 0
            for i in range(len(self.mappy)):
                row = self.mappy[i]
                for j in range(len(self.mappy[i])):
                    tile = row[j]
                    if tile.user != None and tile.user.img == img:
                        foundUser += 1
            
            return foundUser
        
        def searchForUser(self, img = None, interaction = None):
            foundUsers = []
            for i in range(len(self.mappy)):
                row = self.mappy[i]
                for j in range(len(self.mappy[i])):
                    tile = row[j]
                    if interaction != None:
                        if tile.user != None and tile.user.interaction == interaction:
                            foundUsers.append(tile.user)
                    else:
                        if tile.user != None and tile.user.img == img:
                            foundUsers.append(tile.user)
            
            return foundUsers
        
        def searchBack(self, img):
            foundBack = 0
            for i in range(len(self.mappy)):
                row = self.mappy[i]
                for j in range(len(self.mappy[i])):
                    tile = row[j]
                    if tile.back != None and tile.back.img == img:
                        foundBack += 1
            
            return foundBack
        
        
        def checkUsersLocation(self, users, locations):
            allUsers = users
            for user in allUsers:
                x, y = user.getLocation()
                for location in locations:
                    if (x, y) == location:
                        allUsers.remove(user)
                        allUsers.append((x, y))
            for user in allUsers:
                if isinstance(user, MapUser):
                    allUsers.remove(user)
                    allUsers.append(None)
            return allUsers
        
        def locateBackOnTop(self, sprite):
            x, y = sprite.getLocation()
            
            return self.mappy[y][x].back
        
        
        def locateBackInFront(self, sprite):
            x, y = sprite.getLocation()
            facing_x, facing_y = getFacingTile(sprite)
            if self.boundaryCheck(x, y, facing_x - x, facing_y - y) != True:
                return None
            return self.mappy[facing_y][facing_x].back
        
        def locateSpriteInFront(self, sprite):
            x, y = sprite.getLocation()
            facing_x, facing_y = getFacingTile(sprite)
            if self.boundaryCheck(x, y, facing_x - x, facing_y - y) != True:
                return None
            return self.mappy[facing_y][facing_x].user
        
        def replaceSpriteInFront(self, sprite, newSprite):
            oldSprite = self.locateSpriteInFront(sprite)
            if sprite != None:
                removeSprite(self, oldSprite)
            addedSprite = newSprite
            addedSprite.x = oldSprite.x
            addedSprite.y = oldSprite.y
            addSprite(self, addedSprite)
        
        
        def moveForward(self, x, y, offx, offy):
            newU = self.mappy[y][x].user
            self.mappy[y][x].user = None
            self.mappy[y + offy][x + offx].user = newU
            newU.x += offx
            newU.y += offy
        
        def moverMoveTo(self, x, y, offx, offy):
            
            if self.moveCheck(x, y, offx, offy) != True:
                return
            if isPushable(self.mappy[y + offy][x + offx].user):
                
                if isPushable(self.mappy[y][x].user):
                    return
                else:
                    if self.pushCheck(x, y, offx, offy) != True:
                        
                        return
                    
                    result = self.push(x, y, offx, offy)
                    if result == "Pushing":
                        return
            
            self.moveForward(x, y, offx, offy)
        
        def autoMoveLookers(self, interval = 1):
            allLookers = []
            for i in range(len(self.mappy)):
                row = self.mappy[i]
                for j in range(len(self.mappy[i])):
                    tile = row[j]
                    if tile.user != None and isinstance(tile.user, MapLooker):
                        allLookers.append(tile.user)
            for looker in allLookers:
                looker.move(self)
            global dungeon_timer_time
            dungeon_timer_time = interval
            dungeon_timers.append(DungeonTimer(interval, (0, 0)))
        
        def pushBall(self, x, y, offx, offy):
            next_x = x + offx
            next_y = y + offy
            
            if self.moveCheck(x, y, offx, offy) != True or self.isBall(next_x, next_y):
                return
            self.mappy[y][x].user.img = Transform(self.mappy[y][x].user.status, rotate = renpy.random.randint(0, 360), anchor = (0.15, 0.15))
            self.moveForward(x, y, offx, offy)
            x = next_x
            y = next_y
            
            dungeon_timers.append(DungeonTimer(0.01, (x, y, offx, offy)))
        
        def pushableMoveTo(self, x, y, offx, offy):
            if isinstance(self.mappy[y][x].user, MapMover):
                self.mappy[y][x].user.just_moved = True
            if self.mappy[y + offy][x + offx].user != None:
                
                if isPushable(self.mappy[y + offy][x + offx].user):
                    
                    return
            
            if self.mappy[y][x].user.interaction[:4] == "Ball":
                
                self.pushBall(x, y, offx, offy)
            else:
                if self.mappy[y][x].user.interaction == "Snowball":
                    global enct
                    if enct != "Snow Pit Filled":
                        enct = "Snowball"
                
                
                self.moveForward(x, y, offx, offy)
        
        def boundaryCheck(self, x, y, offx, offy):
            if y + offy >= len(self.mappy) or y + offy < 0: 
                return
            if x + offx >= len(self.mappy[y + offy]) or x + offx < 0: 
                return
            return True
        
        
        def moveCheck(self, x, y, offx, offy):
            if self.boundaryCheck(x, y, offx, offy) != True:
                return
            moving_user = self.mappy[y][x].user
            target_back = self.mappy[y + offy][x + offx].back
            if moving_user == sprite and target_back != None and target_back.interaction == "Sanctum To Hall":
                return
            if not self.isEmpty(x + offx, y + offy):  
                
                if not isinstance(moving_user, MapMover):
                    if (encounterable(self.mappy[y + offy][x + offx].user) and not encounterable(self.mappy[y][x].user)):
                        
                        global enct
                        enct = self.mappy[y + offy][x + offx].user.interaction
                        return
                    if isinstance(self.mappy[y+offy][x+offx].user, MapMover):
                        return
                return
            
            
            
            return True
        
        def pushCheck(self, x, y, offx, offy):
            
            facing_tile = self.mappy[y + offy][x + offx].user
            next_tile = self.mappy[y + offy + offy][x + offx + offx]
            next_facing_tile = next_tile.user
            if next_tile.user != None:
                next_tile_img = next_tile.user.img
            elif next_tile.front != None:
                next_tile_img = next_tile.front.img
            elif next_tile.back != None:
                next_tile_img = next_tile.back.img
            else:
                next_tile_img = None
            
            if facing_tile != None and isPushable(facing_tile): 
                if next_facing_tile != None:                 
                    if isPushable(next_facing_tile):
                        
                        return
                if not self.isEmpty(x + offx + offx, y + offy + offy) and next_tile_img != "river1":
                    if (next_tile_img != "snow_normal_pit" and next_tile_img != "snow_bonus_pit" or (isinstance(facing_tile, MapStorer) and facing_tile.status < 9)):
                        
                        return
            return True
        
        def push(self, x, y, offx, offy):
            facing_tile = self.mappy[y + offy][x + offx].user
            next_facing_tile = self.mappy[y + offy + offy][x + offx + offx].user
            
            if facing_tile != None:
                if isPushable(facing_tile): 
                    if isinstance(facing_tile, MapMover):
                        facing_tile.just_moved = True
                    
                    if facing_tile.interaction == "Snowball" and facing_tile.status >= 9:
                        if next_facing_tile != None and (next_facing_tile.img == "snow_normal_pit" or next_facing_tile.img == "snow_bonus_pit"):
                            removeSprite(self, next_facing_tile)
                            global enct
                            enct = "Snow Pit Filled"
                    self.pushableMoveTo(x+offx, y+offy, offx, offy) 
                    self.movingSelf(x, y, offx, offy) 
                    return "Pushing"
                elif next_facing_tile != None:      
                    if next_facing_tile.img == "river1":
                        
                        self.unoccupy(x+offx+offx, y+offy+offy)
                        self.pushableMoveTo(x+offx, y+offy, offx, offy)
        
        def moveTo(self, x, y, offx, offy):
            player_moved = self.mappy[y][x].user == sprite and abs(offx) + abs(offy) == 1
            if player_moved and getattr(self, "sliding_direction", None) != None:
                return
            if self.moveCheck(x, y, offx, offy) != True:
                return
            if abs(offx) <= 1 and abs(offy) <= 1:
                if self.boundaryCheck(x+offx, y+offy, offx, offy) == True:
                    
                    if self.pushCheck(x, y, offx, offy) != True:
                        return
                    
                    result = self.push(x, y, offx, offy)
                    if result == "Pushing":
                        return
            
            self.movingSelf(x, y, offx, offy)
            if player_moved and self.canSlide(offx, offy):
                self.sliding_direction = (offx, offy)
                dungeon_timers.append(DungeonTimer(0.08, ("Slide", offx, offy)))
            elif player_moved:
                self.sliding_direction = None
        
        def movingSelf(self, x, y, offx, offy):
            
            newU = self.mappy[y][x].user
            if newU == None:
                return
            if self.mappy[y][x].user == sprite and encounterable(self.mappy[y+offy][x+offx].user):
                return
            self.mappy[y][x].user = None
            self.mappy[y + offy][x + offx].user = newU
            
            newU.x += offx
            newU.y += offy
            if newU == sprite:
                global step
                step += 1
                timenow.addTime(0, 0, 1)
                
                if self.center_x == x and self.center_y == y:
                    self.center_x += offx
                    self.center_y += offy
                updateSprite(self)
        
        def getSprite(self, x, y):
            if self.mappy[y][x].user != None:
                return self.mappy[y][x].user
        
        def getBack(self, x, y):
            if self.mappy[y][x].back != None:
                return self.mappy[y][x].back.user
        
        def takeItem(self, sprite, item):
            if self.inventory != None:
                return
            if item == None:
                return
            self.inventory = item
            x = item.x
            y = item.y
            if 0 <= y < len(self.mappy) and 0 <= x < len(self.mappy[y]):
                tile = self.mappy[y][x]
                if tile.user == item:
                    self.unoccupy(x, y)
                elif tile.front == item:
                    self.unoccupyfront(x, y)
                elif tile.back == item:
                    self.unoccupyback(x, y)
        
        def passInventory(self, target_map):
            if self.inventory != None:
                target_map.inventory = self.inventory
                self.inventory = None
        
        def getMapStatus(self, num):
            return self.playerSprite.interaction.get(num, False)
        
        def getUserInteraction(self, x, y, interaction, num = 0):
            if self.mappy[y][x].user != None and isinstance(self.mappy[y][x].user.interaction, str):
                if num == 0:
                    return self.mappy[y][x].user.interaction
                elif num < 0:
                    return self.mappy[y][x].user.interaction[:num]
                elif num > 0:
                    return self.mappy[y][x].user.interaction[num:]
            else:
                return False
        
        def update_togglers(self):
            updated_toggler = []
            for row in self.mappy:
                for tile in row:
                    for thing in (tile.user, tile.back):
                        if isinstance(thing, MapToggler) and thing not in updated_toggler:
                            updated_toggler.append(thing)
                            thing.update(self)


    class MapTile:
        def __init__(self, user=None, back=None, front=None):
            self.front = front
            self.user = user
            self.back = back



    class MapThing():
        def __init__(self, img):
            self.img = img



    class MapUser(MapThing):
        def __init__(self, x, y, img, w = 120, h = 120, interaction = "None"):
            super(MapUser, self).__init__(img)
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.interaction = interaction
        
        def getOffset(self):
            return(tile_size - self.w, tile_size - self.h)
        
        def getLocation(self):
            return self.x, self.y
        
        def moveTile(self, dMap, offx, offy):
            dMap.moveTo(self.x, self.y, offx, offy)
        
        def moveToTile(self, dMap, x, y):
            dMap.moveTo(self.x, self.y, x - self.x, y - self.y)

    class MapStorer(MapUser):
        def __init__(self, x, y, img, w, h, interaction, status = 0):
            super(MapStorer, self).__init__(x, y, img, w, h, interaction)
            self.status = status

    class MapChecker(MapStorer):
        def __init__(self, x, y, img, w, h, interaction, status = 0, img2 = None):
            super(MapChecker, self).__init__(x, y, img, w, h, interaction, status)
            self.img2 = img2 
            
            def updateImage(self):
                k = self.img
                self.img = self.img2
                self.img2 = k


    class MapFarmer(MapUser):
        def __init__(self, x, y, img, w, h, interaction, day = 0, hour = 0, full_img = "Empty", empty_img = "Empty", status = 0):
            super(MapFarmer, self).__init__(x, y, img, w, h, interaction)
            self.day = day 
            self.hour = hour
            self.cooldown = CoolDown(self.day, self.hour)
            self.status = status
            self.full_img = full_img
            self.empty_img = empty_img 
        
        def update(self, dMap):
            if self.cooldown.check() and self.status == 0:
                self.status = 1
                self.img = self.full_img
        
        def reset(self):
            self.cooldown = CoolDown(self.day, self.hour)
            self.img = self.empty_img
            self.status = 0

    class MapToggler(MapUser):
        def __init__(self, x, y, img, w, h, interaction, activate_type, ref_pos, img2, status = 0):
            super(MapToggler, self).__init__(x, y, img, w, h, interaction)
            self.activate_type = activate_type
            self.ref_pos = ref_pos
            self.img2 = img2
            self.status = 0
            self.pressed_pos = 0
        
        def update(self, dMap):
            if self.activate_type == "Block":
                self.pressed_pos = 0
                for i in range(len(self.ref_pos)):
                    if dMap.mappy[self.ref_pos[i][1]][self.ref_pos[i][0]].user != None:
                        self.pressed_pos += 1
                
                if self.pressed_pos == len(self.ref_pos) and self.status == 1:
                    self.status = 0
                    if dMap.isEmpty(self.x, self.y) != True and dMap.mappy[self.y][self.x].user.img != "e_dungeon":
                        
                        removeSprite(dMap, self)
                        addBack(dMap, self)
                        
                        img3 = self.img
                        self.img = self.img2
                        self.img2 = img3
                elif self.pressed_pos != len(self.ref_pos) and self.status == 0:
                    if dMap.isEmpty(self.x, self.y) == True:
                        removeBack(dMap, self)
                        addSprite(dMap, self)
                        img3 = self.img
                        self.img = self.img2
                        self.img2 = img3
                        self.status = 1
                    elif step % 3 == 0:
                        self.status = 1


    class MapMover(MapUser):
        def __init__(self, x, y, img, w, h, interaction, cycle, lp, direction, moving = 0, death = False, steppy = 0):
            super(MapMover, self).__init__(x, y, img, w, h, interaction)
            self.moving = moving    
            self.cycle = cycle      
            self.lp = lp            
            self.direction = direction  
            self.death = death      
            self.just_moved = False
            self.steppy = steppy        
        
        def move(self, dMap):
            
            global step
            
            if self.just_moved:
                self.just_moved = False
                return
            if self.death:
                return
            
            if self.lp == 0:
                
                if dMap.moveCheck(self.x, self.y, self.direction[0], self.direction[1]) != True or isPushable(dMap.mappy[self.y + self.direction[1]][self.x + self.direction[0]].user):
                    self.direction = (-self.direction[0], -self.direction[1])
                else:
                    dMap.pushableMoveTo(self.x, self.y, self.direction[0], self.direction[1])
            
            elif self.lp < 4:
                phase = self.steppy % self.cycle
                
                do_move = False
                if   phase in (0,1): offx, offy =  1, 0
                elif phase in (3,4): offx, offy = -1, 0
                else:                 offx, offy =  0, 0  
                if phase == 2:   self.direction = 1
                elif phase == 5: self.direction = 2
                
                if offx or offy:
                    if dMap.moveCheck(self.x, self.y, offx, offy) == True:
                        dMap.moverMoveTo(self.x, self.y, offx, offy)
                        do_move = True
                    else:
                        return
                
                self.steppy = (self.steppy + 1) % self.cycle
                return
            elif self.lp < 8:
                if self.lp == 4:
                    steppy = 0
                else:
                    steppy = 4
                if step % self.cycle == (steppy % self.cycle) or step % self.cycle == (steppy+1 % self.cycle) or step % self.cycle == (steppy+2 % self.cycle): 
                    self.direction = 2
                    dMap.moveTo(self.x, self.y, 1, 0)
                if step % self.cycle == (steppy+4 % self.cycle) or step % self.cycle == (steppy+5 % self.cycle) or step % self.cycle == (steppy+6 % self.cycle):
                    self.direction = 1
                    dMap.moveTo(self.x, self.y, -1, 0)


    class MapLooker(MapUser):
        def __init__(self, x, y, img, w, h, interaction, moveSet = [], dRange = 4, base_img = "bandit_sprite", death = False):
            super(MapLooker, self).__init__(x, y, img, w, h, interaction)
            self.dRange = dRange
            self.moveSet = moveSet
            self.steppy = 0
            self.death = death
            self.base_img = base_img
            self.total = 0
            self.seq = 0
            self.order = 0
            self.preorder = 0
            self.direction = "Up"
            for order in self.moveSet:
                self.total += order[1]
        
        def updateSeq(self):
            self.order = 0
            self.preorder = 0
            for n in range(len(self.moveSet)):  
                self.order += self.moveSet[n][1]        
                if self.steppy < self.order and self.steppy >= self.preorder:
                    self.seq = n
                    self.direction = self.moveSet[self.seq][0]
                    break
                self.preorder += self.moveSet[n][1]
        
        def autoMove(self, dMap, interval = 1):
            self.move(dMap)
            offx, offy = self.getOffset()
            dungeon_timers.append(DungeonTimer(interval, (self.x, self.y, offx, offy)))
        
        def getOffset(self):
            if self.direction == "Up":
                offx = 0
                offy = -1
            elif self.direction == "Down":
                offx = 0
                offy = 1
            elif self.direction == "Left":
                offx = -1
                offy = 0
            elif self.direction == "Right":
                offx = 1
                offy = 0
            else:
                offx = 0
                offy = 0
            return (offx, offy)
        
        def move(self, dMap):
            self.updateSeq() 
            if self.direction != "No":
                self.img = self.base_img + " " + self.direction.lower()
                offx, offy = self.getOffset()
                dMap.moveTo(self.x, self.y, offx, offy)
            dMap.checkDistance(self, self.dRange)
            self.steppy += 1
            self.steppy %= self.total




    class MapChaser(MapUser):
        def __init__(self, x, y, img, w, h, interaction, dp, kp, lp, img1, img2, death = False):
            super(MapChaser, self).__init__(x, y, img, w, h, interaction)
            self.dp = dp
            self.kp = kp
            self.lp = lp
            self.img1 = img1
            self.img2 = img2
            self.death = death
            self.just_moved = False
        
        def move(self, dMap):
            if self.lp == 1 and self.death != True:
                if abs(sprite.x - self.x) + abs(sprite.y - self.y) <= 4:
                    self.img = self.img2
                    if abs(sprite.x - self.x) + abs(sprite.y - self.y) <= 1 and self.kp > 3:
                        idling = 0
                        self.kp = 3
                    if self.kp > 0:
                        if self.kp == 1:
                            self.dp[1] = e_d
                            self.kp -= 1
                        if self.kp == 2:
                            self.kp -= 1
                        if self.kp == 3:
                            if sprite.x < self.x:
                                self.dp[2] = "left"
                            elif sprite.x > self.x:
                                self.dp[2] = "right"
                            elif sprite.y < self.y:
                                self.dp[2] = "back"
                            else:
                                self.dp[2] = "front"
                            self.kp -= 1
                    else:
                        
                        self.dp[3] = self.dp[2]
                        self.dp[2] = self.dp[1]
                        self.dp[1] = e_d
                        if self.dp[3] == "back":
                            dMap.moveTo(self.x, self.y, 0, -1)
                        elif self.dp[3] == "front":
                            dMap.moveTo(self.x, self.y, 0, 1)
                        elif self.dp[3] == "left":
                            dMap.moveTo(self.x, self.y, -1, 0)
                        else:
                            dMap.moveTo(self.x, self.y, 1, 0)
                
                else:
                    self.kp = 5
                    self.img = self.img1
            
            
            if self.lp == 2 and self.death != True:
                if abs(sprite.x - self.x) + abs(sprite.y - self.y) <= 5 and self.kp < 6:
                    self.img = self.img2
                    if abs(sprite.x - self.x) + abs(sprite.y - self.y) <= 2 and self.kp > 3:
                        self.kp = 0
                    elif self.kp == 0:
                        possibleMoves = []
                        if sprite.x < self.x:
                            possibleMoves.append((-1, 0))
                        if sprite.x > self.x:
                            possibleMoves.append((1, 0))
                        if sprite.y < self.y:
                            possibleMoves.append((0, -1))
                        if sprite.y > self.y:
                            possibleMoves.append((0, 1))
                        if len(possibleMoves) == 0 or renpy.random.random() < 0.4:
                            possibleMoves = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0), (0, 0)]
                        for move in possibleMoves:
                            if dMap.isSprite(self.x + move[0], self.y + move[1]) == True:
                                possibleMoves.remove(move)
                        if len(possibleMoves) == 0:
                            return
                        chosen_move = renpy.random.choice(possibleMoves)
                        
                        self.moveTowards(dMap, chosen_move[0], chosen_move[1])
                        self.just_moved = True
                
                else:
                    self.kp = 5
                    self.img = self.img1
        
        def moveTowards(self, dMap, offx, offy):
            
            facing_tile = dMap.mappy[self.y + offy][self.x + offx].user
            
            if self.x + offx == sprite.x and self.y + offy == sprite.y:
                
                global enct
                enct = self.interaction
                
                return
            
            dMap.moveTo(self.x, self.y, offx, offy)

    def getFacingTile(sprite):
        if e_d == "front":
            return(sprite.x, sprite.y + 1)
        elif e_d == "back":
            return(sprite.x, sprite.y - 1)
        elif e_d == "left":
            return(sprite.x - 1, sprite.y)
        else:
            return(sprite.x + 1, sprite.y)

    def getTileInteraction(dMap, x, y):
        if y >= len(dMap.mappy) or y < 0:
            return "No"
        if x >= len(dMap.mappy[y]) or x < 0:
            return "No"
        
        
        targetTile = dMap.mappy[y][x].user
        if targetTile != None and targetTile != sprite and isinstance(targetTile, MapUser) and not dMap.isEmpty(x, y):
            return targetTile.interaction
        elif hasattr(dMap.mappy[y][x], "front") and dMap.mappy[y][x].front != None:
            return dMap.mappy[y][x].front.interaction
        elif dMap.mappy[y][x].back != None:
            return dMap.mappy[y][x].back.interaction
        else:
            return "No"

    def playerInteracts(dMap):
        x, y = getFacingTile(sprite)
        return getTileInteraction(dMap, x, y)

    def playerTakeInteracts(dMap):
        x, y = getFacingTile(sprite)
        interaction = getTileInteraction(dMap, x, y)
        if interaction != "No":
            return interaction
        return getTileInteraction(dMap, sprite.x, sprite.y)

    def removeFrontSprite(dMap):
        x, y = getFacingTile(sprite)
        if y >= len(dMap.mappy) or y < 0:
            return
        if x >= len(dMap.mappy[y]) or x < 0:
            return
        targetTile = dMap.mappy[y][x].user
        if targetTile != None and isinstance(targetTile, MapUser) and not dMap.isEmpty(x, y):
            removeSprite(dMap, targetTile)


    def no_op(user):
        pass

    def isPushable(user):
        if isinstance(user, MapUser):
            if user == sprite:
                return False
            if user != None and user.img == "intfigurine_sprite" or user.img == "barrel_sprite" or user.img == "slime_sprite_0" or user.img == "wolf_statue" or user.interaction[:4] == "Ball" or user.interaction == "Snowball":
                return True
        else:
            return False

    def encounterable(user):
        if user == None:
            return False
        elif user == sprite:
            return False
        elif isinstance(user, MapUser):
            if user.img == "werewolf_sprite_0" or user.img == "werewolf_sprite_1" or user.img == "werewolf_sprite_2" or user.img == "werewolf_sprite_3" or user.img == "werewolf_spritea1" or user.img == "werewolf_spritea2":
                return True
            if user.img == "slime_sprite_0" or user.img == "slime_sprite_a" or user.img == "hefty_sprite_0" or user.img == "hefty_sprite_a" or user.interaction[:5] == "Hefty":
                return True
            if isinstance(user, MapChaser) or isinstance(user, MapMover) or isinstance(user, MapLooker):
                return True
            else:
                return False



    def addSprite(dMap, sprite):
        dMap.occupy(sprite.x, sprite.y, sprite)

    def removeSprite(dMap, sprite):
        dMap.unoccupy(sprite.x, sprite.y)

    def addFront(dMap, sprite):
        dMap.occupyfront(sprite.x, sprite.y, sprite)

    def removeFront(dMap, sprite):
        dMap.unoccupyfront(sprite.x, sprite.y)

    def addBack(dMap, sprite):
        dMap.occupyback(sprite.x, sprite.y, sprite)

    def removeBack(dMap, sprite):
        dMap.unoccupyback(sprite.x, sprite.y)

    def addSpriteQuick(dMap, x, y, img, w = 120, h = 120, interaction = "None"):
        sprite = MapUser(x, y, img, w, h, interaction)
        addSprite(dMap, sprite)

    def addBackQuick(dMap, x, y, img, w = 120, h = 120, interaction = "None"):
        sprite = MapUser(x, y, img, w, h, interaction)
        addBack(dMap, sprite)

    def addFrontQuick(dMap, x, y, img, w = 120, h = 120, interaction = "None"):
        sprite = MapUser(x, y, img, w, h, interaction)
        addFront(dMap, sprite)

    def floorTiling(dMap, floor_dictionary):
        floor = []
        for i in range(len(dMap.mappy)):
            floor.append([])
            for j in range(len(dMap.mappy[i])):
                floor[i].append(weightedChoice(floor_dictionary))
        return floor



    def updateSprite(dMap):
        
        dMap.step += 1
        global tenki_moving
        tenki_moving = True
        moved = []
        
        for row in dMap.mappy:
            for tile in row:
                if tile.user != None:
                    if isinstance(tile.user, (MapMover, MapChaser)):
                        
                        if tile.user not in moved:
                            mover = tile.user
                            moved.append(mover)
                            mover.move(dMap)
                            mover.just_moved = False
                    if isinstance(tile.user, MapFarmer):
                        tile.user.update(dMap)
                if tile.back != None:
                    if isinstance(tile.back, MapFarmer):
                        tile.back.update(dMap)
        
        dMap.update_togglers()
        
        if current_location.img == "Forest Nightwatch":
            
            if step % 8 == 1 or step % 8 == 2:
                if werewolfD[0] == 0:
                    dark_forest1.moveTo(werewolf_sprite.x, werewolf_sprite.y, 1, 0)
                if werewolfD[2] == 0:
                    dark_forest1.moveTo(werewolf_sprite2.x, werewolf_sprite2.y, 1, 0)
                store.werewolf_d1 = "left"
            
            if step % 8 == 5 or step % 8 == 6:
                if werewolfD[0] == 0:
                    dark_forest1.moveTo(werewolf_sprite.x, werewolf_sprite.y, -1, 0)
                if werewolfD[2] == 0:
                    dark_forest1.moveTo(werewolf_sprite2.x, werewolf_sprite2.y, -1, 0)
                store.werewolf_d1 = "right"
            
            if step % 8 == 1 or step % 8 == 0:
                if werewolfD[1] == 0:
                    dark_forest1.moveTo(werewolf_sprite1.x, werewolf_sprite1.y, -1, 0)
                if werewolfD[3] == 0:
                    dark_forest1.moveTo(werewolf_sprite3.x, werewolf_sprite3.y, -1, 0)
                werewolf_d2 = "right"
            
            if step % 8 == 4 or step % 8 == 5:
                if werewolfD[1] == 0:
                    dark_forest1.moveTo(werewolf_sprite1.x, werewolf_sprite1.y, 1, 0)
                if werewolfD[3] == 0:
                    dark_forest1.moveTo(werewolf_sprite3.x, werewolf_sprite3.y, 1, 0)
                werewolf_d2 = "left"
        
        if current_location.img == "Split Trail":
            
            if carrot_check1.check():
                split_trail.mappy[4][2].user.img = "carrot_sprite"
            if carrot_check2.check():
                split_trail.mappy[6][5].user.img = "carrot_sprite"
            if carrot_check3.check():
                split_trail.mappy[4][6].user.img = "carrot_sprite"
            if has_agifigurine:
                global num_tulip
                num_tulip = 17 - (step - agi_num)
                if num_tulip == 0:
                    global enct
                    enct = "TulipDead"

    def ghostlyFilter(img):
        return Transform(img, matrixcolor=TintMatrix("#0affebb6") * ContrastMatrix(1.2) * InvertMatrix(0.55))

    def update_chilly_ice_cave_fronts(dMap):
        sprite = dMap.playerSprite
        front_wall_groups = [
            (6 <= sprite.x <= 12 and 1 <= sprite.y <= 2, [
                (12, 2, "cave_wall_top"), (12, 1, "cave_wall"), (11, 1, "cave_wall"),
                (10, 1, "cave_wall"), (9, 1, "cave_wall"), (8, 1, "cave_wall"),
                (7, 1, "cave_wall_top"), (6, 1, "cave_wall_top"),
            ]),
            (3 <= sprite.x <= 5 and 17 <= sprite.y <= 19, [
                (5, 19, "cave_wall_top"), (5, 18, "cave_wall"), (4, 18, "cave_wall"), (4, 17, "cave_wall"),
            ]),
            (21 <= sprite.x <= 23 and 23 <= sprite.y <= 25, [
                (21, 23, "cave_wall"), (21, 24, "cave_wall_top"),
            ]),
        ]
        for should_fade, coords in front_wall_groups:
            for x, y, base_img in coords:
                front = dMap.mappy[y][x].front
                if front != None:
                    front.img = base_img + "_half" if should_fade else base_img




define e_offset = -60

default disableC = False

default e_d = "front"

image ward_sprite_0:
    "ward_sprite"
    pause 1.25
    "ward_sprite1"
    pause 0.75
    repeat

image golem_sprite_0:
    "golem_sprite"
    pause 1.25
    "golem_sprite_1"
    pause 0.75
    repeat

image ward_sprite_1:
    "ward_sprite1"
    pause 0.75
    "ward_sprite"
    pause 1.25
    repeat

image e_dungeon = "tenki [e_d] [step % 2]"

image tenki back 1:
    "tenki_back_1"
    pause 0.15
    "tenki_back_0"
    pause 0.15


image tenki back 0:
    "tenki_back_2"
    pause 0.15
    "tenki_back_0"
    pause 0.15


image tenki front 1:
    "tenki_front_2"
    pause 0.15
    "tenki_front_0"
    pause 0.15


image tenki front 0:
    "tenki_front_1"
    pause 0.15
    "tenki_front_0"
    pause 0.15


image tenki left 1:
    "tenki_left_2"
    pause 0.15
    "tenki_left_0"
    pause 0.15


image tenki left 0:
    "tenki_left_1"
    pause 0.15
    "tenki_left_0"
    pause 0.15


image tenki right 1:
    "tenki_right_2"
    pause 0.15
    "tenki_right_0"
    pause 0.15


image tenki right 0:
    "tenki_right_1"
    pause 0.15
    "tenki_right_0"
    pause 0.15


define tile_size = 120
define grid_width = 16
define grid_height = 9

default has_figurineL = False
default has_figurineR = False
default has_agifigurine = False

default sprite = ""
default dungeon_timer_time = 0
default tenki_dungeon_image = ""
screen dungeon_map(dMap):
    $ renpy.log(dMap.img)
    if not disableC:
        for idx, timer in enumerate(dungeon_timers):
            if timer.time <= 0.1:
                timer timer.time action Return(timer.interaction), RemoveFromSet(dungeon_timers, timer)
            else:
                timer 0.05 repeat True action If(dungeon_timer_time > 0, true=SetVariable("dungeon_timer_time", dungeon_timer_time - 0.05), false=Return(timer.interaction))
    if not hasattr(dMap, "background") or dMap.background == None:
        add "#000"

    else:
        add dMap.background:
            blur 64
    $ offset_x = 1020 - (tile_size * sprite.x)
    $ offset_y = 480 - (tile_size * sprite.y)


    for i in range(sprite.y-5,sprite.y+5):
        if i >= 0 and i < len(dMap.mappy):
            $ row = dMap.mappy[i]
            for j in range(sprite.x-8,sprite.x+8):
                if j >= 0 and j < len(dMap.mappy[i]):
                    $ tile = row[j]
                    $ tile_lc_x = 120 * (j - sprite.x) + 960
                    $ tile_lc_y = 120 * (i - sprite.y) + 600
                    if isinstance(current_location, MapPat) and current_location.img == "Forgotten Sanctuary" and i < 6:
                        add "shrinefloor":
                            pos (tile_lc_x, tile_lc_y)
                    else:
                        if isinstance(dMap.floor, str):
                            add dMap.floor:
                                pos (tile_lc_x, tile_lc_y)
                        elif isinstance(dMap.floor, list):

                            add dMap.floor[i][j]:
                                pos (tile_lc_x, tile_lc_y)

    for i in range(sprite.y-5,sprite.y+5):
        if i >= 0 and i < len(dMap.mappy):
            $ row = dMap.mappy[i]
            for j in range(sprite.x-8,sprite.x+8):
                if j >= 0 and j < len(dMap.mappy[i]):
                    $ tile = row[j]
                    if not tile.back is None:
                        $ offsx, offsy = tile.back.getOffset()
                        $ tile_lc_x = 120 * (j - sprite.x) + 960 + offsx
                        $ tile_lc_y = 120 * (i - sprite.y) + 600 + offsy
                        add tile.back.img:
                            pos (tile_lc_x + offsx, tile_lc_y + offsy)

                    if not tile.user is None and isinstance(tile.user, MapThing) and not isinstance(tile.user, MapUser):
                        $ tile_lc_x = 120 * (j - sprite.x) + 960
                        $ tile_lc_y = 120 * (i - sprite.y) + 600
                        if tile.user.img == "tree1" or tile.user.img =="tree7" or tile.user.img =="tree8":
                            $ tile_lc_y -= 24
                        if tile.user.img == "puro_tree1" or tile.user.img == "puro_tree2" or tile.user.img == "puro_tree3":
                            $ tile_lc_y -= 120
                            $ tile_lc_x -= 120
                        add tile.user.img:
                            pos (tile_lc_x, tile_lc_y)

                    if not tile.user is None and isinstance(tile.user, MapUser):
                        if not tile.user.img == "e_dungeon":
                            $ offsx, offsy = tile.user.getOffset()
                            $ tile_leftCorner_x = 120 * (j - sprite.x) + 960 + offsx
                            $ tile_leftCorner_y = 120 * (i - sprite.y) + 600 + offsy
                            if not tile.user.interaction[:9] == "Invisible" or dMap.isClairvoyant():
                                add tile.user.img:
                                    pos (tile_leftCorner_x + offsx, tile_leftCorner_y + offsy)

                        else:
                            if tenki_moving == False:
                                $ tenki_dungeon_image = "tenki_" + e_d + "_0"
                            else:
                                $ tenki_dungeon_image = tile.user.img
                            if dMap.isSpirit():
                                $ tenki_dungeon_image = ghostlyFilter(tenki_dungeon_image)

                            add tenki_dungeon_image:
                                pos (1920/2+(sprite.x%2), 1080/2 - 25+(sprite.y%2))
                    if hasattr(tile, "front") and not tile.front is None:
                        $ offsx, offsy = tile.front.getOffset()
                        $ tile_lc_x = 120 * (j - sprite.x) + 960 + offsx
                        $ tile_lc_y = 120 * (i - sprite.y) + 600 + offsy
                        if not tile.front.interaction[:9] == "Invisible" or dMap.isClairvoyant():
                            add tile.front.img:
                                pos (tile_lc_x + offsx, tile_lc_y + offsy)

    if not hasattr(dMap, "background") or dMap.background == None:
        if dMap.isHoldingTotem():
            add "dungeon_spirit_cover"
        else:
            add "dungeon_cover"
    $ renpy.log(dMap.img)
    $ ksk = playerInteracts(dMap)
    $ take_ksk = playerTakeInteracts(dMap)
    $ somethingx = offset_x -  120 * 3 +60
    $ somethingy = offset_y -  120 * 10 + 60

    if has_figurineL:
        add "dungeon_frame":
            pos (1700, 100)
        add "figurine_sprite":
            pos (1700, 100)

    if has_figurineR:
        add "dungeon_frame":
            pos (1700, 250)
        add "figurine_sprite2":
            pos (1700, 250)

    if dMap.inventory != None:
        add "dungeon_frame":
            pos (1700, 250)
        add dMap.inventory.img:
            pos (1700, 250)
    $ num_agi = 18 + pc.agi - (step - agi_num) - agi_numb
    if has_agifigurine:
        if current_location.img == "Minotaur Maze" and num_agi > 0:
            add "dungeon_frame":
                pos (1700, 400)

            text "[num_agi]" xalign 0.9 yalign 0.4
            add "figurine_sprite2":
                pos (1700, 400)

        if current_location.img == "Split Trail" and num_tulip > 0:
            add "dungeon_frame":
                pos (1700, 400)

            text "[num_tulip]" xalign 0.9 yalign 0.4
            add "tulip_sprite":
                pos (1700, 400)

    if disableC == False:

        if current_location.img == "Whispering Hollow" or current_location.img == "Viscid Stream" or current_location.img == "Creek Thicket" or current_location.img == "Forgotten Sanctuary" or current_location.img == "Snowbound Summit":

            imagebutton:
                xalign 0.05
                yalign 0.95
                idle "reset_dgbutton"
                hover "reset_dgbutton_hover"
                action [Return("Restart")]

        if enct != None or (current_location.img == "Forgotten Sanctuary" or current_location.img == "Viscid Stream" or current_location.img == "Creek Thicket" or current_location.img == "Bandit's Hideout" or current_location.img == "Puro Forest" or current_location.img == "Puro Watch Post" or current_location.img == "Snowbound Summit"):
            imagebutton:
                xalign 0.875
                yalign 0.65
                idle "dungeon_up"
                hover "dungeon_up_hover"
                action [Function(dMap.moveTo, sprite.x, sprite.y, 0, -1), SetVariable("e_d", "back"), Return(enct)]

            imagebutton:
                xalign 0.875
                yalign 0.95
                idle "dungeon_down"
                hover "dungeon_down_hover"
                action [Function(dMap.moveTo, sprite.x, sprite.y, 0, 1), SetVariable("e_d", "front"), Return(enct)]

            imagebutton:
                xalign 0.8
                yalign 0.8
                idle "dungeon_left"
                hover "dungeon_left_hover"
                action [Function(dMap.moveTo, sprite.x, sprite.y, -1, 0), SetVariable("e_d", "left"), Return(enct)]

            imagebutton:
                xalign 0.95
                yalign 0.8
                idle "dungeon_right"
                hover "dungeon_right_hover"
                action [Function(dMap.moveTo, sprite.x, sprite.y, 1, 0), SetVariable("e_d", "right"), Return(enct)]

            if dMap.inventory == None:
                imagebutton:
                    xalign 0.2
                    yalign 0.9
                    idle "dungeon_take"
                    hover "dungeon_take_hover"
                    action Return("Take " + take_ksk)
            else:
                imagebutton:
                    xalign 0.2
                    yalign 0.9
                    idle "dungeon_take"
                    hover "dungeon_take_hover"
                    action Return("Drop " + dMap.inventory.interaction)

            imagebutton:
                xalign 0.125
                yalign 0.775
                idle "dungeon_explore"
                hover "dungeon_explore_hover"
                action Return(ksk)


            key "K_UP" action [Function(dMap.moveTo, sprite.x, sprite.y, 0, -1), SetVariable("e_d", "back"), Return(enct)]
            key "K_DOWN" action [Function(dMap.moveTo, sprite.x, sprite.y, 0, 1), SetVariable("e_d", "front"), Return(enct)]
            key "K_LEFT" action [Function(dMap.moveTo, sprite.x, sprite.y, -1, 0), SetVariable("e_d", "left"), Return(enct)]
            key "K_RIGHT" action [Function(dMap.moveTo, sprite.x, sprite.y, 1, 0), SetVariable("e_d", "right"), Return(enct)]
            key "w" action [Function(dMap.moveTo, sprite.x, sprite.y, 0, -1), SetVariable("e_d", "back"), Return(enct)]
            key "s" action [Function(dMap.moveTo, sprite.x, sprite.y, 0, 1), SetVariable("e_d", "front"), Return(enct)]
            key "a" action [Function(dMap.moveTo, sprite.x, sprite.y, -1, 0), SetVariable("e_d", "left"), Return(enct)]
            key "d" action [Function(dMap.moveTo, sprite.x, sprite.y, 1, 0), SetVariable("e_d", "right"), Return(enct)]

        else:

            imagebutton:
                xalign 0.875
                yalign 0.65
                idle "dungeon_up"
                hover "dungeon_up_hover"
                action [Function(dMap.moveTo, sprite.x, sprite.y, 0, -1), SetVariable("e_d", "back")]
            imagebutton:
                xalign 0.875
                yalign 0.95
                idle "dungeon_down"
                hover "dungeon_down_hover"
                action [Function(dMap.moveTo, sprite.x, sprite.y, 0, 1), SetVariable("e_d", "front")]

            imagebutton:
                xalign 0.8
                yalign 0.8
                idle "dungeon_left"
                hover "dungeon_left_hover"
                action [Function(dMap.moveTo, sprite.x, sprite.y, -1, 0), SetVariable("e_d", "left")]

            imagebutton:
                xalign 0.95
                yalign 0.8
                idle "dungeon_right"
                hover "dungeon_right_hover"
                action [Function(dMap.moveTo, sprite.x, sprite.y, 1, 0), SetVariable("e_d", "right")]

            if dMap.inventory == None:
                imagebutton:
                    xalign 0.2
                    yalign 0.9
                    idle "dungeon_take"
                    hover "dungeon_take_hover"
                    action Return("Take " + take_ksk)
            else:
                imagebutton:
                    xalign 0.2
                    yalign 0.9
                    idle "dungeon_take"
                    hover "dungeon_take_hover"
                    action Return("Drop " + dMap.inventory.interaction)

            imagebutton:
                xalign 0.125
                yalign 0.775
                idle "dungeon_explore"
                hover "dungeon_explore_hover"
                action Return(ksk)


            key "K_UP" action [Function(dMap.moveTo, sprite.x, sprite.y, 0, -1), SetVariable("e_d", "back")]
            key "K_DOWN" action [Function(dMap.moveTo, sprite.x, sprite.y, 0, 1), SetVariable("e_d", "front")]
            key "K_LEFT" action [Function(dMap.moveTo, sprite.x, sprite.y, -1, 0), SetVariable("e_d", "left")]
            key "K_RIGHT" action [Function(dMap.moveTo, sprite.x, sprite.y, 1, 0), SetVariable("e_d", "right")]

            key "w" action [Function(dMap.moveTo, sprite.x, sprite.y, 0, -1), SetVariable("e_d", "back")]
            key "s" action [Function(dMap.moveTo, sprite.x, sprite.y, 0, 1), SetVariable("e_d", "front")]
            key "a" action [Function(dMap.moveTo, sprite.x, sprite.y, -1, 0), SetVariable("e_d", "left")]
            key "d" action [Function(dMap.moveTo, sprite.x, sprite.y, 1, 0), SetVariable("e_d", "right")]
        if dMap.inventory == None:
            key "e" action Return("Take " + take_ksk)
        else:
            key "e" action Return("Drop " + dMap.inventory.interaction)
        key "K_SPACE" action Return(ksk)

    else:

        imagebutton:
            xalign 0.875
            yalign 0.65
            idle "dungeon_up"
            hover "dungeon_up_hover"
            action NullAction()

        imagebutton:
            xalign 0.875
            yalign 0.95
            idle "dungeon_down"
            hover "dungeon_down_hover"
            action NullAction()

        imagebutton:
            xalign 0.8
            yalign 0.8
            idle "dungeon_left"
            hover "dungeon_left_hover"
            action NullAction()

        imagebutton:
            xalign 0.95
            yalign 0.8
            idle "dungeon_right"
            hover "dungeon_right_hover"
            action NullAction()

        imagebutton:
            xalign 0.2
            yalign 0.9
            idle "dungeon_take"
            hover "dungeon_take_hover"
            action NullAction()

        imagebutton:
            xalign 0.125
            yalign 0.775
            idle "dungeon_explore"
            hover "dungeon_explore_hover"
            action NullAction()

        key "K_UP" action NullAction()
        key "K_DOWN" action NullAction()
        key "K_LEFT" action NullAction()
        key "K_RIGHT" action NullAction()
        key "w" action NullAction()
        key "s" action NullAction()
        key "a" action NullAction()
        key "d" action NullAction()
        key "K_SPACE" action NullAction()

    vbox:
        spacing 10
        xalign 0.9
        yalign 0.1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
