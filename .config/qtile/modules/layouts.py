from libqtile import layout
from libqtile.config import Match
from .consts import *


layouts = [
    layout.MonadTall(
        margin=MARGIN,
        border_focus=HIGHLIGHT_MAIN,
    ),
    layout.Max(
        margin=MARGIN,
        border_focus=HIGHLIGHT_MAIN,
    ),
    layout.VerticalTile(
        margin=MARGIN,
        border_focus=HIGHLIGHT_MAIN,
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Columns(border_focus_stack='#d75f5f'),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
