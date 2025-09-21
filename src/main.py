# src/main.py

"""
Entry Point for Text Editor
===========================

Launches the Editor application with a splash screen.
"""

import tkinter as tk
from src.editor import Editor
from src.utils import show_splash


def main():
    # Initialize root window but keep it hidden initially
    root = tk.Tk()
    root.withdraw()

    # Show splash screen for 2 seconds
    show_splash(root, "assets/splash.png", duration=2000)

    # After splash, show editor
    def launch_editor():
        root.deiconify()
        editor = Editor(root)
        editor.run()

    root.after(2000, launch_editor)
    root.mainloop()


if __name__ == "__main__":
    main()
