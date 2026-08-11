init python:

    persistent.passcode = "67po21opmmxr34"

    levelCap = 22

    import sys
    sys.setrecursionlimit(2000)

    def UpdatingItemDescription(inventories, pc):
        for i in inventories:
            for item in i:
                if fyi(item.img) != None and item.description != fyi(item.img).description:
                    item.description = fyi(item.img).description
        for item in pc.armor:
            if pc.armor[item] != None and fyi(pc.armor[item].img) != None and pc.armor[item].description != fyi(pc.armor[item].img).description:
                pc.armor[item].description = fyi(pc.armor[item].img).description
        
        if pc.weapon != None and fyi(pc.weapon.img) != None and pc.weapon.description != fyi(pc.weapon.img).description:
            pc.weapon.description = fyi(pc.weapon.img).description

    def UpdatingEquipmentLayer(inventories, pc):
        for i in inventories:
            for item in i:
                if fyi(item.img) != None and isinstance(item, Equipable):
                    
                    
                    item.body_layer = fyi(item.img).body_layer
        
        for item in pc.armor:
            if pc.armor[item] != None and fyi(pc.armor[item].img) != None:
                
                pc.armor[item].body_layer = fyi(pc.armor[item].img).body_layer
        
        if pc.weapon != None and fyi(pc.weapon.img) != None:
            
            pc.weapon.body_layer = fyi(pc.weapon.img).body_layer

    def DebugAddAllEquipment():
        for i in item_dictionary:
            if isinstance(i, Equipable):
                addItem(i.img, inventory, 1)


define yu = Character(_("You"), color="#ffffff", who_outlines=[ (2, "#000") ])
define e = Character("[persistent.player_name]", who_color="#ffffff", who_outlines=[ (2, "#000") ])
define loud = Character(what_size=40)
define patron = Character(_("Patron"), color="#ffffff", who_outlines=[ (2, "#000") ])
define patron2 = Character(_("Patron"), color="#888888", who_outlines=[ (2, "#000") ])
define comrade = Character(_("Crew"), color="#f9df74", who_outlines=[ (2, "#000") ])
define comrade2 = Character(_("Crew"), color="#edae49", who_outlines=[ (2, "#000") ])
define jog = Character(_("Jog"), color="#f9df74", who_outlines=[ (2, "#000") ])
define j = Character(_("Jog"), color="#f9df74", who_outlines=[ (2, "#000") ])
define amble = Character(_("Amble"), color="#ea2b1f", who_outlines=[ (2, "#000") ])
define a = Character(_("Amble"), color="#ea2b1f", who_outlines=[ (2, "#000") ])
define ja = Character(_("Jog and Amble"), color="#f9df74", who_outlines=[ (2, "#000") ])
define goatguard = Character(_("Guard"), color="#edae49", who_outlines=[ (2, "#000") ])
define goatguard2 = Character(_("Guard"), color="#f9df73", who_outlines=[ (2, "#000") ])
define bearGuard = Character(_("Bear Guard"), color="#a3bcc1", who_outlines=[ (2, "#000") ])
define bearGuard2 = Character(_("Bear Guard"), color="#8b827d", who_outlines=[ (2, "#000") ])
define bearCommander = Character(_("Bear Commander"), color="#ebd7cd", who_outlines=[ (2, "#000") ])
define bearChief = Character(_("Bear Chief"), color="#895b46", who_outlines=[ (2, "#000") ])
define gof = Character(_("Goat Officer"), color="#895b46", who_outlines=[ (2, "#000") ])
define kh = Character(_("Kaurhu"), color="#895b46", who_outlines=[ (2, "#000") ])
define gg = Character(_("Goat General"), color="#ffc857", who_outlines=[ (2, "#000") ])
define mn = Character(_("Minotaur"), color="#ffc857", who_outlines=[ (2, "#000") ])
define gt = Character(_("Goat Huntsman"), color="#f9efdf", who_outlines=[ (2, "#000") ])
define gt2 = Character(_("Goat Huntsman"), color="#d9b198", who_outlines=[ (2, "#000") ])
define gtr = Character(_("Goat Ranger"), color="#f9deb2", who_outlines=[ (2, "#000") ])
define bb = Character(_("Buggbear"), color="#f9efdf", who_outlines=[ (2, "#000") ])
define my = Character(_("???"), color="#2e294e", who_outlines=[ (2, "#000") ])

define my1 = Character(_("???"), color="#a4a0be", who_outlines=[ (2, "#000") ])
define my2 = Character(_("???"), color="#2e294e", who_outlines=[ (2, "#000") ])
define my3 = Character(_("???"), color="#544a94", who_outlines=[ (2, "#000") ])
define m2 = Character(kind=my, what_size=40)
define m3 = Character(kind=my, what_size=80)
define msg = Character("", what_color="#eeee00")
define tut = Character(_("Tutorial"), color="#ffffff", who_outlines=[ (2, "#000") ])
define ww = Character(_("Werewolf"), color="#444444", who_outlines=[ (2, "#000") ])
define ww2 = Character(_("Werewolf"), color="#272628", who_outlines=[ (2, "#000") ])
define ww3 = Character(_("Werewolf"), color="#383f3e", who_outlines=[ (2, "#000") ])
define ww4 = Character(_("Werewolf"), color="#6b6c76", who_outlines=[ (2, "#000") ])
define ww5 = Character(_("Werewolf"), color="#415145", who_outlines=[ (2, "#000") ])
define tt = Character(_("Tetto"), color="#b38175", who_outlines=[ (2, "#000") ])
define tart = Character(_("Tart"), color="#757682", who_outlines=[ (2, "#000") ])
define booky = Character(_("Book"), color="#2c6613", who_outlines=[ (2, "#000") ], what_text_align=0.5)
define s = Character(_("Sebas"), color="#edae49", who_outlines=[ (2, "#000") ])
define s2 = Character(kind=s, what_size=40, who_outlines=[ (2, "#000") ])
define s3 = Character(kind=s, what_size=20, who_outlines=[ (2, "#000") ])
define f = Character(_("Furkan"), color="#f9edcc", who_outlines=[ (2, "#000") ])
define ct = Character(_("Castor"), color="#f5e2c4", who_outlines=[ (2, "#000") ])
define h = Character(_("Haskell"), color="#f22b1f", who_outlines=[ (2, "#000") ])
define u = Character(_("Uffe"), color="#906460", who_outlines=[ (2, "#000") ])
define kg = Character(_("Guard"), color="#eb8181", who_outlines=[ (2, "#000") ])
define v = Character(_("Vurro"), color="#f9edcc", who_outlines=[ (2, "#000") ])
define vw = Character(_("Feral Werewolf"), color="#f9edcc", who_outlines=[ (2, "#000") ])
define w = Character(_("Wuldon"), color="#305ca8", who_outlines=[ (2, "#000") ])
define m = Character(_("Methis"), color="#72b3d8", who_outlines=[ (2, "#000") ])
define r = Character(_("Rahim"), color="#906460", who_outlines=[ (2, "#000") ])
define k = Character(_("Kari"), color="#ffc857", who_outlines=[ (2, "#000") ])
define o = Character(_("Ole"), color="#83da6c", who_outlines=[ (2, "#000") ])
define l = Character(_("Lothar"), color="#92939f", who_outlines=[ (2, "#000") ])
define c = Character(_("Cone"), color="#a1a281", who_outlines=[ (2, "#000") ])

define ch = Character(_("Chime"), color="#fae5d1", who_outlines=[ (2, "#000") ])
define g = Character(_("Gwyddyon"), color="#8f4fbe", who_outlines=[ (2, "#000") ])
define p = Character(_("Pirkka"), color="#db8eee", who_outlines=[ (2, "#000") ])
define d = Character(_("Daggi"), color="#ddd5c5", who_outlines=[ (2, "#000") ])
define ar = Character(_("Arthur"), color="#b06d49", who_outlines=[ (2, "#000") ])
define mo = Character(_("Moine"), color="#f9efdf", who_outlines=[ (2, "#000") ])
default hm = Character(_("Haimo"), color="#e77b6d", who_outlines=[ (2, "#000") ])

define rb = Character(_("Ribba"), color="#a48cb8", who_outlines=[ (2, "#000") ])
define tv = Character(_("Tevfik"), color="#e7cec4", who_outlines=[ (2, "#000") ])
define hz = Character(_("Hezzong"), color="#9f7c87", who_outlines=[ (2, "#000") ])
define rbd = Character(_("Speedy Bandit"), color="#7b7264", who_outlines=[ (2, "#000") ])
define sbd = Character(_("Bandit Boss"), color="#8ed3e0", who_outlines=[ (2, "#000") ])
define bd = Character(_("Bandit"), color="#c3a86d", who_outlines=[ (2, "#000") ])
define bd2 = Character(_("Bandit"), color="#bd809d", who_outlines=[ (2, "#000") ])
define bd3 = Character(_("Bandit"), color="#dbb466", who_outlines=[ (2, "#000") ])
define bd4 = Character(_("Bandit"), color="#86728b", who_outlines=[ (2, "#000") ])
define bd5 = Character(_("Bandit"), color="#8995ae", who_outlines=[ (2, "#000") ])
define gnl = Character(_("Gnoll"), color="#724e3e", who_outlines=[ (2, "#000") ])

define fokk = Character(_("Fokk"), color="#a39291", who_outlines=[ (2, "#000") ])
define coit = Character(_("Coit"), color="#c68079", who_outlines=[ (2, "#000") ])
define gato = Character(_("Gato"), color="#78957e", who_outlines=[ (2, "#000") ])


define crowd = Character(_("Crowd"), color="#f9efdf", who_outlines=[ (2, "#000") ])
define crowd2 = Character(_("Crowd"), color="#757067", who_outlines=[ (2, "#000") ])
define tavernkeeper = Character(_("Tavernkeeper"), color="#a1a281", who_outlines=[ (2, "#000") ])
define barker = Character(_("Barker"), color="#7c786b", who_outlines=[ (2, "#000") ])
define rat_patron = Character(_("Rat Patron"), color="#a39291", who_outlines=[ (2, "#000") ])
define acolyte = Character(_("Cultist"), color="#78957e", who_outlines=[ (2, "#000") ])
define snow_caretaker = Character(_("The Caretaker"), color="#757481", who_outlines=[ (2, "#000") ])
define bgless = Character("", window_background=None)

define flash = Fade(0.2, 0.0, 0.3, color='#fff')
define redflash = Fade(0.2, 0.5, 0.3, color='#e12')
define greenflash = Fade(0.2, 0.5, 0.3, color='#584')
define blueflash = Fade(0.2, 0.5, 0.3, color='#5ae')
define blackflash = Fade(0.2, 0.4, 0.3, color='#000')
define dissolveFast = Dissolve(0.3)
define dissolve2 = Dissolve(2.0)
define dissolve3 = Dissolve(3.5)
define config.default_music_volume = 0.8
define config.default_sfx_volume = 0.5
define config.default_voice_volume = 0.5
default highlight_color_day = "#45737ad5"
default highlight_color_night = "#bbf6ff"

transform flip:
    xzoom -1.0
transform flipback:
    xzoom 1.0

transform white_blue_tint:
    matrixcolor TintMatrix("#eee")
    easein 1.25 matrixcolor TintMatrix("#4af")
    easeout 1.25 matrixcolor TintMatrix("#eee")
    repeat
transform r1:
    xalign 0.95
    yalign 1.0
transform l1:
    xalign 0.05
    yalign 1.0
transform r2:
    xalign 3.05
    yalign 1.0
transform l2:
    xalign -2.05
    yalign 1.0
transform r3:
    xalign 1.15
    yalign 1.0
transform l3:
    xalign -0.15
    yalign 1.0
transform c1:
    xalign 0.5
    yalign 1.0
transform shaky:
    linear 0.05 xalign 0.45
    linear 0.05 xalign 0.55
    repeat 5

    linear 0.05 xalign 0.5

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

transform sihoulette:
    matrixcolor TintMatrix("#000000")

transform normal:
    matrixcolor IdentityMatrix()





image black = "#000"
image white = "#ffffff"
image lakewater = "#12355b"



label after_load:

    $ quest_dictionary = [quest01, quest02, quest03, quest04, quest05, quest06, quest07, quest08, quest09, quest10, quest11, quest12, quest13, quest14, quest15, quest16, quest17, quest18, quest19, quest20, quest21, quest22, quest23, quest24, quest25, quest26, quest27, quest28, quest29, quest30, quest31, quest32, quest33, quest34, quest35, quest36, quest37, quest38, quest39, quest40, quest41, quest42, quest43, quest44, quest45, quest46]

    $ task_dictionary = [task01, task02, task03, task04, task05, task06, task07]

    $ selfheal.description = _("Self Heal: {p} You can heal back a portion of your health scaling with your INT.")
    $ fortifying.description = _("Fortify: {p} Your defense is increased by a significant amount for this round.")
    $ alluringlust.description = _("Alluring Lust: {p} You can increase the effectiveness of your Flirt for 3 rounds, scaling with your INT and CHA.")
    $ corestrike.description = _("Core Strike: {p} Deal an increased amount of damage based on your INT and TEN, and stuns enemy for 1 round.")
    $ camouflage.description = _("Camouflage: {p} Increases your dodge rate scaling with your INT and AGI.")
    $ fierycharge.description = _("Fiery Charge: {p} Deal damage and burn all enemies for 3 rounds based on your INT.")
    $ resolution.description = _("Resolution: {p} Reduce your Lust based on your INT.")
    $ piercingblow.description = _("Piercing Blow: {p} At next round, you are guaranteed to hit, and critically hit your enemy with normal attack, critical damage increased based on your AGI.")

    $ selfheal.coolDownTimer = 0
    $ fortifying.coolDownTimer = 0
    $ alluringlust.coolDownTimer = 0
    $ corestrike.coolDownTimer = 0
    $ camouflage.coolDownTimer = 0
    $ fierycharge.coolDownTimer = 0
    $ resolution.coolDownTimer = 0
    $ piercingblow.coolDownTimer = 0
    $ selfheal.coolDown = 2
    $ fortifying.coolDown = 3
    $ alluringlust.coolDown = 3
    $ corestrike.coolDown = 4
    $ camouflage.coolDown = 2
    $ fierycharge.coolDown = 2
    $ resolution.coolDown = 2
    $ piercingblow.coolDown = 3

    $ e = Character("[el]", who_color="#ffffff", who_outlines=[ (2, "#000") ],image="player")
    $ persistent.player_name = el
    $ badge_item.slot = "Bccessory"
    $ tavernapron_item.img = "Torn Tavern Apron"
    if not hasattr(pc, "active_status"):
        $ pc.active_status = []
    if not hasattr(pc, "rank"):
        $ pc.rank = 1
    if not hasattr(pc, "rep"):
        $ pc.rep = 0
    if not hasattr(pc, "max_jobs"):
        $ pc.max_jobs = 3
    $ magicshowpamphlet_item.learn_type = "Special"
    $ magicshowpamphlet_item.scroll = "Magic_Show_Pamphlet"
    $ searchForItemAttr("Magic Show Pamphlet", "learn_type", "Special")
    $ searchForItemAttr("Magic Show Pamphlet", "scroll", "Magic_Show_Pamphlet")
    if quest37.status == True and vote_result >= 0 and goat_reconciliation == False:
        $ goat_reconciliation = True
    if LookForItem("Tavern Apron", inventory):
        $ tavernapronthingy = next((x for x in inventory if x.img == "Tavern Apron"), None)
        if tavernapronthingy != None and quest07.status == 3:
            $ tavernapronthingy.img = "Torn Tavern Apron"
    $ hppotionconsumablerecipe = ConsumableRecipe(hppotion_item, 2, hemp_item, 4, redberry_item, 4, crystalgem_item, 1, [1, 1.5, 1, 1.5, 1, 1.5, 1, 1.2], [6, 1.5])
    $ mppotionconsumablerecipe = ConsumableRecipe(mppotion_item, 2, herbofgrace_item, 4, blueberry_item, 4, crystalgem_item, 1, [1, 1.5, 1, 1.5, 1, 1.5, 1, 1.2], [6, 1.5])
    if not hasattr(hppotion_item, "level") or hppotion_item.recipe == [] or (hppotion_item.recipe.formula[2] / hppotion_item.recipe.formula[0] > 2):
        $ hppotion_item.level = 1
        $ searchForItemAttr("Small HP Potion", "level", 1)
        $ searchForItemAttr("Small HP Potion", "description", _("A small red potion that replenishes the user's HP for a small amount."))
        $ hppotion_item.recipe = hppotionconsumablerecipe
        $ searchForItemAttr("Small HP Potion", "recipe", hppotionconsumablerecipe)
    if not hasattr(mppotion_item, "level") or mppotion_item.recipe == [] or mppotion_item.recipe.formula[2] == 3:
        $ mppotion_item.level = 1
        $ searchForItemAttr("Small MP Potion", "description", _("A small blue potion that replenishes the user's MP for a small amount."))
        $ searchForItemAttr("Small MP Potion", "level", 1)
        $ mppotion_item.recipe = mppotionconsumablerecipe
        $ searchForItemAttr("Small MP Potion", "recipe", mppotionconsumablerecipe)
    $ orbs = Effect(_("Orbs"), "Orbs", _("Spectral Orbs: {p} Target's next attack will heal based on the number of orbs."), "P", 10, 3, 3, special = True)

    $ lindbloom_item = Trinket(_("Lindbloom"), "Lindbloom", _("A Trinket with luck effect, it will increase your chance for loot drop, but decrease luck during battle."), _("Found inside the dark forest near a cave, the trinket is kept by a mysterious creature that craves for a plant of brilliant orange."), 0, [0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0, 0,0,0,0])
    $ weepingwillow_item = Trinket(_("Weeping Willow"), "Weeping Willow", _("A Trinket that heals you each time an enemy has taken damage, but decreases the effectiveness of your defense."), _("Found near the river populated with thick moss, the trinket glows brightest at night, it can be discovered by a small curved tool that digs underwater."), 0,[0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0, 0,0,0,0])
    $ devilssnare_item = Trinket(_("Devil's Snare"), "Devils Snare", _("A Trinket that causes your normal attack to deal extra damage with your flirt, but your max lust is decreased by 15."),  _("Found around the magical pond, the trinket hidden in the pond can be summoned by a mixture of a bovine's essence and the magical flowing water."),0,[0,0,0,0,0,0, 0,0,0,0,0,-15, 0,0,0,0,0,0, 0, 0,0,0,0])
    $ eversprout_item = Trinket(_("Eversprout"), "Eversprout", _("A Trinket that heals and enhances your maximum health by every turn, but your initial health are lowered."), _("Found hidden in the forest, one must be perceptive to spot a sprout spirit's journey from the great waterfall, consecutively in four locations."),0,[0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0, 0,0,0,0])

    $ spirespike_item = Trinket(_("Spirespike"), "Spirespike", _("A Trinket that creates 5 thorns that retaliate every time you are attacked. Damage based on the amount of thorns."), _("Found in the harvesting garden, the trinket is hidden within the thorniest rose bush."), 0, [0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0, 0,0,0,0])

    $ midnightprince_item = Trinket(_("Midnight Prince"), "Midnight Prince", _("A Trinket that replaces normal attack with a trial of precision. Maximum damage is increased by 25%."), _("Found near the riverside bridge only at midnight, the trinket is revealed to those who completes a series of precision trials."), 0, [0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0, 0,0,0,0])

    $ dragonsmane_item = Trinket(_("Dragon's Mane"), "Dragon's Mane", _("A Trinket that increases normal attack by the percentage of enemy's lust, and increases your flirt by the amount of enemy's missing health."), _("Found ahead by the dragon mage, the trinket must be won over by engaging a game with the its owner."), 0, [0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0, 0,0,0,0])

    $ shiveringshard_item = Trinket(_("Shivering Shard"), "Shivering Shard", _("A Trinket that enhances your critical damage, but decreases your dodge chance every time you've critically striked."), _("Found inside the ice mountain, the trinket is discovered amongs the snowball and campfires."), 0, [0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0, 0,0.4,0,0])

    $ bruisersbite_item = Trinket(_("Bruiser's Bite"), "Bruisers Bite", _("A Trinket that enhances your damaging spells to apply 3 wounds to target enemies."), _("Found around dark well, the trinket is found by completing a hidden puzzle of barrel."), 0, [0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0, 0,0,0,0])

    $ hppotion_item = Consumable(_("Small HP Potion"), "Small HP Potion", 16, _("A small red potion that replenishes the user's HP for a small amount."), 1, [0,0,0,0,0,0,40,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], recipe=hppotionconsumablerecipe)
    $ mppotion_item = Consumable(_("Small MP Potion"), "Small MP Potion", 16, _("A small blue potion that replenishes the user's MP for a small amount."), 1, [0,0,0,0,0,0,0,0,40,0,0,0,0,0,0,0,0,0,0,0,0,0,0], recipe=mppotionconsumablerecipe)
    $ redberry_item = Consumable(_("Red Berry"), "Red Berry", 2, _("A red berry I collected from the forest area, it can recover 10 HP."), 1, [0,0,0,0,0,0,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    $ blueberry_item = Consumable(_("Blue Berry"), "Blue Berry", 2, _("A blue berry I collected from the forest area, it can recover 10 MP."), 1, [0,0,0,0,0,0,0,0,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    $ goldenberry_item = Consumable(_("Golden Berry"), "Golden Berry", 2, _("A golden berry I collected from the forest area, it reduces 5 Lust."), 1, [0,0,0,0,0,0, 0,0,0,0,-5,0, 0,0,0,0,0,0,0,0,0,0,0])
    $ strengthpotion_item = Consumable(_("Strength Potion"), "Strength Potion", 16, _("A Strength Potion that temporarily increases drinker's Damage. Drinking it off battle with increase Strength temporarily instead."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0, 0,0,0,0], active_status=mighty)
    $ green_ointment_item = Consumable(_("Green Ointment"), "Green Ointment", 20, _("An Ointment with recipe created by Ole, it can cleanse all negative effect during battle."), 1, [0,0,0,0,0,0, 80,0,80,0,-30,0, 0,0,0,0,0,0, 0, 0,0,0,0])
    $ beer_item = Consumable(_("Beer"),"Beer", 8, _("The Famous Beer from Nocturnal Trunk."), 1, [0,0,0,0,0,0, 15,0,0,0,20,0, 0,0,0,0,0,0, 0, 0,0,0,0], active_status=drunk)
    $ ale_item = Consumable(_("Ale"), "Ale", 12, _("The new addition of beer in Nocturnal Trunk."), 1, [0,0,0,0,0,0, 40,0,40,0,20,0, 0,0,0,0,0,0, 0, 0,0,0,0], active_status=drunk)
    $ topusbeer_item = Consumable(_("Topu's Beer"), "Topus Beer", 80, _("A special beer brewed by the former tavern server, Topu. Drinking it may cause the drinker to experience an odd vision."), 1, [0,0,0,0,0,0, 15,0,0,0,20,0, 0,0,0,0,0,0, 0, 0,0,0,0], active_status=buzzing)
    $ accuracypotion_item = Consumable(_("Accuracy Potion"), "Accuracy Potion", 20, _("A Potion that can increase drinker's Accuracy by 20 for 2 rounds. Drinking it off battle with increase Agility temporarily instead."), 1, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], active_status=agile)
    $ tenacitypotion_item = Consumable(_("Tenacity Potion"), "Tenacity Potion", 20, _("A Potion that can increase drinker's both defenses by 40 for 2 rounds. Drinking it off battle with increase Tenacity temporarily instead."), 1, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], active_status=tenacious)
    $ snowberry_item = Consumable(_("Snow Berry"), "Snow Berry", 14, _("A white berry collected from the snow region, its densely sweet taste and rich nutrition is a rarity in the harsh winter weather. Consuming it can recover a significant amount of HP and MP."), 1, [0,0,0,0,0,0,30,0,30,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    $ leveluppableconsumables = [hppotion_item, mppotion_item]




    $ iron_axe_item = Weapon(_("Iron Axe"), "Iron Axe", 80, _("An axe designed specifically for battles, most fighter use it for its popularity and damage."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,15,0, 0, 0,0,0,0],"Hands", "Axe")
    $ iron_sword_item = Weapon(_("Iron Sword"), "Iron Sword", 80, _("The most common type of sword among adventurers. Even the most legendary heroes bring it to battles."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,10,0, 5, 0,0,0,0], "Hands", "Axe")
    $ shortsword_item = Weapon(_("Short Sword"), "Short Sword",30, _("A short sword I brought from my Tribe."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,5,0, 2, 0,0,0,0], "Hands", "Sword")
    $ smallaxe_item = Weapon(_("Small Axe"), "Small Axe", 40, _("A small axe used for chopping woods, and probably fighting."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,7,0, 0, 0,0,0,0], "Hands", "Axe")
    $ ironscythe_item = Weapon(_("Iron Scythe"), "Iron Scythe", 60, _("A scythe best used for harvesting barley and wheat in the field."), 1, [0,0,0,0,0,0, 0,15,0,0,0,0, 0,0,0,0,8,0, 0, 0,0,0,0],"Hands", "Axe")
    $ knightlongsword_item = Weapon(_("Knight Longsword"), "Knight Longsword", 100, _("A longsword of a knight used to strike down any enemy in the battle."), 1, [2,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,15,0, 0, 0,0,0,0],"Back", "Sword")
    $ huntingbow_item = Weapon(_("Hunting Bow"), "Hunting Bow", 200, _("A specialty bow carved by a hunter, best used for swift movement and aim."), 1, [0,1,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,18,0, 8, 0,0,0,0],"Back", "Bow")
    $ woodenbow_item = Weapon(_("Wooden Bow"), "Wooden Bow", 120, _("A simplistic wooden bow, fairly lightweight and easy to handle."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,7,0, 5, 0,0,0,0],"Back", "Bow")
    $ smalltrowel_item = Weapon(_("Small Trowel"), "Small Trowel", 30, _("A small hand tool most used for digging in a garden, smoothing or spreading mortar."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,4,0, 0, 0,0,0,0], "Hands", "Axe")
    $ copperpickaxe_item = Weapon(_("Copper Pickaxe"), "Copper Pickaxe", 50, _("An old pickaxe that the werewolf miners used, could be too fragile for long term usage."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,4,0, 0, 0,0,0,0], "Hands", "Axe")
    $ tribalspear_item = Weapon(_("Tribal Spear"), "Tribal Spear", 150, _("A long spear crafted by a tribe, the magical power within gives its user an unusual boost."), 1, [0,0,1,0,0,0, 0,0,0,15,0,0, 0,0,0,0,10,0, 0, 0,0,0,0], "Hands", "Axe")
    $ crystalstaff_item = Weapon(_("Crystal Staff"), "Crystal Staff", 1250, _("A wooden staff with a blue crystal on the top, can be used to slap your enemy, and restore 5 mana each round."), 1, [0,0,3,0,0,0, 0,0,0,0,0,0, 0,0,0,0,4,0, 0, 0,0,0,0], "Hands", "Staff")
    $ beartribeharpoon_item = Weapon(_("Bear Tribe Harpoon"), "Bear Tribe Harpoon", 200, _("A barbed spear that sticks in the target when penetrated, it's extremely difficult to pull out without causing extreme damage. The harpoon was mainly used for hunting creatures in the water, but as the tribe moved inland, it is now seldom used as a weapon."), 1, [0,0,0,1,0,0, 0,0,0,0,0,0, 0,0,0,0,30,0, -8, 0,0.25,0,0], "Hands", "Axe")
    $ axeofookko_item = Weapon(_("Axe of Ookko"), "Axe of Ookko", 1500, _("A lost Battle Axe of the primordial god Ookko, the axe is once wielded in endless battles, the blade has long became blunt and chipped, but the power within is still intact."), 1, [0,0,0,2,0,0, 0,0,0,0,0,0, 5,5,0,0,25,0, 0, 0,0,0,0], "Hands", "Axe")


    $ loincloth_item = Armor(_("Tribe Loincloth"),"Tribe Loincloth", 15, _("A loincloth from the Tribe Puro."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 5,0,0,0,0,-5, 0, 0,0,0,0], "Body", "Pants")
    $ necklace_item = Armor(_("Tribe Necklace"),  "Tribe Necklace", 15, _("A skull necklace from the Tribe Puro."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 4,0,0,0,2,0, 0, 0,0,0,0], "Chest", "Accessory")
    $ lioncharm_item = Armor(_("Lion Charm"),"Lion Charm", 80, _("A Lion Charm made by Sebas."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 5,0,2,0,0,0, 0, 0,0,0,0],"Back", "Bccessory")
    $ badge_item = Armor(_("Courier Badge"),"Courier Badge", 80, _("A badge given by Ole, as a symbol of the courier of lusterfield."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 4,0,0,0,0,0, 0, 0,0,0,0], "Chest", "Bccessory")
    $ slimenecklace_item = Armor(_("Slime Necklace"), "Slime Necklace", 80, _("A Necklace with a slime crystal imbedded into the golden frame."), 1, [0,0,1,0,0,0, 0,0,0,0,0,0, 0,5,0,0,0,2, 0, 0,0,0,0],"Chest", "Accessory")
    $ moonstoneamulet_item = Armor(_("Moonstone Amulet"), "Moonstone Amulet", 500, _("An ancient artifact in the werewolf territory, the wearer is granted a gust of strength at the cost of their health."), 1, [2,0,0,0,0,0, 0,-100,0,0,0,0, 0,0,0,0,10,3, 0, 0,0,0,0],"Chest", "Accessory")
    $ herbalistsgloves_item = Armor(_("Herbalist's Gloves"), "Herbalists Gloves", 80, _("A pair of old gloves from a herbalist in the dark forest, it can probably still be used to collect some dangerous herbs with ease."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0, 0,0,0,0], "Hands", "Accessory")

    $ leatherarmor_item = Armor(_("Leather Armor"), "Leather Armor", 100, _("A strong and durable leather armor custom-made and stitched together by tailor Rahim. It had been a rarity and often fetched a great price during the time when he was the King's appointed Tailor."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 10,5,0,0,0,-5, 0, 5,0,0,0], "Body", "Clothes")
    $ tavernapron_item = Armor(_("Torn Tavern Apron"), "Torn Tavern Apron", 30, _("The Apron that Cane gifts his first server. It's torn currently. I should put it on whenever I work in the Tavern."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 5,5,0,0,0,-4, 0, 0,0,0,0], "Robe", "Clothes")
    $ tavernapron2_item = Armor(_("Tavern Apron"), "Tavern Apron", 50, _("The Apron that Cane gifts his first server. It has been patched up. I should put it on whenever I work in the Tavern."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 8,8,0,0,0,-4, 0, 0,0,0,0], "Robe", "Clothes")
    $ tunic_item = Armor(_("Plain Tunic"),"Plain Tunic", 28, _("A plain tunic, comfortable to wear but too limpy to provide much protection."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 3,2,0,0,0,-5, 0, 0,0,0,0], "Robe", "Clothes")
    $ bandana_item = Armor(_("Bandana"), "Bandana", 40, _("A piece of cloth tied around the head of the wearer, usually promises good luck."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 7,0,5,0,0,-2, 0, 0,0,0,0], "Head", "Mask")
    $ flowyrobe_item = Armor(_("Flowy Robe"), "Flowy Robe", 100, _("One of the outfit from Rahim, a soft piece of garment designed for casual settings."), 1, [0,0,0,0,0,0, 0,0,0,20,0,0, 3,0,0,0,0,-2, 0, 0,0,0,0], "Robe 3 Parts", "Clothes")
    $ adventurerarmor_item = Armor(_("Adventurer Armor"), "Adventurer Armor", 100, _("One of the outfit from Rahim, a collection of straps designed for those who frequent adventures."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 11,0,0,0,0,-5, 5, 0,0,0,0], "Body", "Clothes")
    $ taverncloth_item = Armor(_("Tavern Cloth"), "Tavern Cloth", 100, _("One of the outfit from Rahim...? A piece of Cloth, for cleaning purposes in the Tavern."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 2,0,0,0,0,0, 0, 0,0,0,0], "Body","Clothes")
    $ tavernchaps_item = Armor(_("Tavern Chaps"), "Tavern Chaps", 100, _("One of the outfit from Rahim, an elegantly seamed pants with a hole in the crotch area, apparently for working in the Tavern."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 7,0,0,0,0,5, 0, 0,0,0,0], "Trunk", "Pants")
    $ flowywrap_item = Armor(_("Flowy Wrap"), "Flowy Wrap", 100, _("One of the outfit from Rahim, a soft piece of garment designed for casual settings."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 3,10,0,0,0,2, 0, 0,0,0,0], "Robe", "Pants")
    $ adventurerleggings_item = Armor(_("Adventurer Leggings"), "Adventurer Leggings", 100, _("One of the outfit from Rahim, a collection of straps designed for those who frequent adventures."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 9,0,7,0,0,0, 0, 0,0,0,0], "Trunk", "Pants")
    $ hunterhat_item = Armor(_("Hunter Hat"), "Hunter Hat", 52, _("A hat left by a Hunter in the forest, with a few feathers on the side as a sign of bravery."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 5,0,0,0,0,-2, 5, 0,0,0,0], "Head", "Mask")
    $ hunterattire_item = Armor(_("Hunter Attire"), "Hunter Attire", 60, _("The general outfit of a Hunter, Covered the body to prevent being attacked by wild animals."), 1, [0,1,0,0,0,0, 0,0,0,0,0,0, 8,0,0,0,0,-4, 0, 0,0,0,0], "Body", "Clothes")
    $ huntertrousers_item = Armor(_("Hunter Trousers"), "Hunter Trousers", 60, _("A Normal Trousers worn by a Hunter, with a surprisingly stretchy fly piece..."), 1, [0,1,0,0,0,0, 0,0,0,0,0,0, 6,0,0,0,0,-2, 0, 0,0,0,0], "Trunk",  "Pants")
    $ knighthelmet_item = Armor(_("Knight Helmet"), "Knight Helmet", 92, _("A helmet of a renowned knight in the town, framed with pure iron as a sign of honor."), 1, [1,0,0,0,0,0, 0,0,0,0,0,0, 6,0,0,0,0,-5, 0, 0,0,0,0], "Head",  "Mask")
    $ enchantedchaperon_item = Armor(_("Enchanted Chaperon"), "Enchanted Chaperon", 280, _("A moonstone-threaded chaperon with a long draping liripipe and a softly glowing clasp. Its woven magic steadies the mind and shields the wearer with a faint ward."), 1, [0,0,2,1,1,0, 0,0,0,20,0,0, 4,8,3,0,0,2, 0, 0,0,0,0], "Head", "Mask")
    $ knightbreastplate_item = Armor(_("Knight Breastplate"), "Knight Breastplate", 500, _("The breastplate of a knight, the iron structure and welding in its construction boasting a strong and lionhearted will."), 1, [0,0,0,0,0,0, 0,0,0,0,0,0, 12,8,0,0,0,-8, 0, 0,0,0,0], "Body",  "Clothes")
    $ knightcuisses_item = Armor(_("Knight Cuisses"), "Knight Cuisses", 200, _("A knight's Cuisses customized by the town's oldest blacksmith, it happens to fit you perfectly."), 1, [0,0,0,0,0,0, 0,20,0,0,0,0, 10,0,0,0,0,-6, 0, 0,0,0,0], "Trunk", "Pants")
    $ sweater_item = Armor(_("Sweater"), "Sweater", 50, _("The best type of clothing you can wear in winter, keeping wearer warm and fuzzy."), 1, [0,0,0,0,0,0, 0,15,0,0,0,0, 8,0,0,0,0,-4, 0, 0,0,0,0], "Body", "Clothes")
    $ flatbonnet_item = Armor(_("Flat Bonnet"), "Flat Bonnet", 120, _("A stylish headwear, popularised by the academics of the capital."), 1, [0,0,1,0,0,0, 0,0,0,20,0,0, 6,0,0,0,0,-3, 0, 0,0,0,0], "Head", "Mask")
    $ longscarf_item = Armor(_("Long Scarf"), "Long Scarf", 150, _("A scarf usually worn around the wearer's neck. Its smart and classy outlook probably grants wearer actual smartness as well."), 1, [0,0,2,0,1,0, 0,0,0,0,0,0, 2,0,0,0,0,0, 0, 0,0,0,0], "Chest", "Mask")
    $ dogcollar_item = Armor(_("Dog Collar"), "Dog Collar", 200, _("A collar made by a farmer dog who specialises in growing plants and boners, wearing the collar renders the wearer property of the farmer."), 1, [0,0,0,1,0,0, 0,0,0,0,0,15, 9,0,0,0,0,-2, 0, 0,0,0,0], "Head", "Mask")

    $ bandithood_item = Armor(_("Bandit Hood"), "Bandit Hood", 300, _("A leather hood made from rough stitches, it is the plain bandit's most symbolic headgear, both to obfuscate their identity, and to recognise amongst themselves."), 1, [0,2,0,0,0,0, 0,0,0,0,0,0, 14,0,10,0,0,-2, 0, 0,0,0,0], "Head",  "Mask")
    $ songweaverhat_item = Armor(_("Songweaver Hat"), "Songweaver Hat", 250, _("A stylistic green hat of a renowned bard, decorated with two feathers from a legendary creature roaming on the plains."), 1, [0,0,0,0,0,0, 0,0,0,25,0,0, 7,7,0,0,0,1, 0, 0,0,0,0], "Head", "Mask")
    $ songweavercloak_item = Armor(_("Songweaver Cloak"), "Songweaver Cloak", 250, _("An eloquent garment of a renowned bard, its silk fabric soaked with the alluring voices of the previous owner."), 1, [0,0,0,0,1,0, 0,0,0,0,0,0, 18,0,0,0,0,1, 0, 0,0,0,0], "Robe", "Clothes")
    $ songweaverbreeches_item = Armor(_("Songweaver Breeches"), "Songweaver Breeches", 250, _("An impassionate leggings of a renowned bard, the stretchy and tight materials wraps around the wearer perfectly to display his charming physique."), 1, [0,0,0,0,1,0, 0,0,0,0,0,0, 0,18,0,0,0,1, 0, 0,0,0,0], "Trunk", "Pants")

    $ winterworncoat_item = Armor(_("Winterworn Coat"), "Winterworn Coat", 500, _("An old coat worn by Haskell. Despite its age, it seems to protect the wearer from extreme cold weather"), 1, [0,0,0,0,0,0, 0,0,0,10,0,0, 18,10,0,0,0,-6, 0, 0,0,0,0], "Robe", "Clothes")

    $ idolofvirtue_item = Armor(_("Idol of Virtue"), "Idol of Virtue", 500, _("An accessory that blesses the true warrior, it converts all Charisma of the wearer into pure Strength during battle. However, the wearer cannot cast Flirt on the enemy while it is worn."), 1, [0,0,0,0,2,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0, 0,0,0,0], "Right Arm", "Bccessory")

    $ item_dictionary = [hppotion_item, mppotion_item, redberry_item, blueberry_item, goldenberry_item, strengthpotion_item, green_ointment_item, beer_item, ale_item, accuracypotion_item, tenacitypotion_item, iron_axe_item, iron_sword_item, shortsword_item, smallaxe_item, ironscythe_item, knightlongsword_item, huntingbow_item, woodenbow_item, smalltrowel_item, copperpickaxe_item, tribalspear_item, loincloth_item, necklace_item, lioncharm_item, badge_item, slimenecklace_item, moonstoneamulet_item, herbalistsgloves_item, tavernapron_item, tavernapron2_item, tunic_item, bandana_item, flowyrobe_item, adventurerarmor_item, taverncloth_item, tavernchaps_item, flowywrap_item, adventurerleggings_item, hunterhat_item, hunterattire_item, huntertrousers_item, knighthelmet_item, enchantedchaperon_item, enchantedkirtle_item, knightbreastplate_item, knightcuisses_item, sweater_item, linenbraies_item, flatbonnet_item, longscarf_item, dogcollar_item, botanicaljournal_item, bookoffierycharge_item, bookoftranquilmend_item, housekey_item, mossyartifact_item, woodenbucket_item, letter_item, magicalstone_item, werewolfwhistle_item, stone_item, patch_item, slaterock_item, metalhoop_item, woodenlog_item, cashmere_item, pocketbell_item, flax_item, greendye_item, fabric_item, linen_item, slimeball_item, slimecrystal_item, slimybone_item, rawmutton_item, strap_item, cloth_item, buggbearsedative_item, herbofgrace_item, hemp_item, buggbearsaliva_item, iron_item, canvas_item, minotauressence_item, ginger_item, reed_item, cheappillow_item, pelt_item, rosemary_item, barley_item, chrysanthemum_item, loosebutton_item, carrot_item, sage_item, clay_item, yarn_item, flagitiousooze_item, teratoidmucus_item, slimegrancrystal_item, hexroot_item, feather_item, lodestone_item, copper_item, chestnut_item, purplepanacea_item, apple_item, redrose_item, hawthorn_item, hydrangea_item, horehound_item, crystalgem_item, crystalstaff_item, scrollofeversprout_item, softfur_item, leatherstrips_item, limestone_item, cement_item, masonrymix_item, bandithood_item, songweaverhat_item, songweavercloak_item, songweaverbreeches_item, elderwood_item, vine_item, moonstone_item, nylon_item, crystalstring_item, resonatorgem_item, harp_item, leatherarmor_item, bookofimmolation_item, bookofspectralorb_item, bookofsunderingsurge_item, battleoflusterfield_item, snowberry_item, coal_item, spearmint_item, archaicice_item, chamomile_item, bearfur_item, beartribeharpoon_item, idolofvirtue_item, letterofalliance_item, oldmayorsjournal_item, winterworncoat_item, oolongleaves_item, mugwort_item, hops_item, topusgruit_item, topusbeer_item, ruttishflute_item, stainedscroll_item, hagglersamulet_item, magicshowpamphlet_item, portalring_item, bondagebox_item, growthpotion_item, commandcontroller_item, jotunnbones_item, normalletter_item, smallcoffer_item, bouquet_item, bread_item, assistantcostume_item, engravedstoneshard_item, rebalancingelixir_item, irongreatsword_item, woventunic_item, axeofookko_item]

    $ buggbear = Monster(_("Wild Buggbear"), "Buggbear", 210, 100, 22, 50, 0, 0, 8, 25, 5, 85)

    $ inventories = [inventory, storage, sebasInventory, gwyddyonInventory, methisInventory]
    $ UpdatingItemDescription(inventories, pc)
    $ UpdatingEquipmentLayer(inventories, pc)


    $ lusterfield_map = [lusterfield, green_forest, sparkling_lagoon, ancient_tree, mossy_freshwater, woodland_outpost, alchemists_cabin, kechioeren, damp_cave, dark_forest, gloomy_mountainside, summery_farmland, sundersilk_cascades, backyard_barn,  riverside_crossing]

    $ darkforest_map = [forest_nightwatch, moonlit_wolf_den, split_trails, chelforte_cavern, slumbrous_well, cavern_entrance, viscid_streams, forgotten_sanctuarys, creek_thickets, whispering_hollows]

    $ grassland_map = [grove_of_harvest,  prattlefell_meadow, bandits_hideout]

    $ otsovaara_map = [ursinia_glade, frosted_taiga, snowbound_summit_place, otsovaara, avalanche_site, skullstrewn_pass, clawridge_ascent]

    $ mapFarmers = [ccore_spritec1, ccore_spritec2, ccore_spritec3, ccore_spritec4, ccore_spritec5, ccore_spritec6, ccore_spritec7, ccore_spritec8, ccore_spritec9, ccore_spritec11, ccore_spritec12, ccore_spritec13, ccore_spritec14, ccore_spritec15, ccore_spritec16, ccore_spritec17, ccore_spritec21, ccore_spritec22, ccore_spritec23, ccore_spritec24, ccore_spritec25, limestone_sprite1, limestone_sprite2, limestone_sprite3, limestone_sprite4, limestone_sprite5]







    $ lusterfield.item = []
    $ lusterfield.enemy = [dummy]
    $ lusterfield.drop = [patch_item]

    $ green_forest.item = [redberry_item, blueberry_item, stone_item]
    $ green_forest.enemy = [slime]
    $ green_forest.drop = [slimeball_item, slimecrystal_item]

    $ ancient_tree.item = [goldenberry_item]
    $ ancient_tree.enemy = [goat]
    $ ancient_tree.drop = [cashmere_item, pocketbell_item]

    $ sparkling_lagoon.item = [redberry_item, blueberry_item, flax_item]
    $ sparkling_lagoon.enemy = []
    $ sparkling_lagoon.drop = []

    $ mossy_freshwater.item = [reed_item, clay_item, sage_item]
    $ mossy_freshwater.enemy = []
    $ mossy_freshwater.drop = []

    $ alchemists_cabin.item = [hemp_item, herbofgrace_item, ginger_item, rosemary_item]
    $ alchemists_cabin.enemy = []
    $ alchemists_cabin.drop = []

    $ woodland_outpost.item = [chrysanthemum_item]
    $ woodland_outpost.enemy = [buggbear]
    $ woodland_outpost.drop = [rawmutton_item, strap_item]

    $ kechioeren.item = [horehound_item]
    $ kechioeren.enemy = []
    $ kechioeren.drop = []

    $ gloomy_mountainside.item = [limestone_item]
    $ gloomy_mountainside.enemy = [mino]
    $ gloomy_mountainside.drop = [minotauressence_item]

    $ damp_cave.item = []
    $ damp_cave.enemy = [mimic, stoneward]
    $ damp_cave.drop = [stone_item]

    $ summery_farmland.item = [barley_item]
    $ summery_farmland.enemy = [scarecrow, landshark]
    $ summery_farmland.drop = [loosebutton_item]

    $ sundersilk_cascades.item = [feather_item, hydrangea_item]
    $ sundersilk_cascades.enemy = []
    $ sundersilk_cascades.drop = []


    $ dark_forest.item = []
    $ dark_forest.enemy = [werewolf]
    $ dark_forest.drop = [pelt_item, iron_item]

    $ forest_nightwatch.item = []
    $ forest_nightwatch.enemy = [werewolf]
    $ forest_nightwatch.drop = [pelt_item, iron_item]

    $ split_trails.item = []
    $ split_trails.enemy = [werewolf, caproot]
    $ split_trails.drop = [pelt_item, iron_item, carrot_item]

    $ chelforte_cavern.item = []
    $ chelforte_cavern.enemy = [stoneward]
    $ chelforte_cavern.drop = [slaterock_item]

    $ cavern_entrance.item = []
    $ cavern_entrance.enemy = []
    $ cavern_entrance.drop = []

    $ slumbrous_well.item = []
    $ slumbrous_well.enemy = []
    $ slumbrous_well.drop = []


    $ grove_of_harvest.item = [redrose_item, hawthorn_item, apple_item, hops_item]
    $ grove_of_harvest.enemy = [scarecrow]
    $ grove_of_harvest.drop = [loosebutton_item]

    $ prattlefell_meadow.item = [redberry_item, blueberry_item, mugwort_item]
    $ prattlefell_meadow.enemy = [gnoll]
    $ prattlefell_meadow.drop = []

    $ bandits_hideout.item = []
    $ bandits_hideout.enemy = [bandit]
    $ bandits_hideout.drop = []

    $ ursinia_glade.item = [chamomile_item]
    $ ursinia_glade.enemy = []
    $ ursinia_glade.drop = []



    $ frosted_taiga.item = [spearmint_item, snowberry_item]
    $ frosted_taiga.enemy = [bearguard]
    $ frosted_taiga.drop = [bearfur_item]

    $ otsovaara.name = _("Otsovaara")
    $ otsovaara.item = []
    $ otsovaara.enemy = []
    $ otsovaara.drop = []

    $ FixingFarmerImages()
    $ rahim_vote_duration = 7
    $ quest37.description = _("Rahim told me that Lusterfield will hold a vote to decide if they will form an alliance with the Goat Tribe. The voting ends in 7 days.")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
