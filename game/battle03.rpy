label battle_attack_script:
    if ally_num == 1 or battleTurn != "Player":
        $ battle_actor = "You"
        $ battle_possessor = "Your"
    else:
        $ battle_actor = ally.name
        $ battle_possessor = "His"

    if target.img == "Goat Huntsman":
        $ enemymy = _("goat")
    else:
        $ enemymy = _("bear")
    if oa[0] == "S":
        if target.img == "Rune Guardian":
            "You struggle against the spell, trying to break free. You dealt [oa[4]] damage to the guardian in the process, his grip has loosen as well."

    if oa[1] == "M":
        if ally_num == 2 and ally.name == "Amble" and battleTurn != "Ally":
            "Amble strikes his hammer against the fluffy leaves, but it bounces off the bridgeroot slickly."
        elif target.img == "Slime" or target.img == "Hefty Slime" or target.img == "Malignant Slime":
            if oa[3] == "N":
                "You raise your fist and punch as hard as you can into the [target.name!t]. but it swiftly dodges away from your blow."
            elif oa[3] == "A":
                "You raise your sword and slash at the monster, but the [target.name!t] quickly dodges your attack."
            elif oa[3] == "B":
                "You slam your axe into the monster, but the [target.name!t] quickly dodges your attack."
            elif oa[3] == "C":
                "You hold and shoot an arrow at the slime, but it narrowly misses the [target.name!t]."
        elif target.img == "Buggbear":
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the buggbear's arm. It slides right off his fluffy arm. You can only look on in disbelief."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] into the buggbear's arm. It bounces right off. You can only look back in disbelief."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the buggbear's arms. It pierces right through his soft fur but fails to make a dent in his skin, leaving you frozen in disbelief."
            if oa[3] == "N":
                "You raise your fist and throw it at the buggbear, but miss and hit nothing, leaving you standing there like a fool instead."
            if renpy.random.random() > 0.5:
                "The buggbear growls loudly, hitting his chest while taunting at your feeble attempt at attacking him."
        elif target.img == "Rune Guardian":
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the arm of the guardian, but his magical aura repels the attack."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] at the guardian's head, but his magical aura repels the attack."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the guardian, but it seems to have missed."
            if oa[3] == "N":
                "You throw your fist at the guardian, but you punch into the air instead."
        elif target.img == "Dummy":
            if oa[3] == "N":
                "You hold your fist and punch as hard as you can into the [target.name!t]. but you punch the wall instead. Hopefully no one saw that..."
            elif oa[3] == "A":
                "Your swing your sword at the [target.name!t], but it hits the wall instead."
            elif oa[3] == "B":
                "You slam your axe into the [target.name!t], but it hits the wall instead."
            elif oa[3] == "C":
                "You bring up your bow and aim. You release the bowstring, and it barely miss the [target.name!t]."
        elif target.img == "Cult Acolyte":
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the [enemymy!t]'s arm, but he blocks your attack easily with his spell shield."
            if oa[3] == "B":
                "You try to slam your [pc.weapon.name!t] into the [enemymy!t]'s head, he blocks your attack easily with his spell shield."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the [enemymy!t], he blocks your attack easily with his spell shield."
            elif oa[3] == "N":
                "You throw your fist at the [enemymy!t], but he leaps back, blocking your attack easily with his spell shield."
        elif target.img == "Goat Huntsman" or target.img == "Bear Guard":

            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the [enemymy!t]'s arm, but he leaps back, avoiding the blow by inches."
            if oa[3] == "B":
                "You try to slam your [pc.weapon.name!t] into the [enemymy!t]'s head, but he leaps back and avoids the blow by mere inches."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the [enemymy!t], but he leaps back, avoiding the arrow by mere inches."
            elif oa[3] == "N":
                "You throw your fist at the [enemymy!t], but he leaps back, the blow only serving to ruffle his fur a little."
            if target.img == "Goat Huntsman":
                if renpy.random.random() > 0.5:
                    if goat_num == 1:
                        gt "You foul varmint, you really think your little trick is going to hurt me? Now, taste my spear!"
                    if goat_num == 2:
                        gt "T-that wasn't a good attempt, you need to do better."
            else:
                if renpy.random.random() > 0.5:
                    bearGuard "What a waste of time, let me show you how a real snow warrior fight."

        elif target.img == "Bridgeroot" or target.img == "Seedsman":
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the [target.name!t], but it strikes into nothing but a few stranded leaves and vines."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] at the [target.name!t], but it strikes into nothing but a few stranded leaves and vines."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the [target.name!t], but it strikes into nothing but a few stranded leaves and vines."
            if oa[3] == "N":
                "You hold your fist, with all your might you throw a punch at the [target.name!t], but it strikes into nothing but a few stranded leaves and vines."
            "The [target.name!t] stands there, still emotionless, he doesn't seem to notice your feeble attack, not even the slightest."
        elif target.img == "Spriteling" or target.img == "Spritebinder":
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the [target.name!t], but it turns ephereal and dodges swiftly in the air."
            elif oa[3] == "B":
                "You slam your [pc.weapon.name!t] at the [target.name!t], but it turns ephereal and dodges swiftly in the air."
            elif oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the [target.name!t], but it turns ephereal and dodges swiftly in the air."
            else:
                "You throw your fist at the [target.name!t], but it turns ephereal and dodges swiftly in the air."
            if target.img == "Spritebinder":
                yu "Shit, my sword's not working..."
            "The [target.name!t] floats motionless in face of your attack."
        elif target.img == "Werewolf":
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the arms of the [target.name!t], it slides right off his fluffy arm, while you look back in disbelief."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] at the arms of the [target.name!t], it slides right off his fluffy arm, while you look back in disbelief."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the arms of the [target.name!t], it pierces right through his soft fur without touching his skin, leaving you frozen in disbelief."
            if oa[3] == "N":
                "You hold your fist and throw it at the [target.name!t], but it hits nothing and leaves you standing instead."
            if renpy.random.random() > 0.5:
                ww "Unlucky. But not surprised, hmmm..."
            "The [target.name!t] laughs loudly while flexing his claws, it almost seems he's scoffing at your attempt of attack."

        elif target.img == "vurro_spar":
            "You press on, trying to land a hit, but Vurro continues to evade your blows."

            "Despite his illness, Vurro moves with surprising grace, ducking and weaving out of your way."
            $ dia = renpy.random.random()
            if dia < 0.3:
                v "Hey, aim better. I'm walking only slightly faster than a training dummy."
            elif dia < 0.6:
                v "Not saying Uffe is fast and small enough to dodge your blow, but you can't swing your fist anywhere hoping it hits something."
        elif target.img == "Gnoll" or target.img == "Bandit":
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the [target.name!t], but he hops away in time, dodging from your attack."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] at the [target.name!t], but he hops away in time, dodging from your attack."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the [target.name!t], but he hops away in time, dodging from your attack."
            if oa[3] == "N":
                "You hold your fist and throw it at the [target.name!t], but he hops away in time, dodging from your attack."
            $ dia = renpy.random.random()
            if target.img == "Bandit":
                if dia < 0.3:
                    bd "Come on, try harder! You'll never defeat me with such sloppy attacks!"
                elif dia < 0.6:
                    bd "Swing and a miss! You'll have to do better than that!"
            else:
                if dia < 0.3:
                    gnl "You swing, I dance!"
                elif dia < 0.6:
                    gnl "Jump, spin, you miss!"
                "The [target.name!t] laughs loudly while crouching on the grass, it almost seems he's scoffing at your attempt of attack."
    else:


        $ isConfused = next((x for x in status if x.img == "Confused"), None)
        if target.img == "Cult Acolyte" and isConfused != None and renpy.random.random() > 0.5:
            if oa[3] == "A":
                "You try to slice your [pc.weapon.name!t] into the [enemymy!t]'s arm, but it's only after a second that you realise you have hit yourself instead."
            if oa[3] == "B":
                "You slash your [pc.weapon.name!t] at the [enemymy!t] in a wide, horizontal arc, but it's only after a second that you realise you have hit yourself instead."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the [enemymy!t]. Somehow, the arrow has reached your shoulder instead."
            if oa[3] == "N":
                "You throw your fist at the [enemymy!t], but you feel your fist suddenly swings back and hits you in the face instead."
            call Damaging (target, pc, enemy_damage) from _call_Damaging_21
            if renpy.random.random() > 0.5:
                acolyte "Your mind is lost in the shepherd's call."
            else:
                acolyte "Despite being a dragon, you are just as vulnerable as other horned ones."
            return

        if ally_num > 1 and ally.name == "Amble" and battleTurn != "Ally":
            "Amble strikes his hammer against the fluffy leaves of the bridgeroot, it hits his core very effectively as the green monster staggers a bit backwards, you can clearly see the crater his hammer creates there."
        elif target.img == "Slime" or target.img == "Hefty Slime" or target.img == "Malignant Slime":
            if oa[3] == "N":
                "You hold your fist and punch as hard as you can into the [target.name!t]. It is as disgusting as it is effective."
            elif oa[3] == "A":
                "You growl and swing your sword at the monster, slashing right through the [target.name!t]."
            elif oa[3] == "B":
                "You growl and swing your axe at the monster, slashing right through the [target.name!t]."
            elif oa[3] == "C":
                "You hold your bow and aim at the monster, you release the arrow and it flies true, hitting the [target.name!t] right in its core."
        elif target.img == "Dummy":
            if oa[3] == "N":
                "You raise your fist and punch as hard as you can into the dummy."
            elif oa[3] == "A":
                "You growl and swing your sword, slashing right into the dummy."
            elif oa[3] == "B":
                "You growl and swing your axe, slashing right into the dummy."
            elif oa[3] == "C":
                "You bring up your bow and aim. The arrow flies right into its bull's eye."
        elif target.img == "Cult Acolyte":
            if oa[3] == "A":
                "You try to slice your [pc.weapon.name!t] into the [enemymy!t]'s arm. He brings his spell shield up to block, but fails to stop the strike entirely."
            if oa[3] == "B":
                "You slash your [pc.weapon.name!t] at the [enemymy!t] in a wide, horizontal arc. The [enemymy!t] leaps back out of range, but not before the blade nicks a shallow cut across his stomach."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the [enemymy!t]. Before he even reacts, the arrow hits him right in the shoulder."
            if oa[3] == "N":
                "You throw your fist at the [enemymy!t], hitting him right across the face. The sheer impact knocks him to the ground."
            if isConfused != None:
                $ isConfused.rounds -= 1
        elif target.img == "Buggbear":

            if oa[3] == "A":
                if renpy.random.random() > 0.5:
                    "You slash your [pc.weapon.name!t] at the buggbear, grazing its stomach and drawing blood."
                else:
                    "You slash your [pc.weapon.name!t] at the buggbear, knocking him to the ground. He growls at you before getting up, somehow angrier than albeit disheveled. "
            if oa[3] == "B":
                if renpy.random.random() > 0.5:
                    "You slam your [pc.weapon.name!t] into the buggbear, cutting a bright red gash into his orange hide. The fur around the weeping wound grows matted with blood."
                else:
                    "You slam your [pc.weapon.name!t] into the buggbear's face, tipping him off balance with a loud thump and roar."
            if oa[3] == "C":
                if renpy.random.random() > 0.5:
                    "You aim and shoot your [pc.weapon.name!t] at the buggbear. The arrow hits him right in the shoulder. He screams in agony."
                else:
                    "You run while shooting your [pc.weapon.name!t] at the buggbear, knocking him to the ground. He growls at you before getting up, albeit disheveled."
            if oa[3] == "N":
                if renpy.random.random() > 0.5:
                    "You throw your fist at the buggbear, hitting him across his face, the sheer impact of which knocks him to the ground."
                else:
                    "You punch into the buggbear's stomach making him double over in pain. You use this opportunity to knee him in the face. It feels like hitting a stone wall, but the buggbear slams into the ground hard."
            $ dia = renpy.random.random()
            if target.hp >  target.max_hp * 0.5:
                if dia < 0.5:
                    "The buggbear grunts in anger, he definitely doesn't appreciate getting battered by a random visitor."
            else:
                if dia < 0.5:
                    "You can barely hear the groaning sound of the buggbear. He is in absolute distress, and ready to slaughter his attacker without mercy."
        elif target.img == "Rune Guardian":
            if oa[3] == "A":
                if renpy.random.random() > 0.5:
                    "You slash your [pc.weapon.name!t] at the arm of the Rune Guardian, your blade scraps against the stone. Some of it crack and falls off his body."
                else:
                    "You slash your [pc.weapon.name!t] across the guardian's body, knocking him back a few steps. The guardian quakes silently in anger."
            if oa[3] == "B":
                if renpy.random.random() > 0.5:
                    "You slam your [pc.weapon.name!t] at the arm of the Rune Guardian, your blade grazes against the stone. Some of it crack and falls off his body."
                else:
                    "You slam your [pc.weapon.name!t] across the guardian's body, knocking him back a few steps. The guardian quakes silently in anger."
            if oa[3] == "C":
                if renpy.random.random() > 0.5:
                    "You aim and shoot your [pc.weapon.name!t] at the Rune Guardian, the arrow hits right into his arm, striking off a few rubbles."
                else:
                    "You run while shooting your [pc.weapon.name!t] across the guardian's body, knocking him back a few steps. The guardian quakes silently in anger."
            if oa[3] == "N":
                if renpy.random.random() > 0.5:
                    "You throw your fist at the guardian, hitting him right across his body, the sheer impact strikes off a few rubbles."
                else:
                    "You punch into the guardian's stomach, knocking him back a few steps. The guardian quakes silently in anger."
        elif target.img == "Goat Huntsman" or target.img == "Bear Guard":

            if oa[3] == "A":
                if renpy.random.random() > 0.5:
                    "You try to slice your [pc.weapon.name!t] into the [enemymy!t]'s arm. He brings his spear up to block, but fails to stop the strike entirely."
                else:
                    "You feint an overhead chop with your [pc.weapon.name!t], before bringing up your foot for a kick to his chest as he tries to block, knocking him down on the ground."
            if oa[3] == "B":
                if renpy.random.random() > 0.5:
                    "You slash your [pc.weapon.name!t] at the [enemymy!t] in a wide, horizontal arc. The [enemymy!t] leaps back out of range, but not before the blade nicks a shallow cut across his stomach."
                else:
                    "You slam the butt of your [pc.weapon.name!t] into the [enemymy!t]'s head, knocking him on the ground."
            if oa[3] == "C":
                if renpy.random.random() > 0.5:
                    "You aim and shoot your [pc.weapon.name!t] at the [enemymy!t]. The arrow hits him right in the shoulder. "
                else:
                    "You run while shooting your [pc.weapon.name!t] at the [enemymy!t], knocking him to the ground. He growls at you before getting up, albeit disheveled."
            if oa[3] == "N":
                if renpy.random.random() > 0.5:
                    "You throw your fist at the [enemymy!t], hitting him right across the face. The sheer impact knocks him to the ground."
                else:
                    "You slam your fist into the [enemymy!t]'s stomach. As he doubles over in pain, you kick out his legs under him, knocking him flat on the ground."
            if oa[2] == "N":
                $ rnd = renpy.random.random()
                if rnd > .33:
                    "A bright red gash appearing in his arm."
                elif rnd > .66:
                    "He growls at you before getting up, albeit disheveled."
                else:
                    "Drops of blood spill down the front of his body."


        elif target.img == "Bridgeroot" or target.img == "Seedsman":
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the [target.name!t], as your blade grazes through the leaves and vines on [target.name!t], and a chunk of leaves falls off of him, casually."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] at the [target.name!t], as it strikes through the leaves and vines on [target.name!t], and a chunk of leaves falls off of him, casually."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the [target.name!t], as your arrow grazes through the leaves and vines on [target.name!t], and a chunk of leaves falls off of him, casually."
            if oa[3] == "N":
                "You hold your fist, with all your might you throw a punch at the [target.name!t], as your blade grazes through the leaves and vines on [target.name!t], and a chunk of leaves falls off of him, casually."
            "The [target.name!t] grunts loudly, seems more than mildly annoyed now that you're hurting him."
        elif target.img == "Spriteling" or target.img == "Spritebinder":
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the [target.name!t], your blade grazes through the ghostly form of the [target.name!t]."
            elif oa[3] == "B":
                "You slam your [pc.weapon.name!t] at the [target.name!t], your weapon grazes through the ghostly form of the [target.name!t]."
            elif oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the [target.name!t], the shot grazes through the ghostly form of the [target.name!t]."
            else:
                "You throw your fist at the [target.name!t], your punch grazes through the ghostly form of the [target.name!t]."
            "The [target.name!t] vibrates, seems more than mildly annoyed now that you're hurting him."
        elif target.img == "vurro_spar":
            $ dia = renpy.random.random()
            if dia < 0.33:
                "You unleash a flurry of punches, each strike aimed at Vurro's chest and shoulder."
                "Momentarily caught off-guard, Vurro tries to evade your attack, but you manage to graze his side with a swift punch."
            elif dia < 0.66:
                "You feint to the right before landing a solid punch to Vurro's shoulder."
                "It's a clean hit, and you can see a flicker of surprise in Vurro's eyes as he stumbles back a step."
            else:
                "You throw a punch before executing a quick spin, delivering a swift kick to Vurro's midsection."
                "The kick lands, and Vurro grunts in surprise as he stumbles back, momentarily winded."
        else:
            if oa[3] == "A":
                if renpy.random.random() > 0.5:
                    "You slash your [pc.weapon.name!t] at the [target.name!t], your blade grazes through the [target.name!t]'s stomach. Drops of blood drips through his body."
                else:
                    "You slash your [pc.weapon.name!t] at the [target.name!t], knocking him on the ground. He growls at you before getting up, albeit disheveled."
            if oa[3] == "B":
                if renpy.random.random() > 0.5:
                    "You slam your [pc.weapon.name!t] at the [target.name!t], your blade grazes through the [target.name!t]'s stomach. Drops of blood drips through his body."
                else:
                    "You slam your [pc.weapon.name!t] at the [target.name!t], knocking him on the ground. He growls at you before getting up, albeit disheveled."
            if oa[3] == "C":
                if renpy.random.random() > 0.5:
                    "You aim and shoot your [pc.weapon.name!t] at the [target.name!t], the arrow hit right into his shoulder and he screams in agony."
                else:
                    "You run while shooting your [pc.weapon.name!t] at the [target.name!t], knocking him on the ground. He growls at you before getting up, albeit disheveled."
            if oa[3] == "N":
                if renpy.random.random() > 0.5:
                    "You throw your fist at the [target.name!t], hitting him right across his face, the sheer impact knocks him on the ground."
                else:
                    "You punch into the [target.name!t]'s stomach, grabbing him and slam him on the ground hard."
        call Enemy_Damaging (target, oa[4]) from _call_Enemy_Damaging_14
        if oa[2] == "N":
            "His health decreases by [oa[4]] HP."
        else:
            "Critical hit! [target.name!t]'s health now decreases by [oa[4]] HP!"


        $ dia = renpy.random.random()

        if target.img == "vurro_spar":
            if dia < 0.3:
                v "Ouch, your fist does hurt. Wuldon's gonna have a hard time pissing you off, doesn't he?"
            elif dia < 0.6:
                v "That was quite impressive for a non-werewolf. You do have some tricks up your sleeves."
        if target.hp >  target.max_hp * 0.5:
            if target.img == "Werewolf":
                if dia < 0.3:
                    ww "Come here... little prey, stop resisting."
                elif dia < 0.6:
                    ww "Huh... This prey is definitely moving. And I'll prefer a moving one when I get a hold of you."
                "The [target.name!t] howls in anger, you can feel the imminent danger as other werewolves in the forest respond to his howl."
            elif target.img == "Goat Huntsman":
                if dia < 0.33:
                    if goat_num == 1:
                        gt "Aggghh.... W-what the... You little furry lizard, I'll strike you down without mercy!"
                    if goat_num == 2:
                        gt "Grrrrr! L-lucky hit... Let me teach you how to fight properly!"
                elif dia < 0.67:
                    gt "Grrrrr! L-lucky hit... Let me teach you how to fight properly!"
            elif target.img == "Cult Acolyte":
                if dia < 0.33:
                    acolyte "Resistance only delays the inevitable."
                else:
                    acolyte "Your strength of mind is commendable, yet insufficient."
            elif target.img == "Bear Guard":
                if dia < 0.33:
                    bearGuard "Hnnngh! Just a scratch, you'll learn to regret even touching me."
                elif dia < 0.67:
                    bearGuard "Arrgh! By Ookko's bless, I- I won't let you g-get away with this."
            elif target.img == "Gnoll":
                if dia < 0.3:
                    gnl "O-Ouch! Fingertips graze, almost!"
                elif dia < 0.6:
                    gnl "Y-your blow, it finds me!"
            elif target.img == "Bandit":
                if dia < 0.3:
                    bd "Not bad, not bad at all. But I'm not done with you yet!"
                elif dia < 0.6:
                    bd "Alright, this is gonna worth my gold so much."
        else:

            if target.img == "Werewolf":
                if dia < 0.3:
                    ww "Argh...! You can really pack a punch do you not? Can't wait to pin you down and get a taste of your flesh."
                elif dia < 0.6:
                    ww "Hnnngh!!! Now I'm getting real angry. And you don't want to see me when I'm angry, little prey."
                "You can barely hear barking sound of the [target.name!t], it seems like he doesn't appreciate a trespasser, and you've angered him further."
            elif target.img == "Goat Huntsman":
                if dia < 0.33:
                    if goat_num == 1:
                        gt "Ummmph.. How... I-I can't. Chief, please give me the strength to defeat this insolent whelp!"
                    if goat_num == 2:
                        gt "Damn... didn't know a courier can hit that hard...!"
                elif dia < 0.67:
                    if goat_num == 1:
                        gt "Hnnnngh... M-my brothers, they will not spare your pathetic life. T-they're coming... any second now. Y-you better run."
                    if goat_num == 2:
                        gt "Damn... didn't know a courier can hit that hard...! Give me all you got!"
            elif target.img == "Bear Guard":
                if dia < 0.33:
                    bearGuard "Ngggg... I'll fight until my last breath, b-because I'm a warrior!"
                elif dia < 0.67:
                    bearGuard "T'is but a test of my strength, I'll s-strike you down, w-watch it."
            elif target.img == "Gnoll":
                if dia < 0.3:
                    gnl "Gnoll feels that, argh!"
                elif dia < 0.6:
                    gnl "Y-ou strong... I-I see."
            elif target.img == "Bandit":
                if dia < 0.3:
                    bd "Argh! Lucky shot! But don't get cocky, I've got plenty more fight in me!"
                elif dia < 0.6:
                    bd "Hey, let's talk this out, huh? I'll make it worth your while!"
    return

label battle_flirt_script:

    if status == "Bound":
        if target.img == "Rune Guardian":
            "You struggle against the guardian as you try to reach under the guardian's crotch, trying to get a reaction from the guardian."
            "The guardian instanly react with your advance, vibrating profusely with his moss. His grip is weakening as well."
        if target.img == "Cult Acolyte":
            "You struggld against the tendrils from the cultist, only to be bound tighter in its retaliation."
            "Though, the cultist seems to enjoy seeing your suffering."

    elif target.img == "Dummy":
        "You caress your body in front of the dummy, calling its name in some silly fashion."
        "Getting closer to the motionless dummy, you try to get a reaction from it by touching it in the groin area... but it doesn't seem to react to your advance."
    elif target.img == "Spriteling" or target.img == "Spritebinder":
        "Flirt doesn't sound like a great idea on these creatures..."
        jump general_battle_loop
    elif target.img == "Hefty Slime" or target.img == "Malignant Slime":
        "As much as you try to... flirt with the slime, it doesn't flinch, or get aroused."
        "You back off before it tries to grab a hold of your body."
    else:
        $ dia = renpy.random.random()
        if dia > 0.334:
            "You turn around and rub your hand all over your own burly cheeks, feeling and brushing against your ass while you shake your hip."
        elif dia > 0.667:
            "You scrape your member lightly, running your claw from your inner thigh to the back of your balls, you tug at it tightly while staring at [target.name!t] seductively."
        else:
            "You cup at your fluffy chest, drawing circles around the area of your nipples. You smile at the [target.name!t] while your chest bounce up and down slightly."
        if oa[1] == "M":
            if target.img == "vurro_spar":
                v "I'm not sure if this is part of the training, but I don't think you're going to survive after showing Uffe this, so don't do that."
                "Vurro shoots you a playful smile, mildly amused at your demonstration."
            elif target.img == "Slime":
                "It doesn't seem to have noticed, or have the capability to even do that."
            elif target.img == "Goat Huntsman":
                "You continue your act for about a minute, but the huntsman doesn't even flinch."
                if goat_num == 1:
                    gt "Ok... That's too much, you insolent filth. I'm not going to fall for this."
                if goat_num == 2:
                    gt "Well..."
            elif target.img == "Cult Acolyte":
                "The cultist seems to be enjoying your act, but he doesn't get affected by it, based on the mask."
                acolyte "You are a curious one, aren't you?"
            elif target.img == "Bear Guard":
                "The bear snatches at your hand, but you quickly retreat in time."
                bearGuard "Shut it. This is not a warrior's way of battle."
            elif target.img == "Rune Guardian":
                "You continue your act for about a minute, but the Rune Guardian doesn't even flinch."
                "Disappointed, you back away before the guardian can grab a hold of you."
            else:
                "You continue your act for about a minute, but the [target.name!t] just stares at you in confusion."
        else:
            if target.img == "vurro_spar":
                if target.lust > target.max_lust / 2:
                    "Vurro's jaw wide in awe, you notice some unusual movement in his pants."
                    v "W-wuldon's gonna like fighting against you, won't he?"
                else:
                    "Vurro lowers his fists for a moment, his cheeks soon turn bright red."
                    v "Mhmm... just don't flirt with Uffe when the time comes, but I have to admit, you do get a reaction out of me."
            elif target.img == "Goat Huntsman":
                if goat.lust > goat.max_lust / 2:
                    if renpy.random.random() > 0.5:
                        "Within a few seconds you can already see some movement from under the goat's loincloth. He doesn't say anything, except for licking his lips. His lust is increased by [player_flirt]."
                        gt "...I-if you do that one more time I'm going to grab that huge ass and never let go..."
                    else:
                        "You notice the goat is floundering, trying his best not to get aroused by your seduction, but his flushed face and pitched tent says it all. His lust is increased by [player_flirt]."
                        gt "You are w-wasting your time. I'm n-not... I'm not... I- uhh... nooo..."
                else:
                    if renpy.random.random() > 0.5:
                        "The goat huntsman is squirming in reaction to your advance. You can already hear his rapid breathing and grunting, holding his spear tightly. His lust is increased by [player_flirt]."
                        gt "N-noooo. I c-can't control... my mind. Please..."
                    else:
                        "You can tell the huntsman is already playing with himself when his hand goes under his loincloth, staring at your ass intently. His lust is increased by [player_flirt]"
                        gt "Hnnnngh... I n-need to... cum."
            elif target.img == "Buggbear":
                if target.lust > target.max_lust / 2:
                    if renpy.random.random() > 0.5:
                        "Within a few seconds you can already see some movements from under the buggbear's loincloth. The sturdy beast man licks his lips, grumbling at your beautiful sight. His lust is increased by [player_flirt]."
                    else:
                        "You notice the buggbear is staring at your crotch. You give him a subtle wink. He already looks like he can't breath from his arousal. His lust is increased by [player_flirt]."
                else:
                    if renpy.random.random() > 0.5:
                        "The buggbear is squirming in reaction to your advance. You can already hear his rapid breathing and grunting, holding his mace tightly. His lust is increased by [player_flirt]."
                    else:
                        "You can tell the buggbear is already playing with himself when his hand goes under his loincloth, staring at your ass intently. His lust is increased by [player_flirt]."
            elif target.img == "Bear Guard":

                if renpy.random.random() > 0.5:
                    "You can see the bear's clenches his fist tightly, something under his loincloth begins to move, even as he closes his eyes, and remain silent."
                    "His lust is increased by [player_flirt]."
                    bearGuard "S-shut..."
                else:
                    "The bear pants heavily, his cheeks are alraedy so red, you can see his drool dripping uncontrollably as he watches."
                    "His lust is increased by [player_flirt]."
            elif target.img == "Cult Acolyte":
                if renpy.random.random() > 0.5:
                    "You notice his exposed manhood spring awake for a few times, it is no wonder why the cultists are so horny all the time."
                    "Though, the cultist does not speak one word."
                else:
                    "The cult acolyte watches your performance in silence, but his nervous body proves to you that your act has worked in your favour."
                "His lust is increased by [player_flirt]."
            elif target.img == "Rune Guardian":
                if renpy.random.random() > 0.5:
                    "You cannot detect his lust on the face, but by the vibration of the moss you can deduce that he's enjoying this a lot. His lust is increased by [player_flirt]."
                else:
                    "The guardian doesn't speak, but he is extremely distracted by your performance. His lust is increased by [player_flirt]."
            elif target.img == "Bridgeroot":
                "Even if it's just a little, you notice a mild vibration in the bridgeroot's moss, it seems to react easily. His lust is increased by [player_flirt]."
            elif target.img == "Seedsman":
                "The seedsman reacts mildly to your attempt, you can see his verdant body rustling slightly. His lust is increased by [player_flirt]."
            elif target.img == "Slime":
                "Almost surprisingly, the slime budges, even just for a little."
            elif target.lust > target.max_lust / 2:
                if renpy.random.random() > 0.5:
                    "Within a few seconds you can already see some movements under the [target.name!t]'s ripped pants."
                    "The sturdy beast man licks his lips, grumbling at your beautiful sight. His lust is increased by [player_flirt]."
                else:
                    "You notice the [target.name!t] is staring at your crotch, you slightly wink at him and he already looks like he can't breath under such arousal."
                    "His lust is increased by [player_flirt]."
                $ dia = renpy.random.random()
                if target.img == "Werewolf":
                    if dia < 0.33:
                        ww "Hmm... Come closer... little prey."
                    elif dia < 0.66:
                        ww "You have a nice body, little prey. Our pack would be delighted to see you."
                if target.img == "Gnoll":
                    if dia < 0.33:
                        gnl "What's underneath? Gnoll wonders..."
                    if dia < 0.66:
                        gnl "Come... we play instead."
                if target.img == "Bandit":
                    if dia < 0.33:
                        bd "Well... our brothers would like to greet you."
                    if dia < 0.66:
                        bd "Adventurers like you are so slutty, I'd plow your ass right now."
            else:
                if renpy.random.random() > 0.5:
                    "The [target.name!t] is squirming in reaction to your advance."
                    "You can already hear his rapid breathing and grunting, grasping at his own claws. His lust is increased by [player_flirt]."
                else:
                    "You can tell the [target.name!t] is already playing with himself when his claws goes under his pants, staring at your ass intently."
                    "His lust is increased by [player_flirt]."
                $ dia = renpy.random.random()
                if target.img == "Werewolf":
                    if dia < 0.33:
                        ww "I-I can't hold... back- if you keep being like that."
                    elif dia < 0.66:
                        ww "L-little prey, y-our hole is mine. Now give up already and let me... f-fuck."
                if target.img == "Gnoll":
                    if dia < 0.33:
                        gnl "Mmmmmph... I sense a wild growth. Can't hold-"
                    if dia < 0.66:
                        gnl "No think- Not... g-giving in..."
                if target.img == "Bandit":
                    if dia < 0.33:
                        bd "Mmmmph..."
                    if dia < 0.66:
                        bd "N-not even... c-close."
    return

label battle_escape_surrender_script:

    if oa[0] == "E":
        if target.img == "Dummy":
            "You walk away from the dummy; it appears to patch itself up before going motionless, letting dust settle on it again."
            call Battle_Finish from _call_Battle_Finish_44
            jump main_lusterfield_alleyway
        elif target.img == "vurro_spar":
            "You're not sure if you can leave the training with Vurro right now."
            jump general_battle_loop
        elif target.img == "Rune Guardian":
            "As much as you try, you cannot escape from the guardian's magical aura."
            jump general_battle_loop
        elif target.img == "Spritebinder":
            "You try to escape, but the spritebinder's arm yanks you straight back into the fight."
        elif (target.img == "Hefty Slime" or target.img == "Malignant Slime") and wslime_progress > 0 and not quest31.status == True:
            "You can't escape from the arena."
            if target.img == "Hefty Slime":
                jump heftyslime_battle_loop
            else:
                jump malignantslime_battle_loop
        elif target.img == "Goat Huntsman" and quest23.status == 3:
            "You cannot run away from battle practice..."
        elif target.img == "Cult Acolyte":
            "There is no way out of this battle."
        elif oa[0] == "M":
            if target.img == "Slime" or target.img == "Hefty Slime" or target.img == "Malignant Slime" or target.img == "Slushy":
                "You slowly back away from the [target.name!t]'s attack. Attempting to dodge its gooey appendages, you trip and fall on the grass!"
                "Your escape attempt seems to have failed."
            elif target.img == "Goat Huntsman":
                "You slowly back down from the goat's attack, turn around, and run as fast as you can. Suddenly, you slip and fall on the trap he set up ealier. Your escape seems to have failed!"
                if goat_num == 1:
                    gt "Haha... Come back here you insolent wretch, I am not done with you yet."
                if goat_num == 2:
                    gt "Mhmm... need to improve your running skills as well."
            elif target.img == "Buggbear":
                "You slowly back down from the buggbear's attack, you turn around and run as fast as you can."
                "But the beast easily catches up to you and throws your entire body on the ground. Your escape seems to have failed!"
            elif target.img == "Spriteling":
                "You slowly back away from the [target.name!t]'s attack. Attempting to dodge its ghostly form, you trip and fall on the grass!"
                "Your escape attempt seems to have failed."
            else:
                "You slowly back down from the [target.name!t]'s attack, you turn around and run as fast as you can."
                "But the [target.name!t]'s claw instantly grips onto your tail and you fall on the ground. Your escape seems to have failed!"
                if target.img == "Werewolf":
                    ww "Do not ever think about escaping, little prey. You are mine now."
        else:
            if target.img == "Slime" or target.img == "Hefty Slime" or target.img == "Malignant Slime":
                "You slowly back away from the [target.name!t]'s attack. Dodging its gooey appendages. You successfully escape from the [target.name!t]!"
            elif target.img == "Goat Huntsman":
                "You slowly back away from the goat's attack, turn around, and run as fast as you can. The goat throws his spear at you, barely missing your head. You successfully escaped from the huntsman!"
            elif target.img == "Spriteling":
                "You slowly back away from the [target.name!t]'s attack. Dodging its ghostly form. You successfully escape from the [target.name!t]!"
            elif target.img == "Buggbear":
                "You slowly back down from the buggbear's attack, you turn around and run as fast as you can. The beast tries to outrun you but he trips and falls on the ground, You successfully escaped from the buggbear!"
            else:
                "You slowly back down from the [target.name!t]'s attack, you turn around and run as fast as you can."
                "The [target.name!t] tries to outrun you but he trips and falls on the ground, You successfully escaped from the [target.name!t]!"
            hide screen battle_buttons
            hide screen battle_enemy_stat
            hide screen battle_player_stat
            call Battle_Finish from _call_Battle_Finish_89
            if target.img == "Slime":
                jump main_green_forest
            elif target.img == "Goat Huntsman":
                jump main_green_forest
            elif target.img == "Hefty Slime" or target.img == "Malignant Slime":
                if current_location.img == "Viscid Stream":
                    jump Viscid_Stream_Loop
                elif current_location.img == "Forgotten Sanctuary":
                    jump Forgotten_Sanctuary_Loop
                elif current_location.img == "Creek Thicket":
                    jump Creek_Thicket_Loop
            elif target.img == "Werewolf":
                if isinstance(current_location, MapPat):
                    if current_location.img == "Split Trail":
                        jump Split_Trail_Loop
                    elif current_location.img == "Forest Nightwatch":
                        jump Dark_Forest1_Loop
                jump main_dark_forest
            elif target.img == "Buggbear":
                jump main_woodland_outpost
            elif target.img == "Seedsman":
                jump main_grove_of_harvest
            elif target.img == "Bear Guard":
                jump main_frosted_taiga
            elif target.img == "Gnoll":
                jump main_prattlefell_meadow
            elif target.img == "Bandit":
                jump main_bandits_hideout
            elif target.img == "Slushy":
                jump main_avalanche_site
            elif target.img == "Spriteling":
                if current_location == temple_of_tapjoo:
                    jump Temple_of_Tapjoo_Loop
                else:
                    jump Puro_Forest_Loop
            elif target.img == "Snowman" or target.img == "Caretaker":
                if current_location == snowbound_summit:
                    jump main_frosted_taiga


    if oa[0] == "U":
        if target.img == "Dummy":
            "You try to surrender to the dummy, pretending to slip and fall on the floor... its stationary stance seem to advise you to leave instead."
            call Battle_Finish from _call_Battle_Finish_45
            jump main_lusterfield_alleyway
        if target.img == "vurro_spar":
            "You raises your hand, Vurro quickly notices and lowers his arms."
            v "Not going any further? We can stop here."
        elif target.img == "Buggbear":
            "You fall to your knees, exhausted of all your energy. You grasp for breath as you lie on the ground, thinking surrendering yourself to the buggbear might be the best choice."

        elif target.img == "Rune Guardian":
            "You fall to your knees, exhausted all your energy, you grasp for breath as you lie on the ground, surrendering yourself to the guardian."
        elif target.img == "Cult Acolyte":
            "You fall to your knees, exhausted all your energy, you grasp for breath as you lie on the ground, surrendering yourself to the cultist in front of you."
            "The acolyte watches in amusement, staring at you in the same stoic mask."
        elif target.img == "Slime" or target.img == "Hefty Slime":
            "You fall to your knees, having exhausted all your energy. You feel the slime has overpowered you in every way possible."
            "With no possible outcome in sight, you surrender yourself to its gooey grasp..."
        else:
            "You fall to your knees, exhausted all your energy, you grasp for breath as you lie on the ground."
            "Maybe surrendering yourself to the [target.name!t] is the best choice."
            if target.img == "Bridgeroot":
                a "Are we giving up?"
            elif target.img == "Werewolf":
                "The beast man jeers at your submission, and he paces around you, poking you to see if you'd still react."
                "You slowly close your eyes and wait for him to decide your fate."
            elif target.img == "Goat Huntsman":
                if goat_num == 1:
                    gt "Ha... At least you are smart enough to give yourself up to our chief. But, since we're here. I have a better plan for you."
                    "He laughs at your submission and looks you up and down. Thinking carefully about his next step..."
                if goat_num == 2:
                    gt "Well... it seems we're done...heh. I thought our general said you're strong... not strong enough."
                    "He looks at you up and down..."

        hide screen battle_buttons
        hide screen battle_enemy_stat
        hide screen battle_player_stat
        call Battle_Finish from _call_Battle_Finish_90
        if target.img == "Goat Huntsman" and quest23.status == 3:
            jump Kari_Goat_Practice_Lose
        jump expression enemy.img.lower().replace(" ","") + "_lose"

    return

label battle_ally_script:

    if oa[0] == "A_S":
        "Amble strikes the core of [enemy.name], causing [target.name] to fall over. He dealt [ally_damage] and stuns [enemy.name] for [stunned.max_rounds] round."
        if oa[1] == "B":
            "The [enemy.name] is staggered, releasing you from his grasp."
    elif oa[0] == "A_F":
        "It doesn't seem to work on the bridgeroot."
    elif oa[0] == "A_D":
        "Amble defends the two of you, increasing your defence in this round."
    return

label level_up_check(exp_drop_min=0, exp_drop_max=0, gold_drop_min=0, gold_drop_max=0):
    $ exp_drop = renpy.random.randint(int(exp_drop_min), int(exp_drop_max))
    $ found_gold = renpy.random.randint(int(gold_drop_min), int(gold_drop_max))
    $ pc.exp += exp_drop
    $ pc.gold += found_gold
    "You have gained [exp_drop] experience points and [found_gold] gold."
    if pc.exp > pc.expCap and pc.level <= levelCap:
        $ pc.LevelUp()
        msg "You are now Level [pc.level]! Check your inventory to allocate your level points."
    return

label lost_gold_check(lost_gold_percentage, base_lost_gold, reset_lust=False):
    $ lost_gold = int(pc.gold * lost_gold_percentage*renpy.random.random()) + base_lost_gold
    "You lost [lost_gold] Gold."
    $ pc.gold -= lost_gold
    if pc.gold < 0:
        $ pc.gold = 0

    if reset_lust == True:
        $ pc.lust = 0
    return

label mimic_battle:


    $ enemy_num = 1
    $ enemy = mimic
    if current_location.img == "Damp Cave":
        $ enemy.max_hp = 180
        $ enemy.defense = 30
    elif current_location.img == "Forest Nightwatch":
        $ enemy.max_hp = 280
        $ enemy.defense = 40
    elif current_location.img == "Whispering Hollow":
        $ enemy.max_hp = 480
        $ enemy.defense = 50
    $ enemy.dodge = 5
    $ enemy.max_damage = 38
    $ enemy.max_damage = 48
    $ enemy.lust_defense = 35
    $ enemy.min_lust_damage = 15
    $ enemy.max_lust_damage = 31
    call beginningBattle from _call_beginningBattle
    $ mimic.beginbattle()
    hide screen dungeon_map
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen dungeon_buttons
    if current_location.img == "Damp Cave":
        scene cave_interior1:
            blur 8
    else:
        scene dark_forest:
            blur 8
    show mimic:
        xalign 0.5
        yalign 0.25
    if pc.weapon == None:
        "You are facing a mimic chest, it is licking its lips, drooling at your body. You raise your fist in response."
    else:
        "You are facing a mimic chest, it is licking its lips, drooling at your body. You raise your [pc.weapon.name!t] in response."
    jump mimic_battle_loop
label mimic_battle_loop:
    show mimic:
        xalign 0.5
        yalign 0.25
    if check_party(pc) == "lost":
        call Battle_Finish from _call_Battle_Finish
        jump mimic_lose
    $ turn_action = ui.interact()
    call Battle_ASF from _call_Battle_ASF
    if oa[0] == "A":
        if oa[1] == "M":
            if oa[3] == "A" or oa[3] == "B":
                "You aim and slash your [pc.weapon.name!t] at the mimic chest, but you simply miss it by inches."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the mimic, but you simply miss it by inches."
            if oa[3] == "N":
                "You throw your fist at the mimic, but you simply miss it by inches."
        else:
            call Enemy_Damaging (target, oa[4]) from _call_Enemy_Damaging_15
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the appendages of the mimic, your blade grazes through the chest."
                "Drops of blood drips through his body."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] at the chest, knocking him sideway."
                "He growls at you before setting himself down with his tentacles, albeit disheveled."
            if oa[3] == "C":
                "You run while shooting your [pc.weapon.name!t] at the mimic, knocking him sideway."
                "He growls at you before setting himself down with his tentacles, albeit disheveled."
            if oa[3] == "N":
                "You punch into the mimic's stomach, grabbing him and slam him on the ground hard."
            if oa[2] == "N":
                "His health decreases by [oa[4]] HP."
            else:
                "You've critically hit the mimic chest, dealing [oa[4]] HP!"
    if oa[0] == "S":
        "You struggle against the mimic, trying to break free. You dealt [oa[4]] damage to the mimic in the process, his grip has loosen as well."
    if oa[0] == "F":
        "As much as you try to grind your hips against the chest interior, he doesn't flinch, or get aroused."
        "It seems that he is already very aroused."
        "You back off before he tries to grab a hold of your body."
    if oa[0] == "E":
        if oa[1] == "M":
            "You slowly back down from the mimic's attack, you turn around and run as fast as you can."
            "The mimic catches you with his appendages and flings your body right back to him. Your escape seems to have failed!"
        else:
            "You slowly back down from the mimic's attack, you turn around and run as fast as you can."
            "The mimic tries to catch you with his appendages but it barely slips from your body, You successfully escaped from the mimic!"
            hide screen battle_buttons
            hide screen battle_enemy_stat
            hide screen battle_player_stat
            show screen dungeon_buttons
            if current_location.img == "Damp Cave":
                jump Damp_Cave_Loop
            elif current_location.img == "Forest Nightwatch":
                jump Dark_Forest1_Loop
            elif current_location.img == "Whispering Hollow":
                jump Whispering_Hollow_Loop
    if oa[0] == "U":
        "You fall to your knees, exhausted all your energy, you grasp for breath as you lie on the ground, surrendering yourself to the mimic."
        "The mimic licks you full of slime while it seems to be prepares its loser for something bigger..."
        if kari_accompany == True:
            k "Courier? W-what are you doing..."
        call Battle_Finish from _call_Battle_Finish_1
        jump mimic_lose
    call Ability_Item from _call_Ability_Item
    if kari_accompany == True:
        call Battle_Kari from _call_Battle_Kari
    call Battle_Mid_Check from _call_Battle_Mid_Check
    if oa[0] == "W":
        call Battle_Finish from _call_Battle_Finish_2
        jump mimic_win
    if oa[0] == "T":
        call Battle_End_Check from _call_Battle_End_Check_14
        jump mimic_battle_loop
    show mimic:
        linear 0.1 zoom 1.04
        linear 0.05 zoom 1
    if mimic.hp > 0 or mimic.lust == mimic.max_lust:
        if check_party(mimic) == "lost":
            call Battle_Finish from _call_Battle_Finish_3
            jump mimic_win
        $ dia = renpy.random.random()
        if dia < 0.50:
            if renpy.random.random()*100 > pc.dodge+extra_dodge:
                $ raw_damage = int(renpy.random.randint(mimic.min_damage, mimic.max_damage))
                $ enemy_damage = damageFormula(raw_damage, pc.defense)
                call Damaging (enemy, pc, enemy_damage) from _call_Damaging_22
                $ random_chance = renpy.random.random()
                if random_chance < 0.5:
                    "The mimic flings his tongue towards you, you are not quick enough to dodge his blow. Your health decreases by [enemy_damage] HP."
                else:
                    "The mimic slaps his tongue onto your head, knocking you on the ground. Your health decreases by [enemy_damage] HP."
            else:
                $ random_chance = renpy.random.random()
                if random_chance < 0.5:
                    "The mimic flings his tongue towards you, but you manage to dodge the attack."
                else:
                    "The mimic tries to slap his tongue onto your head, but he misses it by inches."
        elif dia < 0.67 and bound not in status:
            "The mimic wraps his tongues and appendages around you."
            "He is holding you in place."
            $ status.append(bound)
            $ grip_strength = bound.effect
        else:
            $ raw_flirt = int(renpy.random.randint(mimic.min_lust_damage, mimic.max_lust_damage))
            $ enemy_flirt = damageFormula(raw_flirt, pc.lust_defense)
            $ pc.lust += enemy_flirt
            if pc.lust > pc.max_lust:
                $ pc.lust = pc.max_lust
            $ random_chance = renpy.random.random()
            "The mimic raises his tongue, smearing all his pheromones onto your skin."
            "You instantly gets aroused by his slime. Thinking about how his tongue would fit inside you... Your lust increased by [enemy_flirt]."
        call Battle_End_Check from _call_Battle_End_Check
    jump mimic_battle_loop
label stoneward_battle:


    $ enemy_num = 1
    $ enemy = stoneward
    $ buffed_attack = 0
    if current_location.img == "Damp Cave":
        $ enemy.max_hp = 200
        $ enemy.min_damage = 30
        $ enemy.max_damage = 50
        $ enemy.defense = 23
        scene cave_interior1:
            blur 8
        show stoneward:
            xalign 0.5
            yalign 0.25
    elif current_location.img == "Chelforte Cavern":
        $ enemy.max_hp = 380
        $ enemy.min_damage = 20
        $ enemy.max_damage = 50
        $ enemy.defense = 58
        scene chelforte_cavern:
            blur 8
        show caveward:
            xalign 0.5
            yalign 0.25
    $ enemy.dodge = 10
    $ enemy.lust_defense = 30
    $ enemy.min_lust_damage = 0
    $ enemy.max_lust_damage = 0
    call beginningBattle from _call_beginningBattle_1
    $ stoneward.beginbattle()
    hide screen dungeon_map
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen dungeon_buttons


    if pc.weapon == None:
        "You are facing a stone ward, it seems to be summoned by the guardian. You raise your fist in defence."
    else:
        "You are facing a stone ward, it seems to be summoned by the guardian. You raise your [pc.weapon.name!t] in defence."
    jump stoneward_battle_loop
label stoneward_battle_loop:
    if current_location.img == "Damp Cave":
        show stoneward:
            xalign 0.5
            yalign 0.25
    if current_location.img == "Chelforte Cavern":
        show caveward:
            xalign 0.5
            yalign 0.25
    if check_party(pc) == "lost":
        call Battle_Finish from _call_Battle_Finish_4
        jump stoneward_lose
    $ turn_action = ui.interact()
    call Battle_ASF from _call_Battle_ASF_1
    if oa[0] == "A":
        if oa[1] == "M":
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the arm of the stone ward, but you simply missed him by inches."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] at the stone ward's head, but you simply missed him by inches."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the stone ward, but you simply missed him by inches."
            if oa[3] == "N":
                "You throw your fist at the stone ward, but you simply missed him by inches."
        else:
            call Enemy_Damaging (target, oa[4]) from _call_Enemy_Damaging_16
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the arm of the stone ward, knocking a few pebbles off his body."
                "He growls at you before getting up, albeit disheveled."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] at the stone ward's head, knocking him on the ground."
                "He growls at you before getting up, albeit disheveled."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the stone ward, the arrow hit right into his shoulder."
            if oa[3] == "N":
                "You throw your fist at the stone ward, hitting him right across his face."
                "The sheer impact knocks a few rocks on the ground."
            if oa[2] == "N":
                "His health decreases by [oa[4]] HP."
            else:
                "You've critically hit the stone ward, dealing [oa[4]] HP!"
    if oa[0] == "F":
        "As much as you move your hip and grind your ass against the stone ward, it doesn't seem to flinch."
        "You eventually give up before he can actually latch onto you."
    if oa[0] == "E":
        if oa[1] == "M":
            "You slowly back down from the stoneward's attack, you turn around and run as fast as you can."
            "Suddenly you slip and fall on the ground! Your escape has failed."
        else:
            "You slowly back down from the stone ward's attack, you turn around and run as fast as you can."
            "The stone ward tries to run after you but he is too slow, You successfully escaped from the Stone Ward!"

            hide screen battle_buttons
            hide screen battle_enemy_stat
            hide screen battle_player_stat
            show screen dungeon_buttons
            if current_location.img == "Damp Cave":
                jump Damp_Cave_Loop
            if current_location.img == "Chelforte Cavern":
                jump Chelforte_Cavern_Loop
    if oa[0] == "U":
        "You fall to your knees, exhausted all your energy, you grasp for breath as you lie on the ground, surrendering yourself to the Stone Ward."
        if kari_accompany == True:
            k "Courier? W-what are you doing..."
        call Battle_Finish from _call_Battle_Finish_5
        jump stoneward_lose
    call Ability_Item from _call_Ability_Item_1
    if kari_accompany == True:
        call Battle_Kari from _call_Battle_Kari_1
    call Battle_Mid_Check from _call_Battle_Mid_Check_1
    if oa[0] == "W":
        call Battle_Finish from _call_Battle_Finish_6
        jump stoneward_win
    if oa[0] == "T":
        call Battle_End_Check from _call_Battle_End_Check_15
        jump stoneward_battle_loop
    if current_location.img == "Damp Cave":
        show stoneward:
            linear 0.1 zoom 1.04
            linear 0.05 zoom 1
    if current_location.img == "Chelforte Cavern":
        show caveward:
            linear 0.1 zoom 1.04
            linear 0.05 zoom 1
    $ dia = renpy.random.random()
    if buffed_attack == 1:
        $ buffed_attack = 0
        if current_location.img == "Damp Cave":
            $ raw_damage = int(renpy.random.randint(stoneward.min_damage, stoneward.max_damage)) / 2
        if current_location.img == "Chelforte Cavern":
            $ raw_damage = int(renpy.random.randint(stoneward.min_damage, stoneward.max_damage) / 1.5)
        $ enemy_damage = damageFormula(raw_damage, pc.defense)
        call Damaging (enemy, pc, enemy_damage) from _call_Damaging_23
        pause 1.5
        call Damaging (enemy, pc, enemy_damage) from _call_Damaging_24
        pause 1.5
        call Damaging (enemy, pc, enemy_damage) from _call_Damaging_25

        $ ed = enemy_damage * 3
        "The stone ward aims and flings 3 huge stones at you, it ignores your dodges and hit you right onto your body. Your health decreases by [ed] HP."
    elif dia < 0.50:
        if renpy.random.random()*100 > pc.dodge+extra_dodge:
            $ raw_damage = int(renpy.random.randint(stoneward.min_damage, stoneward.max_damage))
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_26
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The stone ward swings his left arm towards you, you are not quick enough to dodge his blow. Your health decreases by [enemy_damage] HP."
            else:
                "The stone ward charges at you, hitting you with a punch to the chest. Your health decreases by [enemy_damage] HP."
        else:
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The stone ward swings his left arm towards you, but you managed to deflect his attack."
            else:
                "The stone ward charges at you, trying to punch at your chest but you block the blow and push him back."
    elif dia < 0.83 and buffed_attack == 0:
        $ buffed_attack = 1
        "The stone ward holds his fist, saving himself some pebbles."
        "You can feel that he is preparing an attack next round."
    else:
        if current_location.img == "Damp Cave":
            $ healing = int(0.5 * (stoneward.max_hp - stoneward.hp))
            if healing > 60:
                $ healing = 60
        if current_location.img == "Chelforte Cavern":
            $ healing = int(0.4 * (stoneward.max_hp - stoneward.hp))
            if healing > 90:
                $ healing = 90
        "The stone ward uses the power of the flowing water, and recovers [healing] HP."
        $ stoneward.hp += healing

    call Battle_End_Check from _call_Battle_End_Check_1
    jump stoneward_battle_loop
label stoneward_win:
    "As you defeat the stone ward, the ward begins to collapse and turns to dust in front of your eyes."
    "There's nothing useful for now..."
    $ gold_drop = renpy.random.randint(13, 23)
    if current_location.img == "Damp Cave":
        if equippedTrinket("Lindbloom"):
            $ rnd = 0.6
        else:
            $ rnd = 0.3
        if renpy.random.random() <= rnd:
            "Searching around the stone ward, you found a normal stone and a slate rock!"
            $ addItem("Slate Rock", inventory, 1)
            $ addItem("Stone", inventory, 1)
        else:
            "Searching around the stone ward, you found a normal stone!"
            $ addItem("Stone", inventory, 1)

        $ pc.gold += gold_drop
        $ exp_drop = renpy.random.randint(150, 190)
    if current_location.img == "Chelforte Cavern":
        "You search around the stone ward, you found a slate rock..."
        $ addItem("Slate Rock", inventory, 1)
        $ gold_drop = renpy.random.randint(23, 33)
        $ pc.gold += gold_drop
        $ exp_drop = renpy.random.randint(250, 290)
    "You also found [gold_drop] gold and [exp_drop] EXP."
    $ pc.exp += exp_drop
    if pc.exp > pc.expCap and pc.level <= levelCap:
        $ pc.LevelUp()
        msg "You are now Level [pc.level]! Check your inventory to allocate your level points."


    if current_location.img == "Chelforte Cavern":
        if ward_num == 1:
            $ removeSprite(chelforte, cward_sprite1)
        if ward_num == 2:
            $ removeSprite(chelforte, cward_sprite2)
        if ward_num == 3:
            $ removeSprite(chelforte, cward_sprite3)
        scene black
        with dissolve
        pause 1.0
        jump Chelforte_Cavern_Loop
    else:
        if ward_num == 1:
            $ bandit_den.unoccupy(18, 2)
        if ward_num == 2:
            $ bandit_den.unoccupy(9, 6)
        if ward_num == 3:
            $ bandit_den.unoccupy(8, 10)
        scene black
        with dissolve
        pause 1.0
        jump Damp_Cave_Loop

label mimic_win:

    "As you defeat the mimic, the entity seems to disintegrate completely before your eyes."
    "Only leaving behind the content of its original chest."
    "You search around the mimic, and found a chest key."
    $ gold_drop = renpy.random.randint(24, 40)
    $ exp_drop = renpy.random.randint(160, 200)
    "You found [gold_drop] gold and [exp_drop] EXP."
    $ pc.exp += exp_drop
    $ pc.gold += gold_drop
    if pc.exp > pc.expCap and pc.level <= levelCap:
        $ pc.LevelUp()
        msg "You are now Level [pc.level]! Check your inventory to allocate your level points."

    if mimic_num == 1:
        $ bandit_den.unoccupy(15, 7)
    if mimic_num == 2:
        $ bandit_den.unoccupy(1, 12)
    if mimic_num == 3:
        $ bandit_den.unoccupy(16, 12)
    if mimic_num == 5:
        $ dark_forest1.unoccupy(1, 2)
    if mimic_num == 4:
        $ whispering_hollow.unoccupy(8, 7)
    scene black
    with dissolve
    pause 1.0

    if current_location.img == "Forest Nightwatch":
        jump Dark_Forest1_Loop
    elif current_location.img == "Whispering Hollow":
        jump Whispering_Hollow_Loop
    else:
        jump Damp_Cave_Loop


label stoneward_lose:

    hide screen dungeon_buttons
    hide screen dungeon_map
    if kari_accompany == True:
        "You fell on the ground, the stone ward walks towards you."
        "You faint soon after seeing the ward."
        "..."
        scene black
        with dissolve
        pause 1.0
        scene damp_cave
        with dissolve
        show kari masked
        with dissolve
        $ pc.hp = pc.max_hp
        k "You... woke up?"
        e "Ahh... where am I..."
        k "Outside of the cave. I healed you for a bit."
        e "Thanks, Kari."
        k "You lost to a rock."
        e "Uhmm... I don't know..."
        k "Whatever, I'm waiting here."
        k "Just come back to the cave when you're ready."
        k "I still have to save Furkan..."
        e "A-alright..."
    else:
        "You fell on the ground, the stone ward walks towards you."
        "You faint soon after seeing the ward."
        "When you wake up, you discovered that you are already outside of the cave..."
        "You wonder what happened when you passed out..."
        "But you decide to pick up your items and continue on your adventure."
    if current_location.img == "Damp Cave":

        $ gold_lost = int(30 + renpy.random.random()*0.3*pc.gold)
        $ pc.gold -= gold_lost
        if pc.gold < 0:
            $ pc.gold = 0
        if pc.hp <= 0:
            $ pc.hp = 1
        "You lost [gold_lost] gold."
        scene black
        with dissolve

        pause 1.0
        jump main_damp_cave
    if current_location.img == "Chelforte Cavern":
        $ gold_lost = int(30 + renpy.random.random()*0.3*pc.gold)
        $ pc.gold -= gold_lost
        if pc.gold < 0:
            $ pc.gold = 0
        if pc.hp <= 0:
            $ pc.hp = 1
        "You lost [gold_lost] gold."
        scene black
        with dissolve
        call Leaving_Chelforte from _call_Leaving_Chelforte_1
        pause 1.0

        jump Dark_Forest_Map

label mimic_lose:
    hide screen dungeon_buttons
    hide screen dungeon_map
    "You fell on the ground, the mimic's tongue is about to slither towards you."
    "There's no strength left inside you to struggle against its grasp, it is bringing you into its own mouth..."
    if kari_accompany == True:
        "Just as the mimic is about to engulf you whole, Kari strikes his scepter against the chest and it releases its grip."
        "You fall on the ground hard. Kari carries your half-limp body out of the dungeon and into somewhere safe."
        scene black
        with dissolve
        pause 1.0
        scene damp_cave
        with dissolve
        show kari masked
        with dissolve
        $ pc.hp = pc.max_hp
        k "You... woke up?"
        e "Ahh... where am I..."
        k "Outside of the cave. I healed you for a bit."
        e "Thanks, Kari."
        k "You lost to a chest."
        e "Uhmm... I don't know..."
        k "Whatever, I'm waiting here."
        k "Just come back to the cave when you're ready."
        k "I still have to save Furkan..."
        e "A-alright..."
    else:
        menu:
            "Do you want to play the lose scene?"
            "Yes{#mimiclose}":
                call scene_mimiclose from _call_scene_mimiclose
            "Skip{#mimiclose}":
                pass
        "You stand up... feeling something inside you had changed."
        "You can't point out what happened or what changed, but your body feels... weird after losing to the mimic."
        "Like... it's not your own."
    $ pc.add_active_status(stuffed)
    $ pc.add_active_status(soremouthed)
    call lost_gold_check (0.4, 50, True) from _call_lost_gold_check_7
    $ pc.cor -= 2
    if pc.cor < 0:
        $ pc.cor = 0
    scene black
    with dissolve
    pause 1.0

    if current_location.img == "Forest Nightwatch":
        $ dark_forest1.unoccupy(tenki_sprite3.x, tenki_sprite3.y)
        $ dark_forest1.unoccupy(werewolf_sprite.x, werewolf_sprite.y)
        $ dark_forest1.unoccupy(werewolf_sprite2.x, werewolf_sprite2.y)
        $ dark_forest1.unoccupy(werewolf_sprite1.x, werewolf_sprite1.y)
        $ dark_forest1.unoccupy(werewolf_sprite3.x, werewolf_sprite3.y)
        $ dark_forest1.unoccupy(barrel_sprite1.x, barrel_sprite1.y)
        $ dark_forest1.unoccupy(barrel_sprite2.x, barrel_sprite2.y)
        $ dark_forest1.unoccupyback(wooddoor_sprite2.x, wooddoor_sprite2.y)

        jump main_dark_forest
    elif current_location.img == "Whispering Hollow":

        call Leaving_Whispering_Hollow from _call_Leaving_Whispering_Hollow_2
        jump main_dark_forest
    else:
        jump main_damp_cave

label runeguardian_battle:


    $ enemy_num = 1
    $ grip_strength = 100
    $ enemy = runeguardian
    $ buffed_attack = 0
    if current_location == temple_of_tapjoo:
        $ enemy.max_hp = 600
        $ enemy.min_damage = 45
        $ enemy.max_damage = 69
        $ enemy.min_lust_damage = 13
        $ enemy.max_lust_damage = 21
        $ enemy.dodge = 19
        $ enemy.defense = 49
        $ enemy.lust_defense = 39
        $ enemy.exp_drop = 85
        scene temple_of_tapjoo:
            blur 8
    else:
        $ enemy.max_hp = 400
        $ enemy.min_damage = 35
        $ enemy.max_damage = 55
        $ enemy.min_lust_damage = 13
        $ enemy.max_lust_damage = 21
        $ enemy.dodge = 12
        $ enemy.defense = 30
        $ enemy.lust_defense = 35
        $ enemy.exp_drop = 85
        scene cave_interior1:
            blur 8

    call beginningBattle from _call_beginningBattle_2
    $ runeguardian.beginbattle()
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen dungeon_buttons

    $ enemy_image = "moss_golem"
    with dissolve
    "It is a Rune Guardian. He is standing before you, he looks enraged by your intrusion."
    "You can feel his blue aura radiates across the cave."
    if pc.weapon != None:
        "You raise your [pc.weapon.name!t], defending yourself from the guardian's attack."
    else:
        "You raise your fist, defending yourself from the guardian's attack."

    jump general_battle_loop

label runeguardian_battle_loop:

    if buffed_attack == 1:
        $ buffed_attack = 0
        $ raw_damage = int(renpy.random.randint(stoneward.min_damage, stoneward.max_damage)) / 2
        $ enemy_damage = damageFormula(raw_damage, pc.defense)
        call Damaging (enemy, pc, enemy_damage) from _call_Damaging_27
        pause 1.5
        call Damaging (enemy, pc, enemy_damage) from _call_Damaging_28
        pause 1.5
        call Damaging (enemy, pc, enemy_damage) from _call_Damaging_29
        $ ed = enemy_damage * 3
        "The Rune Guardian aims and flings 3 huge stones at you, it ignores your dodges and hit you right onto your body. Your health decreases by [ed] HP."
    $ dia = renpy.random.random()
    if dia < 0.13 and bound not in status:
        "The Rune Guardian holds you in place with his right arm. You try to struggle free but it doesn't work."
        $ status.append(bound)
        $ grip_strength = bound.effect
    elif dia < 0.66:
        if renpy.random.random()*100 > pc.dodge+extra_dodge:
            $ raw_damage = int(renpy.random.randint(runeguardian.min_damage, runeguardian.max_damage))
            $ enemy_damage = raw_damage * (100 - pc.defense) / 100
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_30
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The guardian swing his fist toward your direction, hitting you in the chest. Your health decreases by [enemy_damage] HP."
            else:
                "The guardian strike you down with his vines, you pass out for a few seconds before getting up. Your health decreases by [enemy_damage] HP."
        else:
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The guardian swing his fist toward your direction, but you manage to dodge his blow."
            else:
                "The guardian tries to strike you down with his vines, but he missed the attack just by inches."
    elif dia < 0.87 and buffed_attack == 0:
        $ buffed_attack = 1
        "The guardian prepares for his magic... you feel like his next attack would hurt a lot more."
        if kari_accompany == True and not current_location == temple_of_tapjoo:
            k "Courier, watch out for his attack!"
    else:
        "The Rune Guardian channels the water into an orb of regeneration, his body becomes revitalised by the power of water."
        $ healing = int(renpy.random.randint(runeguardian.min_damage, runeguardian.max_damage)*1.5)

        "He has recovered [healing] HP."
        $ runeguardian.hp += healing
        if runeguardian.hp >= runeguardian.max_hp:
            $ runeguardian.hp = runeguardian.max_hp
    call Battle_End_Check from _call_Battle_End_Check_2
    jump general_battle_loop

label runeguardian_win:
    hide moss_golem

    if current_location == temple_of_tapjoo:
        jump Temple_Grand_Chamber_Encounter

    scene cave_interior1

    "The Rune Guardian collapse on the ground, you stare at the guardian, its blue marks are glowly weakly."
    if kari_accompany == True:
        show kari masked
        with dissolve
    if bandit_den.inventory != None and bandit_den.inventory.img == "rock_sprite":
        menu:
            "Should you use the rock you picked up on the guardian?"
            "Yes{#userockonguardian}":
                $ guardian_alive = True
                "Holding the stone against the golem. The shell of the rock crumbles and reveals a rune crystal right before your eyes."
                if kari_accompany == True:
                    k "W-what?"
                    e "I think it's glowing..."
                    k "..."
                "The rune fuses into the chest of the dying guardian, and the whole cave glows with bright blue energy."
                with flash
                pause 0.5
                "Soon, everything returns to normal, except that the guardian seems to not disintegrate like the last one did."
                if kari_accompany == True:
                    k "It was a weird stone... how did you know it'd save the guardian?"
                    e "I don't know... I just thought it looked cool."
                    k "I think the stone contains some... remnant of the rune..."
                    k "..."
                    k "At least we can salvage Naim now."
                    e "Is it this guardian's name?"
                    k "Yes."
                    e "..."
                    k "Let him rest here a little."
                "The guardian stays unconscious after the fight, you decide to check in on Furkan at the back."
                jump Damp_Cave_End
            "No{#userockonguardian}":
                $ bandit_den.unoccupy(20, 12)
                pass
    "Soon, the guardian crumbles into dust, just like the last one."
    if kari_accompany == True:
        k "Hmm..."
        k "Now both of them are gone now..."
    "Stepping over the dust that the guardian leaves behind, you decide to check in on Furkan at the back."
    jump Damp_Cave_End

label Damp_Cave_End:
    if kari_accompany == True:
        k "Hey, Furk. Furk! You alright?"
        "The Ram doesn't speak, in fact he still hasn't wake. Kari presses on his chest for a few moment."
        k "Alright, he's alive. Furk."
        "Kari performs healing magic to the unconscious ram."
        "Furkan's eyes flutter open, as an anticipated deer watches in relief."
        f "..."
        k "Furk?"
        show kari masked at r1
        with move
        show furkan normal at l1
        with dissolve
        f "...W-where am I?"
        show kari masked:
            linear 1.0 xalign 0.5
        "Kari hugs the chief tightly, he positions himself on top of Furkan, feeling all his warmth as you watch from a distance."
        k "Furk, you almost scared me to death. I thought you were gone."
        f "Uhm... the cave... I came here looking for the golem did I not?"
        "Kari nods."
        e "Hey, Furkan."
        f "The courier? Why are you here."
        e "Kari asked me to come with him to save you."
        e "Did you pass out after the guardian attacked you?"
        f "No, it was someone else... the guardian was protecting me."
        k "Please tell me who attacked you, Furkan. I will take my own revenge on them."
        f "They hit me from the back, I have no idea."
        "Kari looks disappointed, it seems he cares about the chief a lot by the way he's still hugging him."
        f "W-wait..."
        f "I lost it."
        k "Father's basin?"
        show kari masked at r1 with move
        "The general pulls away, looking at Furkan with concern."
        k "Oh... No."
        e "W-what's it?"
        k "We used it to summon our guardians, or what you called golem."

        if guardian_alive:
            f "Is the guardian doing well?"
            k "Courier used a rock on him, I saw it."
            "You nods slightly as the chief gives you an approving smile."
            "But the smile fades away quickly as he looks back at Kari."
            f "It was stupid of me to come here alone. I did not intend for anyone to follow me."
            f "But that made the perfect opportunity for an ambush."
            f "How silly I am..."
            k "Furk... it's fine. we can find the basin later."
        else:

            f "Where's the guardian?"
            k "We killed it. We thought he went rogue on you and he started attacking us."
            f "Alright."
            "Furkan sighs, he looks down, eyes almost teary."
            "He doesn't speak, instead, he grasps on Kari's hand. The general doesn't seem to flich away."
            "Both of them are just mourning, in their own way."
            f "So, all of what I did was for nothing."
            f "Guardian died, basin got stolen."
            e "W-what's the basin actually?"
            f "It was what my father used to summon guardians, with the help of the runes."
            f "In return, the guardians protect the runes."
            f "And now I lost both of them."
            "Kari rubs his paws on Furkan's wound, tending to it carefully."
            e "I'm really sorry to hear, but we'll try to get them back when you recover."

        f "Thanks, both of you. I need to get back to the tribe now."
        with vpunch
        f "Hmm..."
        "Furkan stumbles forward when he tries to stand up, you see Kari intuitively lifts him back up."
        f "Kari?"
        k "Yeah... Let's go."
        e "Oh... you guys... are going?"
        "Kari carries the furkan's exhausted body on his back. The two men grunts a little before walking."
        k "U-uhm... Thanks, Courier."
        k "Here's some recipe that you might want to take a look."
        k "It's iron sword and axe."
        e "Thanks, general."
        "He hands you the paper, before tugging the chieftain upwards with his hands on his ass."
        k "I'll take our Chief back to our tribe, see you later."
        f "Take care."
        e "See you..."
        "Kari turns away from you, and begin walking towards the exit."
        k "{size=20}Furk, since when did you get this heavy.{/size}"
        "They whispers, but the echo in the cave makes it clear even from afar."
        f "{size=20}Uhmm... Heavier if I fall asleep on your shoulder...{/size}"
        "Kari and Furkan leaves you outside the cave."
        $ kari_accompany = 2
        $ kechioeren.discovered = True
        $ discoveredrecipe.append(ironswordrecipe)
        $ discoveredrecipe.append(ironaxerecipe)
        $ QuestFinish(quest11)
    else:
        show furkan normal
        with dissolve
        e "Fuck, Furkan? Are you awake?"
        "The Ram is completely passed out, you decide to presses on his chest for a few moment."
        "With no avail, you lean your head against his chest, luckily his heart is still beating, albeit weakly."
        "You cast a weak healing magic on him."
        f "..."
        "The chief's eyes flutter open. He looks stressful, and his pupils dilate."
        f "...W-who..."
        e "Hey, Furkan. Are you alright?"
        "He turns his attention to you."
        f "Courier? Why are you here."
        e "Your general told me to save you here..."
        e "He's resting in the tribe now."
        "You try to give him a hand as he shifts his position to you, but he doesn't take it."
        f "W-what happened."
        e "He fought me as I entered your tribe, I defeated him at the end."
        e "I didn't intend to, just trying to protect myself. He thought I kidnapped you."
        e "Afterwards he told me you might be here..."
        "Furkan stares forwards, seemingly pondering something you're not aware of."
        e "Uhm... Furkan... did you pass out after the guardian attacked you?"
        f "No... it was someone else... the guardian was protecting me."
        "He looks around, distressed."
        f "W-wait..."
        f "I lost it."
        f "I lost the basin."
        f "Oh... no no no..."
        e "W-what? The basin?"
        f "Fuck! Why am I so useless."
        f "They stole the basin from me. The thieves."
        e "Who took it? I didn't see anyone else here in the cave."
        f "They're probably gone, I did not get to catch a glimpse but I sensed someone was there."
        f "...Right before I was ambushed from behind."
        e "It's ok, Furkan. We can get it back later. You should focus on recovering first."
        "You lend your hand again towards Furkan, this time he reluctantly accepts it."
        "With your assistance, Furkan turns against a huge rock to lean on."
        if guardian_alive:
            f "Is the guardian doing well?"
            e "Yes, the stone was healing him quite a bit."
            f "What stone?"
            "You show him the rock you found at the lake, apparently it's been soaked in magical energy enough to heal a golem."
            f "Thank god."
            "Furkan sighs, he is looking at the guardian, panting."
            f "It was stupid of me to come here alone. I know the guardian is here."
            "He looks down, hands over his face."
            f "But that made the perfect opportunity for an ambush."
            f "How silly am I..."
            e "Look, don't worry about it..."
        else:

            f "Where's the guardian?"
            e "He attacked me... So I killed it."
            f "Alright."
            "Furkan sighs, he looks down, eyes almost teary."
            f "So, all of what I did was for nothing."
            f "Guardian died, basin got stolen."
            e "W-what's the basin actually?"
            f "It was what my father used to summon guardians, with the help of the runes."
            f "In return, the guardians protect the runes."
            f "And now I lost both of them."
            "He turns away, ears droop low."
            e "I'm really sorry to hear, but we'll try to get them back when you recover."

        f "Thanks, Courier. I need to get back to the tribe now."
        with vpunch
        f "Hmm..."
        "Furkan stumbles forward when he tries to stand up. He lands on the floor again with a loud thump."
        f "..."
        f "Courier, can you ask Kari to send his people here?"
        e "Do you need a hand?"
        f "No need. You've been a great help already. I just need the guards to take me back."
        e "Alright."
        if guardian_alive:
            e "What about the guardian?"
            f "I suppose we will carry it back."
            f "Not sure if he will still go rogue, so we will put him in captivity."
            f "There is just nothing left for it to protect."
            "Furkan takes another pause."

        f "You can leave me here now... Thank you again, Courier."
        $ quest11.qComp(__("Inform Kari of the Chief's safety."))
        $ quest11.status = 3

    scene damp_cave
    with dissolve
    "..."
    "You still don't understand a lot of it... The magical runes, the guardians. the basin..."
    "But maybe there's more to it than you'd imagine."
    "Maybe it all links back to why you arrive to this world in the first place."
    "You desperately want it to be this case."
    "If it is a nightmare, maybe you can find a way to wake up."
    "Though..."
    "What's even wrong with indulging yourself in this, nightmare?"
    "You've never been in charge for the longest of your life."
    "The world you lived in, in the tribe. It was... bland, unfruitful."
    "You don't even remember any other person there, except for Chime."
    "But here you feel like you are doing something. You have the power to change something, for better or worse."
    "Here, you feel powerful, you feel as if there's a flame inside you, waiting to rekindle."
    "You don't ever want to leave behind the friends you've made, if you ever found an exit."
    "Still, what happened to Chime is not a question you can leave unanswered for long."
    "..."
    "Quickly... you put all unnecessary thought in the back of your head."
    "And you continue on your journey in this world."
    $ kechioeren.discovered = True
    $ bandit_den.mappy[9][20] = MapTile()
    $ bandit_den.mappy[10][20] = MapTile()
    hide screen dungeon_buttons
    hide screen dungeon_map


    jump main_damp_cave

label runeguardian_lose:
    hide moss_golem
    if current_location == temple_of_tapjoo:
        e "No!"
        with flash
        "You fall on the ground hard, your world fades to black before you can register anything..."
        menu:
            "Back to Main Menu":
                $ MainMenu(confirm=False)()


    if kari_accompany == True:
        "You fall on the ground, the guardian is trying to approach you."
        "There's no strength left inside you to struggle against his grasp..."
        "Just as the guardian is about to cast his lethal spell, Kari strikes his scepter against the guardian and pull you off."
        "Kari carries your half-limp body out of the dungeon and into somewhere safe."
        scene black
        with dissolve
        pause 1.0
        scene damp_cave
        with dissolve
        show kari masked
        with dissolve
        $ pc.hp = pc.max_hp
        k "You... woke up?"
        e "Ahh... where am I..."
        k "Outside of the cave. I healed you for a bit."
        e "Thanks, Kari."
        k "Furkan was just there..."
        e "Uhmm... I don't know..."
        k "Whatever, I'm waiting here."
        k "Just come back to the cave when you're ready."
        k "I still have to save Furkan..."
        e "A-alright..."
    else:
        "The guardian stares at your vulnerable state, but he doesn't stop here. You realise that you are not making out of this alive..."
        "He casts another spell. Completely binding your body under his control."
        with vpunch
        e "No..."
        scene black
        with dissolve
        "You pass out right before you can sense any pain, you don't know if you should consider this lucky or unlucky..."
        "You think about whether Furkan would survive, you are right in front of him when you passed out."
        "You wonder what he would think when see you like this..."
        "But... it doesn't matter you are gone now."
        "This is the end of your journey."
        msg "You died."
        menu:
            "Back to Main Menu":
                $ MainMenu(confirm=False)()
            "Restart Dungeon":
                $ pc.hp = saved_hp
                $ pc.mp = saved_mp
                $ pc.lust = saved_lust

                jump main_damp_cave
    $ gold_lost = 50 + renpy.random.random()*0.4*pc.gold
    $ pc.gold -= gold_lost
    if pc.gold < 0:
        $ pc.gold = 0
    $ pc.cor -= 2
    if pc.cor < 0:
        $ pc.cor = 0
    "You lost [gold_lost] gold."
    scene black
    with dissolve
    pause 1.0

    jump main_damp_cave
label minostatue_battle:


    $ minostatue.max_hp = 5

    $ enemy_num = 1
    $ enemy = minostatue
    $ minostatue.beginbattle()
    call beginningBattle from _call_beginningBattle_11
    hide screen dungeon_map
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen dungeon_buttons
    scene mino_cave:
        blur 8
    show mino_statue:
        xalign 0.5
        yalign 0.25
    if pc.weapon == None:
        "You are facing the statue of minotaur, You feel that this battle will be quite different than you are used to. You raise your fist."
    else:

        "You are facing the statue of minotaur, You feel that this battle will be quite different than you are used to. You raise your fist instead of your [pc.weapon.name!t]."

    jump minostatue_battle_loop
label minostatue_battle_loop:
    show mino_statue:
        xalign 0.5
        yalign 0.25
    $ fortify = False
    if check_party(pc) == "lost":
        call Battle_Finish from _call_Battle_Finish_10
        jump minostatue_lose
    $ players_turn = True
    $ turn_action = ui.interact()
    if turn_action == "Attack":
        "You throw your punch at the statue. Regardless of your strength, the statue's health dropped by 1."
        $ minostatue.hp -= 1
    if turn_action == "Flirt":
        "The statue seems to be unfazed by all your attempts at seduction..."
        jump minostatue_battle_loop
    if turn_action == "Escape":
        "You cannot escape from the battle."
        jump minostatue_battle_loop
    call Ability_Item from _call_Ability_Item_3
    if turn_action == "Surrender":
        "You fall to your knees, exhausted all your energy, you grasp for breath as you lie on the ground, surrendering yourself to the Statue."
        call Battle_Finish from _call_Battle_Finish_11
        jump minostatue_lose
    $ players_turn = False
    if minostatue.hp < 0:
        $ minostatue.hp = 0
    if check_party(minostatue) == "lost":
        call Battle_Finish from _call_Battle_Finish_12
        jump minostatue_win
    $ dia = renpy.random.random()
    $ raw_damage = int(renpy.random.randint(5, 12))
    $ enemy_damage = damageFormula(raw_damage, pc.defense)
    "The statue casts a few pebbles onto you, each dealing [enemy_damage] HP."
    $ ed = enemy_damage * 5
    call Damaging (enemy, pc, enemy_damage) from _call_Damaging_31
    pause 1
    call Damaging (enemy, pc, enemy_damage) from _call_Damaging_32
    pause 1
    call Damaging (enemy, pc, enemy_damage) from _call_Damaging_33
    pause 1
    call Damaging (enemy, pc, enemy_damage) from _call_Damaging_34
    pause 1
    call Damaging (enemy, pc, enemy_damage) from _call_Damaging_35
    "Your health decreased by [ed] in total."
    call Battle_End_Check from _call_Battle_End_Check_3
    jump minostatue_battle_loop
label minostatue_win:

    "As you defeat the statue, it begins to glow in green in front of your eyes."
    if ten_num == 1:
        $ mino_maze.unoccupy(2, 15)
        $ addSprite(mino_maze, tenfigurine_sprite3)
    if ten_num == 2:
        $ mino_maze.unoccupy(3, 11)
        $ addSprite(mino_maze, tenfigurine_sprite4)
    if mino_maze.mappy[11][3].user.img == "tenfigurine_sprite2" and mino_maze.mappy[15][2].user.img == "tenfigurine_sprite2":
        "You feel that the gem flickered for a moment. You must have completed something..."


    $ gold_drop = renpy.random.randint(15, 25)
    $ pc.gold += gold_drop
    $ exp_drop = renpy.random.randint(150, 190)
    "You also found [gold_drop] gold and [exp_drop] EXP."
    $ pc.exp += exp_drop
    if pc.exp > pc.expCap and pc.level <= levelCap:
        $ pc.LevelUp()
        msg "You are now Level [pc.level]! Check your inventory to allocate your level points."


    scene black
    with dissolve
    pause 1.0
    jump Minotaur_Maze_Loop
label minostatue_lose:
    "You lost to the statue. It seems to be unfazed still."
    "You return to your position."
    if pc.hp <= 0:
        $ pc.hp = 1
    jump Minotaur_Maze_Loop
label mino_battle:



    $ enemy_num = 1
    $ grip_strength = 100
    $ enemy = mino
    $ enemy_extra_damage = 0
    hide screen dungeon_map

    $ mino.beginbattle()
    call beginningBattle from _call_beginningBattle_12
    show screen battle_enemy_stat()
    show screen battle_buttons
    show screen battle_player_stat
    hide screen dungeon_buttons
    scene mino_cave:
        blur 8
    show minotaur:
        xalign 0.5
        yalign 0.25
    with dissolve
    "The minotaur is standing before you, he looks enraged by your intrusion."
    "You can feel his... member dangling in front of you, that must be what the scripture described as hard, and majestic."
    if pc.weapon != None:
        "You raise your [pc.weapon.name!t], defending yourself from the minotaur's attack."
    else:
        "You raise your fist, defending yourself from the minotaur's attack."

    jump mino_battle_loop
label mino_battle_loop:

    show minotaur:
        xalign 0.5
        yalign 0.25
    if check_party(pc) == "lost":
        call Battle_Finish from _call_Battle_Finish_13
        jump mino_lose
    $ turn_action = ui.interact()
    call Battle_ASF from _call_Battle_ASF_3
    if oa[0] == "A":
        if oa[1] == "M":
            if oa[3] == "A":
                "You slash your [pc.weapon.name!t] at the arm of the minotaur, but he dodges the attack in time."
            if oa[3] == "B":
                "You slam your [pc.weapon.name!t] at the minotaur's head, but he dodges the attack in time."
            if oa[3] == "C":
                "You aim and shoot your [pc.weapon.name!t] at the minotaur, but it seems to have missed."
            if oa[3] == "N":
                "You throw your fist at the minotaur, but you punch into the air instead."
        else:
            call Enemy_Damaging (target, oa[4]) from _call_Enemy_Damaging_17
            if oa[3] == "A" or oa[3] == "B":
                if renpy.random.random() > 0.5:
                    "You slash your [pc.weapon.name!t] at the arm of the minotaur, your blade scraps against his fur."
                    "The minotaur stomps on the ground, clearly protesting against your attack."
                else:
                    "You slash your [pc.weapon.name!t] across the minotaur's body, knocking him back a few steps."
                    "The minotaur grunts silently in anger."
            if oa[3] == "C":
                if renpy.random.random() > 0.5:
                    "You aim and shoot your [pc.weapon.name!t] at the minotaur, the arrow hits right into his arm."
                    "The minotaur stomps on the ground, clearly protesting against your attack."
                else:
                    "You run while shooting your [pc.weapon.name!t] across the minotaur's body, knocking him back a few steps."
                    "The minotaur grunts silently in anger."
            if oa[3] == "N":
                if renpy.random.random() > 0.5:
                    "You throw your fist at the arm of the minotaur, your blade scraps against his fur."
                    "The minotaur stomps on the ground, clearly protesting against your attack."
                else:
                    "You punch into the minotaur's stomach, knocking him back a few steps."
                    "The minotaur grunts silently in anger."
            if oa[2] == "N":
                "His health decreases by [oa[4]] HP."
            else:
                "You've critically hit the minotaur, dealing [oa[4]] HP!"
    if oa[0] == "S":
        "You struggle against the arm of the minotaur, trying to break free. You dealt [oa[4]] damage to the minotaur in the process, his grip has loosen as well."
    if oa[0] == "F":
        $ dia = renpy.random.random()
        if status == "Bound":
            "You struggle against the minotaur as you try to reach under the minotaur's crotch, trying to get a reaction from the minotaur."
            "The minotaur instanly react with your advance, grunting profusely as his cock twitches. His grip is weakening as well."
        else:
            if dia > 0.334:
                "You turn around and rub your hand all over your own burly cheeks, feeling and brushing against your ass while you shake your hip."
            elif dia > 0.667:
                "You scrape your member lightly, running your claw from your inner thigh to the back of your balls, you tug at it tightly while staring at the Rune minotaur seductively."
            else:
                "You cup at your fluffy chest, drawing circles around the area of your nipples. You smile at the Rune minotaur while your chest bounce up and down slightly."
            "You approach to the minotaur closely, letting your hands wander inside the huge bush in his crotch area."
            if oa[1] == "M":
                "You continue your act for about a minute, but the minotaur doesn't even flinch."
                "Disappointed, you back away before the minotaur can grab a hold of you."
            else:
                if mino.lust > mino.max_lust / 2:
                    if renpy.random.random() > 0.5:
                        "Within a few seconds you can already see some movements in his cock."
                        "The minotaur doesn't say anything, except for licking his lips. His lust is increased by [player_flirt]."
                        mn "...H...Hnnnnngh..."
                    else:
                        "You notice the minotaur is floundering, trying his best not to get aroused by your seduction."
                        "But it is evident that his flushed face tells it all. His lust is increased by [player_flirt]."
                        mn "No... more... cum..."
                else:
                    if renpy.random.random() > 0.5:
                        "The minotaur is squirming in reaction to your advance."
                        "You can already hear his rapid breathing and grunting. His lust is increased by [player_flirt]."
                        mn "Hnnngh... As..ass...?"
                    else:
                        "You can tell the minotaur is already playing with himself when his hand nudges against his erect cock, staring at your ass intently."
                        "His lust is increased by [player_flirt]."
                        mn "No..."
                "You can tell by the minotaur's fury, he now deals much more damage, as his lust increases."
    if oa[0] == "E":
        "As much as you try, you cannot escape from the barrier behind you."
        jump mino_battle_loop
    if oa[0] == "U":
        "You fall to your knees, exhausted all your energy, you grasp for breath as you lie on the ground, surrendering yourself to the minotaur."
        call Battle_Finish from _call_Battle_Finish_14
        jump mino_lose
    call Ability_Item from _call_Ability_Item_4

    call Battle_Mid_Check from _call_Battle_Mid_Check_3
    if oa[0] == "W":
        mn "U-ughh...not a-again..."
        "The minotaur falls with a loud thud on the ground."
        call Battle_Finish from _call_Battle_Finish_15
        jump mino_win
    if oa[0] == "T":
        call Battle_End_Check from _call_Battle_End_Check_17
        jump mino_battle_loop
    show minotaur:
        linear 0.1 zoom 1.04
        linear 0.05 zoom 1
    $ dia = renpy.random.random()
    if dia < 0.10 and status == None:
        "The minotaur holds you in place with his right arm. You try to struggle free but it doesn't work."
        $ status = "Bound"
        $ grip_strength = 100
    elif dia < 0.55:
        if renpy.random.random()*100 > pc.dodge+extra_dodge:
            $ new_max = mino.max_damage + int(mino.lust/mino.max_lust*30)
            $ raw_damage = int(renpy.random.randint(mino.min_damage, new_max)) + enemy_extra_damage * 5
            $ enemy_damage = damageFormula(raw_damage, pc.defense)
            call Damaging (enemy, pc, enemy_damage) from _call_Damaging_36
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The minotaur swing his fist toward your direction, hitting you in the chest. Your health decreases by [enemy_damage] HP."
            else:
                "The minotaur strike you down with his palm, you pass out for a few seconds before getting up. Your health decreases by [enemy_damage] HP."
        else:
            $ random_chance = renpy.random.random()
            if random_chance < 0.5:
                "The minotaur swing his fist toward your direction, but you manage to dodge his blow."
            else:
                "The minotaur tries to strike you down with his palm, but he missed the attack just by inches."
    else:
        "The minotaur chants and sings a warsong, his damage seems to have been increased."
        $ enemy_extra_damage += 1
    if bound in status:
        "You can still feel yourself being wrapped around by the minotaur's strong arm, refusing to let you go."
        "He buries your face into his warm and fuzzy chest, your lust has increased by 9."
        $ pc.lust += 9
    call Battle_End_Check from _call_Battle_End_Check_4
    jump mino_battle_loop

label mino_win:
    "You have won against the minotaur."
    if quest14.status != True:
        "You take out the vial that Haskell asked you to bring..."
    menu:
        "Do you want to play the scene?"
        "Yes{#fuckmino}":
            call scene_minowin from _call_scene_minowin
            $ pc.lust = 0
        "No{#fuckmino}":
            pass

    if equippedTrinket("Lindbloom"):
        $ rnd = 0.6
    else:
        $ rnd = 0.3
    if renpy.random.random() <= rnd:
        "You retrieved two bottle of minotaur's essence."
        $ addItem("Minotaur Essence", inventory, 2)
    else:
        "You retrieved a bottle of minotaur's essence."
        $ addItem("Minotaur Essence", inventory, 1)

    $ gold_drop = renpy.random.randint(25, 40)
    $ pc.gold += gold_drop
    $ exp_drop = renpy.random.randint(200, 300)
    "You also found [gold_drop] gold and [exp_drop] EXP."
    $ pc.exp += exp_drop
    if pc.exp > pc.expCap and pc.level <= levelCap:
        $ pc.LevelUp()
        msg "You are now Level [pc.level]! Check your inventory to allocate your level points."
    "You leave the dungeon soon after."
    $ removeSprite(mino_maze, mino_maze.playerSprite)
    jump main_gloomy_mountainside
label mino_lose:
    "You lost against the minotaur...he seems to be very satisfied with your slumped form."
    menu:
        "Do you want to play the scene?"
        "Yes{#minofuck}":
            call scene_minolose from _call_scene_minolose
        "No{#minofuck}":
            pass
    $ pc.add_active_status(stuffed)
    $ removeSprite(mino_maze, mino_maze.playerSprite)
    if pc.hp <= 0:
        $ pc.hp = 1
    $ pc.lust = 0
    jump main_gloomy_mountainside
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
