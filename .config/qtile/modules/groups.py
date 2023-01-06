from libqtile.config import Group, Match


groups = [
    Group(
        name="1",
        label="[1] WEB",
        matches=[Match(wm_class=['firefox'])],
        screen_affinity=1,
    ),
    Group(
        name="2",
        label="[2] WRK1",
        matches=[Match(wm_class=['code-oss'])],
    ),
    Group(
        name="3",
        label="[3] WRK2",
        # postman, git, dev browser
        matches=[Match(wm_class=[])],
    ),
    Group(
        name="4",
        label="[4] MSG",
        # thunderbird, slack, teams, signal
        matches=[Match(wm_class=[])],
    ),
    Group(
        name="5",
        label="[5] MUSIC",
        matches=[Match(wm_class=['spotify'])],
    ),
    Group(
        name="6",
        label="[6] MISC",
        matches=[Match(wm_class=['keepassxc'])],
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
