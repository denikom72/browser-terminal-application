#!/usr/bin/python
import sys
import gtk
import webkit
import vte
DEFAULT_URL = 'http://www.google.com' # Change this as you Wish
class SimpleBrowser: # needs GTK, Python, Webkit-GTK
	def __init__(self):
		self.window = gtk.Window()
		self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
		self.window.connect('delete_event', self.close_application)
		self.window.set_default_size(1350, 800)
		
		go_button = gtk.Button("go to...")
		go_button.connect("clicked", self._load_url)
		self.url_bar = gtk.Entry()
		self.url_bar.connect("activate", self._load_url)
		
		self.webview1 = webkit.WebView()
		
		self.go_back = gtk.Button("Back")
		self.go_back.connect("clicked", lambda x: self.webview.go_back())
		self.go_forward = gtk.Button("Forward")
		self.go_forward.connect("clicked", lambda x: self.webview.go_forward())
		
		url_box = gtk.HBox()
		url_box.pack_start(self.url_bar, True, True, 0)
		url_box.pack_start(go_button, True, True, 0)
		
		v = vte.Terminal ()
		v.connect ("child-exited", lambda term: gtk.main_quit())
		
		v.fork_command()
		
		vbox3 = gtk.VBox(spacing=0)
		vbox3.set_border_width(0)
		
		self.txt_url3 = gtk.Entry()
		self.txt_url3.connect('activate', self._txt_url_activate)
		
		vbox3.pack_start(url_box, fill=False, expand=False)
		
		
		vbox2 = gtk.VBox(spacing=1)
		vbox2.set_border_width(1)
		self.txt_url2 = gtk.Entry()
		self.txt_url2.connect('activate', self._txt_url_activate)
		self.scrolled_window2 = gtk.ScrolledWindow()
		self.scrolled_window2.add(self.webview1)
		vbox2.pack_start(self.scrolled_window2, fill=True, expand=True)
		
		vbox1 = gtk.VBox(spacing=1)
		vbox1.set_border_width(1)
		self.txt_url1 = gtk.Entry()
		self.txt_url1.connect('activate', self._txt_url_activate)
		self.scrolled_window1 = gtk.ScrolledWindow()
		self.scrolled_window1.add(v)
		vbox1.pack_start(self.scrolled_window1, fill=True, expand=True)
		
		vboxMain = gtk.VBox(False, 0)
		
		vboxMain.pack_start(vbox3, fill=False, expand=False)
		vboxMain.pack_start(vbox2, fill=True, expand=True)
		vboxMain.pack_start(vbox1, fill=True, expand=True)
		
		self.window.add(vboxMain)

	def _load_url(self, widget):
        	url = self.url_bar.get_text()
	 	if not "://" in url:
     		    url = "https://" + url
		self.webview1.load_uri(url)

	def _txt_url_activate(self, entry):
        	self._load(entry.get_text())

	def open(self, url):
        	self.txt_url.set_text(url)
        	self.window.set_title('%s' % url)
        	#self._load(url)
	def show(self):
        	self.window.show_all()
	def close_application(self, widget, event, data=None):
        	gtk.main_quit()

if __name__ == '__main__':
	if len(sys.argv) > 1:
		url = sys.argv[1]
	else:
        	url = DEFAULT_URL
	gtk.gdk.threads_init()
	browser = SimpleBrowser()
	#browser.open(url)
	browser.show()
	gtk.main()
