GladeWindow
===========

GladeWindow is a simple Gtk Builder for Glade files.


Why is it cool?
-----------


Well, all windows have a property called *w*, which allows you to access all widget from your window.
But this isn't everything. There's a magic method called *show*, which allow you to change the widgets content in the window, and also has a method called *clear* to reset the widget content.

Requirements
----------

* Python 3+
* Gtk 3+