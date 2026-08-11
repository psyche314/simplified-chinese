define config.name = _("Outland Wanderer")
define gui.show_name = True
define config.version = "0.0.29"

define gui.about = _p("""

Outland Wanderer is a Visual Novel RPG created by f1shsticker.

Player plays an outsider stumbling upon the continent of Mokken. In his attempt to travel back to his own Tribe, he bonds and form different relationship with the locals, tackles on unknown forces, and discover shocking yet compelling secret among them. But be ware, your decision will change their lives, forever.

This is a prototype, aims for laying foundations and systems, storytelling and other elements are not refined yet. A lot of bugs might also exists so there is a very high possibility your save would not be able to transfer to future build.

==================================================================

{a=https://discord.gg/QnbJMGhZhV}Official Discord Server{/a}

Credit:

Code/Art/Script: f1shsticker {a=https://twitter.com/OutlandWanderer}Twitter{/a}

Code: 逆戟鲸COPtimer {a=https://twitter.com/COPtimer_1974}Twitter{/a}

Script: Nyarlothotep {a=https://twitter.com/LoveCountry45}Twitter{/a} {p}

LonelyTree {a=https://discordapp.com/users/273928084388839425}Discord{/a}

Magnolia

Music: Will o Wisp {a=https://soundcloud.com/willowispproductions}Twitter{/a}

Pinewood Jerry {a=https://twitter.com/Pinewood_Jerry}Twitter{/a}

French Translation: Sannom(Paul) {a=https://twitter.com/SannomTigris}Twitter{/a}

Portuguese Translation: Fábio.T {a=https://twitter.com/Fabio120938}Twitter{/a}

Simplified Chinese Translation: 逆戟鲸COPtimer {a=https://twitter.com/COPtimer_1974}Twitter{/a}, Dcl5, Robotic-Panda

Font: Adobe Garamond Pro

""")

define build.name = "Outland-Wanderer"

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.main_menu_music = "audio/Forest_Ambience.mp3"

define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None

define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

default preferences.text_cps = 40
default preferences.afm_time = 15

define config.save_directory = "Test1-1648890977"
define config.window_icon = "gui/window_icon.png"

init python:
    import os

    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("sounds", "all")
    build.archive("fonts", "all")

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**LICENSE', None)
    build.classify('**.rpy', None)
    build.classify('**.md', None)

    build.classify('game/**.rpyc', 'scripts')
    build.classify('game/**.png', 'images')
    build.classify('game/**.webp', 'images')
    build.classify('game/**.avif', 'images')
    build.classify('game/**.jpg', 'images')
    build.classify('game/**.ogg', 'sounds')
    build.classify('game/**.mp3', 'sounds')
    build.classify('game/**.wav', 'sounds')
    build.classify('game/**.ttf', 'fonts')
    build.classify('game/**.otf', 'fonts')

    def _gitignore_patterns(filename):
        """Read Git-style ignore patterns and map them to build globs."""
        try:
            with open(filename, "rb") as ignore_file:
                lines = ignore_file.read().splitlines()
        except (IOError, OSError):
            return []

        result = []
        for line in lines:
            line = line.strip()
            if not line:
                continue

            literal = line.startswith("\\#") or line.startswith("\\!")
            include = False
            if literal:
                line = line[1:]
            elif line.startswith("#"):
                continue
            elif line.startswith("!"):
                include = True
                line = line[1:]

            line = line.replace("\\ ", " ")
            directory = line.endswith("/")
            anchored = line.startswith("/")
            line = line.strip("/")
            if not line:
                continue

            if not anchored and "/" not in line and not line.startswith("**"):
                line = "**" + line

            if directory:
                line += "/"

            result.append((line, "all" if include else None))

        # Git uses the last matching pattern in one ignore file, while
        # Ren'Py uses the first matching build.classify rule.
        return result[::-1]

    def _classify_git_ignored_files():
        """Apply repository-local ignore rules to Ren'Py build output."""
        project_root = getattr(config, "basedir", None) or os.getcwd()
        project_root = os.path.abspath(project_root)
        ignore_files = [
            os.path.join(project_root, ".gitignore"),
            os.path.join(project_root, ".git", "info", "exclude"),
        ]

        # This runs after the required script and asset classifiers. Ren'Py's
        # first matching build rule therefore still packages generated .rpyc
        # files even though Git ignores those local bytecode files.
        for ignore_file in ignore_files:
            for pattern, file_list in _gitignore_patterns(ignore_file):
                build.classify(pattern, file_list)

    _classify_git_ignored_files()

    build.documentation('*.html')
    build.documentation('*.txt')

define build.itch_project = "f1shsticker/outland-wanderer"
define config.check_conflicting_properties = True

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
