from libqtile.config import Group, Match

from modules.consts import SCREEN_LEFT, SCREEN_MIDDLE, SCREEN_RIGHT


groups = [
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
