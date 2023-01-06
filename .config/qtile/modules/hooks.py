import os
import subprocess

from libqtile import hook, qtile

from modules.consts import SCREEN_LEFT
from modules.layouts import LAYOUT_VERTICAL_TILE, LAYOUT_MONAD_TALL


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])


@hook.subscribe.setgroup
def set_layout_per_screen():
    for s in qtile.screens:
        if s.index == SCREEN_LEFT:
            s.group.cmd_setlayout(LAYOUT_VERTICAL_TILE.name)
        else:
            s.group.cmd_setlayout(LAYOUT_MONAD_TALL.name)
