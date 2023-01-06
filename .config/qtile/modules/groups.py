from libqtile.config import Group, Match


groups = [
    Group(
        name="1",
        matches=[Match(wm_class=['firefox'])],
        screen_affinity=1,
    ),
    Group(
        name="2",
        matches=[Match(wm_class=['code-oss'])],
    ),
    Group(
        name="3",
        matches=[Match(wm_class=['keepassxc'])],
    ),
    Group(
        name="4",
        matches=[],
    ),
    Group(
        name="5",
        matches=[],
    ),
    Group(
        name="6",
        matches=[],
    ),
    Group(
        name="7",
        matches=[],
    ),
    Group(
        name="8",
        matches=[],
    ),
    Group(
        name="9",
        matches=[],
    ),
    Group(
        name="0",
        matches=[],
    )
]
