import os
import subprocess

from libqtile import hook, qtile

from modules.consts import SCREEN_LEFT
from modules.layouts import layouts, LAYOUT_VERTICAL_TILE


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])


@hook.subscribe.setgroup
def set_layout_per_screen():
    for s in qtile.screens:
        current_layout = layouts[s.group.current_layout].name
        set_defaults(s.group)
        if s.index == SCREEN_LEFT:
            if s.group.prev_screen != SCREEN_LEFT:
                s.group.prev_layout = current_layout
            set_layout(s.group, LAYOUT_VERTICAL_TILE.name, False)
        else:
            if s.group.prev_screen == SCREEN_LEFT:
                set_layout(s.group, s.group.prev_layout, False)
            else:
                set_layout(s.group, current_layout, True)
        s.group.prev_screen = s.index


def set_defaults(group):
    if not hasattr(group, "prev_layout"):
        group.prev_layout = layouts[0].name

    if not hasattr(group, "prev_screen"):
        group.prev_screen = -1


def set_layout(group, layout, remember):
    group.cmd_setlayout(layout)
    if remember is True:
        group.prev_layout = layout
