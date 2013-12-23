#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

# A simple Glade Builder class.
# 2013 (c) Alexandre Vicenzi (vicenzi.alexandre at gmail com)

import sys
from gi.repository import Gtk

class W:

	def __init__(self):
		pass

	def clear(self):
		''' Reset window data. '''
		for name in dir(self):

			widget = getattr(self, name)

			if not issubclass(type(widget), Gtk.Widget):
				continue

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
				
				if not widget:
					continue

				self.__set_value(widget, v)

	def get(self):
		pass

	def __set_value(self, widget, value):

		if isinstance(widget, Gtk.Window) or issubclass(type(widget), Gtk.Window):
			widget.set_title(value)

		elif isinstance(widget, Gtk.AccelLabel) or issubclass(type(widget), Gtk.AccelLabel):
			widget.set_markup(v)

		elif isinstance(widget, Gtk.Label) or issubclass(type(widget), Gtk.Label):
			widget.set_markup(v)

		elif isinstance(widget, Gtk.RadioButton) or issubclass(type(widget), Gtk.RadioButton):
			widget.set_label(v)

		elif isinstance(widget, Gtk.CheckButton) or issubclass(type(widget), Gtk.CheckButton):
			widget.set_label(v)

		elif isinstance(widget, Gtk.ToggleButton) or issubclass(type(widget), Gtk.ToggleButton):
			widget.set_label(v)

		elif isinstance(widget, Gtk.Button) or issubclass(type(widget), Gtk.Button):
			widget.set_label(v)

		elif isinstance(widget, Gtk.LinkButton) or issubclass(type(widget), Gtk.LinkButton):
			widget.set_label(v)

		elif isinstance(widget, Gtk.ScaleButton) or issubclass(type(widget), Gtk.ScaleButton):
			widget.set_label(v)
		
		elif isinstance(widget, Gtk.VolumeButton) or issubclass(type(widget), Gtk.VolumeButton):
			widget.set_label(v)

		elif isinstance(widget, Gtk.Window) or issubclass(type(widget), Gtk.Window):
			widget.set_label(v)
		
		elif isinstance(widget, Gtk.Calendar) or issubclass(type(widget), Gtk.Calendar):
			widget.set_label(v)
		
		elif isinstance(widget, Gtk.Entry) or issubclass(type(widget), Gtk.Entry):
			widget.set_text(v)

		elif isinstance(widget, Gtk.SpinButton) or issubclass(type(widget), Gtk.SpinButton):
			widget.set_value(v)

		elif isinstance(widget, Gtk.ProgressBar) or issubclass(type(widget), Gtk.ProgressBar):
			widget.set_label(v)

		elif isinstance(widget, Gtk.Spinner) or issubclass(type(widget), Gtk.Spinner):
			widget.set_label(v)

		elif isinstance(widget, Gtk.ComboBox) or issubclass(type(widget), Gtk.ComboBox):
			widget.set_label(v)
		
		elif isinstance(widget, Gtk.ComboBoxText) or issubclass(type(widget), Gtk.ComboBoxText):
			widget.set_label(v)
		
		elif isinstance(widget, Gtk.Scale) or issubclass(type(widget), Gtk.Scale):
			widget.set_label(v)

		elif isinstance(widget, Gtk.TreeView) or issubclass(type(widget), Gtk.TreeView):
			widget.set_buffer(v)
		
		elif isinstance(widget, Gtk.TextView) or issubclass(type(widget), Gtk.TextView):
			widget.set_label(v)

		else:
			print('Object not supported: ' + type(widget))
		
				
class GladeWindow:

	def __init__(self, glade_file, window_name):
		self.w = W()

		builder = Gtk.Builder()
		builder.add_from_file(glade_file)
		builder.connect_signals(self)
		self.window = builder.get_object(window_name)

		self.__load_widgets()

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