# Qtile Config File
# Config File Libs
from typing import List  # noqa: F401
from libqtile import bar, layout, widget
#from libqtile.widget.base import ThreadPoolText
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os

#Var
mod = "mod4"
alt = "mod1"
terminal = "alacritty"
browser = "falkon"
browser_p = "falkon -i"
filemanager = "thunar"
screenshot = "flameshot gui"
ide = "code"

#Shortcuts
keys = [
    # Sound
    Key([], "XF86AudioMute",
        lazy.spawn("pactl set-sink-mute 0 toggle")),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-mute 0 false && pactl set-sink-volume 0 -5%")),
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-mute 0 false && pactl set-sink-volume 0 +5%")),
    
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.up(),
        desc="Move focus up in stack pane"),
    Key([mod], "j", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "h", lazy.layout.left(),
        desc="Move focus up in stack pane"),
    Key([mod], "l", lazy.layout.right(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "shift"], "h", lazy.layout.swap_left(),
        desc="Move window left in current stack "),
    Key([mod, "shift"], "l", lazy.layout.swap_right(),
        desc="Move window right in current stack "),

    # X
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),

    # maximize/Normalize the window
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),

    # Switch window focus to other pane(s) of stack
    Key([alt], "Tab", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    
    #Qtile Shortcut
    Key([mod], "F5", lazy.restart(), desc="Restart qtile"),
    Key([alt, "control"], "l", lazy.shutdown(), desc="LogOut"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([alt], "space", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    #App Shortcut
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch Browser"),
    Key([mod,"shift"], "b", lazy.spawn(browser_p), desc="Launch Browser"),
    Key([mod], "e", lazy.spawn(filemanager), desc="Launch FileManager"),
    Key([mod], "s", lazy.spawn(screenshot), desc="Take Screen Shot"),
    Key([mod], "d", lazy.spawn(ide), desc="Launch IDE"),
]

groups = [Group("FiM"), Group("WWW"), Group("Ter"), Group("Med"), Group("DEV"), Group("VBOX")]

keys.append(Key([mod], "1", lazy.group["FiM"].toscreen()))        # Switch to another group
keys.append(Key([mod, "shift"], "1", lazy.window.togroup("FiM"))) # Send current window to another group

keys.append(Key([mod], "2", lazy.group["WWW"].toscreen()))        # Switch to another group
keys.append(Key([mod, "shift"], "2", lazy.window.togroup("WWW"))) # Send current window to another group

keys.append(Key([mod], "3", lazy.group["Ter"].toscreen()))        # Switch to another group
keys.append(Key([mod, "shift"], "3", lazy.window.togroup("Ter"))) # Send current window to another group

keys.append(Key([mod], "4", lazy.group["Med"].toscreen()))        # Switch to another group
keys.append(Key([mod, "shift"], "4", lazy.window.togroup("Med"))) # Send current window to another group

keys.append(Key([mod], "5", lazy.group["DEV"].toscreen()))        # Switch to another group
keys.append(Key([mod, "shift"], "5", lazy.window.togroup("DEV"))) # Send current window to another group

keys.append(Key([mod], "6", lazy.group["VBOX"].toscreen()))        # Switch to another group
keys.append(Key([mod, "shift"], "6", lazy.window.togroup("VBOX"))) # Send current window to another group


layout_theme = {"border_width": 3,
                "margin": 6,
                "border_focus": "#6272A4",
                "border_normal": "#282A36"                                   }

layouts = [
    # Try more layouts by unleashing below layouts.
     layout.MonadTall(**layout_theme),
    # layout.MonadWide(**layout_theme),
    # layout.Max(),
    # layout.Floating(),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Columns(),
     layout.Matrix(**layout_theme),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

os.system("picom -b --config ~/.config/picom/picom.conf")
os.system("feh --bg-scale ~/Pictures/wallpp.*")
os.system("setxkbmap -layout us,ir")
os.system("setxkbmap -option 'grp:alt_shift_toggle'")

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Sep(foreground="#282A36", padding=2),
                widget.CurrentLayoutIcon(custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],padding = 0,scale = 0.7),
                widget.Sep(foreground="#44475A"),
                widget.GroupBox(
                    foreground="#F8F8F2",
                    active="#F8F8F2",
                    inactive="#BFBFBF",
                    this_current_screen_border="#44475A",
                    borderwidth=2,
                    hide_unused=True,
                    urgent_text="#F8F8F2",
                    urgent_border="#FF5555",
                    ),
                widget.Sep(foreground="#44475A"),
                widget.WindowName(foreground="#F8F8F2"),
                widget.Sep(foreground="#44475A"),
                widget.Systray(foreground="#F8F8F2"),
                widget.Sep(foreground="#44475A"),
                widget.Clock(format="%Y/%m/%d %a %H:%M",foreground="#F8F8F2"),
                widget.Sep(foreground="000000",padding=2),
            ],
            24,
            opacity=1,
            background="#282A36"
        ),
        top=bar.Bar(
            [
                widget.Sep(foreground="#282A36",padding=2),
                widget.CPU(format="CPU: {load_percent}%",foreground="#F8F8F2"),
                widget.ThermalSensor(tag_sensor="CPU",foreground="#F8F8F2"),
                widget.Sep(foreground="#44475A"),
                widget.Memory(format="RAM: {MemUsed}M",foreground="#F8F8F2"),
                widget.Sep(foreground="#44475A"),
                widget.Net(format="Net: {down} ↓↑ {up}",foreground="#F8F8F2"),
                #widget.Net(interface="wpl2s0",format="Wifi: {down} ↓↑ {up}",foreground="#F8F8F2"),
                #widget.Sep(foreground="#44475A"),
                #widget.Net(interface="eno1",format="Lan: {down} ↓↑ {up}",foreground="#F8F8F2"),
                widget.Sep(foreground="#44475A"),
                widget.CheckUpdates(foreground="#F8F8F2"),
                widget.Sep(foreground="#44475A"),
                #widget.Notify(foreground="#F8F8F2"),
                widget.Battery(format="Battery: {percent:2.0%} {hour:d}:{min:02d}",foreground="#F8F8F2",update_interval=60),
                widget.Sep(foreground="#44475A"),
                #widget.GmailChecker(username="", password="",update_interval=30,foreground="#F8F8F2"),
                #widget.Sep(foreground="#44475A"),
                widget.Prompt(foreground="#F8F8F2"),
            ],
            24,
            opacity=1,
            background="#282A36"
        ),                
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
