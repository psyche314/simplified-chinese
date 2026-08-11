


init python:

    import renpy.store as store
    import renpy.exports as renpy

    class Link(store.object):      
        pass





    class day_time:
        def __init__(self):
            self.day = 0
            self.week = 0
            self.dayofweek = weektuple[self.week]
            self.hour = 0
            self.minute = 0
            self.minutes = str(self.minute).zfill(2)
            self.hours = str(self.hour).zfill(2)
        
        def addTime(self, day, hour, minute):
            self.day += day
            self.hour += hour
            self.minute += minute
            self.passTime()
        
        def passTime(self):
            if self.minute >= 60:
                self.hour += (self.minute - (self.minute % 60)) / 60
                self.minute %= 60
            
            
            if self.hour >= 24:
                self.day += (self.hour - (self.hour % 24)) / 24
                self.hour %= 24
                
                
                self.week = int(self.day / 7)
            
            self.day = int(self.day)
            self.dayofweek = weektuple[int((self.day - 1) % 7)]
            self.minutes = str(self.minute).zfill(2)
            self.hours = str(self.hour).zfill(2)
        
        def anal(self):
            returnal = (self.day * 24 + self.hour) * 60 + self.minute
            return returnal

    class Page(Link):
        def __init__(self, bodyL, bodyR, num):
            self.bodyL = bodyL 
            self.bodyR = bodyR 
            self.num = num
        
        def addTo(self, book):
            book.content.append(self)
            book.sortPage()

    class Book(Link):
        def __init__(self, name, bg, read):
            self.content = []
            self.name = name
            self.bg = bg
            self.read = read
        
        def sortPage(self):
            okok = []
            
            while len(self.content) > 0:
                smol = self.content[0]
                for i in self.content:
                    if smol.num > i.num:
                        smol = i
                okok.append(smol)
                self.content.remove(smol)
            self.content = okok



    class CoolDown(Link):
        def __init__(self, day = 0, hour = 0, times = 0):
            self.day = day + timenow.day
            self.hour = hour + timenow.hour
            self.times = times
        
        def check(self):
            self.day += int(self.hour / 24)
            self.hour %= 24
            
            if self.day < timenow.day or (self.day == timenow.day and self.hour <= timenow.hour):
                self.day = timenow.day
                self.hour = timenow.hour
                self.times += 1
                return True
            else:
                return False

    class QuestProgress(Link):
        def __init__(self, head, requirement = None, number = None, status = False):
            self.head = head 
            self.status = status 
            self.requirement = requirement 
            self.number = number 
        
        def checkRequirement(self, array):
            if self.requirement != None:
                if isinstance(fyi(self.requirement), InventoryItem):
                    if LookForItemNumber(self.requirement, inventory) >= self.number:
                        self.status = True
                elif isinstance(self.requirement, Monster):
                    if self.requirement.win >= self.number:
                        self.status = True


    class Quest(Link):
        def __init__(self, title='no title', location = 'no location', questgiver= 'no quest giver', description='no description', status = False, progress = []):
            
            self.title = title
            self.location = location
            self.questgiver = questgiver
            self.description = description
            self.status = status
            self.completed_date = 999
            self.progress = []
            self.start_date = 0
            self.start_hour = 0
            self.completed_hour = 0
            self.discovered = False
            self.selection = None
        
        def questStart(self):
            if self.status == False:
                self.status = 2
            self.start_date = timenow.day
            self.start_hour = timenow.hour
        
        def questEnd(self):
            if self.status != False:
                self.status = True
            for checkpoint in self.progress:
                checkpoint.status = True
            self.completed_date = timenow.day
            self.completed_hour = timenow.hour
        
        def qProgress(self, pog, requirement = None, number = None):
            if is_duplicate_progress(self.progress, pog, requirement, number):
                return
            self.progress.append(QuestProgress(pog, requirement, number))
        
        def qComp(self, pog, requirement = None, number = None):
            if is_duplicate_progress(self.progress, pog, requirement, number):
                return
            if len(self.progress) > 0:
                self.progress[-1].status = True
            self.progress.append(QuestProgress(pog, requirement, number))

    def is_duplicate_progress(progress_list, pog, requirement = None, number = None):
        return len(progress_list) > 0 and progress_list[-1].head == pog and progress_list[-1].requirement == requirement and progress_list[-1].number == number

    def trim_duplicate_progress(progress_list):
        deduped = []
        for progress in progress_list:
            if len(deduped) > 0 and deduped[-1].head == progress.head and deduped[-1].requirement == progress.requirement and deduped[-1].number == progress.number:
                deduped[-1].status = progress.status
            else:
                deduped.append(progress)
        return deduped

    def trim_duplicate_entries(entries):
        deduped = []
        for entry in entries:
            if entry not in deduped:
                deduped.append(entry)
        return deduped

    def NormalizeJournalEntries():
        global activequests, completedquests, activetasks, completedtasks
        
        activequests = trim_duplicate_entries(activequests)
        completedquests = trim_duplicate_entries(completedquests)
        activetasks = trim_duplicate_entries(activetasks)
        completedtasks = trim_duplicate_entries(completedtasks)
        
        for quest in activequests + completedquests:
            if hasattr(quest, "progress"):
                quest.progress = trim_duplicate_progress(quest.progress)
        
        for task in activetasks + completedtasks:
            if hasattr(task, "progress"):
                task.progress = trim_duplicate_progress(task.progress)

    def QuestBegin(quest):
        if quest not in activequests:
            activequests.append(quest)
        quest.questStart()

    def QuestFinish(quest):
        if quest in activequests:
            activequests.remove(quest)
        if quest not in completedquests:
            completedquests.append(quest)
        
        quest.questEnd()

    def CheckQuestProgress():
        NormalizeJournalEntries()
        for quest in activequests:
            for check in quest.progress:
                check.checkRequirement(inventory)


    def LookForRecipe(recipe, array):
        throwaway = 0
        for jtem in array:
            if jtem.product == recipe:
                throwaway += 1
        if throwaway >= 1:
            return True
        else:
            return False

    class Task(Link):
        def __init__(self, title='no title', location = 'no location', questgiver= 'no quest giver', description='no description', interval = 1, reward='no reward', delivery = None, status = False):
            self.title = title
            self.location = location
            self.questgiver = questgiver
            self.description = description
            self.status = status
            self.interval = interval
            self.reward = reward
            self.completedtimes = 0
            self.completed_date = 0
            self.start_date = 0
            self.start_hour = 0
            self.progress = []
            self.completed_hour = 0
            self.delivery = delivery
            self.selection = []
        
        def taskStart(self):
            if self.status == False or self.status == True:
                self.status = 2
            self.start_date = timenow.day
            self.start_hour = timenow.hour
        
        def taskEnd(self):
            if self.status != False:
                self.status = True
            self.completed_date = timenow.day
            self.completed_hour = timenow.hour
        
        def tProgress(self, pog, requirement = None, number = None):
            if is_duplicate_progress(self.progress, pog, requirement, number):
                return
            self.progress.append(QuestProgress(pog, requirement, number))
        
        def tComp(self, pog, requirement = None, number = None):
            if is_duplicate_progress(self.progress, pog, requirement, number):
                return
            self.progress[-1].status = True
            self.progress.append(QuestProgress(pog, requirement, number))

    def TaskBegin(task):
        if task in completedtasks:
            completedtasks.remove(task)
        if task not in activetasks:
            activetasks.append(task)
        task.taskStart()

    def taskAvailable(task, preQuest):
        
        if (task.status == True and task.completed_date + task.interval < timenow.day ) or (task.status == False and task.completedtimes == 0 and preQuest.completed_date < timenow.day):
            return True
        else:
            return False

    def TaskFinish(task):
        while task in activetasks:
            activetasks.remove(task)
        if task not in completedtasks:
            completedtasks.append(task)
        task.completedtimes += 1
        task.taskEnd()

    class Skill(Link):
        def __init__(self, name='no title', cost = 0, description= 'no quest giver', img ='no description', effect = 0, level = 0, coolDown = 0, dCost = 0, dEffect = 0):
            self.name = name
            self.cost = cost
            self.effect = effect
            self.description = description
            self.img = img
            self.coolDownTimer = 0
            self.level = level
            self.dCost = dCost
            self.dEffect = dEffect
            self.coolDown = coolDown
        
        def levelUp(self):
            self.cost += self.cost_int
            self.effect += self.dEffect
            self.level += 1
            self.lvluppt -= 1

    def removeSkill(thing):
        abilities[thing] = None

    def addSkill(thing):
        if abilities[0] == None:
            if abilities[1] != thing and abilities[2] != thing:
                abilities[0] = thing
        elif abilities[1] == None:
            if abilities[0] != thing and abilities[2] != thing:
                abilities[1] = thing
        elif abilities[2] == None:
            if abilities[0] != thing and abilities[1] != thing:
                abilities[2] = thing


    class Recipe(Link):
        def __init__(self, product, comp1 = None, num1 = 0, comp2 = None, num2 = 0, comp3 = None, num3 = 0):
            self.product = product
            self.comp1 = comp1
            self.comp2 = comp2
            self.comp3 = comp3
            self.num1 = num1
            self.num2 = num2
            self.num3 = num3
        
        def checkAvailable(self):
            throwaway = 0
            if LookForItemNumber(self.comp1.img, inventory) >= self.num1:
                throwaway += 1
            if self.comp2 != None:
                if LookForItemNumber(self.comp2.img, inventory) >= self.num2:
                    throwaway += 1
            else:
                throwaway += 1
            if self.comp3 != None:
                if LookForItemNumber(self.comp3.img, inventory) >= self.num3:
                    throwaway += 1
            else:
                throwaway += 1
            if throwaway == 3:
                return True
            else:
                return False
        
        def checkMulticraftAvailable(self):
            throwaway = 0
            if LookForItemNumber(self.comp1.img, inventory) >= self.num1*2:
                throwaway += 1
            if self.comp2 != None:
                if LookForItemNumber(self.comp2.img, inventory) >= self.num2*2:
                    throwaway += 1
            else:
                throwaway += 1
            if self.comp3 != None:
                if LookForItemNumber(self.comp3.img, inventory) >= self.num3*2:
                    throwaway += 1
            else:
                throwaway += 1
            if throwaway == 3:
                return True
            else:
                return False
        
        def multicraft(self):
            
            while self.checkAvailable():
                self.craft()
        
        def craft(self):
            if self.comp1 != None:
                removeItem(self.comp1.img, inventory, self.num1)
            if self.comp2 != None:
                removeItem(self.comp2.img, inventory, self.num2)
            if self.comp3 != None:
                removeItem(self.comp3.img, inventory, self.num3)
            
            addItem(self.product.img, inventory, 1)

    class ConsumableRecipe(Recipe):
        def __init__(self, product, product_num = 0, comp1 = None, num1 = 0, comp2 = None, num2 = 0, comp3 = None, num3 = 0, formula = [], multiplier = []):
            Recipe.__init__(self, product, comp1, num1, comp2, num2, comp3, num3)
            self.product_num = product_num
            self.multiplier = multiplier
            self.formula = formula
        
        def checkAvailableLevel(self):
            throwaway = 0
            if LookForItemNumber(self.product.img, inventory) >= self.product_num:
                throwaway += 1
            if LookForItemNumber(self.comp1.img, inventory) >= self.num1:
                throwaway += 1
            if self.comp2 != None:
                if LookForItemNumber(self.comp2.img, inventory) >= self.num2:
                    throwaway += 1
            else:
                throwaway += 1
            if self.comp3 != None:
                if LookForItemNumber(self.comp3.img, inventory) >= self.num3:
                    throwaway += 1
            else:
                throwaway += 1
            if throwaway == 4:
                return True
            else:
                return False
        
        def levelUp(self):
            removeItem(self.product.img, inventory, self.product_num)
            self.formula[1] *= self.formula[0]
            self.product_num = int(self.product_num + self.formula[1])
            if self.comp1 != None:
                removeItem(self.comp1.img, inventory, self.num1)
                self.formula[3] *= self.formula[2]
                self.num1 = int(self.num1 + self.formula[3])
            if self.comp2 != None:
                removeItem(self.comp2.img, inventory, self.num2)
                self.formula[5] *= self.formula[4]
                self.num2 = int(self.num2 + self.formula[5])
            if self.comp3 != None:
                removeItem(self.comp3.img, inventory, self.num3)
                self.formula[7] *= self.formula[6]
                self.num3 = int(self.num3 + self.formula[7])
            self.product.level += 1
            searchForItemAttr(self.product.img, "level", self.product.level)
            self.multiplier[0] *= self.multiplier[1]
            searchForItemStat(self.product.img, int(self.multiplier[0]))





    class Effect(Link):
        def __init__(self, name = None, img = None, description = None, type = None, effect = None,  max_rounds = None, rounds = None, special = False):
            self.name = name
            self.img = img
            self.description = description
            self.type = type
            self.effect = effect
            self.max_rounds = max_rounds
            self.rounds = rounds
            self.special = special
        
        def selfUpdate(self):
            if self.rounds > 0:
                self.rounds -= 1

    def cleanse(status):
        
        for i in status:
            if i.type == "N":
                i.rounds = 0

    def hasStatus(selfie, name):
        if isinstance(selfie, Monster):
            selfie = selfie.item_drop01
        if isinstance(selfie, Ally):
            selfie = selfie.status
        if isinstance(selfie, Player):
            selfie = status
        for i in selfie:
            if i.img == name.img:
                return i
        return False

    class Place(Link):
        def __init__(self, name = None, description = None, item = [], enemy = [], drop = [], discovered = False):
            self.name = name
            self.description = description
            self.discovered = discovered
            self.item = item
            self.enemy = enemy
            self.drop = drop

    def isNight():
        
        if timenow.hour > 18 or timenow.hour < 7:
            return True
        else:
            return False

    def isMidnight():
        
        if timenow.hour < 7:
            return True
        else:
            return False

    def isWeekdayNight():
        
        return timenow.day % 7 > 0 and timenow.day % 7 < 6 and isNight()

    def isDaytime():
        
        if timenow.hour >= 7 and timenow.hour < 15:
            return True
        else:
            return False

    def isWeekend():
        
        if timenow.day % 7 > 4 or timenow.day % 7 == 0:
            return True
        else:
            return False

    def isSunday():
        
        if timenow.day % 7 > 5:
            return True
        else:
            return False

    def isNaked():
        
        if pc.armor["Clothes"] == None and pc.armor["Pants"] == None:
            return True
        else:
            return False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
