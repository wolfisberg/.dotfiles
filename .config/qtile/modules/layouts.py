from libqtile import layout
from libqtile.config import Match

from modules.consts import MARGIN, BORDER_FOCUS, BORDER_NORMAL
from modules.verticaltile_layout import VerticalTile


default_args = dict(
    margin=MARGIN,
    border_focus=BORDER_FOCUS,
    border_normal=BORDER_NORMAL,
    border_width=2,
)

LAYOUT_VERTICAL_TILE = VerticalTile(**default_args)

LAYOUT_MONAD_TALL = layout.MonadTall(**default_args)

LAYOUT_MAX = layout.Max(**default_args)

LAYOUT_BSP = layout.Bsp(
    **default_args,
    border_on_single=True,
    fair=False,
)

layouts = [
    LAYOUT_MONAD_TALL,
    LAYOUT_MAX,
    LAYOUT_VERTICAL_TILE,
    # LAYOUT_BSP,
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
