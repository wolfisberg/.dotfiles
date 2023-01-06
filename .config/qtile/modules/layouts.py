from libqtile import layout
from libqtile.config import Match

from modules.consts import MARGIN, HIGHLIGHT_MAIN
from modules.verticaltile_layout import VerticalTile


LAYOUT_VERTICAL_TILE = VerticalTile(
    margin=MARGIN,
    border_focus=HIGHLIGHT_MAIN,
)

LAYOUT_MONAD_TALL = layout.MonadTall(
    margin=MARGIN,
    border_focus=HIGHLIGHT_MAIN,
)

LAYOUT_MAX = layout.Max(
    margin=MARGIN,
    border_focus=HIGHLIGHT_MAIN,
)

LAYOUT_BSP = layout.Bsp(
    fair=False,
    border_on_single=True,
    margin=MARGIN,
    border_focus=HIGHLIGHT_MAIN,
)

layouts = [
    LAYOUT_MONAD_TALL,
    LAYOUT_MAX,
    LAYOUT_VERTICAL_TILE,
    # LAYOUT_BSP,
    # layout.Stack(num_stacks=2),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.MonadThreeCol(),
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
