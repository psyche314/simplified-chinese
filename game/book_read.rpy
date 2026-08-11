default botanical_journal01 = Page("{b}The Somni-Etern{/b} is a dangerous mushroom for the untrained forager. Its soporific effects are strong enough that a full bite will shut down your nervous system.\nThere have been few cases of survivors - all of them having consumed smaller amounts previously. I assume they built a resistance to it; more on that later.\nDespite the deadly nature of the somni-etern, it is incredibly useful to the medicinal practitioner.\nMixing only a bit in- - —-----d soup or drink, and feeding the result to a patient, will ease their pain significantly. It also tastes quite good, from —- I — —-","Caution in determining dosage is, of course, critical. Quite p--ibly more important, however, is that patients can and will grow resistant, and/or addicted.\nI unfortunately l—--d t- har- w-. M- -on of-e- suf-re- fr- night terrors. To sol-e this, I -xe- som—--rn into h- baby formula ev-y nig-t.\nSome-ow, he fa—d to gr-w addicted. He is, h-ev-r, co-ple-ly im-ne to the mushrooms.\n-- -s six n-w, fi- yea- ol-e- t— he -as then. Perhaps it was my occas-nal -xp-iments on the s-je- that led t- h- im-un-y being perma-nt, or at le— not reduced at all in five years.\n-- - —-- mentioning that - — been t—- months sin-e I — — —-.\nI do not want him to watch me die.", 3)

default botanical_journal02 = Page("{b}Echinacea{/b} is another plant I often use.\nI suppose that goes without saying, as this is in the 'common medical use' section of the book, but all the same.\n\n           I sometimes regret the fact that I cannot erase anything I write in this journal.\nRegardless, while its effects aren’t as strong as many of the other plants or mushrooms in this book, it is useful for nearly any infection.\nThe vast majority of its body, from flower to roots, are useful. Tinctures, potions, teas... anything else you could think of, it is useful for.\nThose same products are widely applicable as well. Anything from infection, to inflammation, it covers.", "The only issue, of course, is that it is too weak to be a true cure; I heavily recommend using it in conjunction with other plants in this journal for anything worse than a headache.\nWhen there is no other plant that can help, but the issue is one that requires something not in this book, as with my own sickness, continue my work and find one.\nThis book is not nearly comprehensive. It is only a collection of notes from one man’s life.\nUntil you find one, try and make the patient comfortable, and give them Echinacea.\nThe dying deserve comfort, and echinacea helps make that final stretch a bit more humane.\nI speak from experience. Nobody wants to see somebody in that much pain, not the patient, nor you, nor their loved ones.", 4)

default kings_pawn_account_journal = Book(_("{i}Seb's Accounts{/i}"), "spritebinder_journal", "Kings_Pawn_Account_Journal")


style book_style:
    color "#29221a"
    font "Eadui.ttf"
    line_spacing 15


screen book_read(book):

    add book.bg

    fixed:
        xalign 0.23
        yalign 0.17
        xmaximum 500
        ymaximum 200
        text "[book.content[book_page].bodyL!t]" style "book_style"

    fixed:
        xalign 0.7
        yalign 0.17
        xmaximum 500
        ymaximum 200
        text "[book.content[book_page].bodyR!t]" style "book_style"

    if book_page > 0:
        imagebutton:
            idle "dungeon_left"
            hover "dungeon_left_hover"
            xalign 0.1
            yalign 0.5
            style "page_button"
            action SetVariable("book_page", book_page - 1)

    if book_page < len(book.content) - 1:
        imagebutton:
            idle "dungeon_right"
            hover "dungeon_right_hover"
            xalign 0.9
            yalign 0.5
            style "page_button"
            action SetVariable("book_page", book_page + 1)

    frame:
        xalign 0.85
        yalign 0.95
        textbutton _("{color=#000}Close{/color}"):
            style "page_button"
            action Return()


label Book_Botanical_Journal:
    $ book_page = 0
    call screen book_read(botanical_journal)

    return

label Book_Battle_Of_Lusterfield:
    $ book_page = 0
    call screen book_read(battle_of_lusterfield)

    return

label Book_Old_Mayors_Journal:
    $ book_page = 0
    call screen book_read(old_mayors_journal)

    return

label Magic_Show_Pamphlet:
    call screen magic_show_pamphlet

    return

label Rebalancing_Elixir:
    $ refunded_points = pc.reset_levelup_points()
    if refunded_points > 0:
        $ removeItem("Rebalancing Elixir", inventory, 1)
        $ renpy.notify(_("Recovered ") + str(refunded_points) + _(" level points."))
    else:
        $ renpy.notify(_("No level points to reset."))

    return

screen magic_show_pamphlet():

    add "magic_show_pamphlet"
    text _("{size=80}R{/size}ibba's Ribald\nMagic Show") font "moria.ttf" color "#3d1e4cb8" size 50 xanchor 0.5 xpos 0.53 yalign 0.1 textalign 0.5
    text _("Forest Skewers\nSweet Pie\nHoney Mead") font "moria.ttf" color "#3d1e4cb8" xalign 0.40 yalign 0.71 size 22 textalign 0.0
    text _("30-Gold\nAdult Only!") font "moria.ttf" color "#3d1e4cb8" xalign 0.67 yalign 0.73 size 22 textalign 1.0
    text _("Come one, come all!\n See the amazing feats of magic\n performed by the great Ribba!\n\n Shows every Weekday night\n at the Travelling Carousal!\n See you on the great plains!") font "moria.ttf" color "#3d1e4cb8" xalign 0.53 yalign 0.88 size 17 textalign 0.5
    frame:
        xalign 0.85
        yalign 0.95
        textbutton _("{color=#000}Close{/color}"):
            style "page_button"
            action Return()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
