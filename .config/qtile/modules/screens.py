import os

from libqtile import qtile, bar, widget
from libqtile.config import Screen

# from modules.widgets import volume
from modules.consts import TERMINAL, WIDGET_SIZE_DEFAULT, \
    WIDGET_SIZE_TWOK, BACKGROUND_DARK, HIGHLIGHT_MAIN, MARGIN, \
    FONT_SIZE_DEFAULT, FONT_SIZE_TWOK


def create_screen(main=False, twok=False):
    WIDGET_SIZE = WIDGET_SIZE_TWOK if twok else WIDGET_SIZE_DEFAULT
    FONT_SIZE = FONT_SIZE_TWOK if twok else FONT_SIZE_DEFAULT
    spacer = widget.Spacer(
        length=10,
        background=BACKGROUND_DARK,
    )

    base_widgets = [
        widget.Sep(
            padding=3,
            linewidth=0,
            background=BACKGROUND_DARK,
        ),
        widget.Image(
            filename='~/.config/qtile/eos-c.png',
            margin=3,
            background=BACKGROUND_DARK,
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn("rofi -show combi")
            },
        ),
        widget.Sep(
            padding=4,
            linewidth=0,
            background=BACKGROUND_DARK,
        ),
        widget.GroupBox(
            highlight_method='line',
            this_screen_border=HIGHLIGHT_MAIN,
            this_current_screen_border=HIGHLIGHT_MAIN,
            active="#ffffff",
            inactive="#848e96",
            background=BACKGROUND_DARK,
            fontsize=FONT_SIZE,
        ),
        widget.TextBox(
            text='',
            padding=0,
            fontsize=WIDGET_SIZE,
            foreground=BACKGROUND_DARK,
        ),
        widget.Prompt(),
        widget.Spacer(
            length=10,
        ),
        widget.TaskList(
            foreground='#99c0de',
            fontsize=FONT_SIZE + 1,
            borderwidth=1,
            highlight_method="block",
            border=HIGHLIGHT_MAIN + "44",
            icon_size=0,
            padding_y=3,
            padding_x=6,
        ),
        widget.Mpris2(
            foreground="#ffffff",
            fontsize=FONT_SIZE + 1,
            display_metadata=["xesam:artist", "xesam:title", "xesam:album"],
            scroll=False,
        ),
        widget.TextBox(
            text='',
            padding=0,
            fontsize=WIDGET_SIZE,
            foreground=BACKGROUND_DARK,
        ),
        widget.CurrentLayoutIcon(
            scale=0.75,
            background=BACKGROUND_DARK,
        ),
    ]

    main_widgets = [
        widget.CheckUpdates(
            update_interval=1800,
            distro="Arch_yay",
            display_format="{updates} Updates",
            foreground="#ffffff",
            mouse_callbacks={
                'Button1':
                lambda: qtile.cmd_spawn(TERMINAL + ' -e yay -Syu')
            },
            background=BACKGROUND_DARK,
        ),
        widget.Systray(
            icon_size=20,
            background=BACKGROUND_DARK,
        ),
        spacer,
        # volume,
        spacer,
        widget.Clock(
            format='%Y-%m-%d %a %I:%M %p',
            background=BACKGROUND_DARK,
            foreground='#ffffff',
            fontsize=FONT_SIZE + 1,
        ),
        spacer,
        widget.TextBox(
            text='',
            mouse_callbacks={
                'Button1':
                lambda: qtile.cmd_spawn(
                    os.path.expanduser('~/.config/rofi/powermenu.sh')
                )
            },
            foreground='#e39378',
            background=BACKGROUND_DARK,
        ),
        spacer,
    ]

    return Screen(top=bar.Bar(
        base_widgets + main_widgets if main else base_widgets,
        30,
        background="#40455200",
        opacity=0.3,
        margin=[MARGIN, MARGIN, 0, MARGIN],
    ))


screens = [
    create_screen(main=True),
    create_screen(twok=True),
    create_screen(twok=True),
]
