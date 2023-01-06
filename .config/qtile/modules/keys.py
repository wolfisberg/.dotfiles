import os

from libqtile.lazy import lazy
from libqtile.config import Key, KeyChord

from modules.groups import groups
from modules.consts import \
    TERMINAL, SCREEN_LEFT, SCREEN_MIDDLE, SCREEN_RIGHT


MOD = "mod4"
SHFT = "shift"
CTRL = "control"
ALT = "mod1"


def create_gotogroup_keys():
    gotogroupkeys = []
    for g in groups:
        gotogroupkeys.append(Key(
            [],
            g.name,
            lazy.group[g.name].toscreen(),
            desc="go to group " + g.name,
        ))
    return gotogroupkeys


def create_sendwindowtogroup_keys():
    sendtogroupkeys = []
    for g in groups:
        sendtogroupkeys.append(Key(
            [],
            g.name,
            lazy.window.togroup(g.name, switch_group=False),
            desc="send window to group " + g.name,
        ))
    return sendtogroupkeys


def create_sendgrouptoscreen_keys(screen):
    keys = []
    for g in groups:
        keys.append(Key(
            [],
            g.name,
            send_group_to_screen(
                int(g.name) - 1 if int(g.name) > 0 else 9,
                screen
            ),
            desc="send group " + g.name + " to screen " + str(screen),
        ))
    return keys


@lazy.function
def focus_next_screen(qtile):
    current_screen = qtile.current_screen.index
    if current_screen == SCREEN_MIDDLE:
        qtile.focus_screen(SCREEN_LEFT)
    if current_screen == SCREEN_LEFT:
        qtile.focus_screen(SCREEN_RIGHT)
    if current_screen == SCREEN_RIGHT:
        qtile.focus_screen(SCREEN_MIDDLE)


@lazy.function
def focus_prev_screen(qtile):
    current_screen = qtile.current_screen.index
    if current_screen == SCREEN_MIDDLE:
        qtile.focus_screen(SCREEN_RIGHT)
    if current_screen == SCREEN_RIGHT:
        qtile.focus_screen(SCREEN_LEFT)
    if current_screen == SCREEN_LEFT:
        qtile.focus_screen(SCREEN_MIDDLE)


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


def prefix_key_descs(keys, prefix):
    for k in keys:
        if type(k).__name__ == "Key":
            k.desc = ("[" + prefix + "] ").ljust(12, " ") + k.desc
        if type(k).__name__ == "KeyChord":
            prefix_key_descs(k.submappings, prefix)
    return keys


layout_keys = [
    Key([MOD], "backslash", lazy.next_layout(), desc="toggle between layouts"),
    Key([MOD, SHFT], "f", lazy.window.toggle_floating(), desc="toggle window floating"),

    Key([MOD], "h", lazy.layout.left(), desc="move focus to left window"),
    Key([MOD], "l", lazy.layout.right(), desc="move focus to right window"),
    Key([MOD], "j", lazy.layout.down(), desc="move focus down window"),
    Key([MOD], "k", lazy.layout.up(), desc="move focus up window"),
    Key([MOD, SHFT], "h", lazy.layout.shuffle_left(), desc="move window left"),
    Key([MOD, SHFT], "l", lazy.layout.shuffle_right(), desc="move window right"),
    Key([MOD, SHFT], "j", lazy.layout.shuffle_down(), desc="move window down"),
    Key([MOD, SHFT], "k", lazy.layout.shuffle_up(), desc="move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([MOD, CTRL], "h", lazy.layout.grow(), desc="grow window"),
    Key([MOD, CTRL], "l", lazy.layout.shrink(), desc="shrink window"),
    Key([MOD, CTRL], "n", lazy.layout.normalize(), desc="reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([MOD, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([MOD, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([MOD, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([MOD, "shift"], "space", lazy.layout.flip()),

    # Key([mod], "h", focus_next_screen(), desc="Focus next screen"),
    # Key([mod], "l", focus_prev_screen(), desc="Focus previous screen"),

    KeyChord([MOD], "semicolon", [
        Key([], "j", focus_screen(SCREEN_LEFT), desc="focus screen left"),
        Key([], "k", focus_screen(SCREEN_MIDDLE), desc="focus screen middle"),
        Key([], "l", focus_screen(SCREEN_RIGHT), desc="focus screen right"),
    ]),
    KeyChord([MOD], "comma", create_gotogroup_keys()),
    KeyChord([MOD], "period", create_sendwindowtogroup_keys()),
    KeyChord(
        [MOD],
        "apostrophe",
        [
            KeyChord([], "j", create_sendgrouptoscreen_keys(SCREEN_LEFT)),
            KeyChord([], "k", create_sendgrouptoscreen_keys(SCREEN_MIDDLE)),
            KeyChord([], "l", create_sendgrouptoscreen_keys(SCREEN_RIGHT)),
        ],
    ),
]

launch_keys = [
    KeyChord([MOD], "m", [
        Key([], "e", lazy.spawn("thunar"), desc="file explorer (thunar)"),
        Key([], "b", lazy.spawn("firefox"), desc="browser (firefox)"),
        Key([], "s", lazy.spawn("spotify"), desc="spotify"),
        Key([], "c", lazy.spawn("code"), desc="vscode"),
        Key([], "t", lazy.spawn(TERMINAL), desc="terminal (alacritty)"),
        Key([], "k", lazy.spawn("keepassxc"), desc="passwords (keepassxc)"),
    ]),
    Key([MOD], "Return", lazy.spawn(TERMINAL), desc="terminal (alacritty"),
    Key([MOD], "n", lazy.spawn("rofi -show combi"), desc="rofi menu"),
]

os_keys = [
    Key([MOD], "F12", show_keybinds(), desc="show keybindings"),
    Key([MOD], "BackSpace", lazy.window.kill(), desc="close window"),
    Key(
        [CTRL, ALT],
        "Delete",
        lazy.spawn(os.path.expanduser('~/.config/rofi/powermenu.sh')),
        desc="power menu",
    ),
    Key([MOD, "control"], "r", lazy.restart(), desc="restart Qtile"),
    # Key([MOD, "control"], "q", lazy.shutdown(), desc="shutdown Qtile"),
]

media_keys = [
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("amixer -D pulse sset Master 3%+"),
        desc="raise volume",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("amixer -D pulse sset Master 3%-"),
        desc="lower volume"
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("amixer -D pulse sset Master toggle"),
        desc="toggle mute"
    ),
    Key(
        [],
        "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"),
        desc="toggle playback",
    ),
    Key(
        [],
        "XF86AudioPrev",
        lazy.spawn("playerctl previous"),
        desc="play previous",
    ),
    Key(
        [],
        "XF86AudioNext",
        lazy.spawn("playerctl next"),
        desc="play next",
    ),
]


keys = prefix_key_descs(layout_keys, "TILING") \
        + prefix_key_descs(launch_keys, "RUN") \
        + prefix_key_descs(os_keys, "OS") \
        + prefix_key_descs(media_keys, "MEDIA")
