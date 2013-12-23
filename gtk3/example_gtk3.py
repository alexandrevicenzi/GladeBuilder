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

	dict = {
		"window1": "Example GTK 3",
		"button1": "Click",
		"togglebutton1": ,
		"checkbutton1": True,
		"entry1": "Some text",
		"spinbutton1": 0.1,
		"combobox1": ,
		"comboboxtext1": ,
		"label1": "<b>Bold text<b>",
		"linkbutton1": ,
		"accellabel1": ,
		"scalebutton1": ,
		"volumebutton1": ,
		"scale1": ,
		"scale2": ,
		"calendar1": ,
		"treeview1": ,
		"treeview-selection1": ,
		"textview1": ,
		"radiobutton1": ,
		"radiobutton2": ,
		"radiobutton3": ,
		"spinner1": ,
		"progressbar1": 0.5,
	}

	Win.w.show(dict)
	Win.show()