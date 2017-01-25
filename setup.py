# installer script for deps

#!/usr/bin/env python

from distutils.core import setup

setup(name='gcc.py.introspector',
      version='0.000000001',
      description='Python Parsing of GCC Tree Dump Utilities',
      author='James Michael DuPont',
      author_email='jamesmikedupont@gmail.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['gcc.tree'],
     )
