# src/utils.py

"""
Utilities Module for Text Editor
================================

Provides helper functions for:
- Status bar updates
- Message dialogs
- Find dialog
- Splash screen
"""

import tkinter as tk
from tkinter import simpledialog, messagebox


def show_status_message(status_var, message, timeout=3000):
    """
    Update a Tkinter StringVar (status bar) temporarily.

    Args:
        status_var: tk.StringVar linked to a Label
        message: str, message to display
        timeout: int, milliseconds to revert to empty string (default 3000)
    """
    status_var.set(message)
    status_var._root().after(timeout, lambda: status_var.set(""))


def show_info(title, message, parent=None):
    """Show an info message box."""
    messagebox.showinfo(title, message, parent=parent)


def show_warning(title, message, parent=None):
    """Show a warning message box."""
    messagebox.showwarning(title, message, parent=parent)


def show_error(title, message, parent=None):
    """Show an error message box."""
    messagebox.showerror(title, message, parent=parent)


def ask_find_text(parent, title="Find"):
    """
    Show a simple Find dialog and return the search query.

    Args:
        parent: Tkinter root or Toplevel

    Returns:
        str: search string entered by user, or None if cancelled
    """
    return simpledialog.askstring(title, "Find:", parent=parent)


def show_splash(root, image_path="assets/splash.png", duration=2000):
    """
    Display a splash screen before launching the main editor.

    Args:
        root: Tk root window (hidden initially)
        image_path: str, path to splash image
        duration: int, milliseconds to show splash before auto-closing
    """
    splash = tk.Toplevel(root)
    splash.overrideredirect(True)  # Remove title bar
    splash.configure(bg="white")

    try:
        img = tk.PhotoImage(file=image_path)
        w, h = img.width(), img.height()
        # Center splash window on screen
        x = (splash.winfo_screenwidth() // 2) - (w // 2)
        y = (splash.winfo_screenheight() // 2) - (h // 2)
        splash.geometry(f"{w}x{h}+{x}+{y}")

        label = tk.Label(splash, image=img, borderwidth=0)
        label.image = img  # Keep reference
        label.pack()
    except Exception:
        # If image missing, fallback to text
        label = tk.Label(splash, text="ashok's text editor", font=("Arial", 20, "bold"), bg="white")
        label.pack(padx=20, pady=20)

    # Auto-close after given duration
    root.after(duration, splash.destroy)
