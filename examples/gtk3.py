#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

# 2013 Alexandre Vicenzi (vicenzi.alexandre at gmail com)

from datetime import datetime
from gi.repository import Gtk, Pango
from gladebuilder import GladeWindow

class MyApp(GladeWindow):

    def __init__(self):
        GladeWindow.__init__(self, 'gtk3.glade', 'main')

    def on_open_clicked(self, *args):
        Win = MyWindow()

        Win.w.scale1.set_range(0.0, 1)
        Win.w.scale2.set_range(0.0, 1)
        Win.w.spinbutton1.set_range(0.0, 1)


        distributions = ["Fedora", "Sabayon", "Debian", "Arch Linux", "Crunchbang"]
        liststore = Gtk.ListStore(str)
        for item in distributions:
            liststore.append([item])

        Win.w.comboboxtext1.set_model(liststore)

        cell = Gtk.CellRendererText()
        Win.w.combobox1.pack_start(cell, True)
        Win.w.combobox1.add_attribute(cell, "text", 0)
        Win.w.combobox1.set_model(liststore)

        textbuffer = Gtk.TextBuffer()
        #textbuffer.set_text('this\nis\na\nmultiline\ntext')
        Win.w.textview1.set_buffer(textbuffer)

        """
        column = Gtk.TreeViewColumn('Column 0')
        column1 = Gtk.TreeViewColumn('Column 1')
        Win.w.treeview1.append_column(column)
        Win.w.treeview1.append_column(column1)
        cell = Gtk.CellRendererText()
        column.pack_start(cell, True)
        column.add_attribute(cell, 'text', 0)
        Win.w.treeview1.set_search_column(0)
        column.set_sort_column_id(0)
        Win.w.treeview1.set_reorderable(True)
        """

        columns = ["First Name",
                    "Last Name",
                    "Phone Number"]

        phonebook = [["Jurg", "Billeter", "555-0123"],
                    ["Johannes", "Schmid", "555-1234"],
                    ["Julita", "Inca", "555-2345"],
                    ["Javier", "Jardon", "555-3456"],
                    ["Jason", "Clinton", "555-4567"],
                    ["Random J.", "Hacker", "555-5678"]]

        for i in range(len(columns)):
            cell = Gtk.CellRendererText()
            if i == 0:
                cell.props.weight_set = True
                cell.props.weight = Pango.Weight.BOLD
            col = Gtk.TreeViewColumn(columns[i], cell, text=i)
            Win.w.treeview1.append_column(col)

        Win.w.treeview1.set_model(Gtk.ListStore(str, str, str))

        dict = {
            "window1": "Example GTK 3",
            "button1": "Click",
            "togglebutton1": "Click me too",
            "checkbutton1": True,
            "entry1": "Some text",
            "spinbutton1": 0.2,
            "combobox1": 2,
            "comboboxtext1": 3,
            "label1": "<b>Bold label</b>",
            "linkbutton1": "https://www.google.com",
            "accellabel1": "<i>Italic accellabel</i>",
            "scalebutton1": 30,
            "volumebutton1": 0.8,
            "scale1": 0.5,
            "scale2": 0.6,
            "calendar1": datetime.today(),
            "treeview1": phonebook,
            "textview1": 'this\nis\na\nmultiline\ntext',
            "radiobutton1": False,
            "radiobutton2": True,
            "radiobutton3": True, # The last one wins.
            "spinner1": True,
            "progressbar1": 0.5,
        }

        Win.w.show(dict)

        dict = {
            "checkbutton1": "Is checked",
            'volumebutton1': 'Volume',
            'scalebutton1': 'Scale button',
            'linkbutton1': 'Go to google.com',
            'radiobutton1': 'First',
            'radiobutton2': 'Second',
            'radiobutton3': 'Third',
        }

        Win.w.show(dict)

        #print(Win.w.get())

        Win.show()

    def on_close(self, *args):
        self.close()
        Gtk.main_quit()

class MyWindow(GladeWindow):

    def __init__(self):
        GladeWindow.__init__(self, 'gtk3.glade', 'window1')

    def on_reset_clicked(self, *args):
        self.w.clear()

    def on_close(self, *args):
        self.close()

if __name__ == "__main__":

    M = MyApp()
    M.show()

    Gtk.main()