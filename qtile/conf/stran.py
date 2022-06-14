########################################
# STRAN                                #
#                                      #
# ~ A qTile configuration ~            #
########################################

# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Match, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
import os.path
import socket
import datetime
import spotify

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
            desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    # Grow windows
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Spawn apps
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "f", lazy.spawn('firefox'), desc="Launch Firefox browser"),
    Key([mod], "d", lazy.spawn('discord'), desc="Launch Discord"),
    
    # Process control
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.run_extension(extension.DmenuRun(
        selected_background="#bd93f9",
        background="#222222",
        font="Cantarell",
        foreground="#bd93f9",
        selected_foreground="#ffffff",        
        
    )), desc="Spawn a command using a prompt widget"),

    # Volume keys
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer -c 1 -q set Master 2%+")
    ),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("amixer -c 1 -q set Master 2%-")
    ),
    Key([], "XF86AudioMute",
        lazy.spawn("amixer -c 1 -q set Master toggle")
    ),

    # Screenshots
    Key([], "Print", lazy.spawn("flameshot gui")),
]

gliphs = {
    "terminal": "",
    "firefox": "",
    "code": "",
    "gamepad": "",
    "headset": "",
    "sign-out": "",
    "cog": "",
    "arrow-left": "🭮",
    "arrow-right": "🭬",
}

__groups = {
    1: Group(gliphs["terminal"]),
    2: Group(gliphs["firefox"], matches=[Match(wm_class=["firefox"])]),
    3: Group(gliphs["code"]),
    4: Group(gliphs["gamepad"], matches=[Match(wm_class=["steam"])]),
    9: Group(gliphs["cog"]),
    0: Group(gliphs["headset"], matches=[Match(wm_class=["discord"])]),
}

groups = [__groups[i] for i in __groups]

def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]

for i in groups:
    keys.extend([
        Key([mod], str(get_group_key(i.name)), lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod, "shift"], str(get_group_key(i.name)), lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.MonadTall(
        name="Half split",
        border_width=3,
        border_focus="#bd93f9",
        single_border_width=0,
        border_normal="#222222",
        margin=8,
        single_margin=16
    ),
]

widget_defaults = dict(
    font='Cantarell',
    fontsize=14,
    padding=5,
    foreground='#f8f8f2'
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    highlight_color=["#44475a"],
                    highlight_method="line",
                    this_current_screen_border="#bd93f9",
                    inactive="#666666",
                    block_highlight_text_color="#bd93f9",
                    active="#f8f8f2",
                    font="Font Awesome 6 Free",
                    disable_drag=True,
                ),
                widget.Spacer(8),
                widget.CheckUpdates(
                    custom_command="checkupdates",
                    update_interval=1800,
                    display_format="{updates}⬆️",
                    padding=10,
                    execute=(terminal + " -e sudo pacman -Syyu"),
                ),
                widget.WindowName(),
                widget.Spacer(bar.STRETCH),
                widget.Spacer(8),
                widget.Systray(),
                widget.Spacer(8),
                widget.Clock(
                    format="%d/%m/%Y %H:%M",
                    timezone="GMT+0",
                ),
                widget.Battery(
                    format="{percent:2.0%} {char}"
                ),
                widget.Spacer(16),
                spotify.Spotify(
                    foreground="#ffb86c",
                    play_icon="🎵",
                    pause_icon="~",
                    format="{icon} {track} {icon}",
                ),
                widget.Spacer(16),
            ],
            24,
            background="#282a36",
            opacity=0.8,
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='qemu'),  # qemu
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"

autostart = [
    "setxkbmap es",
    "feh --bg-fill /home/arnau/.config/qtile/arch.png",
    "picom &",
    "nm-applet &",
]

for cmd in autostart:
    os.system(cmd)
