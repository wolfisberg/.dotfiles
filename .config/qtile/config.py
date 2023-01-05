import os
from modules.keys import keys, mod
from modules.groups import groups
from modules.layouts import layouts, floating_layout
from modules.mouse import mouse
from modules.hooks import *
from modules.screens import screens
from libqtile.config import Key, KeyChord, Group, Match, Screen
from libqtile.lazy import lazy
from libqtile.log_utils import logger


dgroups_key_binder = None
dgroups_app_rules = []
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "Qtile"

sendtogroupkeys = dict(font="Cascadia Code", fontsize=13, padding=3)

mmod = "mod4"
shft = "shift"
ctrl = "control"
alt = "mod1"

groups = [
    Group(
        name="1",
        matches=[Match(wm_class=['firefox'])],
        screen_affinity=1,
    ),
    Group(
        name="2",
        matches=[Match(wm_class=['code-oss'])],
    ),
    Group(
        name="3",
        matches=[Match(wm_class=['keepassxc'])],
    ),
    Group(
        name="4",
        matches=[],
    ),
    Group(
        name="5",
        matches=[],
    ),
    Group(
        name="6",
        matches=[],
    ),
    Group(
        name="7",
        matches=[],
    ),
    Group(
        name="8",
        matches=[],
    ),
    Group(
        name="9",
        matches=[],
    ),
    Group(
        name="0",
        matches=[],
    )
]
gotogroupkeys = []
sendtogroupkeys = []

for i in groups:
    gotogroupkeys.append(Key(
        [],
        i.name,
        lazy.group[i.name].toscreen(),
        desc="Go to group " + i.name,
    ))
    sendtogroupkeys.append(Key(
        [],
        i.name,
        lazy.window.togroup(i.name),
        lazy.group[i.name].toscreen(),
        desc="Send window to group " + i.name,
    ))


def create_send_to_group_keys(screen):
    keys = []
    for g in groups:
        keys.append(Key(
            [],
            g.name,
            my_send_group_to_screen(
                int(g.name) - 1 if int(g.name) > 0 else 9,
                screen
            ),
            desc="Send group " + g.name + " to screen " + str(screen),
        ))
    return keys


@lazy.function
def my_next_screen(qtile):
    current_screen = qtile.current_screen.index
    if current_screen == 0:
        qtile.focus_screen(2)
    if current_screen == 2:
        qtile.focus_screen(1)
    if current_screen == 1:
        qtile.focus_screen(0)


@lazy.function
def my_prev_screen(qtile):
    current_screen = qtile.current_screen.index
    if current_screen == 0:
        qtile.focus_screen(1)
    if current_screen == 1:
        qtile.focus_screen(2)
    if current_screen == 2:
        qtile.focus_screen(0)


@lazy.function
def my_focus_screen(qtile, index):
    qtile.cmd_to_screen(index)


@lazy.function
def my_send_group_to_screen(qtile, group, screen):
    qtile.screens[screen].set_group(qtile.groups[group])
    qtile.cmd_to_screen(screen)


@lazy.function
def my_show_keybinds(qtile):
    binds = []
    for k, v in qtile.keys_map.items():
        binds = binds + key_to_strings(v)
    binds = map(lambda x: x[0].rjust(30, " ") + "     " + x[1], binds)
    qtile.cmd_spawn("echo '" + "\n".join(binds) + "' | rofi -dmenu -i", True)


def key_to_strings(binding, chord_prefix=""):
    sequence = get_sequence_for_key(binding)
    sequence = chord_prefix + "  " + sequence if len(chord_prefix) > 0 else sequence

    if type(binding).__name__ == "Key":
        return [(sequence, binding.desc)]

    if type(binding).__name__ == "KeyChord":
        binds = []
        for b in binding.submappings:
            binds = binds + key_to_strings(b, sequence)
        return binds


def get_sequence_for_key(key):
    return " + ".join(key.modifiers + [key.key])


# TODO: dev code
def print_props(obj):
    logger.warning(vars(obj))


# TODO: dev code
def print_funcs(obj):
    funcs = [
        method_name for method_name in dir(obj) if callable(getattr(obj, method_name))
    ]
    logger.warning(funcs)


keys = keys + [
    Key([mmod], "F12", my_show_keybinds(), desc="Show keybindings"),
    Key([mod], "m", lazy.spawn("rofi -show combi"), desc="spawn rofi"),
    Key([mmod], "b", lazy.spawn("firefox"), desc="Open Firefox"),
    Key(
        [ctrl, alt],
        "Delete",
        lazy.spawn(os.path.expanduser('~/.config/rofi/powermenu.sh')),
        desc="Power menu",
    ),
    Key([mmod], "BackSpace", lazy.window.kill(), desc="Close window"),

    # Key([mmod], "h", my_next_screen(), desc="Focus next screen"),
    # Key([mmod], "l", my_prev_screen(), desc="Focus previous screen"),

    KeyChord([mmod], "semicolon", [
        Key([], "j", my_focus_screen(2), desc="Focus screen left"),
        Key([], "k", my_focus_screen(0), desc="Focus screen middle"),
        Key([], "l", my_focus_screen(1), desc="Focus screen right"),
    ]),
    KeyChord([mmod], "comma", gotogroupkeys),
    KeyChord([mmod], "period", sendtogroupkeys),
    KeyChord(
        [mmod],
        "apostrophe",
        [
            KeyChord([], "j", create_send_to_group_keys(2)),
            KeyChord([], "k", create_send_to_group_keys(0)),
            KeyChord([], "l", create_send_to_group_keys(1)),
        ],
    ),
]
