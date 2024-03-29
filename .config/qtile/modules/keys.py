import os

from libqtile.lazy import lazy
from libqtile.config import Key, KeyChord

from modules.groups import groups as groups_and_scratchpads, \
    GRP_SCRATCHPAD, DD_PASSWORD, DD_TERM, DD_FM, DD_TUI_FM
from modules.consts import \
    TERMINAL, SCREEN_LEFT, SCREEN_MIDDLE, SCREEN_RIGHT


MOD = "mod4"
SHFT = "shift"
CTRL = "control"
ALT = "mod1"

grps = [g for g in groups_and_scratchpads
        if type(g).__name__ != "ScratchPad"]


def create_gotogroup_keys():
    gotogroupkeys = []
    for g in grps:
        gotogroupkeys.append(Key(
            [],
            g.name,
            lazy.group[g.name].toscreen(),
            desc="go to group " + g.name,
        ))
    return gotogroupkeys


def create_sendwindowtogroup_keys():
    sendtogroupkeys = []
    for g in grps:
        sendtogroupkeys.append(Key(
            [],
            g.name,
            lazy.window.togroup(g.name, switch_group=False),
            desc="send window to group " + g.name,
        ))
    return sendtogroupkeys


def create_sendgrouptoscreen_keys(screen):
    keys = []
    for g in grps:
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
        qtile.focus_screen(SCREEN_RIGHT)
    if current_screen == SCREEN_RIGHT:
        qtile.focus_screen(SCREEN_LEFT)
    if current_screen == SCREEN_LEFT:
        qtile.focus_screen(SCREEN_MIDDLE)


@lazy.function
def focus_prev_screen(qtile):
    current_screen = qtile.current_screen.index
    if current_screen == SCREEN_MIDDLE:
        qtile.focus_screen(SCREEN_LEFT)
    if current_screen == SCREEN_LEFT:
        qtile.focus_screen(SCREEN_RIGHT)
    if current_screen == SCREEN_RIGHT:
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

    # WINDOWS
    Key([MOD], "h", lazy.layout.left(), desc="move focus to left window"),
    Key([MOD], "l", lazy.layout.right(), desc="move focus to right window"),
    Key([MOD], "j", lazy.layout.down(), desc="move focus down window"),
    Key([MOD], "k", lazy.layout.up(), desc="move focus up window"),
    Key([MOD, SHFT], "h", lazy.layout.shuffle_left(), desc="move window left"),
    Key([MOD, SHFT], "l", lazy.layout.shuffle_right(), desc="move window right"),
    Key([MOD, SHFT], "j", lazy.layout.shuffle_down(), desc="move window down"),
    Key([MOD, SHFT], "k", lazy.layout.shuffle_up(), desc="move window up"),
    Key(
        [MOD, CTRL],
        "backslash",
        lazy.layout.reset(),
        lazy.layout.normalize(),
        desc="reset all window sizes",
    ),
    Key([MOD], "space", lazy.layout.maximize(), desc="maximze window"),
    Key([MOD, CTRL], "h", lazy.layout.grow(), desc="grow window"),
    Key([MOD, CTRL], "l", lazy.layout.shrink(), desc="shrink window"),

    # SCREENS
    Key([MOD], "bracketleft", focus_prev_screen(), desc="focus previous screen"),
    Key([MOD], "bracketright", focus_next_screen(), desc="focus next screen"),
    KeyChord([MOD], "semicolon", [
        Key([], "j", focus_screen(SCREEN_LEFT), desc="focus screen left"),
        Key([], "k", focus_screen(SCREEN_MIDDLE), desc="focus screen middle"),
        Key([], "l", focus_screen(SCREEN_RIGHT), desc="focus screen right"),
    ]),
    KeyChord(
        [MOD],
        "apostrophe",
        [
            KeyChord([], "j", create_sendgrouptoscreen_keys(SCREEN_LEFT)),
            KeyChord([], "k", create_sendgrouptoscreen_keys(SCREEN_MIDDLE)),
            KeyChord([], "l", create_sendgrouptoscreen_keys(SCREEN_RIGHT)),
        ],
    ),

    # GROUPS
    KeyChord([MOD], "comma", create_gotogroup_keys()),
    KeyChord([MOD], "period", create_sendwindowtogroup_keys()),
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
    Key(
        [MOD],
        "n",
        lazy.spawn("rofi -show combi -filter '-" + GRP_SCRATCHPAD + " '"),
        desc="rofi menu"
    ),
    Key([MOD], "F12", lazy.group[GRP_SCRATCHPAD].dropdown_toggle(DD_PASSWORD)),
    Key([MOD], "F11", lazy.group[GRP_SCRATCHPAD].dropdown_toggle(DD_FM)),
    Key([MOD], "F10", lazy.group[GRP_SCRATCHPAD].dropdown_toggle(DD_TUI_FM)),
    Key([MOD], "F9", lazy.group[GRP_SCRATCHPAD].dropdown_toggle(DD_TERM)),
]

os_keys = [
    Key([MOD], "F1", show_keybinds(), desc="show keybindings"),
    Key([MOD], "BackSpace", lazy.window.kill(), desc="close window"),
    Key(
        [CTRL, ALT],
        "Delete",
        lazy.spawn(os.path.expanduser('~/.config/rofi/powermenu.sh')),
        desc="power menu",
    ),
    Key([MOD, "control"], "r", lazy.restart(), desc="restart Qtile"),
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
