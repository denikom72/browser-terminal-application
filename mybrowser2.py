#!/usr/bin/python3
import sys
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit', '3.0')
from gi.repository import Gtk, WebKit, Vte

DEFAULT_URL = 'http://www.google.com'

class SimpleBrowser:
    def __init__(self):
        self.window = Gtk.Window()
        self.window.set_position(Gtk.WindowPosition.CENTER)
        self.window.connect('delete-event', self.close_application)
        self.window.set_default_size(1350, 800)

        go_button = Gtk.Button("Go to...")
        go_button.connect("clicked", self.load_url)
        self.url_bar = Gtk.Entry()
        self.url_bar.connect("activate", self.load_url)

        self.webview = WebKit.WebView()

        self.go_back = Gtk.Button("Back")
        self.go_back.connect("clicked", lambda x: self.webview.go_back())
        self.go_forward = Gtk.Button("Forward")
        self.go_forward.connect("clicked", lambda x: self.webview.go_forward())

        url_box = Gtk.HBox()
        url_box.pack_start(self.url_bar, True, True, 0)
        url_box.pack_start(go_button, False, False, 0)

        v = Vte.Terminal()
        v.connect("child-exited", lambda term: Gtk.main_quit())
        v.fork_command()

        vbox3 = Gtk.VBox(spacing=0)
        vbox3.set_border_width(0)
        self.txt_url3 = Gtk.Entry()
        self.txt_url3.connect('activate', self.txt_url_activate)
        vbox3.pack_start(url_box, False, False, 0)

        vbox2 = Gtk.VBox(spacing=1)
        vbox2.set_border_width(1)
        self.txt_url2 = Gtk.Entry()
        self.txt_url2.connect('activate', self.txt_url_activate)
        scrolled_window2 = Gtk.ScrolledWindow()
        scrolled_window2.add(self.webview)
        vbox2.pack_start(scrolled_window2, True, True, 0)

        vbox1 = Gtk.VBox(spacing=1)
        vbox1.set_border_width(1)
        self.txt_url1 = Gtk.Entry()
        self.txt_url1.connect('activate', self.txt_url_activate)
        scrolled_window1 = Gtk.ScrolledWindow()
        scrolled_window1.add(v)
        vbox1.pack_start(scrolled_window1, True, True, 0)

        vboxMain = Gtk.VBox(False, 0)
        vboxMain.pack_start(vbox3, False, False, 0)
        vboxMain.pack_start(vbox2, True, True, 0)
        vboxMain.pack_start(vbox1, True, True, 0)

        self.window.add(vboxMain)

    def load_url(self, widget):
        url = self.url_bar.get_text()
        if not "://" in url:
            url = "https://" + url
        self.webview.load_uri(url)

    def txt_url_activate(self, entry):
        self.load_url(entry.get_text())

    def show(self):
        self.window.show_all()

    def close_application(self, widget, event, data=None):
        Gtk.main_quit()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = DEFAULT_URL

    Gtk.init(None)
    browser = SimpleBrowser()
    browser.show()
    Gtk.main()
