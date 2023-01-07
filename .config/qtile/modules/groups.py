from libqtile.config import Group, Match, ScratchPad, DropDown

from modules.consts import SCREEN_LEFT, SCREEN_MIDDLE, SCREEN_RIGHT


GRP_SCRATCHPAD = "scratchpad"
DD_PASSWORD = "dd_password"
DD_TERM = "dd_terminal"
DD_FM = "dd_files"
DD_TUI_FM = "dd_tui_files"

dd_args = dict(
    opacity=1,
    width=0.6,
    height=0.7,
    y=0.05,
    x=0.25,
    on_focus_lost_hide=True,
    warp_pointer=True,
)

groups = [
    ScratchPad(
        GRP_SCRATCHPAD,
        [
            DropDown(DD_PASSWORD, "keepassxc", **dd_args),
            DropDown(DD_TERM, "alacritty", **dd_args),
            DropDown(DD_FM, "thunar", **dd_args),
            DropDown(DD_TUI_FM, "alacritty -e ranger", **dd_args),
        ],
        single=True
    ),
    Group(
        name="1",
        label="[1] WEB",
        matches=[Match(wm_class=['firefox'])],
        screen_affinity=SCREEN_MIDDLE,
    ),
    Group(
        name="2",
        label="[2] WRK1",
        matches=[Match(wm_class=['code-oss'])],
        screen_affinity=SCREEN_MIDDLE,
    ),
    Group(
        name="3",
        label="[3] WRK2",
        # postman, git, dev browser
        matches=[Match(wm_class=[])],
        screen_affinity=SCREEN_LEFT,
    ),
    Group(
        name="4",
        label="[4] MSG",
        # thunderbird, slack, teams, signal
        matches=[Match(wm_class=[])],
        screen_affinity=SCREEN_RIGHT,
    ),
    Group(
        name="5",
        label="[5] MUSIC",
        matches=[Match(wm_class=['spotify'])],
        screen_affinity=SCREEN_RIGHT,
    ),
    Group(
        name="6",
        label="[6] MISC",
        matches=[Match(wm_class=['keepassxc'])],
        screen_affinity=SCREEN_LEFT,
    ),
    # Group(
    #     name="7",
    #     matches=[],
    # ),
    # Group(
    #     name="8",
    #     matches=[],
    # ),
    # Group(
    #     name="9",
    #     matches=[],
    # ),
    # Group(
    #     name="0",
    #     matches=[],
    # )
]
