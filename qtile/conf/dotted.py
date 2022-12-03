# "Dotted" QTile config
# by Arnau478

from libqtile import qtile, bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os

# Meta/win key as mod key
mod = "mod4"

# Detect terminal
terminal = guess_terminal()

# Do not follow mouse focus
follow_mouse_focus = False

# Smart focus on window activation
focus_on_window_activation = "smart"

keys = [
    # Quick open
    Key([mod], "r", lazy.spawn("rofi -show drun")), # Rofi drun
    Key([mod], "period", lazy.spawn("rofi -show emoji")), # Rofi emoji selector
    Key([mod], "c", lazy.spawn("bash -c 'alacritty --working-directory ~/code/$(ls ~/code | rofi -dmenu) -e nvim'")), # Quick code
    Key([mod], "Return", lazy.spawn(terminal)), # Terminal

    # Manage windows
    Key([mod, "shift"], "q", lazy.window.kill()), # Kill window
    Key([mod], "F11", lazy.window.toggle_fullscreen()), # Toggle fullscreen
    Key([mod], "F9", lazy.window.disable_floating()), # Disable floating window

    # Acions
    Key([], "Print", lazy.spawn("flameshot gui")), # Print screen

    # Quit and reload
    Key([mod, "control"], "q", lazy.shutdown()), # Quit QTile
    Key([mod, "control"], "r", lazy.reload_config()), # Reload config
]

# Groups 1-5
groups = [Group(str(i+1), label="●") for i in range(5)]

# Keys for that groups
for i in groups:
    keys.extend(
        [
            Key([mod], i.name, lazy.group[i.name].toscreen()), # Switch to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)), # Move window and switch
        ]
    )

layouts = [
    layout.Bsp(
        margin=10,
    ),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)

extension_defaults = widget_defaults.copy()

# Screens (and bars)
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    text="\uF303",
                    background="#bd92f9",
                    foreground="282a36",
                    fontsize=16,
                    ),
                widget.TextBox(
                    text="\uE0B0",
                    padding=0,
                    fontsize=26,
                    background="#44475a",
                    foreground="#bd92f9",
                ),
                widget.GroupBox(
                    highlight_method="text",
                    background="#44475a",
                    inactive="#282a36",
                    this_current_screen_border="#f8f8f2",
                    active="#6272a4",
                    fontsize=15,
                ),
                widget.TextBox(
                    text="\uE0B0",
                    padding=0,
                    fontsize=26,
                    background="#282a36",
                    foreground="#44475a",
                ),
                widget.Spacer(
                    length=bar.STRETCH,
                ),
                widget.Systray(
                    icon_size=16,
                ),
                widget.Spacer(
                    length=4,
                ),
                widget.TextBox(
                    text="\uE0B2",
                    padding=0,
                    fontsize=26,
                    background="#282a36",
                    foreground="#44475a",
                ),
                widget.TextBox(
                    text="\uE0B2",
                    padding=0,
                    fontsize=26,
                    background="#44475a",
                    foreground="#bd92f9",
                ),
            ],
            24,
            margin=[5, 5, 5, 5],
            background="#282a36",
        )
    )
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()), # Move floating
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()), # Resize floating
]

# Floating layout
floating_layout = layout.Floating(
    float_runes=[
        *layout.Floating.default_float_rules,
    ]
)

@hook.subscribe.float_change
def set_hint():
    for window in qtile.windows_map.values():
        if not isinstance(window, Internal):
            window.window.set_property("IS_FLOATING", str(window.floating), type="STRING", format=8)

@hook.subscribe.client_focus
def set_hint(window):
    window.window.set_property("IS_FLOATING", str(window.floating), type="STRING", format=8)

# Autorun
os.system("~/.config/qtile/autorun.sh")
