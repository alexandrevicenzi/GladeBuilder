#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

# The MIT License (MIT)

# Copyright (c) 2013 Alexandre Vicenzi (vicenzi.alexandre at gmail com)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

__author__ = 'Alexandre Vicenzi'
__version__ = '0.1.0'
__license__ = 'MIT'

import re
import sys

from datetime import datetime

GTK2 = 2
GTK3 = 3

gtk_version = None

try:
    from gi.repository import Gtk, GObject
    from gi import require_version
    require_version('Gtk', '3.0')
    gtk_version = GTK3
except ImportError as e:
    try:
        import pygtk
        pygtk.require('2.0')

        import gtk as Gtk
        import gtk.glade as Glade
        gtk_version = GTK2
    except ImportError as e:
        raise e

class W:

    def __init__(self):
        self.defaults = {}
        self.__set_defaults()

    def __set_defaults(self):
        self.set_default(Gtk.Entry, '')
        self.set_default(Gtk.TextView, '')
        self.set_default(Gtk.RadioButton, False)
        self.set_default(Gtk.CheckButton, False)
        self.set_default(Gtk.Spinner, False)
        self.set_default(Gtk.ComboBox, -1)

        if gtk_version >= GTK3:
            self.set_default(Gtk.ComboBoxText, -1)

        self.set_default(Gtk.ProgressBar, 0)
        self.set_default(Gtk.VolumeButton, 0)
        self.set_default(Gtk.Scale, 0)
        self.set_default(Gtk.ScaleButton, 0)
        self.set_default(Gtk.SpinButton, 0)
        self.set_default(Gtk.TreeView, [])
        self.set_default(Gtk.Calendar, datetime.today())

    def set_default(self, widget_type, value):
        self.defaults[widget_type] = value

    def clear(self):
        ''' Reset window data. '''

        for name in dir(self):

            widget = getattr(self, name)

            if not issubclass(type(widget), Gtk.Widget):
                continue

            default = self.defaults.get(type(widget))

            if not default is None:
                self.__set_value(widget, default)

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
        ''' Get window data. '''

        values = {}

        for name in dir(self):

            widget = getattr(self, name)

            if not issubclass(type(widget), Gtk.Widget):
                continue

            value = self.__get_value(widget)

            if not value is None:
                values[name] = value

        return values

    def __set_value(self, widget, v):

        if isinstance(widget, Gtk.Window) or issubclass(type(widget), Gtk.Window):
            widget.set_title(v)

        elif isinstance(widget, Gtk.AccelLabel) or \
             issubclass(type(widget), Gtk.AccelLabel) or \
             isinstance(widget, Gtk.Label) or \
             issubclass(type(widget), Gtk.Label):
            widget.set_markup(v)

        elif isinstance(widget, Gtk.RadioButton) or \
             issubclass(type(widget), Gtk.RadioButton) or \
             isinstance(widget, Gtk.CheckButton) or \
             issubclass(type(widget), Gtk.CheckButton):
            if type(v) == str:
                widget.set_label(v)
            else:
                widget.set_active(v)

        elif isinstance(widget, Gtk.LinkButton) or issubclass(type(widget), Gtk.LinkButton):
            if self.__is_valid_uri(v):
                widget.set_uri(v)
            else:
                widget.set_label(v)

        elif isinstance(widget, Gtk.ScaleButton) or \
             issubclass(type(widget), Gtk.ScaleButton) or \
             isinstance(widget, Gtk.VolumeButton) or \
             issubclass(type(widget), Gtk.VolumeButton):
            if type(v) == str:
                widget.set_label(v)
            else:
                widget.set_value(v)

        elif isinstance(widget, Gtk.ToggleButton) or \
             issubclass(type(widget), Gtk.ToggleButton) or \
             isinstance(widget, Gtk.Button) or \
             issubclass(type(widget), Gtk.Button):
            widget.set_label(v)

        elif isinstance(widget, Gtk.Calendar) or issubclass(type(widget), Gtk.Calendar):
            widget.select_day(v.day)
            widget.select_month(v.month, v.year)

        elif isinstance(widget, Gtk.SpinButton) or issubclass(type(widget), Gtk.SpinButton):
            widget.set_value(v)

        elif isinstance(widget, Gtk.Entry) or issubclass(type(widget), Gtk.Entry):
            widget.set_text(v)

        elif isinstance(widget, Gtk.ProgressBar) or issubclass(type(widget), Gtk.ProgressBar):
            widget.set_fraction(v)

        elif isinstance(widget, Gtk.Spinner) or issubclass(type(widget), Gtk.Spinner):
            widget.active = v

            if v:
                widget.start()
            else:
                widget.stop()

        elif gtk_version >= GTK3 and (isinstance(widget, Gtk.ComboBoxText) or issubclass(type(widget), Gtk.ComboBoxText)):
            widget.set_active(v)

        elif isinstance(widget, Gtk.ComboBox) or issubclass(type(widget), Gtk.ComboBox):
            widget.set_active(v)

        elif isinstance(widget, Gtk.Scale) or issubclass(type(widget), Gtk.Scale):
            widget.set_value(v)

        elif isinstance(widget, Gtk.TreeView) or issubclass(type(widget), Gtk.TreeView):
            widget.get_model().clear()
            for cells in v:
                widget.get_model().append(cells)

        elif isinstance(widget, Gtk.TextView) or issubclass(type(widget), Gtk.TextView):
            widget.get_buffer().set_text(v)

        else:
            print('** Warning: Object not supported: ' + widget.__class__.__name__)

    def __get_value(self, widget):

        if isinstance(widget, Gtk.Window) or issubclass(type(widget), Gtk.Window):
            return widget.get_title()

        elif isinstance(widget, Gtk.AccelLabel) or issubclass(type(widget), Gtk.AccelLabel):
            return widget.get_label()

        elif isinstance(widget, Gtk.Label) or issubclass(type(widget), Gtk.Label):
            return widget.get_label()

        elif isinstance(widget, Gtk.RadioButton) or issubclass(type(widget), Gtk.RadioButton):
            return widget.get_active()

        elif isinstance(widget, Gtk.CheckButton) or issubclass(type(widget), Gtk.CheckButton):
            return widget.get_active()

        elif isinstance(widget, Gtk.LinkButton) or issubclass(type(widget), Gtk.LinkButton):
            return widget.get_uri()

        elif isinstance(widget, Gtk.ScaleButton) or issubclass(type(widget), Gtk.ScaleButton):
            return widget.get_value()

        elif isinstance(widget, Gtk.VolumeButton) or issubclass(type(widget), Gtk.VolumeButton):
            return widget.get_value()

        elif isinstance(widget, Gtk.ToggleButton) or issubclass(type(widget), Gtk.ToggleButton):
            return widget.get_label()

        elif isinstance(widget, Gtk.Button) or issubclass(type(widget), Gtk.Button):
            return widget.get_label()

        elif isinstance(widget, Gtk.Calendar) or issubclass(type(widget), Gtk.Calendar):
            return widget.get_date()

        elif isinstance(widget, Gtk.SpinButton) or issubclass(type(widget), Gtk.SpinButton):
            return widget.get_value()

        elif isinstance(widget, Gtk.Entry) or issubclass(type(widget), Gtk.Entry):
            return widget.get_text()

        elif isinstance(widget, Gtk.ProgressBar) or issubclass(type(widget), Gtk.ProgressBar):
            return widget.get_fraction()

        elif isinstance(widget, Gtk.Spinner) or issubclass(type(widget), Gtk.Spinner):
            return widget.active

        elif gtk_version >= GTK3 and (isinstance(widget, Gtk.ComboBoxText) or issubclass(type(widget), Gtk.ComboBoxText)):
            return widget.get_active()

        elif isinstance(widget, Gtk.ComboBox) or issubclass(type(widget), Gtk.ComboBox):
            return widget.get_active()

        elif isinstance(widget, Gtk.Scale) or issubclass(type(widget), Gtk.Scale):
            return widget.get_value()

        elif isinstance(widget, Gtk.TreeView) or issubclass(type(widget), Gtk.TreeView):
            return widget.get_model() # TODO:

        elif isinstance(widget, Gtk.TextView) or issubclass(type(widget), Gtk.TextView):
            start = widget.get_buffer().get_start_iter()
            end = widget.get_buffer().get_end_iter()
            return widget.get_buffer().get_text(start, end, True)

        else:
            print('** Warning: Object not supported: ' + widget.__class__.__name__)

    def __is_valid_uri(self, uri):

        regex = re.compile(r'^(?:http|ftp)s?://(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|'\
            '[A-Z0-9-]{2,}\.?)|localhost|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?::\d+)?(?:/?|'\
            '[/?]\S+)$', re.IGNORECASE)

        return regex.match(uri)

class GladeWindow:

    def __init__(self, glade_file, window_name):
        self.w = W()
        self.name = window_name

        if gtk_version >= GTK3:
            builder = Gtk.Builder()
            builder.add_from_file(glade_file)
            #builder.connect_signals(self)
            builder.connect_signals_full(self.__full_callback, self)
            self.window = builder.get_object(window_name)
        elif gtk_version == GTK2:
            tree = Glade.XML(glade_file)
            tree.signal_autoconnect(self)
            self.window = tree.get_widget(window_name)
        else:
            raise Exception('GTK version not supported.')

        if not self.window:
            raise Exception('Failed to open XML file.')

        self.__load_widgets()

    def show(self):
        self.window.show_all()

    def close(self):
        self.window.hide()

    def __load_widgets(self):

        for c in self.__get_all_widgets():

            if gtk_version >= GTK3:
                name = (Gtk.Buildable.get_name(c) or '').strip()
            else:
                name = (c.name or Gtk.Buildable.get_name(c) or '').strip()

            if name in ['', 'None']: continue

            if hasattr(self.w, name):
                print('** Warning: Duplicated widget name: %s **' % name)
                continue

            setattr(self.w, name, c)

    def __get_all_widgets(self):

        controls = [self.window]
        self.__get_widgets(self.window, controls)
        return sorted(controls)

    def __get_widgets(self, widget, list):

        controls = [control for control in widget.get_children() if issubclass(type(control), Gtk.Widget)]

        for c in controls:
            list.append(c)

            if issubclass(type(c), Gtk.Container):
                self.__get_widgets(c, list)

    def __full_callback(self, builder, gobj, signal_name, handler_name, connect_obj, flags, obj_or_map):
        # Gtk+3 only.

        # This code is from Gtk.py
        # https://git.gnome.org/browse/pygobject/tree/gi/overrides/Gtk.py
        # TODO: Find a better way to connect signals from a specific window.

        if gtk_version < GTK3:
            return

        handler = None

        if isinstance(obj_or_map, dict):
            handler = obj_or_map.get(handler_name, None)
        else:
            handler = getattr(obj_or_map, handler_name, None)

        if handler is None:
            #raise AttributeError('Handler %s not found' % handler_name)
            return

        if not callable(handler):
            raise TypeError('Handler %s is not a method or function' % handler_name)

        after = flags & GObject.ConnectFlags.AFTER

        if connect_obj is not None:
            if after:
                gobj.connect_object_after(signal_name, handler, connect_obj)
            else:
                gobj.connect_object(signal_name, handler, connect_obj)
        else:
            if after:
                gobj.connect_after(signal_name, handler)
            else:
                gobj.connect(signal_name, handler)