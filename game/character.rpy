init python:

    class Battle_bg:
        def __init__(self, name, img, location):
            self.name = name
            self.img = img
            self.location = location

    class Player:
        def __init__(self, hp, mp, lust, damage, stg=3, agi=3, itg=3, ten=3, cha=3, cor=0, level=1):
            self.agi = agi
            self.itg = itg
            self.ten = ten
            self.cha = cha
            self.cor = cor
            self.stg = stg
            self.trinket = [None]
            
            self.lust = 0
            self.level = level
            self.rank = 1
            self.max_lust = 100
            self.ext1 = 0
            self.ext2 = 0
            self.gold = 50
            self.lvluppt = 0
            
            self.damage = int((self.level+self.stg)*1.5) + self.cha
            self.max_hp = 80 + 10 * self.level + 10 * self.ten
            self.max_mp = 50 + 5 * self.itg + 5 * self.level
            self.accuracy = 10 + self.agi * 2 + self.itg + self.cor / 10
            self.dodge = 10 + 3 * self.agi + self.ten
            self.defense = 15 + 4 * self.ten + 1 * self.stg
            self.lust_defense = 5 + 2*self.ten + 1 * self.itg
            self.lust_dodge = 5 + 3 * self.agi + 3*self.itg
            self.lust_damage = self.cha * 2 + self.itg + 6
            self.crit_chance = 20 + self.agi * 2
            self.crit_damage = 4 - 1.09**(15-self.agi)
            self.eqdamage = 0
            self.eqmax_lust = 0
            self.eqmax_hp = 0
            self.eqmax_mp = 0
            self.eqaccuracy = 0
            self.eqdodge = 0
            self.eqdefense = 0
            self.eqlust_defense = 0
            self.eqlust_dodge = 0
            self.eqlust_damage = 0
            self.eqcrit_chance = 0
            self.eqcrit_damage = 0
            self.hp = self.max_hp
            self.mp = self.max_mp
            
            self.exp = 0
            self.expCap = int(100*self.level**1.25-self.level*50)
            self.rep = 0
            
            self.max_jobs = 3
            self.active_status = []
            self.weapon = None
            self.weapon2 = None
            self.armor = {"Mask":None, "Clothes":None, "Pants":None, "Accessory":None, "Bccessory":None}
        
        def LevelUp(self):
            self.level += 1
            self.lvluppt += 1
            self.exp = self.exp - self.expCap
            self.expCap = int(100*self.level**1.25-self.level*50)
        
        def refresh_levelup_stats(self):
            self.damage = int((self.level+self.stg)*1.5) + self.cha + self.eqdamage
            self.max_hp = 80 + 10 * self.level + 10 * self.ten + self.eqmax_hp
            self.max_mp = 50 + 5 * self.itg + 5 * self.level + self.eqmax_mp
            self.max_lust = 100 + self.eqmax_lust
            self.accuracy = 10 + self.agi * 2 + self.itg + self.cor / 10 + self.eqaccuracy
            self.dodge = 10 + 3 * self.agi + self.ten + self.eqdodge
            self.defense = 15 + 5*self.ten + 2*self.stg + self.eqdefense
            self.lust_defense = 5 + 2*self.ten + self.itg + self.eqlust_defense
            self.lust_dodge = 5 + 3*self.agi + 3*self.itg + self.eqlust_dodge
            self.lust_damage = self.cha*2 + self.itg + 6 + self.eqlust_damage
            self.crit_chance = 20 + self.agi * 2 + self.eqcrit_chance
            self.crit_damage = 4 - 1.09**(15-self.agi) + self.eqcrit_damage
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            if self.mp > self.max_mp:
                self.mp = self.max_mp
            if self.lust > self.max_lust:
                self.lust = self.max_lust
        
        def reset_levelup_points(self):
            equipped_bonus = {"stg": 0, "agi": 0, "itg": 0, "ten": 0, "cha": 0}
            for item in [self.weapon] + list(self.armor.values()) + self.trinket:
                if item != None:
                    equipped_bonus["stg"] += item.stat[0]
                    equipped_bonus["agi"] += item.stat[1]
                    equipped_bonus["itg"] += item.stat[2]
                    equipped_bonus["ten"] += item.stat[3]
                    equipped_bonus["cha"] += item.stat[4]
            
            refunded_points = 0
            for stat_name in ("stg", "agi", "itg", "ten", "cha"):
                refunded_stat = max(0, getattr(self, stat_name) - equipped_bonus[stat_name] - 3)
                setattr(self, stat_name, getattr(self, stat_name) - refunded_stat)
                refunded_points += refunded_stat
            
            if refunded_points > 0:
                self.lvluppt += refunded_points
                self.refresh_levelup_stats()
            
            return refunded_points
        
        
        
        def addstat(self, stats):
            if stats == 1:
                self.stg += 1
            if stats == 2:
                self.agi += 1
            if stats == 3:
                self.itg += 1
            if stats == 4:
                self.ten += 1
            if stats == 5:
                self.cha += 1
            self.lvluppt -= 1
            self.refresh_levelup_stats()
            self.hp = self.max_hp
            self.mp = self.max_mp
            self.lust = 0
        
        def sleep(self):
            if self.hp < self.max_hp:
                self.hp = self.max_hp
            if self.mp < self.max_mp:
                self.mp = self.max_mp
            if self.lust > 0:
                self.lust = 0
        
        def rest(self):
            if self.hp < self.max_hp:
                self.hp += int(0.25*self.max_hp)
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            if self.mp < self.max_mp:
                self.mp +=int(0.25*self.max_mp)
            if self.mp > self.max_mp:
                self.mp = self.max_mp
            if self.lust > 0:
                self.lust -= int(0.25*self.max_lust)
            if self.lust < 0:
                self.lust = 0
        
        def restore(self, hp=0, mp=0, lust=0):
            self.hp += hp
            if self.hp >= self.max_hp:
                self.hp = self.max_hp 
            if self.hp <= 0:
                self.hp = 0 
            self.mp += mp
            if self.mp >= self.max_mp:
                self.mp = self.max_mp 
            if self.mp <= 0:
                self.mp = 0 
            self.lust += lust
            if self.lust >= self.max_lust:
                self.lust = self.max_lust 
            if self.lust <= 0:
                self.lust = 0
        
        def addHP(self, amount):
            self.hp += amount
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            if self.hp < 0:
                self.hp = 0
        
        def addMP(self, amount):
            self.mp += amount
            if self.mp > self.max_mp:
                self.mp = self.max_mp
            if self.mp < 0:
                self.mp = 0
        
        def addLust(self, amount):
            self.lust += amount
            if self.lust > self.max_lust:
                self.lust = self.max_lust
            if self.lust < 0:
                self.lust = 0
        
        def equip_weapon(self,weapon):
            if self.weapon != None:
                self.unequip_weapon()
            
            self.weapon = weapon
            self.statAdd(weapon)
        
        def unequip_weapon(self):
            if self.weapon != None:
                self.statRemove(self.weapon)
                self.weapon = None
        
        def equip_armor(self, armor, slot):
            if self.armor[slot] != None:
                self.unequip_armor(slot)
            
            self.armor[slot] = armor
            self.statAdd(armor)
        
        def tequip(self, trinket, slot):
            self.trinket[slot] = trinket
            self.trinket[slot].stat = trinket.stat
            self.statAdd(trinket)
        
        def tunequip(self, trinket):
            for item in range(len(self.trinket)):
                if self.trinket[item] == trinket:
                    self.statRemove(trinket)
                    self.trinket[item] = None
        
        
        def unequip_armor(self, slot):
            if self.armor[slot] != None:
                self.statRemove(self.armor[slot])
                self.armor[slot] = None
        
        def statAdd(self, item):
            
            self.stg += item.stat[0]
            self.agi += item.stat[1]
            self.itg += item.stat[2]
            self.ten += item.stat[3]
            self.cha += item.stat[4]
            self.cor += item.stat[5]
            self.hp += item.stat[6]
            self.eqmax_hp += item.stat[7]
            self.mp += item.stat[8]
            self.eqmax_mp += item.stat[9]
            self.lust += item.stat[10]
            self.eqmax_lust += item.stat[11]
            self.eqdefense += item.stat[12]
            self.eqlust_defense += item.stat[13]
            self.eqdodge += item.stat[14]
            self.eqlust_dodge += item.stat[15]
            self.eqdamage += item.stat[16]
            self.eqlust_damage += item.stat[17]
            self.eqaccuracy += item.stat[18]
            self.eqcrit_chance += item.stat[19]
            self.eqcrit_damage += item.stat[20]
            self.ext1 += item.stat[21]
            self.ext2 += item.stat[22]
            
            self.damage = int((self.level+self.stg)*1.5) + self.cha + self.eqdamage
            self.max_hp = 80 + 10*self.stg + 5*self.level + 5*self.ten + self.eqmax_hp
            self.max_mp = 50 + 5*self.itg + 5*self.level + self.eqmax_mp
            self.max_lust = 100 + self.eqmax_lust
            self.accuracy = 10 + self.agi * 2 + self.itg + self.cor/10 + self.eqaccuracy
            self.dodge = 10 + 3 * self.agi + self.ten + self.eqdodge
            self.defense = 15 + 5*self.ten + 2*self.stg + self.eqdefense
            self.lust_defense = 5 + 2*self.ten + self.itg + self.eqlust_defense
            self.lust_dodge = 5 + 3*self.agi + 3*self.itg + self.eqlust_dodge
            self.lust_damage = self.cha*2 + self.itg + 6 + self.eqlust_damage
            self.crit_chance = 20 + self.agi * 2 + self.eqcrit_chance
            self.crit_damage = 4 - 1.09**(15-self.agi) + self.eqcrit_damage
        
        def statRemove(self, item):
            
            self.stg -= item.stat[0]
            self.agi -= item.stat[1]
            self.itg -= item.stat[2]
            self.ten -= item.stat[3]
            self.cha -= item.stat[4]
            self.cor -= item.stat[5]
            self.hp -= item.stat[6]
            self.eqmax_hp -= item.stat[7]
            self.mp -= item.stat[8]
            self.eqmax_mp -= item.stat[9]
            self.lust -= item.stat[10]
            self.eqmax_lust -= item.stat[11]
            self.eqdefense -= item.stat[12]
            self.eqlust_defense -= item.stat[13]
            self.eqdodge -= item.stat[14]
            self.eqlust_dodge -= item.stat[15]
            self.eqdamage -= item.stat[16]
            self.eqlust_damage -= item.stat[17]
            self.eqaccuracy -= item.stat[18]
            self.eqcrit_chance -= item.stat[19]
            self.eqcrit_damage -= item.stat[20]
            self.ext1 -= item.stat[21]
            self.ext2 -= item.stat[22]
            
            self.damage = int((self.level+self.stg)*1.5) + self.cha + self.eqdamage
            self.max_hp = 80 + 10*self.stg + 5*self.level + 5*self.ten + self.eqmax_hp
            self.max_mp = 50 + 5*self.itg + 5*self.level + self.eqmax_mp
            self.max_lust = 100 + self.eqmax_lust
            self.accuracy = 10 + self.agi * 2 + self.itg + self.cor/10 + self.eqaccuracy
            self.dodge = 10 + 3 * self.agi + self.ten + self.eqdodge
            self.defense = 15 + 5*self.ten + 2*self.stg + self.eqdefense
            self.lust_defense = 5 + 2*self.ten + self.itg + self.eqlust_defense
            self.lust_dodge = 5 + 3*self.agi + 3*self.itg + self.eqlust_dodge
            self.lust_damage = self.cha*2 + self.itg + 6 + self.eqlust_damage
            self.crit_chance = 20 + self.agi * 2 + self.eqcrit_chance
            self.crit_damage = 4 - 1.09**(15-self.agi) + self.eqcrit_damage
        
        def add_active_status(self, active_status):
            expire_hour = timenow.hour + active_status["Active Hour"]
            if expire_hour > 23:
                expire_day = timenow.day + 1
                expire_hour -= 24
            else:
                expire_day = timenow.day
            appending_active_status = {"Status": active_status["Status"], "Name": active_status["Name"], "Description": active_status["Description"], "Expire Day": expire_day, "Expire Hour": expire_hour, "Expire Minute": timenow.minute}
            if "Modifiers" in active_status:
                appending_active_status["Modifiers"] = active_status["Modifiers"]
                appending_active_status["Effect Applied"] = False
            self.active_status.append(appending_active_status) 
            renpy.notify(_("You are now ") + active_status["Name"] + ".")
        
        def stripAll(self):
            if self.armor["Clothes"] != None:
                self.armor["Clothes"].unequip()
            if self.armor["Mask"] != None:
                self.armor["Mask"].unequip()
            if self.armor["Accessory"] != None:
                self.armor["Accessory"].unequip()
            if self.armor["Bccessory"] != None:
                self.armor["Bccessory"].unequip()
            if self.armor["Pants"] != None:
                self.armor["Pants"].unequip()
            if self.weapon != None:
                self.weapon.unequip()
        
        def checkEquipped(self, item_img):
            item = fyi(item_img)
            if isinstance(item, Armor):
                if self.armor[item.slot] != None and self.armor[item.slot].img == item.img:
                    return True
                else:
                    return False 
            elif isinstance(item, Weapon):
                if self.weapon != None and self.weapon.img == item.img:
                    return True
                else:
                    return False 
            else:
                return False
        
        def add_rep(self, amount):
            self.rep += amount
            self.update_rank()
        
        def get_next_rep_req(self):
            return int((self.rank) * 2 + max(self.rank - 2, 0)**1.3 + int(max(self.rank - 4, 0)**1.75*1.5)) * 5    
        
        def update_rank(self):
            while True:
                next_rep_req = self.get_next_rep_req()
                if self.rep >= next_rep_req:
                    self.rank += 1
                    self.add_rank_rewards()
                    renpy.notify(_("Your courier rank has increased to ") + str(self.rank) + "!")
                else:
                    break
        
        def add_rank_rewards(self):
            rewards = rank_up_rewards.get(self.rank, {})
            for item, number in rewards.items():
                if item == "Gold":
                    self.gold += number
                if item == "Experience":
                    self.exp += number
                    if self.exp > self.expCap and self.level <= levelCap:
                        self.LevelUp()
                        renpy.notify(_("You are now Level [self.level]! Check your inventory to allocate your level points."))
                elif item == "Level Up Point":
                    self.lvluppt += number
                elif item == "New Job Slot":
                    self.max_jobs += number
                elif item == "New Trinket Slot":
                    self.trinket.append(None)
            renpy.notify(_("You have received your rank-up rewards!"))

    class Ally:
        def __init__(self, name, img, max_hp, max_mp, max_lust, damage, lust_damage, dodge, defense, lust_defense, ext1, ext2, ext3):
            self.name = name
            self.img = img
            self.hp = max_hp
            self.max_hp = max_hp
            self.mp = max_mp
            self.max_mp = max_mp
            self.lust = 0
            self.max_lust = max_lust
            self.damage = damage 
            self.lust_damage = lust_damage
            self.defense = defense
            self.dodge = dodge
            self.lust_dodge = 0
            self.lust_defense = lust_defense
            self.ext1 = ext1 
            self.ext2 = ext2 
            self.ext3 = ext3
            self.crit_damage = 1.5
            self.crit_chance = 0.25
            self.status = []
        
        def beginbattle(self):
            self.hp = self.max_hp
            self.lust = 0
            self.item_chance01 = 0.5
            self.item_drop01 = []
        
        def restore(self, hp=0, mp=0, lust=0):
            self.hp += hp
            if self.hp >= self.max_hp:
                self.hp = self.max_hp 
            if self.hp <= 0:
                self.hp = 0 
            self.mp += mp
            if self.mp >= self.max_mp:
                self.mp = self.max_mp 
            if self.mp <= 0:
                self.mp = 0 
            self.lust += lust
            if self.lust >= self.max_lust:
                self.lust = self.max_lust 
            if self.lust <= 0:
                self.lust = 0

    class Monster:
        def __init__(self, name, img, max_hp, max_lust, min_damage, max_damage, min_lust_damage, max_lust_damage, dodge, defense, lust_defense, exp_drop, item_drop01 = None, item_chance01  = None, item_drop02  = None, item_chance02  = None, item_drop03  = None, item_chance03  = None, img2 = None, img3 = None, max_mp = 0, mp = 0):
            self.name = name
            self.img = img
            self.hp = max_hp
            self.max_hp = max_hp
            self.lust = 0
            self.max_lust = max_lust
            self.min_damage = min_damage
            self.max_damage = max_damage
            self.min_lust_damage = min_lust_damage
            self.max_lust_damage = max_lust_damage
            self.defense = defense
            self.dodge = dodge
            self.lust_dodge = 0
            self.lust_defense = lust_defense
            self.exp_drop = exp_drop
            self.item_drop01 = item_drop01
            self.item_drop02 = item_drop02
            self.item_drop03 = item_drop03
            self.item_chance01 = item_chance01
            self.item_chance02 = item_chance02
            self.item_chance03 = item_chance03
            self.img2 = img2
            self.img3 = img3
            self.max_mp = max_mp
            self.mp = mp
            self.win = 0
            self.lose = 0
        
        def beginbattle(self):
            self.hp = self.max_hp
            self.lust = 0
            self.item_drop01 = []
            self.max_mp = 100
            self.mp = self.max_mp
        
        def restore(self, hp=0, mp=0, lust=0):
            self.hp += hp
            if self.hp >= self.max_hp:
                self.hp = self.max_hp 
            if self.hp <= 0:
                self.hp = 0 
            self.mp += mp
            if self.mp >= self.max_mp:
                self.mp = self.max_mp 
            if self.mp <= 0:
                self.mp = 0 
            self.lust += lust
            if self.lust >= self.max_lust:
                self.lust = self.max_lust 
            if self.lust <= 0:
                self.lust = 0 
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
