style quest_title_text:
    color "#29170b"
    font "kingthing.ttf"
    size 40

style quest_content_text:
    color "#422511"
    size 20


default quest_line_breaker = "======================================"
style quest_line_breaker_text:
    color "#332040"
    font "leafy.otf"
    size 14


screen qlog():
    $ quest_line_breaker = "======================================"
    $ remove_duplicate_delivery_tasks()
    zorder 90 tag menu_bar

    add "bgjournal"
    if journalPage == "Quest":

        imagebutton:
            xalign 0.2
            yalign 0.015
            idle "quest_icon_selected"
            style "page_button"
            action SetVariable("journalPage", "Quest")

        vbox:
            xfill True
            xalign 0.25 yalign 0.4
            text _("Quests") style "quest_title_text" size 45 bold True xalign 0.35 yalign 0.1
            hbox:
                viewport:
                    xpos 0.7 ypos 0.1
                    xminimum 200
                    xmaximum 580
                    ymaximum 700
                    child_size (None, 1000)
                    xfill True
                    draggable True
                    mousewheel True
                    arrowkeys True
                    scrollbars "vertical"
                    has vbox
                    spacing 15
                    text quest_line_breaker style "quest_line_breaker_text"
                    text _("Active Quests:") style "quest_title_text"
                    text quest_line_breaker style "quest_line_breaker_text"
                    for i in activequests:

                        textbutton " -   [i.title!t]" action SetVariable("selected_quest", i) text_hover_color "#AAAAAA" text_color "#333333" text_size 21 style "pling_button"
                    text quest_line_breaker style "quest_line_breaker_text"
                    text _("Completed Quests:") style "quest_title_text"
                    text quest_line_breaker style "quest_line_breaker_text"
                    for i in completedquests:
                        textbutton " -   [i.title!t]" action SetVariable("selected_quest", i) text_hover_color "#AAAAAA" text_color "#333333" text_size 21 style "pling_button"

        if selected_quest != None:
            $ quest_progress = "{p}"
            for checkpoint in selected_quest.progress:
                $ quest_progress += " - "
                if checkpoint.status == False:
                    $ quest_progress += checkpoint.head
                else:
                    $ quest_progress += "{s}" + checkpoint.head + "{/s}"
                $ quest_progress += "{p}{p}"

            vbox:
                xpos 0.62 ypos 0.18
                xmaximum 450
                spacing 15

                text selected_quest.title style "quest_title_text" size 45 italic True
                text "[selected_quest.description!t]" style "quest_content_text" size 25
                text "{p}[quest_line_breaker][quest_line_breaker]" style "quest_line_breaker_text"
                text _(" Progress:") style "quest_title_text" size 35
                text "[quest_progress!t]" style "quest_content_text" size 25
                text "[quest_line_breaker][quest_line_breaker]{p}" style "quest_line_breaker_text"
                text _("Location: [selected_quest.location!t]") style "quest_content_text"
                text _("Quest Giver: [selected_quest.questgiver!t]") style "quest_content_text"
                if hasattr(selected_quest, "start_date") and selected_quest.start_date != 0:
                    text _("Start Date: Day [selected_quest.start_date]") style "quest_content_text"
                if selected_quest in completedquests and selected_quest.completed_date != 999:
                    text _("Completion Date: Day [selected_quest.completed_date]") style "quest_content_text"


    else:

        imagebutton:
            xalign 0.2
            yalign 0.015
            idle "quest_icon"
            style "page_button"
            action SetVariable("journalPage", "Quest")

    if journalPage == "Task":

        imagebutton:
            xalign 0.27
            yalign -0.005
            idle "sidequest_icon_selected"
            style "page_button"
            action SetVariable("journalPage", "Task")


        vbox:
            xfill True
            xalign 0.25 yalign 0.4
            text _("Tasks") style "quest_title_text" size 45 bold True xalign 0.35 yalign 0.1
            hbox:
                viewport:
                    xpos 0.7 ypos 0.1
                    xminimum 200
                    xmaximum 580
                    ymaximum 700
                    child_size (None, 1000)
                    xfill True
                    draggable True
                    mousewheel True
                    arrowkeys True
                    scrollbars "vertical"
                    has vbox
                    spacing 15
                    text quest_line_breaker style "quest_line_breaker_text"
                    text _("Active Tasks:") style "quest_title_text"
                    text quest_line_breaker style "quest_line_breaker_text"
                    for i in activetasks:
                        textbutton " -   [i.title!t]" action SetVariable("selected_task", i) style "pling_button" text_hover_color "#AAAAAA" text_color "#333333" text_size 21
                    text quest_line_breaker style "quest_line_breaker_text"
                    text _("Completed Tasks:") style "quest_title_text"
                    text quest_line_breaker style "quest_line_breaker_text"
                    for i in completedtasks:
                        if i.completed_date + i.interval >= timenow.day:
                            textbutton " -   [i.title!t]" action SetVariable("selected_task", i) style "pling_button" text_hover_color "#AAAAAA" text_color "#333333" text_size 21
                        else:
                            textbutton " ->  [i.title!t]" action SetVariable("selected_task", i) style "pling_button" text_hover_color "#AAAAAA" text_color "#333333" text_size 21

        if selected_task != None:
            $ quest_progress = ""
            for checkpoint in selected_task.progress:
                $ quest_progress += "{p}{p} - "
                if checkpoint.status == False:
                    $ quest_progress += checkpoint.head
                else:
                    $ quest_progress += "{s}" + checkpoint.head + "{/s}"

            $ quest_description = __(selected_task.description)
            $ quest_description += __("{size=20}{p}{p} ==================== {p}{p}{/size=20} {size=32}Progress{/size=32}:")
            $ quest_description += quest_progress + "{size=20}{p}{p}{/size=20}"
            vbox:
                xpos 0.62 ypos 0.18
                xmaximum 450
                spacing 15

                text selected_task.title style "quest_title_text" size 45 italic True
                text "[selected_task.description!t]" style "quest_content_text" size 25
                text "{p}[quest_line_breaker][quest_line_breaker]{p}" style "quest_line_breaker_text"
                text _(" Progress:") style "quest_title_text" size 35
                text "[quest_progress!t]" style "quest_content_text" size 25
                text "{p}[quest_line_breaker][quest_line_breaker]{p}" style "quest_line_breaker_text"
                text _("Location: [selected_task.location!t]") style "quest_content_text"
                text _("Task Giver: [selected_task.questgiver!t]") style "quest_content_text"
                text _("Reward: [selected_task.reward!t]") style "quest_content_text"
                text _("Completed: [selected_task.completedtimes]") style "quest_content_text"

    else:

        imagebutton:
            xalign 0.27
            yalign -0.005
            style "page_button"
            idle "sidequest_icon"
            action SetVariable("journalPage", "Task")

    if quest24.status == True:
        if journalPage == "Trinket":

            imagebutton:
                xalign 0.75
                yalign -0.015
                style "page_button"
                idle "trinket_icon_selected"
                action SetVariable("journalPage", "Trinket"), SetVariable("selected_trinket", None)

            vbox:
                xfill True
                xalign 0.25 yalign 0.4
                text _("Trinkets") style "quest_title_text" size 45 bold True xalign 0.35 yalign 0.1
                hbox:
                    viewport:
                        xpos 0.7 ypos 0.1
                        xminimum 200
                        xmaximum 580
                        ymaximum 700
                        child_size (None, 1000)
                        xfill True
                        draggable True
                        mousewheel True
                        arrowkeys True
                        scrollbars "vertical"
                        has vbox
                        spacing 15
                        text _("Discovered Trinkets:") style "quest_title_text"
                        for i in discoveredtrinket:

                            if i in tinventory:

                                textbutton " -   [i.name!t]" action SetVariable("selected_trinket", i) text_hover_color "#AAAAAA" style "pling_button" text_color "#333333" text_size 21

                            else:
                                textbutton " >   [i.name!t]" action SetVariable("selected_trinket", i) text_hover_color "#AAAAAA" style "pling_button" text_color "#333333" text_size 21


                    if selected_trinket != None:

                        vbox:
                            xpos 1.3 ypos 0.0
                            xmaximum 450
                            spacing 24

                            text selected_trinket.name style "quest_title_text"
                            text _("Description: [selected_trinket.description!t]") style "quest_content_text" size 30
                            text quest_line_breaker style "quest_content_text"
                            text _("{i}[selected_trinket.hint!t]{/i}") style "quest_content_text"

                        frame:
                            xpos 6.0 ypos -0.05
                            xmaximum 450


                            imagebutton:
                                style "click_button"
                                idle selected_trinket.img.lower()
                                action NullAction()


        else:

            imagebutton:
                xalign 0.75
                yalign -0.015
                style "page_button"
                idle "trinket_icon"
                action SetVariable("journalPage", "Trinket")

    if journalPage == "Skill":

        imagebutton:
            xalign 0.82
            yalign -0.007
            style "page_button"
            idle "skill_icon_selected"
            action SetVariable("journalPage", "Skill")

        vbox:
            xfill True
            xalign 0.25 yalign 0.4
            text _("Skills") style "quest_title_text" size 45 bold True xalign 0.75 yalign 0.1
            hbox:
                viewport:
                    xpos 1.2 ypos 0.1
                    xminimum 500
                    xmaximum 980
                    ymaximum 700
                    child_size (None, 1000)
                    xfill True
                    draggable True
                    mousewheel True
                    arrowkeys True
                    scrollbars "vertical"
                    has vbox
                    spacing 15
                    text _("Learned Skills:") style "quest_title_text"
                    for i in learnedabilities:

                        textbutton " -   [i.name!t]" action [SetVariable("selected_skill", i), Function(addSkill, i)] style "pling_button" text_hover_color "#AAAAAA" text_color "#333333" text_size 21

                    text _("Equipped Skills:") style "quest_title_text"

                    if abilities[0] != None:
                        $ chosen_skill = abilities[0]
                        textbutton " -   < [abilities[0].name!t] >" action [SetVariable("selected_skill", abilities[0]), Function(removeSkill, 0)] style "pling_button" text_hover_color "#AAAAAA" text_color "#333333" text_size 21
                    else:
                        textbutton " -   < > " action NullAction() text_hover_color "#AAAAAA" text_color "#333333" text_size 21
                    if abilities[1] != None:
                        $ chosen_skill = abilities[1]
                        textbutton " -   < [abilities[1].name!t] >" action [SetVariable("selected_skill", abilities[1]), Function(removeSkill, 1)] style "pling_button" text_hover_color "#AAAAAA" text_color "#333333" text_size 21
                    else:
                        textbutton " -   < > " action NullAction() text_hover_color "#AAAAAA" text_color "#333333" text_size 21
                    if len(abilities) > 2 and abilities[2] != None:
                        $ chosen_skill = abilities[2]
                        textbutton " -   < [abilities[2].name!t] >" action [SetVariable("selected_skill", abilities[2]), Function(removeSkill, 2)] style "pling_button" text_hover_color "#AAAAAA" text_color "#333333" text_size 21
                    else:
                        textbutton " -   < > " action NullAction() style "pling_button" text_hover_color "#AAAAAA" text_color "#333333" text_size 21

                if selected_skill != None:

                    vbox:
                        xpos -0.95 ypos 0.05
                        xmaximum 450
                        spacing 20

                        text selected_skill.name style "quest_title_text"
                        text quest_line_breaker style "quest_content_text"
                        text selected_skill.description style "quest_content_text"

                        imagebutton:
                            style "click_button"
                            idle selected_skill.img.lower()
                            action NullAction()


    else:

        imagebutton:
            xalign 0.82
            yalign -0.007
            idle "skill_icon"
            style "page_button"
            action SetVariable("journalPage", "Skill")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
