try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='GladeBuilder',
    version='0.1.0',
    author='Alexandre Vicenzi',
    author_email='vicenzi.alexandre@gmail.com',
    packages=['gladebuilder'],
    url='https://github.com/alexandrevicenzi/gladebuilder',
    license='MIT',
    description='Easy way to get and set values/properties of Gtk2/Gtk3 widgets.',
)
