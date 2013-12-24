GladeBuilder
===========

GladeBuilder is a simple Gtk Builder for Glade files.


Why is it cool?
-----------


Well, all windows have a property called `w`, which allows you to access all widgets from your window easily.

    MyWindow.w.label1.set_label('Foo')

But this isn't everything. There's a magic method called `show`, which allow you to change the widgets content in the window.

    MyWindow.w.show({'label1': 'Some Text', 'checkbutton1': True})

A method called `get` to get all widgets content.

    print(MyWindow.w.get())
    
    >>> {'label1': 'Some Text', 'checkbutton1': True}

And also has a method called `clear` to reset the widget content.

   MyWindow.w.clear()