#!/bin/sh

# Set monitor layout
source ~/.screenlayout/sbs31_default.sh

# Swap esc / caps lock
xmodmap -e "clear lock"
xmodmap -e "keycode 9 = Caps_Lock NoSymbol Caps_Lock"
xmodmap -e "keycode 66 = Escape NoSymbol Escape"

# Keyboard repetition delay / rate
xset r rate 180 30

# Wallpaper
feh --bg-fill /usr/share/endeavouros/backgrounds/endeavouros-wallpaper.png

# Compositor
picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Low battery notifier
~/.config/qtile/scripts/check_battery.sh & disown

# Start welcome
eos-welcome & disown

# Policy kit
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME

# Cloud
nextcloud & disown

# Network manager applet (systray)
nm-applet & disown

# Systray volume
volumeicon & disown

