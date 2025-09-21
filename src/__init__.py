# src/__init__.py

"""
Text Editor Package
===================

A simple Word Processor / Text Editor using Python + Tkinter.

Features:
- File menu: New, Open, Save, Save As, Exit
- Edit menu: Undo, Redo, Cut, Copy, Paste, Select All, Find
- Help menu: About dialog
- Main Text Area with undo support
- Keyboard shortcuts for common actions

Modules:
--------
- main.py      : Launches the application
- editor.py    : Editor class (Tkinter GUI, menus, actions)
- file_ops.py  : File operations (open/save)
- utils.py     : Helper functions (status messages, find, splash, etc.)
"""

# Keep this file lightweight — avoid heavy imports here.
# This only marks "src" as a package.
