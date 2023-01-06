import os

from libqtile.lazy import lazy
from libqtile.config import Key, KeyChord

from modules.groups import groups
from modules.consts import TERMINAL


mod = "mod4"
shft = "shift"
ctrl = "control"
alt = "mod1"


def create_gotogroup_keys():
    gotogroupkeys = []
    for g in groups:
        gotogroupkeys.append(Key(
            [],
            g.name,
            lazy.group[g.name].toscreen(),
            desc="Go to group " + g.name,
        ))
    return gotogroupkeys


def create_sendwindowtogroup_keys():
    sendtogroupkeys = []
    for g in groups:
        sendtogroupkeys.append(Key(
            [],
            g.name,
            lazy.window.togroup(g.name, switch_group=True),
            desc="Send window to group " + g.name,
        ))
    return sendtogroupkeys


def create_sendscreentogroup_keys(screen):
    keys = []
    for g in groups:
        keys.append(Key(
            [],
            g.name,
            send_group_to_screen(
                int(g.name) - 1 if int(g.name) > 0 else 9,
                screen
            ),
            desc="Send group " + g.name + " to screen " + str(screen),
        ))
    return keys


@lazy.function
def focus_next_screen(qtile):
    current_screen = qtile.current_screen.index
    if current_screen == 0:
        qtile.focus_screen(2)
    if current_screen == 2:
        qtile.focus_screen(1)
    if current_screen == 1:
        qtile.focus_screen(0)


@lazy.function
def focus_prev_screen(qtile):
    current_screen = qtile.current_screen.index
    if current_screen == 0:
        qtile.focus_screen(1)
    if current_screen == 1:
        qtile.focus_screen(2)
    if current_screen == 2:
        qtile.focus_screen(0)


@lazy.function
def focus_screen(qtile, index):
    qtile.cmd_to_screen(index)


@lazy.function
def send_group_to_screen(qtile, group, screen):
    qtile.screens[screen].set_group(qtile.groups[group])
    qtile.cmd_to_screen(screen)


@lazy.function
def show_keybinds(qtile):
    binds = []
    for k, v in qtile.keys_map.items():
        binds = binds + key_to_strings(v)
    binds = map(lambda x: x[0].rjust(30, " ") + "     " + x[1], binds)
    qtile.cmd_spawn("echo '" + "\n".join(binds) + "' | rofi -dmenu -i", True)


def key_to_strings(binding, chord_prefix=""):
    sequence = get_sequence_for_key(binding)
    sequence = chord_prefix + "  " + sequence if len(chord_prefix) > 0 \
        else sequence

    if type(binding).__name__ == "Key":
        return [(sequence, binding.desc)]

    if type(binding).__name__ == "KeyChord":
        binds = []
        for b in binding.submappings:
            binds = binds + key_to_strings(b, sequence)
        return binds


def get_sequence_for_key(key):
    return " + ".join(key.modifiers + [key.key])


keys = [
    Key([mod], "n", lazy.spawn("rofi -show combi"), desc="Spawn rofi menu"),

    Key([mod], "h", lazy.layout.left(), desc="Move focus to left window"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right window"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down window"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up window"),
    Key([mod, shft], "h", lazy.layout.shuffle_left(), desc="Move window left"),
    Key([mod, shft], "l", lazy.layout.shuffle_right(), desc="Move window right"),
    Key([mod, shft], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, shft], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, ctrl], "h", lazy.layout.grow(), desc="Grow window"),
    Key([mod, ctrl], "l", lazy.layout.shrink(), desc="Shrink window"),
    Key([mod, ctrl], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(TERMINAL), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"],
        "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 3%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 3%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
]

keys = keys + [
    Key([mod], "F12", show_keybinds(), desc="Show keybindings"),
    Key([mod], "m", lazy.spawn("rofi -show combi"), desc="spawn rofi"),
    Key([mod], "b", lazy.spawn("firefox"), desc="Open Firefox"),
    Key(
        [ctrl, alt],
        "Delete",
        lazy.spawn(os.path.expanduser('~/.config/rofi/powermenu.sh')),
        desc="Power menu",
    ),
    Key([mod], "BackSpace", lazy.window.kill(), desc="Close window"),

    # Key([mod], "h", my_next_screen(), desc="Focus next screen"),
    # Key([mod], "l", my_prev_screen(), desc="Focus previous screen"),

    KeyChord([mod], "semicolon", [
        Key([], "j", focus_screen(2), desc="Focus screen left"),
        Key([], "k", focus_screen(0), desc="Focus screen middle"),
        Key([], "l", focus_screen(1), desc="Focus screen right"),
    ]),
    KeyChord([mod], "comma", create_gotogroup_keys()),
    KeyChord([mod], "period", create_sendwindowtogroup_keys()),
    KeyChord(
        [mod],
        "apostrophe",
        [
            KeyChord([], "j", create_sendscreentogroup_keys(2)),
            KeyChord([], "k", create_sendscreentogroup_keys(0)),
            KeyChord([], "l", create_sendscreentogroup_keys(1)),
        ],
    ),
]
