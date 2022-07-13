import os

cmd = 'apt update && apt upgrade && wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb && apt install --assume-yes -y ./chrome-remote-desktop_current_amd64.deb && apt install -y xfce4 desktop-base dbus-x11 xscreensaver xfce4-terminal firefox-esr geany vim-gtk3'
os.system(cmd)
print("Desktop up. Thanks for using!")
