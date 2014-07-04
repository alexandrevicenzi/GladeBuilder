GladeBuilder [![Build Status](https://travis-ci.org/alexandrevicenzi/GladeBuilder.svg?branch=master)](https://travis-ci.org/alexandrevicenzi/GladeBuilder)
===========

GladeBuilder is a simple Gtk Builder for Glade files.


## Why is it cool?


Well, all windows have a property called `w`, which allows you to access all widgets from your window easily.

    MyWindow.w.label1.set_label('Foo')

But this isn't everything. There's a magic method called `show`, which allow you to change the widgets content in the window.

    MyWindow.w.show({'label1': 'Some Text', 'checkbutton1': True})

A method called `get` to get all widgets content.

    print(MyWindow.w.get())

    >>> {'label1': 'Some Text', 'checkbutton1': True}

And also has a method called `clear` to reset the widget content.

    MyWindow.w.clear()

## Why this?

Sometimes is painfull to use Gtk. So I added some cool functions to work with widgets. Doens't support all widgets yet.

## Want some examples?

Take a look at */examples*.

## Want to contribute?

Feel free to fork this repo and send me pull requests.

What I want to do is add more helper functions to use Gtk more easier. For example, create more functions to work with TreeView, Dialogs, Calendar or others in a good way.
