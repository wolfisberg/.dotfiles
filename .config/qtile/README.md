# Qtile Setup

Home of the Qtile configuration.

## Todos

### Bugs
* Sometimes it seems as though keybindings / keys (super and others) are "trapped" in an application and not forwarded for processing to qtile in terminal etc?

### Improvements
* Add some kind of task switcher alt+tab style (rofi?)
* Set keybind to quickly get rid of a window (minimizing or sending to hidden group). Add a rofi launcher to retrieve the hidden windows. [docs](https://docs.qtile.org/en/latest/manual/ref/commands.html#libqtile.backend.base.Window.toggle_minimize)

    ```Key([MOD, CTRL], "space", lazy.layout.minimize(), desc="minimize window")```

* Find (a collection of) wallpapers for triple monitor setup.

### Workarounds
* Custom match hook for spotify
* Scratchpads ignored from `rofi -show window` via predefined filter input (see github issue)

### Projects
* Write some kind of service (go, systemd, dbus?), that listens on dbus for "mpris:artUrl" and pulls album covers as wallpapers (`feh` can use urls for wallpapers)
    ```
    dbus-send --print-reply --session --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:'org.mpris.MediaPlayer2.Player' string:'Metadata'
    ```
