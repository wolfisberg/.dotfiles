# TODO: keys / super / trapped in terminal etc?
# TODO: alt+tab? (rofi?)
# TODO: on launching client, focus
# TODO: write (go?) service (systemd?) to listen for mpris:artUrl
# on dbus and set wallpapers
# dbus-send --print-reply --session --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:'org.mpris.MediaPlayer2.Player' string:'Metadata'
# TODO: set keybind for minimizing windows, and rofi command to resurrect them?
# Key([MOD, CTRL], "space", lazy.layout.minimize(), desc="minimize window"),
# https://docs.qtile.org/en/latest/manual/ref/commands.html#libqtile.backend.base.Window.toggle_minimize
# TODO: ignore scratchpads on window switcher/rofi
