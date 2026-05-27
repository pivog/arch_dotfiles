#!/usr/bin/env python3
import gi
import signal

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class DimOverlay(Gtk.Window):
    def __init__(self):
        super().__init__(type=Gtk.WindowType.TOPLEVEL)
        self.set_title("hyprlock-dim-overlay")
        
        # Strip borders and decorations
        self.set_decorated(False)
        self.set_app_paintable(True)
        
        # Enable RGBA (transparency) support
        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual and screen.is_composited():
            self.set_visual(visual)

        self.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 0, 0, 0.5))

        self.maximize()
        self.show_all()

if __name__ == '__main__':
    # Allow the script to be killed cleanly by Hyprland/Bash
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    signal.signal(signal.SIGTERM, signal.SIG_DFL)
    
    app = DimOverlay()
    Gtk.main()
