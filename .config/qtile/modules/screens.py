import os

from libqtile import qtile, bar, widget
from libqtile.config import Screen

from modules.widgets import volume
from modules.consts import TERMINAL, FONT_SIZE_DEFAULT,\
    FONT_SIZE_TWOK, BACKGROUND_DARK, HIGHLIGHT_MAIN, MARGIN


def create_screen(main=False, twok=False):
    FONT_SIZE = FONT_SIZE_TWOK if twok else FONT_SIZE_DEFAULT
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
        ),
        widget.TextBox(
            text='',
            padding=0,
            fontsize=FONT_SIZE,
            foreground=BACKGROUND_DARK,
        ),
        widget.Prompt(),
        widget.Spacer(
            length=5,
        ),
        widget.WindowName(
            foreground='#99c0de', fmt='{}',
        ),
        widget.Chord(
            chords_colors={
                'launch': ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        widget.CurrentLayoutIcon(
            scale=0.75,
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
        ),
        widget.TextBox(
            text='',
            padding=0,
            fontsize=FONT_SIZE,
            foreground=BACKGROUND_DARK,
        ),
        volume,
        widget.TextBox(
            text='',
            padding=0,
            fontsize=FONT_SIZE,
            foreground=BACKGROUND_DARK,
        ),
        widget.TextBox(
            text='',
            padding=0,
            fontsize=FONT_SIZE,
            foreground=BACKGROUND_DARK,
        ),
        widget.Clock(
            format=' %Y-%m-%d %a %I:%M %p',
            background=BACKGROUND_DARK,
            foreground='#9bd689',
        ),
        widget.TextBox(
            text='',
            padding=0,
            fontsize=FONT_SIZE,
            foreground=BACKGROUND_DARK,
        ),
        widget.TextBox(
            text='',
            mouse_callbacks={
                'Button1':
                lambda: qtile.cmd_spawn(
                    os.path.expanduser('~/.config/rofi/powermenu.sh')
                )
            },
            foreground='#e39378'
        ),
    ]

    return Screen(top=bar.Bar(
        base_widgets + main_widgets if main else base_widgets,
        30,
        background="#40455280",
        opacity=0.6,
        margin=[MARGIN, MARGIN, 0, MARGIN],
    ))


screens = [
    create_screen(main=True),
    create_screen(twok=True),
    create_screen(twok=True),
]
