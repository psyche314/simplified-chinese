init python:
    import copy
    class Trinket:
        def __init__(self,name,img,description,hint,discovered,stat=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]):
            self.name = name
            self.img = img
            self.description = description
            self.hint = hint
            self.stat = stat
            self.discovered = discovered
        
        def equip(self):
            for item in range(len(pc.trinket)):
                i = pc.trinket[item]
                if i == None:
                    k = 0
                    for j in pc.trinket:
                        if j != self:
                            k += 1
                    if k == len(pc.trinket):
                        pc.tequip(self, item)
                        tinventory.remove(self)
        
        def unequip(self):
            pc.tunequip(self)
            tinventory.append(self)
        
        def isDiscovered(self):
            return self.discovered and quest24.status == True
        
        def discover(self):
            if self not in discoveredtrinket:
                discoveredtrinket.append(self)
            self.discovered = True


    class InventoryItem:
        def __init__(self,name,img,value,description,number):
            self.img = img
            self.name = name
            self.value = value
            self.description = description
            self.number = number

    class Material(InventoryItem):
        def __init__(self,name,img,value,description,number):
            self.img = img
            self.value = value
            self.description = description
            self.number = number
            self.name = name

    class Learnable(InventoryItem):
        def __init__(self,name,img,value,description,number,scroll,learn_type):
            InventoryItem.__init__(self,name,img,value,description,number)
            self.learn_type = learn_type 
            self.scroll = scroll
        
        def learn(self):
            if self.learn_type != "Keepsake":
                if self.number > 1:
                    self.number -= 1
                else:
                    inventory.remove(self)
            
            if self.learn_type == "Recipe" and self.scroll not in discoveredrecipe:
                discoveredrecipe.append(self.scroll)
            
            if self.learn_type == "Spell" and self.scroll not in learnedabilities:
                learnedabilities.append(self.scroll)
            
            if self.learn_type == "Trinket" and self.scroll not in discoveredtrinket:
                self.scroll.discover()
            
            global selected_item
            selected_item = None





    class Consumable(InventoryItem):
        def __init__(self,name,img,value,description,number,stat=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],recipe=[],active_status = None):
            InventoryItem.__init__(self,name,img,value,description,number)
            self.stat = stat
            self.recipe = recipe
            self.level = 1
            self.active_status = active_status
        
        def addStatus(self):
            if hasattr(self, "active_status") and self.active_status != None:
                active_status = next((Status for Status in pc.active_status if Status["Status"] == self.active_status["Status"]), False)
                if active_status != False:
                    active_status["Expire Hour"] += self.active_status["Active Hour"]
                else:
                    pc.add_active_status(self.active_status)
        
        def consume(self, target):
            if self.number > 1:
                self.number -= 1
            else:
                inventory.remove(self)
            
            target.stg += self.stat[0]
            target.agi += self.stat[1]
            target.itg += self.stat[2]
            target.ten += self.stat[3]
            target.cha += self.stat[4]
            target.cor += self.stat[5]
            target.addHP(self.stat[6])
            target.max_hp += self.stat[7]
            target.addMP(self.stat[8])
            target.max_mp += self.stat[9]
            target.addLust(self.stat[10])
            target.max_lust += self.stat[11]
            target.defense += self.stat[12]
            target.lust_defense += self.stat[13]
            target.dodge += self.stat[14]
            target.lust_dodge += self.stat[15]
            target.damage += self.stat[16]
            target.lust_damage += self.stat[17]
            target.accuracy += self.stat[18]
            target.crit_chance += self.stat[19]
            target.crit_damage += self.stat[20]
            target.ext1 += self.stat[21]
            target.ext2 += self.stat[22]
            
            global selected_item
            selected_item = None
            
            self.addStatus()



    class Equipable(InventoryItem):
        def __init__(self,name,img,value,description,number,stat=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],body_layer="Body"):
            InventoryItem.__init__(self,name,img,value,description,number)
            self.body_layer = body_layer
            self.stat = stat
            self.in_equipment = False
            self.equipped_to = False
        
        def equip(self, target):
            self.in_equipment = True
            self.equipped_to = target
        
        
        
        def unequip(self):
            self.in_equipment = False
            self.equipped_to = None




    class Weapon(Equipable):
        def __init__(self,name, img, value, description, number, stat, body_layer, wpn_type):
            Equipable.__init__(self,name,img,value,description,number,stat,body_layer)
            self.wpn_type = wpn_type
        
        def equip(self,target):
            if target.weapon != None:
                target.weapon.unequip()
            Equipable.equip(self, target)
            
            target.equip_weapon(self)
            inventory.remove(self)
        
        def unequip(self):
            self.equipped_to.unequip_weapon()
            inventory.append(self)
            Equipable.unequip(self)



    class Armor(Equipable):
        def __init__(self,name, img, value,description, number,stat,body_layer,slot):
            Equipable.__init__(self,name,img,value,description,number,stat,body_layer)
            self.slot = slot
        
        def equip(self, target):
            if target.armor[self.slot] != None:
                target.armor[self.slot].unequip()
            Equipable.equip(self, target)
            target.equip_armor(self, self.slot)
            inventory.remove(self)
        
        def unequip(self):
            self.equipped_to.unequip_armor(self.slot)
            inventory.append(self)
            Equipable.unequip(self)


    class KeyItem(InventoryItem):
        def __init__(self,name, img, value, description, number):
            InventoryItem.__init__(self,name, img, 80, description, 1)

    def isStocked(item_img):
        if LookForItem(item_img, gwyddyonInventory) or LookForItem(item_img, sebasInventory) or LookForItem(item_img, storage) or LookForItem(item_img, inventory):
            return True
        else:
            return False

    def checkNoShopItem(item_img):
        if isinstance(fyi(item_img), Weapon):
            if not isStocked(item_img) and ((pc.weapon != None and pc.weapon.img != item_img) or pc.weapon == None):
                return True
            else:
                return False
        elif isinstance(fyi(item_img), Equipable):
            theslot = fyi(item_img).slot
            if not isStocked(item_img) and ((pc.armor[theslot] != None and pc.armor[theslot].img != item_img) or pc.armor[theslot] == None):
                return True
            else:
                return False
        else:
            if not isStocked(item_img):
                return True
            else:
                return False

    def romnum(num):
        returnal = []
        valueref = [1,    5,  10,  50,  100, 500, 1000, 5000]
        romanref = ["I", "V", "X", "L", "C", "D", "M", "▽"]
        while num != 0:
            for vl in reversed(range(len(romanref))):
                if vl % 2 == 1:
                    lv = vl-1
                else:
                    lv = vl
                if num >= valueref[vl]:     
                    if num < valueref[vl+1] - valueref[lv]:
                        postromnum(romanref[vl], num / valueref[vl], returnal)
                        num %= valueref[vl]
                    else:                   
                        preromnum(romanref[lv], romanref[vl+1], returnal)
                        num -= valueref[vl+1] - valueref[lv]
        
        converted_string = ""
        for i in returnal:
            converted_string += i
        return converted_string

    def preromnum(num1, num2, listy):
        listy.append(num1)
        listy.append(num2)

    def postromnum(num1, value, listy):
        for j in range(int(value)):
            listy.append(num1)


    def ApplyStatus(victim, status, rounds):
        new_status = copy.deepcopy(status)
        new_status.max_rounds = rounds
        new_status.rounds = new_status.max_rounds
        victim.append(new_status)

    def ApplyScorch(enemies, status):
        for tg in enemies:
            isScorched = next((x for x in tg.item_drop01 if x.img == "Scorched"), None)
            if isScorched == None:    
                status.effect = scorch_damage
                ApplyStatus(tg.item_drop01, status, 3)
            else:
                isScorched.rounds += 2
    def restockShopItem(item, merchant, amount):
        found_item = None
        for jtem in merchant:
            if jtem.img == item.img:
                if isinstance(item, Material) or isinstance(item, Consumable):
                    jtem.number = amount
                    found_item = "WOW"
                else:
                    found_item = jtem
                break
        
        if found_item != "WOW":
            if isinstance(item, Material) or isinstance(item, Consumable):
                new_item = copy.deepcopy(item)
                new_item.number = amount
                merchant.append(new_item) 
            else:
                for ktem in range(amount):
                    new_item = copy.deepcopy(item)
                    new_item.number = 1
                    merchant.append(new_item) 

    def callInventoryItem(item_img, slot = None):
        if slot == "Weapon":
            if not LookForItem(item_img, inventory) and ((pc.weapon != None and pc.weapon.img != item_img) or pc.weapon == None):
                return True
            else:
                return False
        elif slot != None:
            if not LookForItem(item_img, inventory) and ((pc.armor[slot] != None and pc.armor[slot].img != item_img) or pc.armor[slot] == None):
                return True
            else:
                return False
        else:
            if not LookForItem(item_img, inventory):
                return True
            else:
                return False

    def searchForItemAttr(item_img, attr, value):
        
        for inv in inventories:
            inv_item = next((x for x in inv if x.img == item_img), None)
            if inv_item != None:
                
                setattr(inv_item, attr, value)

    def searchForItemStat(item_img, value):
        
        for inv in inventories:
            inv_item = next((x for x in inv if x.img == item_img), None)
            if inv_item != None:
                fredstat = []
                for i in inv_item.stat:
                    if i != 0:
                        i += value
                    fredstat.append(i)
                setattr(inv_item, "stat", fredstat)



    def fyi(item_img):
        inv_item = next((x for x in item_dictionary if x.img == item_img), None)
        return inv_item        

    def stackMaterial(array, item, number):
        found_item = None
        for jtem in array:
            if jtem.img == item.img:
                if isinstance(jtem, Material) or isinstance(jtem, Consumable):
                    jtem.number += number
                    found_item = 0 
                else:
                    found_item = jtem 
                break
        
        if found_item == item or found_item == None:
            new_item = copy.deepcopy(item)
            new_item.number = number
            array.append(new_item)

    def whmoveItem(item, slot):
        if item == None or not isinstance(item, InventoryItem):
            return
        
        if item.number == 1:
            item.number -= 1
            inventory.remove(item)
        
        if item.number > 1:
            item.number -= 1
        
        if pillar_item[slot] != None:
            whretrieveItem(slot)
        pillar_item[slot] = item 

    def whretrieveItem(slot):
        item = pillar_item[slot]
        if item == None or not isinstance(item, InventoryItem):
            pillar_item[slot] = None
            return
        
        throwaway = 0
        
        found_item = None
        for jtem in inventory:
            if jtem.img == item.img:
                if isinstance(jtem, Material) or isinstance(jtem, Consumable):
                    jtem.number += 1
                    found_item = 0 
                else:
                    found_item = jtem 
                break
        
        if found_item == item or found_item == None:
            new_item = copy.deepcopy(item)
            new_item.number = 1
            inventory.append(new_item)
        pillar_item[slot] = None

    def isStackableItem(item):
        return isinstance(item, (Material, Consumable))

    def removeOwnedItem(item_img, number = 1, arrays = None, include_equipped = True):
        if arrays == None:
            arrays = inventories
        
        removed_count = 0
        
        while removed_count < number:
            removed_item = False
            
            for array in arrays:
                found_item = next((x for x in array if x.img == item_img), None)
                if found_item != None:
                    if isStackableItem(found_item):
                        found_item.number -= 1
                        if found_item.number <= 0:
                            array.remove(found_item)
                    else:
                        array.remove(found_item)
                    removed_item = True
                    removed_count += 1
                    break
            
            if removed_item:
                continue
            
            if include_equipped and pc.weapon != None and pc.weapon.img == item_img:
                equipped_item = pc.weapon
                equipped_item.unequip()
                if equipped_item in inventory:
                    inventory.remove(equipped_item)
                removed_count += 1
                continue
            
            if include_equipped:
                equipped_armor = next((armor for armor in pc.armor.values() if armor != None and armor.img == item_img), None)
                if equipped_armor != None:
                    equipped_armor.unequip()
                    if equipped_armor in inventory:
                        inventory.remove(equipped_armor)
                    removed_count += 1
                    continue
            
            break
        
        return removed_count

    def sellItem(item, merchant, premium, move_all = 0):
        devaluation = 1 / premium
        item_num = 1
        
        if item not in inventory:
            return
        
        if isStackableItem(item):
            if item.number == item_num or move_all:
                item_num = item.number
                inventory.remove(item)
            elif item.number > item_num:
                item.number -= item_num
        else:
            inventory.remove(item)
        
        if premium != 1:
            pc.gold += item.value*item_num
        
        if isStackableItem(item):
            found_item = next((x for x in merchant if x.img == item.img), None)
            if found_item != None:
                found_item.number += item_num
            else:
                new_item = copy.deepcopy(item)
                new_item.number = item_num
                new_item.value = int(item.value*devaluation)
                merchant.append(new_item)
        else:
            item.number = item_num
            item.value = int(item.value*devaluation)
            merchant.append(item)




    def buyItem(item, merchant, premium, move_all = 0):
        if item not in merchant:
            return
        item_num = 1
        
        if isStackableItem(item):
            if item.number == item_num or move_all:
                item_num = item.number
                merchant.remove(item)
            elif item.number > item_num:
                item.number -= item_num
        else:
            merchant.remove(item)
        
        
        if premium != 1:
            pc.gold -= item.value*item_num
        
        if isStackableItem(item):
            found_item = next((x for x in inventory if x.img == item.img), None)
            if found_item != None:
                found_item.number += item_num
            else:
                new_item = copy.deepcopy(item)
                new_item.number = item_num
                new_item.value = int(item.value*premium)
                inventory.append(new_item)
        else:
            item.number = item_num
            item.value = int(item.value*premium)
            inventory.append(item)

    def LookForItem(item_img, array):
        throwaway = 0
        for jtem in array:
            if jtem.img == item_img:
                throwaway += 1
        if throwaway >= 1:
            return True
        else:
            return False


    def NextInvPage(page):
        page += 1

    def PrevInvPage(page):
        page -= 1

    def LookForPage(book, page):
        
        for i in range(len(book.content)):
            if book.content[i] == page:
                return i

    def LookForWpnType(wpn_type, array):
        throwaway = 0
        for jtem in array:
            if isinstance(jtem, Weapon):
                if jtem.wpn_type == wpn_type:
                    throwaway += 1
        if throwaway >= 1:
            return True
        else:
            return False

    def LookForItemNumber(item_img, array):       
        if isinstance(fyi(item_img), Material) or isinstance(fyi(item_img), Consumable):
            ktem = None
            for jtem in array:
                if jtem.img == item_img:
                    ktem = jtem
            if ktem != None:
                return ktem.number
            else:
                return 0
        else:
            ktem = 0
            for jtem in array:
                if jtem.img == item_img:
                    ktem += 1
            return ktem


    def LookForItemName(item_img):
        return fyi(item_img).name 


    def LookForItemDefense(item_img, array):
        ktem = None
        for jtem in array:
            if jtem.img == item_img:
                ktem = jtem
        if ktem != None:
            return ktem.stat[13]
        else:
            return 0

    def removeAllItem(item_img):
        for inventory in inventories:
            for jtem in inventory:
                if item_img == jtem.img:
                    inventory.remove(jtem)


    def removeItem(item_img, array, number):
        for jtem in array:
            if item_img == jtem.img:
                jtem.number -= number
                if jtem.number <= 0:
                    array.remove(jtem)
                break

    def addTrinket(item, array):
        if item not in array:
            array.append(item)


    def duplicateItem(item_img, array, number = 1):
        found_item = None
        item = fyi(item_img) 
        for jtem in array:
            if jtem.img == item.img:
                if isinstance(jtem, Material) or isinstance(jtem, Consumable):
                    jtem.number += number
                    found_item = 0 
                else:
                    found_item = item 
                break
        
        if found_item == item or found_item == None:
            if isinstance(item, Consumable) and item in leveluppableconsumables:
                new_item = copy.copy(item)
            else:
                new_item = copy.deepcopy(item)
            new_item.number = number
            return new_item

    def addItem(item_img, array, number = 1, value_mult = 1):
        new_item = duplicateItem(item_img, array, number)
        if new_item != None:
            new_item.value = int(new_item.value * value_mult)
            array.append(new_item)

    def damageFormula(damage, defense):
        
        if defense == pc.defense and weepingwillow_item in pc.trinket:
            
            output = int(2 * (damage ** 2) /  (damage + defense ** 0.8))
        
        else:
            
            output = int(2 * (damage ** 2) /  (damage + defense))
        
        return output

    def SortInventory(array, sort_num = 0):
        
        if sort_num % 4 == 0:
            array.sort(key=lambda x: x.img)
        elif sort_num % 4 == 1:
            array.sort(key=lambda x: x.img, reverse=True)
        elif sort_num % 4 == 2:
            array.sort(key=lambda x: x.value, reverse=True)
        else:
            array.sort(key=lambda x: x.value)

    def CategorizeInventory(array, cate_num, sort_order):
        if cate_num % 2 == 0:
            array = sorted(array, key=lambda x: next((sort_order[c] for c in sort_order if isinstance(x, c)), float('inf')))
        else:
            array = sorted(array, key=lambda x: next((sort_order[c] for c in sort_order if isinstance(x, c)), float('inf')), reverse=True)
        return array

    def consuming(item_img, array, number):
        for jtem in array:
            if jtem.img == item_img:
                jtem.number -= number
            if jtem.number == 0:
                array.remove(jtem)

    def weightedChoice(dictionary):
        array = []
        for key in dictionary:
            for i in range(dictionary[key]):
                array.append(key)
        return renpy.random.choice(array)

    def has_active_status(status_name):
        return any(st.get("Status") == status_name for st in pc.active_status)

    def equippinginitial():
        
        for item in inventory:
            if item.img == "Tribe Loincloth" or item.img == "Tribe Necklace" or item.img == "Short Sword":
                item.equip(pc)

    def shopdeselection():
        
        if selected_shopItem != None:
            if selected_shopItem.number < 2:
                selected_shopItem = None

    def setthingstraight(mappppp):
        for j in range(len(mappppp)):
            for i in range(len(mappppp[0])):
                setattr(mappppp[j][i], "front", None)
                setattr(mappppp[j][i], "back", None)

    def hasTrinket(item_img):
        for item in pc.trinket:
            if item != None and item.img == item_img:
                return True
        for item in tinventory:
            if item != None and item.img == item_img:
                return True
        return False

    def equippedTrinket(item_img):
        for item in pc.trinket:
            if item != None and item.img == item_img:
                return True
        return False 

    def checkDuplicateRecipe(recipebook):
        new_recipebook = []
        for j in recipebook:
            nono = 0
            for i in new_recipebook:
                if i.product != j.product or i.comp1 != j.comp1 or i.num1 != j.num1:
                    nono += 1
            if nono == len(new_recipebook):
                new_recipebook.append(j)
        return new_recipebook

    def clearQuestProgress(dictionary):
        for quest in dictionary:
            
            if not hasattr(quest, "progress") or len(quest.progress) == 0:
                quest.progress = []    
            for progress in quest.progress:
                if isinstance(progress, str) or isinstance(progress, unicode):
                    quest.progress.remove(progress)

    def debugAddAllItem(inventory):
        for item in item_dictionary:
            if not LookForItem(item.img, inventory):
                addItem(item.img, inventory, 1)

    def updatePatronSeat(current_tavern, loops = 1):
        empty_seats = []
        for day in range(0, loops):
            for seat, info in current_tavern.items():
                assorted_seat = []
                current_seat = info["Current Seat"]
                info["History"].append(current_seat)
                info["Current Seat"] = None
                for i in range(min(len(info["History"]), 5)):
                    previous_seat = info["History"][-i]
                    assorted_seat.append(previous_seat)
                for patron in info["Patrons"]:
                    if patron not in assorted_seat:
                        info["Current Seat"] = patron
                if info["Current Seat"] == None:
                    info["Current Seat"] = renpy.random.choice(info["Patrons"])
                if info["Current Seat"] == "None":
                    empty_seats.append(seat)
        while len(empty_seats) > 2:
            filled_seat = renpy.random.choice(empty_seats)
            current_tavern[filled_seat]["Current Seat"] = renpy.random.choice(current_tavern[filled_seat]["Patrons"])
            empty_seats = []
            for seat, info in current_tavern.items():
                if info["Current Seat"] == "None":
                    empty_seats.append(seat)

    def dayHover(img):
        return Transform(img, matrixcolor=TintMatrix(highlight_color_day))

    def nightHover(img):
        return Transform(img, matrixcolor=TintMatrix(highlight_color_night))

    def debugUnlockAllMap():
        for map in map_atlas:
            for location in map:
                location.discovered = True

    def FixingFarmerImages():
        farmer_image_pairs = {
            "cwore": ("cwore", "ccore_empty"),
            "cwore2": ("cwore2", "ccore_empty"),
            "cwore3": ("cwore3", "ccore_empty"),
            "cwore4": ("cwore4", "ccore_empty"),
            "cwore5": ("cwore5", "ccore_empty"),
            "cwore6": ("cwore6", "ccore_empty"),
            "cwore7": ("cwore7", "ccore_empty"),
            "limestone_vein": ("limestone_vein", "limestone_empty"),
            "limestone_empty": ("limestone_vein", "limestone_empty"),
        }
        
        for farmer in mapFarmers:
            full_img = getattr(farmer, "full_img", None)
            empty_img = getattr(farmer, "empty_img", None)
            img2 = getattr(farmer, "img2", None)
            resolved_images = None
            
            for sprite_name in (full_img, farmer.img, img2, empty_img):
                if sprite_name in farmer_image_pairs:
                    resolved_images = farmer_image_pairs[sprite_name]
                    break
            
            if resolved_images != None:
                resolved_full_img, resolved_empty_img = resolved_images
                
                if not hasattr(farmer, "full_img") or farmer.full_img == "ccore_empty":
                    farmer.full_img = resolved_full_img
                
                if not hasattr(farmer, "empty_img") or farmer.empty_img == "Empty":
                    farmer.empty_img = resolved_empty_img
            
            if not hasattr(farmer, "full_img"):
                farmer.full_img = farmer.img
            
            if not hasattr(farmer, "empty_img"):
                farmer.empty_img = farmer.img
            
            if farmer.status == 1:
                farmer.img = farmer.full_img
            elif farmer.status == 0:
                farmer.img = farmer.empty_img
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
