########################################
# ATOMIC                               #
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

from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Match, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import extra.spotify

import os

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Apps
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "f", lazy.spawn('firefox'), desc="Launch Firefox browser"),
    Key([mod], "d", lazy.spawn('discord'), desc="Launch Discord"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.run_extension(extension.DmenuRun(
        selected_background="#44475a",
        background="#282a36",
        font="Cantarell",
        foreground="#f8f8f2",
        selected_foreground="#f8f8f2",
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
    Key([], "Print",
        lazy.spawn("flameshot gui")
    ),
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
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                str(get_group_key(i.name)),
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                str(get_group_key(i.name)),
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.MonadTall(

    ),
]

widget_defaults = dict(
    font="Cantarell",
    fontsize=14,
    padding=5,
    foreground="#f8f8f2",
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox("a\ue0b2b", font="Hack Regular Nerd Font", foreground="#282a36", fontsize=19, padding=0),
                widget.GroupBox(
                    background="#282a36",
                    font="Font Awesome 6 Free",
                    padding=3,
                    highlight_method="text",
                    this_current_screen_border="#f8f8f2",
                    active="#6272a4",
                    inactive="#44475a",
                    disable_drag=True,
                ),
                widget.TextBox("\ue0b0", font="Hack Regular Nerd Font", foreground="#282a36", fontsize=19, padding=0),
                widget.Spacer(),
                widget.WindowName(
                    foreground="#f1fa8c",
                    width=bar.CALCULATED,
                    empty_group_string="~",
                    max_chars=130,
                ),
                widget.Spacer(),
                widget.TextBox("\ue0b2", font="Hack Regular Nerd Font", foreground="#282a36", fontsize=19, padding=0),
                spotify.Spotify(
                    foreground="#ffb86c",
                    play_icon="🎵",
                    pause_icon="~",
                    format="{icon} {track} {icon}",
                    background="#282a36"
                ),
                widget.TextBox("\ue0b0", font="Hack Regular Nerd Font", foreground="#282a36", fontsize=19, padding=0),
            ],
            24,
            border_width=5,
            background="#44475a",
            border_color="#44475a",
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


autostart = [
    "setxkbmap es",
    "feh --bg-fill /home/arnau/.config/qtile/arch.png",
    "picom &",
    "nm-applet &",
]

for cmd in autostart:
    os.system(cmd)
