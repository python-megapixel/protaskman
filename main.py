#ProTaskman main.py

import gi
try:
	gi.require_version('Gtk', '4.0')
except ValueError:
	print("Gtk+3 is not available. Please make sure that you have GTK+ installed.")
	
