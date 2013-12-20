#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

# A simple Glade Builder class.
# 2013 (c) Alexandre Vicenzi (vicenzi.alexandre at gmail com)

import sys

GTK3 = sys.version_info.major == 3

if GTK3:
	try:
		from gi.repository import Gtk	
	except Exception, e:
		print('Failed to load Gtk 3: ' + e.message)
		sys.exit(1)
else:
	try:
		import pygtk
		pygtk.require("2.0")	
	except Exception, e:
		print('Failed to load PyGtk: ' + e.message)
		sys.exit(1)

  	try:
		import gtk as Gtk
		import gtk.glade as Glade
	except Exception, e:
		print('Failed to load Gtk 2: ' + e.message)
		sys.exit(1)

class W:

	def __init__(self):
		pass

	def clear(self):
		''' Reset window data. '''
		for name in dir(self):

			widget = getattr(self, name)

			if not issubclass(type(widget), Gtk.Widget): continue

			# TODO: Add all Gtk Widgets.
			if isinstance(widget, Gtk.Entry) or issubclass(type(widget), Gtk.Entry):
				widget.set_text('')

	def show(self, dict):
		''' 
			Show window data.
			:param dict: Dict with widget name and value.
		'''
		for k, v in dict.items():

			if hasattr(self, k):

				widget = getattr(self, k)
				# TODO: Add all Gtk Widgets.
				if isinstance(widget, Gtk.Entry) or issubclass(type(widget), Gtk.Entry):
					widget.set_text(v)
				elif isinstance(widget, Gtk.Label) or issubclass(type(widget), Gtk.Label):
					widget.set_markup(v)
				elif isinstance(widget, Gtk.Button) or issubclass(type(widget), Gtk.Button):
					widget.set_label(v)
				elif isinstance(widget, Gtk.Window) or issubclass(type(widget), Gtk.Window):
					widget.set_title(v)
				elif isinstance(widget, Gtk.TextView) or issubclass(type(widget), Gtk.TextView):
					widget.set_buffer(v)
				
class GladeWindow:

	def __init__(self, glade_file, window_name):
		self.w = W()

		if GTK3:
			builder = Gtk.Builder()
			builder.add_from_file(glade_file)

			builder.connect_signals(self)

			self.window = builder.get_object(window_name)
			self.__load_widgets()
		else:
			self.wTree = Glade.XML(glade_file) 
			self.window = self.wTree.get_widget(window_name)

	def __load_widgets(self):

		for c in self.__get_all_widgets():
			name = (Gtk.Buildable.get_name(c) or '').strip()
			
			if name in ['', 'None']: continue

			if hasattr(self.w, name):
				print('** Warning: Duplicated widget name: %s **' % name)
				continue

			setattr(self.w, name, c)

	def __get_all_widgets(self):

		controls = [self.window]
		self.__get_widgets(self.window, controls)
		return controls
	
	def __get_widgets(self, widget, list):

		controls = [control for control in widget.get_children() if issubclass(type(control), Gtk.Widget)]

		for c in controls:
			list.append(c)
			if issubclass(type(c), Gtk.Container):
				self.__get_widgets(c, list)

	def show(self):
		self.window.show_all()
		Gtk.main()