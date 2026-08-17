translate schinese_rewrite python:
    # Keep the rewrite language's GUI typography in sync with the existing
    # Simplified Chinese package. In particular, styles.rpy references this
    # headline font for screen titles and buttons.
    gui.language = "japanese-normal"

    gui.system_font = "Source_Han_Sans_CN-Regular.otf"

    gui.text_font = gui.interface_text_font = gui.button_text_font = gui.choice_button_text_font = FontGroup().add("AR_PL_KaitiM_Big5.ttf", 0x5187, 0x5187).add("AR_PL_KaitiM_Big5.ttf", 0x5463, 0x5463).add("AR_PL_KaitiM_Big5.ttf", 0x5c44, 0x5c44).add("AR_PL_KaitiM_Big5.ttf", 0x5c4c, 0x5c4c).add("AR_PL_KaitiM_Big5.ttf", 0x808f, 0x808f).add("AR_PL_KaitiM_Big5.ttf", 0x6294, 0x6294).add("AR_PL_KaitiM_Big5.TTF", 0x77ad, 0x77ad).add("AR_PL_KaitiM_Big5.TTF", 0x636f, 0x636f).add("AR_PL_KaitiM_Big5.TTF", 0x7ab8, 0x7ab8).add("AR_PL_KaitiM_Big5.TTF", 0x7aa3, 0x7aa3).add("AR_PL_KaitiM_GB.TTF", 0x2014, 0x201f).add("AR_PL_KaitiM_GB.TTF", 0x2E80, 0xffff).add("garamond.ttf", 0x0000, 0xffff)

    gui.name_text_font = "LXGWWenKaiLite-Bold.ttf"

    gui.text_size = 32

    gui.name_text_size = 48

    gui.headline_text_font = FontGroup().add("Source_Han_Serif_CN-Bold.otf", 0x2E80, 0xffff).add("kingthing.ttf", 0x0000, 0xffff)

    @gui.variant
    def small():
        gui.text_size = 48
        gui.name_text_size = 42
