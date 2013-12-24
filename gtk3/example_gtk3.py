#!/usr/bin/env python3.3
# -*- encoding: UTF-8 -*-

# 2013 Alexandre Vicenzi (vicenzi.alexandre at gmail com)

from gi.repository import Gtk

from gladebuilder import GladeWindow

class MyWindow(GladeWindow):

	def __init__(self):
		GladeWindow.__init__(self, 'example-gtk3.glade', 'window1')

	def on_ok_clicked(self, *args):
		self.w.show({'entry1': 'Foo bar', 'button1': 'OK'})

	def on_close(self, *args):
		Gtk.main_quit(*args)

if __name__ == "__main__":
	Win = MyWindow()

	Win.w.scale1.set_range(0.0, 1)
	Win.w.scale2.set_range(0.0, 1)
	Win.w.spinbutton1.set_range(0.0, 1)


	dict = {
		"window1": "Example GTK 3",
		"button1": "Click",
		"togglebutton1": "Click me too",
		"checkbutton1": True,
		"entry1": "Some text",
		"spinbutton1": 0.2,
		#"combobox1": ,
		#"comboboxtext1": ,
		"label1": "<b>Bold label</b>",
		"linkbutton1": "https://www.google.com",
		"accellabel1": "<i>Italic accellabel</i>",
		"scalebutton1": 30,
		"volumebutton1": 0.8,
		"scale1": 0.5,
		"scale2": 0.6,
		#"calendar1": ,
		#"treeview1": ,
		#"treeview-selection1": ,
		#"textview1": ,
		#"radiobutton1": ,
		#"radiobutton2": ,
		#"radiobutton3": ,
		"spinner1": True,
		"progressbar1": 0.5,
	}

	Win.w.show(dict)

	dict = {
		"checkbutton1": "Is checked",
		'volumebutton1': 'Volume',
		'scalebutton1': 'Scale button',
		'linkbutton1': 'Go to google.com'
	}

	Win.w.show(dict)

	Win.show()